Window: Asset Development Team (2026-11-16; one task: build the Arcade claw closet, bead Eurobound-ms3r)

# Handoff: Asset Development Team, 2026-11-16

The Production Desk Orchestrator assigned this window one task: build the five closet pieces the author approved on the Desk (asset-team-arcade-closet-reference-set, verbatim: "Approve all five: build them"). The five are the Q8 blacklight switch and tube, C4 sparking wiring, C8 Tekken haiku, C9 joystick with lips and C11 Broken Prize Tag.

The pieces are built and wired in. Blind QC passed everything except the size of two pieces, and that question is now on the Desk. **Nothing is committed** (the orchestrator said no commits without the author's OK). The files are listed below.

## What was built

**Art.** `Tools/content_generation/absinthe_arcade/hd2d/closet_wall_props.py` (new, re-runnable from the repo root). It places each approved reference on its wall in room tiles and warps it through the closet's paint camera onto the night plate. The paint shader throws away pixels with alpha < 0.5, so each sprite is a composite: plate plus piece, cut out with a 3 px margin. It writes:
- `aa_int_closet_night_uv.png`: the blacklight-on plate, with a UV Purple #9400D3 wash on the back and left walls and a lavender bloom under the tube. The room's emit map protects the green marquee, the screens and the inks.
- Into `props/`: 21 sprites plus emit masks, merged into `aa_closet_props.json`. They are bl_switch off/on, bl_tube off/on, wiring idle/spark, haiku off/on, joystick faint/glowing/faint_uv/glowing_uv, and prize_tag hanging/hanging_uv/collected.
- `--sheet <out.jpg>` draws the gate-C review sheet.

**Code.**
- `game/core/closet_props.gd`:
  - New flag `debaucheryville.absinthe_arcade.closet_blacklight_on`, registered as ruled in `game/assets/data/world_data/quest_flags.json` after the orchestrator's validator note.
  - The haiku shows and can be read only with the light on (author, bcnr-q8).
  - Spark loop: a burst every 2-5 s, lasting 0.5 s, and one at once when the leader is in zap range.
  - `art_state()`.
- `game/worlds/debaucheryville/plate_prop_layer.gd`: `set_wall_quad()` lays a decal's quad on its side wall, so it sorts against the bros as the wall does.
- `absinthe_arcade_maintenance_closet_hd2d.gd`:
  - Six new PROPS.
  - The switch toggles both the plate and the art.
  - A hidden haiku or joystick leaves the interact group, so it never blocks what is behind it.
  - New and moved interact points: switch, joystick, haiku and wiring junction.

**Placement.** The bros walk only z <= 7.6, and the painted graffiti fills the left wall up to the door. So the switch, joystick and haiku sit on the free wall just in front of the door, as in the approved mock-ups. The wiring is mirrored so its junction box is at z ~7.6, within zap reach.

## Validation

- GUT (with `--import`): `test_maintenance_closet` 7/7 and `test_absinthe_completion_lines` 24/24, including new tests for the blacklight, art states, spark timing, sprites, wall quads and the plate swap.
- `test_quest_data` has 5 failures. They fail with the committed `quest_flags.json` too, and come from other sessions' uncommitted quest edits, not from this build.
- `tools/validate_data.py`: 0 FAIL.
- Blind gate C (Sonnet), log lines `aa_closet_build` rounds 1-3 in `dev/asset_team/reviews/qc_log.jsonl`:
  - R1: the switch toggle didn't read and the switch was oversized. Tag 2x, haiku over a pipe, faint UV joystick too faint.
  - R2 (fix 1): only the switch toggle failed.
  - R3 (fix 2): failed on scale. Measured against the painted door, the switch and joystick are about 2x the brief.
  - Under QC.md that sends it to the author.
- **Desk: `Eurobound-ms3r-q2`** ("Arcade closet: the switch and joystick fail blind QC on size. Which size do we ship?"). Options:
  - shrink the joystick and keep the switch (recommended);
  - shrink both;
  - keep both;
  - a bigger switch and a smaller joystick.
  - Images: `aa_closet_build_desk_scale.jpg`, `aa_closet_build_r3.jpg`.
- Not run: A5 in-game shots (Tools/critic_loop has no closet shot list).

## Where things stand

- Eurobound-ms3r is **blocked** on Eurobound-ms3r-q2, with a progress comment on the bead. The Asset Board row `int-aa_closet_build` is parked and points at the Desk card. A feed entry was added and the bead page synced.
- On the answer: change the two placements in `closet_wall_props.py`, which must match the `PROPS` spans in the room script. Re-run it, re-run `--sheet`, run a fresh blind gate C, run GUT `--select maintenance_closet`, then ask to commit.
- Still open inside ms3r (not part of the five):
  - C5-C7 graffiti split and inpaint (the painted graffiti still glows with the light off);
  - C10 chandelier cut-out, hotspot and animation, plus the tag pickup. There is no approved pickup line, and `cmr_broken_prize_tag` has no engine item entry.
  - C12 door layer;
  - A5.
- New durable finding (`bd remember`): the closet plate is not to the room's tile scale (the painted door is about 3 tiles), so size closet props against the painted fixtures.

## Changed files (uncommitted, this window's only)

- New: `Tools/content_generation/absinthe_arcade/hd2d/closet_wall_props.py`; `game/assets/worlds/debaucheryville/absinthe_arcade/interior/closet/aa_int_closet_night_uv.png` (+ `.import`); in `.../closet/props/`, every `aa_closet_bl_switch_*`, `aa_closet_bl_tube_*`, `aa_closet_wiring_*`, `aa_closet_haiku_*`, `aa_closet_joystick_*`, `aa_closet_prize_tag_*` PNG (+ their `.import`); `dev/asset_team/reviews/aa_closet_build_r1.jpg`, `_r2.jpg`, `_r3.jpg`, `aa_closet_build_desk_scale.jpg`; this handoff.
- Modified: `game/core/closet_props.gd`, `game/worlds/debaucheryville/plate_prop_layer.gd`, `game/worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.gd`, `game/tests/unit/test_maintenance_closet.gd`, `game/tests/unit/test_absinthe_completion_lines.gd`, `.../closet/props/aa_closet_props.json`, `dev/asset_team/reviews/qc_log.jsonl` (3 lines).
- Shared: `game/assets/data/world_data/quest_flags.json`. Only the `closet_blacklight_on` entry is mine; other sessions have uncommitted edits in the same file.
- Not mine, do not commit: the `.import` files that the GUT import made for the older closet props (`aa_closet_crt_*`, `aa_closet_ddr_arrow_*`, `aa_closet_sock_chute`).

## Paused (author, 2026-11-16)

The Production Desk Orchestrator relayed a pause on all asset creation. Author, verbatim: "Pause all asset creations of all types while I do a few more tests before I hand you the new workflow that we are to use to generate assets." Nothing was generating in this window when it arrived; the files above are left as they are.

## Next step

Wait for the author's new asset workflow. The Desk answer on Eurobound-ms3r-q2 comes back to this window name through the relay, but even with it in hand, do not re-run `closet_wall_props.py` or start the "On the answer" steps until the pause is lifted, then check them against the new workflow. This window can be cleared.
