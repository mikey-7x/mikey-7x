# Profile assets

`POWERED BY [mikey:hexoid-sys]`

Approved artwork for the `mikey-7x` GitHub profile. All files belong to **mikey-7x** and may be
reproduced only for the attribution required by `LICENSE`.

| File | Size | Use |
| --- | --- | --- |
| `profile-banner.png` | 1600 × 400 | Profile header image at the top of `README.md` |
| `powered-by-mikey-hexoid-sys.png` | 2000 × 1428 | Hero mark used in the identity section |
| `powered-by-mikey-hexoid-sys.svg` | vector | Print and large-format use |
| `mikey-hexoid-sys-mark.png` | 1024 × 1024 | Square mark for footers and icons |
| `mikey-hexoid-sys-mark.svg` | vector | Scalable square mark |

## Regenerating the banner

```bash
python3 tools/make_banner.py
```

Deterministic: the trace is synthesised from a fixed seed, so the banner can be reproduced
byte-for-byte as long as the fonts and Pillow version are the same.

## Rules

1. Do not crop out, erase or restyle `[mikey:hexoid-sys]`.
2. Proportional resizing only; no stretching or recolouring to illegibility.
3. Keep the credit line `Created by mikey-7x` with the mark.
4. Do not use these files for unrelated work or to suggest endorsement.

`SHA256SUMS` records the exact bytes of every asset here.
