# De Botanische Leugen - Complete PNG Asset Requirements

## 📋 Overview
De Botanische Leugen ("The Botanical Lie") is a floating flower-market stall on the canal where Vendor Margriet has been selling genuine Dutch tulip bulbs to people who will never plant them since 1962, under a sign that dates the operation to 1637 — the year of Tulip Mania, when the Dutch first discovered that hope is the highest-margin product on earth. This document specifies every PNG asset across the swaying floating stall and canal setting, the bulb bins and sample-garden displays, the item sprites from single bulb to desiccated epilogue, Margriet and Piet and the full customer cast, and the purchase / customs / epilogue UI. Its satirical essence in a sentence: the bulbs are completely real, the garden is completely imaginary, and everyone involved is politely agreeing not to mention the difference.

**Location ID:** `shamsterdam_flowermarket_tulip_seller_01`
**Theme:** Souvenir psychology and agricultural optimism — buying the idea instead of the object, and the four-hundred-year-old Dutch business of selling that idea
**Zone:** The Floating Flower Market, stalls on the canal (gentle sway included at no extra charge)
**Hours:** 9 AM - 5:30 PM (market hours, optimism hours)
**Primary Function:** Tourist-trap vendor / purchase-psychology exploration — bulb purchasing system, the Vendor's Dance deflection dialogue, "Bulb Burden" persistent inventory item, optional customs encounter, planting epilogue, five-stage botanical achievement track

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Tulip Red | #E63946 | Signature blooms, signage, price tags |
| Stem Green | #2D6A4F | Foliage, stall structure, awning stripe |
| Petal Pink | #FFB4A2 | Soft bloom mass, background bouquet wash |
| Bulb Brown | #8B4513 | Bulbs, bins, deck timber, paper bags |
| Canal Slate | #6E7B78 | Water, wet planking, overcast sky |
| Market Gold | #E9C46A | Awning trim, "1637" plaque, warm market light |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/de_botanische_leugen/
├── environment/
│   ├── botanische_leugen_stall.png
│   └── leugen_bulb_displays.png
├── objects/
│   └── leugen_items.png
├── npcs/
│   └── npc_leugen_cast.png
└── ui/
    └── leugen_ui_effects.png
```

---

## 🌷 Sprite Sheet 1: Floating Stall, Canal & Signage
**File:** `botanische_leugen_stall.png`
**Dimensions:** 1024x768 pixels
**Color Palette:** #2D6A4F, #8B4513, #6E7B78, #E9C46A

### Market Context:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floating Flower Market Backdrop (tileable) | (0, 0) | 512x256 | Canal receding, stall roofs, gabled houses behind |
| Adjacent Stalls — Left | (512, 0) | 256x256 | Competitor hope merchants, equally sincere |
| Adjacent Stalls — Right | (768, 0) | 256x256 | Seeds, cut flowers, wooden shoes, same logic |

### The Stall Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stall Structure (fully dressed) | (0, 256) | 384x192 | Overflowing with colour; sensory overwhelm by design |
| Stall Structure (undressed / closing) | (384, 256) | 384x192 | 5:30 PM state, shutters half down, bins covered |
| Floating Platform | (768, 256) | 256x96 | The stall sits on water; the ground is not the ground |
| Platform Sway Frame 1-2 | (768, 352) / (896, 352) | 128x96 each | Gentle roll that adds to the dreamlike purchasing haze |

### Canal:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Canal Water Surface (tileable) | (0, 448) | 256x128 | Green-slate, faint petal debris |
| Canal Lap Ripple 1-3 | (256, 448) / (384, 448) / (512, 448) | 128x128 each | Three-frame lapping against the platform |
| Canal Sparkle Overlay | (640, 448) | 128x128 | Point-light glints, additive |
| Mooring Rope + Cleat | (768, 448) | 128x64 | The only thing between the stall and the North Sea |
| Gangplank | (768, 512) | 128x64 | Slight give underfoot, entirely legal, probably |
| Canal Boat Passing (background) | (896, 448) | 128x128 | Wake causes a sway amplitude spike |

### Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Sign | (0, 576) | 384x96 | "DE BOTANISCHE LEUGEN — TULPEN SINDS 1637" |
| Banner "GROW YOUR OWN DUTCH GARDEN!" | (384, 576) | 256x64 | The promise, in full colour |
| Sign "BULBS TRAVEL WELL*" | (384, 640) | 256x32 | Asterisk present, footnote absent |
| Small Sign — Climate Disclaimer | (640, 576) | 256x32 | "Results not guaranteed outside maritime climates" |
| Tiny Sign — Customs Notice | (640, 608) | 256x32 | "Check import regulations for your country" |
| 1637 Tulip-Mania Plaque | (640, 640) | 128x32 | The date is pointed. The date is the whole joke. |
| Asterisk-Leads-Nowhere Detail | (768, 640) | 128x32 | Zoom prop: the asterisk has no matching footnote anywhere on the stall |
| Stall Awning — Striped | (896, 576) | 128x96 | Green and gold, canal-weathered |

### Deck & Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Awning Sway Frame 1-2 | (0, 672) / (256, 672) | 256x96 each | Fabric moving with the platform, not the wind |
| Market Deck Tile — Wet | (512, 672) | 32x32 | Base planking |
| Market Deck Tile — Petal-Strewn | (544, 672) | 32x32 | Accumulated colour underfoot |
| Market Deck Tile — Dry | (576, 672) | 32x32 | Under-awning variant |
| Canal Edge Post | (608, 672) | 32x96 | Rope-scarred, tilted |
| Overhead String of Bulb Bags | (640, 672) | 192x96 | Hanging inventory, windmill graphics facing out |
| Hanging Basket | (832, 672) | 96x96 | Cascading blooms, purely atmospheric |
| Cash Box / Card Reader | (928, 672) | 96x96 | Family stall, modern terminal, no fuss |
| Deck Puddle Decal | (512, 704) | 96x64 | Permanent, reflective, canal-fed |

### Technical Notes:
- The whole stall assembly (structure, awning, displays, NPCs) parents to a single sway node — one rotation driver, not per-sprite motion, to protect the 14 draw-call budget
- Sway amplitude spikes for 3 seconds when Canal Boat Passing crosses; this is the only variation in an otherwise constant rhythm
- Canal Lap Ripple frames sync to the sway phase so water and platform move as one system
- Signage is text-critical across five sign sprites: the 1637 date, the asterisk, and the two tiny disclaimers are the location's core gags and must survive compression

---

## 🌈 Sprite Sheet 2: Bulb Bins, Sample Garden & Packaging Displays
**File:** `leugen_bulb_displays.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #E63946, #FFB4A2, #8B4513, #2D6A4F

### Bins & The Promise:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bulb Bin Row A (4 varieties) | (0, 0) | 256x192 | Open bins, brown bulbs, romantic Dutch names |
| Bulb Bin Row B (4 varieties) | (256, 0) | 256x192 | Second bank; organized by promised colour |
| Bulb Bin Single (empty, restock) | (512, 0) | 128x192 | Piet's next job |
| Sample Garden — Potted Tulips | (640, 0) | 256x192 | Grown in the Netherlands, by professionals, in ideal conditions |
| "The Tulip Promise" Photo Card Set | (896, 0) | 128x96 | Photo of what these bulbs "will become" |
| Variety Label Plates | (896, 96) | 128x96 | Queen of Night, Rembrandt, and six more, all beautifully lettered |

### Cut Flowers & Packaging:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cut Flower Buckets — Colour Explosion | (0, 192) | 256x160 | Atmosphere, not inventory; the reason you stopped |
| Cut Flower Buckets — Second Cluster | (256, 192) | 256x160 | Depth layer for the overwhelm effect |
| International Bulb Bags | (512, 192) | 192x128 | Windmill graphics, "Easy to grow!", "Perfect gift!" |
| Bulb Bag — "Product of Shamsterdam" Face | (704, 192) | 96x128 | Front-facing hero bag; genuinely beautiful object |
| Value Bag Display Stack | (800, 192) | 128x160 | 10s and 20s, stacked to encourage scale |
| Protective Bag (+2 Sovs) | (928, 192) | 96x96 | The upsell that closes the customs question |
| Growing Instructions Leaflet | (512, 320) | 192x32 | Dutch, French, German, and Very Small English |
| Fine-Print Card | (704, 320) | 96x32 | Zoom prop: the English section is four lines long |
| Price Sign — Per Bulb (2 Sovs–5) | (928, 288) | 96x32 | Chalk on slate |
| Price Sign — Value Bags (15 Sovs–30) | (928, 320) | 96x32 | Better value, worse odds |

### Product Racks:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wooden Tulip Rack (painted) | (0, 352) | 192x160 | The honest option. Cannot die. Cannot grow. |
| Tulip Seed Packet Rack | (192, 352) | 128x160 | 12 Sovs — takes seven years to flower |
| "Old Master Collection" Presentation Case | (320, 352) | 192x160 | 50 Sovs, velvet-lined, 0.1% success rate |
| Rainbow Mix Display | (512, 352) | 192x160 | The most popular. Everyone wants a rainbow. |
| Garden Starter Display | (704, 352) | 160x160 | Twenty bulbs; ambition exceeding capacity |
| Bin Scoop + Paper Bag Roll | (864, 352) | 96x96 | Piet's tools |
| Pollen Dust Layer (tileable) | (864, 448) | 160x64 | Fine drift over the whole stall |

### Technical Notes:
- Sample Garden potted tulips are rendered notably healthier and denser than anything the player can actually buy — the visual gap is the delusion engine and must not be softened
- Bulb bins use a single sprite per row rather than per-bin so the fill level cannot desync during purchase
- Variety Label Plates are a separate sprite from the bins for localisation and for the eight named varieties on Sheet 3
- Pollen Dust is a particle texture, not a baked overlay, so it can be culled entirely on Low LOD

---

## 🧅 Sprite Sheet 3: Items, Varieties & The Bulb's Journey
**File:** `leugen_items.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #E63946, #8B4513, #2D6A4F, #E9C46A

### Purchasable Items (Row 0, y=0):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Single Tulip Bulb | (0, 0) | 64x64 | 3 Sovs — individual hope, 2% grow success |
| Rainbow Mix Bag (10) | (64, 0) | 64x64 | 15 Sovs — variety pack of dreams, 1% |
| Garden Starter Bag (20) | (128, 0) | 64x64 | 25 Sovs — 0.5% |
| Old Master Collection | (192, 0) | 96x64 | 50 Sovs — "You're not an Old Master", 0.1% |
| Wooden Tulip (Painted) | (288, 0) | 64x64 | 8 Sovs — 100% success, cannot die, cannot grow |
| Tulip Seeds Packet | (352, 0) | 64x64 | 12 Sovs — the seven-year trap |
| Protective Bag | (416, 0) | 64x64 | 2 Sovs — deployed exclusively as a customs deflection |
| Growing Instructions (folded) | (480, 0) | 32x64 | Inside the bag. Very clear. Mostly clear. |

### The Burden & Props (Row 1, y=64):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "Bulb Burden" Inventory Item | (0, 64) | 64x96 | Light physically, heavy existentially; occupies a slot for the rest of the game |
| Bulb Burden — Weeks Later (dusty) | (64, 64) | 64x96 | Same bag, visibly demoted |
| Desiccated Bulb (epilogue) | (128, 64) | 64x96 | Found during a move, two years on |
| Cut Tulip Bouquet | (192, 64) | 96x96 | Atmospheric purchase; dies in four days, honestly |
| Potted Tulip (sample) | (288, 64) | 96x96 | What you believe you are buying |
| Bulb Cross-Section Diagram | (384, 64) | 64x96 | On the instruction leaflet; nobody reads it |
| Sov Coins / Notes | (448, 64) | 64x96 | 3 Sovs to 50 Sovs, the whole range |

### Varieties & Documents (Row 2, y=160):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Variety — Queen of Night | (0, 160) | 48x96 | "Very dramatic. Very Shamsterdam." |
| Variety — Rembrandt | (48, 160) | 48x96 | What the Experienced Gardener came for |
| Variety — Classic Red | (96, 160) | 48x96 | The one on every postcard |
| Variety — White | (144, 160) | 48x96 | Wedding purchase; the Honeymooners' pick |
| Variety — Pink | (192, 160) | 48x96 | Rainbow Mix component |
| Variety — Yellow | (240, 160) | 48x96 | Rainbow Mix component |
| Variety — Parrot | (288, 160) | 48x96 | Fringed, absurd, expensive |
| Variety — Striped ("Tulip Mania") | (336, 160) | 48x96 | The 1637 flower; a virus, historically |
| CITES Permit Document | (384, 160) | 64x96 | Experienced Gardener's prop; the correct way to do this |
| Customs Declaration Form | (448, 160) | 64x96 | Blank. Always blank. |

### Bags & Transit (Row 3, y=256):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Paper Bag (filled, hope) | (0, 256) | 64x96 | Point of sale |
| Paper Bag (crumpled, home) | (64, 256) | 64x96 | Two weeks later |
| Windmill-Graphic Bag Face | (128, 256) | 96x96 | Hero detail; genuinely worth keeping |
| Souvenir Bag (kept, empty, still nice) | (224, 256) | 96x96 | The only part of the purchase that delivers |
| Suitcase With Bulbs Packed | (320, 256) | 96x96 | Prominent luggage position, step 2 of the journey |
| Drawer With Forgotten Bulbs | (416, 256) | 96x96 | Step 6 of the journey: "Where did we put…?" |

### The Epilogue (Row 4, y=352):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Epilogue Frame 1 — "Somewhere Safe" | (0, 352) | 128x96 | Bag placed on a shelf, on arrival home |
| Epilogue Frame 2 — Two Months Later | (128, 352) | 128x96 | Same shelf, more things on top of it |
| Epilogue Frame 3 — Two Years Later | (256, 352) | 128x96 | Discovered during a move |
| Epilogue Frame 4 — Quiet Disposal | (384, 352) | 128x96 | No acknowledgement, no ceremony |

### Outcomes & Achievements (Row 5, y=448):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Epilogue Frame 5 — The 1% | (0, 448) | 128x64 | An actual Dutch tulip, in an actual pot, against all odds |
| Achievement Tokens (5) | (128, 448) | 256x64 | Hope Planter / Old Master Aspirant / Realist / Attempted Gardener / Botanical Miracle Worker |
| Wooden Tulip (chipped, honest) | (384, 448) | 64x64 | Still on the windowsill years later, still fine |
| Bulb Sprout (rare success) | (448, 448) | 64x64 | Green shoot; the sprite almost nobody will ever see |

### Technical Notes:
- The eight named varieties reuse one silhouette with per-variety petal shape and palette; they are the shop's colour vocabulary and appear in bins, bags, UI and epilogue
- Bulb Burden has three visual states driven by an in-game day counter, not by player action — the item degrades whether you engage with it or not
- Epilogue frames 1-5 are a single sequence played in the post-credits reveal; frame 5 has a 1% roll and frame 4 is the 85% default
- Wooden Tulip (chipped, honest) is deliberately the most positive object on the sheet

---

## 👥 Sprite Sheet 4: Vendor, Assistant & Customer NPCs
**File:** `npc_leugen_cast.png`
**Dimensions:** 1024x288 pixels
**Sprite Size:** 64x96 pixels (groups and portraits noted)

### Stall Staff (Row 0, y=0):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Margriet Idle 1-2 | (0, 0) / (64, 0) | 64x96 each | Floral apron, patient smile, family stall since 1962 |
| Margriet Presenting 1-3 | (128, 0) / (192, 0) / (256, 0) | 64x96 each | Bulb in palm, offered like a small ceremony |
| Margriet Bagging 1-2 | (320, 0) / (384, 0) | 64x96 each | Practised, quick, warm |
| Margriet Warm Upsell 1-2 | (448, 0) / (512, 0) | 64x96 each | "A pot works too! A windowsill! A dream!" |
| Margriet Customs-Question Deflect 1-3 | (576, 0) / (640, 0) / (704, 0) | 64x96 each | Eye contact breaks, hand gestures to the bag, subject changes |
| Margriet "I can see it already" | (768, 0) | 64x96 | Genuine warmth aimed at a garden that will not exist |
| Piet Idle 1-2 | (832, 0) / (896, 0) | 64x96 each | Dirt under fingernails; credibility |
| Piet Lifting Crate | (960, 0) | 64x96 | Silent, useful |

### Assistant & Customers (Row 1, y=96):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Piet Bag Filling 1-3 | (0, 96) / (64, 96) / (128, 96) | 64x96 each | "Careful, they're fragile. Like dreams." |
| Piet Deflecting To Aunt | (192, 96) | 64x96 | "My aunt handles questions. I handle bulbs." |
| Experienced Gardener 1-2 | (256, 96) / (320, 96) | 64x96 each | Older, knows plants, here for specific varieties |
| Gardener Presenting CITES Permit | (384, 96) | 64x96 | The correct way, performed in front of people who won't notice |
| Instagram Tourist 1-2 | (448, 96) / (512, 96) | 64x96 each | Ring light, 50 photos, 0 purchases |
| Instagram Tourist Holding "ALL of them" | (576, 96) | 64x96 | "For the shot? I'll put them back." |
| Honeymooners | (640, 96) | 128x96 | Buying their future garden for their future house |
| Honeymooners Choosing Together | (768, 96) | 128x96 | Naming tulips they will never meet |
| Customs-Aware Tourist 1-2 | (896, 96) / (960, 96) | 64x96 each | Practical shoes, wooden tulips, no regrets |

### Returning Customers & Bros (Row 2, y=192):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Return Customer (Annual) 1-2 | (0, 192) / (64, 192) | 64x96 each | "Last year's didn't grow, but maybe THIS year." |
| Return Customer Recognizing Margriet | (128, 192) | 64x96 | Warm reunion; she does not track outcomes |
| Lord Pilsner Buying Old Master | (192, 192) | 64x96 | "For fifty Sovs I'm basically an Old Master." |
| Lord Pilsner "it's more of a balcony" | (256, 192) | 64x96 | "…it gets sun SOMETIMES…" |
| Chadwick Filming B-Roll | (320, 192) | 64x96 | "The colour palette here is INSANE." |
| Chadwick With Rainbow Mix | (384, 192) | 64x96 | "My apartment is going to be BOTANICAL." |
| Bradley Advocating Wooden Tulips | (448, 192) | 64x96 | The one correct opinion of the entire trip |
| Bradley Overruled | (512, 192) | 64x96 | "Fine. Real bulbs." |
| Browsing Tourist Filler 1-4 | (576, 192) / (640, 192) / (704, 192) / (768, 192) | 64x96 each | Palette-swappable market crowd |
| Margriet Portrait Bust | (832, 192) | 96x96 | Dialogue portrait, warm and unhurried |
| Piet Portrait Bust | (928, 192) | 96x96 | Dialogue portrait, minimal expression range by design |

### Technical Notes:
- Margriet's three Customs-Question Deflect frames are the location's key performance: frame 1 breaks eye contact, frame 2 redirects to the bag, frame 3 resumes the sale. Play them in strict order, never shuffled.
- Max 4 customer NPCs on the stall at once (14 draw-call budget); Honeymooners count as 2
- Browsing Tourist Filler frames are palette-swapped at runtime to produce 8 apparent shoppers from 4 sprites
- All NPCs parent to the stall sway node so they move with the platform, not against it

---

## 🖥️ Sprite Sheet 5: UI, Effects & Accessibility
**File:** `leugen_ui_effects.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #E63946, #2D6A4F, #E9C46A, #6E7B78

### Core UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bulb Selection UI (variety browser) | (0, 0) | 256x192 | Eight varieties with colour, height and price |
| Purchase Confirmation ("Bag acquired") | (256, 0) | 128x96 | Warm, celebratory, entirely sincere |
| Growing Instructions Panel | (384, 0) | 128x96 | Dutch primary, English section conspicuously short |
| Customs Warning (subtle, easily missed) | (256, 96) | 128x32 | Rendered at low contrast on purpose; still readable if sought |
| Bulb Burden Inventory Icon | (384, 96) | 32x32 | Persistent slot occupant |
| Grow-Success Probability Readout | (416, 96) | 96x32 | Shown only in the epilogue, never at point of sale |
| Bravado Prompt — "Do you have a garden?" | (256, 128) | 256x64 | The question that costs Bravado to answer honestly |
| Tulip Fate Epilogue Panel | (0, 192) | 192x128 | Frames the five-stage epilogue reveal |
| Customs Encounter Panel | (192, 192) | 192x128 | Declare / Hide / Forget About Them |
| Value Bag Comparison Chart | (384, 192) | 128x128 | Per-bulb maths that makes the 50 Sovs case |
| Price Tag Popup | (0, 320) | 96x32 | 3–50 Sovs |
| Bulk Discount Negotiation Bar | (96, 320) | 160x32 | Bravado-gain path; Margriet enjoys the attempt |
| Achievement Track Panel | (256, 320) | 256x96 | Five botanical stages |
| Deflection Plate | (0, 352) | 256x64 | "Wonderful choice. Would you like a bag?" |

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Petal Fall 1-3 | (0, 416) / (48, 416) / (96, 416) | 48x48 each | Continuous, gentle, from the hanging baskets |
| Pollen Float 1-2 | (144, 416) / (192, 416) | 48x48 each | Fine gold drift in the market light |
| Canal Sparkle 1-2 | (240, 416) / (288, 416) | 48x48 each | Water glints under the platform |
| Bag Rustle Motion Lines | (336, 416) | 64x48 | Paper handling during bagging |
| Register Chime Sparkle | (400, 416) | 64x48 | Card reader confirmation |
| Sway Motion Marker | (464, 416) | 48x48 | Reduced-motion substitute glyph for the platform roll |

### Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| High-Contrast Bin Outline | (0, 464) | 48x48 | Bold marker for the eight bulb bins |
| High-Contrast Counter / Exit Outline | (48, 464) | 48x48 | Transaction point and gangplank markers |
| Reduced-Motion Static Stall Plate | (96, 464) | 96x48 | Sway disabled; stall held level |
| Reduced-Motion Static Water Plate | (192, 464) | 96x48 | Ripple cycle replaced with a still surface |
| Colorblind Variety Pattern Swatches (8) | (288, 464) | 128x48 | Hatching per tulip variety, matched across bins, bags and UI |
| Visual Cue: Canal Lap | (416, 464) | 32x32 | Water audio mirror |
| Visual Cue: Register | (448, 464) | 32x32 | Transaction audio mirror |
| Visual Cue: Bag Rustle | (480, 464) | 32x32 | Bagging audio mirror |

### Technical Notes:
- Grow-Success Probability is deliberately withheld from the purchase UI — surfacing it at point of sale would defuse the entire location
- The Customs Warning panel renders at 45% opacity against the stall background; it is legible on inspection and invisible in normal play, which is exactly the joke
- Achievement Track Panel shares its nine-slice frame with other Shamsterdam vendor locations for visual consistency
- Sway Motion Marker replaces motion with a static glyph rather than removing the feedback entirely

---

## 🎬 Animation Specifications

### Stall Sway (Sheets 1, 4):
- **Duration:** 5.0 seconds per full cycle (2 frames crossfaded, with node rotation interpolating between them at ±1.5°)
- **Frames:** 2 platform + 2 awning
- **Pattern:** Continuous sine roll; amplitude doubles for 3 seconds on Canal Boat Passing, then eases back
- **Trigger:** Constant while location loaded
- **Purpose:** "Slight swaying, adds to dreamlike purchasing haze" — the floor is water and the decision-making follows
- **Audio Sync:** Rope creak at each sway extreme; canal lap layered under the whole cycle
- **Performance Optimization:** Static stall on Low LOD (profile-mandated static water and simplified stall)

### Canal Lap Ripple (Sheet 1):
- **Duration:** 2.5 seconds per cycle (3 frames at 1.2 FPS), continuous loop, phase-locked to the sway
- **Frames:** 3 + sparkle overlay
- **Pattern:** 1 → 2 → 3 → 2 → loop, so water and platform never desync
- **Trigger:** Constant
- **Purpose:** Grounds the floating stall as genuinely floating
- **Audio Sync:** Soft lap bed at −20 dB, peaking with the sway extremes
- **Performance Optimization:** Single static frame on Low LOD (profile-mandated static water)

### Petal Fall & Pollen Drift (Sheets 2, 5):
- **Duration:** Continuous emission; individual particles live 4-7 seconds
- **Frames:** 3 petal + 2 pollen
- **Pattern:** Petals fall from the hanging baskets and awning edge; pollen drifts laterally with the sway direction
- **Trigger:** Constant while location loaded
- **Purpose:** The beauty that closes the sale; the market is genuinely lovely and that is not the satire
- **Audio Sync:** None (bird song and market murmur bed only)
- **Performance Optimization:** Petals 10 → 5 on Medium, all particles disabled on Low (profile-mandated reduced particles)

### Margriet's Presenting Gesture (Sheet 4):
- **Duration:** 1.8 seconds (3 frames at ~1.7 FPS), single play
- **Frames:** 3
- **Pattern:** Reach into bin → lift bulb to palm height → hold, offered
- **Trigger:** Player selects a variety in the browser UI
- **Purpose:** A small ceremony performed over a brown lump; her sincerity is what makes the purchase happen
- **Audio Sync:** Bulb rustle in the bin on frame 1; warm VO line lands on the hold
- **Performance Optimization:** None needed

### The Customs Deflect (Sheets 4, 5):
- **Duration:** 2.4 seconds (3 frames at 1.25 FPS), single play, strict order
- **Frames:** 3 + deflection dialogue plate
- **Pattern:** Eye contact breaks → hand redirects to the protective bag → sale resumes, warmth fully restored
- **Trigger:** Player asks any customs, climate, or import question
- **Purpose:** "The Margriet Method: answer the question you wish they'd asked" — the single most precise piece of characterisation in the location
- **Audio Sync:** Brief audio hesitation (0.4 second gap in the market bed) on frame 1, then the deflection line over frame 3
- **Performance Optimization:** None needed

### Bagging Sequence (Sheets 3, 4):
- **Duration:** 2.4 seconds (Piet's 3 frames at 1.25 FPS + bag rustle lines), single play
- **Frames:** 3 + rustle overlay
- **Pattern:** Scoop → fill → fold and hand over, then the Bulb Burden sprite enters inventory
- **Trigger:** Purchase confirm
- **Purpose:** The transfer of hope into paper, performed with genuine care by someone who says nothing about it
- **Audio Sync:** Paper rustle on frames 2-3; register chime on the inventory drop
- **Performance Optimization:** None needed

### Bulb Burden Degradation (Sheet 3):
- **Duration:** Instant state swaps at day thresholds; no in-frame animation
- **Frames:** 3 states (fresh → dusty → desiccated)
- **Pattern:** Fresh at purchase, dusty after 7 in-game days, desiccated in the epilogue
- **Trigger:** In-game day counter, independent of player action
- **Purpose:** The item ages whether or not anyone looks at it — which is precisely what happens to real bulbs
- **Audio Sync:** None
- **Performance Optimization:** None needed

### The Planting Epilogue (Sheet 3):
- **Duration:** 8.0 seconds total (frames 1-4 at 1.5 seconds each, plus a 2-second hold on the outcome frame)
- **Frames:** 5 (frame 5 fires on a 1% roll)
- **Pattern:** Somewhere Safe → Two Months → Two Years → Quiet Disposal, or a branch to The 1%
- **Trigger:** Post-credits or future-game reference
- **Purpose:** The location's punchline, delivered months of game-time after the joke was set up
- **Audio Sync:** Market ambience fades to domestic room tone across frames 1-3; frame 5 restores a single bird call
- **Performance Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bin Outline | Sheet 5, (0, 464) | 48x48 | Bold marker distinguishing the eight bulb bins in a very busy colour field |
| Counter / Exit Outline | Sheet 5, (48, 464) | 48x48 | Transaction point and gangplank exit |
| Variety Label Plates | Sheet 2, (896, 96) | 128x96 | Black-on-cream lettering, deliberately the highest-contrast art on the stall |
| Deck Edge Marker | Sheet 1, Canal Edge Post | 32x96 | Bold post silhouette marking the water boundary |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Reduced-Motion Static Stall Plate | Sheet 5, (96, 464) | 96x48 | Sway node locked to 0°; the stall is held level for the whole visit |
| Reduced-Motion Static Water Plate | Sheet 5, (192, 464) | 96x48 | Ripple cycle held on frame 1, sparkle overlay disabled |
| Sway Motion Marker | Sheet 5, (464, 416) | 48x48 | Static glyph retains the "you are on water" information without the movement |
| Petal Fall Suppression | Sheet 5, (0, 416) | 48x48 | Particles disabled; a still petal-scatter decal is used on the deck instead |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Canal Lap | Sheet 5, (416, 464) | 32x32 | Water glyph pulsing with the lap rhythm |
| Register | Sheet 5, (448, 464) | 32x32 | Card reader confirmation |
| Bag Rustle | Sheet 5, (480, 464) | 32x32 | Paper handling during the bagging sequence |
| Rope Creak (sway extreme) | Sheet 1, Mooring Rope + Cleat | 128x64 | Rope sprite flashes a one-frame highlight at each creak |
| Customs Hesitation Gap | Sheet 5, (0, 352) | 256x64 | Deflection plate appears with a held blank beat, mirroring the audio pause |
| Distant Boat Bell | Sheet 1, Canal Boat Passing | 128x128 | Boat sprite carries a bell glyph on approach |

### Colorblind Considerations:
- The eight tulip varieties are distinguished by petal silhouette (cup / fringed / pointed / striped) and by hatching swatch, never by bloom colour alone — this matters because colour is literally the product here
- Bulb Burden's three degradation states differ by shape and surface texture (plump / creased / shrivelled), not by brown-tone shift
- Grow-success outcomes in the epilogue use distinct frames and text, never a red/green result colour
- Price signs use numerals and chalk-slate contrast; no colour-coded pricing tiers
- Touch zones minimum 44px for all eight bins, the sample garden, both value-bag stacks, the wooden tulip rack, the seed rack, and every purchase button

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) the five signage sprites, the fine-print card, and the variety label plates need higher-quality blocks — every one of them is a text gag
- **Fallback:** PNG-24 high quality for the signage band of `botanische_leugen_stall.png` (the 1637 plaque, the orphan asterisk, and the two tiny disclaimers) and for `leugen_bulb_displays.png` (the sample-garden vs. bulb-bin visual gap is the location's core mechanic and must not be muddied)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| leugen_environment | botanische_leugen_stall, leugen_bulb_displays | 2048x1280 |
| leugen_characters | npc_leugen_cast | 1024x512 |
| leugen_objects_ui | leugen_items, leugen_ui_effects | 1024x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full sway with boat-wake spikes, 3-frame water ripple plus sparkle, 10 petals and full pollen drift, all 8 varieties visible in bins, 4 customer NPCs |
| Medium | Sway retained at reduced amplitude, 2-frame water, 5 petals, no pollen, 8 varieties retained, 3 customer NPCs |
| Low | Static stall and static water, no particles, simplified flower variety (4 bins visible), staff plus 1 customer NPC (profile-mandated static water, simplified variety, reduced particles) |

### Performance Targets:
- **Target FPS:** 60 (per location profile performance budget)
- **Max Draw Calls:** 14 per frame (per location profile)
- **Memory Footprint:** 34 MB maximum (per location profile)
- **Particle Limit:** 18 (petal fall, pollen drift, canal sparkle combined)

### Performance Notes:
- The entire stall — structure, awning, displays, props and NPCs — parents to one sway node with a single rotation driver script; there is no per-sprite motion anywhere in this location
- Adjacent stall sprites are static backdrop, never animated, and are the first thing culled if the draw-call ceiling is approached
- Cut Flower Buckets are two composed sprites rather than dozens of individual blooms; the colour overwhelm is painted, not instanced
- Bulb bin fill levels update by swapping the row sprite, not by removing individual bulb sprites

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Node2D sway parent with a single rotation driver (everything on the stall is a child), Sprite2D (stall structure, displays, backdrop), TileMap (deck planking), AnimatedSprite2D (Margriet, Piet, customers, water ripple), CPUParticles2D (petals, pollen, sparkle — not GPU), CanvasModulate (market-hour light), Area2D interaction hotspots sized ≥44px
- Special systems: variety-browser purchase flow with per-item grow-success values stored but not displayed, the Vendor's Dance deflection state machine (customs / climate / soil questions all route to the same three-frame response), Bulb Burden persistent inventory item with a day-driven three-state degradation, optional customs-checkpoint resolver (Declare 50/50, Hide 20/80, Forget), post-credits planting epilogue with a weighted five-outcome roll, bulk-discount negotiation Bravado check, five-stage achievement tracker

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Sway extremes | Rope creak | At each ±1.5° peak |
| Canal Lap Ripple | Water lap bed | Phase-locked to the sway cycle |
| Margriet Presenting frame 1 | Bulb rustle in the bin | On frame display |
| Margriet Presenting hold | Warm VO line | On the held frame |
| Customs Deflect frame 1 | 0.4 second gap in the market bed | On frame display |
| Customs Deflect frame 3 | "They travel very well!" VO | On frame display |
| Piet Bagging frames 2-3 | Paper rustle | On frame display |
| Purchase confirm | Card reader chime | On inventory drop |
| Canal Boat Passing | Distant boat bell, then wake | Bell on approach, wake on the sway amplitude spike |
| Epilogue frames 1-3 | Market ambience crossfading to room tone | Across the 4.5 second sequence |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Botanical Achievement Track | Achievement token strip, purchase confirmation, wooden tulip, epilogue frames | Five stages: Hope Planter / Old Master Aspirant / Realist / Attempted Gardener / Botanical Miracle Worker |
| The Bulb Burden | Bulb Burden three-state item, inventory icon, drawer and suitcase props | Persistent inventory slot from purchase to epilogue |
| The Customs Reality (optional) | Customs Encounter Panel, declaration form, protective bag, CITES permit | Airport checkpoint if implemented; Declare / Hide / Forget branches |
| The Planting Epilogue | Epilogue frames 1-5, desiccated bulb, bulb sprout, probability readout | Post-credits reveal; grow-success values finally surfaced |
| Bulk Discount Negotiation | Negotiation bar, Margriet warm upsell frames | Bravado-gain path at the counter |
| Souvenir Psychology Network | Wooden tulip, souvenir bag, windmill bag face | Shared purchase-logic thread with wooden shoes and bicycle bell vendors |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Stroopwafel Cart | Contrast pairing — the purchase that delivers vs. the purchase that hopes; shared market deck tiles | Adjacent market walk; deck tiles continue seamlessly |
| Klompen Konfessional / wooden-shoe vendors | Wooden Tulip and souvenir bag share the "buy the Dutch icon, never use it" item logic and UI frame | Souvenir Psychology Network dialogue hook |
| Shamsterdam Bike Rental | Bicycle bell souvenir shares the same purchase-for-the-memory pattern; shared achievement panel frame | Cross-vendor achievement reference |
| Canal Ring Promenade | Canal water surface, ripple frames and boat sprite shared | Seamless canal-side walk-off |
| The Tolerance Hostel | Bulb Burden and souvenir bag visible in bunk-room inventory scenes | Bag prop carries into hostel dialogue |
| Airport / Customs (if implemented) | Customs Encounter Panel, declaration form, suitcase-with-bulbs prop | Departure scene resolves the Bulb Burden |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Four hundred years of the Dutch selling hope by the bulb, on a platform that gently moves so you cannot quite think straight"
- **Color Mood:** Saturated tulip red and petal pink against canal slate and bulb brown — the flowers are the brightest thing on screen and the bulbs are the dullest, which is the entire transaction
- **Lighting:** Soft overcast market light with gold warmth under the awning; the sample garden is lit noticeably better than the bins, because of course it is
- **Texture:** Wet planking, papery bulb skin, waxed paper bags, chalk on slate; everything is either freshly beautiful or quietly agricultural

### Environmental Storytelling:
- The sign says 1637 and the family has run the stall since 1962 — the older date is doing marketing work and the plaque is small enough to be plausible
- The asterisk after "BULBS TRAVEL WELL" has no matching footnote anywhere on the stall; a player who goes looking will not find one
- The customs notice is printed in the smallest type on the stall and is, technically, entirely honest
- The sample garden's tulips are visibly healthier than anything in the bins because they were grown by professionals, in the Netherlands, in ideal conditions — nobody is lying, and nobody is explaining
- The bags are genuinely beautiful and genuinely worth keeping, which is the only part of the purchase that reliably delivers

### Character Integration Notes:
- Margriet's warmth is real in every frame; she is not a con artist and must never be drawn as one. She answers the question she wishes you had asked, and she means the answer.
- The only frames where she breaks eye contact are the three Customs Deflect frames — that break is the whole character
- Piet has the narrowest expression range on the sheet by design; he handles bulbs, his aunt handles questions
- The Honeymooners are drawn with real tenderness — they make the satire bittersweet rather than mean
- The Experienced Gardener and the Customs-Aware Tourist are the two competent customers, and both are placed at the visual edges of the composition where the bros will never look

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Sample Garden vs. The Bins** - Side by side, no caption needed
2. **"TULPEN SINDS 1637"** - The date, the plaque, the four-century flex
3. **The Orphan Asterisk** - "BULBS TRAVEL WELL*" with no footnote in frame or out of it
4. **The Customs Deflect** - Margriet's mid-frame eye-contact break, caught as a still
5. **The Desiccated Bulb Epilogue** - Two years later, found during a move
6. **The 1% Frame** - A single actual Dutch tulip, in an actual pot, that almost no player will ever see

### Quote Potential:
- "I sell dreams. Dreams are legal in every country. Dreams need no customs form."
- "1637, people traded houses for tulip bulbs. Now, five Sovs. Progress? Maybe. Romance? Less."
- "A pot works too! A windowsill! A dream!"
- "They travel very well! Would you like the protective bag? Two Sovs extra."
- "I'll put them in the bag. Careful, they're fragile. Like dreams."
- "My grandmother sold to your grandmothers. The bulbs change. The hope is the same."
- "Results not guaranteed outside maritime climates."

---

## 📋 Required PNG Files (5 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | botanische_leugen_stall.png | 1024x768 |
| 2 | leugen_bulb_displays.png | 1024x512 |
| 3 | leugen_items.png | 512x512 |
| 4 | npc_leugen_cast.png | 1024x288 |
| 5 | leugen_ui_effects.png | 512x512 |

**Total Estimated Memory:** ~8.1 MB raw RGBA texture data (~3.6 MB after VRAM compression); ~34 MB maximum total runtime footprint per the location performance budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `botanische_leugen_stall.png` (1024x768)
- [ ] `leugen_bulb_displays.png` (1024x512)
- [ ] `leugen_items.png` (512x512)
- [ ] `npc_leugen_cast.png` (1024x288)
- [ ] `leugen_ui_effects.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + sway-node hierarchy guide (everything on the stall is a child of one rotation driver) + tulip variety reference chart (silhouette, palette and hatching swatch for all eight)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (#E63946, #2D6A4F, #FFB4A2, #8B4513, #6E7B78, #E9C46A)
- [ ] The sample garden reads as visibly, unmistakably healthier than the bulb bins at phone scale
- [ ] Key gags read clearly: the 1637 plaque, the orphan asterisk, both tiny disclaimers, the four-line English instruction section, the desiccated epilogue bulb
- [ ] Accessibility visual alternatives included for all audio cues (canal lap, register, bag rustle, rope creak, customs hesitation, boat bell)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (tourist souvenir psychology, never the Dutch flower industry or Margriet's family trade)
- [ ] Margriet's warmth is genuine in every frame except the three Customs Deflect frames; she is never drawn as a con artist
- [ ] Hidden areas/interactions have discoverable visual cues (orphan asterisk, tiny customs notice, fine-print card, CITES permit in the Gardener's hand)
- [ ] Performance optimized (single sway driver, 18-particle ceiling, three atlases, painted colour mass rather than instanced blooms)
- [ ] Touch zone sizing considered (44px minimum on all bins, racks, sample garden, and purchase buttons)
- [ ] Colorblind-friendly alternatives available where color codes meaning (variety silhouettes and hatching — critical here, since colour is the product)
- [ ] Social media viral potential maximized in composition choices (sample-garden-vs-bins framing, asterisk close-up, epilogue sequence)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | All in-world signage reads "Shamsterdam"; the profile's Holland and Bloemenmarkt references are design commentary, never asset text |
| Cultural Specificity | ✅ | Dutch floating flower-market tradition, Tulip Mania's 1637 callback, family-stall economics, canal-market setting |
| Satirical Targets Appropriate | ✅ | Punches at tourist souvenir logic and agricultural ignorance; Margriet, Piet and the Dutch flower trade are rendered warm, skilled and legitimate |
| Seedy Underbelly Present | ✅ | Selling agricultural goods to people who cannot legally import or successfully grow them, the 2 Sovs protective-bag deflection, the 50 Sovs collection at 0.1% success, outcomes never tracked |
| Gameplay Value Established | ✅ | Purchase system, Vendor's Dance deflection dialogue, persistent Bulb Burden, Bravado negotiation, optional customs encounter, five-stage epilogue and achievement track |
| Technical Feasibility | ✅ | Single sway-node hierarchy, phase-locked water, painted flower mass, day-driven item degradation all documented |
| Performance Budget | ✅ | 60 FPS, 14 draw calls, 34 MB per profile budget |
| Accessibility Features | ✅ | Six visual audio cues, reduced-motion sway/water/petal alternatives, variety silhouettes and hatching for a colour-dependent product, 44px zones |
| No Crypto Elements | ✅ | Cash, card, and four hundred years of botanical hope |
| Social Media Integration | ✅ | Six screenshot moments plus a seven-line quote bank identified |

**Once these assets are delivered, De Botanische Leugen becomes Eurobound's slowest-burning joke: a beautiful, gently rocking stall where a kind woman sells you something real, you carry it across a continent, and the punchline arrives two years later in a drawer you were cleaning out for a completely unrelated reason.**
