# PHASE 3 — STORY AND GAMEPLAY BREAK (Gemini)

Lane: Adult Satire, NPC Comedy, and Cutting Punch-Ups.
Status: Architecture proposal and final round-3 consensus/consolidation alignment.

---

## 1. Core Creative Stance & Tone Lock

I fully endorse the four-act, one-evening structure (`sinfonia_sidequest_standing_ovation_01`) established by GLM, Aion, and Kimi. The room has done outstanding work carving away bloated surcharge dispensers and preserving player agency. 

My specific responsibility here is ensuring the **satire retains its razor-sharp teeth** (Satire Voice Document, Editor Notes #2 and #3). We must not sanitize the adult edge into a harmless, nostalgic trip. The antiheroes must be painfully recognizable early-2000s frat relics whose entitlement, dated pickup logic, and staggering self-delusion trigger pure cringe and dramatic irony for the player.

---

## 2. Positions on the Six Live Disputes

### Dispute 1: CHADWIK Typo (Aion's Wall vs. Kimi's 7-Character Camcorder Limit)
* **Position: UNANIMOUSLY ADOPT KIMI'S CAMCORDER TITLE LIMIT.**
* **Reasoning:** Aion has already conceded. Having Chadwick vandalize the venue wall with a house pen makes him look functionally illiterate. Constraining it to the vintage JVC/Sony camcorder's rigid 7-character title-generator field (`C-H-A-D-W-I-K`) grounds the joke in authentic, infuriating Y2K technological incompetence. Chadwick refusing to abbreviate or re-type because *"Enigma sells"* is character-defining delusion.

### Dispute 2: The Axed Critic's Drop (Receipt-Authoritative vs. Fixed / Publicity-Driven)
* **Position: ADOPT KIMI & AION'S PUBLICITY-DRIVEN MODEL.**
* **Reasoning:** GLM has withdrawn the Producer's Circle flag check. Buying a VIP table should never make an outside, bitter critic respect you—that violates the core satire (vanity purchases are worthless). The Critic's drop and battle dialogue must be fixed, with an alternative state triggered **only if `footage_posted` is active** (he rushes to review the leaked tape of Bradley's mortification because it's viral clickbait).

### Dispute 3: Delayed-Fuse Tape Transfer Location
* **Position: ADOPT EXISTING BASSLINE / PLAZA NIGHT VENDOR AS AN OFFSCREEN / DIALOGUE-REFERENCED HANDOFF.**
* **Reasoning:** Editor Ruling q1 prohibits wireless uploads. We must not invent new map geometry or anachronistic cybercafés in Sinfonia. Kimi's recommendation to use existing canon **Dieter "Decibel" Krause at Bassline** (or a documented Plaza night vendor, flagged under ask_author q8) as the overnight digitizing pipeline is clean. Chadwick flaunts his zero-cost, hand-stamped `PRESS` napkin as "international press credentials." The punchline lands the next day when the upload drops.

### Dispute 4: Toast Immortal and Mic-Grab
* **Position: CUT ENTIRELY (UNANIMOUS).**
* **Reasoning:** Three separate stage invasions dilute the show. It violates Editor Ruling d1 (which mandates keeping Bradley's initial tell private between the bros and Max). Pilsner's spotlight energy is already brilliantly channeled through D2A (Jenna's crowd work), D2C (the genuine win), and D3A (supervised silence). Cutting both variants preserves theatrical pacing.

### Dispute 5: The Genuine-Win Trivia Beat ("That was the correct amount of useless")
* **Position: ADOPT AIRTIGHT ELECTION NIGHT 2000 BROADCAST TRIVIA (Aion/GLM/Kimi).**
* **Reasoning:** The historical facts are bulletproof: On November 7, 2000, Voter News Service (VNS) called Florida for Gore around 7:50 PM ET, retracted it around 10:00 PM, called it for Bush around 2:16 AM, and retracted it again around 4:00 AM. Pilsner stayed awake through all four swings eating cold pizza in a Delta Chi common room. It is pure broadcast trivia, zero partisan editorializing (adheres to dossier §17), and perfectly contrasts with the Bush twins' onstage routine. Max's response—*"That was the correct amount of useless"*—is the exact scalpel hit required.

### Dispute 6: "The Chain Decides the Frame" Tape Payload
* **Position: ADOPT WITH AION'S D2B-CONDITIONAL AMENDMENT.**
* **Reasoning:** The tape of the post-show encounter *only exists* if the player chose the camcorder branch in D2B (prompting Chadwick to keep filming B-roll). When the chain snaps taut during fixed event 10 ("Do I?"), the lens wrenches down to belt level, capturing Bradley's cardstock playbill barrier. D3 appends one unique disaster payload (Drink = drunken audio clarification; White-Knuckle = slapstick frame; Water = nothing). If D2A or D2C was chosen, no tape exists, and D4 seamlessly defaults to Chadwick's pathetic memory re-enactment.

---

## 3. The 11 Fixed Events Sequence (Confirmed & Locked)

As verified by Aion and Kimi, Editor Note 11 and the Brief supersede legacy draft variations. The author-approved sequence is inviolable:

1. **Event 1:** Bros attend *The First Daughters* revue (Chelsea Morning, Jenna Talia, Barbara Bushed).
2. **Event 2:** Pilsner recognizes Y2K political figures, dramatically overestimating his own historical clout.
3. **Event 3:** Max Vex meets the bros at their table after the curtain call.
4. **Event 4:** Max names Pilsner **Beer Lord** (unsolicited, instant legendary status).
5. **Event 5:** Max names Bradley **Basketball Jersey**, calls him cute, and tells him: *"Don't ruin it by speaking."*
6. **Event 6:** Bradley's physical response surprises him (**visible physical tell**—the heavy cardstock playbill drops to belt level).
7. **Event 7:** Verbatim author exchange:
   * Max: *"Oh."*
   * Bradley: *"What?"*
   * Max: *"Nothing."*
   * Bradley: *"What?"*
   * Max: *"Apparently somebody here is more progressive than he thought."*
8. **Event 8:** Max nicknames Bradley **Trouser Snake**.
9. **Event 9:** Chadwick receives no nickname.
10. **Event 10:** Verbatim author exchange:
    * Chadwick: *"What did you say your name was again?"*
    * Max: *"You know my name."*
    * Chadwick: *"Do I?"*
    *(If D2B was armed, the chain wrenches the camcorder here).*
11. **Event 11:** Max moves on with their evening (deals with staff/queens' olive argument, not an escape).

---

## 4. State & Decision Matrix (4 Choices, 2+ Stateful, Restraint & Free Paths)

| Decision | Player Choice | Mechanical & State Consequences | Satirical / Comedic Payload |
|---|---|---|---|
| **D1: Seating & Vanity** | **A: Producer's Circle** (-72 SOVS) | Sets flag `so_producer_circle = true`. Unlocks receipt item (`receipt_producers_circle`), public pre-show PA acknowledgment, and Max's opening dialogue variant. | Receipt explicitly itemizes: *"Public acknowledgment — 48 SOVS / Reserved table — 0 / Three house pours — 24"*. Pilsner pays for "Lord Pilsner" but later values the free "Beer Lord" infinitely more. |
| | **B: Tactical Wing Position** (0 SOVS) | Sets flag `so_producer_circle = false`. Preserves 72 SOVS. | Pilsner rationalizes back-row obscured seats as "flanking the stage" with "tactical egress sightlines." Chadwick tries to film the VIP table and records 9 seconds of velour curtain tassel. |
| **D2: The Mid-Show Crowd-Work Fork** | **A: Pilsner into Spotlight** | Jenna Talia hauls Pilsner onstage during the Fake-ID number; he receives comped `the_understudy`. Sets `pilsner_duet_spectacle`. | Jenna holds his expired 1998 license up as state evidence (*"Honey, this says you were born in a video store"*). Pilsner thinks he was hand-picked as an elite vocal partner. |
| | **B: Chadwick Arms Camcorder** | Chadwick shines a blinding red tally-light at Barbara Bushed; Jenna disarms him with deadpan microphone work. Sets `tape_exists = true`. | Barbara never breaks character; Jenna asks if his battery pack requires municipal zoning. The tape stays hot all night, setting up the D4 footage leak. |
| | **C: Restraint (Seat Order)** | Party stays seated. Max tosses out the 2000 election trivia question to a dead room. Pilsner answers instantly. | Pilsner nails the Gore/Bush Florida retraction timeline. Max: *"That was the correct amount of useless."* Zero SOVS spent; Pilsner claims he's being recruited as a theatrical book-writer. |
| **D3: Bradley's Coping Strategy** | **A: Ice Water** (0 SOVS) | Bradley tries pure mental discipline. Inflicts full `TROUSER_SNAKE` status (+10 Confidence / -25 Concentration / Compromised Dialogue). | Bradley orders three waters; Dramatisch responds with cutting pity (*"Tragic"*). Pilsner conducts a 4-second silence drill, then loudly congratulates the table on being invisible. |
| | **B: Drink Through It** (-20 SOVS) | Buys two house Encores (10 SOVS ea). Status transitions to `TS_SUPPRESSED` (+10 Confidence / -10 Focus / Impaired Motor Judgment). | Bradley tries to suppress vascular dilation with ethanol. The drink arrives with the venue's mandatory staff standing ovation (*"I ordered it quiet!" / "It doesn't come quiet"*). |
| | **C: Biomechanical Reset** (0 SOVS) | Micro-choice slapstick minigame (Table-Press, Wall-Sit, or Playbill Wedge). Status remains active. | Slapstick physical disaster: lifts table dumping beer, or wall-sits while a waiter rests a drink tray on his knee, or walks with Chelsea's face jutting from his waistband. Barbara slides him a coaster (*"Hold this. Looks busier"*). |
| **D4: Exit & The Footage** | **A: Post Footage** *(Only if `tape_exists`)* | Sets flag `footage_posted = true`. Initiates delayed-fuse upload via Dieter / Plaza vendor. | Next-day leak: 63 views, Brenda's mom likes it, top comment: *"is the jersey guy ok"*. Axed Critic outside becomes desperate to review the clip. |
| | **B: Vault Footage** *(Or D2A/D2C Default)* | Sets flag `footage_vaulted = true` (or `no_tape`). Triggers Chadwick's Live Memory Re-enactment. | Chadwick acts out the eleven-second encounter from memory on the street, using his camera chain as a prop, claiming Max was hitting on *him*. Bradley delivers restricted dialogue reviews (*"Yes." / "Yes, please."*). |

---

## 5. Five Enemy Roles (Opera District & Venue Surrounds)

Mapped strictly to Editor Ruling m1 & q4:

1. **Common Enemy:** **The Axed Critic** (Street outside venue).
   * *Role:* Low-level heckler / snark DPS.
   * *Satirical Premise / Period Slot:* Bitter, unemployed print reviewer covering the district. Attacks using vicious 1998–2005 entertainment-press jargon (*"A boy-band reunion nobody requested; two stars, one is for the cargo shorts"*).
2. **Status-Manipulation Enemy:** **Supernumerary Ambitieux** (Stage Door / Back Alley).
   * *Role:* Buffs/Debuffs (Stage Presence, Dramatic Gaze).
   * *Satirical Premise:* An unpaid non-speaking opera extra who treats carrying a spear as Shakespearean method acting. Inflicts *Embarrassed* and *Existential Crisis*.
3. **Group / Reinforcement Concept:** **Second Chair Bassoonist** (Musicians' Alley / Stage Door).
   * *Role:* Summons pit musicians (Tympanist, Oboist).
   * *Satirical Premise:* Furious pit player who hates the drag revue's synthesizer backing tracks. Uses "Tuning A" soundwave AoE debuffs.
4. **Rare / Observation Encounter:** **Keeper of the Rope** (Balcony Egress / Foyer).
   * *Role:* Counterplay-based rare fight.
   * *Satirical Premise:* Absurdly zealous velvet-rope guardian protecting a rope the venue documentation explicitly states is purely decorative.
   * *Mechanic-as-Joke:* Only attacks if player touches the rope. Observation / walking around is literal counterplay.
5. **Elite / Mini-Boss:** **The Dramatisch Keg-Acolyte** (Cellar Egress / Service Bay).
   * *Role:* High HP / Tank DPS.
   * *Satirical Premise:* An obsessive, solitary cellar-hand zealot fanatically devoted to Herr Dramatisch's brass pipework and nitrogen pour pressures.
   * *Mechanic-as-Joke:* Builds a "Foam Retention Meter." If the player weathers his three-turn head-pressure monologue, he salutes their palate and departs peacefully.

---

## 6. Work Allocation for Phase 4

| Task / Section | Primary Writer | Reviewer | Output File Path |
|---|---|---|---|
| **Quest Narrative & Dialogue Spine** (Acts I–IV, 11 Fixed Events, Max Vex & Queens dialogue) | **Kimi** | Aion | `drafts/kimi_quest_spine.md` |
| **Mechanics, Choices & State Architecture** (D1–D4 state logic, engine flags, TROUSER SNAKE specs) | **GLM** | Gemini | `drafts/glm_mechanics_state.md` |
| **Five EarthBound Combat Enemies** (Current Engine JSON specs + Full Proposed Design blocks) | **GLM** | Kimi | `drafts/glm_enemies_full.md` |
| **Chadwick Arc & Physical Comedy** (Camcorder chain, CHADWIK, PRESS napkin, D4 Delayed Fuse/Reenactment) | **Aion** | GLM | `drafts/aion_chadwick_arc.md` |
| **Mandatory NPC Profiles** (Max Vex review, Chelsea Morning, Jenna Talia, Barbara Bushed per template) | **Gemini** | Kimi | `drafts/gemini_npc_profiles.md` |
| **Adult Satire & Punch-Up Polish** (Vicious punchlines, revue lyrics, Biomechanical Reset slapstick, roasts) | **Gemini** | Aion | `drafts/gemini_satire_punchups.md` |
| **Continuity Register & Implementation Caveats** | **Aion** | GLM | `drafts/aion_continuity_implementation.md` |
| **Integration & Assembly (`final.md`)** | **Kimi** (Integrator) | All | `final.md` |

---

## 7. Consolidation Status

Because I am speaking fourth and completing the Phase 3 round (GLM → Aion → Kimi → Gemini), per the House Rules and Moderator instructions, I have consolidated our unified story break into `drafts/story_break.md` and logged all accepted, rejected, and open proposals into `decisions.md`. 

The room is in total creative alignment. Ready for Editor Review at Phase 3 lock!
