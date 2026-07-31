# Paddy's Premium Motors - Complete PNG Asset Requirements

## 📋 Overview
**Location ID:** `publandia_outskirts_paddys_premium_motors_01`  
**Theme:** Resigned fatalism meets tourist overconfidence - the last stop before The Cloverleaf  
**Zone:** Publandia Outskirts, edge of city  
**Hours:** 08:00-20:00

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Irish Green | #228B22 | Signage, accents, shamrock logo |
| Rust Brown | #8B4513 | Wood elements, weathered surfaces |
| Faded White | #F5F5DC | Painted trim, papers |
| Warning Yellow | #FFD700 | Caution signs, counter numbers |
| Gravel Gray | #A9A9A9 | Parking lot, exterior ground |
| Sky Gray | #B0C4DE | Overcast Irish sky |
| Polaroid Brown | #D2691E | Board of Shame photos |
| Cigarette Orange | #FF7F50 | Seamus's cigarette ember |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/paddys_premium_motors/
├── environment/
│   ├── exterior_building.png
│   ├── parking_lot.png
│   ├── interior_reception.png
│   └── background_countryside.png
├── npcs/
│   ├── seamus.png
│   └── sheep_ambient.png
├── objects/
│   ├── board_of_shame.png
│   ├── reception_details.png
│   └── rental_cars.png
├── effects/
│   ├── rain_particles.png
│   └── smoke_effects.png
└── ui/
    └── rental_menu.png
```

---

## 🏠 Sprite Sheet 1: Exterior Building
**File:** `exterior_building.png`  
**Dimensions:** 512x384 pixels

### Building Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Farmhouse Main | (0, 0) | 256x256 | Converted farmhouse, stone walls, green door |
| Roof Section | (0, 0) | 256x96 | Slate roof, slightly weathered |
| Main Sign | (256, 0) | 192x64 | "PADDY'S PREMIUM MOTORS" hand-painted |
| Shamrock Logo | (448, 0) | 64x64 | Faded green shamrock |
| Window | (256, 64) | 64x64 | Rain-streaked glass |
| Door Open | (320, 64) | 64x96 | Green door, brass handle |
| Door Closed | (384, 64) | 64x96 | Same, closed state |
| Warning Signs | (256, 160) | 192x96 | Multiple cautionary signs |
| Counter Sign | (0, 256) | 128x64 | "DAYS SINCE INCIDENT: 0" |

### Warning Signs Detail:
| Sign | Position | Size | Description |
|------|----------|------|-------------|
| Insurance Sign | (256, 160) | 64x32 | "INSURANCE RECOMMENDED" |
| Cloverleaf Sign | (320, 160) | 64x32 | "NOT LIABLE FOR CLOVERLEAF" |
| GPS Sign | (384, 160) | 64x32 | "GPS AVAILABLE €20" |
| Fine Print | (256, 192) | 128x32 | Illegibly small warnings |

---

## 🚗 Sprite Sheet 2: Parking Lot
**File:** `parking_lot.png`  
**Dimensions:** 512x256 pixels

### Ground & Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gravel Base | (0, 0) | 256x128 | Gray gravel texture |
| Puddles | (256, 0) | 128x64 | Rain puddles, reflective |
| Parking Lines | (384, 0) | 64x64 | Faded white lines |
| Road Exit | (0, 128) | 256x64 | Road leading toward Cloverleaf |
| Distant Cloverleaf | (256, 128) | 128x64 | Ominous roundabout visible on horizon |
| Sheep Grazing | (384, 128) | 64x64 | Background sheep |

### Rental Cars (Various):
| Vehicle | Position | Size | Description |
|---------|----------|------|-------------|
| The Shamrock | (0, 192) | 96x64 | Green compact, dented |
| The Lucky Charm | (96, 192) | 96x64 | Blue sedan, scratched |
| The Emerald Dream | (192, 192) | 96x64 | SUV, too wide |
| The Full Irish | (288, 192) | 96x64 | Convertible, impractical |
| Generic Rentals | (384, 192) | 128x64 | Background vehicles |

---

## 🏢 Sprite Sheet 3: Interior Reception
**File:** `interior_reception.png`  
**Dimensions:** 512x512 pixels

### Room Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floor | (0, 0) | 256x128 | Worn linoleum, scuff marks |
| Back Wall | (0, 128) | 256x128 | Cream paint, stained |
| Side Wall Left | (256, 0) | 128x256 | Board of Shame wall |
| Side Wall Right | (384, 0) | 128x256 | Key hooks, map |
| Counter | (0, 256) | 256x64 | Weathered wood, scratched |
| Window | (256, 256) | 128x64 | Gray light, rain streaks |
| Door Interior | (384, 256) | 64x96 | Green, brass fittings |

### Reception Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Key Wall | (0, 320) | 128x64 | Rows of car keys on hooks |
| Tourism Posters | (128, 320) | 128x64 | Faded "VISIT PUBLANDIA" posters |
| Computer | (256, 320) | 64x48 | Ancient PC, Windows 98 |
| Ashtray | (320, 320) | 32x32 | Overflowing, memorial |
| Photo Frame | (352, 320) | 32x32 | Mary's photo |
| Filing Cabinet | (384, 320) | 64x64 | Dented, rusty |
| Incident Counter | (0, 384) | 128x48 | "DAYS SINCE: 0" wall mount |
| Fluorescent Light | (128, 384) | 128x32 | Flickering tubes |

---

## 👴 Sprite Sheet 4: Seamus
**File:** `seamus.png`  
**Dimensions:** 384x384 pixels

### Seamus States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Idle | (0, 0) | 96x128 | Behind counter, thousand-yard stare |
| Talking | (96, 0) | 96x128 | Gesturing, resigned |
| Sliding Keys | (192, 0) | 96x128 | The iconic motion |
| Warning | (288, 0) | 96x128 | Leaning forward, intense |
| Thousand Yard | (0, 128) | 96x128 | Dead eyes, distant |
| Smoking | (96, 128) | 96x128 | Cigarette lit, exhaling |
| Looking at Photo | (192, 128) | 96x128 | Touching Mary's picture |
| Post-Quest Respect | (288, 128) | 96x128 | Slight nod, almost smile |

### Seamus Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Aran Sweater | (0, 256) | 64x64 | Cream cable-knit texture |
| Face Close-Up | (64, 256) | 64x64 | Weathered, deep-set eyes |
| Hands | (128, 256) | 64x32 | Calloused, wedding ring |
| Cigarette | (192, 256) | 32x16 | Behind ear, occasionally lit |
| Wedding Ring | (224, 256) | 16x16 | Gold, worn thin |

### Seamus Expressions:
| Expression | Position | Size | Description |
|------------|----------|------|-------------|
| Resignation | (0, 288) | 48x48 | Default, tired acceptance |
| Warning | (48, 288) | 48x48 | Eyebrows raised, intense |
| Memory | (96, 288) | 48x48 | Distant, thinking of Mary |
| Respect | (144, 288) | 48x48 | Slight softening |
| "Here We Go Again" | (192, 288) | 48x48 | Eye roll, subtle |

### Dialogue Portraits:
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Portrait Default | (0, 336) | 64x48 | For dialogue boxes |
| Portrait Warning | (64, 336) | 64x48 | Intense version |
| Portrait Sad | (128, 336) | 64x48 | Discussing Mary |
| Portrait Respect | (192, 336) | 64x48 | Post-quest |

---

## 📸 Sprite Sheet 5: Board of Shame
**File:** `board_of_shame.png`  
**Dimensions:** 256x256 pixels

### Board Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Corkboard Base | (0, 0) | 192x192 | Brown cork texture |
| Title Card | (0, 0) | 96x24 | "THEY DIDN'T LISTEN" |
| Pushpins | (192, 0) | 64x32 | Red, scattered |

### Polaroid Photos:
| Photo | Position | Size | Description |
|-------|----------|------|-------------|
| 1987 Van | (8, 32) | 48x48 | "JUST MARRIED" visible |
| German Sedan | (64, 32) | 48x48 | 1995 date |
| American Rental | (120, 32) | 48x48 | "VACAY-1" plate |
| French Compact | (8, 88) | 48x48 | Baguette visible inside |
| Italian Sports | (64, 88) | 48x48 | Too fast for roundabout |
| Empty Spot | (120, 88) | 48x48 | Note: "Reserved for next" |
| Recent 1 | (8, 144) | 48x48 | This month's date |
| Recent 2 | (64, 144) | 48x48 | Last week's date |
| Recent 3 | (120, 144) | 48x48 | Yesterday's date |

### Annotations:
| Note | Position | Size | Description |
|------|----------|------|-------------|
| "Still circling" | (176, 32) | 48x16 | Handwritten note |
| "Found empty" | (176, 88) | 48x16 | Handwritten note |
| "Gave up" | (176, 144) | 48x16 | Handwritten note |

---

## 🗺️ Sprite Sheet 6: Reception Details
**File:** `reception_details.png`  
**Dimensions:** 256x256 pixels

### The Map:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Publandia Map | (0, 0) | 128x128 | Standard road map |
| Cloverleaf Circle | (64, 48) | 32x32 | Aggressive red marker |
| "HERE BE DRAGONS" | (48, 80) | 48x16 | Seamus's handwriting |
| Crossed Routes | (0, 0) | 128x128 | Multiple attempts marked out |

### Desk Items:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Computer Screen | (128, 0) | 64x48 | Windows 98, frozen |
| Keyboard | (192, 0) | 48x24 | Yellowed, sticky |
| Mouse | (240, 0) | 16x16 | Ball mouse, ancient |
| Ashtray Full | (128, 48) | 48x32 | Overflowing, memorial |
| Photo Frame | (176, 48) | 32x32 | Mary's photo |
| Photo Back | (208, 48) | 32x32 | "MARY - CLOVERLEAF '92" |
| Ring Box | (128, 80) | 24x24 | Never opened again |
| Coffee Mug | (152, 80) | 24x24 | "WORLD'S MOST PATIENT DAD" |

### Keys & Hooks:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Key Rack | (0, 128) | 128x64 | Wall-mounted, 12 hooks |
| Shamrock Keys | (128, 128) | 32x24 | Green fob |
| Lucky Charm Keys | (160, 128) | 32x24 | Blue fob |
| Emerald Keys | (192, 128) | 32x24 | Gold fob |
| Full Irish Keys | (224, 128) | 32x24 | Leather fob |

### Incident Counter:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Frame | (0, 192) | 128x48 | Wooden frame, official looking |
| "DAYS SINCE" | (8, 200) | 112x16 | Painted letters |
| Numbers "000" | (8, 216) | 112x24 | Permanently stuck |
| Dust Overlay | (0, 192) | 128x48 | Never changed |

---

## 🐑 Sprite Sheet 7: Sheep & Environment
**File:** `sheep_ambient.png`  
**Dimensions:** 192x128 pixels

### Sheep States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Grazing | (0, 0) | 48x48 | Head down, eating |
| Walking | (48, 0) | 48x48 | Mid-stride |
| Staring | (96, 0) | 48x48 | Looking at player, judging |
| Group | (144, 0) | 48x48 | Multiple sheep clump |

### Environment Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stone Wall | (0, 48) | 96x32 | Irish dry stone wall |
| Green Grass | (96, 48) | 48x32 | Wet grass texture |
| Mud Patch | (144, 48) | 48x32 | Near gate |
| Gate | (0, 80) | 48x48 | Metal farm gate |
| Countryside BG | (48, 80) | 144x48 | Rolling green hills |

---

## 🌧️ Sprite Sheet 8: Effects
**File:** `paddys_effects.png`  
**Dimensions:** 128x128 pixels

### Rain Effects:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Rain Drop 1 | (0, 0) | 8x16 | Falling animation |
| Rain Drop 2 | (8, 0) | 8x16 | Variant |
| Rain Drop 3 | (16, 0) | 8x16 | Variant |
| Puddle Ripple | (24, 0) | 24x16 | Impact effect |
| Rain Sheet | (48, 0) | 80x32 | Dense rain overlay |

### Smoke Effects:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Cigarette Smoke 1 | (0, 32) | 16x24 | Wisp frame 1 |
| Cigarette Smoke 2 | (16, 32) | 16x24 | Wisp frame 2 |
| Cigarette Smoke 3 | (32, 32) | 16x24 | Wisp frame 3 |
| Ashtray Smoke | (48, 32) | 32x24 | Ambient from ashtray |

### Lighting:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Fluorescent Flicker | (0, 64) | 64x16 | 3-frame flicker |
| Window Light | (64, 64) | 48x32 | Gray daylight beam |
| Dust Motes | (0, 80) | 32x32 | Floating particles |

---

## 🎮 Sprite Sheet 9: UI Elements
**File:** `paddys_ui.png`  
**Dimensions:** 256x192 pixels

### Rental Menu:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu Frame | (0, 0) | 192x128 | Rental selection box |
| Vehicle Icons | (192, 0) | 64x128 | 4 car silhouettes |
| Price Tags | (0, 128) | 128x32 | €45, €60, €80, €120 |
| Add-On Icons | (128, 128) | 64x32 | GPS, Insurance, Map, Rosary |

### Transaction UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Contract Paper | (0, 160) | 96x32 | Signing animation |
| Keys Handoff | (96, 160) | 64x32 | Seamus sliding keys |
| Warning Popup | (160, 160) | 96x32 | "ARE YOU SURE?" |

---

## 🎬 Animation Specifications

### Seamus Idle Cycle:
- **Duration:** 10 seconds loop
- **Frames:** Idle (4s) → Sigh (1s) → Look at photo (2s) → Return (2s) → Smoke check (1s)
- **Variants:** Occasionally touches wedding ring

### Rain Ambient:
- **Duration:** Continuous
- **Density:** 15-20 drops on screen
- **Pattern:** Random fall with slight wind drift
- **Puddle ripples:** Triggered on drop impact

### Sheep Wandering:
- **Pattern:** Random walk across parking lot background
- **Frequency:** Every 30-45 seconds
- **Interaction:** Pauses to stare at player if approached

### Key Sliding:
- **Duration:** 1.5 seconds
- **Sequence:** Pickup → Slide across counter → Release
- **Audio sync:** Metal scraping on wood

### Fluorescent Flicker:
- **Duration:** Random intervals 15-60 seconds
- **Pattern:** Quick double-flash
- **Note:** Adds to oppressive atmosphere

---

## 📱 Mobile Optimization

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| paddys_environment | exterior, parking_lot, interior, background | 1024x1024 |
| paddys_characters | seamus, sheep_ambient | 512x512 |
| paddys_details | board_of_shame, reception_details, effects, ui | 512x512 |

### Performance Notes:
- Rain particles limited to 20 maximum
- Sheep only 1-2 on screen at a time
- Fluorescent flicker uses simple alpha toggle
- Board of Shame polaroids are static, not animated
- Interior/exterior transition is simple fade

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full rain, all smoke, sheep wandering |
| Medium | Reduced rain (10), simplified smoke |
| Low | Minimal rain (5), static sheep, no smoke |

---

## 📋 Required PNG Files (9 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | exterior_building.png | 512x384 |
| 2 | parking_lot.png | 512x256 |
| 3 | interior_reception.png | 512x512 |
| 4 | seamus.png | 384x384 |
| 5 | board_of_shame.png | 256x256 |
| 6 | reception_details.png | 256x256 |
| 7 | sheep_ambient.png | 192x128 |
| 8 | paddys_effects.png | 128x128 |
| 9 | paddys_ui.png | 256x192 |

**Total Estimated Memory:** ~18MB

---

## ✅ Validation Status

| Requirement | Status |
|-------------|--------|
| World Consistency | ✅ PASS (Publandia) |
| Cultural Specificity | ✅ PASS (Irish driving, left-side roads) |
| Satirical Targets | ✅ PASS (Tourist overconfidence) |
| Gameplay Value | ✅ PASS (Quest trigger, shop) |
| No Crypto Elements | ✅ PASS |
| Mobile Optimization | ✅ PASS |
| Seedy Underbelly | ✅ PASS (Mary's disappearance) |

---

## 🎯 Key Visual Moments

1. **The Board of Shame** - Corkboard full of abandoned car polaroids
2. **"DAYS SINCE INCIDENT: 0"** - Counter that's never moved
3. **Seamus's Thousand-Yard Stare** - The face of a man who has seen too much
4. **The Map** - "HERE BE DRAGONS" over The Cloverleaf
5. **Keys Sliding** - The iconic moment of doom delivery
6. **Mary's Photo** - "CLOVERLEAF '92" on the back
7. **The Distant Roundabout** - Visible through the window, waiting

---

**Paddy's Premium Motors delivers the visual comedy of impending doom. Every element - from the stuck counter to Mary's photo to the Board of Shame - tells the same story: this has happened before, it will happen again, and the bros are about to become the next victims. Seamus's resigned weathering and thousand-yard stare sell the forty years of warnings that have gone unheeded. The distant Cloverleaf, visible on the horizon, waits for its next meal.**

**"That's what they all say."**
