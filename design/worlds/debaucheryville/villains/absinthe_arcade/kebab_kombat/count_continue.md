# Villain Profile: Count Continue

*"CONTINUE? NINE... EIGHT... I'll take that as a yes."*

> ⚠ AUTHOR-REVIEW: The cabinets-release-villains ruling (2026-11-02) is canon. Author rulings
> 2026-11-09: Count Continue is the **only** villain with a paid CONTINUE revive, and it is
> **Approved 2026-11-09** (enemy revive charged to the party wallet). Wallet theft is struck from
> him: he charges for continues and takes nothing else. Stats, XP, drops, the new item, the
> achievement and the Kebab Kombat ladder are **Approved 2026-11-09**. The "wallet can't cover
> it" rule and the ticket payout are **PROPOSED — needs author ruling**.

## 📋 Villain Identity
- **Villain ID**: `debaucheryville_villain_count_continue_01`
- **Display Name**: Count Continue
- **Tier**: Minor Villain (cabinet support)
- **Primary Location**: Absinthe Arcade (`debaucheryville_clocktower_arcade_01`), node `aa_node_main_cabinet_loop`, released by the Kebab Kombat cabinet (`kebab_kombat`), Debaucheryville
- **Associated Quest/Arc**: None. Optional, token-triggered cabinet content.
- **Encounter Type**: Repeatable (token-triggered; Kebab Kombat costs 4 Absinthe Arcade Tokens per play = 4 SOVS, ruled 2026-11-09), Optional

---

## 🎭 Core Concept

### The Racket
Count Continue is the cabinet's announcer: a giant digitized head floating in the upper corner of the screen, voice pitched down two octaves, permed, wearing a headset mic from a 1994 sound booth. He says KEBAB KOMBAT the way a priest says amen. He says FINISH HIM to whoever is winning, because whoever is winning is about to pay.

He is the arcade business model with a face. The fight is free once you've paid the four tokens. *Staying in* the fight costs SOVS. When one of his fighters goes down, he starts the countdown (CONTINUE? 9... 8...), counts faster than anyone can read, charges the continue to the bros' wallet, and puts his fighter back on its feet. The bros paid to fight the ninjas, and now they're paying for the ninjas' second life too. Nothing in the cabinet's coin box has ever left the cabinet.

### What Bros Believe
- **Lord Pilsner** believes the voice said his name. It said "Kebab Kombat." He maintains it said Kebab Kombat *in the tone it would use for his name*. He considers every continue a "VIP extension of the night" and is proud to fund it.
- **Chadwick** sees a fellow broadcaster and keeps trying to co-host. He believes the Count's EXTRA CRISPY! pop-ups are reaction content and that the two of them have chemistry.
- **Bradley** is convinced every FINISH HIM! is addressed to him personally, as encouragement. It is addressed to the man about to finish him.

### The Comedy Gap
Three men who think the hype man respects them are being billed by the hype man in real time. The satire targets: the tourist-trap arcade's coin-drop economics; the continue screen as a business model; the bros' belief that money spent is proof of status. They watch their wallet drain to revive their enemies and call it investing in the run.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Late 30s at the 1994 photo shoot. Permanently late 30s, permanently 1994 |
| Build | No body. A head, a neck stump fading to scanlines, a headset mic |
| Height | Fills the upper-right third of the battle screen. Looming by default |
| Energy | Game-show host repossessing your car |

### Costume & Distinguishing Features
- **The head**: Big perm, wraparound sports sunglasses pushed up on the forehead, a thin moustache that took effort, a headset mic with a foam windscreen that has seen things. Digitized photo texture with a green chroma-key fringe, like the rest of the Kebab Kombat roster.
- **Accessories**: A coin-slot glow under the chin, and a floating CONTINUE? counter that hangs beside him whenever a fighter is down.
- **Tic**: He licks his teeth after every announcement, the way a man does when he's tasted money.
- **The corner pop-up**: For EXTRA CRISPY! he shrinks to a tiny head and slides in from the bottom-right corner, says the line in falsetto, and slides out. It's the 90s secret-pop-up gag reassigned to humiliation.

### Sprite Notes
- **Battle sprite**: Front-view static (EarthBound style), positioned top-right of the enemy row, larger than any other enemy sprite on the stage, floating with a slow 4-frame bob. Background: the Grease Pit (see `condiment_clan_ninja.md`).
- **Extra frames**: Corner pop-up (small head, 3 frames in, 2 frames out); "talking" mouth loop (2 frames); Attract Mode loop (sunglasses down, head rotates in a slow, smug demo spin).
- **Telegraph (CONTINUE?)**: The countdown number appears beside his head one full turn before the continue resolves, in a huge 8-bit font, ticking 9 → 8 → 7 audibly during that turn. The coin-slot under his chin starts glowing gold. The tell has to be readable from across a room.
- **Overworld sprite**: None. On the cabinet's attract screen he is the face over the KEBAB KOMBAT title card.
- **Palette-swap budget**: None. There is one Count.

---

## 🧠 Personality & Dialogue

### Archetype
**The House, Announcing Itself**: Count Continue believes in exactly one thing: the next coin. He has the confidence of a man who has never lost a single round, because he has never fought one. He narrates the fight in capitals, flatters whoever is about to pay, and treats every bro KO as a sales opportunity. He isn't evil. He's on commission.

### Pre-Battle Dialogue
*Trigger: KK-2 or KK-3 rung begins. The head blooms into the top corner of the screen as the fighters climb out.*
> **Count Continue**: "KEBAB... KOMBAT!"
> **Lord Pilsner**: "He said my name."
> **Chadwick**: "He said 'Kebab Kombat,' Pils."
> **Lord Pilsner**: "In the tone he'd use for my name."
> **Count Continue**: "Welcome, warriors. Your credits have been accepted. All of them."
> **Bradley**: "Bro's got no body. I'll go easy on the face."
> **Count Continue**: "That's the spirit. Remember it when the counter starts."

### Mid-Battle Barks
| Trigger | Line |
|---------|------|
| Fight start | "ROUND ONE. Also round two. We'll see how your wallet feels about round three." |
| Ally Clan Ninja KO'd | "Ooh. That's a continue situation." |
| Below 50% HP | "You are damaging the house. The house does not get damaged. The house gets paid." |
| Big-move telegraph | "CONTINUE? NINE... EIGHT... I'll take that as a yes." |
| Continue resolves | "Payment received. Please enjoy your opponent, again." |
| "FINISH HIM!" cast | "FINISH HIM!" *(Bradley, every time: "On it.")* |
| Initials Entered lands | "NEW HIGH SCORE! Initials: D. A. D." |
| Bro reaction (Initials Entered) | **Lord Pilsner**: "Dad. As in daddy. The machine knows." |
| EXTRA CRISPY! lands (Embarrassed) | *(falsetto, corner pop-up)* "EXTRA CRISPY!" |
| Bro reaction (EXTRA CRISPY!) | **Chadwick**: "That's our bit now. We have a bit. Clip it." |
| Bro gets KO'd | "One player down. Two credits remaining. Do the math. I already did." |
| Bro reaction (continue charged) | **Bradley**: "Whatever, bro. You can't put a price on a rematch." **Count Continue**: "I just did." |

### Defeat Dialogue
> **Count Continue** (sunglasses dropping onto his nose, head shrinking into the corner): "GAME OVER... for me. Thank you for playing."
> **Count Continue**: "Your continues were non-transferable. Please insert another token to lose to me properly."

### Post-Defeat Presence (If Any)
He reappears on the Kebab Kombat attract screen seconds later, mid-spin, announcing the title to an empty aisle. If the bros examine the cabinet after beating him, the screen reads **CREDITS: 0**, whatever they put in. No redemption arc. He was never in the room.

---

## ⚔️ Combat Specification

> **Approved 2026-11-09.** Values calibrated against the Feral Segway Tourist band (HP 28 / Off 6 / Def 3 / Spd 6). Count Continue is a support: tankier than a ninja, barely hits, high Speed so his buffs land before the bros act.

### Core Stats
| Stat | Value | Notes |
|------|-------|-------|
| **HP** | 34 | Rolling meter applies |
| **SP** | 20 | FINISH HIM! 4 SP; CONTINUE? 8 SP |
| **Offense** | 4 | He has no arms. He has opinions |
| **Defense** | 4 | |
| **Speed** | 11 | Acts first. Announcers always talk first |
| **Charm** | 9 | Highest on the Kombat stage; drives his Social moves |
| **Luck** | 6 | The house |
| **Grit** | 3 | |

### Move List (weighted-random AI)
| Move | Type | Effect | Status Inflicted | Weight / Condition | Telegraphed? |
|------|------|--------|------------------|--------------------|--------------|
| "FINISH HIM!" | Gimmick (ally buff) | One ally gains **Hardcore Gamer** (+2 Speed, +1 Crit chance, −1 HP/turn, 2 turns). If Shish Kahn is on the field and Kebality is off cooldown, this call starts the Kebality wind-up instead (see `shish_kahn.md`). Costs 4 SP | Hardcore Gamer (ally) | 35% / always | No (but it *is* the Kebality telegraph when Kahn is present) |
| "EXTRA CRISPY!" | Social | Corner pop-up. Light Social damage to one bro | Embarrassed (40%) | 30% / always | No |
| Initials Entered | Social | Writes the target's initials onto the high-score table as a three-letter insult of the Count's choosing (DAD, ASS, MOM, TAB, FEE). No HP damage | Tourist Trap Victim (20%); Embarrassed (25%) | 20% / always | No |
| **CONTINUE?** | Gimmick (paid revive) | Resolves at the end of the telegraph turn: revives one KO'd ally at 50% HP and charges 3 SOVS per continue to the party wallet. Max 2 continues per fight. Costs 8 SP. (Paid revive **Approved 2026-11-09**.) **If the wallet can't cover the 3 SOVS (PROPOSED, needs author ruling):** he takes nothing. The counter hits 0, the screen flashes INSUFFICIENT CREDITS, no revive happens, and the bro with the lowest HP gets **Broke AF**. Battle log: "Count Continue declines your card. Chadwick offers to pay in exposure." | Broke AF (only on INSUFFICIENT CREDITS, PROPOSED) | Always, when an ally is KO'd and a continue remains; overrides the weighted pool | **Yes. Countdown 9 → 8 → 7 beside his head for one full turn; coin-slot glows gold.** KO Count Continue during the telegraph turn and the continue never happens |

**Mechanic (Approved 2026-11-09):** CONTINUE? needs two things the battle system may not have yet: (1) an enemy-side revive of a KO'd ally, and (2) an enemy action that charges the continue fee to the party wallet mid-battle. Both are approved. The paid CONTINUE revive exists on Count Continue and nowhere else in the Arcade.

### Phases (Minor Villain: 1)
| Phase | Trigger | Behavior Change |
|-------|---------|-----------------|
| 1 | Fight start | Standard weights. CONTINUE? jumps the queue whenever an ally is down |
| — | Last enemy standing | With no allies left to buff or revive, he cycles EXTRA CRISPY! (50%) and Initials Entered (50%) and barks *"I don't fight. I announce. Announcing is undefeated."* |

### Buffs & Debuffs They Use
- **Self/ally buffs**: Hardcore Gamer on allies (master list); ally revive via CONTINUE?
- **Debuffs on the party**: Embarrassed, Tourist Trap Victim, Broke AF (master list; Broke AF only on INSUFFICIENT CREDITS, PROPOSED). Tourist Trap Victim and Broke AF persist after the battle per their master-list durations. That's the joke: the cabinet follows you to the shop counter.

### Immunities / Resistances / Weaknesses
| Category | Detail |
|----------|--------|
| **Immune to** | Embarrassed (shame needs a neck) and Grease Fingers (no fingers) |
| **Resistant to** | Physical, 25% resist. He hangs in the corner of the screen and most of him is perm |
| **Weak against** | Chadwick's **Cancel Culture** (target skips actions 1 turn): always lands and lasts 2 turns on him. His whole career is one sentence; cancel it and he has nothing. Chadwick considers this a collab |
| **Vulnerability window** | After a CONTINUE? resolves he drops into **Attract Mode** for 1 turn: sunglasses down, smug demo spin, no action, Defense halved |

### Adds / Minions (If Any)
| Minion | Count | Role | Notes |
|--------|-------|------|-------|
| Condiment Clan Ninja | 2 (KK-2) | Grunts | Revived via CONTINUE? at 50% HP, max 2 continues per fight (Approved 2026-11-09) |
| Shish Kahn | 1 (KK-3) | Heavy | FINISH HIM! cues Kahn's Kebality. CONTINUE? can revive Kahn too if the Count outlives him (Approved 2026-11-09; Kahn returns at 50% HP with one arm missing) |

### Arena & Gimmick
The Grease Pit (shared Kebab Kombat stage; see `condiment_clan_ninja.md` for the full description and the fixed resetting ladder, ruled 2026-11-09). No arena hazard. The paid CONTINUE? is this villain's only gimmick.

---

## 💰 Rewards

> **Approved 2026-11-09**, except the ticket amount (**PROPOSED**).

| Reward | Value / Item | Notes |
|--------|--------------|-------|
| **Tickets** | 8 arcade tickets | **PROPOSED, needs author ruling.** Arcade fights pay tickets, not SOVS (ruling 2026-11-09). Redeemable at the Prize Redemption counter built into the bar. Continue fees are never refunded |
| **Clout (XP)** | 14 | |
| **Guaranteed drop** | None | The house does not drop things. The house keeps things |
| **Rare drop** | **Already-Spent Credit**, 8% | **New item, Approved 2026-11-09.** Battle consumable: revives one KO'd bro at 10% HP. Description: *"An arcade token stamped CREDIT 00. It has already been spent. It will be spent again. Lord Pilsner calls it a family heirloom."* |
| **Unlocks** | Nothing on its own. Clears ladder rung KK-2 | |
| **Achievement** | **No Refunds on Continues**. Public: *"Defeat Count Continue after he has charged you for a continue."* Hidden truth: *"Your SOVS were in the cabinet the whole fight. They are still in there. The arcade empties it on Tuesdays."* | Approved 2026-11-09 |

---

## 🔗 Connections
| NPC / Villain | Relationship |
|---------------|--------------|
| Condiment Clan Ninja (`debaucheryville_villain_condiment_clan_ninja_01`) | His talent. He revives them on the bros' money and calls it a staffing solution |
| Shish Kahn (`debaucheryville_villain_shish_kahn_01`) | His headliner. "FINISH HIM!" is the cue for Kebality. They have the relationship of a boxing promoter and the boxer who doesn't read contracts |
| Kebab Kombat cabinet (`kebab_kombat`) / token exchange | Spiritually the same machine as the arcade's token exchange. One takes SOVS in, the other keeps them. No scripted NPC tie proposed |

---

## ✅ Validation Checklist
| Requirement | Status |
|-------------|--------|
| Funny, unique name (checked against all existing names) | ✅ Grepped `design/`, `game/assets/data/`, `docs/`: zero collisions for villain, move, item and achievement names |
| Racket grounded in the city's satirized culture/underbelly | ✅ Tourist-trap arcade coin economics; continue-screen extraction |
| Full combat spec (stats, moves, phases, immunities, rewards) | ✅ (Approved 2026-11-09; INSUFFICIENT CREDITS rule and ticket amount PROPOSED) |
| Statuses from master list only (or author-approved new ones) | ✅ Hardcore Gamer, Embarrassed, Tourist Trap Victim, Broke AF |
| All prices in SOVS; fight payouts in arcade tickets | ✅ |
| Pre/mid/post-battle dialogue written, full-strength satire | ✅ |
| No moralizing, no reality-check function, no redemption arc | ✅ The insults are announcer trash talk; the bros reframe every one as respect |
| Bros never afraid, never self-aware — annoyed and overconfident | ✅ |
| Sprite notes for artists (battle + overworld + telegraph) | ✅ |
| Author approval on: new mechanics/gimmicks, stat numbers, story ties | ✅ Approved 2026-11-09 (paid CONTINUE? revive, stats, drops, new item, achievement), except PROPOSED: INSUFFICIENT CREDITS rule, ticket amount |

---

## 🔧 Development Status
- **Status**: Approved 2026-11-09 (PROPOSED items above awaiting author ruling)
- **Canon Level**: Approved, with PROPOSED exceptions
- **Profile File Location**: `design/worlds/debaucheryville/villains/absinthe_arcade/kebab_kombat/count_continue.md`
- **Registered In**: Not yet. Target `game/assets/data/enemies/debaucheryville_enemies.json` after author approval
- **Sprite Sheet**: Not yet specced (proposed `kk_count_continue.png`)

## 📜 Revision History
| Date | Change | Author |
|------|--------|--------|
| 2026-11-02 | Initial profile (Kebab Kombat cabinet villain roster, per author ruling 2026-11-02) | Claude draft for machsheltie |
| 2026-11-09 | Applied author rulings: paid CONTINUE? kept and Approved (only villain with it); wallet theft struck (INSUFFICIENT CREDITS rule, PROPOSED); SOVS payout replaced with tickets (PROPOSED); cabinet cost 4 tokens; ladder ruled; stats, drops, item, achievement Approved | Claude (per author rulings 2026-11-09) |
