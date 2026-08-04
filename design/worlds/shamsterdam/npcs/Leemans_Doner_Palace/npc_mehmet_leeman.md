# NPC Profile: Mehmet "The Meat Architect" Leeman

*"Chicken is for children. But okay. Your döner, your choice."*

## 📋 NPC Identity
- **NPC ID**: `shamsterdam_npc_mehmet_leeman_01`
- **Display Name**: Mehmet
- **Internal Name**: Mehmet "The Meat Architect" Leeman — owner, Leeman's Döner Palace, arrived from Istanbul 1989, opened 1992
- **Role**: Vendor / Owner / Silent Judge / Pronunciation Gatekeeper / Community Pillar
- **Associated Quest**: "The Great Döner Debate: International Expansion" (Shamsterdam entry #1)
- **Primary Location**: Leeman's Döner Palace — behind the carving station, late-night district, Shamsterdam
- **Secondary Appearances**: Referenced at The Tolerance Hostel ("Wolf"/Kevin claims a connection: "Tell him Wolf sent you"); referenced at De Groene Gids as the munchies-pipeline terminus

---

## 🎭 Core Concept

### What He's Actually Doing
Making döner. Correctly, at the same standard, for thirty-two years, at noon and at 4 AM without variation. Three meat towers, fresh bread baked on the premises every morning by his wife to the same 1992 recipe, house-made garlic sauce, and no seats — because döner is fuel and you do not sit down with fuel. He is not performing gruffness; he is working, and conversation is a thing that happens adjacent to the work.

### What Bros Believe
That the meat towers are HYPNOTIC (Chadwick, filming). That ordering the Triple Tower proves something (Lord Pilsner, "because I'm not a CHILD"). That Mehmet dislikes them (all three, incorrect). Bradley says "Sir, your craft is remarkable" and receives "...okay. Enjoy döner," and interprets this as a rebuff, and is wrong — it is the highest first-visit response available.

### The Comedy Gap
Mehmet appears disapproving and is actually pleased you are eating his döner. The bros spend the entire transaction trying to earn something they were given at the door. The satire is on tourist ordering incompetence and the theatre of trying to impress a man who is simply waiting for you to say which meat. The food is genuinely excellent and this is never the joke.

### The Pronunciation Beat
Ordering for the first time triggers a pronunciation mini-game on the word "döner." Four outcomes: Perfect (a single nod, slight respect, no comment), Acceptable (standard service, nothing said), Tourist ("...doner. Okay. I understand."), Catastrophic ("You want... what? Show me on menu."). He judges the attempt, not the person, and he serves you either way.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | 50s |
| Build | Forearms built by carving millions of döners. Everything else is unremarkable and that is correct. |
| Height | Average |
| Energy | Economical, watchful, entirely occupied |

### Clothing
- **Traditional döner chef attire**: White coat, döner-red apron accents (#C41E3A), sleeves pushed up permanently
- **Paper cap**: Worn correctly. Has been worn correctly since 1992.
- **Accessories**: The carving knife, which lives in his hand; a cloth over the shoulder for the blade
- **Footwear**: Kitchen shoes, non-slip, replaced on a schedule

### Distinguishing Features
- Weathered hands. Knowing eyes. A moustache that has seen everything.
- Evaluates the customer *before* they speak — the Judging animation fires ahead of the order input, and this is the joke: he has already assessed you
- The eyebrow. Judging Frame 2 is one eyebrow and that is the entire animation.
- Never stops working during conversation. The blade continues. The tower turns.

### Sprite Notes
Sheet `npc_mehmet_elif.png` (512×512; 64×96 character frames, 128×128 portraits). Mehmet Idle at (0,0); Carving Frames 1–4 at (64,0)–(256,0), which loop independently of order state so the tower is always being worked between customers; Judging Frames 1–2 at (320,0)/(384,0) — **frame 2 is one eyebrow, that is the whole animation**; Approving at (448,0), rare and meaningful. Reaction row at y=96: Wrapping, Presenting Bread, Sauce Warning, Chicken Disappointment (*not anger — something quieter, worse*), Pronunciation Perfect, Pronunciation Catastrophic, Pointing at Menu, Debaucheryville Rant. Portraits at y=192: Dialogue (weathered hands out of frame, knowing eyes) and Rare Approval (the Mehmet Paradox visible — he is pleased). **Judging frames must trigger before the player's order input.** He evaluates you first. That is the joke.

---

## 🧠 Personality

### Archetype
**The Master Who Does Not Explain** — Mehmet has spent thirty-two years perfecting one thing and has no interest in narrating it. He answers what he is asked in the minimum number of words, judges the order silently, serves it correctly, and takes the money at the end as is tradition. The gruffness is not a wall; it is an economy. He has twenty döners an hour to make.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Economical past conversation | Every sentence is the shortest version of itself |
| Deeply knowledgeable | Thirty-two years of specifics about meat, rotation speed, bread, and marination |
| Judges the order, serves anyway | The chicken face is real. The chicken is still made properly. |
| Fiercely partisan about döner geography | "Debaucheryville knows NOTHING." He will expand on this. It is the one topic that gets him talking. |
| Quietly delighted by effort | A correct pronunciation, a finished Triple Tower, a returning face. Each earns exactly one line. |

### Internal Monologue
> "The tall one has been reading the board for forty seconds. There are four items. He will order the Triple Tower because the tall ones always order the Triple Tower, and he will order it in a voice that is asking me a question. The quiet one will order veal and say something polite that I will not know how to answer. This is fine. They will eat, they will be surprised, and for the rest of their lives every döner will be worse than this one. That is the service. That is the whole service. The bread is ready at six."

### Motivation
The craft, the legacy, and the shop. His father made döner. His father's father made döner. His daughter Elif is studying business and will probably take over. He has not missed a day since 1992 and the reason is that the shop opens whether or not he feels like it, which is the only philosophy he has and he would not call it one.

---

## 💬 Dialogue

### Approach/Greeting

**First visit** *(Judging animation fires before the player can speak)*:
> "Veal, chicken, or mixed?"
> *(No greeting. The question is the greeting.)*

**Return visit (3+)**:
> *(He is already carving before the player reaches the counter. He does not look up.)* "Same."

**Peak hour, 3 AM**:
> "Next." *(A pause.)* "You are the fifth group tonight who came from the same door. It is a good door for me."

### The Pronunciation Challenge (First Order)

**Perfect**:
> *(A single nod. No comment. He begins carving.)*
> *(Later, unprompted, while wrapping:)* "You pronounced it correctly. ...you practice?" *(Beat.)* "Okay. This I respect."

**Acceptable**:
> *(Nothing. Standard service. This is a pass.)*

**Tourist**:
> "...doner. Okay. I understand."
> *(He understands. He is telling you that he understands. This is the whole rebuke.)*

**Catastrophic**:
> "You want... what?"
> *(Pointing at Menu animation.)*
> "Show me on menu. The menu has pictures. This is why it has pictures."

### Key Interaction Dialogue — Ordering

**Veal**:
> "Good choice."

**Chicken**:
> "Chicken?" *(Chicken Disappointment animation. Not anger. Something quieter.)* "...chicken is for children. But okay. Your döner, your choice."

**Mixed**:
> "Mixed? You can't decide." *(He is already carving both.)* "The mixed is good. Covers all possibilities."

**Asked whether there is lamb**:
> "You can't decide? Mixed. But lamb is better." *(Beat.)* "We don't have lamb tonight."

**The Triple Tower (8 Sovs)**:
> "The Triple Tower? You have big appetite. Or big problems." *(He reaches for the largest bread.)* "Either way, I help."

**Just bread (2 Sovs)**:
> "You came here for... bread?"
> *(He gives it to them. It is excellent bread. He is genuinely confused.)*

### Sauce

**Extra garlic**:
> "Extra garlic? Okay." *(Sauce Warning animation.)* "You plan to be alone tonight. I don't judge."

**Hot sauce**:
> "Hot sauce? Turkish hot. Not tourist hot. You understand?" *(He adds it.)* "...you'll understand soon."

**No sauce**:
> "No sauce?" *(A pause longer than the chicken pause.)* "...no sauce. This is unusual. But okay."

### The Craft (Rare, Only If Asked Directly)

> "The secret is the bread. Always the bread. Also the meat. And the sauce." *(Beat.)* "Okay, everything is secret."

> "Fresh bread every morning. My wife makes. Since 1992. Same recipe. Why change perfection?"

> "The meat rotates slowly. This is important. Fast rotation? Burned outside, raw inside. Patience."

> "Thirty-two years I make döner. The meat knows when you respect it."

> "Fast food means food that is fast. Not food that is slow. You eat. You go. Life continues."

### The Extended Philosophy (Rare Moments, Quiet Hours Only)

> "1992 I open. Port-city man say 'nobody wants Turkish food here.' Now? Three meat towers. Twenty döners an hour. Port-city man is wrong."

> "My father made döner back home. His father made döner. My daughter will make döner. This is legacy."

> "You eat standing because döner is fuel. You don't sit with fuel. You use it and go."

> "The garlic? The garlic is love. If you can't handle garlic, you can't handle love."

> "I see you every city. Different face, same hunger. 3 AM, everyone is same. Everyone needs döner."

### The Great Döner Debate

> "Thirty-two years I make döner. You think Debaucheryville knows döner?"
> *(Debaucheryville Rant animation.)*
> "Debaucheryville knows NOTHING."

> "Shamsterdam, the port city — these know döner. Because we are here. We bring the knowledge."

**On the debate stakes**:
> "You tell them Debaucheryville is better? You don't come back."
> *(He is not joking and he is also not angry. It is a policy.)*
> "I remember faces."

### Rare Approval

**Triple Tower finished**:
> "You finish The Triple Tower? Good. You have warrior spirit."
> *(Warrior Nod animation.)*
> "Come back."

**"Wolf sent me" (Tolerance Hostel cross-reference)**:
> *(He stops carving. This is significant.)*
> "Wolf." *(A long look.)* "Kevin. His name is Kevin. He has told you Wolf."
> *(He resumes.)*
> "He has been here every year for eleven years. He is a good customer and he is not called Wolf."
> *(Beat.)*
> "Tell him I said Kevin."

### Post-Interaction
> *(Handing Döner animation.)* "Enjoy döner."
> *(That is it. There is no farewell beyond this and there has never been one.)*

### If Player Declines / Alternative Path
**Player asks about kapsalon**:
> "No kapsalon. Go to Wim for that." *(He points at the handwritten sign that says exactly this.)* "He is good. Different. He puts cheese." *(Beat.)* "Cheese is a decision."

**Player asks what's in it**:
> "Meat. Bread. Sauce. Salad." *(He does not consider this evasive. He considers it complete.)*

**Player leaves without ordering**:
> *(He does not react. Next customer. The blade continues.)*

### Callback Dialogue (Return Visits)
**Fifth visit ("Regular" status)**:
> *(He nods once as the player enters. This is a first. He has never done this before.)*

**After Kapsalon Koning**:
> "You have been to Wim." *(He can tell. He does not explain how.)* "Good. He is a good man. His food is a lot of food." *(Beat.)* "This is not criticism. It is a measurement."

**After the Great Döner Debate resolves in Shamsterdam's favour**:
> "You said it out loud." *(The Rare Approval portrait.)* "In front of people. Okay." *(He hands over a döner nobody ordered.)* "This one is not on the till."

**Late game**:
> "You. Every week now." *(He is already building it.)* "You will go home and it will be bad there. I am sorry. There is nothing I can do about that."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 06:00–10:59 | Kitchen (bread) | Not open. His wife bakes; he preps the towers. Marination checked. |
| 11:00–17:59 | Carving station | Daytime service. Locals, cab drivers, workers. The philosophy lines are available here. |
| 18:00–00:59 | Carving station | Evening build. Elif arrives for the night shift and the register. |
| 01:00–04:00 | Carving station | **Peak.** Post-club. Twenty döners an hour. Minimum words, maximum output. |
| 04:00–05:00 | Carving station | Last hour. Quietest. Best conversations. |
| 05:00–06:00 | Closed | Blade cleaned. Towers stripped. Six hours until it all starts again. |

### Positioning Notes
- Behind the carving station, framed by the three rotating meat towers, visible from the street through the front window
- The standing counter runs along the window; there are no seats and there never will be
- Elif works the register at his left elbow; the two of them cover the whole operation without either crossing the other's path
- The handwritten "NO KAPSALON. Go to Wim for that." sign is in frame in every counter conversation
- He never leaves the station during service. Not once.

---

## 🎒 Inventory / Services

### Menu
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Döner (Veal) | 6 Sovs | 6 Sovs | +30 HP. "Good choice." |
| Döner (Chicken) | 5 Sovs | 5 Sovs | +25 HP. "...okay." |
| Döner (Mixed) | 5 Sovs | 5 Sovs | +28 HP. "Indecisive. But okay." |
| **The Triple Tower** | 8 Sovs | 8 Sovs | +40 HP, +15 SP. Garlic Aura, possible Meat Sweats. "You are hungry. I respect this." |
| Extra Garlic Sauce | +1 Sov | 0.50 Sovs | +5 HP, Garlic Aura extended. "You want to be alone tonight?" |
| Extra Hot Sauce | +1 Sov | 0.50 Sovs | +5 HP, −5 HP delayed. Fire Breath. "Turkish hot. Not tourist hot." |
| Just Bread | 2 Sovs | 2 Sovs | +10 HP, Disappointment. "You came here for... bread?" |
| Drink (Ayran) | 2 Sovs | 2 Sovs | +10 HP, Cooling. "Good with döner. Traditional." |

### Status Effects Applied
| Effect | Source | Duration | Result |
|--------|--------|----------|--------|
| Garlic Aura | Any döner; extended by extra garlic | 1–3 hours | NPCs maintain 20% larger conversation distance. Stacks with repeat consumption. |
| Meat Sweats | Triple Tower or excessive consumption | 30 minutes | +10% HP regen, −10% Speed. Slight sprite shimmer. |
| Fire Breath | Extra hot sauce | Variable | Turkish hot. Not tourist hot. |

### Hidden Details / Easter Eggs
- **The bread**: Examine the bread display. Baked on the premises, daily, by Mehmet's wife, to the 1992 recipe. She is never seen. She is referenced exactly twice and both times with total respect.
- **"Wolf sent me"**: Cross-location. Say it and Mehmet reveals that Wolf's name is Kevin, that he has been coming for eleven years, and asks you to tell him so. The Tolerance Hostel's veteran backpacker persona does not survive contact with a man who keeps records.
- **The lamb**: He mentions lamb is better every time mixed is ordered, and every time, they don't have lamb tonight. Ask on forty separate visits: they never have lamb tonight.
- **Rotation speed**: Examine a meat tower. The examine text is a short, correct, genuinely informative note on why slow rotation matters. Mehmet did not write it. Elif did.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Elif | Daughter. Night shift, register, customer interface. Studying business. Will probably take over. He has never said so. |
| Mehmet's wife | Bakes the bread daily since 1992. Never appears on screen. Referenced twice, both times with total respect. Do not stage her. |
| Big Wim (Kapsalon Koning) | Down the street. Explicit, warm, mutual rivalry. Leeman's board reads "NO KAPSALON. Go to Wim for that." Wim's line: "Mehmet down the street? Good man. Different style. No cheese. His loss." |
| "Wolf" / Kevin (The Tolerance Hostel) | Eleven-year customer who tells hostel guests to say "Wolf sent you." His name is Kevin. Mehmet would like this corrected. |
| Budtender Bas (De Groene Gids) | Munchies pipeline. Mehmet identifies Bas's customers on sight and has a phrase for it: "tourist eyes." |
| Counter Worker Anouk (FEBO Automat) | The other late-night option. Döner versus kroket. No hostility; a category difference. |
| Rival döner vendors (Debaucheryville, Publandia) | The Great Döner Debate. He takes this VERY seriously and has a policy about it. |

### Territory / Social Dynamics
- Positioned deliberately: next to a tram stop, across from a club exit. He chose this corner in 1992 and it has been correct ever since.
- Mehmet and Wim are the two poles of the late-night ecosystem and both explicitly direct traffic to the other. The signs on both walls say so.
- The standing-only policy is a stated philosophy, not a cost saving, and he will explain it if asked once.

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **First visit**: Judging animation fires before the order. Pronunciation challenge. The chicken face, if earned.
- **Visits 2–4**: Order recognition builds. Sauce warnings. The craft lines unlock in quiet hours.
- **Fifth visit**: "Regular" status. He nods when the player enters. First time he has ever done this.
- **Post-Kapsalon-Koning**: The Wim acknowledgement. "It is not criticism. It is a measurement."
- **Post-Debate**: The free döner. Not on the till. Not discussed.

### In Other Cities
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| Debaucheryville | — | Referenced as the debate rival. Mehmet has never been. | "Debaucheryville knows NOTHING." |
| Publandia | — | Referenced in the Great Döner Debate confrontation chain | "They wrap their shame in bread." (rival's line, not his) |

Mehmet does not travel. He has not missed a day since 1992.

### Evolution Through Game
The arc is subtraction. He starts by asking what you want, then stops asking, then starts building before you arrive. Each stage removes a sentence. The endpoint is a nod at the door and a döner already in progress, and it is the warmest thing in the location precisely because nothing is said.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| mehmet_carving (4 frames) | Blade to tower, meat falling, second pass, blade wipe. **Loops independently of order state** — the tower is always being worked. | 60% |
| mehmet_wiping_knife | Between-order ambient | 18% |
| mehmet_tower_check | Patience, slow rotation, correctness | 15% |
| mehmet_silent_judgment_hold | Held frame for dialogue pauses | 7% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| mehmet_judging (2 frames) | **Fires BEFORE the player's order input.** Frame 2 is one eyebrow. |
| mehmet_chicken_disappointment | Chicken ordered. Not anger. Something quieter. Worse. |
| mehmet_sauce_warning | Extra garlic requested |
| mehmet_pronunciation_perfect | Correct pronunciation. Single nod, no comment. |
| mehmet_pronunciation_catastrophic | Failed pronunciation. "Show me on menu." |
| mehmet_pointing_at_menu | The menu is right there. It has pictures. |
| mehmet_debaucheryville_rant | Great Döner Debate topic raised |
| mehmet_approving / warrior_nod | Triple Tower finished, or debate resolved in Shamsterdam's favour. Rare. |
| mehmet_wrapping | Foil fold, single motion, thirty-two years |
| mehmet_presenting_bread | "The secret is the bread." |

### Sprite States
| State | When Used |
|-------|-----------|
| mehmet_station | Default, carving station |
| mehmet_portrait | Dialogue close-up, 128×128 |
| mehmet_portrait_approval | Rare Approval portrait — the Mehmet Paradox visible |
| mehmet_high_contrast | Accessibility outline variant marking him as interactive |

---

## 🎯 Quest Integration

### Primary Quest: The Great Döner Debate: International Expansion
- **Quest**: The Great Döner Debate: International Expansion
- **Role**: Vendor / Debate Stakeholder
- **Trigger**: Eating here counts as **Shamsterdam entry #1** (Kapsalon Koning is #2)
- **Requirement**: Consume any döner; the opinion is recorded for the final verdict
- **Mehmet's Stake**: He takes it extremely seriously. Ranking Debaucheryville above Shamsterdam is a permanent bar from the shop. He remembers faces.
- **Outcome**: Ranking Shamsterdam first produces the game's only free döner and the Rare Approval portrait

### The Döner Achievement Track
| Achievement | Trigger |
|-------------|---------|
| Initiated | First visit |
| Warrior | Triple Tower consumed |
| Respectful | Pronounced correctly |
| Regular | 5 visits — Mehmet nods in recognition |
| Brave or Foolish | Survived Turkish hot |

### Quest Gate Function
Mehmet gates one of the two Shamsterdam samples required by the Great Döner Debate; the quest cannot resolve without eating here. He also enforces a soft social gate: ranking a rival city above Shamsterdam locks the shop for the remainder of the game. This is the only permanent vendor lockout in the district and it is entirely the player's choice.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Döner (any) | Any | Consumable | HP restore; Garlic Aura |
| Triple Tower | Any | Consumable | +40 HP, +15 SP, Garlic Aura, Meat Sweats risk. "Warrior Spirit" badge on completion. |
| The free döner | Debate resolved for Shamsterdam | One-time | Not on the till. Not discussed. |
| Kevin's real name | "Wolf sent me" | Information | Deflates the Tolerance Hostel's veteran-backpacker persona permanently |

### State Flags Set
- `mehmet_met`: boolean
- `mehmet_visit_count`: integer (Regular status at 5)
- `mehmet_pronunciation_result`: enum (perfect / acceptable / tourist / catastrophic)
- `mehmet_chicken_ordered`: boolean
- `mehmet_triple_tower_completed`: boolean
- `mehmet_wolf_line_used`: boolean
- `doner_debate_shamsterdam_1`: boolean
- `mehmet_locked_out`: boolean (ranked a rival city first)

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. The three meat towers in the window at 3 AM, rotating, beacon in the dark
2. The Judging eyebrow — Frame 2, one eyebrow, fired before the player said anything
3. The Chicken Disappointment face
4. "NO KAPSALON. Go to Wim for that." handwritten and taped to the glass
5. The Rare Approval portrait — proof it exists, posted as evidence

### Meme Potential
- "Chicken is for children. But okay."
- "Turkish hot. Not tourist hot. ...you'll understand soon."
- "You want to be alone tonight? I don't judge."
- "Debaucheryville knows NOTHING."
- "You came here for... bread?"
- "Tell him I said Kevin."

---

## 🗣️ Voice Direction

### Accent
Turkish, thirty-seven years in the Netherlands, Istanbul origin. Fluent functional Dutch and English, both stripped to essentials. He drops articles and pronouns where meaning survives without them — not broken speech, compressed speech. He has been making the same sentences for three decades and has removed everything that was not carrying weight.

### Tone
- **Ordering**: Brisk. Not unfriendly. He has twenty an hour to make and every second in the sentence is a second not in the bread.
- **Chicken**: Genuine, quiet disappointment. Not performed. Not a bit. He would have preferred veal for you.
- **Sauce warnings**: Deadpan, faintly amused, entirely sincere as a warning
- **The craft lines**: Slower. This is the only register where he uses more words than necessary and it should be noticeably different.
- **Debaucheryville**: The one place he raises his voice. Genuine heat. He has strong feelings about döner geography and they are not ironic.
- **Rare Approval**: Four words maximum. It is worth more because everything else is worth fewer.

### Key Delivery Notes
- The Mehmet Paradox must be audible: he sounds disapproving and is, underneath, pleased you are here. Do not let either half win.
- "...okay" is a full sentence and does a great deal of work. It should never sound like a shrug.
- "Enjoy döner" is the entire farewell. No warmth added, no warmth withheld.
- "Tell him I said Kevin" — flat, and completely devastating. Do not point it.
- Never let him be rude to a customer. He judges the order. He has never once judged a person out loud.

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

- **The Judging animation must fire BEFORE the order input.** This is specified in the asset doc and it is the character's central joke: he has assessed you before you opened your mouth. If it fires after, the beat is dead.
- Carving Frames 1–4 loop independently of order state. The tower must always be being worked. If Mehmet ever stands idle behind an untouched tower, the shop reads as closed.
- The food is never the joke. Leeman's döner is genuinely, canonically the best the bros have ever eaten and the game says so out loud through Lord Pilsner. The satire is entirely on the ordering.
- The pronunciation mini-game must have a genuinely achievable "Perfect" tier. If it is unwinnable, Mehmet becomes a gatekeeper rather than a judge and the tone shifts wrong.
- The Debaucheryville lockout is permanent for the save. Do not add a redemption path. "I remember faces" is a policy, not a threat, and it should hold.
- Mehmet's wife is referenced twice and never staged. Do not build her a sprite, a name, or a scene. The bread is her presence.
- The "Wolf sent me" beat requires the Tolerance Hostel visit first. Kevin's real name should not be obtainable any other way.
- Canon check: Mehmet appears once in the game. Elif appears once. Neither name may be reused.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Mehmet has none. Sovs, cash, 2–8 Sovs, payment at the end as is tradition.
- [x] **NO automatic crypto assumptions** — a standing-room döner counter open since 1992 takes cash
- [x] **Coins, kiosks, and certificates come from the master pool** — N/A, no crypto at this location
- [x] **The bros are never scam-aware** — there is no scam; Bradley thanks him sincerely and misreads the reply as a rebuff
- [x] **Nothing winks** — Mehmet never signals that the judgment is affectionate; the player has to earn that read across five visits
- [x] **Focus on city-specific cultural exploitation instead** — the satire is tourist ordering incompetence and 3 AM decision-making

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the joke is bros trying to impress a working man; Turkish immigrant food culture is celebrated explicitly and at length, and the food is stated to be genuinely the best in the game
- [x] NPC is savvy entrepreneur, not villain or stereotype — Mehmet is a master craftsman running a thirty-two-year business, training his daughter to inherit it, and directing customers to his competitor for what his competitor does better
- [x] Humour is affectionate mockery, not mean-spirited — his judgment is warm underneath, his approval is earnable, and the "1992, nobody wants Turkish food here — port-city man is wrong" line is a straight triumph with no irony attached

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Shamsterdam/npcs/Leemans_Doner_Palace/npc_mehmet_leeman.md`
- **Registered In**: No `leemans_doner_palace_npcs.json` exists. **A location JSON roster should be created** (Elif and the five atmospheric customer NPCs still unprofiled — Wave 2). Registration pending; flagged for the JSON authoring pass.
- **Sprite Sheet**: `npc_mehmet_elif.png` (512×512; 64×96 character frames, 128×128 portraits) — Mehmet occupies rows y=0, y=96, portraits at y=192, utility frames at y=416. Specced in `PNG_Assets/Leemans_Doner_Palace_PNG_Assets.md`, Sprite Sheet 4. Supporting: `npc_leemans_customers.png` (The 3 AM Congregation), `three_meat_towers.png`, `pronunciation_challenge.png` (UI).

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — Wave 1 (mechanics-attached NPCs). Sourced from `leemans_doner_palace.md` + `PNG_Assets/Leemans_Doner_Palace_PNG_Assets.md` + `the_tolerance_hostel.md` (Wolf/Kevin cross-reference) + `Design/Quests/greatdonerdebate.md`. | Shamsterdam NPC authoring pass |

---

*Template Version 1.1*
