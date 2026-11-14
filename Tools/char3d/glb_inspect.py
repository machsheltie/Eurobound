import bpy, sys
from mathutils import Vector
glb = sys.argv[sys.argv.index("--") + 1]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
for o in bpy.data.objects:
    print("OBJ", o.name, o.type, tuple(round(v, 3) for v in o.location), tuple(round(v, 3) for v in o.rotation_euler), tuple(round(v,3) for v in o.scale), "parent", o.parent.name if o.parent else None)
    if o.type == "MESH":
        print("  verts", len(o.data.vertices), "mats", [m.name for m in o.data.materials], "vgroups", len(o.vertex_groups))
        ws = [o.matrix_world @ v.co for v in o.data.vertices]
        mn = Vector((min(w.x for w in ws), min(w.y for w in ws), min(w.z for w in ws)))
        mx = Vector((max(w.x for w in ws), max(w.y for w in ws), max(w.z for w in ws)))
        print("  bbox", tuple(round(v, 3) for v in mn), tuple(round(v, 3) for v in mx))
    if o.type == "ARMATURE":
        for b in o.data.bones:
            h = o.matrix_world @ b.head_local
            t = o.matrix_world @ b.tail_local
            print("  BONE", b.name, "parent", b.parent.name if b.parent else None, tuple(round(v, 3) for v in h), tuple(round(v, 3) for v in t))
for a in bpy.data.actions:
    print("ACTION", a.name)
