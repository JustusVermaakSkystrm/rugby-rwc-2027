"""Result validation ledger: protects the simulation from mid-game scores.

Hourly re-runs may happen while matches are in progress. A World Cup score
from the upstream snapshot is only fed to the simulator once it is
trustworthy:

  - entered manually in data/manual_results.csv  -> trusted immediately
  - match date two or more days old              -> certainly finished
  - confirmed by an official source (official.py) -> trusted immediately
  - otherwise (recent match): the same score must be observed unchanged on
    three consecutive runs spanning at least an hour (quarantine in
    data/pending_results.csv)

A mid-game partial score keeps changing between observations, so it never
clears quarantine; a final score confirms after two further runs.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pandas as pd

from .dataset import DATA_DIR

ACCEPTED_PATH = DATA_DIR / "accepted_results.csv"
PENDING_PATH = DATA_DIR / "pending_results.csv"
KEY = ["date", "home_team", "away_team"]
CONFIRM_OBSERVATIONS = 3
CONFIRM_AGE = timedelta(minutes=60)
SAFE_AGE_DAYS = 2
MAX_PLAUSIBLE = 150          # rugby scores can be high; guard only absurdities


def _columns(path) -> list[str]:
    cols = KEY + ["home_score", "away_score"]
    if path == PENDING_PATH:
        cols += ["first_seen", "times_seen"]
    return cols


def _load(path) -> pd.DataFrame:
    if path.exists():
        try:
            return pd.read_csv(path, dtype={"date": str})
        except pd.errors.EmptyDataError:
            pass
    return pd.DataFrame(columns=_columns(path))


def _key_set(df: pd.DataFrame) -> set[tuple]:
    return {(r.date, r.home_team, r.away_team) for r in df.itertuples(index=False)}


def validate_results(scored: pd.DataFrame, manual: pd.DataFrame,
                     official: dict | None = None,
                     now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    today = now.date()
    accepted = _load(ACCEPTED_PATH)
    pending = _load(PENDING_PATH)
    acc_scores = {(r.date, r.home_team, r.away_team): (r.home_score, r.away_score)
                  for r in accepted.itertuples(index=False)}
    pen_rows = {(r.date, r.home_team, r.away_team): r
                for r in pending.itertuples(index=False)}
    manual_keys = set()
    if not manual.empty:
        mm = manual.copy()
        mm["date"] = pd.to_datetime(mm["date"]).dt.strftime("%Y-%m-%d")
        manual_keys = _key_set(mm)

    summary = {"accepted": [], "quarantined": [], "corrected": [], "unstable": []}
    new_pending = []

    def accept(key, hs, as_):
        acc_scores[key] = (hs, as_)
        summary["accepted"].append(f"{key[1]} {hs}-{as_} {key[2]} ({key[0]})")

    for r in scored.itertuples(index=False):
        date_str = pd.Timestamp(r.date).strftime("%Y-%m-%d")
        key = (date_str, r.home_team, r.away_team)
        hs, as_ = int(r.home_score), int(r.away_score)
        if not (0 <= hs <= MAX_PLAUSIBLE and 0 <= as_ <= MAX_PLAUSIBLE):
            summary["unstable"].append(f"implausible score {key}: {hs}-{as_}")
            continue
        if key in acc_scores:
            if acc_scores[key] == (hs, as_):
                continue
            summary["corrected"].append(
                f"{key}: accepted {acc_scores[key]} -> upstream now {hs}-{as_}")
        elif key in manual_keys:
            accept(key, hs, as_)
            continue
        elif official and key in official and tuple(official[key]) == (hs, as_):
            accept(key, hs, as_)
            continue
        elif (today - pd.Timestamp(date_str).date()).days >= SAFE_AGE_DAYS:
            accept(key, hs, as_)
            continue

        prev = pen_rows.get(key)
        if prev is not None and (int(prev.home_score), int(prev.away_score)) == (hs, as_):
            first_seen = datetime.fromisoformat(prev.first_seen)
            seen = int(prev.times_seen) + 1
            if seen >= CONFIRM_OBSERVATIONS and now - first_seen >= CONFIRM_AGE:
                accept(key, hs, as_)
            else:
                new_pending.append((key, hs, as_, prev.first_seen, seen))
        else:
            if prev is not None:
                summary["unstable"].append(
                    f"{key}: score changed {prev.home_score}-{prev.away_score} "
                    f"-> {hs}-{as_} (in-progress?)")
            else:
                summary["quarantined"].append(f"{key[1]} {hs}-{as_} {key[2]}")
            new_pending.append((key, hs, as_,
                                now.isoformat(timespec="seconds"), 1))

    pd.DataFrame(
        [{"date": k[0], "home_team": k[1], "away_team": k[2],
          "home_score": hs, "away_score": as_}
         for k, (hs, as_) in sorted(acc_scores.items())],
        columns=_columns(ACCEPTED_PATH),
    ).to_csv(ACCEPTED_PATH, index=False)
    pd.DataFrame(
        [{"date": k[0], "home_team": k[1], "away_team": k[2],
          "home_score": hs, "away_score": as_, "first_seen": fs,
          "times_seen": seen}
         for k, hs, as_, fs, seen in new_pending if k not in acc_scores],
        columns=_columns(PENDING_PATH),
    ).to_csv(PENDING_PATH, index=False)
    return summary


def apply_ledger(fixtures: pd.DataFrame, manual: pd.DataFrame,
                 now: datetime | None = None) -> pd.DataFrame:
    """Blank out any fixture score not yet validated; the simulator treats
    everything else as unplayed."""
    now = now or datetime.now(timezone.utc)
    today = now.date()
    accepted = _key_set(_load(ACCEPTED_PATH))
    manual_keys = set()
    if not manual.empty:
        mm = manual.copy()
        mm["date"] = pd.to_datetime(mm["date"]).dt.strftime("%Y-%m-%d")
        manual_keys = _key_set(mm)

    out = fixtures.copy()
    blanked = []
    for i, r in out.iterrows():
        if pd.isna(r["home_score"]):
            continue
        date_str = pd.Timestamp(r["date"]).strftime("%Y-%m-%d") if pd.notna(
            r.get("date")) else None
        if date_str is None:
            continue
        key = (date_str, r["home_team"], r["away_team"])
        safe_age = (today - pd.Timestamp(date_str).date()).days >= SAFE_AGE_DAYS
        if not (safe_age or key in accepted or key in manual_keys):
            out.at[i, "home_score"] = float("nan")
            out.at[i, "away_score"] = float("nan")
            blanked.append(f"{r['home_team']} v {r['away_team']} ({date_str})")
    if blanked:
        print(f"Ledger: holding back {len(blanked)} unvalidated score(s): "
              + "; ".join(blanked))
    return out
