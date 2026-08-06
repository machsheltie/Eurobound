---
name: eurobound-item-engine-sync
description: "Registers a finished Eurobound item design doc into the engine item data under game/assets/data/items/. Invoked automatically as the final step of the eurobound-item-creation skill, and usable standalone against any existing item .md that has no engine entry yet. Picks the right JSON file from the item's type, writes the entry keyed by item ID, preserves the item's voice in its description rather than flattening it, and runs the data validator. Refuses to invent a schema for the two JSON files that are still empty — it asks the author instead."
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

**Brewery items have no Item Identity block.** If the filename starts `beer_`,
`opener_`, or `stamp_`, the doc uses the brewery templates' flat shape instead:

- Display Name: the part of the H1 after the colon (e.g. `# Signature Beer: The
  Fool's Gold` → `The Fool's Gold`)
- Item ID: the `**Item ID**` bullet
- Item Type: there is no such field. Do not invent one — see Step 2.

If the doc still contains unfilled `[bracketed placeholders]`, stop. Report which
ones, and send it back to the item author. Do not sync an unfinished doc.

## Step 2 — Pick the target file

| Item Type | Target |
|---|---|
| Consumable — food, drink, drugs, anything used up | `game/assets/data/items/consumables.json` |
| Equippable, swappable through a slot | `game/assets/data/items/equipment.json` |
| Permanent, curse, or quest item | `game/assets/data/items/key_items.json` |
| Hybrid (both cosmetic and mechanical aspects) | **ask the author** which target applies |

If the type does not map cleanly to one of the three fixed rows, stop and ask the
author. Do not force a fit.

**Brewery items have no Item Type, so the target file cannot be derived from the
table above.** Ask the author which target file a given beer, opener, or stamp
belongs in before writing anything. This is a mechanics decision — which JSON an
item's effects live in — and per `CLAUDE.md` that requires an author ruling. Do
not decide the mapping yourself, and do not write a mapping into this skill.

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

**`equipment.json` and `key_items.json` are both still empty.** This skill **does not invent** a schema for either one. The first time an item routes to one of them:

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

Run: `python Tools/validate_data.py` (capital `T` — this is the tracked path;
lowercase `tools/` only resolves on case-insensitive filesystems).

Report the actual output, pass or fail. If it fails, fix the entry and re-run. Never
report success without the validator's output in hand.

**Known pre-existing bug:** `Tools/validate_data.py` points `ROOT` at
`Assets/Data`, but the data actually lives at `game/assets/data/`. Because of this,
the validator currently prints 7 `MISSING` lines every run and never reaches the
item JSONs at all — this happens regardless of what you wrote. Those 7 lines are
the pre-existing failure, not something your entry caused. Do not try to "fix the
entry" in response to them; there is nothing in the entry to fix. Report them as
the known bug they are and move on. Do not edit `Tools/validate_data.py` — that
fix is awaiting its own author ruling.

## Refusal conditions

Stop and report rather than proceeding when:

- The item ID already exists in any of the three JSON files
- The source doc still has unfilled `[bracketed placeholders]`
- The Item Type does not map cleanly to one of the three targets
- Writing the entry would require inventing a schema that has not been ruled on
