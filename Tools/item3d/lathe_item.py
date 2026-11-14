"""Lathe a chunky OPAQUE shot glass (satin tint, opaque liquid, no transparency) as one fused mesh with painted flat-colour art (0 Tripo credits).

blender -b --python Tools/item3d/lathe_item.py -- <kind: absinthe|shot> <out.glb> <paint.png>
 Art comes from dev/asset_team/icon_refs/b15_gen.py (Pillow). The glass wall is mapped around the Z axis (cyl), so the liquid colour, caramel
 drips, thumbprints, residue rings, scuffs are all flat painted areas, not geometry.
 - absinthe (Assets/Graphics/items/absinthe-shot.md): thick glass, coaster, FAT slotted tarnished spoon fused to the rim, sugar cube,
   two fat caramel strands, ONE solid teardrop flame (blue / orange / yellow bands painted by height). No smoke, nothing floating.
 - shot (The Tan Line Neon Shooter): tall narrow shot glass, 1.5 x taller than wide, heavy base, slightly flared walls.
 paint.png layout for absinthe (1024 x 1280): glass cyl rect (0,0,1024,512); coaster plane (0,512,512,1024); flame z-bands (512,512,768,768);
 spoon plane (0,1024,1024,1279). shot (1024 x 512): glass cyl rect (0,0,1024,512).
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import palette_mesh as pm
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:]
kind, out, paint = argv[0], os.path.abspath(argv[1]), os.path.abspath(argv[2])
pm.reset()

if kind == "absinthe":
    H = 0.56
    r_out = lambda z: 0.24 + 0.06 * (z - 0.03) / (H - 0.03)
    r_in = lambda z: 0.19 + 0.045 * (z - 0.18) / (H - 0.18)
    FILL = 0.42
    FLOOR = 0.18
    base_r = 0.2
else:
    H = 0.90
    r_out = lambda z: 0.27 + 0.03 * (z - 0.03) / (H - 0.03)
    r_in = lambda z: 0.20 + 0.04 * (z - 0.30) / (H - 0.30)
    FILL = 0.74
    FLOOR = 0.30
    base_r = 0.24
TOP = H + 0.014
glass = [(0, 0), (base_r, 0), (base_r + 0.032, 0.012), (r_out(0.03), 0.03), (r_out(H), H), (r_out(H) - 0.012, TOP),
         (r_in(H) + 0.012, TOP), (r_in(H), H), (r_in(FLOOR), FLOOR), (r_in(FLOOR) - 0.02, FLOOR - 0.03), (0, FLOOR - 0.04)]
pm.reg(pm.lathe(glass, 48, "glass"), paint={"mode": "cyl", "rect": (0, 0, 1024, 512), "zr": (0, TOP)})
pm.reg(pm.prim("cyl", loc=(0, 0, FILL + 0.012), r=r_in(FILL) - 0.002, d=0.026, v=48), "6EE81E" if kind == "absinthe" else "5B2BFF")

if kind == "absinthe":
    pm.reg(pm.prim("cyl", loc=(0, 0, -0.03), r=0.52, d=0.06, v=48),
           paint={"mode": "plane", "rect": (0, 512, 512, 1024), "ax": (0, 1), "bounds": (-0.52, 0.52, -0.52, 0.52)})
    ZB = TOP - 0.014                                   # spoon bar sunk into the rim: fused
    TH_S = 0.07
    bar = pm.prim("cube", loc=(0, 0, ZB + TH_S / 2), scale=(0.90, 0.16, TH_S))
    for x in (-0.27, -0.14, 0.14, 0.27):               # four bold slots
        bar = pm.difference(bar, pm.prim("cube", loc=(x, 0, ZB + TH_S / 2), scale=(0.08, 0.10, 0.5)))
    pm.reg(pm.bevel(bar, 0.008, 2), paint={"mode": "plane", "rect": (0, 1024, 1024, 1279), "ax": (0, 1), "bounds": (-0.45, 0.45, -0.08, 0.08)})
    ztop = ZB + TH_S
    cube = pm.prim("cube", loc=(0, 0, ztop + 0.095), rot=(0, 0, 8), scale=(0.19, 0.19, 0.19))
    pm.reg(pm.bevel(cube, 0.012, 2), "E8E4D8")
    for x in (-0.14, 0.14):                            # fat caramel strands through the slots
        pm.reg(pm.prim("cyl", loc=(x, 0, (ztop + FILL) / 2), r=0.03, d=ztop - FILL, v=12), "A87C3A")
    zf = ztop + 0.19 - 0.01                            # ONE solid teardrop flame fused to the cube top
    drop = [(0, 0), (0.12, 0.0), (0.145, 0.06), (0.13, 0.14), (0.09, 0.22), (0.05, 0.29), (0.025, 0.32), (0, 0.335)]
    fl = pm.lathe([(r, z + zf) for r, z in drop], 24, "flame")
    pm.reg(fl, paint={"mode": "z", "rect": (512, 512, 768, 768), "zr": (zf, zf + 0.335)})
pm.finish(out, paint_png=paint)
