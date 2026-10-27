"""Daylight world for Absinthe Arcade preview renders. Safe to re-run.

A physical sky aligned with aa_preview_sun, so glass has a sky to reflect and
shaded reveals get blue skylight fill (with the old flat gray world, windows
read as solid panels and white sheers went muddy brown).

Usage: exec in the live session (then save), or --python before rendering.
"""

import math

import bpy

SUN = "aa_preview_sun"
STRENGTH = 0.18


def main():
    sc = bpy.context.scene
    world = bpy.data.worlds.get("aa_day_world") or bpy.data.worlds.new("aa_day_world")
    world.use_nodes = True
    nt = world.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputWorld")
    sky = nt.nodes.new("ShaderNodeTexSky")
    bg = nt.nodes.new("ShaderNodeBackground")
    bg.inputs["Strength"].default_value = STRENGTH
    nt.links.new(sky.outputs["Color"], bg.inputs["Color"])
    nt.links.new(bg.outputs["Background"], out.inputs["Surface"])
    sun = bpy.data.objects.get(SUN)
    if sun is not None:
        # Sun lamps shine down their local -Z; point the sky's sun the same way.
        d = sun.matrix_world.to_3x3() @ __import__("mathutils").Vector((0, 0, -1))
        to_sun = -d
        if hasattr(sky, "sun_elevation"):
            sky.sun_elevation = math.asin(max(-1.0, min(1.0, to_sun.z)))
            sky.sun_rotation = math.atan2(to_sun.x, to_sun.y) % (2 * math.pi)
    if hasattr(sky, "sun_disc"):
        sky.sun_disc = False          # the sun lamp does the direct light
    sc.world = world
    glass = bpy.data.materials.get("m_aa_window_glass")
    return {"world": world.name, "sky_type": getattr(sky, "sky_type", "?"),
            "glass": glass.name if glass else None}


result = main()
print(result)
