"""Lathe a chunky OPAQUE shot glass (satin tint, opaque liquid top, no transparency) as one fused mesh (0 Tripo credits).

blender -b --python Tools/item3d/lathe_item.py -- <kind: absinthe|plain> <out.glb> [liquid_hex] [body_hex]
 - glass: thick walls, heavy base, lathed from an (r, z) profile (plate_slab.py approach), satin pale tint #C4D8DC
 - liquid: opaque top disc inside the rim plus a body-colour band over the lower wall
 - absinthe: adds stained coaster, green spill ring, coffee ring, tarnished slotted spoon across the rim, sugar cube,
   caramel drips, a hard 3-band flame (blue/orange/yellow cones) and a stepped smoke curl.
   Colours from Assets/Graphics/items/absinthe-shot.md section 4.
 - plain: the glass alone (The Tan Line Neon Shooter), liquid colour given on the command line
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import palette_mesh as pm

argv = sys.argv[sys.argv.index("--") + 1:]
kind, out = argv[0], os.path.abspath(argv[1])
LIQ = argv[2] if len(argv) > 2 else "6EE81E"
BODY = argv[3] if len(argv) > 3 else LIQ
pm.reset()

H = 0.56
def r_out(z): return 0.24 + 0.06 * (z - 0.03) / (H - 0.03)
def r_in(z): return 0.19 + 0.045 * (z - 0.18) / (H - 0.18)

glass = [(0, 0), (0.2, 0), (0.232, 0.012), (r_out(0.03), 0.03), (r_out(H), H), (r_out(H) - 0.012, H + 0.014),
         (r_in(H) + 0.012, H + 0.014), (r_in(H), H), (r_in(0.18), 0.18), (0.17, 0.15), (0, 0.14)]
pm.reg(pm.lathe(glass, 48, "glass"), "C4D8DC")
FILL = 0.42
# body-colour band hugging the lower outer wall (the liquid seen through satin glass), opaque
band = [(r_out(0.13) - 0.02, 0.13), (r_out(0.13) + 0.005, 0.13), (r_out(FILL) + 0.005, FILL), (r_out(FILL) - 0.02, FILL)]
pm.reg(pm.lathe(band, 48, "body"), BODY)
pm.reg(pm.prim("cyl", loc=(0, 0, FILL + 0.012), r=r_in(FILL) - 0.002, d=0.026, v=48), LIQ)

if kind == "absinthe":
    pm.reg(pm.prim("cyl", loc=(0, 0, -0.03), r=0.52, d=0.06, v=48), "E8E4D8")                       # coaster
    pm.reg(pm.lathe([(0.27, 0.0), (0.27, 0.012), (0.37, 0.012), (0.37, 0.0)], 48, "spill"), "3A9E0A")  # green spill ring
    pm.reg(pm.lathe([(0.43, 0.0), (0.43, 0.012), (0.485, 0.012), (0.485, 0.0)], 48, "coffee"), "7E6244")  # coffee ring stain
    pm.reg(pm.prim("cyl", loc=(0.22, -0.30, 0.006), r=0.07, d=0.012, scale=(1.4, 0.8, 1), v=24), "A87C3A")  # sticky blot
    ZS = H + 0.014                                                                                 # spoon rests on the rim
    pm.reg(pm.prim("cube", loc=(0, 0, ZS + 0.02), scale=(0.86, 0.09, 0.04)), "7E6244")
    bowl = pm.prim("cyl", loc=(0, 0, ZS + 0.02), r=0.5, d=0.04, scale=(0.44, 0.30, 1), v=40)
    for y in (-0.085, 0.0, 0.085):
        bowl = pm.difference(bowl, pm.prim("cube", loc=(0, y, ZS + 0.02), scale=(0.34, 0.034, 0.3)))
    pm.reg(bowl, "7E6244")
    cube = pm.prim("cube", loc=(0, 0, ZS + 0.04 + 0.11), rot=(0, 0, 14), scale=(0.22, 0.22, 0.22))
    pm.reg(pm.bevel(cube, 0.012, 2), "E8E4D8")
    for (x, y) in ((0.03, 0.085), (-0.06, -0.085)):                                                  # caramel drips through the slots
        pm.reg(pm.prim("cyl", loc=(x, y, (ZS + 0.02 + FILL) / 2 + 0.01), r=0.017, d=ZS - FILL, v=10), "A87C3A")
    zf = ZS + 0.04 + 0.22
    pm.reg(pm.prim("cone", loc=(0, 0, zf + 0.06), r=0.15, d=0.12, v=6), "3E7EE8")
    pm.reg(pm.prim("cone", loc=(0, 0, zf + 0.10), r=0.11, d=0.20, v=6), "F0A418")
    pm.reg(pm.prim("cone", loc=(0, 0, zf + 0.13), r=0.07, d=0.26, v=6), "F8E86E")
    for i in range(3):                                                                             # stepped smoke curl
        pm.reg(pm.prim("cube", loc=(0.10 + 0.055 * i, 0, zf + 0.30 + 0.06 * i), scale=(0.05, 0.05, 0.05)), "6E5F72")
pm.finish(out)
