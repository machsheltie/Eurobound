# Opera House Plaza - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Opera House Plaza location in Sinfonia — the most cultured place in Europe to witness a horse-related disaster. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this grand baroque plaza where 400 years of imperial self-regard meets a drunk Fiaker driver, a runaway horse, and the American tourists who make everything worse. The plaza is ground zero for the Fiaker Fiasco quest.

**Location ID:** `sinfonia_imperial_opera_house_plaza_01`
**Theme:** Imperial baroque grandeur as a tourist commodity — high culture that charges €7 extra for the "historic view"
**Zone:** Imperial Square District
**Hours:** Always accessible (Day 10:00–17:00 bustling cultural; Evening 17:00–22:00 refined formal; Night 22:00–02:00 decadent shadowy)
**Primary Function:** Quest hub / social space — Fiaker Fiasco initiation and resolution, premium tourist-vendor economy, fountain landmark interactions, street performer recovery point

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Imperial Gold | #DAA520 | Gilded statues, signage, trim |
| Baroque Cream | #F5F5DC | Building facades |
| Opera House White | #FFFAFA | Opera facade highlights, columns |
| Cobblestone Grey | #808080 | Plaza surface |
| Cobblestone Dark | #696969 | Worn/shadowed cobble variants |
| Fiaker Black | #1C1C1C | Carriages, driver formal wear |
| Lipizzan Grey (Gustav) | #DCDCDC | Gustav's coat |
| Hans-Jürgen Shame Red | #8B0000 | Panic face, opera cape |
| Fountain Green (aged) | #2F4F4F | Neptune's patina |
| Night Ambient Blue | #4169E1 | Night scene ambient tint |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/opera_house_plaza/
├── environment/
│   └── opera_house_plaza_tileset.png
├── npcs/
│   └── opera_plaza_characters.png
├── objects/
│   └── fiaker_carriage.png
└── effects/
    └── opera_plaza_effects.png
```

---

## 🎨 Sprite Sheet 1: Plaza Tileset
**File:** `opera_house_plaza_tileset.png`  
**Dimensions:** 1024x1024 pixels  
**Color Palette:** 
- Cobblestone Grey: #808080
- Cobblestone Dark: #696969
- Imperial Gold: #DAA520
- Baroque Cream: #F5F5DC
- Opera White: #FFFAFA
- Fountain Green (aged): #2F4F4F

### Cobblestone Tiles (32x32 each):
- **Cobble Standard** (0, 0, 32x32) - Base plaza cobblestone
- **Cobble Worn** (32, 0, 32x32) - Worn variant with subtle cracks
- **Cobble Wet** (64, 0, 32x32) - Rain-soaked cobblestone with reflections
- **Cobble Performer Circle** (96, 0, 32x32) - Decorative pattern marking performance area
- **Cobble Edge** (0, 32, 32x32) - Transition tile to grass/other surfaces
- **Cobble Corner** (32, 32, 32x32) - Corner piece for plaza boundaries

### Fountain Tiles:
- **Fountain Base NW** (256, 0, 64x64) - Northwest section of fountain base
- **Fountain Base NE** (320, 0, 64x64) - Northeast section
- **Fountain Base SW** (256, 64, 64x64) - Southwest section
- **Fountain Base SE** (320, 64, 64x64) - Southeast section
- **Neptune Statue** (384, 0, 96x128) - Central Neptune figure, baroque style, slightly green patina
- **Water Surface** (256, 128, 128x64) - Animated water surface

### Building Facade Tiles:
- **Opera Facade Section** (512, 0, 256x256) - Main opera house facade with columns
- **Opera Columns** (768, 0, 64x256) - Repeatable column element
- **Opera Entrance** (832, 0, 128x192) - Grand entrance doorway with steps
- **Baroque Building 1** (512, 256, 128x192) - Generic baroque facade left
- **Baroque Building 2** (640, 256, 128x192) - Generic baroque facade right
- **Café Facade** (768, 256, 192x160) - Coffeehouse storefront with awning

### Props:
- **Bench Ornate** (0, 128, 64x32) - Habsburg-style ironwork bench
- **Lamppost Gas** (64, 128, 32x96) - Ornate gas lamp (lit state)
- **Signpost Gilded** (96, 128, 32x64) - Directional sign with German text
- **Queue Post** (128, 128, 16x48) - Numbered Fiaker queue marker
- **Café Table** (0, 192, 32x32) - White-clothed table (intact)
- **Café Chair** (32, 192, 24x32) - Matching café chair
- **Performer Hat** (56, 192, 24x16) - Velvet-lined violin case open
- **Opera Poster** (80, 192, 48x64) - "The Magic Flute" performance poster

---

## 🎭 Sprite Sheet 2: Character Sprites
**File:** `opera_plaza_characters.png`  
**Dimensions:** 2048x1024 pixels  
**Color Palette:**
- Fiaker Black: #1C1C1C
- Hans-Jürgen Red Face: #8B0000
- Gustav Lipizzan Grey: #DCDCDC
- Opera Cape Red: #8B0000
- Formal White: #FFFFFF
- Brass Buttons: #B5A642

### Hans-Jürgen (64x96 base size):

**Idle Drunk** (6 frames, 2 FPS):
- (0-320, 96, 64x96 each) - Pronounced sway with flask sipping

**Panic** (8 frames, 8 FPS):
- (0-448, 192, 64x96 each) - Running in place, wild arm gestures, hat bouncing

**Relief Hug** (6 frames, 4 FPS):
- (0-480, 288, 96x96 each) - Bear hug animation with Gustav

**Confession** (4 frames, 1 FPS):
- (0-192, 384, 64x96 each) - Slumped against carriage

**Details:**
- Bowler Hat Askew (512, 0, 32x24)
- Schnapps Flask (544, 0, 16x32)
- Gustav Photo (560, 0, 24x32)

### Gustav Horse (128x96 base size):

**Eating** (6 frames, 2 FPS):
- (640-1280, 96, 128x96 each) - Munching stolen food

**Judgmental Stare** (2 frames, hold frame 1 for 3 seconds):
- (640-768, 192, 128x96 each) - Direct stare, ears back

**Escape Trot** (8 frames, 8 FPS):
- (640-1536, 288, 128x96 each) - Full trot cycle

**Considering Skittles** (4 frames, 1 FPS):
- (640-1024, 384, 128x96 each) - Head tilt, taking one Skittle

**Resigned Return** (6 frames, 2 FPS):
- (640-1280, 480, 128x96 each) - Heavy sigh, reluctant walk

**Accessories:**
- Opera Cape (1408, 0, 64x96) - Red cape overlay
- Harness Broken (1472, 0, 48x64) - Remnant pieces
- Sachertorte Crumbs (1520, 0, 24x16) - Muzzle overlay

### Supporting NPCs (48-64x80):
- Opera Usher states (0-96, 576)
- Café Maître D' states (144-240, 576)
- Street Performer playing (288-432, 576, 4 frames)
- Ticket Scalper states (480-528, 576)
- Pigeon Lady states (576-640, 576)
- Fiaker Driver Variants (704-848, 576)
- Opera Patrons (896-992, 576)

---

## ✨ Sprite Sheet 3: Environmental Effects
**File:** `opera_plaza_effects.png`  
**Dimensions:** 512x512 pixels  

### Fountain Water:
- **Spray** (0-448, 0, 64x64 each) - 8 frames, 8 FPS
- **Ripples** (0-144, 64, 48x48 each) - 4 frames, 4 FPS

### Pigeons:
- **Pecking** (0-120, 128, 24x24 each) - 6 frames, 6 FPS
- **Flying** (0-224, 152, 32x32 each) - 8 frames, 12 FPS

### Gas Lamp Glow:
- (0-144, 200, 48x48 each) - 4 frames, 2 FPS

### Table Destruction:
- (0-320, 256, 64x64 each) - 6 frames, 12 FPS, no loop

---

## 🐴 Sprite Sheet 4: Fiaker Carriage
**File:** `fiaker_carriage.png`  
**Dimensions:** 512x256 pixels  

- **Idle** (0, 0, 192x128) - Empty carriage at rest
- **Horse Attached** (192, 0, 256x128) - Carriage with horse
- **Empty No Horse** (0, 128, 192x128) - Abandoned, harness dangling

---

## 🎬 Animation Specifications

### Fountain Spray:
- **Duration:** 1.0 second cycle
- **Frames:** 8
- **Pattern:** Frame 1 → 8 → loop
- **Trigger:** Constant
- **Purpose:** Living centerpiece; the plaza's heartbeat of aged imperial elegance
- **Audio Sync:** Continuous fountain water layer (volume 0.5)
- **Mobile Optimization:** Drop to 4 frames at 4 FPS on low-end devices

### Hans-Jürgen Panic:
- **Duration:** 1.0 second cycle
- **Frames:** 8
- **Pattern:** Frame 1 → 8 → loop while panicked
- **Trigger:** Fiaker Fiasco quest trigger (first approach during day hours)
- **Purpose:** Sells the quest hook — a grown man's professional life collapsing in real time
- **Audio Sync:** Accelerating violin tremolo stinger on first frame
- **Mobile Optimization:** None needed (single NPC)

### Gustav Judgmental Stare:
- **Duration:** ~3.5 seconds (frame 1 held 3 seconds, frame 2 blink)
- **Frames:** 2
- **Pattern:** Hold frame 1 for 3 seconds → frame 2 → loop
- **Trigger:** Player proximity / dialogue beats
- **Purpose:** The single most meme-able expression in Sinfonia; comedic dead air
- **Audio Sync:** Single low cello note on stare start
- **Mobile Optimization:** None needed

### Gustav Escape Trot:
- **Duration:** 1.0 second cycle
- **Frames:** 8
- **Pattern:** Full trot cycle, loop while fleeing
- **Trigger:** Chase-begins quest phase
- **Purpose:** Launches the cross-city Fiaker Fiasco chase route
- **Audio Sync:** Hoofbeats on cobblestone, 2 per cycle
- **Mobile Optimization:** Reduce to 6 frames at 6 FPS

### Café Table Destruction:
- **Duration:** 0.5 seconds
- **Frames:** 6
- **Pattern:** Frame 1 → 6, no loop, hold final debris frame
- **Trigger:** Gustav collision during chase
- **Purpose:** First property-damage beat; introduces the running € damage gag
- **Audio Sync:** Crash plus cash-register ching on frame 4
- **Mobile Optimization:** Skip intermediate frames 2 and 4 on low-end

### Pigeon Flock (Pecking / Flying):
- **Duration:** 1.0s pecking loop; 0.67s flight cycle
- **Frames:** 6 (pecking), 8 (flying)
- **Pattern:** Pecking loops idle; flying triggered on player approach
- **Trigger:** Constant ambient / proximity startle
- **Purpose:** Ambient life; supports Pigeon Lady characterization
- **Audio Sync:** Intermittent pigeon coo layer (volume 0.2); wing flutter on startle
- **Mobile Optimization:** Cap flock at 12 birds (from 40) on low-end

### Gas Lamp Glow:
- **Duration:** 2.0 second cycle
- **Frames:** 4
- **Pattern:** Subtle pulse loop
- **Trigger:** Evening/night states only
- **Purpose:** Golden-hour-to-night atmosphere shift
- **Audio Sync:** None
- **Mobile Optimization:** Static lit frame on low-end

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gustav outline overlay | set at sheet layout | 128x96 | High-contrast silhouette so the quest target reads against busy cobblestone |
| Hans-Jürgen outline overlay | set at sheet layout | 64x96 | Quest-giver highlight for first-visit trigger |
| Neptune Fountain interact ring | set at sheet layout | 96x96 | Bold ring marking the interactable landmark |
| Fiaker queue post highlight | set at sheet layout | 16x48 | Enhanced-visibility marker for queue position #3 |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fountain static frame | set at sheet layout | 128x64 | Non-animated water surface replacing 8-frame spray |
| Pigeon static cluster | set at sheet layout | 96x48 | Grounded pigeons, no flight burst on approach |
| Gas lamp steady glow | set at sheet layout | 48x48 | Non-pulsing lit state |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Panic tremolo icon | set at sheet layout | 24x24 | Vibrating violin glyph over Hans-Jürgen when the panic stinger fires |
| Cello-note stare vignette | set at sheet layout | 32x16 | Low-note glyph accompanying Gustav's judgmental stare |
| Crash/ching burst | set at sheet layout | 32x32 | Impact star + € glyph for every property-damage sound |
| Hoofbeat ripples | set at sheet layout | 24x12 | Ground pulse marks during Gustav's off-screen trot audio |

### Colorblind Considerations:
- Fiaker queue posts numbered, not color-coded; Hans-Jürgen's post reads "#3" in text
- Damage popups pair the € numeral with an impact-star shape, never color alone
- Touch zones minimum 48px for all interactive elements (per location performance spec)

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); Neptune statue and opera facade need ASTC 4x4 for gilding detail
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for the opera facade (marketing-visible asset)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| plaza_environment | tileset, fiaker carriage | 2048x2048 |
| plaza_characters | Hans-Jürgen, Gustav, supporting NPCs | 2048x1024 |
| plaza_effects | fountain, pigeons, lamp glow, destruction | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full 40-pigeon flock, fountain spray + ripples, autumn leaves, all lamp pulses |
| Medium | 20 pigeons, spray only (no ripples), reduced leaf drift |
| Low | 12 static pigeons, static water, no leaves, static lamps |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 40 per frame
- **Memory Footprint:** 40 MB maximum
- **Particle Limit:** 60 (pigeons + fountain + leaves + horse breath combined)

### Performance Notes:
- Pigeon flocking runs on CPU with position pooling; despawn birds outside camera margin
- Night point lights (gas lamps, café candles, opera spotlights) capped at 8 active
- Character sheet (2048x1024) loads on-demand; supporting NPC rows stream by time-of-day state

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- TileMap for plaza surface; ParallaxBackground for opera facade depth
- AnimatedSprite2D for Hans-Jürgen/Gustav states; CPUParticles2D (not GPU) for fountain, leaves, horse breath
- Time-of-day state machine swaps lighting presets (day/evening/night) and NPC rosters
- CanvasLayer for the shared Fiaker Fiasco damage-counter UI

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Hans-Jürgen panic start | Accelerating violin tremolo | On first panic frame |
| Gustav judgmental stare | Single low cello note | On stare hold start |
| Café table destruction | Crash + cash-register ching | On frame 4 (impact) |
| Bros' wisdom dialogue | Mocking harp flourish | On dialogue box open |
| Fountain spray | Continuous water loop | Constant, volume 0.5 |
| Distant orchestra rehearsal | Muffled opera layer | Constant from north edge, volume 0.3 |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Fiaker Fiasco (initiation) | Hans-Jürgen panic set, Gustav photo detail | First daytime approach triggers cutscene at queue post #3 |
| Fiaker Fiasco (first sighting) | Gustav eating + judgmental stare, café table destruction | Gustav spotted at café terraces, chase begins |
| Fiaker Fiasco (resolution return) | Relief hug / confession / resigned return sets, carriage states | Path A returns Gustav to the carriage; empty-carriage state persists otherwise |
| Post-quest ambience | Newspaper stand headline swap, Gustav background cameo | Environmental storytelling after quest completion |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Bassline Opera House | Opera facade/entrance tiles; shared damage-counter UI | Direct adjacency, north edge door transition |
| Café Sachertorte | Gustav sprite continues (sachertorte-crumb muzzle overlay) | Chase route hand-off, screen wipe with hoofbeats |
| Opera Backstage | Gustav + Hans-Jürgen sprites continue | Chase route phase 3 |
| Stadtpark (Gustav's Refuge) | Gustav, Pigeon Lady base sprites reused | Quest finale hand-off |
| The Black-Tie Backroom | Gossip connection only (NPC dialogue) | No sprite transition |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Imperial grandeur with a tip jar" — every gilded surface has a price tag nearby
- **Color Mood:** Warm golds and creams against cool cobblestone grey; the architecture glows while the pavement does the work
- **Lighting:** Harsh baroque shadows by day, golden hour by evening, gas-lamp pools and royal-blue ambient by night
- **Texture:** Worn cobble, aged fountain patina, crisp white tablecloths — maintained decay, expensively preserved

### Environmental Storytelling:
- Neptune's green patina vs. freshly regilded opera statues: the city polishes what tourists photograph
- Numbered Fiaker queue posts formalize even the horse-carriage hustle; Hans-Jürgen's is #3
- "The Magic Flute" poster foreshadows the backstage disaster two locations later
- Scalper lurking at €200–500 for €40 tickets — the seedy underbelly wears a nice coat

### Character Integration Notes:
- Hans-Jürgen and Gustav are the emotional axis; both need readable silhouettes at plaza-wide zoom
- Gustav's accessory overlays (cape, broken harness, crumbs) composite over the base sheet — do not bake into frames
- Supporting NPC rows swap by time-of-day state (tourists by day, opera patrons by evening, drunks by night)

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Gustav in Opera Cape** - Horse wearing stolen red cape, judging the viewer
2. **Hans-Jürgen's Panic Face** - Red-faced, hat flying, arms flailing
3. **Table Destruction Mid-Frame** - Sachertorte flying through air
4. **Judgmental Stare Close-Up** - Gustav's expression is internet gold

### Quote Potential:
- "Gustav! GUSTAV! He has never done this before, I swear it!" - Hans-Jürgen
- "Face value? Sir, this is a *cultural experience*." - Ticket Scalper
- "The horse knows what he did." - Pigeon Lady

---

## 📋 Required PNG Files (4 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | opera_house_plaza_tileset.png | 1024x1024 |
| 2 | opera_plaza_characters.png | 2048x1024 |
| 3 | opera_plaza_effects.png | 512x512 |
| 4 | fiaker_carriage.png | 512x256 |

**Total Estimated Memory:** ~13.5 MB (uncompressed RGBA)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `opera_house_plaza_tileset.png` (1024x1024)
- [ ] `opera_plaza_characters.png` (2048x1024)
- [ ] `opera_plaza_effects.png` (512x512)
- [ ] `fiaker_carriage.png` (512x256)

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
- **Documentation:** Animation timing reference sheet + time-of-day lighting preset guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Gustav's judgmental stare reads clearly at gameplay zoom
- [ ] Gustav accessory overlays (cape, harness, crumbs) align to base frames
- [ ] Accessibility visual alternatives included for all four audio stingers
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (culture-as-commodity) is clear throughout all assets
- [ ] Fiaker queue and fountain interactions have discoverable visual cues
- [ ] Mobile performance optimized (CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (48px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Vienna evoked, never named |
| Cultural Specificity | ✅ | Viennese imperial plaza culture, Fiaker tradition, coffeehouse terraces |
| Satirical Targets Appropriate | ✅ | Tourist-fleecing economy, scalpers, cultural pretension — punches up |
| Seedy Underbelly Present | ✅ | Ticket scalping, price gouging, night-time "suspicious dealings" |
| Gameplay Value Established | ✅ | Fiaker Fiasco hub, vendors, status effects, recovery services |
| Technical Feasibility | ✅ | Four sheets, atlas plan, LOD tiers documented |
| Mobile Performance Budget | ✅ | 60 FPS, 40 draw calls, 40 MB, 60 particles |
| Accessibility Features | ✅ | Visual cues for all four comedy stingers; static motion variants |
| No Crypto Elements | ✅ | None present |
| Social Media Integration | ✅ | Judgmental stare and cape moments identified |

**Opera House Plaza brings the refined chaos of high culture colliding with American tourist energy—where a drunk Fiaker driver's worst day becomes the bros' most memorable adventure.**
