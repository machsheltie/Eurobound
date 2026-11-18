"""Cut the window cat and the front doors out of the Absinthe Arcade front face (Eurobound-d4i6).

Plan: docs/superpowers/plans/2026-11-14-arcade-rework-plan.md section 3.4 (rows E2 and E3), under
design/style_guides/location_interactables_rule.md. The cat is canon and is never removed from the game.
It becomes its own card on the sill (day, night, emit), cut from the approved plate pixels.

    python Tools/content_generation/absinthe_arcade/exterior_cutouts/front_face_cutouts.py [--review DIR]

Reads  02_facade/aa_face_front_{day,night,emit,height,normal}.png (the live plates; read-only).
Writes
  07_props/aa_prop_window_cat_{day,night,emit}.png       cat card (RGBA, soft 1 px edge)
  07_props/aa_prop_front_door_leaf_{left_outer,left_inner,right_inner}_{day,night,emit}.png
  07_props/aa_layer_entrance_interior_{day,night,emit}.png   the corridor glimpse, as its own layer
  07_props/aa_prop_window_cat.json, 07_props/aa_prop_front_doors.json   placement (face pixels, height)
  02_facade/_staged_d4i6/aa_face_front_{day,night,emit,height,normal}.png   clean plates
The clean plates are STAGED, not live: the live face keeps the cat until the cat card is wired into
the scene (window_cat, absinthe_arcade_exterior_hd2d.gd), so the cat is never missing from the game.

How the plate behind is rebuilt (the same copy steps on all five maps, so day, night, emit, height
and normal stay registered):
  cat, curtain pane and window frame (rows above the railing): mirrored down from the rows above the cat
  cat, railing bar and the dark space under it: tiled across from the strip just left of the cat
  doors: the whole doorway opening becomes the dark void behind the doors (height 1 = deepest
  recess, flat normal); the three leaves and the corridor glimpse cover it again as separate layers.
Re-runnable; output is deterministic.
"""
import argparse
import json
import os
import sys

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
EXT = os.path.join(ROOT, "Assets", "Graphics", "worlds", "debaucheryville", "absinthearcade", "absinthearcade_exterior")
FACE_DIR = os.path.join(EXT, "02_facade")
PROP_DIR = os.path.join(EXT, "07_props")
STAGE_DIR = os.path.join(FACE_DIR, "_staged_d4i6")
FACE = "aa_face_front"
MAPS = ["day", "night", "emit", "height", "normal"]
COLOUR = ["day", "night", "emit"]

# ---- cat (left first-floor window, measured on the 1065 x 1712 face) ----
CAT_BOX = (204, 616, 256, 697)          # x0, y0, x1, y1 (exclusive) search box
CAT_HEIGHT_MIN = 117                    # the cat stands proud of the pane (pane 80-105, cat 124-128)
RAIL_ROWS = (661, 664)                  # railing bar crosses the silhouette in the height map here
RAIL_TOP, RAIL_BOTTOM = 660, 666        # the railing bar's rows on the day plate (657-659 carry leaf tips)
SILL_TOP = 696                          # the sill's dark lip and highlight start here
FRAME_X = 249                           # the window's right wooden frame starts at this column
FRAME_SRC_ROW = 640                     # frame pixels copied down from here (clear of the cat)
BALUSTER_UNIT = (197, 209)              # one baluster and its gap, just left of the cat (columns)
FUR_RED_MINUS_BLUE_MAX = 28             # wood frame is 40-80 here, the cat's fur under 20
CAT_DARK_MAX = 100                      # cat fur luminance on the day plate (curtain 130-200)

# ---- doors (whole doorway opening, measured from the height map steps) ----
DOOR_TOP, DOOR_BOTTOM = 1224, 1700      # rows: below the marquee's border; the threshold step and the
                                        # leaves' kick plates under DOOR_BOTTOM stay painted on the plate
DOOR_PIECES = [                          # id, x0, x1 (exclusive)
    ("aa_prop_front_door_leaf_left_outer", 289, 368),
    ("aa_prop_front_door_leaf_left_inner", 368, 442),
    ("aa_layer_entrance_interior", 442, 695),
    ("aa_prop_front_door_leaf_right_inner", 695, 766),
]
VOID_RGB = {"day": (17, 14, 21), "night": (12, 11, 18), "emit": (0, 0, 0)}


def load():
    m = {}
    for v in MAPS:
        im = Image.open(os.path.join(FACE_DIR, "%s_%s.png" % (FACE, v)))
        m[v] = np.array(im)
    return m


def cat_mask(m):
    x0, y0, x1, y1 = CAT_BOX
    h = m["height"].astype(int)
    lum = np.array(Image.fromarray(m["day"][..., :3]).convert("L")).astype(int)
    hm = np.zeros(h.shape, bool)
    hm[y0:y1, x0:x1] = h[y0:y1, x0:x1] >= CAT_HEIGHT_MIN
    # the railing bar is as proud as the cat: bridge its rows with the rows just above and below
    r0, r1 = RAIL_ROWS
    hm[r0:r1] = hm[r0 - 1] & hm[r1]
    hm = ndi.binary_fill_holes(hm)
    lab, n = ndi.label(hm)
    if n > 1:
        sizes = ndi.sum(hm, lab, range(1, n + 1))
        hm = lab == (1 + int(np.argmax(sizes)))
    # colour refinement: the height map is soft, so grow it and keep dark fur (and the yellow eyes)
    grown = ndi.binary_dilation(hm, iterations=3)
    rgb = m["day"][..., :3].astype(int)
    eyes = (rgb[..., 0] > 150) & (rgb[..., 1] > 100) & (rgb[..., 2] < 90)
    # black fur is neutral; the window frame and pot shadows are just as dark but brown (red over blue)
    fur = ((lum < CAT_DARK_MAX) & (rgb[..., 0] - rgb[..., 2] < FUR_RED_MINUS_BLUE_MAX)) | eyes
    mask = (grown & fur) | ndi.binary_erosion(hm, iterations=1)
    mask[:y0] = False; mask[y1:] = False; mask[:, :x0] = False; mask[:, x1:] = False
    # under the railing the space behind the cat is dark too: keep the cat's own width there
    for y in range(RAIL_TOP, y1):
        xs = np.nonzero(hm[y])[0]
        if len(xs):
            row = np.zeros(mask.shape[1], bool)
            row[max(xs[0] - 2, x0):min(xs[-1] + 3, x1)] = True
            mask[y] &= row
        else:
            mask[y] = False
    mask = ndi.binary_opening(mask, iterations=1)
    mask = ndi.binary_fill_holes(mask)
    lab, n = ndi.label(mask)
    if n > 1:
        sizes = ndi.sum(mask, lab, range(1, n + 1))
        mask = lab == (1 + int(np.argmax(sizes)))
    return mask, hm


def fill_cat(m, remove, keys):
    """Rebuild the colour plate under `remove` for the maps in `keys` (the same copies on every map).

    Curtain pane and frame above the railing: mirrored down from the rows above the cat.
    Railing (bar, turned balusters, the dark gaps between them) and the sill lip: one clean railing
    unit just left of the cat (BALUSTER_UNIT, a baluster and its gap) repeated across to the frame,
    so the balustrade carries on behind the cat.
    Window frame under the bar: copied straight down from the frame above the cat.
    Relief maps (height, normal) are smooth by nature and are filled by relief_fill instead.
    """
    ys, xs = np.nonzero(remove)
    top = ys.min()
    out = {k: m[k].copy() for k in keys}
    u0, u1 = BALUSTER_UNIT
    period = u1 - u0
    for y, x in zip(ys, xs):
        if y < RAIL_TOP:
            src = (top - 1 - (y - top), x)
        elif x >= FRAME_X and RAIL_BOTTOM < y < SILL_TOP:
            src = (FRAME_SRC_ROW + (y - RAIL_BOTTOM) % 8, x)
        else:
            src = (y, u0 + ((x - u0) % period))
        for k in keys:
            out[k][y, x] = m[k][src]
    # soften the seam one pixel in from the boundary with the original neighbours
    ring = remove & ~ndi.binary_erosion(remove, iterations=1)
    for k in keys:
        a = out[k].astype(np.float32)
        blur = ndi.uniform_filter(a, size=(3, 3) + ((1,) if a.ndim == 3 else ()))
        a[ring] = blur[ring]
        out[k] = np.clip(a + 0.5, 0, 255).astype(m[k].dtype)
    return out


def relief_fill(m, hole, keys, iterations=600):
    """Fill `hole` in smooth maps by diffusion (repeated 3x3 averaging with the edge held fixed)."""
    ys, xs = np.nonzero(hole)
    pad = 20
    y0, y1 = max(ys.min() - pad, 0), ys.max() + pad + 1
    x0, x1 = max(xs.min() - pad, 0), xs.max() + pad + 1
    h = hole[y0:y1, x0:x1]
    out = {}
    for k in keys:
        full = m[k].copy()
        a = full[y0:y1, x0:x1].astype(np.float32)
        size = (3, 3) + ((1,) if a.ndim == 3 else ())
        init = ndi.uniform_filter(a, size=(31, 31) + ((1,) if a.ndim == 3 else ()))
        a[h] = init[h]
        for _ in range(iterations):
            a[h] = ndi.uniform_filter(a, size=size)[h]
        full[y0:y1, x0:x1] = np.clip(a + 0.5, 0, 255).astype(m[k].dtype)
        out[k] = full
    return out


def card(img, alpha, bbox):
    x0, y0, x1, y1 = bbox
    rgba = np.zeros((y1 - y0, x1 - x0, 4), np.uint8)
    rgba[..., :3] = img[y0:y1, x0:x1, :3]
    rgba[..., 3] = alpha[y0:y1, x0:x1]
    return Image.fromarray(rgba, "RGBA")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--review", help="also write review images (composites, checkers) here")
    a = ap.parse_args()
    m = load()
    H, W = m["height"].shape
    os.makedirs(STAGE_DIR, exist_ok=True)

    # ---------- cat ----------
    mask, hsil = cat_mask(m)
    # a tight matte: solid inside, one partly transparent pixel on the outline, nothing outside
    alpha = np.where(mask, 255, 0).astype(np.uint8)
    alpha[mask & ~ndi.binary_erosion(mask, iterations=1)] = 200
    ys, xs = np.nonzero(alpha)
    bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
    remove = ndi.binary_dilation(mask, iterations=2)
    clean = fill_cat(m, remove, COLOUR)
    # the relief map's cat is softer and wider than the painted one: clear a wider area there
    hremove = remove | ndi.binary_dilation(hsil, iterations=7)
    clean.update(relief_fill(m, hremove, ["height", "normal"]))
    # defringe: edge pixels take the fur colour of the nearest pixel inside the cat, so no curtain
    # or window colour rides along on the soft edge
    core = ndi.binary_erosion(mask, iterations=2)
    _, (iy, ix) = ndi.distance_transform_edt(~core, return_indices=True)
    fringe = (alpha > 0) & ~core
    cards = {}
    for v in COLOUR:
        c = m[v].copy()
        c[fringe] = m[v][iy[fringe], ix[fringe]]
        cards[v] = c
    cat_spec = {"asset_id": "aa_prop_window_cat", "face": FACE, "bead": "Eurobound-d4i6",
                "source": "cut from the approved front-face plate (the plate cat is approved; TR/aa_prop_window_cat.glb unused)",
                "anchor": "bottom centre sits on the left first-floor sill", "files": {}}
    for v in COLOUR:
        name = "aa_prop_window_cat_%s.png" % v
        card(cards[v], alpha, bbox).save(os.path.join(PROP_DIR, name))
        cat_spec["files"][name] = {"source_face": "%s_%s.png" % (FACE, v), "top_left_px": list(bbox[:2]),
                                   "size_px": [bbox[2] - bbox[0], bbox[3] - bbox[1]], "face_texture_px": [W, H]}
    hv = m["height"][mask]
    cat_spec["face_height_mean"] = round(float(hv.mean()), 1)
    cat_spec["face_height_m_above_wall"] = round((float(hv.mean()) - 128.0) / 255.0, 3)
    # real-world numbers (face ppm 66.49 painting px per metre, painting scale 2.4; wall px 20-1044)
    ppm, ps = 66.49, 2.4
    cx = (bbox[0] + bbox[2]) / 2.0
    cat_spec["real_size_m"] = [round((bbox[2] - bbox[0]) / ppm / ps, 3), round((bbox[3] - bbox[1]) / ppm / ps, 3)]
    cat_spec["height_m"] = cat_spec["real_size_m"][1]
    cat_spec["sill_height_m"] = round((H - bbox[3]) / ppm / ps, 3)
    cat_spec["centre_x_m"] = round((cx - (20 + 1044) / 2.0) / ppm / ps, 3)
    cat_spec["collision_footprint_m"] = "none: the cat sits on the sill out of reach; no blocker"
    cat_spec["examine_point_note"] = ("game window_cat examine marker is at x = -3.3 m; the cat itself is at "
                                      "centre_x_m, so the marker belongs at about that x on the pavement")
    json.dump(cat_spec, open(os.path.join(PROP_DIR, "aa_prop_window_cat.json"), "w"), indent=2)

    # ---------- doors ----------
    door_spec = {"face": FACE, "bead": "Eurobound-d4i6", "scene_exit": "exit_front_door (unchanged)",
                 "note": "pieces tile the doorway opening exactly; drawn over the staged plate they "
                         "reproduce the old front face pixel for pixel", "pieces": {}}
    for pid, dx0, dx1 in DOOR_PIECES:
        box = (dx0, DOOR_TOP, dx1, DOOR_BOTTOM)
        full = np.full((H, W), 255, np.uint8)
        hv = m["height"][DOOR_TOP:DOOR_BOTTOM, dx0:dx1].astype(float)
        door_spec["pieces"][pid] = {"top_left_px": [dx0, DOOR_TOP], "size_px": [dx1 - dx0, DOOR_BOTTOM - DOOR_TOP],
                                    "face_height_median": float(np.median(hv)),
                                    "files": ["%s_%s.png" % (pid, v) for v in COLOUR]}
        for v in COLOUR:
            card(m[v], full, box).save(os.path.join(PROP_DIR, "%s_%s.png" % (pid, v)))
    ox0, ox1 = DOOR_PIECES[0][1], DOOR_PIECES[-1][2]
    door_spec["opening_px"] = [ox0, DOOR_TOP, ox1, DOOR_BOTTOM]
    for v in COLOUR:
        clean[v][DOOR_TOP:DOOR_BOTTOM, ox0:ox1, :3] = VOID_RGB[v]
        if clean[v].shape[2] == 4:
            clean[v][DOOR_TOP:DOOR_BOTTOM, ox0:ox1, 3] = 255
    clean["height"][DOOR_TOP:DOOR_BOTTOM, ox0:ox1] = 1
    clean["normal"][DOOR_TOP:DOOR_BOTTOM, ox0:ox1] = (128, 128, 255)
    json.dump(door_spec, open(os.path.join(PROP_DIR, "aa_prop_front_doors.json"), "w"), indent=2)

    for v in MAPS:
        Image.fromarray(clean[v]).save(os.path.join(STAGE_DIR, "%s_%s.png" % (FACE, v)))

    # ---------- self-check: the cards over the clean plate give back the old plate ----------
    worst = {}
    for v in COLOUR:
        comp = clean[v][..., :3].astype(float)
        al = alpha.astype(float)[..., None] / 255.0
        comp = comp * (1 - al) + m[v][..., :3].astype(float) * al
        comp[DOOR_TOP:DOOR_BOTTOM, ox0:ox1] = m[v][DOOR_TOP:DOOR_BOTTOM, ox0:ox1, :3]
        d = np.abs(comp - m[v][..., :3].astype(float))
        worst[v] = (float(d[mask].max()), float(d.max()))
    print("cat bbox", bbox, "pixels", int(mask.sum()))
    print("composite vs old plate, max abs diff (inside cat, anywhere):", worst)
    for v in MAPS:
        untouched = ~ndi.binary_dilation(remove if v in COLOUR else hremove, iterations=1)
        untouched[DOOR_TOP:DOOR_BOTTOM, ox0:ox1] = False
        assert (clean[v][untouched] == m[v][untouched]).all(), "pixels changed outside the cut regions: " + v
    print("outside the cut regions every map is unchanged")

    if a.review:
        review(a.review, cards, clean, alpha, bbox, remove)


def review(out, m, clean, alpha, bbox, remove):
    # `m` here is the defringed card source for the colour maps
    os.makedirs(out, exist_ok=True)
    x0, y0, x1, y1 = bbox
    pad = 40
    box = (x0 - pad - 30, y0 - pad - 40, x1 + pad, y1 + 20)
    for v in COLOUR:
        Image.fromarray(clean[v]).crop(box).resize(((box[2] - box[0]) * 4, (box[3] - box[1]) * 4), Image.LANCZOS) \
            .save(os.path.join(out, "cat_clean_plate_%s_x4.png" % v))
        c = card(m[v], alpha, bbox)
        chk = Image.new("RGBA", c.size)
        tile = np.indices(c.size[::-1]).sum(0) // 4 % 2
        chk = Image.fromarray(np.dstack([np.where(tile, 200, 120)] * 3 + [np.full(tile.shape, 255)]).astype(np.uint8))
        chk.alpha_composite(c)
        chk.resize((c.width * 6, c.height * 6), Image.NEAREST).save(os.path.join(out, "cat_card_%s_on_checker_x6.png" % v))
    for v in ("day", "night"):
        Image.fromarray(clean[v]).crop((250, 1180, 820, 1712)).save(os.path.join(out, "door_clean_plate_%s.png" % v))
    Image.fromarray(clean["height"]).crop(box).resize(((box[2] - box[0]) * 4, (box[3] - box[1]) * 4)) \
        .save(os.path.join(out, "cat_clean_height_x4.png"))
    # composites: every new layer drawn back over the clean plate, close up and at game size
    for v in ("day", "night"):
        comp = Image.fromarray(clean[v]).convert("RGBA")
        comp.alpha_composite(card(m[v], alpha, bbox), bbox[:2])
        for pid, dx0, dx1 in DOOR_PIECES:
            comp.alpha_composite(Image.open(os.path.join(PROP_DIR, "%s_%s.png" % (pid, v))), (dx0, DOOR_TOP))
        comp.crop(box).resize(((box[2] - box[0]) * 4, (box[3] - box[1]) * 4), Image.LANCZOS) \
            .save(os.path.join(out, "cat_composite_%s_x4.png" % v))
        comp.crop((250, 1180, 820, 1712)).save(os.path.join(out, "door_composite_%s.png" % v))
        bg = Image.new("RGBA", comp.size, (40, 40, 40, 255))
        bg.alpha_composite(comp)
        bg.convert("RGB").resize((comp.width // 2, comp.height // 2), Image.LANCZOS) \
            .save(os.path.join(out, "front_face_composite_%s_half.png" % v))
    for v in COLOUR:
        tiles = [Image.open(os.path.join(PROP_DIR, "%s_%s.png" % (pid, v))) for pid, _, _ in DOOR_PIECES]
        sheet = Image.new("RGB", (sum(t.width for t in tiles) + 20 * (len(tiles) + 1), tiles[0].height + 40), (255, 0, 255))
        x = 20
        for t in tiles:
            sheet.paste(t.convert("RGB"), (x, 20))
            x += t.width + 20
        sheet.save(os.path.join(out, "door_pieces_%s_on_magenta.png" % v))


if __name__ == "__main__":
    sys.exit(main())
