# Central Shamsterdam Bike Crossing - Complete PNG Asset Requirements

*Artist Reference Document for the Bicycle Thunderdome Frogger Mini-Game*

**Location ID**: `shamsterdam_bike_crossing_thunderdome_01`  
**Priority**: HIGH (Central Hub, Mini-Game Location, Required for All Shamsterdam Traversal)  
**Total Sheets Required**: 12  
**Mobile Optimization**: CRITICAL - 60 FPS required for timing-based gameplay

---

## 📋 Overview
The Central Shamsterdam Bike Crossing is a six-lane bicycle intersection bisected by two tram tracks — the "Bicycle Thunderdome," a Frogger-style mini-game where American pedestrian overconfidence meets Dutch cycling reality and loses, every time. This document specifies every PNG asset required to build the crossing: the tileset, eight cyclist archetypes, the unstoppable tram, the cargo parade wall, five NPCs, effects, UI, and the rental kiosk. Its satirical essence in a sentence: the gap between "bike-friendly city" tourism marketing and cyclists who *will not stop for you*.

**Location ID:** `shamsterdam_bike_crossing_thunderdome_01`
**Theme:** Amsterdam's infamous bicycle culture and tourist-hostile traffic — Dutch efficiency as environmental hazard
**Zone:** Canal Ring District / Central Traffic Hub
**Hours:** Always accessible (24 hours; traffic patterns vary — rush hour 08:00-09:00 and 17:00-19:00, night bikes 22:00-06:00)
**Primary Function:** Environmental hazard / mini-game zone / transit chokepoint — Frogger-style crossing mini-game that gates access to Coffeeshop Quarter, Museum Mile, Canal Ring Promenade, and Roodelicht Row; mastery unlocks shortcuts

---

## 🎨 Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Bike Lane Red | #CC0000 | Primary lane markings |
| Dutch Orange | #FF6600 | Warning elements, construction |
| Tram Yellow | #FFD700 | Tram cars, caution elements |
| Asphalt Grey | #4A4A4A | Road surface base |
| Bicycle Black | #1C1C1C | Bike frames, tires |
| Sidewalk Stone | #B8B8B8 | Safe zone surfaces |
| Judgmental Blue | #003DA5 | Dutch authority elements |
| Safety Vest Orange | #FF5500 | Bike Rental Guy vest |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/bike_crossing/
├── environment/
│   ├── bike_crossing_tileset.png
│   └── bike_rental_kiosk.png
├── npcs/
│   ├── npc_bike_rental_guy.png
│   ├── npc_gerrit_philosopher.png
│   ├── npc_fallen_tourist.png
│   ├── npc_officer_vandenberg.png
│   └── npc_mama_bakfiets_detailed.png
├── objects/
│   ├── cyclists_spritesheet.png
│   ├── shamsterdam_tram.png
│   └── cargo_parade_sprites.png
├── effects/
│   └── crossing_effects.png
└── ui/
    └── crossing_ui.png
```

---

## 🚦 Sprite Sheet 1: Crossing Tileset
**Filename**: `bike_crossing_tileset.png`  
**Dimensions**: 1024 × 768 pixels  
**Tile Size**: 32 × 32 pixels

### Road Surface (Row 0)
- **Asphalt Grey**: Base road surface
- **Bike Lane Red**: Painted bike lane surface
- **Bike Lane Red Worn**: Weathered variant with tire marks
- **Crosswalk White**: Zebra crossing stripes
- **Tram Track Steel**: Raised rail surface
- **Tram Track Embedded**: Rails set into asphalt
- **Pedestrian Island Raised**: Elevated refuge platform
- **Sidewalk Stone**: Safe zone paving

### Lane Markings (Row 1)
- **Bike Arrow East**: Directional arrow
- **Bike Arrow West**: Directional arrow (opposite)
- **Bike Symbol**: White bicycle icon for lane identification
- **Stop Line**: Thick white line at intersections
- **Lane Divider Dashed**: Between-lane markers
- **Tram Warning Stripes**: Yellow/black hazard markings

### Infrastructure (Rows 2-4)
- **Traffic Light Pole**: Three-tile-high signal pole
- **Pedestrian Signal**: Button box and signal light
- **Tram Power Pole**: Four-tile-high with connector
- **Tram Overhead Wire**: Horizontal power line
- **Bike Rack Section**: Mass bicycle parking
- **Emergency Call Box**: Blue emergency phone

### Café Terrace (Row 5)
- **Café Table Round**: Small outdoor table
- **Café Chair**: Matching seating
- **Café Umbrella**: Two-tile-high shade (branded)
- **Café Railing**: Terrace boundary
- **Menu Board**: Outdoor pricing display

### Signage (Row 6)
- **Warning Sign Pedestrian**: "Cyclists Have Priority"
- **Warning Sign Tram**: "Trams Cannot Stop"
- **Bike Lane Sign**: Red circle with bike
- **No Standing Sign**: Prohibition symbol
- **I Shamsterdam Ghost Outline**: Faded letters where sign was removed

---

## 🚴 Sprite Sheet 2: Cyclist Sprites (Main)
**Filename**: `cyclists_spritesheet.png`  
**Dimensions**: 1024 × 512 pixels  
**Base Sprite Size**: 48 × 48 pixels (varies by type)

### Cyclist Types (8 rows)

**Row 0: The Commuter** (4 variants, 48×48)
- Business attire (suit jacket, skirt, or casual professional)
- Briefcase in front basket
- Phone held in one hand, NOT looking at road
- Expression: Determined, slightly annoyed
- **Animation**: Steady pedaling, 4 frames each direction

**Row 1: The Parent (Bakfiets)** (3 variants, 96×48 - wide)
- Massive cargo bike frame
- Wooden cargo box in front containing 2-3 children
- Children waving, eating snacks, or fighting
- Parent completely unbothered
- **Animation**: Smooth riding, 4 frames each direction

**Row 2: The Tourist on Rental** (4 variants, 48×48)
- Orange rental bike (distinct color)
- Uncertain posture, gripping handlebars too tight
- Camera around neck, confused expression
- Helmet (Dutch locals don't wear helmets)
- **Animation**: WOBBLY riding, 6 frames to show instability

**Row 3: The Delivery Rider** (2 variants, 64×48 - wide)
- Large insulated food delivery box on rear
- Branded vest or jacket
- Focused, deadline energy expression
- Fast-moving visual streaks
- **Animation**: Speed pedaling, 4 frames each direction

**Row 4: The Student** (3 variants, 48×48)
- Casual clothing, backpack
- Coffee cup in one hand
- Phone in other hand
- Steering with knees (literally)
- **Animation**: Distracted pedaling, 4 frames, phone glow visible

**Row 5: The Elder** (2 variants, 48×48)
- Classic upright Dutch bicycle
- Elderly person in practical clothing
- Impeccable posture, serene expression
- Moving FAST despite appearance
- **Animation**: Minimal movement, maximum speed, 2 frames (eerily smooth)

**Row 6: The Tandem Couple** (2 variants, 80×48 - wide)
- Two-person tandem bicycle
- Front rider pointing/gesturing
- Back rider clearly disagreeing
- Both slightly off-balance due to argument
- **Animation**: Arguing while cycling, 4 frames, head turns visible

**Row 7: The Dog Walker** (2 variants, 72×48 - wide)
- Standard bike with dog leash in one hand
- Dog running alongside (various breeds)
- Leash potentially tangling in wheels
- Expression: Slight panic
- **Animation**: Chaotic movement, 6 frames, dog path varies

---

## 🚋 Sprite Sheet 3: Tram Sprite
**Filename**: `shamsterdam_tram.png`  
**Dimensions**: 512 × 128 pixels  
**Sprite Size**: 256 × 64 pixels

### Tram Design
- **Style**: Amsterdam GVB tram (white/cream with red/blue accents)
- **Length**: Two connected cars
- **Features**: 
  - Windows with silhouette passengers
  - Overhead pantograph connecting to wire
  - Headlights (lit during night scenes)
  - Tram number/route display
  - Warning bell visual (when ringing)

### Animations
- **Row 0**: Moving East (2 frames, subtle track-bounce)
- **Row 1**: Moving West (2 frames, mirrored)

*Art Note*: The tram should look LARGE and UNSTOPPABLE. Players need to immediately understand this is lethal.

---

## 📦 Sprite Sheet 4: Cargo Parade Elements
**Filename**: `cargo_parade_sprites.png`  
**Dimensions**: 1024 × 256 pixels

### Mama Bakfiets (Leader) - 128×64
- Powerful Dutch woman, confident posture
- Massive cargo bike (bigger than others)
- 3 children visible in cargo box
- 2 dogs (one in box, one running alongside)
- Grocery bags visible
- Bright orange helmet
- Expression: Serene command
- **Animation**: 4 frames leading parade

### Parent Cargo Generic - 96×64 (4 variants)
- Various cargo bike designs
- 1-3 children per bike
- Different cargo: groceries, sports equipment, pets

### Delivery Cargo - 80×64 (3 variants)
- Professional cargo bikes
- Large branded boxes
- Company logos (fictional)

### Flower Delivery - 96×64 (2 variants)
- Cargo bikes OVERFLOWING with flowers
- Petals visibly trailing behind
- Tulips, roses, mixed arrangements
- Creates the "flower petals aftermath" effect

*Art Note*: When combined, these should form an IMPENETRABLE WALL of cargo bikes. The parade is beautiful and terrifying.

---

## 🦺 Sprite Sheet 5: Bike Rental Guy NPC
**Filename**: `npc_bike_rental_guy.png`  
**Dimensions**: 192 × 256 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Clothing**: Bright orange safety vest (required, clearly hated)
- **Expression**: Tired eyes that have seen too much
- **Props**: Clipboard with liability waivers
- **Background Element**: Fleet of orange rental bikes
- **Age**: 30s-40s, weathered by tourist interactions

### Animation States (4 rows)
- **Row 0: Idle** (2 frames) - Standing, slight sway, resigned posture
- **Row 1: Warning Gesture** (3 frames) - Pointing at crossing, shaking head
- **Row 2: I Told You So Shrug** (2 frames) - After player collision
- **Row 3: Impressed Nod** (2 frames) - Rare, after perfect crossing

---

## ☕ Sprite Sheet 6: Gerrit the Traffic Philosopher
**Filename**: `npc_gerrit_philosopher.png`  
**Dimensions**: 192 × 192 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Age**: 70s, Dutch elderly
- **Clothing**: Comfortable cardigan, practical trousers
- **Props**: 
  - Permanent coffee cup (always in hand)
  - Newspaper (folded, never read)
  - Small café table
- **Expression**: Slight smile of schadenfreude
- **Setting**: Seated at café terrace, watching crossing

### Animation States (3 rows)
- **Row 0: Sitting Watching** (2 frames) - Eyes following invisible cyclists
- **Row 1: Sipping Coffee** (3 frames) - Never spills despite chaos
- **Row 2: Schadenfreude Chuckle** (2 frames) - After tourist collision

---

## 😵 Sprite Sheet 7: The Fallen Tourist
**Filename**: `npc_fallen_tourist.png`  
**Dimensions**: 240 × 320 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design (American Tourist Archetype)
- **Clothing**: Cargo shorts, fanny pack, tourist t-shirt
- **Distinct Feature**: Visible bike tire mark across shirt
- **Props**: Half-eaten stroopwafel, forgotten in hand
- **Expression**: Thousand-yard stare

### Progressive States (5 rows)
- **Row 0: Visit 1 - Traumatized Coherent** - Fresh shock, staring at bikes
- **Row 1: Visit 2 - More Disheveled** - Hair messy, shirt untucked
- **Row 2: Visit 3 - Eating Numbly** - Stroopwafel, not tasting it
- **Row 3: Visit 4 - Friends with Pigeons** - Pigeons around feet
- **Row 4: Visit 5 - Island is Home** - Peaceful acceptance

---

## 👮 Sprite Sheet 8: Officer van den Berg
**Filename**: `npc_officer_vandenberg.png`  
**Dimensions**: 192 × 256 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Uniform**: Dutch police (Politie) uniform
- **Expression**: Patient, efficient, seen every excuse
- **Props**: Citation booklet, pen ready
- **Posture**: Professional, slightly bored

### Animation States (3 rows)
- **Row 0: Walking Patrol** (4 frames) - Casual patrol walk
- **Row 1: Writing Citation** (3 frames) - Taking notes, issuing fine
- **Row 2: Impressed Pause** (2 frames) - Rare, after exceptional survival

---

## 💪 Sprite Sheet 9: Mama Bakfiets (Detailed)
**Filename**: `npc_mama_bakfiets_detailed.png`  
**Dimensions**: 256 × 192 pixels  
**Sprite Size**: 128 × 64 pixels

### Close-Up Character Design
- **Build**: Strong, capable Dutch mother
- **Expression**: Serene confidence amid chaos
- **Cargo Bike Details**: 
  - Custom wooden cargo box
  - Children individually animated
  - Dogs with distinct personalities
  - Flowers overflowing from back
- **Helmet**: Bright orange, practical

### States
- **Riding Parade**: Leading cargo parade formation
- **Stopped Talking**: Post-parade interaction
- **Commanding Gesture**: "MAKE WAY!" moment

---

## ✨ Sprite Sheet 10: Effects and Particles
**Filename**: `crossing_effects.png`  
**Dimensions**: 512 × 256 pixels

### Effects

**Bicycle Bell Visual** (32×32, 4 frames)
- Musical note burst when bell rings
- Colors: Yellow/orange notes
- Appears above angry cyclists

**Collision Impact** (48×48, 4 frames, 3 variants)
- Light: Small stars
- Medium: Larger impact burst
- Heavy: Full collision explosion

**Tram Sparks** (32×32, 3 frames)
- Yellow/orange electrical sparks
- From pantograph/wire contact
- Warning visual before tram arrives

**Flower Petals** (16×16, 6 frames, 4 colors)
- Pink, red, white, yellow petals
- Drift animation
- Left behind cargo parade

**Success Glow** (64×64, 4 frames)
- Golden/green glow
- Victory celebration effect
- Appears on successful crossing

**Near Miss Whoosh** (48×24, 3 frames)
- Motion blur lines
- Shows close call with cyclist
- Creates tension feedback

---

## 🎮 Sprite Sheet 11: UI Elements
**Filename**: `crossing_ui.png`  
**Dimensions**: 256 × 256 pixels

### Interface Elements

**Lane Indicator** (200×24)
- Shows current position in crossing
- Highlights danger zones
- Color-coded by difficulty

**Tram Warning Icon** (48×48)
- Animated tram symbol
- Flashes when tram approaching
- Audio sync indicator

**Cargo Parade Warning** (96×32)
- "CARGO PARADE INCOMING" text
- Bakfiets silhouettes
- 5-second countdown

**Crossing Progress Bar** (200×16)
- Start to finish visualization
- Current position marker
- Zone color coding

**Hit Counter** (100×24)
- Shows collision count
- Affects final score/buff

**Perfect Crossing Badge** (64×64)
- Golden trophy/star
- "DODGE MASTER" text
- Achievement unlock visual

---

## 🏪 Sprite Sheet 12: Rental Bike Kiosk
**Filename**: `bike_rental_kiosk.png`  
**Dimensions**: 256 × 192 pixels

### Structure
- Small rental booth/kiosk
- "BIKE RENTAL" sign (in Dutch: "FIETS VERHUUR")
- Price board: "€15/DAG"
- Orange rental bikes lined up behind
- Liability waiver stack visible

---

## 🎬 Animation Specifications

*Sprite positions within sheets follow the row layouts specified per sheet above; pixel coordinates set at sheet layout.*

### Cyclist Pedaling Cycles (Sheet 2):
- **Duration:** 0.4-0.67 seconds per cycle (6-10 FPS, speed varies by type)
- **Frames:** 2-6 per type (Commuter/Parent/Delivery/Student/Tandem: 4; Tourist/Dog Walker: 6; Elder: 2)
- **Pattern:** Frame 1 → N → loop, per direction row
- **Trigger:** Constant while cyclist active in lane
- **Purpose:** Players must read cyclist speed visually — frame rate IS the gameplay telegraph
- **Audio Sync:** Bell ring on aggressive types when player is in lane
- **Mobile Optimization:** Pool of 24 sprites, 12 active maximum

### Tram Movement (Sheet 3):
- **Duration:** 0.5 seconds per cycle (4 FPS, slow and deliberate)
- **Frames:** 2 per direction (subtle track-bounce)
- **Pattern:** Frame 1 → 2 → loop
- **Trigger:** Timer — every 45 seconds per track, Track 2 offset by 22 seconds
- **Purpose:** Communicates lethal, unstoppable mass
- **Audio Sync:** Tram bell 3 seconds before arrival; sparks visual precedes
- **Mobile Optimization:** None needed (single large sprite)

### Cargo Parade Wall (Sheet 4):
- **Duration:** 10 seconds on-screen, every 90 seconds
- **Frames:** 4 (Mama Bakfiets lead cycle; parade at 4 FPS)
- **Pattern:** Formation scrolls as impenetrable wall, frames 1 → 4 → loop
- **Trigger:** Timer (90-second interval), 5-second UI warning first
- **Purpose:** Beautiful and terrifying spectacle; forces player to wait
- **Audio Sync:** "CARGO PARADE INCOMING" warning audio at T-5s; children singing, bell cacophony during
- **Mobile Optimization:** Parade rendered as combined formation, not individual physics bodies

### Collision Effects (Sheet 10):
- **Duration:** 0.33-0.4 seconds (10-12 FPS, snappy feedback)
- **Frames:** 4 (3 severity variants: light stars / medium burst / heavy explosion)
- **Pattern:** Frame 1 → 4 → hold last frame briefly → clear
- **Trigger:** Player collision with cyclist/tram/parade
- **Purpose:** Immediate, readable failure feedback
- **Audio Sync:** Impact sound + Dutch reaction line on frame 1
- **Mobile Optimization:** Single effect instance at a time

### NPC Idle Loops (Sheets 5-9):
- **Duration:** 2-4 seconds per cycle (0.25-0.5 FPS, subtle breathing)
- **Frames:** 2-3 per state row
- **Pattern:** Frame 1 → 2 → 1 → loop
- **Trigger:** Constant; reaction states (I Told You So, Schadenfreude Chuckle, Impressed Nod) trigger on player crossing outcomes per state rows above
- **Purpose:** Ambient life; NPC reactions are the crossing's comedy scoreboard
- **Audio Sync:** None (dialogue-driven)
- **Mobile Optimization:** None needed

### UI Warnings (Sheet 11):
- **Duration:** 0.25 seconds per frame (4 FPS, visible warnings)
- **Frames:** Tram Warning Icon flashes; Cargo Parade Warning counts down 5 seconds
- **Pattern:** Flash on/off loop while threat active
- **Trigger:** Tram approach (T-3s) / parade approach (T-5s)
- **Purpose:** Off-screen threat telegraphing
- **Audio Sync:** Warning icons are the visual mirrors of the bell/parade audio cues
- **Mobile Optimization:** None needed

### Animation Frame Rates (CRITICAL)

| Element | FPS | Notes |
|---------|-----|-------|
| Cyclists | 6-10 | Speed varies by type |
| Tram | 4 | Slow, deliberate, unstoppable |
| Cargo Parade | 4 | Wall of motion |
| Collision Effects | 10-12 | Snappy feedback |
| NPC Idle | 0.25-0.5 | Subtle breathing |
| UI Elements | 4 | Visible warnings |

*Art Note*: Frame rates are CRITICAL for gameplay timing. Players need to read cyclist speeds visually.

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cyclist outline set | set at sheet layout | matches cyclist sprites | High-contrast silhouette variants for all 8 cyclist types — speed class readable by outline weight, not color |
| Tram silhouette | set at sheet layout | 256×64 | Solid high-contrast tram shape with bold warning border |
| Pedestrian island highlight | set at sheet layout | 32×32 | Enhanced-visibility safe zone tile outline |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static warning icons | set at sheet layout | 48×48 | Non-flashing versions of Tram Warning Icon and Cargo Parade Warning (steady color fill instead of flash) |
| Reduced near-miss effect | set at sheet layout | 48×24 | Single-frame motion line variant, no blur strobing |
| Slower mode support | n/a | n/a | Mini-game slower mode available in settings (per location spec); all animation loops must read correctly at 0.7× speed |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bicycle Bell Visual | Sheet 10 | 32×32 | Musical note burst — already the visual mirror of the bell audio; REQUIRED for offscreen threats |
| Tram Warning Icon | Sheet 11 | 48×48 | Visual for tram bell (3-second warning) |
| Cargo Parade Warning | Sheet 11 | 96×32 | Visual for "CARGO PARADE INCOMING" audio (5-second countdown) |
| Near Miss Whoosh | Sheet 10 | 48×24 | Visual for near-miss wind/gasp audio |

### Colorblind Considerations:
- Lane difficulty color coding (Lane Indicator, Crossing Progress Bar) must be doubled with zone patterns/shapes, not color alone
- Cyclist speed classes distinguishable by silhouette and sprite width, not only palette
- Touch zones minimum 44×44 pixels for all interactive elements; swipe threshold 20 pixels; one-handed play must be possible

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC (fallback PVRTC 4BPP); cyclist sheet and UI need higher-quality setting for speed readability
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for tram and UI (detail-critical for timing gameplay)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| bike_crossing_environment | tileset, kiosk | 1024x1024 |
| bike_crossing_traffic | cyclists, tram, cargo parade | 1024x1024 |
| bike_crossing_characters | NPC sheets 5-9 | 1024x1024 |
| bike_crossing_effects | effects, UI | 512x512 |

*(5 atlases max, 1024px each per mini-game budget; max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full cyclist pool (12 active), all particle effects, tram sparks, flower petals |
| Medium | Reduced particle density, 8-10 active cyclists, simplified petal drift |
| Low | Minimal particles, reduced cyclist variants, static café terrace (baseline LOD level 2 per core data) |

### Performance Targets:
- **Target FPS:** 60 (non-negotiable for mini-game timing)
- **Max Draw Calls:** Under 50
- **Memory Footprint:** Under 50 MB
- **Particle Limit:** 80

### Performance Notes:
- Cyclist pool: 24 sprites, 12 active maximum
- Touch zone requirements: minimum touch target 44×44 pixels, swipe threshold 20 pixels, one-handed play must be possible
- Pixel-perfect collision detection required for fairness; audio sync must be precise for warning sounds

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: TileMap (crossing tileset), AnimatedSprite2D (cyclists, tram, NPCs), CPUParticles2D (petals, sparks — not GPU), CanvasLayer (mini-game UI)
- Special systems: lane spawner state machine (normal / rush hour / night patterns), 90-second cargo parade timer, 45-second tram timers with 22-second offset, Fallen Tourist progressive-state tracker (5 visits), tutorial mode with visual indicators and forgiving hitboxes

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Tram Warning Icon + Tram Sparks | Tram bell | 3 seconds before tram arrival |
| Cargo Parade Warning | "CARGO PARADE INCOMING" | 5 seconds before parade |
| Bicycle Bell Visual | Angry bell ring | On cyclist bell frame 1 |
| Collision Impact | "Ding ding!" / crash + Dutch swearing (by severity) | On impact frame 1 |
| Near Miss Whoosh | Whoosh + gasp | On near-miss detection |
| Success Glow | Victory flourish / triumphant fanfare | On reaching north sidewalk |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Cargo Cult | Cargo parade sheet, Mama Bakfiets detailed | Ride with the parade; unlocks Rooftop Route + "Bicycle Empathy" |
| The Stay Away Campaign | Crossing tileset, NPC area | Pamphlet distributor stands at crossing |
| Fabergé Egg Hunt | Full crossing scene | Must cross east to reach Museum Mile |
| Canal Bike Recovery | North exit tiles | North exit leads to diving spot |
| The Bicycle Gauntlet | All traffic sheets | Harder crossing variant triggered by NPC challenge |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Canal Ring Promenade (north) | Shared sidewalk/canal edge tiles | Walk-off north sidewalk |
| Roodelicht Row (south) | Shared sidewalk tiles, kiosk visible | Walk-off south sidewalk |
| Museum Mile (east) | Road continuation tiles | Walk-off east |
| Coffeeshop Quarter (west) | Road continuation tiles | Walk-off west |
| Café de Schaamte (northeast) | Café terrace tiles | Terrace-adjacent entry |
| Shamsterdam Bike Rental | Kiosk sheet (Sheet 12), orange rental bikes | Adjacent south-side shop; rental bypasses mini-game |
| Voetgangerstunnel | Tileset stairs | Underground shortcut unlocked after 10 crossings |

### Cross-Reference: Related Assets
- **Connects to**: Shamsterdam city tileset (road consistency), Dutch NPC style guide (cyclist designs), UI framework (progress bars, warnings)
- **Unique to this location**: All cyclist variants, tram sprite, cargo parade formation, mini-game UI elements, crossing-specific effects

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Urban chaos crystallized — modern Dutch infrastructure meets tourist nightmare"
- **Color Mood:** Clean red bike lanes, efficient tram yellow, and judgmental blue authority against grey asphalt — order that reads as hostility
- **Lighting:** See Lighting Requirements below — bright Dutch daylight, Instagram-worthy golden hour, cool blue night with light pools
- **Texture:** Clean and well-maintained surfaces (the danger is the traffic, not decay); worn red paint and tire marks show the volume of cyclists

### Visual Identity
This is **urban chaos crystallized**—a six-lane bicycle intersection that serves as Shamsterdam's central transit point. The aesthetic is modern Dutch infrastructure meets tourist nightmare: clean red bike lanes, efficient tram tracks, and a constant flow of cyclists who absolutely do not care about pedestrians.

### Key Visual Themes
- **Dutch Efficiency**: Clean lines, clear markings, excellent infrastructure
- **Tourist Hostility**: Every visual element says "you don't belong here"
- **Movement Everywhere**: Nothing is static—bikes, trams, bells, all in motion
- **Cultural Clash**: American pedestrian expectations vs Dutch cycling reality

### Lighting Requirements

**Daytime**
- Bright, clear Dutch sky
- Sharp shadows from overhead sun
- Clean, efficient aesthetic

**Evening/Golden Hour**
- Instagram-worthy death trap
- Orange/gold tones
- Long shadows across crossing

**Night**
- Street light pools (12 points)
- Tram headlights (moving)
- Bike lights (fast-moving dots)
- Café terrace warm glow
- Overall cool blue ambient

### Environmental Storytelling:
- The "I Shamsterdam" ghost outline — faded letters where the famous sign was removed because tourists wouldn't stop blocking traffic for photos
- Bike racks with bikes chained since the 1970s; the Fallen Tourist progressively making the pedestrian island his home
- Warning signs ("Cyclists Have Priority", "Trams Cannot Stop") that tell the whole satirical story without dialogue

### Character Integration Notes:
- NPCs are stationary observers around the chaos (Gerrit on terrace, Rental Guy at kiosk, Fallen Tourist on island); Officer van den Berg roams
- Cyclists are the "enemies" — silhouette and width must telegraph speed class at a glance
- Fallen Tourist uses progressive state rows tied to visit count

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Cargo Parade Wall** - Impenetrable mass of bakfiets
2. **Perfect Crossing Victory** - Player on north side, chaos behind
3. **Tram Near Miss** - Split-second survival
4. **Fallen Tourist Progression** - Same character getting worse
5. **Gerrit's Rare Approval** - Actually impressed expression

### Quote Potential:
- "I did warn you. Everyone warns you. No one listens."
- "You're going to WALK? Across THAT?"
- "The children in the cargo bikes... they LAUGHED at me."
- "Think of them as nature. You don't fight nature."
- "This is a bicycle city. Please adjust expectations."

### TikTok Potential
- "POV: You tried to cross the street in Amsterdam"
- Speed runs of perfect crossing
- Compilation of collision fails
- Cargo parade reactions

---

## 📋 Required PNG Files (12 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | bike_crossing_tileset.png | 1024x768 |
| 2 | cyclists_spritesheet.png | 1024x512 |
| 3 | shamsterdam_tram.png | 512x128 |
| 4 | cargo_parade_sprites.png | 1024x256 |
| 5 | npc_bike_rental_guy.png | 192x256 |
| 6 | npc_gerrit_philosopher.png | 192x192 |
| 7 | npc_fallen_tourist.png | 240x320 |
| 8 | npc_officer_vandenberg.png | 192x256 |
| 9 | npc_mama_bakfiets_detailed.png | 256x192 |
| 10 | crossing_effects.png | 512x256 |
| 11 | crossing_ui.png | 256x256 |
| 12 | bike_rental_kiosk.png | 256x192 |

**Total Estimated Memory:** ~50 MB maximum (location performance budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `bike_crossing_tileset.png` (1024x768)
- [ ] `cyclists_spritesheet.png` (1024x512)
- [ ] `shamsterdam_tram.png` (512x128)
- [ ] `cargo_parade_sprites.png` (1024x256)
- [ ] `npc_bike_rental_guy.png` (192x256)
- [ ] `npc_gerrit_philosopher.png` (192x192)
- [ ] `npc_fallen_tourist.png` (240x320)
- [ ] `npc_officer_vandenberg.png` (192x256)
- [ ] `npc_mama_bakfiets_detailed.png` (256x192)
- [ ] `crossing_effects.png` (512x256)
- [ ] `crossing_ui.png` (256x256)
- [ ] `bike_rental_kiosk.png` (256x192)

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
- **Documentation:** Animation timing reference sheet (frame rates are gameplay-critical — see Animation Specifications)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Cyclist speed classes read clearly at gameplay speed; tram reads as lethal at first glance; cargo parade forms a seamless wall
- [ ] Accessibility visual alternatives included for all audio cues (bell, tram warning, parade warning, near miss)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (Dutch efficiency as tourist hostility)
- [ ] Hidden areas/interactions have discoverable visual cues (tunnel stairs, "I Shamsterdam" ghost outline, kiosk)
- [ ] Mobile performance optimized (CPU particles, atlas limits respected, 12-cyclist active cap)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (lane indicators, difficulty zones)
- [ ] Social media viral potential maximized in composition choices (parade wall, near-miss framing)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam only (tram styled after Amsterdam GVB as visual reference) |
| Cultural Specificity | ✅ | Dutch cycling culture, bakfiets, tram infrastructure, Dutch directness |
| Satirical Targets Appropriate | ✅ | Tourist overconfidence and "bike-friendly" marketing — not Dutch locals |
| Seedy Underbelly Present | ✅ | Fines-as-revenue, escort service upsell, the crossing as institutionalized hazing |
| Gameplay Value Established | ✅ | Frogger mini-game, central hub gating 4+ districts, buffs/debuffs, shortcuts |
| Technical Feasibility | ✅ | Sprite pooling, atlas budget, pre-defined lane patterns documented |
| Mobile Performance Budget | ✅ | 60 FPS locked, <50 draw calls, <50 MB, 80 particles |
| Accessibility Features | ✅ | Visual audio cues for all threats, slower mode, 44px touch zones |
| No Crypto Elements | ✅ | All transactions in Euros |
| Social Media Integration | ✅ | 5 screenshot moments + TikTok formats identified |

---

**END OF ASSET REQUIREMENTS**

*Central Shamsterdam Bike Crossing: Where Dutch cycling efficiency meets American pedestrian overconfidence in a Frogger-style battle for survival. The bicycles don't stop. They never stop.*
