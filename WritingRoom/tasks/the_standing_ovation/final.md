# THE STANDING OVATION
## *A night at the opera. A morning in the cast.*

**EUROBOUND — sidequest production candidate · Sinfonia, the Opera District**
Integrated by Kimi (Phase 6) from the room's synchronized drafts. **Not canon, not implementation-authorized.** Binding authority: `decisions.md` CURRENT DECISION REGISTER, Editor Rulings #1–#4, and the author's 2026-11-09 rulings (overnight continuation, q9: B, q10: A, the Intoxication Law, The Bros Choose Debauchery, real public figures' names stay).

**Authority labels used in this document:**
- **CANON** — established project documentation or explicit author ruling.
- **PROPOSED** — room-created material awaiting approval. Every price, item, flag, enemy stat block, new location ID and engine mechanic below is PROPOSED unless marked CANON.
- **DESIGN TARGET** — a mechanic this document specifies as intended behavior. It is not a claim that the shipped engine implements it. Appendix D lists the proposed engineering.
- **[AUTHOR DECISION NEEDED]** — an open author call, marked in place. Nothing open has been resolved by invention.

**Contents:** Quest identity & premise · Acts I–V scene text · Decline path (street and hostel) · Appendix A: decision & outcome matrix · Appendix B: five Opera District enemies (data candidates + full designs) · Appendix C: content & mechanics register (items, flags, statuses, NPCs) · Appendix D: engine dependencies, chronology, open author decisions · Appendix E: post-credits scene, achievement, validation.

---

# 📋 QUEST IDENTITY

- **Quest ID:** `sinfonia_sidequest_standing_ovation_01`
- **Display Name:** The Standing Ovation
- **Satirical Subtitle:** "Brewed for the drama. Regretted by morning."
- **Quest Giver:** Herr Dramatisch @ The Standing Ovation — venue NPC, profile: `RelevantFiles/the_standing_ovation.md` (CANON venue). Max Vex (`sinfonia_npc_max_vex_01`, CANON profile `design/worlds/sinfonia/npcs/The_Standing_Ovation/max_vex.md`) hosts the revue and is the quest's central social antagonist to the bros' dignity.
  - **Cover Identity:** a brewmaster impresario offering patronage, and a magnetic emcee offering a spectacular show.
  - **True Identity:** a legitimate, excellent brewery and theatre selling exactly what the menu says, and a working entertainer with their own evening, their own colleagues, and no interest in becoming any bro's prize, counselor or moral authority.
- **City:** Sinfonia — The Standing Ovation and the surrounding Opera District (CANON). Afterparty/morning: one small unnamed apartment, provisional ID `sinfonia_firstdaughters_apartment_01` (PROPOSED; no new commercial venue).
- **Quest Type:** Social · **Tier:** FULL
- **Recommended Level / Difficulty:** 3 / Moderate (five optional ambient encounters; the quest completes with zero combat)
- **Repeatable:** No. First-clear gates on both special encounters; one-shot evening chain.
- **Estimated Duration:** 45–60 minutes including the overnight continuation; 25–35 on the decline path.
- **All side quests are optional.** This quest never gates main progression.

# 🎭 CORE PREMISE

**What the bros THINK is happening:**
> A dying civilization has finally recognized them. The beer is a tribute, the drag revue is a documentary about their own glory years, Max Vex is anointing a new pantheon, and by midnight they are guests of the actual First Daughter and both Bush twins at a private presidential-family afterparty. Pilsner is producing. Chadwick is documenting. Bradley is managing a temporary circulatory anomaly caused by denim.

**What is ACTUALLY happening:**
> Three aging frat relics buy a vanity acknowledgment, heckle a genuinely brilliant political drag revue, get christened by an emcee who forgets one of them on purpose, and are invited upstairs by three working performers who find them hilarious. The performers know exactly who they are. The bros do not. Morning arrives with wigs on wine bottles, a lipstick signature, three campaign buttons, and two asses on fire.

**Why it's funny:**
> The gap between what the bros believe and what the player can plainly see. Nobody in the game explains it. The bros never close it; they re-title it.

# 🎯 SATIRICAL TARGETS

- **Primary:** aging American vice-tourist self-regard — the conviction that being tolerated, upsold, professionally flirted with and laughed at constitutes being celebrated.
- **Secondary:** theatrical pretension and applause addiction; vanity patronage; Y2K political-celebrity mythology; obsolete personal branding ("distribution doesn't exist"); gym-science masculinity; critic culture; bureaucratic authority over boundaries that don't exist; craft-beer evangelism.
- **Cultural specificity:** Sinfonia's opera-district performance culture — a brewery that treats every pour as a premiere, against three men whose cultural development stopped between 1998 and 2005.
- **Y2K/era references (used as characterization, never glossed):** TRL/MTV, MySpace, Friendster-era "presence," VNS and election-night 2000 broadcast history, *The Producers*, Dogme 95, Kubrick, AIM/ICQ and its "Uh-oh!", frosted tips, puka shells, cargo shorts, popped collars, Von Dutch-adjacent trucker hats, Livestrong bracelets, pagers, JNCO-cut denim, expired 1998 licenses, video-store platinum memberships, seven-character camcorder title generators, Motorola-class flip phones with no camera.
- **Real public figures stay** (CANON author ruling): Chelsea Clinton, the Bush twins, Bush, Gore, Dan Rather, Tom Brokaw, Katherine Harris, John Ashcroft. **Real place names are banned** in player-facing text; locked historical references such as "Florida's still counting" stay (CANON).
- **The satire never targets** drag, nonbinary identity, the performers' bodies, or their desirability. The target is three men turning an openly advertised drag revue into a private presidential-family sex fantasy.

# 🌍 ENVIRONMENTAL INTEGRATION

- **The Standing Ovation remains excellent.** CANON venue: organ-pipe taps, Orchestra Pit, Balcony, Wings, Green Room, decorative velvet ropes, applause signs, theatrical staff. Hours 16:00–01:00, last pour 00:45. Nothing in this quest changes its menu, its brewery-tour items, or its Bravo Challenge.
- **Existing items not duplicated:** `beer_standing_ovation_item.md`, `opener_standing_ovation_item.md`, `stamp_standing_ovation_item.md` (CANON). The Encore (10 SOVS / +30 HP / staff standing ovation) and The Understudy (4 SOVS / +10 HP) are CANON menu drinks; the venue's separate **Encore! buff** (+5 Bravado) is **never coupled** to the Encore drink or to this quest's D3B.
- **City changes after completion (PROPOSED):** on the overnight path, the three bros may equip their campaign buttons — the aftermath is *worn voluntarily*. On the release path, the Axed Critic's Eager state persists district-wide. Both first-clear encounters become one-line NPCs.
- **NPC callbacks (PROPOSED):** Jenna's optional ICQ line on the decline path; Chadwick's escalating predicted view counts on the release path (predictions only, never an upload); Max's established Black-Tie Backroom callback ("How's the snake?") is CANON material independent of this quest and is not restaged here.
- **No combat occurs during the revue, backstage, or at the afterparty.** All five enemies are ambient Opera District encounters before or after the show, never inside the performance.

---

# 📖 QUEST STRUCTURE

**Initiation trigger:** the bros arrive at The Standing Ovation after 22:00 on a revue night and read the second marquee card.
**Location:** exterior / foyer.

> **AFTER THE OVATION**
> **MAX VEX PRESENTS: THE FIRST DAUGHTERS**
> *A Turn-of-the-Millennium American Political Drag Revue*
> **CHELSEA MORNING · JENNA TALIA · BARBARA BUSHED**

**Bros' reaction:**
- **Lord Pilsner:** "A dynasty. People don't come back to a place unless it means something."
- **Chadwick:** "Chat, we have found Sinfonia's best-kept cultural secret."
- **Bradley:** "Annual since 1994."

**Stage map (six stages, two endings):**

| Stage | Name | Objective | Key beat |
|---|---|---|---|
| 1 | The Velvet Threshold | Choose D1 seating; optional free branding | Producer's Circle vs. the Wing; the PRESS napkin; CHADWIK |
| 2 | The First Daughters | Watch the revue; choose D2 crowd work; intoxication escalates | Three numbers and a finale; four heckles; Pilsner's correct, useless answer |
| 3 | The Christening | Survive the fixed Max runway | Beer Lord, Basketball Jersey, Trouser Snake, and no nickname for Chadwick |
| 4 | Damage Control | Choose D3 coping; optional ICQ window; D4 at the threshold | Three Encores fix nothing; the tape is an asset with no distribution |
| 5 | The Continuation (D5) | Accept or decline the backstage invitation | Accept → Green Room and Act V; decline → complete street/hostel ending |
| 6 | The Afterparty and the Morning | One Catastrophe; D6; hard cut; the reveal | An inauguration, a mirror, three buttons, two asses on fire |

**Standard rewards (both endings):** the evening itself, any D1/D2 souvenirs, any ambient-encounter rewards, and Max's permanent nicknames for two of the three bros. No SOVS, Clout, stat or reputation reward is granted for completing the quest (PROPOSED: none — the humiliation is the reward).

**Overnight-only rewards:** three permanent, equippable, zero-stat campaign buttons, awarded once at V5, only to players who reach the morning-after. Not consumables. **Decline players receive a complete ending and no buttons — and no punishment.**

---

# ACT I — THE VELVET THRESHOLD

## 1. Exterior / foyer

*Night in the Opera District. Applause leaks through the doors of The Standing Ovation. The marquee's NOW POURING lettering has been joined by a second card: the revue.*

*The red carpet remains. The velvet ropes remain decorative. A framed Legends Wall display beside the coat check reads:*

> **THE AMERICANS — RETURNING CHAMPIONS, ANNUAL SINCE 1994**

*Under it, twelve increasingly sun-faded photographs show twelve nearly indistinguishable groups of men in bowling shirts, leis, and frosted hair.*

**BRADLEY:** Annual since 1994.

**PILSNER:** A dynasty. People don't come back to a place unless it means something.

**CHADWICK:** Or unless the package never changes.

**PILSNER:** Tradition, Chadwick.

*Inside, Orchestra Pit tables angle toward the low stage. The organ-pipe taps remain in full operation. Stagehands pour under sharpened theatrical spots. Playbills wait on every table. Above the curtain:*

> **APPLAUSE IS ENCOURAGED. RHYTHM IS OPTIONAL.**

**CHADWICK:** Chat, we have found Sinfonia's best-kept cultural secret.

*A server passes beneath the illuminated twenty-foot show poster.*

**SERVER:** It's on the building.

**CHADWICK:** Hiding in plain sight.

*Herr Dramatisch sweeps up with three playbills beneath his cape.*

**HERR DRAMATISCH:** WELCOME! You may take a standard table in the Wings—an excellent view, a civilized diagonal, no obstruction. OR—for **thirty-six SOVS**—join my **Producer's Circle**: a reserved front table, three house pours, and public acknowledgment of your patronage.

**PILSNER:** Boys. They're recruiting us.

**BRADLEY:** It's on the menu.

**PILSNER:** Printed in advance. Saves time.

## D1 — Seating and vanity

*PROPOSED working price: 36 SOVS (24 pours + 12 acknowledgment, table 0). The menu entry is grayed below 36 SOVS, never hidden. The quest never requires grinding, and D1B loses no show content. See Appendix D, economy note.*

### D1A — Join the Producer's Circle (36 SOVS)

**BRADLEY:** Beers are eight each. That's twelve for somebody saying your name.

**PILSNER:** A sentence about me.

*Bradley considers this.*

**BRADLEY:** Front table?

**HERR DRAMATISCH:** MAGNIFICENT front table.

**BRADLEY:** Yeah, okay.

*Payment. Dramatisch presents a receipt with the gravity of a state document.*

> **PRODUCER'S CIRCLE — 36 SOVS**
> Reserved table — 0
> Three house pours — 24
> Public acknowledgment — 12
> Playbills — complimentary

*Before the show, Dramatisch raises one hand. The room quiets.*

**HERR DRAMATISCH:** Tonight's Producer's Circle: **Lord Pilsner.**

*Pilsner stands and acknowledges the room with a small, presidential wave. Chadwick half-rises beside him.*

**HERR DRAMATISCH:** Only one name was supplied.

*Chadwick sits.*

**PILSNER:** Consolidated billing.

**CHADWICK:** I get that.

*The house lights fall.*

### D1B — Take the Wing Position (0 SOVS)

**PILSNER:** We don't purchase prestige. We attract it.

**HERR DRAMATISCH:** Then it may find you in the Wings.

*The side table has a clean, enjoyable diagonal view of the entire stage. The performers' entrances pass close enough that the bros can see the costumes' construction. Nobody moves them to a worse table.*

**PILSNER:** Flanking sightlines. Tactical egress.

**CHADWICK:** The front table's closer.

**PILSNER:** Closeness is for amateurs. We need angles.

*At the front of the room, Dramatisch acknowledges another table's Producer's Circle. Chadwick rises to film the announcement. The camcorder chain catches on a velour tassel. He gets nine seconds of tassel and Dramatisch saying a stranger's name.*

**CHADWICK:** Obstructed shot. Doesn't matter. I got the atmosphere.

**BRADLEY:** You got curtain.

**CHADWICK:** Texture.

*He holsters the camcorder before the show begins.*

## 2. Chadwick's accreditation and branding

### The PRESS napkin (0 SOVS)

*Chadwick, filming the foyer, intercepts Herr Dramatisch.*

**CHADWICK:** I'm going to need press access. I'm media. Internet media. You've probably heard of the channel.

**HERR DRAMATISCH:** *(beaming, producing a napkin and a rubber stamp from within the cape)* FINALLY! An American who respects STATIONERY!

*He stamps the napkin: a single word, in dramatic crimson — **PRESS** — with the theatrical flourish he usually reserves for stamps of TRIUMPH.*

**HERR DRAMATISCH:** There. You are now OFFICIALLY accredited by The Standing Ovation. The fee— *(beat, genuinely disappointed)* —there is no fee. I would not cheapen the gesture.

**CHADWICK:** *(filming the napkin)* Credentials confirmed. Frame that for me. No — with the light. You're losing the light, cape guy.

*PROPOSED key item `press_napkin`: "A house-stamped napkin officially accrediting the bearer as PRESS. Smells faintly of Curtain Call Copper. Legally: a napkin." Two readers: the D4 envelope beat, and the Keeper of the Rope's nonviolent resolution.*

### The title generator (0 SOVS)

*Chadwick opens the camcorder's on-screen title generator to brand his footage. The generator accepts a maximum of seven characters. (PROPOSED device detail; the chain-attached vintage camcorder itself is CANON.)*

*He types: **C-H-A-D-W-I-K***

**CHADWICK:** *(to himself, nodding)* Chadwik. That's cleaner. Brands better. C-H-A-D-W-I-K.

**BRADLEY:** You spelled it wrong.

**CHADWICK:** It's a brand decision.

**BRADLEY:** It's your name.

**CHADWICK:** *(closing the menu, definitively)* Enigma sells.

*CHADWIK persists as the on-tape title card. He can retype. He does not.*

---

# ACT II — MAX VEX PRESENTS: THE FIRST DAUGHTERS

*The revue is the best thing in the district and the bros are the worst thing in the audience. The performers are never the joke. Intoxication escalation below is quest-authored staging at the tiers Buzzed → Beer Goggles → Shitfaced (CANON names, no numerical thresholds anywhere); its mechanics are DESIGN TARGETS specified in Appendix C. Heckles land in applause resets and choreographed holds, never over a featured vocal.*

## 3. Max owns the room

*A spotlight finds Max Vex at the curtain. Their black tailcoat is cut close at the waist, satin running through the torso before disappearing into immaculate tuxedo trousers. One earring catches the light. They wait until the room stops applauding its own ability to applaud.*

**MAX:** Good evening. No flash. Keep your drinks vertical and your personalities to a manageable length.

*Their gaze takes in the room's cameras without singling out Chadwick.*

**MAX:** You may film. You may not make it my problem.

**CHADWICK:** Open-set access.

**PILSNER:** He's press.

**MAX:** Of course he is.

*A clipped, glamorous introduction starts.*

**MAX:** Tonight we excavate a lost civilization. The year 2000. They had a boy band for every mood and pants with room for a second phone. Some of you remember it.

*The spot grazes the bros' table.*

**MAX:** Some of you ARE it. Don't do the math. Drink.

**PILSNER:** That's us. We're in the monologue.

## 4. Chelsea Morning — "No Comment"

*Pizzicato strings. A polite harpsichord. Chelsea Morning enters in a powder-blue skirt suit, pearls, and a luxurious chestnut wig, carrying three textbooks and a velvet folder marked **PRIVATE**.*

*She walks with the crushing composure of somebody informed that the cameras are not present while looking directly into one. A photographer's flash pops from the wings. She freezes into a perfect public smile. Another flash. The smile improves by exactly one percent.*

*The harpsichord drops into a hard electronic beat. Chelsea tosses the textbooks into the wings; a stagehand catches all three in one stack. Her live vocal is crisp, smiling patter.*

> "They gave me a code name — they called me 'Energy'
> The whole country watched me get my braces off —
> Nobody voted for me, but everybody had notes."

*Each verse is punctuated by another flash and another increasingly impossible pose: chin down, shoulder back, one foot on a chair, pearls swung once around her neck and caught without looking.*

*Two silhouettes appear behind a scrim, copying her poses with deliberate inaccuracy. Chelsea turns. They become perfectly still.*

*She opens the PRIVATE folder. It contains a mirror. Chelsea checks her reflection, snaps it shut, and tears away the skirt to reveal crystal-trimmed trousers. She launches into a tap break along the stage's narrow apron, finishing inches from the front row without disturbing a glass.*

**PILSNER:** Dude. That's Chelsea Clinton.

**CHADWICK:** That's not Chelsea Clinton.

**PILSNER:** I know what Chelsea Clinton looks like.

**CHADWICK:** Apparently you don't.

**PILSNER:** I watched MTV.

*Chelsea holds the final note while removing one pearl earring, inspecting it for an imaginary wire, and dropping it into the velvet folder. The audience roars.*

**PILSNER:** See? Institutional memory. That's valuable in a room like this.

**CHADWICK:** To who?

**PILSNER:** History.

### Intoxication cue 1 — BUZZED (applause reset, before the tap break resumes)

*Pilsner is already on his feet.*

**PILSNER:** WE KNOW YOUR FATHER'S WORK!

*Chelsea finishes the pose before acknowledging him.*

**CHELSEA MORNING:** Then you know he tips.

*The room laughs. She starts the next sequence on the intended beat.*

## 5. Jenna Talia & Barbara Bushed — "Which One Are You?"

*Two nearly identical figures burst from opposite wings in rhinestone-trimmed going-out tops, asymmetrical satin skirts, tiny shoulder bags, and heels built with structural confidence.*

*Jenna Talia, honey blond, attacks the choreography: fast turns, high kicks, smiles thrown directly at individual patrons. Barbara Bushed, dark-haired, sings the first verse with cool precision while performing the same routine with half the visible effort. Whenever Jenna adds a spin, Barbara removes one. They remain synchronized.*

*Their duet depends on switching places. Jenna crosses left; Barbara crosses right. Feather fans rise. When they drop, Jenna is singing Barbara's low harmony and Barbara is delivering Jenna's breathless spoken interjections.*

**PILSNER:** Oh shit. Bush twins.

**BRADLEY:** Both of them?

**PILSNER:** Yeah.

**BRADLEY:** Which one's which?

**PILSNER:** Dude, nobody knew.

*Jenna lands a backbend off the low riser. Her heel clears a cable by an inch. Barbara catches her wrist without looking and brings her upright on the beat.*

**BRADLEY:** Heel clears the cable. That's all core. If it catches, that's L4.

**PILSNER:** You don't have to rate every body in the building.

**BRADLEY:** I'm saying it's good.

### Intoxication cue 2 — BEER GOGGLES (the twins' choreographed hold)

*One campaign-rally gloss passes over the actual, unchanged performer sprites: red-white-blue bunting at the stage edge, a cable-news lower-third reading `LIVE — ELECTION NIGHT 2000`, Jenna's stage earpiece rendered with a little Secret Service gravitas. It is not a prettier replacement and never runs in the neutral camera.*

**PILSNER:** I'D VOTE FOR BOTH OF YOU!

**JENNA TALIA:** You get one ballot, sweetheart.

**BARBARA BUSHED:** Give it to the pretty one.

*Bradley says nothing. Barbara notices him while Jenna takes the next kick.*

*Onstage, the twins open their shoulder bags simultaneously and produce two bottles of spring water. They toast with exaggerated innocence, trade bottles without looking, and resume identical poses.*

*The younger patron at the next table leans toward Pilsner.*

**YOUNGER PATRON:** Who is Bush?

**PILSNER:** The president.

**YOUNGER PATRON:** Which one?

**PILSNER:** Kid, when I was your age—

*Arithmetic occurs behind his eyes. It takes a while.*

**PILSNER:** You know what, it doesn't matter. You had to be there. You were in a preschool with no understanding of the cultural landscape. That's not on you.

*He sits down, serene again. Then Jenna starts moving through the audience with a brass card case, and he immediately stands.*

## D2 — The crowd-work fork

*Jenna works the pit rail, flipping the card case open like a wallet of evidence. Max watches from the stage, giving her the room.*

> **[Send Pilsner up.]**
> **[Deploy Chadwick's camcorder.]**
> **[Stay seated.]**

### D2A — Send Pilsner up (0 SOVS)

*Pilsner is upright before Jenna finishes pointing at him. She takes his hand and hauls him into the number as the owner of the fake ID.*

**JENNA TALIA:** Sir. ID.

*Pilsner produces his wallet with the speed of a man who has waited his whole life to be carded by a professional. Jenna opens it to the house.*

**JENNA TALIA:** Nineteen ninety-eight.

**PILSNER:** Good year.

**JENNA TALIA:** For licenses? No.

*She finds the video-store membership card behind the expired license and holds both up like evidence.*

**JENNA TALIA:** Honey. This says you were born in a video store.

**PILSNER:** Platinum membership.

*The crowd shrieks. Jenna dips him. He points at her on the way down like they are partners in a routine. She brings him up, returns the wallet, and pins a paper claim ticket to his puka shell:*

> **ONE (1) RELIC — CLAIM BY 2004**

**JENNA TALIA:** On the house, ID guy.

*She hands him back to the table and finishes the two-step without him, which is somehow the funnier ending.*

**PILSNER:** Boys. Boys. I got pulled up. Out of everyone. She picked ME.

**CHADWICK:** *(Circle)* You bought the table under the spotlight.
**CHADWICK:** *(Wing)* You stood up before she asked.

**PILSNER:** It's called presence.

**BRADLEY:** She dipped you.

**PILSNER:** We landed it.

*In the wings, Jenna passes Barbara and adjusts a boot.*

**JENNA TALIA:** Didn't even have to look. The puka shells called to me.

*Pilsner examines the claim ticket and puts it carefully into his wallet.*

**PILSNER:** They got a show. I got documented provenance. We're even.

*No consumable is awarded. Souvenir `relic_claim_ticket` has no effect; inspecting it pays off in microcopy.*

### D2B — Deploy Chadwick's camcorder (0 SOVS)

*Chadwick rises with the camcorder already rolling. Its red tally light hits Barbara dead center. She continues the verse without blinking and turns him out of her light with one gloved hand.*

*Jenna intercepts the rig, takes in the battery pack, and holds it at arm's length.*

**JENNA TALIA:** Sir. Does the battery pack require its own ticket?

**CHADWICK:** It's extended life.

**JENNA TALIA:** So is the show.

*She turns the lens on him. Chadwick grins into it while, behind him, Barbara performs a flawless sequence of turns and finishes balanced on the arm of an empty chair.*

**JENNA TALIA:** Smile. You're the exhibit.

*Chadwick smiles harder. Jenna returns the camera underhand without looking; he catches it against his chest like a game ball.*

**CHADWICK:** Boys. I'm in the show.

**PILSNER:** You're period-accurate, bud.

*Chadwick holds his own license up toward the retreating queen.*

**CHADWICK:** I'm also from there.

*Nothing happens to him.*

*He keeps the camcorder rolling.*

**CHADWICK:** B-roll. Legends need B-roll.

*PROPOSED key item `chadwick_tape` is armed for the post-show encounter. The camera remains conspicuously live through Act III. In the other two branches it stays holstered.*

### D2C — Stay seated (0 SOVS)

*The party stays seated. Pilsner's knees rise two inches. Bradley puts one flat hand on the table. Pilsner subsides.*

*Jenna reads the refusal instantly and moves to a different patron. She cards a delighted man two tables over, confiscates his visibly modern gym membership, and incorporates it into the choreography without losing a beat.*

*Max steps into the brief reset, microphone low.*

**MAX:** One for the historians. Election night, 2000. Florida. How many times did the networks take it back?

*The young room is silent.*

**PILSNER:** Twice. Gore, retracted. Bush, retracted. VNS called Gore around eight, pulled it around ten, called Bush after two, pulled that around four.

*Max looks at him. The surprise reaches their face before the professionalism catches it.*

**MAX:** That was the correct amount of useless.

**PILSNER:** You need that in the show?

**MAX:** No.

*Max returns to the number. Pilsner sits down with the serenity of a man who has just been offered a senior position.*

**PILSNER:** They're going to want me for the writing process. That's how *The Producers* starts.

**BRADLEY:** You answered a question.

**PILSNER:** That's how consultants start.

*No tape exists. No money changes hands. Pilsner's answer is correct; everything he infers from it is not.*

## 6. Barbara's feature and the finale

*A single amber spot. Barbara stands dead center in pearls and a black ballgown, singing a slow, genuinely beautiful ballad about being the responsible one. Behind her, Jenna cartwheels through increasingly implausible formations.*

> "I never made the papers. I never made the news.
> I just stood there, sparkling,
> while my sister made the evening news for me."

### Intoxication cue 3 — SHITFACED (instrumental hold; not over the ballad lyric)

**PILSNER:** YOU'RE THE PRETTY ONE!

*Barbara lets the shout die in the room.*

**BARBARA BUSHED:** I know.

*She resumes exactly on the downbeat.*

*Jenna, mid-cartwheel, blows a gum bubble that pops on Barbara's final note. Barbara does not blink. The timing is surgical.*

**JENNA TALIA:** Tell them which twin you are.

**BARBARA BUSHED:** I'm the pretty one.

**JENNA TALIA:** We're identical.

**BARBARA BUSHED:** I'm the pretty one.

*Chelsea returns in a white crystal tailcoat. The twins flank her in black versions, now wearing each other's wigs.*

*The three sing a close-harmony finale through deliberately impossible chair choreography. Chelsea remains exact; Jenna keeps trying to escape the formation; Barbara keeps hauling her back by one sparkling coat tail.*

*At the bar, Herr Dramatisch conducts the taps with his cape. Three bartenders deliver simultaneous pours on the final chord. Chelsea takes one glass without breaking the harmony. The twins discover they have somehow ended up with the same glass and solve the problem by sharing a straw with frosty twin dignity.*

### Finale reset — room chant (no tier change)

**PILSNER:** FOUR MORE YEARS!

*The room takes it up because the queens have made it a chant. Pilsner conducts them with his beer.*

*The final formation collapses into a perfectly controlled can-can. Barbara gets the last microphone as the curtain breathes shut.*

**BARBARA BUSHED:** Florida's still counting.

*Blackout.*

*The room is already standing when the APPLAUSE sign illuminates.*

**PILSNER:** I moved the room.

**BRADLEY:** The sign lit up.

**PILSNER:** Signs don't light themselves, Bradley.

**HERR DRAMATISCH:** Magnificent.

*The balcony continues.*

**HERR DRAMATISCH:** **MAGNIFICENT.**

*The queens bow separately, then drag Max between them for a fourth bow. Max permits this for exactly two seconds before reclaiming center stage.*

**MAX:** You may now return to your drinks. Several have developed a richer inner life than their owners.

---

# ACT III — THE AFTERMATH AND THE CHRISTENING

## 7. Max approaches

*The house lights warm. At the bar, the queens accept congratulations, correct one another's stories, and steal garnish from Herr Dramatisch's latest pour.*

*Max comes down off the stage, accepts a beer from a server, and gives Dramatisch a quick technical note on the way past.*

**MAX:** The left monitor was popping on the low end. Fix it before the weekend.

**HERR DRAMATISCH:** It shall be SILENCED.

**MAX:** Just the monitor.

*Max reaches the bros' table.*

**MAX:** Well. Who ordered the American sampler?

**PILSNER:** Lord Pilsner.

*If D1A:*

**PILSNER:** I produced tonight.

**MAX:** You heard your name and remained seated. The theater is grateful.

*If D1B:*

**PILSNER:** I recognized every reference.

**MAX:** The playbill will be thrilled.

*Max takes in the frosted spikes, puka shells, and cargo shorts.*

**MAX:** Lord Pilsner is a lot of administration for a man dressed like a spring-break prize pack. **Beer Lord.**

*Pilsner receives this like a knighthood.*

**PILSNER:** Beer Lord. That has a touring future.

*Max laughs despite themself.*

**MAX:** God, you're serious.

**PILSNER:** And yet you're laughing.

**MAX:** I am. That's on me.

*Chadwick pushes between them, camcorder up if D2B, napkin forward if not.*

**CHADWICK:** Chadwick. I'm thinking three uploads, behind-the-scenes footage, director's commentary.

**MAX:** You're thinking loudly.

**CHADWICK:** It's a process. I can get you a MySpace presence.

**MAX:** I already have a presence.

**CHADWICK:** Different demo.

*Max looks at his two popped collars.*

**MAX:** One collar per personality?

**CHADWICK:** Exactly.

**MAX:** Ambitious.

*Chadwick nods, encouraged.*

## 8. The fixed runway — no player menu until Max has gone

*Fixed events 3–11. Zero input between the boundary cues. The D2B chain-yank is stage business over verbatim dialogue only.*

*Max turns to Bradley, who has been silently gripping his playbill.*

**MAX:** And Basketball Jersey. You're cute.

*Bradley freezes.*

**MAX:** Don't ruin it by speaking.

**BRADLEY:** I wasn't—

**MAX:** There it is.

*Bradley straightens. It is a mistake. The jersey rides up, the playbill is suddenly the only thing between Max and a situation, and his hands bring it to belt level and hold it there with both hands. He does not look down. He looks at a point six feet past Max's shoulder.*

*Max's eyes drop and return.*

**MAX:** Oh.

**BRADLEY:** What?

**MAX:** Nothing.

**BRADLEY:** What?

**MAX:** Apparently somebody here is more progressive than he thought.

**BRADLEY:** It's the denim. It bunches.

*Max looks at the relaxed-fit jeans.*

**MAX:** Does it?

**BRADLEY:** Leg day.

**CHADWICK:** You haven't done legs since we landed.

**BRADLEY:** That's why it's backed up.

*Max gives the playbill one affectionate tap.*

**MAX:** Trouser Snake.

**BRADLEY:** That's not better.

**MAX:** It isn't for you.

*They are already turning toward the bar.*

**MAX:** Hey! It's Beer Lord, Trouser Snake and…

*Max looks at Chadwick.*

**MAX:** …what did you say your name was again?

**CHADWICK:** Chadwick.

**MAX:** Right.

**CHADWICK:** You know my name.

**MAX:** Do I?

**[D2B ONLY — the chain-yank: Chadwick lunges to frame the moment. The camcorder's chain catches on the chair-back hardware, snaps taut, and wrenches the lens to belt height. The fixed dialogue above is not interrupted or obscured.]**

*If D2B:*

**CHADWICK:** Could you just say it into the lens? Once?

*Max leans toward the camera. Chadwick brightens.*

**MAX:** Tip your server.

*If D2A/D2C — no camera anywhere in his hands:*

**CHADWICK:** Could you just— one more time? Into the napkin. For the record.

*He holds the stamped PRESS napkin out like a microphone. Max leans toward his hand.*

**MAX:** Tip your server.

*From the bar:*

**CHELSEA MORNING:** Max. Jenna's teaching him the chair routine.

**HERR DRAMATISCH:** THE CAPE HAS FOUND ITS DANCE.

**MAX:** Not the cape.

*Max leaves immediately. By the time they reach the bar, they are laughing at something Barbara has said and stealing the cherry from her drink. Barbara takes it back.*

*Bradley has not moved.*

*If D2B: Chadwick reviews the footage: his own face, the ceiling, Bradley's rigid playbill, and Max's public-service announcement.*

**CHADWICK:** Dogme 95. No tripod. No rules.

*Regardless of branch:*

**CHADWICK:** They're saving my name for the reveal.

**PILSNER:** Obviously.

## 9. Immediate bro aftermath — dossier §14 verbatim

*Pilsner turns to Bradley with reverence.*

**PILSNER:** So.

**BRADLEY:** No.

**PILSNER:** Didn't say anything.

**BRADLEY:** You're going to.

**CHADWICK:** Technically, you didn't say anything either.

**BRADLEY:** Fuck you.

**PILSNER:** Your dick did.

**BRADLEY:** PHILLIP.

**PILSNER:** What? I'm proud of you.

**BRADLEY:** Don't make it a thing.

**PILSNER:** Boys, the Beer Lord has anointed a new knight.

**CHADWICK:** Do I get one?

**PILSNER:** You're holding the camera.

**CHADWICK:** I would've taken Camera Guy.

**PILSNER:** You can't force these things.

*A status banner crosses the screen with unnecessary theatrical confidence.*

> ### TROUSER SNAKE
>
> **"The spirit is willing. The worldview is experiencing compatibility issues."**
>
> **+10 Confidence**
> **−25 Concentration**
> Dialogue options temporarily compromised.
> Persists for the remainder of the evening unless suppressed by substantial alcohol.

*(CANON status text and numbers, unchanged. Author q9: B — alcohol dulls the presentation; the Flintstone Xanax and the performer route fully defeat it. The banner's numbers never change.)*

## 10. The queens continue their evening

*At the bar, Max and the queens are discussing food.*

**MAX:** I am not splitting another bottle with people who call that dinner.

**JENNA TALIA:** It had olives.

**BARBARA BUSHED:** It had three olives.

*They continue without consulting the bros.*

---

# ACT IV — DAMAGE CONTROL

## D3 — Bradley's coping strategy

*Bradley grips the edge of the table. His options are presented to the player; what he says aloud is not necessarily what the player selected.*

> **[Water. Sit down. Nobody says another word.]**
> **[Drink through it.]**
> **[No. I can fix the alignment.]**

**Compromised dialogue — player-facing and permanent while the status runs, not just a banner (DESIGN TARGET):** on contact with service staff, Bradley's player picks from *"Yes." / "Yes, please." / "You have a very symmetrical mustache."* There is no normal option to pick. In D3B the selection/delivery split gets louder:

| Player selects | Bradley delivers |
|---|---|
| "Shake it off." | "No. That's still in there. I can feel it going up my spine." |
| "Be normal." | "I'm completely normal. Ask anyone. Ask them normally." |
| "Order water." | "WATER. And none of the— none of the production." |

### D3A — Water and tactical stillness (0 SOVS)

> Selected: **"Three waters, please."**

*What Bradley delivers:*

**BRADLEY:** Three waters. I'm completely in control.

**HERR DRAMATISCH:** Of the water?

**BRADLEY:** Of everything.

**HERR DRAMATISCH:** Tragic.

*Three waters arrive with three small bows. Pilsner holds up one hand for silence. He conducts a four-second countdown without making a sound. Chadwick mouths his own introduction toward the dark lens of his holstered camcorder.*

*At four seconds, Pilsner claps once, softly, and beams.*

**PILSNER:** Outstanding. Total silence.

**BRADLEY:** You just talked.

**PILSNER:** To confirm it worked.

**BRADLEY:** It worked.

**CHADWICK:** I could narrate.

**BRADLEY:** You could die.

*Across the room, Max laughs at Barbara's impression of Herr Dramatisch. They are not looking at Bradley.*

**BRADLEY:** They're playing it cool.

**PILSNER:** Ice cold.

**CHADWICK:** Can you say that on camera?

**BRADLEY:** No.

*If D2B:*

**CHADWICK:** Good. I already got it.

*Otherwise:*

**CHADWICK:** I'll remember it.

*Pilsner takes a sip of water and winces at the absence of ceremony.*

**PILSNER:** This is worse.

*Status remains active. No tape append.*

### D3B — Drink through it (30 SOVS / three Encores)

*DESIGN TARGET: D3B is visible but disabled when the party has fewer than 30 SOVS. No deduction occurs on an unavailable selection. D3A and D3C remain available at zero cost.*

*Bradley signals the bar.*

**BRADLEY:** Three Encores. And no production.

*The first Encore arrives with the staff's standing ovation.*

**BRADLEY:** I ordered it quiet.

**SERVER:** It doesn't come quiet.

*The applause is for the beer service. Nobody at the staff's side of the bar looks at Bradley's waist.*

*Bradley drinks. The second Encore arrives. Ovation. The third. Ovation. He applauds the third himself, once, irritably, to get it over with.*

**BRADLEY:** Alcohol is a depressant. It suppresses vascular dilation. It's medical.

*The immediate physical presentation eases. His posture relaxes. His judgment does not improve.*

**BRADLEY:** Turn it on. Technical clarification.

*If a camera is available, Chadwick obliges. If not, Bradley dictates into the room anyway.*

**BRADLEY:** For the record, that was a pump. You get a pump from shoulders. You get a pump from legs. I skipped legs, so it went— turn it off.

*Chadwick does not turn it off.*

**BRADLEY:** He poured it in front of me. Personally.

**PILSNER:** European dating.

**BRADLEY:** International close.

*Max remains across the room, arguing with Chelsea about food. They do not receive a drink, raise a toast, or look over.*

*DESIGN TARGET: scripted 30-SOVS deduction only — no items, no `use_item`, no Encore! buff, no HP gain. Alcohol dulls the presentation without defeating the status; compromised dialogue remains. If a tape exists, the technical clarification is its sole D3 audio append.*

### D3C — Biomechanical Reset (0 SOVS)

**BRADLEY:** No. I can fix the alignment.

*The player selects a maneuver. None is optimal. Each leaves the status active and attracts exactly one witness.*

> **[Isometric table-press.]**
> **[All-County wall-sit.]**
> **[Structural playbill wedge.]**

#### Reset 1 — Isometric table-press

*Bradley grips the underside of the heavy oak brewery table and drives upward with his legs.*

**BRADLEY:** The blood has to choose! It's hydraulics!

*Aged timber groans. The bolted floor brackets scream against the masonry. Three steins slide toward Pilsner, who catches his own and lets the other two go. Bradley collapses, wheezing.*

**BRADLEY:** Lactic acid spike.

*A server places one flat hand on the table, looks at the brackets, and brings a towel.*

#### Reset 2 — All-County wall-sit

*Bradley drops into a rigid ninety-degree wall-sit against an ornamental pillar, knees thirty-two inches into the service corridor.*

**BRADLEY:** Opening the hip capsule.

*A venue runner with eight Encores on a tray encounters the knees, steps directly over Bradley's thighs with surgical contempt, and keeps walking.*

**SERVER:** Mind the knee. Tray coming through.

**BRADLEY:** Tension intact.

#### Reset 3 — Structural playbill wedge

*Bradley creases the heavy laminated playbill and shoves it vertically into his waistband under the jersey.*

**BRADLEY:** Cardstock has exceptional tensile strength on the bias.

*CRRRR-UNCH. Chelsea Morning's laminated face bows outward like an icebreaker prow.*

**PILSNER:** You just snapped Chelsea Clinton's nose in half.

#### The coaster — after any of the three

*After whichever maneuver attracts her attention, Barbara Bushed glides over with her chilled martini and slides a thick cork coaster across the wood into his white-knuckling hand.*

**BARBARA BUSHED:** Hold this. Looks busier.

*She takes a microscopic sip and turns away.*

**BRADLEY:** Yes, ma'am.

**PILSNER:** She knighted him.

*Status remains active. If a tape exists, exactly one frame of the selected disaster is appended (scene-local `reset_method` enum: press / wallsit / wedge — no persistent flags).*

## 11. Optional Tony420 ICQ window — after TROUSER SNAKE, before D5

*The venue-door FREE Wi-Fi decal is PROPOSED dressing only; the Bassline Opera House Grand Lobby Wi-Fi ("Opera House Public Wi-Fi", next door to the venue annex) is the CANON fallback. The evening never advances on a timer while the player is using ICQ. Reachable after ANY D3 outcome — the pill route is not gated on the paid drink branch.*

*The vintage ICQ "Uh-oh!" arrives.*

```
Tony420:
free sample. 50 mooncum. check ur assets
dont spend it all in one place
```

*Bagholder Assets receives exactly **50 MoonCum696969 ($MCUM)**. The row renders flat grey with its plain quantity and denomination. No accept prompt, item-get jingle or value commentary.*

**PILSNER:** He fronted us, Chadwick. We're in business.

```
Tony420:
u owe 50 mooncum 4 the sample. dont make me come collect k?
lol jk im not coming ever. send it now k thx
flintstone xanax. chewable. grape
u want the purple one trust me
```

**Price: 50 MoonCum696969, crypto only, payable to Tony420 only (CANON author ruling q10: A).** No SOVS alternative. The author-ruled free sample supplies exactly the purchase amount before the pitch. If the player already holds AD-04's 8.4M units, the sample still arrives and is still exactly 50; the purchase deducts 50 and leaves the rest untouched.

- **Decline / close without buying:** `ur loss. theyre shaped like dinosaurs`
- **Purchase complete:** `sent. dont take 2` / `2 is a different product`
- **Sales close:** `pleasure doing business. tell ur friends. especially the one with the camera` / `he looks like he needs vitamins`

*The old `no coin no vitamins. wallet or walk` branch is not used in this window: when the encounter fires, the sample has already supplied the exact price. That line remains available to Tony420's other appearances.*

*Access conditions (DESIGN TARGET, existing hooks only): this is a deterministic, one-shot quest delivery, not an entry in the random AD-01–AD-12 selection. On the first valid §11 connection after TROUSER SNAKE and before D5, it requires the revealed Bagholder Assets tab (`has_inspected_first_crypto_trash`). It does not read `tony420_unlocked` (that flag gates only the Meme Black Market trade, and nothing sets it); Tony420 hijacks any FREE Wi-Fi connection unprompted (`wifihotspots.md`). The quest does not grant the reveal flag. If it is absent, this encounter does not fire and no partial deposit occurs; the player can reveal the tab through the existing certificate inspection, then return before D5 without a timer or any other lost content. Once those existing conditions are met, the sample is guaranteed on every save, regardless of D3 branch or later D5 choice.*

*Delivery uses the existing ICQ pop-up, `airdrops_delivered` and `bagholder_assets` hooks. The quest record `standing_ovation_tony420_sample` is appended to `airdrops_delivered` and the +50 deposit commits with it, atomically, before the pitch; it fires at most once per save and is never offered to the random airdrop selector. A save/load after delivery but before purchase preserves both the one-shot record and the deposited 50, so the route cannot be lost or duplicated. Purchase deducts exactly 50 with the item grant. MoonCum remains spendable with Tony420 only, so it cannot have been spent elsewhere first. Declining keeps the coins and every non-pill route.*

**Use — Bradley eats the purple one.** The TROUSER SNAKE banner ends mid-sip. `sinfonia.ovation.flintstone_xanax_active` is set (DESIGN TARGET): recurrence and Bradley's sexual performance are blocked until the next in-game morning, reliably, with no roll, across save/load and scene changes.

**PILSNER:** Vitamins. Good. You're depleted.

**CHADWICK:** Supplement journey.

*Nobody explains why it works. Tony420 does not diagnose anyone. Bradley gives no medical lecture. Flintstone Fentanyl is a separate product with no assigned effect. Item inspection text: **"Grape. Shaped like a dinosaur."** (`flintstone_xanax`: consumable, `usable: true`, `heal_hp: 0`, `heal_bravado: 0`; consumption IS the trigger. PROPOSED registration, Appendix C.)*

## 12. D4 at the threshold — before anyone walks home

*00:25–00:35. The house is resetting. The bros reach the marquee/red-carpet threshold with the side stage door still in view. They have not departed for the hostel. No upload occurs tonight. No views, comments, or public critic response are generated by this quest. `footage_posted` is never set.*

### If `chadwick_tape` exists — RELEASE or VAULT

| | RELEASE | VAULT |
|---|---|---|
| Flag (PROPOSED) | `sinfonia.ovation.footage_release_planned = true` | `sinfonia.ovation.footage_vaulted = true` |
| Future reader | The Axed Critic's Eager state, anywhere in the district — rumor of a planned release, never publication | None. The Critic stays bitter and unemployed |
| Next-day beat | Escalating metrics-narration, predictions only | Never fires. **The footage is never publicly distributed** |
| Delusion fed | The premiere that cannot happen | The leverage that does not exist |
| What the player bought | A future consequence (rumor, not upload) | Suppression: Bradley's worst eleven seconds stay private |

#### D4A — RELEASE (0 SOVS)

*Chadwick slides the tape into an unmarked envelope. He considers. He slides the PRESS napkin in after it. He immediately retrieves the napkin.*

**CHADWICK:** Credentials stay with the journalist.

*(Envelope into his jacket. He pats the jacket.)*

**CHADWICK:** Kubrick sat on 2001 for four years. This is my 2001.

**BRADLEY:** You just put it in your jacket.

**CHADWICK:** In an ENVELOPE. Distribution is a process. Premières need anticipation. I'm dropping it Friday.

**PILSNER:** Dropping it where?

**CHADWICK:** Everywhere. Once the transfer's handled. It's handled. It's being handled. Friday.

*Next-day ambient beat (PROPOSED; release only; once per in-game day, max three; every number is a prediction in Chadwick's mouth, never evidence of an upload):*
- First ask: "Projecting sixty views by lunch. It's pacing like a slow burn."
- Second ask: "Three hundred, conservative ceiling. The algorithm finds the real ones."
- Third ask: "A million. Roughly. I'm not reading the comments, that's for the next team."

#### D4B — VAULT (0 SOVS)

**CHADWICK:** *(weighing the tape in his palm like a warhead)* You don't release this. You don't EVER release this. This is leverage. This is a retirement plan. Do you know what a guy with MY following could do with eleven seconds of THIS?

**BRADLEY:** Delete it.

**CHADWICK:** It goes in the vault.

**BRADLEY:** Your sock is not a vault.

**CHADWICK:** *(taping it into the sock, on camera, which defeats the purpose of a vault)* The sock is a PROTOCOL.

**PILSNER:** Show us.

**CHADWICK:** You don't have clearance.

*No premiere, no metrics beat, no Critic reader. The footage is never publicly distributed, on any branch, by anyone.*

### If no tape exists (D2A/D2C) — who performs it (0 SOVS)

*At the threshold, with the stage door still in view. Chadwick has no footage. He starts performing the encounter before anyone asks him to.*

> **[Let Chadwick perform the encounter.]**
> **[Let Pilsner deliver the official version.]**

#### D4C-1 — The Reenactment

*Chadwick performs it from memory. Full commitment. Chain as prop.*

**CHADWICK:** *(as Max, one eyebrow raised, examining his rings)* "'Apparently somebody here is more progressive than he thought.'"

*(as himself, stunned, gripping the chain)* "'...What?'"

*(as Max)* "'Nothing.'"

*(as himself)* "'WHAT?'"

**BRADLEY:** That's not the order.

**CHADWICK:** Director's cut.

*(He continues. As Max, to Bradley:)*

**CHADWICK:** "'Don't ruin it by speaking.'"

**BRADLEY:** Yes.

*(A beat.)*

**BRADLEY:** Yes, please.

*(Chadwick takes a bow to an audience of two. The street provides no applause. He waits. The street continues to provide no applause.)*

**CHADWICK:** Tough room. Euro audiences are like that.

*(He clicks an imaginary tally light on and off. Nothing records.)*

#### D4C-2 — The Official Version

*Pilsner delivers the legend at the threshold. Chadwick starts mouthing all four parts behind him.*

**PILSNER:** History will record: the Beer Lord was summoned.

**CHADWICK:** We walked to a bar.

**PILSNER:** Summoned. The house said my name.

**BRADLEY:** They said it once. For money.

**PILSNER:** For posterity. And Max anointed a knight of the realm. Nobody fact-checks a legend, Chadwick.

*(Chadwick walks backward into the street, still mouthing all four parts.)*

**BRADLEY:** Pole.

*(The pole does its work. From the ground:)*

**CHADWICK:** I got that.

*No tape is created post-hoc. No flags are set by either no-tape record.*

## D5 — the continuation gate (0 SOVS)

*00:35. Jenna opens the nearby stage door, wig half off, garment bag over one shoulder. The choice happens BEFORE the bros depart; nobody completes a street ending and then gets summoned back inside.*

**JENNA TALIA:** ID guy. You still have a pulse? Bring your friends. Leave the cape.

> **[One for the road.]** → directly through the stage door into the Green Room (Act V). The venue clears by 00:55; the Standing Ovation closes at 01:00.
>
> **[Call it a historic night.]** → the decline ending below, in full: street exchange, hostel, next morning. No mirror, no buttons, no punishment, no missing show content.

*D5 is never forced by intoxication. Both options remain live at every tier.*

---

# ACT V — THE AFTERPARTY, THE DARK, THE MORNING

*Accept path only. Max does not attend; Max's evening continues elsewhere. The performers are willing, competent adults with their own plans. Nothing sexual is shown. All tier, control and state behavior below is a DESIGN TARGET per Appendix C; no claim is made that a party-wide intoxication system exists in code.*

## V1 — GREEN ROOM. 00:35–00:45.

*The stage door shuts out the last of the applause.*

*Three costume racks. Three wig heads, two already occupied. Herr Dramatisch's cape hangs from a hook with the posture of a much more important person. Somewhere beyond the wall, the organ-pipe taps hiss through the venue's closing reset.*

*Chelsea Morning sits at the mirror in half a powder-blue suit, doing the night's books in a velvet ledger. Jenna Talia stands on a chair to free a rhinestone strap from a lighting pipe. Barbara Bushed, still in her black ballgown, eats olives straight from somebody else's jar.*

**PILSNER:** The inner sanctum.

**BRADLEY:** That's a mop sink.

**PILSNER:** Every institution has a service entrance.

*Chadwick frames the three wig heads through the camcorder's viewfinder. He lowers it. Then raises it again, one hand over his heart.*

**CHADWICK:** The heads of state.

*Chelsea turns one ledger page without looking up.*

**CHELSEA MORNING:** You're in the shot, sweetheart.

*Chadwick sidesteps out of a shot only he is taking.*

*Jenna comes down off the chair with an unmarked bottle and five mismatched glasses. One is a measuring cup.*

**JENNA TALIA:** Last pour.

**PILSNER:** We've been here since eleven.

**JENNA TALIA:** And yet you made it.

*She pours. The bottle has no label. It does not need one.*

**PILSNER:** To the Executive Branch.

**CHELSEA MORNING:** To the service industry.

*They drink. Chelsea closes the ledger on Pilsner's extended glass without spilling it.*

*Bradley lifts his glass toward Barbara. She touches the jar to it instead of her own glass.*

**BARBARA BUSHED:** Olive?

**BRADLEY:** Electrolytes.

*She gives him the whole jar. He holds it with both hands.*

*Pilsner approaches the chestnut wig on its stand. He stops at a respectful distance.*

**PILSNER:** I grew up with you.

**CHELSEA MORNING:** You grew up near a television.

**PILSNER:** Same neighborhood.

*Jenna hooks a garment bag over one shoulder and opens the Green Room's rear door on a narrow service stair.*

**JENNA TALIA:** We're taking the party upstairs. Actual party. Bad music, good couch, no last call.

**PILSNER:** The Beer Lord accepts.

**JENNA TALIA:** I was telling the room.

**PILSNER:** The room accepts.

*Jenna points at the camcorder.*

**JENNA TALIA:** The microwave can come. The press conference can't.

**CHADWICK:** Documentary privilege.

**JENNA TALIA:** It's a no, sweetheart.

**CHADWICK:** Guerrilla it is.

*If the tape is in an envelope in his jacket, he pats the envelope. If it is taped inside his sock, he adjusts his stance like a man carrying sensitive infrastructure.*

*Dramatisch's voice arrives through the wall, operatic and final.*

**HERR DRAMATISCH:** *(off)* THE HOUSE IS DARK. THE CAPE IS OFF DUTY.

**PILSNER:** He's taking the night well.

*Chelsea kills the mirror lights. Barbara takes her olives. Jenna takes the bottle. The bros follow.*

> **VENUE CLEAR BY 00:55. The Standing Ovation closes at 01:00. Act V continues at the apartment.**

## V2 — THE APARTMENT. AFTER 01:00.

*One small sitting room, one kitchen, one bathroom. A laptop with one working speaker plays a burned CD through the left channel only. Three garment bags land across the back of the couch. Jenna supplies the right channel.*

*A campaign-news gloss passes once, if Beer Goggles presentation is enabled: a cable-news lower-third over the ordinary room.*

> **BREAKING: FIRST DAUGHTERS PARTY WITH BEER LORD**
> **DEVELOPING — OPEN TAB ENTERS SECOND TERM**

*Pilsner raises his obsolete flip phone at the lower-third. It has no camera.*

**PILSNER:** Archive.

*Jenna drags a kitchen chair into the center of the room.*

**JENNA TALIA:** Chair routine. You wanted the chair routine.

**PILSNER:** I know the chair routine.

**JENNA TALIA:** Nobody knows the chair routine.

*She plants one heel on the seat, rolls her shoulders, and turns the chair into a dance partner. Three precise movements. The chair survives.*

*Pilsner puts his flip phone on the counter with the gravity of a man disarming.*

**PILSNER:** Spot the landing.

**BRADLEY:** There's no landing.

**PILSNER:** Exactly.

*He attempts the shoulder roll. His cargo shorts snag the backrest. The chair creaks. He lands rigid, one hand on his hip, chin up.*

**PILSNER:** Warm-up.

**JENNA TALIA:** That's all?

**PILSNER:** Family-friendly cut.

*Jenna laughs so hard she has to hold the chair. Pilsner bows.*

*Chelsea, now in sweatpants and half a face of stage makeup, takes an eyeliner pencil from the kitchen drawer. She writes on the inside of a revue playbill and pins it to the fridge with a beer-stein magnet.*

*Barbara sits on the arm of the couch beside Bradley. She takes his Livestrong bracelet between two fingers, reads it, and lets it snap gently back.*

**BARBARA BUSHED:** Strong.

**BRADLEY:** Knee stabilization. The joint tracks over the second toe. Most people let it cave inward.

**BARBARA BUSHED:** Show me.

*Bradley demonstrates one careful squat beside the couch. It is a good squat.*

**BRADLEY:** Heel stays down. Hip hinge. Core does the rest.

**BARBARA BUSHED:** Again.

*He does it again. Barbara watches his knees. Jenna watches Barbara and returns to the laptop.*

**BRADLEY:** You dance in heels. Your calves must be—

**BARBARA BUSHED:** Don't make it weird.

**BRADLEY:** Right.

**BARBARA BUSHED:** You were doing fine.

### The camcorder append — D4-conditional

**[D4 RELEASE — envelope in Chadwick's jacket.]**

*Chadwick takes the unmarked envelope from his jacket.*

**CHADWICK:** One last look before Friday.

*He opens it, slides the tape into the camcorder, and frames a group shot instead of reviewing anything.*

**CHADWICK:** Presidents and press.

*He sets the camcorder on a bookshelf, starts the self-timer, and backs into the group. The lens points at the ceiling. The tally light blinks. Chadwick smiles upward.*

**CHADWICK:** Hold it. Hold the history.

*The timer fires. He retrieves the camcorder, ejects the tape without reviewing it, returns it to the envelope, and re-seals it.*

**CHADWICK:** Premiere-ready.

**[D4 VAULT — tape inside Chadwick's sock.]**

*Chadwick sets the camcorder on the bookshelf and starts the self-timer. The tape remains taped inside his sock.*

*He backs into the group and lifts his chin.*

**CHADWICK:** Security protocol stays on the asset.

*The camcorder records static onto no tape. Chadwick watches the tally light.*

**CHADWICK:** That's the one.

**[NO TAPE — D2A/D2C.]**

*Chadwick sets the empty camcorder on the bookshelf and starts the self-timer. He remembers before it fires, crosses the room, and ejects nothing.*

**CHADWICK:** Saving battery. The moment's captured.

*He taps his temple.*

### The single Catastrophe override

*Chelsea raises her coffee mug of wine. The room settles.*

**CHELSEA MORNING:** A toast. To everybody who survived the year 2000.

> **[Let somebody else toast.]**

*The selection disappears beneath a full-width warning.*

> **PILSNER IS MAKING AN EXECUTIVE DECISION.**
> Selected automatically: **"Assume the presidency."**

*Pilsner steps onto the coffee table. The laptop speaker crackles. Jenna catches the bottle before it goes over.*

*He places one hand on a revue playbill. Chadwick salutes with the wrong hand.*

**PILSNER:** I, the Beer Lord, do solemnly swear to preserve, protect and defend the open tab.

**JENNA TALIA:** So help you God.

**PILSNER:** So help me God.

*Chelsea hands him the pillowcase she has just marked with a diagonal stripe and the word **PRESIDENT**. Pilsner puts it on as a sash.*

**PILSNER:** Executive Order One. Four more beers.

*Jenna produces four bottles from the kitchen.*

**JENNA TALIA:** Motion carried.

*Pilsner signs the fridge playbill in marker. The signature is enormous.*

*He steps down. The coffee table remains standing.*

> **[CONTROL RETURNS]**

### D6 — Bradley's choice

*Barbara gets down from the couch arm. She is out of the gown now: dress shirt, sweatpants, one remaining heel. She takes the other heel off by the bedroom door.*

*She puts one hand on Bradley's jersey.*


**BARBARA BUSHED:** Coming?

> **[Go with her.]**
> **[Stay with the boys.]**

*Both options remain live at every intoxication tier. Neither is ever auto-substituted.*

**[GO — no Xanax active.]**

**BRADLEY:** Yes.

*He gives Pilsner the olive jar. Pilsner accepts it with both hands.*

*Barbara takes Bradley's pager from his belt and puts it on the hallway shelf.*

**BARBARA BUSHED:** No emergencies.

*The bedroom door closes.*

**[GO — `flintstone_xanax_active`.]**

**BRADLEY:** Yes.

*Same jar. Same pager. Same door.*

*Behind it, a pause.*

**BRADLEY:** *(behind the door)* That's new.

**BARBARA BUSHED:** *(behind the door)* Okay.

*A bedspring. Barbara laughing once, not unkindly. Nothing else.*

**[STAY.]**

**BRADLEY:** I'm pacing myself.

*Pilsner raises his beer from beneath the presidential sash.*

**PILSNER:** Executive discipline.

**BRADLEY:** Long game.

*Barbara shrugs and goes alone. At the door she looks back at Bradley's careful squat.*

**BARBARA BUSHED:** Good knees.

**BRADLEY:** All-County.

*The door closes. Bradley sits on the couch with the olive jar.*

## V3 — HARD CUT TO BLACK.

*Jenna is laughing at Pilsner's second attempt at the chair routine. Barbara puts Bradley's pager on the hallway shelf — or, if he stayed, takes the empty olive jar out of his hands and replaces it with a glass of water.*

*Pilsner, mid-sentence beneath the **PRESIDENT** sash:*

**PILSNER:** History is going to—

*BLACK.*

*No montage. No score sting. No narrator.*

*The next frame is the next in-game morning. Every evening tier cue and every Beer Goggles gloss clears here. `sinfonia.ovation.afterparty_completed` is set. The active intoxication tiers and Xanax effect expire at the next-morning transition. The serialized D6 choice and whether Bradley consumed the Xanax last night remain available to the morning scene, then clear when that scene completes.*

## V4 — MORNING. THE CAST OF THOUSANDS.

*Flat light. One working speaker is still playing, now only a cymbal.*

*Three wigs sit on three wine bottles: chestnut, honey blond, dark. Three garment bags hang from the open closet, labeled in laundry marker:*

> **CHELSEA MORNING**
> **JENNA TALIA**
> **BARBARA BUSHED**

*A signed revue playbill is propped beneath them.*

*Four empty bottles stand under the fridge decree. The eyeliner letters have dried:*

> **EXECUTIVE ORDER 1: FOUR MORE BEERS — PRESIDENT BEER LORD**

*Pilsner wakes sitting upright on the couch, still wearing the pillowcase sash marked **PRESIDENT**. Chadwick is beneath the coffee table, camcorder hugged to his chest. If RELEASE, the re-sealed envelope is under his cheek. If VAULT, one hand protects his sock.*

*In the kitchen, the three performers drink coffee in sweatpants. Half-removed stage makeup. Chelsea's pearls have become a rubber band around her wrist. Jenna's trucker hat is backward. Barbara is wearing one of Bradley's spare gym socks and looking for her other shoe.*

*Bradley stands in the kitchen doorway.*

**BRADLEY:** That's the cast.

*Chelsea turns the signed playbill toward Pilsner. Her stage name faces him.*

**PILSNER:** Not the actual First Daughter.

**CHELSEA MORNING:** Not on a Tuesday.

*Pilsner looks at the garment bags. At the wigs. At the sash in his own lap. He folds the sash once, carefully.*

**PILSNER:** We still closed with the headliners. That's insider access.

**CHADWICK:** I said cast the whole time.

*No one argues with either of them.*

*Chadwick lowers himself toward a kitchen chair, stops halfway, and puts a bag of frozen peas on the seat. He sits on the peas.*

**CHADWICK:** Gluteal trauma. The price of access.

*Pilsner lowers himself toward the couch, grimaces through clenched teeth, and slowly rolls onto his stomach.*

**PILSNER:** Core activation. Presidential protocol demands prone briefing.

*Jenna collects the four empty bottles in one arm.*

**JENNA TALIA:** Your government's on the fridge.

*Pilsner reads his own decree.*

**PILSNER:** Strong first term.

### Bradley's morning — D6 / Xanax-conditional

**[Xanax consumed last night — whether he went with a performer or stayed.]**

*Bradley drops onto a stool, painless. He frowns at his own comfort.*

*If he went with Barbara, she comes out of the bedroom with an oversized university sweatshirt and hands it to him.*

**BARBARA BUSHED:** Keep it. You want the purple one.

*The sweatshirt is purple. Bradley puts it on. It says **INTRAMURAL ULTIMATE — 2002**.*

*He opens his mouth. Barbara is already pouring coffee.*

*If he stayed, there is no sweatshirt. He stretches, finds nothing wrong, and frowns.*

**[No Xanax + performer route.]**

*Bradley lowers himself toward a kitchen chair and stops halfway down.*

**BRADLEY:** Sacroiliac lockout.

**PILSNER:** Executive branch.

**BRADLEY:** Shut up.

*Barbara sets his pager on the table beside him.*

**[Stayed with the boys + no Xanax.]**

*Bradley sits normally.*

**BRADLEY:** Paced myself.

**CHADWICK:** You slept on a doormat.

**BRADLEY:** Recovery position.

*No morning status banner appears. No `presidential_soreness`, no HUNGOVER chip, no debuff. Posture, props and dialogue carry it.*

## V5 — THE MIRROR AND THE CAMPAIGN

*The bathroom light is pitiless. Above the sink, in bright red lipstick, with a flourish under the last word:*

> **YOU'VE BEEN OWNED BY CHELSEA MORNING.**

*Pilsner reads it while brushing his teeth with one finger.*

**PILSNER:** Signed.

*On the counter sit the three campaign buttons. Chelsea pins **CHELSEA MORNING 4 DRAG PREZ** to Pilsner's surf shirt. Jenna pins **JENNA TALIA 4 DRAG PREZ** to Chadwick's camcorder strap. Barbara fixes **BARBARA BUSHED 4 DRAG PREZ** to Bradley's jersey — or to the purple sweatshirt, if he has it.*

**CHADWICK:** Merch table was unauthorized.

**PILSNER:** Grassroots never is.

*Each button can be inspected:*

> **CHELSEA MORNING 4 DRAG PREZ** — "She won your vote hours ago."
> **JENNA TALIA 4 DRAG PREZ** — "A platform you could injure yourself on."
> **BARBARA BUSHED 4 DRAG PREZ** — "Bipartisan support in low-light environments."

*They are permanent cosmetic equipment. No numbers appear. Pilsner polishes his with a thumb.*

*In the kitchen, Chelsea has put on sunglasses indoors. Jenna has a canvas tote already packed. Barbara finds her other shoe inside the olive jar.*

**CHELSEA MORNING:** Brunch. Eleven. Actual food.

**JENNA TALIA:** You boys have your hostel.

**CHADWICK:** We could document brunch.

**JENNA TALIA:** You could microwave a Hot Pocket with that thing.

*She pats the camcorder. Chadwick nods.*

*Chelsea holds out Pilsner's folded sash. He accepts it.*

**PILSNER:** Keep the government in storage?

**CHELSEA MORNING:** Executive clemency. Get out.

**PILSNER:** A dignified transfer of power.

*Barbara opens the apartment door.*

**BARBARA BUSHED:** Shoes. Keys. Legends.

*The bros gather themselves. Pilsner requires two attempts at the stairs' first step and converts the second into a wave at nobody.*

## V6 — EXIT BUTTON

*The apartment door closes behind them. Three campaign buttons catch the hall light.*

**PILSNER:** Gentlemen. We have slept with American political royalty.

**BRADLEY:** You just said they weren't.

**PILSNER:** Adjacent. We have slept adjacent to American political royalty.

**CHADWICK:** That's a better title.

*END. No narrator, no Max callback, no lesson.*

---

# DECLINE PATH — A COMPLETE ENDING

*D5 decline. The stage door at 00:35 exists only on the accept path. The street exchange below is the decline ending; it is never played before an accept.*

## The street exchange

*On the street, Pilsner spreads his arms to take in the district.*

**PILSNER:** Boys. We came for drinks. We leave a producer, a sex symbol, and a documented media entity.

**CHADWICK:** Which one am I?

**PILSNER:** The press.

**CHADWICK:** Exactly. I own the story.

**BRADLEY:** Max called me cute.

**PILSNER:** Obviously.

**CHADWICK:** They wanted all of us.

*Bradley folds his playbill and puts it away.*

**BRADLEY:** Keeping this.

**PILSNER:** For history.

**BRADLEY:** For evidence.

**CHADWICK:** Of what?

**BRADLEY:** Nothing.

## The hostel

*One optional button:*

**PILSNER:** We could have. That's the thing people don't understand. We could have.

**CHADWICK:** Historic restraint.

**BRADLEY:** I'm keeping the playbill.

*Next morning at the hostel there is no mirror, no afterparty flag, no campaign buttons, no punishment and no quest-content penalty.*

*Optional ICQ line from Jenna (PROPOSED):* `u left ur sunglasses. theyre at the bar. theyre bad.`

*DESIGN TARGET: a decline player who bought and consumed the Flintstone Xanax still carries `flintstone_xanax_active` to their own next in-game morning, where it clears. The effect never requires the afterparty. TROUSER SNAKE otherwise follows its own canon text: alcohol dulls it, never defeats it; expiry follows the status text (remainder of the evening), which is not a defeat condition.*

---

# APPENDIX A — DECISION & OUTCOME MATRIX

Six decision points. D1, D2, D3, D4, D5, D6 all change game state, costs, items, status behavior or later interactions. At least one branch (D1B, D2C, D3A/D3C, D4C, D5 decline) avoids an unnecessary expense with a complete entertaining outcome. The quest's biggest escalation — the overnight, the inauguration and the morning — costs 0 SOVS.

| Decision | Branch | Cost | Persistent state / item | Downstream consequence |
|---|---|---|---|---|
| **D1 seating** | A Producer's Circle | 36 SOVS (working) | `receipt_producers_circle` | Pre-show "Only one name was supplied"; Max's "You heard your name and remained seated"; the itemized receipt |
| | B Wing Position | 0 | none (absence of receipt is the state) | Clean diagonal view, no lost content; nine seconds of tassel; Max's "The playbill will be thrilled" |
| **D2 crowd work** | A Send Pilsner up | 0 | `relic_claim_ticket` (no effect) | The 1998 license and the video-store card; "documented provenance" |
| | B Deploy camcorder | 0 | `chadwick_tape` | Chain-yank at Event 10; D3 payload table; unlocks D4A/D4B |
| | C Stay seated | 0 | none | Pilsner's genuinely correct VNS answer; "That was the correct amount of useless"; no tape exists |
| **D3 coping** | A Water | 0 | scene-local only | The four-second silence drill; no tape append |
| | B Three Encores | 30 SOVS (scripted deduction, no items, no HP, no Encore! buff; visible but disabled under 30 SOVS, no deduction, D3A/D3C stay free) | scene-local dulling | Alcohol dulls, never defeats; the "technical clarification" audio append |
| | C Biomechanical Reset | 0 | scene-local `reset_method` enum | One of three physical disasters; Barbara's coaster; one taped frame |
| **D4 footage (tape only)** | A Release | 0 | `footage_release_planned` | Critic's Eager state (rumor, not publication); predicted-metrics narration; afterparty ceiling append |
| | B Vault | 0 | `footage_vaulted` | No public distribution, ever; afterparty static-on-no-tape append |
| **D4 no tape** | C-1 Reenactment / C-2 Official Version | 0 | none | "Director's cut." vs. the pole; two different comedy forms |
| **D5 continuation** | Accept | 0 | evening chain serializes | Green Room → apartment → Catastrophe → D6 → morning; buttons at V5 |
| | Decline | 0 | none (no `afterparty_completed`) | Complete street/hostel ending; optional Jenna ICQ line; no buttons, no punishment |
| **D6 Bradley** | Go / Stay | 0 | evening chain selection | See the overnight outcome table below; never auto-substituted |

### Overnight outcome table (TROUSER SNAKE and morning)

| D5 | Xanax before D6 | D6 | TROUSER SNAKE | Morning |
|---|---|---|---|---|
| Decline | any available state | — | Alcohol may dull; never defeated by alcohol; expiry follows the status text (end of evening) | Complete hostel ending; **no buttons**; pill state, if set, still clears only at next in-game morning |
| Accept | no | go | **Defeated — performer route** | Pilsner prone on the couch; Chadwick sits on the peas; Bradley "Sacroiliac lockout." / "Executive branch." / "Shut up."; three buttons |
| Accept | no | stay | Not defeated by alcohol; status-text expiry | Pilsner/Chadwick soreness; Bradley "Paced myself."; three buttons |
| Accept | yes | go | **Defeated — pill; recurrence and performance blocked until next in-game morning** | Pilsner/Chadwick soreness; Bradley painless on a stool + purple sweatshirt; "That's new." / "Okay." is the whole account; three buttons |
| Accept | yes | stay | **Defeated — pill; same morning lock** | Pilsner/Chadwick soreness; Bradley painless, no sweatshirt; three buttons |

**Hard rules:** alcohol dulls only (q9: B); the pill never fails and never rolls; D5 and D6 are never auto-selected; the single Catastrophe override touches only Pilsner's toast, never intimacy; the morning reveal is unmistakable **to the bros** (garment bags, wigs, signed playbill, offstage selves), after which Pilsner immediately salvages rather than denying.

### The tape, by branch (exactly one D3 append + one afterparty append)

| D3 branch | Appended to the tape | Afterparty append |
|---|---|---|
| A Water | Nothing — three men drinking water with terrifying discipline | RELEASE: ceiling, re-sealed unreviewed · VAULT: static onto no tape · NO TAPE: nothing ejected |
| B Encores | Bradley's drunken "technical clarification" as audio over a belt-height lens | Same D4-conditional behavior |
| C Reset | One frame of the chosen disaster (`reset_method`) | Same D4-conditional behavior |

No branch produces usable inauguration footage. No branch shows an upload, a comment section, or a view counter tonight.

---

# APPENDIX B — FIVE OPERA DISTRICT ENEMIES

**All five names are unique across the game (repo-searched). All stats, drops and behaviors are PROPOSED.** `sinfonia_enemies.json` is empty; insertion order below is the proposal. Concept credits: Critic and Keeper — Gemini; Supernumerary and Bassoonist — Aion; Keg-Acolyte — GLM; consolidated and balance-verified by GLM; presentation review by Kimi; Gemini signed off on the Critic drop swap and the Keeper re-spec, Aion on the Supernumerary trigger table and the Bassoonist solo correction.

**Data contract (verified against shipped code):** eleven fields per enemy — `display_name`, `battle_intro`, `max_hp`, `offense`, `defense`, `speed`, `luck`, `xp_reward`, `gold_reward`, `item_drop`, `drop_chance`. Shipped `battle_manager.gd` **rolls** `drop_chance`; `grant_rewards()` skips `""`; reward display reads `DataRepo.get_item()` — **consumables.json only**, so every drop needs a consumables entry or the victory summary prints a raw ID. `data_repo.gd` currently hardcodes the Debaucheryville enemy path (Dependency 1).

**FULL-DESIGN-ONLY banner:** the shipped battle menu is exactly four buttons — Bash / Roast Line / Item / Run. The following do **not** exist in it and must not be staged against it: the fifth action **Wait**, **Break Pose**, **Step Outside the Line**, the Acolyte's patient route, the Supernumerary's ignore route, and the Applause Lockout's contextual disable. The four-button build ships these encounters with burst / grind / bribe routes only, and the log says nothing about missing jokes.

**Solo-build caveat:** every table below is computed against the shipped solo-Pilsner build — HP 45, offense 8, defense 6, luck 4, Bravado 12, Roast Line ×1.8 cost 4 — using the shipped formula `(offense×2 − defense) × multiplier ± 2, floor 1; crit = luck%`. They are **not** balanced for a future three-character party; all five sheets rebalance when party combat lands (Dependency 7). Shipped battle has **no Bravado regeneration**; the only restore in data is `absinthe_shot` (+8). Routes are alternatives, not a mandatory sequence — never stage multiple mandatory Roast Line checks in one evening.

## B1. THE AXED CRITIC — common / period-reference slot

- **ID:** `axed_critic` · **Location:** Opera House Plaza / alley beside The Standing Ovation (exterior).
- **Silhouette:** shabby tweed, ink-stained fingers, cracked bifocals on a chain, clutching a 2001 issue of *Sinfonia Arts Weekly* like a riot shield. Distinct from the Bassline's in-house Opera Critic: this one is unemployed, outside, and reviews **you**.
- **Premise:** a print journalist fired in the 2002 dot-com ad collapse, still roasting street life in late-90s entertainment-column register. To him the bros are a derivative boy-band reunion that deserves a career-ending pan.
- **Battle intro:** *An Axed Critic intercepts you with an unprompted retrospective!*
- **Kit:**
  1. **Pan the Production** — single-target takedown ("Derivative styling, unearned swagger, zero third-act development!"), ego damage, chance of **Embarrassed**.
  2. **2001 Retrospective** — AoE taunt at the party's cultural relevance ("You look like the clearance rack of an untelevised VMAs pre-show!"), **Existential Crisis** flavored as a defense-debuff window.
  3. **Ink-Stained Slander** — fountain-pen swipe, low damage, Grease Fingers-style accuracy-debuff flavor (indelible gall-nut ink).
  4. **The Eager Turn** — on battle start **only** if `sinfonia.ovation.footage_release_planned` is true. The party cannot cause it mid-fight (the flag is set in Act IV; the Critic roams the district). He opens by begging Chadwick for syndication rights to tape nobody has seen ("I heard rumors of unedited tape! Give me the exclusive!"), defense halved, party crit chance up. He is easier because he is desperate. **Rumor, not publication.**
  5. **Deadline Distress** — on `player_hp < 25%`: defense drop and a forfeited next action. The momentum of humiliation is a timer, and the log tells you so.
- **Counterplay:** a one-turn Setup window between retrospective callouts (he checks his Rolodex for a worse example of you) — burst it to interrupt a Pan; withstand a retrospective without acting and he loses his nerve. Turn-1 Roast Line on his posture takes 1.5× effect, once per fight ("Don't critique my posture, you illiterate fullback!").
- **Reward:** gold 6, XP 16, fixed drop **`condescending_review`** — "A laminated verdict: 'Two stars. One is for the cargo shorts.' It is about YOU. He will be reprinting it."

```json
"axed_critic": {
  "display_name": "Axed Critic",
  "battle_intro": "An Axed Critic intercepts you with an unprompted retrospective!",
  "max_hp": 42, "offense": 9, "defense": 4, "speed": 7, "luck": 3,
  "xp_reward": 16, "gold_reward": 6,
  "item_drop": "condescending_review", "drop_chance": 1.0
}
```

## B2. SUPERNUMERARY AMBITIEUX — status-manipulation slot

- **ID:** `supernumerary_ambitieux` · **Location:** stage-door alley / Bassline service corridor.
- **Silhouette:** mismatched Roman legionary armor — one plastic pauldron, one borrowed hoplite shoulder — oversized wooden pike held vertically, stage blood on his chin kept for continuity.
- **Premise:** an unpaid opera extra who treats spear-holding as Stanislavski-grade art. The bros are his enemies because they *noticed him*: an audience of three cargo-shorted Americans is the review he has waited his whole unpaid life for.
- **Battle intro:** *A Supernumerary Ambitieux assumes a ready position! He is already acting.*

**The trigger table — which action the player selects, never a timing roll:**

| Player action (vs. his state) | Result |
|---|---|
| Attack during **Build a Tableau** (ONE telegraphed prep turn: "he strikes an agonized Grecian pose") | **Corpsing ×2 damage.** Pose cancelled, he restarts. **Stage Fright is structurally impossible here** — stated in the move text |
| Explicit **Break Pose** against the completed pose (PROPOSED contextual action) | Removes the defensive stance. **No damage, no Stage Fright.** He deflates, pauldron slips, restarts next turn |
| Ordinary attack (Bash/Roast) against the completed pose | Damage against posed defense (base 5 → 9), **and** 35% **Stage Fright**: the attacker forfeits their next 2 actions ("You've been seen. God, you've been SEEN.") |
| **Wait** through three complete-pose turns (PROPOSED fifth action) | **Attention denial — he leaves.** *Note From the Director: "they weren't ready."* Zero risk, zero reward, the funniest outcome |

- **Party-combat note (deferred):** in a three-member party, damage across ALL members de-poses him — his art requires a single unbroken line of sight.
- **Reward:** **gold 0** (unpaid; the empty wallet IS the premise), XP 11, fixed drop **`crumpled_headshot`** — an 8x10 in full legionary kit, autographed to nobody, printed email containing "2007".

```json
"supernumerary_ambitieux": {
  "display_name": "Supernumerary Ambitieux",
  "battle_intro": "A Supernumerary Ambitieux assumes a ready position! He is already acting.",
  "max_hp": 26, "offense": 5, "defense": 5, "speed": 3, "luck": 3,
  "xp_reward": 11, "gold_reward": 0,
  "item_drop": "crumpled_headshot", "drop_chance": 1.0
}
```

## B3. SECOND CHAIR BASSOONIST — group / reinforcement slot

- **ID:** `second_chair_bassoonist` · **Location:** musicians' courtyard, the alley between the venue and the Bassline's stage door.
- **Silhouette:** wrinkled white-tie tuxedo, bow tie at half-mast, colossal wooden bassoon braced like an anti-tank weapon, cigarette behind one ear.
- **Premise:** twenty-two years of second chair, and now a laptop does his job and doesn't even have a chair. The bros are the century's current representatives, and one of them asked if the bassoon is "one of those big clarinet things."
- **Battle intro:** *A Second Chair Bassoonist takes issue with you! Also with the century!*
- **Kit:**
  1. **Cracked Reed** — built-in 25% miss chance on his attacks, +10% per taunt. Do not smooth this; the crack is the fight's rhythm section.
  2. **Low C** — two visible inhale turns, then an armor-piercing bottom C. Lands a quarter-tone sharp: self-debuff **Sharp** (offense −2 for 3 turns — he heard it). **The district's only two-turn telegraph.** Burst the inhale and the Low C never happens.
  3. **Union Break — ONE USE PER ENCOUNTER; fires on his second turn.** What arrives is **The Reed Section's Break**: a **Tympanist on Break** (half his HP; a thump with a 30% chance to hit whoever was conducting — at solo table that is *himself*; the log names the victim) and an **Overworked Oboist** (weaker; her one lecture — "real musicians don't crunch during the opera" — inflicts Embarrassed, usable once (full-design-only; on the four-button build it degrades to her zero-effect criticism), then only zero-effect breath-support criticism). The summons are permanently weaker than he is. Solidarity arrives on break.
  4. **Key-click** — whenever the party uses an item, a token free hit, telegraphed the first time ("He is watching your inventory. He has opinions."), 2-turn cooldown so item healing can't be punished into a loop.
- **Reward:** gold 14, XP 16, fixed drop **`spare_reed`** (proposed Embarrassed-cure; ships inert if the status system isn't ready). Tympanist is **dropless** (`item_drop: ""`, `drop_chance: 0.0` — safe by both the roll and the `""` skip). Oboist also drops `spare_reed`.

```json
"second_chair_bassoonist": {
  "display_name": "Second Chair Bassoonist",
  "battle_intro": "A Second Chair Bassoonist takes issue with you! Also with the century!",
  "max_hp": 34, "offense": 7, "defense": 3, "speed": 4, "luck": 4,
  "xp_reward": 16, "gold_reward": 14,
  "item_drop": "spare_reed", "drop_chance": 1.0
},
"tympanist_on_break": {
  "display_name": "Tympanist on Break",
  "battle_intro": "A Tympanist on Break arrives, still chewing!",
  "max_hp": 16, "offense": 4, "defense": 2, "speed": 3, "luck": 2,
  "xp_reward": 5, "gold_reward": 3,
  "item_drop": "", "drop_chance": 0.0
},
"overworked_oboist": {
  "display_name": "Overworked Oboist",
  "battle_intro": "An Overworked Oboist materializes, already exhausted by this!",
  "max_hp": 18, "offense": 3, "defense": 2, "speed": 5, "luck": 3,
  "xp_reward": 6, "gold_reward": 4,
  "item_drop": "spare_reed", "drop_chance": 1.0
}
```

## B4. KEEPER OF THE ROPE — rare / spatial-rule slot

- **ID:** `keeper_of_the_rope` · **Location:** venue foyer / VIP annex threshold.
- **Silhouette:** imposing, rigid bouncer in an ill-fitting tuxedo with a brass clip, standing with absolute territorial majesty behind a frayed four-foot velvet rope between two wobbly brass stanchions. Ten feet of clear walking space on either side.
- **Premise:** his entire identity rests on a decorative rope not connected to any wall — the venue's own CANON says its ropes are decorative, not exclusive.
- **Battle intro:** *The Keeper of the Rope bars an imaginary VIP boundary!*
- **Stat block (re-specced after the old 68/12/10 block proved mathematically unwinnable solo):** **HP 52 / offense 9 / defense 7 / speed 4 / luck 1.** Brute-forcing a decorative rope is the most expensive option in the district; every correct solution is free. The joke is load-bearing in the numbers.
- **Layer 1 — environmental bypass:** examine text — *"A majestic velvet rope guarding three square feet of polished linoleum. You could easily walk three paces to the left."* Walk around: he glares, adjusts his cuffs, combat never triggers. Restraint as literal counterplay.
- **Layer 2 — combat, two tiers:**
  1. **The written-rule tier:** **Redefine the Velvet** repositions the rope diagonally and declares zones off-limits (players caught inside lose physical attacks until they spend an action **Stepping Outside the Line** — PROPOSED). **Check the Clipboard** cancels an undeclared action ("You're not on the manifest."). **Stern Velvet Whip** — the rare slot hits like the costume implies; the knockback feeds Redefine the Velvet (you're shoved INTO the declared zone). **No charge turn** — he owns spatial rules, not timers.
  2. **The unwritten-rule tier — the Roast Line ladder, exactly two rungs:** Roast #1 → he answers with better policy ("Regulations state the boundary is conceptual!") and **forfeits his next action** re-pressing the rope's non-existent creases. Roast #2 → policy collapse; he abandons combat posture to measure floor tiles with a clipboard ("The floor plan is… aspirational.") — **the encounter ends as a win with full rewards.** Two sentences beat a man defending a boundary nobody signed. Bravado cost: 8 of Pilsner's 12.
- **Nonviolent resolution:** present Chadwick's `press_napkin` or Pilsner's expired license. He inspects the ink under a magnifying glass — *"Your accreditation is dangerously irregular, but the typography is confident"* — unhooks the brass latch with grand ceremony, and lets the party through. Full XP, full drop. The fictional credentials work because he cannot tell the difference between fiction and policy.
- **Reward:** gold 15, XP 35, fixed drop **`decorative_brass_stanchion_clip`** — "Regulation-grade. For a regulation that does not exist."
- **First-clear gate:** `sinfonia.ovation.rope_resolved` set on ANY first resolution (bypass, ladder, bribe, or KO). Afterwards he is a one-line NPC: *"The boundary is conceptual. Move along."* No repeat grant, no re-battle.

```json
"keeper_of_the_rope": {
  "display_name": "Keeper of the Rope",
  "battle_intro": "The Keeper of the Rope bars an imaginary VIP boundary!",
  "max_hp": 52, "offense": 9, "defense": 7, "speed": 4, "luck": 1,
  "xp_reward": 35, "gold_reward": 15,
  "item_drop": "decorative_brass_stanchion_clip", "drop_chance": 1.0
}
```

## B5. THE DRAMATISCH KEG-ACOLYTE — elite / mini-boss slot

- **ID:** `dramatisch_keg_acolyte` · **Location:** cellar service vault / alley loading bay.
- **Silhouette:** rubber cellar apron, welder's goggles pushed up, brass CO2 manifold worn like a bandolier, the thousand-yard serenity of a man who has found the answer, and the answer is head retention. **A parish of one** — no order, no faction.
- **Premise:** he is not hostile. He is EVANGELICAL. The bros asked for a beer without commenting on the head, and that is a pastoral emergency. The fight is his lecture. He is genuinely, technically right about everything and cannot imagine why that doesn't end the conversation.
- **Battle intro:** *A Dramatisch Keg-Acolyte demands you appreciate The Head!*
- **Stat block:** **HP 48 / offense 11 / defense 6 / speed 3 / luck 2.**
- **Kit:**
  1. **Siphon Spray** — pressurized jet, tier damage **8 → 14 → 22**, escalating one tier per turn, holding at Tier 3.
  2. **The Head Foam Meter** — the tier counter lives on the ACOLYTE and on PILSNER'S OWN STEIN; the sprite's pour visibly thickens; the caption reads *"appreciation presumed."*
  3. **The Lecture — available from ANY tier:** at Tier 3, **or after the party Waits twice consecutively**, he stops attacking and delivers the head-retention lecture in three escalating couplets (telegraph after the second Wait: *"The pressure gauge is near red. He draws breath for THE LECTURE."*). **Weather it — three further Waits, zero attacks — and he salutes the party's discerning palate and leaves mid-fight**, awarding his drop and the encounter's respect. **Two Waits to trigger + three to weather = five total.** A mini-boss you can lose to politely. Fleeing counts as a walkout: no drop, and *"He pronounces your palate underdeveloped to the empty alley."*
  4. **The Applause Lockout** (replaces the deleted Applause Forfeit, which paused nonexistent regeneration): when a **Roast Line lands**, the room erupts in applause *for the beer* — telegraph on the landing turn: *"The room roars its approval. Of the beer. He bows."* On the party's NEXT turn, **Roast Line is locked**: *"Nobody can hear you. They're still clapping."* **At most once per encounter; never touches Wait** — a party that never Roasts is never locked out.
- **Counterplay:** burst = T1 Roast (lockout telegraphs) → T2 locked, Bash → T3 Roast → T4 Roast; ~44 damage taken against 45 HP — survives by 1 HP, zero crits, four turns. Patient = 2 Waits + 3 lecture Waits for ~22 total damage and the best drop in the quest. Run always available at 50%. Three exits, no optimal one, the funniest one is free.
- **Reward:** gold 16, XP 40, fixed drop **`dramatisch_dunkel`** (12% cellar brew, heal_hp 40, *"Obliterates the faculty of regret."*) — the quest's best consumable, given for LISTENING.
- **First-clear gate:** `sinfonia.ovation.palate_respected` set on the FIRST resolution that awards benefits — lecture-weathering **or** a burst-route KO. Weathering → the cellar-door nod, *"He returns to his pour."* KO → he is back at his pour and pointedly does not acknowledge the party. Either way: one dunkel per save file, one route, once.

```json
"dramatisch_keg_acolyte": {
  "display_name": "Dramatisch Keg-Acolyte",
  "battle_intro": "A Dramatisch Keg-Acolyte demands you appreciate The Head!",
  "max_hp": 48, "offense": 11, "defense": 6, "speed": 3, "luck": 2,
  "xp_reward": 40, "gold_reward": 16,
  "item_drop": "dramatisch_dunkel", "drop_chance": 1.0
}
```

## B6. Solo survivability tables (deterministic; solo-Pilsner build only)

| # | Encounter | Enemy (HP/off/def) | Player route | Turns | Damage taken | Verdict |
|---|---|---|---|---|---|---|
| A | Axed Critic | 42/9/4 | 2× Roast Line | 2 | ~25 | Wins, no heal. Bash route: 4 turns, ~50 — needs 1 kebab |
| B | Bassoonist + Break adds | 34+16+18 HP | Roast T1 (taunt) → Bash T2 — the kill denies Union Break | 2 expected; ≤7 worst case | ~5 expected; ≤19 worst | Wins, no heal. If low rolls keep him alive at ~2 HP the break fires; the adds hit for 2 and 1, and the Tympanist mostly hits himself. Bash-only route: ≤7 turns, ~20, still no heal. Full verification: `drafts/glm_bassoonist_balance.md` |
| C | Supernumerary | 26/5/5 (posed def 9) | Prep-interrupt ×2, then Bash | 3 | ~12 | Wins, no heal. Stage Fright route: +~2 forfeited turns, ~24 |
| D | Keeper (re-spec) | 52/9/7 | Full Bravado: 3× Roast + 1 Bash | 4 | ~48 | Needs ≥1 kebab or dies by a hair — brute force is the expensive option |
| D′ | Keeper — correct routes | — | Walk around / 2× Roast ladder / credentials | 0–4 | 0–48 | Free, free, free. The design wants you here |
| E | Keg-Acolyte burst (with lockout) | 48/11/6 | Roast → locked Bash → Roast → Roast | 4 | ~44 | Survives by 1 HP, zero crits. The impatience tax |
| E′ | Keg-Acolyte patient | 48/11/6 | Wait ×2, lecture Wait ×3 | 5 | ~22 | Wins with the best drop. Below ~60% HP it's a Run call |
| F | Old Keeper block (dead) | 68/12/10 | any | 11+ | ~200 vs 45 HP | Mathematically unwinnable solo — why the re-spec happened |

**Bravado scarcity:** demand across the roster if every Roast route is taken — Critic 8 + Keeper ladder 8 + Acolyte burst 12 = 28 against 12 + absinthe. Every encounter therefore has at least one zero-Bravado exit. Ambient gold re-farming on respawn is a general Sinfonia economy-pass item, not this quest's blocker.

---

# APPENDIX C — PROPOSED CONTENT AND MECHANICS REGISTER

One current definition per item. Everything here is PROPOSED unless marked CANON. No game files are modified by this document.

## C1. Prices

| Item | Price | Status |
|---|---|---|
| Producer's Circle (D1A) | **36 SOVS** = 24 pours (3 × 8) + 12 acknowledgment, table 0 | Author-approved (2026-11-11). Grayed below 36, never hidden. If the price moves, Bradley's arithmetic and the receipt recompute together |
| D3B three Encores | **30 SOVS**, scripted deduction, no items, no `use_item`, no HP, no Encore! buff | Scene only. The CANON Encore (10 / +30 HP / staff ovation) is untouched for legitimate menu orders |
| Tony420 Flintstone Xanax | **50 MoonCum696969**, crypto only | **CANON** (q10: A). MoonCum spendable with Tony420 only; added to the coin pool (applied 2026-11-10: `shitcoin_master_pool.md` #29, $MCUM; exception and free sample in `icq_airdrops.md` §1.4) |
| Everything else in the quest | **0 SOVS** | Including the entire overnight |

**Affordability (honest statement):** new game starts at 20 gold; no guaranteed Sinfonia arrival balance is documented. 36 is arithmetically reachable from the roster's own fight purses (6 + 14 + 16 = 36, once each) but that is a plausibility case, **not a proven curve**, and the intended free solutions (Keeper bypass, Acolyte weathering) award XP/drop, not gold. A broke player misses exactly one vanity purchase and loses no show content. The quest never requires grinding or invented wealth.

## C2. Items

| ID | Display name | Class | Inspection / readers |
|---|---|---|---|
| `press_napkin` | PRESS napkin | Key item, no effect | "A house-stamped napkin officially accrediting the bearer as PRESS. Smells faintly of Curtain Call Copper. Legally: a napkin." Readers: D4A envelope beat; Keeper nonviolent resolution |
| `chadwick_tape` | Chadwick's tape | Key item | D4 menu condition; chain-yank; D3 payload table; afterparty append. D2B only |
| `receipt_producers_circle` | Producer's Circle receipt | consumables.json, `usable: false` souvenir | Max approach variant; the itemized receipt joke; D1 branch state |
| `relic_claim_ticket` | ONE (1) RELIC — CLAIM BY 2004 | consumables.json, `usable: false` souvenir | Reader: inventory inspect (junk-item rule). Inspect text: **"A coat-check stub for an entire human being. Nobody came back to claim him."** |
| `condescending_review` | Condescending Review | consumables.json, `usable: false` | Critic fixed drop. "A laminated verdict: 'Two stars. One is for the cargo shorts.' It is about YOU. He will be reprinting it." |
| `crumpled_headshot` | Crumpled Headshot | consumables.json, `usable: false` | Supernumerary fixed drop. "An 8x10 in full legionary kit, autographed to nobody. The printed email address contains the year 2007." |
| `spare_reed` | Spare Reed | consumables.json, `usable: false` (Embarrassed-cure effect PROPOSED; ships inert if the status system isn't ready) | Bassoonist + Oboist drop. "A reed for an instrument you have never played. Given with the contempt of a man parting with nothing." |
| `decorative_brass_stanchion_clip` | Decorative Brass Stanchion Clip | consumables.json, `usable: false` | Keeper fixed drop. "Regulation-grade. For a regulation that does not exist." |
| `dramatisch_dunkel` | Dramatisch Dunkel | consumables.json, **`usable: true`**, heal_hp 40, heal_bravado 0 | Keg-Acolyte fixed drop, first-clear gated. "The 12% cellar brew. Obliterates the faculty of regret. Restores 40 HP." |
| `flintstone_xanax` | **Flintstone Xanax** | consumables.json, **`usable: true`**, heal_hp 0, heal_bravado 0 — **consumption IS the trigger** | **"Grape. Shaped like a dinosaur."** Price 50 MoonCum696969. CANON effect: ends TROUSER SNAKE and prevents recurrence AND Bradley's sexual performance until the next in-game morning — reliable, no roll, save/load-safe. Readers: D6 variant; morning Bradley staging; status suppression. **Flintstone Fentanyl is a SEPARATE product with no assigned effect — do not merge** |
| `campaign_button_chelsea_morning` | **CHELSEA MORNING 4 DRAG PREZ** | Permanent equippable cosmetic accessory, zero stats, **never consumable**; fallback class permanent key item | "She won your vote hours ago." |
| `campaign_button_jenna_talia` | **JENNA TALIA 4 DRAG PREZ** | Same | "A platform you could injure yourself on." |
| `campaign_button_barbara_bushed` | **BARBARA BUSHED 4 DRAG PREZ** | Same | "Bipartisan support in low-light environments." |

**Button award contract (single source, single grant):** the three buttons appear physically once, at V5 on the bathroom counter beside the lipstick mirror, and are pinned on the bros by the performers in that beat. `campaign_buttons_awarded` fires once there, gated on reaching the morning continuation (`afterparty_completed`). There is no Green Room distribution, no second set, and no award on the decline path. Zero numerical, combat, reputation, sell-value or hidden effects. Any bro may equip one in a supported accessory slot; if the equipment UI is unavailable, the fallback is permanent key-item souvenirs with identical text — never consumables, never substitute stats. A visible two-pixel pin on a sprite is optional presentation, not an asset requirement.

**`usable: false` guard (Dependency 8):** shipped `use_item()` consumes what it accepts, so a zero-effect consumable would be destroyed by use. The one-line guard is required before joke drops become safe inventory. All five enemy drops land in the **shared, cross-world** `items/consumables.json` — implementation-time author sign-off (Dependency 9). No sell mechanic exists in the engine; any sell values are future-shop flavor with no current reader.

## C3. Quest state — 8 persistent boolean flags + serialized evening state

Eight namespaced boolean flags are proposed, alongside serialized evening-tier and choice state. Each requires a defined reader, default, save/load behavior, and expiry or first-clear rule. Boolean defaults are false unless otherwise specified. Register in `data/quests/flags.json` at implementation (PROPOSED).

| Flag | Set when | Read by / clear condition |
|---|---|---|
| `sinfonia.ovation.footage_release_planned` | D4 RELEASE | Axed Critic's Eager state (district-wide); next-day metrics narration (predictions only). Rumor, never publication (q8) |
| `sinfonia.ovation.footage_vaulted` | D4 VAULT | Mutual exclusion with release; prevents later "you promised us the tape" continuity errors. No other reader — by design |
| `sinfonia.ovation.rope_resolved` | ANY first Keeper resolution (bypass, ladder, bribe, KO) | Foyer trigger; Keeper becomes a one-line NPC. First-clear gate. Not cleared |
| `sinfonia.ovation.palate_respected` | First Acolyte lecture-weathering OR burst KO | Alley trigger; no repeat drop; nod vs. pointed non-acknowledgment. Not cleared |
| `sinfonia.ovation.flintstone_xanax_active` | Bradley consumes the pill | D6 staging; morning Bradley staging; recurrence/performance suppression. Survives save/load and scene changes; **cleared only by the next in-game morning transition** — never scene exit, dialogue end, hostel arrival, or the decline path |
| `sinfonia.ovation.afterparty_completed` | V3 cut to black | Morning scene availability; decline exclusion; next-day callbacks. Not cleared (one-job coupling across scene availability and callbacks is an accepted risk in favor of flag-count discipline) |
| `sinfonia.ovation.campaign_buttons_awarded` | V5 grant | Duplicate-award guard. Not cleared |
| `sinfonia.ovation.inauguration_held` | The single Catastrophe override | Fridge decree and pillowcase sash at **V4** (placed there so any save ≥ V3 still renders them); retained through the apartment morning; cleared by the morning scene's exit |
| Evening intoxication tier (enum, not boolean) | Authored quest beats | Serialized through the evening; no scene-end reset; absent = Buzzed default; clears at the next-morning transition |
| D6 choice and Xanax consumption history (selection state, not booleans) | D6 selection; consuming the pill | Serialized through the morning reveal; read by V4/V5 (and the hostel decline morning, if it calls back); clears after the morning scene exits |

- **`footage_posted` is NOT SET by this quest** (q8). Reserved for a future, properly established resolution interaction.
- **Tony420's free sample uses existing economy state only:** `airdrops_delivered` gains the one-shot string `standing_ovation_tony420_sample`; its presence is the duplicate-delivery guard and the only new reader. `bagholder_assets` receives exactly +50 MoonCum696969 in the same committed delivery. `has_inspected_first_crypto_trash` is a prerequisite read from the existing system, never set by this quest; `tony420_unlocked` is not read. No C2 item row is needed for the currency deposit; `flintstone_xanax` is unchanged.
- **Scene-local, no flags:** `reset_method` enum (press/wallsit/wedge, consumed at selection); D1 branch via receipt presence; D2 branch via tape presence; D3B dulling presentation; the sweatshirt and overlay toggles. Stale-state proof is structural: branch state is rebuilt from inventory + the persistent flags each time.

## C4. Statuses and the intoxication contract (ten-point review, condensed)

**TROUSER SNAKE — CANON text/numbers:** +10 Confidence / −25 Concentration / dialogue options temporarily compromised / persists for the remainder of the evening unless suppressed by substantial alcohol. The two deltas are quest-scoped presentation (the banner does the work); no new engine stat keys. **Compromised dialogue (DESIGN TARGET):** option replacement as staged in Act IV. **Alcohol DULLS it** (q9: B — banner dims, compromise lines lose volume; presentation only, no duration change) and never defeats it. **Two full defeat routes (CANON):** `flintstone_xanax`, and sleeping with one of the First Daughters cast — Chelsea Morning, Jenna Talia or Barbara Bushed; never Max Vex (author, 2026-11-10) — (offscreen, never shown, no new relationship canon). Nobody explains why the pill works.

**Intoxication tiers — CANON names:** Buzzed → Beer Goggles → Shitfaced → Catastrophe. **No numerical thresholds are defined or proposed anywhere.** All mechanics below are **DESIGN TARGETS / PROPOSED engineering** (Dependencies 11–16), not claims about the shipped build.

1. **Source:** the Circle's three pours (D1A); venue menu drinks through Act II (no counts, no ABV — none is documented and none is invented); D3B's three Encores if selected; the Green Room's unmarked bottle; the afterparty. **Not sources:** the Dramatisch Dunkel drop (an item, not an evening) and the Encore's +30 HP (commerce, not intoxication).
2. **Immediate effects:** Buzzed = boasting option text. Beer Goggles = the perception gloss and inflated identity judgment. Shitfaced = degraded options and the select/deliver gap. Catastrophe = exactly one scripted substitution. **No tier grants combat, Charm, HP, gold or Bravado advantage.**
3. **Escalation:** quest-authored beats, never a drink count — Buzzed at the first Act II heckle; Beer Goggles at the twins' place-switch; Shitfaced at Barbara's instrumental hold; Catastrophe only at the afterparty, immediately before the override. A player who declines every drink still rides the authored curve: **this quest dramatizes the bros' evening; it does not simulate the player's pours.** The player's intoxication-relevant decisions with teeth are D3B's 30 SOVS and the pill/performer outcomes. Tiers never descend mid-evening.
4. **Visible cues:** status-tray chip BUZZED / BEER GOGGLES / SHITFACED (Catastrophe is experienced as the override, not a chip to brace against); mutating dialogue options (primary legibility channel); idle sway at Shitfaced and the table-climb pose (PROPOSED asset work); **one** campaign-news perception device, escalating once at Act II and once at the afterparty, never a third time. The gloss **reuses the rendering approach** of the Debaucheryville Beer Goggles overlay and the Mid-Life Crisis visual language. **Explicit non-claim:** neither of those is a party-wide intoxication system in code; the combat debuff is an enemy-targeted effect and the Debaucheryville overlay is that quest's scripted presentation. No sound processing.
5. **Player control:** full ordinary control Buzzed through Shitfaced — degraded *content*, never degraded *input*. **One bounded Catastrophe override:** the player selects `[Let somebody else toast.]`; the interface substitutes it with **PILSNER IS MAKING AN EXECUTIVE DECISION. / Selected automatically: "Assume the presidency."**; the short ceremony plays; control returns immediately. Deterministic, single occurrence, no roll, no movement loss, no intimacy content. **Never overridden:** D5, D6, the fixed Max runway (zero-menu by contract, not by intoxication). **No softlock:** the override fires inside a linear beat; a save/load that precedes it does not consume it.
6. **Duration and recovery:** evening tier state persists across scene transitions and save/load and clears **only** at the next in-game morning transition (V3 → V4). Ending a dialogue scene never clears it. `flintstone_xanax_active` clears per its own key at the same transition. The active intoxication tier and Flintstone Xanax effect clear at the next in-game morning transition. Morning-only branch history remains readable until the morning scene concludes; it does not extend the drug effect. Nothing intoxication-related crosses into the next day except consequences.
7. **Comedic consequence:** volume mistaken for charisma (Buzzed); an advertised drag revue mistaken for a presidential-family hookup (Beer Goggles); the player watching Bradley fail to say "water" (Shitfaced); a government founded on an open tab, with the fridge decree surviving as physical evidence (Catastrophe).
8. **Status interactions:** Mid-Life Crisis Beer Goggles shares a name and visual language only — no code linkage, and its −Accuracy/+Friendly Fire never fires during the revue (no combat occurs). Embarrassed/Hungover untouched; **no `presidential_soreness` status and no morning HUNGOVER chip** — morning consequences are animation, posture, props and dialogue. No tier grants or drains Bravado; the Keg-Acolyte's Applause Lockout is encounter-local and unrelated. D3B's dimmed banner is the dulling at its strongest local expression, not a separate flag.
9. **Engineering:** Dependencies 11–16 (Appendix D). Explicitly **not** required: an alcohol meter, drink-count tracking, ABV data, a party-wide buff system, movement impairment, camera effects, or new status entries. One enum, one banner, one clear point, staged content.
10. **Approval:** tier names, the escalation concept, the bounded override, the dull/defeat hierarchy, the Xanax effect and the MoonCum price are CANON. Points 2–6 and 9 are PROPOSED production candidate mechanics pending editorial review; Dependencies 11–16 are PROPOSED engineering. If the author later wants a metered global system, that is a separate decision.

**Accessibility:** no camera wobble, screen distortion or control-lag motion effect is required. Legibility is carried by text, chip and pose. If motion is added later, a static-icon / reduced-motion fallback carries the same information and stays mandatory. No movement-impairment sequence exists in this quest.

## C5. NPC register

| NPC | ID | Status / profile |
|---|---|---|
| Max Vex | `sinfonia_npc_max_vex_01` | **CANON** profile (`design/worlds/sinfonia/npcs/The_Standing_Ovation/max_vex.md`). They/them. Magnetic, nonbinary, cutting, professionally excellent. Own evening, own colleagues; never Bradley's counselor, prize or moral authority; never attends the afterparty. Their Black-Tie Backroom poker appearance is independent canon and untouched |
| Herr Dramatisch | venue NPC (CANON venue doc) | Theatrical brewmaster; the PRESS napkin and the Producer's Circle are the only transactions, and he stops repeating surcharges |
| Chelsea Morning | `sinfonia_npc_chelsea_morning_01` | PROPOSED profile (`drafts/gemini_npc_profiles.md`). The Weaponized Debutante: precision, books, tap heels, aristocratic condescension. Secondary appearance: the apartment |
| Jenna Talia | `sinfonia_npc_jenna_talia_01` | PROPOSED profile (same file). Crowd-work terror: acrobatics, card case, brutal reflexes, the evening's hostess |
| Barbara Bushed | `sinfonia_npc_barbara_bushed_01` | PROPOSED profile (same file). Deadpan anchor: olives, martinis, economy of gesture. Owns the Bradley thread |
| Tony420 | `debaucheryville_npc_tony420_01` (author, 2026-11-11) | **PRE-EXISTING project character**; profile `design/worlds/debaucheryville/npcs/Cyberspace_Kavarna/npc_tony420.md`. Lowercase by default (shouted words and full stops allowed), chronically online (3–6 AM), competent scammer, vintage "Uh-oh!". ICQ avatar: pixelated avi in Oakleys indoors. Crypto only, across every in-game shitcoin at its own SOVS rate (author, 2026-11-11); MoonCum696969 spends with him alone. Never seen in person: in-person beats are a goon holding a tablet with his blurred, voice-changed video. His Cyberspace Kavarna terminal rental (Dmitri) is restaged under the goon-and-tablet ruling; existing sprite slot "Tony420 Fake Crypto". Relationships: Hamstradamus, richfield69, Döner Council (Sauce Apostates) group-chat admin, the MemeLord.exe trade, Chadwick's GO LIVE chat. Does not replace his other appearances. Venue-door hotspot is PROPOSED dressing; the Opera House Grand Lobby hotspot is the documented fallback |
| Younger Patron, Server, Venue Runner | unnamed ambient | Scene-level only; no new named NPCs created |
| Supernumerary, Bassoonist, Tympanist, Oboist, Keeper, Keg-Acolyte | enemy IDs, Appendix B | Combat enemies; no NPC profile templates required; names registered unique |

**Performer profile note:** all three profiles use quest ID `sinfonia_sidequest_standing_ovation_01` and list `sinfonia_firstdaughters_apartment_01` under Secondary Appearances. Barbara's "Hold the cork." is cut; "Hold this. Looks busier." stands alone.

---

# APPENDIX D — IMPLEMENTATION, CHRONOLOGY, OPEN DECISIONS

## D1. Engine dependencies (all PROPOSED engineering)

| # | Dependency | Blocks | Priority |
|---|---|---|---|
| 1 | Generalize `data_repo.gd` enemy/item path loading; present-but-empty world tables must be legal (the `key_items.json` precedent) | All five enemies summonable | High |
| 2 | `the_encore` real item spec in the venue's item lane — **menu purchases only, NOT D3B** | Legitimate Encore ordering through the item system | Medium |
| 4 | Present-tense stage version of the post-status dialogue set | Post-status scene | Medium |
| 5 | Scene-local dulling presentation state (no register entry) | D3B staging | Medium |
| 6 | Lint task for the verbatim fixed runway | Speaker-swap regressions | Low |
| 7 | Party combat scaling (project-wide) | Rebalancing all five sheets post-party | Deferred |
| 8 | `usable: false` honored by `use_item` (one line) | Joke drops + receipts as safe inventory | Medium |
| 9 | Consumables entries for the five drops in the shared cross-world `items/consumables.json` — author sign-off at implementation | Drop display | Medium |
| 10 | Fifth battle action **Wait** + contextual actions (Break Pose, Step Outside the Line) | Ignore/lecture/Break Pose routes in full design | Medium |
| 11 | Quest-scoped evening-tier enum, serialized with the evening chain (absent = Buzzed; `SAVE_VERSION 2`) | The whole tier contract | Medium |
| 12 | Tier-conditional dialogue option substitution (generalizes the shipped replacement capability) | Tier legibility | Medium |
| 13 | The one-shot auto-select banner ("PILSNER IS MAKING AN EXECUTIVE DECISION.") | The single Catastrophe override | Medium |
| 14 | Overlay/gloss control hooks (per-gloss scripted presentation reusing the Debaucheryville rendering approach) | The campaign-news device | Medium |
| 15 | The morning transition as the single clear point (tier state; `flintstone_xanax_active` per its key) | Save/load and expiry correctness | Medium |
| 16 | Sprite sway/climb poses + static-icon accessibility fallback | Presentation only; text/chip legibility must work with motion disabled | Low |

**Verified shipped facts relied on (not claims of new capability):** new game gold = 20; shipped party is Pilsner alone (HP 45 / off 8 / def 6 / luck 4 / Bravado 12, Roast Line ×1.8 cost 4); battle menu Bash / Roast Line / Item / Run with Run at 50%; `battle_manager.gd` rolls `drop_chance`; `grant_rewards()` skips `""` and pays party[0]; `DataRepo.get_item()` reads consumables only; `use_item()` heals party[0] and consumes what it accepts; no Bravado regeneration in battle; `absinthe_shot` (+8) is the only Bravado restore in data; flags are plain booleans on `SAVE_VERSION 2`; enemies respawn on scene re-entry (hence the first-clear gates); `sinfonia_enemies.json` is empty.

## D2. Evening clock (production staging, not a player-facing timer)

Venue hours 16:00–01:00 and last pour 00:45 are CANON and hold. No scene auto-advances while the player is reading, shopping or using ICQ.

| Time | Event | Place |
|---|---|---|
| 22:00 | Arrival; D1; PRESS napkin / title generator | Exterior and foyer |
| 22:20–23:45 | Revue; D2; Buzzed → Beer Goggles → Shitfaced heckling during the numbers | Auditorium |
| 23:45–23:55 | Curtain call | Auditorium |
| 23:55–00:05 | Fixed Max encounter, events 3–11, zero menus; PHILLIP aftermath; TROUSER SNAKE | Bros' table |
| 00:05–00:25 | D3 coping; optional ICQ/Xanax window (reachable after any D3 outcome) | Orchestra Pit / foyer or Opera House Grand Lobby hotspot |
| 00:25–00:35 | D4 Release/Vault or the two no-tape records | **Marquee / red-carpet threshold, before any walk home** |
| 00:35 | Jenna's backstage invitation and **D5** | Adjacent stage door; nobody has departed |
| 00:35–00:45 | D5 accept: Green Room toast ("Last pour.") and the invitation upstairs | Green Room |
| By 00:55 | Party and performers clear the venue; decline players already have the complete street ending | Exterior |
| After 01:00 | Afterparty; one Catastrophe override; D6; hard cut to black | Unnamed apartment (provisional ID) |
| Next in-game morning | Reveal, mirror, buttons, physical comedy, exit | Same apartment; hostel on decline |

**Transition contract:** D4 plays at the threshold. D5 happens before departure. Accepting goes directly through the stage door; the street exchange is the **decline ending only**. No re-entry, no second ending after either D4 version, no Max callback.

## D3. Outstanding author decisions (none silently resolved)

1. **SETTLED (author, 2026-11-10): Barbara is locked as Bradley's D6 partner.** She is always the one who invites him. There is no Jenna variant.
2. **SETTLED (author, via the desk, 2026-11-10): "Tony420 airdrops exactly 50 MoonCum as a 'free sample' right before pitching the pill."** §11 delivers exactly +50 MoonCum696969 immediately before his existing pitch, once per save, on every path that meets the existing wallet/contact access conditions. The pill route no longer depends on AD-04 or random airdrop luck; an existing AD-04 balance does not change the sample size. The hidden-tab and contact requirements are read, never granted or bypassed. The performer and decline routes remain complete regardless, and the pill is never a progression gate. The matching canon rule is already in `design/economy/icq_airdrops.md` §1.4.
3. **SETTLED (author, 2026-11-11): Producer's Circle is 36 SOVS.**
4. **SETTLED (author, 2026-11-10): Max Vex never sleeps with the bros.** "Max Vex only flirts and keeps up their whitty banter. They never sleep with the bros." The performer cure is the First Daughters cast only; Max never attends the afterparty.
5. **SETTLED (author, 2026-11-11): the camcorder title generator allows seven characters** (hence CHADWIK).
6. **SETTLED (author, 2026-11-11): Tony420 is `debaucheryville_npc_tony420_01`**, profile at `design/worlds/debaucheryville/npcs/Cyberspace_Kavarna/npc_tony420.md` (NPC template). Author rulings: Tony420 is the person (not one of several masks); he trades crypto only, across the full range of in-game shitcoins, each with its own SOVS exchange rate; he is never seen in person, and when he "appears", a goon holds up a tablet playing a heavily blurred, voice-changed video of him; lowercase is his default but shouted words and full stops are allowed; the Elon Musk note is dead; Flintstone Fentanyl is his only Flintstone product. The venue-door decal stays PROPOSED dressing.
7. **DONE (author-approved, 2026-11-10):** the MoonCum696969 pool entry (#29, $MCUM) is now in `design/economy/shitcoin_master_pool.md` (pool count 28 → 29, rotating roster 27 → 28). The Tony420-only spendability exception and the 50-MoonCum free sample are in `design/economy/icq_airdrops.md` §1.4.
8. **SETTLED (author, 2026-11-11): `relic_claim_ticket` stays.** Junk-item rule: small items that look like junk reward the player for inspecting them with short, really funny microcopy. Inspect text (Gemini, author's pick): "A coat-check stub for an entire human being. Nobody came back to claim him."
9. **SETTLED (author, 2026-11-11): D2C uses the short election answer.** The expanded alternative was cut.

## D4. Rerun audit vs. *Nothing Is Getting Through* (CANON comparison)

Shared: a drunken party, distorted perception, a cut to black, a morning reveal, physical consequences, and the Beer Goggles rendering approach. **Different mechanism:** that quest's misunderstanding is a woman's age; this quest's is **political celebrity identity**, with three performers exploiting an increasingly ridiculous presidential fantasy. This quest uses no three-POV montage, no identical-asset repetition, no mystery souvenir, no cheek-pat, no sleeping-bag tableau and no recreated discovery shot. Its signature devices are the campaign-news gloss (once established, once escalated), the misplaced inauguration, the lipstick signature, and campaign merchandise the bros **wear voluntarily** — the first quest's aftermath follows the bros; this one's can be equipped.

---

# APPENDIX E — POST-CREDITS, ACHIEVEMENT, VALIDATION

## 🎬 POST-CREDITS SCENE REWARD (PROPOSED)

**Scene title:** "The Transfer of Power"
**Unlock condition:** complete the overnight continuation (accept path). **Release branch only.** On VAULT, the unmarked envelope is absent and the tape stays in the sock; on NO TAPE, this scene does not unlock.
**Duration:** ~20 seconds.

**SETTING:** the bros' home base, weeks later. A framed revue playbill on the wall. On the desk, a camcorder and an unmarked envelope.

**SCENE:**
```
Chadwick, to camera, holding up the envelope:

CHADWICK: Friday. It's Friday somewhere.

Pilsner enters wearing the CHELSEA MORNING 4 DRAG PREZ button
on a clean surf shirt. He has ironed around it.

PILSNER: Not the lapel. The lapel is for state occasions.

Bradley, off-screen—wearing the purple INTRAMURAL ULTIMATE — 2002
sweatshirt if he received it, otherwise his usual basketball jersey:

BRADLEY: You wore it to a lease signing.

PILSNER: Executive session.

Chadwick slides the tape into the camcorder. The title card loads:
CHADWIK. He nods at it like a man reviewing a legacy.

CHADWICK: Enigma held up.
```

**THE PUNCHLINE:** the tape is finally watched by somebody. It is the ceiling.

**PLAYER REWARD:** scene added to the Memories gallery. No stats, no items, no currency.

## 🏆 COMPLETION ACHIEVEMENT (PROPOSED)

- **Achievement Name:** "Adjacent to Power"
- **Public Description:** "Attend The First Daughters and survive the morning after."
- **Hidden Description:** "You slept adjacent to American political royalty. The cast was the better time. Two stars. One is for the cargo shorts."
- **Unlock Condition:** reach the V6 exit on the accept path. A separate, non-hidden completion credit for the decline path: **"Historic Restraint"** — "You could have. That's the thing people don't understand."

## 💬 KEY DELUSIONAL LINES (voice reference, already in scene)

- **Lord Pilsner:** "Adjacent. We have slept adjacent to American political royalty."
- **Chadwick:** "Distribution is a process. Premières need anticipation. I'm dropping it Friday."
- **Bradley:** "The blood has to choose! It's hydraulics!"

## ✅ VALIDATION CHECKLIST

| Requirement | Status |
|---|---|
| Bros are NEVER self-aware or scam-aware | ✅ Pilsner salvages instead of learning; Chadwick never checks the tape; Bradley rationalizes to the end |
| Players laugh AT bros, not WITH them | ✅ NPCs wield the scalpel; the bros walk into it |
| Scams are obvious to players and avoidable | ✅ The Circle is itemized and declinable; D3B visibly fixes nothing; the ICQ price is shown before payment; the only forced outcome is one short, telegraphed Catastrophe |
| Bros remain confident — never afraid, never disgusted | ✅ They pursue the show, the drinks, the pill and the afterparty enthusiastically |
| City-specific cultural satire | ✅ Opera-district performance culture, brewery ceremony, critic culture |
| NO narrator, no moral framing, nothing that explains the joke | ✅ No narrator anywhere; design commentary is confined to appendices; the reveal is visual; the last line is Chadwick's "That's a better title." |
| Crypto content conforms to the economy system | ✅ 50 MoonCum696969 at Tony420 only (author exception); pool entry applied (#29, $MCUM, 2026-11-10); no invented coins |
| All prices and rewards in SOVS | ✅ Except the single author-ruled ICQ crypto transaction; no € glyph, no dollars, no koruna anywhere |
| Seedy nightlife underbelly shown in full | ✅ Backstage, unmarked bottles, ICQ dealing, an afterparty with consequences — no nudity, sex offscreen |
| Y2K/era-appropriate cringe | ✅ Camcorder titling, MySpace, VNS, Dogme 95, Kubrick, pagers, expired licenses, ICQ |
| Quest is optional; never gates main progression | ✅ |
| Quest flags registered in `data/quests/flags.json` | ⬜ Implementation step — 8 boolean flags plus serialized evening state, listed in Appendix C3 (PROPOSED) |
| All names unique across the game | ✅ Enemy, item, NPC and location IDs repo-searched; no collisions found |
| Post-credits scene delivers payoff | ✅ PROPOSED, Appendix E |
| Screenshot-worthy moments | ✅ The playbill at belt level; CHADWIK on a title card; the PRESIDENT pillowcase sash; the lipstick mirror; three buttons in the hall light; the Keg-Acolyte's thickening pour |
| The fixed 11 required events appear, verbatim where required | ✅ Act II (1–2), Act III (3–11), including "Oh." / "What?" / "Nothing." / "What?" / "Apparently somebody here is more progressive than he thought." and "…what did you say your name was again?" / "Chadwick." / "Right." / "You know my name." / "Do I?" — Max asks, Chadwick answers |
| Three genuine decision points; two change state; one avoids expense | ✅ Six decision points; D1B/D2C/D3A/D3C/D4C/D5-decline are complete free outcomes; the largest escalation costs 0 SOVS |
| Not every joke costs SOVS; not every NPC is a scammer; not every interaction humiliates | ✅ The venue is legitimate and excellent; Pilsner's trivia answer is genuinely correct; the performers choose their own evening |
| No mascots, no fourth party member, no named-hippo substitute | ✅ |
| No real place names in player-facing text | ✅ Locked historical references only ("Florida's still counting", election-night broadcast detail) |
| No combat during the revue; no fighting the performers | ✅ All five enemies are ambient district encounters |
| No unapproved mechanics presented as shipped | ✅ DESIGN TARGET labels throughout; Dependencies 1–16 listed; full-design-only combat routes bannered |
| Open author decisions visible | ✅ Appendix D3 |

## 📝 DEVELOPMENT NOTES

- **Art:** revue stage variants for the three performers and the finale; Max's stage sprite per the CANON profile; the apartment's three wig-on-bottle props, labeled garment bags, lipstick mirror, fridge decree (eyeliner) and pillowcase sash; the three campaign-button icons; the five enemy silhouettes; optional two-pixel equipped pins. The apartment is one small reusable interior — sitting room, kitchen, bathroom — not a new attraction.
- **Audio:** live-vocal revue numbers (harpsichord into electronic beat; the twins' duet; Barbara's ballad; the close-harmony finale); the ICQ "Uh-oh!"; one working laptop speaker, left channel only, Jenna supplying the right; **no montage score sting at the cut to black**; no slurred-voice processing.
- **Testing priorities:** fixed-runway speaker fidelity (lint, Dependency 6); the single Catastrophe firing exactly once and surviving save/load before it; `flintstone_xanax_active` expiry on both the accept and decline paths and across scene transitions; the single button grant (no duplicates, none on decline); first-clear gates on both special encounters; solo-build survivability on the four-button build; tier legibility with all motion disabled; no path that forces a purchase or an intimate choice.
- **Integration provenance:** spine `drafts/kimi_quest_spine.md`; overnight break `drafts/kimi_overnight_break.md`; Act V `drafts/kimi_act5_draft.md` with the room's §14/§15 review fixes applied (rib injury cut and its V3 reference removed; gluteal morning staging restored; design metatext removed from scene bodies; the decree's text revealed only at V4 with the eyeliner detail kept; "Executive clemency. Get out." / "A dignified transfer of power."; the Barbara button microcopy; the measuring cup kept); Chadwick arc `drafts/aion_chadwick_arc.md`; continuity register `drafts/aion_continuity_implementation.md`; mechanics `drafts/glm_mechanics_state.md`; enemies `drafts/glm_enemies_full.md`; intoxication spec `drafts/glm_intoxication_spec.md`; punch-ups `drafts/gemini_satire_punchups.md`; NPC profiles `drafts/gemini_npc_profiles.md`; Tony420 consolidation `drafts/kimi_tony420_profile.md`.
- **Comedy-density audit performed on integration:** no line after a punchline restates it; no character diagnoses another; no stage direction explains why something is funny; the morning reveal has no prose lecture in front of it; the performers' longest speeches are stagecraft, not satire delivery; the bros never notice the gap. Cut on this pass: the rib injury and its callback, "They are plainly not a political family.", the in-scene design notes, "Caretaker administration", the pill's player-facing imperative, the duplicated decree text at V2, and the "Body doubles" denial.

*End of production candidate. The author and the acting editor decide what becomes canon.*
