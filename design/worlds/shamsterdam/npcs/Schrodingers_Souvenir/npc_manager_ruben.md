# NPC Profile: Manager Ruben

*"Schrödinger's cat was both alive and dead until observed. Your souvenir is both legal and illegal until customs observes it. That's the shop's philosophy."*

## 📋 NPC Identity
- **NPC ID**: `shamsterdam_npc_ruben_01`
- **Display Name**: Manager Ruben
- **Internal Name**: Ruben — shop manager, Schrödinger's Souvenir. Former coffeeshop worker, transitioned to "legal" hemp retail.
- **Role**: Vendor / Shop Manager / Legal Disclaimer Specialist / Seed Ritual Administrator
- **Associated Quest**: None owned. Administers the "Is This Legal?" interaction, the Seed Purchase Ritual, the Suspicious Souvenir inventory tag, and the Customs Checkpoint resolution chain.
- **Primary Location**: Schrödinger's Souvenir — counter and legality zones, tourist district, Shamsterdam
- **Secondary Appearances**: Referenced at the Customs Checkpoint / Airport resolution zone (his disclaimer is what the player remembers, and it was correct)

---

## 🎭 Core Concept

### What He's Actually Doing
Selling products that are entirely legal in the Netherlands, in a shop that is legally distinct from a coffeeshop, to tourists who are going to carry some of them across a border. Ruben provides maximum accurate information and accepts minimum liability. He asks where you are travelling to, because it is the relevant question. He tells you exactly what is in the product. He tells you he cannot tell you what your country thinks of what is in the product. Then he sells it to you, because it is legal to sell.

### What Bros Believe
That the asterisks are decoration. Lord Pilsner: "Hemp SOUVENIRS? This is CLASSY. This is DIFFERENT. This isn't a coffeeshop." — which is correct, and which he has understood by accident. Chadwick is buying a grinder for TOBACCO and papers for ROLLING things, LEGAL things. Bradley takes the hemp bag, because hemp bags are safe, and then asks Ruben to explain the CBD situation again. Slowly. Ruben does.

### The Comedy Gap
Everyone in the transaction knows exactly what is happening and the entire exchange is conducted as though they do not. It is a social contract, executed with total politeness, by two parties who are both being scrupulously honest within a framework designed to make honesty non-committal. Ruben never lies. He simply declines, warmly and completely, to answer the one question the customer actually has.

### The Constraint That Makes It Work
**Ruben and Yuki never appear worried, evasive, or shifty in any frame.** The entire satire collapses if the staff read as dishonest. They are being scrupulously truthful and it is not helping.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | 30s |
| Build | Relaxed retail posture. Ex-coffeeshop shoulders — six years of leaning on a counter. |
| Height | Average |
| Energy | Friendly, reassuring, carefully non-liable |

### Clothing
- **Hemp shirt (of course)**: Hemp green (#228B22) staff shirt. It is the uniform and it is the joke and it is also, genuinely, a hemp shirt from the front of the shop. Zone 1 stock. Definitely legal.
- **Professional casual**: Chinos, clean trainers. He looks like a shop manager because he is one.
- **Accessories**: A lab-test certificate binder kept at the counter; a pen he uses to point at percentages
- **Footwear**: Trainers, retail-grade

### Distinguishing Features
- Escalating hand position as qualifier density increases — the Explaining frames get progressively more open-palmed and this is the animation's whole gag
- Genuinely reassuring presence in a shop about legal uncertainty
- Never breaks eye contact when saying "I cannot answer that question"
- Points at the zone signs rather than answering, because the signs do the liability work

### Sprite Notes
Sheet `npc_ruben_yuki.png` (512×512; 64×96 character frames, 128×128 portraits). Ruben's qualification row at y=0: Idle, Welcome Gesture, Explaining Frames 1–3 (**open palms → one qualifier → three more qualifiers**), Destination Query, Careful Hedge, "I cannot answer that question." Transaction row at y=96: Seed Disclaimer Recital, Schrödinger Philosophy, Pointing at Zone Signs, Ringing Up, Sealing the Bag. Portrait at (0,192).

**Critical asset-doc constraints, carried forward:**
- **Ruben's three Explaining frames escalate qualifier density visibly through hand position. The animation is the joke, not the dialogue.**
- **Ruben and Yuki never appear worried, evasive, or shifty in any frame — the entire satire collapses if the staff read as dishonest.**
- The Quantum Cat Portrait exists so the mascot can say what the staff legally cannot.

---

## 🧠 Personality

### Archetype
**The Scrupulously Honest Non-Answer** — Ruben is a former coffeeshop worker who moved into legal hemp retail and learned the distinctions cold. He tells you everything he knows, which is a great deal, and nothing he does not, which is your destination country's regulatory position. He is not hedging to protect the shop from you. He is hedging because he genuinely cannot know, and saying so is more honest than guessing.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Maximum information, minimum responsibility | The Ruben Method. He has more product knowledge than any tourist will use. |
| Warmly final | "I cannot answer that question" is delivered warmly and is completely non-negotiable. |
| Zero evasiveness | He is not shifty. He is precise. The distinction is the character. |
| Committed to the bit — sincerely | The Schrödinger philosophy is not a marketing line to him. He finds it genuinely apt. |
| Non-judgmental about seeds | Everyone knows what the seeds are for. He does not pretend otherwise and he does not comment. |

### Internal Monologue
> "He is going to ask if it is legal, and I am going to say yes, here, absolutely, and then I am going to ask where he is going, because that is the only part of the sentence that matters and nobody ever leads with it. And he will say a country, and I will say I cannot give legal advice for other jurisdictions, which is true, and which he will hear as 'probably fine.' And it might be. It usually is. Customs has bigger concerns than a man with hemp protein powder and a tote bag. But 'usually' is not a thing I can put in a sentence and still sleep, so I will say the true thing again, in a slightly different order, and he will buy two."

### Motivation
Running a legal shop legally. Ruben came out of the coffeeshop trade into a business with clearer rules and better hours, and he takes the clearer rules seriously. He would like customers to make informed choices. He is entirely at peace with the fact that they mostly do not.

---

## 💬 Dialogue

### Approach/Greeting

**First entry**:
> "Welcome to Schrödinger's Souvenir! Everything here is legal in Shamsterdam."
> *(Welcome Gesture animation. Then the pivot, immediately, because it is the only question that matters:)*
> "Where are you traveling to?"

**Player names a destination**:
> "Okay. Good. That changes some things and not others. Let me show you the zones."

**Player asks whether this is a coffeeshop**:
> "No." *(He points at the sign that says THIS IS NOT A COFFEESHOP, which is on the window, in capitals.)* "There is a sign. People still ask. I understand why — we are between two of them. It is a geography problem, not a signage problem."

### Key Interaction Dialogue — The Zones

*Ruben walks the customer through the shop's four legality zones. Pointing at Zone Signs animation. The signs do the liability work.*

**Zone 1 — Definitely Legal**:
> "Hemp clothing, bags, rope. Actual rope. This is plant fibre. There are no cannabinoids in it at all. This zone is boring and I love it."

**Zone 2 — Probably Legal**:
> "CBD oils, hemp food, wellness items. Most countries allow this. Most. I said most twice on purpose."

**Zone 3 — Questionably Legal**:
> "Smoking accessories. For tobacco use." *(No inflection on 'tobacco.' None.)* "Your customs agent may have questions. The questions are usually about the design, not the object."

**Zone 4 — Souvenir Seeds**:
> "Legal here. As souvenirs. Collector's items." *(Beat.)* "Not for germination. That part is important and I am going to say it again later, more formally."

### The "Is This Legal?" Interaction

*The five-step pattern. Explaining Frames 1–3 escalate hand position as the qualifiers stack.*

**Tourist**: "Is this legal to bring home?"

**Ruben** (Explaining Frame 1, open palms):
> "Here, absolutely."

**Ruben** (Explaining Frame 2, one qualifier):
> "In your country — you should research their specific regulations regarding CBD products."

**Ruben** (Explaining Frame 3, three more qualifiers):
> "We can't provide legal advice for other jurisdictions. The threshold varies. The enforcement varies more than the threshold does."

**Tourist**: "But like... will I get in trouble?"

**Ruben** (Careful Hedge):
> "I cannot make that assessment. Every country has different rules."

**Tourist**: "...I'll take two."

**Ruben**:
> *(He rings up two. Ringing Up animation. Nothing on his face has changed.)*

### On CBD

> "CBD is different from THC. CBD won't get you high. It's in a legal gray area internationally. I can explain more."
> *(He can. He will. It takes four minutes and it is completely accurate.)*

> "The oil has less than 0.2% THC. That's the EU threshold. Some countries accept it. Some don't. Research is key."

> "I'm not saying don't buy it." *(Reassuring Shrug animation.)* "I'm saying know what you're buying. Then buy it. Probably."

### The Seed Purchase Ritual

*Seed Disclaimer Recital animation. Word-perfect, seven hundredth time this month.*

**The script**:
> "These seeds are sold as souvenirs and collector's items only. Germination is not legal in most countries and we do not condone or encourage cultivation. By purchasing, you acknowledge these are novelty items."

**Player: "Yes, I understand, just collecting"**:
> "Thank you." *(He seals the bag. Sealing the Bag animation. No comment.)*

**Player: "What do you mean, germination?"**:
> "The process by which a seed becomes a plant." *(Completely straight.)* "It is not legal in most countries."

**Player: "I definitely won't plant these"** *(wink)*:
> "Good." *(He does not wink back. He has never winked back.)*

**Player: "How do I—"**:
> "I cannot answer that question."
> *(Delivered warmly. Delivered finally. He does not look away.)*

**On seeds generally**:
> "These seeds? Absolutely legal to purchase here. As souvenirs. They're collector's items."

> "NOT for germination. That's important. As souvenirs, they're legal. As seeds you plant... different situation."

### On Customs

> "Will customs care? I can't predict customs. I can tell you what's in the products."
> *(Customs Warning animation.)*

> "Most of the time nothing happens. I am not allowed to say that as advice, so I am saying it as an observation about statistics."

### The Philosophy (Schrödinger Philosophy animation)

> "Schrödinger's cat was both alive and dead until observed. Your souvenir is both legal and illegal until customs observes it. That's the shop's philosophy."

> "Schrödinger proposed a thought experiment. We made it a business model. Until observed, everything is fine."

> "Shamsterdam has one set of rules. The EU has another. Your country has another. We exist in the overlap."

> "I sell legal products. What you do with them after you leave is... your experiment to conduct."

> "The seeds are the most honest product. Everyone knows what they are. Everyone pretends otherwise. It's a social contract."

> "CBD is genuinely helpful for many people. It's also genuinely confusing legally. We handle the first part. You handle the second."

**If the player asks about the coffeeshop years**:
> "Six years. Good work, bad hours, and the rules were simpler because everything in the building was one category." *(Beat.)* "Here there are four categories and a border. I prefer it. I am aware that is a strange preference."

### Sales Close

> "Forty Sovs." *(Sealing the Bag.)* "Sealed. That is not a legal protection, it is a bag. But it is sealed."

### Post-Interaction
> "Enjoy Shamsterdam. Check the regulations for your flight home." *(Beat.)* "You won't. That's fine. Most people don't."

### If Player Declines / Alternative Path
**Player buys only the hemp tote bag**:
> "The bag." *(A small nod, genuinely approving.)* "That one is actually simple. Enjoy the bag."

**Player asks him to just say whether it's fine**:
> "I cannot answer that question." *(Same warmth. Same finality. He will say it as many times as it is asked.)*

**Player asks about the quantum cat mascot**:
> "The cat is the only one of us permitted to editorialise." *(He points at the mascot.)* "It has a hemp leaf. It says things I cannot."

### Callback Dialogue (Return Visits)
**Second visit**:
> "Back. Same destination, or has that changed?" *(It is the same question. It is always the relevant question.)*

**After a customs encounter (Observed)**:
> "They found it." *(No surprise, no smugness.)* "I said I could not predict it. That was true in both directions."

**After a customs success (Unobserved)**:
> "Nothing happened." *(Beat.)* "That is the most common outcome and it is not evidence of anything. It is one observation."

**After visiting De Groene Gids**:
> "You've been to the Green Guide." *(Beat.)* "I worked in a shop like that. Not that one. One like it." *(Beat.)* "The prices here are better and the product is less interesting. Both of those are on purpose."

**Late game**:
> "You know the zones now." *(He stays behind the counter.)* "Ask Yuki about the fifteen percent. She has the lab sheets and I have a headache."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 10:00–12:59 | Counter | Opening. The Research Tourist arrives with a phone and checks laws. Ruben's favourite hour. |
| 13:00–17:59 | Counter / floor | Peak. Coffeeshop overflow. Maximum "is this a coffeeshop" questions. |
| 18:00–20:59 | Zone 4 / counter | Evening. Seed purchases cluster here. The Anxious Purchaser hour. |
| 21:00–22:00 | Counter | Last hour. Quietest. The philosophy lines are available here. |
| 22:00–10:00 | Closed | Extended tourist confusion hours end at ten |

### Positioning Notes
- Behind the counter by default; walks the zones for consultations, moving front-to-back through Definitely → Probably → Questionably → Seeds
- The quantum cat mascot signage is in frame at the entrance and again above the counter
- Zone 4 (Souvenir Seeds) is at the back, deliberately, so the walk through the other three zones is the education
- The legal disclaimer board is visible from the counter and Ruben gestures at it without turning
- Yuki works the floor and the education corner; Ruben holds the counter, the disclaimer recital, and the transaction

---

## 🎒 Inventory / Services

### Product Inventory
| Item/Service | Price | Category | NL Legal | Export Risk | Notes |
|--------------|-------|----------|----------|-------------|-------|
| Hemp Tote Bag | 15 Sovs | Clothing | 100% | None | Actually just a bag |
| Hemp Rope Bracelet | 12 Sovs | Accessory | 100% | None | Cannabis-free cannabis plant |
| CBD Oil 5% | 30 Sovs | Wellness | 100% | Low–Medium | "Check your local laws" |
| CBD Oil 15% | 55 Sovs | Wellness | 100% | Medium | "Seriously, check them" |
| CBD Gummies | 25 Sovs | Edible | 100% | Medium | "Some countries are weird about gummies" |
| Hemp Protein Powder | 35 Sovs | Food | 100% | Low | Actual nutrition product |
| "Tobacco" Grinder | 20 Sovs | Accessory | 100% | Low | For tobacco. Obviously. |
| "Tobacco" Pipe | 25 Sovs | Accessory | 100% | Low–Medium | Design-dependent risk |
| Rolling Papers (Branded) | 8 Sovs | Accessory | 100% | Very Low | Paper is legal everywhere |
| Souvenir Seed Pack | 40 Sovs | Seeds | 100%* | **HIGH** | *Not for germination |
| Premium Strain Seeds | 65 Sovs | Seeds | 100%* | **VERY HIGH** | *Definitely not for germination |
| Space Cake Mix | 20 Sovs | "Food" | 100% | High | "Just add... nothing illegal" |
| Leaf-Shaped Everything | 10 Sovs–30 | Novelty | 100% | Embarrassment | Declaring your tourist status |

### The Customs Checkpoint (Resolution)
| Item Class | Pass Rate | Outcome |
|------------|-----------|---------|
| Hemp clothing / accessories | 100% | Pass |
| CBD Oil (<0.2%) | 85% | Usually pass |
| CBD Oil (>0.2%) | 60% | Possible questions |
| Smoking accessories | 90% | Usually pass, some side-eye |
| **Souvenir seeds** | **50/50** | **THE SCHRÖDINGER MOMENT.** Found = confiscation certain. Not found = seeds enter Schrödinger's garden potential. |

### Hidden Details / Easter Eggs
- **The quantum cat**: The mascot is the only entity in the shop permitted to editorialise. Its signage says what Ruben legally cannot, and the Quantum Cat Portrait exists as a dialogue speaker frame specifically for this. Examine the mascot for lines Ruben would never deliver.
- **The asterisk**: The window says "All products comply with Dutch law*". Examine the asterisk. It leads nowhere. This is stated in the location profile and it is authored.
- **The lab-test binder**: Kept at the counter. Examinable. It is real, it is complete, and it is genuinely more information than any customer has ever wanted.
- **The Research Tourist**: An ambient NPC who actually checks their destination's laws on a phone. Ruben's favourite customer. If the player mimics this behaviour — asking about a specific named destination before buying — Ruben gives a measurably better and longer answer.
- **The hemp shirt**: Ruben's uniform is Zone 1 stock. It is for sale. 28 Sovs. He will confirm this if asked and finds the question reasonable.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Associate Yuki | Floor sales, product education, pharmaceutical sciences background. She handles cannabinoid detail; he handles liability. Clean division, no friction. |
| Budtender Bas (De Groene Gids) | Ruben is a former coffeeshop worker. Not that shop — "one like it." Different corridor of the same tourist flow. Never met on screen. |
| Ticket Attendant Lars / Growing Room Attendant Sanne (The Hemp Museum) | Educational counterpart. Same subject, no commerce. Ruben sends genuinely curious customers there. |
| Vendor Margriet (De Botanische Leugen) | Same "customs will be interesting" energy, different product category. Neighbourly awareness. |
| Manager Femke (Condomerie Het Gulden Vlies) | Both run shops where the customer's own assumptions are the main obstacle. Never met on screen. |
| Customs Agent (Airport, if implemented) | The observer. Ruben has never met one and has thought about them a great deal. |

### Territory / Social Dynamics
- Counter is Ruben's; the education corner and floor are Yuki's. Customers with legal questions go to him; customers with chemistry questions go to her; customers with both get passed once, cleanly.
- The shop is positioned deliberately between actual coffeeshops and normal tourist shops — a liminal space, catching overflow confusion from both directions.
- Ruben directs genuinely curious customers to The Hemp Museum and price-sensitive ones to nowhere in particular, because his prices are already better than De Groene Gids's.

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **First visit**: Welcome, the destination pivot, the zone walk, the five-step legality pattern
- **Seed purchase**: The disclaimer recital, word-perfect, and the Suspicious Souvenir tag applied
- **Return visits**: "Same destination, or has that changed?" — always the relevant question
- **Post-customs**: One line, either way, with no smugness in either direction
- **Late game**: He delegates to Yuki and admits to a headache, which is the only complaint he makes in the entire game

### In Other Cities
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| Any | Airport / Customs Checkpoint | Referenced, not present. His disclaimer is what the player remembers at the moment of observation, and it was correct. | "I said I could not predict it. That was true in both directions." |

### Evolution Through Game
Ruben does not change. The player's relationship to the asterisk does: first visit it is invisible, second visit it is a joke, and by the customs checkpoint it is the only thing in the bag that matters. Ruben said the same sentence every single time and it was accurate every single time.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| ruben_idle | Counter pose, relaxed, reassuring | 48% |
| ruben_hemp_shirt_detail | Close crop; the shirt is the uniform and the joke | 18% |
| binder_check | Consults the lab-test binder for a percentage | 20% |
| zone_sign_glance | Confirms the signage is still doing its job | 14% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| ruben_welcome_gesture | Entry. "Everything here is legal in Shamsterdam." |
| ruben_explaining (3 frames) | Any legality question. **Qualifier density escalates visibly through hand position.** |
| ruben_destination_query | The pivot. "Where are you travelling to?" |
| ruben_careful_hedge | "I cannot make that assessment." |
| ruben_cannot_answer | "I cannot answer that question." Warm. Final. |
| ruben_seed_disclaimer | Word-perfect recital, seven hundredth time this month |
| ruben_schrodinger_philosophy | The philosophy lines |
| ruben_pointing_zone_signs | Directional; the signs do the liability work |
| ruben_ringing_up / ruben_sealing_bag | Transaction close |
| ruben_customs_warning | "I can't predict customs." |
| ruben_reassuring_shrug | "I'm not saying don't buy it." |

### Sprite States
| State | When Used |
|-------|-----------|
| ruben_counter | Default, behind-register anchor pose |
| ruben_floor | Zone walk consultations |
| ruben_portrait | Dialogue close-up, 128×128 |
| ruben_high_contrast | Accessibility outline variant marking him as interactive |

---

## 🎯 Quest Integration

### Primary Quest
None owned. Ruben administers four interlocking systems.

### Systems Administered
1. **The "Is This Legal?" interaction.** Five-step pattern: Dutch status (clear) → destination query (relevant) → careful hedge (liability) → "research local laws" (deflection) → tourist buys anyway (inevitable). Every step is truthful.
2. **The Seed Purchase Ritual.** Seven steps of legal fiction, executed by both parties in full knowledge. Ruben's disclaimer script is fixed and word-perfect. Four customer response options, all of which resolve identically.
3. **The Suspicious Souvenir inventory tag.** Applied to seeds, high-concentration CBD, and anything with complex legal status. Drives customs checkpoint awareness and an anxiety status during travel segments.
4. **The Customs Checkpoint.** Inventory scan at the airport or border. Outcomes by item class, with seeds at a genuine 50/50 — the wavefunction collapse.

### Quest Gate Function
Ruben gates nothing and refuses nobody. Everything in the shop is legal to sell and he will sell all of it to anyone. What he withholds is not a product but a *sentence* — the one that says "you'll be fine." The gate is epistemic, and it is the entire location.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Any product | Any | Inventory | Some carry the Suspicious Souvenir tag |
| Suspicious Souvenir tag | Seeds / high-CBD / complex items | Until customs | Customs checkpoint awareness; anxiety status during travel |
| Souvenir Seed Pack / Premium Strain Seeds | Purchase + ritual | Until observed | The Schrödinger item. 50/50 at customs. |
| Sealed bag | Any purchase | Cosmetic | "That is not a legal protection, it is a bag. But it is sealed." |

### The Schrödinger Achievement Track
| Achievement | Trigger |
|-------------|---------|
| Lawyer | Hemp clothing only — played it completely safe |
| Experimenter | CBD purchase — acceptable risk |
| Collector | Seed purchase — embraced the fiction |
| Unobserved | Customs success — the wavefunction never collapsed |
| Observed | Customs encounter — Schrödinger had a bad day |

### State Flags Set
- `ruben_met`: boolean
- `ruben_destination_given`: string
- `ruben_zone_walk_completed`: boolean
- `seed_ritual_completed`: boolean
- `seed_type_purchased`: enum (none / souvenir / premium)
- `suspicious_souvenir_count`: integer
- `customs_encounter_resolved`: boolean
- `customs_outcome`: enum (unobserved / observed)
- `ruben_research_behaviour`: boolean (player named a specific destination before buying — unlocks the longer, better answer)

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. Explaining Frames 1 → 2 → 3 side by side, hand position escalating with qualifier density
2. The window text: "All products comply with Dutch law*" with the asterisk that leads nowhere
3. The quantum cat mascot in a hemp leaf, saying what Ruben legally cannot
4. "NOT FOR GERMINATION" signage stacked three deep in Zone 4
5. The customs checkpoint, bag open, the moment of observation

### Meme Potential
- "I cannot answer that question."
- "I'm not saying don't buy it. I'm saying know what you're buying. Then buy it. Probably."
- "Until observed, everything is fine."
- "The seeds are the most honest product. Everyone knows what they are. Everyone pretends otherwise."
- "That is not a legal protection, it is a bag. But it is sealed."
- "...I'll take two."

---

## 🗣️ Voice Direction

### Accent
Dutch, mid-30s, urban, fluent and relaxed English. Retail-friendly register with an unexpected precision underneath — he uses exact percentages and exact legal terms in a conversational tone, which is what makes the hedges sound like reassurance rather than evasion.

### Tone
- **Welcome**: Genuinely friendly. He is glad you came in and he is about to ask you a slightly awkward question.
- **The destination query**: Casual. It sounds like small talk and it is the single most important question in the shop.
- **The escalating explanation**: Same warmth throughout, increasing precision. The tone never tightens even as the qualifiers stack — that gap is the joke.
- **"I cannot answer that question."**: **Warm. Final.** Both, fully. Not cold, not apologetic, not amused. He will say it identically the tenth time.
- **The seed disclaimer**: Word-perfect and slightly faster than his normal speech, because it is a recital. It should sound learned, not read.
- **The philosophy**: Sincere. He genuinely finds Schrödinger apt and is a little pleased with the shop's name.

### Key Delivery Notes
- **Never shifty. Never evasive. Never a note of "we both know."** The asset doc is explicit: if the staff read as dishonest the satire collapses. Ruben is telling the truth at all times and it is not helping anyone.
- The hedges must sound like care, not like liability management, even though they are both.
- "Probably." at the end of "Then buy it. Probably." is a full beat and it is the funniest word he says.
- He does not wink, smirk, or return a wink. When a customer winks, he says the true thing again.

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

- **HARD CANON: this character is Manager RUBEN. He was formerly drafted as "Manager Daan" and that name is retired.** Daan is the Museum of Questionable Art guard and nobody else, game-wide.
- **Ruben and Yuki must never appear worried, evasive, or shifty in any frame.** Asset-doc constraint. They are being scrupulously truthful and it is not helping. The moment either reads as dishonest, the satire's target shifts from tourist ignorance to shopkeeper deceit and the location breaks.
- **Every statement Ruben makes must be factually accurate**, including the percentages, the EU threshold, the CBD/THC distinction, and the customs pass rates. The shop's comedy is built on a foundation of correct information delivered uselessly. Fact-check the CBD content before ship.
- The three Explaining frames escalate qualifier density through hand position. **The animation is the joke, not the dialogue.** If the frames are drawn as three similar poses, the beat is lost.
- The asterisk on "All products comply with Dutch law*" leads nowhere. This is authored. Do not add a footnote.
- The Quantum Cat Portrait exists so the mascot can say what the staff legally cannot. Use it for any line that would compromise Ruben's scrupulousness — that is what it is for.
- The seed customs outcome must be a genuine 50/50. Not weighted, not narratively determined, not adjusted by player skill. The wavefunction collapse is the location's thesis and it must actually be random.
- The Research Tourist behaviour is mirrorable by the player: naming a specific destination before buying unlocks a measurably longer and better answer from Ruben. This is the shop's one reward for playing it straight and it should not be signposted.
- Crypto: none. The location profile establishes no crypto presence and none is to be added.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Ruben has none. Sovs, card, 8–65 Sovs.
- [x] **NO automatic crypto assumptions** — the location profile explicitly states "no crypto elements: pure quantum legal uncertainty"; do not add any
- [x] **Coins, kiosks, and certificates come from the master pool** — N/A, no crypto at this location
- [x] **The bros are never scam-aware** — there is no scam; Ruben told them everything and they took two anyway
- [x] **Nothing winks** — Ruben structurally cannot wink; the quantum cat mascot exists precisely so nobody has to
- [x] **Focus on city-specific cultural exploitation instead** — the satire is legal gray-zone commerce and willful tourist ignorance

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the joke is tourists who will not check their own country's laws; Dutch tolerance policy is presented as coherent and the shop as compliant
- [x] NPC is savvy entrepreneur, not villain or stereotype — Ruben is honest, informed, fairly priced, and gives more accurate information than any customer wants
- [x] Humour is affectionate mockery, not mean-spirited — nobody is deceived, nobody is harmed, and the worst outcome in the whole chain is a confiscated seed packet
- [x] Drug policy handled without moralising — the satire targets legal confusion and the theatre of plausible deniability, never drug use, drug users, or Dutch policy

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Shamsterdam/npcs/Schrodingers_Souvenir/npc_manager_ruben.md`
- **Registered In**: No `schrodingers_souvenir_npcs.json` exists. **A location JSON roster should be created** (Yuki and the six atmospheric customer NPCs still unprofiled — Wave 2). Registration pending; flagged for the JSON authoring pass.
- **Sprite Sheet**: `npc_ruben_yuki.png` (512×512; 64×96 character frames, 128×128 portraits) — Ruben occupies rows y=0 (qualification), y=96 (transaction/philosophy), portrait at (0,192), counter/utility frames at y=416. Specced in `PNG_Assets/Schrodingers_Souvenir_PNG_Assets.md`, Sprite Sheet 4. Supporting: `npc_schrodingers_customers.png`, `quantum_cat_mascot.png`, `legal_disclaimer_board.png`, `seed_purchase_ritual.png` (UI), `customs_encounter_ui.png`, `wavefunction_collapse.png`.

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — Wave 1 (mechanics-attached NPCs). Sourced from `schrodingers_souvenir.md` + `PNG_Assets/Schrodingers_Souvenir_PNG_Assets.md`. Manager Daan → Manager Ruben rename carried (source file already updated). | Shamsterdam NPC authoring pass |

---

*Template Version 1.1*
