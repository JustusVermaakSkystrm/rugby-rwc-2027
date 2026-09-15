from datetime import datetime, timedelta, timezone
from pathlib import Path

import pyarrow.parquet as pq

from ig_logger.compact import COMPACT_NAME, compact_partition, partitions
from ig_logger.storage import COLUMNS, SCHEMA, TickWriter

BASE = datetime(2026, 9, 15, 10, 0, tzinfo=timezone.utc)


def write_parts(tmp_path, n_parts=3, per_part=10, epic="TEST.A"):
    writer = TickWriter(tmp_path, flush_rows=per_part, flush_seconds=1e9)
    for part in range(n_parts):
        for i in range(per_part):
            row = dict.fromkeys(COLUMNS)
            row.update(
                recv_ts=BASE + timedelta(seconds=part * per_part + i),
                epic=epic,
                bid=100.0 + i,
                ofr=100.5 + i,
            )
            writer.add(row)
    writer.close()
    return writer


def test_partitions_are_discovered(tmp_path):
    write_parts(tmp_path)
    found = list(partitions(tmp_path))
    assert len(found) == 1
    epic, day, directory = found[0]
    assert (epic, day) == ("TEST.A", "2026-09-15")
    assert directory.is_dir()


def test_parts_are_merged_and_removed(tmp_path):
    write_parts(tmp_path, n_parts=3, per_part=10)
    directory = tmp_path / "TEST.A" / "2026-09-15"
    assert len(list(directory.glob("part-*.parquet"))) == 3

    rows = compact_partition(directory)

    assert rows == 30
    assert list(directory.glob("part-*.parquet")) == []
    assert (directory / COMPACT_NAME).exists()
    assert pq.read_table(directory / COMPACT_NAME).num_rows == 30


def test_output_is_sorted_by_arrival(tmp_path):
    write_parts(tmp_path)
    directory = tmp_path / "TEST.A" / "2026-09-15"
    compact_partition(directory)

    stamps = pq.read_table(directory / COMPACT_NAME).column("recv_ts").to_pylist()
    assert stamps == sorted(stamps)


def test_running_twice_folds_in_later_parts(tmp_path):
    """A second run must not discard what the first one compacted - the
    recorder keeps writing parts after a compaction."""
    write_parts(tmp_path, n_parts=2, per_part=10)
    directory = tmp_path / "TEST.A" / "2026-09-15"
    assert compact_partition(directory) == 20

    # more data arrives for the same day, at later timestamps
    writer = TickWriter(tmp_path, flush_rows=5, flush_seconds=1e9)
    for i in range(5):
        row = dict.fromkeys(COLUMNS)
        row.update(recv_ts=BASE + timedelta(hours=1, seconds=i), epic="TEST.A", bid=1.0)
        writer.add(row)
    writer.close()

    assert compact_partition(directory) == 25
    assert pq.read_table(directory / COMPACT_NAME).num_rows == 25


def test_compaction_is_idempotent_with_no_new_parts(tmp_path):
    write_parts(tmp_path)
    directory = tmp_path / "TEST.A" / "2026-09-15"
    compact_partition(directory)
    assert compact_partition(directory) == 0          # nothing left to do
    assert pq.read_table(directory / COMPACT_NAME).num_rows == 30


def test_exact_duplicates_are_dropped(tmp_path):
    """Restarting the recorder can re-receive a snapshot, producing byte-identical
    rows. Genuinely distinct ticks differ in recv_ts and must survive."""
    writer = TickWriter(tmp_path, flush_rows=2, flush_seconds=1e9)
    duplicate = dict.fromkeys(COLUMNS)
    duplicate.update(recv_ts=BASE, epic="TEST.A", bid=100.0, ofr=100.5)
    writer.add(dict(duplicate))
    writer.add(dict(duplicate))
    distinct = dict(duplicate)
    distinct["recv_ts"] = BASE + timedelta(microseconds=1)
    writer.add(distinct)
    writer.close()

    directory = tmp_path / "TEST.A" / "2026-09-15"
    assert compact_partition(directory, dedupe=True) == 2


def test_multiple_epics_and_days_stay_separate(tmp_path):
    write_parts(tmp_path, epic="TEST.A")
    writer = TickWriter(tmp_path, flush_rows=5, flush_seconds=1e9)
    for i in range(5):
        row = dict.fromkeys(COLUMNS)
        row.update(recv_ts=BASE + timedelta(days=1, seconds=i), epic="TEST.B", bid=1.0)
        writer.add(row)
    writer.close()

    found = {(epic, day) for epic, day, _ in partitions(tmp_path)}
    assert found == {("TEST.A", "2026-09-15"), ("TEST.B", "2026-09-16")}

    for _, _, directory in partitions(tmp_path):
        compact_partition(directory)

    table = pq.read_table(sorted(Path(tmp_path).rglob("*.parquet")), schema=SCHEMA)
    assert table.num_rows == 35
