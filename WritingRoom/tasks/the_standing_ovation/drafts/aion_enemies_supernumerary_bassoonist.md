# Aion — Enemy Concepts: Supernumerary Ambitieux & Second Chair Bassoonist

**Phase 4 primary draft. Concept + comic mechanics per Editor Ruling f3 (Aion lane).**
**Reviewer: Gemini.** GLM integrates into `drafts/glm_enemies_full.md` after review.
**Naming check done:** "Supernumerary," "Bassoonist," "Tympanist," "Oboist," "Stage Fright," "Corpsing," "Union Break" appear nowhere in project canon outside this task's drafts. Bassline Opera House already has "The Opera Critic" and "The Velvet Bouncer" — both of these enemies are distinct in role, location, and mechanic. `sinfonia_enemies.json` is currently an empty `enemies: {}`, so these are the world's first two entries; schema copied exactly from `debaucheryville_enemies.json` (the only populated file).

---

## ENEMY 1: THE SUPERNUMERARY AMBITIEUX

### Identity
- **Enemy ID:** `supernumerary_ambitieux`
- **Display Name:** Supernumerary Ambitieux
- **Role:** Status-manipulation enemy (common-adjacent; Opera District streets)
- **Location:** Stage-door alley behind The Standing Ovation / Bassline service corridor. Encounter is ambient, pre- or post-revue.

### Silhouette / Visual
A gaunt man in his forties wearing mismatched Roman legionary armor — one shoulder pauldron plastic, the other clearly borrowed from a different production's polycarbonate Greek hoplite kit — holding an oversized wooden pike vertically, like a palace guard who has decided the pike is the performance. Stage blood on his chin from a production he was in nine years ago that he has chosen not to fully remove because *removing it would break the continuity.* His silhouette reads instantly: spear, pauldron, chin.

### Satirical Premise
A supernumerary is an opera extra: non-speaking, non-singing, paid nothing or nearly nothing, hired to stand at the back of the stage holding a spear so the stage picture looks populated. This one has decided that holding the spear is not a job. It is an *art.* He does Stanislavski exercises before standing still. He has a backstory for the spear. He has an intention for the standing. He has been asked to leave two community theaters for "bringing an energy that disrupted the tableau of the actual paid cast."

The bros are not his enemies because they attacked him. The bros are his enemies because they *noticed him*, and being noticed by an audience of three cargo-shorted Americans is the review he has waited his entire unpaid life for. He will now perform AT them. Whether they consent or not.

The comedy: he cannot act, so he *becomes* an actor — his entire kit is the gap between what he thinks he's doing (soulful, disciplined stagecraft) and what the player sees (a man holding a stick with frightening commitment).

### Battle Intro
> **A Supernumerary Ambitieux assumes a ready position! He is already acting. The battle has not started yet, and he is acting.**

If the party tries to walk past without engaging (PROPOSED ambient trigger — see engine notes):
> **He blocks the alley. Not the whole alley. Symbolically.**

### Moves (PROPOSED FULL DESIGN — mechanics are the joke)

**1. BUILD A TABLEAU** — *His opening move. Zero damage.*
He spends **two full turns sculpting himself** into a heroic pose: pike planted, chin lifted, plastic pauldron rotated for maximum catch of the streetlight. Both turns are visible, telegraphed, and exploitable — the game shows him adjusting an elbow by degrees.
- **If the party hits him during the two setup turns:** the pose is ruined. He takes **double damage** ("corpsing" — the one theater word he'd rather die than hear) and the charge is cancelled. He restarts the tableau next turn, muttering.
- **If he completes the tableau:** he is *posed.* While posed, his entire kit comes online.

**2. FOURTH WALL ADDRESS** — *Passive while posed.*
While posed, he gains **+50% defense**. The in-battle tooltip: **"The fourth wall only exists when nobody breaks it."**
The counterplay in one sentence: **hit him once and the entire buff is gone.** The moment anyone damages him, the fourth wall is broken, the pose is dead, and he drops back to normal defense — visibly deflating, pauldron slipping.
- **Comic escalation:** if the party hits him and then *stops* attacking, he attempts to re-enter the pose mid-battle, and the battle log reads: > **He is trying to get back into it. Nobody is looking. He's doing it anyway.**

**3. INTENSE GAZE** — *Triggered response, not an action.*
If a party member attacks him **while he is posed**, he survives the hit with a locked stare and inflicts **STAGE FRIGHT** (PROPOSED status) on the attacker: the target's next 2 attacks have a 35% chance to "freeze" — miss, as the character chokes under an audience of one unpaid man. Flavor text on application:
> **You've been seen. God, you've been SEEN.**
Counterplay: don't attack the finished pose (see below). Stage Fright is annoying, not run-ending, and fully avoidable.

**4. NOTE FROM THE DIRECTOR** — *Fail-state / timer.*
If nobody attacks him while posed for **3 consecutive turns** — if the party simply ignores the completed tableau — he concludes the audience didn't get it, whispers *"they weren't ready,"* and **leaves the battle to go check if the director saw that.** No further reward, no penalty, the encounter simply ends with him gone.
- **The joke:** the encounter has TWO completely valid counterplays — burst him during setup (deny the art) or ignore the finished product (starve the artist) — and the second one is funnier, because watching a man hold a pose for three turns while three bros pointedly discuss beer is better than any damage number.

### Counterplay Summary
1. Hit him during *Build a Tableau* (double damage, cancels pose).
2. Hit him once after completion (destroys the fourth-wall buff, no Stage Fright — Stage Fright only triggers on hits *while posed*, and the first hit IS the de-posing hit. GLM: ruling needed in the data contract that the de-posing hit itself cannot carry Stage Fright back, or the counterplay self-punishes).
3. Ignore the finished pose entirely for 3 turns (he leaves; zero risk, zero reward).

### Reward Structure
- **Gold: 0.** He is unpaid. He does this for the exposure. The party loots a man who has no money and never has.
- **XP: 11.**
- **Drop (PROPOSED item, drop_chance 1.0): `crumpled_headshot`** — a laminated 8x10 of the Supernumerary in full legionary kit, autographed to nobody, with a printed email address that has "2007" in it. Flavor: *"Headshots are just business cards with more chin."* Sell value 2 SOVS. (Note for GLM: per m2 audit, `grant_rewards` applies `item_drop` unconditionally — which is why drop_chance is authored at 1.0, so engine behavior matches authored intent.)

### CURRENT ENGINE DATA CANDINATE (D-rank, exact shipped schema)
```json
"supernumerary_ambitieux": {
  "display_name": "Supernumerary Ambitieux",
  "battle_intro": "A Supernumerary Ambitieux assumes a ready position! He is already acting.",
  "max_hp": 26,
  "offense": 5,
  "defense": 5,
  "speed": 3,
  "luck": 3,
  "xp_reward": 11,
  "gold_reward": 0,
  "item_drop": "crumpled_headshot",
  "drop_chance": 1.0
}
```
Single-target melee only, no statuses, no multi-turn behavior under the current engine — the tableau, Stage Fright, and fourth-wall mechanics are PROPOSED ENGINE WORK (see continuity file dependency list). Under the current engine he is a slow, tanky, broke weirdo with a spear, which is honestly still on-premise.

---

## ENEMY 2: THE SECOND CHAIR BASSOONIST

### Identity
- **Enemy ID:** `second_chair_bassoonist`
- **Display Name:** Second Chair Bassoonist
- **Role:** Group / reinforcement enemy (Opera District ambient)
- **Location:** Musicians' Courtyard, the alley between The Standing Ovation and the Bassline's stage door, where pit players smoke between acts and complain in eight-part harmony.

### Silhouette / Visual
A man in a wrinkled white-tie tuxedo, bow tie permanently at half-mast, clutching a colossal wooden bassoon the way other men hold anti-tank weapons — two-handed, braced, aimed. The bassoon is visibly older than him and better maintained. Cigarette behind one ear, reed case in breast pocket, the thousand-yard stare of a man who has played the same four bars of the same overture eleven hundred times and been thanked for it twice.

### Satirical Premise
He is Second Chair. He has been Second Chair for twenty-two years. He has heard "we'll go with the first chair's read" so many times it has replaced a childhood memory. And now — NOW — the Bassline and the drag revue next door have started using **synth backing tracks and drum machines**, which means a laptop is doing his job, and the laptop doesn't even have a chair.

He is not angry at the bros specifically. He is angry at the century. The bros are simply the century's current representatives, and they are wearing cargo shorts to an opera district, and one of them just asked if the bassoon is "one of those big clarinet things," and that is the note the fight starts on.

The comedy: every mechanical system in the fight is him losing a labor dispute with modernity in real time.

### Battle Intro
> **A Second Chair Bassoonist takes issue with you! Also with the century!**

### Moves (PROPOSED FULL DESIGN)

**1. CRACKED REED** — *Passive fail-safe / party timing lever.*
His reed is cracked. It has been cracked since intermission. His attacks carry a built-in **25% miss chance**, and the miss chance **rises by 10% each time he's taunted** — Bravado taunts work on him disproportionately well because he is *already furious* and taunting him makes him rush. Miss flavor:
> **The reed squeaks. Twenty-two years of technique, defeated by a splinter of cane.**
**GLM — do not smooth this.** The crack is the fight's rhythm section: it gives a fragile party breathing room and gives taunt-builds a real toy. A bassoonist with a working reed is just a guy.

**2. LOW C** — *Heavy attack with a visible exhale window.*
The bassoon's bottom note, felt in the sternum before it's heard. Armor-piercing — **but he has to inhale for two full turns first** (visible charge: the battle log shows the intake, his chest expanding like a bellows, the bros having a two-turn conversation about whether the big clarinet is okay).
- On release: heavy single-target damage that ignores defense.
- **Then he goes sharp.** The note lands a quarter-tone sharp because he's furious, and the self-debuff **Sharp** (PROPOSED): his offense −2 for the next 3 turns, because he heard it, and he knows, and he'll be thinking about it.
- **Counterplay:** the two-turn inhale is the attack window. Burst him mid-inhale and the Low C never happens — the charge is lost, and the log reads: > **He never got to use it. He'll bring this up at rehearsal. He brings everything up at rehearsal.**

**3. UNION BREAK** — *Reinforcement summon / self-own.*
On his second turn, he signals, and a reinforcement arrives:
- **Tympanist on Break** (`tympanist_on_break`) — a man eating a sandwich with one hand and mallets in the other. Weaker than the Bassoonist: half HP, a single thump attack that has a 30% chance to hit the wrong party member because he isn't looking.
- **Overworked Oboist** (`overworked_oboist`) — a woman who has been doubling on English horn since Tuesday and has the thousand-yard stare to prove it. Weaker than the Bassoonist: her attack inflicts no damage but a 2-turn **Embarrassed** on hit, because being lectured by an oboist about reed discipline is humiliating on a cellular level.
- **The joke is the summon is a downgrade.** His backup is people who are also on break. Calling for solidarity wastes his turn and brings in colleagues *weaker than he is*. GLM, verify in integration that this reads as comic escalation (the fight gets bigger and sillier but not more dangerous) and not as a reward for stalling — my intent is that Union Break is a net tempo LOSS for him, and the log should frame it that way: > **The Second Chair calls for backup. The backup is on break. The backup was always going to be on break.**

**4. KEY-CLICK** — *Triggered free hit.*
Whenever a party member uses an item, the Bassoonist clicks his keys — the pit musician's instinctive, decades-deep contempt reflex — and deals a small free hit to the item user.
> **"Real musicians don't crunch during the opera."**
This taxes item use, pushing the party toward skills and attacks, which feeds back into taunting him (see Cracked Reed) and bursting his inhale windows (see Low C). The whole kit is one interlocking labor dispute.

### Counterplay Summary
1. Taunt to inflate his miss chance (Cracked Reed).
2. Burst the two-turn Low C inhale (deny the nuke, dodge the Sharp self-debuff drama).
3. Let Union Break waste his turn; mow the weak colleagues; feel briefly like management.
4. Minimize item use or eat the key-clicks knowingly.

### Reward Structure
- **Gold: 14** (union scale — he has money, unlike the Supernumerary; it's just never enough).
- **XP: 16.**
- **Drop (PROPOSED item, drop_chance 1.0): `spare_reed`** — a hand-finished bassoon reed in a tiny plastic case. Flavor: *"Smells faintly of decades of second-hand smoke and resentment. Works perfectly. He had spares the whole time."* Consumable, PROPOSED effect: cures Embarrassed, because blowing into it produces a dignified honk that resets the mood. (Effect flagged PROPOSED; Embarrassed-cure interplay to be checked against the status system during GLM's integration.)

### CURRENT ENGINE DATA CANDIDATES (D-rank, exact shipped schema)
```json
"second_chair_bassoonist": {
  "display_name": "Second Chair Bassoonist",
  "battle_intro": "A Second Chair Bassoonist takes issue with you! Also with the century!",
  "max_hp": 34,
  "offense": 7,
  "defense": 3,
  "speed": 4,
  "luck": 4,
  "xp_reward": 16,
  "gold_reward": 14,
  "item_drop": "spare_reed",
  "drop_chance": 1.0
},
"tympanist_on_break": {
  "display_name": "Tympanist on Break",
  "battle_intro": "A Tympanist on Break arrives, still chewing!",
  "max_hp": 16,
  "offense": 4,
  "defense": 2,
  "speed": 3,
  "luck": 2,
  "xp_reward": 5,
  "gold_reward": 3,
  "item_drop": "half_eaten_sandwich",
  "drop_chance": 1.0
},
"overworked_oboist": {
  "display_name": "Overworked Oboist",
  "battle_intro": "An Overworked Oboist materializes, already exhausted by this!",
  "max_hp": 18,
  "offense": 3,
  "defense": 2,
  "speed": 5,
  "luck": 3,
  "xp_reward": 6,
  "gold_reward": 4,
  "item_drop": "spare_reed",
  "drop_chance": 1.0
}
```
*(Note: `half_eaten_sandwich` is a PROPOSED item ID — no existing canon item with this name found in repo search; it is deliberately mundane. If GLM's pass prefers the Tympanist dropless, cut it, but per the m2 audit the engine grants `item_drop` unconditionally, so anything authored here WILL drop every kill — flagging so nobody discovers that in QA.)*

Under the current engine: no summons, no key-click reaction, no charge turns — he's a mid-stat brawler with a good name. All reinforcement and timing behavior is PROPOSED ENGINE WORK.

---

## NOTES FOR REVIEWERS

**Gemini (reviewer):**
1. **Charge-turn DNA check:** the Supernumerary's two-turn *Build a Tableau* and the Bassoonist's two-turn *Low C* inhale are both visible charge windows. If your Keeper of the Rope rebuild (per f4) also leans on a charge turn, we'll have three enemies teaching the same lesson. Tell me if the Keeper uses one; if so I'll re-time the Supernumerary's tableau to a one-turn "strike the pose" so the three fights teach different counterplays.
2. **Stage Fright vs. your Critic's kit:** the Axed Critic inflicts *Embarrassed* / *Existential Crisis* per the story break. My *Stage Fright* (freeze/miss) is deliberately a different failure mode — check we're not stepping on the same "social performance anxiety" pedal twice in one district, since your Critic also roasts.
3. The Supernumerary's zero-gold reward: confirm you read it as a joke (unpaid extra = nothing to loot) and not as a design error, and shout if you think players need a few SOVS for the kill to feel worth it. My position: the headshot drop plus the two counterplay stories is the reward; the empty wallet IS the premise.

**GLM (integration):**
1. Ruling needed in the data contract: the de-posing hit on the Supernumerary cannot itself trigger Stage Fright (see his counterplay summary §2) — otherwise punishing the buff-removal counters its own counterplay.
2. Union Break summons: verify the weaker-stats approach reads as comic escalation, not stalling reward (see §3 note).
3. Both D-rank blocks match the `debaucheryville_enemies.json` field set exactly — confirm before adding to the integration sheet, and note that `sinfonia_enemies.json` is currently empty, so insertion order is yours to define.
4. All multi-turn AI, summons, triggered reactions, and statuses are itemized in my continuity file's engine-dependency list. Nothing in the CURRENT ENGINE blocks above is promised by the data alone.
