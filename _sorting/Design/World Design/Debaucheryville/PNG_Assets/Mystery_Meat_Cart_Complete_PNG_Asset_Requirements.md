# Cirque du Shady – Mystery Meat Cart - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Mystery Meat Cart - a fever dream of carnival grift, forbidden meats, and unlicensed side effects where state fair deep-fryer meets darkweb wet market.

**Location ID:** `debaucheryville_cirque_mystery_cart_01`  
**Theme:** Carnival grift, forbidden meats, unlicensed side effects  
**Zone:** Cirque du Shady (next to the carnival ringmaster tent)  
**Hours:** Circus hours; enhanced effects during nighttime performances  
**Primary Function:** Sketchy food vendor, status effect gambles, Carnival Carnage quest access

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Carnival Red | #DC143C | Cart panels, strobe cycle, sign lettering |
| Toxic Neon Green | #39FF14 | Underglow, "enhanced" food items, mystery vapor |
| Circus Shadow Purple | #4B0082 | Deep shadows, strobe cycle, tent darkness |
| Saddle Brown | #8B4513 | Meat brown range (upper end) |
| Dim Gray | #696969 | Meat brown range (lower end), grey sweaty tube meat |
| Lime Glow | #00FF00 | Glow effects at 50% opacity pulse (Brain Brat core) |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/mystery_meat_cart/
├── environment/
│   └── circus_cart_environment_complete.png
├── npcs/
│   └── chef_chuckles_character_animations.png
├── objects/
│   ├── chef_chuckles_mystery_cart_complete.png
│   ├── mystery_menu_items_detailed.png
│   └── animated_signage_states.png
├── effects/
│   └── carnival_effects_particles.png
└── ui/
    └── mystery_cart_ui.png
```

---

## 🎪 Sprite Sheet 1: Mystery Cart Complete
**File:** `chef_chuckles_mystery_cart_complete.png`  
**Dimensions:** 1024x768 pixels  
**Color Palette:** #DC143C (carnival red), #39FF14 (toxic neon), #4B0082 (circus shadow)

### Cart States (384x256 each):
| State | Position | Description |
|-------|----------|-------------|
| Idle | (0, 0) | Steam wispy, rotisserie slow |
| Active Cooking | (384, 0) | Heavy steam, fast spin, grease |
| Cleaning Mode | (768, 0) | Suspicious rag wiping (256x256) |

### Carousel Rotisserie (96x128 each, 8 frames):
| Frame | Position | Description |
|-------|----------|-------------|
| Frame 1 | (0, 256) | Starting position |
| Frame 2 | (96, 256) | 45° rotation |
| Frame 3 | (192, 256) | 90° rotation |
| Frame 4 | (288, 256) | 135° rotation |
| Frame 5 | (384, 256) | 180° rotation |
| Frame 6 | (480, 256) | 225° rotation |
| Frame 7 | (576, 256) | 270° rotation |
| Frame 8 | (672, 256) | 315° rotation |

### Lighting & Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Neon Underglow | (0, 384) | 256x64 | Toxic green #39FF14 |
| Steam Point 1-4 | (0-96, 448) | 32x32 ea | Emission points |
| Grease Drip Tray | (128, 448) | 96x48 | Overflowing |

### Carnival Lights (192x64 each):
| State | Position | Description |
|-------|----------|-------------|
| Full Strobe | (0, 480) | Maximum intensity |
| Medium Flash | (192, 480) | Reduced flash |
| Reduced | (384, 480) | Accessibility mode |
| Disabled | (576, 480) | Static lighting |

---

## 🤡 Sprite Sheet 2: Chef Chuckles Character
**File:** `chef_chuckles_character_animations.png`  
**Dimensions:** 512x512 pixels  

### Butterfly Knife Flipping (80x128 each, 6 frames):
| Frame | Position | Description |
|-------|----------|-------------|
| Frame 1 | (0, 0) | Knife start |
| Frame 2 | (80, 0) | Flip motion |
| Frame 3 | (160, 0) | Mid-flip |
| Frame 4 | (240, 0) | Catch prep |
| Frame 5 | (320, 0) | Catch |
| Frame 6 | (400, 0) | Chop/serve |

### Food Service (80x128 each):
| Action | Position | Description |
|--------|----------|-------------|
| Prep | (0, 128) | Mystery ingredients |
| Theatrical Wrap | (80, 128) | Flourish |
| Serve Threat | (160, 128) | Veiled menace |
| Payment | (240, 128) | Taking coins |

### Business Hours - Mask ON (80x128 each):
| Pose | Position | Description |
|------|----------|-------------|
| Threatening Service | (0, 256) | Active |
| Deadpan Menace | (80, 256) | Stare |
| Food Pun Delivery | (160, 256) | Speaking |

### Off Hours - Mask OFF (80x128 each):
| Pose | Position | Description |
|------|----------|-------------|
| Relaxed Threat | (240, 256) | Still scary |
| Knife Maintenance | (320, 256) | Caring for blade |

### Outfit Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Clown Shoes | (0, 384) | 64x48 | Oversized, practical |
| Sleeveless Tuxedo | (64, 384) | 64x96 | Stained |
| Butterfly Knife | (128, 384) | 48x32 | Chrome finish |
| Cracked Mask | (176, 384) | 48x48 | Porcelain, unsettling |
| Lighter Fluid Vapor | (224, 384) | 32x48 | Signature smell |

**Chef Chuckles Visual Notes:**
- Cracked porcelain clown mask during business hours
- Expert butterfly knife sausage flipping
- Sleeveless tuxedo (stained)
- Clown shoes (oversized but practical)
- Smells like lighter fluid

---

## 🌭 Sprite Sheet 3: Menu Items
**File:** `mystery_menu_items_detailed.png`  
**Dimensions:** 1024x512 pixels  

### Doner of Illusions™ - 7 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Spinning Heap | (0, 0) | 128x96 | Shredded meat base |
| Gummy Bears Mixed | (128, 0) | 64x64 | Embedded candies |
| Absinthe Glaze | (192, 0) | 64x64 | Green shimmer |
| Wrapped Serving | (256, 0) | 96x96 | Ready to consume |

### Sausage of Suspicion - 6 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Grey Sweaty Tube | (0, 96) | 96x64 | Questionable meat |
| Wooden Stick | (96, 96) | 32x64 | Holding apparatus |
| Whisper Waves | (128, 96) | 64x32 | Audio visualization |
| Suspicious Angles | (192, 96) | 96x64 | Every angle bad |

### Clown Dog Deluxe™ - 9 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Red Licorice Bun | (0, 160) | 96x64 | Candy bread |
| Mustard Smiley | (96, 160) | 48x48 | Face condiment |
| Pop Rocks Relish | (144, 160) | 48x32 | Explosive garnish |
| Assembled Grotesque | (192, 160) | 128x96 | Full horror |

### Meatball on a Lollipop Stick - 5 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Spherical Mystery | (0, 256) | 64x64 | Meat ball |
| Candy Stick | (64, 256) | 24x64 | Inappropriate handle |
| Structural Issue | (88, 256) | 64x64 | Impossible physics |
| Bite Marks | (152, 256) | 32x32 | Previous attempts |

### Glizzénstein's Brain Brat - 12 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Glowing Interior | (0, 320) | 96x64 | AI core visible |
| Circuit Pattern | (96, 320) | 64x64 | Meat surface |
| Organic Digital | (160, 320) | 96x64 | Mixed materials |
| Pulsing Package | (256, 320) | 96x64 | Serving container |

### Food Item Art Notes (ported from legacy spec):
- **Gummy Bears Mixed In** - Colorful candy corruption visible
- **Grey Sweaty Tube Meat** - Unnaturally moist appearance
- **Candy Stick Inappropriate** - Child-targeted presentation
- **Previous Bite Marks** - Evidence of prior consumption
- **Organic Digital Mix** - Grotesque fusion aesthetic

### Food Item Color Requirements (ported from legacy spec):
- Use sickly greens (#39FF14) for "enhanced" items
- Meat browns range: #8B4513 (saddle brown) to #696969 (dim gray)
- Glow effects: #00FF00 (lime) with 50% opacity pulse

---

## 🎡 Sprite Sheet 4: Environment
**File:** `circus_cart_environment_complete.png`  
**Dimensions:** 1024x768 pixels  

### Ringmaster Tent Corner:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tent Corner | (0, 0) | 256x256 | Location context |

### Carnival Chaos Background:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Distressed Families | (256, 0) | 192x128 | Silhouettes |
| Circus Performers | (448, 0) | 192x128 | Other acts |
| Audio Waves | (640, 0) | 128x64 | Sound visualization |
| Safety Violations | (256, 128) | 256x128 | Evidence |

### Environmental Hazards:
| Hazard | Position | Size | Description |
|--------|----------|------|-------------|
| Electrical Sparks | (0, 256) | 64x64 | Wire issues |
| Sanitation Nightmare | (64, 256) | 96x64 | Health codes |
| Structural Concerns | (160, 256) | 96x64 | Stability |
| No Authority Figures | (256, 256) | 96x48 | Complete lack of oversight (ported from legacy; position assigned in BASE layout) |

### Atmosphere Particles (ported from legacy spec, 48x32 each):
| Particle | Position | Description |
|----------|----------|-------------|
| Steam from Cooking | (0, 320) | Food prep vapor |
| Grease Vapor Rising | (48, 320) | Oil smoke |
| Carnival Dust/Sawdust | (96, 320) | Floating debris |
| Mystery Substance Particles | (144, 320) | Unidentifiable mist |

---

## ✨ Sprite Sheet 5: Particle Effects
**File:** `carnival_effects_particles.png`  
**Dimensions:** 512x256 pixels  

### Cooking Steam (32x48 each):
| Wisp | Position | Description |
|------|----------|-------------|
| Wisp 1 | (0, 0) | Initial rise |
| Wisp 2 | (32, 0) | Expanding |
| Wisp 3 | (64, 0) | Swirling |
| Wisp 4 | (96, 0) | Dissipating |

### Mystery Vapor (24x32 each):
| Particle | Position | Description |
|----------|----------|-------------|
| Green 1 | (0, 48) | Toxic color |
| Green 2 | (24, 48) | Variant |

### Grease Steam (24x24 each):
| Particle | Position | Description |
|----------|----------|-------------|
| Oily 1 | (0, 80) | Heavy |
| Oily 2 | (24, 80) | Droplets |

### Carnival Strobe (32x32 each):
| Color | Position | Description |
|-------|----------|-------------|
| Red | (0, 104) | #DC143C |
| Green | (32, 104) | #39FF14 |
| Purple | (64, 104) | #4B0082 |

### Electrical Sparks (16x16 each):
| Spark | Position | Description |
|-------|----------|-------------|
| Spark 1 | (0, 136) | Small |
| Spark 2 | (16, 136) | Medium |
| Spark 3 | (32, 136) | Large |

### Sawdust Debris (8x8 each):
| Particle | Position | Description |
|----------|----------|-------------|
| Particle 1-3 | (0-16, 152) | Flutter |

---

## 📺 Sprite Sheet 6: Animated Signage
**File:** `animated_signage_states.png`  
**Dimensions:** 512x256 pixels  

### Sign States (256x64 each):
| State | Position | Description |
|-------|----------|-------------|
| SHADE MEAT 4 CLOWN SOULS | (0, 0) | Main state |
| Shady Dogs | (0, 64) | Glitch state 1 |
| Meat Roulette | (0, 128) | Glitch state 2 |
| Free Sample (Not Legally Binding) | (0, 192) | Glitch state 3 |

### Infrastructure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bulb Border Normal | (256, 0) | 128x64 | Working lights |
| Bulb Border Burned | (384, 0) | 128x64 | Some out |
| LED Strip | (256, 64) | 192x32 | Hookah hose mount |
| Spark Points | (256, 96) | 64x32 | Electrical issues |

### Audio Cue Visuals (64x64 each):
| Cue | Position | Description |
|-----|----------|-------------|
| Honk Moment | (256, 128) | Clown honk |
| Steam Hiss | (320, 128) | Pressure release |

### Disclaimer Subtexts (ported from legacy spec, 256x32 each):
| Sign | Size | Description |
|------|------|-------------|
| "NO REFUNDS EVER" | 256x32 | Aggressive policy |
| "CONSUME AT OWN RISK" | 256x32 | Liability waiver |

*Positions to be assigned within/appended to the sheet layout ("(Not Legally Binding)" already exists as glitch state 3 above).*

---

## 🎮 Sprite Sheet 7: UI Elements
**File:** `mystery_cart_ui.png`  
**Dimensions:** 384x256 pixels  

### Menu Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu Panel | (0, 0) | 256x192 | Shop interface |

### Status Icons (32x32 each):
| Icon | Position | Description |
|------|----------|-------------|
| Confused | (256, 0) | Swirling stars |
| Itchy | (288, 0) | Scratching |
| Sticky (Enemy) | (320, 0) | Goop effect |
| Digestive Daredevil | (256, 32) | Iron stomach |
| Chef Respect | (288, 32) | Clown approval |

### Special:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hallucination Overlay | (0, 192) | 256x64 | Distortion effect |

---

## 🎬 Animation Specifications

### Carousel Rotation:
- **Pattern:** Frame 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 (loop)
- **Duration:** 1 second per full rotation
- **FPS:** 8

### Knife Flipping:
- **Pattern:** Frame 1 → 2 → 3 → 4 → 5 → 6 (loop)
- **Cycle Duration:** 1.5 seconds
- **FPS:** 4
- **Purpose:** Continuous expert knife work

### Sign Glitching:
- **Pattern:** Main → Shady Dogs → Main → Meat Roulette → Main → Free Sample
- **Cycle Interval:** 60 seconds
- **Audio Sync:** Clown honk then steam hiss

### Strobe Cycling:
- **Pattern:** Red → Green → Purple (random)
- **Interval:** 0.1-0.2 seconds
- **Accessibility:** Full / Reduced / Disabled modes

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
- **Chef Chuckles Enhanced** - Higher contrast for visibility
- **Menu Items Readable** - Emphasized text and borders
- **Sign Text Emphasized** - Increased legibility

### Photosensitive Accommodations:
**CRITICAL FOR COMPLIANCE:**
- **Strobe Reduced Lighting** - Slowed flash rate (max 3 flashes/second)
- **Static Carnival Lights** - No flashing alternative mode
- **No Flash Mode Overlay** - Complete strobe disable option

All strobe effects must be **completely disableable** for photosensitive players per WCAG 2.1 guidelines.

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Honk Moment Visual | (256, 128) in `animated_signage_states.png` | 64x64 | Clown honk indicator for deaf/hard-of-hearing players |
| Steam Hiss Visual | (320, 128) in `animated_signage_states.png` | 64x64 | Pressure release indicator, audio-independent |
| Whisper Waves | (128, 96) in `mystery_menu_items_detailed.png` | 64x32 | Sausage whisper visualization — supernatural audio rendered visually |

### Colorblind Considerations:
- Status icons pair distinct shapes with color (swirling stars, scratch marks, goop) so no effect reads by hue alone
- "Enhanced" toxic-green food items double their color coding with the 50% opacity glow pulse
- Touch zones minimum 44px for menu buttons and cart interactions

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** PVRTC 4BPP for carnival textures, maintains color vibrancy
- **Android:** ETC2 with alpha for particle transparency support
- **Fallback:** PNG at high quality for character detail preservation

### Sprite Atlasing Strategy:
- **Character Atlas:** Chef Chuckles + Carousel Rotisserie combined (1024x1024)
- **Food Items Atlas:** All menu items + particle effects (512x512)
- **Environment Atlas:** Circus background + hazards combined (1024x768)
- **Max Atlas Size:** 2048x2048 for mobile GPU compatibility

### LOD (Level of Detail) Scaling:
- **High-End Devices:** Full particle systems, strobe effects, detailed animations
- **Medium Devices:** Reduced particle density, simplified lighting
- **Low-End Devices:** Minimal particles, static lighting, basic animations
- **Potato Mode:** Essential elements only, no effects

### Performance Targets:
- **Target FPS:** 60 fps on iPhone 8 baseline
- **Max Draw Calls:** 15 per frame
- **Memory Footprint:** 35MB maximum for location

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Animation system: Frame-based with JSON timing data
- Particle systems: Use Godot's CPUParticles2D for mobile performance

### Audio Sync Points:
- Butterfly knife flips sync with "whoosh" sound effects
- Carousel rotation requires continuous mechanical hum
- Sign glitches trigger electrical buzz at transition frames
- 60-second clown honk cycle must align with sign animation loop

### Cross-Location Integration:
- Chef Chuckles references other Cirque du Shady performers
- Menu items tie into "Great Döner Debate" quest system
- Clown gear visuals must match other circus vendor aesthetics
- Environmental details foreshadow "Carnival Carnage" secret quest

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Carnival grift meets dark web wet market"
- **Color Mood:** Toxic neon greens, danger crimsons, shadowy purples
- **Lighting:** Harsh carnival lights creating deep shadows and unease
- **Texture:** Greasy, sweaty, unsettlingly organic surfaces

### Chef Chuckles Character Direction:
- **Personality:** Deadpan menace disguised as carnival entertainment
- **Key Visual:** Cracked porcelain clown mask over muscular arms in sleeveless tuxedo
- **Movement:** Expert butterfly knife work, smooth and threatening
- **Expression:** Never breaks character, maintaining unsettling professionalism

### Food Design Philosophy:
- Each item must look simultaneously **appealing and horrifying**
- Obvious quality/safety issues presented as normal carnival fare
- Supernatural elements (whispers, glows) integrated naturally
- Players should feel both hungry and concerned

### Environmental Storytelling:
- Visible health code violations treated as atmospheric flavor
- Background suggests broader circus conspiracy
- Safety hazards ignored by desperate customers
- Costume economy hints at larger underground network

### Visual References to Capture Mood:
- Carnival horror aesthetic (Tim Burton, American Horror Story: Freak Show)
- Food truck culture (street vendor authenticity)
- Eastern European traveling circus atmosphere
- EarthBound's quirky enemy design philosophy

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Chef Chuckles** - Butterfly knife mastery in cracked mask
2. **Carousel Rotisserie** - Neon-lit spinning mystery meat
3. **Glitching Sign** - "Free Sample (Not Legally Binding)"
4. **Clown Dog Deluxe** - Red licorice bun horror
5. **Glizzénstein's Brain Brat** - AI sausage glow
6. **Violent Strobe** - Carnival light chaos

### Quote Potential:
- "Mystery meat builds character... and possibly tumors!"
- "Don't ask what's in it. Ask what's not in it. Then cry."
- "One bite and you'll see God. Or a god. Probably a meat one."
- "SHADE MEAT 4 CLOWN SOULS"
- "The sausage whispers? That's just... seasoning."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | chef_chuckles_mystery_cart_complete.png | 1024x768 |
| 2 | chef_chuckles_character_animations.png | 512x512 |
| 3 | mystery_menu_items_detailed.png | 1024x512 |
| 4 | circus_cart_environment_complete.png | 1024x768 |
| 5 | carnival_effects_particles.png | 512x256 |
| 6 | animated_signage_states.png | 512x256 |
| 7 | mystery_cart_ui.png | 384x256 |

**Total Estimated Memory:** ~10.5 MB uncompressed RGBA (well within the 35MB location budget)

---

## 📦 File Delivery Checklist

### Required PNG Files (7 Total):
- [ ] `chef_chuckles_mystery_cart_complete.png` (1024x768)
- [ ] `chef_chuckles_character_animations.png` (512x512)
- [ ] `mystery_menu_items_detailed.png` (1024x512)
- [ ] `circus_cart_environment_complete.png` (1024x768)
- [ ] `carnival_effects_particles.png` (512x256)
- [ ] `animated_signage_states.png` (512x256)
- [ ] `mystery_cart_ui.png` (384x256)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha |
| Color Space | sRGB |
| DPI | 72 |
| Naming | snake_case |

### Delivery Format (ported from legacy spec):
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/Photoshop files with organized layer groups
- **Documentation:** Layer naming guide for future updates

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 7 PNG files match exact dimension specifications *(legacy spec said 6 — BASE requires 7)*
- [ ] Sprite coordinates align with JSON mapping data
- [ ] Animation frame counts match technical requirements
- [ ] Color palette matches hex codes provided
- [ ] Accessibility alternatives included
- [ ] File naming follows snake_case convention
- [ ] Master source files preserved for future edits
- [ ] Test import in Godot to verify sprite alignment

### Quality Checkpoints:
- [ ] Chef Chuckles conveys "threatening carnival professional"
- [ ] Food items balance appealing and horrifying aesthetics
- [ ] Carousel rotisserie has clear mechanical animation flow
- [ ] Environment captures circus grift atmosphere
- [ ] Particle effects enhance without overwhelming scene
- [ ] Sign glitch transitions feel authentically broken
- [ ] All elements work together cohesively

**Once validated, assets are ready for Godot integration and the Mystery Meat Cart location is complete!**

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ PASS | Debaucheryville / Cirque du Shady only |
| Cultural Specificity | ✅ PASS | Eastern European traveling circus and carnival food grift |
| Satirical Targets Appropriate | ✅ PASS | Carnival grifters and daring tourists, not locals |
| Seedy Underbelly Present | ✅ PASS | Forbidden meats, no oversight, safety violations as flavor |
| Gameplay Value Established | ✅ PASS | Status effect gambles, Digestive Daredevil passive, Carnival Carnage access |
| Technical Feasibility | ✅ PASS | Mobile optimization documented |
| Mobile Performance Budget | ✅ PASS | 60 FPS, 15 draws, 35MB |
| Accessibility Features | ✅ PASS | Strobe disable option, visual audio cues |
| No Crypto Elements | ✅ PASS | None present |
| Social Media Integration | ✅ PASS | Six viral moments identified |

**The Mystery Meat Cart becomes the essential carnival grift station where Chef Chuckles delivers threatening food puns through a cracked clown mask, the carousel rotisserie spins mystery meats in toxic neon glow, sausages whisper dark secrets, and the Digestive Daredevil passive rewards those brave enough to consume three different items!**
