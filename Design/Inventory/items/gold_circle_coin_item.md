# Item Definition: The Gold Circle Coin

*"the condom of champions, the one and only… nothin' is gettin' through this sucker."* - the legend, quoted verbatim by three men who have never once been champions of anything

## 📋 Item Identity
- **Item ID**: `item_gold_circle_coin`
- **Display Name**: The Gold Circle Coin
- **Internal Name**: A single gold-foil prophylactic, molded 1990, screen-canon, sealed
- **Item Type**: Quest Item (equippable accessory — party-wide effect, never sellable, droppable, or tradeable)
- **Rarity**: One-Of-A-Kind (bros think it's One-Of-A-Kind — for the first and only time in the game, they are correct)
- **Source**: Monsieur Aiguille's locked vitrine, *Objets d'Héritage*, Accessories Alcove, Haute Couture Haberdashery, Sinfonia — obtained via PATH A (Valued Client + errand) or PATH B (after-hours, formal wear)

---

## 🎭 The Deception

### What The Item Actually Is
**The Deception, inverted.** Every other trophy in this game is carnival-grade plastic sold to men who cannot read a receipt. This one is not. The Gold Circle Coin is exactly what the legend says it is: a gold-foil-wrapped piece of cinema history, molded in 1990, sealed, never opened, and — impossibly, absurdly, canonically — it works. Equipped by any one bro, it suppresses `the_herp` across the entire party. The shimmer stops. The Groin Blurts stop. NPCs stop stepping back. It is the only item in Eurobound that fully delivers on its own legend, and it delivers *harder* than the legend promised, because the legend only ever claimed to protect one man.

Monsieur Aiguille knows precisely what he is holding. He has known for years. He does not display it with the cufflinks; he displays it under glass, on velvet, filed under *Objets d'Héritage*, beside a placard that reads: "Molded 1990. A piece of cinema history. **It is not for sale. It is for aspiration.**"

### What The Bros Believe It Is
"It's a CHAMPIONSHIP BELT, bro. Miniature. Gold. You don't WEAR a belt like this, you CARRY it, and it carries YOU. And the best part? The poison ivy's basically cleared up on its own. Immune system. European air. We're built different over here."

*(They believe they beat the rash. They believe the Coin is a commemorative object marking the victory. At no point does any bro connect the item on the lanyard to the absence of the symptom, and at no point does the game let them.)*

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | Not for sale at any price. PATH A costs €500 in unrelated Haberdashery spend (existing Valued Client tier) plus one absurd errand for Monsieur Aiguille; PATH B costs a full set of formal wear bought from the same shop, plus nerve |
| **Actual Value** | Uninsurable. Aiguille has been offered numbers and has declined them without hearing them out |
| **Resale Value** | €0 — no vendor in any city will take it, and the bros would not offer |
| **Can Be Sold** | No. Every shop UI returns Aiguille's line back at the player: "It is not for sale. It is for aspiration." The one thing the bros ever agree with him on |
| **Can Be Dropped** | No (quest-critical; suppression must remain party-available for the rest of the game) |
| **Can Be Traded** | No. It is one and only. There is nothing to trade it against and nobody willing |

---

## 🎨 Visual Specifications

### Physical Appearance
| Attribute | Description |
|-----------|-------------|
| **Material** | Mirror-gold foil laminate, sealed, contents undisturbed since molding |
| **Diameter** | ~3.6cm foil disc, crimped edge |
| **Seal** | Factory crimp, unbroken — the seal is the whole point and is never broken on screen, in any branch, ever |
| **Text/Markings** | Embossed ring lettering around the rim; a small stamped mold date reading **1990** at the six o'clock position |
| **Finish** | High-polish gold that catches every light source in a room it is not the brightest object in |

### Presentation States
| State | Visual |
|-------|--------|
| In the vitrine | Centered on black velvet under a single spot, glass between it and everyone, placard angled for reading |
| Equipped (PATH A) | Carried in the slim burgundy Haberdashery presentation sleeve Aiguille hands over with the item, because he insists |
| Equipped (PATH B) | Carried loose in an opera-cape inside pocket, no sleeve, faint pocket-lint halo the bros never brush off |

### Degradation Over Time
| Days Worn | Visual State |
|-----------|--------------|
| Days 1-3 | Pristine. Gold unmarked, seal intact, mold date crisp |
| Days 4-7 | Pristine. Thumbprints accumulate on the presentation sleeve; the Coin itself is untouched, because whichever bro has it will not stop showing it to people and will not let them hold it |
| Days 8+ | Pristine. The Coin does not degrade. Nothing in this game degrades less. The bros degrade around it — sun-shot, limping, still scratching out of muscle memory — while the one genuinely excellent object they have ever obtained sits in its sleeve looking exactly as it did in 1990 |

---

## 📊 Stats & Effects

### Direct Stats
```
Herp Suppression:  ACTIVE (party-wide — all three bros, while ANY one bro has it equipped)
Charm:             +0 flat (the Coin does not flatter; `the_herp`'s -2 Charm simply stops applying)
Bravado:           +4 ("aura of champions" — the bros' word for it, and for once nobody corrects them)
Composure:         +2 (no Groin Blurts can interrupt dialogue while suppression is active)
```

### Passive Effects
| Effect | Description |
|--------|--------------|
| **Aura of Champions** | While equipped by any bro, `the_herp` is fully suppressed on all three simultaneously. Romance/couchsurf attempts stop auto-routing to rejection scenes and resolve normally; every lady's post-cure callback line becomes available on re-attempt |
| **Shimmer Off** | The waist-level `heat_shimmer` particle is disabled party-wide the instant the Coin is equipped. NPCs stop the half-step back within one dialogue beat |
| **The Unequip Consequence** | Unequip and the shimmer returns immediately, on all three, along with the Charm penalty, the Blurts, and the step-back. The Herp was never cured. It was never going to be. The game never says so out loud after Věra's one refusal — it just turns the shimmer back on |
| **Aiguille's Regard** | Whichever bro carries it is greeted by name at the Haberdashery on every subsequent visit, regardless of which path obtained it. He respects the Coin. The greeting is for the Coin |

### What It Does NOT Do
- ❌ Cure `the_herp`. Nothing cures `the_herp`. Suppression is not a cure and the item file will not pretend otherwise
- ❌ Make any bro more attractive, more interesting, or younger than pushing forty
- ❌ Undo a single rejection that already happened, or erase a single ballad, screenshot, or bingo square
- ❌ Impress Monsieur Aiguille (his regard runs to the object, and only the object)
- ❌ Work while sitting in the inventory unequipped — it must be on a bro, and one bro is enough for all three

---

## 🎯 Gameplay Integration

### Permanent Hybrid Change
Once obtained, the Coin is **permanently party-bound**: it cannot be sold, dropped, traded, stolen, lost to any scripted event, or left behind on any city transition. What it *can* do — uniquely among quest items — is be equipped and unequipped from any bro's accessory slot at will, because the unequip is a designed player-facing choice, not an oversight: the game wants the player able to switch the shimmer back on and watch what it costs. Equipping on one bro covers all three; there is no reason to own three, and there is only one.

> **Template deviation (one-line justification):** the permanent-item template assumes a cosmetic welded to a sprite; the Coin is permanent at the *party inventory* level and toggleable at the *slot* level, and the toggle is the design's whole delayed-gratification payoff.

### Sprite Implementation
- **Visibility**: Worn on a lanyard outside the shirt on whichever bro has it equipped, always visible, in every outfit including formal wear
- **Layer**: Accessory overlay, chest layer (renders over the trivia champ badge if the same bro carries both — the badge is never removed, merely outranked)
- **Animation**: Swings on the lanyard with torso motion; catches a specular glint on any camera pan, one frame, every time
- **Degradation**: None. This is the only permanent item in the game with a single visual state and no degradation table branch — implement as a static asset

### Distinction From Equipment
| Attribute | The Gold Circle Coin | Standard Haberdashery Accessory |
|-----------|--------------|--------------------------|
| **Name** | The Gold Circle Coin | e.g. Pearl Cufflinks, Silk Pocket Square |
| **Type** | Quest Item (equippable, party-bound) | Equippable Accessory |
| **Slot** | Accessory (any one bro) | Accessory |
| **Stats** | +4 Bravado, +2 Composure, party-wide `the_herp` suppression | +1 to +2 single-stat, wearer only |
| **Removable** | Unequippable, never disposable | Yes, fully |
| **Source** | Aiguille's vitrine, *Objets d'Héritage* | Aiguille's shop floor, priced and stocked |

**Note**: A bro may wear the Coin alongside any Haberdashery accessory and the trivia champ badge simultaneously; no accessory in the game conflicts with it, because no accessory in the game is in its weight class.

---

## 🗣️ NPC Reactions

### When NPCs Notice The Coin
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| Monsieur Aiguille | *straightens fractionally, addresses the Coin rather than the man wearing it* "Ah. It travels well. Keep it out of direct sun." | "He's calling me a valued client. I'm basically staff here now." |
| Věra, Midnight Munchies General Store | *one glance at the lanyard, one nod, returns to the register* "Contained." | "She's impressed. That's a professional-to-professional nod." |
| Hamstradamus | "THE GOLD CIRCLE STAYED THE BURNING. THE PROPHECY HELD. REPENT ANYWAY." | "He's saying we're prophesied. We're PROPHESIED, bro." |
| Sinfonia opera-house patron | *reads the lanyard, reads it again, decides against a full sentence* "...Congratulations." | "Old money knows a collector when it sees one." |
| Haberdashery night porter (PATH B only) | *long look at the lanyard, longer look at the opera cape, says nothing at all, files nothing at all* | *don't hear* |

### Callback Dialogue Throughout Game
**Lord Pilsner** (holding court, Coin out of the sleeve, nobody permitted to touch it):
> "1990, boys. This thing is older than the guy pouring our drinks and it's aged BETTER. That's what quality does. That's what I do."

**Chadwick** (livestreaming to eleven viewers, nine of them bots):
> "Chat. CHAT. This is a legit cinema artifact. Museum-grade. And they let ME have it, because they SAW something. Smash the ICQ. #champion #europe #artifact"

**Bradley** (quietly, to Gregory, months in, while absently scratching):
> "Gregory says we should get a case for it. A real one. With a light. Gregory says you don't leave something like this just lying around where anything could happen to it."

---

## 🔗 Quest Integration

### Source Quest
- **Quest ID**: `debaucheryville_sidequest_nothing_is_getting_through_01`
- **Quest Name**: "Nothing Is Getting Through"
- **Quest Giver**: None — the questline self-triggers with the scripted outbreak (`night_event_outbreak_01`) at the Bohemian Riviera's `night_party_zone`; Věra refuses the cure at Midnight Munchies, and Hamstradamus's tent prophecy is the pointer that names the House of Needles
- **Location**: Haute Couture Haberdashery, Accessories Alcove (*Objets d'Héritage* vitrine), Imperial Square, Sinfonia

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| Post-cure re-attempts with all six ladies (each with her own callback line) | Coin equipped on any bro; re-approach any NPC who delivered a Herp-rejection scene |
| Full Couchsurfing Chronicles completion | Coin equipped — rejection auto-routing lifts party-wide, so every remaining Chronicles entry becomes achievable again |
| Haberdashery "by name" greeting and Aiguille's post-quest dialogue branch | Coin obtained via either path; greeting fires on every subsequent shop entry |
| Achievement "Nothing Is Getting Through" | Coin obtained (PATH A or PATH B) |

### Achievement
- **Achievement Name**: "Nothing Is Getting Through"
- **Description**: "Obtain the one and only Gold Circle Coin."
- **Hidden Description**: "Crossed a continent, spent a fortune, and learned nothing whatsoever."

---

## 🎬 Key Story Moments

### The Vitrine
*Accessories Alcove. Black velvet, single spot, glass. Three men who have been limping since Debaucheryville stop moving at the same time.*
> **Placard**: "Molded 1990. A piece of cinema history. **It is not for sale. It is for aspiration.**"

*Lord Pilsner, reading the placard aloud, arriving at exactly the wrong conclusion*
> "'For aspiration.' Bro. That's a CHALLENGE. That's them saying come back when you're somebody."

*Bradley, nose an inch from the glass*
> "Gregory has aspired to this his entire life."

### The Handover (PATH A)
*Monsieur Aiguille unlocks the vitrine with a key he keeps separate from the others. He handles the Coin with both hands. He is not performing.*
> "You understand what this is. No — you do not. But you will carry it, and it will be carried, and that is the arrangement."

*He seats it in a burgundy presentation sleeve before he will let go of it.*
> "Out of direct sun. Never in a trouser pocket. If I hear otherwise, I will know."

*Chadwick, already filming*
> "He's basically knighting me right now."

### The Exit (PATH B)
*Three men in full formal wear hold mannequin poses in opera capes while the night porter passes with a torch. Nobody blinks. One cape hem is trembling.*

*Outside, on the empty square, Lord Pilsner opens his hand.*
> "1990."

*Chadwick, whispering, for reasons nobody can articulate*
> "Don't say it out loud out here."

### Post-Credits: The Wall
*Months later. Back home. The Coin is framed in a shadow box on a living-room wall, mounted the way other men mount championship belts, angled under its own small light.*

*One bro, on the couch beneath it, absentmindedly scratching.*
> "Best summer of my life."

---

## 📱 Mobile Optimization

### Sprite Requirements
- **Base Size**: 8×8 pixels (Coin), 10×14 pixels (Coin on lanyard, chest overlay)
- **Memory**: Negligible — one static overlay asset, three character-body offsets, no degradation variants
- **Animation**: Rides the existing torso rig; one-frame specular glint on camera pan, no additional animation frames required
- **Degradation Variants**: 1 state × 3 characters (any bro can carry) = 3 sprite variants, plus 1 vitrine display asset and 1 shadow-box post-credits asset

### Performance Impact
- Net **negative** particle cost: equipping the Coin disables the party's `heat_shimmer` emitters, so the suppressed state is cheaper to render than the infected state
- No new particle system is introduced by this item
- No dynamic lighting required; the vitrine spot and the post-credits shadow-box light are baked into their scene assets

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item clearly defined | ✅ |
| Purchase/acquisition documented | ✅ (both paths) |
| Stats and effects specified | ✅ |
| Visual specifications complete | ✅ |
| NPC reactions documented | ✅ |
| Quest integration clear | ✅ |
| Distinction from equipment item (if applicable) | ✅ (vs. standard Haberdashery accessories) |
| Comedy value preserved | ✅ |
| Bros never achieve self-awareness | ✅ (they credit their immune systems for the missing rash, permanently) |

---

## 📝 Development Notes

- The Coin is the ONE item in Eurobound that fully delivers on its own legend. Do not add a twist, a catch, a durability counter, or a late-game reveal that it was a knockoff. The joke is that it is real and they still learn nothing
- Suppression is implemented as a party-wide flag driven by the equip slot, not a per-bro buff: one equipped Coin, three suppressed bros, no stacking, no partial states
- Unequip must restore the `heat_shimmer` emitter (asset `heat_shimmer.png`, Bohemian Riviera effects atlas — reused, not re-authored), the −2 Charm, the Groin Blurts, and the NPC step-back within one second, on all three bros at once. No fade, no grace period
- The foil seal is NEVER broken, in any branch, in any scene, in any post-credits variant. Sealed is canon
- Sell/drop/trade must be blocked at the UI layer with Aiguille's line returned as the refusal string, not a generic "you cannot do that"
- Verbatim, must ship exactly: the placard ("Molded 1990. A piece of cinema history. It is not for sale. It is for aspiration."), the Pretty Woman legend line quoted in this file's header, and Hamstradamus's prophecy where it appears in the quest doc
- Easter egg: a Sinfonia department-store window elsewhere in the city displays a modern multipack of the same brand, priced, stocked, at eye level, that the Coin-bearing bro walks past without ever registering
- Achievement "Nothing Is Getting Through" hidden description reveals only on unlock, per standard achievement UI behavior
