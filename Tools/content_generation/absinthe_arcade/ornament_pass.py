"""Ornament pass: fit the Tripo ornaments to the kit. Safe to re-run.

  - cuts the small Tripo cartouche off aa_window_upper (everything above its hood
    cornice), since aa_ornament_window_crest now sits on the hood;
  - paints aa_ornament_rosette_painted in the mural greens: the carving's own
    shading (Tripo basecolor luminance) drives a leaf-green ramp, so it reads as
    original stone painted over, per the reference's painted stone flower.

Run after ingest_tripo.py has brought both ornaments in.
"""

import sys
from pathlib import Path

import bmesh
import bpy

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aa_common as aa  # noqa: E402

HOOD_TOP = 2.07          # window-local z of the hood cornice's top
PAINT_RAMP = [(0.0, (0.03, 0.16, 0.08)), (0.45, (0.10, 0.42, 0.16)),
              (0.8, (0.38, 0.70, 0.22)), (1.0, (0.70, 0.85, 0.45))]


def mesh_obj(asset_id):
    return next(o for o in aa.kit_collection(asset_id).objects if o.type == "MESH")


def trim_window_crest():
    obj = mesh_obj("aa_window_upper")
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    doomed = [v for v in bm.verts if v.co.z > HOOD_TOP]
    bmesh.ops.delete(bm, geom=doomed, context="VERTS")
    bm.to_mesh(obj.data)
    bm.free()
    obj.data.update()
    return len(doomed)


def paint_rosette():
    obj = mesh_obj("aa_ornament_rosette_painted")
    src = obj.data.materials[0]
    tex = next(n for n in src.node_tree.nodes if n.type == "TEX_IMAGE"
               and n.outputs["Color"].is_linked
               and any(l.to_socket.name == "Base Color" for l in n.outputs["Color"].links))
    mat = bpy.data.materials.get("m_aa_ornament_rosette_painted") or src.copy()
    mat.name = "m_aa_ornament_rosette_painted"
    nt = mat.node_tree
    bsdf = next(n for n in nt.nodes if n.type == "BSDF_PRINCIPLED")
    img = next(n for n in nt.nodes if n.type == "TEX_IMAGE" and n.image == tex.image)
    for name in ("aa_paint_bw", "aa_paint_ramp"):
        if name in nt.nodes:
            nt.nodes.remove(nt.nodes[name])
    bw = nt.nodes.new("ShaderNodeRGBToBW")
    bw.name = "aa_paint_bw"
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.name = "aa_paint_ramp"
    els = ramp.color_ramp.elements
    while len(els) > 2:
        els.remove(els[-1])
    els[0].position, els[0].color = PAINT_RAMP[0][0], (*PAINT_RAMP[0][1], 1)
    els[1].position, els[1].color = PAINT_RAMP[-1][0], (*PAINT_RAMP[-1][1], 1)
    for pos, col in PAINT_RAMP[1:-1]:
        e = els.new(pos)
        e.color = (*col, 1)
    nt.links.new(img.outputs["Color"], bw.inputs["Color"])
    nt.links.new(bw.outputs["Val"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], bsdf.inputs["Base Color"])
    bsdf.inputs["Roughness"].default_value = 0.7       # satin exterior paint
    obj.data.materials[0] = mat
    return mat.name


RELIEF_DEPTH = {"aa_ornament_window_crest": 0.16, "aa_ornament_rosette_painted": 0.12}


def flatten_relief(asset_id, depth):
    """Tripo extrudes reliefs ~0.5 m deep; squash to carving depth, back on the wall."""
    me = mesh_obj(asset_id).data
    ys = [v.co.y for v in me.vertices]
    y0, y1 = min(ys), max(ys)
    if y1 - y0 <= depth + 1e-4:
        return round(y1 - y0, 3)
    k = depth / (y1 - y0)
    for v in me.vertices:
        v.co.y = (v.co.y - y1) * k
    me.update()
    return depth


def dims(asset_id):
    obj = mesh_obj(asset_id)
    return [round(v, 3) for v in obj.dimensions]


def main():
    return {
        "window_verts_cut": trim_window_crest(),
        "rosette_material": paint_rosette(),
        "relief_depth": {a: flatten_relief(a, d) for a, d in RELIEF_DEPTH.items()},
        "dims": {a: dims(a) for a in ("aa_window_upper", "aa_ornament_window_crest",
                                      "aa_ornament_rosette_painted")},
    }


result = main()
print(result)
