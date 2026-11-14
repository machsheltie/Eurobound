"""Prepares the step-6 projection inputs and configs. Run with the paint_zones venv python from the worktree root:
  prep_projection.py <work_dir_with_masks_parent> <tmp_dir>
Writes (in <tmp_dir>): derived refs (flat on white, side mirrored for the -X face), 1 px eroded masks, projection configs for colour and emission.
Derived images are role "derived": pixel copies of the canonical refs (opaque area identical), used only as sampling input; the canonical PNGs are untouched."""
import sys, os, json
import numpy as np, cv2
from PIL import Image
PK = "Assets/Graphics/worlds/debaucheryville/absinthearcade/protocol_trial_cabinet"
SAMW = os.environ.get("PAINT_ZONES_WORK", "tools/paint_zones/work")   # machine-specific: set PAINT_ZONES_WORK to the shared SAM work folder
T = sys.argv[1]
os.makedirs(f"{T}/masks", exist_ok=True); os.makedirs(f"{T}/ref", exist_ok=True)
ABS = os.path.abspath(".").replace("\\", "/")

def flat(src, bg, flip=False):
    """Canonical RGBA -> RGB for sampling. Where alpha > 16 the STRAIGHT rgb is kept (the true edge colour, no white/black fringe from compositing); only fully transparent pixels take bg."""
    im = np.array(Image.open(src).convert("RGBA")); out = np.where((im[..., 3:4] > 16), im[..., :3], np.array(bg, np.uint8)).astype(np.uint8)
    out = Image.fromarray(out)
    return out.transpose(Image.FLIP_LEFT_RIGHT) if flip else out

R = f"{PK}/source_references/aa_prop_cabinet_"
for v in ("front", "side"):
    flat(R + f"{v}_day.png", (255, 255, 255)).save(f"{T}/ref/{v}_day_flat.png")
    flat(R + f"{v}_emit.png", (0, 0, 0)).save(f"{T}/ref/{v}_emit_flat.png")
flat(R + "side_day.png", (255, 255, 255), True).save(f"{T}/ref/side_day_flat_mirror.png")
flat(R + "side_emit.png", (0, 0, 0), True).save(f"{T}/ref/side_emit_flat_mirror.png")

def er(m, n=1):
    return cv2.erode(m.astype(np.uint8), np.ones((2 * n + 1, 2 * n + 1), np.uint8)).astype(bool)

def load(asset, z):
    return np.array(Image.open(f"{SAMW}/{asset}/masks/{z}.png").convert("L")) > 127

def save(name, m):
    Image.fromarray((m * 255).astype(np.uint8)).save(f"{T}/masks/{name}.png"); return f"{T}/masks/{name}.png"

fa = np.array(Image.open(R + "front_day.png").convert("RGBA"))[..., 3] > 128
sa = np.array(Image.open(R + "side_day.png").convert("RGBA"))[..., 3] > 128
FZ = ["marquee", "crt_bezel", "control_panel", "lower_fascia", "coin_door", "kick_panel_stickers", "rail_left", "rail_right"]
sil2 = er(fa, 1)   # 1 px off the silhouette (fringe handled by straight-rgb flattening)
fm = {z: er(load("cabinet_trial_front", z)) & sil2 for z in FZ}
rest = sil2 & ~np.any([fm[z] for z in FZ], axis=0)
rest = cv2.morphologyEx(rest.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)).astype(bool)
deck_rows = np.zeros_like(rest); deck_rows[336:404, :] = True
fm["front_rest_deck"] = rest & deck_rows     # buttons, joystick stem, deck slope (ndot 0.25: the deck faces 23 deg off vertical)
fm["front_rest"] = rest & ~deck_rows
fm["front_all"] = sil2   # final pass: base pass first, so no texel inside the silhouette is empty or black; zone views then blend reference over reference
# step-11 repair, right rail only: the rail crosses the deck slope (normal 23 deg off vertical) and the bevelled edge, which ndot 0.5 leaves unpainted; dilate the SAM rail mask 2 px, paint at ndot 0.1
fm["rail_right_fix"] = cv2.dilate(load("cabinet_trial_front", "rail_right").astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool) & sil2
SZ = ["side_trim", "side_stickers", "side_body"]
sm = {z: er(load("cabinet_trial_side", z), 1 if z != "side_trim" else 0) for z in SZ}
# SAM's body mask leaves holes (dark sticker interiors, outlines): everything inside the silhouette that no zone claims is painted by side_rest from the same reference pixels
sm["side_rest"] = er(sa, 1) & ~np.any([sm[z] for z in SZ], axis=0)
# step-11 repair: feathered zone edges blended against the dark fill leave dark halos along every zone boundary (worst in the sticker-dense lower side panel).
# A full-silhouette base pass first (alpha 1 everywhere inside, same reference pixels) means every zone edge blends reference over reference.
sm["side_all"] = er(sa, 1)
cfgs = {}
for kind, rf, rs, rsm in (("day", "front_day_flat", "side_day_flat", "side_day_flat_mirror"), ("emit", "front_emit_flat", "side_emit_flat", "side_emit_flat_mirror")):
    views = []
    order = ["front_all", "front_rest", "front_rest_deck", "lower_fascia", "marquee", "crt_bezel", "control_panel", "coin_door", "kick_panel_stickers", "rail_left", "rail_right", "rail_right_fix"]
    for z in order:
        v = {"ref": f"{T}/ref/{rf}.png", "crop": [0, 0, 290, 740], "side": "front", "mask_png": save(f"front_{z}", fm[z]), "feather": 2, "ndot": 0.2 if z == "front_all" else 0.1 if z == "rail_right_fix" else 0.25 if z in ("control_panel", "front_rest_deck") else 0.5, "bilinear": True, "_zone": z}
        views.append(v)
    for side_name, ref_, flipmask in (("right", rs, False), ("left", rsm, True)):
        for z in ["side_all", "side_rest", "side_body", "side_stickers", "side_trim"]:
            m = sm[z][:, ::-1] if flipmask else sm[z]
            v = {"ref": f"{T}/ref/{ref_}.png", "crop": [0, 0, 383, 740], "side": side_name, "mask_png": save(f"{side_name}_{z}", m), "feather": 2, "ndot": 0.5, "bilinear": True, "_zone": z,
                 "clip": {"axis": "x", "min": 0.3615} if side_name == "right" else {"axis": "x", "max": -0.3615}}   # flat side wall only: recess walls and bevels took the trim pixels (yellow slivers, doubled rail)
            views.append(v)
    cfgs[kind] = views
import shutil
GLB = f"{ABS}/{PK}/mesh/street_cabinet_rebuilt.glb"
for kind in ("day", "emit"):
    g = f"{T}/cab_{kind}.glb"; shutil.copy(GLB, g)
    json.dump({"glb": g, "out_glb": f"{T}/cab_{kind}_proj.glb", "report": f"{T}/report_{kind}.json", "reliable_iou": 0.85, "views": cfgs[kind]}, open(f"{T}/cfg_{kind}.json", "w"), indent=1)
json.dump(cfgs, open(f"{T}/views.json", "w"))
print("prepped", {k: len(v) for k, v in cfgs.items()}, "rest px", int(rest.sum()))
