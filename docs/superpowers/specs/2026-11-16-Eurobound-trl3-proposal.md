# Regional reputation doc vs later rulings: keep / change / cut

**Status:** PROPOSED. Nothing here is canon until the author rules on Eurobound Desk card `Eurobound-trl3-q2`.
**Bead:** Eurobound-trl3. **Date:** 2026-11-16.
**Author's instruction (Desk, 2026-11-16):** "An agent checks the doc against your later rulings and brings me a keep / change / cut list".
**Doc checked:** `design/mechanics/Social/socialmechanicsandreputationsystem.md` (251 lines), plus `design/game_design_document.md:262` (Street Rep).
**Rule:** a verdict appears only where a ruling applies. Where none does it says "no ruling: author's call" and nothing is decided. Ledger = `docs/superpowers/NEXT_WORK.md`. CC = `.claude/CLAUDE.md`. BCD = `design/narrative/bros_choose_debauchery.md`.

## Facts first

- Nothing in the doc is in the ledger as approved. The only reputation ruling is that the game menu shows no Street Rep (ledger :707).
- No code exists (no `reputation`, `street_rep` or `affinity` in `game/`).
- `flirting.md`, `npcaffinity.md` and `dialoguetrees.md` are placeholders.
- Clout (ledger :919, "Both: XP levels for stats, Clout for moves") is a different ladder, for moves. It does not cover prices or access, so it does not replace this system. Whether the two overlap: no ruling: author's call.

## Line by line

| Doc lines | Element | Verdict | Ruling it rests on |
|---|---|---|---|
| 4 | Trio's reputation is collective ("Those Three American Idiots") | **Keep** | CC: the bros are the punchline, party is three bros. No ruling against it |
| 5, 235-243 | "Even success states roast them"; success is relative | **Keep** | CC: bros laughed AT, sincerity is the joke |
| 8-49, 55-96, 102-143 | Three five-step ladders (Publandia, Debaucheryville, Sinfonia) | **No ruling: author's call** (whether per-city ladders exist at all) | City list and order are ruled (ledger :27, :895). Shamsterdam has no ladder: no ruling |
| 8, 55, 102 | City names | **Keep** | CC: parody place names |
| 11, 33, 51 | "Irish joke", "Irish Car Bombs", "Guinness", "craic" | **No ruling: author's call** | CC lets real brands keep names; the real-place-names rule covers places. Whether "Irish" counts is unruled |
| 106, 117, 121-122, 137 | "formal German", "Mozart", "Für Elise", waltz/polka | Mozart and Für Elise **keep**; "German": **no ruling: author's call** | CC: real songs and titles keep real names; "German" is place-derived, unruled |
| 14, 59, 71 | Price markup by reputation (+50%, +100%) | **Change** (do not build as written) | Prices are fixed SOVS with fixed joke prices, e.g. "3 SOVS everywhere" (ledger :508); the economy build order is ruled (ledger :850). Price scaling needs a ruling. Touches bead Eurobound-it49 |
| 14, 71, 93 | Discounts and free goods at high rep | **No ruling: author's call** | BCD bans free advantages for intoxicants only; economy numbers need a ruling (CC "Ask the author first") |
| 15, 31-32, 224 | Bravado regen -1 / +1 in tavern battles | **Change** | Bravado is fully ruled: thirds tiers (ledger :549, :573); Party Prep stays off (ledger :881). New Bravado modifiers need a ruling |
| 16, 22-23, 38, 62, 77-78, 85, 124, 133 | Access gating ("locals only", underground, VIP) | **No ruling: author's call** | No ruling on gating by standing. All side quests are optional (CC) |
| 17, 64, 111 | Starting state set by arriving in the city | **Keep** | No conflict |
| 18-25, 65-72, 112-119 | Mid states "Pub Crawl Rookies", "Useful Idiots", "Eager Students" and the rest | **Keep as copy, pending approval of the ladder** | CC: funny names, bros are the punchline. All names must be unique: check at approval |
| 12, 20, 28, 44, 59, 106, 138 | Descriptions and NPC reactions ("stray dogs", "beloved mascots", "visible disgust") | **Keep** | CC: MA game, full strength. "Mascots" is an NPC reaction, not a companion object, so no-mascots is not broken; confirm at approval |
| 79, 86, 95, 134, 141-142 | New spell variants and combos ("Chaos Magic", "Casino Royale", "Symphony of Bros", "Symphony Conductor") | **Cut from this doc** (unlocks belong to Clout) | Clout opens moves (ledger :919); new mechanics need a ruling (CC) |
| 50-53, 97-100, 144-147 | Reputation Destroyers: "Disrespecting Locals / Mocking accents", "Cultural Vandalism", "Crude Behavior" | **Change** | CC and BCD: no moral framing. Punishing the bros for being crude moralises. Whether bad behaviour can lose standing at all: no ruling: author's call |
| 99 | "Moralizing: lecturing about vice" | **Keep** | BCD: no moral lectures |
| 98 | "Being Too Cautious" | **Keep** | BCD: the bros are willing, never reluctant |
| 147 | "Fake Sophistication: getting caught pretending" | **Change** | CC: the bros are never self-aware or scam-aware. Fine only if they stay oblivious |
| 106-107, 112-113 | NPCs disgusted by the bros, treat them like children | **Keep** | CC: the bros are never afraid or disgusted, NPCs may be |
| 149-157 | Cross-region spillover and combined titles | **No ruling: author's call** | Backtracking and city order are ruled (ledger :27, :38); standing carrying across cities is not |
| 159-170 | Dialogue options by standing, "pathetic groveling to delusional boasting" | **Change** | Boasting fits CC and BCD. "Sophistication", "Cultural Exchange" or witty options clash with "bros are doofuses" (memory `feedback_bros_not_clever.md`; ledger :1012). Exact options: author's call |
| 172-178 | Social combat actions: "Storytelling", "Influence Flexing", "Intimidation" | **Change** | Social damage is a ruled stat formula (ledger :568); a "Words Only" fight exists (ledger :776). Per-bro action names are new content: author's call |
| 179-183 | Reputation modifies social combat | **Change** | Ledger :568 gives the formula without it; a new modifier needs a ruling |
| 185-200 | Gains, losses and reset events ("The Great Misunderstanding", "Cultural Revelation", "Chaos Cascade") | **No ruling: author's call** | Story events belong to the author (CC). "Cultural Revelation: sudden sophistication" is flagged because the bros do not grow clever |
| 189, 243 | "Genuine cultural appreciation", "Character growth" | **Cut** | CC: bros never aspirational. The Clout proposal flags the same "Character Growth" idea (`docs/superpowers/specs/2026-11-15-progression-clout-vs-xp-proposal.md:20`). Pending author confirmation |
| 202-215 | UI: state name, tooltip, emoji icon, progress hints, "locals seem..." | **Change** | The ruled game menu has no Street Rep display (ledger :707). Any display is a new menu section: author's call. "Locals seem..." hints narrate the satire: avoid (CC) |
| 208-211 | "Clear consequences previewed", "impact warnings for disastrous actions" | **Cut** | CC: the game never winks or explains the jokes; warnings undercut the delusion |
| 217-233 | Integration: crowd behaviour, equipment "uniforms", quest gating, failed quests cost rep | **No ruling: author's call** | Quest structure and equipment need rulings (CC). All side quests are optional |
| 222-225 | Bravado synergy; "Reputation loss can drain Bravado" | **Change** | Bravado is ruled (ledger :549, :573, :881); a rep drain needs a ruling |
| 245-251 | Closing goals | **Keep** | Not a rule |
| GDD :262 | "Street Rep: optional meter raised by witty choices" | **Change** | The menu shows no Street Rep (ledger :707). "Witty choices" clashes with the bros being doofuses (`feedback_bros_not_clever.md`; ledger :1012). The meter itself: no ruling: author's call |

## Summary

- **Keep:** collective standing, satire tone, parody city names, funny state names and NPC reactions, the "Moralizing" and "Being Too Cautious" destroyers, NPCs disgusted by the bros.
- **Change:** price markup, Bravado effects, insensitivity penalties, the "caught faking" rule, dialogue options, social combat actions and modifier, reputation display, Street Rep wording.
- **Cut:** spell and ability unlocks (they belong to Clout), "genuine appreciation" and "character growth" gains, consequence previews and warnings.
- **No ruling: the author's call:** whether per-city reputation ships at all; cross-city spillover; access gating; discounts and free goods; story reset events; "Irish" and "German" wording; overlap with Clout.

## On approval

The ledger records the ruled list and the doc gets a status banner (bead acceptance).
