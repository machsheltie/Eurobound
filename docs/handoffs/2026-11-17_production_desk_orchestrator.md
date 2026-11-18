Window: Production Desk Orchestrator

# Handoff: Production Desk Orchestrator, 2026-11-17

Head orchestrator for every Eurobound window and agent. The role is set out in the auto-memory `feedback_main_orchestrator.md`. Read it first: it includes today's **standing dispatch order** from the author. The previous handoff was `eurobound_handoff_production_desk_orchestrator_2026-11-17.md` in the user Temp folder.

## Standing order (author, 2026-11-17)
"once a task is no longer in need of my feedback, you are to go ahead and dispatch it to the correct windows agents to work on it or if there is not a window for it you may generate your own agent team in your window. Remember, each subagent completes one task and then must be replaced by a new agent with fresh context."
- Keep up to 4 subagents busy from `bd ready`. Only one Godot job at a time.
- Send work to the team windows (Sprite / Asset / Writing Room / Beads Deployment) when it fits them.
- Never give a finished agent a second task. Resuming one only to finish the same task is fine.
- The author found nothing deployed this morning because a cleared orchestrator only relayed. Don't repeat that.

## Relay (re-arm after a restart)
- Run `ArtifactComments watch` on the Desk https://claude.ai/artifact/Pm3AgZ5qHqqmcoRcEv52JF.
- Keep the fallback cron at `17,47 * * * *`. Today's job was c4a53c0e, which is session-only and dies with this window, so recreate it.
- Do one catch-up pass of `questions` where status==answered and relayed==false, plus `playtest_notes` where status==new.
- A Desk card missing the `relayed` field never matches the relay query. Today `asset-team-info-bottoms-down-fix-folder` had to be patched to `relayed:false`.

## Waiting on the author (Desk cards posted today, all window "Production Desk Orchestrator" unless noted)
- **Commit:** orch-commit-2026-11-17 asks to commit and push today's work. It is the biggest unblocker: agents keep skipping files that carry uncommitted edits.
- **Battle and mechanics:** 7468-q1, c1gt-q1..q5, iqgo-q1..q4, 397r-q1, ew1h-q1, sogp-q1, tcip-q1/q2, 028k-q2 (progression proposal), mb38-q1, 4062-q1, 7t5b-q1 (titles).
- **World:** eaiq-q13 (final district map), zkgt-q1, zwpf-q1, 4wvc-q1 (north wing: L-wing ruling vs rectangular build), 9tz9-q3 (Kamil or Vlad), p1y-q5, 9x55-q1, xo6e-q1, 3ddh-q1 + z39e-q1 (Club Flyers), yyp6-q1, wo9l-q1.
- **Assets:** u5xn-q2 (garment method; thong waits on it), d4i6-q1 (cat wall), 59b9-q1..q3 (north wing door; Sprite window), zx7u-q1..q3 (masks; Asset window), gcnd-q1.
- **Earlier and still open:** the two Photoshop fix folders, p7n6.6-q5 (Whitney; Sprite window), u5xn-q1, xnpg-wr1 (OpenRouter top-up; blocks the whole Writing Room batch), c8xn-wr2 and c8xn-q9 (story; Writing Room), es6t-q1, jsd0-q1, 8snp-q2, 4ynh-q9, jlzw-q1, 8hjb-q1, f3tq-q15, beads-deployment-team-window-names-mobile.

## Blocked on Chrome (the agents' Chrome window is minimized; screenX -21333)
Three Gemini wall fills are prepped and waiting:
- **59b9 north wing:** run `north_wing_cutouts.py --fill`, then gate C.
- **j9ru taproom chalice:** run cut_plate_prop.py composite; the steps are in docs/handoffs/2026-11-17_asset_development_team_j9ru.md.
- **d4i6 cat wall:** waits on d4i6-q1 as well.

## Running at handoff
- 10g6: per-plate prop boxes, holding the Godot slot.
- 4jln: docs for undocumented engine items.
- gora: Club Flyers item docs.
- csbg + gt26: Debaucheryville data leftovers.

Check `bd list --status in_progress` for their results.

## Godot queue (one at a time)
- Done today: 10g6, 0wn9, 0dde, and the 9l8k reimport check (arcade 128/128).
- 0dde moved Embarrassed's numbers into data. It also added charm -20%, because the old hard-coded ×0.8 hit Charm attacks too, and the 0.4 rounding drifts slightly. Mention both to the author if Embarrassed balance comes up.
- Also done today: a4zx, ny6e, izct (partial; Desk izct-q1), spr0 (built and tested; blocked on fbqk placement, t1gn equipment, Desk 8hk2-q1 and 8xiq-q1, and zihc for the Writing Room), b6qu, z3ec (partial; Desk z3ec-q1), lpki, 81oy (partial; Desk 81oy-q1).
- The full GUT suite was 1333/1334 during spr0; b6qu fixed the one failure.
- Queue now: k3qa (Space Cake cue consumers), 7rdd, 4med, j94r, toqp (door lamp files picked up as door states; fix when the door is wired).
- Field-menu item use still skips the Green Fairy `self_status_risk` roll (from 81oy). File it if wanted.
- izct: dialogue box status effects.
- k3qa: Space Cake cue consumers.
- ny6e: Crash GUT test.
- 7rdd, 81oy, 4med, j94r, spr0, z3ec.
- d7m1: train travel, a large job; check its Desk numbers first.
- Wiring the staged north wing, chalice and cat pieces, after gate C and the Desk answers.
- ka3c waits on the rry7 bug fix.

## Team windows
**Closed by the author on the evening of 2026-11-17 to free memory.** Start from `docs/handoffs/2026-11-17_team_windows_resume.md`: it has each window's handoffs, its open Desk cards, what it does next, and how to reopen it under the right name. While a team window is closed, act on its relayed answers with a fresh subagent, or reopen the window first.


All four (Sprite Development Team, Asset Development Team, Beads Deployment Team, Writing Room) finished their tasks today and wrote handoffs in docs/handoffs/2026-11-17_*. The author was asked to clear them. Asset and Beads said their context was very long, so don't send them more until they are cleared.

## Gotchas learned today
- Before trusting an agent's "skipped: another window's uncommitted edits", check `git diff`. Most of those edits were this orchestrator's own agents' work from yesterday and today; re-dispatch with clearance.
- `gut.py --import` runs the WHOLE suite after reimporting. Reimport with `<godot_bin.local> --headless --path game --import --quit`, then run `gut.py --select`.
- The general-purpose and gameplay-programmer agents stop at about 20 turns. Resume them with SendMessage to finish the same task.
- Agents of type gameplay-programmer, tools-programmer and ui-programmer have no ArtifactData. Use general-purpose when a task posts Desk cards or syncs the bead page, or do the sync yourself.
- Restarting Explorer earlier knocked the Claude desktop app's Equoria session offline. Don't kill Explorer or the desktop app casually.
- The NVIDIA GeForce Overlay can get stuck full-screen and topmost. Hide its window (ShowWindow SW_HIDE); killing it just respawns it.
- The catalog page refresh needs a read before publishing, and the publish has to be sent twice: the first is refused against the newer live version, the second goes through.
- The user settings already have `defaultMode: bypassPermissions`. Windows started earlier keep their own mode until switched with Shift+Tab. `dialogExpiry` is 60s, and the author was offered a longer value but hasn't answered.

## Uncommitted
Nothing was committed today. All work sits in the working tree and waits on orch-commit-2026-11-17. When approved: one commit agent, one commit per piece, `Tools/orchestrator/commit_paths.py`, never stash, reset or checkout, no .glb or .fbx, and run the full GUT suite first with no Blender running.
