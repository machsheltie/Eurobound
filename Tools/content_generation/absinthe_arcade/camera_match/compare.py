"""E1 comparison sheets (Pillow).

  <venv python> compare.py overlay <render.png> <out.png> [alpha]   50% blend on the 1600 px bible
  <venv python> compare.py side <ref.png> <render.png> <out.png>    reference left, render right, same height
  <venv python> compare.py edges <render.png> <out.png>             bible in grey, render edges in red
"""
import sys
from pathlib import Path

from PIL import Image, ImageFilter, ImageOps

REPO = Path(__file__).resolve().parents[4]
BIBLE_1600 = REPO / "dev/aa_team/crops/00_bible_full_1600.png"


def overlay(render, out, alpha=0.5):
    b = Image.open(BIBLE_1600).convert("RGB")
    r = Image.open(render).convert("RGB").resize(b.size, Image.LANCZOS)
    Image.blend(b, r, float(alpha)).save(out)


def side(ref, render, out):
    a = Image.open(ref).convert("RGB")
    r = Image.open(render).convert("RGB")
    h = max(a.height, r.height, 1600)
    a = a.resize((round(a.width * h / a.height), h), Image.LANCZOS)
    r = r.resize((round(r.width * h / r.height), h), Image.LANCZOS)
    c = Image.new("RGB", (a.width + r.width + 16, h), (255, 255, 255))
    c.paste(a, (0, 0))
    c.paste(r, (a.width + 16, 0))
    c.save(out)


def edges(render, out):
    b = ImageOps.grayscale(Image.open(BIBLE_1600)).convert("RGB")
    r = Image.open(render).convert("L").resize(b.size, Image.LANCZOS)
    e = r.filter(ImageFilter.FIND_EDGES).point(lambda v: 255 if v > 40 else 0)
    b.paste(Image.new("RGB", b.size, (255, 0, 0)), mask=e)
    b.save(out)


if __name__ == "__main__":
    mode, *rest = sys.argv[1:]
    {"overlay": overlay, "side": side, "edges": edges}[mode](*rest)
