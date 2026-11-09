"""Render E4 views through aa_bible_cam, windowed on bible-pixel regions, plus side-by-side compares.

  blender -b <file.blend> --factory-startup --python e4_render.py -- --view crop05|head|box_left|box_right|plaque
          [--clay] [--long 1800] [--samples 48] [--out path.png]

The camera keeps aa_bible_cam's pose and focal length; lens + shift crop it to the window, so every
render is pixel-registered with the same window cut from the full-res bible.
"""
import argparse
import math
import sys
from pathlib import Path

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
from e4_cam import BibleCam, crop05_window  # noqa: E402

OUT_DIR = Path(__file__).resolve().parents[5] / "dev/aa_team/renders/E4"


def views():
    return {
        "crop05": crop05_window(),
        "head": (2960, 1470, 3740, 2230),
        "box_left": (1440, 2240, 1820, 2620),
        "box_right": (4380, 1700, 4740, 2000),
        "plaque": (4590, 3095, 4760, 3275),
    }


def setup_camera(cm, win, long_side):
    x0, y0, x1, y1 = win
    w, h = x1 - x0, y1 - y0
    sc = bpy.context.scene
    k = long_side / max(w, h)
    sc.render.resolution_x, sc.render.resolution_y = round(w * k), round(h * k)
    sc.render.resolution_percentage = 100
    data = bpy.data.cameras.get("aa_bible_cam_e4") or bpy.data.cameras.new("aa_bible_cam_e4")
    data.sensor_fit = "HORIZONTAL"
    data.sensor_width = 36.0
    data.lens = 36.0 * cm.f / w
    data.shift_x = ((x0 + w / 2) - cm.cx) / w
    data.shift_y = -((y0 + h / 2) - cm.cy) / w
    data.clip_start, data.clip_end = 0.1, 200
    cam = bpy.data.objects.get("aa_bible_cam_e4") or bpy.data.objects.new("aa_bible_cam_e4", data)
    if cam.name not in sc.collection.objects:
        sc.collection.objects.link(cam)
    cam.location = cm.spec["location"]
    cam.rotation_mode = "XYZ"
    cam.rotation_euler = [math.radians(a) for a in cm.spec["rotation_euler_xyz_deg"]]
    sc.camera = cam
    bpy.context.view_layer.update()
    p = Vector((0.6, 0.0, 5.0))
    u, v = cm.project(p)
    ndc = world_to_camera_view(sc, cam, p)
    return {"lens": round(data.lens, 3), "res": (sc.render.resolution_x, sc.render.resolution_y),
            "registration_px": (round(x0 + ndc.x * w - u, 2), round(y0 + (1 - ndc.y) * h - v, 2))}


def setup_light(clay):
    sc = bpy.context.scene
    world = bpy.data.worlds.get("e4_day") or bpy.data.worlds.new("e4_day")
    nt = world.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputWorld")
    sky = nt.nodes.new("ShaderNodeTexSky")
    try:
        sky.sky_type = "MULTIPLE_SCATTERING"
    except TypeError:
        pass
    if hasattr(sky, "sun_disc"):
        sky.sun_disc = False
    sky.sun_elevation = math.radians(35)
    sky.sun_rotation = math.radians(200)
    bg = nt.nodes.new("ShaderNodeBackground")
    bg.inputs["Strength"].default_value = 0.12
    nt.links.new(sky.outputs["Color"], bg.inputs["Color"])
    nt.links.new(bg.outputs["Background"], out.inputs["Surface"])
    sc.world = world
    for o in [o for o in sc.objects if o.type == "LIGHT"]:
        bpy.data.objects.remove(o)

    def light(name, kind, energy, loc, rot=None, color=(1, 1, 1), size=None):
        ld = bpy.data.lights.new(name, kind)
        ld.energy = energy
        ld.color = color
        if size is not None:
            if kind == "SUN":
                ld.angle = size
            else:
                ld.shadow_soft_size = size
        ob = bpy.data.objects.new(name, ld)
        sc.collection.objects.link(ob)
        ob.location = loc
        if rot:
            ob.rotation_euler = rot
        return ob
    light("e4_sun", "SUN", 1.1 if not clay else 3.0, (0, -5, 10), (math.radians(55), 0, math.radians(-30)),
          (1.0, 0.92, 0.80), math.radians(8))
    a = light("e4_fill", "AREA", 340, (1.5, -6.5, 4.5), (math.radians(80), 0, math.radians(10)), (1.0, 0.95, 0.88))
    a.data.size = 8.0
    a.data.specular_factor = 0.2
    s = light("e4_skyfill", "AREA", 220, (0.5, -4.0, 11.0), (math.radians(20), 0, 0), (0.85, 0.9, 1.0))
    s.data.size = 10.0
    s.data.specular_factor = 0.1


def setup_render(samples, clay):
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_EEVEE"
    sc.eevee.taa_render_samples = samples
    sc.eevee.use_raytracing = True
    sc.view_settings.view_transform = "Standard"
    sc.view_settings.look = "None"
    sc.render.film_transparent = False
    if clay:
        m = bpy.data.materials.get("e4_clay") or bpy.data.materials.new("e4_clay")
        b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
        b.inputs["Base Color"].default_value = (0.55, 0.55, 0.54, 1)
        b.inputs["Roughness"].default_value = 0.7
        bpy.context.view_layer.material_override = m
        for cn in ("e4_context_mason",):
            c = bpy.data.collections.get(cn)
            if c:
                for o in c.objects:
                    if o.name == "aa_decal_mural":
                        o.hide_render = True
        return
    try:
        ng = bpy.data.node_groups.new("e4_comp", "CompositorNodeTree")
        sc.compositing_node_group = ng
        rl = ng.nodes.new("CompositorNodeRLayers")
        gl = ng.nodes.new("CompositorNodeGlare")
        out = ng.nodes.new("NodeGroupOutput")
        ng.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
        gl.inputs["Type"].default_value = "Bloom" if gl.inputs["Type"].type == "MENU" else gl.inputs["Type"].default_value
        for nm, val in (("Threshold", 1.0), ("Strength", 0.3), ("Size", 0.35)):
            gl.inputs[nm].default_value = val
        ng.links.new(rl.outputs["Image"], gl.inputs["Image"])
        ng.links.new(gl.outputs["Image"], out.inputs[0])
    except Exception as e:  # noqa: BLE001
        print("E4 GLOW skipped", e)


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    ap = argparse.ArgumentParser()
    ap.add_argument("--view", default="crop05")
    ap.add_argument("--clay", action="store_true")
    ap.add_argument("--long", type=int, default=1800)
    ap.add_argument("--samples", type=int, default=48)
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    cm = BibleCam()
    info = setup_camera(cm, views()[a.view], a.long)
    setup_light(a.clay)
    setup_render(a.samples, a.clay)
    out = Path(a.out) if a.out else OUT_DIR / f"final_{a.view}{'_clay' if a.clay else ''}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    bpy.context.scene.render.filepath = str(out)
    print("E4 RENDER", a.view, info, "->", out)
    bpy.ops.render.render(write_still=True)


main()
