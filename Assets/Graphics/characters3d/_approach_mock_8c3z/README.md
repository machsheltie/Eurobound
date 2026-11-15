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
