# Eurobound Folder Restructure — Design

**Date:** 2026-07-31
**Status:** Approved by author
**Scope:** Reorganize the entire repository into a clean separation of Godot game project, game design docs, and studio content. Retro JRPG, Godot 4.4, targeting Steam.

## Problem

The repo root is simultaneously the Godot project, the design wiki, and the studio office:

- Two `project.godot` files (root + abandoned `instructions/project/`).
- Game code split across `Scenes/`, `Scripts/`, and a parallel mini-project in `Assets/Godot/` (with its own Scenes/Systems/narrative/data) that live scenes reference via `res://Assets/Godot/...`.
- 510 markdown files (427 in `Design/` alone) scanned by the Godot editor on every open; ~12 loose design docs at root; duplicate variants of the same doc (e.g. four `brewery_passport_book*.md` files); reference photos in `Assets/Ref Images/` imported as game textures.
- Dead weight: `legacy setup/` (58 files), `instructions/project/` (98 files), two competing **empty** graphics trees (`Assets/Graphics/`, `Assets/sprites/`), stale `folderstructure.md` describing a structure that no longer exists.
- Folder names with spaces (`Ref Images`, `World Design`, `legacy setup`) inside a Godot project, against Godot style and export-safety guidance.

One city's content currently lives in ~6 different places. Finding anything requires hunting.

## Decisions (all approved)

1. **`game/` subfolder** holds the entire Godot project. Godot never sees non-game content. `res://` paths are relative to `project.godot`, so the split itself breaks nothing that also keeps its internal layout.
2. **By-feature hybrid layout inside `game/`**: shared systems grouped by function, game content grouped by feature/city. Chosen over keeping by-type because the project is small enough today (57 scenes, 131 scripts, 8 PNGs) that the migration will never be cheaper, and by-feature directly fixes the "one city in six places" problem.
3. **Two-track migration process**: prose content is hand-moved by the author through a `_sorting/` staging folder with a guided walkthrough (familiarization + triage); reference-carrying game files are moved by Claude via `git mv` + reference rewrite + boot verification, batch by batch, with author approval of each batch's destination map. Game files never enter staging; the game is never broken between commits.
4. **Phase 0 lands the in-flight work**: current uncommitted changes on `feature/bacchanus-beach-beatdown` are committed/merged first; restructure happens on a dedicated `chore/folder-restructure` branch from a clean tree.

## Target structure

### Repo root

```
Eurobound/
├── game/            # the entire Godot project — only thing Godot sees
├── design/          # the GDD: all design docs
├── marketing/       # press kit, screenshots, store/compliance docs
├── production/      # schedules, workflows, week write-ups
├── tools/           # Python scripts (validation, content gen, analytics)
├── docs/            # technical docs and specs (this file lives here)
├── builds/          # export output; contents gitignored
└── README.md        # includes the new structure guide
```

Nothing else at root when done. `folderstructure.md` is deleted (superseded by README structure guide).

### game/

```
game/
├── project.godot, export_presets.cfg, icon.svg (+ .import/.uid companions)
├── core/            # autoloads: data_repo, game_state, save_system, input_manager, scene_router
├── systems/         # shared gameplay systems: stats, economy, dialogue engine, ...
├── battle/          # battle scenes + scripts together
├── characters/      # party & NPC scenes/scripts (Bradley, Chadwick, Lord Pilsner, NPCs)
├── ui/              # title screen, menus, HUD
├── worlds/
│   ├── debaucheryville/   # everything for the city: scenes, scripts, JSON data, art
│   ├── publandia/
│   ├── sinfonia/
│   ├── shamsterdam/
│   └── shared/            # location templates, common interactables
├── assets/          # genuinely global: fonts, audio, shared graphics, global data (items, skills, party)
├── addons/          # gut — moves as-is, never triaged
└── tests/
```

- `Assets/Godot/` dissolves entirely into this tree.
- `Assets/Data/` JSON splits: per-city files → their city folder; global data → `assets/data/` or the owning system.
- Both empty graphics trees are deleted; future art goes next to its feature (city art in its city, shared art in `assets/`).
- All folder/file names snake_case, no spaces.
- Autoload paths and `main_scene` in `project.godot` updated as their files move.

### design/

Buckets, not a locked taxonomy — final placement of each file is decided by the author during the walkthrough:

```
design/
├── game_design_spec.md
├── characters/      # per-character folders incl. permanent cosmetic changes
├── worlds/          # per-city folders mirroring game/worlds/
├── quests/
├── mechanics/       # battle, progression, social
├── economy/
├── items/           # weapons, inventory, passport book, NFTs, ...
├── narrative/
├── style_guides/    # incl. naming consistency guide
├── ux/
└── reference/       # EarthBound reference images (outside Godot's reach)
```

Duplicate docs are diffed and merged during the walkthrough; snake_case applied as files are placed.

## Process

**Phase 0 — Checkpoint.** Commit/land the in-flight `feature/bacchanus-beach-beatdown` work. Create `chore/folder-restructure` from the clean tree.

**Phase 1 — Skeleton + staging.** Generate all target folders (empty) plus `_sorting/` at root. Author moves prose-only content into `_sorting/`: `Design/`, `Marketing/`, `Production/`, `Templates/`, `legacy setup/`, `instructions/`, root strays, `Assets/Ref Images/`, non-spec `docs/` content. Excluded from staging always: `.git/`, `.godot/`, `addons/`, all game files.

**Phase 2 — Guided walkthrough (multiple sessions).** Go through `_sorting/` folder by folder. For each item: Claude states what it is, proposed destination, and why; author decides and moves it personally. Duplicates diffed on the spot; dead files deliberately deleted (recoverable from git history). **Exit condition: `_sorting/` reaches zero files, then the folder itself is deleted.** No "sort later" parking.

**Phase 3 — Game migration (Claude moves, author approves).** Batch order: core/autoloads + title screen → ui → battle → characters → systems → one city at a time → shared assets → tests. Per batch: author approves destination map → `git mv` → rewrite all `res://` references (`.tscn`, `.gd` preloads/paths, `project.godot` autoloads and `main_scene`) with `.uid`/`.import` companions traveling with owners → verify game boots to title screen → run GUT tests → commit. A failing batch is fixed or reverted before proceeding.

**Phase 4 — Cleanup.** Structure guide written into README; `.gitignore`/`.gdignore` hygiene; delete `folderstructure.md`; merge `chore/folder-restructure`.

## Safety rails

- Every move is a git commit; rename detection preserves file history; full rollback at any point.
- Boot check + GUT tests gate every game batch.
- Companion files (`.uid`, `.import`) always move with their owners.
- `_sorting/` has a hard zero-files exit condition to prevent a new `legacy setup/`.

## Out of scope

- Moving the repo off OneDrive. Noted risk: `.godot/` cache churn under OneDrive sync; recommend pausing sync during heavy editor sessions. Revisit separately.
- Content changes: no rewriting of design docs beyond merging duplicates; no code refactors beyond path rewrites.
