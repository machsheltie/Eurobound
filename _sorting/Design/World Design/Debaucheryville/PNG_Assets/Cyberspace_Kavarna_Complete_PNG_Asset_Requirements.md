# Cyberspace Kavarna - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for Cyberspace Kavarna - the Y2K-era Eastern European internet cafe where digital dreams die slowly, one dial-up connection at a time.

**Location ID:** `debaucheryville_hostelrow_cyberspace_kavarna_01`  
**Theme:** Eastern Bloc internet culture meets Y2K digital underground  
**Primary Function:** ICQ quest hub, sting operations, metro access unlock, 24-hour terminal rental

---

## 🎨 Sprite Sheet 1: Cyberspace Kavarna Tileset
**File:** `cyberspace_kavarna_tileset.png`  
**Dimensions:** 512x512 pixels  
**Color Palette:** #00FF41 (monitor green), #DC143C (soviet red), #696969 (smoke grey)

### Floor Tiles (32x32 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Concrete Basement | (0, 0) | 32x32 | Raw concrete, stained |
| Cable Covered | (32, 0) | 32x32 | Ethernet cables snaking |
| Stained Floor | (64, 0) | 32x32 | Coffee and cigarette stains |
| Duct Tape Patch | (96, 0) | 32x32 | Cables taped to floor |
| Cigarette Scatter | (128, 0) | 32x32 | Butts scattered |
| Ethernet Junction | (160, 0) | 32x32 | Multiple cables meeting |

### Wall Tiles (64x64 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Basement Wall Bare | (0, 32) | 64x64 | Raw basement wall |
| Wall With Cables | (64, 32) | 64x64 | Ethernet duct-taped |
| Bootleg Poster Wall | (128, 32) | 64x64 | Movie posters attached |
| Warning Signs Wall | (192, 32) | 64x64 | Multiple warnings |

### Ceiling/Staircase (Various):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fluorescent Off | (0, 96) | 32x32 | Inactive light |
| Fluorescent On | (32, 96) | 32x32 | Harsh white |
| Stairs Top | (0, 128) | 64x48 | Street entrance |
| Stairs Bottom | (0, 176) | 64x48 | Basement arrival |

---

## 💻 Sprite Sheet 2: CRT Terminal Spritesheet
**File:** `crt_terminal_spritesheet.png`  
**Dimensions:** 1024x512 pixels  
**Color Palette:** #00FF41 (screen green), #E8E8D0 (beige), #0000FF (BSOD blue)

### CRT Monitors:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Base Monitor | (0, 0) | 64x56 | Standard CRT frame |
| Screen Normal | (64, 0) | 48x40 | Desktop display |
| Screen ICQ Active | (112, 0) | 48x40 | ICQ chat window |
| Screen Blue Screen | (208, 0) | 48x40 | BSOD display |
| Beige CRT | (0, 56) | 64x56 | Classic 90s |
| Cracked CRT | (128, 56) | 64x56 | Damaged, works |

### Furniture & Accessories:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Soviet Desk | (0, 112) | 80x48 | Heavy, durable |
| Office Chair | (0, 160) | 40x56 | Stained, squeaky |
| Keyboard Beige | (0, 280) | 48x16 | 90s keyboard |
| Ashtray Full | (80, 280) | 24x16 | Overflowing |

### Special Terminals:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Terminal 7 | (352, 0) | 64x56 | Hidden crypto wallet |
| Terminal 13 | (416, 0) | 64x56 | Shadow Exchange data |

---

## 👥 Sprite Sheet 3: Kavarna NPC Spritesheet
**File:** `kavarna_npc_spritesheet.png`  
**Dimensions:** 512x512 pixels  

### Dmitri the Operator (48x64 each):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Idle | (0, 0) | 48x64 | Thousand-yard stare |
| Smoking | (48, 0) | 48x64 | Cigarette, exhaling |
| Pointing | (96, 0) | 48x64 | Gesturing to terminal |
| Sighing | (144, 0) | 48x64 | Exasperated |

**Dmitri Notes:** 50s, nicotine-stained fingers, faded Adidas tracksuit, Y2K survivor aesthetic

### Dmitri "The Router" Complete Set (ported from legacy spec):
- **Idle Chain Smoking** (0, 0, 64x96) - Default pose with cigarette, deadpan expression
- **Dispensing Wisdom** (64, 0, 64x96) - Philosophical gesture while exhaling smoke
- **Collecting Payment** (128, 0, 64x96) - Hand extended, serious business expression
- **Technical Support Gesture** (192, 0, 64x96) - Pointing at obviously broken equipment
- **Philosophical Contemplation** (256, 0, 64x96) - Deep thought about American tourists
- **Late Night Exhaustion** (320, 0, 64x96) - 3 AM special wisdom mode
- **Lawsuit Commentary Pose** (384, 0, 64x96) - Casual dismissal of legal problems
- **Restart Everything Gesture** (448, 0, 64x96) - Universal technical solution

> ⚠ CONFLICT: legacy spec says NPC base sprites are 64x96 (512x384 sheet) — BASE uses 48x64 on a 512x512 sheet; legacy coordinates would need remapping — author to decide.

### CyberGoth Katka (48x64 each):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Idle | (0, 64) | 48x64 | Energy drink nearby |
| Typing | (48, 64) | 48x64 | Rapid keyboard |
| Excited | (96, 64) | 48x64 | Discovery moment |
| Conspiratorial | (144, 64) | 48x64 | Leaning, whispering |

**Katka Notes:** Early 20s, cyber-goth, thinks she's Anonymous, fingerless gloves

### CyberGoth Katka Complete Set (ported from legacy spec):
- **Hacker Wannabe Pose** (0, 96, 64x96) - Anonymous mask adjustment, trying to look mysterious
- **Energy Drink Consumption** (64, 96, 64x96) - Rapid consumption of hacker fuel
- **Meme Page Management** (128, 96, 64x96) - Updating 47-follower social media empire
- **Intel Trading Gesture** (192, 96, 64x96) - Negotiating for American candy payment
- **Anonymous Mask Adjustment** (256, 96, 64x96) - Maintaining "subtle" anonymity
- **American Candy Request** (320, 96, 64x96) - Specific Skittles vs M&Ms preferences
- **Social Media Viral Moment** (384, 96, 64x96) - Creating "authentic" hacker content
- **Information Broker Mode** (448, 96, 64x96) - Providing questionable intelligence

### Other NPCs:
| NPC | Position | Size | Description |
|-----|----------|------|-------------|
| Script Kiddie Gaming | (0, 128) | 48x64 | Counter-Strike focus |
| Crypto Miner | (0, 192) | 48x64 | Watching rig |
| Digital Nomad | (0, 256) | 48x64 | Banking obliviously |
| ICQ Veteran | (0, 320) | 48x64 | Nostalgic look |

### Additional Patron Archetypes (ported from legacy spec):
- **Passed Out Gamer** (256, 192, 64x96) - Counter-Strike marathon casualty
- **Security Conscious Tourist** (320, 192, 64x96) - Reading warnings while ignoring them
- **Government Surveillance** (384, 192, 64x96) - Obviously monitoring everything
- **Bootleg Software Dealer** (448, 192, 64x96) - CD collection and furtive transactions

### Scammer Network Representatives (ported from legacy spec):
- **Tony420 Fake Crypto** (0, 288, 64x96) - Crypto scammer with obvious fake wallet
- **Miss Morphine Mysterious** (64, 288, 64x96) - Identity mystery with multiple personas
- **NarcGreg Infiltration Attempt** (128, 288, 64x96) - Terrible undercover work
- **Coordinated Team Leader** (192, 288, 64x96) - Professional tourist targeting
- **Government Agent Obvious** (256, 288, 64x96) - Surveillance barely disguised
- **Underground Network Contact** (320, 288, 64x96) - Legitimate digital underground
- **Romance Scammer Active** (384, 288, 64x96) - Emotional manipulation specialist
- **Tech Support Scammer** (448, 288, 64x96) - Fake virus warning coordinator

### NPC Accessories & Props (ported from legacy spec):
- **Cigarette Collection** (0, 384, 32x16) - Various smoking stages and brands
- **Energy Drink Empties** (32, 384, 24x32) - Katka's consumption evidence
- **Calculator Variety** (56, 384, 32x16) - Dmitri's mysterious multiple calculators
- **Anonymous Mask** (88, 384, 24x24) - Katka's "subtle" disguise prop
- **ICQ Number Badge** (112, 384, 24x16) - 6-digit seniority display
- **Mining Rig Status** (136, 384, 32x24) - Religious devotion equipment
- **Scammer Evidence** (168, 384, 48x32) - Various fake documents and schemes
- **Government Surveillance Gear** (216, 384, 32x24) - Obvious monitoring equipment

---

## 🎬 Sprite Sheet 4: Kavarna Decorations
**File:** `kavarna_decorations.png`  
**Dimensions:** 512x512 pixels  

### Payment Counter:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Base | (0, 0) | 128x64 | Dmitri's domain |
| Cash Register | (128, 0) | 48x40 | Ancient mechanical |
| Cash Only Signs | (176, 0) | 64x32 | Multiple languages |

### Crypto Mining Rigs:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rig Running | (0, 64) | 96x80 | Humming, LEDs |
| Rig Overheating | (96, 64) | 96x80 | Warning lights |
| Making Money Sign | (192, 64) | 48x24 | Handwritten hope |

### Bootleg Posters (48x64 each):
| Poster | Position | Description |
|--------|----------|-------------|
| The Matricks | (0, 144) | Keanu spelled wrong |
| Hackers Wrong | (48, 144) | Nicolas Cage somehow |
| Johnny Nemonic | (96, 144) | Every word wrong |
| Swordfish | (144, 144) | Actually accurate |

### Other Decorations:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| No Torrenting Sign | (0, 208) | 64x32 | Red prohibition |
| ICQ Contact Board | (0, 240) | 96x64 | Circled names |
| CryptoDöner Machine | (0, 368) | 64x96 | 1-3 AM only |
| Metro Door Locked | (128, 368) | 48x80 | Sting reward |

### Hidden Metro Access System (ported from legacy spec):
- **Back Exit Door Locked** (0, 240, 64x96) - Quest completion required
- **Back Exit Door Open** (64, 240, 64x96) - Metro access revealed
- **Metro Password Graffiti** (128, 240, 48x32) - Bathroom intel location
- **Underground Tunnel Entrance** (176, 240, 48x96) - Passage to metro platform
- **Quest Completion Gate** (224, 240, 32x96) - Sting operation requirement indicator
- **Metro Password Invalid** (384, 480, 128x96) - Daily password system failure (interface screen)

> ⚠ CONFLICT: legacy spec says the locked metro door is "Back Exit Door Locked" at 64x96 — BASE's Metro Door Locked is 48x80 — author to decide.

---

## ✨ Sprite Sheet 5: Kavarna Effects
**File:** `kavarna_effects.png`  
**Dimensions:** 512x256 pixels  

### INTERNET Neon Sign (160x48 each):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Off | (0, 0) | 160x48 | Unlit tubes |
| On | (160, 0) | 160x48 | Full green glow |
| Flicker 1 | (320, 0) | 160x48 | Partial |
| Flicker 2 | (0, 48) | 160x48 | Different partial |

### Particles & Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Smoke 1-3 | (0, 96) | 32x32 ea | Cigarette wisps |
| Coffee Steam | (96, 96) | 24x24 | Rising steam |
| Electronic Static | (144, 96) | 16x16 | Interference |
| Scan Lines | (0, 128) | 48x40 | CRT overlay |
| Blue Screen Flash | (112, 128) | 48x40 | BSOD moment |

### Status Icons (32x32 each):
| Icon | Position | Description |
|------|----------|-------------|
| Eye Strain | (0, 184) | -1 Accuracy |
| Nicotine | (32, 184) | +1 Speed, -1 HP |
| Paranoia | (64, 184) | +2 Luck vs scams |
| Nostalgia | (96, 184) | +1 all stats |
| Scammer Boost | (128, 184) | +200% messages |

---

## 🎮 Sprite Sheet 6: Kavarna UI
**File:** `kavarna_ui.png`  
**Dimensions:** 256x256 pixels  

### Terminal Rental Menu:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Background | (0, 0) | 160x96 | Menu panel |
| Standard €3 | (0, 96) | 128x24 | 1 hour option |
| All Night €15 | (0, 120) | 128x24 | Special deal |

### ICQ Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Window Frame | (160, 0) | 96x128 | Classic ICQ |
| Message Bubble | (160, 128) | 80x32 | Chat message |
| Uh-Oh Alert | (160, 160) | 48x24 | Notification |

### Sting Operation UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Objective Panel | (0, 168) | 128x48 | Mission display |
| Progress Bar | (0, 216) | 96x16 | Completion |

---

## 🎬 Animation Specifications

### Neon Sign Flicker:
- **Pattern:** On → Flicker 1 → On → On → Flicker 2 → On
- **Timing:** Random 0.1-0.3s per frame, continuous loop
- **Audio:** Electrical buzz during flicker

### CRT Screen Activity:
- **States:** Normal, ICQ, Windows 98, Loading, Error, BSOD
- **BSOD Trigger:** 15% probability per hour
- **Audio:** Windows sounds for state changes

### Dmitri Smoking:
- **Pattern:** Idle → Smoking → Idle → Sighing
- **Smoke Puff:** Every 15 seconds
- **Continuous background animation

### Cigarette Smoke Drift:
- **FPS:** 4
- **Movement:** Upward with horizontal variance
- **Spawn:** Ashtrays and NPC hands

---

## ♿ Accessibility Sprite Requirements (ported from legacy spec)

### High Contrast Terminal Elements:
- **Enhanced CRT Borders** (0, 0, 128x96) - Clear monitor distinction from background
- **High Contrast ICQ Interface** (128, 0, 128x64) - Readable chat text and UI elements
- **Status Effect Outlines** (256, 0, 64x64) - Clear effect boundary indication

### Motion Sensitivity Alternatives:
- **Static CRT Alternative** (0, 64, 128x96) - No flicker effects for photosensitive users
- **Reduced Smoke Mode** (128, 64, 96x64) - Minimal particle movement
- **Gentle Neon Animation** (224, 64, 64x48) - Slower entrance sign flicker rate

### Visual Audio Cues:
- **ICQ Message Visual** (0, 112, 48x32) - Chat notification without sound dependency
- **Network Activity Indicator** (48, 112, 32x32) - Data transfer visual representation
- **System Error Visual** (80, 112, 48x32) - Blue screen crash without audio

### Clear Navigation Elements:
- **Enhanced Interactive Zones** (0, 144, 64x48) - Obvious terminal interaction areas
- **Payment Interface Highlighting** (64, 144, 96x24) - Clear service selection
- **Quest Progress Visibility** (160, 144, 96x48) - High contrast sting operation tracking

---

## 📱 Mobile Optimization Requirements (ported from legacy spec)

### Texture Compression by Platform:
- **iOS:** PVRTC 4BPP for CRT glow and fluorescent lighting effects
- **Android:** ETC2 with alpha for smoke transparency and particle systems
- **Fallback:** PNG high quality for text readability in ICQ interfaces

### Sprite Atlasing Strategy:
- **Environment Complete Atlas:** Basement + terminals + furniture + infrastructure (1024x768)
- **Interactive Objects Atlas:** CRTs + cables + payment + metro access (512x384)
- **NPC Atlas:** Dmitri + Katka + patrons + scammers (512x384)
- **Interface Screens Atlas:** Windows 98 + ICQ + quest progression (512x512)
- **Particle Effects Atlas:** Smoke + static + status effects (512x256)
- **Max Atlas Size:** 2048x2048 for mobile GPU compatibility

> ⚠ CONFLICT: legacy spec says atlases follow the legacy 5-sheet layout above — BASE's File Delivery Checklist defines 6 different sheet files/dimensions — author to decide.

### LOD (Level of Detail) Scaling:
- **High-End Devices:** Full CRT flicker, all smoke particles, complete interface animations
- **Medium Devices:** Reduced flicker rate, simplified smoke, basic status effects
- **Low-End Devices:** Static monitors, minimal particles, essential animations only
- **Potato Mode:** No particles, static lighting, basic terminal functionality

### Performance Targets:
- **Target FPS:** 45 fps (multiple CRT effects and smoke simulation)
- **Max Draw Calls:** 18 per frame
- **Memory Footprint:** 42MB maximum for location

> ⚠ CONFLICT: legacy spec says 45 fps / 42MB — BASE validation table says 60 FPS, 18 draws, 45MB — author to decide.

---

## 🔧 Technical Integration Notes (ported from legacy spec)

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Animation system: Frame-based with JSON timing data
- ICQ system: Real-time chat interface simulation
- Quest system: Multi-step sting operation coordination
- Particle systems: CPUParticles2D for smoke and electronic effects

### Audio Sync Points:
- Dmitri philosophical commentary syncs with cigarette exhales
- ICQ notifications sync with message alert flashes
- Network activity syncs with ethernet cable data flow
- CRT flicker syncs with period-authentic monitor sounds
- Blue screen events sync with Windows 98 crash audio
- Generator startup syncs with power outage particle effects

### Cross-Location Dependencies:
- **Shadow Exchange:** NFT hunting data coordination via Terminal 13
- **Couchsurfing Chronicles:** Miss Morphine coordination and social engineering
- **Metro Platform:** Underground transportation network access
- **Bathroom Graffiti:** Daily password system and FlagMan wisdom integration

---

## 📦 File Delivery Checklist

### Required PNG Files (6 Total):
- [ ] `cyberspace_kavarna_tileset.png` (512x512)
- [ ] `crt_terminal_spritesheet.png` (1024x512)
- [ ] `kavarna_npc_spritesheet.png` (512x512)
- [ ] `kavarna_decorations.png` (512x512)
- [ ] `kavarna_effects.png` (512x256)
- [ ] `kavarna_ui.png` (256x256)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha |
| Color Space | sRGB |
| DPI | 72 |
| Naming | snake_case |

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **INTERNET Neon Sign** - Flickering Y2K aesthetic
2. **CRT Monitor Maze** - Half blue-screened
3. **Dmitri Smoking** - Philosophical tech wisdom
4. **Bootleg Posters** - "The Matricks" visible
5. **ICQ Contact Board** - Scammer names circled

### Quote Potential:
- "Connection is life. Disconnection is death. Payment is now."
- "Cash only. Credit cards are American conspiracy."
- "Computer broken? Is feature, not bug."
- "Password is 'password123' - like bank security."
- "This place survivor of Y2K, dial-up, and three economic crashes."

---

## 🏆 Location Validation Status

| Requirement | Status |
|-------------|--------|
| World Consistency | ✅ PASS |
| Cultural Specificity | ✅ PASS |
| Satirical Targets | ✅ PASS |
| Seedy Underbelly | ✅ PASS |
| Gameplay Value | ✅ PASS |
| Technical Feasibility | ✅ PASS |
| Mobile Performance | ✅ PASS (60 FPS, 18 draws, 45MB) |
| Accessibility | ✅ PASS |
| Social Media | ✅ PASS |

**Cyberspace Kavarna becomes the essential Y2K internet cafe hub where players access the ICQ quest network, coordinate sting operations, unlock metro access, experience dial-up nostalgia with blue screens and "password123" security, and receive philosophical wisdom from Dmitri while their data is definitely not safe!**
