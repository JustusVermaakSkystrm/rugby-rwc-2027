"""Strength ratings for men's international rugby union.

Two complementary, point-in-time ratings are maintained over the full match
history in a single chronological pass (see dataset.py):

  - ``EloTracker``  — a World-Rugby-flavoured Elo: importance-weighted K,
    home advantage, and a winning-margin multiplier. A single number that
    answers "who is better"; it is the backbone strength feature and decides
    knockout coin-flips.

  - ``PointsAttackDefence`` — per-team attack/defence strengths in *points*
    space (not log-goals as in football). Rugby scorelines are 10-50, not
    0-5, so the model needs to separate a side that wins 35-30 from one that
    wins 18-15. These feed the margin/total and per-side scoring models.

The official World Rugby ranking points (data/rankings.json) are used as a
prior: teams are initialised from them (mapped into Elo space) so that
Tier-2 sides with sparse history start near their true strength instead of
at the global mean. This is the "ranking as strength prior" the brief calls
for, without leaking match outcomes into training features.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

INITIAL_RATING = 1500.0
HOME_ADVANTAGE = 40.0          # Elo points; ~ a 3-4 point on-field edge

# K factors by match importance. Rugby has far fewer fixtures than football,
# so a single test result should move ratings more than a football friendly.
K_WORLD_CUP = 60.0
K_MAJOR_TOURNAMENT = 45.0      # Six Nations, Rugby Championship, RWC qualifiers
K_OTHER_TOURNAMENT = 38.0      # Pacific Nations Cup, Rugby Africa Cup, etc.
K_TEST = 32.0                  # uncategorised internationals / tests
K_FRIENDLY = 24.0

WORLD_CUP_KEYWORDS = ("world cup", "rugby world cup", "rwc")
MAJOR_KEYWORDS = ("six nations", "rugby championship", "tri nations",
                  "the rugby championship", "world cup qual", "rwc qual")
OTHER_TOURNAMENT_KEYWORDS = (
    "nations cup", "pacific nations", "africa cup", "rugby africa",
    "asia rugby", "americas", "nations championship", "nations league",
    "autumn nations", "rugby europe", "championship",
)
FRIENDLY_KEYWORDS = ("friendly", "test match", "tour match", "non-test")


def _norm(tournament: str) -> str:
    return (tournament or "").strip().lower()


def k_factor(tournament: str) -> float:
    t = _norm(tournament)
    if any(k in t for k in WORLD_CUP_KEYWORDS):
        return K_WORLD_CUP
    if any(k in t for k in MAJOR_KEYWORDS):
        return K_MAJOR_TOURNAMENT
    if any(k in t for k in OTHER_TOURNAMENT_KEYWORDS):
        return K_OTHER_TOURNAMENT
    if any(k in t for k in FRIENDLY_KEYWORDS):
        return K_FRIENDLY
    return K_TEST


def importance_level(tournament: str) -> int:
    """Ordinal match-importance feature for the ML model (0 = friendly)."""
    t = _norm(tournament)
    if any(k in t for k in WORLD_CUP_KEYWORDS):
        return 4
    if any(k in t for k in MAJOR_KEYWORDS):
        return 3
    if any(k in t for k in OTHER_TOURNAMENT_KEYWORDS):
        return 2
    if any(k in t for k in FRIENDLY_KEYWORDS):
        return 0
    return 1


def margin_multiplier(margin: int) -> float:
    """Winning-margin multiplier. Rugby blowouts are common and not very
    informative, so growth is logarithmic and capped."""
    n = abs(margin)
    if n <= 6:
        return 1.0
    return min(1.0 + 0.35 * math.log1p((n - 6) / 7.0), 1.75)


def expected_score(rating_a: float, rating_b: float) -> float:
    return 1.0 / (1.0 + 10.0 ** ((rating_b - rating_a) / 400.0))


# --------------------------------------------------------------- WR prior

# Linear map from World Rugby ranking points (~ 30-100) into Elo space, so a
# team's published ranking can seed its Elo. World Rugby points have a SD of
# roughly 12 across test nations; one Elo "400" step ~ 10:1 odds. We map ~1
# WR point -> WR_TO_ELO Elo points and centre the field at INITIAL_RATING.
WR_REFERENCE = 80.0            # ~ a strong Tier-1 side; treated as the centre
WR_TO_ELO = 22.0


def wr_points_to_elo(points: float) -> float:
    return INITIAL_RATING + (points - WR_REFERENCE) * WR_TO_ELO


@dataclass
class EloTracker:
    """Sequential Elo over a chronologically sorted match list."""

    ratings: dict = field(default_factory=dict)
    seeded: set = field(default_factory=set)
    prior: dict = field(default_factory=dict)   # team -> seed Elo (from WR)

    def seed_prior(self, wr_points: dict[str, float]) -> None:
        """Register WR-derived seed ratings. A team's rating is initialised
        to its seed on first appearance (see ``get``)."""
        self.prior = {t: wr_points_to_elo(p) for t, p in wr_points.items()}

    def get(self, team: str) -> float:
        if team not in self.ratings:
            self.ratings[team] = self.prior.get(team, INITIAL_RATING)
            self.seeded.add(team)
        return self.ratings[team]

    def pre_match(self, home: str, away: str, neutral: bool,
                  ) -> tuple[float, float, float]:
        rh, ra = self.get(home), self.get(away)
        bonus = 0.0 if neutral else HOME_ADVANTAGE
        return rh, ra, expected_score(rh + bonus, ra)

    def update(self, home: str, away: str, home_score: int, away_score: int,
               tournament: str, neutral: bool) -> None:
        rh, ra, exp_home = self.pre_match(home, away, neutral)
        if home_score > away_score:
            actual = 1.0
        elif home_score == away_score:
            actual = 0.5
        else:
            actual = 0.0
        delta = (k_factor(tournament)
                 * margin_multiplier(home_score - away_score)
                 * (actual - exp_home))
        self.ratings[home] = rh + delta
        self.ratings[away] = ra - delta


# Attack/defence in points space. Expected points:
#   home ~ MU + HOME + att_home - def_away
#   away ~ MU + att_away - def_home
# Updated by the (capped) residual between actual and expected points.
PTS_MU = 22.0            # league-average points per team per test
PTS_HOME = 3.0           # home scoring bonus (points)
PTS_ETA = 0.06           # learning rate (scaled by importance)
PTS_CAP = 60             # clamp the shock from a single blowout


@dataclass
class PointsAttackDefence:
    att: dict = field(default_factory=dict)
    dfc: dict = field(default_factory=dict)

    def get(self, team: str) -> tuple[float, float]:
        return self.att.get(team, 0.0), self.dfc.get(team, 0.0)

    def expected(self, home: str, away: str, neutral: bool) -> tuple[float, float]:
        ah, dh = self.get(home)
        aa, da = self.get(away)
        bonus = 0.0 if neutral else PTS_HOME
        lh = max(PTS_MU + bonus + ah - da, 3.0)
        la = max(PTS_MU + aa - dh, 3.0)
        return lh, la

    def update(self, home: str, away: str, home_score: int, away_score: int,
               tournament: str, neutral: bool) -> None:
        lh, la = self.expected(home, away, neutral)
        eta = PTS_ETA * (k_factor(tournament) / K_TEST)
        rh = min(home_score, PTS_CAP) - lh
        ra = min(away_score, PTS_CAP) - la
        ah, dh = self.get(home)
        aa, da = self.get(away)
        self.att[home] = ah + eta * rh
        self.dfc[away] = da - eta * rh
        self.att[away] = aa + eta * ra
        self.dfc[home] = dh - eta * ra
