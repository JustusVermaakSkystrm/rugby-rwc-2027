#!/usr/bin/env python3
"""Render a .pptx to PNGs from real shape geometry, for visual QA.

LibreOffice cannot load pptx in this sandbox, so this draws directly from the
file's own coordinates via python-pptx. Fonts are wider proxies than the real
Calibri/Cambria, so this render is CONSERVATIVE: if text fits here it fits in
PowerPoint. Reported overflow may be a false positive; reported fit is safe.
"""
import sys
from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Emu
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

EMU_IN = 914400.0
DPI = 110

SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"
SANS_BI = "/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

_cache = {}


def font(serif, bold, italic, pt):
    px = max(6, int(round(pt * DPI / 72.0)))
    if serif:
        path = SERIF_B if bold else SERIF
    else:
        if bold and italic:
            path = SANS_BI
        elif bold:
            path = SANS_B
        elif italic:
            path = SANS_I
        else:
            path = SANS
    key = (path, px)
    if key not in _cache:
        try:
            _cache[key] = ImageFont.truetype(path, px)
        except OSError:
            _cache[key] = ImageFont.load_default()
    return _cache[key]


def px(emu):
    return int(round(emu / EMU_IN * DPI))


def rgb(color_fmt, default=(0, 0, 0)):
    try:
        c = color_fmt.rgb
        return (c[0], c[1], c[2])
    except Exception:
        return default


def shape_fill(sh):
    try:
        f = sh.fill
        if f.type is not None and f.type == 1:  # solid
            return rgb(f.fore_color, None)
    except Exception:
        pass
    return None


def wrap(draw, text, fnt, maxw):
    """Greedy wrap; returns list of lines."""
    out = []
    for hard in text.split("\n"):
        if not hard:
            out.append("")
            continue
        words, line = hard.split(" "), ""
        for w in words:
            trial = (line + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= maxw or not line:
                line = trial
            else:
                out.append(line)
                line = w
        out.append(line)
    return out


def render(path, prefix):
    prs = Presentation(path)
    W, H = px(prs.slide_width), px(prs.slide_height)
    issues = []

    for idx, slide in enumerate(prs.slides, 1):
        bg = (255, 255, 255)
        try:
            if slide.background.fill.type == 1:
                bg = rgb(slide.background.fill.fore_color, (255, 255, 255))
        except Exception:
            pass
        img = Image.new("RGB", (W, H), bg)
        d = ImageDraw.Draw(img)

        for sh in slide.shapes:
            if sh.left is None:
                continue
            x, y = px(sh.left), px(sh.top)
            w, h = px(sh.width), px(sh.height)

            fill = shape_fill(sh)
            st = str(sh.shape_type)
            try:
                prst = sh._element.spPr.find('{http://schemas.openxmlformats.org/drawingml/2006/main}prstGeom').get('prst')
            except Exception:
                prst = ""
            st = st + " " + (prst or "").upper()
            if fill:
                if "ELLIPSE" in st:
                    d.ellipse([x, y, x + w, y + h], fill=fill)
                elif "ROUND" in st:
                    d.rounded_rectangle([x, y, x + w, y + h], radius=int(0.06 * DPI), fill=fill)
                else:
                    d.rectangle([x, y, x + w, y + h], fill=fill)
            if "LINE" in st and not fill:
                d.line([x, y, x + w, y + h], fill=(90, 140, 120), width=2)

            if not sh.has_text_frame:
                continue
            tf = sh.text_frame
            if not tf.text.strip():
                continue

            # collect paragraph lines
            pad = int(0.04 * DPI)
            box_w = w - 2 * pad
            lines = []
            for para in tf.paragraphs:
                runs = [r for r in para.runs]
                if not runs:
                    lines.append(("", None, 0))
                    continue
                r0 = runs[0]
                sz = r0.font.size.pt if r0.font.size else 12
                bold = bool(r0.font.bold)
                ital = bool(r0.font.italic)
                serif = bool(r0.font.name and "Cambria" in r0.font.name)
                col = rgb(r0.font.color, (30, 30, 30)) if r0.font.color and r0.font.color.type is not None else (30, 30, 30)
                fnt = font(serif, bold, ital, sz)
                txt = "".join(r.text for r in runs)
                bullet = txt and para.level == 0 and sh.name.startswith("__never__")
                for ln in wrap(d, txt, fnt, box_w):
                    lines.append((ln, fnt, col))

            lh = []
            for ln, fnt, col in lines:
                if fnt is None:
                    lh.append(int(10 * DPI / 72))
                else:
                    lh.append(int(fnt.size * 1.22))
            total = sum(lh)

            anchor = tf.vertical_anchor
            if anchor == MSO_ANCHOR.MIDDLE:
                cy = y + (h - total) // 2
            elif anchor == MSO_ANCHOR.BOTTOM:
                cy = y + h - total
            else:
                cy = y + pad

            align = tf.paragraphs[0].alignment
            for (ln, fnt, col), lhi in zip(lines, lh):
                if fnt is None:
                    cy += lhi
                    continue
                tw = d.textlength(ln, font=fnt)
                if align == PP_ALIGN.CENTER:
                    tx = x + (w - tw) / 2
                elif align == PP_ALIGN.RIGHT:
                    tx = x + w - pad - tw
                else:
                    tx = x + pad
                d.text((tx, cy), ln, font=fnt, fill=col)
                cy += lhi

            # overflow checks
            if total > h + 2:
                issues.append(f"slide {idx}: text taller than box by {total - h}px  [{tf.text[:45]!r}]")
            if cy > H:
                issues.append(f"slide {idx}: text past bottom of slide  [{tf.text[:45]!r}]")
            if x + w > W + 2 or x < -2:
                issues.append(f"slide {idx}: shape outside slide horizontally  [{sh.name}]")

        img.save(f"{prefix}-{idx}.png")

    print(f"rendered {len(prs.slides)} slides -> {prefix}-N.png")
    if issues:
        print("\nPOTENTIAL ISSUES (conservative — proxy fonts are wider than real):")
        for i in issues:
            print("  -", i)
    else:
        print("no geometry/overflow issues detected")


if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "slide")
