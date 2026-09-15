"""Merge the many small part files into one Parquet per epic per day.

Run it when nothing is recording that day's data - a nightly cron after the
close, or by hand. Today's partition is skipped by default precisely because
the recorder is probably still writing into it.
"""

import argparse
import logging
import os
from datetime import date
from pathlib import Path

import pyarrow.parquet as pq

from .storage import SCHEMA

logger = logging.getLogger(__name__)

COMPACT_NAME = "compacted.parquet"


def partitions(data_dir):
    """Yield (epic, date, directory) for every partition holding part files."""
    for epic_dir in sorted(p for p in Path(data_dir).iterdir() if p.is_dir()):
        for date_dir in sorted(epic_dir.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]")):
            if any(date_dir.glob("part-*.parquet")):
                yield epic_dir.name, date_dir.name, date_dir


def compact_partition(directory, dedupe=True):
    """Merge one partition. Returns the number of rows in the result.

    Existing compacted output is folded back in, so running twice is safe and
    a later run picks up parts written after the first.
    """
    parts = sorted(directory.glob("part-*.parquet"))
    if not parts:
        return 0

    sources = list(parts)
    existing = directory / COMPACT_NAME
    if existing.exists():
        sources.append(existing)

    table = pq.read_table(sources, schema=SCHEMA)
    table = table.sort_by([("recv_ts", "ascending")])
    if dedupe:
        # exact duplicate rows appear when a recorder is restarted and IG
        # re-sends a snapshot, or if two recorders overlap
        before = table.num_rows
        table = table.group_by(SCHEMA.names).aggregate([]).sort_by(
            [("recv_ts", "ascending")]
        )
        if table.num_rows != before:
            logger.info("dropped %d duplicate rows", before - table.num_rows)

    tmp = directory / (COMPACT_NAME + ".tmp")
    pq.write_table(table, tmp, compression="zstd")
    os.replace(tmp, existing)

    for part in parts:
        part.unlink()

    logger.info("compacted %d parts into %s (%d rows)", len(parts), existing, table.num_rows)
    return table.num_rows


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data_dir", nargs="?", default="data")
    parser.add_argument(
        "--include-today",
        action="store_true",
        help="also compact today's partition (only safe if nothing is recording)",
    )
    parser.add_argument("--no-dedupe", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(levelname)-7s %(message)s")

    today = date.today().isoformat()
    total = 0
    for epic, day, directory in partitions(args.data_dir):
        if day == today and not args.include_today:
            logger.info("skipping today's partition %s/%s", epic, day)
            continue
        total += compact_partition(directory, dedupe=not args.no_dedupe)
    logger.info("total rows after compaction: %d", total)
    return total


if __name__ == "__main__":
    main()
