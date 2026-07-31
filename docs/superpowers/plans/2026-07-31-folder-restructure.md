# Eurobound Folder Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (inline). Do NOT use subagent-driven-development for this plan: Tasks 4–9 are AUTHOR-INTERACTIVE (the author personally moves files as a learning exercise) and every game batch requires author approval of its destination map before moving. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure the repo into `game/` (Godot project, by-feature layout) + `design/`, `marketing/`, `production/`, `tools/`, `docs/` — per the approved spec `docs/superpowers/specs/2026-07-31-folder-restructure-design.md`.

**Architecture:** Two tracks. Prose (markdown/docx/images, no code references) flows through a root `_sorting/` staging folder and is hand-placed by the author in guided sessions. Game files (`.tscn`/`.gd`/`.json`/companions) never enter staging: they move via `git mv` in small batches, Claude rewrites `res://` references in the same commit, and the game must boot + pass GUT before the next batch.

**Tech Stack:** Godot 4.4 (mobile renderer), GDScript, GUT test framework, git on Windows (case-insensitive FS), PowerShell/bash.

## Global Constraints

- Godot binary: resolve in Task 1 and substitute for `$GODOT` everywhere. Verification commands (run from repo root after Task 3):
  - **BOOT:** `$GODOT --headless --path game --quit-after 10` → must exit 0 with no `SCRIPT ERROR`/`Cannot open` lines.
  - **TEST:** `$GODOT --headless --path game -s res://addons/gut/gut_cmdln.gd -gdir=res://tests/unit -ginclude_subdirs -gexit` → pass/fail counts must match the Task 1 baseline (or improve).
- Companion files ALWAYS travel with owners: `foo.gd` + `foo.gd.uid`; `img.png` + `img.png.import`. Never commit a move that separates them.
- Every batch = one commit. Never proceed past a failing BOOT/TEST — fix or `git revert` first.
- Author approves each game batch's destination map before any `git mv` runs.
- AUTHOR-INTERACTIVE tasks: Claude narrates (what the file is, proposed home, why); the author moves the file themselves; Claude verifies and commits.
- `_sorting/` exit condition: zero files, then the folder is deleted. Nothing is "parked."
- Naming: snake_case, no spaces, for all NEW folder/file names. Case-only renames on Windows need two hops: `git mv Assets tmp_assets && git mv tmp_assets assets`.
- `.git/`, `.godot/`, `addons/` never enter `_sorting/`. Delete stray `.godot/` caches rather than moving them.
- Content is never edited except: `res://` path rewrites, approved renames, and author-approved duplicate merges.

### Known static `res://` reference inventory (36 total; re-grep each batch before rewriting)

| File | References |
|---|---|
| `project.godot` | `main_scene` (TitleScreen), icon, 5 autoload paths |
| `Scripts/worlds/location_base.gd:7-10` | preloads: Player, NPCBase, Enemy, PauseMenu |
| `Scripts/core/scene_router.gd:17` | BattleScene.tscn |
| `Scripts/core/data_repo.gd:5` | `const DATA_ROOT := "res://Assets/Data/"` (dynamic root — audit callers) |
| `Scripts/ui/pause_menu.gd`, `Scripts/systems/GameState.gd`, `Scripts/characters/npc_controller.gd`, `Scripts/interactables/kebab/kebab_stand_interact.gd`, `Scripts/interactables/restrooms/grease_trap_entry.gd` | 1 each |
| ~8 `.tscn` in `Scenes/worlds/` + `Assets/Godot/` | ext_resource paths incl. `res://Assets/Godot/...` |

---

### Task 1: Preflight — branch, Godot binary, baseline

**Files:** none created; branch `chore/folder-restructure`.
**Interfaces:** Produces: `$GODOT` path and baseline GUT pass/fail counts used by every later task.

- [ ] **Step 1: Confirm clean tree and create branch**

```bash
cd "/c/Users/heirr/OneDrive/Desktop/Hope2_Studio/Eurobound"
git status --porcelain | wc -l   # must print 0
git switch -c chore/folder-restructure
```

- [ ] **Step 2: Locate the Godot 4.4 executable**

Search, and if not found ASK THE AUTHOR where their Godot editor executable lives:

```bash
ls "/c/Program Files/Godot"* /c/Users/heirr/Downloads/Godot* /c/Users/heirr/Desktop/Godot* 2>/dev/null
where.exe godot godot4 2>/dev/null
```

Record the result as `$GODOT` (e.g. `export GODOT="/c/Users/heirr/Tools/Godot_v4.4-stable_win64.exe"`).

- [ ] **Step 3: Record baseline (pre-restructure) boot + tests**

```bash
"$GODOT" --headless --path . --quit-after 10 2>&1 | tee /tmp/baseline_boot.txt
"$GODOT" --headless --path . -s res://addons/gut/gut_cmdln.gd -gdir=res://tests/unit -ginclude_subdirs -gexit 2>&1 | tee /tmp/baseline_gut.txt
```

Write the counts (passing/failing/erroring) into the plan-execution notes. A pre-existing failure is baseline, not a regression — later batches only need to match it.

- [ ] **Step 4: Commit nothing (no changes yet); confirm branch**

```bash
git branch --show-current   # chore/folder-restructure
```

---

### Task 2: Create target skeleton + `_sorting/`

**Files:** Create (with `.gitkeep` in each leaf so git tracks them):
`game/` (populated by Task 3), `design/{characters,worlds/{debaucheryville,publandia,sinfonia,shamsterdam},quests,mechanics,economy,items,narrative,style_guides,ux,reference}`, `marketing/`, `production/`, `tools/` (exists — keep), `builds/`, `_sorting/`.
**Interfaces:** Produces: the empty buckets every walkthrough session places files into.

- [ ] **Step 1: Generate skeleton**

```bash
cd "/c/Users/heirr/OneDrive/Desktop/Hope2_Studio/Eurobound"
mkdir -p _sorting design/{characters,quests,mechanics,economy,items,narrative,style_guides,ux,reference} design/worlds/{debaucheryville,publandia,sinfonia,shamsterdam}
find design _sorting -type d -exec touch {}/.gitkeep \;
```

(`marketing/`, `production/`: created in Task 8 by renaming the existing `Marketing/`, `Production/` — avoid case-collision now.)

- [ ] **Step 2: Commit**

```bash
git add design _sorting && git commit -m "chore(restructure): target skeleton + _sorting staging"
```

---

### Task 3: Move the Godot project into `game/` (layout-preserving — zero path rewrites)

**Files:** Moves `project.godot`, `export_presets.cfg`, `icon.svg`(+`.import`), `Scenes/`, `Scripts/`, `Assets/` (minus non-game content extracted first), `addons/`, `tests/`, `.editorconfig`, `.gitattributes` → `game/`.
**Interfaces:** Produces: bootable project at `game/`; all later BOOT/TEST commands use `--path game`.

- [ ] **Step 1: Extract non-game content from `Assets/` into `_sorting/`**

```bash
mkdir -p _sorting/from_assets
git mv "Assets/Ref Images" _sorting/from_assets/ref_images
git mv Assets/Audio/musicalbeats.md _sorting/from_assets/
git mv "Assets/Data/items/Bottle Opener Keychain.md" _sorting/from_assets/
git mv Assets/Data/lore _sorting/from_assets/lore
git mv Assets/Data/npcs/LoadingStrategy.md _sorting/from_assets/
git rm "Assets/Data/npcs/dialogue_trees/data.lnk"   # Windows shortcut, dead weight
```

- [ ] **Step 2: Move the project shell (internal layout untouched)**

```bash
mkdir -p game
git mv project.godot export_presets.cfg icon.svg icon.svg.import game/
git mv Scenes Scripts Assets addons tests game/
git mv .editorconfig .gitattributes game/ 2>/dev/null || true
rm -rf .godot   # stale cache; regenerates under game/.godot (already gitignored)
```

- [ ] **Step 3: Verify BOOT + TEST against `--path game`**

```bash
"$GODOT" --headless --path game --quit-after 10
"$GODOT" --headless --path game -s res://addons/gut/gut_cmdln.gd -gdir=res://tests/unit -ginclude_subdirs -gexit
```

Expected: matches Task 1 baseline. `res://` paths are relative to `project.godot`, so nothing broke.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "chore(restructure): move Godot project into game/ (layout preserved)"
```

---

### Task 4 (AUTHOR-INTERACTIVE): Author loads `_sorting/`

**Files:** Author moves (Windows Explorer is fine — these carry no code references): `Design/` → `_sorting/design_old/`, `Templates/` → `_sorting/templates/`, `legacy setup/` → `_sorting/legacy_setup/`, `instructions/` → `_sorting/instructions/`, `docs/` non-spec strays → `_sorting/docs_misc/`, and root strays: `EUROBOUND_PRD.md`, `GAMEPLAN.md`, `Eurobound Character Ecosystem Audit & Development Plan.md`, `Eurobound World Naming Consistency Guide.md`, `Location Profile Validation Checklist & Templates.md`, `Week One Write Up.rtf`, `Week1_BonusRiderPack_COMPLETE.pdf`, `eurobounddata.odt`, `flagmanthebusinessclassbloattour.md`, `weapon-ideas.md`, `weapon-ideas.txt`, `workflow.docx`, `onnetts arcade.jpg`(+`.import`), `folderstructure.md`, `package-lock.json`.
**Interfaces:** Produces: fully loaded `_sorting/` for Tasks 5–9. `Marketing/`+`Production/` stay put (renamed in Task 8). `README.md`, `.gitignore`, `.claude/`, `.remember/`, `.superpowers/`, `docs/superpowers/` stay at root.

- [ ] **Step 1:** Claude prints the checklist above; author drags folders/files in.
- [ ] **Step 2:** Verify nothing game-critical entered staging:

```bash
find _sorting -name "*.gd" -o -name "*.tscn" -o -name "*.godot" | wc -l   # expect 0
git status --porcelain | head -50
```

- [ ] **Step 3:** Commit: `git add -A && git commit -m "chore(restructure): stage prose content into _sorting/"`

---

### Task 5 (AUTHOR-INTERACTIVE): Walkthrough — `_sorting/design_old/` worlds + characters

**Files:** Author places files into `design/worlds/<city>/`, `design/characters/<name>/`. Duplicates (e.g. `brewery_passport_book*.md` ×4) are diffed by Claude on the spot; author picks the survivor; losers deleted.
**Interfaces:** Consumes: skeleton (Task 2). Produces: populated `design/worlds/`, `design/characters/`.

- [ ] **Step 1:** Session protocol, repeated per folder: Claude lists contents → states what each file is, proposed destination + one-line why → author moves it (renaming to snake_case as they go) → Claude spot-checks with `git status`.
- [ ] **Step 2:** For each duplicate cluster Claude runs `git diff --no-index fileA fileB`, summarizes deltas, author picks survivor, others deleted.
- [ ] **Step 3:** Commit per session: `git add -A && git commit -m "chore(restructure): sort design worlds/characters (session N)"`

### Task 6 (AUTHOR-INTERACTIVE): Walkthrough — quests, mechanics, economy, items, narrative, style guides, UX

Same protocol as Task 5, targeting the remaining `design/` buckets. Includes root strays from `_sorting/`: `weapon-ideas.md` vs `.txt` (diff, keep one → `design/items/`), PRD/GAMEPLAN → `design/` root or `production/` (author's call), naming guide → `design/style_guides/`.

- [ ] **Step 1:** Run sessions until `_sorting/design_old/` and root-stray files are empty.
- [ ] **Step 2:** Commit per session.

### Task 7 (AUTHOR-INTERACTIVE): Walkthrough — `legacy_setup/`, `instructions/`, `templates/`, `ref_images/`, `docs_misc/`

**Files:** Ref images → `design/reference/` (delete their `.import` files — no longer inside a Godot project). `instructions/project/` (abandoned second Godot project): expected outcome is deletion after author confirms nothing unique. `legacy_setup/`: triage; most is superseded.
**Interfaces:** Produces: `_sorting/` at zero.

- [ ] **Step 1:** Same protocol; for every candidate deletion Claude states "recoverable via git history" and the author confirms.
- [ ] **Step 2:** Exit check + teardown:

```bash
find _sorting -type f -not -name ".gitkeep" | wc -l   # must be 0
git rm -r _sorting
git add -A && git commit -m "chore(restructure): _sorting emptied and removed"
```

---

### Task 8: Rename `Marketing/`→`marketing/`, `Production/`→`production/`, root tidy

**Files:** Case-only renames (two-hop); move `Marketing/Reviews`, `press_kit`, etc. unchanged inside.

- [ ] **Step 1:**

```bash
git mv Marketing tmp_mk && git mv tmp_mk marketing
git mv Production tmp_pr && git mv tmp_pr production
git mv Tools tmp_tl && git mv tmp_tl tools 2>/dev/null || true
git mv Builds tmp_bd && git mv tmp_bd builds 2>/dev/null || true
```

- [ ] **Step 2:** BOOT still fine (nothing touched `game/`). Commit: `git commit -am "chore(restructure): lowercase studio folders"`

---

### Task 9: Game batch A — `core/` (autoloads)

**Files:** `game/Scripts/core/{data_repo,save_system,input_manager,scene_router,game_manager,audio_manager}.gd`(+`.uid`) and `game/Scripts/systems/GameState.gd`(+`.uid`) → `game/core/`. Modify: `game/project.godot` [autoload] block.
**Interfaces:** Produces: `game/core/*`; autoload names (`DataRepo`, `GameState`, `SaveSystem`, `InputSetup`, `SceneRouter`) unchanged — callers by autoload name are unaffected.

- [ ] **Step 1: Author approves this destination map** (show table, wait for yes).
- [ ] **Step 2: Move**

```bash
cd game && mkdir -p core
git mv Scripts/core/* core/
git mv Scripts/systems/GameState.gd Scripts/systems/GameState.gd.uid core/ 2>/dev/null
git mv core/GameState.gd core/game_state.gd 2>/dev/null; git mv core/GameState.gd.uid core/game_state.gd.uid 2>/dev/null
```

- [ ] **Step 3: Rewrite refs.** Edit `game/project.godot` autoloads to `*res://core/data_repo.gd` etc. Then enumerate stragglers — every hit must be fixed before Step 4:

```bash
grep -rn "res://Scripts/core\|res://Scripts/systems/GameState" --include="*.gd" --include="*.tscn" --include="*.godot" .
```

- [ ] **Step 4: BOOT + TEST** (match baseline). GUT tests preload autoload scripts by path — update `tests/unit/test_data_repo.gd`, `test_game_state.gd`, `test_save_system.gd` if they hard-code `res://Scripts/...`.
- [ ] **Step 5: Commit** `git add -A && git commit -m "chore(restructure): game batch A - core autoloads"`

### Task 10: Game batch B — `ui/`

**Files:** `game/Scenes/ui/**`, `game/Scenes/main/{TitleScreen,main,GameManager}.tscn`, `game/Scripts/ui/*` → `game/ui/{menus,hud,dialogue,popup}/...`; `TitleScreen.tscn`+`title_screen.gd` side by side in `game/ui/`.
**Interfaces:** Produces new `main_scene` path `res://ui/title_screen.tscn` (renamed snake_case).

Steps mirror Task 9: approve map → `git mv` (scene + its script land in the same folder) → rewrite (`project.godot` `main_scene`; `location_base.gd` PauseMenu preload; `pause_menu.gd`; any `scene_router` UI routes; grep `res://Scenes/ui\|res://Scenes/main\|res://Scripts/ui`) → BOOT+TEST → commit.

### Task 11: Game batch C — `battle/` then `characters/`

Two sub-batches, same protocol:
- `battle/`: `Scenes/battle/*` + `Scripts/battle/*` → `game/battle/`. Rewrite `scene_router.gd:17` BattleScene path + grep `res://Scenes/battle\|res://Scripts/battle`.
- `characters/`: `Scenes/characters/*` + `Scripts/characters/*` → `game/characters/`. Rewrite `location_base.gd` Player/NPCBase/Enemy preloads + `npc_controller.gd` ref + grep `res://Scenes/characters\|res://Scripts/characters`.

BOOT+TEST+commit after each sub-batch.

### Task 12: Game batch D — `systems/` + worlds shared

**Files:** `Scripts/systems/{breweries,economy,shadow_exchange,icq_events,dialogue_runner.gd}`, `Scripts/events/*`, `Scripts/utilities/*` → `game/systems/...`; `Scripts/worlds/*` (location_base, interaction_system, map_manager, trigger_zones, clocktower script) + `Scenes/worlds/templates/*` → `game/worlds/shared/`.
**Duplicate to resolve (author decides):** `Scripts/events/icq_great_doner_debate_dialogue.gd` vs `Scripts/systems/icq_events/icq_great_doner_debate_dialogue.gd` — diff, keep one.

Protocol as above; grep `res://Scripts/systems\|res://Scripts/events\|res://Scripts/utilities\|res://Scripts/worlds\|res://Scenes/worlds/templates`.

### Task 13: Game batch E — `worlds/debaucheryville/` (biggest batch, incl. `Assets/Godot` dissolution)

**Files → `game/worlds/debaucheryville/`:** `Scenes/worlds/Debaucheryville/**` (scenes+scripts), `Scenes/worlds/vendors/*` (author call: city vs `worlds/shared/vendors`), `Scripts/interactables/**`, ALL of `Assets/Godot/**` (velvet_vipstall scene+script, memelord dialogue+vendor scene, meme_mastery_meter.json, funcoland/internet-cafe JSON), city JSON from `Assets/Data/locations/**` and `Assets/Data/world_data/events/**`.
**Interfaces:** Consumes `worlds/shared/location_base.gd` (extends chains — `.uid` keeps script links stable, but `ext_resource` paths in `.tscn` files must be rewritten).

- [ ] **Step 1:** Author approves map (subfolders: `scenes/`, `interactables/`, `data/`, `restrooms/` as author prefers — propose flat-ish: scenes at root, `data/` for JSON).
- [ ] **Step 2:** `git mv` per map; delete empty `Assets/Godot` tree.
- [ ] **Step 3:** Rewrite: grep `res://Assets/Godot\|res://Scenes/worlds\|res://Scripts/interactables\|res://Assets/Data/locations\|res://Assets/Data/world_data` — the known 8 referencing scenes/scripts (kebab_stand, shady_meat_cart, grease_trap, arcade_restroom, icq_event, velvet_vipstall, ClocktowerPlaza, kebab_stand_interact.gd, grease_trap_entry.gd, GameState.gd) plus any new hits. **data_repo audit:** grep `DataRepo\.` and `DATA_ROOT` callers; any subpath strings referencing moved JSON (`locations/...`, `world_data/events/...`) get updated to the new city paths.
- [ ] **Step 4:** BOOT+TEST; additionally load DebaucheryvilleMain via a manual editor smoke check by the author (city scenes aren't on the boot path).
- [ ] **Step 5:** Commit.

### Task 14: Game batch F — global data + `assets/`

**Files:** `Assets/Data/{items,party,skills,enemies,npcs,world_data(remainder),quest_flags,saves}` → `game/assets/data/...` (enemies/npcs stay grouped by type since files are per-city *data-driven*, loaded by DataRepo — author may instead route per-city files into cities; decide at map approval). `Assets/Audio` → `game/assets/audio`. Then two-hop case rename of the emptied `Assets` shell away entirely.
**Renames while moving:** `publandia dialogue.json`→`publandia_dialogue.json`, `sinfonia_dialogy.json`→`sinfonia_dialogue.json`, `verworldHUD.tscn` (ui batch if not already)→`overworld_hud.tscn`.

- [ ] **Steps:** approve map → move+rename → update `data_repo.gd` `DATA_ROOT := "res://assets/data/"` + audit every `DataRepo.load*` caller's subpath string (`grep -rn "DataRepo\." --include="*.gd" .`) → confirm `find . -maxdepth 1 -name Assets` empty → BOOT+TEST (data_repo tests are the real gate here) → commit.

### Task 15: Final — `tests/`, hygiene, README, merge

- [ ] **Step 1:** `game/Scripts` and `game/Scenes` must now be empty — verify and remove: `find game/Scripts game/Scenes -type f` → 0 files → `git rm -r game/Scripts game/Scenes` (whatever stragglers appear get triaged with the author, not silently deleted).
- [ ] **Step 2:** Full grep for dead paths: `grep -rn "res://Scenes\|res://Scripts\|res://Assets" --include="*.gd" --include="*.tscn" --include="*.godot" game/` → 0 hits.
- [ ] **Step 3:** `.gitignore` update: ensure `game/.godot/`, `builds/*` patterns hold; remove stale `assets/data/saves/*.save` → `game/assets/data/saves/*.save`.
- [ ] **Step 4:** Write structure guide into `README.md` (tree + one-line-per-folder purpose + "where does X go?" table). Delete `folderstructure.md` if it wasn't already triaged in Task 4.
- [ ] **Step 5:** Final BOOT + full GUT + author opens the project in the Godot editor once (import scan clean, no missing-dependency dialogs).
- [ ] **Step 6:** Merge: `git switch feature/bacchanus-beach-beatdown && git merge chore/folder-restructure` (or to `main` — author's call at the time).

## Self-Review Notes

- Spec coverage: root layout (T2/T8), game/ shell (T3), by-feature batches (T9–14), prose walkthrough (T4–7), `_sorting` zero-exit (T7), cleanup/README/gitignore (T15), safety rails embedded in Global Constraints. Ref-images `.import` deletion covered (T7). OneDrive/out-of-scope items untouched.
- Known unknowns made explicit: Godot binary path (T1 asks), vendors placement + enemies/npcs data placement (decided at map-approval gates), GUT test hard-coded paths (T9 Step 4).
