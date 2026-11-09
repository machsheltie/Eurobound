"""Ingest the Tripo keystone pieces (glazier) into wip/E4_head_ingest.blend. Re-runnable.

  blender -b --factory-startup --python e4_ingest_head.py

  tripo_raw/aa_keystone_head_v3.glb   -> object aa_e4_keystone_head
  tripo_raw/aa_keystone_volute_r.glb  -> object aa_e4_keystone_volute_src (superseded by the lower carving)
  tripo_raw/aa_keystone_lower_carving.glb -> object aa_e4_keystone_lower_carving
Each: import, join, weld glTF seam splits, drop loose crumbs (<0.2% verts), report islands (fused
extras), cap textures at 4K and save them to textures/e4_keystone, normalise to a 1 m tall unit
(centred in x, bottom z=0, front y=0). e4_build.py fits each one to its bible-pixel footprint through
aa_bible_cam, cuts the back flat to the wall and retones it.
"""
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
RAW = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/tripo_raw"
OUT = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/blender/wip/E4_head_ingest.blend"
TEX = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade/textures/e4_keystone"
PIECES = [("aa_keystone_head_v3.glb", "aa_e4_keystone_head"), ("aa_keystone_volute_r.glb", "aa_e4_keystone_volute_src"),
          ("aa_keystone_lower_carving.glb", "aa_e4_keystone_lower_carving")]


def islands(bm):
    bm.verts.ensure_lookup_table()
    seen, parts = set(), []
    for v in bm.verts:
        if v.index in seen:
            continue
        stack, isl = [v], []
        seen.add(v.index)
        while stack:
            x = stack.pop()
            isl.append(x)
            for e in x.link_edges:
                y = e.other_vert(x)
                if y.index not in seen:
                    seen.add(y.index)
                    stack.append(y)
        parts.append(isl)
    parts.sort(key=len, reverse=True)
    return parts


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
    lo = Vector([min(v.co[i] for v in bm.verts) for i in range(3)])
    hi = Vector([max(v.co[i] for v in bm.verts) for i in range(3)])
    s = 1.0 / (hi.z - lo.z)
    c = (lo + hi) / 2
    bmesh.ops.transform(bm, verts=bm.verts, matrix=Matrix.Scale(s, 4) @ Matrix.Translation((-c.x, -lo.y, -lo.z)))
    tris = sum(len(f.verts) - 2 for f in bm.faces)
    bm.to_mesh(me)
    bm.free()
    print("E4 INGEST", name, "tris", tris, "welded", welded, "islands", len(parts), [len(p) for p in parts[:6]],
          "crumb verts removed", len(kill), "raw size", [round(x, 3) for x in (hi - lo)])
    for i, uv in enumerate(me.uv_layers):
        if i == 0:
            uv.name = "uv_material"
    if "uv_bake" not in me.uv_layers:
        me.uv_layers.new(name="uv_bake")
    # textures: cap at 4K, save next to the kit
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


if __name__ == "__main__":
    main()
