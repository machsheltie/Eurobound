# Character Sprite Pipeline (binding)

Author rulings, 2026-11-02 (frame size raised from 96 to 128 the same day). Applies to every character sprite: the three bros, NPCs, enemies.

## The look

- **2.5D hybrid.** Pixel-art characters standing in painterly 3D dioramas, the way Star Ocean: The
  Second Story R puts sprites in 3D towns, with Bravely Default-style painted buildings.
- **Detail target: Final Fantasy X-2 Remastered.** Intricate outfits, readable faces, accessories
  and logos that survive at sprite size. Never smooshed, never blobby.
- **Proportions: semi-realistic**, about 4 to 5 heads tall (Second Story R, not chibi).

## Format

| Item | Value |
|---|---|
| Frame | **128 x 128 px** (character stands about 115 to 120 px tall; face about 15 x 17 px) |
| Directions | 8 (S, SE, E, NE, N, plus W, NW, SW mirrored where the design is symmetric) |
| Base animations | idle, walk (6 to 8 frames); battle sets per the combat spec |
| Palette | Locked per character, shared ramps across the party (`tools/art_cleanup/` palette) |
| In engine | `PartySprite3D` (AnimatedSprite3D, Y-billboard, **lit by the scene**, casts shadows, **nearest** filtering). Not NoClipBillboardSprite3D for characters: it is unshaded, so neon and lanterns would not light the bros. |

## Pipeline

1. **Model sheet (Firefly).** A detailed painterly turnaround of the character: front, side,
   back, full body, neutral pose, flat background. This is the master reference for face,
   outfit and logos. Starting points for the bros are the sheets in each bro's main folder under
   `Assets/Graphics/sprites/characters/party_members/<bro>/` (never the `alts/` folders).
2. **Pixel redraw (PixelLab), proven recipe (Lord Pilsner, 2026-11-02):**
   1. Crop the front view from the model sheet onto a 512 x 512 transparent canvas, figure about
      470 px tall, feet near the bottom.
   2. `pixellab_client.py convert --size 128 --reinterpret --strength 150`: image-to-pixel-art in
      **reinterpret** mode, which redraws clean pixel art (crisp outline, flat cel shading, readable
      face) and keeps the sheet's semi-realistic proportions. Never faithful/copy mode: it copies
      the painting's soft shading and gives noisy, blobby sprites (author rejected, 2026-11-02). (PixelLab "Pro" character creation from a concept came
      out chibi, about 2.7 to 3 heads, even when told not to; do not use it for party members.)
   3. Cut out the background (`art_cleanup.py cutout --key --tol 6 --soft 4`).
   4. **Face pass (author ruling: faces must read).** `pixellab_client.py inpaint --box <face rect>`
      with an explicit feature list (brows, eyes with whites and pupils, nose shadow, mouth
      expression, facial hair, crisp outline). Run 3 seeds, pick the one that sells the character.
   5. `pixellab_client.py rotate --size 128`: Pro `rotate_character` turns that south sprite into
      8 directions; the detailed face carries through the front and side views.
   6. Paste the exact chosen south frame back over PixelLab's south (rotate redraws it), then
      `remove_baked_shadow.py`: strip the baked ground shadow and stray edge specks. Lettering on
      clothing (jersey names, numbers) comes out garbled at 128 px: hand-place it as pixel letters,
      and give back views the lettering their sheet shows.
   7. Animations (Pilsner, 2026-11-04): `pixellab_client.py animate --mode skeleton-v3
      --template walking-8-frames` and `--template breathing-idle`. Skeleton-v3 moves the existing
      sprite rather than redrawing it, so colours stay steady; about 2-4 generations per direction.
      PixelLab animates its **own stored copy** of the character, which lacks the face pass and
      every hand edit (Pilsner's first walk lost his goatee, jaw and blue eyes). Always run
      `carry_master_head.py <approved stills> <animation export> <out>` afterwards: it crops the
      176 px animation canvas to 128 and pastes the approved head onto every frame. Then
      `remove_baked_shadow.py` and pack (`idle_*` = breathing idle, `walk_*` = walk). Archive the
      approved stills `.aseprite` before packing over it.
   Never shrink the painting down to pixel size yourself: averaged pixels are what make sprites
   look smooshed.
3. **Hand fix (Aseprite).** Faces, logos, text on clothing, stray pixels, consistent outlines.
   Lock the palette (`art_cleanup.py palette apply`).
4. **Review.** `art_cleanup.py sheet` on checker, dark, light and magenta; spelling check any
   lettering by eye; then the author approves.
5. **Pack and import.** `pack_aseprite.lua` packs the export into one `.aseprite` with
   `<action>_<direction>` tags under `game/assets/characters/...`; Aseprite Wizard auto-imports it as
   SpriteFrames. Shown with `PartySprite3D` (`game/characters/party/party_sprite_3d.gd`) and checked
   with `tests/capture_character_preview.tscn` in front of the Absinthe Arcade at day and night.

## Never

- Downscale painted art to pixel size.
- Use bilinear filtering or non-integer zoom on character sprites.
- Mix pixel densities inside one character, or between party members.
- Ship a sprite the author has not approved against its model sheet.

## Tools

- PixelLab: MCP server `pixellab` (user-level Claude Code config; API key from pixellab.ai/account).
- Aseprite: full version required (the trial cannot export). Aseprite Wizard addon in
  `game/addons/AsepriteWizard`.
- Cleanup and palette: `tools/art_cleanup/`.
- Pipeline scripts: `tools/sprite_pipeline/` (`pixellab_client.py`, `pack_aseprite.lua`,
  `remove_baked_shadow.py`, `carry_master_head.py`, per-character descriptions in `characters/`).
  `tests/capture_character_preview.tscn` takes a comma-separated list of `.aseprite` files to
  render a lineup. Raw PixelLab exports are
  archived under each bro's `pixellab/` folder.
