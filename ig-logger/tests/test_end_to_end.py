"""Whole-pipeline tests against the synthetic feed.

These are the tests that matter for a recorder: they prove that ticks handed
to the sink end up on disk, that shutdown does not lose the buffer, and that a
feed which dies gets rebuilt.
"""

import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import pyarrow.parquet as pq

from ig_logger.config import Settings
from ig_logger.record import Recorder
from ig_logger.replay import ReplayFeed, intraday_intensity
from ig_logger.storage import SCHEMA


def settings_for(tmp_path, **overrides):
    kwargs = dict(
        username="u",
        password="p",
        api_key="k",
        acc_type="DEMO",
        acc_number="ABC12",
        epics=["TEST.A", "TEST.B"],
        data_dir=Path(tmp_path),
        flush_rows=2_000,
        flush_seconds=0.5,
        stale_seconds=1e9,
    )
    kwargs.update(overrides)
    return Settings(**kwargs)


def read_all(tmp_path):
    files = sorted(Path(tmp_path).rglob("*.parquet"))
    if not files:
        return None
    return pq.read_table(files, schema=SCHEMA)


def test_replay_run_writes_everything_it_received(tmp_path):
    settings = settings_for(tmp_path)
    recorder = Recorder(
        settings, lambda s, sink: ReplayFeed(s, sink, speed=300, seed=1)
    )
    stats = recorder.run(duration=3.0)

    assert stats["received"] > 0, "replay feed produced nothing"
    assert stats["dropped"] == 0
    # nothing may be stranded in the buffer or the queue at shutdown
    assert stats["rows_written"] == stats["received"]

    table = read_all(tmp_path)
    assert table.num_rows == stats["received"]


def test_data_is_partitioned_and_readable(tmp_path):
    settings = settings_for(tmp_path)
    recorder = Recorder(
        settings, lambda s, sink: ReplayFeed(s, sink, speed=300, seed=2)
    )
    recorder.run(duration=3.0)

    epics = {p.name for p in Path(tmp_path).iterdir() if p.is_dir()}
    assert epics == {"TEST.A", "TEST.B"}

    table = read_all(tmp_path)
    assert set(table.column("epic").to_pylist()) == {"TEST.A", "TEST.B"}
    # a tick is only useful if it carries both sides of the book
    assert all(b is not None for b in table.column("bid").to_pylist())
    assert all(o is not None for o in table.column("ofr").to_pylist())


def test_spread_is_wider_when_the_market_is_quiet(tmp_path):
    """Sanity check on the synthetic data itself: the intraday structure the
    execution work is supposed to find has to actually be in there.

    Driven straight into a list rather than through the Recorder - this is
    about the generator, and it needs hours of simulated time, which at a
    disk-sustainable rate would make for a slow test.
    """
    rows = []
    feed = ReplayFeed(settings_for(tmp_path), rows.append, speed=50_000, seed=3)
    feed.start()
    time.sleep(2.0)
    feed.stop()

    assert len(rows) > 1_000
    by_hour = {}
    for row in rows:
        by_hour.setdefault(row["recv_ts"].hour, []).append(row["ofr"] - row["bid"])

    assert 12 in by_hour and 8 in by_hour, f"expected open and midday, got {sorted(by_hour)}"
    midday = sum(by_hour[12]) / len(by_hour[12])
    open_hour = sum(by_hour[8]) / len(by_hour[8])
    assert midday > open_hour


def test_shutdown_flushes_a_partial_buffer(tmp_path):
    """flush_rows far above what the run produces, so everything on disk got
    there via the shutdown path rather than a size-triggered flush."""
    settings = settings_for(tmp_path, flush_rows=10_000_000, flush_seconds=1e9)
    recorder = Recorder(
        settings, lambda s, sink: ReplayFeed(s, sink, speed=300, seed=4)
    )
    stats = recorder.run(duration=2.0)

    assert stats["received"] > 0
    assert stats["rows_written"] == stats["received"]
    assert read_all(tmp_path).num_rows == stats["received"]


def test_a_failing_feed_is_retried(tmp_path):
    """First start raises; the supervisor must build a new feed rather than
    giving up and leaving the recorder alive but deaf."""
    attempts = []

    class FlakyFeed(ReplayFeed):
        def start(self):
            attempts.append(1)
            if len(attempts) == 1:
                raise RuntimeError("simulated connection failure")
            super().start()

    settings = settings_for(tmp_path)
    recorder = Recorder(settings, lambda s, sink: FlakyFeed(s, sink, speed=300))
    stats = recorder.run(duration=8.0)

    assert len(attempts) >= 2, "feed was never retried"
    assert stats["received"] > 0, "recovered feed produced no data"


def test_stale_feed_is_rebuilt(tmp_path):
    """A feed that connects but never delivers is indistinguishable from a
    healthy quiet one, so silence past stale_seconds must force a rebuild."""
    starts = []

    class SilentFeed:
        def __init__(self, settings, sink):
            pass

        def start(self):
            starts.append(1)

        def stop(self):
            pass

    settings = settings_for(tmp_path, stale_seconds=2.0)
    recorder = Recorder(settings, SilentFeed)
    recorder.run(duration=9.0)

    assert len(starts) >= 2, f"silent feed was never rebuilt (starts={len(starts)})"
    assert recorder.restarts >= 1


def test_queue_overflow_is_counted_not_crashed(tmp_path):
    settings = settings_for(tmp_path, queue_size=10)
    recorder = Recorder(settings, lambda s, sink: ReplayFeed(s, sink))
    for _ in range(100):
        recorder.sink({"epic": "X", "recv_ts": datetime.now(timezone.utc)})

    assert recorder.dropped > 0
    assert recorder.received + recorder.dropped == 100


def test_intraday_curve_is_zero_outside_the_session():
    assert intraday_intensity(3) == 0.0
    assert intraday_intensity(20) == 0.0
    assert intraday_intensity(8.1) > intraday_intensity(12)
    assert intraday_intensity(16) > intraday_intensity(12)
