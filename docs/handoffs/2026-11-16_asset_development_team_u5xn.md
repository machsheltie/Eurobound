Window: Asset Development Team (2026-11-16; one task: the Rhinestone Shirt of Shame icon, bead Eurobound-u5xn, first garment only)

# Handoff: Asset Development Team, Rhinestone Shirt of Shame (u5xn)

The Production Desk Orchestrator lifted the asset pause and assigned this window one item to be made with the new workflow (`design/style_guides/tripo_asset_workflow.md`). The icon is built and passed blind QC. The 3D model's back failed QC twice, so the ship question is on the Desk. **Nothing is committed** (no author OK); the files are listed below.

## What was done

1. **Spec:** `Assets/Graphics/items/rhinestone-shirt-of-shame.md` (the approved 12-field physical description; its PROMPT A/B pixel sections belong to the retired pipeline). That file was already modified before this window and is not mine.
2. **Firefly** (website, GPT Image 2.6, Sunburst, High; style reference `lordpilsner/alts/Smug Beach Bro with Beer.png`):
   - Front v1 read as leather, so v2 used v1 as the object reference and fixed the cloth (poplin) and moved the drink stain to the image-left.
   - The left, right and back views were made from front v2.
   - Prompts are in `dev/asset_team/prompts/item_rhinestone_shirt_of_shame_view_front.txt`, `_view_front_v2.txt` and `_views_side_back.txt`.
   - The rejected v1 is `dev/asset_team/icon_refs/item_rhinestone_shirt_of_shame_front_v1_rejected.png`.
   - Blind gate A3 passed (rounds 1 and 1b). It was borderline on two points: the cloth is charcoal rather than #16161A, and the sheen streaks look airbrushed.
3. **Tripo** (website only), task `ca3190f5-47f8-4ae6-acb1-f4007f561543`:
   - Smart Mesh, multi-view with all four slots. Tripo's "Left" slot takes our `_left` file (the subject faces image-right).
   - 10k budget, quad: 11,062 faces / 11,314 vertices.
   - Then Smart UV and a 2K texture.
   - Exported as GLB (the export is free) to `Assets/Graphics/items/rhinestone_shirt_of_shame/rhinestone_shirt_of_shame.glb`, 1.47 MB, gitignored.
4. **Tripo credits used: 130** (Smart Mesh 100, Smart UV 20, texture 10). The account balance fell further over the same time (16630 → 15725) because other windows use the same account.
5. **Icon:** `Tools/item3d/render_item.py`, look B, ortho 0.95, headless Blender (one at a time, closed afterwards).
   - The shipped icon is `game/assets/items/icons/3d/rhinestone_shirt_of_shame_512.png` and `_128.png`, rendered straight on (yaw 0, pitch 12).
   - The default 3/4 view (yaw 28; kept as `dev/asset_team/reviews/u5xn_shirt_icon_r1_yaw28_512.png`) showed a ragged grey fragment on the shoulder and read as a jacket at 128 px.
6. **Blind A4** (fresh Sonnet each round), logged in `dev/asset_team/reviews/qc_log.jsonl`:
   - **Round 1:** REVISION REQUIRED. The 3/4 icon had a shoulder fragment and read as a jacket at 128 px. The model's back is split like a jacket and has stones down it that the reference doesn't, and there is no sweat patch.
   - **Round 2** (straight-on icon): the icon PASSED. The model FAILED again on the back and sides, which are the same Tripo faults.
   - Review renders are `dev/asset_team/reviews/u5xn_shirt_{front,yaw90,back,yaw270}_512.png`; sheets are `u5xn_shirt_a4_sheet.jpg` and `u5xn_shirt_desk.jpg`.

## Where things stand

- **Desk `Eurobound-u5xn-q1`**: "Rhinestone Shirt of Shame: the icon passes blind QC but the model's back fails. Ship the icon, or spend credits rebuilding the back?" Options:
  - ship the icon (recommended; the game only shows it as an inventory icon);
  - rebuild in Tripo (about 130 credits);
  - re-texture only (10 credits; the split back stays);
  - change the icon first.
- Bead Eurobound-u5xn is **blocked** on that card, with a progress comment. The Asset Board row `item-rhinestone_shirt_of_shame` is in review and points at the card, with the new 128 thumbnail. The bead page is synced.
- **On "ship":** set the Asset Board row to done and leave u5xn open for the T-shirt and thong (fresh windows). There is no engine item entry for the shirt yet (`game/assets/data/items/` has none), so wiring the icon needs eurobound-item-engine-sync later. Then ask to commit.
- **On "rebuild":** run a new Smart Mesh from the same four views (perhaps stress a closed, plain back), then Smart UV and texture, re-render, and run fresh blind A4.
- **Not part of this task:**
  - The closet joystick resize (Eurobound-ms3r-q2 answer) is queued as its own task in a fresh window; see `docs/handoffs/2026-11-16_asset_development_team.md`.
  - The T-shirt and thong garments.

## Changed files (uncommitted, this window's only)

- New:
  - `Assets/Graphics/items/rhinestone_shirt_of_shame/`: `_front.png`, `_left.png`, `_right.png`, `_back.png`, plus the `.glb`, which is gitignored.
  - `game/assets/items/icons/3d/rhinestone_shirt_of_shame_512.png`, `_128.png`.
  - The three prompt files above, and the v1 rejected reference.
  - In `dev/asset_team/reviews/`: `u5xn_shirt_front_512.png`, `u5xn_shirt_yaw90_512.png`, `u5xn_shirt_back_512.png`, `u5xn_shirt_yaw270_512.png`, `u5xn_shirt_icon_r1_yaw28_512.png`, `u5xn_shirt_a4_sheet.jpg`, `u5xn_shirt_desk.jpg`.
  - This handoff.
- Modified:
  - `dev/asset_team/reviews/qc_log.jsonl` (4 lines: A3 rounds 1 and 1b, A4 rounds 1 and 2).
  - `docs/handoffs/2026-11-16_asset_development_team.md` (the pause note and the ms3r-q2 answer).
- Not mine: the other `.import` files and handoffs that show in `git status`.

This window can be cleared.
