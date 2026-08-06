# Quest-Creation Skill Design

**Date:** 2026-08-06
**Status:** Author-approved design. Implementation pending.
**Author rulings captured:** master-spec format for general quests; all touched cities in one
run; three-way classification; autonomous runs stop and ask; chained engine-sync skill;
canonical JSON shape; `game/assets/data/quests/` as the engine write path.

Two chained skills, mirroring the `eurobound-item-creation` / `eurobound-item-engine-sync`
pair built the same day:

| Skill | Owns |
|---|---|
| `eurobound-quest-creation` | Classification, routing, template fill, satire guardrails, critic pass |
| `eurobound-quest-engine-sync` | Quest JSON under `game/assets/data/quests/`, flag registration |

---

## 1. Why this exists

Quest docs are currently written freehand. The results diverge: `greatdonerdebate.md` is
656 lines with two cities' location lists inline; five general quests are 2-4 line stubs;
`brewerytour.md` and `couchsurfingchronicles.md` follow a decomposed master-spec pattern
that exists nowhere in writing. The template at `design/templates/sidequest_template.md`
is mandatory per `CLAUDE.md`, but nothing routes an author to it, and nothing decides which
folder the result belongs in.

The skill makes the pattern explicit and executable, and it front-loads the satire rules so
new quest text does not come out sanitized.

---

## 2. Classification

Applied in order. The first test that matches wins.

| # | Test | Class | Output |
|---|---|---|---|
| 1 | Content **differs per city** — different NPCs, venues, challenges | `GENERAL-INSTANCED` | Master spec + one instance per city touched |
| 2 | Plays anywhere, **same content**, no per-city variation | `GENERAL-SYSTEMIC` | One full-template file, `City: Any` |
| 3 | Bound to **one city's** NPCs/venues | `CITY-SPECIFIC` | One full-template file in that city folder |
| 4 | Cannot tell | — | **Ask the author. Never guess.** |

Test 1 runs before test 2. A quest described as "scattered across all cities" is instanced,
not systemic — the phrase means per-city content that has not been written yet.

`GENERAL-SYSTEMIC` is rare. Of the twelve files in `general_quests/` today, exactly one
(`wifiroulettegame.md` — "at any free Wi-Fi hotspot") is genuinely systemic. If a quest looks
systemic mainly because its premise is thin, that is an unfinished quest, not a systemic one;
escalate to test 4.

---

## 3. Routing and naming

snake_case, no spaces, per `CLAUDE.md`.

| Class | Path |
|---|---|
| Master spec | `design/Quests/general_quests/<quest_name>.md` |
| City instance | `design/Quests/<city>/<quest_name>_<city>.md` |
| Systemic | `design/Quests/general_quests/<quest_name>.md` |
| City-specific | `design/Quests/<city>/<quest_name>.md` |

Cities: `publandia`, `debaucheryville`, `sinfonia`, `shamsterdam`.

`design/Quests/` carries a capital Q on disk while many docs reference `design/quests/`.
Windows resolves this case-insensitively. The skill writes to the on-disk casing and does not
rename the folder.

Existing files use squashed lowercase (`brewerytourpublandia.md`). The skill routes only what
it is creating right now. It renames and relocates nothing.

### Quest IDs

- City instance and city-specific: `<city>_sidequest_<quest_name>_01`
- Systemic: `general_sidequest_<quest_name>_01`
- **Master spec: no quest ID.** A master spec describes a system, not an instance. Only its
  instances carry IDs.

---

## 4. Document shapes

### Instances, city-specific, and systemic quests

`design/templates/sidequest_template.md`, filled completely.

- Every H2 header and its emoji preserved exactly; downstream tooling depends on the skeleton
- Every `[bracketed placeholder]` replaced — none survive into the finished file
- The instructional HTML comment blocks deleted
- Structure sections used per the template's own instruction: linear Stages, a Binary Path
  Choice, or both. Delete the one not used.
- Instances open with an `**Authority:**` line naming the master spec as winning every
  conflict

### Master spec

No template file is minted for this. The skill carries the skeleton inline, derived from
`design/Quests/general_quests/brewerytour.md`:

```
# <Quest Name> — Master Spec

**Status: CANONICAL SYSTEM (author-ruled <date>).** This file is the authority on how
<quest> works. City quest files hold each city's instances. Where an older doc
contradicts this file, this file wins.

## Overview                       counts, per-city breakdown, designed vs open
## The Trigger                    the one-time ignition event, and the hard gate before it
## The Loop                       what repeats at every instance
## Shared Rewards & Collectibles  what the quest grants across all cities
## City Instance Index            pointer table: city -> file path -> status
## Satirical Targets              franchise-wide, above the per-city targets
## Dead Mechanics                 explicitly do-not-reintroduce, with the reason
## Validation Checklist           the sidequest template's checklist, quest-wide
```

The `Dead Mechanics` section exists because `brewerytour.md` proved it necessary — it is what
stops a later session reintroducing a killed mechanic.

---

## 5. Skill flow — `eurobound-quest-creation`

### Step 0 — Load context before writing anything

In order, before drafting a line:

1. `CLAUDE.md` — content rules, SOVS-only, no real place names, name uniqueness, all side
   quests optional
2. `design/narrative/Synopsis.md`
3. The `eurobound-satire-voice` skill — **invoked and read in full**, not skimmed

Not a formality. This model's default instinct is to soften satirical content; `CLAUDE.md`
classes that as a defect of the highest severity. The non-negotiables are restated inline in
the skill so they sit in context at write time.

### Step 1 — Interview the author

Never invent quest identity. Ask, and wait:

- What is the quest, and what is the joke?
- Who gives it — cover identity and true identity — and where?
- Which cities does it play out in?
- What do the bros think is happening, versus what is actually happening?
- What does it reward, in SOVS, and what does it unlock?
- Is it triggered, or found?

**Ambiguity escalates. It is never resolved by invention. This holds on autonomous runs
identically** — an autonomous run that hits an open question halts and reports the open
questions rather than writing a guess. Ask only about genuinely open points; do not re-ask
what the author already specified.

### Step 2 — Classify

Section 2's test. On `GENERAL-INSTANCED`, confirm which cities are in scope before writing.

### Step 3 — Route and name

Section 3's tables.

### Step 4 — Blocking checks, before writing

Each stops the skill and returns to the author:

- **Uniqueness.** Grep the repo for the quest display name and quest ID. `CLAUDE.md` requires
  every name unique across the game. A collision is a stop, not a quiet rename.
- **Currency.** Every price and reward in SOVS. No euro glyph, no "euros", no "koruna", no
  bare number presented as a price.
- **Place names.** No real city or place names in player-facing text. Parody names only.

### Step 5 — Write

On `GENERAL-INSTANCED`: master spec first, then every city instance in scope, in the same
run. The City Instance Index is filled as instances are written, never left `PENDING` for a
city that was in scope.

On `GENERAL-SYSTEMIC` or `CITY-SPECIFIC`: the one file.

Write at full strength. The comedy lives in the gap between what the bros believe and what is
actually happening — make both sides specific. Vague is not safe; vague is unfunny.

### Step 6 — Verify, with evidence

Run the checks and report actual output. Never assert success without it.

- Every file exists at its routed path
- No `[bracketed placeholder]` survives in any file
- No euro glyph, "euro", or "koruna"; every price carries an explicit SOVS unit
- Display name and quest ID unique across the repo
- Every template H2 header present and intact on template-based files
- Instructional comment blocks gone
- Master spec's City Instance Index matches the instance files actually written
- Quest is marked optional — never gates main progression

### Step 7 — Critic pass

Invoke `eurobound-adversarial-critic` against every file produced. It hunts sanitization —
pulled punches, moralizing, hedges, a bro gone self-aware — and rule violations. Surface
findings to the author.

Second line of defense against the softening instinct. Not skipped because a draft "feels
fine."

### Step 8 — Hand off to engine sync

Invoke `eurobound-quest-engine-sync` with the paths of the finished docs. Mandatory.

---

## 6. Skill flow — `eurobound-quest-engine-sync`

### Write path

`game/assets/data/quests/<quest_id>.json`.

Rationale: every populated sibling under `game/assets/data/` is the engine's read path
(`enemies`, `items`, `locations`, `npcs`, `party`, `skills`, `world_data`). Only `economies/`
and `quests/` are empty — not yet wired, not deliberately unused. This also matches the item
pipeline.

The two JSONs colocated at `design/Quests/debaucheryville/` (`vip_wristbands.json`,
`astronomical_cockup.json`) are design-side drafts. Migrating them is separate work
(section 8), not this skill's job.

A master spec produces no JSON — it has no quest ID. Its instances each produce their own.

### Canonical schema

Derived from those two drafts, which agree on most keys and diverge on three. Resolutions:

| Divergence | Canonical | Why |
|---|---|---|
| `items` vs `items_acquired` | **`items_acquired`**, sub-keyed `standard` / `path_a` / `path_b` | The drafts differ structurally, not just in name: one is flat, one is path-keyed. The sub-keyed form maps 1:1 onto the template's "Standard Rewards (granted regardless of path)" plus its two path blocks. `standard` alone on a linear quest. |
| `localization` vs `localization_notes` | **`localization`** | The block holds dialogue strings with subtitles. That is data, not annotation. |
| `mobile_optimization` | **`presentation`** | See below. |

Base keys, present on both drafts and carried forward: `quest_id`, `display_name`,
`satirical_subtitle`, `city`, `location`, `quest_type`, `recommended_level`,
`estimated_duration_minutes`, `quest_giver`, `prerequisites`, `satirical_targets`,
`quest_stages`, `npcs`, `rewards`, `quest_flags`, `post_credits_scene`, `npc_callbacks`,
`easter_eggs`, `validation_checklist`.

`dialogue_highlights` is optional — present on one draft only.

### The `mobile_optimization` rename

The quest drafts' `mobile_optimization` block contains nothing mobile:

```json
{"screenshot_moments": ["..."], "dialogue_pacing": "standard_with_comedy_beats",
 "cutscene_skippable": false, "comedy_timing": "silence_after_is_the_joke"}
```

Screenshot moments, pacing, cutscene timing — all needed on desktop, and
`"silence_after_is_the_joke"` is load-bearing comedy timing. The block is **misnamed, not
obsolete.** New quest JSON writes it as `presentation`. Nothing is dropped.

This is distinct from the genuine mobile debris in the world files (section 8, item 3).

### Flags

`data/quests/flags.json` does not exist anywhere in the repo, though `sidequest_template.md`
requires every quest flag be registered there.

The sync skill **does not invent it.** It proposes a schema and asks the author, mirroring
`eurobound-item-engine-sync`'s refusal to invent a schema for empty JSON files. Until that
ruling lands, flags live in the design doc's flag table only, and the skill reports the gap on
every run rather than silently proceeding.

### Validation

`Tools/validate_data.py` has **zero** quest handling — it will not validate what this skill
writes. The skill runs it anyway, to catch nothing regressing elsewhere, and reports plainly
that quest validation is unimplemented. It does not report a pass it did not get.

---

## 7. Out of scope

The skill routes what it is creating now, and nothing else. It does not:

- Decompose the five stub generals or `greatdonerdebate.md`
- Rename or relocate existing quest files
- Write the NPCs, locations, or items a quest references — those have their own templates and
  need their own author rulings
- Sweep `mobile_optimization` out of the world files
- Migrate the two colocated design-side quest JSONs

---

## 8. Deferred work logged to the ledger

Recorded in `docs/superpowers/NEXT_WORK.md`:

1. **Five stub general quests** — `vinylhunt.md`, `streetperformertrials.md`,
   `taxidriverconfessionals.md`, `selfiewithlocallegend.md`, `undergroundkaraokeleague.md`
   are 2-4 lines each and describe per-city content ("scattered across all cities", "each
   world's seedier corners"). They are latent `GENERAL-INSTANCED` quests with no master spec
   and no instances.
2. **`greatdonerdebate.md`** — 656 lines, instanced but undecomposed, with
   `## BASE GAME LOCATIONS` and `## SHAMSTERDAM DÖNER LOCATIONS` inline in one file.
3. **`mobile_optimization` sweep, ~26 world files** — genuine dead-branch debris, unlike the
   quest blocks. Spot-checked: `cafe_sachertorte_core.json` carries `lod_level`,
   `max_particles`, `draw_calls`, `memory_mb`; `cloverleaf_sprite_mapping.json` carries
   `"compression": "PVRTC_iOS_ETC2_Android"` — an iOS texture format on a Steam/desktop
   target. Needs re-budgeting, not renaming. Three of ~26 files inspected; the rest are
   assumed similar but unverified.
4. **Migrate the two colocated quest JSONs** to `game/assets/data/quests/`.
5. **`flags.json` schema ruling** — blocks flag registration in the sync skill.

---

## 9. Open items requiring author rulings

- `flags.json` schema. Blocks flag registration in the sync skill; the design docs' flag
  tables work without it.
- Whether `Tools/validate_data.py` should gain quest validation, and to what depth.
