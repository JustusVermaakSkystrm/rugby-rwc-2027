import threading
from datetime import datetime, timedelta, timezone

import pyarrow.parquet as pq
import pytest

from ig_logger.storage import COLUMNS, SCHEMA, TickWriter


def make_row(epic="TEST.EPIC", when=None, **overrides):
    row = dict.fromkeys(COLUMNS)
    row.update(
        recv_ts=when or datetime(2026, 9, 15, 10, 30, tzinfo=timezone.utc),
        epic=epic,
        bid=100.0,
        ofr=100.5,
    )
    row.update(overrides)
    return row


def test_partitions_by_epic_and_date(tmp_path):
    writer = TickWriter(tmp_path, flush_rows=10_000, flush_seconds=1e9)
    day1 = datetime(2026, 9, 15, 10, 0, tzinfo=timezone.utc)
    day2 = day1 + timedelta(days=1)

    writer.add(make_row("A", day1))
    writer.add(make_row("A", day2))
    writer.add(make_row("B", day1))
    writer.close()

    assert (tmp_path / "A" / "2026-09-15").is_dir()
    assert (tmp_path / "A" / "2026-09-16").is_dir()
    assert (tmp_path / "B" / "2026-09-15").is_dir()


def test_no_temp_files_survive(tmp_path):
    writer = TickWriter(tmp_path, flush_rows=1)
    writer.add(make_row())
    writer.close()
    assert list(tmp_path.rglob("*.tmp")) == []
    assert len(list(tmp_path.rglob("*.parquet"))) == 1


def test_schema_is_stable_when_a_column_is_all_null(tmp_path):
    """The reason for pinning the schema: an all-null column must still be
    typed, or later batches refuse to concatenate with it."""
    writer = TickWriter(tmp_path, flush_rows=1)
    writer.add(make_row(ltv=None, utm=None))          # ltv/utm entirely absent
    writer.add(make_row(ltv=42, utm=datetime(2026, 9, 15, tzinfo=timezone.utc)))
    writer.close()

    files = sorted(tmp_path.rglob("*.parquet"))
    assert len(files) == 2
    for path in files:
        assert pq.read_table(path).schema.equals(SCHEMA)
    # and the two parts read together, which is the thing that actually breaks
    combined = pq.read_table(files, schema=SCHEMA)
    assert combined.num_rows == 2


def test_flush_is_triggered_by_row_count(tmp_path):
    writer = TickWriter(tmp_path, flush_rows=5, flush_seconds=1e9)
    for _ in range(4):
        writer.add(make_row())
    assert writer.rows_written == 0        # not yet
    writer.add(make_row())
    assert writer.rows_written == 5        # fifth row tips it over


def test_close_flushes_partial_buffer(tmp_path):
    writer = TickWriter(tmp_path, flush_rows=1_000_000, flush_seconds=1e9)
    for _ in range(3):
        writer.add(make_row())
    assert writer.rows_written == 0
    writer.close()
    assert writer.rows_written == 3
    assert pq.read_table(list(tmp_path.rglob("*.parquet"))).num_rows == 3


def test_concurrent_writers_lose_nothing(tmp_path):
    """Lightstreamer delivers from several threads; nothing may be dropped or
    written twice."""
    writer = TickWriter(tmp_path, flush_rows=50, flush_seconds=1e9)
    per_thread, threads = 200, 8

    def hammer(n):
        for i in range(per_thread):
            writer.add(make_row(epic=f"E{n}", ltv=i))

    workers = [threading.Thread(target=hammer, args=(n,)) for n in range(threads)]
    for w in workers:
        w.start()
    for w in workers:
        w.join()
    writer.close()

    total = pq.read_table(list(tmp_path.rglob("*.parquet")), schema=SCHEMA).num_rows
    assert total == per_thread * threads


def test_values_round_trip(tmp_path):
    writer = TickWriter(tmp_path, flush_rows=1)
    utm = datetime(2026, 9, 15, 10, 30, 15, tzinfo=timezone.utc)
    writer.add(make_row(bid=1.2345, ofr=1.2347, ltv=7, utm=utm))
    writer.close()

    table = pq.read_table(list(tmp_path.rglob("*.parquet"))).to_pylist()
    assert table[0]["bid"] == pytest.approx(1.2345)
    assert table[0]["ofr"] == pytest.approx(1.2347)
    assert table[0]["ltv"] == 7
    assert table[0]["utm"] == utm
