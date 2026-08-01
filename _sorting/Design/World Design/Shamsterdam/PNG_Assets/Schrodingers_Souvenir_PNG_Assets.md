# Schrödinger's Souvenir - Complete PNG Asset Requirements

## 📋 Overview
Schrödinger's Souvenir sells products that are completely legal in Shamsterdam, probably fine to buy, definitely confusing to understand, and variably legal to bring home. This document specifies every PNG asset for the shop: the green professional storefront and its quantum cat mascot, the four legality zones running front-to-back from Definitely to Schrödinger, the education corner nobody reads, the seed display and its polite fiction, Daan and Yuki dispensing maximum information with minimum liability, and the customs checkpoint where the wavefunction finally collapses. Its satirical essence in a sentence: everyone knows exactly what is happening, and nobody is going to say it out loud.

**Location ID:** `shamsterdam_tourist_schrodingers_souvenir_01`
**Theme:** Legal gray-zone commerce — selling ambiguity at markup while remaining scrupulously, exhaustingly, technically correct
**Zone:** Tourist district, positioned between actual coffeeshops and normal souvenir shops (liminal by design)
**Hours:** 10 AM - 10 PM (extended tourist confusion hours)
**Primary Function:** Retail shop / consequence generator — four-zone legality browsing, "Is This Legal?" interaction loop, the Seed Purchase Ritual, Suspicious Souvenir inventory tagging, and the Customs Checkpoint observation event

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Hemp Green | #228B22 | Storefront, signage, zone 1-2 shelving, mascot |
| CBD Gold | #FFD700 | Product highlights, wellness shelf accents |
| Legal Gray | #808080 | Disclaimer boards, asterisks, zone 3 fixtures |
| Warning Red | #FF0000 | Export risk indicators, customs, "HIGH" chips |
| Retail White | #FAFAF5 | Professional lighting wash, clean shelving |
| Superposition Violet | #6A4C93 | Quantum shimmer, seed section grade, collapse FX |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/schrodingers_souvenir/
├── environment/
│   ├── schrodingers_interior_main.png
│   └── schrodingers_exterior_zones.png
├── objects/
│   └── schrodingers_products.png
├── npcs/
│   ├── npc_daan_yuki.png
│   └── npc_schrodingers_customers.png
├── effects/
│   └── schrodingers_effects.png
└── ui/
    └── schrodingers_ui.png
```

---

## 🏪 Sprite Sheet 1: Interior Main Background
**File:** `schrodingers_interior_main.png`
**Dimensions:** 1920x1080 pixels (standalone full-scene background — not atlased)
**Color Palette:** #228B22, #FAFAF5, #808080, #6A4C93

### Scene Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Interior Backdrop | (0, 0) | 1920x1080 | Full scene: professional retail floor reading front-to-back as a legality gradient — bright clean hemp goods at the entrance, CBD wellness shelving mid-floor, smoking accessories in a glass case toward the rear, and the seed cabinet in the back corner under noticeably cooler light; education corner on the left wall, checkout counter right, disclaimer board mounted above the register where everyone can see it and nobody will read it |

### Technical Notes:
- Anchor points (document in layer names): Zone 1 shelving at (320, 640), Zone 2 shelving at (768, 640), Zone 3 case at (1216, 608), Zone 4 seed cabinet at (1664, 576), education corner at (192, 448), checkout counter at (1536, 832), disclaimer board at (1536, 320), door threshold at (960, 1024)
- Lighting gradient is baked into the backdrop: brightness and warmth step down by roughly 8% per zone from front to back, so the room itself grades from "clearly fine" to "your customs agent will have questions" without a single word of UI
- Seed corner painted one full step cooler and violet-shifted; the Seed Section Hush Grade overlay (Sheet 6) intensifies this on approach
- Nothing in the backdrop may read as sketchy — the entire joke depends on the shop looking like a well-run pharmacy

---

## 🐱 Sprite Sheet 2: Exterior, Signage & Zone Fixtures
**File:** `schrodingers_exterior_zones.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #228B22, #808080, #FFD700, #6A4C93

### Exterior & Mascot:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Schrödinger's Storefront | (0, 0) | 384x384 | Green-heavy professional retail front, clean glazing, legally distinct from a coffeeshop and visibly working at it |
| Quantum Cat (Superposition) | (384, 0) | 128x128 | Mascot in blended legal/illegal state, hemp leaf accessory, deliberately ambiguous outline |
| Quantum Cat (Observed — Legal) | (512, 0) | 128x128 | Collapsed state: relaxed, thumbs-up, green |
| Quantum Cat (Observed — Illegal) | (640, 0) | 128x128 | Collapsed state: wide-eyed, red-shifted, extremely still |
| Main Sign "SCHRÖDINGER'S SOUVENIR" | (768, 0) | 256x128 | Clean retail typography with the cat as the logotype's period |

### Signage & Disclaimers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "THIS IS NOT A COFFEESHOP" | (384, 128) | 256x64 | Large. Prominent. Ignored hourly. |
| "All products comply with Dutch law*" | (384, 192) | 256x64 | The asterisk is the load-bearing element |
| "Your country's laws are your responsibility. Good luck." | (384, 256) | 256x64 | The most honest sign in Shamsterdam |
| "Until observed by customs, all products exist in superposition" | (384, 320) | 256x64 | The shop's actual philosophy, printed |
| Window Display Rack | (640, 128) | 128x256 | HEMP / CBD / LEGAL in the window, each word asterisked |
| Legal Disclaimer Board | (768, 128) | 256x128 | Wall-mounted, dense, comprehensive, unread |
| Asterisk Detail (Leads Nowhere) | (768, 256) | 128x128 | Close-up plate: the asterisk has no corresponding footnote |
| "Premium Hemp Products" Subtitle Plate | (896, 256) | 128x128 | "Shamsterdam's Finest" |

### The Four Legality Zones:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Zone 1 — The Definitely Legal | (0, 384) | 384x256 | Front of shop: hemp clothing, bags, actual rope, CBD skincare. Bright, uncomplicated, boring. |
| Zone 2 — The Probably Legal | (384, 384) | 384x256 | Mid-floor: CBD oils at varying concentrations, hemp food, "wellness" items with leaf imagery |
| Zone 3 — The Questionably Legal | (768, 384) | 256x256 | Rear: smoking accessories "for tobacco use," complex cannabinoid profiles, items requiring explanation |
| Zone 4 — The Souvenir Seeds | (0, 640) | 256x256 | Back corner, cooler light: seeds as collector's items, maximum Schrödinger energy |

### Fixtures & Stations:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Education Corner (CBD vs THC) | (256, 640) | 256x192 | Infographic wall, patient staff, limited effectiveness |
| Checkout Counter | (512, 640) | 256x192 | Register, sealed-bag rack, verbal disclaimer delivery point |
| Customs Checkpoint | (768, 640) | 256x256 | Airport resolution zone: table, scanner, agent position, one open suitcase |
| Product Confusion Matrix Poster | (256, 832) | 256x64 | Eight product rows, four legality columns, one honest "Schrödinger" cell |
| "NOT FOR GERMINATION" Sign Set | (512, 832) | 256x64 | Four variants at four sizes, positioned so you cannot avoid all of them |

### Small Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hemp Clothing Rack | (0, 896) | 128x128 | Zone 1 fixture |
| CBD Shelf Unit | (128, 896) | 128x128 | Zone 2 fixture, tidy, pharmacy-adjacent |
| Smoking Accessory Case | (256, 896) | 128x128 | Zone 3 fixture, glass, locked, well-lit |
| Seed Display Cabinet | (384, 896) | 128x128 | Zone 4 fixture, glass front, small brass lock |
| Retail Lighting Fixture | (512, 896) | 128x128 | Professional track lighting; nothing sketchy anywhere |
| Floor Tile (Tileable) | (640, 896) | 128x128 | Clean commercial vinyl, seamless on all four edges |
| Shopping Basket | (768, 896) | 128x64 | Green plastic, retail-normal |
| Sealed Bag Rack | (768, 960) | 128x64 | Discreet packaging, available on request |
| Airport Conveyor Prop | (896, 896) | 128x128 | Customs checkpoint dressing |

### Technical Notes:
- The three Quantum Cat states are the same silhouette at the same anchor so the collapse animation is a pure crossfade with no shape pop
- Zone blocks are authored as complete shelving walls so an entire zone renders in one draw call
- Floor Tile must seam on all four edges; it is the only tiled asset in the location
- All signage text is baked at 2x internal resolution and flagged for the ASTC 4x4 exception list — this location's comedy is 60% readable text

---

## 🧪 Sprite Sheet 3: Products & Documents
**File:** `schrodingers_products.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #228B22, #FFD700, #808080, #6A4C93

### Larger Products:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hemp Tote Bag | (0, 0) | 48x48 | €15 — actually just a bag |
| Hemp Protein Powder | (48, 0) | 48x48 | €35 — actual nutrition product |
| Space Cake Mix | (96, 0) | 48x48 | €20 — "Just add... nothing illegal" |
| CBD Oil 5% | (144, 0) | 32x48 | €30 — "Check your local laws" |
| CBD Oil 15% | (176, 0) | 32x48 | €55 — "Seriously, check them" |
| CBD Skincare Jar | (208, 0) | 32x48 | Zone 1, no THC claims, entirely uncomplicated |
| Souvenir Seed Pack | (240, 0) | 48x48 | €40 — HIGH export risk, *not for germination |
| Premium Strain Seeds | (288, 0) | 48x48 | €65 — VERY HIGH export risk, *definitely not for germination |
| Hemp Rope Coil | (336, 0) | 48x48 | Cannabis-free cannabis plant, sold by the metre |
| Leaf Novelty Set | (384, 0) | 48x48 | €10-30 — declaring your tourist status in advance |
| Hemp Clothing (Folded) | (432, 0) | 48x48 | Zone 1, fibre only, no cannabinoids, genuinely fine |
| Reserve | (480, 0) | 32x48 | Reserved cell, do not paint |

### Small Products & Packaging:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| CBD Gummies | (0, 48) | 32x32 | €25 — "Some countries are weird about gummies" |
| "Tobacco" Grinder | (32, 48) | 32x32 | €20 — for tobacco. Obviously. |
| "Tobacco" Pipe | (64, 48) | 48x32 | €25 — design-dependent risk |
| Rolling Papers (Branded) | (112, 48) | 32x32 | €8 — paper is legal everywhere |
| Hemp Rope Bracelet | (144, 48) | 32x32 | €12 — definitely fine |
| Hemp Snack Bar | (176, 48) | 32x32 | Zone 2, medium certainty |
| Suspicious Souvenir Tag | (208, 48) | 32x32 | 24x24 art centred in cell — the inventory marker |
| Sealed Shop Bag | (240, 48) | 48x32 | Discreet packaging, offered without comment |
| Receipt with Disclaimer | (288, 48) | 48x32 | The disclaimer is longer than the itemisation |
| Single Seed (Macro) | (336, 48) | 48x32 | Just a seed. Until it isn't. |
| Strain Info Card | (384, 48) | 64x32 | "For educational purposes" |
| Lab Test Certificate | (448, 48) | 64x32 | Yuki's evidence; the cannabinoid content is genuinely documented |

### Documents & The Box:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Product Confusion Matrix (Readable) | (0, 96) | 128x64 | Eight rows, four columns, one "Schrödinger" cell |
| CBD vs THC Infographic | (128, 96) | 128x64 | Attempts to explain the difference; effectiveness limited |
| Collector's Agreement Card | (256, 96) | 96x64 | "By purchasing, you acknowledge these are novelty items." |
| Customs Declaration Form | (352, 96) | 96x64 | Blank, ominous, folded twice |
| Quantum Box (Closed) | (448, 96) | 64x64 | The luggage, unobserved, both states at once |

### Collapse States & Icons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Quantum Box (Open — Legal) | (0, 160) | 64x64 | Wavefunction collapsed favourably; agent uninterested |
| Quantum Box (Open — Illegal) | (64, 160) | 64x64 | Wavefunction collapsed otherwise; agent interested |
| Hemp Tote Icon | (128, 160) | 32x32 | Inventory icon |
| CBD Oil Icon | (160, 160) | 32x32 | Inventory icon |
| Seeds Icon | (192, 160) | 32x32 | Inventory icon |
| Grinder Icon | (224, 160) | 32x32 | Inventory icon |
| Papers Icon | (256, 160) | 32x32 | Inventory icon |
| Gummies Icon | (288, 160) | 32x32 | Inventory icon |
| Suspicious Tag Icon | (320, 160) | 32x32 | Inventory overlay marker |
| Anxiety Status Icon | (352, 160) | 32x32 | Wavy-outline silhouette |
| Calm (CBD) Status Icon | (384, 160) | 32x32 | Level-line silhouette |
| Certainty: High | (416, 160) | 32x32 | Solid filled square glyph |
| Certainty: Medium | (448, 160) | 32x32 | Half-hatched square glyph |
| Certainty: Low / Schrödinger | (480, 160) | 32x32 | Dashed-outline square glyph |

### Display Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shelf Talker Strip | (0, 192) | 128x32 | Zone-edge price/legality talkers |
| Zone Legality Placards | (128, 192) | 128x64 | Four 32x64 placards: Definitely / Probably / Questionably / Schrödinger |
| Seed Packet (Front & Back) | (256, 192) | 128x64 | Two 64x64 faces; the back is entirely disclaimer |
| Museum-Style Strain Chart | (384, 192) | 128x64 | Educational framing for legally-cautious information |
| Reserve Strip | (0, 224) | 128x32 | Reserved padding, do not paint |

### Technical Notes:
- Certainty glyphs are shape-coded (solid / half-hatched / dashed outline) so the legality gradient never depends on green-amber-red alone
- Quantum Box closed/legal/illegal share one silhouette and one anchor for a clean three-state crossfade
- The Collector's Agreement Card and Customs Declaration Form are readable props flagged for the ASTC 4x4 exception list
- Seed sprites are deliberately mundane — the comedy is entirely in the surrounding signage, never in the product art

---

## 🧑‍💼 Sprite Sheet 4: Daan & Yuki
**File:** `npc_daan_yuki.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 per character frame; 128x128 per portrait
**Color Palette:** #228B22 staff shirts, #FAFAF5, #808080

### Manager Daan — Qualification Specialist:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Daan Idle | (0, 0) | 64x96 | 30s Dutch, professional casual, hemp shirt (of course), reassuring |
| Daan Welcome Gesture | (64, 0) | 64x96 | "Everything here is legal in Shamsterdam." |
| Daan Explaining Frame 1 | (128, 0) | 64x96 | Open palms, information beginning |
| Daan Explaining Frame 2 | (192, 0) | 64x96 | One qualifier introduced |
| Daan Explaining Frame 3 | (256, 0) | 64x96 | Three more qualifiers introduced |
| Daan Destination Query | (320, 0) | 64x96 | "Where are you travelling to?" — the pivot |
| Daan Careful Hedge | (384, 0) | 64x96 | The Daan Method: maximum information, minimum responsibility |
| Daan "I cannot answer that question." | (448, 0) | 64x96 | Delivered warmly. Delivered finally. |

### Daan — Transaction & Philosophy:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Daan Seed Disclaimer Recital | (0, 96) | 64x96 | Word-perfect, seven hundredth time this month |
| Daan Schrödinger Philosophy | (64, 96) | 64x96 | "Until observed, everything is fine." |
| Daan Pointing at Zone Signs | (128, 96) | 64x96 | Directional; the signs do the liability work |
| Daan Ringing Up Sale | (192, 96) | 64x96 | Transaction completes. Everyone understood. |
| Daan Sealing the Bag | (256, 96) | 64x96 | Discreet packaging, no comment |
| Yuki Idle | (320, 96) | 64x96 | 20s Dutch-Japanese, knowledgeable, patient |
| Yuki Demonstrating Frame 1 | (384, 96) | 64x96 | Product raised, label forward |
| Yuki Demonstrating Frame 2 | (448, 96) | 64x96 | Label indicated, lab figure cited |

### Portraits & Extras:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Daan Portrait (Dialogue) | (0, 192) | 128x128 | Friendly, informative, carefully non-liable |
| Yuki Portrait (Dialogue) | (128, 192) | 128x128 | Genuinely trying to inform, within limits |
| Quantum Cat Portrait | (256, 192) | 128x128 | Mascot speaker frame for the shop's philosophy lines |
| Yuki Lab-Test Explanation | (384, 192) | 64x96 | "Lab-tested, certified CBD content." |
| Yuki Gentle Reality Check | (448, 192) | 64x96 | "Outside the shop, different rules may apply." |
| Reserve / Atlas Padding | (384, 288) | 128x32 | Reserved strip, do not paint |

### Associate Yuki — Education:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Yuki Cannabinoid Diagram Gesture | (0, 320) | 64x96 | "CBD is non-psychoactive. THC is what gets you high." |
| Yuki Handing Product | (64, 320) | 64x96 | Two-handed, Dutch-Japanese hybrid courtesy |
| Yuki "It's just hemp fibre" | (128, 320) | 64x96 | "That one's actually simple." |
| Yuki Seeds Explanation | (192, 320) | 64x96 | "They're just seeds. Until they're not just seeds anymore." |
| Daan High-Contrast Silhouette | (256, 320) | 64x96 | Accessibility outline variant |
| Yuki High-Contrast Silhouette | (320, 320) | 64x96 | Accessibility outline variant |
| Daan Reassuring Shrug | (384, 320) | 64x96 | "I'm not saying don't buy it." |
| Daan Hemp Shirt Detail Frame | (448, 320) | 64x96 | Close crop; the shirt is the uniform and the joke |

### Counter & Utility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Staff Counter Pose (Daan) | (0, 416) | 64x96 | Behind-register anchor pose |
| Staff Counter Pose (Yuki) | (64, 416) | 64x96 | Floor-station anchor pose |
| Daan Customs Warning | (128, 416) | 64x96 | "I can't predict customs." |
| Yuki Dosage Question Answer | (192, 416) | 64x96 | For the CBD Wellness Convert branch |
| Accessibility Reserve Block | (256, 416) | 256x96 | Reserved for high-contrast/audio-cue glyph overflow |

### Technical Notes:
- Daan's three Explaining frames escalate qualifier density visibly through hand position; the animation is the joke, not the dialogue
- Daan and Yuki never appear worried, evasive, or shifty in any frame — the entire satire collapses if the staff read as dishonest. They are being scrupulously truthful and it is not helping.
- Quantum Cat Portrait is used for the shop's philosophy lines so the mascot can say what the staff legally cannot

---

## 👥 Sprite Sheet 5: Customers & Customs
**File:** `npc_schrodingers_customers.png`
**Dimensions:** 1024x256 pixels
**Sprite Size:** 64x96 per single NPC frame; 128x128 per portrait
**Color Palette:** Mixed tourist palette, retail-white ambient grade

### Shoppers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Research Tourist | (0, 0) | 64x96 | Actually checking destination law, responsible, rare |
| Research Tourist (Phone Up) | (64, 0) | 64x96 | Cross-referencing regulations mid-aisle |
| "It's All Legal" Tourist | (128, 0) | 64x96 | Read nothing, worried about nothing |
| "It's All Legal" Tourist (Arms Full) | (192, 0) | 64x96 | Loading up on everything |
| Seed Collector (Wink) | (256, 0) | 64x96 | Obvious gardening energy, "just curious" |
| Coffeeshop Overflow | (320, 0) | 64x96 | Looking for the smoking area |
| Coffeeshop Overflow (Realising) | (384, 0) | 64x96 | "Wait, this is just... souvenirs?" |
| CBD Wellness Convert | (448, 0) | 64x96 | Reading labels carefully, legitimate interest |
| Anxious Purchaser | (512, 0) | 64x96 | Wants seeds, terrified of consequences |
| Anxious Purchaser (Buying Anyway) | (576, 0) | 64x96 | The internal conflict, resolved |
| Bros Trio Browsing | (640, 0) | 192x96 | Lord Pilsner / Chadwick / Bradley, pre-composed |
| Browsing Filler A | (832, 0) | 64x96 | Ambient shopper |
| Browsing Filler B | (896, 0) | 64x96 | Ambient shopper variant |
| Queue Filler | (960, 0) | 64x96 | Checkout line body |

### Portraits & Strips:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Research Tourist Portrait | (0, 96) | 128x128 | "Sinfonia allows CBD under 0.2%... Publandia is stricter..." |
| All-Legal Tourist Portrait | (128, 96) | 128x128 | "It's Shamsterdam! It's all legal here! It's FINE!" |
| Seed Collector Portrait | (256, 96) | 128x128 | "Just for my collection. Of knowledge. About autoflowering." |
| Anxious Purchaser Portrait | (384, 96) | 128x128 | "And you're SURE it's legal to BUY? Just not to... but it's SEALED..." |
| Coffeeshop Overflow Portrait | (512, 96) | 128x128 | Slow-motion realisation, in one face |
| Browsing Poses Strip | (640, 96) | 256x96 | Four 64x96 stages: enter / consider / read label / put back |
| Decision Paralysis Strip | (896, 96) | 128x96 | Two 64x96 stages: reaching / not reaching |

### Customs & Ambient:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Customs Agent | (640, 192) | 64x64 | Torso-up frame for the checkpoint table |
| Customs Agent (Opening Bag) | (704, 192) | 64x64 | The observation. The collapse. |
| Traveller at Checkpoint | (768, 192) | 64x64 | Player-side anchor frame |
| Shelf-Browsing Silhouette Row | (832, 192) | 128x64 | Cheap crowd depth along zone shelving |
| Accessibility Reserve | (960, 192) | 64x64 | Reserved for high-contrast marker |
| Portrait Band Padding | (0, 224) | 640x32 | Reserved padding, do not paint |

### Technical Notes:
- Bros Trio ships as a pre-composed single block to protect the 14-draw-call budget
- Browsing Poses Strip is palette-modulated onto any shopper; never author per-NPC browse art
- The Customs Agent is deliberately neutral in every frame — bored, procedural, not menacing. The dread is entirely the player's own contribution.

---

## ✨ Sprite Sheet 6: Effects — Superposition & Collapse
**File:** `schrodingers_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #6A4C93, #228B22, #FFD700, #FF0000

### Quantum & Retail:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wavefunction Collapse Frame 1 | (0, 0) | 64x64 | Blur of both states |
| Wavefunction Collapse Frame 2 | (64, 0) | 64x64 | Separation begins |
| Wavefunction Collapse Frame 3 | (128, 0) | 64x64 | One state resolves, the other vanishes |
| Superposition Shimmer | (192, 0) | 64x64 | Persistent legal/illegal blend overlay for tagged items |
| Quantum Cat Blink | (256, 0) | 64x64 | Mascot idle tic, two-frame |
| Legality Uncertainty Haze | (320, 0) | 64x64 | Soft violet fringe on Zone 3-4 products |
| Retail Lighting Bloom | (384, 0) | 64x64 | Clean track-light highlight; nothing sketchy |
| Hemp Leaf Motif Drift | (448, 0) | 64x64 | Subtle decorative motif, professional not psychedelic |

### Transaction & Consequence:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Disclaimer Document Sheen | (0, 64) | 64x64 | Legal-document energy sweep during the seed ritual |
| Seal Tape Application | (64, 64) | 64x64 | Discreet packaging, sealed, one-shot |
| Bag Rustle Frame 1 | (128, 64) | 64x64 | Packaging motion |
| Bag Rustle Frame 2 | (192, 64) | 64x64 | Packaging motion variant |
| Register Glow | (256, 64) | 64x64 | Transaction confirm highlight |
| Anxiety Sweat Drop | (320, 64) | 64x64 | Character-parented, for the Anxious Purchaser and the player |
| Calm Aura (CBD) | (384, 64) | 64x64 | Level, steady, slightly gold |
| Customs Scanner Sweep | (448, 64) | 64x64 | Horizontal sweep bar over the Quantum Box |

### Grades & Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Green Window Wash | (0, 128) | 128x128 | Front-of-shop daylight through green glazing |
| Education Corner Highlight | (128, 128) | 64x64 | Gentle attractor glow, almost never followed |
| Seed Section Hush Grade | (192, 128) | 64x64 | Cool violet grade that intensifies on approach |
| Asterisk Flicker | (256, 128) | 64x64 | The asterisk pulses once when examined. It still leads nowhere. |
| Suspicious Tag Pulse | (320, 128) | 64x64 | Inventory-item marker pulse |
| Customs Pass Glyph | (384, 128) | 32x32 | Visual mirror of the pass chime |
| Customs Fail Glyph | (416, 128) | 32x32 | Visual mirror of the fail sting |
| Disclaimer Sound Glyph | (448, 128) | 32x32 | Visual mirror of the legal-document energy cue |
| Register Beep Glyph | (480, 128) | 32x32 | Visual mirror of the register |
| Bag Rustle Glyph | (128, 192) | 32x32 | Visual mirror of packaging sound |
| Question Asked Glyph | (160, 192) | 32x32 | Visual mirror of the customer question cue |
| Qualified Answer Glyph | (192, 192) | 32x32 | Visual mirror of the staff hedge cue |
| Uncertainty Sting Glyph | (224, 192) | 32x32 | Visual mirror of the seed-purchase sting |
| Chill Ambient Glyph | (256, 192) | 32x32 | Persistent ambient-music indicator |
| Static Superposition (Reduced Motion) | (288, 192) | 64x64 | Non-shimmering blend plate |
| Static Cat (Reduced Motion) | (352, 192) | 64x64 | Non-blinking mascot |
| Instant Collapse Plate | (416, 192) | 64x64 | Reduced-motion replacement for the 3-frame collapse |
| Reserve | (480, 192) | 32x64 | Reserved cell, do not paint |

### Technical Notes:
- Superposition Shimmer parents to individual inventory items in the bag UI; it never renders as a screen-space effect
- The wavefunction collapse is the only high-energy effect in an otherwise deliberately calm retail environment — its impact depends on that contrast
- Asterisk Flicker fires exactly once per examine, then never again in that session; repeating it would over-sell the joke

---

## 🧭 Sprite Sheet 7: UI Elements
**File:** `schrodingers_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #228B22 UI chrome, #808080 panel fill, #FF0000 risk, #6A4C93 quantum

### Legality Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Legality Indicator Panel | (0, 0) | 128x64 | NL legal / export / import status for the selected product |
| Product Legal Status Card | (128, 0) | 128x64 | Per-item detail card with all three jurisdictions |
| Destination Query Panel | (256, 0) | 192x96 | "Where are you travelling to?" — sets all downstream risk values |
| Certainty Meter | (448, 0) | 64x128 | Vertical: High / Medium / Low / Schrödinger, shape-coded segments |
| Product Confusion Matrix UI | (0, 64) | 256x128 | Interactive version of the poster; eight rows, four columns |
| CBD/THC Explainer UI | (0, 192) | 256x96 | The education graphic, optional, rarely opened |

### The Seed Ritual:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Seed Purchase Ritual Panel | (256, 96) | 192x192 | Seven-step disclaimer sequence with the four customer response options |
| Collector Agreement Checkbox | (448, 128) | 64x160 | The acknowledgment column; everyone ticks it; everyone knows |

### Customs & Consequence:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Customs Encounter UI | (0, 288) | 256x192 | Inventory scan panel with per-item pass probability |
| Wavefunction Collapse Result | (256, 288) | 128x96 | Observed / Unobserved outcome frame |
| Suspicious Inventory Indicator | (384, 288) | 128x32 | Tagged-item strip for the bag view |
| Anxiety Status Bar | (384, 320) | 128x32 | Travel-segment anxiety duration |
| Calm Status Bar | (384, 352) | 128x32 | CBD calm duration, minor -Bravado note |

### Achievements & Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Achievement Badges Strip | (256, 384) | 256x64 | Four 64x64 badges: Lawyer / Experimenter / Collector / Unobserved |
| "Observed" Badge (Large) | (256, 448) | 64x64 | Schrödinger had a bad day |
| Export Risk Chips | (384, 384) | 128x32 | Four 32x32 chips: None / Low / Medium / High, shape-coded |
| High-Contrast Counter Marker | (320, 448) | 96x64 | Bold outline for the checkout and seed-cabinet interaction points |
| Zone Silhouette Set | (416, 448) | 96x64 | Four zones as stepped silhouettes with text labels |
| Touch-Zone Guide Overlay | (0, 480) | 256x32 | Dev-only 44px minimum overlay, stripped at build |

### Technical Notes:
- Certainty Meter and Export Risk Chips are shape-coded (solid / half-hatched / dashed / cross-hatched) with text labels — legality is the location's core information and can never be colour-only
- Every seed ritual response option renders at 44px+ touch height; the Collector Agreement checkbox is a 44x44 target inside its 64px column
- The Customs Encounter UI shows explicit numeric pass probabilities per item (100% / 85% / 90% / 60% / 50%); the seeds' 50% is the only coin-flip in the panel and must be visually isolated
- Achievement badges ship full-colour and are grayscale-modulated until earned

---

## 🎬 Animation Specifications

### The "Is This Legal?" Loop (Sheets 4, 6, 7):
- **Duration:** 5.0 seconds (1.0s NL status, 1.0s destination query, 1.5s hedge, 1.0s deflection, 0.5s purchase anyway)
- **Frames:** 3 Daan Explaining frames + Destination Query + Careful Hedge + register glow
- **Pattern:** Play once per product legality inquiry; identical structure every time, which is the joke
- **Trigger:** Player asks about any product's legality
- **Purpose:** Maximum information, minimum responsibility, delivered with total sincerity
- **Audio Sync:** Question glyph at 0.0s; qualified-answer cue at 1.0s and 2.0s; deflection at 3.5s; register beep at 5.0s
- **Mobile Optimization:** Medium LOD reduces Explaining to 2 frames; Low LOD holds a single frame and runs the dialogue text at full length

### The Seed Purchase Ritual (Sheets 3, 4, 6, 7):
- **Duration:** 6.0 seconds (7 steps auto-advancing at ~0.85s each)
- **Frames:** Daan Seed Disclaimer Recital + disclaimer document sheen + checkbox tick + seal tape
- **Pattern:** One-shot ceremony per seed purchase
- **Trigger:** Any seed pack added to cart
- **Purpose:** The polite fiction, performed in full, by both parties, without irony being acknowledged
- **Audio Sync:** Legal-document energy cue rises 0.0-4.0s; checkbox tick at 4.2s; seal tape at 5.4s; a single quiet uncertainty sting at 6.0s
- **Mobile Optimization:** None needed (UI-driven); the sheen is a single alpha sweep

### Quantum Cat Idle (Sheets 2, 6):
- **Duration:** 4.0 seconds per cycle
- **Frames:** 2 (superposition + blink)
- **Pattern:** Blink once per cycle at a randomised offset; the cat never fully resolves while in the shop
- **Trigger:** Constant, on the storefront sign and the mascot standee
- **Purpose:** The mascot is the only thing in the shop allowed to be openly ambiguous
- **Audio Sync:** None
- **Mobile Optimization:** Low LOD uses the static cat plate; disabled in reduced-motion mode

### Wavefunction Collapse (Sheets 3, 5, 6, 7):
- **Duration:** 2.6 seconds (0.8s scanner sweep, 0.6s collapse frames, 1.2s result hold)
- **Frames:** Scanner sweep + 3 collapse frames + Quantum Box open state (legal or illegal)
- **Pattern:** One-shot per customs checkpoint per tagged item category
- **Trigger:** Arriving at the Customs Checkpoint with any Suspicious Souvenir tagged item
- **Purpose:** The observation that determines everything, resolved in six tenths of a second
- **Audio Sync:** Scanner hum 0.0-0.8s; total silence 0.8-1.4s (comedy-critical); pass chime or fail sting at 1.4s
- **Mobile Optimization:** Low LOD replaces the 3 collapse frames with the Instant Collapse Plate; scanner sweep retained

### Suspicious Souvenir Tagging (Sheets 3, 6, 7):
- **Duration:** 1.0s application, then a 2.4s shimmer loop for as long as the item is held
- **Frames:** Tag pulse + superposition shimmer (2-frame)
- **Pattern:** Apply → persistent shimmer loop → resolve at customs
- **Trigger:** Any item with Medium or higher export risk entering inventory
- **Purpose:** The weight is not physical, but it must be visible in the bag
- **Audio Sync:** Soft single tone on application; no loop audio
- **Mobile Optimization:** Shimmer holds on frame 1 on Low LOD and in reduced-motion mode

### The Asterisk Examine (Sheets 2, 6):
- **Duration:** 1.2 seconds
- **Frames:** Asterisk flicker, one-shot
- **Pattern:** Fires exactly once per session on first examine of any asterisked sign
- **Trigger:** Examining "All products comply with Dutch law*"
- **Purpose:** The asterisk leads nowhere. The game confirms this with a single flicker and no footnote.
- **Audio Sync:** One soft click, then nothing
- **Mobile Optimization:** None needed

### Zone Grade Transition (Sheets 1, 6):
- **Duration:** 0.6 seconds per zone crossing
- **Frames:** Alpha crossfade between zone grade overlays
- **Pattern:** Continuous, driven by player X position front-to-back
- **Trigger:** Walking deeper into the shop
- **Purpose:** The room gets 8% cooler and 8% quieter per zone; nobody mentions it
- **Audio Sync:** Ambient music low-pass increases 4% per zone
- **Mobile Optimization:** Medium LOD steps the grade in two stages instead of four; Low LOD applies the Zone 1 grade globally

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| High-Contrast Counter Marker | Sheet 7 (320, 448) | 96x64 | Bold outline for the checkout and seed-cabinet interaction points |
| Zone Silhouette Set | Sheet 7 (416, 448) | 96x64 | Four zones as bold stepped silhouettes with text labels |
| Daan High-Contrast Silhouette | Sheet 4 (256, 320) | 64x96 | Enhanced-visibility outline of the primary interaction NPC |
| Yuki High-Contrast Silhouette | Sheet 4 (320, 320) | 64x96 | Enhanced-visibility outline of the secondary interaction NPC |
| Accessibility Reserve Block | Sheet 4 (256, 416) | 256x96 | Overflow space for additional high-contrast variants |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Superposition | Sheet 6 (288, 192) | 64x64 | Non-shimmering legal/illegal blend plate |
| Static Cat | Sheet 6 (352, 192) | 64x64 | Non-blinking mascot for sign and standee |
| Instant Collapse Plate | Sheet 6 (416, 192) | 64x64 | Replaces the 3-frame collapse with an immediate result state |
| Flat Zone Grade | Sheet 6 (0, 128) | 128x128 | Reduced-motion applies one uniform grade with no crossfade |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Customs Pass Glyph | Sheet 6 (384, 128) | 32x32 | Mirrors the pass chime |
| Customs Fail Glyph | Sheet 6 (416, 128) | 32x32 | Mirrors the fail sting |
| Disclaimer Sound Glyph | Sheet 6 (448, 128) | 32x32 | Mirrors the legal-document energy cue during the seed ritual |
| Register Beep Glyph | Sheet 6 (480, 128) | 32x32 | Mirrors the transaction confirm |
| Bag Rustle Glyph | Sheet 6 (128, 192) | 32x32 | Mirrors packaging sound |
| Question Asked Glyph | Sheet 6 (160, 192) | 32x32 | Mirrors the customer-question cue |
| Qualified Answer Glyph | Sheet 6 (192, 192) | 32x32 | Mirrors the staff hedge cue |
| Uncertainty Sting Glyph | Sheet 6 (224, 192) | 32x32 | Mirrors the seed-purchase sting |
| Chill Ambient Glyph | Sheet 6 (256, 192) | 32x32 | Persistent ambient-music indicator |

### Colorblind Considerations:
- Legality certainty is shape-coded: solid square (High), half-hatched (Medium), dashed outline (Low/Schrödinger) — never green/amber/red alone
- Export Risk Chips use four distinct fill patterns plus text: None / Low / Medium / High
- The four zones are distinguished by shelving silhouette and placard text as well as by the lighting grade, so the front-to-back gradient survives any colour vision profile
- Quantum Box collapse states differ by lid angle and content arrangement, not only by tint
- Status effects use distinct silhouettes: wavy outline (Anxiety), level line (Calm), dashed square (Suspicious Souvenir)
- Touch zones minimum 44px for all product selections, the seed ritual responses, the Collector Agreement checkbox, and the customs interaction

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (fallback PVRTC 4BPP); all signage, the Confusion Matrix, the CBD/THC infographic, the Collector Agreement, the Customs Declaration Form, and all portraits at ASTC 4x4 (this location's comedy is text-dependent)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for `schrodingers_interior_main.png` (the zone lighting gradient bands badly under lossy compression)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| schrodingers_environment | schrodingers_exterior_zones | 1024x1024 |
| schrodingers_characters | npc_daan_yuki, npc_schrodingers_customers | 1024x1024 |
| schrodingers_fx_ui | schrodingers_products, schrodingers_effects, schrodingers_ui | 1024x1024 |

*(schrodingers_interior_main.png loads standalone as a scene background; max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Four-stage zone grade crossfade, cat blink, item superposition shimmer, full 3-frame collapse, scanner sweep, asterisk flicker |
| Medium | Two-stage zone grade, cat blink retained, shimmer at half rate, collapse retained |
| Low | Single global grade (profile requirement: simplified product displays, static education graphics), static cat, static shimmer, Instant Collapse Plate |

### Performance Targets:
- **Target FPS:** 45 (per location performance budget)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 32 MB maximum
- **Particle Limit:** 10 (leaf motif drift, anxiety droplets, collapse motes)

### Performance Notes:
- Each of the four zones renders as one composed shelving block — four draw calls covers the entire retail floor
- Bros Trio ships pre-composed; maximum 4 individually animated NPCs on screen
- The Customs Checkpoint is a separate lightweight scene reusing this location's product, effect, and UI atlases; nothing new streams in for it
- Superposition shimmer is limited to visible bag-UI slots only — never applied to inventory items off-screen

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (interior background, zone blocks, fixtures), AnimatedSprite2D (Daan, Yuki, quantum cat, collapse), CPUParticles2D (leaf drift, collapse motes — not GPU), CanvasLayer (legality UI, seed ritual, customs panel), Area2D (four zone triggers, education corner, checkout, seed cabinet)
- Special systems: destination-country variable set at first Daan interaction and persisted globally, per-product three-jurisdiction legality lookup table, Suspicious Souvenir inventory tag with export-risk weighting, seven-step Seed Purchase Ritual state machine with acknowledgment gate, Customs Checkpoint probability roll per tagged item category, zone-grade shader parameter driven by player X position, Schrödinger achievement track flags

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Daan Explaining frames | Qualified-answer cue, one per qualifier | 1.0s / 2.0s of the legality loop |
| Daan deflection frame | "Research is key" line | 3.5s of the legality loop |
| Disclaimer document sheen | Rising legal-document energy | 0.0-4.0s of the seed ritual |
| Collector Agreement tick | Single soft click | 4.2s of the seed ritual |
| Seal tape application | Tape pull | 5.4s of the seed ritual |
| Seed ritual completion | Quiet uncertainty sting | 6.0s |
| Register glow | Register beep | On transaction commit |
| Customs scanner sweep | Scanner hum | 0.0-0.8s of the collapse |
| Collapse frames 1-3 | Silence (deliberate) | 0.8-1.4s |
| Quantum Box result state | Pass chime or fail sting | 1.4s |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Schrödinger Achievement Track | Badges strip, Observed badge, Suspicious tag, Quantum Box states | Lawyer / Experimenter / Collector / Unobserved / Observed, resolved at the checkpoint |
| The Seed Purchase Ritual | Ritual panel, Daan Disclaimer Recital, agreement checkbox, seed packet front/back | Seven steps; the fiction is completed by both parties in full |
| The Customs Encounter | Customs Checkpoint fixture, agent frames, scanner sweep, collapse frames, encounter UI | Per-item probability roll; seeds are the only 50/50 in the game's inventory |
| "Is This Legal?" (Repeatable) | Legality panel, status card, certainty meter, Daan Explaining frames | Repeatable per product; the destination country set here changes every downstream risk value |
| Cultural Alibi (shared) | Sealed shop bag, receipt with disclaimer | The bag is not a museum bag; different NPCs read it differently |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| De Groene Gids | "THIS IS NOT A COFFEESHOP" sign; Coffeeshop Overflow NPC pair | The Overflow customer walks in from the Groene Gids corridor; the sign is the visual punchline of that walk |
| The Hemp Museum | CBD/THC infographic and Museum-Style Strain Chart share visual language | Educational counterpart; museum gift-shop bag and this shop's sealed bag are deliberately distinguishable |
| De Botanische Leugen | Shared "customs will be interesting" energy; Suspicious Souvenir tag | Tagged items from both locations aggregate into one customs roll |
| The Tolerance Hostel | Sealed shop bag visible in dorm/kitchen scenes | Kitchen gossip may reference "the quantum cat place"; bag persists as a prop |
| Airport / Customs (resolution node) | Customs Checkpoint fixture, agent frames, Quantum Box states | The observation event; wavefunction collapses, epilogue text is written from the result |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A spotless, well-lit, entirely legitimate shop where the lighting gets four degrees cooler with every step toward the back"
- **Color Mood:** Hemp green and retail white with CBD gold accents, cooling into legal gray and superposition violet at the rear — professional, calm, faintly clinical
- **Lighting:** Even commercial track lighting front-of-house, stepping down in brightness and warmth per zone; the seed cabinet is the only cool-lit fixture in the building
- **Texture:** Clean vinyl floor, brushed shelving, glossy laminated signage, matte disclaimer paper, glass cabinet with a very small brass lock

### Environmental Storytelling:
- The shop is arranged as a gradient, not a floorplan: legality decreases with depth and nobody has ever said so out loud
- Every instance of the word "legal" on the premises carries an asterisk, and no asterisk anywhere has a footnote
- The education corner is beautifully made, prominently placed, and shows no wear whatsoever
- The "NOT FOR GERMINATION" signs are placed at four sizes in four positions, which means someone thought hard about coverage
- The disclaimer board is mounted directly above the register — maximum visibility, minimum readership, total liability coverage

### Character Integration Notes:
- Daan and Yuki must never read as evasive; they are the most honest people in the location and it is making everything worse
- Daan's frames escalate in hand-gesture complexity as qualifier count rises — the physicality carries the joke past the dialogue
- The Quantum Cat is the only character permitted to state the shop's philosophy plainly, because it is a mascot and mascots are not legally liable
- The Customs Agent is procedural and bored in every frame; all tension originates from the player's inventory, not the agent's performance

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Quantum Cat in Superposition** — both states at once, hemp leaf accessory, unresolvable
2. **The Asterisk That Leads Nowhere** — examined, flickers once, has no footnote, never will
3. **The Zone Gradient** — one screenshot of the shop from the door, lighting cooling by degrees toward the seed cabinet
4. **The Seed Ritual in Progress** — seven steps of disclaimer with a checkbox everyone ticks
5. **The Wavefunction Collapse** — scanner sweep, six tenths of a second of silence, one of two outcomes

### Quote Potential:
- "Schrödinger's cat was both alive and dead until observed. Your souvenir is both legal and illegal until customs observes it. That's the shop's philosophy."
- "I'm not saying don't buy it. I'm saying know what you're buying. Then buy it. Probably."
- "I can tell you what's in it. I can't tell you what your country thinks of what's in it."
- "They're just seeds. Until they're not just seeds anymore."
- "These are collector's items. Everyone knows what they are. Everyone pretends otherwise. It's a social contract."
- "Your country's laws are your responsibility. Good luck."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | schrodingers_interior_main.png | 1920x1080 |
| 2 | schrodingers_exterior_zones.png | 1024x1024 |
| 3 | schrodingers_products.png | 512x256 |
| 4 | npc_daan_yuki.png | 512x512 |
| 5 | npc_schrodingers_customers.png | 1024x256 |
| 6 | schrodingers_effects.png | 512x256 |
| 7 | schrodingers_ui.png | 512x512 |

**Total Estimated Memory:** ~16.7 MB in-memory (uncompressed RGBA worst case), within the 32 MB location budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `schrodingers_interior_main.png` (1920x1080)
- [ ] `schrodingers_exterior_zones.png` (1024x1024)
- [ ] `schrodingers_products.png` (512x256)
- [ ] `npc_daan_yuki.png` (512x512)
- [ ] `npc_schrodingers_customers.png` (1024x256)
- [ ] `schrodingers_effects.png` (512x256)
- [ ] `schrodingers_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + zone lighting gradient reference (brightness/warmth values per zone) + full signage copy sheet for localisation

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (#228B22, #FFD700, #808080, #FF0000, #FAFAF5, #6A4C93)
- [ ] Key gags read clearly: the four-zone lighting gradient legible in a single wide shot, the footnote-less asterisk, four sizes of "NOT FOR GERMINATION," the pristine unused education corner, the Quantum Cat that never resolves
- [ ] All signage text is legible at gameplay zoom on a 5-inch display
- [ ] Accessibility visual alternatives included for all audio cues (pass, fail, disclaimer, register, bag rustle, question, qualified answer, uncertainty sting, chill ambient)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (the target is legal confusion and willful tourist ignorance, never drug use or Dutch policy)
- [ ] Staff read as scrupulously honest in every single frame — no shifty poses, no knowing smirks
- [ ] Hidden areas/interactions have discoverable visual cues (seed cabinet cool grade, asterisk examine, education corner highlight)
- [ ] Mobile performance optimized (CPU particles, atlas limits respected, zone blocks composed, static-grade fallback)
- [ ] Touch zone sizing considered (44px minimum for products, ritual responses, and the agreement checkbox)
- [ ] Colorblind-friendly alternatives available where color codes meaning (shape-coded certainty and risk, zone silhouettes, patterned chips)
- [ ] Social media viral potential maximized in composition choices (cat superposition framing, single-shot zone gradient, collapse staging)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam tourist district; destination countries referenced as Sinfonia and Publandia only |
| Cultural Specificity | ✅ | Dutch tolerance policy meeting international prohibition complexity; the seed-as-souvenir legal fiction is genuinely Dutch |
| Satirical Targets Appropriate | ✅ | Tourist legal ignorance and the elaborate disclaimer dance — not drug use, not Dutch policy, not the staff |
| Seedy Underbelly Present | ✅ | Selling ambiguity at markup, positioned to catch coffeeshop overflow, profiting from confusion it is legally required to reduce |
| Gameplay Value Established | ✅ | Four-zone browsing, legality inquiry loop, seven-step seed ritual, Suspicious Souvenir tagging, customs probability event, 5-badge track |
| Technical Feasibility | ✅ | Composed zone blocks, static-display and static-graphic fallbacks per profile, shared atlases with the checkpoint scene |
| Mobile Performance Budget | ✅ | 45 FPS, 14 draw calls, 32 MB, 10 particles per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all nine audio cues, reduced-motion set including instant collapse, shape-coded legality, 44px touch zones |
| No Crypto Elements | ✅ | Pure quantum legal uncertainty; the only speculative asset is a seed |
| Social Media Integration | ✅ | 5 screenshot moments + 6 quotable lines identified |

**Once these assets ship, Schrödinger's Souvenir becomes the game's most polite trap: a spotless shop where every product is legal, every sign is true, every staff member is honest, the lighting gets colder the deeper you go, and the only thing anyone is uncertain about is you.**
