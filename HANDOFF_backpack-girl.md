# HANDOFF — worktree `backpack-girl`

| | |
|---|---|
| **Worktree name** | **`backpack-girl`** |
| **Branch** | **`wt/backpack-girl`** |
| **Local path** | `.worktrees/backpack-girl` |
| **Owns** | NPC profiles · character-design canon · Couchsurfing Chronicles · PNG asset specs |
| **Base commit** | `d20ddd3` (main) |
| **Written** | 2026-08-06 |

> **This window is one of several.** Sibling worktrees `hot-kroger-guy` and `nft-vault-copy` are other agent windows with their own handoffs. Do not touch files outside the scope below without checking with the author — you will collide with another window.

---

## 🚨 READ THESE FIRST — IN THIS ORDER

Do not write a single line of content before reading all four. Every one of them exists because an agent drifted and the author had to correct it.

1. **`CLAUDE.md`** — non-negotiable content rules.
2. **`design/reference/earthbound_character_design.md`** — the creative north star. **There are no average characters in this game.**
3. **`design/characters/bros_core_principle.md`** — what actually breaks the bros: their aging bodies and the women. Not fear, not disgust.
4. **`design/Synopsis.md`** — the premise.

### The tone failures that keep happening

The author has had to issue this correction **four separate times**. Read it carefully:

> *"Quit trying to fucking turn my game into something it's not. It's not safe. It's not boring. It's not corporate. It IS subversive."*
>
> *"There is no fucking terror. The whole thing is supposed to be ridiculous satire. Not mundane. Not bored. Not professionals. Quit trying to make to fucking safe."*
>
> *"The bros fucking went to Europe seeking out debauchery. They went there FOR the sex, drugs, drinking, partying, whores, sex clubs, etc. They aren't innocent tourists. They aren't afraid."*

**What breaks the bros** (author, verbatim):

> *"What breaks them is their aging bodies and the women. Because they think they're still as good as college age men... their stomachs can't handle the constant eating of greasy fatty foods, their bodies can't keep up with the all night drugs, drinking and partying and their bodies can't hold up to the onslaught of STDs. They think they can still pull beautiful younger women and instead often get turned down for younger hotter models."*

**Concretely, do NOT:**

- Write workers or staff as the sober, competent, unbothered anchor. **There is no straight man. Everyone is ridiculous.**
- Write the bros as afraid, disgusted, self-aware, or scam-aware.
- Reach for bureaucracy, queue management, customer service, or anticlimax as the joke.
- Sanitize, soften, or explain a joke. No narrator, no wink, no moral framing.

The only content ceiling is **no nudity**. Everything else is in-bounds.

---

## ✅ STATE — what is DONE (do not redo)

| Area | State |
|---|---|
| PNG asset specs | **87 files**, all meeting the 14-section template minimum |
| Name de-duplication | Applied repo-wide. Rule: **one first name = one character** |
| Currency | **Sovs everywhere.** ~4,215 euro symbols removed. No glyph, no subunit, **1-Sov floor** |
| City order canon | `design/worlds/city_progression_order.md` |
| Couchsurf four-state routing | `design/quests/general_quests/couchsurfingchronicles.md` |
| EarthBound north star | `design/reference/earthbound_character_design.md`, wired into both templates |
| Couchsurf rosters (Publandia + Shamsterdam) | **Rewritten with purpose-built hosts.** 10 personas, 4 states each |

### Settled canon — DO NOT RELITIGATE

- **Play order:** Publandia → Debaucheryville → Sinfonia → Shamsterdam. **Backtracking is supported.** All four couchsurf states are reachable in every city. Nobody is assumed clean, and there is no fixed order for reaching couchsurf hosts.
- **All money is SOVS.** Never euros, never the € glyph, never koruna. Prose `40 Sovs`, signage `40 SOVS`. **Nothing below 1 Sov ever changes hands** — no change, no coins. The Shadow Exchange is the only exception.
- **The Herp** is the game's one and only STD, and it is **optional** — a sidequest. The player can skip the party and never get it. It is *suppressed*, never *cured*, by the Gold Circle Coin. A permanently-infected playthrough is a valid, intentional path.
- **Couchsurf hosts are purpose-built parody characters.** They are NOT converted city staff. Ten named staff are permanently barred from being hosts — the bar lists are in the two roster files. Never re-add them.
- **No mascots, ever.** No pets, puppets, companions, or fourth party member. The party is three bros.
- **No real city names** in player-facing text. Parody names only.
- **No `SATIRE_MODE`, `line_safe`, or any safe-build mechanism.** Ever.

---

## 🔨 OPEN WORK — in priority order

### 1. NPC profiles (the big one)

Current counts: Publandia 17 · Debaucheryville 47 · Sinfonia 25 · Shamsterdam 17.
Wave 1 (48 primary) is done. **Waves 2 and 3 remain: roughly 75 named secondary and 50 named ambient.**

**Every profile must pass the EarthBound test before you write it.** Copy `design/templates/NPC_Profile_Template.md` — it now opens with a READ FIRST block and carries three EarthBound rows in its validation checklist.

> Could this character sit in EarthBound's cast next to Miss Morphine and Backpack Girl Who Never Left, without looking like they wandered in from a census?

**Invent the persona first, then check the name is unused.** Never the reverse — the naming registry must not push you toward bland names. "Aoife Brennan, 34, runs a pottery studio" is a failure. "Perpetual Bride Bláthnaid — The Ninth Annual" is the standard.

### 2. Three Sinfonia couchsurf hosts need full NPC profiles

**The Understudy · The Eternal Student · Lady Geheimnis.** Build them *from* their existing Chronicles blocks in `design/quests/sinfonia/couchsurfingchroniclessinfonia.md` — do not reinvent them.

### 3. NPC ID normalization

Canonical scheme: `<city>_npc_<name>_01`. The audit shows **69 canonical** IDs against a large non-canonical tail (`token_goblin`, `velvet_curtain_bouncer`, `sean_murphy_exit_01`, and others). Normalize across the 15 `*_npcs.json` files.

**Exception:** group and crowd entries legitimately keep descriptive IDs — do not force those.

### 4. Venustempel NPCs are unregistered

`design/worlds/shamsterdam/npcs/Venustempel/` holds `npc_gunter.md` and `npc_lotte_beekman.md`, but **there is no `venustempel_npcs.json`**. Gunter, Lotte, Anke, Ruud and Gerda are registered nowhere. Create the JSON and register all five.

### 5. `gold` → Sovs in GDScript

6 `.gd` files still reference `gold`. This is a **code** refactor — save serialisation plus test assertions. Run the GUT suite afterwards (`addons/gut`, tests in `tests/unit/`).

### 6. Conflict callouts

4 unresolved `⚠ CONFLICT` markers in `club_flyers.md`, left over from an earlier merge.

---

## ⚠️ HAZARDS — these have already cost real time

| Hazard | Rule |
|---|---|
| **PowerShell array unrolling** | `@(@('a','b'))` **flattens**. This turned rename pairs into single-character global substitutions and corrupted 8 files. **Never use nested-array rename pairs in PowerShell.** |
| **cp1252 console encoding** | Printing non-ASCII (`≤`, `→`, diacritics) to stdout raises `UnicodeEncodeError` and kills the script **before it writes anything**. Keep stdout pure ASCII. |
| **Unquoted paths** | Paths contain spaces. Always quote them. An unquoted loop once produced false "INVALID" results across the whole JSON set. |
| **Diacritics** | Roughly 2,374 in the tree (`Bláthnaid`, `Dvořák`, `Riviéra`). Verify the count is unchanged before and after any sweep. |
| **Character corruption** | One file previously had every capital `E`→`m` and `V`→`i`. If words look subtly wrong, compare byte counts against `HEAD`. |
| **Do not trust agent reports** | Verify sub-agent claims against the actual files. Reports have been confidently wrong. |

**Always verify before claiming done.** Run the check and show the output. `Tools/validate_data.py` validates the JSON set.

---

## 📐 Author protocol

**Requires an author ruling before doing:** story, lore, or satire changes · mechanics · stat or economy numbers · quest structure · any new content (NPCs, locations, items, quests).

**Ambiguity escalates. It is never resolved by invention.** A previous agent invented an entire plot without asking; it was struck in full.

**Proceed freely:** bug fixes, refactors, tests, doc formatting.

Standing rulings ledger: `docs/superpowers/NEXT_WORK.md`.
Dead branch — never revive, never merge, never treat as canon: `claude/eurobound-jrpg-prd-uv5iog`.

---

## 🎯 The bar for new characters

The ten couchsurf hosts just authored, as the reference standard:

**Publandia** — Perpetual Bride Bláthnaid, who has held her cancelled wedding reception annually for nine years and lives behind the buffet screen · Madam Secretary Doireann, 1,411 meetings of a literary society and zero books ever read · Archdruidess Fidelma of the Damp Spoon · Commandant Neasa, under siege by drizzle for 41 days, whose flat is nine minutes away · "One Sixty-Fourth" Treasa, conducting reverse heritage tourism at professional standard

**Shamsterdam** — Magnet Machteld, 14,091 items catalogued, never kept one, never found the thing she is looking for · Tourmistress Willemijn, ticketed walking tour of her own eleven exes' doorways, and she lives at Stop Six · The Not-Girlfriends, Sietske and Renske, eleven years not-together across eleven metres of canal, cat commuting by rope-and-pulley · Captain Noortje, canal cruises on a boat with no engine, logbook of 4,011 entries all reading `MOORED. FINE.` · Rikst Who Does Not Dismount, 22 years without putting a foot down

Each also has **one inexplicable rule she will not bend, which is never explained** — no umbrellas · don't mention the book · the tour never crosses a bridge · life jackets below decks on a moored boat.

That is the floor, not the ceiling.
