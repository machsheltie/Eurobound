"""Render E3 views through aa_bible_cam (interfaces.json), windowed onto crop 04 regions.

  blender -b wip/E3_entrance.blend --factory-startup --python e3_render.py -- --view straight [--clay]
          [--long 1800] [--out path.png] [--samples 32]

A view is a window of crop-04 pixels; the camera keeps aa_bible_cam's pose and focal length and
uses lens + shift so the render is pixel-registered with the crop window (checked by projecting
a point through both the Blender camera and the pure-Python model).
"""
import argparse
import math
import sys
from pathlib import Path

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
from e3_bible_cam import CROP04_OFFSET, BibleCam  # noqa: E402
import e3_layout as L  # noqa: E402

VIEWS = {   # crop-04 pixel windows (x0, y0, x1, y1)
    "straight": (0, 0, 2296, 2329),
    "lettering": (300, 60, 2240, 800),
    "doorway": (120, 820, 2296, 2329),
}
OUT_DIR = Path(__file__).resolve().parents[5] / "dev/aa_team/renders/E3"


def setup_camera(cam_model, win, long_side):
    x0, y0, x1, y1 = win
    w, h = x1 - x0, y1 - y0
    sc = bpy.context.scene
    k = long_side / max(w, h)
    sc.render.resolution_x, sc.render.resolution_y = round(w * k), round(h * k)
    sc.render.resolution_percentage = 100
    spec = cam_model.spec
    data = bpy.data.cameras.get("aa_bible_cam") or bpy.data.cameras.new("aa_bible_cam")
    data.sensor_fit = "HORIZONTAL"
    data.sensor_width = 36.0
    data.lens = 36.0 * cam_model.f / w
    cx = x0 + w / 2 + CROP04_OFFSET[0]
    cy = y0 + h / 2 + CROP04_OFFSET[1]
    data.shift_x = (cx - cam_model.cx) / w          # HORIZONTAL fit: shift is in sensor-width units
    data.shift_y = -(cy - cam_model.cy) / w
    data.clip_start, data.clip_end = 0.1, 200
    cam = bpy.data.objects.get("aa_bible_cam") or bpy.data.objects.new("aa_bible_cam", data)
    if cam.name not in sc.collection.objects:
        sc.collection.objects.link(cam)
    cam.location = spec["location"]
    cam.rotation_mode = "XYZ"
    cam.rotation_euler = [math.radians(a) for a in spec["rotation_euler_xyz_deg"]]
    sc.camera = cam
    bpy.context.view_layer.update()
    # registration check: a point on the doorway head
    p = Vector((0.5, 0.0, 2.8))
    u, v = cam_model.world_to_crop(p)
    ndc = world_to_camera_view(sc, cam, p)
    ru = x0 + ndc.x * w
    rv = y0 + (1 - ndc.y) * h
    return {"lens": data.lens, "shift": (data.shift_x, data.shift_y), "res": (sc.render.resolution_x,
            sc.render.resolution_y), "registration_px": (round(ru - u, 2), round(rv - v, 2))}


def setup_world_and_lights(clay):
    sc = bpy.context.scene
    world = bpy.data.worlds.get("e3_day") or bpy.data.worlds.new("e3_day")
    world.use_nodes = True
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
    bg.inputs["Strength"].default_value = 0.035     # low: EEVEE does not occlude world light inside the closed hall
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

    # soft, warm overcast key from the upper left/front, low contrast
    light("e3_sun", "SUN", 1.1 if not clay else 3.0, (0, -5, 10),
          (math.radians(55), 0, math.radians(-30)), (1.0, 0.92, 0.80), math.radians(8))
    # big street-side fill (sky bounce off the square)
    a = light("e3_fill", "AREA", 340, (1.5, -6.5, 2.5), (math.radians(80), 0, math.radians(10)), (1.0, 0.95, 0.88))
    a.data.size = 8.0
    a.data.specular_factor = 0.15          # keep the fill off the black iron's gloss (crop: soft highlights)
    outside = bpy.data.collections.get("e3_outside_lit") or bpy.data.collections.new("e3_outside_lit")
    for cn in ("aa_e3_marquee", "aa_e3_doorway"):
        c = bpy.data.collections.get(cn)
        if c and c.name not in [x.name for x in outside.children]:
            outside.children.link(c)
    for o in bpy.data.collections["e3_context"].objects:        # the hall's haze stays out of the daylight
        if o.name != "e3_ctx_interior_haze" and o.name not in outside.objects:
            outside.objects.link(o)
    fl = bpy.data.objects.get("aa_e3_int_floor")          # daylight spills onto the checkerboard (crop)
    if fl and fl.name not in outside.objects:
        outside.objects.link(fl)
    sky = light("e3_skyfill", "AREA", 220, (0.5, -4.0, 9.0), (math.radians(20), 0, 0), (0.85, 0.9, 1.0))
    sky.data.size = 10.0
    sky.data.specular_factor = 0.1
    for lo in (a, sky, bpy.data.objects.get("e3_sun")):
        if lo is not None:
            lo.light_linking.receiver_collection = outside
    if not clay:
        # interior practicals (placed in the uncompressed hall, then pushed through the same
        # forced-perspective map as the set)
        # warm pendant practicals at each bulb (the hall's only light, as in the bible)
        bulbs = [o for o in bpy.data.objects if o.name.startswith("aa_e3_int_lamp_") and o.name.endswith("_bulb")]
        for k, b in enumerate(bulbs):
            vs = [b.matrix_world @ v.co for v in b.data.vertices]
            c = sum(vs, Vector()) / len(vs)
            lt = light(f"e3_int_lamp_{k}", "SPOT", 40, tuple(c - Vector((0, 0, 0.01))), color=(1.0, 0.6, 0.28),
                       size=0.03)
            lt.data.spot_size = math.radians(115)
            lt.data.spot_blend = 0.6
            lt.data.volume_factor = 1.0
            glow_pt = light(f"e3_int_lamp_{k}_glow", "POINT", 2.0, tuple(c), color=(1.0, 0.6, 0.28), size=0.03)
        rear = light("e3_int_rear", "POINT", 3, L.compress((-0.6, 7.2, 1.9)), color=(1.0, 0.45, 0.18), size=0.5)
        rear.data.volume_factor = 2.0                     # glow behind the silhouettes
        light("e3_int_cab", "POINT", 10, L.compress((-1.0, 1.4, 1.5)), color=(0.35, 0.5, 1.0), size=0.2)
        light("e3_int_game", "POINT", 15, L.compress((-1.55, 7.3, 2.1)), color=(1.0, 0.3, 0.08), size=0.2)


def setup_render(samples, clay):
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_EEVEE"
    sc.eevee.taa_render_samples = samples
    sc.eevee.use_raytracing = True
    try:
        sc.eevee.use_shadows = True
    except AttributeError:
        pass
    sc.view_settings.view_transform = "Standard"
    try:
        sc.view_settings.look = "None"
    except TypeError:
        pass
    sc.view_settings.exposure = 0.0
    sc.render.film_transparent = False
    try:
        sc.eevee.volumetric_tile_size = "4"
        sc.eevee.volumetric_samples = 96
        sc.eevee.volumetric_end = 30.0
    except (AttributeError, TypeError):
        pass
    if not clay:
        setup_glow(sc)
    else:
        h = bpy.data.objects.get("e3_ctx_interior_haze")
        if h:
            h.hide_render = True
    if clay:
        m = bpy.data.materials.get("e3_clay") or bpy.data.materials.new("e3_clay")
        m.use_nodes = True
        b = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
        b.inputs["Base Color"].default_value = (0.55, 0.55, 0.54, 1)
        b.inputs["Roughness"].default_value = 0.7
        bpy.context.view_layer.material_override = m


def setup_glow(sc):
    """Compositor bloom so neon and lit glass glow the way the bible's do."""
    try:
        ng = bpy.data.node_groups.new("e3_comp", "CompositorNodeTree")
        sc.compositing_node_group = ng
        rl = ng.nodes.new("CompositorNodeRLayers")
        gl = ng.nodes.new("CompositorNodeGlare")
        out = ng.nodes.new("NodeGroupOutput")
        ng.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
        for prop, val in (("glare_type", "BLOOM"), ("quality", "HIGH")):
            try:
                setattr(gl, prop, val)
            except (AttributeError, TypeError):
                pass
        for nm, val in (("Threshold", 1.0), ("Strength", 0.3), ("Size", 0.35), ("Smoothness", 0.2)):
            if nm in gl.inputs:
                gl.inputs[nm].default_value = val
        ng.links.new(rl.outputs["Image"], gl.inputs["Image"])
        ng.links.new(gl.outputs["Image"], out.inputs[0])
        sc.render.use_compositing = True
        print("E3 GLOW ok", [i.name for i in gl.inputs])
    except Exception as e:  # compositor API drift: render without bloom rather than fail
        print("E3 GLOW skipped", e)


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    ap = argparse.ArgumentParser()
    ap.add_argument("--view", default="straight")
    ap.add_argument("--clay", action="store_true")
    ap.add_argument("--long", type=int, default=1800)
    ap.add_argument("--samples", type=int, default=32)
    ap.add_argument("--out")
    ap.add_argument("--no-context", action="store_true")
    a = ap.parse_args(argv)
    cam = BibleCam()
    info = setup_camera(cam, VIEWS[a.view], a.long)
    setup_world_and_lights(a.clay)
    setup_render(a.samples, a.clay)
    if a.no_context:
        c = bpy.data.collections.get("e3_context")
        if c:
            for o in c.objects:
                o.hide_render = True
    out = Path(a.out) if a.out else OUT_DIR / f"final_{a.view}{'_clay' if a.clay else ''}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    bpy.context.scene.render.filepath = str(out)
    print("E3 RENDER", a.view, info, "->", out)
    bpy.ops.render.render(write_still=True)


main()
