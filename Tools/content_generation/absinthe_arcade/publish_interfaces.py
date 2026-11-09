"""Publish dev/aa_team/interfaces.json (E1 building interface) from manifest.json -> facade.

Plain Python, no bpy:  python publish_interfaces.py [--check]

The manifest's facade block is the one source of the building's numbers (build_shell.py builds from
it). This script restates them in the shared interface format the E2-E6 agents read, adds the
derived numbers (frame outlines at the reveal through aa_bible_cam, interior volume, roof
footprint) and writes the file. --check prints the JSON instead of writing it.
"""

import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT = REPO / "dev" / "aa_team" / "interfaces.json"
M = json.loads((HERE / "manifest.json").read_text(encoding="utf-8"))
F = M["facade"]
CAMSPEC = M["bible_camera"]
CAM_LOC = CAMSPEC["location"]


def r3(v):
    return round(v, 3)


def at_reveal(x0, z0, y):
    """The point on plane y that aa_bible_cam sees where it sees (x0, 0, z0): a frame recessed to y
    with this outline projects exactly onto the bible's frame trace."""
    cx, cy, cz = CAM_LOC
    t = (y - cy) / (0.0 - cy)
    return cx + (x0 - cx) * t, cz + (z0 - cz) * t


def window(key, w, reveal):
    f = w["frame"]
    hw = w["w"] / 2
    e = {"center_x": w["cx"], "width": r3(w["w"]), "sill_z": w["sill"],
         "x_left": r3(w["cx"] - hw), "x_right": r3(w["cx"] + hw), "reveal_depth": reveal}
    fb = {"x_left": f["x"][0], "x_right": f["x"][1], "width": r3(f["x"][1] - f["x"][0])}
    if w["kind"] == "arched":
        e.update(head_shape="elliptical", springing_z=w["springing"], crown_z=w["crown"], head_z=w["crown"],
                 head_rise=r3(w["crown"] - w["springing"]), height=r3(w["crown"] - w["sill"]))
        fb.update(springing_z=f["springing"], crown_z=f["crown"], top_z=f["crown"],
                  height=r3(f["crown"] - w["sill"]))
        top_b = f["crown"]
    else:
        e.update(head_shape="flat", head_z=w["head"], height=r3(w["head"] - w["sill"]))
        fb.update(top_z=f["top"], height=r3(f["top"] - w["sill"]))
        if "transom" in f:
            fb["transom_z"] = f["transom"]
        top_b = f["top"]
    e["frame_bible"] = fb
    e["lining"] = {"sides": r3((e["width"] - fb["width"]) / 2), "head": r3(e["head_z"] - top_b)}
    # Exact 3D frame front outline at the reveal (what aa_bible_cam must see as frame_bible).
    xl, zt = at_reveal(f["x"][0], top_b, reveal)
    xr, _ = at_reveal(f["x"][1], top_b, reveal)
    # Keep the frame inside the hole (>= 0.01 lining): where the bible's lining is thinner than the
    # recess parallax (L1), slide the frame back in and report what the bible camera loses.
    shift = max(0.0, e["x_left"] + 0.01 - xl) - max(0.0, xr - (e["x_right"] - 0.01))
    drop = max(0.0, zt - (e["head_z"] - 0.01))
    xl, xr, zt = xl + shift, xr + shift, zt - drop
    e["frame_at_reveal"] = {"y": reveal, "x_left": r3(xl), "x_right": r3(xr), "width": r3(xr - xl),
                            "center_x": r3((xl + xr) / 2), "top_z": r3(zt), "bottom_z": w["sill"]}
    if shift or drop:
        dist = math.dist(CAM_LOC, (w["cx"], reveal, (w["sill"] + top_b) / 2))
        f_px = CAMSPEC["lens_mm"] / CAMSPEC["sensor_width_mm"] * CAMSPEC["resolution"][0]
        e["frame_at_reveal"]["clamped_into_opening"] = {
            "shift_x": r3(shift), "drop_z": r3(drop),
            "bible_cam_residual_px_at_5248": round(max(abs(shift), drop) * f_px / dist, 1)}
    if "transom" in f:
        e["frame_at_reveal"]["transom_z"] = r3(at_reveal(f["x"][0], f["transom"], reveal)[1])
    if "open" in w:
        e["lower_sash_raised"] = w["open"]
    return e


def side_window(w, reveal):
    f = w["frame"]
    hw = w["w"] / 2
    return {"u_center": w["cx"], "width": r3(w["w"]), "u_left": r3(w["cx"] - hw), "u_right": r3(w["cx"] + hw),
            "sill_z": w["sill"], "head_z": w["head"], "height": r3(w["head"] - w["sill"]), "head_shape": "flat",
            "reveal_depth": reveal,
            "frame": {"u_left": f["x"][0], "u_right": f["x"][1], "width": r3(f["x"][1] - f["x"][0]),
                      "top_z": f["top"], "height": r3(f["top"] - w["sill"])},
            "lining": {"sides": r3((w["w"] - (f["x"][1] - f["x"][0])) / 2), "head": r3(w["head"] - f["top"])},
            "world": {"face_x": F["x_right"], "center_y": w["cx"], "outward_normal": [1, 0, 0]}}


def main():
    sur = F["surround"]
    reveal = sur["reveal_depth"]
    walls = F["walls"]
    depth = M["building"]["depth"]
    A = F["arch"]
    CB = F["corner_bay"]
    RF = F["roof"]
    D = RF["dormer"]
    SR = F["side_right"]
    RC = F["right_corner"]
    cb_a = math.radians(CB["angle_deg"])
    cb_far = (F["x_left"] - math.cos(cb_a) * CB["width"], math.sin(cb_a) * CB["width"])
    back_inner = depth - walls["back_t"]
    door_line = 0.34
    out = {
        "_doc": ("E1 (mason-2) building interface. Blender space, metres: X right along the facade, Y into the "
                 "building (street is -Y), Z up. X=0 the arch axis (keystone head / marquee centre), Z=0 street level "
                 "at the facade, Y=0 the main facade wall plane. Front numbers measured off the bible through "
                 "aa_bible_cam (scale anchored on the 4.4 m doorway); roof, right corner and right side from the asset "
                 "sheet (crops 12/14). 'opening' = the hole in the stone = the inner edge of the bible's stone surround. "
                 "'frame_bible' = the dark frame's outer edge as the bible draws it, traced on the face plane y=0. "
                 "'frame_at_reveal' = the same outline moved back along aa_bible_cam's rays to the frame's front plane "
                 "(y = reveal_depth): build the frame to frame_at_reveal and the bible camera sees frame_bible exactly. "
                 "Source of truth: tools/content_generation/absinthe_arcade/manifest.json -> facade; this file is "
                 "written by publish_interfaces.py."),
        "version": 2.1,
        "status": "v2 (2026-10-28): building depth 4.0 (Q-011), side elevation, interior volume, jambs, keystone recess, window linings and reveals bible-checked. Stable.",
        "changes_v2": [
            "building: depth 4.0 m; side elevation, roof footprint, side openings and side dormer published (Q-011).",
            "interior: interior_depth / set_depth 3.40 from the door line y=0.34 to y=3.74; back wall inner face y=3.76 (back wall 0.24).",
            "arch: right jamb 2.20 -> 2.37 (bible pier arris 2.375, neon's doorway edge 2.365); left jamb -2.30; ring intrados half 2.30 about X=0 (axis unchanged); right pier 2.37..2.80.",
            "keystone: aa_arch_hero_cartouche removed; no crown voussoir (|x|<0.27); E4's head and volutes sit in front of the archivolt.",
            "windows: openings unchanged from v1.1 except L1 (elliptical head, crown 4.876); frames per glazier (L1 1.06, L3 0.98, frame_bible.x_right added for L3); reveal 0.20 -> 0.08 for every front and side window (bible check); frame_at_reveal added.",
            "dormers: frame, lining and reveal added (glazier); side dormer added.",
            "v2.1: L1 frame re-traced in the bible: 1.005 wide (-3.845..-2.84), not glazier's 1.06 (11 px wide on each side), so its 0.08 reveal fits without clamping; corner bay cornices refitted to the bible (ground 0.18 proud, band 7.65-7.9, mid 9.45-9.7 at 0.25) and cant windows moved between them (8.0-9.25, 9.95-11.2). The wall face, arch and openings are unchanged from v2.0.",
        ],
        "facade": {"plane_y": 0.0, "x_left_corner": F["x_left"], "x_right_seam": F["x_right"],
                   "width": r3(F["x_right"] - F["x_left"]),
                   "note": "x_left_corner = main wall's left arris where it turns into the angled corner bay; x_right_seam = the right corner (outer edge of the right downpipe)."},
        "building": {"depth": depth, "front_wall_t": walls["front_t"], "side_wall_t": walls["side_t"],
                     "back_wall_t": walls["back_t"], "back_face_y": depth, "back_wall_inner_y": r3(back_inner),
                     "footprint_xy": [[F["x_left"], 0.0], [F["x_right"], 0.0], [F["x_right"], depth],
                                      [r3(cb_far[0]), depth], [r3(cb_far[0]), r3(cb_far[1])]],
                     "interior_set_depth": 3.40,
                     "note": "Q-011 (author): about 4.0 m deep, the asset sheet's one-bay right side. Footprint CCW from the front-left arris; the corner bay's cant runs from (x_left, 0) to its far end."},
        "interior": {"interior_depth": 3.40, "set_depth": 3.40, "door_line_y": door_line,
                     "y_back_limit": r3(door_line + 3.40), "back_wall_inner_y": r3(back_inner),
                     "clear_x": [r3(cb_far[0] + walls["side_t"]), r3(F["x_right"] - walls["side_t"])],
                     "passage_x": [-A["half"], A["jamb_r"]], "passage_y": [0.0, walls["front_t"]],
                     "floor_z": A["step"]["z_top"],
                     "placeholder_backstop": {"name": "aa_shell_facade_interior_void", "y": [3.745, 3.75],
                                              "note": "E1's dark backstop; hide or delete it when E3's interior set is integrated"},
                     "note": "Q-011: the interior behind the doors fits within about 3.4 m. Measured from E3's door line (y 0.34) to y 3.74, 0.02 short of the back wall."},
        "storeys": {"ground": {"z0": 0.0, "z1": 5.9}, "first_cat_window": {"z0": 5.9, "z1": 10.0},
                    "second_balcony_window": {"z0": 10.0, "z1": F["eave_cornice_z"][0]},
                    "eave_z": F["eave_cornice_z"][0], "eave_z_provisional": F["eave_cornice_z"][0],
                    "eave_cornice_z": F["eave_cornice_z"],
                    "right_column_ledges": F["storey_lines"]["right"],
                    "note": "Stone ledge lines in the bible's left column (5.9 under the cat-window apron, 10.0 under the balcony slab); the right column sits 0.36-0.47 m lower. Above the eave cornice: the slate mansard (Q-001)."},
        "windows": {k: window(k, w, w.get("reveal", reveal)) for k, w in F["windows"].items()},
        "windows_note": ("Bible check (v2, through aa_bible_cam): the openings match the inner edge of the stone surround "
                         "on L1, L2, L3 and R1 (traced); the frames match glazier's widths. The light band between frame "
                         "and surround is the lining (lining.sides), not a narrower opening, so the openings stay. "
                         "Reveal 0.08: at 0.20 the frames of the left column would sit 37-44 px right and 23-47 px "
                         "lower in the bible camera than the bible draws them (R column up to 62 px lower)."),
        "arch": {
            "axis_x": 0.0, "half_width": A["half"], "jamb_x": [-A["half"], A["jamb_r"]],
            "springing_z": A["springing"], "intrados": f"semi-ellipse about X=0, half {A['half']}, rise {A['rise']}",
            "rise": A["rise"], "crown_z": r3(A["springing"] + A["rise"]),
            "extrados_half_width": A["ext_half"], "extrados_rise": A["ext_rise"],
            "extrados_crown_z": r3(A["springing"] + A["ext_rise"]), "ring_proud": A["ring_proud"],
            "right_springing_shelf": {"x": [A["half"], A["jamb_r"]], "z": A["springing"],
                                      "note": "the right impost/capital covers it"},
            "piers": {"left": F["left_pier"], "right": F["right_pier"]},
            "bible_doorway_assembly_x": [-2.02, 2.37], "doorway_top_z": 2.77,
            "marquee_bible": {"x": [-2.28, 2.36], "bottom_z": 2.77, "top_z": 4.65, "tagline_banner_z": [2.77, 3.09]},
            "keystone_head_bible": {"center_x": 0.0, "bottom_z": 4.6, "top_z": 6.17, "proud": 0.5},
            "keystone": {"cartouche": "removed", "crown_voussoir": "none",
                         "crown_gap_x": [-0.27, 0.27],
                         "note": "The bible shows no cartouche: the carved head (E4, keystone_head_bible) and its volutes sit IN FRONT of the archivolt. E1 removed aa_arch_hero_cartouche and builds no voussoir at the crown; the wall face (with the mural) shows behind the head. E4 no longer needs its recess_keystone_context()."},
            "step": A["step"],
            "note": A["jamb_note"],
        },
        "camera": dict(name=CAMSPEC["name"], location=CAMSPEC["location"],
                       rotation_euler_xyz_deg=CAMSPEC["rotation_euler_xyz_deg"], lens_mm=CAMSPEC["lens_mm"],
                       sensor_width_mm=CAMSPEC["sensor_width_mm"], sensor_fit=CAMSPEC["sensor_fit"],
                       shift=[0, 0], resolution=CAMSPEC["resolution"], render_resolution=CAMSPEC["preview_resolution"],
                       f_px_at_5248=r3(CAMSPEC["lens_mm"] / CAMSPEC["sensor_width_mm"] * 5248), pitch_deg=16.394,
                       yaw_deg=25.161, roll_deg=1.295, eye_height_m=CAMSPEC["location"][2],
                       solve="tools/content_generation/absinthe_arcade/camera_match/"),
        "right_corner": {"facade_end_x": F["x_right"], "right_downpipe_x": F["drainpipes"]["right"]["x"],
                         "pilaster_x": RC["x"], "pilaster_proud": RC["pilaster"]["proud"],
                         "plinth_z_top": RC["plinth"]["z_top"], "capital_z": RC["pilaster"]["capital_z"],
                         "gf_cornice": {"x": F["gf_cornice"]["right"]["x"], "z": F["gf_cornice"]["right"]["z"],
                                        "proud": F["gf_cornice"]["right"]["proud"]},
                         "quoins": {"z": RC["quoins"]["z"], "course": RC["quoins"]["course"],
                                    "front_long_short": [RC["quoins"]["long"], RC["quoins"]["short"]],
                                    "proud": RC["quoins"]["proud"]},
                         "wraps_onto_side": RC["wrap"],
                         "note": "Asset sheet crops 12/14: the facade ends against the right downpipe; pilaster+capital and quoins wrap the corner onto the side elevation."},
        "side_right": {
            "frame": {"face_x": F["x_right"], "u_axis": "world +Y (u=0 the front face, u=4.0 the back corner)",
                      "outward_normal": [1, 0, 0], "u_range": [0.0, depth]},
            "windows": {k: side_window(w, reveal) for k, w in SR["windows"].items()},
            "framed_panel": SR["framed_panel"], "awning_zone": SR["awning"],
            "back_pilaster_u": SR["back_pilaster"]["u"], "front_corner_quoins_u": [0.0, RC["wrap"]],
            "downpipes": {"front_corner": {"x": F["drainpipes"]["right"]["x"], "y": -0.08, "note": "the right downpipe on the corner (E4/E6)"},
                          "back_corner": {"u": SR["back_downpipe"]["u"]}},
            "front_corner_lantern": {"note": "the sheet's side shows the facade's right lantern (aa_prop_wall_lantern, x 2.93, z 3.7) on the front corner: same lantern, no second one (E6)"},
            "flower_boxes": "one per window, on the sill slab (E2)",
            "note": SR["_doc"] + " " + SR["windows_note"],
        },
        "dormers": {},
        "roof": {"eave_cornice_z": F["eave_cornice_z"], "mansard_top_z": RF["mansard_top_z"],
                 "mansard_setback": RF["mansard_setback"], "top_setback": RF["top_setback"],
                 "footprint_xy": "building.footprint_xy", "gable": {"half_width": RF["gable"]["half"],
                 "top_z": RF["gable"]["top_z"], "carved_head_z": RF["gable"]["head_z"]},
                 "chimneys": RF["chimneys"], "cresting": RF["cresting"], "mansard": RF["mansard"],
                 "note": RF["_doc"]},
        "corner_bay": {"arris_x": F["x_left"], "cant_angle_deg": CB["angle_deg"], "cant_width": CB["width"],
                       "cant_far_end_xy": [r3(cb_far[0]), r3(cb_far[1])], "window_w": CB["window_w"],
                       "cornice_z": CB["cornice_z"], "cornices_z_proud": CB["cornices"], "windows_z": CB["windows_z"],
                       "note": CB["v2_note"],
                       "corner_pilaster": {"x": CB["corner_pilaster"]["x"], "capital_z": CB["corner_pilaster"]["capital_z"]},
                       "clocktower_plaza_sign_mount_zone": {"at_arris_x": F["x_left"], "at_arris_z": CB["hanging_sign_zone"]["at_arris_z"],
                                                            "note": "E6 hangs the CLOCKTOWER PLAZA bracket sign here (Q-006: ruled IN), on the Arcade's left corner"},
                       "wall_sign_zone": {"x": CB["sign_zone"]["x"], "z": CB["sign_zone"]["z"], "note": CB["sign_zone"]["note"]}},
    }
    for dm in RF["dormers"]:
        out["dormers"][dm["id"]] = {"center_x": dm["cx"], "opening_width": D["opening_w"], "sill_z": D["sill"],
                                    "head_z": D["head"], "face_y": D["proud_of_wall"], "body_width": D["body_w"],
                                    "ridge_z": D["ridge"], "reveal_depth": 0.06, "body_depth": D["body_depth"],
                                    "frame": {"width": 0.46, "height": 0.83}, "lining": {"sides": 0.05, "head": 0.05}}
    sd = RF["side_dormer"]
    out["dormers"][sd["id"]] = {"face": "side_right", "u_center": sd["u"], "world_center_y": sd["u"],
                                "face_x": r3(F["x_right"] - D["proud_of_wall"]), "opening_width": D["opening_w"],
                                "sill_z": D["sill"], "head_z": D["head"], "body_width": D["body_w"], "ridge_z": D["ridge"],
                                "reveal_depth": 0.06, "frame": {"width": 0.46, "height": 0.83},
                                "lining": {"sides": 0.05, "head": 0.05}, "outward_normal": [1, 0, 0]}
    out["dormers"]["note"] = ("Mansard dormers from the asset sheet (crops 09/14): front pair over the window columns, one on the "
                              "right side. Openings cut through the dormer fronts; frame/lining/reveal per glazier (E2).")
    text = json.dumps(out, indent=1, ensure_ascii=False)
    if "--check" in sys.argv:
        print(text)
        return
    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(OUT)
    print(f"wrote {OUT} v{out['version']}")


if __name__ == "__main__":
    main()
