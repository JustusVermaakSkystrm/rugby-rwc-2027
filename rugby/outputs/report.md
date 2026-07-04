# Rugby World Cup 2027 — ML Prediction Report

*Generated 2026-07-04 · data through **2026-07-04** · 50,000 Monte Carlo simulations · 0/36 pool matches played*

Probabilities come from a **margin + total Gaussian model** (World Rugby ranking + Elo strength, points attack/defence, rolling form, venue/importance) trained on 1,905 internationals, simulated through the official RWC 2027 bracket with bonus-point pool standings and tiebreakers.

*Rolling validation (974 matches): chosen model **margin_total** — RPS 0.1574 vs ranking-only baseline 0.1570; margin MAE 12.66 pts vs 12.57.*

## Title favourites

| # | Team | Pool | Champion | Δ vs 2026-07-04 | Final | Semi | Quarter | Rd of 16 |
|---|------|:----:|---------:|-------:|------:|----:|--------:|---------:|
| 1 | South Africa | B | **32.5%** | -3.9 | 42.7% | 61.7% | 96.9% | 100.0% |
| 2 | New Zealand | A | **18.1%** | +0.4 | 31.4% | 52.1% | 96.0% | 100.0% |
| 3 | France | E | **15.6%** | +1.3 | 26.0% | 55.0% | 65.1% | 100.0% |
| 4 | Ireland | D | **14.5%** | -0.4 | 32.4% | 58.2% | 84.5% | 100.0% |
| 5 | England | F | **6.6%** | +1.8 | 19.8% | 44.1% | 80.0% | 100.0% |
| 6 | Argentina | C | **6.3%** | +0.3 | 21.4% | 45.0% | 92.9% | 100.0% |
| 7 | Australia | A | **3.2%** | -0.6 | 14.1% | 35.4% | 86.4% | 99.7% |
| 8 | Scotland | D | **2.9%** | +1.1 | 9.0% | 26.1% | 48.2% | 99.8% |
| 9 | Fiji | C | **0.2%** | – | 1.8% | 10.2% | 55.9% | 99.0% |
| 10 | Italy | B | **0.1%** | – | 1.0% | 5.8% | 22.7% | 97.9% |
| 11 | Wales | F | **0.0%** | – | 0.3% | 3.2% | 34.1% | 92.6% |
| 12 | Japan | E | **0.0%** | – | 0.1% | 1.3% | 8.6% | 79.8% |

## Biggest movers since last run (2026-07-04)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| England | +1.8 | – | 6.6% |
| France | +1.3 | – | 15.6% |
| Scotland | +1.1 | – | 2.9% |
| Ireland | -0.4 | – | 14.5% |
| Australia | -0.6 | +0.6 | 3.2% |
| South Africa | -3.9 | – | 32.5% |

## Path to the final

The model's single most likely knockout bracket — every projected tie from the Round of 16 down to the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1196 568" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,100 C94,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M238,100 C238,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,100 C382,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M526,100 C526,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M670,100 C670,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M814,100 C814,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M958,100 C958,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,100 C1102,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M166,222 C166,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M454,222 C454,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,222 C742,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1030,222 C1030,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M310,344 C310,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M886,344 C886,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M598,466 C598,485 598,485 598,504" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="12" y="77" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 77)" text-anchor="middle">ROUND OF 16</text><text x="12" y="199" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 199)" text-anchor="middle">QUARTER-FINALS</text><text x="12" y="321" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 321)" text-anchor="middle">SEMI-FINALS</text><text x="12" y="443" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 443)" text-anchor="middle">FINAL</text><rect x="28" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="28" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="37" y="72" font-size="11" font-weight="700" fill="#7ef0b6">N. Zealand</text><text x="151" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="37" y="93" font-size="11" font-weight="400" fill="#7c89a3">Spain</text><text x="151" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="172" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="172" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="181" y="72" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="295" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="181" y="93" font-size="11" font-weight="400" fill="#7c89a3">Tonga</text><text x="295" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="316" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="316" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="325" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Fiji</text><text x="439" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">53%</text><text x="325" y="93" font-size="11" font-weight="400" fill="#7c89a3">Wales</text><text x="439" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">47%</text><rect x="460" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="460" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="469" y="72" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="583" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">70%</text><text x="469" y="93" font-size="11" font-weight="400" fill="#7c89a3">Scotland</text><text x="583" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">30%</text><rect x="604" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="604" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="613" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="727" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">92%</text><text x="613" y="93" font-size="11" font-weight="400" fill="#7c89a3">Samoa</text><text x="727" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">8%</text><rect x="748" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="748" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="757" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="871" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="757" y="93" font-size="11" font-weight="400" fill="#7c89a3">Georgia</text><text x="871" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="892" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="892" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="901" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1015" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">89%</text><text x="901" y="93" font-size="11" font-weight="400" fill="#7c89a3">Japan</text><text x="1015" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">11%</text><rect x="1036" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1036" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1045" y="72" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1159" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">81%</text><text x="1045" y="93" font-size="11" font-weight="400" fill="#7c89a3">Italy</text><text x="1159" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">19%</text><rect x="100" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="109" y="194" font-size="11" font-weight="400" fill="#7c89a3">N. Zealand</text><text x="223" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">46%</text><rect x="100" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="223" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">54%</text><rect x="388" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="397" y="194" font-size="11" font-weight="400" fill="#7c89a3">Fiji</text><text x="511" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">11%</text><rect x="388" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="397" y="215" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="511" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">89%</text><rect x="676" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="685" y="194" font-size="11" font-weight="400" fill="#7c89a3">Argentina</text><text x="799" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">42%</text><rect x="676" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="685" y="215" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="799" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">58%</text><rect x="964" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="973" y="194" font-size="11" font-weight="400" fill="#7c89a3">Australia</text><text x="1087" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">42%</text><rect x="964" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="973" y="215" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1087" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">58%</text><rect x="244" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="244" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="253" y="316" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="367" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">59%</text><text x="253" y="337" font-size="11" font-weight="400" fill="#7c89a3">France</text><text x="367" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">41%</text><rect x="820" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="820" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="829" y="316" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="943" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">58%</text><text x="829" y="337" font-size="11" font-weight="400" fill="#7c89a3">England</text><text x="943" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">42%</text><rect x="532" y="420" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="532" y="422" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="541" y="438" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="655" y="438" font-size="9.5" text-anchor="end" fill="#cfe8d8">72%</text><text x="541" y="459" font-size="11" font-weight="400" fill="#7c89a3">Ireland</text><text x="655" y="459" font-size="9.5" text-anchor="end" fill="#5d6880">28%</text><rect x="498" y="504" width="200" height="46" rx="10" fill="#f5c542"/><text x="598" y="525" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 S. Africa</text><text x="598" y="541" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 32% to win</text></svg>
</div>

## Upcoming internationals — match predictions

Every scheduled men's international on the calendar, not just RWC fixtures — the same model rates any pairing. Probabilities are for the listed home side; the predicted scoreline is the model's mean.

| Date | Competition | Match | Home win | Draw | Away win | Predicted | Favourite |
|------|-------------|-------|---------:|-----:|---------:|:---------:|----------|
| 2026-07-04 | Nations Championship | Fiji v Wales | **52.6%** | 2.4% | 45.0% | 24.8–23.2 | Fiji (52.6%) |
| 2026-07-04 | Nations Championship | South Africa v England | **82.0%** | 1.5% | 16.5% | 37.2–21.4 | South Africa (82.0%) |
| 2026-07-04 | Nations Championship | Argentina v Scotland | **69.9%** | 2.1% | 28.0% | 31.8–22.6 | Argentina (69.9%) |
| 2026-07-11 | Nations Championship | New Zealand v Italy | **87.5%** | 1.2% | 11.3% | 36.0–16.2 | New Zealand (87.5%) |
| 2026-07-11 | Nations Championship | Australia v France | 13.6% | 1.4% | **85.0%** | 19.9–37.7 | France (85.0%) |
| 2026-07-11 | Nations Championship | Japan v Ireland | 5.3% | 0.7% | **94.0%** | 17.5–44.0 | Ireland (94.0%) |
| 2026-07-11 | Nations Championship | Fiji v England | 29.2% | 2.1% | **68.7%** | 25.1–33.8 | England (68.7%) |
| 2026-07-11 | Nations Championship | South Africa v Scotland | **81.3%** | 1.6% | 17.2% | 36.6–21.3 | South Africa (81.3%) |
| 2026-07-11 | Nations Championship | Argentina v Wales | **90.0%** | 1.0% | 8.9% | 35.7–13.7 | Argentina (90.0%) |
| 2026-07-18 | Nations Championship | Argentina v England | **65.6%** | 2.2% | 32.2% | 31.0–23.8 | Argentina (65.6%) |
| 2026-07-18 | Nations Championship | South Africa v Wales | **98.2%** | 0.2% | 1.6% | 46.0–10.4 | South Africa (98.2%) |
| 2026-07-18 | Nations Championship | Fiji v Scotland | 37.6% | 2.3% | **60.1%** | 25.5–30.2 | Scotland (60.1%) |
| 2026-07-18 | Nations Championship | Japan v France | 8.0% | 0.9% | **91.1%** | 18.1–41.2 | France (91.1%) |
| 2026-07-18 | Nations Championship | New Zealand v Ireland | **61.2%** | 2.3% | 36.5% | 26.7–21.5 | New Zealand (61.2%) |
| 2026-07-18 | Nations Championship | Australia v Italy | **71.7%** | 2.0% | 26.4% | 29.6–19.5 | Australia (71.7%) |
| 2026-08-08 | International Test Match | Japan v Australia | 36.3% | 2.3% | **61.4%** | 23.9–29.2 | Australia (61.4%) |
| 2026-08-08 | International Test Match | Argentina v South Africa | 30.9% | 2.1% | **67.0%** | 22.2–30.1 | South Africa (67.0%) |
| 2026-08-15 | International Test Match | Australia v Japan | **88.2%** | 1.1% | 10.7% | 37.3–17.0 | Australia (88.2%) |
| 2026-08-22 | International Test Match | South Africa v New Zealand | **69.5%** | 2.1% | 28.4% | 30.1–21.0 | South Africa (69.5%) |
| 2026-08-29 | International Test Match | Argentina v Australia | **71.8%** | 2.0% | 26.2% | 30.6–20.5 | Argentina (71.8%) |
| 2026-08-29 | International Test Match | South Africa v New Zealand | **69.5%** | 2.1% | 28.4% | 30.1–21.0 | South Africa (69.5%) |
| 2026-09-05 | International Test Match | Argentina v Australia | **71.8%** | 2.0% | 26.2% | 30.6–20.5 | Argentina (71.8%) |
| 2026-09-05 | International Test Match | South Africa v New Zealand | **69.5%** | 2.1% | 28.4% | 30.1–21.0 | South Africa (69.5%) |
| 2026-09-05 | International Test Match | Japan v Canada | **96.0%** | 0.5% | 3.5% | 45.6–15.8 | Japan (96.0%) |
| 2026-09-12 | International Test Match | South Africa v New Zealand | **69.5%** | 2.1% | 28.4% | 30.1–21.0 | South Africa (69.5%) |

*46 scheduled fixture(s) on file; full list with exact probabilities in `upcoming_predictions.csv`. "(N)" = neutral venue.*

## Pool projections

### Pool A

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| New Zealand | 13.24 | 72.8% | 99.8% | 100.0% |
| Australia | 10.82 | 27.1% | 96.7% | 99.7% |
| Chile | 3.65 | 0.1% | 3.0% | 36.4% |
| Hong Kong China | 2.13 | 0.0% | 0.6% | 13.8% |

### Pool B

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| South Africa | 14.30 | 94.5% | 99.9% | 100.0% |
| Italy | 8.90 | 5.2% | 80.2% | 97.9% |
| Georgia | 5.45 | 0.3% | 19.0% | 71.0% |
| Romania | 1.38 | 0.0% | 0.9% | 7.9% |

### Pool C

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Argentina | 13.10 | 73.8% | 98.9% | 100.0% |
| Fiji | 10.13 | 25.4% | 85.1% | 99.0% |
| Spain | 5.25 | 0.8% | 15.3% | 67.6% |
| Canada | 1.39 | 0.0% | 0.6% | 8.0% |

### Pool D

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Ireland | 13.23 | 72.2% | 99.8% | 100.0% |
| Scotland | 10.96 | 27.8% | 97.8% | 99.8% |
| Uruguay | 2.95 | 0.0% | 1.7% | 24.6% |
| Portugal | 2.70 | 0.0% | 0.7% | 19.5% |

### Pool E

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| France | 14.19 | 95.9% | 99.8% | 100.0% |
| Japan | 6.90 | 3.4% | 55.1% | 79.8% |
| Samoa | 5.45 | 0.5% | 31.1% | 64.9% |
| United States | 3.47 | 0.2% | 13.9% | 33.6% |

### Pool F

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| England | 13.82 | 90.5% | 99.7% | 100.0% |
| Wales | 8.31 | 8.8% | 70.5% | 92.6% |
| Tonga | 5.42 | 0.7% | 25.2% | 66.1% |
| Zimbabwe | 2.22 | 0.0% | 4.6% | 17.6% |

*\*Advance = top two of the pool or one of the four best third-placed teams.*

## Most likely knockout bracket

Each tie shows the projected pairing and the named side's chance of advancing in that pairing.

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| R16-1 | 2027-10-23 | Sydney Football Stadium | Fiji v Wales | **Fiji** | 53.3% |
| R16-2 | 2027-10-23 | Brisbane Stadium | New Zealand v Spain | **New Zealand** | 99.0% |
| R16-3 | 2027-10-23 | Docklands Stadium, Melbourne | France v Scotland | **France** | 69.7% |
| R16-4 | 2027-10-24 | Perth Stadium | South Africa v Tonga | **South Africa** | 99.0% |
| R16-5 | 2027-10-24 | Sydney Football Stadium | Argentina v Samoa | **Argentina** | 91.9% |
| R16-6 | 2027-10-24 | Docklands Stadium, Melbourne | Ireland v Georgia | **Ireland** | 99.0% |
| R16-7 | 2027-10-23 | Brisbane Stadium | Australia v Japan | **Australia** | 89.3% |
| R16-8 | 2027-10-24 | Perth Stadium | England v Italy | **England** | 81.3% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| QF1 | 2027-10-30 | Stadium Australia, Sydney | New Zealand v South Africa | **South Africa** | 54.1% |
| QF2 | 2027-10-30 | Brisbane Stadium | Fiji v France | **France** | 89.1% |
| QF3 | 2027-10-31 | Brisbane Stadium | Argentina v Ireland | **Ireland** | 58.2% |
| QF4 | 2027-10-31 | Stadium Australia, Sydney | Australia v England | **England** | 57.8% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| SF1 | 2027-11-05 | Stadium Australia, Sydney | South Africa v France | **South Africa** | 59.1% |
| SF2 | 2027-11-06 | Stadium Australia, Sydney | Ireland v England | **Ireland** | 58.4% |

### Bronze final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| BF | 2027-11-12 | Stadium Australia, Sydney | France v England | **France** | 61.2% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| F | 2027-11-13 | Stadium Australia, Sydney | South Africa v Ireland | **South Africa** | 71.8% |

**Projected champion: South Africa** (overall title probability 32.5% — the single path above is only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite still loses about one such match in three.
- Rugby is more predictable than football (few draws, favourites hold more often), but 2027 is well out, so early forecasts are low-information and will sharpen as warm-up tests are played.
- `xPts` = expected pool points (incl. bonus points). Predictions refresh hourly: `python -m rugby.run all`.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
