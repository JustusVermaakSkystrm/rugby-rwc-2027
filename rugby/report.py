"""Readable outputs: markdown report + CSVs in rugby/outputs/."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from .ratings import expected_score
from .simulator import (KO_DRAW_ELO_TILT, MatchPredictor, SimResults,
                        allocate_thirds, load_bracket, pool_table, rank_pool)

OUT_DIR = Path(__file__).parent / "outputs"

KO_TITLES = [("round_of_16", "Round of 16"),
             ("quarterfinals", "Quarter-finals"),
             ("semifinals", "Semi-finals")]


def _pct(x: float) -> str:
    return f"{100 * x:.1f}%"


def _oriented(pred: MatchPredictor, home: str, away: str):
    """Return (p_home_win, p_draw, p_away_win, exp_margin, exp_total) oriented
    to the requested (home, away), accounting for host-home swapping."""
    who_home, dist = pred.dist(home, away)
    ph, draw = dist.win_prob_home, dist.draw_prob
    pa = max(1.0 - ph - draw, 0.0)
    margin = dist.exp_margin
    if who_home != home:                       # predictor put host as home
        ph, pa = pa, ph
        margin = -margin
    return ph, draw, pa, margin, dist.exp_total


def _advance_prob(pred: MatchPredictor, elo: dict, a: str, b: str) -> float:
    """Analytic P(team a advances): win in regulation, or draw then win extra
    time / kicks (resolved near the Elo expectancy)."""
    who_home, dist = pred.dist(a, b)
    other = b if who_home == a else a
    tilt = 0.5 + KO_DRAW_ELO_TILT * (
        expected_score(elo.get(who_home, 1500), elo.get(other, 1500)) - 0.5)
    p_home_adv = dist.win_prob_home + dist.draw_prob * np.clip(tilt, 0, 1)
    p_home_adv = float(np.clip(p_home_adv, 0.01, 0.99))
    return p_home_adv if who_home == a else 1.0 - p_home_adv


def match_probability_table(pred: MatchPredictor, fixtures: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for r in fixtures.itertuples(index=False):
        ph, draw, pa, margin, total = _oriented(pred, r.home_team, r.away_team)
        hp = int(round((total + margin) / 2))
        ap = int(round((total - margin) / 2))
        hp, ap = max(hp, 0), max(ap, 0)
        played = not (pd.isna(r.home_score) or pd.isna(r.away_score))
        rows.append({
            "date": r.date.date() if hasattr(r.date, "date") and pd.notna(r.date)
            else (r.date if pd.notna(r.date) else ""),
            "group": getattr(r, "group", ""), "home": r.home_team, "away": r.away_team,
            "status": "played" if played else "upcoming",
            "score": f"{int(r.home_score)}-{int(r.away_score)}" if played else "",
            "p_home_win": round(ph, 4), "p_draw": round(draw, 4),
            "p_away_win": round(pa, 4),
            "exp_home": f"{(total + margin) / 2:.1f}",
            "exp_away": f"{(total - margin) / 2:.1f}",
            "most_likely_score": f"{hp}-{ap}",
        })
    return pd.DataFrame(rows)


def predicted_bracket(pred: MatchPredictor, res: SimResults, elo: dict) -> dict:
    """A single self-consistent most-likely tournament path: modal group
    finishes from simulation frequencies, knockout ties decided by the
    analytic advance probability of the projected pairing."""
    bracket = load_bracket()
    tt = res.team_table().set_index("team")
    slots, modal_thirds = {}, []
    for g, members in res.groups.items():
        remaining = list(members)
        order = []
        for col in ("p_win_pool", "p_runner_up", "p_third"):
            pick = max(remaining, key=lambda t: tt.loc[t, col])
            order.append(pick)
            remaining.remove(pick)
        order.append(remaining[0])
        slots[f"W_{g}"], slots[f"RU_{g}"] = order[0], order[1]
        modal_thirds.append((g, order[2]))

    thirds_sorted = sorted(modal_thirds,
                           key=lambda r: tt.loc[r[1], "p_third_advance"],
                           reverse=True)[:4]
    slots.update(allocate_thirds(thirds_sorted, bracket["third_place_slots"]))

    path, adv = {}, {}
    for key, _title in KO_TITLES:
        ties = []
        for m in bracket[key]:
            home = slots.get(m["home"]) or adv[m["home"]]
            away = slots.get(m["away"]) or adv[m["away"]]
            p_home = _advance_prob(pred, elo, home, away)
            winner = home if p_home >= 0.5 else away
            adv[f"W_{m['match']}"] = winner
            adv[f"L_{m['match']}"] = away if winner == home else home
            ties.append({"match": m["match"], "date": m["date"],
                         "venue": m["venue"], "home": home, "away": away,
                         "p_home_advance": p_home, "winner": winner})
        path[key] = ties

    for slot_key, single in (("final", bracket["final"]),
                             ("bronze_final", bracket["bronze_final"])):
        fh = adv[single["home"]]
        fa = adv[single["away"]]
        p_home = _advance_prob(pred, elo, fh, fa)
        path[slot_key] = [{"match": single["match"], "date": single["date"],
                           "venue": single["venue"], "home": fh, "away": fa,
                           "p_home_advance": p_home,
                           "winner": fh if p_home >= 0.5 else fa}]
    return path


def current_group_tables(fixtures: pd.DataFrame, groups: dict) -> dict:
    """Actual pool standings from played matches only, with rugby bonus
    points (display order: pts, points-diff, tries)."""
    tables = {}
    played = fixtures.dropna(subset=["home_score", "away_score"])
    for g, members in groups.items():
        sub = played[played["group"] == g]
        results = [(r.home_team, r.away_team, int(r.home_score), int(r.away_score),
                    int(r.home_tries) if pd.notna(r.home_tries) else 0,
                    int(r.away_tries) if pd.notna(r.away_tries) else 0)
                   for r in sub.itertuples(index=False)]
        stats = pool_table(members, results)
        played_count = {t: 0 for t in members}
        for h, a, *_ in results:
            played_count[h] += 1
            played_count[a] += 1
        rows = [{"team": t, "P": played_count[t], "Pts": v[0], "PD": v[1],
                 "TF": v[4]} for t, v in stats.items()]
        df = pd.DataFrame(rows).sort_values(["Pts", "PD", "TF", "team"],
                                            ascending=[False, False, False, True])
        tables[g] = df.reset_index(drop=True)
    return tables


# ----------------------------------------------------------------- writing

def write_outputs(pred: MatchPredictor, res: SimResults, fixtures: pd.DataFrame,
                  meta: dict) -> None:
    OUT_DIR.mkdir(exist_ok=True)
    elo = {t: pred.state.elo.get(t) for g in res.groups.values() for t in g}

    matches = match_probability_table(pred, fixtures)
    matches.to_csv(OUT_DIR / "match_probabilities.csv", index=False)

    from .scorecard import summary, update_log
    meta["scorecard"] = summary(update_log(matches))

    tt = res.team_table()
    prev = _load_previous_projections()
    deltas = _compute_deltas(tt, prev)

    proj = tt.copy()
    proj.insert(0, "data_through", meta["data_through"])
    proj.insert(1, "n_sims", meta["n_sims"])
    proj.round(4).to_csv(OUT_DIR / "tournament_projections.csv", index=False)
    _append_history(proj)

    bracket_path = predicted_bracket(pred, res, elo)
    md = _render_markdown(pred, res, fixtures, tt, bracket_path, elo, meta, deltas)
    (OUT_DIR / "report.md").write_text(md)
    archive = OUT_DIR / "archive"
    archive.mkdir(exist_ok=True)
    (archive / f"report_{meta['data_through']}.md").write_text(md)

    try:
        from .site import build_site
        build_site()
    except ImportError:
        pass


def _load_previous_projections() -> pd.DataFrame | None:
    path = OUT_DIR / "tournament_projections.csv"
    return pd.read_csv(path) if path.exists() else None


def _append_history(proj: pd.DataFrame) -> None:
    path = OUT_DIR / "history.csv"
    proj = proj.copy()
    proj.insert(0, "run_at", pd.Timestamp.now().isoformat(timespec="seconds"))
    proj.round(4).to_csv(path, mode="a", header=not path.exists(), index=False)


DELTA_COLS = ["p_champion", "p_final", "p_SF", "p_QF", "p_R16",
              "p_win_pool", "exp_points"]


def _compute_deltas(tt: pd.DataFrame, prev: pd.DataFrame | None) -> dict | None:
    if prev is None or "team" not in prev.columns:
        return None
    merged = tt.merge(prev[["team"] + [c for c in DELTA_COLS if c in prev.columns]],
                      on="team", how="left", suffixes=("", "_prev"))
    delta = {}
    for c in DELTA_COLS:
        if f"{c}_prev" in merged.columns:
            delta[c] = dict(zip(merged["team"], merged[c] - merged[f"{c}_prev"]))
    label = str(prev["data_through"].iloc[0]) if "data_through" in prev.columns \
        else "previous run"
    return {"deltas": delta, "prev_label": label}


def _fmt_delta(x: float, threshold: float = 0.0005) -> str:
    if x != x:
        return "new"
    if abs(x) < threshold:
        return "–"
    return f"{100 * x:+.1f}"


def _render_markdown(pred, res: SimResults, fixtures, tt, bracket_path, elo,
                     meta, deltas=None) -> str:
    L = []
    add = L.append
    n_played = int(fixtures["home_score"].notna().sum())
    add("# Rugby World Cup 2027 — ML Prediction Report\n")
    add(f"*Generated {date.today().isoformat()} · data through "
        f"**{meta['data_through']}** · {meta['n_sims']:,} Monte Carlo simulations · "
        f"{n_played}/36 pool matches played*\n")
    add(f"Probabilities come from a **{meta.get('model_label', 'rugby points')} "
        "model** (World Rugby ranking + Elo strength, points attack/defence, "
        f"rolling form, venue/importance) trained on {meta.get('n_train', 0):,} "
        "internationals, simulated through the official RWC 2027 bracket with "
        "bonus-point pool standings and tiebreakers.\n")
    if meta.get("validation"):
        v = meta["validation"]
        add(f"*Rolling validation ({v['n_test']:,} matches): chosen model "
            f"**{v['best']}** — RPS {v['model_rps']:.4f} vs ranking-only baseline "
            f"{v['baseline_rps']:.4f}; margin MAE {v['model_margin_mae']:.2f} pts "
            f"vs {v['baseline_margin_mae']:.2f}.*\n")

    add("## Title favourites\n")
    dch = deltas["deltas"].get("p_champion", {}) if deltas else {}
    dcol = f" Δ vs {deltas['prev_label']} |" if deltas else ""
    add(f"| # | Team | Pool | Champion |{dcol} Final | Semi | "
        "Quarter | Rd of 16 |")
    add("|---|------|:----:|---------:|" + ("-------:|" if deltas else "")
        + "------:|----:|--------:|---------:|")
    for i, r in tt.head(12).iterrows():
        dcell = f" {_fmt_delta(dch.get(r['team'], float('nan')))} |" if deltas else ""
        add(f"| {i + 1} | {r['team']} | {r['group']} | **{_pct(r['p_champion'])}** |"
            f"{dcell} {_pct(r['p_final'])} | {_pct(r['p_SF'])} | {_pct(r['p_QF'])} | "
            f"{_pct(r['p_R16'])} |")
    add("")

    if deltas and deltas["deltas"].get("p_champion"):
        ch = pd.Series(deltas["deltas"]["p_champion"]).dropna()
        if not ch.empty and ch.abs().max() >= 0.0005:
            add(f"## Biggest movers since last run ({deltas['prev_label']})\n")
            r16 = pd.Series(deltas["deltas"].get("p_R16", {})).dropna()
            movers = ch.abs().sort_values(ascending=False).head(6).index
            add("| Team | Δ Champion | Δ Rd of 16 | Champion now |")
            add("|------|----------:|-----------:|-------------:|")
            tti = tt.set_index("team")
            for t in sorted(movers, key=lambda t: ch[t], reverse=True):
                add(f"| {t} | {_fmt_delta(ch[t])} | "
                    f"{_fmt_delta(r16.get(t, float('nan')))} | "
                    f"{_pct(tti.loc[t, 'p_champion'])} |")
            add("")

    from .viz import bracket_svg
    champ = bracket_path["final"][0]["winner"]
    champ_prob = float(tt.set_index("team").loc[champ, "p_champion"])
    add("## Path to the final\n")
    add("The model's single most likely knockout bracket — every projected tie "
        "from the Round of 16 down to the champion. Percentages are each side's "
        "chance of advancing from that tie.\n")
    add('<div style="overflow-x:auto; margin:1rem 0;">')
    add(bracket_svg(bracket_path, champ, champ_prob))
    add('</div>\n')

    add("## Pool projections\n")
    from .dataset import load_teams
    groups_cfg = load_teams()["groups"]
    cur = current_group_tables(fixtures, groups_cfg)
    tti = tt.set_index("team")
    for g, members in groups_cfg.items():
        add(f"### Pool {g}\n")
        table = cur[g]
        if table["P"].sum() > 0:
            add("| Team | P | Pts | PD | Tries | xPts | Win pool | Top 2 | Advance* |")
            add("|------|--:|----:|---:|------:|-----:|---------:|------:|--------:|")
            for r in table.itertuples(index=False):
                p = tti.loc[r.team]
                adv = p["p_win_pool"] + p["p_runner_up"] + p["p_third_advance"]
                add(f"| {r.team} | {r.P} | **{r.Pts}** | {r.PD:+d} | {r.TF} | "
                    f"{p['exp_points']:.2f} | {_pct(p['p_win_pool'])} | "
                    f"{_pct(p['p_win_pool'] + p['p_runner_up'])} | {_pct(adv)} |")
        else:
            add("| Team | xPts | Win pool | Top 2 | Advance* |")
            add("|------|-----:|---------:|------:|--------:|")
            order = sorted(members, key=lambda t: tti.loc[t, "exp_points"],
                           reverse=True)
            for t in order:
                p = tti.loc[t]
                adv = p["p_win_pool"] + p["p_runner_up"] + p["p_third_advance"]
                add(f"| {t} | {p['exp_points']:.2f} | {_pct(p['p_win_pool'])} | "
                    f"{_pct(p['p_win_pool'] + p['p_runner_up'])} | {_pct(adv)} |")
        add("")
    add("*\\*Advance = top two of the pool or one of the four best "
        "third-placed teams.*\n")

    add("## Most likely knockout bracket\n")
    add("Each tie shows the projected pairing and the named side's chance of "
        "advancing in that pairing.\n")
    for key, title in KO_TITLES + [("bronze_final", "Bronze final"),
                                   ("final", "Final")]:
        add(f"### {title}\n")
        add("| Match | Date | Venue | Tie | Projected winner | Win prob |")
        add("|:-----:|------|-------|-----|------------------|---------:|")
        for t in bracket_path[key]:
            p = t["p_home_advance"] if t["winner"] == t["home"] else 1 - t["p_home_advance"]
            add(f"| {t['match']} | {t['date']} | {t['venue']} | "
                f"{t['home']} v {t['away']} | **{t['winner']}** | {_pct(p)} |")
        add("")
    add(f"**Projected champion: {champ}** (overall title probability "
        f"{_pct(champ_prob)} — the single path above is only one of many ways "
        "the tournament can unfold).\n")

    add("## How to read this\n")
    add("- All figures are probabilities, not certainties — a 65% favourite "
        "still loses about one such match in three.")
    add("- Rugby is more predictable than football (few draws, favourites hold "
        "more often), but 2027 is well out, so early forecasts are "
        "low-information and will sharpen as warm-up tests are played.")
    add("- `xPts` = expected pool points (incl. bonus points). Predictions "
        "refresh hourly: `python -m rugby.run all`.")
    add("- Machine-readable outputs: `match_probabilities.csv`, "
        "`tournament_projections.csv`. Past reports in `outputs/archive/`.")

    sc = meta.get("scorecard")
    if sc:
        add("\n## Model scorecard\n")
        add(f"**{sc['hits']} of {sc['n']} match outcomes called correctly** "
            f"(model expected ≈{sc['expected_hits']:.1f}) · average probability "
            f"on what actually happened: **{_pct(sc['mean_p_actual'])}** "
            "(33.3% = guessing).\n")
        bm = sc.get("benchmark")
        if bm:
            gap = bm["model_logloss"] - bm["market_logloss"]
            vs = ("essentially level with" if abs(gap) < 0.05
                  else ("ahead of" if gap < 0 else "behind"))
            add("| Forecaster | Log-loss |")
            add("|------------|---------:|")
            add(f"| **This model** | **{bm['model_logloss']:.3f}** |")
            add(f"| Bookmaker (de-vigged) | {bm['market_logloss']:.3f} |")
            add(f"| Coin-flip | {bm['uniform_logloss']:.3f} |")
            add(f"\nThe model is **{vs} the market** ({gap:+.3f} log-loss).\n")
        add("\n*Predictions are frozen at the last run before each result "
            "arrives, then graded — never grading a model that has seen the "
            "answer.*\n")
    return "\n".join(L) + "\n"
