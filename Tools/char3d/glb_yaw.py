"""Rotate every root object of a GLB about Z (degrees) and re-export, so a Tripo model with face_yaw faces -Y for
project_ref.py, which only projects along the axes (Eurobound-8c3z). blender -b --factory-startup --python tools/char3d/glb_yaw.py -- <in.glb> <out.glb> <deg>
"""
import bpy, sys, math
from mathutils import Matrix
glb, out, yaw = sys.argv[sys.argv.index("--") + 1:][:3]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
for o in bpy.data.objects:
    print("OBJ", o.name, o.type, o.parent.name if o.parent else None, len(o.data.vertices) if o.type == "MESH" else "")
    if o.parent is None:
        o.matrix_world = Matrix.Rotation(math.radians(float(yaw)), 4, "Z") @ o.matrix_world
bpy.ops.export_scene.gltf(filepath=out, export_format="GLB", export_animations=True, export_skins=True, export_image_format="AUTO", export_jpeg_quality=95)
