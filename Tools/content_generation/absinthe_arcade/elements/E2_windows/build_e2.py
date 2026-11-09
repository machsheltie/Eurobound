"""E2 window set: builds every window kit at the origin into wip/E2_windows.blend.

Run (headless, re-runnable from scratch):
  blender -b --factory-startup --python build_e2.py

Kits (collection aa_kit/<asset_id>, sill pivot = bottom centre of the opening on the facade plane):
  aa_window_l1_arched   ground-floor arched window above the awning (bible crop 02, bottom)
  aa_window_l2_cat      first-floor left, the cat window (lower sash posed OPEN)
  aa_window_l3_balcony  second-floor left, belly-railed balcony with the magenta vine
  aa_window_r1          first-floor right, two pots + glass-dome filament lamp
  aa_window_r2          second-floor right (bible shows only its sill; rest per R1 + asset sheet)
  aa_window_dormer      mansard dormer (asset sheet), instanced twice by mason

Opening sizes: defaults below are bible-derived (doorway = 4.4 m yardstick); any entry found in
dev/aa_team/interfaces.json overrides them (see read_interfaces()).
"""
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Matrix, Vector

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import importlib  # noqa: E402

import e2_lib  # noqa: E402
import e2_parts  # noqa: E402
import e2_flora  # noqa: E402
importlib.reload(e2_lib)
importlib.reload(e2_parts)
importlib.reload(e2_flora)
from e2_lib import MB, get_coll, make_materials, set_color_attr, to_object  # noqa: E402
from e2_flora import bush, cascade, pot2, wall_cascade  # noqa: E402
from e2_parts import (FLASH_T, architrave_profile, medallion, railing_lattice, railing_web, arch_surround, arched_window, console, cord_curtain, crown_cornice,  # noqa: E402
                      dome_lamp, fascia, gathered_curtains, pot, railing, sash_window, shell_fan, shrub,
                      side_returns, sill_slab, surround_rect, vine, chamfer_block, leaf_geo)

REPO = HERE.parents[4]
AA = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade"
MAIN_BLEND = AA / "blender/aa_exterior.blend"
WIP = AA / "blender/wip/E2_windows.blend"
TEX = AA / "textures"
INTERFACES = REPO / "dev/aa_team/interfaces.json"

# --------------------------------------------------------------------------------------
# Parameters (metres). Bible-derived; see measurement notes in the report.
# --------------------------------------------------------------------------------------
SASH = dict(reveal=0.10, frame_w=0.045, frame_d=0.12, stile=0.04, bottom_rail=0.065, upper_frac=0.36,
            upper_mullions=1, lower_mullions=0)

PARAMS = {
    "aa_window_l1_arched": dict(W=0.79, H=1.35, sash=dict(SASH, frame_w=0.05, stile=0.045, bottom_rail=0.06,
                                                           lower_mullions=1, bar=0.05, rise_frac=0.85),
                                surround=dict(band=0.11, ring=0.09, mold=0.045, voussoirs=17, jamb_blocks=4,
                                              rise_frac=0.85),
                                fit=dict(frame_w=1.06, reveal=0.08),
                                hood=dict(top=2.16, w=1.42, proj=0.22, t=0.10, fascia=0.07, console_x=0.6),
                                sill=dict(w=1.24, proj=0.32, t=0.12, fascia=0.08, console_x=0.55)),
    "aa_window_l2_cat": dict(W=0.66, H=1.46, sash=dict(SASH), pose_open=1.0,
                             surround=dict(band=0.09, mold=0.10, pb=0.025, pm=0.06),
                             crown=dict(proj=0.10, h=0.10), crest=dict(w=0.76, h=0.47),
                             sill=dict(w=1.20, proj=0.22, t=0.08, fascia=0.10),
                             apron=dict(console_x=0.47, cw=0.13, D=0.17, Hc=0.40, crest_w=0.69, crest_h=0.42,
                                        depth=0.80)),
    "aa_window_l3_balcony": dict(W=0.66, H=1.24, sash=dict(SASH, lower_mullions=1),
                                 surround=dict(band=0.09, mold=0.10, pb=0.025, pm=0.06),
                                 crown=dict(proj=0.10, h=0.10), crest=dict(w=0.70, h=0.42),
                                 slab=dict(w=0.98, proj=0.15, t=0.075, fascia=0.06, console_x=0.42, cw=0.10,
                                           D=0.13, Hc=0.22),
                                 rail=dict(half=0.43, h=0.33, y=-0.125, bulge=0.06, style="x")),
    "aa_window_r1": dict(W=0.66, H=1.46, sash=dict(SASH),
                         surround=dict(band=0.09, mold=0.10, pb=0.025, pm=0.06),
                         crown=dict(proj=0.10, h=0.10), crest=dict(w=0.70, h=0.44),
                         sill=dict(w=1.15, proj=0.20, t=0.09, fascia=0.10),
                         apron=dict(console_x=0.47, cw=0.15, D=0.16, Hc=0.24)),
    "aa_window_r2": dict(W=0.66, H=1.24, sash=dict(SASH, lower_mullions=1),
                         surround=dict(band=0.09, mold=0.10, pb=0.025, pm=0.06),
                         crown=dict(proj=0.10, h=0.10), crest=dict(w=0.70, h=0.42),
                         slab=dict(w=0.98, proj=0.17, t=0.08, fascia=0.06, console_x=0.42, cw=0.10,
                                   D=0.14, Hc=0.22),
                         rail=dict(half=0.43, h=0.30, y=-0.14, bulge=0.0, style="x")),
    # side elevation (asset sheet crop 14): plain 2+2 sash, moulded surround + crown, corbelled sill,
    # pots of red flowers; ground floor under E6's awning (mount only)
    "aa_window_side_w0": dict(W=0.66, H=0.76, sash=dict(SASH, upper_frac=0.5, lower_mullions=1),
                              surround=dict(band=0.08, mold=0.08, pb=0.02, pm=0.05), crown=dict(proj=0.07, h=0.07),
                              sill=dict(w=0.98, proj=0.16, t=0.07, fascia=0.06),
                              apron=dict(console_x=0.40, cw=0.10, D=0.12, Hc=0.16), side=True),
    "aa_window_side_w1": dict(W=0.66, H=1.72, sash=dict(SASH, upper_frac=0.5, lower_mullions=1),
                              surround=dict(band=0.08, mold=0.08, pb=0.02, pm=0.05), crown=dict(proj=0.08, h=0.08),
                              sill=dict(w=1.0, proj=0.18, t=0.08, fascia=0.08),
                              apron=dict(console_x=0.41, cw=0.11, D=0.14, Hc=0.2), side=True),
    "aa_window_side_w2": dict(W=0.66, H=1.72, sash=dict(SASH, upper_frac=0.5, lower_mullions=1),
                              surround=dict(band=0.08, mold=0.08, pb=0.02, pm=0.05), crown=dict(proj=0.08, h=0.08),
                              sill=dict(w=1.0, proj=0.18, t=0.08, fascia=0.08),
                              apron=dict(console_x=0.41, cw=0.11, D=0.14, Hc=0.2), side=True),
    "aa_window_dormer_side": dict(W=0.56, H=0.78, sash=dict(SASH, reveal=0.06, frame_w=0.04, frame_d=0.10,
                                                              upper_frac=0.5, lower_mullions=1, stile=0.035),
                                  depth=1.1, vine_side=-1, band=0.05, body_w=1.06, ridge=1.5),
    "aa_window_dormer_l": dict(W=0.56, H=0.78, sash=dict(SASH, reveal=0.06, frame_w=0.04, frame_d=0.10,
                                                           upper_frac=0.5, lower_mullions=1, stile=0.035),
                               depth=1.1, vine_side=1, band=0.05, body_w=1.06, ridge=1.5),
    "aa_window_dormer_r": dict(W=0.56, H=0.78, sash=dict(SASH, reveal=0.06, frame_w=0.04, frame_d=0.10,
                                                           upper_frac=0.5, lower_mullions=1, stile=0.035),
                               depth=1.1, vine_side=-1, band=0.05, body_w=1.06, ridge=1.5),
}

# interfaces.json (mason, E1) key for each kit
IFACE_KEYS = {
    "aa_window_l1_arched": "left_w1_arched",
    "aa_window_l2_cat": "left_w2_cat",
    "aa_window_l3_balcony": "left_w3_balcony",
    "aa_window_r1": "right_w1",
    "aa_window_r2": "right_w2",
    "aa_window_dormer_l": ["dormer_left", "left_dormer", "dormer_l"],
    "aa_window_dormer_r": ["dormer_right", "right_dormer", "dormer_r"],
    "aa_window_dormer_side": ["dormer_side_right"],
    "aa_window_side_w0": "side_w0_ground",
    "aa_window_side_w1": "side_w1",
    "aa_window_side_w2": "side_w2",
}
IFACE = {}


def read_interfaces():
    """Fit each kit to mason's opening.

    PARAMS hold the bible-derived design (W = timber frame width). For an interface entry we take
    the frame width (frame_bible, else opening minus the default lining), derive the kit scale
    k = frame_w / W, and set the design H, lining band and reveal so that after scaling by k the
    frame, the hole (opening) and the reveal depth land exactly on mason's numbers.
    """
    used = {}
    if not INTERFACES.exists():
        return used
    data = json.loads(INTERFACES.read_text(encoding="utf-8"))
    IFACE.update(data)
    wins = dict(data.get("windows", {}))
    side = (data.get("side_right") or {}).get("windows", {})
    for k_, e_ in side.items():   # side windows in face coords (u along the side face)
        fr = e_.get("frame", {})
        wins[k_] = dict(e_, center_x=e_["u_center"], x_left=e_["u_left"], x_right=e_["u_right"],
                        frame_at_reveal=dict(x_left=fr["u_left"], x_right=fr["u_right"], width=fr["width"],
                                             center_x=(fr["u_left"] + fr["u_right"]) / 2, top_z=fr["top_z"],
                                             bottom_z=e_["sill_z"]), _side=True)
    for aid, keys in IFACE_KEYS.items():
        if "dormer" in aid:
            continue
        keys = [keys] if isinstance(keys, str) else keys
        key = next((k for k in keys if k in wins), None)
        e = wins.get(key) if key else None
        if not e:
            continue
        P = PARAMS[aid]
        W_open, H_open = float(e["width"]), float(e["height"])
        cx = float(e.get("center_x", 0.0))
        fb = e.get("frame_bible", {}) or {}
        if "x_left" in fb and "x_right" in fb:
            fw = fb["x_right"] - fb["x_left"]
        elif "x_left" in fb:
            fw = 2 * (cx - fb["x_left"])
        else:
            ref = wins.get("right_w1" if key.startswith("right") else "left_w2_cat", {})
            rfb = ref.get("frame_bible", {})
            if "dormer" in key:
                ref, rfb = {"width": 1.0}, {"x_left": 0.0, "x_right": 0.85}  # default 0.075 m lining
            fw = W_open - (ref["width"] - (rfb["x_right"] - rfb["x_left"]))
        fit = P.get("fit", {})
        if "frame_w" in fit:
            fw = fit["frame_w"]
        far = e.get("frame_at_reveal")
        if far:   # v2: exact frame outline at the reveal plane
            fw = float(far["width"])
            fit = {k2: v2 for k2, v2 in fit.items() if k2 != "reveal"}
        band = (W_open - fw) / 2
        if e.get("head_shape") == "semicircular":
            fh = float(e["springing_z"]) - float(e["sill_z"]) + P["sash"].get("rise_frac", 1.0) * fw / 2
        elif "top_z" in fb:
            fh = float(fb["top_z"]) - float(e["sill_z"])
        else:
            ref = wins.get("right_w1" if key.startswith("right") else "left_w2_cat", {})
            rfb = ref.get("frame_bible", {})
            if "dormer" in key:
                ref, rfb = {}, {}
            top_lining = (ref["height"] - (rfb["top_z"] - ref["sill_z"])) if "top_z" in rfb else band
            fh = H_open - top_lining
        if far:
            fh = float(far["top_z"]) - float(far.get("bottom_z", e["sill_z"]))
            if e.get("head_shape") in ("elliptical", "semicircular") and "springing_z" in e:
                rf = (float(far["top_z"]) - float(e["springing_z"])) / (fw / 2)
                P["sash"]["rise_frac"] = rf
                if "surround" in P:
                    P["surround"]["rise_frac"] = rf
        k = fw / P["W"]
        P["k"] = k
        if far:
            P["frame_dx"] = float(far["center_x"]) - cx          # metres, applied after scaling
            P["hole"] = [(float(e["x_left"]) - cx) / k, (float(e["x_right"]) - cx) / k, H_open / k]
        P["H"] = fh / k
        P["sash"]["reveal"] = float(fit.get("reveal", e.get("reveal_depth", 0.2))) / k
        if "surround" in P:
            P["surround"]["band"] = band / k
            P["surround"]["reveal"] = P["sash"]["reveal"]
        P["place"] = (cx, float(e["sill_z"]))
        if e.get("_side"):
            P["side_place"] = dict(face="side_right", u_center=cx, sill_z=float(e["sill_z"]))
        used[aid] = dict(key=key, frame_dx=round(P.get("frame_dx", 0.0), 3), opening=[W_open, H_open], frame=[round(fw, 4), round(fh, 4)], band=round(band, 4),
                         k=round(k, 4), sill=[cx, e["sill_z"]],
                         reveal=round(P["sash"]["reveal"] * k, 3),
                         frame_vs_opening=dict(dw=round(fw - W_open, 3), dh=round(fh - H_open, 3),
                                               frame_vs_frame_bible_w=round(fw - ((fb.get("x_right", 0) - fb.get("x_left", 0)) or fw), 3)))
    for aid, keys in IFACE_KEYS.items():
        if "dormer" not in aid:
            continue
        dm = data.get("dormers", {}) or {}
        key = next((k for k in keys if k in dm), None)
        if not key:
            continue
        e = dm[key]
        P = PARAMS[aid]
        W_open = float(e["opening_width"])
        H_open = float(e["head_z"]) - float(e["sill_z"])
        band = P["band"]
        P["W"], P["H"], P["k"] = W_open - 2 * band, H_open - band, 1.0
        P["face_y"] = float(e.get("face_y", 0.0))
        if "reveal_depth" in e:
            P["sash"]["reveal"] = float(e["reveal_depth"])
        if "face" in e:
            P["side_place"] = dict(face=e["face"], u_center=float(e["u_center"]), sill_z=float(e["sill_z"]),
                                   face_x=float(e.get("face_x", 0.0)))
            P["place"] = (float(e["u_center"]), float(e["sill_z"]))
        P["body_w"] = float(e.get("body_width", P["body_w"]))
        P["ridge"] = float(e.get("ridge_z", float(e["sill_z"]) + P["ridge"])) - float(e["sill_z"])
        if "face" not in e:
            P["place"] = (float(e["center_x"]), float(e["sill_z"]))
        used[aid] = dict(key=key, opening=[W_open, round(H_open, 3)], frame=[round(P["W"], 3), round(P["H"], 3)],
                         band=band, k=1.0, sill=[e.get("center_x", e.get("u_center")), e["sill_z"]], face_y=P["face_y"])
    st = data.get("storeys", {})
    ground_top = st.get("ground", {}).get("z1")
    if ground_top and "place" in PARAMS["aa_window_l1_arched"]:
        P = PARAMS["aa_window_l1_arched"]
        P["hood"]["top"] = (ground_top - P["place"][1]) / P["k"]
    if ground_top and "place" in PARAMS["aa_window_l2_cat"]:
        P = PARAMS["aa_window_l2_cat"]
        P["apron"]["depth"] = (P["place"][1] - ground_top) / P["k"]
    return used


# --------------------------------------------------------------------------------------
# Scene helpers
# --------------------------------------------------------------------------------------
def reset_file():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def append_from_main(names):
    with bpy.data.libraries.load(str(MAIN_BLEND), link=False) as (src, dst):
        dst.objects = [n for n in names if n in src.objects]
    main_dir = MAIN_BLEND.parent
    for im in bpy.data.images:
        fp = im.filepath
        if fp.startswith("//"):
            im.filepath = str((main_dir / fp[2:]).resolve())
    return {o.name: o for o in dst.objects if o is not None}


def crest_mesh(src_ob, w, h, name):
    """Copy of the Tripo crest mesh normalised to w x h, back face on y=0, bottom at z=0."""
    me = src_ob.data.copy()
    me.name = name
    me.transform(src_ob.matrix_basis)
    xs = [v.co.x for v in me.vertices]
    ys = [v.co.y for v in me.vertices]
    zs = [v.co.z for v in me.vertices]
    sx = w / (max(xs) - min(xs))
    sz = h / (max(zs) - min(zs))
    sy = (sx + sz) / 2 * 1.5   # deeper undercut relief than the Tripo bake (crops read crisp and deep)
    cx = (max(xs) + min(xs)) / 2
    me.transform(Matrix.Translation((-cx, -max(ys), -min(zs))))
    me.transform(Matrix.Diagonal((sx, sy, sz, 1)))
    return me


def tidy_tripo(me, max_faces):
    """Collapse-decimate a Tripo HD mesh to max_faces (visually lossless at window scale) and
    make its winding consistent."""
    import bmesh
    if len(me.polygons) > max_faces:
        tmp = bpy.data.objects.new("_tmp_dec", me)
        bpy.context.scene.collection.objects.link(tmp)
        m = tmp.modifiers.new("dec", "DECIMATE")
        m.ratio = max_faces / len(me.polygons)
        dg = bpy.context.evaluated_depsgraph_get()
        ev = tmp.evaluated_get(dg)
        new = bpy.data.meshes.new_from_object(ev)
        bpy.data.objects.remove(tmp)
        me.clear_geometry()
        bm = bmesh.new()
        bm.from_mesh(new)
        bm.to_mesh(me)
        bm.free()
        bpy.data.meshes.remove(new)
    bm = bmesh.new()
    bm.from_mesh(me)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me)
    bm.free()


CREST_MAT = []


def add_crest(coll, src, name, w, h, loc):
    me = crest_mesh(src, w, h, name)
    # clean carved stone (the Tripo texture carries painted weathering; distress belongs to the author)
    if me.uv_layers:
        me.uv_layers[0].name = "uv_bake"
    me.materials.clear()
    me.materials.append(CREST_MAT[0])
    for p in me.polygons:
        p.material_index = 0
    e2_lib.box_uv(me)
    me.uv_layers["uv_material"].active_render = True
    me.uv_layers.active = me.uv_layers["uv_bake"] if "uv_bake" in me.uv_layers else me.uv_layers["uv_material"]
    ob = bpy.data.objects.new(name, me)
    ob.location = loc
    coll.objects.link(ob)
    bake_loc(ob)
    me.uv_layers.active = me.uv_layers["uv_bake"]
    e2_lib.smart_uv(ob)   # fresh uv_bake (the Tripo atlas has zero-area faces after the cut and cap)
    return ob


def bake_loc(ob):
    ob.data.transform(Matrix.Translation(ob.location))
    ob.location = (0, 0, 0)


def obj(mb, name, coll, M, **kw):
    if not mb.v:
        return None
    return to_object(mb, name, coll, M, **kw)


def foliage_obj(leaves, tints, name, coll, M):
    ob = to_object(leaves, name, coll, M, recalc=False, smooth_angle=180)
    set_color_attr(ob, "leaf_tint", tints)
    return ob


# --------------------------------------------------------------------------------------
# Shared builders
# --------------------------------------------------------------------------------------
def interior(mb, W, H, y0, depth=0.7, arch=False):
    """Dim room box behind the frame (open toward the street); its walls key 1 cm into the frame."""
    x0, x1, z0, z1 = -W / 2 + 0.01, W / 2 - 0.01, 0.01, H - 0.01
    y0 = y0 - 0.01
    y1 = y0 + depth
    vs = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    fs = [(0, 1, 2, 3), (4, 7, 6, 5), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]
    mb.add(vs, fs, "void")


def sash_set(aid, coll, M, W, H, P, pose=0.0, curtain=None, seed=1):
    parts, zb, travel = sash_window(None, W, H, P)
    out = {}
    out["frame"] = obj(parts["frame"], f"{aid}_frame", coll, M)
    out["sash_upper"] = obj(parts["sash_upper"], f"{aid}_sash_upper", coll, M)
    lo = obj(parts["sash_lower"], f"{aid}_sash_lower", coll, M)
    lo.location.z = zb + travel * pose
    lo["e2_moving_part"] = "lower sash: slides up only along +Z; travel 0..%.3f m" % travel
    lo["e2_travel_max"] = travel
    lo["e2_closed_z"] = zb
    out["sash_lower"] = lo
    room = MB()
    interior(room, W, H, P["reveal"] + P["frame_d"])
    out["interior"] = obj(room, f"{aid}_interior", coll, M)
    if curtain == "panels":
        cmb = MB()
        fw = P["frame_w"]
        y = P["reveal"] + P["frame_d"] + 0.03
        top = H - fw - 0.04
        gathered_curtains(cmb, -W / 2 + fw, W / 2 - fw, 0.05, top, y, seed=seed)
        out["curtain"] = obj(cmb, f"{aid}_curtain", coll, M, recalc=False, smooth_angle=180)
        rod = MB()
        rod.tube([(-W / 2 - 0.09, y, top + 0.005), (W / 2 + 0.09, y, top + 0.005)], 0.008, "brass", sides=8)
        out["rod"] = obj(rod, f"{aid}_curtain_rod", coll, M)
    if curtain == "cord":
        cmb, cord = MB(), MB()
        fw = P["frame_w"]
        y = P["reveal"] + P["frame_d"] + 0.035
        split = zb + (H - fw - zb) * (1 - P["upper_frac"])
        z_tie = split - 0.06
        # cord tied to the frame's inner faces; extend ends into the stiles
        cord_curtain(MB(), cord, -W / 2 + fw * 0.5, W / 2 - fw * 0.5, z_tie, 0.05, 0.075, y, seed=seed)
        # cord is behind the frame: anchor it with two cup hooks into the interior reveal
        for sx in (-1, 1):
            cord.box((sx * (W / 2 - fw * 0.5) - 0.006, P["reveal"] + P["frame_d"] - 0.002, z_tie - 0.008),
                     (sx * (W / 2 - fw * 0.5) + 0.006, y - 0.004, z_tie + 0.008), "brass")
        out["curtain"] = cloth_curtain(f"{aid}_curtain", coll, M, -W / 2 + fw * 0.5, W / 2 - fw * 0.5, z_tie,
                                       0.045, 0.075, y + 0.012, seed=seed)
        out["cord"] = obj(cord, f"{aid}_cord", coll, M)
    return out, zb, travel


def cloth_curtain(name, coll, M, x0, x1, z_tie, z_bot, sag, y, seed=1, nu=64, nv=56):
    """Sheer curtain hung from a sagging cord pinched at the centre, sculpted as cloth: the panel is
    gathered toward the pinch along the cord, and loose, irregular folds radiate from the pinch
    (random fold count, phase and amplitude per fold), deepening toward the hem, with a soft billow
    toward the glass and an uneven hem. (A headless cloth sim was tried first: Blender 5.2's pinned
    cloth with a rest shape key did not buckle in background mode, so the folds are sculpted.)"""
    import random
    R = random.Random(seed)
    w = x1 - x0
    xc = (x0 + x1) / 2

    def cord_z(u):
        return z_tie - sag * math.sin(math.pi * u)

    def gather(u):
        d = u - 0.5
        return 0.5 + math.copysign(abs(2 * d) ** 1.9 / 2, d)
    zp = cord_z(0.5)
    folds = [(R.uniform(5.0, 13.0), R.uniform(0, 6.283), R.uniform(0.4, 1.0)) for _ in range(5)]
    hem = [(R.uniform(3, 9), R.uniform(0, 6.283)) for _ in range(3)]
    drape = [(R.uniform(4.0, 9.0), R.uniform(0, 6.283), R.uniform(0.5, 1.0)) for _ in range(4)]
    verts = []
    for j in range(nv + 1):
        t = j / nv
        for i in range(nu + 1):
            u = i / nu
            ut = gather(u)
            uu = ut + (u - ut) * min(1.0, t * 1.4)
            x = x0 + w * uu
            ztop = cord_z(ut)
            zb = z_bot + 0.02 * sum(math.sin(f * u * math.pi + ph) for f, ph in hem) / 3
            z = ztop - (ztop - zb) * t
            dx, dz = x - xc, max(zp - z, 1e-3)
            r = math.hypot(dx, dz)
            phi = math.atan2(dx, dz)
            amp = (0.010 + 0.040 * (1 - math.exp(-r / 0.18))) * (1.0 - 0.7 * (1 - t) ** 6)
            d = sum(a * math.sin(f * phi + ph) for f, ph, a in folds) / 2.6
            # tight bunching right at the pinch
            d += 0.010 * math.exp(-r / 0.06) * math.sin(28 * phi)
            bil = 0.022 * math.sin(math.pi * u) * t ** 1.3
            # hanging drape folds, deepening toward the hem
            bil += 0.02 * t ** 1.2 * sum(a * math.sin(2 * math.pi * f * u + ph) for f, ph, a in drape) / 2.2
            yy = y + amp * d + bil
            verts.append((x, yy, z))
    faces = []
    for j in range(nv):
        for i in range(nu):
            a = j * (nu + 1) + i
            faces.append((a, a + 1, a + nu + 2, a + nu + 1))
    me = bpy.data.meshes.new(name)
    me.from_pydata(verts, [], faces)
    import numpy as np
    arr = np.zeros((len(me.loops), 2))
    lv = np.empty(len(me.loops), dtype=np.int64)
    me.loops.foreach_get("vertex_index", lv)
    arr[:, 0] = (lv % (nu + 1)) / nu
    arr[:, 1] = 1 - (lv // (nu + 1)) / nv
    for nm in ("uv_material", "uv_bake"):
        me.uv_layers.new(name=nm).data.foreach_set("uv", arr.ravel())
    me.uv_layers["uv_material"].active_render = True
    me.uv_layers.active = me.uv_layers["uv_bake"]
    me.materials.append(M["curtain"])
    me.shade_smooth()
    ob = bpy.data.objects.new(name, me)
    coll.objects.link(ob)
    return ob


def tbar_stone(aid, coll, M, W, H, P, crest_src):
    """Moulded surround + crown + crest pediment (L2/R1/L3/R2)."""
    s, cr = P["surround"], P["crown"]
    st = MB()
    hole = P.get("hole")
    if hole:
        # v2: moulding on mason's hole edges; flat lining band filled per side between the hole and the
        # (off-centre) frame, front face proud by pb, back to the frame face (reveal)
        xl, xr, Ht = hole
        dx = P.get("frame_dx", 0.0) / P.get("k", 1.0)
        fl, fr = dx - W / 2, dx + W / 2
        R_ = P["sash"]["reveal"]
        path = [Vector((xl, 0, 0)), Vector((xl, 0, Ht)), Vector((xr, 0, Ht)), Vector((xr, 0, 0))]
        st.sweep(path, architrave_profile(0.0, s["mold"], s["pb"], s["pm"]), "stone")
        pb = s["pb"]
        if fl - xl > 1e-4:
            st.box((xl, -pb, 0.0), (fl, R_ + 0.004, Ht), "stone")
        if xr - fr > 1e-4:
            st.box((fr, -pb, 0.0), (xr, R_ + 0.004, Ht), "stone")
        if Ht - H > 1e-4:
            st.box((max(xl, fl), -pb, H), (min(xr, fr), R_ + 0.004, Ht), "stone")
        outer_l, outer_r = xl - s["mold"], xr + s["mold"]
        top = crown_cornice(st, outer_l - 0.04, outer_r + 0.04, Ht + s["mold"], cr["proj"], cr["h"])
    else:
        surround_rect(st, W, H, s["band"], s["mold"], s["pb"], s["pm"], reveal=P["sash"]["reveal"])
        outer = W / 2 + s["band"] + s["mold"]
        top = crown_cornice(st, -outer - 0.04, outer + 0.04, H + s["band"] + s["mold"], cr["proj"], cr["h"])
    ob = obj(st, f"{aid}_surround", coll, M)
    if "crest" not in P:
        return ob, None, top
    c = P["crest"]
    crest = add_crest(coll, crest_src, f"{aid}_pediment_crest", c["w"], c["h"], (0, 0, top - 0.005))
    return ob, crest, top


def sill_apron(aid, coll, M, W, P, crest_src=None):
    s, a = P["sill"], P["apron"]
    mb = MB()
    zb = sill_slab(mb, s["w"], s["proj"], P["sash"]["reveal"] + 0.02, s["t"])
    fascia(mb, a["console_x"] * 2 - a["cw"] + 0.004, zb, s["fascia"], 0.05)
    for sx in (-1, 1):
        console(mb, sx * a["console_x"], a["cw"], zb, a["D"], a["Hc"], drop=(crest_src is None))
    ob = obj(mb, f"{aid}_sill", coll, M)
    crest = None
    if crest_src is not None:
        top = zb - s["fascia"]
        zc = (top - a["depth"]) / 2 - a["crest_h"] / 2
        crest = add_crest(coll, crest_src, f"{aid}_apron_crest", a["crest_w"], a["crest_h"], (0, 0, zc))
        # apron panel the relief is carved on (slightly proud, between the consoles)
        pnl = MB()
        x = a["console_x"] - a["cw"] / 2
        pnl.box((-x, -0.012, -a["depth"]), (x, 0.0, zb - s["fascia"]), "stone")
        bake_y = obj(pnl, f"{aid}_apron_panel", coll, M)
        crest.data.transform(Matrix.Translation((0, -0.012, 0)))
    return ob, crest


def balcony(aid, coll, M, W, P, seed, mirror=False):
    sl, rl = P["slab"], P["rail"]
    mb = MB()
    zb = sill_slab(mb, sl["w"], sl["proj"], P["sash"]["reveal"] + 0.02, sl["t"])
    fascia(mb, sl["console_x"] * 2 - sl["cw"] + 0.004, zb, sl["fascia"], 0.04)
    for sx in (-1, 1):
        console(mb, sx * sl["console_x"], sl["cw"], zb, sl["D"], sl["Hc"])
    ob = obj(mb, f"{aid}_slab", coll, M)
    ir = MB()
    h, y0, bul = rl["h"], rl["y"], rl["bulge"]

    def yfn(z):  # bombe: belly swells forward in the lower half
        t = z / h
        return y0 - bul * math.sin(math.pi * min(1.0, t * 1.35)) * (1 - t * 0.3)
    hx = rl["half"]
    railing_lattice(ir, -hx, hx, h, yfn, posts=[-hx, hx], finials=[(-hx, "urn"), (hx, "urn")],
                    style=rl.get("style", "x"))
    for sx in (-1, 1):
        side_returns(ir, sx * hx, yfn(0.012), -0.0233, h)
    ob_ir = obj(ir, f"{aid}_railing", coll, M)
    return ob, ob_ir


# --------------------------------------------------------------------------------------
# Kits
# --------------------------------------------------------------------------------------
def kit_l1(coll, M, P):
    aid = "aa_window_l1_arched"
    W, H, S = P["W"], P["H"], P["sash"]
    parts, zb, s = arched_window(W, H, S)
    obj(parts["frame"], f"{aid}_frame", coll, M)
    lo = obj(parts["sash_lower"], f"{aid}_sash_lower", coll, M)
    lo.location.z = zb
    travel = (H - S["frame_w"]) - s  # can only rise into the fanlight zone behind the transom
    lo["e2_moving_part"] = "lower sash: slides up only along +Z (posed closed)"
    lo["e2_travel_max"] = max(0.0, travel - 0.05)
    lo["e2_closed_z"] = zb
    room = MB()
    interior(room, W, H, S["reveal"] + S["frame_d"])
    obj(room, f"{aid}_interior", coll, M)
    cur = MB()
    yc = S["reveal"] + S["frame_d"] + 0.03
    gathered_curtains(cur, -W / 2 + S["frame_w"], W / 2 - S["frame_w"], 0.06, s - 0.06, yc)
    obj(cur, f"{aid}_curtain", coll, M, recalc=False, smooth_angle=180)
    rod = MB()
    rod.tube([(-W / 2 - 0.09, yc, s - 0.055), (W / 2 + 0.09, yc, s - 0.055)], 0.008, "brass", sides=8)
    obj(rod, f"{aid}_curtain_rod", coll, M)
    # stone: arched surround, hood cornice on consoles, sill on consoles
    st = MB()
    arch_surround(st, W, H, P["surround"])
    hd = P["hood"]
    hood = MB()
    zt = hd["top"]
    # hood cornice reads like a sill slab: flashing on top, nose, fascia, end consoles
    zb_h = sill_slab(hood, hd["w"], hd["proj"], 0.0, hd["t"])
    hood.transform(Matrix.Translation((0, 0, zt)))
    zb_h += zt
    fascia(hood, hd["w"] - 0.06, zb_h, hd["fascia"], 0.07)
    for sx in (-1, 1):
        console(hood, sx * hd["console_x"], 0.13, zb_h - hd["fascia"], 0.12, 0.18)
    obj(st, f"{aid}_surround", coll, M)
    obj(hood, f"{aid}_hood", coll, M)
    sl = P["sill"]
    smb = MB()
    zsb = sill_slab(smb, sl["w"], sl["proj"], S["reveal"] + 0.02, sl["t"])
    fascia(smb, sl["console_x"] * 2 + 0.1, zsb, sl["fascia"], 0.05)
    for sx in (-1, 1):
        console(smb, sx * sl["console_x"], 0.13, zsb - sl["fascia"] + 0.002, 0.13, 0.16)
    obj(smb, f"{aid}_sill", coll, M)
    # keystone floral (placeholder carving until the Tripo relief lands) sits between arch and hood
    key = keystone_floral(coll, M, aid, z0=H + P["surround"]["band"] + P["surround"]["ring"] + 0.03,
                          z1=zb_h - hd["fascia"] + 0.005)
    # balconette railing at the sill front, pots BEHIND it on the sill (crop w1)
    ir = MB()
    hx = 0.47
    yr = -0.19
    railing_web(ir, -hx, hx, 0.36, yr, finials=[(-hx, "ball"), (-0.22, "urn"), (hx, "ball")])
    for sx in (-1, 1):
        side_returns(ir, sx * (hx - 0.003), yr, -0.062, 0.36)
    obj(ir, f"{aid}_railing", coll, M)
    pots_plants(aid, coll, M, [
        dict(x=-0.255, y=-0.035, rt=0.125, h=0.14, rb=0.088,
             bush=dict(rx=0.10, ry=0.08, rz=0.08, n=200, leaf=0.032, flowers=(0.02, ("petal_orange", "petal_yellow"), 0.25))),
        dict(x=0.12, y=-0.035, rt=0.136, h=0.15, rb=0.095,
             bush=dict(rx=0.25, ry=0.14, rz=0.28, n=300, leaf=0.075, lift=0.06, droop=0.1, width=0.7, main=5,
                       lean=(-0.02, 0.03, 0.0))),
    ], seed=11)
    return key


def keystone_floral(coll, M, aid, z0, z1):
    """Carved acanthus fleur on the keystone (procedural; replaced by the Tripo relief when present)."""
    tri = bpy.data.objects.get("e2_keystone_rosette_l1") or bpy.data.objects.get("e2_keystone_rosette")
    h = z1 - z0
    if tri is not None:
        me = tri.data.copy()
        me.name = f"{aid}_keystone_floral"
        xs = [v.co.x for v in me.vertices]
        ys = [v.co.y for v in me.vertices]
        zs = [v.co.z for v in me.vertices]
        h = min(h, 0.25)
        sc = h / (max(zs) - min(zs))
        me.transform(Matrix.Translation((-(max(xs) + min(xs)) / 2, -max(ys), -min(zs))))
        me.transform(Matrix.Diagonal((sc, sc * 1.4, sc, 1)))         # squat rosette (crop w1)
        me.transform(Matrix.Translation((0, 0.0, z0 - 0.015)))       # seated on the ring crown
        # drop the flat back cap left by the bisect: it lies on the wall plane, hidden, and overlapped
        # a few relief faces there (QA z-fight pairs)
        import bmesh
        bm_ = bmesh.new()
        bm_.from_mesh(me)
        ymax = max(v.co.y for v in bm_.verts)
        back = [f for f in bm_.faces if abs(f.normal.y) > 0.98 and all(v.co.y > ymax - 0.0015 for v in f.verts)]
        bmesh.ops.delete(bm_, geom=back, context="FACES")
        bm_.to_mesh(me)
        bm_.free()
        if me.uv_layers:
            me.uv_layers[0].name = "uv_bake"
        me.materials.clear()
        me.materials.append(CREST_MAT[0])
        for p in me.polygons:
            p.material_index = 0
        e2_lib.box_uv(me)
        me.uv_layers["uv_material"].active_render = True
        me.uv_layers.active = me.uv_layers["uv_bake"] if "uv_bake" in me.uv_layers else me.uv_layers["uv_material"]
        ob = bpy.data.objects.new(f"{aid}_keystone_floral", me)
        coll.objects.link(ob)
        # fresh non-overlapping uv_bake (the Tripo atlas lost its back half and gained a cap)
        me.uv_layers.active = me.uv_layers["uv_bake"]
        e2_lib.smart_uv(ob)
        return ob
    mb = MB()
    cz = z0 + h * 0.45
    y = -0.05
    # central bud
    mb.lathe([(0.0, 0.0), (0.035, 0.01), (0.05, 0.05), (0.04, 0.09), (0.0, 0.12)], 14, "stone",
             center=(0, y - 0.03, cz - 0.06), sx=1.0, sy=0.7, cap_bottom=True)
    # acanthus leaves fanning out (thick stone leaves)
    for ang, L in [(90, 0.13), (35, 0.15), (145, 0.15), (-20, 0.12), (200, 0.12), (-60, 0.09), (240, 0.09)]:
        a = math.radians(ang)
        axis = Vector((math.cos(a), -0.25, math.sin(a))).normalized()
        sd = Vector((-math.sin(a), 0, math.cos(a)))
        v, fc, uv = leaf_geo(Vector((0, y - 0.02, cz)), axis, sd, L, 0.75, fold=-0.35, curl=-0.25,
                             shape=lambda t: math.sin(math.pi * min(t * 1.05, 1)) ** 0.6 * (1 + 0.25 * math.sin(t * 18)))
        # thicken: back copy offset into the wall
        o = mb.add(v, fc, "stone")
        vb = [tuple(Vector(p) + Vector((0, 0.025, 0))) for p in v]
        mb.add(vb, [tuple(reversed(f)) for f in fc], "stone")
    ob = obj(mb, f"{aid}_keystone_floral", coll, M, recalc=False, smooth_angle=60)
    return ob


def pots_plants(aid, coll, M, specs, seed):
    """Round 2: classic rolled-rim pots + mounded leaf shrubs / flowering cascades (e2_flora)."""
    potmb, leaves, stems, tints = MB(), MB(), MB(), []
    extra = MB()
    for i, s in enumerate(specs):
        top, r_s = pot2(potmb, (s["x"], s["y"], 0.0), s["rt"], s["h"], s["rb"], mat=s.get("mat", "terracotta"),
                        bulge=s.get("bulge", 0.0))
        b_ = s.get("bush")
        if b_:
            bush(leaves, stems, tints, top, b_["rx"], b_["ry"], b_["rz"], b_["n"], b_["leaf"], seed + i * 7,
                 lift=b_.get("lift", 0.0), flowers=b_.get("flowers"), droop=b_.get("droop", 0.25),
                 leaf_width=b_.get("width", 0.62), n_main=b_.get("main", 6), lean=b_.get("lean", (0, 0, 0)))
        c_ = s.get("cascade")
        if c_:
            cascade(leaves, stems, tints, top, c_["length"], c_["n"], seed + 99 + i, side=c_.get("side", -1),
                    fmats=c_.get("fmats", ("petal_pink",)), flower_p=c_.get("flower_p", 0.45),
                    leaf_size=c_.get("leaf", 0.042), spread=c_.get("spread", 0.18))
        w_ = s.get("wall_cascade")
        if w_:
            wall_cascade(leaves, stems, tints, top, w_["ledge_end_x"], w_["ledge_front_y"], w_["ledge_top_z"],
                         w_["drop"], w_["n"], seed + 77 + i, side=-1, fmats=("petal_pink",),
                         flower_p=w_["flower_p"], leaf_size=w_["leaf"], spread=w_["spread"])
        if s.get("lamp"):
            lp = s["lamp"]
            dome_lamp(extra, (top[0] + 0.02, top[1] + 0.02, top[2] - 0.008), lp["top"], lp["dome_r"])
    obj(potmb, f"{aid}_pots", coll, M)
    if leaves.v:
        foliage_obj(leaves, tints, f"{aid}_foliage", coll, M)
        obj(stems, f"{aid}_stems_flowers", coll, M, smooth_angle=60, bake_uv="norm")
    if extra.v:
        obj(extra, f"{aid}_lamp", coll, M)


def kit_l2(coll, M, P, crest_src):
    aid = "aa_window_l2_cat"
    W, H, S = P["W"], P["H"], P["sash"]
    sash_set(aid, coll, M, W, H, S, pose=P["pose_open"], curtain="cord", seed=21)
    # L2's own pediment and apron carving (Tripo from crop w2), not the R1 crest
    ped = bpy.data.objects.get("e2_pediment_l2") or crest_src
    tbar_stone(aid, coll, M, W, H, P, ped)
    sill_apron(aid, coll, M, W, P, ped)
    # one pot on the left; the cat (aa_prop_window_cat) sits on the right, outside the glass (crop w2)
    pots_plants(aid, coll, M, [
        dict(x=-0.17, y=-0.05, rt=0.155, h=0.165, rb=0.11,
             bush=dict(rx=0.25, ry=0.15, rz=0.19, n=900, leaf=0.05, lift=-0.01, lean=(-0.02, 0.0, 0.0))),
    ], seed=31)


def kit_r1(coll, M, P, crest_src):
    aid = "aa_window_r1"
    W, H, S = P["W"], P["H"], P["sash"]
    sash_set(aid, coll, M, W, H, S, pose=0.0, curtain="cord", seed=41)
    tbar_stone(aid, coll, M, W, H, P, crest_src)
    sill_apron(aid, coll, M, W, P, None)
    pots_plants(aid, coll, M, [
        dict(x=-0.18, y=-0.03, rt=0.096, h=0.145, rb=0.07,
             bush=dict(rx=0.14, ry=0.10, rz=0.12, n=300, leaf=0.034, droop=0.5, main=7),
             lamp=dict(top=(-0.19, -0.05, 0.30), dome_r=0.08)),
        dict(x=0.152, y=-0.03, rt=0.132, h=0.17, rb=0.095,
             bush=dict(rx=0.21, ry=0.14, rz=0.15, n=620, leaf=0.046)),
    ], seed=51)


def kit_side(aid, coll, M, P):
    """Side-elevation window (asset sheet crop 14)."""
    W, H, S = P["W"], P["H"], P["sash"]
    sash_set(aid, coll, M, W, H, S, pose=0.0, curtain="panels", seed=sum(map(ord, aid)) % 97)
    tbar_stone(aid, coll, M, W, H, P, None)
    sill_apron(aid, coll, M, W, P, None)
    fl = (0.026, ("petal_red", "petal_red", "petal_orange"), 0.75)
    pots = [dict(x=sx * 0.13, y=-0.06, rt=0.105, h=0.13, rb=0.075,
                 bush=dict(rx=0.16, ry=0.10, rz=0.15, n=460, leaf=0.04, flowers=fl, lift=0.02)) for sx in (-1, 1)]
    pots_plants(aid, coll, M, pots, seed=sum(map(ord, aid)) % 89)
    if aid.endswith("w0"):
        # awning mount for E6: two wall plates with eye lugs at the awning zone's top corners
        mt = MB()
        k = P.get("k", 1.0)
        z_top = (5.06 - P["place"][1]) / k
        for sx in (-1, 1):
            x = sx * 0.50 / k
            mt.box((x - 0.03, -0.012, z_top - 0.10), (x + 0.03, 0.002, z_top), "iron")
            mt.tube([(x, -0.012, z_top - 0.03), (x, -0.06, z_top - 0.03)], 0.007, "iron", sides=6)
            mt.lathe([(0.012, 0.0), (0.018, 0.0), (0.018, 0.008), (0.012, 0.008)], 10, "iron",
                     center=(x, -0.066, z_top - 0.034), cap_bottom=True, cap_top=True)
        mo = obj(mt, f"{aid}_awning_mount", coll, M)
        mo["e2_note"] = "E6 awning hangs from these two lugs (awning zone z 4.75-5.06, width 1.15)"


def kit_balcony(aid, coll, M, P, crest_src, mirror, seed):
    W, H, S = P["W"], P["H"], P["sash"]
    sash_set(aid, coll, M, W, H, S, pose=0.0, curtain=("panels" if aid.endswith("r2") else None), seed=seed)
    tbar_stone(aid, coll, M, W, H, P, crest_src)
    balcony(aid, coll, M, W, P, seed)
    if not mirror:  # L3 (crop w3): copper pot + terracotta pot behind the belly rail, vine pot at the left end
        specs = [
            dict(x=-0.10, y=0.0, rt=0.09, h=0.14, rb=0.075, mat="copper", bulge=0.1,
                 bush=dict(rx=0.18, ry=0.11, rz=0.25, n=620, leaf=0.05, lift=0.08, droop=0.1, main=7)),
            dict(x=0.12, y=0.012, rt=0.118, h=0.13, rb=0.085,
                 bush=dict(rx=0.13, ry=0.09, rz=0.25, n=520, leaf=0.05, lift=0.08, droop=0.1, main=6,
                           lean=(0.02, 0.0, 0.0))),
            dict(x=-0.33, y=-0.075, rt=0.062, h=0.085, rb=0.045,
                 bush=dict(rx=0.16, ry=0.10, rz=0.09, n=420, leaf=0.038, droop=0.6,
                           flowers=(0.026, ("petal_pink",), 1.0), lean=(-0.07, -0.04, 0.0)),
                 wall_cascade=dict(ledge_end_x=-0.50, ledge_front_y=-0.165, ledge_top_z=-0.012, drop=0.62, n=46,
                                   spread=(-0.10, 0.30), flower_p=0.75, leaf=0.046)),
        ]
    else:  # R2 (asset sheet, author 2026-10-28): two pots of orange/yellow flowers behind a straight rail
        fl = (0.024, ("petal_orange", "petal_yellow"), 0.55)
        specs = [
            dict(x=-0.15, y=-0.01, rt=0.10, h=0.13, rb=0.072, bush=dict(rx=0.13, ry=0.09, rz=0.11, n=320, leaf=0.036, flowers=fl)),
            dict(x=0.15, y=-0.01, rt=0.10, h=0.13, rb=0.072, bush=dict(rx=0.13, ry=0.09, rz=0.11, n=320, leaf=0.036, flowers=fl)),
        ]
    pots_plants(aid, coll, M, specs, seed=seed + 5)


def kit_dormer(coll, M, P, aid):
    """Dormer WINDOW kit (opening cut by mason through his dormer front at face_y).

    Kit: cased sash frame (2 + 2 panes), moulded stone architrave + lining, ledge, flower guard,
    pots of flowers and the inner-side flowering vine (asset sheet). The dormer BODY (pilasters,
    pediment with medallion, slate cheeks and roof) is mason's; a stand-in is built into
    e2_dormer_body_standin/<aid>_body for the review renders and as a reference for mason.
    """
    vside = P["vine_side"]
    W, H, S = P["W"], P["H"], P["sash"]
    sash_set(aid, coll, M, W, H, S, pose=0.0, curtain=None)
    st = MB()
    band, mold = P["band"], 0.06
    surround_rect(st, W, H, band, mold, 0.02, 0.05, reveal=S["reveal"])
    xo = P["body_w"] / 2
    sill_slab(st, P["body_w"] + 0.08, 0.30, S["reveal"] + 0.02, 0.09)
    obj(st, f"{aid}_surround_ledge", coll, M)
    ir = MB()
    hx = xo - 0.01
    railing_lattice(ir, -hx, hx, 0.30, lambda z: -0.27, posts=[-hx, hx], finials=[(-hx, "ball"), (hx, "ball")],
                    style="scroll")
    for sx in (-1, 1):
        side_returns(ir, sx * hx, -0.27, -0.075, 0.30)
    obj(ir, f"{aid}_railing", coll, M)
    # asset sheet: two pots of orange/yellow/red flowers behind the rail, a flowering cascade over the inner end
    fl = (0.022, ("petal_orange", "petal_yellow", "petal_red"), 0.55)
    pots_plants(aid, coll, M, [
        dict(x=-0.13 * vside, y=-0.15, rt=0.085, h=0.11, rb=0.062, bush=dict(rx=0.11, ry=0.08, rz=0.10, n=260, leaf=0.034, flowers=fl)),
        dict(x=0.12 * vside, y=-0.15, rt=0.085, h=0.11, rb=0.062, bush=dict(rx=0.11, ry=0.08, rz=0.10, n=260, leaf=0.034, flowers=fl)),
        dict(x=(xo - 0.08) * vside, y=-0.16, rt=0.06, h=0.085, rb=0.045,
             bush=dict(rx=0.14, ry=0.10, rz=0.08, n=260, leaf=0.034, droop=0.6, lean=(0.06 * vside, -0.05, 0.0),
                       flowers=(0.024, ("petal_red", "petal_orange", "petal_yellow", "petal_white"), 0.8)),
             cascade=dict(length=0.9, n=26, side=vside, fmats=("petal_red", "petal_orange", "petal_yellow", "petal_white"),
                          flower_p=0.65, leaf=0.04, spread=0.2)),
    ], seed=71 if vside > 0 else 91)
    body_standin(aid, M, P)


def body_standin(aid, M, P):
    W, H = P["W"], P["H"]
    sb = get_coll("e2_dormer_body_standin")
    c = get_coll(f"{aid}_body", sb)
    st = MB()
    band, mold = P["band"], 0.06
    o = W / 2 + band + mold
    xo = P["body_w"] / 2
    z_ent0 = H + band + mold + 0.01
    for sx in (-1, 1):
        x0, x1 = sorted((sx * (o - 0.004), sx * xo))
        st.box((x0, -0.07, -0.02), (x1, 0.0, z_ent0), "stone")
        st.box((x0 - 0.012, -0.085, -0.02), (x1 + 0.012, 0.0, 0.06), "stone")
        st.box((x0 - 0.012, -0.085, z_ent0 - 0.06), (x1 + 0.012, 0.0, z_ent0), "stone")
    st.box((-xo - 0.03, -0.09, z_ent0), (xo + 0.03, 0.0, z_ent0 + 0.12), "stone")
    zt = z_ent0 + 0.12
    ph = max(0.2, P["ridge"] - zt - 0.06)
    tymp = [(-xo, zt), (xo, zt), (0.0, zt + ph * 0.86)]
    chamfer_block(st, tymp, 0.04, 0.004)
    for sx in (-1, 1):
        a = Vector((sx * (xo + 0.05), -0.0, zt - 0.005))
        b = Vector((0.0, 0.0, zt + ph))
        d = (b - a).normalized()
        prof = [(0.0, 0.0), (0.0, 0.10), (0.07, 0.10), (0.07, 0.0)]
        path = [a, b + d * 0.02] if sx < 0 else [b + d * 0.02, a]
        st.sweep(path, prof, "stone", normal=(0, -1, 0))
    medallion(st, 0.0, zt + ph * 0.36, ph * 0.2, -0.04)
    obj(st, f"{aid}_body_front", c, M)
    rf = MB()
    D = P["depth"]
    zb = -FLASH_T - 0.09
    for sx in (-1, 1):
        x0, x1 = sorted((sx * (xo - 0.06), sx * xo))
        rf.box((x0, 0.0, zb), (x1, D, zt), "slate")
    for sx in (-1, 1):
        a = Vector((sx * (xo + 0.06), 0.0, zt - 0.02))
        b = Vector((0.0, 0.0, zt + ph + 0.02))
        dv = (b - a).normalized()
        up = Vector((-dv.z, 0.0, dv.x))
        if up.z < 0:
            up = -up
        q = [a, b, b + up * 0.05, a + up * 0.05]
        vs = [tuple(p + Vector((0, 0.06, 0))) for p in q] + [tuple(p + Vector((0, D, 0))) for p in q]
        fs = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]
        rf.add(vs, fs, "slate")
    obj(rf, f"{aid}_body_cheeks_roof", c, M)


# --------------------------------------------------------------------------------------
def main():
    used = read_interfaces()
    reset_file()
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    M = make_materials(TEX)
    CREST_MAT.append(M["carved"])
    ext = get_coll("e2_external")  # cached source datablocks (not part of any kit)
    cache = AA / "blender/wip/E2_tripo_cache.blend"
    if not cache.exists():
        raise SystemExit("run prep_tripo_e2.py first (builds wip/E2_tripo_cache.blend)")
    names = ["e2_crest_src", "e2_keystone_rosette", "e2_keystone_rosette_l1", "e2_pediment_l2", "aa_prop_window_cat"]
    with bpy.data.libraries.load(str(cache), link=False) as (src, dst):
        dst.objects = [n for n in names if n in src.objects]
    for o in dst.objects:
        ext.objects.link(o)
        o.hide_render = True
        o.hide_set(True)
    crest_src = bpy.data.objects["e2_crest_src"]
    kit = get_coll("aa_kit")
    built = {}
    for aid in PARAMS:
        c = get_coll(aid, kit)
        P = PARAMS[aid]
        if aid == "aa_window_l1_arched":
            kit_l1(c, M, P)
        elif aid == "aa_window_l2_cat":
            kit_l2(c, M, P, crest_src)
        elif aid == "aa_window_r1":
            kit_r1(c, M, P, crest_src)
        elif aid == "aa_window_l3_balcony":
            kit_balcony(aid, c, M, P, crest_src, mirror=False, seed=61)
        elif aid == "aa_window_r2":
            kit_balcony(aid, c, M, P, crest_src, mirror=True, seed=81)
        elif aid.startswith("aa_window_dormer"):
            kit_dormer(c, M, P, aid)
        elif aid.startswith("aa_window_side"):
            kit_side(aid, c, M, P)
        k = P.get("k", 1.0)
        if abs(k - 1.0) > 1e-6:
            S4 = Matrix.Scale(k, 4)
            for o in c.objects:
                o.data.transform(S4)
                o.location = o.location * k
                for key in ("e2_travel_max", "e2_closed_z"):
                    if key in o:
                        o[key] = o[key] * k
                if "e2_moving_part" in o:
                    o["e2_moving_part"] = "lower sash: slides up only along +Z; travel 0..%.3f m" % o["e2_travel_max"]
                if not any(t in o.name for t in ("foliage", "curtain")):
                    e2_lib.box_uv(o.data)
        dxm = P.get("frame_dx", 0.0)
        if abs(dxm) > 1e-6:
            for o in c.objects:
                if any(o.name.endswith(t) for t in ("_frame", "_sash_upper", "_sash_lower", "_interior",
                                                     "_curtain", "_cord", "_curtain_rod")):
                    o.location.x += dxm
        built[aid] = [o.name for o in c.objects]
    # record parameters on the collections for mason
    for aid in PARAMS:
        c = bpy.data.collections[aid]
        c["e2_params"] = json.dumps(PARAMS[aid])
        c["e2_scale_k"] = PARAMS[aid].get("k", 1.0)
        if "place" in PARAMS[aid]:
            c["e2_place"] = list(PARAMS[aid]["place"])
        c["e2_pivot"] = "sill: bottom centre of the window opening, on the facade front plane (street -Y)"
        if "side_place" in PARAMS[aid]:
            c["e2_side_place"] = json.dumps(PARAMS[aid]["side_place"])
            c["e2_pivot"] += "; side-elevation kit: rotate +90 deg about Z so -Y faces +X, pivot at (face_x, u_center, sill_z)"
    WIP.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(WIP), compress=True)
    print("@@JSON@@" + json.dumps({"saved": str(WIP), "interfaces_used": used, "kits": {k: len(v) for k, v in built.items()}}))


if __name__ == "__main__":
    main()
