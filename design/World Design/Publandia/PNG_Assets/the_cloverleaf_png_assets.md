# The Cloverleaf (Eternal Roundabout) - Complete PNG Asset Requirements

## 📋 Overview
**Location ID:** `publandia_outskirts_cloverleaf_roundabout_01`  
**Theme:** Eternal circulation, absurdist society, American impatience vs. Irish acceptance  
**Zone:** Publandia Outskirts, 1km east of Paddy's Premium Motors  
**Type:** Major Set-Piece - Complex Multi-Vehicle Scene  
**Art Style:** EarthBound oblique view, stylized simplification over photorealism

---

## 🎨 Master Color Palette

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

## 📁 Folder Structure

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

## 📐 Animation Specifications

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

## ✅ Delivery Checklist

- [ ] All sprites delivered at 1x, 2x, 3x resolutions
- [ ] Transparent backgrounds where required
- [ ] Animation frames in sprite sheet format
- [ ] Color palette strictly followed
- [ ] Margaret rendered with dignity (reviewed for tone)
- [ ] Performance tested with 8 active vehicles
- [ ] Rain particles tested for mobile performance
- [ ] All UI elements legible at mobile sizes

---

**The Cloverleaf is Eurobound's most visually ambitious location. Every asset tells a story. Patrick and Margaret's van should make players feel something. Seán's car should be unremarkable until you realize he never exits. The tour bus should show a functioning society. And somewhere in the background, the GPS should be quietly breaking down.**

*"They all lead back here eventually."*
