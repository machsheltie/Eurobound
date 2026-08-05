# Condomerie Het Gulden Vlies - Complete PNG Asset Requirements

## 📋 Overview
Condomerie Het Gulden Vlies ("The Golden Fleece") is a narrow, aggressively respectable boutique on the edge of the Red Light District where protection is merchandised as luxury goods, the staff have been professionally unshockable since 1987, and every bachelor party that walks in immediately regresses to age twelve. This document specifies every PNG asset across the elegant storefront and window display, the five-section boutique interior with its gift-wrapping station and counter, the tastefully abstract product and packaging sprites, Manager Femke and Associate Joost plus the full customer cast, and the Bravado / gag-gift / gift-wrap UI. Its satirical essence in a sentence: the shop is completely professional, the customers are completely not, and the gap between them is the entire joke.

**Location ID:** `shamsterdam_redlight_condomerie_01`
**Theme:** Dutch sexual-health openness vs. tourist awkwardness — the human inability to buy protection without becoming a child, and the markup that awkwardness will happily pay
**Zone:** Edge of the Red Light District, respectable enough for daylight tourist foot traffic
**Hours:** 11 AM - 10 PM (civilized hours for uncivilized purchases)
**Primary Function:** Specialty retail / Bravado challenge / bachelor-party checkpoint — solo-entry Bravado check, five-section product browsing, gag-gift declaration system, gift-wrapping service, group discount and Groom Spotlight, inventory-visibility consequences, five-stage achievement track

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Golden Yellow | #FFD700 | Sign lettering, fleece emblem, premium packaging |
| Deep Red | #8B0000 | Accent shelving, ribbon, "bold" gift wrap |
| Boutique Cream | #FFF8DC | Walls, product backing card, bag stock |
| Professional Black | #1A1A1A | Counter, frames, staff uniform, typography |
| Fleece Gold Shimmer | #E8C466 | Particle shimmer, spotlight falloff, art-piece plinths |
| Red Light Spill | #C43B5A | Neon bleed from the next street over, exterior night wash |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/condomerie_het_gulden_vlies/
├── environment/
│   ├── condomerie_exterior.png
│   └── condomerie_interior.png
├── objects/
│   └── condomerie_products_items.png
├── npcs/
│   └── npc_condomerie_cast.png
└── ui/
    └── condomerie_ui_effects.png
```

---

## 🏆 Sprite Sheet 1: Storefront Exterior & Window Display
**File:** `condomerie_exterior.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #FFD700, #FFF8DC, #1A1A1A, #C43B5A

### Facade & Windows:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Narrow Storefront Facade | (0, 0) | 256x384 | Classic tall-thin Shamsterdam frontage, immaculately maintained |
| Window Display — Day | (256, 0) | 256x192 | Artistic arrangement, more museum vitrine than sex shop |
| Window Display — Evening | (256, 192) | 256x192 | Warm interior light, the whole street's only tasteful glow |
| Red Light District Edge Backdrop (tileable) | (768, 0) | 256x192 | Neighbouring frontages; the respectable end of a disreputable street |
| Storefront Reflection Overlay (glass) | (768, 320) | 256x192 | Passersby reflected in the window they refuse to walk into |

### Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gold Lettering Sign | (512, 0) | 256x64 | "CONDOMERIE HET GULDEN VLIES" in elegant gold |
| "Since 1987 — The Original" Plate | (512, 64) | 256x32 | The credential, stated once, quietly |
| "Protection Is Beautiful" Tagline | (512, 96) | 256x32 | The thesis statement |
| Window Text Decal | (512, 128) | 256x32 | "The World's First Specialty Condom Shop" |
| "Yes, you can just browse…" Small Sign | (512, 160) | 256x32 | "…No, we don't judge. Much." |
| Golden Fleece Emblem | (512, 192) | 128x128 | Jason's quest, rendered with total sincerity |
| Opening Hours Plate | (768, 192) | 128x64 | 11:00 – 22:00 |
| Sandwich Board "Gift Wrapping Available" | (0, 416) | 96x96 | The service nobody expects and everybody uses |

### Entry & Street:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shop Door — Closed | (640, 192) | 64x128 | Brass handle, clean glass |
| Shop Door — Open (warm spill) | (704, 192) | 64x128 | Light and boutique playlist escaping |
| Photograph-From-Outside Marker | (768, 256) | 128x64 | Hotspot for the extremely common non-entry |
| Street Cobble Tile — Clean | (0, 384) | 32x32 | This block gets swept |
| Street Cobble Tile — Wet | (32, 384) | 32x32 | Canal-damp variant |
| Warm Light Spill Decal | (64, 384) | 128x64 | Interior glow pooling on the pavement |
| Red Neon Bleed | (192, 384) | 128x64 | Pink-red wash from one street over |
| Awning / Overhang | (320, 384) | 192x64 | Modest, no branding, deliberate restraint |
| Exterior Interaction Hotspot Ring | (512, 384) | 64x64 | 44px+ entry marker art |
| Bachelor Party Loitering Outside | (576, 384) | 192x64 | Daring each other to go first |
| Bicycle Parked (grime, chained) | (96, 416) | 128x96 | Chained to the drainpipe, as is law |
| Pavement Gum Detail Tile | (224, 416) | 32x32 | Scatter decal |
| Tourist Photographing Storefront | (256, 416) | 64x96 | Will not enter. Never enters. |
| Passerby Pretending Not To Look | (320, 448) | 64x64 | Head forward, eyes sideways |
| Window Display Spotlight Cone | (384, 448) | 128x64 | Museum-grade lighting on the display |
| Exterior Night Wash Overlay | (512, 448) | 256x64 | Evening colour grade for the whole facade |

### Technical Notes:
- The facade must read *respectable* at silhouette distance — the comedy only works if the building looks like a jeweller's
- Red Neon Bleed is an additive layer with a low-amplitude 3-second brightness wobble; it never touches the shop's own signage
- Window Display Day/Evening are swapped by time-of-day state, not cross-faded, to avoid a double-draw during transition
- Gold lettering is text-critical: exclude the sign region from aggressive compression

---

## 🛍️ Sprite Sheet 2: Boutique Interior
**File:** `condomerie_interior.png`
**Dimensions:** 1024x768 pixels
**Color Palette:** #FFF8DC, #1A1A1A, #FFD700, #8B0000

### Shop Body & Product Walls:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Boutique Interior Base (wide) | (0, 0) | 512x384 | Clean lines, good lighting, professional — not a single red bulb |
| Product Wall — Section 1 "The Essentials" | (512, 0) | 256x192 | Standard brands. Tourists rarely stop here. |
| Product Wall — Section 2 "The Sensations" | (768, 0) | 256x192 | Where browsing gets thoughtful |
| Product Wall — Section 3 "The Sizes" | (512, 192) | 256x192 | Comprehensive, sensitively organized |
| Product Wall — Section 4 "The Novelties" | (768, 192) | 256x192 | Tourist magnet; bachelor-party bulk zone |
| Product Wall — Section 5 "The Art Pieces" | (0, 384) | 256x192 | Limited editions under glass; museum gift shop energy |

### Service Areas:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gift Wrapping Station | (256, 384) | 192x192 | Professional service, Discreet / Festive / Bold |
| The Counter | (448, 384) | 256x192 | Where transactions happen and eye contact is optional but noticed |
| Sizing Guide Placard | (704, 384) | 96x64 | Available. Requires asking. |
| Header Plate "The Essentials" | (704, 448) | 96x32 | Section signage |
| Header Plate "The Sensations" | (704, 480) | 96x32 | Section signage |
| Header Plate "The Sizes" | (704, 512) | 96x32 | Section signage |
| Header Plate "The Novelties" | (800, 448) | 96x32 | Section signage |
| Header Plate "The Art Pieces" | (800, 480) | 96x32 | Section signage |
| Museum-Style Plinth | (800, 512) | 96x64 | Art Pieces display base |
| Spotlight Fixture (novelty section) | (896, 384) | 128x64 | The one dramatic light in the room |
| Boutique Ceiling Light Strip | (896, 448) | 128x32 | Even, flattering, clinical-adjacent |
| Floor Tile — Polished | (896, 480) | 32x32 | Base flooring |
| Floor Tile — Scuffed Browse Path | (928, 480) | 32x32 | Wear pattern to Section 4, naturally |
| Baseboard Trim (tileable) | (960, 480) | 64x32 | Wall/floor join |
| Shelving Unit — Empty (restock) | (896, 512) | 128x64 | Joost's ongoing task |

### Fixtures & Atmosphere:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bulk "Bachelor Party" Endcap | (0, 576) | 192x192 | By the counter. Efficiency is key. |
| Gift Card Rack | (192, 576) | 96x128 | "Yes, people use them." |
| Educational Poster Display | (288, 576) | 96x128 | 15 Sovs, conversation starter, Bradley's pick |
| Mirror (customer self-assessment) | (384, 576) | 96x128 | Reflects your face making that face |
| Waiting Bench | (480, 576) | 128x96 | Where "I'm Just Looking" guy has been for 20 minutes |
| Basket Stack | (608, 576) | 96x96 | Optimistic capacity |
| Restock Trolley | (704, 576) | 128x96 | Joost's vehicle |
| Discreet Bag Dispenser | (832, 576) | 96x96 | Plain option, always offered |
| Card Terminal | (928, 576) | 96x96 | Contactless, no drama |
| Golden Shimmer Accent Trim (tileable) | (192, 704) | 192x64 | Fleece motif running the wall line |
| Counter Bell (never used) | (384, 704) | 64x64 | Staff are already looking at you |
| "Exterior Photography Only, Please" Sign | (448, 704) | 128x64 | They have had incidents |
| Nervous-Laughter Zone Decal | (576, 704) | 96x64 | Design overlay marking peak giggle geography (Section 4) |
| Bravado Check Threshold Decal | (672, 704) | 96x64 | Entry check trigger footprint |
| Boutique Speaker | (768, 704) | 64x64 | Deliberately un-sexy playlist source |
| Window-Light Pool (interior) | (832, 704) | 192x64 | Daylight falling across the polished floor |

### Technical Notes:
- Product walls are single composed sprites, not tiled — each section reads as a designed display and swapping one out changes the whole room's tone
- All five section header plates are separate sprites so localisation can replace text without touching the wall art
- The Nervous-Laughter Zone and Bravado Threshold decals ship in the PNG for layout reference and are disabled (visible = false) at runtime
- Interior lighting is baked; only the Spotlight Fixture cone and Window-Light Pool are separate blended layers

---

## 🎁 Sprite Sheet 3: Products, Packaging & Gift Wrap
**File:** `condomerie_products_items.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #FFD700, #8B0000, #FFF8DC, #1A1A1A
**Content Note:** All product sprites are packaging-level abstractions — boxes, sleeves, cards, and silhouettes. No anatomical rendering at any zoom level.

### Product Packages (Row 0, y=0):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Standard Pack (12) | (0, 0) | 64x64 | 15 Sovs — "The responsible choice" |
| Premium Selection | (64, 0) | 64x64 | 25 Sovs — "For the discerning" |
| Glow-in-Dark Pack | (128, 0) | 64x64 | 12 Sovs — party favorite, lights off |
| Glow-in-Dark Pack (glowing) | (192, 0) | 64x64 | Emissive variant; works as advertised |
| Flavored Variety | (256, 0) | 64x64 | 10 Sovs — "Why not" |
| Shamsterdam Souvenir Pack | (320, 0) | 64x64 | 18 Sovs — windmill and tulip motifs, yes really |
| Designer Limited Edition | (384, 0) | 64x64 | 35 Sovs — "Is this a gallery?" |
| The Mystery Box | (448, 0) | 64x64 | 30 Sovs — Chadwick's unboxing content |

### Bundles, Documents & Bags (Row 1, y=64):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bachelor Party Bundle | (0, 64) | 96x96 | 45 Sovs — "The Full Experience" |
| Educational Poster (rolled) | (96, 64) | 48x96 | Inventory form |
| Educational Poster (unrolled) | (144, 64) | 96x96 | Tasteful diagram, hostel-wall ready |
| Gift Card (blank) | (240, 64) | 64x48 | 20 Sovs-100 |
| Gift Card (presented, awkward) | (240, 112) | 64x48 | Held out at arm's length |
| Sizing Guide Booklet | (304, 64) | 64x96 | "Information is power" |
| Shopping Bag — Distinctive | (368, 64) | 64x96 | Gold fleece print; visible from across a hostel kitchen |
| Shopping Bag — Discreet | (432, 64) | 64x96 | Plain kraft; the coward's option, always available |

### Gift Wrapping (Row 2, y=160):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gift Wrap — Discreet | (0, 160) | 64x96 | Plain paper, plain ribbon, plausible deniability |
| Gift Wrap — Festive | (64, 160) | 64x96 | Occasion-appropriate, ambiguous |
| Gift Wrap — Bold | (128, 160) | 64x96 | Everyone at the table will know |
| "Best Man" Ribbon | (192, 160) | 64x32 | Bachelor party option |
| Individual Name Tag Set | (192, 192) | 64x32 | Bulk wrapping, personalised |
| Ribbon Spool | (192, 224) | 64x32 | Deep red, generous |
| Wrapping Paper Roll Rack | (256, 160) | 96x96 | Three stocks, no judgment |
| Wrapping Sequence Frame 1-2 | (352, 160) / (432, 160) | 80x96 each | Fold and tie; a genuinely skilled two-frame loop |

### Displays, Baskets & Tags (Row 3, y=256):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Product Display Riser | (0, 256) | 64x96 | Tiered shelf furniture |
| Category Placard — Essentials | (64, 256) | 96x32 | Shelf-edge label |
| Category Placard — Sensations | (64, 288) | 96x32 | Shelf-edge label |
| Category Placard — Sizes | (64, 320) | 96x32 | Shelf-edge label |
| Category Placard — Novelties | (160, 256) | 96x32 | Shelf-edge label |
| Category Placard — Art Pieces | (160, 288) | 96x32 | Shelf-edge label |
| Price Tag Set (3–50 Sovs) | (160, 320) | 96x32 | Small, honest, no asterisks |
| Basket (customer, filling) | (256, 256) | 96x96 | Two items, growing |
| Basket (overfull, bachelor party) | (352, 256) | 96x96 | Structural integrity in question |
| Receipt (itemized, incriminating) | (448, 256) | 64x96 | Line by line, no euphemisms |

### Counter & Abstract Silhouettes (Row 4, y=352):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Mat | (0, 352) | 96x96 | Where purchases land |
| Cash / Card Tray | (96, 352) | 96x64 | Contactless preferred |
| Card Reader | (96, 416) | 96x32 | Beep, done, move on |
| Novelty Item Silhouette A (abstract) | (192, 352) | 64x96 | Boxed shape, questions implied not answered |
| Novelty Item Silhouette B (abstract) | (256, 352) | 64x96 | Second boxed shape variant |
| Novelty Item Silhouette C (abstract) | (320, 352) | 64x96 | Third boxed shape variant |
| Art Piece Under Glass | (384, 352) | 128x96 | Plinth-mounted, gallery-lit, genuinely handsome |

### Meta & Achievements (Row 5, y=448):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Golden Fleece Shimmer Particle Sheet | (0, 448) | 128x64 | Subtle gold motes, the shop's only "effect" |
| Bag-Visibility Silhouette | (128, 448) | 64x64 | Party-inventory icon for the carried bag |
| Purchase Ratio Tracker Chip | (192, 448) | 128x64 | Secret "gag gift" vs. "personal" tally art (epilogue only) |
| Achievement Tokens (5) | (320, 448) | 160x64 | Protected / Party Supplies / Risk Taker / Brave Soul / Bachelor Party Legend |
| Condomerie Regular Nod Badge | (480, 448) | 32x64 | Earned at 3 visits; other customers notice |

### Technical Notes:
- Every product sprite is packaging-first: the item is inside the box, the box is on screen. This is a hard art rule, not a preference.
- Glow-in-Dark Pack (glowing) uses an emissive-tinted duplicate rather than a shader so it stays cheap and renders identically on all LOD tiers
- Wrapping Sequence frames play at the station during the gift-wrap service; the 2-frame loop is deliberately competent — Femke's staff are good at this
- Achievement token strip is a single 5-cell sprite; individual tokens are addressed by region, not split

---

## 👥 Sprite Sheet 4: Staff & Customer NPCs
**File:** `npc_condomerie_cast.png`
**Dimensions:** 1024x288 pixels
**Sprite Size:** 64x96 pixels (groups noted)

### Staff (Row 0, y=0):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Femke Idle 1-2 | (0, 0) / (64, 0) | 64x96 each | 40s, stylish, entirely unflappable |
| Femke Assisting 1-3 | (128, 0) / (192, 0) / (256, 0) | 64x96 each | Product in hand, information offered, zero performance |
| Femke Explaining 1-2 | (320, 0) / (384, 0) | 64x96 each | "It's protection. It's healthy. It's also, yes, shaped like that." |
| Femke Gift-Wrapping 1-3 | (448, 0) / (512, 0) / (576, 0) | 64x96 each | Fold, ribbon, present — former-nurse hands |
| Femke Unflappable Stare | (640, 0) | 64x96 | "You cannot surprise me. I promise." |
| Joost Idle 1-2 | (704, 0) / (768, 0) | 64x96 each | 20s, art-school adjacent, treats the job as performance |
| Joost Restocking 1-2 | (832, 0) / (896, 0) | 64x96 each | Trolley work, cheerfully |
| Joost Cheerful Frankness | (960, 0) | 64x96 | "I literally cannot be shocked." |

### Staff & Customers (Row 1, y=96):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Joost Sizing-Guide Handoff 1-2 | (0, 96) / (64, 96) | 64x96 each | "Sure. No judgment." |
| Joost Bachelor-Party Processing 1-2 | (128, 96) / (192, 96) | 64x96 each | Bulk mode: efficient, non-judgmental, fast |
| Solo Browser (Serious) 1-2 | (256, 96) / (320, 96) | 64x96 each | Knows what they came for; transaction in 90 seconds |
| Bachelorette Party Frame 1 | (384, 96) | 256x96 | Matching shirts, competitive purchasing |
| Bachelorette Party Frame 2 | (640, 96) | 256x96 | "Get the BIG one! For the HOTEL ROOM! It's TRADITION!" |
| Older Tourist Couple | (896, 96) | 128x96 | Wandered in, genuinely curious, entirely unbothered |

### Customers & Bros (Row 2, y=192):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Older Couple — Thoughtful Question | (0, 192) | 128x96 | "We had three options. This is… comprehensive." |
| "I'm Just Looking" Guy 1-3 | (128, 192) / (192, 192) / (256, 192) | 64x96 each | Twenty minutes, nothing touched, radiating decision paralysis |
| Repeat Customer (Local) 1-2 | (320, 192) / (384, 192) | 64x96 each | Treats it like a pharmacy, because it is one |
| Lord Pilsner Browsing (overwhelmed) | (448, 192) | 64x96 | "There's so MANY. This is… overwhelming. In a good way?" |
| Chadwick Filming Storefront Only | (512, 192) | 64x96 | "The STOREFRONT only. Obviously." |
| Bradley Waiting Outside | (576, 192) | 64x96 | Arms folded, on the pavement, on principle |
| Bradley Dragged In | (640, 192) | 64x96 | "The educational poster is acceptable." |
| Groom Spotlight 1-2 | (704, 192) / (768, 192) | 64x96 each | Turning progressively red as staff ask "Who's the groom?" |
| Nervous Giggle Trio | (832, 192) | 128x96 | Three-figure composition, shoulders shaking, nothing said |
| Staff Silhouette Set (a11y) | (960, 192) | 64x96 | High-contrast interactive-NPC variants |

### Technical Notes:
- Femke and Joost never break professionalism in any frame — no smirks, no raised eyebrows. Every reaction sprite in this location belongs to a customer.
- Max 4 customer NPCs in the shop at once (14 draw-call budget); the Bachelorette Party counts as 2 and locks out one other group
- Groom Spotlight frames use a red-shift shader parameter rather than two full sprite variants, allowing a smooth blush ramp
- "I'm Just Looking" Guy is a fixture — he spawns on first entry and is still there on exit, every visit

---

## 🖥️ Sprite Sheet 5: UI, Effects & Accessibility
**File:** `condomerie_ui_effects.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #FFD700, #FFF8DC, #1A1A1A, #8B0000

### Core UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Product Browser UI (category nav) | (0, 0) | 256x192 | Five-section tabbed browser, abstracted thumbnails |
| Bravado Check Prompt (solo entry) | (256, 0) | 128x64 | The doorway challenge; waived when in a group |
| Purchase Confirmation | (384, 0) | 128x96 | Judgment-free, theoretically |
| Gift Wrap Options | (256, 64) | 128x128 | Discreet / Festive / Bold selector |
| Bachelor Party Discount Chip | (384, 96) | 128x32 | 10% off bulk — "they know what you're here for" |
| Nervous Laughter Indicator | (384, 128) | 128x64 | Customer-state meter, decreases with exposure |
| "Is this a gift?" Dialogue Plate | (0, 192) | 256x64 | Staff ask. Staff don't judge. |
| Gag Gift vs Personal Toggle | (256, 192) | 256x64 | Declaration switch; no gameplay difference, secretly tracked |
| Staff Approach Level Indicator | (0, 256) | 160x64 | Hands-Off / Available / Educational / Bachelor Party Protocol |
| Counter Eye-Contact Meter | (160, 256) | 160x64 | Optional but noticed; feeds Bravado on transaction |
| "What's in the bag?" Party Prompt | (320, 256) | 192x64 | Fires later, from your own party members |
| Inventory Slot — Novelty Purchase | (0, 320) | 64x64 | Occupies real space for the rest of the trip |
| Achievement Track Panel | (64, 320) | 192x96 | Five-stage bachelor-party progression |
| Condomerie Regular Progress | (256, 320) | 128x64 | 3-visit counter toward the staff nod |
| Photography Policy Toast | (384, 320) | 128x64 | "Exterior only, please." |
| Price Tag Popup | (256, 384) | 128x32 | 3–50 Sovs range display |
| Receipt Summary Panel | (384, 384) | 128x32 | Itemized, briefly, then gone |

### Effects & High Contrast:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Golden Shimmer Particle 1-3 | (0, 416) / (48, 416) / (96, 416) | 48x48 each | The fleece theme; subtle, never sparkly |
| Blush Heat Wisp 1-2 | (144, 416) / (192, 416) | 48x48 each | Groom Spotlight and nervous-customer VFX |
| Package Rustle Motion Lines | (240, 416) | 64x48 | Paper handling feedback |
| Register Chime Sparkle | (304, 416) | 64x48 | Transaction complete |
| High-Contrast Counter Outline | (368, 416) | 64x48 | Bold marker for the transaction hotspot |
| High-Contrast Door/Exit Outline | (432, 416) | 80x48 | Entry and exit markers |

### Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Visual Cue: Register Beep | (0, 464) | 32x32 | Transaction audio mirror |
| Visual Cue: Package Rustle | (32, 464) | 32x32 | Handling audio mirror |
| Visual Cue: Boutique Music Bed | (64, 464) | 32x32 | Ambient playlist indicator |
| Visual Cue: Nervous Laughter | (96, 464) | 32x32 | Customer-comedy audio mirror |
| Visual Cue: Street Noise Bleed | (128, 464) | 32x32 | Door-open exterior audio mirror |
| Reduced-Motion Static Shimmer Plate | (160, 464) | 96x48 | Non-animated gold accent substitute |
| Colorblind Category Pattern Swatches (5) | (256, 464) | 160x48 | Section hatching for the five product walls |
| Touch Zone Ring (44px min) | (416, 464) | 64x48 | QA overlay for interactive sizing |

### Technical Notes:
- The Gag Gift toggle is purely cosmetic at runtime — the tracked ratio surfaces only in the epilogue, so the UI must never hint that it matters
- Nervous Laughter Indicator decays across visits: full on visit 1, half on visit 2, absent at Condomerie Regular status
- Blush Heat Wisp doubles as the Groom Spotlight VFX and the solo-entry Bravado-fail effect
- Shimmer particles cap at 8 simultaneous instances; the location's whole particle budget is deliberately tiny

---

## 🎬 Animation Specifications

### Golden Fleece Shimmer (Sheets 3, 5):
- **Duration:** 2.4 seconds per cycle (3 frames at 1.25 FPS), continuous loop
- **Frames:** 3
- **Pattern:** Motes rise and fade along the accent trim and over the Art Pieces plinth
- **Trigger:** Constant while inside the shop
- **Purpose:** The one flourish in an otherwise clinically calm room — it signals "luxury goods," which is the whole satirical premise
- **Audio Sync:** None (the boutique playlist is the only bed)
- **Performance Optimization:** Particle count 8 → 4 on Medium, disabled on Low

### Gift Wrapping Sequence (Sheets 3, 4):
- **Duration:** 3.0 seconds (Femke's 3 frames at 1 FPS, synced to the 2-frame wrap loop at 1.5 FPS), single play
- **Frames:** 3 staff + 2 wrap
- **Pattern:** Fold → ribbon → present, then the wrapped package sprite drops into inventory
- **Trigger:** Player selects Discreet / Festive / Bold at the wrapping station
- **Purpose:** Genuine competence performed on an absurd object — the funniest thing in the shop is how good she is at this
- **Audio Sync:** Paper crease on frame 1, ribbon pull on frame 2, register chime on the inventory drop
- **Performance Optimization:** None needed

### Nervous Laughter (Sheets 4, 5):
- **Duration:** 1.2 seconds (Nervous Giggle Trio held with a 2-frame shoulder shake at 3 FPS), loops 2-3 times
- **Frames:** 2 + indicator meter fill
- **Pattern:** Shake → indicator rises → decays over 6 seconds
- **Trigger:** Entering Section 4 (Novelties) for the first time on any visit; automatic for first-time visitors
- **Purpose:** "The Giggle Response" made a visible, decaying stat rather than a joke told once
- **Audio Sync:** Suppressed-laughter bed under the boutique playlist; subtle comedy note on the indicator peak
- **Performance Optimization:** None needed

### Groom Spotlight Blush (Sheets 4, 5):
- **Duration:** 2.0 seconds ramp (shader red-shift 0 → 1), holds 3 seconds, 1.5 second decay
- **Frames:** 2 sprite frames + Blush Heat Wisp 2-frame loop at 4 FPS
- **Pattern:** Staff asks "Who's the groom?" → ramp → hold → slow decay while everyone looks
- **Trigger:** Bachelor Party flag active (3+ party members) and staff dialogue beat reached
- **Purpose:** The single cruellest, kindest moment in the location — nobody is mocking him, which is worse
- **Audio Sync:** Bachelorette-party "ooooh" from across the shop on the ramp peak
- **Performance Optimization:** Heat wisp cut on Low LOD; the red-shift shader is retained (it is one parameter)

### Staff Approach Shift (Sheets 4, 5):
- **Duration:** 0.8 seconds (2 frames at 2.5 FPS) per level change
- **Frames:** 2 per staff member
- **Pattern:** Idle → step toward customer, held at the new approach level
- **Trigger:** Customer lingers 8+ seconds in one section (Available), asks a question (Educational), or enters with 3+ party members (Bachelor Party Protocol)
- **Purpose:** Non-verbal escalation of service without a single pushy line of dialogue
- **Audio Sync:** Soft footstep on frame 2
- **Performance Optimization:** None needed

### Door Open / Warm Spill (Sheet 1):
- **Duration:** 0.6 seconds (2 sprite states with a 0.6 second light-pool alpha ramp)
- **Frames:** 2 + spill decal
- **Pattern:** Closed → open, spill decal fades in over the pavement, boutique playlist ducks in from outside
- **Trigger:** Player or NPC entry/exit
- **Purpose:** The shop advertising itself honestly — warm light on a red-lit street
- **Audio Sync:** Door chime on frame 2; street noise crossfades with the interior bed
- **Performance Optimization:** Spill decal alpha ramp reduced to an instant swap on Low LOD

### Register / Transaction Complete (Sheets 3, 5):
- **Duration:** 0.5 seconds (chime sparkle 2 frames at 4 FPS), single play
- **Frames:** 2 + receipt drop
- **Pattern:** Card tap → sparkle → receipt panel → bag sprite added to party inventory
- **Trigger:** Any purchase confirm
- **Purpose:** Brief, dignified acknowledgement — the shop refuses to make it a moment
- **Audio Sync:** Terminal beep, then a single warm chime; no fanfare
- **Performance Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Outline | Sheet 5, (368, 416) | 64x48 | Bold marker for the transaction hotspot |
| Door / Exit Outline | Sheet 5, (432, 416) | 80x48 | Entry and exit interaction markers |
| Staff Silhouette Set | Sheet 4, (960, 192) | 64x96 | High-contrast Femke and Joost variants |
| Exterior Interaction Hotspot Ring | Sheet 1, (512, 384) | 64x64 | Bold entry ring, drawn at 112x112 collision |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Reduced-Motion Static Shimmer Plate | Sheet 5, (160, 464) | 96x48 | Replaces the golden mote loop with a still gradient |
| Glow-in-Dark Pack (non-pulsing) | Sheet 3, (192, 0) | 64x64 | Emissive variant held static rather than breathing |
| Blush Ramp Substitution | Sheet 5, (144, 416) | 48x48 | Instant colour set instead of a 2-second ramp; wisp disabled |
| Wrapping Sequence Hold | Sheet 3, (352, 160) | 80x96 | Reduced-motion shows frame 1 then the finished package |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Register Beep | Sheet 5, (0, 464) | 32x32 | Card-terminal confirmation glyph |
| Package Rustle | Sheet 5, (32, 464) | 32x32 | Paper-handling glyph during wrapping and bagging |
| Boutique Music Bed | Sheet 5, (64, 464) | 32x32 | Ambient-playlist presence indicator |
| Nervous Laughter | Sheet 5, (96, 464) | 32x32 | Mirrors the suppressed-laughter comedy bed so deaf players get the gag |
| Street Noise Bleed | Sheet 5, (128, 464) | 32x32 | Fires on every door open, signalling who just walked in |
| Door Chime | Sheet 1, Shop Door — Open | 64x128 | Door sprite flashes a one-frame highlight on the chime |

### Colorblind Considerations:
- The five product sections are distinguished by hatching pattern on their header plates and category placards, not by colour band
- Gift wrap options are identified by pattern (plain / dotted / striped) plus text label, never by wrap colour alone
- Bravado and Nervous Laughter meters use fill position plus a numeric readout
- Achievement tokens use distinct silhouettes (shield / gift / box / envelope / crown), readable at 32px in greyscale
- Touch zones minimum 44px for all five product walls, the wrapping station, the counter, the gift card rack, and every purchase button

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) the gold storefront lettering and all five section header plates need higher-quality blocks — the elegance is the joke and banding kills it
- **Fallback:** PNG-24 high quality for `condomerie_exterior.png` (gold lettering on cream is compression-hostile) and the header-plate region of `condomerie_interior.png`

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| condomerie_environment | condomerie_exterior, condomerie_interior | 2048x1280 |
| condomerie_characters | npc_condomerie_cast | 1024x512 |
| condomerie_objects_ui | condomerie_products_items, condomerie_ui_effects | 1024x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full golden shimmer (8 motes), blush heat wisps, window reflection overlay, spotlight cone, 4 customer NPCs |
| Medium | Shimmer at 4 motes, reflection overlay retained, spotlight cone simplified to a flat gradient, 3 customer NPCs |
| Low | No shimmer or wisp particles, no reflection overlay, static lighting, staff plus 1 customer NPC only (profile-mandated abstracted displays and simplified customer animations) |

### Performance Targets:
- **Target FPS:** 60 (per location profile performance budget)
- **Max Draw Calls:** 14 per frame (per location profile)
- **Memory Footprint:** 32 MB maximum (per location profile)
- **Particle Limit:** 12 (golden shimmer, blush wisps, register sparkle combined — the smallest budget in Shamsterdam, by design)

### Performance Notes:
- Interior and exterior are separate scenes with a hard door transition; only one is resident at a time
- Product wall sprites are the largest single-texture cost — they are loaded as a group and stay resident for the whole visit rather than streaming per section
- Bachelorette Party counts as 2 against the 4-NPC cap and blocks the Older Couple spawn to protect the draw-call ceiling
- The location has no ambient particle bed at all; the shimmer only emits near the accent trim and the Art Pieces plinth

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (composed product walls, facade), TileMap (floor and baseboard), AnimatedSprite2D (Femke, Joost, wrapping sequence, customers), CPUParticles2D (golden shimmer, blush wisps — not GPU), CanvasModulate (day/evening exterior state), Area2D interaction hotspots sized ≥44px, ShaderMaterial with a single `blush` float on the Groom sprite
- Special systems: solo-entry Bravado check gated on party size, five-section browse-state tracker feeding the Staff Approach Level machine, gag-gift declaration flag with hidden ratio counter for the epilogue, gift-wrap selector with three output package sprites, bachelor-party detection (3+ members) driving discount and Groom Spotlight, bag-visibility flag that propagates to Tolerance Hostel kitchen dialogue, three-visit Condomerie Regular counter

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Shop Door — Open | Door chime + street noise crossfade | On sprite state change |
| Wrapping frame 1 | Paper crease | On frame display |
| Wrapping frame 2 | Ribbon pull | On frame display |
| Register Chime Sparkle | Terminal beep, then warm chime | Beep on tap, chime on sparkle frame 1 |
| Nervous Giggle shoulder shake | Suppressed-laughter bed + subtle comedy note | Note on indicator peak |
| Groom blush ramp peak | Bachelorette "ooooh" from across the shop | On ramp completion |
| Staff Approach frame 2 | Soft footstep on polished floor | On frame display |
| Package Rustle lines | Paper handling | On bagging action |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Bachelor Party Achievement Track | Achievement token strip, purchase confirmation, bundle and mystery box sprites | Five stages: Protected / Party Supplies / Risk Taker / Brave Soul / Bachelor Party Legend |
| The Groom Spotlight | Groom blush frames, blush wisp, bachelorette reaction | Fires once per bachelor-party visit at the counter |
| Gag Gift Ledger (epilogue) | Purchase Ratio Tracker Chip, gag/personal toggle | Hidden tally surfaced only in the end-of-trip epilogue |
| Condomerie Regular | Regular Nod Badge, progress UI, Femke idle variant | Third visit; staff nod, other customers notice |
| Solo Entry Challenge | Bravado check prompt, blush wisp, door sprites | Doorway check when the player enters without the party |
| Inventory Consequence Chain | Distinctive shopping bag, bag-visibility silhouette, "What's in the bag?" prompt | Bag remains visible in party inventory for the rest of the trip |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Tolerance Hostel | Distinctive shopping bag and bag-visibility silhouette reused in kitchen scenes | Bag prop carries into hostel dialogue; guests comment |
| Casa Rosé Erotic Theatre | Shared Roodelicht-adjacent street backdrop tile and red neon bleed | Same-district walk; neon bleed intensity increases toward Casa Rosé |
| FEBO Automat | None shared; post-purchase snack-run dialogue hook | Standard street transition |
| Café de Schaamte | Shopping bag visible on the terrace; overheard-conversation hook | Bros process the purchase over espresso |
| Airport / Customs (if implemented) | Shopping bag and receipt sprites | Awkward-moment scene uses the same bag art |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A jeweller's shop that happens to sell condoms, staffed by people who find nothing at all remarkable about that"
- **Color Mood:** Cream and gold with black typography — warm, expensive, calm; the deep red appears only as ribbon and accent, never as mood lighting
- **Lighting:** Even boutique wash with one dramatic spotlight on the Novelties section; the only red light in the location leaks in from a neighbouring street and is never allowed to touch the merchandise
- **Texture:** Polished wood, brushed brass, matte card stock, clean glass — every surface says "we clean this daily"

### Environmental Storytelling:
- The floor wear pattern runs straight from the door to Section 4; the shop knows exactly where you are going before you do
- The Art Pieces plinth is museum furniture, lit like museum furniture, holding something you cannot say out loud
- "Since 1987" appears once, in small type, while the tourist behaviour it has witnessed has not changed in nearly forty years
- The gift card rack exists, is stocked, and is regularly depleted — someone is buying these
- The waiting bench has a worn spot, because "I'm Just Looking" guy has always been here

### Character Integration Notes:
- Femke is composed in every single frame — no eyebrow, no smirk, no shared glance with the player. Her power is that she is simply working.
- Joost's animation is looser and more theatrical than Femke's; he finds the tourists genuinely fascinating and it shows in his posture, never in his face
- Customers carry all of the location's comedy: the giggle, the blush, the paralysis, the bulk-buy bravado
- The bros are rendered slightly larger and louder in composition than the surrounding customers — the room accommodates them without ever acknowledging them

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Art Pieces Plinth** - Museum lighting, gallery plinth, absolute sincerity
2. **Femke's Unflappable Stare** - Held frame, zero expression, infinite authority
3. **The Groom Spotlight Blush** - Full red ramp with the whole shop politely not reacting
4. **The Overfull Bachelor Party Basket** - Structural failure imminent, price tags visible
5. **"Yes, you can just browse. No, we don't judge. Much."** - The window sign in full elegant gold
6. **The Floor Wear Path To Section 4** - Environmental storytelling with zero dialogue

### Quote Potential:
- "We've been here since 1987. We've seen everything. You cannot surprise me. I promise."
- "It's protection. It's healthy. It's also, yes, shaped like that. Both things are true."
- "You're buying it as a joke? Cool. It still works as a joke. Also other things."
- "The Golden Fleece? Jason's quest. Protection on a journey. The metaphor writes itself."
- "Gift wrapping? Of course. Discreet or… expressive?"
- "Every laugh, every blush, every nervous joke — that's culture processing itself. We witness it. We don't judge it."
- "The novelty section is to your left. I assume that's where you're headed. Most people are."

---

## 📋 Required PNG Files (5 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | condomerie_exterior.png | 1024x512 |
| 2 | condomerie_interior.png | 1024x768 |
| 3 | condomerie_products_items.png | 512x512 |
| 4 | npc_condomerie_cast.png | 1024x288 |
| 5 | condomerie_ui_effects.png | 512x512 |

**Total Estimated Memory:** ~8.1 MB raw RGBA texture data (~3.6 MB after VRAM compression); ~32 MB maximum total runtime footprint per the location performance budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `condomerie_exterior.png` (1024x512)
- [ ] `condomerie_interior.png` (1024x768)
- [ ] `condomerie_products_items.png` (512x512)
- [ ] `npc_condomerie_cast.png` (1024x288)
- [ ] `condomerie_ui_effects.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + product-abstraction style guide (packaging-only rule, with approved and rejected examples) + Staff Approach Level state chart

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (#FFD700, #8B0000, #FFF8DC, #1A1A1A, #E8C466, #C43B5A)
- [ ] Every product sprite is packaging-level abstraction only — no anatomical rendering at any zoom level, on any sheet
- [ ] Key gags read clearly at phone scale: gold storefront lettering, "we don't judge. Much." sign, floor wear path to Section 4, Art Pieces plinth, overfull bachelor basket, groom blush
- [ ] Accessibility visual alternatives included for all audio cues (register beep, package rustle, music bed, nervous laughter, street bleed, door chime)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (tourist awkwardness and novelty markup — never the shop, the staff, or sexual health itself)
- [ ] Femke and Joost are composed and professional in every single frame; all reaction comedy belongs to customers
- [ ] Hidden areas/interactions have discoverable visual cues (sizing guide requires asking, gift card rack, Art Pieces plinth, three-visit Regular track)
- [ ] Performance optimized (12-particle ceiling, three atlases, separate interior/exterior scenes)
- [ ] Touch zone sizing considered (44px minimum on all five walls, wrapping station, counter, gift card rack, purchase buttons)
- [ ] Colorblind-friendly alternatives available where color codes meaning (section hatching, wrap patterns, achievement silhouettes)
- [ ] Social media viral potential maximized in composition choices (plinth framing, Femke's held stare, basket structural failure)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | All in-world signage reads "Shamsterdam"; the profile's "Amsterdam institution" note is design commentary, never asset text |
| Cultural Specificity | ✅ | Dutch sexual-health openness and direct professionalism vs. anglophone tourist awkwardness |
| Satirical Targets Appropriate | ✅ | Punches at tourist immaturity and bachelor-party bravado; Femke, Joost and the shop are rendered competent, dignified and correct throughout |
| Seedy Underbelly Present | ✅ | Novelty markup on items bought "as a joke," the 45 Sovs bundle, the 30 Sovs Mystery Box, and the 60% of gag gifts quietly kept |
| Gameplay Value Established | ✅ | Solo-entry Bravado check, five-section browsing, gag-gift declaration, gift-wrap service, group discount, Groom Spotlight, inventory-visibility chain, five-stage achievement track |
| Technical Feasibility | ✅ | Separate interior/exterior scenes, composed wall sprites, single-float blush shader, 12-particle ceiling all documented |
| Performance Budget | ✅ | 60 FPS, 14 draw calls, 32 MB per profile budget |
| Accessibility Features | ✅ | Six visual audio cues, reduced-motion shimmer/blush/wrap alternatives, section hatching, 44px zones |
| No Crypto Elements | ✅ | Cash, card, and gift cards; pure traditional retail awkwardness |
| Social Media Integration | ✅ | Six screenshot moments plus a seven-line quote bank identified |

**Once these assets are delivered, Condomerie Het Gulden Vlies becomes Eurobound's mirror: the one location where nobody is doing anything wrong, the staff are unfailingly kind, the products are functional and well made — and the player still has to watch three grown men in matching shirts fall apart at the sight of a tastefully lit display case.**
