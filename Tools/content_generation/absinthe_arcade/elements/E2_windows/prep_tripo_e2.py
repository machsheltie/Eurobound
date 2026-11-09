"""E2 step 1: cache the Tripo/appended source meshes into a small wip/E2_tripo_cache.blend.

  blender -b --factory-startup --python prep_tripo_e2.py

* e2_tripo_keystone_floral: tripo_raw/aa_ornament_keystone_floral.glb (2M-face HD mesh), textures dropped
  (clean stone; the 8K maps stay in tripo_raw), decimated to 150k faces, the mirrored back half cut off
  and capped flat, normalised: centred on X, back face on y=0, bottom on z=0.
* e2_crest_src: aa_ornament_window_crest appended from aa_exterior.blend, transform applied, textures
  dropped, decimated to 200k faces.
* aa_prop_window_cat: appended as-is (mason's asset, used only for the review renders).
Keeps the build's memory small (the source scene and the 8K Tripo maps never enter the build).
"""
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
AA = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade"
MAIN_BLEND = AA / "blender/aa_exterior.blend"
GLB = AA / "tripo_raw/aa_ornament_keystone_floral.glb"
CACHE = AA / "blender/wip/E2_tripo_cache.blend"


def decimate(ob, max_faces):
    if len(ob.data.polygons) <= max_faces:
        return
    m = ob.modifiers.new("dec", "DECIMATE")
    m.ratio = max_faces / len(ob.data.polygons)
    dg = bpy.context.evaluated_depsgraph_get()
    new = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
    old = ob.data
    ob.modifiers.clear()
    ob.data = new
    bpy.data.meshes.remove(old)


def strip(ob):
    ob.data.materials.clear()


def clean(me, bisect=False):
    """Weld, drop degenerate/zero-area faces, cut non-manifold fans, refill holes, consistent normals.
    With bisect: keep the street half (-Y) of a Tripo relief (its back is a mirrored copy) and cap it flat."""
    bm = bmesh.new()
    bm.from_mesh(me)
    if bisect:
        ys = [v.co.y for v in bm.verts]
        ymid = (max(ys) + min(ys)) / 2 + (max(ys) - min(ys)) * 0.05
        res = bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, ymid, 0),
                                     plane_no=(0, 1, 0), clear_outer=True)
        edges = [e for e in res["geom_cut"] if isinstance(e, bmesh.types.BMEdge)]
        if edges:
            bmesh.ops.holes_fill(bm, edges=edges, sides=0)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
    bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-4)
    bad = [f for f in bm.faces if f.calc_area() < 1e-10]
    bmesh.ops.delete(bm, geom=bad, context="FACES")
    nm = {f for e in bm.edges if len(e.link_faces) > 2 for f in e.link_faces}
    if nm:
        bmesh.ops.delete(bm, geom=list(nm), context="FACES")
        bmesh.ops.holes_fill(bm, edges=[e for e in bm.edges if e.is_boundary], sides=8)
    loose = [v for v in bm.verts if not v.link_faces]
    bmesh.ops.delete(bm, geom=loose, context="VERTS")
    bmesh.ops.triangulate(bm, faces=[f for f in bm.faces if len(f.verts) > 4])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me)
    bm.free()


def import_relief(glb, name, max_faces):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(glb))
    new = [o for o in bpy.data.objects if o not in before and o.type == "MESH"]
    k = new[0]
    k.data.transform(k.matrix_world)
    k.matrix_world = Matrix()
    k.parent = None
    strip(k)
    for o in [o for o in bpy.data.objects if o not in before and o is not k]:
        bpy.data.objects.remove(o)
    decimate(k, max_faces)
    clean(k.data, bisect=True)
    me = k.data
    xs = [v.co.x for v in me.vertices]
    ys = [v.co.y for v in me.vertices]
    zs = [v.co.z for v in me.vertices]
    me.transform(Matrix.Translation((-(max(xs) + min(xs)) / 2, -max(ys), -min(zs))))
    seat_islands(me)
    k.name = name
    return k


def seat_islands(me, min_verts=150):
    """Relief islands (scroll ends the cut separated from the body): drop slivers, push the rest back
    so each island's back face lies on the wall plane y=0 (they read as carved from the wall)."""
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.verts.ensure_lookup_table()
    seen = set()
    isl = []
    for v in bm.verts:
        if v.index in seen:
            continue
        st, cur = [v], []
        seen.add(v.index)
        while st:
            a = st.pop()
            cur.append(a)
            for e in a.link_edges:
                b = e.other_vert(a)
                if b.index not in seen:
                    seen.add(b.index)
                    st.append(b)
        isl.append(cur)
    kill = []
    for g in isl:
        if len(g) < min_verts:
            kill += g
            continue
        dy = -max(v.co.y for v in g)
        if dy > 1e-6:
            for v in g:
                v.co.y += dy
    bmesh.ops.delete(bm, geom=kill, context="VERTS")
    bm.to_mesh(me)
    bm.free()


def main():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    coll = bpy.context.scene.collection
    TR = AA / "tripo_raw"
    import_relief(TR / "aa_ornament_keystone_rosette.glb", "e2_keystone_rosette", 150000)
    import_relief(TR / "aa_ornament_pediment_l2.glb", "e2_pediment_l2", 200000)
    if (TR / "aa_ornament_keystone_rosette_l1.glb").exists():
        import_relief(TR / "aa_ornament_keystone_rosette_l1.glb", "e2_keystone_rosette_l1", 150000)
    for im in list(bpy.data.images):
        bpy.data.images.remove(im)
    for m in list(bpy.data.materials):
        bpy.data.materials.remove(m)
    # crest + cat from the main file (only these datablocks)
    with bpy.data.libraries.load(str(MAIN_BLEND), link=False) as (src, dst):
        dst.objects = [n for n in ("aa_ornament_window_crest", "aa_prop_window_cat") if n in src.objects]
    for o in dst.objects:
        coll.objects.link(o)
    main_dir = MAIN_BLEND.parent
    for im in bpy.data.images:
        if im.filepath.startswith("//"):
            im.filepath = str((main_dir / im.filepath[2:]).resolve())
    c = bpy.data.objects["aa_ornament_window_crest"]
    c.data = c.data.copy()
    c.data.transform(c.matrix_basis)
    c.matrix_basis = Matrix()
    strip(c)
    decimate(c, 200000)
    clean(c.data)
    c.name = "e2_crest_src"
    bpy.ops.outliner.orphans_purge(do_recursive=True)
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(CACHE), compress=True)
    print("@@JSON@@", {o.name: len(o.data.polygons) for o in bpy.data.objects if o.type == "MESH"})


if __name__ == "__main__":
    main()
