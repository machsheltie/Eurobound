# NPC Profile: The UV Man

*"Everything is real until the light says otherwise. Then it is still something. It is just not what it said."*

## 📋 NPC Identity
- **NPC ID**: `debaucheryville_npc_uv_man_01`
- **Display Name**: The UV Man
- **Internal Name**: The UV Man — Shadow Exchange counterfeit-detection specialist. No other name is on record and none has ever been asked for
- **Role**: Item Tester (fee-based authentication) / Tool Vendor (Pocket UV Wand) / Barter Window Operator
- **Associated Quest**: None owned. His Pocket UV Wand is a tool-distribution node that enables counterfeit detection at other locations across the city
- **Primary Location**: Shadow Exchange, Debaucheryville — the UV detection station, one arch along from the main counter
- **Secondary Appearances**: None. The wand travels; he does not

---

## 🎭 Core Concept

### What He's Actually Doing
Standing at a purple-lit station in a repurposed wine cellar, running a handheld UV wand over currency, wristbands, tickets, and whatever else someone slides at him, and telling them accurately whether it is what it claims to be. He charges a fee per test. He does not care what the answer is and he does not moralize about it. He also sells the wand, at a price, to anyone who would rather do it themselves — which is a business decision that on paper should destroy his own trade and has, in twenty years, cost him nothing.

### What Bros Believe
That the wand is a security screening and that passing it means they are safe. That a man who can tell real from fake is on their side by default. That buying the Pocket UV Wand makes them an expert rather than a person holding a torch.

### The Comedy Gap
The UV Man is not on anyone's side. He is a measuring instrument with opinions about technique. He will authenticate a genuine bill for a scammer and expose a fake one for a tourist with exactly the same expression, and he will tell either of them, unprompted, that the test has limits — that the light says what the light says and nothing further. The bros hear "it's real" and stop listening at the second word, which is precisely where the useful part of his sentence begins.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | 40-55 |
| Build | Still. Hands are steady in a way that is professionally notable and slightly unsettling |
| Height | Tall, stoops over the station |
| Energy | Focused, procedural, purple-lit |

### Clothing
- **Work coat**: Dark, plain, unmarked, cuffs rolled to the forearm so the sleeves never enter the light field. Deliberate.
- **Gloves**: Thin, white, cotton. Changed more often than anything else he owns.
- **Accessories**: The UV wand, in hand or in the holster on the station's edge, never anywhere else; a loupe on a cord he uses when the wand is not enough; a small mirror angled to throw light where his hand would shadow it
- **Footwear**: Unremarkable and unmoving. He does not shift his stance during a test.

### Distinguishing Features
- The purple glow underlights his face from below during every scan, which no one has ever described as reassuring
- Runs the wand in a fixed pattern — the same sweep, the same speed, every item, every time
- Announces the result in one word and then, unprompted, states the limitation of the test in a second sentence nobody listens to
- His hands do not move when he is not working. At all.

### Sprite Notes
The character is the light. His idle should read as *waiting to illuminate*; his scan poses are the performance. Palette per `shadow_exchange_png_asset_requirements.md`: UV purple (#9400D3) as the dominant source, thrown upward across a face otherwise in vault black. The wand is the silhouette prop and must be legible at 64x96. Per Sprite Sheet 4 (`shadow_exchange_npcs.png`, 512x512) he is the row at y=96 with seven poses: Idle Testing Position, UV Wand Scanning Frames 1-3, Counterfeit Detection, Tool Sales Pitch, and Authentic Approval. Prop: "UV Wand Tool" at (48, 384, 24x48). His station is `uv_detection_station.png`.

---

## 🧠 Personality

### Archetype
**The Neutral Instrument** — The UV Man has removed himself from every question except the one he can answer. Is this real? He can tell you. Should you buy it, sell it, trust it, or run? Not his stall. He has achieved a kind of professional purity that reads as coldness and is actually just an extremely narrow, extremely reliable service, sold at a fair price, to anyone.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Radically narrow | Answers exactly the question the light can answer and refuses every adjacent one |
| Procedurally identical | Same sweep, same speed, same words, for every customer regardless of who they are |
| Compulsively caveating | Always states the test's limits. Nobody has ever listened to the second sentence |
| Non-partisan | Serves scammers and marks at the same fee with the same neutrality |
| Quietly proud of technique | The only thing that reliably gets a reaction out of him is someone using a wand badly |

### Internal Monologue
> "Bill is genuine. Bill is genuine and the *wristband in his other hand* is not, and he has not asked about the wristband, and I do not volunteer. That is the arrangement. He asked one question. I answered one question. He will find out about the wristband at a door, later, from a larger man. ...His grip on the wand is wrong. That I will mention."

### Motivation
He is the only person in this cellar whose answer is verifiable, and being verifiable in a room built on paperwork that doesn't match is, to him, a genuine calling. Selling the wand does not threaten him: people who buy the wand learn how hard it is to use one properly, and roughly half of them come back and pay him to do it anyway.

---

## 💬 Dialogue

### Approach/Greeting

**First approach at the station**:
> "Put it on the glass. Hands off it while the light is on — your skin fluoresces and then we are testing you, which costs the same and tells us less."

**Approach carrying something obviously fake**:
> "You already know. You would not be here if you did not already know. Put it on the glass anyway; knowing and confirming are billed at the same rate."

### Key Interaction Dialogue

*A bro has slid a VIP wristband across the glass. It says WEDNESDAY. They all say WEDNESDAY.*

**Chadwick**: "So is it legit? Like, will it get me in?"

**The UV Man** (wand sweep, fixed pattern, no pause):
> "The band is not genuine. That is the answer to what the light can be asked." *(sets the wand down)* "Whether it gets you in is a question about a doorman, not about a band. I do not test doormen."

**Chadwick**: "...but would it *work*?"

**The UV Man**:
> "I have told you what it is. You have all the information the light produces. The rest is your evening."

*If the player asks what he thinks they should do:*
> "I am not that stall. Two arches down there is a woman who will convert your money and a corner where a man will sell you a chip. Neither of them will test anything. That is the whole market and you are standing in the middle of it."

*If the player asks whether he ever gets it wrong:*
> "The light does not get it wrong. The light gets it *incomplete*. A good forgery passes because it was made to pass this test specifically, and I will say so when I see one, and I have seen four."

*If the player asks about the wand's limits:*
> "It reads security features under ultraviolet. It does not read intent, provenance, or whether the person who handed it to you was smiling. People believe it reads all four. People are wrong and I tell them so and it changes nothing."

*If the player uses a Pocket UV Wand badly in front of him:*
> *(the only time his flatness cracks)* "No. No — angle. Forty degrees, not flat, you are washing out the entire strip. Give it here." *(demonstrates)* "Forty. Say forty."

*If the player asks about the Rate Sharks or the Counterfeit Connoisseurs:*
> "They discuss currency the way people discuss wine. It is not a lie. It is not useful. They are correct about approximately as often as they are confident, and those are not the same days."

### Sales Close — Pocket UV Wand
> "The wand is yours. It works everywhere, not only here — bars, doors, market stalls, anywhere someone hands you something and says a word about it. It will not make you good at this. Practice makes you good at this. The wand makes you *equipped*, which is the smaller half."

### Post-Interaction
> "You have your answer. It will not change. Items do not become genuine later."

### If Player Declines / Alternative Path

*Refusing the test fee:*
> "Then you will find out the expensive way, which is fine, and which is how most of my regulars became regulars."

*Refusing the wand purchase:*
> "Sensible. It is a tool for people who intend to keep having this problem. Some people only have it once."

*Asking him to test something he cannot test:*
> "The light does nothing for that. I will not take money for a test that answers nothing. Take it to Mrs. Rata or take it back where you got it."

*Asking him to lie about a result:*
> *(long pause; the wand goes into the holster)* "No. Not for money, not for a large amount of money, and not because you asked pleasantly. The stall stops being worth anything on the day I do that. Next."

### Callback Dialogue (Return Visits)

*Second visit:*
> "Again. Same glass. Put it down."

*After the player buys the Pocket UV Wand:*
> "You have your own now. You will still come here, because you will get an ambiguous strip at two in the morning and you will want a second opinion, and I am the second opinion. This was always the business model."

*After the player has had five or more items tested:*
> "You test before you buy. Almost nobody tests before they buy. They test after, at this counter, at two in the morning, holding a receipt from a business that closed."

*After the "no, forty degrees" correction, on a later visit:*
> "Show me the angle." *(player demonstrates)* "...Better. Good. That is the whole lesson, there is not a second one."

*Late game, high standing:*
> "Something has been circulating this month that passes. Genuinely passes. I have seen it four times and I have called it genuine four times and I believe I was wrong on all four. I am telling you because you test things. Nobody else here tests things."

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| All hours | UV detection station | Always accessible once the Exchange is discovered; the UV Man is always at the station |
| During transactions | UV detection station | 2-second authentication procedure per test (per the location's animation timing spec) |
| Post-boss (Count Velvet Absinthe) | UV detection station | Premium Stock circulation increases his test volume; unchanged behavior |

**Note:** No source file has depicted the UV Man absent or elsewhere. Treat the station as permanent.

### Positioning Notes
- One arch along from Mrs. Rata's main counter, under an iron lattice hung with counterfeit handbags and deactivated security tags — a backdrop of things that would fail his own test
- The station is the only purple light source in the vault; it is a wayfinding landmark visible from the stairs
- He faces the glass, not the room. Customers approach into his light rather than into his eyeline
- Positioned so that the barter window's UV-scan timing mini-game runs at his station — his stall is where the counterfeit-detection reaction game lives

---

## 🎒 Inventory / Services

### Services Offered
| Item/Service | Price | Actual Value | Effect/Result |
|--------------|-------|--------------|---------------|
| **Item authentication test** | Per-item fee | Genuinely accurate within the light's limits | Definitively identifies counterfeits among currency, wristbands, tickets, and documents. He states the limitation after every result |
| **Pocket UV Wand** (tool) | Tool price | High — it works everywhere | Player-portable counterfeit detection. **Enables the UV-scan verification mini-game at other locations across Debaucheryville**; the Exchange's primary tool-distribution node |
| **Barter window UV-scan checks** | Included in barter transactions | The difference between a good trade and a bad one | Quick-reaction timing mini-game identifying counterfeits during non-currency trades (concert wristbands, metro day-passes, gag items traded for rare gear, forged vouchers, specialized consumables) |
| **Second opinion** | Full fee, no discount | Emotionally significant, mechanically identical | For players who own a wand and got an ambiguous read. He has never once discounted this and considers the model sound |

### Hidden Details / Easter Eggs
- **Examining the gloves**: Thin white cotton, and there is a box of them under the station. He changes them between customers. Nobody has ever remarked on it.
- **Examining the small angled mirror**: Positioned to throw light into the shadow his own hand casts. It is the single cleverest object in the Shadow Exchange and it cost almost nothing.
- **Examining the counterfeit handbags on the lattice above him**: Every one of them would fail. They are hung there as decoration. He has never mentioned this.
- **Bringing him a genuinely good forgery** (the "four times" line's item, if implemented): The only occasion he asks to keep something. He offers to pay for it. He wants to study it.
- **Testing a genuine item you already knew was genuine**: *"Authentic. You knew. You wanted the sound of someone else saying it. That is also a service and it is the same fee."*

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Mrs. Rata | Adjacent stall, complementary trade. She converts what he authenticates. They have never been observed speaking, and the division of trade has never needed discussion |
| Token Goblin | Adjacent corner. Token Goblin's tokens, transit cards, and queue-skip chips pass across the UV glass constantly. Their working relationship is entirely non-verbal and entirely functional |
| Counterfeit Connoisseurs | Ambient patrons who treat authentication as a wine-tasting art form. He finds them harmless and their technique poor, and has said so exactly once |
| Influencer Resellers | Their "limited" VIP wristbands mysteriously always say WEDNESDAY. He fails them all. They keep selling them. Nothing changes |
| Rate Sharks | Their ledgers are immaculate and their currency is not always. He tests for them at full price like everyone else |
| The Glitching Bouncer (The Tap Dat Vault) | The Vault's door check and the Exchange's UV station are the city's two authentication points. Neither has met the other. Both would recognize the other's work instantly |
| Věra Novotná (Midnight Munchies) | She sells Fake VIP Wristbands with a stated 20% detection risk. His wand is a large part of why the number is 20% and not lower |

### Territory / Social Dynamics
- The strict divide of the Exchange floor — Rata converts, the UV Man authenticates, Token Goblin handles the near-currency margins — is observed absolutely and has never been formalized
- His neutrality is the reason the barter window functions at all: both sides of a trade accept his read, because he has never been known to favor either
- He is the only NPC in the Exchange who has refused money on the record, which the whole floor knows and nobody discusses
- Selling the wand to customers is treated by the Rate Sharks as commercially insane. He has outlasted several of them.

---

## 🔄 Recurring Appearances

### Within Debaucheryville
- Permanent at the Shadow Exchange UV detection station
- His **Pocket UV Wand is the city's counterfeit-detection tool**, making him a systems-level presence at every location where a fake item can be handed over — his influence appears in scenes he isn't in
- The barter window's UV-scan mini-game is his mechanic and recurs across the Exchange's trade content
- His authentication answers indirectly govern the Fake VIP Wristband economy running out of Midnight Munchies and the Influencer Resellers' stalls

### In Other Cities (If Applicable)
| City | Location | Role/Context | Callback Dialogue |
|------|----------|--------------|-------------------|
| — | — | The UV Man does not leave the station. The **wand** is his cross-city presence: once purchased, it functions in every city the player visits | *(If asked whether the wand works abroad)* "Ultraviolet is ultraviolet. The security features change. The physics does not. You will need to learn four new strips and you will learn them the expensive way." |

### Evolution Through Game
- **Visit 1**: Pure service. Test, one-word result, unheard caveat
- **After the wand purchase**: Reframes his own business model out loud — he expects you back, and explains why
- **After the angle correction**: The single teaching moment; on a later visit he asks the player to demonstrate and confirms it. This is his entire relationship arc
- **After five or more tests**: Acknowledges the player as someone who tests *before* rather than after, which from him is the highest available compliment
- **Late game**: The four-passes admission — the only time he expresses doubt about his own results, offered specifically to the player because the player tests things

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| idle_testing_position | Professional authentication stance; hands completely still | 45% |
| glove_change | Removes and replaces thin white cotton gloves | 20% |
| wand_holster_check | Touches the wand in the holster without removing it | 20% |
| mirror_adjust | Nudges the angled mirror by a degree it did not need | 15% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| uv_wand_scanning | Item test initiated; 3-frame sweep, fixed pattern, 2-second authentication procedure |
| counterfeit_detection | Test result: fake. Purple glow reveals the failure |
| authentic_approval | Test result: genuine. Identical delivery, different word |
| tool_sales_pitch | Pocket UV Wand purchase offered |
| angle_correction | Player uses a wand incorrectly in his presence — his only break in composure |

### Sprite States
| State | When Used |
|-------|-----------|
| uvman_idle | Default station presence |
| uvman_scanning | Active test; face underlit purple |
| uvman_result | Result delivery, either outcome |
| uvman_teaching | Angle correction; wand extended, demonstrating |

---

## 🎯 Quest Integration

### Primary Quest (If Applicable)
None owned. The UV Man is a **tool-distribution node** rather than a quest giver — a systems NPC whose output changes how the player interacts with content elsewhere.

### Quest Gate Function (If Applicable)
**Yes — soft systems gate.** The **Pocket UV Wand** is the Shadow Exchange's counterfeit-detection tool and, per `shadowexchange.md`'s Cross-Location Dependencies, it "enables counterfeit detection in other locations." Players without it are exposed to the Fake VIP Wristband economy, forged vouchers, and the barter window's counterfeit risk with no defense. He gates nothing hard — he sells the answer to a problem the player will otherwise keep paying for.

He also administers the **barter window's UV-scan timing mini-game**, which is the pass/fail check on every non-currency trade at the Exchange.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Pocket UV Wand | Any | Yes | Portable counterfeit detection; enables the UV-scan verification mini-game at other locations city-wide |
| Authentication result | Any | N/A (information) | Definitive real/fake determination on currency, wristbands, tickets, and documents, within the light's stated limits |

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. Face underlit purple, mid-sweep, in an otherwise black vault
2. The WEDNESDAY wristband failing under UV with a bro's face visible behind it
3. The lattice of counterfeit handbags hanging directly above the counterfeit-detection station
4. The angle-correction moment — the one frame where he is animated
5. The small angled mirror doing its job, with the shadow it eliminates visible in the before-shot

### Meme Potential
- "Whether it gets you in is a question about a doorman, not about a band. I do not test doormen."
- "Items do not become genuine later."
- "Forty. Say forty."
- "You wanted the sound of someone else saying it. That is also a service and it is the same fee."
- "It does not read intent, provenance, or whether the person who handed it to you was smiling."

---

## 🗣️ Voice Direction

### Accent
Czech, quiet, technical. The most precise diction in the Shadow Exchange after Mrs. Rata's, and unlike hers it is not institutional — it is the diction of someone who has to be understood the first time because he says things once.

### Tone
- **Results**: One word, no inflection. "Authentic." "Counterfeit."
- **Caveats**: Immediately after, same volume, slightly faster — the sentence of a man who knows nobody is listening and says it anyway
- **Refusals**: Flat and final. The "no, not for money" line needs a long pause before it and nothing decorative after
- **Angle correction**: The only animated register he has. Sharp, insistent, over almost immediately

### Key Delivery Notes
- Never make him sound sinister. The purple underlight does all the atmosphere work; the performance should be a technician's
- His caveat sentence must never be delivered as a warning. It is a specification
- "Forty. Say forty." is close to affection and should be played as pedagogy, not as a joke
- He does not do irony. Every apparently dry line is a literal answer
- The long pause before refusing to lie is his most important beat in the profile — do not shorten it

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

- **"The UV Man" is the complete identity.** No first name, surname, or alias exists in any source file. **Do not invent one** — the anonymity is characterizing and it is consistent with Mrs. Rata and Token Goblin, who are also trade-titles rather than names.
- **Pricing is deliberately unspecified.** `shadowexchange.md` states he "tests items for fee" and "sells Pocket UV Wand tool" without numbers. This profile does not invent prices — that belongs to an items/shop pass. Do not fill them in during a profile pass.
- **Dialogue attribution note**: none of the three unattributed lines in `shadowexchange.md`'s "Original NPC Dialogue" section are assigned to the UV Man in this profile. See `npc_mrs_rata.md` Development Notes for the proposed split across the three Exchange vendors.
- The **Pocket UV Wand is a cross-location systems item**. Whoever specs the counterfeit-detection mini-game owns its timing; this profile only establishes that his station is where the barter-window version runs.
- The "four good forgeries" late-game line is a proposed hook, not established canon. If a genuinely-passing counterfeit item is ever implemented, this is its foreshadowing; if not, cut the line rather than leave it dangling.
- The Fake VIP Wristband at Midnight Munchies carries a stated **20% detection risk**. Confirm during a systems pass whether owning the Pocket UV Wand modifies that number — it probably should, and it is currently unspecified in both files.
- Voice acting priority: **medium-high**. Low line count, but his refusal beat and the angle correction are the character in full and both need real performance.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — this profile contains **zero** crypto content; the UV Man's trade is physical authentication only
- [x] **NO automatic crypto assumptions** — a UV wand does not read a blockchain and he says so implicitly by listing exactly what it does read
- [x] **Coins, kiosks, and certificates come from the master pool** — none used, none invented
- [x] **The bros are never scam-aware** — they hear "it's not genuine," ask if it will work anyway, and go to the door with it
- [x] **Nothing winks** — his caveats are technical specifications, never authorial commentary
- [x] **Focus on city-specific cultural exploitation instead** — grey-market authentication economics, the counterfeit-wristband trade, and tourist over-trust in the appearance of a security process

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior (hearing the first word of a two-sentence answer, believing a tool confers expertise), NOT local culture or ethnicity
- [x] NPC is a savvy operator — a specialist with an unimpeachable professional standard and a counterintuitive but sound business model — not a villain or a stereotype
- [x] Humor is affectionate; his integrity is played entirely straight and is the most admirable thing in the Shadow Exchange

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Debaucheryville/npcs/Shadow_Exchange/npc_uv_man.md`
- **Registered In**: No — Shadow Exchange has **no** `shadow_exchange_npcs.json`. One must be created; it will need The UV Man, Mrs. Rata, Token Goblin, CryptoBro69's Ex (profile already exists at `npcs/Shadow_Exchange/cryptobro69s_ex.md`), and the four atmospheric NPC types specced on `atmospheric_npcs_types.png`.
- **Sprite Sheet**: `shadow_exchange_npcs.png` (512x512, 64x96 base; The UV Man's seven poses on the row at y=96, per `PNG_Assets/shadow_exchange_png_asset_requirements.md` Sprite Sheet 4). Prop: "UV Wand Tool" at (48, 384, 24x48). Station asset: `uv_detection_station.png` (128x128).

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile — authored from `shadowexchange.md` (vendor cast, barter window, UV-scan timing checks, tool distribution, cross-location dependencies) and `PNG_Assets/shadow_exchange_png_asset_requirements.md` (Sprite Sheet 4 pose list, 2-second authentication timing). Flagged unspecified pricing and the Fake VIP Wristband detection-risk interaction | machsheltie |

---

*Template Version 1.1*
