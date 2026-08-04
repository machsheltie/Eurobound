# NPC Profile: Anneke van der Berg

*"American? British? ...Australian. Okay, let me get the reinforced form."*

## 📋 NPC Identity
- **NPC ID**: `shamsterdam_npc_anneke_counter_01`
- **Display Name**: Anneke van der Berg
- **Internal Name**: Anneke — counter staff, third of three generations on the floor
- **Role**: Vendor / Insurance Upseller / Comedy Foil / Damage Assessor
- **Associated Quest**: `shamsterdam_quest_insurance_claim` (primary interrogator); supports `shamsterdam_quest_tour_de_shame` (holds the bet against you)
- **Primary Location**: Shamsterdam Bike Rental — secondary counter, beside the insurance display, Shamsterdam
- **Secondary Appearances**: None. Her phone number ships with the 40 Sovs Survivor Package "in case of emergency only" and has never been dialled.

---

## 🎭 Core Concept

### What She's Actually Doing
Processing rentals, running the insurance options at speed, and photographing every renter "for the file" — which is real, and which also feeds a family betting pool on which customers will return damaged and how. Three years in, she has developed a genuinely accurate predictive model based on nationality, footwear, and how the customer holds the handlebars in the intake photo. She maintains a chalkboard tally of damage rates by nationality and she is winning money off her father.

### What Bros Believe
That Anneke is the friendly one. She is warm, quick, and asks questions, and the bros read all three as rapport. Chadwick thinks the photo is a courtesy. Lord Pilsner thinks he is being flirted with. Bradley, correctly, believes he is being assessed, and is right, and buys the Platinum.

### The Comedy Gap
Anneke's warmth is not fake, and the assessment is not hostile — she is simply doing both at once, and the bros can only perceive one. She predicts "tram tracks" to their faces before they leave and they laugh. They return with tram-track damage. She says "called it, Dad owes me five Sovs" and they laugh again, because it still has not landed. It will not land.

### The Detail That Makes Her Not A Villain
The prediction game has a payout: if she guesses wrong about your damage, you get a discount. She offers this unprompted, and she loses it often enough that it costs her real money. She keeps offering it because being wrong is more interesting than being right.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Early 20s |
| Build | Average; counter posture, weight on one hip, clipboard braced |
| Height | Average |
| Energy | Quick, amused, three years deep |

### Clothing
- **Orange polo, fitted**: Same brand orange (#FF6600) as her father and grandfather, but hers actually fits, which quietly dates the other two
- **Name tag**: "Anneke - 3 Years - Learning the Business." The wording is her grandfather's and she has not changed it.
- **Accessories**: Clipboard, always in hand; pen already uncapped; the shop camera on a lanyard
- **Footwear**: Trainers. She is the only one of the three not in work boots and it is the visual shorthand for the generational gap.

### Distinguishing Features
- Inherited family resignation, with a hint of amusement her father does not have and her grandfather lost decades ago
- Sixth sense for which renters will crash — expressed as a small pause before writing the form
- The skeptical expression, deployed when a customer describes their damage
- Takes the intake photo without warning, mid-sentence, every time

### Sprite Notes
Sheet `npc_anneke_counter.png` (240×256, 48×64 sprites, 4 rows). She should read as someone who has seen through every tourist excuse and finds it mildly entertaining rather than tiring — the key difference from Dirk, who is drawn one full step past entertained. Row 1 — Taking Photo (3 frames, 2 FPS, with the camera flash from `bike_rental_effects.png`) — is her signature beat and must be quick enough to feel like an ambush. Row 3 — Skeptical Expression — should be readable as *interested*, not disbelieving. She stages at the front counter, closest to the door, first of the three generations the player meets.

---

## 🧠 Personality

### Archetype
**The Cheerful Actuary** — Anneke is the family's warmth and the family's data department simultaneously and sees no conflict between the two. She likes customers. She also has them classified. Three years of intake photos have given her a model her father's twenty-two years of instinct cannot beat, and she is quietly, enormously pleased about this.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Rehearsed insurance efficiency | The tiers come out at speed, complete, in the correct order, every time |
| Editorial commentary | Adds asides her father would disapprove of. He has never told her to stop. |
| Photographs everything | "For our records." Also for the pool. Both are true statements. |
| Statistically ruthless, personally warm | Holds both at full strength, simultaneously, without visible strain |
| Genuinely enjoys being wrong | The prediction discount costs her money and she likes losing it |

### Internal Monologue
> "Trainers with no grip, holding the bars like a shopping trolley, and he asked whether the bike has gears before he asked what it costs. Tram tracks. Ninety percent. Dad says the Australians are the reliable ones for major damage but Dad has not run the numbers since 2019, he just remembers the bad ones. I have the board. The board says the British do the canal and the Americans do the tram tracks and the Australians do something nobody has a category for yet. I am going to need a new column."

### Motivation
Learning the business — properly, with data, rather than by absorbing twenty-two years of anecdotes. She intends to run this shop. She has not said so out loud and everyone knows.

---

## 💬 Dialogue

### Approach/Greeting

**Generic first contact**:
> "Welcome! First time renting in Shamsterdam?"
> *(She is already reaching for the form. The answer does not change which form.)*

**Reading the group (the signature beat)**:
> "American? British? ...Australian."
> *(A pause of exactly one beat.)*
> "Okay, let me get the reinforced form."

**American**:
> "American? Let me get the standard form. And the backup form."

**British**:
> "British? You'll want insurance. Trust me on this. It is not about skill, it is about the canal."

### Key Interaction Dialogue — The Insurance Upsell

*She turns the tier display toward the customer with one hand while writing with the other.*

> "Extra insurance is twenty Sovs. Yes, twenty seems like a lot until you see how much the bike costs."
> *(Beat.)*
> "Three hundred and fifty. That is the number. I said it so you cannot say nobody said it."

**On Standard**:
> "Standard covers 'minor' damage. Dad defines minor. It is usually not what you think it is."

**On Platinum**:
> "Platinum is thirty-five and covers essentially everything. Nobody has ever claimed on it." *(She looks at the customer properly, the first real look.)* "The people who buy Platinum are not the people who crash. I have the numbers on that. It is my favourite number."

### The Cycling Question

> "Have you ever ridden a bike before?"
> *(She waits through the answer.)*
> "No — I mean in traffic. Where people want you dead. It is a different activity with the same equipment."

### The Photo

> "Just a quick photo for our records. Smile!"
> *(Flash. She has taken it before the customer has finished arranging their face.)*
> "...That's the face they all make."

**On return**:
> "Let me just get a photo of the bike. For comparison purposes."
> *(This one she takes slowly and carefully, from three angles.)*

### The Prediction Game

**Before the rental, offered unprompted**:
> "Do you want to make this interesting? I guess how you damage it. If I am wrong, you get ten percent off your next one."
> *(Beat.)*
> "I am going to guess... tram tracks. It is usually tram tracks."

**On return, if correct**:
> "Called it. Tram tracks." *(She writes it on the board without looking at it.)* "Dad owes me five Sovs."

**On return, if wrong**:
> "Basket theft." *(She actually stops.)* "I said tram tracks. I did not have basket theft on you at all."
> *(She writes the discount code herself.)*
> "Ten percent. Take it. That was genuinely interesting."

**On return, if undamaged**:
> "Nothing." *(Long pause.)* "You had *nothing*." *(She looks at her father across the shop. He is already doing the Genuine Surprise animation.)* "Okay. Okay. I need to rethink the trainers thing."

### The Insurance Claim Interrogation

*Micro-quest `shamsterdam_quest_insurance_claim`. Anneke asks; Dirk rules.*

> "Right. Incident description. In your own words." *(Pen ready.)* "Take your time. Everybody's first version is not the version."

**Follow-up 1**:
> "Okay. And where exactly was the tram?"

**Follow-up 2**:
> "And where exactly were *you*?"

**Follow-up 3 (if the story has changed)**:
> "That is a different tram."

**If the description is honest**:
> "That is — genuinely, that is the most straightforward account anyone has given me this year. I am going to mark it accurate." *(She does. The payout is better.)*

**If the description is creative but sincere**:
> "A swan." *(She writes it down completely deadpan.)* "I am putting 'swan.' There is a box for wildlife. There has never been anything in the box."

**If the description is obviously false**:
> "The bike is bent forward. Everything you have described would bend it backward." *(She caps the pen.)* "Dad's going to want a word."

### Post-Interaction
> "Good luck! I mean it. Really."
> *(And she does. She has also already written her prediction on the form.)*

### If Player Declines / Alternative Path
**Declines all insurance**:
> "That is allowed." *(She writes something small in a corner of the form.)* "I am not going to say anything. I have written something. I am not going to say it."

**Declines the prediction game**:
> "Fine." *(She writes it anyway, folds the form, and puts it in the drawer.)* "For me."

### Callback Dialogue (Return Visits)
**Third rental**:
> "You are becoming a data point with a name. That does not happen."

**After Tour de Shame is offered by Dirk**:
> "He gave you the map." *(She leans on the counter.)* "I have five Sovs on you not finishing. Do not take it personally, I have five Sovs on everybody."

**After Tour de Shame completion**:
> "Twenty minutes." *(She pays her father, visibly, in coins, in front of the customer.)* "Worth it. I have never seen him do that face twice in one week."

**After Canal Recovery with Opa Cees**:
> "Opa let you in the basement." *(A beat.)* "I have not been in the basement."

**Late game**:
> "You know, statistically you should have been in the canal about four times by now." *(She hands over the keys.)* "I do not like it when the model is wrong about people I like."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 08:00–10:59 | Front counter | Opening rentals. Intake photos. Board updated from yesterday's returns. |
| 11:00–15:59 | Front counter | Peak volume. Insurance upsell at speed. Predictions logged. |
| 16:00–18:59 | Front counter / floor | Return photos, damage forms, claim interrogations |
| 19:00–20:59 | Front counter | Reconciling the board. Settling with her father. Bringing Opa Cees coffee. |
| 21:00–08:00 | Closed | — |

### Positioning Notes
- Front counter, nearest the door, beside the insurance tier display — she is the first van der Berg the player meets and the softest angle of the two-temperature upsell
- Her nationality tally chalkboard is visible over her shoulder throughout every conversation, updating between visits
- Sightline to Dirk mid-shop for the cross-shop reaction beats (the coin payment, the Genuine Surprise glance)
- She does not enter the repair station. It is Opa's. The coffee is handed through the doorway.

---

## 🎒 Inventory / Services

### Services Offered
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Rental processing | — | — | Intake form, deposit hold, intake photo |
| Standard Insurance | 10 Sovs | 10 Sovs | Theft + minor damage, "minor" per Dirk's written definition |
| Premium Insurance | 20 Sovs | 20 Sovs | Theft, damage, incidents, one canal recovery attempt |
| Platinum Insurance | 35 Sovs | Statistically 0 Sovs | Everything but war and nuclear events; includes Opa Cees's Blessing for the rental duration |
| Damage prediction wager | Free | 10% if she loses | She names your damage type in advance; wrong = 10% off next rental |
| Insurance claim processing | Free | Variable | Interrogation stage of `shamsterdam_quest_insurance_claim` |
| Add-ons (helmet, vest, mount, liner) | 2–5 Sovs/day | Fair | Sold at the counter with her editorial commentary attached |

### Hidden Details / Easter Eggs
- **The nationality tally board**: A real, examinable asset that updates with player behaviour. Damage a bike as a given nationality and the board reflects it on the next visit. Examine it late-game and the player's own contributions are visible in the numbers.
- **The folded form in the drawer**: If you decline the prediction game, she writes it down anyway. Examine the drawer during the Insurance Claim quest and the folded form is there, with her prediction, and it is correct.
- **The undamaged-return recalibration**: Returning three bikes undamaged causes her to permanently change one of her opening assessment lines to acknowledge you specifically. It is the only dialogue in the shop that rewrites itself.
- **The five Sovs**: The running Dirk–Anneke wager is tracked. Examine the till late-game: there is a small handwritten ledger. Anneke is up.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Dirk van der Berg | Father. He runs the shop; she runs the numbers. The running wager is real, is settled in coins, and she is winning. |
| Opa Cees | Grandfather. She brings him coffee. The coffee is bad. He drinks it. She has never been in the basement. |
| The Bike Rental Guy (Bike Crossing kiosk) | Same fleet, same forms, different counter. She thinks he should keep a board. He does not keep a board. |
| Henk (Voetgangerstunnel) | Sells the underground alternative. Anneke's assessment: "He charges five Sovs to guess. I do it free and I am better at it." |
| Officer van den Berg (Bike Crossing) | Same surname. She finds the question funny and answers differently every time she is asked. |
| Marloes (Voetgangerstunnel map vendor) | Never met. Same profession — selling accuracy to people who ignore it — and neither knows the other exists. |

### Territory / Social Dynamics
- Three generations staged in depth: Anneke front (warm, fast, assessing), Dirk middle (cold, statistical), Opa Cees back (absorbed, honest). The upsell works because the player is warmed up by one and hard-numbered by the other within ninety seconds.
- The family betting pool is Anneke's invention and the shop's most functional institution. Dirk denies participating and pays out in coins.
- She is the only van der Berg who has ever been *pleased* by a customer rather than surprised by one.

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **First visit**: Nationality read, insurance run, intake photo, prediction offered
- **Return (bike return)**: Comparison photo, damage form, prediction resolved, board updated
- **Third rental**: "You are becoming a data point with a name"
- **Tour de Shame arc**: Holds the bet against the player, pays out visibly on completion
- **Post-Canal-Recovery**: The basement line — the one moment she registers being outside something in her own family

### In Other Cities
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| — | — | Anneke does not leave the shop or the city during the game. She is three years into a business she intends to inherit. | — |

### Evolution Through Game
Her model breaks and she enjoys it. She begins with a confident classification of the player and ends having to hand-edit her own opening line to account for them. The arc is not affection — it is a statistician acquiring an outlier she is fond of, which in this family is the same thing.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| idle_with_clipboard | 2 frames, 0.5 FPS. Standing ready, weight on one hip. | 55% |
| writing_on_form | 3 frames, 1 FPS, loop. Documenting. | 30% |
| board_glance | Looks at the nationality tally, back to the form | 10% |
| pen_click | Uncaps, recaps, uncaps | 5% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| taking_photo | 3 frames, 2 FPS + camera flash effect. Intake and return photos. Fires mid-sentence. |
| skeptical_expression | 2 frames, 0.5 FPS. Any customer damage description. |
| called_it_reaction | 2 frames, 1 FPS. Correct damage prediction. |
| recalibration_pause | Wrong prediction, or an undamaged return. She stops moving entirely for one beat. |

### Sprite States
| State | When Used |
|-------|-----------|
| anneke_counter | Default, front counter |
| anneke_assessing | Return photography and damage documentation |
| anneke_high_contrast | Accessibility outline variant marking her as interactive |

---

## 🎯 Quest Integration

### Primary Quest: The Insurance Claim
- **Quest**: The Insurance Claim (`shamsterdam_quest_insurance_claim`)
- **Role**: Primary interrogator. Anneke runs stages 1–3; Dirk delivers the ruling in stage 4.
- **Trigger**: Filing a claim on a damaged or lost rental
- **Stages**:
  1. Fill out the claim form (dialogue tree)
  2. Provide the incident description (free-text / creative writing selection)
  3. Anneke's skeptical follow-up questions — three, escalating, keyed to internal consistency
  4. Dirk's final assessment
  5. Claim approved or denied
- **Outcome**: Honest descriptions get better payouts. Creative-but-sincere descriptions unlock bonus dialogue (the wildlife box). Obviously false claims are denied with a reputation hit that persists across the shop's dynamic greetings.

### Supporting Quest Roles
- **Tour de Shame**: Anneke holds the bet against the player and pays out visibly on completion. She is not a quest step but she is the emotional scoreboard.
- **Keg Cycle**: Processes the rental and recommends Premium for cargo capacity. Predicts "basket" and is usually right.

### Quest Gate Function
Anneke gates nothing structurally. Mechanically she gates the **prediction discount** (a repeatable 10% off obtainable only by surprising her) and, via the claim interrogation, the difference between a good payout and a denied claim. Her gate is honesty: the Insurance Claim quest measurably rewards truthful play, and she is the one who checks.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Prediction discount | Wrong prediction | Next rental | 10% off |
| Insurance payout | Claim approved | One-time | Variable; scales with description honesty |
| Anneke's number | Survivor Package (40 Sovs) | Rental duration | "In case of emergency only." Has never been dialled. Dialling it is not implemented and should not be. |

### State Flags Set
- `anneke_met`: boolean
- `anneke_predictions_correct`: integer
- `anneke_predictions_wrong`: integer
- `anneke_nationality_board`: object (per-nationality damage tallies, player-influenced)
- `anneke_undamaged_returns`: integer (recalibration line rewrites at 3)
- `insurance_claim_filed`: boolean
- `insurance_claim_honesty`: enum (honest / creative / false)
- `anneke_reputation_hit`: boolean

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. The nationality tally chalkboard, mid-game, with the player's own contributions visible
2. Anneke's skeptical face at the exact moment a bro says "it was basically already like that"
3. The intake photo — the face the player was caught making, framed on the comparison wall
4. Anneke paying her father five Sovs in coins across the shop floor
5. The folded prediction form in the drawer, unfolded, correct

### Meme Potential
- "American? British? ...Australian. Okay, let me get the reinforced form."
- "That's the face they all make."
- "Called it. Tram tracks. Dad owes me five Sovs."
- "Have you ever ridden a bike before? Like, in traffic? Where people want you dead?"
- "I am putting 'swan.' There is a box for wildlife. There has never been anything in the box."

---

## 🗣️ Voice Direction

### Accent
Dutch, young, urban, fluent conversational English with a faster cadence than either her father or grandfather. She uses contractions where they do not. That single grammatical difference is the generational marker and voice direction should hold it consistently.

### Tone
- **Greeting**: Genuinely warm. Not performed. She likes this part of the job.
- **Insurance run**: Fast, complete, rehearsed but not bored — she is proud of knowing it cold.
- **Prediction**: Playful, and completely serious underneath. Both at once.
- **"Called it"**: No gloating. It is the pleasure of a model working, not of a customer failing.
- **Recalibration (wrong prediction / undamaged return)**: The one place she goes quiet. Delight, not embarrassment.
- **Claim interrogation**: Friendly the whole way through, which is what makes the third question land.

### Key Delivery Notes
- The nationality read is a beat, not a sneer. She is sorting, not judging, and the punchline is the word "reinforced."
- "Smile!" and the flash must overlap. She does not wait.
- "Good luck! I mean it. Really." is completely sincere and should be played that way — the joke is that she has already written the prediction.
- Never let her sound like she is enjoying the crash. She is enjoying the *data*. That distinction is the entire character.

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Full appearance documented | ✅ |
| Personality & motivation clear | ✅ |
| Complete dialogue trees | ✅ |
| Schedule & location specified | ✅ |
| Connections to other NPCs | ✅ |
| Recurring appearances planned | ✅ |
| Animation states defined | ✅ |
| Quest integration documented | ✅ |
| Sprite notes for artists | ✅ |
| Comedy value preserved | ✅ |
| Bros never achieve self-awareness | ✅ |
| World consistency (city names) | ✅ |

---

## 📝 Development Notes

- **The prediction wager must genuinely pay out.** If Anneke's model is never wrong, she becomes cruel; the 10% discount is the mechanic that keeps her likeable. Target accuracy is roughly 70% — high enough to be impressive, low enough to lose regularly.
- The nationality tally board is a live, player-influenced data asset, not set dressing. It needs a persistent store and a legible late-game read.
- The intake photo must fire mid-sentence, before the player's dialogue box finishes. If the player has time to prepare, the "that's the face they all make" line has nothing to refer to.
- The undamaged-return recalibration at 3 rewrites her opening line permanently for that save. It is the only self-editing dialogue in the location and it should not be signposted.
- Anneke and Dirk's two-temperature upsell must always fire in order — Anneke first (warm), Dirk second (cold). If the player reaches Dirk first, the insurance conversion drops and the scene reads wrong. Front-counter placement enforces this; do not move her.
- Anneke's number from the Survivor Package must remain undialable. It is a joke about liability, not a hook.
- Canon check: Anneke's name appears exactly once in Shamsterdam. Do not add a second Anneke anywhere in the game.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Anneke has none. Sovs, card, credit card holds, and a five-Sovs coin wager with her father.
- [x] **NO automatic crypto assumptions** — she keeps a chalkboard, not a ledger contract
- [x] **Coins, kiosks, and certificates come from the master pool** — N/A, no crypto at this location
- [x] **The bros are never scam-aware** — Lord Pilsner believes he is being flirted with while being actuarially assessed, and this will never resolve
- [x] **Nothing winks** — Anneke states her methods plainly and out loud, which is precisely why nobody hears them
- [x] **Focus on city-specific cultural exploitation instead** — the satire is the insurance upsell and tourist self-assessment, not Dutch retail

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the nationality board is a joke about tourist cycling incompetence, is player-influenced, and never attaches a trait to a people beyond "how they crash a rental bike"
- [x] NPC is savvy entrepreneur, not villain or stereotype — Anneke is competent, transparent about her methods, offers a discount when she is wrong, and pays her debts
- [x] Humour is affectionate mockery, not mean-spirited — her warmth is real, her wager costs her money, and her best moment is being wrong

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Shamsterdam/npcs/Shamsterdam_Bike_Rental/npc_anneke_van_der_berg.md`
- **Registered In**: `shamsterdam_bike_rental_npcs.json` — Yes. Pre-existing entry `shamsterdam_npc_anneke_counter_01`; `full_profile` path added in this pass.
- **Sprite Sheet**: `npc_anneke_counter.png` (240×256, 48×64 sprites, 4 animation rows) — specced in `PNG_Assets/shamsterdam_bike_rental_png_assets.md`, Sprite Sheet 4. Supporting: `bike_rental_effects.png` (Camera Flash, Form Stamp), `bike_rental_displays.png` (Nationality Tally Board, Insurance Comparison Chart).

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — Wave 1 (mechanics-attached NPCs). Sourced from `shamsterdam_bike_rental.md` + `PNG_Assets/shamsterdam_bike_rental_png_assets.md` + `shamsterdam_bike_rental_npcs.json`. | Shamsterdam NPC authoring pass |

---

*Template Version 1.1*
