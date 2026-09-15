"""
A minimal reconstruction of the Cycle Trends / composite-cycle method.

The published description of Bacher's Cycle Trends is:
  "searches the raw data for whatever cycles are there, using Fourier
   transforms, trigonometric regression and array analysis. On average
   20 cycles are isolated, then combined and projected into the future."

That is a well-defined recipe, so it can be written out in ~80 lines:

  1. de-trend the price series with a low-pass ("Fourier") filter
  2. scan candidate periods, fitting each one by least squares (that is
     what "trigonometric regression" means: regress on sin/cos pairs)
  3. keep the N strongest periods, judged by variance explained
  4. add the fitted sine waves back onto the trend and extend the
     formula past the last bar -> the "future zone"

The last function is the part the sales material leaves out: it re-runs
the whole thing on an earlier cut of the data and compares the forecast
against what actually happened.

Only numpy is needed.
"""

import numpy as np


def detrend(x, window=200):
    """Remove the slow trend. Cycle analysis needs a series centred on zero,
    otherwise the trend itself dominates every fit. A centred moving average
    is the simple version of the 'Fourier filter' the program describes."""
    kernel = np.ones(window) / window
    trend = np.convolve(x, kernel, mode="same")
    # the convolution is unreliable at both ends, so hold the edges flat
    half = window // 2
    trend[:half] = trend[half]
    trend[-half:] = trend[-half - 1]
    return trend, x - trend


def fit_one_cycle(t, y, period):
    """Trigonometric regression for a single period.

    Fit y ~ a*cos(wt) + b*sin(wt) by least squares. Returns the fitted
    values, the coefficients, and how much of the variance this period
    explains. Fitting sin and cos separately is the standard trick that
    lets the phase fall out of a *linear* fit instead of needing a
    non-linear solver.
    """
    w = 2 * np.pi / period
    design = np.column_stack([np.cos(w * t), np.sin(w * t)])
    coef, *_ = np.linalg.lstsq(design, y, rcond=None)
    fitted = design @ coef
    explained = 1 - np.var(y - fitted) / np.var(y)
    return fitted, coef, explained


def find_cycles(y, n_cycles=20, min_period=8, max_period=None):
    """Greedy search for the strongest periods.

    Fit every candidate period, take the best one, subtract it, and repeat
    on the residual. Subtracting matters: without it the top 20 results are
    usually 20 near-copies of the same dominant cycle.
    """
    t = np.arange(len(y), dtype=float)
    max_period = max_period or len(y) // 3
    candidates = np.arange(min_period, max_period)

    residual = y.copy()
    found = []
    for _ in range(n_cycles):
        scores = [fit_one_cycle(t, residual, p)[2] for p in candidates]
        best = candidates[int(np.argmax(scores))]
        fitted, coef, explained = fit_one_cycle(t, residual, best)
        if explained <= 0:
            break
        found.append({"period": float(best), "coef": coef, "strength": explained})
        residual = residual - fitted
    return found


def project(cycles, n_history, n_future):
    """Sum the fitted cycles and carry the formula forward past the last bar.

    Nothing new is computed here. The 'forecast' is just the same sine waves
    evaluated at t > n_history, which is why it always looks so clean.
    """
    t = np.arange(n_history + n_future, dtype=float)
    out = np.zeros_like(t)
    for c in cycles:
        w = 2 * np.pi / c["period"]
        a, b = c["coef"]
        out += a * np.cos(w * t) + b * np.sin(w * t)
    return out


def composite_forecast(prices, n_future=60, n_cycles=20):
    trend, detrended = detrend(prices)
    cycles = find_cycles(detrended, n_cycles=n_cycles)
    wave = project(cycles, len(prices), n_future)
    # hold the trend flat over the forecast horizon
    baseline = np.concatenate([trend, np.full(n_future, trend[-1])])
    return baseline + wave, cycles


def honesty_check(prices, n_future=60, n_cycles=20):
    """Refit on data that stops n_future bars early, then compare the
    projection with what actually happened.

    This is the test the forum critics kept asking for. In-sample the
    composite tracks price beautifully; out-of-sample it usually does no
    better than a flat line, because the amplitudes and phases were chosen
    to fit the history that has already been seen.
    """
    cut = len(prices) - n_future
    fc, _ = composite_forecast(prices[:cut], n_future=n_future, n_cycles=n_cycles)

    actual = prices[cut:]
    predicted = fc[cut:]
    in_sample = fc[:cut]

    def rmse(a, b):
        return float(np.sqrt(np.mean((a - b) ** 2)))

    return {
        "in_sample_rmse": rmse(in_sample, prices[:cut]),
        "forecast_rmse": rmse(predicted, actual),
        "flat_line_rmse": rmse(np.full(n_future, prices[cut - 1]), actual),
        "direction_hit_rate": float(
            np.mean(np.sign(np.diff(predicted)) == np.sign(np.diff(actual)))
        ),
    }


if __name__ == "__main__":
    # a random walk: no real cycles exist in it at all
    rng = np.random.default_rng(0)
    prices = 100 + np.cumsum(rng.normal(0, 1, 1200))

    _, cycles = composite_forecast(prices)
    print("strongest periods found in pure noise:")
    for c in cycles[:5]:
        print(f"  {c['period']:6.1f} bars   explains {c['strength']:.1%} of residual")

    print()
    for k, v in honesty_check(prices).items():
        print(f"{k:22s} {v:.3f}")
