# Velvet Curtain Club VIP Stall - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_velvetcurtain_vipstall_bathroom_01`
- **Authoritative slug:** `velvet_curtain_club_vip_stall`
- **Engine:** Godot 4.7
- **Pipeline:** Painterly HD-2D painted faces, depth cards, billboard/cutout props, emission masks and state overlays
- **Visual target:** A tiny velvet-lined toilet trying to perform luxury through stains, RGB shimmer and crypto graffiti.

## Resolution and Frame Layout

Every required PNG uses one of these production classes; do not infer canvas size from the visible subject:

| Asset role | Resolution class | Frame layout |
|---|---:|---|
| Exterior, threshold or full interior scene plate | 2048x1152 px | Single 16:9 frame; provide clean plate and separate depth cards |
| Node or landmark cutout | 1024x1024 px | Single transparent frame with 8 px safe padding |
| NPC or creature animation | 2048x512 px | Four 512x512 cells in one row: idle, talk, react, service/combat; 8 fps unless mapping overrides |
| Item, reward or inventory icon | 256x256 px | Single transparent frame with 16 px safe area |
| UI atlas | 2048x1024 px | Power-of-two atlas; label frame rectangles in delivery manifest |
| FX atlas | 2048x2048 px | 8x8 grid of 256x256 cells; unused cells transparent |
| Emission/occlusion mask | Match its source asset exactly | One grayscale mask per source frame; preserve frame order |

## Spatial Composition

1. **Inside VIP Curtain** — Interior side of the STAFF ONLY curtain.
2. **Velvet Fixture** — Stained black-velvet toilet seat and chipped champagne holder.
3. **Selfie-Cam Mirror** — Overhead mirror with CryptoQueen filter.
4. **QR Code Graffiti** — The Millennium Bug (Mint #00) QR code graffiti, on the wall from the start; scanning plays the highlight glow, scan beep and success chime.
5. **Crypto Graffiti Wall** — ROI jokes, Fistø lore and DO NOT LOOK AT THE BABY clue.
6. **Club Return Curtain** — Returns to Velvet Curtain Club.

## Required PNG Assets

Painted layers are built per role as day and night variants, plus a day front elevation for exteriors, under `game/assets/worlds/debaucheryville/velvet_curtain_club_vip_stall/exterior/` and `.../interior/`; files marked *not built yet* follow the same naming (Eurobound-z50s).

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `velvet_curtain_club_vip_stall_exterior` | `velvet_curtain_club_vip_stall_ext_day.png`, `velvet_curtain_club_vip_stall_ext_night.png`, `velvet_curtain_club_vip_stall_ext_front_elevation_day.png` (not built yet) | exterior/threshold painted layer | `vcs_inside_curtain` |
| `velvet_curtain_club_vip_stall_interior` | `velvet_curtain_club_vip_stall_int_day.png`, `velvet_curtain_club_vip_stall_int_night.png` | interior/service footprint | `vcs_fixture` |
| `velvet_curtain_club_vip_stall_node_vcs_fixture` | `velvet_curtain_club_vip_stall_vcs_fixture.png` | interaction landmark | `vcs_fixture` |
| `velvet_curtain_club_vip_stall_node_vcs_selfie_mirror` | `velvet_curtain_club_vip_stall_vcs_selfie_mirror.png` | interaction landmark | `vcs_selfie_mirror` |
| `velvet_curtain_club_vip_stall_node_vcs_qr_graffiti` | `velvet_curtain_club_vip_stall_vcs_qr_graffiti.png` | quest landmark | `vcs_qr_graffiti` |
| `velvet_curtain_club_vip_stall_node_vcs_graffiti` | `velvet_curtain_club_vip_stall_vcs_graffiti.png` | lore landmark | `vcs_graffiti` |
| `velvet_curtain_club_vip_stall_node_vcs_exit` | `velvet_curtain_club_vip_stall_vcs_exit.png` | exit landmark | `vcs_exit` |
| `velvet_curtain_club_vip_stall_item_item_nft_millennium_bug` | `velvet_curtain_club_vip_stall_item_nft_millennium_bug.png` | item/service icon | global |
| `velvet_curtain_club_vip_stall_item_vcs_spite_reserve` | `velvet_curtain_club_vip_stall_vcs_spite_reserve.png` | item/service icon | global |
| `velvet_curtain_club_vip_stall_item_vcs_nft_affinity` | `velvet_curtain_club_vip_stall_vcs_nft_affinity.png` | item/service icon | global |
| `velvet_curtain_club_vip_stall_ui` | `velvet_curtain_club_vip_stall_ui.png` | interaction/status UI | global |
| `velvet_curtain_club_vip_stall_fx` | `velvet_curtain_club_vip_stall_fx.png` | environmental FX | global |
| `velvet_curtain_club_vip_stall_masks` | `velvet_curtain_club_vip_stall_masks.png` | emission/occlusion masks | global |

## State and Character Coverage

- No resident named NPC; parent-side gatekeepers remain in the parent package.
- `velvet_vip_stall_access_unlocked`: provide a readable base/change indicator where visually applicable.
- `millennium_bug_obtained`: provide a readable base/change indicator where visually applicable.
- `meme_black_market_graffiti_clue_read`: provide a readable base/change indicator where visually applicable.
- `vip_stall_fisto_lore_read`: provide a readable base/change indicator where visually applicable.
- `nft_affinity_protection_active`: provide a readable base/change indicator where visually applicable.

## Accessibility Assets

- Static RGB alternative.
- Base QR remains visible through status overlays.
- Text selfie-filter description.
- Reduced champagne drip.
- Clean plates beneath fog, smoke, particles, glare and distortion.
- Text/icon equivalents for audio, timing and color-only cues.

## Delivery Checklist

- [ ] Every asset ID appears in `sprite_mapping/velvet_curtain_club_vip_stall_sprite_mapping.json`.
- [ ] Every interactive landmark includes base, unavailable and completed states.
- [ ] Parent/child transition art stops at the ownership boundary.
- [ ] Transparent assets use clean alpha and 8 px atlas padding.
- [ ] Painted faces include emission/normal-ready variants where required.

---

## Legacy sprite-sheet detail (folded in 2026-11-12, Eurobound-x0c; HD-2D sheet above is the spec of record)

> Folded in verbatim from the former `velvet_curtain_club_vip_stall_png_asset_requirements.md`. Where anything in this section contradicts the HD-2D sheet above, the HD-2D sheet wins.

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Velvet Curtain Club VIP Stall. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this hyper-exclusive regret shrine where tech bro sponsorship meets toilet-papered luxury.

**Location ID:** `debaucheryville_velvetcurtain_vipstall_bathroom_01`
**Theme:** Hyper-exclusive regret meets toilet-papered luxury — a shrine to everyone who peaked during the 2017 crypto bull run
**Zone:** Velvet Curtain Club — behind the "Staff Only" red velvet curtain
**Hours:** Club hours (20:00–04:00 game time), while the main club is open
**Primary Function:** NFT discovery location & Fistø lore node — Bravado-gated entry past buffed bouncers, "The Millennium Bug (Mint #00)" QR code graffiti, drunk/hungover state-dependent graffiti content, NFT Affinity protection buff

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Gold | #FFD700 | Trim, graffiti spray paint, gold-flake luxury pretension |
| Black Velvet | #1C1C1C | Toilet seat plush, dark accent surfaces |
| Champagne | #F7E7CE | Drip overlays, bubble particles, ceiling fixture glow |
| RGB Shimmer Cyan | #00FFFF | LED shimmer synced to club bass drops |
| Red Velvet | #DC143C | "Staff Only" curtain, failure UI states |
| Kebab Orange | #FF6B35 | Hungover pixel kebab icon glow |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/velvetcurtain/
├── vip_stall_bathroom_complete.png
├── vip_stall_graffiti_interactive.png
├── vip_bathroom_access_elements.png
├── vip_stall_status_effects.png
└── vip_stall_ui_elements.png
```

---

## 🎨 Sprite Sheet 1: VIP Stall Environment Complete
**File:** `vip_stall_bathroom_complete.png`  
**Dimensions:** 512x384 pixels  
**Color Palette:** #FFD700 (gold), #1C1C1C (black velvet), #F7E7CE (champagne), #00FFFF (RGB shimmer)

### Black Velvet Toilet Components:
- **Velvet-Lined Seat** (0, 0, 48x64) - Deeply stained, impossibly plush texture
- **Toilet Base with Gold Trim** (48, 0, 48x64) - Luxury toilet structure
- **Velvet Texture Detail** (96, 0, 32x32) - Close-up plush material
- **Gold Accent Trim** (128, 0, 16x16) - Decorative piping

### Champagne Holder System:
- **Wall-Mounted Holder** (0, 64, 32x48) - Chipped faux-brass mount
- **Moët 2003 Bottle** (32, 64, 16x48) - Half-empty champagne bottle
- **Champagne Glass Position** (48, 64, 16x24) - Resting placement
- **Holder Chip Detail** (64, 64, 16x16) - Visible damage

### Ceiling Fixture:
- **Champagne Flute Light Base** (0, 112, 64x96) - Art deco styling
- **Ambient Glow Effect** (64, 112, 64x96) - Subtle golden illumination
- **Fixture Detail** (128, 112, 32x48) - Decorative elements

### Floor and Wall Textures:
- **Marble-Look Tile** (0, 208, 128x64) - Glitter Mod Podge surface
- **Gold Flake Details** (128, 208, 64x32) - Scattered throughout
- **Cracked Tile Section** (192, 208, 32x32) - Floor set dressing
- **Wall Texture Base** (224, 208, 96x64) - Bathroom wall material

### Technical Notes:
- Velvet texture suggests luxury despite obvious staining
- Champagne holder shows wear revealing faux-brass finish
- Ceiling fixture provides ambient bathroom glow
- Cracked tile is floor set dressing; The Millennium Bug QR is graffiti (Sprite Sheet 2)

---

## 📱 Sprite Sheet 2: VIP Stall Graffiti & Interactive Elements
**File:** `vip_stall_graffiti_interactive.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #FFD700 (gold spray paint), #000000 (black marker), #F7E7CE (champagne drip)

### Primary Graffiti Phrases:
- **"ROI = Regret On Investment"** (0, 0, 128x24) - Large, prominent wall text
- **"I BLEW IT… literally"** (128, 0, 96x24) - Medium, center positioning
- **"Buy Low, Cry High"** (224, 0, 80x24) - Small, sardonic wisdom
- **Velvet DAO QR Code Text** (304, 0, 96x16) - "Scan for Velvet DAO Invite (Not a Scam, Probably)"

### Secondary Graffiti Elements:
- **Scribbled Startup Ideas** (0, 24, 128x32) - Illegible but recognizable doodles
- **@ Social Media Handles** (128, 24, 96x16) - Various handle scratches
- **Altcoin Pump Schemes** (224, 24, 128x32) - Diagram doodles
- **Tech Bro Quotes Gone Wrong** (352, 24, 96x32) - Motivational failures

### QR Code System:
- **QR Code The Millennium Bug (Mint #00)** (96, 56, 32x32) - "The Millennium Bug" QR code graffiti, on the wall from the start (no reveal frames; author, Production Desk `Eurobound-222-q1`)
- **Scanning Highlight Glow** (128, 56, 32x32) - Interactive effect; plays on scan with the scan beep and success chime

### Tech Bro Sponsorship Plaque:
- **Faux-Brass Plaque Base** (0, 88, 128x48) - Tarnished finish
- **Plaque Text Detail** (128, 88, 128x48) - "VIP Stall generously sponsored by Tech Bros Who Can't Hold Their Liquor"
- **Mounting Screws** (256, 88, 8x8) - Installation details

### Approach Trail Elements:
- **Glitter Scatter Pattern** (0, 136, 96x24) - Floor leading to entrance
- **Lip Gloss Smear Detail** (96, 136, 48x16) - Trail markers
- **Expired Wristband Props** (144, 136, 32x16) - Scattered evidence

### Technical Notes:
- Graffiti uses varied handwriting styles for authenticity
- QR code graffiti reveals The Millennium Bug (Mint #00)
- Tech bro plaque is satirical centerpiece
- Approach trail creates visual breadcrumb path

---

## 🚪 Sprite Sheet 3: VIP Bathroom Access System
**File:** `vip_bathroom_access_elements.png`  
**Dimensions:** 384x256 pixels  
**Color Palette:** #DC143C (red velvet), #FFD700 (faux-brass), #708090 (bouncer grey)

### Staff Only Curtain:
- **Red Velvet Curtain Closed** (0, 0, 64x96) - Initial entrance state
- **Cracked "STAFF ONLY" Embroidery** (64, 0, 64x96) - Text detail visible
- **Curtain Parting Frame 1** (128, 0, 64x96) - Bravado check success start
- **Curtain Parting Frame 2** (192, 0, 64x96) - Mid-open animation
- **Curtain Fully Open** (256, 0, 64x96) - Entrance revealed

### Buffed-Out Bouncers:
- **Bouncer Left Stance** (0, 96, 64x96) - Intimidating guard pose
- **Bouncer Right Stance** (64, 96, 64x96) - Mirror intimidation
- **Bravado Check Sizing Up** (128, 96, 64x96) - Assessment animation
- **Arms Crossed Idle** (192, 96, 64x96) - Standard guard position

### Selfie-Cam Mirror:
- **Mirror Base with Frame** (0, 192, 64x96) - Bathroom mirror structure
- **"#CryptoQueen" Filter Overlay** (64, 192, 64x64) - Selfie filter effect
- **Camera Flash Effect** (128, 192, 48x48) - Photo capture visual
- **Selfie Preview Frame** (176, 192, 48x64) - Player preview

### Technical Notes:
- Curtain parting requires Bravado stat check success
- Bouncers flank entrance creating intimidation factor
- Selfie-cam mirror adds social media satire layer
- Filter overlay appears when player approaches mirror

---

## ✨ Sprite Sheet 4: Drunk & Hungover Visual Effects
**File:** `vip_stall_status_effects.png`  
**Dimensions:** 256x256 pixels  
**Color Palette:** #F7E7CE (champagne), #FFD700 (bubble gold), #FF6B35 (kebab orange)

### Champagne Drip Animation (Drunk State):
- **Text Drip Frame 1** (0, 0, 128x96) - Drip starting on graffiti
- **Text Drip Frame 2** (128, 0, 128x96) - Mid-drip cascade
- **Text Drip Frame 3** (0, 96, 128x96) - Full drip effect
- **Drip Return** (128, 96, 128x96) - Return to base state

### Champagne Bubble Particles:
- **Bubble Small Rising 1** (0, 192, 12x12) - Small bubble frame 1
- **Bubble Small Rising 2** (12, 192, 12x12) - Small bubble frame 2
- **Bubble Medium** (24, 192, 16x16) - Medium bubble particle
- **Bubble Large** (40, 192, 20x20) - Large bubble particle
- **Bubble Pop Effect** (60, 192, 24x24) - Burst animation

### Pixel Kebab Icon (Hungover State):
- **Kebab Icon Glow Frame 1** (84, 192, 24x24) - Dim glow
- **Kebab Icon Glow Frame 2** (108, 192, 24x24) - Medium glow
- **Kebab Icon Glow Frame 3** (132, 192, 24x24) - Bright glow pulse
- **Kebab Icon Position Marker** (156, 192, 8x8) - Placement indicator

### Graffiti Enhancement Effects:
- **Enhanced Glow Drunk** (0, 216, 64x40) - Graffiti appears luxurious
- **Champagne Color Tint** (64, 216, 64x40) - Golden overlay
- **Shimmer Effect** (128, 216, 48x40) - Text sparkle when drunk

### Fistø Lore Visual:
- **Text Box for Lore** (176, 192, 80x64) - Display frame
- **Greasy Aesthetic Border** (176, 216, 80x40) - Kebab-themed frame

### Technical Notes:
- Champagne drip only appears when player has Drunk status
- Pixel kebab icon only appears when player has Hungover status
- Each status effect has unique visual enhancement
- Effects make graffiti interactive based on player state

---

## 🎮 Sprite Sheet 5: VIP Stall UI Elements
**File:** `vip_stall_ui_elements.png`  
**Dimensions:** 384x192 pixels  
**Color Palette:** #FFD700 (gold), #00FF00 (success green), #DC143C (failure red)

### Bravado Gate UI:
- **Bravado Check Display** (0, 0, 96x32) - Stat requirement indicator
- **Bouncer Sizing Up Animation** (96, 0, 64x48) - Assessment visual
- **Access Granted Checkmark** (160, 0, 48x32) - Success indicator
- **Access Denied X** (208, 0, 48x32) - Failure indicator

### NFT Discovery UI:
- **"Check VIP Bathroom" Hint** (0, 48, 96x32) - Location clue
- **"Scan Graffiti QR Code" Prompt** (96, 48, 128x32) - Interaction instruction
- **The Millennium Bug (Mint #00) Acquired Popup** (224, 48, 160x48) - "The Millennium Bug" collected
- **QR Scan Success Effect** (0, 96, 64x32) - Confirmation visual

### Status Effect Indicators:
- **Drunk State Icon** (64, 96, 32x32) - Champagne glass symbol
- **Hungover State Icon** (96, 96, 32x32) - Kebab symbol
- **NFT Affinity Protection** (128, 96, 32x32) - Buff shield icon

### Achievement Popups:
- **"VIP Access Granted"** (0, 128, 128x48) - First bathroom entry
- **"The Millennium Bug (Mint #00) Discovered"** (128, 128, 128x48) - Collectible found
- **"Greasy Prophet Progress"** (256, 128, 128x48) - Fistø lore contribution

### Interaction Prompts:
- **"Approach Staff Only Curtain"** (0, 176, 96x16) - Entrance prompt
- **"Read Graffiti"** (176, 176, 64x16) - Interaction option
- **"Use Selfie Mirror"** (240, 176, 80x16) - Photo opportunity

### Technical Notes:
- Bravado check UI clearly communicates stat gate requirement
- NFT discovery prompts guide player to QR code location
- Status effect icons indicate drunk/hungover visual changes
- Achievement popups celebrate milestone discoveries

---

## 📱 Performance & Assets Requirements

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.7 import) for RGB shimmer and champagne effects with alpha for bubble particle transparency
- **Fallback:** PNG high quality for graffiti text readability

### Sprite Atlasing Strategy:
- **Bathroom Environment Atlas:** Toilet + champagne holder + ceiling + textures (512x384)
- **Graffiti Interactive Atlas:** All graffiti + QR code + plaque + trail (512x256)
- **Access System Atlas:** Curtain + bouncers + selfie mirror (384x256)
- **Status Effects Atlas:** Drunk champagne + hungover kebab + overlays (256x256)
- **UI Elements Atlas:** Bravado gate + NFT discovery + achievements (384x192)
- **Max Atlas Size:** 2048x2048 for broad GPU compatibility

### LOD (Level of Detail) Scaling:
- **High-End Devices:** Full RGB shimmer, all drunk/hungover effects, champagne drip animation
- **Medium Devices:** Reduced shimmer complexity, simplified bubble particles, basic overlays
- **Low-End Devices:** Static graffiti glow, minimal particle effects, no RGB shimmer
- **Potato Mode:** Essential bathroom layout, static graffiti, no status visual enhancements

### Performance Targets:
- **Target FPS:** 60 fps (RGB shimmer and status effect overlays)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 35MB maximum for location

---

## ♿ Accessibility Sprite Requirements

### High Contrast Graffiti:
- **Enhanced Text Visibility** (0, 0, 128x96) - Clear readability against wall
- **Colorblind-Friendly Glow** (128, 0, 64x48) - Pattern-based not just color
- **High Contrast QR Code** (192, 0, 32x32) - Enhanced scanability

### Motion Sensitivity Options:
- **Reduced RGB Shimmer** (0, 48, 96x64) - Minimal flicker alternative
- **Static Graffiti** (96, 48, 128x64) - No glow animation
- **Gentle Bubble Float** (224, 48, 48x64) - Slower particle movement

### Visual Audio Cues:
- **QR Scan Beep Visual** (48, 112, 32x32) - Audio-independent indicator
- **Champagne Fizz Visual** (80, 112, 48x48) - Bubble sound representation

### High Contrast UI:
- **Bravado Check Outline** (0, 160, 96x32) - Enhanced stat gate visibility
- **NFT Discovery Emphasis** (96, 160, 96x32) - Clear collectible indication

---

## 🎬 Animation Sequence Specifications

### Champagne Drip Text Overlay (Drunk State):
- **Duration:** 3-frame cycle, 2.0 seconds total (10 fps)
- **Trigger:** Player has Drunk status + viewing bathroom graffiti
- **Pattern:** Text Start Drip → Mid-Drip → Full Drip → Return
- **Particle:** Champagne bubbles float upward continuously
- **Purpose:** Drunk vision makes graffiti appear luxurious

### Pixel Kebab Icon Glow (Hungover State):
- **Duration:** 3-frame pulse, 1.5 seconds total (12 fps)
- **Trigger:** Player has Hungover status + viewing bathroom graffiti
- **Pattern:** Dim Glow → Medium Glow → Bright Pulse → Return
- **Effect:** Icon appears near specific graffiti text
- **Purpose:** Reveals Fistø lore snippet when hungover

### QR Code Graffiti Scan:
- **No reveal animation:** the QR code graffiti is on the wall from the start (author, Production Desk `Eurobound-222-q1`)
- **Trigger:** Player scans the QR code graffiti
- **Effect:** Existing Scanning Highlight Glow (Sprite Sheet 2)
- **Audio:** Existing QR scan beep, then the success chime
- **Purpose:** The Millennium Bug (Mint #00) discovery mechanic

### Staff Only Curtain Parting:
- **Duration:** 3-frame sequence, 1.5 seconds total (10 fps)
- **Trigger:** Player passes Bravado check
- **Pattern:** Closed → Parting Start → Mid-Open → Fully Open
- **Audio:** Curtain swoosh, bouncer grunt approval
- **Purpose:** VIP bathroom access granted animation

### RGB LED Shimmer (Continuous):
- **Duration:** Variable, continuous bass-synced effect
- **Pattern:** Cyan → Magenta → Yellow → Mixed → Repeat
- **Intensity:** Erratic flicker matching club music bass
- **Purpose:** Nightclub atmosphere bleeding into bathroom

### Selfie Mirror Flash:
- **Duration:** Single frame flash, 0.2 seconds
- **Trigger:** Player interacts with selfie mirror
- **Effect:** Camera flash + "#CryptoQueen" filter overlay
- **Audio:** Camera shutter click
- **Purpose:** Social media satire photo opportunity

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Animation system: Frame-based with JSON timing data
- Stat gate system: Bravado check for bathroom access
- NFT discovery: QR code interaction mechanics
- Status-based visuals: Drunk/Hungover conditional rendering

### Audio Sync Points:
- QR scan beep plays with the scanning highlight glow; success chime on The Millennium Bug discovery
- Champagne fizz plays with bubble particles
- Curtain swoosh matches parting animation
- Selfie mirror shutter click on flash frame
- RGB shimmer hum continuous ambient

### Quest Integration:
- **NFT Hunt:** Bathroom QR code graffiti reveals "The Millennium Bug (Mint #00)"
- **Fistø Lore:** Hungover graffiti contributes to "The Greasy Prophet" title
- **Couchsurfing:** References broader Velvet Curtain Club system
- **ICQ System:** CryptoMamiXXX messages mock bathroom access

### Cross-Location Dependencies:
- **Velvet Curtain Club:** Must enter main club before VIP bathroom access
- **Bravado Stat:** Required for bouncer bypass (separate from Charisma club entry)
- **NFT Network:** Bathroom discovery links to 3 NFT collection quest
- **Status Effects:** Drunk and Hungover unlock different content

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Hyper-exclusive regret meets toilet-papered luxury"
- **Color Mood:** Gold excess, black velvet pretension, champagne nostalgia, RGB shimmer chaos
- **Lighting:** Champagne flute ceiling fixture, RGB LED shimmer, selfie-cam flash
- **Texture:** Glitter Mod Podge "marble," velvet staining, faux-brass tarnish

### Satirical Design Philosophy:
- **Tech Bro Sponsorship:** Bathroom financed by those "Who Can't Hold Their Liquor"
- **Crypto Graffiti:** "ROI = Regret On Investment" predicts financial ruin
- **VIP Access Absurdity:** Bravado required to enter toilet stall
- **NFT Discovery Irony:** Collectible mocking NFT culture hidden in bathroom

### Environmental Storytelling:
- Glitter Mod Podge reveals fake marble luxury
- Champagne from 2003 aged like crypto portfolios
- Graffiti literally warns "I BLEW IT" while bros ignore
- Tech bro plaque admits sponsor incompetence
- VIP bathroom as shrine to 2017 bull run nostalgia

---

## 📋 Required PNG Files (5 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | vip_stall_bathroom_complete.png | 512x384 |
| 2 | vip_stall_graffiti_interactive.png | 512x256 |
| 3 | vip_bathroom_access_elements.png | 384x256 |
| 4 | vip_stall_status_effects.png | 256x256 |
| 5 | vip_stall_ui_elements.png | 384x192 |

**Total Estimated Memory:** ~2.3 MB uncompressed RGBA (comfortably within the 35MB location footprint)

---

## 📦 File Delivery Checklist

### Required PNG Files (5 Total):
- [ ] `vip_stall_bathroom_complete.png` (512x384)
- [ ] `vip_stall_graffiti_interactive.png` (512x256)
- [ ] `vip_bathroom_access_elements.png` (384x256)
- [ ] `vip_stall_status_effects.png` (256x256)
- [ ] `vip_stall_ui_elements.png` (384x192)

### Quality Requirements:
- **Format:** PNG-24 with alpha channel
- **Color Space:** sRGB
- **DPI:** 72 (screen resolution)
- **Compression:** Lossless PNG
- **Naming Convention:** snake_case, all lowercase
- **Layer Organization:** Preserve for drunk/hungover overlay updates

### Delivery Format:
- **Primary:** Individual PNG files per specifications
- **Backup:** Master PSD/Photoshop with organized layer groups
- **Documentation:** Status effect timing sheet, Bravado gate guide

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Tech Bro Sponsorship Plaque** - Admitting liquor incompetence
2. **"ROI = Regret On Investment" Graffiti** - Crypto wisdom
3. **Champagne Drip Overlay (Drunk)** - Making graffiti look luxurious
4. **Pixel Kebab Icon (Hungover)** - Fistø lore revelation
5. **#CryptoQueen Selfie Filter** - Social media satire

### TikTok Potential:
- "POV: You paid Bravado to access VIP bathroom (it's a toilet with graffiti)"
- "Reading crypto graffiti drunk vs hungover comparison"
- "The Millennium Bug (Mint #00) discovery in bathroom stall reaction"
- "Tech bros sponsored this bathroom and admitted they can't hold liquor"

### Twitter/X Quote Potential:
- "ROI = Regret On Investment" - VIP Stall wisdom
- "VIP Stall generously sponsored by Tech Bros Who Can't Hold Their Liquor" - Plaque
- "I BLEW IT… literally" - Bathroom graffiti
- "Woke up here with champagne rash and a cease & desist from my liver." - Fistø

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 5 PNG files match exact dimensions
- [ ] Black velvet toilet shows luxury despite staining
- [ ] Graffiti includes all crypto commentary phrases
- [ ] Tech bro sponsorship plaque text fully readable
- [ ] QR code graffiti visible from the start, no reveal frames; scan plays highlight glow, scan beep and success chime
- [ ] Champagne drip overlay works with drunk status
- [ ] Pixel kebab icon appears with hungover status
- [ ] RGB shimmer flicker erratic but not nauseating
- [ ] Buffed bouncers flanking curtain intimidating
- [ ] Selfie mirror "#CryptoQueen" filter clear
- [ ] Color palette matches hex codes exactly
- [ ] Accessibility alternatives for RGB flicker
- [ ] File naming follows snake_case convention
- [ ] Master files preserved with organized layers

### Quality Checkpoints:
- [ ] Bravado gate clearly communicates stat requirement
- [ ] NFT discovery intuitive with the QR code graffiti scan
- [ ] Drunk/hungover visual effects enhance comedy
- [ ] Graffiti readable and satirically effective
- [ ] Tech bro plaque maximizes comedic impact
- [ ] Performance optimized for status overlays
- [ ] All elements support "VIP toilet absurdity" theme
- [ ] Social media viral potential maximized
- [ ] Bathroom feels like regret shrine not gross-out
- [ ] Crypto satire balanced with game progression rewards

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Debaucheryville — Velvet Curtain Club interior sub-location only |
| Cultural Specificity | ✅ | 2017 crypto bull run peak culture weaponized for nightclub VIP exclusivity theater |
| Satirical Targets Appropriate | ✅ | Crypto speculation culture, tech bro excess, VIP bathroom pretension — not legitimate technology or entrepreneurs |
| Seedy Underbelly Present | ✅ | Manufactured VIP toilet exclusivity, tech bro sponsorship plaque, "Not a Scam, Probably" DAO invite |
| Gameplay Value Established | ✅ | Bravado gate, The Millennium Bug (Mint #00) discovery, Fistø lore (hungover), NFT Affinity buff, ICQ CryptoMamiXXX integration |
| Technical Feasibility | ✅ | 5 sprite atlases, LOD tiers down to Potato Mode, state-based conditional rendering documented |
| Performance Budget | ✅ | 60 FPS target, max 14 draw calls, 35MB memory footprint |
| Accessibility Features | ✅ | Visual audio cues (QR beep, champagne fizz), reduced RGB shimmer and static graffiti options |
| No Crypto Elements | ✅ | Crypto/NFT satire established in source material (NFT hunt collectible, crypto graffiti, ICQ mockery) |
| Social Media Integration | ✅ | Tech bro plaque, "ROI = Regret On Investment" graffiti, #CryptoQueen selfie filter identified |

**Once validated, the VIP Stall becomes the unforgettable NFT discovery location where players pass Bravado checks to access a bathroom sponsored by tech bros who admit they can't hold their liquor, discover The Millennium Bug (Mint #00) while reading graffiti that literally warns "ROI = Regret On Investment," experience champagne drip overlays when drunk making the warnings look luxurious, and unlock Fistø lore via pixel kebab icons when hungover, all while a selfie-cam mirror offers "#CryptoQueen" filters in a toilet stall with marble made of glitter Mod Podge!**
