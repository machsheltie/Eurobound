# Mechanics gap audit: what still needs development

- **Date:** 2026-11-14
- **Bead:** Eurobound-alcj
- **Request (author, verbatim):** "heavily look into our game mechanics and figure what still needs development."
- **Written for:** the author. No programming knowledge needed.

## The short version

The game today is the Absinthe Arcade and nothing around it. Inside the Arcade a lot works: walking, fights, the claw, DDR, skee-ball, foosball, the Taproom maze, the menu, the SOVS wallet, the clock and the Brewery Passport. The rules underneath are well tested (770 automated checks in 62 files).

What's missing falls into three groups:

1. **Built but not plugged in.** Saving, resting, the SOVS shop screen, the FREE Wi-Fi hotspot and the ICQ window all exist as working parts that no screen uses yet. The game cannot currently be saved.
2. **Designed but waiting on your numbers or your yes.** Combos, Taunt, Chadwick's and Bradley's moves, the Clout ladder, the original status list, the intoxication tiers, reputation.
3. **Mentioned but never designed.** Street encounters, travel between cities, the city boss, losing a fight outside the Arcade, where the bros sleep.

I filed 19 new beads. Eleven need a decision from you; each one has tap-to-answer options on the bead page, and every option is a route (who drafts it, or when), never an invented answer.

## How I checked

- **Design:** I read the game design document, everything in `design/mechanics/`, `design/economy/`, `design/quests/general_quests/`, `design/templates/` and the approved specs in `docs/superpowers/specs/`.
- **Rulings:** I searched the ledger (`docs/superpowers/NEXT_WORK.md`) and the 170 beads that were open, blocked, deferred or in progress this morning.
- **Code, tests, data:** I searched `game/` by file and by keyword. I did not run the game or the tests, so "built" means the code exists and has tests, not that I watched it work.

In the table, design paths start at `design/`, code paths at `game/`, test names are files in `game/tests/unit/`, and data paths start at `game/assets/data/`. "Ledger" is `docs/superpowers/NEXT_WORK.md`. Bead ids drop the `Eurobound-` prefix. **Bold ids are new beads from this audit.**

## The table

### Battle

| Mechanic | Design | Rulings open | Code | Tests | Data | What's missing | Beads |
|---|---|---|---|---|---|---|---|
| Turns, damage, crits, rolling HP, Run | `mechanics/Battle/battle_system.md:2-50`; numbers approved in `battle_numbers_proposal.md:1-37` | None | `battle/battle_core.gd`, `battle_rules.gd`, `battle_unit.gd` | `test_battle_core`, `test_battle_rules`, `test_attack_conversion` | `party/party_members.json` (3 bros) | Nothing for the Arcade. Turn order following a venue's beat (`battle_system.md:5`) is not built | **wuyu** |
| Bravado (bar, Low/Mid/High, Flex) | `mechanics/Battle/bravado.md`; `battle_numbers_proposal.md:28-33` | None | `battle/battle_rules.gd:40-73`, `core/game_state.gd:26` | `test_bravado_state` | In party data | The world reacting to Bravado level (`bravado.md:103`) is not built and has no numbers | none |
| Abilities and Ultimates | `battle_system.md:214-304`; `templates/ability_template.md` | Yes: only Roast Line has numbers (`battle_numbers_proposal.md:37`) | `battle_core.gd:300` runs a skill | `test_battle_core` | `skills/party_abilities.json`: 1 ability | Chadwick and Bradley can only Attack. No Ultimate exists in data | **g0jr**, uwrw |
| Combos | `battle_system.md:15-33`, `:52-205`, `:306-440` | Yes: no numbers, never approved | None | None | None | Everything | **rl4c** |
| Taunt and counter-brags | `battle_system.md:7-13` | Yes: no numbers | None (Item and Flex only) | None | None | Everything | **wuyu** |
| Status effects | `mechanics/Battle/status_effects.md` (master list); data shape approved in `docs/superpowers/specs/2026-11-12-status-effect-data-shape-proposal.md` | Yes: 8 behaviour questions (64vo); master-list numbers never approved | `battle/status_table.gd`, `core/field_status.gd`, `core/rest_events.gd` | `test_status_table`, `test_field_status`, `test_space_cake`, `test_compulsion` | `skills/status_effects.json`: 12 statuses, all recent | The original list (Hungover, Grease Fingers, Embarrassed, Thirsty, Inspired and the rest) has no data entries | **vdrt**, 64vo, jsd0, picf, 0zt0, izct, rry7, 2uji, qiof |
| Enemy behaviour | `templates/villain_template.md`; `mechanics/Battle/enemyai.md` is a placeholder | None for the Arcade | `battle_core.gd` (weighted moves, telegraphs) | `test_battle_core`, `test_arcade_battle`, `test_taproom_battle` | `enemies/debaucheryville_arcade_battle.json` (13 villains) | Fine for Arcade villains. Street enemies have no data | **skjd**, 26v |
| City boss (Count Velvet Absinthe) | `game_design_document.md:131-134` only; `mechanics/Battle/bossmechanics.md` is a placeholder | Yes: no villain doc | None | None | None | Everything | **nu0k** |
| Battle screen | `game_design_document.md:301-320` (turn-order strip, peek, status icons; controls ruled round v35) | None | `battle/battle_screen.gd` (menu, log, HP) | `test_battle_screen` | n/a | Turn-order strip, hold-to-peek, status icons | **ibgl** |
| Street encounters (visible enemies, ambush, auto-win) | `game_design_document.md:16`, `:292` only. No design doc | Yes: undesigned | None | None | None | Everything, plus what happens when the bros lose outside the Arcade | **skjd** |

### Growing stronger

| Mechanic | Design | Rulings open | Code | Tests | Data | What's missing | Beads |
|---|---|---|---|---|---|---|---|
| XP and levels | `mechanics/Progression/leveling.md` and `xpgain.md` are placeholders | Yes: never ruled. Ledger :572 says "until levels exist" | `core/game_state.gd:56-57`, `:115` store XP; nothing spends it | `test_game_state` | Enemies carry XP values | A levelling rule and its numbers | 5aie, **028k** |
| Clout ladder and skill trees | `mechanics/Progression/skilltrees_cloutspells.md` (171 lines) | Yes: never approved; clashes with XP | None | None | None | A ruling on XP versus Clout, then everything | **028k** |
| Intoxication tiers (Buzzed, Beer Goggles, Shitfaced, Catastrophe) | `mechanics/intoxication_law.md:143-177`. Names ruled; thresholds "not yet approved" (:145) | Yes: numbers, and the 10-point review | `core/intoxicant.gd` reads drink and drug fields. No tier logic. The menu card can show a tier (`ui/field_menu.gd:395`) but nothing sets one | `test_intoxicant` | `items/consumables.json` (11 items) | The tier system itself | p0j, f3tq, tcip |
| Hangovers | Legendary Hangover proposals in `docs/superpowers/specs/2026-11-14-legendary-hangover-unit-and-rescale-proposal.md` | Yes | Rest cures in `core/rest_events.gd` | `test_game_clock` | Partial | Numbers and the cure | picf, 81un, 1dr, 3mqo, 90vn |

### Money and things

| Mechanic | Design | Rulings open | Code | Tests | Data | What's missing | Beads |
|---|---|---|---|---|---|---|---|
| SOVS wallet | `economy/currency.md`; `economy/economy_system.md:21-86` | None | `core/game_state.gd:130-150` | `test_sovs_wallet` | n/a | Nothing | none |
| SOVS shops | `economy/economy_system.md:87-99`; `economy/shoptypes.md` and `itemvalue.md` are placeholders | Yes: the first shop waits on your approval (`docs/superpowers/specs/2026-11-14-first-sovs-shop-proposal.md:5`) | `core/shop_catalog.gd`, `ui/sovs_shop.gd` | `test_sovs_shop` | `world_data/Shops.json`: 0 shops | A real shop, its stock, opening hours, and a place to stand in front of it | it49, j45c, zf6e, rouz, nm8y |
| Arcade tokens and prize counter | Ledger rulings (Arcade, 2026-11-09) | None | `worlds/debaucheryville/absinthe_arcade/prize_shop.gd` | `test_prize_shop` | `enemies/debaucheryville_arcade_battle.json` | Nothing | none |
| Shitcoins, kiosks, rug pulls | `economy/economy_system.md:100-244`; `economy/shitcoin_master_pool.md` | Three small ones (`economy_system.md:306`) | Coin storage only (`core/game_state.gd:178-215`) | `test_coin_store` | None | Kiosks, the 35/65 roll, back-alley vendors | 22n3, ml5r, wgso |
| ICQ airdrops | `economy/icq_airdrops.md:22-330` | One (`:330`) | None | None | None | Everything | li0t |
| NFTs and the Legacy Vault | `economy/legacy_vault_cards.md`; `economy/wallet_ui.md:43-151`; `templates/NFT_Template.md` | None | `core/nft_vault.gd`; listed in the menu (`ui/field_menu.gd:519`) | `test_nft_vault` | `nft/legacy_vault.json` (17 cards) | The proper wallet tab with card frames and first-open message; the hidden Bagholder tab | fxon, 22n3, yf2j, q9bw |
| Inventory and using items | `templates/consumable_item_template.md`, `permanent_item_template.md` | None | `core/game_state.gd:73-108`; `ui/field_menu.gd:173-210` | `test_game_state`, `test_field_menu`, `test_key_items_loader` | `items/consumables.json` (11), `items/key_items.json` (37) | Many designed items are not in the data yet | 0vsu, 028j, jlzw, kuws, e896 |
| Equipment | `templates/equipment_template.md`; slots ruled (ledger :702-705) | Yes: the data format (70z) | Menu lists slot names only (`ui/field_menu.gd:500`) | None | `items/equipment.json`: 0 items | Equipping, stat bonuses, combo sets | **t1gn**, 70z |
| Junk items that pay off when inspected | `.claude/CLAUDE.md` (author, 2026-11-11) | None | Arcade microcopy (`absinthe_arcade/arcade_microcopy.gd`) | `test_arcade_microcopy` | `locations/debaucheryville/absinthe_arcade_microcopy.json` | Only the Arcade has it | o9f |

### Time, movement and the world

| Mechanic | Design | Rulings open | Code | Tests | Data | What's missing | Beads |
|---|---|---|---|---|---|---|---|
| Game clock, day and night | Ledger :666-685, :713 (rounds v34-v37). `mechanics/Systems/daynightcycle.md` is a placeholder | None | `core/game_clock.gd` | `test_game_clock` | n/a | Nothing. The design doc should be filled from the ledger | ps9, kh9g |
| Rest | Ledger :670 ("Morning is the next rest") | Yes: no list of where the bros can rest, what it costs or what it restores | `core/game_clock.gd:64`, `core/rest_events.gd`. Nothing calls them | `test_game_clock` | n/a | A bed, or any rest point | **8snp** |
| Walking and moving between screens | Vertical-slice spec (`docs/superpowers/specs/2026-07-30-vertical-slice-design.md:32-44`) | None | `characters/player/player_controller.gd`, `core/scene_router.gd` (9 Arcade screens) | `test_player_controller`, `test_scene_router` | `world_data/Maps.json`: empty | Every Debaucheryville location except the Arcade | 467, eaiq, nm8y, 4nn3 |
| Shamsterdam tunnel navigation | `worlds/shamsterdam/voetgangerstunnel.md`; odds approved (ledger :848) | Small ones | `core/navigation_roll.gd` | `test_navigation_roll`, `_grants`, `_teleport` | `navigation/voetgangerstunnel.json` | The tunnel itself; several rewards | 39yk, 1esc, k3qa, sj0s, lofj, iakb |
| Travel between cities | `game_design_document.md:10` ("Next city"); `economy/economy_system.md:25` (train and ferry tickets). No design doc | Yes: undesigned | None | None | None | Everything. Does not block a one-city slice | **ya5e** |
| Save and load | Ledger :700: "saving happens at hotspots and beds, plus autosave". `mechanics/Systems/save_load.md` is a placeholder | Small: when autosave fires | `core/save_system.gd` works, but nothing ever saves. Load is in the menu (`ui/field_menu.gd:331`) | `test_save_system` | n/a | **The game cannot be saved today** | **x2ws** |
| Title screen | Vertical-slice spec :11, :34 | None | None. The game opens on the Arcade street (`project.godot:14`) | None | n/a | New Game, Continue, Quit | **9jzp**, 9z3u (art) |

### Quests, talking and the phone

| Mechanic | Design | Rulings open | Code | Tests | Data | What's missing | Beads |
|---|---|---|---|---|---|---|---|
| Flags (the game's memory) | Approved shapes: `docs/superpowers/specs/2026-11-12-quest-flag-schema-proposal.md`, `2026-11-12-flag-write-shape-proposal.md` | None | `core/game_state.gd:109-113` | `test_game_state` | `world_data/quest_flags.json` (104 flags) | Old data still writes flags the old way | ojwi, 5p5z, grng, wqui |
| Quests and the Quest Log | `templates/sidequest_template.md`; 12 quest docs in `quests/debaucheryville/` | Per quest | `core/quest_log.gd`. Each working quest is hand-coded (`absinthe_arcade/grandpa_provides.gd`) | `test_quest_log`, `test_grandpa_provides` | `quest_log/quest_log.json`: 1 quest. Two files in `quests/` that nothing reads | Rewards on completion; reading quests from data; most quests | ou0t, **zkhb**, dah, apz, nda, b8rb, e4bh |
| Dialogue | `narrative/dialoguesystem.md` and `mechanics/Social/dialoguetrees.md` are placeholders | None (it's a technical choice) | Three separate ways: the Dialogue Manager add-on, `absinthe_arcade/dialogue_box.gd`, and tree data nothing reads (`core/data_repo.gd:38`) | `test_dialogue_box`, `test_hall_npc` | `npcs/dialogue_trees/debaucheryville_dialogue.json` (3 trees, unused) | One agreed way to show NPC talk | **04t2**, izct |
| FREE Wi-Fi and ICQ | `worlds/shared/interactables/wifihotspots.md:1-3`; `game_design_document.md:211-230`, `:254-258` | Placement; the other sting quests (1im) | `worlds/shared/icq/` (queue, window, hotspot, Tony420 hijack). Not placed in any scene | `test_icq_queue`, `test_wifi_hotspot`, `test_tony420_hijack` | `world_data/events/icqdialogues/` (3 messages plus the hijack) | A hotspot the bros can walk up to; Mom and Bestie chats; the once-per-hotspot top-up (`game_design_document.md:257`) | ign, uya, rcm, li0t |
| Couchsurfing Chronicles | `quests/general_quests/couchsurfingchronicles.md:61` (the four states); `templates/couchsurf_host_template.md` | Small (g40c) | None | None | One out-of-date file | Everything | **j1h6**, w7nx, zqqy, g40c |
| Brewery tour and passport | `quests/general_quests/brewerytour.md:1-50`; ledger :122 | Small (91iz, nea6) | `core/brewery_passport.gd`, `core/vanek_taproom.gd` | `test_brewery_passport`, `test_bar_discount`, `test_vanek_taproom` | `brewery_tour/breweries.json` (16 breweries) | Only the Arcade's Taproom brewery is playable; selfie scrapbook | 4ti, 4med, akw, nea6, 91iz |
| Reputation and Street Rep | `mechanics/Social/socialmechanicsandreputationsystem.md` (251 lines); `game_design_document.md:261` | Yes: never approved. Only ruling: not shown in the menu (ledger :707) | None | None | None | A yes, no or later from you | **trl3** |

### Minigames, menus, sound and settings

| Mechanic | Design | Rulings open | Code | Tests | Data | What's missing | Beads |
|---|---|---|---|---|---|---|---|
| Arcade minigames (claw, DDR, skee-ball, foosball, mirror puzzle, Taproom maze) | Ledger :380-417 and later Arcade rounds; `mechanics/Social/minigames.md` (9 lines, other cities) | North wing contents (u5i) | `worlds/debaucheryville/absinthe_arcade/` (claw, `ddr/`, `rec/`, mirror puzzle), `core/taproom_maze.gd` | `test_arcade_claw`, `test_claw_screen`, `test_ddr`, `test_rec_games`, `test_arcade_mirror_shadow_puzzle`, `test_taproom_maze` | `taproom_maze/sections.json` | DDR songs and wiring into the hall; art states | cht, u5i, lyvh, sjoc, w2ig |
| Field menu (9 sections) | Ledger :699-707 (round v36) | None | `ui/field_menu.gd` | `test_field_menu` | n/a | Equip and Settings are display-only | **t1gn**, **j0zo**, z3ec |
| Sound and music | `audio/musicalbeats.md`; `game_design_document.md:344`. No system doc | Content is yours | Three scripts each play one sound. No shared player, no music | None | 3 sound files | An audio system; all music | **pqe9**, yf2j, k3qa |
| Settings and accessibility | `ux/UX & Accessibility Guide.md:10-22`; `game_design_document.md:258`, `:313`, `:320`, `:350`; `ux/accessibility.md` is a placeholder | Yes: nothing ruled | `ui/field_menu.gd:550` shows text; reduced motion exists for Arcade effects | `test_arcade_ambient_fx` | n/a | A Settings screen that changes anything | **j0zo** |

## What blocks a playable vertical slice of Debaucheryville

Ranked, most blocking first. "Slice" here means what the approved slice spec asks for: start the game, walk, talk, fight, win something, save, quit, come back.

1. **The game can't be saved.** The save code works and is tested; nothing calls it. (**x2ws**)
2. **There is no title screen.** No New Game, no Continue. (**9jzp**)
3. **Debaucheryville is one building.** Only the Absinthe Arcade exists as screens. The district diagram and map decisions come first. (eaiq, 467)
4. **No FREE Wi-Fi hotspot is placed anywhere.** It is the ruled save point and the door to ICQ and Tony420. (uya, ign)
5. **No shop sells anything.** The shop screen is built; the first shop waits on your approval. (it49)
6. **Fights pay nothing lasting.** XP is counted and thrown away; no ruling says how the bros grow. (5aie, **028k**)
7. **Two of three bros can only Attack.** (**g0jr**)
8. **No way to rest.** The clock can reach closing time, and there is nowhere to sleep. (**8snp**)
9. **No fights outside the Arcade, and no rule for losing one.** (**skjd**)
10. **Quests don't pay rewards from data, and most aren't in the Quest Log.** (ou0t, **zkhb**)
11. **Dialogue has three implementations.** New NPCs have no agreed way to talk. (**04t2**)
12. **No sound system.** (**pqe9**)
13. **Intoxication tiers aren't built**, though drinking is the premise. (p0j, f3tq)
14. **The original status list isn't in the data.** (**vdrt**, 64vo)
15. **The battle screen lacks the turn-order strip and status icons.** (**ibgl**)

Not slice-blocking, but unbuilt: equipment (**t1gn**), Combos (**rl4c**), Taunt (**wuyu**), couchsurfing (**j1h6**), reputation (**trl3**), the city boss (**nu0k**), settings (**j0zo**), city travel (**ya5e**), and economy phases 2 to 6 (22n3, li0t, fxon, ml5r, wgso, nm8y).

## Mechanics the design mentions with no design doc at all

Each of these appears as a line or two in the game design document (or a placeholder file) and nowhere else.

| Mechanic | Where it's mentioned | Bead |
|---|---|---|
| Street encounters: visible enemies, ambushes, auto-win | `design/game_design_document.md:16`, `:292` | **skjd** |
| Losing a fight outside the Arcade | Only cabinets are ruled (`battle_numbers_proposal.md:22`) | **skjd** |
| Travel between cities | `design/game_design_document.md:10` | **ya5e** |
| XP, levelling, classes, unlockables | Placeholders in `design/mechanics/Progression/` | 5aie, **028k**, ps9 |
| Boss mechanics; the city boss | `design/mechanics/Battle/bossmechanics.md` (placeholder); GDD :131 | **nu0k** |
| Where and how the bros rest | Ledger :670 only | **8snp** |
| Save rules (when autosave fires) | `design/mechanics/Systems/save_load.md` (placeholder); GDD :340 | **x2ws** |
| The dialogue system | `design/narrative/dialoguesystem.md` (placeholder) | **04t2** |
| The audio system (music, mix, volume) | `design/audio/musicalbeats.md` covers sung stingers only | **pqe9** |
| Shop types, item values, the black market as a system | `design/economy/shoptypes.md`, `itemvalue.md`, `blackmarket.md` (placeholders) | ps9, it49 |
| Flirting and NPC affinity | `design/mechanics/Social/flirting.md`, `npcaffinity.md` (placeholders) | ps9, **trl3** |
| Each bro's overworld ability (Pilsner negotiates, Chadwick unlocks events, Bradley breaks obstacles) | `design/game_design_document.md:42` | none (overflow) |
| Swapping bros in and out during battle | `design/game_design_document.md:42` | none (overflow) |
| Titles and achievements ("Street Philosopher", "All the Tea", "Poster Collector") | `design/game_design_document.md:191`, `:206`, `:271` | none (overflow) |
| City-completion rewards and cosmetic palettes | `design/game_design_document.md:260` | 7lys (research) |
| NPCs remarking on the player's habits (banter and easter-egg data) | `design/game_design_document.md:327-338` | none (overflow) |
| HUD, navigation flow, wireframes | `design/ux/hud_layout.md`, `navigationflow.md`, `wireframes.md` (placeholders) | ps9 |

## New beads filed (19)

Needs your decision (all carry tap-to-answer options on the bead page):

| Bead | Question |
|---|---|
| Eurobound-8snp | Where can the bros rest? |
| Eurobound-skjd | How should street encounters get designed? |
| Eurobound-rl4c | Combos: number a starter set, or park them? |
| Eurobound-wuyu | Taunt, counter-brags, beat-synced turn order: number them or park them? |
| Eurobound-g0jr | How do Chadwick's and Bradley's first moves get numbers? |
| Eurobound-028k | XP levels, the Clout ladder, or both? |
| Eurobound-vdrt | How does the original status list enter the data? |
| Eurobound-j0zo | Which settings and accessibility options ship first? |
| Eurobound-ya5e | When and how is city-to-city travel designed? |
| Eurobound-nu0k | Count Velvet Absinthe: now, or after the slice? |
| Eurobound-trl3 | Is the reputation system in, out or parked? |

Ready to build (no decision needed, except where noted):

| Bead | Work |
|---|---|
| Eurobound-x2ws | Make the game save (hotspot save; autosave moments to confirm with you) |
| Eurobound-9jzp | Title screen |
| Eurobound-04t2 | Pick one way to show dialogue |
| Eurobound-zkhb | Quest data nothing reads; fill the Quest Log |
| Eurobound-pqe9 | Audio system plumbing |
| Eurobound-ibgl | Battle screen: turn-order strip, peek, status icons |
| Eurobound-t1gn | Equipment (blocked on 70z) |
| Eurobound-j1h6 | Couchsurfing runtime (blocked on w7nx and 8snp) |

I also linked 5aie (XP payout) as waiting on 028k.

## Overflow: gaps found but not filed

I kept to the 20-bead cap and left these lower-priority gaps unfiled:

1. **Bro overworld abilities and in-battle swapping** (`design/game_design_document.md:42`): no design, no code. Needs your ruling.
2. **Titles and achievements** (GDD :191, :206, :271): the menu ruling says no Achievements section (ledger :707); nothing says whether titles exist at all.
3. **Bulletin boards as a system:** design exists (`design/worlds/shared/interactables/Bulletin Boards/bulletin_boards.md`, GDD :263-272); the only code is on the Arcade exterior. The read-all-boards reward is unruled.
4. **Easter-egg and banter data nothing reads:** `game/assets/data/npcs/easter_eggs.json` and `dialogue_trees/behavioral_triggers.json`. Partly noted in 04t2.
5. **ICQ contacts and the hotspot top-up** (GDD :256-257): Mom, Bestie, Hot Kroger Guy, the once-per-hotspot heal. The data has 3 messages.
6. **World reactions to Bravado level** (`design/mechanics/Battle/bravado.md:103`): no numbers, no code.
7. **Regional minigame hooks** (`design/mechanics/Social/minigames.md`): "Party Foul" and "Off-Tempo" are named with no numbers.
8. **Localization** (GDD :342, "localization ready"): no design, no string tables.
9. **Controller rumble and key remapping** (UX guide :13-14): folded into j0zo's question, with no build bead yet.
10. **Design docs to backfill from the ledger:** the game clock, menu and save rulings live only in the ledger; their design files are placeholders (covered loosely by ps9).

## Limits of this audit

- I did not run Godot or the test suite. Eurobound-ewy notes that the test run crashes on exit after passing.
- I read the ledger by search, not end to end, so a ruling I didn't search for could exist. Each new bead tells its owner to check canon before acting.
- Other cities (Publandia, Sinfonia, Shamsterdam) have no screens and almost no engine data. I treated that as outside "a Debaucheryville slice" and did not list it as gaps.
- The bead review page was not re-synced by this audit; its timer picks up the new beads.
