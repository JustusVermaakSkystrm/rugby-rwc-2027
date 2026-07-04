# Rugby World Cup 2027 — ML Prediction Report

*Generated 2026-07-04 · data through **2026-07-04** · 50,000 Monte Carlo simulations · 0/36 pool matches played*

Probabilities come from a **margin + total Gaussian model** (World Rugby ranking + Elo strength, points attack/defence, rolling form, venue/importance) trained on 1,907 internationals, simulated through the official RWC 2027 bracket with bonus-point pool standings and tiebreakers.

*Rolling validation (974 matches): chosen model **margin_total** — RPS 0.1574 vs ranking-only baseline 0.1570; margin MAE 12.66 pts vs 12.57.*

## Title favourites

| # | Team | Pool | Champion | Δ vs 2026-07-04 | Final | Semi | Quarter | Rd of 16 |
|---|------|:----:|---------:|-------:|------:|----:|--------:|---------:|
| 1 | South Africa | B | **34.4%** | +2.0 | 44.5% | 63.1% | 97.7% | 100.0% |
| 2 | New Zealand | A | **18.0%** | -0.1 | 30.9% | 50.3% | 95.8% | 100.0% |
| 3 | France | E | **16.7%** | +1.1 | 26.0% | 61.3% | 72.0% | 100.0% |
| 4 | Ireland | D | **14.0%** | -0.5 | 31.5% | 52.5% | 84.4% | 100.0% |
| 5 | Argentina | C | **6.7%** | +0.4 | 25.3% | 49.0% | 89.0% | 100.0% |
| 6 | England | F | **4.2%** | -2.4 | 15.1% | 42.0% | 80.4% | 100.0% |
| 7 | Australia | A | **3.6%** | +0.4 | 16.1% | 36.4% | 79.7% | 98.9% |
| 8 | Scotland | D | **2.2%** | -0.8 | 7.2% | 21.7% | 39.7% | 99.4% |
| 9 | Italy | B | **0.1%** | – | 1.2% | 6.4% | 21.3% | 96.2% |
| 10 | Wales | F | **0.1%** | +0.1 | 0.9% | 6.7% | 49.0% | 95.6% |
| 11 | Fiji | C | **0.1%** | -0.2 | 0.7% | 5.5% | 44.9% | 97.9% |
| 12 | Japan | E | **0.0%** | – | 0.3% | 2.5% | 12.7% | 75.7% |

## Biggest movers since last run (2026-07-04)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| South Africa | +2.0 | – | 34.4% |
| France | +1.1 | – | 16.7% |
| Australia | +0.4 | -0.8 | 3.6% |
| Ireland | -0.5 | – | 14.0% |
| Scotland | -0.8 | -0.4 | 2.2% |
| England | -2.4 | – | 4.2% |

## Path to the final

The model's single most likely knockout bracket — every projected tie from the Round of 16 down to the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1196 568" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,100 C94,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M238,100 C238,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,100 C382,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M526,100 C526,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M670,100 C670,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M814,100 C814,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M958,100 C958,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,100 C1102,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M166,222 C166,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M454,222 C454,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,222 C742,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1030,222 C1030,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M310,344 C310,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M886,344 C886,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M598,466 C598,485 598,485 598,504" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="12" y="77" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 77)" text-anchor="middle">ROUND OF 16</text><text x="12" y="199" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 199)" text-anchor="middle">QUARTER-FINALS</text><text x="12" y="321" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 321)" text-anchor="middle">SEMI-FINALS</text><text x="12" y="443" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 443)" text-anchor="middle">FINAL</text><rect x="28" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="28" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="37" y="72" font-size="11" font-weight="700" fill="#7ef0b6">N. Zealand</text><text x="151" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="37" y="93" font-size="11" font-weight="400" fill="#7c89a3">Spain</text><text x="151" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="172" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="172" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="181" y="72" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="295" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="181" y="93" font-size="11" font-weight="400" fill="#7c89a3">Tonga</text><text x="295" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="316" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="325" y="72" font-size="11" font-weight="400" fill="#7c89a3">Fiji</text><text x="439" y="72" font-size="9.5" text-anchor="end" fill="#5d6880">43%</text><rect x="316" y="78" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="325" y="93" font-size="11" font-weight="700" fill="#7ef0b6">Wales</text><text x="439" y="93" font-size="9.5" text-anchor="end" fill="#cfe8d8">57%</text><rect x="460" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="460" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="469" y="72" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="583" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">76%</text><text x="469" y="93" font-size="11" font-weight="400" fill="#7c89a3">Scotland</text><text x="583" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">24%</text><rect x="604" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="604" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="613" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="727" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">96%</text><text x="613" y="93" font-size="11" font-weight="400" fill="#7c89a3">Chile</text><text x="727" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">4%</text><rect x="748" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="748" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="757" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="871" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="757" y="93" font-size="11" font-weight="400" fill="#7c89a3">Georgia</text><text x="871" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="892" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="892" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="901" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1015" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">80%</text><text x="901" y="93" font-size="11" font-weight="400" fill="#7c89a3">Japan</text><text x="1015" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">20%</text><rect x="1036" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1036" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1045" y="72" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1159" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">80%</text><text x="1045" y="93" font-size="11" font-weight="400" fill="#7c89a3">Italy</text><text x="1159" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">20%</text><rect x="100" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="109" y="194" font-size="11" font-weight="400" fill="#7c89a3">N. Zealand</text><text x="223" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">44%</text><rect x="100" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="223" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">56%</text><rect x="388" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="397" y="194" font-size="11" font-weight="400" fill="#7c89a3">Wales</text><text x="511" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">5%</text><rect x="388" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="397" y="215" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="511" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">95%</text><rect x="676" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="676" y="178" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="685" y="194" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="799" y="194" font-size="9.5" text-anchor="end" fill="#cfe8d8">50%</text><text x="685" y="215" font-size="11" font-weight="400" fill="#7c89a3">Ireland</text><text x="799" y="215" font-size="9.5" text-anchor="end" fill="#5d6880">50%</text><rect x="964" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="973" y="194" font-size="11" font-weight="400" fill="#7c89a3">Australia</text><text x="1087" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">47%</text><rect x="964" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="973" y="215" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1087" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">53%</text><rect x="244" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="244" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="253" y="316" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="367" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">63%</text><text x="253" y="337" font-size="11" font-weight="400" fill="#7c89a3">France</text><text x="367" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">37%</text><rect x="820" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="820" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="829" y="316" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="943" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">63%</text><text x="829" y="337" font-size="11" font-weight="400" fill="#7c89a3">England</text><text x="943" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">37%</text><rect x="532" y="420" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="532" y="422" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="541" y="438" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="655" y="438" font-size="9.5" text-anchor="end" fill="#cfe8d8">84%</text><text x="541" y="459" font-size="11" font-weight="400" fill="#7c89a3">Argentina</text><text x="655" y="459" font-size="9.5" text-anchor="end" fill="#5d6880">16%</text><rect x="498" y="504" width="200" height="46" rx="10" fill="#f5c542"/><text x="598" y="525" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 S. Africa</text><text x="598" y="541" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 34% to win</text></svg>
</div>

## Upcoming internationals — match predictions

Every scheduled men's international on the calendar, not just RWC fixtures — the same model rates any pairing. Probabilities are for the listed home side; the predicted scoreline is the model's mean.

| Date | Competition | Match | Home win | Draw | Away win | Predicted | Favourite |
|------|-------------|-------|---------:|-----:|---------:|:---------:|----------|
| 2026-07-04 | Nations Championship | Argentina v Scotland | **69.9%** | 2.1% | 28.0% | 29.8–20.7 | Argentina (69.9%) |
| 2026-07-11 | Nations Championship | New Zealand v Italy | **83.6%** | 1.5% | 15.0% | 33.3–16.7 | New Zealand (83.6%) |
| 2026-07-11 | Nations Championship | Australia v France | 11.1% | 1.2% | **87.7%** | 19.7–39.3 | France (87.7%) |
| 2026-07-11 | Nations Championship | Japan v Ireland | 7.1% | 0.9% | **92.0%** | 17.9–41.5 | Ireland (92.0%) |
| 2026-07-11 | Nations Championship | Fiji v England | 19.2% | 1.7% | **79.1%** | 23.1–36.9 | England (79.1%) |
| 2026-07-11 | Nations Championship | South Africa v Scotland | **83.7%** | 1.5% | 14.9% | 37.2–20.6 | South Africa (83.7%) |
| 2026-07-11 | Nations Championship | Argentina v Wales | **83.7%** | 1.5% | 14.8% | 33.2–16.5 | Argentina (83.7%) |
| 2026-07-18 | Nations Championship | Argentina v England | **63.7%** | 2.2% | 34.0% | 28.7–22.4 | Argentina (63.7%) |
| 2026-07-18 | Nations Championship | South Africa v Wales | **98.8%** | 0.2% | 1.0% | 46.2–8.5 | South Africa (98.8%) |
| 2026-07-18 | Nations Championship | Fiji v Scotland | 24.9% | 2.0% | **73.1%** | 23.2–33.9 | Scotland (73.1%) |
| 2026-07-18 | Nations Championship | Australia v Italy | **73.5%** | 1.9% | 24.6% | 31.5–20.7 | Australia (73.5%) |
| 2026-07-18 | Nations Championship | Japan v France | 6.2% | 0.8% | **93.0%** | 17.9–42.7 | France (93.0%) |
| 2026-07-18 | Nations Championship | New Zealand v Ireland | **59.6%** | 2.3% | 38.1% | 26.6–22.1 | New Zealand (59.6%) |
| 2026-08-08 | International Test Match | Japan v Australia | 36.6% | 2.3% | **61.1%** | 23.3–28.4 | Australia (61.1%) |
| 2026-08-08 | International Test Match | Argentina v South Africa | 25.6% | 2.0% | **72.4%** | 21.7–32.0 | South Africa (72.4%) |
| 2026-08-15 | International Test Match | Australia v Japan | **78.2%** | 1.8% | 20.0% | 32.7–19.4 | Australia (78.2%) |
| 2026-08-22 | International Test Match | South Africa v New Zealand | **71.6%** | 2.0% | 26.4% | 29.2–19.3 | South Africa (71.6%) |
| 2026-08-29 | International Test Match | South Africa v New Zealand | **71.6%** | 2.0% | 26.4% | 29.2–19.3 | South Africa (71.6%) |
| 2026-08-29 | International Test Match | Argentina v Australia | **70.4%** | 2.1% | 27.5% | 28.3–19.0 | Argentina (70.4%) |
| 2026-09-05 | International Test Match | South Africa v New Zealand | **71.6%** | 2.0% | 26.4% | 29.2–19.3 | South Africa (71.6%) |
| 2026-09-05 | International Test Match | Argentina v Australia | **70.4%** | 2.1% | 27.5% | 28.3–19.0 | Argentina (70.4%) |
| 2026-09-05 | International Test Match | Japan v Canada | **94.9%** | 0.6% | 4.5% | 43.1–15.7 | Japan (94.9%) |
| 2026-09-12 | International Test Match | South Africa v New Zealand | **71.6%** | 2.0% | 26.4% | 29.2–19.3 | South Africa (71.6%) |
| 2026-09-27 | International Test Match | Australia v South Africa | 17.3% | 1.6% | **81.1%** | 19.9–35.0 | South Africa (81.1%) |
| 2026-10-10 | International Test Match | New Zealand v Australia | **79.5%** | 1.7% | 18.8% | 33.5–19.4 | New Zealand (79.5%) |

*44 scheduled fixture(s) on file; full list with exact probabilities in `upcoming_predictions.csv`. "(N)" = neutral venue.*

## Pool projections

### Pool A

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| New Zealand | 13.17 | 75.1% | 99.6% | 100.0% |
| Australia | 10.26 | 24.6% | 92.2% | 98.9% |
| Chile | 3.73 | 0.2% | 6.0% | 38.4% |
| Hong Kong China | 2.55 | 0.1% | 2.3% | 21.0% |

### Pool B

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| South Africa | 14.58 | 98.8% | 100.0% | 100.0% |
| Italy | 8.31 | 1.0% | 75.4% | 96.2% |
| Georgia | 5.50 | 0.2% | 23.4% | 69.0% |
| Romania | 1.36 | 0.0% | 1.2% | 7.4% |

### Pool C

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Argentina | 13.19 | 79.2% | 99.0% | 100.0% |
| Fiji | 9.46 | 19.7% | 80.4% | 97.9% |
| Spain | 5.17 | 1.1% | 19.3% | 63.2% |
| Canada | 1.80 | 0.0% | 1.3% | 11.7% |

### Pool D

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Ireland | 13.22 | 76.3% | 99.6% | 100.0% |
| Scotland | 10.42 | 23.5% | 95.2% | 99.4% |
| Uruguay | 2.96 | 0.1% | 3.1% | 25.6% |
| Portugal | 2.95 | 0.1% | 2.1% | 24.6% |

### Pool E

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| France | 14.15 | 96.4% | 99.8% | 100.0% |
| Japan | 6.51 | 2.8% | 50.5% | 75.7% |
| Samoa | 5.49 | 0.6% | 34.0% | 64.3% |
| United States | 3.56 | 0.2% | 15.6% | 35.6% |

### Pool F

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| England | 13.32 | 84.0% | 99.1% | 100.0% |
| Wales | 9.09 | 15.0% | 80.9% | 95.6% |
| Tonga | 4.59 | 0.9% | 15.3% | 54.1% |
| Zimbabwe | 2.54 | 0.1% | 4.7% | 21.6% |

*\*Advance = top two of the pool or one of the four best third-placed teams.*

## Most likely knockout bracket

Each tie shows the projected pairing and the named side's chance of advancing in that pairing.

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| R16-1 | 2027-10-23 | Sydney Football Stadium | Fiji v Wales | **Wales** | 57.2% |
| R16-2 | 2027-10-23 | Brisbane Stadium | New Zealand v Spain | **New Zealand** | 99.0% |
| R16-3 | 2027-10-23 | Docklands Stadium, Melbourne | France v Scotland | **France** | 76.5% |
| R16-4 | 2027-10-24 | Perth Stadium | South Africa v Tonga | **South Africa** | 99.0% |
| R16-5 | 2027-10-24 | Sydney Football Stadium | Argentina v Chile | **Argentina** | 96.2% |
| R16-6 | 2027-10-24 | Docklands Stadium, Melbourne | Ireland v Georgia | **Ireland** | 99.0% |
| R16-7 | 2027-10-23 | Brisbane Stadium | Australia v Japan | **Australia** | 79.6% |
| R16-8 | 2027-10-24 | Perth Stadium | England v Italy | **England** | 80.3% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| QF1 | 2027-10-30 | Stadium Australia, Sydney | New Zealand v South Africa | **South Africa** | 56.2% |
| QF2 | 2027-10-30 | Brisbane Stadium | Wales v France | **France** | 94.8% |
| QF3 | 2027-10-31 | Brisbane Stadium | Argentina v Ireland | **Argentina** | 50.4% |
| QF4 | 2027-10-31 | Stadium Australia, Sydney | Australia v England | **England** | 52.9% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| SF1 | 2027-11-05 | Stadium Australia, Sydney | South Africa v France | **South Africa** | 62.9% |
| SF2 | 2027-11-06 | Stadium Australia, Sydney | Argentina v England | **Argentina** | 62.8% |

### Bronze final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| BF | 2027-11-12 | Stadium Australia, Sydney | France v England | **France** | 61.3% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| F | 2027-11-13 | Stadium Australia, Sydney | South Africa v Argentina | **South Africa** | 84.0% |

**Projected champion: South Africa** (overall title probability 34.4% — the single path above is only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite still loses about one such match in three.
- Rugby is more predictable than football (few draws, favourites hold more often), but 2027 is well out, so early forecasts are low-information and will sharpen as warm-up tests are played.
- `xPts` = expected pool points (incl. bonus points). Predictions refresh hourly: `python -m rugby.run all`.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
