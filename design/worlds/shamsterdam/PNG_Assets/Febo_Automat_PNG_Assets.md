# FEBO Automat - Complete PNG Asset Requirements

## 📋 Overview
FEBO is Shamsterdam's 24-hour wall of tiny glowing doors, where coins go in, hot mystery meat comes out, and no one — club refugee, shift worker, philosopher, or bro — is judged. This document specifies every PNG asset for the flagship automat: the yellow beacon exterior, the interior with THE WALL dominant, the full compartment grid and food sprites, staff and 3 AM crowd NPCs, steam and mechanism effects, and the wall-navigation UI. Its satirical essence in a sentence: the great equalizer of 3 AM decisions has been open since 1941 and it will outlive us all.

**Location ID:** `shamsterdam_central_febo_automat_01`
**Theme:** Late-night food desperation democratized; an affectionate portrait of a real Dutch institution
**Zone:** Central Shamsterdam (flagship 24-hour location)
**Hours:** 24 hours (the wall never sleeps; peak 2-4 AM)
**Primary Function:** Automat fast food / 3 AM salvation / regret dispensary — coin-operated wall interaction system, time-based crowd density, Mystery Item gamble, Munchies Pipeline bonus, FEBO Regular status

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| FEBO Yellow | #FFD700 | Facade, signage, uniforms |
| Chrome Silver | #C0C0C0 | Compartment frames, counter, coin machine |
| Fluorescent White | #F5F5F5 | Interior light wash, wall tiles |
| Meat Brown | #8B4513 | Food sprites, fryer tones |
| Night Black | #1A1A1A | Exterior darkness, window contrast |
| Compartment Glow | #FFB347 | Warm light inside each little door |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/febo_automat/
├── environment/
│   ├── febo_exterior.png
│   ├── febo_interior_main.png
│   └── febo_wall_grid.png
├── objects/
│   └── febo_food_items.png
├── npcs/
│   └── npc_febo_staff_customers.png
├── effects/
│   └── febo_effects.png
└── ui/
    └── febo_ui.png
```

---

## 🏪 Sprite Sheet 1: Exterior — The Yellow Beacon
**File:** `febo_exterior.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #FFD700, #1A1A1A, #F5F5F5

### Facade Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| FEBO Facade (Night) | (0, 0) | 512x384 | Yellow beacon in darkness, glass doors, steam escaping |
| FEBO Facade (Day) | (512, 0) | 512x384 | Same structure, daylight grading, quieter energy |
| "FEBO" Letter Sign | (0, 384) | 256x96 | Iconic yellow letters, lit 24/7 |
| "AUTOMATIEK / SINCE 1941" Door Text | (256, 384) | 128x64 | Smaller lettering, true claim |
| "24 UUR" Hours Sign | (384, 384) | 96x64 | Unnecessary; FEBO is eternal |
| Window Food Photos | (480, 384) | 192x96 | Photos that look better than reality (standard practice) |
| Sidewalk Light Spill | (672, 384) | 256x128 | Fluorescent glow wedge cast onto pavement, alpha gradient |
| Escaping Steam Wisp | (928, 384) | 96x128 | Doorway steam, 2 stacked 96x64 frames |

### Technical Notes:
- Night/day facades swap by clock; letter sign renders on both (always lit)
- Light spill is alpha-blended, no additive shader required
- Steam wisp frames alternate at 0.6s; static on Low LOD

---

## 🧱 Sprite Sheet 2: Interior Main Background
**File:** `febo_interior_main.png`
**Dimensions:** 1920x1080 pixels (standalone full-scene background — not atlased)
**Color Palette:** #F5F5F5, #C0C0C0, #FFD700

### Scene Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Interior Backdrop | (0, 0) | 1920x1080 | Full scene: THE WALL dominant on left two-thirds, counter right, kitchen window rear, standing ledges, two sad stools, full trash bin, empty napkin dispenser, wall clock showing the hour of your choices |

### Technical Notes:
- Single full-scene paint; interactive elements (wall grid, counter, coin machine) overlay from Sheets 3-4 at fixed anchor points
- Anchor points (document in layer names): wall grid at (128, 192), counter at (1408, 480), coin machine at (1312, 448), kitchen window at (1472, 128)
- The clock face area (1728, 96, 64x64) is kept blank — a live clock overlay renders the in-game hour

---

## 🚪 Sprite Sheet 3: THE WALL — Grid & Fixtures
**File:** `febo_wall_grid.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #C0C0C0, #FFB347, #F5F5F5

### The Wall:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wall Grid (4 rows x 6 doors) | (0, 0) | 768x512 | Chrome-framed glass doors, 15cm scale, individually lit; rows read top-to-bottom: classics / adventurous / substantial / Mystery Row |
| Compartment Closed | (768, 0) | 64x64 | Single door, red occupied light on, warm glow |
| Compartment Open | (832, 0) | 64x64 | Door swung, food claimable |
| Compartment Empty | (896, 0) | 64x64 | Dark, despair appropriate — someone beat you to it |
| Red Occupied Light | (960, 0) | 32x32 | Indicator lamp, lit state |
| Red Light Off | (992, 0) | 32x32 | Indicator lamp, dark state |
| Menu Board | (768, 64) | 192x128 | Shows what SHOULD be in each slot |
| Coin Slot & Handle Plate | (768, 192) | 96x96 | Insert-turn mechanism close-up, 44px+ touch target art |
| Handle Turned Variant | (864, 192) | 96x96 | Mid-rotation state of the same plate |

### Counter & Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Service Area | (0, 512) | 384x256 | For those who want human interaction (available, not required) |
| Kitchen Glimpse Window | (384, 512) | 256x192 | Theo restocking, fryer glow, factory efficiency |
| Coin Change Machine | (640, 512) | 96x192 | "COIN CHANGE" — always slightly broken, hand-taped note |
| Standing Ledge | (0, 768) | 384x128 | Minimal eating ledge, not designed for lingering |
| Sad Stool (x2 variants) | (384, 768) | 128x128 | Two 64x128 stools side by side, both sad |
| Full Trash Bin | (512, 768) | 64x128 | Always full, overflow wrapper detail |
| Empty Napkin Dispenser | (576, 768) | 64x64 | Always empty; the rarest gift is a napkin |
| Wall Clock Face | (640, 768) | 64x64 | Overlay clock body for interior anchor |
| Restock Door (Rear of Wall) | (736, 512) | 96x192 | Kitchen-side compartment access, glimpsed during restock |

### Technical Notes:
- Wall grid is the master interactable: each 128x128 door region maps to one menu item; door-state sprites (closed/open/empty) overlay per-slot
- Red lights are separate 32x32 overlays so occupancy can change without redrawing doors
- Coin plate and handle are the tap targets — art padded to guarantee 44px minimum at gameplay scale

---

## 🍟 Sprite Sheet 4: Food Compartment Items
**File:** `febo_food_items.png`
**Dimensions:** 256x256 pixels
**Color Palette:** #8B4513, #FFD700, #F5F5F5

### The Wall's Offerings (48x48 grid):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kroket | (0, 0) | 48x48 | The classic — deep-fried ragout, crispy coating |
| Frikandel | (48, 0) | 48x48 | Mystery meat tube; don't ask, just eat |
| Kaassouflé | (96, 0) | 48x48 | Deep-fried cheese in pastry, happiness |
| Bamischijf | (144, 0) | 48x48 | Fried noodle disc, cross-cultural comfort |
| Berehap | (192, 0) | 48x48 | Satay meat on a stick, substantial |
| Mexicano | (0, 48) | 48x48 | "Spicy" by Dutch standards |
| Hamburger | (48, 48) | 48x48 | When you need something recognizable |
| Cheeseburger | (96, 48) | 48x48 | The above, but better |
| Satéschotel | (144, 48) | 48x48 | The commitment option |
| Frikandel Speciaal | (192, 48) | 48x48 | With onions and sauce — the works |
| Mystery Item (Wrapped) | (0, 96) | 48x48 | ??? — changes daily, fate decides |
| Mystery Item Revealed Variants | (48, 96) | 144x48 | Three 48x48 reveal states: great / interesting / experimental |
| In-Hand Kroket (Bite Taken) | (192, 96) | 48x48 | Post-first-bite state, steam nick |
| Food Inventory Icons | (0, 144) | 192x48 | Four 48x48 generic icons: snack, meal, mystery, drink |
| Compartment Steam Puff | (192, 144) | 48x48 | Small steam sprite for door-open moment |

### Technical Notes:
- Each item renders inside its wall slot at 48x48 behind the glass-door overlay
- Mystery reveal variant chosen by daily seed; wrapped sprite always shown pre-purchase
- All food shares one atlas region — one draw call for the entire stocked wall

---

## 👥 Sprite Sheet 5: Staff & The 3 AM Congregation
**File:** `npc_febo_staff_customers.png`
**Dimensions:** 1024x512 pixels
**Sprite Size:** 64x96 per single NPC frame
**Color Palette:** #FFD700 uniforms, mixed night-crowd palette

### Staff:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Anouk Counter Idle | (0, 0) | 64x96 | FEBO yellow uniform, efficiency incarnate |
| Anouk Handing Change | (64, 0) | 64x96 | "Coins? Two Sovs fifty. There." |
| Anouk Restocking Frame 1 | (128, 0) | 64x96 | Loading a slot from the rear |
| Anouk Restocking Frame 2 | (192, 0) | 64x96 | Slot closed, next item |
| Anouk Recognition Nod | (256, 0) | 64x96 | FEBO Regular status acknowledgment |
| Theo Kitchen Glimpse Frame 1 | (320, 0) | 64x96 | Perpetual motion, fry basket up |
| Theo Kitchen Glimpse Frame 2 | (384, 0) | 64x96 | Fry basket down, restock pivot |

### Customers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Club Refugee | (448, 0) | 64x96 | Club outfit, makeup situation, one shoe held in hand |
| Club Refugee Staring | (512, 0) | 64x96 | 30 minutes at the wall, still choosing |
| Shift Worker | (576, 0) | 64x96 | Uniform, efficient, 90 seconds total |
| First-Timer Tourist | (640, 0) | 64x96 | Guidebook visible, photographing the wall |
| First-Timer Touching Glass | (704, 0) | 64x96 | Don't. |
| The Philosopher (3 AM Only) | (768, 0) | 64x96 | Holding kroket like an artifact |
| The Philosopher Nodding | (832, 0) | 64x96 | Profound connection established |
| The Regular | (896, 0) | 64x96 | Coins already out; 45 seconds; transcended |
| Crowd Block — Day | (0, 96) | 256x96 | Pre-composed group: locals + curious tourists, medium density |
| Crowd Block — Evening | (256, 96) | 256x96 | Pre-composed group: pre-club anticipation |
| Crowd Block — 3 AM | (512, 96) | 384x96 | Pre-composed group: maximum density, all types, pure energy |
| Anouk Portrait (Dialogue) | (0, 192) | 128x128 | Close-up: not unfriendly, just efficient beyond conversation |
| Philosopher Portrait (Dialogue) | (128, 192) | 128x128 | Close-up: reverent kroket wonder |
| Eating Poses Strip | (256, 192) | 256x96 | Four 64x96 universal eating poses used by any customer sprite |
| Satisfied Sigh Pose | (512, 192) | 64x96 | The universal language, post-first-bite |

### Technical Notes:
- Crowd blocks swap by time-of-day table (profile's density schedule); only ONE block renders at a time
- Philosopher spawns 2-4 AM only; Regular can spawn any hour
- Eating poses are palette-modulated to match whichever NPC is eating

---

## ✨ Sprite Sheet 6: Effects & Mechanisms
**File:** `febo_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #FFB347, #F5F5F5, #1A1A1A

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Door Opening Frames | (0, 0) | 192x64 | Three 64x64 frames: latch pop → swing → open glow |
| Handle Turn Frames | (192, 0) | 128x64 | Two 64x64 frames of the coin-handle rotation |
| Coin Insert Sparkle | (320, 0) | 32x32 | Brief chrome glint on coin drop |
| Compartment Steam (Large) | (352, 0) | 64x64 | Steam burst on door open, 1-shot |
| Glass Condensation Overlay | (416, 0) | 64x64 | Tileable fog for lower compartments |
| Fluorescent Flicker Strip | (0, 64) | 128x32 | Two 64x32 tube states for subtle interior flicker |
| Fryer Glow (Kitchen Window) | (128, 64) | 64x64 | Warm pulse behind Theo |
| 3 AM Atmosphere Gradient | (192, 64) | 256x128 | Stretchable warm-haze overlay: fluorescent lights feel warmer, strangers feel like friends |
| Munchies Shimmer | (448, 64) | 64x64 | Subtle rainbow edge for Munchies Pipeline food |
| Hot-Bite Steam Sting | (0, 96) | 32x32 | Kroket temperature surprise puff |
| Community Glow Ring | (32, 96) | 64x64 | Soft ring under NPCs during 3 AM event (+Community status) |
| Wrapper Drop | (96, 96) | 32x32 | Trash-bin-adjacent wrapper, physics-free set dressing |

### Technical Notes:
- All effects are CPUParticles2D-compatible single textures or AnimatedSprite2D strips — no shaders
- 3 AM gradient is stretched over the scene at 25% alpha between 2-4 AM only
- Munchies shimmer applies only when arriving from De Groene Gids within 2 in-game hours

---

## 🧭 Sprite Sheet 7: UI Elements
**File:** `febo_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #FFD700 chrome UI, #1A1A1A panels

### Interface Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wall Navigation Panel | (0, 0) | 256x256 | Compartment selection grid mirroring THE WALL, item names + prices |
| Coin Insertion Prompt | (256, 0) | 128x64 | "3 Sovs — Insert Coins" with coin-tap zone |
| Handle Turn Prompt | (256, 64) | 128x64 | Rotational swipe indicator |
| Food Acquired Popup | (256, 128) | 128x96 | Item obtained card with food icon slot |
| Mystery Reveal Panel | (384, 0) | 128x128 | "What did you get?" reveal frame |
| Munchies Bonus Indicator | (384, 128) | 64x64 | +50% HP restoration marker |
| FEBO Regular Status Badge | (448, 128) | 64x64 | Staff recognition achieved |
| Warm Inside Status Icon | (0, 256) | 32x32 | Kroket comfort status |
| Cheese Contentment Icon | (32, 256) | 32x32 | Kaassouflé/cheeseburger status |
| Exotic Confusion Icon | (64, 256) | 32x32 | Bamischijf status |
| Spicy Surprise Icon | (96, 256) | 32x32 | Mexicano delayed-HP warning |
| Full Meal Status Icon | (128, 256) | 32x32 | Satéschotel commitment |
| Community Status Icon | (160, 256) | 32x32 | 3 AM togetherness (temporary) |
| Achievement Badges Strip | (0, 288) | 320x64 | Five 64x64 badges: Wall Beginner / Wall Regular / Wall Gambler / Wall Survivor / Wall Completionist |
| Crowd Density Meter | (320, 256) | 96x32 | Time-based crowd level indicator |
| Empty Slot Despair Popup | (320, 288) | 128x64 | "Someone beat you to it." |

### Technical Notes:
- Wall Navigation Panel slots are 44px+ touch targets at gameplay scale
- Status icons use distinct silhouettes (see Accessibility) — never color-only
- Achievement badges grayscale until earned (modulate, not separate art)

---

## 🎬 Animation Specifications

### Compartment Door Open (Sheets 3 & 6):
- **Duration:** 0.9 seconds (0.3s per frame)
- **Frames:** 3 (latch pop → swing → open glow) + steam burst
- **Pattern:** Play once on successful purchase; door stays open until item taken
- **Trigger:** Coins inserted + handle turned
- **Purpose:** The core FEBO ritual — the wall provides
- **Audio Sync:** Coin clunk at 0.0s, handle ratchet at 0.3s, door pop at 0.6s, steam hiss at 0.7s
- **Performance Optimization:** Steam burst dropped on Low LOD; door frames retained (core feedback)

### Handle Turn (Sheet 6):
- **Duration:** 0.4 seconds (2 frames at 0.2s)
- **Frames:** 2
- **Pattern:** Play once, forward only
- **Trigger:** Player swipe on handle prompt
- **Purpose:** Tactile mechanism feedback
- **Audio Sync:** Mechanical ratchet locked to frame 2
- **Performance Optimization:** None needed

### Anouk Restocking (Sheet 5):
- **Duration:** 2.0 seconds per slot (1.0s per frame), ambient cycle every 20-40s
- **Frames:** 2
- **Pattern:** Idle → restock 1 → restock 2 → idle
- **Trigger:** Timer-based ambient; forced after any Empty Slot purchase attempt
- **Purpose:** The wall's life support made visible; empty slots eventually refill
- **Audio Sync:** Soft slot-thunk on frame 2
- **Performance Optimization:** Ambient cycle rate halved on Low LOD

### Theo Kitchen Loop (Sheet 5):
- **Duration:** 1.6 seconds per cycle (0.8s per frame)
- **Frames:** 2
- **Pattern:** Continuous loop, glimpsed through window
- **Trigger:** Constant
- **Purpose:** Factory efficiency, no wasted motion — never stops moving
- **Audio Sync:** Fryer sizzle bed continuous; basket clank on frame 1
- **Performance Optimization:** Static single frame on Low LOD

### Fluorescent Flicker (Sheet 6):
- **Duration:** 0.4-second burst, random trigger ~every 45s
- **Frames:** 2
- **Pattern:** Steady → flicker burst → steady
- **Trigger:** Random timer (subtle; this is a HAPPY fluorescent place)
- **Purpose:** Institutional authenticity without menace
- **Audio Sync:** Hum dip during burst
- **Performance Optimization:** Disabled on Low LOD and in reduced-motion mode

### Steam & Condensation (Sheets 1 & 6):
- **Duration:** Doorway wisp 1.2s loop; compartment steam 0.8s one-shot
- **Frames:** 2 loop / 1 burst
- **Pattern:** Doorway continuous; compartment on door-open only
- **Trigger:** Constant / purchase event
- **Purpose:** Warmth radiating into the night — the beacon promise
- **Audio Sync:** None (ambience carries it)
- **Performance Optimization:** Simplified steam per profile: doorway static, compartment burst kept

### 3 AM Atmosphere (Sheet 6):
- **Duration:** 4-second alpha breathe cycle (0.20 → 0.30 → 0.20)
- **Frames:** 1 (gradient texture, alpha animated)
- **Pattern:** Slow loop, 2-4 AM only
- **Trigger:** In-game clock
- **Purpose:** Peak FEBO; dreamlike warmth; slight reverb pairing
- **Audio Sync:** Audio bus gains slight reverb while overlay active
- **Performance Optimization:** Fixed 25% alpha (no breathe) on Low LOD

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Compartment Outline Set | (128, 96) | 192x64 | Three 64x64 bold-outline door states (closed/open/empty) — Sheet 6 reserve block |
| Coin Plate High-Contrast | (320, 96) | 96x96 | Black-on-yellow insert-turn plate — Sheet 6 reserve block |
| Counter Interaction Marker | (416, 96) | 64x64 | Bold outline marker for Anouk's counter — Sheet 6 reserve block |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Doorway Steam | Sheet 1 (Steam Wisp frame 1) | 96x64 | Reduced-motion locks steam to a single faint frame |
| No-Flicker Fluorescent | Sheet 6 (Flicker Strip frame 1) | 64x32 | Steady-tube substitute |
| Fixed 3 AM Overlay | Sheet 6 (3 AM Gradient) | 256x128 | Constant alpha, no breathing |
| Static Munchies Marker | Sheet 7 (Munchies Bonus Indicator) | 64x64 | Non-shimmer UI badge replaces sprite shimmer |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Coin Clunk Icon | (448, 192) | 24x24 | Coin glyph flash on insertion, mirrors clunk (Sheet 6 reserve block) |
| Door Pop Icon | (472, 192) | 24x24 | Burst glyph on door open, mirrors pop |
| Fryer Sizzle Waves | (448, 216) | 24x24 | Heat-wave glyph over kitchen window, mirrors sizzle bed |
| Satisfied Sigh Marker | (472, 216) | 24x24 | Soft breath glyph over eating NPCs, mirrors sigh audio |

### Colorblind Considerations:
- Occupied vs. empty compartments coded by light + interior food silhouette + door-glass shine, never red light alone
- Status icons use unique silhouettes (mug of warmth, cheese wedge, noodle disc, chili, plate, linked hands)
- Mystery Item wrapped state uses "?" embossing, not color coding
- Touch zones minimum 44px for every wall slot, coin plate, and counter interaction

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) interior background and menu board kept uncompressed (readable text)
- **Fallback:** PNG high quality for febo_interior_main.png (scene-detail critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| febo_environment | febo_exterior, febo_wall_grid | 2048x2048 |
| febo_characters | npc_febo_staff_customers | 1024x1024 |
| febo_fx_ui | febo_food_items, febo_effects, febo_ui | 1024x1024 |

*(febo_interior_main.png loads standalone as a scene background; max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full steam, flicker, restock ambients, 3 AM breathing overlay, munchies shimmer |
| Medium | Steam bursts only, flicker off, ambients at half rate |
| Low | Static steam/crowd/Theo, fixed 3 AM alpha, door frames only (profile: simplified steam, static crowd, reduced compartment animations) |

### Performance Targets:
- **Target FPS:** 60 (per location performance budget)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 34 MB maximum
- **Particle Limit:** 15 (steam, condensation drips, fryer glow motes)

### Performance Notes:
- One crowd block sprite per time period — never individual crowd NPCs beyond the featured five
- Wall = 1 grid sprite + per-slot overlays batched from a single atlas (2 draw calls total)
- Interior background is static; all life comes from small overlays

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (interior background), TileMap NOT required (grid handled via slot Area2D array), AnimatedSprite2D (doors, NPCs, steam), CPUParticles2D (steam motes — not GPU), CanvasLayer (wall UI), CanvasModulate (3 AM warmth)
- Special systems: per-slot state machine (stocked/empty/open), daily Mystery Item seed, time-of-day crowd table (6 periods), Munchies Pipeline timer (2-hour window from De Groene Gids), visit counter for FEBO Regular status, 3 AM event flag (2-4 AM)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Coin Insert Sparkle | Coin clunk | On insertion tap |
| Handle Turn frame 2 | Mechanical ratchet | 0.2s into turn |
| Door Opening frame 3 | Door pop + steam hiss | 0.6-0.7s |
| First bite (eating pose 2) | Satisfied eating sound | On pose swap |
| Hot-Bite Steam Sting | Kroket-temperature yelp | On first kroket bite, first visit |
| Fluorescent flicker burst | Hum dip | During 0.4s burst |
| 3 AM overlay active | Reverb bus enable | 2:00 AM in-game |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| FEBO Achievement Track ("Wall Beginner" → "Wall Completionist") | Achievement badges strip, all food sprites | First visit, 5 visits, Mystery Item, 3 AM visit, all items tried |
| The Munchies Pipeline | Munchies shimmer + bonus indicator | Arrival within 2 hours of De Groene Gids; +50% HP food |
| FEBO Regular Status | Anouk Recognition Nod, Regular badge | 3+ visits; occasional extra napkin (the rarest of gifts) |
| 3 AM FEBO Experience | 3 AM crowd block, Philosopher, Community Glow Ring | Visit 2-4 AM; +Community, -Judgment |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| De Groene Gids | Munchies shimmer pipeline | Food HP +50%; "best thing I've ever eaten" (2 Sovs kroket) |
| Casa Rosé | Standing ledge as processing space | Post-show neutral-zone dialogue triggers |
| The Tolerance Hostel | Food acquired popup referenced in kitchen talk | Late-night discovery conversations |
| Proeflokaal 't Kansen | Grease-absorption food effects | Reduces The Shakes debuff duration |
| Voetgangerstunnel | Rear heating-unit wall section (restock door area) | Hidden FEBO Emergence exit from the tunnel; 3 AM vibes always |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A warm yellow machine that loves you at your worst"
- **Color Mood:** FEBO yellow and compartment amber against night black — institutional light rendered as comfort, not menace
- **Lighting:** Harsh overhead fluorescent softened by dozens of tiny warm compartment glows; 3 AM overlay warms everything further
- **Texture:** Chrome polished by a million hands, glass fogged by eternal steam, wrappers and worn ledges — clean enough, loved completely

### Environmental Storytelling:
- The always-full trash bin and always-empty napkin dispenser tell you everything about throughput
- Window food photos that outshine reality — standard practice, honestly deployed
- The "SINCE 1941" door text is true, and the wall's chrome wear proves it
- The clock face is always visible: FEBO wants you to know what hour your choices are happening at

### Character Integration Notes:
- Anouk stays behind the counter; her Recognition Nod is the location's emotional payoff
- Theo exists only through the kitchen window — the wall provides, he sustains
- The Philosopher renders slightly closer to camera at 3 AM; his kroket is held like a relic
- Crowd blocks must read as community, not obstacle — everyone at the wall is in this together

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **THE WALL in Full Glory** — 24 glowing doors, symmetric, shareable as pure aesthetic
2. **The Philosopher's Communion** — a man and his kroket at 3 AM
3. **The Empty Slot** — one dark door in a wall of light; universal despair image
4. **Mystery Reveal** — the wrapped item mid-unwrap, fate deciding
5. **3 AM Crowd Block** — club refugees, shift workers, and tourists shoulder to shoulder

### Quote Potential:
- "The wall provides. The wall judges not."
- "The kroket... it is warm... like... like the universe was once warm... you know?"
- "Yes, that's meat. Probably."
- "You belong to the wall now. The wall belongs to you."
- "This is better than 18 Sovs pancakes. I need to DOCUMENT this realization."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | febo_exterior.png | 1024x512 |
| 2 | febo_interior_main.png | 1920x1080 |
| 3 | febo_wall_grid.png | 1024x1024 |
| 4 | febo_food_items.png | 256x256 |
| 5 | npc_febo_staff_customers.png | 1024x512 |
| 6 | febo_effects.png | 512x256 |
| 7 | febo_ui.png | 512x512 |

**Total Estimated Memory:** ~22 MB in-memory (uncompressed RGBA worst case), within the 34 MB location budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `febo_exterior.png` (1024x512)
- [ ] `febo_interior_main.png` (1920x1080)
- [ ] `febo_wall_grid.png` (1024x1024)
- [ ] `febo_food_items.png` (256x256)
- [ ] `npc_febo_staff_customers.png` (1024x512)
- [ ] `febo_effects.png` (512x256)
- [ ] `febo_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + wall-slot anchor map (grid coordinates for all 24 doors)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: the empty-slot despair, the always-broken change machine, the always-empty napkin dispenser, the Philosopher's kroket
- [ ] Accessibility visual alternatives included for all audio cues (coin clunk, door pop, sizzle, sigh)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (affectionate portrait — the tourist experience is the joke, never FEBO)
- [ ] Hidden areas/interactions have discoverable visual cues (Mystery Row, restock door / tunnel emergence wall, Regular's efficiency)
- [ ] Performance optimized (CPU particles, atlas limits respected, one crowd block per period)
- [ ] Touch zone sizing considered (44px minimum for wall slots, coin plate, counter)
- [ ] Colorblind-friendly alternatives available where color codes meaning (occupancy silhouettes, status icon shapes)
- [ ] Social media viral potential maximized in composition choices (THE WALL symmetric hero framing)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Central Shamsterdam; Dutch in-world text ("AUTOMATIEK", "24 UUR") |
| Cultural Specificity | ✅ | Real beloved Dutch automat culture, rendered with explicit affection per profile |
| Satirical Targets Appropriate | ✅ | 3 AM decisions and tourist confusion — the institution itself is honored |
| Seedy Underbelly Present | ✅ | 24-hour enabling of questionable choices, munchies pipeline, coin-operated regret |
| Gameplay Value Established | ✅ | Wall interaction system, Mystery gamble, time-based crowds, status effects, Regular track |
| Technical Feasibility | ✅ | Slot-overlay architecture, crowd blocks, static fallbacks all documented |
| Performance Budget | ✅ | 60 FPS, 14 draw calls, 34 MB, 15 particles per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all audio cues, no-flicker/no-shimmer modes, 44px touch zones |
| No Crypto Elements | ✅ | Pure coin-operated tradition; the machines don't even take card |
| Social Media Integration | ✅ | 5 screenshot moments + 5 quotable lines identified |

**Once these assets ship, FEBO becomes the game's warmest room: a wall of light where every player, at their lowest hour, pulls a handle and is fed without a single question asked.**
