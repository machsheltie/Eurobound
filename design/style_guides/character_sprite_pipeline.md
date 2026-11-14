# Character Pipeline (binding)

**Author ruling, 2026-11-12 (supersedes the 2026-11-02 pixel-art pipeline below):** "WOW. LOOOOVE this version of Jakub from tripo/blender... I think I'd rather we actually do this with all characters including the bros. It just looks so much better than the crap trash we've been producing with pixel art."

Every character (the three bros, NPCs, enemies) now goes through **Tripo (3D model + auto-rig) → Blender (pose, toon render)**. The points marked **PENDING** are open on the Eurobound Desk (window "Sprite Development Team"); don't guess them.

## The look

- **2.5D hybrid**, as before: characters stand in painterly HD-2D dioramas (Star Ocean: The Second Story R, Bravely Default). Semi-realistic adults, not chibi.
- **Shading:** flat toon shading from the 3D model, with a warm key light from the upper left matching the rooms and a soft fill.
- **Final output: clean higher-res 3D renders, no pixelation**, sized to sit in the painted rooms (author, Desk `sprite-dev-3d-look`, 2026-11-12: option B). **Size convention: 300 px per metre** (a 1.8 m bro is 540 px tall), orthographic camera with a fixed ortho scale so every character shares that density, standing canvas 640 x 640 px with the feet at bottom-centre. In Godot: linear filtering with mipmaps, `pixel_size` = 1/300 m.

## Pipeline (proven on Jakub, 2026-11-12)

1. **Reference sheet** (Firefly GPT Image 2.6 from the main Firefly screen, or an existing approved model sheet). Auto-rig works best from a front view in a **T- or A-pose with empty hands**, with props painted out.
2. **Tripo image-to-3D** (tripo3d.ai, author's account): upload the clean front view and generate a textured model (~55 credits). The raw model is very dense (~1.9M faces); auto-rig refuses that.
3. **Simplify the mesh** in Tripo to ~20k triangles (~35 credits).
4. **Tripo humanoid auto-rig** with the Mixamo bone preset (~20 credits). Export GLB (free). Check the hand bones; the trial's far hand came out broken.
5. **Blender 5.2, headless** (`blender -b --python script.py`): import, pose by script, orthographic camera at the game's ~17° pitch, toon ramp material, transparent film, render. Scripts: `tools/char3d/` (`pose_render.py`, `pixelize.py`, pose presets in `poses/`).
6. **Output:** clean render at 300 px/m on a transparent background, no pixelation, no palette lock. For pixel sprites: downsample with area or block-majority sampling onto the character's palette, add a 1 px dark outline, then hand-fix face, stripes and lettering.
7. **Review in scene:** the Arcade build session captures the result in its room before the author sees it. Then the author approves it on the Desk.

Cost: ~110 Tripo credits per character (balance ~23,400 on 2026-11-12, so about 200 characters).

## Usage budget (binding, author 2026-11-12)

The author's weekly Claude usage must not be burned on 3D work ("last time I let it do 3d work it devoured them fast"). Follow `tools/char3d/README.md` § "Keep usage low": headless Blender scripts only (no viewport or screenshot driving), Tripo through the website on the existing subscription credits, never the paid API (author, 2026-11-13: "We may not use the Tripo API. I am NOT buying a subscription AND paying API credits." Keep the browser work lean: page text and element finds over screenshots, one character per short Sonnet run), at most 5 lines of output per command, one small contact sheet per character for review, batched background runs on a cheaper subagent, and Tripo called once per character (new poses and animations are free Blender re-renders of the stored rigged GLB).

## Rulings (Eurobound Desk, 2026-11-12)

- Look: clean higher-res renders, no pixelation (`sprite-dev-3d-look`).
- Redo everyone in 3D, bros included (`sprite-dev-3d-redo`).
- Budget: "Do everyone; I'll top up Tripo when needed" (`sprite-dev-3d-budget`).
- Animation: walkers (named and story characters) get 8-direction idle + walk from the rig; the crowd gets idle only, front-facing (`sprite-dev-3d-anim`).
- **Order (answered):** bros first (Pilsner, Chadwick, Bradley), then the Arcade NPCs, then the crowd groups, then the 15 battle sprites, then Debaucheryville (epic Eurobound-p7n6).
- **QC (author, 2026-11-13/14):** every character passes the blind-reviewer gates in `tools/char3d/QC.md` (G1 source, G2 Tripo input, G3 model, G4 frames); nothing is done on self-review, and two failed fixes go to the Desk.
- **Texturing:** `design/style_guides/reference_locked_texturing_protocol.md` was trialled on Chadwick (2026-11-14, REVISION REQUIRED, `Assets/Graphics/characters3d/chadwick/nhxz_trial/quality_report.md`); hand-texturing stays the rule until the author rules on Desk `sprite-dev-nhxz-chadwick-trial`.
- **Tripo API: NO** (author, 2026-11-13: "We may not use the Tripo API. I am NOT buying a subscription AND paying API credits." Do not propose paid APIs.) Tripo work uses the website and the subscription credits.

## Never

- Ship a character the author hasn't approved against its reference sheet.
- Put props in the hands of the auto-rig source image.

---

## Superseded: pixel-art pipeline (2026-11-02 to 2026-11-12, kept for reference)

PixelLab Tier 1 (2,000 generations/month) ran out in two days on 2026-11-12. The author rejected the cradled-Jakub pixel versions (v3-v6) and preferred the Tripo/Blender trial. Existing pixel sprites stay in the game until replaced.

### The look

- **2.5D hybrid.** Pixel-art characters standing in painterly 3D dioramas, the way Star Ocean: The
  Second Story R puts sprites in 3D towns, with Bravely Default-style painted buildings.
- **Detail target: Final Fantasy X-2 Remastered.** Intricate outfits, readable faces, accessories
  and logos that survive at sprite size. Never smooshed, never blobby.
- **Proportions: semi-realistic**, about 4 to 5 heads tall (Second Story R, not chibi).

### Format

| Item | Value |
|---|---|
| Frame | **128 x 128 px** (character stands about 115 to 120 px tall; face about 15 x 17 px) |
| Directions | 8 (S, SE, E, NE, N, plus W, NW, SW mirrored where the design is symmetric) |
| Base animations | idle, walk (6 to 8 frames); battle sets per the combat spec |
| Palette | Locked per character, shared ramps across the party (`tools/art_cleanup/` palette) |
| In engine | `PartySprite3D` (AnimatedSprite3D, Y-billboard, **lit by the scene**, casts shadows, **nearest** filtering). Not NoClipBillboardSprite3D for characters: it is unshaded, so neon and lanterns would not light the bros. |

### Pipeline

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

### Never

- Downscale painted art to pixel size.
- Use bilinear filtering or non-integer zoom on character sprites.
- Mix pixel densities inside one character, or between party members.
- Ship a sprite the author has not approved against its model sheet.

### Tools

- PixelLab: MCP server `pixellab` (user-level Claude Code config; API key from pixellab.ai/account).
- Aseprite: full version required (the trial cannot export). Aseprite Wizard addon in
  `game/addons/AsepriteWizard`.
- Cleanup and palette: `tools/art_cleanup/`.
- Pipeline scripts: `tools/sprite_pipeline/` (`pixellab_client.py`, `pack_aseprite.lua`,
  `remove_baked_shadow.py`, `carry_master_head.py`, per-character descriptions in `characters/`).
  `tests/capture_character_preview.tscn` takes a comma-separated list of `.aseprite` files to
  render a lineup. Raw PixelLab exports are
  archived under each bro's `pixellab/` folder.
