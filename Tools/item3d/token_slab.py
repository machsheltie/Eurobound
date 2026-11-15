"""Thick two-faced round token (front +Z, reverse -Z) from a 2048x1280 atlas (0 Tripo credits).

blender -b --python Tools/item3d/token_slab.py -- <atlas.png> <out.glb> [tilt_deg=62] [spin_deg=0]
Atlas: front art at left half (top 1024 rows), reverse art at right half (mirrored in x, so it reads from behind),
rim strip across the bottom 256 rows (u = angle). Diameter 1.0, 0.2 thick. One flat bite is pushed out of the rim
(chord at 0.465 around +40 deg). tilt = rotation about X leaning the front face toward the camera (camera at -Y);
use tilt 180-62 = 118 to show the reverse instead. spin = turn about the token's own axis first.
"""
import bpy, bmesh, sys, os, math

argv = sys.argv[sys.argv.index("--") + 1:]
atlas, out_glb = os.path.abspath(argv[0]), os.path.abspath(argv[1])
tilt = float(argv[2]) if len(argv) > 2 else 62.0
spin = float(argv[3]) if len(argv) > 3 else 0.0
bpy.ops.wm.read_factory_settings(use_empty=True)
img = bpy.data.images.load(atlas)
W, H = 2048, 1280
R, N = 0.5, 128
ZF, ZW = 0.10, 0.07
BITE_DIR, BITE_D = math.radians(40), 0.465
# (r, z, kind)  kind: F front art, B back art, W wall strip
prof = [(0.0, ZF, "F"), (0.455, ZF, "F"), (0.478, 0.092, "F"), (0.494, 0.082, "F"), (0.5, ZW, "F"),
        (0.5, ZW, "W"), (0.5, -ZW, "W"),
        (0.5, -ZW, "B"), (0.494, -0.082, "B"), (0.478, -0.092, "B"), (0.455, -ZF, "B"), (0.0, -ZF, "B")]
bm = bmesh.new(); uvl = bm.loops.layers.uv.new("UVMap")
rings = []
for (r, z, kd) in prof:
    if r == 0.0:
        rings.append([bm.verts.new((0, 0, z))] * N)
    else:
        rings.append([bm.verts.new((r * math.cos(2 * math.pi * k / N), r * math.sin(2 * math.pi * k / N), z)) for k in range(N)])
# the wall ring is split into two coincident rings (W top / W bottom) already (indices 5 and 6); face rings 4/5 and 6/7 are distinct verts too


def uv(kind, x, y, k):
    if kind == "F":
        return ((x / (2 * R) + 0.5) * 0.5, (y / (2 * R) + 0.5) * 1024 / H + 256 / H)
    if kind == "B":
        return (0.5 + (-x / (2 * R) + 0.5) * 0.5, (y / (2 * R) + 0.5) * 1024 / H + 256 / H)
    return (k / N, 0.5 * 256 / H)


faces = []
for i in range(len(prof) - 1):
    kind = prof[i][2] if prof[i][2] == prof[i + 1][2] else None
    if kind is None:
        continue                                       # junction between F/W/B rings handled by the wall quad below
    A, B = rings[i], rings[i + 1]
    for k in range(N):
        k2 = (k + 1) % N
        if prof[i][0] == 0.0:
            f = bm.faces.new((A[k], B[k2], B[k]))
            pts = [(A[k], k), (B[k2], k + 1), (B[k], k)]
        elif prof[i + 1][0] == 0.0:
            f = bm.faces.new((A[k], A[k2], B[k]))
            pts = [(A[k], k), (A[k2], k + 1), (B[k], k)]
        else:
            f = bm.faces.new((A[k], A[k2], B[k2], B[k]))
            pts = [(A[k], k), (A[k2], k + 1), (B[k2], k + 1), (B[k], k)]
        faces.append((f, kind, pts))
bm.normal_update()
fix = faces[0][0].normal.z < 0
for f, kind, pts in faces:
    if fix:
        f.normal_flip()
for f, kind, pts in faces:
    for l in f.loops:
        k = next(kk for (v, kk) in pts if v == l.vert)
        l[uvl].uv = uv(kind, l.vert.co.x, l.vert.co.y, k)
# make wall sit with strip v spanning z: simple constant v is fine (flat strip)
# push the bite after UVs are set
nx, ny = math.cos(BITE_DIR), math.sin(BITE_DIR)
for v in bm.verts:
    d = v.co.x * nx + v.co.y * ny
    if d > BITE_D:
        v.co.x -= (d - BITE_D) * nx; v.co.y -= (d - BITE_D) * ny
bmesh.ops.recalc_face_normals(bm, faces=list(bm.faces))
mesh = bpy.data.meshes.new("token"); bm.to_mesh(mesh); bm.free()
obj = bpy.data.objects.new("token", mesh); bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj; obj.select_set(True)
bpy.ops.object.shade_smooth_by_angle(angle=math.radians(45))
mat = bpy.data.materials.new("token_mat"); mat.use_nodes = True
nt = mat.node_tree; bsdf = nt.nodes["Principled BSDF"]
tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = img; tex.interpolation = "Linear"
nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
bsdf.inputs["Metallic"].default_value = 0.0; bsdf.inputs["Roughness"].default_value = 0.8
mesh.materials.clear(); mesh.materials.append(mat)
obj.rotation_euler = (math.radians(tilt), 0, math.radians(spin))
obj.rotation_mode = "XYZ"
bpy.ops.object.transform_apply(rotation=True)
bpy.ops.export_scene.gltf(filepath=out_glb, export_format="GLB", export_image_format="AUTO", export_jpeg_quality=95)
print("TOKEN", out_glb, len(mesh.vertices), len(mesh.polygons))
