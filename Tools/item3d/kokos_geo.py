"""Blender -b: flatten bucket walls onto a clean profile, thin + splay the straws, swap in the new texture, export GLB.
Args: <in.glb> <tex.png> <out.glb>"""
import bpy, sys, math, numpy as np
glb, tex, out = sys.argv[sys.argv.index("--") + 1:][:3]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
ob = [o for o in bpy.data.objects if o.type == "MESH" and len(o.data.vertices) > 500][0]
me = ob.data
V = np.array([v.co[:] for v in me.vertices], np.float64)
Nv = np.array([v.normal[:] for v in me.vertices], np.float64)
r = np.hypot(V[:, 0], V[:, 1]); z = V[:, 2]
rad = (Nv[:, 0] * V[:, 0] + Nv[:, 1] * V[:, 1]) / np.maximum(r, 1e-6)
newV = V.copy()

def profile(mask, zlo, zhi, deg=2, step=0.02):
    zs, rs = [], []
    for a in np.arange(zlo, zhi, step):
        m = mask & (z >= a) & (z < a + step)
        if m.sum() > 8:
            zs.append(a + step / 2); rs.append(np.median(r[m]))
    zs = np.array(zs); rs = np.array(rs)
    # smooth + fit a gentle curve (quadratic) so the wall is a clean frustum
    rs = np.convolve(np.pad(rs, 1, mode="edge"), np.ones(3) / 3, mode="valid")
    return zs, rs

# --- outer wall -> smooth frustum
outer = (rad > 0.25) & (r > 0.3) & (z > 0.0) & (z < 0.60)
zbins, rbins = profile(outer, 0.0, 0.60)
rp = np.interp(z, zbins, rbins)
sel = outer & (np.abs(r - rp) < 0.09)
f = np.where(sel, rp / np.maximum(r, 1e-6), 1.0)
newV[:, 0] *= f; newV[:, 1] *= f
flap = (rad > -0.1) & (r > 0.40) & (z > 0.30) & (z < 0.585) & (np.abs(Nv[:, 2]) < 0.8) & ~sel
ff = np.where(flap, rp / np.maximum(r, 1e-6), 1.0)
newV[:, 0] *= ff; newV[:, 1] *= ff
print('flap', flap.sum())
print('outer profile', len(zbins), sel.sum(), 'of', outer.sum())
# --- inner wall -> smooth
inn = (rad < -0.3) & (r > 0.36) & (z > 0.45) & (z < 0.62)
zi_b, ri_b = profile(inn, 0.45, 0.62)
rpi = np.interp(z, zi_b, ri_b)
seli = inn & (np.abs(r - rpi) < 0.06)
fi = np.where(seli, rpi / np.maximum(r, 1e-6), 1.0)
newV[:, 0] *= fi; newV[:, 1] *= fi
print('inner profile', len(zi_b), seli.sum(), 'of', inn.sum())

# --- straws: above the rim (z>0.66, r<0.45) are straws for sure; label them as components, then extend downward
tris = np.array([t.vertices[:] for t in me.loop_triangles]) if me.loop_triangles else None
me.calc_loop_triangles()
tris = np.array([t.vertices[:] for t in me.loop_triangles])
key = {}; wid = np.zeros(len(V), int)
for i, v in enumerate(V):
    wid[i] = key.setdefault(tuple(np.round(v * 1e4).astype(np.int64)), len(key))
top = (z > 0.545) & (r < 0.40)
par = list(range(len(key)))
def find(a):
    while par[a] != a:
        par[a] = par[par[a]]; a = par[a]
    return a
for t in tris:
    if top[t[0]] and top[t[1]] and top[t[2]]:
        a, b, c_ = wid[t[0]], wid[t[1]], wid[t[2]]
        par[find(b)] = find(a); par[find(c_)] = find(a)
lab = {}
tl = -np.ones(len(V), int)
for i in np.flatnonzero(top):
    tl[i] = lab.setdefault(find(wid[i]), len(lab))
print('straw top comps', len(lab), [int((tl == k).sum()) for k in range(len(lab))])
ZB = 0.47
axes = []
for k in range(len(lab)):
    pts = V[tl == k]
    if len(pts) < 20: continue
    print('comp', k, len(pts), np.round(pts.min(0),2).tolist(), np.round(pts.max(0),2).tolist())
    cen = pts.mean(0)
    u_, s_, vt = np.linalg.svd(pts - cen)
    d = vt[0]
    if d[2] < 0: d = -d
    if d[2] < 0.7: d = np.array([cen[0], cen[1], 0.0]) * 0.25 / max(np.hypot(cen[0], cen[1]), 1e-6) + np.array([0, 0, 1.0]); d = d / np.linalg.norm(d)
    print('  d', np.round(d,2).tolist())
    axes.append((cen, d, k))
print('axes', [(np.round(a[0], 2).tolist(), np.round(a[1], 2).tolist()) for a in axes])
# assign every vertex in the straw zone to the nearest axis line
zone = (z > 0.50) & (r < 0.47) & (rad > -2)
best = np.full(len(V), -1); bd = np.full(len(V), 1e9)
for j, (cen, d, k) in enumerate(axes):
    w = V - cen
    t = w @ d
    dist = np.linalg.norm(w - np.outer(t, d), axis=1)
    m = zone & (dist < bd) & (dist < 0.042)
    # only below the top end of that straw and above the drink
    best[m] = j; bd[m] = dist[m]
inb = (best >= 0)
# exclude rim and walls
inb &= ~((r > 0.42) & (z < 0.64))
print('straw verts', inb.sum())
THIN = 0.74; TILT = math.radians(11)
for j, (cen, d, k) in enumerate(axes):
    m = inb & (best == j)
    if m.sum() == 0: continue
    # base point on the axis at the drink surface
    tb = (ZB - cen[2]) / d[2]
    base = cen + tb * d
    out_h = np.array([base[0], base[1], 0.0]); nh = np.linalg.norm(out_h)
    out_h = out_h / nh if nh > 0.04 else np.array([d[0], d[1], 0.0]) / max(np.hypot(d[0], d[1]), 1e-6)
    # thin about the axis
    w = V[m] - base
    t = w @ d
    perp = w - np.outer(t, d)
    w2 = np.outer(t, d) + perp * THIN
    # tilt about the base: rotate around axis (z x out_h) so the top leans outward
    ax = np.cross([0, 0, 1.0], out_h); ax /= np.linalg.norm(ax)
    # rotation by -TILT or +TILT depending on direction; Rodrigues
    def rot(vv, ang):
        c_, s_ = math.cos(ang), math.sin(ang)
        return vv * c_ + np.cross(ax, vv) * s_ + np.outer(vv @ ax, ax) * (1 - c_)
    w3 = rot(w2, -TILT)
    # pick the sign that moves the tip outward
    tip = np.array([0, 0, 0.3])
    if (rot(tip[None], -TILT)[0] @ out_h) < 0: w3 = rot(w2, TILT)
    newV[m] = base + w3
# --- low fill: drop the drink + ice, stretch the inner wall and straws down to meet it
DROP = 0.12
nz_ = Nv[:, 2]
wall_in = (rad < -0.3) & (np.abs(nz_) < 0.75) & (r > 0.36) & (z > 0.34) & (z < 0.62)
dm = (r < 0.42) & (z > 0.34) & (z < 0.60) & ~inb & ~wall_in & (rad < 0.2) & (nz_ > -0.3)
newV[dm, 2] -= DROP
z0w = 0.36
sw = wall_in
zz = z[sw]
newV[sw, 2] = np.where(zz >= z0w, (z0w - DROP) + (zz - z0w) * (0.62 - (z0w - DROP)) / (0.62 - z0w), zz - DROP)
zs_ = newV[inb, 2]
newV[inb, 2] = zs_ - (DROP + 0.04) * np.clip((0.66 - zs_) / 0.22, 0, 1)
print('lowered', dm.sum(), sw.sum(), inb.sum())
for i, v in enumerate(me.vertices):
    v.co = newV[i]
me.update()
bpy.ops.object.select_all(action='DESELECT'); ob.select_set(True); bpy.context.view_layer.objects.active = ob
bpy.ops.mesh.customdata_custom_splitnormals_clear()
bpy.ops.object.shade_auto_smooth(angle=math.radians(48))

# --- texture: one image on the base-colour node, other maps dropped
mat = ob.material_slots[0].material
nt = mat.node_tree
img = bpy.data.images.load(tex)
img.colorspace_settings.name = "sRGB"
bsdf = [n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"][0]
for n in list(nt.nodes):
    if n.type == "TEX_IMAGE": nt.nodes.remove(n)
tn = nt.nodes.new("ShaderNodeTexImage"); tn.image = img
nt.links.new(tn.outputs["Color"], bsdf.inputs["Base Color"])
bpy.ops.export_scene.gltf(filepath=out, export_format='GLB', export_image_format='JPEG', export_yup=True)
print("EXPORTED", out)





