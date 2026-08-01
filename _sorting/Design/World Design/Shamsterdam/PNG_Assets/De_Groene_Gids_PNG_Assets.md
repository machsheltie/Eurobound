# De Groene Gids - Complete PNG Asset Requirements

## 📋 Overview
De Groene Gids ("The Green Guide") is the Hard Rock Café of coffeeshops — a two-floor corner institution in the Coffeeshop Quarter with the largest neon sign in the district, a 3.1-star TripAdvisor certificate in the window, a Bob Marley poster that is functionally legally required, and a €20/gram price for what locals buy elsewhere at €10. This document specifies every PNG asset across the neon-drenched exterior, the ground-floor counter and merchandise gauntlet, the "VIP Lounge" upstairs that is the same room, the merchandise and consumable objects, Budtender Bas and the full staff and customer cast, the space-cake timer and Tourist Trapped UI, and the permanent green haze. Its satirical essence in a sentence: famous for being famous, expensive for being expensive, and precisely the experience you deserve for not asking a local.

**Location ID:** `shamsterdam_coffeeshop_groene_gids_01`
**Theme:** Brand-name tourism over authentic experience — corporate commodification of counterculture, merchandise margins beating menu margins, and every American mistake performed in public
**Zone:** Coffeeshop Quarter, corner location with maximum tourist visibility (green glow visible from three canals away)
**Hours:** 10 AM - 1 AM (legal operating hours, strictly enforced)
**Primary Function:** Consumable vendor / status-effect hub — strain and space-cake purchasing, cash-only ATM redirect, passport ID mini-game, the two-hour "It's Not Working" system, Tourist Trapped and Contact High status effects, merchandise upsell gauntlet, Regular/Secret Menu progression

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Coffeeshop Green | #228B22 | Walls, carpet, uniforms, branded everything |
| Neon Green | #39FF14 | Exterior sign, menu boards, display-case glow |
| Smoke Grey | #708090 | Permanent haze, ceiling, ventilation, dust motes |
| Wood Brown | #8B4513 | Bar, tables, chairs, the one honest material |
| Dead-Eye Beige | #C8BFA6 | Staff skin tones under green light, Employee of the Month board |
| Amber Haze | #D9A441 | Light-beam shafts through smoke, warm backlit menus |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/de_groene_gids/
├── environment/
│   ├── groene_gids_exterior.png
│   ├── groene_gids_ground_floor.png
│   └── groene_gids_upstairs_vip.png
├── objects/
│   └── groene_gids_merch_objects.png
├── npcs/
│   └── npc_groene_gids_cast.png
├── effects/
│   └── groene_gids_effects_haze.png
└── ui/
    └── groene_gids_ui.png
```

---

## 🟢 Sprite Sheet 1: Exterior & The Famous Sign
**File:** `groene_gids_exterior.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #39FF14, #228B22, #708090, #1A1A1A

### Facade:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Corner Facade (two-street frontage) | (0, 0) | 512x384 | Maximum visibility from every approach; the building is a billboard |
| Double Doors — Closed | (0, 384) | 96x128 | Green carpet visible through the glass |
| Double Doors — Open (green spill) | (96, 384) | 96x128 | Sweet smoke and Dutch hip-hop escaping |
| Green Carpet Strip (exterior) | (192, 384) | 128x64 | Yes, green carpet. Outside. |
| Bouncer Post Marker | (192, 448) | 128x64 | ID-check footprint at the threshold |
| Velvet Rope (never used) | (320, 384) | 64x128 | Present for implication only |
| Souvenir Shop Left | (384, 384) | 128x128 | Sells the same merch, cheaper |
| Souvenir Shop Right | (896, 416) | 128x96 | Also cheaper. Nobody checks. |

### The Neon:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Giant Neon "DE GROENE GIDS" — Lit | (512, 0) | 512x128 | Letters taller than Bradley |
| Neon — Flicker Frame A | (512, 128) | 512x128 | One letter dimmed |
| Neon — Flicker Frame B | (512, 256) | 512x128 | Different letter dimmed; nobody has fixed either |
| Sub-Sign "COFFEESHOP" | (512, 384) | 128x32 | Legally the important one |
| Sub-Sign "MENU INSIDE" | (640, 384) | 128x32 | Redundant, illuminated |
| Sub-Sign "FAMOUS SINCE 1985" | (768, 384) | 128x32 | Ownership changed in 2017 |
| Sub-Sign "AS SEEN ON TV" | (896, 384) | 128x32 | Which TV is never specified |

### Window Credentials:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Window Sticker Collage | (512, 416) | 192x96 | Every travel show logo ever printed |
| TripAdvisor Certificate (3.1 stars) | (704, 416) | 96x96 | Framed. Displayed. Three point one. |
| "TOURIST FRIENDLY!" Decal | (800, 416) | 96x48 | The quiet part, printed |
| Bachelor-Party Queue Silhouettes | (800, 464) | 96x48 | Matching shirts, constant stream |

### Technical Notes:
- The neon is the location's identity: three full-width 512x128 frames rather than a shader flicker, so the dead letters read as specifically, permanently broken
- Green light pollution wash lives on the effects sheet and is applied as a full-screen additive layer over the whole exterior scene
- Sub-signs are separate sprites so localisation can swap text without touching the facade
- The two souvenir shops flank the entrance in the layout to make the "cheaper on either side" gag visible in a single wide screenshot

---

## 🏪 Sprite Sheet 2: Ground Floor — Counter, Menu & Merchandise Gauntlet
**File:** `groene_gids_ground_floor.png`
**Dimensions:** 1024x768 pixels
**Color Palette:** #228B22, #8B4513, #708090, #39FF14

### Counter & Displays:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ground Floor Interior Base (wide) | (0, 0) | 512x256 | Green-tinted everything, including the souls of the employees |
| Long Wooden Bar / Counter | (512, 0) | 256x128 | The one honest material in the building |
| Glass Display Case — Product (stylized) | (768, 0) | 256x128 | Abstract jars and cards; no product rendered literally |
| Counter Service Area | (512, 128) | 256x128 | Where the scripted responses happen |
| Display Case — Branded Bongs | (768, 128) | 256x128 | Priced like fine jewelry, lit like fine jewelry |

### Menu, ATM & Wall Décor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Digital Menu Board — Frame 1 | (0, 256) | 192x256 | Scrolling strain names, "TOURIST RECOMMENDATIONS" highlighted |
| Digital Menu Board — Frame 2 | (192, 256) | 192x256 | Second scroll position |
| Menu Board — Static (mobile fallback) | (384, 256) | 192x256 | Low-LOD non-scrolling variant (profile-mandated static menu option) |
| Branded ATM Machine | (576, 256) | 128x256 | €50 minimum withdrawal, €4.50 fee, branded green |
| Wall — Green-Tinted Panel (tileable) | (704, 256) | 128x128 | Base wall |
| Wall — Panel With Grime | (832, 256) | 128x128 | Shoulder-height wear variant |
| Bob Marley Poster | (960, 256) | 64x128 | Legally required in tourist coffeeshops |
| Polaroid Wall | (704, 384) | 192x128 | Tourists making the same face since 1985 |
| "Employee of the Month" Board | (896, 384) | 128x128 | Same guy since 2019, dead-eyed |

### Floor, Seating & Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Green Carpet Tile | (0, 512) | 32x32 | Base flooring |
| Green Carpet Tile (worn path) | (32, 512) | 32x32 | Door-to-counter-to-merch route |
| Wood Floor Tile | (64, 512) | 32x32 | Under the bar only |
| Bar Foot Rail | (96, 512) | 128x32 | Brass, polished by boots |
| Fake Plant A | (224, 512) | 64x128 | Real ones died from irony |
| Fake Plant B | (288, 512) | 64x128 | Second variant, dustier |
| Branded Ashtray | (352, 512) | 64x64 | Branded. Everything is branded. |
| Vintage "Famous Visitors" Photo Frame | (352, 576) | 64x64 | None you'd recognise |
| Branded Chair 1-2 | (416, 512) / (480, 512) | 64x128 each | Somehow the chairs are branded too |
| Round Table (green) | (544, 512) | 96x96 | Ring-stained, wobbling |
| Lighter/Ashtray Clutter Decal | (544, 608) | 96x32 | Tabletop scatter |
| Bench Seating Segment | (640, 512) | 192x96 | Communal, uncomfortable, always full |
| Ventilation Grille ("decorative") | (640, 608) | 192x32 | Working overtime, achieving nothing |
| "NO TOBACCO" Sign (12 languages) | (832, 512) | 192x64 | Americans need all 12 |
| Stairs Up To "VIP" | (832, 576) | 192x64 | €10 surcharge, one flight |

### Lighting & Exit Path:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ground Floor Green Light Rig | (0, 640) | 256x128 | Green bulbs, green shades, sickly glow |
| Backlit Menu Glow Plate | (256, 640) | 192x128 | The brightest thing in the room is the price list |
| Display Case Spotlight Cone | (448, 640) | 128x128 | Jewelry-store lighting on the bong case |
| Bar Under-Glow Strip | (576, 640) | 192x64 | Neon green underlighting |
| Queue Rope + Floor Decal | (576, 704) | 192x64 | Managed flow at peak tourist hours |
| Bag Rack (€2 bags) | (768, 640) | 96x128 | "The bag is two euros." |
| Merch Gauntlet Corridor | (864, 640) | 160x128 | The exit path routes past everything for sale |

### Technical Notes:
- The merch gauntlet is architectural: the exit corridor sprite is positioned so the player physically cannot leave without passing the T-shirt wall — this is a layout requirement, not a decoration
- Digital Menu Board frames 1-2 alternate at 0.5 FPS for the scroll; the static variant swaps in on Low LOD rather than pausing the loop
- Green Light Rig, Backlit Menu Glow and Bar Under-Glow are additive layers over the baked interior, allowing the green intensity to be dialled down for the accessibility green-tint reduction toggle
- The product display case is deliberately abstract — jars, cards and silhouettes only, at every zoom level

---

## 🛋️ Sprite Sheet 3: Upstairs "VIP Lounge"
**File:** `groene_gids_upstairs_vip.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #228B22, #708090, #8B4513

### The Same Room:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "VIP Lounge" Interior Base | (0, 0) | 512x256 | Identical layout to downstairs, €10 to enter |
| Slightly Nicer Chair 1-2 | (0, 256) / (64, 256) | 64x96 each | Marginally. Provably marginally. |
| Identical Chair (downstairs, for comparison) | (128, 256) | 64x96 | Placed adjacent for direct A/B in one screenshot |
| Different Carpet Tile | (192, 256) | 32x32 | The €10 justification |
| Same Carpet Tile | (224, 256) | 32x32 | The €10 refutation |
| "VIP" Rope + Sign | (256, 256) | 96x96 | Velvet, green, unnecessary |
| €10 Surcharge Placard | (352, 256) | 96x32 | Stated plainly, without shame |
| Upstairs Window | (448, 256) | 64x96 | Green-filtered view of the street below |
| Lounge Table | (352, 288) | 96x64 | Same table. Different floor. |
| Upstairs Speaker | (192, 288) | 64x64 | Same playlist, lower volume, that is the amenity |

### Fixtures & Atmosphere:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Haze Density Overlay — Upstairs | (0, 352) | 256x160 | Thicker than downstairs; ventilation does not reach |
| Stairs Down | (256, 352) | 96x96 | The only exit |
| Space Cake Victim Seat (marked) | (352, 352) | 96x96 | Corner spot, permanently occupied |
| Ceiling Green Bulb Fixture | (448, 352) | 64x64 | Single bulb, single shade |
| Wall Tag "Same Room, Higher Price" | (448, 416) | 64x32 | Scratched into the paint by a previous customer |
| Rug (marginally nicer) | (256, 448) | 96x64 | The other €10 justification |
| Upstairs Floor Grime Decal | (352, 448) | 96x64 | Undermining both justifications |
| Ashtray (upstairs, branded) | (448, 448) | 64x64 | Identical to the downstairs ashtray |

### Technical Notes:
- The VIP base sprite is intentionally near-identical to the ground floor base; the differences (carpet tile, rug, chair) must be small enough that players screenshot the comparison
- Placing the "Identical Chair (downstairs)" sprite on this sheet is deliberate — it lets the game show both chairs side by side in the surcharge prompt UI
- Upstairs haze density is one tier above ground floor at every LOD level
- The wall tag is a discoverable detail requiring the player to walk to the far wall

---

## 👕 Sprite Sheet 4: Merchandise, Consumables & Counter Objects
**File:** `groene_gids_merch_objects.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #228B22, #39FF14, #8B4513, #C8BFA6

### The Merchandise Wall:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| T-Shirt Wall Array (S–XXXL) | (0, 0) | 384x256 | "I GOT HIGH AT DE GROENE GIDS", every size |
| T-Shirt (single, €35) | (384, 0) | 96x128 | Inventory sprite; applies +Embarrassed when worn |
| T-Shirt (glow-in-dark variant) | (480, 0) | 96x128 | "Very popular for bachelor parties" |
| Branded Grinder Display (€45) | (576, 0) | 128x128 | "Collector's item" |
| Branded Grinder (item) | (704, 0) | 64x64 | Functions identically to a €5 grinder |
| Branded Rolling Papers | (768, 0) | 64x64 | Branded. Naturally. |
| Branded Ashtray (item) | (832, 0) | 64x64 | Also branded |
| Poster (€20) | (896, 0) | 64x128 | Hostel-room decorative, −Intelligence display |
| Merch Display Shelf | (960, 0) | 64x128 | Wall unit segment |
| Bong Display Case (jewelry-priced) | (704, 64) | 128x64 | Under glass, under spotlight |
| Sizes Rack Tag Set | (384, 128) | 96x64 | "XXXL? Yes. Very popular." |
| Group Discount Sign | (480, 128) | 96x64 | "Buy four shirts, get fifth half price!" |
| Merch Price Tags | (576, 128) | 128x64 | €20 / €35 / €45 |
| Souvenir Keychain | (704, 128) | 64x64 | The cheapest exit purchase |
| Branded Lighter | (768, 128) | 64x64 | €6 for a €1 lighter |
| Branded Bag (€2) | (832, 128) | 64x64 | The bag is two euros |
| Sticker Sheet | (896, 128) | 128x64 | Free with purchase over €50 |

### Menu Items & Consumables (stylized):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu Item Card — "Shamsterdam Dream" | (0, 256) | 96x64 | €18/g, Tourist Recommended, highest margin |
| Menu Item Card — "Green Guide Special" | (96, 256) | 96x64 | €15/g, House blend, mystery |
| Menu Item Card — "Premium Heritage" | (192, 256) | 96x64 | €25/g, upsell confirmed |
| Space Cake (single piece) | (288, 256) | 64x64 | €8, two-hour countdown trigger |
| Space Cake Display Tray | (352, 256) | 128x64 | Behind glass, under a handwritten "WAIT 2 HOURS" card |
| Hash Block (1g, stylized) | (480, 256) | 64x64 | €12, "For smoking. Not eating." |
| Product Jar (stylized) 1-3 | (544, 256) / (608, 256) / (672, 256) | 64x64 each | Abstract counter jars; labels only |
| Laminated Menu (handheld) | (736, 256) | 64x96 | Decision paralysis enabler |
| Laminated Menu (open) | (800, 256) | 96x96 | Full spread, too many options |
| "Secret Menu" Card | (896, 256) | 128x64 | Same items, different names, unlocked at Regular status |

### Counter Objects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cash Register | (0, 320) | 96x64 | Ka-ching emphasis on large purchases |
| Cash Drawer Open | (96, 320) | 96x64 | Cash only, always |
| Card Machine (declined) | (192, 320) | 64x64 | Exists to point at the ATM |
| Scale (digital) | (256, 320) | 64x64 | Accurate, unglamorous |
| Passport (bro fumbling) | (320, 320) | 64x64 | ID check prop |
| Passport Fumble Frames 1-3 | (384, 320) / (448, 320) / (512, 320) | 64x64 each | Time-based mini-game; failure is embarrassment only |
| Receipt (€63 total) | (576, 320) | 64x64 | Itemized, sobering |
| Paper Bag (€2) | (640, 320) | 64x64 | Charged separately, mentioned casually |
| Rolling Tray | (704, 320) | 96x64 | Provided, branded |
| Grinder (generic €5, for comparison) | (800, 320) | 64x64 | Placed beside the €45 one in the merch UI |
| ATM Receipt (€4.50 fee) | (864, 320) | 64x64 | "We do not control the fee." |
| ID Check Placard | (928, 320) | 96x64 | "18+ — ID REQUIRED" |

### Signage & Interior Décor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "NO TOBACCO" Sign (detail) | (0, 384) | 192x64 | Twelve languages, readable close-up |
| Photography Prohibition Sign | (192, 384) | 128x64 | Interior only; the exterior sign is the product |
| Digital Menu Text Strip 1 | (320, 384) | 256x32 | Scrolling strain-name band |
| Digital Menu Text Strip 2 | (320, 416) | 256x32 | Second scroll position |
| Tourist Recommendation Highlight Bar | (576, 384) | 192x32 | Highlights the highest-margin items |
| Price Column Strip | (576, 416) | 192x32 | €15 / €18 / €25 |
| "FAMOUS SINCE 1985" Interior Plaque | (768, 384) | 128x64 | Repeated indoors, in case you missed it |
| Fake Plant (item) | (896, 384) | 64x64 | Inventory/placement sprite |
| Bob Marley Poster (item) | (960, 384) | 64x64 | Inventory/placement sprite |
| Green Bulb Fixture (item) | (0, 448) | 96x64 | Lighting prop |
| Lampshade (green) | (96, 448) | 96x64 | Lighting prop |
| Vintage "Famous Visitor" Photo | (192, 448) | 128x64 | Signed by someone illegible |
| Green Carpet Sample Swatch | (320, 448) | 128x64 | Reference tile for both floors |
| Ventilation Grille (detail) | (448, 448) | 128x64 | Close-up; visibly ineffective |
| Ashtray Overflow Decal | (576, 448) | 192x64 | Peak-hour table state |
| Wall Clock | (768, 448) | 128x64 | Staff counting down to break |
| Employee Break Countdown Chalk | (896, 448) | 128x64 | Handwritten, behind the counter, honest |

### Technical Notes:
- All product representations are abstract: labelled jars, menu cards, and stylized blocks. Nothing is rendered botanically at any zoom level.
- Menu Text Strips are separate from the Menu Board sprites so the scroll can run at a different rate than the board's backlight pulse
- The €45 branded grinder and the €5 generic grinder are drawn at matching scale and angle specifically so the price comparison UI can show them side by side
- The Employee Break Countdown Chalk is a discoverable detail — visible only from the counter interaction position

---

## 👥 Sprite Sheet 5: Staff & Customer NPCs
**File:** `npc_groene_gids_cast.png`
**Dimensions:** 1024x384 pixels
**Sprite Size:** 64x96 pixels (groups noted)

### Staff (Row 0, y=0):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Budtender Bas Idle 1-2 | (0, 0) / (64, 0) | 64x96 each | Green polo, name tag, passion extinct |
| Bas Scripted Recommendation 1-3 | (128, 0) / (192, 0) / (256, 0) | 64x96 each | "Shamsterdam Dream. Very smooth. Very popular." |
| Bas Sigh 1-2 | (320, 0) / (384, 0) | 64x96 each | The fifty-thousandth explanation |
| Bas No-Tobacco Explanation 1-3 | (448, 0) / (512, 0) / (576, 0) | 64x96 each | Exhausted-teacher cadence, in three beats |
| Bas Ringing Up | (640, 0) | 64x96 | "Your total is sixty-three euros." |
| Bas Dead-Eyed Stare | (704, 0) | 64x96 | Held frame; the fan-art frame |
| Merchandise Maven Marieke Idle 1-2 | (768, 0) / (832, 0) | 64x96 each | Same green polo, commission-based enthusiasm |
| Marieke Upsell 1-2 | (896, 0) / (960, 0) | 64x96 each | Aggressive friendliness targeting groups |

### Staff & Regulars (Row 1, y=96):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marieke Group Discount Pitch 1-3 | (0, 96) / (64, 96) / (128, 96) | 64x96 each | "Buy four shirts, get fifth half price!" |
| Marieke Holding Glow Shirt | (192, 96) | 64x96 | Presented like a prize |
| The Bouncer Idle 1-2 | (256, 96) / (320, 96) | 64x96 each | Standard bouncer, expression of "I've seen things" |
| Bouncer ID Check 1-2 | (384, 96) / (448, 96) | 64x96 each | "ID." |
| Bouncer Resigned Sigh | (512, 96) | 64x96 | "Matching shirts. Eleven guys. Bachelor party." |
| Bouncer Refusing Photo-Of-ID | (576, 96) | 64x96 | "No, a picture of your ID is not ID." |
| Repeat Tourist 1-2 | (640, 96) / (704, 96) | 64x96 each | "Bas! Hey, it's me! From last year?" |
| Local Who Made A Mistake 1-2 | (768, 96) / (832, 96) | 64x96 each | Immediate regret, quick purchase |
| Local Escape Velocity Exit | (896, 96) | 64x96 | No eye contact, straight line to the door |
| Space Cake Victim — Very Still | (960, 96) | 64x96 | Sitting perfectly upright, staring at a wall |

### Victims & Bachelor Parties (Row 2, y=192):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Space Cake Victim Slow Blink 1-3 | (0, 192) / (64, 192) / (128, 192) | 64x96 each | Three-frame blink at a quarter speed |
| Space Cake Victim Giggle | (192, 192) | 64x96 | "It's… it's working now. It's definitely working now." |
| Bachelor Party Pack Frame 1 | (256, 192) | 256x96 | 6-8 matching shirts, one designated "responsible" member |
| Bachelor Party Pack Frame 2 (photographing) | (512, 192) | 256x96 | Photographing everything, about to be told not to |
| Bachelor Party Pack Frame 3 (too loud) | (768, 192) | 256x96 | Your mirror, in matching cotton |

### The Bros (Row 3, y=288):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lord Pilsner "THE Green Guide" | (0, 288) | 64x96 | "This is HISTORIC." |
| Chadwick Filming (approached by staff) | (64, 288) | 64x96 | Ring light up, staff already moving |
| Bradley Menu Paralysis | (128, 288) | 64x96 | "Do they have a… signature blend?" |
| Bros Trio — "It's Not Working" Frame 1 | (192, 288) | 192x96 | 30 minutes in, confident |
| Bros Trio — Frame 2 (skeptical) | (384, 288) | 192x96 | 90 minutes in, drafting a review |
| Bros Trio — "OH." | (576, 288) | 192x96 | 120 minutes in |
| Tourist Filler — Menu Swivel 1-2 | (768, 288) / (832, 288) | 64x96 each | Heads turning at the board, palette-swappable |
| Tourist Filler — Seated Haze 1-2 | (896, 288) / (960, 288) | 64x96 each | Ambient occupants, palette-swappable |

### Technical Notes:
- Bas has the largest frame count in the location and the smallest emotional range; his Dead-Eyed Stare is the held default between all scripted beats
- Marieke is the only staff sprite drawn with raised eyebrows — commission is the difference and it should be visible in silhouette
- Space Cake Victim slow blink runs at 0.8 FPS, roughly a quarter of a normal blink rate; this is the location's best silent joke
- Tourist Filler sprites are palette-swapped at runtime to produce 8 apparent customers from 4 sprites
- Max 6 customer NPCs on the ground floor and 3 upstairs (16 draw-call budget); a Bachelor Party Pack counts as 3

---

## 🖥️ Sprite Sheet 6: UI Elements
**File:** `groene_gids_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #228B22, #39FF14, #708090, #C8BFA6

### The Space Cake System:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Space Cake Timer UI | (0, 0) | 192x64 | Visible two-hour countdown, game time |
| "It's Not Working" Dialogue Plate | (192, 0) | 192x96 | Available at 30-minute intervals |
| Staff Response Plate | (384, 0) | 128x96 | "It is working. You will know. Wait." / "Ninety more minutes." |

### Status Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tourist Trapped Status Icon | (0, 64) | 64x64 | +15% prices at all Shamsterdam vendors for 1 hour |
| Contact High Indicator | (64, 64) | 48x48 | Ambient AoE affecting the whole party while inside |
| Munchies Status Icon | (112, 64) | 48x48 | Post-SP-drop food drive |
| Confused Status Icon | (160, 64) | 32x32 | House blend side effect |
| "Heavy" Status Icon | (160, 96) | 32x32 | Hash movement-speed penalty |

### Transactions:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cash Only Prompt / ATM Redirect | (0, 128) | 192x96 | Card declined → machine is there |
| ATM Fee Breakdown | (192, 128) | 192x96 | €50 minimum, €4.50 fee, branded machine |
| ID Check Mini-Game Bar | (384, 128) | 128x96 | Passport fumble timing bar |
| Strain Selection Menu UI | (0, 224) | 256x160 | Tourist Recommended / House / Premium |
| Price Comparison Reveal | (256, 224) | 128x96 | €20/g here vs. €10/g elsewhere; unlocked by talking to a local |
| Merch Purchase Confirmation | (384, 224) | 128x96 | Includes the €2 bag line |
| Group Discount Calculator | (256, 320) | 256x64 | Four shirts, fifth half price, maths shown |

### Feedback & Progression:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bravado Meter (coffeeshop variant) | (0, 384) | 128x64 | Green-tinted variant of the standard meter |
| "No Tobacco" Warning Toast | (128, 384) | 192x64 | Public correction; −Bravado, no mechanical penalty |
| Photography Warning Toast | (320, 384) | 192x64 | First warning; second means leaving |
| "Regular" Status Progress (3 visits) | (0, 448) | 128x32 | Unlocks the Secret Menu |
| Secret Menu Unlock Toast | (128, 448) | 192x32 | Same items, different names |
| Purchase Total Plate | (320, 448) | 96x32 | "Your total is sixty-three euros." |
| VIP Upstairs Surcharge Prompt | (416, 448) | 96x32 | €10, with both chairs shown side by side |
| Bag Prompt | (0, 480) | 192x32 | "The bag is two euros." |
| Time-of-Day Icon Set | (192, 480) | 128x32 | Morning Lull / Peak / Evening Rush / Last Call |
| Quest / Vendor Marker Set | (320, 480) | 96x32 | Counter, merch wall, ATM markers |
| Touch Zone Ring (44px min) | (416, 480) | 96x32 | QA overlay for interactive sizing |

### Technical Notes:
- The Space Cake Timer runs on game time and persists across location changes — the player can leave, get munchies elsewhere, and the countdown continues
- "It's Not Working" only becomes selectable at 30, 60 and 90 minutes; the staff response text differs at each interval and the third is delivered without eye contact
- Price Comparison Reveal is gated behind a conversation with a local elsewhere in Shamsterdam; showing it unprompted would remove the trap
- Tourist Trapped's +15% modifier is applied by a global vendor-price hook, and its icon must remain visible in the party HUD outside this location

---

## 💨 Sprite Sheet 7: Haze, Lighting Effects & Accessibility
**File:** `groene_gids_effects_haze.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #708090, #39FF14, #D9A441

### Haze & Smoke:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Smoke Haze Overlay (tileable, heavy) | (0, 0) | 256x256 | The permanent layer; ventilation is decorative |
| Haze Density — Medium | (256, 0) | 128x128 | Medium LOD variant |
| Haze Density — Low | (384, 0) | 128x128 | Low LOD variant (profile-mandated reduced density) |
| Smoke Wisp 1-4 | (256, 128) / (320, 128) / (384, 128) / (448, 128) | 64x128 each | Individual drift particles |

### Lighting:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Green Neon Glow Bloom 1-3 | (0, 256) / (96, 256) / (192, 256) | 96x96 each | Sign bloom, three flicker-matched states |
| Green Light Pollution Wash (exterior) | (288, 256) | 224x96 | Full-screen additive; "visible from three canals away" |
| Dust Motes In Light Beam 1-2 | (0, 352) / (64, 352) | 64x64 each | Amber shafts through the haze |

### Feedback VFX:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cash Register Ka-Ching Sparkle | (128, 352) | 64x64 | Emphasised on purchases over €50 |
| Space Cake Hit Distortion Ring 1-3 | (192, 352) / (256, 352) / (320, 352) | 64x64 each | The 120-minute moment, in three expanding rings |
| Slow-Blink Vignette | (384, 352) | 128x64 | Victim-state screen edge softening |
| Floor-Moving Warp Vignette Corner | (0, 416) | 64x64 | Mirrored 4x at runtime; "WHY IS THE FLOOR MOVING" |

### Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| High-Contrast Counter Outline | (64, 416) | 64x64 | Bold marker for the service point in a hazy, green-washed room |
| High-Contrast Exit / Stairs Outline | (128, 416) | 64x64 | Door and VIP stairs markers |
| Reduced-Motion Static Haze Plate | (192, 416) | 96x64 | Non-drifting haze substitute |
| Reduced-Motion Static Neon Plate | (288, 416) | 96x64 | Flicker held on the fully-lit frame |
| Colorblind Strain Pattern Swatches | (384, 416) | 128x64 | Hatching per menu tier, matched in board, cards and UI |
| Visual Cue: Cash Register | (0, 480) | 32x32 | Ka-ching audio mirror |
| Visual Cue: Lighter Flick | (32, 480) | 32x32 | Ambient audio mirror |
| Visual Cue: Menu Board Scroll | (64, 480) | 32x32 | Digital scroll audio mirror |
| Visual Cue: Ventilation Hum | (96, 480) | 32x32 | Constant background hum indicator |
| Visual Cue: Staff Sigh | (128, 480) | 32x32 | Bas's exhaustion, made visible |
| Visual Cue: Space Cake Onset Sting | (160, 480) | 32x32 | The 120-minute audio distortion mirror |
| Visual Cue: Bouncer "ID" | (192, 480) | 32x32 | Door-check prompt mirror |
| Touch Zone Ring (44px min) | (224, 480) | 64x32 | QA overlay for interactive sizing |
| Dutch Hip-Hop Loop Marker | (288, 480) | 96x32 | Beat pips for deaf players; loops every 47 minutes |
| Green-Tint Reduction Toggle Swatch | (384, 480) | 128x32 | Accessibility option reducing the green wash intensity |

### Technical Notes:
- The green tint is applied as a CanvasModulate plus additive glow layers, never baked into the base art, so the accessibility green-tint reduction toggle can lower it without shipping a second art set
- Haze uses three pre-authored density plates rather than a variable particle count, keeping the LOD switch to a single texture swap
- Space Cake Hit Distortion is the only screen-warp effect in the location; it plays once, lasts 2 seconds, and is fully disabled in reduced-motion mode with the sting icon substituted
- Dust Motes only render inside the two amber light shafts, never room-wide

---

## 🎬 Animation Specifications

### Neon Sign Flicker (Sheets 1, 7):
- **Duration:** 4.0 second irregular cycle (3 frames on a non-uniform schedule: lit 2.6s, flicker A 0.2s, lit 0.9s, flicker B 0.3s)
- **Frames:** 3 + 3 bloom states
- **Pattern:** Deliberately arrhythmic so it reads as broken, not animated
- **Trigger:** Constant, exterior only
- **Purpose:** The largest sign in the district, with two letters nobody has repaired since the 2017 ownership change
- **Audio Sync:** Faint neon buzz, with a transformer tick on each flicker frame
- **Mobile Optimization:** Held on the fully-lit frame in reduced-motion mode; retained at all LOD tiers otherwise (it is the location's landmark)

### Smoke Haze Drift (Sheet 7):
- **Duration:** Continuous; individual wisps live 6-9 seconds
- **Frames:** 4 wisps over 1 of 3 density plates
- **Pattern:** Slow lateral drift with a slight upward bias toward the non-functional ventilation grille
- **Trigger:** Constant while inside; density one tier higher upstairs
- **Purpose:** "Permanent haze (ventilation is decorative)" — the room's defining physical property
- **Audio Sync:** Ventilation hum bed, working audibly hard
- **Mobile Optimization:** Density plate swaps High → Medium → Low; wisp particles disabled entirely on Low (profile-mandated simplified smoke)

### Digital Menu Scroll (Sheets 2, 4):
- **Duration:** 2.0 second loop (2 board frames plus 2 text strips at 0.5 FPS)
- **Frames:** 2 + 2
- **Pattern:** Continuous scroll; the "TOURIST RECOMMENDATIONS" highlight bar never scrolls off screen
- **Trigger:** Constant, ground floor
- **Purpose:** The brightest, most confident object in the room is the price list
- **Audio Sync:** Faint digital scroll tick on each frame change
- **Mobile Optimization:** Static menu board variant on Low LOD (profile-mandated static menu option)

### Bas's Sigh & No-Tobacco Explanation (Sheets 5, 7):
- **Duration:** Sigh 1.2 seconds (2 frames at 1.7 FPS); No-Tobacco explanation 3.6 seconds (3 frames at ~0.83 FPS), single play
- **Frames:** 2 + 3
- **Pattern:** Sigh → three-beat explanation → return to Dead-Eyed Stare
- **Trigger:** Tobacco-mixing attempt, or any question answered by the menu descriptions
- **Purpose:** Professional exhaustion as a service standard; the correction is public and costs Bravado
- **Audio Sync:** Flat-monotone VO across all three beats; a single audible exhale before beat 1
- **Mobile Optimization:** None needed

### Space Cake Victim Slow Blink (Sheet 5):
- **Duration:** 3.6 seconds per blink (3 frames at 0.83 FPS), looping with 5-9 second gaps
- **Frames:** 3 + slow-blink vignette
- **Pattern:** Eyes close over a full second, hold, reopen; no other movement anywhere in the sprite
- **Trigger:** Constant while the victim NPC is present (always, at every hour)
- **Purpose:** The quietest and best joke in the building; a preview of the player's own next two hours
- **Audio Sync:** None — the silence around him is the point
- **Mobile Optimization:** None needed

### The Two-Hour Space Cake System (Sheets 4, 6, 7):
- **Duration:** 120 minutes of game time; onset effect is 2.0 seconds (3 distortion rings at 1.5 FPS)
- **Frames:** 3 distortion rings + warp vignette + 3 bros-trio reaction frames
- **Pattern:** Timer runs → "It's Not Working" dialogue available at 30/60/90 → at 120 the rings fire, the warp vignette engages, and the trio hits its "OH." frame
- **Trigger:** Space cake purchase and consumption; the timer persists across location changes
- **Purpose:** The location's structural joke, paid off two hours later, probably somewhere else entirely
- **Audio Sync:** Slightly distorted sound design ramps across the ring sequence; the music bed pitch-bends 4% down and stays there
- **Mobile Optimization:** Warp vignette reduced to a static corner overlay on Low LOD; fully disabled in reduced-motion mode with the onset sting icon substituted

### Passport Fumble ID Check (Sheets 4, 6):
- **Duration:** 4.0 second window (3 frames cycling at 1.5 FPS against a timing bar)
- **Frames:** 3 + timing bar
- **Pattern:** Fumble loop while the player taps to align; failure loops twice more and resolves anyway
- **Trigger:** Door entry, every visit until Regular status
- **Purpose:** "Bros fumble with passports for comedic effect" — failure costs nothing but dignity
- **Audio Sync:** Zip, paper shuffle, and a Bouncer "ID." on the second failure
- **Mobile Optimization:** None needed

### Marieke's Upsell Pitch (Sheet 5):
- **Duration:** 2.4 seconds (3 frames at 1.25 FPS), single play
- **Frames:** 3
- **Pattern:** Approach → shirt presented → held offer, aimed at whichever party member has the highest gold
- **Trigger:** Party of 3+ enters the merch gauntlet corridor
- **Purpose:** Commission-based enthusiasm as the building's only remaining sincerity
- **Audio Sync:** Bright VO over frame 2; hanger rattle on frame 1
- **Mobile Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Outline | Sheet 7, (64, 416) | 64x64 | Bold service-point marker; essential in a green-washed, hazy room |
| Exit / Stairs Outline | Sheet 7, (128, 416) | 64x64 | Door and VIP staircase markers |
| Green-Tint Reduction Toggle Swatch | Sheet 7, (384, 480) | 128x32 | Lowers the CanvasModulate green intensity without swapping art |
| Menu Board Static (high legibility) | Sheet 2, (384, 256) | 192x256 | Non-scrolling variant doubles as the readability option |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Reduced-Motion Static Haze Plate | Sheet 7, (192, 416) | 96x64 | Drift disabled; haze held still |
| Reduced-Motion Static Neon Plate | Sheet 7, (288, 416) | 96x64 | Flicker held on the fully-lit frame |
| Warp Vignette Disable | Sheet 7, (0, 416) | 64x64 | Space cake onset screen-warp replaced with a static corner overlay |
| Menu Scroll Hold | Sheet 2, (384, 256) | 192x256 | Static board substituted for the scrolling frames |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cash Register | Sheet 7, (0, 480) | 32x32 | Ka-ching glyph, emphasised on purchases over €50 |
| Lighter Flick | Sheet 7, (32, 480) | 32x32 | Ambient room-activity indicator |
| Menu Board Scroll | Sheet 7, (64, 480) | 32x32 | Digital tick mirror |
| Ventilation Hum | Sheet 7, (96, 480) | 32x32 | Constant-presence indicator for the overworked extractor |
| Staff Sigh | Sheet 7, (128, 480) | 32x32 | Bas's exhaustion; the Bravado consequence must be readable without audio |
| Space Cake Onset Sting | Sheet 7, (160, 480) | 32x32 | Mirrors the distorted 120-minute audio cue and substitutes for the warp in reduced-motion mode |
| Bouncer "ID" | Sheet 7, (192, 480) | 32x32 | Door-check prompt |
| Dutch Hip-Hop Loop Marker | Sheet 7, (288, 480) | 96x32 | Beat pips so deaf players can perceive the 47-minute loop repeating |

### Colorblind Considerations:
- The three menu tiers are distinguished by hatching swatch and card shape on the board, the menu cards, and the strain-selection UI — never by green-intensity alone, which is unusable in this location's palette
- Status effects (Tourist Trapped, Contact High, Munchies, Confused, Heavy) use distinct silhouettes readable at 32px in greyscale
- The green-tint reduction toggle is offered explicitly because this location's entire palette sits in one hue band
- Space Cake Timer shows numerals and a segmented bar, never a colour-shifting fill
- Price Comparison Reveal uses numerals and bar length, not red/green framing
- Touch zones minimum 44px for the counter, menu board, ATM, merch wall, stairs, and every purchase button

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (fallback PVRTC 4BPP); the exterior neon, the digital menu text strips, the 12-language NO TOBACCO sign and the TripAdvisor certificate all need higher-quality blocks — neon green on black is the single most compression-hostile combination in the project
- **Android:** ETC2 with alpha
- **Fallback:** PNG-24 high quality for `groene_gids_exterior.png` (the sign is the landmark and its flicker frames must not band) and the menu-text region of `groene_gids_merch_objects.png`

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| groene_gids_environment | groene_gids_exterior, groene_gids_ground_floor | 2048x1280 |
| groene_gids_interior_objects | groene_gids_upstairs_vip, groene_gids_merch_objects | 2048x1024 |
| groene_gids_characters_ui | npc_groene_gids_cast, groene_gids_ui, groene_gids_effects_haze | 2048x1024 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Heavy haze plate plus 4 drifting wisps, dust motes in both light shafts, scrolling menu boards, full neon flicker and bloom, warp vignette, 6 ground-floor NPCs |
| Medium | Medium haze plate plus 2 wisps, dust motes in one shaft, scrolling menus retained, neon flicker retained, warp vignette retained, 4 ground-floor NPCs |
| Low | Low haze plate with no wisps, no dust motes, static menu boards, neon flicker retained (landmark exemption), static corner warp overlay, staff plus 2 NPCs (profile-mandated simplified smoke and static menu) |

### Performance Targets:
- **Target FPS:** 45 (per location profile performance budget)
- **Max Draw Calls:** 16 per frame (per location profile)
- **Memory Footprint:** 40 MB maximum (per location profile)
- **Particle Limit:** 22 (smoke wisps, dust motes, register sparkle, distortion rings combined)

### Performance Notes:
- Ground floor and upstairs are separate scenes with a stair transition; only one is resident at a time, and the upstairs scene reuses the ground-floor object and character atlases wholesale
- Haze is three pre-authored density plates, not a variable particle system — the LOD switch is one texture swap with no runtime recalculation
- Green tinting is a CanvasModulate plus two additive glow layers, so the accessibility reduction toggle costs nothing and ships no extra art
- The Space Cake Timer is owned by a global game-time service, not by this location's scene, so it survives unloading when the player wanders off for munchies
- Bachelor Party Pack counts as 3 against the 6-NPC ground-floor cap

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: TileMap (carpet and wood flooring, wall panels), Sprite2D (facade, counter, display cases, merch wall), AnimatedSprite2D (Bas, Marieke, Bouncer, customers, menu boards, neon), CPUParticles2D (smoke wisps, dust motes, register sparkle — not GPU), CanvasModulate + two additive CanvasLayer glow layers (green tint, reducible by accessibility toggle), CanvasLayer warp shader (space cake onset only), Area2D interaction hotspots sized ≥44px
- Special systems: global space-cake timer service with 30/60/90-minute dialogue gates and a 120-minute onset event that persists across scene changes, Tourist Trapped global vendor-price hook (+15% for 1 hour), Contact High party-wide AoE while inside, cash-only enforcement with ATM redirect and fee accounting, passport-fumble timing mini-game, tobacco-mixing detection with public-correction Bravado penalty, interior photography detection (Chadwick's ring light is auto-detected), three-visit Regular counter unlocking the Secret Menu, merchandise group-discount calculator, VIP surcharge gate

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Neon flicker frames | Transformer tick over a neon buzz bed | On each flicker frame |
| Digital menu frame change | Faint digital scroll tick | On frame display |
| Bas No-Tobacco beats 1-3 | Flat-monotone VO, exhale before beat 1 | Per frame |
| Cash Register Ka-Ching | Register chime, emphasised over €50 | On transaction resolve |
| Space Cake ring 1 | Sound design begins distorting | On frame display |
| Space Cake ring 3 | Music bed pitch-bends 4% down and holds | On frame display |
| Passport Fumble second failure | Bouncer "ID." | On loop restart |
| Marieke frame 1 | Hanger rattle, then bright VO on frame 2 | Per frame |
| Ventilation Grille | Constant hum, audibly straining | Ambient bed |
| Dutch Hip-Hop loop restart | Playlist loops every 47 minutes | Beat pips fire on the loop seam |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The "Is It Working Yet?" Chain | Space cake timer, "It's Not Working" plate, staff response plate, bros trio frames 1-3, distortion rings | 30 / 60 / 90 / 120-minute dialogue and effect beats |
| Tourist Trapped | Status icon, price comparison reveal, purchase confirmation | Applied on first purchase; +15% at all Shamsterdam vendors for 1 hour |
| The No Tobacco Tutorial | Bas explanation frames, NO TOBACCO sign detail, warning toast | Triggered by tobacco-mixing attempt; −Bravado, no mechanical penalty |
| The Photography Prohibition | Photography sign, warning toast, Chadwick filming sprite | Ring light auto-detected; second offence means leaving |
| Regular Status & Secret Menu | Regular progress UI, Secret Menu card, unlock toast | Three visits; same items, different names |
| Merchandise Gauntlet | T-shirt wall, group discount sign and calculator, Marieke pitch frames | Exit corridor; unavoidable by layout |
| The Munchies | Munchies status icon, contact high indicator | Drives traffic to FEBO and Leeman's Döner Palace after the SP boost fades |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Café de Schaamte | Smoke Drift wisps are the source of the terrace's ambient haze; Tourist Trapped icon persists in the HUD | Bros arrive needing coffee and complaining; espresso prices show the +15% modifier |
| FEBO Automat | Munchies status icon drives the traffic; shared status-effect HUD art | Munchies prompt fires on SP drop-off |
| Leeman's Döner Palace | Munchies icon and Contact High indicator; Mehmet's "tourist eyes" dialogue hook | Post-high transition; the Tourist Trapped modifier is visible on his prices |
| The Tolerance Hostel | Branded T-shirt and poster items appear in bunk-room scenes; war stories exchanged | Merch worn or displayed carries into hostel dialogue |
| Casa Rosé Erotic Theatre | Prior impairment level affects the show experience; shared Roodelicht evening audio bed | Impairment state carried between locations |
| Coffeeshop Quarter (street) | Green light pollution wash, exterior neon bloom, souvenir shop frontages | Seamless street walk-off; green wash intensity falls off with distance |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A counterculture institution reorganised into a merchandise funnel, lit entirely in one colour"
- **Color Mood:** Coffeeshop green over everything — walls, carpet, uniforms, and the faces of the people who work here; the only relief is the wood of the bar and the amber of light shafts through smoke
- **Lighting:** Green bulbs in green shades, backlit menu boards brighter than any seating area, jewelry-store spotlights on the merchandise, and a permanent grey haze softening all of it
- **Texture:** Sticky varnish, scuffed carpet, fingerprinted display glass, and a wall of cotton in every size up to XXXL

### Environmental Storytelling:
- The exit corridor routes past the entire merchandise wall — you cannot leave without being sold to, and that is the floor plan, not an accident
- The two souvenir shops flanking the entrance sell the same items cheaper; the game shows all three frontages in one wide shot and says nothing
- The TripAdvisor certificate is framed and displayed, and it says 3.1 stars
- "FAMOUS SINCE 1985" appears twice outside and once inside; the ownership changed in 2017
- The carpet's wear path runs door → counter → merch wall → door, which is the entire intended customer journey rendered in foot traffic
- The Employee of the Month board has shown the same photograph since 2019, and the chalk countdown to the current shift's break is written just below it

### Character Integration Notes:
- Bas has more frames and less expression than any other NPC in Shamsterdam; his Dead-Eyed Stare is the held default and every other frame returns to it
- Marieke is the only staff member drawn with raised eyebrows — commission is visible in her silhouette
- The Bouncer never enters the interior in any frame; he exists at the threshold and nowhere else
- The Space Cake Victim is always present, at every hour, in the same upstairs seat, blinking at a quarter speed
- The Local Who Made A Mistake is drawn moving faster than every other sprite on screen

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The 3.1-Star Certificate** - Framed, lit, displayed with pride
2. **Bas's Dead-Eyed Stare** - Held frame, green polo, fifty thousand explanations deep
3. **The VIP Chair Comparison** - Both chairs side by side in the €10 surcharge prompt
4. **The Space Cake Victim's Slow Blink** - Caught mid-close, upstairs, always
5. **"OH."** - The bros trio at the 120-minute mark
6. **The Merch Gauntlet** - The exit corridor, shot from the door, with the price tags legible
7. **The Broken Neon Letters** - Two letters dark since 2017, on the biggest sign in the district

### Quote Potential:
- "Yes, it's expensive. We are famous. Famous things cost money. This is how famous works."
- "Space cake takes two hours. Yes, I know you feel nothing. Two. Hours."
- "Your friend is asking if he can 'try a sample.' We do not do samples. This is not Costco."
- "Your total is sixty-three euros. Would you like a bag. The bag is two euros."
- "No, a picture of your ID is not ID."
- "It. Is. Working. Wait."
- "Matching shirts. Eleven guys. Bachelor party." *resigned sigh*

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | groene_gids_exterior.png | 1024x512 |
| 2 | groene_gids_ground_floor.png | 1024x768 |
| 3 | groene_gids_upstairs_vip.png | 512x512 |
| 4 | groene_gids_merch_objects.png | 1024x512 |
| 5 | npc_groene_gids_cast.png | 1024x384 |
| 6 | groene_gids_ui.png | 512x512 |
| 7 | groene_gids_effects_haze.png | 512x512 |

**Total Estimated Memory:** ~11.5 MB raw RGBA texture data (~5.1 MB after ASTC/ETC2 compression); ~40 MB maximum total runtime footprint per the location performance budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `groene_gids_exterior.png` (1024x512)
- [ ] `groene_gids_ground_floor.png` (1024x768)
- [ ] `groene_gids_upstairs_vip.png` (512x512)
- [ ] `groene_gids_merch_objects.png` (1024x512)
- [ ] `npc_groene_gids_cast.png` (1024x384)
- [ ] `groene_gids_ui.png` (512x512)
- [ ] `groene_gids_effects_haze.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + neon flicker schedule (the arrhythmia is authored, not random) + green-tint layer guide showing base art without the CanvasModulate and glow layers applied + space cake timer state chart (30/60/90/120)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (#228B22, #39FF14, #708090, #8B4513, #C8BFA6, #D9A441)
- [ ] Base art is authored *without* green tint baked in; the tint is delivered as separate modulate and glow layers so the accessibility reduction toggle works
- [ ] All product representations are abstract (jars, cards, blocks, silhouettes) at every zoom level, on every sheet
- [ ] Key gags read clearly at phone scale: the 3.1-star certificate, the two dark neon letters, "FAMOUS SINCE 1985", the VIP chair comparison, the carpet wear path, the Employee of the Month board
- [ ] Accessibility visual alternatives included for all audio cues (register, lighter, menu scroll, ventilation hum, staff sigh, space cake sting, bouncer ID, hip-hop loop seam)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (brand tourism, tourist-trap pricing and American etiquette failures — never cannabis users or Dutch coffeeshop culture)
- [ ] Hidden areas/interactions have discoverable visual cues (Employee Break Countdown Chalk, "Same Room, Higher Price" wall tag, souvenir shops cheaper on both sides, Secret Menu at 3 visits)
- [ ] Mobile performance optimized (three haze density plates, separate floor scenes, shared atlases, CPU particles only)
- [ ] Touch zone sizing considered (44px minimum on counter, menu board, ATM, merch wall, stairs, purchase buttons)
- [ ] Colorblind-friendly alternatives available where color codes meaning (menu tier hatching, status silhouettes, and an explicit green-tint reduction toggle for a single-hue location)
- [ ] Social media viral potential maximized in composition choices (certificate framing, VIP chair A/B, merch gauntlet from the door, "OH." staging)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | All in-world signage reads "Shamsterdam"; the profile's Amsterdam references are design commentary, never asset text |
| Cultural Specificity | ✅ | Dutch coffeeshop regulations (no tobacco, ID checks, 1 AM close), Coffeeshop Quarter geography, locals-avoid-this economics |
| Satirical Targets Appropriate | ✅ | Punches at brand-worship tourism, tourist-trap pricing and American etiquette failures; Bas, Marieke, the Bouncer and Dutch coffeeshop culture itself are treated as competent and correct |
| Seedy Underbelly Present | ✅ | €20/g against a €10/g going rate, €4.50 branded ATM fee on a forced €50 withdrawal, €45 grinders, €2 bags, merchandise margins beating menu margins, an exit corridor built as a funnel |
| Gameplay Value Established | ✅ | Consumables, two-hour space cake system, Tourist Trapped and Contact High status effects, cash-only ATM loop, passport mini-game, merch upsell, Regular/Secret Menu progression |
| Technical Feasibility | ✅ | Separate floor scenes, three-plate haze LOD, non-baked green tint, global timer service, shared atlases all documented |
| Mobile Performance Budget | ✅ | 45 FPS, 16 draw calls, 40 MB per profile budget |
| Accessibility Features | ✅ | Eight visual audio cues, reduced-motion haze/neon/warp/menu alternatives, menu-tier hatching, and an explicit green-tint reduction toggle for a single-hue location |
| No Crypto Elements | ✅ | Cash only, a branded ATM, and a card machine that exists to point at it |
| Social Media Integration | ✅ | Seven screenshot moments plus a seven-line quote bank identified |

**Once these assets are delivered, De Groene Gids becomes Eurobound's most efficient trap: a landmark you can see from three canals away, a two-hour joke that detonates in a completely different location, and a green-lit corridor you cannot exit without buying a T-shirt that says exactly what you did.**
