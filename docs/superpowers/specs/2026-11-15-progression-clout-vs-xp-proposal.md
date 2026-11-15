# How the bros grow: Clout ladder, XP levels, or both

Proposal for the author's approval. Bead Eurobound-028k, Desk card Eurobound-028k-q1. Written 2026-11-15 from a systems-design view. Nothing in `game/` or `design/` was changed.

Audience check used throughout: younger Gen X, xennial and millennial women. The bros are the punchline, never aspirational, never self-aware, and no mechanic lectures (`.claude/CLAUDE.md`, `design/narrative/bros_choose_debauchery.md:16-18`).

## What exists today

- **Nothing is switched on.** A won fight adds up the enemies' XP and then drops it: `game/worlds/debaucheryville/absinthe_arcade/taproom_battle.gd:72` counts it, line 73 pays only SOVS.
- **The engine has the fields.** Each bro stores `level` 1 and `xp` 0 (`game/core/game_state.gd:60-61`, `game/assets/data/party/party_members.json:6-7`). 15 enemy rows carry an `xp_reward`. The menu already prints "Lv" and "XP" (`game/ui/field_menu.gd:393`, `:489`). The one payout function gives XP to the first bro only and only tests call it (`game/core/game_state.gd:120-122`).
- **The docs have one design, never approved.** `design/mechanics/Progression/skilltrees_cloutspells.md` (171 lines) is the Clout ladder. `leveling.md`, `xpgain.md`, `characterclasses.md` and `unlockables.md` are two-line placeholders. The ledger has no ruling on either; it only says "until levels exist" (`docs/superpowers/NEXT_WORK.md:572`).
- **An older doc already says they are one thing.** `design/mechanics/Battle/party.md:103`: "XP → Clout (level-ups, unlocks, stat points)". That doc is old (it still calls money "Cover Charges"), so it is a pointer, not a ruling.

## The three options

### 1. Clout ladder only

- **What the player does:** earns Clout. The ladder doc never says from what; `party.md:100` says from wins.
- **What advancing gives:** five rungs, Pledge to Living Legend (`skilltrees_cloutspells.md:11-15`). Each rung opens moves in three branches per bro (`:17-84`), then team combos (`:86-98`). The doc lists 45 moves; the game has 1 today (`docs/research/2026-11-14-mechanics-gap-audit.md:36`).
- **Satire fit:** the best of the three. Clout measures how legendary the bros think they are, and the doc's core rule is that a bigger ego crashes harder (`:3-7`, `:120-124`). Climbing makes them more ridiculous, not cooler. Three parts cut the other way and should go: a status that shows the bros how they look and rewards "Character Growth" (`:149-153`, breaks never self-aware); "they become genuinely formidable" (`:166`); NPCs bowing to them (`:130`).
- **Already exists:** the doc, the three "Skill Tree (3 branches)" sections in the character files, and all the engine XP fields above, which can carry the Clout number as they are.
- **To build:** pay Clout to every bro on a win; a rung check; the menu label; then moves, rung by rung.
- **What it breaks:** the menu's "Lv / XP" wording. The doc's Embarrassed numbers (`:5-6`) disagree with the ruled ones (`NEXT_WORK.md:569`). "Honorary Irishman" (`:105`) leans on a real place. Every threshold and percentage in the doc is unapproved.

### 2. XP levels only, as the engine has them

- **What the player does:** wins fights; each enemy's `xp_reward` adds up.
- **What advancing gives:** nothing is defined. No doc has a level curve or says what a level raises.
- **Satire fit:** none. It is the standard hero track: the bros get plainly stronger and the game says so with a straight face. Nothing here laughs at them.
- **Already exists:** the fields, the enemy values and the menu line.
- **To build:** the payout, a curve and stat growth per level, all from a blank page.
- **What it breaks:** the Clout doc, `party.md:103` and the three character skill trees are left with no way to unlock anything.

### 3. Both: XP levels for stats, Clout for moves

- **What the player does:** earns two numbers, most likely from the same fights.
- **What advancing gives:** levels raise stats; Clout rungs open moves.
- **Satire fit:** the Clout half keeps the joke; the XP half is the straight hero track again.
- **Already exists:** the same pieces as 1 and 2.
- **To build:** everything in 1 plus everything in 2, and two bars to show and explain.
- **What it breaks:** `party.md:103`, which treats them as one. It also doubles the numbers the author has to rule.

## Recommendation: option 1, Clout only

One number, shown to the player as Clout, stored in the engine's existing `xp` field; the engine's `level` holds the rung. Reasons:

1. It is the only option where growing is itself the joke. For this audience the bros must get more deluded as they climb, not more admirable.
2. It is also the cheapest honest build: the plumbing is there, and one track means one set of numbers to approve.
3. It matches the only line in the docs that speaks to the question (`party.md:103`).

What this proposal does not decide (all are **numbers for the author** or content rulings): how much Clout each rung needs; how much each fight pays (the 15 existing `xp_reward` values are unapproved too); whether a rung also raises stats; which of the 45 listed moves survive; the rung names. The ladder doc's own figures (100, 300, 600, 1000 and the rest) are quoted from an unapproved doc and are not endorsed here.

## First three build steps, if approved

1. **Record the ruling and clear the placeholders.** Ledger entry; `leveling.md` and `xpgain.md` point at the ruled system; a short list of the ladder doc's clashing parts (above) goes to the author to strike or keep.
2. **A numbers proposal for the first slice only**, for approval on the Desk: Clout per fight, Clout per rung, and what the first rungs give. Tied to Eurobound-g0jr (Chadwick's and Bradley's first moves).
3. **Switch it on** (this is Eurobound-5aie): a win pays every bro, the rung check runs, the menu says Clout, with GUT tests. Includes a ruling on what "until levels exist" (`NEXT_WORK.md:572`) means once rungs exist.
