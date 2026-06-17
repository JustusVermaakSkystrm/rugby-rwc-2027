"""Model accuracy tracking: freeze pre-match predictions, grade them later.

Every run upserts the current outcome probabilities for each *unplayed*
match into outputs/prediction_log.csv. Once a match's result is validated,
its row is locked with whatever the model said on the last run before the
result arrived — so the scorecard always grades genuine pre-match
predictions, never a model that has already trained on the outcome.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

LOG_PATH = Path(__file__).parent / "outputs" / "prediction_log.csv"
DATA_DIR = Path(__file__).parent / "data"
KEY = ["date", "home", "away"]
COLS = KEY + ["p_home", "p_draw", "p_away", "pred_score", "locked",
              "home_score", "away_score", "actual_outcome", "hit",
              "score_hit", "p_actual"]


def _load() -> pd.DataFrame:
    if LOG_PATH.exists():
        df = pd.read_csv(LOG_PATH, dtype={"date": str, "pred_score": str})
    else:
        df = pd.DataFrame(columns=COLS)
    df["locked"] = df["locked"].map(lambda x: bool(x) and str(x) != "False") \
        if len(df) else df.get("locked", pd.Series(dtype=bool))
    for c in ("pred_score", "actual_outcome", "hit", "score_hit", "locked"):
        df[c] = df[c].astype(object)
    return df


def update_log(match_table: pd.DataFrame) -> pd.DataFrame:
    log = _load().set_index(KEY)
    for r in match_table.itertuples(index=False):
        key = (str(r.date), r.home, r.away)
        if r.status == "upcoming":
            if key in log.index and bool(log.loc[key, "locked"]):
                continue
            log.loc[key, ["p_home", "p_draw", "p_away", "pred_score", "locked"]] = \
                [r.p_home_win, r.p_draw, r.p_away_win, r.most_likely_score, False]
        else:
            hs, as_ = (int(x) for x in r.score.split("-"))
            outcome = "home" if hs > as_ else ("away" if hs < as_ else "draw")
            if key not in log.index:
                log.loc[key, ["p_home", "p_draw", "p_away", "pred_score"]] = \
                    [r.p_home_win, r.p_draw, r.p_away_win,
                     r.most_likely_score + " (retro)"]
            if bool(log.loc[key, "locked"]):
                continue
            probs = {"home": float(log.loc[key, "p_home"]),
                     "draw": float(log.loc[key, "p_draw"]),
                     "away": float(log.loc[key, "p_away"])}
            picked = max(probs, key=probs.get)
            log.loc[key, ["locked", "home_score", "away_score",
                          "actual_outcome", "hit", "score_hit", "p_actual"]] = \
                [True, hs, as_, outcome, picked == outcome,
                 str(log.loc[key, "pred_score"]) == f"{hs}-{as_}",
                 probs[outcome]]
    out = log.reset_index()
    out.to_csv(LOG_PATH, index=False)
    return out


def summary(log: pd.DataFrame) -> dict | None:
    graded = log[log["locked"] == True]  # noqa: E712
    if graded.empty:
        return None
    probs = graded[["p_home", "p_draw", "p_away"]].astype(float)
    out = {
        "n": len(graded),
        "hits": int(graded["hit"].astype(bool).sum()),
        "expected_hits": float(probs.max(axis=1).sum()),
        "mean_p_actual": float(graded["p_actual"].astype(float).mean()),
        "score_hits": int(graded["score_hit"].astype(bool).sum()),
        "rows": graded.sort_values("date"),
    }
    out["benchmark"] = _benchmark(graded)
    return out


_OUTCOME_COL = {"home": "p_home", "draw": "p_draw", "away": "p_away"}


def _benchmark(graded: pd.DataFrame) -> dict | None:
    """Compare the model's calibration to the de-vigged bookmaker market and
    a coin-flip baseline, over graded games where market odds are on file."""
    import numpy as np

    path = DATA_DIR / "market_odds.csv"
    if not path.exists():
        return None
    mkt = pd.read_csv(path, dtype={"date": str})
    m = graded.merge(mkt, on=["date", "home", "away"], how="inner")
    if m.empty:
        return None

    eps = 1e-12
    model_ll, market_ll, unif_ll = [], [], []
    for r in m.itertuples(index=False):
        col = _OUTCOME_COL[r.actual_outcome]
        model_p = float(getattr(r, col))
        inv = np.array([1 / r.odds_home, 1 / r.odds_draw, 1 / r.odds_away])
        inv = inv / inv.sum()
        market_p = inv[{"home": 0, "draw": 1, "away": 2}[r.actual_outcome]]
        model_ll.append(-np.log(max(model_p, eps)))
        market_ll.append(-np.log(max(market_p, eps)))
        unif_ll.append(-np.log(1 / 3))
    return {
        "n": len(m),
        "model_logloss": float(np.mean(model_ll)),
        "market_logloss": float(np.mean(market_ll)),
        "uniform_logloss": float(np.mean(unif_ll)),
        "beat_market": float(np.mean(model_ll)) < float(np.mean(market_ll)),
    }
