# Eurobound Vertical Slice — Design

**Date:** 2026-07-30
**Status:** Approved approach: vertical slice fed by existing JSON data (Approach A absorbing the data-driven core of Approach C)
**Context:** Design documentation is extensive (445+ markdown files, rich JSON in `Assets/Data/`), but the Godot project is empty scaffolding — every `.tscn` and `.gd` is a placeholder. This spec defines the first playable milestone. Developer is building their first game and directing AI-assisted implementation.

## Goal

One thin, complete path through the real game, playable end to end:

Title screen → New Game → spawn in Clocktower Plaza (Debaucheryville) → walk as Lord Pilsner (placeholder sprite) → talk to one NPC with a branching dialogue tree → touch one visible roaming enemy → EarthBound-style front-view battle (Bash / Skill / Item / Run) → win, gain XP and one item drop → return to street → save from pause menu → quit, relaunch, Continue restores position and inventory.

**Success criterion:** a friend can complete the loop unassisted on a laptop.

## Out of scope (deferred to later sub-projects)

Party members beyond Lord Pilsner, rolling HP meters, status effects, economy/shops, day/night cycle, minigames, additional locations, final art, music/SFX, mobile export. Each becomes its own spec → plan → implementation cycle on top of a working game.

## Architecture

Godot 4.4, GDScript, existing folder layout preserved.

### Autoloads (singletons)

| Autoload | Responsibility |
|---|---|
| `DataRepo` | Loads and caches JSON from `Assets/Data/` at startup; hands out typed data by ID (e.g. `DataRepo.get_enemy("id")`). Validates schema at load; errors name the exact file and field. |
| `GameState` | Single source of truth: party HP/SP/XP/stats, inventory, gold, story flags, current location and position. What saving serializes. |
| `SceneRouter` | All scene transitions (street ↔ battle, title → game) with fade; restores player position after battle. |
| `SaveSystem` | Serializes `GameState` to `user://saves/slot1.json`; loads it for Continue. |

### Scenes

- `Scenes/main/TitleScreen.tscn` — New Game / Continue (greyed out when no valid save).
- `Scenes/worlds/templates/LocationBase.tscn` — reusable template: TileMapLayer (placeholder tiles), spawn points, NPC/enemy/exit containers. Every future location clones this.
- `Scenes/worlds/Debaucheryville/ClocktowerPlaza.tscn` — the slice's one location, instancing LocationBase.
- `Scenes/characters/Player.tscn` — CharacterBody2D, 4/8-direction free movement, interaction ray.
- `Scenes/characters/NPCBase.tscn` — static NPC; interaction opens dialogue by tree ID.
- `Scenes/characters/Enemy.tscn` — visible roaming enemy (simple wander); body contact triggers battle.
- `Scenes/battle/BattleScene.tscn` — front-view battle UI.
- `Scenes/ui/dialogue/DialogueBox.tscn` — bottom text box, typewriter effect, portrait placeholder, branching choices.
- `Scenes/ui/menus/PauseMenu.tscn` — Resume / Save / Quit to Title.

Systems communicate via signals (`battle_won`, `battle_lost`, `dialogue_finished`, `save_completed`); no script reaches into another scene's internals.

## Data pipeline

The slice reads real content from `Assets/Data/`:

- One location's metadata (existing `debaucheryville_locations.json` entry for Clocktower Plaza / Absinthe Arcade exterior).
- One NPC profile + dialogue tree (`Assets/Data/npcs/`).
- One enemy definition with stats (created under `Assets/Data/enemies/` following existing schema style).
- Three items (from `Assets/Data/items/consumables.json` / `equipment.json`).
- Lord Pilsner's starting stats (created under `Assets/Data/` from `Design/Character Profiles/LordPilsner/`).

**Rule:** content is never hardcoded in GDScript. Adding content later means adding JSON, not code. Where a needed file doesn't exist, create it in `Assets/Data/` in the established style.

## Battle (minimal)

Turn-based, front-view: enemy sprite center, text log, player menu Bash / Skill ("Roast Line", costs SP) / Item / Run. Damage = Offense vs Defense with small random spread; crit chance driven by Luck ("SMAAAASH!!"). Enemy AI: attack every turn. Win → XP + item drop → return to overworld; loss → respawn at plaza spawn with 1 HP (no game-over screen yet). Depth (rolling HP, status effects, charm/flirt actions) bolts on later without restructuring.

## Dialogue (minimal)

Bottom dialogue box, typewriter text, speaker name, placeholder portrait, up to 3 branching choices per node, read from dialogue-tree JSON. Dialogue can set a story flag in `GameState` (proves the flag system).

## Error handling

- Malformed/missing JSON: loud failure at startup via `push_error` naming file and field; game refuses to start rather than misbehaving later.
- Corrupt/missing save: Continue greyed out; New Game always works. Never crash on load.
- Battle/dialogue referencing an unknown ID: error names the ID and the scene that asked for it.

## Verification

- **Automated (GUT):** damage calculator, DataRepo loading/validation, save round-trip (`GameState` → JSON → `GameState` equality).
- **Manual playtest checklist** (kept in the repo): full loop walkthrough including edge cases — save/quit/relaunch, losing the battle, walking every map boundary, declining dialogue choices.

## Placeholder art policy

Colored rectangles or a free CC0 asset pack (e.g. Kenney) for everything. Final art will be AI-generated + commissioned later; sprites drop into working scenes. No art tasks block the slice.

## After the slice

Each subsequent system is its own spec → plan → build cycle, in rough order: battle depth (rolling HP, status effects), second location + SceneRouter travel, shops/economy, party members, quest/flag framework, then content production at scale using the proven JSON pipeline.
