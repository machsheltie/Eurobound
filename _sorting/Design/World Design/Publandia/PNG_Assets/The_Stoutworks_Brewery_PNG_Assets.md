# The Stoutworks Brewery - Complete PNG Asset Requirements

## 📋 Overview
A 25 Sovs brewery tour that derails into a six-floor dungeon crawl when the 150-year-old heritage yeast strain achieves consciousness and decides it IS the brewery. This document specifies every sprite for Publandia's cathedral of beer production — Victorian industrial grandeur, sentient foam, the Vat Master's three-phase existential crisis, and a gift shop that stays open through the apocalypse because commerce always finds a way.

**Location ID:** `publandia_dungeon_stoutworks_01`
**Theme:** Brewery-tourism-as-religious-experience parody — the "living beer culture" taken literally, then hostile
**Zone:** Brewery District, Industrial Beer Quarter
**Hours:** Tours 10:00-18:00; Dungeon accessible 24/7 (the yeast never sleeps)
**Primary Function:** Major dungeon / Vat Master boss (defeat OR negotiate) / tour mode attraction / Brewery Passport stamp stop / gift shop economy

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Copper | #B87333 | Stills, fittings, boss arena glow |
| Stout Black | #1A1A1A | Vats, shadows, deep fermentation |
| Brick Red | #8B4513 | Victorian exterior, interior walls |
| Steam White | #F5F5F5 | Steam, foam crests, vapor |
| Yeast Cream | #F0E68C | Golems, foam bodies, the living culture |
| Hazard Amber | #FF8C00 | Warning lights, fire pockets, meltdown state |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/stoutworks_brewery/
├── environment/
│   ├── stoutworks_exterior.png
│   ├── welcome_giftshop.png
│   ├── dungeon_tileset_upper.png
│   └── dungeon_tileset_lower.png
├── npcs/
│   └── brewery_characters.png
├── objects/
│   └── (packed into tilesets and ui sheet)
├── effects/
│   └── brewery_hazards_effects.png
├── boss/
│   └── vat_master.png
└── ui/
    └── stoutworks_ui_tour.png
```

---

## 🏭 Sprite Sheet 1: Exterior — The Cathedral of Beer
**File:** `stoutworks_exterior.png`
**Dimensions:** 512x512 pixels

### Building Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Brewery Facade | (0, 0) | 320x384 | Massive Victorian red brick, copper fittings, dominates the skyline |
| Chimney Stack | (320, 0) | 96x256 | Steam rising day and night |
| Copper Dome Detail | (416, 0) | 96x96 | Rooftop still-house crown |
| Main Sign | (320, 256) | 192x64 | "THE STOUTWORKS" in copper lettering |
| Subtitle Plaque | (320, 320) | 192x32 | "Est. 1869 — Publandia's Finest Since Before Your Grandfather's Grandfather" |
| Tour Office Front | (0, 384) | 128x128 | "BREWERY EXPERIENCE — Book Your Journey" |
| Closure Notice | (128, 384) | 96x64 | "Temporary Closure Due to 'Maintenance Issues'" — quotes doing heavy lifting |
| Staff Only Warning | (128, 448) | 96x48 | "Staff Only Beyond This Point" (ignored) |
| Entrance Doors | (224, 384) | 96x128 | Grand double doors, brass and oak |
| Conveyor Walkway | (320, 352) | 192x64 | Elevated belt link to smaller facilities |
| Cobble Yard Tile | (320, 416) | 64x64 | Brewery District ground |
| Small Facility Silhouette | (384, 416) | 128x96 | Surrounding brewing buildings, background layer |

### Technical Notes:
- Chimney steam is emitted at runtime (effects sheet) — the exterior always breathes
- Closure Notice only posts after "The Yeast Situation" quest activates; sign swap via layer toggle

---

## 🛍️ Sprite Sheet 2: Welcome Center, Gift Shop & Tasting Room
**File:** `welcome_giftshop.png`
**Dimensions:** 512x384 pixels

### Floor 1 — Welcome Center (Safe Zone):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Welcome Hall | (0, 0) | 256x192 | Tour waiting area, polished floors, corporate cheer |
| History Exhibit | (256, 0) | 128x96 | "History of Stoutworks" displays, 1869 onward |
| Ticket Desk | (384, 0) | 128x96 | 25 Sovs validation point |
| Tour Route Sign | (256, 96) | 96x64 | Arrowed path — the safe rails |
| Save Point Cask | (352, 96) | 64x64 | Last save before descent, glowing tap |
| Info Display Board | (416, 96) | 96x64 | Brewing process education panel |

### The Gift Shop (Open Through the Apocalypse):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gift Shop Interior | (0, 192) | 192x128 | Ironic commerce hub, before AND after dungeon |
| Merch Shelf | (192, 192) | 96x96 | T-shirts, mugs, tap handles at retail markup |
| Branded Rack | (288, 192) | 96x96 | "I Survived Stoutworks" display (post-dungeon stock) |
| Register Counter | (192, 288) | 96x64 | Still staffed. Nobody asks how |

### The Tasting Room:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tasting Bar | (0, 320) | 192x64 | Beer flight options, free tour pint |
| Beer Flight Tray | (288, 288) | 64x32 | Four sampler glasses |
| Stamp Station | (384, 192) | 128x128 | Where Fiona stamps the Brewery Passport |
| Brewmaster's Wall | (384, 320) | 128x64 | Photos of past brewmasters — O'Sullivan's frame slightly askew |
| Fermentation View Window | (288, 320) | 96x64 | Glass wall into the halls — ominous foreshadowing, something moves |

### Technical Notes:
- Fermentation View Window has a two-state layer: peaceful bubbling (tour) / a shape pressing the glass (post-trigger)
- Stamp Station doubles as tour-mode and post-boss stamp point

---

## 🌾 Sprite Sheet 3: Dungeon Tileset — Upper Floors (Malt House & Mash Tuns)
**File:** `dungeon_tileset_upper.png`
**Dimensions:** 512x512 pixels

### Floor 2 — The Malt House:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Malt Mountain Large | (0, 0) | 128x128 | Grain pile, subtly shifting — it's animated because it's ALIVE |
| Malt Pile Small | (128, 0) | 64x64 | Scatter variant |
| Barley Shift Frames 1-2 | (128, 64) | 128x64 | Two 64x64 grain-ripple states |
| Brick Wall Tile | (192, 0) | 64x64 | Interior Victorian brick, tileable |
| Industrial Window | (256, 0) | 64x64 | Grimy daylight grid |
| Iron Walkway Tile | (320, 0) | 64x64 | Catwalk floor, tileable |
| Walkway Railing | (384, 0) | 128x32 | Safety theater |
| Pipe Run | (384, 32) | 128x32 | Wall-mounted copper piping |
| Conveyor Belt Frames 1-2 | (0, 128) | 128x64 | Two 64x64 belt states for movement illusion |
| Conveyor Corner | (128, 128) | 64x64 | Turn segment |
| Conveyor Rollers | (192, 128) | 64x64 | Under-belt mechanics |
| Milling Room Gate | (256, 64) | 96x128 | Mini-boss chamber entrance |
| Milling Machinery | (352, 64) | 160x128 | The Miller's backdrop — grinders, belts, menace |

### Floor 3 — The Mash Tuns:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mash Tun Colossal | (0, 192) | 160x192 | Massive vessel, rivets and rim froth |
| Mash Tun Pair | (160, 192) | 128x128 | Smaller twin vessels |
| Catwalk Over Tuns | (288, 192) | 224x64 | Elevated traversal, steam below |
| Temperature Valve Wheel | (288, 256) | 64x64 | Puzzle interactive — too hot = damage, too cold = spawns |
| Temperature Gauge | (352, 256) | 64x64 | Puzzle readout, needle states |
| Steam Pipe Joint | (416, 256) | 64x64 | Vent source anchor |
| Industrial Floor Tile | (0, 384) | 64x64 | Wet concrete, tileable |
| Floor Drain | (64, 384) | 64x64 | Where the mash goes |
| Grain Scatter Overlay | (128, 384) | 64x64 | Battle-debris dressing |
| "STAFF ONLY" Door | (192, 384) | 64x96 | The tour-to-dungeon threshold |
| Tour Rope Barrier | (256, 384) | 96x48 | The safe rails, soon irrelevant |
| Derailment Marker | (256, 432) | 96x48 | Abandoned tour-group items: dropped lanyard, single shoe |
| Wall Lamp Industrial | (352, 384) | 48x64 | Caged bulb, dungeon lighting |
| Emergency Sign | (400, 384) | 112x48 | "IN CASE OF YEAST: RUN" (added recently, handwritten) |

### Technical Notes:
- All floor/wall tiles are 64px-grid tileable; conveyor frames alternate at 0.3s for belt motion
- Temperature puzzle uses gauge needle sprite rotation — no extra frames needed

---

## 🍺 Sprite Sheet 4: Dungeon Tileset — Lower Floors (Fermentation, Barrels & Copper Cathedral)
**File:** `dungeon_tileset_lower.png`
**Dimensions:** 512x512 pixels

### Floor 4 — The Fermentation Halls:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fermentation Vat Huge | (0, 0) | 160x224 | Stout Black tank, rim foam active — golem spawn point |
| Vat Bubbling Frames 1-2 | (160, 0) | 128x64 | Two 64x64 surface states |
| Vat Porthole | (160, 64) | 64x64 | Something looks back |
| Foam Spill Edge | (224, 64) | 64x64 | Overflow lip, tiles against floor |
| Dark Catwalk Tile | (288, 0) | 64x64 | Floor 4-6 traversal, tileable |
| CO2 Mist Band | (352, 0) | 160x48 | Low-lying vapor strip — damage zone dressing |
| Friendly Colony Alcove | (288, 64) | 96x96 | Hidden diplomacy area — softer light, calm foam |
| Drainage Valve Cluster | (384, 64) | 128x96 | Vat drainage sequence puzzle interactives |

### Floor 5 — The Barrel Aging Rooms:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Barrel Stack | (0, 224) | 128x96 | Aged oak wall, wraith territory |
| Single Barrel | (128, 224) | 48x64 | Prop and projectile |
| Rolling Barrel Frames 1-2 | (176, 224) | 96x64 | Two 48x64 roll states — dodge hazard |
| Whiskey Fire Pocket | (272, 224) | 64x64 | Blue-amber flame hazard |
| Angel's Share Shimmer | (336, 224) | 48x96 | Evaporation column — puzzle navigation marker |
| Dark Aging Wall | (384, 160) | 128x128 | Quieter, darker, aged threats |

### Floor 6 — The Copper Cathedrals (Boss Floor):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Copper Still Colossal | (0, 320) | 192x192 | The cathedral centerpiece — beautiful and dangerous; selfie backdrop |
| Copper Still Mid | (192, 320) | 128x160 | Flanking vessel |
| Cathedral Floor Plate | (320, 320) | 64x64 | Polished arena tile, tileable |
| Arena Entry Arch | (320, 384) | 64x128 | Final approach threshold |
| Overhead Gantry | (384, 320) | 128x48 | Moving-parts hazard track |
| Heat Glow Wall | (384, 368) | 128x64 | Radiant copper backwall |
| Pipe Organ Array | (384, 432) | 128x80 | Vertical pipes — cathedral acoustics made literal |

### Technical Notes:
- Boss arena assembles from Cathedral Floor Plate + stills + gantry — Phase 3 meltdown re-lights the same geometry Hazard Amber
- Friendly Colony Alcove only spawns its entrance if the player explores off the vat drainage path (secret gate condition)

---

## 👾 Sprite Sheet 5: Enemies & NPCs
**File:** `brewery_characters.png`
**Dimensions:** 512x384 pixels

### Enemy Roster:
| Enemy | Position | Size | Description |
|-------|----------|------|-------------|
| The Miller (Mini-Boss) | (0, 0) | 96x128 | Animated milling equipment, grinding intent |
| Mash Monster | (96, 0) | 64x96 | Scalding sludge rising from a tun |
| Yeast Golem | (160, 0) | 64x96 | Main enemy — Yeast Cream humanoid, confused about its purpose |
| Barrel Wraith | (224, 0) | 64x96 | Veteran threat, stave-bodied, whiskey-soaked |
| Grain Golem | (288, 0) | 48x64 | Basic swarm unit, barley-bodied |
| CO2 Specter | (336, 0) | 48x64 | Translucent suffocation wisp |
| Foam Elemental | (384, 0) | 48x48 | Obscuring cloud with eyes |
| Friendly Yeast | (432, 0) | 48x48 | Diplomacy ally — smaller, calmer formation |
| Yeast Golem Forming 1-2 | (384, 48) | 96x48 | Two 48x48 mid-formation frames ("FORMING A HUMANOID SHAPE") |

### Staff NPCs:
| NPC | Position | Size | Description |
|-----|----------|------|-------------|
| Fiona Guide (Tour) | (0, 128) | 64x96 | Brewery uniform, corporate enthusiasm |
| Fiona Disheveled | (64, 128) | 64x96 | Post-trigger — hiding, escaped, or rescue target |
| Brewmaster O'Sullivan | (128, 128) | 64x96 | Traditional attire, found on the negotiate route |
| Enemy Vat Emergence 1-2 | (192, 128) | 128x96 | Two 64x96 spawn-from-vat frames, shared by vat enemies |
| Grain Golem Swarm Clump | (320, 128) | 96x64 | Three-unit group sprite for swarm economy |
| Fiona Rescue Pose | (416, 128) | 64x96 | Relieved, "maybe therapy" state |

### Dialogue Portraits (64x48 each):
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Fiona Portrait (Tour) | (0, 224) | 64x48 | "150 years of brewing excellence await!" |
| Fiona Portrait (Panic) | (64, 224) | 64x48 | "I was using 'alive' as a METAPHOR." |
| O'Sullivan Portrait | (128, 224) | 64x48 | "It finally talked back." |
| Friendly Yeast Portrait | (192, 224) | 64x48 | "Not all of us want war." |
| Vat Master Portrait | (256, 224) | 64x48 | Boss dialogue frame, bubbling constantly |

### Attack Overlays:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Scalding Splash AOE | (0, 272) | 96x64 | Mash Monster attack telegraph |
| Fermentation Aura Ring | (96, 272) | 64x64 | Yeast Golem DoT indicator |
| Rolling Charge Trail | (160, 272) | 96x48 | Barrel Wraith wind-up |
| Suffocation Grasp | (256, 272) | 64x64 | CO2 Specter defense-bypass telegraph |
| Grinding Zone | (320, 272) | 96x64 | Miller damage floor marker |
| Obscuring Cloud Burst | (416, 272) | 64x64 | Foam Elemental vision block |

---

## 🫧 Sprite Sheet 6: The Vat Master
**File:** `vat_master.png`
**Dimensions:** 512x256 pixels

### Boss Phases:
| Phase | Position | Size | Description |
|-------|----------|------|-------------|
| Phase 1 — The Swarm | (0, 0) | 128x192 | Semi-formed colony commanding golem waves, invulnerable shimmer |
| Phase 2 — The Confrontation | (128, 0) | 160x224 | Full physical manifestation — massive yeast-foam construct, vaguely humanoid, bubbling constantly |
| Phase 3 — The Meltdown | (288, 0) | 192x256 | Desperate form, Hazard Amber veining, brewery systems haywire behind it |

### Boss Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Negotiate Calm State | (0, 192) | 96x64 | Settled, listening posture crop — "Tell me... what am I?" |
| Foam Tsunami Crest | (96, 192) | 128x64 | Arena-wide dodge-check wave head |
| Living Culture Absorb | (224, 192) | 64x64 | Healing intake vortex |
| Peaceful Hover (Epilogue) | (288, 256-64) | — | See Technical Notes: Peaceful Hover uses Phase 1 sprite recolored at runtime |
| Colony Core Glow | (224, 192) | — | Packed with absorb; core highlight is additive overlay on any phase |

### Technical Notes:
- Phase sprites share one anchor baseline (y-bottom) so transitions scale up in place — 128→160→192 wide reads as escalation
- Peaceful/diplomatic epilogue reuses Phase 1 with a calm-tint shader; no fourth sprite needed
- All phases bubble constantly: 2-frame surface boil via UV offset, not extra frames

---

## 💨 Sprite Sheet 7: Hazards & Effects
**File:** `brewery_hazards_effects.png`
**Dimensions:** 512x256 pixels

### Environmental Hazards:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Steam Vent Burst 1-3 | (0, 0) | 192x96 | Three 64x96 eruption frames — timing puzzle core |
| Foam Flood Spread 1-3 | (192, 0) | 192x64 | Three 64x64 creep frames — slippery, obscuring |
| Foam Bubble Particle | (384, 0) | 32x32 | Physics dressing |
| Yeast Particle | (416, 0) | 32x32 | Ambient culture motes |
| Grain Dust | (448, 0) | 32x32 | Malt house air |
| CO2 Vapor Wisp | (480, 0) | 32x32 | Pocket zone particle |
| Steam Ambient Column | (384, 32) | 64x96 | Constant atmosphere riser |
| Conveyor Motion Lines | (448, 32) | 64x32 | Forced-movement indicator |

### Combat & Boss Effects:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Enemy Emergence Splash | (0, 96) | 64x64 | Vat-spawn foam burst |
| Fermentation Wave Band | (64, 96) | 192x48 | Phase 1 party-wide DoT sweep |
| CO2 Burst | (256, 96) | 64x64 | Targeted suffocation pop |
| Meltdown Alarm Light | (320, 96) | 64x64 | Rotating Hazard Amber beacon |
| Falling Barrel Shadow | (384, 128) | 64x64 | Phase 3 drop telegraph |
| Phase Transition Flash | (0, 160) | 96x96 | Boss escalation burst |
| Negotiate Calm Glow | (96, 160) | 96x96 | Diplomacy route aura |
| Defeat Dissolve 1-2 | (192, 160) | 128x96 | Two 64x96 collapse frames |
| Heat Shimmer Band | (320, 160) | 128x32 | Copper cathedral air distortion |
| Whisper Wisp | (448, 96) | 32x32 | "The Vat's Whisper" cosmetic status |
| Chimney Steam Puff 1-2 | (448, 160) | 64x64 | Two 32x64 exterior frames |
| Tour Derail Record-Scratch Frame | (320, 192) | 96x64 | Freeze-frame vignette for the derailment beat |

---

## 🎮 Sprite Sheet 8: UI & Brewery Tour Assets
**File:** `stoutworks_ui_tour.png`
**Dimensions:** 512x256 pixels

### Dungeon UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Boss Health Bar | (0, 0) | 256x32 | Vat Master HP, foam-head fill |
| Floor Progress Tracker | (256, 0) | 96x32 | Six-floor clear status |
| Hazard Indicator | (352, 0) | 64x32 | Environmental warning chip |
| Fermented Fury Icon | (416, 0) | 32x32 | +15% Attack buff |
| Vat's Whisper Icon | (448, 0) | 32x32 | Cosmetic yeast-thoughts status |
| Peaceful Fermentation Icon | (480, 0) | 32x32 | Negotiate-route beer bonus |
| Dungeon Map | (0, 32) | 128x160 | Floor navigation, non-linear Floor 4 web |
| Negotiation Options Panel | (128, 32) | 128x96 | Diplomacy choices — "Really listen." |
| Gift Shop UI | (256, 32) | 128x96 | Commerce interface, apocalypse-proof |
| Tour vs Dungeon Select | (384, 32) | 96x64 | Mode split screen |
| Brewmaster's Pass | (384, 96) | 64x64 | Permanent access token |
| Stamp: Stoutworks | (448, 96) | 64x64 | Hop-vine border, copper still, steam wisps, "Est. 1869 — Publandia's Finest," copper bronze ink |

### Brewery Tour & Gift Shop Items:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stamp Animation 1-4 | (128, 128) | 256x64 | Four 64x64 stamping-sequence frames |
| Vat Master's Reserve Bottle | (384, 160) | 32x64 | 9.5% imperial stout, absorbed the whiskey barrel AND the awareness |
| Vat Master's Reserve Pint | (416, 160) | 32x48 | Poured, faint shimmer |
| Selfie Frame: Victory | (0, 192) | 96x64 | Copper stills + debris variant |
| Selfie Frame: Diplomatic | (96, 192) | 96x64 | Peaceful Vat Master hovering in background |
| Copper Mug | (192, 192) | 32x32 | +Alcohol resistance |
| Stoutworks T-Shirt | (224, 192) | 32x32 | +5 Defense, 30 Sovs |
| "I Survived Stoutworks" Shirt | (256, 192) | 32x32 | Post-dungeon flex |
| Yeast Sample (Contained) | (288, 192) | 32x32 | Throwable temporary ally |
| Commemorative Tap Handle | (320, 192) | 32x32 | Weapon, +Brewing damage |
| Copper Still Keychain | (352, 192) | 32x32 | Cosmetic collection |
| Steam-Proof Jacket | (192, 224) | 32x32 | +Steam resistance |
| Stoutworks Pint Glass | (224, 224) | 32x32 | +5% HP from beer |
| Brewmaster's Recipe Book | (256, 224) | 32x32 | +10% beer item effectiveness |
| "History of Brewing" Book | (288, 224) | 32x32 | +Intelligence, dungeon hints |
| Grain Shield | (320, 224) | 32x32 | Floor 2 clear reward |
| Steam Goggles | (352, 224) | 32x32 | Floor 3 clear reward |
| Foam-Proof Boots | (384, 224) | 32x32 | Floor 4 clear reward |
| Barrel-Aged Whiskey | (416, 224) | 32x32 | Floor 5 premium consumable |
| Brewmaster's Mallet | (448, 224) | 32x32 | Defeat-route weapon |
| Living Yeast Sample | (480, 224) | 32x32 | Negotiate-route companion |
| Stoutworks Medal | (448, 160) | 32x32 | Defeat-route trophy |
| Allied Brewery Crest | (480, 160) | 32x32 | Negotiate-route status icon |

### Technical Notes:
- Boss Health Bar fill drains as beer, not blood — foam head recedes with damage
- Selfie frames composite over the Copper Still Colossal backdrop from Sheet 4

---

## 🎬 Animation Specifications

### The Tour Derailment:
- **Duration:** 4 seconds
- **Frames:** Vat Bubbling normal → Porthole eye → Yeast Golem Forming 1-2 → Record-Scratch freeze-frame → combat music
- **Trigger:** Quest active + reaching Floor 2, or investigating "Staff Only" areas
- **Purpose:** The moment 25 Sovs of tourism becomes a dungeon — the location's thesis beat
- **Audio Sync:** Fiona's "That's not supposed to happen" on the porthole; corporate tour music cuts dead on the freeze-frame
- **Mobile Optimization:** Freeze-frame vignette dropped; hard cut instead

### Vat Bubbling (Ambient):
- **Duration:** 1.6-second loop
- **Frames:** 2 surface states, staggered per vat
- **Trigger:** Constant, both modes (peaceful tour / ominous dungeon tempo shift)
- **Purpose:** The brewery is alive; the tempo tells you how alive
- **Audio Sync:** Peaceful bubbling (tour) / wet squelching (dungeon)
- **Mobile Optimization:** Every second vat static on Low LOD

### Steam Vent Cycle:
- **Duration:** 4-second cycle (2s idle, 1s telegraph hiss, 1s burst)
- **Frames:** 3 burst frames
- **Trigger:** Timed per vent, offset patterns form the timing puzzle
- **Purpose:** Readable, learnable hazard rhythm
- **Audio Sync:** Hiss on telegraph, blast on frame 1 of burst
- **Mobile Optimization:** Burst frames reduced to 2

### Foam Flood:
- **Duration:** 3 seconds to full spread
- **Frames:** 3 spread states + bubble particles
- **Trigger:** Floor 4 zone events, Phase 2 "Foam Tsunami"
- **Purpose:** Slippery, obscuring, signature Floor 4 chaos
- **Audio Sync:** Rising fizz, wet slap at full spread
- **Mobile Optimization:** Simplified foam — spread states only, no particles

### Enemy Vat Emergence:
- **Duration:** 1.5 seconds
- **Frames:** Emergence Splash → Emergence 1-2 → enemy idle
- **Trigger:** Enemy spawn in vat rooms
- **Purpose:** Enemies come FROM the brewery — never just appear
- **Audio Sync:** Deep glorp on splash, squelch on formation
- **Mobile Optimization:** Splash-to-idle direct on Low LOD

### Boss Phase Transitions:
- **Duration:** 3 seconds per transition
- **Frames:** Phase Transition Flash → next phase sprite scale-in → arena state change (Phase 3 adds Meltdown Alarm + gantry movement + Falling Barrel shadows)
- **Trigger:** Phase 1 swarm thinned / Phase 2 HP threshold
- **Purpose:** Escalation readable at a glance; Phase 3 turns the room itself hostile
- **Audio Sync:** Vat Master's booming line on each flash ("NOW I AM MORE THAN BEER"); alarm klaxon loops in Phase 3
- **Mobile Optimization:** Alarm becomes static amber tint

### The Stamping:
- **Duration:** 1.2 seconds
- **Frames:** 4 (raise → press → ink → lift with reveal)
- **Trigger:** Stamp acquisition at Stamp Station (tour) or post-boss (dungeon)
- **Purpose:** Brewery Passport ritual — collection dopamine
- **Audio Sync:** Thunk on press, page rustle on lift
- **Mobile Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements
**File:** `stoutworks_accessibility.png` (supplemental sheet — delivered alongside the 8 base files, not counted in their total)
**Dimensions:** 256x256 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hazard Zones, Bold | (0, 0) | 96x96 | High-contrast striped borders for steam/CO2/fire/foam zones |
| Boss Bar, Bold | (96, 0) | 96x32 | Heavy-outline segmented HP with phase markers |
| Negotiation Panel, Bold | (96, 32) | 96x64 | Enlarged diplomacy options, thick dividers |
| Valve & Gauge Outlines | (192, 0) | 64x64 | Puzzle interactives in white-on-dark |
| "STAFF ONLY" Door Outline | (192, 64) | 64x64 | Mode-threshold highlight |
| Dungeon Map, Bold | (0, 96) | 96x96 | Enlarged floor labels, cleared-floor check icons |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Foam, Static | (96, 96) | 64x64 | Fixed foam texture replacing spread animation |
| Steam, Reduced | (160, 96) | 64x96 | Single soft column replacing burst cycle (hazard timing conveyed by telegraph icon) |
| Alarm, Steady | (224, 96) | 32x32 | Non-rotating amber state |
| Conveyor, Marked | (0, 192) | 64x32 | Static directional arrows replacing motion lines |
| Bubbling, Calm | (64, 192) | 64x32 | Single-state vat surfaces |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hiss Telegraph Icon | (128, 192) | 32x32 | Steam warning independent of audio |
| Glorp Ring | (160, 192) | 32x32 | Enemy emergence cue |
| Boss Boom Caption Frame | (192, 192) | 64x32 | Vat Master dialogue rendered as arena caption |
| Klaxon Flash Border | (0, 224) | 64x32 | Phase 3 alarm as screen-border pulse (steady variant available) |
| Squelch Blob | (64, 224) | 32x32 | Yeast movement cue |
| Stamp Thunk Star | (96, 224) | 32x32 | Stamping impact cue |
| Whisper Caption Wisp | (128, 224) | 32x32 | "The Vat's Whisper" text-cue variant |

### Colorblind Considerations:
- Hazard types coded by border pattern (stripes/dots/waves/cross-hatch), never zone tint alone
- Temperature gauge pairs needle position with hot/cold icons, not red/blue alone
- Negotiate vs. attack options carry distinct glyphs (open hand / mallet); all interactives meet the 44px minimum touch target

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (Vat Master phases and stamp at ASTC 4x4)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for boss phases and portraits

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| stoutworks_environment | exterior, welcome_giftshop, both tilesets | 2048x2048 |
| stoutworks_characters | brewery_characters, vat_master | 1024x512 |
| stoutworks_fx_ui | hazards_effects, ui_tour | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full foam physics dressing, all particle types, staggered vat bubbling, swarm clumps + individuals |
| Medium | Foam spread states only, halved particles, alternate vats static, swarms as clump sprites |
| Low | Static foam, steam telegraphs only, single-state vats, max 4 enemies on screen |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 18 per frame
- **Memory Footprint:** 48 MB maximum
- **Particle Limit:** 20 (steam + foam + yeast motes combined)

### Performance Notes:
- One floor resident at a time — floors stream on stair transitions
- Grain Golem swarms use the 3-unit clump sprite beyond 4 active enemies
- Phase 3 environmental chaos is choreographed (timeline), not simulated

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- TileMap per floor on a 64px grid; floors stream as sub-scenes; tour mode locks navigation to rope-barrier rails
- CPUParticles2D (not GPU) for steam, foam bubbles, grain dust, yeast motes; vat boil via 2-frame UV offset; all reduced-motion-compliant variants specified
- Mode split: `tour_mode` vs `dungeon_mode` — same scenes, different nav mesh, music, and spawn tables; derailment converts mid-scene
- Boss state machine: Swarm (invulnerable) → Confrontation → Meltdown; negotiate branch gated on `friendly_colony_found` flag from the Floor 4 alcove
- State tracking per `stoutworks_state` (mode, floors_cleared[], miller_defeated, friendly_colony_found, vat_master_outcome [defeated/negotiated], brewmasters_pass, stamp_acquired, fiona_rescued)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Tour derailment freeze-frame | Corporate music hard cut + record scratch | On freeze-frame |
| Steam vent burst | Hiss (telegraph) → blast | Hiss 1s before burst frame 1 |
| Enemy vat emergence | Deep glorp + squelch | Glorp on splash, squelch on formation |
| Boss phase flash | Vat Master boom line | Line starts on flash, phase sprite lands on line end |
| Phase 3 arena | Alarm klaxon loop | Loops while meltdown active |
| Negotiate Calm Glow | Music drops to a single sustained note | Fades in with glow |
| Stamp press | Thunk + page rustle | Thunk frame 2, rustle frame 4 |
| Vat Master's Reserve consumed | Faint whisper murmur (10% status) | 1s after drink, only on status proc |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Yeast Situation | Closure Notice, derailment sequence, all enemy sprites, boss phases | Craic Broker quest hook; investigate → clear → resolve Vat Master |
| Negotiate Route ("Brewing Partner") | Friendly Colony Alcove, Friendly Yeast, O'Sullivan, Negotiation Panel, Calm Glow, Diplomatic selfie | Requires finding the Floor 4 colony; changes ending, rewards, and Reserve beer bonus |
| Brewery Tour Sidequest | Stamp Station, Stamp + 4-frame animation, Reserve bottle/pint, selfie frames | Requires Bottle Opener Keychain from The Blarney Trap; stamp at Tasting Room (tour) or post-boss (dungeon) |
| Fiona's Rescue | Fiona Disheveled, Rescue Pose, both portraits | Optional dungeon objective; affects post-dungeon Tasting Room dialogue |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Blarney Trap | Quest origin and victory celebration; Sweet Surrender brewed here; Reserve + Academic Amber stocked there post-unlock | Standard district transition; Seamus/Fiona cross-referencing dialogue |
| Trinity of Pints | Academic Amber contract-brewed here; academic drinking challenges reference Stoutworks beer | Item-availability link |
| The Quiet Man | "Stoutworks Secret" rumor reveals the Friendly Colony Alcove | Rumor purchase sets `stoutworks_secret_hint` |
| Brewery District / Cobblestone Market Street | Conveyor walkways, closure rumors on the street | District ambient dialogue |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A Victorian cathedral where the congregation is yeast and the god just woke up"
- **Color Mood:** Copper warmth and Brick Red heritage corrupted floor by floor with Yeast Cream and Stout Black; Hazard Amber saved for the meltdown
- **Lighting:** Industrial fixtures and copper glow above; steam-diffused gloom below; boss arena lit like a shrine
- **Texture:** Riveted copper, wet concrete, breathing grain, foam with intent

### Environmental Storytelling:
- The Fermentation View Window's two states foreshadow everything from the safe side of the glass
- "IN CASE OF YEAST: RUN" handwritten under official signage — staff knew before management admitted it
- The Derailment Marker (dropped lanyard, single shoe) tells the last tour group's story
- The gift shop register, staffed through the apocalypse: commerce finds a way

### Character Integration Notes:
- Yeast Golems must read confused, not evil — heads tilt, forms slump; the tragedy is in the posture
- The Vat Master's three phases escalate in size and desperation, not menace; Phase 3 should look like panic
- The Negotiate Calm State is the emotional payoff sprite — settled foam, listening
- Fiona carries the tonal bridge: corporate polish to survivor, same uniform

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Copper Cathedral** - Massive stills in dramatic light — beautiful with or without the boss
2. **The Derailment Freeze-Frame** - A yeast golem forming mid-tour, record-scratch vignette
3. **The Diplomatic Selfie** - Player posing with a peaceful sentient yeast colony hovering behind
4. **Phase 2 Reveal** - The Vat Master fully manifested over a foam-flooded arena
5. **"IN CASE OF YEAST: RUN"** - Handwritten emergency signage
6. **The Gift Shop, Still Open** - Register staffed while the closure notice hangs outside

### Quote Potential:
- "FOR 150 YEARS I HAVE MADE YOUR BEER. NOW I AM MORE THAN BEER."
- "The yeast is supposed to be IN the beer, not FORMING A HUMANOID SHAPE."
- "...oh no. Oh no no no. I was using 'alive' as a METAPHOR."
- "We have to FIGHT a BEER? This is the greatest TRAGEDY of my LIFE."
- "You... you would speak with me? Not destroy? Tell me... what am I?"
- "You can taste the existential crisis. It's delicious."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | stoutworks_exterior.png | 512x512 |
| 2 | welcome_giftshop.png | 512x384 |
| 3 | dungeon_tileset_upper.png | 512x512 |
| 4 | dungeon_tileset_lower.png | 512x512 |
| 5 | brewery_characters.png | 512x384 |
| 6 | vat_master.png | 512x256 |
| 7 | brewery_hazards_effects.png | 512x256 |
| 8 | stoutworks_ui_tour.png | 512x256 |

**Total Estimated Memory:** ~24 MB

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `stoutworks_exterior.png` (512x512)
- [ ] `welcome_giftshop.png` (512x384)
- [ ] `dungeon_tileset_upper.png` (512x512)
- [ ] `dungeon_tileset_lower.png` (512x512)
- [ ] `brewery_characters.png` (512x384)
- [ ] `vat_master.png` (512x256)
- [ ] `brewery_hazards_effects.png` (512x256)
- [ ] `stoutworks_ui_tour.png` (512x256)
- [ ] `stoutworks_accessibility.png` (256x256, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (tour/dungeon sign swaps, window two-state, and boss phases on separate layers)
- **Documentation:** Animation timing reference sheet (derailment 4s, vent 4s cycle, phase transitions 3s, stamp 1.2s) + tileset grid guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Copper #B87333, Stout Black #1A1A1A, Brick Red #8B4513, Steam White #F5F5F5)
- [ ] All 64px-grid tiles verified seamless (walls, floors, catwalks, conveyor)
- [ ] Boss phase baselines aligned — transitions scale in place
- [ ] Stamp text legible at 64x64 ("Est. 1869 — Publandia's Finest")
- [ ] Accessibility visual alternatives included for all audio cues (hiss, glorp, boom, klaxon, thunk, whisper)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (brewery tourism reverence gone literal) is clear throughout all assets
- [ ] Hidden areas discoverable: Friendly Colony Alcove cue, porthole eye, "IN CASE OF YEAST" sign, askew brewmaster photo
- [ ] Mobile performance optimized (floor streaming, swarm clumps, 20-particle cap, choreographed meltdown)
- [ ] Touch zone sizing considered (44px minimum — valves, negotiation options, map floors compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (patterned hazard borders, icon-paired gauge)
- [ ] Social media viral potential maximized (cathedral composition, diplomatic selfie framing)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia Brewery District; Guinness Storehouse satirized without naming |
| Cultural Specificity | ✅ | Dublin-style brewing heritage commodification, tour-and-gift-shop ritual |
| Satirical Targets Appropriate | ✅ | Brewery tourism packaging, not brewing craft — profile-confirmed |
| Seedy Underbelly Present | ✅ | 25 Sovs tours ending in gift shops; the cover story vs. the yeast reality |
| Gameplay Value Established | ✅ | Full 6-floor dungeon, mini-boss, dual-ending boss, puzzles, stamp sidequest, shop economy |
| Technical Feasibility | ✅ | Floor streaming, clump-sprite swarms, choreographed Phase 3, mobile optimization documented |
| Mobile Performance Budget | ✅ | 60 FPS, 18 draw calls, 48MB |
| Accessibility Features | ✅ | Telegraph icons for every hazard, caption frames for boss booms, static-hazard variants |
| No Crypto Elements | ✅ | Absent from source and spec ("pure yeast-based currency of chaos" per profile QA) |
| Social Media Integration | ✅ | Six viral moments identified, quote bank sourced from profile |

**The Stoutworks Brewery delivers the full arc in one building: reverent tour, sudden horror, six floors of living beer, and a choice between destroying a frightened 150-year-old consciousness or actually listening to it. Every asset serves the escalation — and through all of it, the gift shop never closes.**

**"The tour is 25 Sovs. The dungeon is free if you survive."**
