# Headless check of the Claude Notes addon. Prints a handful of lines and exits 1 on failure.
#
#   blender --background --factory-startup --python Tools/blender_notes/test_headless.py -- <empty queue folder>
#
# With --gui after the folder (and no --background) it instead waits for the window
# to draw, sends one note with a real screenshot, and quits Blender.
import json
import os
import sys
import traceback

import bpy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ARGS = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
QUEUE = os.path.abspath(ARGS[0]) if ARGS else None
GUI = "--gui" in ARGS


def newest(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".json")]
    files.sort(key=os.path.getmtime)  # several notes can share one second, so not by name
    with open(files[-1], encoding="utf-8") as handle:
        return json.load(handle), len(files)


def send(note):
    bpy.context.window_manager.claude_notes_text = note
    result = bpy.ops.claude_notes.send()
    assert result == {"FINISHED"}, result
    entry, _count = newest(QUEUE)
    assert entry["note"] == note and entry["status"] == "pending" and entry["schema"] == 1
    for key in ("id", "created", "blend_path", "mode", "objects", "selection_bbox_world", "screenshot"):
        assert key in entry, key
    return entry


def background_checks():
    import claude_notes

    claude_notes.register()
    assert hasattr(bpy.types, "CLAUDENOTES_PT_panel") and hasattr(bpy.ops.claude_notes, "send")
    print("TEST register: ok (Blender %s)" % bpy.app.version_string)

    cube = bpy.data.objects["Cube"]
    bpy.ops.object.select_all(action="DESELECT")
    cube.select_set(True)
    bpy.context.view_layer.objects.active = cube

    # 1. Object mode
    entry = send("object mode note: make the cube less boring")
    assert entry["mode"] == "OBJECT" and entry["objects"][0]["name"] == "Cube"
    assert entry["selection_bbox_world"]["size"] == [2.0, 2.0, 2.0], entry["selection_bbox_world"]
    assert entry["screenshot"] is None and "background" in entry["screenshot_error"]
    assert entry["blend_path"] is None
    print("TEST object mode: ok (screenshot skipped: background)")

    # 2. Edit mode, one face
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.ops.object.mode_set(mode="OBJECT")
    cube.data.polygons[0].select = True
    bpy.ops.object.mode_set(mode="EDIT")
    entry = send("edit mode note: this face, with unicode é✓")
    sel = entry["objects"][0]["selection"]
    assert entry["mode"] == "EDIT_MESH"
    assert sel["faces"] == {"count": 1, "total": 6, "truncated": False, "encoding": "list", "indices": [0]}, sel
    assert sel["vertices"]["count"] == 4 and len(sel["vertices"]["indices"]) == 4
    assert sorted(sel["bbox_world"]["size"]) == [0.0, 2.0, 2.0], sel["bbox_world"]
    assert sel["materials"] == ["Material"], sel["materials"]
    print("TEST edit mode: ok (1 face, 4 verts, bbox %s)" % sel["bbox_world"]["size"])

    # 3. Huge selections: ranges, truncation, "all"
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.subdivide(number_cuts=20)  # 6 * 21 * 21 = 2646 faces
    entry = send("everything")
    sel = entry["objects"][0]["selection"]
    assert sel["faces"]["encoding"] == "all" and sel["faces"]["count"] == 2646, sel["faces"]
    claude_notes.MAX_INDICES, claude_notes.MAX_RANGES = 50, 40
    bpy.ops.mesh.select_all(action="DESELECT")
    bpy.context.tool_settings.mesh_select_mode = (False, False, True)  # faces, so the pattern survives
    bpy.ops.object.mode_set(mode="OBJECT")
    for poly in cube.data.polygons:
        poly.select = poly.index < 300 or poly.index % 3 == 0
    bpy.ops.object.mode_set(mode="EDIT")
    entry = send("big patchy selection")
    faces = entry["objects"][0]["selection"]["faces"]
    assert faces["encoding"] == "ranges" and faces["truncated"] and len(faces["ranges"]) == 40, faces
    assert faces["ranges"][0] == [0, 300] and "indices" not in faces, faces["ranges"][:2]
    size = os.path.getsize(os.path.join(QUEUE, entry["id"] + ".json"))
    print("TEST huge selection: ok (%d faces -> %d ranges of %d, file %d bytes)" % (
        faces["count"], len(faces["ranges"]), faces["range_count"], size))

    # 4. Empty note is refused, nothing written
    before = newest(QUEUE)[1]
    bpy.context.window_manager.claude_notes_text = "   "
    try:
        result = bpy.ops.claude_notes.send()
    except RuntimeError:
        result = {"CANCELLED"}
    assert result == {"CANCELLED"} and newest(QUEUE)[1] == before
    bpy.ops.object.mode_set(mode="OBJECT")
    claude_notes.unregister()
    assert not hasattr(bpy.types.WindowManager, "claude_notes_text")
    print("TEST empty note refused, unregister: ok (%d notes written)" % before)


def gui_check():
    import claude_notes

    claude_notes.register()
    state = {"tries": 0}

    def run():
        state["tries"] += 1
        code = 1
        try:
            window = bpy.context.window_manager.windows[0]
            area = next(a for a in window.screen.areas if a.type == "VIEW_3D")
            region = next(r for r in area.regions if r.type == "WINDOW")
            with bpy.context.temp_override(window=window, area=area, region=region):
                bpy.context.window_manager.claude_notes_text = "gui note with screenshot"
                assert bpy.ops.claude_notes.send() == {"FINISHED"}
            entry, _count = newest(QUEUE)
            png = os.path.join(QUEUE, entry["screenshot"] or "missing")
            with open(png, "rb") as handle:
                assert handle.read(8) == b"\x89PNG\r\n\x1a\n"
            print("TEST gui screenshot: ok (%s, %d bytes, view %s)" % (
                entry["screenshot"], os.path.getsize(png), entry["view"]["perspective"]))
            code = 0
        except Exception:
            traceback.print_exc()
            try:
                print("TEST gui screenshot: FAILED (%s)" % newest(QUEUE)[0].get("screenshot_error"))
            except Exception:
                print("TEST gui screenshot: FAILED")
        sys.stdout.flush()
        os._exit(code)  # hard exit so no window is ever left open

    bpy.app.timers.register(run, first_interval=4.0)


if __name__ == "__main__":
    if not QUEUE:
        print("TEST: pass an empty queue folder after --")
        sys.exit(1)
    os.makedirs(QUEUE, exist_ok=True)
    os.environ["CLAUDE_NOTES_QUEUE"] = QUEUE
    if GUI:
        gui_check()
    else:
        try:
            background_checks()
        except Exception:
            traceback.print_exc()
            print("TEST: FAILED")
            sys.exit(1)
        print("TEST: ALL OK")
