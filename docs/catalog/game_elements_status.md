> Generated 2026-11-14 16:00 UTC; do not edit by hand; run Tools/catalog/build_catalog.py.

# Game elements: where we are

One table per system. The wording comes from `Tools/catalog/game_elements.json` (seeded from `docs/research/2026-11-14-mechanics-gap-audit.md`); the file counts and bead statuses are checked on every build, so closing a bead or adding a test changes this page.

## Summary

| System | Elements | Complete | Partly built | Not built | Open beads |
|---|---|---|---|---|---|
| Battle | 10 | 1 | 5 | 4 | 14 |
| Levelling | 2 | 0 | 1 | 1 | 2 |
| Intoxication | 2 | 0 | 2 | 0 | 8 |
| Economy and shops | 6 | 2 | 3 | 1 | 12 |
| Inventory and equipment | 3 | 0 | 3 | 0 | 7 |
| Clock and rest | 2 | 1 | 1 | 0 | 2 |
| Navigation | 2 | 0 | 2 | 0 | 8 |
| Quests and flags | 2 | 0 | 2 | 0 | 10 |
| ICQ and dialogue | 2 | 0 | 2 | 0 | 6 |
| Couchsurfing | 1 | 0 | 0 | 1 | 4 |
| Brewery tour | 1 | 0 | 1 | 0 | 4 |
| Minigames | 1 | 0 | 1 | 0 | 5 |
| Save and load | 1 | 0 | 1 | 0 | 1 |
| Menus | 3 | 0 | 2 | 1 | 5 |
| Travel | 1 | 0 | 0 | 1 | 1 |
| Audio | 1 | 0 | 1 | 0 | 3 |
| Other | 1 | 0 | 0 | 1 | 1 |

## Battle

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Turns, damage, crits, rolling HP, Run | complete | Yes (2 of 2 files found). `mechanics/Battle/battle_system.md:2-50`; numbers approved in `battle_numbers_proposal.md:1-37` | Yes | Yes (3 of 3 files found). `battle/battle_core.gd`, `battle_rules.gd`, `battle_unit.gd` | Yes (3 of 3 files found). `test_battle_core`, `test_battle_rules`, `test_attack_conversion` | `party/party_members.json` (3 bros) (1 of 1 files found) | Nothing for the Arcade. Turn order following a venue's beat (`battle_system.md:5`) is not built | wuyu (open) |
| Bravado (bar, Low/Mid/High, Flex) | partly built | Yes (2 of 2 files found). `mechanics/Battle/bravado.md`; `battle_numbers_proposal.md:28-33` | Yes | Yes (2 of 2 files found). `battle/battle_rules.gd:40-73`, `core/game_state.gd:26` | Yes (1 of 1 files found). `test_bravado_state` | In party data | The world reacting to Bravado level (`bravado.md:103`) is not built and has no numbers | none |
| Abilities and Ultimates | partly built | Yes (1 of 1 files found). `battle_system.md:214-304`; `templates/ability_template.md` | No. Open: Yes: only Roast Line has numbers (`battle_numbers_proposal.md:37`) | Yes (1 of 1 files found). `battle_core.gd:300` runs a skill | Yes (1 of 1 files found). `test_battle_core` | `skills/party_abilities.json`: 1 ability (1 of 1 files found) | Chadwick and Bradley can only Attack. No Ultimate exists in data | g0jr (open), uwrw (blocked) |
| Combos | not built | See note. `battle_system.md:15-33`, `:52-205`, `:306-440` | No. Open: Yes: no numbers, never approved | No. None | No. None | None | Everything | rl4c (open) |
| Taunt and counter-brags | not built | See note. `battle_system.md:7-13` | No. Open: Yes: no numbers | No. None (Item and Flex only) | No. None | None | Everything | wuyu (open) |
| Status effects | partly built | Yes (2 of 2 files found). `mechanics/Battle/status_effects.md` (master list); data shape approved in `docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md` | No. Open: Yes: 8 behaviour questions (64vo); master-list numbers never approved | Yes (3 of 3 files found). `battle/status_table.gd`, `core/field_status.gd`, `core/rest_events.gd` | Yes (4 of 4 files found). `test_status_table`, `test_field_status`, `test_space_cake`, `test_compulsion` | `skills/status_effects.json`: 12 statuses, all recent (1 of 1 files found) | The original list (Hungover, Grease Fingers, Embarrassed, Thirsty, Inspired and the rest) has no data entries | vdrt (open), 64vo (closed), jsd0 (open), picf (blocked), 0zt0 (blocked), izct (open), rry7 (open), 2uji (closed), qiof (closed) |
| Enemy behaviour | partly built | Yes (2 of 2 files found). `templates/villain_template.md`; `mechanics/Battle/enemyai.md` is a placeholder | Yes | Yes (1 of 1 files found). `battle_core.gd` (weighted moves, telegraphs) | Yes (3 of 3 files found). `test_battle_core`, `test_arcade_battle`, `test_taproom_battle` | `enemies/debaucheryville_arcade_battle.json` (13 villains) (1 of 1 files found) | Fine for Arcade villains. Street enemies have no data | skjd (open), 26v (blocked) |
| City boss (Count Velvet Absinthe) | not built | Yes (2 of 2 files found). `game_design_document.md:131-134` only; `mechanics/Battle/bossmechanics.md` is a placeholder | No. Open: Yes: no villain doc | No. None | No. None | None | Everything | nu0k (open) |
| Battle screen | partly built | Yes (1 of 1 files found). `game_design_document.md:301-320` (turn-order strip, peek, status icons; controls ruled round v35) | Yes | Yes (1 of 1 files found). `battle/battle_screen.gd` (menu, log, HP) | Yes (1 of 1 files found). `test_battle_screen` | n/a | Turn-order strip, hold-to-peek, status icons | ibgl (blocked) |
| Street encounters (visible enemies, ambush, auto-win) | not built | Yes (1 of 1 files found). `game_design_document.md:16`, `:292` only. No design doc | No. Open: Yes: undesigned | No. None | No. None | None | Everything, plus what happens when the bros lose outside the Arcade | skjd (open) |

## Levelling

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| XP and levels | partly built | Yes (2 of 2 files found). `mechanics/Progression/leveling.md` and `xpgain.md` are placeholders | No. Open: Yes: never ruled. Ledger :572 says "until levels exist" | Yes (1 of 1 files found). `core/game_state.gd:56-57`, `:115` store XP; nothing spends it | Yes (1 of 1 files found). `test_game_state` | Enemies carry XP values | A levelling rule and its numbers | 5aie (open), 028k (open) |
| Clout ladder and skill trees | not built | Yes (1 of 1 files found). `mechanics/Progression/skilltrees_cloutspells.md` (171 lines) | No. Open: Yes: never approved; clashes with XP | No. None | No. None | None | A ruling on XP versus Clout, then everything | 028k (open) |

## Intoxication

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Intoxication tiers (Buzzed, Beer Goggles, Shitfaced, Catastrophe) | partly built | Yes (1 of 1 files found). `mechanics/intoxication_law.md:143-177`. Names ruled; thresholds "not yet approved" (:145) | No. Open: Yes: numbers, and the 10-point review | Yes (2 of 2 files found). `core/intoxicant.gd` reads drink and drug fields. No tier logic. The menu card can show a tier (`ui/field_menu.gd:395`) but nothing sets one | Yes (1 of 1 files found). `test_intoxicant` | `items/consumables.json` (11 items) (1 of 1 files found) | The tier system itself | p0j (deferred), f3tq (open), tcip (open) |
| Hangovers | partly built | Yes (1 of 1 files found). Legendary Hangover proposals in `docs/superpowers/specs/2026-11-14-legendary-hangover-unit-and-rescale-proposal.md` | No. Open: Yes | Yes (1 of 1 files found). Rest cures in `core/rest_events.gd` | Yes (1 of 1 files found). `test_game_clock` | Partial | Numbers and the cure | picf (blocked), 81un (open), 1dr (blocked), 3mqo (blocked), 90vn (blocked) |

## Economy and shops

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| SOVS wallet | complete | Yes (2 of 2 files found). `economy/currency.md`; `economy/economy_system.md:21-86` | Yes | Yes (1 of 1 files found). `core/game_state.gd:130-150` | Yes (1 of 1 files found). `test_sovs_wallet` | n/a | Nothing | none |
| SOVS shops | partly built | Yes (3 of 3 files found). `economy/economy_system.md:87-99`; `economy/shoptypes.md` and `itemvalue.md` are placeholders | No. Open: Yes: the first shop waits on your approval (`docs/superpowers/specs/2026-11-14-first-sovs-shop-proposal.md:5`) | Yes (2 of 2 files found). `core/shop_catalog.gd`, `ui/sovs_shop.gd` | Yes (1 of 1 files found). `test_sovs_shop` | `world_data/Shops.json`: 0 shops (1 of 1 files found) | A real shop, its stock, opening hours, and a place to stand in front of it | it49 (deferred), j45c (deferred), zf6e (deferred), rouz (blocked), nm8y (open) |
| Arcade tokens and prize counter | complete | See note. Ledger rulings (Arcade, 2026-11-09) | Yes | Yes (1 of 1 files found). `worlds/debaucheryville/absinthe_arcade/prize_shop.gd` | Yes (1 of 1 files found). `test_prize_shop` | `enemies/debaucheryville_arcade_battle.json` (1 of 1 files found) | Nothing | none |
| Shitcoins, kiosks, rug pulls | partly built | Yes (2 of 2 files found). `economy/economy_system.md:100-244`; `economy/shitcoin_master_pool.md` | Partly. Open: Three small ones (`economy_system.md:306`) | Yes (1 of 1 files found). Coin storage only (`core/game_state.gd:178-215`) | Yes (1 of 1 files found). `test_coin_store` | None | Kiosks, the 35/65 roll, back-alley vendors | 22n3 (open), ml5r (open), wgso (open) |
| ICQ airdrops | not built | Yes (1 of 1 files found). `economy/icq_airdrops.md:22-330` | Partly. Open: One (`:330`) | No. None | No. None | None | Everything | li0t (open) |
| NFTs and the Legacy Vault | partly built | Yes (3 of 3 files found). `economy/legacy_vault_cards.md`; `economy/wallet_ui.md:43-151`; `templates/NFT_Template.md` | Yes | Yes (2 of 2 files found). `core/nft_vault.gd`; listed in the menu (`ui/field_menu.gd:519`) | Yes (1 of 1 files found). `test_nft_vault` | `nft/legacy_vault.json` (17 cards) (1 of 1 files found) | The proper wallet tab with card frames and first-open message; the hidden Bagholder tab | fxon (open), 22n3 (open), yf2j (blocked), q9bw (open) |

## Inventory and equipment

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Inventory and using items | partly built | Yes (2 of 2 files found). `templates/consumable_item_template.md`, `permanent_item_template.md` | Yes | Yes (2 of 2 files found). `core/game_state.gd:73-108`; `ui/field_menu.gd:173-210` | Yes (3 of 3 files found). `test_game_state`, `test_field_menu`, `test_key_items_loader` | `items/consumables.json` (11), `items/key_items.json` (37) (2 of 2 files found) | Many designed items are not in the data yet | 0vsu (open), 028j (closed), jlzw (open), kuws (blocked), e896 (blocked) |
| Equipment | partly built | Yes (1 of 1 files found). `templates/equipment_template.md`; slots ruled (ledger :702-705) | No. Open: Yes: the data format (70z) | Yes (1 of 1 files found). Menu lists slot names only (`ui/field_menu.gd:500`) | No. None | `items/equipment.json`: 0 items (1 of 1 files found) | Equipping, stat bonuses, combo sets | t1gn (open), 70z (deferred) |
| Junk items that pay off when inspected | partly built | Yes (1 of 1 files found). `.claude/CLAUDE.md` (author, 2026-11-11) | Yes | See note. Arcade microcopy (`absinthe_arcade/arcade_microcopy.gd`) | Yes (1 of 1 files found). `test_arcade_microcopy` | `locations/debaucheryville/absinthe_arcade_microcopy.json` (1 of 1 files found) | Only the Arcade has it | o9f (blocked) |

## Clock and rest

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Game clock, day and night | complete | Yes (1 of 1 files found). Ledger :666-685, :713 (rounds v34-v37). `mechanics/Systems/daynightcycle.md` is a placeholder | Yes | Yes (1 of 1 files found). `core/game_clock.gd` | Yes (1 of 1 files found). `test_game_clock` | n/a | Nothing. The design doc should be filled from the ledger | ps9 (deferred), kh9g (closed) |
| Rest | partly built | See note. Ledger :670 ("Morning is the next rest") | No. Open: Yes: no list of where the bros can rest, what it costs or what it restores | Yes (2 of 2 files found). `core/game_clock.gd:64`, `core/rest_events.gd`. Nothing calls them | Yes (1 of 1 files found). `test_game_clock` | n/a | A bed, or any rest point | 8snp (open) |

## Navigation

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Walking and moving between screens | partly built | Yes (1 of 1 files found). Vertical-slice spec (`docs/superpowers/specs/2026-07-30-vertical-slice-design.md:32-44`) | Yes | Yes (2 of 2 files found). `characters/player/player_controller.gd`, `core/scene_router.gd` (9 Arcade screens) | Yes (2 of 2 files found). `test_player_controller`, `test_scene_router` | `world_data/Maps.json`: empty (1 of 1 files found) | Every Debaucheryville location except the Arcade | 467 (in_progress), eaiq (open), nm8y (open), 4nn3 (closed) |
| Shamsterdam tunnel navigation | partly built | Yes (1 of 1 files found). `worlds/shamsterdam/voetgangerstunnel.md`; odds approved (ledger :848) | Partly. Open: Small ones | Yes (1 of 1 files found). `core/navigation_roll.gd` | Yes (1 of 1 files found). `test_navigation_roll`, `_grants`, `_teleport` | `navigation/voetgangerstunnel.json` (1 of 1 files found) | The tunnel itself; several rewards | 39yk (blocked), 1esc (blocked), k3qa (blocked), sj0s (open), lofj (blocked), iakb (closed) |

## Quests and flags

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Flags (the game's memory) | partly built | Yes (2 of 2 files found). Approved shapes: `docs/superpowers/specs/2026-11-12-quest-flag-schema-proposal.md`, `2026-11-12-flag-write-shape-proposal.md` | Yes | Yes (1 of 1 files found). `core/game_state.gd:109-113` | Yes (1 of 1 files found). `test_game_state` | `world_data/quest_flags.json` (104 flags) (1 of 1 files found) | Old data still writes flags the old way | ojwi (blocked), 5p5z (closed), grng (open), wqui (open) |
| Quests and the Quest Log | partly built | Yes (2 of 2 files found). `templates/sidequest_template.md`; 12 quest docs in `quests/debaucheryville/` | Partly. Open: Per quest | Yes (1 of 1 files found). `core/quest_log.gd`. Each working quest is hand-coded (`absinthe_arcade/grandpa_provides.gd`) | Yes (2 of 2 files found). `test_quest_log`, `test_grandpa_provides` | `quest_log/quest_log.json`: 1 quest. Two files in `quests/` that nothing reads (2 of 2 files found) | Rewards on completion; reading quests from data; most quests | ou0t (open), zkhb (blocked), dah (blocked), apz (deferred), nda (open), b8rb (blocked), e4bh (blocked) |

## ICQ and dialogue

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Dialogue | partly built | Yes (2 of 2 files found). `narrative/dialoguesystem.md` and `mechanics/Social/dialoguetrees.md` are placeholders | Yes | Yes (1 of 1 files found). Three separate ways: the Dialogue Manager add-on, `absinthe_arcade/dialogue_box.gd`, and tree data nothing reads (`core/data_repo.gd:38`) | Yes (2 of 2 files found). `test_dialogue_box`, `test_hall_npc` | `npcs/dialogue_trees/debaucheryville_dialogue.json` (3 trees, unused) (1 of 1 files found) | One agreed way to show NPC talk | 04t2 (blocked), izct (open) |
| FREE Wi-Fi and ICQ | partly built | Yes (2 of 2 files found). `worlds/shared/interactables/wifihotspots.md:1-3`; `game_design_document.md:211-230`, `:254-258` | Partly. Open: Placement; the other sting quests (1im) | Yes (1 of 1 files found). `worlds/shared/icq/` (queue, window, hotspot, Tony420 hijack). Not placed in any scene | Yes (3 of 3 files found). `test_icq_queue`, `test_wifi_hotspot`, `test_tony420_hijack` | `world_data/events/icqdialogues/` (3 messages plus the hijack) (1 of 1 files found) | A hotspot the bros can walk up to; Mom and Bestie chats; the once-per-hotspot top-up (`game_design_document.md:257`) | ign (blocked), uya (blocked), rcm (blocked), li0t (open) |

## Couchsurfing

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Couchsurfing Chronicles | not built | Yes (2 of 2 files found). `quests/general_quests/couchsurfingchronicles.md:61` (the four states); `templates/couchsurf_host_template.md` | Partly. Open: Small (g40c) | No. None | No. None | One out-of-date file | Everything | j1h6 (open), w7nx (open), zqqy (blocked), g40c (open) |

## Brewery tour

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Brewery tour and passport | partly built | Yes (1 of 1 files found). `quests/general_quests/brewerytour.md:1-50`; ledger :122 | Partly. Open: Small (91iz, nea6) | Yes (2 of 2 files found). `core/brewery_passport.gd`, `core/vanek_taproom.gd` | Yes (3 of 3 files found). `test_brewery_passport`, `test_bar_discount`, `test_vanek_taproom` | `brewery_tour/breweries.json` (16 breweries) (1 of 1 files found) | Only the Arcade's Taproom brewery is playable; selfie scrapbook | 4ti (blocked), 4med (open), akw (open), nea6 (closed), 91iz (open) |

## Minigames

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Arcade minigames (claw, DDR, skee-ball, foosball, mirror puzzle, Taproom maze) | partly built | Yes (1 of 1 files found). Ledger :380-417 and later Arcade rounds; `mechanics/Social/minigames.md` (9 lines, other cities) | Partly. Open: North wing contents (u5i) | Yes (3 of 3 files found). `worlds/debaucheryville/absinthe_arcade/` (claw, `ddr/`, `rec/`, mirror puzzle), `core/taproom_maze.gd` | Yes (6 of 6 files found). `test_arcade_claw`, `test_claw_screen`, `test_ddr`, `test_rec_games`, `test_arcade_mirror_shadow_puzzle`, `test_taproom_maze` | `taproom_maze/sections.json` (1 of 1 files found) | DDR songs and wiring into the hall; art states | cht (deferred), u5i (open), lyvh (open), sjoc (open), w2ig (open) |

## Save and load

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Save and load | partly built | Yes (1 of 1 files found). Ledger :700: "saving happens at hotspots and beds, plus autosave". `mechanics/Systems/save_load.md` is a placeholder | Partly. Open: Small: when autosave fires | Yes (2 of 2 files found). `core/save_system.gd` works, but nothing ever saves. Load is in the menu (`ui/field_menu.gd:331`) | Yes (1 of 1 files found). `test_save_system` | n/a | The game cannot be saved today | x2ws (blocked) |

## Menus

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Title screen | not built | See note. Vertical-slice spec :11, :34 | Yes | No (1 of 1 files found). None. The game opens on the Arcade street (`project.godot:14`) | No. None | n/a | New Game, Continue, Quit | 9jzp (open), 9z3u (open) |
| Field menu (9 sections) | partly built | See note. Ledger :699-707 (round v36) | Yes | Yes (1 of 1 files found). `ui/field_menu.gd` | Yes (1 of 1 files found). `test_field_menu` | n/a | Equip and Settings are display-only | t1gn (open), j0zo (open), z3ec (open) |
| Settings and accessibility | partly built | Yes (2 of 2 files found). `ux/UX & Accessibility Guide.md:10-22`; `game_design_document.md:258`, `:313`, `:320`, `:350`; `ux/accessibility.md` is a placeholder | No. Open: Yes: nothing ruled | Yes (1 of 1 files found). `ui/field_menu.gd:550` shows text; reduced motion exists for Arcade effects | Yes (1 of 1 files found). `test_arcade_ambient_fx` | n/a | A Settings screen that changes anything | j0zo (open) |

## Travel

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Travel between cities | not built | Yes (2 of 2 files found). `game_design_document.md:10` ("Next city"); `economy/economy_system.md:25` (train and ferry tickets). No design doc | No. Open: Yes: undesigned | No. None | No. None | None | Everything. Does not block a one-city slice | ya5e (open) |

## Audio

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Sound and music | partly built | Yes (2 of 2 files found). `audio/musicalbeats.md`; `game_design_document.md:344`. No system doc | Partly. Open: Content is yours | See note. Three scripts each play one sound. No shared player, no music | No. None | 3 sound files | An audio system; all music | pqe9 (in_progress), yf2j (blocked), k3qa (blocked) |

## Other

| Element | Status | Designed | Ruled | Built | Tested | Data | What's left | Bead ids |
|---|---|---|---|---|---|---|---|---|
| Reputation and Street Rep | not built | Yes (2 of 2 files found). `mechanics/Social/socialmechanicsandreputationsystem.md` (251 lines); `game_design_document.md:261` | No. Open: Yes: never approved. Only ruling: not shown in the menu (ledger :707) | No. None | No. None | None | A yes, no or later from you | trl3 (open) |
