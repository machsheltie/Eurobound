# NPC Profile: Henk the Helpful (Unhelpful)

*"Strange, it was there yesterday."*

## 📋 NPC Identity
- **NPC ID**: `shamsterdam_npc_henk_security_01`
- **Display Name**: Henk
- **Internal Name**: Henk the Helpful (Unhelpful) Security Guard
- **Role**: Gatekeeper / Paid Misdirection / Service Provider (Escort) / Red Herring System
- **Associated Quest**: None directly. Gates the reliable-escort route into Zones 4–5; feeds the "Tour Guide" achievement by being the reason tourists need escorting.
- **Primary Location**: Voetgangerstunnel — Zone 2, The Intersection of Doubt, Shamsterdam
- **Secondary Appearances**: None above ground. Henk has not surfaced in years and this is not a figure of speech.

---

## 🎭 Core Concept

### What He's Actually Doing
Sitting in a booth at the point where five identical corridors meet, being paid to be present rather than to be useful. He answers every direction request in Dutch, points confidently, and is wrong roughly as often as chance would predict — because he genuinely does not know, and has never been given a reason to find out. His 5 Sovs "correct directions" tier is marginally better than free because he thinks slightly harder. His 10 Sovs escort is completely reliable, because walking you there requires no knowledge, only legs. He is not scamming anyone. He is doing exactly the job as it was described to him in 1997.

### What Bros Believe
An official. A uniform behind a desk at a decision point is, to Lord Pilsner, indistinguishable from authority. Chadwick films him for "local flavour." Bradley reads the 5 Sovs upgrade as a premium service tier and pays it without hesitation, because that is how tiers work.

### The Comedy Gap
The bros will pay a confident wrong man 5 Sovs rather than a correct musician 5 Sovs, and rather than reading the free green emergency signs that would solve the entire tunnel. Henk represents the tourist's fatal instinct: trust the uniform. The graffiti on the wall thirty metres away reads "DON'T FOLLOW HENK." They have walked past it four times. It is in English.

### The Detail Nobody Says Out Loud
Henk's escort works. Every time. 10 Sovs buys a guaranteed correct exit. He walks very slowly and the trip takes five real minutes and the bros complain the entire way — and it is, objectively, the best purchase available in the location. The one service he provides competently is the one they resent.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Mid-50s |
| Build | Seated-shaped. The chair and the man have negotiated a settlement. |
| Height | Average, though almost never verified |
| Energy | Fluorescent, load-bearing, entirely spent |

### Clothing
- **Security guard uniform, one size too tight**: Generic contract-security navy. The shirt has not been re-issued in some time and the buttons are doing structural work. Epaulettes with no insignia on them.
- **Clip-on tie**: Never actually clipped on straight
- **Accessories**: An empty coffee cup (always empty, never refilled, never removed); a newspaper folded to a crossword with four answers filled in
- **Footwear**: Standard-issue black shoes with soles worn only at the heel — the wear pattern of a man who pivots in a chair

### Distinguishing Features
- The eyes of someone who stopped caring in 1997, and can tell you it was 1997
- Points with the whole arm, fully extended, absolute conviction, random bearing
- Takes an extremely long time to stand up (4-frame animation, deliberately padded)
- Answers in Dutch regardless of the language he was addressed in, then repeats the same sentence in English with the same information

### Sprite Notes
Sheet `npc_henk_security.png` (192×256, 48×64 sprites, 4 rows). Row 2 — Pointing Confidently — is the character's entire thesis and should read from a distance as *helpful*. The comedy only lands if the pose is genuinely reassuring. Row 1 — Standing Slowly — must be padded to feel too long even at 1 FPS; the escort's value is undercut by how long it takes to begin. Henk should look like the surface is a rumour he has heard about.

---

## 🧠 Personality

### Archetype
**The Confidently Unhelpful Institution** — Henk is not lazy, malicious, or stupid. He is a man performing his job description with total accuracy: he is stationed at the intersection, and he is present at the intersection. Nobody ever wrote "and knows where the corridors go." He answers because it would be rude not to. He is wrong because nobody told him the right answer and it has never come up in a performance review.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Sincerely helpful | He wants to help. This is the problem. An unhelpful man would say "I don't know." |
| Institutionally confident | The uniform has convinced him along with everyone else |
| Language-indifferent | Dutch first, English second, same content, no adjustment |
| Untroubled by evidence | Told he was wrong, he says "Strange, it was there yesterday," and means it |
| Quietly competent when walking | The escort is flawless. He does not appear to notice this contradiction. |

### Internal Monologue
> "They come down the stairs and they look at five corridors and their faces go the same way every time, like a lift arriving. And they look for someone with a uniform, and I am the only uniform. So I point. Somebody has to point. If I say 'I don't know,' they stand there. If I point, they go. Movement is the job. That's what the man said in 1997 — 'keep it moving, Henk.' I keep it moving."

### Motivation
The shift ends at eight. Between now and eight, people should keep moving. That is the whole of it. Any hint of scheming, cynicism, or self-awareness breaks him.

---

## 💬 Dialogue

### Approach/Greeting

**First approach, player asks directions in English**:
> "Ah, Centraal Station? Ja, ja, die kant op." *(Points, full arm, random bearing.)* "Go that way."

**Player asks for a different destination**:
> "Museum Plein? Ja." *(Points in the same direction as before, without lowering his arm.)* "That way also."

**Player points out that both destinations cannot be the same direction**:
> "It is a tunnel. Everything is that way eventually."

### Key Interaction Dialogue

*Player returns after following his directions and reaching the wrong exit:*

**Henk** (mildly surprised, entirely unrepentant):
> "Strange, it was there yesterday."

*Player returns a second time:*
> "You again? Did you try the blue tiles? No? Try the orange ones."

*Player returns a third time:*
> "The blue and the orange both go to the station. One of them is faster. I have never checked which."

*Player asks about the Roodelicht Row exit:*
> "Oh, THAT exit." *(No change in expression.)* "Many tourists find that one. Very popular."

*Player asks how long he has worked down here:*
> "Since '97." *(Beat.)* "It was going to be temporary. It is still going to be temporary."

*Player asks if he has been outside recently:*
> "There is a staircase right there." *(Points, correctly for once, at the staircase, which is visible.)* "I know where THAT goes."

### Paid Service Dialogue

**5 Sovs — "Correct" Directions**:
> "Okay. For five Sovs, I give you the REAL directions."
> *(He puts down the crossword. This is the entire premium experience.)*
> "This way. Maybe."

**5 Sovs result, if the player then reaches the wrong exit**:
> "That is a refund question and I do not handle refunds."

**10 Sovs — Guided Walk (Escort)**:
> "For ten Sovs, I walk you there myself."
> *(He begins to stand. This takes a while.)*
> "But I walk slow. Very slow."

**During the escort**:
> *(Twenty seconds of walking.)* "Nice down here in the winter. Same temperature all year."
> *(Forty seconds.)* "That advert has been there since before the euro. I have read it perhaps nine thousand times. It is for a lawyer."
> *(At the correct exit.)* "There. Centraal Station." *(He is entirely right. He has been entirely right the whole way.)* "You want to go back? Another ten Sovs."

**Player asks why the escort works when the directions don't**:
> "Because I am walking with you." *(He does not consider this a paradox. He considers it obvious.)*

### Post-Interaction
> *(Returns to the booth. Sits. The standing-up animation is not reversed — sitting is fast. Picks up the crossword.)*

### If Player Declines / Alternative Path
**Player declines all paid options**:
> "Okay. Free directions are that way." *(Points at the free directions, which are a thing he says, not a place.)*

**Player mentions the graffiti**:
> "The wall says many things. The wall does not have a uniform."

**Player follows Willem's advice instead**:
> *(Henk does not react. He has never registered the accordion. Zone 3 is not his zone.)*

### Callback Dialogue (Return Visits)
**After 5 successful player navigations**:
> "You know where you are going now." *(A rare flicker of something.)* "You do not need me." *(Beat.)* "Escort is still ten Sovs."

**After the player buys Marloes's map**:
> "You have the map. Good. The map is very good." *(Pause.)* "I have never seen the map."

**Late game**:
> "Still down here? Ja. Me also."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 06:00–09:59 | Zone 2 booth | Seated. Rush-hour commuters pass without asking. Crossword: one answer added. |
| 10:00–13:59 | Zone 2 booth | Seated. Peak tourist arrivals. Maximum pointing. |
| 14:00–17:59 | Zone 2 booth | Seated. Escort purchases most common (afternoon desperation). |
| 18:00–19:59 | Zone 2 booth | Seated. Shift end approaching. Directions marginally faster, no more accurate. |
| 20:00–05:59 | Zone 2 booth | Still there. Nobody has ever seen the relief guard. |

### Positioning Notes
- Booth sits at the exact centre of the Intersection of Doubt, equidistant from all five corridors. He is the first thing the player sees at the decision point, which is the design intent and the design problem.
- His booth blocks a clean sightline down two of the five corridors, which the player will not notice and which matters
- The "DON'T FOLLOW HENK" graffiti is thirty metres away in Zone 3, flashlight-gated. He has never been down there to see it.
- Escort pathing must use the true tunnel graph, not the probability resolver — the escort is a hard-coded correct route

---

## 🎒 Inventory / Services

### Services Offered
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Directions | Free | Approximately zero | Random corridor pointed at with total conviction. No accuracy bonus. |
| "Correct" Directions | 5 Sovs | Approximately 0.50 Sovs | +10% navigation accuracy this decision. Still likely wrong. |
| Guided Walk (Escort) | 10 Sovs | 10 Sovs, honestly | **Guaranteed correct exit.** Bypasses the probability resolver entirely. Costs 5 minutes real time. |
| Conversation | Free | Genuinely pleasant | Three lore lines about the tunnel's construction and the pre-euro adverts |

### Hidden Details / Easter Eggs
- **The crossword**: Examine it across multiple visits. Four answers filled in on visit one; four answers filled in on visit forty. Two of the four are wrong. The newspaper is dated but the date is illegible.
- **The empty cup**: Examine text reads "Empty." Every time. There is no coffee anywhere in the tunnel and no vending machine in Zone 2.
- **Escort economics**: A player who buys the escort every visit spends less than a player who buys the 5 Sovs directions and fails twice. Nobody in-world points this out.
- **The Dutch line**: Henk's Dutch and English lines carry identical information. Players who speak Dutch get no advantage. This is deliberate and mildly infuriating, which is correct.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Marloes (Map Vendor, Zone 1) | She sells the accurate map. He has never seen it. She has stopped bringing it up. |
| Willem the Eternal Busker (Zone 3) | Mutual, total, decades-long non-acknowledgement. Neither has ever referenced the other. |
| The Lost Tourists | His primary output. Every Lost Tourist variant has a dialogue line referencing following the orange tiles back to him. |
| Mevrouw Jansen (Roodelicht exit) | She receives the people he misdirects. They have never met. |
| The Bike Rental Guy (Bike Crossing kiosk) | Same municipal warning-sign energy, opposite competence. The 15 Sovs tunnel access he sells routes tourists directly into Henk's intersection. |

### Territory / Social Dynamics
- Zone 2 is Henk's, absolutely and unchallenged, and it is the zone with the most player traffic and the least useful information
- The tunnel's information economy in one line: Marloes charges 8 Sovs for the truth, Willem gives it for 5 Sovs, Henk charges 5 Sovs for a coin flip and 10 Sovs for a certainty he doesn't realise he's selling
- The graffiti artist who wrote "DON'T FOLLOW HENK" and "Willem knows" is the tunnel's only editorial voice and Henk will never read either

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **Visit 1**: Authority figure. Player asks. Player is misdirected. Foundational.
- **Visits 2–3**: Player begins to suspect. The "Strange, it was there yesterday" line lands on visit 2 and is the pivot.
- **Visit 4+**: Player either buys the escort (correct) or bypasses him entirely (also correct). Either way he is still sitting there.
- **After the flashlight purchase**: The graffiti recontextualises every prior interaction retroactively

### In Other Cities
None. Henk does not appear above ground, in other districts, or in other cities. He is a fixture of the intersection in the strictest sense.

### Evolution Through Game
Henk does not develop. His single acknowledgement of player growth — "You do not need me. Escort is still ten Sovs." — is the whole arc and it is delivered flat. He was here before the bros and he will be here after. The player changes; Henk does not.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| sitting_bored | 2 frames, 0.25 FPS. Barely-perceptible weight shift. | 78% |
| crossword_glance | Looks at the newspaper, does not write | 12% |
| cup_lift_empty | Raises the empty cup, sets it down, no reaction | 10% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| pointing_confidently | 3 frames, 1 FPS. Any directions request, free or paid. Full-arm extension. |
| shrugging | 2 frames, 1 FPS. "Strange, it was there yesterday." |
| standing_slowly | 4 frames, 1 FPS, padded. Escort purchase. Deliberately too long. |
| slow_walking | 4 frames, 1 FPS, loop. Escort in progress. |

### Sprite States
| State | When Used |
|-------|-----------|
| henk_seated | Default. Approximately all of the time. |
| henk_standing | Escort only |
| henk_high_contrast | Accessibility outline variant marking him as interactive |

---

## 🎯 Quest Integration

### Primary Quest
None owned. Henk is a service node and a systems gate.

### Quest Gate Function
Henk gates the **guaranteed-success route** through the tunnel. Every other path — Marloes's map (+15%), Willem's hints, the emergency-sign secret, accumulated memory (+5%/success) — is probabilistic. Henk's 10 Sovs escort is the only deterministic correct exit in the Voetgangerstunnel, and it is sold by the least trustworthy person in it. He gates nothing by refusal; he gates by being the answer nobody wants.

Secondary gate function: the **Tour Guide achievement** (escort a Lost Tourist to the correct exit) exists because Henk keeps producing Lost Tourists. The player becomes the competent Henk.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| "Correct" Directions (verbal) | Any | No | +10% navigation, current decision |
| Guided Walk | Any | No | Guaranteed correct exit; 5 minutes real time |
| Tunnel construction lore (3 lines) | Free conversation | No | Flavour; one line references the 1973 exit that was never re-signed |

### State Flags Set
- `henk_met`: boolean
- `henk_misdirections`: integer (wrong exits reached after taking his free advice — used for the escalating "You again?" ladder)
- `henk_paid_directions_count`: integer
- `henk_escort_purchased`: boolean
- `henk_escort_count`: integer
- `henk_graffiti_seen`: boolean (player has flashlight-revealed "DON'T FOLLOW HENK")

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. Henk pointing with total conviction, "DON'T FOLLOW HENK" graffiti visible on the same wall
2. The wall map's wrong "You Are Here" dot and Henk's booth in the same frame — two municipal failures, one composition
3. The escort walk: player, Henk, eighty metres of empty corridor, 1 FPS
4. Examining the empty coffee cup on visit forty
5. "Strange, it was there yesterday" delivered with no change of expression whatsoever

### Meme Potential
- "Strange, it was there yesterday."
- "Did you try the blue tiles? No? Try the orange ones."
- "It is a tunnel. Everything is that way eventually."
- "Because I am walking with you." — the escort paradox, deployed as a reply format
- "Since '97. It was going to be temporary. It is still going to be temporary."

---

## 🗣️ Voice Direction

### Accent
Dutch, urban, flat. Not warm, not cold. The vocal equivalent of a laminated notice. He is not performing officiousness — he genuinely has one register and it is "public information announcement."

### Tone
- **Free directions**: Total confidence. Zero hesitation. This is the load-bearing performance.
- **"Strange, it was there yesterday"**: Mild curiosity, immediately dropped. He is not embarrassed. He is not defensive. He has simply moved on.
- **Escort**: Slightly warmer. He is doing a thing he can actually do and something in the delivery knows it, without ever saying so.
- **The '97 line**: Absolutely no self-pity. It is a fact about a year, delivered like a fact about a year.

### Key Delivery Notes
- Never sardonic. Never knowing. The second Henk sounds like he's in on the joke, the character dies.
- Dutch lines and English lines are the same information — deliver both at the same speed, with no "let me try again in English" energy
- The pointing is the punchline; the line reading should be so unremarkable that the visual carries it
- Do not have him apologise. He has nothing to apologise for. He pointed. They went.

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

- **The escort must be 100% reliable.** It is the location's pressure-release valve and the character's single joke. If the escort ever fails, Henk becomes a scammer and the satire inverts onto the wrong target.
- Free directions must use a genuine random roll across the five corridors, not a weighted-wrong roll. Henk is not sabotaging anyone; he is guessing. Players who datamine should find a flat distribution.
- The 5 Sovs tier's +10% is deliberately close to worthless. Do not buff it. The joke is that the premium tier is premium in name only, while the 10 Sovs tier is the real product.
- "DON'T FOLLOW HENK" graffiti is flashlight-gated (Marloes, 6 Sovs). The full comedy chain is: buy the flashlight from the honest vendor → read the wall → realise you have been paying the wrong man for three visits.
- Henk and Willem must never share a line of dialogue or a reference. Their mutual non-acknowledgement is a background gag with no punchline, which is what makes it work.
- Do NOT name him Willem, Wim, or any variant. Canon: one first name, one character. Henk here; the FEBO Automat kitchen worker is the other Henk and is a separate, already-registered character — if they are ever placed in a scene together, that collision needs resolving before shipping.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Henk has none. 5 Sovs and 10 Sovs, cash, in a tunnel.
- [x] **NO automatic crypto assumptions** — a contract security guard on a 1997 job description does not take SOVS
- [x] **Coins, kiosks, and certificates come from the master pool** — N/A, no crypto at this location
- [x] **The bros are never scam-aware** — Bradley reads the 5 Sovs tier as a legitimate service upgrade and will defend this position
- [x] **Nothing winks** — Henk never hints he might be wrong; the graffiti does the winking, and the graffiti is an object, not a character
- [x] **Focus on city-specific cultural exploitation instead** — the satire is the tourist reflex to trust a uniform over a wall, a map, or a musician

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the joke is the bros' authority-worship, not Dutch civil service
- [x] NPC is savvy entrepreneur, not villain or stereotype — Henk is neither; he is an honest man in a job with no accuracy requirement, and his one competent service is fairly priced and delivered in full
- [x] Humour is affectionate mockery, not mean-spirited — he is never humiliated, never punished, and is quietly right about the escort

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Shamsterdam/npcs/Voetgangerstunnel/npc_henk_helpful_unhelpful.md`
- **Registered In**: `voetgangerstunnel_npcs.json` — Yes. Pre-existing entry `shamsterdam_npc_henk_security_01` (display_name shortened to "Henk" in JSON vs. full title in the location profile — JSON short form retained); `full_profile` path added in this pass.
- **Sprite Sheet**: `npc_henk_security.png` (192×256, 48×64 sprites, 4 animation rows) — specced in `PNG_Assets/voetgangerstunnel_png_assets.md`, Sprite Sheet 2. Supporting: `voetgangerstunnel_tileset.png` (Security Booth, Row 4–5, 2 tiles).

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — Wave 1 (mechanics-attached NPCs). Sourced from `voetgangerstunnel.md` + `PNG_Assets/voetgangerstunnel_png_assets.md` + `voetgangerstunnel_npcs.json`. | Shamsterdam NPC authoring pass |

---

*Template Version 1.1*
