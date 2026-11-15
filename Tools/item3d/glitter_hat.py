"""Build the Used Glitter Hat: a five-point plastic party crown ring, two curly flat streamers, a limp elastic (0 Tripo credits).

blender -b --python Tools/item3d/glitter_hat.py -- <out.glb> <paint.png>
 paint.png (2048 x 320, made by glitter_hat_paint.py): cyl rect (0,0,2048,320) over z 0..ZTOP. Glitter, gems, stains are painted, not geometry.
 Points peak at model angles -118 + 72k degrees, so with the render yaw of 28 the first one faces the camera.
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy, bmesh
import palette_mesh as pm

out, paint = [os.path.abspath(a) for a in sys.argv[sys.argv.index("--") + 1:][:2]]
pm.reset()
BASE, AMP, ZTOP, T = 0.12, 0.34, 0.46, 0.028
P0 = -118.0
N = 360
TILT = -12.0
LEAN_PT, LEAN = 1, 0.07            # the bent point (index) and how far its upper part leans outward


def f_prof(theta):
    ph = ((math.degrees(theta) - P0) / 72.0 + 0.5) % 1.0
    tri = 1.0 - abs(2 * ph - 1)
    u, c = 1.0 - tri, 0.22                                  # zigzag: straight flanks, rounded tips, sharp valleys
    return 1.0 - u * u / (2 * c) if u < c else 1.0 - u + c / 2


def r_out(z):
    return 0.5 - 0.10 * z / ZTOP


bm = bmesh.new()
rows = []
for i in range(N):
    th = -math.pi + 2 * math.pi * i / N
    ztop = BASE + AMP * f_prof(th)
    lean = 0.0
    d = ((math.degrees(th) - (P0 + 72 * LEAN_PT) + 180) % 360) - 180
    if abs(d) < 36:
        lean = LEAN * math.cos(math.radians(d) * 90 / 36) ** 2

    def pt(r, z, extra=0.0):
        rr = r + extra * max(0.0, (z - BASE)) / AMP
        return bm.verts.new((rr * math.cos(th), rr * math.sin(th), z))
    A = pt(r_out(0), 0); B = pt(r_out(ztop), ztop, lean)
    C = pt(r_out(ztop) - T, ztop, lean); D = pt(r_out(0) - T, 0)
    rows.append((A, B, C, D))
for i in range(N):
    a, b = rows[i], rows[(i + 1) % N]
    for k in range(4):
        bm.faces.new((a[k], a[(k + 1) % 4], b[(k + 1) % 4], b[k]))
bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
me = bpy.data.meshes.new("crown"); bm.to_mesh(me); bm.free()
crown = bpy.data.objects.new("crown", me); bpy.context.collection.objects.link(crown)
pm.reg(crown, paint={"mode": "cyl", "rect": (0, 0, 2048, 320), "zr": (0, ZTOP)})


def strip(path, w, th, name):
    """path: list of (x, y, z); flat ribbon: width w in the XZ plane, thickness th along Y. Closed rectangular tube."""
    bm = bmesh.new(); secs = []
    for i, (x, y, z) in enumerate(path):
        p0, p1 = path[max(i - 1, 0)], path[min(i + 1, len(path) - 1)]
        tx, tz = p1[0] - p0[0], p1[2] - p0[2]
        L = math.hypot(tx, tz) or 1.0
        nx, nz = -tz / L, tx / L
        c = []
        for sx, sy in ((1, 1), (1, -1), (-1, -1), (-1, 1)):
            c.append(bm.verts.new((x + sx * nx * w / 2, y + sy * th / 2, z + sx * nz * w / 2)))
        secs.append(c)
    for i in range(len(secs) - 1):
        for k in range(4):
            bm.faces.new((secs[i][k], secs[i][(k + 1) % 4], secs[i + 1][(k + 1) % 4], secs[i + 1][k]))
    bm.faces.new(secs[0][::-1]); bm.faces.new(secs[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    m = bpy.data.meshes.new(name); bm.to_mesh(m); bm.free()
    ob = bpy.data.objects.new(name, m); bpy.context.collection.objects.link(ob)
    return ob


def curl(tip, side, L=0.42, a=0.05, n=2.5, steps=70):
    pts = []
    for i in range(steps + 1):
        s = i / steps
        ph = 2 * math.pi * n * s
        pts.append((tip[0] + side * (0.09 + a * math.sin(ph)), tip[1], tip[2] - 0.03 - L * s - 0.0))
    return pts


for k, col, side in ((-1, "FF6EC7", -1), (1, "9370DB", 1)):          # flank points of the front point (index 0)
    ang = math.radians(P0 + 72 * k)
    r = r_out(ZTOP)
    tip = (r * math.cos(ang), r * math.sin(ang) + math.sin(ang) * 0.03, BASE + AMP * 0.80)
    path = curl(tip, side)
    pm.reg(strip(path, 0.06, 0.024, "streamer"), col)
    if col == "9370DB":                                                 # dark brown stain near the purple streamer's tip
        q = path[-9]
        pm.reg(pm.prim("sphere", loc=(q[0], q[1] - 0.012, q[2]), scale=(1.0, 0.3, 1.6), r=0.036), "7A5C3A")

ang = math.radians(P0 + 36)                                           # elastic: right front valley, hangs below the rim, stretched
ex, ey = 0.455 * math.cos(ang), 0.455 * math.sin(ang) - 0.02
el = [(ex + 0.09 * math.sin(math.pi * s) + 0.05 * s, ey, 0.05 - 0.28 * s) for s in [i / 30 for i in range(31)]]
pm.reg(strip(el, 0.05, 0.026, "elastic"), "A9A9B2")
pm.finish(out, paint_png=paint, tilt=TILT)
