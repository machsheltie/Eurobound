"""Headless test for material_lookup.base_image (Eurobound-o2yv).

Run: blender --background --python Tools/item3d/test_material_lookup.py
Exits non-zero on failure.
"""
import os, sys
import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from material_lookup import base_image

FAILS = []


def check(name, got, want):
    ok = got is want
    print(("PASS " if ok else "FAIL ") + name, "" if ok else "(got %r, want %r)" % (got and got.name, want and want.name))
    if not ok:
        FAILS.append(name)


def make_mat(name, link_mode):
    """Normal map image node created FIRST, roughness second, base colour last."""
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    imgs = {k: bpy.data.images.new("%s_%s" % (name, k), 4, 4) for k in ("normal", "rough", "base")}
    tex = {}
    for k in ("normal", "rough", "base"):             # creation order = node list order
        n = nt.nodes.new("ShaderNodeTexImage")
        n.image = imgs[k]
        tex[k] = n
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    nmap = nt.nodes.new("ShaderNodeNormalMap")
    nt.links.new(tex["normal"].outputs["Color"], nmap.inputs["Color"])
    nt.links.new(nmap.outputs["Normal"], bsdf.inputs["Normal"])
    nt.links.new(tex["rough"].outputs["Color"], bsdf.inputs["Roughness"])
    if link_mode == "direct":
        nt.links.new(tex["base"].outputs["Color"], bsdf.inputs["Base Color"])
    elif link_mode == "via_mix":
        mix = nt.nodes.new("ShaderNodeMix")
        mix.data_type = "RGBA"
        nt.links.new(tex["base"].outputs["Color"], mix.inputs["B"])
        hsv = nt.nodes.new("ShaderNodeHueSaturation")
        nt.links.new(mix.outputs["Result"], hsv.inputs["Color"])
        nt.links.new(hsv.outputs["Color"], bsdf.inputs["Base Color"])
    return mat, imgs


# Precondition: the old "first image node" logic would pick the normal map here.
mat, imgs = make_mat("direct", "direct")
first = next(n.image for n in mat.node_tree.nodes if n.type == "TEX_IMAGE")
check("precondition: old first-node logic is wrong here", first, imgs["normal"])
check("direct link, normal node first", base_image(mat), imgs["base"])

mat, imgs = make_mat("mixed", "via_mix")
check("through mix + hue/sat nodes", base_image(mat), imgs["base"])

mat, imgs = make_mat("unlinked", "none")               # fallback: first image node, with a warning
check("fallback when Base Color unlinked", base_image(mat), imgs["normal"])

check("no material", base_image(None), None)

print("RESULT", "FAILED: %s" % FAILS if FAILS else "all passed")
sys.exit(1 if FAILS else 0)
