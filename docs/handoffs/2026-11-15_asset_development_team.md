Window: Asset Development Team (asset-team orchestrator, "eurobound-c8")

# Handoff: Asset Development Team, 2026-11-15

Under the one-task rule (bead Eurobound-jpkw), this window takes no new work. Desk answers addressed to "Asset Development Team" reach the next window as fresh single tasks, relayed by the Absinthe Orchestrator.

**Read first:**
- `dev/asset_team/TEAM_BRIEF.md`
- `dev/asset_team/QC.md`
- `dev/qc/QC_COVERAGE.md` (gates C, U and V, around line 205)
- `dev/asset_team/PAINT_JOB.md`
- `Tools/item3d/README.md`
- the repo `CLAUDE.md` files
- `bd prime` (bd memories `tripo-background-tab-0x0-viewport` and `3d-item-icons-flat-or-thin-items-cards`)

## Done (on `main`, pushed)

| Asset | Commit | Notes |
|---|---|---|
| Space Cake Timer UI | c1f094a4 | Gate U pass. Fixed 192x64 panel, plus `space_cake_timer_panel.json`. |
| Shady Loot Crate Voucher icon | ef2d1fc2 | Blender card. |
| Millennium Bug NFT, plus shared `Tools/item3d/nft_slab.py` | 6c999e88 | |
| Sea-Monkeys NFT | a3895f59 | |
| Napster NFT; `nft_slab.py --curl-corner` added | 6b7087f2 | The default output is unchanged. |
| Meme Lord's First Selfie NFT | 423c4d4e | |
| Used Glitter Hat | 46103d13 | |
| Already Spent Credit | 8997f051 | The reverse emblem was drawn by the builder from the facade token, because no Arcade emblem art exists. It is not visible in the icon. |
| Cracked Mirror Shard | ac1f2de6 | |
| Mango OG Gushers fix (coffee ring cut) | 45fb828a | |
| Casting-Call Flyer correction | c5f39499 | |
| Clock Snow Globe | 000e0624 | |
| VIP All-Access Wristband ("Je mi 7!") | 457996cc | |
| Battle HUD look trial: `Tools/item3d/hud_badge.py`, Grease Fingers, Embarrassed | a57573b6 | |
| Arcade Closet reference set, plus `cmr_broken_prize_tag` icon | 863d0337 | |
| Street cabinet protocol trial (nhxz.9), Phase B | 1e403bf4 | The author approved it. The 3072 atlas is allowed for this cabinet only. |
| Bottoms Down plan, author-approved | 5bd795e8, 937ab597 | |
| Hall fix folder README | 937ab597 | |

- Every review is in `dev/asset_team/reviews/qc_log.jsonl`.
- The author kept the shipped velvet wristband, so its correction branch was dropped.

## Uncommitted

- `design/items/leopard_print_thong_item.md` line 183 is my one-line edit. The icon size now follows the 3D standard, under the 2026-11-13 "all icons 3D" ruling. The file sits in the Writers' Room's uncommitted batch, and eurobound-2b was asked to commit it.
- Untracked `*.png.import` files under `game/assets/items/icons/3d/` are Godot churn from other sessions. Do not commit them.

## Open Desk cards (window "Asset Development Team")

| Desk doc id | Question | Worktree to resume (`.claude/worktrees/…`) and next step |
|---|---|---|
| `asset-team-arcade-closet-reference-set` | Approve the five closet items? | Merged. On approval, build or wire them per the answer, as the Hall set was done. |
| `asset-team-garment-icon-method` | Should all clothing icons go reference-first? (A Firefly reference is blind-reviewed, then projected onto a flat 3D slab, at 0 credits.) | Decides the method for the T-shirt, thong and rhinestone shirt (`agent-a12c61dec948704fc`, held). |
| `asset-team-hud-look-trial` | Approve the HUD badge look? | Build the other 24 of `design/ux/battle_hud_icon_pictures.md` with `hud_badge.py`, in batches of 4, through gate U. |
| `asset-team-info-hall-fix-folder` | The author fixes the hall plates in `Assets/Graphics/worlds/debaucheryville/absinthearcade/author_fix_monday/`. | On "Done": copy the plates into `game/assets/worlds/debaucheryville/absinthe_arcade/interior/hall/` and hand them to the Arcade window (bead fbqk). Then do 3.1b in `agent-ada783cbf789ee2ee`. |
| `asset-team-qc-aa_broken_symbol_handheld-cracks` | The brief's plum cracks are invisible at 128. Allow a light edge? | `agent-a5d8d154f6335727e` (Tripo build; the GLB `dev/asset_team/icon_refs/aa_broken_symbol_handheld_tripo.glb` is gitignored). One texture round, then A4. |
| `asset-team-qc-bottoms_down-cleanup` | Add the plates to the author's Monday Photoshop folder? | `agent-a4183eadfc06dcad5`. Design passed; the clean-up artefacts remain. |
| `asset-team-qc-i_survived_tshirt` | Which route? | `agent-a38be739d6c174cf5`. The lettering and print pass; the shape fails. |
| `asset-team-qc-item_kokos_loco_bucket-gloss` | Use the Firefly reference as the icon (an exception to 3D-only), accept the gloss render, or park it? | `agent-a022cce6e188332b1`. The reference is `dev/asset_team/icon_refs/item_kokos_loco_bucket_ref.png` (passed A3); the GLB is gitignored. |
| `asset-team-qc-item_leopard_print_thong` | Which route? | `agent-a49b8c8cacede0b53`. |

## Next step

1. Act on each Desk answer as it arrives.
2. With no answers, the queue still holds:
   - Space Cake items waiting on Writers' Room descriptions (Contact High object, onset rings, vignette, sting icon) or on the writing round (two dialogue plates);
   - about 80 legacy pixel icons waiting on Writers' Room descriptions.
3. One question to the author, asked in chat, is still unanswered: should the 57 finished 3D icons be swapped into `game/assets/items/icons/`, with the pixel originals retired to a legacy folder? Do nothing without a yes.

## Beads touched

- Eurobound-d3x: handheld and team umbrella.
- Eurobound-rpac: Writers' Room item briefs, Kokos, garments.
- Eurobound-g579: Bottoms Down.
- Eurobound-fbqk: hall wiring.
- Eurobound-du51: battle HUD.
- Eurobound-ms3r: closet.
- Eurobound-nhxz.9: cabinet trial.
- Eurobound-k3qa: Space Cake.
- Eurobound-1nvh (new, open): a Blender lock helper. "Is blender.exe running?" checks race; about five overlaps happened.

## Lessons (not yet in team docs)

- **Soft garments fail as Blender-scripted slabs.** Hard objects (cards, tokens, lathes, globes) pass, often first try.
- **The toon render darkens textures.** Agents must measure the RENDERED pixels against the brief's hex values.
- **Another session keeps `docs/superpowers/NEXT_WORK.md` staged,** so merges fail. Use `git checkout <branch> -- <files>`, then `git commit -- <files>`. Never touch their staged file.
- **Firefly:** one image agent at a time. Use active tabs only; a background tab has a 0x0 viewport and freezes.
- **Pillow-drawn props get rejected** (TEAM_BRIEF §3). Pillow is for typed lettering and cleanup only.
- **Briefs that ask for a light edge** have to come from the brief, never from the orchestrator. Otherwise reviewers fail it for contradicting the brief.
