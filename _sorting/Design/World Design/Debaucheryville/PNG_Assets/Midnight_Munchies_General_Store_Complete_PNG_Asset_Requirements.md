# Midnight Munchies General Store - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Midnight Munchies General Store - late-night survival essentials for those who should have planned ahead, open when everything else is closed, priced accordingly.

**Location ID:** `debaucheryville_shop_midnight_munchies_01`  
**Czech Name:** Půlnoční Mlsání  
**Theme:** Desperation pricing, the 3 AM economy, Věra's judgment-free zone  
**Zone:** Hostel Row, Budget Accommodation District (Debaucheryville) - strategic late-night positioning  
**Hours:** 10 PM - 8 AM ("We Don't Judge Your Timing"; +20% Desperation Tax after 2 AM)  
**Primary Function:** Emergency convenience store, Desperation Tax system, status effect management

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Fluorescent White | #F5F5F5 | Interior lighting, main surfaces |
| Energy Drink Green | #00FF00 | Neon sign, product accents, fresh indicator |
| Late Night Blue | #191970 | Exterior darkness, window backdrop |
| Warning Red | #FF6347 | Desperation Tax alerts, disaster quality indicator |
| Heat Lamp Orange | #FFA500 | Heat lamp glow, rotating food warmth |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/midnight_munchies_general_store/
├── environment/
│   ├── midnight_munchies_exterior.png
│   ├── shop_interior_full.png
│   └── shop_sections_combined.png
├── npcs/
│   ├── vera_novotna.png
│   └── midnight_customers.png
├── objects/
│   ├── heat_lamp_station.png
│   ├── vera_counter.png
│   └── midnight_munchies_items.png
├── effects/
│   └── fluorescent_lighting.png
└── ui/
    └── midnight_munchies_ui.png
```

---

## 🏪 Sprite Sheet 1: Exterior
**File:** `midnight_munchies_exterior.png`  
**Dimensions:** 384x384 pixels  
**Color Palette:** #F5F5F5 (fluorescent white), #00FF00 (energy drink green), #191970 (late night blue)

### Building Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Storefront | (0, 0) | 384x256 | Fluorescent beacon |
| Door Closed | (0, 256) | 64x96 | Entry |
| Door Open | (64, 256) | 64x96 | With chime effect |

### Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Neon On | (128, 256) | 192x48 | "MIDNIGHT MUNCHIES" |
| Neon Flicker | (128, 304) | 192x48 | Glitch state |
| Hours Sign | (320, 256) | 64x48 | "10 PM - 8 AM" |

### Window:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Window Display | (0, 352) | 256x32 | Cluttered necessities |

---

## 🛒 Sprite Sheet 2: Shop Interior
**File:** `shop_interior_full.png`  
**Dimensions:** 512x384 pixels  

### Floor Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Full Interior | (0, 0) | 512x384 | Cramped aisles |
| Healing Aisle | (0, 0) | 128x192 | Section marker |
| Support Aisle | (128, 0) | 128x192 | Section marker |
| Offensive Section | (256, 0) | 128x192 | Section marker |
| Utility Aisle | (384, 0) | 128x192 | Section marker |

---

## 📦 Sprite Sheet 3: Shop Sections Combined
**File:** `shop_sections_combined.png`  
**Dimensions:** 512x384 pixels  

| Section | Position | Size | Description |
|---------|----------|------|-------------|
| Healing Section | (0, 0) | 256x192 | Energy drinks, kebabs, kits |
| Support Section | (256, 0) | 192x192 | Caffeine, chargers, stamps |
| Offensive Section | (0, 192) | 192x192 | Defensive items |
| Utility Section | (192, 192) | 256x192 | Practical survival |

---

## 🔥 Sprite Sheet 4: Heat Lamp Station
**File:** `heat_lamp_station.png`  
**Dimensions:** 192x192 pixels  

### Station Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Station Base | (0, 0) | 192x128 | Rotating food display |
| Lamp Glow | (0, 128) | 64x64 | Orange warmth |

### Rotating Food (32x32 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Frame 1 | (64, 128) | Kebab position |
| Frame 2 | (96, 128) | Rotation |
| Frame 3 | (128, 128) | Rotation |
| Frame 4 | (160, 128) | Full cycle |

### Quality Indicators (24x24 each):
| Quality | Position | Description |
|---------|----------|-------------|
| Fresh | (64, 160) | Green check |
| Questionable | (88, 160) | Yellow warning |
| Disaster | (112, 160) | Red skull |

---

## 💰 Sprite Sheet 5: Věra's Counter
**File:** `vera_counter.png`  
**Dimensions:** 256x192 pixels  

| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Base | (0, 0) | 256x128 | Where transactions happen |
| Lottery Tickets | (0, 128) | 64x32 | Display |
| Cigarettes Display | (64, 128) | 64x32 | Behind counter |
| Register | (128, 128) | 64x64 | Transaction point |

---

## 👵 Sprite Sheet 6: Věra Novotná
**File:** `vera_novotna.png`  
**Dimensions:** 256x192 pixels  

### Character States (64x96 each):
| State | Position | Description |
|-------|----------|-------------|
| Reading Newspaper | (0, 0) | Default idle |
| Looking Up | (64, 0) | Customer acknowledged |
| Transaction 1 | (128, 0) | Processing |
| Transaction 2 | (192, 0) | Bagging |
| Wisdom Moment | (0, 96) | Regular dialogue |
| Rare Care | (64, 96) | Maternal moment |

### Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Reading Glasses | (128, 96) | 24x16 | Essential |
| Cardigan | (152, 96) | 48x48 | Signature outfit |
| Newspaper | (200, 96) | 48x32 | Always present |

**Věra Visual Notes:**
- 60s Czech woman
- Reading glasses, cardigan
- Has seen everything twice
- Professional detachment with occasional maternal moments

---

## 👥 Sprite Sheet 7: Customer NPCs
**File:** `midnight_customers.png`  
**Dimensions:** 320x192 pixels  

### Characters (64x96 each):
| Character | Position | Description |
|-----------|----------|-------------|
| 3 AM Desperate | (0, 0) | NEEDS something NOW |
| Pre-Dawn Philosopher | (64, 0) | Contemplative at 5 AM |
| Hostel Forager | (128, 0) | Calculating budget |
| Hangover Expert | (192, 0) | Strategic shopping |
| Lost Tourist | (256, 0) | Seeking connection |

---

## 🧃 Sprite Sheet 8: Item Sprites
**File:** `midnight_munchies_items.png`  
**Dimensions:** 256x256 pixels  

### Healing Items:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Energy Standard | (0, 0) | 24x32 | Basic energy |
| Energy Premium | (24, 0) | 24x32 | Stronger |
| Energy Extreme | (48, 0) | 24x32 | Last resort |
| Greasy Kebab | (72, 0) | 32x32 | Heat lamp fresh |
| Hair of Dog | (104, 0) | 24x32 | Fight poison |
| Hangover Kit | (128, 0) | 48x32 | Complete recovery |
| Snack Bar | (176, 0) | 32x24 | Blood sugar |
| Instant Noodles | (208, 0) | 32x32 | Self-rescue |

### Support Items:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Caffeine Pills | (0, 32) | 24x24 | Precision |
| Fake Stamp | (24, 32) | 24x24 | Placebo |
| Phone Charger | (48, 32) | 32x24 | Lifeline |
| Cigarettes | (80, 32) | 32x24 | If you must |
| Lighter | (112, 32) | 24x24 | Fire |
| Breath Mints | (136, 32) | 24x24 | Essential |

### Offensive Items:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Pepper Spray | (0, 56) | 24x32 | Protection |
| Personal Alarm | (24, 56) | 24x24 | Sound defense |
| Brass Keychain | (48, 56) | 32x24 | Ambiguous |
| Party Poppers | (80, 56) | 32x32 | Flash grenades |
| Heavy Flashlight | (112, 56) | 24x32 | Multi-purpose |

### Utility Items:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Club Earplugs | (0, 88) | 24x24 | Sound protection |
| Fake Wristband | (24, 88) | 32x16 | Might work |
| Cab Voucher | (56, 88) | 32x24 | Guaranteed escape |
| Wet Wipes | (88, 88) | 32x24 | Don't ask |
| First Aid Kit | (120, 88) | 32x32 | Responsible |
| Condoms | (152, 88) | 32x24 | No judgment |

---

## 🎮 Sprite Sheet 9: UI Elements
**File:** `midnight_munchies_ui.png`  
**Dimensions:** 384x256 pixels  

### Shop Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Product Browser | (0, 0) | 256x192 | Section navigation |
| Desperation Tax Notice | (256, 0) | 128x64 | Price increase alert |
| Price Comparison | (256, 64) | 128x64 | "Could have planned ahead" |
| Heat Lamp Quality | (256, 128) | 128x64 | Freshness indicator |

### Status Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Regular Status Badge | (0, 192) | 64x64 | Věra knows you |
| Hangover Cure Icon | (64, 192) | 32x32 | Status removal |
| Energy Crash Warning | (96, 192) | 64x32 | Incoming crash |
| Věra Wisdom Unlock | (160, 192) | 128x64 | Dialogue available |

---

## 💡 Sprite Sheet 10: Lighting Effects
**File:** `fluorescent_lighting.png`  
**Dimensions:** 512x128 pixels  

| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Full Brightness | (0, 0) | 256x64 | Harsh fluorescent |
| Flicker Dim | (256, 0) | 256x64 | Momentary dim |
| Heat Lamp Glow | (0, 64) | 128x64 | Orange warmth |
| Neon Glow | (128, 64) | 128x64 | Green sign glow |

---

## 🎬 Animation Specifications

### Neon Sign Flicker:
- **Pattern:** On → Flicker → On → On
- **Timing:** Random 5-15 seconds between flickers
- **Flicker Duration:** 0.2 seconds

### Heat Lamp Rotation:
- **Pattern:** Frame 1 → 2 → 3 → 4 (loop)
- **FPS:** 2
- **Purpose:** Rotating questionable food display

### Věra Newspaper:
- **Pattern:** Reading → Looking Up → Reading
- **Trigger:** Player entry or approach
- **Look Duration:** 2 seconds

### Věra Transaction:
- **Pattern:** Transaction 1 → Transaction 2 → Looking Up
- **FPS:** 2
- **Trigger:** Purchase complete

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Door Interaction Outline | (0, 256) | 64x96 | High-contrast entry highlight (exterior sheet) |
| Section Marker Bold | (0, 192) | 128x48 | Enhanced aisle labels for the four shop sections |
| Register Highlight | (192, 128) | 64x64 | Transaction point outline (vera_counter.png) |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Neon Sign Steady | (128, 256) | 192x48 | Always-on sign state, flicker disabled |
| Static Heat Lamp Food | (64, 128) | 32x32 | Single non-rotating kebab frame |
| Fluorescent Steady | (0, 0) | 256x64 | Constant brightness, no flicker-dim cycle |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Door Chime Indicator | (320, 304) | 32x32 | Bell icon flash when entry chime plays |
| Register Ding Frame | (352, 192) | 32x32 | Flash frame on transaction sound |
| Desperation Tax Alert | (256, 0) | 128x64 | Already-visual price increase notice (UI sheet) |

### Colorblind Considerations:
- Heat lamp quality indicators pair color with distinct shapes: check (fresh), triangle warning (questionable), skull (disaster)
- Desperation Tax notice uses text + icon, never color alone
- Shop section markers use text labels, not color coding
- Touch zones minimum 44px for product browser, register, and door interactions

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); item sprites kept higher quality for shop browser readability
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for UI panels and item icons (detail-critical at small sizes)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| munchies_environment | exterior, interior, sections, counter | 2048x1024 |
| munchies_characters | Věra states, customer NPCs | 1024x512 |
| munchies_items_ui | item sprites, UI elements, lighting effects | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full lighting effects, dust particles, heat lamp steam, rotating food |
| Medium | Simplified lighting overlays, reduced particles, 1 FPS food rotation |
| Low | Static heat lamp, no particles, steady lighting only |

### Performance Targets:
- **Target FPS:** 45
- **Max Draw Calls:** 12 per frame
- **Memory Footprint:** 30 MB maximum
- **Particle Limit:** 10 (dust motes + heat lamp steam)

### Performance Notes:
- Simplified lighting and static heat lamp on low-end devices (per location profile)
- Customer NPCs rotate on a schedule rather than simultaneous rendering (max 2 on screen)
- Item sprites drawn only inside shop browser UI, not in world scene

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Shop browser: UI scene with section tabs mapped to the four aisle sprites
- Desperation Tax: price modifier system keyed to in-game clock (+20% after 2 AM)
- Heat Lamp Lottery: random quality roll (Fresh/Questionable/Disaster) on hot food purchase
- Regular status: purchase counter persists across sessions (5 purchases threshold)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Door open | Entry chime | On door open frame |
| Neon flicker | Electrical buzz | On flicker frame |
| Věra transaction | Register beep + bag rustle | Transaction frames 1-2 |
| Heat lamp station | Low hum + rotation squeak | Continuous while active |
| Desperation Tax notice | Price "cha-ching" sting | On 2 AM price update |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Regular Status | Regular Status Badge, Věra Rare Care state | Unlocks after 5 purchases |
| Věra's Wisdom | Wisdom Moment state, Wisdom Unlock UI | Dialogue unlocks for regulars |
| Hangover Management | Hangover Kit, Hair of Dog, cure icon | Status effect removal purchases |
| Heat Lamp Lottery | Quality indicators, rotating food frames | Risk/reward hot food gamble |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Hostel "Midnight Checkout" | Hostel Forager customer NPC | Shared Hostel Row street exterior |
| The Strobe Survival Kit | Club earplugs item (marked up resale) | Price comparison callout |
| Velvet Curtain Club | Fake VIP wristband item | Wristband may or may not work there |
| Late-Night Kebab Stand | Greasy kebab competitive pricing | Kebab quality contrast gag |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Fluorescent beacon for the desperate - judgment-free, markup included"
- **Color Mood:** Harsh fluorescent white against late-night blue darkness; energy drink green promising salvation
- **Lighting:** Blazing interior fluorescents, warm heat lamp glow, flickering neon sign as landmark
- **Texture:** Clean-but-cluttered shelves, maximum product density, laminated price tags with visible markups

### Environmental Storytelling:
- Window display cluttered with necessities tells the whole business model at a glance
- Four clearly-sectioned aisles (Healing/Support/Offensive/Utility) map to 3 AM need states
- The heat lamp station's rotating mystery food embodies the "fresh is relative" promise
- Honest signage ("You could have bought this cheaper earlier. But here we are.") is the satire made literal

### Character Integration Notes:
- Věra reads as professional detachment: newspaper default pose, glasses, cardigan; Rare Care state reserved for genuine maternal moments
- Customer NPCs each embody a distinct desperation archetype, readable by posture alone
- Věra positioned behind counter with sightline over the whole store - always watching, never judging

---

## 📋 Required PNG Files (10 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | midnight_munchies_exterior.png | 384x384 |
| 2 | shop_interior_full.png | 512x384 |
| 3 | shop_sections_combined.png | 512x384 |
| 4 | heat_lamp_station.png | 192x192 |
| 5 | vera_counter.png | 256x192 |
| 6 | vera_novotna.png | 256x192 |
| 7 | midnight_customers.png | 320x192 |
| 8 | midnight_munchies_items.png | 256x256 |
| 9 | midnight_munchies_ui.png | 384x256 |
| 10 | fluorescent_lighting.png | 512x128 |

**Total Estimated Memory:** ~30 MB (in-memory budget including atlas overhead)

---

## 📦 File Delivery Checklist

### Required PNG Files (10 Total):
- [ ] `midnight_munchies_exterior.png` (384x384)
- [ ] `shop_interior_full.png` (512x384)
- [ ] `shop_sections_combined.png` (512x384)
- [ ] `heat_lamp_station.png` (192x192)
- [ ] `vera_counter.png` (256x192)
- [ ] `vera_novotna.png` (256x192)
- [ ] `midnight_customers.png` (320x192)
- [ ] `midnight_munchies_items.png` (256x256)
- [ ] `midnight_munchies_ui.png` (384x256)
- [ ] `fluorescent_lighting.png` (512x128)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha |
| Color Space | sRGB |
| DPI | 72 |
| Naming | snake_case |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/layered file with organized layer groups (item sprites on individual layers)
- **Documentation:** Animation timing reference sheet (neon flicker, heat lamp rotation, Věra cycles)

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Věra Portrait** - Reading newspaper, seen everything
2. **Desperation Tax Alert** - Prices jump at 2 AM
3. **Heat Lamp Lottery** - Quality roll gamble
4. **Fluorescent Aesthetic** - The beacon in darkness
5. **3 AM Desperate Customer** - Peak need visualization
6. **Regular Status Badge** - Věra knows your face

### Quote Potential:
- "That's €12. ...€16 after 2 AM. You knew this."
- "You could have bought this cheaper earlier. But here we are."
- "The price includes the lesson: plan ahead next time."
- "Prices went up at 2. You know this. Everyone knows this."
- "Every item in this store has a story. The energy drinks are hope. The aspirin is regret. The kebab is surrender."

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 10 PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Věra's professional detachment reads clearly across all six states
- [ ] All 25 item sprites are distinguishable at inventory scale
- [ ] Heat lamp quality indicators use shape + color (check/warning/skull)
- [ ] Desperation Tax UI notice is legible and attention-grabbing
- [ ] Accessibility visual alternatives included for all audio cues (chime, register, buzz)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Desperation pricing satire is clear throughout (honest signage, tax alerts)
- [ ] Four shop sections are visually distinct and navigable
- [ ] Mobile performance optimized (static heat lamp fallback, simplified lighting)
- [ ] Touch zone sizing considered (44px minimum for shop browser and interactions)
- [ ] Colorblind-friendly alternatives for all quality/status indicators
- [ ] Social media viral potential maximized (Věra portrait, Desperation Tax alert compositions)

---

## 🏆 Location Validation Status

| Requirement | Status |
|-------------|--------|
| World Consistency | ✅ PASS |
| Cultural Specificity | ✅ PASS |
| Satirical Targets | ✅ PASS |
| Seedy Underbelly | ✅ PASS |
| Gameplay Value | ✅ PASS |
| Technical Feasibility | ✅ PASS |
| Mobile Performance | ✅ PASS (45 FPS, 12 draws, 30MB) |
| Accessibility | ✅ PASS |
| Social Media | ✅ PASS |
| No Crypto Elements | ✅ PASS |

**The Midnight Munchies General Store becomes the essential late-night survival hub where the Desperation Tax teaches lessons nobody learns, Věra watches without judgment but with maximum observation, the Heat Lamp Lottery offers questionable odds, and every purchase proves you should have planned ahead (but you didn't, and now it's 3 AM)!**
