# THE STANDING OVATION — STORY AND GAMEPLAY BREAK (CONSOLIDATED)

**Task:** `WritingRoom/tasks/the_standing_ovation/`
**Phase:** Phase 3 — Story and Gameplay Break
**Status:** Unified Production Blueprint (Ready for Editor Review)
**Consolidator:** Gemini (with GLM, Aion, Kimi)

> **EDITOR RULING #2 CORRECTIONS (binding, applied by the moderator 2026-11-09).** Full ruling: `room/editor_ruling_02.md`.
> - Event 10 speakers corrected below (Max asks the name; Chadwick insists "You know my name"; Max: "Do I?").
> - Producer's Circle 72 SOVS is PROVISIONAL. Check affordability against the actual economy (reported starting wallet: 20 SOVS). Do not invent starting funds.
> - The Tactical Wing must give a legitimate, enjoyable view of the show. No obscured-table punishment.
> - D4 is only a real decision for tape-holders. Don't advertise four universal choices. Ideally give no-tape players a distinct exit choice.
> - Tape transfer stays **offscreen** (q8, option B). A "post" means Chadwick commits to releasing it (e.g. `footage_release_planned`), not an instant upload. No new Bassline or Plaza service. No guaranteed view count.
> - TS_SUPPRESSED: the invented +10 Conf / −10 Focus / Motor Impairment numbers are **removed**. TROUSER SNAKE stays +10 Confidence / −25 Concentration / compromised dialogue / rest of the evening unless suppressed by *substantial* alcohol. Check the real drink specs and the intoxication system. Two beers isn't automatically substantial.
> - The D2A comped Understudy needs review: no free advantages for being humiliated. A compliment, prop or souvenir may serve better.
> - Every new price, item, flag, status, stat and NPC detail goes in a single **Proposed Content and Mechanics Register**, not as inline tags on every line.
> - The revue must stay genuinely impressive, with several fully realized numbers.

---

## 1. NARRATIVE & QUEST ARCHITECTURE

* **Quest ID:** `sinfonia_sidequest_standing_ovation_01`
* **Template:** `design/templates/sidequest_template.md`
* **Timing & Scope:** One continuous evening in Sinfonia's Opera District. Entry after 22:00, exit before close. Does not interfere with existing daylight brewery tour items (`beer_standing_ovation_item.md`, `opener_standing_ovation_item.md`, `stamp_standing_ovation_item.md`).
* **Tone Register:** Razor-sharp adult satire, campy theatricality, Y2K frat antihero delusion. The world is contemporary and cutting; the bros are stuck in 2002. No moral redemption, no sanitized winking, no explanatory narrator.

### The Four-Act Structure

* **Act I: The Velvet Threshold (Pre-Show Street & Foyer)**
  * Bros arrive at The Standing Ovation. Foyer environmental comedy (organ pipe taps, velour drapes, dramatic staff).
  * Environmental satire: The Legends Wall is free scenery featuring *"THE AMERICANS — RETURNING CHAMPIONS, ANNUAL SINCE 1994"*.
  * **Decision 1 (Seating & Vanity):** Producer's Circle (72 SOVS) vs. Tactical Wing Position (0 SOVS).
* **Act II: The First Daughters Revue (The Performance)**
  * The performance of *MAX VEX PRESENTS: THE FIRST DAUGHTERS*. High-energy, genuinely brilliant political drag satire.
  * Chelsea Morning, Jenna Talia, and Barbara Bushed execute sharp turn-of-the-millennium musical parody numbers.
  * **Decision 2 (Mid-Show Crowd-Work Fork):**
    * Branch A: Pilsner hauled onstage during Fake-ID number; Jenna exposes his 1998 license; comped `the_understudy`.
    * Branch B: Chadwick arms vintage camcorder; Jenna disarms him with deadpan battery-pack roast; sets `tape_exists = true`.
    * Branch C: Restraint. Max tosses 2000 election trivia; Pilsner nails the Florida VNS retractions; *"That was the correct amount of useless"*.
* **Act III: The Aftermath & The Christening (The 11 Fixed Events)**
  * Max Vex arrives at the bros' table post-curtain.
  * Executes the author-approved 11-event sequence verbatim with zero menu interruptions.
  * Bradley's cardstock playbill drops to belt level; Max christens him **Trouser Snake**. Chadwick denied nickname. Max departs to manage professional duties and staff olive arguments.
  * Dossier §14 verbatim: *"Your dick did." / "PHILLIP." / "What? I'm proud of you."*
* **Act IV: The Damage Control & Egress (Post-Show Coping & Street Exit)**
  * **Decision 3 (Bradley's Coping Strategy):**
    * Option A: Ice Water (0 SOVS) — Pure stoic denial; full `TROUSER_SNAKE` status; Pilsner's silence drill.
    * Option B: Drink Through It (20 SOVS) — Two house Encores; `TS_SUPPRESSED` status; staff standing ovation fanfare.
    * Option C: Biomechanical Reset (0 SOVS) — Slapstick physical mitigation minigame; Barbara Bushed coaster assist.
  * **Decision 4 (Exit & The Footage):**
    * Option A: Post Footage (Only if `tape_exists = true`) — Delayed-fuse upload via Dieter / Plaza vendor; next-day mortification.
    * Option B: Vault Footage (Or D2A/D2C Default) — Chadwick's live memory re-enactment on the street.

---

## 2. THE 11 FIXED EVENTS SPINE (AUTHOR-APPROVED SEQUENCE)

1. **Event 1:** Bros attend *The First Daughters* revue.
2. **Event 2:** Pilsner recognizes Y2K political figures, dramatically overestimating his own historical clout.
3. **Event 3:** Max Vex meets the bros at their table after the curtain call.
4. **Event 4:** Max names Pilsner **Beer Lord** (unsolicited, permanent bro pride).
5. **Event 5:** Max names Bradley **Basketball Jersey**, calls him cute, and says: *"Don't ruin it by speaking."*
6. **Event 6:** Bradley's physical response surprises him (**visible physical tell**—playbill drops to belt level).
7. **Event 7:** Verbatim author exchange:
   * Max: *"Oh."*
   * Bradley: *"What?"*
   * Max: *"Nothing."*
   * Bradley: *"What?"*
   * Max: *"Apparently somebody here is more progressive than he thought."*
8. **Event 8:** Max nicknames Bradley **Trouser Snake**.
9. **Event 9:** Chadwick receives no nickname.
10. **Event 10:** Verbatim author exchange (encounter dossier §10). **Max asks; Chadwick answers.** Corrected per Editor Ruling #2:
    * Max: *"Hey! It's Beer Lord, Trouser Snake and…"*
    * *(Max looks at Chadwick.)*
    * Max: *"…what did you say your name was again?"*
    * Chadwick: *"Chadwick."*
    * Max: *"Right."*
    * Chadwick: *"You know my name."*
    * Max: *"Do I?"*
    *(If D2B armed, the chain wrenches the camcorder to belt height here.)*
11. **Event 11:** Max moves on with their evening.

---

## 3. STATE & DECISION MATRIX (AGENCY & BRANCHING)

| Decision | Branch | Cost | Flags Set | Immediate Outcome | Downstream Consequence |
|---|---|---|---|---|---|
| **D1: Seating** | **A: Producer's Circle** | 72 SOVS | `so_producer_circle = true` | Unlocks `receipt_producers_circle` item; pre-show PA: *"Lord Pilsner and party. Only one name was supplied."* | Max opening dialogue acknowledgment; itemized receipt joke; Axed Critic drops `condescending_review`. |
| | **B: Tactical Wing** | 0 SOVS | `so_producer_circle = false` | Back-row obscured table; Pilsner: *"Flanking sightlines. Tactical egress."* | Saves 72 SOVS; Chadwick's camcorder chain snags on velour tassel trying to film VIPs. |
| **D2: Crowd Work** | **A: Pilsner Spotlight** | 0 SOVS | `pilsner_duet_spectacle = true` | Jenna hauls Pilsner onstage during Fake-ID song; holds up 1998 license; comped `the_understudy`. | Pilsner claims he was hired as guest vocalist; permanent bragging rights. |
| | **B: Camcorder Armed** | 0 SOVS | `tape_exists = true` | Chadwick aims red tally light at Barbara; Jenna roasts his battery pack. | Camera stays running all night; enables D2B chain-wrench in Event 10 and unlocks D4A. |
| | **C: Restraint** | 0 SOVS | `pilsner_trivia_win = true` | Max tosses 2000 election trivia; Pilsner nails Gore/Bush Florida retractions. | Max: *"That was the correct amount of useless."* Pilsner claims book-writing recruitment; 0 SOVS spent. |
| **D3: Coping** | **A: Ice Water** | 0 SOVS | `coping_water = true` | Orders 3 waters; Dramatisch: *"Tragic"*. Pilsner conducts 4-second silence drill. | Inflicts full `TROUSER_SNAKE` (+10 Conf / -25 Conc / Compromised Dialogue: *"Yes." / "Yes, please."*). |
| | **B: Drink Through It** | 20 SOVS | `coping_drink = true` | Orders 2 house Encores (10 SOVS ea); staff delivers mandatory standing ovation fanfare. | PROPOSED suppressed stage (no new numbers, see the ruling); appends audio to the tape. |
| | **C: Biomechanical Reset** | 0 SOVS | `coping_reset = true` | Micro-choice: Table-Press, Wall-Sit, or Playbill Wedge. Slapstick physical failure. | Barbara slides coaster (*"Hold this. Looks busier"*); appends frame to tape; full status persists. |
| **D4: The Footage** | **A: Post Footage** *(Requires D2B)* | 0 SOVS | `footage_posted = true` | Chadwick commits to releasing the tape (`footage_release_planned`, PROPOSED). Transfer happens offscreen, later. | Chadwick's escalating claims about a tape nobody has seen. Any public payoff is a conditional PROPOSED future event, not a guarantee. |
| | **B: Vault Footage** *(Or Default)* | 0 SOVS | `footage_vaulted = true` | Chadwick suppresses tape (or no tape exists). Street memory re-enactment. | Chadwick acts out scene from memory on street walk, chain as prop, self-cast as flirting target. |

---

## 4. FIVE EARTHBOUND-STYLE COMBAT ENEMIES (OPERA DISTRICT)

All encounters take place in the ambient Opera District streets, alleys, and foyer surrounds (Pre- and Post-Revue). No combat during the performance (Ruling q3).

1. **Common Enemy: The Axed Critic**
   * *Location:* Street outside The Standing Ovation.
   * *Silhouette / Visual:* Hunched, ink-stained trench coat, carrying a crushed fedora and a vintage PalmPilot with a broken stylus.
   * *Satirical Premise / Period Slot:* Bitter, unemployed broadsheet reviewer covering the Opera District. Attacks in 1998–2005 entertainment-media register (*"A boy-band reunion nobody requested; two stars, one is for the cargo shorts"*).
   * *Status Interaction:* Inflicts *Embarrassed* and *Existential Crisis*. Eager to review leaked tape if `footage_posted`.
2. **Status-Manipulation Enemy: Supernumerary Ambitieux**
   * *Location:* Backstage Alley / Stage Door Egress.
   * *Silhouette / Visual:* Rigidly posturing theater extra in mismatched Roman legionary plastic armor, holding an oversized wooden pike.
   * *Satirical Premise:* An unpaid non-speaking opera extra who treats holding a spear as high-art Stanislavski method acting.
   * *Mechanic-as-Joke:* Uses "Intense Gaze" and "Dramatic Upstaging" to buff own defense while inflicting *Hesitation* and *Stage Fright*.
3. **Group / Reinforcement Concept: Second Chair Bassoonist**
   * *Location:* Musicians' Courtyard / Alley.
   * *Silhouette / Visual:* Disheveled classical musician in a wrinkled tuxedo, clutching a colossal wooden bassoon like an anti-tank weapon.
   * *Satirical Premise:* Exhausted pit player furious that the drag revue uses digital synthesizers and drum machines.
   * *Mechanic-as-Joke:* "Tuning A" soundwave AoE; summons reinforcements ("Tympanist on Break", "Overworked Oboist").
4. **Rare / Observation Encounter: Keeper of the Rope**
   * *Location:* Balcony Stairs / Vestibule.
   * *Silhouette / Visual:* Imposing, stiff-necked guardian in braided gold epaulets clutching brass stanchions.
   * *Satirical Premise:* Hyper-zealous bouncer defending a red velvet rope that venue documentation explicitly notes is purely decorative.
   * *Mechanic-as-Joke:* **Passive unless provoked.** Only attacks if party interacts with the rope. Counterplay: player literally walks around him.
5. **Elite / Mini-Boss: The Dramatisch Keg-Acolyte**
   * *Location:* Cellar Service Vault / Alley Loading Bay.
   * *Silhouette / Visual:* Towering cellar master in rubber apron, leather welder's goggles, and a brass CO2 pressure manifold worn like a bandolier.
   * *Satirical Premise:* A solitary cellar-hand zealot fanatically dedicated to Herr Dramatisch's nitrogen tap lines.
   * *Mechanic-as-Joke:* Builds a three-stage "Head Foam Meter" through pressurized beer sprays. If player weathers his three-turn head-retention lecture without running, he salutes their discerning palate, awards high-tier brew drops, and walks away.

---

## 5. TECHNICAL & IMPLEMENTATION CONTRACT

* **Current Engine Reality (per GLM/m2 audit):** `data_repo.gd` currently hardcodes Debaucheryville paths; `GameState.grant_rewards()` ignores drop percentages and takes single IDs. Therefore, all 5 enemies are formatted to exact shipped JSON schema as provisional data candidates, while enemy summoning, party combat scaling, multi-turn AI routines, and custom status flags are documented as **PROPOSED ENGINE WORK**.
* **Status System Contract:** `TROUSER_SNAKE` preserves exact player-facing text (+10 Confidence / -25 Concentration / Compromised Dialogue). In engine, this is handled via quest-scoped dialogue-option restriction (`restricted_dialogue = true`), preserving engine integrity without unauthorized global stat modifications.

---

## 6. WORK ALLOCATION FOR PHASE 4 DRAFTING (rebalanced per Editor Ruling #2, f3)

* **Kimi:** Quest narrative and dialogue spine (Acts I–IV, the 11 fixed events checked speaker by speaker against the dossier, Max and the queens' dialogue). File: `drafts/kimi_quest_spine.md`. Reviewer: Aion. Kimi also does the character, dialogue and presentation review of all five enemies.
* **GLM:** Combat architecture, shared balance assumptions, current-engine data contract, D1–D4 state logic and TROUSER SNAKE spec, plus the elite **Keg-Acolyte** encounter. Files: `drafts/glm_mechanics_state.md`, `drafts/glm_enemies_full.md` (GLM integrates all five enemy sheets after the concept writers deliver). Reviewer: Gemini.
* **Gemini:** Initial creative design and dialogue for the **Axed Critic** and the **Keeper of the Rope** (rebuilt per f4: an environmental bypass layer plus a real combat layer built on fake authority over a boundary that doesn't exist, with at least one clever nonviolent resolution). File: `drafts/gemini_enemies_critic_keeper.md`. Reviewer: Aion. Gemini also writes the NPC profiles (Chelsea Morning, Jenna Talia, Barbara Bushed, Max check) in `drafts/gemini_npc_profiles.md` (reviewer: Kimi) and does the satire punch-up pass in `drafts/gemini_satire_punchups.md` (reviewer: Aion).
* **Aion:** Initial creative design and comic mechanics for the **Supernumerary Ambitieux** and the **Second Chair Bassoonist**. File: `drafts/aion_enemies_supernumerary_bassoonist.md`. Reviewer: Gemini. Aion also writes the Chadwick arc (`drafts/aion_chadwick_arc.md`, reviewer GLM) and the continuity register plus the **Proposed Content and Mechanics Register** (`drafts/aion_continuity_implementation.md`, reviewer GLM).
* Every enemy is reviewed by someone other than its concept writer.
* **Kimi (integrator):** Assembles `final.md` only after cross-review. One narrative voice, not a paste-up. Not declared complete or canonical before the next editorial review.

---

## AUTHOR ADDENDUM (2026-11-09 16:25) — structure change, recorded by the moderator

The quest no longer ends when the bros leave The Standing Ovation. An optional overnight continuation follows the show (catcalling during the show → backstage invite → "party" → cut to black → morning-after). See `decisions.md` §6 and `room/author_overnight_source.md`. Its own story break is pending (Kimi drafts it; editor review; author approval) before any of it is drafted.
