"""Comparison sheets for the integrated aa_exterior renders (dev/aa_team/renders/E1/integration/).

  <venv python> integration_compares.py

bible-cam: 50% overlay on the full bible (resized to the render) and a side-by-side, for material
and clay; right corner vs asset-sheet crop 12 (render cropped to x -1.0..3.7 of its 6.5 m ortho
frame); roof front vs the roof band of crop 09; roof and hero isos vs crop 13.
"""
from pathlib import Path

from PIL import Image

Image.MAX_IMAGE_PIXELS = None
REPO = Path(__file__).resolve().parents[4]
O = REPO / "dev/aa_team/renders/E1/integration"
C = REPO / "dev/aa_team/crops"
BIBLE = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/references/Exterior/absinthearcadedaytime.png"


def side(a, r, out, h):
    a = a.resize((round(a.width * h / a.height), h), Image.LANCZOS)
    r = r.resize((round(r.width * h / r.height), h), Image.LANCZOS)
    c = Image.new("RGB", (a.width + r.width + 16, h), "white")
    c.paste(a, (0, 0))
    c.paste(r, (a.width + 16, 0))
    c.save(out)


def _crop(im, f):
    """Crop by fractions (x0, y0, x1, y1) of the frame (the roof band of the iso render)."""
    return im.crop((round(f[0] * im.width), round(f[1] * im.height), round(f[2] * im.width), round(f[3] * im.height)))


def main():
    bible = Image.open(BIBLE).convert("RGB")
    for tag in ("", "_clay"):
        p = O / f"final_bible_cam_full{tag}.png"
        if not p.exists():
            continue
        r = Image.open(p).convert("RGB")
        b = bible.resize(r.size, Image.LANCZOS)
        Image.blend(b, r, 0.5).save(O / f"overlay50_bible_cam_full{tag}.png")
        side(b, r, O / f"compare_bible_cam_full{tag}.png", r.height)
        p = O / f"final_right_corner{tag}.png"
        if p.exists():
            r = Image.open(p).convert("RGB")
            x0 = round((-1.0 + 2.8) * r.width / 6.5)
            side(Image.open(C / "12_assetsheet_front_right_half.png").convert("RGB"), r.crop((x0, 0, r.width, r.height)),
                 O / f"compare_right_corner{tag}.png", r.height)
    if (O / "final_roof_front.png").exists():
        side(Image.open(C / "09_assetsheet_front_full_height.png").convert("RGB").crop((10, 15, 400, 160)),
             Image.open(O / "final_roof_front.png").convert("RGB"), O / "compare_roof_front.png", 800)
    if (O / "final_roof_iso.png").exists():
        side(Image.open(C / "13_assetsheet_hero_iso.png").convert("RGB").crop((60, 0, 480, 170)),
             _crop(Image.open(O / "final_roof_iso.png").convert("RGB"), (0.22, 0.1, 0.86, 0.62)),
             O / "compare_roof_iso.png", 900)
    if (O / "final_hero_iso.png").exists():
        side(Image.open(C / "13_assetsheet_hero_iso.png").convert("RGB"),
             Image.open(O / "final_hero_iso.png").convert("RGB"), O / "compare_hero_iso.png", 1600)


if __name__ == "__main__":
    main()
