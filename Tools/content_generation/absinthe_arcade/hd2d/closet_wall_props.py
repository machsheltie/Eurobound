"""Build the Arcade closet's five approved wall pieces into game sprites (bead Eurobound-ms3r).

Author, Desk asset-team-arcade-closet-reference-set (2026-11-16): "Approve all five: build them".
The five: Q8 blacklight switch + tube, C4 sparking wiring, C8 Tekken haiku, C9 joystick with lips,
C11 Broken Prize Tag. Sources are the approved reference PNGs in dev/asset_team/arcade_refs/closet/.

How it works
- Each piece is placed in room tiles on a wall of the closet's paint geometry (constants copied
  from game/worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.gd) and warped through
  the paint camera onto the 2752x1536 night plate, so it sits in the plate's perspective.
- The paint shader keeps alpha binary (alpha < 0.5 is discarded), so every sprite is a COMPOSITE:
  the plate pixels with the piece blended in, cut out with a few pixels of margin. Soft edges are
  baked against the plate and the cut lands on unchanged plate pixels, so there is no seam.
- The blacklight (Desk bcnr-q8: a wall switch, examine toggles it) is a whole-plate variant,
  aa_int_closet_night_uv.png: a UV Purple #9400D3 wash on the back and left walls with a lavender
  #C77DFF bloom under the tube. Pieces in the wash have a `_uv` state composited on that plate.
- Hidden states (haiku with the light off, tag once collected) are fully transparent sprites.

Writes into game/assets/worlds/debaucheryville/absinthe_arcade/interior/closet/ (the UV plate) and
its props/ folder (sprites, *_emit masks, entries merged into aa_closet_props.json). Run from the
repo root:  python -I <this file>;  add  --sheet <out.jpg>  to only draw the gate-C review sheet.
"""
import json
import math
import os
import sys

import cv2
import numpy as np
from PIL import Image

ROOT = os.getcwd()
REF = os.path.join(ROOT, "dev/asset_team/arcade_refs/closet")
GA = os.path.join(ROOT, "game/assets/worlds/debaucheryville/absinthe_arcade/interior/closet")
PROPS = os.path.join(GA, "props")
REVIEW = os.path.join(ROOT, "dev/asset_team/reviews")

# Paint camera and room walls (absinthe_arcade_maintenance_closet_hd2d.gd).
W, H = 2752, 1536
FOCAL = 2108.0
PITCH = math.radians(19.52)
CAM = np.array([0.0, 8.43, 24.83])
LEFT_WALL = ((-2.56, 0.0), (-5.94, 13.76))
RIGHT_WALL = ((4.28, 0.0), (6.12, 13.76))

UV = np.array([0x94, 0x00, 0xD3], float) / 255.0
LAVENDER = np.array([0xC7, 0x7D, 0xFF], float) / 255.0
MARGIN_PX = 3


def wall_x(line, z):
    (ax, az), (bx, bz) = line
    return ax + (bx - ax) * (z - az) / (bz - az)


def project(p):
    v = np.asarray(p, float) - CAM
    yc = v[1] * math.cos(PITCH) - v[2] * math.sin(PITCH)
    zc = v[1] * math.sin(PITCH) + v[2] * math.cos(PITCH)
    return np.array([W / 2 + FOCAL * v[0] / -zc, H / 2 - FOCAL * yc / -zc])


def quad_world(wall, u0, u1, y0, y1, z=0.0):
    """Corners TL, TR, BR, BL of a rectangle on a wall, in world tiles.
    wall 'left'/'right': u runs along z (u0 = image-left end); 'back'/'plane': u is x at depth z."""
    def pt(u, y):
        if wall == "left":
            return (wall_x(LEFT_WALL, u), y, u)
        if wall == "right":
            return (wall_x(RIGHT_WALL, u), y, u)
        return (u, y, z)
    return [pt(u0, y1), pt(u1, y1), pt(u1, y0), pt(u0, y0)]


def quad_from_px(x0, y0, x1, y1, z):
    """Corners (TL, TR, BR, BL) on the camera-facing plane at depth z that land on a plate box."""
    c, s_ = math.cos(PITCH), math.sin(PITCH)
    out = []
    for px, py in ((x0, y0), (x1, y0), (x1, y1), (x0, y1)):
        dc = np.array([(px - W / 2) / FOCAL, -(py - H / 2) / FOCAL, -1.0])
        d = np.array([dc[0], dc[1] * c + dc[2] * s_, -dc[1] * s_ + dc[2] * c])
        t = (z - CAM[2]) / d[2]
        out.append(tuple(CAM + t * d))
    return out


def load_rgba(name, size=None, mirror=False):
    im = Image.open(os.path.join(REF, name)).convert("RGBA")
    if size is not None and im.size != size:
        im = im.resize(size, Image.LANCZOS)
    if mirror:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    return np.asarray(im).astype(np.float32) / 255.0


def lever_contrast(src):
    """Gate-C fixes 1-2 (the toggle did not read at wall size): a deterministic levels stretch of the
    reference's own toggle slot, so the lever's pale cap (down when off, up when on) stands clear of
    the dark slot and the rust round it after the downscale. No repainting: the same pixels, with
    the slot's darkest quarter pushed to black and its brightest pixels to the plate's ivory."""
    out = src.copy()
    h, w = src.shape[:2]
    y0, y1, x0, x1 = int(h * 0.36), int(h * 0.66), int(w * 0.40), int(w * 0.60)
    reg = out[y0:y1, x0:x1, :3]
    lum = reg @ np.array([0.299, 0.587, 0.114], np.float32)
    lo, hi = np.percentile(lum, 30), np.percentile(lum, 88)
    k = np.clip((lum - lo) / max(hi - lo, 1e-3), 0, 1)[..., None]
    ivory = np.array([0xE8, 0xE0, 0xC8], np.float32) / 255.0
    out[y0:y1, x0:x1, :3] = np.clip(reg * 0.25 * k + ivory * k ** 1.5 * 0.85, 0, 1)
    return out


def warp(src, corners_world):
    """Warps an RGBA float image onto the plate; returns a plate-sized RGBA float canvas."""
    h, w = src.shape[:2]
    dst = np.float32([project(c) for c in corners_world])
    m = cv2.getPerspectiveTransform(np.float32([[0, 0], [w, 0], [w, h], [0, h]]), dst)
    prem = src.copy()
    prem[..., :3] *= prem[..., 3:4]
    out = cv2.warpPerspective(prem, m, (W, H), flags=cv2.INTER_AREA if w > 400 else cv2.INTER_LINEAR,
                              borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
    a = out[..., 3:4]
    out[..., :3] = np.where(a > 1e-4, out[..., :3] / np.maximum(a, 1e-4), 0)
    return out


def ambient(plate, sigma=60):
    return cv2.GaussianBlur(plate, (0, 0), sigma)


def light_like_plate(layer, amb, strength=1.0):
    """Relights a neutrally lit reference with the plate's local light (keeps its own colours)."""
    out = layer.copy()
    k = 0.22 + 1.45 * amb
    out[..., :3] = np.clip(layer[..., :3] * ((1 - strength) + strength * k), 0, 1)
    return out


def over(base, layer):
    a = layer[..., 3:4]
    return base * (1 - a) + layer[..., :3] * a


def surface_map():
    """Per plate pixel: which room surface the paint camera sees there, and the world z of it."""
    ys, xs = np.mgrid[0:H, 0:W].astype(np.float64)
    d_cam = np.stack([(xs - W / 2) / FOCAL, -(ys - H / 2) / FOCAL, -np.ones_like(xs)], -1)
    c, s = math.cos(PITCH), math.sin(PITCH)
    # camera rotated by -PITCH about x: world = R(-pitch) * cam
    d = np.empty_like(d_cam)
    d[..., 0] = d_cam[..., 0]
    d[..., 1] = d_cam[..., 1] * c + d_cam[..., 2] * s
    d[..., 2] = -d_cam[..., 1] * s + d_cam[..., 2] * c
    best_t = np.full((H, W), np.inf)
    label = np.zeros((H, W), np.int8)  # 0 none, 1 back, 2 left, 3 right, 4 floor
    hit_z = np.zeros((H, W))
    # back wall z = 0
    t = (0 - CAM[2]) / d[..., 2]
    x = CAM[0] + t * d[..., 0]
    ok = (t > 0) & (x > wall_x(LEFT_WALL, 0) - 4) & (x < wall_x(RIGHT_WALL, 0) + 4)
    upd = ok & (t < best_t)
    best_t[upd], label[upd], hit_z[upd] = t[upd], 1, 0
    # floor y = 0
    t = (0 - CAM[1]) / d[..., 1]
    upd = (t > 0) & (t < best_t)
    best_t[upd], label[upd] = t[upd], 4
    hit_z[upd] = (CAM[2] + t * d[..., 2])[upd]
    for lab, line in ((2, LEFT_WALL), (3, RIGHT_WALL)):
        (ax, az), (bx, bz) = line
        n = np.array([bz - az, 0.0, -(bx - ax)])
        n /= np.linalg.norm(n)
        p0 = np.array([ax, 0.0, az])
        denom = d @ n
        t = ((p0 - CAM) @ n) / np.where(np.abs(denom) < 1e-9, 1e-9, denom)
        upd = (t > 0) & (t < best_t)
        best_t[upd], label[upd] = t[upd], lab
        hit_z[upd] = (CAM[2] + t * d[..., 2])[upd]
    return label, hit_z


def uv_plate(night, emit, tube_box):
    """The blacklight-on plate: UV wash on the back and left walls, lavender bloom under the tube."""
    label, hz = surface_map()
    m = np.zeros((H, W), np.float32)
    m[label == 1] = 1.0
    left = label == 2
    m[left] = np.clip(1.0 - hz[left] / 20.0, 0.35, 1.0)
    floor = label == 4
    m[floor] = np.clip(0.45 - hz[floor] / 30.0, 0.0, 0.45)
    m[label == 3] = 0.0
    m = cv2.GaussianBlur(m, (0, 0), 30)
    # The fluorescent marquee "stays on and flickering either way" (brief), and the screens, DDR
    # lights and existing inks keep their own colour: the room's emit map protects them.
    glow = cv2.GaussianBlur(np.clip(emit.max(axis=2) * 2.5, 0, 1), (0, 0), 4)
    m = m * (1 - glow)
    lum = (night @ np.array([0.299, 0.587, 0.114], np.float32))[..., None]
    washed = night * 0.45 + (0.10 + 1.25 * lum) * UV[None, None, :]
    out = night * (1 - m[..., None]) + washed * m[..., None]
    # bloom: soft lavender light pooling under and around the tube
    x0, y0, x1, y1 = tube_box
    bloom = np.zeros((H, W), np.float32)
    cv2.ellipse(bloom, (int((x0 + x1) / 2), int(y1 + 40)), (int((x1 - x0) * 0.62), 150), 0, 0, 360, 1.0, -1)
    bloom = cv2.GaussianBlur(bloom, (0, 0), 70) * 0.45
    out = out + bloom[..., None] * LAVENDER[None, None, :] * (0.4 + lum)
    return np.clip(out, 0, 1), m


def cutout(layers_alpha):
    a = np.zeros((H, W), np.float32)
    for al in layers_alpha:
        a = np.maximum(a, al)
    mask = (a > 0.02).astype(np.uint8)
    mask = cv2.dilate(mask, np.ones((2 * MARGIN_PX + 1, 2 * MARGIN_PX + 1), np.uint8))
    ys, xs = np.nonzero(mask)
    box = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
    return mask, box


def save_rgba(path, rgb, mask, box):
    x0, y0, x1, y1 = box
    out = np.zeros((y1 - y0, x1 - x0, 4), np.uint8)
    if rgb is not None:
        out[..., :3] = np.clip(rgb[y0:y1, x0:x1] * 255 + 0.5, 0, 255).astype(np.uint8)
        out[..., 3] = mask[y0:y1, x0:x1] * 255
    Image.fromarray(out, "RGBA").save(path, optimize=True)


def save_emit(path, emit_rgb, mask, box):
    x0, y0, x1, y1 = box
    out = np.zeros((y1 - y0, x1 - x0, 4), np.uint8)
    out[..., :3] = np.clip(emit_rgb[y0:y1, x0:x1] * 255 + 0.5, 0, 255).astype(np.uint8)
    out[..., 3] = mask[y0:y1, x0:x1] * 255
    Image.fromarray(out, "RGBA").save(path, optimize=True)


def main():
    night = np.asarray(Image.open(os.path.join(GA, "aa_int_closet_night.png")).convert("RGB")).astype(np.float32) / 255.0
    amb = ambient(night)
    emit = np.asarray(Image.open(os.path.join(GA, "aa_int_closet_emit.png")).convert("RGB")).astype(np.float32) / 255.0

    # ---- placements, in room tiles (see the bead notes for why each sits where it does) ----
    # The bros walk only z <= 7.6, and the painted graffiti fills the left wall from the back corner
    # to the door, so the switch, joystick and haiku share the free wall just in front of the door
    # (door base z 4.86-7.12), as in the approved mock-ups: switch high by the frame, joystick low
    # beside it, haiku further along.
    # Q8 switch: the brief's 0.35 x 0.55 tiles.
    sw_corners = quad_world("left", 7.82, 7.47, 4.3, 4.85)
    # Q8 tube: back wall, high, above the toilet and the left-wall graffiti (approved mock-up spot).
    tube_corners = quad_world("back", -1.45, 3.05, 5.05, 5.68, z=0.0)
    # C4 wiring: free right wall in front of the cheat codes (painted to z ~6.5); mirrored so the
    # junction box sits at the back end, z ~7.6, where the bros can walk close enough to be zapped,
    # and the cable runs end at the front pipe.
    wire_corners = quad_world("right", 7.0, 13.0, 2.4, 4.0)
    # C8 haiku (brief 3 x 1.2 tiles; 4 x 1.6 on this steeply foreshortened wall).
    # Ends short of the front pipe (gate-C round 1 note).
    haiku_corners = quad_world("left", 12.5, 9.9, 3.35, 4.75)
    # C9 joystick (brief ~1.2 tiles square; 1.4 x 1.5 here, same reason), low, between switch and haiku.
    joy_corners = quad_world("left", 9.7, 8.3, 1.1, 2.6)
    # C11 tag: hangs from the claw arm's tips over the toilet (plate px), on a plane at z = 1.0.
    # Brief: 0.5 x 0.7 tiles plus the twist-tie loop (gate-C round 1: was ~2x).
    tag_corners = quad_from_px(1381, 452, 1421, 526, 1.0)
    tube_px = np.array([project(c) for c in tube_corners])
    tube_box = (tube_px[:, 0].min(), tube_px[:, 1].min(), tube_px[:, 0].max(), tube_px[:, 1].max())
    uv, wash = uv_plate(night, emit, tube_box)
    uv_amb = ambient(uv)

    sprites = {}
    os.makedirs(PROPS, exist_ok=True)

    def emit_entry(name, box):
        x0, y0, x1, y1 = box
        sprites[name] = {"x": x0, "y": y0, "w": x1 - x0, "h": y1 - y0}

    def write(prefix, states, emits=None):
        """states: {state: (rgb plate or None, layer alpha list)}; one shared footprint."""
        mask, box = cutout([al for _, als in states.values() for al in als])
        for st, (rgb, _) in states.items():
            name = f"{prefix}_{st}.png"
            save_rgba(os.path.join(PROPS, name), rgb, mask, box)
            emit_entry(name, box)
        for st, e in (emits or {}).items():
            name = f"{prefix}_{st}_emit.png"
            save_emit(os.path.join(PROPS, name), e, mask, box)
            emit_entry(name, box)
        return box

    # Q8 switch (off on the night plate, on on the UV plate).
    sw_off = light_like_plate(warp(lever_contrast(load_rgba("q8_switch_off.png")), sw_corners), amb, 0.45)
    sw_on = light_like_plate(warp(lever_contrast(load_rgba("q8_switch_on.png")), sw_corners), uv_amb, 0.45)
    # Brief, reads_at_icon_size: "(2) the violet glow state when on": the ivory plastic fluoresces
    # under its own blacklight, so the on state carries a UV Purple emission over the plate.
    plastic = np.clip(sw_on[..., :3].mean(-1, keepdims=True) - 0.25, 0, 1) * sw_on[..., 3:4]
    write("aa_closet_bl_switch", {"off": (over(night, sw_off), [sw_off[..., 3]]),
                                  "on": (over(uv, sw_on), [sw_on[..., 3]])},
          {"on": plastic * (0.55 * UV + 0.25 * LAVENDER)[None, None, :]})

    # Q8 tube (on glows: its glass is emissive).
    t_off_src = load_rgba("q8_tube_off.png")
    t_on_src = load_rgba("q8_tube_on.png", (t_off_src.shape[1], t_off_src.shape[0]))
    t_off = light_like_plate(warp(t_off_src, tube_corners), amb)
    t_on_raw = warp(t_on_src, tube_corners)
    t_on = light_like_plate(t_on_raw, uv_amb)
    glass = np.clip((t_on_raw[..., :3] @ np.array([0.3, 0.2, 0.5], np.float32)) - 0.35, 0, 1)[..., None] * 1.8
    t_on[..., :3] = np.clip(t_on[..., :3] * (1 - np.clip(glass, 0, 1)) + t_on_raw[..., :3] * np.clip(glass, 0, 1), 0, 1)
    tube_emit = t_on_raw[..., :3] * np.clip(glass, 0, 1) * t_on_raw[..., 3:4] * 0.8
    write("aa_closet_bl_tube", {"off": (over(night, t_off), [t_off[..., 3]]),
                                "on": (over(uv, t_on), [t_on[..., 3]])},
          {"on": tube_emit})

    # C4 wiring (right wall: outside the wash, so no _uv state).
    w_idle = light_like_plate(warp(load_rgba("c4_wiring_idle.png", mirror=True), wire_corners), amb)
    w_spark_raw = warp(load_rgba("c4_wiring_spark.png", mirror=True), wire_corners)
    w_spark = light_like_plate(w_spark_raw, amb)
    spark = np.clip((w_spark_raw[..., 0] + w_spark_raw[..., 1]) / 2 - w_spark_raw[..., 2] * 0.6 - 0.45, 0, 1) * 2.2
    spark = np.clip(spark, 0, 1)[..., None] * w_spark_raw[..., 3:4]
    w_spark[..., :3] = w_spark[..., :3] * (1 - spark) + w_spark_raw[..., :3] * spark
    write("aa_closet_wiring", {"idle": (over(night, w_idle), [w_idle[..., 3]]),
                               "spark": (over(night, w_spark), [w_spark[..., 3]])},
          {"spark": w_spark_raw[..., :3] * spark})

    # C8 haiku: highlighter ink, shows only with the blacklight on; the ink fluoresces.
    hk = warp(load_rgba("c8_haiku_decal.png"), haiku_corners)
    hk_rgb = over(uv, hk)
    write("aa_closet_haiku", {"on": (hk_rgb, [hk[..., 3]]), "off": (None, [hk[..., 3]])},
          {"on": hk[..., :3] * hk[..., 3:4] * 0.12})

    # C9 joystick: faint smears; glowing while a bro is Embarrassed; each with and without the UV wash.
    jf = warp(load_rgba("c9_joystick_faint.png"), joy_corners)
    jg = warp(load_rgba("c9_joystick_glowing.png"), joy_corners)
    # the glowing render carries painted wall behind the halo; key the halo to the plate's wall
    write("aa_closet_joystick", {
        "faint": (over(night, jf), [jf[..., 3], jg[..., 3]]),
        "glowing": (over(night, jg), [jg[..., 3]]),
        # Under the wash the smears sank into the purple (gate-C round 1): the same smears, denser.
        "faint_uv": (over(uv, np.concatenate([jf[..., :3], np.clip(jf[..., 3:4] * 1.8, 0, 1)], -1)), [jf[..., 3]]),
        "glowing_uv": (over(uv, jg), [jg[..., 3]]),
    }, {"glowing": jg[..., :3] * jg[..., 3:4] * 0.5, "glowing_uv": jg[..., :3] * jg[..., 3:4] * 0.6})

    # C11 Broken Prize Tag on the claw arm; gone once collected.
    tg = light_like_plate(warp(load_rgba("c11_tag_world_prop.png"), tag_corners), amb, 0.85)
    tg_uv = light_like_plate(warp(load_rgba("c11_tag_world_prop.png"), tag_corners), uv_amb, 0.85)
    write("aa_closet_prize_tag", {"hanging": (over(night, tg), [tg[..., 3]]),
                                  "hanging_uv": (over(uv, tg_uv), [tg_uv[..., 3]]),
                                  "collected": (None, [tg[..., 3]])})

    Image.fromarray((uv * 255 + 0.5).astype(np.uint8)).save(os.path.join(GA, "aa_int_closet_night_uv.png"), optimize=True)

    # merge into the props JSON (replace only this script's entries)
    jpath = os.path.join(PROPS, "aa_closet_props.json")
    data = json.load(open(jpath, encoding="utf-8"))
    mine = ("aa_closet_bl_", "aa_closet_wiring", "aa_closet_haiku", "aa_closet_joystick", "aa_closet_prize_tag")
    data["sprites"] = {k: v for k, v in data["sprites"].items() if not k.startswith(mine)}
    data["sprites"].update(sprites)
    data["note_closet_build"] = ("Eurobound-ms3r: bl_switch/bl_tube/wiring/haiku/joystick/prize_tag are composites "
                                 "(plate + piece) built by Tools/content_generation/absinthe_arcade/hd2d/"
                                 "closet_wall_props.py; *_uv states sit on aa_int_closet_night_uv.png (blacklight on).")
    with open(jpath, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, indent=1)
        fh.write("\n")
    print("wrote", len(sprites), "sprites")
    return 0


def composite(plate_name, names, sprites):
    """The plate with prop sprites drawn as the game draws them (alpha >= 0.5, emit x 1.4 on top)."""
    im = np.asarray(Image.open(os.path.join(GA, plate_name)).convert("RGB")).astype(np.float32) / 255.0
    for n in names:
        b = sprites[n]
        sp = np.asarray(Image.open(os.path.join(PROPS, n)).convert("RGBA")).astype(np.float32) / 255.0
        col = sp[..., :3].copy()
        e = n.replace(".png", "_emit.png")
        if e in sprites:
            col += np.asarray(Image.open(os.path.join(PROPS, e)).convert("RGB")).astype(np.float32) / 255.0 * 1.4
        reg = im[b["y"]:b["y"] + b["h"], b["x"]:b["x"] + b["w"]]
        reg[:] = np.where(sp[..., 3:4] >= 0.5, col, reg)
    return Image.fromarray((np.clip(im, 0, 1) * 255 + 0.5).astype(np.uint8))


def review_sheet(out_path):
    """Blacklight off and on, full view and close-ups, for the blind gate-C reviewer."""
    from PIL import ImageDraw
    sprites = json.load(open(os.path.join(PROPS, "aa_closet_props.json"), encoding="utf-8"))["sprites"]
    off = ["aa_closet_bl_switch_off.png", "aa_closet_bl_tube_off.png", "aa_closet_wiring_idle.png",
           "aa_closet_haiku_off.png", "aa_closet_joystick_faint.png", "aa_closet_prize_tag_hanging.png"]
    on = ["aa_closet_bl_switch_on.png", "aa_closet_bl_tube_on.png", "aa_closet_wiring_spark.png",
          "aa_closet_haiku_on.png", "aa_closet_joystick_glowing_uv.png", "aa_closet_prize_tag_hanging_uv.png"]
    shots = [
        ("Blacklight OFF (default): switch down, tube dark, haiku hidden, joystick faint, wiring idle",
         composite("aa_int_closet_night.png", off, sprites), None),
        ("Blacklight ON + a bro Embarrassed + spark frame",
         composite("aa_int_closet_night_uv.png", on, sprites), None),
        ("Close-up OFF: switch by the door, faint joystick smears", composite("aa_int_closet_night.png", off, sprites), (400, 420, 1100, 1010)),
        ("Close-up ON: switch up, haiku, joystick glowing", composite("aa_int_closet_night_uv.png", on, sprites), (400, 420, 1100, 1010)),
        ("Close-up: joystick glowing, blacklight OFF", composite("aa_int_closet_night.png", ["aa_closet_joystick_glowing.png"], sprites), (400, 420, 1100, 1010)),
        ("Close-up OFF: tube dark, Broken Prize Tag on the claw", composite("aa_int_closet_night.png", off, sprites), (1150, 280, 1650, 640)),
        ("Close-up ON: tube lit", composite("aa_int_closet_night_uv.png", on, sprites), (1150, 280, 1650, 640)),
        ("Close-up: wiring idle", composite("aa_int_closet_night.png", off, sprites), (1750, 380, 2350, 940)),
        ("Close-up: wiring spark", composite("aa_int_closet_night.png", ["aa_closet_wiring_spark.png"], sprites), (1750, 380, 2350, 940)),
    ]
    tiles = []
    for title, im, crop in shots:
        if crop:
            im = im.crop(crop)
            im = im.resize((int(im.width * 520 / im.height), 520), Image.LANCZOS)
        else:
            im = im.resize((1376, 768), Image.LANCZOS)
        canvas = Image.new("RGB", (im.width, im.height + 34), (24, 22, 28))
        canvas.paste(im, (0, 34))
        ImageDraw.Draw(canvas).text((8, 8), title, fill=(255, 220, 140))
        tiles.append(canvas)
    width = 1376 * 2 + 30
    rows, row, x = [], [], 0
    for t in tiles:
        if x + t.width > width and row:
            rows.append(row)
            row, x = [], 0
        row.append(t)
        x += t.width + 10
    rows.append(row)
    height = sum(max(t.height for t in r) + 10 for r in rows) + 10
    sheet = Image.new("RGB", (width, height), (16, 15, 20))
    y = 10
    for r in rows:
        x = 10
        for t in r:
            sheet.paste(t, (x, y))
            x += t.width + 10
        y += max(t.height for t in r) + 10
    sheet.save(out_path, quality=88)
    print("sheet", out_path)


if __name__ == "__main__":
    if "--sheet" in sys.argv:
        review_sheet(sys.argv[sys.argv.index("--sheet") + 1])
        sys.exit(0)
    sys.exit(main())
