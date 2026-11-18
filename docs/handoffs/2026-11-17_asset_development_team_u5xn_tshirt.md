Window: Asset Development Team (2026-11-17; one task from the Production Desk Orchestrator: Eurobound-u5xn garment 2, the I SURVIVED T-shirt icon)

# Handoff: Asset Development Team, I Survived The Cock-Up T-shirt (u5xn)

The icon is built and **passed blind A3 and blind A4 on the first round**. **0 Tripo credits.** Nothing is committed.

## Method

The author's ruling for this item (Desk asset-team-qc-i_survived_tshirt) was "A: Firefly reference, projected onto a flat 3D shape (0 credits)". I followed it rather than the Tripo Smart Mesh route of `tripo_asset_workflow.md`:
- The orchestrator quoted this ruling for the T-shirt.
- The bead's acceptance criteria ask for a projected flat-3D icon.
- Tripo split the rhinestone shirt's back open.

Firefly still followed the workflow: GPT Image 2.6 Sunburst, High quality, 1:1 at 2K, with the Lord Pilsner beer photo as style reference. I made only the front view, because a flat shape needs nothing else. If the author wants four views and Tripo for garments too, that is a Desk question for the orchestrator; I did not post it.

1. **Reference.**
   - v1 drew a whole gothic tower where the doc names only the dial, so I rejected it. It is kept at `dev/asset_team/icon_refs/item_i_survived_tshirt_front_v1_rejected.png`.
   - v2 is the dial with rays as a crying face, the red swoosh, an empty band left for the lettering, the smile hem, the pins and the cardboard scrap.
   - Prompts: `dev/asset_team/prompts/item_i_survived_tshirt_ref_front.txt` and `_v2.txt`.
2. **Lettering, typed and never drawn by an image tool.**
   - `Tools/item3d/tshirt_ref_letter.py` types I SURVIVED THE (#1F4FA3), COCK-UP (#D42B2B, bowed, cracked, flaking at the C) and DEBAUCHERYVILLE (#1F4FA3) in Impact. The ink takes the fabric's shading.
   - The same script then cuts out the grey background, filling from every corner, and trims the clothesline to just past the sleeves.
   - Outputs in `Assets/Graphics/items/i_survived_tshirt/`: `_ref_front_raw.png`, `_ref_front.png` (lettered) and `_ref_front_cutout.png`.
3. **Blind A3, round 1: PASS.** The lettering is exact. Minor notes:
   - DEBAUCHERYVILLE sits under the swoosh, not inside it, because the generated swoosh is a thin line;
   - the cloth is slightly cream;
   - the dial has a pocket-stopwatch crown;
   - the collar is less bacon-wavy than the doc describes.
4. **3D.** The new `Tools/item3d/ref_shape_slab.py` builds a thin shape cut to the cut-out's outline:
   - grid 160 with the edge relaxed, a soft bulge toward the camera, and a plain #EDEAE0 back;
   - 33,656 faces;
   - `Assets/Graphics/items/i_survived_tshirt/i_survived_tshirt.glb`, which is gitignored.
5. **Icon.** `render_item.py`, yaw 0, pitch 12, writing `game/assets/items/icons/3d/i_survived_tshirt_512.png` and `_128.png`.
6. **Blind A4, round 1: APPROVED.** Minor notes:
   - the cracks are subtler than in the reference;
   - the clothesline is shortened to stubs;
   - the outline is stair-stepped, visible only in the off-angle model views.
   - The sheet is `dev/asset_team/reviews/tshirt_a4_sheet.jpg`. Both lines are in `dev/asset_team/reviews/qc_log.jsonl`.
7. **Promoted live** with `promote_icons.py --apply`, which copied both files to `game/assets/items/icons/`. There was no pixel twin, so it made no `git mv`. **Godot needs a rescan**; I did not open Godot (the slot is in use).

## Tracking

- **Asset Board:** row `item-i_survived_tshirt` is **done**, with the new 128 thumbnail and a feed entry.
- **Eurobound-u5xn:** progress comment added. It stays blocked: the rhinestone shirt waits on Desk u5xn-q1 and the thong is next.
- **New bead Eurobound-szz2:** engine item entries for the T-shirt and the rhinestone shirt. Neither has one in `game/assets/data/items/`.
- **Bead page:** synced and acked.

## Changed files (uncommitted, this window's only)

- **New files:**
  - `Tools/item3d/ref_shape_slab.py` and `Tools/item3d/tshirt_ref_letter.py`
  - `Assets/Graphics/items/i_survived_tshirt/` (three PNGs, plus the .glb, which is gitignored)
  - `game/assets/items/icons/3d/i_survived_tshirt_{512,128}.png` and `game/assets/items/icons/i_survived_tshirt_{512,128}.png`
  - the two prompt files and the rejected v1
  - in `dev/asset_team/reviews/`: `tshirt_a3_ref_1024.jpg`, `tshirt_a3_print_crop.jpg`, `tshirt_a4_sheet.jpg`, and `tshirt_a4_yaw{28,90,180}_{512,128}.png`
  - this handoff
- **Modified files:**
  - `dev/asset_team/reviews/qc_log.jsonl` (2 lines: A3 and A4)
  - `Tools/item3d/README.md` (the new route)

## Cleanup

My Firefly tab and the local CORS server are closed. Each headless Blender run exited, and no Blender process is left. Firefly downloads were moved out of Downloads.

This window can be cleared.
