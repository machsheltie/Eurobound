# Dialogue consolidation plan

Bead: Eurobound-04t2. Written 2026-11-14. Status: **waiting on the author** (Eurobound Desk question `Eurobound-04t2-q1`). Nothing in "Migration steps" starts until that answer arrives.

## The decision in one paragraph

The game has three ways to show NPC talk. Only one is in use. This plan recommends keeping that one (the box the Absinthe Arcade already uses), moving it out of the Arcade folder, feeding it from data files, and switching the other two off. The author chooses, because the choice sets how every writer hands in lines.

## The three paths today

All paths below are relative to `game/`.

### Path 1: the box (`DialogueBox`), in use everywhere

- **File:** `worlds/debaucheryville/absinthe_arcade/dialogue_box.gd` (127 lines). A box along the bottom of the screen with three calls: `say(who, line)`, `choose(options)` and `beat()`.
- **Who calls it:** every scene that has talk today.

  | Caller | `say` calls | `choose` calls |
  |---|---|---|
  | `worlds/debaucheryville/absinthe_arcade/grandpa_provides.gd` | 61 | 1 |
  | `worlds/debaucheryville/absinthe_arcade_restroom_hd2d.gd` | 15 | 0 |
  | `worlds/debaucheryville/absinthe_arcade/vanek_talk.gd` | 12 | 2 |
  | `worlds/debaucheryville/absinthe_arcade_interior_hd2d.gd` | 1 | 1 |
  | `worlds/debaucheryville/absinthe_arcade_exterior_hd2d.gd` | 1 | 0 |
  | `worlds/debaucheryville/absinthe_arcade_maintenance_closet_hd2d.gd` | 1 | 0 |
  | `worlds/shared/icq/wifi_hotspot.gd` | 1 | 0 |
  | `worlds/shared/icq/tony420_hijack.gd` | 1 | 0 |

  `absinthe_arcade_taproom_hd2d.gd` creates a box and hands it to `vanek_talk.gd`.
- **Where its lines come from:** two places. The Arcade and Taproom lines are constants inside GDScript (`grandpa_provides.gd`, `core/vanek_taproom.gd`). The ICQ lines are JSON in `assets/data/world_data/events/icqdialogues/`, and the script loops over them.
- **Who decides what is said next:** GDScript. Each conversation is a hand-written function that also runs the game logic (payments, fights, flags).
- **Status effects:** the box already routes every choice through `FieldStatus.choice_index` (`dialogue_box.gd:74`), which is how Green Fairy Confusion picks a random option. Eurobound-izct (text speed, trailing ellipsis, Cottonmouth) is specified against this box.
- **Tests:** `tests/unit/test_dialogue_box.gd` (9 tests), and the box is driven in `test_field_status`, `test_grandpa_provides`, `test_absinthe_completion_lines`, `test_jakub_restroom`, `test_icq_queue`, `test_wifi_hotspot`, `test_tony420_hijack`, `test_save_round_trip`.

### Path 2: the Dialogue Manager add-on, installed and unused

- **Files:** `addons/dialogue_manager/`, registered as an autoload (`project.godot:24`) and an enabled plugin (`project.godot:41`).
- **Who calls it:** nobody. There is no `DialogueManager.` call and no `.dialogue` file anywhere outside the add-on's own folder. (The bead text says `grandpa_provides.gd` and `vanek_talk.gd` use it. They use the box.)
- **What it would read:** `.dialogue` files, a screenplay-like text format with branches, conditions and flag changes written inline. It needs a "balloon" scene to show the text; the game has none of its own.
- **Tests:** none.

### Path 3: the NPC dialogue-tree JSON, loaded and unread

- **Files:** `assets/data/npcs/dialogue_trees/debaucheryville_dialogue.json`, plus four near-empty siblings.
- **Who calls it:** `core/data_repo.gd:38` loads it at startup and fails startup if it is empty. `get_dialogue_tree` (`data_repo.gd:83`) has one caller, a test (`tests/unit/test_data_repo.gd:28`). No scene asks for a tree. `tools/validate_data.py:386` checks only that `vlad_validator` exists.
- **Tests:** that one `test_data_repo` test, and now `tests/unit/test_dialogue_tree_reader.gd` (see "Built now").

## The dialogue-tree data: shape and amount

`debaucheryville_dialogue.json` (dated 2025-09-15) holds three top-level tables:

- `dialogue_trees`: one tree per NPC. A tree is a set of named nodes; the entry node is `default_greeting`. A node has `line_id`, `speaker`, `text`, and optional `options`. An option has `text`, `leads_to` (the next node) and optional `requires` (an item, a flag or a currency amount).
- `status_reactions`: one line per status per NPC (`hungover`, `grease_fingers`, `embarrassed`).
- `world_state_responses`: one line per world-state key per NPC.

| NPC id | Nodes | Options | Options that lead to a node that does not exist |
|---|---|---|---|
| `vlad_validator` | 7 | 7 | 2 |
| `crypto_clown` | 6 | 11 | 7 |
| `shadow_exchange_dealer` | 2 | 5 | 4 |
| **Total** | **15** | **23** | **13** |

So more than half the choices are dead ends. The data also carries fields no code implements: `emotion`, `animation`, `audio_clip`, `party_specific_overrides`, `party_reaction`, `set_flags`, `conditions`, `opens_shop`, `opens_interface`, `triggers_minigame`, `unlocks_area`, `unlocks_shop_discount`, `unlocks_easter_egg`, `consumes_item`, `consumes_currency`, `screenshot_moment`, `social_sharing_trigger`.

The other files:

| File | Contents | Read by |
|---|---|---|
| `dialogue_trees/publandia_dialogue.json`, `sinfonia_dialogue.json` | empty tables | validator only |
| `dialogue_trees/shared_responses.json` | empty table | validator only |
| `dialogue_trees/behavioral_triggers.json` | one entry (`grease_magnet_pattern`) | nothing |
| `npcs/easter_eggs.json` | 6 easter eggs, plus `behavioral_easter_eggs`, `debug_easter_eggs`, `analytics_tracking` blocks | nothing |

**This data predates the standing rulings and needs a content review before any of it reaches the screen.** Examples a reviewer should check against canon: a price in `KC` (all money is SOVS), an `experience` reward, a `meta_commentary` egg (the game never winks), `party_reaction` lines for the bros (the bros-are-doofuses rule), and the social-sharing and analytics hooks. That review is content work and is filed separately (see "Follow-up beads"). This plan changes no line.

## Recommendation: standardise on the box, fed by data files

**Keep `DialogueBox` as the only thing that draws talk. Writers deliver each NPC conversation as a JSON data file. A small walker plays a file through the box. Switch the add-on off.**

Why this one:

1. **It is the only path that works today.** 93 `say` calls, 4 `choose` calls and nine test files already run on it. The add-on has no content and no screen of its own; the trees have no reader.
2. **Status effects already hook into it.** Confusion works now and Eurobound-izct is written against it. On the add-on each of those would be rebuilt inside a new balloon scene.
3. **Writers already deliver this way.** The Writers' Room ICQ messages are JSON that the box plays (`icq_hotspot_messages.json`). NPC talk becomes the same kind of hand-in, and `tools/validate_data.py` can check it before it ships (dead-end choices, missing text).
4. **No rebuild of finished scenes.** The Arcade and Taproom keep working unchanged.

What it costs:

- We write and own a small walker (roughly 150 lines plus tests) that the add-on would have given us for free, along with its editor, syntax checking and translation export. If the game is ever translated, line extraction for JSON has to be built.
- Scripted scenes (Grandpa Provides, Vaněk) stay hand-written GDScript. That is fine for set pieces that run fights and payments. Ordinary NPC talk goes through data.

### The alternatives

- **Switch to the Dialogue Manager add-on.** Writers deliver `.dialogue` script files. Gains a mature tool. Costs: build a balloon, move 93 Arcade/Taproom/ICQ lines and their logic onto it, redo nine test files, rebuild the status hooks, and it all lands in the Absinthe Orchestrator's scene code. High risk to finished work for no visible change.
- **Leave the Arcade on the box and use the add-on for every new NPC.** No rework now, but two systems stay for good: two boxes to style, two places for status effects, two hand-in formats. This is the situation the bead exists to end.

## Migration steps (if the author picks the recommendation)

Each step is its own bead. Order matters.

1. **Move the box.** `git mv game/worlds/debaucheryville/absinthe_arcade/dialogue_box.gd game/ui/dialogue_box.gd` (and its `.uid`). The class name `DialogueBox` stays, so no caller changes; run `gut.py --import` after. Done when the full suite passes with no caller edited.
2. **Agree the hand-in format with the author.** `DialogueTreeReader` already returns a neutral structure (below). What a writer may put in a file (which conditions, which effects) is mechanics and needs a ruling per field; start with the minimum: line, choices, next node, required flag or item, flags set.
3. **Build the walker** (`game/ui/dialogue_walker.gd` or similar): takes a tree from `DialogueTreeReader` and a `DialogueBox`, plays from `start`, hides choices whose `requires` fails, follows `next`, ends when a node has no options. Tests first, with fixture trees.
4. **Extend `tools/validate_data.py`** to fail on what the reader reports (dead-end choices, missing text, missing `default_greeting`).
5. **Point `DataRepo` at the reader** so `get_dialogue_tree` returns the neutral tree, or remove `get_dialogue_tree` and the startup must-not-be-empty check if the old file is retired.
6. **Switch the add-on off:** remove the `DialogueManager` autoload line and the plugin entry through the editor's project settings (never by hand-editing `project.godot`). Deleting `addons/dialogue_manager/` is a second, separate step once nothing references it.
7. **Old data:** after the content review, each of the three old trees and six easter eggs is either rewritten in the agreed format or retired with `git rm`. `behavioral_triggers.json`, `shared_responses.json` and the two empty city files follow the same ruling.
8. **Fill in the design docs:** `design/narrative/dialoguesystem.md` and `design/mechanics/Social/dialoguetrees.md` are placeholders; replace them with the agreed format once step 2 is ruled.
9. **Eurobound-izct** (status effects on the box) unblocks after step 1.

If the author picks the add-on instead, steps 1 and 3 to 5 are replaced by: build a balloon scene, port `FieldStatus.choice_index` into it, convert callers scene by scene with the Absinthe Orchestrator, and convert or retire the JSON trees (the reader is what a converter would read).

## What stays

- `DialogueBox` and its API (`say`, `choose`, `beat`, `close`, `press`).
- Every existing line, exactly as written.
- Hand-written scripted scenes: `grandpa_provides.gd`, `vanek_talk.gd`, the restroom scene, ICQ.
- The ICQ JSON format and its readers (`IcqQueue`, `Tony420Hijack`).

## Risk

| Risk | Likelihood | What limits it |
|---|---|---|
| Moving the box breaks a caller | Low | `class_name` lookups do not depend on the path; `gut.py --import` plus the full suite proves it |
| The stale class cache hides a break after the move | Medium | always run `--import` after the `git mv` |
| Old tree content ships unreviewed | Medium | the walker is wired to no NPC until the content review bead closes |
| The format grows fields nobody ruled on | Medium | the reader keeps unknown fields in `extra` and the walker ignores them; each new field needs a ruling |
| Removing the add-on autoload breaks something hidden | Low | no caller exists (grep `DialogueManager` outside `addons/` is empty); remove the autoload first, the folder later |

## What the Absinthe Orchestrator's code would need

This bead edits none of it. Under the recommendation the Arcade and Taproom scripts need **nothing**: `DialogueBox` keeps its name and API, and the scripts refer to it by class name, not by path. Listed for completeness:

- `absinthe_arcade_exterior_hd2d.gd:111`, `absinthe_arcade_interior_hd2d.gd:344`, `absinthe_arcade_maintenance_closet_hd2d.gd:161`, `absinthe_arcade_restroom_hd2d.gd:167`, `absinthe_arcade_taproom_hd2d.gd:62`: each calls `DialogueBox.new()`. No change.
- `absinthe_arcade/grandpa_provides.gd`, `absinthe_arcade/vanek_talk.gd`: type-hint `DialogueBox`. No change.
- The Orchestrator should be told before the `git mv` in step 1 so it is not mid-edit in that folder, and should run `--import` afterwards.
- Optional, later, its call: moving Arcade and Taproom line constants out of GDScript into data files. Not required by this plan.

Under the add-on option, all seven files above would be rewritten.

## Built now (needed whichever option wins)

`game/core/dialogue_tree_reader.gd` (`DialogueTreeReader`), with tests in `game/tests/unit/test_dialogue_tree_reader.gd`. It is wired to no screen and no autoload.

- `DialogueTreeReader.read_file(path)` and `read_doc(dictionary)` return `{"trees": {...}, "problems": [...]}`.
- A tree is `{"npc_id", "start", "nodes", "status_lines", "world_state_lines"}`. `start` is `"default_greeting"`, or `""` when the tree has none.
- A node is `{"id", "line_id", "speaker", "text", "options", "extra"}`. An option is `{"text", "next", "requires", "extra"}`. Fields the reader does not know are copied untouched into `extra`.
- `problems` is a list of plain sentences: dead-end choices, nodes with no text, trees with no `default_greeting`, unreadable files. The reader reports; it repairs and invents nothing.

Under the recommendation the walker and the validator consume it. Under the add-on option a one-off converter consumes it. Under either, it is how the content review lists what the old data contains.

## Follow-up beads

- Content review of the pre-ruling dialogue-tree and easter-egg data (author-ruling; filed from this bead).
- Migration steps 1 to 9 are filed once the author answers `Eurobound-04t2-q1`.
