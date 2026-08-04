# Velvet Curtain Club - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Velvet Curtain Club social hub. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this seedy elite nightclub where Studio 54 meets Eastern Bloc goth in a decaying opera house ruins.

**Location ID:** `debaucheryville_operaruins_velvetcurtainclub_nightclub_01`
**Theme:** Studio 54 meets Eastern Bloc goth — manufactured VIP exclusivity sold to tourists in decaying opera house ruins ("Vibes Only. No Shoes? No Dignity? You're In")
**Zone:** Dead-end service lane behind the opera ruins
**Hours:** Night hours (20:00–04:00 game time) for full atmosphere
**Primary Function:** Social hub & quest location — no combat; Charisma-gated entry with wristband bribe alternative, Vape Witch Vanessa couchsurf quiz, Influencer Blood Ritual side event, VIP bathroom NFT hunt access

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Deep Burgundy | #800020 | Fog machines, crushed velvet booths, dominant club atmosphere |
| Gold | #FFD700 | Stripper-pole coat racks, chandelier glow, luxury trim excess |
| Deep Purple | #4B0082 | Shadow tones, velvet depth, low-light surfaces |
| Neon Cyan | #00FFFF | Neon aphorism signs, LED underglow accents |
| Vape White | #FFFFFF | Vape clouds, vapor drift near patrons |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/velvetcurtain/
├── environment/
│   └── velvet_club_environment_complete.png
├── objects/
│   └── velvet_club_interactive_objects.png
├── npcs/
│   └── velvet_club_npcs.png
├── effects/
│   └── velvet_club_particle_effects.png
└── ui/
    └── velvet_club_ui_elements.png
```

---

## 🎨 Sprite Sheet 1: Velvet Club Environment Complete
**File:** `velvet_club_environment_complete.png`  
**Dimensions:** 1024x768 pixels  
**Color Palette:** #800020 (burgundy), #FFD700 (gold), #4B0082 (deep purple), #00FFFF (neon cyan)

### Vape-Pen Crystal Chandeliers:
- **Chandelier Base Structure** (0, 0, 128x96) - Crushed vape pens welded together
- **Crystal Teardrop Details** (128, 0, 64x48) - Hanging crystal elements
- **Chandelier Glow Frame 1** (192, 0, 128x96) - Standard golden glow
- **Chandelier Glow Frame 2** (320, 0, 128x96) - Slightly dimmer
- **Chandelier Glow Frame 3** (448, 0, 128x96) - Brightest glow
- **Vape Pen Detail Closeup** (576, 0, 32x32) - Individual crushed pen

### Gold-Plated Stripper Poles (Coat Racks):
- **Pole Base Structure** (0, 96, 48x128) - Gold-plated vertical pole
- **Pole Top Mount** (48, 96, 32x32) - Ceiling attachment
- **Pole Base Mount** (80, 96, 32x32) - Floor attachment
- **Coat Hanging Position 1** (112, 96, 64x96) - Coats draped on pole
- **Coat Hanging Position 2** (176, 96, 64x96) - Multiple coats variant
- **Gold Gleam Effect** (240, 96, 24x24) - Metallic shine particle

### Semicircular Crushed Velvet Booths:
- **Booth Structure Left** (0, 224, 96x64) - Curved booth seating left side
- **Booth Structure Center** (96, 224, 64x64) - Center booth section
- **Booth Structure Right** (160, 224, 96x64) - Curved booth seating right side
- **Booth Table** (256, 224, 64x32) - Low table in booth
- **LED Underglow Base** (320, 224, 96x16) - Lighting strip underneath
- **LED Underglow Pulse 1** (416, 224, 96x16) - Dim pulse state
- **LED Underglow Pulse 2** (512, 224, 96x16) - Bright pulse state
- **LED Underglow Pulse 3** (608, 224, 96x16) - Peak brightness

### DJ Broken Throne Dais:
- **Throne Base** (0, 288, 128x96) - Broken throne structure
- **DJ Equipment Setup** (128, 288, 96x64) - Turntables and mixer
- **Throne Crack Detail** (224, 288, 64x64) - Visible damage
- **DJ Spotlight** (288, 288, 48x48) - Lighting on DJ area
- **Turntable Spinning Frame 1** (336, 288, 48x48) - Record at 0°
- **Turntable Spinning Frame 2** (384, 288, 48x48) - Record at 90°
- **Turntable Spinning Frame 3** (432, 288, 48x48) - Record at 180°
- **Turntable Spinning Frame 4** (480, 288, 48x48) - Record at 270°

### Neon Aphorism Signs:
- **"The Real Party's In Your Head" Frame 1** (0, 384, 256x48) - Base neon glow
- **"The Real Party's In Your Head" Frame 2** (256, 384, 256x48) - Flicker dim
- **"The Real Party's In Your Head" Frame 3** (512, 384, 256x48) - Flicker bright
- **Neon Letter Flicker Detail** (768, 384, 32x48) - Individual letter effect
- **Neon Tube Glow** (800, 384, 16x48) - Cyan glow effect

### Heavy Velvet Curtain Entrance:
- **Curtain Closed** (0, 432, 96x128) - Initial entrance state
- **Curtain Bass Pulse 1** (96, 432, 96x128) - Subtle outward movement
- **Curtain Bass Pulse 2** (192, 432, 96x128) - Peak outward pulse
- **Curtain Bass Pulse 3** (288, 432, 96x128) - Return to base
- **Curtain Opening Frame 1** (384, 432, 96x128) - Player pushing through
- **Curtain Opening Frame 2** (480, 432, 96x128) - Half-open reveal
- **Curtain Fully Open** (576, 432, 96x128) - Entrance visible

### Burgundy Fog Effects:
- **Fog Layer 1 Base** (0, 560, 320x48) - Floor-level burgundy fog
- **Fog Layer 2 Mid** (320, 560, 320x48) - Mid-height fog
- **Fog Layer 3 High** (640, 560, 320x48) - Upper fog layer
- **Fog Swirl Pattern** (0, 608, 128x64) - Dense fog accumulation

### Wall and Floor Textures:
- **Opera Ruins Wall** (0, 672, 128x96) - Decayed grandeur wall texture
- **Graffiti Dumpster Mural** (128, 672, 96x64) - Alley exterior detail
- **Velvet-Rope Checkpoint** (224, 672, 64x48) - Entrance barrier
- **Floor Tiles Club** (288, 672, 128x64) - Dance floor pattern

### Technical Notes:
- Vape-pen chandeliers are centerpiece comedy element
- Gold stripper poles double as coat racks for satirical absurdity
- LED underglow pulses to bass rhythm continuously
- Neon signs flicker to music beat
- Bass-pulsating curtain entrance creates dynamic entry
- Burgundy fog creates Studio 54 decaying glamor atmosphere

---

## 🍾 Sprite Sheet 2: Velvet Club Interactive Objects
**File:** `velvet_club_interactive_objects.png`  
**Dimensions:** 512x384 pixels  
**Color Palette:** #800020 (burgundy), #FFD700 (gold), #00FFFF (neon cyan)

### VIP Bathroom "Staff Only" Curtain:
- **Red Velvet Curtain Closed** (0, 0, 64x96) - Staff Only entrance
- **Curtain with Embroidery** (64, 0, 64x96) - "STAFF ONLY" cracked text
- **Bouncer Guard Left** (128, 0, 64x96) - Buffed bouncer stance
- **Bouncer Guard Right** (192, 0, 64x96) - Second bouncer stance
- **Curtain Opening** (256, 0, 64x96) - Bravado check passed

### VIP Bathroom Interior:
- **Black Velvet Toilet Seat** (0, 96, 48x64) - Plush stained seat
- **Champagne Holder Mount** (48, 96, 32x48) - Wall-mounted holder
- **Moët 2003 Bottle** (80, 96, 16x48) - Half-empty champagne
- **Selfie-Cam Mirror** (96, 96, 64x96) - Mirror with camera filter
- **#CryptoQueen Filter Overlay** (160, 96, 64x64) - Selfie filter effect
- **Cracked Tile Peeling** (224, 96, 32x32) - Reveals QR code underneath
- **QR Code NFT #2** (256, 96, 32x32) - Pixelated Kebab Monkey code

### Bathroom Graffiti Elements:
- **"ROI = Regret On Investment"** (0, 192, 128x24) - Wall scrawl
- **"I BLEW IT… literally"** (128, 192, 96x24) - Graffiti line
- **"Buy Low, Cry High"** (224, 192, 80x24) - Crypto commentary
- **Velvet DAO QR Code** (304, 192, 32x32) - Scan invitation
- **Startup Ideas Scribbled** (336, 192, 64x32) - Random notes
- **@ Handles and Altcoin Schemes** (400, 192, 96x32) - Social media tags

### Tech Bro Sponsorship Plaque:
- **Faux-Brass Plaque** (0, 240, 128x48) - Sponsor nameplate
- **Plaque Text Detail** (128, 240, 128x48) - "VIP Stall generously sponsored by Tech Bros Who Can't Hold Their Liquor"

### Drunk State Visual Effects:
- **Champagne Drip Overlay Frame 1** (0, 288, 128x96) - Text dripping start
- **Champagne Drip Overlay Frame 2** (128, 288, 128x96) - Mid-drip
- **Champagne Drip Overlay Frame 3** (256, 288, 128x96) - Full drip effect
- **Bubble Particle** (384, 288, 16x16) - Champagne bubble
- **Pixel Kebab Icon** (400, 288, 24x24) - Hungover bonus icon

### Dance Floor Elements:
- **RGB LED Floor Panel** (0, 384, 64x64) - Light-up floor section
- **Spilled Drink Puddle** (64, 384, 48x32) - Comedy hazard
- **Glitter Trail** (112, 384, 64x24) - Patron trail effect

### Environmental Details:
- **Expired Concert Wristband** (176, 384, 32x16) - Bribe item
- **Vape Cloud Dense** (208, 384, 48x48) - Thick vapor accumulation
- **Lip Gloss and Wristband Trail** (256, 384, 96x24) - VIP bathroom approach

### Technical Notes:
- VIP bathroom requires Bravado check to access
- QR code graffiti reveals NFT #2 collectible
- Drunk state adds champagne drip visual overlay
- Hungover state shows pixel kebab icon with Fistø lore
- Tech bro sponsorship plaque is satirical centerpiece
- All graffiti supports crypto nostalgia comedy

---

## 👥 Sprite Sheet 3: Velvet Club NPCs
**File:** `velvet_club_npcs.png`  
**Dimensions:** 512x512 pixels  
**Character Size:** 64x96 base sprites
**Color Palette:** #800020 (burgundy), #FFD700 (gold), #00FFFF (neon cyan)

### Cybernetic-Eyed Bouncer:
- **Idle Guard Stance** (0, 0, 64x96) - Professional bouncer pose
- **Eye Glow Animation Frame 1** (64, 0, 64x96) - Cybernetic eyes dim
- **Eye Glow Animation Frame 2** (128, 0, 64x96) - Eyes brightening
- **Eye Glow Animation Frame 3** (192, 0, 64x96) - Eyes full glow
- **Charisma Check Pass Gesture** (256, 0, 64x96) - Approving nod
- **Charisma Check Fail Gesture** (320, 0, 64x96) - Blocking stance
- **Bribe Acceptance** (384, 0, 64x96) - Taking wristband

### Vape Witch Vanessa:
- **Idle with Vape** (0, 96, 64x96) - Holding vape pen
- **Exhaling Vape Cloud** (64, 96, 64x96) - Peach-mango cloud
- **Crystal NFT Display** (128, 96, 64x96) - Showing collection
- **Quiz Asking Pose** (192, 96, 64x96) - Interactive dialogue
- **Morning Cleansing Scene** (256, 96, 64x96) - Vape exhale into mouth
- **Disappointed Quiz Fail** (320, 96, 64x96) - Confused status trigger
- **Happy Quiz Success** (384, 96, 64x96) - SP reward giving

### Club Patron Archetypes:
- **Ravewear Patron Idle** (0, 192, 64x96) - Neon outfit dancer
- **Opera Cloak Patron** (64, 192, 64x96) - Thrifted grandeur
- **NFT Crop Top Patron** (128, 192, 64x96) - Logo fashion
- **Age Denial Patron** (192, 192, 64x96) - "I'm totally 22" stance
- **Sound Alchemist Comment** (256, 192, 64x96) - Patron dialogue pose
- **Emotional Damage Cocktail** (320, 192, 64x96) - Drinking patron

### Influencer Performing Ritual:
- **Livestream Setup** (0, 288, 64x96) - Phone on tripod
- **Fake Mystical Pose 1** (64, 288, 64x96) - Arms raised dramatically
- **Fake Mystical Pose 2** (128, 288, 64x96) - Absinthe pouring
- **Exposed Embarrassed** (192, 288, 64x96) - Called out reaction
- **Follower Count Display** (256, 288, 32x16) - Screen notification
- **Ritual Props** (288, 288, 48x48) - Candles and absinthe bottle

### DJ Sound Alchemist:
- **DJ Mixing Idle** (0, 384, 64x96) - Behind turntables
- **Scratching Animation** (64, 384, 64x96) - Active DJing
- **Headphones Detail** (128, 384, 64x96) - Professional equipment
- **Pretentious Gesture** (192, 384, 64x96) - Explaining "alchemy"

### VIP Bathroom Bouncers:
- **Buffed Bouncer 1 Stance** (256, 384, 64x96) - Guarding left
- **Buffed Bouncer 2 Stance** (320, 384, 64x96) - Guarding right
- **Bravado Check Animation** (384, 384, 64x96) - Sizing up player

### Signature Props & Accessories:
- **Cybernetic Eye Closeup** (448, 0, 24x24) - Bouncer eye detail
- **Vape Pen Accessory** (448, 24, 16x32) - Vanessa signature item
- **Crystal NFT Hologram** (464, 24, 32x32) - Collection display
- **Mirrored Sunglasses** (448, 56, 32x16) - Patron accessory
- **Expired Wristband** (448, 72, 32x16) - Bribe item detail

### Technical Notes:
- Cybernetic-eyed bouncer has glowing eye animation loop
- Vape Witch Vanessa has peach-mango vape cloud particle effect
- Club patrons represent age range mid-20s to 40s pretending they're 22
- Influencer has fake blood ritual livestream setup
- DJ on broken throne dais playing glitchy lounge-techno
- VIP bathroom bouncers require Bravado check to bypass

---

## ✨ Sprite Sheet 4: Velvet Club Particle Effects
**File:** `velvet_club_particle_effects.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #800020 (burgundy), #FFD700 (gold), #00FFFF (neon cyan), #FFFFFF (vape)

### Burgundy Fog Machines:
- **Fog Particle 1** (0, 0, 32x32) - Light burgundy density
- **Fog Particle 2** (32, 0, 32x32) - Medium density
- **Fog Particle 3** (64, 0, 32x32) - Heavy density
- **Fog Particle 4** (96, 0, 32x32) - Wispy tendrils
- **Fog Floor Coverage** (128, 0, 96x32) - Ground-level layer

### Vape Cloud Drift:
- **Vape Cloud 1** (0, 32, 48x48) - White vapor small
- **Vape Cloud 2** (48, 32, 48x48) - Medium vapor
- **Vape Cloud 3** (96, 32, 48x48) - Large vapor cloud
- **Vape Cloud 4** (144, 32, 48x48) - Dispersing vapor
- **Peach-Mango Tint** (192, 32, 48x48) - Vanessa signature cloud

### LED Shimmer Effects:
- **RGB Shimmer 1** (0, 80, 32x32) - Cyan predominant
- **RGB Shimmer 2** (32, 80, 32x32) - Gold predominant
- **RGB Shimmer 3** (64, 80, 32x32) - Magenta predominant
- **RGB Shimmer 4** (96, 80, 32x32) - Mixed colors
- **LED Sparkle** (128, 80, 16x16) - Small shimmer particle

### Bass Ripple Particles:
- **Bass Ripple 1** (0, 112, 64x32) - Subtle outward wave
- **Bass Ripple 2** (64, 112, 64x32) - Medium wave
- **Bass Ripple 3** (128, 112, 64x32) - Peak ripple
- **Bass Ripple 4** (192, 112, 64x32) - Dissipating wave
- **Curtain Pulse Effect** (256, 112, 48x48) - Entrance curtain ripple

### Champagne Bubbles (Drunk State):
- **Bubble 1 Small** (0, 144, 12x12) - Rising bubble
- **Bubble 2 Medium** (12, 144, 16x16) - Mid-size bubble
- **Bubble 3 Large** (28, 144, 20x20) - Large bubble
- **Bubble Pop** (48, 144, 24x24) - Burst effect
- **Champagne Fizz** (72, 144, 32x32) - Effervescent cluster

### Neon Glow Pulse:
- **Neon Pulse 1** (0, 176, 48x48) - Base cyan glow
- **Neon Pulse 2** (48, 176, 48x48) - Intensifying glow
- **Neon Pulse 3** (96, 176, 48x48) - Peak brightness
- **Neon Pulse 4** (144, 176, 48x48) - Returning to base
- **Neon Flicker** (192, 176, 32x32) - Irregular pulse

### Gold Gleam Effects:
- **Pole Gleam 1** (0, 224, 24x24) - Gold shimmer start
- **Pole Gleam 2** (24, 224, 24x24) - Shimmer peak
- **Pole Gleam 3** (48, 224, 24x24) - Shimmer fade
- **Chandelier Sparkle** (72, 224, 16x16) - Crystal glint

### Confused Status Indicator:
- **Confusion Vape Spiral 1** (96, 224, 32x32) - Spiral start
- **Confusion Vape Spiral 2** (128, 224, 32x32) - Mid-spiral
- **Confusion Vape Spiral 3** (160, 224, 32x32) - Peak confusion
- **Confusion Vape Spiral 4** (192, 224, 32x32) - Return cycle

### Embarrassed Status Indicator:
- **Embarrassed Blush 1** (224, 224, 32x32) - Light red tint
- **Embarrassed Blush 2** (256, 224, 32x32) - Medium blush
- **Embarrassed Blush 3** (288, 224, 32x32) - Deep embarrassment
- **Sweat Drop** (320, 224, 16x16) - Social failure indicator

### Particle Emission Rates:
- **Burgundy Fog:** 20/second, 6.0s lifetime
- **Vape Cloud Drift:** 15/second, 5.0s lifetime
- **LED Shimmer:** 10/second, 2.0s lifetime
- **Bass Ripples:** 8/second synced to music, 1.5s lifetime
- **Champagne Bubbles:** 12/second (drunk state only), 3.0s lifetime
- **Neon Glow Pulse:** 5/second, 2.5s lifetime

### Technical Notes:
- Burgundy fog creates Studio 54 atmosphere throughout
- Vape clouds accumulate near Vanessa and patrons
- LED shimmer enhances booth underglow continuously
- Bass ripples sync to glitchy lounge-techno music
- Champagne bubbles only appear during drunk status
- Confused status from vape/absinthe combinations
- Embarrassed status from social interaction failures

---

## 🎮 Sprite Sheet 5: Velvet Club UI Elements
**File:** `velvet_club_ui_elements.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #800020 (burgundy), #FFD700 (gold), #00FFFF (neon cyan)

### Status Effect Icons:
- **Embarrassed Icon Active** (0, 0, 32x32) - Red blush effect
- **Embarrassed Icon Stacked** (32, 0, 32x32) - Multiple sources
- **Confused Icon Active** (64, 0, 32x32) - Vape spiral effect
- **Confused Icon Stacked** (96, 0, 32x32) - Vape + absinthe
- **NFT Affinity Protection** (128, 0, 32x32) - Buff shield icon

### Charisma Gate UI:
- **Charisma Check Display** (0, 32, 96x32) - "+1 Charisma Required"
- **Charisma Pass Checkmark** (96, 32, 32x32) - Success indicator
- **Charisma Fail X** (128, 32, 32x32) - Failure indicator
- **Wristband Bribe Option** (160, 32, 64x32) - Alternative entry

### Couchsurf Quest UI:
- **Vanessa Couchsurf Available** (0, 64, 96x32) - Invitation indicator
- **Quiz Question Display** (96, 64, 128x48) - Crystal NFT trivia
- **Quiz Success** (224, 64, 48x32) - +10 SP reward
- **Quiz Failure** (272, 64, 48x32) - Confused status applied

### VIP Bathroom Access UI:
- **Bravado Check Display** (0, 112, 96x32) - Stat requirement
- **Bouncer Sizing Up** (96, 112, 64x48) - Checking player
- **Access Granted** (160, 112, 48x32) - Pass through curtain
- **Access Denied** (208, 112, 48x32) - Cannot enter

### NFT Hunt Progress:
- **NFT #2 Location Hint** (0, 160, 64x32) - "Check VIP bathroom stalls"
- **QR Code Scan Prompt** (64, 160, 96x32) - "Scan graffiti QR code"
- **NFT #2 Acquired** (160, 160, 128x48) - "Pixelated Kebab Monkey" collected
- **3 NFT Progress Bar** (288, 160, 96x16) - 2 of 3 complete

### Achievement Popups:
- **Vibes Only Unlocked** (0, 208, 128x48) - First club entry
- **NFT #2 Discovered** (128, 208, 128x48) - Bathroom QR found
- **Vanessa Couchsurf Complete** (256, 208, 128x48) - Quiz passed
- **Influencer Ritual Exposed** (384, 208, 128x48) - Event completion

### Interaction Prompts:
- **"Push Through Curtain"** (0, 256, 64x24) - Entrance interaction
- **"Examine Coat Rack Poles"** (64, 256, 80x24) - Stripper pole comedy
- **"Read Neon Sign"** (144, 256, 64x24) - Aphorism interaction
- **"Enter VIP Bathroom"** (208, 256, 80x24) - Staff Only curtain

### Social Hub Indicators:
- **NPC Available** (288, 256, 32x32) - Vanessa present
- **Side Event Active** (320, 256, 32x32) - Influencer ritual
- **Quest Trigger** (352, 256, 32x32) - Couchsurf invitation

### Technical Notes:
- Charisma gate teaches stat check + alternative entry mechanics
- Couchsurf UI tracks Vanessa quiz success/failure
- VIP bathroom requires Bravado check visualization
- NFT Hunt progress shows bathroom location hint
- Achievement popups celebrate social hub milestones
- Status icons clearly indicate Embarrassed and Confused effects

---

## 📱 Mobile Optimization Requirements

### Texture Compression by Platform:
- **iOS:** PVRTC 4BPP for burgundy fog and gold effects
- **Android:** ETC2 with alpha for vape cloud transparency
- **Fallback:** PNG high quality for neon signs and graffiti detail

### Sprite Atlasing Strategy:
- **Environment Complete Atlas:** Chandeliers + booths + DJ dais + curtains + fog (1024x768)
- **Interactive Objects Atlas:** VIP bathroom + graffiti + drunk effects + dance floor (512x384)
- **NPC Atlas:** Bouncer + Vanessa + patrons + influencer + DJ + VIP guards (512x512)
- **Particle Effects Atlas:** Fog + vape + LED + bass + bubbles + status (512x256)
- **UI Elements Atlas:** Status icons + charisma gate + couchsurf + NFT hunt (512x256)
- **Max Atlas Size:** 2048x2048 for mobile GPU compatibility

### LOD (Level of Detail) Scaling:
- **High-End Devices:** Full fog density, all LED underglow pulse, vape cloud particles, bass ripples
- **Medium Devices:** Reduced fog particle count, simplified LED effects, basic vape clouds
- **Low-End Devices:** Static fog layer, minimal vape particles, no bass ripples
- **Potato Mode:** Single ambient light, basic booth layout, essential NPCs only

### Performance Targets:
- **Target FPS:** 60 fps (complex lighting and particle systems)
- **Max Draw Calls:** 18 per frame
- **Memory Footprint:** 42MB maximum for social hub

---

## ♿ Accessibility Sprite Requirements

### High Contrast Charisma Gates:
- **Enhanced Stat Check Display** (0, 0, 128x48) - Clear requirement
- **Alternative Entry Highlight** (128, 0, 96x32) - Wristband option
- **Pass/Fail Clear Indicators** (224, 0, 64x32) - Red/green alternatives

### Motion Sensitivity Options:
- **Reduced LED Pulse** (0, 48, 96x16) - Minimal flicker
- **Static Neon Signs** (96, 48, 256x48) - No bass pulse
- **Gentle Fog Movement** (352, 48, 96x48) - Slower particle drift
- **No Bass Ripples** (448, 48, 64x32) - Static curtain

### Visual Audio Cues:
- **Bass Drop Wave** (0, 96, 48x32) - Sound visualization
- **Charisma Check Visual** (48, 96, 32x32) - Audio-independent
- **Club Music Pulse** (80, 96, 64x48) - Beat indicator

### High Contrast NPCs:
- **Bouncer Outline** (0, 144, 64x96) - Enhanced visibility
- **Vanessa Silhouette** (64, 144, 64x96) - Clear against fog
- **Patron Emphasis** (128, 144, 64x96) - Distinct from background

---

## 🎬 Animation Sequence Specifications

### Bass-Pulsating Velvet Curtain:
- **Duration:** 3-frame cycle, 1.5 seconds total (8 fps)
- **Pattern:** Closed → Pulse Out → Peak → Return
- **Loop:** Continuous synced to music bass
- **Purpose:** Dynamic entrance indicating music intensity

### LED Underglow Booth Pulse:
- **Duration:** 3-frame cycle, 2.0 seconds total (10 fps)
- **Pattern:** Dim → Medium → Bright → Return
- **Loop:** Continuous bass-reactive pulse
- **Purpose:** Creates retro-luxury nightclub atmosphere

### Neon Sign Flicker:
- **Duration:** 3-frame cycle, 2.5 seconds total (variable fps)
- **Pattern:** Base → Dim Flicker → Bright Flicker → Return
- **Loop:** Continuous bass-reactive
- **Purpose:** "The Real Party's In Your Head" emphasis

### Vape-Pen Chandelier Glow:
- **Duration:** 3-frame cycle, 3.0 seconds total (6 fps)
- **Pattern:** Standard → Dimmer → Brightest → Return
- **Loop:** Continuous ambient glow
- **Purpose:** Comedy centerpiece lighting

### DJ Turntable Spinning:
- **Duration:** 4-frame cycle, 2.0 seconds total (12 fps)
- **Pattern:** 0° → 90° → 180° → 270° → Return
- **Loop:** Continuous rotation
- **Purpose:** Live DJ on broken throne aesthetic

### Cybernetic Eye Glow:
- **Duration:** 3-frame cycle, 3.0 seconds total (6 fps)
- **Pattern:** Dim → Brightening → Full Glow → Return
- **Loop:** Continuous idle animation
- **Purpose:** Bouncer signature intimidation

### Vanessa Vape Exhale:
- **Duration:** 4-frame sequence, 2.0 seconds total (8 fps)
- **Trigger:** Dialogue interaction and morning scene
- **Pattern:** Idle → Inhale → Exhale Cloud → Disperse
- **Audio:** Vape hiss and exhale sound
- **Purpose:** Character signature and cleansing ritual

### Influencer Blood Ritual Performance:
- **Duration:** 6-frame sequence, 6.0 seconds total
- **Trigger:** Side event activation
- **Pattern:** Setup → Pose 1 → Pose 2 → Absinthe Pour → Peak Drama → Exposed/Ignored
- **Audio:** Livestream commentary, fake mystical energy
- **Purpose:** Influencer culture satire side event

### Champagne Drip Text Overlay (Drunk State):
- **Duration:** 3-frame cycle, 2.0 seconds total (10 fps)
- **Trigger:** Player drunk status + viewing VIP bathroom graffiti
- **Pattern:** Text Start Drip → Mid-Drip → Full Drip Effect
- **Particle:** Champagne bubbles floating upward
- **Purpose:** Drunk state visual enhancement

### Pixel Kebab Icon Appearance (Hungover State):
- **Duration:** Single frame reveal
- **Trigger:** Player hungover status + viewing VIP bathroom graffiti
- **Effect:** Icon appears near graffiti text
- **Audio:** Fistø lore snippet narration
- **Purpose:** Unlocks "The Greasy Prophet" title progression

### Coat Rack Pole Gleam:
- **Duration:** 3-frame cycle, 1.5 seconds total (12 fps)
- **Pattern:** Base Gold → Gleam Start → Peak Shine → Return
- **Loop:** Random intervals (every 5-8 seconds)
- **Purpose:** Draw attention to stripper poles as coat racks comedy

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Animation system: Frame-based with JSON timing data
- Social hub system: NPC encounter zones, quest triggers
- Stat check system: Charisma gate, Bravado gate mechanics
- Couchsurf system: Vanessa quiz branching outcomes

### Audio Sync Points:
- Bass-pulsating curtain syncs with glitchy lounge-techno
- LED underglow pulse matches music rhythm
- Neon sign flicker reacts to bass drops
- Vape exhale has hiss and dispersion sound
- Champagne drip has bubble pop effects
- Coat rack pole clink when examined

### Quest Integration:
- **NFT Hunt:** VIP bathroom QR code reveals NFT #2 "Pixelated Kebab Monkey"
- **Couchsurfing Chronicles:** Vanessa encounter, morning scene, quiz mechanics
- **Influencer Blood Ritual:** Side event with expose/support/ignore choices
- **Fistø Lore:** Hungover graffiti bonus contributes to "The Greasy Prophet" title

### Cross-Location Dependencies:
- **Opera Ruins Alley:** Entrance from graffiti-laced alley behind billboard
- **Charisma/Bribe Gate:** +1 Charisma OR expired concert wristband required
- **ICQ Integration:** CryptoMamiXXX messages mock stall and player decisions
- **Achievement System:** "Vibes Only" entry, NFT discovery, couchsurf completion

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Studio 54 meets Eastern Bloc goth in decaying opera house ruins"
- **Color Mood:** Burgundy fog dominance, gold accent excess, neon cyan highlights
- **Lighting:** Vape-pen chandeliers, LED underglow booths, neon sign pulse, bass-reactive effects
- **Texture:** Crushed velvet luxury, gold-plated absurdity, burgundy fog atmosphere

### Character Design Philosophy:
- **Cybernetic-Eyed Bouncer:** Robotic monotone enforcing "Vibes Only" philosophy
- **Vape Witch Vanessa:** Crystal NFT collector with peach-mango vape obsession
- **Club Patrons:** Age range mid-20s to 40s all insisting they're 22
- **Influencer:** Fake goth performing blood ritual livestream for followers
- **DJ Sound Alchemist:** Pretentious terminology for basic DJ work

### Social Hub Design:
- No combat encounters, focus on social interactions and dialogue
- Charisma checks gate entry, creating exclusivity satire
- Couchsurf invitation from Vanessa triggers quiz mechanics
- Influencer ritual allows player choice (expose/support/ignore)
- VIP bathroom requires Bravado check for NFT discovery

### Environmental Storytelling:
- Vape-pen chandeliers suggest commercialized vape culture as luxury
- Gold stripper poles as coat racks create avant-garde absurdity
- Neon aphorisms reflect pseudo-deep party philosophy
- VIP bathroom graffiti reveals crypto nostalgia and tech bro regret
- Everyone pretending they're 22 satirizes nightclub age denial culture

---

## 📋 Required PNG Files (5 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | velvet_club_environment_complete.png | 1024x768 |
| 2 | velvet_club_interactive_objects.png | 512x384 |
| 3 | velvet_club_npcs.png | 512x512 |
| 4 | velvet_club_particle_effects.png | 512x256 |
| 5 | velvet_club_ui_elements.png | 512x256 |

**Total Estimated Memory:** ~6.0 MB uncompressed RGBA (within the 42MB social hub footprint)

---

## 📦 File Delivery Checklist

### Required PNG Files (5 Total):
- [ ] `velvet_club_environment_complete.png` (1024x768)
- [ ] `velvet_club_interactive_objects.png` (512x384)
- [ ] `velvet_club_npcs.png` (512x512)
- [ ] `velvet_club_particle_effects.png` (512x256)
- [ ] `velvet_club_ui_elements.png` (512x256)

### Quality Requirements:
- **Format:** PNG-24 with alpha channel
- **Color Space:** sRGB
- **DPI:** 72 (screen resolution)
- **Compression:** Lossless PNG
- **Naming Convention:** snake_case, all lowercase
- **Layer Organization:** Preserve for animation frame updates

### Delivery Format:
- **Primary:** Individual PNG files per specifications
- **Backup:** Master PSD/Photoshop with organized layer groups
- **Documentation:** Animation timing sheet, social hub interaction guide

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Vape-Pen Chandeliers Overhead Shot** - Crushed vape pens as luxury decor
2. **Gold Stripper Poles as Coat Racks** - Avant-garde coat storage absurdity
3. **VIP Bathroom Graffiti** - "ROI = Regret On Investment" crypto commentary
4. **Neon Aphorism Sign** - "The Real Party's In Your Head" philosophy
5. **Burgundy Fog Dance Floor** - Studio 54 meets Eastern Bloc aesthetic

### TikTok Potential:
- "POV: You realize the chandeliers are made of vape pens"
- "When the club coat rack is a stripper pole"
- "Charisma check fail at velvet rope compilation"
- "Reading VIP bathroom graffiti while drunk vs hungover"
- "Everyone here insists they're 22 (they're not)"

### Twitter/X Quote Potential:
- "Vibes Only. No Shoes? No Dignity? You're In" - Entrance sign
- "He said he was a 'sound alchemist.' I think that means DJ." - Club patron
- "I only drink cocktails made with rare emotional damage." - Patron dialogue
- "ROI = Regret On Investment" - VIP bathroom graffiti
- "The coat check is... avant-garde" - Player examining stripper poles

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 5 PNG files match exact dimensions
- [ ] Vape-pen chandeliers show crushed pens welded with crystals
- [ ] Gold stripper poles clearly double as coat racks
- [ ] LED underglow has bass-reactive pulse animation
- [ ] Neon signs have "The Real Party's In Your Head" readable
- [ ] Cybernetic-eyed bouncer has glowing eye animation
- [ ] Vape Witch Vanessa has peach-mango vape cloud effect
- [ ] VIP bathroom graffiti includes all crypto commentary
- [ ] Champagne drip overlay works with drunk status
- [ ] Pixel kebab icon appears with hungover status
- [ ] Club patrons represent varied age-denial fashion
- [ ] Influencer has livestream setup with ritual props
- [ ] DJ on broken throne dais with turntables
- [ ] Burgundy fog creates Studio 54 atmosphere
- [ ] Bass-pulsating curtain entrance animation smooth
- [ ] All particle effects support burgundy/gold/cyan theme
- [ ] Color palette matches hex codes exactly
- [ ] Accessibility alternatives included for motion sensitivity
- [ ] File naming follows snake_case convention
- [ ] Master files preserved with organized layers

### Quality Checkpoints:
- [ ] Charisma gate clearly communicates stat requirement + bribe alternative
- [ ] VIP bathroom Bravado check visually distinct from Charisma gate
- [ ] Vanessa couchsurf quiz mechanics clear and functional
- [ ] NFT #2 discovery in bathroom graffiti intuitive
- [ ] Influencer ritual side event player choices obvious
- [ ] Social hub atmosphere supports "manufactured exclusivity" satire
- [ ] All elements reinforce "party tourism exploitation" theme
- [ ] Mobile performance optimized for complex fog and lighting
- [ ] All animations support nightclub party energy
- [ ] Social media viral potential maximized
- [ ] Nightclub atmosphere feels unique and memorable
- [ ] Decaying glamor aesthetic is comedic not depressing

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Debaucheryville — opera ruins service lane only |
| Cultural Specificity | ✅ | Eastern European nightclub exclusivity culture weaponized for Western party tourism |
| Satirical Targets Appropriate | ✅ | Pretentious club culture, influencer lifestyle, VIP status desperation — not nightlife workers or genuine music scenes |
| Seedy Underbelly Present | ✅ | Manufactured exclusivity sold to tourists, decaying glamor, fake blood ritual livestreams |
| Gameplay Value Established | ✅ | Social hub (no combat) — Charisma gate + bribe alternative, Vanessa couchsurf quiz, influencer event choices, NFT hunt gateway |
| Technical Feasibility | ✅ | 5 sprite atlases, LOD tiers down to Potato Mode, fog/vape via scalable particle systems |
| Mobile Performance Budget | ✅ | 60 FPS target, max 18 draw calls, 42MB memory footprint |
| Accessibility Features | ✅ | Visual audio cues (bass drop wave, club music pulse), static neon/reduced LED options, high contrast NPCs |
| No Crypto Elements | ✅ | Crypto/NFT satire established in source material (NFT hunt, VIP bathroom crypto graffiti) |
| Social Media Integration | ✅ | Vape-pen chandeliers, stripper-pole coat racks, neon aphorisms, quotable patron dialogue identified |

**Once validated, the Velvet Curtain Club becomes the unforgettable social hub where players navigate Charisma gates guarded by cybernetic-eyed bouncers enforcing "Vibes Only" philosophy, meet Vape Witch Vanessa for crystal NFT quiz couchsurfing, discover NFT #2 in VIP bathroom graffiti sponsored by tech bros who can't hold their liquor, expose influencers performing fake blood rituals for followers, and party under vape-pen chandeliers while everyone insists they're 22 despite clearly being mid-20s to 40s, with gold-plated stripper poles serving as avant-garde coat racks and neon signs proclaiming "The Real Party's In Your Head" in a decaying opera house ruins where Studio 54 meets Eastern Bloc goth!**