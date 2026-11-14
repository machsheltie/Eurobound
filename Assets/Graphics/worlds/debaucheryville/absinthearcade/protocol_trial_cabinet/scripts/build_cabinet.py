"""Trial 2 step 5: scripted rebuild of the street cabinet from the reference silhouettes ("Tripo mesh as measuring stick", nhxz.3 method).
The Tripo raw mesh is the wrong proportion (0.58 x 0.57 x 0.98 m, aspect 0.59 vs the reference 0.39) and a different design (stickered body, two joysticks, other marquee),
so the silhouette comes from the approved side reference (traced in side_profile.json) and the width from props.json (0.725 m); height 1.85 m, depth 0.958 m.
blender -b --factory-startup --python build_cabinet.py -- <out.glb> [tex 2048] [base_hex 1c1a22]
Relief added from the FRONT reference layout: CRT glass recess and coin-door plate. Everything else is the plain extrusion with small bevels (gray-clay stage).
"""
import bpy, bmesh, sys, json, math, os
from mathutils import Vector
a = sys.argv[sys.argv.index("--") + 1:]
out = a[0]; TEX = int(a[1]) if len(a) > 1 else 2048; HEX = a[2] if len(a) > 2 else "1c1a22"
HERE = os.path.dirname(os.path.abspath(__file__))
H_M, W_M, D_M = 1.85, 0.725, 0.958
SW, SH = 383.0, 740.0
FW, FH = 290.0, 740.0
# cleaned side profile (ref px, y down); ragged sticker-edge noise on the lower back straightened, the front-top corner kept as traced (step-11 final pass: the first rebuild raised it to the marquee top and left a black wedge; the marquee art is now projected onto the slope at a low ndot instead)
POLY = [[297, 0], [304, 14], [304, 110], [254, 155], [248, 165], [248, 180], [263, 245], [302, 364], [363, 385], [382, 400], [382, 450], [350, 472], [350, 739],
        [44, 739], [36, 730], [36, 481], [31, 469], [0, 450], [0, 400], [9, 389], [79, 359], [93, 347], [97, 336], [97, 79], [110, 63], [280, 0]]
json.dump({"poly_px": POLY, "size_px": [SW, SH], "traced": "side_profile.json"}, open(os.path.join(HERE, "side_profile_cleaned.json"), "w"))
Y = lambda px: (px / SW - 0.5) * D_M
Z = lambda py: (SH - py) / SH * H_M
X = lambda px: (px / FW - 0.5) * W_M
bpy.ops.wm.read_factory_settings(use_empty=True)
bm = bmesh.new()
vs = [bm.verts.new((-W_M / 2, Y(px), Z(py))) for px, py in POLY]
f = bm.faces.new(vs)
if f.normal.x > 0:
    f.normal_flip()
r = bmesh.ops.extrude_face_region(bm, geom=[f])
nv = [e for e in r["geom"] if isinstance(e, bmesh.types.BMVert)]
bmesh.ops.translate(bm, vec=(W_M, 0, 0), verts=nv)
bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
bm.normal_update()

def cut_rect_on_wall(bm, y_plane, x0, x1, z0, z1):
    """bisect the whole mesh by the 4 planes of a front-view rectangle, return faces whose centre is in the rectangle on the wall at y_plane."""
    for co, no in (((x0, 0, 0), (1, 0, 0)), ((x1, 0, 0), (1, 0, 0)), ((0, 0, z0), (0, 0, 1)), ((0, 0, z1), (0, 0, 1))):
        geom = bm.verts[:] + bm.edges[:] + bm.faces[:]
        bmesh.ops.bisect_plane(bm, geom=geom, plane_co=co, plane_no=no, dist=1e-6)
    bm.faces.ensure_lookup_table()
    sel = [fc for fc in bm.faces if fc.normal.y < -0.9 and abs(fc.calc_center_median().y - y_plane) < 1e-4
           and x0 - 1e-5 <= fc.calc_center_median().x <= x1 + 1e-5 and z0 - 1e-5 <= fc.calc_center_median().z <= z1 + 1e-5]
    return sel

yw = Y(97)                       # monitor wall plane
# CRT recess: bezel box in the front ref (x 36-250, y 172-338), pushed back 3 cm
sel = cut_rect_on_wall(bm, yw, X(36), X(250), Z(338), Z(172))
r = bmesh.ops.inset_region(bm, faces=sel, thickness=0.012, depth=-0.0)
sel2 = [fc for fc in r.get("faces", [])] or sel
for fc in sel:
    pass
bmesh.ops.translate(bm, vec=(0, 0.03, 0), verts=list({v for fc in sel for v in fc.verts}))
bm.normal_update()
# coin-door plate (front ref x 98-192, y 480-694), raised 1.2 cm on the front plane at px 36
yc = Y(36)
sel = cut_rect_on_wall(bm, yc, X(98), X(192), Z(694), Z(488))
bmesh.ops.translate(bm, vec=(0, -0.012, 0), verts=list({v for fc in sel for v in fc.verts}))
bm.normal_update()
bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
# small bevels on sharp edges
sharp = [e for e in bm.edges if e.is_manifold and len(e.link_faces) == 2 and e.calc_face_angle(0) > math.radians(50)]
bmesh.ops.bevel(bm, geom=sharp, offset=0.004, segments=1, affect="EDGES")
bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
# triangulate + 2 cuts per edge: flat geometry unchanged, gives the projection tool (>500 verts, per-triangle sampling) a denser, even tessellation
STEP = 0.025   # 2.5 cm grid cuts through every flat face: even tessellation, so the projection tool's vertex+centroid silhouette report is dense enough to be meaningful
for axis, lo, hi in ((0, -W_M / 2, W_M / 2), (1, -D_M / 2, D_M / 2), (2, 0, H_M)):
    n = int((hi - lo) / STEP)
    for i in range(1, n):
        co = [0, 0, 0]; co[axis] = lo + i * STEP; no = [0, 0, 0]; no[axis] = 1
        bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=co, plane_no=no, dist=1e-6)
bmesh.ops.triangulate(bm, faces=bm.faces[:])
bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
me = bpy.data.meshes.new("street_cabinet"); bm.to_mesh(me); bm.free()
ob = bpy.data.objects.new("street_cabinet", me); bpy.context.scene.collection.objects.link(ob)
bpy.context.view_layer.objects.active = ob; ob.select_set(True)
bpy.ops.object.mode_set(mode="EDIT"); bpy.ops.mesh.select_all(action="SELECT")
bpy.ops.uv.smart_project(angle_limit=math.radians(60), island_margin=0.006, area_weight=0.0, correct_aspect=True, scale_to_bounds=False)
bpy.ops.uv.pack_islands(margin=0.006, rotate=False) if hasattr(bpy.ops.uv, "pack_islands") else None
bpy.ops.object.mode_set(mode="OBJECT")
bpy.ops.object.shade_smooth() if False else None
for p in me.polygons: p.use_smooth = False
# material + base-colour image filled with the body black (everything the references do not show is inferred body colour)
rgb = [int(HEX[i:i + 2], 16) / 255 for i in (0, 2, 4)]
img = bpy.data.images.new("cabinet_basecolor", TEX, TEX, alpha=False)
import numpy as np
# fill with the body colour as display values (the first package used c**2.2, i.e. a linear value, which stored as 3/255: the back face rendered mean RGB 3)
img.generated_color = (*rgb, 1.0); img.update()
img.colorspace_settings.name = "sRGB"
# write the fill to a PNG and reload it as a file image so the exporter embeds real pixels
_fp = out.replace(".glb", "_fill_tmp.png"); img.filepath_raw = _fp; img.file_format = "PNG"; img.save()
img = bpy.data.images.load(_fp); img.name = "cabinet_basecolor_file"; img.pack(); img.colorspace_settings.name = "sRGB"
mat = bpy.data.materials.new("cabinet_mat"); mat.use_nodes = True
bs = mat.node_tree.nodes["Principled BSDF"]
tn = mat.node_tree.nodes.new("ShaderNodeTexImage"); tn.image = img
mat.node_tree.links.new(tn.outputs["Color"], bs.inputs["Base Color"])
me.materials.append(mat)
dims = ob.dimensions
print("built", len(me.vertices), "verts", len(me.polygons), "faces", "dims", [round(d, 3) for d in dims])
bpy.ops.export_scene.gltf(filepath=out, export_format="GLB", export_image_format="AUTO", export_apply=False)
print("wrote", out)
os.remove(_fp)
