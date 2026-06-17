"""Data loading and point-in-time feature construction for rugby tests.

One chronological pass over the full results history produces, with no
lookahead leakage:
  - per-match training rows (features + margin/total/score/try targets) for
    completed matches
  - an end-of-history state snapshot per team (Elo, points attack/defence,
    rolling form) used to build feature rows for matches not yet played.

Input schema (data/results.csv), martj42-compatible plus optional tries:
  date, home_team, away_team, home_score, away_score,
  tournament, city, country, neutral, home_tries, away_tries
"""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path

import numpy as np
import pandas as pd

from .ratings import (HOME_ADVANTAGE, PointsAttackDefence, EloTracker,
                      importance_level)

DATA_DIR = Path(__file__).parent / "data"
# Upstream maintained mirror of the historical results (see run.py update).
RESULTS_URL = ("https://raw.githubusercontent.com/seanyboi/rugbydata/"
               "main/README.md")  # placeholder; live updates come via official.py
FORM_WINDOW = 8                   # rolling window of recent tests
MIN_TRAIN_DATE = "1995-01-01"     # professional era onwards
MIN_MATCHES = 10                  # both sides need this many prior tests

FEATURES = [
    "elo_home", "elo_away", "elo_diff_adj",
    "patt_home", "pdef_home", "patt_away", "pdef_away",
    "exp_pts_home", "exp_pts_away",
    "form_pf_home", "form_pa_home", "form_win_home",
    "form_pf_away", "form_pa_away", "form_win_away",
    "matches_home", "matches_away",
    "neutral", "importance",
]

# Ranking-only baseline feature set (Elo difference is the single signal),
# kept for before/after validation comparisons.
FEATURES_BASELINE = ["elo_diff_adj", "neutral"]

_REQUIRED = ["date", "home_team", "away_team", "home_score", "away_score"]


def load_teams() -> dict:
    with open(DATA_DIR / "teams.json") as f:
        return json.load(f)


def load_rankings() -> dict[str, float]:
    """World Rugby ranking points per team (data/rankings.json), used as the
    Elo prior. Returns {} if the file is absent."""
    path = DATA_DIR / "rankings.json"
    if not path.exists():
        return {}
    with open(path) as f:
        blob = json.load(f)
    return {k: float(v) for k, v in blob.get("points", {}).items()}


def _coerce(df: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in _REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"results.csv missing columns: {missing}")
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"]).sort_values("date", kind="stable")
    if "tournament" not in df.columns:                 # accept 'competition'
        df["tournament"] = df.get("competition", "Test Match")
    if "neutral" not in df.columns:
        df["neutral"] = False
    df["neutral"] = df["neutral"].astype(str).str.lower().isin(
        ("true", "1", "yes", "t"))
    for col in ("home_tries", "away_tries"):
        if col not in df.columns:
            df[col] = np.nan
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df.reset_index(drop=True)


def load_results() -> pd.DataFrame:
    return _coerce(pd.read_csv(DATA_DIR / "results.csv"))


def _load_overlay(name: str) -> pd.DataFrame:
    path = DATA_DIR / name
    if not path.exists():
        return pd.DataFrame()
    df = pd.read_csv(path)
    return _coerce(df) if not df.empty else df


def load_manual_results() -> pd.DataFrame:
    """Optional manual entry (data/manual_results.csv) — final word on a
    score, useful minutes after full-time before upstream catches up."""
    return _load_overlay("manual_results.csv")


def load_official_results() -> pd.DataFrame:
    """Full-time scores confirmed by an official source (see official.py)."""
    return _load_overlay("official_results.csv")


def _overlay(base: pd.DataFrame, extra: pd.DataFrame) -> pd.DataFrame:
    """Apply score overrides from `extra` on top of `base` (extra wins)."""
    if extra.empty:
        return base
    key = ["date", "home_team", "away_team"]
    cols = key + ["home_score", "away_score", "home_tries", "away_tries"]
    extra = extra[[c for c in cols if c in extra.columns]]
    base = base.merge(extra, on=key, how="left", suffixes=("", "_x"))
    for c in ("home_score", "away_score", "home_tries", "away_tries"):
        xc = f"{c}_x"
        if xc in base.columns:
            ov = base[xc].notna()
            base.loc[ov, c] = base.loc[ov, c]
            base.loc[ov, c] = base.loc[ov, xc]
            base = base.drop(columns=xc)
    missing = extra.merge(base[key], on=key, how="left", indicator=True)
    missing = missing[missing["_merge"] == "left_only"].drop(columns="_merge")
    if not missing.empty:
        base = pd.concat([base, missing], ignore_index=True).sort_values(
            "date", kind="stable").reset_index(drop=True)
    return base


def merged_results() -> pd.DataFrame:
    """Upstream history with official-result and manual overrides applied
    (manual entries have the final word)."""
    return _overlay(_overlay(load_results(), load_official_results()),
                    load_manual_results())


class _TeamForm:
    __slots__ = ("pf", "pa", "win", "n")

    def __init__(self):
        self.pf = deque(maxlen=FORM_WINDOW)
        self.pa = deque(maxlen=FORM_WINDOW)
        self.win = deque(maxlen=FORM_WINDOW)
        self.n = 0

    def features(self) -> tuple[float, float, float]:
        if not self.pf:
            return 22.0, 22.0, 0.5   # rough global priors
        return (float(np.mean(self.pf)), float(np.mean(self.pa)),
                float(np.mean(self.win)))

    def record(self, scored: int, conceded: int) -> None:
        self.pf.append(scored)
        self.pa.append(conceded)
        self.win.append(1.0 if scored > conceded else
                        (0.5 if scored == conceded else 0.0))
        self.n += 1


class FeatureBuilder:
    """One chronological pass over history; emits leak-free feature rows."""

    def __init__(self, wr_points: dict[str, float] | None = None):
        self.elo = EloTracker()
        if wr_points:
            self.elo.seed_prior(wr_points)
        self.ad = PointsAttackDefence()
        self.form: dict[str, _TeamForm] = {}

    def _form(self, team: str) -> _TeamForm:
        if team not in self.form:
            self.form[team] = _TeamForm()
        return self.form[team]

    def match_features(self, home: str, away: str, neutral: bool,
                       tournament: str) -> dict:
        rh, ra = self.elo.get(home), self.elo.get(away)
        bonus = 0.0 if neutral else HOME_ADVANTAGE
        ah, dh = self.ad.get(home)
        aa, da = self.ad.get(away)
        exp_h, exp_a = self.ad.expected(home, away, neutral)
        fh, fa = self._form(home), self._form(away)
        pf_h, pa_h, win_h = fh.features()
        pf_a, pa_a, win_a = fa.features()
        return {
            "elo_home": rh, "elo_away": ra,
            "elo_diff_adj": (rh + bonus) - ra,
            "patt_home": ah, "pdef_home": dh, "patt_away": aa, "pdef_away": da,
            "exp_pts_home": exp_h, "exp_pts_away": exp_a,
            "form_pf_home": pf_h, "form_pa_home": pa_h, "form_win_home": win_h,
            "form_pf_away": pf_a, "form_pa_away": pa_a, "form_win_away": win_a,
            "matches_home": fh.n, "matches_away": fa.n,
            "neutral": int(neutral), "importance": importance_level(tournament),
        }

    def advance(self, home: str, away: str, hs: int, as_: int,
                tournament: str, neutral: bool) -> None:
        self.elo.update(home, away, hs, as_, tournament, neutral)
        self.ad.update(home, away, hs, as_, tournament, neutral)
        self._form(home).record(hs, as_)
        self._form(away).record(as_, hs)


def build_training_table(results: pd.DataFrame,
                         min_date: str = MIN_TRAIN_DATE,
                         min_matches: int = MIN_MATCHES,
                         wr_points: dict[str, float] | None = None,
                         ) -> tuple[pd.DataFrame, FeatureBuilder]:
    """Returns (training table, end-of-history state for future prediction).

    The full history feeds Elo/form state; only matches after `min_date`
    where both teams have at least `min_matches` prior tests become training
    rows.
    """
    if wr_points is None:
        wr_points = load_rankings()
    fb = FeatureBuilder(wr_points)
    rows = []
    min_ts = pd.Timestamp(min_date)
    played = results.dropna(subset=["home_score", "away_score"])
    for r in played.itertuples(index=False):
        feats = fb.match_features(r.home_team, r.away_team, bool(r.neutral),
                                  r.tournament)
        if (r.date >= min_ts and feats["matches_home"] >= min_matches
                and feats["matches_away"] >= min_matches):
            hs, as_ = int(r.home_score), int(r.away_score)
            ht = int(r.home_tries) if pd.notna(r.home_tries) else -1
            at = int(r.away_tries) if pd.notna(r.away_tries) else -1
            feats.update({
                "date": r.date,
                "home_team": r.home_team, "away_team": r.away_team,
                "home_score": hs, "away_score": as_,
                "margin": hs - as_, "total": hs + as_,
                "home_tries": ht, "away_tries": at,
            })
            rows.append(feats)
        fb.advance(r.home_team, r.away_team, int(r.home_score),
                   int(r.away_score), r.tournament, bool(r.neutral))
    return pd.DataFrame(rows), fb
