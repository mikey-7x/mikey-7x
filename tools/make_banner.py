#!/usr/bin/env python3
"""GitHub profile banner for mikey-7x (1600x400), deterministic."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1600, 400
BG = (7, 8, 10)
TEXT = (238, 239, 242)
SILVER = (199, 204, 211)
MUTED = (150, 155, 161)
DIM = (104, 110, 116)
CYAN = (57, 224, 230)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
for y in range(H):
    v = int(26 - 17 * y / H)
    d.line([(0, y), (W, y)], fill=(v, v, v + 2))
for i in range(60):
    a = int(14 * (i / 60))
    d.rectangle([i, i, W - 1 - i, H - 1 - i], outline=(a + 8, a + 8, a + 10))
d.line([(48, 42), (W - 48, 42)], fill=(56, 59, 63), width=1)
d.line([(48, H - 44), (W - 48, H - 44)], fill=(56, 59, 63), width=1)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
f_kick = ImageFont.truetype(MONO, 22)
f_name = ImageFont.truetype(BOLD, 104)
f_tag = ImageFont.truetype(REG, 27)
f_small = ImageFont.truetype(MONO, 19)
f_tiny = ImageFont.truetype(MONO, 17)

x = 74
d.text((x, 92), "EMBEDDED SYSTEMS  ·  TOOLING  ·  LINUX ON MOBILE", font=f_kick, fill=MUTED)
d.text((x, 128), "mikey-7x", font=f_name, fill=TEXT)
d.line([(x, 258), (x + 470, 258)], fill=(74, 77, 82), width=2)
d.text((x, 276), "Firmware, compilers and instruments — built, measured, documented.", font=f_tag, fill=(206, 209, 214))
d.text((x, 322), "POWERED BY [mikey:hexoid-sys]", font=f_small, fill=SILVER)
d.text((x, 348), "github.com/mikey-7x", font=f_tiny, fill=DIM)

# right motif: trace + slices
rng = np.random.default_rng(3)
t = np.linspace(0, 8 * np.pi, 640)
sig = (np.sin(t) * 0.5 + 0.3 * np.sin(2.6 * t + 0.8) + 0.14 * np.sin(5.9 * t)
       + rng.normal(0, 0.05, t.size))
sig = (sig - sig.mean()) / (np.abs(sig).max() + 1e-9)
base_x, base_y, width, height = 900, 196, 600, 180
pts = [(base_x + i * width / sig.size, base_y - s * height * 0.4) for i, s in enumerate(sig)]
d.line(pts, fill=(70, 76, 82), width=1)
smooth = np.convolve(sig, np.ones(11) / 11, mode="same")
pts2 = [(base_x + i * width / smooth.size, base_y - s * height * 0.4) for i, s in enumerate(smooth)]
d.line(pts2, fill=CYAN, width=2)
for k in range(5):
    xx = base_x + k * 120
    d.rectangle([xx, base_y + 104, xx + 96, base_y + 136], outline=(58, 64, 70))
d.text((base_x, 344), "signal  ·  slices  ·  decode", font=f_tiny, fill=DIM)

mark = Image.open(OUT / "mikey-hexoid-sys-mark.png").convert("RGBA")
mh = 120
mark = mark.resize((int(mark.width * mh / mark.height), mh), Image.LANCZOS)
img.paste(mark, (W - 74 - mark.width, 74), mark)

img.save(OUT / "profile-banner.png", optimize=True)
print("banner:", (OUT / "profile-banner.png").stat().st_size, "bytes")
