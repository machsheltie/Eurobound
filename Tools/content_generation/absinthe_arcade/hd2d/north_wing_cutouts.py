"""Split the five painted-in north-wing interactables out of the Absinthe Arcade plates (bead Eurobound-59b9).

Plan: docs/superpowers/plans/2026-11-14-arcade-rework-plan.md section 3.2 (audit rows N1-N5), under
design/style_guides/location_interactables_rule.md. Gate: dev/qc/QC_COVERAGE.md "C: 2D cut-outs".

    python Tools/content_generation/absinthe_arcade/hd2d/north_wing_cutouts.py [--review DIR] [--fill NAME=PNG ...]

Reads (read-only): the live plates game/.../interior/north_wing/aa_int_north_wing_{day,night,emit}.png and the SAM
masks tools/paint_zones/work/aa_north_wing_{day,night}/masks/ (prompts: tools/paint_zones/zones/aa_north_wing_*.json).
Writes everything to game/.../interior/north_wing/props_staged/ (it has a .gdignore, so Godot skips it until the
scene step); the live plates are never written, so nothing leaves the game before the scene loads the new nodes.

Registration. Night is the master. emit is registered to night. The day relight is NOT registered to night on the
left wall (curtain, plaque, Time Crisis are ~90-130 px higher in the day plate) and is off by a few px at the door.
So every piece is cut from each plate where that plate painted it: the day layer uses the same alpha and size,
moved by the piece's day->night offset (measured here by matching the day and night SAM masks). The JSON gives a
plate_xy per variant. Right wall (DDR, door, lamps): one shared alpha, the pixels both plates' SAM masks agree on
(cleaned; the door leaf is its convex hull). Left wall (curtain, plaque, Time Crisis): the day relight is a redraw
there (mask IoU 0.85-0.88 even after the best shift), so each plate is cut with its own cleaned mask on one canvas size.

Pieces, ids and states (sm = design/.../sprite_mapping/absinthe_arcade_sprite_mapping.json):
  N1 aa_cab_ddr_broken (broken_ddr): error = the painted machine; token_0..3_of_3 use the error art (the pips stay a
     code stand-in, Eurobound-w2ig); unlock_pulse = error + its own neon (house emit rule) added again as glow.
  N2 aa_transition_maintenance_door (maintenance_door): the leaf (sign, latch) in one state "closed"; the top lamp
     cluster and the side indicator in locked_red (red lit, green dark) and unlocked_green (green lit, red dark).
     "Dark" is derived from the painted lit lens (value compressed, glow spill removed). The top cluster also has
     unlocking_amber (amber lit, red and green dark): the brief flash while the door unlocks (author, Desk
     Eurobound-59b9-q2). opening_exterior_only has no art: the scene fades or cuts away (author, 59b9-q3).
  N3 aa_transition_taproom_curtain (taproom_curtain): day_inert (glow removed), evening_faint (+0.35 glow),
     night_breathing (painted, full glow), discovered (+0.5 glow, "subtle"); aa_transition_taproom_glow = the glow
     alone (additive layer for the scene's breathing loop); aa_transition_taproom_plaque, one state.
  N4 aa_cab_time_crisis_cracked (cracked_time_crisis_cabinet): displaced_revealed (painted pose; at night the
     screen neon is taken out), night_glow (painted, neon on), curtain_hidden (the displaced pixels moved right
     until the cabinet body covers the curtain's right edge; the area this exposes needs the Gemini fill).
  N5 aa_transition_taproom_vapor: the vapour as its own layer (shown 20:00-04:00 by the scene). Provisional until
     the Gemini fill exists: alpha from a green-excess unmix, colour = the plate's own pixels.

Clean plates (props_staged/clean_plates/). Script fills (deterministic): maintenance door leaf -> doorway void;
all lamps -> dark; curtain -> void (the arch opening is never seen: the curtain layer covers it); plaque ->
jamb stone copied up from below. Holes that need a Gemini fill (big, structured): DDR (N1) and the left corner
(Time Crisis + gun + vapour, N4/N5). For those, gemini/ holds the exact plate crop, the mask (white = fill) and a
prompt; until a fill is given the staged plate keeps the original pixels there (status in clean_plates/status.json).
With --fill ddr_day=PNG (and ddr_night, left_day, left_night) the returned edit of that crop is pasted inside the
mask only, tone-matched on a band around it (cut_plate_prop.py method); a missing night fill is derived from the
day fill by the day->night colour fit on the surroundings; emit inside the hole = the hall emit rule on night.
The left fill also completes the curtain behind the cabinet (green velvet pixels of the fill inside the arch become
curtain layer; the rest is plate) and re-solves the vapour layer against the clean floor.

Self-check: outside the holes every staged clean plate equals the live plate; every layer drawn back over the
clean plate reproduces the live plate inside its alpha (max difference printed). Re-runnable; deterministic.
"""
import argparse
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage as ndi
from scipy.signal import fftconvolve

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *[".."] * 4))
REL_PLATES = "game/assets/worlds/debaucheryville/absinthe_arcade/interior/north_wing"
PLATES = os.path.join(ROOT, REL_PLATES)
OUT = os.path.join(PLATES, "props_staged")
CLEAN = os.path.join(OUT, "clean_plates")
GEM = os.path.join(OUT, "gemini")
SAM = os.path.join(ROOT, "tools", "paint_zones", "work", "aa_north_wing_%s", "masks")
BASE = "aa_int_north_wing"
KINDS = ("day", "night", "emit")
BEAD = "Eurobound-59b9"

# piece -> SAM zones, prior day->night offset (dx, dy) in px, search radius
PIECES = {
    "ddr": (["ddr_cabinet", "ddr_pad", "ddr_rail_left", "ddr_rail_right"], (0, 0), 24),
    "door_leaf": (["door_leaf"], (7, 10), 24),
    "lamps_top": (["lamp_red", "lamp_amber", "lamp_green"], (5, 3), 12),
    "lamps_side": (["side_panel", "side_red", "side_green"], (8, 12), 12),
    "curtain": (["curtain"], (5, 114), 40),
    "plaque": (["plaque"], (12, 90), 30),
    "tc": (["tc_cabinet", "tc_gun"], (0, 110), 40),
}
VOID = {"day": (17, 14, 21), "night": (12, 11, 18), "emit": (0, 0, 0)}   # doorway void (front_face_cutouts.py)
LAMP_HALO = 3          # the lamp pieces are the lens and bezel only (tight matte); the lit glow is a code light
SIDE_HALO = 0
LENS_GROW = 3
# colour of the painted lamp light (fraction per channel), used to take the whole light off, not only its hue
LIGHT = {"green": (0.45, 1.0, 0.25), "red": (1.0, 0.25, 0.2)}
LEAF_TO_FRAME = 2      # the leaf matte (and the void behind it) reaches 2 px past the hull, up to the frame
# Painted lamp light on the frame and floor (night-frame boxes x0, y0, x1, y1). The unlock light is a code light
# (plan row N2, gd:146-152), so this spill comes off the clean plate: the lamp colour is clamped back to the
# surrounding unlit tone (green: G <= 0.97 x max(R, B); red: R <= the ring's own R / max(G, B), 75th pct).
SPILL_BOXES = [("green_bar", (2540, 645, 2712, 805)),  # green lamp's strip along the top frame bar (+ highlight)
               ("red", (2465, 625, 2568, 740)),       # red lamp on the frame's top-left corner
               ("green", (2598, 985, 2702, 1155)),    # side indicator surround
               ("red", (2552, 975, 2668, 1160)),       # (red side light also falls on the leaf to its left)
               ("green", (2400, 1280, 2752, 1536))]   # threshold and floor in front of the door
# Room camera, copied read-only from game/worlds/debaucheryville/absinthe_arcade_north_wing_hd2d.gd (_init, 64-70):
# focal 4634 px at 2752 wide, pitch 23.1 deg, camera 14.9 tiles up, 40.05 tiles in front of z = 0; a tile = 0.67 m.
CAM = {"focal": 4634.0, "pitch": 23.1, "height": 14.9, "z": 40.05, "tile_m": 0.67}
DOOR_POINT = ((7.6, 15.2), (6.6, 15.2))   # INTERACT_POINTS["maintenance_door"] (gd:37): anchor, bro stands (x, z)
# vapour search region (x0, y0, x1, y1) per frame, minus the cabinet, gun and curtain
VAPOUR_BOX = {"day": (180, 940, 480, 1300), "night": (60, 1000, 540, 1460)}
# The day relight is a redraw on the left wall: after the best translation the day and night outlines of these
# still differ by up to ~15-20 px (mask IoU 0.85-0.88), so a shared alpha would either clip the object or carry
# background. They are cut with each plate's own (cleaned) SAM mask instead, on one canvas size per piece.
PER_PLATE = {"curtain": {"close": 4, "smooth": 2.0}, "plaque": {}, "tc": {"close": 12, "smooth": 3.0, "max_hole": 800}}
GLOW_K = {"day_inert": 0.0, "evening_faint": 0.35, "night_breathing": 1.0, "discovered": 0.5}
GEM_PAD = 96
VAPOUR_RAMP = 40.0     # px over which the vapour fades out towards its search box's sides (gate C round 1)
VAPOUR_MAX = 0.75      # most opaque the solved vapour may be (gate C round 1: opaque lumps read as a sticker)
SHADOW_PAD = 14       # rows below the Time Crisis cabinet's box for its contact shadow (gate C round 1)


# ----------------------------------------------------------------------------------------------- helpers
def f32(im):
    return np.asarray(im).astype(np.float32) / 255.0


def u8(a):
    return (np.clip(a, 0, 1) * 255 + 0.5).astype(np.uint8)


def load_plates():
    return {k: f32(Image.open(os.path.join(PLATES, "%s_%s.png" % (BASE, k))).convert("RGB")) for k in KINDS}


def sam(frame, zone):
    return np.asarray(Image.open(os.path.join(SAM % frame, zone + ".png")).convert("L")) > 127


def shift(mask_or_img, dx, dy):
    """Move an image by (dx, dy) px (new[y+dy, x+dx] = old[y, x]); uncovered pixels are 0."""
    a = mask_or_img
    out = np.zeros_like(a)
    H, W = a.shape[:2]
    ys0, ys1 = max(0, -dy), min(H, H - dy)
    xs0, xs1 = max(0, -dx), min(W, W - dx)
    out[ys0 + dy:ys1 + dy, xs0 + dx:xs1 + dx] = a[ys0:ys1, xs0:xs1]
    return out


def bbox(mask, pad=0, shape=None):
    ys, xs = np.nonzero(mask)
    H, W = shape if shape else mask.shape
    return (max(int(xs.min()) - pad, 0), max(int(ys.min()) - pad, 0),
            min(int(xs.max()) + 1 + pad, W), min(int(ys.max()) + 1 + pad, H))


def lum(a):
    return a @ np.array([0.299, 0.587, 0.114], np.float32)


def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0, 1)
    return t * t * (3 - 2 * t)


def emit_map(night):
    """The hall emit rule (cut_interior_layers.emit_map / cut_plate_prop.emit_map): saturated neon and lamp cores."""
    mx, mn = night.max(-1), night.min(-1)
    sat = (mx - mn) / (mx + 1e-4)
    neon = np.clip((sat * mx - 0.38) / 0.30, 0, 1)
    lamp = np.clip((night.mean(-1) - 0.80) / 0.15, 0, 1)
    m = ndi.gaussian_filter(np.clip(neon + lamp, 0, 1), 1.2)
    return night * m[..., None]


def best_offset(D, N, prior, R):
    """Day->night translation that best overlaps the day mask onto the night mask (search prior +- R)."""
    x0, y0, x1, y1 = bbox(D | shift(N, -prior[0], -prior[1]), pad=R + 4)
    d = D[y0:y1, x0:x1].astype(np.float32)
    px, py = prior
    m = R + max(abs(px), abs(py)) + 8                     # pad so the search window never leaves the image
    Np = np.pad(N, m)
    n = Np[y0 + py - R + m:y1 + py + R + m, x0 + px - R + m:x1 + px + R + m].astype(np.float32)
    c = fftconvolve(n, d[::-1, ::-1], mode="valid")
    iy, ix = np.unravel_index(int(np.argmax(c)), c.shape)
    return (px - R + int(ix), py - R + int(iy))


# ----------------------------------------------------------------------------------------------- pieces
def consensus(N, Ds, hull=False, close=4, smooth=1.5, max_hole=None):
    """The shared alpha: pixels both plates call the object (a leak or a sliver only one SAM mask has is background
    in the other plate, so it would show as a halo), crevices closed, holes filled, the outline smoothed. A door
    leaf is a flat quad: its outline is the convex hull simplified to straight edges."""
    A = N & Ds
    A = ndi.binary_closing(np.pad(A, close), iterations=close)[close:-close, close:-close]
    filled = ndi.binary_fill_holes(A)
    if max_hole:   # a real opening (the loop of the gun's hose) stays open; only small crevices are filled
        lab, n = ndi.label(filled & ~A)
        if n:
            sizes = ndi.sum(filled & ~A, lab, range(1, n + 1))
            filled = A | np.isin(lab, 1 + np.nonzero(sizes < max_hole)[0])
    A = filled
    A = ndi.binary_opening(A, iterations=2)
    lab, n = ndi.label(A)
    if n > 1:
        sizes = ndi.sum(A, lab, range(1, n + 1))
        A = np.isin(lab, 1 + np.nonzero(sizes >= 200)[0])
    A = ndi.gaussian_filter(A.astype(np.float32), smooth) > 0.5
    if hull:
        import cv2
        pts = np.column_stack(np.nonzero(A)[::-1]).astype(np.int32)
        poly = cv2.approxPolyDP(cv2.convexHull(pts), 3.0, True)
        img = Image.new("L", (A.shape[1], A.shape[0]), 0)
        ImageDraw.Draw(img).polygon([tuple(int(v) for v in q[0]) for q in poly], fill=255)
        A = np.asarray(img) > 127
    return A


def build_pieces(P):
    shape = P["day"].shape[:2]
    pieces = {}
    for name, (zones, prior, R) in PIECES.items():
        D = np.zeros(shape, bool)
        N = np.zeros(shape, bool)
        for z in zones:
            D |= sam("day", z)
            N |= sam("night", z)
        off = best_offset(D, N, prior, R)
        Ds = shift(D, *off)
        iou = float((Ds & N).sum()) / float((Ds | N).sum())
        p = {"offset": off, "iou": round(iou, 3), "zones": zones, "own": {"night": N, "day": D}}
        if name in PER_PLATE:
            kw = PER_PLATE[name]
            p["masks"] = {"night": consensus(N, N, **kw), "day": consensus(D, D, **kw)}
            p["alpha"] = "per plate"
            if name == "tc":
                # gate C round 1: notches along the cabinet's right edge showed the floor; a stronger close and
                # smooth for the cut. The Gemini hole keeps the old matte (the fill was made for that crop).
                p["hole_masks"] = dict(p["masks"])
                kw2 = dict(kw, close=20, smooth=4.0)
                p["masks"] = {"night": consensus(N, N, **kw2), "day": consensus(D, D, **kw2)}
        else:
            A = consensus(N, Ds, hull=(name in ("door_leaf", "lamps_side")))   # flat quads: straight edges
            p["masks"] = {"night": A, "day": shift(A, -off[0], -off[1])}
            p["alpha"] = "shared"
            if name == "ddr":
                # gate C round 1 (2026-11-18): the day/night intersection bit the cabinet's left flank, deck end and
                # rails away (the night SAM mask is ragged). The DDR sits where both paintings agree (offset ~1 px),
                # so its matte is the cleaned day outline, plus at night up to 3 px of what the night mask adds at
                # that outline. The Gemini holes keep the old matte (the fills were made for those crops).
                p["hole_masks"] = dict(p["masks"])
                Dc = consensus(D, D, close=6, smooth=2.0)
                Nc = consensus(N, N, close=6, smooth=2.0)
                Dn = shift(Dc, *off)
                p["masks"] = {"day": Dc, "night": Dn | (Nc & ndi.binary_dilation(Dn, iterations=3))}
                p["alpha"] = "day outline (both plates)"
        pieces[name] = p
    for fr in ("day", "night"):
        # the leaf stops where the side indicator (mounted over its right edge) starts
        side = ndi.binary_dilation(pieces["lamps_side"]["masks"][fr], iterations=SIDE_HALO + 2)
        leaf = ndi.binary_dilation(pieces["door_leaf"]["masks"][fr], iterations=LEAF_TO_FRAME)
        pieces["door_leaf"]["masks"][fr] = leaf & ~side
        # lamp pieces carry their glow spill
        for n, r in (("lamps_top", LAMP_HALO), ("lamps_side", SIDE_HALO)):
            if r > 0:   # (scipy reads iterations=0 as "dilate until nothing changes")
                pieces[n]["masks"][fr] = ndi.binary_dilation(pieces[n]["masks"][fr], iterations=r)
        # the curtain stops at the cabinet in front of it
        pieces["curtain"]["masks"][fr] &= ~ndi.binary_dilation(pieces["tc"]["masks"][fr], iterations=1)
    pieces["lamps_top"]["feather"] = pieces["lamps_side"]["feather"] = True
    for p in pieces.values():
        set_boxes(p)
    return pieces


def set_boxes(p, pad=2):
    """One canvas size per piece (every state and variant the same size); top-left per plate frame."""
    bd, bn = bbox(p["masks"]["day"], pad), bbox(p["masks"]["night"], pad)
    w = max(bd[2] - bd[0], bn[2] - bn[0])
    h = max(bd[3] - bd[1], bn[3] - bn[1])
    p["boxes"] = {"day": (bd[0], bd[1], bd[0] + w, bd[1] + h), "night": (bn[0], bn[1], bn[0] + w, bn[1] + h)}


def frame_box(p, kind):
    """The piece's box in a plate's frame (emit shares the night frame)."""
    return p["boxes"]["day" if kind == "day" else "night"]


def frame_mask(p, kind):
    return p["masks"]["day" if kind == "day" else "night"]


def alpha_of(mask):
    """Solid inside, one 200 px on the outline (front_face_cutouts.py matte)."""
    a = np.where(mask, 255, 0).astype(np.uint8)
    a[mask & ~ndi.binary_erosion(mask, iterations=1)] = 200
    return a


def defringe(img, mask):
    """Edge pixels take the colour of the nearest pixel two in from the outline (no background on the edge)."""
    core = ndi.binary_erosion(mask, iterations=2)
    if not core.any():
        return img
    _, (iy, ix) = ndi.distance_transform_edt(~core, return_indices=True)
    fr = mask & ~core
    out = img.copy()
    out[fr] = img[iy[fr], ix[fr]]
    return out


def crop_layer(P, p, kind, img=None, origin=(0, 0)):
    """RGBA float crop of a piece from plate `kind` (or from `img`, a window of that plate's frame at `origin`)."""
    src = P[kind] if img is None else img
    x0, y0, x1, y1 = frame_box(p, kind)
    m = frame_mask(p, kind)[y0:y1, x0:x1]
    ox, oy = origin
    if p.get("feather"):
        # lamp pieces: painted pixels as they are (they sit over the same painted housing on the clean plate),
        # matte feathered about one px over the bezel, no hard outline
        rgb = src[y0 - oy:y1 - oy, x0 - ox:x1 - ox]
        a = np.clip((ndi.gaussian_filter(m.astype(np.float32), 0.8) - 0.1) / 0.8, 0, 1)
        return np.dstack([rgb, a])
    rgb = defringe(src[y0 - oy:y1 - oy, x0 - ox:x1 - ox], m)
    a = alpha_of(m).astype(np.float32) / 255.0
    return np.dstack([rgb, a])


def save_rgba(arr, name):
    Image.fromarray(u8(arr), "RGBA").save(os.path.join(OUT, name))


# ----------------------------------------------------------------------------------------------- lamps
LAMP_AXIS = {"red": np.array([1, -.5, -.5], np.float32), "green": np.array([-.5, 1, -.5], np.float32),
             "amber": np.array([.5, .5, -1], np.float32)}


def lamp_off(img, lens, colour):
    """Derive an unlit lamp from the painted lit one, keeping the painted glass: inside the lens the painted pixels
    are scaled down (one factor, so texture and the specular highlight stay) until the brightest glass sits about
    1.25x the unlit metal around it, and their saturation is pulled to 55%: dim dark-red / dark-green / amber glass.
    On the bezel just outside the lens, the lamp-coloured fringe is pulled back to the housing's own colour at the
    same brightness (texture kept). Same rule day and night. Returns (image, lens weight for the emit)."""
    out = img.copy()
    L = lum(img)
    near = ndi.binary_dilation(lens, iterations=9) & ~ndi.binary_dilation(lens, iterations=4)
    ref = float(np.median(L[near])) if near.any() else 0.2
    f = min(1.0, 1.25 * ref / max(float(np.percentile(L[lens], 95)), 1e-3))
    g = (L * f)[..., None]
    dim = g + (img * f - g) * 0.55
    w = np.maximum(ndi.gaussian_filter(lens.astype(np.float32), 0.7), lens)[..., None]
    out = out * (1 - w) + dim * w
    # bezel fringe (3 px round the lens): lamp colour above the housing's -> housing colour, same luminance
    ring = ndi.binary_dilation(lens, iterations=3) & ~lens
    ax = LAMP_AXIS[colour]
    e = img @ ax
    base = float(np.median(e[near])) if near.any() else 0.0
    sw = smoothstep(0.0, 0.12, e - base) * ring
    hc = np.median(img[near] / np.maximum(L[near], 1e-3)[:, None], 0) if near.any() else np.ones(3, np.float32)
    rec = np.clip(hc[None, None, :] * L[..., None], 0, 1)
    out = out * (1 - sw[..., None]) + rec * sw[..., None]
    return np.clip(out, 0, 1), w[..., 0]


def despill(img, kind, offset, emit=False):
    keep = lens_union(kind)
    """Take the painted lamp light off the frame and floor (SPILL_BOXES, moved into this plate's frame by `offset`):
    only the lamp's own channel is lowered, and only where it exceeds the unlit tone; nothing is moved or blurred."""
    out = img.copy()
    H, W = img.shape[:2]
    dx, dy = offset if kind == "day" else (0, 0)
    for name, (x0, y0, x1, y1) in SPILL_BOXES:
        colour = name.split("_")[0]
        x0, y0, x1, y1 = max(x0 - dx, 0), max(y0 - dy, 0), min(x1 - dx, W), min(y1 - dy, H)
        box = np.zeros((H, W), bool)
        box[y0:y1, x0:x1] = True
        w = ndi.gaussian_filter(box.astype(np.float32), 6)
        sl = (slice(max(y0 - 24, 0), min(y1 + 24, H)), slice(max(x0 - 24, 0), min(x1 + 24, W)))
        a = out[sl]
        L = np.array(LIGHT[colour], np.float32)
        ring = ndi.binary_dilation(box, iterations=30) & ~ndi.binary_dilation(box, iterations=4)
        ref = P_REF[kind if kind != "emit" else "night"][ring]
        if colour == "green":
            # the unlit G/R of the surroundings (30th percentile: the ring itself is partly green-lit at night)
            kg = float(np.clip(np.percentile(ref[:, 1] / np.maximum(ref[:, 0], 1e-3), 30), 0.70, 0.97))
            # amount s of light (colour L) to remove so that G - s = kg (R - L_r s), or so that G no longer
            # tops B (a neutral grey like the door metal is not green light) - whichever removes less
            s_r = (a[..., 1] - kg * a[..., 0]) / (1.0 - kg * L[0])
            s_b = (a[..., 1] - a[..., 2]) / (1.0 - L[2])
            s_amt = np.minimum(s_r, s_b)
        else:
            ratio = ref[:, 0] / np.maximum(np.maximum(ref[:, 1], ref[:, 2]), 1e-3)
            k = float(np.clip(np.percentile(ratio, 75), 1.05, 1.6))
            # R - s = k (G - L_g s)
            s_amt = (a[..., 0] - k * a[..., 1] - (0 if emit else 0.02)) / (1.0 - k * L[1])
        s_amt = np.clip(s_amt, 0, None)
        fixed = np.clip(a - s_amt[..., None] * L[None, None, :], 0, 1)
        if name == "green_bar" and not emit:
            # the lamp's pale highlight line (near white, not orange like the sconce light) goes down to the
            # brightest unlit tone around it
            cap = float(np.percentile(lum(ref), 90))
            lf = lum(fixed)
            hl = (lf > cap) & (a[..., 1] >= 0.9 * a[..., 0])
            fixed[hl] = fixed[hl] * (cap / np.maximum(lf[hl], 1e-4))[:, None]
        ww = (w[sl] * ~keep[sl])[..., None]          # the lenses themselves keep their light
        out[sl] = a * (1 - ww) + fixed * ww
    return out


P_REF = {}


def lens_union(kind):
    """Every lamp lens (grown) in this plate's frame: despill never touches the glass itself."""
    fr = "day" if kind == "day" else "night"
    m = np.zeros(P_REF["day"].shape[:2], bool)
    for z in ("lamp_red", "lamp_amber", "lamp_green", "side_red", "side_green"):
        m |= sam(fr, z)
    return m


def lamp_lenses(kind, p, which):
    """Lens masks (one per lamp) in plate frame `kind` for the top cluster or the side indicator."""
    fr = "day" if kind == "day" else "night"
    if which == "top":
        names = {"red": "lamp_red", "amber": "lamp_amber", "green": "lamp_green"}
    else:
        names = {"red": "side_red", "green": "side_green"}
    # raw SAM lens plus one px of its anti-aliased edge; the housing and bezel stay painted
    return {c: ndi.binary_dilation(sam(fr, z), iterations=1) for c, z in names.items()}


def lamp_state(P, p, which, kind, lit_colours, pad=24):
    """Image (or emit) of a window around the piece with only `lit_colours` lit; returns (window, (x0, y0))."""
    bx0, by0, bx1, by1 = frame_box(p, kind)
    H, W = P["day"].shape[:2]
    x0, y0, x1, y1 = max(bx0 - pad, 0), max(by0 - pad, 0), min(bx1 + pad, W), min(by1 + pad, H)
    img = P["night" if kind == "emit" else kind][y0:y1, x0:x1].copy()
    killed = np.zeros(img.shape[:2], np.float32)
    lit_w = np.zeros(img.shape[:2], np.float32)
    for colour, lens in lamp_lenses(kind, p, which).items():
        lw = lens[y0:y1, x0:x1]
        if colour in lit_colours:      # a lit lens is the painted pixels, untouched
            lit_w = np.maximum(lit_w, np.maximum(ndi.gaussian_filter(lw.astype(np.float32), 0.7), lw))
            continue
        img, w = lamp_off(img, lw, colour)
        killed = np.maximum(killed, w)
    if kind == "emit":
        # unlit lens: black in emit; lit lens: the painted night glass itself, so its core is solid (the plate's
        # emit map only holds the saturated rim of a blown-out lens)
        em = P["emit"][y0:y1, x0:x1] * (1 - killed[..., None])
        return np.maximum(em, img * lit_w[..., None]), (x0, y0)
    return img, (x0, y0)


# ----------------------------------------------------------------------------------------------- curtain glow
def curtain_split(img):
    """inert (glow taken out) and glow (img - inert) for curtain pixels: the bright folds are pressed toward the dark
    folds (35% of their contrast kept) and the green is calmed 20%, so the velvet stays but stops shining."""
    L = lum(img)
    L0 = np.percentile(L, 25)
    Lt = np.where(L > L0, L0 + (L - L0) * 0.35, L)
    inert = img * (Lt / np.maximum(L, 1e-4))[..., None]
    g = lum(inert)[..., None]
    inert = np.clip(inert * 0.8 + g * 0.2, 0, 1)
    return inert, np.clip(img - inert, 0, 1)


def green_neon_off(img):
    """Unlit version of green neon (the Time Crisis screen and the light on its hose): bright, strongly green pixels
    lose most of their green excess and value; everything else is untouched."""
    ge = img[..., 1] - np.maximum(img[..., 0], img[..., 2])
    w = smoothstep(0.08, 0.30, ge) * smoothstep(0.25, 0.55, img.max(-1))
    w = ndi.gaussian_filter(w, 1.0)[..., None]
    g = lum(img)[..., None]
    off = np.clip(0.55 * (0.6 * g + 0.4 * img), 0, 1)
    return img * (1 - w) + off * w


# ----------------------------------------------------------------------------------------------- vapour
def vapour_alpha(P, kind, pieces):
    """Provisional vapour opacity in plate frame `kind` (day or night) from a green-excess unmix against the floor
    around it; returns (alpha, fog colour)."""
    img = P[kind]
    H, W = img.shape[:2]
    objs = np.zeros((H, W), bool)
    for n in ("tc", "curtain"):
        objs |= frame_mask(pieces[n], kind)
    objs = ndi.binary_dilation(objs, iterations=2)
    x0, y0, x1, y1 = VAPOUR_BOX[kind]
    reg = np.zeros((H, W), bool)
    reg[y0:y1, x0:x1] = True
    reg &= ~objs
    e = img[..., 1] - (img[..., 0] + img[..., 2]) / 2
    sel = e[reg]
    F = np.median(img[reg][sel > np.percentile(sel, 97)], 0)
    if kind == "night":
        # the night floor is lit green all over, so green excess cannot tell vapour from reflection; the emit plate
        # holds the vapour as saturated wisps (the floor reflections are not neon), so the opacity comes from it
        em = P["emit"]
        ge = em[..., 1] - np.maximum(em[..., 0], em[..., 2])            # green neon only (no orange lamp glints)
        a = np.clip(ge / max(float(F[1] - max(F[0], F[2])), 1e-3) * 1.3, 0, 0.85)
    else:
        ring = ndi.binary_dilation(reg, iterations=30) & ~ndi.binary_dilation(reg, iterations=6) & ~objs
        t = float(np.percentile(e[ring], 50))
        eF = float(F[1] - (F[0] + F[2]) / 2)
        a = np.clip((e - t) / (eF - t), 0, 0.85)
    a = ndi.gaussian_filter(a, 1.5)
    # the matte the Gemini holes were cut for (the fills were made for those crops): keep it for the hole only
    a_hole = a * np.clip(ndi.gaussian_filter(reg.astype(np.float32), 8) * reg * 1.5, 0, 1)
    a_hole[a_hole < 0.03] = 0
    # gate C round 1: the search box's own sides showed as straight steps on the floor. The alpha now ramps to 0
    # over VAPOUR_RAMP px towards the box sides (not towards the cabinet and curtain, which it meets)
    box = np.zeros((H, W), bool)
    box[y0:y1, x0:x1] = True
    ramp = np.clip(ndi.distance_transform_edt(box) / VAPOUR_RAMP, 0, 1)
    ramp = (ramp * ramp * (3 - 2 * ramp)) * reg
    a = a * ramp
    a[a < 0.03] = 0
    return a.astype(np.float32), F, ramp.astype(np.float32), a_hole.astype(np.float32)


# ----------------------------------------------------------------------------------------------- door placement
def project(x, y, z):
    """Room camera (CAM) projection of a point in tiles to plate px (the gd's own fit is approximate)."""
    import math
    p = math.radians(CAM["pitch"])
    vx, vy, vz = x, y - CAM["height"], z - CAM["z"]
    d = -vy * math.sin(p) - vz * math.cos(p)
    vu = vy * math.cos(p) - vz * math.sin(p)
    return (1376.0 + CAM["focal"] * vx / d, 768.0 - CAM["focal"] * vu / d)


def door_placement(pieces):
    """Anchor, interaction point, collision and height for the maintenance door spec."""
    leaf = pieces["door_leaf"]
    out = {"anchor": {}, "pieces_anchor": {}}
    for k in KINDS:
        m = frame_mask(leaf, k)
        ys, xs = np.nonzero(m)
        yb = int(ys.max())
        xb = xs[ys >= yb - 3]
        out["anchor"][k] = {"origin": "bottom_centre_of_leaf", "plate_px": [int(round(float(xb.mean()))), yb]}
        for n in ("lamps_top", "lamps_side"):
            bx = frame_box(pieces[n], k)
            out["pieces_anchor"].setdefault(n, {})[k] = {"origin": "box_centre",
                                                         "plate_px": [(bx[0] + bx[2]) // 2, (bx[1] + bx[3]) // 2]}
    (ax, az), (sx, sz) = DOOR_POINT
    m = frame_mask(leaf, "night")
    cols = np.nonzero(m.any(0))[0]
    edges = []
    for c in (cols.min() + 4, cols.max() - 4):    # the leaf's two vertical edges (the top and bottom are slanted)
        ys = np.nonzero(m[:, c])[0]
        edges.append(float(ys.max() - ys.min()))
    span_px = sum(edges) / 2
    px_per_tile = project(ax, 0, az)[1] - project(ax, 1, az)[1]
    out["interaction_point"] = {
        "id": "maintenance_door",
        "source": "game/worlds/debaucheryville/absinthe_arcade_north_wing_hd2d.gd:37 INTERACT_POINTS (read only)",
        "anchor_tiles_xz": [ax, az], "stand_tiles_xz": [sx, sz],
        "anchor_m_xz": [round(ax * CAM["tile_m"], 2), round(az * CAM["tile_m"], 2)],
        "stand_m_xz": [round(sx * CAM["tile_m"], 2), round(sz * CAM["tile_m"], 2)],
        "anchor_plate_px_by_room_camera": [round(v) for v in project(ax, 0, az)],
        "note": "the room camera fit is approximate (gd:7-11); the painted door base is at anchor.plate_px"}
    out["collision_footprint"] = ("none: the door is flush in the right wall, which the room's right_wall collider "
                                  "already blocks (gd _build_room); the door is a hotspot, not a blocker")
    out["height_m"] = round(span_px / px_per_tile * CAM["tile_m"], 2)
    out["height_note"] = ("mean length of the leaf's two vertical edges in px (night, %.0f and %.0f) over the room "
                          "camera's px per tile at the anchor depth (%.1f), x 0.67 m. Approximate like the camera fit "
                          "(gd:7-11); the painted door reads tall for the bros" % (edges[0], edges[1], px_per_tile))
    return out


# ----------------------------------------------------------------------------------------------- fills
def plaque_fill(img, hole):
    """Jamb stone under the plaque copied straight up (the jamb face is plain stone), seam softened one px."""
    x0, y0, x1, y1 = bbox(hole)
    h = (y1 - y0) + 4
    out = img.copy()
    ys, xs = np.nonzero(hole)
    out[ys, xs] = img[np.minimum(ys + h, img.shape[0] - 1), xs]
    ring = hole & ~ndi.binary_erosion(hole, iterations=1)
    blur = ndi.uniform_filter(out, size=(3, 3, 1))
    out[ring] = blur[ring]
    return out


def gemini_paste(base, fill_crop, box, mask_full):
    """Paste a returned edit of `box` inside the feathered mask, tone-matched on a band just outside it."""
    x0, y0, x1, y1 = box
    fill = fill_crop
    if fill.shape[:2] != (y1 - y0, x1 - x0):
        # a resize would silently misregister the fill: the crop box moved since the fill was made
        raise SystemExit("fill is %s but the crop box %s is %dx%d: re-prepare the fill" %
                         (fill.shape[:2][::-1], box, x1 - x0, y1 - y0))
    soft = ndi.gaussian_filter(ndi.binary_dilation(mask_full, iterations=6).astype(np.float32), 3)[y0:y1, x0:x1]
    inside = soft > 0.02
    band = ndi.binary_dilation(inside, iterations=30) & ~inside
    crop = base[y0:y1, x0:x1]
    gain = crop[band].mean(0) / np.maximum(fill[band].mean(0), 1e-4)
    fill = np.clip(fill * gain, 0, 1)
    out = base.copy()
    out[y0:y1, x0:x1] = crop * (1 - soft[..., None]) + fill * soft[..., None]
    return out, soft


def night_from_day(day_clean_full, night, hole_night, offset, near):
    """Night pixels for a hole from a clean day fill: affine colour fit day->night on the surroundings (cut_plate_prop
    method), with the day image moved into the night frame by the piece's offset."""
    dshift = shift(day_clean_full, *offset)
    fit = near & ~ndi.binary_dilation(hole_night, iterations=40)
    X = np.concatenate([dshift[fit], np.ones((int(fit.sum()), 1), np.float32)], 1)
    M, *_ = np.linalg.lstsq(X, night[fit], rcond=None)
    H, W = night.shape[:2]
    pred = np.clip((np.concatenate([dshift.reshape(-1, 3), np.ones((H * W, 1), np.float32)], 1) @ M).reshape(H, W, 3), 0, 1)
    return pred


BOXES_NOTE = ("Per-plate boxes for PlatePropLayer (Eurobound-10g6), keyed by sprite prefix: each is the top-left and size "
              "where that plate paints the piece. Measured 2026-11-17 by masked SSD of each painted-state cut-out against "
              "its own plate (best match at exactly these boxes); emit is the night frame.")


def loader_boxes(sprites):
    """{prefix: {variant: [x, y, w, h]}} from a spec's sprites, for plate_prop_layer.gd's "boxes" (Eurobound-10g6).
    Every state of a prefix shares one box per variant; emit is cut in the night frame."""
    boxes = {}
    for fn, s in sprites.items():
        prefix = fn[:-len("_%s_%s.png" % (s["state"], s["variant"]))]
        r = [s["x"], s["y"], s["w"], s["h"]]
        if boxes.setdefault(prefix, {}).setdefault(s["variant"], r) != r:
            raise ValueError("%s: %s box differs between states" % (prefix, s["variant"]))
    return boxes


def with_boxes(spec):
    """The spec with "boxes_note" and "boxes" placed just before "sprites"."""
    out = {}
    for k, v in spec.items():
        if k == "sprites":
            out["boxes_note"] = BOXES_NOTE
            out["boxes"] = loader_boxes(v)
        if k not in ("boxes", "boxes_note"):
            out[k] = v
    return out


# ----------------------------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--review", help="write review images for the blind reviewer here")
    ap.add_argument("--fill", action="append", default=[], help="NAME=PNG, NAME in ddr_day ddr_night left_day left_night")
    a = ap.parse_args()
    fills = dict(f.split("=", 1) for f in a.fill)
    os.makedirs(CLEAN, exist_ok=True)
    os.makedirs(GEM, exist_ok=True)
    open(os.path.join(OUT, ".gdignore"), "w").close()

    P = load_plates()
    P_REF.update(P)
    H, W = P["day"].shape[:2]
    pieces = build_pieces(P)
    # the door pieces (and their lamp states) are cut from plates with the painted lamp light taken off
    PD = {k: despill(P[k], k, pieces["door_leaf"]["offset"], emit=(k == "emit")) for k in KINDS}
    for n, p in pieces.items():
        print("%-10s offset %-10s iou %.3f alpha %-9s night box %s" % (n, p["offset"], p["iou"], p["alpha"],
                                                                     p["boxes"]["night"]))

    clean = {k: P[k].copy() for k in KINDS}
    changed = {k: np.zeros((H, W), bool) for k in KINDS}       # every pixel any fill touched (self-check)
    status = {}
    specs = {}
    layers = {}                                               # name -> {kind: rgba} for review composites

    def mark(kind, m):
        changed[kind] |= m

    def fr(kind):
        return "day" if kind == "day" else "night"

    # ---- N2 door leaf: doorway void behind it ----
    p = pieces["door_leaf"]
    for k in KINDS:
        # the void stops one px inside the leaf: under the leaf's soft outline the plate keeps its own pixels,
        # so the closed door composites back without a dark rim
        hole = ndi.binary_erosion(frame_mask(p, k), iterations=1)
        clean[k][hole] = np.array(VOID[k], np.float32) / 255.0
        mark(k, hole)
    status["maintenance_door_leaf"] = "script fill: doorway void (flat, as the front doors)"

    # ---- N2 lamps: every lamp dark on the plate; states on the layer ----
    for piece, which in (("lamps_top", "top"), ("lamps_side", "side")):
        p = pieces[piece]
        for k in KINDS:
            m = ndi.binary_dilation(frame_mask(p, k), iterations=1)
            off_all, (ox, oy) = lamp_state(PD, p, which, k, ())
            h, w = off_all.shape[:2]
            win = clean[k][oy:oy + h, ox:ox + w]
            win[m[oy:oy + h, ox:ox + w]] = off_all[m[oy:oy + h, ox:ox + w]]
            mark(k, m)
    # the painted lamp light on the frame and floor comes off too (the unlock light is a code light)
    for k in KINDS:
        before = clean[k]
        clean[k] = despill(before, k, pieces["door_leaf"]["offset"], emit=(k == "emit"))
        mark(k, np.abs(clean[k] - before).max(-1) > 0)
    status["maintenance_door_lamps"] = ("script fill: every lens derived as unlit near-black glass; the painted lamp "
                                        "light on the frame bar, frame corner, side-panel surround, threshold and "
                                        "floor clamped back to the unlit tone (despill, SPILL_BOXES)")

    # ---- N3 curtain: void in the arch; plaque: stone from below ----
    p = pieces["curtain"]
    for k in KINDS:
        hole = ndi.binary_erosion(frame_mask(p, k), iterations=1) & ~frame_mask(pieces["tc"], k)
        clean[k][hole] = np.array(VOID[k], np.float32) / 255.0
        mark(k, hole)
    status["taproom_curtain"] = "script fill: arch opening void (the curtain layer always covers it)"
    p = pieces["plaque"]
    for k in KINDS:
        hole = ndi.binary_dilation(frame_mask(p, k), iterations=3)
        clean[k] = plaque_fill(clean[k], hole)
        mark(k, ndi.binary_dilation(hole, iterations=1))
    status["taproom_plaque"] = "script fill: jamb stone copied up from below the plaque"

    # ---- vapour (provisional) ----
    vap = {k: vapour_alpha(P, k, pieces) for k in ("day", "night")}

    # ---- Gemini holes: DDR, and the left corner (cabinet + gun + vapour) ----
    gem_holes = {}
    for k in ("day", "night"):
        # the hole takes the shared alpha and what this plate's own SAM mask calls the object next to it (not its
        # far leaks: the night DDR mask runs into the potted plant)
        A = pieces["ddr"]["hole_masks"]["day" if k == "day" else "night"]   # the matte the fills were made for
        own = pieces["ddr"]["own"][k] & ndi.binary_dilation(A, iterations=8)
        gem_holes["ddr_" + k] = ndi.binary_dilation(A | own, iterations=4)
        left = pieces["tc"]["hole_masks"]["day" if k == "day" else "night"] | pieces["tc"]["own"][k] | (vap[k][3] > 0.03)
        gem_holes["left_" + k] = ndi.binary_dilation(ndi.binary_closing(left, iterations=4), iterations=4)
    prompt = ("Edit only the area under the white mask. Remove the object there and fill it with what is behind it: "
              "continue the surrounding {what} with the same perspective, lighting, brush style and colours as the "
              "rest of the painting. Add nothing new: no objects, no people, no text, no smoke or mist, no glow. "
              "Keep every pixel outside the mask unchanged and keep the image size.")
    what = {"ddr": "stone wall, wall cables and checkerboard marble floor tiles (tile edges must line up with the "
                   "neighbouring tiles)",
            "left": "green velvet curtain (vertical folds down to the floor inside the stone arch), the stone arch "
                    "jamb and the checkerboard marble floor tiles (tile edges must line up)"}
    gem_info = {}
    for name, hole in gem_holes.items():
        item, k = name.rsplit("_", 1)
        box = bbox(hole, pad=GEM_PAD)
        x0, y0, x1, y1 = box
        Image.fromarray(u8(P[k][y0:y1, x0:x1])).save(os.path.join(GEM, "%s_crop.png" % name))
        Image.fromarray(np.where(hole[y0:y1, x0:x1], 255, 0).astype(np.uint8)).save(os.path.join(GEM, "%s_mask.png" % name))
        # a red-tinted preview of the mask over the crop, for whoever drives the browser
        prev = P[k][y0:y1, x0:x1].copy()
        prev[hole[y0:y1, x0:x1]] = prev[hole[y0:y1, x0:x1]] * 0.4 + np.array([1, 0, 0]) * 0.6
        Image.fromarray(u8(prev)).save(os.path.join(GEM, "%s_mask_preview.png" % name))
        txt = prompt.format(what=what[item])
        with open(os.path.join(GEM, "%s_prompt.txt" % name), "w", encoding="utf-8", newline="\n") as f:
            f.write(txt + "\n")
        gem_info[name] = {"plate": "%s_%s.png" % (BASE, k), "crop_box_px": list(box), "crop": "%s_crop.png" % name,
                          "mask": "%s_mask.png" % name, "prompt": "%s_prompt.txt" % name,
                          "return_as": "gemini/fills/%s.png (same size as the crop)" % name,
                          "filled": name in fills}

    # ---- apply fills that exist ----
    left_fill_day = None
    for item, piece in (("ddr", "ddr"), ("left", "tc")):
        p = pieces[piece]
        for k in ("day", "night"):
            name = "%s_%s" % (item, k)
            if name not in fills:
                continue
            box = gem_info[name]["crop_box_px"]
            fc = f32(Image.open(fills[name]).convert("RGB"))
            clean[k], soft = gemini_paste(clean[k], fc, box, gem_holes[name])
            m = np.zeros((H, W), bool)
            m[box[1]:box[3], box[0]:box[2]] = soft > 0
            mark(k, m)
            if item == "left" and k == "day":
                left_fill_day = clean["day"].copy()
        dn, nn = "%s_day" % item, "%s_night" % item
        if dn in fills and nn not in fills:
            hn = gem_holes[nn]
            near = np.zeros((H, W), bool)
            x0, y0, x1, y1 = bbox(hn, pad=160)
            near[y0:y1, x0:x1] = True
            pred = night_from_day(clean["day"], P["night"], hn, p["offset"], near)
            soft = ndi.gaussian_filter(ndi.binary_dilation(hn, iterations=6).astype(np.float32), 3)
            clean["night"] = clean["night"] * (1 - soft[..., None]) + pred * soft[..., None]
            mark("night", soft > 0)
        for k in ("day", "night"):
            if "%s_%s" % (item, k) in fills or (k == "night" and dn in fills):
                hk = gem_holes["%s_%s" % (item, k)]
                soft = ndi.gaussian_filter(ndi.binary_dilation(hk, iterations=6).astype(np.float32), 3)
                if k == "night":
                    clean["emit"] = clean["emit"] * (1 - soft[..., None]) + emit_map(clean["night"]) * soft[..., None]
                    mark("emit", soft > 0)
        done = [k for k in ("day", "night") if "%s_%s" % (item, k) in fills or (k == "night" and dn in fills)]
        status[item] = ("Gemini fill composited: " + ", ".join(done)) if done else "NEEDS GEMINI FILL (gemini/%s_*)" % item

    # The left fill puts velvet where the cabinet hid the curtain: that velvet joins the curtain layer and the plate
    # under it becomes void like the rest of the arch.
    if left_fill_day is not None:
        for k in ("day", "night"):
            src = clean[k]
            hole = gem_holes["left_" + k]
            g = src[..., 1] - np.maximum(src[..., 0], src[..., 2])
            velvet = hole & (g > 0.06)
            cur = frame_mask(pieces["curtain"], k)
            x0, _, x1, _ = bbox(cur)
            velvet[:, :x0] = False
            velvet[:, x1:] = False
            lab, n = ndi.label(velvet | cur)
            keep = np.isin(lab, np.unique(lab[cur]))
            # gate C round 1: the per-pixel green test left holes and a torn right edge in the dark folds; close,
            # fill and smooth the velvet as one cloth, kept inside the curtain's column span and the hole
            keep = ndi.binary_closing(np.pad(keep, 8), iterations=8)[8:-8, 8:-8]
            keep = ndi.binary_fill_holes(keep)
            keep = ndi.binary_opening(keep, iterations=3)
            keep = (ndi.gaussian_filter(keep.astype(np.float32), 2.5) > 0.5)
            keep[:, :x0] = False
            keep[:, x1:] = False
            ext = keep & ~cur & (hole | ndi.binary_dilation(cur, iterations=3))
            pieces["curtain"].setdefault("ext", {})[k] = (ext, src.copy())
        pc = pieces["curtain"]
        for fr in ("day", "night"):
            pc["masks"][fr] = ndi.binary_fill_holes(pc["masks"][fr] | pc["ext"][fr][0])
        set_boxes(pc)
        for k in KINDS:
            under = frame_mask(pc, k) & frame_mask(pieces["tc"], k)    # arch opening behind the cabinet -> void
            clean[k][under] = np.array(VOID[k], np.float32) / 255.0
            mark(k, under)
        status["taproom_curtain"] += "; hidden part behind the cabinet taken from the left fill"

    # ---- write layers and specs ----
    def write_piece(prefix, piece_name, states, per_kind, spec_extra, files_index):
        """states: {state: {kind: rgba crop}}; writes <prefix>_<state>_<kind>.png"""
        p = pieces[piece_name]
        x0, y0, x1, y1 = p["boxes"]["night"]
        sprites = {}
        for st, kinds in states.items():
            for k, arr in kinds.items():
                fn = "%s_%s_%s.png" % (prefix, st, k)
                save_rgba(arr, fn)
                bx = frame_box(p, k)
                sprites[fn] = {"plate": "%s_%s.png" % (BASE, k), "x": bx[0], "y": bx[1], "w": x1 - x0, "h": y1 - y0,
                               "plate_size": [W, H], "state": st, "variant": k}
        files_index.update(sprites)
        return {"plate_size": [W, H], "size": [x1 - x0, y1 - y0],
                "plate_xy": {k: list(frame_box(p, k)[:2]) for k in KINDS},
                "day_to_night_offset_px": list(p["offset"]), "day_night_mask_iou": p["iou"], "alpha": p["alpha"],
                "sam_zones": p["zones"], **spec_extra}

    def cut(piece, kind, img=None, origin=(0, 0)):
        return crop_layer(P, pieces[piece], kind, img, origin)

    # N1 DDR
    sprites = {}
    st = {"error": {k: cut("ddr", k) for k in KINDS}}
    pulse = {}
    for k in ("day", "night"):
        base = P[k]
        glow = ndi.gaussian_filter(emit_map(base), (3, 3, 0))
        pulse[k] = cut("ddr", k, np.clip(base + 0.9 * glow + 0.6 * emit_map(base), 0, 1))
    pulse["emit"] = cut("ddr", "emit", np.clip(P["emit"] * 1.8 + ndi.gaussian_filter(P["emit"], (3, 3, 0)), 0, 1))
    st["unlock_pulse"] = pulse
    layers["ddr"] = st["error"]
    spec = write_piece("aa_cab_ddr_broken", "ddr", st, None, {}, sprites)
    spec.update({"asset_id": "aa_cab_ddr_broken", "interaction_id": "broken_ddr", "node_id": "aa_node_broken_ddr",
                 "bead": BEAD, "states": {s: {k: "aa_cab_ddr_broken_%s_%s.png" % (src, k) for k in KINDS} for s, src in
                                          (("error", "error"), ("token_0_of_3", "error"), ("token_1_of_3", "error"),
                                           ("token_2_of_3", "error"), ("token_3_of_3", "error"),
                                           ("unlock_pulse", "unlock_pulse"))},
                 "derivation": {"error": "the painted machine (cracked pad, screen as painted)",
                                "token_N_of_3": "error art; the pips are a code stand-in until Eurobound-w2ig",
                                "unlock_pulse": "error + its own neon (hall emit rule) added back as a soft glow; emit x1.8"},
                 "clean_plate": status.get("ddr"), "sprites": sprites})
    specs["aa_cab_ddr_broken"] = spec

    # N2 door: leaf + lamps
    sprites = {}
    leaf = {"closed": {k: cut("door_leaf", k, PD[k]) for k in KINDS}}
    layers["door_leaf"] = leaf["closed"]
    s_leaf = write_piece("aa_transition_maintenance_door", "door_leaf", leaf, None, {}, sprites)
    lamp_specs = {}
    for piece, which, prefix in (("lamps_top", "top", "aa_transition_maintenance_door_lamps_top"),
                                 ("lamps_side", "side", "aa_transition_maintenance_door_lamps_side")):
        sts = {}
        lamp_states = [("locked_red", ("red",)), ("unlocked_green", ("green",))]
        if which == "top":     # only the top cluster has an amber lens (author, Desk Eurobound-59b9-q2)
            lamp_states.append(("unlocking_amber", ("amber",)))
        for state, lit in lamp_states:
            sts[state] = {k: cut(piece, k, *lamp_state(PD, pieces[piece], which, k, lit)) for k in KINDS}
        layers[piece] = sts["locked_red"]
        lamp_specs[prefix] = write_piece(prefix, piece, sts, None, {}, sprites)
    specs["aa_transition_maintenance_door"] = {
        "asset_id": "aa_transition_maintenance_door", "interaction_id": "maintenance_door",
        "node_id": "aa_node_maintenance_door", "bead": BEAD,
        "note": "three pieces, each with its own box: the leaf (sign, latch) and two lamp pieces. Draw order: leaf, "
                "lamps_top, lamps_side. The side lamp is ALWAYS drawn over the leaf: the leaf has a notch where the "
                "side indicator sits, and only the side piece fills it. State from the flag "
                "arcade_maintenance_restroom_unlocked. The lit lamp's glow on the frame and floor is not painted: "
                "it is the code light (gd:146-152).",
        **door_placement(pieces),
        "states": {
            "locked_red": {"leaf": "closed", "lamps_top": "locked_red", "lamps_side": "locked_red"},
            "unlocked_green": {"leaf": "closed", "lamps_top": "unlocked_green", "lamps_side": "unlocked_green"},
            "unlocking_amber_flash": {"leaf": "closed", "lamps_top": "unlocking_amber", "lamps_side": "locked_red"},
            "opening_exterior_only": "NO ART (author, Desk Eurobound-59b9-q3: 'No new art: the scene fades or cuts "
                                     "away as the door starts to open'). Scene step: when the door starts to open, "
                                     "fade or cut away; the leaf stays 'closed' until the fade covers it."},
        "amber_behaviour": "author, Desk Eurobound-59b9-q2: 'Amber flashes briefly while the door unlocks, then goes "
                           "dark'. Scene step: when arcade_maintenance_restroom_unlocked turns true, show "
                           "unlocking_amber_flash briefly, then unlocked_green; amber is dark in every other state. "
                           "The flash length is the scene step's choice. The side indicator has no amber lens, so it "
                           "keeps locked_red during the flash (a default the scene step may change).",
        "derivation": {"lit lamp": "the painted lit lens (tight matte: lens and bezel only, edge colour from the "
                                   "nearest interior pixel)",
                       "dark lamp": "derived from the painted lens: near-black unlit glass, same rule day and night; "
                                    "emit zeroed there",
                       "amber": "the painted lit amber lens (it is lit in the plate, day and night), cut the same way "
                                "as red and green: lamps_top unlocking_amber = amber lit, red and green dark"},
        "qc": "try 3 accepted by the author as it is (Desk Eurobound-59b9-q1, 2026-11-18: 'Accept try 3 as it is: "
              "the remaining faults are small at game size'); the amber state passes its own gate C",
        "clean_plate": status["maintenance_door_leaf"] + "; " + status["maintenance_door_lamps"],
        "pieces": {"leaf": s_leaf, **{k.rsplit("_", 2)[-2] + "_" + k.rsplit("_", 1)[-1]: v for k, v in lamp_specs.items()}},
        "sprites": sprites}

    # N3 curtain, glow, plaque
    sprites = {}
    cur_states = {s: {} for s in GLOW_K}
    glow_layer = {}
    for k in ("day", "night"):
        src = P[k]
        m = frame_mask(pieces["curtain"], k)
        img = src.copy()
        ext = pieces["curtain"].get("ext", {}).get(k)
        if ext is not None:
            img[ext[0]] = ext[1][ext[0]]
        inert, glow = curtain_split(img[m])
        for s, kk in GLOW_K.items():
            full = img.copy()
            full[m] = img[m] if kk == 1.0 else np.clip(inert + kk * glow, 0, 1)   # full glow = the painted pixels
            cur_states[s][k] = cut("curtain", k, full)
        gfull = np.zeros_like(img)
        gfull[m] = glow
        glow_layer[k] = cut("curtain", k, gfull)
    em_src = P["emit"].copy()
    ext = pieces["curtain"].get("ext", {}).get("night")
    if ext is not None:
        em_src[ext[0]] = emit_map(ext[1])[ext[0]]
    for s, kk in GLOW_K.items():
        cur_states[s]["emit"] = cut("curtain", "emit", em_src * kk)
    glow_layer["emit"] = cut("curtain", "emit", em_src)
    layers["curtain"] = cur_states["night_breathing"]
    s_cur = write_piece("aa_transition_taproom_curtain", "curtain", cur_states, None, {}, sprites)
    s_glow = write_piece("aa_transition_taproom_glow", "curtain", {"additive": glow_layer}, None, {}, sprites)
    plaque = {"default": {k: cut("plaque", k) for k in KINDS}}
    layers["plaque"] = plaque["default"]
    s_plq = write_piece("aa_transition_taproom_plaque", "plaque", plaque, None, {}, sprites)
    specs["aa_transition_taproom_curtain"] = {
        "asset_id": "aa_transition_taproom_curtain", "interaction_id": "taproom_curtain",
        "node_id": "aa_node_taproom_curtain", "bead": BEAD, "active_hours": "20:00_to_04:00",
        "states": {s: {"curtain": s, "plaque": "default"} for s in GLOW_K},
        "glow_factor": GLOW_K,
        "derivation": {"day_inert": "the painted curtain with its glow taken out (bright folds pressed to 35% of their "
                                    "contrast over the dark folds, green calmed 20%)",
                       "evening_faint": "inert + 0.35 x glow", "night_breathing": "the painted curtain (inert + glow)",
                       "discovered": "inert + 0.5 x glow ('subtle after 20:00')",
                       "aa_transition_taproom_glow": "glow alone (painted - inert), RGB to ADD over the curtain for the "
                                                     "5 s breathing loop; alpha = the curtain alpha",
                       "plaque": "the painted brass plaque, one state, its own box (the day relight moved it relative "
                                 "to the curtain, so it cannot share the curtain's box)"},
        "glow_spill_note": "the green light the glow throws on the jambs and floor stays painted on the plate",
        "clean_plate": status["taproom_curtain"] + "; plaque: " + status["taproom_plaque"],
        "behind_cabinet": "complete" if pieces["curtain"].get("ext") else
                          "MISSING until the left Gemini fill: the curtain layer has no pixels where the cabinet hides it",
        "pieces": {"curtain": s_cur, "glow": s_glow, "plaque": s_plq}, "sprites": sprites}

    # N4 Time Crisis
    sprites = {}
    p = pieces["tc"]
    night_dim = green_neon_off(P["night"])
    tc = {"displaced_revealed": {"day": cut("tc", "day", green_neon_off(P["day"])), "night": cut("tc", "night", night_dim),
                                 "emit": cut("tc", "emit", np.zeros_like(P["emit"]))},
          "night_glow": {k: cut("tc", k) for k in KINDS}}
    # curtain_hidden: move the cabinet right until its body's right edge meets the curtain's right edge at the floor
    body = sam("night", "tc_cabinet")
    cm = pieces["curtain"]["masks"]["night"]
    cy0, cy1 = bbox(cm)[1], bbox(cm)[3]
    # the curtain's right edge over its lower half (the left fill's hem slopes down to the left, so its last rows
    # alone no longer reach the right jamb: gate C round 1 found a 0 px shift)
    low = slice((cy0 + cy1) // 2, cy1)
    cur_right = int(np.nonzero(cm[low].any(0))[0].max())
    by0, by1 = bbox(body)[1], bbox(body)[3]
    blow = slice(by1 - max((by1 - by0) // 6, 8), by1)
    body_right = int(np.nonzero(body[blow].any(0))[0].max())
    hide_dx = max(cur_right - body_right, 0)
    # one box for both poses: widen the piece to the right by hide_dx, and down by SHADOW_PAD for the contact shadow
    for fr in ("day", "night"):
        bx0, by0, bx1, by1 = p["boxes"][fr]
        p["boxes"][fr] = (bx0, by0, bx1 + hide_dx, by1 + SHADOW_PAD)

    def widen(rgba):
        out = np.zeros((rgba.shape[0] + SHADOW_PAD, rgba.shape[1] + hide_dx, 4), np.float32)
        out[:rgba.shape[0], :rgba.shape[1]] = rgba
        return out

    def contact_shadow(rgba, strength):
        """Gate C round 1: the fill removed the floor shadow, so the cabinet floated. A soft dark pool round the
        base, in the layer itself (it moves with the cabinet in curtain_hidden); never over the cabinet."""
        a = rgba[..., 3]
        rows = np.nonzero(a.max(1) > 0.5)[0]
        base = int(rows.max())
        foot = np.zeros_like(a)
        foot[max(base - 28, 0):base + 1] = a[max(base - 28, 0):base + 1]
        foot = np.roll(foot, 5, axis=0)
        s = np.clip(ndi.gaussian_filter(foot, (5, 9)) * 1.6, 0, 1) * strength
        new_a = a + (1 - a) * s
        dark = np.array([0.04, 0.035, 0.05], np.float32)
        rgb = (rgba[..., :3] * a[..., None] + dark * (new_a - a)[..., None]) / np.maximum(new_a, 1e-4)[..., None]
        return np.dstack([rgb, new_a])
    for s in tc:
        for k in KINDS:
            tc[s][k] = widen(tc[s][k])
            if k != "emit":
                tc[s][k] = contact_shadow(tc[s][k], 0.55 if k == "day" else 0.65)
    tc["curtain_hidden"] = {k: np.roll(tc["displaced_revealed"][k], hide_dx, axis=1) for k in KINDS}
    for k in KINDS:
        tc["curtain_hidden"][k][:, :hide_dx] = 0
    layers["tc"] = tc["night_glow"]
    s_tc = write_piece("aa_cab_time_crisis_cracked", "tc", tc, None, {}, sprites)
    s_tc.update({"asset_id": "aa_cab_time_crisis_cracked", "interaction_id": "cracked_time_crisis_cabinet",
                 "node_id": "aa_node_taproom_curtain", "bound_to": "taproom_curtain", "bead": BEAD,
                 "states": {s: {k: "aa_cab_time_crisis_cracked_%s_%s.png" % (s, k) for k in KINDS} for s in tc},
                 "curtain_hidden_shift_px": [hide_dx, 0],
                 "derivation": {"displaced_revealed": "the painted pose with its green neon (screen, glowing hose) pressed down "
                                                      "to unlit; emit black",
                                "night_glow": "the painted pose with its painted night neon and emit",
                                "curtain_hidden": "displaced_revealed moved %d px right (the cabinet body's right edge "
                                                  "reaches the curtain's right edge at the floor); straight sideways, no "
                                                  "scale. Usable only after the left Gemini fill (it uncovers the "
                                                  "area the cabinet stood on)" % hide_dx},
                 "clean_plate": status.get("left"), "sprites": sprites})
    specs["aa_cab_time_crisis_cracked"] = s_tc

    # N5 vapour
    sprites = {}
    vbox = {}
    vm_night = vap["night"][0] > 0
    vm_day = vap["day"][0] > 0
    off = pieces["tc"]["offset"]
    pieces["vapour"] = {"masks": {"night": vm_night, "day": vm_day}, "offset": off, "iou": None, "zones": [],
                        "alpha": "per plate (fog density)"}
    set_boxes(pieces["vapour"])
    # the vapour masks are cut per plate, so its offset comes from its own boxes, not the cabinet's (Eurobound-6fbg)
    _bd, _bn = pieces["vapour"]["boxes"]["day"], pieces["vapour"]["boxes"]["night"]
    pieces["vapour"]["offset"] = (int(_bn[0] - _bd[0]), int(_bn[1] - _bd[1]))
    vl = {}
    for k in ("day", "night"):
        al = vap[k][0]
        img = P[k]
        if left_fill_day is not None:
            # exact solve against the clean floor: alpha along (fog - clean), colour so layer over clean = plate
            C = clean[k]
            F = vap[k][1]
            d = F[None, None, :] - C
            al = np.clip(((img - C) * d).sum(-1) / np.maximum((d * d).sum(-1), 1e-4), 0, 1) * (vap[k][0] > 0)
            # gate C round 1: the solved night fog came out opaque in lumps (a pasted sticker); cap it so the floor
            # shows through, soften it, and take the box-side ramp (the solve alone ended in hard straight steps)
            al = np.minimum(ndi.gaussian_filter(al, 1.2), VAPOUR_MAX) * vap[k][2]
            rgb = np.clip(C + (img - C) / np.maximum(al, 0.05)[..., None], 0, 1)
        else:
            # one fog colour (the vapour's own, sampled from its densest pixels), shaded a little by the plate so
            # the wisps keep their painted light; no floor texture rides along
            F = vap[k][1]
            shade = np.clip(lum(img) / max(float(lum(F)), 1e-3), 0.7, 1.2)[..., None]
            rgb = np.clip(F[None, None, :] * shade, 0, 1)
        x0, y0, x1, y1 = frame_box(pieces["vapour"], k)
        vl[k] = np.dstack([rgb[y0:y1, x0:x1], al[y0:y1, x0:x1]])
    x0, y0, x1, y1 = frame_box(pieces["vapour"], "night")
    vl["emit"] = np.dstack([P["emit"][y0:y1, x0:x1], vap["night"][0][y0:y1, x0:x1]])
    layers["vapour"] = vl
    s_vap = write_piece("aa_transition_taproom_vapor", "vapour", {"active": vl}, None, {}, sprites)
    s_vap.update({"asset_id": "aa_transition_taproom_vapor", "node_id": "aa_node_taproom_curtain", "bead": BEAD,
                  "active_hours": "20:00_to_04:00 (env taproom_curtain_vapor); the scene shows it, this is the layer",
                  "low_motion_state": "still_vapor (this layer); the 8-frame loop in sm is not made",
                  "provisional": left_fill_day is None,
                  "derivation": ("provisional: alpha from a green-excess unmix against the floor around it, colour = "
                                 "the plate's own pixels; re-solved exactly against the clean floor once the left "
                                 "Gemini fill exists") if left_fill_day is None else
                                "solved against the clean floor (layer over clean = plate)",
                  "clean_plate": status.get("left"), "sprites": sprites})
    specs["aa_transition_taproom_vapor"] = s_vap

    for name, spec in specs.items():
        with open(os.path.join(OUT, name + ".json"), "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(with_boxes(spec), indent=1, ensure_ascii=False) + "\n")

    # ---- staged clean plates ----
    for k in KINDS:
        Image.fromarray(u8(clean[k]), "RGB").save(os.path.join(CLEAN, "%s_%s.png" % (BASE, k)))
    with open(os.path.join(CLEAN, "status.json"), "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps({"bead": BEAD, "staged": "not live; the live plates are unchanged",
                            "holes": status, "gemini": gem_info}, indent=1) + "\n")

    # ---- self-check ----
    for k in KINDS:
        untouched = ~ndi.binary_dilation(changed[k], iterations=1)
        same = np.array_equal(u8(clean[k])[untouched], u8(P[k])[untouched])
        assert same, "pixels changed outside the holes: " + k
    worst = {}
    for name, lay in layers.items():
        for k, rgba in lay.items():
            if name in ("vapour", "lamps_top", "lamps_side"):   # no lamp state is the painted one (one lamp is dark)
                continue
            x0, y0, x1, y1 = frame_box(pieces[name], k)
            al = rgba[..., 3:4]
            comp = clean[k][y0:y1, x0:x1] * (1 - al) + rgba[..., :3] * al
            core = ndi.binary_erosion(rgba[..., 3] >= 0.99, iterations=2)     # defringed outline excluded
            ref = (PD if name == "door_leaf" else P)[k]     # the leaf is cut from the despilled plate
            worst["%s/%s" % (name, k)] = round(float(np.abs(comp - ref[y0:y1, x0:x1])[core].max() * 255), 1)
    print("outside the holes every staged plate equals the live plate")
    print("layer over clean vs live plate, max diff inside the solid alpha (0-255):", worst)

    if a.review:
        review(a.review, P, clean, pieces, specs, gem_holes, fills)
    return 0


# ----------------------------------------------------------------------------------------------- review
def checker(w, h, s=8):
    t = (np.arange(h)[:, None] // s + np.arange(w)[None, :] // s) % 2
    return np.where(t[..., None], 0.78, 0.47).astype(np.float32) * np.ones(3, np.float32)


def zoom_for(w, h, target=1300):
    return max(1, min(4, int(round(target / max(w, h)))))


def review(out, P, clean, pieces, specs, gem_holes, fills):
    os.makedirs(out, exist_ok=True)
    H, W = P["day"].shape[:2]
    groups = {"N1_ddr": ["aa_cab_ddr_broken"], "N2_door": ["aa_transition_maintenance_door"],
              "N3_curtain": ["aa_transition_taproom_curtain"], "N4_time_crisis": ["aa_cab_time_crisis_cracked"],
              "N5_vapour": ["aa_transition_taproom_vapor"]}
    # 1. every file on a checkerboard, zoomed
    for g, names in groups.items():
        for n in names:
            for fn in sorted(specs[n]["sprites"]):
                im = f32(Image.open(os.path.join(OUT, fn)))
                h, w = im.shape[:2]
                z = zoom_for(w, h)
                bg = checker(w, h)
                comp = bg * (1 - im[..., 3:]) + im[..., :3] * im[..., 3:]
                Image.fromarray(u8(comp)).resize((w * z, h * z), Image.NEAREST).save(
                    os.path.join(out, "%s__%s_on_checker_x%d.png" % (g, fn[:-4], z)))
    # 2. clean plate behind and 3. every layer back over it, per item crop, day and night
    # until the left fill exists the staged plate still carries the painted vapour, so the provisional vapour layer
    # is left out of the composites (it would double)
    order = ["ddr", "door_leaf", "lamps_top", "lamps_side", "curtain", "plaque", "tc"] + \
        (["vapour"] if "left_day" in fills else [])
    item_pieces = {"N1_ddr": ["ddr"], "N2_door": ["door_leaf", "lamps_top", "lamps_side"],
                   "N3_curtain": ["curtain", "plaque"], "N4_time_crisis": ["tc"], "N5_vapour": ["vapour"]}
    default_file = {"ddr": "aa_cab_ddr_broken_error_%s.png", "door_leaf": "aa_transition_maintenance_door_closed_%s.png",
                    "lamps_top": "aa_transition_maintenance_door_lamps_top_locked_red_%s.png",
                    "lamps_side": "aa_transition_maintenance_door_lamps_side_locked_red_%s.png",
                    "curtain": "aa_transition_taproom_curtain_night_breathing_%s.png",
                    "plaque": "aa_transition_taproom_plaque_default_%s.png",
                    "tc": "aa_cab_time_crisis_cracked_night_glow_%s.png", "vapour": "aa_transition_taproom_vapor_active_%s.png"}

    def composite(k, files=None):
        comp = clean[k].copy()
        for pn in order:
            fn = (files or {}).get(pn, default_file[pn]) % k
            im = f32(Image.open(os.path.join(OUT, fn)))
            x0, y0 = frame_box(pieces[pn], k)[:2]
            h, w = im.shape[:2]
            reg = comp[y0:y0 + h, x0:x0 + w]
            al = im[:reg.shape[0], :reg.shape[1], 3:]
            comp[y0:y0 + h, x0:x0 + w] = reg * (1 - al) + im[:reg.shape[0], :reg.shape[1], :3] * al
        return comp

    comps = {k: composite(k) for k in ("day", "night")}
    for g, pns in item_pieces.items():
        for k in ("day", "night"):
            boxes = [frame_box(pieces[pn], k) for pn in pns]
            x0 = max(min(b[0] for b in boxes) - 60, 0); y0 = max(min(b[1] for b in boxes) - 60, 0)
            x1 = min(max(b[2] for b in boxes) + 60, W); y1 = min(max(b[3] for b in boxes) + 60, H)
            z = zoom_for(x1 - x0, y1 - y0, 1300)
            sz = ((x1 - x0) * z, (y1 - y0) * z)
            Image.fromarray(u8(clean[k][y0:y1, x0:x1])).resize(sz, Image.LANCZOS).save(
                os.path.join(out, "%s__clean_plate_%s_x%d.png" % (g, k, z)))
            Image.fromarray(u8(comps[k][y0:y1, x0:x1])).resize(sz, Image.LANCZOS).save(
                os.path.join(out, "%s__composite_%s_x%d.png" % (g, k, z)))
            Image.fromarray(u8(P[k][y0:y1, x0:x1])).resize(sz, Image.LANCZOS).save(
                os.path.join(out, "%s__live_plate_%s_x%d.png" % (g, k, z)))
    # door states side by side (night), both lamp states over the clean plate
    for k in ("day", "night"):
        tiles = []
        for top, side in (("locked_red", "locked_red"), ("unlocking_amber", "locked_red"),
                          ("unlocked_green", "unlocked_green")):
            c = composite(k, {"lamps_top": "aa_transition_maintenance_door_lamps_top_%s" % top + "_%s.png",
                              "lamps_side": "aa_transition_maintenance_door_lamps_side_%s" % side + "_%s.png"})
            tiles.append(c[640:1180, 2470:2720])
        tiles.append(clean[k][640:1180, 2470:2720])
        sheet = np.concatenate([np.pad(t, ((0, 0), (0, 12), (0, 0)), constant_values=1) for t in tiles], 1)
        Image.fromarray(u8(sheet)).resize((sheet.shape[1] * 2, sheet.shape[0] * 2), Image.LANCZOS).save(
            os.path.join(out, "N2_door__states_locked_amber_unlocked_clean_%s_x2.png" % k))
    # whole plate at about game size, plus a hole map
    for k in ("day", "night"):
        Image.fromarray(u8(comps[k])).resize((1920, 1072), Image.LANCZOS).save(
            os.path.join(out, "whole_plate_composite_%s_1920.png" % k))
        Image.fromarray(u8(clean[k])).resize((1920, 1072), Image.LANCZOS).save(
            os.path.join(out, "whole_clean_plate_staged_%s_1920.png" % k))
        hm = clean[k] * 0.5
        for name, hole in gem_holes.items():
            if name.endswith(k) and name not in fills:
                hm[hole] = hm[hole] * 0.4 + np.array([1, 0, 0]) * 0.6
        Image.fromarray(u8(hm)).resize((1376, 768), Image.LANCZOS).save(
            os.path.join(out, "whole_plate_pending_gemini_holes_red_%s.png" % k))


if __name__ == "__main__":
    sys.exit(main())
