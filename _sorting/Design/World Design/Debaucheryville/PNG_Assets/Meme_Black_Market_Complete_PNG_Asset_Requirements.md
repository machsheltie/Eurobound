# Meme Black Market - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Meme Black Market - where weaponized nostalgia meets underground meme economy, a cursed shrine to early internet degeneracy.

**Location ID:** `debaucheryville_museum_meme_black_market_01`  
**Theme:** Underground meme economy, weaponized nostalgia, early internet worship  
**Primary Function:** Hidden vendor, meme summons, MemeMastery progression, ICQ integration

---

## 🎮 Sprite Sheet 1: Den Environment
**File:** `meme_black_market_den.png`  
**Dimensions:** 1024x768 pixels  
**Color Palette:** #4169E1 (CRT blue), #00FF00 (early internet green), #8B4513 (carpet burn brown)

### Room Base:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Full Den | (0, 0) | 512x384 | RGB-lit cramped back room |
| RGB Lighting Overlay | (512, 0) | 256x192 | Color cycling effect |

### VHS Shelf Door (128x192 each):
| State | Position | Description |
|-------|----------|-------------|
| Closed | (0, 384) | Hidden entrance |
| Opening 1 | (128, 384) | Animation frame |
| Opening 2 | (256, 384) | Animation frame |
| Open | (384, 384) | Revealed passage |

### Windows 98 PC (96x80 each):
| State | Position | Description |
|-------|----------|-------------|
| Startup | (512, 192) | Chime playing |
| Loading | (608, 192) | Progress bar |
| Blue Screen | (704, 192) | BSOD |
| Restart | (800, 192) | Rebooting |

### AIM Shrine:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Base | (512, 272) | 128x112 | Away message display |
| Status On | (640, 272) | 32x32 | Green dot |
| Status Blink | (672, 272) | 32x32 | Flickering |

### Funcoland Bags (48x56 each):
| Bag | Position | Description |
|-----|----------|-------------|
| Bag 1 | (0, 576) | Sacred relic |
| Bag 2 | (48, 576) | Memory cards inside |
| Bag 3 | (96, 576) | Scattered |

### Guy Fieri Shrine:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wig Stand | (144, 576) | 64x80 | Bleached tips |
| Visor | (208, 576) | 48x32 | Guy Fieri signature |

---

## 👤 Sprite Sheet 2: MemeLord.exe Vendor
**File:** `memelord_exe_vendor.png`  
**Dimensions:** 512x384 pixels  

### Character States (96x128 each):
| State | Position | Description |
|-------|----------|-------------|
| Idle | (0, 0) | Half-Adobe Flash runtime |
| Vaping | (96, 0) | Baja Blast cloud |
| Selling | (192, 0) | Transaction mode |
| Prophetic | (288, 0) | Delivering internet wisdom |

### Outfit Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bleached Tips | (0, 128) | 48x48 | Hair detail |
| Guy Fieri Visor | (48, 128) | 56x32 | Essential accessory |
| Fingerless Gloves | (104, 128) | 40x32 | Hacker aesthetic |
| Flash Runtime Overlay | (144, 128) | 96x128 | Digital corruption effect |

### Vape Cloud (64x48 each):
| Puff | Position | Description |
|------|----------|-------------|
| Puff 1 | (0, 176) | Initial exhale |
| Puff 2 | (64, 176) | Expanding |
| Puff 3 | (128, 176) | Drifting |
| Puff 4 | (192, 176) | Dissipating |

### Dialogue Poses (96x128 each):
| Pose | Position | Description |
|------|----------|-------------|
| LimeWire Vengeance | (0, 224) | Intense delivery |
| Hamster Dance Eternal | (96, 224) | Reverent |
| Diamond Hands | (192, 224) | Crypto gesture |

**MemeLord.exe Visual Notes:**
- Half-human, half-Adobe Flash runtime
- Bleached tips, Guy Fieri visor, fingerless gloves
- Vapes exclusively Baja Blast mist (green #00FF7F)
- Text-to-speech quality mixed with Guy Fieri enthusiasm

---

## 🐕 Sprite Sheet 3: Meme Summons
**File:** `meme_summon_sprites.png`  
**Dimensions:** 512x384 pixels  

### Shiba Hype (64x64 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Idle | (0, 0) | Pixelated Shiba |
| Barking | (64, 0) | Motivational quote |
| Motivating | (128, 0) | +Morale effect |

### Dat Boi (64x64 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Appearing | (192, 0) | Entrance |
| Unicycling | (256, 0) | "o shit waddup" |
| Leaving | (320, 0) | Does nothing |

### Dancing Baby (48x64 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Dance 1 | (0, 64) | Classic pose |
| Dance 2 | (48, 64) | Animation |
| Dance 3 | (96, 64) | Animation |
| Dance 4 | (144, 64) | Full loop |

### Rage Comic:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Panel Base | (192, 64) | 96x96 | Classic frame |
| FFFFUUUU | (288, 64) | 64x64 | Rage face |
| Me Gusta | (352, 64) | 64x64 | Alternative |

### Trollface Bomb:
| Frame | Position | Size | Description |
|-------|----------|------|-------------|
| Appearing | (0, 128) | 96x96 | Initial summon |
| Expanding | (96, 128) | 128x128 | Growing |
| Full Screen LULs | (224, 128) | 192x128 | Maximum chaos |

### 🎲 Summon RNG (ported from legacy spec):
- **Dancing Baby.exe:** Cringe backfire effect (if 33% chance triggers)
- **Trollface Bomb:** Party argument effect (if 20% chance triggers, speech bubbles arguing)

---

## 💎 Sprite Sheet 4: Meme Trinkets
**File:** `meme_trinkets.png`  
**Dimensions:** 256x192 pixels  

### XP Ring from eBaum's World:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Icon | (0, 0) | 48x48 | Inventory display |
| Equipped Effect | (48, 0) | 64x64 | Active visual |

### Meatspin NFT (48x48 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Spinning 1 | (0, 48) | Won't stop |
| Spinning 2 | (48, 48) | Still spinning |
| Spinning 3 | (96, 48) | Never stops |
| Spinning 4 | (144, 48) | Eternal curse |
| Won't Stop | (192, 48) | 64x64 expanded |

**CRITICAL:** Meatspin NFT appears automatically, cannot be refused, applies Mentally Unwell status

### Funcoland Futures NFT:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| NFT Card | (0, 96) | 64x96 | #1999 edition |
| Prediction Wrong | (64, 96) | 48x48 | Always incorrect |

---

## 🎨 Sprite Sheet 5: Corrupted GIF Wall
**File:** `corrupted_gif_wall.png`  
**Dimensions:** 512x256 pixels  

### Dancing Banana (48x64 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Frame 1 | (0, 0) | Peanut butter |
| Frame 2 | (48, 0) | Jelly time |
| Corrupted | (96, 0) | Glitched |

### Hamster Dance (64x48 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Frame 1 | (144, 0) | Dee da dee |
| Frame 2 | (208, 0) | Animation |
| Corrupted | (272, 0) | Broken |

### Badger Badger:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Badger | (0, 64) | 64x48 | Badger badger |
| Mushroom | (64, 64) | 48x48 | MUSHROOM |
| Snake | (112, 64) | 64x48 | A snake! |

### Dramatic Chipmunk (64x64 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Looking | (176, 64) | Before turn |
| Dramatic Turn | (240, 64) | DUN DUN |

### Glitch Artifacts (32x32 each):
| Artifact | Position | Description |
|----------|----------|-------------|
| Artifact 1 | (0, 112) | Pixel scramble |
| Artifact 2 | (32, 112) | Color shift |
| Artifact 3 | (64, 112) | Static burst |

---

## 🐱 Sprite Sheet 6: ASCII Cat Guardians
**File:** `ascii_cat_guardians.png`  
**Dimensions:** 256x128 pixels  

### Guardian Cats (64x64 each):
| Guardian | State | Position | Description |
|----------|-------|----------|-------------|
| Guardian 1 | Staring | (0, 0) | Cursed watch |
| Guardian 1 | Tracking | (64, 0) | Eyes follow |
| Guardian 2 | Staring | (128, 0) | Second guardian |
| Guardian 2 | Tracking | (192, 0) | Eyes follow |

### Ductwork Mount:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mount | (0, 64) | 128x48 | Attachment point |

---

## 🎮 Sprite Sheet 7: UI Elements
**File:** `meme_black_market_ui.png`  
**Dimensions:** 384x256 pixels  

### Vendor Menu:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Background | (0, 0) | 256x192 | Menu panel |
| Summon Tab | (0, 192) | 64x32 | Tab button |
| Trinket Tab | (64, 192) | 64x32 | Tab button |

### MemeMastery Meter (128x24 each):
| Stage | Position | Description |
|-------|----------|-------------|
| Empty | (256, 0) | 0% |
| 25% | (256, 24) | Quarter |
| 50% | (256, 48) | Half |
| 75% | (256, 72) | Three quarter |
| Full | (256, 96) | SHITPOSTER SUPREME |

### Status Icons (32x32 each):
| Icon | Position | Description |
|------|----------|-------------|
| Mentally Unwell | (256, 120) | Meatspin curse |
| Cringe | (288, 120) | Dancing Baby backfire |
| Elite Internet User | (320, 120) | XP Ring passive |

### Password Terminal:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| MSN Frame | (128, 192) | 128x64 | Login interface |
| Access Denied | (256, 152) | 96x32 | Lockout display |

### Title Badge:
| Badge | Position | Size | Description |
|-------|----------|------|-------------|
| Shitposter Supreme | (256, 184) | 96x32 | Achievement |

### Achievement Popup Banners (128x48 each) — ported from legacy spec:
- **Shitposter Supreme Unlocked**: Golden banner with meme icons
- **Weaponized Nostalgia Survivor**: Achievement for completing meme economy
- **SWF Vault Access Granted**: Tony420 trading completion
- **Pilsner Embarrassed**: Lord Pilsner internet history discovered

### Password Input UI — ported from legacy spec:
- Text input field showing typed password as asterisks
- "SUBMIT" and "CANCEL" buttons
- Remaining attempts counter (3 tries before lockout)
- Success/failure visual feedback states

---

## ✨ Sprite Sheet 8: Particle Effects
**File:** `meme_market_particles.png`  
**Dimensions:** 256x128 pixels  

### Vape Particles (32x32 each):
| Particle | Position | Description |
|----------|----------|-------------|
| Baja 1 | (0, 0) | Green mist |
| Baja 2 | (32, 0) | Expanding |
| Baja 3 | (64, 0) | Drifting |
| Baja 4 | (96, 0) | Dissipating |

### Pixel Distortion (16x16 each):
| Fragment | Position | Description |
|----------|----------|-------------|
| Fragment 1 | (0, 32) | Static |
| Fragment 2 | (16, 32) | Scramble |
| Fragment 3 | (32, 32) | Glitch |

### RGB Glow (48x24 each):
| Color | Position | Description |
|-------|----------|-------------|
| Red | (0, 48) | Cycling |
| Green | (48, 48) | Cycling |
| Blue | (96, 48) | Cycling |

---

## 🔐 Password Puzzle Elements (ported from legacy spec)
**File:** `password_puzzle_elements.png`
**Dimensions:** 512x384 pixels

The three-step entrance puzzle components:

**GeoCities Kiosk States:**
- **Inactive State**: Dusty touchscreen showing blank screen or screensaver
- **Active 3:33 AM**: Screen lights up with "Under Construction" gifs
- **Under Construction Gif**: Animated construction workers, flashing yellow barriers
- **Pixelated Wizard**: Low-res wizard character appears with message: "PROCEED TO THE MESSENGER OF MICROSOFT"
- **Kiosk Hardware**: Beige plastic casing, visible dust, cracked screen corners

**MSN Messenger Terminal States:**
- **Waiting State**: MSN Messenger login screen, blinking cursor in password field
- **Password Field Active**: User typing, asterisks appearing
- **Success AIM Door**: Green checkmark, AIM door opening sound visual
- **Error Screen**: Red X, error message: "ACCESS DENIED - TRY AGAIN"
- **Terminal Design**: Cracked monitor, sticky keyboard with visible Mountain Dew residue

**VHS Shelf Mechanism (4-frame opening sequence):**
- **Frame 1 - Closed**: Complete wall of VHS tapes labeled "STUFF", "THINGS", "MOVIES MAYBE"
- **Frame 2 - Opening 1**: Shelf begins sliding left, revealing gap with RGB light leaking
- **Frame 3 - Opening 2**: Shelf halfway open, more RGB light visible, Nokia ringtone visual waves
- **Frame 4 - Fully Open**: Complete passage revealed, RGB-lit shrine visible beyond
- **VHS Tape Details**: Handwritten labels, various tape conditions, authentically scattered

**Environmental Puzzle Details:**
- Worn stone stairs visible through open VHS shelf
- RGB LED light bleeding around shelf edges when opening
- Nokia ringtone represented by visual sound waves
- Cold air effect particles (blue mist) emanating from opening

**Password Puzzle Sequence:**
- GeoCities activation: Instant on correct time (3:33 AM)
- MSN terminal typing: Real-time player input
- VHS shelf opening: 3-second mechanical sliding animation
- Remaining attempts counter (3 tries before lockout)

---

## 🖥️ Windows 98 Crash Loop (ported from legacy spec — no BASE equivalent)
**File:** `windows_98_crash_loop.png`
**Dimensions:** 384x256 pixels

The eternal digital samsara display:

**Crash Sequence Animation (4 states):**
- **State 1 - Startup Chime Screen**: Windows 98 logo with loading bar
- **State 2 - Loading Windows**: Blue sky with clouds background, progress continuing
- **State 3 - Blue Screen of Death**:
  - Error text: "FATAL ERROR: EXISTENCE"
  - Additional text: "A problem has been detected and Windows has achieved digital samsara"
  - "Press any key to continue suffering"
- **State 4 - Restart Loop**: Black screen with "Restarting..." then back to State 1

**Desktop PC Physical Details:**
- **Beige Case**: Yellowed beige plastic showing age and UV damage
- **Dust Layer**: Thick visible dust accumulation (years of operation)
- **Power LED**: Green LED blinking in rhythm with crash cycle
- **Floppy Drive**: Visible 3.5" floppy drive (authenticity detail)
- **CD-ROM Tray**: Partially ejected, stuck in that position forever

**Philosophical Error Messages:**
- "The startup chime plays for the 47,000th time today"
- "It will never stop. It will never learn."
- "This computer has achieved digital samsara."
- Error code: "0x00000000EXISTENCE_IS_SUFFERING"

**Environmental Placement:**
- Corner position showing it's been running since 2003
- Cables trailing off into darkness
- Small pile of ancient floppy disks nearby
- Coffee mug ring stains on case

---

## 🎬 Animation Specifications

### VHS Shelf Opening:
- **Pattern:** Closed → Opening 1 → Opening 2 → Open
- **Duration:** 3 seconds total
- **FPS:** 4
- **Audio:** vhs_slide_open.wav

### Windows 98 Crash Loop:
- **Pattern:** Startup → Loading → Blue Screen → Restart (loop)
- **Cycle Duration:** 8 seconds
- **Purpose:** Endless suffering visualization

> ⚠ CONFLICT: legacy spec says Windows 98 crash is a 15-second full cycle (startup → crash → restart) — author to decide.

### MemeLord.exe Vaping:
- **Pattern:** Idle → Vaping → Idle
- **Trigger:** Every 15-30 seconds
- **Vape Duration:** 3 seconds
- **Particle:** Baja Blast cloud spawns

> ⚠ CONFLICT: legacy spec says vaping is an 8 FPS continuous loop, vape cloud persistence 5 seconds per exhale, "never stops vaping (character life support system)" — author to decide.

### ASCII Cat Tracking:
- **Pattern:** Staring → Eyes Tracking → Staring
- **Idle Duration:** Random 10-20 seconds
- **Tracking Duration:** 2 seconds
- **Trigger:** Player movement

### Meatspin Curse:
- **Pattern:** Spinning 1 → 2 → 3 → 4 (loop)
- **FPS:** 8
- **Special:** WON'T STOP

### Corrupted GIF Cycle:
- **Pattern:** Varied per gif
- **FPS:** 4
- **Glitch:** Random corruption overlay triggers

### Animation Timing Requirements (ported from legacy spec):

**MemeLord.exe Vaping Idle:**
- 8 FPS continuous loop
- Vape cloud persistence: 5 seconds per exhale
- Never stops vaping (character life support system)

**Meme Summon Timings:**
- Shiba Hype: 2.5 seconds total (appears, barks 3x, exits)
- Dat Boi: 1.5 seconds total (unicycles across screen)
- Dancing Baby: 3 seconds total (dance sequence + confusion effect)
- Trollface Bomb: 2 seconds buildup + 1 second explosion

**Password Puzzle Sequence:**
- GeoCities activation: Instant on correct time (3:33 AM)
- MSN terminal typing: Real-time player input
- VHS shelf opening: 3-second mechanical sliding animation

**Environmental Loops:**
- Windows 98 crash: 15-second full cycle (startup → crash → restart)
- Nokia ringtone: 8-second loop continuously
- ASCII cat eyes: 6 FPS tracking animation
- RGB LED pulse: 10 FPS color cycling

---

## 🔊 Audio Synchronization Points

**Critical Audio-Visual Sync Requirements:**

1. **VHS Shelf Opening**: Mechanical grinding sound syncs with frame 1, Nokia gets louder each frame
2. **Meme Summons**: Each summon has signature sound (Shiba bark, "o shit waddup", baby sounds, trollface chaos)
3. **Windows 98 Crash**: Startup chime → loading sounds → error sound → restart beep perfectly timed
4. **MemeLord.exe Vaping**: Continuous hiss sound follows vape cloud animation
5. **Password Success/Failure**: AIM door slam or Windows error chord at exact feedback moment
6. **Meatspin Curse**: Ominous spinning sound begins immediately when NFT acquired

---

## ⚡ Performance Specifications

**Frame Rate Target:** 50 FPS  
**Memory Footprint:** 42MB maximum  
**Draw Calls:** Maximum 18  
**Mobile Optimization:**
- Simplified CRT flicker effects on older devices
- Reduced vape particle count (60% reduction on medium, 90% on low)
- Static RGB lighting on low-end hardware
- Potato mode: Basic sprites, no particles, static lighting

---

## 📦 File Delivery Checklist

### Required PNG Files (8 Total):
- [ ] `meme_black_market_den.png` (1024x768)
- [ ] `memelord_exe_vendor.png` (512x384)
- [ ] `meme_summon_sprites.png` (512x384)
- [ ] `meme_trinkets.png` (256x192)
- [ ] `corrupted_gif_wall.png` (512x256)
- [ ] `ascii_cat_guardians.png` (256x128)
- [ ] `meme_black_market_ui.png` (384x256)
- [ ] `meme_market_particles.png` (256x128)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha |
| Color Space | sRGB |
| DPI | 72 |
| Naming | snake_case |
| Compression | Lossless PNG compression |
| Layer Organization | Preserve layer structure for future edits |

### Delivery Format (ported from legacy spec):
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/Photoshop files with organized layer groups
- **Documentation:** Layer naming guide for future updates

---

## 📝 In-World Text Strings (ported from legacy spec)

### AIM Away Message Wall:
- Three message panels backlit like stained glass windows:
  - Panel 1: "brb pizza rolls" / "out laterz" / "if u can read this ur 2 close"
  - Panel 2: "brb crying to dashboard confessional" / "away: living my best life (jk dying inside)"
  - Panel 3: "idle: 47 minutes" (meditation on impermanence)

### Funcoland Receipts and Bag Labels:
- Bags labeled with tragic trade-in values: "$0.78 for 12 games", "Your childhood, appraised"
- Trade-in receipts showing: "Trade-in value: $1.10. Store credit: $1.47"
- One receipt visible: "47 cartridges = 1 gum wrapper"

### BSOD Text:
- Error text: "FATAL ERROR: EXISTENCE"
- Additional text: "A problem has been detected and Windows has achieved digital samsara"
- "Press any key to continue suffering"
- Error code: "0x00000000EXISTENCE_IS_SUFFERING"

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **MemeLord.exe** - Bleached tips, visor, vape cloud
2. **VHS Shelf Opening** - Hidden entrance reveal
3. **Trollface Bomb** - Full screen LULs
4. **Meatspin NFT** - Won't stop spinning
5. **ASCII Cat Guardians** - Eyes tracking
6. **MemeMastery Full** - Shitposter Supreme

### Quote Potential:
- "Warning: I run on LimeWire and vengeance."
- "Hamster Dance is eternal, peasant."
- "My soul is encoded in Winamp skins and guilt."
- "Funcoland offered me $1.10 for my soul and two PS2 controllers."
- "I got diamond hands and zero liquidity, baby."

---

## 🎨 Art Direction Summary (ported from legacy spec)

### Visual Aesthetic:
- **Primary Theme:** "Early 2000s internet culture as religious shrine"
- **Color Mood:** CRT blue, Baja Blast green, RGB neon, carpet burn brown
- **Lighting:** Flickering CRT glow with RGB LED accents creating nostalgic atmosphere
- **Texture:** Dusty screens, sticky keyboards, old carpet, Funcoland bag plastic

### MemeLord.exe Character Direction:
- **Personality:** Prophetic reverence for internet garbage, dramatic delivery of meme wisdom
- **Key Visual:** Half-human, half-corrupted Flash runtime with continuous Baja Blast vaping
- **Movement:** Confident vendor stance with occasional Flash error glitches
- **Expression:** Dramatic intensity treating worthless memes as sacred artifacts

### Meme Summon Design Philosophy:
- Each summon maintains authentic early internet aesthetic
- Low-resolution, poor quality is intentional and sacred
- Visual effects range from "does nothing" to "screen-filling chaos"
- Psychological damage is a feature, not a bug

### Environmental Storytelling:
- Every element reinforces "frozen moment from 2003"
- Funcoland bags represent economic trauma (predatory trade-ins)
- Windows 98 crash represents futility and eternal loops
- ASCII cats as silent guardians judging all who enter
- AIM away messages as sacred devotional texts

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
| Mobile Performance | ✅ PASS (50 FPS, 18 draws, 42MB) |
| Accessibility | ✅ PASS |
| Social Media | ✅ PASS |

**The Meme Black Market becomes the essential underground economy hub where MemeLord.exe sells psychological damage as sacred artifacts, Meme Summons provide battle variety, the MemeMastery Meter tracks addiction progression, and the Meatspin NFT appears whether you want it or not (you don't)!**
