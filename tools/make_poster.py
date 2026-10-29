#!/usr/bin/env python3
"""Owner-repository poster for mikey-7x / POWERED BY [mikey:hexoid-sys].

A2 portrait (2481 x 3508 px at 150 dpi). A brand sheet, not an icon wall:
typography, hairline rules and one measured line drawing of the stack.

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
W, H = 2481, 3508
M = 130                    # page margin
CW = W - 2 * M             # content width

BRAND = "POWERED BY [mikey:hexoid-sys]"

PROJECTS = [
    ("01", "mikey:hexoid v5.0.0",
     "Universal embedded cross-compilation engine for Android (Termux) and Linux. 105 board\n"
     "entries, Arduino CLI 0.35.3 pinned, SDCC for 8051 and STM8, iCE40 synthesis on the OSS CAD\n"
     "Suite, and a library manager — driven from a numbered terminal menu, without an IDE.",
     "Bash + Python · Arduino CLI 0.35.3 · SDCC · iCE40 / OSS CAD Suite"),
    ("02", "298.666 MHz frequency counter",
     "STM32F103C8T6 counter on a TIM3:TIM2 32-bit hardware count, asynchronous ETR/8 input, a TI1F\n"
     "cross-check at and below 40 MHz, 100 ms and 250 ms gates, and an SSD1306 display over I2C.\n"
     "Companion exact-step generator and a VHF/UHF transmitter test circuit.",
     "STM32F103C8T6 · STM32duino · SSD1306 I2C · TIM2 ETR / TI1F · 2N2222"),
    ("03", "Project Synapse v1",
     "Single-channel EEG and subvocal-EMG acquisition chain: INA128 front-end at G = 501, ADS1115\n"
     "16-bit conversion at 140 Hz, a framed HC-05 link, Trinx segmentation, DTW matching and\n"
     "CNN-LSTM / CNN-GRU decoders. An experimental study — not a medical device.",
     "INA128 · ADS1115 16-bit · 140 Hz · HC-05 · Trinx / DTW · CNN-LSTM"),
]

CRITERIA = [
    ("01", "Documented architecture", "what the system assumes and what it refuses to do"),
    ("02", "Measured or checkable results", "the method is published with the number"),
    ("03", "Reproducible build path", "pinned versions, scripted install, checksums"),
    ("04", "Explicit limits and licence", "stated in plain language, in the repository"),
]

STACK = [
    ("WORKLOADS", "Windows · Linux · Android applications", False),
    ("COMPATIBILITY & RUNTIME", "Wine + WoW64 · Box64 · Termux · PRoot", False),
    ("GRAPHICS & COMPUTE APIs", "Vulkan · OpenGL / GLES · OpenCL", False),
    ("MESA USER SPACE", "Turnip · Zink · rusticl", False),
    ("KERNEL & LIBC", "Linux DRM / MSM · glibc · bionic", False),
    ("SILICON", "Snapdragon 8 Gen 3 · Adreno 750 · Hexagon NPU", True),
]

METHOD = [
    ("ARCHITECTURE", "which layer owns the job, what each layer\nmay assume, and where it will fail"),
    ("DRIVERS", "Vulkan, OpenGL and OpenCL paths; correctness\nbefore speed, validation on the device"),
    ("HARDWARE", "silicon limits, board bring-up, power and\nthermal budget — calculated, not guessed"),
    ("EVIDENCE", "measured numbers, checksums, and a\nself-check that runs on every push"),
]


def build(target=OUT / "introduction-poster.png"):
    img = K.page(W, H)

    # ---------------------------------------------------------- brand bar --
    K.brand_bar(img, OUT / "mikey-hexoid-sys-mark.png", M, 116, CW,
                brand=BRAND, left_note="the engineering identity of the owner repository",
                right_a="OWNER REPOSITORY", right_b="github.com/mikey-7x")
    K.rule(img, M, 258, W - M, 258, K.RULE, 2)

    # ----------------------------------------------------------- wordmark --
    K.silver_text(img, (M - 6, 286), "MIKEY-7X", K.font(K.BOLD, 176))
    K.text(img, (M, 486), "Architect  ·  software developer  ·  hardware developer",
           K.font(K.SANS, 46), K.SILVER, spacing=0.6)
    K.text(img, (M, 552), "Vulkan capabilities on Android phones — graphics and compute "
                          "drivers, the runtimes above them,", K.font(K.SANS, 31), K.GREY)
    K.text(img, (M, 592), "and the compatibility layers that carry Windows and Linux "
                          "applications onto a phone.", K.font(K.SANS, 31), K.GREY)

    K.meta_row(img, M, 666, CW, [
        ("TARGET PLATFORM", "Snapdragon 8 Gen 3 · Adreno 750"),
        ("API OF RECORD", "Vulkan"),
        ("RUNTIME", "Wine + WoW64 · Box64 · Termux"),
        ("SILICON LIBRARIES", "glibc · bionic"),
        ("LICENCE", "Strict personal & educational"),
    ], size=22)

    # ------------------------------------------------------------- brand --
    K.section(img, M, 800, CW, "01", "THE BRAND",
              "reserved for flagship work only")
    K.text(img, (M, 880),
           "POWERED BY [mikey:hexoid-sys] is the mark of the owner repository. It is not a\n"
           "label for the account: it is applied to the few projects that carry a complete\n"
           "engineering build — architecture, measurement or checkable results, a reproducible\n"
           "path and an explicit licence. Three repositories carry it today.",
           K.font(K.SANS, 30), K.INK, spacing=0)
    # official brand artwork, applied / not applied
    hero = OUT / "powered-by-mikey-hexoid-sys.png"
    if hero.is_file():
        hp = Image.open(hero).convert("RGBA")
        hw = 300
        hp = hp.resize((hw, int(hp.height * hw / hp.width)), Image.LANCZOS)
        img.alpha_composite(hp, (M, 1042))
    K.rule(img, M, 1020, 1260, 1020, K.RULE, 1)
    K.text(img, (M + 340, 1040), "APPLIED TO", K.font(K.MONO, 19), K.DIM, spacing=2.0)
    K.text(img, (M + 340, 1070),
           "flagship instruments · compiler and toolchain ·\nbiosignal acquisition chain",
           K.font(K.SANS, 23), K.SILVER)
    K.text(img, (M + 340, 1152), "NOT APPLIED TO", K.font(K.MONO, 19), K.DIM, spacing=2.0)
    K.text(img, (M + 340, 1182),
           "utilities, experiments, studies and archives — including any\nrepository that does not meet all four criteria",
           K.font(K.SANS, 23), K.GREY)

    for i, (num, title, note) in enumerate(CRITERIA):
        y = 886 + i * 92
        K.text(img, (1420, y), num, K.font(K.MONO, 21), K.DIM)
        K.text(img, (1490, y - 6), title, K.font(K.BOLD, 25), K.INK)
        K.text(img, (1490, y + 30), note, K.font(K.MONO, 20), K.GREY)
        K.rule(img, 1420, y + 62, W - M, y + 62, K.RULE, 1)

    # ---------------------------------------------------------- projects --
    K.section(img, M, 1290, CW, "02", "POWERED PROJECTS", "03 of 33 repositories")
    top = 1370
    for i, (num, name, desc, tags) in enumerate(PROJECTS):
        y = top + i * 246
        K.text(img, (M, y), num, K.font(K.MONO, 34), K.DIM)
        K.text(img, (M + 90, y - 10), name, K.font(K.BOLD, 42), K.INK)
        K.text(img, (W - M, y - 2), BRAND, K.font(K.MONOB, 19), K.SILVER, anchor="ra", spacing=1.0)
        K.text(img, (M + 90, y + 52), desc, K.font(K.SANS, 24), K.GREY, spacing=0)
        K.text(img, (M + 90, y + 196), tags, K.font(K.MONO, 20), K.DIM)
        K.rule(img, M, y + 232, W - M, y + 232, K.RULE, 1)

    # --------------------------------------------------------- platform ---
    K.section(img, M, 2140, CW, "03", "PLATFORM", "silicon to application, in six layers")
    K.band_diagram(img, M + 40, 2230, CW - 40, STACK, band_height=76, gap=14)

    # ----------------------------------------------------------- method ---
    K.section(img, M, 2850, CW, "04", "METHOD", "how the work is done")
    for i, (title, note) in enumerate(METHOD):
        x = M + i * (CW / 4)
        K.text(img, (x, 2928), title, K.font(K.MONOB, 22), K.SILVER, spacing=2.2)
        K.text(img, (x, 2972), note, K.font(K.SANS, 21), K.GREY)
        if i:
            ImageDraw.Draw(img).line([(x - 34, 2920), (x - 34, 3060)], fill=K.RULE + (255,), width=1)

    # ----------------------------------------------------------- footer ---
    K.footer(img, M, 3130, CW,
             contacts=[("EMAIL", "chauhanyogesh9825@gmail.com"),
                       ("GITHUB", "github.com/mikey-7x"),
                       ("YOUTUBE", "youtube.com/@mikey-7x"),
                       ("BLOG", "rtod-yv8.blogspot.com/?m=1"),
                       ("LINKEDIN", "linkedin.com/in/yogesh-r-chauhan-780005417")],
             licence_lines=["Personal and educational use with attribution.",
                            "Commercial, industrial and clinical use require a",
                            "separate written licence. Technical statements on this",
                            "sheet describe active work; they are not benchmark",
                            "results or certifications."],
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
