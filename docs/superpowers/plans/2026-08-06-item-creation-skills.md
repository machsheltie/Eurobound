# Item Creation Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build two chained Claude Code skills that force every new Eurobound item through the correct template, into the correct city/general folder, and then into the engine JSON.

**Architecture:** Two skill directories under `.claude/Skills/`. `eurobound-item-creation` handles authoring: mandatory context pre-load, author interview, template selection, folder routing, verification, critic pass. Its final step invokes `eurobound-item-engine-sync`, which reads the finished doc and writes the matching entry into `game/assets/data/items/*.json`, then runs the data validator.

**Tech Stack:** Markdown skill files with YAML frontmatter. Python 3.13 for validation (`tools/validate_data.py`, PyYAML available). Git Bash for verification commands.

**Spec:** `docs/superpowers/specs/2026-08-06-item-creation-skill-design.md`

## Global Constraints

- Skill directory casing is `.claude/Skills/` — **capital S**. The repo already tracks 113 files under that path. Do not create `.claude/skills/`.
- New files and folders: snake_case for content, kebab-case for skill directory names (matching `eurobound-satire-voice`, `eurobound-adversarial-critic`).
- Every price written by these skills is in **SOVS**. Never the euro glyph, never "euros", never "koruna".
- The synopsis lives at `design/narrative/Synopsis.md`. `CLAUDE.md` still points at `Design/Synopsis.md`, which does not exist. Use the real path.
- Item templates live in `design/templates/`. `/Templates` at repo root is the legacy location named in CLAUDE.md; the restructure already moved them.
- Skill frontmatter must be valid YAML with exactly two keys: `name` and `description`. `name` must match the directory name.
- No skill may create a safe-build mechanism, content flag, or string-swap toggle. `CLAUDE.md` bans these permanently.

---

### Task 1: `eurobound-item-creation` skill

**Files:**
- Create: `.claude/Skills/eurobound-item-creation/SKILL.md`

**Interfaces:**
- Consumes: existing skills `eurobound-satire-voice` and `eurobound-adversarial-critic` (both at `.claude/Skills/`, currently untracked in git); templates in `design/templates/`; the five item folders under `design/items/`.
- Produces: a finished item `.md` at a routed path, and the invocation contract for Task 2 — the sync skill is invoked with the absolute path to that finished doc.

- [ ] **Step 1: Write the verification script first**

Create `scratch/verify_item_creation_skill.sh` (temporary, deleted in Step 7). This is the failing test.

```bash
#!/usr/bin/env bash
# Verifies the eurobound-item-creation skill file is well-formed and self-consistent.
set -u
SKILL=".claude/Skills/eurobound-item-creation/SKILL.md"
fail=0

check() { if [ "$1" = "0" ]; then echo "PASS: $2"; else echo "FAIL: $2"; fail=1; fi }

test -f "$SKILL"; check $? "skill file exists"

# Frontmatter parses as YAML and has name matching the directory
python -c "
import sys, yaml
raw = open('$SKILL', encoding='utf-8').read()
parts = raw.split('---')
fm = yaml.safe_load(parts[1])
assert set(fm.keys()) == {'name','description'}, fm.keys()
assert fm['name'] == 'eurobound-item-creation', fm['name']
assert len(fm['description']) > 200, 'description too thin to trigger reliably'
" 2>&1; check $? "frontmatter valid, name matches dir, description substantial"

# Every repo path the skill names must actually exist
python -c "
import re, os, sys
raw = open('$SKILL', encoding='utf-8').read()
paths = set(re.findall(r'\`((?:design|game|tools|docs)/[A-Za-z0-9_./-]+)\`', raw))
missing = [p for p in paths if not os.path.exists(p)]
assert not missing, 'missing paths: ' + repr(missing)
print('checked', len(paths), 'paths')
" 2>&1; check $? "all referenced repo paths exist"

# The five destination folders must all be named
for d in general_items publandia_items debaucheryville_items sinfonia_items shamsterdam_items brewery_tour; do
  grep -q "$d" "$SKILL"; check $? "names destination $d"
done

# All four templates must be named
for t in permanent_item_template signature_beer_item_template opener_item_template stamp_item_template; do
  grep -q "$t" "$SKILL"; check $? "names template $t"
done

# Mandatory pre-load targets
grep -q "eurobound-satire-voice" "$SKILL"; check $? "requires satire-voice preload"
grep -q "design/narrative/Synopsis.md" "$SKILL"; check $? "uses correct Synopsis path"
grep -q "eurobound-item-engine-sync" "$SKILL"; check $? "hands off to engine sync"

# Currency discipline: the skill must not itself contain a euro glyph
! grep -q "€" "$SKILL"; check $? "no euro glyph in skill text"

exit $fail
```

- [ ] **Step 2: Run it to make sure it fails**

Run: `bash scratch/verify_item_creation_skill.sh`
Expected: `FAIL: skill file exists` and a nonzero exit — the skill does not exist yet.

- [ ] **Step 3: Create the skill directory**

```bash
mkdir -p .claude/Skills/eurobound-item-creation
```

- [ ] **Step 4: Write the skill file**

Create `.claude/Skills/eurobound-item-creation/SKILL.md` with exactly this content:

````markdown
---
name: eurobound-item-creation
description: Creates any new Eurobound item — permanent items, weapons, equipment, consumables, key items, quest items, brewery beers, bottle openers, passport stamps. Use whenever the user asks to create, add, write, design, or spec a new item for Eurobound, and whenever an autonomous run determines a new item is needed. This skill owns the whole path: it loads the project's satire rules before writing so the content does not come out sanitized, interviews the author instead of inventing item identity, picks the correct template from design/templates/, and files the finished doc into the correct city or general items folder. Do not write an Eurobound item doc freehand — the folder routing and template skeleton are load-bearing for downstream tooling.
---

# Eurobound Item Creation

Every new item goes through this path. No freehand item docs.

## Step 0 — Load context before writing anything

Read these, in this order, before drafting a single line of item text:

1. `CLAUDE.md` — content rules, SOVS-only currency, no real place names, name uniqueness
2. `design/narrative/Synopsis.md` — the premise, the three bros, the world
3. The `eurobound-satire-voice` skill — **invoke it and read it in full**, not just the opening section

Step 0 is not optional and not a formality. The reason it exists: this model's
default instinct is to soften satirical content — hedged jokes, moralizing asides,
a bro who suddenly becomes self-aware. `CLAUDE.md` classes that as a defect of the
highest severity. Loading the rules into context immediately before writing is what
prevents it.

### The non-negotiables, restated here so they are in context at write time

- This is an MA game for adults. Satire ships at full strength or not at all.
- No narrator, no disclaimer, no moral framing, no device that explains the joke.
  The game never winks at the player.
- The only ceiling is no nudity. Sex, sex workers, drugs, drinking, late-night
  partying, red-light districts, and hookups are in-bounds and core to the premise.
- The bros are never afraid, disgusted, self-aware, or scam-aware. They came to
  Europe seeking exactly this. They may be clueless; they are never scared.
- NPCs are never boring, corporate, or professional. Every name is funny.
- No mascots. No pets, puppets, or companion objects. The party is three bros.
- Tone reference is EarthBound: sincere delivery of absurd material. Sincerity is
  the joke. Do not resolve the irony.

## Step 1 — Interview the author

Never invent item identity. Ask, and wait for answers:

- What is the item, and what is it for?
- Which bro, city, NPC, quest, or location does it attach to?
- What is the mundane reality of it, versus what the bros believe it is?
  (This is the deception, and it is the spine of the permanent-item template.)
- What does it cost, and what is it actually worth — in SOVS?
- How is it acquired: purchased, earned, found, quest reward?

Ambiguity escalates. It is never resolved by invention. This holds on autonomous
runs too: if a question is open, ask it rather than guessing.

Ask about genuinely open questions only. If the author already specified something,
do not re-ask it back to them.

## Step 2 — Pick the template

| The item is… | Use |
|---|---|
| A brewery's signature beer | `design/templates/signature_beer_item_template.md` |
| A brewery bottle opener | `design/templates/opener_item_template.md` |
| A brewery passport stamp | `design/templates/stamp_item_template.md` |
| Anything else | `design/templates/permanent_item_template.md` |

`permanent_item_template.md` is the default. The three brewery templates apply only
to those specific classes.

Read the chosen template before filling it in. Then:

- Keep every H2 header (with its emoji) and every table column shape exactly as the
  template has them. The permanent template states outright that downstream tooling
  depends on this skeleton matching.
- Delete the instructional HTML comment block from the finished doc.
- Include optional subsections (per-character variants, distinction-from-equipment)
  only when they apply; omit them otherwise, per the template's own instructions.
- Replace every `[bracketed placeholder]`. None may survive into the finished file.

## Step 3 — Route the file

| The item is… | Goes to |
|---|---|
| Found everywhere, not tied to one city | `design/items/general_items/` |
| Tied to Publandia | `design/items/publandia_items/` |
| Tied to Debaucheryville | `design/items/debaucheryville_items/` |
| Tied to Sinfonia | `design/items/sinfonia_items/` |
| Tied to Shamsterdam | `design/items/shamsterdam_items/` |
| A brewery beer, opener, or stamp | `design/items/brewery_tour/` |

Apply this test in order:

1. Is it a brewery beer, opener, or stamp? → `design/items/brewery_tour/`. Done.
2. Is its source — the NPC, shop, quest, or location that provides it — in exactly
   one city? → that city's folder.
3. Is it sold by a generic vendor type, dropped by common enemies, or obtainable in
   two or more cities? → `design/items/general_items/`.
4. Still unclear? → **ask the author.** Never guess the folder.

Do not relocate or reorganize items that already exist. This skill routes the item
it is creating right now, and nothing else.

## Step 4 — Name the file

snake_case, no spaces:

- Standard items: `<item_name>_item.md` — e.g. `vip_wristband_item.md`
- Brewery items keep their prefix: `beer_<brewery_slug>_item.md`,
  `opener_<brewery_slug>_item.md`, `stamp_<brewery_slug>_item.md`
- Item ID inside the doc: `item_<item_name_snake_case>`, or the brewery prefix form

## Step 5 — Blocking checks, before writing

Both of these stop the skill and go back to the author:

- **Uniqueness.** Grep the repo for the display name and the item ID. `CLAUDE.md`
  requires every name to be unique across the whole game. A collision is a stop —
  not a quiet rename-and-continue.
- **Currency.** Every price is SOVS. No euro glyph, no "euros", no "koruna".

## Step 6 — Write the doc

Fill the template. Write at full strength. The item's comedy lives in the gap
between what it actually is and what the bros believe it is — make that gap
specific and concrete on both sides. Vague is not safe; vague is just unfunny.

## Step 7 — Verify, with evidence

Run the checks and report actual output. Do not assert success without it.

- File exists at the routed path
- No `[bracketed placeholder]` text survives
- No euro glyph, "euro", or "koruna" anywhere in the file
- Display name and item ID are unique across the repo
- Every template H2 header is present and intact
- The instructional comment block is gone

If a check fails, fix it and re-run. Never report done on a failing check.

## Step 8 — Critic pass

Invoke the `eurobound-adversarial-critic` skill against the new file. It hunts for
sanitization — pulled punches, moralizing, hedges, softened jokes — and for rule
violations. Surface its findings to the author.

This is the second line of defense against the softening instinct. Do not skip it
because the draft "feels fine."

## Step 9 — Hand off to engine sync

Invoke the `eurobound-item-engine-sync` skill, passing the path to the finished doc.

This step is mandatory, not a suggestion. It is how the item reaches the engine data.

## Out of scope

This skill does not:

- Sort or move the legacy loose `*_item.md` files in `design/items/`
- Author PNG asset specs
- Write the quests, NPCs, or locations the item references — those need their own
  author rulings and their own templates
- Touch the per-location JSONs under `design/worlds/<city>/items/`
````

- [ ] **Step 5: Run the verification script to confirm it passes**

Run: `bash scratch/verify_item_creation_skill.sh`
Expected: every line `PASS:`, exit 0.

If `all referenced repo paths exist` fails, the script prints the missing paths — fix the skill text to name real paths rather than loosening the check.

- [ ] **Step 6: Confirm the skill is discoverable**

Run: `ls .claude/Skills/eurobound-item-creation/SKILL.md && head -3 .claude/Skills/eurobound-item-creation/SKILL.md`
Expected: the file lists, and line 2 reads `name: eurobound-item-creation`.

- [ ] **Step 7: Remove the scratch script and commit**

```bash
rm -f scratch/verify_item_creation_skill.sh
rmdir scratch 2>/dev/null
git add .claude/Skills/eurobound-item-creation/SKILL.md
git commit -m "skill: eurobound-item-creation — template routing and city folders"
```

---

### Task 2: `eurobound-item-engine-sync` skill

**Files:**
- Create: `.claude/Skills/eurobound-item-engine-sync/SKILL.md`

**Interfaces:**
- Consumes: the invocation contract from Task 1 — a path to a finished item `.md`. Reads that doc's Item Identity block for Item ID, Display Name, Item Type.
- Produces: an entry in one of `game/assets/data/items/consumables.json`, `equipment.json`, or `key_items.json`, plus the output of `python tools/validate_data.py`.

- [ ] **Step 1: Write the verification script first**

Create `scratch/verify_item_sync_skill.sh`. This is the failing test.

```bash
#!/usr/bin/env bash
set -u
SKILL=".claude/Skills/eurobound-item-engine-sync/SKILL.md"
fail=0
check() { if [ "$1" = "0" ]; then echo "PASS: $2"; else echo "FAIL: $2"; fail=1; fi }

test -f "$SKILL"; check $? "skill file exists"

python -c "
import yaml
raw = open('$SKILL', encoding='utf-8').read()
fm = yaml.safe_load(raw.split('---')[1])
assert set(fm.keys()) == {'name','description'}, fm.keys()
assert fm['name'] == 'eurobound-item-engine-sync', fm['name']
assert len(fm['description']) > 150
" 2>&1; check $? "frontmatter valid and name matches dir"

python -c "
import re, os
raw = open('$SKILL', encoding='utf-8').read()
paths = set(re.findall(r'\`((?:design|game|tools|docs)/[A-Za-z0-9_./-]+)\`', raw))
missing = [p for p in paths if not os.path.exists(p)]
assert not missing, 'missing paths: ' + repr(missing)
" 2>&1; check $? "all referenced repo paths exist"

for j in consumables.json equipment.json key_items.json; do
  grep -q "$j" "$SKILL"; check $? "names target $j"
done

grep -q "validate_data.py" "$SKILL"; check $? "runs the data validator"
grep -q -i "does not invent\|do not invent" "$SKILL"; check $? "refuses to invent a schema"
! grep -q "€" "$SKILL"; check $? "no euro glyph in skill text"

exit $fail
```

- [ ] **Step 2: Run it to make sure it fails**

Run: `bash scratch/verify_item_sync_skill.sh`
Expected: `FAIL: skill file exists`, nonzero exit.

- [ ] **Step 3: Confirm the current engine JSON shapes before writing the skill**

Run: `cat game/assets/data/items/consumables.json game/assets/data/items/equipment.json game/assets/data/items/key_items.json`

Expected, as of 2026-08-06: `consumables.json` holds three entries keyed by snake_case id, each with `display_name`, `heal_hp`, `heal_sp`, `description`. `equipment.json` is `{"schema_version": "1.0", "equipment": {}}`. `key_items.json` is `{"schema_version": "1.0", "key_items": {}}`.

If these differ, the skill's Schema section below must be updated to match reality before continuing.

- [ ] **Step 4: Create the directory and write the skill file**

```bash
mkdir -p .claude/Skills/eurobound-item-engine-sync
```

Create `.claude/Skills/eurobound-item-engine-sync/SKILL.md` with exactly this content:

````markdown
---
name: eurobound-item-engine-sync
description: Registers a finished Eurobound item design doc into the engine item data under game/assets/data/items/. Invoked automatically as the final step of the eurobound-item-creation skill, and usable standalone against any existing item .md that has no engine entry yet. Picks the right JSON file from the item's type, writes the entry keyed by item ID, preserves the item's voice in its description rather than flattening it, and runs the data validator. Refuses to invent a schema for the two JSON files that are still empty — it asks the author instead.
---

# Eurobound Item Engine Sync

Takes a finished item design doc and registers it in the engine data.

## Input

The path to a finished item `.md`. If invoked without one, ask which item.

## Step 1 — Read the item's identity

From the doc's Item Identity block, take:

- Item ID
- Display Name
- Item Type

If the doc still contains unfilled `[bracketed placeholders]`, stop. Report which
ones, and send it back to the item author. Do not sync an unfinished doc.

## Step 2 — Pick the target file

| Item Type | Target |
|---|---|
| Consumable — food, drink, drugs, anything used up | `game/assets/data/items/consumables.json` |
| Equippable, swappable through a slot | `game/assets/data/items/equipment.json` |
| Permanent, curse, or quest item | `game/assets/data/items/key_items.json` |

If the type does not map cleanly to one of the three, stop and ask the author.
Do not force a fit.

## Step 3 — Check for a collision

Grep all three JSON files for the item ID. If it already exists anywhere, stop and
report where. Do not overwrite, and do not silently suffix the id.

## Step 4 — Write the entry

**`consumables.json` has an established shape.** Match it:

```json
"lukewarm_kebab": {
  "display_name": "Lukewarm Kebab",
  "heal_hp": 20,
  "heal_sp": 0,
  "description": "Street meat of dubious provenance. Restores 20 HP."
}
```

**`equipment.json` and `key_items.json` are both still empty.** This skill **does
not invent** a schema for either one. The first time an item routes to one of them:

1. Propose an entry shape, derived from the item doc's actual fields and from the
   `consumables.json` conventions.
2. Present it to the author and wait for a ruling.
3. Once ruled, follow that shape from then on, and record the ruling in
   `docs/superpowers/NEXT_WORK.md` so it is not re-litigated.

Preserve `schema_version` and the existing top-level key. Add the new entry inside
the existing object; do not restructure the file.

### The description field

Lift the item's voice from the design doc. Do not rewrite it into flat, functional
prose — a description that reads like a database field is a defect, not a
simplification. Prices in SOVS only.

## Step 5 — Validate

Run: `python tools/validate_data.py`

Report the actual output, pass or fail. If it fails, fix the entry and re-run. Never
report success without the validator's output in hand.

## Refusal conditions

Stop and report rather than proceeding when:

- The item ID already exists in any of the three JSON files
- The source doc still has unfilled `[bracketed placeholders]`
- The Item Type does not map cleanly to one of the three targets
- Writing the entry would require inventing a schema that has not been ruled on
````

- [ ] **Step 5: Run the verification script to confirm it passes**

Run: `bash scratch/verify_item_sync_skill.sh`
Expected: every line `PASS:`, exit 0.

- [ ] **Step 6: Confirm the validator still runs clean on untouched data**

Run: `python tools/validate_data.py`
Expected: whatever it currently reports. Record that output — it is the baseline for Task 3. If it already fails on `main`, note the failure and continue; it is pre-existing and not caused by this work.

- [ ] **Step 7: Remove the scratch script and commit**

```bash
rm -f scratch/verify_item_sync_skill.sh
rmdir scratch 2>/dev/null
git add .claude/Skills/eurobound-item-engine-sync/SKILL.md
git commit -m "skill: eurobound-item-engine-sync — engine JSON registration"
```

---

### Task 3: End-to-end dry run

**Files:**
- Temporarily create then delete: `design/items/general_items/plan_dryrun_probe_item.md`
- Read only: both SKILL.md files from Tasks 1 and 2

**Interfaces:**
- Consumes: both skills, complete.
- Produces: confirmation that the chain works, and a clean working tree.

This task proves the two skills chain correctly without committing any invented content. No author interview happens here, because no real item is being created — this is a mechanical wiring check.

- [ ] **Step 1: Confirm both skills are visible to the Skill tool**

Run: `ls -d .claude/Skills/eurobound-item-*`
Expected: exactly two directories — `eurobound-item-creation` and `eurobound-item-engine-sync`.

- [ ] **Step 2: Confirm the routing table covers every folder that exists on disk**

Run:

```bash
for d in design/items/*_items design/items/brewery_tour; do
  name=$(basename "$d")
  if grep -q "$name" .claude/Skills/eurobound-item-creation/SKILL.md; then
    echo "PASS: $name is routed"
  else
    echo "FAIL: $name exists on disk but the skill never names it"
  fi
done
```

Expected: six `PASS` lines — `general_items`, `publandia_items`, `debaucheryville_items`, `sinfonia_items`, `shamsterdam_items`, `brewery_tour`. Any `FAIL` means a destination folder is unreachable through the skill; add it to the routing table.

- [ ] **Step 3: Confirm the handoff is one-directional and complete**

Run:

```bash
grep -c "eurobound-item-engine-sync" .claude/Skills/eurobound-item-creation/SKILL.md
grep -c "eurobound-adversarial-critic" .claude/Skills/eurobound-item-creation/SKILL.md
grep -c "eurobound-satire-voice" .claude/Skills/eurobound-item-creation/SKILL.md
```

Expected: each returns at least 1. The creation skill must reference all three of its collaborators by exact name, or the chain breaks at runtime.

- [ ] **Step 4: Verify the template skeleton check is enforceable**

Confirm the permanent template's H2 headers are extractable, so Step 7 of the creation skill is a real check rather than a vibe:

```bash
grep "^## " design/templates/permanent_item_template.md
```

Expected: the full list of emoji H2 headers — Item Identity, The Deception, Economic Details, Visual Specifications, Stats & Effects, Gameplay Integration, NPC Reactions, Quest Integration, Key Story Moments, Performance & Assets, Validation Checklist, Development Notes.

- [ ] **Step 5: Confirm no euro glyph entered the repo through this work**

Run: `grep -rn "€" .claude/Skills/eurobound-item-creation/SKILL.md .claude/Skills/eurobound-item-engine-sync/SKILL.md`
Expected: no matches, exit 1 from grep.

Check the two SKILL.md files only. This plan document itself does contain the glyph three times — inside the verification scripts, which have to name the character in order to search for it. That is correct and expected; do not "fix" it.

- [ ] **Step 6: Confirm the working tree is clean**

Run: `git status --short`
Expected: the only untracked entries are `.claude/Skills/eurobound-satire-voice/` and `.claude/Skills/eurobound-adversarial-critic/`, which are pre-existing and belong to the author to commit or not. No `plan_dryrun_probe_item.md`, no `scratch/`.

If a probe file was created during exploration, delete it now:

```bash
rm -f design/items/general_items/plan_dryrun_probe_item.md
```

- [ ] **Step 7: Commit the plan document**

```bash
git add docs/superpowers/plans/2026-08-06-item-creation-skills.md
git commit -m "plan: item-creation skills implementation"
```

---

## Open item for the author

The two skills this plan depends on — `eurobound-satire-voice` and
`eurobound-adversarial-critic` — exist on disk but are **untracked in git**. The
creation skill invokes both by name. If they are never committed, the chain works
locally and breaks for any other clone or worktree.

This plan does not commit them, because they are the author's files and were added
deliberately outside this session. Raise it; do not decide it.
