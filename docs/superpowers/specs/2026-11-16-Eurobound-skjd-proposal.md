# Street encounters: proposal for the author (Eurobound-skjd)

**Status: APPROVED, Option A (author, Eurobound Desk `Eurobound-skjd-q2`, 2026-11-16, verbatim: "A: EarthBound straight (lose = back to last save, lose some SOVS)"). Options B and C were not picked. Every [author] blank and every gap in section 5 stays open until the author rules it.**

The author asked for this (bead page, 2026-11-16, verbatim): "An agent drafts a street-encounter proposal from the GDD lines plus a comparison with EarthBound, for my approval".

Ground rules for this draft: it is built only from what the docs and the rulings ledger already say. It adds no enemy, place, NPC, line of dialogue or number. Anything that needs one is listed under "Open for the author" (section 5). No game file or design doc was changed.

---

## 1. What canon already says

### 1.1 The promise (never designed)

| What | Where |
|---|---|
| Game loop: "Explore overworld → Trigger visible encounters → EarthBound-style battle → Earn EXP, items, gear → City boss → ..." | `design/game_design_document.md:10` |
| "Encounters: visible enemies; preemptive/back attacks; auto-win vs. very weak foes" | `design/game_design_document.md:16` |
| "Encounters: Visible enemies with preemptive/back attack logic; auto-win vs weak foes." | `design/game_design_document.md:293` |
| "Combat: Front-view, menu-driven, rolling HP meter, SMAAAASH crits" | `design/game_design_document.md:287` |
| Microinteraction: "rolling HP tween (1–2s)" | `design/game_design_document.md:277` |
| Enemy template asks each regular enemy for its "Zone / Encounter Table", "Encounter Family", an "On fleeing" line and an "Overworld Sprite" ("If it is visible before the fight, or 'random encounter only'") | `design/templates/enemy_template.md:34-35`, `:92`, `:120` |

### 1.2 Debaucheryville street enemies the docs already name

`design/worlds/debaucheryville/debaucheryville.md:157-170` (repeated in `design/game_design_document.md:126-128`):

- Street & Club: The Velvet Hostess, The Expat Who Never Left, The Silent Bouncer, Velvet Flyer, Backpack Bard, Pickpocket Pair, Green Fairy Wisp.
- Circus: Crypto Clown, Rigged Carnival Game, Knife-Throwing Assistant.
- Also: "Living statue encounters (they come alive and attack)" in The Gilded Square (`debaucheryville.md:9`).

None of them has an enemy doc, stats or engine data yet. `game/assets/data/enemies/debaucheryville_enemies.json` holds only the Arcade and Taproom villains. The Green Fairy Wisp is already a Taproom fight (72 HP, leaves after round 6; `docs/superpowers/NEXT_WORK.md:774-780`).

Time hooks the docs already name: "Closing Time Chaos: Final hour brings unique encounters" (`debaucheryville.md:138`); "Hour-Dependent Events: Different NPCs and opportunities appear at specific times" (`debaucheryville.md:135`); Publandia's Doner Lane has "fights after 1 a.m." (`game_design_document.md:58`); Sinfonia's opera house lists "Day Mode Enemies" (`design/worlds/sinfonia/bassline_opera_house.md:945`).

### 1.3 Standing rulings that any street encounter must respect

| Ruling | Where |
|---|---|
| Battles: HD-2D side view, bros and enemies both on screen in a 3D arena. Overworld: a leader with the other two following in a line | `NEXT_WORK.md:510-511` (round v24) |
| Rolling HP meter drains 10 HP/s | `NEXT_WORK.md:552`; `design/mechanics/Battle/battle_numbers_proposal.md:19`, `:34` |
| Run chance 50% ±5% per point of average-Speed edge, clamped 10-90% | `NEXT_WORK.md:553` |
| A downed bro leaves a won fight at 1 HP | `NEXT_WORK.md:572` |
| Lasting statuses (Tourist Trap Victim, Food Poisoning, Broke AF, Grease Fingers) persist after the fight | `NEXT_WORK.md:574` |
| 1 battle turn = 40 overworld steps | `NEXT_WORK.md:827` |
| XP levels raise stats; Clout opens moves (direction only; curve and numbers open) | `NEXT_WORK.md:919` |
| Saving only at hotspots and beds, 3 slots, no autosave | `NEXT_WORK.md:892` |
| Rest spots are the hostel and the hosts; saving is offered at the hostel bed | `NEXT_WORK.md:920` |
| **Losing, the only cases ruled:** an Arcade cabinet fight puts the bros back in front of that cabinet at 1 HP, tokens spent (`NEXT_WORK.md:513-514`, `battle_numbers_proposal.md:22`); a Grandpa Provides loss costs 50 SOVS to Accounts Receivable (`NEXT_WORK.md:793`, `:635`) | as cited |
| The bros are never afraid or disgusted, never self-aware | `.claude/CLAUDE.md`, Content rules |

Not ruled, and not used as a rule here: "Blackout Drunk ... Battle ends, wake up in random location with random items missing" (`design/mechanics/Battle/status_effects.md:102-104`); the dead PRD's encounter rules (`design/legacy/EUROBOUND_PRD.md:246`, superseded branch, never canon).

### 1.4 What the code has

`game/battle/battle_core.gd:24` already returns `"won"`, `"lost"` or `"ran"`; `game/battle/battle_screen.gd:557-559` prints "GAME OVER" on a loss. There is no overworld enemy, no contact trigger, no first-strike logic and no loss handling outside the Arcade (`grep encounter|preempt` in `game/` finds nothing).

---

## 2. EarthBound, mechanic by mechanic

What EarthBound (SNES, 1994/95) does, and how it lines up with Eurobound.

| Mechanic | EarthBound | Eurobound canon today | Gap |
|---|---|---|---|
| **Visible enemies** | Every regular enemy walks the map. Some walk toward the party, some wander, some stand still. Leaving and re-entering an area brings them back. | Promised (GDD:16, :293). The template has an Overworld Sprite field (`enemy_template.md:120`). | How they move, where, how many, when they come back. |
| **Contact starts the fight** | Touching an enemy starts the battle with a swirl. Nearby enemies can be pulled into the same fight. | Arcade fights start by facing a cabinet and pressing the button, no cue (`NEXT_WORK.md:514`). | Street contact rule; whether nearby enemies join. |
| **First strike (preemptive)** | Touch an enemy from behind: green swirl, the party gets a free first round. | "preemptive/back attacks" (GDD:16, :293), no rule. | Who gets the free round and how big it is. |
| **Back attack** | An enemy touches the party from behind: red swirl, the enemy gets the free first round. | Same line, no rule. | Same. |
| **Auto-win vs weak foes** | If the party clearly outclasses an enemy, contact ends the fight on the spot: "YOU WON!", full EXP and drops, no battle screen. Such enemies usually walk away from the party. | Promised (GDD:16, :293). Needs a level or strength comparison; XP levels are ruled in direction only (`NEXT_WORK.md:919`). | The "clearly outclasses" test and its threshold. |
| **Rolling HP meter** | HP rolls down like an odometer. A character hit for mortal damage can still act, heal, or win before the meter reaches zero. | **Already ruled and built**: 10 HP/s (`NEXT_WORK.md:552`; `battle_numbers_proposal.md:19`). | None for battle. Whether the meter matters on the map (EarthBound's does not) is not asked. |
| **Running** | A Run command; on the map, the party has a moment where enemies cannot re-engage. | Run is ruled (`NEXT_WORK.md:553`); running from a cabinet returns the bros to it. | What happens on the street after a successful Run (grace time). |
| **Losing** | When the whole party falls: a "continue?" choice. Continuing puts the party back at the last place the game was saved, keeps EXP and items, and **halves the cash on hand** (banked money is safe). | Only the cabinet loss and the Grandpa Provides loss are ruled (section 1.3). The Taproom loss is not ruled. | The loss rule everywhere else. |

---

## 3. Options

Each option is a complete encounter model plus a loss rule, so the author can pick one card. All three keep the ruled battle (side view, rolling HP, Run, 1 HP after a win) unchanged. Any number marked **[author]** stays blank until ruled.

### Option A: EarthBound straight (recommended)

The closest match to the GDD lines, which name EarthBound's model almost word for word.

1. **Visible.** Street enemies are on the map, drawn with their overworld sprite. Each enemy doc says where it appears (its "Zone / Encounter Table") and how it moves: stands still, wanders, or walks toward the bros. Which enemy does which is per enemy doc **[author]**.
2. **Contact.** Walking into an enemy starts the fight. Whether other enemies close by join it **[author: yes/no]**.
3. **First strike.** The bros touch an enemy from behind: the bros act first for one round. An enemy touches the bros from behind: the enemy acts first for one round. Otherwise normal Speed order (`battle_numbers_proposal.md:15`).
4. **Auto-win.** Touching an enemy the bros clearly outclass ends it on the spot: the win screen, its XP, SOVS and drops, no battle. The test compares party level to the enemy's level **[author: the gap]**. Until the XP curve is ruled (`NEXT_WORK.md:919`), auto-win is off.
5. **After a fight or a Run.** A short grace period where enemies on the map cannot start a fight **[author: length, in steps or seconds]**.
6. **Respawn.** Enemies come back when the bros leave the screen and return.
7. **Losing.** When all three bros are down: back at the last save (a FREE Wi-Fi hotspot or the hostel bed, `NEXT_WORK.md:892`, `:920`), XP and items kept, part of the SOVS on hand lost **[author: what share]**. Who pays and how it is shown on screen goes to the Writers' Room for the author's approval.

Cost: the biggest build of the three (overworld AI, facing test, level test). Fits the game loop at `game_design_document.md:10`.

### Option B: EarthBound encounters, Arcade-style loss

The same encounter rules as Option A (points 1-6), with a loss rule that extends the two losses already ruled instead of EarthBound's "back to the save".

7. **Losing.** The fight ends, the bros get up where the fight happened at 1 HP each (as the cabinet loss, `NEXT_WORK.md:513-514`), and the enemy takes SOVS, as Accounts Receivable does on a Grandpa Provides loss (`NEXT_WORK.md:793`). How many SOVS **[author: a flat sum, a share, or per enemy doc]**. No trip back to a save point, so a loss never undoes progress since the last save.

Cost: the same as A for encounters; the loss is simpler (no reload). It keeps one loss rule across the Arcade, the Taproom (still unruled) and the street.

### Option C: Placed encounters, authored losses

Street enemies do not roam. Each stands at a fixed spot the location doc names, like the cabinets and Jiří at Tram Stop #17, and some appear only at the hours the docs already tie to fights (`debaucheryville.md:135`, `:138`; `game_design_document.md:58`).

1. **Visible.** Every street enemy is on the map at its spot (and hours, if its doc gives any). Walking into it starts the fight.
2. **First strike.** As Option A, point 3, judged by which way the enemy is facing.
3. **Auto-win.** As Option A, point 4 (off until levels are ruled).
4. **After a win.** The enemy stays gone until the next rest (`NEXT_WORK.md:920`) **[author: or until the screen reloads]**.
5. **Losing.** Each enemy doc carries its own loss outcome, the way the cabinets and Grandpa Provides do. An enemy doc with no outcome uses Option B's rule.

Cost: the smallest build (no roaming AI, no density tuning) and the most writing: every enemy doc needs a spot, hours and a loss outcome. Fewer fights overall; it drifts from "visible enemies" toward "visible set pieces".

---

## 4. What stays the same in every option

- No new enemy, place, NPC or line is added by this proposal. The street enemies are the ten already named (section 1.2) plus the living statues; each gets an enemy doc from `design/templates/enemy_template.md` before it is built.
- The battle itself is unchanged: side view, rolling HP at 10 HP/s, Run, 1 HP after a won fight, lasting statuses.
- The bros are never afraid: an enemy that walks away from them (auto-win) is the enemy's doing; no option has the bros flee or avoid anything on their own.
- The "GAME OVER" text in `battle_screen.gd:559` is a placeholder until the loss rule is ruled.

## 5. Open for the author (gaps no option fills)

1. **Slice scope:** are street encounters in the Debaucheryville slice, or later? (Bead acceptance.)
2. **Which named enemies roam where**, and in which district (The Gilded Square, Clocktower Plaza, Hostel Row, the Cirque du Shady). Each is an enemy doc decision.
3. **Numbers:** the auto-win level gap, the grace period, the SOVS taken on a loss, how many enemies a screen holds, the size of the first-strike advantage (one round is the EarthBound size).
4. **The Green Fairy Wisp** is both a Taproom fight (`NEXT_WORK.md:774-780`) and a street enemy (`debaucheryville.md:165`). Is the street one the same enemy, a palette swap, or struck? (All names must be unique.)
5. **The Taproom loss** has no rule. Should it follow whatever is picked here?
6. **Blackout Drunk** (`status_effects.md:102-104`, "wake up in random location with random items missing") is unruled. Is it a loss outcome, a drinking outcome, both, or struck? It is not used in any option.
7. **Do nearby enemies join a fight** (EarthBound does this)?
8. **Day and night enemy sets:** should street enemies change by hour (the docs hint at it, section 1.2)?

## 6. After the ruling

A design doc under `design/mechanics/Battle/` records the picked option, and build beads follow (overworld enemy node, contact and facing test, auto-win test, loss handler, enemy docs for the named street enemies).
