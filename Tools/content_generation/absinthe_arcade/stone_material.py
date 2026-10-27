"""Limestone for the Absinthe Arcade shell, from the author's painted wall texture.

m_aa_limestone_painted_basecolor.png is the author's seamless limestone painting
(made seamless by a half-offset cross-blend; see the production doc). No joints,
cracks or grime are added here: the author paints distress by hand in Ucupaint.

Two samples of the painting at different scales and rotations are blended
under a large soft noise mask so the blotches don't visibly repeat across the
14 m facade. Relief comes from the painting's own luminance through a bump node.

  m_aa_limestone_weathered   walls, quoins
  m_aa_trim_weathered        mouldings, archivolt, plinths (a touch lighter)

The Headphone Gentleman is carved from the same stone (entrance reference), but
Tripo baked him a brown texture. tone_bust() keeps that texture's carved light and
dark and takes the colour from the facade limestone.

Usage: exec in the live session, or blender aa_exterior.blend --python stone_material.py
"""

import math
import sys
from pathlib import Path

import bpy
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402

TEXTURE = aa.REPO / ("Assets/Graphics/worlds/debaucheryville/absinthearcade/textures/"
                     "m_aa_limestone_painted_basecolor.png")
# Mottling should read hand- to torso-sized on the building, not floor-sized.
TILE_A = 1.8      # metres covered by one repeat of the painting
TILE_B = 2.3
CONTRAST = -0.12  # underpainting: let the hand-painted pass carry the detail
WALL_OBJECTS = ("aa_shell_facade_walls", "aa_shell_facade_quoins")
TRIM_OBJECTS = ("aa_shell_facade_mouldings", "aa_arch_hero_archivolt", "aa_arch_hero_plinths",
                "aa_arch_hero_cartouche")


def build(name, brightness):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    N, L = nt.nodes.new, nt.links.new
    out = N("ShaderNodeOutputMaterial")
    bsdf = N("ShaderNodeBsdfPrincipled")
    L(bsdf.outputs["BSDF"], out.inputs["Surface"])

    # Project by face direction so reveals, returns and soffits don't smear: front faces
    # use (x, z), side faces (y, z), top/bottom faces (x, y).
    tc = N("ShaderNodeTexCoord")
    sep = N("ShaderNodeSeparateXYZ")
    L(tc.outputs["Object"], sep.inputs["Vector"])

    def combine(u, v):
        c = N("ShaderNodeCombineXYZ")
        L(sep.outputs[u], c.inputs["X"])
        L(sep.outputs[v], c.inputs["Y"])
        return c.outputs["Vector"]

    front, side, flat_top = combine("X", "Z"), combine("Y", "Z"), combine("X", "Y")
    nsep = N("ShaderNodeSeparateXYZ")
    L(tc.outputs["Normal"], nsep.inputs["Vector"])

    def absval(sock):
        n = N("ShaderNodeMath")
        n.operation = "ABSOLUTE"
        L(sock, n.inputs[0])
        return n.outputs[0]

    ax, ay, az = absval(nsep.outputs["X"]), absval(nsep.outputs["Y"]), absval(nsep.outputs["Z"])

    def dominant(a, b, c):
        m = N("ShaderNodeMath")
        m.operation = "MAXIMUM"
        L(b, m.inputs[0])
        L(c, m.inputs[1])
        g = N("ShaderNodeMath")
        g.operation = "GREATER_THAN"
        L(a, g.inputs[0])
        L(m.outputs[0], g.inputs[1])
        return g.outputs[0]

    def vmix(fac, va, vb):
        m = N("ShaderNodeMix")
        m.data_type = "VECTOR"
        L(fac, m.inputs["Factor"])
        L(va, m.inputs[4])
        L(vb, m.inputs[5])
        return m.outputs[1]

    proj = vmix(dominant(ax, ay, az), front, side)
    proj = vmix(dominant(az, ax, ay), proj, flat_top)

    img = bpy.data.images.load(str(TEXTURE), check_existing=True)

    def sample(tile, rot, shift):
        m = N("ShaderNodeMapping")
        m.inputs["Location"].default_value = (shift, shift * 0.37, 0)
        m.inputs["Rotation"].default_value = (0, 0, math.radians(rot))
        m.inputs["Scale"].default_value = (1 / tile, 1 / tile, 1)
        L(proj, m.inputs["Vector"])
        t = N("ShaderNodeTexImage")
        t.image = img
        t.interpolation = "Cubic"
        L(m.outputs["Vector"], t.inputs["Vector"])
        return t.outputs["Color"]

    a = sample(TILE_A, 0, 0.0)
    b = sample(TILE_B, 90, 0.41)
    noise = N("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 0.22
    noise.inputs["Detail"].default_value = 2.0
    L(proj, noise.inputs["Vector"])
    fac = N("ShaderNodeMapRange")
    fac.inputs["From Min"].default_value = 0.42
    fac.inputs["From Max"].default_value = 0.58
    L(noise.outputs["Fac"], fac.inputs["Value"])
    mix = N("ShaderNodeMix")
    mix.data_type = "RGBA"
    L(fac.outputs["Result"], mix.inputs["Factor"])
    L(a, mix.inputs[6])
    L(b, mix.inputs[7])
    color = mix.outputs[2]

    bc = N("ShaderNodeBrightContrast")
    bc.inputs["Bright"].default_value = brightness - 1.0
    bc.inputs["Contrast"].default_value = CONTRAST
    L(color, bc.inputs["Color"])
    color = bc.outputs["Color"]
    L(color, bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = 0.82

    bw = N("ShaderNodeRGBToBW")
    L(color, bw.inputs["Color"])
    bump = N("ShaderNodeBump")
    bump.inputs["Strength"].default_value = 0.45
    bump.inputs["Distance"].default_value = 0.01
    L(bw.outputs["Val"], bump.inputs["Height"])
    L(bump.outputs["Normal"], bsdf.inputs["Normal"])
    return mat


def assign(names, mat):
    done = []
    for n in names:
        obj = bpy.data.objects.get(n)
        if obj is None:
            continue
        for slot in obj.material_slots:
            if slot.material and slot.material.name.startswith(("m_aa_limestone", "m_aa_trim")):
                slot.material = mat
        done.append(n)
    return done


BUST_MATERIAL = "m_aa_arch_hero"
BUST_STONE = (0.64, 0.53, 0.39)   # sRGB; warm sandy limestone, as in the gentleman reference
BUST_DETAIL = 0.55                # how much of the texture's light/dark survives (exponent)


def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def tone_bust():
    """Base colour = limestone x (texture luminance / its median) ^ BUST_DETAIL. Idempotent."""
    mat = bpy.data.materials.get(BUST_MATERIAL)
    if mat is None:
        return None
    nt = mat.node_tree
    N, L = nt.nodes.new, nt.links.new
    bsdf = nt.nodes["Principled BSDF"]
    tex = next(n for n in nt.nodes if n.type == "TEX_IMAGE" and "basecolor" in n.image.name)
    for n in [n for n in nt.nodes if n.name.startswith("aa_tone")]:
        nt.nodes.remove(n)
    img = tex.image
    px = np.empty(img.size[0] * img.size[1] * 4, dtype=np.float32)
    img.pixels.foreach_get(px)
    rgb = px.reshape(-1, 4)[:, :3]
    lin = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    lum_med = float(np.median(lin @ np.array([0.2126, 0.7152, 0.0722])))

    bw = N("ShaderNodeRGBToBW")
    div = N("ShaderNodeMath")
    div.operation, div.inputs[1].default_value = "DIVIDE", lum_med
    pw = N("ShaderNodeMath")
    pw.operation, pw.inputs[1].default_value = "POWER", BUST_DETAIL
    mix = N("ShaderNodeMix")
    mix.data_type, mix.blend_type = "RGBA", "MULTIPLY"
    mix.inputs["Factor"].default_value = 1.0
    mix.inputs[6].default_value = (*[srgb_to_linear(c) for c in BUST_STONE], 1)
    for i, n in enumerate((bw, div, pw, mix)):
        n.name = f"aa_tone_{i}"
        n.location = (tex.location.x + 200 + 180 * i, tex.location.y + 300)
    L(tex.outputs["Color"], bw.inputs["Color"])
    L(bw.outputs["Val"], div.inputs[0])
    L(div.outputs["Value"], pw.inputs[0])
    L(pw.outputs["Value"], mix.inputs[7])
    L(mix.outputs[2], bsdf.inputs["Base Color"])
    return round(lum_med, 4)


def main():
    wall = build("m_aa_limestone_weathered", 1.0)
    trim = build("m_aa_trim_weathered", 1.06)
    return {"walls": assign(WALL_OBJECTS, wall), "trim": assign(TRIM_OBJECTS, trim),
            "bust_lum_median": tone_bust()}


result = main()
print(result)
