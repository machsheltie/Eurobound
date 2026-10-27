"""Graybox review renders for the architectural quality pass (Sol brief, item 21/22).

Puts the scene in neutral clay: one gray material override for the whole view
layer, mural and interior hidden, strong low raking sun, no neon. Renders a
three-quarter street view and an entrance close-up, then restores the scene.

Usage: exec in the live session with OUT_DIR set, or
       blender aa_exterior.blend --background --python graybox_review.py -- --out DIR
"""

import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector

SHOTS = {
    # name: (camera location, aim point, lens mm)
    "graybox_threequarter": ((7.5, -13.0, 2.2), (-0.8, 0.0, 8.0), 20.0),
    "graybox_entrance": ((2.6, -6.2, 2.4), (0.0, 0.0, 4.4), 28.0),
}
HIDE = ("aa_decal_mural__01",)
RES = (1100, 1100)


def out_dir():
    if "--" in sys.argv:
        args = sys.argv[sys.argv.index("--") + 1:]
        if "--out" in args:
            return Path(args[args.index("--out") + 1])
    return Path(globals().get("OUT_DIR", "."))


def clay():
    mat = bpy.data.materials.get("aa_review_clay") or bpy.data.materials.new("aa_review_clay")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (0.55, 0.55, 0.54, 1)
    bsdf.inputs["Roughness"].default_value = 0.7
    return mat


def main():
    sc = bpy.context.scene
    vl = bpy.context.view_layer
    saved = {
        "camera": sc.camera, "override": vl.material_override, "res": (
            sc.render.resolution_x, sc.render.resolution_y), "path": sc.render.filepath,
        "hidden": {n: bpy.data.objects[n].hide_render for n in HIDE if n in bpy.data.objects},
    }
    vl.material_override = clay()
    for n in saved["hidden"]:
        bpy.data.objects[n].hide_render = True

    sun_data = bpy.data.lights.get("aa_review_sun") or bpy.data.lights.new("aa_review_sun", "SUN")
    sun_data.energy = 4.5
    sun_data.angle = math.radians(0.6)
    sun = bpy.data.objects.get("aa_review_sun") or bpy.data.objects.new("aa_review_sun", sun_data)
    if sun.name not in sc.collection.objects:
        sc.collection.objects.link(sun)
    # Low and from the side so every projection throws a long shadow across the wall.
    sun.rotation_euler = (math.radians(62), 0, math.radians(-58))
    others = [o for o in sc.objects if o.type == "LIGHT" and o is not sun and not o.hide_render]
    for o in others:
        o.hide_render = True

    cam_data = bpy.data.cameras.get("aa_review_cam") or bpy.data.cameras.new("aa_review_cam")
    cam = bpy.data.objects.get("aa_review_cam") or bpy.data.objects.new("aa_review_cam", cam_data)
    if cam.name not in sc.collection.objects:
        sc.collection.objects.link(cam)
    sc.camera = cam
    sc.render.resolution_x, sc.render.resolution_y = RES
    written = []
    try:
        for name, (loc, aim, lens) in SHOTS.items():
            cam.location = loc
            cam.rotation_euler = (Vector(aim) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()
            cam_data.lens = lens
            sc.render.filepath = str(out_dir() / f"{name}.png")
            bpy.ops.render.render(write_still=True)
            written.append(sc.render.filepath)
    finally:
        vl.material_override = saved["override"]
        for n, h in saved["hidden"].items():
            bpy.data.objects[n].hide_render = h
        for o in others:
            o.hide_render = False
        sun.hide_render = True
        sc.camera = saved["camera"]
        sc.render.resolution_x, sc.render.resolution_y = saved["res"]
        sc.render.filepath = saved["path"]
    return {"written": written}


if __name__ == "__main__" or "OUT_DIR" in globals():
    result = main()
    print(result)
