# Item Definition: The Shark Fin

*"You caught me. Take it — I keep one ready." - Herr Falsch, handing it over with better manners than he was beaten with*

## 📋 Item Identity
- **Item ID**: `item_shark_fin`
- **Display Name**: The Shark Fin
- **Internal Name**: Pewter dorsal-fin lapel pin, novelty-supplier stock, ordered by the dozen
- **Item Type**: Permanent Hybrid (Cosmetic + Passive)
- **Rarity**: Common (bros think it's One-Of-A-Kind, Never Awarded Before, "the only one in Europe")
- **Source**: Herr Falsch (`sinfonia_npc_herr_falsch_01`) @ the Private Boxes, The Black-Tie Backroom (`sinfonia_operahouse_blacktie_backroom_01`), Sinfonia — awarded on defeating him

---

## 🎭 The Deception

### What The Item Actually Is
A pewter lapel pin shaped like a shark's dorsal fin, about 4cm tall, mounted on a small backing card stamped with a spade. It costs about four euro and comes from a novelty supplier that also does the Backroom's cufflink-shaped swizzle sticks and the cloakroom's numbered brass tags. Herr Falsch orders them **by the dozen**, keeps the box in his coat's inside pocket, and has one on his person at all times.

This is not a scheme. It is manners. Herr Falsch has been cheating in that room for a very long time and takes the entirely sincere view that anybody sharp enough to catch him at it has earned something to take home, and that having to go and find a trophy afterward would be graceless. He has handed nine of these over this decade. He remembers every one of them. He would not dream of mentioning the other eight.

The pin is real, the win is real, and the fight is genuinely hard. The only thing that is not true about the Shark Fin is the part the bros supply themselves.

### What The Bros Believe It Is
"Nobody has ever done this. Understand me — nobody. That man has been sitting in that room for TWENTY YEARS and he had that pin in his pocket for TWENTY YEARS waiting for somebody good enough, and boys, he did not know it was gonna be an American in a rented tuxedo. That's not a souvenir. That's a *title*. There is one of these and I'm wearing it."

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | N/A (boss reward only — never sold by any vendor in the game) |
| **Actual Value** | €4 (€38 the dozen, plus postage) |
| **Resale Value** | €0 (worthless — and the bros would sooner walk into The Bacchanus than sell it) |
| **Can Be Sold** | No |
| **Can Be Dropped** | No (permanent cosmetic) |
| **Can Be Traded** | No — whichever bro landed the finish wears it and the argument about that is settled permanently on the walk out |

---

## 🎨 Visual Specifications

### Physical Appearance
| Attribute | Description |
|-----------|--------------|
| **Material** | Cast pewter, unlacquered, with the mould's parting line still visible along the trailing edge |
| **Height** | ~4cm from the base plate to the tip of the fin |
| **Closure** | Butterfly clutch, slightly loose, which the wearer discovers by losing the pin twice and finding it both times |
| **Text/Markings** | No text on the fin. The supplier's four-digit stock number is stamped into the underside of the base plate, upside down, where the wearer will never look |
| **Finish** | Bright grey when new; pewter tarnishes fast and unevenly, and the trailing edge goes first |

### Degradation Over Time
| Days Worn | Visual State |
|-----------|--------------|
| Days 1-3 | Bright, sharp, sits proud on the lapel; the clutch holds |
| Days 4-7 | Tarnish creeping along the trailing edge and into the mould line; the fin now sits about eight degrees off vertical and stays there |
| Days 8+ | Dull grey-brown all over, the tip scuffed pale from doorframes, one clutch replaced with a folded bit of a cigarette carton. The stock number on the underside is still perfectly legible |

---

## 📊 Stats & Effects

### Direct Stats
```
Bravado:                    +2  (defeated the room's hardest opponent, on the level, in front of the house)
Charm (Backroom staff):     +1  (they saw it; they were pleased; they are professionals about it)
Charm (Backroom regulars):  -1  (they have seen the pin before)
```

### Passive Effects
| Effect | Description |
|--------|--------------|
| **The Slow Breath** | At the Backroom's **real, playable** poker tables, opponent tell animations hold one beat longer, making an existing learnable tell easier to catch. It changes the wearer's read window and nothing else |
| **Settled Business** | Backroom staff serve the wearer first at the bar and the cage processes his collateral without the queue. Neither is comped; both are courtesy |
| **Marked Cards On The Felt** | Unlocks the "Shark Slayer" selfie variant at the High Stakes Salon spot — Herr Falsch's marked deck laid out on the table behind the wearer |

### What It Does NOT Do
- ❌ Reduce the house edge on poker, roulette, or blackjack — the documented edge is unchanged and remains documented
- ❌ Grant High Roller status, Private Box access, or any door it did not already open
- ❌ Make the wearer a card counter, a card sharp, or a better player at any table in any city
- ❌ Function anywhere outside The Black-Tie Backroom, in any way, at all
- ❌ Prove that the wearer is the only person who has ever been given one

---

## 🎯 Gameplay Integration

### Permanent Cosmetic Change
Once awarded, the fin is **permanently pinned to the winning bro's lapel** for the rest of the game, visible in every animation and every subsequent scene, in every city, over whatever he is wearing — including the states in which he is wearing nothing that has a lapel, where it is simply attached to him. It cannot be removed, unequipped, hidden, or reassigned to another bro.

### Sprite Implementation
- **Visibility**: Always visible, left lapel, high; the eight-degree tilt from Day 4 onward is permanent once it arrives
- **Layer**: Accessory overlay, torso layer, drawn above outfit and above `item_trivia_champ_badge` if both are present on the same bro
- **Animation**: Rides with the torso rig; the loose clutch gives it a one-frame lag on hard direction changes in the run cycle
- **Degradation**: Tarnish state advances on in-game days elapsed since the award, per the table above

---

## 🗣️ NPC Reactions

### When NPCs Notice The Fin
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| Anton the Doorman | "Ah. He gave you the fin." *(no change of expression, no further comment, steps aside)* | "He *gave*. Past tense. Anton's already heard about it." |
| Madame Karten | "Darling. How wonderful for you. He does love that hand." | "She's shaken. That's a woman rethinking her whole floor." |
| Siegfried at the coat check | *takes the jacket, sees the pin, sets a second wafer bar on the counter, says nothing at all* | "Coat guy KNOWS. Coat guys always know first." |
| Novelty-shop kid, Kaffeehaus Row | "We have those. Fin, anchor, or the little skull. Four euro." | "Knockoffs. Somebody's already bootlegging me." |
| Publandia bartender, weeks later | "What's the fish for?" | "It's not a fish. It's a *classification*." |

### Callback Dialogue Throughout Game
**Lord Pilsner** (as Fin-Bearer, to anyone within eight feet):
> "There's a room in Sinfonia. You don't get told about it, you find it. And in that room there's a man who has never lost, and now there is a man who has lost once, and the difference between those two sentences is standing in front of you wearing the reason."

**Chadwick** (as Fin-Bearer, filming the lapel at an angle):
> "This doesn't photograph. Chat, I've tried it in four lights. You have to be *there*. Which honestly makes it rarer, if you think about the economics."

**Bradley** (as Fin-Bearer, flat, to a barman who did not ask):
> "It's a dorsal fin. Which is the fin they show you. There are other fins."

---

## 🔗 Quest Integration

### Source Quest
- **Quest ID**: `sinfonia_sidequest_the_card_shark_01` *(provisional — "The Card Shark" is listed in the Backroom location file's Quest Integration but has no quest file yet; confirm the ID when it is authored)*
- **Quest Name**: "The Card Shark"
- **Quest Giver**: Nobody. The party discovers Herr Falsch is cheating, or loses €1,000+ to him, and challenges him directly
- **Location**: The Private Boxes, The Black-Tie Backroom, Sinfonia

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| "Shark Slayer" selfie variant at the High Stakes Salon | Fin worn (which it permanently is) + High Roller status for salon access |
| "The Slow Breath" read window at the Backroom's real poker tables | Automatic on award |
| Cage and bar priority inside the Backroom | Automatic on award |

### Achievement
- **Achievement Name**: "The Shark Slayer"
- **Description**: "Catch Herr Falsch and beat him anyway."
- **Hidden Description**: "Become the ninth person this decade to be handed a four-euro pin by a very polite man."

---

## 🎬 Key Story Moments

### The Handover
*The Private Box. The marked deck is on the table, face up, where the party put it. Herr Falsch straightens his cuffs, unhurried, and reaches into his coat's inside pocket — and there is a small flat box in there, and he takes one pin out of it, and closes the box, and puts the box back.*

**Herr Falsch** *(with total courtesy, no bitterness anywhere in it)*:
> "You caught me. Take it — I keep one ready."

*He pins it on himself, properly, and steps back to check that it is straight. It is the most respectful thing that happens to any of them in Sinfonia and none of the three of them notice.*

**Lord Pilsner** *(to the room, at volume)*: "First one! First one he's ever given out!"

*Herr Falsch does not correct him. It would be rude, and he is not a rude man.*

### The Photograph
*The High Stakes Salon selfie spot. Chadwick lines up the shot with the marked deck laid out on the felt behind him.*

**Chadwick**:
> "Get the cards in. The cards are the *evidence*."

*The pin is a four-centimetre grey object on a burgundy lapel in low tungsten light. It is, in every one of the eleven photographs, an indistinct smudge.*

**Chadwick** *(reviewing them)*:
> "Yeah, that's about what I expected. This is a live-audience piece."

### Weeks Later
*A Publandia pub. The pin is tarnished, tilted eight degrees, and held on with a folded piece of cigarette carton. A man two stools down looks at it for a while.*

**Man**:
> "What's the fish for?"

**Bradley** *(flat, without turning)*:
> "It's not a fish. It's a classification."

*The man nods and goes back to his pint. Both of them consider the matter closed for entirely different reasons.*

---

## 📱 Mobile Optimization

### Sprite Requirements
- **Base Size**: 32×48 pixels (`shark_fin.png`, per the Backroom's sprite manifest)
- **Memory**: Minimal — one small overlay sprite, three tarnish states, three character variants
- **Animation**: Syncs with the torso rig; one-frame lag on direction change, no additional frames required
- **Degradation Variants**: 3 tarnish states × 3 characters (any bro can land the finish) = 9 sprite variants

### Performance Impact
- Negligible additional draw calls
- No particle effects; the pewter does not glint, spark, or emit
- No dynamic lighting requirements — and per the Key Story Moments, the pin must read as an indistinct smudge in the salon's tungsten light, which is a rendering requirement rather than a bug

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

- **Herr Falsch keeps his dignity.** He cheats, he is caught, he loses, and he is gracious about all three. He is never humiliated by the text, the art, or the audio, and his box of pins is a courtesy rather than a punchline at his expense. The joke is the bros' certainty that they are the first
- **Nobody says "the other eight."** No NPC, narrator line, tooltip, or achievement string counts the previous winners out loud. The box in his coat is visible in the handover frame and that is the entire delivery
- The existing boss-victory achievement **"Card Counter"** and the location file's **"The Shark Slayer"** both fire off this fight per the Backroom's canon; this item's achievement is "The Shark Slayer." Confirm both against the boss encounter when "The Card Shark" gets a quest file, and do not create a third
- The supplier's four-digit stock number on the underside of the base plate must be legible on close inspection/zoom — it is a punchline, not noise, and it is the only place the truth is written down
- **"The Slow Breath" is a read-window change only.** It must never be implemented as an odds modifier, a hidden-card reveal, or a house-edge reduction, and it must not stack with or overlap Siegfried's "Gambler's Insight" couchsurf effect
- The fin functions **only** inside The Black-Tie Backroom. It travels with the wearer to every other city and does precisely nothing there, permanently, and no bro ever notices this
- Degradation is purely visual; the bros never acknowledge the tarnish, the tilt, or the cigarette-carton clutch, no matter how bad it gets
