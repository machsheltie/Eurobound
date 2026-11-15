"""Phase B: wear for the surfaces the references never show (back, underside, recess walls, bevel strips), painted as flat grime in the style of the approved +X side body:
charcoal-violet paint (#231C24, the +X body median), mottling, vertical drips, rust creeping up from the foot, light scuffs, edge chips, peeled-sticker residue ghosts on the back.
ALL OF IT IS INFERRED (no reference shows these faces); it is a flat colour-only atlas fill, no relief, painted in 3D position space so the back, underside and walls carry it consistently.
Projection passes (front, +X, -X) overwrite it wherever a reference exists.
blender -b --factory-startup --python grime_fill.py -- <in.glb> <out.glb> [seed 1990]"""
import bpy, sys, numpy as np
a = sys.argv[sys.argv.index("--") + 1:]
IN, OUT = a[0], a[1]; SEED = int(a[2]) if len(a) > 2 else 1990
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=IN)
ob = max([o for o in bpy.data.objects if o.type == "MESH"], key=lambda o: len(o.data.vertices)); me = ob.data
node = [n for n in me.materials[0].node_tree.nodes if n.type == "TEX_IMAGE"][0]; img = node.image
W, H = img.size
mw = ob.matrix_world
vco = np.array([tuple(mw @ v.co) for v in me.vertices])
me.calc_loop_triangles()
uv = np.array([tuple(l.uv) for l in me.uv_layers.active.data]); tris = np.array([t.loops for t in me.loop_triangles]); tv = np.array([t.vertices for t in me.loop_triangles])
nrm = np.array([[tuple(x) for x in t.split_normals] for t in me.loop_triangles]) @ np.array(mw.to_3x3()).T
bmin, bmax = vco.min(0), vco.max(0)
rng = np.random.default_rng(SEED)
N = 64
VOL = [rng.random((N, N, N)).astype(np.float32) for _ in range(9)]


def noise(i, p, f):
    """periodic trilinear value noise, p in metres, f cells per metre (per axis tuple allowed)"""
    q = (p * np.asarray(f)) % N; i0 = np.floor(q).astype(int); t = q - i0; t = t * t * (3 - 2 * t); i1 = (i0 + 1) % N; i0 = i0 % N; v = VOL[i]
    c = lambda x, y, z: v[x, y, z]
    x0, y0, z0 = i0.T; x1, y1, z1 = i1.T; tx, ty, tz = t.T
    return ((c(x0, y0, z0) * (1 - tx) + c(x1, y0, z0) * tx) * (1 - ty) + (c(x0, y1, z0) * (1 - tx) + c(x1, y1, z0) * tx) * ty) * (1 - tz) + \
           ((c(x0, y0, z1) * (1 - tx) + c(x1, y0, z1) * tx) * (1 - ty) + (c(x0, y1, z1) * (1 - tx) + c(x1, y1, z1) * tx) * ty) * tz


BODY = np.array([0x23, 0x1c, 0x24], np.float32) / 255
RUST = np.array([0x4a, 0x2c, 0x16], np.float32) / 255
SCUFF = np.array([0x52, 0x4e, 0x52], np.float32) / 255
RESID = np.array([0x3c, 0x34, 0x3a], np.float32) / 255
OIL = np.array([0x0e, 0x0b, 0x10], np.float32) / 255
# peeled-sticker residue ghosts on the back: (x0, x1, z0, z1) metres
GHOSTS = [(-0.28, -0.12, 0.30, 0.46), (-0.05, 0.15, 0.60, 0.78), (0.10, 0.30, 0.25, 0.38), (-0.22, -0.02, 0.95, 1.08), (0.05, 0.28, 1.15, 1.30), (-0.30, -0.15, 1.40, 1.50)]
out = np.tile(BODY, (H, W, 1)); done = np.zeros((H, W), bool)
for ti in range(len(tv)):
    luv = uv[tris[ti]] * [W, H]
    lo = np.floor(luv.min(0)).astype(int) - 1; hi = np.ceil(luv.max(0)).astype(int) + 1
    xs, ys = np.meshgrid(np.arange(lo[0], hi[0] + 1), np.arange(lo[1], hi[1] + 1)); q = np.stack([xs + .5, ys + .5], -1).reshape(-1, 2)
    a0, b0, c0 = luv; d = (b0[1] - c0[1]) * (a0[0] - c0[0]) + (c0[0] - b0[0]) * (a0[1] - c0[1])
    if abs(d) < 1e-9: continue
    w0 = ((b0[1] - c0[1]) * (q[:, 0] - c0[0]) + (c0[0] - b0[0]) * (q[:, 1] - c0[1])) / d
    w1 = ((c0[1] - a0[1]) * (q[:, 0] - c0[0]) + (a0[0] - c0[0]) * (q[:, 1] - c0[1])) / d
    ok = (w0 >= -0.02) & (w1 >= -0.02) & (1 - w0 - w1 >= -0.02)
    if not ok.any(): continue
    w = np.stack([w0, w1, 1 - w0 - w1], 1)[ok]; qq = q[ok]
    p = w @ vco[tv[ti]]; n = w @ nrm[ti]; n /= np.linalg.norm(n, axis=1, keepdims=True) + 1e-9
    pw = p + 0.05 * (np.stack([noise(1, p + o, (7, 7, 7)) for o in (0.0, 3.1, 7.7)], 1) - 0.5)   # domain warp: no axis-aligned value-noise blockiness
    n1 = noise(0, pw, (3, 3, 3)); n2 = noise(1, pw, (11, 11, 11)); n3 = noise(2, pw, (38, 38, 38)); n4 = noise(3, pw, (55, 55, 55))
    drip = noise(4, pw, (30, 30, 2.5))                              # long vertical streaks
    z = p[:, 2]
    ss = lambda x, lo, hi: (lambda t: t * t * (3 - 2 * t))(np.clip((x - lo) / (hi - lo), 0, 1))
    col = BODY[None] * (0.74 + 0.55 * n1)[:, None] * (0.93 + 0.14 * n3)[:, None]      # mottled paint
    col = col * (1 - 0.42 * ss(drip, 0.55, 0.82))[:, None]                             # dark drips, soft edged
    under = n[:, 2] < -0.7; back = n[:, 1] > 0.7
    rw = np.clip((0.5 - z) / 0.5, 0, 1) * ss(n2, 0.4, 0.8) * (0.45 + 0.1 * under)          # rust creeps up from the foot (B2: much less on the underside, which should read as the +X body: dark charcoal, fine grain, scratches)
    col = col * (1 - rw[:, None] * 0.65) + RUST[None] * rw[:, None] * 0.65 * (0.75 + 0.5 * n3)[:, None]
    oil = ss(n1, 0.62, 0.88) * (0.35 + 0.15 * under)                                      # dark oily pools, mostly low and under
    col = col * (1 - oil[:, None] * 0.65) + OIL[None] * oil[:, None] * 0.65
    # B2: full-atlas-resolution fine grain, crisp thin scratches and pits (the first pass was soft, blotchy blobs)
    g1 = noise(5, p, (150, 150, 150)); g2 = noise(6, p, (330, 330, 330))
    col = col * (0.88 + 0.16 * g1 + 0.12 * g2)[:, None]
    sc = np.zeros(len(p), np.float32)
    dlt = 0.002
    for (ax, fq) in ((0, (110, 3, 3)), (2, (3, 3, 110))):                                  # hairline scratches: noise iso-lines of CONSTANT width (width = |n-0.5| / gradient)
        pa = pw + ax * 1.7
        na = noise(7, pa, fq); nb = noise(7, pa + dlt, fq); grad = np.abs(nb - na) / (dlt * 1.7) + 1e-3
        wm = np.abs(na - 0.5) / grad                                                       # distance to the line in metres
        sc = np.maximum(sc, ss(0.0009 - wm, 0, 0.0006) * ss(noise(8, pw, (7, 7, 7)), 0.6, 0.78))   # sparse: a coarse mask lets only some stretches show
    pit = ss(g2 - 0.9, 0, 0.05) * ss(n2, 0.3, 0.6)
    col = col * (1 - sc[:, None] * 0.5) + SCUFF[None] * (sc * 0.7)[:, None]                 # light scratches
    col = col * (1 - pit[:, None] * 0.5)                                                    # dark pits
    up = ss(n[:, 2], 0.25, 0.6)                                                              # up-facing shelves and ledges (the back shoulder at z 0.89 caught the sun as a flat pale wedge): dust- and oil-soaked, darker and grainier
    col = col * (1 - 0.8 * up)[:, None]
    col = np.where(back[:, None], col * 1.28, col)                                          # B2: back lifted a little so the wear reads in game light, still dark
    dd6 = np.sort(np.stack([p[:, 0] - bmin[0], bmax[0] - p[:, 0], p[:, 1] - bmin[1], bmax[1] - p[:, 1], p[:, 2] - bmin[2], bmax[2] - p[:, 2]], 1), 1)
    edge = dd6[:, 1]   # distance to the SECOND nearest bounding plane = distance to a box edge (the faces themselves sit on one plane: not edge wear)
    chip = ss(0.016 - edge, 0, 0.012) * ss(n4, 0.45, 0.7)                               # edge chips, bare metal
    col = col * (1 - chip[:, None] * 0.7) + SCUFF[None] * chip[:, None] * 0.7
    for gx0, gx1, gz0, gz1 in GHOSTS:                                                   # peeled sticker residue on the back
        dd = np.minimum.reduce([p[:, 0] - gx0, gx1 - p[:, 0], z - gz0, gz1 - z])
        ins = back * np.clip(dd / 0.012 + (n2 - 0.5) * 1.6, 0, 1) * ss(n3 + 0.4 * n2, 0.25, 0.6)
        col = col * (1 - ins[:, None] * 0.5) + RESID[None] * (ins * (0.75 + 0.5 * n4))[:, None] * 0.5
    out[np.clip(qq[:, 1].astype(int), 0, H - 1), np.clip(qq[:, 0].astype(int), 0, W - 1)] = np.clip(col, 0, 1)
    done[np.clip(qq[:, 1].astype(int), 0, H - 1), np.clip(qq[:, 0].astype(int), 0, W - 1)] = True
print("texels filled", int(done.sum()), "of", W * H)
ni = bpy.data.images.new("base_grime", W, H, alpha=True); ni.colorspace_settings.name = img.colorspace_settings.name
ni.pixels.foreach_set(np.dstack([out, np.ones((H, W), np.float32)]).ravel()); ni.update(); ni.file_format = "PNG"
node.image = ni
bpy.ops.export_scene.gltf(filepath=OUT, export_format="GLB", export_image_format="AUTO")
print("wrote", OUT)
