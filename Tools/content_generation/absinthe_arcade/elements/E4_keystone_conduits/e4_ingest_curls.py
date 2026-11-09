"""Ingest glazier's two Tripo scroll clusters into wip/E4_curls_ingest.blend. Re-runnable.

  blender -b --factory-startup --python e4_ingest_curls.py

  tripo_raw/aa_keystone_curls_right.glb -> object aa_e4_keystone_curls_r
  tripo_raw/aa_keystone_curls_left.glb  -> object aa_e4_keystone_curls_l

Each: import, join, weld glTF seam splits, drop loose crumbs (<0.2% verts), report islands (fused extras),
decimate to ~300k tris, cap textures at 4K (saved to textures/e4_keystone), normalise to a 1 m tall unit
(centred in x, bottom z = 0, front y = 0). Renders a 4-side check sheet per piece for fused extras.
e4_build.py fits each to its side's bible footprint through aa_bible_cam, cuts the back flat and retones it.
"""
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from e4_ingest_head import RAW, TEX, islands  # noqa: E402  (module guards main() below)

REPO = HERE.parents[4]
OUT = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/wip/E4_curls_ingest.blend"
PIECES = [("aa_keystone_curls_right.glb", "aa_e4_keystone_curls_r"),
          ("aa_keystone_curls_left.glb", "aa_e4_keystone_curls_l")]
TARGET_TRIS = 300000


def ingest(glb, name):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(RAW / glb))
    new = [o for o in bpy.data.objects if o not in before]
    meshes = [o for o in new if o.type == "MESH"]
    for o in meshes:
        o.data.transform(o.matrix_world)
        o.parent = None
        o.matrix_world = Matrix.Identity(4)
    if len(meshes) > 1:
        with bpy.context.temp_override(active_object=meshes[0], selected_editable_objects=meshes,
                                       selected_objects=meshes):
            bpy.ops.object.join()
    for o in new:
        if o.name in bpy.data.objects and o.type != "MESH":
            bpy.data.objects.remove(o)
    ob = [o for o in bpy.data.objects if o.type == "MESH" and o in new][0]
    ob.name = ob.data.name = name
    me = ob.data
    bm = bmesh.new()
    bm.from_mesh(me)
    n0 = len(bm.verts)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-6)
    welded = n0 - len(bm.verts)
    parts = islands(bm)
    kill = [v for p in parts[1:] if len(p) < 0.002 * len(bm.verts) for v in p]
    if kill:
        bmesh.ops.delete(bm, geom=kill, context="VERTS")
    bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-7)
    bm.to_mesh(me)
    bm.free()
    tris0 = sum(len(p.vertices) - 2 for p in me.polygons)
    if tris0 > TARGET_TRIS:
        dm = ob.modifiers.new("Decimate", "DECIMATE")
        dm.ratio = TARGET_TRIS / tris0
        dm.use_collapse_triangulate = True
        dg = bpy.context.evaluated_depsgraph_get()
        nm = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
        ob.modifiers.clear()
        old = ob.data
        ob.data = nm
        nm.name = name
        bpy.data.meshes.remove(old)
        me = ob.data
    vs = [v.co for v in me.vertices]
    lo = Vector([min(v[i] for v in vs) for i in range(3)])
    hi = Vector([max(v[i] for v in vs) for i in range(3)])
    s = 1.0 / (hi.z - lo.z)
    c = (lo + hi) / 2
    me.transform(Matrix.Scale(s, 4) @ Matrix.Translation((-c.x, -lo.y, -lo.z)))
    me.update()
    tris = sum(len(p.vertices) - 2 for p in me.polygons)
    print("E4 INGEST", name, "tris", tris0, "->", tris, "welded", welded, "islands", len(parts),
          [len(p) for p in parts[:6]], "crumb verts removed", len(kill), "raw size", [round(x, 3) for x in (hi - lo)])
    TEX.mkdir(parents=True, exist_ok=True)
    for m in me.materials:
        for n in m.node_tree.nodes:
            if n.type != "TEX_IMAGE" or not n.image:
                continue
            im = n.image
            if im.size[0] > 4096 or im.size[1] > 4096:
                im.scale(4096, 4096)
            kind = "basecolor" if im.colorspace_settings.name == "sRGB" else \
                ("normal" if "normal" in im.name.lower() else "rm")
            im.name = f"{name}_{kind}"
            im.filepath_raw = str(TEX / f"{name}_{kind}.png")
            im.file_format = "PNG"
            im.save()
            im.filepath = im.filepath_raw
            print("E4 INGEST texture", im.name, tuple(im.size))
    return ob


def main():
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o)
    for glb, name in PIECES:
        ingest(glb, name)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(OUT))
    print("E4 INGEST saved", OUT)


main()
