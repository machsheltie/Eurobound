# Sprite Development Team: handoff, 2026-11-17 (Eurobound-1nwj, look-B walk arm)

The Production Desk Orchestrator assigned one task: check whether Eurobound-1nwj still applies under the binding workflow `design/style_guides/tripo_asset_workflow.md`, and fix it or close it.

## Result: closed as superseded

No frames were re-rendered. No Blender or Godot was run, and no Tripo credits were used.

Evidence (also in the bead comment):
1. **The workflow replaces the look-B pipeline.** Since 2026-11-16, every character is a Tripo-rigged GLB with its own idle and walk, and the workflow says it replaces the char3d look-B rebuilds. The old look-B walk frames therefore get replaced, not re-rendered with walk_arm 6 / walk_elbow 4.
2. **The non-bro walk frames are never shown in game.** Nine hall NPCs ship look_b folders: accounts_receivable_accounts, accounts_receivable_receivable, ashleigh, brynleigh, cara, jakub_tokens_dvorak, kenleigh, tomas_two_fifty and tomas_two_fifty_ring.
   - Hall NPCs only stand. `hall_npc.gd` never sets `sprite.action`.
   - The only code that switches a sprite to walk is `player_controller.gd:320-350`, for the party.
   - So the arm fault is in the files but never appears on screen, and blind in-game QC has nothing to judge. That is why there was no QC round.
3. **The only on-screen instance is Lord Pilsner's look_b walk** (`character_looks.json`: lord_pilsner = 3d). Pilsner is the author's own and was not touched.

## Filed

- **Eurobound-x3lw (P3, cleanup):** retire each hall NPC's look_b folder once its workflow GLB replaces it in the hall. The walk/ half is 1,008 tracked PNGs (about 77 MB). It also covers the HALL_NPCS entries and the jakub assertion at `test_hall_npc.gd:59`. Don't delete any NPC's frames before its replacement exists, because the idle frames are live.

## State

- The bead page is synced and acked.
- No files were changed except this handoff and the bead DB. Nothing is committed.
- No processes were started.
- Whitney (Eurobound-p7n6.6) stays parked on Desk p7n6.6-q5.

This window can be cleared.
