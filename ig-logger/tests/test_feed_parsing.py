from datetime import datetime, timezone

import pytest

from ig_logger.feed import build_row, epic_from_item


def fake_update(values):
    """Stands in for a Lightstreamer ItemUpdate.getValue."""
    return lambda field: values.get(field)


def test_epic_is_extracted_from_the_item_name():
    assert epic_from_item("CHART:CS.D.EURUSD.MINI.IP:TICK") == "CS.D.EURUSD.MINI.IP"


def test_full_tick_is_parsed():
    row = build_row(
        "CHART:CS.D.EURUSD.MINI.IP:TICK",
        fake_update(
            {
                "BID": "1.0812",
                "OFR": "1.0814",
                "LTP": "1.0813",
                "LTV": "5",
                "TTV": "120",
                "UTM": "1789488000000",
                "DAY_HIGH": "1.0850",
            }
        ),
    )
    assert row["epic"] == "CS.D.EURUSD.MINI.IP"
    assert row["bid"] == pytest.approx(1.0812)
    assert row["ltv"] == 5
    assert row["ttv"] == 120
    assert row["day_high"] == pytest.approx(1.0850)
    assert row["utm"] == datetime.fromtimestamp(1789488000, tz=timezone.utc)


def test_missing_and_empty_fields_become_none():
    row = build_row("CHART:X:TICK", fake_update({"BID": "", "OFR": None}))
    assert row["bid"] is None
    assert row["ofr"] is None
    assert row["utm"] is None


def test_junk_values_do_not_raise():
    """IG sends the occasional non-numeric placeholder. Losing one field must
    not take down the stream."""
    row = build_row(
        "CHART:X:TICK", fake_update({"BID": "not-a-number", "OFR": "1.5", "UTM": "nope"})
    )
    assert row["bid"] is None
    assert row["ofr"] == pytest.approx(1.5)
    assert row["utm"] is None


def test_recv_ts_is_always_populated():
    row = build_row("CHART:X:TICK", fake_update({}))
    assert row["recv_ts"].tzinfo is not None


def test_every_schema_column_is_present():
    """Rows go straight into a fixed-schema Arrow table, so a missing key
    would be a KeyError at flush time rather than here."""
    from ig_logger.storage import COLUMNS

    row = build_row("CHART:X:TICK", fake_update({"BID": "1.0"}))
    assert set(row) == set(COLUMNS)
