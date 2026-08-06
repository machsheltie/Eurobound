# Item Definition: Trinity Student ID

*"We're not tourists anymore, gentlemen. We're EXCHANGE STUDENTS." - Lord Pilsner, holding a laminated card that is still warm from the laminator*

> ⚠ AUTHOR-REVIEW: entire item drafted by Claude under the author's draft-for-review ruling
> (2026-08-05 Student ID interview). Author-fixed facts: one doc / per-bro variants; permanent
> running-gag item; 10-Sovs tuition acquisition per trinity_of_pints.md L141-145. Everything
> else below is draft pending author approval.

## 📋 Item Identity
- **Item ID**: `item_student_id`
- **Display Name**: Trinity Student ID
- **Internal Name**: Laminated pub cover-charge card with a name typed on it
- **Item Type**: Permanent Cosmetic (flashed, not worn)
- **Rarity**: Common (bros think it's Accredited)
- **Source**: Enrollment desk ("Registrar"), Trinity of Pints, Publandia

---

## 🎭 The Deception

### What The Item Actually Is
A cover-charge receipt. Ten Sovs buys an evening of "courses" at a pub that cosplays as a
university, and the receipt comes shaped like a student ID: bar-top inkjet card stock, a name
field typed by a bartender who did not ask for spelling, a photo taken on a webcam zip-tied to
the enrollment desk, and a lamination pouch applied while still hot. It is honored as
identification exactly nowhere, including at Trinity of Pints, where the only admission
requirement is the ten Sovs.

### What The Bros Believe It Is
"Official proof of enrollment at Europe's most exclusive drinking academy. This is
INTERNATIONAL STUDENT STATUS, boys. Museums, trains, cover charges — student pricing,
continent-wide. You know what this card says to the world? It says we BELONG in academia."

---

## 💰 Economic Details

| Attribute | Value |
|-----------|-------|
| **Purchase Price** | 10 Sovs each (30 Sovs for all 3 bros — "tuition") |
| **Actual Value** | 0.5 Sovs (the lamination pouch) |
| **Resale Value** | 0 Sovs (worthless) |
| **Can Be Sold** | No — no vendor on the continent will make eye contact with it |
| **Can Be Dropped** | No (permanent cosmetic) |
| **Can Be Traded** | No — the name is laminated on, and so is the shame |

---

## 🎨 Visual Specifications

### Physical Appearance
| Attribute | Description |
|-----------|-------------|
| **Material** | Inkjet card stock in a heat-sealed lamination pouch |
| **Size** | Standard wallet card; slightly trapezoidal (cut freehand) |
| **Fastening** | None — carried in wallet, produced with a two-finger flourish |
| **Text/Markings** | TRINITY OF PINTS crest (a shamrock reading a book), name field, photo, "MAJOR", "AGE", and "VALID: FOREVER*" (*the asterisk resolves to nothing) |
| **Finish** | High-gloss lamination, one air bubble each, non-negotiable |

### Per-Character Variants
> ⚠ AUTHOR-REVIEW: all three variant rows drafted.

| Character | Card Details | Photo |
|-----------|--------------------|----------------------|
| Lord Pilsner | Name: "LORD PILSNER" (he typed it himself; caps lock was a choice). Major: International Business (Self-Designed). Age: 22 | Chin raised, eyes fixed past the camera like a yearbook photo he expects to be asked to sign |
| Chadwick | Name: "CHAD WICK" (bartender heard two words, typed two words). Major: Communications. Age: 22 | Mouth open mid-sentence — he was saying "we should get matching ones" |
| Bradley | Name: "BRADLEY" (last-name field laminated over a thumbprint of cocktail sauce). Major: Undeclared. Age: 22 | Mid-blink, mid-chew, somehow both |

### Degradation Over Time
| Days Worn | Visual State |
|-----------|--------------|
| Days 1-3 | Pristine gloss; the bros angle them at strangers so the light catches |
| Days 4-7 | Corners peeling; Bradley's has a bite mark he will not explain |
| Days 8+ | Inkjet ink migrating inside the pouch — the photos are becoming ghosts, and the ghosts are still being presented to bouncers with total confidence |

---

## 📊 Stats & Effects

### Direct Stats
> ⚠ AUTHOR-REVIEW: stat numbers drafted — author rules per house economy law.

```
Bravado:        +1 (laminated proof of belonging)
Intelligence:   -1 (they believe the card is real, and belief has a cost)
```

### Passive Effects
| Effect | Description |
|--------|--------------|
| **"Student Discount?"** | Unlocks a dialogue option with any vendor: demand student pricing. It has never once worked. The bros track their attempts as "pending applications." |
| **Course Access** | Grants evening access to Trinity of Pints' four-course curriculum (the card's one true function, which the bros consider its least interesting feature) |
| **Registrar Recognition** | Trinity staff greet cardholders by whatever the card says — Chad Wick is Chad Wick forever now |

### What It Does NOT Do
- ❌ Get a student discount anywhere, from anyone, ever
- ❌ Constitute enrollment at any institution on any continent
- ❌ Make anyone 22

---

## 🎯 Gameplay Integration

### Permanent Cosmetic Change
Once acquired, the card lives in each bro's wallet for the rest of the game and cannot be
removed, sold, or surrendered — even to bouncers who ask to "keep this for a second." It
surfaces automatically in dialogue: any interaction where price is mentioned rolls the chance
that a bro produces it unprompted.

### Sprite Implementation
- **Visibility**: Flash animation during dialogue interactions (card raised, light glint, hold for one beat too long)
- **Layer**: UI/dialogue overlay, above portrait
- **Animation**: 3-frame flourish per bro; glint frame reuses the NFT shimmer
- **Degradation**: Card sprite swaps at day 4 and day 8 states; the flash animation never changes, because their confidence doesn't

---

## 🗣️ NPC Reactions

> ⚠ AUTHOR-REVIEW: reaction rows and bro interpretations drafted.

### When NPCs Notice The Item
| NPC Type | Reaction | Bros' Interpretation |
|----------|----------|------------------------|
| Trinity staff | "Ah, a scholar. The bar is that way, professor." | "Faculty respect. They can TELL we're serious academics." |
| Publandia barkeep | Doesn't look up: "That's a beer mat with a face on it." | "Jealous. Publicly educated." |
| Sinfonia box office | Holds it to the light. Turns it over. Reads the back, which is blank. "This is a pub receipt." | "She checked the WATERMARK, boys. That's how official this is." |
| Debaucheryville bouncer | Scans it with the UV wand. The wand finds nothing, because there is nothing. | *doesn't hear the sigh* |
| Hostel clerk | "Student rate requires a student. From a school." | "Semantics. The Euromemeian system is different." |

### Callback Dialogue Throughout Game
**Lord Pilsner** (any museum, any city):
> "Three student admissions. We're with the university. You may have heard of it — Trinity? Of Pints? Feel free to verify. Take your time. We'll wait."

**Chadwick** (checking his card in idle moments):
> "It says Chad Wick. Two words. Honestly? Cleaner branding. I'm keeping it."

**Bradley** (whenever a discount attempt fails):
> "Denied AGAIN. Whatever man, the credit transfers. It transfers."

---

## 🔗 Quest Integration

### Source Quest
- **Quest ID**: `publandia_sidequest_brewery_tour_trinity_01`
- **Quest Name**: "Brewery Tour — Trinity of Pints"
- **Quest Giver**: The Registrar (enrollment desk), Trinity of Pints
- **Location**: Trinity of Pints, Publandia

### Gates/Unlocks
| What It Unlocks | How |
|------------------|-----|
| The four-course curriculum (Pub 115 / Song 220 / Greek 330 / Thesis Defense 401) | Evening course access is tuition-gated; the card is the tuition receipt |
| "Student Discount?" dialogue option | Automatic once any bro holds a card |
| Registrar wrong-name greetings | Automatic; permanent; Chad Wick |

### Achievement
> ⚠ AUTHOR-REVIEW: achievement drafted.
- **Achievement Name**: "Non-Traditional Students"
- **Description**: "Enroll all three bros at Trinity of Pints."
- **Hidden Description**: "Three men with a combined age of 115 wrote '22' on three forms within sight of each other and nobody blinked."

---

## 🎬 Key Story Moments

> ⚠ AUTHOR-REVIEW: all three beats drafted.

### The Enrollment
*The Registrar slides three blank forms across the desk. All three bros, independently and without conferring, write "22" in the age field.*
> **Registrar**: "Three for tuition. Smile for the webcam. Or don't. It captures at two frames a second either way."

*The laminator hums. Lord Pilsner receives his card the way other men receive knighthoods.*
> **Lord Pilsner**: "Gentlemen. As of this moment, we are ENROLLED. Do you understand what this means?"
> **Bradley**: "Free pint glass."
> **Lord Pilsner**: "It means free pint glass, yes. But ALSO—"

### The First Discount Attempt
*Sinfonia box office. The clerk has been holding Chadwick's card for eleven seconds.*
> **Chadwick**: "Take your time. It's real."
> **Clerk**: "It says your major is Communications."
> **Chadwick**: "Minor in Marketing. It's not on the card. The card was full."

### The Ghost Cards (late game)
*Shamsterdam. The photos have fully migrated into fog inside the lamination. Bradley presents his anyway.*
> **Bradley**: "That's me. The smudge. I've matured since then."

---

## 🖥️ Performance & Assets

### Sprite Requirements
- **Base Size**: 32x20 pixels per card (dialogue overlay at 2x)
- **Memory**: Negligible
- **Animation**: 3-frame flash flourish per bro; no idle animation
- **Degradation Variants**: 3 states × 3 characters = 9 card sprites

### Performance Impact
- Zero draw-call impact outside dialogue overlays
- No particle effects (the glint is a palette swap frame)
- No lighting requirements

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Item clearly defined | ☑ |
| Purchase/acquisition documented | ☑ |
| Stats and effects specified | ☑ (⚠ numbers pending author) |
| Visual specifications complete | ☑ |
| NPC reactions documented | ☑ (⚠ drafted) |
| Quest integration clear | ☑ |
| Distinction from equipment item (if applicable) | ─ (n/a — no equippable counterpart) |
| Comedy value preserved | ☑ |
| Bros never achieve self-awareness | ☑ |

---

## 📝 Development Notes

- The card is flashed, never worn — visibility is dialogue-overlay only, no overworld sprite layer
- Name fields must stay legible at 2x dialogue scale (CHAD WICK is two words on two lines)
- Bros never acknowledge degradation states; NPCs may
- Easter egg candidate (⚠ AUTHOR-REVIEW): the Registrar's webcam photo files are named `enrollee_4051.png` onward — Trinity has enrolled over four thousand "students" and the bros' cards are three of them
- Depends on: Trinity of Pints enrollment desk scene (brewerytourpublandia.md); Registrar NPC is the enrollment-desk staffer — if the author wants them to be a named character, that's a separate NPC profile and ruling
- Cross-reference: age field "22" echoes the continent-wide everyone-is-22 delusion (Velvet Curtain Club's bouncer canon)
