# Rugby World Cup 2027 — ML Prediction Report

*Generated 2026-09-05 · data through **2026-09-05** · 50,000 Monte Carlo simulations · 0/36 pool matches played*

Probabilities come from a **margin + total Gaussian model** (World Rugby ranking + Elo strength, points attack/defence, rolling form, venue/importance) trained on 1,926 internationals, simulated through the official RWC 2027 bracket with bonus-point pool standings and tiebreakers.

*Rolling validation (974 matches): chosen model **margin_total** — RPS 0.1574 vs ranking-only baseline 0.1570; margin MAE 12.66 pts vs 12.57.*

## Following South Africa — upcoming fixtures

Every scheduled South Africa international, with kick-off in your timezones, the model's call, and where to watch.

| Date | Kick-off | Opponent | Competition | Venue | Model call | Where to watch |
|------|----------|----------|-------------|-------|-----------|----------------|
| Sat 12 Sep 2026 | 22:00 UK · 23:00 SAST | New Zealand (N) | International Test Match | M&T Bank Stadium | **48.0%** win · 26–26 | SuperSport (SA)? |
| Sun 27 Sep 2026 | 10:45 UK · 11:45 SAST | Australia (A) | International Test Match | Optus Stadium | **76.8%** win · 36–23 | SuperSport (SA)? |
| Sat 07 Nov 2026 | 11:40 UK · 13:40 SAST | Italy (A) | Nations Championship | Allianz Stadium | **97.6%** win · 45–12 | ITV (UK) · SuperSport (SA) |
| Fri 13 Nov 2026 | 20:10 UK · 22:10 SAST | France (A) | Nations Championship | Stade de France | **60.3%** win · 30–25 | ITV (UK) · SuperSport (SA) |
| Sat 21 Nov 2026 | 16:40 UK · 18:40 SAST | Ireland (A) | Nations Championship | Aviva Stadium | **53.7%** win · 28–25 | ITV (UK) · SuperSport (SA) |

*Kick-off times are converted from the official UTC start time. Broadcast listings are curated (ESPN publishes none for internationals), as of 2026-07-02 — a "?" marks rights we could not confirm for this cycle, so check local listings.*

## Title favourites

| # | Team | Pool | Champion | Δ vs 2026-09-05 | Final | Semi | Quarter | Rd of 16 |
|---|------|:----:|---------:|-------:|------:|----:|--------:|---------:|
| 1 | South Africa | B | **34.4%** | +7.5 | 44.5% | 60.0% | 97.4% | 100.0% |
| 2 | New Zealand | A | **26.8%** | -0.2 | 37.8% | 51.7% | 97.8% | 100.0% |
| 3 | France | E | **13.6%** | -0.8 | 22.6% | 63.3% | 69.9% | 100.0% |
| 4 | Ireland | D | **10.4%** | -0.9 | 30.5% | 56.4% | 80.8% | 100.0% |
| 5 | England | F | **6.7%** | -2.7 | 25.1% | 50.4% | 88.4% | 100.0% |
| 6 | Australia | A | **3.8%** | -2.5 | 16.7% | 37.3% | 89.4% | 99.7% |
| 7 | Argentina | C | **2.2%** | +0.3 | 11.8% | 35.3% | 87.0% | 100.0% |
| 8 | Scotland | D | **2.0%** | -0.7 | 9.4% | 32.2% | 44.9% | 99.8% |
| 9 | Wales | F | **0.1%** | – | 0.8% | 5.4% | 57.6% | 98.6% |
| 10 | Italy | B | **0.0%** | – | 0.5% | 3.4% | 16.7% | 97.3% |
| 11 | Fiji | C | **0.0%** | – | 0.1% | 2.3% | 39.3% | 99.0% |
| 12 | Samoa | E | **0.0%** | – | 0.0% | 0.4% | 4.5% | 70.7% |

## Biggest movers since last run (2026-09-05)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| South Africa | +7.5 | – | 34.4% |
| Scotland | -0.7 | +0.1 | 2.0% |
| France | -0.8 | – | 13.6% |
| Ireland | -0.9 | – | 10.4% |
| Australia | -2.5 | -0.1 | 3.8% |
| England | -2.7 | – | 6.7% |

## Path to the final

The model's single most likely knockout bracket — every projected tie from the Round of 16 down to the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1196 568" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,100 C94,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M238,100 C238,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,100 C382,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M526,100 C526,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M670,100 C670,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M814,100 C814,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M958,100 C958,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,100 C1102,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M166,222 C166,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M454,222 C454,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,222 C742,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1030,222 C1030,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M310,344 C310,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M886,344 C886,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M598,466 C598,485 598,485 598,504" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="12" y="77" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 77)" text-anchor="middle">ROUND OF 16</text><text x="12" y="199" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 199)" text-anchor="middle">QUARTER-FINALS</text><text x="12" y="321" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 321)" text-anchor="middle">SEMI-FINALS</text><text x="12" y="443" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 443)" text-anchor="middle">FINAL</text><rect x="28" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="28" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="37" y="72" font-size="11" font-weight="700" fill="#7ef0b6">N. Zealand</text><text x="151" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="37" y="93" font-size="11" font-weight="400" fill="#7c89a3">Spain</text><text x="151" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="172" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="172" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="181" y="72" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="295" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="181" y="93" font-size="11" font-weight="400" fill="#7c89a3">Tonga</text><text x="295" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="316" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="325" y="72" font-size="11" font-weight="400" fill="#7c89a3">Fiji</text><text x="439" y="72" font-size="9.5" text-anchor="end" fill="#5d6880">37%</text><rect x="316" y="78" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="325" y="93" font-size="11" font-weight="700" fill="#7ef0b6">Wales</text><text x="439" y="93" font-size="9.5" text-anchor="end" fill="#cfe8d8">63%</text><rect x="460" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="460" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="469" y="72" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="583" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">76%</text><text x="469" y="93" font-size="11" font-weight="400" fill="#7c89a3">Scotland</text><text x="583" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">24%</text><rect x="604" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="604" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="613" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="727" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">94%</text><text x="613" y="93" font-size="11" font-weight="400" fill="#7c89a3">Samoa</text><text x="727" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">6%</text><rect x="748" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="748" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="757" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="871" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="757" y="93" font-size="11" font-weight="400" fill="#7c89a3">Georgia</text><text x="871" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="892" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="892" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="901" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1015" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">88%</text><text x="901" y="93" font-size="11" font-weight="400" fill="#7c89a3">Japan</text><text x="1015" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">12%</text><rect x="1036" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1036" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1045" y="72" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1159" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">88%</text><text x="1045" y="93" font-size="11" font-weight="400" fill="#7c89a3">Italy</text><text x="1159" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">12%</text><rect x="100" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="109" y="194" font-size="11" font-weight="400" fill="#7c89a3">N. Zealand</text><text x="223" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">45%</text><rect x="100" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="223" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">55%</text><rect x="388" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="397" y="194" font-size="11" font-weight="400" fill="#7c89a3">Wales</text><text x="511" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">4%</text><rect x="388" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="397" y="215" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="511" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">96%</text><rect x="676" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="685" y="194" font-size="11" font-weight="400" fill="#7c89a3">Argentina</text><text x="799" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">42%</text><rect x="676" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="685" y="215" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="799" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">58%</text><rect x="964" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="973" y="194" font-size="11" font-weight="400" fill="#7c89a3">Australia</text><text x="1087" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">36%</text><rect x="964" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="973" y="215" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1087" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">64%</text><rect x="244" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="244" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="253" y="316" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="367" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">67%</text><text x="253" y="337" font-size="11" font-weight="400" fill="#7c89a3">France</text><text x="367" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">33%</text><rect x="820" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="820" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="829" y="316" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="943" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">69%</text><text x="829" y="337" font-size="11" font-weight="400" fill="#7c89a3">England</text><text x="943" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">31%</text><rect x="532" y="420" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="532" y="422" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="541" y="438" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="655" y="438" font-size="9.5" text-anchor="end" fill="#cfe8d8">81%</text><text x="541" y="459" font-size="11" font-weight="400" fill="#7c89a3">Ireland</text><text x="655" y="459" font-size="9.5" text-anchor="end" fill="#5d6880">19%</text><rect x="498" y="504" width="200" height="46" rx="10" fill="#f5c542"/><text x="598" y="525" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 S. Africa</text><text x="598" y="541" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 34% to win</text></svg>
</div>

## Upcoming internationals — match predictions

Every scheduled men's international on the calendar, not just RWC fixtures — the same model rates any pairing. Probabilities are for the listed home side; the predicted scoreline is the model's mean.

| Date | Competition | Match | Home win | Draw | Away win | Predicted | Favourite |
|------|-------------|-------|---------:|-----:|---------:|:---------:|----------|
| 2026-09-05 | International Test Match | Argentina v Australia | **51.4%** | 2.4% | 46.1% | 28.8–27.8 | Argentina (51.4%) |
| 2026-09-12 | International Test Match | South Africa v New Zealand (N) | 48.0% | 2.4% | **49.5%** | 25.6–25.9 | New Zealand (49.5%) |
| 2026-09-27 | International Test Match | Australia v South Africa | 21.4% | 1.8% | **76.8%** | 23.1–35.7 | South Africa (76.8%) |
| 2026-10-10 | International Test Match | New Zealand v Australia | **84.2%** | 1.4% | 14.4% | 35.6–18.6 | New Zealand (84.2%) |
| 2026-10-17 | International Test Match | Australia v New Zealand | 19.1% | 1.7% | **79.2%** | 21.3–35.2 | New Zealand (79.2%) |
| 2026-10-24 | International Test Match | Japan v Fiji | 40.3% | 2.4% | **57.3%** | 24.2–27.7 | Fiji (57.3%) |
| 2026-10-31 | International Test Match | Belgium v Hong Kong China | 38.4% | 2.3% | **59.3%** | 20.1–24.5 | Hong Kong China (59.3%) |
| 2026-11-06 | Nations Championship | Ireland v Argentina | **82.5%** | 1.5% | 16.0% | 37.3–21.4 | Ireland (82.5%) |
| 2026-11-07 | Nations Championship | Italy v South Africa | 2.1% | 0.3% | **97.6%** | 11.8–44.8 | South Africa (97.6%) |
| 2026-11-07 | Nations Championship | Scotland v New Zealand | 21.5% | 1.8% | **76.7%** | 21.1–33.6 | New Zealand (76.7%) |
| 2026-11-07 | Nations Championship | Wales v Japan | **64.7%** | 2.2% | 33.0% | 28.3–21.6 | Wales (64.7%) |
| 2026-11-07 | Nations Championship | France v Fiji | **98.2%** | 0.2% | 1.5% | 47.3–12.3 | France (98.2%) |
| 2026-11-08 | Nations Championship | England v Australia | **70.2%** | 2.1% | 27.7% | 33.2–23.9 | England (70.2%) |
| 2026-11-13 | Nations Championship | France v South Africa | 37.4% | 2.3% | **60.3%** | 24.8–29.6 | South Africa (60.3%) |
| 2026-11-14 | Nations Championship | Italy v Argentina | 27.0% | 2.1% | **70.9%** | 22.1–31.7 | Argentina (70.9%) |
| 2026-11-14 | Nations Championship | Wales v New Zealand | 4.7% | 0.6% | **94.7%** | 17.0–44.1 | New Zealand (94.7%) |
| 2026-11-14 | Nations Championship | England v Japan | **93.1%** | 0.8% | 6.2% | 38.9–14.0 | England (93.1%) |
| 2026-11-14 | Nations Championship | Ireland v Fiji | **96.0%** | 0.5% | 3.5% | 44.2–15.0 | Ireland (96.0%) |
| 2026-11-14 | International Test Match | Paraguay v Brazil | **62.7%** | 2.3% | 35.0% | 30.3–24.5 | Paraguay (62.7%) |
| 2026-11-15 | Nations Championship | Scotland v Australia | **51.3%** | 2.4% | 46.3% | 29.2–28.2 | Scotland (51.3%) |
| 2026-11-21 | Nations Championship | England v New Zealand | 39.5% | 2.4% | **58.1%** | 24.9–28.7 | New Zealand (58.1%) |
| 2026-11-21 | Nations Championship | Scotland v Japan | **89.1%** | 1.1% | 9.8% | 37.3–16.5 | Scotland (89.1%) |
| 2026-11-21 | Nations Championship | Ireland v South Africa | 43.9% | 2.4% | **53.7%** | 25.5–27.5 | South Africa (53.7%) |
| 2026-11-21 | Nations Championship | Italy v Fiji | **58.8%** | 2.4% | 38.9% | 26.1–21.9 | Italy (58.8%) |
| 2026-11-21 | Nations Championship | France v Argentina | **79.8%** | 1.7% | 18.6% | 35.6–21.4 | France (79.8%) |

*26 scheduled fixture(s) on file; full list with exact probabilities in `upcoming_predictions.csv`. "(N)" = neutral venue.*

## Pool projections

### Pool A

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| New Zealand | 13.59 | 80.7% | 99.9% | 100.0% |
| Australia | 10.42 | 19.3% | 95.8% | 99.7% |
| Chile | 3.45 | 0.0% | 3.5% | 31.6% |
| Hong Kong China | 2.28 | 0.0% | 0.8% | 16.0% |

### Pool B

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| South Africa | 14.46 | 96.6% | 100.0% | 100.0% |
| Italy | 8.50 | 3.3% | 74.1% | 97.3% |
| Georgia | 5.91 | 0.1% | 25.3% | 78.7% |
| Romania | 1.02 | 0.0% | 0.7% | 4.7% |

### Pool C

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Argentina | 13.16 | 78.0% | 98.2% | 100.0% |
| Fiji | 9.85 | 20.2% | 84.3% | 99.0% |
| Spain | 5.38 | 1.7% | 16.9% | 70.1% |
| Canada | 1.36 | 0.0% | 0.6% | 7.5% |

### Pool D

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Ireland | 13.05 | 69.0% | 99.6% | 100.0% |
| Scotland | 11.09 | 30.9% | 97.2% | 99.8% |
| Portugal | 3.04 | 0.1% | 1.7% | 27.6% |
| Uruguay | 2.79 | 0.1% | 1.6% | 23.9% |

### Pool E

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| France | 14.48 | 98.3% | 99.9% | 100.0% |
| Japan | 6.53 | 1.4% | 50.4% | 77.6% |
| Samoa | 5.88 | 0.3% | 38.3% | 70.7% |
| United States | 3.05 | 0.0% | 11.4% | 28.0% |

### Pool F

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| England | 13.81 | 85.8% | 99.8% | 100.0% |
| Wales | 9.72 | 14.0% | 90.2% | 98.6% |
| Tonga | 4.69 | 0.2% | 8.5% | 58.9% |
| Zimbabwe | 1.57 | 0.0% | 1.5% | 10.5% |

*\*Advance = top two of the pool or one of the four best third-placed teams.*

## Most likely knockout bracket

Each tie shows the projected pairing and the named side's chance of advancing in that pairing.

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| R16-1 | 2027-10-23 | Sydney Football Stadium | Fiji v Wales | **Wales** | 63.0% |
| R16-2 | 2027-10-23 | Brisbane Stadium | New Zealand v Spain | **New Zealand** | 99.0% |
| R16-3 | 2027-10-23 | Docklands Stadium, Melbourne | France v Scotland | **France** | 76.0% |
| R16-4 | 2027-10-24 | Perth Stadium | South Africa v Tonga | **South Africa** | 99.0% |
| R16-5 | 2027-10-24 | Sydney Football Stadium | Argentina v Samoa | **Argentina** | 93.6% |
| R16-6 | 2027-10-24 | Docklands Stadium, Melbourne | Ireland v Georgia | **Ireland** | 99.0% |
| R16-7 | 2027-10-23 | Brisbane Stadium | Australia v Japan | **Australia** | 87.7% |
| R16-8 | 2027-10-24 | Perth Stadium | England v Italy | **England** | 87.8% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| QF1 | 2027-10-30 | Stadium Australia, Sydney | New Zealand v South Africa | **South Africa** | 55.4% |
| QF2 | 2027-10-30 | Brisbane Stadium | Wales v France | **France** | 95.5% |
| QF3 | 2027-10-31 | Brisbane Stadium | Argentina v Ireland | **Ireland** | 57.8% |
| QF4 | 2027-10-31 | Stadium Australia, Sydney | Australia v England | **England** | 64.1% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| SF1 | 2027-11-05 | Stadium Australia, Sydney | South Africa v France | **South Africa** | 66.5% |
| SF2 | 2027-11-06 | Stadium Australia, Sydney | Ireland v England | **Ireland** | 68.6% |

### Bronze final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| BF | 2027-11-12 | Stadium Australia, Sydney | France v England | **France** | 58.0% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| F | 2027-11-13 | Stadium Australia, Sydney | South Africa v Ireland | **South Africa** | 81.0% |

**Projected champion: South Africa** (overall title probability 34.4% — the single path above is only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite still loses about one such match in three.
- Rugby is more predictable than football (few draws, favourites hold more often), but 2027 is well out, so early forecasts are low-information and will sharpen as warm-up tests are played.
- `xPts` = expected pool points (incl. bonus points). Predictions refresh hourly: `python -m rugby.run all`.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
