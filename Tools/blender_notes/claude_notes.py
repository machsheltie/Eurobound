# Claude Notes: a Blender addon for the "last 10% of polish" loop (bead Eurobound-nhxz.4).
#
# In the 3D viewport sidebar (N key) > "Claude Notes" tab: select an object, or
# box-select a region in Edit Mode, type a note, click Send. The addon writes one
# JSON file (plus a viewport screenshot PNG) into a queue folder that a Claude
# session reads with Tools/blender_notes/list_notes.py.
#
# Written against Blender 5.2 (Python 3.13). Single file, no dependencies beyond
# what ships with Blender (bpy, numpy).

bl_info = {
    "name": "Claude Notes",
    "author": "Eurobound tools",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "3D Viewport > Sidebar (N) > Claude Notes",
    "description": "Select something, type a note, and queue it for a Claude session",
    "category": "3D View",
}

import datetime
import json
import os
import uuid

import bpy
import numpy as np

SCHEMA = 1
MAX_INDICES = 2000      # up to this many selected ids are written as a plain list
MAX_RANGES = 500        # above that, ids are written as [first, last] runs, capped here
MAX_OBJECTS = 200       # objects listed per note
SCREENSHOT_MAX_PX = 1600
QUEUE_ENV = "CLAUDE_NOTES_QUEUE"

_pending_cache = {"count": None}


# ----------------------------------------------------------------------------
# Queue folder
# ----------------------------------------------------------------------------

def queue_dir(context=None):
    """Folder the notes are written to, or None when it is not set up.

    Order: addon preference, then the CLAUDE_NOTES_QUEUE environment variable,
    then a 'queue' folder next to this file (when the addon runs from the repo).
    """
    context = context or bpy.context
    addon = context.preferences.addons.get(__name__)
    if addon is not None and addon.preferences is not None:
        path = (addon.preferences.queue_dir or "").strip()
        if path:
            return os.path.normpath(bpy.path.abspath(path))
    env = os.environ.get(QUEUE_ENV, "").strip()
    if env:
        return os.path.normpath(env)
    here = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(os.path.join(here, "list_notes.py")):
        return os.path.join(here, "queue")
    return None


def count_pending(context=None):
    path = queue_dir(context)
    if not path or not os.path.isdir(path):
        return 0
    return sum(1 for name in os.listdir(path) if name.endswith(".json"))


# ----------------------------------------------------------------------------
# Selection capture
# ----------------------------------------------------------------------------

def _r(values):
    return [round(float(v), 5) for v in values]


def _bbox(points):
    """points: (N, 3) array. Returns min/max/center/size, or None when empty."""
    if points is None or len(points) == 0:
        return None
    lo = points.min(axis=0)
    hi = points.max(axis=0)
    return {"min": _r(lo), "max": _r(hi), "center": _r((lo + hi) / 2.0), "size": _r(hi - lo)}


def _union(boxes):
    boxes = [b for b in boxes if b]
    if not boxes:
        return None
    pts = np.array([b["min"] for b in boxes] + [b["max"] for b in boxes], dtype=np.float64)
    return _bbox(pts)


def _to_world(obj, points):
    m = np.array(obj.matrix_world, dtype=np.float64)
    return points @ m[:3, :3].T + m[:3, 3]


def summarise_indices(mask):
    """Turn a boolean 'selected' array into a compact JSON-friendly summary.

    encoding is one of:
      "none"   nothing selected
      "all"    every element selected (no ids written)
      "list"   'indices' holds every selected id
      "ranges" 'ranges' holds [first, last] runs (inclusive); if 'truncated' is
               true the selection had more runs than the cap and the list is cut
               short, so use the bounding box to find the rest.
    """
    total = int(mask.size)
    idx = np.flatnonzero(mask)
    count = int(idx.size)
    out = {"count": count, "total": total, "truncated": False}
    if count == 0:
        out["encoding"] = "none"
    elif count == total:
        out["encoding"] = "all"
    elif count <= MAX_INDICES:
        out["encoding"] = "list"
        out["indices"] = idx.tolist()
    else:
        breaks = np.flatnonzero(np.diff(idx) > 1)
        starts = np.concatenate(([idx[0]], idx[breaks + 1]))
        ends = np.concatenate((idx[breaks], [idx[-1]]))
        out["encoding"] = "ranges"
        out["range_count"] = int(starts.size)
        if starts.size > MAX_RANGES:
            out["truncated"] = True
            starts, ends = starts[:MAX_RANGES], ends[:MAX_RANGES]
        out["ranges"] = [[int(a), int(b)] for a, b in zip(starts, ends)]
    return out


def _select_mask(elements):
    mask = np.zeros(len(elements), dtype=bool)
    if len(elements):
        elements.foreach_get("select", mask)
    return mask


def _material_names(obj):
    return [slot.material.name if slot.material else None for slot in obj.material_slots]


def _object_bbox_world(obj):
    corners = np.array([tuple(c) for c in obj.bound_box], dtype=np.float64)
    return _bbox(_to_world(obj, corners))


def describe_object(obj):
    info = {
        "name": obj.name,
        "type": obj.type,
        "data_name": obj.data.name if obj.data is not None else None,
        "bbox_world": _object_bbox_world(obj),
        "materials": _material_names(obj),
    }
    if obj.type == "MESH":
        info["vertex_count"] = len(obj.data.vertices)
        info["face_count"] = len(obj.data.polygons)
    return info


def describe_edit_mesh(obj):
    """Selected vertex/edge/face ids of a mesh that is in Edit Mode."""
    obj.update_from_editmode()  # copy the edit-mode state into obj.data
    mesh = obj.data
    vert_mask = _select_mask(mesh.vertices)
    edge_mask = _select_mask(mesh.edges)
    face_mask = _select_mask(mesh.polygons)

    sel = {
        "vertices": summarise_indices(vert_mask),
        "edges": summarise_indices(edge_mask),
        "faces": summarise_indices(face_mask),
        "bbox_local": None,
        "bbox_world": None,
        "materials": [],
    }
    if vert_mask.any():
        co = np.empty(len(mesh.vertices) * 3, dtype=np.float32)
        mesh.vertices.foreach_get("co", co)
        picked = co.reshape(-1, 3)[vert_mask].astype(np.float64)
        sel["bbox_local"] = _bbox(picked)
        sel["bbox_world"] = _bbox(_to_world(obj, picked))
    if face_mask.any():
        mat_index = np.zeros(len(mesh.polygons), dtype=np.int32)
        mesh.polygons.foreach_get("material_index", mat_index)
        names = _material_names(obj)
        used = sorted(set(mat_index[face_mask].tolist()))
        sel["materials"] = [names[i] if i < len(names) else None for i in used]
    return sel


def _view_info(context):
    space = getattr(context, "space_data", None)
    if space is None or space.type != "VIEW_3D" or space.region_3d is None:
        return None
    r3d = space.region_3d
    return {
        "perspective": r3d.view_perspective,
        "location": _r(r3d.view_location),
        "rotation_quaternion": _r(r3d.view_rotation),
        "distance": round(float(r3d.view_distance), 5),
        "camera": context.scene.camera.name if (r3d.view_perspective == "CAMERA" and context.scene.camera) else None,
        "shading": space.shading.type,
    }


def build_entry(context, note):
    """Collect everything about the current selection. Does not touch the disk."""
    mode = context.mode
    active = context.view_layer.objects.active
    objects = []
    boxes = []
    skipped = 0

    if mode.startswith("EDIT"):
        targets = list(getattr(context, "objects_in_mode", None) or ([active] if active else []))
    elif mode == "OBJECT":
        targets = list(context.selected_objects)
    else:  # sculpt, paint and pose modes work on the active object
        targets = [active] if active else []

    for obj in targets:
        if len(objects) >= MAX_OBJECTS:
            skipped += 1
            continue
        info = describe_object(obj)
        if mode == "EDIT_MESH" and obj.type == "MESH":
            info["selection"] = describe_edit_mesh(obj)
            boxes.append(info["selection"]["bbox_world"])
        elif mode == "EDIT_ARMATURE" and obj.type == "ARMATURE":
            info["selected_bones"] = [b.name for b in obj.data.edit_bones if b.select][:MAX_INDICES]
            boxes.append(info["bbox_world"])
        elif mode == "POSE" and obj.type == "ARMATURE":
            info["selected_bones"] = [
                b.name for b in obj.pose.bones if getattr(b, "select", getattr(b.bone, "select", False))
            ][:MAX_INDICES]
            boxes.append(info["bbox_world"])
        else:
            if mode.startswith("EDIT"):
                info["selection_note"] = "element selection is only captured for meshes"
            boxes.append(info["bbox_world"])
        objects.append(info)

    now = datetime.datetime.now().astimezone()
    blend = bpy.data.filepath
    return {
        "schema": SCHEMA,
        "id": now.strftime("%Y%m%d_%H%M%S") + "_" + uuid.uuid4().hex[:4],
        "status": "pending",
        "created": now.isoformat(timespec="seconds"),
        "note": note,
        "blend_path": blend.replace("\\", "/") if blend else None,
        "blend_dirty": bool(bpy.data.is_dirty),
        "blend_saved_on_send": False,
        "blender_version": bpy.app.version_string,
        "scene": context.scene.name,
        "mode": mode,
        "active_object": active.name if active else None,
        "objects": objects,
        "objects_not_listed": skipped,
        "selection_bbox_world": _union(boxes),
        "view": _view_info(context),
        "screenshot": None,
        "screenshot_error": None,
    }


# ----------------------------------------------------------------------------
# Screenshot
# ----------------------------------------------------------------------------

def _find_view3d(context):
    window = getattr(context, "window", None)
    area = getattr(context, "area", None)
    if area is not None and area.type == "VIEW_3D":
        return window, area
    windows = [window] if window else []
    windows += [w for w in context.window_manager.windows if w != window]
    for win in windows:
        for candidate in win.screen.areas:
            if candidate.type == "VIEW_3D":
                return win, candidate
    return window, None


def _shrink(path):
    """Scale a big screenshot down so a session can read it cheaply."""
    image = bpy.data.images.load(path)
    try:
        width, height = image.size
        longest = max(width, height)
        if longest > SCREENSHOT_MAX_PX:
            scale = SCREENSHOT_MAX_PX / longest
            image.scale(max(1, int(width * scale)), max(1, int(height * scale)))
            image.filepath_raw = path
            image.file_format = "PNG"
            image.save()
    finally:
        bpy.data.images.remove(image)


def capture_screenshot(context, path):
    """Save the 3D viewport as a PNG. Returns (ok, error_text)."""
    if bpy.app.background:
        return False, "Blender is running in background mode (no window), so no screenshot was taken"
    window, area = _find_view3d(context)
    if window is None or area is None:
        return False, "no 3D viewport was found to screenshot"
    region = next((r for r in area.regions if r.type == "WINDOW"), None)
    try:
        with context.temp_override(window=window, area=area, region=region):
            result = bpy.ops.screen.screenshot_area(filepath=path)
    except Exception as exc:  # a note without a picture still beats no note
        return False, "screenshot failed: %s" % exc
    if "FINISHED" not in result or not os.path.isfile(path):
        return False, "screenshot operator did not write a file"
    try:
        _shrink(path)
    except Exception:
        pass  # the full-size screenshot is still there
    return True, None


# ----------------------------------------------------------------------------
# Writing
# ----------------------------------------------------------------------------

def write_entry(entry, folder):
    os.makedirs(folder, exist_ok=True)
    final = os.path.join(folder, entry["id"] + ".json")
    temp = final + ".tmp"
    with open(temp, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(entry, handle, indent=1, ensure_ascii=False)
        handle.write("\n")
    os.replace(temp, final)  # a reader never sees a half-written note
    return final


def send_note(context, note, save_blend=False):
    """Capture, screenshot and queue one note. Returns (entry, json_path)."""
    folder = queue_dir(context)
    if not folder:
        raise RuntimeError(
            "The queue folder is not set. Open Edit > Preferences > Add-ons > Claude Notes and choose it."
        )
    os.makedirs(folder, exist_ok=True)

    saved = False
    if save_blend and bpy.data.filepath and bpy.data.is_dirty:
        try:
            saved = "FINISHED" in bpy.ops.wm.save_mainfile()
        except Exception:
            saved = False

    entry = build_entry(context, note)
    entry["blend_saved_on_send"] = saved

    png_name = entry["id"] + ".png"
    ok, error = capture_screenshot(context, os.path.join(folder, png_name))
    entry["screenshot"] = png_name if ok else None
    entry["screenshot_error"] = error

    path = write_entry(entry, folder)
    _pending_cache["count"] = count_pending(context)
    return entry, path


# ----------------------------------------------------------------------------
# UI
# ----------------------------------------------------------------------------

class CLAUDENOTES_Preferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    queue_dir: bpy.props.StringProperty(
        name="Queue folder",
        description="Folder the notes are saved to (Tools/blender_notes/queue in the Eurobound repo)",
        subtype="DIR_PATH",
        default="",
    )

    def draw(self, context):
        self.layout.prop(self, "queue_dir")
        self.layout.label(text="Currently writing to: %s" % (queue_dir(context) or "(not set)"))


class CLAUDENOTES_OT_send(bpy.types.Operator):
    bl_idname = "claude_notes.send"
    bl_label = "Send to Claude"
    bl_description = "Save the selection, a screenshot and your note to the Claude queue"
    bl_options = {"REGISTER"}

    def execute(self, context):
        wm = context.window_manager
        note = wm.claude_notes_text.strip()
        if not note:
            self.report({"ERROR"}, "Type a note first")
            return {"CANCELLED"}
        try:
            entry, _path = send_note(context, note, save_blend=wm.claude_notes_save_blend)
        except Exception as exc:
            self.report({"ERROR"}, "Note NOT sent: %s" % exc)
            return {"CANCELLED"}

        parts = ["Sent %s" % entry["created"][11:16]]
        if not entry["objects"]:
            parts.append("nothing selected, so it reads as a note about the whole scene")
        if entry["screenshot"] is None:
            parts.append("no screenshot")
        if entry["blend_path"] is None:
            parts.append("file never saved")
        elif entry["blend_dirty"] and not entry["blend_saved_on_send"]:
            parts.append("file has unsaved changes")
        wm.claude_notes_last = "; ".join(parts)
        wm.claude_notes_text = ""
        self.report({"INFO"}, wm.claude_notes_last)
        return {"FINISHED"}


class CLAUDENOTES_OT_open_queue(bpy.types.Operator):
    bl_idname = "claude_notes.open_queue"
    bl_label = "Open Queue Folder"
    bl_description = "Open the folder the notes are saved to"

    def execute(self, context):
        folder = queue_dir(context)
        if not folder:
            self.report({"ERROR"}, "The queue folder is not set (see the addon preferences)")
            return {"CANCELLED"}
        os.makedirs(folder, exist_ok=True)
        bpy.ops.wm.path_open(filepath=folder)
        _pending_cache["count"] = count_pending(context)
        return {"FINISHED"}


def _selection_label(context):
    mode = context.mode
    obj = context.view_layer.objects.active
    if mode == "EDIT_MESH" and obj is not None and obj.type == "MESH":
        mesh = obj.data
        return "%s: %d faces, %d verts selected" % (
            obj.name, getattr(mesh, "total_face_sel", 0), getattr(mesh, "total_vert_sel", 0))
    if mode == "OBJECT":
        names = [o.name for o in context.selected_objects]
        if not names:
            return "Nothing selected (note is about the whole scene)"
        if len(names) == 1:
            return "Object: %s" % names[0]
        return "%d objects: %s..." % (len(names), ", ".join(names[:2]))
    return "%s: %s" % (mode.replace("_", " ").title(), obj.name if obj else "no active object")


class CLAUDENOTES_PT_panel(bpy.types.Panel):
    bl_idname = "CLAUDENOTES_PT_panel"
    bl_label = "Claude Notes"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Claude Notes"

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager

        if not queue_dir(context):
            box = layout.box()
            box.alert = True
            box.label(text="Queue folder not set", icon="ERROR")
            box.label(text="Preferences > Add-ons > Claude Notes")

        layout.label(text=_selection_label(context), icon="RESTRICT_SELECT_OFF")
        layout.prop(wm, "claude_notes_text", text="", icon="GREASEPENCIL")

        if not bpy.data.filepath:
            layout.label(text="Save this file first (Ctrl+S)", icon="ERROR")
        else:
            layout.prop(wm, "claude_notes_save_blend")

        row = layout.row()
        row.scale_y = 1.6
        row.enabled = bool(wm.claude_notes_text.strip())
        row.operator("claude_notes.send", icon="EXPORT")

        if wm.claude_notes_last:
            layout.label(text=wm.claude_notes_last, icon="CHECKMARK")
        if _pending_cache["count"] is None:
            _pending_cache["count"] = count_pending(context)
        layout.label(text="Waiting for Claude: %d" % _pending_cache["count"])
        layout.operator("claude_notes.open_queue", icon="FILE_FOLDER")


_classes = (
    CLAUDENOTES_Preferences,
    CLAUDENOTES_OT_send,
    CLAUDENOTES_OT_open_queue,
    CLAUDENOTES_PT_panel,
)


def register():
    for cls in _classes:
        bpy.utils.register_class(cls)
    wm_type = bpy.types.WindowManager
    wm_type.claude_notes_text = bpy.props.StringProperty(
        name="Note",
        description="What should Claude change about the selected part?",
        default="",
    )
    wm_type.claude_notes_save_blend = bpy.props.BoolProperty(
        name="Save file when sending",
        description="Save the .blend first, so Claude opens exactly what you are looking at",
        default=True,
    )
    wm_type.claude_notes_last = bpy.props.StringProperty(default="")
    _pending_cache["count"] = None


def unregister():
    wm_type = bpy.types.WindowManager
    for name in ("claude_notes_text", "claude_notes_save_blend", "claude_notes_last"):
        if hasattr(wm_type, name):
            delattr(wm_type, name)
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
