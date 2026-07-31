# Item Definition: Summer Vacation Trivia Champ Badge

*"Unfortunately, bro, you actually won." - Jaxson Vane, immediately regretting the tape he's now contractually obligated to air*

## 📋 Item Identity
- **Item ID**: `item_trivia_champ_badge`
- **Display Name**: Summer Vacation Trivia Champ Badge
- **Internal Name**: Defective 2003 Party-Favor Sheriff Star
- **Item Type**: Permanent Hybrid (Cosmetic + Passive)
- **Rarity**: Common (bros think it's One-Of-A-Kind)
- **Source**: Hamstradamus @ Fauxst Beach prize podium — win The Bacchanus Beach Beatdown

---

## 🎭 The Deception

### What The Item Actually Is
A ~€0.008 plastic gold kids' sheriff badge, stamped "SUMMER VACATION TRIVIA CHAMP 2003" in glitter print that was already flaking before it left the box. Shady Productions bought a pallet of these decades ago as bulk mystery merch for a summer-special trivia gauntlet nobody expected a tourist to survive, let alone win. A badge is a nonsensical prize for a trivia contest — it's not even shaped like a trophy, a medal, or anything you'd give a "champion" of anything — but it was cheap, it was there, and no local contestant had ever lost before this summer, so nobody at Shady Productions ever had to think harder than that.

### What The Bros Believe It Is
"This is basically a Mensa card, bro. Like, a WEARABLE one. Law enforcement doesn't hand these out to just anybody — you have to EARN jurisdiction. I'm not saying I'm a cop now, I'm saying I'm cop-ADJACENT. Intellectually deputized. This star means something."

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | N/A (prize only — not sold anywhere; only obtainable by winning The Bacchanus Beach Beatdown) |
| **Actual Value** | €0.008 |
| **Resale Value** | €0 (worthless) |
| **Can Be Sold** | No (bros would sooner surrender a kidney than the badge) |
| **Can Be Dropped** | No (permanent cosmetic) |
| **Can Be Traded** | No |

---

## 🎨 Visual Specifications

### Physical Appearance
| Attribute | Description |
|-----------|--------------|
| **Material** | Gold-painted injection-molded plastic |
| **Shape** | Five-point sheriff star, ~4cm across |
| **Closure** | Bent metal pin (bent at manufacture, never fixed) |
| **Text/Markings** | "SUMMER VACATION TRIVIA CHAMP 2003" stamped in flaking glitter print, curved around the star's face |
| **Finish** | Gold paint over gray plastic base, visibly thin at the star's points even on Day 1 |

### Degradation Over Time
| Days Worn | Visual State |
|-----------|--------------|
| Days 1-3 | Pristine — gold paint intact, glitter text fully legible, pin holds a shirt without sagging |
| Days 4-7 | Worn — gold paint flaking off the star's points and edges, glitter print starting to shed in the wind |
| Days 8+ | Crusty — bare gray plastic showing through at every high point, pin rusted orange from repeated river spray, text now reads "SUM ER VAC TION T IVIA CH MP 2 03" where the glitter has worn away completely |

---

## 📊 Stats & Effects

### Direct Stats
```
Bravado:              +3 ("the law of the beach")
Charm (Tourists):     +1 (fellow tourists respect a badge, any badge)
Charm (Locals):       -1 (they watched the episode)
```

### Passive Effects
| Effect | Description |
|--------|--------------|
| **Aggressive Guessing** | 10% chance on taking damage: the wearer shouts a confidently incorrect "fact" at the enemy ("ACTUALLY, hexagons are INFINITE!") and inflicts the existing **Embarrassed** status on all enemies for 1 turn |
| **Deputy of Denial** | Wearer is immune to the first instance of **Embarrassed** applied to him each battle — the badge means he simply cannot be humiliated first |

### What It Does NOT Do
- ❌ Grant law-enforcement authority of any kind, anywhere
- ❌ Deputize anyone, including the wearer
- ❌ Prove intelligence, trivia knowledge, or the ability to read
- ❌ Impress anyone who can read
- ❌ Open VIP doors, velvet ropes, or any door with a bouncer standing in front of it

---

## 🎯 Gameplay Integration

### Permanent Hybrid Change
Once won, the badge becomes **permanently pinned** to the winning bro's chest on his character sprite for the rest of the game, visible in all animations. It cannot be removed, hidden, unequipped, or given to another bro. Degradation is purely cosmetic and layers on top of the mechanical passives, which never weaken regardless of paint condition.

### Sprite Implementation
- **Visibility**: Always visible, pinned to the chest, over whatever outfit the winning bro is wearing
- **Layer**: Accessory overlay, torso layer
- **Animation**: Rides with the torso in all animation frames; the bent pin gives it a slight independent jiggle during running/combat animations
- **Degradation**: Visual state updates automatically based on in-game days elapsed since the win, per the table above

---

## 🗣️ NPC Reactions

### When NPCs Notice The Badge
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| Velvet Curtain bouncer | "That is... child's toy, yes?" | "That is a champion's decoration, yes." |
| Kid outside a party supply store | "Hey, we SELL those! They're in the birthday aisle, next to the pirate eyepatches." | "Underground collector's circuit. Deep cuts only." |
| Off-duty real police officer | "That's not a badge. That's not even a convincing FAKE badge." | "Professional jealousy. Happens to every real deputy." |
| Boardwalk trinket-cart kid | "You know I sell the exact one, right? Ten koruna, no waiting in a river." | "That's called competition, my dude. Mine's got provenance." |
| Locals who watched the episode air | *phones already out, recording, whispering to each other in Czech-parody* | "Fans. We have fans now." |

### Callback Dialogue Throughout Game
**Lord Pilsner** (as Badge-Bearer, holding court at Three Crown Keg Haus):
> "You see this? This is JURISDICTION, bro. I could probably write you a ticket right now if I wanted to."

**Chadwick** (as Badge-Bearer, live on socials):
> "Day 1 with LEGAL trivia authority. They don't call it a badge for nothing. #champion #cop-adjacent #europe"

**Bradley** (as Badge-Bearer, to a table of confused vacationers):
> "It's not that I outrank regular tourists. It's just that I technically could, if the situation called for it."

---

## 🔗 Quest Integration

### Source Quest
- **Quest ID**: `debaucheryville_sidequest_bacchanus_beach_beatdown_01`
- **Quest Name**: "The Bacchanus Beach Beatdown"
- **Quest Giver**: Petra the Production Assistant
- **Location**: Fauxst Beach, The Bohemian Riviera

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| "Trivia Champion of Europe" dialogue options | Badge equipped, available game-wide in any NPC conversation with a trivia-adjacent branch |
| Velvet Curtain Club "flash the badge" scene | Winning bro's first attempt to enter the club while wearing the badge |
| Achievement "Beach's Finest" | The Bacchanus Beach Beatdown completed with a WIN outcome |

### Achievement
- **Achievement Name**: "Beach's Finest"
- **Description**: "Outsmart Fauxst Beach's toughest trivia gauntlet and take home the star."
- **Hidden Description**: "Answer trivia better than two launched friends and one guy who wasn't trying"

---

## 🎬 Key Story Moments

### The Pinning Ceremony
*Hamstradamus, wizard hat askew over a beach-appropriate speedo, produces the badge from somewhere on his person nobody wants to think too hard about*
> "The star chooses. The star has chosen. Wear it, champion, and know: by the year Y2K plus twenty-six, a hamster in a speedo will have told you the truth, and you will not have listened."

*He pins it to the winning bro's chest. It is immediately crooked.*

**Winning bro** (any of the three):
> "I feel... powerful. Like the beach itself just deputized me."

### The Velvet Curtain Flash
*Winning bro approaches the Velvet Curtain Club door, badge gleaming (relatively), and taps it twice like a TV detective*
> "We're good here. Trivia Champion. You've probably heard."

*Bouncer looks down at the badge, then back up, expression unchanged*
> "That is... child's toy, yes?"

*Winning bro, without breaking stride*
> "That is a champion's decoration, yes. Glad we're on the same page."

*The bouncer does not move. Nobody is on the same page.*

### Post-Credits: The Real Cop
*Six months later, the badge now bare gray plastic with a rust-orange pin, the winning bro corners an actual uniformed police officer outside a chain restaurant*
> "Professional courtesy, right? One badge to another?"

*The officer looks at the star for a full three seconds*
> "That's not a badge. That's not even a good fake badge."

*Winning bro, nodding slowly, entirely unbothered*
> "Right, right. Can't be seen fraternizing on duty. I get it. Respect the uniform."

---

## 📱 Mobile Optimization

### Sprite Requirements
- **Base Size**: 6×6 pixels per badge
- **Memory**: Minimal (single small overlay sprite, no particle system)
- **Animation**: Syncs with torso movement; no additional animation frames needed beyond the existing torso rig
- **Degradation Variants**: 3 states × 3 characters (any bro can be the winner) = 9 sprite variants

### Performance Impact
- Negligible additional draw calls
- No particle effects
- No dynamic lighting requirements

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

- Badge MUST be visible on whichever bro's sprite wins the Beatdown — position must read correctly on all three body types (chest-pinned, over outfit)
- Degrading glitter text ("SUM ER VAC TION T IVIA CH MP 2 03") must remain legible on close inspection/zoom at the Day 8+ state — it's a punchline, not noise
- Degradation is purely visual and mechanical; bros never acknowledge the badge's condition changing, no matter how bare the plastic gets
- Easter egg idea: a party supply store window display featuring the identical badge, priced and visible, that the badge-wearing bro walks past without ever noticing
- Achievement "Beach's Finest" hidden description should only reveal after unlock, per standard achievement UI behavior
- Aggressive Guessing's shouted line pool should rotate (hexagons, etc.) so it doesn't repeat every proc within a single battle
