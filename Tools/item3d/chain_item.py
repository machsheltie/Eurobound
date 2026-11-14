"""Two thick glow sticks joined by ONE fat solid lace cord with ONE big knot, as one fused mesh (0 Tripo credits). Standing in the XZ plane, loose V.

blender -b --python Tools/item3d/chain_item.py -- <out.glb> <paint.png>
 Source: Assets/Graphics/items/glowstick-nunchucks.md sections 1-4. Sticks are plain bevelled cylinders; ALL their markings are painted flat colour
 (core stripe, darker pooled section, bold crack, black electrical tape, scuffs, grime), mapped around each stick's own axis.
 paint.png (1024 x 1280): green stick rect (0,0,1024,640), magenta stick rect (0,640,1024,1279). No motion dashes, no thin or detached parts.
 The cord is round, the same thickness end to end (cylinders plus spheres of one radius).
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import palette_mesh as pm
from mathutils import Vector

av = sys.argv[sys.argv.index("--") + 1:]
out, paint = os.path.abspath(av[0]), os.path.abspath(av[1])
pm.reset()
L, R, ANG = 0.66, 0.10, 32.0
ex = 0.27
cam = Vector((-0.469, -0.883, 0.0))        # local direction that faces the render camera after the 28 deg yaw


def stick(side, rect):
    a = math.radians(ANG) * side
    d = Vector((math.sin(a), 0.0, math.cos(a)))
    p0 = Vector((side * ex, 0.0, 0.0))
    ob = pm.prim("cyl", loc=p0 + d * (L / 2), rot=(0, math.degrees(a), 0), r=R, d=L, v=32)
    e1 = (cam - d * cam.dot(d)).normalized()
    pm.reg(pm.bevel(ob, 0.02, 2), paint={"mode": "axis", "rect": rect, "p0": p0, "d": d, "e1": e1, "tr": (0.0, L)})


stick(-1, (0, 0, 1024, 640))       # acid green: tape on its knot end
stick(+1, (0, 640, 1024, 1279))    # hot magenta: crack and pooled section
LACE, LACE_D = "E8E4D8", "B8B2A2"
N, CR = 14, 0.085
pts = [(-ex + 2 * ex * i / N, 0.0, -0.2 * math.sin(math.pi * i / N)) for i in range(N + 1)]
for (x0, y0, z0), (x1, y1, z1) in zip(pts, pts[1:]):
    ln = math.hypot(x1 - x0, z1 - z0)
    ang = math.degrees(math.atan2(x1 - x0, z1 - z0))
    pm.reg(pm.prim("cyl", loc=((x0 + x1) / 2, 0, (z0 + z1) / 2), rot=(0, ang, 0), r=CR, d=ln + 0.01, v=20), LACE)
for (x, y, z) in pts:
    pm.reg(pm.prim("sphere", loc=(x, 0, z), r=CR), LACE)
pm.reg(pm.prim("sphere", loc=(0, 0, -0.2), r=0.17, scale=(1.15, 1.0, 0.9)), LACE_D)   # the one big knot
pm.finish(out, paint_png=paint)
