"""Buffered, crash-safe Parquet writer for tick data.

Design notes, since the reasons matter more than the code:

* One fixed schema for every file. If you let Parquet infer types per batch,
  a column that happens to be all-null in one batch becomes `null` type and
  later refuses to concatenate with the same column typed float elsewhere.

* Many small part files rather than one appended file. Parquet cannot be
  appended to, and a part file that is already closed survives a crash.
  `compact.py` merges them later, when nothing is being written.

* Every file is written to `.tmp` and then renamed. `os.replace` is atomic on
  POSIX, so a reader never sees a half-written file and a crash mid-write
  leaves a stray .tmp rather than a corrupt part.

* Laid out as `<EPIC>/<YYYY-MM-DD>/part-*.parquet`, with plain directory
  names rather than Hive-style `epic=`/`date=`. Hive naming would make pyarrow
  synthesise its own dictionary-typed `epic` partition column, which then
  refuses to merge with the real string `epic` column stored in the files.
  Keeping the epic inside the file matters more: a part file that gets moved
  or copied is still self-describing. The cost is no partition-level predicate
  pushdown, which at this data size is not worth the footgun.
"""

import itertools
import logging
import os
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

logger = logging.getLogger(__name__)

# recv_ts is OUR clock; utm is IG's tick timestamp. Keep both: utm can be null
# or lag, and you cannot reconstruct arrival order after the fact.
SCHEMA = pa.schema(
    [
        ("recv_ts", pa.timestamp("us", tz="UTC")),
        ("epic", pa.string()),
        ("utm", pa.timestamp("ms", tz="UTC")),
        ("bid", pa.float64()),
        ("ofr", pa.float64()),
        ("ltp", pa.float64()),
        ("ltv", pa.int64()),
        ("ttv", pa.int64()),
        ("day_open_mid", pa.float64()),
        ("day_net_chg_mid", pa.float64()),
        ("day_perc_chg_mid", pa.float64()),
        ("day_high", pa.float64()),
        ("day_low", pa.float64()),
    ]
)

COLUMNS = [f.name for f in SCHEMA]


class TickWriter:
    """Accumulates rows and flushes them to partitioned Parquet parts.

    Thread-safe: `add` may be called from any thread, though in this project a
    single writer thread drains the queue so disk latency never blocks the
    Lightstreamer callback.
    """

    def __init__(self, data_dir, flush_rows=5_000, flush_seconds=30.0):
        self.data_dir = Path(data_dir)
        self.flush_rows = flush_rows
        self.flush_seconds = flush_seconds

        self._buffer = []
        self._lock = threading.Lock()
        self._last_flush = time.monotonic()
        # itertools.count is atomic under CPython, so two threads flushing at
        # once cannot land on the same part filename
        self._seq = itertools.count(1)

        self.rows_written = 0
        self.files_written = 0

    def add(self, row):
        with self._lock:
            self._buffer.append(row)
            due = (
                len(self._buffer) >= self.flush_rows
                or time.monotonic() - self._last_flush >= self.flush_seconds
            )
        if due:
            self.flush()

    def maybe_flush(self):
        """Flush if the time-based deadline has passed. Call periodically so a
        quiet market still gets its handful of rows written out."""
        with self._lock:
            due = (
                self._buffer
                and time.monotonic() - self._last_flush >= self.flush_seconds
            )
        if due:
            self.flush()

    def flush(self):
        with self._lock:
            rows, self._buffer = self._buffer, []
            self._last_flush = time.monotonic()
        if not rows:
            return 0

        # group by partition so each part file belongs to exactly one
        # epic/date, which is what makes the directory layout meaningful
        groups = {}
        for row in rows:
            key = (row["epic"], row["recv_ts"].astimezone(timezone.utc).date().isoformat())
            groups.setdefault(key, []).append(row)

        for (epic, date), group in groups.items():
            self._write_part(epic, date, group)

        self.rows_written += len(rows)
        return len(rows)

    def _write_part(self, epic, date, rows):
        directory = self.data_dir / epic / date
        directory.mkdir(parents=True, exist_ok=True)

        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
        name = f"part-{stamp}-{os.getpid()}-{next(self._seq):06d}.parquet"
        final = directory / name
        tmp = directory / (name + ".tmp")

        table = pa.Table.from_pydict(
            {col: [row.get(col) for row in rows] for col in COLUMNS},
            schema=SCHEMA,
        )
        pq.write_table(table, tmp, compression="zstd")
        os.replace(tmp, final)   # atomic: readers see all of it or none of it

        self.files_written += 1
        logger.debug("wrote %d rows to %s", len(rows), final)

    def close(self):
        self.flush()
        logger.info(
            "writer closed: %d rows in %d files under %s",
            self.rows_written,
            self.files_written,
            self.data_dir,
        )
