# Rugby World Cup 2027 — ML Prediction Report

*Generated 2026-09-04 · data through **2026-08-29** · 50,000 Monte Carlo simulations · 0/36 pool matches played*

Probabilities come from a **margin + total Gaussian model** (World Rugby ranking + Elo strength, points attack/defence, rolling form, venue/importance) trained on 1,924 internationals, simulated through the official RWC 2027 bracket with bonus-point pool standings and tiebreakers.

*Rolling validation (974 matches): chosen model **margin_total** — RPS 0.1574 vs ranking-only baseline 0.1570; margin MAE 12.66 pts vs 12.57.*

## Following South Africa — upcoming fixtures

Every scheduled South Africa international, with kick-off in your timezones, the model's call, and where to watch.

| Date | Kick-off | Opponent | Competition | Venue | Model call | Where to watch |
|------|----------|----------|-------------|-------|-----------|----------------|
| Sat 05 Sep 2026 | 16:10 UK · 17:10 SAST | New Zealand (H) | International Test Match | FNB Stadium | **50.3%** win · 28–27 | SuperSport (SA)? |
| Sat 12 Sep 2026 | 22:00 UK · 23:00 SAST | New Zealand (N) | International Test Match | M&T Bank Stadium | **50.2%** win · 27–27 | SuperSport (SA)? |
| Sun 27 Sep 2026 | 10:45 UK · 11:45 SAST | Australia (A) | International Test Match | Optus Stadium | **76.4%** win · 33–21 | SuperSport (SA)? |
| Sat 07 Nov 2026 | 11:40 UK · 13:40 SAST | Italy (A) | Nations Championship | Allianz Stadium | **97.8%** win · 45–11 | ITV (UK) · SuperSport (SA) |
| Fri 13 Nov 2026 | 20:10 UK · 22:10 SAST | France (A) | Nations Championship | Stade de France | **62.8%** win · 30–24 | ITV (UK) · SuperSport (SA) |
| Sat 21 Nov 2026 | 16:40 UK · 18:40 SAST | Ireland (A) | Nations Championship | Aviva Stadium | **57.1%** win · 28–25 | ITV (UK) · SuperSport (SA) |

*Kick-off times are converted from the official UTC start time. Broadcast listings are curated (ESPN publishes none for internationals), as of 2026-07-02 — a "?" marks rights we could not confirm for this cycle, so check local listings.*

## Title favourites

| # | Team | Pool | Champion | Δ vs 2026-08-29 | Final | Semi | Quarter | Rd of 16 |
|---|------|:----:|---------:|-------:|------:|----:|--------:|---------:|
| 1 | South Africa | B | **29.0%** | – | 38.7% | 56.9% | 97.9% | 100.0% |
| 2 | New Zealand | A | **26.1%** | – | 37.2% | 53.5% | 98.2% | 100.0% |
| 3 | France | E | **13.3%** | – | 25.0% | 56.0% | 61.8% | 100.0% |
| 4 | Ireland | D | **11.2%** | – | 30.1% | 60.9% | 79.3% | 100.0% |
| 5 | England | F | **10.8%** | – | 30.0% | 54.9% | 91.5% | 100.0% |
| 6 | Scotland | D | **4.0%** | – | 14.3% | 41.8% | 55.5% | 99.9% |
| 7 | Australia | A | **3.5%** | – | 15.0% | 35.5% | 92.1% | 99.9% |
| 8 | Argentina | C | **2.1%** | – | 8.9% | 30.9% | 88.5% | 100.0% |
| 9 | Wales | F | **0.0%** | – | 0.5% | 4.1% | 47.6% | 96.8% |
| 10 | Italy | B | **0.0%** | – | 0.2% | 1.5% | 11.7% | 96.6% |
| 11 | Fiji | C | **0.0%** | – | 0.1% | 2.2% | 47.5% | 98.5% |
| 12 | Japan | E | **0.0%** | – | 0.0% | 0.5% | 6.0% | 80.9% |

## Path to the final

The model's single most likely knockout bracket — every projected tie from the Round of 16 down to the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1196 568" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,100 C94,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M238,100 C238,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,100 C382,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M526,100 C526,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M670,100 C670,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M814,100 C814,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M958,100 C958,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,100 C1102,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M166,222 C166,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M454,222 C454,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,222 C742,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1030,222 C1030,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M310,344 C310,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M886,344 C886,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M598,466 C598,485 598,485 598,504" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="12" y="77" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 77)" text-anchor="middle">ROUND OF 16</text><text x="12" y="199" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 199)" text-anchor="middle">QUARTER-FINALS</text><text x="12" y="321" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 321)" text-anchor="middle">SEMI-FINALS</text><text x="12" y="443" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 443)" text-anchor="middle">FINAL</text><rect x="28" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="28" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="37" y="72" font-size="11" font-weight="700" fill="#7ef0b6">N. Zealand</text><text x="151" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="37" y="93" font-size="11" font-weight="400" fill="#7c89a3">Spain</text><text x="151" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="172" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="172" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="181" y="72" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="295" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="181" y="93" font-size="11" font-weight="400" fill="#7c89a3">Tonga</text><text x="295" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="316" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="316" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="325" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Fiji</text><text x="439" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">51%</text><text x="325" y="93" font-size="11" font-weight="400" fill="#7c89a3">Wales</text><text x="439" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">49%</text><rect x="460" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="460" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="469" y="72" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="583" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">67%</text><text x="469" y="93" font-size="11" font-weight="400" fill="#7c89a3">Scotland</text><text x="583" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">33%</text><rect x="604" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="604" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="613" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="727" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">94%</text><text x="613" y="93" font-size="11" font-weight="400" fill="#7c89a3">Samoa</text><text x="727" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">6%</text><rect x="748" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="748" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="757" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="871" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">98%</text><text x="757" y="93" font-size="11" font-weight="400" fill="#7c89a3">Georgia</text><text x="871" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">2%</text><rect x="892" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="892" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="901" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1015" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">92%</text><text x="901" y="93" font-size="11" font-weight="400" fill="#7c89a3">Japan</text><text x="1015" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">8%</text><rect x="1036" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1036" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1045" y="72" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1159" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">92%</text><text x="1045" y="93" font-size="11" font-weight="400" fill="#7c89a3">Italy</text><text x="1159" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">8%</text><rect x="100" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="109" y="194" font-size="11" font-weight="400" fill="#7c89a3">N. Zealand</text><text x="223" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">48%</text><rect x="100" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="223" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">52%</text><rect x="388" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="397" y="194" font-size="11" font-weight="400" fill="#7c89a3">Fiji</text><text x="511" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">2%</text><rect x="388" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="397" y="215" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="511" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">98%</text><rect x="676" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="685" y="194" font-size="11" font-weight="400" fill="#7c89a3">Argentina</text><text x="799" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">34%</text><rect x="676" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="685" y="215" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="799" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">66%</text><rect x="964" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="973" y="194" font-size="11" font-weight="400" fill="#7c89a3">Australia</text><text x="1087" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">33%</text><rect x="964" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="973" y="215" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1087" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">67%</text><rect x="244" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="244" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="253" y="316" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="367" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">55%</text><text x="253" y="337" font-size="11" font-weight="400" fill="#7c89a3">France</text><text x="367" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">45%</text><rect x="820" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="820" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="829" y="316" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="943" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">58%</text><text x="829" y="337" font-size="11" font-weight="400" fill="#7c89a3">England</text><text x="943" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">42%</text><rect x="532" y="420" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="532" y="422" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="541" y="438" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="655" y="438" font-size="9.5" text-anchor="end" fill="#cfe8d8">82%</text><text x="541" y="459" font-size="11" font-weight="400" fill="#7c89a3">Ireland</text><text x="655" y="459" font-size="9.5" text-anchor="end" fill="#5d6880">18%</text><rect x="498" y="504" width="200" height="46" rx="10" fill="#f5c542"/><text x="598" y="525" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 S. Africa</text><text x="598" y="541" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 29% to win</text></svg>
</div>

## Upcoming internationals — match predictions

Every scheduled men's international on the calendar, not just RWC fixtures — the same model rates any pairing. Probabilities are for the listed home side; the predicted scoreline is the model's mean.

| Date | Competition | Match | Home win | Draw | Away win | Predicted | Favourite |
|------|-------------|-------|---------:|-----:|---------:|:---------:|----------|
| 2026-09-05 | International Test Match | Japan v Canada | **95.4%** | 0.5% | 4.0% | 44.9–16.3 | Japan (95.4%) |
| 2026-09-05 | International Test Match | South Africa v New Zealand | **50.3%** | 2.4% | 47.3% | 28.0–27.4 | South Africa (50.3%) |
| 2026-09-05 | International Test Match | Argentina v Australia | **49.5%** | 2.4% | 48.1% | 27.6–27.3 | Argentina (49.5%) |
| 2026-09-12 | International Test Match | South Africa v New Zealand (N) | **50.2%** | 2.4% | 47.4% | 27.4–26.8 | South Africa (50.2%) |
| 2026-09-27 | International Test Match | Australia v South Africa | 21.8% | 1.8% | **76.4%** | 20.8–33.3 | South Africa (76.4%) |
| 2026-10-10 | International Test Match | New Zealand v Australia | **88.5%** | 1.1% | 10.4% | 38.4–18.0 | New Zealand (88.5%) |
| 2026-10-17 | International Test Match | Australia v New Zealand | 19.8% | 1.7% | **78.5%** | 22.7–36.3 | New Zealand (78.5%) |
| 2026-10-24 | International Test Match | Japan v Fiji | **49.4%** | 2.4% | 48.2% | 25.9–25.6 | Japan (49.4%) |
| 2026-10-31 | International Test Match | Belgium v Hong Kong China | 43.3% | 2.4% | **54.3%** | 22.5–24.8 | Hong Kong China (54.3%) |
| 2026-11-06 | Nations Championship | Ireland v Argentina | **69.4%** | 2.1% | 28.5% | 32.9–24.0 | Ireland (69.4%) |
| 2026-11-07 | Nations Championship | Wales v Japan | **60.8%** | 2.3% | 36.9% | 29.6–24.6 | Wales (60.8%) |
| 2026-11-07 | Nations Championship | France v Fiji | **96.6%** | 0.4% | 2.9% | 44.6–13.7 | France (96.6%) |
| 2026-11-07 | Nations Championship | Italy v South Africa | 1.9% | 0.3% | **97.8%** | 11.3–45.3 | South Africa (97.8%) |
| 2026-11-07 | Nations Championship | Scotland v New Zealand | 24.6% | 1.9% | **73.4%** | 23.0–33.9 | New Zealand (73.4%) |
| 2026-11-08 | Nations Championship | England v Australia | **64.0%** | 2.2% | 33.8% | 30.4–23.9 | England (64.0%) |
| 2026-11-13 | Nations Championship | France v South Africa | 34.9% | 2.2% | **62.8%** | 24.1–30.0 | South Africa (62.8%) |
| 2026-11-14 | Nations Championship | Italy v Argentina | 24.8% | 1.9% | **73.2%** | 20.3–31.1 | Argentina (73.2%) |
| 2026-11-14 | Nations Championship | Wales v New Zealand | 4.3% | 0.6% | **95.1%** | 18.8–46.9 | New Zealand (95.1%) |
| 2026-11-14 | Nations Championship | England v Japan | **94.1%** | 0.7% | 5.2% | 39.9–13.4 | England (94.1%) |
| 2026-11-14 | Nations Championship | Ireland v Fiji | **95.1%** | 0.6% | 4.3% | 46.2–18.2 | Ireland (95.1%) |
| 2026-11-14 | International Test Match | Paraguay v Brazil | **62.9%** | 2.2% | 34.8% | 31.0–25.0 | Paraguay (62.9%) |
| 2026-11-15 | Nations Championship | Scotland v Australia | 43.4% | 2.4% | **54.2%** | 26.7–29.0 | Australia (54.2%) |
| 2026-11-21 | Nations Championship | France v Argentina | **74.8%** | 1.9% | 23.3% | 33.6–22.0 | France (74.8%) |
| 2026-11-21 | Nations Championship | England v New Zealand | 38.1% | 2.3% | **59.6%** | 26.4–30.9 | New Zealand (59.6%) |
| 2026-11-21 | Nations Championship | Scotland v Japan | **93.2%** | 0.8% | 6.0% | 40.8–15.4 | Scotland (93.2%) |

*28 scheduled fixture(s) on file; full list with exact probabilities in `upcoming_predictions.csv`. "(N)" = neutral venue.*

## Pool projections

### Pool A

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| New Zealand | 13.71 | 79.7% | 99.9% | 100.0% |
| Australia | 10.78 | 20.2% | 98.0% | 99.9% |
| Chile | 3.43 | 0.0% | 1.6% | 31.8% |
| Hong Kong China | 2.16 | 0.0% | 0.5% | 15.2% |

### Pool B

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| South Africa | 14.57 | 98.3% | 100.0% | 100.0% |
| Italy | 8.29 | 1.6% | 73.8% | 96.6% |
| Georgia | 5.70 | 0.2% | 25.1% | 75.4% |
| Romania | 1.17 | 0.0% | 1.1% | 6.5% |

### Pool C

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Argentina | 13.33 | 79.7% | 99.0% | 100.0% |
| Fiji | 9.83 | 19.3% | 86.3% | 98.5% |
| Spain | 5.04 | 1.0% | 13.4% | 66.7% |
| Canada | 1.62 | 0.0% | 1.3% | 10.9% |

### Pool D

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Ireland | 12.83 | 62.9% | 99.5% | 100.0% |
| Scotland | 11.48 | 37.0% | 98.1% | 99.9% |
| Uruguay | 3.34 | 0.1% | 1.5% | 32.9% |
| Portugal | 2.40 | 0.0% | 0.9% | 19.1% |

### Pool E

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| France | 14.33 | 97.5% | 99.9% | 100.0% |
| Japan | 6.79 | 2.0% | 54.8% | 80.9% |
| Samoa | 5.62 | 0.4% | 34.0% | 69.1% |
| United States | 2.95 | 0.1% | 11.2% | 28.0% |

### Pool F

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| England | 13.87 | 88.6% | 99.8% | 100.0% |
| Wales | 9.13 | 11.1% | 86.1% | 96.8% |
| Tonga | 4.31 | 0.2% | 8.9% | 52.2% |
| Zimbabwe | 2.32 | 0.0% | 5.1% | 19.6% |

*\*Advance = top two of the pool or one of the four best third-placed teams.*

## Most likely knockout bracket

Each tie shows the projected pairing and the named side's chance of advancing in that pairing.

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| R16-1 | 2027-10-23 | Sydney Football Stadium | Fiji v Wales | **Fiji** | 50.5% |
| R16-2 | 2027-10-23 | Brisbane Stadium | New Zealand v Spain | **New Zealand** | 99.0% |
| R16-3 | 2027-10-23 | Docklands Stadium, Melbourne | France v Scotland | **France** | 66.9% |
| R16-4 | 2027-10-24 | Perth Stadium | South Africa v Tonga | **South Africa** | 99.0% |
| R16-5 | 2027-10-24 | Sydney Football Stadium | Argentina v Samoa | **Argentina** | 94.1% |
| R16-6 | 2027-10-24 | Docklands Stadium, Melbourne | Ireland v Georgia | **Ireland** | 98.5% |
| R16-7 | 2027-10-23 | Brisbane Stadium | Australia v Japan | **Australia** | 92.3% |
| R16-8 | 2027-10-24 | Perth Stadium | England v Italy | **England** | 91.8% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| QF1 | 2027-10-30 | Stadium Australia, Sydney | New Zealand v South Africa | **South Africa** | 51.7% |
| QF2 | 2027-10-30 | Brisbane Stadium | Fiji v France | **France** | 98.0% |
| QF3 | 2027-10-31 | Brisbane Stadium | Argentina v Ireland | **Ireland** | 66.1% |
| QF4 | 2027-10-31 | Stadium Australia, Sydney | Australia v England | **England** | 67.4% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| SF1 | 2027-11-05 | Stadium Australia, Sydney | South Africa v France | **South Africa** | 55.3% |
| SF2 | 2027-11-06 | Stadium Australia, Sydney | Ireland v England | **Ireland** | 58.1% |

### Bronze final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| BF | 2027-11-12 | Stadium Australia, Sydney | France v England | **England** | 51.1% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| F | 2027-11-13 | Stadium Australia, Sydney | South Africa v Ireland | **South Africa** | 81.7% |

**Projected champion: South Africa** (overall title probability 29.0% — the single path above is only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite still loses about one such match in three.
- Rugby is more predictable than football (few draws, favourites hold more often), but 2027 is well out, so early forecasts are low-information and will sharpen as warm-up tests are played.
- `xPts` = expected pool points (incl. bonus points). Predictions refresh hourly: `python -m rugby.run all`.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
