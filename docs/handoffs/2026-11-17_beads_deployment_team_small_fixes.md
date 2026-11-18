# Handoff: Beads Deployment Team, small fixes 7nbx / b10l / b8yo / wqui / dyez (2026-11-17)

**Window name: Beads Deployment Team.** The Production Desk Orchestrator assigned one task: item 6 of the ready-queue ranking, five small fixes whose author answers were already in. **Done. This window can be cleared.** Nothing is running. Godot and GUT were not run.

## Per bead

| Bead | Result | What changed |
|---|---|---|
| Eurobound-7nbx | **Closed** | `design/quests/shamsterdam/great_doner_debate_shamsterdam.md`: line 15 now gives the trigger as the author's words (7nbx-q1, "It starts once the base quest has a winner and the bros reach Shamsterdam"). Three headings changed from EXPANSION to SHAMSTERDAM (:7, :92, :393). The ruling note at :9 is updated to say the trigger was re-ruled. Every other line is unchanged. The ledger already held the ruling (`NEXT_WORK.md:910`). |
| Eurobound-b10l | **Closed** | The "Meta References" bullet is deleted from `vlad_the_validator.md` and `crypto_clown.md` (both were at :139), as b10l-q1 said ("Strike both lines"). |
| Eurobound-dyez | **Closed** | Every player-facing exit name was already a parody: "Terminal Chaos" and "Museum Mile" in `game/assets/data/navigation/voetgangerstunnel.json`, the `sign_says` field and `voetgangerstunnel.md` N1. The last design-text leftover, `voetgangerstunnel.md:146`, changed from "Centraal" to "Terminal Chaos". The internal ids (`centraal_station`, `museum_plein`, `NavigationRoll.SIGN_CENTRAAL` and the tests that use it) are never shown to the player and are left alone, because renaming them needs code and test changes plus a GUT run. No new name was needed, so there's no Desk card. |
| Eurobound-b8yo | **Open (partial)** | The "Shadow Exchange Dealer" Related Characters line is removed from `crypto_clown.md` (was :148). **Skipped:** `game/assets/data/npcs/base_profiles/debaucheryville_core.json`, because it has another window's uncommitted edits (the Vlad door ids for 9tz9). The `shadow_exchange_dealer` entry and its sprite entries (`npcs/sprite_mappings/debaucheryville_sprites.json:176, :356`) wait for that file to be committed. His old dialogue (`dialogue_trees/debaucheryville_dialogue.json:276-350`, `easter_eggs.json:56`) belongs to Eurobound-rras and Eurobound-04t2 and was not touched. |
| Eurobound-wqui | **Open (skipped)** | `game/assets/data/world_data/quest_flags.json` has another window's uncommitted edits (`settings.prompt_style`, `nav_tunnel_visit_rolled`, the Marloes `set_by` line). **Mistake, corrected:** I first checked the wrong path (`game/assets/data/quests/`), added the declaration while keeping their edits, then saw their diff. I took my entry back out and restored `cloverleaf_environment.json`. Both files now hold exactly what they held before. The exact change to apply later is in the bead comment: `publandia.cloverleaf.path_b_chosen`, keeping the existing event name, plus the declaration. validate_data was 0 FAIL with the entry in. |

## Checks

- `python -I Tools/validate_data.py` was run once, with the wqui entry briefly in: 0 FAIL. That file then went back to the other window's version.
- The canon index was rebuilt.
- The bead page was synced once.
- Nothing was committed.

## Uncommitted (this task)

- `design/quests/shamsterdam/great_doner_debate_shamsterdam.md`. The file is untracked: Eurobound-0xz created it today, and my edits sit on top.
- `design/worlds/debaucheryville/npcs/Velvet_Curtain_Club/vlad_the_validator.md`
- `design/worlds/debaucheryville/npcs/Cirque_du_Shady/crypto_clown.md`
- `design/worlds/shamsterdam/voetgangerstunnel.md`
- This handoff.

## Next

- **b8yo:** finish it once `debaucheryville_core.json` is committed.
- **wqui:** finish it once `quest_flags.json` is committed.

Both comments say exactly what to change.
