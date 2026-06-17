"""Monte-Carlo simulation of Rugby World Cup 2027 (Australia).

24 teams, 6 pools of 4 (round-robin). Group standings use the official rugby
bonus-point system (win 4 / draw 2 / loss 0, +1 for scoring 4+ tries, +1 for
losing by 7 or fewer) and the official pool tiebreakers. The top two of each
pool plus the four best third-placed teams advance to a Round of 16, then
quarter-finals, semi-finals, a bronze final and the final
(data/bracket.json). Every match is played in Australia, so only the host
receives home advantage.

Already-played matches enter with their real scores; the rest are sampled
from the fitted score model (model.py).
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd

from .dataset import FeatureBuilder, load_teams
from .model import ScoreModel
from .ratings import expected_score

DATA_DIR = Path(__file__).parent / "data"
RWC_TOURNAMENT = "Rugby World Cup"
KO_DRAW_ELO_TILT = 1.0     # extra time / kicking resolved ~ by Elo expectancy


def load_bracket() -> dict:
    with open(DATA_DIR / "bracket.json") as f:
        return json.load(f)


def generate_group_fixtures(teams_cfg: dict) -> pd.DataFrame:
    """The 36 pool matches (6 pools x round-robin), host oriented as home.

    Columns: home_team, away_team, neutral, country, group, plus empty
    score/try columns to be filled by played results.
    """
    hosts = set(teams_cfg.get("hosts", []))
    rows = []
    for g, members in teams_cfg["groups"].items():
        for a, b in combinations(members, 2):
            if b in hosts and a not in hosts:       # host always listed home
                a, b = b, a
            rows.append({"home_team": a, "away_team": b,
                         "neutral": a not in hosts, "country": "Australia",
                         "group": g, "home_score": np.nan, "away_score": np.nan,
                         "home_tries": np.nan, "away_tries": np.nan})
    return pd.DataFrame(rows)


def attach_played(fixtures: pd.DataFrame, results: pd.DataFrame) -> pd.DataFrame:
    """Fill scores/tries for pool matches already played (matched on the
    unordered team pair within the RWC 2027 window)."""
    fx = fixtures.copy()
    played = results[(results["tournament"].str.contains("World Cup", case=False, na=False))
                     & (results["date"] >= "2027-09-01")]
    by_pair = {}
    for r in played.itertuples(index=False):
        by_pair[frozenset((r.home_team, r.away_team))] = r
    for i, fr in fx.iterrows():
        r = by_pair.get(frozenset((fr.home_team, fr.away_team)))
        if r is None:
            continue
        if r.home_team == fr.home_team:
            fx.at[i, "home_score"], fx.at[i, "away_score"] = r.home_score, r.away_score
            fx.at[i, "home_tries"], fx.at[i, "away_tries"] = r.home_tries, r.away_tries
        else:
            fx.at[i, "home_score"], fx.at[i, "away_score"] = r.away_score, r.home_score
            fx.at[i, "home_tries"], fx.at[i, "away_tries"] = r.away_tries, r.home_tries
    return fx


class MatchPredictor:
    """Builds and caches a PairingDist per (home, away) orientation. Team
    strengths are frozen at the latest data refresh."""

    def __init__(self, model: ScoreModel, state: FeatureBuilder, hosts: list[str]):
        self.model = model
        self.state = state
        self.hosts = set(hosts)
        self.cache: dict[tuple, object] = {}

    def dist(self, home: str, away: str):
        if away in self.hosts and home not in self.hosts:
            home, away = away, home          # keep host as the home side
        key = (home, away)
        if key not in self.cache:
            neutral = home not in self.hosts
            feats = self.state.match_features(home, away, neutral=neutral,
                                              tournament=RWC_TOURNAMENT)
            self.cache[key] = (home, self.model.pairing(pd.DataFrame([feats])))
        return self.cache[key]


# --------------------------------------------------------------- standings

def pool_table(members: list[str],
               results: list[tuple]) -> dict[str, list]:
    """Per-team [match_pts, pts_diff, try_diff, pts_for, tries_for]
    with rugby bonus points. results: (home, away, hs, as, ht, at)."""
    s = {t: [0, 0, 0, 0, 0] for t in members}
    for h, a, hs, as_, ht, at in results:
        for team, sf, sa, tf, ta in ((h, hs, as_, ht, at), (a, as_, hs, at, ht)):
            if team not in s:
                continue
            won = sf > sa
            drew = sf == sa
            pts = 4 if won else (2 if drew else 0)
            if tf >= 4:
                pts += 1                              # try bonus
            if (not won) and (not drew) and (sa - sf) <= 7:
                pts += 1                              # losing bonus
            row = s[team]
            row[0] += pts
            row[1] += sf - sa
            row[2] += tf - ta
            row[3] += sf
            row[4] += tf
    return s


def _overall_key(stats: dict, elo: dict, t: str) -> tuple:
    v = stats[t]
    return (v[0], v[1], v[2], v[3], v[4], elo.get(t, 0.0))


def rank_pool(members: list[str], results: list[tuple],
              elo: dict[str, float]) -> list[str]:
    """Order a pool by the official RWC tiebreakers: match points, then for
    level teams head-to-head, then overall points difference, try difference,
    points scored, tries scored, then ranking (Elo proxy)."""
    overall = pool_table(members, results)

    def resolve(tied: list[str], allow_h2h: bool) -> list[str]:
        if len(tied) == 1:
            return tied
        if allow_h2h:
            sub = [r for r in results if r[0] in tied and r[1] in tied]
            stats = pool_table(tied, sub)
            keyf = lambda t: (stats[t][0],) + _overall_key(overall, elo, t)[1:]
        else:
            keyf = lambda t: _overall_key(overall, elo, t)
        order = sorted(tied, key=keyf, reverse=True)
        out, block = [], [order[0]]
        for t in order[1:]:
            if keyf(t) == keyf(block[-1]):
                block.append(t)
            else:
                out.extend(_settle(block, tied, allow_h2h))
                block = [t]
        out.extend(_settle(block, tied, allow_h2h))
        return out

    def _settle(block, parent, was_h2h):
        if len(block) == 1:
            return block
        if was_h2h and len(block) < len(parent):
            return resolve(block, allow_h2h=True)
        return resolve(block, allow_h2h=False)

    ordered = sorted(members, key=lambda t: overall[t][0], reverse=True)
    out, block = [], [ordered[0]]
    for t in ordered[1:]:
        if overall[t][0] == overall[block[-1]][0]:
            block.append(t)
        else:
            out.extend(resolve(block, allow_h2h=True))
            block = [t]
    out.extend(resolve(block, allow_h2h=True))
    return out


def rank_thirds(third_rows: list[tuple], elo: dict) -> list[tuple[str, str]]:
    """Best-first ranking of the six third-placed teams (no head-to-head:
    match points, points diff, try diff, points scored, tries scored, Elo)."""
    ordered = sorted(third_rows,
                     key=lambda r: (r[2][0], r[2][1], r[2][2], r[2][3],
                                    r[2][4], elo.get(r[1], 0.0)), reverse=True)
    return [(g, t) for g, t, _ in ordered]


def allocate_thirds(qualified: list[tuple[str, str]], slots: list[dict]
                    ) -> dict[str, str]:
    """Assign the four best thirds to the R16 slots whose allowed pool list
    accepts their pool. The confirmed slot constraints uniquely determine the
    assignment for every 4-of-6 combination; backtracking finds it and never
    pairs a third with its own pool winner."""
    slot_ids = [s["slot"] for s in slots]
    allowed = {s["slot"]: set(s["groups"]) for s in slots}
    assignment: dict[str, str] = {}

    def backtrack(i: int, used: frozenset) -> bool:
        if i == len(qualified):
            return True
        group, team = qualified[i]
        for sid in slot_ids:
            if sid in used or group not in allowed[sid]:
                continue
            assignment[sid] = team
            if backtrack(i + 1, used | {sid}):
                return True
            del assignment[sid]
        return False

    if not backtrack(0, frozenset()):
        raise RuntimeError(f"No valid third-place allocation for {qualified}")
    return assignment


# -------------------------------------------------------------- simulation

STAGE_REACHED = ["R16", "QF", "SF", "F", "W"]


class TournamentSimulator:
    def __init__(self, predictor: MatchPredictor, group_fixtures: pd.DataFrame,
                 seed: int = 42):
        self.pred = predictor
        self.bracket = load_bracket()
        self.teams_cfg = load_teams()
        self.groups: dict[str, list[str]] = self.teams_cfg["groups"]
        self.rng = np.random.default_rng(seed)
        self.fixtures = group_fixtures.reset_index(drop=True)
        self.played_mask = self.fixtures["home_score"].notna().to_numpy()
        self.elo = {t: predictor.state.elo.get(t)
                    for g in self.groups.values() for t in g}
        self._fix = [(r.home_team, r.away_team, r.group)
                     for r in self.fixtures.itertuples(index=False)]
        self._group_idx = {g: [i for i, f in enumerate(self._fix) if f[2] == g]
                           for g in self.groups}

    def _sample_groups(self, n_sims: int) -> np.ndarray:
        """(n_fix, n_sims, 4) -> home_pts, away_pts, home_tries, away_tries."""
        n = len(self._fix)
        out = np.empty((n, n_sims, 4), dtype=np.int64)
        for j, (h, a, _) in enumerate(self._fix):
            who_home, dist = self.pred.dist(h, a)
            hp, ap, ht, at = dist.sample(self.rng, n_sims)
            if who_home != h:                 # predictor swapped to host-home
                hp, ap, ht, at = ap, hp, at, ht
            out[j] = np.stack([hp, ap, ht, at], axis=1)
        played = self.fixtures[["home_score", "away_score",
                                "home_tries", "away_tries"]].to_numpy(float)
        for j in np.where(self.played_mask)[0]:
            row = played[j]
            tries = np.where(np.isnan(row[2:]), 0, row[2:])
            out[j, :, :] = np.concatenate([row[:2], tries]).astype(np.int64)
        return out

    def _ko_winner(self, a: str, b: str) -> tuple[str, str]:
        """Resolve a knockout match -> (winner, loser). Draws go to extra
        time / kicks, resolved near the Elo expectancy."""
        who_home, dist = self.pred.dist(a, b)
        p_home = dist.win_prob_home
        draw = dist.draw_prob
        ph_elo = expected_score(self.elo.get(who_home, 1500) + 0,
                                self.elo.get(b if who_home == a else a, 1500))
        p_home_win = p_home + draw * (0.5 + KO_DRAW_ELO_TILT * (ph_elo - 0.5))
        home_team, away_team = who_home, (b if who_home == a else a)
        if self.rng.random() < np.clip(p_home_win, 0.01, 0.99):
            return home_team, away_team
        return away_team, home_team

    def run(self, n_sims: int = 50_000) -> "SimResults":
        res = SimResults(self.groups, n_sims)
        scores = self._sample_groups(n_sims)
        ko_rounds = [self.bracket["round_of_16"], self.bracket["quarterfinals"],
                     self.bracket["semifinals"]]
        stage_of = {0: "R16", 1: "QF", 2: "SF"}

        for s in range(n_sims):
            slots, thirds = {}, []
            for g, members in self.groups.items():
                results = [(self._fix[i][0], self._fix[i][1],
                            int(scores[i, s, 0]), int(scores[i, s, 1]),
                            int(scores[i, s, 2]), int(scores[i, s, 3]))
                           for i in self._group_idx[g]]
                order = rank_pool(members, results, self.elo)
                stats = pool_table(members, results)
                res.record_group(g, order, stats)
                slots[f"W_{g}"] = order[0]
                slots[f"RU_{g}"] = order[1]
                thirds.append((g, order[2], stats[order[2]]))

            best_thirds = rank_thirds(thirds, self.elo)[:4]
            res.record_thirds(best_thirds)
            slots.update(allocate_thirds(best_thirds,
                                         self.bracket["third_place_slots"]))

            adv = {}
            for ri, matches in enumerate(ko_rounds):
                stage = stage_of[ri]
                for m in matches:
                    home = slots.get(m["home"]) or adv[m["home"]]
                    away = slots.get(m["away"]) or adv[m["away"]]
                    res.reach(home, stage); res.reach(away, stage)
                    w, l = self._ko_winner(home, away)
                    adv[f"W_{m['match']}"] = w
                    adv[f"L_{m['match']}"] = l

            fm = self.bracket["final"]
            fh, fa = adv[fm["home"]], adv[fm["away"]]
            res.reach(fh, "F"); res.reach(fa, "F")
            champ, runner = self._ko_winner(fh, fa)
            res.reach(champ, "W")
            res.record_final(champ, runner)
            bf = self.bracket["bronze_final"]
            bw, _ = self._ko_winner(adv[bf["home"]], adv[bf["away"]])
            res.record_bronze(bw)
        return res


class SimResults:
    def __init__(self, groups: dict[str, list[str]], n_sims: int):
        self.n = n_sims
        self.groups = groups
        teams = [t for g in groups.values() for t in g]
        self.rank_counts = {t: np.zeros(4) for t in teams}
        self.points_sum = {t: 0.0 for t in teams}
        self.pdiff_sum = {t: 0.0 for t in teams}
        self.third_qualified = Counter()
        self.stage = {t: Counter() for t in teams}
        self.champion = Counter()
        self.bronze = Counter()
        self.final_pair = Counter()

    def record_group(self, g, order, stats):
        for pos, t in enumerate(order):
            self.rank_counts[t][pos] += 1
        for t, v in stats.items():
            self.points_sum[t] += v[0]
            self.pdiff_sum[t] += v[1]

    def record_thirds(self, qualified):
        for _, t in qualified:
            self.third_qualified[t] += 1

    def reach(self, team, stage):
        self.stage[team][stage] += 1

    def record_final(self, champion, runner_up):
        self.champion[champion] += 1
        self.final_pair[(champion, runner_up)] += 1

    def record_bronze(self, team):
        self.bronze[team] += 1

    def team_table(self) -> pd.DataFrame:
        rows = []
        for g, members in self.groups.items():
            for t in members:
                rc = self.rank_counts[t] / self.n
                st = self.stage[t]
                rows.append({
                    "group": g, "team": t,
                    "exp_points": self.points_sum[t] / self.n,
                    "exp_pdiff": self.pdiff_sum[t] / self.n,
                    "p_win_pool": rc[0], "p_runner_up": rc[1],
                    "p_third": rc[2], "p_fourth": rc[3],
                    "p_third_advance": self.third_qualified[t] / self.n,
                    "p_R16": st["R16"] / self.n, "p_QF": st["QF"] / self.n,
                    "p_SF": st["SF"] / self.n, "p_final": st["F"] / self.n,
                    "p_champion": self.champion[t] / self.n,
                    "p_bronze": self.bronze[t] / self.n,
                })
        df = pd.DataFrame(rows)
        return df.sort_values(["p_champion", "p_final", "p_SF"],
                              ascending=False).reset_index(drop=True)
