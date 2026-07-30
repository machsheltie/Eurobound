# Item Definition: [Item Name]

*"[Satirical tagline or quote capturing the delusion]" - [Optional framing, e.g. what the bros call it]*

<!--
HOW TO USE THIS TEMPLATE
This template is for PERMANENT ITEMS: items that become permanently affixed to a bro
once acquired (cosmetic-permanent, hybrid cosmetic+mechanical, or curse items). They
are never equipped/unequipped through a normal item slot - once on, they're on for
the rest of the game (see vip_wristband_item.md for the exemplar this was generalized
from). If the item CAN be removed/swapped through an equipment slot, use an equipment
item template instead, not this one.

Replace every [bracketed placeholder] with real content. Delete this comment block
before publishing the finished item doc. Keep all H2 section headers (with emoji) and
table column shapes exactly as they appear here - Task 2 depends on this skeleton
matching exactly.
-->

## 📋 Item Identity
- **Item ID**: `item_[item_name_snake_case]`
- **Display Name**: [Item Name]
- **Internal Name**: [What the item actually is, in plain terms]
- **Item Type**: [Permanent Cosmetic / Hybrid / Curse Item / Quest Item]
- **Rarity**: [Actual rarity] (bros think it's [Rarity bros believe])
- **Source**: [NPC or event that provides this item], [Location]

---

## 🎭 The Deception

### What The Item Actually Is
[The mundane, cheap, or embarrassing reality of the item - what it is, where it came from, what it's actually worth or does. Ground this in specific, verifiable detail.]

### What The Bros Believe It Is
"[The bros' delusional interpretation, in their own voice - what they think this grants them, why they think it's special.]"

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | [€X each / €X for all 3 bros] |
| **Actual Value** | [€X] |
| **Resale Value** | [€X or "€0 (worthless)"] |
| **Can Be Sold** | [Yes/No + why] |
| **Can Be Dropped** | [Yes/No + why, e.g. "No (permanent cosmetic)"] |
| **Can Be Traded** | [Yes/No + why] |

---

## 🎨 Visual Specifications

### Physical Appearance
| Attribute | Description |
|-----------|-------------|
| **Material** | [What it's made of] |
| **[Size/Dimension attribute]** | [Value] |
| **[Closure/Fastening attribute]** | [Value] |
| **Text/Markings** | [Any text, symbols, or markings] |
| **[Color/Finish attribute]** | [Value] |

### [Per-Character Variants — include only if the item differs by bro; otherwise omit this subsection]
| Character | [Variant Attribute] | [Hex Code / Detail] |
|-----------|---------------------|----------------------|
| Lord Pilsner | [Variant] | [Detail] |
| Chadwick | [Variant] | [Detail] |
| Bradley | [Variant] | [Detail] |

### Degradation Over Time
| Days Worn | Visual State |
|-----------|--------------|
| Days 1-3 | [Pristine state description] |
| Days 4-7 | [Worn state description] |
| Days 8+ | [Crusty/degraded state description] |

---

## 📊 Stats & Effects

### Direct Stats
```
[Stat Name]:       [+/-X] ([reason])
[Stat Name]:       [+/-X] ([reason])
[Stat Name]:       [+/-X] ([reason])
```

### Passive Effects
| Effect | Description |
|--------|--------------|
| **[Effect Name]** | [What it does to bro behavior/dialogue/perception] |
| **[Effect Name]** | [What it does] |
| **[Effect Name]** | [What it does] |

### What It Does NOT Do
- ❌ [Thing bros believe it does but doesn't]
- ❌ [Thing bros believe it does but doesn't]
- ❌ [Thing bros believe it does but doesn't]

---

## 🎯 Gameplay Integration

### Permanent [Cosmetic/Hybrid] Change
Once acquired, [description of the permanent visibility rule - what becomes permanently visible/active on the bro(s), and confirmation it cannot be removed, hidden, or replaced].

### Sprite Implementation
- **Visibility**: [Where/how it's always visible]
- **Layer**: [Sprite layer it occupies]
- **Animation**: [How it behaves during character animation]
- **Degradation**: [How visual state updates based on in-game time/days elapsed]

### [Distinction From Equipment — include only if a similarly-named equippable item exists; otherwise omit this subsection]
| Attribute | [This Item] | [Equipment Counterpart] |
|-----------|--------------|--------------------------|
| **Name** | [Item Name] | [Equipment Name] |
| **Type** | Permanent Cosmetic | Equippable Accessory |
| **Slot** | None (always visible) | [Slot name] |
| **Stats** | [Cosmetic only / stats] | [+X Stat, +X Stat] |
| **Removable** | Never | Yes |
| **Source** | [This item's source] | [Equipment's source] |

**Note**: [Any interaction note, e.g. whether bros can have both simultaneously.]

---

## 🗣️ NPC Reactions

### When NPCs Notice The Item
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| [NPC Type] | "[What they say]" | "[How bros twist it]" |
| [NPC Type] | "[What they say]" | "[How bros twist it]" |
| [NPC Type] | "[What they say]" | "[How bros twist it]" |
| [NPC Type] | "[What they say]" | *[reaction, e.g. don't hear]* |
| [NPC Type] | *[non-verbal reaction]* | "[How bros twist it]" |

### Callback Dialogue Throughout Game
**Lord Pilsner** ([context]):
> "[Line]"

**Chadwick** ([context]):
> "[Line]"

**Bradley** ([context]):
> "[Line]"

---

## 🔗 Quest Integration

### Source Quest
- **Quest ID**: `[city]_sidequest_[quest_name]_01`
- **Quest Name**: "[Quest Name]"
- **Quest Giver**: [NPC Name]
- **Location**: [Location]

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| [Unlock] | [Trigger condition] |
| [Unlock] | [Trigger condition] |
| [Unlock] | [Trigger condition] |

### Achievement
- **Achievement Name**: "[Achievement Name]"
- **Description**: "[Public-facing description]"
- **Hidden Description**: "[The humiliating truth, revealed on unlock]"

---

## 🎬 Key Story Moments

### [Beat 1 Name, e.g. "The Purchase/Acquisition"]
*[Stage direction]*
> "[Dialogue]"

*[Stage direction]*
> "[Dialogue]"

### [Beat 2 Name, e.g. "The Revelation"]
*[Stage direction]*
> "[Dialogue]"

*[Stage direction]*
> "[Dialogue]"

### [Beat 3 Name, e.g. "Post-Credits/Callback" — optional third beat]
*[Stage direction]*
> "[Dialogue]"

---

## 📱 Mobile Optimization

### Sprite Requirements
- **Base Size**: [Dimensions] pixels per [item]
- **Memory**: [Impact level]
- **Animation**: [Sync requirements, additional frames needed or not]
- **Degradation Variants**: [X states × X characters = X sprite variants]

### Performance Impact
- [Draw call impact]
- [Particle effects note]
- [Lighting requirements note]

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item clearly defined | ☐ |
| Purchase/acquisition documented | ☐ |
| Stats and effects specified | ☐ |
| Visual specifications complete | ☐ |
| NPC reactions documented | ☐ |
| Quest integration clear | ☐ |
| Distinction from equipment item (if applicable) | ☐ |
| Comedy value preserved | ☐ |
| Bros never achieve self-awareness | ☐ |

---

## 📝 Development Notes

- [Sprite/visibility requirement]
- [Legibility or asset detail requirement]
- [Degradation/behavior rule - e.g. bros never acknowledge condition changes]
- [Easter egg idea]
- [Any special scene/asset dependency]
- [Achievement or hidden-content note]
