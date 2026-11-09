"""Create or update aa_bible_cam from manifest.json -> bible_camera. Safe to re-run.

The camera reproduces the daytime bible's perspective (see camera_match/README.md for the
solve). Every E1-E6 comparison against the bible renders from this camera.

Usage: exec in the live session, or blender aa_exterior.blend --python bible_camera.py
"""

import math
import sys
from pathlib import Path

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402


def main(set_scene_camera=False):
    spec = aa.load_manifest()["bible_camera"]
    name = spec["name"]
    data = bpy.data.cameras.get(name) or bpy.data.cameras.new(name)
    data.lens = spec["lens_mm"]
    data.sensor_width = spec["sensor_width_mm"]
    data.sensor_fit = spec["sensor_fit"]
    data.shift_x = data.shift_y = 0.0
    data.clip_start, data.clip_end = 0.1, 200.0
    cam = bpy.data.objects.get(name) or bpy.data.objects.new(name, data)
    cam.data = data
    if cam.name not in bpy.context.scene.collection.objects:
        bpy.context.scene.collection.objects.link(cam)
    cam.location = spec["location"]
    cam.rotation_mode = "XYZ"
    cam.rotation_euler = [math.radians(a) for a in spec["rotation_euler_xyz_deg"]]
    if set_scene_camera:
        sc = bpy.context.scene
        sc.camera = cam
        sc.render.resolution_x, sc.render.resolution_y = spec["preview_resolution"]
        sc.render.pixel_aspect_x = sc.render.pixel_aspect_y = 1.0
    return {"camera": cam.name, "lens": data.lens, "location": list(cam.location)}


if __name__ == "__main__" or "AA_RUN" in globals():
    print(main())
