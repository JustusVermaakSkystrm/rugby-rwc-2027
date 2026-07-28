# Rugby World Cup 2027 — ML Prediction Report

*Generated 2026-07-28 · data through **2026-07-18** · 50,000 Monte Carlo simulations · 0/36 pool matches played*

Probabilities come from a **margin + total Gaussian model** (World Rugby ranking + Elo strength, points attack/defence, rolling form, venue/importance) trained on 1,920 internationals, simulated through the official RWC 2027 bracket with bonus-point pool standings and tiebreakers.

*Rolling validation (974 matches): chosen model **margin_total** — RPS 0.1574 vs ranking-only baseline 0.1570; margin MAE 12.66 pts vs 12.57.*

## Following South Africa — upcoming fixtures

Every scheduled South Africa international, with kick-off in your timezones, the model's call, and where to watch.

| Date | Kick-off | Opponent | Competition | Venue | Model call | Where to watch |
|------|----------|----------|-------------|-------|-----------|----------------|
| Sat 08 Aug 2026 | 20:00 UK · 21:00 SAST | Argentina (A) | International Test Match | Estadio José Amalfitani | **87.4%** win · 40–20 | SuperSport (SA)? |
| Sat 22 Aug 2026 | 16:10 UK · 17:10 SAST | New Zealand (H) | International Test Match | Ellis Park | **50.0%** win · 23–22 | SuperSport (SA)? |
| Sat 29 Aug 2026 | 16:10 UK · 17:10 SAST | New Zealand (H) | International Test Match | DHL Stadium | **50.0%** win · 23–22 | SuperSport (SA)? |
| Sat 05 Sep 2026 | 16:10 UK · 17:10 SAST | New Zealand (H) | International Test Match | FNB Stadium | **50.0%** win · 23–22 | SuperSport (SA)? |
| Sat 12 Sep 2026 | 22:00 UK · 23:00 SAST | New Zealand (N) | International Test Match | M&T Bank Stadium | **45.9%** win · 22–23 | SuperSport (SA)? |
| Sun 27 Sep 2026 | 10:45 UK · 11:45 SAST | Australia (A) | International Test Match | Optus Stadium | **70.6%** win · 32–22 | SuperSport (SA)? |
| Sat 07 Nov 2026 | 11:40 UK · 13:40 SAST | Italy (A) | Nations Championship | Allianz Stadium | **96.0%** win · 44–14 | ITV (UK) · SuperSport (SA) |
| Fri 13 Nov 2026 | 20:10 UK · 22:10 SAST | France (A) | Nations Championship | Stade de France | **58.1%** win · 29–25 | ITV (UK) · SuperSport (SA) |
| Sat 21 Nov 2026 | 16:40 UK · 18:40 SAST | Ireland (A) | Nations Championship | Aviva Stadium | **57.9%** win · 28–24 | ITV (UK) · SuperSport (SA) |

*Kick-off times are converted from the official UTC start time. Broadcast listings are curated (ESPN publishes none for internationals), as of 2026-07-02 — a "?" marks rights we could not confirm for this cycle, so check local listings.*

## Title favourites

| # | Team | Pool | Champion | Δ vs 2026-07-18 | Final | Semi | Quarter | Rd of 16 |
|---|------|:----:|---------:|-------:|------:|----:|--------:|---------:|
| 1 | South Africa | B | **30.2%** | – | 42.0% | 59.4% | 97.7% | 100.0% |
| 2 | New Zealand | A | **21.4%** | – | 35.1% | 54.4% | 97.8% | 100.0% |
| 3 | France | E | **15.4%** | – | 27.3% | 61.4% | 66.6% | 100.0% |
| 4 | Ireland | D | **15.1%** | – | 35.5% | 63.9% | 83.8% | 100.0% |
| 5 | England | F | **7.6%** | – | 24.4% | 50.2% | 90.4% | 100.0% |
| 6 | Australia | A | **3.9%** | – | 11.9% | 34.2% | 86.9% | 99.6% |
| 7 | Scotland | D | **3.2%** | – | 10.9% | 34.3% | 47.3% | 99.8% |
| 8 | Argentina | C | **3.2%** | – | 12.0% | 31.8% | 89.0% | 100.0% |
| 9 | Wales | F | **0.0%** | – | 0.4% | 3.9% | 57.6% | 96.3% |
| 10 | Italy | B | **0.0%** | – | 0.3% | 2.4% | 12.8% | 97.1% |
| 11 | Fiji | C | **0.0%** | – | 0.1% | 1.8% | 34.6% | 97.6% |
| 12 | Japan | E | **0.0%** | – | 0.1% | 0.7% | 8.4% | 78.4% |

## Path to the final

The model's single most likely knockout bracket — every projected tie from the Round of 16 down to the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1196 568" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,100 C94,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M238,100 C238,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,100 C382,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M526,100 C526,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M670,100 C670,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M814,100 C814,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M958,100 C958,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,100 C1102,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M166,222 C166,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M454,222 C454,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,222 C742,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1030,222 C1030,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M310,344 C310,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M886,344 C886,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M598,466 C598,485 598,485 598,504" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="12" y="77" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 77)" text-anchor="middle">ROUND OF 16</text><text x="12" y="199" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 199)" text-anchor="middle">QUARTER-FINALS</text><text x="12" y="321" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 321)" text-anchor="middle">SEMI-FINALS</text><text x="12" y="443" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 443)" text-anchor="middle">FINAL</text><rect x="28" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="28" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="37" y="72" font-size="11" font-weight="700" fill="#7ef0b6">N. Zealand</text><text x="151" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="37" y="93" font-size="11" font-weight="400" fill="#7c89a3">Spain</text><text x="151" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="172" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="172" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="181" y="72" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="295" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="181" y="93" font-size="11" font-weight="400" fill="#7c89a3">Samoa</text><text x="295" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="316" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="325" y="72" font-size="11" font-weight="400" fill="#7c89a3">Fiji</text><text x="439" y="72" font-size="9.5" text-anchor="end" fill="#5d6880">30%</text><rect x="316" y="78" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="325" y="93" font-size="11" font-weight="700" fill="#7ef0b6">Wales</text><text x="439" y="93" font-size="9.5" text-anchor="end" fill="#cfe8d8">70%</text><rect x="460" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="460" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="469" y="72" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="583" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">72%</text><text x="469" y="93" font-size="11" font-weight="400" fill="#7c89a3">Scotland</text><text x="583" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">28%</text><rect x="604" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="604" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="613" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="727" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="613" y="93" font-size="11" font-weight="400" fill="#7c89a3">Zimbabwe</text><text x="727" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="748" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="748" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="757" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="871" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="757" y="93" font-size="11" font-weight="400" fill="#7c89a3">Georgia</text><text x="871" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="892" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="892" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="901" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1015" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">87%</text><text x="901" y="93" font-size="11" font-weight="400" fill="#7c89a3">Japan</text><text x="1015" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">13%</text><rect x="1036" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1036" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1045" y="72" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1159" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">91%</text><text x="1045" y="93" font-size="11" font-weight="400" fill="#7c89a3">Italy</text><text x="1159" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">9%</text><rect x="100" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="109" y="194" font-size="11" font-weight="400" fill="#7c89a3">N. Zealand</text><text x="223" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">43%</text><rect x="100" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="223" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">57%</text><rect x="388" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="397" y="194" font-size="11" font-weight="400" fill="#7c89a3">Wales</text><text x="511" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">3%</text><rect x="388" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="397" y="215" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="511" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">97%</text><rect x="676" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="685" y="194" font-size="11" font-weight="400" fill="#7c89a3">Argentina</text><text x="799" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">32%</text><rect x="676" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="685" y="215" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="799" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">68%</text><rect x="964" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="973" y="194" font-size="11" font-weight="400" fill="#7c89a3">Australia</text><text x="1087" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">33%</text><rect x="964" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="973" y="215" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1087" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">67%</text><rect x="244" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="244" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="253" y="316" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="367" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">64%</text><text x="253" y="337" font-size="11" font-weight="400" fill="#7c89a3">France</text><text x="367" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">36%</text><rect x="820" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="820" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="829" y="316" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="943" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">67%</text><text x="829" y="337" font-size="11" font-weight="400" fill="#7c89a3">England</text><text x="943" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">33%</text><rect x="532" y="420" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="532" y="422" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="541" y="438" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="655" y="438" font-size="9.5" text-anchor="end" fill="#cfe8d8">75%</text><text x="541" y="459" font-size="11" font-weight="400" fill="#7c89a3">Ireland</text><text x="655" y="459" font-size="9.5" text-anchor="end" fill="#5d6880">25%</text><rect x="498" y="504" width="200" height="46" rx="10" fill="#f5c542"/><text x="598" y="525" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 S. Africa</text><text x="598" y="541" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 30% to win</text></svg>
</div>

## Upcoming internationals — match predictions

Every scheduled men's international on the calendar, not just RWC fixtures — the same model rates any pairing. Probabilities are for the listed home side; the predicted scoreline is the model's mean.

| Date | Competition | Match | Home win | Draw | Away win | Predicted | Favourite |
|------|-------------|-------|---------:|-----:|---------:|:---------:|----------|
| 2026-08-08 | International Test Match | Japan v Australia | 33.1% | 2.2% | **64.7%** | 24.1–30.9 | Australia (64.7%) |
| 2026-08-08 | International Test Match | Argentina v South Africa | 11.5% | 1.2% | **87.4%** | 20.4–39.9 | South Africa (87.4%) |
| 2026-08-15 | International Test Match | Australia v Japan | **85.6%** | 1.3% | 13.1% | 35.6–17.4 | Australia (85.6%) |
| 2026-08-22 | International Test Match | South Africa v New Zealand | **50.0%** | 2.4% | 47.6% | 22.7–22.2 | South Africa (50.0%) |
| 2026-08-29 | International Test Match | South Africa v New Zealand | **50.0%** | 2.4% | 47.6% | 22.7–22.2 | South Africa (50.0%) |
| 2026-08-29 | International Test Match | Argentina v Australia | **62.6%** | 2.2% | 35.1% | 30.2–24.3 | Argentina (62.6%) |
| 2026-09-05 | International Test Match | South Africa v New Zealand | **50.0%** | 2.4% | 47.6% | 22.7–22.2 | South Africa (50.0%) |
| 2026-09-05 | International Test Match | Argentina v Australia | **62.6%** | 2.2% | 35.1% | 30.2–24.3 | Argentina (62.6%) |
| 2026-09-05 | International Test Match | Japan v Canada | **94.3%** | 0.7% | 5.0% | 42.7–15.8 | Japan (94.3%) |
| 2026-09-12 | International Test Match | South Africa v New Zealand (N) | 45.9% | 2.4% | **51.7%** | 21.8–23.0 | New Zealand (51.7%) |
| 2026-09-27 | International Test Match | Australia v South Africa | 27.3% | 2.0% | **70.6%** | 22.1–31.7 | South Africa (70.6%) |
| 2026-10-10 | International Test Match | New Zealand v Australia | **88.3%** | 1.1% | 10.5% | 36.4–16.0 | New Zealand (88.3%) |
| 2026-10-17 | International Test Match | Australia v New Zealand | 28.6% | 2.1% | **69.4%** | 22.9–31.8 | New Zealand (69.4%) |
| 2026-10-24 | International Test Match | Japan v Fiji | **53.0%** | 2.4% | 44.6% | 27.0–25.2 | Japan (53.0%) |
| 2026-11-06 | Nations Championship | Ireland v Argentina | **75.1%** | 1.9% | 23.0% | 34.9–23.1 | Ireland (75.1%) |
| 2026-11-07 | Nations Championship | France v Fiji | **95.7%** | 0.5% | 3.8% | 43.0–14.0 | France (95.7%) |
| 2026-11-07 | Nations Championship | Wales v Japan | **55.7%** | 2.4% | 42.0% | 29.1–26.3 | Wales (55.7%) |
| 2026-11-07 | Nations Championship | Scotland v New Zealand | 33.0% | 2.2% | **64.8%** | 24.3–31.1 | New Zealand (64.8%) |
| 2026-11-07 | Nations Championship | Italy v South Africa | 3.5% | 0.5% | **96.0%** | 14.2–44.0 | South Africa (96.0%) |
| 2026-11-08 | Nations Championship | England v Australia | **73.3%** | 1.9% | 24.7% | 32.4–21.5 | England (73.3%) |
| 2026-11-13 | Nations Championship | France v South Africa | 39.5% | 2.3% | **58.1%** | 25.4–29.3 | South Africa (58.1%) |
| 2026-11-14 | Nations Championship | Italy v Argentina | 21.0% | 1.8% | **77.3%** | 22.9–35.9 | Argentina (77.3%) |
| 2026-11-14 | Nations Championship | Wales v New Zealand | 6.1% | 0.8% | **93.2%** | 17.8–43.2 | New Zealand (93.2%) |
| 2026-11-14 | Nations Championship | England v Japan | **91.0%** | 0.9% | 8.1% | 38.5–15.6 | England (91.0%) |
| 2026-11-14 | Nations Championship | Ireland v Fiji | **96.5%** | 0.4% | 3.1% | 43.1–12.5 | Ireland (96.5%) |

*33 scheduled fixture(s) on file; full list with exact probabilities in `upcoming_predictions.csv`. "(N)" = neutral venue.*

## Pool projections

### Pool A

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| New Zealand | 12.84 | 64.0% | 99.7% | 100.0% |
| Australia | 11.15 | 35.9% | 96.2% | 99.6% |
| Hong Kong China | 3.15 | 0.0% | 1.1% | 27.3% |
| Chile | 2.74 | 0.1% | 3.0% | 24.3% |

### Pool B

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| South Africa | 14.45 | 97.7% | 100.0% | 100.0% |
| Italy | 8.44 | 2.0% | 76.1% | 97.1% |
| Georgia | 5.60 | 0.2% | 23.0% | 74.3% |
| Romania | 1.16 | 0.0% | 1.0% | 6.5% |

### Pool C

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Argentina | 13.23 | 81.4% | 98.1% | 100.0% |
| Fiji | 9.40 | 16.2% | 80.3% | 97.6% |
| Spain | 5.53 | 2.4% | 20.1% | 71.4% |
| Canada | 1.62 | 0.0% | 1.6% | 10.5% |

### Pool D

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Ireland | 13.23 | 72.0% | 99.7% | 100.0% |
| Scotland | 11.00 | 27.9% | 97.7% | 99.8% |
| Uruguay | 3.01 | 0.1% | 1.8% | 27.5% |
| Portugal | 2.64 | 0.0% | 0.8% | 20.4% |

### Pool E

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| France | 14.21 | 96.1% | 99.8% | 100.0% |
| Japan | 6.61 | 2.9% | 50.0% | 78.4% |
| Samoa | 5.99 | 0.8% | 39.1% | 72.9% |
| United States | 3.04 | 0.1% | 11.0% | 28.4% |

### Pool F

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| England | 14.05 | 91.5% | 99.9% | 100.0% |
| Wales | 8.92 | 8.4% | 83.9% | 96.3% |
| Zimbabwe | 3.68 | 0.1% | 10.6% | 38.9% |
| Tonga | 3.01 | 0.1% | 5.5% | 28.7% |

*\*Advance = top two of the pool or one of the four best third-placed teams.*

## Most likely knockout bracket

Each tie shows the projected pairing and the named side's chance of advancing in that pairing.

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| R16-1 | 2027-10-23 | Sydney Football Stadium | Fiji v Wales | **Wales** | 70.0% |
| R16-2 | 2027-10-23 | Brisbane Stadium | New Zealand v Spain | **New Zealand** | 99.0% |
| R16-3 | 2027-10-23 | Docklands Stadium, Melbourne | France v Scotland | **France** | 71.6% |
| R16-4 | 2027-10-24 | Perth Stadium | South Africa v Samoa | **South Africa** | 99.0% |
| R16-5 | 2027-10-24 | Sydney Football Stadium | Argentina v Zimbabwe | **Argentina** | 98.6% |
| R16-6 | 2027-10-24 | Docklands Stadium, Melbourne | Ireland v Georgia | **Ireland** | 99.0% |
| R16-7 | 2027-10-23 | Brisbane Stadium | Australia v Japan | **Australia** | 86.9% |
| R16-8 | 2027-10-24 | Perth Stadium | England v Italy | **England** | 91.1% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| QF1 | 2027-10-30 | Stadium Australia, Sydney | New Zealand v South Africa | **South Africa** | 56.7% |
| QF2 | 2027-10-30 | Brisbane Stadium | Wales v France | **France** | 96.6% |
| QF3 | 2027-10-31 | Brisbane Stadium | Argentina v Ireland | **Ireland** | 68.2% |
| QF4 | 2027-10-31 | Stadium Australia, Sydney | Australia v England | **England** | 67.5% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| SF1 | 2027-11-05 | Stadium Australia, Sydney | South Africa v France | **South Africa** | 64.3% |
| SF2 | 2027-11-06 | Stadium Australia, Sydney | Ireland v England | **Ireland** | 67.1% |

### Bronze final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| BF | 2027-11-12 | Stadium Australia, Sydney | France v England | **France** | 59.8% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| F | 2027-11-13 | Stadium Australia, Sydney | South Africa v Ireland | **South Africa** | 74.8% |

**Projected champion: South Africa** (overall title probability 30.2% — the single path above is only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite still loses about one such match in three.
- Rugby is more predictable than football (few draws, favourites hold more often), but 2027 is well out, so early forecasts are low-information and will sharpen as warm-up tests are played.
- `xPts` = expected pool points (incl. bonus points). Predictions refresh hourly: `python -m rugby.run all`.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
