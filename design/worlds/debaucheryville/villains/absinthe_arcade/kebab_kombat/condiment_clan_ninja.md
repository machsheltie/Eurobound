# Villain Profile: Condiment Clan Ninja

*"Garlic or chili. That was not a question."*

> ⚠ AUTHOR-REVIEW: The cabinets-release-villains ruling (2026-11-02) is canon. This villain's
> name, moves, dialogue, stats, drops and encounter placement were a Claude draft. Author
> rulings 2026-11-09: stats, XP, drops, the new item, the achievement, the fixed resetting
> ladder and the MYSTERY BROWN palette-spawn roll are **Approved 2026-11-09**. The SOVS payout is
> replaced with arcade tickets; the ticket amount is **Approved 2026-11-09**
> (review round).

## 📋 Villain Identity
- **Villain ID**: `debaucheryville_villain_condiment_clan_ninja_01`
- **Display Name**: Condiment Clan Ninja. Battle nameplates by palette: **GARLIC**, **CHILI**, and the secret **MYSTERY BROWN**
- **Tier**: Minor Villain (cabinet grunt)
- **Primary Location**: Absinthe Arcade (`debaucheryville_clocktower_arcade_01`), node `aa_node_main_cabinet_loop`, released by the Kebab Kombat cabinet (`kebab_kombat`), Debaucheryville
- **Associated Quest/Arc**: None. Optional, token-triggered cabinet content.
- **Encounter Type**: Repeatable (token-triggered; Kebab Kombat costs 4 Absinthe Arcade Tokens per play = 4 SOVS, ruled 2026-11-09), Optional

---

## 🎭 Core Concept

### The Racket
Kebab Kombat's roster is one actor in one hood, photographed once in a parking lot in 1994 and recoloured until the cabinet had a "cast." The Condiment Clan are that actor. Their job is the question every 3 a.m. kebab counter asks a man who can no longer form words: *garlic or chili?* It has no right answer. The answer is always both, both is extra, and the Clan is very good at extra. They climb out of the screen dripping, interrogate the bros about sauce at fighting-game volume, and then hit them with the answer.

The arcade sells you the same enemy three times and calls it a roster. The Clan doesn't mind. They are paid per appearance, and there is only one of them.

### What Bros Believe
- **Lord Pilsner** believes the cabinet recognized him. He held the high score on a Kebab Kombat machine at a roller rink in 1996 (he did not; that cabinet did not exist), and the Clan is clearly the machine's honour guard, sent out to test whether the legend still has it.
- **Chadwick** thinks they're paid promo performers and keeps asking them to redo the flip because his stream lagged. He rates their choreography a 6, then a 9, then a 4, depending on how the chat is reacting to him.
- **Bradley** thinks the Chili one is mean-mugging him specifically and wants a rematch with a man who doesn't exist.

### The Comedy Gap
Three bros who think they're fighting an elite ninja order are actually fighting a cost-cutting decision. The sharper target is the kebab counter itself: the sauce question is the industry's one real upsell, and these ninjas are that upsell, hyper-competent, mid-air, swinging a skewer on a string. The bros say "both" every single time and every time it's extra.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Indeterminate. The photo shoot was 1994; the actor has aged, the sprite has not |
| Build | Lean, crouched, fighting-stance bounce that never stops, even while talking |
| Height | Average. Exactly the same height in every palette, because it is the same man |
| Energy | Squeeze-bottle menace |

### Costume & Distinguishing Features
- **The hood and wrap**: Classic palette-swap ninja hood and gi. Garlic is off-white with cream trim; Chili is arterial red; Mystery Brown is a colour nobody approved. A paper kebab-shop napkin is tucked into each belt like a sash.
- **Accessories**: A twin holster of squeeze bottles on the hips (the nozzles have crusted closed and been reopened with a fork), and a steel kebab skewer on a length of greasy rope. That is the weapon behind GET IN THE PITA!
- **Digitized tell**: Every frame has the faint green chroma-key fringe of a 1994 photo shoot. When two ninjas stand side by side, the same wrinkle sits in the same place on both sleeves.
- **The bounce**: The idle is the fighting-game bounce, two frames, forever. They keep bouncing through dialogue, through being hit, through defeat.

### Sprite Notes
- **Battle sprite**: Front-view static (EarthBound style) over the cabinet's psychedelic stage background, the **Grease Pit** (see Arena). One base sheet, three palettes: Garlic, Chili, Mystery Brown. Palette-swap budget: **3 palettes, 1 sheet, 0 new frames.** That *is* the joke; do not let anyone draw a second ninja.
- **Digitized look**: Slightly over-sharpened photo texture, posterized to a limited palette, green fringe at the silhouette edge. In the HD-2D build this reads as a flat billboard sprite with a faint scanline shimmer, deliberately lower fidelity than the bros.
- **Emergence**: Climbs out of the Kebab Kombat screen head-first, the CRT glass bulging like a soap bubble, then drops into the bounce. This needs a new cabinet state ("villain emergence"), which `aa_cab_kebab_kombat` does not currently list. Flag for the PNG spec owner.
- **Overworld sprite**: None. They only exist in battle and on the cabinet's attract screen.
- **Telegraph (GET IN THE PITA!)**: One full turn of the skewer-rope twirling overhead in a widening circle, with a squeaky-bottle wind-up SFX. The ninja's bounce stops. It is the only time it stops.

---

## 🧠 Personality & Dialogue

### Archetype
**The Upsell in a Hood**: The Clan has one belief: every customer wants both sauces and does not know it yet. They are not cruel. They are thorough. They talk in clipped, deadpan counter-speak, like a night-shift kebab worker running on four hours of sleep and a vendetta, and they treat combat as a slightly longer version of taking an order. They know they are palette swaps and they are proud of it. Consistency is a brand.

### Pre-Battle Dialogue
*Trigger: a bro feeds the cabinet four tokens and presses REGRET. The screen flashes CHOOSE YOUR SAUCE, then two ninjas climb out.*
> **GARLIC**: "Garlic or chili."
> **CHILI**: "That was not a question."
> **Lord Pilsner**: "Both. I was born ordering both."
> **GARLIC**: "Both is extra."
> **Lord Pilsner**: "Gentlemen. I have never once in my life done anything that wasn't extra."
> **Chadwick**: "Can you guys come out of the screen again? Slower? My stream dropped."
> **Bradley**: "Red one's mean-mugging me. Somebody hold my pager."

*Mystery Brown variant (secret palette appears):*
> **MYSTERY BROWN**: "You did not choose me. Nobody chooses me. I arrive."
> **Chadwick**: "Secret character, boys. Chat is going to lose its mind. Both of them."

### Mid-Battle Barks
| Trigger | Line |
|---------|------|
| Fight start | **GARLIC**: "Same guy. Different sauce. Pay attention." |
| Fight start (alt) | **CHILI**: "Your order is up. Your order is us." |
| Below 50% HP | **CHILI**: "You are dripping on my hood. Dripping is my job." |
| Below 50% HP (alt) | **GARLIC**: "Fine. Extra garlic. On the house. The house is your face." |
| Big-move telegraph | **Either**: "GET IN THE PITA!" |
| Bro gets wrapped (Stun lands) | **GARLIC**: "Wrapped. Rolled. Foil on. Next customer." |
| Embarrassed lands (Garlic Breath Spray) | **GARLIC**: "Go flirt with that breath. I'll wait." |
| Sauce Swap used | **CHILI**: "I am Garlic now." **GARLIC**: "I am Chili now." **CHILI**: "Nothing has changed." |
| Bro reaction (wrapped) | **Bradley**: "He grabbed me with a SKEWER on a STRING. Respect. Doing it back." |
| Bro reaction (Embarrassed) | **Chadwick**: "Garlic breath is a personal brand. I'm pivoting." |
| Bro reaction (Sloppy) | **Lord Pilsner**: "Chili in the eye. Classic warrior's handicap. I fight better half-blind." |

### Defeat Dialogue
> **GARLIC** (still bouncing, dissolving into scanlines): "We are a renewable resource. Insert another token."
> **CHILI**: "Next time we come out Mystery Brown. Nobody wants that. You'll get it anyway."

### Post-Defeat Presence (If Any)
They dissolve back into the screen, which immediately shows them bouncing on the attract loop, fully healed, under the words CHOOSE YOUR SAUCE. They are back for the next token. They have no grudge and no memory. Grudges are a premium feature. No redemption arc; nothing to redeem. They are a sprite.

---

## ⚔️ Combat Specification

> **Approved 2026-11-09.** All values below are calibrated against the only shipped Debaucheryville enemy (Feral Segway Tourist: HP 28 / Off 6 / Def 3 / Spd 6 / Luck 2 / XP 12 / 8 SOVS). The Clan is a grunt and sits in that band, faster and more fragile.

### Core Stats (Garlic and Chili share one block; Mystery Brown noted)
| Stat | Value | Notes |
|------|-------|-------|
| **HP** | 26 (Mystery Brown: 32) | Rolling meter applies |
| **SP** | 8 | Pays for GET IN THE PITA! (6 SP) |
| **Offense** | 6 (Mystery Brown: 7) | |
| **Defense** | 3 | |
| **Speed** | 9 | Fastest thing on the Kombat stage; the bounce is load-bearing |
| **Charm** | 2 | Counter staff. Charm was never part of the job |
| **Luck** | 3 | |
| **Grit** | 2 | Crits land easily. They're a photograph |

### Move List (weighted-random AI)
| Move | Type | Effect | Status Inflicted | Weight / Condition | Telegraphed? |
|------|------|--------|------------------|--------------------|--------------|
| Squeeze Strike | Physical | Light single-target hit: a squeeze-bottle jab to the sternum | — | 40% / always | No |
| Sauce Spray (palette-specific, see below) | Social (Garlic) / Physical (Chili, Mystery Brown) | Light damage plus palette status | See below | 30% / always | No |
| Sauce Swap | Gimmick | Two Clan ninjas trade palettes. Each clears its own negative statuses. Battle log: *"GARLIC is CHILI now. Nothing has changed."* If only one ninja is alive, it swaps with itself; the log says so and nothing happens | — (self-cleanse) | 15% / only when self has a negative status | No |
| **GET IN THE PITA!** | Physical / Gimmick | The skewer-rope spears one bro and reels him into a pita. Moderate damage, target wrapped (Stun, 1 turn) | Stun (1 turn) + Grease Fingers | 15% / max once every 3 rounds per ninja; costs 6 SP | **Yes. One full turn of overhead skewer-twirl; the bounce stops** |

**Sauce Spray by palette:**
| Palette | Move name | Effect |
|---------|-----------|--------|
| GARLIC | Garlic Breath Spray | Light Social damage; **Embarrassed** 35%. Battle log: *"Chadwick's next pickup line now arrives three seconds before he does."* |
| CHILI | Chili Mist | Light Physical damage; **Sloppy** 30% (chili in the eyes) |
| MYSTERY BROWN | The Brown Note | Light Physical damage; **Food Poisoning** 40%. Battle log: *"Nobody asked what the brown one was. Lord Pilsner's intestines are asking now."* |

### Phases (Minor Villain: 1)
| Phase | Trigger | Behavior Change |
|-------|---------|-----------------|
| 1 | Fight start | Standard weights above. With two ninjas alive, the AI favours the same target for GET IN THE PITA! (both ninjas spear the same bro if both are off cooldown; the second spear on a wrapped bro only adds damage, Stun does not stack) |

### Buffs & Debuffs They Use
- **Self/ally buffs**: Sauce Swap (self-cleanse of negative statuses). No stat buffs. Count Continue's "FINISH HIM!" can grant them Hardcore Gamer (see `count_continue.md`).
- **Debuffs on the party**: Embarrassed, Sloppy, Grease Fingers, Food Poisoning (master list); Stun (1 turn) as used throughout the Combat Bible (Beer Belly Bash, Bouncer Breaker).

### Immunities / Resistances / Weaknesses
| Category | Detail |
|----------|--------|
| **Immune to** | Grease Fingers. They *are* the grease |
| **Resistant to** | Food Poisoning (75% resist). They've eaten here |
| **Weak against** | Light/flash attacks: Chadwick's **Selfie Smite**, Lord Pilsner's **Flash of the Red Solo Cup**. +50% damage and the blind always lands, because a 1994 digitized photo overexposes into a white smear when you point a ring light at it. Chadwick takes credit for "discovering" this every fight |
| **Vulnerability window** | The turn after GET IN THE PITA! resolves, the ninja is reeling its rope back in: Defense halved for 1 turn |

### Adds / Minions (If Any)
None of its own. The Clan *are* the adds for Count Continue and Shish Kahn encounters.

### Arena & Gimmick
**Arena: The Grease Pit.** This is the cabinet's stage background, rendered as the battle backdrop: a sunken pit lined with upright rotating skewers, a foil-sheet horizon, one buzzing sodium parking-lot lamp (the actual 1994 digitization site), and a heat-lamp orange sky. Background only, no hazard proposed.

**Encounter placement (shared Kebab Kombat ladder; fixed resetting ladder ruled 2026-11-09):** The token-triggered fight works like the cabinet's fighting-game ladder. Each play (4 tokens) runs the next rung:
| Rung | Name | Roster |
|------|------|--------|
| KK-1 | Sauce Rung | 2 × Condiment Clan Ninja (GARLIC + CHILI) |
| KK-2 | Continue Rung | 2 × Condiment Clan Ninja + Count Continue |
| KK-3 | Spit Rung | Shish Kahn + Count Continue |
The ladder resets after KK-3 is won. On a party wipe the bros are spat out of the cabinet onto the arcade carpet, the tokens are gone, and the rung resets to KK-1.

**Secret palette (palette-spawn roll Approved 2026-11-09):** In any rung, each Clan ninja slot has a 5% chance to spawn as MYSTERY BROWN instead. This parodies the secret hidden ninja of 90s gore fighters. Existing spawn tech may not support per-slot variant rolls; flag for engine.

---

## 💰 Rewards

> **Approved 2026-11-09**, including the ticket amount (review round). Token economics: a Kebab Kombat play costs 4 tokens = 4 SOVS (ruled 2026-11-09). Fights pay arcade tickets, not SOVS, and Count Continue's paid continues pull the bros' SOVS further down on KK-2/KK-3.

| Reward | Value / Item | Notes |
|--------|--------------|-------|
| **Tickets** | 5 arcade tickets per ninja (Mystery Brown: 10) | **Approved 2026-11-09** (review round). Arcade fights pay tickets, not SOVS (ruling 2026-11-09). Redeemable at the Prize Redemption counter built into the bar |
| **Clout (XP)** | 10 per ninja (Mystery Brown: 18) | Just under Feral Segway Tourist's 12 |
| **Guaranteed drop** | None | The squeeze bottles go back in the cabinet. They are inventory |
| **Common drop** | `lukewarm_kebab` (existing engine item), 25% | Reuses the existing Debaucheryville drop, no new item |
| **Rare drop** | **Squeeze-Bottle Kunai**, 10% (Mystery Brown: 35%) | **New item, Approved 2026-11-09.** Battle consumable: thrown at one enemy for light damage plus a 50% chance of Grease Fingers. Description: *"A ninja's squeeze bottle, sharpened at the nozzle. Contains garlic, chili, or a third thing. The label was the first casualty."* |
| **Unlocks** | Nothing on its own. Clears ladder rung KK-1 | |
| **Achievement** | **Same Guy, Different Sauce**. Public: *"Defeat a Condiment Clan Ninja in all three palettes."* Hidden truth: *"It was the same man all three times. He was paid once, in 1994, in sauce."* | Approved 2026-11-09 |

---

## 🔗 Connections
| NPC / Villain | Relationship |
|---------------|--------------|
| Count Continue (`debaucheryville_villain_count_continue_01`) | Their announcer and their revive button. Every time a ninja drops, Count Continue spends the bros' SOVS to bring it back. The Clan considers this employee benefits |
| Shish Kahn (`debaucheryville_villain_shish_kahn_01`) | The cabinet's sub-boss. The Clan are his sauce: technically his staff, spiritually his condiments. They don't fight together in the proposed ladder; they share the stage |
| Kebab Kombat cabinet (`kebab_kombat`) | Their home sprite sheet. They climb out of it and dissolve back into it |
| Frogger: Existential Edition / Street Fighter: Identity Crisis villains | No tie. Separate cabinets, separate photo shoots |

---

## ✅ Validation Checklist
| Requirement | Status |
|-------------|--------|
| Funny, unique name (checked against all existing names) | ✅ Grepped `design/`, `game/assets/data/`, `docs/` for every villain, move, item and achievement name: zero collisions |
| Racket grounded in the city's satirized culture/underbelly | ✅ 3 a.m. kebab sauce upsell plus tourist-trap cabinet cost-cutting |
| Full combat spec (stats, moves, phases, immunities, rewards) | ✅ (Approved 2026-11-09; ticket amount approved in the review round) |
| Statuses from master list only (or author-approved new ones) | ✅ Embarrassed, Sloppy, Grease Fingers, Food Poisoning, Hardcore Gamer; Stun as used in the Combat Bible |
| All prices in SOVS; fight payouts in arcade tickets | ✅ |
| Pre/mid/post-battle dialogue written, full-strength satire | ✅ |
| No moralizing, no reality-check function, no redemption arc | ✅ |
| Bros never afraid, never self-aware — annoyed and overconfident | ✅ |
| Sprite notes for artists (battle + overworld + telegraph) | ✅ |
| Author approval on: new mechanics/gimmicks, stat numbers, story ties | ✅ Approved 2026-11-09 (stats, drops, new item, achievement, ladder, secret-palette spawn roll); ticket amount approved in the review round |

---

## 🔧 Development Status
- **Status**: Approved 2026-11-09 (ticket amount approved in the review round, 2026-11-09)
- **Canon Level**: Approved (the existence of cabinet villains is Established, per the author ruling of 2026-11-02; this roster was approved 2026-11-09, ticket amount approved in the review round)
- **Profile File Location**: `design/worlds/debaucheryville/villains/absinthe_arcade/kebab_kombat/condiment_clan_ninja.md`
- **Registered In**: `game/assets/data/enemies/debaucheryville_enemies.json` (`condiment_clan_ninja`), 2026-11-10
- **Sprite Sheet**: Not yet specced (proposed `kk_condiment_clan_ninja.png`, 1 sheet + 3 palettes)

## 📜 Revision History
| Date | Change | Author |
|------|--------|--------|
| 2026-11-02 | Initial profile (Kebab Kombat cabinet villain roster, per author ruling 2026-11-02) | Claude draft for machsheltie |
| 2026-11-09 | Applied author rulings: SOVS payout replaced with tickets (PROPOSED); cabinet cost 4 tokens; fixed resetting ladder ruled; palette-spawn roll, stats, drops, item, achievement Approved | Claude (per author rulings 2026-11-09) |
| 2026-11-09 | Review-round author rulings applied: 5-ticket payout (Mystery Brown 10) Approved (labels flipped from PROPOSED to Approved 2026-11-09) | Claude (per author rulings 2026-11-09) |
