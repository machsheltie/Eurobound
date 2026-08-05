# Absinthe Arcade - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Absinthe Arcade location. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this psychedelic corrupted barcade where childhood nostalgia meets bad trip aesthetics.

**Location ID:** `debaucheryville_clocktower_arcade_01`  
**Theme:** Dave & Buster's if it was haunted by your bad trip  
**Zone:** Clocktower Plaza (side street beneath a green-lit arch)  
**Hours:** Always accessible; lighting effects change dramatically after 10 PM  
**Primary Function:** NFT Hunt location, Brewery Tour entrance, Couchsurfing host, Parody arcade minigames

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Toxic Green | #39FF14 | Dominant glow — floor tiles, screen glow, absinthe bar, mist |
| UV Fairy Green | #00FF41 | UV reactive surfaces, Green Fairy mural form |
| Neon Purple | #BF00FF | Accent elements, circuit corruption patterns |
| Deep Black | #0A0A0A | Background voids, ceiling, unlit surfaces |
| Cabinet Pink | #FF1493 | Arcade cabinet bodies |
| Neon Pink | #FF69B4 | Environmental neon accents |
| Cyan | #00FFFF | Cabinet screens, mist tint, glitch artifacts |
| Cabinet Wood Grain | #8B4513 | Cabinet trim, worn wood surfaces |
| Token Gold | #FFD700 | Tokens, exchange machine highlights |
| Spark Yellow | #FFFF00 | Electrical spark tint |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/absinthe_arcade/
├── environment/
│   ├── absinthe_arcade_tileset.png
│   └── green_fairy_mural_parallax.png
├── objects/
│   └── arcade_machines_spritesheet.png
└── effects/
    └── environmental_effects.png
```

---

## 🎨 Sprite Sheet 1: Absinthe Arcade Tileset
**File:** `absinthe_arcade_tileset.png`  
**Dimensions:** 1024x1024 pixels  
**Color Palette:** #39FF14 (toxic green), #BF00FF (neon purple), #0A0A0A (deep black), #00FF41 (UV reactive green)

### Floor Tiles (32x32 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Standard Floor | (0, 0) | 32x32 | Base tile, dark with subtle texture |
| Light-Up Tile Off | (32, 0) | 32x32 | Inactive state, dim surface |
| Light-Up Tile Frame 1 | (64, 0) | 32x32 | Dim glow beginning |
| Light-Up Tile Frame 2 | (96, 0) | 32x32 | Medium brightness |
| Light-Up Tile Frame 3 | (128, 0) | 32x32 | Peak brightness, full toxic green |
| Light-Up Tile Flicker | (160, 0) | 32x32 | Malfunction state, erratic glow |
| Cracked Floor Variation 1 | (192, 0) | 32x32 | Visible damage, minor cracks |
| Cracked Floor Variation 2 | (224, 0) | 32x32 | Heavy wear, deep cracks |
| Green Glow Floor | (256, 0) | 32x32 | UV reactive permanent glow tile |

### Wall Tiles (64x64 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Blacklight Wall Base | (0, 32) | 64x64 | Standard blacklight wash surface |
| Mirror Wall Normal | (64, 32) | 64x64 | Reflective surface, clean |
| Mirror Wall Lagged | (128, 32) | 64x64 | 0.2s reflection delay state visual |
| Cracked Wall Light | (192, 32) | 64x64 | Minor structural damage |
| Cracked Wall Heavy | (256, 32) | 64x64 | Significant arcade decay |
| Circuit Pattern Wall | (320, 32) | 64x64 | Green Fairy mural integration pattern |

### Ceiling Tiles (48x48 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Standard Ceiling | (0, 96) | 48x48 | Dark overhead surface |
| Exposed Wiring | (48, 96) | 48x48 | Electrical hazard visible |
| Flickering Light Source | (96, 96) | 48x48 | Unstable illumination fixture |
| Green Glow Wash | (144, 96) | 48x48 | Toxic atmospheric tint overlay |

### Green Glow Overlay Effects (128x128 each):
| Effect Name | Position | Size | Description |
|-------------|----------|------|-------------|
| Subtle Glow | (384, 0) | 128x128 | Gentle toxic green wash |
| Medium Intensity | (512, 0) | 128x128 | Standard arcade glow level |
| Peak Intensity | (640, 0) | 128x128 | Overwhelming green effect |
| Pulsing Animation Frame 1 | (768, 0) | 128x128 | Breathing effect start |
| Pulsing Animation Frame 2 | (896, 0) | 128x128 | Breathing effect peak |

### Technical Notes - Tileset:
- Floor tiles use random activation pattern (0.5-3 second delays between tiles)
- Approximately 20% of light-up tiles active at any given time
- Mirror lag effect: 0.2-second delay on player reflection requires shader support
- Green glow overlays use additive blend mode for proper layering
- UV reactive materials respond to blacklight ambient lighting

---

## 🕹️ Sprite Sheet 2: Arcade Machines Spritesheet
**File:** `arcade_machines_spritesheet.png`  
**Dimensions:** 2048x1024 pixels  
**Color Palette:** #39FF14 (screen glow), #FF1493 (cabinet pink), #00FFFF (cyan screens), #8B4513 (cabinet wood grain)

### Frogger: Existential Edition Cabinet (128x192):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Idle State | (0, 0) | 128x192 | Standard cabinet with philosophical title |
| Active Playing | (128, 0) | 128x192 | Screen lit, existential obstacles visible |
| Broken Leaking Mist | (256, 0) | 128x192 | Cracked cabinet with green fog emission |
| Screen Content Frame 1 | (384, 0) | 64x48 | Philosophical obstacles on screen |
| Screen Content Frame 2 | (448, 0) | 64x48 | Existential traffic hazards |
| Screen Content Frame 3 | (512, 0) | 64x48 | Life questions as game obstacles |

### Street Fighter: Identity Crisis Cabinet (128x192):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Idle State | (0, 192) | 128x192 | Cabinet with identity confusion theme |
| Active Mid-Combo | (128, 192) | 128x192 | Characters questioning their moves |
| Broken State | (256, 192) | 128x192 | Damaged, identity completely lost |
| Screen Identity Question 1 | (384, 192) | 64x48 | "Who am I hitting?" text |
| Screen Identity Question 2 | (448, 192) | 64x48 | Character self-doubt animation |
| Screen Identity Question 3 | (512, 192) | 64x48 | Move confusion visual |

### Kebab Kombat Cabinet (128x192):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Idle State | (0, 384) | 128x192 | Fighting game aesthetic cabinet |
| Active Regret Button | (128, 384) | 128x192 | Single REGRET button glowing |
| Broken State | (256, 384) | 128x192 | Leaking mystery meat vapor |
| Regret Button Glow Dim | (384, 384) | 64x64 | Button in dim state |
| Regret Button Glow Bright | (448, 384) | 64x64 | Button at peak brightness |
| Regret Button Pressed | (512, 384) | 64x64 | Active press state, depressed |

### Rigged Absinthe Arcade Claw Machine (256x384):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Idle Operating | (576, 0) | 256x384 | Standard claw machine front view |
| Claw Moving | (832, 0) | 256x384 | Rigged physics in action |
| Dispensing NFT | (1088, 0) | 256x384 | Beer Pong Saint Relic dropping |
| NFT Prize Inside | (576, 384) | 64x64 | 8-bit halo red solo cup visible |
| Claw Mechanism Open | (640, 384) | 48x64 | Claw in open position |
| Claw Mechanism Closing | (688, 384) | 48x64 | Claw closing on prize |
| Rigged Physics Visual | (736, 384) | 96x96 | Obviously unfair grab animation |

### Broken DDR Machine (192x256):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Cabinet Base | (1344, 0) | 192x256 | Dance Dance Revolution full setup |
| Broken Pad | (1536, 0) | 96x128 | Non-functional dance surface |
| Token Slot | (1632, 0) | 64x96 | 3-token unlock mechanism slot |
| Token Insert 1/3 | (1696, 0) | 64x32 | First token progress indicator |
| Token Insert 2/3 | (1760, 0) | 64x32 | Second token progress indicator |
| Token Insert 3/3 | (1824, 0) | 64x32 | Third token, unlock complete glow |

### Cracked Time Crisis Machine - Hidden Entrance (192x256):
| State/Element | Position | Size | Description |
|---------------|----------|------|-------------|
| Cabinet Closed | (1344, 256) | 192x256 | Normal damaged cabinet, concealing passage |
| Cabinet Opening | (1536, 256) | 192x256 | Swinging aside, revealing passage |
| Hidden Passage Visible | (1728, 256) | 192x256 | Absinthium Taproom access revealed |
| Secret Entrance Glow | (1920, 256) | 64x96 | Discovery indicator green glow |

### Universal Cabinet Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Green Mist Particle | (1920, 352) | 32x32 | Leaking from damaged machines |
| Electrical Spark | (1952, 352) | 24x24 | Random cabinet malfunction spark |
| Screen Flicker Effect | (1976, 352) | 48x48 | 2-second interval glitch overlay |

### Technical Notes - Arcade Machines:
- All cabinets designed for front-facing oblique EarthBound perspective
- Screen content loops independently from cabinet state
- Claw machine physics deliberately shows unfairness for comedy
- Green mist particles spawn from seams of "broken" cabinets
- DDR token slot should show visible progress with each token inserted

---

## 🧚 Sprite Sheet 3: Green Fairy Mural Parallax
**File:** `green_fairy_mural_parallax.png`  
**Dimensions:** 1024x512 pixels  
**Color Palette:** #00FF41 (fairy green), #BF00FF (circuit purple), #39FF14 (toxic glow), #0A0A0A (background black)

### Layer 1 - Circuit Board Background (Furthest - 0.1x scroll):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Circuit Pattern Base | (0, 0) | 512x256 | Deep background technology pattern |
| Circuit Glow Points | (512, 0) | 512x256 | Pulsing connection nodes overlay |

### Layer 2 - Fairy Silhouette (Middle-Far - 0.3x scroll):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fairy Form Solid | (0, 256) | 256x256 | Green Fairy iconic shape, intact |
| Fairy Form Dissolving | (256, 256) | 256x256 | Beginning melt/corruption effect |
| Fairy Form Melted | (512, 256) | 256x256 | Heavy digital corruption state |

### Layer 3 - Melting Effect (Middle-Near - 0.5x scroll):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Drip Frame 1 | (768, 0) | 256x128 | Initial melt, drips forming |
| Drip Frame 2 | (768, 128) | 256x128 | Progressive melting |
| Drip Frame 3 | (768, 256) | 256x128 | Advanced decay state |
| Drip Frame 4 | (768, 384) | 256x128 | Near-complete melt |

### Layer 4 - Circuit Overlay (Nearest - 0.7x scroll):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Circuit Overlay Active | (0, 512) | 512x256 | Foreground tech corruption lines |
| Circuit Overlay Pulsing 1 | (512, 512) | 256x128 | Pulse animation frame 1 |
| Circuit Overlay Pulsing 2 | (768, 512) | 256x128 | Pulse animation frame 2, peak |

### Parallax Movement Specifications:
| Layer | Scroll Speed | Purpose |
|-------|--------------|---------|
| Layer 1 (Circuit Background) | 0.1x player speed | Deep background, barely moves |
| Layer 2 (Fairy Silhouette) | 0.3x player speed | Mid-ground focal point |
| Layer 3 (Melting Effect) | 0.5x player speed | Near-ground dynamic element |
| Layer 4 (Circuit Overlay) | 0.7x player speed | Foreground framing |

### Animation Timing:
| Animation | Frames | FPS | Duration | Loop |
|-----------|--------|-----|----------|------|
| Melting Effect | 4 | 1.33 | 3 seconds | Yes |
| Circuit Pulse | 2 | 1.33 | 1.5 seconds | Yes |
| Fairy Dissolve | 3 | 0.5 | 6 seconds | Yes (gradual) |

### Technical Notes - Parallax:
- Use ParallaxBackground node in Godot 4.x
- Each layer should be separate texture for proper scroll
- Fairy dissolve is gradual transformation, not abrupt switch
- Circuit overlay uses additive blend for glow effect
- Mobile: Can reduce to 2 layers on low-end devices

---

## 🍾 Sprite Sheet 4: Environmental Effects
**File:** `environmental_effects.png`  
**Dimensions:** 1024x512 pixels  
**Color Palette:** #39FF14 (absinthe glow), #FF69B4 (neon pink), #00FFFF (cyan mist), #FFD700 (token gold)

### Absinthe Bottle Bar System:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bottle Bar Base | (0, 0) | 256x128 | Cracked bottle shape structure |
| Glow Animation Frame 1 | (256, 0) | 256x128 | Dim internal glow |
| Glow Animation Frame 2 | (512, 0) | 256x128 | Medium brightness |
| Glow Animation Frame 3 | (768, 0) | 256x128 | Peak toxic green intensity |
| Glow Animation Frame 4 | (0, 128) | 256x128 | Pulsing descent |

**Bar Glow Animation:** 4-frame pulse, 3 seconds total, continuous loop

### Mismatched Bar Seating:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Highchair Seat | (256, 128) | 64x96 | Absurdly inappropriate child's highchair |
| Beanbag Seat | (320, 128) | 64x64 | Collapsed gaming furniture, deflated |
| Bidet Seat | (384, 128) | 64x96 | The infamous bathroom fixture stool |
| Normal Stool | (448, 128) | 48x72 | Only one "normal" option, ironic |

### Token Exchange Machine:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Machine Idle | (0, 224) | 128x192 | Ready for overpriced exchange |
| Machine Active | (128, 224) | 128x192 | Processing transaction animation |
| Machine Dispensing | (256, 224) | 128x192 | Tokens falling out animation |
| Screen Display (1KC=5T) | (384, 224) | 96x48 | Overpriced conversion rate visible |
| Token Slot Detail | (480, 224) | 48x64 | Kebab coin insertion point |

### Particle Systems:

#### Green Mist (From Cabinets):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mist Wisp 1 | (0, 416) | 32x32 | Light fog particle, translucent |
| Mist Wisp 2 | (32, 416) | 32x32 | Medium density wisp |
| Mist Wisp 3 | (64, 416) | 32x32 | Dense fog particle |
| Mist Wisp 4 | (96, 416) | 32x32 | Dissipating wisp |

**Mist Animation:** 4 frames, 0.3s per frame, additive blend, upward drift

#### Electrical Sparks:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Spark Frame 1 | (128, 416) | 16x16 | Initial spark burst |
| Spark Frame 2 | (144, 416) | 16x16 | Peak brightness |
| Spark Frame 3 | (160, 416) | 16x16 | Fading arc |

**Spark Animation:** 3 frames, 0.1s per frame, yellow #FFFF00 tint

#### Digital Artifacts:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Glitch Fragment 1 | (176, 416) | 24x24 | Cyan pixelated fragment |
| Glitch Fragment 2 | (200, 416) | 24x24 | Magenta glitch piece |
| Glitch Fragment 3 | (224, 416) | 24x24 | Yellow digital debris |
| Screen Tear Effect | (272, 416) | 48x32 | Visual distortion |

**Glitch Animation:** 3 frames, 0.4s per frame, random drift movement

### Particle Emission Rates:
- **Green Mist:** 3 particles/second from damaged cabinets
- **Electrical Sparks:** Random 1-4 second intervals
- **Digital Artifacts:** Continuous low-density atmospheric effect

### UI Elements (Location-Specific):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Token Counter Background | (0, 448) | 128x32 | HUD element for token count |
| Token Icon | (128, 448) | 16x16 | Single token sprite for counter |
| Score Display | (0, 480) | 96x24 | Arcade game score readout |
| Game Over Overlay | (96, 480) | 128x32 | Failure state overlay |
| Examine Prompt | (224, 480) | 64x24 | "Examine" interaction button |
| Play Prompt | (288, 480) | 64x24 | "Play" interaction button |
| Insert Token Prompt | (352, 480) | 96x24 | "Insert Token" prompt |

---

## 🎬 Animation Specifications

### Floor Tile Random Activation:
- **Duration:** Random 0.5-3 second delays per tile
- **Pattern:** Off → Dim (Frame 1) → Medium (Frame 2) → Bright (Frame 3) → Medium → Dim → Off
- **Coverage:** Approximately 20% of tiles active at any time
- **Purpose:** Disorienting atmosphere, creates "something's wrong" feeling
- **Performance Optimization:** Reduce active percentage to 10% on low-end devices

### Arcade Cabinet Screen Flicker:
- **Duration:** 2-second intervals between flicker events
- **Pattern:** Normal display → Glitch artifacts → Brief static → Return to normal
- **Consistency:** All cabinets flicker independently (random offset)
- **Purpose:** Arcade decay aesthetic, corrupted nostalgia theme
- **Audio Sync:** Brief analog distortion sound accompanies each flicker

### Green Fairy Mural Melting:
- **Duration:** 6-second gradual transformation cycle
- **Pattern:** Solid fairy → Dissolving edges → Circuit corruption visible → Reform to solid
- **Parallax:** All 4 layers move at different speeds during player movement
- **Purpose:** Psychedelic atmosphere, reality breakdown visualization
- **Performance Optimization:** Can use 2-layer simplified version

### Absinthe Bottle Bar Glow:
- **Duration:** 4-frame pulse, 3 seconds total cycle
- **Pattern:** Dim → Medium → Peak → Descent (smooth sine wave)
- **Continuous:** Never stops glowing while location is active
- **Purpose:** Toxic green atmosphere, bar centerpiece attention draw
- **Audio Sync:** Subtle hum increases with glow intensity

### Mirror Reflection Lag:
- **Duration:** 0.2-second delay on all player movement near mirrors
- **Pattern:** Player moves → Mirror reflection updates 0.2s later
- **Technical:** Duplicate player sprite with transform delay shader
- **Purpose:** Subtle wrongness feeling, reality distortion theme
- **Performance Optimization:** Disable on devices below medium settings

### Rigged Claw Machine Physics:
- **Duration:** Variable based on player input timing
- **Pattern:** Claw descends → Grabs prize → Lifts → Visibly weakens grip → Drops prize
- **Visual:** Claw obviously loosens when near success (comedy beat)
- **Purpose:** Satirical tourist trap mechanics, intentional frustration
- **Strategy:** After 5 failures, success probability increases slightly

---

## ♿ Accessibility Sprite Requirements

*(All accessibility sprites live in `environmental_effects.png` at the coordinates below.)*

### High Contrast Alternatives (Colorblind-Friendly):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Enhanced Floor Tiles | (528, 416) | 256x96 | High contrast for light-up patterns |
| Cabinet Screen Clarity | (784, 416) | 128x96 | Readable game content |
| Mural Visibility | (912, 416) | 112x96 | Pattern-based instead of color-only |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Mural Alternative | (544, 0) | 480x256 | Non-parallax Green Fairy |
| Reduced Flicker Lighting | (544, 256) | 256x128 | Gentle floor tile pulse |
| Minimal Particle Mode | (800, 256) | 224x128 | Essential mist only |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cabinet Sound Visual | (528, 384) | 32x32 | Audio indicator for deaf players |
| Token Machine Beep | (560, 384) | 32x24 | Transaction confirmation visual |
| Hidden Entrance Reveal | (592, 384) | 48x32 | Discovery cue without audio dependency |

### Colorblind Considerations:
- Light-up floor tiles, mural corruption, and DDR token progress all offer pattern/shape-based indicators wherever color codes meaning
- Touch zones minimum 44px for interactive elements (cabinets, token machine, prompts)

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) for green glow effects, maintains toxic aesthetic with alpha for mist particle transparency
- **Fallback:** PNG high quality for mural parallax detail

### Sprite Atlasing Strategy:
- **Tileset Atlas:** Floor + walls + ceiling combined (1024x1024)
- **Arcade Machines Atlas:** All cabinets + claw machine (2048x1024)
- **Mural Parallax Atlas:** 4 layers separate for parallax effect (1024x512)
- **Environmental Effects Atlas:** Bar + seating + particles (1024x512)
- **Max Atlas Size:** 2048x2048 for broad GPU compatibility

### LOD (Level of Detail) Scaling:
- **High-End Devices:** Full particle systems, parallax mural, mirror lag effect
- **Medium Devices:** Reduced particle density, simplified parallax (2 layers)
- **Low-End Devices:** Static mural, minimal particles, no mirror lag
- **Potato Mode:** Essential cabinets and bar only, no effects

### Performance Targets:
- **Target FPS:** 60 fps (psychedelic atmosphere requires smoothness)
- **Max Draw Calls:** 15 per frame
- **Memory Footprint:** 50MB maximum for location

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Parallax layers: Use ParallaxBackground and ParallaxLayer nodes
- Particle systems: CPUParticles2D for performance (not GPU particles)
- Mirror effect: Custom shader with position delay, or sprite duplication with offset
- Floor tile system: TileMap with animated tiles, random activation script

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Floor tile activation | Electronic beep | On glow start |
| Cabinet screen flicker | Analog distortion burst | On glitch frame |
| Claw machine NFT dispense | Remixed "Für Elise" | On prize drop |
| Token exchange complete | Metallic clink | On dispense animation |
| Hidden entrance reveal | Atmospheric drone swell | On passage open |
| Regret button press | Deep bass thump + sizzle | On button press |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| NFT Hunt | Claw machine, NFT prize sprite | Beer Pong Saint Relic acquisition |
| Brewery Tour | Cracked Time Crisis, hidden passage | Absinthium Taproom access |
| Couchsurf System | (NPC sprites separate) | Backpack Girl interaction |
| Sinfonia Prep | Hidden Game Boy (discoverable item) | Symbol puzzle preparation |
| Hidden Bathroom | DDR machine, token slot | 3-token unlock mechanic |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Absinthium Taproom | Time Crisis passage sprites | Green glow intensifies, fade transition |
| Claw Machine Maintenance Closet | DDR token progress sprites | Mechanical grinding, door reveal |
| Clocktower Plaza | (Exterior handled separately) | Arcade sounds fade, plaza ambience rises |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Corrupted childhood nostalgia meets psychedelic tourist trap"
- **Color Mood:** Toxic green dominance (#39FF14), neon purple accents (#BF00FF), deep black voids (#0A0A0A)
- **Lighting:** Blacklight wash with UV-reactive materials, flickering point sources, no natural light
- **Texture:** Cracked arcade surfaces, digital melting imagery, grimy yet glowing

### Arcade Cabinet Direction:
- **Parody Games:** Obvious twists on 80s/90s classics (Frogger, Street Fighter)
- **Visual Decay:** Green mist leaking from cabinet seams, cracked screens still functional
- **Screen Content:** Game parodies visible and recognizable, philosophical/absurd text readable
- **Nostalgic Corruption:** Familiar shapes made uncomfortable through color and decay

### Green Fairy Mural Philosophy:
- **Iconic Imagery:** Classic absinthe advertising fairy, recognizable silhouette
- **Digital Corruption:** Circuit board patterns eating into organic fairy form
- **Parallax Depth:** Creates sense of the mural being a portal, not flat surface
- **Melting Effect:** Suggests reality breakdown, absinthe hallucination aesthetic

### Environmental Storytelling:
- **Mismatched Seating:** Haphazard tourist trap setup (highchair, beanbag, bidet at bar)
- **Overpriced Exchange:** Token machine prominently displays unfair rates
- **Mirror Lag:** Subtle wrongness players notice subconsciously
- **Hidden Areas:** Reward exploration with discoverable passages

### Character Integration Notes:
- NPCs (Backpack Girl, Twitchy Hackers, EDM Ghosts) require separate sprite sheets
- NPC positions should account for bar seating, cabinet clustering, north wing depth
- EDM Ghosts should have translucent rendering with glow stick color accents

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Green Fairy Mural** - Psychedelic parallax melting effect, perfect for "trippy game" posts
2. **Bidet Bar Stool** - Absurd seating choice, guaranteed "WTF" reactions
3. **Kebab Kombat Cabinet** - Single "REGRET" button fighting game, meme-ready
4. **Mirror Lag Effect** - Reflection delay creates creepy video content
5. **Rigged Claw Machine** - Obviously unfair NFT grab, rage-bait comedy

### TikTok Potential:
- "Childhood arcade games reimagined wrong" (cabinet tour video)
- "When your reflection is late to the party" (mirror lag showcase)
- "The most cursed bar seating ever" (bidet stool reaction)
- "Found the absinthe arcade tourist trap" (location reveal)
- "POV: You're trying to win a fake NFT" (claw machine frustration)

### Twitter/X Quote Potential:
- "I got high and accidentally joined a DAO" (NPC dialogue)
- "This place accepted crypto before it was a currency… or a cult" (NPC dialogue)
- Every arcade parody game title is meme material
- "Lose Your Mind One Token at a Time" (location tagline)
- "The only button is REGRET" (Kebab Kombat description)

---

## 📋 Required PNG Files (4 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | absinthe_arcade_tileset.png | 1024x1024 |
| 2 | arcade_machines_spritesheet.png | 2048x1024 |
| 3 | green_fairy_mural_parallax.png | 1024x512 |
| 4 | environmental_effects.png | 1024x512 |

**Total Estimated Memory:** ~16 MB uncompressed RGBA (well within the 50MB location budget)

---

## 📦 File Delivery Checklist

### Required PNG Files (4 Total):
- [ ] `absinthe_arcade_tileset.png` (1024x1024)
- [ ] `arcade_machines_spritesheet.png` (2048x1024)
- [ ] `green_fairy_mural_parallax.png` (1024x512)
- [ ] `environmental_effects.png` (1024x512)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha channel |
| Color Space | sRGB |
| DPI | 72 (screen resolution) |
| Compression | Lossless PNG |
| Naming Convention | snake_case, all lowercase |
| Layer Organization | Preserve parallax layers separately in master file |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/Photoshop file with organized layer groups
- **Documentation:** Animation timing reference sheet, parallax layer guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 4 PNG files match exact dimensions specified
- [ ] Floor tiles create believable disorienting random pattern when tiled
- [ ] Arcade cabinets show clear parody game content on screens
- [ ] Green Fairy mural has 4 distinct parallax layers with proper scroll speeds
- [ ] Mirror reflection lag is technically achievable with provided assets
- [ ] Claw machine NFT prize is intentionally ugly (8-bit halo red solo cup)
- [ ] Bidet bar stool is clearly identifiable and absurd
- [ ] Green glow maintains toxic aesthetic throughout all elements
- [ ] Color palette matches hex codes exactly
- [ ] Accessibility visual alternatives included for audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Arcade parodies are instantly recognizable yet twisted
- [ ] Green Fairy mural creates genuine psychedelic depth
- [ ] Environmental effects support tourist trap atmosphere
- [ ] Hidden areas (bathroom entrance, brewery passage) have discoverable visual cues
- [ ] Nostalgic corruption theme is clear throughout all assets
- [ ] Performance optimized (particle systems use CPU, not GPU)
- [ ] All elements support "childhood corrupted" satire consistently
- [ ] Social media viral potential maximized in composition choices
- [ ] Touch zone sizing considered for interactive elements (44px minimum)
- [ ] Colorblind-friendly alternatives available where color-coded

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ PASS | Debaucheryville only |
| Cultural Specificity | ✅ PASS | Prague absinthe/arcade culture |
| Satirical Targets Appropriate | ✅ PASS | Tourist behavior, not locals |
| Seedy Underbelly Present | ✅ PASS | Rigged games, overpriced tokens |
| Gameplay Value Established | ✅ PASS | NFT hunt, brewery access, minigames |
| Technical Feasibility | ✅ PASS | Mobile optimization documented |
| Performance Budget | ✅ PASS | 60 FPS, 15 draw calls, 50MB |
| Accessibility Features | ✅ PASS | Visual audio cues included |
| No Crypto Elements | ✅ PASS | Beer Pong Saint Relic NFT is satirical and established in source material; no functional crypto |
| Social Media Integration | ✅ PASS | Multiple viral moments identified |

**Once validated, the Absinthe Arcade becomes the psychedelic quest hub where players experience corrupted gaming nostalgia, meet Backpack Girl Who Never Left, obtain the Beer Pong Saint Relic NFT from a rigged claw machine, discover hidden passages to the Absinthium Taproom and secret bathroom, and play parody arcade games while bros think they're experiencing sophisticated underground European culture!**
