# Item Definition: Participant Wristband

*"SUBJECT 0417. ALLERGIES: NONE KNOWN. DO NOT RESUSCITATE WITHOUT CONSENT FORM." - the band itself, which is the only part of it that has been read closely*

**Rulings:** Eurobound Desk 4ti-q2 (author, 2026-11-13): "B: selfie + Participant Wristband" (the hospital-style band and its inspect line, as pitched). Eurobound Desk 4ti-q3 (author, 2026-11-13): "B (chosen for science), no effect, can't sell". The author's note on 4ti-q3: "B as we have another junk item that says 'I'm 7!' Or some such nonsense as a bracelet already" (the VIP All-Access Wristband, `design/items/vip_wristband_item.md`). Anything below marked **[PROPOSED]** is not ruled yet. Anything marked "Not ruled (author)" is waiting on the author.

## 📋 Item Identity
- **Item ID**: `item_participant_wristband` (engine key: `participant_wristband`)
- **Display Name**: Participant Wristband
- **Internal Name**: A hospital-style patient ID band with Dr. Vaněk's subject number on it
- **Item Type**: Junk item (permanent key item; no effect) **[RULED 4ti-q3]**
- **Rarity**: Not ruled (author). (The bros think they were chosen.)
- **Source**: Dr. Miloš Vaněk (`npc_dr_milos_vanek.md`), the reward for completing Vaněk's Survey, The Absinthium Taproom, Debaucheryville **[RULED 4ti-q2]**

---

## 🎭 The Deception

### What The Item Actually Is
A hospital-style patient band **[RULED 4ti-q2]**. The printed label reads, in full: `SUBJECT 0417. ALLERGIES: NONE KNOWN. DO NOT RESUSCITATE WITHOUT CONSENT FORM.` **[RULED 4ti-q2]** The bros get it for finishing a six-question survey that a man behind a bar wrote, whose ethics board is himself ("The ethics board is me", his canon survey line). It does nothing **[RULED 4ti-q3]**. **[PROPOSED]** The subject number is not a rank. It is just the next number on the roll.

### What The Bros Believe It Is
They believe they were chosen for science **[RULED 4ti-q3, option B]**. **[PROPOSED]** in their voice:

"Bro. A *doctor* picked us. Out of everybody in that bar. You don't get a subject number unless you're a subject, and you don't get to be a subject unless science looks at you and goes, 'that one.' Four-one-seven. That's, like, top five hundred."

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | N/A (survey reward, not sold) **[RULED 4ti-q2]** |
| **Actual Value** | Not ruled (author). It has no sale value because it cannot be sold. |
| **Resale Value** | 0 SOVS (cannot be sold) **[RULED 4ti-q3]** |
| **Can Be Sold** | No **[RULED 4ti-q3: "can't sell"]** |
| **Can Be Dropped** | No (permanent key item, like the other Arcade junk prizes) |
| **Can Be Traded** | Not ruled (author) |

---

## 🎨 Visual Specifications

### Physical Appearance
| Attribute | Description |
|-----------|-------------|
| **Material** | Hospital-style patient band **[RULED 4ti-q2]**; exact material not ruled (author) |
| **Size** | Not ruled (author) |
| **Closure** | Not ruled (author) |
| **Text/Markings** | `SUBJECT 0417. ALLERGIES: NONE KNOWN. DO NOT RESUSCITATE WITHOUT CONSENT FORM.` **[RULED 4ti-q2]** |
| **Color** | Not ruled (author) |

### Degradation Over Time
| Days Worn | Visual State |
|-----------|--------------|
| Days 1-3 | Not ruled (author). Whether the band is worn on a sprite at all is open (see Sprite Implementation). |
| Days 4-7 | Not ruled (author) |
| Days 8+ | Not ruled (author) |

---

## 📊 Stats & Effects

### Direct Stats
```
None:              0  (author, 4ti-q3: "no effect")
```

### Passive Effects
| Effect | Description |
|--------|--------------|
| **None** | No effect **[RULED 4ti-q3]**. Inspecting it shows the label text. |

### What It Does NOT Do
- ❌ It does not mark the bros as anything to anyone. No NPC, door, discount or check reads it.
- ❌ It does not unlock further research, a second survey, or anything else at the Taproom.
- ❌ It does not sell, at any price, anywhere.

---

## 🎯 Gameplay Integration

### Permanent Inventory Item
Once acquired, the Participant Wristband sits in the key-item inventory for the rest of the game and cannot be sold or dropped, like the other Arcade junk prizes (`key_items.json` `aa_junk_*`). Whether it is also visibly worn on a bro's sprite, and on which bro, is **not ruled (author)**. Until it is ruled, it is inventory only.

### Sprite Implementation
- **Visibility**: Not ruled (author). Inventory only until ruled.
- **Layer**: Not ruled (author)
- **Animation**: Not ruled (author)
- **Degradation**: Not ruled (author)

### Distinction From Equipment
| Attribute | Participant Wristband | VIP All-Access Wristband |
|-----------|--------------|--------------------------|
| **Name** | Participant Wristband | VIP All-Access Wristband (`item_vip_wristband_im_seven`) |
| **Type** | Junk item (permanent key item) | Permanent Cosmetic |
| **Slot** | None (inventory) | None (always visible on all three bros) |
| **Stats** | None | See its doc |
| **Removable** | Never (cannot be sold or dropped) | Never |
| **Source** | Dr. Vaněk, Vaněk's Survey, The Absinthium Taproom | Shady Wristband Guy, Astronomical Cock-Up Square |

**Note**: The two do not interact. The author picked the "chosen for science" belief for this band because the VIP wristband already covers the "it's a VIP band" joke (4ti-q3 note).

---

## 🗣️ NPC Reactions

### When NPCs Notice The Item
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| Not ruled (author) | Not ruled (author) | Not ruled (author) |

No NPC reacts to the band until the author rules reactions in. It has no effect (4ti-q3), so no reaction is required for it to work.

### Callback Dialogue Throughout Game
Not ruled (author). None is written.

---

## 🔗 Quest Integration

### Source Quest
- **Quest ID**: none (Vaněk's Survey is an optional Taproom activity, not a side quest doc)
- **Quest Name**: "Vaněk's Survey"
- **Quest Giver**: Dr. Miloš Vaněk
- **Location**: The Absinthium Taproom, Debaucheryville (`design/worlds/debaucheryville/the_absinthium_taproom.md`, section "Vaněk's Survey")

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| Nothing | The band has no effect (4ti-q3) |

Granted at the end of Vaněk's Survey, together with the "The Research Subject" selfie (4ti-q2). The code already records consent as `vanek_survey_consented` (`game/core/vanek_taproom.gd`); the grant is wired by the Absinthe Orchestrator. No flag is written on acquire.

### Achievement
- **Achievement Name**: Not ruled (author)
- **Description**: Not ruled (author)
- **Hidden Description**: Not ruled (author)

---

## 🎬 Key Story Moments

### The Survey Ends
*Vaněk's closer (approved, 4ti-q1):*
> "Thank you. Your data will be used for science, or for my memoirs. The distinction is philosophical."

*He hands over the band. The selfie "The Research Subject" is taken (4ti-q2).*

### Inspect
> "SUBJECT 0417. ALLERGIES: NONE KNOWN. DO NOT RESUSCITATE WITHOUT CONSENT FORM."

---

## 🖥️ Performance & Assets

### Sprite Requirements
- **Base Size**: Inventory icon only, at the key-item icon size. A worn sprite is not ruled (author).
- **Memory**: Negligible (one icon)
- **Animation**: None
- **Degradation Variants**: None until a worn sprite is ruled

### Performance Impact
- One inventory icon; no draw-call impact in the world
- No particle effects
- No lighting requirements

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item clearly defined | ☑ |
| Purchase/acquisition documented | ☑ |
| Stats and effects specified | ☑ (none, ruled) |
| Visual specifications complete | ☐ (only the label is ruled) |
| NPC reactions documented | ☐ (not ruled) |
| Quest integration clear | ☑ |
| Distinction from equipment item (if applicable) | ☑ |
| Comedy value preserved | ☑ |
| Bros never achieve self-awareness | ☑ |

---

## 📝 Development Notes

- The inspect text is the approved label, verbatim. Don't paraphrase it.
- Open for the author: whether it's worn on a sprite (and which bro), its material, colour and look, its rarity and actual value, NPC reactions, callbacks, and any achievement.
- Inventory icon: the band with its label legible is enough. Per the generated-text rule, check every word on any generated art (`SUBJECT 0417`, `DO NOT RESUSCITATE`).
- Survey text and reward: `design/worlds/debaucheryville/the_absinthium_taproom.md`, "Vaněk's Survey".
