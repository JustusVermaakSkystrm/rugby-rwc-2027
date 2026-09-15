"""The recorder: wires a feed to the writer and keeps it alive.

Shape of the thing:

    Lightstreamer thread(s) --> bounded Queue --> writer thread --> Parquet
                                     ^
                              supervisor thread restarts a dead feed

The queue matters. Disk I/O must never happen on a Lightstreamer callback: if
writing blocks, the client's internal buffers back up and you silently lose
ticks. The queue is bounded so that a stalled disk drops rows loudly - with a
counter you can see - instead of growing until the OOM killer arrives.
"""

import argparse
import logging
import queue
import signal
import threading
import time
from datetime import datetime, timezone

from .config import Settings, load_dotenv
from .storage import TickWriter

logger = logging.getLogger(__name__)

# Put on the queue to tell the writer "no more producers, drain and stop".
_SENTINEL = object()


class Recorder:
    def __init__(self, settings, feed_factory):
        self.settings = settings
        self.feed_factory = feed_factory
        self.writer = TickWriter(
            settings.data_dir,
            flush_rows=settings.flush_rows,
            flush_seconds=settings.flush_seconds,
        )
        self.queue = queue.Queue(maxsize=settings.queue_size)
        self.stop_event = threading.Event()

        self.received = 0
        self.dropped = 0
        self.restarts = 0
        self._last_tick = None      # monotonic clock of the most recent tick

    def sink(self, row):
        """Called from the feed's thread. Cheap, and never raises."""
        try:
            self.queue.put_nowait(row)
            self.received += 1
            self._last_tick = time.monotonic()
        except queue.Full:
            self.dropped += 1
            if self.dropped % 1000 == 1:
                logger.error("queue full, dropped %d rows so far", self.dropped)

    def _writer_loop(self):
        """Drain the queue until told to stop by the sentinel.

        Deliberately NOT keyed off stop_event. The feed keeps delivering for a
        moment after a shutdown is requested, so a writer that stopped on
        stop_event could exit while the queue was briefly empty and strand
        every tick that arrived afterwards. The sentinel is only queued once
        the feed is provably stopped, which makes the tail safe.
        """
        while True:
            try:
                row = self.queue.get(timeout=0.5)
            except queue.Empty:
                self.writer.maybe_flush()
                continue
            if row is _SENTINEL:
                break
            self.writer.add(row)
        self.writer.flush()

    def _supervise(self):
        """Keep a live feed running, rebuilding it when it goes quiet.

        A silent stream and a healthy one look identical from the outside, so
        silence past `stale_seconds` is treated as failure. Outside market
        hours that means a reconnect every few minutes, which is harmless and
        has the useful property that the recorder is already live the moment
        the market opens.
        """
        backoff = 5.0
        while not self.stop_event.is_set():
            feed = self.feed_factory(self.settings, self.sink)
            try:
                feed.start()
                backoff = 5.0
                self._last_tick = time.monotonic()

                while not self.stop_event.wait(5.0):
                    idle = time.monotonic() - (self._last_tick or 0)
                    if idle > self.settings.stale_seconds:
                        logger.warning(
                            "no ticks for %.0fs, rebuilding the session", idle
                        )
                        self.restarts += 1
                        break
            except Exception:
                logger.exception("feed failed, retrying in %.0fs", backoff)
                self.stop_event.wait(backoff)
                backoff = min(backoff * 2, 300.0)
            finally:
                try:
                    feed.stop()
                except Exception:
                    logger.exception("error stopping feed")

    def run(self, duration=None):
        writer_thread = threading.Thread(
            target=self._writer_loop, name="writer", daemon=True
        )
        supervisor = threading.Thread(
            target=self._supervise, name="supervisor", daemon=True
        )
        writer_thread.start()
        supervisor.start()

        started = time.monotonic()
        try:
            while not self.stop_event.is_set():
                if duration and time.monotonic() - started >= duration:
                    logger.info("duration reached")
                    break
                self.stop_event.wait(1.0)
                self._log_heartbeat()
        finally:
            # Order matters: stop producing, confirm the feed is down, only
            # then tell the writer to drain. Reversing the last two loses ticks.
            self.stop_event.set()
            supervisor.join(timeout=15)
            try:
                self.queue.put(_SENTINEL, timeout=30)
            except queue.Full:
                logger.error("queue still full at shutdown; some rows may be lost")
            writer_thread.join(timeout=60)
            self.writer.close()

        return {
            "received": self.received,
            "dropped": self.dropped,
            "restarts": self.restarts,
            "rows_written": self.writer.rows_written,
            "files_written": self.writer.files_written,
        }

    _last_heartbeat = 0.0

    def _log_heartbeat(self, every=60.0):
        now = time.monotonic()
        if now - self._last_heartbeat < every:
            return
        self._last_heartbeat = now
        logger.info(
            "received=%d written=%d dropped=%d queued=%d restarts=%d",
            self.received,
            self.writer.rows_written,
            self.dropped,
            self.queue.qsize(),
            self.restarts,
        )


def main(argv=None):
    parser = argparse.ArgumentParser(description="Record IG tick data to Parquet.")
    parser.add_argument(
        "--replay",
        action="store_true",
        help="use the synthetic feed instead of IG (no credentials needed)",
    )
    parser.add_argument(
        "--speed", type=float, default=1.0, help="replay speed multiplier"
    )
    parser.add_argument(
        "--duration", type=float, help="stop after this many seconds (default: forever)"
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
    )

    load_dotenv()
    if args.replay:
        # the replay feed needs the epic list and paths but no credentials
        import os

        os.environ.setdefault("IG_USERNAME", "replay")
        os.environ.setdefault("IG_PASSWORD", "replay")
        os.environ.setdefault("IG_API_KEY", "replay")
        os.environ.setdefault("IG_ACC_NUMBER", "replay")
        os.environ.setdefault("IG_EPICS", "CS.D.EURUSD.MINI.IP,IX.D.FTSE.DAILY.IP")

    settings = Settings.from_env()

    if args.replay:
        from .replay import ReplayFeed

        def factory(s, sink):
            return ReplayFeed(s, sink, speed=args.speed)
    else:
        from .feed import IGTickFeed

        factory = IGTickFeed
        logger.info(
            "recording %s account, epics: %s",
            settings.acc_type,
            ", ".join(settings.epics),
        )

    recorder = Recorder(settings, factory)

    def handle_signal(signum, _frame):
        logger.info("signal %s received, shutting down", signum)
        recorder.stop_event.set()

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    stats = recorder.run(duration=args.duration)
    logger.info("done: %s", stats)
    return stats


if __name__ == "__main__":
    main()
