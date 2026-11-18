# Sprite Development Team: handoff, 2026-11-16

## Task: Woo Woo Whitney with the new Tripo workflow (bead Eurobound-p7n6.6)

The Production Desk Orchestrator assigned this task (pause lifted, `design/style_guides/tripo_asset_workflow.md` binding). Lord Pilsner, Chadwick and Bradley were not touched.

## Result

- **GLB:** `Assets/Graphics/characters3d/woo_woo_whitney/woo_woo_whitney.glb`, 5.9 MB.
  - Mesh: 1 mesh, 29,334 quads.
  - Texture: one 4K JPEG atlas, made at 8K and exported at 4K.
  - Rig: Mixamo, 66 joints (`mixamorig:*`).
  - Clips: `idle_001` (15.4 s) and `walk_001` (2.4 s), in place.
  - Size: exported about 1.0 m tall; shown at 1.66 m (petite, with platforms).
- **Sources** (same folder): `woo_woo_whitney_view_{front,left,right,back}.png`, made in Firefly with GPT Image 2.6 Sunburst on High at 4:5. References were Pilsner's beer photo (style) and her Desk-approved portrait (outfit). `woo_woo_whitney_tpose.png` comes from Tripo's T Pose template.
- **Hall preview:** `Assets/Graphics/characters3d/woo_woo_whitney/hall_preview/` (night, the hall's own camera, as for the author's Pilsner preview). Use `a_idle_t7.7_full.png`, the best idle frame; the stock idle keeps her head slightly down.
  - Script: `game/tests/_preview_whitney/capture_whitney.{gd,tscn}`, adapted from the author's `capture_walk.gd`. It takes a height argument, matches bones by name suffix, and reads facing from foot to toe because the walk is in place. The folder is untracked, like `_preview_author_pilsner`.
- **Blind QC** (`tools/char3d/qc_log.jsonl`, 2026-11-16): G2 source views pass. The in-game check fails at 5/10:
  - At game size her face is mush, and it is neutral instead of the portrait's laugh. I asked Tripo for a closed mouth in the T-pose.
  - The stock idle keeps her head down.
  - The pigtails read as a clump.
  - The stock walk is stiff.
  - She has no shadow.
  One producer fix was tried: sampling the idle for a better frame.
- **QC process miss:** G2 should have run before Tripo credits were spent. I self-checked the four views and ran G2 afterwards. It passed, and this is stated in the log and on the Desk card.

## Tripo route actually used, and why it differs from the workflow

1. Image > T Pose template (free).
2. Multiview Image (100 credits).
3. Multi-View to 3D > Smart Mesh, quad, 25k (120 credits).
4. Retopology, quad, 25k (10 credits).
5. Smart UV (20 credits).
6. Texture (30 credits).
7. Auto Rig, Mixamo (20 credits).
8. Stock idle and walk presets (free).
9. Export GLB (free).

Segment and Fill Parts were done on separate copies, but the delivered model skips them. Tripo refuses Smart UV on any segmented model ("not currently supported for multi-part models"), even after its parts are merged back into one. Segmenting her also made about 250 parts, and retopology on that model hung until the parts were merged. Which step characters should drop is on the Desk (q2).

**Tripo credits:** 16,630 → 16,200 on the counter. 30 of that was the author's own texture job running at the same time, so this task used **400 net**. That includes two segment runs (50 + 40) and two stuck retopos that were cancelled and refunded. **Firefly:** 6 generations.

Tripo models kept:
- `f734c3b3`: the delivered model, with the full chain.
- `6a30525d`: segmented, filled, merged and retopologised, with no UV.
- `181db83c` and `207599ce`: abandoned segment copies with about 250 parts.

## Waiting on the author (Eurobound Desk, window "Sprite Development Team")

- `Eurobound-p7n6.6-q1`: keep Whitney, or fix and rebuild. Recommended: redo the T-pose with her laugh and bigger pigtails, plus a bubbly text-prompted idle, for about 300 credits.
- `Eurobound-p7n6.6-q2`: should characters drop segment/fill parts or Smart UV? Recommended: drop segment and fill parts.

The bead is `blocked` with `author-ruling`. The Asset Board row `npc-woo_woo_whitney` is `parked` with the note and a thumbnail. The bead page is synced.

## New gotchas (saved with `bd remember`)

- `firefly-reference-upload-via-local-server`: how an agent attaches Firefly reference images and saves generations.
- `tripo-segment-retopo-smartuv-gotchas`: about 250 segment parts hang retopology (merge them first), Smart UV refuses segmented models, stuck jobs can be cancelled for a refund, and the export download can be captured in the page.

## Files (none committed)

- New: `woo_woo_whitney.glb`, `woo_woo_whitney_view_*.png` and `woo_woo_whitney_tpose.png` in `Assets/Graphics/characters3d/woo_woo_whitney/`; `hall_preview/`; `game/tests/_preview_whitney/`; `.desk_upload/sprite_dev/whitney_tripo_*.jpg`; this handoff.
- Changed: `tools/char3d/qc_log.jsonl` (one line).

## Update, same day: rebuild 2 and two author answers

Author answers, relayed by the Production Desk Orchestrator:
- `Eurobound-p7n6.6-q1`: "Fix and rebuild: redo the T-pose with her laugh from the portrait and bigger pigtails, and try a bubbly text-prompted idle (about 300 more credits)".
- `sprite-dev-8c3z-b-painted-mock`: "i redid pi;smer myself". Eurobound-8c3z is closed as superseded. Eurobound-1nwj (the shipped look-B walk frames) stays open.

The Asset Board rows for Pilsner, Chadwick and Bradley now say the author is building them personally.

**Rebuild 2.** Route:
1. T Pose template, from the portrait plus the views, with a laugh and bigger-pigtails prompt (`woo_woo_whitney_tpose_v2.png`, option 4 of 4).
2. Multiview.
3. Smart Mesh, quad, 25k.
4. Retopology: 27,696 quads.
5. Smart UV.
6. Texture at 8K.
7. Rig.
8. A text-prompted "bubbly idle" (5 s) plus the stock walk.
9. Export at 4K.

`woo_woo_whitney.glb` is now build 2 (7.5 MB). Build 1 is kept as `woo_woo_whitney_v1.glb`. Hall shots are in `hall_preview_v2/`. It used **200 Tripo credits**, and the Tripo model is `2df38940`.

**Blind QC failed at 4/10.**
- The open laugh renders as a black void with no teeth.
- The AI idle hunches her forward.
- The pigtails merge into one blob from the side.
- The denim is noisy.

That is the second failed round, so both builds went to the author side by side on `Eurobound-p7n6.6-q3`. The recommended option is rebuild 3: a toothy grin with the lips closed, pigtails set wide apart, the stock walk and a short happy-sway idle. `q2` (segment vs Smart UV) is still open. The bead is `blocked`.

**Godot gotcha.** Another session added a new class (`AbilityTable`). Godot's class cache is now stale, so `absinthe_arcade_interior_hd2d.gd` fails to compile when the capture runs. The shots still matched build 1's screen size and position. The fix is a one-time `godot --headless --path game --import --quit`. That command was denied in this session, so it has not been run.

Total Tripo credits for Whitney today: 600 (400 + 200).

## Update 2: rebuild 3

Author answers, relayed:
- `q2`: "Characters skip segment and fill parts; keep Smart UV (how Whitney was made)". The orchestrator is updating `tripo_asset_workflow.md` to match.
- `q3`: "Rebuild 3: big toothy grin (lips closed), pigtails set wide apart, stock walk, a short happy-sway idle (about 200 credits)".

**Build 3.** Route:
1. T Pose template, from the v2 T-pose plus the front and back views (`woo_woo_whitney_tpose_v3.png`, option 1 of 4).
2. Multiview.
3. Smart Mesh, quad, 25k (Tripo model `894c4821`).
4. Retopology.
5. Smart UV.
6. Texture, twice. The forehead spot came back on the second roll.
7. Rig.
8. An AI "Happy sway" idle (5 s) plus the stock walk.
9. Export at 4K, 7.9 MB.

`woo_woo_whitney.glb` is now build 3. Builds 1 and 2 are kept as `_v1.glb` and `_v2.glb`. Hall shots are in `hall_preview_v3/`. It used **230 Tripo credits**, so Whitney's total for today is **830**.

**Blind QC failed at 5/10** (G2 failed too):
- The T-pose source doesn't set the pigtails wide enough.
- A dark spot sits mid-forehead.
- The idle pitches her head and torso forward.
- The pins and denim smear into noise at the hall camera's distance.
- In one walk frame a hand blends into her jeans.

The grin fixed build 2's black-void mouth. After three rounds, the card `Eurobound-p7n6.6-q4` asks the author to choose. The recommended option is a free headless-Blender repair:
- Paint the forehead spot out with her skin tone.
- Tilt the idle's spine and head bones back a few degrees.
- Run the blind check again.

The bead is `blocked`.

**For whoever does the Blender repair.**
- The forehead spot is not at the triangle centroids I sampled. The forehead texels around x≈0, y 0.93-0.955, z>0.05 are skin-toned (about 130,89,67), and the hairline parting sits at y 0.96-0.975. The mesh profile steps in between y 0.935 and 0.94, so the spot may be geometry, such as a dent, rather than texture.
- To find it, render a front close-up in Blender and pick the face under the spot.
- The parsing helper I used is in the session scratchpad (`fix/glbio.py`). It is not needed.

**Capture script fix.** `capture_whitney.gd` now picks the idle as "the clip that is not the walk", because AI idles are named after their prompt. Without this, the capture hung.

## Update 3: free Blender repair (author in chat: "Yes, try the free repair in blender")

Card `q4` is marked answered on the Desk.

`Tools/char3d/whitney_v3_repair.py` (headless Blender 5.2, 0 credits) does two things:
- **Forehead.** The spot was a hole in Tripo's mesh, not texture: you could see the inside of the back of her head through it. Its 4 boundary edges sit at x≈−0.004, z≈0.94, y≈−0.056. They are split at UV seams, so `holes_fill` fails. The script builds the face from one vertex per corner and gives it the neighbouring UVs.
- **Idle.** Relative to rest, the AI idle's head is pitched up about 10–14°, and the neck juts forward 4–8°. The script rotates the Neck back over the chest on every frame and counter-rotates the Head, so its angle in the world doesn't change. The walk is untouched.

Two mistakes from my first passes, both reverted:
- Restoring the head to its rest pitch made her look down.
- Remapping UVs of faces hit by rays went through the hole and onto the back of her head.

Files:
- `woo_woo_whitney.glb` is now the repaired build. The unrepaired one is kept as `_v3_raw.glb`.
- Hall shots are in `hall_preview_v3_repaired/`.

**Blind QC failed at 6/10**, the best of the four builds (5, 4, 5, 6).
- Cleared: the forehead spot and the head pitch.
- Still flagged: a stiff, low-energy idle; a muddy lower face; pins and denim reading as noise; small and low-contrast at the hall camera.

Card `Eurobound-p7n6.6-q5` asks the author to accept her, look in game themselves, or pause the NPC rebuilds and set how characters should read at the hall camera first. The bead is `blocked`.

## State

No Godot or Blender process is running, the local file server is stopped, and the Chrome tab is closed. Scratch copies are in the session scratchpad and are not needed. This window can be cleared.
