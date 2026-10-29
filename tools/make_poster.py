#!/usr/bin/env python3
"""Owner-repository poster for mikey-7x / POWERED BY [mikey:hexoid-sys].

A2 portrait, 2481 x 3508 px at 150 dpi. The page is carried by the emblem wall:
twenty relief marks of the tools, drivers, runtimes, silicon and libraries the
work is built on, drawn by tools/emblem3d.py from tools/emblems.py.

POWERED BY [mikey:hexoid-sys] - Copyright (c) 2026 mikey-7x. All rights reserved.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from PIL import Image, ImageDraw  # noqa: E402

import emblem3d as E  # noqa: E402
import emblems as EM  # noqa: E402
import poster_kit as K  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
W, H = 2481, 3508
M = 120
CW = W - 2 * M
BRAND = "POWERED BY [mikey:hexoid-sys]"


def tile(w, h, emblem, label, sub, accent, index=""):
    t = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(t)
    # a hairline plate, nothing more
    d.rectangle([0, 0, w - 1, h - 1], outline=(34, 38, 44, 255), width=1)
    d.line([(0, 0), (w * 0.30, 0)], fill=accent + (110,), width=2)
    if index:
        d.text((12, 8), index, font=K.font(K.MONO, 17), fill=(96, 103, 110, 255))

    ew = int(h * 0.70)
    em = emblem.resize((ew, ew), Image.LANCZOS)
    t.alpha_composite(em, (int((w - ew) / 2), int(h * 0.02)))

    f = K.font(K.BOLD, 27)
    while d.textlength(label, font=f) > w * 0.90 and f.size > 14:
        f = K.font(K.BOLD, f.size - 1)
    d.text((w / 2, h * 0.775), label, font=f, fill=(236, 239, 243, 255), anchor="ma")
    fs = K.font(K.MONO, 19)
    d.text((w / 2, h * 0.862), sub, font=fs, fill=(150, 157, 165, 255), anchor="ma")
    return t


def build(target=OUT / "introduction-poster.png"):
    img = K.page(W, H)

    # ------------------------------------------------------------- header ---
    K.brand_bar(img, OUT / "mikey-hexoid-sys-mark.png", M, 96, CW, brand=BRAND,
                left_note="the engineering identity of this owner repository",
                right_a="OWNER REPOSITORY", right_b="github.com/mikey-7x")
    K.rule(img, M, 244, W - M, 244, K.RULE, 2)

    K.silver_text(img, (M - 6, 268), "MIKEY-7X", K.font(K.BOLD, 190))
    K.text(img, (M + 4, 484), "Architect  ·  software developer  ·  hardware developer",
           K.font(K.SANS, 44), K.SILVER, spacing=0.5)
    K.text(img, (M + 4, 552),
           "Vulkan capabilities on Android phones — graphics and compute drivers, the runtimes "
           "above them, and the compatibility layers", K.font(K.SANS, 29), K.GREY)
    K.text(img, (M + 4, 590),
           "that carry Windows and Linux applications onto a phone.",
           K.font(K.SANS, 29), K.GREY)

    K.rule(img, M, 660, W - M, 660, K.RULE, 1)
    K.text(img, (M, 682), "20 COMPONENTS  ·  SILICON TO APPLICATION", K.font(K.MONOB, 21),
           K.SILVER, spacing=2.6)
    K.text(img, (W - M, 684),
           "Snapdragon 8 Gen 3  ·  Adreno 750  ·  Hexagon NPU  ·  Vulkan on Turnip",
           K.font(K.MONO, 21), K.DIM, anchor="ra")

    # --------------------------------------------------------- emblem wall --
    entries = EM.EMBLEMS
    cols = 4
    rows = (len(entries) + cols - 1) // cols
    gap = 20
    tw = (CW - gap * (cols - 1)) // cols
    top, bottom = 738, 2912
    th = (bottom - top - gap * (rows - 1)) // rows

    for i, entry in enumerate(entries):
        key, label, sub, accent = entry[0], entry[1], entry[2], entry[3]
        emblem = EM.emblem_image(int(th * 0.62), entry, depth=0.08)
        r, c = divmod(i, cols)
        x = M + c * (tw + gap)
        y = top + r * (th + gap)
        img.alpha_composite(tile(tw, th, emblem, label, sub, accent, f"{i + 1:02d}"), (x, y))

    # ------------------------------------------------------- brand statement --
    K.rule(img, M, 2950, W - M, 2950, K.RULE, 2)
    d = ImageDraw.Draw(img)

    mark = OUT / "powered-by-mikey-hexoid-sys.png"
    if mark.is_file():
        mk = Image.open(mark).convert("RGBA")
        mh = 150
        mk = mk.resize((int(mk.width * mh / mk.height), mh), Image.LANCZOS)
        img.alpha_composite(mk, (M, 2980))

    bx = M + 300
    K.text(img, (bx, 2970), BRAND, K.font(K.MONOB, 30), K.SILVER, spacing=1.4)
    K.text(img, (bx, 3008),
           "The mark of the advanced builds: long research, analysis and learning, then testing\n"
           "and verification. Carried by three projects. Every repository here is my own work —",
           K.font(K.SANS, 22), K.GREY)
    K.text(img, (bx, 3068),
           "the rest are published as utilities, studies and archives, without the mark.",
           K.font(K.SANS, 22), K.GREY)
    K.text(img, (bx, 3112), "mikey:hexoid v5.0.0", K.font(K.MONOB, 21), K.INK)
    K.text(img, (bx, 3144), "298.666 MHz frequency counter", K.font(K.MONOB, 21), K.INK)
    K.text(img, (bx + 590, 3112), "Project Synapse v1", K.font(K.MONOB, 21), K.INK)
    K.text(img, (bx + 590, 3144), "three projects — the advanced builds",
           K.font(K.MONO, 19), K.DIM)

    # ------------------------------------------------------------- footer --
    K.footer(img, M, 3210, CW,
             contacts=[("EMAIL", "chauhanyogesh9825@gmail.com"),
                       ("GITHUB", "github.com/mikey-7x"),
                       ("YOUTUBE", "youtube.com/@mikey-7x"),
                       ("BLOG", "rtod-yv8.blogspot.com/?m=1"),
                       ("LINKEDIN", "linkedin.com/in/yogesh-r-chauhan-780005417")],
             licence_lines=["Personal and educational use with attribution.",
                            "Commercial, industrial and clinical use require a",
                            "separate written licence. Statements describe active",
                            "work, not benchmark results or certifications.",
                            "Emblems are original symbols, not vendor artwork."],
             brand=BRAND,
             copyright_lines=["Copyright © 2026 mikey-7x.", "All rights reserved.",
                              "Created by mikey-7x"])

    img = img.convert("RGB")
    img.save(target, optimize=True)
    img.save(target.with_suffix(".pdf"), resolution=150.0)
    print("poster:", target.stat().st_size, "bytes", img.size)
    return img


if __name__ == "__main__":
    build()
