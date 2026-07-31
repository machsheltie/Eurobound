# Shamsterdam Bike Rental - Complete PNG Asset Requirements

*Artist Reference Document for the Tourist Cycling Disaster Headquarters*

**Location ID**: `shamsterdam_bike_rental_01`  
**Priority**: MEDIUM (Service Shop, Bike Crossing Alternative, Recurring Interactions)  
**Total Sheets Required**: 8  
**Mobile Optimization**: Standard (60 FPS, dialogue-heavy)

---

## Art Direction Summary

### Visual Identity
This is a **working bike rental shop**—practical Dutch efficiency meets tourist-focused commerce. Orange dominates everything as the "tourist warning color." The shop is clean but well-used, organized but with visible history of countless rental disasters.

### Key Visual Themes
- **Dutch Orange Branding**: Everything orange—bikes, polos, signage, warning highlights
- **Working Service Shop**: Forms, counters, equipment, practical organization
- **History on Display**: Damage photos, memorial board, canal recovery wall
- **Family Business**: Three generations visible in the space

### Color Palette

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

## SHEET 1: Shop Tileset
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

## SHEET 2: Bike Fleet
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

## SHEET 3: Dirk van der Berg (Owner)
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

## SHEET 4: Anneke van der Berg (Daughter)
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

## SHEET 5: Opa Willem (Grandfather)
**Filename**: `npc_opa_willem_repair.png`  
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

*Art Note*: Opa Willem should look like he contains 47 years of accumulated wisdom and weariness.

---

## SHEET 6: Wall Displays
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

## SHEET 7: Repair Station Elements
**Filename**: `repair_station_sprites.png`  
**Dimensions**: 384 × 256 pixels

### Workshop Elements

**Canal Recovery Wall** (192×128)
- Wall covered in recovered bikes
- Some with visible seaweed/rust
- Before/after comparison area
- Decades of accumulation visible
- Opa Willem's trophy wall

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

## SHEET 8: Effects and UI
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
- €150 deposit tracker
- Depletes with damage
- Green → Yellow → Red

---

## Lighting Requirements

### Main Shop
- Commercial fluorescent lighting
- Bright, professional, slightly harsh
- Window natural light influence

### Repair Station
- Workshop lighting
- Warmer tone
- Work lamp accent on bench
- More atmospheric

---

## Animation Frame Rates

| Element | FPS | Notes |
|---------|-----|-------|
| NPC idle | 0.25-0.5 | Subtle movement |
| NPC active | 1-2 | When interacting |
| Camera flash | 8 | Quick burst |
| Form stamp | 4 | Satisfying timing |
| Damage reveal | 4 | Dramatic pacing |

---

## Social Media Viral Moments

### Screenshot Opportunities
1. **Damage Photo Gallery**: Wall of tourist failures
2. **Dirk's Genuine Surprise**: Rare undamaged return
3. **Nationality Tally**: Who crashes most?
4. **Canal Memorial Board**: RIP bikes
5. **Orange Army Fleet**: 50+ identical bikes

### TikTok Potential
- Insurance tier explanation speedrun
- Dirk reaction compilation
- "Will I damage it?" challenge
- Opa Willem's wisdom moments

---

## Technical Specifications

### File Format
- **Format**: PNG-24 with alpha transparency
- **Color Space**: sRGB
- **Resolution**: 72 DPI
- **Compression**: Lossless

### Mobile Optimization
- Dialogue-heavy (low animation load)
- Pre-rendered bike fleet (not individual)
- Menu-based interactions
- Simple shop geometry
- 60 FPS target
- <35MB memory budget
- <30 draw calls

---

## Cross-Reference: Related Assets

### Connects To
- Bike Crossing assets (adjacent location)
- Canal Ring assets (recovery quest)
- All Shamsterdam district assets (bike access)

### Unique to This Location
- Dirk, Anneke, Opa Willem NPCs
- Orange rental bike fleet
- Wall displays (damage, insurance, memorial)
- Repair station elements
- Rental/return UI

---

**END OF ASSET REQUIREMENTS**

*Shamsterdam Bike Rental: Where every tourist believes they'll "cycle like a local," and where Dirk, Anneke, and Opa Willem have been waiting for them. The orange bikes are ready. The damage forms are printed. The canal is patient.*
