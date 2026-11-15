# NPC Profile: Bartender Kees

*"Wrong. Try again."*

## 📋 NPC Identity
- **NPC ID**: `shamsterdam_npc_kees_01`
- **Display Name**: Kees
- **Internal Name**: Kees — third-generation bartender, Bottoms Down (est. 1624), Old Town distillery district
- **Role**: Gatekeeper / Cross-City Quest Gate / Vendor (Oude Genever) / Gauntlet Administrator / Stamp Giver
- **Associated Quest**: "Shamsterdam Brewery Tour" (1 of 4, any order — Oude Genever stamp); gates the "Canal Courage" passive completion; administers the Jenever Taste Test gauntlet
- **Primary Location**: Bottoms Down — behind the eight-metre oak bar, Shamsterdam Old Town
- **Secondary Appearances**: None. Kees has been behind this bar since he inherited it and there is no reason to move him.

---

## 🎭 Core Concept

### What He's Actually Doing
Tending a jenever bar that has not changed because it has not needed to. He fills tulip glasses above the brim so surface tension makes them impossible to lift, and waits to see whether the customer bends to the bar or tries to pick the glass up like a man. He runs a five-glass blind tasting with two words of feedback per round. He checks bottle openers at the door — one from Publandia, one from this building — and he does not make exceptions.

He is also, technically, the man who keeps score. The chalkboard behind him is not decoration; it is a record, it is accurate, and he is the one who updates it. **[PROPOSED]** Pim rings the bell, Kees marks the tally. He does this the way other men take out the rubbish: without ceremony, without malice, and slightly too often.

### What Bros Believe
That this is a challenge and they are winning it.

- **Lord Pilsner** has read the scoreboard and decided it is a leaderboard, and that he is going on it. **Bradley** has read two inches of sawdust as gym flooring and wants to do squats on it. **Chadwick** is filming the ceiling, saying the word "content," and has decided the fall, the bell and the second fall are three separate pieces.

Nobody is frightened. Nobody is disgusted. The room smells like bleach and wet sawdust and they think it smells like somewhere they are about to be great in.

### The Comedy Gap
Kees is not testing anyone. The glass is full because that is how jenever is served. The sawdust is on the floor because things get spilled. The gauntlet is a tasting flight with questions attached. The padding on the beams is there because the ceiling is low and the patrons are not.

The bros walk in and read a personal challenge into a building that has been doing the same four practical things since before their country existed. Kees has never modified his expression for a customer, has never warned one, and does not intend to start.

### The Cross-City Gate
Kees runs the Publandia cross-reference. **The Blarney Trap Bottle Opener is a hard requirement** — without it, no tour, no gauntlet, no stamp, no negotiation. His recognition of it is one word: *"Seamus."* He means Seamus O'Brien, owner of The Blarney Trap. He does not elaborate and has never needed to.

The check happens before he says anything at all. He looks at the opener, then at the player, and the frame chosen for that look is chosen by the inventory, not by the conversation.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | 60s |
| Build | Built like the barrel he tends. Forearms from four decades of ceramic jugs. |
| Height | Comfortable under a low ceiling, which is more than can be said for anyone taller than 5'10" |
| Energy | Neutral. Permanently, comprehensively neutral. Nothing in the room requires him to react to it. |
| Silhouette | Barrel. Apron. Jug. At 231px he reads as a shape standing behind a slab, and the slab reads as a bar. That is all he needs to be. |

### Clothing
- **Apron older than most tourists**: Heavy canvas, jenever-stained to a single uniform amber, stiff enough at the hem that it does not move when he turns. The ties are knotted rather than tied, and have been knotted so long the knot has a shape of its own.
- **Collarless shirt, sleeves rolled**: The same one or six identical ones. Nobody has established which. He is not going to say.
- **Accessories**: The ceramic jug, functionally part of his right hand. A cloth folded over the rail that has not been used on the bar in years, because the bar does not need it and he does not want to.
- **Footwear**: Boots, sawdust to the ankle by mid-shift. The sawdust does not come off them. It has been in the boot a long time.

### Distinguishing Features
- **Permanently neutral expression.** Nothing surprises him. Nothing impresses him. Nothing. This is the character and it is also the reason the room has to do all the talking.
- **The pour**: jug raised, glass placed, stream to the brim, surface tension achieved, jug withdrawn, expression unchanged. Three frames, no variation, ten thousand repetitions.
- **The nod**: two frames. It is the highest praise available anywhere in Shamsterdam and most players will never see it.
- **[PROPOSED] His hand goes to the chalk before the order is finished.** Not rudeness. He has done the arithmetic already, the arithmetic is usually right, and on the rare occasion it is wrong he is exactly as unbothered by that.
- **He does not look up at the bell.** Everyone else in the room does. He is already reaching for the chalk.
- His "Wrong." face and his "Correct." face are near-identical **by design**.

### Sprite Notes
Sheet `npc_kees_pim.png` (512×512; 64×96 character frames, 128×128 portraits). Service row at y=0: Idle, Pour Frames 1–3, Nod Frames 1–2, "Wrong.", "Correct." Instruction row at y=96: Demonstrating the Bow, Pointing at Sawdust, Pointing at Chair, Pointing at Back Room, and the **three opener-check frames** (Blarney Trap Only / Both Openers / No Shamrock). Portraits at y=192: Neutral Eternal, and The Nod — *the single frame in the entire game where he approves of you*.

**Critical asset-doc constraints, carried forward:**
- **"Wrong." and "Correct." must be near-identical.** The joke is that his face carries no information, so the gauntlet UI must carry it instead.
- **The three opener-check frames are selected by inventory state before any dialogue plays. The Blarney Trap check happens first and gates everything.**
- **[PROPOSED] He never turns around on camera.** The scoreboard is on the wall behind him. He does not need to look at it and the player does not need him to; the tally is readable over his shoulder in every portrait, which the art gets for free.
- **[PROPOSED] No bell-reaction frame exists and none should be drawn.** Every other sprite in the location gets one. He is the only character in the room who does not turn his head.

---

## 🧠 Personality

### Archetype
**The Bar Itself** — Kees is less a character than a fixture with opinions he does not share. Four hundred years of the same room distilled into twelve words. He is neither warm nor cold; he is *neutral* in a way that reads as either, depending entirely on what the customer brought with him.

He has served more jenever than water in his lifetime and it has removed from him any capacity for surprise. It has not removed his handwriting, which is small, level and very good, and which appears on the board several times an hour.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Absolute neutrality | Not stoicism, not disdain. An actual absence of reaction. He is the only man in the room not performing. |
| Total economy of language | Twelve words. It has been enough and it is enough now. |
| Precision of pour | Above the brim, every time, without measuring. Nobody has ever seen him overfill past the meniscus. |
| Unmoved by failure | "Sawdust is there for this. Not the first time. Continue." There is no judgement in it and there is no comfort in it either. |
| Immovable on the gate | No shamrock, no tour. He will wait. He is very good at waiting. |
| **[PROPOSED]** Keeps the board himself | Pim rings, Kees marks. He has never once got a tally wrong and has never once been asked about one. |
| **[PROPOSED]** Water is free and nobody asks | There is a bottle under the bar. It comes out for the ones in the chair. It goes back. He does not mention it. |

### Internal Monologue
> "Six since the door opened. Pim rang four. The other two did not need the bell, they needed the chair.
> The board says eleven for the week. I do not remember the tenth. I do not need to; the board remembers it, and the board is the record.
> The one at the end of the bar has been coming fifty years and has never been on the board, and he drinks the oldest thing in the building, and I have never worked out how. He is not going to tell me. He has a newspaper.
> The bucket sits on a stool because a man should have somewhere to be proud of. The chair is bolted because a man should not be able to take it home.
> Pim will walk them out at eleven. He always does. I will sweep."

### Motivation
None stated. None inferable. He opens at twelve and closes at eleven and pours what is asked for. The tasting house has been in the family three generations and he is the current arrangement.

He has one preference and it is not a warm one: he would rather they bend than lift. Not out of kindness. The bending ones stay upright, and upright customers order again, and the ones who lift end their evening on his floor with his chalk in their name.

---

## 💬 Dialogue

### Complete Vocabulary (Canon — Twelve Words)

> "Welcome." / "Jenever?" / "Rookie. Geezer. Choose." / "Traditional method?" / "You bend." / "Correct." / "Wrong." / "Sawdust." / "Chair." / "Acceptable." / "Back room." / "Goodbye."

*That's it. That's all of it. Four hundred years of tradition distilled into twelve words. Everything below is drawn from this vocabulary or from the small number of sanctioned extensions.*

### Approach/Greeting

**Entry**:
> "Welcome."

**At the bar**:
> "Jenever. Rookie or geezer. Beer also. Choose."

### The Opener Check (Cross-City Gate — Runs FIRST, Before Anything Else)

**With the Blarney Trap opener, no Bottoms Down opener**:
> *(He nods.)*
> "Seamus."
> *(He points to the gauntlet setup. Five glasses, already there.)*
> "Gauntlet."

**With both openers**:
> *(One nod.)*
> "You have the glass. You earned it."
> *(He pours, with precision, to the brim.)*
> "Oude Genever."

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

**On The Concussion**:
> *(Concussion Setup animation. Jenever placed. Beer placed. No commentary whatsoever.)*
> "Traditional. Brave."

### The Jenever Taste Test Gauntlet

*Five glasses lined up, rookie to fossil. Three rounds plus The Concussion. Kees gives two words per round.*

**Round 1 — Rookie vs. Geezer**:
> "Two. One young. One old. Which."

*Correct*: "Correct."
*Wrong*: "Wrong. Try again."

**Round 2 — The Middle Three**:
> "Three. Order them."

*Correct*: *(The Nod. Two frames. This is the first one and most players will not realise what they have just received.)*
*Wrong*: *(A sigh. Not disapproving. The sigh of a man who has watched this ten thousand times.)*

**Round 3 — The Blind Test**:
> "Four. One is fossil. Find it."

*Correct*: "Acceptable." *(He points at the back room door.)* "Back room is there."
*Wrong*: "Close enough." *(He pours the Oude Genever anyway. The back room stays shut.)*

**Final — The Concussion**:
> *(Jenever placed. Beer placed. He steps back one pace, which for Kees is an enormous gesture.)*
> "Traditional. Brave."

*Success*: "Acceptable."
*Failure*: *(He points at the chair. There is one chair. It is for the truly fallen.)* "The chair is there."
*(Not unkindly. It has never once been unkindly.)*

### The Back Room

> "Back room."
> *(That is the entire unlock. He does not explain what is in it, does not accompany the player, and does not comment when they come out.)*

### Sales

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

**After all four Shamsterdam breweries are stamped (The Wobbly Windmill Brewery included)**:
> "Hendrik stamped you." *(Beat.)* "Windmill." *(He pours without being asked.)* "Canal Courage. You have it."

**After the Flesh Market tunnel emergence (Red Light Shame debuff active)**:
> *(He looks at the debuff. He pours a jenever.)* "Rookie." *(Beat.)* "For this, rookie is correct."

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
| Jonge Jenever | 4 SOVS | 35% | +15 Bravado, mild warmth. "Young. Starter." |
| Oude Jenever | 6 SOVS | 35% | +25 Bravado, The Shakes (−Accuracy). "Old. Respect required." |
| Fossil Jenever | 12 SOVS | 38% | +40 Bravado, The Shakes ×2. "Very old. Very serious." |
| Grain Train | 15 SOVS | 38% | +50 Bravado, +Liquid Courage, The Shakes. "Grain wine. Not for beginners." |
| Beer (Pilsner) | 4 SOVS | 5% | +10 HP, chaser compatibility. "Also available. Yes." |
| The Concussion Combo | 8 SOVS | — | Combined effect, +Shamsterdam Cred, −Intelligence, +Bravado. "Traditional. Brave." |
| "The Flight" (5 samples) | 20 SOVS | Escalating | The gauntlet. "For tasting. Or testing." |
| Back Room Special | 25 SOVS | 40% | +60 Bravado, everything status. "If you qualify." |

### Consumable: Oude Genever
| Effect | Value |
|--------|-------|
| Bravado Restore | +25 (35% ABV, 6 SOVS: one item with the menu's Oude Jenever, round v34 e3_genever) |
| HP Effect | None |
| Status | "The Shakes" — −15% Accuracy for 3 turns |
| Special | Cannot be consumed during combat (hands shaking) |

*Flavour text: "Four hundred years of tradition in one glass. Your ancestors are watching. They're disappointed but not surprised."*

### Hidden Details / Easter Eggs
- **The 100-Year Barrel**: In the back room. Touched annually, never opened, allegedly. Examine it. Kees will not discuss it. Pim will, at length, and knows nothing.
- **The traditional method diagram**: On the wall, in frame, from the moment the player enters. Three hand-drawn panels and a coffee ring over the third one, which is the panel showing the man in the sawdust. Every customer who spills has walked past it. Examine text confirms it has been there since 1889.
- **[PROPOSED] The board's record**: Thirty-one. Chalked, underlined twice, in a hand that has not changed in decades. It is not a boast. It is a measurement. The `TODAY` column is never empty and the space beneath it has been pre-drawn, so the next mark has somewhere to go.
- **The bottles without labels**: 200+ on the wall, arranged by age — rookie, geezer, fossil, and a fourth section with no label. Ask about the fourth section: "Don't ask." That is the entire response and it is also the section's name.
- **[PROPOSED] The labels over labels**: Several bottles wear a handwritten label pasted over an older handwritten label, which is pasted over a printed one. Nobody has peeled one back. Examine text confirms only that the top label is the newest and the newest one is not new.
- **The newspaper clippings**: Notable patrons across four centuries. Examine them. They are all the same photograph: somebody horizontal, somebody else pointing. Even the frames are the same frame.
- **The spill kit by the door**: mop, scoop, sack of sawdust, and a card reading "SELF SERVE." Examine it. The mop is dry. It has been dry a long time, and nobody has ever used it, and the sawdust is replaced weekly regardless.
- **[PROPOSED] The chair's tag**: the seatbelt bolted to the lawn chair has a luggage tag on it, in marker, with a man's first name on it. Not a patron's name. Not anyone the player will ever meet. Nobody at the bar has ever taken the tag off. [Deliberately no dog, no pet, no mascot: the tag is a luggage tag, and the chair is a chair.]
- **The distance markers on the floor**: painted, radiating out from the bar — "1M — 2M — 3M — PERSONAL BEST." Examine them and Pim, unprompted, tells you the personal best is a lie, and that he was there, and that it was closer to two.
- **The bell**: mounted behind the bar. Examine it and Kees says nothing at all, and the silence has a length to it.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Assistant Barkeep Pim | Nephew, "volunteered" into the family business. Restocking, sawdust, ringing the bell, physical support. **Answers every question requiring more than four words.** Kees has never thanked him out loud and has also never hired anyone else. |
| Seamus O'Brien (The Blarney Trap, Publandia) | The cross-city gate. Kees's recognition of the shamrock opener is one word: "Seamus." They have an arrangement neither has ever described. |
| Brewmaster Hendrik (The Wobbly Windmill Brewery) | The other half of the Shamsterdam brewery tour. Mutual respect expressed entirely through stamps. Hendrik on Kees: "He does not stamp. If Kees has stamped you, you have done something." |
| The Regular (Ancient) | Fifty years, same spot, one jenever per hour, exactly, and never once on the board. Potential couchsurf host — Kees translates his mutter into "He says you can stay." |
| Opa Cees (Tram Track Magnets) | **Same first name, different character.** Both are named Cees; one goes by Kees, the family diminutive, and is a bartender in Old Town; the other is Opa Cees, a mechanic on the south side. They have never met and must never be staged together. |
| Maarten (The Salty Swallow) | Same district generation. They nod. That is sufficient. |

### Territory / Social Dynamics
- The bar is Kees's and the room defers to it entirely. Pim manages the floor, the sawdust, the bell, and every sentence longer than four words; Kees manages the pour, the board and the chair.
- The Regular has territorial rights to the end of the bar and has held them for fifty years. Kees has never had to enforce this, does not expect to, and would not enjoy it.
- **[PROPOSED]** The board is public and the board is accurate. That is the only social contract in the building and every regular has signed it without being asked.
- Cross-city: Kees and Hendrik form a two-stamp gate on the Canal Courage passive. Neither can be bypassed. Neither makes exceptions. Both check the same Publandia opener first.

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **First visit**: The opener check. Then the glass, and the choice: bend or lift. Then the chalk, either way.
- **Gauntlet visit**: Five glasses, three rounds, The Concussion, and either "Acceptable" or the chair.
- **Post-gauntlet**: The back room, the nod on entry, and thereafter forever. The board records falls, not successes. He has never explained the distinction and nobody has asked him to.
- **Post-both-breweries**: The Hendrik acknowledgement and the unprompted pour.
- **Late game**: "Welcome," with the glass already filling, and the chalk already in his other hand.

### In Other Cities
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| Publandia | The Blarney Trap | Referenced only. His entire connection to Seamus O'Brien is one word and an arrangement. | "Seamus." |

Kees does not leave the bar. He has not needed to.

### Evolution Through Game
His vocabulary does not expand. What changes is what he does before speaking: the nod on entry, the pour without an order, the rookie selected for a specific debuff, the chalk put back down untouched. By the late game Kees is having a full conversation with the player using twelve words and a ceramic jug, and neither party has acknowledged that anything has changed.

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
| kees_pointing_chair | Concussion failure |
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

### Primary Quest: Shamsterdam Brewery Tour (1 of 4, any order)
- **Quest**: Shamsterdam Brewery Tour
- **Role**: Quest Gate, Gauntlet Administrator, Vendor, Stamp Giver
- **Trigger**: Arrival at Bottoms Down carrying the Blarney Trap Bottle Opener
- **Outcome**: "Oude Genever" stamp added to the Bottle Opener Keychain. With the other three Shamsterdam stamps (The Wobbly Windmill Brewery's Windmill Grist stamp, The Hoisted Pint and The Mad Monarch's Wit-tea Party), **completes the "Canal Courage" passive** — all Bravado loss reduced by 25% while intoxicated, with a small Shamsterdam flag icon when active.

### Quest Gate Function — CROSS-CITY, HARD REQUIREMENT

**Layer 1 — The Blarney Trap Bottle Opener (Publandia).** Required to access the brewery tour AT ALL. This is a cross-city dependency on `the_blarney_trap.md` and Seamus O'Brien's shamrock-shaped brass opener. Without it Kees says "No shamrock. No tour. Return. With opener." and the conversation ends. **There is no bribe, no skill check, no alternate route, and no exception.** The opener check runs before any other dialogue state.

**Layer 2 — The Bottoms Down opener.** Required for the stamp and Oude Genever purchase. Obtained by completing the Jenever Taste Test gauntlet only. Openers are earned, never sold (author ruling 2026-08-04), and none can be collected without the Bottle Opener Keychain from The Blarney Trap (author round v43). Without it the player can enter and drink but takes no progression.

**Layer 3 — The back room.** Full gauntlet completion (all three rounds correct) unlocks it. "Close enough" does not.

### The Jenever Taste Test Gauntlet
| Round | Challenge | Success | Failure |
|-------|-----------|---------|---------|
| 1 | Distinguish rookie (harsher) from geezer (smoother) | Proceed | Continue with accumulating debuff |
| 2 | Arrange three jenevers by age | **The Nod** | The sigh of experience |
| 3 | Identify the fossil among four similar glasses | Full completion + back room | "Close enough" — Oude Genever, no back room |
| Final | The Concussion — jenever shot immediately followed by beer chaser | "Acceptable." Maximum reward. | The chair. The sawdust does its job. |

**Success rewards**: Oude Genever ×5, "Jenever Master" title (questionable accuracy), back room access, Kees's recognition, Chadwick's footage (rough — he warned you)
**Failure consequences**: Oude Genever ×2, "Jenever Survivor" title (more accurate), immediate The Shakes, recoverable dignity damage, sawdust on your clothes

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Bottoms Down Bottle Opener | Gauntlet only (never sold; requires the Bottle Opener Keychain from The Blarney Trap (author round v43)) | Yes | Gates stamp + Oude Genever; convex glass mimics the meniscus |
| Oude Genever ×5 (or ×2) | Gauntlet resolution | Consumable | 35%, +25 Bravado, The Shakes (−15% Accuracy for 3 turns), cannot be used in combat |
| "Oude Genever" stamp | Tour completion with opener | Yes | 1 of 4 → **Canal Courage passive unlocked** when all four are stamped |
| Back Room access | Full gauntlet | Yes | The 100-Year Barrel, the private stock, the one chair |
| "Jenever Master" / "Jenever Survivor" title | Gauntlet outcome | Yes | Accuracy varies |

### State Flags Set
- `kees_met`: boolean
- `blarney_opener_verified`: boolean
- `bottoms_down_opener_acquired`: boolean
- `bottoms_down_opener_source`: enum (gauntlet)
- `traditional_method_learned`: boolean
- `first_glass_spilled`: boolean
- `gauntlet_rounds_correct`: integer (0–3)
- `kopstootje_survived`: boolean
- `back_room_unlocked`: boolean
- `bottoms_down_stamp_acquired`: boolean
- `canal_courage_unlocked`: boolean (requires all four Shamsterdam brewery stamps)

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
- **Name collision, resolved:** Kees (bartender, Old Town) and Opa Cees (mechanic, Tram Track Magnets) are two distinct characters sharing a root name — Kees is the standard Dutch diminutive of Cornelis, as is Cees. This is a documented, accepted pairing given the different diminutive spellings and non-overlapping locations, but the two must never appear in the same scene and neither should ever be referred to by the other's spelling. Flagged for the naming registry.
- Pim exists to answer questions longer than four words. This is his mechanical function and it must be implemented — if the player can extract a long answer from Kees directly, Pim has no reason to exist and Kees has no vocabulary.
- The Shakes debuff blocks combat consumption of Oude Genever. This is authored, not a bug: your hands are shaking.
- Do not give Kees a backstory reveal, a soft moment, or a late-game monologue. "The chair is there," delivered not unkindly, is his entire interior life and it is enough.
- The 100-Year Barrel is never opened. Not in a quest, not in an epilogue, not ever.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Kees has none. SOVS, 4–25 SOVS, and a bar that predates paper money.
- [x] **NO automatic crypto assumptions** — a 1624 distillery does not need a payment innovation
- [x] **Coins, kiosks, and certificates come from the master pool** — N/A, no crypto at this location
- [x] **The bros are never scam-aware** — there is nothing to be aware of; the glass is full because that is how it is served
- [x] **Nothing winks** — Kees is incapable of winking; his face carries no information by design
- [x] **Focus on city-specific cultural exploitation instead** — the satire is tourist overconfidence and the "I can handle my alcohol" fallacy

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the joke is bros reading four centuries of practical arrangements as a personal challenge; Dutch jenever culture is presented as genuinely difficult and genuinely worth respecting
- [x] NPC is savvy entrepreneur, not villain or stereotype — Kees runs a fair, transparent, four-hundred-year-old bar and has never mocked a customer
- [x] Humour is affectionate mockery — "The chair is there" is delivered *not unkindly*, which is canon and is the tonal key to the whole location
- [x] Alcohol handled responsibly — the satire targets drinking hubris, not alcoholism; the sawdust, the chair, and Pim's physical support all exist because the bar takes care of people who overreach

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `design/worlds/shamsterdam/npcs/bottoms_down/npc_kees.md`
- **Registered In**: No `bottoms_down_npcs.json` exists. **A location JSON roster should be created** (Pim and the four atmospheric patron NPCs still unprofiled — Wave 2). Registration pending; flagged for the JSON authoring pass.
- **Sprite Sheet**: `npc_kees_pim.png` (512×512; 64×96 character frames, 128×128 portraits) — Kees occupies rows y=0 (service), y=96 (instruction + the three opener-check frames), portraits at y=192, high-contrast silhouette at (0,416). Specced in `PNG_Assets/bottoms_down_png_assets.md`, Sprite Sheet 5. Supporting: `npc_bottoms_down_patrons.png`, `surface_tension_glass.png`, `gauntlet_setup.png`, `bottle_opener_bottoms_down.png`.

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — Wave 1 (mechanics-attached NPCs). Sourced from `bottoms_down.md` + `PNG_Assets/bottoms_down_png_assets.md` + `Publandia/the_blarney_trap.md` (Seamus O'Brien cross-city opener gate). Kees / Opa Cees name-root collision documented and flagged for the naming registry. | Shamsterdam NPC authoring pass |

---

*Template Version 1.1*
