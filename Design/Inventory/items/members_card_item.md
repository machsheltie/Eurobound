# Item Definition: The Member's Card

*"Ah. Then we skip two of the three questions." ... "Not that one." - Viktor the Doorman, gesturing at the deposit window*

## 📋 Item Identity
- **Item ID**: `item_members_card`
- **Display Name**: The Member's Card
- **Internal Name**: Unnamed, unnumbered plastic card the house cuts for guests it would like to see again
- **Item Type**: Quest Item (permanent — key-item slot, cannot be dropped, sold, or destroyed)
- **Rarity**: Uncommon (bros think it's Inner Circle, Invitation Only, "there are maybe forty of these")
- **Source**: The house — cut at the cage on Madame Karten's instruction (`sinfonia_npc_madame_karten_01`) and left with Siegfried at the coat check (`sinfonia_npc_siegfried_coatcheck_01`), The Black-Tie Backroom (`sinfonia_operahouse_blacktie_backroom_01`), Sinfonia

---

## 🎭 The Deception

### What The Item Actually Is
A rectangle of black plastic, 85×54mm, with the Backroom's spade-and-laurel mark blind-embossed in one corner. There is **no name on it.** There is **no number on it.** There is no expiry date, no signature strip, no magnetic stripe, and nothing on the reverse but the mark again, smaller. It is not personalised because it is not personal, and it is not personal because the house cuts them in batches.

The cage cuts one for any guest who has moved roughly **€1,000 across the Backroom's real tables — in either direction.** Won it, lost it, or churned it through the rake: the threshold is turnover, not outcome, and the little card that comes with it is the identical card either way, printed in a batch, with the identical wording:

> *"The house would be glad of your company again."*

Which is true. The house would. The house is extremely glad of the company of anybody who has demonstrated they will move a thousand euro across a table in a room with a documented edge.

Mechanically, the card does exactly one thing: it satisfies Viktor's **attire** requirement at the door in place of Black-Tie Attire. It does not satisfy the stat check. It does not satisfy the €500 collateral. It does not open the velvet rope to the High Stakes Salon, the Private Boxes, or the vault antechamber. It gets the party down the stairs in whatever they happen to be wearing.

### What The Bros Believe It Is
"They don't advertise this. There's no application. You can't *ask* for one — I checked, I asked, and the guy went and got the card, which tells you the asking is part of it. Point is we're on a list now. Somewhere in that building there is a list, and it is not a long list, and we are on it. That's Europe-wide access, potentially. I'd honestly try it at an airport."

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | N/A (issued by the house — not sold, not purchasable, not obtainable by asking, despite Lord Pilsner asking) |
| **Actual Value** | €0.11 (batch-cut plastic; the embossing die is thirty years old and paid for) |
| **Resale Value** | €0 (worthless — and it is not transferable, so a buyer would get nothing) |
| **Can Be Sold** | No |
| **Can Be Dropped** | No (permanent key item) |
| **Can Be Traded** | No — the card is party-scoped; whichever bro is holding it at the door is the bro who presents it |

---

## 🎨 Visual Specifications

### Physical Appearance
| Attribute | Description |
|-----------|--------------|
| **Material** | Matte black PVC, 0.8mm, batch-cut with a very slightly rounded corner die |
| **Dimensions** | 85×54mm — standard, which the bros read as deliberate discretion |
| **Closure/Carry** | None. It goes in a jacket pocket and comes out of a jacket pocket, and there is no wallet in the party that fits it properly |
| **Text/Markings** | Obverse: blind-embossed spade-and-laurel mark, upper left. **No name. No number. No date.** Reverse: the same mark at half size, centred, and nothing else |
| **Finish** | Matte, fingerprint-hungry; the embossing catches light only at a shallow angle, which is why Chadwick cannot photograph it either |

### Degradation Over Time
| Days Worn | Visual State |
|-----------|--------------|
| Days 1-3 | Flat, matte, immaculate; the emboss crisp; carried in an inside pocket and produced with two hands |
| Days 4-7 | Fine scratching across the matte face from being carried loose with coins; one corner beginning to lift where the PVC has been flexed |
| Days 8+ | Face scuffed grey-black, emboss softened to a suggestion, one corner delaminating, and a faint ring pressed into it from a bottle that was standing on it. Still opens the same door, because the door was never checking the card's condition |

---

## 📊 Stats & Effects

### Direct Stats
```
Charm (Backroom staff):    +1  (they know what the card means; they are pleasant about it)
Bravado:                   +2  (membership, in his own assessment, of something)
Charm (Everyone else):      0  (the card is unreadable to anybody outside that building)
```

### Passive Effects
| Effect | Description |
|--------|--------------|
| **Attire Substitution** | Satisfies Viktor's Black-Tie Attire item requirement at the Backroom door. The stat check (+3 Charm **or** +3 Bravado) and the €500 collateral are unaffected and still apply in full |
| **The House Would Be Glad** | Backroom staff greet the party by sight rather than by assessment on every subsequent entry. No comps, no credit, no odds change |
| **Presented Unprompted** | On first entry to any gated venue in any city, a bro presents the card. It is never accepted anywhere except the Backroom door, and no venue authors a unique refusal for it — the existing rejection line plays, unchanged |

### What It Does NOT Do
- ❌ Waive, reduce, or defer the €500 collateral by one euro
- ❌ Satisfy the +3 Charm / +3 Bravado door check
- ❌ Open the High Stakes Salon, the Private Boxes, or the vault antechamber
- ❌ Confer credit, a line, a tab, comps, or any standing with the cage beyond being recognised on sight
- ❌ Work at any door, rope, lounge, airline counter, or club anywhere else in the game, ever

---

## 🎯 Gameplay Integration

### Permanent Quest-Item Change
Once issued, the card is a **permanent party key item** for the rest of the game. It cannot be dropped, sold, destroyed, or left behind, and it is present in the final save. It is the alternative access route named in the Backroom's entry conditions, and it makes the Haute Couture Haberdashery's Black-Tie Attire optional **for this door only** — which the bros discover after buying the attire, and which changes nothing about how they feel about having bought the attire.

### Sprite Implementation
- **Visibility**: Carried in an inside jacket pocket, not visible in the idle sprite; drawn in-hand during any presentation beat and during the door check
- **Layer**: Prop layer during presentation; no persistent overlay
- **Animation**: Two-frame produce-and-present, reusing the existing hand-to-chest rig. Lord Pilsner's version holds the card a beat longer than the animation needs and Viktor waits it out every time
- **Degradation**: Card wear advances on in-game days elapsed since issue, per the table above; the door check never reads the wear state

---

## 🗣️ NPC Reactions

### When NPCs Notice The Card
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| Viktor the Doorman | *takes it, looks at it for the same two seconds he looks at everything, hands it back* "Ah. Then we skip two of the three questions." *(gestures at the deposit window)* "Not that one." — his dedicated card line, per `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/viktor_the_doorman.md` | "Two out of three. That's a *supermajority*, boys." |
| Madame Karten | "Darling, how lovely. The house would be glad of your company again." *(the wording on the card, verbatim, warmly)* | "She's quoting the charter at us. That's a ceremony thing." |
| Siegfried at the coat check | *hangs the coats, nods at the pocket the card lives in, says nothing* | "He's counting us in. Coat guy counts everybody in." |
| Monsieur Aiguille, Haute Couture Haberdashery | "Then you will not require the suit." *(a pause exactly long enough to be a needle)* "You will still want the suit." | "He's trying to keep the sale. Respect the hustle." |
| Publandia doorman, weeks later | *does not take it, does not look down at it* "This is a pub." | "Different system over here. They go by face." |

### Callback Dialogue Throughout Game
**Lord Pilsner** (producing the card in a venue that has no door policy at all):
> "I'm not gonna make a thing of it. I'm just gonna leave it on the bar face-up and let the room do what the room does."

**Chadwick** (to camera, card angled into the light and refusing to photograph):
> "Chat, it's black-on-black, which is a flex, because it means it's not FOR you. I can't get it to read on camera and honestly? That's the point. That's the whole design brief."

**Bradley** (flat, to a hostel receptionist, having been asked for a passport):
> "Will this do? It's got no name on it. That's usually a good sign."

---

## 🔗 Quest Integration

### Source Quest
- **Quest ID**: `sinfonia_sidequest_high_stakes_01` *(provisional — "High Stakes" is listed in the Backroom location file's Quest Integration but has no quest file yet; confirm the ID and the exact turnover threshold when it is authored)*
- **Quest Name**: "High Stakes"
- **Quest Giver**: Nobody. The cage cuts the card on Madame Karten's instruction and Siegfried hands it over with the coats
- **Location**: The cage and the coat check, The Black-Tie Backroom, Sinfonia

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| Backroom entry without Black-Tie Attire equipped | Card held; stat check and €500 collateral still enforced separately |
| Staff recognition on entry (greeting instead of assessment) | Automatic once issued |
| The Haberdashery's Black-Tie Attire becomes optional for this door | Automatic once issued — and the party has usually already bought it |

### Achievement
- **Achievement Name**: "Valued Guest"
- **Description**: "Receive a Member's Card from The Black-Tie Backroom."
- **Hidden Description**: "Move €1,000 across the house's tables. Direction not important."

---

## 🎬 Key Story Moments

### The Issue
*The coat check, near close. Siegfried hands the coats back and puts a small black card on the counter on top of them, with a printed slip.*

**Siegfried**:
> "From the floor. Bring it next time — you won't need the jacket."

*Lord Pilsner picks it up with two hands. He turns it over. There is nothing on the back.*

**Lord Pilsner** *(quietly, to the card)*:
> "Boys. There's no name on it."

**Chadwick**:
> "That's because they know the name."

*The printed slip says: "The house would be glad of your company again." It is a batch print. There is a box of them under the counter, and the box is in frame, and nobody looks at it.*

### The Door
*The bottom of the stairs, next visit. Lord Pilsner produces the card and holds it out, and holds it out, and holds it out. Viktor takes it, looks at it for exactly as long as he looks at everything, and hands it back.*

**Viktor**:
> "Ah. Then we skip two of the three questions."

*He gestures at the deposit window. Nothing else about the check changes: the collateral is the collateral.*

**Viktor**:
> "Not that one."

**Lord Pilsner** *(already reaching for the gold, delighted)*: "He's waiving things for us now. You hear that? He's *waiving*."

### The Airport
*Weeks later. A check-in desk. Lord Pilsner slides the card across, face-up, with two fingers.*

**Lord Pilsner**:
> "Anything you can do."

*The agent looks at a black rectangle with no name, no number, and a small embossed spade on it. She has been doing this for eleven years.*

**Agent**:
> "Window or aisle?"

**Lord Pilsner** *(taking the card back, entirely satisfied)*:
> "See, that's a bump. That's how they tell you."

*It is not a bump. It is a window seat, which is the seat he booked.*

---

## 🖥️ Performance & Assets

### Sprite Requirements
- **Base Size**: 48×32 pixels (`members_card.png`, per the Backroom's sprite manifest)
- **Memory**: Minimal — one prop sprite, three wear states, no persistent overlay
- **Animation**: Two-frame produce-and-present reusing the existing hand-to-chest rig; no new skeleton required
- **Degradation Variants**: 3 wear states × 1 shared prop = 3 variants (the card is party-scoped, not per-bro)

### Performance Impact
- Negligible — the card is on screen only during presentation beats
- No particle effects; the emboss is a sprite detail, not a highlight pass
- No dynamic lighting; the card must read as matte and unphotographable at every zoom level, which is a rendering requirement rather than a bug

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
| Distinction from equipment item (if applicable) | N/A — the card is not an equippable; it substitutes for the Black-Tie Attire **requirement** at one door and occupies no equipment slot |
| Comedy value preserved | ✅ |
| Bros never achieve self-awareness | ✅ |

---

## 📝 Development Notes

- **The card substitutes for attire only.** Any pass that lets it waive the €500 collateral or the +3 stat check has broken both the door and the Backroom's economy. The three entry conditions are independent and stay independent
- **Nobody explains the threshold.** No NPC, narrator line, tooltip, or achievement string says out loud that the card is cut on turnover rather than on winning. The box of identical printed slips under the coat-check counter is visible in the issue frame and that is the entire delivery
- **The wording is identical for winners and losers** — same card, same slip, same batch, same sentence. If a later pass writes a second version of the note for a winning party, the joke is gone
- The card is **party-scoped, not per-bro** — one card, one key-item slot, whoever is at the front presents it. No variants, no duplicates, no arguments about custody authored
- Blind embossing must be legible at 48×32 at a shallow angle and effectively invisible head-on. Chadwick's inability to photograph it is a rendering requirement
- Confirm the issue trigger and threshold against "High Stakes" when that quest is authored; until then the €1,000-turnover rule and the provisional quest ID above are this file's assumption and are flagged as such
- The card does nothing at any other door in any other city, permanently, and no bro ever stops trying it
