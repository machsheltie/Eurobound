# Sprite Development Team: handoff, 2026-11-15 (second task)

## Task done: Eurobound-8c3z, one more mock shot of "B with a painted-style texture"

The author's answer on `sprite-dev-8c3z-character-approaches` was, verbatim: "B with a painted-style texture: show me one more mock shot first". That shot is now on the Desk as `sprite-dev-8c3z-b-painted-mock`, with three images. The bead is `blocked` with `author-ruling`. The bead page and the Asset Board are synced (`npc-lord_pilsner`, `npc-chadwick` and `npc-bradley` are parked on this card, and there is a feed entry).

- **Method.** Pilsner's rigged GLB was turned -40° to face -Y and rendered as a flat 4-view turnaround (front, left, back, right). ChatGPT (website, pay dialog closed) repainted the whole sheet once. `project_ref.py` projected the repaint back onto the model's texture (silhouette IoU 0.976-0.979 on all four views). The texture was then copied onto the original GLB, posed with `render_dirs.py` (export_glb, idle S 0 and walk S 2) and captured in the hall with `game/tests/capture_character_approaches.tscn`.
- **Blind ranking** (fresh Sonnet, three unlabelled panels): painted B 7, last time's B 5, C painted sprites 4. Logged in `tools/char3d/qc_log.jsonl`. The reviewer liked painted B's colour fit, face and grounding. It flagged three problems: it still reads slightly airbrushed with no dark outlines, the build is bodybuilder-muscular (that comes from Tripo), and the walker's left hand is fused into the hip (a Tripo mesh fault, also in the earlier B).
- **Recommended option on the card:** go with B plus the painted texture, build Pilsner properly with the fused hand fixed, then build Chadwick and Bradley the same way.

## Author note after posting, 2026-11-15 (chat): "The walking rendered pic has deformed arms"

- **Cause.** The look-B walk (`tools/char3d/poses/lord_pilsner_look_b.json`, `proc_params` walk_arm 38, walk_elbow 22) swings the arm, but the Tripo mesh has the hand fused into the pocket. The swing dragged the forearm and stretched the hip into a skin wedge. The shipped frames have the same fault (`game/assets/characters/party/lord_pilsner/look_b/walk/E/02.png`).
- **Fix in the mock.** The walk was re-exported with walk_arm 6 and walk_elbow 4 (the hand stays in the pocket), then recaptured. The Desk card images and text were updated (card version 2), and `pilsner_painted_tex_walk.glb` was replaced.
- **Blind anatomy check: strict fail.** The arm is no longer stretched or fused, but the hand at the pocket reads cramped and ambiguous and the skin-to-shorts join is mushy. Logged in `qc_log.jsonl`. The real fix is in the mesh (separate the hand from the pocket in Blender, or rebuild with free hands). That is the first step of the recommended option, and it also fixes the shipped walk.
- Recorded on Eurobound-8c3z.

## Files (none committed; this window doesn't commit tools/char3d)

- `tools/char3d/project_ref.py`: new per-view `depth_test` option (z-buffer). Without it, the hand and bottle painted in the front view were also stamped onto the chest behind them.
- New: `tools/char3d/turnaround_views.py`, `tools/char3d/glb_yaw.py`, `tools/char3d/swap_atlas.py`, plus a row in `tools/char3d/README.md`.
- `tools/char3d/qc_log.jsonl` (one new line).
- `Assets/Graphics/characters3d/_approach_mock_8c3z/`: README section "B with a painted texture" with the rebuild steps, `turnaround_source.png`, `painted_turnaround_raw.png`, `painted_tex_turnaround_check.png`, `pilsner_painted_tex_idle.glb` and `pilsner_painted_tex_walk.glb` (5.4 MB each, JPEG atlas), `desk_full_model_painted.jpg`, `desk_closeup_b_painted.jpg`, `blind_three.jpg`.
- Still uncommitted from the first task: `tools/char3d/render_dirs.py`, the capture scene `game/tests/capture_character_approaches.gd/.tscn`, and the rest of the mock folder.
- This handoff.

## What the next window does

1. When the author answers `sprite-dev-8c3z-b-painted-mock`, update Eurobound-8c3z and the Asset Board rows.
2. If the answer is go: build Pilsner as a real-time 3D character in Godot, with the hand pulled out of the hip in Blender and a real animation set instead of posed frames. Then do Chadwick (p7n6.2) and Bradley (p7n6.3) the same way. Each one gets a blind in-game check before the Desk.
3. After that, the six held answers below.

## Author answers already on the Desk that are not acted on yet (held behind the 8c3z pick)

- `sprite-dev-pilsner-g4-retro`: "Fix both (sunglasses + head tilt), then re-review".
- `sprite-dev-g3-whitney-bradley` (note): try TextureCraft, and ask ChatGPT (GPT Image) what it recommends and to draft reference images.
- `sprite-dev-chadwick-frames-motion` (note): have an agent research the best way to handle movement, hand the method to the agents and let them try again.
- `sprite-dev-nhxz-chadwick-trial`: "Try the ChatGPT repaint + Blender fallback on a few assets", note "And try texturecraft". This mock is a working instance of that fallback, with the depth test added.
- `sprite-dev-chadwick-3d-face` (Eurobound-p7n6.2): "Accept the projected face; go on to his frames".
- `sprite-dev-vanek-mad-doctor` (Eurobound-dg5p): "Too much, tone it down", note "Find a happy medium between the teo".

## Gotchas found today

- `project_ref.py` only projects along the axes. A Tripo model with `face_yaw` must be turned first (`glb_yaw.py`), and the painted atlas is then copied back onto the original GLB (`swap_atlas.py`, which works because the UVs are identical).
- `render_dirs.py` export_glb poses: use direction S for both. The capture scene turns the walker itself (yaw 90), so exporting E turns it twice and you get a back view.
- ChatGPT kept the 1536x1024 canvas and the figure bounds to within 1-2 px when told the image is a projection source.
- The payment dialog appears twice on load: once on page load and again after the first upload. Close it with its X both times.
- Blender is `C:/Program Files/Blender Foundation/Blender 5.2/blender.exe`. Godot's console build is in Downloads (see `bd memories godot`).

## State

No Blender or Godot process of mine is running, and the ChatGPT tab is closed. The painted sheet is also in the Downloads folder as `pilsner_turnaround_painted_8c3z.png`. The scratchpad holds the 37 MB working GLBs. They aren't needed, because the rebuild steps are in the mock README.
