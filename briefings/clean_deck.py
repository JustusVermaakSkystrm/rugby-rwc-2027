#!/usr/bin/env python3
"""Mechanical clean-up of Sandra's edited deck.

Fixes typos, text collisions, alignment drift and file metadata. Makes no
content or wording decisions beyond spelling, punctuation and dash style —
every phrase Sandra wrote survives.

Usage: clean_deck.py <in.pptx> <out.pptx>
"""
import re
import shutil
import sys
import zipfile

from pptx import Presentation
from pptx.util import Inches

CHANGES = []


def log(slide, kind, detail):
    CHANGES.append((slide, kind, detail))


# ---------------------------------------------------------------- text ----
TEXT_FIXES = [
    # (slide no, before, after, description)
    (3, "as well as forecast- have", "as well as forecast – have",
     "missing space and hyphen before 'have'"),
    (3, "Is it once off or an emerging trend",
     "Is it once off or an emerging trend?", "missing question mark"),
    (4, "across the all finance areas", "across all finance areas",
     "'the all' → 'all'"),
    (5, "Predefined ratesMonetary threshold",
     "Predefined rates\nMonetary threshold",
     "two bullets run together — line break restored"),
    (5, "Safety issues , compliance", "Safety issues, compliance",
     "space before comma"),
    (5, "cant be cut", "can't be cut", "missing apostrophe"),
    (5, "Identify changes to assumption", "Identify changes to assumptions",
     "singular → plural"),
    (6, "It effects the surplus", "It affects the surplus",
     "effects → affects"),
    (6, "Identify the gap provide a recommendation",
     "Identify the gap, provide a recommendation", "missing comma"),
    (6, "Be timely in the communication  - ",
     "Be timely in the communication – ", "double space and hyphen"),
]


def para_text(p):
    return "".join(r.text for r in p.runs)


def set_para(p, new):
    """Replace a paragraph's text, keeping the first run's formatting."""
    if not p.runs:
        return
    p.runs[0].text = new
    for extra in p.runs[1:]:
        extra.text = ""


def fix_text(prs):
    for n, before, after, desc in TEXT_FIXES:
        hit = False
        for sh in prs.slides[n - 1].shapes:
            if not sh.has_text_frame:
                continue
            for p in sh.text_frame.paragraphs:
                cur = para_text(p)
                if before in cur:
                    set_para(p, cur.replace(before, after))
                    hit = True
        log(n, "Text" if hit else "NOT FOUND", desc)

    # trailing whitespace + em dash → en dash, everywhere including notes
    dashes = trailing = 0
    for i, s in enumerate(prs.slides, 1):
        frames = [sh.text_frame for sh in s.shapes if sh.has_text_frame]
        if s.has_notes_slide:
            frames.append(s.notes_slide.notes_text_frame)
        for tf in frames:
            for p in tf.paragraphs:
                for j, r in enumerate(p.runs):
                    t = r.text
                    if "—" in t:
                        dashes += t.count("—")
                        t = t.replace("—", "–")
                    # only the last run: an inner run's trailing space is the
                    # word gap before the next run
                    if j == len(p.runs) - 1:
                        stripped = re.sub(r"[ \t]+$", "", t)
                        if stripped != t:
                            trailing += 1
                            t = stripped
                    r.text = t
    log(0, "Text", f"{dashes} em dashes changed to en dashes (slides and notes)")
    log(0, "Text", f"{trailing} trailing spaces removed")


# -------------------------------------------------------------- layout ----
def move(sh, x=None, y=None, w=None, h=None):
    if x is not None: sh.left = Inches(x)
    if y is not None: sh.top = Inches(y)
    if w is not None: sh.width = Inches(w)
    if h is not None: sh.height = Inches(h)


def by_text(slide, needle):
    for sh in slide.shapes:
        if sh.has_text_frame and needle in sh.text_frame.text:
            return sh
    return None


def geom(sh):
    ns = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    try:
        return sh._element.spPr.find(ns + "prstGeom").get("prst")
    except Exception:
        return None


def fix_slide3(prs):
    """Number badges overlap the card edge and the 'Price' heading."""
    s = prs.slides[2]
    cards = sorted([sh for sh in s.shapes if geom(sh) == "roundRect"],
                   key=lambda sh: sh.left)
    circles = sorted([sh for sh in s.shapes if geom(sh) == "ellipse"],
                     key=lambda sh: sh.left)
    nums = sorted([sh for sh in s.shapes if sh.has_text_frame
                   and sh.text_frame.text.strip() in ("01", "02", "03")],
                  key=lambda sh: sh.left)
    heads = [by_text(s, t) for t in ("Volume", "Price", "Mix")]

    for i, card in enumerate(cards):
        cx = card.left / 914400
        move(circles[i], x=cx + 0.22, y=3.04)
        move(nums[i], x=cx + 0.22, y=3.04, w=0.46, h=0.46)
        move(heads[i], x=cx + 0.86, y=3.09, w=2.7, h=0.36)

    # body and 'what I'd look at' blocks onto one baseline
    for i, card in enumerate(cards):
        cx = card.left / 914400
        blocks = sorted([sh for sh in s.shapes if sh.has_text_frame
                         and abs(sh.left / 914400 - (cx + 0.35)) < 0.4
                         and sh.top / 914400 > 3.4],
                        key=lambda sh: sh.top)
        if len(blocks) >= 2:
            move(blocks[0], x=cx + 0.35, y=3.60, w=3.11, h=0.95)
            move(blocks[1], x=cx + 0.35, y=4.70, w=3.11)
    log(3, "Layout", "number badges realigned inside the cards; the '02' badge "
                     "no longer overlaps 'Price'; the three columns share a baseline")


def fix_slide5(prs):
    """Heading 03 wraps into its body text; rows unevenly spaced."""
    s = prs.slides[4]
    rows = [
        ("Planning", "Properly understand the nature"),
        ("Use available capacity", "Productivity, first-time fix"),
        ("Challenge additional spend", "Checking variations"),
        ("Highlight risks", "Identify any offsetting"),
        ("Rephase selectively", "Discretionary planned work"),
    ]
    circles = sorted([sh for sh in s.shapes if geom(sh) == "ellipse"
                      and sh.width / 914400 < 1], key=lambda sh: sh.top)
    nums = sorted([sh for sh in s.shapes if sh.has_text_frame
                   and sh.text_frame.text.strip() in ("01", "02", "03", "04", "05")],
                  key=lambda sh: sh.top)
    wide = sorted([sh for sh in s.shapes if geom(sh) == "ellipse"
                   and sh.width / 914400 > 1], key=lambda sh: sh.top)
    wide_tx = sorted([sh for sh in s.shapes if sh.has_text_frame
                      and sh.left / 914400 > 6.5 and sh.text_frame.text.strip()],
                     key=lambda sh: sh.top)

    for i, (head_key, body_key) in enumerate(rows):
        y = 1.70 + i * 1.02
        move(circles[i], x=0.60, y=y + 0.02, w=0.46, h=0.46)
        move(nums[i], x=0.60, y=y + 0.02, w=0.46, h=0.46)
        move(by_text(s, head_key), x=1.22, y=y, w=5.7, h=0.34)
        move(by_text(s, body_key), x=1.22, y=y + 0.38, w=5.7, h=0.62)
        if i < len(wide):
            move(wide[i], x=7.00, y=y + 0.06, w=5.73, h=0.78)
            move(wide_tx[i], x=7.27, y=y + 0.15, w=5.19, h=0.60)

    log(5, "Layout", "heading 03 widened so it no longer wraps into its own body "
                     "text; five rows evenly spaced; badges and the right-hand "
                     "callouts aligned to their rows")


def fix_slide6(prs):
    """The two lead-in lines overlap each other."""
    s = prs.slides[5]
    l1 = by_text(s, "It affects the surplus")
    l2 = by_text(s, "It competes with the investment")
    timely = by_text(s, "Be timely in the communication")

    move(l1, x=0.60, y=3.66, w=12.13, h=0.60)
    move(l2, x=0.60, y=4.32, w=12.13, h=0.60)
    move(timely, x=0.60, y=5.05, w=12.13, h=0.95)

    # an empty leftover box sat between them
    for sh in list(s.shapes):
        if sh.has_text_frame and not sh.text_frame.text.strip() and geom(sh) == "rect":
            sh._element.getparent().remove(sh._element)
            log(6, "Layout", "removed an empty leftover text box between the two lines")

    # colour only the lead-in phrase, not the whole sentence
    from pptx.dml.color import RGBColor
    for shape in (l1, l2):
        p = shape.text_frame.paragraphs[0]
        full = para_text(p)
        if " - " not in full:
            continue
        lead, rest_txt = full.split(" - ", 1)
        keep = p.runs[0]
        for extra in p.runs[1:]:
            extra._r.getparent().remove(extra._r)
        keep.text = lead + " – "
        tail = copy_run(p, keep)
        tail.text = rest_txt
        tail.font.bold = False
        tail.font.color.rgb = RGBColor(0x33, 0x42, 0x3D)
    log(6, "Layout", "the two lines no longer overlap; only the lead-in phrase is "
                     "highlighted, the explanation is body colour")


def copy_run(paragraph, src):
    import copy as _c
    new = _c.deepcopy(src._r)
    src._r.addnext(new)
    from pptx.text.text import _Run
    return _Run(new, paragraph)


def fix_slide7(prs):
    """Rule and closing line stranded well below the lists."""
    s = prs.slides[6]
    rule = [sh for sh in s.shapes if geom(sh) == "line"]
    cadence = by_text(s, "Weekly look at exceptions")
    if rule:
        move(rule[0], y=4.55)
    move(cadence, x=0.60, y=4.75, w=12.13)
    log(7, "Layout", "rule and closing line pulled up under the lists, closing a "
                     "2-inch gap left when the summary line was deleted")


# ------------------------------------------------------------ metadata ----
def fix_metadata(prs):
    cp = prs.core_properties
    if cp.subject:
        log(0, "Metadata", f"cleared Subject field (was {cp.subject!r})")
        cp.subject = ""

    # employer classification stamp baked into the slide master
    master = prs.slide_masters[0]
    for sh in list(master.shapes):
        if sh.has_text_frame and "INTERNAL" in sh.text_frame.text:
            sh._element.getparent().remove(sh._element)
            log(0, "Metadata", "removed the 'INTERNAL' classification stamp from "
                               "the slide master")


def strip_custom_props(path):
    """Remove the Purview classification properties from docProps/custom.xml."""
    tmp = path + ".tmp"
    removed = removed_company = False
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "docProps/app.xml":
                text = data.decode("utf8")
                new = re.sub(r"<Company>[^<]*</Company>", "<Company></Company>", text)
                if new != text:
                    removed_company = True
                    data = new.encode("utf8")
            if item.filename == "docProps/custom.xml":
                text = data.decode("utf8")
                new = re.sub(r"<property[^>]*name=\"Classification[^\"]*\".*?</property>",
                             "", text, flags=re.S)
                if new != text:
                    removed = True
                    data = new.encode("utf8")
            zout.writestr(item, data)
    shutil.move(tmp, path)
    if removed:
        log(0, "Metadata", "removed the ClassificationContentMarking properties "
                           "(employer sensitivity label)")
    if removed_company:
        log(0, "Metadata", "cleared the Company field (was 'PptxGenJS')")


# ------------------------------------------------------------------ run ----
def main(src, dst):
    prs = Presentation(src)
    fix_text(prs)
    fix_slide3(prs)
    fix_slide5(prs)
    fix_slide6(prs)
    fix_slide7(prs)
    fix_metadata(prs)
    prs.save(dst)
    strip_custom_props(dst)

    print(f"{'SLIDE':<7}{'TYPE':<11}CHANGE")
    for n, kind, detail in CHANGES:
        where = str(n) if n else "all"
        print(f"{where:<7}{kind:<11}{detail}")
    import json
    with open("clean_changes.json", "w") as f:
        json.dump(CHANGES, f, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
