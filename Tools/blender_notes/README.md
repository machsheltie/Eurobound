# Tools/blender_notes: Claude Notes (a Blender addon)

Point at a part of a 3D model in Blender, type what is wrong with it, and click Send. A Claude session picks the note up and does the work. This is the "last 10% of polish" loop from bead Eurobound-nhxz.4.

Built and tested on Blender 5.2.3 LTS (`C:/Program Files/Blender Foundation/Blender 5.2/blender.exe`).

## Install (once)

1. Close Blender.
2. Double-click `install.bat` in this folder. It should print `CLAUDE_NOTES_INSTALL: OK`.
3. Open Blender. In the 3D view press **N** to open the sidebar. There is a new tab called **Claude Notes**.

A Claude session can do steps 1–2 for you with:

```
"C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" --background --python Tools/blender_notes/install_addon.py
```

Run the same thing again after `claude_notes.py` changes; it replaces the old copy.

By hand instead: Edit > Preferences > Add-ons > the down arrow at the top right > Install from Disk > pick `claude_notes.py`, tick it on, then open its settings and set **Queue folder** to this folder's `queue` folder.

## How to use it

1. Open the model and save it (Ctrl+S) so the file has a name.
2. Pick what the note is about:
   - **A whole object:** click it in Object Mode.
   - **A region:** press Tab for Edit Mode and drag a box over the part (or select faces any way you like).
   - **Nothing selected** means the note is about the whole scene.
3. Turn the view so the problem is visible. The addon takes a picture of the 3D view exactly as you see it.
4. Type the note in the box in the **Claude Notes** tab, for example "this collar should be the darker green from the reference".
5. Click **Send to Claude**. The panel shows "Sent 14:32" and the "Waiting for Claude" count goes up.
6. Tell the Claude session that owns the model "check my Blender notes" (or just keep working; send as many as you like first).

**Save file when sending** is ticked by default. It saves the .blend as you send, so Claude opens exactly what you were looking at. Untick it if you don't want the file saved; the note is then flagged as "unsaved changes".

## How a Claude session reads the queue

```
python Tools/blender_notes/list_notes.py                  # pending notes, 5 lines each
python Tools/blender_notes/list_notes.py show <id>        # one note in full (JSON)
python Tools/blender_notes/list_notes.py done <id> -m "what was changed"
python Tools/blender_notes/list_notes.py --all            # pending and done
python Tools/blender_notes/list_notes.py reopen <id>
```

`<id>` can be any unique part of the id; the last four characters are enough. `done` moves the note and its screenshot into `queue/done/`.

Working a note:

1. Run `list_notes.py`, then `show <id>` for the note you take. Look at its screenshot once (it is at most 1600 px wide).
2. Find the region from the note. Vertex, edge and face ids are in `objects[].selection`; they are ids on the mesh in `blend_path`, valid as long as the mesh has not been rebuilt since. `selection.bbox_world` / `bbox_local` and `selection.materials` locate the same region when ids can't be trusted.
3. Do the work under the usual rules (`design/style_guides/3d_asset_rules.md`, `Tools/char3d/README.md` usage rules: headless scripts, short output).
4. `done <id> -m "..."` with one line on what changed, and tell the author.

If a note says `unsaved changes when sent` or `FILE NEVER SAVED`, the ids may not match the file on disk: use the bounding box and screenshot, or ask the author to save and resend.

### What a note holds

Each note is one file, `queue/<id>.json`, with its screenshot `queue/<id>.png` beside it.

| Field | Meaning |
|---|---|
| `id`, `created`, `status` | Timestamp-based id, local time with offset, `pending` or `done` |
| `note` | What the author typed |
| `blend_path`, `blend_dirty`, `blend_saved_on_send` | The .blend, whether it had unsaved changes, whether the addon saved it |
| `mode`, `active_object`, `scene`, `blender_version` | Blender state when sent (`OBJECT`, `EDIT_MESH`, ...) |
| `objects[]` | Each selected object (or each object in Edit Mode): `name`, `type`, `bbox_world`, `materials`, vertex and face counts |
| `objects[].selection` | Edit Mode meshes only: `vertices`, `edges`, `faces`, `bbox_local`, `bbox_world`, `materials` used by the selected faces |
| `selection_bbox_world` | One box around everything selected (`min`, `max`, `center`, `size`) |
| `view` | Viewport camera (perspective, location, rotation, distance, shading) |
| `screenshot`, `screenshot_error` | PNG file name, or `null` plus the reason |

Selected ids are kept small. Each of `vertices` / `edges` / `faces` has `count`, `total` and an `encoding`:

- `none`: nothing selected. `all`: everything selected (no ids written).
- `list`: `indices` has every id (used up to 2,000 ids).
- `ranges`: `ranges` has `[first, last]` runs, inclusive (used above 2,000 ids). If `truncated` is true there were more than 500 runs and the list is cut short; use the bounding box for the rest.

## Limits

- **No screenshot without a window.** When Blender runs in background mode (`--background`, as the tests do) there is no viewport to photograph. The note is still written, with `"screenshot": null` and the reason in `screenshot_error`.
- The note box is a single line. Long notes work; they just scroll.
- Element ids are captured for meshes only. For armatures the selected bone names are saved; for other object types only the object itself.
- Ids are for the base mesh, before modifiers.
- The screenshot is the 3D view area, including any panels open inside it.

## Files

| File | What it is |
|---|---|
| `claude_notes.py` | The addon (one file) |
| `install_addon.py`, `install.bat` | Installs or updates the addon and points it at `queue/` |
| `list_notes.py` | Reader for sessions: list, show, done, reopen |
| `test_headless.py` | Checks for agents (below) |
| `queue/` | The notes. Its contents are gitignored |

## Testing (for agents)

Check `tasklist` for `blender.exe` first; only one Blender can run on this laptop.

```
blender --background --factory-startup --python Tools/blender_notes/test_headless.py -- <empty temp folder>
```

Expect `TEST: ALL OK` (register, Object Mode note, Edit Mode note, huge selection, empty note refused). Adding `--gui` after the folder and dropping `--background` opens a window for about four seconds, sends one note with a real screenshot, and exits by itself. Set `BLENDER_USER_RESOURCES` to a temp folder to keep either run away from the author's Blender settings.
