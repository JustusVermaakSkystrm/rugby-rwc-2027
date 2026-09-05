# Rugby World Cup 2027 — ML Prediction Report

*Generated 2026-09-05 · data through **2026-09-05** · 50,000 Monte Carlo simulations · 0/36 pool matches played*

Probabilities come from a **margin + total Gaussian model** (World Rugby ranking + Elo strength, points attack/defence, rolling form, venue/importance) trained on 1,927 internationals, simulated through the official RWC 2027 bracket with bonus-point pool standings and tiebreakers.

*Rolling validation (974 matches): chosen model **margin_total** — RPS 0.1574 vs ranking-only baseline 0.1570; margin MAE 12.66 pts vs 12.57.*

## Following South Africa — upcoming fixtures

Every scheduled South Africa international, with kick-off in your timezones, the model's call, and where to watch.

| Date | Kick-off | Opponent | Competition | Venue | Model call | Where to watch |
|------|----------|----------|-------------|-------|-----------|----------------|
| Sat 12 Sep 2026 | 22:00 UK · 23:00 SAST | New Zealand (N) | International Test Match | M&T Bank Stadium | **48.8%** win · 24–24 | SuperSport (SA)? |
| Sun 27 Sep 2026 | 10:45 UK · 11:45 SAST | Australia (A) | International Test Match | Optus Stadium | **70.5%** win · 34–24 | SuperSport (SA)? |
| Sat 07 Nov 2026 | 11:40 UK · 13:40 SAST | Italy (A) | Nations Championship | Allianz Stadium | **92.7%** win · 41–17 | ITV (UK) · SuperSport (SA) |
| Fri 13 Nov 2026 | 20:10 UK · 22:10 SAST | France (A) | Nations Championship | Stade de France | **64.9%** win · 31–24 | ITV (UK) · SuperSport (SA) |
| Sat 21 Nov 2026 | 16:40 UK · 18:40 SAST | Ireland (A) | Nations Championship | Aviva Stadium | **53.6%** win · 28–26 | ITV (UK) · SuperSport (SA) |

*Kick-off times are converted from the official UTC start time. Broadcast listings are curated (ESPN publishes none for internationals), as of 2026-07-02 — a "?" marks rights we could not confirm for this cycle, so check local listings.*

## Title favourites

| # | Team | Pool | Champion | Δ vs 2026-09-05 | Final | Semi | Quarter | Rd of 16 |
|---|------|:----:|---------:|-------:|------:|----:|--------:|---------:|
| 1 | South Africa | B | **35.3%** | +0.8 | 46.9% | 60.5% | 97.9% | 100.0% |
| 2 | New Zealand | A | **23.7%** | -3.1 | 35.7% | 48.5% | 97.4% | 100.0% |
| 3 | England | F | **12.4%** | +5.7 | 35.1% | 56.8% | 89.8% | 100.0% |
| 4 | France | E | **11.4%** | -2.2 | 19.5% | 62.7% | 68.1% | 100.0% |
| 5 | Ireland | D | **7.1%** | -3.3 | 23.9% | 51.6% | 73.9% | 100.0% |
| 6 | Australia | A | **4.5%** | +0.6 | 14.9% | 34.9% | 94.5% | 99.8% |
| 7 | Scotland | D | **4.1%** | +2.0 | 15.4% | 46.3% | 54.4% | 99.8% |
| 8 | Argentina | C | **1.7%** | -0.5 | 8.0% | 31.4% | 87.4% | 100.0% |
| 9 | Wales | F | **0.0%** | -0.1 | 0.3% | 3.3% | 66.5% | 98.5% |
| 10 | Italy | B | **0.0%** | – | 0.2% | 1.9% | 15.1% | 98.5% |
| 11 | Japan | E | **0.0%** | – | 0.0% | 0.4% | 5.2% | 79.6% |
| 12 | Fiji | C | **0.0%** | – | 0.0% | 0.7% | 23.9% | 96.7% |

## Biggest movers since last run (2026-09-05)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| England | +5.7 | – | 12.4% |
| Scotland | +2.0 | – | 4.1% |
| South Africa | +0.8 | – | 35.3% |
| France | -2.2 | – | 11.4% |
| New Zealand | -3.1 | – | 23.7% |
| Ireland | -3.3 | – | 7.1% |

## Path to the final

The model's single most likely knockout bracket — every projected tie from the Round of 16 down to the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1196 568" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,100 C94,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M238,100 C238,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,100 C382,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M526,100 C526,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M670,100 C670,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M814,100 C814,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M958,100 C958,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,100 C1102,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M166,222 C166,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M454,222 C454,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,222 C742,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1030,222 C1030,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M310,344 C310,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M886,344 C886,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M598,466 C598,485 598,485 598,504" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="12" y="77" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 77)" text-anchor="middle">ROUND OF 16</text><text x="12" y="199" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 199)" text-anchor="middle">QUARTER-FINALS</text><text x="12" y="321" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 321)" text-anchor="middle">SEMI-FINALS</text><text x="12" y="443" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 443)" text-anchor="middle">FINAL</text><rect x="28" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="28" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="37" y="72" font-size="11" font-weight="700" fill="#7ef0b6">N. Zealand</text><text x="151" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="37" y="93" font-size="11" font-weight="400" fill="#7c89a3">Spain</text><text x="151" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="172" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="172" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="181" y="72" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="295" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="181" y="93" font-size="11" font-weight="400" fill="#7c89a3">Tonga</text><text x="295" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="316" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="325" y="72" font-size="11" font-weight="400" fill="#7c89a3">Fiji</text><text x="439" y="72" font-size="9.5" text-anchor="end" fill="#5d6880">20%</text><rect x="316" y="78" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="325" y="93" font-size="11" font-weight="700" fill="#7ef0b6">Wales</text><text x="439" y="93" font-size="9.5" text-anchor="end" fill="#cfe8d8">80%</text><rect x="460" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="460" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="469" y="72" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="583" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">68%</text><text x="469" y="93" font-size="11" font-weight="400" fill="#7c89a3">Scotland</text><text x="583" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">32%</text><rect x="604" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="604" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="613" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="727" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">96%</text><text x="613" y="93" font-size="11" font-weight="400" fill="#7c89a3">Samoa</text><text x="727" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">4%</text><rect x="748" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="748" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="757" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="871" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="757" y="93" font-size="11" font-weight="400" fill="#7c89a3">Georgia</text><text x="871" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="892" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="892" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="901" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1015" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">96%</text><text x="901" y="93" font-size="11" font-weight="400" fill="#7c89a3">Japan</text><text x="1015" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">4%</text><rect x="1036" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1036" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1045" y="72" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1159" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">90%</text><text x="1045" y="93" font-size="11" font-weight="400" fill="#7c89a3">Italy</text><text x="1159" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">10%</text><rect x="100" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="109" y="194" font-size="11" font-weight="400" fill="#7c89a3">N. Zealand</text><text x="223" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">42%</text><rect x="100" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="223" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">58%</text><rect x="388" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="397" y="194" font-size="11" font-weight="400" fill="#7c89a3">Wales</text><text x="511" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">4%</text><rect x="388" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="397" y="215" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="511" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">96%</text><rect x="676" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="685" y="194" font-size="11" font-weight="400" fill="#7c89a3">Argentina</text><text x="799" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">43%</text><rect x="676" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="685" y="215" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="799" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">57%</text><rect x="964" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="973" y="194" font-size="11" font-weight="400" fill="#7c89a3">Australia</text><text x="1087" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">27%</text><rect x="964" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="973" y="215" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1087" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">73%</text><rect x="244" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="244" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="253" y="316" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="367" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">73%</text><text x="253" y="337" font-size="11" font-weight="400" fill="#7c89a3">France</text><text x="367" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">27%</text><rect x="820" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="820" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="829" y="316" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="943" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">54%</text><text x="829" y="337" font-size="11" font-weight="400" fill="#7c89a3">England</text><text x="943" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">46%</text><rect x="532" y="420" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="532" y="422" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="541" y="438" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="655" y="438" font-size="9.5" text-anchor="end" fill="#cfe8d8">84%</text><text x="541" y="459" font-size="11" font-weight="400" fill="#7c89a3">Ireland</text><text x="655" y="459" font-size="9.5" text-anchor="end" fill="#5d6880">16%</text><rect x="498" y="504" width="200" height="46" rx="10" fill="#f5c542"/><text x="598" y="525" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 S. Africa</text><text x="598" y="541" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 35% to win</text></svg>
</div>

## Upcoming internationals — match predictions

Every scheduled men's international on the calendar, not just RWC fixtures — the same model rates any pairing. Probabilities are for the listed home side; the predicted scoreline is the model's mean.

| Date | Competition | Match | Home win | Draw | Away win | Predicted | Favourite |
|------|-------------|-------|---------:|-----:|---------:|:---------:|----------|
| 2026-09-12 | International Test Match | South Africa v New Zealand (N) | **48.8%** | 2.4% | 48.8% | 24.4–24.4 | South Africa (48.8%) |
| 2026-09-27 | International Test Match | Australia v South Africa | 27.5% | 2.0% | **70.5%** | 24.5–33.9 | South Africa (70.5%) |
| 2026-10-10 | International Test Match | New Zealand v Australia | **80.0%** | 1.6% | 18.3% | 34.7–20.1 | New Zealand (80.0%) |
| 2026-10-17 | International Test Match | Australia v New Zealand | 22.4% | 1.8% | **75.8%** | 23.2–35.4 | New Zealand (75.8%) |
| 2026-10-24 | International Test Match | Japan v Fiji | 44.5% | 2.4% | **53.1%** | 25.7–27.5 | Fiji (53.1%) |
| 2026-10-31 | International Test Match | Belgium v Hong Kong China | 24.9% | 1.9% | **73.2%** | 18.1–28.9 | Hong Kong China (73.2%) |
| 2026-11-06 | Nations Championship | Ireland v Argentina | **69.1%** | 2.1% | 28.8% | 32.1–23.2 | Ireland (69.1%) |
| 2026-11-07 | Nations Championship | Italy v South Africa | 6.6% | 0.8% | **92.7%** | 16.8–41.5 | South Africa (92.7%) |
| 2026-11-07 | Nations Championship | Scotland v New Zealand | 23.5% | 1.9% | **74.7%** | 22.1–33.7 | New Zealand (74.7%) |
| 2026-11-07 | Nations Championship | Wales v Japan | **54.1%** | 2.4% | 43.5% | 27.1–24.9 | Wales (54.1%) |
| 2026-11-07 | Nations Championship | France v Fiji | **98.4%** | 0.2% | 1.4% | 47.1–11.0 | France (98.4%) |
| 2026-11-08 | Nations Championship | England v Australia | **63.6%** | 2.2% | 34.2% | 30.0–23.7 | England (63.6%) |
| 2026-11-13 | Nations Championship | France v South Africa | 32.9% | 2.2% | **64.9%** | 24.4–31.3 | South Africa (64.9%) |
| 2026-11-14 | Nations Championship | Italy v Argentina | 17.6% | 1.6% | **80.8%** | 18.5–33.6 | Argentina (80.8%) |
| 2026-11-14 | Nations Championship | Wales v New Zealand | 4.7% | 0.6% | **94.7%** | 18.0–45.4 | New Zealand (94.7%) |
| 2026-11-14 | Nations Championship | England v Japan | **95.6%** | 0.5% | 3.8% | 41.7–12.6 | England (95.6%) |
| 2026-11-14 | Nations Championship | Ireland v Fiji | **94.0%** | 0.7% | 5.3% | 41.9–15.4 | Ireland (94.0%) |
| 2026-11-14 | International Test Match | Paraguay v Brazil | **60.5%** | 2.3% | 37.2% | 29.3–24.3 | Paraguay (60.5%) |
| 2026-11-15 | Nations Championship | Scotland v Australia | 47.7% | 2.4% | **49.9%** | 26.6–27.1 | Australia (49.9%) |
| 2026-11-21 | Nations Championship | England v New Zealand | 40.4% | 2.3% | **57.3%** | 25.4–29.0 | New Zealand (57.3%) |
| 2026-11-21 | Nations Championship | Scotland v Japan | **88.2%** | 1.1% | 10.6% | 37.6–17.3 | Scotland (88.2%) |
| 2026-11-21 | Nations Championship | Ireland v South Africa | 44.0% | 2.4% | **53.6%** | 26.0–28.0 | South Africa (53.6%) |
| 2026-11-21 | Nations Championship | Italy v Fiji | **64.3%** | 2.2% | 33.5% | 26.7–20.1 | Italy (64.3%) |
| 2026-11-21 | Nations Championship | France v Argentina | **68.5%** | 2.1% | 29.4% | 34.4–25.8 | France (68.5%) |
| 2026-11-21 | Nations Championship | Wales v Australia | 19.6% | 1.7% | **78.8%** | 22.2–36.0 | Australia (78.8%) |

*25 scheduled fixture(s) on file; full list with exact probabilities in `upcoming_predictions.csv`. "(N)" = neutral venue.*

## Pool projections

### Pool A

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| New Zealand | 13.42 | 74.9% | 99.9% | 100.0% |
| Australia | 10.87 | 25.1% | 97.6% | 99.8% |
| Chile | 3.20 | 0.0% | 2.0% | 26.2% |
| Hong Kong China | 2.36 | 0.0% | 0.5% | 15.9% |

### Pool B

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| South Africa | 14.51 | 97.2% | 100.0% | 100.0% |
| Italy | 8.86 | 2.7% | 83.1% | 98.5% |
| Georgia | 5.38 | 0.1% | 16.4% | 71.7% |
| Romania | 0.93 | 0.0% | 0.4% | 3.9% |

### Pool C

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Argentina | 13.07 | 80.9% | 96.9% | 100.0% |
| Fiji | 8.81 | 13.1% | 69.1% | 96.7% |
| Spain | 6.68 | 6.0% | 33.1% | 83.7% |
| Canada | 1.26 | 0.0% | 0.9% | 6.5% |

### Pool D

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Ireland | 12.80 | 62.7% | 99.6% | 100.0% |
| Scotland | 11.37 | 37.2% | 97.8% | 99.8% |
| Uruguay | 3.10 | 0.0% | 1.4% | 27.3% |
| Portugal | 2.60 | 0.0% | 1.2% | 21.4% |

### Pool E

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| France | 14.34 | 97.6% | 99.9% | 100.0% |
| Japan | 6.65 | 1.5% | 51.3% | 79.6% |
| Samoa | 5.91 | 0.9% | 38.7% | 71.6% |
| United States | 2.86 | 0.0% | 10.1% | 25.7% |

### Pool F

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| England | 14.08 | 91.4% | 99.9% | 100.0% |
| Wales | 9.39 | 8.4% | 88.9% | 98.5% |
| Tonga | 5.02 | 0.2% | 10.1% | 66.9% |
| Zimbabwe | 1.20 | 0.0% | 1.1% | 6.5% |

*\*Advance = top two of the pool or one of the four best third-placed teams.*

## Most likely knockout bracket

Each tie shows the projected pairing and the named side's chance of advancing in that pairing.

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| R16-1 | 2027-10-23 | Sydney Football Stadium | Fiji v Wales | **Wales** | 79.7% |
| R16-2 | 2027-10-23 | Brisbane Stadium | New Zealand v Spain | **New Zealand** | 99.0% |
| R16-3 | 2027-10-23 | Docklands Stadium, Melbourne | France v Scotland | **France** | 68.1% |
| R16-4 | 2027-10-24 | Perth Stadium | South Africa v Tonga | **South Africa** | 99.0% |
| R16-5 | 2027-10-24 | Sydney Football Stadium | Argentina v Samoa | **Argentina** | 95.7% |
| R16-6 | 2027-10-24 | Docklands Stadium, Melbourne | Ireland v Georgia | **Ireland** | 98.9% |
| R16-7 | 2027-10-23 | Brisbane Stadium | Australia v Japan | **Australia** | 96.4% |
| R16-8 | 2027-10-24 | Perth Stadium | England v Italy | **England** | 90.3% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| QF1 | 2027-10-30 | Stadium Australia, Sydney | New Zealand v South Africa | **South Africa** | 57.7% |
| QF2 | 2027-10-30 | Brisbane Stadium | Wales v France | **France** | 96.0% |
| QF3 | 2027-10-31 | Brisbane Stadium | Argentina v Ireland | **Ireland** | 56.6% |
| QF4 | 2027-10-31 | Stadium Australia, Sydney | Australia v England | **England** | 73.1% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| SF1 | 2027-11-05 | Stadium Australia, Sydney | South Africa v France | **South Africa** | 72.9% |
| SF2 | 2027-11-06 | Stadium Australia, Sydney | Ireland v England | **Ireland** | 54.2% |

### Bronze final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| BF | 2027-11-12 | Stadium Australia, Sydney | France v England | **France** | 57.3% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| F | 2027-11-13 | Stadium Australia, Sydney | South Africa v Ireland | **South Africa** | 84.0% |

**Projected champion: South Africa** (overall title probability 35.3% — the single path above is only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite still loses about one such match in three.
- Rugby is more predictable than football (few draws, favourites hold more often), but 2027 is well out, so early forecasts are low-information and will sharpen as warm-up tests are played.
- `xPts` = expected pool points (incl. bonus points). Predictions refresh hourly: `python -m rugby.run all`.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
