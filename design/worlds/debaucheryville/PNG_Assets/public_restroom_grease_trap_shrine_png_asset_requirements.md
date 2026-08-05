# Grease Trap Shrine - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Grease Trap Shrine restroom location. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this biohazard pilgrimage site.

**Location ID:** `debaucheryville_kebaballey_greasetrapshrine_restroom_01`
**Theme:** Urban legend meets gastrointestinal pilgrimage — a sacred biohazard shrine for worshippers of bad decisions, 4AM meat, and bodily resilience
**Zone:** Kebab Alley — behind the grease vendor tent
**Hours:** Crawlspace entrance accessible only at 3:00 AM game time (follow the glowing chili sauce trail)
**Primary Function:** Hidden exploration shrine — "Stomach of Steel" passive unlock, FistØ graffiti lore reads, "The Greasy Prophet" title progression, secret FistØ ICQ message

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Sickly Orange | #FF8C00 | Shrine light from repurposed "Open Late" sign, dominant interior glow |
| Grease Brown | #8B4513 | Wall coating, grease vapor, ambient grime surfaces |
| Oily Shimmer Gold | #FFD700 | Rainbow oil-slick highlights, legend-tier graffiti accents |
| Hot Pink Tag | #FF1493 | FistØ main graffiti spray paint |
| Neon Green Glow | #00FF00 | Hungover-only pixel kebab googly-eye glow |
| Chili Sauce Red | #FF4500 | 3AM discovery trail pulse, neon kebab signage bleed |
| Dark Slate Gray | #2F4F4F | Shadows, crawlspace darkness, fixture bases |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/kebab_alley/
├── grease_shrine_restroom_complete.png
├── fisto_graffiti_system.png
├── shrine_environmental_effects.png
└── crawlspace_access_system.png
```

---

## 🎨 Sprite Sheet 1: Grease Shrine Restroom Complete
**File:** `grease_shrine_restroom_complete.png`  
**Dimensions:** 512x512 pixels  
**Color Palette:** #FF8C00 (sickly orange), #8B4513 (grease brown), #FFD700 (oily shimmer), #2F4F4F (dark slate gray)

### Grease-Coated Walls (128x128 each):
1. **Normal Grease Coating** (0, 0) - Shimmer with airborne fat layer, rainbow oil-slick patterns
2. **Oily Reflection State** (128, 0) - Enhanced rainbow patterns, active reflection
3. **Player Movement Reflection** (256, 0) - Walls tracking player like oily shadows

### Toilet Area:
- **Toilet Base** (0, 128, 32x48) - Cramped mop closet size fixture
- **Receipt Toilet Paper 2004** (32, 128, 16x24) - Crumpled kebab receipt, still warm appearance
- **Mr. Chadz Receipt Detail** (48, 128, 32x16) - 20-year-old pricing visible, aged paper texture

### Sink Cursed Collection:
- **Sink Basin** (0, 176, 48x32) - Tiny restroom fixture, grease-stained porcelain
- **Cursed Coin** (48, 176, 8x8) - Unknown origin currency, mysterious glow
- **Half-Chewed Antacid** (56, 176, 8x8) - Gastrointestinal evidence, partially dissolved
- **Kebab Napkin Swan** (64, 176, 16x16) - Origami artistry, incongruous elegance

### Lighting Systems:
- **Sickly Orange Shrine Light** (384, 0, 64x32) - Repurposed "Open Late" sign backlight
- **Flickering Fluorescent** (384, 32, 32x64) - Dangling from ceiling, irregular pulse
- **Meat Skewer Mount** (416, 32, 16x32) - Skewer stabbed into ceiling tile
- **Neon Kebab Pulse** (432, 32, 48x24) - Bleeding through walls from outside

### Animation Notes:
- Wall reflections: Continuous oily shimmer, player movement tracking
- Fluorescent sway: 1.5-2 second irregular intervals
- Receipt paper: Subtle "warm" glow effect (freshly used appearance)
- Cursed items: Faint mystical aura on cursed coin

---

## 🖊️ Sprite Sheet 2: FistØ Graffiti System
**File:** `fisto_graffiti_system.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #FF1493 (hot pink tag), #00FF00 (neon green glow), #FFD700 (legend gold), #FFFFFF (white text)

### Main FistØ Graffiti:
1. **"Puked here in '99" Base** (0, 0, 128x64) - Legendary tag establishing origin story
2. **"Came back like it's Mecca"** (128, 0, 128x64) - Pilgrimage humor continuation
3. **FistØ Signature** (256, 0, 64x32) - Authentic travel legend mark

### Haiku Graffiti (Social Media Gold):
- **"Grease beneath my feet"** (0, 64, 96x16) - Line 1, 5 syllables, philosophical
- **"Secrets marinate in heat"** (96, 64, 96x16) - Line 2, 7 syllables, culinary mysticism
- **"I pray. Then I leak."** (192, 64, 96x16) - Line 3, 5 syllables, gastrointestinal honesty

### Pixel Kebab Googly Eyes (Hungover-Only):
- **Hungover Invisible** (0, 80, 32x32) - Completely hidden state
- **Hungover Visible Glow** (32, 80, 32x32) - Appears when player hungover, neon green
- **Eyes Follow Frame 1** (64, 80, 32x32) - Tracking animation start
- **Eyes Follow Frame 2** (96, 80, 32x32) - Tracking animation end (unsettling food surveillance)

### Eldritch Meat Glyphs:
- **Cryptic QR Codes** (288, 64, 64x64) - Scanning fails, deeper mystery suggested
- **Meat Glyph 1** (352, 64, 16x16) - Mystical sausage symbol
- **Meat Glyph 2** (368, 64, 16x16) - Sacred rotisserie pattern
- **Sheltie Paper Crown** (384, 64, 24x24) - FistØ inside joke, bizarre reference

### Text Specifications:
- FistØ main graffiti: Bold spray paint aesthetic with drips
- Haiku: Elegant handwriting, contrasts with crude surroundings
- Glyphs: Ancient mystical style meets meat vendor imagery

---

## 🌫️ Sprite Sheet 3: Shrine Environmental Effects
**File:** `shrine_environmental_effects.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #F0E68C (steam white-yellow), #8B4513 (grease brown), #FF4500 (chili sauce red), #98FB98 (cumin green fog)

### Steam Particles:
- **Fryer Vent Steam 1** (0, 0, 16x16) - External vent wisp variation 1
- **Fryer Vent Steam 2** (16, 0, 16x16) - Wisp variation 2
- **Fryer Vent Steam 3** (32, 0, 16x16) - Wisp variation 3
- **Grease Vapor Heavy** (48, 0, 12x12) - Oily particles from wall coating

### Cumin Despair Fog:
- **Fog Wisp 1** (0, 20, 20x20) - Atmospheric drift variation 1
- **Fog Wisp 2** (20, 20, 20x20) - Drift variation 2, spice-scented
- **Fog Wisp 3** (40, 20, 20x20) - Drift variation 3, despair aesthetic

### Chili Sauce Trail (3AM Access System):
- **Glowing Trail Segment** (0, 40, 8x8) - Discovery beacon base
- **Trail Glow Pulse 1** (8, 40, 8x8) - Animation frame 1, brightening
- **Trail Glow Pulse 2** (16, 40, 8x8) - Animation frame 2, peak brightness

### Grease Aura Effect:
- **Player Low Health Aura** (60, 0, 24x24) - Permanent shrine experience reminder
- **Grease Shimmer Effect** (84, 0, 16x16) - Stomach of Steel buff visualization

### Particle Emission Rates:
- **Steam:** 3 particles/second from fryer vents
- **Cumin Fog:** 2 particles/second, ambient layer
- **Chili Trail:** 1-second pulse cycle (3AM only)
- **Grease Aura:** Continuous when buff active or low health

---

## 🚪 Sprite Sheet 4: Crawlspace Access System
**File:** `crawlspace_access_system.png`  
**Dimensions:** 256x256 pixels  
**Color Palette:** #696969 (grease gray), #228B22 (vinyl tent green), #FF4500 (chili trail red), #000000 (crawlspace black)

### Vinyl Tent Flap (64x96 each):
1. **Closed Normal** (0, 0) - Standard grease-stained vinyl
2. **Grease Stained** (64, 0) - Heavy deterioration visible
3. **Partially Open** (128, 0) - Revealing crawlspace entrance

### Exterior Debris:
- **Empty Skewer Boxes** (0, 96, 32x24) - Stacked haphazardly nearby
- **Fly-Buzzing Barrels** (32, 96, 24x32) - Pickle barrels with visible flies
- **Pickle Barrel Flies** (56, 96, 8x8) - Animated insect swarm (health violations)

### Hand-Scrawled Signage:
- **"NOT TOILET Unless Desperate"** (0, 128, 96x24) - Crude handwriting, faded
- **Hand-Scrawled Text** (96, 128, 64x16) - Grease-stained, barely legible

### Crawlspace Entrance States:
- **3AM Invisible** (0, 152, 48x24) - Completely hidden during normal hours
- **3AM Visible Glow** (48, 152, 48x24) - Chili sauce trail reveals entrance
- **Player Crawling** (96, 152, 32x16) - Awkward entry animation sequence

### Animation Specifications:
- Tent flap: Gentle sway when partially open (0.5s intervals)
- Flies: 3-frame buzzing loop (0.2s per frame)
- Crawlspace glow: 1-second pulse cycle matching chili trail
- Player crawl: 1.5-second entrance sequence (uncomfortable squeezing)

---

## 📐 Performance & Assets Requirements

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) for grease effects, maintains oily shimmer with alpha for particle transparency
- **Fallback:** PNG at high quality for graffiti readability

### Sprite Atlasing Strategy:
- **Restroom Complete Atlas:** Walls + fixtures + lighting combined (512x512)
- **Graffiti System Atlas:** All FistØ content + haiku + glyphs (512x256)
- **Effects Particles Atlas:** Steam + fog + trail effects (512x256)
- **Crawlspace Access Atlas:** Entrance system + debris (256x256)
- **Max Atlas Size:** 1024x1024 for broad GPU compatibility

### LOD (Level of Detail) Scaling:
- **High-End Devices:** Full grease reflections, all particle effects, pixel kebab animation
- **Medium Devices:** Simplified reflections, reduced particle density, static kebab eyes
- **Low-End Devices:** Static grease coating, minimal particles, no reflection tracking
- **Potato Mode:** Essential graffiti only, no environmental effects, static lighting

### Performance Targets:
- **Target FPS:** 60 fps (small enclosed space optimization)
- **Max Draw Calls:** 8 per frame
- **Memory Footprint:** 20MB maximum for location

---

## ♿ Accessibility Sprite Requirements

### High Contrast Graffiti Alternatives:
- **FistØ Main Enhanced** (0, 208, 128x32) - Increased contrast for visibility
- **Haiku High Contrast** (128, 208, 96x32) - Enhanced text readability
- **Meat Glyphs Emphasized** (224, 208, 64x32) - Symbol clarity improved

### Visual Audio Cues:
- **Receipt Crinkle Visual** (0, 240, 16x16) - Toilet paper sound indicator
- **Shrine Reverence Visual** (16, 240, 24x16) - Buff activation notification
- **Steam Hiss Indicator** (40, 240, 12x16) - Environmental audio visualization

### Motion Sensitivity Options:
- **Static Grease Alternative** - No wall reflection movement
- **Reduced Flicker Lighting** - Gentler fluorescent pulse
- **Minimal Particle Mode** - Essential steam only, no fog

---

## 🎬 Animation Sequence Specifications

### Fluorescent Bulb Sway:
- **Duration:** 1.5-2 second irregular intervals
- **Pattern:** Electrical malfunction aesthetic
- **Audio Sync:** Buzzing sound on flicker frames
- **Purpose:** Atmospheric discomfort, unreliable lighting

### Pixel Kebab Eyes Follow:
- **Trigger:** Player has Hungover status only
- **Duration:** 2-second tracking cycle
- **Pattern:** Eyes follow player position (unsettling surveillance)
- **Purpose:** Food paranoia, absurdist humor callback

### Chili Sauce Trail Pulse:
- **Trigger:** 3AM game time only
- **Duration:** 1-second pulse cycle
- **Pattern:** Glow brightens → peak → dims (discovery beacon)
- **Purpose:** Hidden entrance guidance system

### Grease Wall Reflections:
- **Trigger:** Player movement tracking
- **Pattern:** Oily shadows follow character position
- **Visual:** Protective glaze reflecting movement
- **Purpose:** Environmental storytelling (shrine watches over visitors)

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Animation system: Frame-based with JSON timing data
- Particle systems: Use Godot's CPUParticles2D for performance

### Audio Sync Points:
- Fluorescent buzz syncs with flicker frames
- Receipt crinkle when examining toilet area
- Steam hiss continuous ambient with vent particle emission
- "Stomach of Steel" buff unlock has unique chime
- Crawlspace entrance triggers camera pan with echoing retches

### Quest Integration:
- **Stomach of Steel Passive:** Unlocks when eating kebab while reading graffiti
- **The Greasy Prophet Title:** Complete all graffiti reads while Hungover
- **FistØ ICQ Secret:** Absinthe + Grease Kebab + Reading graffiti combination
- **3AM Discovery:** Chili trail appears only at 3:00 AM game time

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Urban legend meets gastrointestinal pilgrimage"
- **Color Mood:** Sickly orange shrine glow, oily rainbow shimmer, grease-brown ambiance
- **Lighting:** Flickering fluorescent creating unstable shadows and sacred ambiance
- **Texture:** Everything coated in protective grease glaze, organic biohazard meets shrine

### FistØ Graffiti Direction:
- **Main Tags:** Bold spray paint with authentic travel legend aesthetic
- **Haiku:** Elegant handwriting contrasts with crude surroundings (social media gold)
- **Pixel Kebab:** Retro 8-bit style with unsettling googly eyes tracking
- **Glyphs:** Ancient mystical symbols merged with meat vendor imagery

### Environmental Storytelling:
- Grease as protective shrine coating (not just dirt)
- Receipt toilet paper suggests time dilation (2004 but still warm)
- Cursed coin + antacid + napkin swan = pilgrimage offerings
- 3AM access reinforces urban legend mystery
- FistØ's return pilgrimage establishes sacred site status

---

## 📋 Required PNG Files (4 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | grease_shrine_restroom_complete.png | 512x512 |
| 2 | fisto_graffiti_system.png | 512x256 |
| 3 | shrine_environmental_effects.png | 512x256 |
| 4 | crawlspace_access_system.png | 256x256 |

**Total Estimated Memory:** ~2.4 MB uncompressed RGBA (comfortably within the 20MB location footprint)

---

## 📦 File Delivery Checklist

### Required PNG Files (4 Total):
- [ ] `grease_shrine_restroom_complete.png` (512x512)
- [ ] `fisto_graffiti_system.png` (512x256)
- [ ] `shrine_environmental_effects.png` (512x256)
- [ ] `crawlspace_access_system.png` (256x256)

### Quality Requirements:
- **Format:** PNG-24 with alpha channel
- **Color Space:** sRGB
- **DPI:** 72 (screen resolution)
- **Compression:** Lossless PNG compression
- **Naming Convention:** snake_case, all lowercase
- **Layer Organization:** Preserve for future graffiti updates

### Delivery Format:
- **Primary:** Individual PNG files per specifications
- **Backup:** Master PSD/Photoshop files with organized layers
- **Documentation:** Graffiti text layer guide for localization

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Haiku Discovery** - "Grease beneath my feet / Secrets marinate in heat / I pray. Then I leak." (instant meme format)
2. **FistØ Pilgrimage Tag** - "Puked here in '99. Came back like it's Mecca." (travel legend humor)
3. **Pixel Kebab Eyes** - Googly-eyed food surveillance while hungover (absurdist perfection)
4. **3AM Discovery** - Chili sauce trail revealing hidden shrine (urban legend mystery)
5. **Stomach of Steel Unlock** - Eating kebab while reading graffiti (ritual completion)

### TikTok Potential:
- "POV: You found the legendary grease shrine at 3AM"
- "Reading FistØ's haiku while my character is dying"
- "The kebab is watching me and I don't like it"
- "When the toilet paper is a 20-year-old receipt"

### Twitter/X Quote Potential:
- Every line of the haiku is quotable life advice
- FistØ's Mecca comparison for any bad decision revisited
- "Stomach of Steel" as metaphor for surviving anything

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 4 PNG files match exact dimension specifications
- [ ] Graffiti text is pixel-perfect and readable at target resolution
- [ ] Grease reflection effects capture oily shimmer aesthetic
- [ ] Pixel kebab eyes properly track in both animation frames
- [ ] Chili sauce trail pulse cycle is clear discovery beacon
- [ ] 3AM crawlspace entrance visibility states work correctly
- [ ] Color palette matches hex codes provided
- [ ] Accessibility alternatives included for all key elements
- [ ] File naming follows snake_case convention
- [ ] Master source files preserved for localization updates

### Quality Checkpoints:
- [ ] FistØ graffiti captures legendary travel pilgrim aesthetic
- [ ] Haiku text creates instant social media quotability
- [ ] Grease walls feel like protective shrine coating (not just dirt)
- [ ] Receipt toilet paper conveys time dilation weirdness
- [ ] Cursed sink items suggest pilgrimage offerings
- [ ] 3AM discovery reinforces urban legend status
- [ ] Environmental effects enhance biohazard-meets-sacred ambiance
- [ ] All elements work together for gastrointestinal pilgrimage theme

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Debaucheryville — Kebab Alley only |
| Cultural Specificity | ✅ | European late-night kebab/street-food culture and backpacker travel-legend lore |
| Satirical Targets Appropriate | ✅ | Drunk pilgrim tourists worshipping FistØ's bad decisions — not vendors or locals |
| Seedy Underbelly Present | ✅ | Biohazard restroom shrine, health-violation grease vendor alley, fly-buzzing pickle barrels |
| Gameplay Value Established | ✅ | Stomach of Steel passive, Greasy Prophet title, FistØ ICQ secret, 3AM discovery mechanic |
| Technical Feasibility | ✅ | 4 sprite atlases, LOD tiers down to Potato Mode, CPUParticles2D particles |
| Performance Budget | ✅ | 60 FPS target, max 8 draw calls, 20MB memory footprint |
| Accessibility Features | ✅ | Visual audio cues (receipt crinkle, steam hiss, shrine reverence), high-contrast graffiti, motion sensitivity options |
| No Crypto Elements | ✅ | None present — cryptic QR codes are eldritch mystery, not crypto |
| Social Media Integration | ✅ | Haiku meme format, FistØ pilgrimage tag, TikTok POV hooks identified |

**Once validated, the Grease Trap Shrine becomes the most quotable, screenshot-worthy location in Eurobound - where players complete a gross-out ritual to unlock legendary buffs while documenting their pilgrimage for social media immortality!**