# Mystery Meat Cart - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Mystery Meat Cart location. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements.

---

## 🎨 Sprite Sheet 1: Chef Chuckles Character
**File:** `chef_chuckles_complete.png`  
**Dimensions:** 512x384 pixels  
**Color Palette:** #DC143C (crimson), #39FF14 (neon green), #FFFFFF (porcelain white), #000000 (sleeveless tuxedo)

### Character States (64x96 each):
1. **Idle Menacing** (0, 0) - Default threatening pose, cracked porcelain mask visible
2. **Butterfly Knife Flip 1** (64, 0) - First frame of expert knife work
3. **Butterfly Knife Flip 2** (128, 0) - Mid-flip, blade blur effect
4. **Butterfly Knife Flip 3** (192, 0) - Final flip, sausage being prepped
5. **Serving Threatening** (256, 0) - Handing food with deadpan menace
6. **Cracked Mask Close-Up** (320, 0) - Unsettling detail reveal
7. **Sleeveless Tuxedo Full** (384, 0) - Full costume display

### Costume Detail Elements:
- **Cracked Porcelain Mask** (0, 96, 32x32) - Web of cracks, dead-eyed expression
- **Sleeveless Tuxedo Detail** (32, 96, 48x64) - Formal vest with exposed muscular arms
- **Butterfly Knife Held** (80, 96, 24x48) - Weapon in various positions

### Animation Notes:
- Knife flip loop: 0.2s per frame, continuous during service
- Menacing idle: 2s base pose, 0.5s mask close-up with audio trigger
- All animations must convey "carnival entertainment facade hiding obvious threat"

---

## 🎪 Sprite Sheet 2: Carousel Rotisserie System
**File:** `carousel_rotisserie_complete.png`  
**Dimensions:** 512x384 pixels  
**Color Palette:** #DC143C (neon crimson), #FFD700 (carnival gold), #8B4513 (mystery meat brown)

### Rotisserie Core Elements:
1. **Carousel Base Structure** (0, 0, 128x128) - Spinning platform with carnival aesthetic
2. **Rotating Meat Heap Frame 1** (128, 0, 96x96) - Starting rotation position
3. **Rotating Meat Heap Frame 2** (224, 0, 96x96) - 90° rotation
4. **Rotating Meat Heap Frame 3** (320, 0, 96x96) - 180° rotation
5. **Rotating Meat Heap Frame 4** (416, 0, 96x96) - 270° rotation

### Steam & Grease Effects:
- **Steam Vent Top** (0, 128, 32x32) - Primary emission point
- **Steam Vent Sides** (32, 128, 32x32) - Secondary vents
- **Grease Drip Bottom** (64, 128, 32x32) - Drip tray overflow

### Neon Lighting Effects:
- **Carousel Lights On** (0, 160, 128x64) - Full brightness carnival glow
- **Carousel Lights Flicker** (128, 160, 128x64) - Electrical malfunction state
- **Carnival Glow Overlay** (256, 160, 128x64) - Atmospheric wash effect

### Technical Specs:
- Rotation: 2 RPM continuous (30 frames per rotation at 60fps)
- Steam emission: Every 0.8 seconds
- Grease drip: Every 3 seconds with spatter particles

---

## 🍖 Sprite Sheet 3: Mystery Menu Items
**File:** `mystery_menu_items_detailed.png`  
**Dimensions:** 1024x512 pixels  
**Item Size:** 64x64 pixels each

### 1. Döner of Illusions™ (Row 1: Y=0)
- **Spinning Meat Heap** (0, 0) - Rotating doner with questionable layers
- **Gummy Bears Mixed In** (64, 0) - Colorful candy corruption visible
- **Absinthe Glaze Shimmer** (128, 0) - Green iridescent coating
- **Serving Wrapped** (192, 0) - Final presentation in greasy paper

### 2. Sausage of Suspicion (Row 2: Y=64)
- **Grey Sweaty Tube Meat** (0, 64) - Unnaturally moist appearance
- **Wooden Stick Presentation** (64, 64) - On carnival stick
- **Whisper Audio Waves** (128, 64) - Supernatural visual effect (particle overlay)
- **Suspicious From All Angles** (192, 64) - Rotated view showing concerns

### 3. Clown Dog Deluxe™ (Row 3: Y=128)
- **Red Licorice Bun** (0, 128) - Candy bread substitute
- **Mustard Smiley Face** (64, 128) - Disturbing condiment pattern
- **Pop Rocks Relish** (128, 128) - Crackling topping effect
- **Assembled Grotesque** (192, 128) - Complete horrific creation

### 4. Meatball on Lollipop Stick (Row 4: Y=192)
- **Spherical Mystery Meat** (0, 192) - Round processed meat product
- **Candy Stick Inappropriate** (64, 192) - Child-targeted presentation
- **Structural Impossibility** (128, 192) - Defying physics display
- **Previous Bite Marks** (192, 192) - Evidence of prior consumption

### 5. Glizzénstein's Brain Brat (Row 5: Y=256)
- **Glowing Internal AI** (0, 256) - Pulsing circuit interior
- **Circuit Pattern Surface** (64, 256) - Tech-meat hybrid texture
- **Organic Digital Mix** (128, 256) - Grotesque fusion aesthetic
- **Pulsing Glow Packaging** (192, 256) - Active energy effect

### Color Requirements:
- Use sickly greens (#39FF14) for "enhanced" items
- Meat browns range: #8B4513 (saddle brown) to #696969 (dim gray)
- Glow effects: #00FF00 (lime) with 50% opacity pulse

---

## 🎪 Sprite Sheet 4: Circus Cart Environment
**File:** `circus_cart_environment_complete.png`  
**Dimensions:** 1024x768 pixels  
**Color Palette:** #4B0082 (indigo night), #DC143C (danger crimson), #FFD700 (carnival gold)

### Background Context Elements:
#### Ringmaster Tent Corner (Top Row: Y=0, Height=96):
- **Tent Corner Visible** (0, 0, 128x96) - Partial circus tent in background
- **Circus Entrance Context** (128, 0, 128x96) - Entry point reference
- **Performer Network Hints** (256, 0, 128x96) - Other circus staff silhouettes

#### Carnival Chaos Background (Row 2: Y=96, Height=64):
- **Distressed Family Silhouettes** (0, 96, 96x64) - Tourists in distress
- **Other Circus Performers** (96, 96, 128x64) - Supporting cast atmosphere
- **Carnival Game Audio Waves** (224, 96, 64x64) - Sound effect visualization
- **Safety Violation Evidence** (288, 96, 96x64) - Obvious hazards ignored

### Environmental Hazards (Row 3: Y=160, Height=48):
- **Electrical Issues Sparking** (0, 160, 64x48) - Dangerous wiring
- **Sanitation Nightmares** (64, 160, 96x48) - Health code violations
- **Structural Concerns** (160, 160, 64x48) - Cart stability issues
- **No Authority Figures** (224, 160, 96x48) - Complete lack of oversight

### Atmosphere Particles (Row 4: Y=208, Height=32):
- **Steam from Cooking** (0, 208, 48x32) - Food prep vapor
- **Grease Vapor Rising** (48, 208, 48x32) - Oil smoke
- **Carnival Dust/Sawdust** (96, 208, 48x32) - Floating debris
- **Mystery Substance Particles** (144, 208, 48x32) - Unidentifiable mist

---

## 🎆 Sprite Sheet 5: Carnival Effects & Particles
**File:** `carnival_effects_particles.png`  
**Dimensions:** 512x256 pixels  
**Particle Emission Rates:** See technical specs below

### Steam Systems (Row 1: Y=0, 16x16 each):
- **Cooking Steam Wisp 1-4** (0-48, 0) - Continuous emission loop

### Grease Effects (Row 2: Y=16):
- **Grease Spatter Small** (0, 16, 8x8) - Minor splashes
- **Grease Spatter Medium** (8, 16, 12x12) - Moderate splashes
- **Grease Spatter Large** (20, 16, 16x16) - Major splashes
- **Grease Drip Animation** (36, 16, 8x24) - Falling droplet sequence

### Carnival Lights (Row 3: Y=40, 32x32 each):
- **Light Burst 1** (0, 40) - Flash frame 1
- **Light Burst 2** (32, 40) - Flash frame 2
- **Strobe Flash** (64, 40) - High-intensity flicker
- **Neon Glow Pulse** (96, 40) - Ambient carnival wash

### Mystery Vapor (Row 4: Y=72, 24x24 each):
- **Suspicious Mist 1-3** (0-48, 72) - Hallucinogenic fog loop
- **Hallucinogenic Shimmer** (72, 72) - Psychedelic distortion effect

### Particle Emission Technical Specs:
- **Steam:** 5 particles/second, continuous
- **Grease:** 2 particles/second, sporadic bursts
- **Carnival Lights:** 12 flashes/second during strobe
- **Mystery Vapor:** 3 particles/second, ambient layer

### Accessibility Note:
**CRITICAL:** All strobe effects must have reduced-motion alternatives in accessibility sprites section

---

## 🪧 Sprite Sheet 6: Animated Signage System
**File:** `mystery_cart_signs_animated.png`  
**Dimensions:** 768x256 pixels  
**Color Palette:** #39FF14 (toxic green), #FF1493 (hot pink), #FFD700 (warning yellow)

### Main Sign States (256x64 each):
1. **"SHADY DOGS" Display** (0, 0) - First rotation frame
2. **"MEAT ROULETTE" Display** (256, 0) - Second rotation frame
3. **"FREE SAMPLE" Display** (512, 0) - Third rotation frame (with asterisk)

### Glitch Transition Frames (256x64 each):
- **Glitch Transition 1** (0, 64) - Electrical malfunction effect
- **Glitch Transition 2** (256, 64) - Data corruption aesthetic
- **Glitch Transition 3** (512, 64) - Reality breakdown visual

### Disclaimer Subtexts (256x32 each, Row 3: Y=128):
- **"(Not Legally Binding)"** (0, 128) - Fine print warning
- **"NO REFUNDS EVER"** (256, 128) - Aggressive policy
- **"CONSUME AT OWN RISK"** (512, 128) - Liability waiver

### Animation Cycle:
1. "SHADY DOGS" - 3 seconds
2. Glitch 1 - 0.1 seconds
3. "MEAT ROULETTE" - 3 seconds
4. Glitch 2 - 0.1 seconds
5. "FREE SAMPLE" - 3 seconds + audio cue: "not_legally_binding_whisper"
6. Glitch 3 - 0.1 seconds
7. Loop

### Audio Integration:
- **60-Second Cycle:** Squeaky clown honk + steam hiss (every 60 seconds)
- **Sign Glitch Sound:** Electrical malfunction buzz (during transitions)
- **Whisper Effect:** Sinister "not legally binding" voiceover

---

## 📐 Mobile Optimization Requirements

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

---

## 📦 File Delivery Checklist

### Required PNG Files (6 Total):
- [ ] `chef_chuckles_complete.png` (512x384)
- [ ] `carousel_rotisserie_complete.png` (512x384)
- [ ] `mystery_menu_items_detailed.png` (1024x512)
- [ ] `circus_cart_environment_complete.png` (1024x768)
- [ ] `carnival_effects_particles.png` (512x256)
- [ ] `mystery_cart_signs_animated.png` (768x256)

### Quality Requirements:
- **Format:** PNG-24 with alpha channel
- **Color Space:** sRGB
- **DPI:** 72 (screen resolution)
- **Compression:** Lossless PNG compression
- **Naming Convention:** snake_case, all lowercase
- **Layer Organization:** Preserve layer structure for future edits

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/Photoshop files with organized layer groups
- **Documentation:** Layer naming guide for future updates

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

## 📞 Artist Support & Questions

**For clarification on any specifications, reference:**
- JSON sprite mapping file: `debaucheryville_sprite_mapping.json`
- Character profile: Chef Chuckles detailed personality and mechanics
- Location design doc: Mystery Meat Cart satirical concept

**Visual references to capture mood:**
- Carnival horror aesthetic (Tim Burton, American Horror Story: Freak Show)
- Food truck culture (street vendor authenticity)
- Eastern European traveling circus atmosphere
- EarthBound's quirky enemy design philosophy

**The goal:** Create a location so visually memorable that players screenshot it constantly for social media, while maintaining the satirical edge that makes Eurobound unique.

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 6 PNG files match exact dimension specifications
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