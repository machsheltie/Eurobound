# Torte Royale - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for Torte Royale — a mobile premium cake cart (in-world brand: "Der Zuckerschock — Konditormeister seit 1847") that rotates through four Sinfonia locations daily, selling genuinely excellent Viennese pastries behind a velvet rope, a Gothic-script menu, and a pronunciation test administered by Frau Tortenmeister, a vendor whose default expression is judgment. The location satirizes food-tourism authenticity gatekeeping: the cakes are perfect; the experience of buying them is engineered to make you feel unworthy of them.

**Location ID:** `sinfonia_kaffeehausrow_torte_royale_01`
**Theme:** Imperial pretension on wheels — cultural gatekeeping as a retail model, pronunciation as currency
**Zone:** Kaffeehaus Row, Intellectual Café District (mobile — rotates positions daily)
**Hours:** 10:00–20:00 (cake has standards)
**Primary Function:** Mobile shop / pronunciation mini-game / location-hunt mechanic — premium consumables, Charm-based pricing, Sugar High buff economy, Cake Connoisseur progression

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Chocolate Brown | #3D1C02 | Cart body, menu board, chocolate everything |
| Apricot Glaze | #FFDAB9 | Cake glazes, warm highlights, awning stripes |
| Cream | #FFFDD0 | Backdrops, doilies, porcelain, awning base |
| Judgmental White | #FFFFFF | Frau Tortenmeister's konditor uniform, spotlights |
| Imperial Gold | #CFB53B | Eagle motifs, gold leaf trim, chandelier, calligraphy |
| Brass Plate | #B5A642 | Review plates, register, stanchions, wheel spokes |
| Gothic Ink | #1A1A1A | Menu script, pince-nez, price calligraphy outlines |
| Velvet Burgundy | #5C0A14 | Velvet rope, display case backing, imperial accents |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/torte_royale/
├── environment/
│   ├── torte_royale_cart.png
│   └── torte_royale_backdrops.png
├── npcs/
│   ├── frau_tortenmeister.png
│   └── torte_royale_queue_npcs.png
├── objects/
│   └── torte_royale_display_case.png
└── effects/
    └── torte_royale_effects_ui.png
```

---

## 🛒 Sprite Sheet 1: The Cart (Der Zuckerschock)
**File:** `torte_royale_cart.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #3D1C02 (Chocolate Brown), #CFB53B (Imperial Gold), #B5A642 (Brass), #5C0A14 (Velvet Burgundy)

### Cart Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cart Full Body | (0, 0) | 256x224 | Ornate wheeled cart, more elaborate than most restaurants — carved wood, gilded moldings, museum energy |
| Imperial Eagle Crest Left | (256, 0) | 48x48 | Gold double-headed eagle motif, cart flank |
| Imperial Eagle Crest Right | (304, 0) | 48x48 | Mirrored crest for opposite flank |
| Gold Leaf Trim Strip A | (352, 0) | 96x16 | Repeating gilded edge trim, horizontal |
| Gold Leaf Trim Strip B | (352, 16) | 96x16 | Repeating gilded edge trim, corner variant |
| Gold Filigree Corner Set | (448, 0) | 64x32 | Four 16x32 corner flourishes for cart edges |

### Chandelier & Velvet Rope:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cart Chandelier Frame 1 | (256, 48) | 48x64 | Tiny crystal chandelier mounted on a CART — hanging still |
| Cart Chandelier Frame 2 | (304, 48) | 48x64 | Gentle sway left, crystals catching light |
| Cart Chandelier Frame 3 | (352, 48) | 48x64 | Gentle sway right |
| Velvet Rope Post | (400, 48) | 24x64 | Brass stanchion (yes, for a cart) |
| Velvet Rope Span Taut | (424, 48) | 80x32 | Burgundy velvet rope between posts |
| Velvet Rope Span Sagging | (424, 80) | 80x32 | Rope unhooked — queue admitted |

### Signage & Menu:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gothic Menu Board | (256, 112) | 96x128 | Full menu in Gothic German script — legible as a minefield, not as text |
| Calligraphy Price Tag Strip | (352, 112) | 96x16 | Three 32x16 elegant tags; the elegance makes the prices hurt more |
| Ornate Price Tag Large | (352, 128) | 48x24 | Zuckerschock Special tag, extra flourishes |
| Brass Review Plate A | (400, 128) | 48x24 | "★★★★★" etched in brass — suspiciously perfect |
| Brass Review Plate B | (448, 128) | 48x24 | Another five stars, different suspicious donor |
| Brass Review Plate C | (448, 152) | 48x24 | Third plate; all five stars, all suspicious |
| Pronunciation Guide Sign | (352, 152) | 96x48 | "Pronunciation Guide Available (5 Sovs)" — the guide costs money; the judgment is free |
| Photography Fee Sign | (352, 200) | 64x40 | "3 Sovs Foto. 10 Sovs mit Frau Tortenmeister. Sie hasst es." |
| Brass Register | (416, 200) | 48x48 | Antique register, polished daily, ding included |
| Main Signage | (0, 224) | 320x64 | "Der Zuckerschock — Konditormeister seit 1847" in gilded Gothic lettering |

### Base & Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cart Awning | (0, 288) | 256x64 | Cream and apricot striped canopy, gold fringe |
| Gilded Wheel | (256, 288) | 64x64 | Wagon wheel with brass spokes — it moves, and it's smug about it |
| Wheel Chock | (320, 288) | 32x32 | Carved wooden chock, current parking spot |
| Queue Stanchion Marker | (352, 288) | 32x32 | Brass floor marker: "Warten Sie hier" |
| Spotlight Housing Straight | (384, 288) | 32x32 | Case-mounted brass spotlight |
| Spotlight Housing Angled | (416, 288) | 32x32 | Angled variant for slice-dramatic lighting |
| Cool-Air Vent Grille | (448, 288) | 32x32 | Temperature-control vent, brass grille |
| Velvet Rope Hook | (480, 288) | 16x32 | Wall-side rope hook |
| "Seit 1847" Plaque | (320, 320) | 64x32 | Founding plaque; the cart is older than most buildings it parks beside |
| Cobblestone Base Tiles | (0, 352) | 64x32 | Two 32x32 street tiles under wheels |
| Cart Shadow Oval | (64, 352) | 128x32 | Soft ground shadow, all backdrops |
| Night Lantern Glow Variant | (192, 352) | 48x32 | Evening MusikGasse warm-glow overlay |
| Chandelier Crystal Detail | (240, 352) | 16x16 | Single crystal for glint effect anchoring |

### Technical Notes:
- Cart body renders once per backdrop; all trim/crest elements are baked into composition at load, not drawn separately (draw-call budget is 10)
- Chandelier sway is ambient 3-frame loop; static frame 1 used on low LOD and reduced-motion
- Gothic menu board text must read as "ornate German" at gameplay zoom without being real legible text (localization-proof)

---

## 🍰 Sprite Sheet 2: Display Case & Menu Items
**File:** `torte_royale_display_case.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #3D1C02 (Chocolate), #FFDAB9 (Apricot Glaze), #FFFDD0 (Cream), #5C0A14 (Velvet backing)

### Temperature-Controlled Glass Case (128x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Case Closed | (0, 0) | 128x96 | Pristine glass, individually spotlit slices, faint cool-air shimmer |
| Case Opening Frame 1 | (128, 0) | 128x96 | Lid rising, hinge glint |
| Case Opening Frame 2 | (256, 0) | 128x96 | Half open, cool air visibly escaping |
| Case Open | (384, 0) | 128x96 | Fully open — the cakes are briefly mortal |

### Precision Cutting & Service Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Spotlight Beam | (0, 96) | 32x48 | Individual cone of light per slice — museum treatment |
| Spotlight Glow Pool | (32, 96) | 32x48 | Warm pool on the display shelf |
| Knife Poised | (64, 96) | 48x48 | Silver knife hovering, surgical stillness |
| Knife Descend | (112, 96) | 48x48 | Mid-cut, perfectly vertical |
| Clean Cut | (160, 96) | 48x48 | Blade through, zero crumb deviation |
| Slice Lifted | (208, 96) | 48x48 | Slice raised on silver server, geometry intact |
| Silver Cake Server | (256, 96) | 32x24 | Engraved, older than the player character |
| Porcelain Plate | (288, 96) | 32x24 | White with gold rim |
| Lace Doily | (256, 120) | 32x24 | Cream lace, non-negotiable |
| Silver Tongs | (288, 120) | 32x24 | For Punschkrapfen handling only |
| Temperature Gauge | (320, 96) | 24x32 | Brass dial, needle at "Korrekt" |
| Sold-Out Placard | (344, 96) | 48x24 | Brass: "Ausverkauft" — somehow smug |
| Case Interior Shelf Tile | (392, 96) | 64x32 | Velvet-backed shelf segment |
| Empty Slot With Crumbs | (456, 96) | 48x48 | Post-purchase gap; crumbs arranged with dignity |

### Menu Items (the cakes must look GENUINELY excellent — the joke requires it):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sachertorte Slice | (0, 144) | 48x48 | Dark chocolate gleam, apricot glaze line, cross-section perfection |
| Linzer Torte | (48, 144) | 48x48 | Lattice top, ruby preserve visible |
| Apfelstrudel | (96, 144) | 48x48 | Golden layers, powdered sugar dusting |
| Kaiserschmarrn | (144, 144) | 48x48 | Torn pancake pile, caramelized edges, plum compote |
| Topfenstrudel | (192, 144) | 48x48 | Pale quark filling, delicate pastry sheen |
| Punschkrapfen | (240, 144) | 48x48 | Pink fondant cube, faintly boozy sparkle |
| Der Zuckerschock Special | (288, 144) | 64x64 | Tower of everything — the 25 Sovs recommendation trap |
| Special Pedestal | (352, 144) | 48x48 | Gilded riser; the Special sits above its peers |
| Glass Reflection Overlay | (400, 144) | 112x64 | Case-front reflection sweep for closed state |
| Presentation Plate With Slice | (0, 192) | 48x48 | Served state — doily, plate, slice, judgment |
| Item Spotlight Halo | (48, 192) | 48x48 | Additive glow ring behind any focused item |
| Mini Price Stand | (96, 192) | 24x32 | Calligraphy card holder per slice |
| Powdered Sugar Shaker | (128, 192) | 24x32 | Silver, for tableside Kaiserschmarrn drama |
| Case Lock & Key | (160, 192) | 24x24 | Konditor key — the cakes are secured overnight |

### Technical Notes:
- Case opening is 4-frame single-play; opening audio (hinge whisper + cool-air hiss) syncs to frame 2
- Cutting sequence holds "Clean Cut" 0.3s before "Slice Lifted" — precision is the performance
- Each menu item doubles as inventory icon at native 48x48 (Special at 64x64); no separate icon pass needed

---

## 👩‍🍳 Sprite Sheet 3: Frau Tortenmeister
**File:** `frau_tortenmeister.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #FFFFFF (Judgmental White uniform), #1A1A1A (Gothic Ink / pince-nez), #CFB53B (Gold accents)

### Judgment Baseline (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Neutral Judgment Idle 1 | (0, 0) | 64x96 | Default state: judgment. Hands folded, severe bun, pince-nez level |
| Neutral Judgment Idle 2 | (64, 0) | 64x96 | Subtle breath; judgment persists |
| Eyebrow Raise Frame 1 | (128, 0) | 64x96 | Left eyebrow beginning ascent |
| Eyebrow Raise Frame 2 | (192, 0) | 64x96 | Full altitude achieved |
| Eyebrow Raise Held | (256, 0) | 64x96 | Held indefinitely; the eyebrow has opinions |
| Approving Nod Frame 1 | (320, 0) | 64x96 | RARE. Chin dips 4 pixels |
| Approving Nod Frame 2 | (384, 0) | 64x96 | RARE. Lowest point — almost warmth |
| Approving Nod Frame 3 | (448, 0) | 64x96 | Return to neutral; it never happened |

### Disappointment Spectrum (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Slight Wince | (0, 96) | 64x96 | Passable pronunciation — one eye narrows, +10% |
| Visible Disappointment 1 | (64, 96) | 64x96 | Poor pronunciation — shoulders drop 2px, +25% |
| Visible Disappointment Held | (128, 96) | 64x96 | Sustained while price adjusts itself |
| Needs A Moment Frame 1 | (192, 96) | 64x96 | Catastrophic ("Zakertordy") — eyes close |
| Needs A Moment Frame 2 | (256, 96) | 64x96 | Hand rises to pince-nez |
| Needs A Moment Held | (320, 96) | 64x96 | Perfect stillness; the moment of silence is mandatory |
| Recovering Breath | (384, 96) | 64x96 | Slow exhale, composure rebuilt from tradition |
| Pince-Nez Adjust | (448, 96) | 64x96 | Micro-gesture punctuating any transaction |

### Crisis & Craft States (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sit-Down Frame 1 | (0, 192) | 64x96 | "American chocolate cake" mentioned — sway begins |
| Sit-Down Frame 2 | (64, 192) | 64x96 | Reaching for the stool, dignity intact |
| Sit-Down Frame 3 | (128, 192) | 64x96 | Seated devastation; still judging from the stool |
| Cutting Stance | (192, 192) | 64x96 | Knife raised, breath held, museum silence |
| Cutting Mid-Stroke | (256, 192) | 64x96 | The precise cut in progress |
| Presenting Slice | (320, 192) | 64x96 | Slice offered on silver — reverence expected |
| Register Ding Pose | (384, 192) | 64x96 | Key strike; the only sound she enjoys |
| Rare Conversation | (448, 192) | 64x96 | 6+ Charm only — she initiates. Almost warm(ish) |

### Interaction & Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu Correction Point | (0, 288) | 64x96 | Finger at Gothic script: "The SACHERTORTE." |
| Photography Objection | (64, 288) | 64x96 | Palm raised at camera; 10 Sovs and she still hates it |
| Accepting Payment | (128, 288) | 64x96 | Coins counted twice, silently |
| Pince-Nez Glint | (192, 288) | 16x16 | Lens flash detail for judgment beats |
| Grudge Ledger | (216, 288) | 32x40 | Leather book of catalogued mispronunciations (she remembers) |
| Stool | (256, 288) | 32x48 | For the sit-down reaction only; otherwise decorative |
| Handkerchief | (288, 288) | 24x24 | Pressed linen, dabbed after catastrophes |
| Approving Nod Held (Rare) | (320, 288) | 64x96 | Extended hold for "…Perhaps there is hope for you yet." |
| High-Contrast Silhouette | (384, 288) | 64x96 | Accessibility outline variant (see ♿) |
| Reserved Smile | (448, 288) | 64x96 | One frame. Never triggered in v1. Reserved for future DLC and legend |

### Technical Notes:
- Expression range IS the location — all five pronunciation tiers must be readable at 64x96 on a phone (posture + eyebrow + hand position, never face detail alone)
- Uniform stays pristine white in every state; only posture degrades
- Sit-down sequence single-play, holds frame 3 for full dialogue duration

---

## 👥 Sprite Sheet 4: Queue NPCs
**File:** `torte_royale_queue_npcs.png`
**Dimensions:** 512x384 pixels
**Color Palette:** Mixed civilian tones; #FFFDD0 (Cream) backdrop harmony, tourist pastels vs. local charcoals

### Nervous Tourist & Smug Local (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Nervous Tourist Idle | (0, 0) | 64x96 | Money belt visible, phrasebook clutched |
| Nervous Tourist Sweating | (64, 0) | 64x96 | Two customers from the front, rehearsing syllables |
| Nervous Tourist Ordering | (128, 0) | 64x96 | Mid-attempt, eyes closed in prayer |
| Nervous Tourist Relieved | (192, 0) | 64x96 | Survived with only +10% |
| Smug Local Idle | (256, 0) | 64x96 | Charcoal coat, unbothered posture |
| Smug Local Flawless Delivery | (320, 0) | 64x96 | Perfect pronunciation mid-word, hand gesture included |
| Smug Local Satisfaction | (384, 0) | 64x96 | Receiving the approving nod; peak smug |
| Smug Local Nod Exchange | (448, 0) | 64x96 | Mutual acknowledgment with Frau Tortenmeister — two equals |

### Backpacker & Cake Blogger (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Confused Backpacker Idle | (0, 96) | 64x96 | Oversized pack, wrong shoes for cobblestones |
| Backpacker Menu Squint | (64, 96) | 64x96 | Gothic script defeating him in real time |
| Backpacker Defeat | (128, 96) | 64x96 | "I just wanted chocolate cake, man..." |
| Cake Blogger Idle | (192, 96) | 64x96 | Ring light in bag, tips extensively |
| Cake Blogger Photographing | (256, 96) | 64x96 | Crouched for the perfect glaze angle |
| Cake Blogger Paying Fee | (320, 96) | 64x96 | 3 Sovs handed over, no regrets |
| Cake Blogger Mispronouncing | (384, 96) | 64x96 | Photographs everything, still says "SACK-er-tort" |
| Queue Shuffle Frame | (448, 96) | 64x96 | Shared one-step-forward frame, reused per NPC layer |

### Nostalgic Local & Confused American (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Nostalgic Local Idle | (0, 192) | 64x96 | Sensible coat, decades of standards |
| Nostalgic Local Gesturing | (64, 192) | 64x96 | "It was better in my grandmother's day" (it wasn't) |
| Nostalgic Local Disapproving | (128, 192) | 64x96 | Disapproves of the queue, the tourists, the year |
| Confused American Idle | (192, 192) | 64x96 | Baseball cap, genuine goodwill, zero context |
| Confused American Portion-Point | (256, 192) | 64x96 | Pointing at slice: "That's it? That's the whole thing?" |
| Confused American Question Gesture | (320, 192) | 64x96 | Just wants to understand the portions |
| Confused American Eating Awe | (384, 192) | 64x96 | First bite. Everything is forgiven. Worth every Sov |
| Money Belt Detail | (448, 192) | 32x32 | Tourist-detection trigger prop |
| Guidebook Detail | (480, 192) | 32x32 | "SINFONIA ON 40 Sovs/DAY" — the second trigger |

### Composite Queue Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Queue Group Compressed | (0, 288) | 192x96 | Three-body silhouette cluster for long-queue rendering (single draw) |
| Whispering Pair | (192, 288) | 128x96 | Two tourists exchanging anxious intel about the menu |
| Evacuating Tourist | (320, 288) | 64x96 | Fleeing after catastrophic tier; shame trails behind |
| Defeated Walk-Away | (384, 288) | 64x96 | Shown the door (briefly) after asking "what's cheap?" |
| Blogger Flash Raise | (448, 288) | 64x96 | Phone lifted overhead — pairs with camera flash effect |

### Technical Notes:
- Queue renders as max 4 individual NPCs + 1 compressed group sprite (draw-call discipline)
- Queue Shuffle Frame is shared by palette-swapping the base NPCs; no per-NPC walk cycles
- NPC mix shifts per backdrop: tourists (Imperial Square), intellectuals (Kaffeehaus Row), culture seekers (Opera), performers (MusikGasse)

---

## 🏛️ Sprite Sheet 5: Rotating Location Backdrops
**File:** `torte_royale_backdrops.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #FFFDD0 (Cream) base, per-backdrop tinting — morning gold, midday neutral, afternoon amber, evening violet

### Daily Rotation Backdrops (256x256 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Imperial Square Backdrop | (0, 0) | 256x256 | Morning (10–12): grand plaza, statue plinth, tour groups implied — tourist hunting grounds |
| Kaffeehaus Row Backdrop | (256, 0) | 256x256 | Midday (12–15): café façades, newspaper readers, intellectual lunchers, Café Existenz signage visible in distance |
| Opera House Vicinity Backdrop | (0, 256) | 256x256 | Afternoon (15–18): The Bassline Opera House steps and columns, culture seekers, intermission energy |
| MusikGasse Backdrop | (256, 256) | 256x256 | Evening (18–20): lantern-lit lane, performer crowds, instrument cases, warm night tint |

### Technical Notes:
- Backdrops swap by time of day via single texture-region change — zero transition cost; cart and case sprites layer identically over all four
- Each backdrop pre-tinted (no runtime color grading) to protect the 10-draw-call budget
- Cart position anchor identical in all four (cart shadow oval aligns to same baseline y)

---

## ✨ Sprite Sheet 6: Effects & UI
**File:** `torte_royale_effects_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #FFFFFF (glints/steam), #CFB53B (gold UI trim), #3D1C02 (UI panels), #FFDAB9 (highlights)

### Particles & Audio Glyphs:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sugar Dust Frame 1 | (0, 0) | 16x32 | Fine sparkle drift off fresh-cut slices |
| Sugar Dust Frame 2 | (16, 0) | 16x32 | Dispersing |
| Sugar Dust Frame 3 | (32, 0) | 16x32 | Settling |
| Chocolate Sheen Glint 1 | (48, 0) | 24x24 | Light sweep across Sachertorte glaze |
| Chocolate Sheen Glint 2 | (72, 0) | 24x24 | Glint peak — the gleam that sells it |
| Steam Frame 1 | (96, 0) | 16x32 | Rising from fresh Apfelstrudel/Kaiserschmarrn |
| Steam Frame 2 | (112, 0) | 16x32 | Curling |
| Steam Frame 3 | (128, 0) | 16x32 | Fading |
| Disappointed-Sigh Glyph | (144, 0) | 32x32 | Drooping breath-cloud glyph — visual twin of the sigh audio |
| Approval-Hum Glyph | (176, 0) | 32x32 | Gentle rising wave lines (no notes — there is no music here) |
| Silence Indicator | (208, 0) | 32x24 | "..." glyph for the mandatory moment of silence |
| Register Ding Star | (240, 0) | 24x24 | Brass ping burst over the register |
| Case-Open Shimmer | (264, 0) | 32x32 | Cool-air sparkle when case opens |
| Spotlight Sparkle | (296, 0) | 16x16 | Per-slice glint pop |
| Camera Flash Burst | (312, 0) | 32x32 | Blogger flash / photography fee trigger |
| Moment-of-Silence Vignette Tile | (344, 0) | 64x64 | Screen-corner dimming tile for catastrophic tier |

### Pronunciation Mini-Game Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mini-Game Panel | (0, 64) | 384x192 | Gothic-framed panel: item name in German, phonetic breakdown zone top, multiple-choice zone bottom |
| Phonetic Syllable Chip | (384, 64) | 96x32 | "SAH · khur · TOR · tuh" chip, neutral state |
| Phonetic Syllable Chip Selected | (384, 96) | 96x32 | Gold-rimmed selected state |
| Choice Button | (384, 128) | 112x40 | Multiple-choice pronunciation option (44px+ touch height with padding) |
| Choice Button Pressed | (384, 168) | 112x40 | Pressed state, brass depression |
| Tier Icon — Perfect | (384, 208) | 32x32 | Gold laurel (unique shape: circle) — approving nod, −15% |
| Tier Icon — Good | (416, 208) | 32x32 | Brass seal (square) — neutral acceptance |
| Tier Icon — Passable | (448, 208) | 32x32 | Wavy ribbon (diamond) — slight wince, +10% |
| Tier Icon — Poor | (480, 208) | 32x32 | Drooping flag (pentagon) — visible disappointment, +25% |
| Tier Icon — Catastrophic | (448, 240) | 32x32 | Cracked plate (octagon) — moment of silence, +50% |

### Price & Status Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Price Modifier Popup +% | (0, 256) | 64x32 | Red-trimmed "+25%" bubble with down-arrow shape cue |
| Price Modifier Popup −% | (64, 256) | 64x32 | Gold-trimmed "−15%" bubble with laurel shape cue |
| Grudge Surcharge Popup | (128, 256) | 48x24 | "+3 Sovs" — she remembers |
| Competence Surcharge Tag | (176, 256) | 96x24 | "Menu assumed competence" itemized line |
| Cake Connoisseur Badge | (272, 256) | 48x48 | Gold fork-and-laurel crest — 200 Sovs spent, judgment reduced |
| Sugar High Buff Icon | (320, 256) | 32x32 | Upward sparkle burst (up-arrow silhouette) |
| Sugar Crash Debuff Icon | (352, 256) | 32x32 | Melting droop (down-arrow silhouette) |
| Uncultured Status Icon | (384, 256) | 32x32 | Broken pretzel over crossed fork (5-min shame debuff) |
| Tipsy Status Icon | (416, 256) | 32x32 | Wobbling Punschkrapfen cube |
| Photography Fee Prompt | (0, 304) | 192x96 | Dialog: "Foto: 3 Sovs / Mit Frau Tortenmeister: 10 Sovs (sie hasst es)" with accept/decline zones |
| Payment Confirm Dialog | (192, 304) | 160x96 | Itemized receipt panel — base price + pronunciation adjustments, in calligraphy |
| Charm Price Indicator | (352, 304) | 96x32 | Tourist-detection meter: money-belt icon → local-coat icon |
| Queue Position Marker | (352, 336) | 32x32 | "You are customer 4" brass token |
| Daily Rotation Compass | (384, 336) | 48x48 | Four-point cart-location dial (Square/Row/Opera/Gasse) for Cart Hunter tracking |
| Point-At-Menu Skip Button | (448, 304) | 64x40 | Coward's option — skips mini-game, applies penalty |
| Five-Star Suspicion Tooltip | (448, 344) | 64x40 | Tap a brass plate: "Review verified by Frau Tortenmeister's nephew" |

### Accessibility Variants (see ♿ section):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Display Case HC Outline | (0, 400) | 128x96 | High-contrast frame around primary interactable |
| Vendor HC Silhouette | (128, 400) | 64x96 | Frau Tortenmeister outline against cream backdrops |
| Menu Board HC Outline | (192, 400) | 96x112 | High-contrast Gothic menu frame |
| Velvet Rope HC Marker | (288, 400) | 64x48 | Queue entry point marker |
| Static Chandelier Frame | (352, 400) | 48x64 | Reduced-motion chandelier (no sway) |
| Dust-Free Case Overlay | (400, 400) | 64x64 | Removes sugar-dust particles |
| Steam-Free Item Overlay | (464, 400) | 48x48 | Removes steam loops from fresh items |

### Technical Notes:
- All five tier icons are SHAPE-coded (circle/square/diamond/pentagon/octagon) — color is reinforcement only
- Price popups pair sign, color, AND arrow silhouette; never color alone
- Mini-game panel is a single NinePatch draw; chips and buttons are the only per-frame additions

---

## 🎬 Animation Specifications

### Glass Case Opening:
- **Duration:** 0.8 seconds, single play
- **Frames:** 4 (closed → frame 1 → frame 2 → open)
- **Pattern:** Advance every 0.2s, hold open state
- **Trigger:** Purchase confirmed / Frau Tortenmeister begins service
- **Purpose:** Ceremony — the case opens like a reliquary
- **Audio Sync:** Hinge whisper + cool-air hiss on frame 2 (0.4s)
- **Mobile Optimization:** None needed

### Precise Slice Cutting:
- **Duration:** 1.2 seconds, single play (hold Clean Cut 0.3s)
- **Frames:** 4 (poised → descend → clean cut → lifted)
- **Pattern:** 0.3s poised → 0.2s descend → 0.3s hold → 0.4s lift
- **Trigger:** Sachertorte/Linzer/Topfenstrudel purchase (sliced items)
- **Purpose:** The precision is the pretension — surgical theater for dessert
- **Audio Sync:** Single clean knife-through sound at descend (0.5s); porcelain clink at lift (1.0s)
- **Mobile Optimization:** None needed

### Frau Tortenmeister Neutral Judgment Idle:
- **Duration:** 2.0 second cycle, loop
- **Frames:** 2
- **Pattern:** Frame 1 (1.2s) → Frame 2 breath (0.8s) → loop
- **Trigger:** Constant while cart is open
- **Purpose:** Default state: judgment. The idle IS the atmosphere
- **Audio Sync:** None — the silence is the audio design (no music: cake is serious business)
- **Mobile Optimization:** None needed

### Approving Nod (RARE):
- **Duration:** 1.0 second, single play
- **Frames:** 3
- **Pattern:** Frame 1 (0.3s) → Frame 2 (0.4s) → Frame 3 return (0.3s)
- **Trigger:** Perfect pronunciation tier only
- **Purpose:** The rarest reward in Sinfonia; players will chase this nod
- **Audio Sync:** Approval hum begins on frame 2 (0.3s), hum glyph spawns simultaneously
- **Mobile Optimization:** None needed

### Needs A Moment (Catastrophic Reaction):
- **Duration:** 3.0 seconds (2.0s mandatory held silence)
- **Frames:** 3 + recovery frame
- **Pattern:** Eyes close (0.4s) → pince-nez hand (0.6s) → held stillness (2.0s) → recovering breath
- **Trigger:** Catastrophic pronunciation tier ("Zakertordy")
- **Purpose:** The moment of silence as gameplay consequence; +50% applies when she reopens her eyes
- **Audio Sync:** Disappointed sigh at 0.4s (sigh glyph fires with it); then engineered total silence — ambient street audio ducks to zero for the 2.0s hold
- **Mobile Optimization:** Vignette tile omitted on low-end; held frame carries it

### Needs To Sit Down (American Chocolate Cake):
- **Duration:** 2.4 seconds, single play, hold seated
- **Frames:** 3
- **Pattern:** Sway (0.8s) → stool reach (0.8s) → seated devastation held (0.8s+, holds through dialogue)
- **Trigger:** Player compares menu to "American chocolate cake" (The Ultimate Crime achievement)
- **Purpose:** The comparison crime's full visual payoff
- **Audio Sync:** Stool scrape at 1.4s; nothing else — words have failed her
- **Mobile Optimization:** None needed

### Register Ding:
- **Duration:** 0.4 seconds, single play
- **Frames:** 2 (pose + ding star effect)
- **Pattern:** Key strike → ding star burst over register
- **Trigger:** Payment accepted
- **Purpose:** Transaction closure; the only sound she enjoys
- **Audio Sync:** Brass register ding exactly on star spawn (0.1s)
- **Mobile Optimization:** None needed

### Chandelier Sway (Ambient):
- **Duration:** 3.0 second cycle, loop
- **Frames:** 3 (still → left → right)
- **Pattern:** Gentle pendulum, 1.0s per frame
- **Trigger:** Constant (breeze); pauses during moment-of-silence
- **Purpose:** A chandelier. On a cart. Perpetually reminding you of both facts
- **Audio Sync:** None
- **Mobile Optimization:** Static frame on low LOD / reduced motion

### Sugar Dust & Steam Loops:
- **Duration:** 1.5 second cycles, loop
- **Frames:** 3 each
- **Pattern:** Rise → disperse → fade
- **Trigger:** Sugar dust on cut events; steam constant on Apfelstrudel/Kaiserschmarrn/Topfenstrudel slots
- **Purpose:** Freshness signal — these cakes are genuinely excellent and the particles prove it
- **Audio Sync:** None
- **Mobile Optimization:** Steam sources halved (3 → 1), sugar dust event-only on low LOD

### Queue Shuffle:
- **Duration:** 0.6 seconds per advance, single play per queue event
- **Frames:** 2 (idle → shuffle frame → next idle)
- **Pattern:** Whole queue advances one slot after each transaction
- **Trigger:** Customer served or flees
- **Purpose:** Waiting-game tension; player watches others succeed/fail before their turn
- **Audio Sync:** Soft footstep scuff at 0.3s
- **Mobile Optimization:** Compressed group sprite advances as one unit

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Display Case HC Outline | (0, 400) on effects/UI sheet | 128x96 | High-contrast frame around the primary interactable |
| Vendor HC Silhouette | (128, 400) on effects/UI sheet | 64x96 | Frau Tortenmeister outline vs. cream backdrops (white-on-cream is the risk case) |
| Menu Board HC Outline | (192, 400) on effects/UI sheet | 96x112 | Gothic menu interaction zone marker |
| Velvet Rope HC Marker | (288, 400) on effects/UI sheet | 64x48 | Queue entry point — where the interaction begins |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Chandelier Frame | (352, 400) on effects/UI sheet | 48x64 | No sway; single frame replaces loop |
| Dust-Free Case Overlay | (400, 400) on effects/UI sheet | 64x64 | Removes sugar-dust particle loops |
| Steam-Free Item Overlay | (464, 400) on effects/UI sheet | 48x48 | Removes steam loops; freshness conveyed by sheen glint (2-frame, slow) |

### Visual Audio Cues (critical — pronunciation feedback is primarily audio):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Disappointed-Sigh Glyph | (144, 0) on effects/UI sheet | 32x32 | Fires with every sigh audio event — bad pronunciation readable with sound off |
| Approval-Hum Glyph | (176, 0) on effects/UI sheet | 32x32 | Fires with approval hum — the rare nod is never audio-only |
| Silence Indicator | (208, 0) on effects/UI sheet | 32x24 | "..." glyph + vignette during mandatory silence (the ducked audio has a visual) |
| Register Ding Star | (240, 0) on effects/UI sheet | 24x24 | Transaction-complete visual for the register ding |
| Case-Open Shimmer | (264, 0) on effects/UI sheet | 32x32 | Visualizes hinge whisper + cool-air hiss |
| Camera Flash Burst | (312, 0) on effects/UI sheet | 32x32 | Visualizes shutter sound / photography fee trigger |

### Colorblind Considerations:
- The five pronunciation tiers are SHAPE-coded (laurel-circle / seal-square / ribbon-diamond / flag-pentagon / cracked-octagon) — never color-only; tier name text always accompanies the icon
- Price popups pair +/− sign, arrow silhouette, and numeric text; red/gold tint is reinforcement only
- Sugar High (up-burst) vs. Sugar Crash (down-droop) are distinct silhouettes, not palette swaps
- Charm price indicator uses icon progression (money belt → local coat), not a color gradient
- Touch zones minimum 44px for: menu board, display case, each choice button (112x40 + padding), point-at-menu skip, photography prompt buttons, payment confirm

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); display case sheet at ASTC 4x4 — the chocolate sheen is the product shot
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for display case & menu items sheet (cakes are screenshot-critical; the joke requires they look genuinely excellent)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| torte_royale_environment | cart, display case, backdrops | 1024x1024 |
| torte_royale_characters | Frau Tortenmeister, queue NPCs | 1024x512 |
| torte_royale_effects_ui | particles, glyphs, mini-game UI | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Chandelier sway, 3 steam sources, sugar dust on cuts, sheen glints, 4 queue NPCs + group sprite |
| Medium | Static chandelier, 1 steam source, sheen glints only, 3 queue NPCs + group sprite |
| Low | All ambient particles off, static everything except Frau Tortenmeister expressions (never cut — they ARE the location), 2 NPCs + group sprite |

### Performance Targets:
- **Target FPS:** 60 (deliberately lightweight scene — per location profile, NOT 60)
- **Max Draw Calls:** 10 per frame
- **Memory Footprint:** 25 MB maximum
- **Particle Limit:** 12 (steam 3, sugar dust 6, sheen 2, flash 1 — event particles replace ambient, never stack)

### Performance Notes:
- Simple scene by design: one cart, one case, one vendor, small queue — budget goes to Frau Tortenmeister's expression range, which is the actual content
- Backdrops swap by time of day as a single texture-region switch; no transition animation, no double-loading
- Cart + trim composited at load into one canvas item; backdrop + cart + case = 3 environment draws
- Queue uses shared shuffle frame + palette swaps; compressed group sprite caps NPC draws
- Moment-of-silence audio ducking is a bus fade, zero render cost

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- AnimatedSprite2D for Frau Tortenmeister expression states (single state machine: idle → tier reaction → return)
- CPUParticles2D (not GPU) for steam, sugar dust, sheen
- CanvasLayer for pronunciation mini-game panel and price popups
- Cart location controller: `time_of_day` drives backdrop region + NPC mix + queue composition (10–12 Square / 12–15 Row / 15–18 Opera / 18–20 Gasse)
- Persistent flags: `pronunciation_mastery[item]`, `connoisseur_progress_sov`, `grudge_ledger[]` (photography offenses, comparison crimes), `uncultured_until` timestamp

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Case opening frame 2 | Hinge whisper + cool-air hiss | 0.4s into open animation |
| Knife descend / porcelain lift | Clean knife-through, then plate clink | 0.5s / 1.0s of cutting sequence |
| Register ding pose | Brass register ding | On ding-star spawn (0.1s) |
| Visible Disappointment / Needs A Moment | Disappointed sigh (+ sigh glyph) | On first frame of either reaction |
| Approving nod frame 2 | Approval hum (+ hum glyph) | 0.3s into nod |
| Needs A Moment held frame | Total silence — ambient bus ducks to zero | 2.0s hold; silence indicator + vignette carry it visually |
| Blogger flash raise | Camera shutter | On flash burst spawn |
| Ambient (always) | NO MUSIC — street murmur + case hum only | "Cake is serious business": the silence itself is the audio design |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Perfect Pronunciation | Mini-game panel, syllable chips, all 5 tier icons, approving nod frames | Master all 7 menu items; per-item mastery tracked via tier results |
| Cake Connoisseur | Payment dialog, Connoisseur badge, reduced-judgment idle usage | 200 Sovs cumulative spend unlocks badge + flat 10% discount + fewer wince frames |
| The Comparison Crime | Sit-down sequence, grudge ledger, surcharge popups | Dialogue trigger; mentioning other cities' desserts fires disappointment tier, "American chocolate cake" fires full sit-down |
| Cart Hunter | All four backdrops, daily rotation compass, cart shadow anchor | Find cart at all four locations in one day; compass UI tracks visits |
| Achievements (First Slice / Acceptable / The Full Menu / Cart Stalker / Photography License / The Ultimate Crime / Redemption Arc) | Menu item sprites, tier icons, photo fee prompt, Uncultured icon, sit-down hold frame | Achievement toasts reuse item/tier/status sprites; The Ultimate Crime = sit-down sequence completion |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Kaffeehaus Row | Primary midday backdrop; Café Existenz façade visible in backdrop distance | None — cart is IN the street scene |
| Café Existenz | Philosophers reference the cart ("is the cake authentic?"); no shared sprites, shared district palette | Standard street adjacency |
| The Bassline Opera House | Afternoon backdrop; intermission crowd NPC mix; opera-goer variants reuse culture-seeker palette swaps | Cart appears near steps 15:00–18:00 |
| Imperial Square | Morning backdrop; heaviest tourist NPC mix (money belt / guidebook props active) | Cart appears 10:00–12:00 |
| Daily Rotation System (integration note) | The cart is a single scene instanced at four map anchor points on a real-time schedule; world map shows cart pin only at current anchor. Finding it without asking NPCs grants Charm bonus; NPC directions come with judgment | Backdrop region swap + anchor move at 12:00 / 15:00 / 18:00 |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A palace that fits on four wheels and knows it's better than you"
- **Color Mood:** Deep chocolate browns and cream warmth pierced by imperial gold — inviting food, uninviting institution
- **Lighting:** Individual spotlights per slice (museum treatment), natural daylight shifting per backdrop, tiny chandelier glow, evening lantern warmth on MusikGasse
- **Texture:** Polished brass, pressed white linen, flawless glaze, velvet nap — nothing here is worn; decay would be a pronunciation error

### Environmental Storytelling:
- A velvet rope, a chandelier, and brass five-star review plates on a CART — the pretension outsizes the vehicle by design
- All review plates are five stars and all are suspicious (tooltip: verified by her nephew)
- The Pronunciation Guide costs 5 Sovs; the judgment it would prevent is dispensed free
- The grudge ledger sits visibly by the register: she catalogues mispronunciations, she remembers
- The cakes themselves are rendered with genuine, un-ironic beauty — the satire only works if the product is actually excellent

### Character Integration Notes:
- Frau Tortenmeister's expression range is the location's content budget: five pronunciation tiers must read at 64x96 via posture, eyebrow altitude, and hand position — never face detail alone
- Her uniform stays Judgmental White (#FFFFFF) in every state; only her posture and the queue's morale degrade
- Queue NPCs are the tutorial: the player watches the smug local succeed and the backpacker fail before ordering
- She is rendered slightly taller than every customer sprite. This is not an accident

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The full cart reveal** — velvet rope, chandelier, and five-star brass plates on a pastry cart; the pretension-per-square-meter record
2. **The Approving Nod** — the rarest animation in Sinfonia; players will screenshot the frame like a shiny catch
3. **The sit-down** — Frau Tortenmeister lowering herself onto the stool after "American chocolate cake," Uncultured icon blooming over the player
4. **The itemized receipt** — base price plus "menu assumed competence" surcharge line in perfect calligraphy
5. **"The Judge" selfie variant** — her judgment face beside the player mid-mispronunciation, caption "Cultural Education in Progress"

### Quote Potential:
- "Welcome to Der Zuckerschock. I assume you cannot pronounce anything on the menu." — Frau Tortenmeister
- "The menu assumed competence." — Frau Tortenmeister
- "...Perhaps there is hope for you yet." — Frau Tortenmeister, after good pronunciation
- "The Sachertorte is made with seventeen layers of tradition and one layer of disappointment when tourists call it 'chocolate cake.'" — Frau Tortenmeister
- "I just wanted chocolate cake, man..." — Confused Backpacker
- "They are ALL chocolate. Be specific." — Frau Tortenmeister

---

## 📋 Required PNG Files (6 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | torte_royale_cart.png | 512x384 |
| 2 | torte_royale_display_case.png | 512x256 |
| 3 | frau_tortenmeister.png | 512x384 |
| 4 | torte_royale_queue_npcs.png | 512x384 |
| 5 | torte_royale_backdrops.png | 512x512 |
| 6 | torte_royale_effects_ui.png | 512x512 |

**Total Estimated Memory:** ~5 MB (uncompressed RGBA — 1,245,184 px × 4 bytes ≈ 4.98 MB; comfortably inside the 25 MB scene budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `torte_royale_cart.png` (512x384)
- [ ] `torte_royale_display_case.png` (512x256)
- [ ] `frau_tortenmeister.png` (512x384)
- [ ] `torte_royale_queue_npcs.png` (512x384)
- [ ] `torte_royale_backdrops.png` (512x512)
- [ ] `torte_royale_effects_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + backdrop rotation schedule guide (which backdrop, which NPC mix, which hours)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All five pronunciation-tier reactions distinguishable at 64x96 on a 5" phone screen (posture + eyebrow + hands — the judgment expression range is the location)
- [ ] Cakes look genuinely, un-ironically excellent — the satire collapses if the product doesn't deserve the ceremony
- [ ] Approving nod reads as rare and precious (subtle, 4px chin dip, no exaggeration)
- [ ] Sit-down sequence lands as devastation, not slapstick
- [ ] Cart composition reads as "absurdly over-appointed" against all four backdrops
- [ ] Tier icons distinguishable by shape alone in grayscale
- [ ] Sigh and hum glyphs legible at gameplay scale (audio feedback must never be sound-only)
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (authenticity gatekeeping, pretension economy) is clear throughout all assets
- [ ] Cart-hunt discoverability cues present (queue visible from distance, chandelier glint as beacon)
- [ ] Mobile performance optimized (CPU particles, 10 draw calls, 60 FPS scene, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for all interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (tier shapes, popup arrows)
- [ ] Social media viral potential maximized in composition choices (nod frame, sit-down, receipt)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Viennese konditorei culture evoked, never named |
| Cultural Specificity | ✅ | Sachertorte mythos, konditorei tradition, pronunciation-as-status |
| Satirical Targets Appropriate | ✅ | Food-tourism pretension and gatekeeping — not Austrian cuisine or locals; punches up at the authenticity industry |
| Seedy Underbelly Present | ✅ | Tourist-detection price gouging, photography fees, pronunciation surcharges, grudge ledger, nephew-verified five-star reviews |
| Gameplay Value Established | ✅ | Shop economy, pronunciation mini-game, Charm pricing, buff/debuff loop, daily location hunt |
| Technical Feasibility | ✅ | Six sheets, three atlases, LOD tiers, single-scene four-anchor rotation documented |
| Mobile Performance Budget | ✅ | 60 FPS target, 10 draw calls, 25 MB, 12 particles (per location profile — deliberately lightweight) |
| Accessibility Features | ✅ | Sigh/hum/silence glyphs for all audio events; shape-coded tiers; reduced-motion variants; 44px zones |
| No Crypto Elements | ✅ | Pure food snobbery; the only speculative asset is your pronunciation |
| Social Media Integration | ✅ | Approving nod, sit-down, and competence-surcharge receipt identified as shareable beats |

**Torte Royale: the only shop in Eurobound where the boss fight is a vowel, the loot is genuinely worth it, and victory is a four-pixel nod from a woman who catalogues your failures in a leather book.**
