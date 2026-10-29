#!/usr/bin/env python3
"""emblem3d — a compact relief renderer used by the owner poster.

A silhouette is turned into a height field: flat interior, bevelled border from
a chamfer distance transform, shaded with Lambert + Blinn-Phong, extruded
downwards and dropped on a soft shadow. Everything is numpy, so a full poster
renders in a few seconds.

POWERED BY [mikey:hexoid-sys] - Copyright (c) 2026 mikey-7x. All rights reserved.
"""
from __future__ import annotations

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SS = 2  # supersampling factor


def lerp(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))


def lighter(c, t):
    return lerp(c, (255, 255, 255), t)


def darker(c, t):
    return lerp(c, (0, 0, 0), t)


# ------------------------------------------------------- distance transform --
def chamfer_dist(mask):
    """Distance in pixels from the nearest background pixel (3-4 chamfer)."""
    n = mask.shape[0]
    big = 1e6
    d = np.where(mask > 0.5, big, 0.0).astype(np.float32)
    a, b = 1.0, 1.4142
    for y in range(1, n):
        prev, cur = d[y - 1], d[y]
        cand = prev + a
        np.minimum(cur, cand, out=cur)
        np.minimum(cur[1:], (prev[:-1] + b), out=cur[1:])
        np.minimum(cur[:-1], (prev[1:] + b), out=cur[:-1])
    for y in range(n - 2, -1, -1):
        prev, cur = d[y + 1], d[y]
        np.minimum(cur, prev + a, out=cur)
        np.minimum(cur[1:], (prev[:-1] + b), out=cur[1:])
        np.minimum(cur[:-1], (prev[1:] + b), out=cur[:-1])
    return d


def extrude_alpha(mask, depth):
    """Union of the mask shifted down 1..depth px, brightest next to the face."""
    n = mask.shape[0]
    out = np.zeros((n + depth, n), np.float32)
    for i in range(1, depth + 1):
        np.maximum(out[i:i + n], mask * (1.0 - 0.55 * i / depth), out=out[i:i + n])
    return out


# ---------------------------------------------------------------- renderer --
def render(mask, accent, depth=0.10, bevel=0.055, gloss=0.55, shadow=0.5,
           light=(-0.46, -0.60, 0.66), ambient=0.44, diffuse=0.76,
           spec_power=30.0, rim=0.40):
    n = mask.size[0]
    m = np.asarray(mask, np.float32) / 255.0
    m = (m > 0.5).astype(np.float32)
    if m.sum() < 10:
        return Image.new("RGBA", (n, n), (0, 0, 0, 0))

    bevel_px = max(2.0, n * bevel)
    depth_px = max(2, int(n * depth))

    dist = chamfer_dist(m)
    height = np.clip(dist / bevel_px, 0, 1)
    height = np.asarray(
        Image.fromarray((height * 255).astype(np.uint8), "L").filter(
            ImageFilter.GaussianBlur(max(1.0, n * 0.004))), np.float32) / 255.0

    gy, gx = np.gradient(height * bevel_px * 1.0)
    nx, ny = -gx, -gy
    nz = np.full_like(nx, max(1.0, bevel_px * 0.55))
    norm = np.sqrt(nx * nx + ny * ny + nz * nz)
    nx, ny, nz = nx / norm, ny / norm, nz / norm

    L = np.array(light, np.float32)
    L /= np.linalg.norm(L)
    lambert = np.clip(nx * L[0] + ny * L[1] + nz * L[2], 0, 1)

    H = L + np.array([0, 0, 1.0], np.float32)
    H /= np.linalg.norm(H)
    spec = np.clip(nx * H[0] + ny * H[1] + nz * H[2], 0, 1) ** spec_power
    fres = (1.0 - np.clip(nz, 0, 1)) ** 2

    yy, xx = np.mgrid[0:n, 0:n].astype(np.float32) / (n - 1)
    t = np.clip(xx * 0.40 + yy * 0.60, 0, 1)[..., None]
    base = np.array(lighter(accent, 0.28), np.float32) * (1 - t) + \
        np.array(darker(accent, 0.34), np.float32) * t

    rgb = base * (ambient + diffuse * lambert)[..., None]
    rgb += (spec * gloss)[..., None] * 255.0
    rgb += (fres * rim * lambert)[..., None] * 255.0 * 0.5
    rgb = np.clip(rgb, 0, 255)

    # ---- canvas large enough for the extrusion
    H2 = n + depth_px + 4
    out = np.zeros((H2, n, 4), np.float32)
    take = min(H2, n)

    # drop shadow
    sh = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(
        ImageFilter.GaussianBlur(max(2.0, n * 0.02))), np.float32) / 255.0
    sh = np.roll(sh, int(n * 0.03) + depth_px, axis=0)
    shadow_alpha = np.zeros((H2, n), np.float32)
    shadow_alpha[:take] = np.clip(sh[:take] * shadow, 0, 1)
    out = _over(out, np.zeros((H2, n, 3), np.float32), shadow_alpha)

    # extruded side wall
    side_alpha = np.zeros((H2, n), np.float32)
    ext = extrude_alpha(m, depth_px)
    side_alpha[:ext.shape[0]] = ext
    grad = np.linspace(1.0, 0.5, H2, dtype=np.float32)[:, None, None]
    side_rgb = np.clip(np.array(darker(accent, 0.58), np.float32)[None, None, :] * grad, 0, 255)
    out = _over(out, side_rgb, side_alpha)

    # shaded top face
    face_rgb = np.zeros((H2, n, 3), np.float32)
    face_rgb[:n] = rgb
    face_alpha = np.zeros((H2, n), np.float32)
    face_alpha[:n] = m
    out = _over(out, face_rgb, face_alpha)

    img = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA")
    if H2 != n:
        img = img.resize((n, n), Image.LANCZOS)
    return img


def _over(dst, src_rgb, src_alpha):
    """Composite an RGB layer with a 0..1 alpha over an RGBA float buffer."""
    sa = src_alpha[..., None]
    da = dst[..., 3:4] / 255.0
    oa = sa + da * (1 - sa)
    safe = np.maximum(oa, 1e-6)
    dst[..., :3] = (src_rgb * sa + dst[..., :3] * da * (1 - sa)) / safe
    dst[..., 3] = np.clip(oa[..., 0] * 255.0, 0, 255)
    return dst


def compose(size, mask_fn, accent, **kw):
    """Rasterise a silhouette at SS scale, render, return an RGBA of `size`."""
    import inspect

    big = size * SS
    m = Image.new("L", (big, big), 0)
    if len(inspect.signature(mask_fn).parameters) >= 3:      # fn(draw, size, origin)
        mask_fn(ImageDraw.Draw(m), big, 0.0)
    else:                                                    # fn(size, origin) -> mask
        m = mask_fn(big, 0.0)
    out = render(m, accent, **kw)
    return out.resize((int(size * 1.12),) * 2, Image.LANCZOS)


def detail(img, size, draw_fn):
    draw_fn(ImageDraw.Draw(img), img.size[0])
    return img
