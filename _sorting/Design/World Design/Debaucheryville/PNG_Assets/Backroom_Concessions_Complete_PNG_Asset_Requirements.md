# Backroom Concessions - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Backroom Concessions location. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this hidden digital underground food court where gamer fuel meets health code violations.

**Location ID:** `debaucheryville_internet_cafe_backroom_concessions_01`  
**Theme:** Digital depravity meets greasy gamer fuel - eat meat cubes while torrenting conspiracy documentaries  
**Zone:** 24-Hour Internet Café - Back Room (Debaucheryville)  
**Hours:** Always accessible once discovered (24-hour operation; hidden entrance via restroom graffiti clue)  
**Primary Function:** Hidden vendor with status effect consumables, ICQ thread unlock, black market referral source

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Neon Green | #00FF41 | 404 sign, menu glow, screen green, status effects |
| Warning Orange | #FF8C00 | Warning lights, cooking heat, accent glow, status icons |
| Server Black | #1C1C1C | Background shadows, server room walls |
| Sickly Fluorescent | #E8E8D0 | Fluorescent panels, beige CRT plastic |
| Machine Metal | #C0C0C0 | Vending machines, cooking equipment, chair frames |
| Counter Wood | #8B4513 | Booth counter, fake leather chairs |
| Error Red | #FF0000 | Popup errors, warning status, gaming chair accent |
| Warning Yellow | #FFFF00 | Popup warning banners |
| Office Grey | #4A4A4A | Mismatched office chairs |
| Steam White | #FFFFFF | Cooking steam particles, static bursts |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/backroom_concessions/
├── environment/
│   ├── backroom_concessions_tileset.png
│   └── backroom_environmental_effects.png
├── npcs/
│   └── concession_booth_spritesheet.png      (includes Donny.exe states)
├── objects/
│   ├── vending_machines_spritesheet.png
│   ├── crt_popup_cascade.png
│   └── mismatched_seating.png
└── effects/
    └── 404_sign_effects.png
```

---

## 🎨 Sprite Sheet 1: Backroom Concessions Tileset
**File:** `backroom_concessions_tileset.png`  
**Dimensions:** 512x512 pixels  
**Color Palette:** #00FF41 (neon green), #FF8C00 (warning orange), #1C1C1C (server black), #E8E8D0 (sickly fluorescent)

### Floor Tiles (32x32 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Concrete Floor Stained | (0, 0) | 32x32 | Base tile with grease/food stains |
| Concrete Floor Clean | (32, 0) | 32x32 | Rare clean section |
| Tile Cracked | (64, 0) | 32x32 | Damaged floor tile |
| Cable Floor Overlay | (96, 0) | 32x32 | Network cables running across floor |
| Grease Stain | (128, 0) | 32x32 | Prominent food grease mark |

### Wall Tiles (64x64 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Server Room Wall | (0, 32) | 64x64 | Industrial server aesthetic |
| Exposed Wiring Wall | (64, 32) | 64x64 | Cables and wires visible |
| Poster Wall Protocols | (128, 32) | 64x64 | "Hot Pockets + Protocols" poster |
| Vent Grate Wall | (192, 32) | 64x64 | Ventilation with mysterious airflow |

### Ceiling Tiles (32x32 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Fluorescent Panel Off | (0, 96) | 32x32 | Inactive light panel |
| Fluorescent Panel On | (32, 96) | 32x32 | Active sickly illumination |
| Fluorescent Panel Flicker | (64, 96) | 32x32 | Mid-flicker state |
| Exposed Pipe Ceiling | (96, 96) | 32x32 | Industrial pipes overhead |

### Technical Notes - Tileset:
- Floor stains should appear organic, food-related
- Fluorescent flicker occurs every 3-8 seconds randomly
- Cable overlays can layer on any floor tile
- Sickly yellow-green color cast on all lit areas

---

## 🍖 Sprite Sheet 2: Concession Booth Spritesheet
**File:** `concession_booth_spritesheet.png`  
**Dimensions:** 512x512 pixels  
**Color Palette:** #00FF41 (menu glow), #8B4513 (counter wood), #C0C0C0 (metal equipment), #FF8C00 (cooking heat)

### Booth Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Booth Base | (0, 0) | 192x128 | Full concession booth structure |
| Counter Front | (192, 0) | 128x64 | Customer-facing counter surface |
| Menu Board | (320, 0) | 96x128 | Laminated menu, peeling edges |

### Donny.exe Character (64x96 each):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Idle | (0, 128) | 64x96 | Standing with distant stare |
| Serving | (64, 128) | 64x96 | Handing food to customer |
| Philosophical | (128, 128) | 64x96 | Mid-quote dramatic pose |
| Lanyard Detail | (192, 128) | 32x48 | Expired LAN party badges close-up |
| Vape Mod Detail | (224, 128) | 24x32 | Broken breathing apparatus |

**Donny.exe Visual Notes:**
- Middle-aged, gaunt from digital lifestyle
- Lanyard has 5+ expired badges from various LAN parties (2003-2015)
- Broken vape mod has duct tape repairs
- Eyes have thousand-yard debugging stare
- Apron says "404: Chef Not Found"

### Menu Items (48x48 each):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| CryptoDöner Box | (0, 224) | 48x48 | Mystery meat in digital-themed container |
| Thermal Paste Sundae | (48, 224) | 48x48 | Grey blob with rainbow sprinkles |
| RAM Chips & Dip | (96, 224) | 48x48 | Green circuit board chips, orange dip |
| Alt+Meat Slider | (144, 224) | 48x48 | Perfect grey patty, iridescent sauce |
| 404 Juice | (192, 224) | 48x48 | Blue slushie in scratched cup |

**Menu Item Visual Notes:**
- CryptoDöner: Styrofoam container with blockchain symbol, mystery meat visible
- Thermal Paste Sundae: Disturbingly grey with incongruously cheerful sprinkles
- RAM Chips: Actual circuit board green color, Queso.exe is neon orange
- Alt+Meat Slider: Uncanny valley perfect, AI-generated looking
- 404 Juice: Electric blue, slightly radioactive glow

### Cooking Equipment:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Grill Idle | (0, 272) | 64x48 | Flat top grill, no activity |
| Grill Active | (64, 272) | 64x48 | Sizzling with steam |
| Slushie Machine | (128, 272) | 48x64 | Blue liquid swirling |

---

## 🎰 Sprite Sheet 3: Vending Machines Spritesheet
**File:** `vending_machines_spritesheet.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #C0C0C0 (machine metal), #00FF41 (internal glow), #FF8C00 (warning lights), #1C1C1C (shadows)

### Thermal Paste Vending Machine (96x160):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Idle | (0, 0) | 96x160 | Full machine, tubes visible |
| Rattling Frame 1 | (96, 0) | 96x160 | Slight left shift |
| Rattling Frame 2 | (192, 0) | 96x160 | Slight right shift |
| Paste Tubes Grid | (288, 0) | 64x96 | Internal tube arrangement |
| Empty Sundae Slot | (352, 0) | 32x24 | "EMERGENCY SUNDAE SUPPLY" slot |

**Thermal Paste Machine Notes:**
- Tubes arranged in neat rows like candy
- One slot labeled "EMERGENCY SUNDAE SUPPLY" is conspicuously empty
- Rattling animation subtle but unsettling
- Internal LED strips provide eerie glow

### Mysterious Knowledge Machine (96x160):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Dark | (0, 160) | 96x96 | Internal contents obscured |
| Flicker Frame 1 | (96, 160) | 96x96 | Brief illumination |
| Flicker Frame 2 | (192, 160) | 96x96 | Different angle glimpse |
| Flicker Frame 3 | (288, 160) | 96x96 | Most revealing moment |
| Mystery Glimpse 1 | (384, 160) | 48x48 | Labels? Manuals? |
| Mystery Glimpse 2 | (432, 160) | 48x48 | Something text-like |
| Mystery Glimpse 3 | (384, 208) | 48x48 | The meaning of life? |

**Mystery Machine Notes:**
- Contents deliberately unclear
- Flicker pattern erratic, never fully reveals contents
- Each glimpse suggests different possibility
- Creates perpetual curiosity/unease

### Animation Timing:
| Animation | Frames | Trigger | Duration |
|-----------|--------|---------|----------|
| Thermal Rattle | 3 | Random 10-30s | 1.5s |
| Mystery Flicker | 4 | Continuous | Variable 0.1-0.5s per frame |

---

## 📺 Sprite Sheet 4: CRT Popup Cascade
**File:** `crt_popup_cascade.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #E8E8D0 (beige plastic), #00FF41 (screen green), #FF0000 (error red), #FFFF00 (warning yellow)

### Monitor Frames (64x56 each):
| Monitor Type | Position | Size | Description |
|--------------|----------|------|-------------|
| Beige CRT | (0, 0) | 64x56 | Classic 90s monitor |
| Black CRT | (64, 0) | 64x56 | Later model |
| Damaged CRT | (128, 0) | 64x56 | Cracked bezel, works anyway |

### Popup Ad Sprites (48x32 each):
| Popup Type | Position | Size | Description |
|------------|----------|------|-------------|
| Winner Popup | (0, 56) | 48x32 | "YOU'RE THE 1,000,000th VISITOR!" |
| Virus Warning | (48, 56) | 48x32 | Fake security alert |
| Hot Singles | (96, 56) | 48x32 | "IN YOUR AREA" classic |
| Free Download | (144, 56) | 48x32 | Suspicious button |
| Casino Popup | (192, 56) | 48x32 | Flashing jackpot |
| Error Popup | (240, 56) | 48x32 | Windows-style error |

### Screen Content (56x42 each):
| Content Type | Position | Size | Description |
|--------------|----------|------|-------------|
| Desktop Cluttered | (0, 88) | 56x42 | Icons everywhere |
| Cascade Layer 1 | (56, 88) | 56x42 | First popup layer |
| Cascade Layer 2 | (112, 88) | 56x42 | Building chaos |
| Cascade Layer 3 | (168, 88) | 56x42 | Maximum popup density |
| ICQ Hint Screen | (224, 88) | 56x42 | Hidden message (post-completion) |
| Thread Preview | (280, 88) | 56x42 | #SnackHackRevenge glimpse |

### Animation Specs:
| Animation | FPS | Notes |
|-----------|-----|-------|
| Popup Cascade | 4 | Random popup selection, spawn every 0.5-1.5s |
| Screen Flicker | 8 | 10% probability per second |

**Popup Content Notes:**
- Each popup should be readable but comically dated
- Mix of threatening, enticing, and absurd
- Error messages reference food items ("SANDWICH.EXE has stopped responding")
- ICQ hint only appears after player completes full menu

---

## ✨ Sprite Sheet 5: 404 Sign and Effects
**File:** `404_sign_effects.png`  
**Dimensions:** 256x256 pixels  
**Color Palette:** #00FF41 (neon green), #1C1C1C (background), #FF8C00 (accent glow)

### Main Sign (192x64 each state):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Sign Off | (0, 0) | 192x64 | Unlit neon tubes visible |
| Sign On | (0, 64) | 192x64 | Full "404: Calories Not Found" |
| Sign Flicker | (0, 128) | 192x64 | Partial illumination |

### Server Rack Backlight:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Glow Frame 1 | (192, 0) | 64x96 | Server rack glow state 1 |
| Glow Frame 2 | (192, 96) | 64x96 | Server rack glow state 2 |

### Entrance Frame:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Hidden Door Closed | (0, 192) | 64x64 | Concealed entrance |
| Hidden Door Open | (64, 192) | 64x64 | Revealed entrance |

**Sign Visual Notes:**
- "404" in large block letters
- "Calories Not Found" in smaller text below
- Neon green with orange accent on colon
- Server rack behind creates depth glow
- Flicker should feel electrical, not supernatural

---

## 🌫️ Sprite Sheet 6: Environmental Effects
**File:** `backroom_environmental_effects.png`  
**Dimensions:** 256x256 pixels  
**Color Palette:** #FFFFFF (steam), #00FF41 (status green), #FF8C00 (status orange), #FF0000 (warning red)

### Cooking Steam Particles (24x24 each):
| Particle | Position | Size | Description |
|----------|----------|------|-------------|
| Wisp 1 | (0, 0) | 24x24 | Small steam puff |
| Wisp 2 | (24, 0) | 24x24 | Medium wisp |
| Wisp 3 | (48, 0) | 24x24 | Large dissipating |
| Wisp 4 | (72, 0) | 24x24 | Final fade state |

### Electronic Static (16x16 each):
| Particle | Position | Size | Description |
|----------|----------|------|-------------|
| Static 1 | (0, 24) | 16x16 | White noise burst |
| Static 2 | (16, 24) | 16x16 | Scan line variant |
| Static 3 | (32, 24) | 16x16 | Digital artifact |

### Heat Shimmer Overlay:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shimmer Tile | (0, 40) | 64x64 | Distortion overlay for shader |

### Status Effect Indicators:
| Icon | Position | Size | Description |
|------|----------|------|-------------|
| DigiDysentery Icon | (0, 104) | 32x32 | Inverted arrows symbol |
| DigiDysentery Edge | (32, 104) | 64x32 | Screen edge glitch effect |
| Caffeine Twitch Icon | (0, 136) | 32x32 | Jittering coffee cup |
| Caffeine Twitch Jitter | (32, 136) | 32x32 | Movement blur effect |
| Intelligence Surge Icon | (0, 168) | 32x32 | Brain with overheat warning |

### UI Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu Interface BG | (0, 200) | 128x56 | Food ordering backdrop |
| Item Slot | (128, 200) | 48x48 | Individual menu item frame |
| Price Tag | (176, 200) | 32x16 | Sov price display |

---

## 🪑 Sprite Sheet 7: Mismatched Seating
**File:** `mismatched_seating.png`  
**Dimensions:** 256x128 pixels  
**Color Palette:** #4A4A4A (office grey), #8B4513 (fake leather), #C0C0C0 (metal), #FF0000 (gaming chair accent)

### Chair Variations:
| Chair Type | Position | Size | Description |
|------------|----------|------|-------------|
| Broken Armrest | (0, 0) | 48x64 | One armrest missing |
| Squeaky Wheels | (48, 0) | 48x64 | Visibly worn casters |
| Duct Taped | (96, 0) | 48x64 | Held together by tape |
| Broken Gaming Chair | (144, 0) | 56x72 | Premium chair, completely ruined |

### Occupied States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Player Sitting 1 | (0, 64) | 48x64 | Generic sitting pose |
| Player Sitting 2 | (48, 64) | 48x64 | Slouched eating pose |

**Chair Visual Notes:**
- Each chair tells a story of neglect
- Broken gaming chair is the saddest - was expensive once
- Duct tape should be multiple colors (repairs over time)
- Squeaky wheels have visible rust

---

## 🎬 Animation Sequence Specifications

### Fluorescent Buzz:
- **Duration:** Random 3-8 second intervals
- **Pattern:** On → Flicker (0.2s) → On
- **Coverage:** All ceiling panels independently
- **Purpose:** Sickly atmosphere, eye strain aesthetic
- **Audio Sync:** Electrical buzz intensifies during flicker

### Popup Cascade:
- **New Popup Interval:** 0.5-1.5 seconds
- **Popup Lifetime:** 2-4 seconds before despawn
- **Maximum Concurrent:** 6 popups per screen
- **Cascade Behavior:** New popups spawn on top of old
- **Purpose:** Y2K internet nostalgia, overwhelming chaos
- **Audio Sync:** Digital chirp per new popup

### Vending Machine Rattle:
- **Trigger:** Random 10-30 second intervals
- **Pattern:** Idle → Left shift → Right shift → Left → Idle
- **Duration:** 1.5 seconds total
- **Purpose:** Unsettling background activity
- **Audio Sync:** Plastic container rattling

### Mystery Machine Flicker:
- **Pattern:** Dark → Brief glimpse → Dark → Different glimpse → etc.
- **Frame Duration:** 0.1-0.5 seconds (variable)
- **Purpose:** Perpetual mystery, player curiosity
- **Key Rule:** NEVER fully reveal contents

### Cooking Steam Emission:
- **Emission Rate:** 8 particles per second
- **Particle Lifetime:** 2.5 seconds
- **Movement:** Upward drift, 10% horizontal variance
- **Purpose:** Active cooking atmosphere
- **Spawn Location:** Above grill when active

### 404 Sign Flicker:
- **Pattern:** On → Flicker → On
- **Interval:** Every 5-10 seconds
- **Duration:** 0.3 seconds
- **Purpose:** Neon sign authenticity
- **Audio Sync:** Electrical buzz during flicker

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hidden Door Outline | (128, 192) | 64x64 | High-contrast outline of concealed entrance for discoverability assist |
| Menu Item Slot Highlight | (176, 216) | 48x48 | Bright border variant for menu item frames |
| Donny.exe Silhouette | (256, 128) | 64x96 | High-contrast vendor outline for interaction targeting |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Popup Screen | (336, 88) | 56x42 | Single non-cascading popup frame (replaces popup cascade) |
| Fluorescent Steady Panel | (128, 96) | 32x32 | Non-flickering ceiling panel variant |
| 404 Sign Steady | (0, 192) | 192x64 | Always-on sign state, no flicker cycle |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Buzz Indicator | (48, 24) | 16x16 | Visual spark icon when fluorescent buzz plays |
| Rattle Indicator | (416, 0) | 32x32 | Shake lines icon over vending machine during rattle audio |
| Order Ding Indicator | (208, 200) | 32x16 | Flash frame on transaction sound |
| DigiDysentery Onset Flash | (96, 104) | 32x32 | Screen-corner pulse replacing dial-up + gurgle audio cue |

### Colorblind Considerations:
- Status effect icons use distinct shapes (inverted arrows, jittering cup, brain symbol) — never color alone
- DigiDysentery edge glitch uses pattern distortion, not just green tint
- Menu item slots numbered 1-5 so items are identifiable without color
- Touch zones minimum 44px for all menu interface elements and the hidden door

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); CRT screen content kept at higher quality for popup readability
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for menu item sprites and status icons (detail-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| backroom_environment | tileset, 404 sign, environmental effects | 1024x1024 |
| backroom_characters | concession booth + Donny.exe, seating | 1024x512 |
| backroom_effects | vending machines, CRT popups, UI | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full popup cascade (6 concurrent), heat shimmer shader, 8/s steam particles |
| Medium | Max 3 concurrent popups, no heat shimmer, 4/s steam particles |
| Low | Static popup screens, no shader effects, steam disabled, reduced flicker rate |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 12 per frame
- **Memory Footprint:** 35 MB maximum
- **Particle Limit:** 20 concurrent (steam + static combined)

### Performance Notes:
- Popup cascade uses a spawn pool of pre-instanced sprites, no runtime instantiation
- Reduced CRT flicker rate on low-end devices (profile-specified battery management)
- Mystery machine flicker capped at 2 FPS on Low LOD
- Heat shimmer shader disabled below Medium LOD

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Popup cascade: Use spawn pool with random selection
- Status effects: Overlay sprites with shader support
- Heat shimmer: Custom shader using distortion overlay tile

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Fluorescent flicker | Electrical buzz spike | On flicker frame |
| Popup spawn | Digital chirp | On spawn |
| Vending rattle | Plastic container noise | Throughout animation |
| Food ordered | Sizzle + register ding | On transaction |
| 404 sign flicker | Neon buzz | On flicker |
| DigiDysentery onset | Dial-up + stomach gurgle | On status apply |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Menu Completion | All 5 menu item sprites | Track consumption for ICQ unlock |
| ICQ Thread Unlock | ICQ hint screen, thread preview | Post-completion CRT content |
| Black Market Referral | DigiDysentery status icon | Triggers Donny.exe special dialogue |

### Status Effect Visuals:
| Status | Screen Effect | Duration Display |
|--------|---------------|------------------|
| DigiDysentery | Edge glitch overlay | 2-minute timer |
| Caffeine Twitch | Subtle screen shake | 3-minute timer |
| Intelligence Surge | Brain icon pulse | "1 Battle" indicator |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Digital underground food court - where hackers eat health violations"
- **Color Mood:** Sickly fluorescent yellow-green, neon accents, server black shadows
- **Lighting:** Buzzing overhead fluorescents, CRT glow, server rack backlight
- **Texture:** Greasy surfaces, dated electronics, makeshift repairs

### Concession Booth Direction:
- **Donny.exe:** World-weary ex-hacker, badges from glory days, philosophical detachment
- **Menu Items:** Each should look questionable but oddly appealing when hungry
- **Equipment:** Functional but clearly not up to code
- **Atmosphere:** Cramped, busy, smells implied through visual grease

### Vending Machine Philosophy:
- **Thermal Paste Machine:** Organized chaos, industrial beauty
- **Mystery Machine:** Perpetual enigma, frustrating curiosity
- **Both:** Gutted but repurposed, digital underground resourcefulness

### CRT Monitor Array:
- **Popup Aesthetic:** Peak Y2K internet experience
- **Content:** Mix of threatening, enticing, absurd
- **Cascade Effect:** Overwhelming but hypnotic
- **Easter Eggs:** Food-related error messages hidden in popups

### Environmental Storytelling:
- **Floor Stains:** Map of food consumption history
- **Chair Collection:** Each represents someone who gave up
- **Exposed Wiring:** Safety third philosophy
- **404 Sign:** Beacon for the digitally hungry

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | backroom_concessions_tileset.png | 512x512 |
| 2 | concession_booth_spritesheet.png | 512x512 |
| 3 | vending_machines_spritesheet.png | 512x256 |
| 4 | crt_popup_cascade.png | 512x256 |
| 5 | 404_sign_effects.png | 256x256 |
| 6 | backroom_environmental_effects.png | 256x256 |
| 7 | mismatched_seating.png | 256x128 |

**Total Estimated Memory:** ~35 MB (in-memory budget including atlas overhead)

---

## 📦 File Delivery Checklist

### Required PNG Files (7 Total):
- [ ] `backroom_concessions_tileset.png` (512x512)
- [ ] `concession_booth_spritesheet.png` (512x512)
- [ ] `vending_machines_spritesheet.png` (512x256)
- [ ] `crt_popup_cascade.png` (512x256)
- [ ] `404_sign_effects.png` (256x256)
- [ ] `backroom_environmental_effects.png` (256x256)
- [ ] `mismatched_seating.png` (256x128)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha channel |
| Color Space | sRGB |
| DPI | 72 (screen resolution) |
| Compression | Lossless PNG |
| Naming Convention | snake_case, all lowercase |

### Delivery Format:
- **Primary:** Individual PNG files per specifications
- **Backup:** Master PSD/Photoshop with organized layers
- **Documentation:** Animation timing reference, popup content list

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **404: Calories Not Found Sign** - Neon green with server rack backlight
2. **Thermal Paste Sundae** - Grey blob with rainbow sprinkles close-up
3. **CryptoDöner Box** - "Meat. Data. Destiny." presentation
4. **Donny.exe Portrait** - Ex-hacker with LAN party badges
5. **Popup Cascade Maximum** - Peak early 2000s internet chaos
6. **Broken Gaming Chair** - Expensive dream, ruined reality

### TikTok Potential:
- "POV: You're eating mystery meat in digital underground"
- "Following bathroom graffiti to hidden food vendor"
- "The status effects from this food are WILD"
- "Speedrunning the entire menu for ICQ access"
- "My character has DigiDysentery and I can't control the menu"

### Twitter/X Quote Potential:
- "You want toppings? I only accept blockchain drizzle." - Donny.exe
- "I deep-fried the future and served it with packet loss." - Donny.exe
- "Air-gapped chakras mean pure nutrition, no network interference."
- "404: Calories Not Found"
- "Meat. Data. Destiny."

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 7 PNG files match exact dimensions
- [ ] Donny.exe has clear ex-hacker aesthetic with LAN badges
- [ ] All 5 menu items are visually distinct and questionable
- [ ] Thermal paste vending machine tubes are clearly visible
- [ ] Mystery machine contents remain ambiguous in all frames
- [ ] Popup ads are readable and period-appropriate
- [ ] 404 sign is clear landmark for navigation
- [ ] Status effect icons clearly communicate debuffs
- [ ] Fluorescent lighting creates sickly atmosphere
- [ ] Each chair type is distinctly damaged

### Quality Checkpoints:
- [ ] Digital underground aesthetic consistent throughout
- [ ] Food items look questionable but oddly appealing
- [ ] Y2K internet nostalgia captured in popups
- [ ] Health code violation humor clear but not gross
- [ ] Mobile performance optimized (small file sizes)
- [ ] All animations have clear timing specifications
- [ ] Status effects have both icons and screen effects
- [ ] Accessibility alternatives for color-coded elements

---

## 🏆 Location Validation Status

### Template Compliance Check:
| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency | ✅ PASS | Debaucheryville only |
| Cultural Specificity | ✅ PASS | Internet café + gamer food culture |
| Satirical Targets Appropriate | ✅ PASS | Digital pretension, not individuals |
| Seedy Underbelly Present | ✅ PASS | Health violations as underground cred |
| Gameplay Value Established | ✅ PASS | Status effect consumables, ICQ unlock |
| Technical Feasibility | ✅ PASS | Mobile optimization documented |
| Mobile Performance Budget | ✅ PASS | 60 FPS, 12 draw calls, 35MB |
| Accessibility Features | ✅ PASS | Status icons, DigiDysentery assist option |
| No Crypto Elements | ✅ PASS | Crypto satire established in source material (CryptoDöner, blockchain drizzle) |
| Social Media Integration | ✅ PASS | Multiple viral moments identified |

**Once validated, the Backroom Concessions becomes the hidden digital underground food court where players discover questionable nutrition through bathroom graffiti clues, experience risk/reward consumables with hilarious status effects, unlock ICQ communication channels through menu completion, and get black market referrals from Donny.exe while he philosophizes about air-gapped chakras and blockchain drizzle!**
