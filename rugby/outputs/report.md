# Rugby World Cup 2027 — ML Prediction Report

*Generated 2026-06-28 · data through **2026-04-10** · 50,000 Monte Carlo simulations · 0/36 pool matches played*

Probabilities come from a **margin + total Gaussian model** (World Rugby ranking + Elo strength, points attack/defence, rolling form, venue/importance) trained on 1,902 internationals, simulated through the official RWC 2027 bracket with bonus-point pool standings and tiebreakers.

*Rolling validation (974 matches): chosen model **margin_total** — RPS 0.1574 vs ranking-only baseline 0.1570; margin MAE 12.66 pts vs 12.57.*

## Title favourites

| # | Team | Pool | Champion | Δ vs 2026-04-10 | Final | Semi | Quarter | Rd of 16 |
|---|------|:----:|---------:|-------:|------:|----:|--------:|---------:|
| 1 | South Africa | B | **32.0%** | – | 44.1% | 61.2% | 96.5% | 100.0% |
| 2 | New Zealand | A | **21.4%** | – | 36.5% | 55.4% | 96.2% | 100.0% |
| 3 | France | E | **15.4%** | – | 23.1% | 58.7% | 68.7% | 100.0% |
| 4 | Ireland | D | **14.1%** | – | 32.2% | 55.5% | 82.0% | 100.0% |
| 5 | Argentina | C | **5.8%** | – | 19.8% | 42.4% | 89.1% | 100.0% |
| 6 | England | F | **4.0%** | – | 15.2% | 37.6% | 74.1% | 100.0% |
| 7 | Australia | A | **3.7%** | – | 15.5% | 38.0% | 83.3% | 99.4% |
| 8 | Scotland | D | **2.9%** | – | 8.9% | 25.6% | 45.6% | 99.7% |
| 9 | Italy | B | **0.3%** | – | 2.3% | 9.7% | 31.6% | 97.8% |
| 10 | Fiji | C | **0.3%** | – | 1.8% | 9.7% | 54.4% | 98.3% |
| 11 | Georgia | B | **0.0%** | – | 0.1% | 0.9% | 5.3% | 69.3% |
| 12 | Samoa | E | **0.0%** | – | 0.1% | 0.9% | 7.3% | 67.3% |

## Path to the final

The model's single most likely knockout bracket — every projected tie from the Round of 16 down to the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1196 568" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,100 C94,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M238,100 C238,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,100 C382,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M526,100 C526,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M670,100 C670,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M814,100 C814,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M958,100 C958,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,100 C1102,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M166,222 C166,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M454,222 C454,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,222 C742,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1030,222 C1030,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M310,344 C310,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M886,344 C886,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M598,466 C598,485 598,485 598,504" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="12" y="77" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 77)" text-anchor="middle">ROUND OF 16</text><text x="12" y="199" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 199)" text-anchor="middle">QUARTER-FINALS</text><text x="12" y="321" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 321)" text-anchor="middle">SEMI-FINALS</text><text x="12" y="443" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 443)" text-anchor="middle">FINAL</text><rect x="28" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="28" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="37" y="72" font-size="11" font-weight="700" fill="#7ef0b6">N. Zealand</text><text x="151" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="37" y="93" font-size="11" font-weight="400" fill="#7c89a3">Spain</text><text x="151" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="172" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="172" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="181" y="72" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="295" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="181" y="93" font-size="11" font-weight="400" fill="#7c89a3">Tonga</text><text x="295" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="316" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="316" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="325" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Fiji</text><text x="439" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">58%</text><text x="325" y="93" font-size="11" font-weight="400" fill="#7c89a3">Wales</text><text x="439" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">42%</text><rect x="460" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="460" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="469" y="72" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="583" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">70%</text><text x="469" y="93" font-size="11" font-weight="400" fill="#7c89a3">Scotland</text><text x="583" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">30%</text><rect x="604" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="604" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="613" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="727" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">96%</text><text x="613" y="93" font-size="11" font-weight="400" fill="#7c89a3">Chile</text><text x="727" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">4%</text><rect x="748" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="748" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="757" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="871" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="757" y="93" font-size="11" font-weight="400" fill="#7c89a3">Georgia</text><text x="871" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="892" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="892" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="901" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1015" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">85%</text><text x="901" y="93" font-size="11" font-weight="400" fill="#7c89a3">Japan</text><text x="1015" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">15%</text><rect x="1036" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1036" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1045" y="72" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1159" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">76%</text><text x="1045" y="93" font-size="11" font-weight="400" fill="#7c89a3">Italy</text><text x="1159" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">24%</text><rect x="100" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="109" y="194" font-size="11" font-weight="400" fill="#7c89a3">N. Zealand</text><text x="223" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">46%</text><rect x="100" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="223" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">54%</text><rect x="388" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="397" y="194" font-size="11" font-weight="400" fill="#7c89a3">Fiji</text><text x="511" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">6%</text><rect x="388" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="397" y="215" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="511" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">94%</text><rect x="676" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="685" y="194" font-size="11" font-weight="400" fill="#7c89a3">Argentina</text><text x="799" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">42%</text><rect x="676" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="685" y="215" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="799" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">58%</text><rect x="964" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="973" y="194" font-size="11" font-weight="400" fill="#7c89a3">Australia</text><text x="1087" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">47%</text><rect x="964" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="973" y="215" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1087" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">53%</text><rect x="244" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="244" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="253" y="316" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="367" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">67%</text><text x="253" y="337" font-size="11" font-weight="400" fill="#7c89a3">France</text><text x="367" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">33%</text><rect x="820" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="820" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="829" y="316" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="943" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">65%</text><text x="829" y="337" font-size="11" font-weight="400" fill="#7c89a3">England</text><text x="943" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">35%</text><rect x="532" y="420" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="532" y="422" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="541" y="438" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="655" y="438" font-size="9.5" text-anchor="end" fill="#cfe8d8">65%</text><text x="541" y="459" font-size="11" font-weight="400" fill="#7c89a3">Ireland</text><text x="655" y="459" font-size="9.5" text-anchor="end" fill="#5d6880">35%</text><rect x="498" y="504" width="200" height="46" rx="10" fill="#f5c542"/><text x="598" y="525" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 S. Africa</text><text x="598" y="541" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 32% to win</text></svg>
</div>

## Upcoming internationals — match predictions

Every scheduled men's international on the calendar, not just RWC fixtures — the same model rates any pairing. Probabilities are for the listed home side; the predicted scoreline is the model's mean.

| Date | Competition | Match | Home win | Draw | Away win | Predicted | Favourite |
|------|-------------|-------|---------:|-----:|---------:|:---------:|----------|
| 2026-08-08 | International Test Match | Japan v Australia | 26.9% | 2.0% | **71.0%** | 22.3–32.1 | Australia (71.0%) |
| 2026-08-08 | International Test Match | Argentina v South Africa | 27.8% | 2.0% | **70.2%** | 22.5–31.9 | South Africa (70.2%) |
| 2026-08-15 | International Test Match | Australia v Japan | **84.4%** | 1.4% | 14.2% | 33.5–16.0 | Australia (84.4%) |
| 2026-08-22 | International Test Match | South Africa v New Zealand | **72.0%** | 2.0% | 26.1% | 28.6–18.4 | South Africa (72.0%) |
| 2026-08-29 | International Test Match | South Africa v New Zealand | **72.0%** | 2.0% | 26.1% | 28.6–18.4 | South Africa (72.0%) |
| 2026-08-29 | International Test Match | Argentina v Australia | **66.3%** | 2.1% | 31.5% | 26.7–19.2 | Argentina (66.3%) |
| 2026-09-05 | International Test Match | Japan v Canada | **93.7%** | 0.7% | 5.6% | 44.0–17.8 | Japan (93.7%) |
| 2026-09-05 | International Test Match | South Africa v New Zealand | **72.0%** | 2.0% | 26.1% | 28.6–18.4 | South Africa (72.0%) |
| 2026-09-05 | International Test Match | Argentina v Australia | **66.3%** | 2.1% | 31.5% | 26.7–19.2 | Argentina (66.3%) |
| 2026-09-12 | International Test Match | South Africa v New Zealand | **72.0%** | 2.0% | 26.1% | 28.6–18.4 | South Africa (72.0%) |
| 2026-09-27 | International Test Match | Australia v South Africa | 18.5% | 1.6% | **79.9%** | 21.6–36.1 | South Africa (79.9%) |
| 2026-10-10 | International Test Match | New Zealand v Australia | **79.9%** | 1.6% | 18.4% | 32.0–17.5 | New Zealand (79.9%) |
| 2026-10-17 | International Test Match | Australia v New Zealand | 24.3% | 1.9% | **73.8%** | 20.6–31.7 | New Zealand (73.8%) |
| 2026-11-06 | Nations Championship | Ireland v Argentina | **74.3%** | 1.9% | 23.8% | 33.9–22.5 | Ireland (74.3%) |
| 2026-11-07 | Nations Championship | France v Fiji | **90.2%** | 1.0% | 8.8% | 38.8–16.7 | France (90.2%) |
| 2026-11-07 | Nations Championship | Wales v Japan | **54.2%** | 2.4% | 43.4% | 27.2–24.9 | Wales (54.2%) |
| 2026-11-07 | Nations Championship | Scotland v New Zealand | 42.8% | 2.4% | **54.8%** | 25.5–28.0 | New Zealand (54.8%) |
| 2026-11-07 | Nations Championship | Italy v South Africa | 6.9% | 0.8% | **92.2%** | 13.3–37.6 | South Africa (92.2%) |
| 2026-11-08 | Nations Championship | England v Australia | **66.4%** | 2.1% | 31.4% | 28.7–21.1 | England (66.4%) |
| 2026-11-13 | Nations Championship | France v South Africa | **49.0%** | 2.4% | 48.6% | 27.3–27.3 | France (49.0%) |
| 2026-11-14 | Nations Championship | Italy v Argentina | 34.2% | 2.2% | **63.6%** | 23.8–30.1 | Argentina (63.6%) |
| 2026-11-14 | Nations Championship | Wales v New Zealand | 3.6% | 0.5% | **95.9%** | 14.7–44.3 | New Zealand (95.9%) |
| 2026-11-14 | Nations Championship | England v Japan | **91.7%** | 0.9% | 7.5% | 36.4–12.8 | England (91.7%) |
| 2026-11-14 | Nations Championship | Ireland v Fiji | **93.0%** | 0.8% | 6.2% | 40.8–15.6 | Ireland (93.0%) |
| 2026-11-15 | Nations Championship | Scotland v Australia | **65.2%** | 2.2% | 32.6% | 29.6–22.6 | Scotland (65.2%) |

*31 scheduled fixture(s) on file; full list with exact probabilities in `upcoming_predictions.csv`. "(N)" = neutral venue.*

## Pool projections

### Pool A

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| New Zealand | 13.07 | 72.0% | 99.6% | 100.0% |
| Australia | 10.61 | 27.8% | 94.8% | 99.4% |
| Chile | 3.74 | 0.1% | 4.4% | 37.7% |
| Hong Kong China | 2.19 | 0.0% | 1.2% | 15.9% |

### Pool B

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| South Africa | 14.19 | 92.5% | 99.8% | 100.0% |
| Italy | 9.01 | 7.2% | 81.3% | 97.8% |
| Georgia | 5.38 | 0.3% | 17.9% | 69.3% |
| Romania | 1.26 | 0.0% | 0.9% | 6.8% |

### Pool C

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Argentina | 12.93 | 73.4% | 98.5% | 100.0% |
| Fiji | 9.79 | 25.1% | 80.8% | 98.3% |
| Spain | 5.59 | 1.5% | 19.9% | 71.7% |
| Canada | 1.31 | 0.0% | 0.8% | 7.1% |

### Pool D

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Ireland | 13.26 | 74.1% | 99.7% | 100.0% |
| Scotland | 10.70 | 25.9% | 96.6% | 99.7% |
| Portugal | 2.87 | 0.0% | 1.3% | 21.5% |
| Uruguay | 2.80 | 0.1% | 2.3% | 23.0% |

### Pool E

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| France | 14.27 | 97.0% | 99.9% | 100.0% |
| Japan | 6.24 | 2.1% | 46.5% | 72.8% |
| Samoa | 5.71 | 0.8% | 36.9% | 67.3% |
| United States | 3.71 | 0.2% | 16.7% | 36.8% |

### Pool F

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| England | 13.49 | 86.0% | 99.3% | 100.0% |
| Wales | 8.86 | 13.1% | 77.8% | 95.1% |
| Tonga | 5.18 | 0.9% | 19.5% | 64.6% |
| Zimbabwe | 2.03 | 0.0% | 3.5% | 15.2% |

*\*Advance = top two of the pool or one of the four best third-placed teams.*

## Most likely knockout bracket

Each tie shows the projected pairing and the named side's chance of advancing in that pairing.

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| R16-1 | 2027-10-23 | Sydney Football Stadium | Fiji v Wales | **Fiji** | 58.1% |
| R16-2 | 2027-10-23 | Brisbane Stadium | New Zealand v Spain | **New Zealand** | 99.0% |
| R16-3 | 2027-10-23 | Docklands Stadium, Melbourne | France v Scotland | **France** | 69.6% |
| R16-4 | 2027-10-24 | Perth Stadium | South Africa v Tonga | **South Africa** | 99.0% |
| R16-5 | 2027-10-24 | Sydney Football Stadium | Argentina v Chile | **Argentina** | 95.9% |
| R16-6 | 2027-10-24 | Docklands Stadium, Melbourne | Ireland v Georgia | **Ireland** | 99.0% |
| R16-7 | 2027-10-23 | Brisbane Stadium | Australia v Japan | **Australia** | 85.2% |
| R16-8 | 2027-10-24 | Perth Stadium | England v Italy | **England** | 75.5% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| QF1 | 2027-10-30 | Stadium Australia, Sydney | New Zealand v South Africa | **South Africa** | 53.6% |
| QF2 | 2027-10-30 | Brisbane Stadium | Fiji v France | **France** | 93.9% |
| QF3 | 2027-10-31 | Brisbane Stadium | Argentina v Ireland | **Ireland** | 58.3% |
| QF4 | 2027-10-31 | Stadium Australia, Sydney | Australia v England | **England** | 52.7% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| SF1 | 2027-11-05 | Stadium Australia, Sydney | South Africa v France | **South Africa** | 67.5% |
| SF2 | 2027-11-06 | Stadium Australia, Sydney | Ireland v England | **Ireland** | 64.7% |

### Bronze final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| BF | 2027-11-12 | Stadium Australia, Sydney | France v England | **France** | 72.4% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| F | 2027-11-13 | Stadium Australia, Sydney | South Africa v Ireland | **South Africa** | 64.6% |

**Projected champion: South Africa** (overall title probability 32.0% — the single path above is only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite still loses about one such match in three.
- Rugby is more predictable than football (few draws, favourites hold more often), but 2027 is well out, so early forecasts are low-information and will sharpen as warm-up tests are played.
- `xPts` = expected pool points (incl. bonus points). Predictions refresh hourly: `python -m rugby.run all`.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
