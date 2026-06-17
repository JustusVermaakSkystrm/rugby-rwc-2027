"""SVG 'path to the final' bracket — the projected knockout tree drawn
top-down, from the Round of 16 converging to the champion at the bottom.

Pure string generation (no deps); embedded as inline SVG in the report and
site. Driven by report.predicted_bracket() output.
"""

from __future__ import annotations

from html import escape

# Left-to-right order at each level so connector lines never cross, derived
# from bracket.json:
#   QF1=R16-2/R16-4  QF2=R16-1/R16-3  QF3=R16-5/R16-6  QF4=R16-7/R16-8
#   SF1=QF1/QF2      SF2=QF3/QF4      Final=SF1/SF2
R16_ORDER = ["R16-2", "R16-4", "R16-1", "R16-3", "R16-5", "R16-6", "R16-7", "R16-8"]
QF_ORDER = ["QF1", "QF2", "QF3", "QF4"]
SF_ORDER = ["SF1", "SF2"]

LEVELS = [
    ("round_of_16", R16_ORDER, "ROUND OF 16"),
    ("quarterfinals", QF_ORDER, "QUARTER-FINALS"),
    ("semifinals", SF_ORDER, "SEMI-FINALS"),
    ("final", ["F"], "FINAL"),
]

MARGIN, BOX_W, BOX_H, GAPX, ROW_GAP = 28, 132, 46, 12, 122
TOP_Y = 54

SHORT = {
    "South Africa": "S. Africa", "New Zealand": "N. Zealand",
    "United States": "USA", "Hong Kong China": "Hong Kong",
}


def _short(name: str) -> str:
    return SHORT.get(name, name)


def _pct(x: float) -> str:
    return f"{100 * x:.0f}%"


def _centers() -> dict:
    n = len(R16_ORDER)
    r16 = [MARGIN + BOX_W / 2 + i * (BOX_W + GAPX) for i in range(n)]
    levels = {"round_of_16": r16}
    prev = r16
    for key in ("quarterfinals", "semifinals"):
        cur = [(prev[2 * k] + prev[2 * k + 1]) / 2 for k in range(len(prev) // 2)]
        levels[key] = cur
        prev = cur
    levels["final"] = [(prev[0] + prev[1]) / 2]
    return levels


def _row_y(level_idx: int) -> int:
    return TOP_Y + level_idx * ROW_GAP


def _box(cx: float, y: int, tie: dict) -> str:
    x = cx - BOX_W / 2
    home, away, winner = tie["home"], tie["away"], tie["winner"]
    p_home = tie["p_home_advance"]
    rows = [(home, p_home, winner == home), (away, 1 - p_home, winner == away)]
    parts = [
        f'<rect x="{x:.0f}" y="{y}" width="{BOX_W}" height="{BOX_H}" rx="6" '
        f'fill="#161e31" stroke="#26314f" stroke-width="1"/>'
    ]
    for r, (team, p, win) in enumerate(rows):
        ty = y + 18 + r * 21
        if win:
            parts.append(
                f'<rect x="{x:.0f}" y="{y + 2 + r * 22:.0f}" width="{BOX_W}" '
                f'height="21" rx="4" fill="#4cc38a" opacity="0.16"/>')
        fill = "#7ef0b6" if win else "#7c89a3"
        weight = "700" if win else "400"
        parts.append(
            f'<text x="{x + 9:.0f}" y="{ty}" font-size="11" font-weight="{weight}" '
            f'fill="{fill}">{escape(_short(team))}</text>')
        parts.append(
            f'<text x="{x + BOX_W - 9:.0f}" y="{ty}" font-size="9.5" '
            f'text-anchor="end" fill="{"#cfe8d8" if win else "#5d6880"}">'
            f'{_pct(p)}</text>')
    return "".join(parts)


def _conn(x1: float, y1: float, x2: float, y2: float) -> str:
    my = (y1 + y2) / 2
    return (f'<path d="M{x1:.0f},{y1:.0f} C{x1:.0f},{my:.0f} {x2:.0f},{my:.0f} '
            f'{x2:.0f},{y2:.0f}" fill="none" stroke="#33436b" stroke-width="1.5"/>')


def bracket_svg(bracket_path: dict, champion: str, champ_prob: float) -> str:
    c = _centers()
    by_match = {t["match"]: t for key, _, _ in LEVELS for t in bracket_path[key]}
    width = MARGIN * 2 + len(R16_ORDER) * BOX_W + (len(R16_ORDER) - 1) * GAPX
    champ_y = _row_y(len(LEVELS)) - (ROW_GAP - BOX_H) // 2
    height = champ_y + 64

    s = [f'<svg viewBox="0 0 {width} {height}" width="100%" '
         f'preserveAspectRatio="xMidYMin meet" '
         f'xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,'
         'BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif">']

    keys = [k for k, _, _ in LEVELS]
    for li in range(len(keys) - 1):
        upper, lower = c[keys[li]], c[keys[li + 1]]
        y_from, y_to = _row_y(li) + BOX_H, _row_y(li + 1)
        for k in range(len(lower)):
            for j in (2 * k, 2 * k + 1):
                s.append(_conn(upper[j], y_from, lower[k], y_to))
    s.append(_conn(c["final"][0], _row_y(len(LEVELS) - 1) + BOX_H,
                   c["final"][0], champ_y))

    for li, (_, _, label) in enumerate(LEVELS):
        ly = _row_y(li) + BOX_H / 2
        s.append(f'<text x="12" y="{ly:.0f}" font-size="9" font-weight="700" '
                 f'fill="#5d6880" transform="rotate(-90 12 {ly:.0f})" '
                 f'text-anchor="middle">{label}</text>')

    for li, (key, order, _) in enumerate(LEVELS):
        for j, mno in enumerate(order):
            if mno in by_match:
                s.append(_box(c[key][j], _row_y(li), by_match[mno]))

    cw, cx = 200, c["final"][0]
    s.append(
        f'<rect x="{cx - cw / 2:.0f}" y="{champ_y}" width="{cw}" height="46" '
        f'rx="10" fill="#f5c542"/>'
        f'<text x="{cx:.0f}" y="{champ_y + 21}" font-size="13" font-weight="800" '
        f'fill="#1a1300" text-anchor="middle">\U0001F3C6 '
        f'{escape(_short(champion))}</text>'
        f'<text x="{cx:.0f}" y="{champ_y + 37}" font-size="10" fill="#5a4a00" '
        f'text-anchor="middle">projected champion · {_pct(champ_prob)} to win</text>')

    s.append("</svg>")
    return "".join(s)
