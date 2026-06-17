#!/usr/bin/env python3
"""Fetch men's international rugby test results from ESPN hidden JSON API."""
import urllib.request, json, time, os, sys
from collections import Counter

OUT = "/Users/justusvermaak/rugby-rwc-2027/rugby/data/espn_raw.json"

LEAGUES = {
    289234: "International Test Match",
    180659: "Six Nations",
    244293: "Rugby Championship",  # also covers old Tri Nations
    164205: "Rugby World Cup",
}

def fetch(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.load(r)
        except Exception as e:
            if i == tries - 1:
                return None
            time.sleep(1.5 * (i + 1))
    return None

def month_windows(start_year, end_year):
    # ESPN caps results per request; query month by month to be safe.
    for y in range(start_year, end_year + 1):
        for m in range(1, 13):
            if y == 2026 and m > 7:
                break
            nm = m + 1
            ny = y
            if nm == 13:
                nm = 1; ny = y + 1
            start = f"{y}{m:02d}01"
            end = f"{ny}{nm:02d}01"
            yield start, end

def main():
    all_events = {}  # event_id -> record
    counts = Counter()
    for lg_id, lg_name in LEAGUES.items():
        for start, end in month_windows(1995, 2026):
            url = f"https://site.api.espn.com/apis/site/v2/sports/rugby/{lg_id}/scoreboard?dates={start}-{end}"
            d = fetch(url)
            if not d:
                continue
            for e in d.get('events', []):
                eid = e.get('id')
                if not eid or eid in all_events:
                    continue
                comps = e.get('competitions', [])
                if not comps:
                    continue
                c = comps[0]
                cs = c.get('competitors', [])
                if len(cs) != 2:
                    continue
                rec = {
                    'id': eid,
                    'league_id': lg_id,
                    'league_name': lg_name,
                    'event_name': e.get('name'),
                    'date': e.get('date'),
                    'neutralSite': c.get('neutralSite'),
                    'venue': c.get('venue', {}),
                    'status': (c.get('status', {}).get('type', {}) or {}).get('completed'),
                    'season_slug': (e.get('season', {}) or {}).get('slug'),
                    'competitors': [],
                }
                tid = {x['team']['id']: x for x in cs}
                tries = Counter()
                for dd in c.get('details', []):
                    t = (dd.get('type', {}) or {}).get('text', '').lower()
                    if 'try' in t:  # 'try' and 'penalty try'
                        team = dd.get('team', {}) or {}
                        if team.get('id'):
                            tries[team['id']] += 1
                for x in cs:
                    t = x['team']
                    rec['competitors'].append({
                        'id': t.get('id'),
                        'name': t.get('displayName'),
                        'abbr': t.get('abbreviation'),
                        'homeAway': x.get('homeAway'),
                        'score': x.get('score'),
                        'tries': tries.get(t.get('id')),
                        'had_details': len(c.get('details', [])) > 0,
                    })
                all_events[eid] = rec
            counts[lg_name] += len(d.get('events', []))
        print(f"  {lg_name}: swept, total events so far {len(all_events)}", file=sys.stderr)
    with open(OUT, 'w') as f:
        json.dump(list(all_events.values()), f)
    print(f"WROTE {len(all_events)} unique events -> {OUT}")

if __name__ == '__main__':
    main()
