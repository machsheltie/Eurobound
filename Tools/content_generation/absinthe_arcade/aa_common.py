"""Shared helpers for the Absinthe Arcade Blender pipeline (runs inside Blender).

Two coordinate spaces are in play:
  engine  - meters, Y-up, facade front faces +Z (manifest.json, glTF, layout JSON)
  blender - meters, Z-up, facade front faces -Y (what you see in the viewport)
glTF import/export converts between them; the manifest is written in engine space,
so anything that reads manifest positions or dims goes through to_blender().
"""

import json
import sys
from pathlib import Path

import bpy

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
MANIFEST_PATH = HERE / "manifest.json"
ASSET_ROOT = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade"
EXPORT_DIR = ASSET_ROOT / "export"

KIT_COLL = "aa_kit"            # one child collection per asset, authored at world origin
LAYOUT_COLL = "aa_layout"      # collection-instance empties that assemble the building
REF_COLL = "aa_reference"      # imported blockout, display only

PIVOT_TOL = 0.05               # meters


def load_manifest():
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f)


def to_blender(p):
    x, y, z = p
    return (x, -z, y)


def to_engine(p):
    x, y, z = p
    return (x, z, -y)


def blender_dims(dims):
    """Manifest [w, h, d] -> Blender (x, y, z) extents."""
    w, h, d = dims
    return (w, d, h)


def script_args():
    """Arguments after `--` on the Blender command line (empty under MCP exec)."""
    argv = sys.argv
    return argv[argv.index("--") + 1:] if "--" in argv else []


def get_or_create_collection(name, parent=None):
    coll = bpy.data.collections.get(name)
    if coll is None:
        coll = bpy.data.collections.new(name)
    parent = parent or bpy.context.scene.collection
    if coll.name not in parent.children:
        parent.children.link(coll)
    return coll


def find_layer_collection(name, layer_coll=None):
    layer_coll = layer_coll or bpy.context.view_layer.layer_collection
    if layer_coll.collection.name == name:
        return layer_coll
    for child in layer_coll.children:
        found = find_layer_collection(name, child)
        if found:
            return found
    return None


def kit_collection(asset_id):
    return bpy.data.collections.get(asset_id)


def mesh_objects(coll):
    return [o for o in coll.all_objects if o.type == "MESH"] if coll else []


def tri_count(obj, depsgraph=None):
    depsgraph = depsgraph or bpy.context.evaluated_depsgraph_get()
    try:
        mesh = obj.evaluated_get(depsgraph).data
    except (RuntimeError, ReferenceError):
        mesh = obj.data
    return sum(len(p.vertices) - 2 for p in mesh.polygons)


def world_bbox(objs):
    """Axis-aligned world bounds over all vertices of objs, or None."""
    lo = [float("inf")] * 3
    hi = [float("-inf")] * 3
    for o in objs:
        mw = o.matrix_world
        for v in o.data.vertices:
            p = mw @ v.co
            for i in range(3):
                lo[i] = min(lo[i], p[i])
                hi[i] = max(hi[i], p[i])
    return (lo, hi) if objs and lo[0] != float("inf") else None


def pivot_offset(pivot, dims_b, category):
    """Center of a dims_b box placed so its pivot sits at the origin (placeholders)."""
    w, d, h = dims_b
    if pivot == "ground":
        return (0.0, 0.0, h / 2)
    if pivot == "wall":
        return (0.0, -d / 2, 0.0)
    if pivot == "sill":
        return (0.0, 0.0, h / 2 - 0.14)
    if pivot == "facade":
        return (0.0, d / 2 if category == "structure" else -d / 2, h / 2)
    raise ValueError(f"unknown pivot {pivot!r}")
