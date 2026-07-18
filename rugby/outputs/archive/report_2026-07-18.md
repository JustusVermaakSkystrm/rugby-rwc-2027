# Rugby World Cup 2027 — ML Prediction Report

*Generated 2026-07-18 · data through **2026-07-18** · 50,000 Monte Carlo simulations · 0/36 pool matches played*

Probabilities come from a **margin + total Gaussian model** (World Rugby ranking + Elo strength, points attack/defence, rolling form, venue/importance) trained on 1,919 internationals, simulated through the official RWC 2027 bracket with bonus-point pool standings and tiebreakers.

*Rolling validation (974 matches): chosen model **margin_total** — RPS 0.1574 vs ranking-only baseline 0.1570; margin MAE 12.66 pts vs 12.57.*

## Following South Africa — upcoming fixtures

Every scheduled South Africa international, with kick-off in your timezones, the model's call, and where to watch.

| Date | Kick-off | Opponent | Competition | Venue | Model call | Where to watch |
|------|----------|----------|-------------|-------|-----------|----------------|
| Sat 08 Aug 2026 | 20:00 UK · 21:00 SAST | Argentina (A) | International Test Match | Estadio José Amalfitani | **82.3%** win · 37–22 | SuperSport (SA)? |
| Sat 22 Aug 2026 | 16:00 UK · 17:00 SAST | New Zealand (H) | International Test Match | Ellis Park | **60.7%** win · 24–19 | SuperSport (SA)? |
| Sat 29 Aug 2026 | 16:00 UK · 17:00 SAST | New Zealand (H) | International Test Match | DHL Stadium | **60.7%** win · 24–19 | SuperSport (SA)? |
| Sat 05 Sep 2026 | 16:00 UK · 17:00 SAST | New Zealand (H) | International Test Match | FNB Stadium | **60.7%** win · 24–19 | SuperSport (SA)? |
| Sat 12 Sep 2026 | 22:00 UK · 23:00 SAST | New Zealand (N) | International Test Match | M&T Bank Stadium | **58.0%** win · 24–20 | SuperSport (SA)? |
| Sun 27 Sep 2026 | 10:45 UK · 11:45 SAST | Australia (A) | International Test Match | Optus Stadium | **71.6%** win · 33–23 | SuperSport (SA)? |
| Sat 07 Nov 2026 | 11:40 UK · 13:40 SAST | Italy (A) | Nations Championship | Allianz Stadium | **98.2%** win · 48–13 | ITV (UK) · SuperSport (SA) |
| Fri 13 Nov 2026 | 20:10 UK · 22:10 SAST | France (A) | Nations Championship | Stade de France | **61.8%** win · 30–24 | ITV (UK) · SuperSport (SA) |
| Sat 21 Nov 2026 | 16:40 UK · 18:40 SAST | Ireland (A) | Nations Championship | Aviva Stadium | **57.9%** win · 28–24 | ITV (UK) · SuperSport (SA) |

*Kick-off times are converted from the official UTC start time. Broadcast listings are curated (ESPN publishes none for internationals), as of 2026-07-02 — a "?" marks rights we could not confirm for this cycle, so check local listings.*

## Title favourites

| # | Team | Pool | Champion | Δ vs 2026-07-18 | Final | Semi | Quarter | Rd of 16 |
|---|------|:----:|---------:|-------:|------:|----:|--------:|---------:|
| 1 | South Africa | B | **33.1%** | +2.9 | 43.8% | 60.3% | 98.2% | 100.0% |
| 2 | New Zealand | A | **25.9%** | -3.4 | 39.9% | 56.3% | 98.3% | 100.0% |
| 3 | Ireland | D | **13.3%** | -0.1 | 33.5% | 63.2% | 77.6% | 100.0% |
| 4 | France | E | **12.7%** | +2.4 | 21.9% | 58.1% | 66.7% | 100.0% |
| 5 | England | F | **5.7%** | -0.3 | 23.1% | 48.0% | 89.8% | 100.0% |
| 6 | Argentina | C | **3.7%** | -0.3 | 15.2% | 36.6% | 93.6% | 100.0% |
| 7 | Australia | A | **2.8%** | -0.1 | 10.8% | 33.7% | 86.5% | 99.7% |
| 8 | Scotland | D | **2.7%** | -1.2 | 10.4% | 30.5% | 52.1% | 99.9% |
| 9 | Wales | F | **0.0%** | – | 0.7% | 5.6% | 52.1% | 95.8% |
| 10 | Italy | B | **0.0%** | – | 0.4% | 2.9% | 15.3% | 95.0% |
| 11 | Fiji | C | **0.0%** | – | 0.1% | 2.2% | 37.2% | 97.7% |
| 12 | Japan | E | **0.0%** | – | 0.1% | 1.2% | 9.2% | 80.5% |

## Biggest movers since last run (2026-07-18)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| South Africa | +2.9 | – | 33.1% |
| France | +2.4 | – | 12.7% |
| England | -0.3 | – | 5.7% |
| Argentina | -0.3 | – | 3.7% |
| Scotland | -1.2 | – | 2.7% |
| New Zealand | -3.4 | – | 25.9% |

## Path to the final

The model's single most likely knockout bracket — every projected tie from the Round of 16 down to the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1196 568" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,100 C94,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M238,100 C238,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,100 C382,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M526,100 C526,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M670,100 C670,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M814,100 C814,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M958,100 C958,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,100 C1102,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M166,222 C166,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M454,222 C454,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,222 C742,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1030,222 C1030,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M310,344 C310,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M886,344 C886,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M598,466 C598,485 598,485 598,504" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="12" y="77" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 77)" text-anchor="middle">ROUND OF 16</text><text x="12" y="199" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 199)" text-anchor="middle">QUARTER-FINALS</text><text x="12" y="321" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 321)" text-anchor="middle">SEMI-FINALS</text><text x="12" y="443" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 443)" text-anchor="middle">FINAL</text><rect x="28" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="28" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="37" y="72" font-size="11" font-weight="700" fill="#7ef0b6">N. Zealand</text><text x="151" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="37" y="93" font-size="11" font-weight="400" fill="#7c89a3">Spain</text><text x="151" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="172" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="172" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="181" y="72" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="295" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="181" y="93" font-size="11" font-weight="400" fill="#7c89a3">Tonga</text><text x="295" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="316" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="325" y="72" font-size="11" font-weight="400" fill="#7c89a3">Fiji</text><text x="439" y="72" font-size="9.5" text-anchor="end" fill="#5d6880">45%</text><rect x="316" y="78" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="325" y="93" font-size="11" font-weight="700" fill="#7ef0b6">Wales</text><text x="439" y="93" font-size="9.5" text-anchor="end" fill="#cfe8d8">55%</text><rect x="460" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="460" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="469" y="72" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="583" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">74%</text><text x="469" y="93" font-size="11" font-weight="400" fill="#7c89a3">Scotland</text><text x="583" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">26%</text><rect x="604" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="604" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="613" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="727" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">95%</text><text x="613" y="93" font-size="11" font-weight="400" fill="#7c89a3">Samoa</text><text x="727" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">5%</text><rect x="748" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="748" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="757" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="871" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="757" y="93" font-size="11" font-weight="400" fill="#7c89a3">Georgia</text><text x="871" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="892" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="892" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="901" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1015" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">84%</text><text x="901" y="93" font-size="11" font-weight="400" fill="#7c89a3">Japan</text><text x="1015" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">16%</text><rect x="1036" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1036" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1045" y="72" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1159" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">89%</text><text x="1045" y="93" font-size="11" font-weight="400" fill="#7c89a3">Italy</text><text x="1159" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">11%</text><rect x="100" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="109" y="194" font-size="11" font-weight="400" fill="#7c89a3">N. Zealand</text><text x="223" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">45%</text><rect x="100" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="223" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">55%</text><rect x="388" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="397" y="194" font-size="11" font-weight="400" fill="#7c89a3">Wales</text><text x="511" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">6%</text><rect x="388" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="397" y="215" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="511" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">94%</text><rect x="676" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="685" y="194" font-size="11" font-weight="400" fill="#7c89a3">Argentina</text><text x="799" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">23%</text><rect x="676" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="685" y="215" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="799" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">77%</text><rect x="964" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="973" y="194" font-size="11" font-weight="400" fill="#7c89a3">Australia</text><text x="1087" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">33%</text><rect x="964" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="973" y="215" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1087" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">67%</text><rect x="244" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="244" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="253" y="316" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="367" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">66%</text><text x="253" y="337" font-size="11" font-weight="400" fill="#7c89a3">France</text><text x="367" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">34%</text><rect x="820" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="820" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="829" y="316" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="943" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">60%</text><text x="829" y="337" font-size="11" font-weight="400" fill="#7c89a3">England</text><text x="943" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">40%</text><rect x="532" y="420" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="532" y="422" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="541" y="438" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="655" y="438" font-size="9.5" text-anchor="end" fill="#cfe8d8">77%</text><text x="541" y="459" font-size="11" font-weight="400" fill="#7c89a3">Ireland</text><text x="655" y="459" font-size="9.5" text-anchor="end" fill="#5d6880">23%</text><rect x="498" y="504" width="200" height="46" rx="10" fill="#f5c542"/><text x="598" y="525" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 S. Africa</text><text x="598" y="541" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 33% to win</text></svg>
</div>

## Upcoming internationals — match predictions

Every scheduled men's international on the calendar, not just RWC fixtures — the same model rates any pairing. Probabilities are for the listed home side; the predicted scoreline is the model's mean.

| Date | Competition | Match | Home win | Draw | Away win | Predicted | Favourite |
|------|-------------|-------|---------:|-----:|---------:|:---------:|----------|
| 2026-07-18 | Nations Championship | Argentina v England | **61.4%** | 2.3% | 36.2% | 29.3–24.1 | Argentina (61.4%) |
| 2026-08-08 | International Test Match | Japan v Australia | 41.5% | 2.4% | **56.1%** | 23.8–26.9 | Australia (56.1%) |
| 2026-08-08 | International Test Match | Argentina v South Africa | 16.1% | 1.5% | **82.3%** | 21.5–37.3 | South Africa (82.3%) |
| 2026-08-15 | International Test Match | Australia v Japan | **81.5%** | 1.6% | 17.0% | 34.1–18.9 | Australia (81.5%) |
| 2026-08-22 | International Test Match | South Africa v New Zealand | **60.7%** | 2.3% | 37.0% | 24.1–19.2 | South Africa (60.7%) |
| 2026-08-29 | International Test Match | South Africa v New Zealand | **60.7%** | 2.3% | 37.0% | 24.1–19.2 | South Africa (60.7%) |
| 2026-08-29 | International Test Match | Argentina v Australia | **71.5%** | 2.0% | 26.5% | 30.2–20.4 | Argentina (71.5%) |
| 2026-09-05 | International Test Match | Argentina v Australia | **71.5%** | 2.0% | 26.5% | 30.2–20.4 | Argentina (71.5%) |
| 2026-09-05 | International Test Match | South Africa v New Zealand | **60.7%** | 2.3% | 37.0% | 24.1–19.2 | South Africa (60.7%) |
| 2026-09-05 | International Test Match | Japan v Canada | **93.0%** | 0.8% | 6.2% | 41.9–17.1 | Japan (93.0%) |
| 2026-09-12 | International Test Match | South Africa v New Zealand (N) | **58.0%** | 2.4% | 39.6% | 23.5–19.7 | South Africa (58.0%) |
| 2026-09-27 | International Test Match | Australia v South Africa | 26.4% | 2.0% | **71.6%** | 22.7–32.6 | South Africa (71.6%) |
| 2026-10-10 | International Test Match | New Zealand v Australia | **89.7%** | 1.1% | 9.3% | 37.4–16.2 | New Zealand (89.7%) |
| 2026-10-17 | International Test Match | Australia v New Zealand | 28.4% | 2.1% | **69.5%** | 21.1–30.0 | New Zealand (69.5%) |
| 2026-11-06 | Nations Championship | Ireland v Argentina | **62.5%** | 2.3% | 35.2% | 29.6–23.9 | Ireland (62.5%) |
| 2026-11-07 | Nations Championship | France v Fiji | **97.8%** | 0.3% | 1.9% | 46.2–12.6 | France (97.8%) |
| 2026-11-07 | Nations Championship | Wales v Japan | **64.9%** | 2.2% | 32.9% | 29.1–22.3 | Wales (64.9%) |
| 2026-11-07 | Nations Championship | Italy v South Africa | 1.5% | 0.2% | **98.2%** | 12.6–47.8 | South Africa (98.2%) |
| 2026-11-07 | Nations Championship | Scotland v New Zealand | 28.5% | 2.1% | **69.5%** | 20.6–29.5 | New Zealand (69.5%) |
| 2026-11-08 | Nations Championship | England v Australia | **74.8%** | 1.9% | 23.3% | 32.8–21.3 | England (74.8%) |
| 2026-11-13 | Nations Championship | France v South Africa | 35.9% | 2.3% | **61.8%** | 24.1–29.5 | South Africa (61.8%) |
| 2026-11-14 | Nations Championship | Italy v Argentina | 19.2% | 1.7% | **79.1%** | 20.7–34.6 | Argentina (79.1%) |
| 2026-11-14 | Nations Championship | Wales v New Zealand | 9.0% | 1.0% | **89.9%** | 18.3–39.9 | New Zealand (89.9%) |
| 2026-11-14 | Nations Championship | England v Japan | **94.3%** | 0.7% | 5.1% | 40.7–14.2 | England (94.3%) |
| 2026-11-14 | Nations Championship | Ireland v Fiji | **94.5%** | 0.7% | 4.9% | 43.1–16.4 | Ireland (94.5%) |

*32 scheduled fixture(s) on file; full list with exact probabilities in `upcoming_predictions.csv`. "(N)" = neutral venue.*

## Pool projections

### Pool A

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| New Zealand | 13.25 | 72.4% | 99.9% | 100.0% |
| Australia | 10.87 | 27.6% | 97.1% | 99.7% |
| Hong Kong China | 2.97 | 0.0% | 1.2% | 26.2% |
| Chile | 2.74 | 0.0% | 1.8% | 22.7% |

### Pool B

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| South Africa | 14.52 | 98.0% | 100.0% | 100.0% |
| Italy | 8.17 | 1.9% | 74.3% | 95.0% |
| Georgia | 5.18 | 0.0% | 22.8% | 63.7% |
| Romania | 1.88 | 0.0% | 2.9% | 13.8% |

### Pool C

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Argentina | 14.00 | 90.5% | 99.8% | 100.0% |
| Fiji | 8.93 | 9.1% | 77.2% | 97.7% |
| Spain | 5.48 | 0.4% | 21.8% | 72.2% |
| Canada | 1.41 | 0.0% | 1.2% | 8.8% |

### Pool D

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Ireland | 12.70 | 61.5% | 99.6% | 100.0% |
| Scotland | 11.48 | 38.4% | 98.4% | 99.9% |
| Portugal | 2.82 | 0.0% | 0.8% | 24.2% |
| Uruguay | 2.82 | 0.0% | 1.2% | 25.6% |

### Pool E

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| France | 14.36 | 97.1% | 99.9% | 100.0% |
| Japan | 6.76 | 2.7% | 54.6% | 80.5% |
| Samoa | 5.38 | 0.1% | 32.1% | 64.4% |
| United States | 3.27 | 0.1% | 13.3% | 32.3% |

### Pool F

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| England | 13.62 | 84.2% | 99.7% | 100.0% |
| Wales | 9.18 | 15.4% | 82.8% | 95.8% |
| Tonga | 4.50 | 0.3% | 11.9% | 55.4% |
| Zimbabwe | 2.48 | 0.1% | 5.6% | 22.1% |

*\*Advance = top two of the pool or one of the four best third-placed teams.*

## Most likely knockout bracket

Each tie shows the projected pairing and the named side's chance of advancing in that pairing.

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| R16-1 | 2027-10-23 | Sydney Football Stadium | Fiji v Wales | **Wales** | 55.3% |
| R16-2 | 2027-10-23 | Brisbane Stadium | New Zealand v Spain | **New Zealand** | 99.0% |
| R16-3 | 2027-10-23 | Docklands Stadium, Melbourne | France v Scotland | **France** | 74.1% |
| R16-4 | 2027-10-24 | Perth Stadium | South Africa v Tonga | **South Africa** | 99.0% |
| R16-5 | 2027-10-24 | Sydney Football Stadium | Argentina v Samoa | **Argentina** | 94.8% |
| R16-6 | 2027-10-24 | Docklands Stadium, Melbourne | Ireland v Georgia | **Ireland** | 99.0% |
| R16-7 | 2027-10-23 | Brisbane Stadium | Australia v Japan | **Australia** | 83.9% |
| R16-8 | 2027-10-24 | Perth Stadium | England v Italy | **England** | 89.1% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| QF1 | 2027-10-30 | Stadium Australia, Sydney | New Zealand v South Africa | **South Africa** | 54.5% |
| QF2 | 2027-10-30 | Brisbane Stadium | Wales v France | **France** | 93.6% |
| QF3 | 2027-10-31 | Brisbane Stadium | Argentina v Ireland | **Ireland** | 76.9% |
| QF4 | 2027-10-31 | Stadium Australia, Sydney | Australia v England | **England** | 66.7% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| SF1 | 2027-11-05 | Stadium Australia, Sydney | South Africa v France | **South Africa** | 65.7% |
| SF2 | 2027-11-06 | Stadium Australia, Sydney | Ireland v England | **Ireland** | 60.5% |

### Bronze final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| BF | 2027-11-12 | Stadium Australia, Sydney | France v England | **France** | 61.2% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| F | 2027-11-13 | Stadium Australia, Sydney | South Africa v Ireland | **South Africa** | 76.7% |

**Projected champion: South Africa** (overall title probability 33.1% — the single path above is only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite still loses about one such match in three.
- Rugby is more predictable than football (few draws, favourites hold more often), but 2027 is well out, so early forecasts are low-information and will sharpen as warm-up tests are played.
- `xPts` = expected pool points (incl. bonus points). Predictions refresh hourly: `python -m rugby.run all`.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
