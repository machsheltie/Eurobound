"""Phase B (revision) projection prep. Supersedes prep_projection.py + prep_pbr_refs.py for the revised pass. Run from the repo/worktree root with a python that has numpy, cv2, PIL, scipy:
  prep_projection_b.py <tmp_dir> <rebuilt_day_glb> <rebuilt_emit_glb> <rebuilt_orm_glb>
Env: PAINT_ZONES_WORK = shared SAM work folder (the zone masks; machine-specific).
What changed against the first pass:
 * References are enlarged 3x (Lanczos, no AI) BEFORE sampling, and the SAM masks 3x (bilinear, threshold), so the projection samples a smooth high-resolution
   image into the 3072 atlas instead of a 400 px/m image into 2048 texels. Unsharp mask is applied inside each zone mask only (project_ref `sharpen`),
   stronger on the coin door and the sticker zones. Bilinear sampling everywhere. The atlas is written lossless (project_ref `lossless`), not JPEG q92.
 * The -X flank uses the new approved other-side art (source_references/aa_prop_cabinet_side_other_mirror_*.png: painted as seen FROM -X so the lettering
   reads correctly), one full-silhouette pass, no mirror of the +X side.
 * Value maps (R sticker relief height, G roughness, B metallic): coin door is now metal (metallic 0.85, roughness 0.38, ASSUMED); the -X sticker mask is derived from the new art.
B2 round (after the blind nhxz.8 review): unsharp radius 1.6, percent 30-70, threshold 0.03 and a local min/max clamp (no halos); coin-door METAL TRIM (slot bezels, locks, hinges, coin-return frame) is its own zone: metallic 1.0, roughness 0.28, relief for edge highlights, albedo lifted to dark steel; the door body stays black matte. Left art prefix via env LEFT_ART (side_other_mirror = option A, side_other_alt = option B).
Derived images are pixel copies of the canonical references, used only as sampling input."""
import sys, os, json, shutil
import numpy as np, cv2
from PIL import Image
from scipy import ndimage as ndi
PK = "Assets/Graphics/worlds/debaucheryville/absinthearcade/protocol_trial_cabinet"
SAMW = os.environ.get("PAINT_ZONES_WORK", "tools/paint_zones/work")
T, GLB_DAY, GLB_EMIT, GLB_ORM = sys.argv[1:5]
UP = 3
LEFT = os.environ.get("LEFT_ART", "side_other_mirror")
for d in ("masks", "ref"):
    os.makedirs(f"{T}/{d}", exist_ok=True)
ABS = os.path.abspath(".").replace("\\", "/")
R = f"{PK}/source_references/aa_prop_cabinet_"


def flat(src, bg, mirror=False):
    im = np.array(Image.open(src).convert("RGBA"))
    out = np.where((im[..., 3:4] > 16), im[..., :3], np.array(bg, np.uint8)).astype(np.uint8)
    return out


def up(rgb):
    return np.array(Image.fromarray(rgb).resize((rgb.shape[1] * UP, rgb.shape[0] * UP), Image.LANCZOS))


def save_ref(name, rgb):
    Image.fromarray(up(rgb)).save(f"{T}/ref/{name}.png")


save_ref("front_day", flat(R + "front_day.png", (255, 255, 255)))
save_ref("front_emit", flat(R + "front_emit.png", (0, 0, 0)))
save_ref("side_day", flat(R + "side_day.png", (255, 255, 255)))
save_ref("side_emit", flat(R + "side_emit.png", (0, 0, 0)))
save_ref("left_day", flat(R + f"{LEFT}_day.png", (255, 255, 255)))
save_ref("left_emit", flat(R + f"{LEFT}_emit.png", (0, 0, 0)))


def er(m, n=1):
    return cv2.erode(m.astype(np.uint8), np.ones((2 * n + 1, 2 * n + 1), np.uint8)).astype(bool)


def load(asset, z):
    return np.array(Image.open(f"{SAMW}/{asset}/masks/{z}.png").convert("L")) > 127


def save_mask(name, m):
    big = cv2.resize(m.astype(np.float32), (m.shape[1] * UP, m.shape[0] * UP), interpolation=cv2.INTER_LINEAR) > 0.5
    Image.fromarray((big * 255).astype(np.uint8)).save(f"{T}/masks/{name}.png")
    return f"{T}/masks/{name}.png"


fa = np.array(Image.open(R + "front_day.png").convert("RGBA"))[..., 3] > 128
sa = np.array(Image.open(R + "side_day.png").convert("RGBA"))[..., 3] > 128
la = np.array(Image.open(R + f"{LEFT}_day.png").convert("RGBA"))[..., 3] > 128
# coin-door metal trim in front-reference px (read off the 4x crop of the reference, origin 90,470): slot bezel rings, lock circles, hinge strips, coin-return frame ring
def trim_mask():
    m = np.zeros((740, 290), np.uint8)
    X = lambda px: 90 + px / 4.0
    Yv = lambda py: 470 + py / 4.0
    def ring(x0, y0, x1, y1, w=3.5):
        a = (int(round(X(x0))), int(round(Yv(y0))), int(round(X(x1))), int(round(Yv(y1))))
        cv2.rectangle(m, (a[0], a[1]), (a[2], a[3]), 1, -1)
        cv2.rectangle(m, (int(a[0] + w), int(a[1] + w)), (int(a[2] - w), int(a[3] - w)), 0, -1)
    for r in [(120, 88, 208, 188), (228, 88, 318, 188), (112, 335, 208, 428), (226, 335, 318, 428)]:
        ring(*r)
    for c in [(333, 257), (333, 668)]:
        cv2.circle(m, (int(round(X(c[0]))), int(round(Yv(c[1])))), 6, 1, -1)
    for r in [(62, 118, 76, 395), (62, 535, 76, 800)]:
        cv2.rectangle(m, (int(X(r[0])), int(Yv(r[1]))), (int(X(r[2])), int(Yv(r[3]))), 1, -1)
    ring(78, 480, 372, 868, 3.0)
    return m.astype(bool)
TRIM = trim_mask()
_d = flat(R + "front_day.png", (255, 255, 255)).astype(np.float32)
_l = (_d @ np.array([0.299, 0.587, 0.114], np.float32) / 255.0)[..., None]
_steel = np.array([190, 192, 198], np.float32) * np.clip(0.62 + 0.8 * _l, 0, 1)   # dark steel (F0 about 0.2-0.4 linear) keeping the painted shading
_dm = np.where(TRIM[..., None], 0.25 * _d + 0.75 * _steel, _d)
save_ref("front_day_metal", np.clip(_dm, 0, 255).astype(np.uint8))
FZ = ["marquee", "crt_bezel", "control_panel", "lower_fascia", "coin_door", "kick_panel_stickers", "rail_left", "rail_right"]
sil2 = er(fa, 1)
fm = {z: er(load("cabinet_trial_front", z)) & sil2 for z in FZ}
rest = sil2 & ~np.any([fm[z] for z in FZ], axis=0)
rest = cv2.morphologyEx(rest.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)).astype(bool)
deck_rows = np.zeros_like(rest); deck_rows[336:404, :] = True
fm["front_rest_deck"] = rest & deck_rows
fm["front_rest"] = rest & ~deck_rows
fm["front_all"] = sil2
fm["coin_trim"] = TRIM & sil2
fm["rail_right_fix"] = cv2.dilate(load("cabinet_trial_front", "rail_right").astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool) & sil2
SZ = ["side_trim", "side_stickers", "side_body"]
sm = {z: er(load("cabinet_trial_side", z), 1 if z != "side_trim" else 0) for z in SZ}
sm["side_rest"] = er(sa, 1) & ~np.any([sm[z] for z in SZ], axis=0)
sm["side_all"] = er(sa, 1)
lm = {"left_all": er(la, 1)}

# unsharp [radius in enlarged px, percent], inside each mask only. Stronger where the blind review saw softness (coin door, stickers).
SHARP = {"front_all": [1.6, 30], "front_rest": [1.6, 40], "front_rest_deck": [1.6, 40], "lower_fascia": [1.6, 40], "marquee": [1.6, 60], "crt_bezel": [1.6, 50],
         "control_panel": [1.6, 55], "coin_door": [1.6, 70], "coin_trim": [1.6, 50], "kick_panel_stickers": [1.6, 70], "rail_left": [1.6, 35], "rail_right": [1.6, 35], "rail_right_fix": [1.6, 35],
         "side_all": [1.6, 30], "side_rest": [1.6, 40], "side_body": [1.6, 40], "side_stickers": [1.6, 70], "side_trim": [1.6, 40], "left_all": [1.6, 60]}
FEATHER = 2 * UP
cfgs = {}
for kind in ("day", "emit"):
    views = []
    order = ["front_all", "front_rest", "front_rest_deck", "lower_fascia", "marquee", "crt_bezel", "control_panel", "coin_door", "coin_trim", "kick_panel_stickers", "rail_left", "rail_right", "rail_right_fix"]
    for z in order:
        v = {"ref": f"{T}/ref/front_{kind}.png", "crop": [0, 0, 290 * UP, 740 * UP], "side": "front", "mask_png": save_mask(f"front_{z}", fm[z]), "feather": FEATHER,
             "ndot": 0.2 if z == "front_all" else 0.1 if z == "rail_right_fix" else 0.25 if z in ("control_panel", "front_rest_deck") else 0.5, "bilinear": True, "_zone": z}
        if kind == "day":
            v["sharpen"] = SHARP[z]; v["sharpen_thr"] = 0.03; v["sharpen_clamp"] = 2
            if z == "coin_trim":
                v["ref"] = f"{T}/ref/front_day_metal.png"
        views.append(v)
    for side_name, zones, mset, refn in (("right", ["side_all", "side_rest", "side_body", "side_stickers", "side_trim"], sm, f"side_{kind}"), ("left", ["left_all"], lm, f"left_{kind}")):
        for z in zones:
            v = {"ref": f"{T}/ref/{refn}.png", "crop": [0, 0, 383 * UP, 740 * UP], "side": side_name, "mask_png": save_mask(f"{side_name}_{z}", mset[z]), "feather": FEATHER, "ndot": 0.5,
                 "bilinear": True, "_zone": z, "clip": {"axis": "x", "min": 0.3615} if side_name == "right" else {"axis": "x", "max": -0.3615}}
            if kind == "day":
                v["sharpen"] = SHARP[z]; v["sharpen_thr"] = 0.03; v["sharpen_clamp"] = 2
            views.append(v)
    cfgs[kind] = views

# ---- value maps for the ORM pass: R sticker relief height, G roughness, B metallic (ASSUMED values, not measured) ----
FRONT = [("__bg", (0, .75, 0)), ("lower_fascia", (0, .8, 0)), ("marquee", (0, .3, 0)), ("crt_bezel", (0, .55, 0)), ("crt_screen", (0, .08, 0)),
         ("control_panel", (0, .5, 0)), ("joystick_red", (0, .35, 0)), ("coin_door", (0, .45, 0)), ("__trim", (1, .28, 1.0)), ("kick_panel_stickers", (0, .35, 0)),
         ("rail_left", (0, .5, 0)), ("rail_right", (0, .5, 0))]
SIDE = [("__bg", (0, .8, 0)), ("side_trim", (0, .5, 0)), ("side_stickers", (1, .3, 0))]


def comp(asset, zones, size):
    out = np.zeros((size[1], size[0], 3), np.float32)
    for z, (h, r, m) in zones:
        mk = np.ones((size[1], size[0]), bool) if z == "__bg" else TRIM if z == "__trim" else load(asset, z)
        out[mk] = (h, r, m)
    return (out * 255).round().astype(np.uint8)


def upn(a):
    return np.array(Image.fromarray(a).resize((a.shape[1] * UP, a.shape[0] * UP), Image.NEAREST))


Image.fromarray(upn(comp("cabinet_trial_front", FRONT, (290, 740)))).save(f"{T}/ref/front_value.png")
Image.fromarray(upn(comp("cabinet_trial_side", SIDE, (383, 740)))).save(f"{T}/ref/side_value.png")
# -X flank: sticker mask derived from the new art itself (saturated ink or white vinyl border, holes closed, specks removed); assumed values as the +X sticker zone
art = np.array(Image.open(R + f"{LEFT}_day.png").convert("RGBA")).astype(np.float32)
mx, mn = art[..., :3].max(-1), art[..., :3].min(-1)
stk = (((mx - mn) > 60) | (mn > 120)) & la
stk = ndi.binary_closing(stk, iterations=3); stk = ndi.binary_fill_holes(stk)
lab, n = ndi.label(stk); sz = ndi.sum(stk, lab, range(1, n + 1)); stk = np.isin(lab, [i + 1 for i, s_ in enumerate(sz) if s_ > 40])
lv = np.zeros((740, 383, 3), np.float32); lv[...] = (0, .8, 0); lv[stk] = (1, .3, 0)
Image.fromarray(upn((lv * 255).round().astype(np.uint8))).save(f"{T}/ref/left_value.png")
orm_views = []
for v in cfgs["day"]:
    v = dict(v); v.pop("sharpen", None); v["bilinear"] = False
    v["ref"] = f"{T}/ref/" + ("front_value.png" if v["side"] == "front" else "side_value.png" if v["side"] == "right" else "left_value.png")
    orm_views.append(v)
cfgs["orm"] = orm_views
for kind, g in (("day", GLB_DAY), ("emit", GLB_EMIT), ("orm", GLB_ORM)):
    gg = f"{T}/cab_{kind}.glb"; shutil.copy(g, gg)
    json.dump({"glb": gg, "out_glb": f"{T}/cab_{kind}_proj.glb", "report": f"{T}/report_{kind}.json", "reliable_iou": 0.85, "lossless": True, "views": cfgs[kind]}, open(f"{T}/cfg_{kind}.json", "w"), indent=1)
print("prepped", {k: len(v) for k, v in cfgs.items()}, "left sticker share", round(float(stk.sum() / la.sum()), 3))
