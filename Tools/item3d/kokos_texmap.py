"""Blender -b: rasterise the GLB's UV layout to per-texel 3D position + normal (npz)."""
import bpy, sys, numpy as np
glb, out = sys.argv[sys.argv.index("--") + 1:][:2]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
ob = [o for o in bpy.data.objects if o.type == "MESH" and len(o.data.vertices) > 500][0]
me = ob.data
me.calc_loop_triangles()
mw = ob.matrix_world
V = np.array([(mw @ v.co)[:] for v in me.vertices], dtype=np.float32)
M3 = np.array(mw.to_3x3())
uvl = me.uv_layers.active.data
# weld vertices by position and label connected components
key = {}
wid = np.zeros(len(V), np.int64)
for i, v in enumerate(V):
    k = tuple(np.round(v * 1e4).astype(np.int64))
    wid[i] = key.setdefault(k, len(key))
par = list(range(len(key)))
def find(a):
    while par[a] != a:
        par[a] = par[par[a]]; a = par[a]
    return a
for t in me.loop_triangles:
    a, b, c = [wid[i] for i in t.vertices]
    ra, rb, rc = find(a), find(b), find(c)
    par[rb] = ra; par[find(rc)] = ra
roots = {}
vcomp = np.zeros(len(V), np.int32)
for i in range(len(V)):
    vcomp[i] = roots.setdefault(find(wid[i]), len(roots))
print('components', len(roots))
for ci in range(len(roots)):
    m = vcomp == ci
    if m.sum() > 30:
        print('COMP', ci, m.sum(), np.round(V[m].min(0), 3), np.round(V[m].max(0), 3))
N = 4096
vuv = np.zeros((len(V), 2), np.float32)
for l in me.loops: vuv[l.vertex_index] = uvl[l.index].uv
pos = np.zeros((N, N, 3), np.float32)
nor = np.zeros((N, N, 3), np.float32)
ok = np.zeros((N, N), bool)
comp = np.full((N, N), -1, np.int32)
VN = np.array([(M3 @ np.array(v.normal)) for v in me.vertices], dtype=np.float32)
for t in me.loop_triangles:
    idx = t.vertices
    uv = np.array([[uvl[l].uv[0], 1 - uvl[l].uv[1]] for l in t.loops]) * N
    x0, y0 = np.floor(uv.min(0)).astype(int); x1, y1 = np.ceil(uv.max(0)).astype(int)
    x0 = max(x0, 0); y0 = max(y0, 0); x1 = min(x1, N - 1); y1 = min(y1, N - 1)
    if x1 < x0 or y1 < y0: continue
    xs, ys = np.meshgrid(np.arange(x0, x1 + 1) + .5, np.arange(y0, y1 + 1) + .5)
    a, b, c = uv
    d = (b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])
    if abs(d) < 1e-9: continue
    w0 = ((b[1] - c[1]) * (xs - c[0]) + (c[0] - b[0]) * (ys - c[1])) / d
    w1 = ((c[1] - a[1]) * (xs - c[0]) + (a[0] - c[0]) * (ys - c[1])) / d
    w2 = 1 - w0 - w1
    m = (w0 >= -0.02) & (w1 >= -0.02) & (w2 >= -0.02)
    if not m.any(): continue
    P = w0[..., None] * V[idx[0]] + w1[..., None] * V[idx[1]] + w2[..., None] * V[idx[2]]
    Nn = w0[..., None] * VN[idx[0]] + w1[..., None] * VN[idx[1]] + w2[..., None] * VN[idx[2]]
    sl = (slice(y0, y1 + 1), slice(x0, x1 + 1))
    pos[sl][m] = P[m]; nor[sl][m] = Nn[m]; ok[sl][m] = True; comp[sl][m] = vcomp[idx[0]]
np.savez_compressed(out, pos=pos, nor=nor, ok=ok, V=V, comp=comp, vcomp=vcomp, vuv=vuv)
print("MAP", V.min(0), V.max(0), ok.mean())

