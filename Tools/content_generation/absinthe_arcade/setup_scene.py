"""Build the Absinthe Arcade authoring scene from manifest.json. Safe to re-run.

  aa_reference  blockout glTF, wireframe, unselectable
  aa_kit        one collection per asset, authored at world origin; empty ones get
                a sized placeholder box (custom prop aa_placeholder) at the right pivot
  aa_layout     one collection-instance empty per manifest instance, at its anchor

Real meshes already in a kit collection are never touched. The layout is rebuilt
from the manifest on every run, so edit positions in manifest.json, not by hand.

Usage: blender aa_exterior.blend --python setup_scene.py
"""

import sys
from pathlib import Path

import bmesh
import bpy

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402

CATEGORY_COLORS = {
    "structure": (0.78, 0.72, 0.60, 1.0),
    "prop": (0.25, 0.90, 0.10, 1.0),
    "decal": (0.75, 0.0, 1.0, 1.0),
}


def setup_units():
    us = bpy.context.scene.unit_settings
    us.system = "METRIC"
    us.scale_length = 1.0
    us.length_unit = "METERS"


def import_blockout(manifest):
    ref = aa.get_or_create_collection(aa.REF_COLL)
    if ref.objects:
        return "kept"
    path = aa.REPO / manifest["building"]["blockout"]
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(path))
    for obj in set(bpy.data.objects) - before:
        for c in list(obj.users_collection):
            c.objects.unlink(obj)
        ref.objects.link(obj)
        obj.display_type = "WIRE"
        obj.hide_select = True
        obj.hide_render = True
    return "imported"


def make_placeholder(asset, coll):
    dims_b = aa.blender_dims(asset["dims"])
    cx, cy, cz = aa.pivot_offset(asset["pivot"], dims_b, asset["category"])
    mesh = bpy.data.meshes.new(f"{asset['id']}_placeholder")
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x = v.co.x * dims_b[0] + cx
        v.co.y = v.co.y * dims_b[1] + cy
        v.co.z = v.co.z * dims_b[2] + cz
    bm.to_mesh(mesh)
    bm.free()
    for name in ("uv_material", "uv_bake"):
        mesh.uv_layers.new(name=name)
    obj = bpy.data.objects.new(f"{asset['id']}_placeholder", mesh)
    obj["aa_placeholder"] = True
    obj.color = CATEGORY_COLORS[asset["category"]]
    coll.objects.link(obj)


def build_kit(manifest):
    kit = aa.get_or_create_collection(aa.KIT_COLL)
    created = []
    for asset in manifest["assets"]:
        coll = aa.get_or_create_collection(asset["id"], kit)
        coll["aa_asset"] = True
        if not aa.mesh_objects(coll):
            make_placeholder(asset, coll)
            created.append(asset["id"])
    # Kit pieces overlap at the origin; hide them (viewport and render) and look at
    # the layout instances instead, which still draw and render.
    kit.hide_render = True
    layer = aa.find_layer_collection(aa.KIT_COLL)
    if layer:
        layer.hide_viewport = True
    return created


def build_layout(manifest):
    layout = aa.get_or_create_collection(aa.LAYOUT_COLL)
    for obj in list(layout.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    count = 0
    for asset in manifest["assets"]:
        coll = aa.kit_collection(asset["id"])
        for i, inst in enumerate(asset["instances"], start=1):
            empty = bpy.data.objects.new(f"{asset['id']}__{i:02d}", None)
            empty.instance_type = "COLLECTION"
            empty.instance_collection = coll
            empty.location = aa.to_blender(inst["pos"])
            empty["aa_asset_id"] = asset["id"]
            layout.objects.link(empty)
            count += 1
    return count


def main():
    manifest = aa.load_manifest()
    setup_units()
    return {
        "blockout": import_blockout(manifest),
        "placeholders_created": build_kit(manifest),
        "layout_instances": build_layout(manifest),
    }


result = main()
print(result)
