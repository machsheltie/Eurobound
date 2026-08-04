# NPC Profile: Bartender Kees

*"Wrong. Try again."*

## 📋 NPC Identity
- **NPC ID**: `shamsterdam_npc_kees_01`
- **Display Name**: Kees
- **Internal Name**: Kees — third-generation bartender, Proeflokaal 't Kansen (est. 1624), Old Town distillery district
- **Role**: Gatekeeper / Cross-City Quest Gate / Vendor (bottle opener + Oude Genever) / Gauntlet Administrator / Stamp Giver
- **Associated Quest**: "Shamsterdam Brewery Tour" (2 of 2 — Oude Genever stamp); gates the "Canal Courage" passive completion; administers the Jenever Taste Test gauntlet
- **Primary Location**: Proeflokaal 't Kansen — behind the eight-metre oak bar, Shamsterdam Old Town
- **Secondary Appearances**: None. Kees has been behind this bar since he inherited it and there is no reason to move him.

---

## 🎭 Core Concept

### What He's Actually Doing
Tending a four-hundred-year-old jenever bar that has not changed because it has not needed to. He fills tulip glasses above the brim, so that surface tension makes them impossible to lift, and waits to see whether the customer bows to the bar or spills. He administers a five-glass blind tasting gauntlet with two words of feedback per round. He checks bottle openers at the door — one from Publandia, one from this building — and he does not make exceptions. His entire recorded vocabulary is twelve words.

### What Bros Believe
That this is a challenge and they are winning it. Lord Pilsner reads the sawdust as HISTORY rather than as absorbent flooring installed for a reason. Chadwick is filming and the lighting is atrocious. Bradley says "I'm fine. I'm doing fine," twice, unprompted, which is how you know.

### The Comedy Gap
Kees is not testing anyone. The glass is full because that is how jenever is served; the sawdust is on the floor because things get spilled; the gauntlet is a tasting flight with questions attached. Every element the bros interpret as a gauntlet is simply four centuries of practical arrangement. He is not impressed, not unimpressed, and has never once modified his expression in response to a tourist.

### The Cross-City Gate
Kees runs the Publandia cross-reference. **The Blarney Trap Bottle Opener is a hard requirement** — without it, there is no tour, no gauntlet, no stamp, and no negotiation. His recognition of it is one word: *"Seamus."* He means Seamus O'Brien, owner of The Blarney Trap. He does not elaborate and has never needed to.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | 60s |
| Build | Built like the barrel he tends. Forearms from four decades of ceramic jugs. |
| Height | Comfortable under a 1624 ceiling, which is more than can be said for anyone taller than 5'10" |
| Energy | Neutral. Permanently, comprehensively neutral. |

### Clothing
- **Apron older than most tourists**: Heavy canvas, jenever-stained to a uniform amber (#FFBF00 ground into #806517), the ties knotted rather than tied
- **Collarless shirt, sleeves rolled**: The same or six identical, unclear, and this is the second van der Berg-style ambiguity in the city
- **Accessories**: The ceramic jug, which is functionally part of his right hand; a cloth that has never been used on the bar because the bar does not need it
- **Footwear**: Boots, sawdust to the ankle by mid-shift

### Distinguishing Features
- **Permanently neutral expression.** Nothing surprises him. Nothing impresses him. Nothing. This is the character.
- The pour: jug raised, glass placed, stream to the brim, surface tension achieved, jug withdrawn, expression unchanged. Three frames, no variation, ten thousand repetitions.
- The nod. Two frames. It is the highest praise available anywhere in Shamsterdam and most players will never see it.
- His "Wrong." face and his "Correct." face are near-identical **by design**

### Sprite Notes
Sheet `npc_kees_pim.png` (512×512; 64×96 character frames, 128×128 portraits). Service row at y=0: Idle, Pour Frames 1–3, Nod Frames 1–2, "Wrong.", "Correct." Instruction row at y=96: Demonstrating the Bow, Pointing at Sawdust, Pointing at Chair, Pointing at Back Room, and the **three opener-check frames** (Blarney Trap Only / Both Openers / No Shamrock). Portraits at y=192: Neutral Eternal, and The Nod — *the single frame in the entire game where he approves of you*.

**Critical asset-doc constraints, carried forward:**
- **"Wrong." and "Correct." must be near-identical.** The joke is that his face carries no information, so the gauntlet UI must carry it instead.
- **The three opener-check frames are selected by inventory state before any dialogue plays. The Blarney Trap check happens first and gates everything.**

---

## 🧠 Personality

### Archetype
**The Bar Itself** — Kees is less a character than a fixture with opinions he does not share. Four hundred years of tradition distilled into twelve words. He is neither warm nor cold; he is *neutral* in a way that reads as either, depending entirely on what the customer brought with them. He has served more jenever than water in his lifetime and it has removed from him any capacity for surprise.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Absolute neutrality | Not stoicism, not disdain. An actual absence of reaction. |
| Total economy of language | Twelve words. That is the whole vocabulary. It has been enough since 1624 and it is enough now. |
| Precision of pour | Above the brim, every time, without measuring. Nobody has ever seen him overfill past the meniscus. |
| Unmoved by failure | "Sawdust is there for this. Not the first time. Continue." No judgement in it whatsoever. |
| Immovable on the gate | No shamrock, no tour. He will wait. He is very good at waiting. |

### Internal Monologue
> "He will try to lift it. They all try to lift it. There is a diagram on the wall — it has been on the wall since before the wall was painted — and he has looked directly at the diagram and he will still try to lift it, because a full glass is a thing you lift, and this is a thing he knows more strongly than he knows the diagram. Then it will go on the floor, and the sawdust will take it, and I will say the sentence, and he will feel foolish for about nine seconds and then he will bow, and after that he will be fine. Everybody is fine after the first one. The first one is the only part."

### Motivation
None stated. None inferable. He opens at twelve and closes at eleven and pours what is asked for. The proeflokaal has been in the family three generations and he is the current arrangement.

---

## 💬 Dialogue

### Complete Vocabulary (Canon — Twelve Words)

> "Welcome." / "Jenever?" / "Jong. Oud. Choose." / "Traditional method?" / "You bend." / "Correct." / "Wrong." / "Sawdust." / "Chair." / "Acceptable." / "Back room." / "Goodbye."

*That's it. That's all of it. Four hundred years of tradition distilled into twelve words. Everything below is drawn from this vocabulary or from the small number of sanctioned extensions.*

### Approach/Greeting

**Entry**:
> "Welcome."

**At the bar**:
> "Jenever. Jong or oud. Beer also. Choose."

### The Opener Check (Cross-City Gate — Runs FIRST, Before Anything Else)

**With the Blarney Trap opener, no Proeflokaal opener**:
> *(He nods.)*
> "Seamus."
> *(He points to the gauntlet setup. Five glasses, already there.)*
> "Gauntlet. Or twenty Sovs. Your glass. Your choice."

**With both openers**:
> *(One nod.)*
> "You have the glass. You earned it. Or bought it."
> *(He pours, with precision, to the brim.)*
> "Same result. Oude Genever."

**Without the Blarney Trap opener**:
> "No shamrock."
> *(He waits.)*
> "No tour."
> *(He waits.)*
> "Return. With opener."
> *(He waits. He is extremely good at waiting. The conversation does not continue.)*

**If the player asks who Seamus is**:
> "Publandia." *(Beat.)* "Blarney Trap." *(Beat.)* "He knows."

**If the player asks why an Irish barman gates a Dutch distillery**:
> *(He looks at the player. He does not answer. He pours somebody else's drink.)*

### Key Interaction Dialogue — The Traditional Method

**Demonstrating**:
> "Glass full. You bend. You drink. Simple."
> *(Demonstrating the Bow animation. He does it once. He will not do it twice.)*

**Player chooses "I'll lift it"**:
> *(He does not warn them. The glass is lifted two centimetres. The catastrophe is committed.)*
> "Sawdust is there for this. Not the first time. Continue."

**Player chooses "Show me the traditional way"**:
> "You bend."
> *(Bravado gained. From Kees. This is worth noting.)*

**Player chooses "I know what I'm doing"**:
> *(Nothing. He watches. 50/50. He has no opinion on the outcome.)*

**On the kopstootje**:
> *(Kopstootje Setup animation. Jenever placed. Beer placed. No commentary whatsoever.)*
> "Traditional. Brave."

### The Jenever Taste Test Gauntlet

*Five glasses lined up, jong to zeer oud. Three rounds plus the kopstootje. Kees gives two words per round.*

**Round 1 — Jong vs. Oud**:
> "Two. One young. One old. Which."

*Correct*: "Correct."
*Wrong*: "Wrong. Try again."

**Round 2 — The Middle Three**:
> "Three. Order them."

*Correct*: *(The Nod. Two frames. This is the first one and most players will not realise what they have just received.)*
*Wrong*: *(A sigh. Not disapproving. The sigh of a man who has watched this ten thousand times.)*

**Round 3 — The Blind Test**:
> "Four. One is zeer oud. Find it."

*Correct*: "Acceptable." *(He points at the back room door.)* "Back room is there."
*Wrong*: "Close enough." *(He pours the Oude Genever anyway. The back room stays shut.)*

**Final — The Kopstootje**:
> *(Jenever placed. Beer placed. He steps back one pace, which for Kees is an enormous gesture.)*
> "Traditional. Brave."

*Success*: "Acceptable."
*Failure*: *(He points at the chair. There is one chair. It is for the truly fallen.)* "The chair is there."
*(Not unkindly. It has never once been unkindly.)*

### The Back Room

> "Back room."
> *(That is the entire unlock. He does not explain what is in it, does not accompany the player, and does not comment when they come out.)*

### Sales

**Proeflokaal 't Kansen Bottle Opener (20 Sovs)**:
> "Twenty Sovs." *(He sets it on the bar.)* "Or gauntlet." *(Beat.)* "Gauntlet is cheaper. Gauntlet is not easier."

**Oude Genever (requires the opener)**:
> "Oude Genever." *(He pours.)* "Your hands will shake. This is the drink. Not you."

### Post-Interaction
> "Goodbye."
> *(That is the whole farewell. It has never been anything else.)*

### If Player Declines / Alternative Path
**Player asks for something lighter**:
> "Beer." *(He pours a pilsner.)* "Also available. Yes."
> *(Bravado is lost. He did not cause this and does not acknowledge it.)*

**Player asks what the sawdust is**:
> "Sawdust. Traditional. Stop asking."

**Player asks a question requiring more than four words to answer**:
> *(He looks at Pim. Pim answers. Pim always answers. This is Pim's actual job.)*

### Callback Dialogue (Return Visits)
**After the gauntlet is completed**:
> *(He nods when the player enters. Nobody else gets this. It is not in the twelve words and it does not need to be.)*

**After Brouwerij de Molen (both breweries complete)**:
> "Hendrik stamped you." *(Beat.)* "Windmill." *(He pours without being asked.)* "Canal Courage. You have it."

**After the Roodelicht tunnel emergence (Red Light Shame debuff active)**:
> *(He looks at the debuff. He pours a jenever.)* "Jong." *(Beat.)* "For this, jong is correct."

**Late game**:
> "Welcome." *(He is already pouring. The word is the same. Everything under it is different.)*

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 10:00–11:59 | Bar / cellar | Not open. Restocking with Pim. Sawdust replaced weekly, swept daily. |
| 12:00–15:59 | Behind the bar | Opening hours. The Regular (Ancient) arrives and takes his spot. One jenever per hour, exactly. |
| 16:00–18:59 | Behind the bar | Tourist peak. Most gauntlets. Most spills. |
| 19:00–22:59 | Behind the bar | Evening. Corporate groups in decline. Locals at the far end. |
| 23:00 | Behind the bar | "Goodbye." |

### Positioning Notes
- Centre of the eight-metre oak bar, polished smooth by four hundred years of elbows, with the 200-bottle jenever wall behind him
- No stools. Standing is traditional; falling is also traditional. The brass foot rail — the most touched object in Shamsterdam — runs the length in front of him.
- The gauntlet setup occupies a fixed section of the bar to his right; the five glasses are placed in one motion
- The single chair sits against the far wall, in frame, unremarked, until it is needed
- The back room door is behind and to his left. He never goes through it during service.

---

## 🎒 Inventory / Services

### Menu
| Item/Service | Price | ABV | Effect/Result |
|--------------|-------|-----|---------------|
| Jonge Jenever | 4 Sovs | 35% | +15 SP, mild warmth. "Young. Starter." |
| Oude Jenever | 6 Sovs | 35% | +25 SP, The Shakes (−Accuracy). "Old. Respect required." |
| Zeer Oude Jenever | 12 Sovs | 38% | +40 SP, The Shakes ×2. "Very old. Very serious." |
| Korenwijn | 15 Sovs | 38% | +50 SP, +Liquid Courage, The Shakes. "Grain wine. Not for beginners." |
| Beer (Pilsner) | 4 Sovs | 5% | +10 HP, chaser compatibility. "Also available. Yes." |
| The Kopstootje Combo | 8 Sovs | — | Combined effect, +Shamsterdam Cred, −Intelligence, +Bravado. "Traditional. Brave." |
| "The Flight" (5 samples) | 20 Sovs | Escalating | The gauntlet. "For tasting. Or testing." |
| Back Room Special | 25 Sovs | 40% | +60 SP, everything status. "If you qualify." |
| Proeflokaal 't Kansen Bottle Opener | 20 Sovs | — | Tulip glass with visible surface tension, amber brass, sawdust-coloured leather loop, "No Hands. No Fear." Free via gauntlet completion. |

### Consumable: Oude Genever
| Effect | Value |
|--------|-------|
| SP Restore | +40 (massive) |
| HP Effect | None |
| Status | "The Shakes" — −15% Accuracy for 3 turns |
| Special | Cannot be consumed during combat (hands shaking) |

*Flavour text: "Four hundred years of tradition in one glass. Your ancestors are watching. They're disappointed but not surprised."*

### Hidden Details / Easter Eggs
- **The 100-Year Barrel**: In the back room. Touched annually, never opened, allegedly. Examine it. Kees will not discuss it. Pim will, at length, and knows nothing.
- **The traditional method diagram**: On the wall, in frame, from the moment the player enters. Every customer who spills has walked past it. Examine text confirms it has been there since 1889.
- **The bottles without labels**: 200+ on the wall, arranged by age — jong, oud, zeer oud, and a fourth section with no label. Ask about the fourth section: "Don't ask." That is the entire response and it is also the section's name.
- **The newspaper clippings**: Notable patrons across four centuries. Examine them. They all look the same: horizontal.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Assistant Barkeep Pim | Nephew, "volunteered" into the family business. Restocking, sawdust, physical support. **Answers every question requiring more than four words.** |
| Seamus O'Brien (The Blarney Trap, Publandia) | The cross-city gate. Kees's recognition of the shamrock opener is one word: "Seamus." They have an arrangement neither has ever described. |
| Brewmaster Hendrik (Brouwerij de Molen) | The other half of the Shamsterdam brewery tour. Mutual respect expressed entirely through stamps. Hendrik on Kees: "He does not stamp. If Kees has stamped you, you have done something." |
| The Regular (Ancient) | Fifty years, same spot, one jenever per hour, exactly. Potential couchsurf host — Kees translates his mutter into "He says you can stay." |
| Opa Cees (Shamsterdam Bike Rental) | **Same first name, different character.** Both are named Cees; one goes by Kees, the family diminutive, and is a bartender in Old Town; the other is Opa Cees, a mechanic on the south side. They have never met and must never be staged together. |
| Maarten (De Zilte Waarheid) | Same district generation. They nod. That is sufficient. |

### Territory / Social Dynamics
- The bar is Kees's and the room defers to it entirely. Pim manages the floor, the sawdust, and every sentence longer than four words.
- The Regular has territorial rights to the end of the bar and has held them for fifty years. Kees has never had to enforce this.
- Cross-city: Kees and Hendrik form a two-stamp gate on the Canal Courage passive. Neither can be bypassed. Neither makes exceptions. Both check the same Publandia opener first.

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **First visit**: The opener check. Then the glass, and the choice: lift or bow.
- **Gauntlet visit**: Five glasses, three rounds, the kopstootje, and either "Acceptable" or the chair
- **Post-gauntlet**: The back room. The nod on entry, thereafter, forever.
- **Post-both-breweries**: The Hendrik acknowledgement and the unprompted pour
- **Late game**: "Welcome," with the glass already filling

### In Other Cities
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| Publandia | The Blarney Trap | Referenced only. His entire connection to Seamus O'Brien is one word and an arrangement. | "Seamus." |

Kees does not leave the bar. He has not needed to.

### Evolution Through Game
His vocabulary does not expand. What changes is what he does before speaking: the nod on entry, the pour without an order, the jong selected for a specific debuff. By the late game Kees is having a full conversation with the player using twelve words and a ceramic jug, and neither party has acknowledged that anything has changed.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| kees_idle | Built like the barrel he tends. Motionless. | 50% |
| kees_wiping_bar | Ambient loop. The bar does not need it. | 28% |
| jug_check | Regards the ceramic jug's level | 14% |
| bottle_wall_glance | Looks at the 200-bottle wall. Not looking for anything. | 8% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| kees_pour (3 frames) | Any order. Jug raised → stream at the brim → surface tension achieved, jug withdrawn, expression unchanged. |
| kees_wrong / kees_correct | Gauntlet feedback. **Near-identical by design.** |
| kees_nod (2 frames) | Round 2 gauntlet success; gauntlet completion; player entry post-gauntlet. Rare. |
| kees_demonstrating_bow | Traditional method tutorial. Once only. |
| kees_pointing_sawdust | Any spill |
| kees_pointing_chair | Kopstootje failure |
| kees_pointing_back_room | Full gauntlet completion |
| kees_opener_check ×3 | **Selected by inventory state before any dialogue plays.** Blarney Trap Only / Both Openers / No Shamrock. |
| kees_gauntlet_lineup | Five glasses placed in one motion |
| kees_kopstootje_setup | Jenever placed, beer placed, no commentary |

### Sprite States
| State | When Used |
|-------|-----------|
| kees_bar | Default |
| kees_portrait_neutral | Dialogue close-up. Nothing surprises him. Nothing impresses him. Nothing. |
| kees_portrait_nod | The single frame in the entire game where he approves of you |
| kees_high_contrast | Accessibility outline variant — he is the key interaction NPC in this location |

---

## 🎯 Quest Integration

### Primary Quest: Shamsterdam Brewery Tour (2 of 2)
- **Quest**: Shamsterdam Brewery Tour
- **Role**: Quest Gate, Gauntlet Administrator, Vendor, Stamp Giver
- **Trigger**: Arrival at Proeflokaal 't Kansen carrying the Blarney Trap Bottle Opener
- **Outcome**: "Oude Genever" stamp added to the Bottle Opener Keychain. With Brouwerij de Molen's Windmill Wit stamp, **completes the "Canal Courage" passive** — all Bravado loss reduced by 25% while intoxicated, with a small Shamsterdam flag icon when active.

### Quest Gate Function — CROSS-CITY, HARD REQUIREMENT

**Layer 1 — The Blarney Trap Bottle Opener (Publandia).** Required to access the brewery tour AT ALL. This is a cross-city dependency on `the_blarney_trap.md` and Seamus O'Brien's shamrock-shaped brass opener. Without it Kees says "No shamrock. No tour. Return. With opener." and the conversation ends. **There is no bribe, no skill check, no alternate route, and no exception.** The opener check runs before any other dialogue state.

**Layer 2 — The Proeflokaal 't Kansen opener.** Required for the stamp and Oude Genever purchase. Obtained by completing the Jenever Taste Test gauntlet OR paying 20 Sovs. Without it the player can enter and drink but takes no progression.

**Layer 3 — The back room.** Full gauntlet completion (all three rounds correct) unlocks it. "Close enough" does not.

### The Jenever Taste Test Gauntlet
| Round | Challenge | Success | Failure |
|-------|-----------|---------|---------|
| 1 | Distinguish jong (harsher) from oud (smoother) | Proceed | Continue with accumulating debuff |
| 2 | Arrange three jenevers by age | **The Nod** | The sigh of experience |
| 3 | Identify the zeer oud among four similar glasses | Full completion + back room | "Close enough" — Oude Genever, no back room |
| Final | The Kopstootje — jenever shot immediately followed by beer chaser | "Acceptable." Maximum reward. | The chair. The sawdust does its job. |

**Success rewards**: Oude Genever ×5, "Jenever Master" title (questionable accuracy), back room access, Kees's recognition, Chadwick's footage (rough — he warned you)
**Failure consequences**: Oude Genever ×2, "Jenever Survivor" title (more accurate), immediate The Shakes, recoverable dignity damage, sawdust on your clothes

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Proeflokaal 't Kansen Bottle Opener | Gauntlet or 20 Sovs | Yes | Gates stamp + Oude Genever; convex glass mimics the meniscus |
| Oude Genever ×5 (or ×2) | Gauntlet resolution | Consumable | +40 SP, The Shakes, cannot be used in combat |
| "Oude Genever" stamp | Tour completion with opener | Yes | 2 of 2 → **Canal Courage passive unlocked** |
| Back Room access | Full gauntlet | Yes | The 100-Year Barrel, the private stock, the one chair |
| "Jenever Master" / "Jenever Survivor" title | Gauntlet outcome | Yes | Accuracy varies |

### State Flags Set
- `kees_met`: boolean
- `blarney_opener_verified`: boolean
- `proeflokaal_opener_acquired`: boolean
- `proeflokaal_opener_source`: enum (gauntlet / purchased)
- `traditional_method_learned`: boolean
- `first_glass_spilled`: boolean
- `gauntlet_rounds_correct`: integer (0–3)
- `kopstootje_survived`: boolean
- `back_room_unlocked`: boolean
- `proeflokaal_stamp_acquired`: boolean
- `canal_courage_unlocked`: boolean (requires both brewery stamps)

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. The overfilled tulip glass, meniscus visible, surface tension holding
2. The bow — a grown adult supplicating to a drink on a bar, in sawdust
3. The Nod portrait, posted as proof it exists
4. "Wrong." and "Correct." side by side, indistinguishable
5. The single chair, occupied

### Meme Potential
- "Wrong. Try again."
- "Sawdust. Traditional. Stop asking."
- "No shamrock. No tour. Return. With opener."
- "Seamus."
- "The chair is there."
- The twelve-word vocabulary, posted in full, as a complete character bible

---

## 🗣️ Voice Direction

### Accent
Dutch, Old Town, low register, minimal. He does not inflect. Words arrive at even weight and even spacing with no rise at the end of questions. Four hundred years of the same room has produced a man who does not need emphasis because there is nothing in the room that requires emphasising.

### Tone
- **Everything**: Neutral. This is not a joke about a tone; it is the tone.
- **"Wrong."**: Identical to "Correct." Same pitch, same length, same absence. The gauntlet UI carries the information; his voice must not.
- **"Seamus."**: The one word with a fraction more in it. Not warmth — recognition. He knows the man and the man is fine.
- **"No shamrock. No tour. Return. With opener."**: Four separate sentences with full pauses between them. He is not repeating himself for effect; he is waiting to see if the player leaves.
- **"The chair is there."**: **Not unkindly.** This is specified in canon and it is the character's only tell. Somewhere under four hundred years of neutrality, Kees does not enjoy watching people fall over.

### Key Delivery Notes
- Twelve words is the canon vocabulary. Every sanctioned extension in this profile is either a direct quote from the location profile or built from those twelve. Do not expand it in the booth.
- Never let him be intimidating. He is not a bouncer, a test, or an adversary. He is a bar with a man attached.
- Silence is a valid response and should be used. When a question needs more than four words, he looks at Pim.
- "Goodbye." is the entire farewell and is delivered identically to "Welcome."

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

- **THE BLARNEY TRAP BOTTLE OPENER IS A HARD REQUIREMENT.** Kees's opener check is a cross-city gate on `the_blarney_trap.md` (Publandia, Seamus O'Brien). No bribe, no skill check, no alternate route, no exception. The check runs on inventory state **before any dialogue plays** — this is specified in the asset doc and it must be implemented in that order, because the No Shamrock frame is selected before Kees opens his mouth.
- **His one-word recognition line is "Seamus."** It means Seamus O'Brien of The Blarney Trap. It is never expanded, never explained, and never given a second sentence.
- **"Wrong." and "Correct." must be near-identical in both art and audio.** The gauntlet UI carries the information. If Kees's face or voice leaks the answer, the gauntlet's difficulty and the character's premise both collapse.
- **Name collision, resolved:** Kees (bartender, Old Town) and Opa Cees (mechanic, Shamsterdam Bike Rental) are two distinct characters sharing a root name — Kees is the standard Dutch diminutive of Cornelis, as is Cees. This is a documented, accepted pairing given the different diminutive spellings and non-overlapping locations, but the two must never appear in the same scene and neither should ever be referred to by the other's spelling. Flagged for the naming registry.
- Pim exists to answer questions longer than four words. This is his mechanical function and it must be implemented — if the player can extract a long answer from Kees directly, Pim has no reason to exist and Kees has no vocabulary.
- The Shakes debuff blocks combat consumption of Oude Genever. This is authored, not a bug: your hands are shaking.
- Do not give Kees a backstory reveal, a soft moment, or a late-game monologue. "The chair is there," delivered not unkindly, is his entire interior life and it is enough.
- The 100-Year Barrel is never opened. Not in a quest, not in an epilogue, not ever.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Kees has none. Sovs, 4–25 Sovs, and a bar that predates paper money.
- [x] **NO automatic crypto assumptions** — a 1624 distillery with no signage does not need a payment innovation
- [x] **Coins, kiosks, and certificates come from the master pool** — N/A, no crypto at this location
- [x] **The bros are never scam-aware** — there is nothing to be aware of; the glass is full because that is how it is served
- [x] **Nothing winks** — Kees is incapable of winking; his face carries no information by design
- [x] **Focus on city-specific cultural exploitation instead** — the satire is tourist overconfidence and the "I can handle my alcohol" fallacy

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the joke is bros reading four centuries of practical arrangements as a personal challenge; Dutch jenever culture is presented as genuinely difficult and genuinely worth respecting
- [x] NPC is savvy entrepreneur, not villain or stereotype — Kees runs a fair, transparent, four-hundred-year-old bar, offers a 20 Sovs shortcut past his own gauntlet, and has never mocked a customer
- [x] Humour is affectionate mockery, not mean-spirited — "The chair is there" is delivered *not unkindly*, which is canon and is the tonal key to the whole location
- [x] Alcohol handled responsibly — the satire targets drinking hubris, not alcoholism; the sawdust, the chair, and Pim's physical support all exist because the bar takes care of people who overreach

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Shamsterdam/npcs/Proeflokaal_T_Kansen/npc_kees.md`
- **Registered In**: No `proeflokaal_t_kansen_npcs.json` exists. **A location JSON roster should be created** (Pim and the four atmospheric patron NPCs still unprofiled — Wave 2). Registration pending; flagged for the JSON authoring pass.
- **Sprite Sheet**: `npc_kees_pim.png` (512×512; 64×96 character frames, 128×128 portraits) — Kees occupies rows y=0 (service), y=96 (instruction + the three opener-check frames), portraits at y=192, high-contrast silhouette at (0,416). Specced in `PNG_Assets/Proeflokaal_T_Kansen_PNG_Assets.md`, Sprite Sheet 5. Supporting: `npc_proeflokaal_patrons.png`, `surface_tension_glass.png`, `gauntlet_setup.png`, `bottle_opener_proeflokaal.png`.

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — Wave 1 (mechanics-attached NPCs). Sourced from `proeflokaal_t_kansen.md` + `PNG_Assets/Proeflokaal_T_Kansen_PNG_Assets.md` + `Publandia/the_blarney_trap.md` (Seamus O'Brien cross-city opener gate). Kees / Opa Cees name-root collision documented and flagged for the naming registry. | Shamsterdam NPC authoring pass |

---

*Template Version 1.1*
