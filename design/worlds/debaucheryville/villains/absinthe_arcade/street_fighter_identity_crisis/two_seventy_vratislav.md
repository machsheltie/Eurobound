# Villain Profile: Two-Seventy Vratislav

*"My special move requires a full rotation of the stick. I have never once finished the rotation."*

## 📋 Villain Identity
- **Villain ID**: `debaucheryville_villain_two_seventy_vratislav_01`
- **Display Name**: Two-Seventy Vratislav
- **Tier**: Minor Villain
- **Primary Location**: Absinthe Arcade (`debaucheryville_clocktower_arcade_01`), node `aa_node_main_cabinet_loop`, released by the Street Fighter: Identity Crisis cabinet (`street_fighter_identity_crisis`)
- **Associated Quest/Arc**: None
- **Encounter Type**: Optional, Repeatable (token-triggered, 1 Absinthe Arcade Token per release under the current spec; per-cabinet cost is still open with the author)
- **Fight role**: **Bruiser / heavy**, with a one-time **Leech** desperation move. He's slow and tanky, hits hard on a telegraph, changes fighting style halfway through, and goes for the party wallet when he's losing.

---

## 🎭 Core Concept

### The Racket
Vratislav is the cabinet's big-body grappler, baby-oiled and championship-belted, and named after the angle where he always stops. His super needs a full 360-degree motion on the stick. Every time, he gets to two-seventy, stops, and reconsiders who he is as a fighter. He's still the most expensive thing in the machine. When he's losing he runs the oldest arcade con there is. The CONTINUE countdown starts, and somebody's SOVS go into the slot so he can keep fighting. The bros think they're tipping a legend.

### What Bros Believe
That the biggest man in the Arcade came out specifically because he heard Bradley was in the building. That his grapple is a sign of respect between big men. That the SOVS he lifts from them at the CONTINUE screen is a cover charge ("means it's exclusive, bro") or a tip they chose to give.

### The Comedy Gap
He's a man who can't commit to the move that defines him, fighting three men who've committed to a bender their bodies can't finish. Neither side gets all the way around. He takes their money for the privilege of continuing, and they thank him. Satire targets: the arcade continue-screen money grab as a tourist-trap tax, the "authentic underground" fight experience sold by the token, and three 39-year-old bodies trying to grapple like it's senior year.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | 40s, oiled until it doesn't matter |
| Build | Barrel chest, enormous forearms, tiny ankles. He moves like a wardrobe being walked across a room |
| Height | Looming. The cabinet he climbed out of is visibly shorter than him |
| Energy | Gentle, enormous, indecisive |

### Costume & Distinguishing Features
- **Wrestling singlet, high-cut, in faded cabinet-art red**: glistening with oil that drips onto the arcade floor tiles and leaves a slick under the battle sprite.
- **Accessories**: A championship belt whose center plate is a cracked joystick base with the ball-top missing. Knee pads on his elbows; he moved them during an earlier identity crisis. A tiny wrist sweatband on one wrist only.
- **Tell**: He traces circles in the air with one finger and stops every time at the same point, about three-quarters of the way around.
- **Visual element**: A curved **270°** arc floats over his head like a halo that ran out of budget.

### Sprite Notes
- **Battle sprite**: front-view static (EarthBound style) over the psychedelic background, 1–2 frame idle (chest breathing, oil shimmer). He's the largest sprite in the Identity Crisis set and should fill most of the enemy row height. Phase 2 variant: same sprite with one fireball-practice glove overlay and a confused glance.
- **Release animation**: the shared Identity Crisis cabinet exit, with one exception. He doesn't fit through the screen, so the whole cabinet tilts forward and he unfolds out of it in segments.
- **Overworld**: none. He only exists inside the encounter.
- **Big-move telegraph (The Full Three-Sixty)**: the 270° arc over his head fills in segment by segment through the telegraph round and stops at three-quarters. He turns slowly in place, and the battle log ticks the motion one direction at a time. On resolve the arc snaps shut for one frame (the only time it closes), and then he's dizzy.
- **CONTINUE countdown (Leech move)**: a full-screen arcade CONTINUE? overlay with a countdown (9 → 0) laid over the battle background for about one second. Then a coin-slot SFX.

---

## 🧠 Personality & Dialogue

### Archetype
**The Uncommitted Grappler.** A gentle giant with the strongest move in the cabinet and no ability to finish it. He wants to be held in high regard and, honestly, to hold people. Halfway through every fight he decides he's actually a fireball character, a style he's watched one video about. He's funny because the menace is real (the hug does hurt), and the indecision is real, and he's totally at peace with both.

### Pre-Battle Dialogue
*A token drops. The cabinet groans and tilts forward. He unfolds out of it in sections:*
> VRATISLAV: "I am Two-Seventy Vratislav. I am a grappler. Most days. Today I am still deciding."
> BRADLEY: "FINALLY. A big boy. I have been waiting this entire trip for a big boy."
> VRATISLAV: "My special move needs a full rotation of the stick. I have never once finished the rotation."
> LORD PILSNER: "A man who knows his limits. I shall teach him to forget them, as I have forgotten mine."
> CHADWICK: "He oiled up, bro. He oiled up FOR US. Arcade's a nine. Pending the hug."
> VRATISLAV: *(opening his arms)* "Come. Let us be held."

### Mid-Battle Barks
| Trigger | Line |
|---------|------|
| Fight start | "FIGHT. Or grapple. I will know which when I am holding you." |
| Below 50% HP (style change) | "New plan. I am a fireball man now. I have watched one video about it." |
| Big-move telegraph (The Full Three-Sixty) | "Back... down-back... down... down-forward... forward... hmm. Let me think about up." |
| Bro gets KO'd / status lands (Grease Fingers) | "Now you are slippery also. We are brothers in the oil." |
| Desperation (CONTINUE?) | "CONTINUE? Nine... eight... somebody's wallet will continue for me." |
| The Full Three-Sixty lands | "Two-seventy. Again. It is enough. It is always enough." |

### Bro Reaction Barks (battle-log / party lines)
| Trigger | Line |
|---------|------|
| Bradley takes Hug of Undeclared Intent | "My lower back just did a combo on its own. That's fine. That's a gym thing." |
| Lord Pilsner takes Lariat, Probably | "That is not my knee. That is a war wound. Spring break, '98. Do not ask about it." |
| Chadwick takes Grease Fingers | "Bro, my hands are SO moisturized right now. This is a skincare win." |
| CONTINUE? steals SOVS | CHADWICK: "That's a cover charge, bro. Means it's exclusive." / BRADLEY: "Tip the big man. Respect." |

### Defeat Dialogue
> "I did not lose. I completed a different, shorter circle. Here. Your SOVS. I was holding them. Holding is my gift."

### Post-Defeat Presence (If Any)
He folds himself back into the cabinet, which tilts upright again. On later tokens he greets the bros with an update: "Previously: two-seventy. Today: two-seventy-one. Progress." He never reaches 360 and he never will. He has no arc and wants none.

---

## ⚔️ Combat Specification

> **PROPOSED — needs author ruling.** Every number in this section (stats, multipliers, weights, durations, the SOVS steal) is a proposal. Benchmarked against Feral Segway Tourist (HP 28 / OFF 6 / DEF 3 / SPD 6 / LCK 2 / 12 XP / 8 gold). He's the cabinet's heavy draw, with about twice the Tourist's HP.

### Core Stats
| Stat | Value | Notes |
|------|-------|-------|
| **HP** | 54 | Heaviest of the three Identity Crisis villains |
| **SP** | N/A | Engine enemy schema has no SP field |
| **Offense** | 9 | |
| **Defense** | 6 | |
| **Speed** | 2 | Acts last nearly every round. The bros get to set up before every telegraph |
| **Charm** | 1 | Not in the engine schema yet |
| **Luck** | 2 | |
| **Grit** | 8 | Hard to crit, except during the dizzy window (see below). Not in the engine schema yet |

### Move List (data-driven weighted-random AI)
| Move | Type | Effect | Status Inflicted | Weight / Condition | Telegraphed? |
|------|------|--------|------------------|--------------------|--------------|
| **Hug of Undeclared Intent** | Physical (grab) | 1.2× single target. He holds the bro "until he knows what this is" | **Grease Fingers** (−2 accuracy steps, tech items locked; 4 turns or washed) | 45% / phase 1 | No |
| **Lariat, Probably** | AoE Physical | 0.6× to all three bros. He spins with arms out and doesn't finish the spin either | — | 35% / phase 1 (→ 30% phase 2) | No |
| **A Fireball He Has Never Practiced** | Special (projectile) | 1.6× single target at a −3 accuracy-step penalty (about 68% to hit before evasion). It's big when it lands, and it usually doesn't | — | 0% phase 1 / 50% phase 2 (replaces Hug) | No |
| **CONTINUE? Nine... Eight...** | Gimmick (Leech) | Steals up to 10 SOVS from the party wallet (less if the wallet holds less) and heals himself 30% max HP. Stolen SOVS are returned in full on his defeat and kept if the party loses or flees | — | **Once per fight** / HP < 25% (replaces his next action) | No (the CONTINUE overlay plays as it resolves) |
| **The Full Three-Sixty** | Physical (big move) | 2.0× single target (the highest-HP bro), and the target is spun into **Sloppy** | **Sloppy** (−3 accuracy steps, 15% friendly fire; 2 turns) | Every 4th round (round 4, 8…), both phases | **Yes**: a full telegraph round. The 270° arc fills, the log ticks the motion, and he reconsiders "up" |

**Counterplay already in the system:** a bro who **Braces** during the telegraph round halves The Full Three-Sixty (standard Brace). If Vratislav is **Embarrassed** when the move would resolve, he abandons it at ninety degrees and the move fizzles. Bark: "No. Not in front of people." That uses the existing `target_has_status` gate on himself.

### Phases (Minor Villain: 3 phases)
| Phase | Trigger | Behavior Change |
|-------|---------|-----------------|
| 1 | Fight start | Grappler: Hug / Lariat / Full Three-Sixty table |
| 2 | HP < 50% | **Style change (identity crisis):** announces he's a fireball character now. A Fireball He Has Never Practiced replaces Hug of Undeclared Intent. Lariat stays. This swap is the cabinet's "remaps his own moves mid-combo" twist, done entirely through the existing phase-script system |
| 3 | HP < 25% | Desperation: CONTINUE? Nine... Eight... fires once, then he goes back to the phase 2 table |

### Buffs & Debuffs They Use
- **Self/ally buffs**: 30% self-heal via CONTINUE?. He receives Gains Bro from Super Turbo Hyper Jarmila when she's in the group.
- **Debuffs on the party**: Grease Fingers (his oil), Sloppy (the spin). Both are on the master list.

### Immunities / Resistances / Weaknesses
| Category | Detail |
|----------|--------|
| **Immune to** | **Grease Fingers**. He's the source |
| **Resistant to** | Physical damage, a flat 15% (oil + bulk); Stun-type effects (e.g. Beer Belly Bash, Beeramid Blast stun), 50% resist |
| **Weak against** | **Embarrassed** (cancels The Full Three-Sixty, as above). He's also weak to being out-hugged: Bradley's *Wristband Check* taunt makes Vratislav target Bradley, which Vratislav treats as consent and Bradley treats as a rivalry. That's taunt behavior, not new mechanics |
| **Vulnerability window** | After The Full Three-Sixty resolves he's dizzy for 1 turn. He skips his next action and his Grit drops to 0 until his next turn (uses the PRD §6.8 "Distracted for 1 turn" convention). This is the SMAAAASH window |

### Adds / Minions (If Any)
| Minion | Count | Role | Notes |
|--------|-------|------|-------|
| Super Turbo Hyper Jarmila | 1 (in the "Vratislav + Jarmila" group) | Support | She buffs and heals him. Killing her first is the intended read. No re-summon |

### Arena & Gimmick
The fight happens in place at `aa_node_main_cabinet_loop`, using the shared Identity Crisis battle background. His oil leaves a visual slick under the enemy row (cosmetic; the mechanical effect is just his Grease Fingers move). The CONTINUE? overlay is a brief full-screen visual on a once-per-fight move.

**Economy flag (NEEDS AUTHOR RULING):** CONTINUE? takes SOVS directly out of the party wallet in battle. The PRD's Leech archetype (Pickpocket Pair, "steals Sovs") suggests that's an existing enemy behavior class, but no Leech enemy is implemented yet, so the author should confirm the amount and the return-on-defeat rule.

He participates in the cabinet-wide **Second Thoughts** re-roll proposal (see `player_two_palette_swap.md` → Arena & Gimmick, **NEEDS AUTHOR RULING**). His flavor version: "Vratislav uses Hug of Undeclared Intent! ...He has decided it is a lariat. Probably." Encounter table proposal also lives in that profile.

---

## 💰 Rewards

> **PROPOSED — needs author ruling.** All values and every new item below.

| Reward | Value / Item | Notes |
|--------|--------------|-------|
| **SOVS** | 0 SOVS, plus the return of any SOVS stolen by CONTINUE? | Same farming flag as the other Identity Crisis villains (1 SOV per token, repeatable). Alternative: 2 SOVS, since he's the rarest draw (20% of tokens under the proposed table) |
| **Clout (XP)** | 28 | A bit over twice Feral Segway Tourist, matching his HP |
| **Guaranteed drop** | **Absinthe Arcade Token** ×1 (existing `item_absinthe_arcade_token`) | Beating the heavy refunds the token. It's still net zero for the house |
| **Rare drop** | **Two-Seventy Wrist Brace** (PROPOSED new item), 8% | Accessory. Proposed: +1 Grit, and the wearer resists Grease Fingers. Item card: "Gets you three-quarters of the way around anything." Needs a `permanent_item_template.md` / item doc if approved |
| **Unlocks** | Shares the cabinet's existing `hacker_respects_adaptation` dialogue unlock on first Identity Crisis win (see Swap profile) | |
| **Achievement** | **Most of the Way Around** (PROPOSED). *Public*: "Survive The Full Three-Sixty." *Hidden truth*: "Nobody has ever survived a 360. You survived a 270." | |

---

## 🔗 Connections
| NPC / Villain | Relationship |
|---------------|--------------|
| Super Turbo Hyper Jarmila | She has promised him a complete rotation "in the next revision" for eleven revisions. He believes her every time |
| Player Two Palette Swap | His warm-up partners in attract mode. He holds them. They tolerate it |
| Arcade Employee (`debaucheryville_npc_arcade_employee_01`) | The only person who can tilt the cabinet back upright after Vratislav folds into it. He does it with the reset remote and a look |
| Token Attendant (`debaucheryville_npc_arcade_token_attendant_01`) | Gets a cut of every CONTINUE?. Calls it "the extended experience" |

---

## ✅ Validation Checklist
| Requirement | Status |
|-------------|--------|
| Funny, unique name (checked against all existing names) | ✅ Repo-grepped: "Vratislav", "Two-Seventy", every move name, "Wrist Brace" and "Most of the Way Around" have zero hits. (I avoided "Insert Coin" because it's already the Maintenance Closet's CRT mirror gag.) Cross-check against parallel cabinet profiles pending with the lead |
| Racket grounded in the city's satirized culture/underbelly | ✅ Continue-screen wallet grab as a tourist tax; token-priced "underground" fight |
| Full combat spec (stats, moves, phases, immunities, rewards) | ✅ (PROPOSED numbers) |
| Statuses from master list only (or author-approved new ones) | ✅ Grease Fingers, Sloppy, Embarrassed (as counterplay), Gains Bro (received); dizzy skip per PRD §6.8 |
| All prices/drops in SOVS | ✅ |
| Pre/mid/post-battle dialogue written, full-strength satire | ✅ |
| No moralizing, no reality-check function, no redemption arc | ✅ |
| Bros never afraid, never self-aware — annoyed and overconfident | ✅ Their bodies break and they file it under gym things and war wounds |
| Sprite notes for artists (battle + overworld + telegraph) | ✅ |
| Author approval on: new mechanics/gimmicks, stat numbers, story ties | ⬜ Pending: stats/rewards, CONTINUE? SOVS steal, Second Thoughts, new item + achievement |

---

## 🔧 Development Status
- **Status**: Drafted
- **Canon level**: Provisional (pending author ruling)
- **Profile File Location**: `design/worlds/debaucheryville/villains/absinthe_arcade/street_fighter_identity_crisis/two_seventy_vratislav.md`
- **Registered In**: Not yet. Target: `game/assets/data/enemies/debaucheryville_enemies.json` (as `two_seventy_vratislav`) after author approval
- **Sprite Sheet**: not yet specced

## 📜 Revision History
| Date | Change | Author |
|------|--------|--------|
| 2026-11-02 | Initial profile (agent draft for author review, per the 2026-11-02 cabinets-are-battles ruling) | Claude (agent) |
