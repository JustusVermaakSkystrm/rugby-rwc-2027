#!/usr/bin/env python3
"""Second mechanical pass over Sandra's deck (v3).

Alignment drift, two stray hyphens, a trailing space, and heading
capitalisation. No wording or content decisions: the slide 5 title, the empty
lower thirds on slides 4 and 7, and list punctuation style are left alone.

Usage: clean_deck2.py <in.pptx> <out.pptx>
"""
import re
import sys

from pptx import Presentation
from pptx.util import Inches

EMU = 914400.0
CHANGES = []


def log(slide, kind, detail):
    CHANGES.append((slide, kind, detail))


def para_text(p):
    return "".join(r.text for r in p.runs)


def replace_in(prs, n, before, after, desc):
    hit = False
    for sh in prs.slides[n - 1].shapes:
        if not sh.has_text_frame:
            continue
        for p in sh.text_frame.paragraphs:
            cur = para_text(p)
            if before in cur:
                # rewrite only the run that carries the fragment, so a
                # two-tone paragraph keeps both of its colours
                for r in p.runs:
                    if before in r.text:
                        r.text = r.text.replace(before, after)
                        hit = True
                        break
                else:
                    p.runs[0].text = cur.replace(before, after)
                    for extra in p.runs[1:]:
                        extra.text = ""
                    hit = True
    log(n, "Text" if hit else "NOT FOUND", desc)


def strip_trailing(prs):
    n_fixed = 0
    for n, s in enumerate(prs.slides, 1):
        frames = [sh.text_frame for sh in s.shapes if sh.has_text_frame]
        if s.has_notes_slide:
            frames.append(s.notes_slide.notes_text_frame)
        for tf in frames:
            for p in tf.paragraphs:
                if not p.runs:
                    continue
                last = p.runs[-1]
                stripped = re.sub(r"[ \t]+$", "", last.text)
                if stripped != last.text:
                    last.text = stripped
                    n_fixed += 1
    log(0, "Text", f"{n_fixed} trailing space(s) removed from the ends of lines")


def move(sh, x=None, y=None, w=None, h=None):
    if x is not None: sh.left = Inches(x)
    if y is not None: sh.top = Inches(y)
    if w is not None: sh.width = Inches(w)
    if h is not None: sh.height = Inches(h)


def geom(sh):
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    try:
        return sh._element.spPr.find(ns + "prstGeom").get("prst")
    except Exception:
        return None


def by_text(slide, needle):
    for sh in slide.shapes:
        if sh.has_text_frame and needle in sh.text_frame.text:
            return sh
    return None


def fix_slide3(prs):
    s = prs.slides[2]

    # kicker sat 0.017in right and 0.05in high of every other slide's kicker
    move(by_text(s, "· INVESTIGATE") or by_text(s, "INVESTIGATE"), x=0.60, y=0.42)
    log(3, "Layout", "kicker moved to x 0.60 / y 0.42, matching every other slide "
                     "(was x 0.617 / y 0.370)")

    # the italic intro block hung 0.05in left of the title
    move(by_text(s, "Is it real"), x=0.60)
    log(3, "Layout", "intro block moved to x 0.60 so it lines up with the title "
                     "(was 0.547, hanging left of it)")

    # even gutters: three 3.81in cards across 0.60–12.73 leaves 0.35in each
    cards = sorted([sh for sh in s.shapes if geom(sh) == "roundRect"],
                   key=lambda sh: sh.left)
    badges = sorted([sh for sh in s.shapes if geom(sh) == "ellipse"],
                    key=lambda sh: sh.left)
    nums = sorted([sh for sh in s.shapes if sh.has_text_frame
                   and sh.text_frame.text.strip() in ("01", "02", "03")],
                  key=lambda sh: sh.left)
    heads = [by_text(s, t) for t in ("Volume", "Price", "Mix")]
    bodies, looks = [], []
    for cx_old in [sh.left / EMU for sh in cards]:
        blocks = sorted([sh for sh in s.shapes if sh.has_text_frame
                         and abs(sh.left / EMU - (cx_old + 0.35)) < 0.25
                         and sh.top / EMU > 3.4],
                        key=lambda sh: sh.top)
        bodies.append(blocks[0])
        looks.append(blocks[1])

    for i, cx in enumerate((0.60, 4.76, 8.92)):
        move(cards[i], x=cx, y=3.06, w=3.81, h=3.19)
        move(badges[i], x=cx + 0.22, y=3.12, w=0.46, h=0.46)
        move(nums[i], x=cx + 0.22, y=3.12, w=0.46, h=0.46)
        move(heads[i], x=cx + 0.86, y=3.17, w=2.70, h=0.36)
        move(bodies[i], x=cx + 0.35, y=3.70, w=3.11, h=0.95)
        move(looks[i], x=cx + 0.35, y=4.78, w=3.11, h=1.10)
    log(3, "Layout", "card gutters evened to 0.35in (were 0.43 and 0.35); the "
                     "number badges now sit inside the cards instead of straddling "
                     "the top edge")


def fix_slide4(prs):
    s = prs.slides[3]
    badges = sorted([sh for sh in s.shapes if geom(sh) == "ellipse"],
                    key=lambda sh: sh.left)
    keys = ("Realistic plan for the year", "Use run rate as a cost guide",
            "Sign-off with the operations")
    for badge, key in zip(badges, keys):
        move(by_text(s, key), x=badge.left / EMU + 0.04, y=3.764, w=3.71)
    log(4, "Layout", "the three body blocks put on one baseline and given the same "
                     "0.04in offset from their badges (were at x 0.640 / 4.761 / "
                     "8.982 and two different heights)")


def fix_slide7(prs):
    s = prs.slides[6]
    line = by_text(s, "Weekly look at exceptions")
    if line and abs(line.left / EMU - 0.60) > 0.005:
        move(line, x=0.60)
        log(7, "Layout", "closing line moved to x 0.60, matching the heading and "
                         "standfirst above it (was 0.62)")


def main(src, dst):
    prs = Presentation(src)

    # --- text ---
    replace_in(prs, 5, "opportunities - escalate early",
               "opportunities – escalate early",
               "hyphen → en dash in the slide title, matching the rest of the deck")
    replace_in(prs, 5, "Variance to budget - causal",
               "Variance to budget – causal",
               "hyphen → en dash")
    replace_in(prs, 4, "Operational Buy In", "Operational buy-in",
               "sentence case and hyphen, to match 'Agree the plan' and "
               "'Cost the work honestly'")
    replace_in(prs, 3, "walk through jobs with operational team",
               "walk through jobs with the operational team",
               "missing article")
    strip_trailing(prs)

    # --- layout ---
    fix_slide3(prs)
    fix_slide4(prs)
    fix_slide7(prs)

    prs.save(dst)

    print(f"{'SLIDE':<7}{'TYPE':<11}CHANGE")
    for n, kind, detail in CHANGES:
        print(f"{(str(n) if n else 'all'):<7}{kind:<11}{detail}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
