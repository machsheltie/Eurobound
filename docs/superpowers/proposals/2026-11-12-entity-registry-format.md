# Proposal: entity registry format (for author OK)

Status: PROPOSAL. No registry file exists, no canon doc and no game code changed. `design/registry/` is not created. Origin: author ruling v45 `registry_create` ("Create it: an agent proposes a format for my OK"), after v44 `p_registry` = yes.

## 1. Purpose

**What it is.** One source of truth for names, ids, numbers and formulas that appear in more than one doc. Each entry names its canonical value, the ruling or `path:line` that fixed it, and every doc and engine file that restates it. The `consistency-check` skill greps the docs for each entry and flags any restatement that disagrees.

**What it is NOT.**
- Not engine data. `game/assets/data/` (items, enemies, status_effects, quests, locations) stays the runtime source. The registry stores only the cross-doc facts and points at the engine file.
- Not a content source. It never invents a value. An entry exists only after a ruling or an approved doc line. Unruled values are recorded as `pending: <ruling bead>`, never guessed.
- Not a ledger. The rulings ledger (`docs/superpowers/NEXT_WORK.md`) stays the authority; the registry is its index by entity.

**What already expects it** (all point at `design/registry/entities.yaml`, none can run today):
- `.claude/Skills/consistency-check/SKILL.md:13,42,229,238` (reads it, offers to fix stale entries)
- `.claude/Skills/design-system/SKILL.md:83,709-725` (greps `  - name: <candidate>`)
- `.claude/Skills/review-all-gdds/SKILL.md:67-70`
- `.claude/agents/systems-designer.md:81-94`, `.claude/agents/economy-designer.md:82-97`
- `docs/superpowers/NEXT_WORK.md:791` ("The registry may record these"); v43 proposal line 205.
- (`docs/registry/architecture.yaml` is a separate, ADR-only registry; out of scope.)

**Overlap with engine data to avoid.** `game/assets/data/skills/status_effects.json` already holds status definitions (Embarrassed there is partly "pending author"); `enemies/debaucheryville_enemies.json:171` holds `green_fairy_wisp`; `items/consumables.json` and `key_items.json` hold items (no Essence or Lager entry yet). Design docs indexed: `design/items/`, `design/worlds/*/`, `design/mechanics/Battle/status_effects.md`, `design/Quests/`, `design/worlds/*/*.json` sidecars. The registry holds the number once; engine JSON may carry it too, and the validator checks they match.

## 2. Format options

Entries below use only approved facts. `ledger` = `docs/superpowers/NEXT_WORK.md`.

### Option A: one YAML file, grouped by category (`design/registry/entities.yaml`)
```yaml
items:
  - name: Green Fairy Essence          # fits the skills' "  - name:" grep
    id: green_fairy_essence
    kind: consumable
    values: {desc: "a stoppered vial of green mist", confusion: guaranteed, bravado: 30}
    source: [desk q21, design/worlds/debaucheryville/the_absinthium_taproom.md:183]
    used_in: [the_absinthium_taproom.md:183, v43 proposal 1.3]   # engine: none yet (Wisp drop)
  - name: Cracked Mirror Shard
    id: cracked_mirror_shard
    kind: drop
    values: {dropped_by: Mirror Chad, drop_rate: 1.0}
    source: [the_absinthium_taproom.md:372, v43 proposal :72]
  - name: Absinthe Lager
    id: absinthe_lager
    kind: signature_beer
    values: {price_sovs: 12}
    source: [ledger:780]
    used_in: [the_absinthium_taproom.md:225, absinthium_taproom_interactions.json:86, location_nodes.json:30]
statuses:
  - {name: Embarrassed, id: embarrassed, kind: status, values: {field_duration_game_min: 60, battle_turns: 2, resistance_shortening: "10% per point"}, source: [ledger:782-785]}
formulas:
  - {name: Bartender discount, id: bartender_discount, kind: formula, values: {expr: "min(0.05 * cities_done, 0.20)"}, source: [ledger:788]}
```
Pros: one file, one grep, matches existing skill wording. Cons: grows to hundreds of entries; merge conflicts when many agents add entries.

### Option B: one YAML per category or city under `design/registry/`
```yaml
# design/registry/items.yaml            (also statuses.yaml, formulas.yaml, enemies.yaml)
# plus design/registry/_index.yaml: lists the files; skills read it first
- name: Absinthe Lager
  id: absinthe_lager
  kind: signature_beer
  city: debaucheryville
  values: {price_sovs: 12}
  source: [ledger:780]
  used_in: {docs: [the_absinthium_taproom.md:225], engine: [absinthium_taproom_interactions.json:86]}
# design/registry/formulas.yaml
- name: Bartender discount
  id: bartender_discount
  values: {expr: "min(0.05 * cities_done, 0.20)", cities_done: "int 0-4", max_discount: 0.20}
  source: [ledger:788, v44]
```
(Essence, Shard and Embarrassed look as in A, filed in `items.yaml`, `drops` and `statuses.yaml`.) Pros: small diffs, parallel agents rarely collide, a skill can load only what it needs. Cons: the skills' hardcoded path must be updated to a folder; cross-file ids need the validator.

### Option C: generated from the docs by a script
No hand-kept file. Docs carry a tagged line, and `tools/` builds `design/registry/entities.generated.yaml` (same schema as A). Example tag in the Taproom doc:
```markdown
- **Absinthe Lager** — 12 SOVS <!-- registry: absinthe_lager kind=signature_beer price_sovs=12 source=ledger:780 -->
```
Pros: cannot drift from the tagged doc line; follows the `canon_index build` pattern. Cons: tags must be added to every doc (touching canon docs under the "ask first" rule); only catches the doc that is tagged, not a restatement elsewhere; formulas and ruling-only facts (Bartender discount lives only in the ledger) need a tagged ledger line anyway.

## 3. How it stays true
- **Who/when.** The agent applying a ruling adds or edits the entry in the same change, citing the ruling id. An engine sync (new row in `game/assets/data/`) adds the engine path to `used_in`. Entries are written only after the author's OK (existing "May I add these?" protocol). New cross-system entities are flagged at session end, per the agent files.
- **Consistency check.** The skill reads the registry, greps each `name`/`id` across `design/`, and reports any value that differs from `values`, with `path:line`. The registry wins only if it cites a ruling; otherwise the conflict goes to the author.
- **Validator idea** (extend `tools/validate_data.py`, which already carries tests in `tools/tests/`): (1) schema check, every entry has id, name, kind, values, source; (2) ids and names unique across the game; (3) each `source` `path:line` still contains the registered value; (4) each `used_in` engine file parses and holds the same number; (5) report entries with no `used_in`, and registered names no doc mentions. Run `canon_index build` afterwards so searches find the registry.

## 4. Questions for the author
1. **Format:** (a) A, one YAML (recommended: matches the skills as written, small today); (b) B, YAML per category; (c) C, generated from doc tags; (d) other.
2. **File type:** (a) YAML (recommended: comments allowed, skills expect it); (b) JSON (matches `game/` data and `validate_data.py`).
3. **Who maintains it:** (a) the agent applying each ruling, with your OK per batch (recommended); (b) a periodic agent sweep that proposes entries; (c) script-only (needs option C).
4. **First entries:** register only the five above (recommended), or also the Keychain facts at ledger:786-790 (Tier B, Party Prep +1 Bravado per city, 16 openers / 16 breweries)?
