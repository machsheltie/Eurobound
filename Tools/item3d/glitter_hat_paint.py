"""Paint the Used Glitter Hat atlas art (flat toon colours, bold clumps) with Pillow.

python Tools/item3d/glitter_hat_paint.py <out.png>
2048 x 320 cylinder map: x = angle (-180..180 deg), y = height (top = z 0.46). Hex values from used_glitter_hat_item.md.
"""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter

W, H, SS = 2048, 320, 2
ZTOP, BASE, AMP, P0 = 0.46, 0.12, 0.34, -118.0
PINK, GREY_PINK, GLUE = "#F7B6D2", "#E5A9C3", "#D9B9C6"
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
        if z + 0.06 > height(deg) or random.random() < 0.22:
            continue
        clumps.append((deg + random.uniform(-4, 4), z + random.uniform(-0.02, 0.02), random.uniform(50, 72), cyc[n % 8]))
        n += 1
for deg, z, rx, col in clumps:
    cx, cy = X(deg), Y(z)
    ry = rx * 0.55
    ell(cx, cy, rx * 0.9, ry * 0.9, GLUE if random.random() < 0.0 else col)           # solid colour core so it reads at 128
    for _ in range(int(rx * 0.3)):
        a = random.uniform(0, 6.283); rr = random.random() ** 0.6
        px, py = cx + math.cos(a) * rx * 1.05 * rr, cy + math.sin(a) * ry * 1.05 * rr
        ell(px, py, random.uniform(8, 12), random.uniform(8, 12), random.choice([MAG, PUR, SIL, col, col]))
# bare worn patches (glue showing)
for deg, z, rx in ((-125, 0.26, 40), (-100, 0.28, 35), (-62, 0.22, 40), (-24, 0.18, 35), (-150, 0.14, 40)):
    ell(X(deg), Y(z), rx * 0.8, rx * 0.4, GLUE)
# dark patch where glitter flaked off
ell(X(-104), Y(0.10), 50, 18, DARK)
# sweat stains along the band bottom
for deg, rx in ((-140, 70), (-110, 50), (-85, 80), (-40, 60), (-170, 50), (60, 120), (120, 90)):
    ell(X(deg), Y(0.01), rx, 26, STAIN)
# mould seam down the centre of one point (front point), a dark thin line
d.rectangle([S(X(P0) - 4), S(Y(0.46)), S(X(P0) + 4), S(Y(0.17))], fill="#C07A9D")


def gem(deg, z, cracked=False):
    cx, cy = X(deg), Y(z)
    ell(cx, cy, 52, 36, GEM_DK)
    ell(cx, cy, 44, 29, GEM)
    ell(cx - 14, cy - 10, 14, 7, "#FFFFFF")
    ell(cx + 12, cy + 8, 8, 5, "#E58BB0")                                               # fingerprint smudge
    if cracked:
        d.line([S(cx - 30), S(cy - 22), S(cx - 4), S(cy), S(cx + 8), S(cy - 8), S(cx + 34), S(cy + 22)], fill="#4A2A3A", width=S(5))


gem(P0, 0.33)
gem(P0 - 72, 0.33, True)
gem(P0 + 72, 0.33)


def sparkle(cx, cy, r):
    d.polygon([S(cx), S(cy - r), S(cx + r * 0.18), S(cy - r * 0.18), S(cx + r), S(cy), S(cx + r * 0.18), S(cy + r * 0.18),
               S(cx), S(cy + r), S(cx - r * 0.18), S(cy + r * 0.18), S(cx - r), S(cy), S(cx - r * 0.18), S(cy - r * 0.18)], fill="#FFFFFF")


for deg, z, r in ((-128, 0.44, 22), (-104, 0.30, 26), (-84, 0.34, 20), (-148, 0.22, 24), (-58, 0.22, 24), (-36, 0.12, 20),
                  (-172, 0.30, 20), (-112, 0.10, 20), (-20, 0.36, 18), (-92, 0.22, 20)):
    sparkle(X(deg), Y(z), r)
img = img.resize((W, H), Image.LANCZOS)
img.save(sys.argv[1])
print("painted", sys.argv[1])
