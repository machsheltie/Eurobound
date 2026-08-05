# Shamsterdam Bike Rental - Complete PNG Asset Requirements

*Artist Reference Document for the Tourist Cycling Disaster Headquarters*

**Location ID**: `shamsterdam_bike_rental_01`  
**Priority**: MEDIUM (Service Shop, Bike Crossing Alternative, Recurring Interactions)  
**Total Sheets Required**: 8  
**Performance Optimization**: Standard (60 FPS, dialogue-heavy)

---

## 📋 Overview
Shamsterdam Bike Rental ("Fiets Verhuur" — the sign everyone ignores) is the official source of the distinctive orange tourist bikes, run by three generations of the van der Berg family who have made a fortune from deposit forfeitures and damage claims. This document specifies every PNG asset for the shop: tileset, orange bike fleet, three family NPCs, the wall displays that document decades of tourist failure, the repair station, and the rental/return effects and UI. Its satirical essence in a sentence: the shop sells the illusion of "cycling like a local," and everyone behind the counter knows exactly how that story ends.

**Location ID:** `shamsterdam_bike_rental_01`
**Theme:** Tourist bike rental culture and the "Amsterdam bike experience" marketing myth; insurance industry satire
**Zone:** Adjacent to Central Bike Crossing (South Side)
**Hours:** 08:00-21:00 (closed overnight; "tourists shouldn't cycle in the dark")
**Primary Function:** Service shop / recurring interaction hub — bike rental bypasses the Bike Crossing mini-game; tiered rentals, insurance packages, repairs, damage assessment scenes, and quest source ("Tour de Shame", "Canal Recovery", "The Insurance Claim")

---

## 🎨 Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Rental Orange | #FF6600 | Bikes, uniforms, primary branding |
| Warning Yellow | #FFD700 | Caution elements, insurance highlights |
| Canal Blue | #003DA5 | Water references, accent |
| Shop White | #F5F5F5 | Walls, forms, clean surfaces |
| Grease Grey | #4A4A4A | Repair station, used equipment |
| Damage Red | #CC0000 | Warning indicators, major damage |
| Receipt Cream | #FFF8DC | Paper, forms, posters |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/bike_rental/
├── environment/
│   ├── bike_rental_shop_tileset.png
│   ├── bike_rental_displays.png
│   └── repair_station_sprites.png
├── npcs/
│   ├── npc_dirk_rental_owner.png
│   ├── npc_anneke_counter.png
│   └── npc_opa_cees_repair.png
├── objects/
│   └── rental_bike_fleet.png
└── effects/
    └── bike_rental_effects.png
```

---

## 🏪 Sprite Sheet 1: Shop Tileset
**Filename**: `bike_rental_shop_tileset.png`  
**Dimensions**: 512 × 512 pixels  
**Tile Size**: 32 × 32 pixels

### Walls (Row 0)
- **Shop Wall White**: Clean commercial wall
- **Shop Wall Orange Stripe**: Brand stripe at eye level
- **Window Frame**: Large front window frame
- **Doorway Frame**: Interior doorway to repair station
- **Poster Backing**: Cork/board background for displays

### Floor (Row 1)
- **Shop Floor Tile**: Commercial floor tiles
- **Shop Floor Worn**: Traffic-worn variant
- **Repair Floor Concrete**: Workshop concrete floor
- **Floor Mat Entrance**: "Fiets Verhuur" branded mat

### Counter Elements (Row 2)
- **Service Counter Front**: Main counter facing (3 tiles wide)
- **Service Counter Top**: Counter surface from above (2 tiles)
- **Cash Register**: Classic register
- **Form Stack**: Pile of rental forms/waivers
- **Credit Card Machine**: Modern payment terminal

### Display Frames (Row 3)
- **Photo Frame Damage**: For damage gallery photos
- **Photo Frame Memorial**: For canal memorial polaroids
- **Insurance Chart Frame**: Large frame for comparison chart
- **Tally Board**: Chalkboard style frame
- **Poster Cycling Rules**: Framed poster

### Equipment (Row 4)
- **Helmet Display**: Row of helmets on pegs
- **Accessories Shelf**: Add-ons display
- **Repair Tools**: Tool wall silhouette
- **Bike Parts Shelf**: Organized parts storage
- **Workbench Surface**: Work area surface

---

## 🚲 Sprite Sheet 2: Bike Fleet
**Filename**: `rental_bike_fleet.png`  
**Dimensions**: 512 × 256 pixels

### Rental Bikes

**Standard Orange Rental Bike** (48×48, 4 variants)
- Classic Dutch-style city bike
- Bright orange frame
- Front basket with "RENTAL" sticker
- Lock attached to rear wheel
- Variants: Slightly different basket positions, handlebar angles

**Bike Stand Row** (256×32)
- 8 bikes in a row on stands
- Shows the fleet scale
- Visible through shop window

**Damaged Bike Variants** (48×48 each)
- **Bent Wheel**: Wheel clearly not round
- **Missing Basket**: Basket torn off
- **Twisted Frame**: Impact damage visible
- **Canal Recovered**: Rust, seaweed, water stains

*Art Note*: The orange should be VERY orange. These bikes are designed to be identifiable from a distance as "tourist target."

---

## 🔧 Sprite Sheet 3: Dirk van der Berg (Owner)
**Filename**: `npc_dirk_rental_owner.png`  
**Dimensions**: 288 × 320 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Age**: Mid-50s
- **Build**: Stocky, bike mechanic muscles
- **Uniform**: Orange polo shirt, stretched slightly
- **Hands**: Grease permanently embedded
- **Expression**: Seen every tourist disaster imaginable
- **Name Tag**: "Dirk - 22 Years - 847 Canal Recoveries"

### Animation States (5 rows)
- **Row 0: Idle at Counter** (2 frames) - Standing, slight shift
- **Row 1: Checking Paperwork** (3 frames) - Looking at forms
- **Row 2: Pointing at Crossing** (2 frames) - Warning gesture
- **Row 3: I Told You So** (2 frames) - The signature expression
- **Row 4: Genuine Surprise** (3 frames) - RARE, for undamaged returns

*Art Note*: Dirk's "I told you so" expression should be immediately recognizable. It's his most-used animation.

---

## 📋 Sprite Sheet 4: Anneke van der Berg (Daughter)
**Filename**: `npc_anneke_counter.png`  
**Dimensions**: 240 × 256 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Age**: Early 20s
- **Build**: Average
- **Uniform**: Orange polo shirt, fitted
- **Props**: Clipboard always in hand, pen ready
- **Expression**: Inherited family resignation, hint of amusement
- **Name Tag**: "Anneke - 3 Years - Learning the Business"

### Animation States (4 rows)
- **Row 0: Idle with Clipboard** (2 frames) - Standing ready
- **Row 1: Taking Photo** (3 frames) - Camera to face, flash
- **Row 2: Writing on Form** (3 frames) - Documenting damage
- **Row 3: Skeptical Expression** (2 frames) - Doubt about your story

*Art Note*: Anneke should look like she's seen through every tourist excuse but finds it mildly entertaining.

---

## 👴 Sprite Sheet 5: Opa Cees (Grandfather)
**Filename**: `npc_opa_cees_repair.png`  
**Dimensions**: 240 × 320 pixels  
**Sprite Size**: 48 × 64 pixels

### Character Design
- **Age**: 80+
- **Build**: Wiry, still active
- **Clothing**: Oil-stained apron older than most customers
- **Setting**: Surrounded by decades of bike debris
- **Expression**: Philosophical about bike mortality

### Animation States (5 rows)
- **Row 0: Repairing Bike** (4 frames) - Active work on bike
- **Row 1: Examining Damage** (3 frames) - Assessing the worst
- **Row 2: Looking at Canal Wall** (2 frames) - Contemplating history
- **Row 3: Sighing at Damage** (2 frames) - The deep, weary sigh
- **Row 4: Giving Blessing** (3 frames) - Hands raised, bestowing navigation luck

*Art Note*: Opa Cees should look like he contains 47 years of accumulated wisdom and weariness.

---

## 🖼️ Sprite Sheet 6: Wall Displays
**Filename**: `bike_rental_displays.png`  
**Dimensions**: 512 × 384 pixels

### Display Elements

**Damage Photo Gallery** (192×128)
- Grid of 6 photos showing damaged bikes
- Each with a caption plaque below
- Examples:
  - Bike folded in half: "Tram tracks. Classic."
  - Bike with seaweed: "Canal. Third time for this one."
  - Missing front wheel: "We never found it."
- Visible horror show aesthetic

**Insurance Comparison Chart** (128×128)
- Four tiers in columns
- Color-coded: Green → Yellow → Orange → Red
- Escalating warning icons
- "Covers" and "Does NOT Cover" sections
- Platinum tier has gold border

**Canal Memorial Board** (128×128)
- Corkboard with polaroids
- Each polaroid shows a lost bike
- RIP-style captions
- "Your bike could be next" footer
- Solemn but slightly dark humor

**Nationality Tally Board** (128×96)
- Chalkboard style
- Country flags with percentages
- Rankings of damage rates
- Handwritten style numbers
- Anneke's personal project

**Cycling Rules Poster** (96×128)
- "How to Cycle in Shamsterdam"
- 5 numbered rules
- Small bike icons
- "Nobody reads this" energy
- Professional but ignored

**Helmet Wall Display** (128×64)
- Row of helmets on pegs
- Various sizes
- "Locals don't wear them" sign
- Dusty appearance (rarely taken)

---

## 🛠️ Sprite Sheet 7: Repair Station Elements
**Filename**: `repair_station_sprites.png`  
**Dimensions**: 384 × 256 pixels

### Workshop Elements

**Canal Recovery Wall** (192×128)
- Wall covered in recovered bikes
- Some with visible seaweed/rust
- Before/after comparison area
- Decades of accumulation visible
- Opa Cees's trophy wall

**Workbench** (128×64)
- Tools organized (wrenches, pliers)
- Oil cans, chain lubricant
- Current project bike
- Overhead lamp
- Parts in progress

**Vintage Bikes Corner** (128×96)
- Old BLUE rental bikes
- "Before orange became the tourist warning color"
- Visible age and nostalgia
- Museum-quality positioning
- Placards with dates

**Parts Shelves** (128×64)
- Wheels, chains, handlebars
- Organized chaos
- Label system (Dutch)
- Spare baskets stack
- Lock collection

---

## ✨ Sprite Sheet 8: Effects and UI
**Filename**: `bike_rental_effects.png`  
**Dimensions**: 256 × 128 pixels

### Effects

**Camera Flash** (64×64, 3 frames)
- Bright white flash
- Anneke's photo moment
- Quick burst effect

**Form Stamp** (32×32, 2 frames)
- Red "APPROVED" or "DENIED" stamp
- Satisfying thunk visual

**Cash Register Ching** (48×32, 3 frames)
- Register drawer opening
- Money/receipt visual
- Comedy timing for upsells

**Damage Reveal** (64×64, 4 frames)
- Dramatic reveal effect
- Red glow for major damage
- Used during assessment

### UI Elements

**Rental Tier Icons** (48×48 each)
- Basic: Simple bike silhouette
- Premium: Bike with sparkle
- Survivor: Bike with shield

**Insurance Tier Icons** (32×32 each)
- Basic: Small shield outline
- Standard: Half-filled shield
- Premium: Full shield
- Platinum: Gold shield with star

**Damage Level Indicators** (24×24 each)
- None: Green checkmark
- Minor: Yellow warning
- Major: Orange alert
- Canal: Blue water drop

**Deposit Bar** (150×20)
- 150 Sovs deposit tracker
- Depletes with damage
- Green → Yellow → Red

---

## 🎬 Animation Specifications

*Sprite positions within sheets follow the row layouts specified per sheet above; pixel coordinates set at sheet layout.*

### NPC Idle Loops (Sheets 3-5):
- **Duration:** 2-4 seconds per cycle (0.25-0.5 FPS, subtle movement)
- **Frames:** 2 per idle row (Dirk at counter, Anneke with clipboard, Opa Cees repairing at 4 frames)
- **Pattern:** Frame 1 → 2 → 1 → loop
- **Trigger:** Constant while shop scene active
- **Purpose:** Lived-in family business atmosphere
- **Audio Sync:** Ambient — bell tests, tire pump, wrench on metal
- **Performance Optimization:** None needed (dialogue-heavy, low animation load)

### NPC Interaction States (Sheets 3-5):
- **Duration:** 0.5-1 second per state (1-2 FPS when interacting)
- **Frames:** 2-3 per state row (Checking Paperwork, Pointing at Crossing, I Told You So, Genuine Surprise, Taking Photo, Writing on Form, Skeptical Expression, Examining Damage, Sighing, Giving Blessing)
- **Pattern:** Play once → return to idle
- **Trigger:** Dialogue beats — rental sequence, damage assessment, insurance upsell, blessing reward
- **Purpose:** NPC reactions ARE the comedy; Dirk's "I Told You So" is his most-used animation
- **Audio Sync:** Opa Cees sigh audio on Sighing row; triumphant fanfare with Genuine Surprise (undamaged return, rare)
- **Performance Optimization:** None needed

### Camera Flash (Sheet 8):
- **Duration:** 0.375 seconds (8 FPS, quick burst)
- **Frames:** 3
- **Pattern:** Frame 1 → 3, no loop
- **Trigger:** Anneke's "photo for the file" moment (first visit and damage assessments)
- **Purpose:** Punchline timing for the family betting pool gag
- **Audio Sync:** Camera shutter on frame 1
- **Performance Optimization:** None needed

### Form Stamp (Sheet 8):
- **Duration:** 0.5 seconds (4 FPS, satisfying timing)
- **Frames:** 2
- **Pattern:** Raise → thunk, no loop
- **Trigger:** Claim approved/denied; rental paperwork complete
- **Purpose:** Bureaucratic finality feedback
- **Audio Sync:** Stamp thunk on frame 2
- **Performance Optimization:** None needed

### Cash Register Ching (Sheet 8):
- **Duration:** ~0.75 seconds (4 FPS)
- **Frames:** 3
- **Pattern:** Drawer opens → receipt, no loop
- **Trigger:** Payment, deposit hold, insurance upsell
- **Purpose:** Comedy timing for upsells
- **Audio Sync:** "Cha-ching" on frame 1
- **Performance Optimization:** None needed

### Damage Reveal (Sheet 8):
- **Duration:** 1 second (4 FPS, dramatic pacing)
- **Frames:** 4
- **Pattern:** Build → red glow hold on final frame
- **Trigger:** Damage assessment scene on bike return
- **Purpose:** Dramatic reveal of what the tourist did
- **Audio Sync:** Record scratch / dramatic sting on frame 1
- **Performance Optimization:** None needed

### Animation Frame Rates

| Element | FPS | Notes |
|---------|-----|-------|
| NPC idle | 0.25-0.5 | Subtle movement |
| NPC active | 1-2 | When interacting |
| Camera flash | 8 | Quick burst |
| Form stamp | 4 | Satisfying timing |
| Damage reveal | 4 | Dramatic pacing |

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter/register outline | set at sheet layout | 32×32 tiles | High-contrast outline for primary interaction point |
| Rental/insurance tier icons (high contrast) | set at sheet layout | 48×48 / 32×32 | Bold-outline versions of tier icons for menu legibility |
| NPC interaction highlight | set at sheet layout | 48×64 | Outline variant marking talkable NPCs (Dirk, Anneke, Opa Cees) |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static camera flash | set at sheet layout | 64×64 | Single-frame soft glow replacing the bright 3-frame flash burst |
| Static damage reveal | set at sheet layout | 64×64 | Non-pulsing steady red outline variant |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Camera Flash | Sheet 8 | 64×64 | Visual for camera shutter audio |
| Form Stamp | Sheet 8 | 32×32 | Visual for stamp thunk audio |
| Cash Register Ching | Sheet 8 | 48×32 | Visual for "cha-ching" upsell audio |
| Sigh indicator | set at sheet layout | 24×24 | Small breath-puff sprite mirroring Opa Cees's audible sigh |

### Colorblind Considerations:
- Insurance Comparison Chart tiers (Green → Yellow → Orange → Red) doubled with escalating warning icon count, not color alone
- Damage Level Indicators pair color with distinct shapes (checkmark / warning triangle / alert / water drop)
- Deposit Bar (Green → Yellow → Red) includes numeric `N SOVS` readout (word lettered, no currency mark)
- Touch zones minimum 44px for all menu and dialogue interactions

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import); wall displays need higher quality (readable in-fiction text)
- **Fallback:** PNG high quality for displays sheet and UI icons (text/detail-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| bike_rental_environment | shop tileset, wall displays, repair station | 1024x1024 |
| bike_rental_characters | Dirk, Anneke, Opa Cees sheets | 1024x1024 |
| bike_rental_effects | effects, UI, bike fleet | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | All NPC animations, all effects, full display detail |
| Medium | Reduced effect frames, displays at standard detail |
| Low | Static NPCs outside dialogue, minimal effects, pre-rendered fleet only |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** Under 30
- **Memory Footprint:** Under 35 MB
- **Particle Limit:** 20 (minimal)

### Performance Notes:
- Dialogue-heavy location (low animation load) — menu-based interactions
- Bike fleet pre-rendered as Bike Stand Row (not individual bike instances)
- Simple shop geometry, single interior scene plus repair station doorway view

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: TileMap (shop tileset), AnimatedSprite2D (NPCs, effects), Control/CanvasLayer (rental and insurance menus, deposit bar)
- Special systems: recurring interaction state machine (first visit → return visit → subsequent rentals with player "file" tracking), damage event resolution on return, deposit tracker bound to Deposit Bar UI, loyalty discount/surcharge flags

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Camera Flash | Camera shutter | Frame 1 of flash |
| Form Stamp | Stamp thunk | Frame 2 (impact) |
| Cash Register Ching | "Cha-ching" | Drawer-open frame |
| Damage Reveal | Record scratch / dramatic sting | Frame 1 of reveal |
| Opa Cees Sighing row | Audible sigh | Row start |
| Dirk Genuine Surprise | Triumphant fanfare (rare) | Undamaged return resolution |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Keg Cycle | Bike fleet, rental UI | Requires bike rental for delivery timer challenge |
| Tour de Shame | Fleet, tier icons, Dirk states | Given by Dirk after second rental; undamaged circuit under 20 minutes |
| Canal Recovery Assistant | Opa Cees sheet, Canal Recovery Wall | Opa Cees quest giver; recovered bikes added to wall |
| The Insurance Claim | Form Stamp, Anneke Skeptical row, Damage Reveal | Interactive bureaucracy micro-quest on claim filing |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Central Bike Crossing | Orange rental bikes (shared design with crossing kiosk/cyclist sheets) | Adjacent south side; rental bypasses the mini-game |
| Canal Ring Promenade | Canal Recovered bike variants, recovery wall | Canal recovery quest site |
| All Shamsterdam districts | Orange rental bike (player-mounted) | Faster district travel while rental active |
| Voetgangerstunnel | — | Alternative (underground) to renting |

### Cross-Reference: Related Assets
- **Connects to**: Bike Crossing assets (adjacent location), Canal Ring assets (recovery quest), all Shamsterdam district assets (bike access)
- **Unique to this location**: Dirk, Anneke, Opa Cees NPCs; orange rental bike fleet; wall displays (damage, insurance, memorial); repair station elements; rental/return UI

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A working bike rental shop — practical Dutch efficiency meets tourist-focused commerce"
- **Color Mood:** Orange dominates everything as the "tourist warning color"; clean shop white against grease grey workshop tones
- **Lighting:** See Lighting Requirements below — harsh commercial fluorescents up front, warmer workshop atmosphere in back
- **Texture:** Clean but well-used; organized but with visible history of countless rental disasters

### Visual Identity
This is a **working bike rental shop**—practical Dutch efficiency meets tourist-focused commerce. Orange dominates everything as the "tourist warning color." The shop is clean but well-used, organized but with visible history of countless rental disasters.

### Key Visual Themes
- **Dutch Orange Branding**: Everything orange—bikes, polos, signage, warning highlights
- **Working Service Shop**: Forms, counters, equipment, practical organization
- **History on Display**: Damage photos, memorial board, canal recovery wall
- **Family Business**: Three generations visible in the space

### Lighting Requirements

**Main Shop**
- Commercial fluorescent lighting
- Bright, professional, slightly harsh
- Window natural light influence

**Repair Station**
- Workshop lighting
- Warmer tone
- Work lamp accent on bench
- More atmospheric

### Environmental Storytelling:
- The damage photo gallery, canal memorial board, and nationality tally tell decades of tourist failure without a word of dialogue
- Vintage blue bikes in the corner — "before orange became the tourist warning color"
- Dusty helmet wall ("Locals don't wear them") and the ignored cycling rules poster

### Character Integration Notes:
- Three generations staged in depth: Anneke at counter (front), Dirk mid-shop, Opa Cees visible through the repair station doorway (background)
- Name tags carry lore ("Dirk - 22 Years - 847 Canal Recoveries")
- NPC reaction states are the shop's core feedback loop for rental outcomes

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Damage Photo Gallery** - Wall of tourist failures
2. **Dirk's Genuine Surprise** - Rare undamaged return
3. **Nationality Tally** - Who crashes most?
4. **Canal Memorial Board** - RIP bikes
5. **Orange Army Fleet** - 50+ identical bikes

### Quote Potential:
- "The platinum covers your dignity. None of them cover your decision-making."
- "American? British? ...Australian. Okay, let me get the reinforced form."
- "This bike came out of the canal. This one too. And this one..."
- "You're back. The bike is not."
- "No damage? I don't believe you, but I respect the lie."

### TikTok Potential
- Insurance tier explanation speedrun
- Dirk reaction compilation
- "Will I damage it?" challenge
- Opa Cees's wisdom moments

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | bike_rental_shop_tileset.png | 512x512 |
| 2 | rental_bike_fleet.png | 512x256 |
| 3 | npc_dirk_rental_owner.png | 288x320 |
| 4 | npc_anneke_counter.png | 240x256 |
| 5 | npc_opa_cees_repair.png | 240x320 |
| 6 | bike_rental_displays.png | 512x384 |
| 7 | repair_station_sprites.png | 384x256 |
| 8 | bike_rental_effects.png | 256x128 |

**Total Estimated Memory:** ~35 MB maximum (location performance budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `bike_rental_shop_tileset.png` (512x512)
- [ ] `rental_bike_fleet.png` (512x256)
- [ ] `npc_dirk_rental_owner.png` (288x320)
- [ ] `npc_anneke_counter.png` (240x256)
- [ ] `npc_opa_cees_repair.png` (240x320)
- [ ] `bike_rental_displays.png` (512x384)
- [ ] `repair_station_sprites.png` (384x256)
- [ ] `bike_rental_effects.png` (256x128)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha channel |
| Color Space | sRGB |
| DPI | 72 (screen resolution) |
| Compression | Lossless PNG |
| Naming Convention | snake_case, all lowercase |
| Layer Organization | Preserve layers in master file |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/layered file with organized layer groups
- **Documentation:** Animation timing reference sheet

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Rental orange is VERY orange — bikes identifiable at distance as "tourist target"; Dirk's "I Told You So" reads instantly; wall display gags legible
- [ ] Accessibility visual alternatives included for all audio cues (flash, stamp, register, sigh)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (tourist optimism vs. rental reality, insurance satire)
- [ ] Hidden areas/interactions have discoverable visual cues (repair station doorway, vintage blue bikes, tally board)
- [ ] Performance optimized (pre-rendered fleet, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (insurance tiers, damage levels, deposit bar)
- [ ] Social media viral potential maximized in composition choices (damage gallery, memorial board framing)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam only; Dutch naming ("Fiets Verhuur") in-world |
| Cultural Specificity | ✅ | Dutch cycling culture, family bike shop, canal bike graveyard lore |
| Satirical Targets Appropriate | ✅ | Tourist cycling optimism and insurance upselling — gentle mockery, not locals |
| Seedy Underbelly Present | ✅ | Deposit forfeiture economy, damage-claim profiteering, betting pool on renters |
| Gameplay Value Established | ✅ | Crossing bypass, tiered rentals/insurance, recurring visits, 3 quests |
| Technical Feasibility | ✅ | Pre-rendered fleet, menu-based interactions, simple geometry |
| Performance Budget | ✅ | 60 FPS, <30 draw calls, <35 MB, 20 particles |
| Accessibility Features | ✅ | Visual audio cues, shape-coded tiers, 44px touch zones |
| No Crypto Elements | ✅ | All transactions in Sovs (credit card holds, 5% cash discount) |
| Social Media Integration | ✅ | 5 screenshot moments + TikTok formats identified |

---

**END OF ASSET REQUIREMENTS**

*Shamsterdam Bike Rental: Where every tourist believes they'll "cycle like a local," and where Dirk, Anneke, and Opa Cees have been waiting for them. The orange bikes are ready. The damage forms are printed. The canal is patient.*
