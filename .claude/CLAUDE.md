# CLAUDE.md — Eurobound

Eurobound is a satirical, EarthBound-style JRPG built in **Godot 4.7 (Forward+ renderer)**, targeting **Steam/desktop**. Visual style is a 2.5D HD-2D hybrid (2D sprites in painterly 3D dioramas) in the vein of Star Ocean: The Second Story and Bravely Default 1 and 2. Three aging frat bros — Lord Pilsner, Chadwick, and Bradley — take one last bender across a parody Europe soaked in 90s/early-2000s pop culture. Read `design/narrative/Synopsis.md` before writing or editing any game content.

## Content rules (non-negotiable)

- **This is an MA game for adults. Satire ships at full strength or not at all.** Sanitizing, softening, de-subversifying, or over-explaining any content is a defect of the highest severity.
- **No narrator, disclaimer, moral framing, or any device that explains the satire or the jokes.** The game never winks at the player and never undercuts the delusion — sincerity is the joke (Trust the Player).
- **The only content ceiling is no nudity. Beyond that, anything goes.** Sex (happens, never shown), sex workers, drugs, drinking, late-night partying, red-light districts, and hookups are in-bounds and core to the premise. No rating-driven ceiling exists, and no safe-build mechanism (`SATIRE_MODE`, `line_safe`, string swaps, or anything like them) may ever be created.
- **The bros are never afraid or disgusted.** They came to Europe seeking all of this. They may be clueless; they are never scared. They are also never self-aware or scam-aware.
- **NPCs are never boring, corporate, or professional.** Every NPC, location, and item gets a funny name and is written cleverly, with wit, in service of satirizing and parodying everything.
- **No real city or place names in game content.** Parody names only: Publandia, Debaucheryville, Sinfonia, Shamsterdam. Internal planning docs may reference the real-world inspirations; player-facing text never does. Minted world-name canon and exemptions live in the rulings ledger (below).
- **No Dutch names in Shamsterdam** (author, 2026-11-13): "We do not use official looking names in dutch. We use american names and they should be whitty, clever, satirical, parody type names that are fully americanized and lean heavily into what each location is." Funny, not highbrow. The existing Dutch names are being replaced via the Eurobound Desk (bead Eurobound-ucpf); never mint a new one.
- **Real brands, products, games, songs and titles keep their real names** (author, 2026-11-09: "The only thing that never gets the real name is locations. ALL other things get their real names."). Invented NPCs, items and quests still get funny names.
- **All money is SOVS.** Never euros, never the € glyph, never koruna. Write prices as SOVS (e.g. "40 SOVS"); the singular is "1 SOV" (author, 2026-11-10). This supersedes the €-as-display-glyph rule in the Round 5 economy spec §1.2.
- **No mascots, ever.** No pets, puppets, named companion objects, emotional-support entities, or fourth party members. The party is three bros. (Ambient set-dressing animals the author rules in, like the Absinthe Arcade window cat, are ledger exceptions.)
- **All names must be unique** across the game — NPCs, locations, items, quests, everything.
- **All side quests are optional.**
- NFT artwork is 90s/00s pop culture, never location-derived.
- **Junk items pay off when inspected** (author, 2026-11-11): "little bit items like that that seem to be junk reward the player for investigating them and that they should come with really funny microcopy." Keep it short, and "It can go as dark comedy, dirty, and unfamily friendly as it likes as this is an MA game."
- **Drinking, drugs and sex follow two standing author laws:** `design/narrative/bros_choose_debauchery.md` (the bros are willing, delusional antiheroes; no intoxicant gives a free advantage; no moral lectures) and `design/mechanics/intoxication_law.md` (alcohol escalates Buzzed → Beer Goggles → Shitfaced → Catastrophe; bounded loss of player control is a legitimate mechanic; run its 10-point design review before adding any intoxication mechanic).

## Templates are mandatory

Creating a new NPC, villain, location, NFT, item, enemy, status effect, PNG asset spec, or side quest doc? **Copy the matching template from `design/templates/`**:
- **Characters:** `NPC_Profile_Template.md`; `villain_template.md` (every villain gets one at creation — author mandate); `enemy_template.md` (regular enemies); `couchsurf_host_template.md`.
- **Places:** `city_overview_template.md`; `location_validation_template.md`.
- **Items:** `permanent_item_template.md` (permanently held by a bro); `consumable_item_template.md` (food, drinks, drugs, vapes); `equipment_template.md`; `signature_beer_item_template.md`; `opener_item_template.md`; `stamp_item_template.md`; `NFT_Template.md`.
- **Systems:** `ability_template.md`; `status_effect_template.md`.
- **Quests:** `sidequest_template.md` (the only quest template — the old `quest.md` short form is retired, its unique sections merged in).
- **Art:** `PNG_Assets_Template.md`; `3D_Asset_Manifest_Template.md` (one per 3D building kit).

Templates are floors, not ceilings. If no template fits, ask the author before inventing a format.

`design/templates/` is the only canonical template folder. Retired copies live in `design/legacy/retired_templates/` (author, 2026-11-11). Do not use them.

## 3D assets

**3D work** (any building, prop, or decal modeled for the game; Tripo, Blender, meshes, materials): read `design/style_guides/3d_asset_rules.md` before starting. It is binding: references are canon, architecture passes a gray clay review before ornament, the author hand-paints all distress, and agents drive the tools themselves.

## Ask the author first

- **The story belongs to the author alone.** No agent writes, extends, or reshapes the game's story, plot, hook, act structure, or endings on its own — the author dictates direction and the writing happens with them, decision by decision. (A previous agent invented an entire plot without asking; it was struck in full. Do not repeat this.)
- **Requires an author ruling before doing:** story, lore, or satire changes; adding or changing mechanics; stat or economy numbers; quest structure; any new content (NPCs, locations, items, quests). Present the decision, interview the author if information is missing, and wait. **Ambiguity escalates — it is never resolved by invention.**
- **Proceed freely:** bug fixes, refactors, tests, doc formatting.

## Canon and standing rulings

- Standing rulings ledger: `docs/superpowers/NEXT_WORK.md` and the binding rules in `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` §0a. **Do not relitigate settled rulings.**
- **Search canon before writing, deciding or asking:** `tools/canon_index/.venv/Scripts/python tools/canon_index/canon_index.py search "<subject>"` (add `--rulings` for the ledger only). It returns `path:line` hits across `design/` and the ledger; read those lines instead of whole files. Run `build` after editing design docs. See `tools/canon_index/README.md`.
- **Work tracking is beads (`bd`):** open tasks, blockers and items waiting on author rulings live there (`bd ready`, `bd list`). Rules for this repo are in the root `CLAUDE.md`.
- The branch `claude/eurobound-jrpg-prd-uv5iog` (EUROBOUND_PRD.md; 16+ ceiling, euro currency, `line_safe` columns, mobile-first) is **dead and superseded**. Never treat it as canon, never merge it, never revive its rules.
- Older docs (README, GAMEPLAN, Designer Persona) describing a mobile-first iOS game are stale on platform: the target is Steam/desktop.

## Repo notes

- A folder restructure is in flight on `chore/folder-restructure` (target layout: `game/`, `design/`, `marketing/`, `production/`, `tools/`, `docs/`; spec: `docs/superpowers/specs/2026-07-31-folder-restructure-design.md`). `_sorting/` on that branch is the author's staging area — never touch it. After the restructure merges, refresh paths in this file.
- Godot project lives in `game/`. Tests: GUT (`game/addons/gut`), tests in `game/tests/`. Data validation: `tools/validate_data.py`.
- Installed addons: Dialogue Manager, Phantom Camera, LimboAI, NoClipBillboardSprite3D, Aseprite Wizard, GUT, Godot MCP Pro (`.mcp.json` → `tools/godot_mcp_pro_server`, port 6505; open the editor to connect; paid licence, both its folders are gitignored, reinstall from the purchase zip). Runtime tools (screenshots, input) need `play_scene` first. Tilt-shift post shader: `game/shaders/post/tilt_shift_layer.tscn`.
- Image cleanup for generated art: `tools/art_cleanup/` (see its README).
- **Character sprites** follow `design/style_guides/character_sprite_pipeline.md`. Author ruling 2026-11-12: every character, bros included, is made with Tripo (3D model) + Blender ("It just looks so much better than the crap trash we've been producing with pixel art"); the old Firefly -> PixelLab -> Aseprite pixel pipeline is superseded. Open details (final look, redoing existing sprites, credit budget, animation, order) are pending on the Eurobound Desk; don't start new PixelLab character work.
- New files and folders: snake_case, no spaces (per the restructure spec). Match existing conventions when editing.
