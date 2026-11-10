# Villain Profile: Player Two Palette Swap

*"I'm Player One. I have always been Player One. He is wearing my trousers in the wrong color."*

## 📋 Villain Identity
- **Villain ID**: `debaucheryville_villain_player_two_palette_swap_01`
- **Display Name**: Player Two Palette Swap (spawns as 2–3 units; battle UI suffixes A/B/C)
- **Tier**: Minor Villain
- **Primary Location**: Absinthe Arcade (`debaucheryville_clocktower_arcade_01`), node `aa_node_main_cabinet_loop`, released by the Street Fighter: Identity Crisis cabinet (`street_fighter_identity_crisis`)
- **Associated Quest/Arc**: None
- **Encounter Type**: Optional, Repeatable (token-triggered; Street Fighter: Identity Crisis costs 3 Absinthe Arcade Tokens per release = 3 SOVS, ruled 2026-11-09)
- **Fight role**: **Swarmer.** Cheap, fast, multiple units. They're the fodder that the other two Identity Crisis villains bring along.

---

## 🎭 Core Concept

### The Racket
The Identity Crisis cabinet runs a bootleg board. Somewhere inside it, a counterfeit circuit board has been rolling out the same karate man in a new colorway every few seconds since 1994. Each copy is fully convinced he's the original. That makes them Debaucheryville's counterfeit trade in fighter form, the same town that sells fake VIP wristbands and food-colored "authentic" absinthe. The Arcade charges three tokens to let them out. They work for nothing because they think the fighting *is* the pay. The house keeps the token, every time.

### What Bros Believe
That the cabinet took one look at them, recognized three returning champions, and sent its best fighters out to defend its honor. Each Swap calls whoever it's fighting "Player One," and to the bros that settles it. The cabinet remembers them, and they're Player One.

### The Comedy Gap
The Swaps are interchangeable men, cut from the same template and dressed in different colors, each completely sure he's the singular original. They're fighting three interchangeable men in different-colored polos, each completely sure he's the singular original. Nobody on either side of the fight notices. Satire targets: counterfeit tourist culture, the "authentic" knockoff, and the bros' belief that they're unique when they're line item #4,000 with a predictable average spend.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Permanently 24, the age fighters stayed in 1994 |
| Build | Lean karate-tournament build, one fixed fighting stance, bouncing on the balls of his feet with no off switch |
| Height | Average. Exactly average. Every copy is the same height to the pixel |
| Energy | Earnest, twitchy, territorial |

### Costume & Distinguishing Features
- **Martial-arts gi in a colorway nobody chose**: teal-and-mustard, cocktail-sauce pink, hospital-scrubs green, nicotine beige. Every copy's gi is a palette swap of the same garment, which is the whole joke and the whole sprite budget.
- **Accessories**: A headband with the tails fluttering in a wind that isn't there. Hand wraps in the "wrong" color. A small player indicator floating over his head that reads **2P** and that he keeps trying to swat away.
- **Tell**: Every few seconds he glances sideways at the other Swaps to check whose colors look more original.
- **Visual element**: Faint scanlines run across his whole body. He's slightly lower resolution than the battle background, and he resents it.

### Sprite Notes
- **Battle sprite**: front-view static (EarthBound style) over the psychedelic background, 1–2 frame bounce idle. **One base sprite, palette-swapped 3–5 times.** This villain *is* the palette-swap budget, so build it to be swapped.
- **Release animation** (shared across all three Identity Crisis villains): the cabinet screen bulges, then the fighter steps out through the glass as a flat 2D sprite and settles into the battle lineup. Green mist trails off the cabinet.
- **Overworld**: none. They only exist inside the encounter.
- **Big-move telegraph (Mirror Match Custody Dispute)**: two Swaps turn to face each other and jab a finger, each with a **1P** marker blinking over its head. The markers flicker between the two of them.
- **Remap gag (cosmetic)**: on each new round, the Swaps' palettes rotate one step, so A is wearing B's colors. Purely cosmetic, and it can be disabled under motion/flash accessibility settings.

---

## 🧠 Personality & Dialogue

### Archetype
**The Insistent Copy.** A counterfeit who's certain he's real. He wants to be acknowledged as the original, the one in the attract-mode demo, the face on the side art. He'll fight anyone to prove it, though he mostly argues with the other Swaps about it in the middle of a punch. He's funny because he's wrong in exactly the way the bros are wrong, and he defends it just as hard.

### Pre-Battle Dialogue
*Three tokens drop. The cabinet screen reads **2P HAS JOINED**. Two Swaps (three after a second release in the same visit) climb out of the glass:*
> TEAL SWAP: "Player One. Finally. I have been the original for nine years."
> MUSTARD SWAP: "He is the copy. Look at his trousers. Now look at MY trousers."
> CHADWICK: "Bro. They know us. The machine KNOWS us. We're Player One."
> BRADLEY: "I've beaten this game before. Senior week, '97. Under the pier. No shirt."
> LORD PILSNER: "Gentlemen, I was regional champion of this very game. Different region. Same spirit."
> TEAL SWAP: "Select your fighter."
> BRADLEY: "We ARE the fighters, bro. Hit start."

### Mid-Battle Barks
| Trigger | Line |
|---------|------|
| Fight start | "ROUND ONE. Which one of us said that? FIGHT!" |
| Below 50% HP | "I'm not hurt. The other one is hurt. We are not the same." |
| Big-move telegraph | TEAL: "I'M PLAYER ONE." / MUSTARD: "I'M PLAYER ONE." |
| Bro gets KO'd / status lands | "Your health bar is the same color as his. One of you is a bootleg. My money is on the cargo shorts." |
| Another Swap is KO'd (passive fires) | "He's gone. I'm the original now. I have always been the original." |
| Bro lands a SMAAAASH on a Swap | "That hit the copy. I felt it as the original, but it hit the copy." |

### Bro Reaction Barks (battle-log / party lines)
| Trigger | Line |
|---------|------|
| Lord Pilsner targets any Swap | "Have at thee, Dennis." (He calls every Swap Dennis. All of them. Every visit.) |
| Chadwick opens the fight | "Cocktail-sauce one is mine. Best colorway in the lineup. Nine out of ten." |
| Bradley gets hit by Same Punch, Different Trousers | "That's fine. My shoulder does that now. That's a gym thing." |

### Defeat Dialogue
> "K.O.? No. That was the other one. Tell the cabinet it was the other one."

### Post-Defeat Presence (If Any)
They go back into the cabinet and come out of the next token in new colors. They don't remember the bros, and the bros remember all of them, wrongly. Pilsner keeps calling every one of them Dennis on every return visit. No redemption, no growth. The bootleg board keeps printing them forever.

---

## ⚔️ Combat Specification

> **Approved 2026-11-09.** Every number in this section (stats, multipliers, weights, durations) is approved. They're benchmarked against the only shipped Debaucheryville enemy, Feral Segway Tourist (HP 28 / OFF 6 / DEF 3 / SPD 6 / LCK 2 / 12 XP / 8 gold), and sized for a 2–3 unit swarm.

### Core Stats
| Stat | Value | Notes |
|------|-------|-------|
| **HP** | 16 (each) | Rolling meter applies to the bros, not enemies. Low HP because they come in packs |
| **SP** | N/A | Engine enemy schema has no SP field |
| **Offense** | 5 | |
| **Defense** | 2 | |
| **Speed** | 8 | Fastest of the three Identity Crisis villains. They act early and often |
| **Charm** | 2 | Not in the engine schema yet (design stat only) |
| **Luck** | 3 | |
| **Grit** | 1 | Crit resist. A SMAAAASH lands easily on a Swap. Not in the engine schema yet |

### Move List (data-driven weighted-random AI)
Damage multipliers follow the PRD damage model (`ATK × SkillMult − DEF`).

| Move | Type | Effect | Status Inflicted | Weight / Condition | Telegraphed? |
|------|------|--------|------------------|--------------------|--------------|
| **Same Punch, Different Trousers** | Physical | 1.0× single target. Battle log: "It is the same punch. It is in a different color." | — | 50% / always | No |
| **Is This My Taunt or His?** | Social (Bravado attack) | Performs the "original's" taunt slightly wrong. Target bro −3 BP. | — | 25% / always | No |
| **Hold Back to Block, Spiritually** | Gimmick (self-guard) | Halves damage taken by this Swap until its next turn | — | 25% / always (→ 10% when it is the last Swap alive) | No |
| **Mirror Match Custody Dispute** | Physical (two-unit) | Two Swaps hit the same bro back to back, 1.25× each | — | Once every 3 rounds / **requires ≥2 Swaps alive** (ally-count AI gate **Approved 2026-11-09**) | **Yes**: one round of the 1P-marker finger-pointing argument (see Sprite Notes) |

**Passive: I'm the Original Now.** When a Swap is KO'd, one surviving Swap gains **Gains Bro** (+20% ATK, 2 turns). Doesn't stack, and reapplying it refreshes the duration (master-list rule). It uses an "ally KO'd" AI trigger alongside the documented gates (`hp<50%`, `target_has_status`, `round>2`); the trigger is **Approved 2026-11-09**.

### Phases (Minor Villain: 1 phase)
| Phase | Trigger | Behavior Change |
|-------|---------|-----------------|
| 1 | Fight start | Weighted-random per table. Once a single Swap is left, Hold Back to Block drops to 10% and the freed weight goes to Same Punch, Different Trousers. He has no one left to argue with, so he commits. |

### Buffs & Debuffs They Use
- **Self/ally buffs**: Gains Bro (via the passive); the self-guard from Hold Back to Block.
- **Debuffs on the party**: none from the master status list. They attack Bravado directly (Cringe-caster flavor) instead of applying a status. A grunt that stacks statuses would crowd out Super Turbo Hyper Jarmila's job.

### Immunities / Resistances / Weaknesses
| Category | Detail |
|----------|--------|
| **Immune to** | Nothing. They're grunts |
| **Resistant to** | Embarrassed, 50% resist. They can't be embarrassed by a costume they'd die defending |
| **Weak against** | **Confused** (random targeting). A Confused Swap aims at another Swap at the normal random-target rate, and it reads as him finally settling the custody dispute. Chadwick's *Charm of the Bro Code* landing on a Swap is the intended "aha" |
| **Vulnerability window** | After **Mirror Match Custody Dispute** resolves, both participating Swaps skip their next action arguing about who did more damage (uses the PRD §6.8 "Distracted for 1 turn" vulnerability convention) |

### Adds / Minions (If Any)
| Minion | Count | Role | Notes |
|--------|-------|------|-------|
| Player Two Palette Swap | 2–3 | Swarmer | They *are* the adds. They also escort the other two Identity Crisis villains (see the encounter table proposal below). No re-summon mid-fight |

### Arena & Gimmick
The fight happens in place at `aa_node_main_cabinet_loop`. The battle transition swipes out of the cabinet screen into the standard psychedelic background, which here gets a CRT scanline overlay and a palette that cycles through the Swaps' colorways.

**Cabinet-wide gimmick: Second Thoughts (Approved 2026-11-09).** Each Identity Crisis villain's chosen move has a 20% chance to be re-rolled after it's announced. The log prints the first move name, then a correction ("Mustard Swap uses Same Punch, Different Trousers! ...No. He has decided it is his taunt."). This is the cabinet's "questions and remaps his own moves mid-combo" identity expressed in the battle system.

**Encounter table (weighted random table; structure ruled 2026-11-09, weights Approved 2026-11-09)**. One play (3 tokens) releases one of these groups:
| Roll | Group |
|------|-------|
| 50% | 2 Player Two Palette Swaps (3 if the party is above the Arcade's level band) |
| 30% | Super Turbo Hyper Jarmila + 1 Player Two Palette Swap |
| 20% | Two-Seventy Vratislav + Super Turbo Hyper Jarmila |

**Stale-spec note for the lead**: `absinthe_arcade_interactions.json` → `street_fighter_identity_crisis` still carries mini-game fields (`complete_three_adaptive_combos`, `identity_meter_reaches_zero`, `type: mini_game_cabinet`). The 2026-11-02 ruling makes those obsolete. Per instructions, this profile doesn't edit the package JSON.

---

## 💰 Rewards

> **Approved 2026-11-09**, including the ticket amount (review round).

| Reward | Value / Item | Notes |
|--------|--------------|-------|
| **Tickets** | 4 arcade tickets per Swap | **Approved 2026-11-09** (review round). Arcade fights pay tickets, not SOVS (ruling 2026-11-09), so the cabinet can't print money. Redeemable at the Prize Redemption counter built into the bar |
| **Clout (XP)** | 6 per Swap | A 2-Swap pull pays 12, matching one Feral Segway Tourist. Clout is farmable at 3 SOVS per play; no cap or taper is proposed |
| **Guaranteed drop** | None | |
| **Rare drop** | **Absinthe Arcade Token** (existing item `item_absinthe_arcade_token`), 15% | One of your three tokens back, occasionally. The house keeps the other two |
| **Rare drop** | **Spare Player-Two Headband** (new item, Approved 2026-11-09), 5% | Accessory: +1 Speed. Item card: "Fits anyone. That's the problem." Tails flutter in no wind at all. Needs a `permanent_item_template.md` / item doc |
| **Unlocks** | First win against any Identity Crisis villain fires the existing cabinet reward dialogue set `hacker_respects_adaptation` (Twitchy Hacker Types), reusing the package's current reward hook | |
| **Achievement** | **Accept No Substitutes** (Approved 2026-11-09). *Public*: "Defeat three Player Two Palette Swaps in a single fight." *Hidden truth*: "All three were Dennis." | Callback to Pilsner's running name gag. It doesn't comment on the bros |

---

## 🔗 Connections
| NPC / Villain | Relationship |
|---------------|--------------|
| Super Turbo Hyper Jarmila | She "rebalances" them between revisions and they take it as a promotion. She can't tell them apart either |
| Two-Seventy Vratislav | They warm up on him in attract mode. He holds them. They tolerate it |
| Arcade Employee (`debaucheryville_npc_arcade_employee_01`) | Uses the `cabinet_reset` remote to send them back in after a fight. They call him the Producer |
| Token Attendant (`debaucheryville_npc_arcade_token_attendant_01`) | Sells the three tokens that release them and treats the beating as hospitality |
| Twitchy Hacker Types | Know the board is a bootleg. Say nothing. Tip-funded |

---

## ✅ Validation Checklist
| Requirement | Status |
|-------------|--------|
| Funny, unique name (checked against all existing names) | ✅ Repo-grepped `design/`, `game/assets/data/`, `docs/`: villain, move, passive, item and achievement names have zero hits. ("Palette swap" appears only as an art-pipeline term.) Cross-check against the parallel Frogger / Kebab Kombat profiles is pending with the lead |
| Racket grounded in the city's satirized culture/underbelly | ✅ Counterfeit / knockoff tourist trade, token money sink |
| Full combat spec (stats, moves, phases, immunities, rewards) | ✅ (Approved 2026-11-09; ticket amount approved in the review round) |
| Statuses from master list only (or author-approved new ones) | ✅ Gains Bro, Confused, Embarrassed; Distracted-style skip per PRD §6.8 |
| All prices in SOVS; fight payouts in arcade tickets | ✅ |
| Pre/mid/post-battle dialogue written, full-strength satire | ✅ |
| No moralizing, no reality-check function, no redemption arc | ✅ |
| Bros never afraid, never self-aware — annoyed and overconfident | ✅ |
| Sprite notes for artists (battle + overworld + telegraph) | ✅ |
| Author approval on: new mechanics/gimmicks, stat numbers, story ties | ✅ Approved 2026-11-09 (stats, ally-count AI gate, ally-KO trigger, Second Thoughts, encounter table, new item + achievement); ticket amount approved in the review round |

---

## 🔧 Development Status
- **Status**: Approved 2026-11-09 (ticket amount awaiting author ruling)
- **Canon level**: Approved
- **Profile File Location**: `design/worlds/debaucheryville/villains/absinthe_arcade/street_fighter_identity_crisis/player_two_palette_swap.md`
- **Registered In**: `game/assets/data/enemies/debaucheryville_enemies.json` (`player_two_palette_swap`), 2026-11-10
- **Sprite Sheet**: not yet specced

## 📜 Revision History
| Date | Change | Author |
|------|--------|--------|
| 2026-11-02 | Initial profile (agent draft for author review, per the 2026-11-02 cabinets-are-battles ruling) | Claude (agent) |
| 2026-11-09 | Applied author rulings: SOVS payout replaced with tickets (PROPOSED); cabinet cost 3 tokens; weighted encounter table ruled; AI triggers, Second Thoughts, stats, drops, item, achievement Approved | Claude (per author rulings 2026-11-09) |
| 2026-11-09 | Review-round author rulings applied: 4-ticket-per-Swap payout Approved (labels flipped from PROPOSED to Approved 2026-11-09) | Claude (per author rulings 2026-11-09) |
