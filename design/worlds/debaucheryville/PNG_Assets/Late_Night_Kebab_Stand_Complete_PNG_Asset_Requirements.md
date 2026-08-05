# Late-Night Kebab Stand - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Late-Night Kebab Stand - the spiritual equivalent of an edible walk of shame, a symphony of salt, shame, and mystery meat.

**Location ID:** `debaucheryville_velvet_alley_kebab_01`  
**Theme:** Greasy post-party lifeline for blackout characters, sketchy street food exploitation  
**Zone:** Velvet Alley — near the Velvet Curtain Club alley exit, wedged between chain-link fence and NFT-graffitied wall  
**Hours:** Always accessible (24/7), thrives during post-party hours (10 PM – 6 AM)  
**Primary Function:** Consumable vendor, grease-cure items, status management, Great Döner Debate sample

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Fluorescent White | #FFFFFF | Cart lighting bank, blinding illumination states |
| Grease Rainbow Orange | #FF6B35 | Grease puddles, food sheen, drip tray buildup |
| Alley Shadow | #2C2C2C | Environment darks, fence, night alley surfaces |
| Glitter Pink | #FF1493 | Mr. Chadz's glittery crop top, LED strip accents |
| Vest Gray | #4B4B4B | Bulletproof vest, cart metal fixtures |
| Gold | #FFD700 | Outfit gold accents, kebab coin icon |
| Burner Black | #000000 | Burner phone, deepest shadows, off-state LEDs |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/late_night_kebab_stand/
├── environment/
│   └── alley_environment_details.png
├── npcs/
│   └── mr_chadz_kebab_vendor.png
├── objects/
│   ├── mr_chadz_kebab_cart_complete.png
│   └── kebab_menu_items_detailed.png
├── effects/
│   └── kebab_stand_particle_effects.png
└── ui/
    └── kebab_stand_ui.png
```

---

## 🍖 Sprite Sheet 1: Mr. Chadz Kebab Cart Complete
**File:** `mr_chadz_kebab_cart_complete.png`  
**Dimensions:** 1024x768 pixels  
**Color Palette:** #FFFFFF (fluorescent white), #FF6B35 (grease rainbow), #2C2C2C (alley shadow)

### Cart Base States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Idle | (0, 0) | 384x256 | Cart ready for business |
| Active Cooking | (384, 0) | 384x256 | Steam, activity |
| Cleaning Mode | (768, 0) | 256x256 | Rare sight |

### Vertical Rotisserie (96x192 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Meat Frame 1 | (0, 256) | Starting position |
| Meat Frame 2 | (96, 256) | 90° rotation |
| Meat Frame 3 | (192, 256) | 180° rotation |
| Meat Frame 4 | (288, 256) | 270° rotation |
| Mechanism | (384, 256) | Motor/mount 64x192 |
| Drip Tray | (448, 256) | Grease collector 96x48 |

### Fluorescent Lighting (256x64 each):
| State | Position | Description |
|-------|----------|-------------|
| Full Brightness | (0, 448) | Blinding white |
| Flickering Dim | (256, 448) | Power issues |
| Electrical Issues | (512, 448) | Buzzing state |

### Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Sign | (0, 512) | 256x96 | "MR. CHADZ KEBABS" faux-Arabic |
| LED Strip On | (256, 512) | 192x32 | Full glow |
| LED Strip Flicker | (256, 544) | 192x32 | Inconsistent |
| LED Strip Off | (256, 576) | 192x32 | Dead |
| Hookah Hose Mount | (448, 512) | 64x96 | LED attachment point |

### Effects Points:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Steam Emission 1-3 | (0-64, 608) | 32x32 ea | Spawn points |
| Grease Light | (96, 608) | 64x32 | Minimal buildup |
| Grease Medium | (160, 608) | 64x32 | Standard |
| Grease Heavy | (224, 608) | 64x32 | Health code violation |

---

## 👨‍🍳 Sprite Sheet 2: Mr. Chadz Vendor
**File:** `mr_chadz_kebab_vendor.png`  
**Dimensions:** 512x512 pixels  
**Color Palette:** #FF1493 (glittery crop top), #4B4B4B (bulletproof vest), #FFD700 (gold accents), #000000 (burner phone)

### Idle Phone Checking (96x128 each):
| Frame | Position | Description |
|-------|----------|-------------|
| Frame 1 | (0, 0) | Looking at phone |
| Frame 2 | (96, 0) | Typing response |
| Frame 3 | (192, 0) | Concerned expression |
| Frame 4 | (288, 0) | Back to business |

### Food Service Actions (96x128 each):
| Action | Position | Description |
|--------|----------|-------------|
| Prep Ingredients | (0, 128) | Slicing mystery meat |
| Wrapping | (96, 128) | Foil technique |
| Serving | (192, 128) | Handoff |
| Payment | (288, 128) | Taking kebab coins |

### Business Reactions (96x128 each):
| Reaction | Position | Description |
|----------|----------|-------------|
| Supplier Concerns | (0, 256) | Worried call |
| Health Inspector Panic | (96, 256) | Hiding evidence |
| Sketchy Negotiations | (192, 256) | Lowered voice |
| Deadpan Stare | (288, 256) | Judging choices |

### Outfit Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Glittery Crop Top | (0, 384) | 64x64 | Essential absurdity |
| Bulletproof Vest | (64, 384) | 64x64 | Practical fashion |
| Burner Phone | (128, 384) | 32x48 | Business device. Screen may show a crypto price-alert banner or ticker row — see Crypto Scope below |
| 6'4" Proportions | (368, 0) | 64x96 | Full height reference sprite *(coordinates from legacy 64x96 grid — re-layout needed for new 96x128 grid)* |
| Deadpan Expression | (432, 0) | 32x32 | Face close-up, no emotion *(coordinates from legacy 64x96 grid — re-layout needed for new 96x128 grid)* |

**Mr. Chadz Visual Notes:**
- 6'4" imposing height with deadpan expression
- Glittery crop top OVER bulletproof vest (non-negotiable)
- One-handed food service while on phone
- Bouncer-turned-kebabist energy

### Mr. Chadz Character Direction:
- **Personality:** Deadpan bouncer-turned-kebabist, sketchy but skilled
- **Key Visual:** Glittery crop top over bulletproof vest (absurd contrast)
- **Movement:** One-handed food service while managing phone calls
- **Expression:** Never breaks deadpan, treats violations as selling points — including when the phone buzzes with a price alert. The glance is identical to the supplier glance. He does not react

### ⚠️ Crypto Scope at This Location (author ruling — supersedes any blanket "no crypto" note)
**The burner phone screen is the only crypto-legible surface at the Late-Night Kebab Stand, and it is permitted.**
- ✅ **Permitted, phone screen only:** a price-alert banner or a small ticker row. Keep it tiny and unreadable at sprite scale — the read is "his phone is doing something," not "here is a market." If a ticker is legible in any close-up or portrait asset, it uses a master-pool coin only; **`$KBAB`** (KebabSwap) is the canonical pairing for this cart, per `design/economy/shitcoin_master_pool.md`.
- ✅ **Permitted:** the existing "NFT 4 LYFE" wall graffiti, unchanged, as period-satire set dressing.
- ❌ **Not permitted anywhere else at this location:** kiosk or terminal hardware, wallet UI, coin logos or wordmarks on the cart, signage, menu board, packaging, certificates, or crypto pricing on any menu item. Prices are Sovs and Kebab Coins; that does not change.
- **Register:** crypto here is a background gag (2% of game max), never a mechanic and never a plot element. Mr. Chadz half-follows the alerts and acts on none of them.

---

## 🥙 Sprite Sheet 3: Menu Items Detailed
**File:** `kebab_menu_items_detailed.png`  
**Dimensions:** 1024x512 pixels  

### Gutbuster Wrap - 6 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Wrapped | (0, 0) | 128x96 | Foil presentation |
| Unwrapped Dripping | (128, 0) | 128x96 | Mystery lamb visible |
| Cross Section | (256, 0) | 96x96 | Interior horror |

### Vampire Slayer Garlic Fries - 4 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Container | (352, 0) | 96x96 | Week-old oil sheen |
| Sauce Dripping | (448, 0) | 96x96 | Pepper spray levels |
| Oil Shimmer | (544, 0) | 64x64 | Rainbow grease |

### EuroMeat Pocket™ - 5 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Full View | (0, 96) | 128x96 | Soggy pita exterior |
| Grey Filling | (128, 96) | 96x96 | Suspiciously grey |
| Microwaved Steam | (224, 96) | 64x64 | Reheated evidence |

### MegaMix Box - 9 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Closed | (288, 96) | 128x96 | Cardboard coffin |
| Horrifying Contents | (416, 96) | 128x96 | Everything visible |
| Regret Visualization | (544, 96) | 96x96 | Immediate consequences |

### Drunken Sauce Shot - 2 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Thimble | (0, 192) | 48x64 | Plastic container |
| Sauce Swirl | (48, 192) | 48x64 | Hot sauce/mayo mix |
| Dysentery Warning | (96, 192) | 64x32 | Side effect hint |

### Lambsomnia Special - 7 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Full Plate | (160, 192) | 128x96 | Spiced lamb beauty |
| Sleepless Tzatziki | (288, 192) | 64x64 | Insomniac sauce |
| Insomniac Glow | (352, 192) | 64x64 | Buff visual |

### Yogurt Reboot - 3 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Tiny Cup | (416, 192) | 64x64 | Questionable container |
| Expired Yogurt | (480, 192) | 64x64 | Warm and concerning |
| Expiration Date | (544, 192) | 48x24 | Clearly past |

### Belly Of Chadz - 6 Sovs:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Dense Box | (0, 288) | 128x96 | Three-sauce soaked |
| Three Sauces | (128, 288) | 96x96 | Sauce layers |
| Ego Emanation | (224, 288) | 64x64 | Pride visualization |

**Food Art Direction:**
- Balance disgusting and mysteriously appealing
- Each item should look questionable but well-seasoned
- Mystery meat unidentifiable but appetizing when hungry
- Status effect visual cues integrated

---

## 🏚️ Sprite Sheet 4: Alley Environment Details
**File:** `alley_environment_details.png`  
**Dimensions:** 1024x768 pixels  

### Rainbow Grease Puddles:
| Size | Position | Dimensions | Description |
|------|----------|------------|-------------|
| Small | (0, 0) | 64x32 | Minor spill |
| Medium | (64, 0) | 96x48 | Standard puddle |
| Large | (160, 0) | 128x64 | Major accumulation |
| Shimmer 1 | (0, 64) | 128x64 | Oil-slick iridescence |
| Shimmer 2 | (128, 64) | 128x64 | Animation frame |
| Shimmer 3 | (256, 64) | 128x64 | Animation frame |

### Post-Party Debris:
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Red Bull Can | (0, 128) | 24x32 | Empty, crushed |
| Condom Wrapper | (24, 128) | 16x16 | Crumpled |
| Rave Flyer | (40, 128) | 32x24 | Overturned |
| Cigarette Butts | (72, 128) | 24x8 | Multiple |
| Mystery Stain | (96, 128) | 48x32 | Don't ask |

### NFT Graffiti:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Tag | (0, 160) | 192x96 | "NFT 4 LYFE" |
| Additional Tags | (192, 160) | 128x96 | Supporting graffiti |
| Faded Older | (320, 160) | 96x96 | Previous generations |

### Chain-Link Fence (128x192 each):
| State | Position | Description |
|-------|----------|-------------|
| Normal | (0, 256) | Intact |
| Damaged | (128, 256) | Holes, rust |
| Debris Caught | (256, 256) | Trash trapped |

### Carlos the Rat:
| Frame | Position | Size | Description |
|-------|----------|------|-------------|
| Gnaw 1 | (0, 448) | 48x32 | Bite motion |
| Gnaw 2 | (48, 448) | 48x32 | Chewing |
| Gnaw 3 | (96, 448) | 48x32 | Swallow |
| Gnaw 4 | (144, 448) | 48x32 | Return |
| Chili Intact | (192, 448) | 24x16 | Full pepper |
| Chili Gnawed | (216, 448) | 24x16 | Half eaten |

---

## ✨ Sprite Sheet 5: Particle Effects
**File:** `kebab_stand_particle_effects.png`  
**Dimensions:** 512x256 pixels  

### Cooking Steam (32x48 each):
| Wisp | Position | Description |
|------|----------|-------------|
| Wisp 1 | (0, 0) | Initial rise |
| Wisp 2 | (32, 0) | Expanding |
| Wisp 3 | (64, 0) | Dissipating |
| Wisp 4 | (96, 0) | Fading |

### Grease Vapor:
| Type | Position | Size | Description |
|------|----------|------|-------------|
| Small | (0, 48) | 16x24 | Light vapor |
| Medium | (16, 48) | 24x32 | Heavier |
| Droplet | (40, 48) | 8x12 | Falling grease |

### Cigarette Smoke (24x32 each):
| Curl | Position | Description |
|------|----------|-------------|
| Curl 1 | (0, 80) | Tight spiral |
| Curl 2 | (24, 80) | Expanding |
| Curl 3 | (48, 80) | Dissipating |

### Urban Debris:
| Type | Position | Size | Description |
|------|----------|------|-------------|
| Paper Scrap | (0, 112) | 16x12 | Wind-blown |
| Plastic Fragment | (16, 112) | 12x8 | Floating |
| Food Wrapper | (28, 112) | 20x16 | Tumbling |

### Particle Emission Rates:
- **Cooking Steam:** 5 particles/second from rotisserie
- **Grease Vapor:** 3 particles/second from drip tray
- **Cigarette Smoke:** 2 particles/second ambient
- **Urban Debris:** Random flutter 1 particle every 2-3 seconds

---

## 🎮 Sprite Sheet 6: UI Elements
**File:** `kebab_stand_ui.png`  
**Dimensions:** 384x256 pixels  

### Menu Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu Panel | (0, 0) | 256x192 | Background |
| Button Normal | (0, 192) | 64x32 | Unselected |
| Button Hover | (64, 192) | 64x32 | Highlighted |
| Button Selected | (128, 192) | 64x32 | Chosen |

### Status Effect Icons (32x32 each):
| Icon | Position | Description |
|------|----------|-------------|
| Greaseburp | (256, 0) | Burp bubble |
| Socially Rejected | (288, 0) | Distance icon |
| Meat Doubt | (320, 0) | Question mark |
| Greasy Coma | (352, 0) | Drowsy eyes |
| Insomniac Clarity | (256, 32) | Wide awake |
| Dysentery Light | (288, 32) | Bathroom warning |

### Currency:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kebab Coin Icon | (256, 64) | 24x24 | Payment display |

---

## 🎬 Animation Specifications

### Rotisserie Spin:
- **Pattern:** Meat Frame 1 → 2 → 3 → 4 (loop)
- **Speed:** 2 RPM (hypnotic, continuous)
- **Purpose:** Centerpiece animation, draws attention

### LED Strip Flicker:
- **Pattern:** On → Flicker → On → Off → On
- **Timing:** Random 0.5-2 seconds between states
- **Purpose:** Electrical instability atmosphere

### Mr. Chadz Phone Check:
- **Pattern:** Frame 1 → 2 → 3 → 4 → 3 → 2
- **FPS:** 4
- **Trigger:** Every 10-15 seconds
- **Duration:** 3 seconds
- **Purpose:** Business call handling

### Carlos Gnawing:
- **Pattern:** Gnaw 1 → 2 → 3 → 4 (loop)
- **FPS:** 3
- **Cycle:** 1.5 seconds
- **Purpose:** Quality control in action

### Grease Puddle Shimmer:
- **Pattern:** Shimmer 1 → 2 → 3 (loop)
- **FPS:** 2
- **Purpose:** Beautiful horror of oil-slick rainbow

---

## ♿ Accessibility Sprite Requirements

*(coordinates from legacy 64x96 grid — re-layout needed for new 96x128 grid)*

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

### Colorblind Considerations:
- Status effect icons pair distinct shapes with color (bubble, question mark, drowsy eyes) so no buff/debuff is color-only
- Grease puddle hazards readable by shimmer pattern, not hue alone
- Touch zones minimum 44px for all menu buttons and interactive cart elements

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) for fluorescent lighting, maintains harsh brightness with alpha for steam particle transparency
- **Fallback:** PNG at high quality for menu item detail preservation

### Sprite Atlasing Strategy:
- **Cart Complete Atlas:** Base + rotisserie + signage + lighting (1024x768)
- **Character Atlas:** Mr. Chadz all states + outfit elements (512x512)
- **Menu Items Atlas:** All 8 food items with variations (1024x512)
- **Environment Atlas:** Puddles + debris + fence + rat (1024x768)
- **Effects Atlas:** All particle systems combined (512x256)
- **Max Atlas Size:** 2048x2048 for broad GPU compatibility

### LOD (Level of Detail) Scaling:
- **High-End Devices:** Full steam effects, 4-frame rotisserie, rainbow grease shimmer
- **Medium Devices:** Reduced particles, 2-frame rotisserie, simplified grease effects
- **Low-End Devices:** Minimal steam, static rotisserie position, no shimmer animation
- **Potato Mode:** Essential cart and character only, no particle effects

### Performance Targets:
- **Target FPS:** 60 fps (open environment optimization)
- **Max Draw Calls:** 12 per frame
- **Memory Footprint:** 30MB maximum for location

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

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Velvet Curtain Club | Alley exit adjacency — fluorescent glare visible from club's back door; shared alley wall graffiti | Club bass muffles as sizzle and fluorescent hum rise |
| Absinthe Arcade | Status effect pipeline — grease-cure items counter arcade-acquired debuffs | Standard street transition, status icons persist |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "An edible walk of shame under fluorescent interrogation lighting"
- **Color Mood:** Blinding fluorescent white slammed against alley shadow; grease-rainbow orange and glitter pink supply the absurdity
- **Lighting:** Single harsh fluorescent bank with flicker states plus LED strip accents — no soft light anywhere in the alley
- **Texture:** Grease film on every surface, foil shine, damp asphalt, rusted chain-link

### Environmental Storytelling:
- Rainbow grease puddles beautiful despite being hazards
- Rat gnawing pepper obviously present but casually accepted
- Post-party debris shows years of late-night operation
- NFT graffiti represents cultural moment without dominating

### Character Integration Notes:
- Mr. Chadz rendered at 6'4" scale relative to the cart counter; deadpan expression never changes across all states
- Carlos the Rat sits on the environment layer, not the NPC layer — a casual fixture, never a threat
- Drunk customer NPCs (separate sprite sheets) queue along the chain-link fence, lit by fluorescent spill

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Mr. Chadz** - Glittery crop top over bulletproof vest
2. **Rainbow Grease Puddles** - Beautiful health hazards
3. **Carlos the Rat** - Quality control gnawing chili
4. **Mystery Meat Rotisserie** - Hypnotic spinning
5. **MegaMix Box** - Cardboard coffin of regret
6. **NFT 4 LYFE Graffiti** - Cultural time capsule

### Quote Potential:
- "I call this one 'intestinal roulette.' You want two?"
- "The FDA stopped returning my emails in 2019."
- "Meat's mostly legal. Heat lamp's all vibes."
- "That rat? That's Carlos. He's quality control."
- "The Meat You Regret Tomorrow™"

---

## 📋 Required PNG Files (6 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | mr_chadz_kebab_cart_complete.png | 1024x768 |
| 2 | mr_chadz_kebab_vendor.png | 512x512 |
| 3 | kebab_menu_items_detailed.png | 1024x512 |
| 4 | alley_environment_details.png | 1024x768 |
| 5 | kebab_stand_particle_effects.png | 512x256 |
| 6 | kebab_stand_ui.png | 384x256 |

**Total Estimated Memory:** ~10 MB uncompressed RGBA (well within the 30MB location budget)

---

## 📦 File Delivery Checklist

### Required PNG Files (6 Total):
- [ ] `mr_chadz_kebab_cart_complete.png` (1024x768)
- [ ] `mr_chadz_kebab_vendor.png` (512x512)
- [ ] `kebab_menu_items_detailed.png` (1024x512)
- [ ] `alley_environment_details.png` (1024x768)
- [ ] `kebab_stand_particle_effects.png` (512x256)
- [ ] `kebab_stand_ui.png` (384x256)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha |
| Color Space | sRGB |
| DPI | 72 |
| Naming | snake_case |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/layered file with organized layer groups
- **Documentation:** Animation timing reference sheet

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 6 PNG files match exact dimensions
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
- [ ] Performance optimized for particle effects

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ PASS | Debaucheryville only |
| Cultural Specificity | ✅ PASS | European late-night kebab culture |
| Satirical Targets Appropriate | ✅ PASS | Desperate post-party tourists and sketchy exploitation, not locals |
| Seedy Underbelly Present | ✅ PASS | Health code violations as atmosphere, mystery meat economy |
| Gameplay Value Established | ✅ PASS | 8-item consumable vendor, status management, quest sample |
| Technical Feasibility | ✅ PASS | Mobile optimization documented |
| Performance Budget | ✅ PASS | 60 FPS, 12 draws, 30MB |
| Accessibility Features | ✅ PASS | Visual audio cues, motion sensitivity, high contrast options |
| Crypto Scope Bounded | ✅ PASS | Per author ruling, Mr. Chadz's burner-phone screen may show crypto price alerts (`$KBAB`, master pool) — the single permitted crypto surface here. "NFT 4 LYFE" graffiti remains period-satire set dressing. No kiosk, no wallet UI, no coin signage, no crypto pricing; no functional crypto anywhere at the location. See **Crypto Scope at This Location** under Sprite Sheet 2 |
| Social Media Integration | ✅ PASS | Six viral moments identified |

**The Late-Night Kebab Stand becomes the essential grease-cure station where 8 menu items provide strategic status management, Mr. Chadz dispenses mystery meat and wisdom in equal measure, Carlos provides quality control, and the Belly Of Chadz serves as Debaucheryville's official Great Döner Debate sample!**
