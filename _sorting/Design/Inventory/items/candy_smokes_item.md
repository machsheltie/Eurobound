# Item Definition: Puff-Puff-Powder™ Chalk 'n' Ash Candy Smokes

*"Don't smoke it, just bite the end off." - Aaron the Unflappable, handing over a carton he did not need to hand over*

## 📋 Item Identity
- **Item ID**: `item_candy_smokes`
- **Display Name**: Puff-Puff-Powder™ Chalk 'n' Ash Candy Smokes
- **Internal Name**: Worn carton of chalk-and-sugar candy sticks with red-dipped tips
- **Item Type**: Permanent Hybrid (Novelty + Use Effect) — **not a consumable**; the carton never runs out and cannot be depleted, sold, or discarded
- **Rarity**: Common (bros think it's Regional / Import / "you can't get these back home")
- **Source**: Aaron the Unflappable (`sinfonia_npc_aaron_unflappable_01`) @ Aaron's Corner Table, The Black-Tie Backroom, Sinfonia — granted at Beat 8 of `blacktie_event_kings_were_humming_01`

---

## 🎭 The Deception

### What The Item Actually Is
A carton of children's candy cigarettes. Chalk-white compressed sugar sticks, roughly 7cm, dipped red at one end to suggest a lit ember, printed on the carton with a brand name — **Puff-Puff-Powder™ Chalk 'n' Ash** — in a typeface that has been legally distinct from a real cigarette brand since 1974 and not one letter further. They cost about forty cents a carton and are sold in petrol stations, corner shops, and the checkout aisle of every supermarket in Europe, at child height, next to the plastic whistles.

Aaron recently quit smoking. These are the substitute, and the ritual he has built around them — stir, drag, CRUNCH, fresh one — is the reason he had a carton on the table at one in the morning to give away. The carton the party receives is worn soft at the corners from several thousand openings and it is not visibly less full than it was on the felt. It will never be visibly less full than it was on the felt. Nothing in the game investigates this.

### What The Bros Believe It Is
"Okay, so first of all, you cannot get these in the States, they banned these, which — tells you something. Second of all, this is what the guy who took our whole stake was running on. Whatever's IN these, he had it, we watched him have it, and now we have it. That's not candy, bro. That's *his* thing. He gave us his thing."

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | N/A (gift only — never sold by any vendor in the game, in any city) |
| **Actual Value** | €0.40 per carton, available within four minutes' walk of every location the party visits |
| **Resale Value** | €0 (worthless) |
| **Can Be Sold** | No — no vendor will take them, and the bros would not part with them regardless |
| **Can Be Dropped** | No (permanent party item) |
| **Can Be Traded** | No — but the bros offer them to NPCs constantly, unprompted, forever |

---

## 🎨 Visual Specifications

### Physical Appearance
| Attribute | Description |
|-----------|--------------|
| **Material** | Compressed sugar and chalk-fine dextrose, red food-dye tip; carton is 250gsm card |
| **Stick Dimensions** | ~7cm long, ~7mm across, blunt-cut at the unlit end |
| **Closure** | Flip-top carton lid, hinge long since gone soft, held shut by habit rather than by structure |
| **Text/Markings** | "PUFF-PUFF-POWDER™" across the front in the legally-distinct typeface; "CHALK 'N' ASH" beneath it; a small cartoon cloud with a face; a fine-print line on the base panel nobody in the party has ever read |
| **Finish** | Matte white sticks, glossy red tip, carton edges furred and soft with a faint fingerprint sheen on the flip-top |

### Per-Character Variants — the chalk ring
| Character | Ring Placement | Detail |
|-----------|---------------------|----------------------|
| Lord Pilsner | Full ring, wide, dead centre | Applied with real commitment; he does not blot, he does not check, and he holds court for the entire duration with it on |
| Chadwick | Ring smeared to one side | From filming himself at an angle; he wipes the wrong side every time and gets it worse |
| Bradley | Thin, precise, almost neat | Then he licks his lips once and it becomes a moustache. He does not know. Nobody tells him. |

### Degradation Over Time
| Days Worn | Visual State |
|-----------|--------------|
| Days 1-3 | Carton soft at the corners, print crisp, flip-top holds. Sticks white, tips bright red |
| Days 4-7 | Corners furred through to the grey board, one crease across the cartoon cloud's face, tips fading to pink from pocket friction |
| Days 8+ | Carton visibly ancient — split at one bottom corner, print worn off the "™", cloud's face gone entirely, held together at the seam. **Exactly as full as it was on Day 1.** |

---

## 📊 Stats & Effects

### Direct Stats
```
Perceived Confidence:  +4%  (this stat does not exist; it is displayed anyway)
Bravado:               +2   (on use, 60 seconds, does not stack with itself)
Charm (Children):      +1   (they know what it is; they respect a man with a carton)
Charm (Anyone Else):    0   (they also know what it is)
```

### Passive Effects
| Effect | Description |
|--------|--------------|
| **The Carton Never Empties** | Infinite uses, permanently, in every city, for the rest of the game. No counter, no cooldown display, no restock prompt. The inventory tooltip does not show a quantity because there isn't one |
| **The Offer** | Whenever a bro is in dialogue with any NPC while the buff is active, he offers them one. The NPC's decline is folded into their existing dialogue; no unique refusal lines are authored, and no NPC ever accepts |
| **Chalk Ring** | On use, a white ring is applied to the using bro's mouth sprite for the buff duration plus four in-game minutes. It is never wiped clean in a single wipe |

### What It Does NOT Do
- ❌ Contain nicotine, caffeine, sugar substitutes, or any substance whatsoever beyond sugar, chalk and red dye
- ❌ Confer, transfer, or approximate whatever the bros believe Aaron was running on
- ❌ Help anybody quit anything
- ❌ Light. It does not light. It never lights, on any attempt, in any weather, with any lighter
- ❌ Read as a cigarette to any observer over the age of six, at any distance, in any lighting

---

## 🎯 Gameplay Integration

### Permanent Hybrid Change
Once granted, the carton is a **permanent party item** — key-item slot, no equip, no unequip, no drop, no sell, no destroy. Any bro may use it at any time from the inventory screen; the buff applies to the user only, the carton belongs to the party. It survives every city transition and every story beat and is present in the final save.

### Sprite Implementation
- **Visibility**: The carton rides in Lord Pilsner's jacket pocket by default, visible as a small silhouette bulge, and is drawn in-hand during the use animation. The chalk ring is drawn on the using bro's face sprite for the buff duration
- **Layer**: Carton — hand/prop layer during use, torso-pocket overlay otherwise. Chalk ring — face overlay, above the mouth layer
- **Animation**: The use animation is a three-frame quote of Aaron's ritual — raise, dramatic drag, bite — with the same **CRUNCH** audio cue, mixed identically. The bros perform it slightly wrong. No frame of the bro version is reused from `aaron_the_unflappable.png` and no frame of Aaron's is reused for theirs
- **Degradation**: Carton visual state advances on in-game days elapsed since acquisition, per the table above. Fullness never changes at any state

---

## 🗣️ NPC Reactions

### When NPCs Notice The Item
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| Sinfonia café barista (Grounds For Concern) | "That's a sweet. For children. There is a bowl of them by the till, they are free." | "Free samples. They're seeding the market here." |
| Backroom server | *sets down the tray, waits, does not react at all, moves on* | "That's respect. That's a nod from the house." |
| Corner-shop owner, any city | "Forty cents. The blue ones are the same but mint." | "He's got a *mint* line. That's a whole other tier." |
| A seven-year-old outside a supermarket | "I have those." | *(Lord Pilsner, warmly)* "Yeah you do, buddy. Yeah you do." |
| Publandia bartender | *slides an actual ashtray down the bar without breaking eye contact* | "Ashtray. So they're allowed in here. Noted." |

### Callback Dialogue Throughout Game
**Lord Pilsner** (holding court, buff active, ring fully applied):
> "See, you gotta bite it. Everybody wants to smoke it. You bite it. That's the whole thing. That's what he told me personally, and I don't repeat everything he told me."

**Chadwick** (to camera, at any scenic overlook in any city):
> "Day nineteen on the Puff-Puff. Chat, I'm not gonna lie to you, my palate has changed. Everything tastes like chalk now, but in a way where I think I'm ahead of it."

**Bradley** (flat, to a table of strangers, chalk moustache):
> "There's no filter on these. Which means it's harsher. Which means it's more authentic."

---

## 🔗 Quest Integration

### Source Quest
- **Quest ID**: `sinfonia_sidequest_the_kings_were_humming_01`
- **Quest Name**: "The Kings Were Humming"
- **Quest Giver**: Aaron the Unflappable (not in any transactional sense — the carton is a gift)
- **Location**: Aaron's Corner Table (`aarons_corner_table`), The Black-Tie Backroom, Sinfonia

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| "Bite, Don't Smoke" use action (game-wide) | Granted at Beat 8 of `blacktie_event_kings_were_humming_01` |
| The chalk-ring visual state | Any use of the item, any bro, any city |
| Bradley's one-time lighting attempt scene | First use of the item outdoors after leaving Sinfonia |

### Achievement
- **Achievement Name**: "Perceived Confidence"
- **Description**: "Bite the end off."
- **Hidden Description**: "Use a forty-cent carton of children's candy one hundred times."

---

## 🎬 Key Story Moments

### The Grant
*Aaron slides the worn carton across the felt with two fingers, immediately after taking everything the party posted at the door.*
> "Here. Take one. It helps with the hand jitters when you lose your shirt. Don't smoke it, just bite the end off. You want a hit of my White Russian to wash it down? No? Suit yourselves."

*[ACQUIRED: `item_candy_smokes` — party, permanent]*

**Chadwick** *(taking two)*:
> "One for the road, one for the archive."

### The Lighting Attempt
*Outside, first use after Sinfonia. Bradley has a lighter he bought in Debaucheryville and has never once used. He puts a candy cigarette in his mouth and lights it. It does not catch. It chars. It smells overwhelmingly of burnt sugar and the red tip runs down onto his hand.*

**Bradley** *(entirely unbothered, examining the melted end)*:
> "Slow burn. That's a quality thing, actually. The cheap ones go up like paper."

*He bites the end off. It is the wrong end. The CRUNCH is the same.*

### The Long Tail
*Months later, any city, the carton now split at one bottom corner and worn through to the grey board. Lord Pilsner opens it, in front of a woman who has not asked, and turns it toward her.*

**Lord Pilsner**:
> "You want one? They do 'em right here."

*They do not do them right here. They do them everywhere. He has never once been to the place they do them.*

---

## 📱 Mobile Optimization

### Sprite Requirements
- **Base Size**: 16×24 pixels per carton; 12×4 pixels per chalk ring overlay
- **Memory**: Minimal — one prop sprite, three degradation variants, three per-bro ring overlays
- **Animation**: Three-frame use animation (raise / drag / bite) reusing each bro's existing hand-to-face rig; no new skeleton required
- **Degradation Variants**: 3 carton states × 1 shared prop = 3 variants; ring overlays 1 state × 3 characters = 3 variants

### Performance Impact
- Negligible additional draw calls (single prop, single face overlay)
- No particle effects — the chalk ring is a sprite overlay, not a particle system, and no smoke particle may ever be attached to this item
- No dynamic lighting requirements; the red tip does not emit

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

- **Not a consumable. Author-locked.** No quantity field, no stack count, no "last one" warning, no restock vendor. If a later pass adds a use counter to this item, that pass has broken it
- **The carton never empties and this is never investigated** — no quest, no examine chain, no NPC remark, no achievement text, no tooltip. It is a fact of the world, offered once and dropped
- The **CRUNCH** cue is shared with Aaron's ritual and must be the identical sample, mixed identically, so it is recognisable from another room when a bro does it in a different city
- "+4% Perceived Confidence" is displayed in the item tooltip as a real stat line, in the same font and colour as real stat lines, and is not asterisked, footnoted, or explained anywhere in the UI
- Bradley's chalk moustache must be visible at 64px and must never be commented on by any character, in any scene, ever
- Easter egg: a bowl of the identical candy sticks, free, sits by the till at Grounds For Concern from the party's first visit — before Sinfonia's Backroom is ever discovered. It is never pointed at
- Grant is scene-triggered only (`blacktie_event_kings_were_humming_01`, Beat 8) and must be idempotent against the one-time-scene flag; see the quest file's Engine Requirements block
