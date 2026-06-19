"""Incremental result ingestion: keep data/results.csv current.

The historical results.csv was assembled by a one-off ESPN sweep (see
scripts/). This module does the same fetch for a *recent* window only and
appends any newly-completed men's international test that isn't already on
file — so re-running `python -m rugby.run update` (hourly, in the cloud)
keeps team ratings sharp as warm-up tests through 2026-2027 are played,
without a manual rebuild.

Try counts are derived from ESPN's scoring-play details (the same method the
full build used), so freshly-ingested matches carry tries for the
bonus-point model. Every failure path degrades to "added nothing".
"""

from __future__ import annotations

import json
import urllib.request
from collections import Counter
from datetime import date, timedelta

import numpy as np
import pandas as pd

from .dataset import DATA_DIR

RESULTS_PATH = DATA_DIR / "results.csv"
UPCOMING_PATH = DATA_DIR / "upcoming_fixtures.csv"
SCOREBOARD_URL = ("https://site.api.espn.com/apis/site/v2/sports/rugby/"
                  "{league}/scoreboard?dates={start}-{end}")

# ESPN scoreboard league ids that carry men's international tests. 17567 is the
# World Rugby Nations Championship — the July tours and the November (Autumn)
# windows, including the July 2026 series and the finals. 289234 is the broad
# catch-all for other internationals (most Pacific / South-American Tier-2
# tests etc.). The Six Nations and Rugby Championship feeds add their own
# fixtures. Known gap: ESPN exposes no Rugby Europe Championship feed, so
# Georgia / Spain / Portugal / Romania's internal competition isn't ingested
# (their cross-tier tests still are).
LEAGUES = {
    "17567": "Nations Championship",
    "289234": "International Test Match",
    "180659": "Six Nations",
    "244293": "Rugby Championship",
    "164205": "Rugby World Cup",
}

# ESPN display name -> canonical name used across results.csv (matches the
# normalisation the full build used).
NORM = {
    "United States of America": "United States", "USA": "United States",
    "Hong Kong": "Hong Kong China", "Hong Kong, China": "Hong Kong China",
    "Korea Republic": "South Korea", "Czechia": "Czech Republic",
    "Cote d'Ivoire": "Ivory Coast", "Côte d'Ivoire": "Ivory Coast",
    "Western Samoa": "Samoa",
}
NOT_NATIONAL = {"Cambridge", "Oxford", "Barbarians", "British & Irish Lions"}


def _norm(name) -> str | None:
    if name is None:
        return None
    name = str(name).strip()
    return NORM.get(name, name)


def _fetch(url: str, tries: int = 3) -> dict | None:
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception:
            continue
    return None


def _parse_event(e: dict, league_name: str) -> dict | None:
    comps = e.get("competitions") or []
    if not comps:
        return None
    c = comps[0]
    if not (c.get("status", {}).get("type", {}) or {}).get("completed"):
        return None
    cs = c.get("competitors") or []
    if len(cs) != 2:
        return None
    tries = Counter()
    for dd in c.get("details", []):
        if "try" in ((dd.get("type", {}) or {}).get("text", "") or "").lower():
            tid = (dd.get("team", {}) or {}).get("id")
            if tid:
                tries[tid] += 1
    home = next((x for x in cs if x.get("homeAway") == "home"), cs[0])
    away = next((x for x in cs if x.get("homeAway") == "away"), cs[1])
    ht, at = _norm(home["team"]["displayName"]), _norm(away["team"]["displayName"])
    if not ht or not at or ht in NOT_NATIONAL or at in NOT_NATIONAL:
        return None
    try:
        hs, as_ = int(home["score"]), int(away["score"])
    except (TypeError, ValueError, KeyError):
        return None
    venue = c.get("venue") or {}
    addr = venue.get("address") or {}
    return {
        "date": e["date"][:10], "home_team": ht, "away_team": at,
        "home_score": hs, "away_score": as_,
        "tournament": league_name, "city": addr.get("city") or "",
        "country": addr.get("state") or "",
        "neutral": bool(c.get("neutralSite")),
        "home_tries": tries.get(home["team"]["id"]),
        "away_tries": tries.get(away["team"]["id"]),
    }


def fetch_recent(days_back: int = 18) -> list[dict]:
    """Completed internationals over the recent window, [] on any failure."""
    end = (date.today() + timedelta(days=1)).strftime("%Y%m%d")
    start = (date.today() - timedelta(days=days_back)).strftime("%Y%m%d")
    found, seen = [], set()
    for league, name in LEAGUES.items():
        payload = _fetch(SCOREBOARD_URL.format(league=league, start=start, end=end))
        if not payload:
            continue
        for e in payload.get("events", []):
            rec = _parse_event(e, name)
            if rec is None:
                continue
            key = (rec["date"], frozenset((rec["home_team"], rec["away_team"])))
            if key not in seen:
                seen.add(key)
                found.append(rec)
    return found


def _parse_upcoming(e: dict, league_name: str) -> dict | None:
    """A scheduled (not-yet-played) international between two national teams."""
    comps = e.get("competitions") or []
    if not comps:
        return None
    c = comps[0]
    if (c.get("status", {}).get("type", {}) or {}).get("completed"):
        return None
    cs = c.get("competitors") or []
    if len(cs) != 2:
        return None
    home = next((x for x in cs if x.get("homeAway") == "home"), cs[0])
    away = next((x for x in cs if x.get("homeAway") == "away"), cs[1])
    ht, at = _norm(home["team"]["displayName"]), _norm(away["team"]["displayName"])
    if not ht or not at or ht in NOT_NATIONAL or at in NOT_NATIONAL or ht == at:
        return None
    venue = c.get("venue") or {}
    addr = venue.get("address") or {}
    return {
        "date": e["date"][:10], "home_team": ht, "away_team": at,
        "tournament": league_name, "city": addr.get("city") or "",
        "country": addr.get("state") or "",
        "neutral": bool(c.get("neutralSite")),
    }


def fetch_upcoming(days_ahead: int = 500) -> list[dict]:
    """Scheduled internationals over the run-in to the World Cup, [] on any
    failure. The horizon (~16 months to RWC 2027) is swept in ~120-day chunks
    because a single long scoreboard request gets truncated by ESPN."""
    found, seen = [], set()
    chunk = 120
    for league, name in LEAGUES.items():
        if name == "Rugby World Cup":
            continue          # the tournament simulator owns RWC fixtures
        offset = 0
        while offset < days_ahead:
            start = (date.today() + timedelta(days=offset)).strftime("%Y%m%d")
            end = (date.today() + timedelta(days=min(offset + chunk, days_ahead))
                   ).strftime("%Y%m%d")
            payload = _fetch(SCOREBOARD_URL.format(league=league, start=start, end=end))
            offset += chunk
            if not payload:
                continue
            for e in payload.get("events", []):
                rec = _parse_upcoming(e, name)
                if rec is None:
                    continue
                key = (rec["date"], frozenset((rec["home_team"], rec["away_team"])))
                if key not in seen:
                    seen.add(key)
                    found.append(rec)
    return found


def refresh_upcoming_fixtures() -> int:
    """Cache the scheduled-internationals list to data/upcoming_fixtures.csv
    (so the prediction step has fixtures without a second network call).
    Returns the number written; leaves any existing file in place on failure."""
    upcoming = fetch_upcoming()
    if not upcoming:
        return 0
    df = pd.DataFrame(upcoming).sort_values("date", kind="stable")
    df["neutral"] = df["neutral"].map(lambda b: "True" if bool(b) else "False")
    df.to_csv(UPCOMING_PATH, index=False)
    return len(df)


def _fmt_try(x) -> str:
    return "" if x is None or (isinstance(x, float) and np.isnan(x)) else str(int(x))


def ingest_new_results() -> list[str]:
    """Append newly-completed internationals to results.csv (dedup on date +
    unordered team pair). Returns one description per match added."""
    recent = fetch_recent()
    if not recent or not RESULTS_PATH.exists():
        return []
    existing = pd.read_csv(RESULTS_PATH)
    existing["date"] = pd.to_datetime(existing["date"], errors="coerce").dt.strftime("%Y-%m-%d")
    have = {(r.date, frozenset((r.home_team, r.away_team)))
            for r in existing.itertuples(index=False)}

    new_rows, added = [], []
    for m in recent:
        key = (m["date"], frozenset((m["home_team"], m["away_team"])))
        if key in have:
            continue
        have.add(key)
        new_rows.append({
            "date": m["date"], "home_team": m["home_team"],
            "away_team": m["away_team"], "home_score": m["home_score"],
            "away_score": m["away_score"], "tournament": m["tournament"],
            "city": m["city"], "country": m["country"],
            "neutral": "True" if m["neutral"] else "False",
            "home_tries": _fmt_try(m["home_tries"]),
            "away_tries": _fmt_try(m["away_tries"]),
        })
        added.append(f"{m['home_team']} {m['home_score']}-{m['away_score']} "
                     f"{m['away_team']} ({m['date']})")
    if not new_rows:
        return []
    combined = pd.concat([existing, pd.DataFrame(new_rows)], ignore_index=True)
    combined = combined.sort_values("date", kind="stable").reset_index(drop=True)
    combined.to_csv(RESULTS_PATH, index=False)
    return added
