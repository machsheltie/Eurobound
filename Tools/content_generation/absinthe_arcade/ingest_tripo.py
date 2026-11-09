"""Bring a Tripo-generated GLB into its kit collection, normalized to the manifest.

Steps: import -> bake transforms and join into one mesh -> optional yaw fix ->
uniform scale to the manifest height -> move to the asset's pivot rule ->
collapse-decimate to 95% of tri_budget only if the asset has one (null = keep full detail) -> uv_material (Tripo's atlas)
+ uv_bake (smart-projected, non-overlapping) -> replace the placeholder.

Tripo models face +Z in glTF, which lands facing -Y (street side) in Blender, the
kit convention. If one comes in turned, pass --yaw 90/180/270.

Tripo's material is renamed <asset_id>_tripo. validate_assets.py will warn until
it is rebaked into the manifest material (e.g. m_aa_props_atlas); that is the
cue for the texture pass, not an error.

Usage: blender aa_exterior.blend --background --python ingest_tripo.py -- \
           --asset aa_prop_arcade_cabinet --file path/to/tripo.glb [--yaw 0] [--no-decimate]
"""

import argparse
import math
import sys
from pathlib import Path

import bpy
import numpy as np
from mathutils import Matrix

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402


def import_glb(path):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(path))
    return flatten(set(bpy.data.objects) - before, path)


def from_scene(name):
    """Objects already in the scene, e.g. sent over by Tripo Bridge: the named
    object plus everything parented under it."""
    root = bpy.data.objects.get(name)
    if root is None:
        raise SystemExit(f"no object named {name!r} in the scene")
    return flatten({root, *root.children_recursive}, name)


def flatten(new, source):
    """Bake world transforms into the meshes, unparent them, drop the rest."""
    meshes = [o for o in new if o.type == "MESH"]
    if not meshes:
        raise RuntimeError(f"{source} contained no meshes")
    for o in meshes:
        o.data = o.data.copy() if o.data.users > 1 else o.data
        o.data.transform(o.matrix_world)
        o.parent = None
        o.matrix_world = Matrix.Identity(4)
    for o in new - set(meshes):
        bpy.data.objects.remove(o, do_unlink=True)
    return meshes


def join(meshes):
    if len(meshes) == 1:
        return meshes[0]
    with bpy.context.temp_override(active_object=meshes[0], selected_editable_objects=meshes,
                                   object=meshes[0]):
        bpy.ops.object.join()
    return meshes[0]


def normalize(obj, asset, yaw_deg):
    mesh = obj.data
    if yaw_deg:
        mesh.transform(Matrix.Rotation(math.radians(yaw_deg), 4, "Z"))
    lo, hi = aa.world_bbox([obj])
    target_h = aa.blender_dims(asset["dims"])[2]
    s = target_h / (hi[2] - lo[2])
    mesh.transform(Matrix.Scale(s, 4))
    lo, hi = aa.world_bbox([obj])
    cx, cy, cz = [(lo[i] + hi[i]) / 2 for i in range(3)]
    pivot = asset["pivot"]
    if pivot == "ground":
        shift = (-cx, -cy, -lo[2])
    elif pivot == "wall":
        shift = (-cx, -hi[1], -cz)
    else:
        raise ValueError(f"Tripo ingest supports ground/wall pivots, not {pivot!r}; place by hand")
    mesh.transform(Matrix.Translation(shift))
    mesh.update()
    return s


def decimate(obj, budget):
    tris = aa.tri_count(obj)
    if tris <= budget:
        return tris, tris
    mod = obj.modifiers.new("aa_decimate", "DECIMATE")
    mod.decimate_type = "COLLAPSE"
    mod.ratio = budget * 0.95 / tris
    mod.use_collapse_triangulate = True
    with bpy.context.temp_override(object=obj, active_object=obj):
        bpy.ops.object.modifier_apply(modifier=mod.name)
    return tris, aa.tri_count(obj)


def weld_seams(obj):
    """glTF splits vertices along UV seams; weld them so the mesh is one connected
    surface again (face-corner UVs survive the merge)."""
    bpy.context.view_layer.objects.active = obj
    for o in bpy.context.view_layer.objects:
        o.select_set(o == obj)
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.remove_doubles(threshold=0.00005)
    bpy.ops.object.mode_set(mode="OBJECT")


def setup_uvs(obj):
    """uv_material = Tripo's atlas. uv_bake = a copy of it when the atlas already sits
    inside 0..1 (Tripo atlases don't overlap), otherwise a smart projection."""
    uvs = obj.data.uv_layers
    if len(uvs) == 0:
        uvs.new(name="uv_material")
    uvs[0].name = "uv_material"
    src = uvs["uv_material"]
    co = np.empty(len(src.data) * 2, dtype=np.float32)
    src.data.foreach_get("uv", co)
    bake = uvs.get("uv_bake") or uvs.new(name="uv_bake")
    if len(co) and co.min() >= -1e-4 and co.max() <= 1 + 1e-4:
        bake.data.foreach_set("uv", np.clip(co, 0.0, 1.0))
    else:
        uvs.active = bake
        bpy.context.view_layer.objects.active = obj
        for o in bpy.context.view_layer.objects:
            o.select_set(o == obj)
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.uv.smart_project(island_margin=0.02)
        bpy.ops.object.mode_set(mode="OBJECT")
    uvs.active = uvs["uv_material"]
    for uv in uvs:
        uv.active_render = uv.name == "uv_material"


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--asset", required=True)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--file", help="Tripo GLB on disk")
    src.add_argument("--object", help="object already in the scene (Tripo Bridge import)")
    ap.add_argument("--yaw", type=float, default=0.0)
    ap.add_argument("--no-decimate", action="store_true")
    args = ap.parse_args(argv)

    manifest = aa.load_manifest()
    asset = next((a for a in manifest["assets"] if a["id"] == args.asset), None)
    if asset is None:
        raise SystemExit(f"unknown asset {args.asset!r}")
    coll = aa.kit_collection(asset["id"])
    if coll is None:
        raise SystemExit("kit collection missing; run setup_scene.py first")

    # Editing needs the kit visible; restore the previous state afterwards.
    layer = aa.find_layer_collection(aa.KIT_COLL)
    was_hidden = layer.hide_viewport if layer else False
    if layer:
        layer.hide_viewport = False

    obj = join(import_glb(Path(args.file)) if args.file else from_scene(args.object))
    weld_seams(obj)
    scale = normalize(obj, asset, args.yaw)
    budget = asset["tri_budget"]
    if args.no_decimate or budget is None:  # no polygon limits unless an asset opts in
        before = after = aa.tri_count(obj)
    else:
        before, after = decimate(obj, budget)
    setup_uvs(obj)

    for o in list(coll.objects):
        if o.get("aa_placeholder"):
            bpy.data.objects.remove(o, do_unlink=True)
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    coll.objects.link(obj)
    obj.name = obj.data.name = asset["id"]
    if len(obj.material_slots) == 1 and obj.material_slots[0].material:
        obj.material_slots[0].material.name = f"{asset['id']}_tripo"

    if layer:
        layer.hide_viewport = was_hidden
    return {"asset": asset["id"], "scale_applied": round(scale, 4), "tris_before": before,
            "tris_after": after, "budget": asset["tri_budget"]}


if __name__ == "__main__":
    result = main(aa.script_args())
    print(result)
