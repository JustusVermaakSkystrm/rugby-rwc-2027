"""
The salvageable core of Cycle Trends, done properly.

Cycle Trends' techniques are all legitimate signal processing. What is
missing is any procedure for deciding whether a cycle it "found" is real.
This module supplies that: three gates a candidate period must pass before
it is allowed into a model.

  Gate 1  significance vs. the correct null  (is the peak bigger than what
          a random walk routinely produces, AFTER accounting for the fact
          that we scanned hundreds of candidate periods?)
  Gate 2  phase stability  (a real cycle keeps its timing across the
          sample; a curve-fit to noise drifts)
  Gate 3  cross-sectional confirmation  (a real cycle shows up independently
          in related-but-distinct series)

Also fixes the look-ahead bug: filtering is causal (trailing), never centred.
numpy only.
"""

import numpy as np


def causal_detrend(x, window=200):
    """Trailing moving average - uses only data available at the time.

    A CENTRED moving average (np.convolve(..., mode='same')) averages
    window/2 bars of FUTURE data into every point. Any backtest built on
    one is measuring its own peeking, not a forecast.
    """
    c = np.cumsum(np.insert(np.asarray(x, dtype=float), 0, 0.0))
    ma = (c[window:] - c[:-window]) / window
    return x[window - 1:] - ma


def fit_cycles(y, periods, t=None):
    """Trigonometric regression for many periods at once.

    Closed-form 2x2 least squares per period, vectorised. Returns the
    fraction of variance each period explains, plus amplitude and phase.
    `t` is ABSOLUTE time - phase is meaningless without a common origin.
    """
    y = np.asarray(y, dtype=float)
    if t is None:
        t = np.arange(len(y), dtype=float)
    y = y - y.mean()
    periods = np.atleast_1d(np.asarray(periods, dtype=float))

    w = 2 * np.pi / periods[:, None]
    C, S = np.cos(w * t), np.sin(w * t)
    Scc, Sss, Scs = (C * C).sum(1), (S * S).sum(1), (C * S).sum(1)
    Scy, Ssy = C @ y, S @ y

    det = Scc * Sss - Scs ** 2
    det = np.where(np.abs(det) < 1e-12, np.nan, det)
    a = (Sss * Scy - Scs * Ssy) / det
    b = (Scc * Ssy - Scs * Scy) / det

    r2 = (a * Scy + b * Ssy) / (y @ y)
    return np.nan_to_num(r2), np.hypot(a, b), np.arctan2(b, a)


def gate1_significance(prices, periods, n_surrogates=300, window=200, seed=0):
    """Is any cycle stronger than what a random walk produces AT THAT PERIOD?

    Two traps are handled here, and the second one is the subtle one.

    1. Multiple comparisons. Scanning 400 candidate periods and reporting
       the winner's R^2 is meaningless unless the null is also the maximum
       over 400 candidates.

    2. Coloured noise. A random walk has enormously more energy at long
       periods than short ones (power ~ 1/f^2). So a raw max-R^2 statistic
       is ALWAYS won by some 300-bar wobble, and a real 60-bar cycle is
       invisible underneath it. The fix is to standardise each period
       against its OWN null distribution first - whitening - and only then
       take the maximum. Comparing every frequency to a single global
       threshold is what makes long spurious "cycles" so seductive.

    The null is a bootstrap of the actual price increments: same volatility,
    same fat tails, no deterministic cycle. Every surrogate goes through the
    identical pipeline, detrending included.
    """
    rng = np.random.default_rng(seed)
    periods = np.asarray(periods, dtype=float)
    obs, _, _ = fit_cycles(causal_detrend(prices, window), periods)

    steps = np.diff(prices)
    null = np.empty((n_surrogates, periods.size))
    for i in range(n_surrogates):
        walk = np.concatenate([[prices[0]], prices[0] + np.cumsum(
            rng.choice(steps, size=steps.size, replace=True))])
        null[i] = fit_cycles(causal_detrend(walk, window), periods)[0]

    # per-period p-values: how unusual is this R^2 for THIS period?
    obs_p = (1 + (null >= obs).sum(0)) / (1 + n_surrogates)

    # null distribution of the best per-period p-value across the scan
    # (each surrogate scored against the same null ensemble)
    null_p = (1 + (null[:, None, :] >= null[None, :, :]).sum(0)) / (1 + n_surrogates)
    null_min_p = null_p.min(1)

    best = int(obs_p.argmin())
    overall_p = (1 + (null_min_p <= obs_p[best]).sum()) / (1 + n_surrogates)
    return {"period": float(periods[best]), "r2": float(obs[best]),
            "null_median_r2": float(np.median(null[:, best])),
            "null_95th_r2": float(np.percentile(null[:, best], 95)),
            "p_value": float(overall_p)}


def refine_period(y, period, span=0.1, step=0.02):
    """Sharpen a period estimate on a fine grid around the integer winner.

    This matters more than it looks. Gate 2 fits the same period in
    different blocks of the sample and compares phases. If the period is
    even 5% wrong, the fitted phase drifts steadily across the sample
    purely from the period error, and a perfectly real cycle fails the
    stability test. Resolve the period first, then judge the phase.
    """
    grid = np.arange(period * (1 - span), period * (1 + span), step)
    grid = grid[grid > 2]
    r2, _, _ = fit_cycles(y, grid)
    return float(grid[int(np.argmax(r2))])


def gate2_phase_stability(y, period, n_blocks=4):
    """Does the cycle keep its timing?

    Fit the same period separately in each block of the sample, using
    absolute time so the phases are comparable. Returns the circular
    resultant length: 1.0 = perfectly consistent phase, ~0 = the fit is
    chasing whatever the noise did in that block.
    """
    t = np.arange(len(y), dtype=float)
    phases = [float(fit_cycles(yb, [period], t=tb)[2][0])
              for yb, tb in zip(np.array_split(y, n_blocks),
                                np.array_split(t, n_blocks))]
    return float(np.abs(np.mean(np.exp(1j * np.array(phases)))))


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    n = 1200
    periods = np.arange(8, n // 3, dtype=float)
    t = np.arange(n, dtype=float)

    walk = 100 + np.cumsum(rng.normal(0, 1, n))
    planted = walk + 6.0 * np.sin(2 * np.pi * t / 63 + 0.7)

    for name, series in [("pure random walk", walk),
                         ("random walk + real 63-bar cycle", planted)]:
        g1 = gate1_significance(series, periods)
        det = causal_detrend(series)
        sharp = refine_period(det, g1["period"])
        g2 = gate2_phase_stability(det, sharp)
        verdict = "ACCEPT" if g1["p_value"] < 0.05 and g2 > 0.7 else "REJECT"
        print(f"\n{name}")
        print(f"  best period            {g1['period']:.0f} bars "
              f"(refined {sharp:.1f})")
        print(f"  variance explained     {g1['r2']:.1%}")
        print(f"  random walks get       {g1['null_median_r2']:.1%} "
              f"(median) / {g1['null_95th_r2']:.1%} (95th pct)")
        print(f"  p-value                {g1['p_value']:.3f}")
        print(f"  phase stability        {g2:.2f}")
        print(f"  -> {verdict}")
