# Brouwerij de Molen - Complete PNG Asset Requirements

## 📋 Overview
Brouwerij de Molen ("The Windmill Brewery") is a 350-year-old working windmill in the Shamsterdam countryside converted into a craft brewery mini-dungeon — a spinning building where tourists pay 25 Sovs to get dizzy while Brewmaster Hendrik lectures about respecting the grain and a Yeast Golem rises from the grinding floor. This document specifies every PNG asset across the four floors (ground/gift shop, grinding floor boss arena, tasting room, blade level), the exterior and countryside approach, the Yeast Golem boss with all three phases, staff and visitor NPCs, and the tasting/selfie/opener systems. Its satirical essence in a sentence: authentic Dutch heritage weaponized into Instagram bait that charges you to be disoriented.

**Location ID:** `shamsterdam_countryside_brouwerij_molen_01`
**Theme:** "Authentic" experience tourism — paying premium for discomfort disguised as tradition; craft beer pretension; windmill fetishization
**Zone:** Shamsterdam Countryside (short train ride from central, 8 Sovs round trip, views are fields)
**Hours:** 11 AM - 8 PM (brewery tour hours, last tour at 6 PM)
**Primary Function:** Brewery Tour Location #1 / mini-dungeon — Yeast Golem boss battle, tasting flight system with Spin Meter, brewmaster speech endurance challenge, selfie timing mini-game, bottle opener gating (Blarney Trap prerequisite + Windmill opener), "Canal Courage" quest progress

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Grain Gold | #DAA520 | Grain, beer, signage accents |
| Copper | #B87333 | Brewing vats, opener, candle reflections |
| Windmill Wood | #8B4513 | Structure, beams, barrels |
| Flour White | #FFFAF0 | Dust haze, golem body, flour clouds |
| Countryside Green | #6B8E23 | Flat Dutch landscape, train approach |
| Candle Warm | #FFB347 | Tasting room electric-candle glow |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/brouwerij_de_molen/
├── environment/
│   ├── brouwerij_molen_exterior.png
│   ├── molen_ground_floor.png
│   ├── molen_grinding_floor.png
│   └── molen_tasting_blade_level.png
├── npcs/
│   └── npc_molen_cast.png
├── boss/
│   ├── yeast_golem_battle.png
│   └── yeast_golem_phases.png
└── ui/
    └── molen_items_ui.png
```

---

## 🌾 Sprite Sheet 1: Exterior & Countryside
**File:** `brouwerij_molen_exterior.png`
**Dimensions:** 1024x768 pixels

### The Windmill:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Windmill Exterior Body | (0, 0) | 512x512 | Circa-1680 windmill, brewery conversion details, Instagram magnet silhouette |
| Blade Assembly Rotation 1-4 | (512, 0) / (704, 0) / (512, 192) / (704, 192) | 192x192 each | Four rotation positions; also driven by Godot node rotation for smooth spin |
| Entrance Door | (896, 256) | 96x128 | Heavy wooden door, "BROUWERIJ" carved above |
| Accessibility Ramp | (896, 192) | 128x64 | Modern EU-requirement ramp against ancient wood |

### Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Painted Sign | (896, 0) | 128x64 | "BROUWERIJ DE MOLEN — Est. 1680 / 2008" |
| Modern Sign | (896, 64) | 128x32 | "CRAFT BEER TOURS — TASTING FLIGHTS — GIFT SHOP" |
| Warning Sign | (896, 96) | 128x64 | "WINDMILL OPERATIONAL — BLADES ROTATE — WATCH HEAD" |
| Liability Sign | (896, 160) | 128x32 | "The spinning is intentional. The dizziness is not our fault." |

### Approach:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Train Station Exterior | (512, 384) | 512x256 | Rural platform, transport hub, tourists comparing tasting notes |
| Countryside Background | (0, 512) | 512x256 | Flat Dutch fields parallax strip (tileable horizontally) |
| Platform Tourist Cluster | (512, 640) | 256x128 | Photographing tourists waiting for the return train |

### Technical Notes:
- Blade assembly renders on separate node above windmill body; casts the interior window shadows (Sheet 3)
- Countryside strip tiles seamlessly for the "scenic" train ride transition
- Blade rotation speed varies with "wind" variable — sync with grinding mechanism speed

---

## 🛍️ Sprite Sheet 2: Ground Floor & Gift Shop
**File:** `molen_ground_floor.png`
**Dimensions:** 1024x512 pixels

### Reception & Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Reception Desk | (0, 0) | 256x128 | "Reclaimed barrel wood" (claimed), tour purchase point |
| Bottled Product Case | (256, 0) | 128x128 | Display bottles — available everywhere in the building |
| Windmill History Panels | (384, 0) | 192x128 | 5% windmill history, 95% beer marketing |
| Coat Hooks | (576, 0) | 64x128 | For the tasting flight aftermath |
| Gift Shop Shelving | (640, 0) | 256x128 | Branded EVERYTHING wall unit |

### Gift Shop Merchandise:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Branded Glasses Display | (0, 128) | 128x96 | "Molen" glasses 18 Sovs (the beer is 6 Sovs) |
| Mini Windmill Souvenirs | (128, 128) | 128x96 | 25 Sovs, made overseas, painted here |
| Brewmaster's Book Stack | (256, 128) | 96x96 | "Respect The Grain" 35 Sovs, self-published, unreadable |
| T-Shirt Rack | (352, 128) | 128x96 | "I SURVIVED THE SPIN" 30 Sovs (they know) |
| Survivor Pack Display | (480, 128) | 96x96 | Motion sickness pills 3 Sovs + water 2 Sovs = 5 Sovs "Survivor Pack" |

### Structure Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Curved Wall Segments 1-8 | (0, 224) to (224, 224), 32px steps | 32x32 each | Round-room wall pieces (it's a windmill) |
| Wood Plank Floor | (256, 224) | 32x32 | Base flooring |
| Worn Plank Floor | (288, 224) | 32x32 | Foot-traffic variant |
| "Rustic" Fixture | (320, 224) | 32x64 | IKEA 2015 light pretending to be heritage |
| Stairs Up | (384, 224) | 96x96 | To the grinding floor |
| Bram's Counter Zone | (480, 224) | 128x96 | Gift shop attendant post — unavoidable on entry AND exit |

### Technical Notes:
- Curved wall segments assemble the circular room via TileMap
- Gift shop displays are interaction hotspots (44px+ touch zones) with price-shock tooltips

---

## ⚙️ Sprite Sheet 3: Grinding Floor (Boss Arena)
**File:** `molen_grinding_floor.png`
**Dimensions:** 1024x1024 pixels

### The Grinding Mechanism:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Millstone Mechanism Rotation 1-4 | (0, 0) / (256, 0) / (512, 0) / (768, 0) | 256x256 each | Massive central grindstone, connected to blades, actually grinding |
| Wooden Gears Large | (512, 256) | 192x192 | Original, terrifying, functional |
| Gear Small Rotation 1-2 | (704, 256) / (832, 256) | 128x128 each | Secondary gear meshing |

### Brewing Equipment:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Copper Vat A / B / C | (0, 256) / (128, 256) / (256, 256) | 128x192 each | Spotlit brewing vats around the circle |
| Grain Storage Bins | (384, 256) | 128x128 | Open-topped, visible safety concern |

### Windows & Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Window Blade Shadow 1-4 | (0, 448) / (128, 448) / (256, 448) / (384, 448) | 128x128 each | Rotating blade shadow sweeping the room (disorienting) |
| "DO NOT TOUCH MACHINERY" Sign | (512, 448) | 160x64 | Five languages: Dutch, German, English, Japanese, Chinese |
| Danger Rail | (672, 448) | 128x32 | Tourists grab this when the floor vibrates |

### Arena & Atmosphere:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floor Vibration Overlay | (0, 576) | 512x128 | Shake-line overlay strip for grinding vibration |
| Flour Haze Overlay | (512, 576) | 256x256 | Semi-transparent dust atmosphere tile |
| Arena Floor Base / Flour-Dusted / Worn / Grain-Spill | (0, 704) / (32, 704) / (64, 704) / (96, 704) | 32x32 each | Boss arena floor tiles |
| Grain Dust Particles 1-2 | (128, 704) / (192, 704) | 64x64 each | Constant ambient dust |
| Boss Spawn Dust Swirl 1-3 | (256, 704) / (352, 704) / (448, 704) | 96x96 each | Unnatural swirl pattern preceding golem rise |
| Stairs Up / Stairs Down | (768, 576) / (864, 576) | 96x96 each | Floor transitions |

### Technical Notes:
- Millstone rotation speed syncs to exterior blade speed (shared "wind" variable)
- Floor Vibration Overlay pulses while grinding — also ripples beer glasses (Sheet 8 liquid ripple)
- Flour haze density drops per LOD tier

---

## 🍺 Sprite Sheet 4: Tasting Room & Blade Level
**File:** `molen_tasting_blade_level.png`
**Dimensions:** 1024x512 pixels

### Tasting Room (Second Floor):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Barrel Table Variants 1-3 | (0, 0) / (96, 0) / (192, 0) | 96x96 each | Circle arrangement around central shaft |
| Brewmaster's Throne | (288, 0) | 96x128 | Fancy chair at head table |
| Chalkboard Offerings | (384, 0) | 128x192 | Today's beers with pretentious descriptions |
| Central Shaft Segment | (512, 0) | 64x192 | Rotating shaft through the room |
| Tasting Flight Board (set) | (576, 0) | 256x96 | Five glasses, escalating ABV, escalating mistake |
| Candle Fixture Flicker 1-2 | (576, 96) / (640, 96) | 64x64 each | Electric candlelight (fire code) |
| Window Countryside Day | (832, 0) | 128x128 | Reorientation aid |
| Window Countryside Dusk | (832, 128) | 128x128 | Late-tour variant |

### Blade Level (Post-Boss):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Blade Level Platform | (0, 192) | 384x192 | Cramped platform below blade hub |
| Safety Railing | (384, 192) | 192x64 | Lawyers insisted |
| Wind Gust Lines | (384, 256) | 128x64 | SIGNIFICANT wind indicator |
| Selfie Spot Marker | (512, 256) | 64x64 | Photo trigger zone |
| Hair Chaos Overlay | (576, 192) | 96x96 | Wind-destroyed hair for photo results |
| Blade Sweep Close-Up 1-4 | (0, 384) / (256, 384) / (512, 384) / (768, 384) | 256x128 each | Selfie mini-game blade positions (dramatic → face-blocking) |

### Technical Notes:
- Blade Sweep frames drive the timing mini-game — frame 2 is the "Perfect Windmill Shot" window
- Tasting room applies progressive room-spin via shader (CanvasLayer rotation/warp), intensity = Spin Meter; no PNG overlay needed
- Candle flicker disabled in reduced-motion mode (hold frame 1)

---

## 🍞 Sprite Sheet 5: Yeast Golem — Battle Core
**File:** `yeast_golem_battle.png`
**Dimensions:** 1024x1024 pixels
**Sprite Size:** 192x256 pixels

### Phase 1 "Rising Dough":
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rising 1-4 | (0, 0) / (192, 0) / (384, 0) / (576, 0) | 192x256 each | Emerges from grain dust and forgotten yeast cultures |
| Idle Breathing 1-3 | (0, 256) / (192, 256) / (384, 256) | 192x256 each | Semi-solid dough mass, slow bubble |
| Flour Cloud Attack 1-4 | (0, 512) / (192, 512) / (384, 512) / (576, 512) | 192x256 each | AoE cast — applies "Bleary" (-Accuracy) |
| Yeast Punch 1-4 | (0, 768) / (192, 768) / (384, 768) / (576, 768) | 192x256 each | Single-target doughy haymaker |
| Dough Hook 1-2 | (768, 256) / (768, 512) | 192x256 each | Phase 3 pull attack — drags party member into melee |

### Technical Notes:
- Weakness window after Flour Cloud: reuse Idle frame 3 with 20% brightness lift (shader), no extra sprite
- Body reads as flour-white (#FFFAF0) with grain-gold veining; fire/alcohol hits tint it toast-brown

---

## 🥖 Sprite Sheet 6: Yeast Golem — Phases & Adds
**File:** `yeast_golem_phases.png`
**Dimensions:** 1024x1024 pixels

### Phase 2-3 Bodies:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Expanding 1-3 | (0, 0) / (256, 0) / (512, 0) | 256x320 each | Fermentation Frenzy growth — every 3 turns, bigger and slower |
| Final Rise Charge 1-3 | (0, 320) / (256, 320) / (512, 320) | 256x320 each | 2-turn massive AoE charge; vulnerability if hit with fire/alcohol |
| Collapse to Bread 1-4 | (0, 640) / (256, 640) / (512, 640) / (768, 640) | 256x320 each | Defeat: deflates into harmless loaf |

### Adds & Drops:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sourdough Sprite Idle 1-2 | (768, 0) / (864, 0) | 96x96 each | Weak summoned adds (Wild Fermentation) |
| Sourdough Sprite Attack 1-2 | (768, 96) / (864, 96) | 96x96 each | Tiny tangy lunge |
| Harmless Bread Loaf | (768, 192) | 96x64 | Post-defeat arena prop; drops Windmill Wit recipe |

### Technical Notes:
- Expansion frames anchor bottom-center so golem grows upward from arena floor
- Collapse frame 4 crossfades into Harmless Bread Loaf prop

---

## 👥 Sprite Sheet 7: Staff & Visitor NPCs
**File:** `npc_molen_cast.png`
**Dimensions:** 1024x384 pixels
**Sprite Size:** 64x96 pixels (groups noted)

### Staff (Row 0, y=0):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hendrik Idle 1-2 | (0, 0) / (64, 0) | 64x96 each | Barrel-chested brewmaster, beard that could filter beer |
| Hendrik Lecturing 1-4 | (128, 0) / (192, 0) / (256, 0) / (320, 0) | 64x96 each | 40-minute passion, arms conducting the grain |
| Hendrik Approval 1-2 | (384, 0) / (448, 0) | 64x96 each | Post-golem respect nod |
| Tessa Idle 1-2 | (512, 0) / (576, 0) | 64x96 each | Practical shoes, ready stance |
| Tessa Pointing 1-2 | (640, 0) / (704, 0) | 64x96 each | Directing tour flow |
| Tessa Catch-Ready | (768, 0) | 64x96 | Trained reflexes for dizzy tourists |
| Bram Idle 1-2 | (832, 0) / (896, 0) | 64x96 each | Gift shop, slightly bored, always there |

### Staff & Visitors (Row 1, y=96):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bram Upsell 1-3 | (0, 96) / (64, 96) / (128, 96) | 64x96 each | "You could buy those glasses." |
| Beer Blogger (German) 1-2 | (192, 96) / (256, 96) | 64x96 each | Notebook, reverent nodding, respects the grain |
| Repeat Visitor 1-2 | (320, 96) / (384, 96) | 64x96 each | Mysteriously unaffected by full flight |
| Instagram Couple 1-2 | (448, 96) / (576, 96) | 128x96 each | 300 photos, zero beers |
| Bachelor Party Group Frame 1 | (704, 96) | 256x96 | Dutch locals, further along in the flight |

### Visitors (Row 2, y=192):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bachelor Party Group Frame 2 | (0, 192) | 256x96 | Supporting each other literally |
| Bachelor Party Stumble | (256, 192) | 256x96 | "Johannes, are we spinning?" |
| Tourist Grabbing Rail 1-2 | (512, 192) / (576, 192) | 64x96 each | Floor vibration response |
| Dizzy Tourist 1-2 | (640, 192) / (704, 192) | 64x96 each | Spiral-eyed wobble |

### Technical Notes:
- Hendrik's lecture loop runs the entire endurance challenge; frames 2-4 shuffle randomly to avoid robotic looping
- Max 3 visitor NPCs per floor (draw call budget)

---

## 🏅 Sprite Sheet 8: Items, Effects & UI
**File:** `molen_items_ui.png`
**Dimensions:** 512x512 pixels

### Tasting & Rewards:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Flight Glasses 1-5 | (0, 0) to (128, 0), 32px steps | 32x48 each | Polder Pilsner → Windmill Wit, deepening color |
| Windmill Wit Bottle | (160, 0) | 48x64 | Consumable icon: +40 HP, -20% Navigation |
| Bottle Opener (Static) | (208, 0) | 48x48 | Miniature windmill, brushed copper, "Respect The Grain" |
| Opener Blade Spin 1-4 | (256, 0) / (304, 0) / (352, 0) / (400, 0) | 48x48 each | Blade arms actually rotate |
| Tour Stamp "Windmill Wit" | (448, 0) | 64x64 | Keychain stamp — 1 of 2 Shamsterdam breweries |
| Tasting Token | (384, 256) | 32x32 | Included with 25 Sovs tour |

### UI Panels:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Spin Meter | (0, 64) | 96x128 | Disorientation accumulation gauge (windmill needle) |
| Selfie Timing Mini-Game UI | (96, 64) | 256x192 | Blade position ring + shutter button |
| Tasting Flight Tracker | (352, 64) | 160x128 | Five-beer progress with ABV warnings |
| Yeast Slayer Title Badge | (352, 192) | 128x32 | Boss defeat title art |
| Navigation Debuff Icon | (96, 256) | 32x32 | Post-Windmill-Wit penalty |
| Bleary Status Icon | (128, 256) | 32x32 | Flour Cloud -Accuracy indicator |

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Liquid Ripple 1-2 | (0, 256) / (48, 256) | 48x32 each | Beer rippling in glasses during floor vibration |
| Spin Vignette Corner | (160, 256) | 128x128 | Corner gradient, mirrored 4x at runtime for spin effect edges |
| Beer Foam Sparkle 1-3 | (288, 256) / (320, 256) / (352, 256) | 32x32 each | Pour celebration |
| Camera Shutter Flash | (0, 304) | 64x64 | Selfie capture flash |
| Grain Dust Puff | (64, 304) | 64x64 | Footstep dust on grinding floor |

### Technical Notes:
- Room spin is shader-driven (CanvasLayer warp); Spin Vignette Corner is the only texture it needs
- Opener spin animation plays in inventory when item is inspected

---

## 🎬 Animation Specifications

### Windmill Blade Rotation (Sheets 1, 3, 4):
- **Duration:** 8 seconds per revolution (continuous; frames crossfade at 0.5 FPS, node rotation interpolates between)
- **Frames:** 4 positions
- **Pattern:** Continuous loop, speed scales with "wind" variable
- **Trigger:** Constant while location loaded
- **Purpose:** The whole building's identity — and the source of the dizziness
- **Audio Sync:** Blade whoosh on each 90° position pass
- **Mobile Optimization:** Static blade shadows on older devices (profile-mandated)

### Millstone Grinding (Sheet 3):
- **Duration:** 2 seconds per cycle (4 frames at 2 FPS)
- **Frames:** 4
- **Pattern:** Continuous loop synced to blade speed
- **Trigger:** Constant on grinding floor
- **Purpose:** The windmill actually works; the floor actually vibrates
- **Audio Sync:** Grinding rumble loop locked to cycle; low-frequency emphasis
- **Mobile Optimization:** Simplified grinding animation (2 frames) on older devices

### Floor Vibration (Sheets 3, 8):
- **Duration:** 0.3-second shake bursts every 2 seconds while grinding
- **Frames:** Overlay strip + 2-frame liquid ripple
- **Pattern:** Vibration overlay pulses; glasses ripple in sync
- **Trigger:** Grinding active (first floor); echoes faintly in tasting room
- **Purpose:** Tourists grab rails; beer ripples; history is felt
- **Audio Sync:** Rumble peak on each burst
- **Mobile Optimization:** Overlay only, no ripple, on Low LOD

### Yeast Golem Rising (Sheet 5):
- **Duration:** 3 seconds (4 frames at ~1.3 FPS), single play
- **Frames:** 4 + 3 spawn dust swirls
- **Pattern:** Dust swirl 1-3 → Rising 1-4 → Idle loop
- **Trigger:** Boss encounter start on grinding floor
- **Purpose:** "From the accumulated flour and forgotten yeast cultures, something RISES."
- **Audio Sync:** Reversed, slowed bread-baking sounds building to a boom on frame 4
- **Mobile Optimization:** 2 dust swirls on Low LOD

### Golem Expansion (Sheet 6):
- **Duration:** 1.5 seconds per expansion (3 frames at 2 FPS), every 3 turns in Phase 2
- **Frames:** 3
- **Pattern:** Expand → hold larger silhouette; weakness window during frames 2-3
- **Trigger:** Phase 2 turn counter
- **Purpose:** Over-proofing readability — bigger, stronger, slower
- **Audio Sync:** Dough stretch squelch on each frame
- **Mobile Optimization:** None needed

### Final Rise & Collapse (Sheet 6):
- **Duration:** Charge 4 seconds (2 game turns, 3 frames looping at 1 FPS); Collapse 2.5 seconds (4 frames at ~1.6 FPS), single play
- **Frames:** 3 + 4
- **Pattern:** Charge loop (interruptible by fire/alcohol) → Collapse 1-4 → bread loaf prop
- **Trigger:** Phase 3 script
- **Purpose:** Climax and punchline — the boss becomes bread
- **Audio Sync:** Rising oven-timer tick during charge; soft "poof" + oven ding on collapse frame 4
- **Mobile Optimization:** None needed

### Tasting Room Spin (Sheets 4, 8):
- **Duration:** Continuous; intensity ramps with Spin Meter (0-5 beers) over the flight
- **Frames:** Shader-driven, vignette corner texture
- **Pattern:** Subtle wobble at beer 2 → definite rotation at beer 4 → full "why is the floor moving" at Windmill Wit
- **Trigger:** Each flight beer consumed
- **Purpose:** Each beer makes the spinning more noticeable; the building doesn't help
- **Audio Sync:** Room-spin audio effect layers in per beer (profile audio design)
- **Mobile Optimization:** Vignette-only (no warp shader) on Low LOD; fully disabled in reduced-motion mode

### Selfie Blade Timing (Sheet 4):
- **Duration:** 4-second blade sweep loop (4 frames at 1 FPS); shutter window 0.5 seconds on frame 2
- **Frames:** 4 + shutter flash
- **Pattern:** Sweep loop → player taps → flash → result (Perfect/Unfortunate Windmill Shot)
- **Trigger:** Selfie Spot Marker interaction (post-boss)
- **Purpose:** Timing mini-game; wind factor option adds hair chaos overlay
- **Audio Sync:** Camera shutter on tap; wind howl constant at blade level
- **Mobile Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stairs/exit outlines | Sheet 8, (416, 256) | 32x32 x2 (x416, x448) | Bold-outline floor-transition markers for the circular, disorienting layout |
| Boss weakness flash | Sheet 8, (128, 304) | 64x64 | High-contrast burst marking fire/alcohol vulnerability window |
| Rail interaction highlight | Sheet 8, (192, 304) | 64x32 | Outline variant for the grab-rail during vibration |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static blade shadow | Sheet 3 (Window Blade Shadow 1) | 128x128 | Reduced-motion mode holds shadow frame 1 |
| Steady candle | Sheet 4 (Candle Fixture 1) | 64x64 | Non-flickering variant |
| Spin effect disabled note | Sheet 8 (Spin Vignette Corner) | 128x128 | Reduced-motion replaces warp with static vignette + "Dizzy" status text |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Grinding rumble icon | Sheet 8, (256, 304) | 32x32 | Vibration waves icon mirroring rumble audio |
| Blade whoosh marker | Sheet 8, (288, 304) | 32x32 | Sweep arc icon on each blade pass |
| Oven-ding defeat cue | Sheet 8, (320, 304) | 32x32 | Bell icon mirroring collapse audio sting |
| Charge warning icon | Sheet 8, (352, 304) | 32x32 | Two-turn Final Rise countdown pips |

### Colorblind Considerations:
- Flight beers differ by glass shape and fill level, not color alone; ABV numerals printed on flight board
- Boss weakness window uses brightness flash + icon, never a color-only tint
- Spin Meter uses needle position + numeric readout
- Touch zones minimum 44px for tasting choices, selfie shutter, and gift shop interactions

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC (fallback PVRTC 4BPP); chalkboard and signage need higher quality (readable text)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for boss sheets (phase silhouettes are gameplay-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| molen_environment | exterior, ground floor, grinding floor, tasting/blade | 2048x2048 |
| molen_boss | golem battle + phases | 2048x1024 |
| molen_characters_ui | NPC cast, items/effects/UI | 1024x1024 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full blade rotation, dust particles, spin shader, all visitor NPCs |
| Medium | Reduced dust, 2-frame grinding, vignette-only spin, 2 visitor NPCs |
| Low | Static blade shadows, no dust, no spin shader, staff NPCs only (profile-mandated simplifications) |

### Performance Targets:
- **Target FPS:** 60 (per location profile performance budget)
- **Max Draw Calls:** 18 per frame
- **Memory Footprint:** 42 MB maximum
- **Particle Limit:** 25 (grain dust, foam, boss flour clouds)

### Performance Notes:
- Load floors as separate scenes; only one floor + boss sheets resident at a time
- Boss sheets load on grinding-floor entry, unload after victory
- Blade/millstone share one rotation driver script to avoid duplicate per-frame updates

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: TileMap (floors), AnimatedSprite2D (golem, NPCs, mechanisms), CPUParticles2D (grain dust, flour — not GPU), CanvasLayer + warp shader (room spin), Camera2D shake (floor vibration)
- Special systems: dual bottle-opener gate (Blarney Trap opener = tour access; Windmill opener = stamp/beer access, earned via golem or 22 Sovs from Hendrik), Spin Meter accumulator, brewmaster speech skip/Bravado check, selfie timing evaluator, boss phase state machine with fire/alcohol interrupt

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Blade rotation positions | Rhythmic whoosh | Each 90° pass |
| Millstone frames | Grinding rumble loop | Locked to 4-frame cycle |
| Golem rising | Reversed/slowed bread-baking build | Frames 1-4, boom on 4 |
| Collapse frame 4 | Soft poof + oven ding | On frame display |
| Flight glass raise | Pour + toast clink | On consume action |
| Selfie shutter | Camera click + wind howl bed | On player tap |
| Hendrik lecture frames | Reverent baritone VO bed | Loop during endurance challenge |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Shamsterdam Brewery Tour (1 of 2) | Tour stamp, opener sprites, flight tracker | Stamp awarded with both openers held |
| "Canal Courage" Passive | Flight tracker completion state | Both Shamsterdam breweries → 25% Bravado-loss reduction while intoxicated |
| Yeast Golem Boss | Both boss sheets, arena tiles, Yeast Slayer badge | Grinding floor encounter; unlocks tasting room + blade level |
| Couchsurf — Beer Blogger | Beer Blogger sprites | Serious tasting-note engagement triggers invitation |
| Selfie Spot Challenge | Blade sweep frames, shutter flash, hair chaos | Post-boss blade level |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Proeflokaal 't Kansen | Shared stamp/keychain UI style | Brewery tour achievement pairing |
| The Tolerance Hostel | Windmill Wit bottle (conversation prop) | "The windmill" guest discussions |
| De Groene Gids | None shared; dialogue reference only | Staff comment on "trying the local breweries" |
| Train Station (central Shamsterdam) | Train station exterior, countryside strip | 8 Sovs round-trip transition scene |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "350 years of genuine heritage, 15 years of monetized reverence, and a building that never stops moving"
- **Color Mood:** Grain gold and copper warmth over old wood — inviting until it starts rotating
- **Lighting:** Dusty natural shafts on the grinding floor, spotlights on vats, warm fake candlelight above; the light itself sways subtly with the spin
- **Texture:** Flour-dusted everything; worn wood polished only where tourists grab it

### Environmental Storytelling:
- Gift shop bookends the tour (entry AND exit) — the funnel is the architecture
- "History" panels that are 95% beer marketing tell you what heritage is for here
- Open grain bins and pre-EU lighting rig read as authentic-because-uninsurable
- The Survivor Pack display admits everything the tour pretends not to know

### Character Integration Notes:
- Hendrik dominates rooms — position him centrally, lecture frames large in the composition
- Tessa orbits the tour group edges, always between a tourist and a railing gap
- Visitor NPCs escalate in dishevelment by floor: composed at reception, rail-clutching upstairs
- The golem must stay comedic-threatening: dough physics, never horror

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Fighting Bread** - The Yeast Golem mid-expansion; "I fought bread" energy
2. **The Perfect Windmill Shot** - Selfie mini-game success (and its face-blocked failure twin)
3. **The Spin Meter Maxed** - Full tasting flight with the room warping
4. **Collapse to Loaf** - Boss defeat becoming a harmless bread prop
5. **"I SURVIVED THE SPIN" Rack** - The gift shop admitting the business model

### Quote Potential:
- "Respect The Grain. Fear The Spin."
- "The first beer teaches you humility. The second teaches you character. The third teaches you why we have railings."
- "It's made of BREAD. How is BREAD this AGGRESSIVE?"
- "I fought bread. I have footage of fighting BREAD. This trip is INSANE."
- "The spinning is intentional. The dizziness is not our fault."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | brouwerij_molen_exterior.png | 1024x768 |
| 2 | molen_ground_floor.png | 1024x512 |
| 3 | molen_grinding_floor.png | 1024x1024 |
| 4 | molen_tasting_blade_level.png | 1024x512 |
| 5 | yeast_golem_battle.png | 1024x1024 |
| 6 | yeast_golem_phases.png | 1024x1024 |
| 7 | npc_molen_cast.png | 1024x384 |
| 8 | molen_items_ui.png | 512x512 |

**Total Estimated Memory:** ~22 MB raw RGBA texture data; ~42 MB maximum total footprint (location performance budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `brouwerij_molen_exterior.png` (1024x768)
- [ ] `molen_ground_floor.png` (1024x512)
- [ ] `molen_grinding_floor.png` (1024x1024)
- [ ] `molen_tasting_blade_level.png` (1024x512)
- [ ] `yeast_golem_battle.png` (1024x1024)
- [ ] `yeast_golem_phases.png` (1024x1024)
- [ ] `npc_molen_cast.png` (1024x384)
- [ ] `molen_items_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + blade/millstone rotation sync guide + boss phase state chart

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: gift shop funnel, Survivor Pack, "I SURVIVED THE SPIN" merch, golem-becomes-bread, blade-blocked selfie failure
- [ ] Accessibility visual alternatives included for all audio cues (rumble, whoosh, charge warning, oven ding)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (heritage commodification, reverence vs. dizziness)
- [ ] Hidden areas/interactions have discoverable visual cues (blade level unlock, opener purchase option)
- [ ] Mobile performance optimized (CPU particles, atlas limits, per-floor scene loading)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (glass shapes, weakness flash)
- [ ] Social media viral potential maximized in composition choices (golem expansion framing, selfie results)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam countryside only; profile's "Amsterdam" mentions are meta design commentary, not in-world assets |
| Cultural Specificity | ✅ | Dutch windmill heritage tourism + craft beer culture explosion |
| Satirical Targets Appropriate | ✅ | Brewery pretension and experience-tourists; Dutch heritage and legitimate brewing respected |
| Seedy Underbelly Present | ✅ | 40 Sovs flights in a disorientation machine, comprehensive liability waivers, gift shop funnel |
| Gameplay Value Established | ✅ | Boss battle, tasting/Spin Meter system, endurance speech, selfie mini-game, opener gating |
| Technical Feasibility | ✅ | Per-floor scenes, shared rotation driver, shader spin, CPU particles documented |
| Mobile Performance Budget | ✅ | 60 FPS, 18 draw calls, 42 MB per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all audio cues, reduced-motion spin disable, 44px zones |
| No Crypto Elements | ✅ | Pure traditional brewing; Tier of tech gimmicks absent per profile |
| Social Media Integration | ✅ | 5 screenshot moments + quote bank identified |

**Once these assets are delivered, Brouwerij de Molen becomes Eurobound's first spinning dungeon: a heritage site that fights back with bread, beer, and centrifugal force — and every player leaves with a photo, a stamp, and a navigation debuff they paid 25 Sovs for.**
