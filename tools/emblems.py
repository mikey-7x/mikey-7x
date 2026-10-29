#!/usr/bin/env python3
"""emblem definitions for the owner poster.

Each entry is (key, label, note, accent, builder). Builders draw a silhouette
into an 'L' mask at the requested size; optional `cut` glyphs are subtracted,
so letters become real holes in the extruded mark.

These are original stylised symbols drawn for this poster — not vendor artwork.
"""
from __future__ import annotations

import math

from PIL import Image, ImageDraw, ImageFont

import emblem3d as E

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONOB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


# --------------------------------------------------------------- utilities --
def letters(size, text, ratio=0.58, font_path=MONOB, dx=0.0, dy=0.0, tracking=0.0):
    """A mask of centred text, for subtraction from a silhouette."""
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    f = ImageFont.truetype(font_path, int(size * ratio))
    total = sum(d.textlength(ch, font=f) + size * tracking for ch in text) - size * tracking
    x = (size - total) / 2 + dx * size
    y = (size - int(size * ratio)) / 2 + dy * size
    for ch in text:
        d.text((x, y), ch, font=f, fill=255)
        x += d.textlength(ch, font=f) + size * tracking
    return m


def cut(mask, other):
    from PIL import ImageChops
    return ImageChops.subtract(mask, other)


def ring(d, s, o, cx, cy, r_out, r_in, fill=255):
    d.ellipse([cx - r_out, cy - r_out, cx + r_out, cy + r_out], fill=fill)
    d.ellipse([cx - r_in, cy - r_in, cx + r_in, cy + r_in], fill=0)



def as_mask(fn, s, o=0.0):
    """Call a builder that wants a Draw object, or one that returns a mask."""
    import inspect
    m = Image.new("L", (s, s), 0)
    if len(inspect.signature(fn).parameters) >= 3:
        out = fn(ImageDraw.Draw(m), s, o)
        return out if isinstance(out, Image.Image) else m
    return fn(s, o)


# ------------------------------------------------------------------ shapes --
def vulkan(d, s, o=0.0):
    w = s * 0.74
    x0 = o + (s - w) / 2
    for yy, ww in ((0.05, 1.0), (0.39, 0.66), (0.67, 0.34)):
        top = o + s * yy
        left = (x0 + w * (1 - ww) / 2, top)
        right = (left[0] + w * ww, top)
        d.polygon([left, right, (right[0] - w * ww * 0.26, top + s * 0.17),
                   (x0 + w / 2, top + s * 0.31),
                   (left[0] + w * ww * 0.26, top + s * 0.17)], fill=255)


def snapdragon(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([o + s * 0.15, o + s * 0.15, o + s * 0.85, o + s * 0.85],
                        radius=s * 0.07, fill=255)
    for i in range(7):
        u = 0.21 + i * 0.097
        d.rectangle([o + s * u, o + s * 0.055, o + s * (u + 0.048), o + s * 0.16], fill=255)
        d.rectangle([o + s * u, o + s * 0.84, o + s * (u + 0.048), o + s * 0.945], fill=255)
        d.rectangle([o + s * 0.055, o + s * u, o + s * 0.16, o + s * (u + 0.048)], fill=255)
        d.rectangle([o + s * 0.84, o + s * u, o + s * 0.945, o + s * (u + 0.048)], fill=255)
    return m


def adreno(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([o + s * 0.10, o + s * 0.22, o + s * 0.90, o + s * 0.78],
                        radius=s * 0.10, fill=255)
    return m


def hexagon_size(s, o, r):
    cx = o + s / 2
    cy = o + s / 2
    return [(cx + r * math.cos(math.radians(60 * i - 30)),
             cy + r * math.sin(math.radians(60 * i - 30))) for i in range(6)]


def hexnpu(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.polygon(hexagon_size(s, o, s * 0.46), fill=255)
    d.polygon(hexagon_size(s, o, s * 0.31), fill=0)
    d.polygon(hexagon_size(s, o, s * 0.21), fill=255)
    return m


def mesa(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.polygon([(o + s * 0.5, o + s * 0.09), (o + s * 0.93, o + s * 0.88),
               (o + s * 0.07, o + s * 0.88)], fill=255)
    # the band that runs across the triangle
    d.polygon([(o + s * 0.30, o + s * 0.60), (o + s * 0.70, o + s * 0.60),
               (o + s * 0.78, o + s * 0.71), (o + s * 0.22, o + s * 0.71)], fill=0)
    return m


def turnip(s, o=0.0):
    """A root and a sprout: the turnip's own silhouette, drawn as one shape."""
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.ellipse([o + s * 0.17, o + s * 0.40, o + s * 0.83, o + s * 0.82], fill=255)
    d.polygon([(o + s * 0.21, o + s * 0.60), (o + s * 0.79, o + s * 0.60),
               (o + s * 0.50, o + s * 0.94)], fill=255)
    # sprout: a stem and three leaves
    d.polygon([(o + s * 0.465, o + s * 0.46), (o + s * 0.535, o + s * 0.46),
               (o + s * 0.52, o + s * 0.20), (o + s * 0.48, o + s * 0.20)], fill=255)
    d.ellipse([o + s * 0.30, o + s * 0.10, o + s * 0.50, o + s * 0.26], fill=255)
    d.ellipse([o + s * 0.50, o + s * 0.10, o + s * 0.70, o + s * 0.26], fill=255)
    d.ellipse([o + s * 0.42, o + s * 0.03, o + s * 0.58, o + s * 0.19], fill=255)
    return m


def zink(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    pts = [(0.12, 0.10), (0.88, 0.10), (0.88, 0.29), (0.45, 0.66),
           (0.88, 0.66), (0.88, 0.90), (0.12, 0.90), (0.12, 0.71),
           (0.55, 0.34), (0.12, 0.34)]
    d.polygon([(o + s * a, o + s * b) for a, b in pts], fill=255)
    return m


def gear_mask(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    cx = cy = o + s / 2
    ro, ri = s * 0.46, s * 0.365
    teeth = 10
    pts = []
    for i in range(teeth * 2):
        ang = 2 * math.pi * i / (teeth * 2) - math.pi / 2
        r = ro if i % 2 == 0 else ri
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d.polygon(pts, fill=255)
    d.polygon(hexagon_size(s, o, s * 0.17), fill=0)
    return m


def opengl(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.polygon(hexagon_size(s, o, s * 0.47), fill=255)
    # three lines from the centre to alternating corners
    cx = cy = o + s / 2
    for ang in (-90, 30, 150):
        a = math.radians(ang)
        d.line([(cx, cy), (cx + s * 0.5 * math.cos(a), cy + s * 0.5 * math.sin(a))],
               fill=0, width=max(3, int(s * 0.045)))
    d.ellipse([cx - s * 0.07, cy - s * 0.07, cx + s * 0.07, cy + s * 0.07], fill=0)
    return m


def opencl(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.polygon(hexagon_size(s, o, s * 0.47), fill=255)
    d.polygon(hexagon_size(s, o, s * 0.36), fill=0)
    d.polygon(hexagon_size(s, o, s * 0.30), fill=255)
    return m


def linux(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.ellipse([o + s * 0.245, o + s * 0.05, o + s * 0.755, o + s * 0.58], fill=255)
    d.ellipse([o + s * 0.175, o + s * 0.26, o + s * 0.825, o + s * 0.90], fill=255)
    d.ellipse([o + s * 0.105, o + s * 0.55, o + s * 0.295, o + s * 0.85], fill=255)
    d.ellipse([o + s * 0.705, o + s * 0.55, o + s * 0.895, o + s * 0.85], fill=255)
    d.ellipse([o + s * 0.225, o + s * 0.885, o + s * 0.445, o + s * 0.965], fill=255)
    d.ellipse([o + s * 0.555, o + s * 0.885, o + s * 0.775, o + s * 0.965], fill=255)
    d.ellipse([o + s * 0.375, o + s * 0.195, o + s * 0.445, o + s * 0.275], fill=0)
    d.ellipse([o + s * 0.555, o + s * 0.195, o + s * 0.625, o + s * 0.275], fill=0)
    return m


def glibc(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.ellipse([o + s * 0.06, o + s * 0.06, o + s * 0.94, o + s * 0.94], fill=255)
    return m


def bionic(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.polygon([(o + s * 0.50, o + s * 0.06), (o + s * 0.90, o + s * 0.26),
               (o + s * 0.90, o + s * 0.58), (o + s * 0.50, o + s * 0.94),
               (o + s * 0.10, o + s * 0.58), (o + s * 0.10, o + s * 0.26)], fill=255)
    return m


def android(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.pieslice([o + s * 0.13, o + s * 0.24, o + s * 0.87, o + s * 0.98], 180, 360, fill=255)
    d.rectangle([o + s * 0.13, o + s * 0.60, o + s * 0.87, o + s * 0.80], fill=255)
    for dx in (0.24, 0.76):
        d.line([(o + s * dx, o + s * 0.34), (o + s * (dx - 0.07 + 0.14 * (dx > 0.5)),
                                            o + s * 0.19)], fill=255, width=int(s * 0.045))
    d.ellipse([o + s * 0.32, o + s * 0.50, o + s * 0.40, o + s * 0.58], fill=0)
    d.ellipse([o + s * 0.60, o + s * 0.50, o + s * 0.68, o + s * 0.58], fill=0)
    return m


def termux(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([o + s * 0.06, o + s * 0.16, o + s * 0.94, o + s * 0.84],
                        radius=s * 0.09, fill=255)
    d.rounded_rectangle([o + s * 0.12, o + s * 0.24, o + s * 0.88, o + s * 0.76],
                        radius=s * 0.05, fill=0)
    d.line([(o + s * 0.22, o + s * 0.42), (o + s * 0.33, o + s * 0.50)], fill=255,
           width=int(s * 0.05))
    d.line([(o + s * 0.33, o + s * 0.50), (o + s * 0.22, o + s * 0.58)], fill=255,
           width=int(s * 0.05))
    d.rectangle([o + s * 0.38, o + s * 0.56, o + s * 0.60, o + s * 0.61], fill=255)
    return m


def termux_x11(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([o + s * 0.05, o + s * 0.14, o + s * 0.95, o + s * 0.72],
                        radius=s * 0.06, fill=255)
    d.rounded_rectangle([o + s * 0.12, o + s * 0.21, o + s * 0.88, o + s * 0.65],
                        radius=s * 0.03, fill=0)
    d.rectangle([o + s * 0.44, o + s * 0.72, o + s * 0.56, o + s * 0.86], fill=255)
    d.rounded_rectangle([o + s * 0.28, o + s * 0.86, o + s * 0.72, o + s * 0.94],
                        radius=s * 0.03, fill=255)
    d.line([(o + s * 0.28, o + s * 0.28), (o + s * 0.72, o + s * 0.58)], fill=255,
           width=int(s * 0.055))
    d.line([(o + s * 0.72, o + s * 0.28), (o + s * 0.28, o + s * 0.58)], fill=255,
           width=int(s * 0.055))
    return m


def box64(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    c = o + s / 2
    hexa = [(c, c - s * 0.46), (c + s * 0.44, c - s * 0.20), (c, c + s * 0.06),
            (c - s * 0.44, c - s * 0.20)]
    d.polygon(hexa, fill=255)
    d.polygon([(c, c + s * 0.06), (c + s * 0.44, c - s * 0.20),
               (c + s * 0.44, c + s * 0.26), (c, c + s * 0.50)], fill=255)
    d.polygon([(c, c + s * 0.06), (c - s * 0.44, c - s * 0.20),
               (c - s * 0.44, c + s * 0.26), (c, c + s * 0.50)], fill=255)
    return m


def wine(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.polygon([(o + s * 0.17, o + s * 0.07), (o + s * 0.83, o + s * 0.07),
               (o + s * 0.61, o + s * 0.44), (o + s * 0.58, o + s * 0.56),
               (o + s * 0.42, o + s * 0.56), (o + s * 0.39, o + s * 0.44)], fill=255)
    d.rectangle([o + s * 0.465, o + s * 0.54, o + s * 0.535, o + s * 0.82], fill=255)
    d.ellipse([o + s * 0.26, o + s * 0.79, o + s * 0.74, o + s * 0.94], fill=255)
    return m


def wow64(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([o + s * 0.08, o + s * 0.16, o + s * 0.92, o + s * 0.84],
                        radius=s * 0.10, fill=255)
    return m


def accel(s, o=0.0):
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    d.polygon([(o + s * 0.60, o + s * 0.03), (o + s * 0.19, o + s * 0.57),
               (o + s * 0.44, o + s * 0.57), (o + s * 0.36, o + s * 0.97),
               (o + s * 0.81, o + s * 0.39), (o + s * 0.54, o + s * 0.39)], fill=255)
    return m


# ------------------------------------------------------------------ registry --
EMBLEMS = [
    # key, label, sub-label, accent rgb, mask builder, optional cut glyphs
    ("vulkan", "Vulkan", "explicit GPU API", (214, 66, 62), vulkan, None),
    ("snapdragon", "Snapdragon 8 Gen 3", "target SoC", (198, 30, 58), snapdragon,
     "8G3"),
    ("adreno", "Adreno 750", "GPU", (216, 92, 56), adreno, "750"),
    ("hexagon", "Hexagon NPU", "DSP · inference", (186, 116, 190), hexnpu, None),
    ("mesa", "Mesa", "driver framework", (74, 140, 202), mesa, None),
    ("turnip", "Turnip", "Adreno Vulkan driver", (146, 104, 208), turnip, None),
    ("zink", "Zink", "OpenGL on Vulkan", (44, 186, 172), zink, None),
    ("rusticl", "rusticl", "OpenCL on Mesa", (198, 104, 48), gear_mask, None),
    ("opengl", "OpenGL / GLES", "3D graphics API", (64, 166, 214), opengl, None),
    ("opencl", "OpenCL", "compute API", (120, 136, 150), opencl, "CL"),
    ("linux", "Linux kernel", "DRM / MSM · scheduler", (206, 164, 44), linux, None),
    ("glibc", "glibc", "Linux C library", (76, 128, 172), glibc, "GNU"),
    ("bionic", "bionic", "Android C library", (122, 178, 68), bionic, "BIO"),
    ("android", "Android", "target platform", (98, 178, 92), android, None),
    ("termux", "Termux", "Linux user space", (72, 184, 96), termux, None),
    ("termux_x11", "Termux:X11", "desktop on the phone", (128, 152, 176), termux_x11, None),
    ("box64", "Box64", "x86_64 → ARM64", (96, 112, 196), box64, "64"),
    ("wine", "Wine", "Windows applications", (154, 52, 78), wine, None),
    ("wow64", "WoW64", "32-bit in 64-bit", (110, 132, 158), wow64, "W64"),
    ("accel", "Hardware acceleration", "GPU + NPU offload", (232, 166, 72), accel, None),
]


# ------------------------------------------------------------------ builder --
def emblem_image(size, entry, **kw):
    """Render one registry entry to an RGBA image of `size` (plus bleed)."""
    from PIL import ImageChops

    key, label, sub, accent, fn, cut_text = entry
    s = size * E.SS
    mask = as_mask(fn, s)
    if cut_text:
        mask = ImageChops.subtract(mask, letters(s, cut_text, ratio=0.26, tracking=0.02))
    img = E.render(mask, accent, **kw)
    return img.resize((int(size * 1.14),) * 2, Image.LANCZOS)


def emblem_by_key(key):
    for entry in EMBLEMS:
        if entry[0] == key:
            return entry
    raise KeyError(key)
