# Claw Machine Maintenance Closet Restroom - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Claw Machine Maintenance Closet Restroom. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this hidden secret bathroom where childhood arcade nostalgia has been corrupted by adult regret.

**Location ID:** `debaucheryville_arcade_maintenance_closet_01`  
**Theme:** Chaotic retro grime meets early 2000s LAN party afterglow - forbidden backroom of childhood corrupted  
**Primary Function:** Hidden bathroom, graffiti collection, ICQ Rival Trio messaging, achievement progression

---

## 🎨 Sprite Sheet 1: Maintenance Closet Tileset
**File:** `maintenance_closet_tileset.png`  
**Dimensions:** 256x256 pixels  
**Color Palette:** #00FF41 (fluorescent green), #FF69B4 (retro pink), #3C2415 (grime brown), #1C1C1C (shadow black)

### Floor Tiles (32x32 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Grimy Floor Base | (0, 0) | 32x32 | Stained, worn tile surface |
| Puddle Absinthe | (32, 0) | 32x32 | Spilled green liquid pool |
| Chewed Gum Spot | (64, 0) | 32x32 | Multiple gum deposits |
| Cracked Tile | (96, 0) | 32x32 | Damaged flooring |

### Wall Tiles (64x64 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Grime Wall Base | (0, 32) | 64x64 | Dirty wall surface, ready for graffiti overlay |
| Exposed Wiring Wall | (64, 32) | 64x64 | Cables snaking across surface |
| Graffiti Wall Base | (128, 32) | 64x64 | Wall section with texture for UV reveal |

### Ceiling Tiles (32x32 each):
| Tile Name | Position | Size | Description |
|-----------|----------|------|-------------|
| Ceiling With Wiring | (0, 96) | 32x32 | Exposed cables overhead |
| Marquee Light Mount | (32, 96) | 32x32 | Arcade panel mounting point |
| Claw Arm Mount Point | (64, 96) | 32x32 | Chandelier attachment |

### Technical Notes - Tileset:
- Room is extremely cramped - only 3-4 tiles wide in any direction
- Grime brown (#3C2415) should dominate with green accents
- All surfaces should look decades neglected
- Absinthe puddle reflects neon green light

---

## 🚽 Sprite Sheet 2: Closet Furniture Spritesheet
**File:** `closet_furniture_spritesheet.png`  
**Dimensions:** 512x512 pixels  
**Color Palette:** #00FF41 (DDR arrows), #FF69B4 (retro pink), #808080 (metal), #3C2415 (grime)

### DDR Toilet Seat System (64x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Base Toilet | (0, 0) | 64x80 | Toilet with DDR pad seat |
| Arrows Overlay | (64, 0) | 64x80 | Dance pad arrow graphics |
| Pressure Frame UP | (128, 0) | 64x80 | Up arrow lit |
| Pressure Frame DOWN | (192, 0) | 64x80 | Down arrow lit |
| Pressure Frame LEFT | (256, 0) | 64x80 | Left arrow lit |
| Pressure Frame RIGHT | (320, 0) | 64x80 | Right arrow lit |
| Sticky Residue Overlay | (384, 0) | 64x80 | Gross texture layer |
| Combo Counter UI | (448, 0) | 48x24 | "COMBO: X" display |

**DDR Toilet Visual Notes:**
- Actual DDR dance pad design on toilet seat
- Four directional arrows clearly visible
- Sticky residue should be subtle but disgusting
- When arrows light up, they pulse like real DDR
- Combo counter appears during use

### Claw Machine Arm Chandelier (96x128 each):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Hanging Idle | (0, 80) | 96x128 | Suspended from ceiling, limp |
| Twitch Frame 1 | (96, 80) | 96x128 | Slight movement left |
| Twitch Frame 2 | (192, 80) | 96x128 | Slight movement right |
| Grab Attempt | (288, 80) | 96x128 | Claw opens as if trying to grab |
| Chain Detail | (384, 80) | 32x64 | Close-up of mounting chain |

**Chandelier Visual Notes:**
- Recognizable claw machine grabber arm
- Hangs by cable/chain from ceiling
- Occasional pathetic twitch animation
- "Grab attempt" motion at nothing - sad and relatable
- Rusted, worn metal finish

### CRT Mirror System (Various sizes):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Frame | (0, 208) | 80x64 | Beige CRT monitor housing |
| Screen Insert Coin 1 | (80, 208) | 64x48 | "INSERT" text |
| Screen Insert Coin 2 | (144, 208) | 64x48 | "COIN" text |
| Screen Insert Coin 3 | (208, 208) | 64x48 | Full "INSERT COIN" |
| Screen High Score | (272, 208) | 64x48 | Easter egg display |
| Reflection Overlay | (336, 208) | 64x48 | Semi-transparent player reflection |

**CRT Mirror Visual Notes:**
- Old beige/cream colored CRT monitor frame
- Screen shows scrolling "INSERT COIN" text
- Player reflection visible through text
- Easter egg shows embarrassing high score names (ASS, BRO, LOL)
- Subtle scan lines for authenticity

### Sock Dispenser System:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mounted Base | (0, 272) | 48x64 | Wall-mounted dispenser unit |
| Lever Up | (48, 272) | 48x64 | Ready state |
| Lever Down | (96, 272) | 48x64 | Pulled state |
| Sock Dropping | (144, 272) | 48x64 | Sock mid-fall |
| Sock - Argyle Hole | (192, 272) | 24x32 | Fancy sock with hole |
| Sock - Mismatched | (216, 272) | 24x32 | Two different patterns |
| Sock - Crusty Athletic | (240, 272) | 24x32 | Stiff white sock |
| Sock - Novelty Stained | (264, 272) | 24x32 | Cartoon pattern, suspicious stains |

**Sock Dispenser Visual Notes:**
- Repurposed claw machine prize chute
- "PAPER TOWELS" label crossed out
- Each sock should be distinctly gross in different ways
- Lever has satisfying mechanical design

### Foot Soak Bucket:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bucket Base | (0, 336) | 48x48 | Yellow janitor bucket |
| Murky Water | (48, 336) | 48x48 | Disgusting liquid fill |
| Floaties Overlay | (96, 336) | 48x48 | Unidentifiable debris |
| Foot Dipping | (144, 336) | 48x48 | Speedrunner foot in water |

### Maintenance Door:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Closed | (0, 384) | 48x80 | Door fully shut |
| Opening | (48, 384) | 48x80 | Mid-swing awkward |
| Open | (96, 384) | 48x80 | Revealing cramped interior |
| Sticker Detail | (144, 384) | 32x24 | "XXX PAC-MAN" promo |
| Maintenance Label | (176, 384) | 48x16 | Smudged "MAINTENANCE ONLY" |

---

## 🖊️ Sprite Sheet 3: Blacklight Graffiti System
**File:** `blacklight_graffiti.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #FF69B4 (neon pink), #00FFFF (cyan), #FFFF00 (yellow), #FF00FF (magenta) - all UV-reactive colors

### Primary Graffiti:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| SMAAAASH Quote | (0, 0) | 256x64 | "He moaned SMAAAASH in bed. I ghosted mid-combo." |

**Quote Visual Notes:**
- Handwritten style, highlighter ink aesthetic
- Pink/magenta primary color
- Should look hastily scrawled
- Clearly readable when blacklight active

### Secondary Graffiti:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pixelated Art 1 | (0, 64) | 64x64 | Crude pixel art, suggestive |
| Pixelated Art 2 | (64, 64) | 64x64 | Different crude pixel art |
| Fake Cheat Code 1 | (128, 64) | 96x32 | "Up Up Down Down Left Right B A (for love)" |
| Fake Cheat Code 2 | (224, 64) | 96x32 | "IDDQD (for self-esteem)" |
| Tekken Haiku | (128, 96) | 128x32 | 5-7-5 syllable poem about losing match and virginity |

**Secondary Graffiti Notes:**
- Pixelated art should be recognizably inappropriate but low-res
- Cheat codes in gaming font style
- Haiku should be readable and maintain proper syllable count
- All in various neon highlighter colors

### Embarrassed-Exclusive Content:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Combo'd by Love | (0, 128) | 192x48 | Title in stylized text |
| DDR Arrow Glyphs | (192, 128) | 128x48 | Story written in ↑↓←→ arrows |
| Joystick With Lips | (0, 176) | 48x48 | Arcade joystick with lipstick marks |

**Embarrassed-Exclusive Notes:**
- Only visible when player has Embarrassed status
- DDR arrows should form readable patterns
- Joystick icon glows when requirements met
- More intimate/personal content than standard graffiti

### Blacklight Overlay:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| UV Wash Effect | (256, 0) | 256x256 | Purple tint overlay for entire graffiti system |

---

## ⚡ Sprite Sheet 4: Closet Effects
**File:** `closet_effects.png`  
**Dimensions:** 256x256 pixels  
**Color Palette:** #00FF41 (fluorescent), #FFFF00 (spark yellow), #FF69B4 (LED pink), #9400D3 (UV purple)

### Marquee Light Panel:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Off | (0, 0) | 64x32 | Dark panel |
| On | (64, 0) | 64x32 | Full fluorescent green glow |
| Flicker 1 | (128, 0) | 64x32 | Partial illumination |
| Flicker 2 | (192, 0) | 64x32 | Different partial state |

### Electrical Sparks:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Spark 1 | (0, 32) | 16x16 | Small burst |
| Spark 2 | (16, 32) | 16x16 | Medium burst |
| Spark 3 | (32, 32) | 16x16 | Fading spark |
| Arc Effect | (48, 32) | 32x24 | Electrical arc between wires |

### Exposed Wiring:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wire Segment 1 | (0, 48) | 64x16 | Horizontal cable run |
| Wire Segment 2 | (64, 48) | 64x16 | Different cable pattern |
| Wire Junction | (128, 48) | 32x32 | Where wires meet, spark source |

### Atmospheric Particles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Citrus Vapor 1 | (0, 64) | 24x24 | Yellow-tinted mist |
| Citrus Vapor 2 | (24, 64) | 24x24 | Dissipating vapor |
| Vape Mist | (48, 64) | 32x32 | White cloudy particle |

### Pink LED Indicator:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| LED Off | (0, 88) | 16x16 | Dark indicator |
| LED On | (16, 88) | 16x16 | Bright pink glow |
| Glow Effect | (32, 88) | 24x24 | Bloom around LED |

---

## 🎮 Sprite Sheet 5: Closet UI Elements
**File:** `closet_ui.png`  
**Dimensions:** 256x128 pixels  
**Color Palette:** #00FF41 (text green), #FF0000 (warning), #FFFFFF (white), #000000 (black bg)

### Shame Timer Display:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Background | (0, 0) | 128x32 | Dark panel with retro border |
| Text Overlay | (128, 0) | 128x32 | "You've achieved nothing but shame, player one" |

### ICQ Prompt:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Send Button | (0, 32) | 64x32 | "SEND TO RIVALS" |
| Cancel Button | (64, 32) | 64x32 | "KEEP SECRET" |
| Message Preview | (128, 32) | 128x48 | Preview of SMAAAASH quote |

### Achievement Notifications:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Graffiti Discovered | (0, 64) | 96x32 | "GRAFFITI FOUND" popup |
| Title Unlocked | (96, 64) | 96x32 | "TITLE: Joysticks & Shame" |
| Embarrassed Bonus | (192, 64) | 64x32 | "+1 Embarrassed Resistance" |

### DDR Combo UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Combo Counter | (0, 96) | 48x24 | "COMBO: 0" display |
| Arrow Prompts | (48, 96) | 64x24 | Random directional prompts |

---

## 👤 Sprite Sheet 6: Speedrunner NPC Sprites
**File:** `speedrunner_sprites.png`  
**Dimensions:** 256x128 pixels  
**Color Palette:** #808080 (hoodie grey), #00FF00 (energy drink), #FFCC00 (Dorito dust)

### Speedrunner Character:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Idle | (0, 0) | 48x64 | Standing, thousand-yard stare |
| Foot Soak | (48, 0) | 48x64 | Foot in bucket |
| Talking | (96, 0) | 48x64 | Explaining routing |
| Gaming Gloves | (144, 0) | 24x24 | Specialized fingerless gloves |
| Energy Drink Cans | (168, 0) | 32x32 | Empty cans surrounding |

**Speedrunner Visual Notes:**
- Gaunt, pale from indoor lifestyle
- Hoodie with energy drink stains
- Specialized gaming gloves, worn
- Surrounded by empty energy drink cans
- Expression: deeply focused on nothing

---

## 🚪 Sprite Sheet 7: Maintenance Door & Unlock System
**File:** `claw_closet_door_unlock.png`  
**Dimensions:** 256x256 pixels  
**Color Palette:** #8B4513 (door brown), #FF1493 (flickering pink LED), #FFD700 (token gold), #C0C0C0 (metal hardware)

### Flickering Pink LED System:
- **LED Off** (0, 160, 16x16) - Door locked state
- **LED Flicker 1** (16, 160, 16x16) - Unlock animation frame 1
- **LED Flicker 2** (32, 160, 16x16) - Unlock animation frame 2
- **LED Full Bright** (48, 160, 16x16) - Unlocked, access granted

### Token Slot Mechanism:
- **Broken DDR Slot Closed** (0, 176, 48x32) - Insert point
- **Token Inserting** (48, 176, 48x32) - Mid-insertion animation
- **Token Count Display 1/3** (96, 176, 32x16) - Progress indicator
- **Token Count Display 2/3** (128, 176, 32x16) - Progress indicator
- **Token Count Display 3/3** (160, 176, 32x16) - Unlocked state

### Unlock Animation Sequence:
1. Insert token 1 → DDR machine responds
2. Insert token 2 → Pink LED begins flicker
3. Insert token 3 → LED full bright, door unlocks
4. Duration: 1.5 seconds total sequence

---

## 🎵 Sprite Sheet 8: Environmental Effects & Audio Visualizations
**File:** `claw_closet_effects_audio.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #00FF41 (audio wave green), #FF69B4 (techno pink), #FFD700 (warning yellow)

### Techno Music Echo Visualization:
- **Bass Wave Through Wall** (0, 0, 64x32) - Muffled beat visualization
- **Treble Ripple Effect** (64, 0, 64x32) - High-frequency echo
- **Music Sync Sprite Flash** (128, 0, 32x32) - Random visual sync to beats

### Joystick Squeak Loop System:
- **Squeak Visual Wave 1** (0, 32, 48x24) - Audio cue indicator frame 1
- **Squeak Visual Wave 2** (48, 32, 48x24) - Audio cue indicator frame 2
- **Squeak Visual Wave 3** (96, 32, 48x24) - Intensity increases over time
- **Squeak Visual Warning** (144, 32, 64x24) - 30-second warning state

### 30-Second Shame Timer:
- **Timer Bar Empty** (0, 56, 128x16) - Room entry, fresh start
- **Timer Bar 10 Seconds** (0, 72, 128x16) - Progressing
- **Timer Bar 20 Seconds** (0, 88, 128x16) - Warning threshold
- **Timer Bar 30 Seconds** (0, 104, 128x16) - Triggered message

### Achievement Notification Display:
- **"You've achieved nothing but shame"** (0, 120, 256x32) - 30-second trigger text
- **"Player one" Taunt Visual** (0, 152, 128x24) - Automated mockery
- **Achievement Failed Icon** (128, 152, 32x32) - Satirical failure indicator

### Animation Timing:
- Techno echo: Syncs to random beat intervals (0.5-2 seconds)
- Joystick squeak: Increases frequency over stay duration
- 30-second timer: Linear progress, triggers message at completion

---

## 🎬 Animation Sequence Specifications

### Fluorescent Light Flicker:
- **Duration:** Random 1-3 second intervals
- **Pattern:** On → Flicker 1 → On → Flicker 2 → On
- **Flicker Duration:** 0.1 seconds per flicker frame
- **Purpose:** Unsettling atmosphere, blacklight reveal
- **Audio Sync:** Electrical buzz during flicker

### Claw Chandelier Twitch:
- **Trigger:** Random 15-45 second intervals
- **Pattern:** Idle → Twitch 1 → Twitch 2 → Grab Attempt → Idle
- **Duration:** 2 seconds total
- **Purpose:** Sad reminder of failed purpose
- **Audio Sync:** Metal creak, then motor strain

### CRT Mirror Loop:
- **FPS:** 2 frames per second
- **Pattern:** Insert Coin 1 → 2 → 3 → repeat
- **Continuous:** Always looping when visible
- **Easter Egg:** Insert token for high score display

### DDR Toilet Response:
- **Trigger:** Player use interaction
- **Response Time:** 0.2 seconds
- **Pattern:** Random arrow direction lights up
- **Return:** 0.5 seconds back to base state
- **Audio Sync:** DDR arrow hit sound

### Sock Dispenser Use:
- **Duration:** 1.5 seconds total
- **Pattern:** Lever Up → Lever Down → Sock Dropping → Lever Up
- **Result:** Random sock variety spawns
- **Audio Sync:** Mechanical lever, fabric drop

### Electrical Spark Burst:
- **Trigger:** Player proximity (32px) OR random 2-5 seconds
- **Pattern:** Spark 1 → Spark 2 → Arc → Spark 3
- **Duration:** 0.5 seconds
- **Audio Sync:** Electrical crackle

### Joystick Squeak Escalation:
- **Type:** Audio-only progression
- **Stages:** 
  - 0-15 seconds: 20% volume
  - 15-30 seconds: 50% volume
  - 30-60 seconds: 80% volume
  - 60+ seconds: 100% volume
- **Purpose:** Encourage player to leave

### Shame Timer:
- **Trigger:** 30 seconds in location
- **Effect:** Audio announcement + screen flash
- **Repeat:** Every 30 seconds thereafter
- **Text:** "You've achieved nothing but shame, player one"

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Blacklight graffiti: Overlay system with visibility toggle
- Cramped space: Limit camera movement, claustrophobic framing
- DDR toilet: Input capture for arrow timing mini-game

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Fluorescent flicker | Electrical buzz spike | On flicker frame |
| Claw twitch | Metal creak | On twitch start |
| Claw grab | Motor strain | On grab frame |
| DDR arrow light | Arrow hit sound | On pressure |
| Sock dispense | Lever + plop | Throughout animation |
| Spark burst | Electrical crackle | On spark frames |
| Shame timer | Announcement | At 30s intervals |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| ICQ Messaging | ICQ prompt UI | Send SMAAAASH to Rivals |
| Graffiti Collection | All graffiti sprites | Discovery tracking |
| Bathroom Network | Achievement notifications | Cross-city progress |
| Embarrassed Bonus | Exclusive graffiti | Status-dependent reveal |

### Status Effect Visuals:
| Status | Required For | Visual Indicator |
|--------|--------------|------------------|
| Embarrassed | Exclusive graffiti | Joystick with lips glows |
| Cringe Lock (Rivals) | ICQ message sent | Enemy debuff icon |
| Grossed Out | Foot soak/sock | Green face icon |

### Cross-Location Dependencies:
- **Absinthe Arcade:** 3 tokens from main arcade unlock door
- **Bathroom Network:** Part of cross-city graffiti collection
- **Status System:** Embarrassed status enables bonus content

---

## 📐 Mobile Optimization Requirements

### Texture Compression by Platform:
- **iOS:** PVRTC 4BPP for fluorescent effects, maintains neon intensity
- **Android:** ETC2 with alpha for blacklight graffiti transparency
- **Fallback:** PNG high quality for text readability in cramped space

### Sprite Atlasing Strategy:
- **Interior Complete Atlas:** Room + lighting + wiring (512x512)
- **Interactive Elements Atlas:** DDR toilet + claw arm + CRT + chute + bucket (512x512)
- **Graffiti System Atlas:** All blacklight content combined (512x256)
- **Door & Unlock Atlas:** Complete entry system (256x256)
- **Effects & Audio Atlas:** Visual cues and timing systems (512x256)
- **Max Atlas Size:** 1024x1024 for mobile GPU compatibility

### LOD (Level of Detail) Scaling:
- **High-End Devices:** Full spark effects, blacklight graffiti reveal, DDR reactivity
- **Medium Devices:** Reduced spark density, simplified graffiti glow, basic DDR response
- **Low-End Devices:** Static wiring, basic graffiti visibility, minimal effects
- **Potato Mode:** Essential room and interactive elements only, no particle effects

### Performance Targets:
- **Target FPS:** 45 fps (reduced for cramped space rendering)
- **Max Draw Calls:** 10 per frame
- **Memory Footprint:** 25MB maximum for hidden location

---

## ♿ Accessibility Sprite Requirements

### High Contrast Graffiti Alternatives:
- **Enhanced Text Visibility** (0, 176, 256x64) - All graffiti with increased contrast
- **Status Effect Clear Indicators** (256, 176, 128x32) - Embarrassed status visualization
- **Interactive Element Highlights** (384, 176, 96x32) - Touch targets emphasized

### Motion Sensitivity Options:
- **Static Flicker Alternative** (0, 208, 64x32) - Steady fluorescent lighting
- **Reduced Spark Effects** (64, 208, 48x24) - Minimal electrical danger
- **No Swing Chandelier** (112, 208, 96x128) - Static claw arm position

### Visual Audio Cues:
- **Squeak Loop Indicator** (0, 240, 32x16) - Audio visualization for deaf players
- **30-Second Warning Flash** (32, 240, 48x16) - Visual timer substitute
- **DDR Sound Visual** (80, 240, 32x24) - Pad press feedback alternative

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Childhood arcade corrupted by adult regret"
- **Color Mood:** Sickly fluorescent green, retro pink accents, grime brown base
- **Lighting:** Single flickering fluorescent, CRT glow, blacklight reveal
- **Texture:** Everything grimy, sticky, neglected for decades

### DDR Toilet Philosophy:
- **Core Joke:** Someone actually thought this was a good idea
- **Visual:** Unmistakably DDR dance pad repurposed as toilet seat
- **Interaction:** Pressure-sensitive arrows respond to use
- **Comedy:** Combo counter tracks meaningless timing

### Claw Chandelier Meaning:
- **Symbolism:** Failed purpose, still trying to grab something
- **Visual:** Recognizable claw machine arm, now decorative
- **Animation:** Occasional sad twitch, pathetic grab at nothing
- **Relatability:** Players identify with purposeless grasping

### Graffiti Content Direction:
- **Primary Quote:** Sexual + gaming mashup, immediately memorable
- **Secondary Content:** Mix of crude, clever, and cringe
- **Exclusive Content:** More personal/vulnerable for Embarrassed players
- **Overall Tone:** Early 2000s LAN party bathroom humor

### Environmental Storytelling:
- **Sock Dispenser:** Paper towels were too normal for this place
- **Foot Soak:** Speedrunners have normalized the absurd
- **CRT Mirror:** Even hygiene involves "INSERT COIN"
- **Exposed Wiring:** Safety was never a priority

---

## 📦 File Delivery Checklist

### Required PNG Files (6 Total):
- [ ] `maintenance_closet_tileset.png` (256x256)
- [ ] `closet_furniture_spritesheet.png` (512x512)
- [ ] `blacklight_graffiti.png` (512x256)
- [ ] `closet_effects.png` (256x256)
- [ ] `closet_ui.png` (256x128)
- [ ] `speedrunner_sprites.png` (256x128)

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
- **Backup:** Master PSD with organized layers
- **Special Note:** Graffiti layer must support toggle visibility

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **DDR Toilet Seat** - The central absurdist fixture
2. **Claw Machine Chandelier** - Sad decorative repurposing
3. **SMAAAASH Graffiti** - Instantly quotable content
4. **Sock Dispenser** - "Paper towels" crossed out
5. **CRT INSERT COIN Mirror** - Gaming has infected everything
6. **Speedrunner Foot Soak** - Normalized insanity

### TikTok Potential:
- "Found a secret bathroom in the arcade and it has a DDR toilet"
- "The graffiti in this game's bathroom is unhinged"
- "POV: You've achieved nothing but shame, player one"
- "This game has speedrunners soaking their feet in buckets"
- "The paper towel dispenser only gives socks"

### Twitter/X Quote Potential:
- "He moaned SMAAAASH in bed. I ghosted mid-combo."
- "You've achieved nothing but shame, player one"
- "Up Up Down Down Left Right B A (for love)"
- "IDDQD (for self-esteem)"
- The entire Tekken haiku

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 6 PNG files match exact dimensions
- [ ] DDR toilet clearly shows dance pad arrows
- [ ] Claw chandelier is recognizably a claw machine arm
- [ ] All graffiti is readable under blacklight effect
- [ ] SMAAAASH quote is prominent and memorable
- [ ] Sock varieties are distinctly gross
- [ ] CRT mirror shows INSERT COIN loop
- [ ] Speedrunner has energy drink stains and gaming gloves
- [ ] Fluorescent lighting creates sickly green atmosphere
- [ ] All interactive elements have clear state changes

### Quality Checkpoints:
- [ ] Early 2000s LAN party aesthetic captured
- [ ] Graffiti humor lands without being truly offensive
- [ ] DDR toilet is clearly interactive
- [ ] Claw chandelier evokes sadness/relatability
- [ ] Cramped space feeling conveyed through composition
- [ ] Mobile optimization maintains visual quality
- [ ] Blacklight reveal system works as overlay
- [ ] All UI elements are touch-friendly (44px minimum)

---

## 🏆 Location Validation Status

### Template Compliance Check:
| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency | ✅ PASS | Debaucheryville, Absinthe Arcade child |
| Cultural Specificity | ✅ PASS | LAN party + arcade culture |
| Satirical Targets Appropriate | ✅ PASS | Gaming nostalgia corruption |
| Seedy Underbelly Present | ✅ PASS | Adult content disguised as maintenance |
| Gameplay Value Established | ✅ PASS | ICQ, achievements, status effects |
| Technical Feasibility | ✅ PASS | Mobile optimized for small space |
| Mobile Performance Budget | ✅ PASS | 45 FPS, 10 draw calls, 25MB |
| Accessibility Features | ✅ PASS | Graffiti always-visible option |
| Social Media Integration | ✅ PASS | SMAAAASH quote is pure gold |

**Once validated, the Claw Machine Maintenance Closet Restroom becomes the ultimate hidden gaming nostalgia corruption experience where players discover their arcade childhood has been repurposed into an adult embarrassment chamber, complete with DDR toilet, claw machine chandelier, SMAAAASH graffiti, and the shame timer reminding them they've achieved nothing but shame, player one!**
