Window: Asset Development Team (second window of the day, after the eurobound-c8 handoff)

# Handoff: Asset Development Team, 2026-11-15 (window 2)

Under the one-task rule (bead Eurobound-jpkw), this window did one bookkeeping task and stops. The previous handoff is `docs/handoffs/2026-11-15_asset_development_team.md`; read it first.

## What came in

The Production Desk Orchestrator (formerly the Absinthe Orchestrator) relayed nine Desk answers. All nine are reflected on the Asset Board (https://claude.ai/artifact/52rttv6iaR89LY9PynE7dM), with three feed entries.

| Desk card | Answer | Where it went |
|---|---|---|
| `asset-team-qc-item_kokos_loco_bucket-gloss` | B: accept the glossy render | **Done.** Committed to main in 3188b2de, from `worktree-agent-a022cce6e188332b1`. The QC log records the author's acceptance. Board row set to done. |
| `asset-team-qc-aa_broken_symbol_handheld-cracks` | A: thin light edge on the cracks | Ready bead **Eurobound-rspb**. Board row queued. |
| `asset-team-qc-bottoms_down-cleanup` | A: add to my Monday Photoshop folder | **Done.** See the next section. |
| `asset-team-garment-icon-method` | Reference-first for all clothing | Ready bead **Eurobound-u5xn** (T-shirt, thong, rhinestone shirt). Board rows queued. |
| `asset-team-qc-item_leopard_print_thong` | A: Firefly reference on a flat 3D slab | Eurobound-u5xn |
| `asset-team-qc-i_survived_tshirt` | A: Firefly reference on a flat 3D shape | Eurobound-u5xn |
| `asset-team-hud-look-trial` | Not right: redo the badge. "This is very generic" | Bead Eurobound-du51 (open). Board: the two trial badges are set to redo, and the 24 parked rows wait on a new look. |
| `asset-team-arcade-closet-reference-set` | Approve all five: build them | Bead Eurobound-ms3r (open). Build them as the hall set was built. |
| `asset-team-icon-swap-live-folder` (posted this window; it was asked in chat before) | Swap as they're finished; pixel twins to a legacy folder | Ready bead **Eurobound-952g**. |

## Bottoms Down

- The seven plates from `worktree-agent-a4183eadfc06dcad5` (ba615521) were copied to `Assets/Graphics/worlds/debaucheryville/absinthearcade/author_fix_monday/bottoms_down/`. The PNGs are gitignored. The README there lists the four spots.
- The parent README points to it. Both READMEs are in 3188b2de.
- New Desk info card: `asset-team-info-bottoms-down-fix-folder`. The author taps Done after the fix.
- Eurobound-g579 is blocked until then.
- On Done:
  1. copy the plates into `game/assets/worlds/shamsterdam/bottoms_down/`, together with the branch's exterior props, `placement.json`, prompts and reviews;
  2. run blind A2;
  3. commit to main.

## Found this window

- **The broken handheld's R2/R3 screen paint is lost.** The previous agent painted it from a script in its scratch folder, which is deleted. The GLB holds only the raw Tripo texture. Eurobound-rspb says to rebuild the paint as a committed script. Lesson: texture-fix scripts belong in `Tools/item3d/`, never only in scratch.
- **Stopped the leftover eurobound-c8 timer** (session cron 13b3bafd, every 20 min). It went against the "don't poll" and one-task rules, and the Production Desk Orchestrator does the relaying.
- `docs/superpowers/NEXT_WORK.md` is still staged by another session. It was left alone; this window committed with `git commit -- <paths>`.

## Uncommitted

Nothing from this window. Earlier items still stand (see the previous handoff):
- the thong doc's line-183 edit, in the Writers' Room batch;
- `.import` churn under `game/assets/items/icons/3d/`.

## Ready beads for fresh windows

- Eurobound-rspb: broken handheld crack round.
- Eurobound-u5xn: garment icons, reference-first.
- Eurobound-952g: promote 3D icons, pixel twins to legacy.
- Eurobound-du51: HUD badge look redo.
- Eurobound-ms3r: closet build.

Still open on the Desk for this window: `asset-team-info-hall-fix-folder` and `asset-team-info-bottoms-down-fix-folder`.

Bead page synced (sync_check acked).
