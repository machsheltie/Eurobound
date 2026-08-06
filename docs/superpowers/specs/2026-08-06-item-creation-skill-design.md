# Item Creation Skill — Design

**Date:** 2026-08-06
**Status:** Approved (author, 2026-08-06)
**Scope:** Two chained project skills governing how new Eurobound items are authored and registered.

---

## 1. Problem

Item creation today has no enforced path. Four item templates exist in `design/templates/`,
five destination folders exist under `design/items/` and are all empty, and engine item JSON
lives separately under `game/assets/data/items/`. Nothing connects them.

Two failure modes result:

1. **Wrong shape or wrong place.** An item gets written freehand, or dropped loose in
   `design/items/` instead of the city/general folder that should own it.
2. **Sanitization drift.** Absent a forced re-read of the project's satire rules, generated
   item text softens: hedged jokes, moralizing asides, bros who become self-aware or
   disgusted. `CLAUDE.md` classes this as a defect of the highest severity.

The skills below close both.

---

## 2. Architecture

Two skills, chained by handoff.

```
eurobound-item-creation  --(final checklist item)-->  eurobound-item-engine-sync
   interview -> template -> route -> write .md           read .md -> write JSON -> validate
```

`eurobound-item-engine-sync` is also invocable standalone against any existing item doc,
which is why it is a separate skill rather than a second phase of the first.

"Trigger on completion" means the creation skill's last mandatory checklist item is to invoke
the sync skill. It is not an OS-level or hook-level event. This is a hard step, not a suggestion.

Both skills live in `.claude/Skills/`.

---

## 3. Skill 1 — `eurobound-item-creation`

### 3.1 Triggers

Any request to create or add a new item, weapon, equipment, consumable, key item, or permanent
item for Eurobound. Also fires on autonomous runs that determine a new item is needed.

### 3.2 Mandatory pre-load

Before writing any content, in this order:

1. `CLAUDE.md` — content rules, SOVS-only currency, no real place names, uniqueness requirement
2. `design/narrative/Synopsis.md` — premise, the three bros, the world
3. The `eurobound-satire-voice` skill — read **in full**, not just the opening section

This ordering is the anti-sanitization guard. The skill restates the non-negotiables inline so
they are present in context at write time:

- This is an MA game for adults. Satire ships at full strength or not at all.
- No narrator, disclaimer, moral framing, or any device that explains the joke.
- The only ceiling is no nudity. Sex, sex workers, drugs, drinking, red-light districts,
  and hookups are in-bounds and core to the premise.
- The bros are never afraid, disgusted, self-aware, or scam-aware. They came to Europe for this.
- NPCs are never boring, corporate, or professional.
- Tone reference is EarthBound: sincere delivery of absurd material. Sincerity is the joke.

### 3.3 Author interview

The skill never invents item identity. It interviews the author and waits for answers on:

- What the item is and what it is for
- Which bro, city, NPC, quest, or location it attaches to
- The mundane reality vs. what the bros believe it is (the deception, per the template)
- Price and value, in SOVS
- How it is acquired: purchased, earned, found, quest reward

Ambiguity escalates. It is never resolved by invention. This holds on autonomous runs: if a
question is open, the skill asks rather than guessing.

### 3.4 Template selection

| Item is… | Template |
|---|---|
| Brewery signature beer | `design/templates/signature_beer_item_template.md` |
| Brewery bottle opener | `design/templates/opener_item_template.md` |
| Brewery passport stamp | `design/templates/stamp_item_template.md` |
| Everything else | `design/templates/permanent_item_template.md` |

`permanent_item_template.md` is the default. The three brewery templates are used only for
those specific item classes, matching the 36 existing files in `design/items/brewery_tour/`.

All H2 section headers (with emoji) and table column shapes are preserved exactly as they
appear in the template. The permanent template states that downstream tooling depends on
this skeleton matching. The instructional HTML comment block is deleted from the finished doc.

Optional template subsections (per-character variants, distinction-from-equipment) are
included when applicable and omitted otherwise, per the template's own instructions.

### 3.5 Routing

| Item is… | Destination |
|---|---|
| Found everywhere / not tied to one city | `design/items/general_items/` |
| Tied to Publandia | `design/items/publandia_items/` |
| Tied to Debaucheryville | `design/items/debaucheryville_items/` |
| Tied to Sinfonia | `design/items/sinfonia_items/` |
| Tied to Shamsterdam | `design/items/shamsterdam_items/` |
| Brewery beer / opener / stamp | `design/items/brewery_tour/` |

Decision test, applied in order:

1. Is it a brewery beer, opener, or stamp? → `brewery_tour/`. Done.
2. Is its source — the NPC, shop, quest, or location that provides it — in exactly one city?
   → that city's folder.
3. Is it sold by a generic vendor type, dropped by common enemies, or obtainable in two or
   more cities? → `general_items/`.
4. Still unclear? → **ask the author.** Never guess the folder.

### 3.6 File naming

snake_case, no spaces, matching existing convention:

- Standard items: `<item_name>_item.md` (e.g. `vip_wristband_item.md`, `candy_smokes_item.md`)
- Brewery items keep their prefixes: `beer_<brewery_slug>_item.md`,
  `opener_<brewery_slug>_item.md`, `stamp_<brewery_slug>_item.md`
- Item ID inside the doc: `item_<item_name_snake_case>`, or the brewery prefix form

### 3.7 Pre-write blocking checks

Both stop the skill and return to the author on failure:

- **Uniqueness.** Grep the repo for the display name and the item ID. `CLAUDE.md` requires all
  names unique across the game — NPCs, locations, items, quests, everything. A collision is a
  stop, not a rename-and-continue.
- **Currency.** Every price is SOVS. No euro glyph, no "euros", no "koruna". This supersedes
  the euro-as-display-glyph rule in the Round 5 economy spec §1.2.

### 3.8 Post-write verification

Confirmed with evidence, not assertion:

- File exists at the correct routed path
- No `[bracketed placeholder]` text remains
- No euro glyph, "euro", or "koruna" anywhere in the file
- Display name and item ID are unique across the repo
- All template H2 headers present and intact
- Instructional comment block removed

### 3.9 Self-critique handoff

After verification passes and before the engine sync, the skill invokes
`eurobound-adversarial-critic` against the new file. That skill hunts specifically for
sanitization — pulled punches, moralizing, hedges, softened jokes — and for rule violations.
Findings are surfaced to the author. This is the second line of defense against the softening
instinct the satire-voice skill exists to override.

### 3.10 Final step

Invoke `eurobound-item-engine-sync`, passing the path to the finished doc. Mandatory.

---

## 4. Skill 2 — `eurobound-item-engine-sync`

### 4.1 Triggers

Invoked by the final checklist item of `eurobound-item-creation`. Also invocable standalone
against any existing item `.md`.

### 4.2 Input

Path to a finished item design doc.

### 4.3 Process

1. Read the doc's Item Identity block: Item ID, Display Name, Item Type.
2. Select the target file by type:

   | Item Type | Target |
   |---|---|
   | Consumable — food, drink, drugs, anything used up | `game/assets/data/items/consumables.json` |
   | Equippable, swappable through a slot | `game/assets/data/items/equipment.json` |
   | Permanent, curse, or quest item | `game/assets/data/items/key_items.json` |

3. Add the entry keyed by item ID, matching the file's existing shape.
4. `description` is lifted from the item doc's voice. It is not rewritten into flat,
   functional prose. SOVS only.
5. Run `python tools/validate_data.py` and report the actual output, pass or fail.

### 4.4 Schema state

`consumables.json` has an established shape: `display_name`, `heal_hp`, `heal_sp`, `description`.

`equipment.json` and `key_items.json` are both empty (`{}`) as of 2026-08-06. **The skill does
not invent a schema for either.** The first time an item routes to one of them, the skill
presents a proposed entry shape and waits for an author ruling. Once ruled, that shape is
followed from then on and the ruling is recorded in `docs/superpowers/NEXT_WORK.md`.

### 4.5 Refusal conditions

The skill stops and reports rather than proceeding when:

- The item ID already exists in any of the three JSON files
- The source doc still contains unfilled `[bracketed placeholders]`
- The doc's Item Type does not map cleanly to one of the three targets

---

## 5. Non-goals

Explicitly out of scope:

- Sorting or relocating the 12 legacy loose `*_item.md` files in `design/items/`. The skill
  governs the item it is currently creating and nothing else.
- PNG asset specs. Item docs may reference them; the skill does not author them.
- Quests, NPCs, or locations the item references. Those need their own author rulings and
  their own templates.
- The per-location item JSONs under `design/worlds/<city>/items/`. Unrelated system.

---

## 6. Author rulings captured

Recorded 2026-08-06 during design:

1. **Template selection:** permanent by default; brewery beer/opener/stamp route to their
   specialized templates and to `design/items/brewery_tour/`.
2. **Author gate:** the skill interviews the author rather than drafting unratified content.
   It must load `CLAUDE.md`, `design/narrative/Synopsis.md`, and `eurobound-satire-voice` before writing,
   because the model's default instinct is to sanitize.
3. **Legacy files:** not sorted. New items only.
4. **Engine JSON:** handled by a second skill chained off the first, not inline.
