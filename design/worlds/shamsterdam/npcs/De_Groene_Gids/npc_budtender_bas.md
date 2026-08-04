# NPC Profile: Budtender Bas

*"Space cake takes two hours. Yes, I know you feel nothing. Two. Hours."*

## 📋 NPC Identity
- **NPC ID**: `shamsterdam_npc_budtender_bas_01`
- **Display Name**: Budtender Bas
- **Internal Name**: Bas — primary counter service, De Groene Gids (flagship coffeeshop, "Famous Since 1985", changed owners 2017)
- **Role**: Vendor / Counter Service / Scripted-Response Machine / Rule Enforcer
- **Associated Quest**: None owned. Administers the "Space Cake Timer" system and the "It's Not Working" dialogue chain; feeds the munchies pipeline into Leeman's, Kapsalon Koning, and FEBO.
- **Primary Location**: De Groene Gids — ground floor counter, Coffeeshop Quarter, Shamsterdam
- **Secondary Appearances**: None. Bas is behind that counter and the "VIP Lounge" upstairs is the same room with different carpet.

---

## 🎭 Core Concept

### What He's Actually Doing
Reading a script. Bas provides accurate product information, enforces the no-tobacco rule, redirects card payments to the branded ATM, and states the space cake timing correctly and repeatedly to people who will not believe him. Every line he delivers is true. Every price he quotes is double the going rate three streets away. He is not lying about anything; the shop's markup is the sign, not the product, and Bas is simply the man who says the numbers out loud.

### What Bros Believe
That they are somewhere historic. Lord Pilsner: "This is HISTORIC. We're in the GREEN GUIDE. THE Green Guide." Chadwick needs footage and is about to be told he cannot have it. Bradley reads a laminated menu with too many options and asks whether there is a "signature blend," which there is, and it is the highest-margin item, and Bas will recommend it because that is what the script says.

### The Comedy Gap
The bros are paying 20 Sovs a gram for a sign. Locals walk past the door to smaller shops with better product and Bas watches them do it forty times a night. He has told the truth in every sentence and it has never once functioned as a warning. The satire is brand tourism: paying for the photo, not the product, and defending the purchase afterward.

### The Dead Eyes
Bas has the largest frame count in the location and the smallest emotional range. His Dead-Eyed Stare is the held default between all scripted beats. He has explained the no-tobacco rule roughly fifty thousand times. He is not depressed and he is not rude — he is a competent employee who has run out of any reason to inflect.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Late 20s |
| Build | Counter posture. Forearms on the glass. Weight distributed for a six-hour shift. |
| Height | Average |
| Energy | Professional exhaustion, fully calcified |

### Clothing
- **Green polo (uniform)**: Coffeeshop green (#228B22), branded, issued. Everything in this shop is branded including, somehow, the chairs.
- **Name tag**: "BAS." Nothing else. The Employee of the Month board has had the same photograph since 2019 and it is not his.
- **Accessories**: A scoop, a scale, and a laminated menu he has never needed to read
- **Footwear**: Trainers. Six hours standing.

### Distinguishing Features
- **The Dead-Eyed Stare** — a held frame, the default between all scripted beats, and the location's designated fan-art frame
- Delivers everything in flat monotone including genuinely useful information
- The sigh, which precedes the no-tobacco explanation and has become part of the explanation
- Never raises his voice over the Dutch hip-hop, which is at 40% volume — just loud enough to prevent real conversation, which suits him

### Sprite Notes
Sheet `npc_groene_gids_cast.png` (1024×384, 64×96 sprites), Row 0. Bas Idle 1-2 at (0,0)/(64,0); Scripted Recommendation 1-3 at (128,0)–(256,0); Sigh 1-2 at (320,0)/(384,0) — the fifty-thousandth explanation; No-Tobacco Explanation 1-3 at (448,0)–(576,0), exhausted-teacher cadence in three beats; Ringing Up at (640,0); **Dead-Eyed Stare at (704,0) — held frame, the fan-art frame.**

**Asset-doc constraint carried forward: Bas has the largest frame count in the location and the smallest emotional range; his Dead-Eyed Stare is the held default between all scripted beats.** He must be visually distinguishable from Marieke by silhouette alone — she is the only staff sprite drawn with raised eyebrows, because commission is the difference.

---

## 🧠 Personality

### Archetype
**The Accurate Script** — Bas is a well-trained employee delivering correct information in a building designed to make correct information irrelevant. He does not upsell (that is Marieke's commission), does not gatekeep, and does not editorialise about the prices. He tells you what things do, how long they take, and what the total is. Then he says it again, because you did not believe him.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Factually reliable | Every product statement he makes is true. The menu descriptions are accurate and he will tell you to read them. |
| Emotionally absent | Not depressed. Not hostile. Depleted in a specific, professional way. |
| Rule-firm, never harsh | The no-tobacco rule is non-negotiable and he enforces it like a teacher, not a bouncer. |
| Immune to persuasion | The two hours are two hours. He has been asked to make them fewer hours several thousand times. |
| Uninterested in the brand | He works here. He has never once used the words "famous since 1985" without them being part of a required greeting. |

### Internal Monologue
> "He is going to ask for the strongest. They always ask for the strongest, and then they buy the tourist recommendation anyway, because the tourist recommendation is highlighted and highlighted things are chosen. Then in two hours he will be sitting exactly where the last one sat, very still, looking at the poster. Not even a good poster. Same poster as every shop in this district. Nobody has ever asked why there is a Bob Marley poster. It is because there is always a Bob Marley poster. That is the whole reason. That is the entire chain of reasoning."

### Motivation
The shift. Bas has no arc, no ambition disclosed to the player, and no complaint. He wants the group in front of him to read the menu, not mix tobacco, and accept that the space cake takes two hours. He has never been given any of these three things.

---

## 💬 Dialogue

### Approach/Greeting

**Required greeting (scripted, verbatim, every customer)**:
> "Welcome to De Groene Gids. Famous since 1985. How can I help you."
> *(No question mark in the delivery. There is no question in it.)*

**Return visit**:
> "Welcome to De Groene Gids. Famous since 1985. How can I—" *(He recognises the player. The script continues anyway, because it is the script.)* "—help you."

**Regular status (3+ visits, "Secret Menu" unlocked)**:
> "You want the secret menu." *(He slides an identical laminated card across.)* "It is the same items. Different names. I am required to call it the secret menu."

### Key Interaction Dialogue — The Scripted Recommendation

**Asked for a recommendation**:
> "Tourist recommendation? Shamsterdam Dream. Very smooth. Very popular."
> *(Scripted Recommendation animation, three frames. It is not a lie. It is also not advice.)*

**Extended, if the player lingers**:
> "You want recommendation? Shamsterdam Dream. Everyone wants Shamsterdam Dream. I will get Shamsterdam Dream."

**Asked what the strongest is**:
> "The menu has descriptions. The descriptions are accurate. Please read the descriptions."
> *(Bravado is lost. He did not cause this and does not notice it.)*

**Asked about the price**:
> "Yes, it's expensive. We are famous. Famous things cost money. This is how famous works."

### The No-Tobacco Tutorial

*Triggers on any attempt to mix tobacco. Three-beat animation, exhausted-teacher cadence.*

**Beat 1**:
> *(The sigh. It arrives before the sentence and is part of the sentence.)*

**Beat 2**:
> "Here, we do not mix tobacco. This is not... how we do. Please."

**Beat 3**:
> "No tobacco. Yes, I know you have your own. No. We do not mix here."

*(No gameplay penalty. Bravado lost from public correction. He has moved on before the player has.)*

### Cash Only

> "Cash only. ATM is there."
> *(Beat.)*
> "Yes, the fee is normal. No, we do not control the fee."

**If pressed on the 5 Sovs fee**:
> "It is not our machine." *(It is branded with the shop's logo.)* "It has our name on it. It is not our machine."

### The Space Cake Timer

**At purchase**:
> "Space cake takes two hours. Yes, I know you feel nothing. Two. Hours."
> *(Beat.)*
> "Wait two hours. Americans never wait."

**30 minutes — "It's not working"**:
> *(Not looking up.)* "It. Is. Working. Wait."

**60 minutes**:
> *(Still not looking up.)* "Ninety more minutes."

**90 minutes**:
> "You are going to leave a review." *(He continues weighing something.)* "Leave the review. Then wait thirty minutes and read it again."

**120 minutes — the effect lands**:
> *(He does not react. He has watched this happen approximately eleven thousand times. He does not even look over.)*

### The Photography Prohibition

*Chadwick's ring light is detected.*

> "No photos of the product. No photos of the menu. No photos of me."
> *(Beat.)*
> "Outside is fine. Everybody photographs outside. The sign is the point."

**Repeat offence**:
> "I asked once." *(He looks at the bouncer. That is the whole escalation.)*

### Sales Close

> "Your total is sixty-three Sovs."
> *(Ringing Up animation.)*
> "Would you like a bag. The bag is two Sovs."

**If the player queries the bag charge**:
> "The bag is two Sovs." *(He has no further information about the bag.)*

### Post-Interaction
> "Upstairs is the VIP lounge. It is ten Sovs. It is this room with a different carpet." *(Beat.)* "I am required to mention it. I have mentioned it."

### If Player Declines / Alternative Path
**Player asks for a sample**:
> "Your friend is asking if he can 'try a sample.' We do not do samples." *(Beat.)* "This is not Costco."

**Player asks for a small amount**:
> "The minimum is one gram." *(Beat.)* "There are shops where the minimum is smaller. They are that way." *(He points. He is not being helpful and he is not being unhelpful. He is answering.)*

**Player mentions a Yelp review**:
> *(Nothing. The Dead-Eyed Stare. Held.)*

**Player asks how he is**:
> *(A pause noticeably longer than any other pause he has.)* "Fine." *(He rings up the next customer.)*

### Callback Dialogue (Return Visits)
**Second visit**:
> "You came back." *(Not surprised. Not pleased.)* "Everybody comes back once."

**After the space cake has landed once**:
> "You know about the two hours now." *(He does not smile.)* "You will still ask. Everybody still asks."

**After visiting a local coffeeshop elsewhere in the Quarter**:
> "You have been somewhere else." *(Beat.)* "It was cheaper." *(Beat.)* "Welcome to De Groene Gids. Famous since 1985. How can I help you."

**Late game**:
> "Shamsterdam Dream." *(He is already weighing it. He has not asked.)* "I have stopped saying the rest of it. You know the rest of it."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 10:00–11:59 | Ground floor counter | Morning lull. Slightly less dead. Prices identical. |
| 12:00–13:59 | Ground floor counter | Building. First space cake purchases of the day. |
| 14:00–17:59 | Ground floor counter | **Peak tourist hours.** Maximum crowds, longest waits, full "experience." |
| 18:00–19:59 | Ground floor counter | Afternoon's space cake victims now visible in the seating |
| 20:00–22:59 | Ground floor counter | Evening rush. Second wave. |
| 23:00–01:00 | Ground floor counter | Last call. Desperate purchases. Marieke discounts merchandise; Bas does not. |
| 01:00–10:00 | Closed | Legal operating hours, strictly enforced |

### Positioning Notes
- Behind the long wooden bar with the glass product display cases, ground floor, directly under the digital menu boards
- Green-tinted lighting on everything including him; the ventilation is decorative and the haze is permanent
- The branded ATM (5 Sovs fee) is in his sightline and he gestures at it without looking roughly forty times a shift
- Marieke works the T-shirt wall behind and to his right; the two of them are the shop's cold and hot upsell and neither coordinates with the other
- The Bob Marley poster (legally required in tourist coffeeshops) is directly above his head in every counter conversation

---

## 🎒 Inventory / Services

### Menu
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| "Shamsterdam Dream" (Tourist Rec) | 18 Sovs/g | ~9 Sovs/g elsewhere | +20 SP, −Speed, delayed Space Cake Effect. "Very popular. Very smooth." (scripted) |
| "Green Guide Special" (House) | 15 Sovs/g | ~8 Sovs/g elsewhere | +15 SP, +Confused. "House blend. Good choice." (automatic) |
| "Premium Heritage" | 25 Sovs/g | ~12 Sovs/g elsewhere | +30 SP, −Intelligence, +Bravado temporarily. "Excellent selection, sir." (upsell confirmed) |
| Space Cake (1 piece) | 8 Sovs | 8 Sovs | Delayed: +40 SP after 2 hours game time. Unlocks the "It's Not Working" dialogue chain. |
| Hash (1g) | 12 Sovs | 12 Sovs | +25 SP, "Heavy" (−Movement speed). *sigh* "For smoking. Not eating." |
| Bag | 2 Sovs | 0 Sovs | It is a bag. He has no further information about the bag. |
| VIP Lounge upstairs | 10 Sovs | 0 Sovs | Same room. Slightly nicer chairs. Different carpet. He is required to mention it. |

*(Merchandise — T-shirt 35 Sovs, branded grinder 45 Sovs, poster 20 Sovs — is Marieke's counter, not Bas's. He will not pitch it and does not receive commission.)*

### Status Effects Applied
| Effect | Source | Duration | Result |
|--------|--------|----------|--------|
| Tourist Trapped | First purchase | 1 hour | +15% prices at all other Shamsterdam vendors — you look like a mark |
| Contact High | Ambient, inside the shop | While inside | Mild Confusion, all party members |
| Space Cake Timer | Space cake purchase | 2 hours game time | Visible countdown; all effects land simultaneously |
| The Munchies | After SP boost wears off | Variable | Increases food purchase likelihood — feeds Leeman's, Kapsalon Koning, FEBO |

### Hidden Details / Easter Eggs
- **The Employee of the Month board**: Same photograph since 2019. It is not Bas. Examine it — the name plate is blank and has been unscrewed and re-screwed at least once.
- **The "secret menu"**: Unlocked at 3+ visits. It is the same items with different names, and Bas says so out loud while handing it over.
- **The ATM**: Branded with the shop's logo. Bas states it is not their machine. Both facts are true simultaneously and the game never resolves it.
- **The Polaroid wall**: Tourists making the same face since 1985. Examine it late-game and the player's own party is on it, in the corner, from their first visit.
- **The "How are you" pause**: Asking Bas how he is produces the longest pause in his dialogue set and a one-word answer. It is available from the first visit and almost nobody tries it.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Merchandise Maven Marieke | Same green polo, opposite temperature. She works on commission and he does not, and this is visible in the sprite silhouettes. They do not coordinate. |
| The Bouncer (unnamed by design) | Door, ID checks, and the entirety of Bas's escalation path. Bas looks at him; that is the whole mechanism. |
| Mehmet (Leeman's Döner Palace) | Munchies pipeline terminus. Mehmet identifies Bas's customers on sight and calls it "tourist eyes." |
| Big Wim (Kapsalon Koning) | The other munchies terminus. Receives Bas's customers about ninety minutes later, considerably worse. |
| Manager Ruben (Schrödinger's Souvenir) | Former coffeeshop worker who moved into "legal" hemp retail. Different shop, different corridor of the same tourist flow. They have never met on screen. |
| The Repeat Tourist | Claims to know Bas personally. Bas does not recognise him. This happens annually. |

### Territory / Social Dynamics
- Ground floor is Bas's; the merchandise wall is Marieke's; the door is the Bouncer's. Three staff, three zones, zero coordination, and the shop functions perfectly.
- The local ecosystem is pure tourist. Locals stopped coming years ago and Bas watches them walk past to smaller shops. He has never once mentioned this to a customer.
- Munchies pipeline: De Groene Gids → (90 minutes) → Leeman's / Kapsalon Koning / FEBO. Bas is the head of a supply chain he takes no part in.

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **First visit**: Scripted greeting, scripted recommendation, cash-only redirect, no-tobacco tutorial if earned, the two hours stated twice
- **The 2-hour chain**: The "It's Not Working" dialogue at 30/60/90/120 minutes — the location's centrepiece and Bas's flattest, best material
- **Third visit**: "Secret menu" unlocked, immediately explained to be identical
- **Post-local-coffeeshop**: The three-beat acknowledgement that ends with him restarting the required greeting
- **Late game**: He begins weighing before the player speaks and has stopped saying the second half of the script

### In Other Cities
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| — | — | Bas does not appear outside De Groene Gids. He is on the counter for the duration. | — |

### Evolution Through Game
Bas does not warm. He *shortens*. The scripted greeting compresses, the recommendation becomes a weight already on the scale, and the two-hour warning eventually goes unsaid because it has finally been learned. The endpoint — "I have stopped saying the rest of it. You know the rest of it." — is as close to a relationship as this building permits.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| bas_dead_eyed_stare | **Held frame. The default between all scripted beats.** The fan-art frame. | 52% |
| bas_idle (2 frames) | Minimal counter shift | 28% |
| scale_adjust | Zeroes the scale, waits | 12% |
| atm_gesture | Points at the branded ATM without looking at it | 8% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| bas_scripted_recommendation (3 frames) | Any recommendation request. "Shamsterdam Dream. Very smooth. Very popular." |
| bas_sigh (2 frames) | Precedes the no-tobacco explanation; also any hash-eating question |
| bas_no_tobacco_explanation (3 frames) | Tobacco mixing detected. Exhausted-teacher cadence, three beats. |
| bas_ringing_up | Transaction close. "Your total is sixty-three Sovs." |

### Sprite States
| State | When Used |
|-------|-----------|
| bas_counter | Default, ground floor |
| bas_dead_eyed | Held default between beats |
| bas_high_contrast | Accessibility outline variant marking him as interactive |

---

## 🎯 Quest Integration

### Primary Quest
None owned. Bas is a systems NPC running three interlocking mechanics.

### Systems Administered
1. **The Space Cake Timer.** Purchase starts a 2-hour game-time countdown with a visible UI counter. All delayed effects land simultaneously at expiry. Bas states the duration correctly at purchase and correctly at every subsequent enquiry.
2. **The "It's Not Working" dialogue chain.** Available at 30-minute intervals post-purchase. Four stages, escalating bro certainty, terminating in "OH." Bas's four responses get progressively shorter and he never once looks up.
3. **The Munchies pipeline.** When the SP boost wears off, The Munchies status fires and increases food purchase likelihood, driving traffic to Leeman's, Kapsalon Koning, and FEBO. Bas is the origin of a supply chain he has no stake in.

### Quest Gate Function
Bas gates nothing structurally and refuses nobody. He gates *information compliance*: the no-tobacco rule (enforced), the photography prohibition (enforced via the Bouncer), and the two-hour truth (stated, restated, and ignored). His only escalation is looking at the door.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Consumables (three strains, hash, space cake) | Any | Consumable | SP restore with varying debuffs |
| Tourist Trapped | First purchase | 1 hour | +15% prices at all other Shamsterdam vendors |
| The "secret menu" | 3+ visits | Yes | Identical items, different names, stated as such |

### State Flags Set
- `bas_met`: boolean
- `bas_visit_count`: integer (secret menu at 3)
- `bas_tobacco_attempted`: boolean
- `bas_photo_warned`: integer (2 = removed by Bouncer)
- `space_cake_purchased`: boolean
- `space_cake_timer`: integer (game-minutes remaining)
- `its_not_working_stage`: integer (0–4)
- `tourist_trapped_active`: boolean
- `bas_how_are_you_asked`: boolean

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. The Dead-Eyed Stare, full frame, no context needed
2. The Bob Marley poster directly above Bas's head during a transaction
3. The 63 Sovs total on screen beside a "would you like a bag, the bag is two Sovs" prompt
4. The Polaroid wall, late game, with the player's own party visible in the corner
5. The four-panel "It's Not Working" chain, 30 → 60 → 90 → 120 minutes

### Meme Potential
- "It. Is. Working. Wait."
- "Yes, it's expensive. We are famous. Famous things cost money. This is how famous works."
- "We do not do samples. This is not Costco."
- "The bag is two Sovs."
- "It has our name on it. It is not our machine."
- The Dead-Eyed Stare as a universal reaction image

---

## 🗣️ Voice Direction

### Accent
Dutch, young, urban, and entirely flat. Fluent English delivered without inflection, rhythm, or emphasis. He is not doing an accent bit — the accent is incidental and the monotone is the performance.

### Tone
- **Everything**: Flat monotone. This is stated in the location profile as direction and it holds for the whole part.
- **The required greeting**: The flattest thing in the game. There is no question in "how can I help you."
- **"Two. Hours."**: The only place he uses emphasis, and it is three separate full stops rather than volume.
- **The no-tobacco explanation**: Exhausted teacher, not security. He is explaining, not accusing.
- **"Fine."**: One word, after a long pause. The single crack. Do not widen it.

### Key Delivery Notes
- Never sarcastic. Bas has no irony available to him. Every line is the literal sentence.
- The sigh is a recorded audio asset that precedes and belongs to the no-tobacco line — do not separate them.
- He never argues about the price, never defends the shop, and never criticises it. He states.
- "This is not Costco" must be delivered as flat as everything else. It is the funniest line he has and it must not know that.

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

- **Every product statement Bas makes must be true.** The two hours are two hours. The descriptions on the menu are accurate. The strains do what he says they do. The satire is the markup and the brand, never deception — the instant Bas lies, the location's target shifts from tourist trap economics to fraud and the tone breaks.
- The Dead-Eyed Stare is the **held default between all scripted beats**, per the asset doc. It is not a reaction state. If it only appears on trigger, the character reads as moody rather than depleted.
- Bas and Marieke must be distinguishable by silhouette. She is the only staff sprite drawn with raised eyebrows — commission is the difference and it should be visible without colour.
- The "It's Not Working" chain is the location's centrepiece. Bas's four responses must get progressively shorter, and he must never look up. The bros' escalation carries the scene; Bas is the flat surface it bounces off.
- The 5 Sovs ATM contradiction (branded with the shop's logo, "not our machine") is authored and must never be resolved.
- Bas takes no merchandise commission and must never pitch a T-shirt. If he upsells, he becomes Marieke and the shop loses its cold pole.
- "Fine." after the long pause is his only interior moment. Do not build on it, do not follow it up, and do not add a second one.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Bas has none. Cash only, Sovs, with a 5 Sovs ATM fee that is not theirs.
- [x] **NO automatic crypto assumptions** — the location profile explicitly establishes cash-only and no blockchain; do not add any
- [x] **Coins, kiosks, and certificates come from the master pool** — N/A, no crypto at this location
- [x] **The bros are never scam-aware** — they will defend the 63 Sovs purchase and describe the shop as historic for the remainder of the game
- [x] **Nothing winks** — Bas states facts flatly and never signals that the pricing is absurd, because to him it simply is the pricing
- [x] **Focus on city-specific cultural exploitation instead** — the satire is brand tourism and paying for the sign rather than the product

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the joke is Americans who will not wait two hours and will not read a menu; Dutch coffeeshop culture and regulation are presented as sensible and Bas enforces them correctly
- [x] NPC is savvy entrepreneur, not villain or stereotype — Bas is not the owner and takes no cut; he is an accurate, rule-following employee in an overpriced building
- [x] Humour is affectionate mockery, not mean-spirited — Bas is never humiliated, never wrong, and never cruel; the shop is the target, the customers are the punchline, and he is the flat surface between them
- [x] Cannabis handled without moralising — the product is legal, regulated, correctly described, and the satire targets tourist behaviour and pricing, never use

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Shamsterdam/npcs/De_Groene_Gids/npc_budtender_bas.md`
- **Registered In**: No `de_groene_gids_npcs.json` exists. **A location JSON roster should be created** (Marieke, the Bouncer, and the four atmospheric customer NPCs still unprofiled — Wave 2). Registration pending; flagged for the JSON authoring pass.
- **Sprite Sheet**: `npc_groene_gids_cast.png` (1024×384, 64×96 sprites) — Row 0, positions (0,0) through (704,0). Specced in `PNG_Assets/De_Groene_Gids_PNG_Assets.md`, Sprite Sheet 5. Supporting: `groene_gids_ui.png` (space cake timer, Tourist Trapped status, cash-only prompt, "It's Not Working" dialogue availability), `digital_menu_board.png`, `branded_atm_machine.png`.

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — Wave 1 (mechanics-attached NPCs). Sourced from `de_groene_gids.md` + `PNG_Assets/De_Groene_Gids_PNG_Assets.md`. | Shamsterdam NPC authoring pass |

---

*Template Version 1.1*
