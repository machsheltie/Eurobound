"""Shared Eurobound 3D look: toon ramp material, warm upper-left key + cool fill, transparent EEVEE render.

Import from any headless Blender script (characters: tools/char3d/pose_render.py; items: tools/item3d/):
    import sys; sys.path.insert(0, "tools/char3d"); import look
    mat = look.toon_material("name", img=bpy_image)   # or base=(r, g, b, 1)
    look.lights(scene)
    look.render(scene, "out.png")
Defaults match the approved Jakub trial (author, 2026-11-12). Pass a cfg dict to override ramp/light values.
"""
import math
import bpy
from mathutils import Vector

RAMP = ((0.50, 0.42, 0.45), (0.80, 0.74, 0.70), (1.0, 0.95, 0.86))   # shadow (cool), mid, warm lit
RAMP_POS = (0.0, 0.30, 0.62)
KEY = {"dir": (1.0, 0.8, -1.0), "energy": 3.4, "color": (1.0, 0.86, 0.66)}     # warm, from upper left
FILL = {"dir": (-0.8, 1.0, -0.3), "energy": 1.0, "color": (0.75, 0.82, 1.0)}   # soft cool fill


def toon_material(name, base=None, img=None, cfg=None):
    cfg = cfg or {}
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    dif = nt.nodes.new("ShaderNodeBsdfDiffuse")
    dif.inputs["Color"].default_value = (1, 1, 1, 1)
    s2r = nt.nodes.new("ShaderNodeShaderToRGB")
    bw = nt.nodes.new("ShaderNodeRGBToBW")
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.interpolation = "CONSTANT"
    cr = ramp.color_ramp
    cols = [tuple(cfg.get(f"ramp{i}", RAMP[i])) for i in range(3)]
    cr.elements[0].position, cr.elements[0].color = RAMP_POS[0], cols[0] + (1,)
    cr.elements[1].position, cr.elements[1].color = RAMP_POS[1], cols[1] + (1,)
    e = cr.elements.new(RAMP_POS[2])
    e.color = cols[2] + (1,)
    mix = nt.nodes.new("ShaderNodeMix")
    mix.data_type = "RGBA"
    mix.blend_type = "MULTIPLY"
    mix.inputs["Factor"].default_value = 1.0
    if img is not None:
        t = nt.nodes.new("ShaderNodeTexImage")
        t.image = img
        t.interpolation = "Linear"
        nt.links.new(t.outputs["Color"], mix.inputs["A"])
    else:
        mix.inputs["A"].default_value = base or (0.8, 0.8, 0.8, 1)
    em = nt.nodes.new("ShaderNodeEmission")
    nt.links.new(dif.outputs[0], s2r.inputs[0])
    nt.links.new(s2r.outputs["Color"], bw.inputs[0])
    nt.links.new(bw.outputs[0], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], mix.inputs["B"])
    nt.links.new(mix.outputs["Result"], em.inputs["Color"])
    nt.links.new(em.outputs[0], out.inputs["Surface"])
    return m


def sun(scene, name, travel_dir, strength, color, shadows=False):
    ld = bpy.data.lights.new(name, "SUN")
    ld.energy = strength
    ld.color = color
    ld.use_shadow = shadows
    ld.angle = math.radians(5)
    o = bpy.data.objects.new(name, ld)
    scene.collection.objects.link(o)
    o.rotation_euler = Vector(travel_dir).normalized().to_track_quat("-Z", "Y").to_euler()
    return o


def lights(scene, cfg=None):
    cfg = cfg or {}
    sun(scene, "key", cfg.get("key_dir", KEY["dir"]), cfg.get("key", KEY["energy"]), KEY["color"], cfg.get("shadows", False))
    sun(scene, "fill", cfg.get("fill_dir", FILL["dir"]), cfg.get("fill", FILL["energy"]), FILL["color"], cfg.get("shadows", False))
    world = bpy.data.worlds.new("w")
    world.use_nodes = True
    world.node_tree.nodes["Background"].inputs[0].default_value = (0.08, 0.07, 0.07, 1)
    world.node_tree.nodes["Background"].inputs[1].default_value = 1.0
    scene.world = world


def render(scene, filepath, samples=16):
    eng = [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items]
    scene.render.engine = "BLENDER_EEVEE" if "BLENDER_EEVEE" in eng else "BLENDER_EEVEE_NEXT"
    scene.render.film_transparent = True
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    try:
        scene.eevee.taa_render_samples = samples
    except Exception:
        pass
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.filepath = filepath
    bpy.ops.render.render(write_still=True)
    print("RENDERED", filepath, scene.render.resolution_x, scene.render.resolution_y)
