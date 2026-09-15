# Cycle research

Two standalone scripts from the Cycle Trends investigation, kept here because
they are the validation layer for anything built on the recorded data.

**`cycletrends_method.py`** — a reconstruction of the composite-cycle method
Cycle Trends sells: de-trend, fit ~20 periods by trigonometric regression, sum
them, project forward. Run it and it finds twenty strong cycles in a pure
random walk, fits the past beautifully, and forecasts worse than a flat line.
That is the method's problem in four numbers.

**`cycle_gate.py`** — the part that is missing. Three gates a candidate cycle
must pass before it is allowed into a model:

1. significance against a bootstrap-of-increments null, standardised
   per-frequency first (a random walk has far more energy at long periods, so
   an un-whitened maximum is always won by some spurious 300-bar wobble)
2. phase stability across sub-samples
3. cross-sectional confirmation in related instruments — not yet implemented,
   and the strongest of the three

```bash
python research/cycle_gate.py
```

On a pure random walk it rejects. On a random walk with a real 63-bar cycle
buried in it, it recovers the period as 62.5 and accepts at p=0.003.

Use it on any periodicity claim before trading it, including your own.
