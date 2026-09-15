"""IG Lightstreamer tick feed.

Subscribes to CHART:<epic>:TICK in DISTINCT mode and turns each update into a
row matching storage.SCHEMA. Field names are taken from trading_ig's own
TickerSubscription, so they stay in step with the library.
"""

import logging
from datetime import datetime, timezone

from .storage import COLUMNS

logger = logging.getLogger(__name__)

# IG field -> (our column, cast). UTM is handled separately: it is epoch millis.
FIELD_MAP = {
    "BID": ("bid", float),
    "OFR": ("ofr", float),
    "LTP": ("ltp", float),
    "LTV": ("ltv", int),
    "TTV": ("ttv", int),
    "DAY_OPEN_MID": ("day_open_mid", float),
    "DAY_NET_CHG_MID": ("day_net_chg_mid", float),
    "DAY_PERC_CHG_MID": ("day_perc_chg_mid", float),
    "DAY_HIGH": ("day_high", float),
    "DAY_LOW": ("day_low", float),
}


def epic_from_item(item_name):
    """'CHART:CS.D.EURUSD.MINI.IP:TICK' -> 'CS.D.EURUSD.MINI.IP'"""
    parts = item_name.split(":")
    return parts[1] if len(parts) > 2 else item_name


def build_row(item_name, get_value, recv_ts=None):
    """Turn one Lightstreamer update into a storage row.

    `get_value` is a callable taking an IG field name, so this is testable
    without a live Lightstreamer update object.

    IG happily sends empty strings and the occasional non-numeric placeholder;
    a bad field is dropped rather than allowed to kill the stream, because
    losing one value beats losing the connection.
    """
    row = dict.fromkeys(COLUMNS)
    row["recv_ts"] = recv_ts or datetime.now(timezone.utc)
    row["epic"] = epic_from_item(item_name)

    for field, (column, cast) in FIELD_MAP.items():
        raw = get_value(field)
        if raw is None or raw == "":
            continue
        try:
            row[column] = cast(raw)
        except (TypeError, ValueError):
            logger.debug("unparseable %s=%r on %s", field, raw, row["epic"])

    raw_utm = get_value("UTM")
    if raw_utm:
        try:
            row["utm"] = datetime.fromtimestamp(int(raw_utm) / 1000, tz=timezone.utc)
        except (TypeError, ValueError, OSError):
            logger.debug("unparseable UTM=%r on %s", raw_utm, row["epic"])

    return row


class FeedError(RuntimeError):
    """Raised instead of exiting, so the supervisor can retry."""


class IGTickFeed:
    """A live IG tick subscription. `sink` is called once per tick, from a
    Lightstreamer thread, so it must be cheap and must not raise."""

    def __init__(self, settings, sink):
        self.settings = settings
        self.sink = sink
        self._stream = None
        self._subscriptions = []

    def start(self):
        # imported here so the replay path and the tests do not need the
        # Lightstreamer client installed
        from lightstreamer.client import SubscriptionListener
        from trading_ig import IGService, IGStreamService
        from trading_ig.streamer.ticker import TickerSubscription

        sink = self.sink

        class _Listener(SubscriptionListener):
            def onItemUpdate(self, update):
                try:
                    sink(build_row(update.getItemName(), update.getValue))
                except Exception:
                    # never let an exception escape into the LS thread
                    logger.exception("failed to handle tick update")

            def onSubscriptionError(self, code, message):
                logger.error("subscription error %s: %s", code, message)

        service = IGService(
            self.settings.username,
            self.settings.password,
            self.settings.api_key,
            acc_type=self.settings.acc_type.lower(),
            acc_number=self.settings.acc_number,
        )
        stream = IGStreamService(service)
        # Required. IGStreamService.__init__ sets acc_number = None and
        # create_session() passes it straight to Lightstreamer setUser()
        # without ever populating it, so without this you authenticate as None.
        stream.acc_number = self.settings.acc_number

        try:
            # v3 sessions are the current auth flow; trading_ig fetches the
            # CST/X-SECURITY-TOKEN pair needed for the Lightstreamer password
            stream.create_session(version="3")
        except SystemExit as exc:
            # trading_ig calls sys.exit(1) if the LS connect fails, which would
            # kill a daemon that is perfectly capable of retrying
            raise FeedError("Lightstreamer connect failed") from exc

        self._stream = stream
        for epic in self.settings.epics:
            subscription = TickerSubscription(epic)
            subscription.addListener(_Listener())
            stream.subscribe(subscription)
            self._subscriptions.append(subscription)
            logger.info("subscribed to %s", epic)

    def stop(self):
        if self._stream is None:
            return
        try:
            self._stream.disconnect()
        except Exception:
            logger.exception("error while disconnecting stream")
        finally:
            self._stream = None
            self._subscriptions = []
