# Owner repository assets

`POWERED BY [mikey:hexoid-sys]`

Approved artwork for the `mikey-7x` owner repository. All files belong to **mikey-7x** and may
be reproduced only for the attribution required by `LICENSE`. The brand
`POWERED BY [mikey:hexoid-sys]` belongs to this repository and the three powered projects —
see `NOTICE.md` for the exact list and the four conditions.

| File | Size | Use |
| --- | --- | --- |
| `profile-banner.png` | 1600 × 400 | Owner banner at the top of `README.md` |
| `powered-by-mikey-hexoid-sys.png` | 2000 × 1428 | Hero mark used in the identity section |
| `powered-by-mikey-hexoid-sys.svg` | vector | Print and large-format use |
| `mikey-hexoid-sys-mark.png` | 1024 × 1024 | Square mark for footers and icons |
| `mikey-hexoid-sys-mark.svg` | vector | Scalable square mark |
| `introduction-poster.png` | 2481 × 3508 (A2) | Owner poster: brand, three powered projects, platform, method |
| `introduction-poster.pdf` | A2 vector page | Print and large-format use of the same poster |

## Regenerating the artwork

```bash
python3 tools/make_banner.py     # assets/profile-banner.png
python3 tools/make_poster.py     # assets/introduction-poster.png + .pdf
                                 # (both use tools/poster_kit.py, the shared design system)
cd assets && sha256sum profile-banner.png powered-by-mikey-hexoid-sys.png \
  powered-by-mikey-hexoid-sys.svg mikey-hexoid-sys-mark.png mikey-hexoid-sys-mark.svg \
  introduction-poster.png introduction-poster.pdf > SHA256SUMS
```

Deterministic: the banner trace is synthesised from a fixed seed and the poster is drawn from
fixed coordinates, so both can be reproduced byte-for-byte as long as the fonts, Matplotlib and
Pillow versions are the same.

## Rules

1. Do not crop out, erase or restyle `[mikey:hexoid-sys]`.
2. Proportional resizing only; no stretching or recolouring to illegibility.
3. Keep the credit line `Created by mikey-7x` with the mark.
4. Do not use these files for unrelated work or to suggest endorsement.
5. The mark belongs to this owner repository and the three powered projects listed in
   `NOTICE.md`; do not apply it to any other repository.

`SHA256SUMS` records the exact bytes of every asset here.
