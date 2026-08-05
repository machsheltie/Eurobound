# The Pancake House - Complete PNG Asset Requirements

## 📋 Overview
The Pancake House serves genuinely excellent Dutch pannenkoeken to Americans who ordered pancakes, on a canal, at canal prices, with a bread basket nobody asked for. This document specifies every PNG asset for the restaurant: the Delft-framed canal house exterior, the manufactured rustic interior, the terrace with its unadvertised 2 Sovs/hour heaters, the open kitchen pass where Jan makes one plate-sized pancake every two minutes, the multi-page laminated menu that requires a translation guide (2 Sovs, also on the menu), Marleen's knowing smile, Jesse's spek explanation, and the moment the bill says sixty-four Sovs. Its satirical essence in a sentence: nobody is scamming anybody, the food is good, and the word "pancake" has betrayed you.

**Location ID:** `shamsterdam_canalring_pancake_house_01`
**Theme:** American food expectations meeting Dutch reality — a cultural mismatch monetised at waterfront rates
**Zone:** Canal Ring Promenade, premium waterfront location
**Hours:** 8 AM - 10 PM (breakfast rush 8-11 AM is peak expectation collision)
**Primary Function:** Restaurant / ordering-and-billing puzzle — multi-page menu navigation, hidden-cost bill calculation, the Portion Revelation, the Syrup Situation, the Spek Specificity Problem, and the permanent Expectation Adjustment buff

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Dutch Blue | #1E90FF | Delft tiles, checkered cloths, door, signage |
| Butter Yellow | #FFD700 | Batter, pancake surfaces, warm lighting, sign |
| Delft White | #F5F5F5 | Tile ground, plates, tablecloth base |
| Wood Brown | #8B4513 | Beams, tables, floorboards, clogs |
| Copper Warm | #B87333 | Ceiling pans, griddle rims, decorative metal |
| Canal Gray-Green | #5F7A6E | Water, boats, exterior daylight cast |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/pancake_house/
├── environment/
│   ├── pancake_house_interior_main.png
│   ├── pancake_house_terrace.png
│   └── pancake_house_fixtures.png
├── objects/
│   └── pancake_house_food.png
├── npcs/
│   ├── npc_pancake_house_staff.png
│   └── npc_pancake_house_customers.png
├── effects/
│   └── pancake_house_effects.png
└── ui/
    └── pancake_house_ui.png
```

---

## 🏠 Sprite Sheet 1: Main Dining Room Background
**File:** `pancake_house_interior_main.png`
**Dimensions:** 1920x1080 pixels (standalone full-scene background — not atlased)
**Color Palette:** #8B4513, #1E90FF, #F5F5F5, #B87333

### Scene Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Interior Backdrop | (0, 0) | 1920x1080 | Full scene: two-floor canal house dining room, exposed beams, copper pans hanging decoratively from the ceiling, blue-checkered tables with a windmill miniature on each, Delft tile displays along the left wall, steep Dutch stairs rear-left, the open kitchen pass across the right third with Jan visible behind it, "As Featured In" clippings (2009-2014) by the till, fake tulips in Delft vases |

### Technical Notes:
- Anchor points (document in layer names): kitchen pass at (1472, 448), till at (1728, 640), stairs at (256, 384), table slots at (512, 768) / (832, 768) / (1088, 832) / (448, 960), Delft tile wall at (128, 512), terrace door at (1856, 704)
- Lighting is warm and deliberately "rustic," which is to say carefully manufactured; the warm interior wash overlay (Sheet 7) sits on top and can be dialled per time-of-day
- The kitchen pass opening is authored as an alpha cutout so Jan's griddle frames and the kitchen steam (Sheets 5 & 7) composite behind the pass frame
- Every visible table has a windmill miniature painted in; the 15 Sovs breakage fee is never signposted anywhere in the room
- Copper pans must read as unmistakably unused — no soot, no wear, perfect polish

---

## 🌊 Sprite Sheet 2: Terrace & Canal Background
**File:** `pancake_house_terrace.png`
**Dimensions:** 1920x1080 pixels (standalone full-scene background — not atlased)
**Color Palette:** #5F7A6E, #1E90FF, #F5F5F5, #8B4513

### Scene Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Terrace Backdrop | (0, 0) | 1920x1080 | Full scene: canal-side terrace, four tables under the awning, patio heaters standing between them, canal railing across the lower-middle, water and the opposite bank filling the upper half, boats moored and passing, ducks working the railing line, other tourists taking the identical photograph |

### Technical Notes:
- Anchor points: heater slots at (384, 640) / (960, 640) / (1536, 640), table slots at (512, 768) / (1024, 768) / (1472, 800), railing run at (960, 896), boat lane at (960, 320), duck patrol at (704, 928), interior door at (128, 576)
- The canal band (y 0-512) is authored with a clean horizontal seam so the passing-boat sprites (Sheet 3) can scroll across it without a parallax layer
- Heaters are painted unlit; the heater glow overlay (Sheet 7) activates only when the fee is actually running
- Every other terrace table has a tourist in mid-photograph; the composition must communicate that this exact photo is being taken forty times an hour
- No price signage anywhere on the terrace — the absence is the point

---

## 🪟 Sprite Sheet 3: Exterior, Décor & Fixtures
**File:** `pancake_house_fixtures.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #1E90FF, #FFD700, #8B4513, #B87333

### Exterior & Kitchen:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pancake House Exterior | (0, 0) | 384x512 | Charming canal house, Delft tile door frame, windmill decorations, tourist magnetism maximum |
| Kitchen Pass View | (384, 0) | 384x256 | Open concept: watch "the magic," which is an assembly line running at industrial efficiency |
| Copper Pans Ceiling Run | (384, 256) | 384x128 | Tileable horizontal run, decorative only, never used |
| Wooden Beams Ceiling Run | (384, 384) | 384x128 | Tileable horizontal run, rustic aesthetic |
| Menu (Physical, Multi-Page) | (768, 0) | 192x384 | Laminated, five languages, overwhelming, translation guide 2 Sovs (also on the menu) |
| Golden Pancake Sign | (960, 0) | 64x128 | Hanging sign, pancake-shaped, gold |
| Windmill Logo | (960, 128) | 64x128 | Folksy branding element |
| Delft Door Frame | (960, 256) | 64x128 | Blue tile surround |
| Chalkboard Special | (768, 384) | 192x128 | "TODAY'S SPECIAL: Bacon & Stroop 17 Sovs" |
| Blue Door | (960, 384) | 64x128 | The entrance, "FAMILIES WELCOME" plate at eye level |

### Interior Décor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Delft Tile Wall (Tileable) | (0, 512) | 256x256 | Some authentic, most reproductions, seamless all edges |
| Table Setting (Blue Checkered) | (256, 512) | 256x192 | Cloth, cutlery, windmill mini, small Dutch knife |
| Wooden Shoes Shelf | (512, 512) | 128x96 | Obviously |
| Vintage Cheese Posters | (640, 512) | 192x256 | Dutch advertising, genuinely handsome |
| Antique Pancake Griddle (Display) | (832, 512) | 192x128 | On display; modern ones do the actual work |
| Tulips in Delft Vase (Fake) | (512, 608) | 128x96 | Good fakes. Very good fakes. |
| "As Featured In" Clippings | (832, 640) | 192x128 | 2009-2014. Nothing recent. |
| Windmill Miniature (Table) | (256, 704) | 64x64 | Don't touch. 15 Sovs if broken. Unsignposted. |
| "Traditional Pancake Making" Photos | (320, 704) | 192x64 | Stock photos. Definitely stock photos. |
| Steep Dutch Stairs | (512, 704) | 128x64 | To the second dining floor, at an angle that surprises everybody |

### Terrace & Kitchen Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Terrace Heater | (0, 768) | 64x128 | 2 Sovs/hour. Not advertised. Warm. |
| Terrace Table + Chairs | (64, 768) | 192x128 | Premium seating, premium pricing |
| Canal Railing (Tileable) | (256, 768) | 128x64 | Seamless horizontal run |
| Reservation Sign | (384, 768) | 128x64 | "Recommended" during peak; walk-ins "tolerated" |
| Card Machine | (512, 768) | 64x64 | Card accepted, cash preferred |
| Bread Basket Stand | (576, 768) | 64x64 | Where the 4 Sovs lives before it arrives |
| Restaurant Floor Tile (Tileable) | (640, 768) | 128x128 | Worn canal-house board, seamless all edges |
| Kitchen Griddle (Working) | (768, 768) | 128x128 | Large circular, actual equipment |
| Batter Dispenser | (896, 768) | 128x128 | Portion controlled. Cost controlled. |
| Duck (Aggressive Beggar) | (256, 832) | 64x64 | Working the railing line |
| Duck (Wings Up) | (320, 832) | 64x64 | Escalation frame |
| Canal Boat (Passing) | (384, 832) | 192x64 | Scrolls across the canal band |
| Duck (Swimming) | (576, 832) | 64x64 | Off-duty |

### Service Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Chef's Pass Window | (0, 896) | 64x128 | Frame element with alpha cutout |
| Napkin & Cutlery Caddy | (64, 896) | 192x128 | Table service kit |
| Small Dutch Knife | (256, 896) | 64x64 | Genuinely smaller than Americans expect; the sound is different too |
| Bill Presenter Folder | (320, 896) | 64x64 | Leather, heavy, ominous |
| Heater Fee Notice | (384, 896) | 192x128 | Exists. Is on the menu. Is on page six. |
| Topping Station (Pre-Portioned) | (576, 896) | 64x128 | Cost controlled, visible through the pass |
| Grill Steam Vent | (640, 896) | 128x128 | Kitchen extraction, always running |
| Open-Concept Pass Counter | (768, 896) | 256x128 | The counter the plates land on, and where eye contact happens |

### Technical Notes:
- Delft Tile Wall, Canal Railing, Restaurant Floor Tile, Copper Pans Run, and Wooden Beams Run must all seam cleanly; they are the location's five tiled assets
- The Menu prop is baked at 2x internal resolution and flagged for the uncompressed-texture exception list — the multi-page menu is a readable puzzle object, not set dressing
- Canal Boat sprite scrolls at a fixed rate across the terrace canal band; one instance active at a time, recycled
- Heater Fee Notice is authored fully readable and is genuinely present in the scene; the joke is placement, not concealment

---

## 🥞 Sprite Sheet 4: Food & The Bill
**File:** `pancake_house_food.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #FFD700, #F5F5F5, #8B4513, #1E90FF

### The Pancakes (Plate-Sized, Thin, One Per Plate):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kaaspannenkoek (Cheese) | (0, 0) | 128x128 | 14 Sovs base — "Classic choice." Cheese Sweats risk. |
| Spekpannenkoek (Bacon) | (128, 0) | 128x128 | 15 Sovs base — cubes, not strips. "Dutch bacon. Very good." |
| Appelpannenkoek (Apple) | (256, 0) | 128x128 | 15 Sovs base — the actual best one, and nobody orders it first |
| "American Style" Stack | (384, 0) | 128x128 | 22 Sovs — three small ones. Still thin. Closest to expectations. |

### Condiments & Extras:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Syrup Pitcher (Small) | (0, 128) | 48x64 | 3 Sovs for more. Same pitcher. It's concentrated. |
| Stroop Container | (48, 128) | 48x64 | Dutch syrup, thicker, less maple, genuinely excellent |
| Whipped Cream Can | (96, 128) | 32x64 | 4 Sovs. "Fresh. From the can." |
| Bread Basket | (128, 128) | 96x64 | Complimentary to receive. Not complimentary to keep. 4 Sovs. |
| Receipt (Itemised) | (224, 128) | 96x64 | Line by line, all correct, all surprising |
| Spek Cubes (Close-Up) | (320, 128) | 64x64 | The specificity problem, rendered |
| Cutlery + Coffee Pair | (384, 128) | 64x64 | Small Dutch knife, small cup |
| Kid's Pancake | (448, 128) | 64x64 | 12 Sovs. Same pancake. Smaller plate. |

### Bill, States & Icons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Toppings Array | (0, 192) | 192x64 | Six 32x64 topping units, each individually priced |
| Bill / Receipt (The 64 Sovs Reveal) | (192, 192) | 96x64 | Long-format bill; the total sits at the bottom where it can be seen coming |
| Empty Plate | (288, 192) | 64x64 | Clean-finish state, no complaint, +Bravado |
| Half-Eaten Pancake | (352, 192) | 64x64 | Mid-meal state — it is, in fact, very filling |
| Pancake Inventory Icon | (416, 192) | 32x32 | Item icon |
| Syrup Icon | (448, 192) | 32x32 | Item icon |
| Bread Basket Icon | (480, 192) | 32x32 | Item icon |
| Expectation Adjustment Icon | (416, 224) | 32x32 | Small-arrow-recalibrating silhouette |
| Cheese Sweats Icon | (448, 224) | 32x32 | Droplet-over-wedge silhouette |
| Confused Icon | (480, 224) | 32x32 | Spiral silhouette |

### Technical Notes:
- All four pancake sprites are drawn at the same 128x128 plate footprint with visibly different toppings and the *same thinness* — the Portion Revelation depends on the plate being full and the food being flat
- The American Style Stack must still read as three thin discs; it is closer to expectations, not equal to them
- Syrup Pitcher is drawn at genuine scale relative to the plate: it is small, and it is going to stay small
- Spek Cubes close-up is used as an inset during Jesse's explanation; it must read as appetising, because the food is good — only the expectation is wrong

---

## 👩‍🍳 Sprite Sheet 5: Restaurant Staff
**File:** `npc_pancake_house_staff.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 per character frame; 128x128 per portrait
**Color Palette:** #1E90FF uniform accents, #F5F5F5, #8B4513

### Hostess Marleen — Expectation Management (Attempting):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marleen Idle | (0, 0) | 64x96 | Dutch, traditional dress (authenticity theatre, required), professional smile |
| Marleen Greeting | (64, 0) | 64x96 | "Table inside or terrace?" |
| Marleen Menu Provision | (128, 0) | 64x96 | Menu handed over with both hands, like a warning |
| Marleen "Terrace has... beautiful view." | (192, 0) | 64x96 | The pause is doing work |
| Marleen Pointing at Photos | (256, 0) | 64x96 | "Yes, that is actual size. One pancake per plate." |
| Marleen Knowing Smile F1 | (320, 0) | 64x96 | It begins |
| Marleen Knowing Smile F2 | (384, 0) | 64x96 | It lands |
| Marleen "Of course. Enjoy your meal." | (448, 0) | 64x96 | She tried. She genuinely tried. |

### Server Jesse — Explanation Duty:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Jesse Idle | (0, 96) | 64x96 | Young, efficient, traditional Dutch vest (uniform requirement) |
| Jesse Order Taking | (64, 96) | 64x96 | Pad out, helpful, not responsible for your expectations |
| Jesse Spek Explanation F1 | (128, 96) | 64x96 | "The bacon is spek. Cubes." |
| Jesse Spek Explanation F2 | (192, 96) | 64x96 | "Traditional. Not strips. Is that okay? ...I'll bring the spek." |
| Jesse Syrup Explanation | (256, 96) | 64x96 | "Maple-FLAVOURED. Yes." |
| Jesse Bread Basket Clarification | (320, 96) | 64x96 | "Complimentary to receive. Not complimentary to keep. Four Sovs." |
| Jesse Bill Delivery | (384, 96) | 64x96 | Brief pause for reaction preparation |
| Jesse Internal Struggle | (448, 96) | 64x96 | Thought-bubble frame: "Explaining spek is my cardio." |

### Portraits & Chef Jan:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marleen Portrait (Dialogue) | (0, 192) | 128x128 | Patient, experienced, has seen every reaction |
| Jesse Portrait (Dialogue) | (128, 192) | 128x128 | Helpful but not liable |
| Jan Portrait (Dialogue) | (256, 192) | 128x128 | Chef whites, tall hat (theatrical), quietly proud |
| Jan Chef Idle (Through Pass) | (384, 192) | 64x96 | Framed by the pass cutout |
| Jan Griddle Work Frame 1 | (448, 192) | 64x96 | Batter poured |
| Reserve / Atlas Padding | (384, 288) | 128x32 | Reserved strip, do not paint |

### Kitchen & Service Motion:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Jan Griddle Work Frame 2 | (0, 320) | 64x96 | Spread across the griddle |
| Jan Griddle Work Frame 3 (Flip) | (64, 320) | 64x96 | The flip. One every two minutes. Forever. |
| Jan Professional Nod | (128, 320) | 64x96 | Occasional eye contact, then back to production |
| Jan Plating | (192, 320) | 64x96 | Toppings arranged from the pre-portioned station |
| Jesse Carrying Plates | (256, 320) | 64x96 | Two plates, one arm, no drama |
| Jesse Terrace Route | (320, 320) | 64x96 | Through the door, past the heaters |
| Marleen Seating Guests | (384, 320) | 64x96 | Table assignment, menu placement |
| Marleen Reservation Check | (448, 320) | 64x96 | "Recommended." "Tolerated." |

### Bill Handling & Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marleen High-Contrast Silhouette | (0, 416) | 64x96 | Accessibility outline variant |
| Jesse High-Contrast Silhouette | (64, 416) | 64x96 | Accessibility outline variant |
| Jesse Contest-Charges Response | (128, 416) | 64x96 | Every charge is legitimate. He will explain each one. |
| Jesse Small Discount Concession | (192, 416) | 64x96 | Bravado success outcome; slightly embarrassed for both of you |
| Accessibility Reserve Block | (256, 416) | 256x96 | Reserved for high-contrast/audio-cue glyph overflow |

### Technical Notes:
- Jan's three griddle frames loop continuously behind the pass whenever the interior scene is loaded — the kitchen is always producing, at exactly the profile-specified rate
- Marleen's two Knowing Smile frames are a crossfade, not a pop; the smile must arrive rather than appear
- No staff frame may read as smug, contemptuous, or predatory. They are patient people running a legitimate restaurant, and that is what makes the bill land.

---

## 👥 Sprite Sheet 6: Customers
**File:** `npc_pancake_house_customers.png`
**Dimensions:** 1024x256 pixels
**Sprite Size:** 64x96 per single NPC frame; 128x128 per portrait
**Color Palette:** Mixed tourist palette, warm-interior ambient grade

### Diners:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| American Family (Just Received Food) | (0, 0) | 192x96 | Four people, four plates, one universal expression |
| American Dad Doing Math | (192, 0) | 64x96 | The bill has not arrived yet. He is preparing. |
| Kid Asking "Where's the Syrup" | (256, 0) | 64x96 | The pitcher is right there. It is the pitcher. |
| Dutch Couple (Regulars) | (320, 0) | 128x96 | Eating normally, finished before the tourists processed their order |
| Food Blogger (Ring Light) | (448, 0) | 64x96 | Ten minutes of setup, cold pancake, worth it |
| Food Blogger (Repositioning) | (512, 0) | 64x96 | "Again. The light isn't right." |
| Backpacker Who's Been Warned | (576, 0) | 64x96 | Ordered the apple. Smug. Correct. |
| Bros Trio Seated | (640, 0) | 192x96 | Lord Pilsner / Chadwick / Bradley, pre-composed |
| Terrace Diner A | (832, 0) | 64x96 | Photographing the canal |
| Terrace Diner B | (896, 0) | 64x96 | Photographing the same canal |
| Waiting Party (Doorway) | (960, 0) | 64x96 | Walk-in, being tolerated |

### Portraits & Reaction Strips:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| American Family Portrait | (0, 96) | 128x128 | "These are the pancakes? The whole—this is it?" |
| Food Blogger Portrait | (128, 96) | 128x128 | Chadwick sees himself, feels seen, feels attacked |
| Backpacker Portrait | (256, 96) | 128x128 | "You guys should've gotten the apple. It's actually great." |
| Dutch Couple Portrait | (384, 96) | 128x128 | Satisfied. Unbothered. Correct. |
| Portion Reaction Strip | (512, 96) | 256x96 | Four 64x96 stages: anticipation / arrival / confusion / acceptance |
| Bill Reaction Strip | (768, 96) | 192x96 | Three 64x96 stages: reading / recalculating / paying |
| Photographing Pose Strip | (960, 96) | 64x96 | Two 64x48 frames: phone raised / phone lowered |

### Ambient:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Seated Diner Silhouette Row | (512, 192) | 256x64 | Cheap table-depth for the far dining room |
| Terrace Silhouette Row | (768, 192) | 192x64 | Cheap depth for the outdoor tables |
| Accessibility Reserve | (960, 192) | 64x64 | Reserved for high-contrast marker |
| Portrait Band Padding | (0, 224) | 512x32 | Reserved padding, do not paint |

### Technical Notes:
- American Family, Dutch Couple, and Bros Trio ship as pre-composed single blocks to protect the 16-draw-call budget
- Portion Reaction Strip is palette-modulated onto any diner sprite and is the location's most reused asset
- The Dutch Couple must always be visibly further through their meal than any tourist party in frame; this timing gag is set-dressing, not scripted

---

## ✨ Sprite Sheet 7: Effects — Kitchen, Canal & Consequences
**File:** `pancake_house_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #FFD700, #F5F5F5, #5F7A6E, #B87333

### Kitchen & Food:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Kitchen Steam Frame 1 | (0, 0) | 64x64 | Griddle steam, first rise |
| Kitchen Steam Frame 2 | (64, 0) | 64x64 | Dispersal |
| Butter Sizzle Sparkle | (128, 0) | 64x64 | Batter meeting hot iron |
| Griddle Heat Shimmer | (192, 0) | 64x64 | Painted haze band, no distortion shader |
| Batter Pour Arc | (256, 0) | 64x64 | Dispenser to griddle, portion controlled |
| Syrup Pour Stream | (320, 0) | 64x64 | The whole pitcher, which is not a lot |
| Powdered Sugar Fall | (384, 0) | 64x64 | Sweet pancake finishing dust |
| Candle Flicker (Electric) | (448, 0) | 64x64 | Safety-compliant ambience |

### Canal & Consequence:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Canal Breeze Ripple | (0, 64) | 64x64 | Surface motion, terrace only |
| Boat Wake | (64, 64) | 64x64 | Trails the passing boat sprite |
| Duck Splash | (128, 64) | 64x64 | Begging escalation |
| Heater Glow (Terrace) | (192, 64) | 64x64 | Warm. 2 Sovs/hour. Running right now. |
| Ring Light Bloom (Blogger) | (256, 64) | 64x64 | Character-parented, obnoxious, accurate |
| Card Machine Beep Flash | (320, 64) | 64x64 | Transaction confirm |
| Bill Reveal Sting Plate | (384, 64) | 64x64 | A single small dramatic vignette on the bill folder |
| Portion Reveal Beat Plate | (448, 64) | 64x64 | Brief desaturation pulse the instant the plate lands |

### Grades & Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Warm Interior Wash | (0, 128) | 128x128 | Full-scene multiply plate, dining room |
| Terrace Daylight Wash | (128, 128) | 64x64 | Cooler, brighter, canal-reflected |
| Window Light Pool | (192, 128) | 64x64 | Natural light on the tables by the glass |
| Kitchen Pass Glow | (256, 128) | 64x64 | Warm spill through the pass cutout |
| Steam Rise (Tall) | (320, 128) | 64x64 | Vertical column over the extraction vent |
| Sizzle Glyph | (384, 128) | 32x32 | Mirrors the continuous kitchen sizzle |
| Cutlery Clink Glyph | (416, 128) | 32x32 | Mirrors the smaller-knife-on-plate sound |
| Boat Horn Glyph | (448, 128) | 32x32 | Mirrors the canal horn, terrace only |
| Duck Quack Glyph | (480, 128) | 32x32 | Mirrors aggressive begging |
| Card Beep Glyph | (128, 192) | 32x32 | Mirrors the card machine |
| Bill Sting Glyph | (160, 192) | 32x32 | Mirrors the total-reveal sting |
| Menu Page Turn Glyph | (192, 192) | 32x32 | Mirrors laminated page turns |
| Syrup Pour Glyph | (224, 192) | 32x32 | Mirrors the pour cue |
| Multilingual Murmur Glyph | (256, 192) | 32x32 | Persistent ambient-room indicator |
| Static Steam (Reduced Motion) | (288, 192) | 64x64 | Non-animating steam plate |
| Static Boats (Reduced Motion) | (352, 192) | 64x64 | Moored-only canal, no scroll |
| Static Kitchen (Reduced Motion) | (416, 192) | 64x64 | Jan holds a single plating frame |
| Reserve | (480, 192) | 32x64 | Reserved cell, do not paint |

### Technical Notes:
- The Portion Reveal Beat Plate is a 0.4-second desaturation pulse and nothing more — the joke is the food, not the effect
- Heater Glow renders only while the fee timer is actually accruing; this is the player's only in-world warning and it is a warm orange glow that looks like hospitality
- Boat Wake parents to the scrolling boat sprite; one instance at a time

---

## 🧭 Sprite Sheet 8: UI Elements
**File:** `pancake_house_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #1E90FF UI chrome, #F5F5F5 panel fill, #FFD700 highlights

### Menu & Ordering:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu Navigation UI (Multi-Page) | (0, 0) | 256x256 | Five-language laminated menu, page-turn interaction, base prices only |
| Page Tabs | (256, 0) | 256x64 | Four 64x64 tabs: Savoury / Sweet / "American Style" / Kids |
| Topping Extra Cost Indicator | (256, 64) | 128x32 | "+3 Sovs" per topping, appears only after selection |
| Terrace Heater Fee Reveal | (384, 64) | 128x32 | Surfaces on the bill, not at seating |
| Bread Basket Charge Notice | (256, 96) | 256x32 | "Complimentary to receive. Not complimentary to keep." |
| Order Confirm Panel | (256, 128) | 256x128 | Final selection with base price shown and nothing else |

### Bill & Consequence:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bill Breakdown Popup | (0, 256) | 256x192 | Line-by-line: base + toppings + terrace + bread + service = the number |
| Running Total Ticker | (256, 256) | 128x32 | Optional accessibility/assist mode: live total during ordering |
| Contest Charges Panel | (384, 256) | 128x96 | Bravado check; success yields a small discount, failure yields silence |
| Expectation Adjustment Status | (256, 288) | 128x64 | Permanent subtle buff; better menu reading everywhere afterwards |

### Photography & Status:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Food Photo Frame | (256, 352) | 128x96 | Overhead pancake shot; it genuinely looks good |
| Caption Choice Panel | (384, 352) | 128x96 | "Dutch pancakes!" / "Basically a crepe" / "Amazing!" |
| Status Icon Row | (0, 448) | 128x32 | Four 32x32: Expectation Adjustment / Cheese Sweats / Comfort / Confused |
| Dutch Food Learning Curve Tracker | (128, 448) | 192x32 | Five stages: Confusion → Adjustment → Acceptance → "Actually pretty good" → Smug |
| High-Contrast Table Marker | (320, 448) | 64x32 | Bold outline for table and counter interaction points |
| Portion Silhouette Set | (384, 448) | 128x32 | Dutch pancake vs. American stack as labelled stepped silhouettes |
| Touch-Zone Guide Overlay | (0, 480) | 256x32 | Dev-only 44px minimum overlay, stripped at build |
| Reserve | (256, 480) | 256x32 | Reserved strip, do not paint |

### Technical Notes:
- The Menu Navigation UI shows base prices only, exactly as the physical menu does; toppings surface their cost after selection. This is not a UI bug and must be documented as intentional in the build notes.
- The Running Total Ticker is available as an assist-mode toggle so players who find the hidden-cost mechanic frustrating rather than funny can opt out; the joke survives, the friction does not
- Every menu row and topping option renders at 44px+ touch height across all five language layouts
- The Bill Breakdown Popup itemises honestly — every charge is real, every charge was disclosed somewhere, and that is the entire point

---

## 🎬 Animation Specifications

### Jan's Griddle Loop (Sheets 5 & 7):
- **Duration:** 6.0 seconds per cycle (2.0s per frame), representing a 2-minute production cycle in compressed time
- **Frames:** 3 (batter poured / spread / flip) + kitchen steam + butter sizzle
- **Pattern:** Continuous while the interior scene is loaded
- **Trigger:** Constant
- **Purpose:** The pancakes really are made fresh; that is the one thing that is exactly as advertised
- **Audio Sync:** Batter hiss at 0.0s; spread scrape at 2.0s; flip slap at 4.0s; continuous griddle sizzle bed underneath
- **Performance Optimization:** Low LOD holds the plating frame with static steam (profile requirement: simplified kitchen animation, reduced steam)

### The Portion Revelation (Sheets 4, 6, 7):
- **Duration:** 2.2 seconds (0.4s plate land, 0.4s desaturation beat, 1.4s reaction hold)
- **Frames:** Pancake sprite placement + Portion Reveal Beat Plate + Portion Reaction Strip frames 2-3
- **Pattern:** One-shot on first order delivered per visit
- **Trigger:** First plate arriving at the player's table
- **Purpose:** "Is this... is this all of it?" — the location's central beat
- **Audio Sync:** Plate on wood at 0.0s; a brief total audio dropout 0.4-0.8s (comedy-critical); ambient room returns at 0.8s; Marleen's line at 1.6s
- **Performance Optimization:** None needed (one-shot, cheap, load-bearing)

### The Syrup Situation (Sheets 4, 5, 7):
- **Duration:** 3.0 seconds (1.2s pour, 0.4s pitcher empty, 1.4s Jesse explanation)
- **Frames:** Syrup Pour Stream + Jesse Syrup Explanation frame
- **Pattern:** Repeatable; each "more syrup" request costs 3 Sovs and produces the identical pitcher
- **Trigger:** Any syrup request
- **Purpose:** "Maple-FLAVOURED. Yes." The pitcher was always going to be this size.
- **Audio Sync:** Pour cue 0.0-1.2s; a small hollow note when the pitcher empties at 1.2s
- **Performance Optimization:** Pour reduced to a static stream frame on Low LOD

### The Spek Explanation (Sheets 4 & 5):
- **Duration:** 3.2 seconds (1.2s F1, 1.2s F2, 0.8s resignation hold)
- **Frames:** 2 Jesse frames + Spek Cubes close-up inset
- **Pattern:** One-shot per bacon order
- **Trigger:** Ordering the Spekpannenkoek
- **Purpose:** He asks if it's okay. He already knows he is bringing the spek.
- **Audio Sync:** Dialogue only; the inset slides in at 1.2s with a soft tick
- **Performance Optimization:** None needed

### The Bill Reveal (Sheets 4, 5, 7, 8):
- **Duration:** 3.4 seconds (0.6s folder placement, 0.8s pause for reaction preparation, 2.0s line-by-line reveal)
- **Frames:** Bill presenter + Bill Reveal Sting Plate + Bill Breakdown Popup line stagger + Bill Reaction Strip
- **Pattern:** One-shot at end of meal
- **Trigger:** Requesting the bill, or Jesse deciding it is time
- **Purpose:** "Your total is... sixty-four Sovs. For three." Every line is correct.
- **Audio Sync:** Folder placement 0.0s; silence 0.6-1.4s; a small dramatic sting on the total at 3.0s
- **Performance Optimization:** Lines snap in rather than stagger in reduced-motion mode

### Canal & Terrace Ambience (Sheets 3 & 7):
- **Duration:** Boat traverse 18.0s; duck patrol 6.0s loop; heater glow 3.0s breathe
- **Frames:** 1 scrolling boat + wake, 2 duck frames, 1 alpha heater plate
- **Pattern:** Boat every ~45s; ducks continuous; heater glow only while the fee accrues
- **Trigger:** Terrace scene loaded
- **Purpose:** The view you are paying for, plus the ducks you are not
- **Audio Sync:** Boat horn on entry to frame; quacks on duck escalation frames
- **Performance Optimization:** Low LOD moors all boats (profile requirement: static boats), ducks reduce to a single pose

### The Food Photograph (Sheets 4, 6, 8):
- **Duration:** 1.8 seconds (0.6s frame compose, 0.4s capture, 0.8s caption prompt)
- **Frames:** Food Photo Frame + Photographing Pose Strip + Caption Choice Panel
- **Pattern:** One-shot per plate photographed
- **Trigger:** Player photographs any dish
- **Purpose:** It genuinely looks good from above; the caption is where honesty costs Bravado
- **Audio Sync:** Shutter at 0.6s
- **Performance Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| High-Contrast Table Marker | Sheet 8 (320, 448) | 64x32 | Bold outline for table, counter, and pass interaction points |
| Portion Silhouette Set | Sheet 8 (384, 448) | 128x32 | Dutch pancake vs. American stack as labelled stepped silhouettes |
| Marleen High-Contrast Silhouette | Sheet 5 (0, 416) | 64x96 | Enhanced-visibility outline of the seating NPC |
| Jesse High-Contrast Silhouette | Sheet 5 (64, 416) | 64x96 | Enhanced-visibility outline of the ordering NPC |
| Accessibility Reserve Block | Sheet 5 (256, 416) | 256x96 | Overflow space for additional high-contrast variants |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Steam | Sheet 7 (288, 192) | 64x64 | Non-animating kitchen steam plate |
| Static Boats | Sheet 7 (352, 192) | 64x64 | Moored-only canal with no scrolling traversal |
| Static Kitchen | Sheet 7 (416, 192) | 64x64 | Jan holds a single plating frame |
| No-Desaturation Portion Reveal | Sheet 7 (448, 64) | 64x64 | Reduced-motion skips the desaturation beat; the audio dropout is retained |
| Snapped Bill Lines | Sheet 8 (0, 256) | 256x192 | Bill lines appear instantly instead of staggering |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sizzle Glyph | Sheet 7 (384, 128) | 32x32 | Mirrors the continuous kitchen sizzle bed |
| Cutlery Clink Glyph | Sheet 7 (416, 128) | 32x32 | Mirrors the distinctively smaller Dutch cutlery |
| Boat Horn Glyph | Sheet 7 (448, 128) | 32x32 | Mirrors the canal horn, terrace only |
| Duck Quack Glyph | Sheet 7 (480, 128) | 32x32 | Mirrors aggressive duck begging |
| Card Beep Glyph | Sheet 7 (128, 192) | 32x32 | Mirrors the card machine |
| Bill Sting Glyph | Sheet 7 (160, 192) | 32x32 | Mirrors the total-reveal sting |
| Menu Page Turn Glyph | Sheet 7 (192, 192) | 32x32 | Mirrors laminated page turns |
| Syrup Pour Glyph | Sheet 7 (224, 192) | 32x32 | Mirrors the pour cue and the hollow empty-pitcher note |
| Multilingual Murmur Glyph | Sheet 7 (256, 192) | 32x32 | Persistent ambient-room indicator |
| Portion Reveal Silence Marker | Sheet 7 (448, 64) | 64x64 | Explicit on-screen marker for the deliberate 0.4s audio dropout |

### Colorblind Considerations:
- The four pancakes are distinguished by topping geometry and text labels on every menu and order panel, never by surface colour
- Bill line items use pattern-coded left rules (solid = ordered, hatched = automatic, dotted = fee) plus explicit text, never colour-coded charges
- Status effects use distinct silhouettes: recalibrating arrow (Expectation Adjustment), droplet-over-wedge (Cheese Sweats), open circle (Comfort), spiral (Confused)
- The Dutch Food Learning Curve tracker uses five numbered, labelled stages, not a colour gradient
- Terrace heater active state is communicated by the glow plus an explicit on-screen fee ticker, never by warmth of colour alone
- Touch zones minimum 44px for all menu rows, topping options, page tabs, caption choices, and the contest-charges prompt

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) the physical menu, chalkboard, heater fee notice, bill/receipt props, "As Featured In" clippings, and all portraits kept uncompressed
- **Fallback:** PNG high quality for `pancake_house_interior_main.png` and `pancake_house_terrace.png` (the warm interior gradient and the canal water band both band under lossy compression)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| pancake_house_environment | pancake_house_fixtures | 1024x1024 |
| pancake_house_characters | npc_pancake_house_staff, npc_pancake_house_customers | 1024x1024 |
| pancake_house_fx_ui | pancake_house_food, pancake_house_effects, pancake_house_ui | 1024x1024 |

*(Interior and terrace backgrounds load standalone; only one is resident at a time in normal play. Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full 3-frame griddle loop with steam and sizzle, scrolling boats with wake, duck patrol, heater glow breathe, electric candle flicker, staggered bill reveal |
| Medium | Griddle at 2 frames, steam at half density, boats scroll without wake, ducks at half rate, candles static |
| Low | Static kitchen (profile requirement), static table decor (profile requirement), reduced steam (profile requirement), moored boats, single duck pose, snapped bill lines |

### Performance Targets:
- **Target FPS:** 60 (per location performance budget)
- **Max Draw Calls:** 16 per frame
- **Memory Footprint:** 36 MB maximum
- **Particle Limit:** 14 (kitchen steam, sizzle sparkle, powdered sugar, canal ripple)

### Performance Notes:
- Interior and terrace are separate scene loads; the transition through the terrace door is a hard cut with a 0.3s fade, keeping only one 8.29 MB background resident
- American Family, Dutch Couple, and Bros Trio ship pre-composed; maximum 4 individually animated NPCs on screen
- One canal boat instance is recycled for all traversals; there is no parallax layer on the terrace
- The windmill miniatures, copper pans, and Delft tiles are all baked into their backgrounds — only tables, NPCs, and food are separate draws

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (both backgrounds, fixtures, décor), AnimatedSprite2D (Jan's griddle, ducks, boat, staff), CPUParticles2D (kitchen steam, sizzle, powdered sugar, canal ripple — not GPU), CanvasLayer (menu UI, bill popup, photo frame), Area2D (tables, terrace tables, pass counter, till)
- Special systems: multi-page menu state machine with per-page language layout, hidden-cost bill calculator (base + per-topping + terrace heater timer + automatic bread basket + service), terrace heater accrual timer started on seating, permanent Expectation Adjustment flag on first completed meal, Dutch Food Learning Curve global counter shared across Shamsterdam food locations, photo caption Bravado/Authenticity resolution, contest-charges Bravado check with discount branch, time-of-day clientele mix selector

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Griddle frame 1 | Batter hiss | 0.0s of griddle loop |
| Griddle frame 2 | Spread scrape | 2.0s |
| Griddle frame 3 | Flip slap | 4.0s |
| Plate landing | Plate on wood | 0.0s of Portion Revelation |
| Portion reveal beat | Total audio dropout (deliberate) | 0.4-0.8s |
| Syrup pitcher empty | Small hollow note | 1.2s of syrup pour |
| Spek inset slide | Soft tick | 1.2s of spek explanation |
| Bill folder placement | Leather-on-wood | 0.0s of bill reveal |
| Bill total line | Small dramatic sting | 3.0s |
| Card machine | Confirm beep | On payment |
| Boat entering frame | Canal horn | On traversal start (terrace) |
| Any cutlery use | Distinctively smaller-knife clink | Per use |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Portion Revelation | Pancake sprites, reveal beat plate, Portion Reaction Strip, Marleen Pointing frame | First plate delivered; grants the permanent Expectation Adjustment buff |
| The Syrup Situation | Syrup pitcher, stroop container, pour stream, Jesse Syrup Explanation | Repeatable; every request costs 3 Sovs and returns the same pitcher |
| The Bacon Specificity Problem | Spek cubes close-up, Jesse Spek frames, bacon pancake sprite | Ordering the Spekpannenkoek; the food is good, the expectation was wrong |
| The Bill Breakdown | Bill popup, running total ticker, contest panel, Bill Reaction Strip | End of meal; every line is legitimate and every line was disclosed somewhere |
| Food Photography | Photo frame, caption panel, blogger NPC | Honest caption costs Bravado and grants Authenticity |
| The Dutch Food Learning Curve | Learning Curve tracker, Expectation Adjustment status | Shared five-stage counter across Shamsterdam food locations, ending in smugly explaining Dutch food to other tourists |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Tolerance Hostel | Expectation Adjustment status carried into kitchen dialogue | "Did you go to the pancake place? Did they explain before you ordered?" — the answer changes the exchange |
| FEBO Automat | Shared Dutch Food Learning Curve counter | "At FEBO you KNOW what you're getting for 3 Sovs" — value comparison dialogue unlocks after the bill reveal |
| Café de Schaamte | Expectation Adjustment status, food photo album entry | Post-pancake espresso; processing what happened |
| De Groene Gids | Munchies modifier on appetite appreciation | Pre-pancake visit shifts the Portion Revelation from disappointment to delight |
| Leeman's Döner Palace | Shared Dutch Food Learning Curve counter | Later stages of the curve change the player's default ordering confidence |
| Canal Ring Promenade (street node) | Terrace background, canal railing, boat lane | The terrace is visible from the promenade; the heaters are visible; the prices are not |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Genuinely charming, genuinely good, genuinely expensive, and genuinely not what you ordered"
- **Color Mood:** Dutch blue and Delft white over warm wood and butter yellow, with the canal's gray-green cooling the terrace — cosy, photogenic, and priced accordingly
- **Lighting:** Warm overhead spots inside with natural window light on the good tables; open daylight on the terrace; the kitchen pass is the warmest point in the room
- **Texture:** Polished unused copper, laminated menu shine, blue-checkered cotton, worn floorboards, glazed Delft tile, canal water with a hard reflective band

### Environmental Storytelling:
- Every table has a windmill miniature and there is no sign anywhere stating what breaking one costs
- The copper pans are spotless because they have never been used
- The "As Featured In" press clippings stop in 2014, and nobody has taken them down
- The photos on the menu show the actual portion size, at actual scale, in full colour, and are looked at by nobody
- The heater fee notice is real, legible, and on page six
- The Dutch couple two tables over finished eating before the tourists finished ordering

### Character Integration Notes:
- Marleen genuinely tries to manage expectations at three separate points before the order is placed; her knowing smile at the end is earned, not smug
- Jesse is helpful, accurate, and completely unresponsible for the gap between what you heard and what you ordered
- Jan is the only person in the building doing exactly what the marketing promises, and he does it every two minutes forever
- No staff frame may read as predatory; the restaurant is honest and the misunderstanding is cultural. If the staff look like they are in on a scam, the whole location fails.

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Single Pancake** — plate-sized, thin, arranged, alone, and correct
2. **The Syrup Pitcher Beside the Plate** — scale comparison, no caption required
3. **The Bill Breakdown** — 64 Sovs for three, itemised, every line defensible
4. **Spek vs. Strips** — the close-up inset, side by side with the expectation
5. **The Terrace Heater Glowing** — warm, welcoming, accruing at 2 Sovs/hour

### Quote Potential:
- "Our pancakes are traditional Dutch. Very large. Very thin. One is usually enough."
- "The bacon is spek. Cubes. Traditional. Not strips. Is that okay? ...I'll bring the spek."
- "More syrup is three Sovs. Yes, for the small one. It's... concentrated."
- "The bread basket was complimentary to receive. Not complimentary to keep. Four Sovs."
- "Your total is... sixty-four Sovs. For three."
- "I see you are looking at the photos. Yes, that is actual size. One pancake per plate."
- "You guys should've gotten the apple. It's actually great."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | pancake_house_interior_main.png | 1920x1080 |
| 2 | pancake_house_terrace.png | 1920x1080 |
| 3 | pancake_house_fixtures.png | 1024x1024 |
| 4 | pancake_house_food.png | 512x256 |
| 5 | npc_pancake_house_staff.png | 512x512 |
| 6 | npc_pancake_house_customers.png | 1024x256 |
| 7 | pancake_house_effects.png | 512x256 |
| 8 | pancake_house_ui.png | 512x512 |

**Total Estimated Memory:** ~25.0 MB in-memory (uncompressed RGBA worst case) with both backgrounds resident; ~16.7 MB in normal play since interior and terrace are separate scene loads. Within the 36 MB location budget.

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `pancake_house_interior_main.png` (1920x1080)
- [ ] `pancake_house_terrace.png` (1920x1080)
- [ ] `pancake_house_fixtures.png` (1024x1024)
- [ ] `pancake_house_food.png` (512x256)
- [ ] `npc_pancake_house_staff.png` (512x512)
- [ ] `npc_pancake_house_customers.png` (1024x256)
- [ ] `pancake_house_effects.png` (512x256)
- [ ] `pancake_house_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + full five-language menu copy sheet with page numbering + bill line-item pattern-coding key

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (#1E90FF, #FFD700, #F5F5F5, #8B4513, #B87333, #5F7A6E)
- [ ] Key gags read clearly: one thin pancake filling an entire plate, the syrup pitcher's true scale beside it, spotless never-used copper pans, press clippings ending in 2014, the heater fee notice present and on page six
- [ ] The food looks genuinely appetising in every sprite — the joke is expectation, never quality
- [ ] Menu text is legible at gameplay zoom on a 5-inch display across all five language layouts
- [ ] Accessibility visual alternatives included for all audio cues (sizzle, cutlery, boat horn, quack, card beep, bill sting, page turn, syrup pour, murmur, reveal silence)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (the targets are tourist expectation and waterfront pricing — Dutch cuisine is depicted as legitimately excellent)
- [ ] No staff sprite reads as predatory, smug, or complicit in a scam
- [ ] Hidden areas/interactions have discoverable visual cues (menu photos at actual scale, heater fee notice, bread basket stand, second dining floor stairs)
- [ ] Performance optimized (CPU particles, atlas limits respected, separate interior/terrace loads, static kitchen and boat fallbacks)
- [ ] Touch zone sizing considered (44px minimum for menu rows, toppings, page tabs, and caption choices)
- [ ] Colorblind-friendly alternatives available where color codes meaning (pattern-coded bill rules, labelled portion silhouettes, numbered learning-curve stages)
- [ ] Social media viral potential maximized in composition choices (overhead plate framing, pitcher scale comparison, itemised bill readability)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam Canal Ring Promenade; menu and décor reference Dutch tradition without naming a real city |
| Cultural Specificity | ✅ | Dutch pannenkoeken reality, spek vs. strips, stroop vs. maple, Delft tile, smaller cutlery, canal-house architecture |
| Satirical Targets Appropriate | ✅ | American food expectations abroad and waterfront tourist pricing — Dutch cuisine and the staff are treated with respect |
| Seedy Underbelly Present | ✅ | 18 Sovs for a 3 Sovs plate because it faces a canal, unadvertised heater fees, the automatic bread basket, per-topping surcharges surfacing after selection |
| Gameplay Value Established | ✅ | Multi-page menu navigation, hidden-cost bill calculator, three revelation beats, Bravado contest branch, permanent Expectation Adjustment buff, shared learning-curve counter |
| Technical Feasibility | ✅ | Separate interior/terrace loads, static kitchen and boat fallbacks per profile, pre-composed customer blocks, single recycled boat instance |
| Performance Budget | ✅ | 60 FPS, 16 draw calls, 36 MB, 14 particles per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all ten audio cues including the deliberate silence, reduced-motion set, optional running-total assist mode, 44px touch zones |
| No Crypto Elements | ✅ | Pure tourist-trap dining; the only speculative instrument is the bread basket |
| Social Media Integration | ✅ | 5 screenshot moments + 7 quotable lines identified |

**Once these assets ship, The Pancake House becomes the game's most reasonable ambush: a beautiful room, a warm welcome, three separate honest warnings, a genuinely delicious plate-sized crepe, and a bill for sixty-four Sovs in which every single line is correct.**
