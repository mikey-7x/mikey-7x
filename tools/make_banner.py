#!/usr/bin/env python3
"""Profile banner for mikey-7x (1600 x 400), deterministic.

Same design language as the poster: matte black, silver type, hairline rules,
the official brand mark on the right.

POWERED BY [mikey:hexoid-sys] - Copyright (c) 2026 mikey-7x. All rights reserved.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from PIL import Image, ImageDraw  # noqa: E402

import poster_kit as K  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1600, 400

img = K.page(W, H, top=(16, 17, 19), bottom=(6, 7, 8))

d = ImageDraw.Draw(img)
# frame
d.rectangle([0, 0, W - 1, H - 1], outline=(30, 33, 38, 255), width=2)
K.rule(img, 63, 74, 1537, 74, K.RULE, 1)

K.text(img, (64, 40), "POWERED BY [mikey:hexoid-sys]", K.font(K.MONOB, 20), K.SILVER,
       spacing=1.4)
K.text(img, (1537, 42), "OWNER REPOSITORY", K.font(K.MONO, 17), K.DIM, anchor="ra",
       spacing=1.8)

K.silver_text(img, (60, 100), "mikey-7x", K.font(K.BOLD, 118))
K.rule(img, 64, 268, 560, 268, (70, 76, 84), 2)
K.text(img, (64, 284), "Vulkan capabilities on Android phones", K.font(K.SANS, 30), K.SILVER)
K.text(img, (64, 328),
       "graphics & compute drivers  ·  runtimes  ·  compatibility layers",
       K.font(K.MONO, 19), K.GREY)
K.text(img, (64, 358), "github.com/mikey-7x", K.font(K.MONO, 17), K.DIM)

# official mark, right side, with a hairline separator
mark = OUT / "mikey-hexoid-sys-mark.png"
K.rule(img, 1035, 108, 1035, 358, K.RULE, 1)
if mark.is_file():
    mk = Image.open(mark).convert("RGBA")
    mh = 210
    mk = mk.resize((int(mk.width * mh / mk.height), mh), Image.LANCZOS)
    img.alpha_composite(mk, (1537 - mk.width, 128))
K.text(img, (1537, 352), "mikey:hexoid-sys", K.font(K.MONOB, 20), K.SILVER, anchor="ra",
       spacing=1.2)

img = img.convert("RGB")
img.save(OUT / "profile-banner.png", optimize=True)
print("banner:", (OUT / "profile-banner.png").stat().st_size, "bytes")
