"""Helper for stamp_text.py (system Python + Pillow): renders the 1024 px disc bitmap (rim ring, flat fill, bold dark text).
python stamp_text_bitmap.py '<json: lines fill ink rim margin blur font out>'   prints the font size in px."""
import sys, json, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
c = json.loads(sys.argv[1]); lines, fill, ink, rimf, margin = c["lines"], c["fill"], c["ink"], c["rim"], c["margin"]
FONT = c["font"]; N = 1024
def bitmap():
    """disc bitmap over [-1,1]^2: returns RGB float (N,N,3), disc mask is d<=1 computed by the caller"""
    bm = Image.new("RGB", (N, N), tuple(int(c * 255) for c in [x * rimf for x in fill]))
    dr = ImageDraw.Draw(bm); R = N / 2
    inner = 1 - 0.10   # rim ring width 0.10 r
    dr.ellipse([R - R * inner, R - R * inner, R + R * inner, R + R * inner], fill=tuple(int(c * 255) for c in fill))
    n = len(lines); usable = 1 - margin - 0.10
    L = 2 * usable * 0.74 / n * R   # line pitch in px (block spans about +-0.74 usable)
    size = int(L * 1.0)
    while True:
        f = ImageFont.truetype(FONT, size); ok = True
        for i, t in enumerate(lines):
            yc = (i - (n - 1) / 2) * L
            bb = dr.textbbox((0, 0), t, font=f, anchor="ls")
            half_h = max(abs(bb[1]), abs(bb[3])) / 2
            chord = 2 * math.sqrt(max((usable * R) ** 2 - (abs(yc) + half_h) ** 2, 1)) * 0.98
            if bb[2] - bb[0] > chord or (bb[3] - bb[1]) > L * 1.02: ok = False
        if ok or size < 20: break
        size -= 2
    for i, t in enumerate(lines):
        yc = R + (i - (n - 1) / 2) * L
        dr.text((R, yc), t, font=f, fill=tuple(int(c * 255) for c in ink), anchor="mm")
    return bm, size



bm, size = bitmap()
if c["blur"] > 0: bm = bm.filter(ImageFilter.GaussianBlur(c["blur"]))
bm.save(c["out"]); print(size)
