# Neon & Chrome Boutique - Complete PNG Asset Requirements

## 📋 Overview
The Neon & Chrome Boutique sells the FANTASY of club status — strobe shades, six-inch platforms, and a VIP wristband holder that holds nothing but hope. This document specifies every PNG needed to render Katarina's chrome-and-neon showroom, the club simulation fitting booth, and the Premium Stock section that only unlocks after the player defeats Count Velvet Absinthe. The satire: some gear actually works, some is pure status theater, and the shop sells both at the same counter.

**Location ID:** `debaucheryville_shop_neon_chrome_01`
**Theme:** VIP culture and the purchase of status signifiers — "Dress for the Club You Want to Be In."
**Zone:** Absinthe Arcade, Neon Entertainment Quarter (premium end)
**Hours:** 4 PM - 4 AM (closed during "amateur hours")
**Primary Function:** Specialty shop / equipment vendor — Style, Intimidation, and Visibility stat gear; club simulation fitting; boss-gated Premium Stock; Bravado interactions

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Neon Pink | #FF1493 | Primary neon signage, window glow |
| Chrome Silver | #C0C0C0 | Fixtures, door frame, mirror shades |
| Club Purple | #4B0082 | Background walls, mannequin lighting |
| LED Blue | #00BFFF | LED product glow, programmable glasses |
| Night Black | #1A1A1A | Exterior night context, shadow zones |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/neon_chrome_boutique/
├── environment/
│   ├── boutique_exterior.png
│   ├── boutique_interior.png
│   └── fitting_room_sim.png
├── objects/
│   └── boutique_gear.png
├── npcs/
│   ├── boutique_staff.png
│   └── boutique_customers.png
├── effects/
│   └── boutique_effects.png
└── ui/
    └── boutique_ui.png
```

---

## 🏪 Sprite Sheet 1: Boutique Exterior
**File:** `boutique_exterior.png`
**Dimensions:** 512x512 pixels

### Storefront Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Storefront Facade | (0, 0) | 384x384 | All glass and chrome, a club entrance that sells things |
| Mannequin Window Display | (384, 0) | 128x256 | Full club regalia bathed in purple and pink neon |
| LED Main Sign | (384, 256) | 128x64 | "NEON & CHROME BOUTIQUE" in glowing LED script |
| Category Strip Sign | (384, 320) | 128x32 | "EYEWEAR \| FOOTWEAR \| ACCESS \| GLOW" |
| Honest Plaque | (384, 352) | 128x32 | Small print: "Actual belonging sold separately" |

### Entry Sequence:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Auto Door Closed | (0, 384) | 96x128 | Chrome-framed glass, reflective |
| Auto Door Half-Open | (96, 384) | 96x128 | Mid-whoosh frame |
| Auto Door Open | (192, 384) | 96x128 | Full open, interior glow spilling out |
| Neon Underglow Strip | (288, 384) | 224x64 | Pink/purple pavement wash below the facade |
| Sidewalk Neon Reflection | (288, 448) | 224x64 | Wet-look mirror of the signage on the street |

### Technical Notes:
- LED Main Sign cycles a 3-frame shader tint (no extra frames needed) — pink → blue → pink
- Door frames drive the entry whoosh + bass drop moment; hold the open frame while player is inside range
- Facade is the only exterior state needed: the shop is only open 4 PM - 4 AM, so night lighting is baked in

---

## 🛍️ Sprite Sheet 2: The VIP Showroom
**File:** `boutique_interior.png`
**Dimensions:** 1024x512 pixels

### Showroom Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Showroom Base | (0, 0) | 512x384 | Walls, floor, chrome fixtures, club preview lighting |
| Eyewear Station | (512, 0) | 256x192 | Shades racks, "The Bouncer Won't Judge You" collection card |
| Footwear Display | (768, 0) | 256x256 | Platform pyramid — the higher the platform, the higher the shelf |
| Access Accessories Display | (512, 192) | 192x192 | Stamp books, wristband holders, lanyard systems |
| Mirror Try-On Station | (704, 192) | 64x192 | Full-length mirror with flattering rim light |
| Glow & Visibility Section | (768, 256) | 256x192 | LED jewelry, UV-reactive accents, "Be Seen" signage |

### Commerce & Premium Stock:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Premium Stock Gate (Locked) | (0, 384) | 256x128 | Velvet rope + chrome shutter, "PROVEN CUSTOMERS ONLY" |
| Premium Stock Revealed | (256, 384) | 256x128 | Open alcove, Velvet Rope Clip on a lit pedestal |
| Checkout Counter | (512, 384) | 192x128 | Chrome counter, register, "confidence talk" zone |
| Velvet Rope Clip Display Case | (704, 384) | 64x96 | Glass case for the post-boss trophy trinket |
| Bass Speaker Stack | (768, 448) | 128x64 | Source of the entry bass drop |
| Fog Machine Vent | (896, 448) | 128x64 | Subtle fog emitter, floor level |

### Technical Notes:
- Premium Stock swaps Locked → Revealed on `count_velvet_absinthe_defeated` flag; play unlock burst from Sheet 7
- Mirror Try-On Station renders equipped-gear preview via viewport texture, not extra sprites
- Speaker stack has a 2-frame membrane wobble driven by the ambient bass loop

---

## 🕶️ Sprite Sheet 3: Club Simulation Fitting Room
**File:** `fitting_room_sim.png`
**Dimensions:** 512x512 pixels

### Booth Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Booth Exterior | (0, 0) | 192x256 | Private booth, "CLUB SIMULATION" door sign |
| Booth Interior Neutral | (192, 0) | 256x256 | Fitting room in rest state, before the show starts |
| Curtain Closed | (448, 0) | 64x128 | Chrome-ringed blackout curtain |
| Curtain Open | (448, 128) | 64x128 | Tied back, inviting |

### Lighting Mode Overlays:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Strobe Overlay Frame 1 | (0, 256) | 128x128 | Full white flash |
| Strobe Overlay Frame 2 | (128, 256) | 128x128 | Half-decay flash |
| Strobe Overlay Frame 3 | (256, 256) | 128x128 | Dark between-flash frame |
| UV Blacklight Overlay | (384, 256) | 128x128 | Purple wash — UV-reactive gear pops under this |
| Fog Overlay | (0, 384) | 128x128 | Booth fog layer |
| Bass Pulse Overlay Frame 1 | (128, 384) | 128x128 | Expanding low-frequency light ring |
| Bass Pulse Overlay Frame 2 | (256, 384) | 128x128 | Ring dissipating |

### Controls:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Venue Preset Panel | (384, 384) | 128x64 | "Velvet Curtain Main Floor" and other venue presets |
| Lighting Control Panel | (384, 448) | 128x64 | Strobe / UV / bass / fog toggle switches |

### Technical Notes:
- Overlays are additive-blended on top of Booth Interior Neutral; only one mode set active at a time on mobile
- Strobe mode is gated behind the accessibility motion-sensitivity setting (see ♿ section)
- Dominik can set Venue Preset Panel to match Velvet Curtain's rig — swaps overlay tint values only

---

## 💎 Sprite Sheet 4: Gear Inventory
**File:** `boutique_gear.png`
**Dimensions:** 256x256 pixels

### Eyewear Station Stock:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Strobe Shades (Basic) | (0, 0) | 32x24 | 15 Sovs entry-level protection |
| Strobe Shades (Premium) | (32, 0) | 32x24 | 35 Sovs, statement AND function |
| LED Glasses (Static) | (64, 0) | 32x24 | Single color, maximum impact |
| LED Glasses (Programmable) | (96, 0) | 32x24 | 50 Sovs, control your own light show |
| Mirror Shades (Chrome) | (128, 0) | 32x24 | They see themselves, not you |
| "The Bouncer" Aviators | (160, 0) | 32x24 | Professional recognition |
| "Inner Circle" Shades | (192, 0) | 32x24 | Premium Stock exclusive |
| LED Earrings | (224, 0) | 24x24 | Light up conversations |

### Footwear & Access Stock:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Platform Boots (2 inch) | (0, 32) | 32x32 | Subtle elevation |
| Platform Boots (4 inch) | (32, 32) | 32x32 | Committed elevation |
| Platform Boots (6 inch) | (64, 32) | 32x32 | Maximum presence, balance required |
| LED-Sole Sneakers | (96, 32) | 32x32 | Feet that announce you |
| "Dance Floor" Comfort Platforms | (128, 32) | 32x32 | Function meets fashion |
| Club Stamp Collection Book | (160, 32) | 32x32 | Documentation of your journey |
| VIP Wristband Holder | (192, 32) | 32x24 | Displays wristbands you don't have yet |
| Multi-Venue Lanyard | (224, 32) | 32x32 | For the serious clubber |

### Glow & Premium Stock:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "Scene Veteran" Pin Collection | (0, 64) | 32x32 | Allegiances displayed |
| Velvet Rope Clip ★ | (32, 64) | 32x32 | Post-boss trophy trinket, gold clip on velvet |
| Premium Glow Necklace | (64, 64) | 32x32 | Not the cheap ones — 8-hour glow |
| UV-Reactive Accent Set | (96, 64) | 48x32 | Only visible when it matters |
| LED Ring Set (3) | (144, 64) | 32x24 | Subtle but effective |
| Full Body Glow Kit | (176, 64) | 48x48 | The nuclear option |
| Shadow Exchange Member Card | (224, 64) | 32x24 | Premium Stock — better rates elsewhere |

### Lit States & Retail Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "Recognized" Status Pin | (0, 96) | 24x24 | Bouncers acknowledge you |
| LED Glasses (Lit) | (32, 96) | 32x24 | Glow-active variant for equipped display |
| LED Sneakers (Lit) | (64, 96) | 32x32 | Sole glow-active variant |
| Glow Necklace (Lit) | (96, 96) | 32x32 | Active glow variant |
| Boutique Shopping Bag | (128, 96) | 32x32 | Chrome-handled purchase bag |
| Price Tag (Standard) | (0, 128) | 24x16 | Neon pink tag |
| Price Tag (Premium) | (24, 128) | 24x16 | Gold-trimmed tag |
| Charging Dock | (48, 128) | 32x32 | For the rechargeable LED line |

### Technical Notes:
- Lit variants swap in when items are equipped in dark/club contexts
- All shop-menu icons pulled from this single sheet via texture regions — one draw call for the whole browser
- 32x32 grid alignment throughout; oversized items (glow kit, UV set) span cells cleanly

---

## 👥 Sprite Sheet 5: Katarina & Dominik
**File:** `boutique_staff.png`
**Dimensions:** 512x256 pixels

### Katarina "Kat" Svobodová:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Katarina Idle | (0, 0) | 64x96 | Immaculate club-ready presentation, always |
| Katarina Welcome Gesture | (64, 0) | 64x96 | VIP host approach — "You're going out tonight?" |
| Katarina Sales Pitch | (128, 0) | 64x96 | Presenting gear, "Height is presence. Presence is power." |
| Katarina Honest Moment | (192, 0) | 64x96 | Level gaze — "The gear helps. But it's not magic." |
| Katarina Assessing F1 | (256, 0) | 64x96 | VIP potential evaluation, looking player up |
| Katarina Assessing F2 | (320, 0) | 64x96 | Evaluation, looking player down |
| Katarina Premium Unlock | (384, 0) | 64x96 | "You've EARNED these" — gesturing at the alcove |
| Katarina Portrait | (448, 0) | 64x96 | Dialogue box portrait |

### Assistant Dominik:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Dominik Idle | (0, 96) | 64x96 | Fully committed to the aesthetic, walks the walk |
| Dominik Hype | (64, 96) | 64x96 | "Dude, these LED glasses at Velvet Curtain?" |
| Dominik Fitting Controls | (128, 96) | 64x96 | Operating the booth panel |
| Dominik LED Demo | (192, 96) | 64x96 | Wearing lit programmables, being his own light show |
| Dominik Portrait | (256, 96) | 64x96 | Dialogue box portrait |
| Katarina Walk F1 | (320, 96) | 64x96 | Floor movement frame |
| Katarina Walk F2 | (384, 96) | 64x96 | Floor movement frame |
| Dominik Walk | (448, 96) | 64x96 | Floor movement sway |

### Expressions & Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Katarina Knowing | (0, 192) | 48x48 | The smile of someone who understands the game perfectly |
| Katarina Honest | (48, 192) | 48x48 | Truth-moment expression |
| Katarina Proud | (96, 192) | 48x48 | Post-boss welcome to the inner circle |
| Katarina Deadpan | (144, 192) | 48x48 | "...there's no percentage." |
| Dominik Enthusiastic | (192, 192) | 48x48 | Genuine believer energy |
| Dominik Conspiratorial | (240, 192) | 48x48 | "I know their lighting rig" |
| Purchase Handoff Hands | (288, 192) | 64x48 | Bag-over-counter close-up |
| Confidence Talk Icon | (352, 192) | 48x48 | Speech spark for the post-purchase pep moment |

---

## 🧑‍🤝‍🧑 Sprite Sheet 6: Customers & Bros
**File:** `boutique_customers.png`
**Dimensions:** 512x192 pixels

### Atmospheric Customers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pre-Game Group | (0, 0) | 192x96 | Friend trio coordinating LED glasses — "We're a UNIT" |
| VIP Aspirant | (192, 0) | 64x96 | Solo shopper calculating combinations |
| Return Customer (Success) | (256, 0) | 64x96 | "The platforms WORKED" — upgrading to six-inch |
| Return Customer (Reality) | (320, 0) | 64x96 | Had everything right, still got regular line |
| Scene Expert (Local) | (384, 0) | 64x96 | Buying strobe shades for function, not looks |
| Generic Browser | (448, 0) | 64x96 | Ambient shopper filler |

### The Bros:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lord Pilsner (Platforms) | (0, 96) | 64x96 | "This is where champions EQUIP" — trying boots |
| Chadwick (LED Filming) | (64, 96) | 64x96 | Filming himself in sound-reactive programmables |
| Bradley (Wristband Holder) | (128, 96) | 64x96 | Holding a holder that holds nothing |
| Group Mirror Moment | (192, 96) | 192x96 | All three posed at the mirror wall |
| VIP Aspirant Calculating | (384, 96) | 64x96 | Fingers up, doing VIP percentage math |
| Success Story Pointing | (448, 96) | 64x96 | Testifying to the platform theory |

---

## ✨ Sprite Sheet 7: Effects
**File:** `boutique_effects.png`
**Dimensions:** 256x256 pixels

### Neon & Light:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Neon Flicker F1 | (0, 0) | 64x32 | Full-bright sign glow |
| Neon Flicker F2 | (64, 0) | 64x32 | Partial dim |
| Neon Flicker F3 | (128, 0) | 64x32 | Buzz-out frame |
| LED Glow Halo | (192, 0) | 32x32 | Generic glow ring for lit gear |
| Light Leak Beam | (0, 32) | 128x64 | Diagonal club-light shaft |
| Fog Puff F1 | (128, 32) | 64x64 | Floor fog bloom |
| Fog Puff F2 | (192, 32) | 64x64 | Fog dissipating |

### Bass & Celebration:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Bass Pulse Ring F1 | (0, 96) | 64x64 | Ring at speaker |
| Bass Pulse Ring F2 | (64, 96) | 64x64 | Ring expanding |
| Bass Pulse Ring F3 | (128, 96) | 64x64 | Ring fading |
| Premium Unlock Burst | (192, 96) | 64x64 | Gold-pink burst when the shutter lifts |
| UV Reactive Shimmer | (0, 160) | 64x32 | Blacklight pop on UV gear |
| Chrome Gleam Sweep | (64, 160) | 96x32 | Traveling highlight across fixtures |
| Purchase Sparkle F1 | (160, 160) | 32x32 | Transaction sparkle |
| Purchase Sparkle F2 | (192, 160) | 32x32 | Sparkle fade |
| LED Pattern Trail | (224, 160) | 32x32 | Programmable-glasses motion trail |

### Entry Sequence:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Door Whoosh Lines | (0, 192) | 96x64 | Automatic door air movement |
| Bass Drop Shockwave | (96, 192) | 96x64 | The entry moment — lighting shift ring |
| Confidence Aura | (192, 192) | 64x64 | Subtle glow on player after "confidence talk" |

---

## 🎮 Sprite Sheet 8: UI Elements
**File:** `boutique_ui.png`
**Dimensions:** 256x256 pixels

### Shop Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gear Browser Frame | (0, 0) | 160x96 | Chrome-edged section navigation panel |
| VIP Potential Meter | (160, 0) | 96x32 | Assessment display (deliberately unquantified) |
| Style Stat Chip | (160, 32) | 96x32 | Current Style level readout |
| Intimidation Icon | (160, 64) | 32x32 | Platform effect indicator |
| Visibility Icon | (192, 64) | 32x32 | Glow gear effect indicator |
| Scene Cred Icon | (224, 64) | 32x32 | Stamp book / pin effect indicator |

### Premium Stock & Status:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Premium Locked Banner | (0, 96) | 128x48 | "DEFEAT THE COUNT" shutter state |
| Premium Unlocked Banner | (128, 96) | 128x48 | "INNER CIRCLE — WELCOME" state |
| Fitting Control Icons | (0, 144) | 160x32 | Strobe / UV / bass / fog / preset toggles |
| Velvet Rope Clip Equipped | (160, 144) | 48x48 | Trophy trinket HUD icon |
| Charm Icon | (208, 144) | 32x32 | Clip charm bonus indicator |

### Feedback:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Achievement Toast Frame | (0, 192) | 192x48 | "Equipped" / "Scene Ready" / "Towering" toasts |
| Bravado Up | (192, 192) | 32x32 | Confident-purchase feedback |
| Bravado Down | (224, 192) | 32x32 | "Will this actually get me in?" feedback |
| Price Tag UI | (0, 240) | 64x16 | Item price chip |
| Discount Tag UI | (64, 240) | 64x16 | Velvet Rope Clip shop discount chip |

---

## 🎬 Animation Specifications

### Entry Bass Drop:
- **Duration:** 2.5 seconds total
- **Frames:** Door Closed → Half → Open (0.5s), Bass Drop Shockwave (1s), lighting shift lerp (1s)
- **Pattern:** One-shot on player entry
- **Trigger:** Player crosses the door threshold
- **Purpose:** The shop IS a club preview — entering should feel like walking past a velvet rope
- **Audio Sync:** Door whoosh at 0.0s, bass drop hit at 0.5s, muffled club track fades in over the last second
- **Performance Optimization:** Shockwave ring drops to a simple screen tint pulse on Low LOD

### Neon Flicker:
- **Duration:** 4 seconds loop
- **Frames:** 3 (F1 3.4s → F2 0.3s → F3 0.3s → loop)
- **Pattern:** Mostly steady with an occasional stutter — premium neon, not dying neon
- **Trigger:** Constant, exterior and interior signage
- **Purpose:** Alive-but-classy signage; this shop is upmarket, its neon barely misbehaves
- **Audio Sync:** Faint buzz tick on F3
- **Performance Optimization:** Static F1 on Low LOD

### Club Simulation — Strobe Mode:
- **Duration:** 0.6 seconds loop while active
- **Frames:** 3 (flash → decay → dark, 0.2s each)
- **Pattern:** Loops while strobe toggle is on
- **Trigger:** Player or Dominik activates the fitting room strobe
- **Purpose:** "See how gear looks under actual club conditions" — sells the strobe shades honestly
- **Audio Sync:** Strobe relay click on each flash frame
- **Performance Optimization:** Disabled entirely when reduced-motion is on; replaced by steady UV overlay

### Bass Pulse (Fitting Room & Speakers):
- **Duration:** 1.0 second loop
- **Frames:** 3 rings (F1 → F2 → F3)
- **Pattern:** One ring per beat
- **Trigger:** Bass toggle active, or ambient near speaker stack
- **Purpose:** Physicalize the soundtrack; syncs the room to the music
- **Audio Sync:** Ring spawns exactly on the beat of the ambient club loop
- **Performance Optimization:** Single ring, half opacity on Medium; off on Low

### Premium Stock Reveal:
- **Duration:** 3 seconds one-shot
- **Frames:** Locked gate → shutter lift (1.5s) → Premium Unlock Burst (0.5s) → Revealed state hold (1s)
- **Pattern:** Plays once when the flag flips, then Revealed state persists
- **Trigger:** First entry after defeating Count Velvet Absinthe
- **Purpose:** The payoff moment — "You've proven yourself" made visible
- **Audio Sync:** Triumphant unlock sting starts with the shutter, peaks on the burst
- **Performance Optimization:** None needed (one-shot, low cost)

### Katarina's VIP Assessment:
- **Duration:** 3 seconds
- **Frames:** Assessing F1 (1.2s) → Assessing F2 (1.2s) → Knowing expression (0.6s)
- **Pattern:** One-shot after significant purchase
- **Trigger:** Purchase total crosses assessment threshold, or player asks for assessment
- **Purpose:** Comedy beat — the up-down evaluation before the honest(ish) verdict
- **Audio Sync:** "VIP potential assessment" fanfare stinger on the Knowing frame
- **Performance Optimization:** None needed

### Chrome Gleam Sweep:
- **Duration:** 6 seconds loop
- **Frames:** 1 sprite tweened across fixtures
- **Pattern:** Highlight travels left-to-right across counter and racks
- **Trigger:** Constant ambient
- **Purpose:** Everything in here is polished; the shop itself is dressed for the club
- **Audio Sync:** None
- **Performance Optimization:** Off on Low LOD

---

## ♿ Accessibility Sprite Requirements
**File:** `boutique_accessibility.png` (supplemental sheet — delivered alongside the 8 base files, not counted in their total)
**Dimensions:** 256x256 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Katarina Interactive Outline | (0, 0) | 64x96 | White-on-dark outline hotspot overlay |
| Dominik Interactive Outline | (64, 0) | 64x96 | Matching hotspot outline |
| Gear Browser, Bold Frame | (128, 0) | 96x64 | High-contrast shop menu border |
| Premium Gate, Large-Print | (128, 64) | 128x48 | Enlarged "PROVEN CUSTOMERS ONLY" readable without zoom |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Strobe Mode, Disabled Card | (0, 96) | 96x64 | "Strobe preview unavailable — steady lighting shown" booth card |
| Neon, Steady | (96, 128) | 64x32 | Static full-bright sign replacing the flicker cycle |
| Bass Pulse, Steady Glow | (160, 128) | 32x32 | Constant speaker glow replacing expanding rings |
| LED Trail, Off | (192, 128) | 32x32 | Static lit-glasses frame replacing the pattern trail |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bass Drop Icon | (0, 176) | 48x48 | Speaker burst glyph on the entry bass drop |
| Door Whoosh Icon | (48, 176) | 32x32 | Air-lines glyph on door open |
| Purchase Chime Icon | (80, 176) | 32x32 | Register glyph on transaction |
| Assessment Fanfare Icon | (112, 176) | 48x32 | Trumpet glyph on the VIP assessment stinger |
| Unlock Sting Icon | (160, 176) | 48x48 | Rising-notes glyph on the Premium Stock reveal |
| Ambient Beat Tick | (208, 176) | 32x32 | Metronome pip synced to the club loop for beat-driven visuals |

### Colorblind Considerations:
- Stat effect icons are shape-coded (fist = Intimidation, eye = Visibility, star = Style), never color-only
- Premium Locked vs. Unlocked banners differ by icon (padlock vs. open rope) in addition to color
- Lit vs. unlit gear variants add a radiating-line glyph, not just a hue shift
- All shop buttons and the fitting-room toggles meet the 44px minimum touch target

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) — boutique_gear.png kept uncompressed (small item icons need crisp edges)
- **Fallback:** PNG high quality for boutique_ui.png and gear icons

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| neon_chrome_environment | exterior, interior, fitting room | 2048x1024 |
| neon_chrome_characters | staff, customers | 1024x512 |
| neon_chrome_effects_ui | gear, effects, ui, accessibility | 1024x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full fitting-room simulation, bass rings, fog, chrome gleam, all customer NPCs |
| Medium | Single bass ring, no fog, 3 customer NPCs max, static neon between flickers |
| Low | Static neon, no gleam/fog/rings, 2 customer NPCs, tint-pulse entry instead of shockwave |

### Performance Targets:
- **Target FPS:** 60 (per location profile performance budget)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 34 MB maximum
- **Particle Limit:** 16 (fog + sparkles combined)

### Performance Notes:
- Fitting room overlays only loaded when the booth is entered (on-demand)
- Premium Stock assets stay unloaded until the boss flag is set
- All lighting shifts are modulate tweens, not shader passes, on Medium/Low
- Simplified LED effects and static neon per the profile's platform considerations

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Interior as a single scene: Sprite2D regions from boutique_interior.png, CanvasModulate for the club-preview lighting shift
- Fitting room: overlay TextureRects with additive blend; strobe loop driven by a Timer node gated on the accessibility setting
- CPUParticles2D (not GPU) for fog puffs and purchase sparkles
- Shop inventory driven by a resource table keyed to boutique_gear.png regions; lit variants swapped by an `is_dark_context` check
- State tracking: `neon_chrome_state` (premium_unlocked, purchases_made, fitting_room_used, velvet_rope_clip_owned, achievement_flags)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Entry sequence | Door whoosh → bass drop | Whoosh at 0.0s, drop at 0.5s |
| Bass Pulse rings | Club ambient loop | Ring spawn on each beat |
| Strobe overlay | Relay click | On each flash frame |
| Premium Stock Reveal | Triumphant unlock sting | Starts with shutter, peaks on burst |
| Katarina assessment | "VIP potential" fanfare | On Knowing expression frame |
| Purchase Sparkle | Register chime + confidence talk VO | Sparkle F1 on chime |
| LED Demo (Dominik) | Sound-reactive glasses blips | Pattern trail syncs to music transients |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Count Velvet Absinthe (boss, Velvet Curtain) | Premium Stock Gate/Revealed, Unlock Burst, Katarina Premium Unlock pose | Boss victory flips the Premium Stock flag; reveal plays on next entry |
| Velvet Rope Clip acquisition | Velvet Rope Clip sprite, display case, equipped HUD icon, Discount Tag UI | Purchase enables shop discounts + VIP access hints city-wide |
| Achievement track (Equipped → Inner Circle → Theory Validated) | Achievement Toast Frame, gear sprites | Toast fires on first purchase, full outfit, 6-inch platforms, premium access, clip purchase, post-purchase VIP entry |
| Bravado system | Bravado Up/Down icons, Confidence Aura | Confident purchases and assertive fitting-room use gain Bravado; hesitation loses it |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Velvet Curtain Club | Gear stat effects apply at the door; "The Bouncer" Aviators charm bonus with door staff | Standard street fade; equipped gear persists |
| Threads & Treads | Complementary vendor — fashion vs. club-specific gear; shared Style economy | Standard street fade |
| Shadow Exchange | Member Card sprite grants better rates there | Card shown in Shadow Exchange dialogue |
| The Strobe Survival Kit | Overlapping strobe-protection products (deliberate market overlap gag) | None (referenced in dialogue) |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A club entrance that sells things — status theater with a straight face"
- **Color Mood:** Neon Pink and Club Purple aspiration over Chrome Silver polish; LED Blue for everything that promises to make you visible
- **Lighting:** Full club simulation capability — the shop always looks like the best five minutes of a night out
- **Texture:** Flawless chrome, glass without fingerprints, velvet that has never been touched by anyone unproven

### Environmental Storytelling:
- The honest plaque under the glowing promise: "Actual belonging sold separately" — the shop admits the con in 8-point font
- The platform pyramid prices by altitude; the 6-inch shelf is at eye level, of course
- The VIP wristband holder display holds beautifully lit, entirely empty holders
- The Premium Stock alcove is visible but shuttered from day one — aspiration you can window-shop

### Character Integration Notes:
- Katarina reads as the smartest person in the room because she is — poses stay composed, never salesy-desperate
- Dominik wears the stock; his LED demo pose is a walking product display
- Customer NPCs cover the full delusion spectrum (Pre-Game unit → Aspirant math → Success testimony → Reality check → Local pragmatist) so the satire plays out in the background without dialogue

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Group Mirror Moment** - Three bros in full regalia believing in themselves simultaneously
2. **The Premium Stock Reveal** - Boss trophy commerce, shutter lifting in gold light
3. **The Fitting Room Strobe Test** - Trying on shades under simulated Velvet Curtain conditions
4. **The Honest Plaque** - "Actual belonging sold separately" close-up
5. **Bradley's Empty Wristband Holder** - Preparation as its own signal

### Quote Potential:
- "I don't sell VIP access. I sell looking like you already have it. The rest is up to you."
- "If I combine the platforms with the mirror shades and the wristband holder... what's my VIP percentage?"
- "...there's no percentage. But you'll look like you expect to get in. That helps."
- "Does the VIP wristband holder work if you don't have a VIP wristband?"
- "This is CONTENT and FASHION."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | boutique_exterior.png | 512x512 |
| 2 | boutique_interior.png | 1024x512 |
| 3 | fitting_room_sim.png | 512x512 |
| 4 | boutique_gear.png | 256x256 |
| 5 | boutique_staff.png | 512x256 |
| 6 | boutique_customers.png | 512x192 |
| 7 | boutique_effects.png | 256x256 |
| 8 | boutique_ui.png | 256x256 |

**Total Estimated Memory:** ~19 MB (well inside the 34 MB location budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `boutique_exterior.png` (512x512)
- [ ] `boutique_interior.png` (1024x512)
- [ ] `fitting_room_sim.png` (512x512)
- [ ] `boutique_gear.png` (256x256)
- [ ] `boutique_staff.png` (512x256)
- [ ] `boutique_customers.png` (512x192)
- [ ] `boutique_effects.png` (256x256)
- [ ] `boutique_ui.png` (256x256)
- [ ] `boutique_accessibility.png` (256x256, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (fitting-room overlays and Premium Stock states in separate groups)
- **Documentation:** Animation timing reference sheet (entry bass drop, strobe cycle, premium reveal) + gear lit/unlit variant map

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Neon Pink #FF1493, Chrome Silver #C0C0C0, Club Purple #4B0082, LED Blue #00BFFF)
- [ ] Honest plaque text ("Actual belonging sold separately") readable on examine
- [ ] Premium Stock Locked and Revealed states align to the same alcove footprint
- [ ] Lit gear variants register-aligned with their unlit counterparts
- [ ] Accessibility visual alternatives included for all audio cues (bass drop, whoosh, chime, fanfare, unlock sting)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (status theater sold with a wink) is clear throughout all assets
- [ ] Hidden gags discoverable: empty wristband holders, altitude-priced platform pyramid, unquantified VIP meter
- [ ] Performance optimized (on-demand fitting room, gated Premium assets, CPU particles)
- [ ] Touch zone sizing considered (44px minimum — shop buttons and booth toggles compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (shape-coded stat icons, padlock/rope banners)
- [ ] Social media viral potential maximized (group mirror moment, premium reveal composition)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Debaucheryville / Absinthe Arcade only; Prague referenced solely as cultural inspiration in design docs, never in-game text |
| Cultural Specificity | ✅ | Eastern European club-scene hierarchy and VIP status games |
| Satirical Targets Appropriate | ✅ | Status-seeking and VIP culture — not the clubbers, not the locals |
| Seedy Underbelly Present | ✅ | Premium prices for "VIP potential" that may never materialize |
| Gameplay Value Established | ✅ | Stat gear (Style/Intimidation/Visibility), boss-gated stock, Bravado hooks, Velvet Curtain integration |
| Technical Feasibility | ✅ | 8 sheets, on-demand overlays, region-swap gear system — all standard Godot 4.x |
| Performance Budget | ✅ | 60 FPS / 14 draw calls / 34 MB per profile; estimate ~19 MB |
| Accessibility Features | ✅ | Strobe-disable path, visual cues for every audio beat, shape-coded stats |
| No Crypto Elements | ✅ | Pure fashion status commerce (profile-confirmed) |
| Social Media Integration | ✅ | Five viral moments identified, quotes sourced from profile dialogue |

**Once these assets land, Neon & Chrome Boutique becomes the game's most honest con: a glowing chrome temple where the player can buy presence by the inch, watch three bros calculate their VIP percentage in a mirror, and discover that the only item in the shop with real power is the one you can't buy until you've already proven you don't need it.**
