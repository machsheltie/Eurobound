# NPC Profile: Dirk van der Berg

*"The basic covers theft. The premium covers damage. The platinum covers your dignity. None of them cover your decision-making."*

## 📋 NPC Identity
- **NPC ID**: `shamsterdam_npc_dirk_rental_owner_01`
- **Display Name**: Dirk van der Berg
- **Internal Name**: Dirk — Owner/Manager, Shamsterdam Bike Rental (second of three generations on the floor)
- **Role**: Vendor / Service Provider / Quest Giver / Recurring Interaction Anchor
- **Associated Quest**: `shamsterdam_quest_tour_de_shame` (giver); supports `shamsterdam_quest_insurance_claim` (final assessor) and the "Keg Cycle" delivery quest (rental prerequisite)
- **Primary Location**: Shamsterdam Bike Rental — main counter, Shamsterdam (south side of the Central Bike Crossing)
- **Secondary Appearances**: Referenced at Central Shamsterdam Bike Crossing (the orange bikes in traffic are his fleet); Canal Ring Promenade during Canal Recovery quest resolution

---

## 🎭 Core Concept

### What He's Actually Doing
Running a legitimate, profitable, twenty-two-year-old bike rental business whose margin comes overwhelmingly from deposit forfeitures and damage claims. He tells every customer, truthfully and in detail, exactly how badly this is likely to go. He does this because it is honest, because it protects him legally, and because it does not work — the warning has never once prevented a rental. He would genuinely prefer the bikes came back. They mostly do not. His name tag reads "Dirk - 22 Years - 847 Canal Recoveries" and every number on it is accurate.

### What Bros Believe
That Dirk is doing a bit. Lord Pilsner has decided the warnings are "part of the experience," like a haunted house barker. Chadwick is filming the insurance tier chart as content. Bradley — the only one listening — buys the Platinum, and Dirk quietly notes that the people who buy Platinum never need it, because the impulse to buy Platinum and the impulse to crash are mutually exclusive.

### The Comedy Gap
Dirk is the most honest vendor in Shamsterdam. He discloses everything. The disclosure has become the sales pitch. The bros hear "seventeen years of tourists have tried this and the bikes come back, sometimes" and interpret it as a challenge, which converts a legal warning into an upsell. He is not exploiting anyone. He is being ignored profitably, which is worse and funnier.

### The Detail That Makes Him Not A Villain
Dirk keeps the free Crossing Tips service on the menu at 0 Sovs and pushes it before every rental. Nobody takes it. He offers it anyway, every time, twenty-two years running.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Mid-50s |
| Build | Stocky; bike-mechanic mass in the forearms and shoulders, not the gym kind |
| Height | Average, but he takes up counter |
| Energy | Weathered, patient, statistically informed |

### Clothing
- **Orange polo, stretched**: Company uniform, brand orange (#FF6600), fitted for a smaller version of him from some years ago. He has not requested a new one.
- **Name tag**: "Dirk - 22 Years - 847 Canal Recoveries." The canal count updates. Artists must design the tag to accommodate a four-digit number.
- **Accessories**: A pen behind the ear he never uses (he uses Anneke's); a workshop rag in the back pocket
- **Footwear**: Steel-toe work boots, indoors, always

### Distinguishing Features
- Grease permanently embedded in the creases of both hands. Not dirty — sealed. It does not wash out and he stopped trying.
- The "I told you so" expression, which is his most-used animation and which precedes the words by a full second
- Genuine surprise is a distinct and rare face; players may go the whole game without seeing it
- Speaks while doing something else — filing, stamping, checking a wheel — and only makes eye contact for the important sentences

### Sprite Notes
Sheet `npc_dirk_rental_owner.png` (288×320, 48×64 sprites, 5 rows). Row 3 — "I Told You So" — must be legible at thumbnail size; it is the shop's signature reaction and the most-triggered state in the location. Row 4 — Genuine Surprise (3 frames) — is rare, and should be drawn as a completely different face, not a variation: eyebrows up, mouth slightly open, the man briefly unarmoured. Dirk stands mid-shop with Anneke at the counter in front and Opa Cees framed through the repair-station doorway behind: three generations staged in depth.

---

## 🧠 Personality

### Archetype
**The Honest Operator Nobody Listens To** — Dirk has run the numbers on tourist cycling for twenty-two years and can recite them from memory. He discloses everything up front, prices fairly, and has developed a dry statistical humour as the only sustainable response to watching the same accident happen four thousand times. He is not cynical. He is calibrated.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Deadpan statistician | Delivers genuinely alarming numbers in the tone of a weather report |
| Sincerely invested in survival | Dead tourists are bad business and also bad. He means the warnings. |
| Perfected the "I told you so" | Twenty-two years of refinement. It is now almost gentle. |
| Secretly moved by competence | An undamaged return produces real, unguarded surprise. It is the character's warmest beat. |
| Unbudgeable on price | The damage assessment is fair, itemised, and non-negotiable. He will show you the parts. |

### Internal Monologue
> "Seventeen of them this week said they cycle at home. At home. There are no trams at home. There are no forty cyclists behind you at home who will not stop and will not swerve because it has never once been necessary. I tell them. I tell all of them. And then I take the hundred and fifty Sovs hold, and I write the date on the form, and I think about which bike it will be. Usually it is the one with the good brakes. They always take the one with the good brakes and then they use them."

### Motivation
Keep the shop going, keep the family in it, keep the fleet turning over, and — genuinely, underneath all of it — get everybody back in one piece. He would trade the damage revenue for the return rate. He is not going to get to make that trade.

---

## 💬 Dialogue

### Approach/Greeting

**First visit**:
> "Welcome to Shamsterdam Bike Rental. You've already decided to rent one, haven't you."
> *(He does not wait for an answer. He reaches for the form.)*
> "Let me tell you why you shouldn't."

**Return visit, bike not returned**:
> "You're back. The bike is not. This is why we take deposits."

**Return visit, bike undamaged**:
> "No damage? No damage at all?"
> *(Full stop. He actually looks at the player. This is the Genuine Surprise animation.)*
> "...I don't believe you, but I respect the lie."

**Multiple rentals, player still alive**:
> "Ah, you again. Still alive. The statistics were not in your favour."

### Key Interaction Dialogue — The Insurance Pitch

*Dirk turns the laminated tier chart around on the counter. He has done this so many times that the card is worn white at the corner where his thumb goes.*

**Dirk** (flat, unhurried):
> "The basic covers theft. The premium covers damage. The platinum covers your dignity. None of them cover your decision-making."

**On Standard (10 Sovs)**:
> "Standard covers minor damage. I define minor. You will not agree with my definition. That is why it is written down."

**On Premium (20 Sovs)**:
> "Twenty Sovs sounds like a lot until you're fishing your holiday out of a canal. It includes one recovery attempt. One. The canal gets a vote."

**On Platinum (35 Sovs)**:
> "The platinum tier. Nobody who buys this has ever used it." *(He lets that sit.)* "They are too careful to need it. Funny how that works."

**If player declines all insurance**:
> "That is allowed. The deposit is one hundred and fifty Sovs. The bike is three hundred and fifty. I am telling you these two numbers in the same sentence on purpose."

### Sales Close — The Rental

> "Basic is fifteen. Premium is twenty-five, and the brakes are better, and yes, that matters. The Survivor is forty — reinforced frame, twelve canal recoveries, still true."
> *(He sets the keys down.)*
> "Lock combination is on the tag. You will forget it. Everyone forgets it. Come back and I will tell you again, free."

### The Free Service Nobody Takes

> "Before you go. Crossing tips. It costs nothing. It takes ninety seconds."
> *(A pause. It is always the same length.)*
> "No. Nobody ever does. Good luck."

**If the player actually accepts Crossing Tips**:
> *(He stops. He puts the form down. He gives ninety seconds of genuinely excellent, specific advice about tram tracks, right-of-way, and the bell.)*
> "...That is the first time this month. Take the premium. I will do it at basic price."

### Damage Assessment

**Minor**:
> "This? This is nothing. I have seen worse before breakfast." *(Beat.)* "Eight Sovs. The tyre."

**Major**:
> "How did you even—" *(He stops himself. He genuinely does not want to know.)* "No. Let me get the form."

**Canal**:
> "The canal. Again."
> *(He looks at the bike for a long moment. Seaweed. The smell.)*
> "Do you know how cold that water is? The bike knows. Eight hundred and forty-eight."

**Total loss / no return**:
> "Three hundred and fifty. Deposit covers one-fifty of it. You will need a police report for the insurance, and the police will ask you where it was, and you will not know."
> *(He takes a polaroid off the counter and pins it to the memorial board without comment.)*

### Quest Accept — "Tour de Shame"

*Triggers on the player's second rental.*

> "You have rented twice and come back twice. That puts you above most."
> *(He pulls a folded, hand-drawn circuit map from under the counter. It is not a printed product. He made it.)*
> "Coffeeshop Quarter. Museum Mile. Roodelicht Row. Cheese and Clog Corner. Canal Ring Promenade. All five. Twenty minutes. No damage."
> "Nobody has done it. My daughter says nobody will. She has money on it."
> *(A beat.)*
> "So do I. Go on."

**On completion**:
> "Twenty minutes. Five districts. No damage."
> *(He looks at the bike. He looks at the player. He does not say anything for a moment.)*
> "Twenty percent off. Permanently. And take this—" *(a small brass bell)* "—it is a good bell. It will not help. Nobody stops for a bell. But it is a good bell."

**On failure**:
> "Twenty-three minutes. And the wheel." *(He is not unkind about it.)* "Try again tomorrow. The circuit is not going anywhere. Neither am I."

### Post-Interaction
> *(Returns to the paperwork. Writes the date. Does not look up.)* "Bell on the left. Brake on the right. Both of them are the front one. Go."

### If Player Declines / Alternative Path
**Player leaves without renting**:
> "Sensible. The tunnel is free and only confusing." *(Beat.)* "Mostly free."

**Player mentions renting elsewhere**:
> "There are cheaper. Their bikes are also cheaper. That is the same sentence twice."

### Callback Dialogue (Return Visits)
**After Canal Recovery quest with Opa Cees**:
> "My father says you pulled three out of the water." *(Something shifts fractionally.)* "He does not say things about people. Take the premium at basic price."

**After Tour de Shame completion, subsequent rentals**:
> "The champion. Twenty percent." *(He does not smile. The discount is the smile.)*

**Late game**:
> "You have been in this shop more than some of my staff." *(He hands the keys over without the warning speech.)* "You know the numbers. Go."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 08:00–10:59 | Main counter | Morning rentals. Full warning speech delivered at full length. |
| 11:00–15:59 | Main counter / floor | Peak rental window. Warning speech compresses under volume. |
| 16:00–18:59 | Main counter | Returns and damage assessments. The day's actual work. |
| 19:00–21:00 | Repair station doorway | With Opa Cees. Counting the fleet. Closing. |
| 21:00–08:00 | Closed | "Tourists shouldn't cycle in the dark." He means it. |

### Positioning Notes
- Mid-shop, behind the main service counter, with the damage photo gallery directly behind his left shoulder — every conversation is framed against evidence
- Sightline through the repair-station doorway to Opa Cees; he checks it periodically without comment
- Anneke at the secondary counter in front of him, near the insurance display, which means the upsell hits the customer twice from two angles at two temperatures
- The memorial board is positioned so customers pass it on the way out, not the way in. This is deliberate and Dirk arranged it.

---

## 🎒 Inventory / Services

### Bike Rental Tiers
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Basic Rental | 15 Sovs/day | 15 Sovs | Standard orange bike, lock, basket. Bypasses the Bike Crossing mini-game. One free "I told you so." |
| Premium Rental | 25 Sovs/day | 25 Sovs, honestly | Better brakes (materially better), working bell, upgraded lock, map holder. Dirk's reluctant respect. |
| "Survivor" Package | 40 Sovs/day | 40 Sovs | Reinforced frame (12 canal recoveries survived), reflective tape, emergency whistle. Anneke's number "for emergencies only." |
| Crossing Tips | Free | Extremely high | 90 seconds of genuinely correct cycling advice. Offered every time. Taken almost never. |

### Insurance Packages
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Basic Insurance | Included | Marginal | Theft only, with police report. Excludes damage, canal, user error, Dutch cyclists. |
| Standard Insurance | 10 Sovs | 10 Sovs | Theft + minor damage. "Minor" defined by Dirk, in writing. |
| Premium Insurance | 20 Sovs | 20 Sovs | Theft, damage, "incidents." One free canal recovery attempt. |
| Platinum Insurance | 35 Sovs | Statistically 0 Sovs | Everything but war and nuclear events. Unlimited canal recoveries. 500 Sovs damage waiver. Includes Opa Cees's blessing (minor navigation buff). Has never been claimed on. |

### Add-Ons & Deposits
| Item/Service | Price | Effect/Result |
|--------------|-------|---------------|
| Helmet | 5 Sovs/day | +10% Collision Survival, marks you visibly as a tourist |
| High-Visibility Vest | 4 Sovs/day | +20% Visibility, −30% Dignity |
| Phone Mount | 3 Sovs/day | GPS while cycling; distraction risk |
| Basket Liner | 2 Sovs | Stops small items falling through |
| "Tourist Escort" Guide | 50 Sovs/hour | Guided cycling on safe routes |
| Standard Deposit | 150 Sovs | Or credit card hold |
| Bike Replacement | 350 Sovs | Non-negotiable |
| Canal Recovery Fee | 75 Sovs found / 350 Sovs not found | The canal gets a vote |

### Hidden Details / Easter Eggs
- **The name tag counter**: "847 Canal Recoveries" increments in real time. Dump a rental in the canal and the tag reads 848 on your next visit. Nobody mentions it.
- **The hand-drawn Tour de Shame map**: Not a printed asset. Examine text reveals it is drawn on the back of a 2009 insurance renewal notice, with the Cheese & Clog Corner leg redrawn twice.
- **The cash discount**: 5% for cash, offered without being asked, only to players who have returned a bike undamaged at least once
- **Crossing Tips acceptance**: Accepting the free tips is tracked. It is the single cheapest way to earn Dirk's genuine respect and the game never signposts it.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Anneke van der Berg | Daughter. Three years on the counter. He disapproves of the editorial commentary and has never once told her to stop. |
| Opa Cees | Father. Forty-seven years in the repair station. Dirk runs the front; Cees runs the back; the arrangement has never been discussed. |
| The Bike Rental Guy (Bike Crossing kiosk) | Sells the same fleet at the crossing kiosk. Same warnings, same non-compliance, different counter. Professional parity. |
| Officer van den Berg (Bike Crossing) | Same surname. No confirmed relation. Dirk has been asked and answers, "It is a common name." He does not elaborate. |
| Henk (Voetgangerstunnel) | Sells the underground alternative. Dirk considers the tunnel "free and only confusing," which is the most he will say about a competitor. |
| Brewmaster Hendrik (Brouwerij de Molen) | Brewery-tour cyclists rent from here. Dirk has opinions about arriving at a tasting flight on a bicycle and keeps them to himself. |

### Territory / Social Dynamics
- Three generations, staged in depth: Anneke front, Dirk middle, Cees back. The player moves through the family in order of increasing honesty and decreasing commercial interest.
- Dirk and Anneke run a two-temperature upsell — his cold statistics, her warm prediction game — and it is far more effective than either alone. Neither planned it.
- The family betting pool on renter damage is Anneke's; Dirk pretends not to participate and owes her five Sovs as of the most recent tram-track incident.

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **First visit**: Full introduction, insurance hard-sell, the warning, the photo "for records"
- **Return visit (bike return)**: Damage assessment scene, deposit resolution, commentary keyed to condition
- **Second rental**: "Tour de Shame" unlocks. He gives it in person, from under the counter, unprompted.
- **Subsequent rentals**: Dynamic greeting from player history — the file on you is real and he reads from it
- **Post-Canal-Recovery**: One-off dialogue where he passes on his father's rare compliment

### In Other Cities
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| — | — | Dirk does not leave the shop, the district, or the city. Any rental-shop archetype elsewhere is a different person. | — |

### Evolution Through Game
Dirk's arc is a discount and a dropped speech. He never becomes warm. What changes is what he stops saying: the warning speech shortens visit by visit until, in the late game, he simply hands over the keys and says "You know the numbers. Go." That silence is the relationship.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| idle_at_counter | 2 frames, 0.5 FPS. Standing, slight weight shift. | 55% |
| checking_paperwork | 3 frames, 1 FPS. Forms, dates, filing. | 30% |
| doorway_glance | Looks through to the repair station, back to the form | 10% |
| hand_wipe | Wipes grease off hands with the rag. It does not come off. | 5% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| pointing_at_crossing | Warning gesture during the crossing speech |
| i_told_you_so_expression | Any damaged return; any player who ignored the Crossing Tips offer |
| genuine_surprise | Undamaged return, or player accepting Crossing Tips. Rare. |
| damage_assessment | 4 frames. Bike inspection sequence on return. |

### Sprite States
| State | When Used |
|-------|-----------|
| dirk_counter | Default, front of shop |
| dirk_assessing | Damage assessment, bent over the bike |
| dirk_surprised | Genuine Surprise only — a distinct face, not a variant |
| dirk_high_contrast | Accessibility outline variant marking him as interactive |

---

## 🎯 Quest Integration

### Primary Quest: Tour de Shame
- **Quest**: Tour de Shame (`shamsterdam_quest_tour_de_shame`)
- **Role**: Quest Giver
- **Trigger**: Player's second bike rental. Given face to face, unprompted, from under the counter.
- **Objective**: Cycle a circuit hitting Coffeeshop Quarter → Museum Mile → Roodelicht Row → Cheese & Clog Corner → Canal Ring Promenade, return the bike undamaged, total time under 20 minutes
- **Outcome**: "Tour de Shame Champion" achievement, permanent 20% rental discount, "Golden Bell" cosmetic, and Dirk's genuine respect (rare, and mechanically expressed as the discount rather than a line)

### Supporting Quest Roles
- **The Insurance Claim** (`shamsterdam_quest_insurance_claim`): Dirk is the final assessor. Anneke asks the skeptical questions; Dirk makes the ruling. Honest incident descriptions get better payouts; creative ones unlock bonus dialogue; obviously false ones are denied with a reputation hit.
- **Keg Cycle**: Rental is a hard prerequisite. Dirk recommends Premium for cargo capacity and is correct.
- **Canal Recovery Assistant**: Not his quest (Opa Cees owns it), but completing it unlocks a one-time Dirk dialogue and a discounted premium rental.

### Quest Gate Function
Dirk gates bicycle access, which gates the Bike Crossing bypass, the cyclist-only shortcuts, faster district travel, and the Keg Cycle timer challenge. The gate is entirely economic — 15 Sovs and a 150 Sovs hold — and he will not refuse anyone, no matter how many bikes they have destroyed. He will, however, quote the running total.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Rental Bike (tiered) | Any | No | Bypasses Bike Crossing mini-game; Orange Target debuff active while ridden |
| Golden Bell | Tour de Shame complete | Yes | Cosmetic. Nobody stops for a bell. |
| Responsible Renter | Undamaged return | One rental | 10% discount on the next rental |
| Permanent 20% discount | Tour de Shame complete | Yes | Applies to all tiers and add-ons |

### State Flags Set
- `dirk_met`: boolean
- `dirk_rental_count`: integer
- `dirk_undamaged_returns`: integer
- `dirk_canal_recovery_count`: integer (drives the name tag number)
- `dirk_crossing_tips_accepted`: boolean
- `tour_de_shame_offered`: boolean
- `tour_de_shame_complete`: boolean

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. The insurance tier chart, four columns of escalating warnings, Platinum in a gold border
2. Dirk's Genuine Surprise face — rare enough that posting it is a flex
3. The damage photo gallery behind him during a damage assessment, the new photo about to join it
4. The name tag reading a number the player personally incremented
5. The hand-drawn Tour de Shame map on the back of a 2009 insurance notice

### Meme Potential
- "The platinum covers your dignity. None of them cover your decision-making."
- "You're back. The bike is not."
- "No damage? I don't believe you, but I respect the lie."
- "How did you even— No. I don't want to know."
- "Before you go. Crossing tips. It costs nothing." — the free advice nobody takes, as a reply format

---

## 🗣️ Voice Direction

### Accent
Dutch, direct, unornamented. Standard Shamsterdam commercial register. His English is fluent and slightly clipped; he does not soften statements and does not use hedging language, which is why the warnings land as jokes to people used to hedging.

### Tone
- **Warning speech**: Weather report. No urgency, no theatre. The content is alarming; the delivery is not.
- **Insurance pitch**: Rehearsed, but not tired. He believes the tiers are correctly priced because they are.
- **Damage assessment**: Neutral, itemised, professional. Never gloating. The "I told you so" is a face, not a tone.
- **Genuine Surprise**: Unarmoured. One beat of a different man. Do not overplay it — it works because everything around it is flat.
- **Tour de Shame handoff**: The one place he is almost animated. He made the map. Something in the read should know that.

### Key Delivery Notes
- "Let me tell you why you shouldn't" is not sarcastic. He is about to actually tell you.
- Numbers are delivered as numbers, never as punchlines. The audience supplies the punchline.
- "...I don't believe you, but I respect the lie" — the pause before it is longer than feels comfortable in the booth. Keep it.
- He never raises his voice, not for the canal, not for total loss, not ever.

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

- **The warning must always be given in full on first rental, and must never prevent the rental.** If a player can be talked out of it, the joke breaks. Dirk discloses; the player proceeds; the shop profits; nobody was deceived.
- Crossing Tips at 0 Sovs must remain on the service menu permanently and must be genuinely useful when accepted (measurable Bike Crossing accuracy improvement). It is the character's moral floor.
- The name tag canal counter must be live-bound to `dirk_canal_recovery_count`. Art needs a four-digit-capable tag.
- Insurance reduces damage cost, never damage probability. Dirk says this out loud in the Standard pitch and it must remain true in code.
- Genuine Surprise is a **distinct sprite**, not a palette or eyebrow variant. If a player can't tell it apart from idle at a glance, the location's warmest beat is invisible.
- Tour de Shame must be given face to face on the second rental, not via a quest board or notification. The hand-drawn map is the point.
- Do not let Dirk crack. No moment of "we both know this is ridiculous." He has run these numbers; to him it is not ridiculous, it is Tuesday.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Dirk has none. Sovs, cash discount, credit card holds for deposits.
- [x] **NO automatic crypto assumptions** — a twenty-two-year family bike shop takes cards and cash and nothing else
- [x] **Coins, kiosks, and certificates come from the master pool** — N/A, no crypto at this location
- [x] **The bros are never scam-aware** — there is no scam to be aware of; they are aware of neither the scam nor the honesty
- [x] **Nothing winks** — Dirk never signals that the warnings are a bit. He is not doing a bit.
- [x] **Focus on city-specific cultural exploitation instead** — the satire is tourist cycling confidence and the insurance industry, not Dutch business

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the joke is the bros hearing full disclosure as a dare
- [x] NPC is savvy entrepreneur, not villain or stereotype — Dirk is a competent, honest, fairly-priced operator who offers free correct advice and is systematically ignored
- [x] Humour is affectionate mockery, not mean-spirited — his respect is earnable, his surprise is sincere, and his father and daughter both like him

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Shamsterdam/npcs/Shamsterdam_Bike_Rental/npc_dirk_van_der_berg.md`
- **Registered In**: `shamsterdam_bike_rental_npcs.json` — Yes. Pre-existing entry `shamsterdam_npc_dirk_rental_owner_01`; `full_profile` path added in this pass.
- **Sprite Sheet**: `npc_dirk_rental_owner.png` (288×320, 48×64 sprites, 5 animation rows) — specced in `PNG_Assets/shamsterdam_bike_rental_png_assets.md`, Sprite Sheet 3. Supporting: `bike_rental_displays.png` (Insurance Comparison Chart, Damage Photo Gallery, Canal Memorial Board), `bike_rental_effects.png` (Form Stamp, Cash Register Ching, Damage Reveal).

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — Wave 1 (mechanics-attached NPCs). Sourced from `shamsterdam_bike_rental.md` + `PNG_Assets/shamsterdam_bike_rental_png_assets.md` + `shamsterdam_bike_rental_npcs.json`. | Shamsterdam NPC authoring pass |

---

*Template Version 1.1*
