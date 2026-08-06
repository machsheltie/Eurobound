---
name: eurobound-item-creation
description: "Creates any new Eurobound item — permanent items, weapons, equipment, consumables, key items, quest items, brewery beers, bottle openers, passport stamps. Use whenever the user asks to create, add, write, design, or spec a new item for Eurobound, and whenever an autonomous run determines a new item is needed. This skill owns the whole path: it loads the project's satire rules before writing so the content does not come out sanitized, interviews the author instead of inventing item identity, picks the correct template from design/templates/, and files the finished doc into the correct city or general items folder. Do not write an Eurobound item doc freehand — the folder routing and template skeleton are load-bearing for downstream tooling."
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
