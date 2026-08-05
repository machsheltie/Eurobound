# The Awkward Truffle - Complete PNG Asset Requirements

## 📋 Overview
The Awkward Truffle is a tourist-district boutique where award-winning Belgian chocolate craftsmanship meets full anatomical accuracy — a shop whose three-zone layout (respectable front, suggestive middle, committed back) mirrors every customer's journey from "I'll just look" to "I'll take the party platter." This document specifies every PNG asset for the shop: zone backdrops, exterior and display fixtures, Sophie and Niels NPC sheets, the customer cast, the tastefully-abstracted product line, and effects/UI including the "Complicated Feelings" status. Its satirical essence in a sentence: complete professionalism applied to ridiculous products, and everyone eventually eats their "gag gift" alone.

**Location ID:** `shamsterdam_tourist_awkward_truffle_01`
**Theme:** The "it's a gag gift" denial; bachelor/bachelorette souvenir culture; Belgian chocolate artistry colliding with Shamsterdam's commerce of the body — body-positive framing, chocolate > shame
**Zone:** Tourist shopping district, strategically placed between normal shops for impulse purchases
**Hours:** 10 AM - 9 PM (extended tourist hours)
**Primary Function:** Specialty shop / zone-progression social comedy / consumable economy (+HP with "Complicated Feelings" status) / gift system with "gift vs kept" tracking / "Truffle Collector" achievement track

**Content Note (MA rating):** All anatomical products render as tasteful abstractions — silhouettes, wrapped forms, and suggestive-but-not-explicit shapes per the profile's "appropriate abstraction" mandate. The comedy is in reactions and framing, never in explicit detail.

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Chocolate Brown | #3C1414 | Product bodies, display shadows |
| Belgian Gold | #CFB53B | Case trim, branding, award plaques |
| Cream Display | #FFF8DC | Case interiors, walls, wrapping paper |
| Anatomical Pink | #FFB6C1 | Packaging accents, Zone 3 ribbon coding |
| Boutique Warm | #E8C87A | Warm boutique lighting wash |
| Velvet Shadow | #2A1A2E | Zone 3 depth and drapes |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/awkward_truffle/
├── environment/
│   ├── truffle_zone_backdrops.png
│   └── truffle_fixtures.png
├── npcs/
│   ├── npc_sophie_bas.png
│   └── npc_truffle_customers.png
├── objects/
│   └── truffle_products.png
└── ui/
    └── truffle_effects_ui.png
```

---

## 🏪 Sprite Sheet 1: Zone Backdrops (The Gradual Revelation)
**File:** `truffle_zone_backdrops.png`
**Dimensions:** 1920x1080 pixels
**Color Palette:** Cream → gold → velvet gradient across zones

### Interior Zones (640x1080 vertical panels, walked left to right):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Zone 1 — The Respectable Entry | (0, 0) | 640x1080 | Traditional truffles/pralines/bars, "normal chocolate shop" energy, brightest lighting |
| Zone 2 — The Transition | (640, 0) | 640x1080 | Shapes become... suggestive; plausible-deniability abstract forms; lighting warms |
| Zone 3 — The Commitment | (1280, 0) | 640x1080 | Full specialty display (abstracted), velvet drapes, "We're all adults here" section |

### Technical Notes:
- The three panels tile seamlessly into one continuous horizontal scroll — the zone progression IS the level design
- Lighting gradient is baked: Zone 1 bright cream → Zone 3 warm velvet; CanvasModulate handles day/evening tint only
- Zone 2 shapes must genuinely support both readings ("is that a... no, it's probably just... wait")

---

## 🏬 Sprite Sheet 2: Exterior & Shop Fixtures
**File:** `truffle_fixtures.png`
**Dimensions:** 1024x768 pixels

### Exterior & Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Exterior storefront | (0, 0) | 384x384 | Elegant script signage, artful window display (normal chocolates front, hints beyond), "Yes, those are what you think they are" tiny sign |
| Zone transition doorway | (384, 0) | 128x256 | Arch between sections, ribbon curtain |
| Crafting window | (512, 0) | 256x256 | Sophie visible at work, warm spot lighting |
| Counter & wrapping station | (768, 0) | 256x192 | Transaction zone near the "respectable" front, dignity preservation by design |

### Display Cases (The Gallery of Awkwardness):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Case 1 — The Classics | (0, 384) | 256x192 | Traditional Belgian chocolates, establishes legitimacy |
| Case 2 — The Suggestives | (256, 384) | 256x192 | Abstract shapes that MIGHT be something |
| Case 3/4 — The Anatomicals (paired case) | (512, 384) | 256x192 | Equal-opportunity awkwardness, arranged by "complexity" (abstracted contents) |
| Case 5 — The Couples' Collection | (768, 384) | 128x192 | Coordinated gift-box sets |
| Case 6 — Party Platter display | (896, 384) | 128x192 | Bulk arrangements, bachelor/bachelorette packages |
| Award plaque wall strip | (0, 576) | 256x96 | "Belgian Master Chocolatier — Award Winning" |
| Gift wrap options rack | (256, 576) | 192x96 | Standard/discreet/festive/bold/party regalia rolls |
| Window display (interior side) | (448, 576) | 192x128 | The respectable decoys |
| Price placard set (5) | (640, 576) | 160x96 (5x 32x96) | 8-120 Sovs range markers |
| Shop shelf backing (tileable) | (800, 576) | 224x128 | Cream shelving fill tile |

### Technical Notes:
- Cases are separate sprites over backdrops so contents can swap for the "Full Collection" purchased state
- Crafting window has a cut-out region where Sophie's crafting animation plays behind glass
- All case contents rendered at abstraction level: wrapped forms, ribboned silhouettes, tasteful shadows

---

## 👩‍🍳 Sprite Sheet 3: Sophie & Niels
**File:** `npc_sophie_bas.png`
**Dimensions:** 320x480 pixels
**Sprite Size:** 64x96 pixels (5 columns x 5 rows)

### Chocolatier Sophie (rows 0-2):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Row 0: Idle composure (2 frames) | (0, 0) | 128x96 | Chocolate-stained apron, complete professional dignity |
| Row 0: Welcome gesture (2 frames) | (128, 0) | 128x96 | "Belgian chocolate, creative interpretations, no judgment." |
| Row 1: Crafting at window (3 frames) | (0, 96) | 192x96 | Tempering, detail work — treats every piece as art regardless of shape |
| Row 1: Presenting piece (2 frames) | (192, 96) | 128x96 | "73% Ecuadorian cacao. The shape is... anatomical. The CHOCOLATE is excellent." |
| Row 2: Gift wrapping (2 frames) | (0, 192) | 128x96 | "Discreet or... declarative?" |
| Row 2: Commission consideration (1 frame) | (128, 192) | 64x96 | "We've made stranger. We've made MUCH stranger." |

### Assistant Niels (rows 3-4):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Row 3: Idle with smirk (2 frames) | (0, 288) | 128x96 | Bow tie professional, permanent slight smirk (human) |
| Row 3: Helpful gesture (2 frames) | (128, 288) | 128x96 | "Don't be shy. I've worked here two years. Nothing fazes me." |
| Row 4: Wrapping sequence (3 frames) | (0, 384) | 192x96 | Paper fold → ribbon → handover, any style |
| Row 4: Deadpan product description (1 frame) | (192, 384) | 64x96 | "The dark is more intense. In flavor. Obviously flavor." |

### Technical Notes:
- Sophie's crafting loop plays continuously behind the crafting window glass; her face NEVER breaks composure in any frame
- Niels's smirk is 2 pixels of mouth curve — restraint is the joke
- Wrapping sequence frames are shared across all five wrap styles via ribbon palette swap

---

## 👥 Sprite Sheet 4: Customer NPCs
**File:** `npc_truffle_customers.png`
**Dimensions:** 640x288 pixels
**Sprite Size:** 64x96 base; groups 256x96 / 128x96

### Row 0 (y=0):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "Just Chocolate" Shopper (2 frames) | (0, 0) | 128x96 | Stuck in Zone 1, aggressively avoiding eye contact with the rest of the shop |
| Bachelor Party Scout (2 frames) | (128, 0) | 128x96 | Photographing platter options, serious mission face |
| Repeat Customer (2 frames) | (256, 0) | 128x96 | Local, refill run, zero embarrassment, friendly with Sophie |
| Brave Couple (2 frames) | (384, 0) | 256x96 (2x 128x96) | Meaningful eye contact over the Couples' Set |

### Row 1 (y=96):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bachelorette Group (2 states) | (0, 96) | 512x96 (2x 256x96) | Matching sashes, competitive ranking energy — "It looks JUST like Kevin" |
| Instagram Documentarian (2 frames) | (512, 96) | 128x96 | Aesthetic angles — "This is SO MUCH content." |

### Row 2 (y=192):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Generic browse cycle (4 frames) | (0, 192) | 256x96 | Shared rig for zone drift movement |
| Zone 2 hesitation loop (2 frames) | (256, 192) | 128x96 | Hover-unable-to-commit pose (Bravado loss trigger) |
| Zone 3 commitment stride (2 frames) | (384, 192) | 128x96 | No more pretense walk |
| Checkout dignity pose (1 frame) | (512, 192) | 64x96 | "It's for a friend," said with a straight face |

### Technical Notes:
- Customer zone-progression uses the shared browse rig with per-zone pose overrides
- Bachelorette group caps at one instance; congestion event swaps in state B (louder posing)
- Documentarian's ring light is baked into her frames (no separate prop needed here)

---

## 🍫 Sprite Sheet 5: Product Line (Tastefully Abstracted)
**File:** `truffle_products.png`
**Dimensions:** 512x256 pixels

### Products (Case Stock & Inventory Icons):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Classic Truffle Box (6) | (0, 0) | 48x32 | 12 Sovs — "for when you're with family" |
| Abstract "Art" Piece | (48, 0) | 32x32 | 8 Sovs dark — "open to interpretation" |
| The Male Classic (abstracted) | (80, 0) | 32x48 | 15 Sovs milk — bestseller, silhouette form |
| The Male Detailed (abstracted) | (112, 0) | 32x48 | 25 Sovs Belgian dark — "for the discerning customer" |
| The Female Classic (abstracted) | (144, 0) | 32x48 | 15 Sovs white — equal opportunity awkwardness |
| The Female Detailed (abstracted) | (176, 0) | 32x48 | 25 Sovs Belgian dark — craftsmanship respects no gender |
| The Couples' Set | (208, 0) | 64x48 | 35 Sovs paired gift box |
| Bachelor Party Platter | (272, 0) | 96x64 | 50 Sovs bulk — "make it weird for 8-12 people" |
| Bachelorette Party Platter | (368, 0) | 96x64 | 50 Sovs matching energy, different shapes |
| The Full Collection box | (0, 64) | 128x96 | 120 Sovs — "You're committed. We respect that." |
| Custom Commission (wrapped mystery) | (128, 64) | 48x64 | 75 Sovs+ — fully wrapped, shape implied only |
| Gift-wrapped chocolate (5 style variants) | (176, 64) | 240x48 (5x 48x48) | Standard/discreet/festive/bold/party regalia |
| Branded shopping bag | (416, 64) | 48x64 | Tastefully branded, clutched at exit |
| Half-eaten anatomical (abstracted) | (176, 112) | 32x48 | The "someone always eats theirs" evidence sprite |
| Chocolate dust particles (3) | (208, 112) | 96x32 (3x 32x32) | Crafting window ambience |
| Warmth wave (2 frames) | (304, 112) | 128x64 (2x 64x64) | Rising from tempering station |

### Technical Notes:
- Anatomical items are silhouette + ribbon + wrapper reads — MA-appropriate abstraction, never explicit
- Inventory icons reuse case-stock sprites at native size (32-96px reads at UI scale)
- Full Collection box art changes case 3/4 contents to "sold out" state when purchased

---

## 🎀 Sprite Sheet 6: Effects & UI
**File:** `truffle_effects_ui.png`
**Dimensions:** 512x384 pixels

### Interface Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Zone indicator banner | (0, 0) | 128x32 | "Zone 1: Respectable / Zone 2: ...Hm / Zone 3: Committed" |
| Product selection browser | (128, 0) | 256x192 | Category tabs, price, Sophie's deadpan flavor text |
| Gift wrap options panel | (384, 0) | 128x128 | Five styles with implication captions |
| Purchase confirmation | (384, 128) | 128x96 | "It's YOUR chocolate." |
| Complicated Feelings status icon | (0, 32) | 32x32 | Post-consumption indicator (2 turns, no effect, just... there) |
| Complicated Feelings banner | (0, 64) | 96x32 | Status bar readout version |
| Truffle Collector badge | (0, 96) | 64x64 | Full-set achievement medal |
| Achievement track pips (6) | (64, 96) | 192x32 (6x 32x32) | Traditionalist/Interpreter/Committed/Distributor/Completionist/Human |
| Zone 3 realization vignette | (0, 224) | 256x128 | Screen-edge warm flush on first Zone 3 entry |
| "It's for someone else" declaration prompt | (256, 224) | 192x96 | Checkout gift-flag dialog (internal tracking begins) |
| Bravado tick pair | (448, 224) | 64x32 (2x 32x32) | Eye-contact wrap request vs. 5-minute "just browsing" |
| Touch highlight ring (44px min) | (0, 352) | 48x48 | Case/counter interaction indicator |

### Technical Notes:
- Zone 3 vignette is a one-shot overlay, 1.5s, warm pink — reduced-motion mode swaps to instant subtle tint
- Achievement pips light progressively; "Human" pip lights secretly when anyone eats a "gift" in private

---

## 🎬 Animation Specifications

### Sophie Crafting Loop (Sheets 2 & 3):
- **Duration:** 3 seconds per cycle (1 FPS)
- **Frames:** 3
- **Pattern:** Temper → shape → detail, continuous behind crafting window
- **Trigger:** Constant while shop loaded
- **Purpose:** Watching someone professionally craft chocolate anatomy is... something
- **Audio Sync:** Soft scrape/tap crafting foley on frames 1 and 3
- **Performance Optimization:** Static crafting frame on low LOD (per profile: "static crafting view")

### Customer Zone Drift (Sheets 1 & 4):
- **Duration:** Browse cycle 2 seconds (2 FPS); zone hesitation 3 seconds (0.7 FPS)
- **Frames:** 4 browse / 2 hesitation
- **Pattern:** Browse loop per zone → hesitation at Zone 2/3 threshold → commit stride or retreat
- **Trigger:** Ambient AI; player proximity pauses NPC decisions
- **Purpose:** The shop layout mirrors the customer's internal journey
- **Audio Sync:** None
- **Performance Optimization:** Max 3 concurrent customers, 2 on low-end

### Wrapping Sequence (Sheet 3):
- **Duration:** 2.4 seconds (1.25 FPS, 3 frames)
- **Frames:** 3
- **Pattern:** Fold → ribbon → handover, played once per purchase
- **Trigger:** Purchase confirmed with wrap style selected
- **Purpose:** The classy ritual applied to unclassy items
- **Audio Sync:** Paper crinkle frame 1, ribbon zip frame 2, register ding frame 3
- **Performance Optimization:** None needed

### Zone 3 Realization Vignette (Sheet 6):
- **Duration:** 1.5 seconds, played once per save file
- **Frames:** 1 (alpha ramp in/out)
- **Pattern:** Fade to 60% → hold 0.5s → fade out
- **Trigger:** First player entry into Zone 3
- **Purpose:** "The Moment" — when you realize the back section exists
- **Audio Sync:** Elegant Belgian café music continues, completely inappropriate (the joke is the non-reaction)
- **Performance Optimization:** Instant 30% tint, no ramp, for reduced motion

### Consumption & Complicated Feelings (Sheets 5 & 6):
- **Duration:** 1s eat + 1.5s extended pause + icon fade-in 0.5s
- **Frames:** Standard eat cycle + status icon
- **Pattern:** Eat → pause (nothing happens) → Complicated Feelings icon settles above head
- **Trigger:** Consuming any anatomical chocolate
- **Purpose:** +20-40 HP and thoughts
- **Audio Sync:** Standard eating sound, extended silence, tiny chime on icon
- **Performance Optimization:** None needed

### Chocolate Dust & Warmth (Sheet 5):
- **Duration:** 2-second drift loop
- **Frames:** 3 dust / 2 warmth
- **Pattern:** Rise and fade near tempering station
- **Trigger:** Constant near crafting window
- **Purpose:** Subtle boutique atmosphere per profile particle spec
- **Audio Sync:** None
- **Performance Optimization:** Disabled on low LOD

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Case outline set | (416, 128) in Sheet 5 reserve zone | 96x96 | Bold outlines for all six interactive cases |
| Counter/crafting window outline | (416, 176) in Sheet 5 reserve zone | 96x48 | Interactive-station highlight variants |
| Zone threshold markers | (448, 0) in Sheet 6 reserve | 64x64 | High-contrast floor arrows at zone doorways |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static crafting frame | Sheet 3 Row 1 frame 1 | 64x96 | Reduced-motion crafting window |
| Instant vignette tint | Sheet 6 vignette at fixed 30% | 256x128 | No fade ramp for Zone 3 moment |
| Static dust | Sheet 5 dust frame 1 | 32x32 | Non-drifting ambience |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Register ding icon | (48, 352) in Sheet 6 | 48x48 | Purchase completion mirror |
| Paper/ribbon crinkle glyphs | (96, 352) in Sheet 6 | 96x48 (2x 48x48) | Wrapping foley visualization |
| Café-music note marker | (192, 352) in Sheet 6 | 48x48 | Shows the inappropriately elegant soundtrack is playing |
| Eating-pause ellipsis bubble | (240, 352) in Sheet 6 | 48x48 | Visualizes the extended consumption silence |

### Colorblind Considerations:
- Zone coding uses banner text + lighting warmth + floor markers, never color alone
- Chocolate types (milk/dark/white) differ by value and label, not hue-only
- Wrap styles distinguished by pattern (plain/box/ribbon/transparent/regalia), not palette
- Touch zones minimum 44px for all cases, counter, wrap panel, and gift-flag prompt

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import); product sprites need higher quality (abstraction reads depend on clean silhouettes)
- **Fallback:** PNG high quality for truffle_effects_ui.png (text-heavy)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| truffle_environment | zone backdrops, fixtures | 2048x2048 |
| truffle_characters | Sophie/Niels, customers | 1024x512 |
| truffle_objects | products, effects, UI | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full crafting loop, dust/warmth particles, 3 concurrent customers, vignette ramp |
| Medium | 2-frame crafting, no dust, 2 customers |
| Low | Static crafting window, simplified case displays, 1 customer (per profile platform notes) |

### Performance Targets:
- **Target FPS:** 60 (per location profile budget)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 32 MB maximum
- **Particle Limit:** 10 (dust, warmth)

### Performance Notes:
- Single continuous interior scene — no scene swaps, camera scrolls across the three panels
- Case-content swap states are sprite region changes, not duplicate case art
- Customer pool of 4 rigs recycled with palette variation

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D backdrop panels + fixtures, AnimatedSprite2D (Sophie, Niels, customers), CPUParticles2D (dust — not GPU), CanvasLayer (browser UI, vignette overlay), Area2D zone-threshold triggers
- Special systems: zone-progression tracker (drives Bravado checks and achievement pips), "gift vs kept" ratio ledger with epilogue reveal hook, consumption tracker ("who ate theirs first"), Complicated Feelings status timer, Full Collection shop-state swap

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Crafting frames 1/3 | Scrape/tap foley | On frame display |
| Wrapping frames 1-3 | Crinkle → ribbon zip → register ding | Per frame |
| Zone 3 entry vignette | Café music continues unchanged | Deliberate non-sync (the joke) |
| Consumption pause | Eating SFX → 1.5s silence → tiny chime | Chime with status icon fade-in |
| Case open interaction | Glass case click | On browser open |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Truffle Collector (achievement track) | Achievement pips, Collector badge, Full Collection box | Purchase across all categories; staff "committed" recognition |
| "It's For Someone Else" ledger | Declaration prompt, wrap variants | Checkout gift-flag; epilogue reveals what happened to the "gifts" |
| The Chocolatier Observation | Crafting window, Sophie crafting loop | 30-second viewing; +Respect for the craft, +Dissonance |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Tolerance Hostel | Branded shopping bag visible in kitchen scene | Bag sprite reused as prop in hostel kitchen |
| Condomerie Het Gulden Vlies | Same-district awkwardness energy | Street adjacency, dialogue callbacks |
| Venustempel (Museum Mile) | Museum vs. retail contrast callbacks; Sophie's tempering critique of De Grote Fontein; same-day comparison dialogue | Dialogue only; no shared sprites. The Venustempel's Cacaogalerij and gift-shop chocolate line are the direct commercial rival — their pieces are authored on the Venustempel sheets, never reused here. |
| FEBO Automat | Post-chocolate late-night comparison | Dialogue only |
| Stroopwafel Cart | Comfort-food contrast | Status interaction (Comfort vs Complicated Feelings) |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "High-end Belgian boutique dignity, applied without blinking to anatomical novelty"
- **Color Mood:** Deep chocolate browns and Belgian gold under warm boutique light; Zone 3 adds velvet shadow and a blush of anatomical pink
- **Lighting:** Warm spots on every case as if each piece were a Fabergé egg; the crafting window glows like a stage
- **Texture:** Polished glass, satin ribbon, tempered-chocolate sheen — nothing here is cheap, which is exactly the problem

### Environmental Storytelling:
- The three-zone gradient tells the whole customer psychology arc without a word of dialogue
- The tiny "Yes, those are what you think they are" sign under elegant script signage is the shop's thesis
- Award plaques beside Case 3/4 insist on legitimacy — and they're real awards
- The half-eaten "gift" sprite appearing in later scenes is the game quietly confirming what everyone knew

### Character Integration Notes:
- Sophie never reacts to product shapes in any frame — her composure is load-bearing for the entire satire
- Niels's 2-pixel smirk is the only crack in the professionalism, and it's aimed at customers, never products
- Customers carry the embarrassment so the staff never have to; the shop itself remains serene
- Bachelor/bachelorette groups get collective-confidence poses — safety in numbers, rendered literally

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Zone 2 "wait—" moment** — abstract shapes mid-realization, perfectly ambiguous
2. **Sophie crafting through the window** — total artisan seriousness, unphotographable subject
3. **The Full Collection purchase** — 120 Sovs commitment with staff recognition
4. **The wrap-style menu** — "Discreet or... declarative?" as a UI screenshot
5. **Complicated Feelings icon** appearing over a character alone at night

### Quote Potential:
- "Chocolate is chocolate. Shape is creative expression. Together? Commerce."
- "The dark is more intense. In flavor. Obviously flavor."
- "We've made stranger. We've made MUCH stranger. We don't judge."
- "Bachelor Party Platter. For BRAD. Obviously. Not for me. For BRAD."
- "I found the other chocolate. I have questions. I'm eating it anyway."

---

## 📋 Required PNG Files (6 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | truffle_zone_backdrops.png | 1920x1080 |
| 2 | truffle_fixtures.png | 1024x768 |
| 3 | npc_sophie_bas.png | 320x480 |
| 4 | npc_truffle_customers.png | 640x288 |
| 5 | truffle_products.png | 512x256 |
| 6 | truffle_effects_ui.png | 512x384 |

**Total Estimated Memory:** ~13 MB uncompressed sprite data; fits ~32 MB location ceiling per profile budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `truffle_zone_backdrops.png` (1920x1080)
- [ ] `truffle_fixtures.png` (1024x768)
- [ ] `npc_sophie_bas.png` (320x480)
- [ ] `npc_truffle_customers.png` (640x288)
- [ ] `truffle_products.png` (512x256)
- [ ] `truffle_effects_ui.png` (512x384)

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
- **Backup:** Master PSD/layered file with organized layer groups (per-zone groups + abstraction-pass layer)
- **Documentation:** Animation timing reference sheet + abstraction guideline sign-off sheet (every product sprite reviewed against MA-rating standard)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: three-zone gradient, "Yes, those are what you think they are" sign, Sophie's unbroken composure, Complicated Feelings icon
- [ ] Accessibility visual alternatives included for all audio cues (register, wrapping foley, café music marker, consumption pause)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits
- [ ] Every product sprite passes the abstraction review — suggestive silhouette only, zero explicit detail

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (professionalism vs. product, denial vs. consumption)
- [ ] Hidden areas/interactions have discoverable visual cues (Zone 3 glow through doorway, crafting window spotlight)
- [ ] Performance optimized (single-scene scroll, CPU particles, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (zone text/pattern coding)
- [ ] Social media viral potential maximized in composition choices (wrap menu and Zone 2 shapes framed for screenshots)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam tourist district only; "trained in Brussels" is NPC backstory flavor, no real-city location |
| Cultural Specificity | ✅ | Belgian chocolate tradition meets Shamsterdam's openness economy |
| Satirical Targets Appropriate | ✅ | Gag-gift denial and bachelor party culture — body-positive framing, never body negativity |
| Seedy Underbelly Present | ✅ | 15 Sovs of chocolate sold for 35 Sovs because of the shape; shape-based markup economy |
| Gameplay Value Established | ✅ | Zone progression, consumption/status system, gift ledger, achievement track, Bravado checks |
| Technical Feasibility | ✅ | Single-scroll scene, static-crafting LOD, abstraction-friendly sprite sizes documented |
| Performance Budget | ✅ | 60 FPS, ≤14 draw calls, ≤32 MB per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all audio cues, reduced-motion variants, 44px touch zones |
| No Crypto Elements | ✅ | Pure artisan chocolate awkwardness (profile-confirmed) |
| Social Media Integration | ✅ | 5 screenshot moments identified; wrap-menu UI composed as shareable frame |

**Once these assets are delivered, The Awkward Truffle becomes Shamsterdam's most honest lie detector: a beautifully lit boutique where the player's zone progression, wrap choice, and 3 AM consumption record quietly say everything about them — with complimentary Complicated Feelings.**
