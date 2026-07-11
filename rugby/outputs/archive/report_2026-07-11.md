# Rugby World Cup 2027 — ML Prediction Report

*Generated 2026-07-11 · data through **2026-07-11** · 50,000 Monte Carlo simulations · 0/36 pool matches played*

Probabilities come from a **margin + total Gaussian model** (World Rugby ranking + Elo strength, points attack/defence, rolling form, venue/importance) trained on 1,912 internationals, simulated through the official RWC 2027 bracket with bonus-point pool standings and tiebreakers.

*Rolling validation (974 matches): chosen model **margin_total** — RPS 0.1574 vs ranking-only baseline 0.1570; margin MAE 12.66 pts vs 12.57.*

## Following South Africa — upcoming fixtures

Every scheduled South Africa international, with kick-off in your timezones, the model's call, and where to watch.

| Date | Kick-off | Opponent | Competition | Venue | Model call | Where to watch |
|------|----------|----------|-------------|-------|-----------|----------------|
| Sat 11 Jul 2026 | 16:40 UK · 17:40 SAST | Scotland (H) | Nations Championship | Loftus Versfeld | **82.0%** win · 35–20 | ITV (UK) · SuperSport (SA) |
| Sat 18 Jul 2026 | 16:40 UK · 17:40 SAST | Wales (H) | Nations Championship | Hollywoodbets Kings Park | **98.4%** win · 46–9 | ITV (UK) · SuperSport (SA) |
| Sat 08 Aug 2026 | 20:00 UK · 21:00 SAST | Argentina (A) | International Test Match | Estadio José Amalfitani | **86.8%** win · 40–21 | SuperSport (SA)? |
| Sat 22 Aug 2026 | 16:00 UK · 17:00 SAST | New Zealand (H) | International Test Match | Ellis Park | **57.0%** win · 25–21 | SuperSport (SA)? |
| Sat 29 Aug 2026 | 16:00 UK · 17:00 SAST | New Zealand (H) | International Test Match | DHL Stadium | **57.0%** win · 25–21 | SuperSport (SA)? |
| Sat 05 Sep 2026 | 16:00 UK · 17:00 SAST | New Zealand (H) | International Test Match | FNB Stadium | **57.0%** win · 25–21 | SuperSport (SA)? |
| Sat 12 Sep 2026 | 22:00 UK · 23:00 SAST | New Zealand (N) | International Test Match | M&T Bank Stadium | **56.5%** win · 25–21 | SuperSport (SA)? |
| Sun 27 Sep 2026 | 10:45 UK · 11:45 SAST | Australia (A) | International Test Match | Optus Stadium | **81.9%** win · 36–20 | SuperSport (SA)? |
| Sat 07 Nov 2026 | 11:40 UK · 13:40 SAST | Italy (A) | Nations Championship | Allianz Stadium | **95.2%** win · 43–15 | ITV (UK) · SuperSport (SA) |
| Fri 13 Nov 2026 | 20:10 UK · 22:10 SAST | France (A) | Nations Championship | Stade de France | **67.6%** win · 31–23 | ITV (UK) · SuperSport (SA) |
| Sat 21 Nov 2026 | 16:40 UK · 18:40 SAST | Ireland (A) | Nations Championship | Aviva Stadium | **61.2%** win · 29–23 | ITV (UK) · SuperSport (SA) |

*Kick-off times are converted from the official UTC start time. Broadcast listings are curated (ESPN publishes none for internationals), as of 2026-07-02 — a "?" marks rights we could not confirm for this cycle, so check local listings.*

## Title favourites

| # | Team | Pool | Champion | Δ vs 2026-07-11 | Final | Semi | Quarter | Rd of 16 |
|---|------|:----:|---------:|-------:|------:|----:|--------:|---------:|
| 1 | South Africa | B | **33.6%** | -1.9 | 44.6% | 63.8% | 97.7% | 100.0% |
| 2 | New Zealand | A | **22.6%** | -1.1 | 35.6% | 54.3% | 98.4% | 100.0% |
| 3 | France | E | **14.7%** | +2.8 | 26.2% | 60.5% | 66.0% | 100.0% |
| 4 | Ireland | D | **13.3%** | -1.6 | 32.1% | 58.5% | 83.4% | 100.0% |
| 5 | England | F | **6.7%** | +2.6 | 24.5% | 50.3% | 88.8% | 100.0% |
| 6 | Argentina | C | **4.1%** | – | 15.8% | 38.9% | 92.2% | 100.0% |
| 7 | Scotland | D | **2.5%** | -0.1 | 9.1% | 30.6% | 46.8% | 99.8% |
| 8 | Australia | A | **2.4%** | -0.6 | 10.8% | 29.8% | 88.3% | 99.7% |
| 9 | Wales | F | **0.1%** | -0.1 | 0.6% | 5.5% | 52.4% | 95.8% |
| 10 | Italy | B | **0.0%** | – | 0.4% | 2.5% | 15.1% | 96.9% |
| 11 | Samoa | E | **0.0%** | – | 0.0% | 0.6% | 4.8% | 69.4% |
| 12 | Fiji | C | **0.0%** | -0.1 | 0.1% | 3.2% | 41.4% | 98.9% |

## Biggest movers since last run (2026-07-11)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| France | +2.8 | – | 14.7% |
| England | +2.6 | – | 6.7% |
| Australia | -0.6 | -0.1 | 2.4% |
| New Zealand | -1.1 | – | 22.6% |
| Ireland | -1.6 | – | 13.3% |
| South Africa | -1.9 | – | 33.6% |

## Path to the final

The model's single most likely knockout bracket — every projected tie from the Round of 16 down to the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1196 568" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,100 C94,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M238,100 C238,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,100 C382,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M526,100 C526,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M670,100 C670,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M814,100 C814,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M958,100 C958,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,100 C1102,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M166,222 C166,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M454,222 C454,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,222 C742,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1030,222 C1030,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M310,344 C310,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M886,344 C886,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M598,466 C598,485 598,485 598,504" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="12" y="77" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 77)" text-anchor="middle">ROUND OF 16</text><text x="12" y="199" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 199)" text-anchor="middle">QUARTER-FINALS</text><text x="12" y="321" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 321)" text-anchor="middle">SEMI-FINALS</text><text x="12" y="443" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 443)" text-anchor="middle">FINAL</text><rect x="28" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="28" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="37" y="72" font-size="11" font-weight="700" fill="#7ef0b6">N. Zealand</text><text x="151" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="37" y="93" font-size="11" font-weight="400" fill="#7c89a3">Spain</text><text x="151" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="172" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="172" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="181" y="72" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="295" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="181" y="93" font-size="11" font-weight="400" fill="#7c89a3">Tonga</text><text x="295" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="316" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="325" y="72" font-size="11" font-weight="400" fill="#7c89a3">Fiji</text><text x="439" y="72" font-size="9.5" text-anchor="end" fill="#5d6880">39%</text><rect x="316" y="78" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="325" y="93" font-size="11" font-weight="700" fill="#7ef0b6">Wales</text><text x="439" y="93" font-size="9.5" text-anchor="end" fill="#cfe8d8">61%</text><rect x="460" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="460" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="469" y="72" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="583" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">73%</text><text x="469" y="93" font-size="11" font-weight="400" fill="#7c89a3">Scotland</text><text x="583" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">27%</text><rect x="604" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="604" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="613" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="727" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">98%</text><text x="613" y="93" font-size="11" font-weight="400" fill="#7c89a3">Chile</text><text x="727" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">2%</text><rect x="748" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="748" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="757" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="871" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="757" y="93" font-size="11" font-weight="400" fill="#7c89a3">Georgia</text><text x="871" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="892" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="892" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="901" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1015" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">90%</text><text x="901" y="93" font-size="11" font-weight="400" fill="#7c89a3">Japan</text><text x="1015" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">10%</text><rect x="1036" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1036" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1045" y="72" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1159" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">90%</text><text x="1045" y="93" font-size="11" font-weight="400" fill="#7c89a3">Italy</text><text x="1159" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">10%</text><rect x="100" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="109" y="194" font-size="11" font-weight="400" fill="#7c89a3">N. Zealand</text><text x="223" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">43%</text><rect x="100" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="223" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">57%</text><rect x="388" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="397" y="194" font-size="11" font-weight="400" fill="#7c89a3">Wales</text><text x="511" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">5%</text><rect x="388" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="397" y="215" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="511" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">95%</text><rect x="676" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="685" y="194" font-size="11" font-weight="400" fill="#7c89a3">Argentina</text><text x="799" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">39%</text><rect x="676" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="685" y="215" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="799" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">61%</text><rect x="964" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="973" y="194" font-size="11" font-weight="400" fill="#7c89a3">Australia</text><text x="1087" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">31%</text><rect x="964" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="973" y="215" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1087" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">69%</text><rect x="244" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="244" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="253" y="316" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="367" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">61%</text><text x="253" y="337" font-size="11" font-weight="400" fill="#7c89a3">France</text><text x="367" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">39%</text><rect x="820" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="820" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="829" y="316" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="943" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">70%</text><text x="829" y="337" font-size="11" font-weight="400" fill="#7c89a3">England</text><text x="943" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">30%</text><rect x="532" y="420" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="532" y="422" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="541" y="438" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="655" y="438" font-size="9.5" text-anchor="end" fill="#cfe8d8">74%</text><text x="541" y="459" font-size="11" font-weight="400" fill="#7c89a3">Ireland</text><text x="655" y="459" font-size="9.5" text-anchor="end" fill="#5d6880">26%</text><rect x="498" y="504" width="200" height="46" rx="10" fill="#f5c542"/><text x="598" y="525" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 S. Africa</text><text x="598" y="541" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 34% to win</text></svg>
</div>

## Upcoming internationals — match predictions

Every scheduled men's international on the calendar, not just RWC fixtures — the same model rates any pairing. Probabilities are for the listed home side; the predicted scoreline is the model's mean.

| Date | Competition | Match | Home win | Draw | Away win | Predicted | Favourite |
|------|-------------|-------|---------:|-----:|---------:|:---------:|----------|
| 2026-07-11 | Nations Championship | South Africa v Scotland | **82.0%** | 1.5% | 16.5% | 35.5–19.7 | South Africa (82.0%) |
| 2026-07-11 | Nations Championship | Argentina v Wales | **85.3%** | 1.3% | 13.4% | 36.5–18.5 | Argentina (85.3%) |
| 2026-07-18 | Nations Championship | New Zealand v Ireland | **60.7%** | 2.3% | 37.0% | 27.8–22.7 | New Zealand (60.7%) |
| 2026-07-18 | Nations Championship | Japan v France | 5.7% | 0.7% | **93.6%** | 17.9–43.7 | France (93.6%) |
| 2026-07-18 | Nations Championship | Australia v Italy | **80.3%** | 1.6% | 18.1% | 33.1–18.3 | Australia (80.3%) |
| 2026-07-18 | Nations Championship | Fiji v Scotland | 20.5% | 1.8% | **77.7%** | 22.8–36.1 | Scotland (77.7%) |
| 2026-07-18 | Nations Championship | South Africa v Wales | **98.4%** | 0.2% | 1.4% | 45.5–9.2 | South Africa (98.4%) |
| 2026-07-18 | Nations Championship | Argentina v England | 36.6% | 2.3% | **61.1%** | 27.2–32.5 | England (61.1%) |
| 2026-08-08 | International Test Match | Argentina v South Africa | 12.0% | 1.2% | **86.8%** | 20.8–39.9 | South Africa (86.8%) |
| 2026-08-08 | International Test Match | Japan v Australia | 34.0% | 2.2% | **63.8%** | 22.6–29.0 | Australia (63.8%) |
| 2026-08-15 | International Test Match | Australia v Japan | **88.5%** | 1.1% | 10.3% | 37.0–16.4 | Australia (88.5%) |
| 2026-08-22 | International Test Match | South Africa v New Zealand | **57.0%** | 2.3% | 40.7% | 24.7–21.3 | South Africa (57.0%) |
| 2026-08-29 | International Test Match | South Africa v New Zealand | **57.0%** | 2.3% | 40.7% | 24.7–21.3 | South Africa (57.0%) |
| 2026-08-29 | International Test Match | Argentina v Australia | **66.0%** | 2.2% | 31.8% | 30.8–23.4 | Argentina (66.0%) |
| 2026-09-05 | International Test Match | Japan v Canada | **95.3%** | 0.6% | 4.2% | 43.7–15.3 | Japan (95.3%) |
| 2026-09-05 | International Test Match | South Africa v New Zealand | **57.0%** | 2.3% | 40.7% | 24.7–21.3 | South Africa (57.0%) |
| 2026-09-05 | International Test Match | Argentina v Australia | **66.0%** | 2.2% | 31.8% | 30.8–23.4 | Argentina (66.0%) |
| 2026-09-12 | International Test Match | South Africa v New Zealand (N) | **56.5%** | 2.4% | 41.1% | 24.7–21.4 | South Africa (56.5%) |
| 2026-09-27 | International Test Match | Australia v South Africa | 16.6% | 1.5% | **81.9%** | 20.2–36.0 | South Africa (81.9%) |
| 2026-10-10 | International Test Match | New Zealand v Australia | **83.1%** | 1.5% | 15.4% | 34.2–17.7 | New Zealand (83.1%) |
| 2026-10-17 | International Test Match | Australia v New Zealand | 26.2% | 2.0% | **71.9%** | 22.3–32.5 | New Zealand (71.9%) |
| 2026-11-06 | Nations Championship | Ireland v Argentina | **70.6%** | 2.0% | 27.4% | 32.3–22.8 | Ireland (70.6%) |
| 2026-11-07 | Nations Championship | Italy v South Africa | 4.3% | 0.6% | **95.2%** | 14.6–42.8 | South Africa (95.2%) |
| 2026-11-07 | Nations Championship | Scotland v New Zealand | 36.0% | 2.3% | **61.7%** | 23.0–28.5 | New Zealand (61.7%) |
| 2026-11-07 | Nations Championship | Wales v Japan | **62.3%** | 2.2% | 35.4% | 28.8–23.1 | Wales (62.3%) |

*39 scheduled fixture(s) on file; full list with exact probabilities in `upcoming_predictions.csv`. "(N)" = neutral venue.*

## Pool projections

### Pool A

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| New Zealand | 13.12 | 71.3% | 99.7% | 100.0% |
| Australia | 10.83 | 28.5% | 96.1% | 99.7% |
| Chile | 3.64 | 0.1% | 3.4% | 37.9% |
| Hong Kong China | 2.30 | 0.0% | 0.8% | 17.4% |

### Pool B

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| South Africa | 14.43 | 96.8% | 99.9% | 100.0% |
| Italy | 8.64 | 3.0% | 78.4% | 96.9% |
| Georgia | 5.43 | 0.2% | 20.3% | 70.3% |
| Romania | 1.44 | 0.0% | 1.3% | 8.8% |

### Pool C

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Argentina | 13.71 | 85.5% | 99.5% | 100.0% |
| Fiji | 9.56 | 13.8% | 83.3% | 98.9% |
| Spain | 5.21 | 0.6% | 16.6% | 66.7% |
| Canada | 1.42 | 0.0% | 0.6% | 8.1% |

### Pool D

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Ireland | 13.12 | 70.5% | 99.6% | 100.0% |
| Scotland | 11.04 | 29.4% | 97.8% | 99.8% |
| Portugal | 3.15 | 0.0% | 1.3% | 27.6% |
| Uruguay | 2.58 | 0.1% | 1.3% | 20.9% |

### Pool E

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| France | 14.37 | 97.8% | 99.9% | 100.0% |
| Japan | 6.52 | 1.6% | 51.0% | 76.6% |
| Samoa | 5.77 | 0.5% | 36.1% | 69.4% |
| United States | 3.28 | 0.1% | 13.0% | 31.6% |

### Pool F

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| England | 13.94 | 90.3% | 99.8% | 100.0% |
| Wales | 8.98 | 9.4% | 83.1% | 95.8% |
| Tonga | 4.47 | 0.3% | 12.2% | 53.6% |
| Zimbabwe | 2.42 | 0.0% | 4.9% | 20.2% |

*\*Advance = top two of the pool or one of the four best third-placed teams.*

## Most likely knockout bracket

Each tie shows the projected pairing and the named side's chance of advancing in that pairing.

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| R16-1 | 2027-10-23 | Sydney Football Stadium | Fiji v Wales | **Wales** | 61.2% |
| R16-2 | 2027-10-23 | Brisbane Stadium | New Zealand v Spain | **New Zealand** | 99.0% |
| R16-3 | 2027-10-23 | Docklands Stadium, Melbourne | France v Scotland | **France** | 73.1% |
| R16-4 | 2027-10-24 | Perth Stadium | South Africa v Tonga | **South Africa** | 99.0% |
| R16-5 | 2027-10-24 | Sydney Football Stadium | Argentina v Chile | **Argentina** | 98.4% |
| R16-6 | 2027-10-24 | Docklands Stadium, Melbourne | Ireland v Georgia | **Ireland** | 99.0% |
| R16-7 | 2027-10-23 | Brisbane Stadium | Australia v Japan | **Australia** | 90.3% |
| R16-8 | 2027-10-24 | Perth Stadium | England v Italy | **England** | 89.8% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| QF1 | 2027-10-30 | Stadium Australia, Sydney | New Zealand v South Africa | **South Africa** | 57.1% |
| QF2 | 2027-10-30 | Brisbane Stadium | Wales v France | **France** | 95.5% |
| QF3 | 2027-10-31 | Brisbane Stadium | Argentina v Ireland | **Ireland** | 61.3% |
| QF4 | 2027-10-31 | Stadium Australia, Sydney | Australia v England | **England** | 68.8% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| SF1 | 2027-11-05 | Stadium Australia, Sydney | South Africa v France | **South Africa** | 60.9% |
| SF2 | 2027-11-06 | Stadium Australia, Sydney | Ireland v England | **Ireland** | 70.0% |

### Bronze final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| BF | 2027-11-12 | Stadium Australia, Sydney | France v England | **France** | 59.8% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| F | 2027-11-13 | Stadium Australia, Sydney | South Africa v Ireland | **South Africa** | 74.2% |

**Projected champion: South Africa** (overall title probability 33.6% — the single path above is only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite still loses about one such match in three.
- Rugby is more predictable than football (few draws, favourites hold more often), but 2027 is well out, so early forecasts are low-information and will sharpen as warm-up tests are played.
- `xPts` = expected pool points (incl. bonus points). Predictions refresh hourly: `python -m rugby.run all`.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
