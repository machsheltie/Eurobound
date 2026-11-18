Window: Asset Development Team (2026-11-18; pickup note for the next task, NOT started)

# Pickup: Eurobound-u5xn, Rhinestone Shirt of Shame Tripo rebuild

The previous task in this window was zx7u (handoff `2026-11-18_asset_development_team_zx7u.md`, done). The orchestrator sent u5xn, but the window's context was long, so the task is recorded here for a fresh session. Nothing for u5xn has been started: no Chrome, no Tripo credits.

## Author answer (Eurobound Desk Eurobound-u5xn-q1), verbatim
"Rebuild the model in Tripo (about 130 credits) and re-check /"

## What was wrong (from the orchestrator)
- Tripo split the shirt's back open like a jacket.
- It painted a stone sash down the back, where the approved back reference has only a small cluster of stones at the shoulder.
- It left out the sweat patch.

The icon itself had passed. See `2026-11-16_asset_development_team_u5xn_tshirt.md` and `dev/asset_team/reviews/qc_log.jsonl` (rhinestone_shirt_of_shame, A4 rounds 1-2).

## Steps (orchestrator's brief)
1. **Check Chrome first.** Make sure the agents' Chrome window can be used for the Tripo website. Yesterday it was minimized at screenX -21333. If it can't be used, stop at once and SendMessage the Production Desk Orchestrator. Don't force the window.
2. **Rebuild** following `design/style_guides/tripo_asset_workflow.md`:
   - Tripo website only, never the API.
   - Smart Mesh from the four approved views, 10k polygon budget.
   - Smart UV, then texture, then export as GLB. Mind the export gotchas in the workflow doc (Chrome drops downloads; use GLB).
3. **Review.** Run blind gate A4 on the model's back as well as the icon. Re-render the icon only if the model looks different straight on; if the front is unchanged, keep the shipped icon.
4. **Credits.** Log the credits used. If the back still fails after the allowed fix rounds, take it to the Desk under the window name "Asset Development Team". Don't spend more credits.

## Rules
- Close Chrome tabs and Blender when done.
- No .glb or .fbx in any commit. A commit run is in progress, so don't commit anything yourself.
- No git stash, reset or checkout.
- File anything you find with `bead_new.py`.
- Update the Asset Board.

## When done
1. Sync the bead page.
2. Write `docs/handoffs/2026-11-18_asset_development_team_u5xn_shirt.md`, with the window name first.
3. SendMessage the Production Desk Orchestrator a summary.
