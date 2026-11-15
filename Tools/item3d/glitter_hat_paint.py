"""Paint the Used Glitter Hat atlas art (flat toon colours, bold clumps) with Pillow.

python Tools/item3d/glitter_hat_paint.py <out.png>
2048 x 320 cylinder map: x = angle (-180..180 deg), y = height (top = z 0.46). Hex values from used_glitter_hat_item.md.
"""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter

W, H, SS = 2048, 320, 2
ZTOP, BASE, AMP, P0 = 0.46, 0.12, 0.34, -118.0
PINK, GREY_PINK, GLUE = "#F7B6D2", "#DE9DBB", "#E6BDA6"
MAG, PUR, SIL = "#FF6EC7", "#9370DB", "#C0C0C8"
GEM, GEM_DK, STAIN, DARK = "#F4A7C3", "#B8708F", "#7A5C3A", "#8F6F72"
random.seed(11)
img = Image.new("RGB", (W * SS, H * SS), PINK)
d = ImageDraw.Draw(img)
S = lambda v: v * SS
PXU_Y = H / ZTOP
PXU_X = W / 3.02


def X(deg):
    return ((deg + 180) % 360) / 360.0 * W


def Y(z):
    return H - z / ZTOP * H


def ell(cx, cy, rx, ry, fill, outline=None, w=0):
    d.ellipse([S(cx - rx), S(cy - ry), S(cx + rx), S(cy + ry)], fill=fill, outline=outline, width=S(w))


# finger-grey dulling blotches
for _ in range(40):
    ell(random.uniform(0, W), random.uniform(0, H), random.uniform(30, 90), random.uniform(10, 30), GREY_PINK)

# glitter clumps: (centre deg, z, radius px x, colour mix), bare glue patches left between them
def height(deg):
    ph = ((deg - P0) / 72.0 + 0.5) % 1.0
    u, c = abs(2 * ph - 1), 0.22
    u = 1.0 - (1.0 - u)          # distance from tip is 1 - tri; tri = 1 - |2ph-1|
    tri = 1.0 - abs(2 * ph - 1)
    uu = 1.0 - tri
    f = 1.0 - uu * uu / (2 * c) if uu < c else 1.0 - uu + c / 2
    return BASE + AMP * f


clumps = []
cyc = [MAG, PUR, SIL, MAG, PUR, SIL, PUR, MAG]
n = 0
for deg in range(-205, 160, 17):
    for z in (0.07, 0.20, 0.33):
        if z + 0.06 > height(deg) or random.random() < 0.5:
            continue
        clumps.append((deg + random.uniform(-4, 4), z + random.uniform(-0.02, 0.02), random.uniform(50, 72), cyc[n % 8]))
        n += 1
# large dull bare areas where the glitter flaked off: matte glue-yellowed pink, about 40% of the front
BARE = []
for deg in range(-205, -20, 22):
    for z in (0.10, 0.24, 0.36):
        if z + 0.05 < height(deg) and random.random() < 0.7:
            BARE.append((deg + random.uniform(-6, 6), z + random.uniform(-0.03, 0.03), random.uniform(75, 125)))
for deg, z, rx in BARE:
    ell(X(deg), Y(z), rx, rx * 0.5, GLUE)
for deg, z, rx in BARE:                                   # stray flecks left behind
    for _ in range(4):
        ell(X(deg) + random.uniform(-rx, rx) * 0.8, Y(z) + random.uniform(-rx, rx) * 0.3, random.uniform(5, 8), random.uniform(5, 8), random.choice([MAG, PUR, SIL]))
for deg, z, rx, col in clumps:
    cx, cy = X(deg), Y(z)
    ry = rx * 0.55
    ell(cx, cy, rx * 0.9, ry * 0.9, GLUE if random.random() < 0.0 else col)           # solid colour core so it reads at 128
    for _ in range(int(rx * 0.3)):
        a = random.uniform(0, 6.283); rr = random.random() ** 0.6
        px, py = cx + math.cos(a) * rx * 1.05 * rr, cy + math.sin(a) * ry * 1.05 * rr
        ell(px, py, random.uniform(8, 12), random.uniform(8, 12), random.choice([MAG, PUR, SIL, col, col]))
# dark patch where glitter flaked off
ell(X(-104), Y(0.10), 50, 18, DARK)
# sweat stains along the band bottom
for deg, rx in ((-140, 70), (-110, 50), (-85, 80), (-40, 60), (-170, 50), (60, 120), (120, 90)):
    ell(X(deg), Y(0.01), rx, 26, STAIN)
# mould seam down the centre of a side point (index +2, right-back), dark thin line
d.rectangle([S(X(P0 + 144) - 4), S(Y(0.46)), S(X(P0 + 144) + 4), S(Y(0.17))], fill="#A8668A")


def gem(deg, z, big=False, cracked=False):
    cx, cy = X(deg), Y(z)
    k = 1.3 if big else 1.0
    ell(cx, cy, 52 * k, 36 * k, "#9A5E7C")
    ell(cx, cy, 44 * k, 29 * k, "#E3A3BF")                                           # duller cloudy pink
    ell(cx - 6 * k, cy - 4 * k, 34 * k, 20 * k, "#EFC4D6")                           # milky overlay
    ell(cx + 14 * k, cy + 6 * k, 20 * k, 11 * k, "#F6DCE7")                          # fingerprint smear
    for r in (6, 11, 16):
        d.arc([S(cx + (14 - r) * k), S(cy + (6 - r * 0.5) * k), S(cx + (14 + r) * k), S(cy + (6 + r * 0.5) * k)], 200, 340, fill="#C99AB2", width=S(2))
    if cracked:
        pts = [cx - 34 * k, cy - 26 * k, cx - 8 * k, cy - 4 * k, cx + 6 * k, cy - 14 * k, cx + 20 * k, cy + 6 * k, cx + 40 * k, cy + 26 * k]
        d.line([S(v) for v in pts], fill="#FFFFFF", width=S(17), joint="curve")
        d.line([S(v) for v in pts], fill="#2A1020", width=S(7), joint="curve")
        d.polygon([S(cx + 30 * k), S(cy - 30 * k), S(cx + 50 * k), S(cy - 10 * k), S(cx + 36 * k), S(cy - 8 * k), S(cx + 22 * k), S(cy - 22 * k)], fill="#8F6F72")  # chipped facet


gem(P0 - 72, 0.33)
gem(P0 + 72, 0.33)
gem(P0, 0.31, big=True, cracked=True)
img = img.resize((W, H), Image.LANCZOS)
img.save(sys.argv[1])
print("painted", sys.argv[1])
