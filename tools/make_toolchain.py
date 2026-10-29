#!/usr/bin/env python3
"""Export the toolchain emblems used by the README.

Renders every entry of tools/emblems.py to assets/toolchain/NN-name.png, so the
owner repository can show the same marks the poster uses.

POWERED BY [mikey:hexoid-sys] - Copyright (c) 2026 mikey-7x. All rights reserved.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from PIL import Image  # noqa: E402

import emblems as EM  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "toolchain"
OUT.mkdir(parents=True, exist_ok=True)

SIZE = 224

names = []
for i, entry in enumerate(EM.EMBLEMS, start=1):
    key, label, sub, accent = entry[0], entry[1], entry[2], entry[3]
    img = EM.emblem_image(SIZE, entry, depth=0.075)
    path = OUT / f"{i:02d}-{key}.png"
    img.save(path, optimize=True)
    names.append(f"{path.name}\t{label}\t{sub}")

# a sheet of everything, for the poster and for documentation
cols = 5
rows = (len(EM.EMBLEMS) + cols - 1) // cols
cell = SIZE
sheet = Image.new("RGB", (cols * cell, rows * cell), (10, 11, 13))
for i, entry in enumerate(EM.EMBLEMS):
    img = EM.emblem_image(cell, entry, depth=0.075)
    r, c = divmod(i, cols)
    x, y = c * cell, r * cell
    tile = sheet.crop((x, y, x + cell, y + cell))
    tile.paste(img, (0, 0), img)
    sheet.paste(tile, (x, y))
sheet.save(OUT / "toolchain-sheet.png", optimize=True)
sheet.resize((sheet.width // 2, sheet.height // 2), Image.LANCZOS).save(
    OUT / "toolchain-sheet.png", optimize=True)

(OUT / "INDEX.txt").write_text(
    "Toolchain emblems — original stylised symbols drawn by tools/emblems.py.\n"
    "POWERED BY [mikey:hexoid-sys] — Copyright (c) 2026 mikey-7x. All rights reserved.\n\n"
    "file\tlabel\tnote\n" + "\n".join(names) + "\n",
    encoding="utf-8")

print(f"exported {len(names)} emblems to {OUT}")
