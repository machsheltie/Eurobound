"""Round 3 of the cabinet's OTHER (-X) side art: painterly sticker panel generated in Adobe Firefly (Gemini 3.1 / Nano Banana 2, free plan,
no payment), composited into the approved side's exact silhouette; ONE lettering sticker typed with Pillow.
Run from the worktree root:  make_other_side_r3.py <firefly_raw_png> <out_dir> [source_dir]
Firefly prompt (symbols only, no text asked for): painterly, brush-textured, grimy black arcade-cabinet panel, upper 40 percent bare,
dense peeling die-cut sticker cluster in the lower 60 percent (bolts, cherries, ghost, crown, dice, flaming skull, eyeball, hazard stripes,
broken heart, target, stars, flame, mushroom, lips), 9:16 vertical.
Lettering: "XXX PAC-MAN: The Director's Cut" exactly as design/worlds/debaucheryville/clawmachinemaintenanceclosetrestroom.md line 30 (line 82 also).
"MAINTENANCE ONLY" is dropped: line 30 puts it on a door label, not on a sticker."""
import sys, os, math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
from scipy import ndimage as ndi

PK = "Assets/Graphics/worlds/debaucheryville/absinthearcade/protocol_trial_cabinet"
RAW, OUT = sys.argv[1], sys.argv[2]
SRC = sys.argv[3] if len(sys.argv) > 3 else f"{PK}/source_references"
FONTS = os.environ.get("WIN_FONTS", "C:/Windows/Fonts")
CM = os.environ.get("CABINET_MIRROR", "")
MIRROR = CM == "1"      # Phase B option A: the art as seen FROM -X (front on the right): silhouette AND cluster mirrored, lettering NOT mirrored (reads correctly)
ALT = CM == "alt"       # Phase B option B: silhouette mirrored, cluster placed AS DRAWN in the approved art (not mirrored), lettering as drawn (reads correctly)
SIL = MIRROR or ALT
rng = random.Random(1990)
nrng = np.random.default_rng(1990)

day = Image.open(f"{SRC}/aa_prop_cabinet_side_day.png").convert("RGBA")
night = Image.open(f"{SRC}/aa_prop_cabinet_side_night.png").convert("RGBA")
if SIL:
    from PIL import ImageOps
    day, night = ImageOps.mirror(day), ImageOps.mirror(night)
W, H = day.size
a_final = np.array(day)[..., 3]
inside = a_final > 200
dist = ndi.distance_transform_edt(inside)
rim = inside & (dist <= 9)

# ---- panel: crop the Firefly cabinet's inner panel (no frame), scale uniformly to 383x740, drop it 40 px so the cluster sits low ----
raw = Image.open(RAW).convert("RGB")
crop = raw.crop((68, 136, 700, 1356)).resize((W, H), Image.LANCZOS)
if MIRROR:
    crop = ImageOps.mirror(crop)
SHIFT = 40
panel = Image.new("RGB", (W, H))
panel.paste(crop, (0, SHIFT))
top = crop.crop((0, 40, W, 40 + SHIFT)).transpose(Image.FLIP_TOP_BOTTOM)   # bare dark panel to fill the gap, mirrored
panel.paste(top, (0, 0))
p = np.array(panel).astype(np.float32)

# ---- extra grime: soot blotches, vertical drips from the foot, darkened stickers toward the bottom ----
gr = ndi.gaussian_filter(nrng.normal(0, 1, (H, W)), 7) + ndi.gaussian_filter(nrng.normal(0, 1, (H, W)), (34, 1.6)) * 1.4
gr = np.clip(gr, 0, None); gr /= gr.max() + 1e-6
fac = 1 - 0.42 * gr[..., None] * (0.35 + 0.65 * np.linspace(0, 1, H)[:, None, None])
p *= fac
# fine scuff speckle
sp = ndi.gaussian_filter(nrng.normal(0, 1, (H, W)), 0.8)
p += (sp * 9)[..., None]
panel = Image.fromarray(np.clip(p, 0, 255).astype(np.uint8))
dr = ImageDraw.Draw(panel)
for _ in range(70):   # scratches
    x, y = rng.randrange(W), rng.randrange(H); l = rng.randint(8, 40); t = rng.uniform(0, 6.28)
    dr.line([x, y, x + l * math.cos(t), y + l * math.sin(t)], fill=(150, 145, 135) if rng.random() < .55 else (14, 12, 10), width=1)

# ---- the one lettering sticker (Pillow type, then painted over so it sits in the painterly style) ----
S = 4
def lettering():
    w, h = 176, 74
    im = Image.new("RGBA", (w * S, h * S), (214, 28, 44, 255)); d = ImageDraw.Draw(im)
    d.rectangle([4 * S, 4 * S, (w - 4) * S, (h - 4) * S], outline=(255, 232, 96, 255), width=2 * S)
    def line(t, f, sz, y, fill):
        ft = ImageFont.truetype(f"{FONTS}/{f}", sz * S)
        bb = d.textbbox((0, 0), t, font=ft); x = (w * S - (bb[2] - bb[0])) / 2 - bb[0]
        for ox, oy in [(-2, 0), (2, 0), (0, -2), (0, 2), (2, 2), (-2, 2), (2, -2), (-2, -2)]:
            d.text((x + ox * S / 2, y - bb[1] + oy * S / 2), t, font=ft, fill=(20, 10, 10, 255))   # chunky black outline
        d.text((x, y - bb[1]), t, font=ft, fill=fill)
    line("XXX PAC-MAN:", "ariblk.ttf", 21, 9 * S, (255, 232, 96, 255))
    line("The Director's Cut", "impact.ttf", 22, 38 * S, (255, 255, 255, 255))
    # die-cut white border
    pad = 6 * S
    big = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0)); big.alpha_composite(im, (pad, pad))
    a = big.split()[3].filter(ImageFilter.MaxFilter(2 * 4 * S + 1)).filter(ImageFilter.GaussianBlur(1.5)).point(lambda v: 255 if v > 90 else 0)
    st = Image.new("RGBA", big.size, (238, 232, 214, 255)); st.putalpha(a); st.alpha_composite(big)
    st = st.resize((st.width // S, st.height // S), Image.LANCZOS)
    # painterly treatment: median + posterise-ish smoothing, brush-direction smear, colour jitter, grime, scratches
    rgb = st.convert("RGB").filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.SMOOTH)
    arr = np.array(rgb).astype(np.float32)
    arr = ndi.gaussian_filter(arr, (0.6, 0.6, 0)) * 0.55 + arr * 0.45
    arr *= (0.86 + ndi.gaussian_filter(nrng.normal(0, 1, arr.shape[:2]), 3)[..., None] * 0.35)
    dirt = ndi.gaussian_filter(nrng.normal(0, 1, arr.shape[:2]), 4) > 0.8
    arr[dirt] *= 0.5
    out = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA"); out.putalpha(st.split()[3])
    d2 = ImageDraw.Draw(out)
    for _ in range(14):
        x, y = rng.randrange(out.width), rng.randrange(out.height); l = rng.randint(6, 26); t = rng.uniform(-.5, .5)
        d2.line([x, y, x + l * math.cos(t), y + l * math.sin(t)], fill=(228, 222, 206, 255) if rng.random() < .65 else (30, 20, 16, 255), width=1)
    return out
lt = lettering().rotate(4 if MIRROR else -4, expand=True, resample=Image.BICUBIC)
lt = lt.resize((int(lt.width * 0.86), int(lt.height * 0.86)), Image.LANCZOS)
# place on the bare upper body just above the cluster, fully inside the silhouette (6 px margin), nothing covers it
safe = ndi.binary_erosion(inside, iterations=7)
la = np.array(lt.split()[3]) > 40
LT_POS = None
if ALT and safe[270:270 + lt.height, 102:102 + lt.width][la[:, :]].all():
    LT_POS = (102, 270)   # as drawn
if MIRROR and not LT_POS and safe[270:270 + lt.height, W - lt.width - 102:W - 102][la[:, :]].all():
    LT_POS = (W - lt.width - 102, 270)   # mirror of the approved position
for ty in range(250, 340, 2):
    for tx in ([] if LT_POS else range(60, W - lt.width, 2)):
        if safe[ty:ty + lt.height, tx:tx + lt.width][la].all():
            LT_POS = (tx, ty); break
    if LT_POS: break
assert LT_POS, "lettering does not fit"
print("lettering at", LT_POS, "size", lt.size)
sh = Image.new("RGBA", lt.size, (0, 0, 0, 0)); sh.putalpha(lt.split()[3].point(lambda v: int(v * .6))); sh = sh.filter(ImageFilter.GaussianBlur(2))
pr = panel.convert("RGBA")
pr.alpha_composite(sh, (LT_POS[0] + 2, LT_POS[1] + 3)); pr.alpha_composite(lt, LT_POS)

# ---- clip to the approved silhouette; the approved rim stays as it is ----
dayo = np.array(pr)
dayo[..., 3] = a_final
dayo[rim] = np.array(day)[rim]

# ---- night: same per-channel linear fit (approved day -> approved night) ----
dd = np.array(day).astype(np.float32); nn = np.array(night).astype(np.float32); m = a_final > 200
coef = [np.polyfit(dd[m][::7, c], nn[m][::7, c], 1) for c in range(3)]
nout = dayo.astype(np.float32)
for c in range(3):
    nout[..., c] = np.clip(dayo[..., c] * coef[c][0] + coef[c][1], 0, 255)

# ---- emit: near-black, a FEW small bright neon hot-spots on selected stickers (saturated ink only) ----
def to_out(hx, hy):   # Firefly half-res coords -> output px
    return ((W - (hx * 2 - 68) * W / 632.0) if MIRROR else (hx * 2 - 68) * W / 632.0, (hy * 2 - 136) * H / 1220.0 + SHIFT)
spots = [to_out(190, 375), to_out(252, 456), to_out(310, 410), to_out(68, 355), to_out(160, 596), to_out(255, 330), to_out(100, 465)]   # ghost, eyeball, flame-skull, bolt, flame
spots_r = [26, 22, 24, 20, 24, 18, 22]
base = dayo[..., :3].astype(np.float32)
sat = base.max(-1) - base.min(-1)
ink = (sat > 80) & (base.max(-1) > 120) & ~(dist <= 9)
yy, xx = np.mgrid[0:H, 0:W]
hot = np.zeros((H, W), np.float32)
for (cx, cy), r in zip(spots, spots_r):
    hot = np.maximum(hot, np.clip(1.15 - np.hypot(xx - cx, yy - cy) / r, 0, 1))
# lettering sticker: its yellow border/text glows a little too
lx0, ly0 = LT_POS
txt = np.zeros((H, W), bool); txt[ly0:ly0 + lt.height, lx0:lx0 + lt.width] = (base[ly0:ly0 + lt.height, lx0:lx0 + lt.width, 0] > 215) & (base[ly0:ly0 + lt.height, lx0:lx0 + lt.width, 2] < 140) & (base[ly0:ly0 + lt.height, lx0:lx0 + lt.width, 1] > 190)
eo = np.zeros_like(dayo)
e = base * ink[..., None] * hot[..., None] * 0.8
eo[..., :3] = np.clip(e, 0, 146).astype(np.uint8)
ae = np.array(Image.open(f"{SRC}/aa_prop_cabinet_side_emit.png").convert("RGBA"))
print("emit mean new %.2f approved %.2f  max new %d approved %d" % (eo[..., :3][m].mean(), ae[..., :3][m].mean(), eo[..., :3].max(), ae[..., :3].max()))

os.makedirs(OUT, exist_ok=True)
for name, arr in (("day", dayo), ("night", nout.astype(np.uint8)), ("emit", eo)):
    arr = arr.copy(); arr[..., 3] = a_final
    Image.fromarray(arr, "RGBA").save(f"{OUT}/aa_prop_cabinet_side_other_{'mirror_' if MIRROR else 'alt_' if ALT else ''}{name}.png")
print("night fit", [tuple(round(float(v), 3) for v in c) for c in coef])
