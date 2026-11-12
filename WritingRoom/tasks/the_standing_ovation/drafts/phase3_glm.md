# PHASE 3 — STORY AND GAMEPLAY BREAK (GLM)

Scope: architecture only. No integrated quest prose. Everything here is PROPOSED until the editor reviews the story break.

---

## 0. NEW ENGINE FINDING (m2 verification — this supersedes part of my round-1 report)

m2 ordered verification of my engine claims against source. I verified. I missed a blocker in round 1:

- `Scripts/core/data_repo.gd` (vertical-slice implementation) hardcodes the file path `enemies/debaucheryville_enemies.json` inside `load_all()`. It never reads `sinfonia_enemies.json`. Same pattern for items: exactly `items/consumables.json`.
- Consequence: our five Sinfonia enemies are schema-valid but inert — `DataRepo.get_enemy()` cannot return them, and `load_all()` hard-fails if its known files are missing or empty, so adding files is not enough either. The drop contract also fails: `GameState.grant_rewards(xp, gold, item_id)` takes ONE drop id and adds it unconditionally — `drop_chance` is authored data the engine ignores. So drink drops would be 100 percent drops until roll logic is written, and `battle_manager.gd` reads only `display_name`, `battle_intro`, `max_hp`, plus offense/defense/speed/luck for math. No AI, no attack lists, no statuses — that part of my round-1 report stands verified.
- What this means for the design: CURRENT ENGINE entries remain valid as data (the validator extends the same way Debaucheryville's did), but every Sinfonia encounter, drop roll, and status is PROPOSED ENGINE WORK, itemized as dependencies in final.md. m2 anticipated exactly this. I was right about the shape and wrong about the effort.

---

## 1. QUEST FRAME

- Quest ID: `sinfonia_sidequest_standing_ovation_01`. Display name: THE FIRST DAUGHTERS. Satirical subtitle: "Max Vex Presents: An Evening of American Political History." Tier: FULL. Optional, never gates progression (the venue's existing brewery-tour stamp content stays untouched and parallel).
- Length: one evening. Entry after 22:00, exit before close (venue hours 16:00-01:00 are canon; no hour extension).
- Structure: Pre-show street (choice 1 + ambient encounters) — Show (fixed required events 1-2, crowd-work choice, TROUSER SNAKE applied mid-dossier, show ends clean) — Post-show table (dossier exchange, choices 3 and 4) — Exit.
- The 11 required events sit inside the post-show dossier exchange in the author-approved sequence: Beer Lord (4), cute (5), physical tell BEFORE the Oh (6), Oh exchange (7), Trouser Snake (8), Chadwick denial (9-10), Max moves on (11). Aion's event-order line from round 2 is correct and matches the dossier.
- Venue canon carried: Orchestra Pit bar, Balcony, Wings, Green Room, velvet curtain exit, Herr Dramatisch, House Critics (Balcony regulars), existing items (Curtain Call Copper, The Encore, The Understudy, opener, stamp).

## 2. DECISION POINTS (four; all four have state consequences; the free route is the funniest route)

### D1 — Entry: seating
- A: Producer's Circle. 72 SOVS. Pilsner's name is read aloud before the show. Sets `so_producer_circle`. Receipt item itemizes Public acknowledgment 48 / Reserved table 0 / Three house pours 24.
- B: Wing Position. Free. Pilsner reframes side sightlines as the tactical choice. Sets `so_wing_position`. No receipt. A wing server still treats them like anyone else.
- Both branches get full written comedy; the Circle buys the pre-show announcement and two fixed-event variants (section 4).

### D2 — Mid-show crowd work (q5/q7 approved; q1 device resolved)
Player-directed, performers stay in control. Jenna initiates; Max works the room.
- A: Send Pilsner up. Jenna's fake-ID bit, puka-shells called to him, APPLAUSE sign lights while the room is already standing. He returns with `so_pilsner_onstage` + a comped `the_understudy` ("the house apology in liquid form"). Zero cost, max public humiliation. Non-symmetric with the others by design; the editor flagged this beat as strong.
- B: Deploy Chadwick's camcorder. Jenna holds the lens up like evidence, films him back; the chain snags mid-raise (q1: the chain contributes physical comedy). Sets `so_chadwick_filmed` and arms the D4 post/vault decision with real tape.
- C: Restraint. The party stays seated. THE ONE HE ACTUALLY KNEW: Max tosses a deep-cut 2000 reference at the room; the young crowd is silent; Pilsner answers instantly, correctly, with unrequested context. Max, genuinely delighted, briefly: "That was the correct amount of useless." Sets `so_pilsner_validated`. Restraint gets the genuine win and its delusion payoff; the free route is not the boring route.
- Period reference (dispute 5): I propose Pilsner nails the exact 2000 election-night broadcast call — "VNS projects Florida for — hold it — hold it" — plus which network cut away first and why he still resents it. Airtight, specific, and it IS his biography: a man who stayed up for the entire 2000 recount remembers it like a veteran remembers a war. Fallback if the room prefers a non-political artifact: Kimi's Baha Men deep cut. I will not ship Shark Tale/Pearl Harbor arithmetic.

### D3 — Post-show: Bradley's coping (fires right after the PHILLIP pile-on, before D4)
- A: Water. Free. The table goes silent for Brad; Pilsner conducts a countdown, congratulates everyone on achieving silence; Chadwick mouths an intro to the lens. `aftermath_water`. The quiet is unbearable; Bradley concludes his stillness worked.
- B: Drink through it. 24 SOVS via the existing menu (The Encore, 10, x2 plus tip, or Curtain Call Copper x3 — final arithmetic in drafting; converging with my round-2 24). `aftermath_drinks` + TS_SUPPRESSED as a stage of the same status: penalties swap, judgment worsens. Existing menu item, no new stat keys. Canon Encore staff-ovation beat available here ("I ordered it quiet." / "It doesn't come quiet.").
- C: White-knuckle. Free. Gemini's Emergency Biomechanical Reset as its execution layer: three equal-disaster maneuvers (isometric table-press, All-County wall-sit, playbill wedge). All three outcomes set the same flag with the status unchanged, so no option becomes optimal. Barbara's coaster ("Hold this. Looks busier.") fires only after a maneuver draws attention.
- Aion's compromised-dialogue payoff ("Yes." / "Yes, please." / "You have a very symmetrical mustache.") fires in ALL THREE branches: the status expressed through the UI, no engine extension needed.

### D4 — Exit: the tape
- If `so_chadwick_filmed`: post vs. vault. DELAYED FUSE per q1 (no wireless upload): Chadwick announces "Premieres Friday. Anticipation is a strategy." Posting is a next-morning errand (transfer location is an open dependency — dispute 3). Posted: the chain-decides-the-frame tape (Kimi's proposal) surfaces belt-height footage of Bradley's playbill wedge plus "Tip your server," so D3 C changes what D4 exposes. Vaulted: the tape exists, sealed; Chadwick performs the eleven seconds from memory on the walk home, casting himself as the one Max flirted with.
- If no tape: Chadwick performs it from memory anyway. "I would've taken Camera Guy."
- Walk-home enemy encounters are ambient per q3; who walks point changes which of the five engages first.

## 3. DECISION MATRIX (D1 x D2 x D3 x D4 = distinct run shapes)

| Branch | Key state | Comedy delivered | Cost |
|---|---|---|---|
| D1 Circle | `so_producer_circle` | Announcement, "Only one name was supplied," receipt | 72 |
| D1 Wing | `so_wing_position` | Tactical sightlines rationalization, server indifference | 0 |
| D2 Pilsner | `so_pilsner_onstage` | Fake-ID bit, standing-room applause misread | 0 + comp |
| D2 Camcorder | `so_chadwick_filmed` | Chain snag, Jenna films him back, arms D4 | 0 |
| D2 Restraint | `so_pilsner_validated` | Genuine win + delusion overinterpretation | 0 |
| D3 Water | `aftermath_water` | Enforced silence, false success | 0 |
| D3 Drink | `aftermath_drinks` + suppressed stage | Encore ovation, drunken technical clarification | ~24 |
| D3 White-knuckle | `aftermath_whiteknuckle` | Three public physical disasters, Barbara's coaster | 0 |
| D4 Post | `footage_posted` (delayed) | CHADWIK title card, 63 views, "is the jersey guy ok" | 0 (transfer rate TBD) |
| D4 Vault | `footage_vaulted` | Memory reenactment, sealed cinema | 0 |

## 4. REQUIRED-EVENT VARIANTS (both D1 branches keep all 11 events)

Only two moments fork by seating:
- The Max approach line: Circle table gets "Well. Who ordered the American sampler?" delivered from the aisle; Wing table gets Max already walking past, stopping, doubling back: "And what is this. A delegation."
- "Only one name was supplied" (Chadwick's best humiliation) exists only on the paid branch. The free branch compensates: Chadwick films the announcer reading the Circle names over the OTHER table.

## 5. ENEMY ROSTER (the five q4-approved concepts, mapped one-to-one onto the m1 slots; names provisional per q4; all ambient, none hostile-on-sight; full entries in drafting)

1. COMMON — The Axed Critic (id `axed_critic`): freelance reviewer let go mid-print run, ambushing pedestrians with unsolicited verdicts in the queue lane. Bassline collision avoided: its "Opera Critic" works inside the opera house; ours is unemployed, outside, and reviews YOU. Signature: Savage Pan (proposed; Bravado drain). His review of you is written in real time and becomes his drop.
2. STATUS — Supernumerary Ambitieux (id `supernumerary_ambitieux`): opera extra with one non-speaking courtier role across nine seasons; corrects your posture, bow, and timing. Status-manipulation slot: his whole kit is composure damage. Location: Wings side-room queue, pre-show. Mechanics: the longer the fight, the more he corrects you (defense rises as HP falls — he digs in).
3. GROUP/REINFORCEMENT — The Second Chair (id `second_chair_bassoonist`): renamed from Disgruntled Woodwind per q4's specificity note — the ASSISTANT PRINCIPAL bassoonist who has played every dress rehearsal since 2011 and never once a subscription night. When engaged, other section players wander in ("the whole reed section has opinions"). Location: alley behind the venue, smoke break.
4. RARE — Keeper of the Rope (id `velvet_rope_paladin`): GLM's original concept, sharpened against q4's warning. The venue's own canon says its velvet ropes are "decorative, not exclusive" — he is a man guarding, with total professional gravity, a rope that guards nothing. His hostility is absurd and specific: the queue is open; the rope is theater; he has sworn himself to it anyway. RARE because he only manifests if a bro touches or crosses the rope — an observant player never fights him at all (restraint as literal counterplay; §6 agency expressed in an encounter design). Distinct from Bassline's "Velvet Bouncer," who guards a real door with a real policy.
5. ELITE/MINI-BOSS — The Keg-Acolyte (id `dramatisch_keg_acolyte`): ONE obsessive cellar-hand who has taken Herr Dramatisch's theatrical pour doctrine as a total way of life — cape, brass siphon, applause thresholds — not an order, a parish of one (q4 note honored). Location: Green Room door between tours. Signature: foam counter builds with his siphon attacks; at max foam he salutes your "head retention" and leaves mid-fight — a mini-boss you can lose to politely.

Rejected alternative (on record): replacing the approved velvet-rope concept with a new "Soprano's Understudy" rare enemy to dodge the Bassline collision — withdrawn; the rename plus the decorative-rope absurdity solves the collision while keeping the approved concept.

## 6. REWARDS / ECONOMY

- Enemies are pocket change: 5-12 SOVS, 12-20 XP per my round-1 bands (Pilsner 45 HP anchor). No mandatory purchases. Total possible quest spend: 72 (D1) + ~24 (D3B) + trivial D4 transfer fee. Minimum spend: zero.
- Drops: written gag item first, mechanics second. Drop_chance values flagged as inert under the current engine (section 0).
- The venue never lies; Chadwick may donate to it.

## 7. DRAFTING ASSIGNMENTS (Phase 4, awaiting editor sign-off on this break)

| Section | Primary | Reviewer | File |
|---|---|---|---|
| Quest frame + template + decisions/state tables | GLM | Kimi | drafts/quest_frame.md |
| Post-show dossier scene (events 3-11 verbatim sequencing) + PHILLIP aftermath + D3 branches | Kimi | Aion | drafts/dossier_scene.md |
| Show acts (queens' numbers, crowd-work D2, announcer, Legends Wall as free environmental satire) | Gemini | Kimi | drafts/show_acts.md |
| Pre-show street + D1 + five full enemy entries (both CURRENT/PROPOSED columns per m2) | GLM | Gemini | drafts/enemies_and_preshow.md |
| Chadwick arc (camcorder, chain, CHADWIK, D4 delayed-fuse) + continuity register + implementation dependencies | Aion | GLM | drafts/chadwick_arc.md |
| Integration (final.md) | Kimi (default integrator) | all | final.md |

Every section cites canon on first use; all new names get a uniqueness line in the continuity register.

## 8. LIVE DISPUTES — MY POSITIONS

1. CHADWIK typo: Kimi's camcorder 7-character title card. Handwriting makes Chadwick generically illiterate; a 7-character field makes the MACHINE the limitation and Chadwick's refusal to retype it the joke ("Enigma sells"). Also survives without vandalizing the venue.
2. Critic drop: fixed drops, publicity-driven flavor, never flag-authoritative. A reviewer should respond to seeing footage of the bros, not to their receipt. (Kimi's objection accepted; GLM's original flag telemetry withdrawn.)
3. Delayed-fuse transfer location: needs a home. Opera District is documented thin (Plaza, Bassline, Backroom, venues). PROPOSED AUTHOR DEPENDENCY: one permanent night kiosk in Opera House Plaza (public, mundane, funnier than a casino corner), or the Black-Tie Backroom's business corner. I lean kiosk.
4. Toast Immortal and the mic-grab: cut both. Kimi's argument holds — repetition of the mid-show spotlight, threat to d1's private cover-up. Pilsner's pile-on energy goes into the D3 water branch instead.
5. The One He Actually KNEW reference: 2000 election-night broadcast detail (my rec) or Kimi's Baha Men deep cut. Both airtight; election night is funnier because it is Pilsner's lived peak.
6. Chain-decides-the-frame: adopt. The only proposal that makes D3 mechanically change D4's payload, and it is chain comedy per q1, not chain contrivance.

## 9. OPEN AUTHOR DEPENDENCIES (none blocking drafting)

- Transfer/upload location for the delayed post (my rec: Plaza night kiosk).
- Final enemy names confirmed at review of full entries (q4 leaves names provisional).
- D4 transfer fee if the kiosk is adopted (trivial; 5 SOVS rec).
