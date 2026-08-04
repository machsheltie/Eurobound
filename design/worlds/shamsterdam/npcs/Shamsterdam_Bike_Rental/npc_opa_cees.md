# NPC Profile: Opa Cees

*"This bike came out of the canal. This one too. And this one. And—"*

## 📋 NPC Identity
- **NPC ID**: `shamsterdam_npc_opa_cees_repair_01`
- **Display Name**: Opa Cees
- **Internal Name**: Cees van der Berg — grandfather, repair station, first of three generations on the floor
- **Role**: Service Provider (Repairs) / Lore Source / Quest Giver / Buff Granter
- **Associated Quest**: `shamsterdam_quest_canal_recovery` ("Canal Recovery Assistant")
- **Primary Location**: Shamsterdam Bike Rental — repair station, visible through the interior doorway, Shamsterdam
- **Secondary Appearances**: Canal Ring Promenade during the Canal Recovery quest (the only time he leaves the workshop, and he does not go in the water)

---

## 🎭 Core Concept

### What He's Actually Doing
Repairing bicycles, as he has for forty-seven years, in a workshop that has become an involuntary museum of tourist failure. The back wall is bikes recovered from the canal — decades of them, mounted and unlabelled. In the corner sit the old blue rental bikes from before the fleet went orange. He fixes what can be fixed, prices it fairly, refuses what cannot be fixed, and mumbles about how tourists cycled in his day. He is completely uninterested in the rental business his son runs eight metres away.

### What Bros Believe
Chadwick has identified Opa Cees as "the soul of the place" and wants footage. Lord Pilsner thinks the canal wall is a themed decoration. Bradley — after being told three separate times that these were real bikes belonging to real tourists — is the only one who looks at the wall properly and goes quiet.

### The Comedy Gap
The canal wall is a body count. The bros read it as set dressing. Opa Cees is not performing rustic wisdom; he is a working mechanic giving a factual account of forty-seven years of the same accident, and the bros have decided this is charming. He gestures at an entire wall of destroyed property and they say "sick."

### The Quiet Underneath It
He does not resent the tourists. He resents the canal. The distinction matters and it is the whole character: the water takes bikes, and he gets them back, one at a time, and he has been getting them back longer than his son has been alive.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | 80+ |
| Build | Wiry, still active. Hands that close on a wrench without hesitation. |
| Height | Shorter than he used to be, taller than the bench |
| Energy | Unhurried, absorbed, entirely occupied |

### Clothing
- **Oil-stained apron, older than most customers**: Canvas, blackened at the front, the ties replaced with different cord at least twice. It is not a costume; it is load-bearing.
- **Wool shirt, sleeves rolled**: Same shirt or six identical shirts, unclear
- **Accessories**: Reading glasses pushed up onto the forehead and forgotten there; a cloth over the shoulder
- **Footwear**: Leather boots, resoled, the workshop floor mapped into them

### Distinguishing Features
- Surrounded by decades of accumulated cycling debris, organised by a system only he holds
- Speaks while working, does not look up, finishes the sentence after the bolt is seated
- The sigh — deep, weary, entirely genuine, and one of the location's signature audio cues
- Hands with grease in the same places as his son's, only forty-seven years further in

### Sprite Notes
Sheet `npc_opa_cees_repair.png` (240×320, 48×64 sprites, 5 rows). He should read as containing forty-seven years of accumulated wisdom and weariness in equal measure. Row 2 — Looking at Canal Wall (2 frames, 0.25 FPS) — is his contemplative default when nobody is talking to him, and the slowest animation in the location. Row 4 — Giving Blessing (3 frames, hands raised) — must not read as mystical; it is a grumpy old man doing a thing he was asked to do. He is framed permanently through the repair-station doorway: visible from the shop floor, background layer, third generation in depth behind Dirk and Anneke.

---

## 🧠 Personality

### Archetype
**The Working Historian** — Cees is not a sage, a mystic, or a repository of folk wisdom. He is a mechanic who has been in one room long enough that the room became an archive. He gives lore because he was there, not because he is dispensing it. He judges silently, fixes competently, and considers the canal a persistent adversary with which he has an ongoing arrangement.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Absorbed in the work | The bike is the conversation partner. You are the interruption, briefly tolerated. |
| Philosophical about bike mortality | Not sad about it. Bikes end. He has a lot of data on how. |
| Can fix nearly anything | And is precise about the "nearly." When he says no, it is genuinely gone. |
| Judges silently | The sigh is the entire verdict and it is comprehensive |
| Territorial about the canal | Forty-seven years of retrieval. It is his, in a way he could not explain and will not try. |

### Internal Monologue
> "The frame is bent at the head tube, which means the tram track, which means they were looking at a telephone. The wheel I can true. The frame I cannot. He will ask me if I can. I will say no. He will ask again in a different way, as if the metal is negotiable. Then he will go and my son will take the deposit and the bike will go on the wall, and in eleven years someone will point at it and say 'what happened to that one' and I will not remember which one it was."

### Motivation
Get the bike back. Get it working if it can work. Get it out of the water if it is in the water. There is no larger project. There has not been one since 1979.

---

## 💬 Dialogue

### Approach/Greeting

**First approach**:
> *(He looks up from a bike. It takes a moment.)*
> "Hmm? Tourist. Looking for repairs, or just looking?"

**Second approach**:
> "Still looking." *(He goes back to the wheel.)* "Fine. Look."

**If the player has damaged a bike**:
> *(He does not look up.)* "I heard the front counter. Bring it here."

### Key Interaction Dialogue — The History

**History, unprompted (first conversation)**:
> "Forty-seven years. I have fixed forty-seven years of tourist mistakes."
> *(He does not stop working.)*
> "It is the same mistake. That is the part nobody believes."

**On the fleet colour**:
> "The rental bikes used to be blue." *(He nods at the corner, where four of them still stand.)* "Then orange became the tourist warning colour. Not my decision. It was correct."

**Assessing a group**:
> "Your group?" *(He looks at all three bros. It takes about two seconds.)* "I give you... three hours before the first one comes back bent."

**If the player asks how he was right about the three hours**:
> "I was not right. I was two hours generous."

### The Canal Wall

*The player examines the back wall. He notices.*

**Opa Cees**:
> "This bike came out of the canal. This one too. And this one. And—"
> *(He gestures at the entire wall. The gesture keeps going. It is a big wall.)*
> "Eight hundred and forty-seven. My son keeps the number on his shirt. I keep the bikes."

**On the canal itself**:
> "The canal takes. The canal gives back. Eventually. Usually bent."

**On the oldest one**:
> "That one is from 1981. English boy. He cried. I gave him a cloth." *(Beat.)* "He never came for the bike."

### Repair Services

**Standard repair**:
> "I can fix this. Twenty-five Sovs. Come back in an hour."

**Beyond repair**:
> "This... this I cannot fix." *(He turns it once in the stand, then leaves it.)* "This is art now. Tragic art."

**If the player pushes**:
> "You can ask three times. The metal will still be bent. It does not know you are asking."

**Flat tyre**:
> "Eight Sovs. Sit down. Do not watch me, it makes it slower."

### Quest Accept — Canal Recovery Assistant

*Triggers on the third interaction, after `history_1` and `canal_wall` have both played.*

> "You keep coming back here. Nobody comes back here. They come to the counter and they leave."
> *(He sets the wrench down. This is significant; he does not set the wrench down.)*
> "The canal has many bikes. Many, many bikes. The city pulls them once a year with a machine and the machine misses more than it takes."
> "You want to help an old man recover some?"

**On accept**:
> "Basement. Left side, behind the blue ones. There is a pole with a hook. It is heavier than it looks and it is exactly as heavy as it looks — both of those are true."
> "Canal Ring Promenade. Three bikes. I will be there. I will not be in the water."

**During the recovery mini-game**:
> "Slow. The hook does the work, not the arm."
> "That is a shopping trolley. Leave it. It has been there since the nineties and it has earned its place."
> "There. Feel that? That is a frame. Do not rush now, this is where they let go."

**On completion**:
> *(He looks at the three bikes on the promenade stones, dripping.)*
> "Three." *(A long pause.)* "Eight hundred and fifty."
> "Thirty Sovs. And a damage waiver on your next rental — do not tell my son, he will tell me it is not mine to give. It is not. I am giving it."

**The Blessing**:
> "You want my blessing? *(He squints.)* Fine."
> *(He raises both hands. It is not solemn. It is a man doing an errand.)*
> "May your wheels stay round and your chain stay oiled."
> *(He picks the wrench back up.)* "That is it. That is the whole blessing. It works about as well as you would expect, which is to say slightly."

### Post-Interaction
> *(Returns to the bike. The wrench turns. He does not say goodbye and never has.)*

### If Player Declines / Alternative Path
**Declines the quest**:
> "Ja." *(He picks the wrench back up. There is no disappointment in it.)* "They stay in the water then. They are patient."

**Player offers to just buy him a drink instead**:
> "I am eighty-three and I am holding a wrench. Think about your offer."

### Callback Dialogue (Return Visits)
**After Tour de Shame completion**:
> "Twenty minutes. Five districts." *(He looks up, properly.)* "In 1974 I did it in fourteen. There were fewer trams. Still. Twenty is not bad."

**After the player has damaged five or more bikes**:
> "You again." *(The sigh. The full one.)* "I am going to put your bikes together on the wall. As a section."

**Late game**:
> "You have been in this workshop more than my granddaughter." *(Beat.)* "Do not tell her that. She will bring me coffee to win it back, and her coffee is terrible."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 08:00–11:59 | Repair station bench | Overnight damage queue. Head down. Least talkative window. |
| 12:00–15:59 | Repair station bench | Working. Most receptive to conversation. Lore lines unlock here. |
| 16:00–18:59 | Repair station / canal wall | Assessing returns. Sighing. The Looking at Canal Wall idle dominates. |
| 19:00–21:00 | Repair station doorway | With Dirk. Counting the fleet. Closing. |
| 21:00–08:00 | Closed | He is 83. The workshop closes when the shop closes. |

### Positioning Notes
- Visible through the interior doorway from the main shop floor at all times — background layer, never blocked
- Requires deliberate interaction to speak to; he will not hail the player, ever
- The Canal Recovery Wall is behind him and in frame for every conversation, which does the environmental storytelling without a line of dialogue
- The vintage blue bikes sit at the edge of frame in the corner, placarded with dates, museum-positioned
- During the Canal Recovery quest he stands on the Canal Ring Promenade stones, above the waterline, holding nothing. He supervises. He does not fish.

---

## 🎒 Inventory / Services

### Repair Services
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| Flat Tire Repair | 8 Sovs | 8 Sovs | While you wait. Do not watch. |
| Chain Fix | 10 Sovs | 10 Sovs | Grease on your clothes guaranteed |
| Brake Adjustment | 12 Sovs | 12 Sovs | "You should have had this done BEFORE" |
| Bent Wheel Realignment | 25 Sovs | 25 Sovs | "How did you even—never mind" |
| Full Damage Assessment | Free | High | Honest, itemised, and the news is never good |
| Beyond Repair Ruling | Free | — | He will not take money to fail. The bike goes to the wall. |

### Buffs Granted
| Item/Service | Source | Duration | Effect |
|--------------|--------|----------|--------|
| Opa Cees's Blessing | Canal Recovery quest complete | Permanent | +5% Navigation in Shamsterdam |
| Opa Cees's Blessing | Platinum Insurance purchase | Rental duration | +5% Navigation in Shamsterdam |
| Free damage waiver | Canal Recovery quest complete | Next rental | One damage event fully waived |
| "Recovered goods" inventory | Canal Recovery quest complete | Permanent access | Random cheap items pulled from the canal over the decades |

### Hidden Details / Easter Eggs
- **The 1981 bike**: Examine the oldest bike on the wall. Placard reads a date and nothing else. Ask Cees about it and you get the English boy and the cloth. It is the only piece of lore in the location with a person attached and it is delivered in nine words.
- **The blue bikes**: Four pre-orange rental bikes in the corner, placarded with dates. Examining all four in one visit triggers a single extra line: "Blue was better. Blue was invisible. That was the problem."
- **The shopping trolley**: During the Canal Recovery mini-game, hooking the trolley three times triggers escalating dialogue and, on the third, a small reward. He calls it "the tenant."
- **The counter discrepancy**: Dirk's name tag counts canal recoveries; Cees counts bikes on the wall. The numbers do not match and have not since 2011. Neither man has raised it.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Dirk van der Berg | Son. Dirk runs the front, Cees runs the back. The division was never negotiated; it simply happened and has held for twenty-two years. |
| Anneke van der Berg | Granddaughter. Brings him coffee sometimes. The coffee is bad. He drinks it. |
| Maarten (De Zilte Waarheid) | Same generation, same district, same forty-year fixture status. They nod. That is the entire relationship and both consider it sufficient. |
| Willem the Eternal Busker (Voetgangerstunnel) | Cees has never been in the tunnel. "Underground is for bicycles and I have enough bicycles." |
| Officer van den Berg (Bike Crossing) | Same surname, no confirmed relation, and unlike Dirk, Cees will not answer the question at all. |

### Territory / Social Dynamics
- The repair station is absolutely his. Dirk does not do damage assessments back here; he brings the bike to the doorway and hands it over.
- Three generations staged in depth: Anneke (front, warm), Dirk (middle, calibrated), Cees (back, unbothered). Commercial interest decreases with depth; honesty increases.
- Cees is the only member of the family with zero interest in the upsell. He has never quoted an insurance tier and would not know the prices.

---

## 🔄 Recurring Appearances

### Within Shamsterdam
- **Interaction 1**: Greeting + `history_1`. He is a background fixture who happens to talk.
- **Interaction 2**: The canal wall. The location's tone shifts permanently at this beat.
- **Interaction 3**: Canal Recovery Assistant offered. He puts the wrench down.
- **Post-quest**: Blessing granted, recovered-goods inventory unlocked, the running bike count becomes a live number he references
- **Every damaged return, forever**: The sigh

### In Other Cities
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| — | — | Cees does not travel. He has been in this room since 1979 and will be in it at the end of the game. | — |

### Evolution Through Game
He does not warm up, exactly. He becomes *available*: the first conversations are grudging interruptions of the work, and by the late game he sets the wrench down when the player enters. That gesture — the wrench going down — is the entire arc and it is used exactly twice in the whole game.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| repairing_bike | 4 frames, 1 FPS, loop. Active work at the stand. | 60% |
| looking_at_canal_wall | 2 frames, 0.25 FPS, loop. Contemplating the archive. Slowest animation in the location. | 22% |
| examining_damage | 3 frames, 0.5 FPS. Assessing the worst. | 12% |
| glasses_forget | Pushes glasses up, forgets them, looks for them | 6% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| sighing_at_damage | 2 frames, 0.5 FPS. Any major damage return. Carries the location's signature audio cue. |
| giving_blessing | 3 frames, hands raised. Quest completion or Platinum Insurance purchase. |
| wrench_down | Canal Recovery quest offer; late-game player entry. Used twice in the game. |
| gesture_at_wall | The canal wall line. The gesture is deliberately too long for the frame. |

### Sprite States
| State | When Used |
|-------|-----------|
| cees_workbench | Default, repair station |
| cees_promenade | Canal Recovery quest only, standing on the stones above the waterline |
| cees_high_contrast | Accessibility outline variant marking him as interactive |

---

## 🎯 Quest Integration

### Primary Quest: Canal Recovery Assistant
- **Quest**: Canal Recovery Assistant (`shamsterdam_quest_canal_recovery`)
- **Role**: Quest Giver
- **Trigger**: Third interaction with Opa Cees, after the `history_1` and `canal_wall` dialogue beats have both fired. Not offered at the counter and not offered by Dirk.
- **Stages**:
  1. Speak with Opa Cees about "the old days"
  2. Retrieve the hook pole from the basement (behind the blue bikes)
  3. Travel to Canal Ring Promenade
  4. Hook and recover 3 bikes (timing mini-game)
  5. Return the equipment and the bikes
- **Outcome**: "Canal Fisher" achievement, 30 Sovs, one free damage waiver on the next rental, Opa Cees's Blessing (+5% Navigation, permanent), access to the "recovered goods" inventory

### Quest Gate Function
Cees gates the permanent Navigation blessing and the recovered-goods vendor. He also gates the location's emotional register — a player who never walks through the repair-station doorway experiences Shamsterdam Bike Rental purely as an insurance joke. The gate is attention, not currency: he cannot be bought, hurried, or unlocked with money.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Hook Pole | Stage 2 | No | Quest item; returned at completion |
| Opa Cees's Blessing | Quest complete | Yes | +5% Navigation in Shamsterdam |
| Free Damage Waiver | Quest complete | One use | Next rental's damage event waived in full |
| Recovered Goods access | Quest complete | Yes | Random cheap-item vendor: bells, lights, one bent key, a 1997 tram token |

### State Flags Set
- `cees_met`: boolean
- `cees_interaction_count`: integer (quest offer fires at 3)
- `cees_history_heard`: boolean
- `cees_canal_wall_seen`: boolean
- `canal_recovery_offered`: boolean
- `canal_recovery_complete`: boolean
- `cees_blessing_acquired`: boolean
- `cees_trolley_hooks`: integer (easter egg counter)

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. The canal recovery wall in full — decades of bikes, seaweed, rust, no captions
2. The four blue bikes in the corner with their date placards
3. Cees mid-gesture at the wall, the gesture still going
4. Three recovered bikes dripping on the promenade stones at dusk, Cees standing dry beside them
5. The Blessing animation, which looks exactly as unmagical as it is

### Meme Potential
- "This bike came out of the canal. This one too. And this one. And—"
- "This is art now. Tragic art."
- "I give you... three hours before the first one comes back bent."
- "I was not right. I was two hours generous."
- "I am eighty-three and I am holding a wrench. Think about your offer."

---

## 🗣️ Voice Direction

### Accent
Dutch, older generation, slower cadence than his son. Sentences trail rather than land. He does not use contractions and does not soften — but where Dirk is clipped, Cees is simply unhurried, because he has decided how long a sentence takes and that is how long it takes.

### Tone
- **Working**: Half-attention. Most of him is on the bolt.
- **The canal wall**: Factual. Not elegiac. He is reading out an inventory that happens to be sad.
- **The 1981 line**: Nine words, no weight added. The listener supplies the weight.
- **The quest offer**: The only time he has the player's full attention and gives his own. Wrench down.
- **The blessing**: Faintly annoyed. He was asked, so he is doing it.

### Key Delivery Notes
- Never mystical. Never twinkly. The instant Cees sounds like a wise old man, the character collapses into cliché.
- The sigh is a full, audible, recorded asset — not a text beat. It is the location's signature sound and it must be worth the design attention.
- "And—" in the canal wall line cuts off because the gesture takes over. Do not let him finish it.
- He never says goodbye. Do not record a farewell line.

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

- **HARD CANON: this character is Opa CEES. He was formerly drafted as "Opa Willem" and that name is retired.** Willem is the Voetgangerstunnel busker and nobody else, game-wide. Any remaining "Opa Willem" string in JSON, spawn tables, or asset names is a rename miss and must be corrected — see the Development Status note below regarding the legacy `npc_id` and `spawn_points` key.
- He must never hail the player. Requires deliberate interaction, always. If he calls out to the player from the doorway, the entire "nobody comes back here" quest premise breaks.
- The quest fires on interaction count, not on rental count. A player who never rents a bike can still complete Canal Recovery Assistant. This is intentional.
- The wrench-down gesture is used exactly twice in the game: the quest offer, and the late-game entry line. Do not reuse it for flavour.
- The recovered-goods inventory should be genuinely cheap and genuinely useless (bells, a bent key, one 1997 tram token that is also a Voetgangerstunnel collectible). It is a reward of texture, not power.
- Dirk's canal counter and Cees's wall count must NOT be reconciled in code. The discrepancy is authored.
- Do not give him a death, an illness, or a retirement arc. He is 83 and he is fine and he is still there in the epilogue.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Cees has none. Sovs, in cash, quoted to the Sov.
- [x] **NO automatic crypto assumptions** — he has been in this workshop since 1979 and does not operate the card machine
- [x] **Coins, kiosks, and certificates come from the master pool** — N/A, no crypto at this location
- [x] **The bros are never scam-aware** — there is no scam; Chadwick is filming a body count and calling it soul
- [x] **Nothing winks** — Cees does not know he is poignant and would object to the suggestion
- [x] **Focus on city-specific cultural exploitation instead** — the satire is tourists reading real consequences as atmosphere

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the joke is the bros mistaking an archive of their own kind's failures for decoration
- [x] NPC is savvy entrepreneur, not villain or stereotype — Cees is a fair, skilled tradesman who refuses money for work he cannot do
- [x] Humour is affectionate mockery, not mean-spirited — he is dignified throughout, his skill is real, and the game rewards players who take him seriously
- [x] Age is portrayed with competence, not frailty — he is 83, sharp, working, and the best mechanic in the district

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Shamsterdam/npcs/Shamsterdam_Bike_Rental/npc_opa_cees.md`
- **Registered In**: `shamsterdam_bike_rental_npcs.json` — Yes. **Legacy `npc_id` was `shamsterdam_npc_opa_willem_repair_01` with `spawn_points` key `opa_willem`, both leftovers from the pre-rename draft. Corrected in this pass to `shamsterdam_npc_opa_cees_repair_01` / `opa_cees` to match `shamsterdam_bike_rental.md` and the canon one-name rule.** `full_profile` path added.
- **Sprite Sheet**: `npc_opa_cees_repair.png` (240×320, 48×64 sprites, 5 animation rows) — specced in `PNG_Assets/shamsterdam_bike_rental_png_assets.md`, Sprite Sheet 5. Supporting: `repair_station_sprites.png` (Canal Recovery Wall, Workbench, Vintage Bikes Corner, Parts Shelves).

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — Wave 1 (mechanics-attached NPCs). Sourced from `shamsterdam_bike_rental.md` + `PNG_Assets/shamsterdam_bike_rental_png_assets.md` + `shamsterdam_bike_rental_npcs.json`. Legacy `opa_willem` identifiers corrected to `opa_cees` per canon one-name-per-character rule. | Shamsterdam NPC authoring pass |

---

*Template Version 1.1*
