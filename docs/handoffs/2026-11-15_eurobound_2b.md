# Handoff: eurobound-2b, Writers' Room moderator (2026-11-15)

**Window name: eurobound-2b.** This window moderates the Writers' Room (`WritingRoom/`). Under the one-task rule (bead Eurobound-jpkw), its last task is finished and **this window can be cleared.** Nothing is running. Desk answers sent to window "eurobound-2b" still reach whichever window takes the name next.

## How the room works (read these first)

- `WritingRoom/MODERATOR.md`, `WritingRoom/README.md`, and the auto-memory `project_writing_room.md` (roster, run rule, standing rules).
- **Roster (author, 2026-11-15):** Kimi K3 (finalizer), Aion 3.5, Gemini 3.8 Flash and GLM 5.3 FlashX, each at max_tokens 32000. It lives in `WritingRoom/room_config.json`. Only the author changes the roster.
- **Run rule:** one writer per foreground call, in this form: `timeout 585 python -u room.py round <task> --phase drafting --budget N --writers <Name> --no-advance`. If a writer times out, retry once with a narrower brief.
- Relay the author's words verbatim with `room.py note <task> "<text>"`.
- **Questions:** every author question goes to the Eurobound Desk (window "eurobound-2b"), never to chat.
- Run the 3a stand-up test on every bro line.
- **Banned words:** "Europe" is banned in player-facing text. Use Euromemeia / Euromemeian instead.

## Room state

- **Paused: OpenRouter is out of credits** (HTTP 402). Do not run the room until the author answers Desk **Eurobound-xnpg-wr1** ("Topped up: carry on").
- **Paused mid-round:** `WritingRoom/tasks/20261114_2059_wobbly_windmill_brewery_location_rewrite/` (bead Eurobound-xnpg).
  - Done: slices A (Kimi, location), B (Deepseek, Hendrik) and C (Mistral, PNG doc). Their drafts are in `drafts/`.
  - Still to do:
    1. Slice D: Aion writes the exterior signs, reading only Kimi's draft, into `drafts/aion_windmill_signs.md`. The slice spec is in `brief.md`.
    2. Kimi integrates in three passes.
    3. Run the stand-up test.
    4. Post the result to the Desk for the author.
    5. Splice it into the three design files, only after approval.
- The other task folders from 2026-11-14 are finished and applied.

## Open Desk cards (window eurobound-2b)

- **Eurobound-xnpg-wr1:** the OpenRouter top-up. Only the author can pay it.
- **Eurobound-c8xn-wr2:** the Monday 2026-11-16 story session, questions 1 and 3. The room asks one question per card and records the author's words verbatim. It never drafts or proposes story.

## Done in this task (Desk answers relayed by the Absinthe Orchestrator)

- **du51-wr1:** the battle HUD icon list is in the new file `design/ux/battle_hud_icon_pictures.md`. The GDD 309 border line now includes grey.
- **jt8q-wr1:** 16 Europe→Euromemeia swaps across 15 files, including the Arcade microcopy JSON and Tony420's "euro tour". The other Euro- names stay.
- **k3qa-wr2:** the older Space Cake landing block is deleted from `de_groene_gids.md`.
- **ms3r-wr2:** the closet prop looks are in the closet PNG doc. There is a new `broken_prize_tag_item.md` that prints "PRIZE: 1x DIGNITY — CLAIMED".
- **rpac-q5:** item looks batch 3 is in the five item docs. Two of those docs are new.
- The looks were sent to the Asset Development Team, which has queued them. That team also edited one line of `design/items/leopard_print_thong_item.md` (line 183, the icon size is now the 3D standard). Commit that edit with the file.
- **Beads:**
  - jt8q closed.
  - du51 unblocked, with its author-ruling label removed.
  - Comments added on ms3r, rpac and k3qa.
  - New bead **Eurobound-0161**: a validator warning on Europe/European (tools work, low effort).
- **Ledger:** "Writers' Room answers, part three" is staged in `docs/superpowers/NEXT_WORK.md`.
- The bead page is synced and acked, and the canon index is rebuilt. `tools/validate_data.py` runs OK.

## Uncommitted (this window's files; commit only when the author asks, through the Beads team or `commit_paths.py`)

```
Assets/Graphics/items/rhinestone-shirt-of-shame.md
WritingRoom/tasks/20261114_2015_space_cake_cue_lines_with_the_author/thread.md
WritingRoom/tasks/20261114_2029_battle_hud_icon_pictures/thread.md
WritingRoom/tasks/20261114_2047_closet_props_physical_descriptions/thread.md
WritingRoom/tasks/20261114_2051_item_physical_descriptions_batch_3_debau/thread.md
design/Synopsis.md
design/characters/LordPilsner/lordpilsner.md
design/game_design_document.md
design/items/leopard_print_thong_item.md
design/items/shark_fin_item.md
design/items/vip_wristband_item.md
design/items/debaucheryville_items/broken_prize_tag_item.md
design/items/debaucheryville_items/clock_snow_globe_item.md
design/items/debaucheryville_items/i_survived_tshirt_item.md
design/mechanics/Battle/party.md
design/narrative/Synopsis.md
design/quests/debaucheryville/couchsurfingchroniclesdebaucheryville.md
design/quests/general_quests/fratbronft.md
design/ux/battle_hud_icon_pictures.md
design/worlds/debaucheryville/PNG_Assets/Claw_Machine_Maintenance_Closet_Complete_PNG_Asset_Requirements.md
design/worlds/debaucheryville/location_nodes/tram_stop_17_location_nodes.json
design/worlds/debaucheryville/npcs/Cyberspace_Kavarna/npc_tony420.md
design/worlds/shamsterdam/cafe_de_schaamte.md
design/worlds/shamsterdam/de_groene_gids.md
design/worlds/shamsterdam/shamsterdam.md
design/worlds/shamsterdam/the_tolerance_hostel.md
design/worlds/sinfonia/PNG_Assets/the_black_tie_backroom_png_assets.md
docs/handoffs/2026-11-15_eurobound_2b.md
docs/superpowers/NEXT_WORK.md (ledger entry, staged)
game/assets/data/locations/debaucheryville/absinthe_arcade_microcopy.json
```

## Next steps and beads

1. When xnpg-wr1 comes back topped up, resume the Windmill rewrite (bead Eurobound-xnpg) with slice D, as described above.
2. Monday 2026-11-16 (c8xn-wr2): hold the story session with the author on questions 1 and 3.
3. Bead Eurobound-rpac is in progress. Next, more item-description batches from `design/items/docs/physical_descriptions_tracker.md` (172 JSON-only items still lack a look). One batch per Desk card.
4. Queued after that:
   - Eurobound-9mha (Starbaked).
   - The legacy `Assets/Graphics/items/` specs.
   - NPC conversations as data files, once the engine format arrives (Desk 04t2).

## Queued batch from the Production Desk Orchestrator (2026-11-16, waiting on credits)

One task, one room round, one batch. It is author-approved on the Desk. Start it only after the top-up. On 2026-11-16 OpenRouter had $0.24 of $40 left.
1. **Eurobound-40tc-q1:** extra Pilsner lines for DON'T NAP. The scene is `design/narrative/opening_step1.md` Scene 8. The slot is `LINES_DONT_NAP_PRETEND` in `game/worlds/publandia/bunk_and_blunder/opening_nap.gd:24`. The prompt stays where the scene puts it.
2. **Eurobound-x2ws-q4:** the save-slot picker's blank lines, `PENDING_LINES` and `LOCATION_NAMES` in `game/ui/save_slot_picker.gd:16-30`. Place names are canon parody names only.
3. **Eurobound-1n2u-q1:** the keychain State 12 description, plus new Chadwick/Bradley callbacks, in `design/items/bottle_opener_keychain_item.md`. Ruling: the brand-new keychain wins everywhere.
4. **Eurobound-lq6g-q1:** rewrite the lines in the six docs that still use the old Ultimate names. Bead lq6g lists the docs. The canon names are in `design/mechanics/Battle/battle_system.md:283-299`.

Rules:
- Use the satire-voice skill.
- The bros are doofuses. Name the audience in the brief.
- Post the drafts to the Desk one review at a time.
- When the batch is done, write a handoff and tell the author the window can be cleared.

**Added to the queued room batch (2026-11-17, Writing Room).** The author has already asked for drafted options on these beads (bead page answers), so after the top-up the room drafts them and posts each set to the Desk for the author to pick:
- **Eurobound-lei5:** a junk drop for the Voluntold Wrangler (`design/worlds/sinfonia/enemies/voluntold_wrangler.md:96`). Match the style of the other seven Golden Cutlet drops.
- **Eurobound-9tb7:** parody names for the non-European origins:
  - Istanbul and Turkey: `leemans_doner_palace.md:55`, `:203`
  - Morocco: `the_tolerance_hostel.md:209`
  - Australia: `de_botanische_leugen.md:237`
  - China: `astronomical_cockup.json:186`
- **Eurobound-ysi:** 3-4 parody demonyms to replace "Irish" in Publandia.
- **Eurobound-g40c:** 2-4 low-brow names to replace the per-city title "Cultural Ambassador". The title is at `couchsurfingchroniclesdebaucheryville.md:522` and `couchsurfingchroniclespublandia.md:640`. Author: "cultural ambassador sounds much too high brow. Rewrite".
