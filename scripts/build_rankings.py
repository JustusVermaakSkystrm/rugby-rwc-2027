#!/usr/bin/env python3
"""Build rankings.json from World Rugby official rankings API."""
import urllib.request, json

URL = "https://api.wr-rims-prod.pulselive.com/rugby/v3/rankings/mru?language=en"
OUT = "/Users/justusvermaak/rugby-rwc-2027/rugby/data/rankings.json"

NORM = {
    "USA": "United States",
    "United States of America": "United States",
    "Hong Kong": "Hong Kong China",
    "Hong Kong China": "Hong Kong China",
}

def norm(n):
    return NORM.get(n, n)

req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
d = json.load(urllib.request.urlopen(req, timeout=40))
as_of = d["effective"]["label"]
points = {}
for e in d.get("entries", []):
    points[norm(e["team"]["name"])] = round(float(e["pts"]), 2)

out = {
    "as_of": as_of,
    "source": "https://api.wr-rims-prod.pulselive.com/rugby/v3/rankings/mru (World Rugby Men's Rankings, world.rugby)",
    "points": points,
}
with open(OUT, "w") as f:
    json.dump(out, f, indent=2)

RWC = ["Australia","New Zealand","Chile","Hong Kong China","South Africa","Italy","Georgia",
       "Romania","Argentina","Fiji","Canada","Spain","Ireland","Scotland","Uruguay","Portugal",
       "France","Japan","Samoa","United States","England","Wales","Tonga","Zimbabwe"]
missing = [t for t in RWC if t not in points]
print(f"as_of {as_of}; {len(points)} teams; RWC missing: {missing}")
