#!/usr/bin/env python3
"""Merge ESPN international results with Tier-1 historical CSV into martj42-compatible results.csv."""
import json, pandas as pd, numpy as np

DATA = "/Users/justusvermaak/rugby-rwc-2027/rugby/data/"

# ---- team name normalization to the canonical RWC-2027 names + common aliases ----
NORM = {
    "United States of America": "United States",
    "USA": "United States",
    "Hong Kong": "Hong Kong China",
    "Hong Kong, China": "Hong Kong China",
    "Korea Republic": "South Korea",
    "Czechia": "Czech Republic",
    "Cote d'Ivoire": "Ivory Coast",
    "Chinese Taipei": "Chinese Taipei",
    "Western Samoa": "Samoa",
}
# entities that are NOT national teams -> drop the match
NOT_NATIONAL = {"Cambridge"}

def norm(name):
    if name is None:
        return None
    name = str(name).strip()
    return NORM.get(name, name)

# ---- load ESPN ----
ev = json.load(open(DATA + "espn_raw.json"))
rows = []
for e in ev:
    if not e.get("status"):  # only completed matches
        continue
    cs = e["competitors"]
    if len(cs) != 2:
        continue
    home = next((c for c in cs if c["homeAway"] == "home"), None)
    away = next((c for c in cs if c["homeAway"] == "away"), None)
    if home is None or away is None:
        # fall back to order
        home, away = cs[0], cs[1]
    ht, at = norm(home["name"]), norm(away["name"])
    if ht in NOT_NATIONAL or at in NOT_NATIONAL:
        continue
    try:
        hs = int(home["score"]); as_ = int(away["score"])
    except (TypeError, ValueError):
        continue
    venue = e.get("venue") or {}
    addr = venue.get("address") or {}
    city = addr.get("city")
    country = addr.get("state")  # ESPN puts country in 'state' for internationals
    rows.append({
        "date": e["date"][:10],
        "home_team": ht,
        "away_team": at,
        "home_score": hs,
        "away_score": as_,
        "tournament": e.get("league_name") or "International Test Match",
        "city": city,
        "country": country,
        "neutral": bool(e.get("neutralSite")),
        "home_tries": home.get("tries"),
        "away_tries": away.get("tries"),
        "_src": "espn",
    })
espn = pd.DataFrame(rows)
print("ESPN rows (completed, national):", len(espn))

# ---- load Tier-1 historical CSV (the existing file) ----
t1 = pd.read_csv(DATA + "results.csv")
t1 = t1.rename(columns={"competition": "tournament"})
t1["home_team"] = t1["home_team"].map(norm)
t1["away_team"] = t1["away_team"].map(norm)
t1["neutral"] = t1["neutral"].astype(bool)
t1["home_tries"] = np.nan
t1["away_tries"] = np.nan
t1["_src"] = "tier1"
t1 = t1[["date", "home_team", "away_team", "home_score", "away_score",
         "tournament", "city", "country", "neutral", "home_tries", "away_tries", "_src"]]
print("Tier-1 rows:", len(t1))

# ---- merge: ESPN primary, Tier-1 fills gaps (esp. pre-1995) ----
both = pd.concat([espn, t1], ignore_index=True)
both["date"] = pd.to_datetime(both["date"], errors="coerce").dt.strftime("%Y-%m-%d")
both = both.dropna(subset=["date", "home_team", "away_team"])

# dedup key: same date + unordered team pair. Prefer ESPN (has tries) over tier1.
def pairkey(r):
    return (r["date"], frozenset((r["home_team"], r["away_team"])))
both["_key"] = both.apply(pairkey, axis=1)
both["_pri"] = both["_src"].map({"espn": 0, "tier1": 1})
both = both.sort_values(["_key", "_pri"]).drop_duplicates("_key", keep="first")

# ---- finalize ----
out = both.sort_values("date").reset_index(drop=True)
out = out[["date", "home_team", "away_team", "home_score", "away_score",
           "tournament", "city", "country", "neutral", "home_tries", "away_tries"]]

# integer scores; tries integer-or-empty
out["home_score"] = out["home_score"].astype(int)
out["away_score"] = out["away_score"].astype(int)
def tri(x):
    if pd.isna(x):
        return ""
    return str(int(x))
out["home_tries"] = out["home_tries"].map(tri)
out["away_tries"] = out["away_tries"].map(tri)
# neutral as Python bool literal
out["neutral"] = out["neutral"].map(lambda b: "True" if bool(b) else "False")
# clean city/country NaN -> empty
out["city"] = out["city"].fillna("")
out["country"] = out["country"].fillna("")
out["tournament"] = out["tournament"].fillna("International Test Match")

out.to_csv(DATA + "results.csv", index=False)
print("WROTE results.csv rows:", len(out))
