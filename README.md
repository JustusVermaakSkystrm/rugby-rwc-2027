# Rugby World Cup 2027 — ML prediction engine

An auto-updating machine-learning prediction engine for the **Men's Rugby
World Cup 2027** (Australia, 1 Oct – 13 Nov 2027): probability outputs for
every match, a full Monte-Carlo tournament simulation (pool standings →
knockouts → final), a "path to the final" bracket, a model scorecard with a
market benchmark, and a static site that refreshes hourly.

**Live site:** `https://<owner>.github.io/rugby-rwc-2027/`

## What it does

- **Strength ratings** ([`ratings.py`](rugby/ratings.py)) — a World-Rugby-flavoured Elo
  (importance-weighted, home advantage, margin multiplier) seeded from the
  official World Rugby ranking points, plus per-team attack/defence in points
  space.
- **Leak-free features** ([`dataset.py`](rugby/dataset.py)) — a single chronological pass
  builds point-in-time training rows from 3,600+ internationals (1995–2026)
  with no lookahead.
- **Scoring model** ([`model.py`](rugby/model.py)) — rugby points are not low-integer
  Poisson goals, so two models are built behind one interface: a **margin +
  total Gaussian** model and a **per-side negative-binomial** model. Spread is
  estimated out-of-fold so the win/draw/loss probabilities stay calibrated. A
  try estimator maps points to try counts for the bonus-point system. Rolling
  validation picks the winner against a ranking-only baseline.
- **Tournament simulator** ([`simulator.py`](rugby/simulator.py)) — Monte-Carlo over the
  24-team, 6-pool format with the official **bonus-point** standings (win 4 /
  draw 2 / loss 0, +1 for 4+ tries, +1 for losing by ≤7), rugby pool
  tiebreakers, the four-best-thirds → Round-of-16 allocation, and the
  R16 → QF → SF → bronze/final knockout tree. Australia gets host advantage.
- **Outputs** ([`report.py`](rugby/report.py), [`site.py`](rugby/site.py), [`viz.py`](rugby/viz.py),
  [`scorecard.py`](rugby/scorecard.py)) — markdown report, machine-readable CSVs, an
  inline SVG bracket, and a frozen-prediction scorecard graded against results
  and (optionally) bookmaker odds.
- **Live result handling** ([`ledger.py`](rugby/ledger.py), [`official.py`](rugby/official.py)) —
  full-time scores are confirmed via ESPN's public scoreboard and quarantined
  until trustworthy, so a mid-match score never enters a simulation.

## Usage

```bash
pip install -r rugby/requirements.txt
python -m rugby.run all --sims 50000     # update + validate/train + simulate
# or individually:
python -m rugby.run update                # confirm live results, run ledger
python -m rugby.run train                 # rolling validation + fit best model
python -m rugby.run simulate --sims 50000 # Monte Carlo + report + site
python -m rugby.site                       # rebuild outputs/site/index.html
```

Outputs land in [`rugby/outputs/`](rugby/outputs): `report.md`,
`match_probabilities.csv`, `tournament_projections.csv`, `history.csv`, and
`site/index.html`.

## Deployment

- **Hourly cloud refresh:** [`.github/workflows/rwc-hourly.yml`](.github/workflows/rwc-hourly.yml)
  re-confirms results, re-simulates when something changed, and publishes the
  site to GitHub Pages. Enable **Settings → Pages → Source: GitHub Actions**.
- **Reliable hourly trigger** from a Mac: see
  [`rugby/scheduling/README.md`](rugby/scheduling/README.md).

## Data

- `rugby/data/results.csv` — men's international test results (1871–2026;
  dense from 1995), ESPN + Wikipedia sourced, with try counts where available
  (~21% of rows). Rebuilt by the helpers in [`scripts/`](scripts).
- `rugby/data/rankings.json` — World Rugby ranking points (the Elo prior).
- `rugby/data/teams.json`, `rugby/data/bracket.json` — the confirmed RWC 2027
  pools and knockout template.

## Caveats

- Rugby is *more* predictable than football (few draws, favourites hold), so
  expect a higher hit-rate — but 2027 is well out, so until warm-up tests are
  played the forecasts are low-information and will sharpen over time.
- Historical try coverage is partial; the try estimator learns the
  points→tries relationship where tries are recorded and falls back to a
  parametric rate elsewhere.
