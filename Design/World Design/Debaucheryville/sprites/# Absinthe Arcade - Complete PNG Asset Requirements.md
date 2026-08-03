# Absinthe Arcade - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Absinthe Arcade location. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this psychedelic barcade dungeon.

---

## 🎨 Sprite Sheet 1: Absinthe Arcade Tileset
**File:** `absinthe_arcade_tileset.png`  
**Dimensions:** 1024x1024 pixels  
**Color Palette:** #39FF14 (toxic green), #BF00FF (neon purple), #0A0A0A (deep black), #00FF41 (UV reactive green)

### Floor Tiles (32x32 each):
- **Standard Floor** (0, 0, 32x32) - Base tile, dark with subtle texture
- **Light-Up Tile Off** (32, 0, 32x32) - Inactive state
- **Light-Up Tile Frame 1** (64, 0, 32x32) - Dim glow beginning
- **Light-Up Tile Frame 2** (96, 0, 32x32) - Medium brightness
- **Light-Up Tile Frame 3** (128, 0, 32x32) - Peak brightness
- **Light-Up Tile Flicker** (160, 0, 32x32) - Malfunction state
- **Cracked Floor Variation 1** (192, 0, 32x32) - Visible damage
- **Cracked Floor Variation 2** (224, 0, 32x32) - Heavy wear
- **Green Glow Floor** (256, 0, 32x32) - UV reactive permanent glow

### Wall Tiles (64x64 each):
- **Blacklight Wall Base** (0, 32, 64x64) - Standard blacklight wash
- **Mirror Wall Normal** (64, 32, 64x64) - Reflective surface
- **Mirror Wall Lagged** (128, 32, 64x64) - 0.2s reflection delay state
- **Cracked Wall Light** (192, 32, 64x64) - Minor structural damage
- **Cracked Wall Heavy** (256, 32, 64x64) - Significant arcade decay
- **Circuit Pattern Wall** (320, 32, 64x64) - Green Fairy mural integration

### Ceiling Tiles (48x48 each):
- **Standard Ceiling** (0, 96, 48x48) - Dark overhead
- **Exposed Wiring** (48, 96, 48x48) - Electrical hazard visible
- **Flickering Light Source** (96, 96, 48x48) - Unstable illumination
- **Green Glow Wash** (144, 96, 48x48) - Toxic atmospheric tint

### Green Glow Overlay Effects:
- **Subtle Glow** (384, 0, 128x128) - Gentle toxic green wash
- **Medium Intensity** (512, 0, 128x128) - Standard arcade glow
- **Peak Intensity** (640, 0, 128x128) - Overwhelming green effect
- **Pulsing Animation Frame 1** (768, 0, 128x128) - Breathing effect start
- **Pulsing Animation Frame 2** (896, 0, 128x128) - Peak pulse

### Technical Notes:
- Floor tiles: Random activation pattern (0.5-3 second delays)
- Mirror lag: 0.2-second delay on player reflection
- Green glow: Continuous pulse effect for atmosphere
- UV reactive: Materials respond to blacklight lighting

---

## 🕹️ Sprite Sheet 2: Arcade Machines Spritesheet
**File:** `arcade_machines_spritesheet.png`  
**Dimensions:** 2048x1024 pixels  
**Color Palette:** #39FF14 (screen glow), #FF1493 (cabinet pink), #00FFFF (cyan screens), #8B4513 (cabinet wood)

### Frogger: Existential Edition Cabinet:
- **Idle State** (0, 0, 128x192) - Standard arcade cabinet, philosophical title
- **Active Playing** (128, 0, 128x192) - Screen lit, existential obstacles visible
- **Broken Leaking Mist** (256, 0, 128x192) - Cracked cabinet with green fog
- **Screen Content Frame 1** (384, 0, 64x48) - Philosophical obstacles
- **Screen Content Frame 2** (448, 0, 64x48) - Existential traffic
- **Screen Content Frame 3** (512, 0, 64x48) - Life questions as hazards

### Street Fighter: Identity Crisis Cabinet:
- **Idle State** (0, 192, 128x192) - Cabinet with identity confusion theme
- **Active Mid-Combo** (128, 192, 128x192) - Characters questioning moves
- **Broken State** (256, 192, 128x192) - Damaged, identity lost
- **Screen Identity Question 1** (384, 192, 64x48) - "Who am I hitting?"
- **Screen Identity Question 2** (448, 192, 64x48) - Character self-doubt
- **Screen Identity Question 3** (512, 192, 64x48) - Move confusion

### Kebab Kombat Cabinet:
- **Idle State** (0, 384, 128x192) - Fighting game aesthetic
- **Active Regret Button** (128, 384, 128x192) - Single button glowing
- **Broken State** (256, 384, 128x192) - Leaking mystery meat vapor
- **Regret Button Glow 1** (384, 384, 64x64) - Button dim
- **Regret Button Glow 2** (448, 384, 64x64) - Button bright
- **Regret Button Pressed** (512, 384, 64x64) - Active press state

### Rigged Absinthe Arcade Claw Machine:
- **Idle Operating** (576, 0, 256x384) - Standard claw machine view
- **Claw Moving** (832, 0, 256x384) - Rigged physics active
- **Dispensing NFT** (1088, 0, 256x384) - Beer Pong Saint Relic dropping
- **NFT Inside** (576, 384, 64x64) - 8-bit halo red solo cup
- **Claw Mechanism 1** (640, 384, 48x64) - Claw open
- **Claw Mechanism 2** (688, 384, 48x64) - Claw closing
- **Rigged Physics Visual** (736, 384, 96x96) - Obviously unfair grab

### Broken DDR Machine:
- **Cabinet Base** (1344, 0, 192x256) - Dance Dance Revolution setup
- **Broken Pad** (1536, 0, 96x128) - Non-functional dance surface
- **Token Slot** (1632, 0, 64x96) - 3-token unlock mechanism
- **Token Insert 1/3** (1696, 0, 64x32) - Progress indicator
- **Token Insert 2/3** (1760, 0, 64x32) - Progress indicator
- **Token Insert 3/3** (1824, 0, 64x32) - Unlock complete

### Cracked Time Crisis Machine (Hidden Entrance):
- **Cabinet Closed** (1344, 256, 192x256) - Concealing brewery entrance
- **Cabinet Opening** (1536, 256, 192x256) - Revealing passage
- **Hidden Passage Visible** (1728, 256, 192x256) - Absynthium Taproom access
- **Secret Entrance Glow** (1920, 256, 64x96) - Discovery indicator

### Cabinet Universal Elements:
- **Green Mist Particle** (1920, 352, 32x32) - Leaking from damaged machines
- **Electrical Spark** (1952, 352, 24x24) - Random cabinet malfunction
- **Screen Flicker Effect** (1976, 352, 48x48) - 2-second interval glitch

---

## 🧚 Sprite Sheet 3: Green Fairy Mural Parallax
**File:** `green_fairy_mural_parallax.png`  
**Dimensions:** 1024x512 pixels  
**Color Palette:** #00FF41 (fairy green), #BF00FF (circuit purple), #39FF14 (toxic glow), #0A0A0A (background black)

### Layer 1 - Circuit Board Background (Furthest):
- **Circuit Pattern Base** (0, 0, 512x256) - Deep background technology
- **Circuit Glow Points** (512, 0, 512x256) - Pulsing connection nodes

### Layer 2 - Fairy Silhouette (Middle-Far):
- **Fairy Form Solid** (0, 256, 256x256) - Green Fairy iconic shape
- **Fairy Form Dissolving** (256, 256, 256x256) - Beginning melt effect
- **Fairy Form Melted** (512, 256, 256x256) - Heavy corruption state

### Layer 3 - Melting Effect (Middle-Near):
- **Drip Frame 1** (768, 0, 256x128) - Initial melt
- **Drip Frame 2** (768, 128, 256x128) - Progressive melting
- **Drip Frame 3** (768, 256, 256x128) - Advanced decay
- **Drip Frame 4** (768, 384, 256x128) - Near-complete melt

### Layer 4 - Circuit Overlay (Nearest):
- **Circuit Overlay Active** (0, 512, 512x256) - Foreground tech corruption
- **Circuit Overlay Pulsing 1** (512, 512, 256x128) - Animation frame
- **Circuit Overlay Pulsing 2** (768, 512, 256x128) - Peak intensity

### Parallax Movement Specifications:
- **Layer 1:** Moves at 0.2x player speed (deep background)
- **Layer 2:** Moves at 0.5x player speed (mid-ground)
- **Layer 3:** Moves at 0.8x player speed (near-ground)
- **Layer 4:** Moves at 1.0x player speed (foreground)

### Animation Timing:
- Melting effect: 4-frame loop, 3 seconds total
- Circuit pulse: 2-frame cycle, 1.5 seconds
- Fairy dissolve: Gradual 6-second transformation

---

## 🍾 Sprite Sheet 4: Environmental Effects
**File:** `environmental_effects.png`  
**Dimensions:** 1024x512 pixels  
**Color Palette:** #39FF14 (absinthe glow), #FF69B4 (neon pink), #00FFFF (cyan mist), #FFD700 (token gold)

### Absinthe Bottle Bar System:
- **Bottle Bar Base** (0, 0, 256x128) - Cracked bottle shape structure
- **Glow Animation Frame 1** (256, 0, 256x128) - Dim internal glow
- **Glow Animation Frame 2** (512, 0, 256x128) - Medium brightness
- **Glow Animation Frame 3** (768, 0, 256x128) - Peak toxic green
- **Glow Animation Frame 4** (0, 128, 256x128) - Pulsing descent

### Mismatched Bar Seating:
- **Highchair Seat** (256, 128, 64x96) - Absurdly inappropriate
- **Beanbag Seat** (320, 128, 64x64) - Collapsed gaming furniture
- **Bidet Seat** (384, 128, 64x96) - The infamous bathroom fixture stool
- **Normal Stool** (448, 128, 48x72) - Only one "normal" option

### Token Exchange Machine:
- **Machine Idle** (0, 224, 128x192) - Ready for exchange
- **Machine Active** (128, 224, 128x192) - Processing transaction
- **Machine Dispensing** (256, 224, 128x192) - Tokens falling out
- **Screen Display 1KC=5T** (384, 224, 96x48) - Overpriced conversion rate
- **Token Slot** (480, 224, 48x64) - Kebab coin insertion point

### Particle Systems:
#### Green Mist (From Cabinets):
- **Mist Wisp 1** (0, 416, 32x32) - Light fog particle
- **Mist Wisp 2** (32, 416, 32x32) - Medium density
- **Mist Wisp 3** (64, 416, 32x32) - Thick atmospheric fog
- **Mist Wisp 4** (96, 416, 32x32) - Dissipating particle

#### Electrical Sparks:
- **Spark Small** (128, 416, 16x16) - Minor electrical issue
- **Spark Medium** (144, 416, 24x24) - Active malfunction
- **Spark Large** (168, 416, 32x32) - Dangerous discharge

#### Digital Artifacts:
- **Pixel Corruption 1** (200, 416, 24x24) - Glitch effect
- **Pixel Corruption 2** (224, 416, 24x24) - Data decay
- **Pixel Corruption 3** (248, 416, 24x24) - Reality breakdown
- **Screen Tear Effect** (272, 416, 48x32) - Visual distortion

### Particle Emission Rates:
- **Green Mist:** 3 particles/second from damaged cabinets
- **Electrical Sparks:** Random 1-4 second intervals
- **Digital Artifacts:** Continuous low-density atmospheric effect

---

## 📐 Performance & Assets Requirements

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

## ♿ Accessibility Sprite Requirements

### Colorblind-Friendly Alternatives:
- **Enhanced Floor Tiles** (528, 416, 256x96) - High contrast for light-up patterns
- **Cabinet Screen Clarity** (784, 416, 128x96) - Readable game content
- **Mural Visibility** (912, 416, 112x96) - Pattern-based instead of color-only

### Motion Sensitivity Options:
- **Static Mural Alternative** (544, 0, 480x256) - Non-parallax Green Fairy
- **Reduced Flicker Lighting** (544, 256, 256x128) - Gentle floor tile pulse
- **Minimal Particle Mode** (800, 256, 224x128) - Essential mist only

### Visual Audio Cues:
- **Cabinet Sound Visual** (528, 384, 32x32) - Audio indicator for deaf players
- **Token Machine Beep** (560, 384, 32x24) - Transaction confirmation visual
- **Hidden Entrance Reveal** (592, 384, 48x32) - Discovery without audio

---

## 🎬 Animation Sequence Specifications

### Floor Tile Random Activation:
- **Duration:** Random 0.5-3 second delays per tile
- **Pattern:** Off → dim → bright → flicker → off
- **Coverage:** Approximately 20% of tiles active at any time
- **Purpose:** Disorienting atmosphere, creates wrong feeling

### Arcade Cabinet Screen Flicker:
- **Duration:** 2-second intervals
- **Pattern:** Normal → glitch → static → return
- **Consistency:** All cabinets flicker independently
- **Purpose:** Arcade decay, corrupted nostalgia

### Green Fairy Mural Melting:
- **Duration:** 6-second gradual transformation
- **Pattern:** Solid fairy → dissolving → circuit corruption → return
- **Parallax:** 4 layers move at different speeds
- **Purpose:** Psychedelic atmosphere, reality breakdown

### Absinthe Bottle Bar Glow:
- **Duration:** 4-frame pulse, 3 seconds total
- **Pattern:** Dim → medium → peak → descent
- **Continuous:** Never stops glowing
- **Purpose:** Toxic green atmosphere, bar centerpiece

### Mirror Reflection Lag:
- **Duration:** 0.2-second delay on player movement
- **Pattern:** Player moves → mirror updates late → creates unease
- **Technical:** Duplicate sprite with transform delay
- **Purpose:** Wrong feeling, reality distortion

### Rigged Claw Machine Physics:
- **Duration:** Variable based on player attempt
- **Pattern:** Claw grabs → rigged release → obvious unfairness
- **Visual:** Claw deliberately weakens near prize
- **Purpose:** Satirical tourist trap mechanics

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Parallax layers: Use ParallaxBackground node
- Particle systems: CPUParticles2D for performance
- Mirror effect: Sprite duplication with position delay

### Audio Sync Points:
- Floor tile activation syncs with electronic beep
- Cabinet screens flicker with analog distortion sound
- Claw machine plays remixed "Für Elise" on NFT dispense
- Token exchange machine clinks with overpriced emphasis
- Hidden entrance reveals with atmospheric drone

### Quest Integration:
- **NFT Hunt:** Claw machine dispenses "Beer Pong Saint Relic"
- **Brewery Access:** Time Crisis cabinet reveals Absynthium Taproom
- **Couchsurf System:** Backpack Girl offers accommodation
- **Sinfonia Prep:** Broken Game Boy with symbols findable

### Cross-Location Dependencies:
- **Hidden Bathroom:** 3 tokens into DDR unlocks maintenance closet
- **Brewery Tour:** Time Crisis passage to Absynthium Taproom
- **Character Flow:** NPCs reference 24-Hour Internet Café, Shadow Exchange

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Corrupted childhood nostalgia meets psychedelic tourist trap"
- **Color Mood:** Toxic green dominance, neon purple accents, deep black voids
- **Lighting:** Blacklight wash with flickering point sources, UV reactive materials
- **Texture:** Cracked arcade surfaces, melting digital imagery, lagged reflections

### Arcade Cabinet Direction:
- **Parody Games:** Obvious twists on classics (Frogger with philosophy, Street Fighter with identity crisis)
- **Visual Decay:** Green mist leaking from damaged cabinets
- **Screen Content:** Game parodies visible and playable
- **Nostalgic Corruption:** Childhood memories turned uncomfortable

### Green Fairy Mural Philosophy:
- Iconic absinthe imagery corrupted by digital circuits
- Parallax creates depth and psychedelic movement
- Melting effect suggests reality breakdown
- Circuit overlay shows commercialization of mystique

### Environmental Storytelling:
- Mismatched seating shows haphazard tourist trap setup
- Overpriced token exchange exploits nostalgia
- Mirror lag creates subtle wrongness
- Hidden areas reward exploration

---

## 📦 File Delivery Checklist

### Required PNG Files (4 Total):
- [ ] `absinthe_arcade_tileset.png` (1024x1024)
- [ ] `arcade_machines_spritesheet.png` (2048x1024)
- [ ] `green_fairy_mural_parallax.png` (1024x512)
- [ ] `environmental_effects.png` (1024x512)

### Quality Requirements:
- **Format:** PNG-24 with alpha channel
- **Color Space:** sRGB
- **DPI:** 72 (screen resolution)
- **Compression:** Lossless PNG
- **Naming Convention:** snake_case, all lowercase
- **Layer Organization:** Preserve parallax layers separately

### Delivery Format:
- **Primary:** Individual PNG files per specifications
- **Backup:** Master PSD/Photoshop with organized layer groups
- **Documentation:** Parallax layer guide, animation timing sheet

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Green Fairy Mural** - Psychedelic parallax melting effect
2. **Bidet Bar Stool** - Absurd seating choice
3. **Kebab Kombat** - Single "regret" button fighting game
4. **Mirror Lag Effect** - Reflection delay unease
5. **Rigged Claw Machine** - Obviously unfair NFT grab

### TikTok Potential:
- "Childhood arcade games reimagined wrong"
- "When your reflection is late to the party"
- "The most cursed bar seating ever"
- "Found the absinthe arcade tourist trap"

### Twitter/X Quote Potential:
- "I got high and accidentally joined a DAO"
- "This place accepted crypto before it was a currency… or a cult"
- Every arcade parody game title is meme material

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 4 PNG files match exact dimensions
- [ ] Floor tiles create disorienting random pattern
- [ ] Arcade cabinets show clear parody game content
- [ ] Green Fairy mural has 4 distinct parallax layers
- [ ] Mirror reflection lag is technically achievable
- [ ] Claw machine NFT is intentionally ugly (8-bit halo red solo cup)
- [ ] Bidet bar stool is clearly visible and absurd
- [ ] Green glow maintains toxic aesthetic throughout
- [ ] Color palette matches hex codes
- [ ] Accessibility alternatives included
- [ ] File naming follows convention
- [ ] Master files preserve layer structure

### Quality Checkpoints:
- [ ] Arcade parodies are instantly recognizable yet twisted
- [ ] Green Fairy mural creates psychedelic depth
- [ ] Environmental effects support tourist trap atmosphere
- [ ] Hidden areas (bathroom, brewery) are discoverable
- [ ] Nostalgic corruption theme is clear throughout
- [ ] Performance optimized for particle systems
- [ ] All elements support "childhood corrupted" satire
- [ ] Social media viral potential maximized

**Once validated, the Absinthe Arcade becomes the psychedelic quest hub where players experience corrupted gaming nostalgia, meet Backpack Girl Who Never Left, obtain the Beer Pong Saint Relic NFT, and discover hidden passages while bros think they're in sophisticated underground European culture!**