# De Stroopwafel Kar (The Stroopwafel Cart) - Complete PNG Asset Requirements

## 📋 Overview
De Stroopwafel Kar is Shamsterdam's mobile street-food landmark — a blue-and-white tiled three-wheeled cart where Tante Bep presses fresh stroopwafels for 8 Sovs that locals buy packaged for 2 Sovs, and the tourists are STILL right to pay it. This document specifies every PNG asset for the cart: three time-based location backdrops, the cart structure and equipment, Tante Bep and Mila NPC sheets, the customer cast, food/production sprites with steam and caramel effects, and the ordering UI. Its satirical essence in a sentence: the one tourist trap in Shamsterdam that delivers exactly what it promises, at five times the price.

**Location ID:** `shamsterdam_market_stroopwafel_cart_01`
**Theme:** Tourist pricing acceptance vs. genuine value; "authentic experience" markup satirized, the stroopwafel itself treated with total respect
**Zone:** De Kuipmarkt / mobile — Verdoemplein adjacent and Wandelpark entrance by time of day
**Hours:** 9 AM - 6 PM (market hours); cart relocates at 12 PM and 3 PM; packed up evenings
**Primary Function:** Street food vendor / comfort item source (Comfort + Sugar Rush statuses) / "Track the Cart" and "The Stroopwafel Trail" quests / Bravado interaction node

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Dutch Blue | #003DA5 | Cart tiles, awning stripes |
| Caramel Gold | #C9932A | Stroop, drips, warm glow accents |
| Cream White | #FFFDD0 | Cart panels, awning base, wax paper |
| Cart Wood | #DEB887 | Wheels, counter trim, chalk price board frame |
| Iron Steel | #6E7B8B | Waffle irons, caramel pot |
| Steam White | #F5F5F5 | Steam and warmth particles (alpha-heavy) |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/stroopwafel_cart/
├── environment/
│   ├── cart_location_backdrops.png
│   └── stroopwafel_cart_structure.png
├── npcs/
│   ├── npc_tante_bep_mila.png
│   └── npc_cart_customers.png
├── effects/
│   └── stroopwafel_food_effects.png
└── ui/
    └── stroopwafel_ui.png
```

---

## 🏪 Sprite Sheet 1: Location Backdrops (Time-Based)
**File:** `cart_location_backdrops.png`
**Dimensions:** 2048x1536 pixels
**Color Palette:** Global palette + per-location ambience (market bustle warm, square stone grey, park green)

### Backdrop Strips (2048x512 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| De Kuipmarkt entrance (9 AM-12 PM) | (0, 0) | 2048x512 | Market stalls, morning light, supermarket visible across the street (the joke lives in the background) |
| Verdoemplein adjacent (12 PM-3 PM) | (0, 512) | 2048x512 | Peak-tourist stone plaza, pigeons, tour groups mid-distance |
| Wandelpark entrance (3-6 PM) | (0, 1024) | 2048x512 | Park gate, afternoon gold light, cyclists passing lane |

### Technical Notes:
- Cart sprite (Sheet 2) is composited onto each backdrop at a fixed anchor; backdrops never include the cart itself
- Each strip scrolls horizontally max 1 screen; keep focal detail in center 1152px
- Supermarket signage in the market strip must be legible at gameplay zoom (price-comparison gag)

---

## 🛒 Sprite Sheet 2: Cart Structure & Equipment
**File:** `stroopwafel_cart_structure.png`
**Dimensions:** 1024x512 pixels

### Cart Body:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Full cart (front 3/4 view) | (0, 0) | 384x384 | Blue/white tiles, chrome trim, wood panels, three wheels, windmill + tulip decoration |
| Cart awning | (384, 0) | 256x128 | Blue/white striped, "VERSE STROOPWAFELS" banner |
| Price board | (640, 0) | 128x96 | "Klein 4 Sovs / Groot 8 Sovs", crossed-out "Local price: 2 Sovs", "Yes, They're Worth It" |
| Cash box | (768, 0) | 64x64 | Weathered, well-used, efficient |
| Card reader (with sigh) | (832, 0) | 48x64 | Mila's reluctant contraption |

### Production Equipment:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Waffle iron pair (closed) | (384, 128) | 192x128 | Two large circular irons, synchronized |
| Waffle iron (open, waffle inside) | (576, 128) | 96x128 | Press-cycle key frame |
| Caramel pot station | (672, 128) | 96x96 | Warm stroop, spreading implements |
| Batter container + dough balls | (768, 128) | 96x96 | Fresh portions ready |
| Warming rack (stocked) | (864, 128) | 128x96 | Finished stroopwafels staying warm |
| Splitting wire tool | (864, 224) | 64x32 | Sixty years of family practice |
| Front counter display | (0, 384) | 256x128 | Finished stroopwafels, klein/groot size comparison visible |
| Discount token ("Track the Cart" reward) | (256, 384) | 32x32 | One-time 2 Sovs off chip |
| Wax paper sleeve | (288, 384) | 48x48 | Handover wrapper |

### Technical Notes:
- Cart renders as one Sprite2D; equipment sprites overlay at fixed offsets so the press cycle can animate independently
- Price board is a separate sprite so the crossed-out local price can be zoomed for the reveal beat
- Cart reposition between locations is a fade-out/fade-in, not a driving animation (per profile mobile optimization)

---

## 👵 Sprite Sheet 3: Tante Bep & Mila
**File:** `npc_tante_bep_mila.png`
**Dimensions:** 384x480 pixels
**Sprite Size:** 64x96 pixels (6 columns x 5 rows)

### Tante Bep (rows 0-2):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Row 0: Idle at iron (2 frames) | (0, 0) | 128x96 | Apron, practical clothing, efficient hands at rest |
| Row 0: Taking order (2 frames) | (128, 0) | 128x96 | "Klein of groot?" head tilt |
| Row 1: Pressing cycle (4 frames) | (0, 96) | 256x96 | Ball → press → flip → lift, the visible theater |
| Row 1: Splitting with wire (2 frames) | (256, 96) | 128x96 | Horizontal split, sixty years of practice |
| Row 2: Spreading stroop (2 frames) | (0, 192) | 128x96 | Grandmother's recipe applied |
| Row 2: Serving handover (2 frames) | (128, 192) | 128x96 | Warm stroopwafel passed on wax paper |
| Row 2: Approving nod (1 frame) | (256, 192) | 64x96 | "Of course groot. You've learned." |

### Assistant Mila (rows 3-4):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Row 3: Idle prep (2 frames) | (0, 288) | 128x96 | Portioning batter, family resemblance |
| Row 3: Line management gesture (2 frames) | (128, 288) | 128x96 | "About ninety seconds. Worth the wait, promise." |
| Row 4: Card payment sigh (2 frames) | (0, 384) | 128x96 | Reader tap + small apologetic sigh |
| Row 4: Price-sign shrug (1 frame) | (128, 384) | 64x96 | "It's a joke. Sort of." |

### Technical Notes:
- Bep's press cycle is the location's hero animation — it must loop cleanly against the iron equipment overlay
- Bep and Mila are always both present; Mila handles queue-side interactions so Bep never breaks production rhythm
- No haggling animations exist by design — Bep has no time for that

---

## 🧍 Sprite Sheet 4: Customer NPCs & Queue
**File:** `npc_cart_customers.png`
**Dimensions:** 640x288 pixels
**Sprite Size:** 64x96 base (child 48x72)

### Row 0 (y=0):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Repeat Tourist (2 frames) | (0, 0) | 128x96 | Orders groot immediately, waits with zen patience |
| Food Blogger (2 frames) | (128, 0) | 128x96 | Ring light at a street cart, 20 photos of the process |
| Local Grabbing One (2 frames) | (256, 0) | 128x96 | Klein, exact change, gone in 30 seconds |
| Price Calculator Tourist (2 frames) | (384, 0) | 128x96 | Calculator app out, buys groot anyway |
| Child Experiencing Joy (2 frames) | (512, 0) | 96x72 (2x 48x72) | Caramel on face, "THIS IS THE BEST THING EVER" |

### Row 1 (y=96):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Queue block (3 waiting poses) | (0, 96) | 192x96 | Line of 1-3 customers, staggered anticipation |
| First-bite reaction (3 frames, shared rig) | (192, 96) | 192x96 | Pause → eyes widen → understanding achieved |
| Caramel-on-shirt shrug (1 frame) | (384, 96) | 64x96 | "There's stroop on my shirt. I don't care. Worth it." |

### Row 2 (y=192):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Generic walk-up cycle (4 frames) | (0, 192) | 256x96 | Tourists gravitating like moths to sweet, warm flame |
| Blogger crouch-for-angle (2 frames) | (256, 192) | 128x96 | "Can you do that split part again?" (denied) |
| Parent-and-child pair | (384, 192) | 128x96 | Escort sprite for the joy child |

### Technical Notes:
- Queue caps at 3 visible customers during tourist peaks, 0 off-peak (per profile queue system)
- First-bite reaction rig is shared by all customers AND the player party for the revelation beat
- Customer mix varies by backdrop: market = shoppers, square = peak tourists, park = local-ish

---

## 🧇 Sprite Sheet 5: Food & Effects
**File:** `stroopwafel_food_effects.png`
**Dimensions:** 512x256 pixels

### Food Sprites:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stroopwafel klein | (0, 0) | 48x48 | Small, still delicious |
| Stroopwafel groot | (48, 0) | 64x64 | The correct choice |
| Packaged supermarket stroopwafel | (112, 0) | 48x32 | The sad comparison, shrink-wrap shine |
| Production stages strip (4 stages) | (160, 0) | 256x64 (4x 64x64) | Press → split → fill → close |
| Half-eaten groot | (416, 0) | 64x64 | Bite radius, caramel strand |

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Iron steam plume (4 frames) | (0, 64) | 256x64 (4x 64x64) | Rising steam from press, alpha gradient |
| Caramel drip sparkle (3 frames) | (256, 64) | 96x32 (3x 32x32) | The stroop moment |
| Warmth wave rings (3 frames) | (352, 64) | 96x32 (3x 32x32) | 50-meter caramel-smell radius visualized |
| Comfort glow aura (2 frames) | (0, 128) | 128x64 (2x 64x64) | Warm glow around character while Comfort active |
| Sugar rush speed lines (2 frames) | (128, 128) | 128x64 (2x 64x64) | Large-size consequence |
| Fresh-steam wisp (2 frames) | (256, 128) | 128x64 (2x 64x64) | Off the just-served stroopwafel |
| Enlightenment sparkle burst (3 frames) | (0, 192) | 144x48 (3x 48x48) | "Fresh vs Packaged" revelation flash |

### Technical Notes:
- Steam is the location's only continuous particle system; cap at 12 concurrent quads
- Comfort glow is an additive-blend underlay behind the character sprite, not a shader
- Production stages strip doubles as the wait-timer illustration in the UI

---

## 🧾 Sprite Sheet 6: UI Elements
**File:** `stroopwafel_ui.png`
**Dimensions:** 512x256 pixels

### Interface Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Order selection panel | (0, 0) | 192x128 | Klein 4 Sovs / Groot 8 Sovs choice, groot subtly highlighted |
| Production wait timer | (192, 0) | 128x32 | 90 seconds of anticipation, iron icon fills |
| Comfort status icon | (192, 32) | 32x32 | Warm glow badge (3 or 5 turns) |
| Sugar Rush status icon | (224, 32) | 32x32 | Speed-boost lightning waffle |
| Enlightened status icon | (256, 32) | 32x32 | Packaged stroopwafels forever halved |
| Stroopwafel acquired popup | (192, 64) | 128x96 | Item obtained, warmth noted |
| Cart location map | (320, 0) | 192x128 | Three positions, time-based, "Track the Cart" progress pips |
| Bravado tick (up/down pair) | (320, 128) | 64x32 (2x 32x32) | Correct "groot" pronunciation vs. "how much in dollars" |
| Stroopwafel Connoisseur title card | (0, 128) | 192x64 | "The Stroopwafel Trail" quest reward banner |
| Touch highlight ring (44px min) | (0, 192) | 48x48 | Cart interaction indicator |

### Technical Notes:
- Wait timer must feel pleasurable, not annoying — fill animation eases with the press-cycle rhythm
- Location map pips light in visit order for the one-day Trail quest

---

## 🎬 Animation Specifications

### Iron Press Cycle (Sheets 2, 3, 5):
- **Duration:** 3 seconds per cycle (Bep at ~1.3 FPS across 4 frames)
- **Frames:** 4 (Bep) + iron open/closed overlays
- **Pattern:** Ball placed → press down → hold/sizzle → lift, continuous while cart active
- **Trigger:** Constant during open hours; syncs to order timer when player waits
- **Purpose:** The visible theater — 90 seconds of craft justifying 8 Sovs
- **Audio Sync:** Sizzle on press-down frame; iron clank on lift
- **Mobile Optimization:** Cycle halves to 2 key frames on low LOD

### Steam Plume (Sheet 5):
- **Duration:** 2 seconds per loop (2 FPS)
- **Frames:** 4
- **Pattern:** Rise → drift → dissipate → respawn, continuous
- **Trigger:** Constant from active iron; burst on iron lift
- **Purpose:** Warmth radius that pulls NPCs (and players) toward the cart
- **Audio Sync:** None (ambient sizzle covers it)
- **Mobile Optimization:** Simplified 2-frame steam, half spawn rate

### Splitting & Filling (Sheet 3):
- **Duration:** 2 seconds (2 FPS across split + spread rows)
- **Frames:** 4 total (2 split, 2 spread)
- **Pattern:** Wire split → open → stroop spread → close, played once per order
- **Trigger:** Order timer reaches 60s mark
- **Purpose:** "Watch. See how I split it?" — the craft close-up
- **Audio Sync:** Soft wire shear; caramel pour smear
- **Mobile Optimization:** None needed

### First-Bite Revelation (Sheets 4, 5):
- **Duration:** 2.5 seconds (pause 1s → 3 frames at 2 FPS → sparkle)
- **Frames:** 3 + 3 sparkle
- **Pattern:** Freeze → widen → melt → Enlightenment sparkle, played once per character
- **Trigger:** First fresh consumption after any packaged stroopwafel
- **Purpose:** "All those packaged ones were LIES. BEAUTIFUL LIES."
- **Audio Sync:** Ambient dips to near-silence during pause, warm chord on sparkle
- **Mobile Optimization:** Sparkle burst drops to 1 frame

### Comfort Glow (Sheet 5):
- **Duration:** 3-second gentle pulse loop
- **Frames:** 2
- **Pattern:** Soft in/out while Comfort status active (3-5 turns)
- **Trigger:** Fresh stroopwafel consumed
- **Purpose:** "The warmth stays with you, inside and out"
- **Audio Sync:** None
- **Mobile Optimization:** Static 40%-opacity glow on reduced motion

### Cart Relocation Fade (Sheets 1, 2):
- **Duration:** 1.5 seconds out + 1.5 seconds in
- **Frames:** Alpha fade only
- **Pattern:** Fade cart at old anchor → backdrop swap → fade in at new anchor
- **Trigger:** Game clock crossing 12 PM / 3 PM
- **Purpose:** Mobile cart system without driving animation cost
- **Audio Sync:** Distant bicycle bell + market ambience crossfade
- **Mobile Optimization:** None needed (already the optimization)

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cart outline variant | (336, 384) in Sheet 2 reserve zone | 192x128 | Bold-outline cart silhouette so the vendor reads in high-contrast mode |
| Price board large-text variant | (528, 384) in Sheet 2 reserve zone | 128x96 | Enlarged Klein/Groot text, crossed-out price kept legible |
| Order-choice outline buttons | (48, 192) in Sheet 6 | 96x48 (2x 48x48) | High-contrast klein/groot selectors |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static steam sprite | Sheet 5, (192, 192) | 64x64 | Non-animated steam for reduced-motion mode |
| Static comfort glow | Sheet 5, (256, 192) | 64x64 | Constant soft aura, no pulse |
| Sugar rush icon only | Sheet 6 status icon | 32x32 | Speed lines suppressed; status shown by icon alone |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sizzle icon | (320, 192) in Sheet 5 | 32x32 | Visual mirror of press sizzle |
| Iron clank marker | (352, 192) in Sheet 5 | 32x32 | Lift-clank visualization |
| Bicycle bell pip | (384, 192) in Sheet 5 | 32x32 | Relocation ambience cue |
| Warm chord glyph | (416, 192) in Sheet 5 | 32x32 | Revelation-moment audio mirrored visually |

### Colorblind Considerations:
- Klein/groot are size-coded and text-labeled, never color-coded
- Status icons (Comfort/Sugar Rush/Enlightened) use distinct silhouettes, not palette swaps
- Crossed-out local price uses strikethrough + label, not red-only signaling
- Touch zones minimum 44px for order buttons, cart interaction, and map pips

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC (fallback PVRTC 4BPP); price board and backdrop supermarket signage need higher quality (readable gag text)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for stroopwafel_ui.png (text) and food close-ups

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| cart_environment | backdrops (streamed per time slot), cart structure | 2048x2048 |
| cart_characters | Bep/Mila, customers | 1024x512 |
| cart_effects | food, effects, UI | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full press cycle, 4-frame steam, comfort/sugar auras, 3-customer queue |
| Medium | 2-frame steam, reduced queue to 2, half particle rate |
| Low | Static cart with key-frame press only, static backdrops, no steam particles (per profile) |

### Performance Targets:
- **Target FPS:** 60 (per location profile budget)
- **Max Draw Calls:** 12 per frame
- **Memory Footprint:** 30 MB maximum
- **Particle Limit:** 12 (steam, drips)

### Performance Notes:
- Only one backdrop strip resident at a time (time-slot streaming)
- Cart relocation is a fade, never a traversal — no vehicle pathing cost
- Customer NPC pool of 5 rigs recycled across all three locations

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D backdrop + cart, AnimatedSprite2D (Bep, Mila, customers, iron overlays), CPUParticles2D (steam — not GPU), CanvasLayer (order UI, timer)
- Special systems: game-clock relocation scheduler (9/12/3 slots), 90-second order timer bound to press-cycle animation, "Enlightened" permanent flag, gift/consumption status stacker (Comfort + Sugar Rush), Bravado pronunciation check hook

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Press-down frame | Iron sizzle | On frame 2 of press cycle |
| Iron lift frame | Metal clank + steam burst | On frame 4 |
| Wire split frames | Soft shear | Frame 1 of split |
| Serving handover | Wax paper crinkle | On handover frame 2 |
| First-bite pause | Ambience duck → warm chord | Chord lands with sparkle frame 1 |
| Relocation fade | Bicycle bell + ambience crossfade | Bell at fade-out midpoint |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Track the Cart | Cart location map pips, discount token | Visit all three locations; one-time 2 Sovs off token |
| The Stroopwafel Trail (time-limited) | Map pips + Connoisseur title card | All three locations in one day; free groot next visit |
| Stroopwafel Wisdom (achievement) | Enlightenment sparkle, Enlightened icon | Buy fresh after having packaged; permanent vendor-discount look |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Pancake House | Comparison dialogue callbacks (8 Sovs well-spent vs 18 Sovs regret) | Post-Pancake Disappointment status interacts with Comfort |
| De Groene Gids | Enhanced-appreciation state ("This is like CLOUDS") | Space Cake Effect modifies first-bite reaction text |
| De Kuipmarkt | Market backdrop strip shared with market zone | Cart anchored at market entrance mornings |
| FEBO Automat | Comfort-food network contrast (3 AM vs daytime) | Dialogue references only, no shared sprites |
| Supermarket (any) | Packaged stroopwafel sprite | The sad comparison item sold elsewhere |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Maximum Dutch-ness deployed honestly — the trap that isn't lying"
- **Color Mood:** Dutch blue and cream warmth with caramel gold as the emotional center; everything near the irons glows
- **Lighting:** Natural outdoor light per time slot (morning market, noon stone glare, golden park afternoon) + constant warm halo at the irons
- **Texture:** Glazed tile, worn wood, chrome polished by thirty years of hands; steam softens every edge

### Environmental Storytelling:
- The crossed-out "Local price: 2 Sovs" on the board tells the entire satire in four words
- Supermarket visible across the street in the market backdrop — the cheaper option is never hidden
- The warming rack is always stocked but the line still waits for fresh — the product earns its markup on screen
- Windmill and tulip decoration is deliberate tourist-bait maximalism, and Bep knows it

### Character Integration Notes:
- Tante Bep never leaves the iron station; her production rhythm is the location's heartbeat
- Mila handles all queue-facing interaction so Bep's animation loop stays unbroken
- Customer cast rotates per time slot; the Child Experiencing Joy is the emotional thesis sprite
- The player's first-bite uses the same shared reaction rig as NPCs — everyone is equal before fresh stroop

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The price board** — "Klein 4 Sovs / Groot 8 Sovs" over crossed-out "Local price: 2 Sovs" and "Yes, They're Worth It"
2. **The split-and-fill close-up** — production stages strip is pure process-video bait
3. **First-bite freeze frame** — the party's synchronized revelation faces
4. **Child Experiencing Joy** — caramel-faced pure happiness beside price-calculating adults
5. **Steam-wreathed cart at golden hour** — Wandelpark backdrop postcard shot

### Quote Potential:
- "Groot is better. Fresh, more caramel. Same love, bigger joy."
- "The stroop is my grandmother's recipe. The price is my landlord's recipe."
- "Yes, it's eight Sovs. Yes, I know the supermarket. No, it's not the same."
- "Wait. WAIT. This is what they were SUPPOSED to taste like?"
- "Every stroopwafel is ninety seconds of my life. That's worth eight Sovs. My life, your snack."

---

## 📋 Required PNG Files (6 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | cart_location_backdrops.png | 2048x1536 |
| 2 | stroopwafel_cart_structure.png | 1024x512 |
| 3 | npc_tante_bep_mila.png | 384x480 |
| 4 | npc_cart_customers.png | 640x288 |
| 5 | stroopwafel_food_effects.png | 512x256 |
| 6 | stroopwafel_ui.png | 512x256 |

**Total Estimated Memory:** ~16 MB uncompressed sprite data; fits ~30 MB location ceiling per profile budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `cart_location_backdrops.png` (2048x1536)
- [ ] `stroopwafel_cart_structure.png` (1024x512)
- [ ] `npc_tante_bep_mila.png` (384x480)
- [ ] `npc_cart_customers.png` (640x288)
- [ ] `stroopwafel_food_effects.png` (512x256)
- [ ] `stroopwafel_ui.png` (512x256)

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
- **Backup:** Master PSD/layered file with organized layer groups (per-time-slot backdrop groups)
- **Documentation:** Animation timing reference sheet + press-cycle/order-timer sync chart

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: crossed-out local price, visible supermarket, klein/groot size comparison, first-bite revelation
- [ ] Accessibility visual alternatives included for all audio cues (sizzle, clank, bell, revelation chord)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (markup satirized, stroopwafel respected)
- [ ] Hidden areas/interactions have discoverable visual cues (Trail map pips, discount token)
- [ ] Mobile performance optimized (CPU particles, time-slot streaming, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (size/text coding, distinct status silhouettes)
- [ ] Social media viral potential maximized in composition choices (price board framing, process strip)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam only. Zone names are fully in-world: De Kuipmarkt, Verdoemplein, Wandelpark |
| Cultural Specificity | ✅ | Dutch stroopwafel tradition treated as genuine cultural treasure |
| Satirical Targets Appropriate | ✅ | Tourist pricing acceptance — never the food, never the vendors |
| Seedy Underbelly Present | ✅ | 5x tourist markup with a smile, cart strategically stalking tourist peaks (mildest vice in Shamsterdam by design) |
| Gameplay Value Established | ✅ | Comfort/Sugar Rush economy, two cart quests, Bravado checks, Enlightened flag |
| Technical Feasibility | ✅ | Fade-based relocation, streamed backdrops, 12-particle cap documented |
| Mobile Performance Budget | ✅ | 60 FPS, ≤12 draw calls, ≤30 MB per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all audio cues, reduced-motion variants, 44px touch zones |
| No Crypto Elements | ✅ | Pure traditional street food (profile-confirmed) |
| Social Media Integration | ✅ | 5 screenshot moments identified, process-video composition built in |

**Once these assets are delivered, De Stroopwafel Kar becomes the emotional counterweight of Shamsterdam: the one place where the bros overpay by 5x and the game, the vendor, and the player all agree they were completely right to do it.**
