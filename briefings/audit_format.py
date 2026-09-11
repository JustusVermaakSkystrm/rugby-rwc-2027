#!/usr/bin/env python3
"""Formatting audit for a .pptx: overflow, overlap, alignment and consistency.

Geometry checks use the file's own coordinates. Text-fit uses proxy fonts that
are WIDER than the real Calibri/Cambria, so a reported overflow may be a false
positive; a clean result is trustworthy.
"""
import sys
from collections import Counter, defaultdict

from PIL import ImageFont
from pptx import Presentation
from pptx.util import Emu

EMU = 914400.0
DPI = 96
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
_f = {}

SLIDE_W, SLIDE_H = 13.333, 7.5
MARGIN = 0.6
FOOTER_Y = 6.95


def font(serif, bold, pt):
    key = (serif, bold, round(pt))
    if key not in _f:
        path = (SERIF_B if bold else SERIF) if serif else (SANS_B if bold else SANS)
        _f[key] = ImageFont.truetype(path, max(6, int(pt * DPI / 72)))
    return _f[key]


def inches(v):
    return v / EMU


def run_style(p):
    if not p.runs:
        return 12, False, False
    r = p.runs[0]
    sz = r.font.size.pt if r.font.size else 12
    return sz, bool(r.font.bold), bool(r.font.name and "Cambria" in r.font.name)


def wrapped_lines(text, fnt, max_w_px):
    lines = 0
    for hard in text.split("\n"):
        if not hard.strip():
            lines += 1
            continue
        words, cur = hard.split(" "), ""
        for w in words:
            trial = (cur + " " + w).strip()
            if fnt.getlength(trial) <= max_w_px or not cur:
                cur = trial
            else:
                lines += 1
                cur = w
        lines += 1
    return lines


def boxes(slide):
    out = []
    for sh in slide.shapes:
        if sh.left is None or not sh.has_text_frame:
            continue
        if not sh.text_frame.text.strip():
            continue
        out.append(sh)
    return out


def audit(path):
    prs = Presentation(path)
    findings = defaultdict(list)

    for n, slide in enumerate(prs.slides, 1):
        shapes = boxes(slide)

        # ---- overflow: does the text need more height than the box has?
        for sh in shapes:
            tf = sh.text_frame
            w_px = (inches(sh.width) - 0.08) * DPI
            total = 0.0
            for p in tf.paragraphs:
                sz, bold, serif = run_style(p)
                txt = "".join(r.text for r in p.runs)
                if not txt:
                    total += sz * 1.25
                    continue
                total += wrapped_lines(txt, font(serif, bold, sz), w_px) * sz * 1.25
            need = total / 72.0
            have = inches(sh.height)
            if need > have + 0.06:
                findings[n].append(
                    f"OVERFLOW  needs {need:.2f}in, box is {have:.2f}in  "
                    f"– \"{tf.text.strip()[:58]}…\"")

            # ---- off-slide / into the footer
            if inches(sh.left) < MARGIN - 0.08:
                findings[n].append(
                    f"MARGIN    starts at {inches(sh.left):.2f}in, left margin is {MARGIN}in  "
                    f"– \"{tf.text.strip()[:44]}…\"")
            if inches(sh.left) + inches(sh.width) > SLIDE_W - MARGIN + 0.12:
                findings[n].append(
                    f"MARGIN    ends at {inches(sh.left)+inches(sh.width):.2f}in, right margin is "
                    f"{SLIDE_W-MARGIN:.2f}in  – \"{tf.text.strip()[:40]}…\"")
            bottom = inches(sh.top) + need
            if inches(sh.top) < FOOTER_Y and bottom > FOOTER_Y + 0.02 and inches(sh.top) > 1:
                findings[n].append(
                    f"FOOTER    text reaches {bottom:.2f}in, footer sits at {FOOTER_Y}in  "
                    f"– \"{tf.text.strip()[:44]}…\"")

        # ---- overlap between text blocks
        for i, a in enumerate(shapes):
            for b in shapes[i + 1:]:
                ax1, ay1 = inches(a.left), inches(a.top)
                ax2, ay2 = ax1 + inches(a.width), ay1 + inches(a.height)
                bx1, by1 = inches(b.left), inches(b.top)
                bx2, by2 = bx1 + inches(b.width), by1 + inches(b.height)
                ox = min(ax2, bx2) - max(ax1, bx1)
                oy = min(ay2, by2) - max(ay1, by1)
                if ox > 0.25 and oy > 0.10:
                    findings[n].append(
                        f"OVERLAP   {oy:.2f}in vertical overlap between "
                        f"\"{a.text_frame.text.strip()[:26]}…\" and "
                        f"\"{b.text_frame.text.strip()[:26]}…\"")

        # ---- left-edge alignment drift
        lefts = [round(inches(sh.left), 2) for sh in shapes]
        for val, cnt in Counter(lefts).items():
            for other in set(lefts):
                if 0.005 < abs(val - other) < 0.09 and val < other:
                    findings[n].append(
                        f"ALIGN     two left edges nearly but not exactly equal: "
                        f"{val:.2f}in and {other:.2f}in")

    # ---- deck-wide consistency
    sizes, fonts = Counter(), Counter()
    for slide in prs.slides:
        for sh in boxes(slide):
            for p in sh.text_frame.paragraphs:
                for r in p.runs:
                    if r.text.strip():
                        if r.font.size:
                            sizes[round(r.font.size.pt, 1)] += 1
                        if r.font.name:
                            fonts[r.font.name] += 1
    return findings, sizes, fonts, prs


def main(path):
    findings, sizes, fonts, prs = audit(path)
    total = sum(len(v) for v in findings.values())
    print(f"FORMATTING AUDIT — {path}")
    print(f"{len(prs.slides)} slides, {total} findings\n")
    for n in sorted(findings):
        seen = set()
        rows = [f for f in findings[n] if not (f in seen or seen.add(f))]
        print(f"  SLIDE {n}")
        for f in rows:
            print(f"    {f}")
        print()
    if not total:
        print("  no geometry problems found\n")
    print("FONTS   :", ", ".join(f"{k} ({v})" for k, v in fonts.most_common()))
    print("SIZES   :", ", ".join(f"{k}pt ({v})" for k, v in sorted(sizes.items(), reverse=True)))


if __name__ == "__main__":
    main(sys.argv[1])
