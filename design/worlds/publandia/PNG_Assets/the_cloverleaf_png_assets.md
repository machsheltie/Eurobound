# The Cloverleaf (Eternal Roundabout) - Complete PNG Asset Requirements

## 📋 Overview
The Cloverleaf is Eurobound's most visually ambitious set-piece: an impossibly large Irish roundabout where every exit leads back to the beginning, populated by a functioning society of the trapped — Patrick and Margaret's 1987 wedding van still circling toward the Cliffs of Moher, a democratic tour bus community, a food truck economy, and Seán, who knows the exit and never takes it. This document specifies every PNG asset for the roundabout, its eight resident vehicles, effects, and UI. Its satirical essence in a sentence: American tourist impatience meets Irish "it'll be grand" acceptance, and the only way out is to slow down.

**Location ID:** `publandia_outskirts_cloverleaf_roundabout_01`  
**Theme:** Eternal circulation, absurdist society, American impatience vs. Irish acceptance  
**Zone:** Publandia Outskirts, 1km east of Paddy's Premium Motors  
**Hours:** Always accessible (24/7 — the roundabout never closes; auto-triggered when driving east from Paddy's, cannot be avoided)  
**Primary Function:** Major set-piece / driving puzzle / absurdist ecosystem — quest "The Cloverleaf of Confusion" with binary path choice (Path A: escape by slowing down, 20-30 min; Path B: adapt to roundabout life, 3+ in-game days); lane merge and food truck intercept minigames  
**Type:** Major Set-Piece - Complex Multi-Vehicle Scene  
**Art Style:** EarthBound oblique view, stylized simplification over photorealism

---

## 🎨 Color Palette

| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| Asphalt Grey | `#696969` | 105, 105, 105 | Road surface |
| Road Marking White | `#FFFFFF` | 255, 255, 255 | Lane markings, text |
| Warning Yellow | `#FFD700` | 255, 215, 0 | Signs, caution elements |
| Exit Green | `#228B22` | 34, 139, 34 | Exit signage |
| 1987 Van Cream | `#FFFDD0` | 255, 253, 208 | Wedding van base (faded) |
| Van Weathered Yellow | `#F5DEB3` | 245, 222, 179 | Van aging tint |
| Tour Bus Red | `#DC143C` | 220, 20, 60 | Double-decker bus |
| Food Truck Orange | `#FF8C00` | 255, 140, 0 | Cloverleaf Kitchen |
| Irish Green | `#228B22` | 34, 139, 34 | Center island, fields |
| Sky Grey | `#A9A9A9` | 169, 169, 169 | Overcast sky |
| Skeleton Bone | `#E3DAC9` | 227, 218, 201 | Margaret |
| Rain Blue | `#ADD8E6` | 173, 216, 230 | Rain particles |
| Rust Brown | `#8B4513` | 139, 69, 19 | Seán's Micra, tractor |
| Wedding White | `#FFFAFA` | 255, 250, 250 | Margaret's dress |

---

## 📁 File Structure

```
assets/sprites/locations/publandia/cloverleaf_roundabout/
├── environment/
│   ├── roundabout_base_1024.png
│   ├── lane_markings_overlay.png
│   ├── center_island_512.png
│   ├── celtic_monument.png
│   ├── gift_shop_closed.png
│   ├── exit_signs_sheet.png
│   ├── approach_road.png
│   ├── background_fields.png
│   └── background_sky.png
├── vehicles/
│   ├── wedding_van_1987/
│   │   ├── wedding_van_base.png
│   │   ├── wedding_van_details.png
│   │   ├── patrick_driver.png
│   │   ├── margaret_skeleton.png
│   │   └── tin_cans_dragging.png
│   ├── tour_bus/
│   │   ├── tour_bus_base.png
│   │   ├── tour_bus_passengers.png
│   │   └── orla_with_clipboard.png
│   ├── food_truck/
│   │   ├── food_truck_base.png
│   │   ├── food_truck_window_open.png
│   │   └── chef_maeve.png
│   ├── local_car_sean/
│   │   ├── nissan_micra_1999.png
│   │   └── sean_driver.png
│   ├── learner_car/
│   │   ├── learner_car_base.png
│   │   ├── l_plates.png
│   │   ├── brenda_instructor.png
│   │   └── kevin_student.png
│   ├── family_van/
│   │   ├── people_carrier_rental.png
│   │   └── murphy_family_silhouettes.png
│   ├── farmer_tractor/
│   │   ├── tractor_ancient.png
│   │   ├── sheep_trailer.png
│   │   └── padraig_driver.png
│   └── bros_rental/
│       ├── rental_car_base.png
│       └── bros_interior_view.png
├── effects/
│   ├── rain_particles.png
│   ├── exhaust_puffs.png
│   ├── road_spray.png
│   ├── windshield_wiper_overlay.png
│   └── headlight_glow.png
└── ui/
    ├── circle_counter.png
    ├── days_counter.png
    ├── gps_recalculating.png
    ├── lane_indicator.png
    └── food_truck_schedule.png
```

---

## 🛣️ Sprite Sheet 1: Roundabout Base

**File:** `roundabout_base_1024.png`  
**Dimensions:** 1024x1024 pixels  
**View Angle:** Top-down oblique (EarthBound style)

### Layout Grid

```
┌─────────────────────────────────────────────┐
│                                             │
│     ┌─────────────────────────────┐        │
│     │                             │        │
│   ←─┤    CENTER ISLAND (GRASS)    ├──→     │
│     │    + Celtic Monument        │        │
│     │    + Gift Shop              │        │
│     └─────────────────────────────┘        │
│                                             │
│  ╔═══════════════════════════════════════╗ │
│  ║ INNER LANE (Fast)                     ║ │
│  ╠═══════════════════════════════════════╣ │
│  ║ MIDDLE LANE (Default)                 ║ │
│  ╠═══════════════════════════════════════╣ │
│  ║ OUTER LANE (Slow)                     ║ │
│  ╚═══════════════════════════════════════╝ │
│                                             │
│   EXIT 1    EXIT 2    EXIT 3    EXIT 4     │
│     ↓         ↓         ↓         ↓        │
└─────────────────────────────────────────────┘
```

### Elements to Include

| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Center Island | Center | 300x300px | Green grass with monument |
| Inner Lane | 50px from center | 60px wide | Darker asphalt, worn |
| Middle Lane | 110px from center | 70px wide | Standard asphalt |
| Outer Lane | 180px from center | 80px wide | Lighter asphalt |
| Lane Markings | Between lanes | 4px wide, dashed | White, faded in places |
| Merge Zones | 6 entry points | 80x120px each | Yield markings |

### Road Surface Details
- **Texture**: Wet asphalt appearance (rain-slick)
- **Tire marks**: Visible at merge zones and around 1987 van's regular path
- **Faded areas**: Lane markings worn near middle lane (37 years of the van)
- **Puddle reflections**: Small reflective patches scattered

---

## 🏝️ Sprite Sheet 2: Center Island

**File:** `center_island_512.png`  
**Dimensions:** 512x512 pixels

### Elements

| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Grass Base | Full area | 300x300px | Perfectly manicured Irish green |
| Celtic Monument | Center | 80x120px | Stone cross, weathered |
| Gift Shop | North side | 60x40px | Tiny building, "Opening Soon" sign |
| Bench | East side | 30x15px | Wooden, never used |
| Information Board | South side | 40x30px | Faded maps, outdated info |

### Celtic Monument Details
- **Style**: Traditional Irish high cross
- **Condition**: Ancient-looking, moss-covered base
- **Mystery**: Nobody knows who built it or when
- **Sign**: Plaque reading "CLOVERLEAF MONUMENT - EST. ???"

### Gift Shop Details
- **Building**: Tiny stone cottage
- **Sign**: "GIFT SHOP - OPENING SOON (Since 1994)"
- **Windows**: Dusty, nothing visible inside
- **Door**: Padlocked with rusty chain

---

## 🚐 Sprite Sheet 3: The 1987 Wedding Van (HERO ASSET)

**File:** `wedding_van_1987.png`  
**Dimensions:** 256x128 pixels  
**Priority:** HIGH (Most iconic visual in the game)

### Vehicle Base
| Element | Description |
|---------|-------------|
| Model | 1987 Ford Transit Connect |
| Color | Cream faded to yellow (#FFFDD0 → #F5DEB3) |
| Condition | Well-maintained but aged |
| Rust | None (Patrick maintains it lovingly) |

### Exterior Details

| Detail | Position | Description |
|--------|----------|-------------|
| "JUST MARRIED 1987" | Rear window | Faded shoe polish, barely readable |
| Tin Cans | Rear bumper | 6-8 cans, worn to nubs, still dragging |
| Anniversary Banner | Side | "37 YEARS" hand-painted |
| Dead Flowers | Dashboard visible | Dried bouquets in vases |
| Clean Windows | All | Lovingly maintained despite age |

### Patrick (Driver)

| Feature | Description |
|---------|-------------|
| Age | 70s (was 30s when entered) |
| Clothing | Original wedding suit (preserved) |
| Hair | Grey, thinning, neatly combed |
| Expression | Warm, genuine, slight wistfulness |
| Animation | Waving hand (6 frames, 1.5s loop) |
| Position | Driver's seat, slightly turned toward Margaret |

### Margaret (Passenger) - TREAT WITH DIGNITY

| Feature | Description |
|---------|-------------|
| State | Skeleton |
| Clothing | Wedding dress (faded white, remarkably preserved) |
| Accessories | Dried flower crown, wedding ring on finger bone |
| Pose | Seated, "looking" out passenger window |
| Expression | Peaceful (as peaceful as a skeleton can look) |
| Animation | Subtle wind sway (4 frames, 2s loop) |

**CRITICAL ART DIRECTION**: Margaret must be rendered with dignity and respect. She is part of a love story, NOT a gross-out gag. Her pose should suggest peaceful rest, not horror. The dress should be beautiful despite its age. The flower crown should look delicate, not macabre.

### Animation States

| State | Frames | Duration | Trigger |
|-------|--------|----------|---------|
| Default Loop | 1 | Static | Always |
| Patrick Waving | 6 | 1.5s | First encounter, passing bros |
| Margaret Sway | 4 | 2s | Wind effect, continuous subtle |

---

## 🚌 Sprite Sheet 4: Tour Bus Community

**File:** `tour_bus.png`  
**Dimensions:** 256x256 pixels

### Vehicle Base
| Element | Description |
|---------|-------------|
| Type | Double-decker tour bus |
| Color | Classic red (#DC143C) |
| Condition | Lived-in, functional |
| Windows | Passengers visible, laundry hanging from some |

### Exterior Details

| Detail | Position | Description |
|--------|----------|-------------|
| "CLOVERLEAF TOURS" | Side | Faded original name |
| Community Banner | Top | "TOUR BUS COMMUNITY - EST. 2012" |
| Democratic Banner | Front | "DEMOCRATIC SINCE 2013" |
| Garden Boxes | Roof edge | Small plants growing |
| Laundry Lines | Between windows | Clothes drying |

### Visible Passengers (Silhouettes)
- ~30 passengers visible through windows at various activities
- Some sleeping, some reading, some waving
- One window shows a "COUNCIL MEETING" sign

### Orla Brennan (Leader)

| Feature | Description |
|---------|-------------|
| Age | 55 |
| Clothing | Comfortable travel clothes, official badge |
| Badge | "CLOVERLEAF COMMUNITY COUNCIL" |
| Accessories | Clipboard, whistle, schedule book |
| Expression | Organized, welcoming, practical |
| Position | Standing at front entrance, gesturing |

---

## 🚚 Sprite Sheet 5: Food Truck

**File:** `food_truck.png`  
**Dimensions:** 192x128 pixels

### Vehicle Base
| Element | Description |
|---------|-------------|
| Type | Classic food truck |
| Color | Orange (#FF8C00) with white accents |
| Name | "THE CLOVERLEAF KITCHEN" |
| Condition | Operational, greasy but loved |

### Exterior Details

| Detail | Position | Description |
|--------|----------|-------------|
| Menu Board | Side | Prices visible (see menu in main doc) |
| Serving Window | Side (open) | Shows interior kitchen |
| Steam Vent | Roof | Constant steam emission |
| Grease Stains | Various | Around serving window |
| Lights | Under awning | Warm welcoming glow |

### Chef Maeve

| Feature | Description |
|---------|-------------|
| Age | 40s |
| Clothing | Chef whites (stained), apron |
| Hair | Pulled back, under bandana |
| Expression | Tired but determined |
| Position | At serving window |

---

## 🚗 Sprite Sheet 6: The Local Who Knows (Seán)

**File:** `local_car_sean.png`  
**Dimensions:** 128x64 pixels

### Vehicle
| Element | Description |
|---------|-------------|
| Model | 1999 Nissan Micra |
| Color | Green (#228B22), heavily rusted |
| Condition | Barely functional, somehow still running |
| Rust | Extensive, especially wheel wells |

### Seán

| Feature | Description |
|---------|-------------|
| Age | 60s |
| Clothing | Flat cap, wool jumper |
| Expression | Serene, knowing, slightly ominous |
| Position | Driver's seat, relaxed |
| Animation | Occasional knowing nod |

---

## 🚙 Sprite Sheet 7: Learner Car

**File:** `learner_car.png`  
**Dimensions:** 128x64 pixels

### Vehicle
| Element | Description |
|---------|-------------|
| Type | Compact sedan (driving school) |
| Color | White with "APEX DRIVING SCHOOL" decal |
| L-Plates | Front and rear, oversized |
| Dual Controls | Visible through windshield |

### Brenda (Instructor)

| Feature | Description |
|---------|-------------|
| Age | 45 |
| Expression | Increasingly haunted |
| Position | Passenger seat, gripping door handle |
| Animation | Occasional flinch |

### Kevin (Student)

| Feature | Description |
|---------|-------------|
| Age | 17 |
| Expression | Perpetually nervous |
| Position | Driver's seat, hunched over wheel |
| Animation | White-knuckle grip on wheel |

---

## 🚐 Sprite Sheet 8: Murphy Family Van

**File:** `family_van.png`  
**Dimensions:** 192x96 pixels

### Vehicle
| Element | Description |
|---------|-------------|
| Type | Rental people carrier |
| Color | Silver |
| Condition | New rental, pristine |
| Luggage | Roof rack overloaded |

### Visible Through Windows
- Da: Frustrated expression, gripping wheel
- Ma: Zen acceptance, reading book
- Kids (x3): Various states of boredom/excitement
- Gran: Asleep in back, mouth open

---

## 🚜 Sprite Sheet 9: Farmer's Tractor

**File:** `farmer_tractor.png`  
**Dimensions:** 192x128 pixels

### Vehicle
| Element | Description |
|---------|-------------|
| Type | Ancient tractor (60s model) |
| Color | Rust red (#8B4513), faded |
| Condition | Miraculously running |
| Attachment | Sheep trailer |

### Padraig

| Feature | Description |
|---------|-------------|
| Age | 70s |
| Clothing | Flat cap, overalls, wellies |
| Expression | Unbothered, patient |
| Position | Tractor seat, hands loosely on wheel |

### Sheep Trailer
- 4-5 sheep visible
- Some eating hay
- One looking directly at camera

---

## 🚗 Sprite Sheet 10: Bros' Rental Car

**File:** `bros_rental.png`  
**Dimensions:** 128x64 pixels

### Vehicle
| Element | Description |
|---------|-------------|
| Type | Economy rental (Paddy's Premium Motors) |
| Color | Generic silver |
| Condition | Already showing wear (bros driving) |
| Damage | Minor scratches from merge attempts |

### Interior View (For Driving Sequences)
- Lord Pilsner: Driver, frustrated expression
- Chadwick: Backseat, phone out filming
- Bradley: Passenger, contemplative/stressed

---

## 🪧 Sprite Sheet 11: Exit Signs

**File:** `exit_signs_sheet.png`  
**Dimensions:** 256x256 pixels

### Sign Types (6 exits)

| Exit | Sign Text | Subtext |
|------|-----------|---------|
| Exit 1 | "→ EAST" | "Scenic Route" |
| Exit 2 | "↘ SOUTHEAST" | "Country Roads" |
| Exit 3 | "↙ SOUTHWEST" | "Return to Town" |
| Exit 4 | "← WEST" | "Coastal Drive" |
| Exit 5 | "↖ NORTHWEST" | "Sheep Crossing" |
| Exit 6 | "↑ NORTH" | "Cliffs of Moher" |

### Sign Design
- **Style**: Standard Irish road sign (green background, white text)
- **Condition**: Faded, some bent, one has bullet holes (local tradition)
- **Additional sign**: "ALL EXITS LEAD SOMEWHERE" (philosophical vandalism)

---

## ✨ Effects Sprites

### Rain Particles
**File:** `rain_particles.png`  
**Dimensions:** 64x64 pixels

- 8 particle variations
- Light drizzle style
- Semi-transparent (#ADD8E6 at 40% opacity)
- Various fall angles

### Exhaust Puffs
**File:** `exhaust_puffs.png`  
**Dimensions:** 128x64 pixels

- 6 puff variations
- Grey smoke (#808080)
- Dissolve over 2 seconds
- Scale variation for distance

### Windshield Wiper Overlay
**File:** `windshield_wiper_overlay.png`  
**Dimensions:** Screen width x 200 pixels

- Wiper blade positions (4 frames)
- Water droplet clearing effect
- Semi-transparent rain streaks

### Headlight Glow
**File:** `headlight_glow.png`  
**Dimensions:** 128x64 pixels

- Warm yellow glow (#FFFACD)
- Cone shape
- 15m range representation
- Multiple intensity levels

---

## 🖥️ UI Elements

### Circle Counter
**File:** `circle_counter.png`  
**Dimensions:** 128x64 pixels

- Counter display: "CIRCLES: ###"
- Style: Dashboard/GPS aesthetic
- Animation: Number increment

### Days Counter (Path B)
**File:** `days_counter.png`  
**Dimensions:** 128x64 pixels

- Counter display: "DAYS: #"
- Style: Calendar/worn paper aesthetic
- Animation: Day increment

### GPS Recalculating
**File:** `gps_recalculating.png`  
**Dimensions:** 256x128 pixels

- GPS screen mockup
- "RECALCULATING..." text with loading animation
- Increasingly stressed tone in later versions
- Final version: GPS appears to be crying (subtle)

---

## 🎬 Animation Specifications

### Pre-Baked Circulation Loops

All circling vehicles use pre-animated loops for mobile performance.

| Vehicle | Loop Duration | Lane | Notes |
|---------|---------------|------|-------|
| Wedding Van 1987 | 30 seconds | Middle | Includes Patrick wave cycle |
| Tour Bus | 45 seconds | Outer | Includes community activity |
| Food Truck | 60 seconds | Outer | Includes stop-and-serve beats |
| Seán's Micra | 25 seconds | Middle | Passes Exit 6 without slowing |
| Learner Car | Variable | Inner (badly) | Irregular, jerky motion |
| Family Van | 35 seconds | Outer | Lost, hesitant speed changes |
| Farmer Tractor | 90 seconds | Creates own path | Crosses lanes occasionally |
| Background Traffic | 20 seconds each | Various | Generic shapes, simplified |

### Character Animations

| Character | Animation | Frames | Duration | Loop |
|-----------|-----------|--------|----------|------|
| Patrick | Wave | 6 | 1.5s | No |
| Patrick | Driving content | 2 | 3s | Yes |
| Margaret | Wind sway | 4 | 2s | Yes |
| Orla | Gesture with clipboard | 8 | 2s | No |
| Seán | Knowing nod | 4 | 1s | No |
| Kevin | White-knuckle grip | 2 | 0.5s | Yes |
| Brenda | Flinch | 4 | 0.5s | No |

### Key Animation Details

### Patrick's Wave (Sheet 3):
- **Duration:** 1.5 seconds
- **Frames:** 6
- **Pattern:** Raise → wave → lower, no loop
- **Trigger:** First encounter; passing the bros' rental car
- **Purpose:** The game's warmest and most unsettling greeting — 37 years of circling, still friendly
- **Audio Sync:** Faint wedding march (music box version) as the van passes
- **Performance Optimization:** None needed (part of pre-baked van loop)

### Margaret's Wind Sway (Sheet 3):
- **Duration:** 2 seconds per cycle
- **Frames:** 4
- **Pattern:** Gentle sway loop, continuous and subtle
- **Trigger:** Constant (wind effect)
- **Purpose:** She is at rest, not lifeless — dignity in motion; brief ominous chord resolves to warm tone on first reveal
- **Audio Sync:** Brief ominous chord on first sighting, quickly replaced by warm tone
- **Performance Optimization:** None needed

### GPS Recalculating (UI):
- **Duration:** ~2 seconds per loop, escalating versions over quest
- **Frames:** Loading animation cycle; final version adds subtle crying detail
- **Pattern:** Loop while GPS active; version swaps at frustration milestones
- **Trigger:** Every failed exit attempt / continuous during circling
- **Purpose:** The GPS is as trapped as the player — comedy through UI decay
- **Audio Sync:** "Recalculating" voice line with sad trombone undertone on failure
- **Performance Optimization:** None needed

### Windshield Wiper Overlay (Effects):
- **Duration:** Swipe every 3 seconds
- **Frames:** 4 blade positions
- **Pattern:** Rhythmic swipe loop, constant
- **Trigger:** Constant (default light rain weather)
- **Purpose:** Rhythmic hypnosis of the eternal circle; POV framing device
- **Audio Sync:** Wiper rhythm layered under rain patter
- **Performance Optimization:** Disable overlay entirely at Low LOD

### Circulation Loops (all vehicles):
- **Duration:** 20-90 seconds per vehicle (see table above)
- **Frames:** Pre-baked path animation, 12fps character detail / 30fps particles
- **Pattern:** Continuous loops; Seán's loop deliberately passes Exit 6 without slowing
- **Trigger:** Constant while location active
- **Purpose:** Hypnotic perpetual motion — the roundabout as ecosystem
- **Audio Sync:** Per-lane engine beds; radio snippets fade in/out as vehicles pass
- **Performance Optimization:** Pre-baked loops (no real-time pathfinding); distant vehicles simplified to colored rectangles

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Exit sign high-contrast set | set at sheet layout | 256x256 sheet | Bold-outline exit sign variants — exit reading is the core puzzle interaction |
| Lane boundary outlines | set at sheet layout | overlay | High-contrast lane divider overlay for the three concentric lanes |
| Vehicle silhouette set | set at sheet layout | per vehicle | Distinct outline shapes for the 8 resident vehicles (recognition without color) |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static rain option | set at sheet layout | 64x64 | Reduced/disabled rain particle variant (density scalable to zero) |
| Wiper overlay off-state | n/a | n/a | Windshield wiper overlay can be disabled — constant rhythmic motion is a vestibular trigger |
| Reduced circulation mode | n/a | n/a | Background traffic loops pausable; hero vehicles remain (slow, steady movement only) |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| GPS Recalculating panel | UI | 256x128 | Visual mirror of the "recalculating" voice line (already specified) |
| Indicator tick icon | set at sheet layout | 24x24 | Blinking indicator visual (1Hz) mirroring the tick-tick-tick audio |
| Radio snippet marker | set at sheet layout | 24x24 | Music-note icon above vehicles when their radio audio is audible (love songs from the 1987 van, tour bus PA) |
| Exit success flash | set at sheet layout | 64x64 | Visual for the triumphant-relief stinger on successful exit |

### Colorblind Considerations:
- Exit signs distinguished by arrow direction + text, never color alone (all six are deliberately identical green — the confusion is textual, not chromatic)
- Lane difficulty communicated by lane width, asphalt tone AND position, not color coding
- Brake light / indicator states paired with icon cues
- Touch zones minimum 44px for lane-change and exit controls; text readable at mobile sizes

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import); wedding van sheet and GPS UI need higher quality (hero asset, readable text)
- **Fallback:** PNG high quality for roundabout base and exit signs (gameplay-critical readability)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| cloverleaf_environment | roundabout base, island, monument, gift shop, signs, approach, backgrounds | 2048x2048 |
| cloverleaf_vehicles | all 8 resident vehicles + bros rental + drivers | 1024x1024 |
| cloverleaf_effects_ui | rain, exhaust, spray, wipers, headlights, counters, GPS | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | 8 detailed vehicles, full rain (50 particles/sec), exhaust per vehicle, road spray, wiper overlay |
| Medium | Reduced particle density (scalable rain), simplified exhaust, distant vehicles at 50m simplified |
| Low | Distant vehicles as colored rectangles, minimal rain, no road spray, wiper overlay off |

### Performance Targets:
- **Target FPS:** 60 (min-spec baseline)
- **Max Draw Calls:** Under 50
- **Memory Footprint:** Under 64 MB total for location
- **Particle Limit:** Rain 50 particles/second (scalable) + 8 exhaust sources max

### Performance Notes:
- All circling vehicles use pre-baked animation loops — no real-time pathfinding
- Max 8 detailed vehicles on screen; LOD distance 50m
- Particle density scalable by device capability
- Target resolutions: 1x, 2x, 3x for mobile scaling

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D on Path2D/PathFollow2D (pre-baked circulation loops), CPUParticles2D (rain, exhaust, spray — not GPU), CanvasLayer (wiper overlay, GPS, counters), AnimationPlayer for character sub-animations
- Special systems: speed-threshold exit resolver (exits only work below threshold), circle/day counters bound to quest state, Path A/B branch controller, GPS escalation state machine, food truck schedule window (south bend, outer lane)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Wedding van passing | Faint wedding march (music box) + love songs 1987 radio | While van within pass range |
| Margaret first visible | Brief ominous chord → warm tone | On first reveal camera focus |
| Seán's Micra passing Exit 6 | Existential drone (philosophy scenes) | Dialogue-triggered |
| GPS Recalculating panel | "Recalculating" voice + sad trombone undertone | On failed exit / continuous circling |
| Missed exit | Whoosh + GPS beep | On exit pass above speed threshold |
| Food truck window open | Cheerful food service jingle + sizzle | During outer-lane serve window |
| Successful exit | Triumphant relief stinger | On exit below speed threshold |
| Indicator icon | Tick-tick-tick | 1Hz blink sync |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Cloverleaf of Confusion (`publandia_sidequest_eternal_roundabout_01`) | Entire location set | Auto-triggered driving east from Paddy's; binary Path A/B |
| Path A: Escape Attempts | Exit signs, GPS UI, circle counter | Slow-down discovery; "Road Warrior" achievement |
| Path B: Adaptation | Tour bus, food truck, days counter | 3+ in-game days; "Roundabout Veteran"; Bradley's girlfriend epilogue |
| Lane Merge Challenge (minigame) | Lane indicator UI, merge zone markings | Timing-based merges |
| Food Truck Intercept (minigame) | Food truck sheet, schedule UI | Position-matching during outer-lane window |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Paddy's Premium Motors | Bros' rental car (Paddy's vehicle), Exit 3 | Entry prerequisite; Exit 3 returns to Paddy's |
| Bigger Roundabout | Exit 1 signage | Exit 1 leads to a BIGGER roundabout |
| Cliffs of Moher | Exit 6 signage | The actual destination — where Patrick and Margaret were going in 1987 |
| Publandia background scenes | Patrick & Margaret van | Post-completion easter egg appearances |
| Final Boss (Publandia) | Circulation pattern reference | Boss uses "roundabout attack pattern"; Lord Pilsner recognizes it |
| Airplane Departure | Roundabout aerial, wedding van | Visible from airplane window, still circling |

---

## 🎯 Priority Order for Artist

### Phase 1: Core Set-Piece (CRITICAL)
1. ⭐ **Wedding Van 1987** - Hero asset, most screenshots
2. ⭐ **Roundabout Base** - Foundation for everything
3. ⭐ **Patrick & Margaret** - Iconic characters
4. **Center Island** - Establishes scale

### Phase 2: Community Vehicles
5. **Tour Bus** - Second most important vehicle
6. **Food Truck** - Economic hub
7. **Seán's Car** - Existential horror vehicle
8. **Orla Brennan** - Key NPC

### Phase 3: Background Life
9. **Learner Car** - Comedy relief
10. **Family Van** - Relatable tourists
11. **Farmer Tractor** - Irish authenticity
12. **Background traffic** - Can be simplified

### Phase 4: Polish
13. **Exit Signs** - Gameplay essential
14. **Effects (rain, exhaust)** - Atmosphere
15. **UI Elements** - Functionality
16. **GPS Crying** - Easter egg polish

---

## 📏 Technical Requirements Summary

| Specification | Requirement |
|--------------|-------------|
| **Max Sprite Sheet Size** | 2048x2048 pixels |
| **Color Depth** | 32-bit RGBA |
| **File Format** | PNG with transparency |
| **Target Resolution** | 1x, 2x, 3x for mobile scaling |
| **Memory Budget** | <64MB total for location |
| **Max Active Sprites** | 8 detailed vehicles + effects |
| **Animation Frame Rate** | 12fps for character, 30fps for particles |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Tiny vehicles circling a massive roundabout forever — hypnotic, absurd, and quietly heartbreaking"
- **Color Mood:** Grey overcast sky and wet asphalt against defiant Irish green; warm accents (van cream, food truck orange, bus red) mark the pockets of life
- **Lighting:** Grey overcast daylight (perpetual "might rain" energy); headlights on at all hours (Irish tradition); ambient #B0B0B0 at 60% intensity; warm food truck glow (#FFD700)
- **Texture:** Rain-slick asphalt with puddle reflections, 37 years of tire wear, moss on the monument, rust on the Micra and tractor

### Environmental Storytelling:
- Lane markings faded along the 1987 van's regular middle-lane path — 37 years written into the road itself
- "GIFT SHOP - OPENING SOON (Since 1994)", the "EST. ???" monument plaque, and "ALL EXITS LEAD SOMEWHERE" vandalism
- Tin cans worn to nubs, dead dashboard flowers, hand-painted "37 YEARS" banner — Patrick's whole story without a word
- Laundry lines and roof gardens on the tour bus: a society, not a breakdown

### Character Integration Notes:
- Drivers and passengers render inside/on their vehicles (no on-foot NPC sprites in circulation)
- Margaret rendered with dignity and reviewed for tone — love story, never gross-out (see CRITICAL ART DIRECTION, Sheet 3)
- Seán's Micra must look unremarkable — the horror lands only when players realize he never exits
- Bros' interior view sheet used for driving sequences and dialogue framing

---

## 🎨 Style Reference Notes

### EarthBound Aesthetic Principles
- **Oblique top-down view** (not pure isometric)
- **Bold outlines** (2-3px for main elements)
- **Limited color palette** per object
- **Intentional simplification** over photorealism
- **Charm over accuracy**

### What Makes This Location Special
- **Scale contrast**: Tiny vehicles on massive roundabout
- **Movement**: Everything circles, creates hypnotic effect
- **Story in visuals**: 37-year-old wedding decorations tell Patrick's story
- **Dignity in darkness**: Margaret is a skeleton but posed with love
- **Irish atmosphere**: Grey skies, green grass, wet roads

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The 1987 Wedding Van with Margaret** - The game's most iconic visual: 37 years of love, still circling
2. **Aerial Circulation View** - Endless hypnotic vehicle loops from above
3. **"DAYS CIRCLING: 3" Counter Overlay** - Path B despair/comedy in one UI element
4. **Tour Bus Community Celebration** - Democracy, laundry lines, and roof gardens on a trapped bus
5. **Patrick Waving While Margaret "Rests"** - Tragicomedy in a single frame

### Quote Potential:
- "First time? ...That's what they all say."
- "They all lead back here eventually."
- "In here, I know what comes next. Another circle. Then another."
- "Did ye try... slowing down?"
- "Margaret? She's just resting."

### Meme Potential:
- "Patrick and Margaret: 37 Years and Still Going"
- "Seán could leave. He doesn't."
- GPS sobbing "recalculating"
- Tour bus democracy vs. American chaos

---

## 📋 Required PNG Files (43 Total)

*Component files below are grouped per composite sheet where a sheet dimension is specified; individual component dimensions are set at sheet layout.*

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | roundabout_base_1024.png | 1024x1024 |
| 2 | lane_markings_overlay.png | set at sheet layout |
| 3 | center_island_512.png | 512x512 |
| 4 | celtic_monument.png | set at sheet layout (80x120 in-scene) |
| 5 | gift_shop_closed.png | set at sheet layout (60x40 in-scene) |
| 6 | exit_signs_sheet.png | 256x256 |
| 7 | approach_road.png | set at sheet layout |
| 8 | background_fields.png | set at sheet layout |
| 9 | background_sky.png | set at sheet layout |
| 10 | wedding_van_base.png | 256x128 (composite sheet) |
| 11 | wedding_van_details.png | set at sheet layout |
| 12 | patrick_driver.png | set at sheet layout |
| 13 | margaret_skeleton.png | set at sheet layout |
| 14 | tin_cans_dragging.png | set at sheet layout |
| 15 | tour_bus_base.png | 256x256 (composite sheet) |
| 16 | tour_bus_passengers.png | set at sheet layout |
| 17 | orla_with_clipboard.png | set at sheet layout |
| 18 | food_truck_base.png | 192x128 (composite sheet) |
| 19 | food_truck_window_open.png | set at sheet layout |
| 20 | chef_maeve.png | set at sheet layout |
| 21 | nissan_micra_1999.png | 128x64 (composite sheet) |
| 22 | sean_driver.png | set at sheet layout |
| 23 | learner_car_base.png | 128x64 (composite sheet) |
| 24 | l_plates.png | set at sheet layout |
| 25 | brenda_instructor.png | set at sheet layout |
| 26 | kevin_student.png | set at sheet layout |
| 27 | people_carrier_rental.png | 192x96 (composite sheet) |
| 28 | murphy_family_silhouettes.png | set at sheet layout |
| 29 | tractor_ancient.png | 192x128 (composite sheet) |
| 30 | sheep_trailer.png | set at sheet layout |
| 31 | padraig_driver.png | set at sheet layout |
| 32 | rental_car_base.png | 128x64 (composite sheet) |
| 33 | bros_interior_view.png | set at sheet layout |
| 34 | rain_particles.png | 64x64 |
| 35 | exhaust_puffs.png | 128x64 |
| 36 | road_spray.png | set at sheet layout |
| 37 | windshield_wiper_overlay.png | screen width x 200 |
| 38 | headlight_glow.png | 128x64 |
| 39 | circle_counter.png | 128x64 |
| 40 | days_counter.png | 128x64 |
| 41 | gps_recalculating.png | 256x128 |
| 42 | lane_indicator.png | set at sheet layout |
| 43 | food_truck_schedule.png | set at sheet layout |

**Total Estimated Memory:** ~64 MB maximum (location performance budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] Environment set: `roundabout_base_1024.png` (1024x1024), `center_island_512.png` (512x512), `exit_signs_sheet.png` (256x256), `lane_markings_overlay.png`, `celtic_monument.png`, `gift_shop_closed.png`, `approach_road.png`, `background_fields.png`, `background_sky.png`
- [ ] Wedding van set (256x128 composite): `wedding_van_base.png`, `wedding_van_details.png`, `patrick_driver.png`, `margaret_skeleton.png`, `tin_cans_dragging.png`
- [ ] Tour bus set (256x256 composite): `tour_bus_base.png`, `tour_bus_passengers.png`, `orla_with_clipboard.png`
- [ ] Food truck set (192x128 composite): `food_truck_base.png`, `food_truck_window_open.png`, `chef_maeve.png`
- [ ] Seán set (128x64 composite): `nissan_micra_1999.png`, `sean_driver.png`
- [ ] Learner car set (128x64 composite): `learner_car_base.png`, `l_plates.png`, `brenda_instructor.png`, `kevin_student.png`
- [ ] Family van set (192x96 composite): `people_carrier_rental.png`, `murphy_family_silhouettes.png`
- [ ] Tractor set (192x128 composite): `tractor_ancient.png`, `sheep_trailer.png`, `padraig_driver.png`
- [ ] Bros rental set (128x64 composite): `rental_car_base.png`, `bros_interior_view.png`
- [ ] Effects: `rain_particles.png` (64x64), `exhaust_puffs.png` (128x64), `road_spray.png`, `windshield_wiper_overlay.png` (screen width x 200), `headlight_glow.png` (128x64)
- [ ] UI: `circle_counter.png` (128x64), `days_counter.png` (128x64), `gps_recalculating.png` (256x128), `lane_indicator.png`, `food_truck_schedule.png`

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG with transparency, 32-bit RGBA |
| Color Space | sRGB |
| DPI | 72 (screen resolution) |
| Compression | Lossless PNG |
| Naming Convention | snake_case, all lowercase |
| Layer Organization | Preserve layers in master file |
| Resolutions | 1x, 2x, 3x variants for mobile scaling |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above, at 1x/2x/3x
- **Backup:** Master PSD/layered file with organized layer groups
- **Documentation:** Animation timing reference sheet + circulation loop path guide

### Delivery Checklist:
- [ ] All sprites delivered at 1x, 2x, 3x resolutions
- [ ] Transparent backgrounds where required
- [ ] Animation frames in sprite sheet format
- [ ] Color palette strictly followed
- [ ] Margaret rendered with dignity (reviewed for tone)
- [ ] Performance tested with 8 active vehicles
- [ ] Rain particles tested for mobile performance
- [ ] All UI elements legible at mobile sizes

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: "JUST MARRIED 1987" legible-but-faded, tin cans worn to nubs, gift shop "Since 1994" sign, GPS crying easter egg subtle
- [ ] Accessibility visual alternatives included for all audio cues (GPS voice, indicator ticks, radio snippets, exit stinger)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (American impatience vs. Irish acceptance; existential comfort horror)
- [ ] Margaret reviewed for tone — dignity and love story, never gross-out
- [ ] Hidden details discoverable (bullet-holed sign, sheep staring at camera, COUNCIL MEETING window, GPS tears)
- [ ] Performance optimized (pre-baked loops, CPU particles, 8-vehicle cap, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (exit signs by text/arrow, not color)
- [ ] Social media viral potential maximized in composition choices (wedding van framing, aerial circulation shot)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia throughout ("Cliffs of Moher" is the in-world eternal destination reference) |
| Cultural Specificity | ✅ | Irish roundabout confusion, emigration/staying themes, community resilience |
| Satirical Targets Appropriate | ✅ | American tourist impatience (punching at privilege); Irish stereotypes affectionate |
| Seedy Underbelly Present | ✅ | Accidentally existential — the vice is giving up on destinations entirely |
| Gameplay Value Established | ✅ | Major set-piece, binary Path A/B, two minigames, status effects, post-completion unlocks |
| Technical Feasibility | ✅ | Pre-baked animation loops solve mobile performance |
| Performance Budget | ✅ | 60 FPS on min-spec hardware, <50 draw calls, <64 MB, scalable particles |
| Accessibility Features | ✅ | Visual audio cues, motion-reduction options (rain/wipers), text-based exit reading |
| No Crypto Elements | ✅ | All transactions in Sovs (food truck menu) |
| Social Media Integration | ✅ | 5 screenshot moments + quotes + meme formats identified |

---

**The Cloverleaf is Eurobound's most visually ambitious location. Every asset tells a story. Patrick and Margaret's van should make players feel something. Seán's car should be unremarkable until you realize he never exits. The tour bus should show a functioning society. And somewhere in the background, the GPS should be quietly breaking down.**

*"They all lead back here eventually."*
