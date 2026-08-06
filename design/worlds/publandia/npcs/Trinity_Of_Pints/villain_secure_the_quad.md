# Villain Profile: SECURE THE QUAD (Dean Cathal Murphy & the Faculty)

*"NOBODY GRADUATES! SECURE THE QUAD!"*

> ⚠ AUTHOR-REVIEW: the encounter's existence, trigger, and battle roster are author-dictated
> (extraction Rulings, Trinity addenda — "BATTLE IS IN," "Dean Cathal + three professors").
> Every combat number, move, phase, and piece of non-canon dialogue below is a Claude draft
> and is flagged for author approval before implementation. This is the first villain profile
> written for the project — no prior stat-block precedent exists to calibrate against, so
> all numbers are first-pass estimates against the Combat Bible's general framework
> (`docs/EUROBOUND_PRD.md` §6), not balanced against any other boss.

<!-- Villain-template mandate: every boss gets a profile at creation (author mandate
2026-08-03). This is a 4-enemy squad encounter, not a single monster — the template's
single-villain sections are adapted below to cover Dean Cathal as the squad leader plus
three professors as a linked Adds table, per Combat Bible §6.8 conventions. -->

## 📋 Villain Identity
- **Villain ID**: `publandia_villain_secure_the_quad_01`
- **Display Name**: Dean Cathal Murphy & the Faculty (battle nameplates: Dean Cathal Murphy,
  Prof. Róisín O'Sullivan, Prof. Cian MacCarthy, Prof. Aisling Byrne)
- **Tier**: Dungeon Miniboss (Publandia — optional Brewery Tour content, not the main-story
  city boss)
- **Primary Location**: The Quad, Trinity of Pints, Publandia
- **Associated Quest/Arc**: `publandia_quest_trinity_graduation_01` — the redesigned Trinity
  of Pints sequence, `design/quests/publandia/brewerytourpublandia.md`
- **Encounter Type**: Mandatory story fight within the (optional) Trinity of Pints brewery
  challenge — the entire Brewery Tour sidequest is optional per the standing side-quest rule,
  but once a player commits to Trinity of Pints, this fight is not skippable; it is the
  direct consequence of the referee-reveal beat, not a separate choice.

---

## 🎭 Core Concept

### The Racket

Dean Cathal Murphy has run Trinity of Pints as a fifteen-year bit — a themed pub cosplaying
a university, played with total commitment and never once broken. THESIS DEFENSE 401 is his
signature closer: a beer pong tournament he wins constantly, using a ball he has quietly
magnetized, with a matching magnet hidden under the table. It is the one piece of dishonesty
in an otherwise scrupulously honest operation (see `npc_cathal_murphy.md` — "he never states
a falsehood"), and it exists purely so the house always wins the tournament that "certifies"
graduation. Tonight the trick shot goes wrong, the ball shatters, the magnet is exposed, and
the referee's ruling strips him of the win in front of his own faculty and every patron in
the room.

### What Bros Believe

That they earned this. Pilsner reads the disqualification as a "critical block" that
literally exploded the Dean's ball on impact; the professors are, to the bros, simply the
last "exam" standing between them and a diploma they're already certain they've passed. None
of the three notice that the man screaming and reaching for a gavel is not part of the
ceremony.

### The Comedy Gap

Dean Cathal has spent fifteen years never breaking character for anyone — hecklers, skeptics,
a man point-blank asking if the accreditation is current. The one thing that breaks him is
being caught cheating and denied even the satisfaction of humiliating the people he cheated
against, because they're too oblivious to feel humiliated. The fight is a fully-committed
academic performer's psychotic break, played at the same total sincerity as everything else
he does — he does not become a different character to fight the bros, he becomes an
*extremely* invested version of the same one.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|---|---|
| Age | Dean Cathal: mid-50s. Professors: 40s (Róisín), 30s (Cian), 20s (Aisling) — per their established venue-doc appearances |
| Build | Dean Cathal: tall, normally stooped, now bolt upright with rage. Professors: unchanged from their teaching appearances. |
| Height | Dean Cathal reads as tallest and loomiest once the jacket comes off. |
| Energy | Dean Cathal: a fifteen-year performance finally overclocking. Professors: visibly reluctant conscripts, there because the Dean called their names, not because they want to be. |

### Costume & Distinguishing Features
- **Dean Cathal**: tweed jacket RIPPED OFF and discarded at the top of the encounter — he
  fights in shirtsleeves and the mortarboard, the one piece of regalia he refuses to remove
  even mid-battle. Ceremonial brass gavel, previously decorative, now a weapon.
- **Prof. Róisín O'Sullivan**: still holding a glass; throws its contents as an attack.
- **Prof. Cian MacCarthy**: fighting with darts pulled from his own robe pocket.
- **Prof. Aisling Byrne**: bodhrán in hand, used as both instrument and improvised shield.
- Accessories: none of the four ever fully commits to "battle mode" cosmetically — they
  fight in their teaching outfits, robes and all, because nobody had time to change.

### Sprite Notes

Battle sprites: front-view static (EarthBound style) over a psychedelic Quad-at-night
background — string lights, fake ivy, a toppled graduation banner. Dean Cathal shares no
frames with his NPC-mode sheet (`trinity_faculty.png`) — this is a dedicated battle sheet.
Palette-swap budget: none: all four keep their established colors from their NPC profiles.
Telegraph animation notes: Dean's big move ("TENURE DENIED") needs a clearly readable
gavel-raise wind-up (minimum 1 full beat) before it lands, per Combat Bible telegraphing
convention.

---

## 🧠 Personality & Dialogue

### Archetype

**The Committed Bit, Overclocked** — Dean Cathal's entire fight persona is the same
fifteen-year performance running one register hotter than it has ever run before. He is not
suddenly a violent man; he is a deeply committed one who has just been denied the one form of
control he actually cares about (winning, on his terms, in front of witnesses), and the
gavel is the closest prop to a weapon his costume already contained. The professors, by
contrast, are visibly not committed to this part — they showed up to teach shot IDs and
rhythm games, not to fight tourists, and their dialogue should carry that reluctance
throughout.

### Pre-Battle Dialogue

*Context: immediately after the referee's ruling and Pilsner's "hand over the bottle opener,
or do we have to take our diplomas by force?"*

> **Dean Cathal**: "NOBODY GRADUATES! SECURE THE QUAD!"

*(canon, verbatim — extraction Rulings, Trinity addendum "BATTLE IS IN")*

> **Prof. Cian MacCarthy** (already reaching for darts, resigned): "He does this. Not often. But he does this."
>
> **Prof. Róisín O'Sullivan** (setting down her glass, then picking it back up as a weapon
> instead): "For the record, I am not paid enough for the SECURE THE QUAD clause."
>
> **Prof. Aisling Byrne** (tuning the bodhrán mid-crisis): "If we're doing this, we're doing
> it in time."

### Mid-Battle Barks

| Trigger | Line |
|---|---|
| Fight start | **Dean Cathal**: "Fifteen years! FIFTEEN YEARS without breaking character, and THIS is what does it!" |
| Below 50% HP (Dean) | **Dean Cathal**: "I HAD A CURRICULUM! I HAD A CURVE! I HAD A GAVEL AND NOW I'M USING IT PROPERLY!" |
| Big-move telegraph (gavel wind-up) | **Dean Cathal**: "TENURE. DENIED." |
| A professor drops out | **Prof. Cian MacCarthy** (clocking off): "That's my contracted hours. Good luck, lads — to both sides, honestly." |
| Bro gets KO'd / status lands | **Prof. Róisín O'Sullivan**: "A failing grade, if grades still existed here, which — notably — they don't anymore." |
| Aisling's cringe-attack lands | **Prof. Aisling Byrne**: "Sing along if you know it! You won't! Nobody does!" |

### Defeat Dialogue

> **Dean Cathal** (gavel dropped, mortarboard askew, jacket long gone): "...Fine. FINE. You
> win. By combat, not by academic merit, which I want on the record, but — fine."
>
> ⚠ AUTHOR-REVIEW **The backhanded compliment** (delivered here, per the author's ruling that
> it lands post-battle): "Congratulations. You've beaten a man in his fifties and three
> adjuncts who haven't slept properly since the Thesis Defense season started. Do enjoy
> telling that story."

### Post-Defeat Presence (If Any)

Dean Cathal proceeds directly into the graduation ceremony beat — full regalia restored
off-screen, gavel put away, straight back into the Committed Bit with no acknowledgment that
a fight just happened. He never gets a redemption arc and never learns anything; the
graduation ceremony he officiates minutes later is played with exactly the same sincerity as
before the fight, which is the point (per `npc_cathal_murphy.md`: he never breaks character,
for anyone, ever). Security — not the faculty — knocks the bros out at the door afterward;
Dean Cathal does not personally retaliate again.

---

## ⚔️ Combat Specification

### Squad Structure

Dean Cathal is the boss; the three professors are a linked Adds table (Combat Bible §6.8
convention) rather than independent bosses. The fight does not end until Dean Cathal is
defeated — professors can be knocked out individually and stop attacking, but Dean Cathal
gains no direct enrage bonus from losing them (their attrition is comedic, not mechanical
escalation, matching "lets the bros succeed without being heroes or great at any of it").

### Core Stats — Dean Cathal Murphy (boss)
| Stat | Value | Notes |
|---|---|---|
| **HP** | 320 | ⚠ AUTHOR-REVIEW — rolling HP meter applies |
| **SP** | 40 | Spent on the gavel big move |
| **Offense** | 22 | |
| **Defense** | 14 | |
| **Speed** | 9 | Slow — a man in his fifties in dress shoes |
| **Charm** | 6 | Low outside the ceremony register; he is not trying to charm anyone here |
| **Luck** | 8 | |
| **Grit** | 16 | High — fifteen years of never breaking |

### Core Stats — Professors (Adds)
| Stat | Prof. Róisín O'Sullivan | Prof. Cian MacCarthy | Prof. Aisling Byrne |
|---|---|---|---|
| **HP** | 60 | 65 | 55 |
| **Offense** | 12 | 15 | 8 |
| **Defense** | 8 | 10 | 6 |
| **Speed** | 10 | 13 | 11 |
| **Charm** | 10 | 7 | 13 |
| **Notes** | Debuffer archetype | Bruiser-lite archetype | Cringe-caster archetype (Combat Bible §6.8) |

### Move List — Dean Cathal (2–4 moves + big move)
| Move | Type | Effect | Status Inflicted | Weight / Condition | Telegraphed? |
|---|---|---|---|---|---|
| Gavel Rap | Physical | Moderate damage | — | 40% / always | No |
| "Extra Credit" Lecture | Social | Bravado damage, no HP damage | Embarrassed (15%) | 30% / always | No |
| Cite the Handbook | Debuff | -1 party Accuracy | — | 20% / round > 1 | No |
| **TENURE DENIED (big move)** | Physical AoE | Heavy damage, full party | Distracted (self, 1 turn — recoil from the wind-up) | Once per phase | **Yes — 1-beat gavel raise, "TENURE. DENIED." bark** |

### Move List — Prof. Róisín O'Sullivan (Debuffer)
| Move | Type | Effect | Status Inflicted | Weight / Condition | Telegraphed? |
|---|---|---|---|---|---|
| Glass Toss | Physical | Light damage | Sloppy (25%) | 50% / always | No |
| "Identify This" Pop Quiz | Social | Bravado damage | Embarrassed (10%) | 50% / always | No |

### Move List — Prof. Cian MacCarthy (Bruiser-lite)
| Move | Type | Effect | Status Inflicted | Weight / Condition | Telegraphed? |
|---|---|---|---|---|---|
| Dart Throw | Physical | Moderate damage, single target | — | 60% / always | No |
| State Champion '08 | Physical | High damage, single target | — | 40% / hp<50% (self) | No |

### Move List — Prof. Aisling Byrne (Cringe-caster)
| Move | Type | Effect | Status Inflicted | Weight / Condition | Telegraphed? |
|---|---|---|---|---|---|
| Bodhrán Beat | Social | Bravado damage, full party | — | 50% / always | No |
| Off-Key Drinking Song | Social | Bravado damage, full party | Embarrassed (30%) | 50% / always | No |

### Phases (Dean Cathal)
| Phase | Trigger | Behavior Change |
|---|---|---|
| 1 | Fight start | Standard weighted moveset above; professors fight alongside at full strength |
| 2 | Dean HP < 60% | Gavel Rap damage +20%; TENURE DENIED becomes available every 2 rounds instead of once per phase; professors begin dropping out individually as their own HP empties (see Adds table) |
| 3 | Dean HP < 25% | Desperation: "PUBLISH OR PERISH" — Dean drops all social moves, spams Gavel Rap and TENURE DENIED exclusively; any surviving professors clock out entirely at this point ("that's my contracted hours") |

### Buffs & Debuffs They Use
- **Self/ally buffs**: none — this is not a coordinated tactical unit, it is four
  academics improvising badly
- **Debuffs on the party**: Embarrassed (Cite the Handbook lowers Accuracy separately;
  Aisling's moves stack Embarrassed chance), Sloppy (Róisín), Distracted (self-inflicted on
  Dean only, the TENURE DENIED recoil — this is the vulnerability window, not a party debuff)

### Immunities / Resistances / Weaknesses
| Category | Detail |
|---|---|
| **Immune to** | Dean Cathal is immune to Embarrassed — fifteen years of never breaking means the character mechanically cannot take that status. Professors are not immune to anything. |
| **Resistant to** | Dean Cathal resists Social-type damage 25% (his register is armor) |
| **Weak against** | Beer-tagged moves — per the Combat Bible's Publandia EnvMult, beer-tagged attacks are ×1.5 here, and thematically the whole fight is happening because of a beer pong scandal |
| **Vulnerability window** | After TENURE DENIED lands, Dean is Distracted for 1 turn (recoil from his own wind-up) — the fight's one clean punish window |

### Adds / Minions (If Any)
| Minion | Count | Role | Notes |
|---|---|---|---|
| Prof. Róisín O'Sullivan | 1 | Debuffer | Drops out (stops attacking, remains on-screen) once her own HP hits 0 — she does not "die," she simply steps back, consistent with no character in this game facing real violence consequences |
| Prof. Cian MacCarthy | 1 | Bruiser-lite | Same drop-out rule |
| Prof. Aisling Byrne | 1 | Cringe-caster | Same drop-out rule |

### Arena & Gimmick

The Quad at night — string lights, a toppled "CONGRATULATIONS GRADUATES" banner, plastic ivy
torn off one wall in the scuffle. ⚠ AUTHOR-REVIEW gimmick proposal, pending author approval:
a scattered ring of intact and shattered ping-pong balls litters the arena floor as a
callback to the trick shot; no mechanical effect is proposed for them beyond set dressing,
to avoid inventing an ungated new mechanic.

---

## 💰 Rewards

| Reward | Value / Item | Notes |
|---|---|---|
| **SOVS** | ⚠ AUTHOR-REVIEW 45 SOVS | First-pass estimate, unbalanced against other content |
| **Clout (XP)** | ⚠ AUTHOR-REVIEW 60 | |
| **Guaranteed drop** | `opener_trinity_of_pints`, `beer_trinity_of_pints`, `stamp_trinity_of_pints` | Not battle loot in the conventional sense — these are the brewery's standard challenge-completion rewards per the master spec's loop (stamp + selfie + opener + beer, all on completion), delivered via the graduation ceremony that immediately follows this fight, not as a battle drop screen |
| **Rare drop** | None | |
| **Unlocks** | Graduate status, Advanced Course access, Academic Amber for purchase | Per `design/worlds/publandia/trinity_of_pints.md` |
| **Achievement** | None directly tied to this fight — see the Trinity of Pints venue file's Achievement Track for "Bachelor" / "Scholar" | |

---

## 🔗 Connections
| NPC / Villain | Relationship |
|---|---|
| Prof. Róisín O'Sullivan, Prof. Cian MacCarthy, Prof. Aisling Byrne | Colleagues, not conspirators — none of the three knew about the magnet, and none of them wanted this fight; they show up because the Dean called their names, not out of loyalty to the cheat |
| Fintan Brogan (Tournament Referee) | The trigger for this whole encounter — his ruling is what breaks Dean Cathal. Fintan does not participate in or witness the battle itself; his jurisdiction ends at the table. |
| Brendan Nolan (Trinity Brewmaster) | Uninvolved in the fight; appears immediately after for the graduation ceremony, entirely unaware anything happened |

---

## ✅ Validation Checklist
| Requirement | Status |
|---|---|
| Funny, unique name (checked against all existing names) | ✅ (Dean Cathal Murphy and all three professors are pre-existing, established characters — no new names introduced by this file) |
| Racket grounded in the city's satirized culture/underbelly | ✅ (gimmick-pub academic tourism, cheating to keep the house always winning) |
| Full combat spec (stats, moves, phases, immunities, rewards) | ✅ — all ⚠ AUTHOR-REVIEW, first-pass numbers |
| Statuses from master list only (or author-approved new ones) | ✅ (Embarrassed, Sloppy, Distracted — all pre-existing; Distracted per PRD's own Craic Baron precedent) |
| All prices/drops in SOVS | ✅ |
| Pre/mid/post-battle dialogue written, full-strength satire | ✅ |
| No moralizing, no reality-check function, no redemption arc | ✅ — Dean Cathal learns nothing and returns to the bit immediately |
| Bros never afraid, never self-aware — annoyed and overconfident | ✅ — the bros treat this as more "coursework," never register real danger |
| Sprite notes for artists (battle + overworld + telegraph) | ✅ |
| Author approval on: new mechanics/gimmicks, stat numbers, story ties | ⬜ PENDING — everything numeric in this file needs a balance pass |

---

## 🔧 Development Status
- **Status**: Concept — drafted in full, pending author approval on all combat numbers
- **Profile File Location**: `design/worlds/publandia/npcs/Trinity_Of_Pints/villain_secure_the_quad.md`
- **Registered In**: No enemy/encounter data file exists yet for this content
- **Sprite Sheet**: not yet specced — recommend a dedicated `trinity_secure_the_quad_battle.png` sheet, separate from both the faculty NPC sheet and any other battle sheet

## 📜 Revision History
| Date | Change | Author |
|------|--------|--------|
| 2026-08-05 | Initial profile — first villain profile in the project | Claude (Task 8, quest-doc reconciliation) |

---

*Template Version 1.0 — author-mandated 2026-08-03: every villain must have a completed
profile at creation. This file also establishes the project's first Adds-table precedent for
multi-enemy squad encounters; future squad bosses should follow this pattern rather than
inventing a new one.*
