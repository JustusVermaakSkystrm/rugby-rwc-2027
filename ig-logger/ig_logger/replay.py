"""Synthetic tick feed, for exercising the pipeline without touching IG.

Two uses. It lets the storage and shutdown paths be tested in CI with no
credentials and no network, and it produces data with a realistic intraday
shape - busier and wider-spread around the open and close, quiet in the middle
- so the analysis built on top has something with known structure to be
validated against.

Nothing here talks to IG. It is a stand-in for `IGTickFeed`, same interface.
"""

import logging
import math
import random
import threading
from datetime import datetime, timedelta, timezone

from .storage import COLUMNS

logger = logging.getLogger(__name__)


def intraday_intensity(hour):
    """U-shaped activity curve over a 08:00-16:30 session, in [0.15, 1.0].

    Real intraday volume looks like this: a burst at the open, a lull over
    lunch, a larger burst into the close. It is the single most reliable
    periodicity in market data, which is exactly why it is worth recording.
    """
    if hour < 8 or hour > 16.5:
        return 0.0
    position = (hour - 8) / 8.5            # 0 at open, 1 at close
    u = math.cos(2 * math.pi * position) * 0.5 + 0.5   # 1 at both ends, 0 mid
    return 0.15 + 0.85 * (u ** 1.5)


class ReplayFeed:
    """Drop-in replacement for IGTickFeed that invents its own ticks.

    `speed` is simulated seconds per real second, so speed=3600 replays an
    hour of market in a second and a full day in about 24 seconds.
    """

    def __init__(self, settings, sink, speed=1.0, start_time=None, seed=0):
        self.settings = settings
        self.sink = sink
        self.speed = speed
        self.rng = random.Random(seed)
        self.start_time = start_time or datetime.now(timezone.utc).replace(
            hour=8, minute=0, second=0, microsecond=0
        )
        self._stop = threading.Event()
        self._thread = None

    def start(self):
        self._stop.clear()
        self._thread = threading.Thread(target=self._run, name="ReplayFeed", daemon=True)
        self._thread.start()
        logger.info("replay feed started at %sx speed", self.speed)

    def stop(self):
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=5)
            self._thread = None

    def _run(self):
        mids = {epic: 100.0 + 10 * i for i, epic in enumerate(self.settings.epics)}
        sim_time = self.start_time

        while not self._stop.is_set():
            hour = sim_time.hour + sim_time.minute / 60
            intensity = intraday_intensity(hour)

            if intensity == 0.0:
                # outside the session, jump to the next open rather than
                # crawling through the night one step at a time
                sim_time = (sim_time + timedelta(days=1)).replace(hour=8, minute=0, second=0)
                continue

            for epic in self.settings.epics:
                if self.rng.random() > intensity:
                    continue
                mids[epic] += self.rng.gauss(0, 0.02)
                mid = mids[epic]
                # spread is widest when activity is lowest - the effect the
                # execution work is meant to exploit
                spread = 0.5 + 1.5 * (1 - intensity) + abs(self.rng.gauss(0, 0.1))
                row = dict.fromkeys(COLUMNS)
                row.update(
                    recv_ts=sim_time,
                    epic=epic,
                    utm=sim_time,
                    bid=round(mid - spread / 2, 4),
                    ofr=round(mid + spread / 2, 4),
                    ltp=round(mid, 4),
                    ltv=int(abs(self.rng.gauss(0, 50)) * intensity) + 1,
                )
                self.sink(row)

            sim_time += timedelta(seconds=1)
            # always yield: without this a high speed becomes a busy loop that
            # buries the writer and makes the drop counter the only output
            self._stop.wait(1.0 / self.speed)
