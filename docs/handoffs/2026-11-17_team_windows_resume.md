Window: Production Desk Orchestrator (resume index for the four team windows)

# Resume here: team windows, 2026-11-17

On 2026-11-17 the author closed the four team windows to free memory; the laptop was down to 0.4 GB free. Each window finished its last task and wrote a handoff. This file is the starting point for whoever picks one of them up: a reopened window, or the orchestrator's own subagent.

## How to reopen a team window
1. Start a new Claude Code session in the Eurobound repo, then run `/rename <Window name>` with the exact name below. Desk answers are relayed by window name, so a window without that name never receives them.
2. Tell it: "Read docs/handoffs/2026-11-17_team_windows_resume.md, then your latest handoff, then do the next task the orchestrator sends." One task, then a handoff, then clear (see root CLAUDE.md and Tools/orchestrator/README.md, "Handoffs and window names").
3. **While a window is closed, the relay can't reach it.** The orchestrator either acts on the answer itself (with a fresh subagent) or reopens the window first. Every answer is also written on its bead, so nothing is lost.

## Sprite Development Team
- **Latest handoffs, newest first:**
  - `2026-11-17_sprite_development_team_59b9.md` (north wing cut-outs)
  - `..._d4i6.md` (window cat and doors)
  - `..._2bb9.md`
  - `..._1nwj_look_b_walk_arm.md`
  - `2026-11-16_sprite_development_team.md`
- **Waiting on the author:**
  - 59b9-q1, q2, q3 (north wing door accept, amber lamp, exterior-only opening)
  - d4i6-q1 (cat wall)
  - p7n6.6-q5 (Woo Woo Whitney: accept her, or rethink how NPCs read at the hall camera)
- **Waiting on Chrome:** the north wing Gemini fills. The prep is in `game/.../interior/north_wing/props_staged/gemini/`. Run `north_wing_cutouts.py --fill`, then gate C. The script now writes the per-plate boxes (10g6).
- **Next:**
  - Once p7n6.6-q5 is answered: the next Arcade NPC rebuild (objf, dg5p).
  - Once the north wing pieces pass gate C and the Desk: wiring (toqp; t562 marks them built).
  - Never touch the three bros (the author builds them).

## Asset Development Team
- **Latest handoffs, newest first:**
  - `2026-11-17_asset_development_team_zx7u.md` (masks and guides)
  - `..._ms3r_joystick.md`
  - `..._j9ru.md` (chalice: everything done except the Gemini wall fill)
  - `..._pg9a.md` (restroom statue; the scene step was done later by the orchestrator, bead closed)
  - `..._u5xn_tshirt.md`
- **Waiting on the author:**
  - u5xn-q1 (rhinestone shirt)
  - zx7u-q1, q2, q3 (outdoor masks, mirror corridor mask, scale guide labels)
  - the two Photoshop fix folders: asset-team-info-hall-fix-folder, asset-team-info-bottoms-down-fix-folder
  - u5xn-q2 (garment method; posted under the orchestrator's name, and it decides the thong)
- **Waiting on Chrome:** the j9ru chalice wall fill (exact steps in its handoff), and the d4i6 cat wall (also needs d4i6-q1).
- **Next:**
  - the thong (after u5xn-q2)
  - rspb is done; promote the broken handheld at commit time
  - o4n8 (hall plates bake the lit DDR glow)
  - wic3 (ghost lettering behind the Beanie claw)
  - Re-run `build_masks_guides.py` after any staged piece goes live.

## Beads Deployment Team
- **Latest handoffs, newest first:**
  - `2026-11-17_beads_deployment_team_4ynh_q9.md`
  - `..._8snp.md`
  - `..._jpkw.md`
  - `..._wqui_b8yo.md`
  - `..._small_fixes.md`
  - `..._8hjb.md`
  - `..._f3tq.md`
  - `..._ready_triage.md` (the ranked dispatch list)
- **Waiting on the author:**
  - 4ynh-q9 (NPC group 9; post group 10 after it)
  - 8hjb-q1 (doc format)
  - 8snp-q2 (hostel prices; post N2 after it, list on the bead)
  - f3tq-q15 (drunk-rule ranges)
  - beads-deployment-team-window-names-mobile (optional: /rename windows)
- **Next:** a fresh ready-queue triage. Many beads changed today, so re-rank them.

## Writing Room (formerly eurobound-2b)
- **Latest handoffs:** `2026-11-17_writing_room_desk_cards.md`, `2026-11-17_writing_room_story_q9.md`, `2026-11-15_eurobound_2b.md`.
- **Waiting on the author:**
  - c8xn-q9 (story question 9, Brenda; post the next one after it, and check story_core first, since the handoff lists questions it may already settle)
  - w5ra-q1, q2, q3
  - w7nx-q1
  - under the old name eurobound-2b: c8xn-wr2 (story session), xnpg-wr1 (OpenRouter top-up)
- **Blocked on OpenRouter credits (xnpg-wr1):**
  - 40tc, x2ws, 1n2u, lq6g, m6rc, y3r5, nu0k
  - lei5, 9tb7, ysi, g40c
  - 6j69 (street-loss text)
  - zihc (Backpack Girl State 4 order)
  - 3iwg
  - drafts requested on gora-q1, xo6e-q1, 9x55-q1 and zkgt-q1 if the author picks the Writers' Room route

## Orchestrator
See `2026-11-17_production_desk_orchestrator.md` for the relay re-arm, the Godot queue, the commit card and today's gotchas.
