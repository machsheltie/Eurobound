"""Clock Snow Globe (clock_snow_globe): opaque fused toon mesh, 0 Tripo credits (brief: design/items/debaucheryville_items/clock_snow_globe_item.md).

blender -b --python Tools/item3d/snow_globe.py -- <out.glb> <paint.png>     (paint.png from snow_globe_paint.py)
The toon render is opaque, so the glass is a BACK-HALF shell painted murky aqua (open toward the camera) plus a teal outline arch along the
silhouette, a pale glass rim ring and a white highlight arc. The tower, snow and bubble sit in front of the shell. Everything is built facing -Y
and turned -28 deg at the end so the hex base's front face points at the icon camera (yaw 28).
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bpy, bmesh
import palette_mesh as pm
from mathutils import Vector, Matrix

out, paint = os.path.abspath(sys.argv[sys.argv.index("--") + 1]), os.path.abspath(sys.argv[sys.argv.index("--") + 2])
pm.reset()
random.seed(3)
ALL = []


def R(ob, hexc=None, paint=None):
    pm.reg(ob, hexc, paint)
    ALL.append(ob)
    return ob


def xf(ob, M):
    ob.data.transform(M @ ob.matrix_basis)
    ob.matrix_basis = Matrix.Identity(4)


def tube(pts, r, n=6, name="tube"):
    bm = bmesh.new()
    rings = []
    for i, p in enumerate(pts):
        t = (pts[min(i + 1, len(pts) - 1)] - pts[max(i - 1, 0)]).normalized()
        a = Vector((0, 0, 1)) if abs(t.z) < 0.9 else Vector((1, 0, 0))
        u = t.cross(a).normalized(); v = t.cross(u).normalized()
        rings.append([bm.verts.new(p + (u * math.cos(2 * math.pi * k / n) + v * math.sin(2 * math.pi * k / n)) * r) for k in range(n)])
    for i in range(len(rings) - 1):
        for k in range(n):
            bm.faces.new((rings[i][k], rings[i][(k + 1) % n], rings[i + 1][(k + 1) % n], rings[i + 1][k]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    return ob


H_BASE, ZC, RX, RZ = 0.35, 0.45, 0.29, 0.47
T0 = -math.asin((ZC - H_BASE) / RZ)


def egg(t):   # slightly wobbly egg, taller than wide
    return RX * math.cos(t) * (1 + 0.014 * math.sin(3 * t + 1.0)), ZC + RZ * math.sin(t)


# ------------------------------------------------------------------ felt pad + price sticker
R(pm.lathe([(0, -0.028), (0.43, -0.028), (0.43, 0.0), (0, 0.0)], 6, "pad"), "4A3B2C")
R(pm.prim("cube", loc=(-0.12, -0.395, -0.014), scale=(0.12, 0.07, 0.01)), "F2EEE4")
R(pm.prim("cube", loc=(-0.12, -0.402, -0.014), scale=(0.075, 0.016, 0.012)), "6E6A66")        # the single printed stroke
R(pm.prim("cube", loc=(0.30, -0.36, -0.022), scale=(0.1, 0.06, 0.02)), "4A3B2C")
# ------------------------------------------------------------------ hex resin base (painted wall: scene + lettering band)
prof = [(0, 0), (0.42, 0), (0.42, 0.05), (0.37, 0.05), (0.37, 0.30), (0.40, 0.30), (0.40, H_BASE), (0.0, H_BASE)]
R(pm.lathe(prof, 6, "base"), paint={"mode": "cyl", "rect": (0, 0, 2048, 340), "zr": (0.0, 0.36)})
# ------------------------------------------------------------------ dome back shell (front half removed), rim ring, outline arch, highlight
N = 48
steps = 14
dp = [egg(T0 + (math.pi / 2 - T0) * i / steps) for i in range(steps)] + [(0.0, ZC + RZ)]
shell = pm.lathe(dp, N, "shell")
bm = bmesh.new(); bm.from_mesh(shell.data)
bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.calc_center_median().y < -1e-6], context='FACES')
bm.to_mesh(shell.data); bm.free()
R(shell, paint={"mode": "cyl", "rect": (0, 340, 2048, 910), "zr": (H_BASE, ZC + RZ)})
R(pm.prim("torus", loc=(0, 0, H_BASE + 0.012), R=0.292, r=0.03, v=36, mv=10), "CFE3E2")           # thick glass rim
arch = []
for sgn in (-1, 1):
    seq = [T0 + (math.pi / 2 - T0) * i / 24 for i in range(25)]
    seq = seq if sgn == -1 else seq[::-1]
    for t in seq:
        r, z = egg(t)
        arch.append(Vector((sgn * r * 1.012, 0.0, z)))
R(tube(arch, 0.011, 6, "arch"), "5F8F8B")
hl = []
for i in range(13):                                    # white glint arc on the upper-left front glass
    t = math.radians(22 + i * 3.6); az = math.radians(-90 - 58 + i * 1.3)
    r, z = egg(t)
    hl.append(Vector((r * 1.03 * math.cos(az), r * 1.03 * math.sin(az), z)))
R(tube(hl, 0.009, 6, "glint"), "FFFFFF")
t = math.radians(12); az = math.radians(-90 - 62 - 4); r, z = egg(t)
R(pm.prim("sphere", loc=(r * 1.03 * math.cos(az), r * 1.03 * math.sin(az), z), r=0.017), "FFFFFF")
# the bubble stuck at the top, and the dead glitter stuck to the glass above the waterline
R(pm.prim("sphere", loc=(0.01, -0.012, 0.888), r=0.034), "5F8F8B")
R(pm.prim("sphere", loc=(0.01, -0.03, 0.885), r=0.027), "E1F0EF")
r, z = egg(math.radians(55)); az = math.radians(60)
R(pm.prim("sphere", loc=(r * 0.96 * math.cos(az), r * 0.96 * math.sin(az), z), r=0.016), "B8912F")
# ------------------------------------------------------------------ snow floor + mounds + flakes + gold clump
R(pm.prim("cyl", loc=(0, 0, H_BASE + 0.012), r=0.275, d=0.03, v=36), "F5F5F0")
for (x, y, sx, sy) in ((0.0, -0.03, 0.14, 0.07), (-0.15, -0.07, 0.07, 0.04), (0.15, -0.09, 0.06, 0.04), (0.10, -0.17, 0.05, 0.03), (-0.08, -0.19, 0.05, 0.03)):
    R(pm.prim("sphere", loc=(x, y, H_BASE + 0.02), scale=(sx / 0.05, sy / 0.05, 0.9), r=0.05), "F5F5F0")
for (x, y, z) in ((-0.14, -0.15, .70), (0.17, -0.10, .62), (-0.19, -0.02, .55), (0.2, 0.02, .74), (-0.09, -0.20, .80), (0.06, -0.20, .66),
                  (-0.2, -0.12, .45), (0.12, -0.22, .50), (-0.12, -0.23, .72), (0.22, -0.16, .84), (-0.17, -0.19, .88), (0.0, -0.17, .78),
                  (-0.22, 0.05, .65), (0.24, -0.02, .56)):
    R(pm.prim("sphere", loc=(x, y, z), r=0.014), "F5F5F0")
for (x, y, z) in ((0.13, -0.19, .60), (0.15, -0.19, .62), (0.12, -0.2, .625), (0.145, -0.205, .595), (0.165, -0.19, .59)):   # clumped suspended glitter
    R(pm.prim("cube", loc=(x, y, z), rot=(20, 30, 10), scale=(0.02, 0.02, 0.02)), "B8912F")
for (x, y) in ((-0.1, -0.12), (0.2, -0.04), (0.04, -0.21)):                                # gold clump settled on the floor
    R(pm.prim("cube", loc=(x, y, H_BASE + 0.035), rot=(0, 0, 25), scale=(0.022, 0.022, 0.016)), "B8912F")
# ------------------------------------------------------------------ the tower (leans 3 degrees), built then leaned about its foot
T = []


def tw(ob, hexc):
    T.append(ob)
    return R(ob, hexc)


ZB = H_BASE + 0.01
tw(pm.bevel(pm.prim("cube", loc=(0, 0, ZB + 0.125), scale=(0.17, 0.17, 0.25)), 0.006, 2), "6E6A66")
tw(pm.prim("cone", loc=(0, 0, ZB + 0.25 + 0.085), rot=(0, 0, 45), r=0.125, d=0.17, v=4), "6E6A66")
tw(pm.prim("cube", loc=(0, 0, ZB + 0.255), scale=(0.195, 0.195, 0.018)), "F5F5F0")             # snow on the tower's shoulders
tw(pm.prim("sphere", loc=(0, 0, ZB + 0.005), scale=(2.6, 2.6, 0.5), r=0.05), "F5F5F0")           # snow at its foot
tw(pm.prim("cyl", loc=(-0.02, -0.091, ZB + 0.19), rot=(90, 0, 0), r=0.062, d=0.016, v=24), "CFB53B")
tw(pm.prim("cyl", loc=(-0.02, -0.1, ZB + 0.19), rot=(90, 0, 0), r=0.047, d=0.016, v=24), "2E4A7A")
tw(pm.prim("cube", loc=(-0.02, -0.109, ZB + 0.205), scale=(0.011, 0.01, 0.034)), "CFB53B")      # stubby hands
tw(pm.prim("cube", loc=(0.0, -0.109, ZB + 0.19), scale=(0.034, 0.01, 0.011)), "CFB53B")
for x in (-0.065, -0.025):                                                                      # two tiny shut apostle windows
    tw(pm.prim("cube", loc=(x, -0.088, ZB + 0.085), scale=(0.026, 0.008, 0.05)), "3F3C3A")
tw(pm.prim("cube", loc=(0.058, -0.088, ZB + 0.135), scale=(0.03, 0.008, 0.045)), "3F3C3A")      # window above the skeleton
tw(pm.prim("sphere", loc=(0.058, -0.095, ZB + 0.14), r=0.018), "D4A017")                       # rooster gold comma
tw(pm.prim("cone", loc=(0.058, -0.095, ZB + 0.162), rot=(0, 10, 0), r=0.012, d=0.03, v=6), "D4A017")
tw(pm.prim("sphere", loc=(0.078, -0.098, ZB + 0.075), r=0.026), "E8E4D8")                      # bone-white skeleton blob
tw(pm.prim("sphere", loc=(0.078, -0.098, ZB + 0.03), scale=(1, 0.8, 1.4), r=0.022), "E8E4D8")
tw(pm.prim("cone", loc=(0.045, -0.105, ZB + 0.045), r=0.013, d=0.025, v=6), "D4A017")           # speck of an hourglass
lean = Matrix.Translation((0, 0, H_BASE)) @ Matrix.Rotation(math.radians(3), 4, 'Y') @ Matrix.Translation((0, 0, -H_BASE))
for ob in T:
    xf(ob, lean)
# ------------------------------------------------------------------ turn the whole model so the hex front faces the icon camera
rot = Matrix.Rotation(math.radians(-28), 4, 'Z')
for ob in ALL:
    xf(ob, rot)
pm.finish(out, paint_png=paint, smooth_deg=35, rough=0.8)
