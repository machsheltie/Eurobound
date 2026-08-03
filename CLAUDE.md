# CLAUDE.md — Eurobound

Eurobound is a satirical, EarthBound-style JRPG built in **Godot 4.4**, targeting **Steam/desktop**. Three aging frat bros — Lord Pilsner, Chadwick, and Bradley — take one last bender across a parody Europe soaked in 90s/early-2000s pop culture. Read `Design/Synopsis.md` before writing or editing any game content.

## Content rules (non-negotiable)

- **This is an MA game for adults. Satire ships at full strength or not at all.** Sanitizing, softening, de-subversifying, or over-explaining any content is a defect of the highest severity.
- **No narrator, disclaimer, moral framing, or any device that explains the satire or the jokes.** The game never winks at the player and never undercuts the delusion — sincerity is the joke (Trust the Player).
- **The only content ceiling is no nudity. Beyond that, anything goes.** Sex (happens, never shown), sex workers, drugs, drinking, late-night partying, red-light districts, and hookups are in-bounds and core to the premise. No rating-driven ceiling exists, and no safe-build mechanism (`SATIRE_MODE`, `line_safe`, string swaps, or anything like them) may ever be created.
- **The bros are never afraid or disgusted.** They came to Europe seeking all of this. They may be clueless; they are never scared. They are also never self-aware or scam-aware.
- **NPCs are never boring, corporate, or professional.** Every NPC, location, and item gets a funny name and is written cleverly, with wit, in service of satirizing and parodying everything.
- **No real city or place names in game content.** Parody names only: Publandia, Debaucheryville, Sinfonia, Shamsterdam. Internal planning docs may reference the real-world inspirations; player-facing text never does. Minted world-name canon and exemptions live in the rulings ledger (below).
- **All money is SOVS.** Never euros, never the € glyph, never koruna. Write prices as SOVS (e.g. "40 SOVS"). This supersedes the €-as-display-glyph rule in the Round 5 economy spec §1.2.
- **No mascots, ever.** No pets, puppets, named companion objects, emotional-support entities, or fourth party members. The party is three bros.
- **All names must be unique** across the game — NPCs, locations, items, quests, everything.
- **All side quests are optional.**
- NFT artwork is 90s/00s pop culture, never location-derived.

## Templates are mandatory

Creating a new NPC, location, NFT, item, PNG asset spec, or side quest doc? **Copy the matching template from `/Templates`** — `NPC_Profile_Template.md`, `location_validation_template.md`, `NFT_Template.md`, `permanent_item_template.md`, `PNG_Assets_Template.md`, `sidequest_template.md` (short form: `quest.md`). Templates are floors, not ceilings. If no template fits, ask the author before inventing a format.

`/Templates` is the only canonical template folder (it moves to `design/templates/` when the folder restructure completes). Template copies elsewhere (e.g. `Design/Character Profiles/Templates/`) are legacy — do not use them.

## Ask the author first

- **The story belongs to the author alone.** No agent writes, extends, or reshapes the game's story, plot, hook, act structure, or endings on its own — the author dictates direction and the writing happens with them, decision by decision. (A previous agent invented an entire plot without asking; it was struck in full. Do not repeat this.)
- **Requires an author ruling before doing:** story, lore, or satire changes; adding or changing mechanics; stat or economy numbers; quest structure; any new content (NPCs, locations, items, quests). Present the decision, interview the author if information is missing, and wait. **Ambiguity escalates — it is never resolved by invention.**
- **Proceed freely:** bug fixes, refactors, tests, doc formatting.

## Canon and standing rulings

- Standing rulings ledger: `docs/superpowers/NEXT_WORK.md` and the binding rules in `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` §0a. **Do not relitigate settled rulings.**
- The branch `claude/eurobound-jrpg-prd-uv5iog` (EUROBOUND_PRD.md; 16+ ceiling, euro currency, `line_safe` columns, mobile-first) is **dead and superseded**. Never treat it as canon, never merge it, never revive its rules.
- Older docs (README, GAMEPLAN, Designer Persona) describing a mobile-first iOS game are stale on platform: the target is Steam/desktop.

## Repo notes

- A folder restructure is in flight on `chore/folder-restructure` (target layout: `game/`, `design/`, `marketing/`, `production/`, `tools/`, `docs/`; spec: `docs/superpowers/specs/2026-07-31-folder-restructure-design.md`). `_sorting/` on that branch is the author's staging area — never touch it. After the restructure merges, refresh paths in this file.
- Tests: GUT (`addons/gut`), unit tests in `tests/unit/`. Data validation: `Tools/validate_data.py`.
- New files and folders: snake_case, no spaces (per the restructure spec). Match existing conventions when editing.
