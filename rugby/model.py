"""Scoring models for rugby tests.

Rugby points are not low-integer Poisson goals (try=5, conv=2, penalty/drop=3;
match totals ~10-50), so the football goal model is replaced by two rugby
points models behind a common interface:

  - ``MarginTotalModel`` — gradient-boosted regressors for the match *margin*
    (home - away) and *total* points, with Gaussian residual spread. Scorelines
    follow by splitting a sampled (margin, total). Win probability is the clean
    closed form P(margin > 0).

  - ``NegBinomModel`` — gradient-boosted regressors for each side's points,
    sampled as negative-binomial counts to capture rugby's over-dispersion.

Both expose ``.pairing(features) -> PairingDist`` which the Monte-Carlo
simulator samples. A ``TryModel`` maps sampled points to a try count (learned
from matches where tries are recorded, with a parametric fallback) so the
simulator can award the 4-try and losing bonuses.

``evaluate_rolling`` runs rolling-origin validation (margin MAE, total MAE,
3-way log-loss and RPS) for both models against a ranking-only baseline and
reports which wins; ``fit_best`` fits the winner on all data.
"""

from __future__ import annotations

import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.model_selection import KFold

from .dataset import FEATURES, FEATURES_BASELINE

MODEL_PATH = Path(__file__).parent / "data" / "score_model.pkl"
WEIGHT_HALF_LIFE_YEARS = 8.0
MAX_POINTS = 100
DRAW_HALF_WIDTH = 0.5          # |margin| < this rounds to a draw


def _recency_weights(dates: pd.Series) -> np.ndarray:
    age_years = (dates.max() - dates).dt.days / 365.25
    return np.power(0.5, age_years / WEIGHT_HALF_LIFE_YEARS).to_numpy()


def _reg(loss: str = "squared_error") -> HistGradientBoostingRegressor:
    # Early stopping curbs the overfitting that would otherwise make in-sample
    # residuals (and thus forecast spread) far too small.
    return HistGradientBoostingRegressor(
        loss=loss, max_iter=400, learning_rate=0.05,
        max_leaf_nodes=15, min_samples_leaf=60,
        l2_regularization=2.0, early_stopping=True,
        validation_fraction=0.15, n_iter_no_change=20, random_state=7,
    )


def _oof_predict(loss: str, X: pd.DataFrame, y: np.ndarray, w: np.ndarray,
                 k: int = 5) -> np.ndarray:
    """Out-of-fold predictions, so residual spread reflects genuine forecast
    error rather than in-sample overfit. Honest spread is what keeps the
    win/draw/loss probabilities calibrated."""
    oof = np.empty(len(y), dtype=float)
    kf = KFold(n_splits=k, shuffle=True, random_state=7)
    Xv = X.to_numpy()
    for tr, te in kf.split(Xv):
        m = _reg(loss).fit(X.iloc[tr], y[tr], sample_weight=w[tr])
        oof[te] = m.predict(X.iloc[te])
    return oof


# --------------------------------------------------------------- try model

@dataclass
class TryModel:
    """E[tries | points scored], learned where tries are recorded.

    Falls back to a parametric mean (a try plus conversion is ~7 points, but
    penalties and missed kicks dilute that) when there is no try data.
    """
    reg: HistGradientBoostingRegressor | None = None
    fallback_rate: float = 1.0 / 6.6

    def fit(self, table: pd.DataFrame) -> "TryModel":
        pts, tries = [], []
        for side in ("home", "away"):
            m = table[f"{side}_tries"] >= 0
            pts.append(table.loc[m, f"{side}_score"].to_numpy())
            tries.append(table.loc[m, f"{side}_tries"].to_numpy())
        pts = np.concatenate(pts)
        tries = np.concatenate(tries)
        if len(pts) >= 200:
            self.reg = _reg("poisson")
            self.reg.fit(pts.reshape(-1, 1), tries)
        else:
            self.reg = None
            if len(pts):
                self.fallback_rate = float(
                    tries.sum() / max(pts.sum(), 1)) or self.fallback_rate
        return self

    def rate(self, points: np.ndarray) -> np.ndarray:
        points = np.asarray(points, dtype=float)
        if self.reg is not None:
            lam = self.reg.predict(points.reshape(-1, 1))
        else:
            lam = points * self.fallback_rate
        return np.clip(lam, 0.05, 14.0)

    def sample(self, rng: np.random.Generator, points: np.ndarray) -> np.ndarray:
        return np.minimum(rng.poisson(self.rate(points)), 15)


# ------------------------------------------------------------- pairing dist

@dataclass
class PairingDist:
    """Per-pairing predictive distribution used by the simulator."""
    exp_margin: float
    exp_total: float
    win_prob_home: float
    draw_prob: float
    _sampler: Callable[[np.random.Generator, int], tuple[np.ndarray, np.ndarray]]
    _tries: TryModel

    def sample(self, rng: np.random.Generator, size: int):
        hp, ap = self._sampler(rng, size)
        hp = np.clip(hp, 0, MAX_POINTS).astype(np.int64)
        ap = np.clip(ap, 0, MAX_POINTS).astype(np.int64)
        ht = self._tries.sample(rng, hp)
        at = self._tries.sample(rng, ap)
        return hp, ap, ht, at


# ---------------------------------------------------------------- base API

class ScoreModel:
    name = "base"

    def __init__(self, features: list[str] | None = None):
        self.features = features or FEATURES
        self.tries = TryModel()

    # subclasses implement these ----------------------------------------
    def _fit_core(self, table: pd.DataFrame, w: np.ndarray) -> None: ...
    def _params(self, X: pd.DataFrame) -> dict: ...
    def _pairing(self, row: dict) -> PairingDist: ...

    # shared --------------------------------------------------------------
    def fit(self, table: pd.DataFrame) -> "ScoreModel":
        w = _recency_weights(table["date"])
        self._fit_core(table, w)
        self.tries.fit(table)
        return self

    def expected(self, X: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
        p = self._params(X)
        return p["mu_margin"], p["mu_total"]

    def outcome_probs(self, X: pd.DataFrame) -> np.ndarray:
        """(P home, P draw, P away) per row."""
        p = self._params(X)
        return self._outcome_from_params(p)

    def _outcome_from_params(self, p: dict) -> np.ndarray: ...

    def pairing(self, features: pd.DataFrame) -> PairingDist:
        row = {k: np.asarray(v)[0] for k, v in self._params(features).items()}
        return self._pairing(row)

    def save(self, path: Path = MODEL_PATH) -> None:
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path: Path = MODEL_PATH) -> "ScoreModel":
        with open(path, "rb") as f:
            return pickle.load(f)


# ------------------------------------------------------- margin/total model

class MarginTotalModel(ScoreModel):
    name = "margin_total"

    def _fit_core(self, table: pd.DataFrame, w: np.ndarray) -> None:
        X = table[self.features]
        ym, yt = table["margin"].to_numpy(), table["total"].to_numpy()
        self.m_margin = _reg("squared_error").fit(X, ym, sample_weight=w)
        self.m_total = _reg("squared_error").fit(X, yt, sample_weight=w)
        rm = ym - _oof_predict("squared_error", X, ym, w)
        rt = yt - _oof_predict("squared_error", X, yt, w)
        self.sd_margin = float(np.sqrt(np.average(rm ** 2, weights=w)))
        self.sd_total = float(np.sqrt(np.average(rt ** 2, weights=w)))

    def _params(self, X: pd.DataFrame) -> dict:
        Xf = X[self.features]
        mu_m = self.m_margin.predict(Xf)
        mu_t = np.clip(self.m_total.predict(Xf), 6.0, None)
        return {"mu_margin": mu_m, "mu_total": mu_t,
                "sd_margin": np.full(len(Xf), self.sd_margin),
                "sd_total": np.full(len(Xf), self.sd_total)}

    def _outcome_from_params(self, p: dict) -> np.ndarray:
        mu, sd = p["mu_margin"], p["sd_margin"]
        away = norm.cdf((-DRAW_HALF_WIDTH - mu) / sd)
        home = 1.0 - norm.cdf((DRAW_HALF_WIDTH - mu) / sd)
        draw = np.clip(1.0 - home - away, 1e-6, None)
        return np.column_stack([home, draw, away])

    def _pairing(self, r: dict) -> PairingDist:
        mu_m, mu_t = float(r["mu_margin"]), float(r["mu_total"])
        sd_m, sd_t = float(r["sd_margin"]), float(r["sd_total"])

        def sampler(rng, size):
            margin = rng.normal(mu_m, sd_m, size)
            total = np.clip(rng.normal(mu_t, sd_t, size), 0, None)
            hp = np.rint((total + margin) / 2.0)
            ap = np.rint((total - margin) / 2.0)
            neg = ap < 0
            hp[neg] -= ap[neg]
            ap[neg] = 0
            neg = hp < 0
            ap[neg] -= hp[neg]
            hp[neg] = 0
            return hp, ap

        probs = self._outcome_from_params(
            {"mu_margin": np.array([mu_m]), "sd_margin": np.array([sd_m])})[0]
        return PairingDist(mu_m, mu_t, float(probs[0]), float(probs[1]),
                           sampler, self.tries)


# ------------------------------------------------------- negative-binomial

class NegBinomModel(ScoreModel):
    name = "neg_binom"

    def _fit_core(self, table: pd.DataFrame, w: np.ndarray) -> None:
        X = table[self.features]
        yh, ya = table["home_score"].to_numpy(), table["away_score"].to_numpy()
        self.m_home = _reg("poisson").fit(X, yh, sample_weight=w)
        self.m_away = _reg("poisson").fit(X, ya, sample_weight=w)
        # Pooled over-dispersion (method of moments) from OUT-OF-FOLD means:
        # Var = mu + mu^2 / r. In-sample means understate the variance.
        mu = np.concatenate([_oof_predict("poisson", X, yh, w),
                             _oof_predict("poisson", X, ya, w)])
        obs = np.concatenate([yh, ya])
        ww = np.concatenate([w, w])
        var = np.average((obs - mu) ** 2, weights=ww)
        mbar = np.average(mu, weights=ww)
        self.r = float(np.clip(mbar ** 2 / max(var - mbar, 1.0), 1.5, 60.0))

    def _params(self, X: pd.DataFrame) -> dict:
        Xf = X[self.features]
        mu_h = np.clip(self.m_home.predict(Xf), 1.0, None)
        mu_a = np.clip(self.m_away.predict(Xf), 1.0, None)
        return {"mu_home": mu_h, "mu_away": mu_a,
                "mu_margin": mu_h - mu_a, "mu_total": mu_h + mu_a}

    def _nb_p(self, mu: np.ndarray) -> np.ndarray:
        return self.r / (self.r + mu)

    def _outcome_from_params(self, p: dict) -> np.ndarray:
        # Closed-form 3-way via a quick fixed-grid convolution would be exact
        # but heavy; a deterministic quadrature MC is plenty for validation.
        rng = np.random.default_rng(0)
        n = len(p["mu_home"])
        draws = 4000
        hp = rng.negative_binomial(self.r, self._nb_p(p["mu_home"])[:, None],
                                   size=(n, draws))
        ap = rng.negative_binomial(self.r, self._nb_p(p["mu_away"])[:, None],
                                   size=(n, draws))
        d = hp - ap
        home = (d > 0).mean(1)
        draw = np.clip((d == 0).mean(1), 1e-6, None)
        away = (d < 0).mean(1)
        return np.column_stack([home, draw, away])

    def _pairing(self, r: dict) -> PairingDist:
        mu_h, mu_a = float(r["mu_home"]), float(r["mu_away"])
        p_h, p_a = self.r / (self.r + mu_h), self.r / (self.r + mu_a)

        def sampler(rng, size):
            return (rng.negative_binomial(self.r, p_h, size),
                    rng.negative_binomial(self.r, p_a, size))

        probs = self._outcome_from_params(
            {"mu_home": np.array([mu_h]), "mu_away": np.array([mu_a])})[0]
        return PairingDist(mu_h - mu_a, mu_h + mu_a, float(probs[0]),
                           float(probs[1]), sampler, self.tries)


# ---------------------------------------------------------------- metrics

def _outcome_index(test: pd.DataFrame) -> np.ndarray:
    return np.where(test["margin"] > 0, 0,
                    np.where(test["margin"] == 0, 1, 2)).astype(int)


def _rps(probs: np.ndarray, idx: np.ndarray) -> float:
    cum = np.cumsum(probs, axis=1)
    obs = np.zeros_like(probs)
    obs[np.arange(len(idx)), idx] = 1.0
    return float(np.mean(np.sum((cum - np.cumsum(obs, 1)) ** 2, 1)
                         / (probs.shape[1] - 1)))


def _logloss(probs: np.ndarray, idx: np.ndarray) -> float:
    p = probs / probs.sum(1, keepdims=True)
    return float(-np.mean(np.log(p[np.arange(len(idx)), idx] + 1e-12)))


ROLLING_WINDOWS = [("2014-01-01", "2017-01-01"), ("2017-01-01", "2020-01-01"),
                   ("2020-01-01", "2023-01-01"), ("2023-01-01", "2027-01-01")]

MODELS = {"margin_total": MarginTotalModel, "neg_binom": NegBinomModel}


def evaluate_rolling(table: pd.DataFrame,
                     windows: list[tuple[str, str]] = ROLLING_WINDOWS,
                     ) -> pd.DataFrame:
    """Rolling-origin validation. For each window, train on everything before
    it and score the window. Compares a ranking-only baseline (margin from the
    Elo gap alone) with both full models."""
    rows = []
    for start, end in windows:
        train = table[table["date"] < start]
        test = table[(table["date"] >= start) & (table["date"] < end)]
        if len(test) < 20 or len(train) < 200:
            continue
        idx = _outcome_index(test)
        fitted = {
            "baseline": MarginTotalModel(features=FEATURES_BASELINE).fit(train),
            "margin_total": MarginTotalModel().fit(train),
            "neg_binom": NegBinomModel().fit(train),
        }
        for name, mdl in fitted.items():
            probs = mdl.outcome_probs(test)
            mu_m, mu_t = mdl.expected(test)
            rows.append({
                "window": f"{start[:4]}-{int(end[:4]) - 1}", "n_test": len(test),
                "model": name,
                "margin_mae": float(np.mean(np.abs(mu_m - test["margin"]))),
                "total_mae": float(np.mean(np.abs(mu_t - test["total"]))),
                "logloss": _logloss(probs, idx), "rps": _rps(probs, idx),
            })
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    agg = (df.groupby("model").apply(lambda g: pd.Series({
        "margin_mae": np.average(g["margin_mae"], weights=g["n_test"]),
        "total_mae": np.average(g["total_mae"], weights=g["n_test"]),
        "logloss": np.average(g["logloss"], weights=g["n_test"]),
        "rps": np.average(g["rps"], weights=g["n_test"]),
        "n_test": g["n_test"].sum()}), include_groups=False).reset_index())
    agg["window"] = "ALL"
    return pd.concat([df, agg], ignore_index=True)


def pick_best(evaluation: pd.DataFrame) -> str:
    """Lowest overall RPS among the real models wins (ties broken by log-loss)."""
    overall = evaluation[evaluation["window"] == "ALL"].set_index("model")
    cands = [m for m in MODELS if m in overall.index]
    return min(cands, key=lambda m: (overall.loc[m, "rps"],
                                     overall.loc[m, "logloss"]))


def fit_best(table: pd.DataFrame, name: str) -> ScoreModel:
    return MODELS[name]().fit(table)
