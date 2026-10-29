#!/usr/bin/env python3
"""Offline self-check for the mikey-7x profile repository.

POWERED BY [mikey:hexoid-sys] - Copyright (c) 2026 mikey-7x. All rights reserved.

Verifies the expected files, the required identity lines, licence terms, asset
checksums, that every local image referenced by README.md exists, and that no
personal name leaked into the presentation.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRAND = "POWERED BY [mikey:hexoid-sys]"
PASSED, FAILED = [], []


def check(name, condition, detail=""):
    (PASSED if condition else FAILED).append(name + (f": {detail}" if detail and not condition else ""))


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8", errors="replace")


REQUIRED = [
    "README.md", "LICENSE", "NOTICE.md", ".gitattributes", ".gitignore",
    "assets/profile-banner.png", "assets/powered-by-mikey-hexoid-sys.png",
    "assets/powered-by-mikey-hexoid-sys.svg", "assets/mikey-hexoid-sys-mark.png",
    "assets/mikey-hexoid-sys-mark.svg", "assets/README.md", "assets/SHA256SUMS",
    "tools/make_banner.py", "tools/verify_profile.py",
    ".github/workflows/verify.yml",
]
for rel in REQUIRED:
    check(f"file exists: {rel}", (ROOT / rel).is_file())

readme = read("README.md") if (ROOT / "README.md").is_file() else ""
check("README shows the banner", "assets/profile-banner.png" in readme)
check("README shows the hero logo", "assets/powered-by-mikey-hexoid-sys.png" in readme)
check("README shows the square mark", "assets/mikey-hexoid-sys-mark.png" in readme)
check("README carries the identity line", BRAND in readme)
check("README carries the credit", "Created by mikey-7x" in readme)
check("README links the repositories tab", "tab=repositories" in readme)
check("README uses the mikey-7x name only", "mikey-7x" in readme)
check("README has no placeholder text",
      not any(w in readme.lower() for w in ("lorem ipsum", "todo", "tbd", "fixme")))

# every local image must exist
for src in re.findall(r'src="(assets/[^"]+)"', readme):
    check(f"referenced image exists: {src}", (ROOT / src).is_file())

licence = read("LICENSE") if (ROOT / "LICENSE").is_file() else ""
for phrase in ("STRICT PERSONAL & EDUCATIONAL USE LICENCE", BRAND,
               "Copyright (c) 2026 mikey-7x", "MANDATORY ATTRIBUTION",
               "COMMERCIAL LICENSING"):
    check(f"licence contains: {phrase[:40]}", phrase in licence)
check("licence is not open source", "NOT an\nopen-source licence" in licence or "NOT an" in licence)

sums = ROOT / "assets" / "SHA256SUMS"
if sums.is_file():
    listed = 0
    for line in sums.read_text().splitlines():
        if not line.strip():
            continue
        digest, name = line.split(maxsplit=1)
        target = ROOT / "assets" / name.strip()
        actual = hashlib.sha256(target.read_bytes()).hexdigest() if target.is_file() else ""
        check(f"asset checksum: {name.strip()}", actual == digest)
        listed += 1
    check("asset checksum list is complete", listed == 5, f"listed {listed}")

# no personal name anywhere in the published presentation
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or path.suffix.lower() not in {".md", ".py", ".yml", ".cff", ".txt", ".svg", ""}:
        continue
    if path.name in {"verify_profile.py", "00_START_HERE.txt"}:
        continue
    low = path.read_text(encoding="utf-8", errors="replace").lower()
    check(f"no personal name in {path.relative_to(ROOT).as_posix()}",
          not any(n in low for n in ("yogesh", "chauhan", "9825", "9512")))

total = len(PASSED) + len(FAILED)
print(f"Profile verification: {len(PASSED)}/{total} passed")
if FAILED:
    print("\nFailed checks:")
    for item in FAILED:
        print(f"  - {item}")
    sys.exit(1)
print("All structure, identity, licence, image-reference and asset checks passed.")
