"""CLI for the Rugby World Cup 2027 prediction engine.

    python -m rugby.run update              # confirm live results, run ledger
    python -m rugby.run train               # validate + fit the score model
    python -m rugby.run simulate [--sims N] # Monte Carlo + reports
    python -m rugby.run all [--sims N]      # update + train + simulate
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from .dataset import (DATA_DIR, build_training_table, load_manual_results,
                      load_rankings, load_teams, merged_results)
from .ledger import apply_ledger, validate_results
from .model import (MODEL_PATH, ScoreModel, evaluate_rolling, fit_best,
                    pick_best)
from .report import write_outputs
from .simulator import (MatchPredictor, TournamentSimulator, attach_played,
                        generate_group_fixtures)

META_PATH = DATA_DIR / "last_validation.json"
N_POOL_MATCHES = 36
MODEL_LABELS = {"margin_total": "margin + total Gaussian",
                "neg_binom": "per-side negative-binomial"}


def cmd_update() -> None:
    """Refresh data/results.csv with newly-completed internationals (so
    ratings track warm-up tests), confirm completed RWC matches via the
    official scoreboard, and run live RWC scores through the validation
    ledger."""
    from .ingest import ingest_new_results, refresh_upcoming_fixtures
    added = ingest_new_results()
    if added:
        print(f"Ingested {len(added)} new international result(s):")
        for line in added:
            print(f"  + {line}")
    else:
        print("No new internationals to ingest.")
    n_up = refresh_upcoming_fixtures()
    print(f"Upcoming fixtures on file: {n_up}" if n_up
          else "No upcoming fixtures fetched (kept existing).")
    official_map = _refresh_official_results()
    fixtures = _rwc_fixtures(validated_only=False)
    scored = fixtures.dropna(subset=["home_score", "away_score"])
    summary = validate_results(scored, load_manual_results(), official=official_map)
    for kind in ("accepted", "quarantined", "corrected", "unstable"):
        for line in summary[kind]:
            print(f"  [{kind}] {line}")
    validated = _rwc_fixtures(validated_only=True)
    print(f"RWC 2027: {len(scored)}/{N_POOL_MATCHES} pool matches have raw "
          f"scores; {int(validated['home_score'].notna().sum())}/"
          f"{N_POOL_MATCHES} validated for simulation.")


def _refresh_official_results() -> dict:
    from .official import fetch_official_results
    teams = load_teams()
    all_teams = {t for g in teams["groups"].values() for t in g}
    confirmed = fetch_official_results(known_teams=all_teams)

    path = DATA_DIR / "official_results.csv"
    existing = pd.read_csv(path) if path.exists() else pd.DataFrame()
    fixtures = _rwc_fixtures(validated_only=False)
    by_pair = {frozenset((r.home_team, r.away_team)): r
               for r in fixtures.itertuples(index=False)}
    rows = {(r["date"], r["home_team"], r["away_team"]): r
            for r in existing.to_dict("records")} if not existing.empty else {}
    added = []
    for m in confirmed:
        fix = by_pair.get(frozenset((m["home"], m["away"])))
        if fix is None:
            continue
        if fix.home_team == m["home"]:
            hs, as_, ht, at = m["home_score"], m["away_score"], m["home_tries"], m["away_tries"]
        else:
            hs, as_, ht, at = m["away_score"], m["home_score"], m["away_tries"], m["home_tries"]
        date_str = pd.Timestamp(fix.date).strftime("%Y-%m-%d") if pd.notna(fix.date) \
            else m["event_date"][:10]
        key = (date_str, fix.home_team, fix.away_team)
        row = {"date": date_str, "home_team": fix.home_team,
               "away_team": fix.away_team, "home_score": hs, "away_score": as_,
               "tournament": "Rugby World Cup", "city": fix.city if hasattr(fix, "city") else "",
               "country": "Australia", "neutral": fix.neutral,
               "home_tries": ht, "away_tries": at}
        if key not in rows or (rows[key]["home_score"], rows[key]["away_score"]) != (hs, as_):
            added.append(f"{fix.home_team} {hs}-{as_} {fix.away_team}")
        rows[key] = row
    if rows:
        pd.DataFrame(list(rows.values())).to_csv(path, index=False)
    if added:
        print(f"  official full-time results: {'; '.join(added)}")
    return {(r["date"], r["home_team"], r["away_team"]):
            (int(r["home_score"]), int(r["away_score"])) for r in rows.values()}


def _rwc_fixtures(validated_only: bool = True) -> pd.DataFrame:
    """The 36 pool matches with played scores attached (and, optionally, only
    ledger-validated scores kept). Generated fixtures carry no date until a
    real result attaches one, so the ledger leaves generated rows untouched."""
    teams = load_teams()
    fixtures = generate_group_fixtures(teams)
    fixtures.insert(0, "date", pd.NaT)
    fixtures["city"] = ""
    fixtures = attach_played(fixtures, merged_results())
    if validated_only:
        fixtures = apply_ledger(fixtures, load_manual_results())
    return fixtures


def cmd_train(skip_validation: bool = False) -> None:
    results = merged_results()
    wr = load_rankings()
    table, _ = build_training_table(results, wr_points=wr)
    print(f"Training table: {len(table):,} matches "
          f"({table['date'].min().date()} – {table['date'].max().date()}); "
          f"{int((table['home_tries'] >= 0).sum()):,} rows with try counts.")
    meta = {"n_train": len(table), "validation": None}
    best = "margin_total"
    if not skip_validation:
        print("Rolling-origin validation (margin MAE / total MAE / log-loss / RPS)...")
        ev = evaluate_rolling(table)
        if not ev.empty:
            print(ev[ev["window"] == "ALL"].round(4).to_string(index=False))
            best = pick_best(ev)
            o = ev[ev["window"] == "ALL"].set_index("model")
            meta["validation"] = {
                "best": best, "n_test": int(o.loc[best, "n_test"]),
                "model_rps": float(o.loc[best, "rps"]),
                "baseline_rps": float(o.loc["baseline", "rps"]),
                "model_margin_mae": float(o.loc[best, "margin_mae"]),
                "baseline_margin_mae": float(o.loc["baseline", "margin_mae"]),
                "model_logloss": float(o.loc[best, "logloss"]),
            }
            print(f"Chosen model: {best} ({MODEL_LABELS[best]})")
    print("Fitting final model on all data ...")
    model = fit_best(table, best)
    model.save()
    meta["model_name"] = best
    meta["model_label"] = MODEL_LABELS[best]
    print(f"Saved {MODEL_PATH} ({MODEL_LABELS[best]})")
    if meta["validation"] is None and META_PATH.exists():
        meta["validation"] = json.loads(META_PATH.read_text()).get("validation")
    META_PATH.write_text(json.dumps(meta))


def cmd_simulate(n_sims: int, seed: int) -> None:
    results = merged_results()
    wr = load_rankings()
    if not MODEL_PATH.exists():
        print("No saved model found — training first.")
        cmd_train()
    model = ScoreModel.load()
    _, state = build_training_table(results, wr_points=wr)
    teams = load_teams()
    pred = MatchPredictor(model, state, teams["hosts"])
    fixtures = _rwc_fixtures(validated_only=True)
    played = int(fixtures["home_score"].notna().sum())
    print(f"{played}/{N_POOL_MATCHES} pool matches played; simulating the rest "
          f"({n_sims:,} tournaments, seed {seed}) ...")
    sim = TournamentSimulator(pred, fixtures, seed=seed)
    res = sim.run(n_sims)

    meta = {"n_sims": n_sims,
            "data_through": str(results.dropna(subset=["home_score"])["date"].max().date()),
            "n_train": 0, "validation": None, "model_label": "rugby points"}
    if META_PATH.exists():
        saved = json.loads(META_PATH.read_text())
        meta.update({k: saved[k] for k in ("n_train", "validation",
                     "model_label") if k in saved})
    write_outputs(pred, res, fixtures, meta)
    out = Path(__file__).parent / "outputs"
    print(f"Wrote {out / 'report.md'}")
    print(f"      {out / 'match_probabilities.csv'}")
    print(f"      {out / 'tournament_projections.csv'}")
    print("\nTitle favourites:")
    for _, r in res.team_table().head(5).iterrows():
        print(f"  {r['team']:<16} {100 * r['p_champion']:5.1f}%")


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(prog="rugby")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("update")
    pt = sub.add_parser("train")
    pt.add_argument("--skip-validation", action="store_true")
    for name in ("simulate", "all"):
        p = sub.add_parser(name)
        p.add_argument("--sims", type=int, default=50_000)
        p.add_argument("--seed", type=int, default=42)
        if name == "all":
            p.add_argument("--skip-validation", action="store_true")
    args = ap.parse_args(argv)

    if args.cmd == "update":
        cmd_update()
    elif args.cmd == "train":
        cmd_train(skip_validation=args.skip_validation)
    elif args.cmd == "simulate":
        cmd_simulate(args.sims, args.seed)
    elif args.cmd == "all":
        cmd_update()
        cmd_train(skip_validation=args.skip_validation)
        cmd_simulate(args.sims, args.seed)


if __name__ == "__main__":
    main()
