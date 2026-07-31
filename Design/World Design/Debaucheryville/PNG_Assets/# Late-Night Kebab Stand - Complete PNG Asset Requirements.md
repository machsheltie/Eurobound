# Late-Night Kebab Stand - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Late-Night Kebab Stand location. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this post-party lifeline operation.

---

## 🎨 Sprite Sheet 1: Mr. Chadz Kebab Cart Complete
**File:** `mr_chadz_kebab_cart_complete.png`  
**Dimensions:** 1024x768 pixels  
**Color Palette:** #FFFFFF (fluorescent white), #FF6B35 (grease orange), #FFD700 (golden rotisserie), #2C2C2C (alley shadow)

### Base Cart Structure (256x192 each):
1. **Idle State** (0, 0) - Standard operation, gentle steam wisps
2. **Active Cooking** (256, 0) - Heavy steam, active meat carving, grease dripping
3. **Cleaning Mode** (512, 0) - Suspicious rag wiping, questionable sanitation

### Vertical Rotisserie System:
- **Rotation Frame 1** (0, 192, 64x96) - Starting position, meat layers visible
- **Rotation Frame 2** (64, 192, 64x96) - 90° rotation
- **Rotation Frame 3** (128, 192, 64x96) - 180° rotation
- **Rotation Frame 4** (192, 192, 64x96) - 270° rotation
- **Rotisserie Mechanism** (256, 192, 48x96) - Motor housing, grease-stained metal
- **Drip Tray Collection** (304, 192, 64x32) - Grease accumulation, questionable liquid

### Fluorescent Lighting States:
- **Full Brightness** (0, 288, 128x48) - Blinding cart illumination
- **Flickering Dim** (128, 288, 128x48) - Electrical issues, unstable light
- **Electrical Issues** (256, 288, 128x48) - Sparking, dangerous wiring visible

### Signage System:
- **"MR. CHADZ KEBABS" Main** (384, 0, 256x64) - Crooked faux-Arabic font
- **LED Strip Normal** (384, 64, 256x16) - Backlit by LED strip
- **LED Strip Flickering** (384, 80, 256x16) - Electrical malfunction state
- **LED Strip Burned Out** (384, 96, 256x16) - Some bulbs dead
- **Hookah Hose Mount** (640, 64, 64x48) - Zip-tied LED strip attachment

### Steam Emission Points:
- **Rotisserie Top Vent** (768, 0, 32x32) - Primary steam source
- **Drip Tray Steam** (800, 0, 32x24) - Grease vapor rising
- **Cart Side Vents** (832, 0, 48x32) - Ambient cooking steam

### Animation Notes:
- Rotisserie: 2 RPM continuous (0.5s per 90° frame)
- LED strip: Random flicker 0.5-2 second intervals
- Steam: Continuous particle emission from all vents
- Drip tray: Grease accumulation increases over time

---

## 👨‍🍳 Sprite Sheet 2: Mr. Chadz Kebab Vendor
**File:** `mr_chadz_kebab_vendor.png`  
**Dimensions:** 512x512 pixels  
**Character Height:** 6'4" proportions (64x96 sprite size)
**Color Palette:** #FF1493 (glittery crop top), #4B4B4B (bulletproof vest), #FFD700 (gold accents), #000000 (burner phone)

### Idle Phone Checking Animation (64x96 each):
- **Frame 1** (0, 0) - Looking at burner phone, deadpan expression
- **Frame 2** (64, 0) - Scrolling sketchy messages
- **Frame 3** (128, 0) - Annoyed supplier text visible
- **Frame 4** (192, 0) - Puts phone away, returns to service

### Food Service Actions (64x96 each):
- **Prep Ingredients** (0, 96) - Handling mystery meat with one hand
- **Wrapping with Flourish** (64, 96) - Theatrical food assembly
- **Serving Customer** (128, 96) - Deadpan handoff, intimidating presence
- **Payment Collection** (192, 96) - Taking kebab coins, phone still visible

### Business Reactions (64x96 each):
- **Supplier Concerns** (0, 192) - Tense phone conversation, one-handed cooking
- **Health Inspector Panic** (64, 192) - Brief alarm, quickly composed
- **Sketchy Negotiation** (128, 192) - Whispering into burner phone
- **Normal Service Resume** (192, 192) - Back to deadpan food service

### Signature Outfit Elements:
- **Glittery Crop Top** (256, 0, 48x64) - Sequined, catches light, absurd contrast
- **Bulletproof Vest** (304, 0, 48x72) - Over crop top, bouncer origin visible
- **Burner Phone** (352, 0, 16x32) - Constantly in hand or pocket
- **6'4" Proportions** (368, 0, 64x96) - Full height reference sprite
- **Deadpan Expression** (432, 0, 32x32) - Face close-up, no emotion

### Character Notes:
- Glittery crop top must contrast absurdly with bulletproof vest
- Burner phone always visible (in hand, pocket, or nearby)
- Deadpan expression maintained during all activities
- One-handed food service while managing phone calls
- 6'4" height should feel imposing but casual

---

## 🍖 Sprite Sheet 3: Kebab Menu Items Detailed
**File:** `kebab_menu_items_detailed.png`  
**Dimensions:** 1024x512 pixels  
**Item Size:** 64x64 base, variations as needed
**Color Palette:** #8B4513 (mystery meat brown), #FF4500 (sauce red), #FFD700 (grease gold), #98FB98 (questionable green)

### Row 1 - Gutbuster Wrap (Y=0):
- **Wrapped Closed** (0, 0, 64x64) - Dripping, barely contained
- **Unwrapped Dripping** (64, 0, 64x64) - Mystery lamb visible, sauce overflow
- **Cross-Section View** (128, 0, 64x64) - Interior horror/appeal balance
- **Existential Regret Visual** (192, 0, 64x64) - Steam effect, ominous glow

### Row 2 - Vampire Slayer Garlic Fries (Y=64):
- **Container Closed** (0, 64, 64x64) - Takeout box, grease-stained
- **Sauce Dripping** (64, 64, 64x64) - Garlic sauce overflow
- **Week-Old Oil Shimmer** (128, 64, 64x64) - Rainbow grease effect on fries
- **Pepper Spray Intensity** (192, 64, 64x64) - Visual garlic vapor cloud

### Row 3 - EuroMeat Pocket™ (Y=128):
- **Suspicious Grey Filling** (0, 128, 64x64) - Mystery gyro content
- **Soggy Pita** (64, 128, 64x64) - Microwaved bread, structural failure
- **Microwaved Steam** (128, 128, 64x64) - Unnatural heat vapor
- **Meat Doubt Visualization** (192, 128, 64x64) - Question mark particles

### Row 4 - MegaMix Box (Y=192):
- **Cardboard Coffin Closed** (0, 192, 96x64) - Ominous takeout container
- **Horrifying Contents** (96, 192, 96x64) - Everything crammed together
- **Regret Visualization** (192, 192, 64x64) - Status effect preview aura

### Row 5 - Drunken Sauce Shot (Y=256):
- **Plastic Thimble** (0, 256, 32x48) - Tiny dangerous container
- **Hot Sauce/Mayo Swirl** (32, 256, 32x48) - Questionable mixture
- **Dysentery Warning** (64, 256, 48x32) - Skull icon, danger indication

### Row 6 - Lambsomnia Special (Y=304):
- **Spiced Lamb Base** (0, 304, 64x64) - Well-seasoned mystery meat
- **Sleepless Tzatziki** (64, 304, 64x64) - Sauce with energy effect
- **Insomniac Glow** (128, 304, 64x64) - Buff visualization, eyes wide open

### Row 7 - Yogurt Reboot (Y=368):
- **Tiny Cup** (0, 368, 48x48) - Balkan yogurt container
- **Expired Yogurt** (48, 368, 48x48) - Questionable expiration date visible
- **Warm Temperature Visual** (96, 368, 48x48) - Inappropriately room temp

### Row 8 - Belly Of Chadz (Y=416):
- **Dense Kebab Box** (0, 416, 96x64) - Heavy, sauce-soaked container
- **Three Sauces Soaked** (96, 416, 96x64) - Overlapping sauce colors
- **Ego Emanation Effect** (192, 416, 64x64) - Mr. Chadz's pride visualization

### Food Design Notes:
- Balance disgusting and mysteriously appealing in each item
- Mystery meat should be unidentifiable but well-seasoned
- Status effect visual cues integrated (grease = stamina, garlic = social rejection)
- Each item tells story of questionable choices and skilled preparation

---

## 🏙️ Sprite Sheet 4: Alley Environment Details
**File:** `alley_environment_details.png`  
**Dimensions:** 1024x768 pixels  
**Color Palette:** #2C2C2C (alley shadow), #FF6B35 (grease rainbow), #00FF00 (NFT neon), #696969 (chain-link gray)

### Rainbow Grease Puddles (Row 1, Y=0):
- **Small Puddle** (0, 0, 48x32) - Oil-slick shimmer effect
- **Medium Puddle** (48, 0, 96x48) - Rainbow reflection active
- **Large Puddle** (144, 0, 128x64) - Full spectrum grease beauty
- **Shimmer Frame 1** (272, 0, 64x48) - Animation cycle start
- **Shimmer Frame 2** (336, 0, 64x48) - Peak rainbow
- **Shimmer Frame 3** (400, 0, 64x48) - Cycle end

### Post-Party Debris (Row 2, Y=64):
- **Red Bull Cans** (0, 64, 32x48) - Scattered energy drinks
- **Condom Wrappers** (32, 64, 24x16) - Post-party evidence
- **Rave Flyer Pieces** (56, 64, 48x32) - Torn promotional material
- **Cigarette Butts** (104, 64, 16x8) - Multiple scattered
- **Mystery Stains** (120, 64, 64x32) - Unidentifiable spills

### NFT Wall Graffiti (Row 3, Y=128):
- **"NFT 4 LYFE" Base** (0, 128, 256x96) - Main graffiti tag
- **Additional Tags** (256, 128, 128x96) - Supporting crypto art
- **Faded Older Graffiti** (384, 128, 96x96) - Layers of street art history

### Chain-Link Fence (Row 4, Y=224):
- **Normal Section** (0, 224, 128x96) - Standard fence
- **Damaged Section** (128, 224, 128x96) - Bent, broken links
- **Debris-Caught Section** (256, 224, 128x96) - Trash stuck in fence

### Rat and Chili Pepper (Row 5, Y=320):
- **Rat Gnaw Frame 1** (0, 320, 32x24) - Starting to bite
- **Rat Gnaw Frame 2** (32, 320, 32x24) - Mid-bite
- **Rat Gnaw Frame 3** (64, 320, 32x24) - Chewing motion
- **Rat Gnaw Frame 4** (96, 320, 32x24) - Swallow, return
- **Intact Chili Pepper** (128, 320, 16x24) - Fresh pepper
- **Gnawed Chili Pepper** (144, 320, 16x24) - Bite marks visible

### Environmental Notes:
- Rainbow grease puddles should be beautiful despite being hazards
- Rat casually gnawing pepper, obviously present but accepted
- Post-party debris tells years of operation history
- NFT graffiti represents cultural moment (background detail only)

---

## 🌫️ Sprite Sheet 5: Kebab Stand Particle Effects
**File:** `kebab_stand_particle_effects.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #F5F5F5 (steam white), #FFD700 (grease vapor), #708090 (smoke gray)

### Cooking Steam (Row 1, Y=0):
- **Steam Wisp 1** (0, 0, 16x24) - Continuous emission variation
- **Steam Wisp 2** (16, 0, 16x24) - Rising pattern variation
- **Steam Wisp 3** (32, 0, 16x24) - Dispersal variation
- **Steam Wisp 4** (48, 0, 16x24) - Full dissipation

### Grease Vapor (Row 2, Y=24):
- **Small Particle** (0, 24, 8x8) - Tiny grease droplet
- **Medium Particle** (8, 24, 12x12) - Standard vapor
- **Droplet Effect** (20, 24, 8x16) - Falling grease drop

### Cigarette Smoke (Row 3, Y=40):
- **Curl Variation 1** (0, 40, 24x32) - Ambient haze pattern
- **Curl Variation 2** (24, 40, 24x32) - Secondary curl
- **Curl Variation 3** (48, 40, 24x32) - Dispersing smoke

### Urban Debris Flutter (Row 4, Y=72):
- **Paper Scrap** (0, 72, 12x12) - Floating litter
- **Plastic Fragment** (12, 72, 8x8) - Wind-blown trash
- **Food Wrapper** (20, 72, 16x12) - Kebab packaging debris

### Particle Emission Rates:
- **Cooking Steam:** 5 particles/second from rotisserie
- **Grease Vapor:** 3 particles/second from drip tray
- **Cigarette Smoke:** 2 particles/second ambient
- **Urban Debris:** Random flutter 1 particle every 2-3 seconds

---

## 📐 Mobile Optimization Requirements

### Texture Compression by Platform:
- **iOS:** PVRTC 4BPP for fluorescent lighting, maintains harsh brightness
- **Android:** ETC2 with alpha for steam particle transparency
- **Fallback:** PNG at high quality for menu item detail preservation

### Sprite Atlasing Strategy:
- **Cart Complete Atlas:** Base + rotisserie + signage + lighting (1024x768)
- **Character Atlas:** Mr. Chadz all states + outfit elements (512x512)
- **Menu Items Atlas:** All 8 food items with variations (1024x512)
- **Environment Atlas:** Puddles + debris + fence + rat (1024x768)
- **Effects Atlas:** All particle systems combined (512x256)
- **Max Atlas Size:** 2048x2048 for mobile GPU compatibility

### LOD (Level of Detail) Scaling:
- **High-End Devices:** Full steam effects, 4-frame rotisserie, rainbow grease shimmer
- **Medium Devices:** Reduced particles, 2-frame rotisserie, simplified grease effects
- **Low-End Devices:** Minimal steam, static rotisserie position, no shimmer animation
- **Potato Mode:** Essential cart and character only, no particle effects

### Performance Targets:
- **Target FPS:** 50 fps (open environment optimization)
- **Max Draw Calls:** 12 per frame
- **Memory Footprint:** 30MB maximum for location

---

## ♿ Accessibility Sprite Requirements

### High Contrast Menu Items:
- **Enhanced Food Visibility** (0, 448, 512x64) - All menu items with increased contrast
- **Status Effect Icons Clear** (0, 512, 256x32) - Buff/debuff indicators emphasized
- **Price Display Readable** (256, 512, 128x32) - Kebab coin costs visible

### Visual Audio Cues:
- **Sizzle Visual** (0, 544, 24x24) - Cooking sound indicator
- **Phone Buzz Visual** (24, 544, 24x24) - Mr. Chadz call notification
- **LED Flicker Warning** (48, 544, 32x16) - Strobe alternative indicator

### Motion Sensitivity Options:
- **Static Rotisserie** (384, 544, 64x96) - Non-rotating meat alternative
- **Reduced Steam** (448, 544, 32x48) - Minimal particle mode
- **No Flicker Lighting** (480, 544, 128x48) - Steady fluorescent alternative

---

## 🎬 Animation Sequence Specifications

### Rotisserie Meat Rotation:
- **Duration:** 0.5 seconds per 90° frame (2 RPM total)
- **Pattern:** Continuous hypnotic rotation
- **Audio Sync:** Mechanical hum matches visual rotation
- **Purpose:** Mesmerizing food preparation, mystery meat appeal

### Mr. Chadz Phone Checking:
- **Trigger:** Every 10-15 seconds during idle
- **Duration:** 4-frame sequence, 2 seconds total
- **Pattern:** Check phone → read message → react → pocket
- **Purpose:** Sketchy business operations, bouncer background reveal

### LED Strip Flicker:
- **Trigger:** Random intervals 0.5-2 seconds
- **Pattern:** Normal → dim → spark → normal
- **Visual:** Electrical instability, unsafe wiring
- **Purpose:** Health code violation atmosphere

### Rat Gnawing Chili Pepper:
- **Duration:** 1.5 second loop cycle
- **Pattern:** Approach → bite → chew → swallow
- **Visibility:** Constantly present, casually accepted
- **Purpose:** Obvious health violation normalized

### Rainbow Grease Shimmer:
- **Duration:** 3-frame cycle, 2 seconds total
- **Pattern:** Dull → rainbow peak → dull
- **Visual:** Oil-slick beauty despite hazard
- **Purpose:** Environmental comedy, beautiful grotesque

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Animation system: Frame-based with JSON timing
- Particle systems: CPUParticles2D for mobile performance
- Menu system: Inventory UI integration for 8 items

### Audio Sync Points:
- Rotisserie hum syncs with rotation visual
- Grease sizzle punctuates active cooking state
- Mr. Chadz phone notifications trigger animation
- LED electrical buzz on flicker frames
- Menu item purchases have unique audio per food type

### Quest Integration:
- **Great Döner Debate:** "Belly Of Chadz" serves as Debaucheryville sample
- **Status Effect Pipeline:** Hangover cures connect to club/arcade locations
- **Repeat Customer:** Purchase tracking unlocks backstory dialogue
- **Achievement System:** Contributes to "World's Pickiest Drunk" badge

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Post-party desperation meets sketchy entrepreneur"
- **Color Mood:** Harsh fluorescent white, grease rainbow, alley shadows
- **Lighting:** Blinding cart brightness contrasts with dim alley darkness
- **Texture:** Grease accumulation everywhere, mystery meat appeal

### Mr. Chadz Character Direction:
- **Personality:** Deadpan bouncer-turned-kebabist, sketchy but skilled
- **Key Visual:** Glittery crop top over bulletproof vest (absurd contrast)
- **Movement:** One-handed food service while managing phone calls
- **Expression:** Never breaks deadpan, treats violations as selling points

### Food Design Philosophy:
- Each item balances disgusting and mysteriously appealing
- Mystery meat unidentifiable but well-seasoned when hungry
- Status effect visual cues integrated naturally
- Strategic gameplay benefits justify questionable quality

### Environmental Storytelling:
- Rainbow grease puddles beautiful despite being hazards
- Rat gnawing pepper obviously present but casually accepted
- Post-party debris shows years of late-night operation
- NFT graffiti represents cultural moment without dominating

---

## 📦 File Delivery Checklist

### Required PNG Files (5 Total):
- [ ] `mr_chadz_kebab_cart_complete.png` (1024x768)
- [ ] `mr_chadz_kebab_vendor.png` (512x512)
- [ ] `kebab_menu_items_detailed.png` (1024x512)
- [ ] `alley_environment_details.png` (1024x768)
- [ ] `kebab_stand_particle_effects.png` (512x256)

### Quality Requirements:
- **Format:** PNG-24 with alpha channel
- **Color Space:** sRGB
- **DPI:** 72 (screen resolution)
- **Compression:** Lossless PNG
- **Naming Convention:** snake_case, all lowercase
- **Layer Organization:** Preserve for menu updates

### Delivery Format:
- **Primary:** Individual PNG files per specifications
- **Backup:** Master PSD/Photoshop with organized layers
- **Documentation:** Menu item effects guide for balance testing

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Mr. Chadz Outfit** - Glittery crop top + bulletproof vest absurdity
2. **Mystery Meat Rotisserie** - Hypnotic rotation of unidentifiable food
3. **Rainbow Grease Puddles** - Beautiful environmental hazards
4. **Health Code Violations** - Rat gnawing pepper while customers eat
5. **Menu Items** - Each food perfectly disgusting yet appealing

### TikTok Potential:
- "Trying the most sketchy kebab stand in gaming"
- "Mr. Chadz handling business calls while serving food"
- "POV: You ignore obvious health violations because you're drunk"
- "When the food vendor's outfit is the real mystery"

### Twitter/X Quote Potential:
- "The FDA stopped returning my emails in 2019."
- "I call this one 'intestinal roulette.' You want two?"
- "Meat's mostly legal. Heat lamp's all vibes."

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 5 PNG files match exact dimensions
- [ ] Mr. Chadz 6'4" proportions feel imposing
- [ ] Glittery crop top contrasts absurdly with bulletproof vest
- [ ] All 8 menu items balance disgusting and appealing
- [ ] Rotisserie 4-frame animation flows smoothly at 2 RPM
- [ ] Rainbow grease puddles shimmer beautifully
- [ ] Rat gnawing animation obvious but casual
- [ ] LED strip flicker creates electrical instability
- [ ] Steam particles emit from all correct points
- [ ] Color palette matches hex codes
- [ ] Accessibility alternatives included
- [ ] File naming follows convention
- [ ] Master files preserved for updates

### Quality Checkpoints:
- [ ] Mr. Chadz captures deadpan sketchy entrepreneur perfectly
- [ ] Food items create strategic gameplay decisions
- [ ] Environmental details tell post-party operation story
- [ ] Health code violations normalized as atmosphere
- [ ] Mystery meat both repulsive and appealing when hungry
- [ ] All elements support "desperate tourists meet exploitation" theme
- [ ] Social media viral potential maximized
- [ ] Mobile performance optimized for particle effects

**Once validated, the Late-Night Kebab Stand becomes the essential post-party recovery location where players make questionable food choices for strategic gameplay benefits while Mr. Chadz provides deadpan commentary on his sketchy operation!**