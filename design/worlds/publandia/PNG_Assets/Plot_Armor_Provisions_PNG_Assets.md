# Plot Armor Provisions - Complete PNG Asset Requirements

## 📋 Overview
Plot Armor Provisions is the food cart that knows it's keeping you alive for the story — a warm, cheerful, suspiciously well-placed street vendor where Deirdre Murphy serves hearty Irish comfort food, maximum HP restoration, and the gentle, never-quite-stated certainty that you're the main character. This document specifies every PNG needed to sell the gag: the cart is cozy, the stew is perfect, the menu changes before the game tells you why, and nobody — nobody — questions the placement.

**Location ID:** `publandia_vendor_plot_armor_01`
**Theme:** RPG vendor convenience made flesh — plot armor in delicious edible form, meta-awareness played completely sincere
**Zone:** Cobblestone Market Street, Publandia (conveniently placed, always)
**Hours:** 11 AM - 3 AM (always there when you need it, suspiciously)
**Primary Function:** Street vendor / major HP restoration / pre-event preparation — adaptive menu shop, "Suggestion" mechanic, Plot Essential status progression, four quest hooks

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Hearth Orange | #FF7F50 | Cart lighting, awning, warm glow effects |
| Stew Brown | #8B4513 | Cart wood, food bases, chalkboard frame |
| Warm Cream | #FFFDD0 | Signage backgrounds, apron, steam highlights |
| Hero Gold | #FFD700 | Shield-and-fork logo, Plot Essential badge, suggestion sparkle |
| Chalk White | #F5F5F0 | Chalkboard lettering, menu board text |
| Market Mist Gray | #B0C4DE | Cobblestone Market Street mist, cool backdrop the cart glows against |
| Knowing Green | #2E8B57 | Deirdre's shawl, off-menu card accents, chime visual |
| Meta Violet | #9370DB | Fourth-wall wobble indicator, mysterious chime glyph |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/plot_armor_provisions/
├── environment/
│   ├── plot_armor_cart.png
│   └── provisions_stations.png
├── npcs/
│   ├── deirdre_murphy.png
│   └── provision_customers.png
├── objects/
│   └── provisions_items.png
├── effects/
│   └── provisions_ui_fx.png (shared with ui/)
└── ui/
    └── provisions_ui_fx.png
```

---

## 🛒 Sprite Sheet 1: The Cart & Signage
**File:** `plot_armor_cart.png`
**Dimensions:** 512x384 pixels
**Color Palette:** Hearth Orange #FF7F50, Stew Brown #8B4513, Warm Cream #FFFDD0, Hero Gold #FFD700

### Cart Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cart Body (Day) | (0, 0) | 256x192 | Cheerful wooden cart, scalloped awning, warm lantern light, impossibly inviting |
| Cart Base & Wheels | (0, 192) | 256x64 | Sturdy wheels that have "always been here" — zero road wear, don't think about it |
| Cobblestone & Mist Backdrop | (0, 256) | 256x128 | Cobblestone Market Street ground tile with cool gray mist for the cart to glow against |

### Signage (Every Word Load-Bearing):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shield-and-Fork Logo | (256, 0) | 64x64 | Hero Gold shield crossed with a fork — the crest of edible invincibility |
| Main Sign | (320, 0) | 192x48 | "PLOT ARMOR PROVISIONS" — hand-painted, confident, warm |
| Subtitle Sign | (320, 48) | 192x32 | "Keeping You Alive Since You Started Playing" |
| Chalkboard Special | (256, 64) | 64x96 | "TODAY'S SPECIAL: Whatever You Need Right Now" — chalk text on separate layer, it changes |
| Side Sign | (320, 80) | 128x48 | "Main Characters Eat Free*" — bold heroic lettering |
| Asterisk Fine Print | (448, 80) | 64x48 | "*They Don't, But It Sounded Heroic" — legible only on examine, worth the tap |
| Pre-Boss Specials Banner | (320, 128) | 192x48 | "Pre-Boss Specials Available • We Know You're About to Do Something Stupid" |
| Awning Scallop Strip | (256, 160) | 64x32 | Tileable Hearth Orange awning edge |
| Warm Bunting Strip | (320, 176) | 192x16 | String lights, permanently on, never flicker — narrative-grade wiring |

### Atmosphere & Placement States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Warm Glow Overlay | (256, 192) | 256x96 | Hearth-light halo pushing back the market mist — the visual thesis of the location |
| Cart Front (Night, 3 AM) | (256, 288) | 128x96 | Lantern-lit night state, still open, still expecting you |
| Save Point Adjacency Tile | (384, 288) | 128x48 | Dressing tile placing the cart "coincidentally" beside a save point |
| Boss-Gate Adjacency Tile | (384, 336) | 128x48 | Dressing tile placing the cart directly before a difficult area, as always |

### Technical Notes:
- Chalkboard text lives on its own layer; the board redraws per game state (see Adaptive Menu system)
- Warm Glow Overlay is additive blend, alpha 0.35, and must read against the mist backdrop
- Adjacency tiles let level designers stamp the cart anywhere the plot needs it — which is everywhere

---

## 🍲 Sprite Sheet 2: Hot Station, Display Case & Adaptive Menu Board
**File:** `provisions_stations.png`
**Dimensions:** 512x256 pixels

### The Hot Station:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stew Pot Simmer Frame 1 | (0, 0) | 64x64 | The perpetually simmering Irish stew — surface roll begins |
| Stew Pot Simmer Frame 2 | (64, 0) | 64x64 | Bubble crest, ladle at rest |
| Stew Pot Simmer Frame 3 | (128, 0) | 64x64 | Bubble break, steam release — loops forever, always perfect temperature |
| Meat Pie Warmer | (192, 0) | 64x64 | Meat pies, always fresh, no visible restocking ever observed |
| Full Irish Components | (256, 0) | 128x64 | Sausages, rashers, eggs, pudding — ready to assemble into The Complete Recovery |
| Soup Kettle (Daily Rotation) | (384, 0) | 64x64 | Hearty soup, rotated daily, plot-appropriate |
| Ladle & Utensil Rack | (448, 0) | 64x64 | Well-worn tools of the provision trade |
| Hot Station Base | (0, 64) | 192x96 | Counter, burners, and the warm heart of the cart |

### The Display Case:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Display Case Base | (192, 64) | 192x96 | Glass case, warm interior light, grab-and-survive selection |
| Sausage Rolls Tray | (0, 160) | 64x32 | Quick, satisfying, Bradley-approved |
| Pasties Tray | (64, 160) | 64x32 | Various fillings, all of them correct |
| Sandwich Stack | (128, 160) | 64x32 | Hearty sandwiches in confident piles |
| Emergency Provisions (Wrapped) | (192, 160) | 64x32 | Travel-wrapped parcels labeled for emergencies you haven't had yet |
| Price Tag Set | (256, 160) | 64x32 | 6-40 Sovs range, handwritten, non-negotiable, fair |
| Soup Label Set | (320, 160) | 64x32 | Rotating chalk labels for the daily soup |

### The Adaptive Menu Board:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Adaptive Menu Board Frame | (384, 64) | 128x192 | Tall chalk menu board with six slotted panel rails — the board that knows |
| Swap Panel: Standard Fare | (0, 192) | 96x32 | Default panel listing the always-available six |
| Swap Panel: Pre-Fight Fuel | (96, 192) | 96x32 | Slides in when combat approaches |
| Swap Panel: Liquid Fortitude Stew | (192, 192) | 96x32 | Slides in when a boss area is nearby |
| Swap Panel: The Second Wind | (288, 192) | 96x32 | Slides in when player HP/SP runs low |
| Swap Panel: Plot Convenience Pie | (0, 224) | 96x32 | Slides in before crucial decisions |
| Swap Panel: The Protagonist's Portion | (96, 224) | 96x32 | Slides in at main quest milestones — Hero Gold border |
| Swap Panel: Today's Special Chalk | (192, 224) | 96x32 | "Whatever You Need Right Now" in Deirdre's handwriting |
| Swap Panel: Blank Chalk | (288, 224) | 96x32 | Clean slate panel for future events the board already knows about |

### Technical Notes:
- Stew pot 3-frame loop is the location's heartbeat — it must never stop simmering
- Swap panels slide into the menu board frame rails; the swap animates only when a major event approaches (see Animation Specifications)
- Display case interior uses a static warm gradient, no realtime light

---

## 👩‍🍳 Sprite Sheet 3: Deirdre Murphy
**File:** `deirdre_murphy.png`
**Dimensions:** 384x256 pixels

### Deirdre States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Warm Default | (0, 0) | 96x128 | 50s Irish woman, apron, shawl, warm smile — maternal HQ |
| Knowing Smile | (96, 0) | 96x128 | The look. Eyes that have read ahead in the script |
| Serving Handoff | (192, 0) | 96x128 | Bowl extended across the counter, steam trailing |
| Suggestion Pose | (288, 0) | 96x128 | One finger raised toward the menu board: "You'll want the Pre-Fight Fuel. Trust me." |

### Deirdre Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Apron & Shawl | (0, 128) | 64x64 | Warm Cream apron, Knowing Green shawl texture |
| Knowing Eyes Close-Up | (64, 128) | 64x64 | The uncanny certainty, rendered at examine scale |
| Warm Smile Close-Up | (128, 128) | 64x64 | Genuine warmth — she really is glad you're here |
| Ladle Hand | (192, 128) | 64x64 | Practiced stir grip for the stew loop |
| Bowl Handoff Hand | (256, 128) | 64x64 | Mid-pass hand for the serving animation |
| Humming Notes | (320, 128) | 64x64 | Small note glyphs for her pleasant, constant humming |

### Dialogue Portraits:
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Portrait Warm | (0, 192) | 64x48 | Default dialogue box face — "There you are! I was expecting you." |
| Portrait Knowing | (64, 192) | 64x48 | For recommendations and things she shouldn't know |
| Portrait Cryptic | (128, 192) | 64x48 | For "The cart goes where it's needed. I follow the cart. The cart knows." |
| Portrait Reassuring | (192, 192) | 64x48 | "You're going to be fine. You're the protagonist." |
| Plot Essential Greeting Card | (256, 192) | 128x48 | Name-greeting banner shown once Plot Essential status unlocks — she knows your name now |
| Warm Rim-Light Strip | (0, 240) | 384x16 | Reusable Hearth Orange rim-light band applied to Deirdre against the mist |

### Technical Notes:
- The Knowing Smile must be a small change from Warm Default — two pixels of eyelid, no eyebrow theatrics; the horror is in the subtlety
- Suggestion Pose pairs with the recommendation "ping" and the suggestion highlight UI
- Rim-light strip keeps her readable at night state without a second character pass

---

## 👥 Sprite Sheet 4: Customer NPCs
**File:** `provision_customers.png`
**Dimensions:** 256x256 pixels

### Customer States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Suspicious One | (0, 0) | 64x96 | Arms crossed, eyeing the cart's placement — "Don't you find it weird she's ALWAYS here?" |
| The Regular Hero | (64, 0) | 64x96 | Another clear protagonist, eating determinedly before their own boss fight |
| The NPC Who Doesn't Get It | (128, 0) | 64x96 | Ordering politely, receiving standard service, zero recommendations — not a protagonist, doesn't need armor |
| The Returner | (192, 0) | 64x96 | Back from surviving something, grateful and slightly awed |

### Reaction Poses:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Suspicious Squint | (0, 96) | 64x48 | Half-body pose for the "...I guess?" beat |
| Determined Eating | (64, 96) | 64x48 | Regular Hero mid-fortitude-stew, resolute |
| Unrecognized Shrug | (128, 96) | 64x48 | "Weird, she didn't give ME any recommendations." |
| Grateful Bow | (192, 96) | 64x48 | The Returner's thank-you — "That food saved my life. Literally." |

### Dialogue Portraits:
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Portrait Suspicious | (0, 144) | 64x48 | Narrowed eyes for the questions that get non-answers |
| Portrait Regular Hero | (64, 144) | 64x48 | Confident — "She's never been wrong." |
| Portrait Doesn't Get It | (128, 144) | 64x48 | Mild confusion, no narrative weight whatsoever |
| Portrait Returner | (192, 144) | 64x48 | Awe, gratitude, slight thousand-yard warmth |

### Crowd Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Queue Group | (0, 192) | 128x64 | Two-to-three customer clump for busy hours |
| Locals Walking Past | (128, 192) | 128x64 | Publandia locals who do not see the cart at all. Odd. |

### Technical Notes:
- Locals Walking Past never path toward the cart — their oblivion is a scripted, permanent gag
- Maximum one customer NPC rendered at a time on low-end devices (single NPC focus per profile)

---

## 🥧 Sprite Sheet 5: Food & Item Sprites
**File:** `provisions_items.png`
**Dimensions:** 256x128 pixels

### Standard Fare (Always Available):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Irish Stew | (0, 0) | 32x32 | 8 Sovs, +40 HP — classic, reliable, warm |
| Meat Pie | (32, 0) | 32x32 | 10 Sovs, +50 HP — substantial, portable |
| Sausage Roll | (64, 0) | 32x32 | 6 Sovs, +30 HP — quick, satisfying, take two |
| Beef & Guinness Pie | (96, 0) | 32x32 | 12 Sovs, +60 HP — premium restoration |
| Shepherd's Pie | (128, 0) | 32x32 | 10 Sovs, +50 HP — comfort food maximum |
| Full Irish (Portable) | (160, 0) | 48x32 | 15 Sovs, +80 HP, cures Hungover — the complete recovery |
| Emergency Provision Parcel | (208, 0) | 48x32 | Wrapped-for-travel inventory icon of the display case parcels |

### Situational Specials (Appear When Needed):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Pre-Fight Fuel | (0, 32) | 32x32 | 12 Sovs, +50 HP, +10 Attack for one battle — combat approaches |
| Liquid Fortitude Stew | (32, 32) | 32x32 | 15 Sovs, +60 HP, Fear immunity 30 min — boss area nearby |
| The Second Wind | (64, 32) | 32x32 | 18 Sovs, +70 HP, +20 SP, removes fatigue — for rough times |
| Plot Convenience Pie | (96, 32) | 32x32 | 20 Sovs, +80 HP, +5% Luck for 1 hour — think clearly, eat first |
| The Protagonist's Portion | (128, 32) | 48x48 | 25 Sovs, full HP restore, +all stats 30 min — the big one, Hero Gold plating |

### Off-Menu Items (Plot Essential Status Required):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Narrative Insurance | (176, 32) | 32x32 | 30 Sovs, survive one fatal blow per day — "Just in case." |
| The Retcon Roast | (208, 32) | 32x32 | 25 Sovs, removes one recent bad decision's consequences — "Everyone deserves a second draft." |
| Destiny's Dumpling | (176, 64) | 32x32 | 35 Sovs, next critical roll guaranteed — "Some moments matter more." |
| The Epilogue Entrée | (208, 64) | 32x32 | 40 Sovs, full restore + preview of good ending — "You're going to be fine. I've seen it." |

### Presentation & Shop Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Suggested Item Glow Ring | (0, 64) | 32x32 | Hero Gold ring framing whatever Deirdre recommends |
| Plate & Fork Base | (32, 64) | 32x32 | Serving plate underlay for hot items |
| Takeaway Wrap | (64, 64) | 32x32 | Paper wrap underlay for portable items |
| Sovs Price Chip | (96, 64) | 32x32 | Price tag overlay for shop rows: numeral above the lettered word `SOVS`. **The symbol is the word — do not draw a currency mark.** ⚠️ 32x32 will not hold a price figure and `SOVS` legibly. Widen to 64x32, or letter only the numeral on the chip and set `SOVS` once in the shop-row column header. |
| Suggestion Sparkle Frame 1 | (0, 96) | 32x32 | Gold glint spawn |
| Suggestion Sparkle Frame 2 | (32, 96) | 32x32 | Glint sweep |
| Suggestion Sparkle Frame 3 | (64, 96) | 32x32 | Glint peak |
| Suggestion Sparkle Frame 4 | (96, 96) | 32x32 | Glint fade |
| Off-Menu Card Back | (128, 96) | 64x32 | Knowing Green card — "Ask Deirdre" — shown before Plot Essential unlock |
| Sold-Out Chalk X | (192, 96) | 32x32 | Chalk cross for panels the story has moved past |
| Hidden Bonus Star | (224, 96) | 32x32 | Marks the +10% suggestion bonus in purchase feedback |

### Technical Notes:
- All 15 purchasable items ship on this one sheet — shop UI pulls regions directly from the atlas
- The Protagonist's Portion is deliberately oversized (48x48): it should look like it doesn't fit the grid, because it doesn't fit the rules
- Situational and off-menu icons carry distinct silhouettes, never color-only differentiation

---

## 🎮 Sprite Sheet 6: UI & Effects
**File:** `provisions_ui_fx.png`
**Dimensions:** 256x256 pixels

### Adaptive Menu UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Adaptive Menu Panel | (0, 0) | 128x128 | In-game shop popup; item rows populate from current event flags |
| Suggestion Highlight Frame | (128, 0) | 96x48 | Glowing "Deirdre recommends" border snapped to the suggested row |
| Plot Essential Badge | (224, 0) | 32x32 | Hero Gold shield-and-fork badge — protagonist rate unlocked |
| Confirm Button ("Eat First") | (128, 112) | 96x48 | Primary purchase button, 48px tall — over the 44px touch floor |
| Decline Button ("No Thanks — Bold Choice") | (128, 160) | 96x48 | Decline with mild concern from Deirdre, no penalty |
| Price Row Strip | (128, 208) | 96x24 | `N SOVS` pricing backplate for menu rows — word lettered, no currency mark |
| Swap Flash Frame 1 | (128, 232) | 32x24 | Menu row refresh glint when inventory adapts |
| Swap Flash Frame 2 | (160, 232) | 32x24 | Glint sweep |
| Swap Flash Frame 3 | (192, 232) | 32x24 | Glint settle |

### Status Icons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Well Fed Icon | (128, 48) | 32x32 | Steaming bowl — major HP restoration, +10% healing 1 hour |
| Plot Protected Icon | (160, 48) | 32x32 | Shield-and-fork — ate before a major event, hidden survival bonus |
| Deirdre's Suggestion Icon | (192, 48) | 32x32 | Gold check — followed the recommendation, +10% item effect |
| Narrative Nourished Icon | (224, 48) | 32x32 | Green laurel — Plot Essential status, ongoing minor luck |

### Meta-Moment Indicators:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fourth-Wall Wobble Frame 1 | (128, 80) | 32x32 | Screen-corner glyph shivers — she said something too knowing |
| Fourth-Wall Wobble Frame 2 | (160, 80) | 32x32 | Wobble peak, Meta Violet fringe |
| Fourth-Wall Wobble Frame 3 | (192, 80) | 32x32 | Settle — everything is fine, eat your stew |
| Mysterious Chime Glyph | (224, 80) | 32x32 | Violet star-note shown when Deirdre "knows" something |
| Fourth-Wall Ripple Overlay | (224, 112) | 32x96 | Vertical screen-edge ripple strip for the meta moment |
| Warm Vignette Corner | (224, 208) | 32x48 | Corner warmth overlay while standing at the cart |

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Food Steam Frame 1 | (0, 128) | 32x48 | Steam wisp rise |
| Food Steam Frame 2 | (32, 128) | 32x48 | Wisp curl |
| Food Steam Frame 3 | (64, 128) | 32x48 | Wisp dissipate |
| Pot Bubble Burst | (96, 128) | 32x48 | Stew surface pop, syncs to bubbling audio |
| Warm Glow Radial | (0, 176) | 64x48 | Hearth-light radial for cart lanterns |
| Hearth Flicker Frame A | (64, 176) | 32x48 | Gentle lantern breathing, bright |
| Hearth Flicker Frame B | (96, 176) | 32x48 | Gentle lantern breathing, dim |
| Knowing-Chime Ring Frame 1 | (0, 224) | 32x32 | Violet ring spawn at Deirdre's head height |
| Knowing-Chime Ring Frame 2 | (32, 224) | 32x32 | Ring expansion |
| Knowing-Chime Ring Frame 3 | (64, 224) | 32x32 | Ring fade — the sound of narrative convenience, visualized |
| Market Mist Wisp | (96, 224) | 32x32 | Drifting Cobblestone Market Street mist particle |

### Technical Notes:
- Suggestion Highlight Frame + Suggested Item Glow Ring (Sheet 5) fire together on approach
- Fourth-wall wobble is a UI-layer effect only — the world never wobbles, just your certainty about it
- All buttons and status icons meet the 44px minimum touch target when rendered at UI scale (2x)

---

## 🎬 Animation Specifications

### Stew Stirring (The Heartbeat):
- **Duration:** 2.4 seconds per loop
- **Frames:** 3 (Simmer Frames 1 → 2 → 3 → loop)
- **Pattern:** Continuous loop; Pot Bubble Burst overlays on frame 3 every second cycle
- **Trigger:** Constant while location is loaded — the stew never stops
- **Purpose:** The cart's perpetual warmth; the visual promise that the food is always ready because you were always coming
- **Audio Sync:** Stew bubbling (comforting) on each frame-3 bubble break
- **Performance Optimization:** Low LOD drops the bubble burst overlay, keeps the 3-frame loop

### The Knowing Smile Beat:
- **Duration:** 1.2 seconds, hold 2 seconds, release 0.8 seconds
- **Frames:** 2 (Warm Default → Knowing Smile → hold → Warm Default)
- **Pattern:** Single ease-in transition, held, eased out — never a snap
- **Trigger:** Player approach when a tracked event flag is active; also on any "how did you know" dialogue branch
- **Purpose:** The entire location in one expression — she knows, she won't say, the smile is kind
- **Audio Sync:** Deirdre's knowing "hmm" lands exactly at the smile's peak
- **Performance Optimization:** None needed (2-frame swap)

### Menu Board Item Swap (Event Approaching):
- **Duration:** 1.0 second per panel
- **Frames:** 4 (panel slide-out 0.3s → rail empty 0.2s → new panel slide-in 0.3s → Swap Flash 0.2s)
- **Pattern:** One panel at a time, top rail first; Swap Flash Frames 1-3 punctuate the landing
- **Trigger:** Hidden pre-event detection flag change (combat, boss, low HP/SP, decision, milestone)
- **Purpose:** The player sees the menu adapt to a future the game hasn't announced yet — the core meta gag, animated
- **Audio Sync:** Mysterious chime on the slide-in landing frame
- **Performance Optimization:** Low LOD swaps panels instantly with Swap Flash only

### Serving Handoff:
- **Duration:** 1.5 seconds
- **Frames:** 3 (Warm Default → Serving Handoff → hold → Warm Default)
- **Pattern:** Bowl extends with Food Steam Frames 1-3 trailing the pass
- **Trigger:** Purchase confirmed
- **Purpose:** Purchase feedback with warmth — the meal changes hands like a blessing
- **Audio Sync:** Food served sound on the handoff frame
- **Performance Optimization:** Steam trail reduced to 1 wisp on low-end devices

### Suggestion Sparkle:
- **Duration:** 0.8 seconds, repeats every 6 seconds while unpurchased
- **Frames:** 4 (Sparkle Frames 1 → 2 → 3 → 4)
- **Pattern:** Single glint sweep across the suggested item, then rest
- **Trigger:** Deirdre's recommendation issued; clears on purchase or decline
- **Purpose:** Marks the +10% bonus item without a tutorial popup — trust the gold
- **Audio Sync:** Recommendation "ping" on first cycle only
- **Performance Optimization:** Repeat interval extends to 12 seconds on low LOD

### The Meta-Moment Wobble:
- **Duration:** 0.9 seconds
- **Frames:** 3 (Wobble Frames 1 → 2 → 3)
- **Pattern:** Screen-corner glyph shiver + Fourth-Wall Ripple Overlay at 20% alpha, one pass, no loop
- **Trigger:** Flagged "too knowing" dialogue lines ("I've seen it.", "You're the main characters. Now eat.")
- **Purpose:** A half-second of the game admitting something before both of you agree to move on
- **Audio Sync:** Fourth-wall sound effect spans the full 0.9 seconds
- **Performance Optimization:** Ripple overlay dropped on low LOD; glyph frames only

### Hearth Glow Breathing:
- **Duration:** 4 seconds per cycle
- **Frames:** 2 (Flicker Frame A → B → A), alpha crossfade
- **Pattern:** Slow sine crossfade — breathing, never flickering; this cart does not do ominous
- **Trigger:** Constant; intensity +15% during 3 AM night state
- **Purpose:** The warm hearth glow against the Cobblestone Market Street mist — safety rendered in light
- **Audio Sync:** None
- **Performance Optimization:** Static Warm Glow Radial on low LOD

---

## ♿ Accessibility Sprite Requirements
**File:** `provisions_accessibility.png` (supplemental sheet — delivered alongside the 6 base files, not counted in their total)
**Dimensions:** 256x192 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Adaptive Menu Panel, Bold | (0, 0) | 96x64 | Thick-bordered menu popup with enlarged rows and high-contrast pricing |
| Suggestion Highlight, Bold | (96, 0) | 96x64 | Heavy gold-on-dark outline; recommendation readable without glow effects |
| Deirdre Interact Outline | (192, 0) | 64x64 | White-on-dark outline for Deirdre's counter interaction hotspot |
| Menu Board Examine Outline | (0, 64) | 64x64 | Outlined board hotspot; swap panels at readable weight |
| Display Case Hotspot Outline | (64, 64) | 64x64 | Outlined case hotspot with enlarged item silhouettes |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Steam, Static | (128, 64) | 32x32 | Fixed single-wisp steam replacing the 3-frame rise loop |
| Meta Indicator, Static | (160, 64) | 32x32 | Non-animated violet glyph — the fourth-wall wobble becomes a steady marker, no shiver |
| Chime Ring, Static | (192, 64) | 32x32 | Single fixed ring replacing the expansion animation |
| Hearth Glow, Steady | (224, 64) | 32x32 | Constant-intensity glow — breathing crossfade disabled |
| Menu Swap, Instant | (128, 96) | 64x32 | Panels change with no slide and no flash — before/after only |
| Stew Surface, Still | (192, 96) | 64x32 | Static simmering-stew top with painted (non-animated) bubbles |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stew Bubble Glyph | (0, 128) | 32x32 | Rising bubble icon pulsing with the stew bubbling ambience |
| Plate-Served Burst | (32, 128) | 32x32 | Radiating plate icon on the food served sound |
| Recommendation Ping Badge | (64, 128) | 32x32 | Gold exclamation badge for the recommendation "ping" |
| Knowing "Hmm" Bubble | (96, 128) | 32x32 | Small thought-bubble "hmm" over Deirdre at her knowing beat |
| Mysterious Chime Star | (128, 128) | 32x32 | Violet star-burst wherever the mysterious chime fires |
| Fourth-Wall Crack Glyph | (160, 128) | 32x32 | Hairline-crack icon for the fourth-wall sound effect |
| Humming Notes Cue | (192, 128) | 32x32 | Drifting note glyphs for Deirdre's pleasant, constant humming |
| Sizzle Lines Cue | (224, 128) | 32x32 | Heat-line glyph over the hot station for food sizzling |
| Subtitle Banner Backplate | (0, 160) | 256x32 | High-contrast caption strip for all Deirdre dialogue and ambient text |

### Colorblind Considerations:
- Suggested items are marked by the gold ring AND the sparkle AND the ping badge — shape, motion, and icon, never hue alone
- The four status icons (Well Fed / Plot Protected / Deirdre's Suggestion / Narrative Nourished) use four distinct silhouettes: bowl, shield, check, laurel
- Situational vs. off-menu items differ by card shape (rounded tray vs. Knowing Green card back), not color coding
- Menu rows, Confirm/Decline buttons, status icons, and all examine hotspots meet the 44px minimum touch target at UI scale

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) Deirdre's portraits and all signage text ship uncompressed — the fine print must stay legible
- **Fallback:** PNG high quality for signage sheet and dialogue portraits (text-critical assets)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| plot_armor_environment | plot_armor_cart, provisions_stations | 1024x1024 |
| plot_armor_characters | deirdre_murphy, provision_customers | 512x512 |
| plot_armor_items_ui | provisions_items, provisions_ui_fx, provisions_accessibility | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility — all three atlases sit comfortably under.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full steam loop + bubble burst, animated menu swaps, glow breathing, wobble ripple, 1 customer NPC + queue group |
| Medium | 3-frame steam only, animated swaps without flash, static glow, glyph-only wobble, 1 customer NPC |
| Low | Static steam wisp, instant menu swaps, static glow radial, static meta glyph, no customer NPCs, stew loop retained (the stew never stops) |

### Performance Targets:
- **Target FPS:** 60 (profile floor: never below 45 on minimum-spec devices)
- **Max Draw Calls:** 10 per frame (per the location's performance budget)
- **Memory Footprint:** 25 MB maximum (per profile budget; asset set lands well under — see Required PNG Files)
- **Particle Limit:** 12 (steam wisps + mist; simplified steam per profile)

### Performance Notes:
- Single NPC focus: Deirdre is the only always-animated character; customers load on demand
- Adaptive menu swaps are sprite-region changes, not new texture loads — zero streaming hitch when the board "knows"
- Warm Glow Overlay and Vignette are two static quads with alpha, not shader passes
- Cart night state is a sprite swap, not a lighting pass

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D for cart/stations, AnimatedSprite2D for Deirdre and stew loop, CPUParticles2D (not GPU) for steam and market mist, CanvasLayer for menu UI and meta-moment overlay
- **Hidden Pre-Event Detection System:** the adaptive menu is driven by game event flags — `upcoming_combat`, `upcoming_boss`, `player_low_hp_sp`, `upcoming_decision`, `main_quest_milestone`. On flag change, the menu board swaps in the matching panel (Sheet 2 swap panels), the shop adds the matching situational item (Sheet 5), and Deirdre's first-approach dialogue selects the matching recommendation. The player is never told why. The board just knows.
- Suggestion mechanic: purchasing the flagged item applies the +10% bonus and stamps the Hidden Bonus Star in purchase feedback; declining costs nothing but earns Portrait Warm with mild concern
- State tracking per `plot_armor_provisions_state` (purchases_before_events, plot_essential_unlocked, suggestions_followed, questions_asked, off_menu_purchased)
- Plot Essential unlock (3 pre-event purchases) swaps in the Greeting Card, enables the Off-Menu Card Back flip, and applies the protagonist discount

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Stew Simmer loop (2.4s) | Stew bubbling (comforting) | Bubble break on frame 3, every cycle |
| Hot station idle | Food sizzling (appetizing) | Continuous while location loaded |
| Serving Handoff | Food served sound | On the handoff frame |
| Suggestion Sparkle, first cycle | Recommendation "ping" | On Sparkle Frame 1 |
| Knowing Smile peak | Deirdre's knowing "hmm" | Exactly at smile peak, every time |
| Menu panel slide-in landing | Mysterious chime | On the landing frame |
| Meta-Moment Wobble (0.9s) | Fourth-wall sound effect | Spans the full wobble |
| Deirdre idle | Deirdre's humming (pleasant) | Loops under everything; note glyphs optional |
| Approach before major event | Music swells slightly more triumphant | On player entering cart radius while an event flag is active |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Deirdre Mystery | Portrait Cryptic, Knowing Smile, Mysterious Chime Glyph, Fourth-Wall Ripple | Every "how do you know" attempt logs a non-answer; quest is permanently, deliberately inconclusive |
| Perfect Timing | Plot Protected icon, Serving Handoff, situational item sprites | Survive 5 events after buying her food — Plot Protected icon tracks each one |
| The Protagonist's Journey | Plot Essential Badge, Greeting Card, Off-Menu Card Back flip, all 4 off-menu items | Achieve Plot Essential status; off-menu tier unlocks with the badge ceremony |
| Don't Question It | Suggestion Highlight, Suggestion Sparkle, Deirdre's Suggestion icon | Accept 10 recommendations without asking how she knew; asking resets nothing but she notices |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Stoutworks Brewery | Boss-Gate Adjacency Tile before the dungeon entrance; Liquid Fortitude Stew swap panel active | Cart appears before the dungeon; "Big day ahead? You'll want something substantial." |
| The Quiet Man | Cart placement before the champion fight; Pre-Fight Fuel swap panel active | "You look like you're about to test something. Physically." |
| Paddy's Book | Cart present after major losses; The Second Wind swap panel active | Warm glow reads as recovery beacon post-defeat; "Rough time? This'll help." |
| Main Quest Milestones | Always present; The Protagonist's Portion panel + triumphant audio swell | "This is the big one." The cart is simply there. It is always there. |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Narrative convenience rendered as hearth-light — the warmest thing on Cobblestone Market Street, and nobody asks why"
- **Color Mood:** Hearth Orange and Warm Cream glowing against Market Mist Gray; Hero Gold reserved for the moments the game is being honest about what this cart is; Meta Violet appears only when the fourth wall thins
- **Lighting:** The cart is its own light source — lanterns, string bunting, case glow — surrounded by cool Publandia mist; night state deepens the contrast rather than dimming the warmth
- **Texture:** Well-loved wood, chalk dust, steam sheen, clean apron cotton — everything cared for, nothing weathered; this cart has no history because it has always been exactly here

### Environmental Storytelling:
- The signage escalates the joke top to bottom: proud main sign, sincere subtitle, threatening banner, heroic side sign, deflating asterisk, and a chalkboard that simply tells the truth
- The menu board's rails and blank chalk panel imply the board is prepared for futures the player hasn't reached yet
- Locals stream past without a glance while every protagonist-shaped customer stops — the crowd itself is the meta gag
- Irish comfort food as HP restoration, played completely straight: the stew is genuinely good, and that sincerity is what makes the meta-awareness land

### Character Integration Notes:
- Deirdre carries the location on four states and four portraits — warmth first, knowing second, cryptic only on direct questioning; she must never wink at the camera
- The Knowing Smile is a two-pixel change. Restraint IS the joke
- Customer NPCs are a Greek chorus: suspicion, faith, exclusion, gratitude — the four responses to plot armor

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Full Signage Stack** - "Main Characters Eat Free* (*They Don't, But It Sounded Heroic)" above "We Know You're About to Do Something Stupid" — one frame, whole location
2. **The Menu Board Mid-Swap** - Catching The Protagonist's Portion panel sliding in before the game announces the milestone — proof the board knows
3. **The Knowing Smile + Chime Glyph** - Deirdre's two-pixel smile with the violet chime star — the warmest jump-scare in the game
4. **The Chalkboard** - "TODAY'S SPECIAL: Whatever You Need Right Now" — infinitely screenshotable, always true
5. **Locals Walking Past** - The cart glowing like a hearth while every local NPC files by without seeing it
6. **The Fourth-Wall Wobble** - The screen-corner shiver on "I've seen it." — clip-length perfection

### Quote Potential:
- "Main characters don't skip meals. It's bad for the narrative."
- "Eat your sausage roll, dear."
- "You're not ready. Eat this. Now you're ready."
- "Don't worry about how I knew you'd be here. Just eat."
- "Take the Fortitude Stew. You'll thank me later. Or you won't be able to, if you don't."
- "Am I part of the story? I'm part of YOUR story. That's all that matters."
- "The cart goes where it's needed. I follow the cart. The cart knows."

---

## 📋 Required PNG Files (6 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | plot_armor_cart.png | 512x384 |
| 2 | provisions_stations.png | 512x256 |
| 3 | deirdre_murphy.png | 384x256 |
| 4 | provision_customers.png | 256x256 |
| 5 | provisions_items.png | 256x128 |
| 6 | provisions_ui_fx.png | 256x256 |

**Total Estimated Memory:** ~11 MB runtime (atlased with mipmaps, VRAM-compressed — comfortably inside the location's 25 MB budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `plot_armor_cart.png` (512x384)
- [ ] `provisions_stations.png` (512x256)
- [ ] `deirdre_murphy.png` (384x256)
- [ ] `provision_customers.png` (256x256)
- [ ] `provisions_items.png` (256x128)
- [ ] `provisions_ui_fx.png` (256x256)
- [ ] `provisions_accessibility.png` (256x192, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (chalkboard text, menu swap panels, and all signage lettering on separate layers — the board is designed to change)
- **Documentation:** Animation timing reference sheet (2.4s stew loop, 1.0s panel swap, knowing-smile beat curve, 0.9s wobble)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Hearth Orange #FF7F50, Hero Gold #FFD700, Market Mist Gray #B0C4DE, Meta Violet #9370DB)
- [ ] The "Main Characters Eat Free*" asterisk fine print is legible on examine and invisible-ish at street scale — the joke has two reads
- [ ] All eight menu swap panels seat cleanly into the board frame rails; the adaptive swap must look mechanical, not magical
- [ ] Deirdre's Knowing Smile differs from Warm Default by eyes only — if the smile is broad, redo it
- [ ] Warm glow reads as safety against the Cobblestone Market Street mist at gameplay zoom
- [ ] Accessibility visual alternatives included for all audio cues (bubbling, served, ping, hmm, chime, fourth-wall effect)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (meta-awareness played completely sincere) is clear throughout all assets
- [ ] Hidden interactions discoverable: asterisk fine print, blank chalk panel, Off-Menu Card Back, locals-not-noticing gag, Hidden Bonus Star
- [ ] Performance optimized (CPU particles, 12-particle cap, sprite-region menu swaps, single NPC focus)
- [ ] Touch zone sizing considered (44px minimum — menu rows, Confirm/Decline, status icons, examine hotspots compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (silhouette-distinct status icons, shape-coded item tiers, ring + sparkle + badge suggestion marking)
- [ ] Social media viral potential maximized (signage stack framing, mid-swap board capture, knowing-smile composition)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia only — Cobblestone Market Street, Stoutworks, The Quiet Man, Paddy's Book |
| Cultural Specificity | ✅ | Irish comfort food as HP restoration; stew, pasties, Full Irish, maternal vendor archetype |
| Satirical Targets Appropriate | ✅ | Punches at RPG vendor placement, game food mechanics, and plot armor tropes — affectionate parody of game design, not of the Irish |
| Seedy Underbelly Present | ❌ | Profile states Primary Vice: None — Deirdre is genuinely helpful. The location's edge is meta-unease (she knows things she shouldn't, locals can't see the cart, nobody questions it), not vice or exploitation. Intentional outlier, honestly flagged. |
| Gameplay Value Established | ✅ | Major HP restoration, adaptive shop, suggestion bonus, Plot Essential progression, 4 quests, 7 achievements |
| Technical Feasibility | ✅ | Sprite-swap adaptive menu, CPU particles, single always-animated NPC — mobile-safe by design |
| Performance Budget | ✅ | 60 FPS target (45 floor), 10 draw calls, 25 MB cap, 12-particle limit — asset set at ~11 MB |
| Accessibility Features | ✅ | Supplemental sheet: visual cues for all 8 audio events, static-motion variants, high contrast hotspots, 44px targets |
| No Crypto Elements | ✅ | PASS — the only tokens here are edible |
| Social Media Integration | ✅ | Six screenshot moments and seven quotable lines identified |

**Plot Armor Provisions turns the oldest RPG lie — the conveniently placed vendor — into the warmest location in Publandia. Every asset serves the same double read: a genuinely lovely food cart, and a narrative device that is fully aware it's a narrative device. The signage confesses, the menu board predicts, the locals don't see it, and Deirdre smiles two pixels wider because she's already read your save file. When these PNGs land, the player gets fed, healed, protected, and gently unsettled in a single transaction — and comes back before every boss fight anyway, exactly as she knew they would.**

**"Eat your sausage roll, dear."**
