# Item Definition: The Leopard-Print Thong

*"...Mine now?"* - Lord Pilsner, from inside a sleeping bag, without opening his eyes, closing the only negotiation of his life he has ever won

## 📋 Item Identity
- **Item ID**: `item_leopard_print_thong`
- **Display Name**: The Leopard-Print Thong
- **Internal Name**: One leopard-print male thong, provenance unknown, permanently
- **Item Type**: Permanent Hybrid (Cosmetic + Passive) — equippable, bound to Lord Pilsner, never leaves the inventory
- **Rarity**: Common (Lord Pilsner is certain it is One-Of-A-Kind, and in the only sense that matters to him, it is)
- **Source**: Acquired automatically during `night_event_outbreak_01`, the outbreak morning at `night_party_zone`, The Bohemian Riviera. **"...Mine now?" IS the acquisition line** — the inventory-grant stinger fires on it

---

## 🎭 The Deception

### What The Item Actually Is
A mass-produced novelty leopard-print male thong, 92% polyester, 8% spandex, of the exact kind sold off a rotating wire rack at every beachfront stall on the strip for about 5 Sovs, three for 12 Sovs. The care label has been washed past legibility — no brand, no size, no country of manufacture, nothing. It was at the party. Many things were at the party.

**Whose it was is never established.** Not in this file, not in the quest, not in a tooltip, not in an examine string, not in an achievement, not in any later pass. The game gives the player nothing, forever, on purpose.

### What The Bros Believe It Is
"This is a TROPHY, boys. You don't GET one of these. One of these gets AWARDED to you, and it gets awarded at NIGHT, and there's no ceremony, and there's no paperwork, and that's how you know it counts. Am I gonna talk about how I got it? No. Am I gonna WEAR it every single day for the rest of this trip? Obviously. That's called respecting the win."

*(He has no idea how he got it. He has never once considered the question. The absence of an answer is, to him, the strongest evidence that something magnificent happened.)*

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | N/A (never purchased — granted automatically to Lord Pilsner at the outbreak morning; not stocked by any vendor in any city) |
| **Actual Value** | 5 Sovs at any beachfront stall on the strip (three for 12 Sovs) |
| **Resale Value** | 0 Sovs (worthless) |
| **Can Be Sold** | No. No vendor anywhere will take it, and Lord Pilsner would not offer it if they would |
| **Can Be Dropped** | No (permanent — it is a trophy, and one does not drop a trophy) |
| **Can Be Traded** | No (Chadwick and Bradley have never asked, and will never ask) |

---

## 🎨 Visual Specifications

### Physical Appearance
| Attribute | Description |
|-----------|-------------|
| **Material** | 92% polyester, 8% spandex, stall-grade |
| **Print** | Machine-repeated leopard rosettes, visibly misaligned where the pattern meets at the seam |
| **Waistband** | Flat elastic, already slightly relaxed on Day 1, one loose thread at the left hip that never gets longer or shorter |
| **Text/Markings** | Care label faded past reading. No brand. No size. No country of manufacture. Zoom in as far as the engine allows and the answer is still not there |
| **Fit** | Not his size. Not close to his size. He has never mentioned this and never will |

### Degradation Over Time
| Days Worn | Visual State |
|-----------|--------------|
| Days 1-3 | Sand in the seam, print still bright, elastic holding |
| Days 4-7 | Sun-faded across the top band from being worn under everything on a cross-continent limp; rosettes softening toward vague spots |
| Days 8+ | Fully sun-bleached to a pale ochre, rosettes now abstract, hip thread grey, elastic surrendered — visibly a thing that has been to another country and back, which is precisely how Lord Pilsner describes it |

---

## 📊 Stats & Effects

### Direct Stats
```
Bravado:              +1 (net: +2 entirely unearned and structurally load-bearing, -1 because he brings it up)
Charm:                +0 (nobody can see it; the few who learn of it are not charmed)
Resolve (Pilsner):    +2 (conditional — applies only while equipped by Lord Pilsner, which is always)
```

### Passive Effects
| Effect | Description |
|--------|--------------|
| **Spoils of War** | 8% chance on Lord Pilsner's turn: he references the trophy unprompted, mid-combat, apropos of nothing. Enemies of tourist/local type gain **Embarrassed** for 1 turn (they did not want this information); his own party members take −1 Accuracy for 1 turn (they cannot look at him) |
| **The Sleeping Bag Standard** | Lord Pilsner is immune to **Existential Crisis** while equipped. A man with a trophy does not question his life choices; he questions why other people don't have trophies |
| **Nothing Is Established** | Examining it in the inventory returns the same non-answer string every time, verbatim, on every examine, in every city, for the entire game. The description never grows, never hints, never rewards persistence |
| **Layer Discipline** | Worn under everything, always, including formal wear. Never rendered on-body beyond a single waistband pixel line — the joke is that it is there, not that it is seen |

### What It Does NOT Do
- ❌ Establish that any conquest, victory, or achievement of any kind took place
- ❌ Identify its previous owner — nothing in this game ever will
- ❌ Fit
- ❌ Come off (see Gameplay Integration)
- ❌ Improve Charm with any NPC who learns of its existence, which is a growing list

---

## 🎯 Gameplay Integration

### Permanent Hybrid Change
Once acquired, the thong is **permanently bound to Lord Pilsner**. It cannot be sold, dropped, traded, stored, gifted, laundered out of existence, or transferred to another bro. It occupies an equippable slot and *can* be unequipped from the menu — and if it is, the game silently re-equips it after the next rest, with no dialogue, no notification, and no acknowledgement from anyone. Lord Pilsner has never been observed removing it and does not discuss the subject.

> **Template deviation (one-line justification):** the permanent-item template assumes a visible cosmetic; this one is permanent and mechanically live but deliberately almost invisible, because the comedy is entirely in the knowing, not the seeing.

### Sprite Implementation
- **Visibility**: One 2-pixel waistband line above the cargo shorts, visible only in specific animations (sitting, bending, the golden-hour flex, and any victory pose)
- **Layer**: Undergarment layer, beneath every other clothing layer Lord Pilsner can wear, including the Conductor's Tuxedo and the Opera Cape
- **Animation**: No independent motion; rides the hip rig. The waistband line appears and disappears with the existing animation frames — no new frames required
- **Degradation**: Colour ramp shifts across three states by in-game days elapsed since acquisition, per the table above; Lord Pilsner never acknowledges the change

### Distinction From Equipment
N/A — no equippable counterpart exists and none will be authored. There is exactly one of these in the game, it belongs to one bro, and it is not part of any gear line.

**Note**: The thong stacks with every other Lord Pilsner accessory, including the Gold Circle Coin and any Haberdashery purchase, with no conflicts. It is beneath all of them, in every sense he would dispute.

---

## 🗣️ NPC Reactions

### When NPCs Notice The Item
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| Hostel front-desk clerk (laundry service) | *sorts it into the pile without comment, the way she sorts everything, because it is Tuesday* | "She recognized it. She KNOWS what this is." |
| Věra, Midnight Munchies General Store | *one glance, zero questions, rings up the antihistamine* "Anything else." | "Total professional. Discretion. That's respect." |
| Monsieur Aiguille, mid-fitting | *measuring tape pauses for exactly one beat, then continues* "I did not ask. I would like that on the record." | "He's noting my measurements for the archive." |
| Laundromat attendant, Sinfonia | *holds up the machine door, waits, says nothing, keeps waiting* | *don't hear* |
| Sinfonia opera-house cloakroom attendant | *accepts the coat, declines — with a small, immaculate head-shake — to accept anything further* | "Coat check has TIERS, boys. We're above the tier." |

### Callback Dialogue Throughout Game
**Lord Pilsner** (unprompted, to a table of strangers, three cities later):
> "You see a guy in cargo shorts. You do NOT see the full picture. There's a whole SECOND layer to this operation and it is not for public consumption."

**Chadwick** (streaming, cutting away fast):
> "Anyway — anyway — chat, we're not doing the sleeping bag thing today. We've MOVED ON. Smash the ICQ."

**Bradley** (flat, to nobody, on a train):
> "I asked twice whose it was. I've stopped asking."

---

## 🔗 Quest Integration

### Source Quest
- **Quest ID**: `debaucheryville_sidequest_nothing_is_getting_through_01`
- **Quest Name**: "Nothing Is Getting Through"
- **Quest Giver**: None — granted inside the scripted outbreak event `night_event_outbreak_01`; the grant is wired in `Design/World Design/Debaucheryville/interactions/bohemian_riviera_interactions.json` (phase `thong_discovery_reply`), not in any shop or item table
- **Location**: `night_party_zone`, The Bohemian Riviera, Debaucheryville

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| Lord Pilsner's "Spoils of War" dialogue branch (game-wide, tourist/local NPCs) | Item acquired; fires unprompted on a cooldown, in any city, forever |
| The Haberdashery fitting-room beat with Monsieur Aiguille | First fitting after acquisition, any formal-wear purchase |
| Achievement "Mine Now" | Item acquired (automatic — no player action can prevent it) |

### Achievement
- **Achievement Name**: "Mine Now"
- **Description**: "Acquire the leopard-print thong."
- **Hidden Description**: "Claimed ownership of an object whose owner will never be established, and considered the matter closed."

---

## 🎬 Key Story Moments

### The Acquisition
*Morning. Flat grey light. Chadwick holds up an item of clothing he has already decided not to think about.*
> **Chadwick**: "Bro. Whose is this."

*From inside the sleeping bag, without opening his eyes, Lord Pilsner settles the question forever.*
> **Lord Pilsner**: "...Mine now?"

*[ACQUIRED: `item_leopard_print_thong` — Lord Pilsner, permanent]*

### The Fitting
*Haute Couture Haberdashery. Monsieur Aiguille, mid-measurement, encounters the waistband line above the trouser and does not react for exactly one beat.*
> **Monsieur Aiguille**: "I did not ask. I would like that on the record."

*Lord Pilsner, arms out, chin up, radiant*
> "Noted. And respected."

### Post-Credits: The Drawer
*Months later, back home. The Gold Circle Coin is framed on the wall in its shadow box, lit, angled, the way other men mount championship belts.*

*In the drawer directly beneath it, folded — actually folded, deliberately, by hand — is a sun-bleached leopard-print thong. Nobody in this house has ever asked about it. Nobody in this house ever will.*

*He does not throw it out. He is never going to throw it out.*

---

## 🖥️ Performance & Assets

### Sprite Requirements
- **Base Size**: 8×4 pixels (item icon), 2×1 pixel waistband sliver (in-world overlay)
- **Memory**: Negligible — one icon, one sliver overlay, no on-body render
- **Animation**: No additional frames; the sliver rides the existing Lord Pilsner hip rig and appears only in animations that already exist
- **Degradation Variants**: 3 states × 1 character (Lord Pilsner only, always) = 3 sprite variants

### Performance Impact
- No additional draw calls of any consequence (single 2-pixel overlay, culled at distance)
- No particle effects
- No dynamic lighting requirements

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item clearly defined | ✅ |
| Purchase/acquisition documented | ✅ (auto-granted, outbreak morning, acquisition line quoted) |
| Stats and effects specified | ✅ |
| Visual specifications complete | ✅ |
| NPC reactions documented | ✅ |
| Quest integration clear | ✅ |
| Distinction from equipment item (if applicable) | N/A — no equippable counterpart exists and none will be authored |
| Comedy value preserved | ✅ (the joke is Lord Pilsner's pride, start to finish) |
| Bros never achieve self-awareness | ✅ (he never once wonders whose it was) |

---

## 📝 Development Notes

- **BINDING RULE — the original owner is NEVER established.** Not Renata's. Not any named NPC's. Not any unnamed NPC's. No line of dialogue, examine string, tooltip, item description, achievement text, loading-screen tip, art asset, or later content pass anywhere in this repo may answer, hint at, narrow down, or joke toward the answer. Any content that resolves the mystery is a defect and must be reverted. The mystery is permanent canon
- The grant is wired in the quest event (`night_event_outbreak_01`, phase `thong_discovery_reply`, in `interactions/bohemian_riviera_interactions.json`). It is deliberately NOT added to `Design/World Design/Debaucheryville/items/bohemian_riviera_items.json` — this item is never stocked, never priced, never listed in a location item sheet
- Casting is author-locked: the thong goes to **Lord Pilsner**, on every playthrough, with no scene-setup assignment and no variant branch
- Tone guard: the comedy is Lord Pilsner's delusional pride and the group's refusal to discuss it — never body-shame, never a joke about anyone's body, and never a joke at the expense of whoever it might have belonged to (a person the game does not name and does not have)
- No graphic content: the item is never rendered on-body beyond the 2-pixel waistband sliver, in any frame, in any scene, including the outbreak morning
- The examine string must be byte-identical on every examine for the whole game. Do not add a "the more you look at it" variation pass — the flatness IS the joke
- Auto-re-equip after rest must be completely silent: no toast, no log line, no bro dialogue, no achievement ping
- Easter egg: the same rotating wire rack, restocked, three-for-12 Sovs sign visible, is present in the background of a Bohemian Riviera bar-strip frame that Lord Pilsner walks past without ever looking at it
