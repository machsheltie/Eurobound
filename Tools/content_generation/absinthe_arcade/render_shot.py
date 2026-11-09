"""Render one shot of aa_exterior.blend in a separate background Blender process.

The live session has crashed mid-render twice on this heavy scene; rendering
out of process keeps a crash from taking the working session with it.

Usage:
  blender -b aa_exterior.blend --python render_shot.py -- \
      --out shot.png --loc X Y Z --aim X Y Z [--lens 35] [--res 900 900] [--samples 16] [--clay]
"""

import argparse
import math
import sys

import bpy
from mathutils import Vector


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--loc", type=float, nargs=3, required=True)
    ap.add_argument("--aim", type=float, nargs=3, required=True)
    ap.add_argument("--lens", type=float, default=35.0)
    ap.add_argument("--res", type=int, nargs=2, default=(900, 900))
    ap.add_argument("--samples", type=int, default=16)
    ap.add_argument("--clay", action="store_true", help="neutral gray override, mural off, raking sun")
    args = ap.parse_args(sys.argv[sys.argv.index("--") + 1:])

    sc = bpy.context.scene
    cam_data = bpy.data.cameras.new("aa_shot_cam")
    cam_data.lens = args.lens
    cam = bpy.data.objects.new("aa_shot_cam", cam_data)
    sc.collection.objects.link(cam)
    cam.location = args.loc
    cam.rotation_euler = (Vector(args.aim) - Vector(args.loc)).to_track_quat("-Z", "Y").to_euler()
    sc.camera = cam
    sc.render.resolution_x, sc.render.resolution_y = args.res
    sc.render.resolution_percentage = 100
    sc.eevee.taa_render_samples = args.samples
    sc.eevee.use_raytracing = True     # screen-space reflections: glass needs them to read
    if args.clay:
        mat = bpy.data.materials.new("aa_shot_clay")
        mat.use_nodes = True
        b = mat.node_tree.nodes["Principled BSDF"]
        b.inputs["Base Color"].default_value = (0.55, 0.55, 0.54, 1)
        b.inputs["Roughness"].default_value = 0.7
        bpy.context.view_layer.material_override = mat
        mural = bpy.data.objects.get("aa_decal_mural__01")
        if mural:
            mural.hide_render = True
        for o in sc.objects:
            if o.type == "LIGHT":
                o.hide_render = True
        sun = bpy.data.objects.new("aa_shot_sun", bpy.data.lights.new("aa_shot_sun", "SUN"))
        sun.data.energy = 4.5
        sun.data.angle = math.radians(0.6)
        sun.rotation_euler = (math.radians(62), 0, math.radians(-58))
        sc.collection.objects.link(sun)
    sc.render.filepath = args.out
    bpy.ops.render.render(write_still=True)


main()
