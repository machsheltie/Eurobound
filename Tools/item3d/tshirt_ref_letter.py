"""I Survived The Cock-Up T-shirt: type the doc's lettering onto the approved Firefly reference, then cut it out.

python -I Tools/item3d/tshirt_ref_letter.py <ref_raw.png> <out_lettered.png> <out_cutout.png>

Lettering is never drawn by an image tool (tripo_asset_workflow.md, "Standing rules"): Firefly was asked for an empty
band above the crying dial, and this script types the three lines from
design/items/debaucheryville_items/i_survived_tshirt_item.md ("lettering" and "decoration" fields):
  I SURVIVED THE   small royal-blue capitals            #1F4FA3
  COCK-UP          enormous red capitals, bowed over the belly, cracked across the folds, flaking at the "C"   #D42B2B
  DEBAUCHERYVILLE  small blue capitals with the red swoosh underline   #1F4FA3
The ink is modulated by the fabric's own light and shade so it sits on the cloth like the generated print.
The cut-out keys the plain grey studio background (sampled from the border) and fills interior holes.
Layout numbers are reference pixels for the 2048 x 2048 v2 reference (dev/asset_team/prompts/item_i_survived_tshirt_ref_front_v2.txt).
"""
import sys, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

src, out_lettered, out_cut = sys.argv[1:4]
FONT = "C:/Windows/Fonts/impact.ttf"
BLUE, RED = (0x1F, 0x4F, 0xA3), (0xD4, 0x2B, 0x2B)

img = Image.open(src).convert("RGB")
W, H = img.size
base = np.asarray(img).astype(np.float32)
lum = base.mean(axis=2)
lum_b = np.asarray(Image.fromarray(lum.astype(np.uint8)).filter(ImageFilter.GaussianBlur(28))).astype(np.float32)
shade = np.clip(lum / np.maximum(lum_b, 1), 0.78, 1.12)            # folds and weave show through the ink


def text_mask(txt, width, bow=0.0, angle=0.0, spacing=0.0):
    """Antialiased mask of txt fitted to `width` px; bow > 0 sags the middle (px); angle in degrees (ccw)."""
    size = 200
    f = ImageFont.truetype(FONT, size)
    adv = [f.getlength(c) for c in txt]
    tw = sum(adv) + spacing * size * (len(txt) - 1)
    k = width / tw
    f = ImageFont.truetype(FONT, int(size * k))
    adv = [f.getlength(c) for c in txt]
    sp = spacing * size * k
    asc, desc = f.getmetrics()
    hh = asc + desc + int(abs(bow)) + 8
    m = Image.new("L", (int(width) + 8, hh), 0)
    x = 4.0
    for c, a in zip(txt, adv):
        cx = x + a / 2
        t = (cx - (width + 8) / 2) / ((width + 8) / 2)
        dy = bow * (1 - t * t)
        ch = Image.new("L", (int(a) + 6, asc + desc + 4), 0)
        ImageDraw.Draw(ch).text((3, 0), c, font=f, fill=255)
        ch = ch.rotate(-np.degrees(np.arctan(-2 * bow * t / ((width + 8) / 2))), resample=Image.BICUBIC, expand=False)
        m.paste(ch, (int(x) - 3, int(dy)), ch)
        x += a + sp
    if angle:
        m = m.rotate(angle, resample=Image.BICUBIC, expand=True)
    return m


def place(mask, cx, top):
    full = Image.new("L", (W, H), 0)
    full.paste(mask, (int(cx - mask.width / 2), int(top)))
    return full


layers = []                                                         # (mask L image, colour)
layers.append((place(text_mask("I SURVIVED THE", 600, spacing=0.06), 958, 448), BLUE))
cock = place(text_mask("COCK-UP", 1000, bow=26, spacing=0.02), 958, 505)
layers.append((cock, RED))
# DEBAUCHERYVILLE rides the swoosh: tilted to its slope, centred under its rising middle section
layers.append((place(text_mask("DEBAUCHERYVILLE", 560, angle=7.5, spacing=0.05), 1010, 1585), BLUE))

out = base.copy()
for m, col in layers:
    a = np.asarray(m).astype(np.float32)[..., None] / 255.0 * 0.96
    ink = np.array(col, np.float32)[None, None, :] * shade[..., None]
    out = out * (1 - a) + ink * a

# cracks across the red COCK-UP along the fold lines, and the red flaking at the "C"
rng = random.Random(7)
crack = Image.new("L", (W, H), 0)
d = ImageDraw.Draw(crack)
cm = np.asarray(cock) > 40
ys, xs = np.nonzero(cm)
x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
for fx in np.linspace(x0 + 40, x1 - 40, 11):                        # near-vertical fold cracks
    pts, x, y = [], fx + rng.uniform(-30, 30), y0 - 10
    while y < y1 + 10:
        pts.append((x, y)); x += rng.uniform(-22, 22); y += rng.uniform(10, 22)
    d.line(pts, fill=255, width=rng.choice([2, 3]))
    for (bx, by) in pts[1:-1:2]:                                   # short side branches
        d.line([(bx, by), (bx + rng.uniform(-40, 40), by + rng.uniform(-12, 12))], fill=255, width=2)
for fy in (y0 + (y1 - y0) * 0.45, y0 + (y1 - y0) * 0.7):           # two horizontal fold cracks
    pts, x, y = [], x0 - 10, fy
    while x < x1 + 10:
        pts.append((x, y)); y += rng.uniform(-10, 10); x += rng.uniform(16, 34)
    d.line(pts, fill=255, width=2)
cx0 = x0                                                            # flake: bite out of the first C's lower left
for _ in range(14):
    fx, fy = cx0 + rng.uniform(0, 90), y0 + (y1 - y0) * rng.uniform(0.55, 0.95)
    r = rng.uniform(6, 16)
    d.polygon([(fx + r * np.cos(t) * rng.uniform(0.6, 1.2), fy + r * np.sin(t) * rng.uniform(0.6, 1.2))
               for t in np.linspace(0, 2 * np.pi, 7)[:-1]], fill=255)
ca = (np.asarray(crack.filter(ImageFilter.GaussianBlur(0.8))).astype(np.float32) / 255.0 * cm)[..., None]
out = out * (1 - ca) + base * ca                                    # cracks show the bare fabric underneath
res = Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGB")
res.save(out_lettered)
print("COCK-UP rows", int(np.nonzero(np.asarray(cock) > 40)[0].min()), int(np.nonzero(np.asarray(cock) > 40)[0].max()))

# cut-out: key the border grey, keep the largest shape, fill its holes
border = np.concatenate([base[0], base[-1], base[:, 0], base[:, -1]])
key = np.median(border, axis=0)
dist = np.linalg.norm(np.asarray(res).astype(np.float32) - key, axis=-1)
alpha = np.clip((dist - 22) / 30, 0, 1)
hard = Image.fromarray(((alpha > 0.5) * 255).astype(np.uint8))
hard = hard.filter(ImageFilter.MaxFilter(25)).filter(ImageFilter.MinFilter(25))  # close scuff bites and pin holes
bg = hard.copy()
for corner in ((0, 0), (W - 1, 0), (0, H - 1), (W - 1, H - 1)):   # the clothesline splits the frame: fill from every corner
    if bg.getpixel(corner) == 0:
        ImageDraw.floodfill(bg, corner, 128)
fm = np.where(np.asarray(bg) == 128, 0, 255).astype(np.uint8)       # not reachable from any corner
cols = np.nonzero((fm > 0).sum(axis=0) > 150)[0]                    # "a short clothesline": shirt columns are deep, cord columns thin; stop the cord just past the sleeves
fm[:, :max(cols.min() - 40, 0)] = 0
fm[:, cols.max() + 40:] = 0
filled = Image.fromarray(fm)
alpha = np.asarray(filled.filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32) / 255.0
rgba = np.dstack([np.asarray(res), (alpha * 255).astype(np.uint8)])
Image.fromarray(rgba, "RGBA").save(out_cut)
print("WROTE", out_lettered, out_cut, "key", key.round().tolist())
