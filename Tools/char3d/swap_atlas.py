"""Copy the base-colour atlas of a projected GLB (same mesh and UVs) into another GLB and export; puts a texture painted on a
glb_yaw.py copy back on the original. blender -b --factory-startup --python tools/char3d/swap_atlas.py -- <src.glb> <dst.glb> <out.glb> <atlas.png>
"""
import bpy, sys
src, dst, out, png = sys.argv[sys.argv.index("--") + 1:][:4]
def base_img():
    for m in bpy.data.materials:
        if m.node_tree:
            for n in m.node_tree.nodes:
                if n.type == "BSDF_PRINCIPLED" and n.inputs["Base Color"].links:
                    return n.inputs["Base Color"].links[0].from_node
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=src)
im = base_img().image; im.filepath_raw = png; im.file_format = "PNG"; im.save()
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=dst)
node = base_img(); new = bpy.data.images.load(png); new.colorspace_settings.name = node.image.colorspace_settings.name
node.image = new
bpy.ops.export_scene.gltf(filepath=out, export_format="GLB", export_animations=True, export_skins=True, export_image_format="AUTO", export_jpeg_quality=92)
print("SWAPPED", out)
