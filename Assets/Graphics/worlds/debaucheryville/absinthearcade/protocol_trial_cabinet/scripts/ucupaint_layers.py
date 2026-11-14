"""Protocol step 8 fallback (ArmorPaint is not used, author ruling nhxz-q3): Ucupaint layer scaffold in Blender, attempted headless.
Imports the trial GLB, enables the Ucupaint extension (bl_ext.blender_org.ucupaint), adds its node group to the material, puts the projected base colour in as the
bottom layer and an EMPTY transparent layer on top named "distress_AUTHOR" for the author's hand-painted wear (3d_asset_rules.md: the author paints all distress).
Ucupaint's operators expect a Shader Editor context; this script borrows one from the default UI screen. If the borrow fails, the failure is printed and no .blend is written.
blender -b --factory-startup --python ucupaint_layers.py -- <trial.glb> <basecolor.png> <out.blend>"""
import bpy, sys, traceback
a = sys.argv[sys.argv.index("--") + 1:]
GLB, BASE, OUT = a
bpy.ops.preferences.addon_enable(module="bl_ext.blender_org.ucupaint")
print("ucupaint enabled:", "bl_ext.blender_org.ucupaint" in bpy.context.preferences.addons)
bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete()
bpy.ops.import_scene.gltf(filepath=GLB)
ob = [o for o in bpy.data.objects if o.type == "MESH"][0]
bpy.context.view_layer.objects.active = ob; ob.select_set(True)
mat = ob.data.materials[0]
area = None
for scr in bpy.data.screens:
    for ar in scr.areas:
        if ar.type == "NODE_EDITOR":
            area = ar; screen = scr; break
    if area: break
if area is None:
    for scr in bpy.data.screens:
        if scr.areas:
            area = scr.areas[0]; screen = scr; break
    area.type = "NODE_EDITOR"
sp = area.spaces.active
sp.tree_type = "ShaderNodeTree"; sp.shader_type = "OBJECT"; sp.pin = False
reg = [r for r in area.regions if r.type == "WINDOW"][0]
try:
    with bpy.context.temp_override(area=area, space_data=sp, region=reg, screen=screen, object=ob, active_object=ob):
        r = bpy.ops.wm.y_add_new_ypaint_node()
        print("add yp node:", r)
        r = bpy.ops.wm.y_open_image_as_layer(filepath=BASE, relative_path=False)
        print("base layer:", r)
        r = bpy.ops.wm.y_new_layer(name="distress_AUTHOR", type="IMAGE", color=(0, 0, 0, 0), width=2048, height=2048)
        print("distress layer:", r)
    grp = [n for n in mat.node_tree.nodes if n.type == "GROUP"]
    yp = grp[0].node_tree.yp if grp else None
    print("layers:", [l.name for l in yp.layers] if yp else None)
    bpy.ops.wm.save_as_mainfile(filepath=OUT)
    print("ucupaint scaffold saved", OUT)
except Exception:
    traceback.print_exc()
    print("UCUPAINT HEADLESS FAILED")
