"""Ingest the Tripo roof-gable head relief into wip/E2_roof_gable_head.blend (for mason-2 to swap in).

  blender -b --factory-startup --python ingest_gable_head.py [-- --glb aa_roof_gable_head_v2.glb --height 1.0]

tripo_raw/aa_roof_gable_head.glb -> object `aa_shell_facade_roof_gable_head` in collection
aa_kit/aa_roof_gable_head:
* welded (merge by distance), degenerate faces dissolved, normals made consistent; decimated to
  300k faces (no polygon limit, but the HD mesh is ~1.9M);
* the mirrored back half cut off and capped flat; the flat back sits on y = 0, street side -Y;
* pivot `wall`: bottom centre of the relief on its back plane; 1 m tall by default (`--height`);
* texture capped at 4K (Tripo ships 8K), colour pulled toward the facade sandstone
  (m_aa_limestone_tile_basecolor mean, sRGB ~(226, 207, 177)) by a hue/value/saturation correction;
  UV layers uv_material (Tripo atlas) + uv_bake.
"""
import sys
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
AA = REPO / "Assets/Graphics/worlds/debaucheryville/absinthearcade"
GLB = AA / "tripo_raw/aa_roof_gable_head.glb"
OUT = AA / "blender/wip/E2_roof_gable_head.blend"
TEX = AA / "textures"


def arg(name, default):
    a = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    return type(default)(a[a.index(name) + 1]) if name in a else default


def main():
    height = arg("--height", 1.0)
    glb = AA / "tripo_raw" / arg("--glb", GLB.name)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(glb))
    obs = [o for o in bpy.data.objects if o not in before and o.type == "MESH"]
    ob = obs[0]
    ob.data.transform(ob.matrix_world)
    ob.matrix_world = Matrix()
    ob.parent = None
    for o in [o for o in bpy.data.objects if o not in before and o is not ob]:
        bpy.data.objects.remove(o)
    # decimate the HD mesh
    if len(ob.data.polygons) > 300000:
        m = ob.modifiers.new("dec", "DECIMATE")
        m.ratio = 300000 / len(ob.data.polygons)
        dg = bpy.context.evaluated_depsgraph_get()
        new = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
        old = ob.data
        ob.modifiers.clear()
        ob.data = new
        bpy.data.meshes.remove(old)
    me = ob.data
    # glTF Y-up import: the relief faces -Y in Blender already (front view). Keep the street half.
    bm = bmesh.new()
    bm.from_mesh(me)
    ys = [v.co.y for v in bm.verts]
    ymid = (max(ys) + min(ys)) / 2 + (max(ys) - min(ys)) * 0.08
    res = bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, ymid, 0),
                                 plane_no=(0, 1, 0), clear_outer=True)
    edges = [e for e in res["geom_cut"] if isinstance(e, bmesh.types.BMEdge)]
    if edges:
        bmesh.ops.holes_fill(bm, edges=edges, sides=0)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-5)
    bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=1e-5)
    bad = [f for f in bm.faces if f.calc_area() < 1e-10]
    bmesh.ops.delete(bm, geom=bad, context="FACES")
    # drop small detached slivers left by the cut (< 300 verts)
    bm.verts.ensure_lookup_table()
    seen, kill = set(), []
    for v in bm.verts:
        if v.index in seen:
            continue
        st, isl = [v], []
        seen.add(v.index)
        while st:
            a = st.pop()
            isl.append(a)
            for e in a.link_edges:
                b = e.other_vert(a)
                if b.index not in seen:
                    seen.add(b.index)
                    st.append(b)
        if len(isl) < 300:
            kill += isl
    bmesh.ops.delete(bm, geom=kill, context="VERTS")
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me)
    bm.free()
    xs = [v.co.x for v in me.vertices]
    ys = [v.co.y for v in me.vertices]
    zs = [v.co.z for v in me.vertices]
    me.transform(Matrix.Translation((-(max(xs) + min(xs)) / 2, -max(ys), -min(zs))))
    me.transform(Matrix.Scale(height / (max(zs) - min(zs)), 4))
    # UVs: Tripo atlas -> uv_material, copy -> uv_bake
    if me.uv_layers:
        me.uv_layers[0].name = "uv_material"
        b = me.uv_layers.new(name="uv_bake")
        me.uv_layers.active = b
        me.uv_layers["uv_material"].active_render = True
        # fresh non-overlapping bake layout (the Tripo atlas has zero-area faces after the cut + cap)
        vl = bpy.context.view_layer
        bpy.context.scene.collection.objects.link(ob) if ob.name not in bpy.context.scene.collection.objects else None
        vl.objects.active = ob
        ob.select_set(True)
        with bpy.context.temp_override(active_object=ob, object=ob, selected_objects=[ob], selected_editable_objects=[ob]):
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_all(action="SELECT")
            bpy.ops.uv.smart_project(angle_limit=1.15, island_margin=0.002)
            bpy.ops.object.mode_set(mode="OBJECT")
    # material: cap textures at 4K, pull colour toward the facade sandstone
    for mat in me.materials:
        if not mat or not mat.node_tree:
            continue
        nt = mat.node_tree
        for n in nt.nodes:
            if n.type == "TEX_IMAGE" and n.image and max(n.image.size) > 4096:
                src = n.image
                src.scale(4096, 4096)
                p = TEX / f"{glb.stem}_basecolor_4k.png"
                src.save(filepath=str(p), quality=95)
                cs = src.colorspace_settings.name
                n.image = bpy.data.images.load(str(p))          # reference the 4K file, not the packed 8K
                n.image.colorspace_settings.name = cs
                bpy.data.images.remove(src)
        bsdf = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None)
        base = bsdf.inputs["Base Color"].links[0].from_node if bsdf and bsdf.inputs["Base Color"].links else None
        if base is not None:
            hsv = nt.nodes.new("ShaderNodeHueSaturation")
            hsv.inputs["Saturation"].default_value = 0.85
            hsv.inputs["Value"].default_value = 1.25
            nt.links.new(base.outputs["Color"], hsv.inputs["Color"])
            warm = nt.nodes.new("ShaderNodeMix")
            warm.data_type = "RGBA"
            warm.blend_type = "MULTIPLY"
            warm.inputs["Factor"].default_value = 0.5
            warm.inputs[7].default_value = (1.0, 0.9, 0.74, 1.0)
            nt.links.new(hsv.outputs[0], warm.inputs[6])
            nt.links.new(warm.outputs[2], bsdf.inputs["Base Color"])
        mat.name = "m_aa_roof_gable_head"
    ob.name = me.name = "aa_shell_facade_roof_gable_head"
    kit = bpy.data.collections.new("aa_kit")
    bpy.context.scene.collection.children.link(kit)
    c = bpy.data.collections.new("aa_roof_gable_head")
    kit.children.link(c)
    for cc in list(ob.users_collection):
        cc.objects.unlink(ob)
    c.objects.link(ob)
    ob["e2_pivot"] = "wall: bottom centre of the relief, back face on y=0, street -Y; scale to the gable"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(OUT), compress=True)
    print("@@JSON@@", {"faces": len(me.polygons), "dims": [round(d, 3) for d in ob.dimensions], "out": str(OUT)})


main()
