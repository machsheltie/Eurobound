"""Night presentation shot matched to the Absinthe Arcade reference render. Safe to re-run.

Builds everything in the `aa_preview` collection, which export_assets.py never
touches: wet cobbled street, a glimpse of the arcade floor behind the door, warm
window and lantern light, a moonlit night world, neon at full strength, bloom,
and a street-level camera. Nothing here is a manifest asset.

Usage: blender aa_exterior.blend --python preview_night.py
       (or exec() it in a live session, then render aa_night_cam)
"""

import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402

PREVIEW = "aa_preview"
GREEN = (0.35, 1.0, 0.08)
PURPLE = (0.62, 0.12, 1.0)
WARM = (1.0, 0.62, 0.28)

# Blender space: facade on y=0 facing -Y, street toward -Y, z up.
CAMERA_POS = (3.4, -9.6, 1.55)
CAMERA_AIM = (-0.6, 0.0, 6.2)
CAMERA_LENS = 17.0
RESOLUTION = (1312, 1200)


def preview_collection():
    coll = aa.get_or_create_collection(PREVIEW)
    for obj in list(coll.objects):
        data = obj.data
        bpy.data.objects.remove(obj, do_unlink=True)
        if data is None or data.users:
            continue
        if isinstance(data, bpy.types.Mesh):
            bpy.data.meshes.remove(data)
        elif isinstance(data, bpy.types.Light):
            bpy.data.lights.remove(data)
        elif isinstance(data, bpy.types.Camera):
            bpy.data.cameras.remove(data)
    return coll


def new_material(name):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat, nt, bsdf


def link_mesh(coll, name, verts, faces, mat):
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    mesh.uv_layers.new(name="uv_material")
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    coll.objects.link(obj)
    return obj


def box(coll, name, mn, mx, mat):
    (x0, y0, z0), (x1, y1, z1) = mn, mx
    v = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0),
         (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    f = [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
    return link_mesh(coll, name, v, f, mat)


def wet_cobble_material():
    """Rounded dark setts with bright wet tops, puddles that turn to mirrors."""
    mat, nt, bsdf = new_material("m_aa_preview_wet_cobble")
    N = nt.nodes.new
    tc = N("ShaderNodeTexCoord")
    mapping = N("ShaderNodeMapping")
    mapping.inputs["Scale"].default_value = (4.2, 3.4, 1.0)
    nt.links.new(tc.outputs["Object"], mapping.inputs["Vector"])
    vor = N("ShaderNodeTexVoronoi")
    vor.feature = "DISTANCE_TO_EDGE"
    vor.inputs["Randomness"].default_value = 0.35
    nt.links.new(mapping.outputs["Vector"], vor.inputs["Vector"])
    vor_col = N("ShaderNodeTexVoronoi")
    vor_col.inputs["Randomness"].default_value = 0.35
    nt.links.new(mapping.outputs["Vector"], vor_col.inputs["Vector"])
    # Stone dome profile: 0 in the joints, 1 on the crown.
    dome = N("ShaderNodeMapRange")
    dome.inputs["From Min"].default_value = 0.02
    dome.inputs["From Max"].default_value = 0.22
    nt.links.new(vor.outputs["Distance"], dome.inputs["Value"])
    # Per-stone tint.
    tint = N("ShaderNodeValToRGB")
    tint.color_ramp.elements[0].color = (0.035, 0.032, 0.034, 1)
    tint.color_ramp.elements[1].color = (0.11, 0.10, 0.095, 1)
    nt.links.new(vor_col.outputs["Distance"], tint.inputs["Fac"])
    joint_mix = N("ShaderNodeMix")
    joint_mix.data_type = "RGBA"
    joint_mix.inputs["B"].default_value = (0.012, 0.011, 0.012, 1)
    inv = N("ShaderNodeMath")
    inv.operation = "SUBTRACT"
    inv.inputs[0].default_value = 1.0
    nt.links.new(dome.outputs["Result"], inv.inputs[1])
    nt.links.new(inv.outputs["Value"], joint_mix.inputs["Factor"])
    nt.links.new(tint.outputs["Color"], joint_mix.inputs["A"])
    nt.links.new(joint_mix.outputs["Result"], bsdf.inputs["Base Color"])
    # Puddles: large soft noise, near-mirror where wet.
    noise = N("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 0.35
    noise.inputs["Detail"].default_value = 4.0
    nt.links.new(tc.outputs["Object"], noise.inputs["Vector"])
    puddle = N("ShaderNodeMapRange")
    puddle.inputs["From Min"].default_value = 0.46
    puddle.inputs["From Max"].default_value = 0.56
    puddle.inputs["To Min"].default_value = 0.16
    puddle.inputs["To Max"].default_value = 0.015
    nt.links.new(noise.outputs["Fac"], puddle.inputs["Value"])
    nt.links.new(puddle.outputs["Result"], bsdf.inputs["Roughness"])
    bump = N("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.55
    bump.inputs["Distance"].default_value = 0.03
    nt.links.new(dome.outputs["Result"], bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"], bsdf.inputs["Normal"])
    bsdf.inputs["Specular IOR Level"].default_value = 0.7
    return mat


def build_street(coll):
    mat = wet_cobble_material()
    v = [(-30, -26, 0), (30, -26, 0), (30, -0.02, 0), (-30, -0.02, 0)]
    link_mesh(coll, "aa_preview_street", v, [(0, 1, 2, 3)], mat)


def emissive(name, color, strength):
    mat, nt, bsdf = new_material(name)
    bsdf.inputs["Base Color"].default_value = (*color, 1)
    bsdf.inputs["Emission Color"].default_value = (*color, 1)
    bsdf.inputs["Emission Strength"].default_value = strength
    return mat


def checker_floor_material():
    mat, nt, bsdf = new_material("m_aa_preview_checker_floor")
    tc = nt.nodes.new("ShaderNodeTexCoord")
    chk = nt.nodes.new("ShaderNodeTexChecker")
    chk.inputs["Scale"].default_value = 1.0
    chk.inputs["Color1"].default_value = (0.75, 0.75, 0.72, 1)
    chk.inputs["Color2"].default_value = (0.01, 0.01, 0.012, 1)
    mapping = nt.nodes.new("ShaderNodeMapping")
    mapping.inputs["Scale"].default_value = (1.6, 1.6, 1.6)
    nt.links.new(tc.outputs["Object"], mapping.inputs["Vector"])
    nt.links.new(mapping.outputs["Vector"], chk.inputs["Vector"])
    nt.links.new(chk.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = 0.08
    return mat


def build_interior(coll):
    """Arcade floor behind the door: checker floor, dark room, cabinet row, green haze."""
    floor = checker_floor_material()
    link_mesh(coll, "aa_preview_interior_floor",
              [(-3.5, 0.3, 0.005), (3.5, 0.3, 0.005), (3.5, 11, 0.005), (-3.5, 11, 0.005)],
              [(0, 1, 2, 3)], floor)
    room, _, rb = new_material("m_aa_preview_interior_room")
    rb.inputs["Base Color"].default_value = (0.02, 0.025, 0.02, 1)
    rb.inputs["Roughness"].default_value = 0.6
    # Open box (no front face) so the door looks into it.
    x0, x1, y0, y1, z1 = -3.5, 3.5, 1.6, 11.0, 4.6
    v = [(x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0),
         (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    link_mesh(coll, "aa_preview_interior_room", v,
              [(4, 5, 6, 7), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)], room)
    # Cabinet row down both sides, instanced from the real cabinet kit piece.
    cab = aa.kit_collection("aa_prop_arcade_cabinet")
    rows = [(-1.9, 3.4, -90), (1.9, 4.2, 90), (-1.9, 5.6, -90), (1.9, 6.6, 90), (-0.3, 9.6, 180)]
    for i, (x, y, rot) in enumerate(rows, start=1):
        e = bpy.data.objects.new(f"aa_preview_interior_cabinet_{i:02d}", None)
        e.instance_type = "COLLECTION"
        e.instance_collection = cab
        e.location = (x, y, 0)
        e.rotation_euler = (0, 0, math.radians(rot))
        e.scale = (0.82, 0.82, 0.82)
        coll.objects.link(e)
    # Ceiling strip lights and a purple sign glow at the back.
    for i, y in enumerate((3.0, 5.5, 8.0), start=1):
        box(coll, f"aa_preview_interior_strip_{i:02d}", (-0.9, y - 0.06, 4.45), (0.9, y + 0.06, 4.55),
            emissive("m_aa_preview_strip_green", GREEN, 18.0))
    box(coll, "aa_preview_interior_back_sign", (-1.4, 10.9, 2.6), (1.4, 10.95, 3.3),
        emissive("m_aa_preview_sign_purple", PURPLE, 14.0))
    # Green haze filling the room.
    haze, nt, _ = new_material("m_aa_preview_green_haze")
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    vol = nt.nodes.new("ShaderNodeVolumePrincipled")
    vol.inputs["Color"].default_value = (*GREEN, 1)
    vol.inputs["Density"].default_value = 0.09
    vol.inputs["Emission Color"].default_value = (*GREEN, 1)
    vol.inputs["Emission Strength"].default_value = 0.35
    nt.links.new(vol.outputs["Volume"], out.inputs["Volume"])
    box(coll, "aa_preview_interior_haze", (-3.4, 0.2, 0.0), (3.4, 10.9, 4.5), haze)
    # Light pouring out of the door.
    add_light(coll, "aa_preview_interior_fill", "AREA", (0, 4.5, 4.3), 2200, GREEN,
              size=5.0, rot=(0, 0, 0))
    add_light(coll, "aa_preview_door_spill", "POINT", (0, 1.2, 1.6), 900, GREEN, radius=0.8)


def add_light(coll, name, kind, loc, energy, color, radius=0.1, size=1.0, rot=None, spot=None):
    data = bpy.data.lights.new(name, kind)
    data.energy = energy
    data.color = color
    if kind in ("POINT", "SPOT"):
        data.shadow_soft_size = radius
    if kind == "AREA":
        data.size = size
    if kind == "SPOT" and spot:
        data.spot_size = math.radians(spot)
        data.spot_blend = 0.6
    obj = bpy.data.objects.new(name, data)
    obj.location = loc
    if rot is not None:
        obj.rotation_euler = rot
    coll.objects.link(obj)
    return obj


def aim(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def build_lights(coll):
    # Windows: a warm glow behind each upper and ground window.
    window_spots = [(-4.6, 6.9), (4.6, 6.9), (-4.6, 10.5), (4.6, 10.5), (-4.6, 14.1), (4.6, 14.1)]
    for i, (x, z) in enumerate(window_spots, start=1):
        add_light(coll, f"aa_preview_window_glow_{i:02d}", "POINT", (x, 0.9, z + 1.0), 260, WARM,
                  radius=0.6)
    add_light(coll, "aa_preview_window_glow_ground", "POINT", (-4.4, 0.9, 4.6), 240, WARM, radius=0.6)
    # Wall lanterns pool warm light on the wall and street.
    for i, x in enumerate((-6.4, 6.4), start=1):
        add_light(coll, f"aa_preview_lantern_{i:02d}", "POINT", (x, -0.45, 5.0), 140, WARM,
                  radius=0.12)
    # Neon bounce: green from the marquee, purple from the conduits and mural pixels.
    add_light(coll, "aa_preview_marquee_bounce", "AREA", (0, -1.4, 4.3), 600, GREEN, size=4.0,
              rot=(math.radians(90), 0, 0))
    add_light(coll, "aa_preview_purple_wash", "AREA", (1.5, -2.5, 8.0), 900, PURPLE, size=6.0,
              rot=(math.radians(70), 0, 0))
    add_light(coll, "aa_preview_cabinet_glow", "POINT", (-4.4, -1.3, 1.6), 120, (0.4, 0.6, 1.0),
              radius=0.4)
    # Moonlight: cold, low, from the street side.
    moon = add_light(coll, "aa_preview_moon", "SUN", (0, 0, 20), 0.35, (0.55, 0.65, 1.0))
    moon.rotation_euler = (math.radians(58), 0, math.radians(-30))
    moon.data.angle = math.radians(1.0)


def build_camera(coll):
    cam_data = bpy.data.cameras.new("aa_night_cam")
    cam_data.lens = CAMERA_LENS
    cam_data.clip_end = 300
    cam = bpy.data.objects.new("aa_night_cam", cam_data)
    cam.location = CAMERA_POS
    aim(cam, CAMERA_AIM)
    coll.objects.link(cam)
    return cam


def night_world():
    world = bpy.data.worlds.get("aa_night_world") or bpy.data.worlds.new("aa_night_world")
    world.use_nodes = True
    nt = world.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputWorld")
    tc = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    nt.links.new(tc.outputs["Generated"], sep.inputs["Vector"])
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.45
    ramp.color_ramp.elements[0].color = (0.035, 0.028, 0.03, 1)  # warm haze at the horizon
    ramp.color_ramp.elements[1].position = 0.7
    ramp.color_ramp.elements[1].color = (0.004, 0.009, 0.03, 1)  # deep blue night
    nt.links.new(sep.outputs["Z"], ramp.inputs["Fac"])
    bg = nt.nodes.new("ShaderNodeBackground")
    bg.inputs["Strength"].default_value = 1.0
    nt.links.new(ramp.outputs["Color"], bg.inputs["Color"])
    nt.links.new(bg.outputs["Background"], out.inputs["Surface"])
    return world


def neon_full_strength():
    """Switch the night-preview hooks on and push the neon materials into emission."""
    for mat in bpy.data.materials:
        if not mat.use_nodes:
            continue
        node = mat.node_tree.nodes.get("AA_NeonStrength")
        if node is not None:
            node.outputs[0].default_value = 1.0 if mat.name == "m_aa_mural_decal" else 8.0
    for name, color, strength in (("aa_tmp_conduit_green", GREEN, 22.0),
                                  ("aa_tmp_conduit_purple", PURPLE, 22.0)):
        mat = bpy.data.materials.get(name)
        if mat is None:
            continue
        bsdf = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
        bsdf.inputs["Emission Color"].default_value = (*color, 1)
        bsdf.inputs["Emission Strength"].default_value = strength
    tag = bpy.data.materials.get("m_aa_arch_hero_tagline")
    if tag is not None:
        bsdf = next(n for n in tag.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
        bsdf.inputs["Emission Strength"].default_value = max(
            bsdf.inputs["Emission Strength"].default_value, 6.0)


def bloom():
    sc = bpy.context.scene
    group = getattr(sc, "compositing_node_group", None)
    if group is None and hasattr(sc, "compositing_node_group"):
        group = bpy.data.node_groups.new("aa_preview_compositor", "CompositorNodeTree")
        sc.compositing_node_group = group
    if group is None:
        sc.use_nodes = True
        group = sc.node_tree
    group.nodes.clear()
    rl = group.nodes.new("CompositorNodeRLayers")
    glare = group.nodes.new("CompositorNodeGlare")
    for attr, value in (("glare_type", "BLOOM"), ("quality", "HIGH")):
        if hasattr(glare, attr):
            setattr(glare, attr, value)
    for sock, value in (("Type", "Bloom"), ("Threshold", 1.0), ("Strength", 0.6), ("Size", 0.75)):
        if sock in glare.inputs:
            try:
                glare.inputs[sock].default_value = value
            except (TypeError, ValueError):
                pass
    group.links.new(rl.outputs["Image"], glare.inputs["Image"])
    if hasattr(group, "interface") and not any(
            i.item_type == "SOCKET" and i.in_out == "OUTPUT" for i in group.interface.items_tree):
        group.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
    out = group.nodes.new("NodeGroupOutput") if hasattr(group, "interface") else \
        group.nodes.new("CompositorNodeComposite")
    group.links.new(glare.outputs["Image"], out.inputs[0])


def main():
    coll = preview_collection()
    build_street(coll)
    build_interior(coll)
    build_lights(coll)
    cam = build_camera(coll)
    sc = bpy.context.scene
    # The day rig and the shell's flat black void stay out of the night shot.
    for name in ("aa_preview_sun", "Light"):
        obj = bpy.data.objects.get(name)
        if obj is not None:
            obj.hide_render = True
    void = bpy.data.objects.get("aa_shell_facade_interior_void")
    if void is not None:
        void.hide_render = True
    sc.world = night_world()
    neon_full_strength()
    sc.camera = cam
    sc.render.resolution_x, sc.render.resolution_y = RESOLUTION
    sc.view_settings.view_transform = "AgX"
    sc.view_settings.look = "AgX - Punchy" if "AgX - Punchy" in [
        i.identifier for i in sc.view_settings.bl_rna.properties["look"].enum_items] else "None"
    sc.view_settings.exposure = 0.0
    sc.eevee.use_raytracing = True
    sc.eevee.use_volumetric_shadows = True
    bloom()
    return {"objects": len(coll.objects), "camera": cam.name}


result = main()
print(result)
