# The Connoisseur's Cache - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for The Connoisseur's Cache — Sinfonia's general item shop where healing items are "artisanal," weapons are "collectibles," and every purchase comes with a certificate of authenticity you didn't ask for. It's a gift shop pretending to be a gallery pretending to be essential: the tea works, the pain relief works, but you're paying for the STORY, delivered in an unskippable 30–60 second provenance speech by a shopkeeper who genuinely believes he's enriching your life.

**Location ID:** `sinfonia_kaffeehausrow_connoisseurs_cache_01`
**Theme:** Premium retail narrative and "curated" culture — Viennese museum-shop pretension where ordinary items become special through presentation, provenance, and paperwork
**Zone:** Kaffeehaus Row, Intellectual Café District
**Hours:** 09:00–20:00 (refined hours; the shopkeeper will explain the provenance of EVERYTHING)
**Primary Function:** General item shop (consumables / support / weapons / utilities / specialty goods) — provenance speech mechanic, certificate system, Discerning Customer progression (200 Sovs spent unlocks speech-skip and the locked specialty cabinet), selfie spot

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Library Brown | #5D4037 | Wooden shelving, walnut paneling, floors, counter |
| Refined Gold | #B8860B | Gilding, frames, certificate seals, cabinet hardware |
| Paper Cream | #FFF8E1 | Placards, certificates, wall plaster, lamplight |
| Intellectual Green | #2E5D4B | Velvet display cloth, reading-nook upholstery, awning |
| Provenance Burgundy | #6D2E3C | Persian rug, wax seals, ribbon accents |
| Brass Patina | #8C7853 | Bell, register, lamp fittings, cabinet key |
| Ink Black | #1F1B18 | Calligraphy, Kurator's vest, signage lettering |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/connoisseurs_cache/
├── environment/
│   └── connoisseurs_cache_tileset.png
├── npcs/
│   ├── herr_kurator.png
│   └── connoisseurs_cache_npcs.png
├── objects/
│   └── connoisseurs_cache_items.png
├── effects/
│   └── connoisseurs_cache_certificate_effects.png
└── ui/
    ├── connoisseurs_cache_ui.png
    └── connoisseurs_cache_accessibility.png
```

---

## 🏪 Sprite Sheet 1: Shop Tileset & Zones
**File:** `connoisseurs_cache_tileset.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #5D4037 (Library Brown), #FFF8E1 (Paper Cream), #B8860B (Refined Gold), #2E5D4B (Intellectual Green)

### Floor Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Parquet Floor | (0, 0) | 32x32 | Herringbone walnut, gallery polish |
| Parquet Worn | (32, 0) | 32x32 | Browsing-path wear in front of displays |
| Persian Rug Center | (64, 0) | 32x32 | Burgundy with gold medallion |
| Persian Rug Border | (96, 0) | 32x32 | Fringed gold-trimmed edge |
| Reading Nook Carpet | (128, 0) | 32x32 | Deep green, plush pile |
| Marble Threshold | (160, 0) | 32x32 | Entrance strip, "wipe your feet" pristine |

### Wall Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Walnut Panel | (0, 32) | 32x64 | Dark wainscoting with grain detail |
| Cream Plaster Upper | (32, 32) | 32x64 | Aged paper-cream wall above wainscot |
| Wainscot Cap Gilded | (64, 32) | 32x64 | Gold molding strip on panel top edge |
| Gilded Frame | (96, 32) | 64x64 | Empty museum frame for rotating "exhibits" |
| Gallery Spotlight Fixture | (160, 32) | 32x64 | Brass track light angled at displays |
| Oil Portrait (Stern Ancestor) | (192, 32) | 48x64 | Unidentified aristocrat; placard says "Provenance: Unquestioned" |

### Fixtures & Furniture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wooden Shelf Section | (0, 96) | 64x48 | Open shelving, items spaced like exhibits |
| Glass Display Case | (64, 96) | 48x48 | For "special" items, brass corners |
| Velvet Display Pedestal | (112, 96) | 32x48 | Green velvet drape, single-item shrine |
| Service Counter Section | (144, 96) | 64x48 | Walnut with brass rail, no visible prices anywhere |
| Brass Register | (208, 96) | 32x48 | Antique, elegant chime, judgmental gleam |
| Reading Armchair | (240, 96) | 32x48 | Green leather, the obligation trap |
| Reading Lamp | (272, 96) | 16x48 | Warm glow pool for the nook |

### Zone Backdrops:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Floor Display Wall | (0, 144) | 224x96 | Museum-style shelving run, placard beside every item |
| Healing Alcove | (224, 144) | 160x96 | Artisanal remedies, hanging herb bundles, apothecary jars |
| Implements Corner | (384, 144) | 160x96 | "Collectible" weapons on velvet, framed provenance certificates ("Not for violence — for appreciation") |
| Reading Nook | (544, 144) | 160x96 | Guidebooks, armchairs, "Curated Selections" sign (selfie spot) |
| Window Display (Interior View) | (704, 144) | 128x96 | Selective items with handwritten significance cards |

### Specialty Cabinet & Entry:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Specialty Cabinet Locked | (0, 240) | 64x96 | Glass case, brass lock, contents tantalizingly visible |
| Specialty Cabinet Denied Shimmer | (64, 240) | 64x96 | Locked state + polite refusal gleam (pre-Discerning) |
| Specialty Cabinet Unlocking | (128, 240) | 64x96 | Kurator's key inserted, door swinging |
| Specialty Cabinet Open | (192, 240) | 64x96 | Interior lit, rotating event stock visible |
| Front Door with Brass Bell | (256, 240) | 32x64 | Wooden door, bell above, calligraphy "Open" sign |
| Calligraphy Open Sign | (288, 240) | 24x32 | Standalone flip state for closed hours |
| Storefront Façade | (320, 240) | 192x96 | Exterior: curated window, "The Connoisseur's Cache — Curated Goods for Cultivated Tastes" |

### Small Props & Placards:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Placard Blank | (0, 336) | 16x12 | Handwritten descriptive card, cream |
| Placard Long | (16, 336) | 24x12 | Two-line significance card |
| "Price Upon Inquiry" Card | (40, 336) | 16x12 | The judgment-summoning card |
| Herb Bundle | (56, 336) | 16x16 | Alcove hanging dressing |
| Teapot Display | (72, 336) | 16x16 | Heritage Herbal Tea shrine centerpiece |
| Complimentary Bookmark | (88, 336) | 8x16 | Given whether you want one or not |
| Thank-You Card | (96, 336) | 16x12 | Accompanies every receipt |
| Business Card | (112, 336) | 16x12 | Embossed, naturally |
| Wrapped Parcel | (128, 336) | 16x16 | Packaging that required a second purchase |
| Brass Bell (Detail) | (144, 336) | 8x8 | Door chime close-up element |
| "Not a Gift Shop. An Experience." Sign | (152, 336) | 48x16 | Window signage, ink-black calligraphy |

### Technical Notes:
- Diffused gallery lighting baked into zone backdrops — everything must look IMPORTANT
- Velvet surfaces get subtle green-on-green texture; placards must read as handwritten at game resolution
- Specialty cabinet states are texture swaps driven by Discerning Customer flag, zero runtime cost
- No price tags anywhere in the environment art — this is a load-bearing joke

---

## 🎩 Sprite Sheet 2: Herr Kurator (The Shopkeeper)
**File:** `herr_kurator.png`
**Dimensions:** 384x288 pixels
**Color Palette:** #1F1B18 (Ink Black vest), #FFF8E1 (Shirt), #B8860B (Watch chain), #5D4037 (Trousers)

### Idle & Retrieval States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Idle | (0, 0) | 48x96 | Wire-rim glasses, vest with watch chain, hands clasped, perpetually ready |
| Idle Blink | (48, 0) | 48x96 | Blink frame; glasses glint |
| Retrieval Frame 1 | (96, 0) | 48x96 | Reaching toward shelf with visible reverence |
| Retrieval Frame 2 | (144, 0) | 48x96 | Lifting item with both hands, breath held |
| Retrieval Frame 3 | (192, 0) | 48x96 | Presenting item on open palms like a relic |

### Provenance Speech States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Passionate Frame 1 | (240, 0) | 48x96 | Speech begins, finger raised — "This blend dates to 1847—" |
| Passionate Frame 2 | (288, 0) | 48x96 | Sweeping gesture, item still cradled |
| Passionate Frame 3 | (336, 0) | 48x96 | Eyes closed, rapture — the lunar cycle portion |
| Passionate Frame 4 | (0, 96) | 48x96 | Crescendo, both hands aloft — "You're buying CONTINUITY." |

### Recognition & Transaction States (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Approving Nod Frame 1 | (48, 96) | 48x96 | Chin dipping, eyes softening — Discerning Customer recognized |
| Approving Nod Frame 2 | (96, 96) | 48x96 | Held nod — "You've grown." |
| Certificate Handing Frame 1 | (144, 96) | 48x96 | Certificate raised in both hands |
| Certificate Handing Frame 2 | (192, 96) | 48x96 | Extended to player — "It's as important as the item itself." |
| Pained Smile | (240, 96) | 48x96 | Reaction to "healing stuff" — "Yes. We have... remedies." |
| Eyes-Light-Up Delight | (288, 96) | 48x96 | A TRUE connoisseur asked about the Opera Glasses |
| Price Inquiry Judgment | (336, 96) | 48x96 | You asked the price. He answers. His eyebrows answer too. |

### Detail Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pocket Watch on Chain | (0, 192) | 16x16 | Close-up detail; consulted, never rushed |
| Wire-Rim Glasses Glint | (16, 192) | 16x16 | Overlay glint for delight state |
| Certificate in Hand | (32, 192) | 24x32 | Cream paper, gold seal, held delicately |
| Fountain Pen | (56, 192) | 8x24 | For the signature on every certificate |
| Cabinet Key on Chain | (64, 192) | 16x24 | The only key; produced ceremonially |
| White Gloves | (80, 192) | 16x16 | Donned for specialty cabinet retrievals |
| Speech Gesture Hands Set | (96, 192) | 48x32 | Detached hand poses for dialogue-portrait compositing |

### Technical Notes:
- Posture is KEY: never hurried, always holding something carefully — even his idle should suggest an item just handled
- Passionate frames loop for the full 30–60 second speech duration; the loop must not feel impatient because HE never is
- Approving nod is the game's most earned two frames — hold timing matters more than motion

---

## 😶 Sprite Sheet 3: The Browser & Ambient
**File:** `connoisseurs_cache_npcs.png`
**Dimensions:** 256x128 pixels
**Color Palette:** #5D4037 (Coat), #FFF8E1 (Face pallor), #6D2E3C (Scarf)

### The Browser — Trapped Customer (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Polite Nod Frame 1 | (0, 0) | 48x96 | Mid-provenance speech, nodding — "Mm-hmm. Yes. Fascinating." |
| Polite Nod Frame 2 | (48, 0) | 48x96 | Nod continues; soul departing |
| Glazed Stare | (96, 0) | 48x96 | Eyes unfocused — "The lunar cycle, you say?" |
| Desperate Eye Contact | (144, 0) | 48x96 | Locks eyes with the player — "Help me." |
| Escape Shuffle | (192, 0) | 48x96 | One foot angled at the door, body still politely facing Kurator |

### Ambient Glyphs:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Desperate Sigh Glyph | (0, 96) | 16x16 | Small exhale wisp above Browser's head |
| "Help me." Speech Bubble | (16, 96) | 48x24 | Tiny, urgent, easily missed — the gag rewards attentive players |
| Nodding Motion Lines | (64, 96) | 16x16 | Overlay arcs for the nod loop |

### Technical Notes:
- The Browser NEVER escapes; the escape shuffle loops back to polite nodding
- Desperate Eye Contact fires only when the player's sprite is within line-of-sight — a shared moment
- Keep his palette drab against the shop's warmth: he is the only unenriched object in the room

---

## 🫖 Sprite Sheet 4: The Curated Inventory (Item Sprites)
**File:** `connoisseurs_cache_items.png`
**Dimensions:** 256x256 pixels
**Color Palette:** Full global palette; each item over-packaged relative to contents

### Artisanal Remedies (Healing):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Artisanal Pain Relief | (0, 0) | 32x32 | +50 HP — apothecary jar, "hand-pressed herbs from Alpine monasteries" |
| Gourmet Energy Bar | (32, 0) | 32x32 | +30 HP / +10 SP — single-origin cacao, wrapper nicer than most books |
| Heritage Herbal Tea | (64, 0) | 32x32 | +20 HP, cures status — tin unchanged since 1847 (except the lost year) |
| Mineral Water (Imported) | (96, 0) | 32x32 | +15 HP, cures Thirsty — "from a spring that inspired Beethoven" |
| Rejuvenation Elixir | (128, 0) | 32x32 | Full HP restore — wax-sealed bottle, family-secret formula |

### Tall-Format Items:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Restorative Tincture | (0, 32) | 32x48 | +75 HP — dropper bottle, seven-generation apothecary label |
| Conductor's Baton | (32, 32) | 32x48 | Weapon: +3 Charm, chance to Confuse — "allegedly touched by Strauss," displayed vertically on velvet |
| Art Appreciation Guide | (64, 32) | 32x48 | +10% Culture stat — gilt-spined volume |
| Etiquette Guidebook | (96, 32) | 32x48 | Reduces social combat difficulty — "the complete rules, annotated" |
| Weighted Walking Cane | (128, 32) | 32x48 | Weapon: moderate damage, +2 Style — "Conceals nothing. Officially." |

### Cultural Enhancement (Support):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Classical Music CD | (0, 80) | 32x32 | +15% Focus (2 hours) — jewel case, liner notes longer than the album |
| Meditation Incense | (32, 80) | 32x32 | Restores SP over time — bundled sticks, ribbon-tied |
| Pocket Philosopher | (64, 80) | 32x32 | +20% Dialogue combat — small book of witty responses |
| Language Phrasebook | (96, 80) | 32x32 | Reduces pronunciation penalties — dog-eared by design |
| Calling Cards (Set of 20) | (128, 80) | 32x32 | +5% NPC first impressions — embossed, naturally |

### Collectibles With Purpose (Weapons):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Opera Glasses | (0, 112) | 32x32 | Ranged advantage, +2 Perception — "used by a Countess at the premiere of Don Giovanni" |
| Letter Opener (Ornate) | (32, 112) | 32x32 | Quick attack, low damage — "from a diplomat's desk, circa 1890" |
| Antique Lorgnette | (64, 112) | 32x32 | Thrown weapon, single use — "Too valuable to throw. But you could." |
| Masquerade Mask (Basic) | (96, 112) | 32x32 | Required for Baroness' Ballroom — "carnival style, locally made" |

### Large-Format Items:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Masquerade Mask (Ornate) | (0, 144) | 48x48 | +2 Mystery at masquerades — "actual carnival import," gold filigree |
| Art Authentication Kit | (48, 144) | 48x48 | Detect all forgeries — velvet-lined case of loupes and swabs |

### Documents & Specialty:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Formal Event Invitation | (0, 192) | 48x32 | Access to one formal event — "transferable, untraceable" |
| Dance Lesson Voucher | (48, 192) | 48x32 | +15% Dance skill permanently — specialty cabinet stock |
| VIP Opera Pass | (96, 192) | 48x32 | Backstage access at Bassline — season pass on a lanyard it's embarrassed by |
| Baroness' Favor Token | (144, 192) | 32x32 | +1 starting reputation at Ballroom — enameled crest |
| Forged Invitation | (176, 192) | 48x32 | Access anywhere, 10% detection risk — visually identical to the Formal Invitation except one flourish, sold from under the counter |

### Status & Extras:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Discerning Customer Badge | (0, 224) | 32x32 | Status indicator — gold laurel, worn knowledge |
| Certificate (Rolled) | (32, 224) | 32x32 | Inventory form of every certificate; you will see MANY |
| Gift Wrapping (Second Purchase) | (64, 224) | 32x32 | The packaging you had to buy to carry the packaging |
| Complimentary Bookmark (Inventory) | (96, 224) | 16x32 | Unremovable. He insists. |

### Technical Notes:
- Every item sprite includes its placard shadow when rendered in-shop (placards from Sheet 1 composited beside)
- Forged Invitation and Formal Event Invitation must differ by exactly one visual flourish — players who notice feel clever
- Weapons drawn as display pieces, not armaments: velvet context, museum lighting

---

## 📜 Sprite Sheet 5: Certificates & Effects
**File:** `connoisseurs_cache_certificate_effects.png`
**Dimensions:** 256x192 pixels
**Color Palette:** #FFF8E1 (Paper Cream), #B8860B (Gold seal), #6D2E3C (Wax), #1F1B18 (Ink)

### The Certificate:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Certificate Template | (0, 0) | 96x64 | Full readable layout: item name, date, authenticity guarantee, serial number (yes, for tea), Kurator's signature |
| Stamp Raised | (96, 0) | 32x32 | Brass hand-stamp lifted, poised |
| Stamp Descending | (128, 0) | 32x32 | Mid-strike blur |
| Stamp Impact | (160, 0) | 32x32 | Contact with authority burst |
| Stamped Seal Result | (192, 0) | 32x32 | Gold-embossed seal on paper |

### Shop Animation Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Page Turn Frame 1 | (0, 64) | 32x32 | Reading nook book, page lifting |
| Page Turn Frame 2 | (32, 64) | 32x32 | Page arcing |
| Page Turn Frame 3 | (64, 64) | 32x32 | Page settling |
| Cabinet Unlock Glow | (96, 64) | 64x64 | Gold radiance when the specialty cabinet opens — heaven, retail edition |
| Dust Motes in Light Beam | (160, 64) | 64x64 | Floating particles in gallery spotlight |

### Ambience & Gag Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gallery Spotlight Cone | (0, 128) | 32x48 | Diffused importance-conferring beam |
| Candle Flicker Frame 1 | (32, 128) | 16x24 | Reading nook candle |
| Candle Flicker Frame 2 | (48, 128) | 16x24 | Alternate flame lean |
| Register Chime Sparkle | (64, 128) | 24x24 | Elegant chime visual — a single tasteful glint |
| Clock Pendulum Frame 1 | (88, 128) | 24x32 | Wall clock, pendulum left — time passing during speeches |
| Clock Pendulum Frame 2 | (112, 128) | 24x32 | Pendulum right |
| Certificate Flutter Frame 1 | (136, 128) | 16x24 | Falling paper — inventory overflow gag |
| Certificate Flutter Frame 2 | (152, 128) | 16x24 | Mid-tumble |
| Certificate Flutter Frame 3 | (168, 128) | 16x24 | Settling to floor |
| Wax Seal Glint | (184, 128) | 16x16 | Specular ping on fresh seals |

### Technical Notes:
- Certificate template must be legible enough to screenshot — the serial number for tea is a shareable joke
- Dust motes are the only looping ambient particle system; budget accordingly (see Mobile Optimization)
- Clock pendulum runs ONLY during provenance speeches — its appearance is the comedy cue

---

## 🖥️ Sprite Sheet 6: Shop UI
**File:** `connoisseurs_cache_ui.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #5D4037 (Frames), #B8860B (Gold trim), #FFF8E1 (Card faces), #1F1B18 (Text)

### Shop Interface — Placard Cards:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Placard Item Card Frame | (0, 0) | 160x96 | Museum-placard-styled item card: name, provenance line, effect — price appears only after you ask |
| Tab: Artisanal Remedies | (160, 0) | 48x24 | Teacup icon |
| Tab: Cultural Enhancement | (160, 24) | 48x24 | Book icon |
| Tab: Collectible Implements | (160, 48) | 48x24 | Opera glasses icon |
| Tab: Practical Sophistication | (160, 72) | 48x24 | Mask icon |
| Tab: Specialty (Locked) | (208, 0) | 48x24 | Cabinet icon with brass lock |
| Tab: Specialty (Unlocked) | (208, 24) | 48x24 | Cabinet icon, open, gold glow |
| "Inquire" Price Button | (208, 48) | 48x24 | Asking is an act of courage |
| Judgment Glare Icon | (208, 72) | 24x24 | Appears beside price after inquiring |

### Provenance Speech UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Provenance Speech Panel | (0, 96) | 200x64 | Dialogue frame with gold scrollwork — the speech box you cannot close |
| Clock Ticking Frame 1 | (200, 96) | 32x32 | UI clock face, hand at tick — mocks the player with real time passing |
| Clock Ticking Frame 2 | (232, 96) | 32x32 | Hand at tock |
| Time-Passing Glyph | (264, 96) | 24x24 | Small hourglass wisp beside the clock |
| Skip Button (Locked) | (200, 128) | 56x24 | Grayed "Skip" — tooltip: "That would be rude." |
| "The usual, please." Button (Unlocked) | (256, 128) | 64x24 | Discerning Customer speech-skip; transaction in 5 seconds |

### Certificate Overflow Gag:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Inventory Overflow Mock Panel | (0, 160) | 128x96 | Inventory grid crammed with rolled certificates crowding actual items |
| "Inventory Full (Paper)" Banner | (128, 160) | 120x24 | Warning banner for the certificate-hoard state |
| Certificate Counter Chip | (128, 184) | 48x24 | Running certificate count — feeds "Certificate Collector" |
| Sell-Back 1 Sov Dialog | (128, 208) | 96x48 | Confirmation: "Sell certificate for 1 Sov? (He will see.)" — insulting but possible |

### Progression & Selfie UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Discerning Progress Bar | (0, 256) | 160x24 | 0 Sovs → 200 Sovs spend tracker with gold fill |
| Discerning Customer Badge (Large UI) | (160, 256) | 48x48 | Laurel badge for status screen |
| Sovs-Spent Counter | (208, 256) | 64x24 | Cumulative `N SOVS` display — word lettered, no currency mark. ⚠️ 64x24 fits four digits + `SOVS` only if the word is set at half-height beneath the figure; widen to 88x24 for a single-line treatment. |
| Achievement Toast Frame | (288, 256) | 128x48 | For "First Certificate," "Provenance Survivor," "Overwhelmed," etc. |
| Caption Card: "Certified Authentic" | (0, 312) | 96x24 | Standard selfie caption |
| Caption Card: "I Have Documentation" | (96, 312) | 96x24 | "The Collector" variant (10+ certificates, overwhelmed expression) |
| Caption Card: "They Trust Me Now" | (192, 312) | 96x24 | Discerning Customer variant (behind counter, cabinet visible) |

### Technical Notes:
- Shop cards deliberately omit prices until "Inquire" is pressed — the UI itself performs the satire
- The clock ticking UI element is synced to the clock-ticking audio loop, one tick per second of speech
- Overflow mock panel is a static gag texture, swapped in when certificates > items

---

## ♿ Sprite Sheet 7: Accessibility Overlays
**File:** `connoisseurs_cache_accessibility.png`
**Dimensions:** 256x256 pixels
**Color Palette:** #FFF8E1 on #1F1B18 (maximum contrast pairs), shape-coded glyphs

*(All coordinate tables for the Accessibility Sprite Requirements section below reference this sheet.)*

| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Herr Kurator High-Contrast Outline | (0, 0) | 48x96 | Cream silhouette rim against dark shelving |
| The Browser High-Contrast Outline | (48, 0) | 48x96 | Distinguishes the trapped NPC from décor |
| Specialty Cabinet Outline | (96, 0) | 64x96 | High-contrast frame around the locked interactable |
| Counter Interaction Highlight | (160, 0) | 64x48 | Enhanced-visibility marker for the shop trigger zone |
| Reading Nook Highlight | (160, 48) | 64x48 | Marks the selfie spot / browse trigger |
| Static Light Beam (No Motes) | (0, 96) | 64x64 | Spotlight without floating particles |
| Static Candle | (64, 96) | 16x24 | Non-flickering flame frame |
| Static Wall Clock | (80, 96) | 24x32 | Pendulum removed; time still passes, quietly |
| Static Cabinet Glow | (104, 96) | 64x64 | Non-pulsing unlock radiance |
| Register Chime Glyph | (0, 160) | 24x24 | Bell-note shape on every purchase chime |
| Stamp Thunk Burst | (24, 160) | 24x24 | Impact star for certificate stamping sound |
| Cabinet Unlock Click Glyph | (48, 160) | 24x24 | Key-turn arc for the unlock sound |
| Page Turn Glyph | (72, 160) | 24x24 | Curling-page mark for nook reading audio |
| Clock Tick Glyph | (96, 160) | 24x24 | Tick-mark pulse for speech-duration audio |
| Doorbell Glyph | (120, 160) | 24x24 | Brass bell shape on entry chime |
| Speech-Drone Waveform | (144, 160) | 32x24 | Steady waveform strip while provenance audio plays |
| Sigh Glyph | (176, 160) | 16x24 | The Browser's desperate sighs, visualized |
| Category Shape: Remedies (Circle) | (0, 192) | 24x24 | Shape-coded tab alternative |
| Category Shape: Support (Square) | (24, 192) | 24x24 | Shape-coded tab alternative |
| Category Shape: Implements (Triangle) | (48, 192) | 24x24 | Shape-coded tab alternative |
| Category Shape: Utility (Diamond) | (72, 192) | 24x24 | Shape-coded tab alternative |
| Category Shape: Specialty (Star) | (96, 192) | 24x24 | Shape-coded tab alternative |

### Technical Notes:
- Overlays render on a dedicated CanvasLayer toggled by accessibility settings, no base-sheet duplication
- Static variants are frame-for-frame size matches with their animated counterparts for clean swaps

---

## 🎬 Animation Specifications

### Herr Kurator Reverent Retrieval:
- **Duration:** 1.5 seconds, single play
- **Frames:** 3
- **Pattern:** Frame 1 → 2 → 3, hold on presentation
- **Trigger:** Player selects any item to purchase
- **Purpose:** Establishes that no object in this shop is merely picked up — everything is HANDLED
- **Audio Sync:** Soft fabric rustle on frame 2; silence on frame 3 (reverence)
- **Mobile Optimization:** None needed

### Herr Kurator Provenance Speech Loop:
- **Duration:** 1.6 second cycle, looping for the full 30–60 second speech
- **Frames:** 4
- **Pattern:** Frame 1 → 2 → 3 → 4 → loop
- **Trigger:** Purchase confirmation (pre-Discerning Customer); cannot be interrupted without offense
- **Purpose:** The location's core mechanic and core joke — sincerity sustained far past comfort
- **Audio Sync:** Speech VO throughout; clock ticking begins 3 seconds in and persists to speech end
- **Mobile Optimization:** Drop to 2-frame alternation (frames 1/3) on low-end devices

### Herr Kurator Approving Nod:
- **Duration:** 0.8 seconds, single play with 0.4 second hold
- **Frames:** 2
- **Pattern:** Frame 1 → 2, hold frame 2
- **Trigger:** Discerning Customer uses "The usual, please."
- **Purpose:** "You already understand." — the emotional payoff of 200 Sovs of accumulated speeches
- **Audio Sync:** None (the silence IS the approval)
- **Mobile Optimization:** None needed

### Certificate Handing:
- **Duration:** 1.0 second, single play
- **Frames:** 2
- **Pattern:** Frame 1 → 2, hold until player accepts
- **Trigger:** Every completed purchase, without exception, forever
- **Purpose:** You cannot escape the certificate; the animation refuses to end until you take it
- **Audio Sync:** Paper crispness foley on frame 2
- **Mobile Optimization:** None needed

### Certificate Stamping:
- **Duration:** 0.5 seconds, single play
- **Frames:** 4 (raised → descending → impact → seal result)
- **Pattern:** Frame 1 → 4, hold seal
- **Trigger:** Transaction finalization, behind the counter
- **Purpose:** Bureaucratic ceremony for a 10 Sovs tea purchase
- **Audio Sync:** Certificate stamp thunk exactly on impact frame (frame 3)
- **Mobile Optimization:** None needed

### Specialty Cabinet Unlock:
- **Duration:** 1.2 seconds, single play
- **Frames:** 3 cabinet states + glow overlay
- **Pattern:** Locked → unlocking → open, glow fades in over final 0.6 seconds
- **Trigger:** First specialty purchase attempt after reaching Discerning Customer status
- **Purpose:** The retail rapture moment — access as sacrament
- **Audio Sync:** Cabinet unlock click on frame 2; soft chord swell with glow
- **Mobile Optimization:** Glow overlay replaced by static gold frame on low-end devices

### Reading Nook Page Turn:
- **Duration:** 0.9 second cycle, loops while browsing
- **Frames:** 3
- **Pattern:** Lift → arc → settle, loop with 2 second rest between cycles
- **Trigger:** Player enters reading nook browse mode
- **Purpose:** The obligation trap ambience — the comfy chair whispering "you'll feel bad leaving empty-handed"
- **Audio Sync:** Page turning foley on frame 2 of each cycle
- **Mobile Optimization:** None needed

### Provenance Clock Ticking (UI):
- **Duration:** 1.0 second cycle (tick → tock), loops for speech duration
- **Frames:** 2
- **Pattern:** Frame 1 ↔ 2, one swap per second
- **Trigger:** Provenance speech active
- **Purpose:** The comedy metronome — real time visibly leaving the player's life
- **Audio Sync:** Clock ticking audio, one tick per frame swap
- **Mobile Optimization:** None needed (2 frames is already minimal)

### The Browser Polite Nod:
- **Duration:** 2.0 second cycle, loops eternally
- **Frames:** 2
- **Pattern:** Nod 1 ↔ Nod 2; every fourth cycle substitutes Glazed Stare for one beat
- **Trigger:** Constant while shop is open
- **Purpose:** A living warning of what engaging fully costs
- **Audio Sync:** Desperate sigh (quiet) on the glazed-stare beat
- **Mobile Optimization:** None needed

### Dust Motes Drift:
- **Duration:** 4.0 second drift cycle
- **Frames:** Particle system (CPUParticles2D), 12 particles max
- **Pattern:** Slow float through spotlight cones
- **Trigger:** Constant, main floor and implements corner beams only
- **Purpose:** Gallery gravitas — dust as set dressing for importance
- **Audio Sync:** None
- **Mobile Optimization:** Disabled entirely at Low LOD; halved (6 particles) at Medium

### Certificate Flutter (Overflow Gag):
- **Duration:** 1.2 seconds per certificate, single play
- **Frames:** 3
- **Pattern:** Tumble frames 1 → 2 → 3, certificate lands and persists on floor
- **Trigger:** Opening inventory while certificates outnumber items ("Overwhelmed" achievement state)
- **Purpose:** The paperwork has won
- **Audio Sync:** Soft paper flutter, one per falling certificate (max 3 concurrent)
- **Mobile Optimization:** Single certificate falls instead of three on low-end devices

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Herr Kurator outline overlay | (0, 0) on Sheet 7 | 48x96 | Key NPC silhouette against dark walnut shelving |
| The Browser outline overlay | (48, 0) on Sheet 7 | 48x96 | Separates the trapped customer from furniture |
| Specialty cabinet outline | (96, 0) on Sheet 7 | 64x96 | High-contrast frame around the progression-gated interactable |
| Counter interaction highlight | (160, 0) on Sheet 7 | 64x48 | Enhanced-visibility marker for the primary shop trigger |
| Reading nook highlight | (160, 48) on Sheet 7 | 64x48 | Marks browse mode and selfie spot trigger |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static light beam (no motes) | (0, 96) on Sheet 7 | 64x64 | Spotlight without floating dust particles |
| Static candle frame | (64, 96) on Sheet 7 | 16x24 | Non-flickering reading nook flame |
| Static wall clock | (80, 96) on Sheet 7 | 24x32 | Pendulum-free clock; UI tick counter becomes numeric-only |
| Static cabinet glow | (104, 96) on Sheet 7 | 64x64 | Non-pulsing unlock state; certificate flutter gag becomes a static pile |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Register chime glyph | (0, 160) on Sheet 7 | 24x24 | Bell-note shape fires with every elegant register chime |
| Stamp thunk burst | (24, 160) on Sheet 7 | 24x24 | Impact star on certificate stamp audio |
| Cabinet unlock click glyph | (48, 160) on Sheet 7 | 24x24 | Key-turn arc on unlock audio |
| Page turn glyph | (72, 160) on Sheet 7 | 24x24 | Curling-page mark per page-turn foley |
| Clock tick glyph | (96, 160) on Sheet 7 | 24x24 | Pulse per tick during provenance speeches |
| Doorbell glyph | (120, 160) on Sheet 7 | 24x24 | Entry bell visualization |
| Speech-drone waveform | (144, 160) on Sheet 7 | 32x24 | Continuous strip while provenance VO plays; length reflects speech progress |
| Sigh glyph | (176, 160) on Sheet 7 | 16x24 | The Browser's sighs made visible |

### Colorblind Considerations:
- Shop category tabs pair icons AND shapes (circle/square/triangle/diamond/star chips at (0–96, 192) on Sheet 7) — never gold-tint alone
- Locked vs. unlocked specialty cabinet differs by lock icon and door position, not just glow color
- Forged Invitation vs. Formal Invitation distinguished by flourish shape, not ink color
- Discerning progress bar uses fill pattern (hatched → solid) in addition to gold color
- Touch zones minimum 44px for all interactives: counter, cabinet, nook, tabs, Inquire button, skip button, certificate accept

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); certificate template and placard card frame need ASTC 4x4 — the paperwork must be legible, it's the joke
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for UI sheet (text-bearing placards and certificate are screenshot-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| cache_environment | tileset & zones, certificate/effects | 1024x1024 |
| cache_characters | Herr Kurator, The Browser & ambient | 512x512 |
| cache_items_ui | item roster, shop UI, accessibility overlays | 1024x1024 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full dust motes (12), candle flicker, pendulum, cabinet glow, 4-frame speech loop, 3-certificate flutter |
| Medium | 6 dust motes, static pendulum, glow simplified to fade, 4-frame speech loop retained |
| Low | No ambient particles, static clock/candle/glow, 2-frame speech loop, single-certificate flutter, zone backdrops as flat textures |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 35 MB maximum
- **Particle Limit:** 12 (dust motes only; flutter gag is sprite-based, not particles)

### Performance Notes:
- Shop is UI-heavy and motion-light by design — the 14 draw call budget holds because zones are pre-composited backdrops, not tile-assembled at runtime
- Specialty cabinet, Discerning UI, and overflow gag states are pure texture swaps on flags: zero animation cost when inactive
- Provenance speech scene disables all ambient systems except the clock — Kurator's loop and the tick are the only movers, focusing attention AND the frame budget
- Reading nook assets load on-demand when the player crosses the nook threshold

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- AnimatedSprite2D for Herr Kurator and The Browser state machines
- CPUParticles2D (not GPU) for dust motes; certificate flutter as scripted Sprite2D tweens
- CanvasLayer for shop UI, provenance panel, and accessibility overlay toggles
- Location state machine: `standard_customer → discerning_customer` drives cabinet textures, skip button, speech bypass; `certificates_owned > items_owned` flag drives the overflow gag
- Shop inventory data-driven: item sprites referenced by atlas region, placard text from item database

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Brass register / purchase complete | Elegant register chime | On transaction confirm, with chime sparkle |
| Certificate stamping | Certificate stamp thunk | On impact frame (frame 3 of 4) |
| Specialty cabinet unlocking | Cabinet unlock click + chord swell | Click on frame 2; swell with glow fade-in |
| Reading nook page turn | Page turning foley | On frame 2 of each cycle |
| Provenance speech UI clock | Clock ticking loop | One tick per frame swap, starts 3s into speech |
| Front door | Brass bell chime | On enter/exit |
| The Browser glazed-stare beat | Quiet desperate sigh | Every fourth nod cycle |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Certificate Collector | Certificate rolled item, counter chip, overflow panel, flutter gag | Counter increments per purchase; achievement at 20 certificates |
| The Curated Journey | All five category tabs, item roster sprites, achievement toast | Toast fires on first purchase from each category ("The Complete Set" at all five) |
| Discerning Customer | Progress bar, badge sprites, approving nod frames, cabinet unlock sequence, "The usual, please." button | 200 Sovs spend threshold flips location state; unlock animation plays once |
| Provenance Master | Passionate speech loop, clock UI, speech-drone waveform | Tracks full uninterrupted speeches; masochist achievement at all speeches heard ("Provenance Survivor" at 10) |
| First Certificate / Overwhelmed (achievements) | Certificate handing frames, overflow mock panel | First purchase; certificates > items state |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Kaffeehaus Row | Home district ambience; storefront façade matches Row street tileset trim | Standard street-door transition with brass bell chime |
| Baroness' Ballroom | Masquerade masks (basic/ornate), Formal/Forged Invitations, Favor Token sprites referenced at ballroom entry check | Item-gate check reuses this sheet's item sprites in ballroom UI |
| The Bassline Opera House | VIP Opera Pass sprite shown at backstage access | Pass presented in opera door UI |
| Café Existenz | Pocket Philosopher and dialogue combat aids appear in Existenz debate UI | Shared item iconography, no scene transition |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A gift shop cosplaying as a museum cosplaying as a necessity"
- **Color Mood:** Library brown and paper cream warmed by refined gold — old money lighting on new merchandise
- **Lighting:** Diffused gallery wash, brass spotlight cones on featured items, reading-lamp pools in the nook; everything lit to look important
- **Texture:** Velvet, walnut grain, embossed paper, glass gleam — surfaces that whisper "don't touch" while begging you to buy

### Environmental Storytelling:
- No visible price tags anywhere — asking summons judgment; the environment enforces the pretension economy
- Placards beside EVERYTHING, including a broom (placard: "Utility. Local maple. Unprovenance'd, tragically.")
- The framed provenance certificates in the Implements Corner outnumber the implements
- The reading nook chairs face the register — comfort with surveillance; the obligation trap is architectural
- The specialty cabinet is positioned so every customer walks past what they can't access yet

### Character Integration Notes:
- Herr Kurator is rendered warmer than his shop — his sincerity is genuine, which is the joke; never draw him smug
- The Browser reads as furniture at first glance; his desperate eye contact frame should be a delayed discovery
- Bros (Lord Pilsner, Chadwick, Bradley) use standard party sprites; the shop's reaction shots come from Kurator's pained smile / delight frames

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The certificate for tea** — a full readable certificate with a serial number for a 10 Sovs tea tin; screenshots itself
2. **The Browser's "Help me."** — tiny speech bubble mid-provenance speech, a blink-and-miss-it gag players will share when they catch it
3. **The inventory overflow** — certificates crowding out actual items with the "Inventory Full (Paper)" banner
4. **The approving nod** — "The usual, please." → "You've grown." — the most weirdly emotional shop transaction in the game
5. **Selfie spot variants** — "Certified Authentic" / "I Have Documentation" / "They Trust Me Now"

### Quote Potential:
- "You wanted TEA. You're receiving HISTORY." — Herr Kurator
- "But you'll eat them KNOWINGLY." — Herr Kurator
- "Help me." — The Browser
- "This isn't mere commerce. This is... curation." — Herr Kurator
- "I've grown to FEAR the speeches." — Lord Pilsner / "Fear and respect are close neighbors." — Herr Kurator

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | connoisseurs_cache_tileset.png | 1024x512 |
| 2 | herr_kurator.png | 384x288 |
| 3 | connoisseurs_cache_npcs.png | 256x128 |
| 4 | connoisseurs_cache_items.png | 256x256 |
| 5 | connoisseurs_cache_certificate_effects.png | 256x192 |
| 6 | connoisseurs_cache_ui.png | 512x384 |
| 7 | connoisseurs_cache_accessibility.png | 256x256 |

**Total Estimated Memory:** ~4 MB (uncompressed RGBA — 1,044,480 px × 4 bytes ≈ 4.18 MB)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `connoisseurs_cache_tileset.png` (1024x512)
- [ ] `herr_kurator.png` (384x288)
- [ ] `connoisseurs_cache_npcs.png` (256x128)
- [ ] `connoisseurs_cache_items.png` (256x256)
- [ ] `connoisseurs_cache_certificate_effects.png` (256x192)
- [ ] `connoisseurs_cache_ui.png` (512x384)
- [ ] `connoisseurs_cache_accessibility.png` (256x256)

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
- **Documentation:** Animation timing reference sheet + Discerning Customer state-swap guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] Certificate template legible at game resolution — the serial number joke must read
- [ ] Forged Invitation differs from Formal Event Invitation by exactly one flourish
- [ ] Herr Kurator's reverence reads in the retrieval frames (both hands, always)
- [ ] The Browser's "Help me." bubble small enough to be a discovery, large enough to be found
- [ ] Specialty cabinet contents visible through glass in ALL lock states (temptation is the point)
- [ ] No price tags visible anywhere in environment art
- [ ] Clock pendulum and UI clock tick sync at exactly 1 tick/second
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets — curation-as-commerce reads without dialogue
- [ ] Hidden areas/interactions have discoverable visual cues (Browser eye contact, cabinet glow, under-counter Forged Invitation)
- [ ] Mobile performance optimized (CPU particles, atlas limits respected, 14 draw call budget)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices (certificate, overflow, selfie spot)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Viennese museum-shop tradition evoked, never named |
| Cultural Specificity | ✅ | Viennese museum shop / Habsburg souvenir culture, Kaffeehaus Row intellectual district |
| Satirical Targets Appropriate | ✅ | Premium retail narrative and "curated" culture — retail practice, not cultural appreciation; confused tourists are marks, not butts |
| Seedy Underbelly Present | ✅ | Soft vice, honestly noted: Forged Invitation sold under the counter ("transferable, untraceable," 10% detection risk), deliberate exploitation of confused bros who "pay extra because it SEEMS important," and the reading-nook obligation trap — pretension economy rather than hard crime |
| Gameplay Value Established | ✅ | Full 26-item general shop, provenance mechanic, certificate system, Discerning Customer progression, 4 quests + 7 achievements |
| Technical Feasibility | ✅ | Seven sheets, three atlases, LOD tiers, state-swap architecture documented |
| Mobile Performance Budget | ✅ | 60 FPS, 14 draw calls, 35 MB, 12 particles (per source profile) |
| Accessibility Features | ✅ | Visual cues for all 7 audio events; static variants; shape-coded categories; 44px zones |
| No Crypto Elements | ✅ | Pure retail curation satire; certificates are paper, pointedly |
| Social Media Integration | ✅ | Tea certificate, "Help me.", inventory overflow, three selfie variants identified |

**The Connoisseur's Cache: where the player buys tea and receives history, buys weapons and receives appreciation, and leaves every single time holding a certificate — because in Sinfonia, you're not shopping, you're being curated.**
