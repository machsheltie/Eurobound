# Haute Couture Haberdashery

*Where the fitting rooms have more mirrors than a funhouse, the tailor knows your flaws before you undress, and "off the rack" is a phrase that causes physical pain*

## Location Identity
- **Location ID**: sinfonia_imperialsquare_haute_couture_01
- **Display Name**: Haute Couture Haberdashery
- **Satirical Subtitle**: "You Can't Afford to Look This Good (But You Will)"
- **World Location**: Sinfonia
- **Area Zone**: Imperial Square, Grand Entrance District
- **Location Type**: Equipment Shop / Formal Wear / Accessories / Social Armor

## Access & Requirements
### Entry Conditions
- **Time Restrictions**: 10 AM - 7 PM (fashion keeps civilized hours)
- **Stat Requirements**: None to enter, but staff treatment scales with current outfit quality
- **Item Requirements**: Gold (significant amounts)
- **Previous Location Requirements**: None
- **Special Conditions**: Entering in "casual" attire triggers assessment protocol

### Exit Conditions
- **Normal Exit**: Front door (with or without purchase, with or without dignity)
- **Completion Requirements**: N/A (shop location)
- **Failure States**: None (they'll take anyone's money)
- **Progressive Unlocks**: "Valued Client" after 500 Sovs spent (private fitting room, advance notice of new stock)

## Visual Design
### Exterior Description
- **Façade**: Elegant storefront with gold-lettered signage, mannequins in windows posed dramatically
- **Windows**: Display formal wear that costs more than rent, changed weekly
- **Entrance**: Glass door with brass handle, bell that announces arrivals (judgmentally)
- **Signage**: 
  - Main: "Haute Couture Haberdashery — Bespoke Excellence Since 1822"
  - Window: "By Appointment Preferred. Walk-Ins Tolerated."
- **Atmosphere**: Intimidating elegance designed to make you spend more

### Interior Layout — The Temple of Textiles

**The Showroom (Main Floor)**
- Polished marble floors, crystal chandeliers, strategic lighting
- Displays organized by occasion: Opera, Ball, Formal Dining, "Being Seen"
- Each piece spotlit like museum artifacts
- Prices not visible (if you have to ask...)
- Velvet seating for those waiting to be judged

**The Fitting Rooms (Assessment Zone)**
- Floor-to-ceiling mirrors (every angle, no escape)
- Lighting that reveals every flaw (intentional)
- Bell to summon tailor (who was already watching)
- Private rooms for Valued Clients (slightly less humiliating)

**The Accessories Alcove (Add-On Sales)**
- Gloves, cufflinks, monocles, capes
- "Essential additions" to any purchase
- Where the profit margin lives
- Each item displayed on velvet pillows
- **The Locked Vitrine — *Objets d'Héritage***: at the back of the alcove, a single sealed glass case on its own spotlight, black velvet, its own key (kept apart from every other key in the shop). Inside, alone: **The Gold Circle Coin** (`item_gold_circle_coin`), gold foil, seal unbroken. Placard, hand-set: "Molded 1990. A piece of cinema history. **It is not for sale. It is for aspiration.**"
- The vitrine is not stock. It is not priced, not in the add-on patter, and no assistant will discuss it — inquiries are redirected to Monsieur Aiguille, who declines offers without hearing the number

**The Alteration Workshop (Visible)**
- Glass wall showing tailors at work
- Demonstration of craftsmanship
- Subtle pressure: "See how much work goes into this?"
- Where excuses die ("We can alter ANYTHING")

### The Shop Aesthetic
Every detail reinforces "you need to be better":
- Mirrors positioned to catch unflattering angles
- Lighting shifts to make current clothes look worse
- Staff outfits nicer than anything you're wearing
- Classical music suggesting sophistication you lack
- Complimentary champagne (you'll need it when you see prices)

### Technical Specifications
- **Color Palette**: Primary: Velvet Black (#1A1A1A), Accent: Gold Thread (#CFB53B), Background: Cream Marble (#FFF8E7), Judgment Gray (#808080)
- **Lighting Setup**: Chandelier glamour, spotlight drama, fitting room interrogation
- **Particle Systems**: Fabric shimmer, dust motes in light beams, champagne bubbles
- **Animation Elements**: Mannequin poses, mirror reflections, tailor measurements
- **Performance Optimization**: Static showroom, focus on item inspection and NPC interaction

## Satirical Design
### Theme & Vibe
**Core Concept**: Haute Couture Haberdashery satirizes luxury fashion retail — the way high-end shops make customers feel inadequate to justify prices, the performance of exclusivity, and the absurd seriousness applied to clothing.

The deeper joke: The clothes ARE excellent. They WILL make you look better. But the experience of buying them is designed to make you feel you don't deserve them until you pay. It's psychological warfare dressed in silk.

### The Assessment Protocol
What happens when you enter in casual clothes:
1. Door chime sounds (slightly disappointed tone)
2. Staff member appears (assessing gaze)
3. Polite greeting with subtle emphasis on "help"
4. Guided toward "accessible" options first
5. Gradual revelation of better items based on demonstrated budget

If you enter already well-dressed:
1. Door chime sounds (welcoming tone)
2. Staff member appears (approving nod)
3. Warm greeting, champagne offered
4. Full showroom access, suggestions based on taste
5. "You clearly understand quality"

### Cultural Targets
- **Primary Satirical Focus**: Luxury retail psychology, fashion gatekeeping
- **Secondary Targets**: "Investment pieces" justification, formal wear obsession
- **Cultural Specificity**: Sinfonian haute-tailoring traditions, old-imperial concert-hall dress influence
- **Humor Approach**: Staff genuinely believe they're helping you achieve your potential
- **Sensitivity Considerations**: Satirizes industry practices, not body image issues

### Buffoon Exploitation
The shop sees the bros coming:
- Their current outfits are assessed instantly (found wanting)
- They'll be guided toward "transformative" pieces
- Every compliment is backhanded ("This will help SO much")
- They'll spend more than planned (the system works)

## Gameplay Mechanics

### Equipment System — Formal Wear

**Core Equipment**:
| Item | Price | Stats | Special Effect |
|------|-------|-------|----------------|
| Formal Gloves | 75 Sovs | +2 Charm | Reduces Embarrassed duration by 50% |
| Conductor's Tuxedo | 300 Sovs | +5 Charm, +3 Performance | +15% damage on rhythm-timed attacks |
| Opera Cape | 200 Sovs | +4 Style, +2 Dramatic Flair | Dramatic entrance bonus (+10 Bravado when entering locations) |
| Ballroom Shoes | 150 Sovs | +3 Dance, +2 Speed | +20% Speed during formal events and dance duels |
| Cultural Critic's Monocle | 175 Sovs | +3 INT, +2 Art Authentication | Reveals hidden item values, forgery detection |
| Maestro's Cufflinks | 125 Sovs | +2 Conductor Skills, +2 Musical Timing | +10% rhythm game timing window |

**Premium Collection** (Valued Client access):
| Item | Price | Stats | Special Effect |
|------|-------|-------|----------------|
| The Emperor's Ensemble | 750 Sovs | +8 Charm, +5 Style | Automatic respect from all Sinfonia NPCs |
| Prima Donna Gown | 600 Sovs | +6 Charm, +4 Performance | +25% Bravado gains in social encounters |
| The Phantom's Mask | 400 Sovs | +4 Mystery, +3 Charm | Identity hidden in masquerade (+1 social combat round) |
| Virtuoso's Vest | 350 Sovs | +4 Performance, +3 Charm | Musical attacks gain +15% critical chance |
| Aristocrat's Walking Stick | 250 Sovs | +3 Style, +2 Charm | Weapon: 1.2x damage, chance to Embarrass |

**Accessories**:
| Item | Price | Stats | Special Effect |
|------|-------|-------|----------------|
| Silk Pocket Square | 50 Sovs | +1 Charm | Prevents "Disheveled" status |
| Pearl Cufflinks | 80 Sovs | +1 Style | +5% shop discounts when worn |
| Velvet Bow Tie | 60 Sovs | +1 Charm, +1 Performance | Required for some formal venues |
| Opera Glasses | 100 Sovs | +2 Perception | Ranged advantage in combat, see NPC details |
| Ivory Fan | 90 Sovs | +2 Style | Can fan away status effects (one use per battle) |

### The Fitting Experience

**Fitting Room Mechanic**:
When trying on equipment:
1. Enter fitting room
2. Mirrors show character in new outfit
3. Tailor provides "honest" assessment
4. Comparison to current stats visible
5. Pressure to buy increases with time spent

**Tailor Commentary**:
| Situation | Tailor Says |
|-----------|-------------|
| Item suits you | "Ah, yes. This was MADE for someone like you." |
| Item doesn't suit | "We can... work with this. Alterations, perhaps." |
| Trying something expensive | "Quality recognizes quality." |
| Trying something cheap | "A... practical choice." |
| Leaving without purchase | "Perhaps another time. When you're... ready." |

### Valued Client System

**Unlocked After**: 500 Sovs total spent

**Benefits**:
- Private fitting room (less public judgment)
- 10% discount on all items
- First access to new inventory
- Tailor remembers your sizes
- Champagne is better quality
- Name used (they learned it)

**Valued Client Tiers**:
| Tier | Spent | Benefits |
|------|-------|----------|
| Client | 0 Sovs | Standard treatment |
| Valued Client | 500 Sovs | Private room, 10% off |
| Distinguished Client | 1000 Sovs | 15% off, reserved items |
| Patron of Fashion | 2000 Sovs | 20% off, custom orders available |

### Special Services

**Alterations**:
- Any purchased item can be altered
- +50 Sovs for "perfect fit" bonus (+1 to primary stat)
- Takes in-game time (return later)

**Outfit Consultation**:
- 100 Sovs for full wardrobe advice
- Tailor suggests items for your build/class
- Reveals hidden synergies between equipment
- Includes backhanded compliments (free)

**Rush Tailoring**:
- Need formal wear NOW?
- +50% price for immediate availability
- Tailor sighs but complies

### Selfie Spot Integration

**Location**: Three-way mirror in showroom

**Standard Photo**:
- Posed in new outfit
- Multiple mirror angles visible
- Caption: "Investment Piece"

**"The Transformation"** Variant:
- Before/after comparison
- Old clothes visible in corner
- Caption: "The Old Me Is Dead"
- Requires: Spend 300 Sovs+ in one visit

**"Distinguished Client"** Variant:
- Private fitting room
- Champagne in hand
- Caption: "They Know My Name Now"
- Requires: Patron of Fashion status

## NPCs & Characters

### Monsieur Aiguille — The Head Tailor
- **NPC ID**: `sinfonia_npc_monsieur_aiguille_01`
- **Role**: Primary shop interface, fitting authority, gentle devastation
- **Appearance**: Immaculate three-piece suit, measuring tape around neck, perpetually assessing
- **Personality**: Genuinely believes he's helping people become their best selves (through clothing)
- **Function**: Shop interface, fitting room commentary, style advice
- **Dialogue**: 
  - "Welcome to Haute Couture. I see we have... work to do."
  - "This fabric was woven by artisans who have dedicated their LIVES to this craft. You're worth it. Probably."
  - *measuring* "Interesting proportions. We can... flatter them."
  - *after purchase* "You're already standing differently. See? CONFIDENCE."

### The Shop Assistants
- **Role**: Secondary service, champagne delivery, subtle pressure
- **Appearance**: Impeccably dressed, moving silently, always nearby
- **Function**: Fetch items, provide options, apply sales psychology
- **Dialogue**: 
  - "Might I suggest the matching cufflinks? They really complete the look."
  - "That piece is very popular. We only have one left in your... size."
  - "Champagne while you decide?"

### The Other Customers
- **Role**: Social comparison, atmosphere, pressure
- **Types**: Confident aristocrats, nervous tourists, decisive regulars
- **Function**: Make you feel you should buy more
- **Dialogue**: 
  - Aristocrat: *doesn't acknowledge your existence*
  - Tourist: "Is this... is this too much? It's too much, right?"
  - Regular: *hands over card without looking at price*

### Bros' Haute Couture Haberdashery Reactions

**Entering**:
- **Lord Pilsner**: *in tourist clothes* "Whoa, this place is FANCY."
- **Monsieur Aiguille**: *assessing gaze* "...Yes. Welcome. I see you're in need of... everything."
- **Chadwick**: "We're here for the EXPERIENCE!"
- **Monsieur Aiguille**: "Mmm. We can provide... that."

**The Assessment**:
- **Monsieur Aiguille**: *circling Lord Pilsner* "The shoulders... the posture... the fabric choices..."
- **Lord Pilsner**: "What about them?"
- **Monsieur Aiguille**: "Nothing that can't be fixed. With time. And investment."
- **Bradley**: "I'd like to see the monocles."
- **Monsieur Aiguille**: *slight approval* "A man of focus. This way."

**Trying On**:
- **Chadwick**: *in Conductor's Tuxedo* "How do I look?!"
- **Monsieur Aiguille**: "...Better. Considerably better. The improvement is notable."
- **Chadwick**: "That's a compliment, right?"
- **Monsieur Aiguille**: "It is an observation of progress."

**The Price Reveal**:
- **Lord Pilsner**: "I'll take the cape! What's the damage?"
- **Monsieur Aiguille**: "The Opera Cape is 200 Sovs."
- **Lord Pilsner**: *stage-whisper to Chadwick and Bradley, audible from the street* "Two hundred. TWO HUNDRED, boys. He has no idea what he's sitting on. Nobody make a face. Act natural."
- **Chadwick**: *making a face* "We are ROBBING this man."
- **Lord Pilsner**: *to Aiguille, casual to the point of theatre* "Yeah, alright. I'll take it off your hands. Free up some rack space for you."
- **Monsieur Aiguille**: "For a transformation. But if value isn't important to you..."
- **Lord Pilsner**: "I— no, I GET it. It's an INVESTMENT."
- **Monsieur Aiguille**: *slight smile* "Indeed."
- **Monsieur Aiguille**: *to the assistant, at entirely normal volume, writing the ticket* "The cape is 200 Sovs. It has been 200 Sovs all season. I should not like the gentleman to feel he had underpaid."

**Post-Purchase**:
- **Lord Pilsner**: *wearing cape* "I feel like a DIFFERENT PERSON."
- **Monsieur Aiguille**: "You look like one. My work here is done."
- **Chadwick**: "EIGHT HUNDRED SOVS, boys — for ALL of it. That's not a receipt, that's a RÉSUMÉ. They don't let you spend that in here unless they can TELL. We came out AHEAD and we're not tourists anymore — we're CLIENTELE."
- **Bradley**: "Elevated."

**The Vitrine (PATH A handover — "Nothing Is Getting Through")**:
- **Monsieur Aiguille**: *unlocks the vitrine with the separate key, lifts the Coin with both hands, entirely unironic* "You understand what this is. No — you do not. But you will carry it, and it will be carried, and that is the arrangement."
- **Lord Pilsner**: "Totally. Yeah. It's a coin."
- **Monsieur Aiguille**: *seating it in a burgundy presentation sleeve before he will let go of it* "Out of direct sun. Never in a trouser pocket. If I hear otherwise, I will know."
- **Bradley**: "We promise."
- **Monsieur Aiguille**: "Mm."

## System Integration

### Cross-Location Dependencies
- **Imperial Square**: Home district, visible storefront
- **Baroness' Ballroom**: Formal attire required for entry
- **The Black-Tie Backroom**: Black-Tie attire sold here
- **The Bassline Opera House**: Opera wear for day attendance

### Quest Integration
- **"Dress for Success"**: Acquire formal wear for masquerade infiltration
- **"The Emperor's Ensemble"**: Premium quest to unlock highest-tier item
- **"Fashion Critic"**: Monsieur Aiguille asks you to assess others' outfits
- **"Patron of Fashion"**: Reach maximum client status
- **"Nothing Is Getting Through"** (`debaucheryville_sidequest_nothing_is_getting_through_01`): this shop is the "HOUSE OF NEEDLES" of Hamstradamus's prophecy (Aiguille = French for "needle"). Three bros arrive from Debaucheryville carrying `the_herp` and are met by the shop's EXISTING Assessment Protocol on first visit — that snub is played completely straight and is not modified for this quest. The Gold Circle Coin in the alcove vitrine is the objective; two resolutions:
  - **PATH A — "Become Someone Who Belongs Here"**: reach **Valued Client** on the existing 500 Sovs tier (no new tier, no new pricing), then complete one absurd errand for Monsieur Aiguille. He opens the vitrine himself, with genuine ceremony (see "The Vitrine (PATH A handover)" under Bros' Reactions) — he respects the Coin considerably more than they do, and always will.
  - **PATH B — "Big. Huge. Mistake."**: after-hours infiltration (shop closes 7 PM per Entry Conditions) requiring formal wear purchased from this shop; the marquee beat is three men holding mannequin poses in opera capes on the showroom floor while the night porter (`sinfonia_npc_night_porter_01`) passes with a torch.
- Quest detail, scene text, and branch logic live in `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md`. This file registers only the vitrine, the shop-side requirements of both paths, and Aiguille's handover beat.

### Achievement Track
- **"First Fitting"**: Try on any item
- **"Well Dressed"**: Purchase first equipment piece
- **"Valued Client"**: Reach first status tier
- **"Patron of Fashion"**: Reach maximum status
- **"The Transformation"**: Buy complete outfit (500 Sovs+)
- **"Accessorized"**: Own 5+ accessories
- **"Cape Confidant"**: Buy the Opera Cape

## Audio Design

### Environmental Audio
- **Ambient**: Soft classical music, champagne fizz, fabric rustling, hushed conversations
- **Music**: Elegant strings, piano, nothing too loud
- **Interactive**: Cash register (refined chime), fitting room curtain, mirror inspection
- **Comedy**: Slight "sting" when prices revealed, champagne cork when Valued Client

### Character Audio
- **Monsieur Aiguille**: Precise French-accented English, measured delivery, occasional sigh
- **Assistants**: Soft, helpful, slightly urgent
- **Price reveal**: Subtle musical emphasis

## Implementation Specifications

### Technical Requirements
- **Asset List**:
  - Storefront exterior
  - Showroom with displays
  - Fitting rooms with mirrors
  - Accessories alcove
  - Workshop visible through glass
  - Monsieur Aiguille and assistants
  - Equipment items displayed
- **Animation Requirements**:
  - Mirror reflections
  - Fabric shimmer
  - Character outfit preview
  - Tailor measuring
- **Performance Budget**: 60 FPS target, max 15 draw calls, 40MB memory
- **Platform Considerations**: Equipment preview system, mirror reflections simplified

### Development Timeline
- **Asset Creation**: 8 hours (detailed shop, equipment displays)
- **Implementation Phase**: 8 hours (shop system, fitting mechanic, client tiers)
- **Testing Requirements**: Equipment balance, price points, status effects
- **Polish Phase**: 4 hours (atmosphere, NPC dialogue, comedy timing)

## Quality Assurance Checklist
- [x] **World consistency verified** (Sinfonia specific)
- [x] **Cultural specificity confirmed** (Sinfonian haute-tailoring, formal wear traditions)
- [x] **Satirical targets appropriate** (Luxury retail, not fashion itself)
- [x] **Gameplay value established** (Equipment shop, stat bonuses, social requirements)
- [x] **Sinfonia requirements met**:
  - [x] Formal/high society etiquette
  - [x] Imperial aesthetic
  - [x] Luxury/status items
  - [x] Cultural gatekeeping theme
- [x] **No crypto elements** (Pure fashion snobbery)

---

## PNG Asset Requirements Summary

> **Authority: `PNG_Assets/Haute_Couture_Haberdashery_PNG_Assets.md`.** That spec is the artist's delivery contract and **wins over this file** on sprite filenames, dimensions, and sheet membership. Nothing here ships as a standalone per-sprite PNG — every sprite is a **cell inside one of the sheets below**. Cell sizes are specified per row inside the spec; where this file previously stated a blanket cell size, the spec's per-row figure wins. Do not re-derive individual filenames from this summary.

### Required PNG Files (8 sheets)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | haute_couture_tileset.png | 1024x512 |
| 2 | haute_couture_landmarks.png | 512x384 |
| 3 | monsieur_aiguille.png | 384x288 |
| 4 | night_porter.png | 256x288 |
| 5 | haute_couture_npcs.png | 384x288 |
| 6 | haute_couture_equipment.png | 512x256 |
| 7 | haute_couture_effects.png | 256x192 |
| 8 | haute_couture_ui.png | 256x256 |

### Names retired from this summary (do not request these files)

These filenames appeared in earlier revisions of this summary and are **not delivered**. Each is a cell inside one of the sheets above — look it up by description in `PNG_Assets/Haute_Couture_Haberdashery_PNG_Assets.md`.

- `storefront_exterior.png`
- `showroom_main.png`
- `fitting_room.png`
- `accessories_alcove.png`
- `workshop_visible.png`
- `mannequin_display.png`
- `champagne_service.png`
- `private_fitting.png`
- `monsieur_aiguille_approval.png`
- `monsieur_aiguille_measuring.png`
- `shop_assistant.png`
- `aristocrat_customer.png`
- `nervous_tourist.png`
- `formal_gloves.png`
- `conductors_tuxedo.png`
- `opera_cape.png`
- `ballroom_shoes.png`
- `cultural_critics_monocle.png`
- `maestros_cufflinks.png`
- `emperors_ensemble.png`
- `prima_donna_gown.png`
- `phantoms_mask.png`
- `virtuosos_vest.png`
- `aristocrats_walking_stick.png`
- `silk_pocket_square.png`
- `velvet_bow_tie.png`
- `opera_glasses.png`
- `ivory_fan.png`
- `valued_client_badge.png`

---

*Haute Couture Haberdashery: Where the mirrors show who you could be, the prices show who you'll need to become, and the tailor believes — truly believes — he's changing lives. One hem at a time. Walk in a tourist. Walk out transformed. The cape is worth it. Trust us.*
