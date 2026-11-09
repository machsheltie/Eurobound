"""Headless E1 rebuild: aa_bible_cam + build_shell.py on aa_exterior.blend, saved to a temp copy.

  blender -b aa_exterior.blend --python-exit-code 1 --python rebuild_shell_headless.py -- \
          --save <tmp.blend> [--report <out.json>]

Saves with copy=True to --save; the caller swaps it over aa_exterior.blend once Blender has exited
(atomic for the agents that read the main file through bpy.data.libraries.load). Prints and
optionally writes a JSON report: what build_shell made plus probe raycasts on the v2 openings.
"""

import argparse
import json
import sys
from pathlib import Path

import bpy
from mathutils import Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bible_camera  # noqa: E402
import build_shell  # noqa: E402


def ray(o, d):
    sc = bpy.context.scene
    dg = bpy.context.evaluated_depsgraph_get()
    hit, loc, _n, _i, ob, _m = sc.ray_cast(dg, Vector(o), Vector(d).normalized(), distance=60)
    return [ob.name, [round(v, 3) for v in loc]] if hit else None


def probes():
    """Raycasts that pin the v2 interface: jambs, keystone gap, window holes, side holes, depth."""
    return {
        "jamb_left_z2_x-2.32": ray((-2.32, -3, 2.0), (0, 1, 0)),
        "jamb_left_z2_x-2.28": ray((-2.28, -3, 2.0), (0, 1, 0)),
        "jamb_right_z2_x2.35": ray((2.35, -3, 2.0), (0, 1, 0)),
        "jamb_right_z2_x2.39": ray((2.39, -3, 2.0), (0, 1, 0)),
        "keystone_gap_x0_z5.0_behind_head": ray((0.0, -0.05, 5.0), (0, 1, 0)),
        "L2_hole_x-3.95": ray((-3.95, -3, 7.5), (0, 1, 0)),
        "L2_stone_x-4.0": ray((-4.0, -3, 7.5), (0, 1, 0)),
        "R1_hole_x1.66": ray((1.66, -3, 7.5), (0, 1, 0)),
        "side_w1_hole_y1.45": ray((8, 1.45, 7.5), (-1, 0, 0)),
        "side_w1_stone_y1.40": ray((8, 1.40, 7.5), (-1, 0, 0)),
        "back_wall_inner_from_front": ray((-1.0, 1.0, 1.0), (0, 1, 0)),
        "back_face_from_behind": ray((-1.0, 9.0, 8.0), (0, -1, 0)),
    }


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    ap = argparse.ArgumentParser()
    ap.add_argument("--save", required=True)
    ap.add_argument("--report")
    a = ap.parse_args(argv)
    cam = bible_camera.main()
    made = build_shell.main()
    bpy.context.view_layer.update()
    rep = {"camera": cam, "made": made, "probes": probes(),
           "shell": {o.name: dict(polys=len(o.data.polygons), dims=[round(v, 3) for v in o.dimensions])
                     for o in bpy.data.collections["aa_shell_facade"].objects if o.type == "MESH"}}
    bpy.ops.wm.save_as_mainfile(filepath=a.save, copy=True)
    rep["saved"] = a.save
    text = json.dumps(rep, indent=1, default=str)
    if a.report:
        Path(a.report).write_text(text, encoding="utf-8")
    print("@@JSON@@" + json.dumps({"saved": a.save, "made": made}, default=str))


main()
