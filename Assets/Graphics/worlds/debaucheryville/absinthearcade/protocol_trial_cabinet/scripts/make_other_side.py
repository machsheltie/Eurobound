"""Paints the cabinet's OTHER (-X) side-panel art in pure Pillow/numpy (no image tool, no AI text).
Run from the worktree root:  make_other_side.py <out_dir_for_day_night_emit> [source_dir]
Same silhouette, rim, palette and proportions as the approved side reference; different stickers; new grime.
Sticker text is typed with Windows fonts and is ONLY text found in a project doc:
  "XXX PAC-MAN" / "The Director's Cut" / "MAINTENANCE ONLY"
  <- design/worlds/debaucheryville/clawmachinemaintenanceclosetrestroom.md line 30 (line 82 also lists "XXX PAC-MAN" stickers).
All other stickers are symbol-only. No people, no nudity, no place names."""
import sys, os, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
from scipy import ndimage as ndi

PK = "Assets/Graphics/worlds/debaucheryville/absinthearcade/protocol_trial_cabinet"
OUT = sys.argv[1]
SRC = sys.argv[2] if len(sys.argv) > 2 else f"{PK}/source_references"
FONTS = os.environ.get("WIN_FONTS", "C:/Windows/Fonts")
rng = random.Random(1989)
nrng = np.random.default_rng(1989)
S = 3  # supersample for stickers


def font(n, sz):
    return ImageFont.truetype(f"{FONTS}/{n}", sz)


day = Image.open(f"{SRC}/aa_prop_cabinet_side_day.png").convert("RGBA")
night = Image.open(f"{SRC}/aa_prop_cabinet_side_night.png").convert("RGBA")
W, H = day.size
alpha = np.array(day)[..., 3]
inside = alpha > 200

# ---- body: keep the approved rim (edge band), repaint the interior with fresh grime ----
dist = ndi.distance_transform_edt(inside)
rim = inside & (dist <= 9)
d0 = np.array(day).astype(np.float32)
body_ref = np.median(d0[(dist > 12) & (d0[..., :3].sum(-1) < 150)][:, :3], axis=0)
noise = ndi.gaussian_filter(nrng.normal(0, 1, (H, W)), 6) * 9 + ndi.gaussian_filter(nrng.normal(0, 1, (H, W)), 1.2) * 4
streak = ndi.gaussian_filter(nrng.normal(0, 1, (H, W)), (22, 2)) * 11  # vertical drip streaks
body = np.clip(body_ref[None, None, :] + (noise + streak)[..., None] * np.array([1, 1, 1.15]), 0, 255)
yy = np.linspace(0, 1, H)[:, None, None]
body = body * (1 - 0.35 * yy ** 3) + np.array([46, 32, 22]) * 0.35 * yy ** 3  # rust/grime toward the foot
out = d0.copy()
out[inside & ~rim, :3] = body[inside & ~rim]
img = Image.fromarray(out.astype(np.uint8), "RGBA")


# ---- sticker helpers ----
def die_cut(art, border=5, tint=(236, 232, 218)):
    pad = border * S + 8
    w, h = art.size
    big = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    big.alpha_composite(art, (pad, pad))
    a = big.split()[3].filter(ImageFilter.MaxFilter(2 * border * S + 1))
    a = a.filter(ImageFilter.GaussianBlur(1.5)).point(lambda v: 255 if v > 90 else 0)
    base = Image.new("RGBA", big.size, tint + (255,))
    base.putalpha(a)
    base.alpha_composite(big)
    return base


def scuff(st):
    a = np.array(st).astype(np.float32)
    h, w = a.shape[:2]
    n = ndi.gaussian_filter(nrng.normal(0, 1, (h, w)), 2.5) * 40
    a[..., :3] = np.clip(a[..., :3] * 0.82 + n[..., None] * 0.5 - 8, 0, 255)
    dirt = ndi.gaussian_filter(nrng.normal(0, 1, (h, w)), 5) > 0.9
    a[dirt, :3] *= 0.45
    im = Image.fromarray(a.astype(np.uint8), "RGBA")
    dr = ImageDraw.Draw(im)
    for _ in range(rng.randint(6, 12)):
        x, y = rng.randrange(w), rng.randrange(h)
        l = rng.randint(10, 60) * S // 2
        t = rng.uniform(0, 6.28)
        dr.line([x, y, x + l * math.cos(t), y + l * math.sin(t)],
                fill=(215, 210, 195, 255) if rng.random() < .6 else (30, 25, 20, 255), width=rng.choice([1, 1, 2]))
    m = Image.new("L", im.size, 255)
    md = ImageDraw.Draw(m)
    cx, cy = rng.choice([(0, 0), (w, 0), (0, h), (w, h)])
    r = rng.randint(14, 30) * S // 2
    md.polygon([(cx, cy), (cx + (r if cx == 0 else -r), cy), (cx, cy + (r if cy == 0 else -r))], fill=0)  # peeled corner
    im.putalpha(ImageChops.multiply(im.split()[3], m))
    return im


def new(w, h, bg=(0, 0, 0, 0)):
    return Image.new("RGBA", (w * S, h * S), bg)


def poly_star(cx, cy, r1, r2, n):
    return [(cx + (r1 if i % 2 == 0 else r2) * math.sin(i * math.pi / n),
             cy - (r1 if i % 2 == 0 else r2) * math.cos(i * math.pi / n)) for i in range(2 * n)]


def mk_bolt():
    im = new(60, 80, (250, 214, 20, 255)); d = ImageDraw.Draw(im)
    d.polygon([(x * S, y * S) for x, y in [(34, 4), (10, 44), (28, 44), (20, 76), (52, 30), (33, 30), (44, 4)]], fill=(20, 20, 24, 255))
    return im


def mk_cherries():
    im = new(70, 70, (210, 28, 52, 255)); d = ImageDraw.Draw(im)
    d.line([(20 * S, 62 * S), (36 * S, 12 * S), (54 * S, 58 * S)], fill=(40, 120, 40, 255), width=4 * S)
    for cx in (20, 54):
        d.ellipse([(cx - 13) * S, 46 * S, (cx + 13) * S, 70 * S - 2], fill=(120, 6, 24, 255), outline=(255, 120, 130, 255), width=2 * S)
    d.ellipse([36 * S, 6 * S, 52 * S, 16 * S], fill=(60, 170, 60, 255))
    return im


def mk_eye():
    im = new(84, 56, (24, 20, 40, 255)); d = ImageDraw.Draw(im)
    d.ellipse([6 * S, 6 * S, 78 * S, 50 * S], fill=(245, 245, 235, 255), outline=(0, 0, 0, 255), width=3 * S)
    d.ellipse([28 * S, 12 * S, 56 * S, 44 * S], fill=(40, 200, 90, 255))
    d.ellipse([36 * S, 20 * S, 48 * S, 36 * S], fill=(0, 0, 0, 255))
    for i in range(6):
        d.line([(10 + i * 3) * S, 28 * S, (24 + i * 2) * S, (24 + i * 3) * S], fill=(200, 40, 40, 255), width=S)
    return im


def mk_crown():
    im = new(80, 64, (90, 20, 120, 255)); d = ImageDraw.Draw(im)
    d.polygon([(x * S, y * S) for x, y in [(8, 52), (4, 14), (24, 32), (40, 8), (56, 32), (76, 14), (72, 52)]],
              fill=(250, 190, 30, 255), outline=(60, 30, 0, 255), width=2 * S)
    d.rectangle([8 * S, 50 * S, 72 * S, 58 * S], fill=(250, 190, 30, 255))
    for x, y in [(4, 14), (40, 8), (76, 14)]:
        d.ellipse([(x - 5) * S, (y - 4) * S, (x + 5) * S, (y + 6) * S], fill=(230, 40, 70, 255))
    return im


def mk_dice():
    im = new(64, 64); d = ImageDraw.Draw(im)
    d.rounded_rectangle([4 * S, 4 * S, 60 * S, 60 * S], 10 * S, fill=(235, 30, 60, 255), outline=(255, 255, 255, 255), width=3 * S)
    for x, y in [(18, 18), (46, 18), (32, 32), (18, 46), (46, 46)]:
        d.ellipse([(x - 6) * S, (y - 6) * S, (x + 6) * S, (y + 6) * S], fill=(255, 255, 255, 255))
    return im


def mk_ghost():
    im = new(64, 70, (20, 10, 60, 255)); d = ImageDraw.Draw(im)
    c = (40, 220, 230, 255)
    d.pieslice([10 * S, 6 * S, 54 * S, 52 * S], 180, 360, fill=c)
    d.rectangle([10 * S, 29 * S, 54 * S, 58 * S], fill=c)
    for i in range(4):
        d.polygon([((10 + i * 11) * S, 56 * S), ((15.5 + i * 11) * S, 66 * S), ((21 + i * 11) * S, 56 * S)], fill=c)
    for x in (24, 42):
        d.ellipse([(x - 6) * S, 26 * S, (x + 6) * S, 40 * S], fill=(255, 255, 255, 255))
        d.ellipse([(x - 2) * S, 31 * S, (x + 4) * S, 39 * S], fill=(20, 40, 200, 255))
    return im


def mk_skullbones():
    im = new(80, 80, (14, 14, 14, 255)); d = ImageDraw.Draw(im)
    w = (240, 240, 225, 255)
    for a in (35, -35):
        t = math.tan(math.radians(a)) * .6
        d.line([(14 * S, (40 - 26 * t) * S), (66 * S, (40 + 26 * t) * S)], fill=w, width=6 * S)
    d.ellipse([22 * S, 12 * S, 58 * S, 48 * S], fill=w)
    d.rectangle([30 * S, 40 * S, 50 * S, 58 * S], fill=w)
    for x in (31, 49):
        d.ellipse([(x - 6) * S, 26 * S, (x + 6) * S, 38 * S], fill=(14, 14, 14, 255))
    d.polygon([(40 * S, 38 * S), (37 * S, 45 * S), (43 * S, 45 * S)], fill=(14, 14, 14, 255))
    for x in (34, 40, 46):
        d.line([x * S, 50 * S, x * S, 58 * S], fill=(14, 14, 14, 255), width=S)
    return im


def mk_target():
    im = new(70, 70); d = ImageDraw.Draw(im)
    for i, c in enumerate([(240, 240, 240), (225, 30, 40), (240, 240, 240), (225, 30, 40), (20, 20, 20)]):
        r = (33 - i * 6.5) * S
        d.ellipse([35 * S - r, 35 * S - r, 35 * S + r, 35 * S + r], fill=c + (255,))
    return im


def mk_flame():
    im = new(60, 80); d = ImageDraw.Draw(im)
    d.polygon([(x * S, y * S) for x, y in [(30, 4), (48, 30), (54, 52), (44, 74), (16, 74), (6, 52), (14, 32), (22, 40)]], fill=(255, 90, 20, 255))
    d.polygon([(x * S, y * S) for x, y in [(30, 30), (42, 52), (38, 70), (22, 70), (18, 52)]], fill=(255, 214, 40, 255))
    return im


def mk_star():
    im = new(76, 76); d = ImageDraw.Draw(im)
    d.polygon([(x * S, y * S) for x, y in poly_star(38, 40, 36, 15, 5)], fill=(40, 190, 250, 255), outline=(10, 30, 120, 255), width=3 * S)
    return im


def mk_heartbroke():
    im = new(72, 68); d = ImageDraw.Draw(im)
    c = (235, 40, 120, 255)
    d.ellipse([4 * S, 6 * S, 38 * S, 40 * S], fill=c)
    d.ellipse([34 * S, 6 * S, 68 * S, 40 * S], fill=c)
    d.polygon([(7 * S, 28 * S), (65 * S, 28 * S), (36 * S, 64 * S)], fill=c)
    d.line([(36 * S, 12 * S), (30 * S, 28 * S), (42 * S, 38 * S), (34 * S, 58 * S)], fill=(20, 10, 20, 255), width=3 * S)
    return im


def mk_text(lines, w, h, bg, fg, fonts, sizes, border=None):
    im = new(w, h, bg); d = ImageDraw.Draw(im)
    if border:
        d.rectangle([3 * S, 3 * S, (w - 3) * S, (h - 3) * S], outline=border, width=2 * S)
    tot = sum(sizes) * 1.05
    y = (h * S - tot * S) / 2
    for t, f, sz in zip(lines, fonts, sizes):
        ft = font(f, sz * S)
        bb = d.textbbox((0, 0), t, font=ft)
        d.text(((w * S - (bb[2] - bb[0])) / 2 - bb[0], y - bb[1]), t, font=ft, fill=fg)
        y += sz * S * 1.05
    return im


def mk_hazard(w, h):
    im = new(w, h, (250, 200, 0, 255)); d = ImageDraw.Draw(im)
    for x in range(-h, w + h, 16):
        d.polygon([(x * S, h * S), ((x + 8) * S, h * S), ((x + 8 + h) * S, 0), ((x + h) * S, 0)], fill=(20, 20, 20, 255))
    return im


Y = (255, 235, 90, 255)
specs = [  # (maker, scale, glows in emit)
    (lambda: mk_text(["XXX", "PAC-MAN"], 96, 56, (230, 20, 40, 255), Y, ["ariblk.ttf", "impact.ttf"], [24, 22], Y), 1.0, True),  # doc: clawmachinemaintenanceclosetrestroom.md:30,82
    (lambda: mk_text(["The Director's", "Cut"], 108, 50, (14, 14, 14, 255), Y, ["impact.ttf", "impact.ttf"], [17, 19]), 0.95, False),  # doc: ...:30
    (lambda: mk_text(["MAINTENANCE", "ONLY"], 118, 50, (250, 200, 0, 255), (20, 20, 20, 255), ["impact.ttf", "impact.ttf"], [20, 20], (20, 20, 20, 255)), 1.0, False),  # doc: ...:30
    (mk_bolt, 1.0, True), (mk_cherries, 1.0, False), (mk_eye, 1.0, True), (mk_crown, 1.0, False), (mk_dice, 0.95, False),
    (mk_ghost, 1.0, True), (mk_skullbones, 1.1, False), (mk_target, 0.9, False), (mk_flame, 0.95, True), (mk_star, 0.95, False),
    (mk_heartbroke, 1.0, False), (lambda: mk_hazard(90, 24), 1.0, False), (mk_bolt, 0.7, False), (mk_star, 0.65, False),
    (mk_dice, 0.6, False), (mk_flame, 0.7, False), (mk_ghost, 0.7, False), (lambda: mk_hazard(70, 20), 0.9, False), (mk_target, 0.65, False),
    (mk_cherries, 0.7, False), (mk_eye, 0.7, False), (mk_crown, 0.65, False), (mk_skullbones, 0.7, False), (mk_heartbroke, 0.7, False),
    (mk_bolt, 0.55, False), (mk_flame, 0.55, False), (mk_star, 0.5, False), (mk_ghost, 0.55, False), (mk_cherries, 0.55, False),
    (mk_target, 0.5, False), (mk_dice, 0.5, False), (mk_eye, 0.55, False), (mk_crown, 0.5, False), (mk_skullbones, 0.55, False),
    (lambda: mk_hazard(60, 16), 0.8, False), (mk_heartbroke, 0.55, False), (mk_bolt, 0.8, False), (mk_star, 0.8, False), (mk_flame, 0.6, False),
]

elig = ndi.binary_erosion(inside, iterations=22)
ys, xs = np.nonzero(elig)
placed = []
day_l = img.copy()
layers = []
emit_l = Image.new("RGBA", (W, H), (0, 0, 0, 0))
for idx, (maker, sc, gl) in enumerate(specs):
    st = scuff(die_cut(maker()))
    st = st.resize((max(1, int(st.width * sc / S)), max(1, int(st.height * sc / S))), Image.LANCZOS)
    ang = rng.uniform(-35, 35) if idx > 2 else rng.uniform(-14, 14)
    rot = st.rotate(ang, expand=True, resample=Image.BICUBIC)
    r = max(rot.size) / 2 * 0.62
    for tries in range(4000):
        i = rng.randrange(len(xs))
        cx, cy = int(xs[i]), int(ys[i])
        if rng.random() < .5 and cy < H * 0.35:
            continue
        if cx - rot.width / 2 < 3 or cx + rot.width / 2 > W - 3 or cy - rot.height / 2 < 3 or cy + rot.height / 2 > H - 3:
            continue
        ok = all(inside[int(np.clip(cy + dy * rot.height * .42, 0, H - 1)), int(np.clip(cx + dx * rot.width * .42, 0, W - 1))]
                 for dx in (-1, 1) for dy in (-1, 1))
        if not ok:
            continue
        if any(math.hypot(cx - px, cy - py) < (r + pr) * (0.62 if tries < 1500 else 0.42) for px, py, pr in placed):
            continue
        break
    else:
        print("could not place", idx)
        continue
    placed.append((cx, cy, r))
    pos = (int(cx - rot.width / 2), int(cy - rot.height / 2))
    layers.append((idx, rot, pos))
    if gl:
        e = np.array(rot).astype(np.float32)
        e[..., :3] *= 0.45
        emit_l.alpha_composite(Image.fromarray(e.astype(np.uint8), "RGBA"), pos)
for idx, rot, pos in sorted(layers, key=lambda t: (t[0] < 3, t[0])):   # lettering stickers (0-2) composited last, fully on top
    sh = Image.new("RGBA", rot.size, (0, 0, 0, 0))
    sh.putalpha(rot.split()[3].point(lambda v: int(v * 0.6)))
    sh = sh.filter(ImageFilter.GaussianBlur(2))
    day_l.alpha_composite(sh, (pos[0] + 2, pos[1] + 3))
    day_l.alpha_composite(rot, pos)
print("placed", len(placed), "of", len(specs))

a_final = np.array(day.split()[3])
dayo = np.array(day_l)
# overall grime over stickers and body: smudge blotches + drips from the foot (painted, flat)
gr = ndi.gaussian_filter(nrng.normal(0, 1, (H, W)), 9) * 1.0 + ndi.gaussian_filter(nrng.normal(0, 1, (H, W)), (30, 1.5)) * 1.4
gr = np.clip(gr, 0, None); gr = gr / (gr.max() + 1e-6)
fac = 1 - 0.5 * gr[..., None] * (0.4 + 0.6 * np.linspace(0, 1, H)[:, None, None])
dayo[..., :3] = np.clip(dayo[..., :3].astype(np.float32) * fac, 0, 255).astype(np.uint8)
dayo[rim] = np.array(day)[rim]  # keep the approved rim crisp

# night: the same per-channel linear relation the approved side has (fit day -> night on opaque pixels)
dd = np.array(day).astype(np.float32)
nn = np.array(night).astype(np.float32)
m = a_final > 200
coef = [np.polyfit(dd[m][::7, c], nn[m][::7, c], 1) for c in range(3)]
nout = dayo.astype(np.float32)
for c in range(3):
    nout[..., c] = np.clip(dayo[..., c] * coef[c][0] + coef[c][1], 0, 255)

# emit: derived from the new day the way the approved emit relates to its day: near-black, a FAINT copy of sticker colour
# (not body, not white vinyl border) with a few slightly brighter stickers; gain fitted so mean matches the approved emit.
ae = np.array(Image.open(f"{SRC}/aa_prop_cabinet_side_emit.png").convert("RGBA"))
tgt_mean = ae[..., :3][a_final > 200].mean()
base = dayo[..., :3].astype(np.float32)
sat = base.max(-1) - base.min(-1)
art = (sat > 70) & (base.max(-1) > 90)                       # saturated sticker ink only
art &= ~np.array(dist <= 9)                                  # never the rim
gain = ndi.gaussian_filter(nrng.uniform(0.4, 1.6, (H, W)), 14) * 1.0   # patchy: some stickers a little brighter
gain = gain / gain.mean()
eo = np.zeros_like(dayo)
e = base * art[..., None] * gain[..., None]
k = tgt_mean * m.size / max(1.0, (e[m].sum() / 3.0 * 1.0)) if False else tgt_mean / max(1e-6, e[m].mean())
eo[..., :3] = np.clip(e * k, 0, 140).astype(np.uint8)
print("emit mean new", eo[..., :3][m].mean().round(2), "approved", round(float(tgt_mean), 2))

os.makedirs(OUT, exist_ok=True)
for name, arr in (("day", dayo), ("night", nout.astype(np.uint8)), ("emit", eo)):
    arr = arr.copy()
    arr[..., 3] = a_final
    Image.fromarray(arr, "RGBA").save(f"{OUT}/aa_prop_cabinet_side_other_{name}.png")
print("fit coef", [tuple(round(float(v), 3) for v in c) for c in coef])
