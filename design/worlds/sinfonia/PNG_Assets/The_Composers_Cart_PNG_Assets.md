# The Composer's Cart - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for The Composer's Cart — the MusikGasse manuscript stall where an ancient vendor can name any piece from three notes, will tell you exactly what is wrong with your interpretation, and has posted a sign begging you not to hum. It is a rhythm-buff shop with a four-tier patron ladder, a humming mini-game that can earn you a discount or a ten-minute ban, and a man whose gatekeeping is a defence mechanism against thirty years of badly hummed "Für Elise."

**Location ID:** `sinfonia_musikgasse_composers_cart_01`
**Theme:** Classical-music gatekeeping — the belief that appreciation requires expertise and that some interpretations are simply *wrong*
**Zone:** MusikGasse, Street Performer District
**Hours:** 9 AM - 9 PM (the vendor keeps musician hours)
**Primary Function:** Street vendor / specialty shop — rhythm-game buff items, humming mini-game, Patron of the Arts progression, quest hints, three selfie variants

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Parchment Cream | #F5DEB3 | Sheet music, scrolls, manuscript stacks |
| Ink Black | #1A1A1A | Notation, lettering, vendor's coat, portrait frames |
| Aged Paper | #FFF8DC | Backdrop paper mass, folios, vellum |
| Musical Gold | #CFB53B | Cart brasswork, seals, patron badge, portrait gilt |
| Cart Walnut | #6B4A2F | Cart timber, crates, shelving (derived structural tone) |
| Foxing Umber | #8A6B3A | Water stains, page edges, dust accumulation (derived weathering tone) |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/the_composers_cart/
├── environment/
│   ├── composers_cart_tileset.png
│   └── composers_cart_props.png
├── npcs/
│   ├── herr_notenschreiber.png
│   └── composers_cart_npcs.png
├── objects/
│   └── composers_cart_items.png
├── effects/
│   └── composers_cart_effects.png
└── ui/
    └── composers_cart_ui.png
```

---

## 📜 Sprite Sheet 1: MusikGasse Street & Cart Tileset
**File:** `composers_cart_tileset.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #6B4A2F (Cart Walnut), #F5DEB3 (Parchment Cream), #FFF8DC (Aged Paper), #CFB53B (Musical Gold)

### Street & Ground Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| MusikGasse Cobble | (0, 0) | 32x32 | Base district paving |
| Cobble, Ink-Stained | (32, 0) | 32x32 | Decades of spilled inkwells |
| Cobble With Chalk Staff Lines | (64, 0) | 32x32 | Busker pitch markings |
| Kerb | (96, 0) | 32x32 | Street boundary |
| Gutter | (128, 0) | 32x32 | Drainage run |
| Paving, Worn Smooth By Buskers | (160, 0) | 32x32 | Performance pitch |
| Drain Grate | (192, 0) | 32x32 | Detail tile |
| Loose Sheet On Ground | (224, 0) | 32x32 | Escaped manuscript |

### Wall & Façade:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| MusikGasse Stucco | (0, 32) | 32x64 | Standard façade |
| Stucco With Music-School Plaque | (32, 32) | 32x64 | Conservatory adjacency |
| Shuttered Window | (64, 32) | 32x64 | Practice rooms above |
| Arched Doorway | (96, 32) | 32x64 | Neighbouring entrance |
| Bill-Posted Wall, Concert Flyers | (128, 32) | 32x64 | Pasted layers deep |
| Downpipe | (160, 32) | 16x64 | Cast-iron detail |
| Corner Return | (176, 32) | 16x64 | Façade turn piece |

### Street Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Busker Pitch Chalk Circle | (0, 96) | 64x32 | Territory marker |
| Street Lamp, Wrought | (64, 96) | 24x96 | District standard |
| Bollard | (88, 96) | 16x32 | Kerb furniture |
| Café Chair, Stray | (104, 96) | 24x40 | Migrated from somewhere |
| Instrument Case, Open | (128, 96) | 48x24 | Coins inside |
| Bicycle | (176, 96) | 48x40 | Leaned |
| Planter | (224, 96) | 32x40 | Street greenery |
| Pigeon On Manuscript | (256, 96) | 32x24 | The vendor has seen this and chosen to survive it |
| Concert Flyer Bundle | (288, 96) | 32x32 | Undistributed |
| Sandwich Board, Rival Busker | (320, 96) | 48x64 | Competition |
| Tram Rail Strip | (368, 96) | 48x16 | District infrastructure |
| Window Box | (368, 112) | 48x32 | Above-street detail |

### The Cart Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Antique Cart Body | (0, 192) | 192x128 | Overflowing wooden cart, paper on every surface |
| Cart Wheel Large | (192, 192) | 64x64 | Spoked, rarely turned |
| Cart Wheel Small | (256, 192) | 48x48 | Front castor |
| Dust-Sheet Cover | (304, 192) | 80x64 | Closing state |
| Pinned Sheet Music Surface A | (384, 192) | 96x64 | Tileable pinned-paper skin |
| Pinned Sheet Music Surface B | (480, 192) | 96x64 | Variant skin |
| Manuscript Pile, Stable | (576, 192) | 96x64 | Chaos with an internal logic |
| Paper Avalanche, Collapsed | (672, 192) | 128x128 | "I Touched Something" |
| Cart Canopy Frame | (192, 256) | 96x64 | Overhead structure |
| Cart Side Shelf | (288, 256) | 96x32 | Display run |
| Cart Undershelf, Crated Folios | (288, 288) | 96x32 | Bulk storage |
| Cart Handle Shafts | (384, 256) | 96x24 | Pull bars |
| Fluttering Pinned Sheet, Frame A | (384, 280) | 48x40 | Breeze frame A |
| Fluttering Pinned Sheet, Frame B | (432, 280) | 48x40 | Breeze frame B |
| Scroll Bundle | (480, 256) | 48x64 | Tied stock |
| Bound Folio Stack Tall | (528, 256) | 48x64 | Leather spines |
| Manuscript Pile, Toppling | (576, 256) | 96x64 | Mid-avalanche state |

### Signage & Cart Décor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Sign "The Composer's Cart — Manuscripts, Scores, & Musical Mysteries" | (0, 320) | 320x40 | Primary board |
| Secondary Sign "Please Do Not Hum. We Will Know If It's Wrong." | (0, 360) | 320x24 | The house rule |
| Hours Plate "9 AM – 9 PM" | (320, 320) | 96x24 | Musician hours |
| Price Slate | (320, 344) | 96x40 | Fair prices; he is not a scammer |
| Patron-of-the-Arts Notice | (416, 320) | 96x32 | 100 Sovs tier explained |
| "Musically Offensive — 10 Minute Ban" Placard | (416, 352) | 96x32 | Posted consequence |
| Faded Composer Portrait A | (512, 320) | 48x64 | Gilt-framed, sun-bleached |
| Faded Composer Portrait B | (560, 320) | 48x64 | Gilt-framed, sun-bleached |
| Faded Composer Portrait C | (608, 320) | 48x64 | Gilt-framed, sun-bleached |
| Metronome, Disapproving | (656, 320) | 32x64 | It ticks. It judges |
| Inkwell & Quill Set | (688, 320) | 48x32 | Working tools |
| Ink-Stain Decal | (688, 352) | 48x32 | Permanent |
| Rare-Stock Drawer, Locked | (736, 320) | 64x64 | Patron access only |

### Street Performer District (right block):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Busker Violinist Silhouette | (416, 0) | 64x96 | Distant performer layer |
| Busker Accordionist Silhouette | (480, 0) | 64x96 | Distant performer layer |
| Hurdy-Gurdy Player Silhouette | (544, 0) | 64x96 | Distant performer layer |
| Conservatory Gate | (608, 0) | 96x128 | The institution up the street |
| Music School Notice Board | (704, 0) | 96x64 | Recitals, lessons, lost sheet music |
| Instrument Shop Window | (704, 64) | 96x64 | Neighbouring trade |
| Distant Spire | (800, 0) | 96x128 | Skyline anchor |
| Awning, Striped | (896, 0) | 128x32 | Shop overhead |
| Chalked Staff Lines On Wall | (896, 32) | 128x32 | Busker practice marks |
| Hanging Sign, Treble Clef Bracket | (896, 64) | 64x64 | District iconography |
| Wall Poster "Für Elise Recital" | (960, 64) | 64x64 | The vendor has not looked at it in years |
| Bench | (416, 96) | 96x32 | Street seating |
| Rubbish Bin | (512, 96) | 32x40 | Contains rejected manuscripts |
| Cat Asleep On Folios | (544, 96) | 48x24 | Undisturbed, permitted |
| Paper Weight Stones | (608, 128) | 48x32 | Against the breeze |
| Cat, Awake | (608, 160) | 48x32 | Second state |
| Rolled Poster Tube Rack | (656, 128) | 48x64 | Large-format stock |
| Café Existenz Signpost | (704, 128) | 96x32 | Cross-location wayfinding |
| Bassline Opera House Signpost | (704, 160) | 96x32 | Cross-location wayfinding |
| Manuscript Crate, Delivery | (800, 128) | 64x64 | Fresh stock, unsorted |
| Handcart, Rival Vendor | (864, 128) | 96x64 | Inferior, and he knows it |
| Cobble Puddle Reflection | (960, 128) | 64x64 | Wet-street variant |

### Backdrop / Parallax Layers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| MusikGasse Backdrop Far | (0, 384) | 512x128 | Slow parallax building line |
| MusikGasse Backdrop Near, Street Performers | (512, 384) | 384x128 | Fast parallax with distant buskers |
| Daylight Gradient Overlay | (896, 384) | 128x128 | Additive natural-light wash |

### Technical Notes:
- The cart must read as **chaotic but navigable** — the vendor finds anything instantly, and the art has to support that being plausible rather than magical
- Pinned Sheet Music Surfaces A and B are tileable skins applied over the cart body; the fluttering frames replace specific pinned regions at runtime, so their edges must match the skin seams exactly
- Manuscript Pile Stable / Toppling / Avalanche is a three-state progression sharing a base silhouette — the "Paper Avalanche" achievement plays across all three
- The three faded portraits are deliberately generic and unnamed; no real composer likeness
- Regions x992–1024 (y0–128) and x800–1024 (y192–320) are reserved padding

---

## 🖋️ Sprite Sheet 2: Manuscripts, Instruments of Judgment & Cart Props
**File:** `composers_cart_props.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #F5DEB3 (Parchment Cream), #FFF8DC (Aged Paper), #1A1A1A (Ink Black), #8A6B3A (Foxing Umber)

### Paper Stock:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sheet Music Sheaf, Loose | (0, 0) | 64x64 | Untied, precarious |
| Sheet Music, Pinned Row | (64, 0) | 96x32 | Display run |
| Ledger, Vendor's | (64, 32) | 48x32 | Every sale, recorded |
| Paper Clip Weights | (112, 32) | 48x32 | Against the breeze |
| Folio, Bound Leather | (160, 0) | 48x64 | Premium stock |
| Folio, Open | (208, 0) | 64x64 | Notation visible |
| Scroll, Sealed | (272, 0) | 32x64 | Unexamined |
| Scroll, Unrolled | (304, 0) | 64x64 | Examined |
| Vellum Sheet, Ancient | (368, 0) | 48x64 | Rare stock |
| Paper Stack, Short | (416, 0) | 48x32 | Common compositions |
| Wax Seal Detail | (416, 32) | 48x32 | Close-up prop |
| Paper Stack, Tall | (464, 0) | 48x64 | Bulk |

### Paper Detail & The Metronome:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Loose Page Airborne A | (0, 64) | 32x32 | Flutter frame |
| Loose Page Airborne B | (32, 64) | 32x32 | Flutter frame |
| Loose Page Airborne C | (0, 96) | 32x32 | Flutter frame |
| Loose Page Airborne D | (32, 96) | 32x32 | Flutter frame |
| Torn Corner Detail | (64, 64) | 32x32 | Damage state |
| Foxing Stain Detail | (96, 64) | 32x32 | Age state |
| Ink Blot Decal | (64, 96) | 64x32 | Accident, preserved |
| Metronome, Still | (128, 64) | 48x64 | Silent |
| Metronome, Arm Left | (176, 64) | 48x64 | Tick |
| Metronome, Arm Right | (224, 64) | 48x64 | Tock |
| Inkwell, Full | (272, 64) | 32x32 | Working |
| Inkwell, Dry | (304, 64) | 32x32 | Neglected |
| Quill Pen | (336, 64) | 32x48 | In use |
| Quill Stand | (368, 64) | 32x48 | At rest |
| Blotter | (272, 96) | 64x32 | Ink-soaked |
| Sealing Wax Stick | (336, 112) | 32x16 | For premium stock |
| Nib Box | (368, 112) | 32x16 | Spares |
| Spectacles, Thick As Opera Glasses | (400, 64) | 48x32 | His only optic |
| Magnifier | (448, 64) | 32x32 | For the small notation |
| Cash Tin | (480, 64) | 32x32 | Fair prices, honestly kept |
| Coin Dish | (400, 96) | 48x32 | Change |
| Rubber Stamp "Patron" | (448, 96) | 32x32 | Tier confirmation |
| Receipt Spike | (480, 96) | 32x32 | Impaled sales slips |

### Portraits, Rare Stock & Musical Tools:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Faded Composer Portrait 1 | (0, 128) | 48x64 | Anonymous, gilt-framed |
| Faded Composer Portrait 2 | (48, 128) | 48x64 | Anonymous, gilt-framed |
| Faded Composer Portrait 3 | (96, 128) | 48x64 | Anonymous, gilt-framed |
| Portrait, Glass Cracked | (144, 128) | 48x64 | Never repaired |
| Bust, Chipped | (192, 128) | 48x64 | Plaster, nose gone |
| Rare-Stock Drawer, Open | (240, 128) | 64x64 | Patron of the Arts access |
| Lost Manuscript In Drawer | (304, 128) | 48x64 | 50 Sovs, permanent +25% rhythm timing |
| Forbidden Opus, Wrapped | (352, 128) | 48x64 | 75 Sovs, still wrapped |
| Tuning Fork | (400, 128) | 24x48 | Reference pitch |
| Pitch Pipe | (424, 128) | 24x24 | Portable reference |
| Dust Sheet | (424, 152) | 24x40 | Cover cloth |
| Rosin Block | (400, 176) | 24x16 | Busker supply |
| Conductor's Baton | (448, 128) | 64x16 | Not for sale |
| Music Stand, Folded | (448, 144) | 64x48 | Leaning |

### Cart Furniture & Enforcement:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cart Awning Cloth | (0, 192) | 96x64 | Weather cover |
| Crate, Manuscripts | (96, 192) | 64x64 | Sorted |
| Crate, Empty | (160, 192) | 64x64 | Awaiting delivery |
| Stool, Vendor's | (224, 192) | 32x48 | Worn to his shape |
| Blanket On Stool | (256, 192) | 32x32 | Winter provision |
| Thermos Of Something Bitter | (288, 192) | 24x40 | Personal |
| Handbill Spike | (312, 192) | 24x40 | Rejected flyers |
| Vendor's Coat On Hook | (336, 192) | 48x64 | Ink-marked at the cuffs |
| "Do Not Hum" Small Placard | (384, 192) | 96x24 | Cart-mounted duplicate |
| "We Will Know" Sub-Placard | (384, 216) | 96x24 | The threat, itemised |
| Ban Timer Hourglass | (384, 240) | 96x16 | Ten minutes, enforced |
| Chalk Tally Of Offenses | (480, 192) | 32x64 | Marks going back years |

### Technical Notes:
- The metronome's three states (still / left / right) must be visually identical apart from the arm — it is a background presence with a running audio commitment
- **Every piece of notation drawn on any sheet must be non-specific.** No recognisable real melody may be legible at any zoom level; use plausible but invented notation
- The chalk tally of offenses is dressing, not a counter — it never updates at runtime
- Rare-Stock Drawer Open pairs with the Locked variant on Sheet 1; they must align to the same cart geometry

---

## 👓 Sprite Sheet 3: Herr Notenschreiber — The Vendor
**File:** `herr_notenschreiber.png`
**Dimensions:** 384x288 pixels
**Color Palette:** #1A1A1A (Coat, ink), #F5DEB3 (Shirt/parchment key), #8A6B3A (Weathering), #CFB53B (Spectacle rims)

### Working & Approving States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Neutral, Already Disappointed | (0, 0) | 48x96 | The resting state |
| Squinting Through Spectacles | (48, 0) | 48x96 | Thick as opera glasses |
| Identifying From Three Notes | (96, 0) | 48x96 | He needs no more than three |
| Retrieving Item From Chaos | (144, 0) | 48x96 | Instantly, without looking |
| Flicker Of Hope | (192, 0) | 48x96 | "I took lessons until age 12." |
| Genuine Surprise | (240, 0) | 48x96 | Obscure piece, hummed correctly |
| Nod Of Approval | (288, 0) | 48x96 | Mozart, correct |
| Rare Respect | (336, 0) | 48x96 | "...You have taste. This is unexpected." |

### Pain & Enforcement States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Heavy Sigh | (0, 96) | 48x96 | "Für Elise," again, basic |
| Visible Pain | (48, 96) | 48x96 | "Für Elise," wrong |
| Clutching Chest | (96, 96) | 48x96 | Conservatory boaster's wrong note |
| "He's ROLLING In His Grave" | (144, 96) | 48x96 | Mozart, wrong |
| Confusion, Then Intrigue | (192, 96) | 48x96 | Made-up tune: "What IS that?" |
| RAGE | (240, 96) | 48x96 | Copyrighted modern song |
| Pointing To The Sign | (288, 96) | 48x96 | "Please Do Not Hum." |
| Issuing The 10-Minute Ban | (336, 96) | 48x96 | "Musically Offensive" |

### Teaching & Extended States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Lecture, Beginning | (0, 192) | 48x96 | Educational, and long |
| The Lecture, Ongoing | (48, 192) | 48x96 | Still going |
| The Quiz Pose | (96, 192) | 48x96 | Testing a customer |
| The Recommendation | (144, 192) | 48x96 | "You seem like a Beethoven player. Aggressive. Dramatic. Here." |
| Humming The Four Notes Himself | (192, 192) | 48x96 | Dun dun dun DUNNN — done correctly |
| Horrified | (240, 192) | 48x96 | Paper avalanche witnessed |

### Detail Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ink-Stained Fingers | (288, 192) | 48x24 | Permanent |
| Thick Spectacles | (288, 216) | 48x24 | Close-up |
| Squint Close-Up | (288, 240) | 48x48 | The identifying look |
| Hand On Manuscript, Reverent | (336, 192) | 48x48 | He loves this. That is the tragedy |
| Metronome Held | (336, 240) | 48x48 | Demonstrating correct tempo |

### Animation Timing:
- Neutral idle: 2fps, loop — minimal, weary, occasional squint
- Identifying From Three Notes: 1.5s hold, single play, fires the instant a tune is triggered
- Reaction states: 1.0s minimum hold before returning to Neutral; RAGE holds 2.0s
- The Lecture: 2 frames alternating at 1fps for as long as the lecture text runs (deliberately, uncomfortably long)
- Rare Respect: 1.5s hold — the longest positive expression he has

### Character Notes:
- **He genuinely loves music.** Every pained frame is grief, not snobbery — decades of tourists have broken something, and the art must show the break rather than the contempt
- Ink-stained fingers and thick spectacles are the silhouette identifiers at 48px; both must be present in every frame
- He is ancient and physically small; the paper piles should tower over him in composition
- The Flicker Of Hope frame is the most important expression on the sheet: it is what he looks like when he thinks somebody might understand
- He never smiles broadly. Rare Respect is a softening, not a grin

---

## 🎻 Sprite Sheet 4: Street Performers, Customers & The Bros
**File:** `composers_cart_npcs.png`
**Dimensions:** 384x192 pixels
**Color Palette:** MusikGasse earth tones, #F5DEB3 (Parchment accents), #1A1A1A (Ink Black)

### Performers & Customers (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Street Performer, Violinist | (0, 0) | 48x96 | MusikGasse regular |
| Street Performer, Mid-Wrong-Note | (48, 0) | 48x96 | The cart hears everything |
| Conservatory Boaster | (96, 0) | 48x96 | "I studied at the conservatory! Watch THIS—" |
| Conservatory Boaster, Humiliated | (144, 0) | 48x96 | The note lands badly |
| Passing Tourist, Humming | (192, 0) | 48x96 | Unaware of the sign |
| Passing Tourist, Banned | (240, 0) | 48x96 | Ten minutes, outside |
| Regular Customer, Patron Badge | (288, 0) | 48x96 | Allowed to hum, within reason |
| Regular, Requesting Obscure Piece | (336, 0) | 48x96 | Found instantly |

### The Bros (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Chadwick, Absently Humming Pop | (0, 96) | 48x96 | "WHAT is THAT?" |
| Chadwick, Defending A Billion Streams | (48, 96) | 48x96 | "A BILLION people can be WRONG." |
| Lord Pilsner, Pointing At Random | (96, 96) | 48x96 | "What's this one?" |
| Lord Pilsner, "Dun dun dun DUNNN!" | (144, 96) | 48x96 | "Please leave the 'dun duns' to the professionals." |
| Bradley, Quiet Bach | (192, 96) | 48x96 | Cello Suite No. 1, hummed correctly |
| Bradley, 15% Off | (240, 96) | 48x96 | "I paid attention during lessons." |
| Bro Buried In Manuscripts | (288, 96) | 48x96 | Paper avalanche victim |
| Party Retreating From Cart | (336, 96) | 48x96 | Ban served, dignity not recovered |

### Character Notes:
- The Conservatory Boaster is the tutorial for the humming system: the player watches someone else fail before risking it
- Street performers are drawn at slightly lower contrast than cart-side NPCs so the eye stays on the vendor
- Bradley's Quiet Bach frame is the only bro sprite in this location drawn with composed posture — it is the visual joke

---

## 🎼 Sprite Sheet 5: Manuscripts, Consumables & Tune Cards
**File:** `composers_cart_items.png`
**Dimensions:** 256x256 pixels
**Color Palette:** #F5DEB3 (Parchment Cream), #1A1A1A (Ink Black), #CFB53B (Musical Gold), #8A6B3A (Foxing Umber)

### Standard Items (32x48 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Basic Score | (0, 0) | 32x48 | 5 Sovs, +5% rhythm timing |
| Practice Sheet | (32, 0) | 32x48 | 8 Sovs, +10% rhythm timing, one battle |
| Tempo Guide | (64, 0) | 32x48 | 12 Sovs, reveals enemy attack patterns |
| Conductor's Notes | (96, 0) | 32x48 | 15 Sovs, +15% rhythm damage |
| Harmony Chart | (128, 0) | 32x48 | 20 Sovs, party rhythm sync +10% |
| Crescendo Script | (160, 0) | 32x48 | 10 Sovs, damage increases each turn |
| Diminuendo Draft | (192, 0) | 32x48 | 10 Sovs, enemy damage decreases each turn |
| Fermata Fragment | (224, 0) | 32x48 | 15 Sovs, pause enemy for one turn |

### Premium & Consumables:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lost Manuscript | (0, 48) | 48x64 | 50 Sovs, +25% rhythm timing, permanent passive |
| Forbidden Opus | (48, 48) | 48x64 | 75 Sovs, unlocks secret rhythm pattern |
| The Unfinished Symphony | (96, 48) | 48x64 | 100 Sovs, massive buff that ends randomly |
| Original Composition | (144, 48) | 48x64 | 150 Sovs, custom attack pattern, unique to player |
| Sforzando Scrap | (192, 48) | 32x32 | 20 Sovs, one attack deals 3x damage |
| Patron Badge | (224, 48) | 32x32 | 100 Sovs tier indicator |
| Rare LP Cross-Reference Card | (192, 80) | 64x32 | Points toward the Vinyl Hunt |

### Status & Reaction Icons (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Musically Offensive (Ban) Icon | (0, 112) | 32x32 | Ten-minute lockout |
| Rhythm Timing Buff Icon | (32, 112) | 32x32 | Widened window |
| Rhythm Damage Buff Icon | (64, 112) | 32x32 | Increased on-beat damage |
| Party Sync Icon | (96, 112) | 32x32 | Coordinated attacks |
| Pattern Reveal Icon | (128, 112) | 32x32 | See the beat coming |
| Discount 5% Token | (160, 112) | 32x32 | Mozart, correct |
| Discount 15% Token | (192, 112) | 32x32 | Obscure piece, correct |
| Price Increase 10% Token | (224, 112) | 32x32 | Mozart, wrong |

### Humming Tune Cards:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tune Card "Für Elise" | (0, 144) | 64x32 | Heavy sigh, or visible pain |
| Tune Card "Mozart" | (64, 144) | 64x32 | Nod, or "He's ROLLING in his grave" |
| Tune Card "Obscure Piece" | (128, 144) | 64x32 | Genuine surprise, or "You ALMOST had it" |
| Tune Card "Made-Up Tune" | (192, 144) | 64x32 | Confusion, then intrigue — possible quest trigger |
| Tune Card "Copyrighted Modern Song" | (0, 176) | 64x32 | RAGE, ten-minute ban |
| Tune Card, Blank | (64, 176) | 64x32 | Reusable frame |
| Correct Interpretation Marker | (128, 176) | 32x32 | Resolved, consonant glyph |
| Wrong Interpretation Marker | (160, 176) | 32x32 | Cracked, dissonant glyph |
| "You ALMOST Had It" Marker | (192, 176) | 64x32 | Respect for trying |

### Selfie & Quest Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Caption Plate "Cultured" | (0, 208) | 80x24 | Standard photo |
| Caption Plate "He Didn't Cringe" | (80, 208) | 96x24 | Requires passing a humming test |
| Caption Plate "I Touched Something" | (176, 208) | 80x24 | Requires the paper avalanche |
| Lost Opus Quest Card | (0, 232) | 96x24 | Vendor's fetch quest |
| Correct Interpretation Quest Card | (96, 232) | 96x24 | Learn a piece properly |
| Humming Champion Rosette | (192, 232) | 32x24 | All tests passed |
| Sheet-Music-Upside-Down Prop | (224, 232) | 32x24 | Standard selfie prop |

### Technical Notes:
- All item sprites must be distinguishable by paper *format* at 32px: single sheet, folded sheet, bound folio, sealed scroll, wrapped parcel. Colour is secondary
- The Unfinished Symphony is visibly, deliberately incomplete — the notation stops mid-stave
- Tune cards carry a non-specific notation fragment plus the descriptor text; **no real melody may be legible**
- Correct/Wrong interpretation markers are shape-coded (resolved circle vs. cracked circle), never colour-only

---

## 🍃 Sprite Sheet 6: Paper Flutter, Ink & Judgment Glyphs
**File:** `composers_cart_effects.png`
**Dimensions:** 256x192 pixels
**Color Palette:** #FFF8DC (Aged Paper), #F5DEB3 (Parchment), #1A1A1A (Ink), #8A6B3A (Dust)

### Paper Motion:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Paper Flutter Frame A | (0, 0) | 48x48 | Pinned sheet in breeze |
| Paper Flutter Frame B | (48, 0) | 48x48 | Frame B |
| Paper Flutter Frame C | (96, 0) | 48x48 | Frame C |
| Page Turn A | (144, 0) | 32x32 | Browsing |
| Page Turn B | (176, 0) | 32x32 | Browsing |
| Paper Avalanche Burst | (208, 0) | 48x48 | Collapse moment |
| Page Swirl Trail | (144, 32) | 64x16 | Airborne trajectory |

### Dust, Ink & Light:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dust Mote Cluster | (0, 48) | 48x32 | Ambient |
| Dust Puff | (48, 48) | 32x32 | Pile disturbed |
| Ink Drip A | (80, 48) | 16x32 | From the quill |
| Ink Drip B | (96, 48) | 16x32 | Frame B |
| Ink Splatter | (112, 48) | 32x32 | Impact |
| Motes In Daylight Shaft | (144, 48) | 32x32 | Concentrated |
| Daylight Shaft | (176, 48) | 80x48 | Natural light through paper |
| Paper Edge Glow | (0, 80) | 48x16 | Backlit sheet rim |
| Metronome Tick Arc | (48, 80) | 48x16 | Arm sweep trail |
| Chalk Dust | (96, 80) | 48x16 | Slate writing |
| Quill Scratch Mark | (144, 80) | 32x16 | Writing feedback |

### Judgment & Audio Glyphs:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Discordant Sting Glyph | (0, 96) | 32x32 | Bad humming audio marker |
| Pleasant Resolution Glyph | (32, 96) | 32x32 | Good humming audio marker |
| Pain Glyph (Bad Humming) | (64, 96) | 32x32 | His physical reaction, visualised |
| Three-Note Recognition Glyph | (96, 96) | 48x32 | He has identified it |
| Metronome Tick Glyph | (144, 96) | 32x32 | Tick audio marker |
| Page Rustle Glyph | (176, 96) | 32x32 | Paper audio marker |
| Ban Buzzer Glyph | (208, 96) | 48x32 | Ten-minute lockout audio marker |
| Sigh Glyph | (0, 128) | 24x24 | Weary exhale |
| Approval Hum Glyph | (24, 128) | 24x24 | His "hmm" of approval |
| Purchase Chime Glyph | (48, 128) | 48x24 | Sale confirmed |
| Quiz Prompt Glyph | (96, 128) | 48x24 | He is testing you |
| Lecture Text-Wall Glyph | (144, 128) | 48x24 | Educational, and long |
| Respect Nod Glyph | (192, 128) | 32x24 | Earned |
| Confusion Glyph | (224, 128) | 32x24 | Made-up tune |

### Motion-Safe & Humming Feedback:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Paper Frame (Motion-Safe) | (0, 152) | 64x40 | No flutter |
| Static Metronome Frame (Motion-Safe) | (64, 152) | 48x40 | Arm held; tick conveyed by glyph only |
| Reduced Dust Density Variant | (112, 152) | 48x40 | Low-motion ambient |
| Humming Waveform, Correct | (160, 152) | 48x40 | Smooth, resolved contour |
| Humming Waveform, Wrong | (208, 152) | 48x40 | Jagged, unresolved contour |

### Technical Notes:
- Paper flutter is the location's signature motion — three emitters on the cart's pinned surfaces, offset so the cart never pulses in unison
- The Paper Avalanche Burst is the only high-particle event here (16 pages max) and it fires once per achievement
- Humming waveforms are the accessibility backbone of the mini-game: correct/wrong is legible by *contour shape* alone

---

## 🖥️ Sprite Sheet 7: Shop Interface, Humming Mini-Game & Patron Track
**File:** `composers_cart_ui.png`
**Dimensions:** 256x288 pixels
**Color Palette:** #1A1A1A (Panel), #CFB53B (Musical Gold frame), #FFF8DC (Field), #F5DEB3 (Highlight)

### Shop Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shop Panel Frame | (0, 0) | 160x96 | Manuscript list + vendor reaction |
| Item Row Blank | (160, 0) | 96x24 | Unselected |
| Item Row Highlighted | (160, 24) | 96x24 | Selected |
| Price Chip | (160, 48) | 48x24 | Price lettered as `N SOVS`; always fair. **The word is the symbol; no currency mark exists.** ⚠️ 48x24 is tight for numeral + `SOVS`: set the word at half-height under the figure, or widen the chip to 72x24. |
| Effect Chip | (208, 48) | 48x24 | Rhythm buff preview |
| Vendor Portrait Slot | (160, 72) | 96x24 | Live expression window |

### The Humming Mini-Game:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Humming Prompt Panel | (0, 96) | 128x64 | Tune selection and warning |
| Note Target Ring | (128, 96) | 48x48 | Pitch accuracy target |
| Pitch Slider | (176, 96) | 80x24 | Player input rail |
| Accuracy Meter | (176, 120) | 80x24 | Live interpretation score |
| Tune Selection Chip A | (128, 144) | 64x24 | Known tune option |
| Tune Selection Chip B | (192, 144) | 64x24 | Known tune option |
| Judgment Bar | (0, 160) | 128x24 | His verdict, filling |
| Vendor Reaction Face Slot | (128, 168) | 64x24 | Live expression during judgment |
| Consequence Chip | (192, 168) | 64x24 | Discount / price increase / ban |

### Patron of the Arts Track:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Patron Progress Bar | (0, 192) | 160x24 | 0 Sovs → 100 Sovs rail |
| Patron Tier Pip | (160, 192) | 24x24 | Milestone marker |
| Discount Badge | (184, 192) | 24x24 | 10% permanent |
| Rare Stock Unlock Banner | (208, 192) | 48x24 | Premium inventory opens |
| Spend Counter Plate "N / 100 SOVS" | (0, 216) | 96x40 | Running total; word lettered, no currency mark |
| Ban Timer Ring | (96, 216) | 40x40 | Ten-minute countdown |
| Quiz Panel | (136, 216) | 120x40 | His occasional test |

### Toasts & Prompts:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Achievement Toast Frame | (0, 256) | 128x32 | "Passed the Test" / "The Humming Champion" / "Genuine Respect" |
| Selfie Prompt Icon | (128, 256) | 32x32 | Photo-op indicator |
| Request Prompt Banner | (160, 256) | 96x32 | "Ask for something good" / "something popular" |

### Technical Notes:
- The Judgment Bar fills toward one of three outcomes and must be readable by fill *pattern* (solid / hatched / cross-hatched), not colour
- The Note Target Ring closes by geometry, never by hue shift
- The Ban Timer Ring is the only punitive UI element and must be non-hostile in tone — the ban is comedy, not punishment
- The Request Prompt Banner offers three phrasings; "something popular" is a valid choice with a real cost to his soul and none to your wallet

---

## 🎬 Animation Specifications

### Paper Flutter:
- **Duration:** 1.8 second cycle
- **Frames:** 3 (flutter A → B → C)
- **Pattern:** Continuous loop across three emitters on the cart's pinned surfaces, each offset by 0.6s
- **Trigger:** Constant during opening hours
- **Purpose:** The cart reads as *breathing* — sheet music fluttering like paper wings
- **Audio Sync:** Continuous soft paper-rustle bed; the Page Rustle Glyph fires on the loudest emitter cycle
- **Performance Optimization:** Two emitters on Medium; one static pinned surface on Low

### Metronome Tick:
- **Duration:** 1.0 second cycle (60 BPM, unhelpfully slow)
- **Frames:** 3 (still → arm left → arm right)
- **Pattern:** Continuous, never speeds up, never stops during opening hours
- **Trigger:** Constant
- **Purpose:** Disapproving timekeeping; also a free tempo reference the player can use
- **Audio Sync:** Tick on each arm extreme; Metronome Tick Glyph fires with it
- **Performance Optimization:** Static frame + glyph only on Low LOD; **static automatically under Reduced Motion**

### Three-Note Identification:
- **Duration:** 1.5 seconds, single play
- **Frames:** 1 (Identifying From Three Notes) + Three-Note Recognition Glyph
- **Pattern:** Snap in on the third note of any hummed tune; hold
- **Trigger:** Player hums, whistles, or selects a musical dialogue option near the cart
- **Purpose:** He needs three notes. That is the entire character in one animation
- **Audio Sync:** Three hummed notes from the player; a single sharp "hmm" of recognition on the third
- **Performance Optimization:** None needed

### The Judgment:
- **Duration:** 2.5 seconds, single play
- **Frames:** Identification hold → reaction frame → verdict
- **Pattern:** Judgment Bar fills across 1.5s, then the reaction frame snaps in and holds 1.0s
- **Trigger:** Humming mini-game resolution
- **Purpose:** The pause before the verdict is where the comedy lives
- **Audio Sync:** Silence during the bar fill; **discordant sting** (wrong) or **pleasant resolution** (correct) on the reaction frame
- **Performance Optimization:** None needed

### The Lecture:
- **Duration:** Variable — as long as the text runs, deliberately uncomfortable
- **Frames:** 2 (Lecture Beginning ↔ Lecture Ongoing) at 1fps
- **Pattern:** Slow alternation; the player may not skip the first 4.0 seconds
- **Trigger:** Wrong answer to the Quiz; "regular"/"popular" requests; certain humming failures
- **Purpose:** Educational but long — the punishment is his sincerity
- **Audio Sync:** Continuous measured speech; Lecture Text-Wall Glyph on the panel
- **Performance Optimization:** None needed

### RAGE (Copyrighted Modern Song):
- **Duration:** 2.0 second hold, single play
- **Frames:** 1 (RAGE) → Pointing To The Sign → Issuing The 10-Minute Ban
- **Pattern:** Snap to RAGE, hold 2.0s, then two 0.8s frames
- **Trigger:** Humming a copyrighted modern song near the cart
- **Purpose:** "That is NOT music. That is FOUR CHORDS repeating."
- **Audio Sync:** Harsh discordant sting on the snap; ban buzzer on the final frame
- **Performance Optimization:** None needed

### Paper Avalanche:
- **Duration:** 2.0 seconds, single play
- **Frames:** 3 (pile stable → toppling → collapsed) + 16-page burst
- **Pattern:** Pile leans, gives, and buries; pages settle over 1.2s
- **Trigger:** Browsing carelessly
- **Purpose:** The "I Touched Something" selfie and the "Paper Avalanche" achievement
- **Audio Sync:** Paper cascade; a single anguished vendor noise on the collapse frame
- **Performance Optimization:** Burst reduced to 8 pages on Medium, 4 on Low

### Vendor Reaction Hold:
- **Duration:** 1.0 second minimum per reaction (2.0s for RAGE), single play
- **Frames:** 1 + return to Neutral, Already Disappointed
- **Pattern:** Snap in, hold, ease back
- **Trigger:** Any purchase, request, quiz answer, or humming outcome
- **Purpose:** His face is the shop's entire feedback system
- **Audio Sync:** Sigh / approval hum / pained noise, matched per reaction
- **Performance Optimization:** None needed

### Rare Stock Reveal:
- **Duration:** 1.2 seconds, single play
- **Frames:** 2 (drawer locked → drawer open) + dust puff
- **Pattern:** Drawer slides, dust rises, premium items visible
- **Trigger:** Reaching Patron of the Arts (100 Sovs), or a correctly hummed obscure piece
- **Purpose:** The reward for being taken seriously
- **Audio Sync:** Drawer slide, then a beat of silence before he speaks
- **Performance Optimization:** Dust puff cut on Low LOD

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cart outline | set at sheet layout | 192x128 | Primary interactable high-contrast frame |
| Herr Notenschreiber outline | set at sheet layout | 48x96 | Vendor silhouette, thick rim |
| Rare-stock drawer outline | set at sheet layout | 64x64 | Patron-gated interactable |
| Metronome outline | set at sheet layout | 32x64 | Tempo reference visibility |
| Shop panel high-contrast frame | set at sheet layout | 160x96 | Increased border weight |
| Item icon outlines (all 15) | set at sheet layout | varies | White-rim variants for menu legibility |
| Manuscript pile outline | set at sheet layout | 96x64 | Avalanche hazard marker |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static paper frame | (0, 152) | 64x40 | No flutter; sheets held |
| Static metronome frame | (64, 152) | 48x40 | Arm held; tick conveyed by glyph only |
| Reduced dust density variant | (112, 152) | 48x40 | Minimal ambient motion |
| Non-scrolling backdrop frame | set at sheet layout | 512x128 | Parallax disabled variant |
| Avalanche, static collapsed state | set at sheet layout | 128x128 | Skips the 16-page burst entirely |
| Static ink drip | set at sheet layout | 16x32 | Final frame only |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Metronome tick glyph | (144, 96) | 32x32 | Fires on every tick — the location's constant audio |
| Page rustle glyph | (176, 96) | 32x32 | Fires on paper flutter and page turns |
| Discordant sting glyph | (0, 96) | 32x32 | Fires on every bad-humming sting |
| Pleasant resolution glyph | (32, 96) | 32x32 | Fires on every good-humming resolution |
| Three-note recognition glyph | (96, 96) | 48x32 | Fires the instant he identifies a tune |
| Pain glyph | (64, 96) | 32x32 | Fires on his pained noises |
| Sigh glyph | (0, 128) | 24x24 | Fires on every weary exhale |
| Approval hum glyph | (24, 128) | 24x24 | Fires on his "hmm" of approval |
| Purchase chime glyph | (48, 128) | 48x24 | Fires on sale confirmation |
| Ban buzzer glyph | (208, 96) | 48x32 | Fires on the ten-minute lockout |
| Humming waveform, correct | (160, 152) | 48x40 | **The mini-game's core feedback is a contour shape, not a sound** |
| Humming waveform, wrong | (208, 152) | 48x40 | Jagged, unresolved contour |

### Colorblind Considerations:
- **The humming mini-game is fully playable without audio or colour:** the pitch target closes by geometry, and correct/wrong is carried by waveform contour (smooth-resolved vs. jagged-unresolved)
- The Judgment Bar fills by pattern (solid = approval, hatched = tolerated, cross-hatched = offence), never by hue
- Correct/Wrong interpretation markers are shape-coded (resolved circle vs. cracked circle)
- Discount and price-increase tokens differ by arrow direction and border geometry, not colour
- Item sprites are distinguishable by paper format (sheet / folded / folio / scroll / parcel) before colour
- Patron tier is communicated by pip count and text, never hue
- Touch zones minimum 44px for item rows, tune selection chips, the pitch slider, and the selfie prompt

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) for environment and characters; uncompressed for `composers_cart_items.png` and `composers_cart_ui.png` — paper-format silhouettes and notation detail must stay legible at inventory scale, with alpha across all sheets
- **Fallback:** PNG high quality for `composers_cart_props.png` — fine notation and foxing gradients degrade badly under aggressive compression

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| composers_cart_environment | tileset, props | 1024x1024 |
| composers_cart_characters | Herr Notenschreiber, performers & bros | 512x512 |
| composers_cart_items_fx | items, effects, UI | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Three paper-flutter emitters, dust motes, daylight shaft, ink drips, full metronome cycle, 16-page avalanche burst, two parallax layers |
| Medium | Two flutter emitters, halved dust density, daylight shaft retained, 8-page avalanche, one parallax layer |
| Low | One static pinned surface, no dust, no ink drips, static metronome + tick glyph, 4-page avalanche, no parallax. **Vendor reaction frames and all humming-mini-game feedback are retained at every LOD — they are the content** |

### Performance Targets:
- **Target FPS:** 60 (game-wide standard; location profile predates the 60 FPS ruling)
- **Max Draw Calls:** 10 per frame (per location profile)
- **Memory Footprint:** 25 MB maximum (per location profile)
- **Particle Limit:** 16 (paper flutter 6, dust 4, ink 2, avalanche 16 — the avalanche temporarily suspends all ambient emitters rather than adding to the count)

### Performance Notes:
- Single-scene location; no sub-scenes, no on-demand loading required
- The backdrop is two parallax strips from the tileset sheet, not separate textures — one environment atlas bind
- Distant busker silhouettes are baked into the near-parallax strip, not spawned as sprites
- Street-performer NPCs cap at 2 concurrent sprites; the cat is a 2-frame ambient sprite that costs nothing
- Paper flutter emitters share one texture region and one material — three emitters, one draw call

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- `TileMap` for street/façade tiles; `ParallaxBackground` with two `ParallaxLayer` nodes for the MusikGasse backdrop
- `AnimatedSprite2D` for Herr Notenschreiber (22 states) and the metronome
- `Sprite2D` pool (max 2) for street performers; 1 ambient cat sprite with 2 frames
- `CPUParticles2D` (not GPU) for paper flutter, dust motes, ink drips, and the avalanche burst
- `CanvasLayer` for the shop panel, humming mini-game, patron track, and ban timer
- Cart state machine: `browsing → item_selected → purchase | request | quiz`; a parallel `humming` state can interrupt from any node and resolves to `discount | neutral | price_increase | ban`
- Humming controller: pitch input → tune identification (3 notes) → accuracy scoring → outcome table (Für Elise basic/wrong, Mozart correct/wrong, obscure correct/wrong, made-up, copyrighted). The made-up-tune branch sets a quest-trigger flag
- Ban state locks all shop interaction for 10 in-game minutes and drives the Ban Timer Ring; the vendor sprite remains present and visibly unmoved
- Patron controller persists `total_spent`; 100 Sovs unlocks the Rare-Stock Drawer, a permanent 10% discount, name recognition, specific-composition requests, and limited humming permission

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Metronome arm extremes | Tick | Every 0.5s (60 BPM cycle) |
| Paper flutter emitter cycle | Paper rustle | Continuous bed, peak on loudest emitter |
| Three-note identification | Sharp "hmm" of recognition | On the third note |
| Judgment bar fill | *(silence)* | 1.5s — the pause is the joke |
| Reaction frame, correct | Pleasant resolution chord | On frame in |
| Reaction frame, wrong | Discordant sting | On frame in |
| RAGE snap | Harsh discordant sting | On frame in |
| Ban issued | Ban buzzer | On final frame |
| Page turn | Page rustle | Per turn |
| Paper avalanche collapse | Cascade + one anguished vendor noise | On collapse frame |
| Purchase confirm | Chime | On confirmation |
| Rare-stock drawer | Drawer slide, then silence | Slide, 0.8s beat, then his line |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| "The Lost Opus" | Lost Manuscript sprite, rare-stock drawer, Lost Opus quest card, Retrieving From Chaos frame | Vendor seeks a specific rare manuscript (fetch quest) |
| "Correct Interpretation" | Tune cards, humming waveforms, Correct Interpretation quest card, Rare Respect frame | Learn a piece properly for a performance quest |
| "The Humming Champion" | All five tune cards, Judgment Bar, Humming Champion rosette | Pass every humming challenge |
| "Forbidden Music" | Forbidden Opus (wrapped), rare-stock drawer, RAGE frame | Acquire the banned composition (late game) |
| "Paper Avalanche" | Pile stable/toppling/collapsed, avalanche burst, Horrified frame, Bro Buried In Manuscripts | Knock over a manuscript pile |
| "Patron of the Arts" | Patron progress bar, patron badge, rare-stock unlock banner, discount badge | Spend 100 Sovs total |
| "Genuine Respect" | Rare Respect frame, approval hum glyph, achievement toast | Earn the vendor's approval |
| "Passed the Test" | Quiz panel, Quiz Pose frame, discount tokens | Correctly identify a piece |
| Selfie Spot — Standard | Cart with paper avalanche visible, sheet-music-upside-down prop, caption "Cultured" | Any visit |
| Selfie Spot — "The Scholar" | Folio open (read correctly), Nod Of Approval frame, caption "He Didn't Cringe" | Requires passing a humming test |
| Selfie Spot — "Paper Avalanche" | Bro Buried In Manuscripts, Horrified frame, caption "I Touched Something" | Requires failing to browse carefully |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| MusikGasse | Shared district façade tiles, backdrop strips, busker silhouettes, cross-location signposts | Standard street transition |
| The Bassline Opera House | Manuscripts contain boss-fight hints; Tempo Guide and Conductor's Notes buff its rhythm combat | None (item carry-over) |
| Mozart's Last Rave | "Lost Manuscript" connects to Bassmeister lore; Rare LP cross-reference card points to the Vinyl Hunt in the Requiem Room | None (lore + item flag) |
| The Moderato Pub | Tempo-debate participants shop here; shared MusikGasse regulars | None (NPC crossover) |
| Café Existenz | Intellectual customers referenced in the vendor's recommendations | None (dialogue flag) |
| Grounds For Concern | Caffeine tremor narrows rhythm windows that his manuscripts widen — the two vendors' buffs interact | None (status interaction) |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A paper avalanche with a filing system only one man understands"
- **Color Mood:** Parchment cream and aged paper under natural daylight, with ink black as the only hard value in the scene and musical gold reserved for what he considers precious
- **Lighting:** Flat natural daylight from screen-left, catching paper edges and turning stacked manuscripts translucent at the rim; long shadows from the piles across the cobbles
- **Texture:** Foxed paper, ink absorption, worn leather spines, sun-bleached portrait gilt, chalk dust, and one wooden cart worn smooth where his hands go

### Environmental Storytelling:
- The cart looks like collapse waiting to happen, and the vendor retrieves any item from it instantly — the art must make both true at once
- Three faded, anonymous composer portraits hang in gilt frames; one has cracked glass that was never repaired
- A chalk tally of humming offences runs down the cart's side, going back years
- A wall poster for a "Für Elise Recital" hangs across the street; he has not looked at it in a long time
- The metronome ticks at 60 BPM — unhelpfully slow, permanently disapproving
- A cat sleeps on a stack of folios and is permitted to
- Prices are posted, plain, and fair. He is not a scammer, just disappointed
- His coat hangs on a hook with ink-marked cuffs; the stool is worn to his shape

### Character Integration Notes:
- **Herr Notenschreiber's gatekeeping is grief, not superiority.** Every pained frame must read as a man being hurt by something he loves, not a man looking down on you
- He is ancient and physically small; compose him dwarfed by his own stock
- Ink-stained fingers and thick spectacles must appear in all 22 frames — they are the 48px silhouette
- The Flicker Of Hope frame is the emotional centre of the sheet: it is what he looks like when he thinks someone might understand
- Street performers are lower-contrast than the vendor; the eye goes to the paper, then to him
- Bradley's Quiet Bach frame is the only composed bro posture in the location

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Bradley's Bach** — the vendor stopping mid-criticism, and a 15% discount landing on the one bro who paid attention during lessons
2. **The paper avalanche** — a bro buried to the shoulders in manuscripts with the vendor horrified behind him
3. **The RAGE frame** — "A BILLION people can be WRONG."
4. **The chalk tally of offences** running down the cart side, in the same crop as the "Please Do Not Hum" sign
5. **The Flicker Of Hope** — a single frame of an old man daring to believe someone might know what a minor key is
6. **Lord Pilsner's "Dun dun dun DUNNN!"** with the vendor's response in frame

### Quote Potential:
- "Please Do Not Hum. We Will Know If It's Wrong." - cart signage
- "Welcome to The Composer's Cart. Please tell me you know the difference between major and minor keys." - Herr Notenschreiber
- "You want Mozart? EVERYONE wants Mozart. Fine. Which Mozart? There are HUNDREDS of pieces." - Herr Notenschreiber
- "That wasn't music. That was... sound. Organized poorly." - Herr Notenschreiber
- "...You have taste. This is unexpected. Refreshing, even." - Herr Notenschreiber
- "That is NOT music. That is FOUR CHORDS repeating. Please. I beg you. Stop." - Herr Notenschreiber
- "A BILLION people can be WRONG." - Herr Notenschreiber
- "Please leave the 'dun duns' to the professionals." - Herr Notenschreiber
- "Your friends are... unfortunate. But YOU. You may have 15% off." - Herr Notenschreiber
- "You seem like a Beethoven player. Aggressive. Dramatic. Here." - Herr Notenschreiber
- "I paid attention during lessons." - Bradley

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | composers_cart_tileset.png | 1024x512 |
| 2 | composers_cart_props.png | 512x256 |
| 3 | herr_notenschreiber.png | 384x288 |
| 4 | composers_cart_npcs.png | 384x192 |
| 5 | composers_cart_items.png | 256x256 |
| 6 | composers_cart_effects.png | 256x192 |
| 7 | composers_cart_ui.png | 256x288 |

**Total Estimated Memory:** ~4.1 MB (1,028,096 px uncompressed RGBA); ~1.1 MB after VRAM compression — comfortably inside the 25 MB profile budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `composers_cart_tileset.png` (1024x512)
- [ ] `composers_cart_props.png` (512x256)
- [ ] `herr_notenschreiber.png` (384x288)
- [ ] `composers_cart_npcs.png` (384x192)
- [ ] `composers_cart_items.png` (256x256)
- [ ] `composers_cart_effects.png` (256x192)
- [ ] `composers_cart_ui.png` (256x288)

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
- **Documentation:** Animation timing reference sheet + parallax layer guide (two strips, 0.25x / 0.6x) + manuscript-pile three-state alignment guide + **notation clearance note (all drawn notation must be invented and non-recognisable)**

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (including the two derived tones, flagged in the palette table)
- [ ] **No drawn notation anywhere on any sheet is a recognisable real melody at any zoom level** — all notation is invented
- [ ] The three faded composer portraits are anonymous; no real composer likeness is used
- [ ] The cart reads as chaotic *and* navigable — a viewer should believe the vendor can find anything in it
- [ ] Manuscript Pile Stable / Toppling / Collapsed share a base silhouette and align across all three states
- [ ] Pinned Sheet Music Surfaces A/B seam-match the fluttering frame replacements exactly
- [ ] Ink-stained fingers and thick spectacles appear in all 22 Herr Notenschreiber frames
- [ ] **Every pained vendor frame reads as grief, not contempt**
- [ ] The Flicker Of Hope frame is distinguishable from Nod Of Approval and Rare Respect
- [ ] Item sprites are distinguishable by paper format at 32px without colour
- [ ] Humming waveform contours (smooth-resolved vs. jagged-unresolved) are legible in monochrome
- [ ] The chalk tally of offences is present and reads as years old
- [ ] Accessibility visual alternatives included for all audio cues — including the constant metronome tick
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (classical gatekeeping, "correct interpretation" culture) is clear throughout
- [ ] Prices read as fair and posted — he is not a scammer, and the art must not imply one
- [ ] The humming mini-game is fully playable without audio or colour
- [ ] Hidden content (rare-stock drawer, Forbidden Opus, made-up-tune quest trigger) has discoverable visual cues
- [ ] Performance optimized (CPU particles only, 10-draw-call ceiling, three atlas binds, baked busker silhouettes)
- [ ] Touch zone sizing considered (44px minimum for item rows, tune chips, pitch slider, selfie prompt)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia and MusikGasse only; Sinfonian musical-heritage obsession evoked, no real place named. Composer portraits are anonymous and unnamed |
| Cultural Specificity | ✅ | Sinfonia's musical heritage obsession, conservatory adjacency, street-performer district culture, "correct interpretation" orthodoxy |
| Satirical Targets Appropriate | ✅ | Music snobbery and one-upmanship, and the bros' cheerful ignorance; the vendor is a genuine expert broken by decades of tourists, never a national stereotype, and the satire protects music education |
| Seedy Underbelly Present | ❌ | Profile explicitly rules it out: "Prices remain fair (he's not a scammer, just disappointed)." No vice or exploitation operation exists here. Nearest element is a ten-minute humming ban, which costs nothing. Flagged for owner — this location is intentionally benign |
| Gameplay Value Established | ✅ | 13-item rhythm-buff shop across three tiers, humming mini-game with eight outcomes, Patron of the Arts progression, quiz and request systems, four quests, six achievements, three selfie variants |
| Technical Feasibility | ✅ | Seven sheets, three atlases, three LOD tiers, no sub-scenes, baked parallax buskers, CPU particles only |
| Performance Budget | ✅ | 60 FPS / 10 draw calls / 25 MB taken verbatim from the profile's stated budget. Normalized to the game-wide 60 FPS standard (author ruling); effect density must be tuned to hold it|
| Accessibility Features | ✅ | Visual glyphs for all twelve audio cues including the constant metronome tick; the humming mini-game is fully playable without audio or colour via waveform contour; static/reduced-motion variants for flutter, metronome, dust, ink, avalanche, parallax |
| No Crypto Elements | ✅ | None present, and the profile explicitly confirms "No crypto elements (Pure musical snobbery)" |
| Social Media Integration | ✅ | Three documented selfie variants with unlock conditions, six screenshot moments, eleven quotable lines |

**The Composer's Cart: a collapsing tower of paper with a filing system only one man understands — where three notes are enough for him to name your piece, tell you what you did to it, and mean every word out of love.**
