# Item Definition: "She Thinks My Tractor's Sexy" (Mint #42)

*"It's on the chain. Digital land, baby." - Aaron the Unflappable, handing over a piece of aluminum in complete sincerity*

## 📋 Item Identity
- **Item ID**: `item_tractor_nft`
- **Display Name**: "She Thinks My Tractor's Sexy" (Mint #42)
- **Internal Name**: Scratched aluminum token with a QR code stamped into it
- **Item Type**: Quest Item (permanent — key-item slot, cannot be dropped, sold, or destroyed)
- **Rarity**: Common (bros think it's Limited Drop, Early Position, Mint #42 of a series they have never seen the size of)
- **Source**: Aaron the Unflappable (`sinfonia_npc_aaron_unflappable_01`) @ Aaron's Corner Table, The Black-Tie Backroom, Sinfonia — granted at Beat 8 of `blacktie_event_kings_were_humming_01`

---

## 🎭 The Deception

### What The Item Actually Is
A scratched aluminum token, roughly the diameter of a bottle cap and about as heavy, with a QR code stamped into one face and **MINT #42** stamped into the other. It smells faintly of Kahlúa and fresh-cut grass, and it has smelled of both since before it reached Aaron's pocket.

The QR resolves — on the party's phone, in-world, on the first scan — to a Geocities page that expired years ago. What loads instead is the host's placeholder: a grey background, a broken-image icon, a hit counter reading **000019**, and a MIDI file that autoplays and cannot be stopped without closing the browser.

The token is the physical stub for an NFT. The NFT is a **low-res animated GIF of a zero-turn mower doing a donut on a manicured lawn**, eleven frames, looping, with a **tiny pixelated cowboy hat bouncing on the seat** slightly out of sync with the turn. The lawn is very good. Somebody clearly cared about the lawn.

It is worth **€0** at any bank, any exchange, any pawnbroker, any legitimate vendor, and every illegitimate one, in every city in the game, permanently and by design.

Aaron gave it away because he thought it would help. He believed that entirely. Nobody in the Backroom has ever asked him where he got it and he has never volunteered.

### What The Bros Believe It Is
"Mint number FORTY-TWO. In a limited drop. Do you understand what that means? That means forty-one people got in before us and everybody after us is paying *our* number. That's not a souvenir, that's a *position*. And he didn't sell it to us, chat — that's the part — he HANDED it to us. Nobody hands you a position unless they want you at the table next time."

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | N/A (gift only — never sold, never listed, never findable anywhere else in the game) |
| **Actual Value** | €0 |
| **Resale Value** | €0 (worthless). Every vendor, exchange, bank, pawnbroker, and shady terminal in the game returns the same €0 valuation |
| **Can Be Sold** | No — offering it to a vendor plays that vendor's standard "I can't use this" line, unchanged, every time |
| **Can Be Dropped** | No (permanent quest item; also the bros would not) |
| **Can Be Traded** | No — Chadwick has offered it to nine people and will offer it to more |

---

## 🎨 Visual Specifications

### Physical Appearance
| Attribute | Description |
|-----------|--------------|
| **Material** | Stamped aluminum, unplated, soft enough to mark with a fingernail |
| **Diameter** | 31mm, ~1.5mm thick, slightly out of round from a press that needed servicing |
| **Edge** | Milled, with one flat spot where somebody once used it to open something |
| **Text/Markings** | Obverse: QR code stamped into the metal, one corner marker shallow. Reverse: **MINT #42** above a five-line stamp of a tractor rendered in about forty dots |
| **Finish** | Scuffed satin, fine circular scratching all over, the faintest smell of Kahlúa and fresh-cut grass that does not fade at any point in the game |

### Degradation Over Time
| Days Worn | Visual State |
|-----------|--------------|
| Days 1-3 | As received: scuffed, legible, the tractor stamp readable if you know it is a tractor |
| Days 4-7 | Pocket-polished on the high points, QR's shallow corner marker now scanning unreliably — every second scan fails and the bros blame the phone |
| Days 8+ | The tractor stamp is a smear, the QR no longer resolves at all on any device, and the flat spot on the edge has widened from being used to open bottles. **Still worth €0. Was always worth €0.** |

---

## 📊 Stats & Effects

### Direct Stats
```
Bravado:              +1  (asset ownership)
Charm (Bros):         +2  (among themselves, exclusively, at all times)
Charm (Everyone Else): 0  (the token is not visible to anyone who is not shown it, and it is shown to everyone)
Gold Value:            0  (displayed as "€0" in the inventory value column, in the same font as real values)
```

### Passive Effects
| Effect | Description |
|--------|--------------|
| **On The Chain** | Counts as **one of the twelve** Frat Bro NFT collection targets — Sinfonia's fourth. Advances collection milestones at 4 / 8 / 12 exactly like any other target |
| **The Scan** | Examining the token in the inventory opens the in-world browser, loads the expired Geocities placeholder, plays the MIDI, and displays hit counter **000019**. The counter increments by one on each scan. It never reaches anything |
| **Unprompted Presentation** | Whenever the party enters a new location for the first time, a bro shows the token to the first NPC who speaks to them. The NPC's response is their existing greeting, unchanged. No unique lines are authored for this |

### What It Does NOT Do
- ❌ Convert to gold, credit, chips, or goods anywhere in the game, at any point, at any exchange rate
- ❌ Grant Backroom access, table credit, or any standing with the house
- ❌ Appreciate, tier up, unlock a "collection value" screen, or reveal a real drop size
- ❌ Get the party a ticket back to anything, top or otherwise
- ❌ Resolve. The Geocities page is expired and stays expired for the whole game

---

## 🎯 Gameplay Integration

### Permanent Quest-Item Change
Once granted, the token is a **permanent party key item**. It occupies a key-item slot for the rest of the game, cannot be dropped, sold, destroyed, or left behind, and is present in the final save. It is carried by Chadwick by default because he took it and did not put it down.

### Sprite Implementation
- **Visibility**: Carried in Chadwick's front pocket, drawn as a small silhouette; drawn in-hand during any presentation beat; visible on the phone screen in any scene where Chadwick is filming it
- **Layer**: Prop layer during presentation; pocket overlay otherwise; screen-content layer when displayed on the in-world phone
- **Animation**: The GIF itself is an **11-frame loop** — mower rotating, cowboy hat bouncing one frame behind the turn. Loops continuously whenever it is on screen, including in the inventory preview pane, including during dialogue, including in the background of other conversations
- **Degradation**: Metal wear advances on in-game days elapsed since acquisition, per the table above. The GIF never degrades; it is the token that wears out

---

## 🗣️ NPC Reactions

### When NPCs Notice The Token
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| Sinfonia bank teller | "This is not a currency. This is a piece of metal with a picture on it." | "That's what they said about every currency." |
| Grounds For Concern barista | "Five euro." — *(token held up)* — "No." | "They're not set up for it yet. Early market." |
| Pawnbroker, any city | *turns it over twice, sets it down, slides it back without a word* | "He knows what it is. He knows he can't afford it." |
| Shady terminal operator, Debaucheryville | "Ah — the tractor. Yes. I have seen the tractor." | "It's KNOWN. Bro. The tractor is KNOWN." |
| Actual NFT-flaunting Influencer Syndicate member | *glances at it for under a second, glances away, keeps talking* | "Intimidated. Straight up." |

### Callback Dialogue Throughout Game
**Lord Pilsner** (any bar, holding the token to the light):
> "Every asset class starts out looking like a bottle cap. Every single one. Somebody in a room in Sinfonia handed me digital land and did not ask me for one euro. You think about what that means about the guy. Then you think about what it means about me."

**Chadwick** (to camera, front-facing, token filling the frame):
> "Chat, I keep getting asked what the floor is. I'm not gonna give you a number, because I'm not a financial advisor. What I *will* say is that mine is number forty-two, and yours is not."

**Bradley** (flat, to a hostel receptionist who is trying to check them in):
> "It's on the chain. So it can't be lost. Even if I lose it, it's still there. That's why I'm not that careful with it."

---

## 🔗 Quest Integration

### Source Quest
- **Quest ID**: `sinfonia_sidequest_the_kings_were_humming_01`
- **Quest Name**: "The Kings Were Humming"
- **Quest Giver**: Aaron the Unflappable (a gift, not a transaction — he asks for nothing and is given nothing)
- **Location**: Aaron's Corner Table (`aarons_corner_table`), The Black-Tie Backroom, Sinfonia

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| Frat Bro NFT collection target — Sinfonia 4 of 4 | Granted at Beat 8 of `blacktie_event_kings_were_humming_01`; see `Design/Quests/Location Specific/Sinfonia/nfthuntsinfonia.md` |
| Milestone progress at 4 / 8 / 12 collected | Counts as one target, identically to every other; see `Design/Quests/fratbronft.md` |
| The expired-Geocities scan scene | First examine of the token from the inventory screen |

### Achievement
- **Achievement Name**: "Digital Land"
- **Description**: "Leave the Black-Tie Backroom with more assets than you walked in with."
- **Hidden Description**: "Leave the Black-Tie Backroom with a carton of candy and a piece of aluminum."

---

## 🎬 Key Story Moments

### The Grant
*Aaron digs in the velvet pocket, past the tie, and comes out with a scratched aluminum token. He presents it the way you present something you believe will genuinely help.*
> "It's on the chain. Digital land, baby. She Thinks My Tractor's Sexy. Limited drop. Mint #42. Hold onto that—that's your ticket back to the top."

*[ACQUIRED: `item_tractor_nft` — party, permanent]*

**Chadwick** *(turning the token over, already filming it)*: "Bro. He's cutting us IN."

### The First Scan
*A hostel stairwell, three in the morning, one bar of signal. Chadwick scans the token. The page loads grey. A broken-image icon. A hit counter reading 000019. A MIDI file starts and does not stop.*

**Chadwick** *(reading the counter aloud)*:
> "Nineteen. Nineteen views on the whole *contract*. Boys. Boys, we are so early."

*Bradley reaches over and scans it too. The counter reads 000020.*

**Bradley**:
> "Twenty. It's moving."

### The Valuation
*A Sinfonia bank, daylight, a queue behind them. Lord Pilsner slides the token across the counter with two fingers, the way he pushed the chips.*

**Lord Pilsner**:
> "What are we looking at, ballpark."

*The teller looks at the token. Then at him. Then back at the token. She is a professional and she gives him a professional answer.*

**Teller**:
> "Nothing."

**Lord Pilsner** *(nodding slowly, gathering it up, entirely satisfied)*:
> "Yeah. They can't quote it. That's what happens when it's not in the system yet."

---

## 🖥️ Performance & Assets

### Sprite Requirements
- **Base Size**: 12×12 pixels per token; 48×48 pixels for the GIF loop in the inventory preview pane
- **Memory**: Low — one prop sprite with three wear states, one 11-frame GIF, one static browser-page asset
- **Animation**: 11-frame GIF loop, ~8fps, must play in the inventory preview and on the in-world phone screen simultaneously without a second instance being loaded
- **Degradation Variants**: 3 token wear states × 1 shared prop = 3 variants; the GIF has no variants

### Performance Impact
- One additional small draw call while the token is on screen
- No particle effects; the Kahlúa-and-grass smell is a text-only detail and must never be rendered as a particle or an aura
- No dynamic lighting; the token does not glint, shine, sparkle, or emit under any circumstances

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item clearly defined | ✅ |
| Purchase/acquisition documented | ✅ |
| Stats and effects specified | ✅ |
| Visual specifications complete | ✅ |
| NPC reactions documented | ✅ |
| Quest integration clear | ✅ |
| Distinction from equipment item (if applicable) | N/A — no equippable counterpart exists |
| Comedy value preserved | ✅ |
| Bros never achieve self-awareness | ✅ |

---

## 📝 Development Notes

- **Locked facts, do not drift:** low-res animated GIF of a zero-turn mower doing a donut on a manicured lawn; tiny pixelated cowboy hat bouncing on the seat; stamped on a scratched aluminum token; smells faintly of Kahlúa and fresh-cut grass; QR links to an expired Geocities page; worth €0 at any bank, exchange, or legitimate vendor
- **€0 is permanent and universal.** No vendor, no exchange, no black market, no late-game buyer, no post-credits twist in which it turns out to be worth something. If any future pass gives this token a value, that pass has broken it
- **Aaron's sincerity is untouchable.** He is not offloading it, not running a bit, and not amused. He believes it will help them and he gives it away for nothing. No line, examine text, or later scene may imply otherwise
- The **hit counter increments per scan and is shared party-wide**, starting at 000019. It has no cap, no reward threshold, and no reaction at any number
- The MIDI is a single short loop and must autoplay every time the page is opened, with no in-page stop control — closing the browser is the only way out, exactly as it was in 2003
- The GIF's cowboy hat must bounce **one frame behind** the mower's rotation. This is the joke in the asset and it does not survive being synced
- Easter egg: the same GIF is the background of exactly one other expired page reachable from a Debaucheryville shady terminal, at a different mint number, and nobody ever mentions it
- Grant is scene-triggered only (`blacktie_event_kings_were_humming_01`, Beat 8) and must be idempotent against the one-time-scene flag; see the quest file's Engine Requirements block
