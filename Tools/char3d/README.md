# tools/char3d: 3D character pipeline (Tripo + Blender)

Replaces `tools/sprite_pipeline/` (PixelLab) for every character (author ruling 2026-11-12). The binding spec is `design/style_guides/character_sprite_pipeline.md`.

| File | What it does | Run |
|---|---|---|
| `tripo_client.py` | **DO NOT USE.** author, 2026-11-13: "We may not use the Tripo API. I am NOT buying a subscription AND paying API credits." Kept only for history; all Tripo work goes through the website on the subscription credits. |
| `look.py` | The shared Eurobound 3D look: toon ramp material, warm upper-left key plus cool fill light, transparent EEVEE render. Characters and items (`tools/item3d/`) import it so everything matches. | `import look` inside a headless Blender script (see its docstring) |
| `pose_render.py` | Imports a Tripo rigged GLB (Mixamo bone names), poses it from a JSON preset, toon-shades it and renders with an orthographic camera at the game's ~17° pitch on a transparent background. | `blender -b --python tools/char3d/pose_render.py -- <rigged.glb> <outdir> <tag> <pose.json>` |
| `pixelize.py` | Downsamples a render to sprite pixels on a palette, with a 1 px outline. Only used if the final look is pixel sprites (pending on the Desk). | `python tools/char3d/pixelize.py <render.png> <out.png> ...` (see `-h`) |
| `face_fix.py` | Hand-placed face pixels for the trial (Jakub-specific). | — |
| `project_ref.py` (nhxz extension) | Protocol step 6: `mask_png` per view (a SAM zone mask from `tools/paint_zones/segment_ref.py`) clips the projection to one material zone; `side` also takes `left`/`right` for side elevations; writes `<out>_projection_report.json` with per-view silhouette IoU and a `reliable` flag (IoU >= 0.85). Chadwick: Tripo source 0.89 (reliable), canonical portrait in a different pose 0.66 (not reliable). | `blender -b --factory-startup --python tools/char3d/project_ref.py -- <config.json>` |
| `glb_jpeg.py` | Re-encodes opaque PNG textures inside a GLB as JPEG (q92) without touching geometry or the rig. Run it after `project_ref.py`, which re-exports uncompressed (Bradley went from 97 MB to 21 MB, and the render diff was negligible). | `python tools/char3d/glb_jpeg.py in.glb out.glb` |
| `glb_inspect.py` | Prints bones and meshes of a GLB (headless Blender). | `blender -b --python tools/char3d/glb_inspect.py -- <file.glb>` |
| `shared_rig.py` | **Shared skeleton.** Rebuilds a Tripo rigged GLB onto the one canonical 22-bone Eurobound skeleton (Mixamo names, no fingers; fitted to the Tripo joints, canonical roll; facing detected from toes/hips plus a mesh symmetry scan and aligned to -Y, so `face_yaw` is always 0; weights remapped and cleaned: no arm/hand weight below the waist, `rig.pocket_sides` for hand-in-pocket; `--weights auto` for Blender auto-weights). Writes `<id>_shared.glb` next to the input. | `blender -b --factory-startup --python tools/char3d/shared_rig.py -- <id>_rigged.glb --profile <id>` |
| `shared_motion.py`, `anim_lib/{idle,walk}.json`, `profiles/<id>.json` | One idle/walk library (seeded from Lord Pilsner's approved procedural motion; `anim_lib/build_lib.py` regenerates it) retimed per body by a profile: cycle frames, stride/knee/arm/elbow/bounce/sway/breathe multipliers, lean, per-direction head lift, swayback counter, static pose. Used by `render_dirs.py` with `"rig": "shared", "profile": "<id>"`; see `poses/lord_pilsner_shared.json`, `poses/chadwick_shared.json`. | `blender -b --factory-startup --python tools/char3d/render_dirs.py -- <id>_shared.glb <out_dir> <id> tools/char3d/poses/<id>_shared.json` |
| `contact_sheet.py` | Review sheet (PIL, figure-cropped, <=1024 px) from chosen frames. | `python tools/char3d/contact_sheet.py out.png 5 frame.png ...` |
| `poses/*.json` | Pose presets (bone aims, camera, light). `jakub_cradled.json` is the approved-direction trial pose. | — |

Blender 5.2 is at `C:/Program Files/Blender Foundation/Blender 5.2/blender.exe`.

## Keep usage low (author, 2026-11-12: last time 3D work "devoured" the weekly tokens in two days)

1. **Scripts, not screenshots.** Run Blender headless (`-b`) from Bash; never drive Blender through the MCP viewport or by screenshot. Tripo runs on the website (the paid API is ruled out, author, 2026-11-13: "We may not use the Tripo API. I am NOT buying a subscription AND paying API credits."). Keep that browser run lean: one character per short Sonnet subagent run, `find`/`get_page_text` instead of screenshots, a screenshot only to confirm a result, and download the rigged GLB straight into `Assets/Graphics/characters3d/<id>/`.
2. **One command, short output.** Every script prints at most ~5 lines (paths, counts, credits). Send full logs to a file and `tail` it only on failure.
3. **Look at one small image.** Review a single contact sheet per character (≤1024 px, all angles on one sheet). Never Read full-size renders one by one, and never Read the same image twice.
4. **Batch.** Queue several characters per run in the background (`run_in_background`), with one notification at the end, and no polling.
5. **Cheap workers.** Batch runs go to a Sonnet subagent with a short brief and a ≤100-word report; the main session only reviews contact sheets and talks to the author.
6. **Reuse, don't regenerate.** Keep each character's rigged GLB in `Assets/Graphics/characters3d/<id>/`. New poses, angles or animations are Blender re-renders (free, no Tripo credits). Tripo is called once per character.
7. **No duplicate work.** Exactly one session owns character work (the Sprite Development Team). Check the Asset Board before starting.

## Lessons from Lord Pilsner (passed the 1:1 hall check 2026-11-13, config `poses/lord_pilsner_look_b.json`)

1. Start from the character's original painted art, never from pixel art or anything derived from it (the author rejected Pilsner v1 for that).
2. Tripo's idle preset deforms baggy shorts; use `procedural` breathe/walk in `render_dirs.py` instead.
3. Tripo meshes come out yawed relative to the armature (`face_yaw`), and the head dips along the mesh's axis: scale the head lift per direction (`body_rot_scale_by_dir`) or the side views stare at the ceiling.
4. Baked swayback shows up as a 20–30° lean-back in the side and three-quarter views; counter-rotate the spine per direction.
5. Auto-weights tie shorts and legs to the hands; run `strip_weights` before any arm swing, or the swing drags the shorts.
6. Cull held props with `cull_boxes` and re-pose that arm with `bone_rot_arm`.
7. Tripo multi-view can mix the views up: Bradley got the back of his head as a face. Build from a single front-view crop of the turnaround.
8. Tripo garbles lettering (jersey text, hat patches). Fix it with `project_ref.py`, which projects the reference sheet's front and back views onto the texture in UV space; masks live in `poses/<id>_project.json`. Then read every letter in a crop.
