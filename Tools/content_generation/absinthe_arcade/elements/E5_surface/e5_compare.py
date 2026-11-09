"""Side-by-side compare: the bible window (full-res bible, or crop 05 for the crop05 view) left, render right.

  <venv python> e4_compare.py <view> <render.png> <out.png>
"""
import sys

from PIL import Image

sys.path.insert(0, __file__.rsplit("\\", 1)[0].rsplit("/", 1)[0])
from e5_cam import BIBLE  # noqa: E402
from e5_render_views import views  # noqa: E402

def main():
    view, ren, out = sys.argv[1:4]
    # every view (crop05 included) is cut from the full-res bible at the render's own window, so the
    # two halves are pixel-registered; crop05_window() is crop 05's footprint in the bible
    Image.MAX_IMAGE_PIXELS = None
    a = Image.open(BIBLE).convert("RGB").crop(views()[view])
    b = Image.open(ren).convert("RGB")
    a = a.resize((round(a.width * b.height / a.height), b.height), Image.LANCZOS)
    o = Image.new("RGB", (a.width + b.width + 12, b.height), (255, 255, 255))
    o.paste(a, (0, 0))
    o.paste(b, (a.width + 12, 0))
    o.save(out)


main()
