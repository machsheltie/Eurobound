# Torte Royale

*A mobile cake cart where the chocolate is dark, the prices are darker, and the vendor will absolutely judge your pronunciation of "Sachertorte"*

## Location Identity
- **Location ID**: sinfonia_kaffeehausrow_torte_royale_01
- **Display Name**: Torte Royale
- **Satirical Subtitle**: "Authentic™ Since We Said So"
- **World Location**: Sinfonia
- **Area Zone**: Kaffeehaus Row, Intellectual Café District (mobile — rotates positions)
- **Location Type**: Street Vendor / Premium Food Cart / Mobile Shop / Cultural Gatekeeping Station

## Access & Requirements
### Entry Conditions
- **Time Restrictions**: 10 AM - 8 PM (cake has standards)
- **Stat Requirements**: None (but Charm affects pricing)
- **Item Requirements**: Gold (significant amounts)
- **Previous Location Requirements**: None
- **Special Conditions**: Cart changes location daily — must find it

### Finding the Cart
Der Zuckerschock doesn't stay put:
- **Morning**: Near Imperial Square (tourist traffic)
- **Midday**: Kaffeehaus Row (intellectual clientele)
- **Afternoon**: Near The Bassline Opera House (culture seekers)
- **Evening**: MusikGasse (performer crowds)
- **Random Events**: Sometimes appears at quest locations for comedy

### Exit Conditions
- **Normal Exit**: Walk away (after purchase or shame)
- **Completion Requirements**: N/A (vendor location)
- **Failure States**: "Uncultured" status if you mispronounce badly enough (5 min debuff)
- **Progressive Unlocks**: "Cake Connoisseur" status after 200 Sovs spent (slight discount, less judgment)

## Visual Design
### Cart Description
- **Structure**: Ornate wheeled cart, more elaborate than most restaurants
- **Display**: Glass case showing perfect cake slices, temperature controlled
- **Signage**: 
  - Main: "Der Zuckerschock — Konditormeister seit 1847"
  - Secondary: "Pronunciation Guide Available (5 Sovs)"
- **Décor**: Imperial eagle motifs, gold leaf details, tiny chandelier on cart
- **Atmosphere**: Queue of tourists attempting to look sophisticated

### The Cart Details
Every element maximizes pretension:
- Cake slices displayed like museum pieces
- Individual spotlights on each offering
- Velvet rope (yes, for a cart)
- Menu written in Gothic German script
- Price tags in elegant calligraphy (the elegance makes the prices hurt more)
- Customer reviews etched in brass plates (all five stars, all suspicious)

### The Vendor
- **Name**: Frau Tortenmeister ("Mrs. Cake Master")
- **Appearance**: Traditional konditor uniform, pristine white, severe bun, pince-nez glasses
- **Expression**: Default: judgment. Range: mild judgment to extreme judgment.
- **Posture**: Ready to correct pronunciation at any moment

### Technical Specifications
- **Color Palette**: Primary: Chocolate Brown (#3D1C02), Accent: Apricot Glaze (#FFDAB9), Background: Cream (#FFFDD0), Judgmental White (#FFFFFF)
- **Lighting Setup**: Display case backlighting, natural daylight, spotlight drama
- **Particle Systems**: Sugar dust, chocolate sheen, steam from fresh items
- **Animation Elements**: Glass case opening, precise slice cutting, judgmental eyebrow raise
- **Mobile Optimization**: Simple cart, focus on NPC expression range

## Satirical Design
### Theme & Vibe
**Core Concept**: Der Zuckerschock satirizes premium food tourism — specifically the way "authentic" treats come with cultural gatekeeping, pronunciation tests, and prices that suggest the chocolate was hand-delivered by Mozart himself.

The deeper joke: The cakes ARE excellent. The experience around buying them is designed to make you feel unworthy of the excellence. You're not just paying for cake — you're paying for the privilege of being judged while eating it.

### The Pronunciation Economy
Correct pronunciation = better treatment:
- "SAH-khur-TOR-tuh" = Nod of approval, standard price
- "SACK-er-tort" = Visible pain, price increase
- "Chocolate cake" = Existential crisis, refused service (briefly)
- "Zakertordy" = Frau Tortenmeister needs a moment

This extends to all menu items. The menu is a minefield.

### Cultural Targets
- **Primary Satirical Focus**: Food tourism authenticity gatekeeping
- **Secondary Targets**: Premium pricing psychology, cultural snobbery in culinary arts
- **Cultural Specificity**: Viennese cake culture, Sachertorte mythos, konditorei traditions
- **Humor Approach**: Absurd seriousness about dessert
- **Sensitivity Considerations**: Satirizes pretension, not Austrian culture itself

### Buffoon Exploitation
The cart exists to humble tourists:
- Prices increase with obvious tourist indicators
- Pronunciation mistakes are catalogued (she remembers)
- "Recommendations" steer toward most expensive items
- Photos of food require "photography fee"
- The more confident you seem, the harder the tests

### Buffoon Delusion Scenarios

**What bros THINK is happening**: 
"We're getting AUTHENTIC Sinfonian cake from a REAL local vendor!"

**What is ACTUALLY happening**: 
They're paying triple price because they pointed at the menu instead of pronouncing items.

**The Order**:
- **Lord Pilsner**: "I'll have the... *squints* ...SAK-er... torty?"
- **Frau Tortenmeister**: *long pause* "...The Sachertorte."
- **Lord Pilsner**: "Yes! That! The Sacker-tort!"
- **Frau Tortenmeister**: *adds 3 Sovs to price* "Of course."

**The Follow-Up**:
- **Chadwick**: "How much is the chocolate one?"
- **Frau Tortenmeister**: "They are ALL chocolate. Be specific."
- **Chadwick**: "The... brown one?"
- **Frau Tortenmeister**: *adds 5 Sovs* "...The BROWN one. Yes."
- **Bradley**: "The Linzer Torte, please."
- **Frau Tortenmeister**: *perfect pronunciation, slight nod* "...Acceptable."

## Gameplay Mechanics

### Shop System — Premium Pastries

**Menu Items**:

| Item | Base Price | Effect | Pronunciation Bonus/Penalty |
|------|-----------|--------|---------------------------|
| Sachertorte Slice | 12 Sovs | +35 HP, cures Hungry, cures Thirsty | Perfect: 10 Sovs / Butchered: 18 Sovs |
| Linzer Torte | 10 Sovs | +25 HP, +10 SP | Perfect: 8 Sovs / Butchered: 14 Sovs |
| Apfelstrudel | 8 Sovs | +20 HP, cures Thirsty | Perfect: 7 Sovs / Butchered: 12 Sovs |
| Kaiserschmarrn | 14 Sovs | +40 HP, removes Embarrassed | Perfect: 12 Sovs / Butchered: 20 Sovs |
| Topfenstrudel | 9 Sovs | +15 HP, +15 SP | Perfect: 7 Sovs / Butchered: 15 Sovs |
| Punschkrapfen | 6 Sovs | +10 HP, Tipsy status (mild) | Perfect: 5 Sovs / Butchered: 10 Sovs |
| Der Zuckerschock Special | 25 Sovs | Full HP restore, +20 SP, "Sugar High" buff | Perfect: 20 Sovs / Butchered: 35 Sovs |

**"Sugar High" Buff**:
- +15% Speed for 30 minutes
- +10% Charm for 30 minutes
- Followed by "Sugar Crash" (-10% Speed for 15 minutes)

### Pronunciation Mini-Game

**Triggered**: When ordering any item (or can use "point at menu" to skip with price penalty)

**Mechanic**:
- German text appears with phonetic breakdown
- Player selects pronunciation (multiple choice)
- Frau Tortenmeister reacts accordingly

**Pronunciation Tiers**:
| Performance | Price Modifier | Reaction |
|-------------|---------------|----------|
| Perfect | -15% | Approving nod |
| Good | Standard | Neutral acceptance |
| Passable | +10% | Slight wince |
| Poor | +25% | Visible disappointment |
| Catastrophic | +50% | Moment of silence required |

**Learning System**:
- Each successful pronunciation = that item permanently easier
- After 3 perfect orders = "Cake Connoisseur" status (flat 10% discount)
- Bradley has +20% bonus to all pronunciation checks

### Charm Pricing System

High Charm reduces tourist markup:
- 0-1 Charm: +20% base prices (obvious tourist)
- 2-3 Charm: Standard prices (acceptable)
- 4+ Charm: -10% prices (possibly local?)
- 6+ Charm: -15% AND Frau Tortenmeister initiates conversation (rare)

### Special Interactions

**The Photography Fee**:
- Taking photo of cart or food: 3 Sovs charge
- Taking photo with Frau Tortenmeister: 10 Sovs (she hates it)
- Taking photo WITHOUT asking: +5 Sovs on next purchase (she remembers)

**The Recommendation Trap**:
- Asking "what's good?" = steered to 25 Sovs Special
- Asking "what's popular?" = slight respect, honest recommendation
- Asking "what's cheap?" = visible contempt, shown the door (briefly)

**The Comparison Crime**:
- Mentioning any other city's desserts: immediate price increase
- Mentioning chain bakeries: service refusal (temporary)
- Comparing to "American chocolate cake": Frau Tortenmeister needs to sit down

### Cart Location System

**Daily Schedule**:
| Time | Location | Customer Type |
|------|----------|--------------|
| 10 AM - 12 PM | Imperial Square | Morning tourists |
| 12 PM - 3 PM | Kaffeehaus Row | Intellectual lunchers |
| 3 PM - 6 PM | Opera House vicinity | Culture seekers |
| 6 PM - 8 PM | MusikGasse | Evening performers |

**Finding Bonus**:
- Locating cart without asking NPCs: Small Charm boost
- Asking NPCs: They judge you AND give directions
- Following the queue: Usually works (tourist strategy)

### Selfie Spot Integration

**Location**: With cart (if you pay photography fee)

**Standard Photo**:
- Posed with cake slice
- Cart visible in background
- Caption: "Authentic™ Experience"

**"Connoisseur"** Variant:
- Frau Tortenmeister acknowledging you
- Multiple cake items visible
- Caption: "She Knows My Name Now"
- Requires: Cake Connoisseur status

**"The Judge"** Variant (Comedy):
- Frau Tortenmeister's judgment face
- Player mid-mispronunciation
- Caption: "Cultural Education in Progress"
- Requires: Catastrophic pronunciation failure

## NPCs & Characters

### Frau Tortenmeister — The Vendor
- **Role**: Vendor, gatekeeper, pronunciation authority
- **Appearance**: Pristine white konditor uniform, severe bun, pince-nez, judgment incarnate
- **Personality**: Takes cake VERY seriously, has seen too many tourists
- **Function**: Primary shop interface, cultural comedy
- **Dialogue**: 
  - "Welcome to Der Zuckerschock. I assume you cannot pronounce anything on the menu."
  - "The Sachertorte is made with seventeen layers of tradition and one layer of disappointment when tourists call it 'chocolate cake.'"
  - *after good pronunciation* "...Perhaps there is hope for you yet."

### The Queue NPCs
- **Role**: Atmosphere, waiting game, commentary
- **Types**: Nervous tourists, confident locals, confused backpackers
- **Function**: Build anticipation, demonstrate consequences
- **Dialogue**: 
  - Tourist: "What did she say? Did I order wrong? Why is she looking at me like that?"
  - Local: *perfect pronunciation, smug satisfaction*
  - Backpacker: "I just wanted chocolate cake, man..."

### Regulars (Rotating)
- **The Cake Blogger**: Photographs everything, tips extensively, still mispronounces
- **The Nostalgic Local**: "It was better in my grandmother's day" (it wasn't)
- **The Confused American**: Just wants to understand the portions

### Bros' Full Cart Experience

**Finding the Cart**:
- **Chadwick**: "Is that... a CAKE CART? With a VELVET ROPE?!"
- **Lord Pilsner**: "Dude, Sinfonia takes dessert SERIOUSLY. This is CULTURE."
- **Bradley**: "The prices visible from here appear... aggressive."

**In the Queue**:
- **Chadwick**: "Why is everyone whispering? It's just cake."
- **Local Ahead**: *flawless Apfelstrudel pronunciation*
- **Frau Tortenmeister**: *approving nod*
- **Tourist Ahead**: "Uh... apple... stew-dell?"
- **Frau Tortenmeister**: *prolonged silence*
- **Lord Pilsner**: "...I'm suddenly nervous."

**The Order Attempt**:
- **Lord Pilsner**: "I'll have the Sacker-torty and the Kaiser-schmar... shmar..."
- **Frau Tortenmeister**: "Kaiserschmarrn."
- **Lord Pilsner**: "Kaiser-smarren."
- **Frau Tortenmeister**: "...No."
- **Lord Pilsner**: "Kaiser-schmarrn?"
- **Frau Tortenmeister**: "...Close enough. 34 Sovs."
- **Lord Pilsner**: "The menu said 26 Sovs!"
- **Frau Tortenmeister**: "The menu assumed competence."

**Post-Purchase**:
- **Chadwick**: *eating* "Oh my god. This is INCREDIBLE. Worth every Sov."
- **Lord Pilsner**: *eating* "Even the judgment tax?"
- **Bradley**: *eating, satisfied* "I pronounced everything correctly. I paid 22 Sovs."
- **Lord Pilsner**: "BRADLEY."

## System Integration

### Cross-Location Dependencies
- **Kaffeehaus Row**: Primary afternoon location, intellectual customers
- **Café Existenz**: Philosophers debate whether cake is "authentic"
- **The Bassline Opera House**: Afternoon location, opera intermission sales
- **Imperial Square**: Morning tourist hunting grounds

### Quest Integration
- **"The Perfect Pronunciation"**: Master all menu items (achievement)
- **"Cake Connoisseur"**: Spend 200 Sovs, earn permanent discount
- **"The Comparison Crime"**: Accidentally offend Frau Tortenmeister
- **"Cart Hunter"**: Find the cart at all four locations in one day

### Achievement Track
- **"First Slice"**: Purchase any item
- **"Acceptable"**: Perfect pronunciation on any item
- **"Cake Connoisseur"**: Earn permanent status
- **"The Full Menu"**: Try every item
- **"Cart Stalker"**: Find cart at all locations
- **"Photography License"**: Pay all photo fees in one visit
- **"The Ultimate Crime"**: Mention American chocolate cake
- **"Redemption Arc"**: Return after "Uncultured" status

## Audio Design

### Environmental Audio
- **Ambient**: Street sounds, queue murmuring, display case hum
- **Music**: None (cake is serious business)
- **Interactive**: Glass case opening, precise cutting, register ding
- **Comedy**: Disappointed sigh on bad pronunciation, approval hum on good

### Character Audio
- **Frau Tortenmeister**: Clipped, precise, German accent, ranges from neutral to pained
- **Queue NPCs**: Anxious whispers, relieved exhales, defeated sighs
- **Pronunciation feedback**: Clear audio difference between success and failure

## Implementation Specifications

### Technical Requirements
- **Asset List**:
  - Ornate cart (single main asset)
  - Display case with items
  - Frau Tortenmeister sprite (expression range)
  - 4 background location variants
  - Queue NPC variants
- **Animation Requirements**:
  - Display case opening
  - Cake slicing (precision)
  - Vendor expression changes
  - Queue movement
- **Performance Budget**: 35 FPS target, max 10 draw calls, 25MB memory
- **Platform Considerations**: Simple scene, focus on NPC interaction

### Development Timeline
- **Asset Creation**: 4 hours (cart detail, NPC expressions)
- **Implementation Phase**: 5 hours (shop system, pronunciation game, location rotation)
- **Testing Requirements**: Price economy, pronunciation balance
- **Polish Phase**: 2 hours (comedy timing, expressions)

## Quality Assurance Checklist
- [x] **World consistency verified** (Sinfonia specific)
- [x] **Cultural specificity confirmed** (Viennese cake culture, konditorei traditions)
- [x] **Satirical targets appropriate** (Food tourism pretension, not Austrian cuisine)
- [x] **Gameplay value established** (Premium consumables, pronunciation game, location hunt)
- [x] **Sinfonia requirements met**:
  - [x] Formal expectations (pronunciation standards)
  - [x] Imperial history (est. 1847)
  - [x] High society gatekeeping
  - [x] Culinary culture
- [x] **No crypto elements** (Pure food snobbery)

---

## PNG Asset Requirements Summary

> **Authority: `PNG_Assets/Torte_Royale_PNG_Assets.md`.** That spec is the artist's delivery contract and **wins over this file** on sprite filenames, dimensions, and sheet membership. Nothing here ships as a standalone per-sprite PNG — every sprite is a **cell inside one of the sheets below**. Cell sizes are specified per row inside the spec; where this file previously stated a blanket cell size, the spec's per-row figure wins. Do not re-derive individual filenames from this summary.

### Required PNG Files (6 sheets)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | torte_royale_cart.png | 512x384 |
| 2 | torte_royale_display_case.png | 512x256 |
| 3 | frau_tortenmeister.png | 512x384 |
| 4 | torte_royale_queue_npcs.png | 512x384 |
| 5 | torte_royale_backdrops.png | 512x512 |
| 6 | torte_royale_effects_ui.png | 512x512 |

### Names retired from this summary (do not request these files)

These filenames appeared in earlier revisions of this summary and are **not delivered**. Each is a cell inside one of the sheets above — look it up by description in `PNG_Assets/Torte_Royale_PNG_Assets.md`.

- `cart_main.png`
- `display_case.png`
- `cart_location_square.png`
- `cart_location_kaffeehaus.png`
- `cart_location_opera.png`
- `cart_location_musik.png`
- `frau_tortenmeister_approval.png`
- `frau_tortenmeister_judgment.png`
- `frau_tortenmeister_pained.png`
- `queue_tourist.png`
- `queue_local.png`
- `sachertorte_slice.png`
- `linzer_torte.png`
- `apfelstrudel.png`
- `kaiserschmarrn.png`
- `topfenstrudel.png`
- `punschkrapfen.png`
- `zuckerschock_special.png`
- `pronunciation_ui.png`
- `cake_connoisseur_badge.png`
- `sugar_high_icon.png`

---

*Der Zuckerschock: Where the cakes are perfect, the prices are flexible (upward), and your pronunciation determines your worth as a human being. Find the cart. Brave the queue. Master the German. Eat the cake. It's worth it. Frau Tortenmeister believes in you. (She doesn't, but the cake is still worth it.)*
