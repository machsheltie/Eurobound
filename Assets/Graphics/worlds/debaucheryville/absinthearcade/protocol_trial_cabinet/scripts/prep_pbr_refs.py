"""Step 8 helper: builds "value reference" images (R sticker height, G roughness, B metallic) per view from the SAM zone masks, plus a projection config
that pushes them through the same camera-matched projection as the colour, so the PBR value maps land on the UVs exactly where the colour did.
The values are ASSUMED per finish (inferred, not measured, not physically validated: protocol step 4 / rule on generated PBR).
Run with the paint_zones venv python: prep_pbr_refs.py <abs tmp dir used by prep_projection.py> <abs path of a glb built with base hex 00d900>"""
import sys, json, os
import numpy as np
from PIL import Image
T = sys.argv[1]; GLB = sys.argv[2]
SAMW = os.environ.get("PAINT_ZONES_WORK", "tools/paint_zones/work")  # machine-specific: set PAINT_ZONES_WORK
def L(a, z): return np.array(Image.open(f"{SAMW}/{a}/masks/{z}.png").convert("L")) > 127
# zone: (height 0/1, roughness, metallic)  painter's order, later wins
FRONT = [("__bg", (0, .75, 0)), ("lower_fascia", (0, .8, 0)), ("marquee", (0, .3, 0)), ("crt_bezel", (0, .55, 0)), ("crt_screen", (0, .08, 0)),
         ("control_panel", (0, .5, 0)), ("joystick_red", (0, .35, 0)), ("coin_door", (0, .45, .6)), ("kick_panel_stickers", (0, .35, 0)),
         ("rail_left", (0, .5, 0)), ("rail_right", (0, .5, 0))]
SIDE = [("__bg", (0, .8, 0)), ("side_trim", (0, .5, 0)), ("side_stickers", (1, .3, 0)), ]
def comp(asset, zones, size):
    out = np.zeros((size[1], size[0], 3), np.float32)
    for z, (h, r, m) in zones:
        mk = np.ones((size[1], size[0]), bool) if z == "__bg" else L(asset, z)
        out[mk] = (h, r, m)
    return (out * 255).round().astype(np.uint8)
f = comp("cabinet_trial_front", FRONT, (290, 740)); s = comp("cabinet_trial_side", SIDE, (383, 740))
os.makedirs(f"{T}/ref", exist_ok=True)
Image.fromarray(f).save(f"{T}/ref/front_value.png"); Image.fromarray(s).save(f"{T}/ref/side_value.png")
Image.fromarray(s[:, ::-1]).save(f"{T}/ref/side_value_mirror.png")
cfg = json.load(open(f"{T}/cfg_day.json"))
views = []
for v in cfg["views"]:
    v = dict(v); v.pop("delight_px", None); v["bilinear"] = False
    v["ref"] = f"{T}/ref/" + ("front_value.png" if v["side"] == "front" else "side_value.png" if v["side"] == "right" else "side_value_mirror.png")
    views.append(v)
cfg.update(glb=f"{T}/cab_orm.glb", out_glb=f"{T}/cab_orm_proj.glb", report=f"{T}/report_orm.json", views=views)
import shutil; shutil.copy(GLB, f"{T}/cab_orm.glb")
json.dump(cfg, open(f"{T}/cfg_orm.json", "w"), indent=1)
print("orm cfg written")
