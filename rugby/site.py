"""Static website generation: renders the markdown report as a styled
single-page site in outputs/site/ (deployable to any static host).

    python -m rugby.site        # rebuild outputs/site/index.html
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

OUT_DIR = Path(__file__).parent / "outputs"
SITE_DIR = OUT_DIR / "site"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rugby World Cup 2027 — ML Predictions</title>
<style>
  :root {{
    --bg: #0e1320; --card: #161e31; --text: #e8ecf5; --muted: #93a0b8;
    --accent: #4cc38a; --accent2: #f5c542; --line: #26314f;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--text);
    font: 16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      Helvetica, Arial, sans-serif;
  }}
  header.hero {{
    background: linear-gradient(135deg, #14532d 0%, #0b7d3e 100%);
    padding: 2.2rem 1rem 1.8rem; text-align: center;
  }}
  header.hero h1 {{ margin: 0 0 .4rem; font-size: 1.7rem; }}
  header.hero p {{ margin: .2rem 0; color: #d6f5e3; font-size: .95rem; }}
  main {{ max-width: 980px; margin: 0 auto; padding: 1rem; }}
  h2 {{
    margin-top: 2.2rem; padding-bottom: .35rem; font-size: 1.25rem;
    border-bottom: 2px solid var(--line); color: var(--accent2);
  }}
  h3 {{ margin-top: 1.4rem; font-size: 1.05rem; color: var(--accent); }}
  p, li {{ color: var(--text); }}
  em {{ color: var(--muted); }}
  a {{ color: #7cb8ff; }}
  table {{
    border-collapse: collapse; width: 100%; margin: .8rem 0 1.2rem;
    font-size: .88rem; background: var(--card); border-radius: 8px;
    overflow: hidden; display: block; overflow-x: auto; white-space: nowrap;
  }}
  thead th {{
    background: #1f2a44; color: #cdd7ea; text-align: left;
    padding: .5rem .65rem; position: sticky; top: 0;
  }}
  td {{ padding: .42rem .65rem; border-top: 1px solid var(--line); }}
  tbody tr:nth-child(odd) {{ background: rgba(255,255,255,.02); }}
  tbody tr:hover {{ background: rgba(76,195,138,.08); }}
  strong {{ color: var(--accent); }}
  footer {{
    margin: 3rem 0 1rem; text-align: center; color: var(--muted);
    font-size: .8rem; padding: 0 1rem;
  }}
</style>
</head>
<body>
<header class="hero">
  <h1>&#127945; Rugby World Cup 2027 — ML Predictions</h1>
  <p>Machine-learned probabilities for every match, pool and the road to the final</p>
  <p>Last checked {updated} UTC — refreshes hourly; predictions move when new results arrive</p>
</header>
<main>
{body}
</main>
<footer>
  Rugby points model (World Rugby ranking + Elo strength) and Monte Carlo
  tournament simulation. Probabilities, not promises — refreshed after each
  test window.
</footer>
</body>
</html>
"""


def _inline(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def _md_to_html(lines: list[str]) -> str:
    """Render the small markdown subset the report uses — headings, GitHub
    tables, emphasis, bullet lists — and pass raw HTML/SVG blocks through
    verbatim. Self-contained so the site builds with no third-party deps."""
    out: list[str] = []
    i, n = 0, len(lines)
    while i < n:
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1
            continue
        if s.startswith("<"):                              # raw HTML / SVG
            out.append(ln)
            i += 1
            continue
        if s.startswith("### "):
            out.append(f"<h3>{_inline(s[4:])}</h3>")
            i += 1
            continue
        if s.startswith("## "):
            out.append(f"<h2>{_inline(s[3:])}</h2>")
            i += 1
            continue
        if s.startswith("# "):
            i += 1
            continue
        if s.startswith("|"):                              # table block
            block = []
            while i < n and lines[i].strip().startswith("|"):
                block.append(lines[i].strip())
                i += 1
            out.append(_table(block))
            continue
        if s.startswith("- "):                             # bullet list
            out.append("<ul>")
            while i < n and lines[i].strip().startswith("- "):
                out.append(f"<li>{_inline(lines[i].strip()[2:])}</li>")
                i += 1
            out.append("</ul>")
            continue
        out.append(f"<p>{_inline(s)}</p>")
        i += 1
    return "\n".join(out)


def _cells(row: str) -> list[str]:
    return [c.strip() for c in row.strip().strip("|").split("|")]


def _table(block: list[str]) -> str:
    if len(block) < 2:
        return ""
    head = _cells(block[0])
    rows = [_cells(r) for r in block[2:]]            # block[1] is the separator
    html = ["<table><thead><tr>"]
    html += [f"<th>{_inline(c)}</th>" for c in head]
    html.append("</tr></thead><tbody>")
    for r in rows:
        html.append("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>")
    html.append("</tbody></table>")
    return "".join(html)


def build_site() -> Path:
    md_text = (OUT_DIR / "report.md").read_text()
    lines = md_text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    body = _md_to_html(lines)
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    html = TEMPLATE.format(
        updated=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        body=body)
    out = SITE_DIR / "index.html"
    out.write_text(html)
    for csv in ("match_probabilities.csv", "tournament_projections.csv",
                "upcoming_predictions.csv", "history.csv"):
        src = OUT_DIR / csv
        if src.exists():
            (SITE_DIR / csv).write_bytes(src.read_bytes())
    return out


if __name__ == "__main__":
    print(f"Wrote {build_site()}")
