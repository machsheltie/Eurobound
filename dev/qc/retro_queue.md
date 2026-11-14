# Retroactive blind-review queue (bead Eurobound-lrg5, under Eurobound-2boh)

Author ruling (2026-11-14): "be sure ALL types of assets/sprites are being reviewed by our blind agents". This queue lists assets accepted, merged or in the game with NO passing blind-review line in `dev/asset_team/reviews/qc_log.jsonl` or `Tools/char3d/qc_log.jsonl`. Gates are in `dev/asset_team/QC.md`, `Tools/char3d/QC.md` and `dev/qc/QC_COVERAGE.md`.

Built 2026-11-14 from: `git log --since=2026-11-01` on `game/assets` and `Assets/Graphics` (2,292 distinct paths), both qc_logs (117 lines), and the Sprite and Asset team accounts passed in by the coordinator. The Asset Board is a live artifact, not a repo file, so its "done" rows could not be read directly; the teams' own lists stand in for it. The Asset team's 62-row plate list is summarised below, not itemised.

Priority: P1 = in the game now and author-facing, P2 = in the game now, not prominent, or current work awaiting review, P3 = decision needed first. Order inside a priority is the order to run.

## Active queue

| # | Type | Path | Gate needed | Priority | Why it has no passing line |
|---|---|---|---|---|---|
| 1 | Party 3D model + frames | `game/assets/characters/party/lord_pilsner/look_b/` (112 files), `Assets/Graphics/characters3d/lord_pilsner/` | G3 (model, reference-locked) then G4 (idle and walk, 8 dir) | P1 | Approved by the author's 1:1 hall check on 2026-11-13, before QC existed. No Pilsner line in the char3d log. Author 2026-11-14 (lrg5-q1): "Review them and fix whatever fails, like any other asset". |
| 2 | Party 3D model | `Assets/Graphics/characters3d/lord_pilsner_v2/` (the painting look B was built from) | G3 | P1 | Same. It is also the A5 critic-loop reference for the two Pilsner shots, so an unreviewed reference anchors a score. Author 2026-11-14 (lrg5-q1): "Review them and fix whatever fails, like any other asset". |
| 3 | Enemy battle sprites, 15 | `game/assets/characters/enemies/absinthe_arcade/*_battle_w.png`: accounts_receivable, condiment_clan_ninja chili / garlic / mystery_brown, count_continue, croc_monsieur, hit_and_ponder_hatchback, player_two_palette_swap cocktail_pink / nicotine_beige / scrubs_green / teal, shish_kahn, sinking_fund, super_turbo_hyper_jarmila, two_seventy_vratislav | E | at redo (p7n6) | In the Arcade battle data (`debaucheryville_arcade_battle.json`). Old pixel pipeline, never blind-reviewed. | QC owner 2026-11-14: these are pixel art and the author ruled all pixel art is redone in 3D (Eurobound-p7n6), so gate E runs on the 3D versions, not these.
| 4 | Enemy model sheets, 9 | `Assets/Graphics/sprites/characters/enemies/absinthe_arcade/model_sheets/*` | G1 Checklist A (the sheet is the reference for gate E, so review it first) | P1 | No lines. |
| 5 | Audio, 3 | `game/assets/audio/icq/icq_uh_oh.ogg`, `game/assets/audio/velvet_curtain_club/qr_code_scan_beep.ogg`, `.../vip_bathroom_nft_discovery.ogg` | S (S-a cue sheet, S-b author listen) | P1 | In the game; no audio gate existed. |
| 6 | Portraits (G1 missing), 8 | jakub_portrait_v2, tomas_two_fifty, cara, woo_woo_whitney, brynleigh, ashleigh, kenleigh, accounts_receivable_accounts (`Assets/Graphics/characters3d/<id>/`) | G1 | P2 | Approved on the Desk before G1 existed. The log shows only G2 passes for them, and G2 compares the Tripo source to the unreviewed portrait, so the chain starts unchecked. Run G1 first; a G1 fail voids the G2 line. |
| 7 | Special-pose frames | `game/assets/characters/npcs/absinthe_arcade/jakub_tokens_dvorak_asleep_statue.png`, `..._asleep_cradled.png`, and `Assets/Graphics/sprites/characters/npcs/absinthe_arcade/jakub_tokens_dvorak_asleep_statue.png` | G4-S | P1 | In the game (Green Fairy statue scene). No single-frame gate existed. |
| 8 | Jakub 3D buttons (stamp_text lettering) | `Assets/Graphics/characters3d/jakub/` texture | G4-T | P2 | Known issues from the Sprite team: a cream rim and a wedge on the "1". Expect REVISION REQUIRED; run to get it on record. |
| 9 | Models with G3 not yet run | Bradley, Jakub, the seven-NPC batch (`Assets/Graphics/characters3d/`: woo_woo_whitney, brynleigh, ashleigh, kenleigh, tomas_two_fifty, cara, accounts_receivable_accounts) and the RECEIVABLE twin (`accounts_receivable_receivable`) | G3 (reference-locked), then G4 | P2 | Queued on the Sprite team's side already; listed so the 2boh audit sees it. Their G2 lines exist. dr_vanek has G1 only: G2 and G3 pending. |
| 10 | Item icon with no passing A4 | `game/assets/items/icons/3d/aa_prize_highlighter_hydro_bro_2000_512.png` (+ `_128`) | A4 (fresh review of the whole gate) | P1 | qc_log has four A4 lines for it and all are fails (rounds ending 2026-11-14), and A3 passed. It is in the repo. If the mechanical colour fix (to "highlighter yellow") was applied, it needs the fresh whole-gate review the QC.md exception demands. |
| 11 | Item icon, fallback pass | `aa_prize_sobriety_test_deluxe_512.png` | A4 (fresh) | P2 | Last A4 lines: a fail dated 2026-11-14, then an undated pass noted "explicitly identified fallback, pre-rollout". Not a clean blind pass. |
| 12 | Item icon, trial | `opener_crown_and_cask_512.png` | A3 + A4 | P2 | The Crown & Cask trial the author approved ("make all icons this way"). No qc_log line at all. |
| 13 | Protocol trial outputs (Chadwick) | SAM masks line exists; material manifest, zoned texture and `Tools/qc_review/reports/chadwick_qa_round1.*` | G4-T plus `review_3d.py` step-10 report | P2 | Only the masks have a log line. Chadwick G3 and G4 are in the failed-three-times state and with the author on the Desk; do not re-run until the Desk answers. |
| 14 | Item icons, legacy pixel (about 40 `weapon_*`, `windows_mobile_pda_phone` and similar, `_64` and `_128`) | `game/assets/items/icons/*_64.png`, `*_128.png` | none: retired, redone in 3D look B and reviewed then (A3/A4) | retired | Superseded for new icons (author 2026-11-12, "stop pixel art"). Author decision below. |

## Done (pre-QC), reviewed at repaint (Asset team's QC-owner decision)

The Asset team's 62 location plate rows merged before the gates get NO retro A2 now. The author ruled a full Writers' Room rewrite and repaint of every location, so each plate gets its blind A2 (and A2+) when it is repainted. They are marked "done (pre-QC), reviewed at repaint" and are not queued.

| Group | Path | Count | Note |
|---|---|---|---|
| Shamsterdam and Debaucheryville exterior and interior plates | `game/assets/worlds/<city>/<location>/{exterior,interior}/` (about 28 locations: Hoisted Pint, Pancake House, Kapsalon Koning, Leeman's Doner Palace, Bicycle Warfare Accessories, Mad Monarch's Wit Tea Party, Velvet Curtain Club and VIP stall, Cirque du Shady, Cyberspace Kavarna, Shadow Exchange, Euro Ink 4 Less, Hostel Midnight Checkout, and the rest) | 62 rows (32 exteriors, 30 interiors), per the Asset team | Listed by the Asset team. Already blind-reviewed: the_tolerance_hostel (A2 pass 2026-11-13) and de_zilte_waarheid (A2 pass). The_wobbly_windmill_brewery, bottoms_down and de_groene_gids only have A2 fails in the log and are also covered by the repaint ruling. |
| Arcade props | `game/assets/worlds/debaucheryville/absinthe_arcade/**/props/` (9 interior prop rows inside the 62; the wider tree holds about 222 files: exterior faces and props, hall, closet, mirror corridor, taproom maze, depth layers, battle backdrops) | 9 rows | Covered by the Arcade rework (Eurobound-bcnr, the interactables rule). Review under A2+ and gate C when the reworked pieces land. The 4 battle backdrops take gate T then. |

## Not queued, and why

- **Old pixel character sprites** (`Assets/Graphics/sprites/characters/party_members/*` about 1,385 files, the 15 NPC `.aseprite` under `game/assets/characters/npcs/`, and their model sheets): all replaced under p7n6 (Tripo + Blender). No review.
- **Item icons passing A3 and A4 on a dated pass:** all other icons in `icons/3d` (25 of the 29 in git) have blind passes.
- **Crowd groups, standalone NFT art, UI sheets, VFX atlases, tilesets (empty folders under `Assets/Graphics/tilesets`), city area plates, key art images:** none produced yet. Their gates are written (G4-C, N, U, V, T, A1/A2, K). The key-art doc is text only.
- **A5 in-game critic scores:** only `arcade_hall` has a shot list; other wired scenes have no A5 coverage (not a retro review; a gap for the 2boh audit).

## Author decisions needed

1. Legacy pixel icons (row 14): review them under gate C, or declare them retired and have the Item team replace them with look B on a schedule?
2. Audio (row 5): is the author's ear (gate S-b) the final judge for tone, with the agent cue sheet only screening technical faults?
3. Pilsner (rows 1 and 2): the author's 1:1 hall check approved him. Does the retro G3/G4 pass count as a formality for the log, or may a REVISION REQUIRED reopen an approved look?


## Author answers (2026-11-14)
- lrg5-q1 (Pilsner and other author-approved art): "Review them and fix whatever fails, like any other asset".
- lrg5-q2 (audio): "The agent's check is enough; I'll hear them in game". Gate S runs S-a only.
- lrg5-q3 (legacy pixel icons): "Retire them: redo each in 3D look B (reviewed then)".
