# Sprite Development Team: handoff, 2026-11-15

## Task done: Eurobound-8c3z, in-game mock shots of the character approaches

The Desk card `sprite-dev-8c3z-character-approaches` is up with five images. The bead is `blocked` with `author-ruling`.

- Shots: Lord Pilsner standing and mid-stride in the Absinthe Arcade hall (night, gameplay camera, 1920x1080), drawn four ways: today, A fixed sprites, B real-time 3D, C painted sprites.
- Blind ranking (fresh Sonnet, unlabelled panels): C 7, B 5, today 5, A 4. Logged in `tools/char3d/qc_log.jsonl`.
- Recommended option on the card: B with a painted-style texture, one more mock shot first.
- Files: `Assets/Graphics/characters3d/_approach_mock_8c3z/` (README has the rebuild commands), `game/tests/capture_character_approaches.gd` and `.tscn`, `tools/char3d/render_dirs.py` (new `export_glb` option, used with `only`).

## Not committed (needs an orchestrator; this window never commits tools/char3d)

- `tools/char3d/render_dirs.py`, `tools/char3d/qc_log.jsonl`
- `game/tests/capture_character_approaches.gd`, `game/tests/capture_character_approaches.tscn` (Godot will add a `.uid` on next import)
- `Assets/Graphics/characters3d/_approach_mock_8c3z/` (two 3.4 MB GLBs; leave them out if size matters)
- `docs/handoffs/2026-11-15_sprite_development_team.md`

## What the next window does

1. When the author answers the card, update Eurobound-8c3z and the Asset Board, then build under the chosen option. The Chadwick (p7n6.2) and Bradley (p7n6.3) rebuilds are approved but wait on this pick.
2. If the pick is the recommended one: repaint Pilsner's texture in the painted style (ChatGPT website, close the pay dialog), put the model in the hall with the capture scene, blind-review, post one more shot.

## Author answers already on the Desk that are not acted on yet (held behind the 8c3z pick)

- `sprite-dev-pilsner-g4-retro`: "Fix both (sunglasses + head tilt), then re-review".
- `sprite-dev-g3-whitney-bradley` (note): try TextureCraft, and ask ChatGPT (GPT Image) what it recommends and to draft reference images.
- `sprite-dev-chadwick-frames-motion` (note): have an agent research the best way to handle movement, hand the method to the agents and let them try again.
- `sprite-dev-nhxz-chadwick-trial`: "Try the ChatGPT repaint + Blender fallback on a few assets", note "And try texturecraft".

## Gotchas found today

- The 3D model stands taller on screen than the sprite of the same character. The sprite frames are rendered with a 17 degree camera pitch and then drawn on an upright billboard seen from the game's pitched camera, so they are foreshortened twice.
- `Sprite3D` with `ALPHA_ANTIALIASING_ALPHA_TO_COVERAGE` and cut-out alpha drew nothing in the hall; `ALPHA_CUT_OPAQUE_PREPASS` works.
- Mipmaps on the 300 px/m frames blur them; pre-scaling to about 190 px/m is sharper.
- ChatGPT's Plus renewal failed (payment dialog on load). Image generation still worked after closing the dialog.
- Characters are about 215 px tall in the hall at 1080p. That caps face quality under every option.

## State

No Blender, Godot or background job of mine is running. The ChatGPT tab is closed. The painted source is also in the Downloads folder as `pilsner_painted_8c3z.png`.
