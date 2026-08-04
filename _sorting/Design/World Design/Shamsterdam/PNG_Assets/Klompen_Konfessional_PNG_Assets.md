# Klompen Konfessional - Complete PNG Asset Requirements

## 📋 Overview
Klompen Konfessional is the tourist-district clog shop where every purchase is an implicit confession: these wooden shoes are going on a shelf, and everyone — staff, tourists, the crying child in the baby clogs — knows it. This document specifies every PNG asset for the shop: the aggressively Dutch clog-covered exterior, the Clog Cathedral interior with its four retail sections, the try-on station where dreams of wearing clogs die, Pieter's genuine craft demonstration, Hendrika and Jeroen, the customer gallery, the full try-on/walking-attempt animation suite, and the confession-mechanic UI. Its satirical essence in a sentence: 40 Sovs of authentic craftsmanship, purchased as footwear, destined for a wall.

**Location ID:** `shamsterdam_tourist_klompen_konfessional_01`
**Theme:** Souvenir purchasing as ritual — buying symbols, not objects; the elaborate pretense that clogs are "footwear"
**Zone:** Tourist shopping district, between cheese shop and tulip seller
**Hours:** 9 AM - 8 PM (tourist shopping hours)
**Primary Function:** Souvenir shop / blister prevention center — browsing system across four sections, try-on experience, 10-step walking attempt, confession mechanic at checkout, Clog Burden inventory item, craftsman demonstration cycle

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Natural Wood | #DEB887 | Clogs, shelving, shavings |
| Delft Blue | #1E90FF | Painted clogs, premium display |
| Dutch Orange | #FF6600 | Signage, price tags, tourist bait |
| Traditional Red | #B22222 | Painted accents, blister warnings |
| Windmill White | #FAF3E0 | Painted clog motifs, wall backing |
| Shaving Cream Tan | #E8D5A8 | Fresh wood shavings, demonstration dust |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/klompen_konfessional/
├── environment/
│   ├── klompen_interior_main.png
│   ├── klompen_exterior_display.png
│   └── klompen_sections_stations.png
├── objects/
│   └── klompen_item_sprites.png
├── npcs/
│   ├── npc_klompen_staff.png
│   └── npc_klompen_customers.png
├── effects/
│   └── klompen_animations.png
└── ui/
    └── klompen_ui.png
```

---

## 🏪 Sprite Sheet 1: Interior Main Background — The Clog Cathedral
**File:** `klompen_interior_main.png`
**Dimensions:** 1920x1080 pixels (standalone full-scene background — not atlased)
**Color Palette:** #DEB887, #FAF3E0, #FF6600

### Scene Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Interior Backdrop | (0, 0) | 1920x1080 | Full scene: floor-to-ceiling clog displays, clogs hanging from ceiling, pyramid stacks, four section zones (traditional left, artistic center-left, "wearable" center-right, miniatures right), try-on station front-right, demonstration area rear, checkout counter front-left — overwhelming by design |

### Technical Notes:
- Anchor points (document in layer names): try-on station at (1344, 640), demonstration area at (896, 192), checkout at (192, 704), miniatures at (1600, 384)
- Ceiling clog clusters painted into backdrop; only the swaying cluster overlay (Sheet 7) animates
- Section signage areas left clean for overlay signs (Sheet 3) so sections can be highlighted during browsing

---

## 🪵 Sprite Sheet 2: Exterior & The Wall of Clogs
**File:** `klompen_exterior_display.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #DEB887, #FF6600, #1E90FF

### Exterior & Master Displays:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Storefront Exterior | (0, 0) | 384x384 | Clog-covered facade, giant decorative window clogs, "KLOMPEN KONFESSIONAL" traditional lettering |
| Clog Wall Display | (384, 0) | 512x384 | Floor-to-ceiling interior wall unit, every size and color, the entry spectacle |
| Hanging Clog Cluster | (896, 0) | 128x128 | Ceiling-hung bundle, sway-animation target |
| Pyramid Stack | (896, 128) | 128x128 | Freestanding clog pyramid, one nudge from disaster |
| Honest Addition Sign | (896, 256) | 128x64 | "Perfect for: Walls, Shelves, Gardens, Literally Anywhere But Your Feet" |
| Made-In Sign | (896, 320) | 128x64 | "AUTHENTIC HANDCRAFTED CLOGS — MADE IN [smaller] various locations" |
| Size Range Display | (0, 384) | 384x128 | EU 20 (baby) to EU 50 (concerning), ascending dramatic order |
| Window Display Giant Clog | (384, 384) | 192x128 | Boat-sized painted masterpiece, exterior showpiece |
| Tagline Sign | (576, 384) | 192x64 | "Traditional Dutch Footwear — Since Forever" |
| Truth Subtitle Sign | (576, 448) | 192x64 | "Also Available: The Truth About What You'll Do With These" |
| Wood Shavings Scent Vent | (768, 384) | 64x64 | The piped-in atmosphere source, visible gag for observant players |
| Doorbell Clog | (832, 384) | 64x64 | A clog on a string; it clonks |

### Technical Notes:
- Clog Wall Display renders as a mid-layer over the interior backdrop at the left wall anchor
- Hanging cluster and pyramid are separate so the cluster can sway and the pyramid can wobble on interaction
- All signage drawn at readable resolution — the honest signs are the location's thesis

---

## 🗄️ Sprite Sheet 3: Sections & Stations
**File:** `klompen_sections_stations.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #DEB887, #1E90FF, #B22222

### Retail Sections:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Traditional Section | (0, 0) | 384x256 | Natural wood classics, "as worn by Dutch farmers (in the 1800s)", 25 Sovs-40 shelf tags |
| Artistic Section | (384, 0) | 384x256 | Hand-painted windmills, tulips, Delft blue — clearly decorations, 35 Sovs-60 |
| "Wearable" Section (Allegedly) | (768, 0) | 256x256 | Rubber soles, padding inserts, suspiciously small shelf, 50 Sovs-80; staff maintain straight faces |
| Miniatures Section | (0, 256) | 256x192 | Keychains, magnets, tiny clogs — the honest purchase, best-seller by volume |
| Try-On Station | (256, 256) | 256x256 | Bench, sizing guide, mirror, discreetly positioned first aid kit |
| Demonstration Area | (512, 256) | 384x256 | Pieter's workspace: shaving horse, blades, half-carved blanks, 400 years of technique |

### Station Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Checkout Counter | (0, 512) | 256x192 | Where the confession happens; bag rack behind |
| Try-On Mirror | (256, 512) | 96x160 | Full-effect viewing, slightly merciless |
| Try-On Bench | (352, 512) | 128x64 | Seat of decisions |
| First Aid Kit (Discreet) | (352, 576) | 64x64 | Not technically required, absolutely stocked |
| Sizing Guide Chart | (416, 512) | 96x128 | EU sizing; irrelevant, they're going on a shelf |
| Craftsman Tool Rack | (512, 512) | 128x64 | Real tools, real technique |
| Wood Shavings Pile | (640, 512) | 64x32 | Fresh from the last demonstration |
| Half-Carved Clog Blank | (704, 512) | 64x48 | Poplar, mid-transformation |
| Section Sign Set | (0, 704) | 384x64 | Four 96x64 overlay signs: TRADITIONAL / ARTISTIC / "WEARABLE" / MINIATURES |
| Shopping Bag Rack | (384, 704) | 128x96 | Branded bags awaiting wooden cargo |
| Confession Plaque | (512, 704) | 192x64 | "Admit It. These Are Going On A Shelf." — checkout-counter brass |

### Technical Notes:
- Sections are interactable browse zones; overlay signs brighten on focus
- "Wearable" section drawn narrower than the others — the shelf size IS the joke
- First aid kit is a hidden-detail interactable (+Appreciation dialogue from Jeroen)

---

## 👡 Sprite Sheet 4: Clog Items & Inventory
**File:** `klompen_item_sprites.png`
**Dimensions:** 256x256 pixels
**Color Palette:** #DEB887, #1E90FF, #B22222, #FAF3E0

### Product Inventory:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Traditional Natural Clog | (0, 0) | 64x48 | Classic pair, 25 Sovs, shelf-bound (94%) |
| Hand-Painted Windmill Clog | (64, 0) | 64x48 | Tourist favorite, 45 Sovs, wall mount (89%) |
| Canal Blue Decorative | (128, 0) | 64x48 | Delft premium, 55 Sovs, curio cabinet (91%) |
| "Comfort" Modified Clog | (192, 0) | 64x48 | Alleged wearability, 65 Sovs, one wearing then shelf (88%) |
| Garden Clog (Rubber) | (0, 48) | 64x48 | Actually practical, 35 Sovs, real garden use (40%) |
| Baby Clog Pair | (64, 48) | 32x24 | Photo prop → storage (97%) |
| Giant Display Clog | (96, 48) | 96x72 | 80 Sovs statement piece, wearability impossible |
| Clog Painting Kit | (192, 48) | 48x48 | 30 Sovs activity, never completed (85%) |
| Miniature Keychain | (0, 96) | 24x24 | 8 Sovs — finally honest |
| Miniature Magnet | (24, 96) | 24x24 | 5 Sovs — fridge-ready honesty |
| Shopping Bag (Loaded) | (48, 96) | 48x64 | Heavy, wooden contents, visibly straining |
| Clog Burden Inventory Icon | (96, 120) | 32x32 | Equipment icon; -50% movement if actually equipped |
| Blister Status Icon | (128, 120) | 32x32 | Try-on consequence marker |
| Honest Purchase Icon | (160, 120) | 32x32 | Miniature-only checkout marker |
| Equipped Clogs (Feet Overlay) | (0, 160) | 64x32 | Player-feet overlay for the Masochist achievement |
| Clog On Shelf (Epilogue Prop) | (64, 160) | 64x48 | "The clogs are on a shelf. They've always been on a shelf." |
| Price Tag Set | (128, 160) | 96x32 | Three 32x32 orange tags lettered `S`, `SS`, `SSS` — the game-wide cheap / mid / expensive tier marks. **No currency glyph exists; these are Sov-tier block capitals, not a symbol.** Three caps fit 32x32 at ~8px wide each. |

### Technical Notes:
- Full-size clogs share a 64x48 silhouette so section shelves can tile them efficiently
- Shopping Bag (Loaded) has weight-strain lines — wooden shoes are DENSE
- Equipped Clogs overlay pairs with the -50% movement debuff state

---

## 👥 Sprite Sheet 5: Shop Staff
**File:** `npc_klompen_staff.png`
**Dimensions:** 512x384 pixels
**Sprite Size:** 64x96 per frame
**Color Palette:** #DEB887, #FAF3E0, traditional dress accents

### Proprietor Hendrika:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hendrika Idle | (0, 0) | 64x96 | Traditional dress (for tourists), practical shoes (for reality) |
| Hendrika Presenting Frame 1 | (64, 0) | 64x96 | Clog showcase gesture, warm professionalism |
| Hendrika Presenting Frame 2 | (128, 0) | 64x96 | Turning the clog to catch the light |
| Hendrika Diplomatic Pause | (192, 0) | 64x96 | Asked directly if people wear them: the honest beat |
| Hendrika Confession Warmth | (256, 0) | 64x96 | "For display? Wonderful. That's also a tradition now." |
| Hendrika Portrait (Dialogue) | (384, 0) | 128x128 | Close-up: sells the tradition, knows the reality, respects both |

### Craftsman Pieter:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pieter Idle | (0, 96) | 64x96 | Wood shavings in beard, genuine craftsman energy |
| Pieter Carving Frame 1 | (64, 96) | 64x96 | Blade set against poplar blank |
| Pieter Carving Frame 2 | (128, 96) | 64x96 | Long stroke, shavings curl |
| Pieter Carving Frame 3 | (192, 96) | 64x96 | Turning the blank, appraising |
| Pieter Carving Frame 4 | (256, 96) | 64x96 | Detail cut — "the wood remembers" |
| Pieter Philosophical | (320, 96) | 64x96 | "The shape hasn't changed. The purpose has. That's not the clog's fault." |
| Pieter Portrait (Dialogue) | (384, 128) | 128x128 | Close-up: pride of craft, awareness of context |

### Associate Jeroen:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Jeroen Idle | (0, 192) | 64x96 | Suspiciously comfortable regular shoes, patient expression |
| Jeroen Fetching Size | (64, 192) | 64x96 | "Let me get you... okay, try these." |
| Jeroen Watching Try-On | (128, 192) | 64x96 | Has seen the 10-step walk many times |
| Jeroen Gentle Aftermath | (192, 192) | 64x96 | "So... display? That's great. They display really well." |
| Jeroen Miniature Approval | (256, 192) | 64x96 | "Miniatures? Excellent choice. Very... honest." |
| Jeroen Portrait (Dialogue) | (320, 192) | 128x128 | Close-up: summer job turned career turned clog philosophy |

### Technical Notes:
- Hendrika's practical shoes must be visible in every frame — the quiet punchline of her design
- Pieter's carving loop syncs with wood shaving particles (Sheet 7) and rhythmic carving audio
- Jeroen's frames deliberately underplay — his comedy is patience

---

## 🧳 Sprite Sheet 6: Customer Gallery
**File:** `npc_klompen_customers.png`
**Dimensions:** 512x256 pixels
**Sprite Size:** 64x96 per single NPC frame (Child Victim 48x72)
**Color Palette:** Mixed tourist palette over wood tones

### Atmospheric Customers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Committed Tourist | (0, 0) | 64x96 | Determination visible: "I'm going to wear these EVERY DAY. At HOME." |
| Committed Tourist Lapping | (64, 0) | 64x96 | Walking laps in clogs, ignoring pain |
| Honest Tourist | (128, 0) | 64x96 | Straight to miniatures, unbothered, experienced |
| Child Victim | (192, 0) | 48x72 | Crying in "cute" baby clogs: "THEY'RE MADE OF WOOD." |
| Parent (Oblivious) | (240, 0) | 64x96 | Photographing the crying child fondly |
| Return Customer | (304, 0) | 64x96 | Back with clogs, seeking padding, hope against evidence |
| Photographer Tourist | (368, 0) | 64x96 | Holding clogs up for the SHOT, never wearing |
| Photographer Posing Clogs | (432, 0) | 64x96 | Arranging clogs in a scenic composition |
| Browsing Poses Strip | (0, 96) | 256x96 | Four 64x96 universal poses: shelf-scan / pick-up / examine / price-wince |
| Try-On Queue Filler | (256, 96) | 64x96 | Waiting for the bench, apprehension building |
| Confession Line Filler | (320, 96) | 64x96 | Checkout queue body, bag in hand |
| Child Victim Portrait | (384, 96) | 128x128 | Close-up: the only honest face in the shop |

### Technical Notes:
- Browsing poses are palette-modulated to multiply apparent shop population
- Child Victim renders at 48x72 with parent adjacency rule — always paired
- Return Customer carries the same Shopping Bag (Loaded) sprite from Sheet 4

---

## 🎬 Sprite Sheet 7: Try-On & Walking Animations
**File:** `klompen_animations.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** Player palette + #DEB887 clogs, #B22222 pain accents

### The Try-On Experience:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Try-On Frame 1 — The Insertion | (0, 0) | 256x192 | Foot enters clog; immediate wooden reality |
| Try-On Frame 2 — The Standing | (256, 0) | 256x192 | Upright, wobble begins |
| Try-On Frame 3 — The Wobble | (512, 0) | 256x192 | Balance negotiation, arms deploying |
| Try-On Frame 4 — The Realization | (768, 0) | 256x192 | Face says everything; mirror confirms |

### The Walking Attempt (Steps 1-10):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Walk Frames 1-6 | (0, 192) | 384x96 | Six 64x96 frames: steps 1-3 "this is fine" → steps 4-6 "adjustment needed" → 7-9 "I think I'm bleeding" → step 10 resolve |
| Clog Selection Frames | (384, 192) | 384x96 | Three 128x96 frames: browse → examine → choose |
| Confession Moment Frames | (768, 192) | 256x96 | Two 128x96 frames: truth ("...decoration") or delusion ("Wearing, definitely") |
| Pain Stars Burst | (0, 288) | 32x32 | Comic pain indicator for steps 7+ |
| Wobble Lines | (32, 288) | 64x64 | Balance-loss marks for try-on frames 2-3 |
| Wood Shaving Curl Particles | (96, 288) | 64x32 | Two 32x32 shaving sprites for Pieter's demonstration |
| Dust Motes | (160, 288) | 32x32 | Warm-light atmosphere particle |
| Ceiling Cluster Sway Frames | (192, 288) | 256x128 | Two 128x128 frames of the hanging clog cluster gently swaying |
| Pyramid Wobble Frame | (448, 288) | 128x128 | Nudged-pyramid tension frame (never falls; the tension is eternal) |
| Blister Formation Close-Up | (576, 288) | 96x96 | Educational agony inset for step 9 |
| Removal Relief Pose | (672, 288) | 64x96 | Clogs off, socks reunited with mercy |

### Technical Notes:
- Walk frames tie to the 10-step counter; frame advance is step-driven, not time-driven
- Pain stars begin at step 7; density increases per step
- Confession frames are the checkout cinematic — camera pushes in slightly (code-side)

---

## 🧭 Sprite Sheet 8: UI Elements
**File:** `klompen_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #FF6600 UI chrome, #DEB887 panels, #B22222 warnings

### Interface Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Clog Browser Panel | (0, 0) | 256x192 | Category selection: Traditional / Artistic / "Wearable" / Miniatures |
| Size Selection Chart | (256, 0) | 192x128 | EU 20-50 picker; footnote: "size is irrelevant to shelves" |
| Try-On Prompt | (256, 128) | 128x64 | "Try them on? (Recommended: few steps)" — invitation to suffer |
| Step Counter | (384, 128) | 96x64 | 1-10 step tracker with escalating tint |
| Blister Warning | (256, 192) | 96x32 | Walk consequence alert |
| Confession Dialogue Panel | (0, 192) | 256x128 | "Will you be wearing these, or are they for display?" — four response options |
| Honest Customer Badge | (352, 192) | 64x64 | Confession achieved; staff respect +10 |
| Achievement Badges Strip | (0, 320) | 320x64 | Five 64x64 badges: Realist / Optimist / Believer / Masochist / Confessed |
| Clog Burden Equip Card | (320, 320) | 128x96 | -50% movement, +Blister; "technically equipment" |
| Demonstration Watch Prompt | (0, 384) | 128x64 | "Watch closely. This technique is 400 years old." |
| Appreciation Buff Icon | (128, 384) | 32x32 | +Appreciation for craft (wearability assessment unchanged) |
| Purchase Receipt Panel | (160, 384) | 192x128 | Itemized truth: item, price, probable fate percentage |
| Miniature Wisdom Icon | (352, 384) | 32x32 | Keychain glyph — wisdom gained marker |
| Bag Weight Indicator | (384, 384) | 96x32 | Inventory heaviness readout; wood is dense |

### Technical Notes:
- Confession options each render at 44px+ touch height; option 4 ("...decoration") slightly highlighted after a beat
- Receipt panel prints the profile's fate statistics (shelf 94%, wall 89%, etc.) as flavor data
- Badges grayscale until earned (modulate, not separate art)

---

## 🎬 Animation Specifications

### Pieter's Carving Demonstration (Sheet 5):
- **Duration:** 4.0 seconds per cycle (1.0s per frame), 5-minute in-world demonstration loop
- **Frames:** 4
- **Pattern:** Blade set → stroke → appraise → detail cut → loop
- **Trigger:** Hourly during peak tourist times; always when player approaches demonstration area
- **Purpose:** Genuine craft, genuinely impressive — the legitimacy engine of the whole shop
- **Audio Sync:** Rhythmic carving stroke on frame 2 start (1.0s); shaving-fall whisper on frame 3
- **Mobile Optimization:** Static demonstration option per profile (single appraise frame + audio)

### The Try-On Sequence (Sheet 7):
- **Duration:** 4.8 seconds (1.2s per frame)
- **Frames:** 4
- **Pattern:** Insertion → standing → wobble → realization; holds on frame 4 pending player choice
- **Trigger:** Player accepts Try-On Prompt at the station
- **Purpose:** The moment dreams of wearing clogs die, rendered with dignity
- **Audio Sync:** Hollow wooden CLONK at 0.0s insertion; creak at 1.2s stand; ominous try-on-area silence otherwise (profile audio note)
- **Mobile Optimization:** None needed (one-shot)

### The Walking Attempt (Sheet 7):
- **Duration:** Step-driven; ~0.8s per step at normal tap cadence, 10 steps maximum
- **Frames:** 6 pose frames mapped across 10 steps + pain stars from step 7
- **Pattern:** Frame advance per step tap; abort available any step (removal relief pose)
- **Trigger:** Player chooses to walk after try-on
- **Purpose:** The 10-step test — Bravado on completion, honesty on retreat
- **Audio Sync:** Distinctive wood-on-floor CLOK per step; subtle pain sting at steps 7 and 9
- **Mobile Optimization:** Pain star density capped at 3 concurrent on Low LOD

### Ceiling Cluster Sway (Sheet 7):
- **Duration:** 3.0 seconds per sway cycle
- **Frames:** 2
- **Pattern:** Continuous gentle alternation
- **Trigger:** Constant; amplitude doubles briefly when door opens
- **Purpose:** The shop breathes wood
- **Audio Sync:** Soft clog-on-clog clack on direction change (every 1.5s, quiet)
- **Mobile Optimization:** Static on Low LOD and in reduced-motion mode

### Hendrika Presenting (Sheet 5):
- **Duration:** 1.6 seconds (0.8s per frame)
- **Frames:** 2
- **Pattern:** Showcase → light-catch turn → hold
- **Trigger:** Player examines any full-size clog
- **Purpose:** Retail theater with complete professionalism
- **Audio Sync:** Gentle "presentation" chime on frame 2
- **Mobile Optimization:** None needed

### Confession Moment (Sheet 7):
- **Duration:** 2.0 seconds (1.0s per frame + UI hold)
- **Frames:** 2
- **Pattern:** Question pose → resolution pose (truth or delusion variant framing)
- **Trigger:** Checkout with any full-size clog
- **Purpose:** The location's namesake mechanic
- **Audio Sync:** Slight confession acknowledgment tone ONLY on honest answers (profile: audio acknowledgment when truth is spoken)
- **Mobile Optimization:** None needed

### Pyramid Wobble (Sheet 7):
- **Duration:** 0.6 seconds, plays once per nudge
- **Frames:** 2 (base + wobble)
- **Pattern:** Wobble → settle; never falls
- **Trigger:** Player walks within 16px of pyramid
- **Purpose:** Perpetual near-disaster tension gag
- **Audio Sync:** Wooden rattle, cut short
- **Mobile Optimization:** Disabled on Low LOD

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Try-On Station Outline | (768, 288) | 64x64 | Bold outline marker for the try-on interactable (Sheet 7 reserve block) |
| Section Boundary Outlines | (832, 288) | 128x64 | High-contrast section divider overlays for the four retail zones (Sheet 7 reserve block) |
| Checkout Marker | (960, 288) | 64x64 | Bold confession-point outline (Sheet 7 reserve block) |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Ceiling Cluster | Sheet 7 (Sway frame 1) | 128x128 | Reduced-motion locks the hanging clogs still |
| Static Demonstration | Sheet 5 (Pieter Carving Frame 3) | 64x96 | Appraise pose replaces the carving loop |
| No-Wobble Try-On | Sheet 7 (Try-On Frame 2) | 256x192 | Wobble frame skipped; standing holds directly to realization |
| Capped Pain Stars | Sheet 7 (Pain Stars) | 32x32 | Single static star replaces burst accumulation |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wood CLONK Marker | (768, 352) | 24x24 | Clog-impact glyph per walking step, mirrors step audio (Sheet 7 reserve block) |
| Carving Rhythm Tick | (792, 352) | 24x24 | Metronome glyph over Pieter during strokes |
| Confession Tone Marker | (816, 352) | 24x24 | Soft halo glyph on honest checkout answers |
| Doorbell Clog Marker | (840, 352) | 24x24 | Clonk glyph at entrance on door events |

### Colorblind Considerations:
- Section identity coded by sign text + shelf silhouette (natural/painted/padded/tiny), never wood-tone alone
- Step Counter escalation uses fill segments + numerals, not red gradient alone
- Blister warning pairs #B22222 with a bandage-cross glyph
- Touch zones minimum 44px for browser categories, try-on prompt, step taps, and confession options

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (fallback PVRTC 4BPP); signage set and receipt panel at ASTC 4x4 (readable text)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for klompen_interior_main.png (scene-detail critical) and honest signage

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| klompen_environment | klompen_exterior_display, klompen_sections_stations | 2048x2048 |
| klompen_characters | npc_klompen_staff, npc_klompen_customers | 1024x1024 |
| klompen_fx_ui | klompen_item_sprites, klompen_animations, klompen_ui | 2048x1024 |

*(klompen_interior_main.png loads standalone as a scene background; max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full carving loop, cluster sway, pyramid wobble, shaving particles, dust motes |
| Medium | Carving at 2 keyframes, sway retained, no pyramid wobble, half particles |
| Low | Static demonstration and cluster (profile: simplified clog variety, static demonstration), no particles |

### Performance Targets:
- **Target FPS:** 60 (per location performance budget)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 32 MB maximum
- **Particle Limit:** 10 (wood shavings, dust motes)

### Performance Notes:
- Clog variety achieved by palette modulation over shared 64x48 silhouettes (profile: simplified clog variety)
- Browsing poses reused across customer sprites via modulate
- Try-on and walk sequences are one-shots; no persistent overlays beyond blister status icon

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (interior background), AnimatedSprite2D (staff, try-on, walk), CPUParticles2D (shavings, dust — not GPU), CanvasLayer (browser/confession UI), Area2D (section zones, pyramid proximity, try-on bench)
- Special systems: 10-step walk counter with per-step audio/pain escalation, confession response tracker (4 options; option 4 unlocks Honest Customer), Clog Burden inventory weight + equip debuff (-50% movement, +Blister), demonstration hourly scheduler, fate-statistics receipt printer

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Try-On Frame 1 | Hollow wooden CLONK | 0.0s of insertion |
| Walk step frames | Wood-on-floor CLOK | Per step tap |
| Walk steps 7 & 9 | Subtle pain sting | On step registration |
| Pieter Carving Frame 2 | Rhythmic carving stroke | 1.0s into cycle |
| Cluster sway direction change | Quiet clog-on-clog clack | Every 1.5s |
| Honest confession option | Acknowledgment tone | On selection |
| Doorbell Clog | Entrance clonk | On shop entry/exit |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Clog Achievement Track — "Realist" | Miniature sprites, Miniature Wisdom icon | Miniatures-only purchase |
| "Optimist" / "Believer" | Full-size clog sprites, walk frames, step counter | Full-size purchase / 10 steps completed |
| "Masochist" | Equipped Clogs overlay, Clog Burden card | Equipped during combat (technically possible) |
| "Confessed" | Confession frames, Honest Customer badge | Admitted decoration purpose at checkout |
| Craftsman Appreciation | Pieter carving frames, Appreciation buff icon | Watch full demonstration cycle |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| De Botanische Leugen | Shared "buying the dream" receipt styling | Souvenir psychology dialogue crosslinks |
| Cheese Shop (tourist corridor) | Adjacent storefront edge in exterior art | Same-energy shopping corridor continuity |
| Tulip Seller (tourist corridor) | Opposing storefront glimpse | Same customers, same delusion, different plant |
| Bicycle Warfare routes | Clog Burden movement debuff | Contrast gag: accessories might help, clogs definitely won't |
| The Tolerance Hostel | Shopping Bag (Loaded) prop reference | Other travelers judge the clog purchase in kitchen scenes |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A cathedral of sincere craftsmanship serving a completely insincere transaction"
- **Color Mood:** Warm natural wood everywhere, punctuated by Delft blue and Dutch orange — cozy, golden, faintly absurd in volume
- **Lighting:** Warm wood-enhancing wash, spotlights on painted showpieces, bright honest light over the demonstration, ominously neutral light at the try-on station
- **Texture:** Smooth carved poplar, hand-painted gloss, fresh shaving curls, the faint shine of shelves that hold everything and support nothing

### Environmental Storytelling:
- The miniatures section outsells everything — its worn floor patch and depleted racks say so
- The "wearable" section's smallness is a confession the shop makes about itself
- The first aid kit at the try-on station is visible only to those who look — mercy, discreetly positioned
- Pieter's genuine workspace amid the souvenir flood: the real tradition, still alive, watching its own gift shop

### Character Integration Notes:
- Hendrika anchors checkout; her traditional dress vs. practical shoes contradiction must read at sprite scale
- Pieter never leaves the demonstration area — craft is stationary, commerce circulates
- Jeroen floats between try-on and shelves, the shop's shock absorber
- Child Victim + oblivious parent are a paired unit; children speak truth adults avoid

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The 10-Step Walk** — step 8 face, pain stars deployed, mirror witnessing
2. **The Honest Sign** — "Perfect for: Walls, Shelves, Gardens, Literally Anywhere But Your Feet"
3. **The Clog Cathedral Entry** — floor-to-ceiling wooden overwhelm in one frame
4. **The Child Victim** — crying truth in baby clogs while a parent photographs fondly
5. **The Confession Panel** — four options, one honest, everyone knows which

### Quote Potential:
- "Comfortable? They're... traditional. Comfort is modern. These are heritage."
- "The clogs work perfectly. The feet are the problem."
- "Miniatures are honest. Keychains admit they're keychains. Full-size clogs pretend to be shoes."
- "THESE HURT. I DON'T LIKE THEM. THEY'RE MADE OF WOOD."
- "My grandmother wore clogs daily. In fields. On farms. You probably have different floors."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | klompen_interior_main.png | 1920x1080 |
| 2 | klompen_exterior_display.png | 1024x512 |
| 3 | klompen_sections_stations.png | 1024x1024 |
| 4 | klompen_item_sprites.png | 256x256 |
| 5 | npc_klompen_staff.png | 512x384 |
| 6 | npc_klompen_customers.png | 512x256 |
| 7 | klompen_animations.png | 1024x512 |
| 8 | klompen_ui.png | 512x512 |

**Total Estimated Memory:** ~22 MB in-memory (uncompressed RGBA worst case), within the 32 MB location budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `klompen_interior_main.png` (1920x1080)
- [ ] `klompen_exterior_display.png` (1024x512)
- [ ] `klompen_sections_stations.png` (1024x1024)
- [ ] `klompen_item_sprites.png` (256x256)
- [ ] `npc_klompen_staff.png` (512x384)
- [ ] `npc_klompen_customers.png` (512x256)
- [ ] `klompen_animations.png` (1024x512)
- [ ] `klompen_ui.png` (512x512)

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
- **Backup:** Master PSD/layered file with organized layer groups
- **Documentation:** Animation timing reference sheet + 10-step walk state chart

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: honest signage set, the suspiciously small "wearable" section, the discreet first aid kit, Hendrika's practical shoes
- [ ] Accessibility visual alternatives included for all audio cues (wood clonks, carving rhythm, confession tone, doorbell clog)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (tourist purchasing logic satirized; Pieter's craft respected)
- [ ] Hidden areas/interactions have discoverable visual cues (first aid kit, scent vent, pyramid proximity, confession highlight)
- [ ] Mobile performance optimized (CPU particles, palette-modulated clog variety, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for browser, try-on, steps, confession)
- [ ] Colorblind-friendly alternatives available where color codes meaning (section silhouettes, segmented step counter)
- [ ] Social media viral potential maximized in composition choices (step-8 mirror framing, honest signage legibility)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam tourist district; all in-world text city-agnostic or Shamsterdam-branded |
| Cultural Specificity | ✅ | Genuine Dutch klompen craft tradition vs. modern tourist clog economy |
| Satirical Targets Appropriate | ✅ | Souvenir purchasing logic and tourist self-delusion — never the craft or the craftsman |
| Seedy Underbelly Present | ✅ | Selling 40 Sovs wood as "footwear" with try-on theater everyone sees through |
| Gameplay Value Established | ✅ | Try-on system, 10-step challenge, confession mechanic, inventory burden, achievement track |
| Technical Feasibility | ✅ | Palette-modulated variety, static demonstration fallback, one-shot animations documented |
| Mobile Performance Budget | ✅ | 60 FPS, 14 draw calls, 32 MB, 10 particles per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all audio cues, reduced-motion set, 44px touch zones |
| No Crypto Elements | ✅ | Pure wooden authenticity |
| Social Media Integration | ✅ | 5 screenshot moments + 5 quotable lines identified |

**Once these assets ship, Klompen Konfessional becomes the game's gentlest trap: a warm wooden room where players buy exactly what they think they're buying — and confess, at the register, what they'll actually do with it.**
