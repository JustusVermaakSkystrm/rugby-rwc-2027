"""Official result confirmation via ESPN's public rugby scoreboard.

The quarantine ledger's stability rule (three unchanged sightings) is a
heuristic; this module provides ground truth. ESPN's scoreboard API reports
a per-match completed flag and final score (and, where available, a try
count in the boxscore), so a result can be accepted the moment the match is
officially over — and rejected while in progress.

Verified league ids: Rugby World Cup 164205, International Test Match
289234, Six Nations 180659, The Rugby Championship 244293. Every failure
path degrades gracefully to the stability rule.
"""

from __future__ import annotations

import json
import urllib.request
from datetime import date, timedelta

SCOREBOARD_URL = ("https://site.api.espn.com/apis/site/v2/sports/rugby/"
                  "{league}/scoreboard?dates={d}")
LEAGUES = ("164205", "289234")        # World Cup, then general test matches

ALIASES = {
    "usa": "United States", "united states": "United States",
    "hong kong": "Hong Kong China", "hong kong china": "Hong Kong China",
    "samoa": "Samoa", "western samoa": "Samoa",
    "czechia": "Czech Republic",
    "ivory coast": "Ivory Coast", "côte d'ivoire": "Ivory Coast",
}


def _canon(name: str, known: set[str]) -> str | None:
    n = (name or "").strip()
    if n in known:
        return n
    return ALIASES.get(n.lower())


def _tries(competitor: dict) -> int | None:
    """Best-effort try count from the competitor's statistics block."""
    for stat in competitor.get("statistics", []) or []:
        nm = str(stat.get("name", "")).lower()
        if nm in ("tries", "tries scored"):
            try:
                return int(float(stat.get("displayValue", stat.get("value"))))
            except (TypeError, ValueError):
                return None
    return None


def parse_scoreboard(payload: dict, known_teams: set[str]) -> list[dict]:
    out = []
    for ev in payload.get("events", []):
        try:
            status = ev["status"]["type"]
            if not (status.get("completed") or status.get("state") == "post"):
                continue
            comp = ev["competitions"][0]
            sides = {}
            for c in comp["competitors"]:
                team = _canon(c["team"]["displayName"], known_teams)
                if team is None:
                    raise KeyError(f"unmapped team {c['team']['displayName']}")
                sides[c["homeAway"]] = (team, int(c["score"]), _tries(c))
            out.append({
                "home": sides["home"][0], "home_score": sides["home"][1],
                "away": sides["away"][0], "away_score": sides["away"][1],
                "home_tries": sides["home"][2], "away_tries": sides["away"][2],
                "event_date": ev.get("date", ""),
            })
        except (KeyError, IndexError, ValueError) as e:
            print(f"  official: skipping event ({e})")
    return out


def fetch_official_results(days_back: int = 3, known_teams: set[str] | None = None,
                           ) -> list[dict]:
    """Completed international matches over the recent window, [] on failure."""
    known_teams = known_teams or set()
    results, seen = [], set()
    for delta in range(days_back, -1, -1):
        d = (date.today() - timedelta(days=delta)).strftime("%Y%m%d")
        for league in LEAGUES:
            try:
                req = urllib.request.Request(
                    SCOREBOARD_URL.format(league=league, d=d),
                    headers={"User-Agent": "rugby-rwc-2027-predictor"})
                with urllib.request.urlopen(req, timeout=20) as resp:
                    payload = json.loads(resp.read())
            except Exception as e:
                print(f"  official: fetch failed league {league} {d}: {e}")
                continue
            for m in parse_scoreboard(payload, known_teams):
                key = frozenset((m["home"], m["away"]))
                if key not in seen:
                    seen.add(key)
                    results.append(m)
    return results
