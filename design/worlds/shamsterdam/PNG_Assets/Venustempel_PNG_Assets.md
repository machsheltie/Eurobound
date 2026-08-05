# Venustempel - Complete PNG Asset Requirements

## 📋 Overview
Venustempel is the world's first sex museum, groundbreaking in 1985 and dated since roughly 1986, which in 2011 bought a chocolate collection, moved off Roodelicht Row to Museum Mile, and put a four-metre working chocolate phallus fountain on the pavement outside. It is now two museums in one building — **De Cacaogalerij**, a climate-controlled gallery of artisan chocolate genitalia curated with total sincerity, and **De Mechanische Vleugel**, the entire original Victorian curiosity collection relocated intact — and nobody has ever asked why those two things are in the same building. This document specifies every PNG asset: the plaza and its hero fountain in all six operational states, Gunter's Deep Dips and its two hero readable-text signs, the nitrogen-flushed 1974 centrepiece, the tempering room, the relocated Giggling Figure and its pneumatic inevitability, the eight photo-op stations the bros post every single frame of, the municipal HYGIËNESCORE card in its four descending states, and the gift shop you have to walk through. Its satirical essence in a sentence: the bros came to Europe for exactly this, they get it in full, they are having the best day of the trip, and four hundred strangers a day double-dip into a shared public vat of hot chocolate under a road-sign-sized notice asking them not to.

**Location ID:** `shamsterdam_museumrow_venustempel_01`
**Retired ID:** `shamsterdam_roodelicht_venustempel_01` (Roodelicht Row, 1985-2011) — no assets are authored against the old ID
**Theme:** Total transparency changes nothing. The satire targets the bros treating a working city as a theme park, and the tourism machine that sells them exactly what they want, competently, while finding them tedious.
**Register (author ruling, 2026-08-01 — binding):** **Not safe, not boring, not corporate. Subversive.** This is an MA-rated adult comedy set piece. The bros came to Europe for exactly this, they get it in full, and the consequences are ridiculous and physical. Nothing here is an anticlimax and nothing here is administrative. Permits, hygiene cards and municipal paperwork are **garnish on genuine mayhem** and must never be composed as the main event. See `Design/Character Profiles/bros_core_principle.md`.
**Currency (author ruling, 2026-08-01):** **The entire game runs on Sovs.** Every price on every asset in this document is in Sovs. There are no euro symbols anywhere and no exchange mechanic exists.
**Positioning (author ruling):** Venustempel is the **curated institution** end of Shamsterdam's chocolate-anatomy industry — artisan, historical, provenanced, gallery-grade, expensive, queued. The Shamsterdam Museum of Questionable Art is the **cheap gift shop** end — mass-produced novelty, sprinkles, fondant bow ties, 3.50 Sovs eggs, no queue. Both exist; they are opposite ends of the same trade and every asset in this document must hold that line.
**Zone:** Museum Mile (the Cultural Alibi District), plaza frontage, between Het Rijke Museum and a bureau de change, directly opposite the empty "I SHAMSTERDAM" plinth
**Hours:** 10 AM - 11 PM interior (school groups 10 AM-1 PM, peak 1-5 PM, bachelor parties 5-8 PM, quiet 8-11 PM). The fountain plaza is public space and never closes; the fountain is drained and hosed 11 PM-6 AM.
**Primary Function:** Fountain / germ-mechanic system — **Sharing the Love** five-tier stacking status, the Gunter's Deep Dips cart economy, the quarterly health-inspection world state with a downgrading score card, the Cultural Alibi flag, plus the retained Giggling Figure encounter, mutoscope coin economy, eight photo-op stations, and the John Lennon knowledge unlock

**Content Handling Note:** Every asset in this specification depicts confectionery, machinery, mannequins, framed historical artefacts, signage, municipal paperwork, food-service equipment, and visitor reactions. No sprite in this document depicts explicit content. The collection is chocolate and the fountain is a fountain — both are rendered plainly, at scale, without euphemism and without leering. This is an MA-rated adult comedy set piece and it is meant to be gleeful, crude and genuinely fun. Crude, yes; explicit, no. No minors, no real people or businesses. The institution plays it dead straight and the absurdity does the work.

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Venus Red | #DC143C | Salvaged signage, mechanical wing wash, velvet |
| Velvet Purple | #800080 | Curtains, upholstery, second floor accents |
| Vintage Cream | #FFF8DC | Placards, Victorian paper, mannequin fabric |
| Neon Pink | #FF69B4 | Exterior Venus outline, gift shop, UV accents |
| Brass Mechanism | #B08D57 | Mutoscope bodies, coin slots, pneumatic fittings |
| Couverture Brown | #3B1F0B | The chocolate itself, in bulk and in shadow |
| Tempered Gloss | #6B4226 | Cascade highlights, vitrine pieces, wet specular |
| Municipal Green | #2E6B4F | HYGIËNESCORE card, Gerda's kit, permit stock, cart livery |
| Gallery Cold | #E8ECEF | Cacaogalerij 17°C wash, vitrine glass, spot pools |
| Civic Stone | #9C9184 | Nineteenth-century frontage, plaza paving, plinth |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/venustempel/
├── environment/
│  ├── venustempel_plaza.png
│  ├── venustempel_interior_a.png
│  └── venustempel_interior_b.png
├── objects/
│  ├── venustempel_fountain.png
│  └── venustempel_exhibits.png
├── npcs/
│  ├── npc_venustempel_staff.png
│  └── npc_venustempel_plaza.png
├── effects/
│  └── venustempel_effects.png
└── ui/
  └── venustempel_ui.png
```

---

## 🍫 Sprite Sheet 1: The Plaza (Hero Environment)
**File:** `venustempel_plaza.png`
**Dimensions:** 2048x1024 pixels
**Color Palette:** #9C9184, #3B1F0B, #6B4226, #2E6B4F, #DC143C

### Plaza Backgrounds:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Museum Mile Forecourt (Day) | (0, 0) | 1024x1024 | Wide paved civic forecourt under daylight: nineteenth-century four-storey frontage with salvaged art deco "VENUSTEMPEL" lettering mounted two degrees crooked, the fountain plinth centred and dominant, Gunter's Deep Dips cart pitched four metres to the left with its menu board and patron warning sign both turned to camera and both legible, permanent crowd, the "DE CACAOGALERIJ — Nu Geopend" banner that has said Now Open since 2011, and the empty "I SHAMSTERDAM" plinth visible across the street with its own separate crowd photographing nothing |
| Museum Mile Forecourt (Night, 11 PM-6 AM) | (1024, 0) | 1024x1024 | Same forecourt, museum dark, banner unlit, neon Venus still flickering, the fountain drained and stripped to its armature, the two-person night crew in full PPE with a pressure hose and a drum trolley, the HYGIËNESCORE card still lit from below because it is a municipal fitting and municipal fittings stay lit |

### Technical Notes:
- Anchor points (Day): fountain plinth base at (512, 704), cart at (192, 736), museum door at (704, 640), ticket queue tail at (768, 800), banner at (640, 320), Venus neon at (832, 288), score card at (512, 832), ONE DIP sign at (448, 640), across-street plinth at (960, 576)
- Anchor points (Night): fountain armature at (1536, 704), night crew at (1440, 768) / (1600, 736), drum trolley at (1664, 800), hose reel at (1376, 832)
- The fountain is the tallest object in the composition and must read as a landmark from the furthest camera pull — its silhouette is the location's identity and it is a four-metre chocolate phallus, rendered plainly, without coyness and without leering
- The cart is angled so its own queue feeds directly into the fountain queue; this is a deliberate commercial arrangement and the art must show it
- Crowd density on the day plate is authored at peak (1-5 PM) and thinned by the crowd LOD system for other hours
- The across-street "I SHAMSTERDAM" plinth crowd is a separate low-detail band so the two crowds visibly interleave and photograph past each other
- The night plate ships as a full second background rather than a lighting grade — the drained fountain armature is structurally different art and it is worth having

---

## ⛲ Sprite Sheet 2: De Grote Fontein (Hero Object)
**File:** `venustempel_fountain.png`
**Dimensions:** 2048x1024 pixels
**Color Palette:** #3B1F0B, #6B4226, #9C9184, #2E6B4F

### Fountain States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Flowing (Default) | (0, 0) | 512x1024 | Full operational state. Four-metre sculpted phallus in food-grade stainless with a bronze-effect finish, four tiers of collection bowls, continuous tempered dark couverture cascading from the tip. Hot, glossy, wet specular throughout. The default and by far the most-seen state in the game. |
| Clogged | (512, 0) | 512x1024 | Flow broken and uneven across two tiers, a dropped banana slice visibly lodged in the upper channel, chocolate sheeting sideways off the second bowl onto the paving. Nobody has stopped dipping. |
| Seized (Stick Jam) | (1024, 0) | 512x1024 | Pump straining, flow reduced to a thick intermittent slump, a wooden skewer wedged crosswise in the tip aperture. The specific failure state Gunter has seen four hundred times. |
| Being Serviced | (1536, 0) | 512x1024 | Plinth service hatch open, top-up drum on a trolley, a maintenance operative on a step platform with a paddle, flow reduced but not stopped. The museum services it live, in front of the crowd, mid-trade, and the crowd waits. |

### Inspection, Drained & Detail:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Roped for Inspection | (0, 1024) | 512x0 | *See note — this state is authored on Sheet 2 via overlay, not as a fifth full render* |

*(The full-height states above consume the sheet. The two remaining states and all detail elements are authored as overlays and inserts on Sheet 5, listed under "Fountain Overlays & Plinth Furniture." This keeps the four expensive full-height renders on a single 2048x1024 sheet.)*

### Technical Notes:
- The cascade animation loop is authored against the Flowing plate only; the other three states carry their own reduced or broken loops sourced from the same frame set
- Flowing is the one animation in the location that is **never** degraded on any LOD or reduced-motion setting. It is the landmark. If it is not moving, the location does not exist.
- Wet specular is the single most important surface property in this document. Warm, mobile, slightly uneven. Chocolate that reads as cold or matte kills the asset.
- The bronze-effect stainless must read as *food-service equipment scaled up*, not as a bronze monument — visible seams, sanitary welds, a service hatch, and a manufacturer's plate at ankle height reading "ROTTERDAM" and a serial number
- The Clogged and Seized states are world-state art driven by cumulative player dipping, not random; both revert on the next service cycle
- All four states must silhouette identically at 64px so the landmark reads at map scale regardless of condition

---

## 🏛️ Sprite Sheet 3: Interior A — Entrance Hall & De Cacaogalerij
**File:** `venustempel_interior_a.png`
**Dimensions:** 2048x1024 pixels (paired room backgrounds, streamed — only one interior sheet resident at a time)
**Color Palette:** #E8ECEF, #6B4226, #FFF8DC, #DC143C, #9C9184

### Room Backgrounds:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Entrance Hall | (0, 0) | 1024x1024 | Grand civic lobby, marble floor, high ceiling, ticket desk with Anke's cross-stitch, and the Giggling Figure bolted to the floor four steps inside the door where it cannot be avoided by any route. The bench sits in direct sight of it, visibly well-used, carried over from the old building. On the wall: the 1985 opening photograph and, framed beside it at identical size, the municipal hygiene violation notice. Coin dispenser for the machines upstairs. |
| De Cacaogalerij (Ground Floor) | (1024, 0) | 1024x1024 | A serious museum gallery at 17°C: cold spot-lit vitrines on plinths, hushed, tasteful, three-language placards. De Oervorm (1974) in its nitrogen-flushed case with a live humidity readout. The National Styles Wall. The twelve-metre Scale Progression plinth running the length of the room and ending in the unnamed largest piece. The glass-walled Tempering Room with two working chocolatiers, marble slabs and thermometers. The Hollow vs. Solid cutaway. The Failures Case. |

### Technical Notes:
- Anchor points (Hall): Giggling Figure at (288, 640), ticket desk at (640, 576), bench at (352, 832), 1985 photo at (768, 384), framed violation notice at (864, 384), coin dispenser at (704, 640), stair to first floor at (928, 512)
- Anchor points (Gallery): De Oervorm case at (1216, 576), National Styles Wall at (1408, 448), Scale Progression plinth run at (1280, 800) through (1920, 800), Tempering Room glass at (1792, 512), Hollow/Solid cutaway at (1600, 640), Failures Case at (1088, 704), stair up at (1952, 576)
- The Giggling Figure's position must make it unavoidable from the door in any camera framing — the layout is the joke and the layout is load-bearing, and the relocation preserved it exactly
- The Cacaogalerij must read as a **genuinely good museum**. Gallery-grade lighting, correct plinth heights, real placard typography, honest climate control. It is funny because it is serious. If it reads as a novelty shop the asset has failed.
- The framed violation notice hangs at the same size and height as the 1985 opening photograph, deliberately, and no visitor NPC ever stops at it
- The Tempering Room glass carries a permanent condensation gradient at its base and a small handwritten "17°C" card taped to the inside
- Ceiling height in the Hall is roughly double the old canal house; a 96px character sprite must read as small here, in direct contrast to the cramped Mechanische Vleugel above

---

## 🕰️ Sprite Sheet 4: Interior B — De Mechanische Vleugel, Photo Ops & Gift Shop
**File:** `venustempel_interior_b.png`
**Dimensions:** 2048x1024 pixels (paired room backgrounds, streamed)
**Color Palette:** #DC143C, #800080, #FF69B4, #FFF8DC, #B08D57

### Room Backgrounds:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| De Mechanische Vleugel (First Floor) | (0, 0) | 1024x1024 | The entire original Venustempel collection, relocated intact and packed into a lower-ceilinged floor under red and pink wash: the mutoscope row, the Marilyn Monroe statue over its subway grate, the John Lennon sketch display (under-lit, off the main sightline), the chastity belt case, the 1800s medical diagrams, the framed historical prints, the vintage pin-up wall, the early film room screen, the 1970s section. Entered through a doorway marked only "VERVOLG →". |
| Photo Ops & Gift Shop (Second Floor / Exit) | (1024, 0) | 1024x1024 | "Ervaar de Tempel": The Throne centred as the mandatory group shot, costume rack (5 Sovs), the swing with its small "for display only" sign, wax figures in legally-distinct poses, the green screen station (10 Sovs, composites you into the cascade), the short mirror maze passage — feeding into ninety square metres of gift shop with an island display, floor-to-ceiling shelving, a proper wrapping counter, the chocolate line, and the toilet door everyone on Museum Mile uses |

### Technical Notes:
- Anchor points (Mechanical Wing): mutoscope row at (128, 576) / (128, 768), Marilyn at (448, 576), Lennon display at (704, 512), chastity case at (320, 448), medical diagrams at (576, 448), print wall at (832, 448), pin-up wall at (896, 640), film room screen at (256, 704), 1970s wall at (640, 768), "VERVOLG" doorway at (32, 640)
- Anchor points (Photo Ops / Shop): Throne at (1280, 640), costume rack at (1088, 576), swing at (1440, 512), green screen at (1536, 704), wax figures at (1184, 512), maze entrance at (1600, 576), maze exit at (1728, 704), shop counter at (1920, 768), island display at (1792, 832), toilet door at (2016, 640)
- The Mechanische Vleugel must feel **cramped** in direct contrast to the gallery below — lower ceiling, tighter circulation, warmer and dirtier light. The old museum survived the move and it survived it slightly squashed.
- The "VERVOLG →" doorway is the entire transition between a nitrogen-flushed 1974 chocolate vitrine and a room of Victorian mutoscopes. One word, one arrow. Do not add explanatory signage; the absence is the joke.
- The John Lennon display is deliberately under-lit and off the main sightline with a subtle extra frame highlight; discovering it should feel like the player found something
- The gift shop is visibly, obviously **larger than it needs to be** and Lotte is visibly pleased about it. There is still no bypass route to the exit and there must be no bypass route in the art.
- The mirror maze occupies a short passage between the photo ops and the shop; its reflective panels are authored as a tileable element (Sheet 5)

---

## 🎭 Sprite Sheet 5: Exhibits, Cart, Fixtures & Fountain Overlays
**File:** `venustempel_exhibits.png`
**Dimensions:** 2048x1024 pixels
**Color Palette:** #6B4226, #3B1F0B, #2E6B4F, #B08D57, #FFF8DC, #DC143C

### Fountain Overlays & Plinth Furniture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Roped for Inspection Overlay | (0, 0) | 384x256 | Municipal stanchions and green tape ringing the plinth, a crowd held back at the rope line, Gerda's kit case open on the paving. Composites over any fountain state. Forty minutes. |
| Drained Armature Insert | (384, 0) | 256x384 | The fountain stripped to its bare pump armature for the 11 PM-6 AM clean. Composites into the night plate. |
| Fountain Service Hatch (Open) | (640, 0) | 128x128 | Plinth access panel, pump housing visible, top-up drum coupling |
| Top-Up Drum & Trolley | (768, 0) | 128x128 | 25kg couverture drum on a service trolley |
| Collection Bowl (Tier Detail) | (896, 0) | 128x128 | Single bowl close detail, chocolate depth, a lost marshmallow at the rim |
| Manufacturer's Plate | (1024, 0) | 96x64 | Ankle height. "ROTTERDAM" and a serial number. Nobody has ever read it. |
| **HYGIËNESCORE Card — A** | (1120, 0) | 128x160 | Municipal green, laminated, bolted to the plinth. Visit 1 state. |
| **HYGIËNESCORE Card — B** | (1248, 0) | 128x160 | Visit 2 state. Identical card, different letter. |
| **HYGIËNESCORE Card — C** | (1376, 0) | 128x160 | Visit 3 state. |
| **HYGIËNESCORE Card — IN BEHANDELING** | (1504, 0) | 128x160 | Visit 4 state. The letter window has been replaced with a card showing only the inspection date. |
| ONE DIP Sign — Size 1 (Original) | (1632, 0) | 96x64 | "EEN KEER DOPEN A.U.B. / ONE DIP PLEASE." Modest. Stainless. Ignored. |
| ONE DIP Sign — Size 2 | (1728, 0) | 128x96 | Larger. Ignored. |
| ONE DIP Sign — Size 3 | (1856, 0) | 160x128 | Larger still. Ignored. |
| ONE DIP Sign — Size 4 (Current) | (1632, 128) | 256x192 | The size of a road sign. Has never worked once. |
| Municipal Stanchion (Tileable) | (1888, 128) | 64x96 | Seamless rope-line run for inspection days |

### Gunter's Deep Dips — The Cart:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cart Body (Closed, Pre-09:30) | (0, 256) | 256x192 | Shuttered, padlocked, green-and-white, the awning folded |
| Cart Body (Open, Trading) | (256, 256) | 256x192 | Awning out, wares racked, card reader on its cord, radio on the shelf, glove box, tongs in sanitiser, and the laminated straight-A hygiene card taped to the side at customer eye height |
| Skewer Rack (Loaded) | (512, 256) | 128x128 | Four hundred a day, loaded by hand |
| Organic Strawberries Skewer | (640, 256) | 64x96 | 5 SOVS. Three berries. Structurally sound. |
| Jumbo Marshmallows Skewer | (704, 256) | 64x96 | 5 SOVS. Loses one to the bowl 40% of the time. |
| Rice Krispie Squares Skewer | (768, 256) | 64x96 | 5 SOVS. Disintegrates on a second dip. Guaranteed re-dip attempt. |
| Banana Slices Skewer | (832, 256) | 64x96 | 5 SOVS. Falls off. Always. |
| Pineapple Chunks Skewer | (896, 256) | 64x96 | 5 SOVS. The only item that survives four dips. |
| **Bare Wooden Skewer** | (960, 256) | 64x96 | 1 SOV. Nothing on it. Not on the board. Best margin on the cart. Sells constantly. |
| Hand Wipe Sachet | (1024, 256) | 64x64 | 1 SOV. Not on the board. Offered every transaction. Almost never bought. |
| **THE MENU BOARD** | (1088, 256) | 288x224 | **HERO READABLE TEXT ASSET.** Hand-lettered, laminated, mounted at customer eye height. Full verbatim copy below — must be legible at gameplay zoom on a 5-inch display without an inspect mode. |
| **THE WARNING SIGN TO PATRONS** | (1376, 256) | 288x160 | **HERO READABLE TEXT ASSET.** Bolted beside the board. Municipal in tone, entirely sincere, universally ignored. Full verbatim copy below — must be legible at gameplay zoom on a 5-inch display without an inspect mode. |
| Cart Hygiene Card (A) | (1664, 256) | 96x128 | Straight A. He will point at it. |
| Sanitiser Tub & Tongs | (1760, 256) | 96x96 | His actual working hygiene, in frame, four metres from the fountain |
| Glove Box (Half Used) | (1856, 256) | 96x96 | Changed constantly. The box is always half empty. |
| Card Reader on Cord | (1952, 256) | 64x64 | The one moment per customer he looks up |
| Cart Radio | (1952, 320) | 64x64 | Talk radio. He does not listen to it. |
| Skewer Waste Bin (Overflowing) | (1664, 384) | 96x96 | Emptied hourly. Never empty. |

### 📜 Verbatim Signage Copy (Author-Supplied — Reproduce Exactly)

**THE MENU BOARD** — set this text and nothing else. Do not paraphrase, abbreviate, reformat, or sanitize. Line breaks and parentheticals as written.

> **"Get them while they're hot and heavy- 5 SOVS"**
>
> **Organic Strawberries**
> *(Plump, firm, and begging to be absolutely smothered.)*
>
> **Pineapple Chunks**
> *(For a sweeter finish. You know why. We don't need to explain it to you.)*
>
> **Banana Slices**
> *(Just the tips. Yes, it's redundant. No, we don't judge.)*
>
> **Jumbo Marshmallows**
> *(Soft, sticky, and expands nicely in the mouth.)*
>
> **Rice Krispie Squares**
> *(Firm, rigid, and heavily textured for maximum friction against the flow.)*

**THE WARNING SIGN TO PATRONS** — set this text and nothing else.

> **"Please maintain a firm, two-handed grip on your skewer at all times. Do NOT double-dip, do NOT stroke the fountain base, and absolutely NO open-mouth catching directly from the tip of the statue. We've had incidents."**

**Signage art direction:**
- Both are the comedic centrepiece of the location and both are **readable in-world text**, not set dressing. If a player cannot read them from standing distance at gameplay zoom on a 5-inch display, the asset is a reject.
- The board is hand-lettered and cheerful. The warning sign is municipal, formal and completely sincere — different typography, different stock, different tone. The gap between how the two signs are *set* is a second joke on top of the first.
- Neither sign winks. No cartoon eyes, no nudge iconography, no exclamation-mark flourishes, no double-entendre visual puns. Plain shop signage that happens to say this. The straight-faced typesetting is what makes the copy land.
- **"We've had incidents" is the key line.** It implies an entire history that nobody explains, and nobody in the game ever does. Set it at the same weight as the rest of the sign; do not emphasise it.
- Both are baked at 2x internal resolution and flagged for the uncompressed-texture exception list.
- The warning sign forbids double-dipping. Every visitor NPC in the plaza composition double-dips. Both facts must be visible in the same frame.

### De Cacaogalerij Exhibits:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| **De Oervorm (1974)** | (0, 448) | 192x256 | The oldest surviving piece. Hand-moulded, cracked down one side, in a nitrogen-flushed case with a live humidity readout. Genuinely fragile, genuinely irreplaceable, insured for more than the van that moved it. Render it with real reverence. |
| National Styles Wall | (192, 448) | 256x192 | Belgian, Swiss, French, Dutch, Italian, side by side, with a tempering-difference placard nobody reads |
| Scale Progression (Tileable Plinth Run) | (448, 448) | 256x128 | Eleven pieces ascending along twelve metres; authored as a tileable plinth segment plus per-piece inserts |
| Scale Progression — "The Big One" | (704, 448) | 192x256 | The terminal piece. The museum has never given it a name. Internally: "the big one." |
| Tempering Room Glass & Interior | (896, 448) | 256x256 | Marble slabs, seeding, thermometer, two chocolatiers in absolute concentration, condensation gradient at the base of the glass, a handwritten "17°C" card taped inside |
| Hollow vs. Solid Cutaway | (1152, 448) | 192x160 | Structural failure modes, dated and updated weekly in summer with actual casualties |
| **The Failures Case** | (1344, 448) | 192x160 | Bloomed, seized, split and collapsed pieces with honest labels. The curator's favourite case. Nobody stops at it. Its placard is genuinely sad and it is worth reading. |
| "De Fontein: Een Technisch Verhaal" | (1536, 448) | 192x160 | Original Rotterdam engineering drawings and a framed letter from the firm politely declining to build a second one |
| Gallery Vitrine (Tileable) | (1728, 448) | 128x160 | Seamless cold-lit case run |
| Three-Language Placard (Tileable) | (1856, 448) | 128x96 | NL / EN / DE, gallery typography, played completely straight |
| Humidity Readout | (1856, 544) | 96x64 | Live display on De Oervorm's case |

### De Mechanische Vleugel Exhibits (Relocated Intact):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Giggling Figure (Static / Rest) | (0, 704) | 192x288 | Life-sized Victorian mannequin at rest, skirts down, mechanism dormant, entirely innocent-looking. Now bolted to a marble lobby floor rather than boards. |
| Peep Show Device (Mutoscope) | (192, 704) | 160x224 | Coin-operated Victorian flip-card viewer, brass body, original |
| Marilyn Monroe Statue (Rest) | (352, 704) | 160x288 | Over the subway grate, dress down, waiting for the timer |
| John Lennon Sketch Display | (512, 704) | 160x224 | Yes, really. He drew these. The most genuinely interesting object in the building, under-lit and off the sightline. |
| Chastity Belt Display | (672, 704) | 224x128 | Real artefacts, questionable provenance, universally photographed |
| Medical Diagrams (1800s) | (896, 704) | 160x128 | "Educational" anatomy charts, more terrifying than titillating |
| Historical "Art" Frames | (1056, 704) | 160x128 | Prints that would have been contraband 150 years ago |
| Vintage Pin-Up Wall | (1216, 704) | 160x224 | From tasteful to "what decade was this acceptable" |
| Early Film Room Screen | (1376, 704) | 160x128 | Looping clips from the earliest adult cinema. Surprisingly boring. |
| 1970s Section Wall | (1536, 704) | 160x128 | An aesthetic that has not aged well and is fascinating for exactly that reason |
| Wax Figures (Legally Distinct) | (1696, 704) | 128x224 | Celebrities. Allegedly. Legally distinct. Allegedly. |
| "VERVOLG →" Doorway Placard | (1824, 704) | 128x64 | One word, one arrow. The entire explanation. |
| Coin Slot Detail | (1824, 768) | 96x96 | 1 Sov per viewing, brass, worn smooth |

### Photo Ops, Gift Shop, Signage & Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Throne | (0, 992) | 224x32 | *(overflow strip — see note)* |

*(Remaining fixtures continue on the reserved lower band; the authoritative placements are:)*

| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Throne | (1120, 608) | 224x96 | Oversized chair. Mandatory group photo spot. Bradley will not be sitting on that. |
| Costume Corner Rack | (1344, 608) | 160x96 | 5 Sovs rental accessories for "artistic" photos |
| Green Screen Station | (1504, 608) | 160x96 | 10 Sovs printed composite into the cascade. Best-selling photo product in the building. |
| The Swing ("For Display Only") | (1664, 608) | 96x96 | The sign is small. It is still for display only. |
| Mirror Maze Panel (Tileable) | (1760, 608) | 96x96 | Reflective panel, seamless, assembles to any passage length |
| Mirror Maze Corner Piece | (1856, 608) | 96x96 | 90° junction with double reflection |
| Gift Shop Island Display | (1952, 608) | 96x96 | The new one. Ninety square metres allowed it. Lotte is delighted. |
| Gift Shop Shelving (Tileable) | (1952, 448) | 96x160 | Floor to ceiling, aggressively stocked, judgement-free |
| Wrapping Counter | (1952, 704) | 96x160 | Proper counter, tape dispenser, ribbon spools, plain discreet stock underneath |
| Chocolate Line Display | (1952, 864) | 96x160 | Solid and hollow, white/milk/dark, "De Collectie" boxed sets |
| "Handreiniger" Bottle | (1888, 864) | 64x96 | 4 Sovs. Moulded in the shape of the fountain. Faced forward on the counter. Sells poorly. |
| Fountain Keyring & Magnet | (1824, 864) | 64x96 | 5 Sovs and 3.50 Sovs. These sell fine. |
| Bench | (1728, 864) | 96x96 | Carried over from Roodelicht Row. Same bench. Visibly well-used. |
| Ticket Desk + Cross-Stitch | (1632, 864) | 96x96 | 9 Sovs, cash or card, coins for the machines, Anke's project |
| 1985 Opening Photograph (Framed) | (1536, 864) | 96x96 | On the lobby wall |
| **Framed Violation Notice** | (1440, 864) | 96x96 | Same wall, same size, same height. The museum thinks it is funny. Nobody reads it. |
| Neon Venus Outline | (1344, 864) | 96x128 | Salvaged. Pink. Always on, always flickering slightly. |
| Art Deco "VENUSTEMPEL" Sign | (1152, 864) | 192x64 | Salvaged, mounted two degrees crooked on a building that predates art deco by sixty years |
| "DE CACAOGALERIJ — Nu Geopend" Banner | (1152, 928) | 192x64 | Has said Now Open since 2011 |
| "ADULTS ONLY" Sign | (1056, 864) | 96x64 | Font suggests this was added later |
| "Educational Exhibits" Plaque | (1056, 928) | 96x64 | Sure |
| 5 Sovs-Under-9 Sovs Ticket Sign | (960, 864) | 96x64 | The sign says five. The sign is old. There is a sticker. |
| Creaky Wooden Stairs | (864, 864) | 96x64 | Between the wings. The building is old and says so. |
| Victorian Music Box | (864, 928) | 96x64 | Mechanical wing ambient source, period appropriate |
| Red Velvet Curtain (Tileable) | (768, 864) | 96x160 | Seamless vertical drape run, mechanical wing |
| Marble Lobby Tile (Tileable) | (672, 864) | 96x80 | Civic, cold, seamless all edges |
| Gallery Floor Tile (Tileable) | (672, 944) | 96x80 | Cacaogalerij, pale, seamless all edges |
| Plaza Paving Tile (Tileable) | (576, 864) | 96x80 | Civic stone, chocolate-spattered variant included |
| Museum Floor Tile (Tileable) | (576, 944) | 96x80 | Worn board, mechanical wing, seamless all edges |

### Technical Notes:
- The Giggling Figure at rest must look completely harmless; nothing in the static sprite may telegraph the mechanism. First-encounter comedy depends entirely on this and the relocation did not change it.
- **De Oervorm and the Failures Case are the two assets in this document that must be rendered without a single joke in them.** The 1974 piece is a genuine artefact in a nitrogen case and the Failures Case placard is genuinely sad. The surrounding sincerity is what makes the fountain outside funny.
- The four HYGIËNESCORE cards are identical municipal stock with a swapped letter window; the fourth replaces the window entirely with a date card. They must be legible at gameplay zoom on a 5-inch display — the player has to be able to read the downgrade without entering an inspect mode.
- The four ONE DIP signs must all read as the same sign at four scales, in the same stainless, with the same wording. The escalation is the gag and identical typography sells it.
- Gunter's cart hygiene card (A) and the fountain plinth card (A→B→C→IN BEHANDELING) use the same municipal template, at the same size, four metres apart. This adjacency is the single most important compositional relationship on the plaza and must survive every camera framing.
- The cart's sanitiser tub, tongs and half-empty glove box are load-bearing props, not set dressing — her competence is visible or the joke does not land
- Six tileable assets: Red Velvet Curtain, Mirror Maze Panel, Marble Lobby Tile, Gallery Floor Tile, Plaza Paving Tile, Museum Floor Tile. Plus tileable runs for Gallery Vitrine, Three-Language Placard, Gift Shop Shelving, Scale Progression plinth and Municipal Stanchion.
- All signage, placards and hygiene cards are baked at 2x internal resolution and flagged for the uncompressed-texture exception list

---

## ⚙️ Sprite Sheet 6: Animated Mechanisms & The Dip
**File:** `venustempel_animated_objects.png`
**Dimensions:** 2048x1024 pixels
**Color Palette:** #6B4226, #3B1F0B, #FFF8DC, #B08D57, #DC143C

### The Cascade (Hero Loop):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cascade Frame 1 | (0, 0) | 256x512 | Flow from tip over tier one |
| Cascade Frame 2 | (256, 0) | 256x512 | Tier two sheeting |
| Cascade Frame 3 | (512, 0) | 256x512 | Tier three, full weight |
| Cascade Frame 4 | (768, 0) | 256x512 | Tier four, return to sump |
| Cascade Frame 5 | (1024, 0) | 256x512 | Loop midpoint, offset sheeting |
| Cascade Frame 6 | (1280, 0) | 256x512 | Loop close, seamless to frame 1 |
| Cascade — Clogged Variant | (1536, 0) | 256x512 | Two-tier break, sideways sheeting onto paving |
| Cascade — Seized Variant | (1792, 0) | 256x512 | Thick intermittent slump around a wedged skewer |

### The Dip Cycle:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dip Frame 1 — Approach | (0, 512) | 128x128 | Skewer entering the flow |
| Dip Frame 2 — Immerse | (128, 512) | 128x128 | Contact, displacement, the sound the whole mechanic hangs on |
| Dip Frame 3 — Coat | (256, 512) | 128x128 | Full coverage, the item disappearing |
| Dip Frame 4 — Lift | (384, 512) | 128x128 | Withdrawal, chocolate tension breaking |
| Dip Frame 5 — Drip | (512, 512) | 128x128 | Three-second trailing drip |
| Dip Frame 6 — Clear | (640, 512) | 128x128 | Coated, glossy, held, ready |
| **Re-Dip (Double-Dip) Variant** | (768, 512) | 128x128 | Bitten item returning to the flow. +2 stacks. The default player behaviour. |
| **Bare Hand Dip** | (896, 512) | 128x128 | +3 stacks. A worse, wetter version of the whole cycle. |
| Bowl Retrieval (Hand in Bowl) | (1024, 512) | 128x128 | +3 stacks. Unavoidable with banana or marshmallow. |
| **Leaning Into The Cascade** | (1152, 512) | 128x128 | +5 stacks. Once per bro. Ruud will intervene. Ruud will be too late. |
| Item Loss to Bowl | (1280, 512) | 128x128 | The marshmallow's 40%, the banana's 100% |

### Retained Mechanisms:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Giggling Figure Frame 1 | (1408, 512) | 160x256 | Mechanism engages, skirts begin to lift, the clicking has already started |
| Giggling Figure Frame 2 | (1568, 512) | 160x256 | Mid-lift, pneumatic, unstoppable |
| Giggling Figure Frame 3 | (1728, 512) | 160x256 | Full extent, recorded giggle plays, an entire marble lobby jumps at once |
| Giggling Figure Frame 4 | (1888, 512) | 160x256 | Descent, mechanism resets, thirty seconds until the next one |
| Marilyn Billow Frame 1 | (0, 768) | 128x256 | Grate activates |
| Marilyn Billow Frame 2 | (128, 768) | 128x256 | Rising |
| Marilyn Billow Frame 3 | (256, 768) | 128x256 | Full billow, the photograph everyone takes |
| Marilyn Billow Frame 4 | (384, 768) | 128x256 | Settling, thirty-second reset |
| Flip Card Frames 1-8 | (512, 768) | 512x64 | Eight 128x64 Victorian silhouette frames, period mutoscope reel style, tame by any modern standard |
| Tempering Room Loop (4 frames) | (512, 832) | 512x96 | Chocolatier working the marble: pour, spread, gather, test. Continuous background loop. |
| Cart Transaction Loop (4 frames) | (1024, 768) | 256x96 | Gunter: load, hand over, take payment, next. Four frames, no wasted motion. |
| Motion Sensor Trigger Zone | (1280, 768) | 96x96 | Dev/accessibility visualisation of the Giggling Figure's detection radius |
| Mechanical Clicking Indicator | (1376, 768) | 96x96 | The pre-activation tell; learn to anticipate |
| Pneumatic Hiss Plate | (1472, 768) | 64x96 | Air release visualisation |

### Accessibility & Reduced Motion Variants:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| **Cascade Reduced-Motion Loop (2 frames)** | (1536, 768) | 256x256 | The cascade is never fully static. In reduced-motion mode it drops to a slow two-frame breathe. The landmark must always be alive. |
| Fountain High-Contrast Silhouette | (1792, 768) | 256x256 | Bold outline variant of the location's defining object |
| Giggling Figure High-Contrast Silhouette | (1280, 864) | 128x160 | Bold outline variant |
| Static Giggling Figure (Reduced Motion) | (1408, 864) | 128x160 | Locked to frame 1; no lift, no jump-scare, the giggle audio and glyph still play |
| Static Marilyn (Reduced Motion) | (1536, 1024) | 0x0 | *(see note)* |
| Peep Show Static Card | (1024, 864) | 128x64 | Single-frame substitute for the flip animation |
| Static Marilyn (Reduced Motion) | (1152, 864) | 128x160 | Holds at rest; the photo station still functions |
| Static Dip (Reduced Motion) | (896, 864) | 128x128 | Frames 1 and 6 only — contact and result, no intermediate motion. The stack is still applied and the audio still fires. |
| Reserve | (768, 864) | 128x160 | Reserved cell, do not paint |

### Technical Notes:
- **The six-frame cascade is the most important animation in the location and possibly in Shamsterdam.** It never degrades below two frames on any setting. A static fountain reads as broken, and a broken fountain is a different joke.
- Chocolate motion must have *weight*. Couverture is heavy, slow, and slightly reluctant. Water-like flow kills the asset instantly.
- The Dip Cycle's frame 2 (Immerse) carries the location's signature sound and must be authored to feel unreasonably satisfying — the player should want to do it again, because wanting to do it again is the entire germ mechanic
- The Re-Dip variant is visually near-identical to a standard dip. It is not flagged, highlighted, or warned about in the art. The player does it because it is natural.
- The Giggling Figure's four frames must read as *mechanical* rather than lifelike — visible pneumatic strut, slight jerkiness, 1985 build quality. Now with a marble floor under it, which makes the bolt flange visible and slightly worse.
- Flip cards depict Victorian-era silhouettes only, in period mutoscope reel style; they are tame by any modern standard and that is the punchline the game explicitly makes
- Both retained mechanisms reset on a hard 30-second timer with no randomisation — predictability is required for the "learn to anticipate" gag
- The duplicate "Static Marilyn" row above is resolved to the (1152, 864) placement; the (1536, 1024) entry is a documentation artefact and must not be painted

---

## 🧵 Sprite Sheet 7: Museum Staff
**File:** `npc_venustempel_staff.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 per character frame; 128x128 per portrait
**Color Palette:** #DC143C, #FF69B4, #FFF8DC, #6B4226

### Ticket Seller Anke — Fifteen Years of Immunity:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Anke Ticket Seller Idle | (0, 0) | 64x96 | Middle-aged Dutch, reading glasses, entirely unfazed |
| Anke Cross-Stitch | (64, 0) | 64x96 | Between customers. Always between customers. |
| Anke Coin Exchange | (128, 0) | 64x96 | "Coins for the machines are there." |
| Anke Deadpan Frame 1 | (192, 0) | 64x96 | Has heard every possible reaction |
| Anke Deadpan Frame 2 | (256, 0) | 64x96 | Is immune to all of them |
| Anke "You will also jump." | (320, 0) | 64x96 | Not a warning. A prediction. Accurate. |
| Anke "The fountain is free." | (384, 0) | 64x96 | She cannot sell you a ticket for it. She has explained this today eleven times. |
| Anke "Toilets are past the gift shop. Go now." | (448, 0) | 64x96 | Fires at Sharing the Love Tier 4. No further comment. |

### Floor Attendant Ruud:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ruud Floor Attendant Idle | (0, 96) | 64x96 | Young Dutch, museum polo, "this is my summer job" |
| **Ruud "One dip."** | (64, 96) | 64x96 | Plaza rotation. Nine hundred times a day. The single most-used staff frame in the location. |
| Ruud "One dip, please. Sir." | (128, 96) | 64x96 | Escalation tier two of three. There is no tier three. |
| Ruud "Please do not put your face in the fountain." | (192, 96) | 64x96 | He is too late. He is always too late. |
| Ruud "No flash on the 1974." | (256, 96) | 64x96 | The only time his professional neutrality carries real feeling |
| Ruud Suppressed Smile | (320, 96) | 64x96 | Briefly failing. Deploy rarely. |
| Ruud Bench Suggestion | (384, 96) | 64x96 | "Many people use the bench." |
| Ruud at Lennon Display | (448, 96) | 64x96 | "Yes, really. I don't know why either. But yes." |

### Gift Shop Attendant Lotte Beekman:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lotte Gift Shop Idle | (0, 192) | 64x96 | Pink apron, ribbon in her hair, aggressively helpful |
| Lotte Gift Wrapping | (64, 192) | 64x96 | "No judgment. Very discreet packaging available." |
| **Lotte Handreiniger Recommendation** | (128, 192) | 64x96 | Cheerful, sincere, every departing customer, every time. Nobody takes one. |
| Lotte "Ninety square metres." | (192, 192) | 64x96 | Genuinely delighted. On Roodelicht it was forty-one. |
| Lotte Solid-or-Hollow Pitch | (256, 192) | 64x96 | "Hollow will not survive August." Everyone buys hollow. |
| Lotte at the Lennon Print | (320, 192) | 64x96 | Her favourite thing in the shop. She is right about it. |
| Lotte Postcard Recommendation | (384, 192) | 64x96 | "Yes, you can mail them. Yes, people do mail them." |
| Lotte "We'll be here when you're ready." | (448, 192) | 64x96 | Since 1985. Delivered warmly. |

### Portraits:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Anke Portrait (Dialogue) | (0, 288) | 128x128 | Fifteen years. Cross-stitch. Nothing left to surprise her. |
| Ruud Portrait (Dialogue) | (128, 288) | 128x128 | Professionally neutral, visibly fraying at the plaza rotation |
| Lotte Portrait (Dialogue) | (256, 288) | 128x128 | Cheerful, pink apron, gift-wrapping ribbon, entirely sincere |
| Staff Portrait Reserve | (384, 288) | 128x128 | Reserved for a fourth staff portrait, do not paint |

### Accessibility & Anchors:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Anke High-Contrast Silhouette | (0, 416) | 64x96 | Accessibility outline variant |
| Ruud High-Contrast Silhouette | (64, 416) | 64x96 | Accessibility outline variant |
| Lotte High-Contrast Silhouette | (128, 416) | 64x96 | Accessibility outline variant |
| Ticket Desk Pose (Anke) | (192, 416) | 64x96 | Behind-counter anchor pose |
| Shop Counter Pose (Lotte) | (256, 416) | 64x96 | Behind-counter anchor pose |
| Plaza Rotation Pose (Ruud) | (320, 416) | 64x96 | Outdoor anchor pose, hi-vis over the museum polo |
| Accessibility Reserve Block | (384, 416) | 128x96 | Reserved for high-contrast/audio-cue glyph overflow |

### Technical Notes:
- Anke's two Deadpan frames must be functionally identical; the immunity is the characterisation and it must be visually total
- Ruud is the only staff member whose composure visibly degrades, and it degrades only on plaza rotation. His "One dip." frame is used more than any other sprite in the location. Author it to survive nine hundred repetitions a day without becoming a bit.
- Ruud's Suppressed Smile is the only frame in the staff set with a positive visible reaction, and it fires rarely
- Lotte treats every transaction as completely normal in every frame; no knowing looks, no winks. Her cheerfulness is sincere and that is what makes the gift shop funny. Her "Ninety square metres" frame carries genuine pride and must not read as ironic.
- No staff frame in this set may express disapproval, judgement, discomfort, or complicity. They are competent professionals having an ordinary working day.

---

## 👥 Sprite Sheet 8: Plaza NPCs, Visitors, Effects & UI
**File:** `npc_venustempel_plaza.png` / `venustempel_effects.png` / `venustempel_ui.png`

### 8a. Plaza NPCs — `npc_venustempel_plaza.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 per character frame; 128x128 per portrait
**Color Palette:** #2E6B4F, #6B4226, mixed tourist palette

| Element | Position | Size | Description |
|---------|----------|------|-------------|
| **Gunter Idle (Behind Cart)** | (0, 0) | 64x96 | Cap, apron, gloves, not looking up |
| Gunter Loading Skewers | (64, 0) | 64x96 | Four hundred a day, twelve years, no wasted motion |
| Gunter Hand-Over | (128, 0) | 64x96 | The one moment per customer he looks up |
| Gunter Card Reader | (192, 0) | 64x96 | Payment. Glasses on the cord, used only for this. |
| Gunter Glove Change | (256, 0) | 64x96 | Constant. Visible. Load-bearing. |
| **Gunter "Wipe? One SOV."** | (320, 0) | 64x96 | Offered flat, every transaction, at the same volume as the price |
| Gunter Pointing At His Hygiene Card | (384, 0) | 64x96 | Straight A. Four metres from the fountain. |
| Gunter "I have seen the fountain." | (448, 0) | 64x96 | Asked whether he eats there. One beat, then the line. |
| **Gerda Vonk Idle** | (0, 96) | 64x96 | Municipal hi-vis over a good coat, clipboard, no small talk |
| Gerda Setting the Rope | (64, 96) | 64x96 | Forty minutes. The crowd waits. |
| Gerda Taking a Sample | (128, 96) | 64x96 | Yes, from the fountain. Yes, that is the job. |
| Gerda Probe Thermometer | (192, 96) | 64x96 | Procedure |
| Gerda Shoe Covers | (256, 96) | 64x96 | On a paved outdoor square, because the procedure says so |
| Gerda Writing the Violation | (320, 96) | 64x96 | Same finding as March |
| Gerda "You have a bigger sign now." | (384, 96) | 64x96 | To Ruud. Without looking up. |
| Gerda Departing | (448, 96) | 64x96 | Forty other premises this week |
| Night Crew Operative A | (0, 192) | 64x96 | Full PPE, pressure hose |
| Night Crew Operative B | (64, 192) | 64x96 | Full PPE, drum trolley. They do not make eye contact with each other. |
| Gunter Portrait | (128, 192) | 128x128 | Mid-to-late forties, big, cap, forearms, total equanimity. Deadpan. Has heard every joke. |
| Gerda Portrait | (256, 192) | 128x128 | Correct, thorough, entirely unbothered |
| Cart Queue Silhouette | (384, 192) | 128x64 | Depth band for the Gunter's Deep Dips queue |
| Fountain Queue Silhouette | (384, 256) | 128x64 | Depth band for the fountain crowd |
| Gunter High-Contrast Silhouette | (0, 320) | 64x96 | Accessibility outline variant |
| Gerda High-Contrast Silhouette | (64, 320) | 64x96 | Accessibility outline variant |
| Cart Anchor Pose (Gunter) | (128, 320) | 64x96 | Behind-cart anchor pose |
| Rope-Line Anchor Pose (Gerda) | (192, 320) | 64x96 | Inspection anchor pose |
| **Bachelor Party (British)** | (256, 320) | 256x96 | Six lads, "GARY'S LAST STAND" shirts, one recording. A dipping contest with invented rules. |
| **Family With Small Children** | (0, 416) | 192x96 | Two parents, three under eight, all five at the fountain, none going inside. The funniest fact about this location, stated without comment. |
| Couple on Holiday | (192, 416) | 128x96 | Guidebook out, one of them actually reading the placards |
| Solo Traveler (Suspicious) | (320, 416) | 64x96 | No camera. No stick. Just looking. Probably fine. |
| Teenager Who Got In | (384, 416) | 64x96 | Dipped four times on the way in |
| School Group (Food Technology) | (448, 416) | 64x96 | Vocational catering students; the group block composites from this base frame |

### 8b. Effects — `venustempel_effects.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #6B4226, #3B1F0B, #DC143C, #FF69B4, #2E6B4F

| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cascade Wet Specular | (0, 0) | 64x64 | The single most important surface effect in the location |
| Chocolate Drip (3s trail) | (64, 0) | 64x64 | Post-lift, every dip |
| Chocolate Drip (Bare Hand) | (128, 0) | 64x64 | A worse, wetter version |
| Chocolate Spatter (Paving) | (192, 0) | 64x64 | Accumulates through the trading day, reset by the night crew |
| Cocoa Steam | (256, 0) | 64x64 | Rising off the cascade; carries the smell the game cannot render |
| Bowl Ripple | (320, 0) | 64x64 | Displacement on immersion |
| Item Loss Plop | (384, 0) | 64x64 | The marshmallow's 40% |
| Chocolate Tension Break | (448, 0) | 64x64 | The moment on lift |
| Camera Flash Burst Frame 1 | (0, 64) | 64x64 | Constant on the plaza and the second floor |
| Camera Flash Burst Frame 2 | (64, 64) | 64x64 | Falloff |
| Pink Neon Flicker Frame 1 | (128, 64) | 64x64 | Salvaged exterior Venus outline |
| Pink Neon Flicker Frame 2 | (192, 64) | 64x64 | The slight, permanent, never-fixed flicker |
| Red Light Wash Plate | (256, 64) | 64x64 | Mechanical wing grade |
| Gallery Cold Wash Plate | (320, 64) | 64x64 | Cacaogalerij 17°C grade |
| Plaza Daylight Wash | (384, 64) | 64x64 | Open forecourt grade |
| Plaza Night Wash | (448, 64) | 64x64 | 11 PM-6 AM grade |
| Spot Lighting Pool | (0, 128) | 64x64 | Per-exhibit gallery spot |
| UV Accent Glow | (64, 128) | 64x64 | Second floor and mirror maze |
| Dust Motes (Old Building) | (128, 128) | 64x64 | Mechanical wing only; the gallery is filtered |
| Mirror Maze Fog | (192, 128) | 64x64 | Subtle, disorienting, short-lived |
| Mirror Reflection Ghost | (256, 128) | 64x64 | Low-detail silhouette layer at 40% alpha |
| Pneumatic Hiss Puff | (320, 128) | 64x64 | The Giggling Figure venting |
| Mechanical Click Spark | (384, 128) | 64x64 | The pre-activation tell, visible as well as audible |
| Coin Drop Glint | (448, 128) | 64x64 | 1 Sov entering a mutoscope |
| Jump-Scare Vignette | (0, 192) | 64x64 | First Giggling Figure encounter only, once per save file |
| Startle Flush Overlay | (64, 192) | 64x64 | Character-parented, half-second Composure gag. **Ambient visitor NPCs only** — never applied to the bros, who are not embarrassed by anything in this building and think the mannequin rules. |
| **Sharing the Love Tier Aura T1-T2** | (128, 192) | 64x64 | Faint, warm, entirely pleasant. It looks like a buff. It is currently a buff. |
| **Sharing the Love Tier Aura T3** | (192, 192) | 64x64 | The warmth curdles slightly. No character comments. |
| **Sharing the Love Tier Aura T4** | (256, 192) | 64x64 | Urgency. Paired with the facilities marker. |
| **Sharing the Love Tier Aura T5** | (320, 192) | 64x64 | Shamsterdam Stomach. Full-party overlay. |
| Stomach Gurgle Visualiser | (384, 192) | 64x64 | Enters at Tier 2 and never fully leaves. Louder by tier. Never mentioned by any character. |
| Municipal Rope Shimmer | (448, 192) | 64x64 | Inspection-day tape movement |

### Visual Audio Cue Glyphs:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| **The Dip Glyph** | (0, 256) | 32x32 | Mirrors the signature immersion sound. The most-fired glyph in the location. |
| Drip Glyph | (32, 256) | 32x32 | Mirrors the three-second trail |
| Cascade Glyph | (64, 256) | 32x32 | Mirrors the continuous flow; persistent, low-frequency |
| Pump Hum Glyph | (96, 256) | 32x32 | Mirrors the low mechanical hum under the cascade |
| **Mechanical Click Glyph** | (128, 256) | 32x32 | Mirrors the pre-activation clicking — the anticipation cue |
| Giggle Glyph | (160, 256) | 32x32 | Mirrors the signature recorded giggle |
| Pneumatic Hiss Glyph | (192, 256) | 32x32 | Mirrors the mechanism venting |
| Camera Shutter Glyph | (224, 256) | 32x32 | Mirrors constant tourist photography |
| Coin Clunk Glyph | (256, 256) | 32x32 | Mirrors coin insertion |
| Flip Card Glyph | (288, 256) | 32x32 | Mirrors the mutoscope card flipping |
| Marilyn Whoosh Glyph | (320, 256) | 32x32 | Mirrors the dress mechanism |
| Music Box Glyph | (352, 256) | 32x32 | Mirrors the mechanical wing music box |
| Stair Creak Glyph | (384, 256) | 32x32 | Mirrors the old wooden stairs |
| Skewer Snap Glyph | (416, 256) | 32x32 | Mirrors the cart transaction rhythm |
| **Gurgle Glyph** | (448, 256) | 32x32 | Mirrors the Tier 2+ ambient stomach bed |
| "One Dip" Glyph | (480, 256) | 32x32 | Mirrors Ruud's endless plaza line |

### Reduced Motion & Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Slow Cascade Plate (Reduced Motion) | (0, 320) | 128x128 | Two-frame breathe. The fountain is never fully static. |
| No-Flash Plate | (128, 320) | 64x64 | Photography without the burst; ambient NPC flashes also suppressed |
| Static Fog | (192, 320) | 64x64 | Motionless mirror maze atmosphere |
| Static Neon | (256, 320) | 64x64 | Steady exterior Venus outline |
| Static Steam | (320, 320) | 64x64 | Held cocoa steam |
| Static Gurgle Marker | (384, 320) | 64x64 | Non-animated Tier indicator |
| Fountain High-Contrast Marker | (448, 320) | 64x64 | Bold outline pip for the plaza's key interactive |
| Effects Reserve | (0, 384) | 512x128 | Reserved band, do not paint |

### 8c. UI — `venustempel_ui.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #6B4226 UI chrome, #2E6B4F municipal panels, #DC143C highlights, #FF69B4 accents

#### Sharing the Love System:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| **Sharing the Love Stack Meter** | (0, 0) | 256x96 | Five segmented tiers with written tier names, never a colour gradient. Reads as a buff at T1-T2. |
| Tier Name Plate Set | (256, 0) | 256x96 | Five 128x48 plates: Warm Inside / Communal / Well-Travelled Chocolate / De Fontein Voorziet / Everyone's Chocolate |
| Stack Gain Popup | (512, 0) | 192x64 | "+1", "+2 (double-dip)", "+3 (bare hand)", "+5". States the reason in plain text. Never warns. |
| **The Attribution Table** | (704, 0) | 320x96 | Eight ranked blame entries: döner, tap water, "European milk", pancakes, Bradley's protein powder, jet lag, "something in the air here", each other. The fountain is not on the list and cannot be added to it. |
| Shamsterdam Stomach Banner | (0, 96) | 256x64 | Tier 5. Max HP −40% for the in-game day, Bravado gains halved. |
| Facilities Urgency Marker | (256, 96) | 128x64 | Tier 4. Flashing on Febo Automat and Voetgangerstunnel only. |
| Cure Item Row | (384, 96) | 256x64 | Four 64x64: hand wipe (1 Sov, −1) / Handreiniger (4 Sovs, −2) / hostel rest (−2) / Febo croquette (2.20 Sovs, −1) |
| Stack Decay Indicator | (640, 96) | 128x64 | −1 per in-game day, shown as a plain countdown |
| Sharing the Love Status Icon | (768, 96) | 64x64 | Party-wide HUD pip, shape-coded not colour-coded |
| Shared-Stick Transfer Prompt | (832, 96) | 192x64 | "+2 to recipient." Bradley's entire arc, delivered as a neutral UI string. |

#### Cart, Fountain & Inspection:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gunter's Deep Dips Purchase Panel | (0, 160) | 256x128 | Eight-item menu with prices, HP restore and per-dip stack cost stated openly |
| Dip Interaction Prompt | (256, 160) | 128x64 | `DIP` — available whenever the party holds anything dippable |
| Re-Dip Confirmation | (256, 224) | 128x64 | A neutral confirm. Not a warning. It does not discourage. |
| Fountain Info Card | (384, 160) | 192x128 | Free. Public. No ticket. States all three facts and nothing else. |
| **HYGIËNESCORE UI Panel** | (576, 160) | 192x128 | Mirrors the physical plinth card; four states; readable without an inspect mode |
| Inspection Notice Panel | (768, 160) | 256x128 | Gerda's visit: forty minutes, rope up, the same finding as last quarter |
| Fine Economics Card | (768, 288) | 256x64 | 1,200 Sovs fine. Cleared before noon on a Saturday. Stated as a plain fact, sourced to the annual report. |

#### Photo, Alibi & Knowledge:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Photo Station Popup | (0, 288) | 192x96 | "Take Photo?" with station name and cost |
| Photo Op Station Table | (192, 288) | 256x96 | Eight stations with honest postability ratings (95% / 60% / 0% / 15% / 5% / 0% / 30% / 0%) |
| **Cultural Alibi Badge** | (448, 288) | 128x64 | Permanent, city-wide, granted on entering the Cacaogalerij. It is completely true. |
| "We went to a museum" Dialogue Chip | (448, 352) | 128x64 | Unlocked line, available with every NPC in every city, forever |
| Photo Album (Venus Temple Collection) | (0, 384) | 256x96 | Privacy-flagged interior sub-album |
| **Unflagged Fountain Album** | (256, 384) | 192x96 | Exterior plaza photos, freely shareable, and the ones the bros send to their mothers |
| Privacy Warning Panel | (448, 416) | 192x64 | Interior photos only. Names Mom (ICQ), Ingrid, Agent Havok explicitly. |
| Unexplainable Photo Item Card | (640, 384) | 128x64 | Key item, cannot be discarded, sourced from The Throne |
| Knowledge Unlock: Lennon | (768, 384) | 256x64 | "Did you know John Lennon drew erotic sketches?" |
| Lennon Reaction Split Bar | (768, 448) | 256x64 | 70% disbelief / 20% "I knew that" / 10% extremely interested, stacked bar with pattern fills and written percentages |
| Composure Meter | (640, 448) | 128x64 | Giggling Figure temporary state; recovers on the bench |
| Coin Purse / Peep Show UI | (0, 480) | 192x32 | 1 Sov units, thirty seconds each |
| Museum Ticket UI (9 Sovs) | (192, 480) | 128x32 | The sign says 5 Sovs. There is a sticker. |
| **Achievement Strip** | (320, 480) | 320x32 | Five 64x32 badges: Delen is Lief / Eén Keer Dopen / Ik Heb Niet Eens Gedoopt / Temple Tourist / Cultural Alibi |
| High-Contrast Interactive Marker | (640, 480) | 64x32 | Bold outline for the fountain, cart, exhibits and photo stations |
| Touch-Zone Guide Overlay | (704, 480) | 192x32 | Dev-only 44px minimum overlay, stripped at build |
| UI Reserve | (896, 480) | 128x32 | Reserved strip, do not paint |

### Technical Notes:
- **The Sharing the Love meter must read as a buff at Tiers 1-2 and never signal a trap.** No red, no warning icon, no ominous framing. The player earns it happily. The turn at Tier 3 should feel like a surprise the UI never hinted at, because the UI was telling the truth the whole time and the truth was "warm inside."
- The Attribution Table is a UI feature, not just writing: it is displayed, it is ranked, it updates, and the fountain is structurally excluded from it. If a designer later adds the fountain to this list, the joke is destroyed.
- The Fountain Info Card states three facts — free, public, no ticket — and does not state a fourth. Everything else the player needs is on the plinth card, at eye height, in the world.
- The HYGIËNESCORE UI panel and the physical plinth card share art so the world-state downgrade is legible from either surface
- The Fine Economics Card is sourced in-fiction to the museum's annual report, which is on a shelf in the gift shop for 8 Sovs and has sold four copies. Nothing is hidden. Nothing changes.
- Every dip prompt, cart menu row, photo station and coin option renders at 44px+ touch height

---

## 🎬 Animation Specifications

### De Grote Fontein Cascade (Sheets 2, 6, 8b) — HERO:
- **Duration:** 2.4-second seamless loop, six frames at 0.4s
- **Frames:** 6 (plus clogged and seized variants sharing the frame set)
- **Pattern:** Continuous, permanent, day and night except during the 11 PM-6 AM drain
- **Trigger:** Always on. There is no off state during trading hours.
- **Purpose:** The landmark. The queue. The business model. The reason the museum has a Museum Mile lease.
- **Audio Sync:** Continuous wet cascade bed with a low pump hum beneath it; recognisable two streets away and audible, attenuated, from the entrance hall and the Cacaogalerij
- **Performance Optimization:** **Never reduced below two frames on any LOD or accessibility setting.** Reduced-motion drops to the two-frame slow breathe. A static fountain reads as broken and broken is a different joke.

### The Dip Cycle (Sheets 6, 8b, 8c):
- **Duration:** 2.6 seconds (0.4s approach, 0.4s immerse, 0.4s coat, 0.4s lift, 0.6s drip, 0.4s clear)
- **Frames:** 6, plus four variants (re-dip, bare hand, bowl retrieval, cascade lean)
- **Pattern:** One-shot per dip. No cooldown. The fountain has never said no to anything.
- **Trigger:** `DIP` interaction with any dippable item
- **Purpose:** The germ mechanic's entire delivery vector. Engineered to be genuinely, unreasonably satisfying so the player repeats it voluntarily.
- **Audio Sync:** Immersion at 0.4s (the signature sound); tension break at 1.6s; three-second drip trail from 2.0s
- **Performance Optimization:** Reduced-motion uses frames 1 and 6 only — contact and result. Stack application and audio are unchanged.

### The Health Inspection (Sheets 2, 5, 8a, 8c):
- **Duration:** Forty in-game minutes, once per in-game quarter, four times per standard playthrough
- **Frames:** Rope set + sample + probe + write + depart, plus the HYGIËNESCORE card state swap on completion
- **Pattern:** Fixed calendar, not random. The player can be present or absent; the card downgrades either way.
- **Trigger:** In-game date
- **Purpose:** The world-state tell. Compliance is total, disclosure is complete, and the fountain never once stops.
- **Audio Sync:** Rope clip at set; a single clipboard-pen click on the finding; nothing else. Gerda works in silence.
- **Performance Optimization:** Crowd hold-back band caps at eight NPCs on Low LOD

### The Giggling Figure (Sheets 5, 6, 8b):
- **Duration:** 3.2 seconds (1.2s pre-activation click, 0.4s lift, 0.8s hold with giggle, 0.8s descent)
- **Frames:** 4 + mechanical click spark + pneumatic hiss puff
- **Pattern:** Every 30 seconds exactly, whenever anyone is within the sensor radius. No randomisation.
- **Trigger:** Motion sensor; unavoidable four steps inside the door
- **Purpose:** 100% jump-scare rate on first encounter, 80% photography rate on second. The relocation gave it a marble lobby and better acoustics.
- **Audio Sync:** Clicking at 0.0s (the tell); pneumatic hiss at 1.2s; recorded giggle at 1.6s; reset thunk at 3.2s
- **Performance Optimization:** Retains all four frames on every LOD. Reduced-motion holds at frame 1 with the giggle audio and glyph intact and the vignette suppressed.

### Marilyn Dress Timer (Sheets 5, 6):
- **Duration:** 2.4 seconds (0.4s grate, 0.6s rise, 0.8s billow, 0.6s settle)
- **Frames:** 4
- **Pattern:** Every 30 seconds on a timer, independent of player presence
- **Trigger:** Timer only
- **Purpose:** Everyone takes the same photograph. Everyone. Every time.
- **Audio Sync:** Grate whoosh at 0.4s
- **Performance Optimization:** Low LOD reduces to 2 frames; reduced-motion holds at rest with the station functional

### Peep Show Flip Cards (Sheets 5, 6, 8c):
- **Duration:** 30 seconds per 1 Sov viewing; 8-frame loop at 0.4s
- **Frames:** 8
- **Pattern:** Loops for the paid duration, then stops mid-cycle
- **Trigger:** Coin insertion
- **Purpose:** "People paid money for THIS? ...Put in another coin."
- **Audio Sync:** Coin clunk at 0.0s; mechanical flip per frame; wind-down at 30s
- **Performance Optimization:** Low LOD reduces to 4 frames at 0.8s; reduced-motion uses the static card with audio retained

### The Tempering Room Loop (Sheets 3, 6):
- **Duration:** 12-second loop, four frames at 3.0s
- **Frames:** 4 (pour, spread, gather, test)
- **Pattern:** Continuous background during trading hours
- **Trigger:** Ambient
- **Purpose:** The most technically impressive thing on Museum Mile, drawing a smaller crowd than the mannequin downstairs. Three minutes of observation grants Trivial Knowledge.
- **Audio Sync:** Marble scrape on spread; a single thermometer tap on test
- **Performance Optimization:** Low LOD holds at frame 1 (chocolatier at the slab, static)

### Cart Transaction Loop (Sheets 5, 6, 8a):
- **Duration:** 4.0 seconds, four frames at 1.0s
- **Frames:** 4 (load, hand over, take payment, next)
- **Pattern:** Continuous during trading hours, speed-scaled by time of day
- **Trigger:** Ambient; overridden by the player's own purchase
- **Purpose:** Six hundred sticks on a Saturday. She processes a stag party faster than it can be funny at her.
- **Audio Sync:** Skewer snap on load; card reader beep on payment
- **Performance Optimization:** Low LOD reduces to 2 frames

### Sharing the Love Tier Escalation (Sheets 8b, 8c):
- **Duration:** 1.6-second tier-up flourish; the aura itself is persistent
- **Frames:** Tier aura T1-T2 / T3 / T4 / T5, plus the stack gain popup
- **Pattern:** One-shot on tier change; aura persists until decay or cure
- **Trigger:** Crossing a stack threshold
- **Purpose:** Tiers 1-2 read as a buff and are a buff. The turn at Tier 3 is unannounced. The gurgle bed enters at Tier 2 and never fully leaves.
- **Audio Sync:** A warm chime at T1-T2; no chime at all at T3 (the absence is the tell); the gurgle bed rises at every tier
- **Performance Optimization:** Aura renders as a single overlay quad on Low LOD

### Neon Venus Flicker (Sheets 5, 8b):
- **Duration:** 0.2-second dip roughly every 6 seconds
- **Frames:** 2
- **Pattern:** Continuous, exterior only, has been like this since 1985 and survived the move
- **Trigger:** Constant
- **Purpose:** Never repaired, on two buildings now
- **Audio Sync:** Faint neon buzz
- **Performance Optimization:** Static plate on Low LOD; disabled in reduced-motion

### The John Lennon Discovery (Sheets 5, 7, 8c):
- **Duration:** 2.8 seconds (0.6s examine, 0.6s pause, 1.6s unlock panel)
- **Frames:** Lennon display examine + Ruud's "Yes, really." frame + unlock panel
- **Pattern:** One-shot per save file
- **Trigger:** Examining the display
- **Purpose:** The one genuinely surprising fact in the building, and the game is not lying about it
- **Audio Sync:** A single clean chime at 1.2s, distinct from every other sound in the museum
- **Performance Optimization:** None needed (one-shot)

### Mirror Maze Traversal (Sheets 4, 8b):
- **Duration:** ~10 seconds of traversal with continuous reflection ghosting
- **Frames:** Reflection ghost layer + maze fog + UV wash
- **Pattern:** Continuous while inside the passage
- **Trigger:** Entering the maze
- **Purpose:** Short. Disorienting. You will find your way out. Eventually.
- **Audio Sync:** Footsteps gain a slight reverb tail
- **Performance Optimization:** Reflection ghosts cap at two instances on Low LOD; static fog in reduced-motion

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fountain High-Contrast Silhouette | Sheet 6 (1792, 768) | 256x256 | Bold outline of the location's defining object |
| Giggling Figure High-Contrast Silhouette | Sheet 6 (1280, 864) | 128x160 | Bold outline of the retained key interactive |
| Anke / Ruud / Lotte High-Contrast Silhouettes | Sheet 7 (0/64/128, 416) | 64x96 each | All three interior staff |
| Gunter / Gerda High-Contrast Silhouettes | Sheet 8a (0/64, 320) | 64x96 each | Both plaza NPCs |
| Fountain High-Contrast Marker | Sheet 8b (448, 320) | 64x64 | Bold outline pip for the plaza's key interactive |
| High-Contrast Interactive Marker | Sheet 8c (640, 480) | 64x32 | Fountain, cart, exhibits and photo stations |
| Motion Sensor Trigger Zone | Sheet 6 (1280, 768) | 96x96 | Visualises the Giggling Figure's detection radius when interaction zones are enabled |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| **Slow Cascade Plate** | Sheet 8b (0, 320) | 128x128 | Two-frame breathe. The fountain is the one animation that is never fully stopped, on any setting, because a still fountain reads as a fault. |
| Static Dip | Sheet 6 (896, 864) | 128x128 | Frames 1 and 6 only; stack application and audio unchanged |
| Static Giggling Figure | Sheet 6 (1408, 864) | 128x160 | Holds at frame 1; giggle audio and glyph retained; vignette suppressed |
| Static Marilyn | Sheet 6 (1152, 864) | 128x160 | Holds at rest; the photo station remains fully functional |
| Peep Show Static Card | Sheet 6 (1024, 864) | 128x64 | Single-frame substitute with audio retained |
| No-Flash Plate | Sheet 8b (128, 320) | 64x64 | Photography without the burst; ambient NPC flashes suppressed |
| Static Fog | Sheet 8b (192, 320) | 64x64 | Motionless maze atmosphere; reflection ghosts held still |
| Static Neon | Sheet 8b (256, 320) | 64x64 | Steady exterior Venus outline |
| Static Steam | Sheet 8b (320, 320) | 64x64 | Held cocoa steam off the cascade |
| Static Gurgle Marker | Sheet 8b (384, 320) | 64x64 | Non-animated Sharing the Love tier indicator |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Dip Glyph | Sheet 8b (0, 256) | 32x32 | Mirrors the signature immersion sound — the most-fired glyph in the location |
| Drip Glyph | Sheet 8b (32, 256) | 32x32 | Mirrors the three-second post-lift trail |
| Cascade Glyph | Sheet 8b (64, 256) | 32x32 | Mirrors the continuous flow; persistent, low-frequency |
| Pump Hum Glyph | Sheet 8b (96, 256) | 32x32 | Mirrors the low hum beneath the cascade |
| Mechanical Click Glyph | Sheet 8b (128, 256) | 32x32 | Mirrors the pre-activation clicking — the anticipation cue |
| Giggle Glyph | Sheet 8b (160, 256) | 32x32 | Mirrors the recorded giggle |
| Pneumatic Hiss Glyph | Sheet 8b (192, 256) | 32x32 | Mirrors the mechanism venting |
| Camera Shutter Glyph | Sheet 8b (224, 256) | 32x32 | Mirrors constant tourist photography |
| Coin Clunk Glyph | Sheet 8b (256, 256) | 32x32 | Mirrors coin insertion |
| Flip Card Glyph | Sheet 8b (288, 256) | 32x32 | Mirrors the mutoscope card flipping |
| Marilyn Whoosh Glyph | Sheet 8b (320, 256) | 32x32 | Mirrors the dress mechanism |
| Music Box Glyph | Sheet 8b (352, 256) | 32x32 | Mirrors the mechanical wing music box |
| Stair Creak Glyph | Sheet 8b (384, 256) | 32x32 | Mirrors the old wooden stairs |
| Skewer Snap Glyph | Sheet 8b (416, 256) | 32x32 | Mirrors the cart transaction rhythm |
| Gurgle Glyph | Sheet 8b (448, 256) | 32x32 | Mirrors the Tier 2+ ambient stomach bed that no character ever mentions |
| "One Dip" Glyph | Sheet 8b (480, 256) | 32x32 | Mirrors Ruud's endless plaza line |
| Lennon Chime Glyph | Sheet 8c (768, 384) | 256x64 | The knowledge unlock panel doubles as the visual mirror for its distinct chime |

### Colorblind Considerations:
- The HYGIËNESCORE card communicates by **letter and date text**, never by colour. The A / B / C / IN BEHANDELING states are legible in greyscale at gameplay zoom.
- The Sharing the Love meter uses segment count plus a written tier name, never a green-to-red gradient. Tier auras are distinguished by pattern and density, not hue.
- Photo station postability is shown as explicit percentage text
- The Lennon reaction split is a stacked bar with pattern fills and written percentages
- The four fountain states are distinguishable by flow geometry and silhouette, not by colour — clogged sheets sideways, seized slumps, serviced has an open hatch and a trolley, drained has no chocolate at all
- Status effects use distinct silhouettes: wave (Sharing the Love), zigzag (Embarrassed), small-frame (Vintage Knowledge), book-with-question-mark (Trivial Knowledge), steady-line (Composure), stamped-card (Cultural Alibi)
- Privacy-flagged photos carry a shape-coded corner marker; unflagged fountain photos carry none
- Exhibits are identified by silhouette and placard text; the Cacaogalerij and the Mechanische Vleugel are distinguishable by ceiling height, plinth style and fixture density as well as by lighting grade
- Touch zones minimum 44px for the fountain dip, cart menu, coin insertions, exhibit examines and all photo stations

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) all four HYGIËNESCORE cards, all four ONE DIP signs, the cart price board, the cart hygiene card, exhibit placards, the framed violation notice, the art deco sign, the Cacaogalerij three-language placards, the Lennon label and all portraits kept uncompressed
- **Fallback:** PNG high quality for the plaza sheet, the fountain sheet and both interior sheets (the chocolate specular, the red wash and the mirror maze UV all band badly under lossy compression)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| venustempel_fountain | venustempel_fountain | 2048x1024 |
| venustempel_exhibits | venustempel_exhibits | 2048x1024 |
| venustempel_mechanisms | venustempel_animated_objects | 2048x1024 |
| venustempel_characters | npc_venustempel_staff, npc_venustempel_plaza | 1024x1024 |
| venustempel_fx_ui | venustempel_effects, venustempel_ui | 2048x512 |

*(The plaza sheet and the two interior sheets load and unload as streamed room units — only one is resident in normal play. The fountain sheet is resident whenever the plaza is resident. Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full 6-frame cascade, full 6-frame dip cycle with all four variants, 4-frame Giggling Figure and Marilyn, 8-frame flip cards, 4-frame tempering and cart loops, ambient flash bursts, neon flicker, cocoa steam, chocolate spatter accumulation, mirror reflection ghosts, dust motes, full crowd density |
| Medium | Cascade at 4 frames, dip variants share the base cycle, Marilyn at 2 frames, flip cards at 4 frames, tempering at 2 frames, flash bursts capped at two, reflection ghosts capped at two, crowd density −40% |
| Low | **Cascade holds at 4 frames — never lower.** Dip reduces to 3 frames, Giggling Figure retains all 4 as the interior's core beat, Marilyn holds 2, flip cards hold 1, tempering and cart loops hold at frame 1; reduced flash effects; static mannequins elsewhere; no dust motes; no spatter accumulation; crowd density −70%; inspection hold-back band caps at 8 NPCs |

### Performance Targets:
- **Target FPS:** 60 (per location performance budget)
- **Max Draw Calls:** 16 per frame
- **Memory Footprint:** 42 MB maximum (raised from the pre-relocation 38 MB to accommodate the plaza and the fountain hero sheet)
- **Particle Limit:** 18 (chocolate drip, spatter, cocoa steam, bowl ripple, dust motes, mirror fog, pneumatic puff, flash motes)

### Performance Notes:
- Streamed room units keep typical resident footprint at ~26.2 MB (plaza + fountain, or one interior sheet, plus all atlases); theoretical all-resident worst case is ~38.4 MB, inside the 42 MB budget
- The cascade is the one animation never degraded below four frames on any LOD — it is the location's entire identity and the reason the location exists
- Bachelor Party, Family, School Group and Bros Trio all render as pre-composed single blocks to protect the 16-draw-call budget
- The two crowd depth bands (cart queue, fountain queue) are single-quad silhouette strips, never individual NPCs
- Chocolate spatter accumulation writes to a single paving decal layer, capped, and is cleared by the night crew state rather than accumulating across sessions
- Mirror reflection ghosts are static silhouette sprites at 40% alpha, never real-time renders
- Ambient camera flashes are hard-capped at three simultaneous instances and pooled

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (plaza, room backgrounds, exhibits, fixtures, signage), AnimatedSprite2D (cascade, dip cycle, Giggling Figure, Marilyn, flip cards, tempering room, cart transactions, neon, staff), CPUParticles2D (chocolate drip, spatter, cocoa steam, dust motes, mirror fog, pneumatic puff — not GPU), CanvasLayer (Sharing the Love HUD, attribution table, photo UI, album, hygiene panel, coin prompts, knowledge unlock), Area2D (fountain dip zone, collection bowls, cart counter, Giggling Figure sensor radius, each mutoscope, all eight photo stations, De Oervorm no-flash zone, tempering room observation zone, Lennon display, maze entrance, gift shop counter, toilet door), Timer (30-second mechanism scheduler, 40-minute inspection window, in-game-day stack decay)
- Special systems: **Sharing the Love** five-tier stacking status with seven distinct gain sources and four cure sources, persisting across locations and decaying per in-game day; the structurally-excluded attribution table; Tier 4 navigation override flagging Febo Automat and Voetgangerstunnel; Tier 5 Shamsterdam Stomach day-long debuff with a Tolerance Hostel rest event hook; quarterly inspection calendar driving a four-state HYGIËNESCORE world flag and a four-state ONE DIP sign flag; cumulative-dipping-driven fountain condition state machine (flowing / clogged / seized / serviced) with service-cycle reversion; 11 PM-6 AM drained night state with night-crew ambient; Gunter's Deep Dips eight-item cart economy; **Cultural Alibi** permanent world flag with a city-wide dialogue unlock; 30-second hard-timer scheduler shared by the Giggling Figure and Marilyn; first-encounter jump-scare flag with vignette suppression; anticipation-tell activation; coin economy with per-viewing 30-second timers; eight-station photo system writing to a split album (flagged interior / unflagged fountain); Unexplainable Photo key-item grant; NPC-exclusion enforcement on interior album viewing; John Lennon knowledge flag with a 70/20/10 weighted reaction table; Composure temporary state with bench recovery; time-of-day clientele mix selector

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Cascade loop | Continuous wet cascade bed + low pump hum | Persistent; audible attenuated from the entrance hall and gallery |
| Dip frame 2 (Immerse) | The signature immersion sound | 0.4s of dip cycle |
| Dip frame 4 (Lift) | Chocolate tension break | 1.6s |
| Dip frame 5 (Drip) | Three-second trailing drip (bare-hand variant is distinct and worse) | 2.0s |
| Cart transaction | Skewer snap, then card reader beep | 0.0s / 3.0s |
| Sharing the Love T1-T2 | Warm chime | On tier-up |
| Sharing the Love T3 | **No chime.** The absence is the tell. | On tier-up |
| Sharing the Love T2+ | Ambient stomach gurgle bed enters and never fully leaves; rises per tier | Persistent |
| Mechanical click spark | Pre-activation clicking (the tell) | 0.0s of Giggling Figure cycle |
| Pneumatic hiss puff | Air release | 1.2s |
| Giggling Figure frame 3 | Recorded giggle + musical jump-scare hit | 1.6s |
| Post-jump recovery | Total silence | 2.4-3.2s |
| Mechanism reset | Reset thunk | 3.2s |
| Marilyn grate activation | Dress whoosh | 0.4s of Marilyn cycle |
| Coin insertion | Coin clunk | 0.0s of peep show viewing |
| Flip card frames | Mechanical flip, per frame | Every 0.4s for 30s |
| Tempering room spread | Marble scrape | Per loop |
| Tempering room test | Single thermometer tap | Per loop |
| Photo station capture | Shutter, then an unearned triumphant sting | 0.8s / 2.0s |
| Fountain photo capture | Shutter, then the full triumphant sting — this is the photograph of the trip and they know it | 0.8s |
| Lennon display examine | A single clean chime, unique in the building | 1.2s of discovery |
| Ruud, plaza rotation | "One dip." on an endless distant loop | Continuous, attenuated |
| Gerda's inspection | Rope clip, then a single clipboard-pen click on the finding, then nothing | On set / on write |
| Mechanical wing ambience | Victorian music box loop | Continuous |
| Stairs | Wooden creak | Per step |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Fountain (free, unmissable) | Cascade, dip cycle, plaza, ONE DIP sign, HYGIËNESCORE card | Public space, no ticket, available from first arrival in Shamsterdam. The first dip is the on-ramp to everything else. |
| Sharing the Love | Stack meter, tier plates, gain popup, tier auras, gurgle visualiser, cure item row | Seven gain sources, four cures, five tiers, persists city-wide and decays one stack per in-game day |
| The Attribution Table | Attribution table panel, bro portraits | Eight ranked blame entries fire at Tiers 3-5. The fountain is structurally excluded and must remain so. |
| Shamsterdam Stomach | Tier 5 banner, T5 aura, facilities marker | Max HP −40% for the in-game day, Bravado gains halved, Tolerance Hostel bathroom-queue event on next rest |
| Gunter's Deep Dips | Cart, seven wares, **the menu board and the warning sign as hero readable-text assets**, Gunter's full frame set, purchase panel | Seven-item economy: five board items at 5 SOVS, plus the off-board 1 SOV bare skewer (highest margin on the cart, sells constantly) and the off-board 1 SOV hand wipe (offered every transaction, almost never bought). The warning sign forbids the double-dip that the entire mechanic runs on. |
| The Health Inspection | Gerda's frame set, rope overlay, four HYGIËNESCORE cards, four ONE DIP signs, inspection panel, fine economics card | Quarterly, fixed calendar, four visits per playthrough, visible world-state downgrade, fountain never stops |
| The Cultural Alibi | Alibi badge, dialogue chip, Cacaogalerij placards | Granted on paying 9 Sovs and entering the chocolate wing. Permanent, city-wide, and completely true. |
| The Giggling Figure Encounter | Figure cycle, jump-scare vignette, Composure meter, bench | Unavoidable four steps inside the door; first encounter costs Composure, second becomes a photo opportunity |
| Photo Consequences System | Eight station panels, split album, privacy warning, sensitive flags | Interior photos flagged; fountain exteriors unflagged and sent to Mom |
| The "Unexplainable Photo" | The Throne, station popup, item card | Key item, cannot be discarded |
| John Lennon Knowledge Unlock | Lennon display, Ruud's "Yes, really." frame, unlock panel, reaction split bar | Permanent dialogue option with a 70/20/10 split |
| Peep Show Devices | Mutoscopes, coin UI, 8-frame flip cards | 1 Sov per 30-second viewing; grants Vintage Knowledge |
| Achievements | Achievement strip | Delen is Lief (T5) / Eén Keer Dopen (leave the city having dipped exactly once) / Ik Heb Niet Eens Gedoopt (Bradley at T3 with zero voluntary dips) / Temple Tourist / Cultural Alibi |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Awkward Truffle | No shared sprites; Sophie's tempering critique is dialogue only | Direct commercial rival. Sophie is the only NPC who criticises the fountain, and does it on tempering grounds, never hygiene. Same-day purchase from both unlocks a comparison dialogue. |
| **Shamsterdam Museum of Questionable Art** | **No shared sprites — the rivalry is tonal and dialogue-only.** Unlicensed fountain merch on their shelves is authored as a distinct low-quality knock-off prop, never a reuse of Venustempel art. | **The two locations are opposite ends of the same industry and must read that way to a player who visits both.** Questionable Art is the cheap gift shop: mass-produced novelty, sprinkles, fondant bow ties, 3.50 Sovs collector's eggs, a bored teenager on the till, no queue. Venustempel is the curated institution: artisan pieces with provenance, gallery-grade plinths and lighting, three-language placards, climate control, trained staff, a restrained and expensive shop, and a queue that runs down the Mile. **Every visual axis must separate them** — price point, signage quality, plinth and case construction, lighting discipline, staff bearing, crowd density. Venustempel's disdain is one-directional and is expressed in a single dry line, never a rant. Do not edit the Questionable Art sheets; their chocolate material is load-bearing for the Fabergé Egg Hunt. |
| Condomerie Het Gulden Vlies | Shared hygiene-product UI language; no shared sprites | Adjacent trade, different district since the 2011 move. Femke and Lotte have professional awareness and no relationship. |
| The Hemp Museum | Cultural Alibi badge, shared museum-ticket UI style | "We've been to TWO museums" — with decreasing conviction. Venustempel grants the flag; the Hemp Museum is the second stamp. |
| The Tolerance Hostel | Album privacy flag; Sharing the Love decay on rest; Tier 5 bathroom-queue event | Interior photos cannot be shown to Ingrid; fountain exteriors can. A full night removes 2 stacks. Tier 5 fires the dorm bathroom queue. |
| Febo Automat | Tier 4 facilities marker; croquette cure item | Urgent-navigation node. The croquette removes a stack for reasons that are mechanically real and medically nonsense. The bros swear by it. |
| Voetgangerstunnel | Tier 4 facilities marker | Urgent-navigation node. Henk gives unhelpfully accurate directions to a toilet. |
| Café de Schaamte | Album entries, Composure status, Cultural Alibi chip | Bros attempt to describe the museum to Agent Havok, fail, describe the fountain instead, succeed far too well |
| Casa Rosé | No longer a shared corridor since the relocation | Staff line updated: "The Temple? They moved. They do chocolate now. Yes. I don't know either." |
| ICQ / Mom (system) | Unflagged fountain album | Mom receives a photograph of a four-metre chocolate phallus. She has noticed. She does not raise it. |
| Agent Havok (character system) | Privacy warning exclusion list | Interior photos are a hard exclusion; professional relationship |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A genuinely good museum with a genuinely absurd collection, fronted by a landmark that four hundred strangers a day put their hands in, run by people who have disclosed all of it and been ignored"
- **Color Mood:** Couverture brown and tempered gloss under civic stone and municipal green outside; cold gallery grey-white on the ground floor; Venus red and velvet purple under salvaged pink neon upstairs. The plaza is warm, wet and public; the Cacaogalerij is cold, dry and serious; the Mechanische Vleugel is red, cramped and forty years old.
- **Lighting:** Open daylight and wet specular on the plaza; correct gallery spots at 17°C below; red and pink wash with deliberately dim corners above; constant tourist flash on the second floor; the HYGIËNESCORE card lit from below at all hours because it is a municipal fitting
- **Texture:** Food-grade stainless with sanitary welds and a Rotterdam manufacturer's plate, warm couverture with real weight, gallery glass and nitrogen seals, municipal lamination, green-and-white cart paint kept spotless, brass mutoscope bodies worn smooth, red velvet, Victorian paper, 1985 moulded plastic, marble lobby, chocolate-spattered civic paving

### Environmental Storytelling:
- The fountain is free and the sticks are not, and the composition of the plaza — cart queue feeding fountain queue feeding ticket queue — says so without a word of dialogue
- Gunter's straight-A hygiene card and the fountain's descending municipal score sit four metres apart, at the same height, on the same municipal template
- The ONE DIP sign has been replaced four times, each time larger, and is currently the size of a road sign
- The framed hygiene violation hangs beside the 1985 opening photograph at identical size, and no visitor NPC ever stops at it
- The salvaged art deco lettering is mounted two degrees crooked on a building that predates art deco by sixty years, and nobody has commented
- The banner has said "Nu Geopend" since 2011
- The Giggling Figure came with the contents, not the building, and its bolt flange is visible on the marble
- The bench came from Roodelicht Row, is the same bench, and is visibly the most-used object in the entrance hall
- The Failures Case is the curator's favourite and nobody stops at it
- The gift shop is ninety square metres, which is more than it needs, and Lotte is delighted
- The Handreiniger bottles are faced forward on the counter every morning and the stack never goes down

### Character Integration Notes:
- Gunter's competence is visible in props before it is visible in dialogue: gloves, tongs in sanitiser, the A card, the half-empty glove box. He is four metres from the fountain and he has never eaten from it.
- Ruud is the only staff member who visibly frays, and only on plaza rotation. His "One dip." frame is the most-used sprite in the location; author it to survive nine hundred repetitions a day.
- Anke's total immunity is the interior's anchor; her expression range is the narrowest in the building
- Lotte's cheerfulness is completely sincere; she is not in on a joke, and her pride in the floor space must not read as ironic
- Gerda is correct, thorough and entirely unbothered. Not an antagonist, not an obstacle. She has told them. They have listened. Nothing has changed. She has forty other premises this week.
- **No staff or vendor frame in this document may express disapproval, judgement, discomfort, or complicity.** They are competent professionals having an ordinary working day, and the bros are the punchline.
- The Family With Small Children at the fountain is the funniest composition in the location and it is played completely straight

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Plaza at Peak** — the cascade at full flow, the cart queue feeding the fountain queue, the ONE DIP sign at actual road-sign scale, and the crowd ignoring it
1b. **The Board and the Sign** — Gunter's menu board and the patron warning sign side by side, both fully legible, with a customer double-dipping in the same frame
2. **The Two Cards** — Gunter's straight-A hygiene card and the fountain's IN BEHANDELING card in one frame, four metres apart, same municipal template
3. **The Attribution Table** — eight ranked blame entries with the fountain conspicuously absent
4. **Gerda's Forty Minutes** — a woman in municipal hi-vis roping off a four-metre chocolate phallus while a crowd waits patiently for her to finish
5. **The Family** — two parents and three small children dipping marshmallows, entirely unbothered, none of them going inside
6. **De Oervorm** — the 1974 piece, cracked, in a nitrogen case with a live humidity readout, rendered with complete reverence
7. **The Framed Violation** — hanging beside the 1985 opening photograph at identical size

### Quote Potential:
- "Get them while they're hot and heavy- 5 SOVS"
- "Firm, rigid, and heavily textured for maximum friction against the flow."
- "Just the tips. Yes, it's redundant. No, we don't judge."
- "...and absolutely NO open-mouth catching directly from the tip of the statue. We've had incidents."
- *(customer reads the whole board aloud, laughing)* — **"Five SOVS."**
- "My cart is clean. What happens at the fountain is between you and the fountain."
- "No." *beat* "I have seen the fountain."
- "There is a sign. It is very large. Next, please."
- "One dip. One dip, please. Sir. One dip."
- "Please do not put your face in the fountain. Please. Sir. Please."
- "The fountain is free. The fountain has always been free. You do not need a ticket for the fountain and I cannot sell you one."
- "Nine Sovs. The sign says five. The sign is old. Cash or card."
- "It is real. It is warm. It is free. That is the fountain's whole personality."
- "Handreiniger? Four Sovs, and the bottle is the fountain. It's a nice little bottle. Nobody ever takes one."
- "Ninety square metres. On Roodelicht it was forty-one. Forty-one, and a corridor."
- "Same finding as March." / "You have a bigger sign now."
- "It is a shared food surface in a public square with no supervision. That is what I have written. It is on the plinth. Good afternoon."
- "I DIDN'T EVEN DIP."
- "We went to a museum today."

---

## 📋 Required PNG Files (9 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | venustempel_plaza.png | 2048x1024 |
| 2 | venustempel_fountain.png | 2048x1024 |
| 3 | venustempel_interior_a.png | 2048x1024 |
| 4 | venustempel_interior_b.png | 2048x1024 |
| 5 | venustempel_exhibits.png | 2048x1024 |
| 6 | venustempel_animated_objects.png | 2048x1024 |
| 7 | npc_venustempel_staff.png | 512x512 |
| 8 | npc_venustempel_plaza.png | 512x512 |
| 9 | venustempel_effects.png | 512x512 |
| 10 | venustempel_ui.png | 1024x512 |

*(Ten files across nine specification sheets — Sheet 8 covers three files: plaza NPCs, effects and UI.)*

**Total Estimated Memory:** ~26.2 MB typical resident (plaza + fountain, or one interior sheet, plus all atlases); ~38.4 MB theoretical all-resident worst case. Within the 42 MB location budget.

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `venustempel_plaza.png` (2048x1024)
- [ ] `venustempel_fountain.png` (2048x1024)
- [ ] `venustempel_interior_a.png` (2048x1024)
- [ ] `venustempel_interior_b.png` (2048x1024)
- [ ] `venustempel_exhibits.png` (2048x1024)
- [ ] `venustempel_animated_objects.png` (2048x1024)
- [ ] `npc_venustempel_staff.png` (512x512)
- [ ] `npc_venustempel_plaza.png` (512x512)
- [ ] `venustempel_effects.png` (512x512)
- [ ] `venustempel_ui.png` (1024x512)

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
- **Documentation:** Cascade loop timing reference (six-frame seamless), dip cycle timing reference with all four variants, 30-second mechanism scheduler diagram, the four-state HYGIËNESCORE and four-size ONE DIP progression sheets, the fountain condition state machine diagram, the eight-station photo postability table, and a content-handling sign-off confirming no explicit depiction in any delivered asset

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (#DC143C, #800080, #FFF8DC, #FF69B4, #B08D57, #3B1F0B, #6B4226, #2E6B4F, #E8ECEF, #9C9184)
- [ ] **The cascade is the hero and reads as one:** warm, heavy, wet, with real weight and mobile specular. Chocolate that reads cold, matte or water-like is a reject.
- [ ] The fountain silhouettes identically at 64px across all four operational states so the landmark reads at map scale in any condition
- [ ] Key gags read clearly: the ONE DIP sign at road-sign scale, Gunter's A card and the plinth's downgraded card in one frame at the same height, the framed violation beside the 1985 photograph at identical size, the "VERVOLG →" placard as the only transition between the two collections, the crooked art deco lettering, the family at the fountain, the Giggling Figure at rest looking completely harmless, no bypass route around the gift shop
- [ ] **De Oervorm and the Failures Case contain no joke whatsoever** — the 1974 piece is rendered with reverence in a nitrogen case with a live readout, and the Failures Case placard is genuinely sad. The surrounding sincerity is what makes the plaza funny.
- [ ] The Cacaogalerij reads as a real gallery: correct plinth heights, gallery-grade lighting, honest climate control, three-language placard typography. If it reads as a novelty shop the sheet is a reject.
- [ ] All four HYGIËNESCORE states and all four ONE DIP sizes are legible at gameplay zoom on a 5-inch display without an inspect mode
- [ ] **Gunter's menu board and the patron warning sign are set verbatim from the author copy, in full, with no paraphrase, abbreviation, reformatting or sanitisation** — and both are legible from standing distance at gameplay zoom on a 5-inch display
- [ ] The board reads as hand-lettered and cheerful; the warning sign reads as municipal, formal and sincere. Different typography, different stock. Neither sign winks — no cartoon eyes, no nudge iconography, no visual puns.
- [ ] The warning sign and a double-dipping visitor are visible in the same frame
- [ ] **Venustempel reads as the curated institution and not as the Museum of Questionable Art** — gallery-grade plinths, lighting discipline, three-language placards, climate control, trained staff bearing, a restrained expensive gift shop, and a queue. A player who visits both must be able to tell them apart on price point and signage quality alone.
- [ ] Content handling verified: no delivered asset depicts explicit content. Every exhibit is confectionery, machinery, a mannequin, a framed artefact, signage, municipal paperwork, food-service equipment, or a visitor reaction. The collection is rendered plainly and at scale, without euphemism and without leering.
- [ ] Peep show flip cards are period-accurate Victorian silhouettes and tame by any modern standard
- [ ] Gunter's competence props are present and legible: gloves, tongs in sanitiser, half-empty glove box, straight-A card, sanitiser tub
- [ ] Accessibility visual alternatives included for all sixteen audio cues (dip, drip, cascade, pump, click, giggle, hiss, shutter, coin, flip, whoosh, music box, stair creak, skewer snap, gurgle, "one dip")
- [ ] The cascade never fully stops on any accessibility setting — reduced motion delivers the two-frame slow breathe, not a still
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets — targets are the bros treating a working city as a theme park, and the commercialized tourism machine; never human sexuality, sex work, sex education, or the staff
- [ ] Staff and vendors read as competent, unbothered professionals doing an ordinary job; no frame expresses disapproval, judgement, discomfort or complicity
- [ ] Gerda reads as correct and procedural, never as an antagonist or an obstacle
- [ ] The Sharing the Love UI reads as a **buff** at Tiers 1-2 with no warning framing, no red, and no ominous iconography
- [ ] The Attribution Table renders all eight entries and structurally excludes the fountain
- [ ] Hidden areas/interactions have discoverable visual cues (Lennon display highlight, the bench, the anticipation tell, the maze entrance, the Failures Case, the framed violation, the manufacturer's plate)
- [ ] Performance optimized (streamed room units, CPU particles, atlas limits respected, crowd depth bands as single quads, spatter on a capped decal layer, cascade floor of four frames honoured)
- [ ] Touch zone sizing considered (44px minimum for the dip, cart menu, coin slots, exhibit examines and photo stations)
- [ ] Colorblind-friendly alternatives available where color codes meaning (letter/date text on hygiene cards, segmented and named Sharing the Love tiers, percentage text on postability, pattern-filled reaction split, flow-geometry-distinguished fountain states, shape-coded album markers)
- [ ] Social media viral potential maximized in composition choices (plaza at peak, the two cards in one frame, the attribution table, Gerda's forty minutes, the family, De Oervorm, the framed violation)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam Museum Mile; `shamsterdam_museumrow_venustempel_01`; the retired Roodelicht ID has no assets authored against it; the museum's own signage claims "World's First Since 1985" without naming a real city |
| Cultural Specificity | ✅ | Dutch disclosure culture (everything signposted, nothing hidden, compliance total and consequence-free), municipal hygiene regime and its paperwork, Museum Mile as a district built around the appearance of culture, Victorian mutoscope history, Belgian/Swiss/French/Dutch/Italian tempering traditions |
| Satirical Targets Appropriate | ✅ | The bros treating a working city as a theme park; the commercialized tourism machine that sells them exactly what they want, competently, while finding them tedious. Never human sexuality, sex work, sex education, or the staff. |
| Seedy Underbelly Present | ✅ | Free chocolate as a customer-acquisition funnel returning eleven times its 90,000 Sovs annual running cost; the 1 SOV bare skewer as the cart's highest-margin product; a 10 Sovs green screen composite of a cascade you can stand in front of for free, outselling every other photo product; a 1,200 Sovs fine cleared before noon on a Saturday |
| Gameplay Value Established | ✅ | Sharing the Love five-tier stacking status with seven gain sources and four cures persisting city-wide; the structurally-excluded attribution table; Tier 4 navigation override and Tier 5 day-long debuff; the eight-item cart economy; quarterly inspection world state with a four-stage score downgrade and a four-stage sign escalation; the Cultural Alibi permanent flag; retained Giggling Figure encounter, mutoscope economy, eight photo stations and the Lennon unlock |
| Technical Feasibility | ✅ | Streamed room units, cascade floor of four frames on Low LOD, crowd depth bands as single quads, capped spatter decal layer, pooled flash instances, pre-composed group blocks, CPU particles throughout |
| Performance Budget | ✅ | 60 FPS, 16 draw calls, 42 MB (raised from 38 MB for the plaza and hero fountain), 18 particles; ~26.2 MB typical resident, ~38.4 MB worst case |
| Accessibility Features | ✅ | Visual mirrors for all sixteen audio cues including the dip and the gurgle bed; a reduced-motion set that preserves every comedy beat (the cascade breathes, the dip still lands, the giggle still fires); letter/date-coded hygiene states; segmented and named status tiers; 44px touch zones |
| No Crypto Elements | ✅ | The only currencies are Sovs, 1 Sov coins for machines built in the 1890s, and germs |
| Content Handled Appropriately | ✅ | No asset in this specification depicts explicit content. Every exhibit is confectionery, machinery, a mannequin, a framed artefact, signage, municipal paperwork, food-service equipment, or a visitor reaction. The collection and the fountain are rendered plainly and at full scale, without euphemism and without leering; the register is gleeful MA-rated excess played dead straight by the institution, with escalating physical consequences landing on the bros - never anticlimax, never administrative deflation. |
| Social Media Integration | ✅ | 7 screenshot moments + 14 quotable lines identified |

**Once these assets ship, Venustempel becomes the game's most completely honest tourist trap: nine Sovs to see a cracked 1974 chocolate phallus in a nitrogen case, one Sov for a stick with nothing on it, and nothing at all for the fountain — which is free, which is warm, which is four metres tall, which is under a road-sign-sized notice asking for one dip, and which four hundred strangers a day have already touched.**
