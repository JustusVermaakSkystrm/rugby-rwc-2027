# Rugby World Cup 2027 — ML Prediction Report

*Generated 2026-07-10 · data through **2026-07-04** · 50,000 Monte Carlo simulations · 0/36 pool matches played*

Probabilities come from a **margin + total Gaussian model** (World Rugby ranking + Elo strength, points attack/defence, rolling form, venue/importance) trained on 1,908 internationals, simulated through the official RWC 2027 bracket with bonus-point pool standings and tiebreakers.

*Rolling validation (974 matches): chosen model **margin_total** — RPS 0.1574 vs ranking-only baseline 0.1570; margin MAE 12.66 pts vs 12.57.*

## Following South Africa — upcoming fixtures

Every scheduled South Africa international, with kick-off in your timezones, the model's call, and where to watch.

| Date | Kick-off | Opponent | Competition | Venue | Model call | Where to watch |
|------|----------|----------|-------------|-------|-----------|----------------|
| Sat 11 Jul 2026 | 16:40 UK · 17:40 SAST | Scotland (H) | Nations Championship | Loftus Versfeld | **86.4%** win · 38–19 | ITV (UK) · SuperSport (SA) |
| Sat 18 Jul 2026 | 16:40 UK · 17:40 SAST | Wales (H) | Nations Championship | Hollywoodbets Kings Park | **97.2%** win · 43–12 | ITV (UK) · SuperSport (SA) |
| Sat 08 Aug 2026 | 20:00 UK · 21:00 SAST | Argentina (A) | International Test Match | Estadio José Amalfitani | **82.5%** win · 38–22 | SuperSport (SA)? |
| Sat 22 Aug 2026 | 16:00 UK · 17:00 SAST | New Zealand (H) | International Test Match | Ellis Park | **73.3%** win · 29–18 | SuperSport (SA)? |
| Sat 29 Aug 2026 | 16:00 UK · 17:00 SAST | New Zealand (H) | International Test Match | DHL Stadium | **73.3%** win · 29–18 | SuperSport (SA)? |
| Sat 05 Sep 2026 | 16:00 UK · 17:00 SAST | New Zealand (H) | International Test Match | FNB Stadium | **73.3%** win · 29–18 | SuperSport (SA)? |
| Sat 12 Sep 2026 | 22:00 UK · 23:00 SAST | New Zealand (N) | International Test Match | M&T Bank Stadium | **72.8%** win · 29–18 | SuperSport (SA)? |
| Sun 27 Sep 2026 | 10:45 UK · 11:45 SAST | Australia (A) | International Test Match | Optus Stadium | **74.7%** win · 34–23 | SuperSport (SA)? |
| Sat 07 Nov 2026 | 11:40 UK · 13:40 SAST | Italy (A) | Nations Championship | Allianz Stadium | **93.8%** win · 41–15 | ITV (UK) · SuperSport (SA) |
| Fri 13 Nov 2026 | 20:10 UK · 22:10 SAST | France (A) | Nations Championship | Stade de France | **61.8%** win · 30–24 | ITV (UK) · SuperSport (SA) |
| Sat 21 Nov 2026 | 16:40 UK · 18:40 SAST | Ireland (A) | Nations Championship | Aviva Stadium | **58.7%** win · 28–24 | ITV (UK) · SuperSport (SA) |

*Kick-off times are converted from the official UTC start time. Broadcast listings are curated (ESPN publishes none for internationals), as of 2026-07-02 — a "?" marks rights we could not confirm for this cycle, so check local listings.*

## Title favourites

| # | Team | Pool | Champion | Δ vs 2026-07-04 | Final | Semi | Quarter | Rd of 16 |
|---|------|:----:|---------:|-------:|------:|----:|--------:|---------:|
| 1 | South Africa | B | **35.5%** | – | 44.3% | 62.7% | 97.8% | 100.0% |
| 2 | New Zealand | A | **18.4%** | – | 34.1% | 55.7% | 96.2% | 100.0% |
| 3 | France | E | **15.2%** | – | 24.9% | 53.8% | 64.6% | 100.0% |
| 4 | Ireland | D | **11.9%** | – | 29.0% | 54.0% | 82.5% | 100.0% |
| 5 | Argentina | C | **6.7%** | – | 23.9% | 46.2% | 90.7% | 100.0% |
| 6 | Australia | A | **5.4%** | – | 16.7% | 41.5% | 86.7% | 99.8% |
| 7 | England | F | **3.6%** | – | 13.7% | 37.0% | 81.4% | 100.0% |
| 8 | Scotland | D | **3.0%** | – | 10.3% | 28.1% | 49.8% | 99.8% |
| 9 | Wales | F | **0.2%** | – | 1.4% | 8.4% | 56.4% | 98.5% |
| 10 | Fiji | C | **0.1%** | – | 0.6% | 5.3% | 41.7% | 98.5% |
| 11 | Italy | B | **0.0%** | – | 0.7% | 4.1% | 20.9% | 98.0% |
| 12 | Japan | E | **0.0%** | – | 0.2% | 1.6% | 8.8% | 80.1% |

## Path to the final

The model's single most likely knockout bracket — every projected tie from the Round of 16 down to the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1196 568" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,100 C94,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M238,100 C238,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,100 C382,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M526,100 C526,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M670,100 C670,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M814,100 C814,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M958,100 C958,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,100 C1102,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M166,222 C166,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M454,222 C454,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,222 C742,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1030,222 C1030,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M310,344 C310,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M886,344 C886,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M598,466 C598,485 598,485 598,504" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="12" y="77" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 77)" text-anchor="middle">ROUND OF 16</text><text x="12" y="199" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 199)" text-anchor="middle">QUARTER-FINALS</text><text x="12" y="321" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 321)" text-anchor="middle">SEMI-FINALS</text><text x="12" y="443" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 443)" text-anchor="middle">FINAL</text><rect x="28" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="28" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="37" y="72" font-size="11" font-weight="700" fill="#7ef0b6">N. Zealand</text><text x="151" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="37" y="93" font-size="11" font-weight="400" fill="#7c89a3">Spain</text><text x="151" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="172" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="172" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="181" y="72" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="295" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="181" y="93" font-size="11" font-weight="400" fill="#7c89a3">Tonga</text><text x="295" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="316" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="325" y="72" font-size="11" font-weight="400" fill="#7c89a3">Fiji</text><text x="439" y="72" font-size="9.5" text-anchor="end" fill="#5d6880">44%</text><rect x="316" y="78" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="325" y="93" font-size="11" font-weight="700" fill="#7ef0b6">Wales</text><text x="439" y="93" font-size="9.5" text-anchor="end" fill="#cfe8d8">56%</text><rect x="460" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="460" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="469" y="72" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="583" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">71%</text><text x="469" y="93" font-size="11" font-weight="400" fill="#7c89a3">Scotland</text><text x="583" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">29%</text><rect x="604" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="604" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="613" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="727" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">92%</text><text x="613" y="93" font-size="11" font-weight="400" fill="#7c89a3">Samoa</text><text x="727" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">8%</text><rect x="748" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="748" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="757" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="871" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="757" y="93" font-size="11" font-weight="400" fill="#7c89a3">Georgia</text><text x="871" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="892" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="892" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="901" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1015" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">88%</text><text x="901" y="93" font-size="11" font-weight="400" fill="#7c89a3">Japan</text><text x="1015" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">12%</text><rect x="1036" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1036" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1045" y="72" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1159" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">82%</text><text x="1045" y="93" font-size="11" font-weight="400" fill="#7c89a3">Italy</text><text x="1159" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">18%</text><rect x="100" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="109" y="194" font-size="11" font-weight="400" fill="#7c89a3">N. Zealand</text><text x="223" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">45%</text><rect x="100" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="223" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">55%</text><rect x="388" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="397" y="194" font-size="11" font-weight="400" fill="#7c89a3">Wales</text><text x="511" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">8%</text><rect x="388" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="397" y="215" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="511" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">92%</text><rect x="676" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="685" y="194" font-size="11" font-weight="400" fill="#7c89a3">Argentina</text><text x="799" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">46%</text><rect x="676" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="685" y="215" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="799" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">54%</text><rect x="964" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="964" y="178" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="973" y="194" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1087" y="194" font-size="9.5" text-anchor="end" fill="#cfe8d8">52%</text><text x="973" y="215" font-size="11" font-weight="400" fill="#7c89a3">England</text><text x="1087" y="215" font-size="9.5" text-anchor="end" fill="#5d6880">48%</text><rect x="244" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="244" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="253" y="316" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="367" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">58%</text><text x="253" y="337" font-size="11" font-weight="400" fill="#7c89a3">France</text><text x="367" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">42%</text><rect x="820" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="820" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="829" y="316" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="943" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">58%</text><text x="829" y="337" font-size="11" font-weight="400" fill="#7c89a3">Australia</text><text x="943" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">42%</text><rect x="532" y="420" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="532" y="422" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="541" y="438" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="655" y="438" font-size="9.5" text-anchor="end" fill="#cfe8d8">77%</text><text x="541" y="459" font-size="11" font-weight="400" fill="#7c89a3">Ireland</text><text x="655" y="459" font-size="9.5" text-anchor="end" fill="#5d6880">23%</text><rect x="498" y="504" width="200" height="46" rx="10" fill="#f5c542"/><text x="598" y="525" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 S. Africa</text><text x="598" y="541" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 35% to win</text></svg>
</div>

## Upcoming internationals — match predictions

Every scheduled men's international on the calendar, not just RWC fixtures — the same model rates any pairing. Probabilities are for the listed home side; the predicted scoreline is the model's mean.

| Date | Competition | Match | Home win | Draw | Away win | Predicted | Favourite |
|------|-------------|-------|---------:|-----:|---------:|:---------:|----------|
| 2026-07-11 | Nations Championship | New Zealand v Italy | **87.6%** | 1.2% | 11.2% | 36.2–16.7 | New Zealand (87.6%) |
| 2026-07-11 | Nations Championship | Australia v France | 21.3% | 1.8% | **76.9%** | 24.5–37.0 | France (76.9%) |
| 2026-07-11 | Nations Championship | Japan v Ireland | 7.6% | 0.9% | **91.5%** | 18.2–41.1 | Ireland (91.5%) |
| 2026-07-11 | Nations Championship | Fiji v England | 28.2% | 2.1% | **69.7%** | 23.9–32.8 | England (69.7%) |
| 2026-07-11 | Nations Championship | South Africa v Scotland | **86.4%** | 1.3% | 12.3% | 37.7–19.2 | South Africa (86.4%) |
| 2026-07-11 | Nations Championship | Argentina v Wales | **77.6%** | 1.8% | 20.6% | 31.7–18.7 | Argentina (77.6%) |
| 2026-07-18 | Nations Championship | Argentina v England | **57.7%** | 2.4% | 39.9% | 28.0–24.3 | Argentina (57.7%) |
| 2026-07-18 | Nations Championship | Fiji v Scotland | 29.1% | 2.1% | **68.8%** | 24.1–32.6 | Scotland (68.8%) |
| 2026-07-18 | Nations Championship | South Africa v Wales | **97.2%** | 0.4% | 2.4% | 43.4–11.6 | South Africa (97.2%) |
| 2026-07-18 | Nations Championship | Japan v France | 8.2% | 1.0% | **90.8%** | 19.5–41.8 | France (90.8%) |
| 2026-07-18 | Nations Championship | New Zealand v Ireland | **65.0%** | 2.2% | 32.8% | 28.3–21.5 | New Zealand (65.0%) |
| 2026-07-18 | Nations Championship | Australia v Italy | **84.5%** | 1.4% | 14.1% | 32.9–15.8 | Australia (84.5%) |
| 2026-08-08 | International Test Match | Japan v Australia | 48.7% | 2.4% | **48.9%** | 25.2–25.3 | Australia (48.9%) |
| 2026-08-08 | International Test Match | Argentina v South Africa | 16.0% | 1.5% | **82.5%** | 21.8–37.6 | South Africa (82.5%) |
| 2026-08-15 | International Test Match | Australia v Japan | **86.4%** | 1.3% | 12.3% | 35.7–17.2 | Australia (86.4%) |
| 2026-08-22 | International Test Match | South Africa v New Zealand | **73.3%** | 2.0% | 24.7% | 29.2–18.5 | South Africa (73.3%) |
| 2026-08-29 | International Test Match | South Africa v New Zealand | **73.3%** | 2.0% | 24.7% | 29.2–18.5 | South Africa (73.3%) |
| 2026-08-29 | International Test Match | Argentina v Australia | **70.1%** | 2.1% | 27.8% | 29.7–20.5 | Argentina (70.1%) |
| 2026-09-05 | International Test Match | South Africa v New Zealand | **73.3%** | 2.0% | 24.7% | 29.2–18.5 | South Africa (73.3%) |
| 2026-09-05 | International Test Match | Japan v Canada | **97.0%** | 0.4% | 2.6% | 45.6–14.3 | Japan (97.0%) |
| 2026-09-05 | International Test Match | Argentina v Australia | **70.1%** | 2.1% | 27.8% | 29.7–20.5 | Argentina (70.1%) |
| 2026-09-12 | International Test Match | South Africa v New Zealand (N) | **72.8%** | 2.0% | 25.2% | 28.8–18.4 | South Africa (72.8%) |
| 2026-09-27 | International Test Match | Australia v South Africa | 23.4% | 1.9% | **74.7%** | 22.9–34.2 | South Africa (74.7%) |
| 2026-10-10 | International Test Match | New Zealand v Australia | **78.2%** | 1.8% | 20.0% | 32.3–19.0 | New Zealand (78.2%) |
| 2026-10-17 | International Test Match | Australia v New Zealand | 33.9% | 2.3% | **63.9%** | 25.4–31.7 | New Zealand (63.9%) |

*43 scheduled fixture(s) on file; full list with exact probabilities in `upcoming_predictions.csv`. "(N)" = neutral venue.*

## Pool projections

### Pool A

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| New Zealand | 12.89 | 64.3% | 99.7% | 100.0% |
| Australia | 11.26 | 35.6% | 97.2% | 99.8% |
| Chile | 3.47 | 0.1% | 2.5% | 35.6% |
| Hong Kong China | 2.33 | 0.0% | 0.6% | 17.8% |

### Pool B

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| South Africa | 14.51 | 97.5% | 100.0% | 100.0% |
| Italy | 8.74 | 2.4% | 81.4% | 98.0% |
| Georgia | 5.34 | 0.1% | 17.9% | 70.4% |
| Romania | 1.15 | 0.0% | 0.7% | 6.3% |

### Pool C

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Argentina | 13.46 | 82.7% | 99.2% | 100.0% |
| Fiji | 9.42 | 16.1% | 80.2% | 98.5% |
| Spain | 5.41 | 1.1% | 19.9% | 70.2% |
| Canada | 1.52 | 0.0% | 0.8% | 9.4% |

### Pool D

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Ireland | 12.99 | 68.2% | 99.6% | 100.0% |
| Scotland | 11.11 | 31.7% | 97.7% | 99.8% |
| Uruguay | 2.89 | 0.0% | 1.5% | 25.7% |
| Portugal | 2.81 | 0.1% | 1.2% | 24.1% |

### Pool E

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| France | 14.29 | 96.6% | 99.9% | 100.0% |
| Japan | 6.82 | 3.0% | 55.2% | 80.1% |
| Samoa | 5.43 | 0.4% | 31.4% | 65.6% |
| United States | 3.33 | 0.1% | 13.5% | 32.6% |

### Pool F

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| England | 13.21 | 78.2% | 99.4% | 100.0% |
| Wales | 9.99 | 21.3% | 90.4% | 98.5% |
| Tonga | 4.09 | 0.4% | 7.7% | 48.5% |
| Zimbabwe | 2.28 | 0.0% | 2.5% | 19.2% |

*\*Advance = top two of the pool or one of the four best third-placed teams.*

## Most likely knockout bracket

Each tie shows the projected pairing and the named side's chance of advancing in that pairing.

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| R16-1 | 2027-10-23 | Sydney Football Stadium | Fiji v Wales | **Wales** | 56.1% |
| R16-2 | 2027-10-23 | Brisbane Stadium | New Zealand v Spain | **New Zealand** | 99.0% |
| R16-3 | 2027-10-23 | Docklands Stadium, Melbourne | France v Scotland | **France** | 71.4% |
| R16-4 | 2027-10-24 | Perth Stadium | South Africa v Tonga | **South Africa** | 99.0% |
| R16-5 | 2027-10-24 | Sydney Football Stadium | Argentina v Samoa | **Argentina** | 91.9% |
| R16-6 | 2027-10-24 | Docklands Stadium, Melbourne | Ireland v Georgia | **Ireland** | 98.7% |
| R16-7 | 2027-10-23 | Brisbane Stadium | Australia v Japan | **Australia** | 87.8% |
| R16-8 | 2027-10-24 | Perth Stadium | England v Italy | **England** | 81.6% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| QF1 | 2027-10-30 | Stadium Australia, Sydney | New Zealand v South Africa | **South Africa** | 54.6% |
| QF2 | 2027-10-30 | Brisbane Stadium | Wales v France | **France** | 92.1% |
| QF3 | 2027-10-31 | Brisbane Stadium | Argentina v Ireland | **Ireland** | 53.6% |
| QF4 | 2027-10-31 | Stadium Australia, Sydney | Australia v England | **Australia** | 51.8% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| SF1 | 2027-11-05 | Stadium Australia, Sydney | South Africa v France | **South Africa** | 57.7% |
| SF2 | 2027-11-06 | Stadium Australia, Sydney | Ireland v Australia | **Ireland** | 58.3% |

### Bronze final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| BF | 2027-11-12 | Stadium Australia, Sydney | France v Australia | **France** | 78.5% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| F | 2027-11-13 | Stadium Australia, Sydney | South Africa v Ireland | **South Africa** | 77.1% |

**Projected champion: South Africa** (overall title probability 35.5% — the single path above is only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite still loses about one such match in three.
- Rugby is more predictable than football (few draws, favourites hold more often), but 2027 is well out, so early forecasts are low-information and will sharpen as warm-up tests are played.
- `xPts` = expected pool points (incl. bonus points). Predictions refresh hourly: `python -m rugby.run all`.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
