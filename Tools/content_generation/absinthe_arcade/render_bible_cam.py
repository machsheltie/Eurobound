"""Render aa_exterior.blend from aa_bible_cam in a background Blender (E1 comparisons).

  blender -b aa_exterior.blend --python render_bible_cam.py -- --out shot.png
          [--clay] [--engine eevee|workbench] [--res 1600 1462] [--samples 32] [--hide NAME ...]

--clay   one neutral gray override, mural hidden, a low raking sun (graybox review look).
default  the scene's own materials under a soft, warm overcast daylight like the bible's
         (physical sky with the sun disc off, a weak warm sun, a cool fill from the sky).
Nothing is saved; the .blend on disk is untouched.
"""

import argparse
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bible_camera  # noqa: E402

CLAY_HIDE = ("aa_decal_mural__01",)


def daylight(sc):
    """Soft overcast, slightly warm: the bible is lit by a bright cloudy sky."""
    world = bpy.data.worlds.new("aa_bible_overcast")
    world.use_nodes = True
    nt = world.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputWorld")
    bg = nt.nodes.new("ShaderNodeBackground")
    bg.inputs["Color"].default_value = (0.80, 0.79, 0.78, 1)     # bright, faintly warm overcast sky
    bg.inputs["Strength"].default_value = 0.62    # overcast dusk-ish: lets the lamps and neon read
    nt.links.new(bg.outputs["Background"], out.inputs["Surface"])
    sc.world = world
    for o in sc.objects:
        if o.type == "LIGHT":
            o.hide_render = True
    sun = bpy.data.objects.new("aa_bible_sun", bpy.data.lights.new("aa_bible_sun", "SUN"))
    sun.data.energy = 0.8
    sun.data.angle = math.radians(25)            # very soft: overcast, no hard shadow edges
    sun.data.color = (1.0, 0.87, 0.72)           # warm
    sun.rotation_euler = (math.radians(50), 0, math.radians(35))
    sc.collection.objects.link(sun)


def practicals(sc):
    """The bible's warm lamp light: point lights in the lanterns, the clocktower sign lamp and the
    awning's string bulbs, a warm glow from the hall, and faint green/purple spill from the
    marquee neon, so the wet cobbles catch warm and neon streaks. Render-only (not assets)."""
    def light(name, loc, watts, color, radius=0.06, kind="POINT"):
        ld = bpy.data.lights.new(name, kind)
        ld.energy, ld.color = watts, color
        if kind == "POINT":
            ld.shadow_soft_size = radius
        else:
            ld.size = radius
        ob = bpy.data.objects.new(name, ld)
        ob.location = loc
        sc.collection.objects.link(ob)
        return ob

    def centre(n):
        o = bpy.data.objects.get(n)
        if o is None:
            return None
        cs = [o.matrix_world @ Vector(c) for c in o.bound_box]
        return Vector([sum(c[i] for c in cs) / 8 for i in range(3)])
    warm = (1.0, 0.68, 0.38)
    n = 0
    for name, w in (("aa_e6_wall_lantern_l", 140), ("aa_e6_wall_lantern_r", 140),
                    ("aa_e6_clocktower_lantern_glass_glow", 45)):
        c = centre(name)
        if c is not None:
            light(f"aa_rl_{name}", c, w, warm)
            n += 1
    o = bpy.data.objects.get("aa_e6_awning_string_bulbs")
    if o is not None:
        cs = [o.matrix_world @ Vector(c) for c in o.bound_box]
        x0, x1 = min(c.x for c in cs), max(c.x for c in cs)
        y, z = sum(c.y for c in cs) / 8, min(c.z for c in cs)
        for k in range(5):
            light(f"aa_rl_string_{k}", (x0 + (x1 - x0) * (k + 0.5) / 5, y, z), 14, warm, 0.03)
            n += 1
    if bpy.data.collections.get("aa_e3_interior_set"):
        a = light("aa_rl_hall", (0.1, 1.2, 2.4), 420, (1.0, 0.62, 0.32), 1.6, "AREA")
        a.rotation_euler = (math.radians(70), 0, 0)
        n += 1
    if bpy.data.collections.get("aa_e3_marquee"):
        light("aa_rl_neon_green", (-0.8, -0.9, 3.9), 70, (0.55, 1.0, 0.25), 0.8)
        light("aa_rl_neon_purple", (0.9, -0.9, 3.4), 70, (0.75, 0.35, 1.0), 0.8)
        n += 2
    return n


def clay(sc):
    mat = bpy.data.materials.new("aa_e1_clay")
    mat.use_nodes = True
    b = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = (0.55, 0.55, 0.54, 1)
    b.inputs["Roughness"].default_value = 0.7
    bpy.context.view_layer.material_override = mat
    for n in CLAY_HIDE:
        o = bpy.data.objects.get(n)
        if o:
            o.hide_render = True
    for o in sc.objects:
        if o.type == "LIGHT":
            o.hide_render = True
    sun = bpy.data.objects.new("aa_e1_sun", bpy.data.lights.new("aa_e1_sun", "SUN"))
    sun.data.energy = 2.6
    sun.data.angle = math.radians(1.5)
    sun.rotation_euler = (math.radians(58), 0, math.radians(40))   # raking from the upper right
    sc.collection.objects.link(sun)
    world = bpy.data.worlds.new("aa_e1_clay_world")
    world.use_nodes = True
    bg = next(n for n in world.node_tree.nodes if n.type == "BACKGROUND")
    bg.inputs["Color"].default_value = (0.6, 0.65, 0.72, 1)
    bg.inputs["Strength"].default_value = 0.35
    sc.world = world


def ground_plane(sc):
    """Render-only street: a flat dark plane at z=0 so the building has contact shadows and
    the bible's dark wet ground tone (the cobbles belong to E6)."""
    import bmesh
    me = bpy.data.meshes.new("aa_e1_ground")
    bm = bmesh.new()
    bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=40.0)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new("aa_e1_ground", me)
    ob.location = (0.0, -10.0, -0.002)
    mat = bpy.data.materials.new("aa_e1_ground")
    b = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    b.inputs["Base Color"].default_value = (0.05, 0.05, 0.055, 1)
    b.inputs["Roughness"].default_value = 0.35
    me.materials.append(mat)
    sc.collection.objects.link(ob)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--clay", action="store_true")
    ap.add_argument("--engine", default="eevee")
    ap.add_argument("--res", type=int, nargs=2, default=(1600, 1462))
    ap.add_argument("--samples", type=int, default=32)
    ap.add_argument("--hide", nargs="*", default=[])
    ap.add_argument("--loc", type=float, nargs=3, help="override: a free camera at this point (review shots)")
    ap.add_argument("--aim", type=float, nargs=3)
    ap.add_argument("--lens", type=float, default=28.0)
    ap.add_argument("--ortho", type=float, help="with --loc/--aim: orthographic, this many metres wide")
    args = ap.parse_args(sys.argv[sys.argv.index("--") + 1:])
    sc = bpy.context.scene
    bible_camera.main()
    sc.camera = bpy.data.objects["aa_bible_cam"]
    if args.loc:
        from mathutils import Vector
        cd = bpy.data.cameras.new("aa_e1_review")
        cd.lens = args.lens
        cam = bpy.data.objects.new("aa_e1_review", cd)
        sc.collection.objects.link(cam)
        cam.location = args.loc
        cam.rotation_euler = (Vector(args.aim) - Vector(args.loc)).to_track_quat("-Z", "Y").to_euler()
        if args.ortho:
            cd.type = "ORTHO"
            cd.ortho_scale = args.ortho
            cd.sensor_fit = "HORIZONTAL"           # --ortho is the frame WIDTH, also for tall frames
        cd.clip_end = 300.0
        sc.camera = cam
    sc.render.resolution_x, sc.render.resolution_y = args.res
    sc.render.resolution_percentage = 100
    sc.render.pixel_aspect_x = sc.render.pixel_aspect_y = 1.0
    for n in args.hide:
        o = bpy.data.objects.get(n)
        if o:
            o.hide_render = True
    if bpy.data.objects.get("aa_e6_ground_bed") is None:     # E6 brings the street
        ground_plane(sc)
    if args.engine == "workbench":
        sc.render.engine = "BLENDER_WORKBENCH"
        sh = sc.display.shading
        sh.light = "STUDIO"
        sh.color_type = "MATERIAL" if not args.clay else "SINGLE"
        sh.single_color = (0.6, 0.6, 0.58)
        sh.show_cavity = True
        sh.show_shadows = True
    else:
        sc.render.engine = "BLENDER_EEVEE"
        sc.eevee.taa_render_samples = args.samples
        sc.eevee.use_raytracing = True
        try:
            sc.eevee.shadow_pool_size = "1024"    # many practical lights
            sc.eevee.shadow_resolution_scale = 0.8
        except (TypeError, AttributeError):
            pass
        if args.clay:
            clay(sc)
        else:
            daylight(sc)
            practicals(sc)
    sc.view_settings.view_transform = "AgX"
    if not args.clay:
        try:
            sc.view_settings.look = "AgX - Medium High Contrast"
        except TypeError:
            pass
    sc.render.filepath = str(resolve_out(args.out))
    bpy.ops.render.render(write_still=True)
    print("@@JSON@@{\"out\": \"%s\"}" % sc.render.filepath.replace("\\", "/"))


REPO = Path(__file__).resolve().parents[3]


def resolve_out(out):
    """Relative or drive-less paths ("dev/aa_team/...", "/dev/aa_team/...") resolve against the
    repo, never the process's drive root (the 2026-10-28 renders landed in C:/dev by mistake)."""
    p = Path(out)
    if not p.drive:
        p = REPO / str(out).lstrip("/\\")
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


main()
