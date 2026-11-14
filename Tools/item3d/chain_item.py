"""Two thick glow sticks joined by a chunky chain of fat links, as one fused mesh (0 Tripo credits). Standing in the XZ plane, loose V.

blender -b --python Tools/item3d/chain_item.py -- <out.glb>
 Source: Assets/Graphics/items/glowstick-nunchucks.md section 1-4. Doc: two thick glow sticks (acid green and hot magenta), flat saturated colour
 with a lighter core stripe, joined by a grubby off-white shoelace knotted at each end; one stick has a darker pooled section; black electrical
 tape on one knot; five spaced dashes arcing off one stick. The lace is built as fat chain-like links in the lace colour (the lead's chunky-chain
 brief, a thin lace would not survive 128 px).
 R1B: coordinator corrected the brief, the lace is ONE fat solid cord with ONE big knot, no links.
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import palette_mesh as pm

out = os.path.abspath(sys.argv[sys.argv.index("--") + 1])
pm.reset()
L, R, ANG = 0.66, 0.10, 32.0
ex = 0.27                                  # x of each stick's lower end
cam = (-0.469, -0.883)                      # local direction that faces the render camera after the 28 deg yaw


def stick(side, body, core, dark=None, tape=False):
    a = math.radians(ANG) * side
    dx, dz = math.sin(a), math.cos(a)       # unit vector along the stick, up and outward
    sx = -side * ex                          # side=+1 leans right; lower end sits on the opposite x so the V opens upward
    def at(t): return (sx * 0 + side * ex + dx * t, 0.0, dz * t)
    rot = (0, math.degrees(a), 0)           # cylinder axis z -> tilt about Y
    c = at(L / 2)
    body_ob = pm.prim("cyl", loc=c, rot=rot, r=R, d=L, v=28)
    pm.reg(pm.bevel(body_ob, 0.02, 2), body)
    off = (cam[0] * (R - 0.012), cam[1] * (R - 0.012), 0.0)
    pm.reg(pm.prim("cyl", loc=(c[0] + off[0], c[1] + off[1], c[2]), rot=rot, r=0.02, d=L * 0.86, v=10), core)
    if dark:
        t = L * 0.62
        p = at(t)
        pm.reg(pm.prim("cyl", loc=p, rot=rot, r=R + 0.007, d=0.15, v=28), dark)
    if tape:
        p = at(0.1)
        pm.reg(pm.prim("cyl", loc=p, rot=rot, r=R + 0.014, d=0.09, v=28), "1A1A1E")
    return at(L)


tip_g = stick(-1, "7EF018", "C4FF8E", dark="4A9E0A", tape=True)    # acid green, tape on its knot end, pooled darker section
tip_m = stick(+1, "F018A8", "FF8ED8", dark="9E0A66")               # hot magenta
LACE, LACE_D = "E8E4D8", "B8B2A2"
# ONE fat solid lace cord (thick tube, sagging between the stick ends) with one big chunky knot in the middle
N, CR = 14, 0.08
pts = [(-ex + 2 * ex * i / N, 0.0, -0.2 * math.sin(math.pi * i / N)) for i in range(N + 1)]
for (x0, y0, z0), (x1, y1, z1) in zip(pts, pts[1:]):
    mx, mz = (x0 + x1) / 2, (z0 + z1) / 2
    ln = math.hypot(x1 - x0, z1 - z0)
    ang = math.degrees(math.atan2(x1 - x0, z1 - z0))
    pm.reg(pm.prim("cyl", loc=(mx, 0, mz), rot=(0, ang, 0), r=CR, d=ln + 0.01, v=16), LACE)
for (x, y, z) in pts:
    pm.reg(pm.prim("sphere", loc=(x, 0, z), r=CR), LACE)
pm.reg(pm.prim("sphere", loc=(0, 0, -0.2), r=0.16, scale=(1.15, 1.0, 0.9)), LACE_D)   # the one big knot
# five spaced motion dashes arcing off the magenta stick's tip
cxm, czm = tip_m[0], tip_m[2]
for i in range(5):
    th = math.radians(-20 + i * 24)
    px, pz = cxm + 0.17 * math.sin(th) + 0.07, czm - 0.17 + 0.17 * math.cos(th) * 0.9 + 0.05
    pm.reg(pm.prim("cube", loc=(px, 0, pz), rot=(0, -math.degrees(th), 0), scale=(0.07, 0.025, 0.022)), "FF8ED8")
pm.finish(out)
