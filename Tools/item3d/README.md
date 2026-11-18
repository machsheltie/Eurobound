# tools/item3d: 3D item icons (Tripo + Blender), trial: opener_crown_and_cask
1. Reference: Firefly HOME screen, GPT Image 2.5 Sunburst, Quality High, 1:1, one object on flat light grey (prompt in `dev/asset_team/prompts/opener_crown_and_cask_3d_prompt.md`). Download button, move out of Downloads. 0 Tripo credits.
2. Tripo Studio (browser, no API key yet): upload the PNG, Generate (HD Model, default): 55 credits, about 2 min, 1.96M faces.
3. Same page, Retopo tab: Triangle, count 20000, Smart Mesh on: 35 credits, about 2 min, 19,400 faces. (This is the "simplify" step; there is none in Export.)
4. Export: GLB, 4k texture, free. Move the file out of Downloads into a dl/ folder.
5. Render: `"C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" -b --python tools/item3d/render_item.py -- <glb> <out>_512.png` writes the 512 RGBA and a 128 LANCZOS copy (`_128.png`, needs system `python` with Pillow). About 11 s.
6. Render details: deletes Icosphere* helpers, toon material from the GLB base-colour texture (`look.toon_material`), `look.lights`, `look.render`; ortho camera, yaw 28 deg, pitch 22 deg, key upper left, transparent film, Standard view transform. No outline, no palette lock, no painted shadow.
7. Scale: the model is normalised to a bounding-sphere diameter of 1.0 unit and ORTHO_SCALE = 0.95 is fixed, so every icon shares one px-per-unit (512 px / 0.95 units).
8. Texture fixes on a Tripo atlas live in a script here, never only in scratch (the handheld's R2/R3 screen paint was lost that way). Example: `handheld_screen.py <tripo.glb> <out.glb>` repaints the Broken Handheld's screen (flat #101010, three plum cracks with a thin light edge from one impact), flattens the neume and applies the R1 body gain, then writes a new GLB for `render_item.py ... 5 20`. Bead Eurobound-rspb.
Total Tripo cost for one item: 90 credits (55 + 35). The new Tripo balance reading also drops from other users' work on the shared account.

## Going live (author, Desk asset-team-icon-swap-live-folder, 2026-11-15)
"Swap as they're finished": once an icon's latest A4 line in `dev/asset_team/reviews/qc_log.jsonl` is a pass, run `python -I Tools/item3d/promote_icons.py` (dry run), then `--apply`. It copies `3d/<id>_128.png` and `_512.png` into `game/assets/items/icons/` and moves the pixel twin (`_64`, `_128` and their `.import`) to `game/assets/items/icons/legacy_pixel/` with `git mv`. Pixel icons with no 3D version stay live. Name ids to promote one icon (also refreshes a stale live copy); `--hold <id>` leaves one alone. It never commits; Godot needs a rescan afterwards.

9. `material_lookup.base_image(mat)` (used by `render_item.py`) returns the image that feeds the Principled BSDF Base Color, walking back through mix or colour-correction nodes; it falls back to the first image node, with a printed WARNING, only when nothing is linked (Eurobound-o2yv). Test: `blender --background --python Tools/item3d/test_material_lookup.py` (exit code 1 on failure).

## Soft flat items from the reference itself (garments; Eurobound-u5xn, 2026-11-17)
Author ruling for clothing icons: "Firefly reference, projected onto a flat 3D shape (0 credits)". Scripted outlines failed blind QC on shape three times, so the outline now comes from the reference:
1. Firefly front view on a plain mid-grey background, with any lettering zones left EMPTY (prompts: `dev/asset_team/prompts/item_i_survived_tshirt_ref_front_v2.txt`).
2. Type the doc's lettering and cut out the grey (per item; example `tshirt_ref_letter.py <raw> <lettered> <cutout>`). Blind A3 on the lettered image.
3. `blender -b --python Tools/item3d/ref_shape_slab.py -- <cutout_rgba.png> <out.glb>` builds a thin shape cut to the alpha outline (grid 160, edge relaxed, soft bulge toward the camera, plain back), textured with the reference. About 34k faces, 0 credits.
4. `render_item.py <glb> <id>_512.png 0 12` (straight on), then blind A4. First use: I Survived The Cock-Up T-shirt, A3 and A4 passed first round.

10. `sobriety_hole.py <tripo.glb> <out.glb>` darkens the Sobriety Test Deluxe's goal hole on the Tripo atlas (bead Eurobound-ioxj). It fits a circle to the hole's wall faces, then ramps every texel below the groove floor inside that circle to near black (#050508) over a short lip; nothing else on the atlas changes. Render the output with `render_item.py` at the default framing (28, 22). Source: Tripo Studio asset fe489ed7 (the 18,447-face retopo of rebuild 2), re-exported free as a 4k GLB to `dev/asset_team/icon_refs/aa_prize_sobriety_test_deluxe_tripo.glb` on 2026-11-17 because the original download was lost with its worktree. GLBs are gitignored, so an export that only lives in a worktree's `dl/` disappears when the worktree is removed; Tripo Studio's Assets page keeps every model and re-exports it for 0 credits.

**Where Tripo source GLBs live (Eurobound-0ygw, 2026-11-17).** Save every icon source GLB as `dev/asset_team/icon_refs/<id>_tripo.glb` (gitignored, but outside any worktree), never only in a worktree's `dl/` folder: a worktree is deleted after merge and its GLBs go with it. If a GLB is lost, Tripo Studio's Assets page can re-export it for free.

## One Blender at a time: `blender_lock.py` (Eurobound-1nvh, 2026-11-17)
Checking `tasklist` for blender.exe is racy (three overlaps on 2026-11-16). Every Blender run now goes through an atomic lock file (`O_CREAT|O_EXCL`, holds PID, time and label) in the system temp folder, so all worktrees and agent windows share it. Stale locks (dead PID, over 4 h old, or unreadable) are cleared automatically.
- Any Blender command: `python -I Tools/item3d/blender_lock.py run --label <what> -- "C:/Program Files/Blender Foundation/Blender 5.2/blender.exe" -b --python Tools/item3d/render_item.py -- <glb> <out>_512.png`
- It waits up to 30 min (`--timeout S`), runs the command, passes on its exit code, releases. Exit 75 = timed out waiting.
- `python -I Tools/item3d/blender_lock.py status` shows who holds it; `clear-stale` removes a dead holder's lock.
- Python callers: `from blender_lock import blender_lock` then `with blender_lock("label"): subprocess.run([BLENDER, ...])`. Already wired into `nft_slab.py` and `Tools/char3d/batch_g3.py` (so `render_frames.py` too). Nesting under the wrapper is safe.
- Scripts such as `render_item.py`, `card_slab.py` and the other `*_slab.py` run INSIDE Blender, so you wrap their launch line as above.
- Tests (fake command, no Blender): `python -I -m unittest discover -s Tools/item3d -p test_blender_lock.py`
