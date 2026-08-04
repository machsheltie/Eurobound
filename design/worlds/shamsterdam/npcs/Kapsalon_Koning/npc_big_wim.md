# NPC Profile: Big Wim

*"You want small? There is no small. There is only 'you are not ready' and 'regular.'"*

## 📋 NPC Identity
- **NPC ID**: `shamsterdam_npc_big_wim_01`
- **Display Name**: Big Wim
- **Internal Name**: Wim — owner, Kapsalon Koning, opened 2008. "Big Wim" is the trading name and how everyone addresses him. "Wim" alone is the personal name and almost nobody uses it.
- **Role**: Vendor / Owner / Kapsalon Evangelist / Challenge Judge / Achievement Gatekeeper
- **Associated Quest**: "The Great Döner Debate: International Expansion" (Shamsterdam entry #2); The King Size Challenge (optional, Wall of Fame)
- **Primary Location**: Kapsalon Koning — counter, late-night district, Shamsterdam
- **Secondary Appearances**: The Great Döner Debate confrontation scene (his counter, after 1 AM, when a döner vendor from a previous city kicks the door in)

---

## 🎭 Core Concept

### What He's Actually Doing
Running a Dutch-Turkish snack bar that serves the definitive version of a genuine national dish, at fair prices, at the hours people actually need it, with total conviction about every layer of it. The kapsalon is real: invented in the port city in 2003 when a barber asked his local snack bar to put döner meat and cheese on his fries. Wim regards that barber as a visionary and himself as his disciple, and he is not joking, and the food is genuinely excellent.

### What Bros Believe
That they are ordering a late-night snack. Lord Pilsner asks what it is and is told, accurately, and orders it anyway without processing the answer. Chadwick sees LAYERS and therefore CONTENT. Bradley asks if there is a smaller size, which is how the "no small" beat fires, and which is the correct question that nobody in this building will ever validate.

### The Comedy Gap
Nothing here is a trick. The prices are fair, the portions are stated on the board, the photos on the wall are accurate, and the fork will break. Wim tells you all of this warmly and in advance. The bros hear enthusiasm and interpret it as hype, order the Large, and then have a religious experience followed by a cardiovascular one. The satire is entirely on the eating, never on the dish or the culture that produced it.

### The Beat That Must Survive
During the Great Döner Debate confrontation, a rival vendor from a previous city addresses him by his personal name mid-argument — not "Big Wim," just "WIM." He stops the entire fight to say *"...you know my name?"* It turns out they are in the same WhatsApp group ("European Döner Alliance"). This beat is load-bearing and must be preserved verbatim in the confrontation scene.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Late 40s |
| Build | Enormous. Hands that have built thousands of kapsalons. |
| Height | 6'5". Visible over everyone in every crowd frame, always. |
| Energy | Loud, warm, evangelical, entirely welcoming |

### Clothing
- **Apron over a football jersey**: Cheese-gold apron accents (#FFD700); the jersey stretched over an impressive frame. He is dressed for work and for a match that is not on.
- **Shaved head, gold chain**: The chain is visible over the jersey collar and moves when he laughs, which is often
- **Accessories**: The salamander paddle; a stack of aluminium trays permanently within arm's reach
- **Footwear**: Kitchen clogs, non-slip, correct

### Distinguishing Features
- Genuinely, structurally too tall for the space. His 128px sprite height must clear every other NPC in every shared frame — this is specified in the asset doc and it is the character's primary visual joke.
- Warmth entirely disproportionate to his size. He is the least threatening enormous man in the game.
- Points at the Wall of Fame with the whole arm when a champion enters
- The pained face — reserved exclusively for the words "less cheese"

### Sprite Notes
Sheet `npc_wim_kemal.png` (512×512). Wim is 64×128; Kemal is 64×96. Wim Idle at (0,0); Assembling Frames 1–4 at (64,0)–(256,0), which align with the layer sprites from Sheet 3 appearing at the Assembly Station anchor; Wim Approving at (320,0) for the both-sauces order; Wim Portrait (dialogue) 128×128 at (384,0); Explaining Frames 1–3 at (0,128)–(128,128) for the barber story; Handing Fork at (192,128); Watching (King Size) at (256,128); Pained ("Less Cheese") at (320,128); Wall-Point Gesture at (0,352); Laughing at (64,352). **Technical constraint from the asset doc: Wim's 128px height must clear all other NPCs in any shared frame — he is always visible.** Do not compress him to fit a crowd composition.

---

## 🧠 Personality

### Archetype
**The Evangelist of Excess** — Wim believes, sincerely and at volume, that the kapsalon can fix people. Not metaphorically. He thinks a hungry person at 3 AM is a solvable problem and that he has the solution, and he has been solving it nightly since 2008. He is opinionated about everything, generous with everyone, and completely uninterested in moderation as a concept.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Loud and warm in equal measure | The volume is hospitality, not aggression. Nobody has ever been intimidated by Wim for longer than four seconds. |
| Doctrinally committed to the layers | Fries, meat, cheese, salad, sauce. In that order. The order is not negotiable and he will explain why. |
| Reverent about the barber | Nataniël Gomes, 2003, port city. Wim met him once and shook his hand. He tells this story unprompted. |
| Judges the order, never the person | "Less cheese" earns a pained face. The customer still gets less cheese. |
| Purpose-driven | "Every night at 3 AM, I see the same thing. Hungry people. I fix them. This is my purpose." He means it exactly as stated. |

### Internal Monologue
> "The tall one is looking at the board like the board is going to change. It does not change. There is no small. There has never been a small and there will not be a small, because small is a decision you make before you know what you want, and at this hour nobody knows what they want, they only know that they need. So I give them regular. And if they are brave, large. And if they are something else entirely, King Size, and then they go on the wall. The wall is not a joke. The wall is a record of people who committed. There are eleven of them and I remember every name."

### Motivation
Feeding people at the hour they most need feeding, in a way that honours a dish he considers a national achievement, in a shop with his own name on it. Also, quietly: proving that the port city's invention deserves a proper temple in this city, and that he built it.

---

## 💬 Dialogue

### Approach/Greeting

**First arrival**:
> "AH. Come in, come in. You have found the right place. Not the only place — the RIGHT place."
> *(He is already reaching for a tray.)*
> "Regular or Large."

**Player asks for a small**:
> "You want small?"
> *(The whole thing pauses. This is the location's signature beat and it must land with warmth, not scorn.)*
> "There is no small. There is only 'you are not ready' and 'regular.'"

**Return visit**:
> "You came back. Everybody comes back. This is not a boast, it is a statistic."

**Regular status (3+ visits)**:
> "The usual? *(He is already building it.)* You do not have to answer. I have started."

### Key Interaction Dialogue — The Origin Story

*Wim tells this constantly, unprompted, at full length, to anyone in earshot.*

> "2003. The port city. El Aviva snack bar. A barber named Nataniël Gomes. Every day he comes, every day he orders. One day he says 'everything together. With cheese.' The owner says 'you want fries and meat and cheese?' He says 'YES.' The kapsalon is born."

> "They named it after him. His profession. KAPSALON. Hair salon. Because the barber created it. This is how legends are made."

> "Now every snack bar in the country has kapsalon. EVERY ONE. Because of one barber. One vision. One tray."

**The part he only tells people who are still listening**:
> "I met Nataniël once. Port city festival. I shook his hand. I said 'you changed my life.'"
> *(A pause. The volume drops for the only time.)*
> "He said 'I just wanted my food together.'"
> *(Back up.)*
> "THIS IS GENIUS. Accidental genius. The best kind."

### The Assembly (Visible Theatre)

*Delivered layer by layer while building, matched to Assembling Frames 1–4.*

> "First the fries. Foundation. Without foundation, chaos."
> "Then the meat. Soul. The meat gives meaning."
> "Then the cheese. Gouda. Because Dutch. This is where the port city happens. Where we become one."
> "Salad on top. For health." *(Beat.)* "...okay, for texture. The health is bonus."
> "Sauce. Garlic, sambal, or both."

**Both sauces ordered**:
> "Both sauces?"
> *(The Approving animation.)*
> "You understand. You have achieved understanding."

**"Less cheese" requested**:
> "...less cheese."
> *(The Pained animation. He complies. He complies fully and correctly and without shorting the customer.)*
> "Okay. But why. Why would you do this."

### The Fork Break (100% Guaranteed, First Kapsalon)

*Fires mid-bite, maximum comedy timing. Wim is already moving before the customer registers it.*

> "The fork breaks because you eat with passion."
> *(Second fork extended, Handing Fork animation.)*
> "This is natural. This is tradition. Get new fork."

**If the player asks for a better fork**:
> "There is no better fork. There is only the next fork. This is also a philosophy."

### The King Size Challenge

**On ordering King Size**:
> "King Size." *(He stops. He looks at the customer properly for the first time.)* "You are certain."
> "There is no time limit. This is not about speed. This is about whether you finish."
> *(He sets it down. Watching animation engages. He does not leave.)*

**During**:
> *(He says nothing. He watches. The Watching (King Size) frame holds. This silence is the entire mechanic.)*

**On completion**:
> "You finished."
> *(Wall-Point Gesture, whole arm.)*
> "You go on the wall. The wall remembers."

**On failure**:
> "You stopped." *(No cruelty in it whatsoever.)* "The tray is still yours. The wall is still there. Come back when you are ready. The kapsalon is patient."

### On the Consequences

> "Food coma? This is the body's respect for what you have eaten. Accept the coma."
> "Cheese sweats are good. Cheese sweats mean the cheese is working."
> "The tray is yours. It has absorbed your victory."

### On the Neighbours

> "Mehmet down the street? Good man. Different style. No cheese."
> *(Beat.)*
> "His loss."

> "FEBO is snack. Kapsalon is MEAL. Both have their place. Their place is smaller."

**On the Great Döner Debate**:
> "Kapsalon is BEYOND döner. It INCLUDES döner. And transcends it. Write that down. Someone should write that down."

### The Confrontation Beat (Great Döner Debate — PRESERVE VERBATIM)

*Triggers after the bros have sampled both Shamsterdam döner locations, at Wim's counter, after 1 AM. The rival vendor from whichever döner the player previously crowned kicks the door in.*

**Rival vendor**: "I KNOW WHAT IT IS, WIM."

**Big Wim**:
> "...you know my name?"

**Rival vendor**: "We're in the same WhatsApp group. 'European Döner Alliance.' But that's NOT THE POINT."

**Big Wim** (to the bros, entirely derailed, genuinely moved):
> "He knows my name."

*He is no help for the remainder of the confrontation. He is thinking about the WhatsApp group.*

### Post-Interaction
> "Go. Eat. Be slower afterward. This is correct."

### If Player Declines / Alternative Path
**Player leaves without ordering**:
> "Okay. But you will think about it." *(He is right.)* "I will be here. I am always here."

**Player orders only a drink**:
> "A cola. Just a cola." *(He hands it over without comment, then, as they turn:)* "The cola is FOR the cheese. It is not a meal. It is a TOOL."

### Callback Dialogue (Return Visits)
**After the fork break has happened once**:
> "You know about the fork now. *(He puts two forks down at the start.)* We do not discuss it."

**After King Size completion**:
> "Hey." *(Wall-Point Gesture.)* "That is you."

**After visiting Leeman's**:
> "You have been to Mehmet." *(He can tell. Nobody has established how.)* "Good. He is good. He does one thing and he does it thirty-two years. I do one thing and I put cheese on it. Both are valid."

**Late game**:
> "You have eaten here more than some of my family." *(He laughs, the full-body Laughing frame.)* "I am telling them this. They will not be pleased."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 16:00–20:59 | Counter | Dinner service. Assembly line running at half speed. Origin story told at full length. |
| 21:00–23:59 | Counter | Building volume. Pre-club traffic. Kemal arrives for second shift. |
| 00:00–04:00 | Counter | **Peak.** When kapsalon calls loudest. Wim at full output. All Wall of Fame attempts happen here. |
| 04:00–06:00 | Counter | The desperate hours. Quieter, warmer, the best conversations. |
| 06:00–16:00 | Closed | — |

### Positioning Notes
- Behind the counter, at the assembly station, with the cheese salamander glowing to his left — the shop's visual heart is in every frame with him
- The Wall of Fame is behind and to his right, positioned so the Wall-Point Gesture crosses the customer's eyeline
- Aluminium tray stack within arm's reach; he never has to turn away from a customer
- Visible over the queue at all times regardless of crowd density (the 128px constraint)
- Kemal works the cheese station beside him; the two of them cover the full counter without either moving much

---

## 🎒 Inventory / Services

### Menu
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Kapsalon (Regular) | 10 Sovs | 10 Sovs | +35 HP, Cheese Sweats. "Large enough for most." |
| Kapsalon (Large) | 14 Sovs | 14 Sovs | +50 HP, Cheese Sweats, 20% Food Coma risk. "For the committed." |
| Kapsalon "King Size" | 18 Sovs | 18 Sovs | +70 HP, Cheese Sweats, Food Coma guaranteed. Wall of Fame eligible. |
| **The Wim** | 15 Sovs | 15 Sovs | Large with extra cheese, extra meat, extra sauce, extra EVERYTHING. **Constitution check required** — fail = immediate Food Coma. Survive = +50 HP and the "Kapsalon Conqueror" achievement. |
| Extra Cheese | +2 Sovs | +2 Sovs | +10 HP, extended Cheese Sweats. "More blanket." |
| Extra Sambal | +1 Sov | +1 Sov | +5 HP, −5 HP delayed. "Port City hot." |
| Both Sauces | +1 Sov | Priceless | +5 HP, **Wim Respect**. "You understand." |
| Drink (Cola) | 3 Sovs | 3 Sovs | +5 HP. "For the cheese." |
| Replacement Fork | Free | Essential | Provided before you ask. Always. |

### Special Items
| Item | Acquisition | Effect |
|------|-------------|--------|
| Kapsalon Battle Tray | Complete the "Full Kapsalon Experience" (Large + extra cheese + both sauces) | Equipment (Throwable/Shield). +2 Defence equipped; moderate damage thrown; single use if thrown, infinite as shield. Retains cheese aroma; may attract or repel NPCs. |
| Wall of Fame photo | King Size completion | Permanent shop fixture; examinable; Wim points at it on every subsequent visit |

### Hidden Details / Easter Eggs
- **The Wall of Fame is real**: Eleven photos before the player arrives. Examine them individually — each has a first name and a date. Wim can name all eleven from memory if asked, in order, with dates.
- **"The Wim"**: The 15 Sovs item is named after him, by his customers, without his input. He has never referred to it by that name out loud. Ordering it produces a beat of silence before he starts building.
- **Nataniël Gomes**: The barber's name and the 2003 date are historically accurate to the real dish's origin. This is deliberate — the tribute is sincere.
- **The two forks**: After your first fork break, Wim silently sets down two forks with every subsequent order, forever, and never mentions it.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Kemal | Nephew. Cheese station, second shift, business student. Trained by Wim. Will probably open his own someday and Wim knows it. |
| Mehmet "The Meat Architect" Leeman | Down the street. Friendly rivalry, genuine mutual respect, opposite philosophies. Leeman's board reads "NO KAPSALON. Go to Wim for that." |
| Counter Worker Anouk / Kitchen Worker Henk (FEBO Automat) | The other late-night tier. "FEBO is snack. Kapsalon is MEAL." No hostility; a hierarchy. |
| Budtender Bas (De Groene Gids) | Munchies pipeline endpoint. Wim receives Bas's customers roughly ninety minutes after Bas is finished with them. |
| The rival döner vendor (Great Döner Debate) | Same WhatsApp group: "European Döner Alliance." Knows Wim's actual first name. This surprises Wim enormously. |
| Brewmaster Hendrik (Brouwerij de Molen) | Never met. Wim has heard about a man who lectures about grain for forty minutes and has expressed a desire to meet him. |

### Territory / Social Dynamics
- Wim and Mehmet are the two poles of Shamsterdam's late-night food ecosystem and both are explicitly, warmly aware of it. Neither poaches. Each sends customers to the other for what the other does better.
- The 3 AM decision tree: FEBO (snack, no commitment) → Leeman's (fuel, standing, judged) → Kapsalon Koning (maximum commitment, seating, cheese). Wim is the terminus.
- Kemal is being trained deliberately and generously. Wim has never once implied the shop is his to keep.

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **First visit**: "No small," the origin story, the assembly theatre, the fork break
- **Second visit**: Two forks placed silently. The Great Döner Debate progress registers (Shamsterdam entry #2).
- **Post-both-döner-locations, after 1 AM**: The confrontation scene fires. The "you know my name?" beat.
- **King Size attempt**: The Watching. Then the wall, or the invitation to come back.
- **Late game**: Regular status. He starts building before you speak.

### In Other Cities
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| — | — | Wim does not leave the shop. He is behind that counter fourteen hours a day. His cross-city presence is a WhatsApp group he did not know he was famous in. | "He knows my name." |

### Evolution Through Game
Wim does not change; the player's standing does. The progression is: customer → someone who ordered both sauces → someone who broke a fork → someone on the wall → someone Wim tells his family about. Each step is marked by a gesture rather than a line, and the final one is a laugh.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| wim_idle | Commanding presence, warm despite size, visible over everyone | 45% |
| tray_stack_adjust | Squares the aluminium tray stack. Compulsive. | 20% |
| salamander_check | Regards the cheese station, satisfied | 20% |
| wim_laughing | Full-body warmth, usually at something a customer said | 15% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| wim_assembling (4 frames) | Order placed. Frames align with layer sprites at the Assembly Station anchor. |
| wim_approving | Both sauces ordered |
| wim_explaining (3 frames) | The barber story |
| wim_handing_fork | The fork break (100%, first kapsalon) |
| wim_watching | King Size in progress. Held frame, no movement. |
| wim_pained | "Less cheese" requested |
| wim_wall_point | Champion enters, or King Size completed |

### Sprite States
| State | When Used |
|-------|-----------|
| wim_counter | Default, 64×128 |
| wim_portrait | Dialogue close-up, 128×128 |
| wim_high_contrast | Accessibility outline variant marking him as interactive |

---

## 🎯 Quest Integration

### Primary Quest: The Great Döner Debate: International Expansion
- **Quest**: The Great Döner Debate: International Expansion
- **Role**: Vendor / Debate Participant / Confrontation Scene Host
- **Trigger**: Eating here counts as Shamsterdam entry #2 (Leeman's is #1). Sampling both triggers the confrontation scene at Wim's counter after 1 AM.
- **Distinction**: Kapsalon is "döner-adjacent" — it counts, and it is its own category. Wim's stated position: "Kapsalon is BEYOND döner. It INCLUDES döner. And transcends it."
- **Outcome**: The player must publicly rank the döner of the trip. Wim's counter is the venue for the reckoning.

### Optional Challenge: The King Size
- **Requirement**: Order and finish the King Size kapsalon (18 Sovs)
- **Time Limit**: None. This is survival, not speed.
- **Witness**: Wim watches the entire attempt. He does not leave and does not speak.
- **Reward**: Photo on the Wall of Fame (permanent, examinable), Wim's eternal recognition, "Wall of Fame" achievement
- **Consequence**: Guaranteed Food Coma. No regrets.

### The Achievement Track
| Achievement | Trigger |
|-------------|---------|
| Initiated | First kapsalon |
| Passionate | Fork break |
| Understanding | Both sauces |
| Committed | Large completed |
| Kapsalon Conqueror | "The Wim" survived (Constitution check passed) |
| Wall of Fame | King Size completed |
| Transcended | Survived a Food Coma |

### Quest Gate Function
Wim gates the Wall of Fame, the Kapsalon Battle Tray equipment item, and one half of the Great Döner Debate's Shamsterdam sample requirement. None of these can be obtained elsewhere. He refuses nobody; the only gate is appetite.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Kapsalon Battle Tray | Full Kapsalon Experience | Yes (shield) / single use (thrown) | +2 Defence equipped; moderate throw damage; cheese aroma affects NPC reactions |
| Wall of Fame photo | King Size complete | Yes | Permanent shop fixture, examinable |
| Wim Respect | Both sauces, or King Size | Yes | Dialogue state; unlocks the regular-status ordering shortcut |

### State Flags Set
- `wim_met`: boolean
- `wim_visit_count`: integer
- `wim_fork_broken`: boolean (drives the silent two-fork behaviour thereafter)
- `wim_both_sauces`: boolean
- `wim_respect`: boolean
- `king_size_attempted`: boolean
- `king_size_completed`: boolean
- `the_wim_ordered`: boolean
- `the_wim_survived`: boolean
- `doner_debate_shamsterdam_2`: boolean
- `wim_confrontation_played`: boolean

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. Wim at full 128px height towering over the entire queue
2. The assembly line mid-build, all five layers visible in cross-section
3. The Wall of Fame, eleven photos, the twelfth space empty and waiting
4. The Pained face at the exact moment "less cheese" is said
5. "...you know my name?" — the confrontation frozen, a döner war paused by a WhatsApp group

### Meme Potential
- "There is no small. There is only 'you are not ready' and 'regular.'"
- "Both sauces? You understand. You have achieved understanding."
- "The fork breaks because you eat with passion."
- "...less cheese. Okay. But why. Why would you do this."
- "...you know my name?"
- "He said 'I just wanted my food together.' THIS IS GENIUS."

---

## 🗣️ Voice Direction

### Accent
Dutch-Turkish, second generation, Shamsterdam-raised with port-city cadence. A thunderous mix of Dutch slang, Turkish endearments, and food philosophy. Loud by default — not shouting, just operating at a volume calibrated for a fryer, a salamander, and a queue.

### Tone
- **Greeting**: Enormous warmth. He is genuinely glad you are here at this hour.
- **"No small"**: Firm, warm, final. Never mocking. The customer is not stupid for asking; the question simply has one answer.
- **Assembly**: Escalating, rhythmic, one line per layer, building like the tray builds
- **The barber story**: Volume drops exactly once, on "I just wanted my food together," then comes back up hard on "THIS IS GENIUS"
- **King Size watching**: Silence. Do not record filler.
- **"...you know my name?"**: Quiet. Genuinely thrown. A very large man briefly touched. This is the character's single most vulnerable line and it must be underplayed.

### Key Delivery Notes
- The volume is hospitality. If Wim ever reads as aggressive, the direction has failed.
- "Why would you do this" is asked in real bewilderment, not sarcasm. He would like an answer and does not expect one.
- "This is my purpose" is delivered completely straight. He is not being profound; he is describing his job.
- The Nataniël Gomes story gets told at full length to anyone who stands still. Do not trim it in the booth — the length is the characterisation.

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

- **HARD CANON: this character is BIG WIM. He was formerly drafted as "Big Willem" and that name is retired.** Willem is the Voetgangerstunnel busker and nobody else, game-wide.
  - ⚠️ **KNOWN OUTSTANDING RENAME MISS**: `Design/Quests/greatdonerdebate.md` line 325 still reads *"I KNOW WHAT IT IS, WILLEM."* This must be changed to *"I KNOW WHAT IT IS, WIM."* The "...you know my name?" response is unaffected and still works — "Big Wim" is the trading name, "Wim" is the personal one, and the rival using the personal name is the point. Flagged, not edited in this pass.
- **"The Wim" (15 Sovs) and "King Size" (18 Sovs) are two different items with overlapping design intent.** `greatdonerdebate.md` defines The Wim (large + extra everything, Constitution check, Kapsalon Conqueror achievement); `kapsalon_koning.md` defines King Size (Wall of Fame eligible, guaranteed Food Coma). Both are carried in this profile as distinct SKUs. If a reconciliation pass merges them, The Wim's name and the Constitution check must survive.
- Wim's 128px sprite height must clear every other NPC in every shared frame. This is an asset-doc constraint and a character constraint. Do not compress him into a crowd.
- The fork break is 100% guaranteed on the first kapsalon and cannot be prevented. After it fires once, Wim silently puts down two forks forever and never mentions it again — implement the silence, it is funnier than a callback line.
- The confrontation beat is scene-critical. Preserve "...you know my name?" verbatim. Wim is useless for the rest of the confrontation because he is thinking about the WhatsApp group; play it that way.
- The Wall of Fame's eleven pre-existing photos need real first names and dates as examine text. Wim must be able to recite all eleven in order.
- Nataniël Gomes and the 2003 origin are the real history of the dish. The tribute is sincere and must not be played for irony.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Wim has none. Sovs, cash, 10–18 Sovs.
- [x] **NO automatic crypto assumptions** — a snack bar counter at 3 AM takes cash and card
- [x] **Coins, kiosks, and certificates come from the master pool** — N/A, no crypto at this location
- [x] **The bros are never scam-aware** — there is nothing to be aware of; the board is accurate, the photos are accurate, the fork will break
- [x] **Nothing winks** — Wim's enthusiasm is total and unironic at every moment including the fork
- [x] **Focus on city-specific cultural exploitation instead** — the satire is the eating experience and late-night decision-making, never the dish or the community that made it

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the joke is bros ordering Large at 3 AM; the kapsalon itself is celebrated and its real inventor is honoured by name
- [x] NPC is savvy entrepreneur, not villain or stereotype — Wim is a skilled, generous, fairly-priced operator training his nephew to succeed him; he sends business to his competitor and speaks well of him
- [x] Humour is affectionate mockery, not mean-spirited — the Dutch-Turkish fusion is celebrated at length and with historical accuracy; every laugh is at the customer's relationship with a tray, never at Wim

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Shamsterdam/npcs/Kapsalon_Koning/npc_big_wim.md`
- **Registered In**: No `kapsalon_koning_npcs.json` exists. **A location JSON roster should be created** (Kemal and the five atmospheric customer groups still unprofiled — Wave 2). Registration pending; flagged for the JSON authoring pass.
- **Sprite Sheet**: `npc_wim_kemal.png` (512×512; Wim 64×128, Kemal 64×96) — Wim occupies rows at y=0 and y=128 plus the Wall-Point and Laughing frames at y=352. Specced in `PNG_Assets/Kapsalon_Koning_PNG_Assets.md`, Sprite Sheet 4. Supporting: `npc_kapsalon_customers.png` (Wall of Fame residents), and the location's food/effect sheets for assembly layers, fork break, and Battle Tray.

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — Wave 1 (mechanics-attached NPCs). Sourced from `kapsalon_koning.md` + `PNG_Assets/Kapsalon_Koning_PNG_Assets.md` + `Design/Quests/greatdonerdebate.md` ("The Wim" menu item, confrontation beat). Big Willem → Big Wim rename carried; outstanding rename miss in `greatdonerdebate.md` flagged. | Shamsterdam NPC authoring pass |

---

*Template Version 1.1*
