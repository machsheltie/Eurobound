# The Confidence Man - Complete PNG Asset Requirements

## 📋 Overview
A mobile street cart selling bottled confidence, run by a former actor whose products work partly through herbs, mostly through belief, and entirely through a magnificent mustache. This document specifies every sprite needed for a vendor who puts "con" right in his name and dares you to buy anyway — carnival theatre parked outside a Publandia pub, selling the placebo effect at 15 Sovs a bottle.

**Location ID:** `publandia_vendor_confidence_man_01`
**Theme:** Self-improvement snake oil, confidence as performance, the placebo effect with a price board
**Zone:** Cobblestone Market Street (mobile cart — prime spots near pub entrances)
**Hours:** 14:00-00:00 (prime confidence-needing hours)
**Primary Function:** Street vendor / Bravado buff shop / haggling minigame / pre-challenge preparation stop

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Carnival Red | #DC143C | Cart trim, banners, pitch energy |
| Apothecary Gold | #FFD700 | Gold-tier labels, brass fittings, lantern glow |
| Wood Brown | #8B4513 | Cart body, work station |
| Tonic Blue | #4169E1 | Silver-tier labels, "Steady Nerves" bottles |
| Reserve Black | #1A1A1A | Special Reserve labels, hidden compartment |
| Placebo Shimmer | #E6E6FA | Potion glow, transformation sparkle |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/confidence_man/
├── environment/
│   ├── confidence_cart.png
│   └── market_context.png (packed into confidence_cart.png)
├── npcs/
│   ├── cormac.png
│   └── crowd_customers.png
├── objects/
│   └── tonic_bottles.png
├── effects/
│   └── confidence_effects.png
└── ui/
    └── confidence_ui.png
```

---

## 🎪 Sprite Sheet 1: The Travelling Apothecary Cart
**File:** `confidence_cart.png`
**Dimensions:** 512x384 pixels

### Cart Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cart Body | (0, 0) | 256x192 | Wooden cart, brass fittings, theatrical paint job |
| Cart Wheels | (0, 192) | 128x64 | Spoked wheels, one slightly wobbly |
| Display Front | (128, 192) | 128x96 | Bottles arranged by "potency," tier-shelved |
| Work Station | (0, 256) | 128x96 | Mixing bench, mysterious ingredients (mostly herbs, some alcohol) |
| Secret Recipe Box | (128, 288) | 64x64 | Theatrical prop, ornate and meaningless |
| Hidden Compartment Closed | (192, 288) | 64x64 | Innocent cart panel |
| Hidden Compartment Open | (0, 352) | 64x32 | The REAL stock — Special Reserve shelf revealed |

### Signage & Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Sign | (256, 0) | 192x48 | "THE CONFIDENCE MAN" in bold carnival lettering |
| Banner | (256, 48) | 192x32 | "BRAVADO TONICS • COURAGE ELIXIRS • GUARANTEED BOLDNESS" |
| Side Sign | (256, 80) | 128x48 | "Nervous? Shy? Lacking CONVICTION? I Can HELP!" |
| Small Print Plaque | (384, 80) | 64x48 | "Entertainment purposes. Individual results vary. No refunds." |
| Price Board | (256, 128) | 96x128 | Chalk prices, "negotiable, allegedly" |
| Testimonial Cards | (352, 128) | 64x64 | "Definitely real customers" |
| Cart Lantern Lit | (416, 128) | 48x64 | Warm gold pitch-light |
| Cart Lantern Off | (464, 128) | 48x64 | Packed-up state |
| Demonstration Table | (256, 256) | 128x64 | Watered-down sample cups |
| Pub-Adjacent Cobbles | (384, 256) | 128x64 | Ground tile — cart repositions near pub entrances |
| Cart Packed (Travel Mode) | (256, 320) | 192x64 | Folded cart for relocation between visits |

### Technical Notes:
- Cart spawns at one of three market anchor points per visit — same sprite, new position, sells the "mobile" gag
- Hidden Compartment Open only renders after Special Reserve is asked about or Valued Customer status reached

---

## 🎩 Sprite Sheet 2: Cormac "The Confidence Man" Byrne
**File:** `cormac.png`
**Dimensions:** 384x384 pixels

### Cormac States (96x128 each):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| The Pitch | (0, 0) | 96x128 | Arms wide, full carnival barker projection |
| The Point | (96, 0) | 96x128 | "You! Yes, YOU!" — finger extended at player |
| Mixing | (192, 0) | 96x128 | Theatrical custom-blend performance at work station |
| Presenting Bottle | (288, 0) | 96x128 | Tonic held aloft, catching lantern light |
| The Close | (0, 128) | 96x128 | Leaning in, deal-sealing intimacy |
| Haggle React | (96, 128) | 96x128 | Clutched chest, "Do I look like a charity?" |
| Honest Mode | (192, 128) | 96x128 | Dropped act, elbow on cart — Valued Customers only |
| Calling Back | (288, 128) | 96x128 | Waving after a walking-away player: "Wait, WAIT!" |

### Cormac Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Mustache | (0, 256) | 48x24 | Magnificent. Non-negotiable. Its own layer for micro-animation |
| Theatrical Coat | (48, 256) | 64x64 | Actor's wardrobe, patched with pride |
| Pouring Hands | (112, 256) | 64x32 | Mid-pour, showman's flourish |
| Coin Flourish | (176, 256) | 32x32 | Payment accepted with sleight-of-hand |

### Cormac Expressions (48x48 each):
| Expression | Position | Size | Description |
|------------|----------|------|-------------|
| Salesman Gleam | (0, 288) | 48x48 | Default — eyes that have read your Bravado |
| Mock Offense | (48, 288) | 48x48 | Failed haggle response |
| Conspiratorial | (96, 288) | 48x48 | Special Reserve territory |
| Genuine Respect | (144, 288) | 48x48 | "Beyond the Potion" earned without a tonic |
| Honest Tired | (192, 288) | 48x48 | Twelve years of belief retail, act down |

### Dialogue Portraits (64x48 each):
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Portrait Pitch | (0, 336) | 64x48 | Full theatre |
| Portrait Close | (64, 336) | 64x48 | The sell |
| Portrait Honest | (128, 336) | 64x48 | "Between us? Mostly it's you deciding to be brave." |
| Portrait Respect | (192, 336) | 64x48 | The rare real smile |

---

## 👥 Sprite Sheet 3: Crowd & Customers
**File:** `crowd_customers.png`
**Dimensions:** 384x192 pixels

### Customer NPCs (64x96 each):
| NPC | Position | Size | Description |
|-----|----------|------|-------------|
| The Repeat Buyer | (0, 0) | 64x96 | Weekly supply in arms, evangelical |
| The Skeptic | (64, 0) | 64x96 | Arms crossed: "You can't BOTTLE confidence." |
| The First-Timer | (128, 0) | 64x96 | Nervous, hopeful, date tonight |
| The Crasher | (192, 0) | 64x96 | Deflated post-Transformation, hiding behind own shoulders |

### Crowd Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Crowd Clump A | (256, 0) | 128x96 | Three gathered onlookers, mid-demonstration |
| Crowd Clump B | (0, 96) | 128x96 | Two leaning-in listeners |
| Reaction Overlay: Impressed | (128, 96) | 64x48 | Raised eyebrows layer for crowd clumps |
| Reaction Overlay: Doubtful | (128, 144) | 64x48 | Side-eye layer |
| First-Timer Drinking | (192, 96) | 64x96 | The plunge, mid-swig |
| Crasher Portrait | (256, 96) | 64x48 | "I was a GOD for an hour." |
| Skeptic Portrait | (256, 144) | 64x48 | Unconvinced in close-up |
| Sample Cup Held | (320, 96) | 32x32 | Watered-down demo prop |
| Nervous Fidget Hands | (320, 128) | 32x32 | First-timer detail overlay |

---

## 🧪 Sprite Sheet 4: Tonic Bottles
**File:** `tonic_bottles.png`
**Dimensions:** 256x192 pixels

### Bronze Tier (24x48 each, brown labels, y=0):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| "Mild Courage" Tonic | (0, 0) | 24x48 | Starter courage, 5 Sovs |
| "Steady Nerves" Drops | (24, 0) | 24x48 | Dropper bottle, calming blue liquid |
| "Social Ease" Elixir | (48, 0) | 24x48 | Round flask, chatty fizz |
| "Basic Boldness" Shot | (72, 0) | 24x48 | Stubby shot bottle |

### Silver Tier (24x48 each, blue labels, y=0 cont.):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| "Liquid Boldness" | (96, 0) | 24x48 | The signature product — hero bottle |
| "Charm Amplifier" | (120, 0) | 24x48 | Heart-stoppered |
| "Fear Suppressant" | (144, 0) | 24x48 | Square, clinical-adjacent |
| "Voice of Authority" | (168, 0) | 24x48 | Megaphone-shaped neck |

### Gold Tier (24x48 each, gold labels, y=48):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| "Absolute Confidence" | (0, 48) | 24x48 | Gold wax seal |
| "Irresistible Presence" | (24, 48) | 24x48 | Perfume-bottle silhouette |
| "Fearless Fighter" | (48, 48) | 24x48 | Fist-embossed glass |
| "The Closer" | (72, 48) | 24x48 | Contract-scroll label |

### Special Reserve (24x48 each, black labels, y=48 cont.):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| "Cormac's Personal Blend" | (96, 48) | 24x48 | Hand-written label, the real stuff |
| "Emergency Confidence" | (120, 48) | 24x48 | Break-glass styling |
| "The Transformation" | (144, 48) | 24x48 | Warning band: crash after |
| "Liquid Legend" | (168, 48) | 24x48 | 50 Sovs, faintly glowing |

### Tier Sets & Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bronze Shelf Set | (0, 96) | 72x48 | Three-bottle display grouping |
| Silver Shelf Set | (72, 96) | 72x48 | Display grouping |
| Gold Shelf Set | (144, 96) | 72x48 | Display grouping, lantern-lit |
| Empty Bottle | (216, 96) | 24x48 | Post-consumption prop |
| Cork Set | (0, 144) | 48x24 | Assorted stoppers |
| Ingredient Jars | (48, 144) | 96x48 | Rhodiola, ginseng, "adaptogens" — they have STUDIES |
| Label Sheet | (144, 144) | 64x48 | Definitely-not-relabeling supplies |

### Technical Notes:
- Tier is double-coded: label color AND cap shape (round/square/crown/skull) for colorblind safety
- Hero "Liquid Boldness" bottle gets a 2px Placebo Shimmer outline in shop UI

---

## ✨ Sprite Sheet 5: Confidence Effects
**File:** `confidence_effects.png`
**Dimensions:** 256x128 pixels

### Potion & Buff Effects:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Potion Shimmer Frame 1-3 | (0, 0) | 72x24 | Three 24x24 sparkle frames on bottles |
| Buff Activation Burst | (72, 0) | 48x48 | Radial confidence glow on drink |
| Transformation Aura | (120, 0) | 48x64 | Full-body golden outline (premium tonics) |
| Crash Deflation Frame 1-3 | (168, 0) | 72x24 | Three 24x24 drooping gray wisps |
| Placebo Glint | (168, 24) | 24x24 | Subtle — appears only when belief bonus active |

### Cart Atmosphere:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Theatrical Smoke Puff 1-3 | (0, 48) | 96x32 | Three 32x32 small puffs for the mixing performance |
| Lantern Glow | (96, 48) | 48x48 | Warm radial pool |
| Crowd Energy Lines | (144, 48) | 64x32 | Excitement radiating during pitch |
| Coin Sparkle | (208, 48) | 24x24 | Transaction flourish |
| Pitch Spotlight | (0, 80) | 64x48 | Street-lamp pool Cormac positions himself in |
| Chalk Dust | (64, 80) | 32x32 | Price board updates |

### Technical Notes:
- Transformation Aura is additive blend, 1.5s fade-in; replaced by static outline in reduced-motion mode
- Crash Deflation plays exactly when a premium buff timer expires — the timing IS the joke

---

## 🎮 Sprite Sheet 6: UI Elements
**File:** `confidence_ui.png`
**Dimensions:** 256x256 pixels

### Shop & Buff UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Product Menu Frame | (0, 0) | 160x192 | Carnival-poster shop interface, tier-tabbed |
| Buff Active Display | (160, 0) | 96x48 | Current effect + remaining potency |
| Buff Timer | (160, 48) | 64x32 | Duration countdown ring |
| Placebo Bonus Indicator | (224, 48) | 32x32 | Hidden belief bonus glyph (±10%) |
| Crash Warning | (160, 80) | 96x48 | "WARNING: CRASH AFTER" — premium confirm gate |
| Stack Warning | (160, 128) | 96x32 | "Overlap can cause... unpredictability" |
| Haggle Options Panel | (0, 192) | 128x64 | Accept / Haggle / Bulk / Sob Story / Walk Away |
| Haggle Result Stamps | (128, 192) | 64x64 | Two 32x32 pairs: success flourish / mock-offense |
| Valued Customer Badge | (192, 192) | 48x48 | 5-purchase loyalty seal |
| Special Reserve Tab | (192, 160) | 64x32 | Black-label menu section, unlock-gated |

### Technical Notes:
- Walk Away option triggers Cormac's Calling Back state + "special offer" popup reusing Product Menu Frame
- Buff Timer ring turns Reserve Black in final 10% — crash telegraph for premium tonics

---

## 🎬 Animation Specifications

### The Pitch Cycle:
- **Duration:** 8 seconds loop
- **Frames:** Pitch (3s) → Point at passerby (1.5s) → Presenting Bottle (2s) → Close lean (1.5s)
- **Pattern:** Loops while player is in range; Point frame targets player position
- **Trigger:** Player within cart radius
- **Purpose:** Cormac is never off — the pitch IS the location
- **Audio Sync:** Pitch bark lines rotate on each Point frame
- **Performance Optimization:** Loop drops to Pitch + Presenting only on Low LOD

### Custom Blend Mixing:
- **Duration:** 3 seconds
- **Frames:** 5 + smoke puffs
- **Pattern:** Grab jars → theatrical pour → Secret Recipe Box tap → puff → bottle raised
- **Trigger:** Any purchase confirmation
- **Purpose:** The theatre is the product; every sale gets the show
- **Audio Sync:** Glass clinks on pours; cheesy "transformation" sting on the final puff
- **Performance Optimization:** Smoke puffs reduced to 1 frame on Low LOD

### Buff Activation:
- **Duration:** 1.5 seconds
- **Frames:** Drink → Buff Activation Burst → aura settle (premium only)
- **Trigger:** Consuming any tonic
- **Purpose:** Feedback that "it's working" — feeding the placebo loop
- **Audio Sync:** Magical transformation sound (deliberately cheesy) on burst frame
- **Performance Optimization:** Aura becomes static outline

### The Crash:
- **Duration:** 2 seconds
- **Frames:** 3 deflation wisps + posture slump overlay
- **Trigger:** Premium buff timer expiry ("The Transformation," "Emergency Confidence")
- **Purpose:** Consequence made visible — the Crasher NPC's whole arc in one effect
- **Audio Sync:** Deflating slide-whistle-adjacent crash sound, ends in silence
- **Performance Optimization:** Single-frame gray flash

### Cart Reposition:
- **Duration:** Off-screen between visits
- **Frames:** Cart Packed sprite at new anchor on next area load
- **Trigger:** Area re-entry
- **Purpose:** "Location changes slightly each visit" — mobile vendor authenticity
- **Audio Sync:** Distant cart-wheel rattle on area load if position changed
- **Performance Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements
**File:** `confidence_accessibility.png` (supplemental sheet — delivered alongside the 6 base files, not counted in their total)
**Dimensions:** 256x192 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Product Menu, Bold | (0, 0) | 96x64 | Heavy-bordered menu, enlarged tier tabs with text labels |
| Crash Warning, Bold | (96, 0) | 96x48 | Oversized warning with icon + text, impossible to miss |
| Cormac Interaction Outline | (192, 0) | 48x64 | White-on-dark cart hotspot |
| Haggle Panel, Bold | (0, 64) | 96x64 | Five options with distinct icons, thick dividers |
| Hidden Compartment Outline | (96, 64) | 64x64 | Discoverable-interaction highlight |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Aura, Static | (160, 64) | 48x64 | Fixed outline replacing pulsing Transformation Aura |
| Shimmer, Off | (208, 64) | 24x48 | Matte bottle state, no sparkle cycling |
| Crowd, Calm | (0, 128) | 64x48 | Energy lines removed, static onlookers |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pitch Bark Bubble | (64, 128) | 32x32 | Speech-burst glyph on each pitch line |
| Transformation Sting Star | (96, 128) | 32x32 | Cheesy star glyph on buff activation |
| Crash Slide Glyph | (128, 128) | 32x32 | Downward-arrow wisp on crash sound |
| Glass Clink Icon | (160, 128) | 32x32 | On mixing pours |
| Coin Chime Icon | (192, 128) | 32x32 | On transaction complete |
| Cart Rattle Icon | (224, 128) | 32x32 | On reposition detection |

### Colorblind Considerations:
- Tonic tiers coded by label color AND cap shape (round/square/crown/skull) AND menu tab text
- Buff Timer crash telegraph uses ring segmentation, not color shift alone
- Haggle options carry distinct icons; all menu rows and the cart hotspot meet the 44px minimum touch target

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import)
- **Fallback:** PNG high quality for Cormac portraits and signage

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| confidence_environment | confidence_cart | 512x512 |
| confidence_characters | cormac, crowd_customers | 512x512 |
| confidence_items_fx | tonic_bottles, effects, ui | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full crowd (2 clumps + 4 NPCs), smoke, shimmer, aura effects |
| Medium | 1 crowd clump, single-frame smoke, shimmer on hero bottle only |
| Low | No crowd clumps, no particles, static lantern glow |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 10 per frame
- **Memory Footprint:** 25 MB maximum
- **Particle Limit:** 10 (smoke + shimmer + burst combined)

### Performance Notes:
- Cart is a single composite node — reposition costs one transform, not a scene reload
- Crowd clumps share one reaction-overlay pair rather than per-NPC expressions

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Cart anchored to one of three Marker2D spawn points on Cobblestone Market Street, rotated per visit
- CPUParticles2D (not GPU) for smoke puffs and buff bursts; potion shimmer via 3-frame AnimatedSprite2D, disabled in reduced-motion mode
- Buff system: timed StatusEffect resources with stack-with-diminishing-returns rule and crash payloads on premium tonics; hidden placebo modifier reads `confidence_state.successful_uses` (±10%)
- State tracking per `confidence_man_state` (purchases_count, valued_customer, reserve_unlocked, crashes_experienced, beyond_the_potion_earned, last_cart_anchor)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Pitch Point frame | Rotating bark line | On each Point in the 8s loop |
| Mixing final puff | Cheesy "transformation" sting | On puff frame |
| Buff Activation Burst | Magical activation sound | On burst frame |
| Crash Deflation | Deflating crash sound → silence | Starts on first wisp, silence by frame 3 |
| Haggle success | "Sharp customer!" + coin chime | On success stamp |
| Walk Away trigger | "Wait, WAIT!" call-back | 0.5s after player exits radius |
| Cart reposition | Distant wheel rattle | On area load, new anchor only |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| True Confidence | Buff Active Display (must stay empty), Genuine Respect expression | Complete a major challenge with zero tonics active — Cormac acknowledges it |
| Cormac's Assistant | The Pitch states, First-Timer NPC, Haggle Panel | Moral-choice sale assist; player works the crowd side |
| The Ingredients | Ingredient Jars, Label Sheet, Hidden Compartment Open | Examine chain revealing the herbs/alcohol/theatre breakdown |
| Beyond the Bottle | Portrait Respect, Empty Bottle prop | Graduation quest — +30 Bravado, Cormac's real respect |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Blarney Trap | Cart anchor positioned near its entrance; pre-pub purchase flow | None — same street scene |
| Trinity of Pints | "Exam confidence" pitch variant before challenge courses | Dialogue-only crossover |
| The Quiet Man | "Fearless Fighter" bottle referenced pre-fight; buff persists into the Pit | Buff carries via StatusEffect system |
| Shenanigans / Paddy's Book | Fearless-gambler demand; confidence before gambling (ironic) | Buff carries; Cormac dialogue nods to it |
| The Craic Tax | Prime positioning territory — anchor point three | Same street network |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A one-man carnival parked between you and the pub door"
- **Color Mood:** Carnival Red and Apothecary Gold blazing against Wood Brown practicality — the cart is brighter than everything around it, on purpose
- **Lighting:** Lantern-warm pitch pool at dusk; the cart makes its own spotlight
- **Texture:** Painted wood gone glossy from handling, brass polished only where customers look, chalk-dusted price board

### Environmental Storytelling:
- The Small Print Plaque ("No refunds") undercuts every banner above it
- The Secret Recipe Box is visibly ornamental — the tell is there for players who look
- Ingredient Jars with real adaptogen labels next to a Label Sheet: the whole business model in two props
- The Crasher NPC standing in the cart's shadow is the warning label the bottles don't carry

### Character Integration Notes:
- Cormac's mustache is its own layer — micro-twitch on the Close and Honest Mode states
- Honest Mode must read as a different man: shoulders down, gestures small, same coat
- The crowd is a prop for the pitch; reaction overlays keep them alive without stealing focus

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Full Pitch** - Cormac mid-bark, arms wide, crowd energy lines radiating, "GUARANTEED BOLDNESS" banner overhead
2. **The Crash** - A player character deflating in gray wisps the exact second their god-hour ends
3. **The Hidden Compartment** - Black-label Special Reserve sliding out of an innocent cart panel
4. **The Small Print** - "Entertainment purposes. Individual results vary. No refunds." under all that gold
5. **Honest Mode** - The act dropped, elbow on cart, twelve years of belief retail in one pose

### Quote Potential:
- "Some people call me a con man. I'm RIGHT HERE. I call MYSELF a con man. Where's the CON if I'm HONEST about it?"
- "The potion is just the SPARK. YOU are the FIRE!"
- "I feel like I could FIGHT A BEAR. Is there a bear? I want to fight it."
- "I was a GOD for an hour. Now I want to hide under a rock."
- "Between us? The herbs help. The alcohol helps. But mostly? It's you deciding to be brave. I just give you permission."

---

## 📋 Required PNG Files (6 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | confidence_cart.png | 512x384 |
| 2 | cormac.png | 384x384 |
| 3 | crowd_customers.png | 384x192 |
| 4 | tonic_bottles.png | 256x192 |
| 5 | confidence_effects.png | 256x128 |
| 6 | confidence_ui.png | 256x256 |

**Total Estimated Memory:** ~12 MB

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `confidence_cart.png` (512x384)
- [ ] `cormac.png` (384x384)
- [ ] `crowd_customers.png` (384x192)
- [ ] `tonic_bottles.png` (256x192)
- [ ] `confidence_effects.png` (256x128)
- [ ] `confidence_ui.png` (256x256)
- [ ] `confidence_accessibility.png` (256x192, supplemental)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha channel |
| Color Space | sRGB |
| DPI | 72 (screen resolution) |
| Compression | Lossless PNG |
| Naming Convention | snake_case, all lowercase |
| Layer Organization | Preserve layers in master file |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/layered file with organized layer groups (mustache and bottle labels on separate layers for future product-line additions)
- **Documentation:** Animation timing reference sheet (8s pitch loop, 3s mixing, 1.5s activation, 2s crash)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Carnival Red #DC143C, Apothecary Gold #FFD700, Wood Brown #8B4513, Reserve Black #1A1A1A)
- [ ] Small Print Plaque legible on examine — the disclaimer is the punchline
- [ ] Tier double-coding verified (label color + cap shape) on every bottle
- [ ] Crash Deflation timing lands exactly on buff expiry in engine test
- [ ] Accessibility visual alternatives included for all audio cues (bark, sting, crash, clink, chime, rattle)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (self-aware con artistry, belief as product) is clear throughout all assets
- [ ] Easter eggs discoverable: Secret Recipe Box, Ingredient Jars with real studies, Label Sheet, Placebo Glint
- [ ] Performance optimized (10-particle cap, composite cart node, shared crowd overlays)
- [ ] Touch zone sizing considered (44px minimum — menu rows, haggle options, cart hotspot compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (cap shapes, ring segmentation, icon-coded haggling)
- [ ] Social media viral potential maximized (pitch composition, crash moment framing)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia, Cobblestone Market Street only |
| Cultural Specificity | ✅ | Dublin market culture, carnival barker tradition |
| Satirical Targets Appropriate | ✅ | Snake-oil sellers and buyer belief — not actual supplements; punches at the con, not the nervous |
| Seedy Underbelly Present | ✅ | Belief sold at premium prices, positioned to catch nervous tourists at pub doors |
| Gameplay Value Established | ✅ | Bravado buff economy, haggle minigame, crash risk/reward, Valued Customer track |
| Technical Feasibility | ✅ | Single composite cart, 6 sheets, mobile optimization documented |
| Performance Budget | ✅ | 60 FPS, 10 draw calls, 25MB |
| Accessibility Features | ✅ | Visual cues for every audio beat, static aura/shimmer variants, shape-coded tiers |
| No Crypto Elements | ✅ | Absent from source and spec |
| Social Media Integration | ✅ | Five viral moments identified, quote bank sourced from profile |

**The Confidence Man delivers a con you can see through and buy from anyway. Every asset — the gold banners over the no-refunds plaque, the shimmer that might be placebo, the crash that always comes on time — sells the same honest lie: confidence is 15 Sovs, and it works exactly as much as you decide it does.**

**"Ready to become who you were MEANT to be?"**
