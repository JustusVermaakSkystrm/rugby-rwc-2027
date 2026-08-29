# Rugby World Cup 2027 — ML Prediction Report

*Generated 2026-08-29 · data through **2026-08-22** · 50,000 Monte Carlo simulations · 0/36 pool matches played*

Probabilities come from a **margin + total Gaussian model** (World Rugby ranking + Elo strength, points attack/defence, rolling form, venue/importance) trained on 1,922 internationals, simulated through the official RWC 2027 bracket with bonus-point pool standings and tiebreakers.

*Rolling validation (974 matches): chosen model **margin_total** — RPS 0.1574 vs ranking-only baseline 0.1570; margin MAE 12.66 pts vs 12.57.*

## Following South Africa — upcoming fixtures

Every scheduled South Africa international, with kick-off in your timezones, the model's call, and where to watch.

| Date | Kick-off | Opponent | Competition | Venue | Model call | Where to watch |
|------|----------|----------|-------------|-------|-----------|----------------|
| Sat 29 Aug 2026 | 16:10 UK · 17:10 SAST | New Zealand (H) | International Test Match | DHL Stadium | **53.1%** win · 25–23 | SuperSport (SA)? |
| Sat 05 Sep 2026 | 16:10 UK · 17:10 SAST | New Zealand (H) | International Test Match | FNB Stadium | **53.1%** win · 25–23 | SuperSport (SA)? |
| Sat 12 Sep 2026 | 22:00 UK · 23:00 SAST | New Zealand (N) | International Test Match | M&T Bank Stadium | **48.4%** win · 23–23 | SuperSport (SA)? |
| Sun 27 Sep 2026 | 10:45 UK · 11:45 SAST | Australia (A) | International Test Match | Optus Stadium | **70.8%** win · 33–23 | SuperSport (SA)? |
| Sat 07 Nov 2026 | 11:40 UK · 13:40 SAST | Italy (A) | Nations Championship | Allianz Stadium | **95.2%** win · 42–14 | ITV (UK) · SuperSport (SA) |
| Fri 13 Nov 2026 | 20:10 UK · 22:10 SAST | France (A) | Nations Championship | Stade de France | **61.5%** win · 30–25 | ITV (UK) · SuperSport (SA) |
| Sat 21 Nov 2026 | 16:40 UK · 18:40 SAST | Ireland (A) | Nations Championship | Aviva Stadium | **54.8%** win · 29–26 | ITV (UK) · SuperSport (SA) |

*Kick-off times are converted from the official UTC start time. Broadcast listings are curated (ESPN publishes none for internationals), as of 2026-07-02 — a "?" marks rights we could not confirm for this cycle, so check local listings.*

## Title favourites

| # | Team | Pool | Champion | Δ vs 2026-08-22 | Final | Semi | Quarter | Rd of 16 |
|---|------|:----:|---------:|-------:|------:|----:|--------:|---------:|
| 1 | South Africa | B | **27.3%** | – | 38.1% | 55.8% | 97.8% | 100.0% |
| 2 | New Zealand | A | **25.7%** | – | 38.0% | 55.5% | 98.0% | 100.0% |
| 3 | France | E | **15.4%** | – | 25.9% | 64.5% | 69.4% | 100.0% |
| 4 | Ireland | D | **12.6%** | – | 33.1% | 61.9% | 77.3% | 100.0% |
| 5 | England | F | **10.7%** | – | 31.7% | 58.0% | 91.9% | 100.0% |
| 6 | Scotland | D | **3.4%** | – | 12.5% | 36.7% | 48.5% | 99.8% |
| 7 | Australia | A | **2.8%** | – | 10.7% | 30.3% | 91.4% | 99.8% |
| 8 | Argentina | C | **2.1%** | – | 9.3% | 29.2% | 89.3% | 100.0% |
| 9 | Wales | F | **0.0%** | – | 0.3% | 2.5% | 51.8% | 96.1% |
| 10 | Italy | B | **0.0%** | – | 0.2% | 2.0% | 11.8% | 97.1% |
| 11 | Fiji | C | **0.0%** | – | 0.0% | 1.7% | 37.2% | 96.7% |
| 12 | Georgia | B | **0.0%** | – | 0.0% | 0.6% | 4.4% | 74.3% |

## Path to the final

The model's single most likely knockout bracket — every projected tie from the Round of 16 down to the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1196 568" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,100 C94,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M238,100 C238,138 166,138 166,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,100 C382,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M526,100 C526,138 454,138 454,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M670,100 C670,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M814,100 C814,138 742,138 742,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M958,100 C958,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,100 C1102,138 1030,138 1030,176" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M166,222 C166,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M454,222 C454,260 310,260 310,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,222 C742,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1030,222 C1030,260 886,260 886,298" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M310,344 C310,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M886,344 C886,382 598,382 598,420" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M598,466 C598,485 598,485 598,504" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="12" y="77" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 77)" text-anchor="middle">ROUND OF 16</text><text x="12" y="199" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 199)" text-anchor="middle">QUARTER-FINALS</text><text x="12" y="321" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 321)" text-anchor="middle">SEMI-FINALS</text><text x="12" y="443" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 12 443)" text-anchor="middle">FINAL</text><rect x="28" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="28" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="37" y="72" font-size="11" font-weight="700" fill="#7ef0b6">N. Zealand</text><text x="151" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="37" y="93" font-size="11" font-weight="400" fill="#7c89a3">Spain</text><text x="151" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="172" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="172" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="181" y="72" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="295" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">99%</text><text x="181" y="93" font-size="11" font-weight="400" fill="#7c89a3">Tonga</text><text x="295" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">1%</text><rect x="316" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="325" y="72" font-size="11" font-weight="400" fill="#7c89a3">Fiji</text><text x="439" y="72" font-size="9.5" text-anchor="end" fill="#5d6880">44%</text><rect x="316" y="78" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="325" y="93" font-size="11" font-weight="700" fill="#7ef0b6">Wales</text><text x="439" y="93" font-size="9.5" text-anchor="end" fill="#cfe8d8">56%</text><rect x="460" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="460" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="469" y="72" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="583" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">76%</text><text x="469" y="93" font-size="11" font-weight="400" fill="#7c89a3">Scotland</text><text x="583" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">24%</text><rect x="604" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="604" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="613" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Argentina</text><text x="727" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">93%</text><text x="613" y="93" font-size="11" font-weight="400" fill="#7c89a3">Chile</text><text x="727" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">7%</text><rect x="748" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="748" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="757" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="871" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">98%</text><text x="757" y="93" font-size="11" font-weight="400" fill="#7c89a3">Georgia</text><text x="871" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">2%</text><rect x="892" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="892" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="901" y="72" font-size="11" font-weight="700" fill="#7ef0b6">Australia</text><text x="1015" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">94%</text><text x="901" y="93" font-size="11" font-weight="400" fill="#7c89a3">Japan</text><text x="1015" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">6%</text><rect x="1036" y="54" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1036" y="56" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1045" y="72" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1159" y="72" font-size="9.5" text-anchor="end" fill="#cfe8d8">92%</text><text x="1045" y="93" font-size="11" font-weight="400" fill="#7c89a3">Italy</text><text x="1159" y="93" font-size="9.5" text-anchor="end" fill="#5d6880">8%</text><rect x="100" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="109" y="194" font-size="11" font-weight="400" fill="#7c89a3">N. Zealand</text><text x="223" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">49%</text><rect x="100" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="223" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">51%</text><rect x="388" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="397" y="194" font-size="11" font-weight="400" fill="#7c89a3">Wales</text><text x="511" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">2%</text><rect x="388" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="397" y="215" font-size="11" font-weight="700" fill="#7ef0b6">France</text><text x="511" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">98%</text><rect x="676" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="685" y="194" font-size="11" font-weight="400" fill="#7c89a3">Argentina</text><text x="799" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">27%</text><rect x="676" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="685" y="215" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="799" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">73%</text><rect x="964" y="176" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="973" y="194" font-size="11" font-weight="400" fill="#7c89a3">Australia</text><text x="1087" y="194" font-size="9.5" text-anchor="end" fill="#5d6880">25%</text><rect x="964" y="200" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="973" y="215" font-size="11" font-weight="700" fill="#7ef0b6">England</text><text x="1087" y="215" font-size="9.5" text-anchor="end" fill="#cfe8d8">75%</text><rect x="244" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="244" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="253" y="316" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="367" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">62%</text><text x="253" y="337" font-size="11" font-weight="400" fill="#7c89a3">France</text><text x="367" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">38%</text><rect x="820" y="298" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="820" y="300" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="829" y="316" font-size="11" font-weight="700" fill="#7ef0b6">Ireland</text><text x="943" y="316" font-size="9.5" text-anchor="end" fill="#cfe8d8">62%</text><text x="829" y="337" font-size="11" font-weight="400" fill="#7c89a3">England</text><text x="943" y="337" font-size="9.5" text-anchor="end" fill="#5d6880">38%</text><rect x="532" y="420" width="132" height="46" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="532" y="422" width="132" height="21" rx="4" fill="#4cc38a" opacity="0.16"/><text x="541" y="438" font-size="11" font-weight="700" fill="#7ef0b6">S. Africa</text><text x="655" y="438" font-size="9.5" text-anchor="end" fill="#cfe8d8">76%</text><text x="541" y="459" font-size="11" font-weight="400" fill="#7c89a3">Ireland</text><text x="655" y="459" font-size="9.5" text-anchor="end" fill="#5d6880">24%</text><rect x="498" y="504" width="200" height="46" rx="10" fill="#f5c542"/><text x="598" y="525" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 S. Africa</text><text x="598" y="541" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 27% to win</text></svg>
</div>

## Upcoming internationals — match predictions

Every scheduled men's international on the calendar, not just RWC fixtures — the same model rates any pairing. Probabilities are for the listed home side; the predicted scoreline is the model's mean.

| Date | Competition | Match | Home win | Draw | Away win | Predicted | Favourite |
|------|-------------|-------|---------:|-----:|---------:|:---------:|----------|
| 2026-08-29 | International Test Match | South Africa v New Zealand | **53.1%** | 2.4% | 44.5% | 24.9–23.1 | South Africa (53.1%) |
| 2026-08-29 | International Test Match | Argentina v Australia | **59.0%** | 2.3% | 38.7% | 31.3–27.0 | Argentina (59.0%) |
| 2026-09-05 | International Test Match | Japan v Canada | **95.6%** | 0.5% | 3.9% | 45.4–16.7 | Japan (95.6%) |
| 2026-09-05 | International Test Match | South Africa v New Zealand | **53.1%** | 2.4% | 44.5% | 24.9–23.1 | South Africa (53.1%) |
| 2026-09-05 | International Test Match | Argentina v Australia | **59.0%** | 2.3% | 38.7% | 31.3–27.0 | Argentina (59.0%) |
| 2026-09-12 | International Test Match | South Africa v New Zealand (N) | 48.4% | 2.4% | **49.2%** | 23.2–23.4 | New Zealand (49.2%) |
| 2026-09-27 | International Test Match | Australia v South Africa | 27.2% | 2.0% | **70.8%** | 23.1–32.6 | South Africa (70.8%) |
| 2026-10-10 | International Test Match | New Zealand v Australia | **85.2%** | 1.4% | 13.5% | 35.1–17.3 | New Zealand (85.2%) |
| 2026-10-17 | International Test Match | Australia v New Zealand | 25.1% | 2.0% | **72.9%** | 22.3–32.9 | New Zealand (72.9%) |
| 2026-10-24 | International Test Match | Japan v Fiji | **56.8%** | 2.4% | 40.8% | 27.3–24.0 | Japan (56.8%) |
| 2026-10-31 | International Test Match | Belgium v Hong Kong China | 39.7% | 2.3% | **58.0%** | 23.0–26.9 | Hong Kong China (58.0%) |
| 2026-11-06 | Nations Championship | Ireland v Argentina | **72.6%** | 2.0% | 25.5% | 33.9–23.5 | Ireland (72.6%) |
| 2026-11-07 | Nations Championship | France v Fiji | **96.9%** | 0.4% | 2.7% | 46.8–15.5 | France (96.9%) |
| 2026-11-07 | Nations Championship | Wales v Japan | **58.7%** | 2.3% | 39.0% | 28.1–24.0 | Wales (58.7%) |
| 2026-11-07 | Nations Championship | Italy v South Africa | 4.2% | 0.6% | **95.2%** | 14.0–42.1 | South Africa (95.2%) |
| 2026-11-07 | Nations Championship | Scotland v New Zealand | 20.7% | 1.8% | **77.5%** | 20.2–33.2 | New Zealand (77.5%) |
| 2026-11-08 | Nations Championship | England v Australia | **76.8%** | 1.8% | 21.4% | 34.5–21.9 | England (76.8%) |
| 2026-11-13 | Nations Championship | France v South Africa | 36.2% | 2.3% | **61.5%** | 25.1–30.4 | South Africa (61.5%) |
| 2026-11-14 | Nations Championship | Italy v Argentina | 16.5% | 1.6% | **81.9%** | 20.8–36.4 | Argentina (81.9%) |
| 2026-11-14 | Nations Championship | Wales v New Zealand | 4.2% | 0.6% | **95.2%** | 15.7–43.9 | New Zealand (95.2%) |
| 2026-11-14 | Nations Championship | England v Japan | **95.0%** | 0.6% | 4.5% | 40.4–12.8 | England (95.0%) |
| 2026-11-14 | Nations Championship | Ireland v Fiji | **95.2%** | 0.6% | 4.2% | 45.0–16.9 | Ireland (95.2%) |
| 2026-11-14 | International Test Match | Paraguay v Brazil | **60.4%** | 2.3% | 37.3% | 29.6–24.8 | Paraguay (60.4%) |
| 2026-11-15 | Nations Championship | Scotland v Australia | **56.4%** | 2.4% | 41.2% | 31.0–27.9 | Scotland (56.4%) |
| 2026-11-21 | Nations Championship | France v Argentina | **79.5%** | 1.7% | 18.8% | 37.1–22.9 | France (79.5%) |

*30 scheduled fixture(s) on file; full list with exact probabilities in `upcoming_predictions.csv`. "(N)" = neutral venue.*

## Pool projections

### Pool A

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| New Zealand | 13.36 | 74.9% | 99.9% | 100.0% |
| Australia | 10.81 | 25.0% | 96.5% | 99.8% |
| Chile | 3.46 | 0.1% | 3.1% | 33.1% |
| Hong Kong China | 2.35 | 0.0% | 0.6% | 16.2% |

### Pool B

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| South Africa | 14.57 | 98.4% | 100.0% | 100.0% |
| Italy | 8.46 | 1.3% | 77.0% | 97.1% |
| Georgia | 5.60 | 0.3% | 22.1% | 74.3% |
| Romania | 1.17 | 0.0% | 0.9% | 6.2% |

### Pool C

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Argentina | 13.32 | 82.3% | 98.2% | 100.0% |
| Fiji | 9.04 | 14.9% | 73.3% | 96.7% |
| Spain | 6.27 | 2.8% | 27.6% | 82.8% |
| Canada | 1.09 | 0.0% | 0.9% | 5.3% |

### Pool D

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| Ireland | 12.89 | 64.1% | 99.7% | 100.0% |
| Scotland | 11.35 | 35.9% | 98.0% | 99.8% |
| Portugal | 3.07 | 0.0% | 1.0% | 24.7% |
| Uruguay | 2.56 | 0.0% | 1.3% | 20.0% |

### Pool E

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| France | 14.43 | 98.1% | 100.0% | 100.0% |
| Japan | 6.52 | 1.5% | 52.3% | 77.3% |
| Samoa | 5.26 | 0.3% | 31.8% | 61.5% |
| United States | 3.55 | 0.1% | 15.9% | 35.6% |

### Pool F

| Team | xPts | Win pool | Top 2 | Advance* |
|------|-----:|---------:|------:|--------:|
| England | 14.09 | 92.6% | 99.9% | 100.0% |
| Wales | 8.84 | 7.2% | 83.6% | 96.1% |
| Tonga | 4.80 | 0.2% | 12.5% | 59.4% |
| Zimbabwe | 1.96 | 0.0% | 4.0% | 14.4% |

*\*Advance = top two of the pool or one of the four best third-placed teams.*

## Most likely knockout bracket

Each tie shows the projected pairing and the named side's chance of advancing in that pairing.

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| R16-1 | 2027-10-23 | Sydney Football Stadium | Fiji v Wales | **Wales** | 56.4% |
| R16-2 | 2027-10-23 | Brisbane Stadium | New Zealand v Spain | **New Zealand** | 99.0% |
| R16-3 | 2027-10-23 | Docklands Stadium, Melbourne | France v Scotland | **France** | 75.8% |
| R16-4 | 2027-10-24 | Perth Stadium | South Africa v Tonga | **South Africa** | 99.0% |
| R16-5 | 2027-10-24 | Sydney Football Stadium | Argentina v Chile | **Argentina** | 93.1% |
| R16-6 | 2027-10-24 | Docklands Stadium, Melbourne | Ireland v Georgia | **Ireland** | 98.4% |
| R16-7 | 2027-10-23 | Brisbane Stadium | Australia v Japan | **Australia** | 93.8% |
| R16-8 | 2027-10-24 | Perth Stadium | England v Italy | **England** | 92.5% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| QF1 | 2027-10-30 | Stadium Australia, Sydney | New Zealand v South Africa | **South Africa** | 50.7% |
| QF2 | 2027-10-30 | Brisbane Stadium | Wales v France | **France** | 97.5% |
| QF3 | 2027-10-31 | Brisbane Stadium | Argentina v Ireland | **Ireland** | 72.8% |
| QF4 | 2027-10-31 | Stadium Australia, Sydney | Australia v England | **England** | 74.5% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| SF1 | 2027-11-05 | Stadium Australia, Sydney | South Africa v France | **South Africa** | 62.3% |
| SF2 | 2027-11-06 | Stadium Australia, Sydney | Ireland v England | **Ireland** | 61.7% |

### Bronze final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| BF | 2027-11-12 | Stadium Australia, Sydney | France v England | **France** | 58.7% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob |
|:-----:|------|-------|-----|------------------|---------:|
| F | 2027-11-13 | Stadium Australia, Sydney | South Africa v Ireland | **South Africa** | 75.7% |

**Projected champion: South Africa** (overall title probability 27.3% — the single path above is only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite still loses about one such match in three.
- Rugby is more predictable than football (few draws, favourites hold more often), but 2027 is well out, so early forecasts are low-information and will sharpen as warm-up tests are played.
- `xPts` = expected pool points (incl. bonus points). Predictions refresh hourly: `python -m rugby.run all`.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
