# Central Shamsterdam Bike Crossing - Complete PNG Asset Requirements

*Artist Reference Document for the Bicycle Thunderdome Frogger Mini-Game*

**Location ID**: `shamsterdam_bike_crossing_thunderdome_01`  
**Priority**: HIGH (Central Hub, Mini-Game Location, Required for All Shamsterdam Traversal)  
**Total Sheets Required**: 12  
**Mobile Optimization**: CRITICAL - 60 FPS required for timing-based gameplay

---

## Art Direction Summary

### Visual Identity
This is **urban chaos crystallized**—a six-lane bicycle intersection that serves as Shamsterdam's central transit point. The aesthetic is modern Dutch infrastructure meets tourist nightmare: clean red bike lanes, efficient tram tracks, and a constant flow of cyclists who absolutely do not care about pedestrians.

### Key Visual Themes
- **Dutch Efficiency**: Clean lines, clear markings, excellent infrastructure
- **Tourist Hostility**: Every visual element says "you don't belong here"
- **Movement Everywhere**: Nothing is static—bikes, trams, bells, all in motion
- **Cultural Clash**: American pedestrian expectations vs Dutch cycling reality

### Color Palette

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

## SHEET 1: Crossing Tileset
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

## SHEET 2: Cyclist Sprites (Main)
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

## SHEET 3: Tram Sprite
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

## SHEET 4: Cargo Parade Elements
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

## SHEET 5: Bike Rental Guy NPC
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

## SHEET 6: Gerrit the Traffic Philosopher
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

## SHEET 7: The Fallen Tourist
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

## SHEET 8: Officer van den Berg
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

## SHEET 9: Mama Bakfiets (Detailed)
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

## SHEET 10: Effects and Particles
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

## SHEET 11: UI Elements
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

## SHEET 12: Rental Bike Kiosk
**Filename**: `bike_rental_kiosk.png`  
**Dimensions**: 256 × 192 pixels

### Structure
- Small rental booth/kiosk
- "BIKE RENTAL" sign (in Dutch: "FIETS VERHUUR")
- Price board: "€15/DAG"
- Orange rental bikes lined up behind
- Liability waiver stack visible

---

## Lighting Requirements

### Daytime
- Bright, clear Dutch sky
- Sharp shadows from overhead sun
- Clean, efficient aesthetic

### Evening/Golden Hour
- Instagram-worthy death trap
- Orange/gold tones
- Long shadows across crossing

### Night
- Street light pools (12 points)
- Tram headlights (moving)
- Bike lights (fast-moving dots)
- Café terrace warm glow
- Overall cool blue ambient

---

## Animation Frame Rates (CRITICAL)

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

## Social Media Viral Moments

### Key Screenshot Opportunities
1. **The Cargo Parade Wall** - Impenetrable mass of bakfiets
2. **Perfect Crossing Victory** - Player on north side, chaos behind
3. **Tram Near Miss** - Split-second survival
4. **Fallen Tourist Progression** - Same character getting worse
5. **Gerrit's Rare Approval** - Actually impressed expression

### TikTok Potential
- "POV: You tried to cross the street in Amsterdam"
- Speed runs of perfect crossing
- Compilation of collision fails
- Cargo parade reactions

---

## Technical Specifications

### File Format
- **Format**: PNG-24 with alpha transparency
- **Color Space**: sRGB
- **Resolution**: 72 DPI
- **Compression**: Lossless

### Mobile Optimization (CRITICAL)
- **Cyclist Pool**: 24 sprites, 12 active maximum
- **Texture Atlases**: 5 max, 1024px each
- **Draw Calls**: Under 50
- **Memory**: Under 50MB
- **Target FPS**: 60 (non-negotiable for mini-game)

### Touch Zone Requirements
- Minimum touch target: 44×44 pixels
- Swipe threshold: 20 pixels
- One-handed play must be possible

---

## Cross-Reference: Related Assets

### Connects To
- Shamsterdam city tileset (road consistency)
- Dutch NPC style guide (cyclist designs)
- UI framework (progress bars, warnings)

### Unique to This Location
- All cyclist variants
- Tram sprite
- Cargo parade formation
- Mini-game UI elements
- Crossing-specific effects

---

**END OF ASSET REQUIREMENTS**

*Central Shamsterdam Bike Crossing: Where Dutch cycling efficiency meets American pedestrian overconfidence in a Frogger-style battle for survival. The bicycles don't stop. They never stop.*
