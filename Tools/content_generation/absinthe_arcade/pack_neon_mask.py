"""Pack grayscale masks into one RGBA <asset>_neonmask.png (plain Python + Pillow).

  R  green neon group   (white = tube/letter lights green)
  G  purple neon group
  B  flicker phase 0..1 (paint a different gray per letter or tube segment)
  A  flicker enable     (white = this light stutters, black = steady when lit)

Omitted --phase defaults to black (all in sync); omitted --flicker defaults to
black (everything steady). All inputs must share one resolution, and that should
match the asset's _emissive map so the same uv_material coordinates drive both.

Usage: python pack_neon_mask.py --green g.png --purple p.png \
           [--phase phase.png] [--flicker flicker.png] --out aa_arch_hero_neonmask.png
"""

import argparse
import sys

from PIL import Image


def load(path, size=None):
    im = Image.open(path).convert("L")
    if size and im.size != size:
        sys.exit(f"{path} is {im.size}, expected {size}")
    return im


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--green", required=True)
    ap.add_argument("--purple", required=True)
    ap.add_argument("--phase")
    ap.add_argument("--flicker")
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)

    r = load(args.green)
    g = load(args.purple, r.size)
    b = load(args.phase, r.size) if args.phase else Image.new("L", r.size, 0)
    a = load(args.flicker, r.size) if args.flicker else Image.new("L", r.size, 0)
    Image.merge("RGBA", (r, g, b, a)).save(args.out, optimize=True)
    print(f"wrote {args.out} {r.size[0]}x{r.size[1]}")


if __name__ == "__main__":
    main()
