# Shadow Exchange - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for the Shadow Exchange underground bazaar. Each sprite sheet includes pixel-perfect coordinates, color specifications, and animation requirements for this officially unofficial economic hub.

**Location ID:** `debaucheryville_oldtown_shadow_exchange_01`
**Theme:** Old-world bank vault meets post-Soviet flea market — "Best Rates If You Don't Ask" financial grey-market satire
**Zone:** Sub-basement beneath Old Town backstreets
**Hours:** Always accessible once discovered (hidden cobblestone entrance behind market square, marked by "cash-only" candle)
**Primary Function:** Underground shop & economic hub — split-flap rate board mini-game, barter window, UV counterfeit checks, shady contracts, NFT hunt ledger, couchsurf trigger, Premium Stock post-boss unlock

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Stone Grey | #708090 | Vault arches, walls, fixer coats — main surfaces |
| UV Purple | #9400D3 | UV wand verification glow, shimmer accents |
| Vault Black | #1C1C1C | Background shadows, underground depth |
| Currency Gold | #FFD700 | Rate board, currency trays, toner-gold highlights |
| CRT Green | #00FF00 | Monitor wall market data displays |
| Crisis Red | #DC143C | Red rate ticks, crashing meme-coin charts, warnings |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/oldtown/
├── shadow_exchange_underground_complete.png
├── split_flap_rate_board_system.png
├── crt_monitor_wall_markets.png
├── shadow_exchange_npcs.png
├── atmospheric_npcs_types.png
└── underground_environmental_effects.png
```

---

## 🎨 Sprite Sheet 1: Shadow Exchange Underground Complete
**File:** `shadow_exchange_underground_complete.png`  
**Dimensions:** 1920x1080 pixels  
**Color Palette:** #708090 (stone grey), #9400D3 (UV purple), #1C1C1C (vault black), #FFD700 (currency gold)

### Vaulted Stone Arches (Wine-Cellar Repurposed):
- **Stone Arch Variation 1** (0, 0, 320x240) - Historical architecture, market conversion
- **Stone Arch Variation 2** (320, 0, 320x240) - Different angle, vault aesthetic
- **Stone Arch Variation 3** (640, 0, 320x240) - Third variation, post-communist style
- **Market Stall Conversion** (960, 0, 320x240) - Improvised infrastructure visible

### Iron Lattice Dividers:
- **Lattice Panel Design 1** (0, 240, 128x192) - Market stall separation
- **Lattice Panel Design 2** (128, 240, 128x192) - Alternative pattern
- **Counterfeit Handbags Hung** (256, 240, 96x128) - Grey market decoration
- **Deactivated Security Tags** (352, 240, 64x96) - Scattered evidence

### Wooden Counters with Currency Display:
- **Counter with Scratched Glass** (0, 432, 256x128) - Worn transaction surface
- **Currency Tray - Coins** (256, 432, 64x48) - Physical currency compartment
- **Currency Tray - Transit Cards** (320, 432, 64x48) - Travel document section
- **Currency Tray - Casino Chips** (384, 432, 64x48) - Gaming token area
- **Currency Tray - Arcade Tokens** (448, 432, 64x48) - Entertainment currency

### Lighting Systems:
- **Single Desk Lamp** (0, 560, 128x96) - Illuminating Shadow Ledger area
- **Cigarette-Burned Tealights** (128, 560, 32x32) - Stairwell entrance lighting
- **UV Wand Illumination** (160, 560, 96x64) - Purple glow for verification
- **CRT Monitor Glow** (256, 560, 128x96) - Multiple screen ambient light

### Underground Vault Atmosphere:
- **Stone Wall Texture** (512, 432, 256x256) - Cold vault material
- **Worn Floor Stones** (768, 432, 256x256) - Years of foot traffic
- **Atmospheric Lighting Overlay** (1024, 0, 896x640) - Complete mood enhancement

### Technical Notes:
- Stone arches suggest historical wine cellar repurposed
- Iron lattice creates market stall divisions
- Currency displays show multi-currency operation
- Lighting creates underground vault mood

---

## 🔄 Sprite Sheet 2: Split-Flap Rate Board System
**File:** `split_flap_rate_board_system.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #FFD700 (rate gold), #32CD32 (green tick), #DC143C (red tick), #708090 (mechanical grey)

### Rate Board Infrastructure:
- **Board Frame Complete** (0, 0, 256x128) - Mechanical housing structure
- **Split-Flap Mechanism** (256, 0, 128x64) - Visible mechanical components
- **Broker Mood Display** (384, 0, 128x64) - Market psychology indicator

### Split-Flap Letters and Numbers:
- **Alphabet A-M** (0, 128, 208x32) - First half of letter set
- **Alphabet N-Z** (208, 128, 208x32) - Second half of letter set
- **Numbers 0-9** (0, 160, 160x32) - Complete number set
- **Defunct & Novelty Marks** (160, 160, 96x32) - Six 16x32 split-flap tiles for the board's dead-money column. Shadow Exchange is the game's **only** sanctioned money changer and it deals exclusively in defunct, foreign and novelty currency nobody else accepts (`Design/Economy/currency.md`, "THE ONE EXCEPTION"). The six flaps: **(1)** the guilder hook — a stroked lowercase `f`, ties to De Guldenvreter; **(2)** a small crown silhouette with a bar struck through it — the dead crown of a country that stopped issuing; **(3)** a casino-chip pip — notched-rim disc; **(4)** an arcade/transit token — octagon with a centre hole; **(5)** a skull-over-coin — the demonetised tile; **(6)** a hand-inked `?` — the catch-all for whatever the back alley is pretending has value this week. **No euro tile: euros do not exist in this game.** **No `SOVS` tile either** — the board prices worthless paper; Sovs are what you hand Mrs. Rata at the counter, never a line on the board.

### Rate Change Indicators (Mini-Game System):
- **Green Tick Frame 1** (0, 192, 32x32) - Favorable rate start
- **Green Tick Frame 2** (32, 192, 32x32) - Peak favorable timing
- **Green Tick Frame 3** (64, 192, 32x32) - Favorable fade
- **Red Tick Frame 1** (96, 192, 32x32) - Unfavorable rate warning
- **Red Tick Frame 2** (128, 192, 32x32) - Peak unfavorable timing
- **Red Tick Frame 3** (160, 192, 32x32) - Unfavorable fade
- **Neutral Display** (192, 192, 32x32) - Standard rate state

### Mechanical Animation Frames:
- **Split-Flap Position 1** (0, 224, 64x32) - Letter flip sequence start
- **Split-Flap Position 2** (64, 224, 64x32) - Mid-flip motion blur
- **Split-Flap Position 3** (128, 224, 64x32) - Flip complete, next letter
- **Clacking Audio Visual** (192, 224, 48x32) - Sound effect indicator

### Mini-Game Timing Notes:
- Green tick: Favorable rates, player should interact
- Red tick: Unfavorable rates, player should wait
- Clacking updates: 3-5 second intervals
- Street Rep/Charm stats nudge board temporarily

---

## 🖥️ Sprite Sheet 3: CRT Monitor Wall Markets
**File:** `crt_monitor_wall_markets.png`  
**Dimensions:** 512x384 pixels  
**Color Palette:** #00FF00 (CRT green), #708090 (monitor grey), #FFD700 (data gold), #DC143C (crash red)

### CRT Monitor Array (4 Screens):
- **Monitor 1 - Kebab Prices** (0, 0, 128x96) - Food vendor market data
- **Monitor 2 - Nightclub Covers** (128, 0, 128x96) - Entertainment pricing
- **Monitor 3 - Meme Coins** (256, 0, 128x96) - Cryptocurrency parody
- **Monitor 4 - General Markets** (384, 0, 128x96) - Broader economic indicators

### Pixelized Data Display Content:
- **Kebab Price Chart** (0, 96, 96x64) - Food market fluctuation graph
- **Cover Charge List** (96, 96, 96x64) - Venue pricing scrolling text
- **Meme Coin Candles** (192, 96, 96x64) - Rising/crashing patterns
- **Market Ticker Scroll** (288, 96, 224x32) - Continuous data stream

### CRT Screen Effects:
- **Normal Flicker State** (0, 160, 128x96) - Standard display
- **Dim Flicker Variation** (128, 160, 128x96) - Power fluctuation
- **Screen Refresh Lines** (256, 160, 128x96) - Authentic CRT scan
- **CRT Curve Overlay** (384, 160, 128x96) - Retro screen distortion

### Data Animation Frames:
- **Kebab Prices Rising** (0, 256, 64x32) - Upward trend
- **Kebab Prices Falling** (64, 256, 64x32) - Downward trend
- **Meme Coin Pump** (128, 256, 64x32) - Rapid increase
- **Meme Coin Dump** (192, 256, 64x32) - Rapid crash
- **Ticker Scroll Frame 1** (256, 256, 128x32) - Continuous movement
- **Ticker Scroll Frame 2** (384, 256, 128x32) - Next position

### Technical Notes:
- Authentic CRT curve for retro atmosphere
- Pixelized data reinforces underground aesthetic
- Market parody (kebabs, meme coins) satirizes financial culture
- Continuous animation for living bazaar feel

---

## 👥 Sprite Sheet 4: Shadow Exchange Main NPCs
**File:** `shadow_exchange_npcs.png`  
**Dimensions:** 512x512 pixels  
**Character Size:** 64x96 base sprites
**Color Palette:** #708090 (clerk grey), #9400D3 (UV purple), #FFD700 (token gold), #DC143C (crisis red)

### Mrs. Rata (Main Clerk) - 64x96 each:
- **Idle Professional** (0, 0) - Deadpan bureaucratic efficiency
- **Calculator Checking Frame 1** (64, 0) - Obsessive rate calculation
- **Calculator Checking Frame 2** (128, 0) - Multiple calculators visible
- **Calculator Checking Frame 3** (192, 0) - Cross-referencing rates
- **Calculator Checking Frame 4** (256, 0) - Final verification
- **Paperwork Stamping** (320, 0) - Legitimizing transactions
- **Suspicious Glance** (384, 0) - Notoriety threshold warning

### The UV Man (Counterfeit Specialist) - 64x96 each:
- **Idle Testing Position** (0, 96) - Professional authentication stance
- **UV Wand Scanning Frame 1** (64, 96) - Beginning verification
- **UV Wand Scanning Frame 2** (128, 96) - Active purple glow
- **UV Wand Scanning Frame 3** (192, 96) - Final authentication
- **Counterfeit Detection** (256, 96) - Revealing fake currency
- **Tool Sales Pitch** (320, 96) - Pocket UV Wand marketing
- **Authentic Approval** (384, 96) - Money verified legitimate

### Token Goblin (Specialty Currency) - 64x96 each:
- **Arcade Token Sorting** (0, 192) - Entertainment currency expertise
- **Transit Card Inspection** (64, 192) - Travel document examination
- **Queue-Skip Chip Sales** (128, 192) - Tap Dat Vault midnight access
- **Specialty Negotiation** (192, 192) - Non-traditional currency deals
- **Token Counting** (256, 192) - Verifying quantities
- **Card Validation** (320, 192) - Transit pass authentication

### CryptoBro69's Ex (Couchsurf Trigger) - 64x96 each:
- **Screaming About Fees** (0, 288) - Slippage fee breakdown
- **Couchsurf Invitation** (64, 288) - "Better looking but dumber" pickup
- **Desperate Plea** (128, 288) - Need place to crash tonight
- **Morning Scene Gone** (192, 288) - Futon aftermath reference
- **NFT Minting Flashback** (256, 288) - 3:17 AM creation memory

### Signature Props & Details:
- **Multiple Calculators** (0, 384, 48x32) - Mrs. Rata obsession
- **UV Wand Tool** (48, 384, 24x48) - Purple verification light
- **Specialty Tokens** (72, 384, 32x32) - Various currency types
- **Burner Phone** (104, 384, 16x32) - CryptoBro69's Ex device

---

## 👤 Sprite Sheet 5: Atmospheric Background NPCs
**File:** `atmospheric_npcs_types.png`  
**Dimensions:** 512x256 pixels  
**Character Size:** 48x72 background scale
**Color Palette:** #708090 (fixers grey), #FFD700 (currency gold), #9400D3 (UV glow)

### Rate Sharks (Grey-Coated Fixers) - 48x72 each:
- **Nicotine Fingers Ledger** (0, 0) - Immaculate record keeping
- **Professional Manipulation** (48, 0) - Financial scheme planning
- **Banking Jargon Delivery** (96, 0) - Street credibility mixed

### Expat Flippers (Travel Specialists) - 48x72 each:
- **Travel Card Trading** (144, 0) - Document exchange
- **Concert Wristband Sales** (192, 0) - Event access reselling
- **Museum Ticket Grey Market** (240, 0) - Cultural venue passes

### Counterfeit Connoisseurs (UV Sommeliers) - 48x72 each:
- **UV Wand Sommelier Pose** (288, 0) - Authentication as high art
- **Bill Authentication Ritual** (336, 0) - Money verification expertise
- **Wine Tasting Terminology** (384, 0) - Applied to currency

### Influencer Resellers (Fake VIP) - 48x72 each:
- **Fake Wristband Display** (432, 0) - Always says WEDNESDAY
- **Social Media Pitch** (0, 72) - Influencer meets black market
- **Obvious Scam Disguise** (48, 72) - "Exclusive access" fraud

### Background Atmosphere Actions:
- **Whispered Haggling** (96, 72, 64x48) - Negotiation gestures
- **Cash Counter Usage** (160, 72, 48x48) - Money handling
- **Paperwork Shuffling** (208, 72, 56x48) - Bureaucratic activity
- **UV Testing in Background** (264, 72, 48x48) - Ambient authentication

### Crowd Density Variations:
- **Sparse Crowd** (0, 120, 256x64) - Low traffic period
- **Moderate Crowd** (256, 120, 256x64) - Standard business
- **Busy Underground** (0, 184, 512x72) - Peak economic activity

---

## 🌫️ Sprite Sheet 6: Underground Environmental Effects
**File:** `underground_environmental_effects.png`  
**Dimensions:** 512x256 pixels  
**Color Palette:** #708090 (smoke grey), #9400D3 (UV purple), #FFD700 (toner gold)

### Blue-Grey Smoke System:
- **Smoke Wisp 1** (0, 0, 48x48) - Mysterious underground atmosphere
- **Smoke Wisp 2** (48, 0, 48x48) - Variation for randomization
- **Smoke Wisp 3** (96, 0, 48x48) - Third density option
- **Atmospheric Haze** (144, 0, 96x48) - Background fog layer

### Photocopier Toner Dust:
- **Toner Particle 1** (0, 48, 16x16) - Office equipment operation
- **Toner Particle 2** (16, 48, 16x16) - Bureaucratic atmosphere
- **Toner Particle 3** (32, 48, 16x16) - Document processing evidence
- **Toner Cloud** (48, 48, 64x32) - Heavy copying session

### UV Light Shimmer System:
- **Purple Glow Effect 1** (0, 80, 64x64) - Money verification glow
- **Purple Glow Effect 2** (64, 80, 64x64) - Counterfeit detection pulse
- **Money Verification Shine** (128, 80, 48x48) - Authentic currency sparkle
- **UV Wand Beam** (176, 80, 32x64) - Active scanning light

### Underground Vault Atmosphere:
- **Cold Air Particles** (0, 144, 32x32) - Temperature differential visible
- **Stone Dust Drift** (32, 144, 32x32) - Ancient vault particulate
- **Musty Vapor** (64, 144, 48x32) - Old wine cellar moisture

### Transaction Visual Effects:
- **Cash Counter Spin** (112, 144, 64x48) - Money counting machine
- **Receipt Printing** (176, 144, 48x32) - Mismatched paperwork generation
- **Stamp Impact Effect** (224, 144, 32x32) - Official legitimization visual

### Particle Emission Rates:
- **Blue-Grey Smoke:** Continuous low density for atmosphere
- **Toner Dust:** Sporadic bursts during transactions
- **UV Shimmer:** Active during verification mini-games
- **Cold Air:** Constant subtle drift reinforcing underground feel

---

## 📐 Mobile Optimization Requirements

### Texture Compression by Platform:
- **iOS:** PVRTC 4BPP for UV purple effects, maintains glow
- **Android:** ETC2 with alpha for smoke transparency
- **Fallback:** PNG high quality for split-flap readability

### Sprite Atlasing Strategy:
- **Underground Complete Atlas:** Arches + counters + lighting (1920x1080)
- **Rate Board System Atlas:** Mechanical elements + indicators (512x256)
- **CRT Monitor Atlas:** All screens + data displays (512x384)
- **Main NPCs Atlas:** Mrs. Rata + UV Man + Token Goblin + CryptoBro69's Ex (512x512)
- **Background NPCs Atlas:** All atmospheric character types (512x256)
- **Environmental Effects Atlas:** Smoke + UV + particles (512x256)
- **Max Atlas Size:** 2048x2048 for mobile GPU compatibility

### LOD (Level of Detail) Scaling:
- **High-End Devices:** Full CRT effects, all particles, split-flap animation
- **Medium Devices:** Simplified CRT refresh, reduced particle density, basic flaps
- **Low-End Devices:** Static monitors, minimal smoke, no UV shimmer
- **Potato Mode:** Essential vendors and counters only, no atmospheric effects

### Performance Targets:
- **Target FPS:** 60 fps (underground enclosed space)
- **Max Draw Calls:** 16 per frame
- **Memory Footprint:** 40MB maximum for location

---

## ♿ Accessibility Sprite Requirements

### High Contrast Rate Board:
- **Enhanced Indicators** (0, 176, 256x80) - Green/red ticks emphasized
- **Currency Display Readable** (256, 176, 192x80) - Clear denomination visibility
- **Mini-Game Visual Cues** (448, 176, 64x80) - Timing assistance indicators

### Colorblind Accommodations:
- **Pattern-Based Ticks** (240, 0, 128x64) - Shapes not just colors for timing
- **Money Verification Textures** (368, 0, 144x64) - UV without purple dependency
- **Rate Change Symbols** (0, 64, 256x48) - Icons supplement color coding

### Visual Audio Cues:
- **Split-Flap Clack** (256, 64, 48x32) - Sound wave visualization
- **Cash Counter Whir** (304, 64, 48x32) - Machine operation indicator
- **UV Scan Beep** (352, 64, 32x32) - Verification complete visual

---

## 🎬 Animation Sequence Specifications

### Split-Flap Rate Board Updates:
- **Duration:** 3-5 second random intervals
- **Pattern:** Current rate → flap → new rate with clack
- **Mini-Game:** Green tick = interact, Red tick = wait
- **Purpose:** Economic timing skill challenge

### Mrs. Rata Calculator Obsession:
- **Duration:** 4-frame cycle, 2 seconds total
- **Pattern:** Calculator 1 → Calculator 2 → Calculator 3 → Cross-reference
- **Continuous:** Never stops checking rates
- **Purpose:** Obsessive professional characterization

### The UV Man Scanning Sequence:
- **Duration:** 2-second authentication procedure
- **Pattern:** Position money → activate wand → purple glow → verdict
- **Mini-Game:** Quick reaction timing for verification
- **Purpose:** Counterfeit detection gameplay mechanic

### CRT Monitor Market Data:
- **Duration:** Continuous scrolling and updates
- **Pattern:** Kebab prices → meme coins → cover charges → cycle
- **Flicker:** Authentic CRT refresh every 2-3 seconds
- **Purpose:** Living underground economy atmosphere

### Token Goblin Sorting:
- **Duration:** 3-frame loop, 1.5 seconds
- **Pattern:** Examine token → sort into tray → next token
- **Specialty:** Different animation for each currency type
- **Purpose:** Non-traditional currency expertise

### CryptoBro69's Ex Breakdown:
- **Trigger:** Player approaches main counter
- **Duration:** 5-second couchsurf encounter setup
- **Pattern:** Screaming → recognition → invitation
- **Purpose:** Couchsurf quest trigger with NFT consequences

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility
- Coordinate system: Top-left origin (0,0)
- Animation system: Frame-based with JSON timing
- Mini-games: Input detection for rate board timing
- Particle systems: CPUParticles2D for smoke and UV effects

### Audio Sync Points:
- Split-flap clacking syncs with board updates
- Mrs. Rata calculator buttons match animation frames
- UV wand emits verification beep at purple glow peak
- Cash counter whirring during transaction sequences
- CRT monitors have authentic electrical hum

### Quest Integration:
- **NFT Hunt:** Shadow Ledger inspection reveals VIP Wristband PNG
- **Couchsurf System:** CryptoBro69's Ex full morning scene with NFT reward
- **Boss Unlock:** Count Velvet Absinthe defeat opens Premium Stock gate
- **Tool Distribution:** UV Wand enables counterfeit detection elsewhere

### Cross-Location Dependencies:
- **Economic Hub:** Central currency exchange for all Debaucheryville
- **Tool Network:** UV Wand used in other vendor locations
- **Queue-Skip System:** Tap Dat Vault chips from Token Goblin
- **Boss Integration:** Premium Stock requires main story progression

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Old-world bank vault meets post-Soviet flea market"
- **Color Mood:** Stone grey dominance, UV purple accents, vault black shadows
- **Lighting:** Focused desk lamp, CRT glow, UV shimmer, tealight flicker
- **Texture:** Worn stone surfaces, scratched glass, official-looking paperwork

### Character Design Philosophy:
- **Mrs. Rata:** Professional detachment, treats illegal as mundane
- **UV Man:** Counterfeit connoisseur, authentication as art form
- **Token Goblin:** Specialty currency expertise, non-traditional dealer
- **CryptoBro69's Ex:** Desperate crypto crash victim, couchsurf trigger

### Mini-Game Design:
- Split-flap timing requires player skill and attention
- Green/red tick system creates risk/reward decisions
- UV verification adds interactive authentication gameplay
- Stat influence (Street Rep/Charm) provides RPG integration

### Environmental Storytelling:
- Vaulted arches suggest historical wine cellar repurposed
- Mismatched paperwork shows grey market operations
- Multiple currency types reveal underground economy scope
- CRT monitors display absurd market data (kebabs, meme coins)

---

## 📋 Required PNG Files (6 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | shadow_exchange_underground_complete.png | 1920x1080 |
| 2 | split_flap_rate_board_system.png | 512x256 |
| 3 | crt_monitor_wall_markets.png | 512x384 |
| 4 | shadow_exchange_npcs.png | 512x512 |
| 5 | atmospheric_npcs_types.png | 512x256 |
| 6 | underground_environmental_effects.png | 512x256 |

**Total Estimated Memory:** ~11.7 MB uncompressed RGBA (within the 40MB location footprint)

---

## 📦 File Delivery Checklist

### Required PNG Files (6 Total):
- [ ] `shadow_exchange_underground_complete.png` (1920x1080)
- [ ] `split_flap_rate_board_system.png` (512x256)
- [ ] `crt_monitor_wall_markets.png` (512x384)
- [ ] `shadow_exchange_npcs.png` (512x512)
- [ ] `atmospheric_npcs_types.png` (512x256)
- [ ] `underground_environmental_effects.png` (512x256)

### Quality Requirements:
- **Format:** PNG-24 with alpha channel
- **Color Space:** sRGB
- **DPI:** 72 (screen resolution)
- **Compression:** Lossless PNG
- **Naming Convention:** snake_case, all lowercase
- **Layer Organization:** Preserve for rate board updates

### Delivery Format:
- **Primary:** Individual PNG files per specifications
- **Backup:** Master PSD/Photoshop with organized layers
- **Documentation:** Mini-game timing sheet, animation sequences

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Split-Flap Rate Board** - Mechanical mini-game aesthetic
2. **Mrs. Rata Calculator Obsession** - Multiple calculators comedy
3. **UV Money Verification** - Purple glow counterfeit detection
4. **CRT Meme Coin Charts** - Absurd market data displays
5. **CryptoBro69's Ex Breakdown** - Couchsurf encounter setup

### TikTok Potential:
- "Underground currency exchange mini-game timing"
- "Getting the best rates in the Shadow Exchange"
- "When the clerk has too many calculators"
- "POV: You trusted the obviously sketchy bazaar"

### Twitter/X Quote Potential:
- "Cash speaks. Whining does not."
- "Exchange rate? Depends how loudly you asked."
- "NFTs are just zoo animals with bank accounts, darling."

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All 6 PNG files match exact dimensions
- [ ] Split-flap board shows clear green/red tick timing
- [ ] Mrs. Rata calculator obsession is obvious (4 calculators)
- [ ] UV wand creates purple verification glow
- [ ] CRT monitors display absurd market data clearly
- [ ] CryptoBro69's Ex breakdown is visually clear
- [ ] Underground vault atmosphere feels authentic
- [ ] All currency types visible in trays
- [ ] Color palette matches hex codes
- [ ] Accessibility alternatives included
- [ ] File naming follows convention
- [ ] Master files preserved for updates

### Quality Checkpoints:
- [ ] Split-flap mini-game timing is intuitive
- [ ] NPCs convey "officially unofficial" operations
- [ ] Environmental effects support underground mood
- [ ] Premium Stock gate is discoverable post-boss
- [ ] Couchsurf trigger is clear and compelling
- [ ] Mobile performance optimized for particles
- [ ] All elements support financial satire theme
- [ ] Social media viral potential maximized

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Debaucheryville — Old Town sub-basement only |
| Cultural Specificity | ✅ | Post-communist grey-market economy adapted for Western tourist currency confusion |
| Satirical Targets Appropriate | ✅ | Exploitative currency practices and financially desperate tourists — not legitimate local commerce |
| Seedy Underbelly Present | ✅ | Black-market bazaar, counterfeit trading, notoriety/"verification fee" racket |
| Gameplay Value Established | ✅ | Split-flap timing mini-game, UV scan checks, barter window, shady contracts, boss-gated Premium Stock |
| Technical Feasibility | ✅ | 6 sprite atlases, LOD tiers down to Potato Mode, CPUParticles2D smoke/UV effects |
| Mobile Performance Budget | ✅ | 60 FPS target, max 16 draw calls, 40MB memory footprint |
| Accessibility Features | ✅ | Visual audio cues (split-flap clack, cash counter whir, UV beep), pattern-based ticks for colorblind timing |
| No Crypto Elements | ✅ | Crypto parody established in source material (meme-coin monitors, CryptoBro69's Ex NFT storyline) |
| Social Media Integration | ✅ | Split-flap aesthetic, calculator obsession comedy, quotable NPC dialogue identified |

**Once validated, the Shadow Exchange becomes the essential underground economic hub where players navigate split-flap timing mini-games, encounter Mrs. Rata's calculator obsession, trigger CryptoBro69's Ex couchsurf disaster, and unlock Premium Stock after defeating Count Velvet Absinthe!**