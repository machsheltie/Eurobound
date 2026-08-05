# Leeman's Döner Palace - Complete PNG Asset Requirements

## 📋 Overview
Leeman's Döner Palace is thirty-two years of Turkish mastery served standing up at 3 AM to people who cannot pronounce what they are eating. This document specifies every PNG asset for the shop: the beacon-bright exterior, the standing-room-only temple interior, the three rotating towers of the Holy Trinity, Mehmet and his daughter Elif, the late-night customer ecology, the Garlic Aura and Meat Sweats effect sets, and the ordering UI where the pronunciation mini-game decides how much respect you get. Its satirical essence in a sentence: the food is genuinely perfect, and you are genuinely not ready for it.

**Location ID:** `shamsterdam_latenight_leemans_doner_01`
**Theme:** Turkish-Dutch immigrant döner mastery vs. tourist ordering incompetence — the craft is celebrated, the customer is judged
**Zone:** Late-night district, next to the tram stop, across from a club exit
**Hours:** 11 AM - 5 AM (peak: 1 AM - 4 AM, when the real customers arrive)
**Primary Function:** Late-night food vendor / status-effect dispensary — ordering system with Mehmet Evaluation, Pronunciation Challenge mini-game, Triple Tower warrior item, Garlic Aura + Meat Sweats statuses, Great Döner Debate quest entry #1

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Döner Red | #C41E3A | Main signage, awning, brand surfaces |
| Turkish Gold | #FFD700 | Sign lettering, trim, approval highlights |
| Night Black | #1A1A1A | Exterior night backdrop, interior shadow |
| Meat Brown | #8B4513 | Tower meat, bread crust, counter warmth |
| Fluorescent White | #F8F8F0 | Interior lighting wash, the beacon effect |
| Sauce Cream | #EDE3C8 | Garlic/yogurt sauce, napkin stacks |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/leemans_doner_palace/
├── environment/
│   ├── leemans_interior_main.png
│   └── leemans_exterior_fixtures.png
├── objects/
│   └── leemans_food_items.png
├── npcs/
│   ├── npc_mehmet_elif.png
│   └── npc_leemans_customers.png
├── effects/
│   └── leemans_effects.png
└── ui/
    └── leemans_ui.png
```

---

## 🏪 Sprite Sheet 1: Interior Main Background
**File:** `leemans_interior_main.png`
**Dimensions:** 1920x1080 pixels (standalone full-scene background — not atlased)
**Color Palette:** #1A1A1A, #8B4513, #F8F8F0

### Scene Layout:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Interior Backdrop | (0, 0) | 1920x1080 | Full scene: three meat towers glowing centre-rear behind glass, carving station left-centre, narrow stainless standing counter running along the window right, industrial napkin dispenser, bread oven rear-left, register right, zero seating anywhere — the absence is the design |

### Technical Notes:
- Anchor points (document in layer names): tower bank at (896, 288), carving station at (512, 448), standing counter at (1408, 704), register at (1664, 512), bread oven at (256, 352), queue origin at (1024, 896)
- Tower zone painted dim/neutral in the backdrop; the rotation blur and heat haze overlays (Sheet 6) composite on top
- Window wall painted with alpha-safe cutout so the exterior beacon glow (Sheet 6) can bleed inward at night hours
- Floor painted with pre-baked grease sheen only in low-traffic corners; the tileable sheen overlay handles the counter run

---

## 🥙 Sprite Sheet 2: Exterior & Fixtures
**File:** `leemans_exterior_fixtures.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #C41E3A, #FFD700, #1A1A1A, #8B4513

### Exterior Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Leeman's Storefront | (0, 0) | 384x384 | Small takeaway front, bright interior punching through night, meat smell implied by everyone facing it |
| Three Meat Towers (Bank) | (384, 0) | 256x384 | The Holy Trinity behind glass — veal, chicken, mixed, hypnotic at 3 AM |
| Carving Station | (640, 0) | 192x256 | Mehmet's workspace: long knife, catch tray, thirty-two years of muscle memory |
| Menu Board (Four Languages) | (832, 0) | 192x256 | Dutch, Turkish, English, German — none spelled consistently correctly |
| Bread Display | (640, 256) | 192x128 | Fresh-baked daily, warm, the actual secret |
| Sauce Station | (832, 256) | 192x128 | Garlic / yogurt / hot / sambal, four pumps, one regret |

### Interior Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Standing Counter (Customer Side) | (0, 384) | 512x192 | Stainless, narrow, along the window — room for 6-8 shoulder-to-shoulder |
| Industrial Napkin Dispenser | (512, 384) | 128x192 | You will need many. It knows. |
| Window Shelf Run | (640, 384) | 192x192 | Where warriors eat, facing the street, watching the night |
| Register / Elif's Post | (832, 384) | 192x192 | Cash drawer, card reader, receipt printer nobody wants |

### Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Sign "LEEMAN'S DÖNER PALACE" | (0, 576) | 256x128 | Red and gold, separate layer for night glow overlay |
| "Since 1992 — Original Turkish Recipe" | (256, 576) | 256x64 | Subtitle plate, faded but proud |
| "NO KAPSALON. Go to Wim for that." | (256, 640) | 256x64 | Handwritten addition, taped, unmistakably sincere |
| "FRESH BREAD BAKED DAILY" Window Decal | (512, 576) | 192x128 | True. Crucial. Load-bearing. |
| Turkish Radio Shelf | (704, 576) | 160x128 | Small radio, always on, always traditional |
| Bread Oven Door | (864, 576) | 160x128 | Rear-wall oven, wife's recipe, unchanged since 1992 |

### Individual Towers & Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tower 1 — Veal (Dana) | (0, 704) | 192x160 | The traditional, the respected, marinated 24 hours |
| Tower 2 — Chicken (Tavuk) | (192, 704) | 192x160 | The lighter option; Mehmet judges this selection silently |
| Tower 3 — Mixed (Karışık) | (384, 704) | 192x160 | The crowd-pleaser for the indecisive |
| Knife Rack | (576, 704) | 128x96 | Blades in descending order of seriousness |
| Ayran Fridge | (704, 704) | 128x96 | Traditional pairing, glass door, humming |
| Queue Rail / Doorway Frame | (832, 704) | 192x160 | Where the line forms at 2 AM |
| Coin Tray | (576, 800) | 128x64 | Payment at the end, as is tradition |
| Receipt Printer | (704, 800) | 128x64 | "You want receipt? Nobody wants receipt." |

### Environmental Context Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tileable Grease Floor Tile | (0, 864) | 256x128 | Seamless, faintly reflective, thirty-two years deep |
| Mehmet Plaque — "Chicken is for children." | (256, 864) | 256x64 | Not officially a sign; someone laminated it anyway |
| Mehmet Plaque — "The secret is the bread." | (256, 928) | 256x64 | Second plaque, same laminator |
| Tram Stop Marker | (512, 864) | 192x128 | Perfect positioning made visible |
| Club Exit Doorway | (704, 864) | 192x128 | The customer supply line, across the street |
| Street Beacon Base | (896, 864) | 128x128 | Pavement light-pool plate under the beacon glow overlay |

### Technical Notes:
- Towers 1-3 drawn with vertical symmetry so a 2-frame swap reads as continuous slow rotation (see Animation Specs)
- Main sign and beacon base are separate from the storefront block so night glow (Sheet 6) can be additively blended without lighting the whole facade
- Grease floor tile must seam cleanly on all four edges; it is the only tiled asset in the location
- Menu board text baked in at 2x internal resolution for readability at gameplay zoom; keep on the uncompressed-texture exception list

---

## 🍖 Sprite Sheet 3: Food & Sauces
**File:** `leemans_food_items.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #8B4513, #EDE3C8, #FFD700, #C41E3A

### The Menu:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Döner (Veal) | (0, 0) | 64x48 | 6 Sovs — "Good choice." |
| Döner (Chicken) | (64, 0) | 64x48 | 5 Sovs — "...okay." |
| Döner (Mixed) | (128, 0) | 64x48 | 5 Sovs — "Indecisive. But okay." |
| The Triple Tower | (192, 0) | 96x64 | 8 Sovs — all three meats, warrior portion, structurally optimistic |
| Döner Wrap (Dürüm) | (288, 0) | 64x48 | "Wrap is for tourists. But okay." |
| Bread Pocket (Ekmek) | (352, 0) | 64x48 | "Real döner is in bread." |
| Fresh Bread Loaf | (416, 0) | 48x32 | The secret, warm, crisp outside |
| Ayran | (464, 0) | 32x48 | 2 Sovs, traditional, cooling |

### Sauces & Extras:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Garlic Sauce Pump | (0, 48) | 32x32 | House-made, legendary, socially consequential |
| Yogurt Sauce Pump | (32, 48) | 32x32 | Cooling, traditional, rounded container |
| Hot Sauce Bottle | (64, 48) | 32x32 | Turkish hot. Not tourist hot. Angular container. |
| Sambal Jar | (96, 48) | 32x32 | Dutch-Indonesian addition, tolerated |
| Just Bread (Plain) | (128, 48) | 48x32 | 2 Sovs — "You came here for... bread?" |
| Napkin Wad | (176, 48) | 32x32 | Post-sauce reality |
| Sov Coin Stack | (208, 48) | 32x32 | Payment at the end |
| Meat Shave Curl | (240, 48) | 48x32 | Single ribbon off the tower |
| Triple Tower Cross-Section | (288, 48) | 96x96 | Cutaway showing all three meats layered, labeled |
| Döner Half-Eaten | (384, 48) | 64x48 | Mid-journey state |
| Döner Nearly Done | (448, 48) | 64x48 | Final third, commitment visible |

### Icons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Veal Inventory Icon | (0, 96) | 32x32 | Item icon |
| Chicken Inventory Icon | (32, 96) | 32x32 | Item icon |
| Mixed Inventory Icon | (64, 96) | 32x32 | Item icon |
| Triple Tower Inventory Icon | (96, 96) | 32x32 | Item icon |
| Ayran Inventory Icon | (128, 96) | 32x32 | Item icon |
| Garlic Aura Icon | (160, 96) | 32x32 | Status icon — radiating bulb silhouette |
| Meat Sweats Icon | (192, 96) | 32x32 | Status icon — droplet over tower silhouette |
| Fire Breath Icon | (224, 96) | 32x32 | Status icon — hatched flame silhouette |
| Extra Garlic Upgrade Chip | (256, 96) | 32x32 | +1 Sov modifier chip |
| Foil Wrapper (Open) | (384, 96) | 64x48 | Mid-eat presentation |
| Foil Wrapper (Closed) | (448, 96) | 64x48 | Takeaway presentation |

### Plated States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Triple Tower Plated | (0, 144) | 96x64 | The warrior choice, in full |
| Standard Döner Plated | (96, 144) | 96x64 | Regular service presentation |
| Bread-Only Sad Plate | (192, 144) | 96x64 | Visible disappointment, structural and emotional |
| Sauce Station Tray | (288, 144) | 96x64 | Four containers arranged, shape-coded |
| Turkish Hot Warning Chili | (384, 144) | 64x64 | Large warning glyph for the hot sauce prompt |
| Garlic Bulb (Large) | (448, 144) | 64x64 | Large warning glyph for the extra-garlic prompt |

### Sequence Strips:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Tray Strip | (0, 208) | 128x48 | Two 64x48 frames: served / collected |
| Eating Progress Strip | (128, 208) | 128x48 | Two 64x48 frames: 33% / 66% |
| Wrap Unwrap Strip | (256, 208) | 128x48 | Two 64x48 frames: foil closed / foil peeled |
| Mehmet's Knife | (384, 208) | 128x48 | Long carving blade prop, held-item layer |

### Technical Notes:
- Sauce containers are shape-coded (round pump / round pump ridged / angular bottle / squat jar) so garlic vs. yogurt vs. hot vs. sambal never rely on color alone
- Half-eaten and nearly-done states swap at 33% and 66% eating progress
- Triple Tower silhouette must read as ~1.6x a standard döner at gameplay zoom without any UI label

---

## 👨‍🍳 Sprite Sheet 4: Mehmet & Elif
**File:** `npc_mehmet_elif.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 per character frame; 128x128 per portrait
**Color Palette:** #C41E3A apron accents, #8B4513, #F8F8F0

### Mehmet "The Meat Architect" Leeman — Service:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mehmet Idle | (0, 0) | 64x96 | 50s, döner chef attire, arms that have carved millions |
| Mehmet Carving Frame 1 | (64, 0) | 64x96 | Blade to tower, first pass |
| Mehmet Carving Frame 2 | (128, 0) | 64x96 | Meat falling to catch tray |
| Mehmet Carving Frame 3 | (192, 0) | 64x96 | Second pass, rhythm established |
| Mehmet Carving Frame 4 | (256, 0) | 64x96 | Blade wipe, tray gathered |
| Mehmet Judging Frame 1 | (320, 0) | 64x96 | The pre-order evaluation begins |
| Mehmet Judging Frame 2 | (384, 0) | 64x96 | Eyebrow. That is the whole animation. |
| Mehmet Approving | (448, 0) | 64x96 | Rare. Meaningful. "This I respect." |

### Mehmet — Reactions:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mehmet Wrapping | (0, 96) | 64x96 | Foil fold, single motion, thirty-two years |
| Mehmet Presenting Bread | (64, 96) | 64x96 | "The secret is the bread. Always the bread." |
| Mehmet Sauce Warning | (128, 96) | 64x96 | "You want to be alone tonight?" |
| Mehmet Chicken Disappointment | (192, 96) | 64x96 | Not anger. Something quieter. Worse. |
| Mehmet Pronunciation — Perfect | (256, 96) | 64x96 | Single nod, slight respect, no comment |
| Mehmet Pronunciation — Catastrophic | (320, 96) | 64x96 | "You want... what? Show me on menu." |
| Mehmet Pointing at Menu | (384, 96) | 64x96 | The menu is right there. It has pictures. |
| Mehmet Debaucheryville Rant | (448, 96) | 64x96 | "Debaucheryville knows NOTHING." |

### Portraits & Extras:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mehmet Portrait (Dialogue) | (0, 192) | 128x128 | Weathered hands out of frame, knowing eyes, mustache that has seen everything |
| Mehmet Portrait (Rare Approval) | (128, 192) | 128x128 | The Mehmet Paradox visible: he is pleased |
| Elif Portrait (Dialogue) | (256, 192) | 128x128 | Efficient, biased, correct |
| Mehmet Warrior Nod | (384, 192) | 64x96 | Post-Triple-Tower acknowledgment |
| Mehmet Handing Döner | (448, 192) | 64x96 | Transaction complete, life continues |
| Reserve / Atlas Padding | (384, 288) | 128x32 | Reserved strip, do not paint |

### Elif (Mehmet's Daughter, Night Shift):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Elif Idle | (0, 320) | 64x96 | 20s Turkish-Dutch, inherited her father's economy of words |
| Elif At Register | (64, 320) | 64x96 | Card reader extended, no wasted motion |
| Elif Order Repeat | (128, 320) | 64x96 | "Order? ...and sauce? ...and to drink?" |
| Elif Receipt Question | (192, 320) | 64x96 | "Nobody wants receipt. But okay." |
| Elif Pattern Recognition | (256, 320) | 64x96 | "Fifth group of Americans tonight. I see pattern." |
| Elif Fast-Move Blur | (320, 320) | 64x96 | Peak-hour transit frame |
| Elif Biased-But-Correct | (384, 320) | 64x96 | Arms folded, entirely unbothered |
| Elif Handing Ayran | (448, 320) | 64x96 | "Good with döner. Traditional." |

### Utility Frames:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mehmet Wiping Knife | (0, 416) | 64x96 | Between-order ambient loop frame |
| Mehmet Tower Check | (64, 416) | 64x96 | Ambient: patience, slow rotation, correctness |
| Mehmet Silent Judgment Hold | (128, 416) | 64x96 | Held frame for dialogue pauses |
| Elif Closing Register | (192, 416) | 64x96 | End-of-transaction beat |
| Mehmet High-Contrast Silhouette | (256, 416) | 64x96 | Accessibility outline variant |
| Accessibility Reserve Block | (320, 416) | 192x96 | Reserved for high-contrast/audio-cue glyph overflow |

### Technical Notes:
- Carving frames 1-4 loop independently of the order state so the tower is always being worked between customers
- Judging frames trigger before the player's order input — Mehmet evaluates you first, that is the joke
- Portraits sit in their own 128px band so the character rows can be sliced as a uniform 64x96 grid

---

## 👥 Sprite Sheet 5: The 3 AM Congregation
**File:** `npc_leemans_customers.png`
**Dimensions:** 1024x256 pixels
**Sprite Size:** 64x96 per single NPC frame; 128x128 per portrait
**Color Palette:** Mixed night-crowd palette, fluorescent-white ambient grade

### Standing-Room Customers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Post-Club Crowd | (0, 0) | 256x96 | Group in club clothes, various states of coherence, pure gratitude |
| Local Regular | (256, 0) | 64x96 | Dutch, here three times a week, orders by existing |
| Local Regular Nod | (320, 0) | 64x96 | The entire transaction, performed |
| Cab Driver Break | (384, 0) | 64x96 | Professional standing-eating form, back to work in 90 seconds |
| First-Timer Tourist | (448, 0) | 64x96 | Reading the menu intently, overthinking visibly |
| First-Timer Committed | (512, 0) | 64x96 | Decision made, terror managed |
| Döner Veteran | (576, 0) | 64x96 | "Triple Tower. Extra hot. You know how I like it." |
| Standing Eater (Universal Pose) | (640, 0) | 64x96 | Counter-slot pose, palette-modulated per NPC |
| Queue Filler A (Back View) | (704, 0) | 64x96 | Peak-hour line body |
| Queue Filler B (Back View) | (768, 0) | 64x96 | Line body variant |
| Bros Trio Block | (832, 0) | 192x96 | Lord Pilsner / Chadwick / Bradley at the counter, pre-composed |

### Reactions & Portraits:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Eating Poses Strip | (0, 96) | 256x96 | Four 64x96 stages: first bite / pacing / sauce crisis / transcendence |
| Sauce Disaster Pose | (256, 96) | 64x96 | Garlic sauce has reached the sleeve |
| Garlic Aura Recoil Pose | (320, 96) | 64x96 | NPC maintaining the mandatory 20% larger conversation distance |
| Meat Sweats Shimmer Pose | (384, 96) | 64x96 | Slightly slower, slightly glowing, entirely content |
| Döner Veteran Portrait | (448, 96) | 128x128 | Knows the drill, has always known the drill |
| Local Regular Portrait | (576, 96) | 128x128 | Says nothing. Has said nothing for years. |
| Post-Club Enthusiast Portrait | (704, 96) | 128x128 | "This is the BEST thing I've ever eaten." |
| First-Timer Portrait | (832, 96) | 128x128 | "Is the veal... is it spicy? What's in the sauce?" |
| Shoulder-to-Shoulder Filler | (960, 96) | 64x96 | Single body for peak-density counter packing |

### Ambient Strips:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Silhouette Row | (0, 192) | 256x64 | Backs of heads at the window, cheap crowd depth |
| Napkin Grab Strip | (256, 192) | 192x64 | Three 64x64 frames: reach / pull / surrender |
| Accessibility Reserve | (960, 192) | 64x64 | Reserved for high-contrast marker |
| Outline Strip Reserve | (448, 224) | 512x32 | Reserved padding under portrait band |

### Technical Notes:
- Post-Club Crowd and Bros Trio ship as single pre-composed blocks to protect the 14-draw-call budget
- Eating Poses Strip is palette-modulated onto any 64x96 customer for counter slots — never author per-NPC eating art
- Maximum 4 individually animated customer sprites on screen; all others use static poses from this sheet

---

## ✨ Sprite Sheet 6: Effects — Sizzle, Aura & Beacon
**File:** `leemans_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #FFD700, #C41E3A, #F8F8F0, #8B4513

### Meat & Heat:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Meat Sizzle Steam Frame 1 | (0, 0) | 64x64 | Tower steam, first rise |
| Meat Sizzle Steam Frame 2 | (64, 0) | 64x64 | Tower steam, dispersal |
| Grease Sizzle Pop | (128, 0) | 64x64 | Fat hitting the drip tray |
| Bread Warmth Glow | (192, 0) | 64x64 | Soft halo over the bread display |
| Garlic Aura Ring Frame 1 | (256, 0) | 64x64 | Faint expanding ring, character-parented |
| Garlic Aura Ring Frame 2 | (320, 0) | 64x64 | Ring at full radius before fade |
| Meat Sweats Shimmer | (384, 0) | 64x64 | Heat-shimmer overlay for the affected sprite |
| Fire Breath Wisp | (448, 0) | 64x64 | Turkish-hot delayed consequence |

### Station & Light:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Knife Carve Spark | (0, 64) | 64x64 | Blade-on-tower contact glint |
| Meat Curl Fall | (64, 64) | 64x64 | Single ribbon dropping to the tray |
| Beacon Light Cone | (128, 64) | 128x128 | The shop as lighthouse — pavement light-pool, night hours |
| Fluorescent Flicker Strip | (256, 64) | 128x32 | Two 64x32 interior lighting states |
| Neon Sign Glow | (256, 96) | 128x96 | Additive glow plate for the main sign |
| Tower Heat Haze | (384, 64) | 64x64 | Distortion-free painted haze band |
| Sauce Squirt Arc | (448, 64) | 64x64 | Pump-to-döner arc |
| Garlic Warning Glow | (0, 128) | 64x64 | Ominous pulse when extra garlic is requested |
| Napkin Flutter | (64, 128) | 64x64 | Dispenser overdraw, two-frame |
| Tower Rotation Blur | (384, 128) | 128x64 | Two 64x64 blur plates alternated with tower frames |

### Ambient & Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Steam Rise (Tall) | (0, 192) | 64x64 | Vertical column for the bread oven |
| Grease Sheen Tile | (64, 192) | 64x64 | Tileable counter sheen overlay |
| Garlic Cloud Puff | (128, 192) | 64x64 | One-shot on extra-garlic application |
| Turkish Hot Flame Lick | (192, 192) | 64x64 | One-shot on hot sauce application |
| Respect Glint (Mehmet Nod) | (256, 192) | 32x32 | Small gold sparkle on rare approval |
| Pronunciation Success Glyph | (288, 192) | 32x32 | Rising-note glyph, mirrors the approval chime |
| Pronunciation Fail Glyph | (320, 192) | 32x32 | Flat-note glyph, mirrors the correction sting |
| Steam Wave Glyph | (352, 192) | 32x32 | Visual mirror of the ambient sizzle bed |
| Sizzle Glyph | (384, 192) | 32x32 | Visual mirror of the tower sizzle |
| Register Ding Glyph | (416, 192) | 32x32 | Visual mirror of the cash register |
| Knife Rhythm Glyph | (448, 192) | 32x32 | Visual mirror of the carving rhythm |
| Ayran Pour Glyph | (480, 192) | 32x32 | Visual mirror of the pour cue |

### Technical Notes:
- Garlic Aura ring parents to the affected character sprite; it never renders as a screen-space effect
- Beacon Light Cone and Neon Sign Glow are additive-blend only during 8 PM - 5 AM clock states
- All 32x32 glyphs in the bottom-right band are the deaf/HoH visual mirrors; they render in the HUD gutter, never over the action

---

## 🧭 Sprite Sheet 7: UI Elements
**File:** `leemans_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #C41E3A UI chrome, #FFD700 highlights, #1A1A1A panel fill

### Ordering Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Meat Selection Panel | (0, 0) | 256x128 | Veal / Chicken / Mixed / Triple Tower with Mehmet-opinion flavor slots |
| Bread Selection Panel | (256, 0) | 256x128 | Dürüm vs. Ekmek — "Wrap is for tourists. But okay." |
| Sauce Selection Panel | (0, 128) | 256x128 | Garlic / Yogurt / Hot / Sambal / None, shape-coded chips |
| Pronunciation Challenge Panel | (256, 128) | 192x128 | "döner" input prompt with four outcome states |
| Pronunciation Meter | (448, 128) | 64x128 | Vertical scale: Perfect / Acceptable / Tourist / Catastrophic |

### Transaction & Quest:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu Board UI Overlay | (0, 256) | 192x128 | Zoomed readable four-language board with inconsistent spellings preserved |
| Bill / Payment Panel | (192, 256) | 128x96 | Payment at the end, as is tradition |
| Great Döner Debate Tracker | (320, 256) | 128x64 | Shamsterdam entry #1 quest chip |
| Cost Chip (SOVS) | (448, 256) | 64x64 | Price token for menu rows: numeral above the lettered word `SOVS`. **The symbol is the word — do not draw a currency mark.** 64x64 is ample. |
| Garlic Aura Status Bar | (320, 320) | 96x32 | 1-3 hour duration display |
| Meat Sweats Status Bar | (416, 320) | 96x32 | 30-minute regen/speed display |
| Fire Breath Status Bar | (192, 352) | 128x32 | Delayed-damage warning bar |
| Debate Verdict Slider | (320, 352) | 192x32 | Shamsterdam vs. Debaucheryville opinion commit |

### Achievements & Status Icons:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Achievement Badges Strip | (0, 384) | 320x64 | Five 64x64 badges: Initiated / Warrior / Respectful / Regular / Brave or Foolish |
| Warrior Spirit Badge (Large) | (320, 384) | 64x64 | Triple Tower completion, presentation size |
| Regular Status Chip | (384, 384) | 128x64 | Unlocks at 5 visits: Mehmet nods first |
| Garlic Aura Icon | (0, 448) | 32x32 | Radiating bulb silhouette |
| Meat Sweats Icon | (32, 448) | 32x32 | Droplet-over-tower silhouette |
| Fire Breath Icon | (64, 448) | 32x32 | Hatched flame silhouette |
| Disappointment Icon | (96, 448) | 32x32 | Bread-alone silhouette |
| Cooling (Ayran) Icon | (128, 448) | 32x32 | Cup-with-arc silhouette |
| High-Contrast Counter Marker | (160, 448) | 64x64 | Bold outline for the order interaction point |
| Meat Silhouette Set | (224, 448) | 128x64 | Veal/chicken/mixed/triple as stepped silhouettes with labels |
| Touch-Zone Guide Overlay | (352, 448) | 160x64 | Dev-only 44px minimum overlay, stripped at build |

### Technical Notes:
- Every selectable row on meat/bread/sauce panels renders at 44px+ touch height
- Badges ship full-color and are grayscale-modulated until earned; no separate locked art
- Pronunciation Meter uses four discrete stepped segments plus text labels, never a continuous color gradient

---

## 🎬 Animation Specifications

### Tower Rotation (Sheets 2 & 6):
- **Duration:** 3.0 seconds per visual cycle
- **Frames:** 2 tower symmetry frames + 2 blur plates
- **Pattern:** Frame A → blur → Frame B → blur → loop, continuous
- **Trigger:** Constant during open hours, all three towers offset by 1.0s so they never align
- **Purpose:** The hypnotic 3 AM meat trinity; "fast rotation? Burned outside, raw inside. Patience."
- **Audio Sync:** Continuous sizzle bed, amplitude gently tied to loop phase
- **Performance Optimization:** Low LOD drops blur plates and uses a single static frame per tower (profile requirement: simplified tower rotation)

### Mehmet Carving Sequence (Sheets 3, 4, 6):
- **Duration:** 4.8 seconds total (4 frames at 1.2s)
- **Frames:** 4 character frames + meat curl + carve spark
- **Pattern:** Blade to tower → meat falls → second pass → blade wipe → serve
- **Trigger:** Any döner order; ambient idle version plays between customers
- **Purpose:** Watching the master work is half the price of admission
- **Audio Sync:** Knife-on-tower shave at 0.0s and 2.4s; meat-to-tray at 1.2s; foil crinkle at 4.8s
- **Performance Optimization:** Medium LOD reduces to 2 keyframes; Low LOD uses a single composed frame + serve

### Pronunciation Challenge (Sheets 4, 6, 7):
- **Duration:** 2.2 seconds (1.0s input window, 0.4s judgment beat, 0.8s reaction hold)
- **Frames:** Meter fill + one of four Mehmet reaction frames
- **Pattern:** Play once on first-ever order
- **Trigger:** First order at this location, per save file
- **Purpose:** The gap between thirty-two years of craft and thirty-two seconds of effort
- **Audio Sync:** Player attempt at 0.0s; 0.4s of pure silence (comedy-critical); reaction line at 1.4s
- **Performance Optimization:** None needed (one-shot, cheap, never degraded)

### Garlic Aura Application (Sheets 5 & 6):
- **Duration:** 1.2s one-shot puff, then a 2.0s ring pulse loop for the status duration
- **Frames:** Garlic cloud puff + 2 ring frames
- **Pattern:** Puff → ring pulse loop → fade on expiry
- **Trigger:** Any döner (base 1 hour), extended to 3 hours with extra garlic
- **Purpose:** NPCs step back 20% — the effect is social, so it must be visible
- **Audio Sync:** Soft "whumph" on the puff; no loop audio (the silence is the joke)
- **Performance Optimization:** Low LOD holds ring frame 1 statically

### Meat Sweats Onset (Sheets 5 & 6):
- **Duration:** 2.0-second onset, then held shimmer for 30 minutes game-time
- **Frames:** Shimmer overlay, 2-frame slow alternation
- **Pattern:** Onset fade-in → 1.6s shimmer cycle → fade on expiry
- **Trigger:** Triple Tower consumption, or excessive consumption in one visit
- **Purpose:** +10% HP regen, -10% Speed, 100% earned
- **Audio Sync:** Low sustained hum on onset only
- **Performance Optimization:** Shimmer cycle at half rate on Low LOD; disabled entirely in reduced-motion mode

### Beacon & Interior Flicker (Sheet 6):
- **Duration:** Fluorescent flicker 0.4s burst roughly every 45s; beacon cone 4.0s breathe
- **Frames:** 2 / 1 (alpha)
- **Pattern:** Random flicker / continuous breathe, night hours only
- **Trigger:** Clock-based, 8 PM - 5 AM
- **Purpose:** The bright box in the dark that pulls the whole street toward it
- **Audio Sync:** Faint ballast buzz on flicker
- **Performance Optimization:** Both static on Low LOD; disabled in reduced-motion mode

### Triple Tower Completion (Sheets 3, 4, 7):
- **Duration:** 2.4 seconds (1.0s final bite, 0.4s pause, 1.0s Mehmet nod + badge)
- **Frames:** Nearly-done → empty foil + Mehmet Warrior Nod + respect glint
- **Pattern:** One-shot ceremony
- **Trigger:** Triple Tower eaten to completion in a single visit
- **Purpose:** "You have warrior spirit. Come back." — the highest available honor
- **Audio Sync:** Foil crumple at 0.0s; silence 1.0-1.4s; low approving grunt at 1.4s; badge chime at 2.0s
- **Performance Optimization:** Glint replaced by instant badge award in reduced-motion mode

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| High-Contrast Counter Marker | Sheet 7 (160, 448) | 64x64 | Bold outline marker for the ordering interaction point |
| Meat Silhouette Set | Sheet 7 (224, 448) | 128x64 | Veal/chicken/mixed/triple as bold stepped silhouettes with text labels |
| Mehmet High-Contrast Silhouette | Sheet 4 (256, 416) | 64x96 | Enhanced-visibility outline of the key interaction NPC |
| Accessibility Reserve Block | Sheet 4 (320, 416) | 192x96 | Overflow space for additional high-contrast variants |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Tower Frame | Sheet 2 (0/192/384, 704) | 192x160 | Reduced-motion locks all three towers to frame A, no blur plates |
| No-Flicker Fluorescent | Sheet 6 (256, 64) frame 1 | 64x32 | Steady interior lighting substitute |
| Static Beacon Cone | Sheet 6 (128, 64) | 128x128 | Beacon renders at fixed 70% alpha, no breathe |
| Static Meat Sweats Overlay | Sheet 6 (384, 0) | 64x64 | Shimmer holds on frame 1, no alternation |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sizzle Glyph | Sheet 6 (384, 192) | 32x32 | Mirrors the constant tower sizzle bed |
| Knife Rhythm Glyph | Sheet 6 (448, 192) | 32x32 | Pulses on each carving contact |
| Register Ding Glyph | Sheet 6 (416, 192) | 32x32 | Fires on payment confirmation |
| Pronunciation Success Glyph | Sheet 6 (288, 192) | 32x32 | Rising-note glyph on the approval cue |
| Pronunciation Fail Glyph | Sheet 6 (320, 192) | 32x32 | Flat-note glyph on the correction sting |
| Ayran Pour Glyph | Sheet 6 (480, 192) | 32x32 | Fires on the pour cue |
| Steam Wave Glyph | Sheet 6 (352, 192) | 32x32 | Persistent ambient-audio indicator |

### Colorblind Considerations:
- Sauces coded by container shape (round pump / ridged pump / angular bottle / squat jar) and by drip pattern, never by red-vs-cream color alone
- Meat selection coded by silhouette thickness and text label, never by meat-tone color alone
- Status effects use distinct silhouettes: radiating bulb (Garlic Aura), droplet-over-tower (Meat Sweats), hatched flame (Fire Breath), cup-with-arc (Cooling)
- Pronunciation Meter uses four discrete stepped segments plus written outcome labels
- Touch zones minimum 44px for all meat/bread/sauce options, the counter interaction, and the pronunciation input

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) menu board, cross-section diagram, and all portraits kept uncompressed (readable text and faces)
- **Fallback:** PNG high quality for `leemans_interior_main.png` (scene-detail critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| leemans_environment | leemans_exterior_fixtures | 1024x1024 |
| leemans_characters | npc_mehmet_elif, npc_leemans_customers | 1024x1024 |
| leemans_fx_ui | leemans_food_items, leemans_effects, leemans_ui | 1024x1024 |

*(leemans_interior_main.png loads standalone as a scene background; max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Three offset tower rotations with blur, full carving sequence, beacon breathe, aura + shimmer loops, flicker |
| Medium | Towers rotate without blur plates, carving at 2 keyframes, beacon static, aura loop retained |
| Low | Static towers (profile requirement), static steam (profile requirement), single-frame carving, no flicker, one-shot pronunciation event retained |

### Performance Targets:
- **Target FPS:** 60 (per location performance budget)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 32 MB maximum
- **Particle Limit:** 14 (tower steam, grease pops, garlic puff)

### Performance Notes:
- Post-Club Crowd and Bros Trio are pre-composed single blocks; maximum 4 individually animated NPCs on screen
- Three towers share one AnimatedSprite2D texture with per-instance frame offset — one material, three instances
- Beacon and neon glow are alpha overlays, no Light2D nodes anywhere in the scene
- Pronunciation Challenge is a one-shot UI event with no persistent cost after first visit

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (interior background, fixtures), AnimatedSprite2D (Mehmet, Elif, towers, effects), CPUParticles2D (steam, grease pops — not GPU), CanvasLayer (order UI, pronunciation panel), Area2D (counter, register, sauce station interaction zones)
- Special systems: Mehmet Evaluation dialogue branch keyed to order composition, Pronunciation Challenge first-visit flag, Garlic Aura duration timer with NPC proximity modifier, Meat Sweats stat modifier, visit-count tracker driving Regular status, Great Döner Debate opinion persistence

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Tower rotation loop | Constant meat sizzle bed | Continuous, phase-locked |
| Carving frame 1 / frame 3 | Knife-on-tower shave | 0.0s / 2.4s of carve sequence |
| Carving frame 2 | Meat falling to tray | 1.2s |
| Mehmet wrapping | Foil crinkle | 4.8s of carve sequence |
| Pronunciation judgment beat | Silence (deliberate) | 1.0-1.4s of challenge |
| Garlic cloud puff | Soft "whumph" | On extra-garlic application |
| Payment panel confirm | Cash register ding | On transaction commit |
| Triple Tower completion | Low approving grunt + badge chime | 1.4s / 2.0s of ceremony |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Great Döner Debate: International Expansion | Döner sprites, Debate Tracker chip, Verdict Slider, Mehmet Debaucheryville Rant | Eating any döner here = Shamsterdam entry #1; verdict is remembered and Mehmet remembers faces |
| Döner Achievement Track | Badges strip, pronunciation panel, Triple Tower sprite, Regular chip | Initiated / Warrior / Respectful / Regular / Brave or Foolish |
| The Triple Tower Challenge | Triple Tower plated, Mehmet Warrior Nod, respect glint, Meat Sweats overlay | Finish in one visit → Warrior Spirit badge + guaranteed Meat Sweats |
| Pronunciation Respect | Pronunciation panel + meter, Mehmet reaction frames | Perfect delivery unlocks the rare-approval portrait and a permanent dialogue tone shift |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Kapsalon Koning | "NO KAPSALON. Go to Wim for that." handwritten sign; friendly-rivalry dialogue hooks | Sign is the visual handoff; Wim's counterpart line reads "Mehmet down the street? Good man. No cheese. His loss." |
| De Groene Gids | Munchies pipeline endpoint marker | Post-coffeeshop arrival raises Triple Tower order probability in the ordering UI default |
| The Tolerance Hostel | Kitchen gossip references "the döner place"; Wolf's "tell him Wolf sent you" hook | Mehmet's Silent Judgment Hold frame plays on that specific line — he will not confirm knowing Wolf |
| FEBO Automat | Comparison dialogue hook | "FEBO is machine. This is hands." |
| Club Exit (street node) | Club Exit Doorway prop, Post-Club Crowd block | Natural customer flow; crowd density scales with the club's closing timer |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A bright box of meat and light at 3 AM, run by a man who has never once been impressed"
- **Color Mood:** Döner red and Turkish gold burning against night black — warm, functional, unglamorous, deeply reassuring
- **Lighting:** Hard fluorescent interior spilling onto the pavement as a beacon; warm tower glow as the only soft light in frame
- **Texture:** Brushed stainless, thirty-two-year grease patina, crisp bread crust, laminated menu shine

### Environmental Storytelling:
- Three towers, not one — this is a shop that refuses to specialize downward
- No chairs anywhere in the scene; the absence of seating is the loudest design statement in the room
- The handwritten "NO KAPSALON" note is the only unlaminated thing in the shop, and it is the friendliest
- The bread oven at the back is bigger than the register, which tells you where the money actually comes from
- Napkin dispenser is industrial-scale and positioned before the counter — the shop knows what happens next

### Character Integration Notes:
- Mehmet occupies the carving station and never leaves it; his authority comes from position, not motion
- Elif holds the register and moves twice as fast as anyone else in frame — the generational contrast is kinetic
- The Local Regular's entire arc is two sprites; he must read as the most competent person in the building
- Post-Club Crowd renders as a single block behind featured NPCs to keep the counter legible at peak density

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Three Towers at 3 AM** — hypnotic, offset rotation, the meat trinity in full glow
2. **Mehmet's Chicken Disappointment frame** — no dialogue needed, universally legible
3. **The "NO KAPSALON. Go to Wim for that." sign** — inter-location beef, handwritten, taped
4. **The Triple Tower cross-section** — all three meats, labeled, structurally ambitious
5. **Garlic Aura in effect** — every NPC in frame standing exactly 20% further away

### Quote Potential:
- "Chicken is for children. But okay. Your döner, your choice."
- "Thirty-two years I make döner. The meat knows when you respect it."
- "Extra garlic? Okay. You plan to be alone tonight. I don't judge."
- "Hot sauce? Turkish hot. Not tourist hot. You understand? ...you'll understand soon."
- "You think Debaucheryville knows döner? Debaucheryville knows NOTHING."
- "The garlic is love. If you can't handle garlic, you can't handle love."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | leemans_interior_main.png | 1920x1080 |
| 2 | leemans_exterior_fixtures.png | 1024x1024 |
| 3 | leemans_food_items.png | 512x256 |
| 4 | npc_mehmet_elif.png | 512x512 |
| 5 | npc_leemans_customers.png | 1024x256 |
| 6 | leemans_effects.png | 512x256 |
| 7 | leemans_ui.png | 512x512 |

**Total Estimated Memory:** ~16.7 MB in-memory (uncompressed RGBA worst case), within the 32 MB location budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `leemans_interior_main.png` (1920x1080)
- [ ] `leemans_exterior_fixtures.png` (1024x1024)
- [ ] `leemans_food_items.png` (512x256)
- [ ] `npc_mehmet_elif.png` (512x512)
- [ ] `npc_leemans_customers.png` (1024x256)
- [ ] `leemans_effects.png` (512x256)
- [ ] `leemans_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + tower rotation offset guide (three towers, 1.0s stagger)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (#C41E3A, #FFD700, #1A1A1A, #8B4513, #F8F8F0, #EDE3C8)
- [ ] Key gags read clearly: three towers not one, zero chairs, the "NO KAPSALON" handwritten sign, Mehmet's Chicken Disappointment frame, the industrial napkin dispenser placed *before* the counter
- [ ] Accessibility visual alternatives included for all audio cues (sizzle, knife rhythm, register ding, pronunciation success/fail, ayran pour)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (the craft is honored; only the customer is the joke)
- [ ] Hidden areas/interactions have discoverable visual cues (sauce shape-coding, Regular status recognition, rare-approval portrait)
- [ ] Performance optimized (CPU particles, atlas limits respected, static tower fallback, pre-composed crowd blocks)
- [ ] Touch zone sizing considered (44px minimum for meat/bread/sauce options and the pronunciation input)
- [ ] Colorblind-friendly alternatives available where color codes meaning (sauce container shapes, meat silhouettes, stepped pronunciation meter)
- [ ] Social media viral potential maximized in composition choices (tower bank framing, cross-section diagram, aura recoil staging)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam late-night district; origin told as "back home" and "Debaucheryville" only |
| Cultural Specificity | ✅ | Turkish-Dutch immigrant döner culture, 1992 founding, three-tower tradition, ayran pairing |
| Satirical Targets Appropriate | ✅ | Tourist pronunciation and ordering incompetence — the Turkish craft is celebrated, never mocked |
| Seedy Underbelly Present | ✅ | Enabling 3 AM decisions, post-club exploitation-by-positioning, garlic consequences you'll carry for days |
| Gameplay Value Established | ✅ | Ordering system, pronunciation mini-game, two status effects, Triple Tower challenge, debate quest entry |
| Technical Feasibility | ✅ | Static tower/steam fallbacks per profile; overlay-based glow; pre-composed crowd blocks |
| Performance Budget | ✅ | 60 FPS, 14 draw calls, 32 MB, 14 particles per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all seven audio cues, reduced-motion set, high-contrast silhouettes, 44px touch zones |
| No Crypto Elements | ✅ | Pure meat mastery; the only currency is Sovs and Mehmet's opinion |
| Social Media Integration | ✅ | 5 screenshot moments + 6 quotable lines identified |

**Once these assets ship, Leeman's Döner Palace becomes the game's fixed point at 3 AM: three towers turning in a bright box, no chairs, no kapsalon, and a man behind the counter who has already decided what you were going to order before you opened your mouth — and is going to feed you anyway.**
