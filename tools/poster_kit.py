#!/usr/bin/env python3
"""poster_kit — the shared design system for the mikey:hexoid-sys poster set.

Monochrome silver on matte black, a strict grid, hairline rules and monospaced
technical annotations. No decorative pictograms: every mark on a page is either
type, a rule, or a measured line drawing.

POWERED BY [mikey:hexoid-sys] - Copyright (c) 2026 mikey-7x. All rights reserved.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ------------------------------------------------------------------ palette --
PAPER = (9, 10, 12)
INK = (238, 240, 243)
SILVER = (196, 202, 210)
GREY = (140, 147, 155)
DIM = (98, 105, 112)
FAINT = (58, 63, 70)
RULE = (36, 40, 46)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONOB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIFB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

_FONTS: dict = {}


def font(path, size):
    key = (path, max(6, int(round(size))))
    if key not in _FONTS:
        _FONTS[key] = ImageFont.truetype(path, key[1])
    return _FONTS[key]


# ------------------------------------------------------------------ canvas ---
def page(width, height, top=(13, 14, 16), bottom=(6, 7, 8)):
    img = Image.new("RGB", (width, height), PAPER)
    gradient = np.zeros((height, width, 3), np.float32)
    ramp = np.linspace(0.0, 1.0, height, dtype=np.float32)[:, None]
    for i in range(3):
        gradient[..., i] = top[i] + (bottom[i] - top[i]) * ramp
    img.paste(Image.fromarray(gradient.astype(np.uint8), "RGB"), (0, 0))
    return img.convert("RGBA")


def rule(img, x1, y1, x2, y2, colour=RULE, width=2):
    ImageDraw.Draw(img).line([(x1, y1), (x2, y2)], fill=colour + (255,), width=width)
    return img


def text(img, xy, s, f, fill=INK, anchor="la", spacing=0, opacity=255):
    """Draw text, optionally with extra tracking between characters."""
    d = ImageDraw.Draw(img)
    if not spacing:
        d.text(xy, s, font=f, fill=fill + (opacity,), anchor=anchor)
        return img
    total = sum(d.textlength(ch, font=f) + spacing for ch in s) - spacing
    x, y = xy
    if anchor[0] == "r":
        x -= total
    elif anchor[0] == "m":
        x -= total / 2
    for ch in s:
        d.text((x, y), ch, font=f, fill=fill + (opacity,), anchor="l" + anchor[1])
        x += d.textlength(ch, font=f) + spacing
    return img


def tracked_length(img, s, f, spacing):
    d = ImageDraw.Draw(img)
    return sum(d.textlength(ch, font=f) + spacing for ch in s) - spacing


def silver_text(img, xy, s, f, anchor="la", top=(247, 249, 251), bottom=(138, 146, 155)):
    """Large display type filled with a vertical silver gradient."""
    d = ImageDraw.Draw(img)
    bbox = d.textbbox((0, 0), s, font=f)
    w, h = bbox[2] - bbox[0] + 8, bbox[3] - bbox[1] + 8
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).text((4 - bbox[0], 4 - bbox[1]), s, font=f, fill=255)
    grad = np.zeros((h, w, 3), np.float32)
    ramp = np.linspace(0.0, 1.0, h, dtype=np.float32)[:, None]
    for i in range(3):
        grad[..., i] = top[i] + (bottom[i] - top[i]) * ramp
    plate = Image.fromarray(grad.astype(np.uint8), "RGB").convert("RGBA")
    plate.putalpha(mask)
    x, y = xy
    if anchor[0] == "r":
        x -= w - 8
    elif anchor[0] == "m":
        x -= (w - 8) / 2
    img.alpha_composite(plate, (int(x - 4), int(y - 4)))
    return img


# ------------------------------------------------------------- page pieces ---
def brand_bar(img, mark_path, x, y, width, brand="POWERED BY [mikey:hexoid-sys]",
              left_note="", right_a="", right_b=""):
    """The brand lock-up: mark, brand line, and the repository identification."""
    if Path(mark_path).is_file():
        mk = Image.open(mark_path).convert("RGBA")
        mh = 116
        mk = mk.resize((int(mk.width * mh / mk.height), mh), Image.LANCZOS)
        img.alpha_composite(mk, (x, y))
        tx = x + mk.width + 34
    else:
        tx = x
    text(img, (tx, y + 10), brand, font(MONOB, 27), SILVER, spacing=1.2)
    if left_note:
        text(img, (tx, y + 54), left_note, font(MONO, 19), DIM)
    if right_a:
        text(img, (x + width, y + 10), right_a, font(MONO, 19), DIM, anchor="ra")
    if right_b:
        text(img, (x + width, y + 42), right_b, font(MONO, 22), GREY, anchor="ra")
    return img


def section(img, x, y, width, number, title, note=""):
    d = ImageDraw.Draw(img)
    d.line([(x, y), (x + width, y)], fill=RULE + (255,), width=2)
    text(img, (x, y + 22), number, font(MONO, 20), DIM)
    text(img, (x + 66, y + 20), title, font(BOLD, 27), INK, spacing=3.4)
    if note:
        text(img, (x + width, y + 24), note, font(MONO, 19), DIM, anchor="ra")
    return img


def meta_row(img, x, y, width, cells, size=21, colour=INK, label_colour=DIM,
             label_size=16, gap=28):
    """A single row of label / value pairs spread across a width."""
    d = ImageDraw.Draw(img)
    colw = (width - gap * (len(cells) - 1)) / len(cells)
    for i, (label, value) in enumerate(cells):
        cx = x + i * (colw + gap)
        text(img, (cx, y), label, font(MONO, label_size), label_colour, spacing=1.6)
        text(img, (cx, y + label_size + 12), value, font(MONO, size), colour)
    return img


def band_diagram(img, x, y, width, rows, band_height=74, gap=12, label_w=430,
                 note_colour=DIM):
    """A stack diagram drawn as thin outlined bands — a technical figure."""
    d = ImageDraw.Draw(img)
    top = y
    for i, (label, note, emphasis) in enumerate(rows):
        by = top + i * (band_height + gap)
        stroke = SILVER if emphasis else FAINT
        d.rectangle([x, by, x + width, by + band_height], outline=stroke + (255,), width=2)
        if emphasis:
            d.rectangle([x, by, x + 8, by + band_height], fill=SILVER + (255,))
        text(img, (x + 34, by + band_height / 2 - 14), label, font(MONOB, 24),
             INK if emphasis else SILVER, spacing=2.6)
        if note:
            text(img, (x + width - 26, by + band_height / 2 - 12), note,
                 font(MONO, 20), note_colour, anchor="ra")
        # connector arrow to the band below
        if i < len(rows) - 1:
            cx = x + label_w / 2
            cy1 = by + band_height + 2
            cy2 = by + band_height + gap - 2
            d.line([(cx, cy1), (cx, cy2)], fill=FAINT + (255,), width=2)
    # side bracket
    bx = x - 34
    height_total = len(rows) * band_height + (len(rows) - 1) * gap
    d.line([(bx, top), (bx, top + height_total)], fill=FAINT + (255,), width=2)
    for yy in (top, top + height_total):
        d.line([(bx, yy), (bx + 14, yy)], fill=FAINT + (255,), width=2)
    return img, top + height_total


def footer(img, x, y, width, contacts, licence_lines, brand, copyright_lines):
    d = ImageDraw.Draw(img)
    d.line([(x, y), (x + width, y)], fill=RULE + (255,), width=2)
    text(img, (x, y + 26), "CONTACT", font(MONO, 17), DIM, spacing=2.4)
    yy = y + 56
    for label, value in contacts:
        text(img, (x, yy), label, font(MONO, 18), DIM)
        text(img, (x + 150, yy), value, font(MONO, 20), SILVER)
        yy += 34
    lx = x + 900
    text(img, (lx, y + 26), "LICENCE", font(MONO, 17), DIM, spacing=2.4)
    yy = y + 56
    for line in licence_lines:
        text(img, (lx, yy), line, font(SANS, 20), GREY)
        yy += 30
    text(img, (x + width, y + 26), brand, font(MONOB, 21), SILVER, anchor="ra")
    yy = y + 58
    for line in copyright_lines:
        text(img, (x + width, yy), line, font(MONO, 18), DIM, anchor="ra")
        yy += 28
    return img
