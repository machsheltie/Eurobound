# Character approach mock shots (Eurobound-8c3z)

In-game mock shots of Lord Pilsner in the Absinthe Arcade hall, four ways, for the author's Desk card `sprite-dev-8c3z-character-approaches`.

- `desk_full_now.jpg`: look-B frames as the game draws them today (300 px/m frames shrunk by the GPU, hard cut-out edges).
- `desk_full_fixed.jpg`: the same frames pre-scaled to display size with smooth edges.
- `desk_full_model.jpg`: the posed 3D model standing in the room (`pilsner_idle.glb`, `pilsner_walk.glb`).
- `desk_full_painted.jpg`: the same two frames repainted by ChatGPT (`painted_raw.png`), cut out and fitted to the look-B framing at 2x.
- `desk_closeup.jpg`: 2x close-up of all four. `blind_closeup.jpg`: the same without labels, for the blind review.

Rebuild (repo root, Godot window needed):

    blender -b --factory-startup --python tools/char3d/render_dirs.py -- Assets/Graphics/characters3d/lord_pilsner_v2/lord_pilsner_rigged.glb <tmp> pilsner <cfg>
        cfg = tools/char3d/poses/lord_pilsner_look_b.json without "render_anims", plus "only": ["idle"|"walk", "S"], "only_frame": 0|2, "export_glb": "<out.glb>"
    godot --path game --resolution 1920x1080 res://tests/capture_character_approaches.tscn -- <out_dir> <idle.glb> <walk.glb> <painted_idle.png> <painted_walk.png>

These are mocks. Nothing here is wired into the game.

## B with a painted texture (author's pick "show me one more mock shot first", 2026-11-15)

- `turnaround_source.png`: flat rest-pose turnaround (front, left, back, right; 384x1024 each) of `lord_pilsner_v2/lord_pilsner_rigged.glb` turned -40 degrees to face -Y.
- `painted_turnaround_raw.png`: ChatGPT's repaint of that sheet (website; same canvas, same silhouettes).
- `painted_tex_turnaround_check.png`: the model with the repaint projected onto its texture, flat, four sides.
- `pilsner_painted_tex_idle.glb`, `pilsner_painted_tex_walk.glb`: posed, JPEG atlas. `desk_full_model_painted.jpg`, `desk_closeup_b_painted.jpg` (last B vs painted B), `blind_three.jpg` (1 painted B, 2 C, 3 last B).

Rebuild (repo root; B = Blender 5.2, <t> = a temp folder):

    B -b --factory-startup --python tools/char3d/glb_yaw.py -- Assets/Graphics/characters3d/lord_pilsner_v2/lord_pilsner_rigged.glb <t>/rot.glb -40
    B -b --factory-startup --python tools/char3d/turnaround_views.py -- <t>/rot.glb <t>/pil      (paste the 4 views side by side into a 1536x1024 sheet)
    project_ref.py config: glb <t>/rot.glb, out_glb <t>/rot_painted.glb, lossless true, views left/right/back/front (that order) with
        crop = mask = the panel box [i*384, 0, (i+1)*384, 1024], ndot 0.25 (front 0.3), ndot_soft 0.2, bilinear, auto_align, depth_test true
    B -b --factory-startup --python tools/char3d/swap_atlas.py -- <t>/rot_painted.glb Assets/Graphics/characters3d/lord_pilsner_v2/lord_pilsner_rigged.glb <t>/painted.glb <t>/atlas.png
    render_dirs.py on <t>/painted.glb with the look-B config as above ("only": ["idle"|"walk", "S"]), then glb_jpeg.py, then the capture scene.

depth_test matters: without it the hand and bottle painted in the front view are also stamped onto the chest behind them.

Walk pose for the painted mock: the look-B `proc_params` with walk_arm 6 and walk_elbow 4 (author note "The walking rendered pic has deformed arms": the default 38/22 swing drags Pilsner's pocket-fused hand and stretches the hip).
