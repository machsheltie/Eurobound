# The Gilded Suite - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for The Gilded Suite (in-world name: "Das Schlafgemach") — a Habsburg palace converted to luxury short-term lodging where the five-star reviews are suspiciously uniform, the host hasn't blinked since 1847, and checkout at 11 AM is the only rule the building truly believes in. It satirizes surveillance hospitality and review-manipulated rental culture: every weird vacation-rental fear made politely, gorgeously real. Assets must sell horror-comedy through subtle wrongness — imperial gold and innocent cream on the surface, watchful crimson underneath, never gore.

**Location ID:** `sinfonia_imperialdistrict_gilded_suite_01`
**Theme:** Luxury short-term rental culture — fake reviews, smothering hosts, surveillance-as-service, guest entrapment as five-star hospitality
**Zone:** Imperial District, near Imperial Square
**Hours:** Check-in 15:00–23:00, checkout by 11:00 (strictly enforced; the building enforces it more than the law does)
**Primary Function:** Rest location (three paid room tiers) / mystery location / optional basement dungeon / two boss encounters (The First Guest puzzle boss, Herr Gastfreund social-combat boss) / couchsurfing economic counterpoint

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Palatial Gold | #D4AF37 | Gilding, frames, chandeliers, trim, the entire lie |
| Watchful Crimson | #8B0000 | Carpets, drapes, surveillance accents, sting flashes |
| Innocent Cream | #FFFDD0 | Walls, marble, linens — the "nothing is wrong here" base |
| Something Wrong | #2F2F2F | Shadows, portrait backgrounds, basement, Gastfreund's suit |
| Habsburg Marble | #F5F0E1 | Foyer floors, staircase, fountain stone |
| Candlelight Amber | #FFBF66 | Sconce glow, chandelier light pools, warm menace |
| Eternal Fruit Wax | #E8C547 | The fruit. Always the fruit. Slightly too glossy |
| Basement Verdigris | #4E6E58 | Hospitality Engine brass patina, 1784 record spines |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/gilded_suite/
├── environment/
│   ├── gilded_suite_exterior.png
│   ├── gilded_suite_tileset.png
│   └── gilded_suite_rooms.png
├── npcs/
│   ├── herr_gastfreund.png
│   └── gilded_suite_npcs.png
├── objects/
│   └── gilded_suite_portraits.png
├── effects/
│   └── gilded_suite_effects.png
└── ui/
    └── gilded_suite_ui.png
```

---

## 🏰 Sprite Sheet 1: Palace Exterior
**File:** `gilded_suite_exterior.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #F5F0E1 (Habsburg Marble), #D4AF37 (Palatial Gold), #2F2F2F (Something Wrong), #FFFDD0 (Innocent Cream)

### Facade & Roofline:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Facade Center Block | (0, 0) | 256x192 | Immaculate Habsburg palace front, too clean, zero pigeons |
| Facade Left Wing | (256, 0) | 192x192 | Symmetrical wing, every curtain identically parted |
| Facade Right Wing | (448, 0) | 192x192 | Mirror of left wing — literally identical, that's the problem |
| Roofline & Crest | (640, 0) | 256x96 | Gilded double-headed crest, weathervane pointing at viewer |
| Windows Lit Overlay | (640, 96) | 256x96 | Night overlay; one upper window holds a motionless silhouette |
| Iron Gates Closed | (896, 0) | 128x160 | Ornate wrought iron, gold-tipped, welcoming like a jaw |

### Gates, Gardens & Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Iron Gates Open | (0, 192) | 128x128 | Open inward. They only open inward |
| Fountain Base | (128, 192) | 96x96 | Marble cherub fountain, water unnaturally silent |
| Fountain Eyes Frame 1 | (224, 192) | 96x96 | Sculptural eyes forward — default state |
| Fountain Eyes Frame 2 | (320, 192) | 96x96 | Sculptural eyes tracked to player position |
| Fountain Eyes Frame 3 | (416, 192) | 96x96 | Eyes fixed on the front door, expectant |
| Garden Hedge Straight | (512, 192) | 64x64 | Manicured to the millimeter |
| Garden Hedge Corner | (576, 192) | 64x64 | Corner piece, geometrically perfect |
| Manicured Flowerbed | (640, 192) | 64x32 | Flowers in review-star arrangement (subtle, 5 blooms) |
| Gravel Path Tile | (640, 224) | 32x32 | Raked daily. By whom? |
| Gravel Path Edge | (672, 224) | 32x32 | Border trim tile |
| Brass Plaque ★★★★★ | (704, 192) | 96x64 | "Das Schlafgemach — Est. 1784 — ★★★★★" polished brass |
| Magazine Feature Sign | (800, 192) | 96x64 | "As Featured in 'Authentic Palace Living' Magazine" (magazine doesn't exist) |
| Lamppost Unlit | (896, 192) | 32x96 | Period gas lamp |
| Lamppost Lit | (928, 192) | 32x96 | Flame perfectly steady, no flicker outdoors |
| Neighbor Building Lean Left | (960, 192) | 64x128 | Adjacent facade visibly leaning AWAY from the palace |

### Entrance & Street:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Neighbor Building Lean Right | (0, 320) | 64x96 | Other side, also leaning away |
| Front Door Grand | (64, 320) | 64x96 | Double doors, brass fittings, always freshly oiled |
| Front Door Ajar | (128, 320) | 64x96 | Open exactly enough to imply invitation |
| Front Door Sealed Glow | (192, 320) | 64x96 | Checkout Denied exterior state — faint crimson seam light |
| Palace Steps | (256, 320) | 128x48 | Marble steps, center worn by 240 years of arrivals (few departures) |
| Welcome Mat | (384, 320) | 48x32 | Reads "WILLKOMMEN" — the N trails off like it wanted to write FOREVER |
| Exterior Night Overlay | (432, 320) | 256x96 | Blue-dark tint layer; palace windows stay warm |
| Bulletin Ad Poster | (688, 320) | 64x96 | Citywide bulletin board advertisement art — "150 Sovs/night! A PALACE!" |
| Doorway Farewell Backdrop | (752, 320) | 128x96 | Framed doorway composition for the "Survived" selfie (Gastfreund waving) |
| Cobblestone Tile | (880, 320) | 32x32 | Imperial District street stone |
| Cobblestone Worn | (912, 320) | 32x32 | Variant with wear |
| Iron Fence Section | (944, 320) | 64x64 | Perimeter fencing, decorative spikes (decorative?) |

### Garden Detail:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Garden Statue Watching | (0, 416) | 64x96 | Classical statue, head forward |
| Garden Statue Head-Turned | (64, 416) | 64x96 | Same statue, head rotated toward player — swap on re-entry only |
| Chimney Smoke Static | (128, 416) | 32x64 | Smoke column that never moves. Painted-on sky behavior |
| Cornerstone 1784 | (160, 416) | 48x32 | Foundation stone, date suspiciously re-chiseled |
| Curtain Twitch Frame A | (208, 416) | 64x64 | Ground-floor window, curtain at rest |
| Curtain Twitch Frame B | (272, 416) | 64x64 | Curtain settling as if just released |
| Check-In Hours Sign | (336, 416) | 64x48 | "Check-in 15:00–23:00. Checkout 11:00. This is non-negotiable." |

### Technical Notes:
- Exterior is a static painted composition per profile mobile guidance — the only "animation" is state swaps (fountain eyes, statue head, curtain) triggered on look-away or re-entry, never live motion
- Leaning neighbor buildings must read at a glance: 4–6° shear, exaggerated EarthBound-style
- Facade symmetry should be pixel-perfect left/right; wrongness comes from perfection, not decay

---

## 🏛️ Sprite Sheet 2: Foyer, Breakfast Room & Basement Tileset
**File:** `gilded_suite_tileset.png`
**Dimensions:** 1024x768 pixels
**Color Palette:** #FFFDD0 (Innocent Cream), #D4AF37 (Palatial Gold), #8B0000 (Watchful Crimson), #4E6E58 (Basement Verdigris)

### Floor Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marble Floor Cream | (0, 0) | 32x32 | Foyer base marble |
| Marble Floor Veined | (32, 0) | 32x32 | Gold-veined variant |
| Marble Too-Polished | (64, 0) | 32x32 | Faint reflection of someone standing behind you |
| Red Carpet Center | (96, 0) | 32x32 | Watchful Crimson runner |
| Red Carpet Edge | (128, 0) | 32x32 | Gold-trimmed border |
| Parquet Room Floor | (160, 0) | 32x32 | Guest room herringbone |
| Parquet Worn Path | (192, 0) | 32x32 | Wear path from bed to door that predates the current furniture |
| Breakfast Room Tile | (224, 0) | 32x32 | Checkered cream/gold |
| Basement Stone | (256, 0) | 32x32 | Cold flagstone |
| Basement Stone Stained | (288, 0) | 32x32 | Old stains (wine. definitely wine) |

### Wall Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cream Wall Panel | (0, 32) | 32x64 | Upper wall plaster |
| Gold Wainscoting | (32, 32) | 32x64 | Gilded lower paneling |
| Damask Wallpaper | (64, 32) | 32x64 | Crimson damask pattern |
| Damask Eyes Variant | (96, 32) | 32x64 | Same damask; motif resolves into faint eyes at second glance |
| Window Tall Interior | (128, 32) | 32x64 | Opens exactly four inches |
| Window Barred Decorative | (160, 32) | 32x64 | Gold-painted bars ("original 1784 security features") |
| Crown Molding Cap | (192, 32) | 32x32 | Gilded ceiling trim |
| Basement Brick Wall | (224, 32) | 32x64 | Bare brick, verdigris seep |

### Grand Foyer Landmarks:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Reception Desk | (0, 96) | 128x80 | Marble-topped, brass bell, no computer — never a computer |
| Guest Book Open | (128, 96) | 48x32 | Centuries of signatures in suspiciously similar handwriting |
| Guest Book Closed | (176, 96) | 48x32 | Leather-bound, warm to the touch |
| House Rules Frame | (224, 96) | 64x96 | All 27 rules framed in gold; Rule 6 visibly removed |
| Grand Chandelier | (288, 96) | 128x112 | Crystal cascade, candles lit |
| Chandelier Sync Frame 2 | (416, 96) | 128x112 | All candles flickering in perfect unison |
| Elevator Doors Closed | (544, 96) | 64x96 | Brass cage elevator |
| Elevator Doors Open | (608, 96) | 64x96 | Already open when you approach. It knew |
| Elevator Floor Indicator | (672, 96) | 48x24 | Dial shows only YOUR floor. No other numbers exist |
| Desk Bell | (672, 120) | 24x24 | Rings before you touch it |
| Music Speaker Grate | (696, 120) | 32x24 | Source of the too-slow waltz, styled as period vent |

### Grand Staircase & Breakfast Room:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Grand Staircase | (0, 208) | 256x192 | Sweeping marble stairs, red runner — the selfie spot |
| Staircase Balustrade | (256, 208) | 64x192 | Gilded rail section for layering |
| Portrait Row Overlay | (320, 208) | 192x96 | Background portrait cluster for "The Watched" selfie variant |
| Foyer Grand Rug | (320, 304) | 128x96 | Crimson rug, crest pattern |
| Breakfast Table Long | (512, 208) | 160x96 | White linen, seats eight, always set for exactly your party plus one |
| Breakfast Buffet Spread | (672, 208) | 128x96 | Lavish continental buffet — suspiciously exceptional |
| Breakfast Chair | (800, 208) | 32x48 | Gilded chair |
| Breakfast Chair Warm | (832, 208) | 32x48 | Identical but subtly indented — someone just left |
| Coffee Service Cart | (864, 208) | 64x64 | Silver pots, refills appear between blinks |
| Host Podium | (928, 208) | 64x96 | Where Gastfreund presides, watching you eat |
| Breakfast Place Settings | (512, 304) | 160x64 | Table-top overlay: plates, folded swans, name cards you didn't provide |
| Juice Pyramid | (672, 304) | 48x64 | Glasses stacked with structural confidence |

### Uncanny Objects & Passages:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Grandfather Clock 3:07 | (0, 400) | 48x112 | Shows 3:07. It is not 3:07 |
| Mantel Clock 11:58 | (48, 400) | 48x48 | Forever two minutes to checkout |
| Cuckoo Clock 8:41 | (96, 400) | 48x64 | No clock in the building shows the current time |
| Front Desk Ledger | (144, 400) | 32x32 | Open to today's date. Every day |
| Room Key Rack | (176, 400) | 64x64 | Every hook filled, every key identical |
| Velvet Rope | (240, 400) | 64x32 | Blocks nothing, implies everything |
| Potted Palm | (304, 400) | 48x80 | Standard foyer palm |
| Potted Palm Moved | (352, 400) | 48x80 | Same palm — it was by the window before. Swap on re-entry |
| Minibar Cabinet | (400, 400) | 48x64 | Stocked |
| Minibar Restocking | (448, 400) | 48x64 | Bottles mid-materialize while you watch |
| Do Not Disturb Sign | (496, 400) | 24x32 | On handle where you left it |
| Do Not Disturb Moved | (520, 400) | 24x32 | Never QUITE where you left it |
| Eternal Fruit Painting | (544, 400) | 96x112 | Still life of the fruit basket — the hidden basement entrance |
| Fruit Painting Ajar | (656, 400) | 112x112 | Swung open on hinges, dark stair behind |
| Wi-Fi Password Placard | (768, 400) | 48x32 | The password is your grandmother's maiden name. You never told them |
| Hallway Runner Tile | (816, 400) | 32x32 | Corridor carpet base |
| Staff Door | (848, 400) | 48x96 | "THIRD FLOOR — STAFF ONLY." There is no third floor |

### Basement (Secret Area):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Basement Stair Down | (0, 512) | 96x128 | Stone steps behind the fruit painting |
| Records Shelf 1784 | (96, 512) | 128x96 | Guest ledgers back to 1784 — every entry, same handwriting |
| Lost Items Shelf | (224, 512) | 128x96 | Hats, canes, monocles, one modern smartphone, still charged |
| Lost Items Pile | (352, 512) | 96x64 | Overflow luggage from guests who "extended their stay" |
| Original Gastfreund Portrait | (448, 512) | 96x128 | Dated 1784. Identical to the current host. Identical |
| Hospitality Engine Idle | (544, 512) | 192x160 | Brass-and-verdigris machine, gauges labeled COMFORT / SATISFACTION / RETENTION |
| Hospitality Engine Active | (736, 512) | 192x160 | Gauges glowing amber, five-star dial pinned, faint heartbeat pulse |
| Original Checkout Desk | (928, 512) | 96x96 | Dusty 1784 desk — the First Guest puzzle objective |

### Basement Details & Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Candle Sconce Lit | (0, 672) | 16x32 | Standard wall sconce |
| Candle Sconce Dimmed | (16, 672) | 16x32 | Lower flame state |
| Candle Sconce Watching-Dim | (32, 672) | 16x32 | Dims further — this frame triggers only when looked at |
| Basement Cobweb | (48, 672) | 32x32 | Corner web; even the spider checked out |
| Guest Record Page | (80, 672) | 32x32 | Loose ledger page prop, 1847 entry circled |
| Pastry Tray | (112, 672) | 48x32 | Breakfast prop, replenishes off-screen |
| Coffee Pot | (160, 672) | 24x32 | Steam emitter anchor |
| Emergency Release Lever | (184, 672) | 32x48 | The early-exit puzzle's hidden lever, disguised as gas valve |
| Original Deed Frame | (216, 672) | 48x64 | The property deed — proves the violations, one of the four escape methods |

### Technical Notes:
- Room bases are static backgrounds per profile; all wrongness is delivered via object swaps triggered on re-entry or look-away, never continuous animation
- Clocks are static sprites — three different wrong times, never ticking visually (audio only)
- Fruit painting → ajar swap is the basement reveal moment; give it a 2px gold rim light so it reads as interactive after the clue

---

## 🎩 Sprite Sheet 3: Herr Gastfreund (The Host)
**File:** `herr_gastfreund.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #2F2F2F (Suit), #FFFDD0 (Shirt/Gloves/Smile), #D4AF37 (Watch chain, buttons), #8B0000 (Cravat)

### Idle & Check-In (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Idle Unblinking | (0, 0) | 48x96 | Perfect stillness, hands clasped, eyes OPEN. Always open |
| Idle Smile Intensifies | (48, 0) | 48x96 | Identical pose, smile 8% wider — the dialogue beat sprite |
| Idle Head Tilt | (96, 0) | 48x96 | Polite 15° tilt, attentive-predator listening |
| Check-In Welcome Arms | (144, 0) | 48x96 | Arms spread in greeting, "I know ALL my guests" |
| Check-In Sign Here | (192, 0) | 48x96 | Presenting the Guest Agreement, pen already inked |
| Check-In Key Presentation | (240, 0) | 48x96 | Key offered on velvet cushion, slight bow |
| Materialize Frame 1 | (288, 0) | 48x96 | 40% opacity, forming from candlelight |
| Materialize Frame 2 | (336, 0) | 48x96 | 80% opacity, features resolving smile-first |
| Materialize Frame 3 | (384, 0) | 48x96 | Fully present, mid-bow, as if always here |
| Deep Bow | (432, 0) | 48x96 | Formal bow, eyes still on you through the brow |

### Night & Morning Hospitality (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| 3AM Knock | (0, 96) | 48x96 | Knuckles raised at door, immaculate at 3 AM |
| 3AM Waiting | (48, 96) | 48x96 | Face inches from door, infinite patience |
| 3AM Just Checking In | (96, 96) | 48x96 | Leaning through opened doorway, "just checking in" |
| Morning Greeting Inches Away | (144, 96) | 48x96 | Standing far too close, dawn light, coffee ready |
| Morning Coffee Offer | (192, 96) | 48x96 | "I never left. More coffee?" — pot extended |
| Pillow Fluff | (240, 96) | 48x96 | Aggressive pillow hospitality, guest optional |
| Temperature Adjust | (288, 96) | 48x96 | Hand at thermostat that has no controls |
| Watching You Sleep | (336, 96) | 48x96 | At bed's foot, hands clasped. That last one was a joke. It wasn't |
| Hallway Mid-Distance | (384, 96) | 48x96 | Far end of corridor, facing player |
| Hallway Closer Than Before | (432, 96) | 48x96 | Same pose. You didn't see him move |

### Hospitality Attacks — Social Combat Boss (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| One More Night Cast 1 | (0, 192) | 48x96 | Pocket watch raised, chain taut |
| One More Night Cast 2 | (48, 192) | 48x96 | Watch spinning, gold time-warp glow (pairs with effect fx) |
| Five-Star Service Cast 1 | (96, 192) | 48x96 | Arms wide, silver tray conjuring |
| Five-Star Service Cast 2 | (144, 192) | 48x96 | Buried in gifts, towels folded into swans mid-air |
| The Guest Book Cast 1 | (192, 192) | 48x96 | Guest book raised like scripture |
| The Guest Book Cast 2 | (240, 192) | 48x96 | Pages fanning, testimonial wisps escaping |
| Checkout Denied Cast 1 | (288, 192) | 48x96 | Single raised finger. "Checkout is at 11 AM. It is not 11 AM" |
| Checkout Denied Cast 2 | (336, 192) | 48x96 | Arms crossed, every key on his belt vanishing |
| One-Star Recoil | (384, 192) | 48x96 | Staggered by a one-star review — his only weakness |
| Existential Wobble | (432, 192) | 48x96 | The "take a vacation?" suggestion landing; smile buffering |

### Finale & Farewell (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mildly Distressed 1 | (0, 288) | 48x96 | Smile falters 4%. Maximum canonical distress |
| Mildly Distressed 2 | (48, 288) | 48x96 | One (1) hair out of place |
| Mildly Distressed 3 | (96, 288) | 48x96 | Smoothing lapels, composure reloading |
| Letting Go | (144, 288) | 48x96 | First Guest resolution — releasing a guest, genuinely confused by the concept |
| Sad Doorway Wave 1 | (192, 288) | 48x96 | Hand raised in farewell, framed in doorway |
| Sad Doorway Wave 2 | (240, 288) | 48x96 | Slow metronome wave |
| Sad Doorway Wave 3 | (288, 288) | 48x96 | Hand lowering, smile holding, eyes following you out |
| Eternal Guest Nod | (336, 288) | 48x96 | Respectful nod to Eternal Guest Card holders — peer recognition |
| Glide Walk 1 | (384, 288) | 48x96 | Walk cycle A — feet never clearly resolve |
| Glide Walk 2 | (432, 288) | 48x96 | Walk cycle B — he simply arrives places |

### Dialogue Close-Ups & Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Close-Up Morning Greeting | (0, 384) | 96x96 | Dialogue portrait, face filling frame, inches away |
| Close-Up Smile Intensifies | (96, 384) | 96x96 | The smile at full aperture, unnaturally white |
| Close-Up Mild Distress | (192, 384) | 96x96 | The 4% falter, rendered large — finale beat |
| White Gloves Pair | (288, 384) | 24x16 | Detail prop for cutaways |
| Pocket Watch | (312, 384) | 16x24 | Face shows 11:00. It always shows 11:00 |
| Master Key Ring | (336, 384) | 24x24 | One ring, uncountable keys |

### Character Notes:
- The eyes NEVER close in any frame. Not one. Verify at delivery
- Suit is Something Wrong (#2F2F2F), not black — he must read slightly softer than true shadow
- Posture is ramrod-vertical in every state including distress; only the smile and one hair are allowed to change
- Materialize frames double as his despawn (play reversed)

---

## 👥 Sprite Sheet 4: The First Guest, Silent Porter & Other Guests
**File:** `gilded_suite_npcs.png`
**Dimensions:** 512x384 pixels
**Color Palette:** Period-mismatched garment colors over #2F2F2F, #FFFDD0 skin tones drained 10%

### The First Guest (1784) — Puzzle Boss (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Frozen Confused Smile | (0, 0) | 48x80 | 1784 formal attire, expression frozen mid-pleasantry for 240 years |
| Searching For Desk 1 | (48, 0) | 48x80 | Patting the wall where the checkout desk was. It was HERE |
| Searching For Desk 2 | (96, 0) | 48x80 | Peering behind furniture, powdered wig askew |
| Riddle Pose | (144, 0) | 48x80 | Reciting guest-agreement clauses from memory, eyes distant |
| Realization | (192, 0) | 48x80 | It's okay to leave. The concept landing after two centuries |
| Tearful Checkout 1 | (240, 0) | 48x80 | Tears, gratitude, quill trembling over the ledger |
| Tearful Checkout 2 | (288, 0) | 48x80 | Signing out — the first checkout in the building's history |
| Departing Free | (336, 0) | 48x80 | Walking toward light, posture unfreezing |
| Boss Aura Idle | (384, 0) | 48x80 | Encounter state — faint 1784 dust-glow outline |
| First Guest Portrait Cameo | (432, 0) | 48x80 | His face in a hallway portrait, pre-discovery foreshadow |

### The Silent Porter (48x96 each unless noted):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Appearing Frame 1 | (0, 80) | 48x96 | Barely-there outline where no one stood |
| Appearing Frame 2 | (48, 80) | 48x96 | Half-present — already holding YOUR bags |
| Appearing Frame 3 | (96, 80) | 48x96 | Fully there. The bags were in your room. The room was locked |
| Standing By | (144, 80) | 48x96 | Cap shadow permanently obscuring the face |
| Bags Handoff | (192, 80) | 48x96 | Wordless presentation of luggage |
| Vanish Frame | (240, 80) | 48x96 | Gone. Bags remain, perfectly aligned |
| Corner Presence | (288, 80) | 48x96 | Peripheral-vision pose for background placement |
| Porter Luggage Cart | (336, 80) | 64x64 | Brass cart, wheels silent |
| Stacked Vintage Luggage | (400, 80) | 64x64 | Steamer trunks, 1780s–1980s stickers |
| Modern Suitcase Anomaly | (464, 80) | 48x64 | Wheeled polycarbonate case among the trunks. Recent. Unclaimed |

### Other Guests x3 — Review Speakers (48x80 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Guest 1 Vacant Stare | (0, 176) | 48x80 | 1920s flapper dress, thousand-yard stare |
| Guest 1 Review Delivery | (48, 176) | 48x80 | Mid-recitation: "The breakfast buffet is exceptional" |
| Guest 1 Breakfast Seated | (96, 176) | 48x80 | Seated, fork raised, not eating |
| Guest 2 Vacant Stare | (144, 176) | 48x80 | 1970s leisure suit, empty smile |
| Guest 2 Review Delivery | (192, 176) | 48x80 | "The staff anticipates every need" |
| Guest 2 Breakfast Seated | (240, 176) | 48x80 | Chewing in perfect 4/4 time |
| Guest 3 Vacant Stare | (288, 176) | 48x80 | Modern athleisure — the newest guest, the oldest eyes |
| Guest 3 Review Delivery | (336, 176) | 48x80 | "Five stars. Never leaving" |
| Guest 3 Breakfast Seated | (384, 176) | 48x80 | Coffee cup raised to lips, never sipped |
| Hallway Glimpse Silhouette | (432, 176) | 48x80 | Generic guest shape for corridor flickers — never the same twice |

### Group States & Hallway Variants:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Synchronized Turn Frame 1 | (0, 256) | 144x80 | All three guests mid-turn toward player, in unison |
| Synchronized Turn Frame 2 | (144, 256) | 144x80 | Turn complete. Three smiles. Same smile |
| Hallway Guest Variant A | (288, 256) | 48x80 | Edwardian gentleman — glimpsed once, never again |
| Hallway Guest Variant B | (336, 256) | 48x80 | 1950s nurse — glimpsed once, never again |
| Hallway Guest Variant C | (384, 256) | 48x80 | Disco tourist — glimpsed once, never again |
| Thousand-Yard Close-Up | (432, 256) | 64x64 | Dialogue portrait: vacant eyes, five-star pupil glint |
| Review Bubble ★★★★★ | (0, 336) | 64x32 | Floating speech bubble, five gold stars |
| "Never Leaving" Bubble | (64, 336) | 64x32 | Speech bubble, cheerful font, dreadful words |

### NPC Notes:
- All Other Guests share one desaturated skin ramp — 10% drained, not zombie-gray; they're satisfied, not dead (probably)
- The First Guest's palette is the only one using pure 1784 period color — he predates the house's filter
- Porter's face must never resolve: cap shadow in every frame including handoff

---

## 🛏️ Sprite Sheet 5: Room Tiers & Shifting Hallways
**File:** `gilded_suite_rooms.png`
**Dimensions:** 1024x768 pixels
**Color Palette:** #FFFDD0 (Innocent Cream), #D4AF37 (Palatial Gold), #8B0000 (Watchful Crimson), #E8C547 (Eternal Fruit Wax)

### Standard Room (150 Sovs):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Standard Bed | (0, 0) | 96x80 | Comfortable, dated, corners hospital-tight |
| Standard Bed Slept | (96, 0) | 96x80 | Post-rest state; already half-remade somehow |
| Dated Armchair | (192, 0) | 48x64 | Floral upholstery, faces the bed by default |
| Standard Dresser | (240, 0) | 64x64 | Drawers pre-lined with paper dated this morning |
| Standard Portrait Watching | (304, 0) | 48x64 | Single portrait; eye frames driven by Sheet 6 overlays |
| Standard Fruit Basket | (352, 0) | 48x32 | Modest arrangement. Never ripens. Never rots |
| Standard Window Stuck | (400, 0) | 48x80 | Opens exactly four inches, painted stop |
| Bathroom Door No Lock | (448, 0) | 48x96 | Excellent water pressure, visibly absent lock plate |
| Standard Rug | (496, 0) | 96x64 | Worn center — the previous guests stood here a lot |
| Standard Nightstand | (592, 0) | 32x48 | Drawer contains House Rules copy, pre-bookmarked |
| Standard Lamp | (624, 0) | 24x48 | Turns itself off at 23:00 sharp |
| Ornate Radiator | (648, 0) | 48x48 | Clanks in your walking rhythm |
| Room Number Plate 217 | (696, 0) | 32x24 | Your room number. Today |
| Room Number Plate 31B | (728, 0) | 32x24 | Your room number. Tomorrow. Same door |

### Deluxe Suite (300 Sovs):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Deluxe Bed | (0, 128) | 128x96 | Larger, plusher, monogrammed with initials — yours |
| Deluxe Seating Set | (128, 128) | 96x80 | Settee and side table, arranged toward the portraits |
| Deluxe Portrait Pair | (224, 128) | 96x64 | Two watchers; double the surveillance, double the value |
| Deluxe Fruit Basket | (320, 128) | 64x48 | More fruit. Still eternal. Same wax gleam |
| Balcony Door Sticking | (384, 128) | 48x96 | Beautiful view; door sticks at 20cm |
| Balcony View Backdrop | (432, 128) | 128x96 | Imperial Square vista, painted-postcard perfect |
| Bathroom Door Broken Lock | (560, 128) | 48x96 | HAS a lock. Lock rotates freely, engages nothing |
| Deluxe Vanity | (608, 128) | 64x64 | Mirror angled to reflect the bed |
| Deluxe Chaise | (672, 128) | 96x48 | Recamier lounge, permanently mid-fainting-couch drama |
| Deluxe Drapes | (768, 128) | 64x96 | Crimson velvet, drawn each night by no one |
| Writing Desk | (832, 128) | 64x64 | Stationery pre-addressed to your next of kin |

### The Royal Chamber (500 Sovs):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Royal Canopy Bed | (0, 288) | 160x144 | Palatial four-poster, canopy like a held breath |
| Portrait Wall Normal | (160, 288) | 192x128 | Six gilt-framed watchers in salon hang |
| Portrait Wall Meeting | (352, 288) | 192x128 | Subjects leaned toward each other mid-conference — seen only on return |
| Portrait Wall Facing Bed | (544, 288) | 192x128 | Portrait Party night event: every frame rotated toward the bed |
| Royal Fruit Mountain | (736, 288) | 96x64 | So much fruit. A monument of fruit. Eternal |
| Spa Bathroom Fixtures | (832, 288) | 96x96 | Gold fixtures; faucet heads carry subtle lens glints |
| Terrace Door | (928, 288) | 48x96 | Private terrace access, gold handle |

### Royal Chamber Details & Furniture-Shift Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Terrace Bars Decorative | (0, 480) | 128x96 | Iron bars painted gold — "decorative." The paint is fresh |
| Royal Throne Chair | (128, 480) | 64x80 | Overstuffed gilt armchair |
| Royal Wardrobe | (192, 480) | 80x96 | Your clothes already hung inside, sorted by color |
| Champagne Service | (272, 480) | 48x48 | Self-refilling flute and bucket |
| Royal Crest Rug | (320, 480) | 128x80 | Woven crest; threads spell WELCOME in three languages |
| Royal Chandelier Small | (448, 480) | 96x80 | Room-scale crystal fixture |
| Turndown Chocolate | (544, 480) | 24x24 | Always exactly where your head will land |
| Furniture Shift Ghost | (576, 480) | 96x80 | Faint outline overlay marking where the armchair USED to be |
| Belongings Organized | (672, 480) | 64x48 | The Rearrangement event: your items in a perfect grid |
| Belongings Before | (736, 480) | 64x48 | Your natural mess, for the before/after gut-punch |

### Shifting Hallways (Liminal Spaces):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hallway Door Identical | (0, 592) | 48x96 | The door. Every door. All of them |
| Hallway Door Yours-Maybe | (48, 592) | 48x96 | Identical, but with subtly warmer key light. Probably yours |
| Carpet Pattern A | (96, 592) | 64x64 | Baseline crimson-gold hallway carpet |
| Carpet Pattern B | (160, 592) | 64x64 | Same pattern, mirrored. You can't prove it changed |
| Carpet Pattern C | (224, 592) | 64x64 | Motifs now point toward your room. All of them |
| Hallway Sconce Lit | (288, 592) | 24x48 | Full flame |
| Hallway Sconce Dimming | (312, 592) | 24x48 | Mid-dim — triggered when player faces it |
| Hallway Sconce Dark | (336, 592) | 24x48 | Out. Relights when you look away |
| Hallway End Window | (360, 592) | 48x96 | Shows a garden the palace doesn't have |
| Corridor Junction Tile | (408, 592) | 64x64 | T-junction floor piece for the shifting maze |
| Door Number Blur | (472, 592) | 32x24 | Number plate mid-change, unreadable |
| Hallway Mirror | (504, 592) | 48x80 | Reflection runs a half-second late (two-frame swap) |
| Breakfast Room Door | (552, 592) | 48x96 | Double doors, buffet smell rendered as gold wisp |
| Exit Door Never Closer | (600, 592) | 48x96 | The front door as seen from any hallway. Distance constant |

### Technical Notes:
- Tier escalation must read as a visual rhyme: 1 portrait → 2 portraits → 6-portrait wall; modest basket → bigger basket → fruit mountain; no lock → broken lock → spa cameras. Same jokes, scaled
- The fruit basket sprite is reused across ALL tiers at different scales — pixel-identical fruit arrangement is the gag; do not redraw the fruit
- Carpet A/B/C and portrait wall states swap ONLY between room entries or on look-away (profile: timed reveals, not live motion)
- Rooms load per tier — only the booked tier's props enter memory

---

## 🖼️ Sprite Sheet 6: The Watching Portraits
**File:** `gilded_suite_portraits.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #2F2F2F (Backgrounds), #D4AF37 (Frames), #FFFDD0 (Faces), #8B0000 (Drapery)

### Portrait Subjects — Eye Tracking Frames (48x64 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Baron Eyes Left | (0, 0) | 48x64 | Stern Habsburg baron, eyes left |
| Baron Eyes Center | (48, 0) | 48x64 | Eyes center |
| Baron Eyes Right | (96, 0) | 48x64 | Eyes right |
| Baron Eyes Lock | (144, 0) | 48x64 | Direct eye contact — the Rule 5 four-second state |
| Baron Frame Empty | (192, 0) | 48x64 | Frame with no baron. He'll be back |
| Your-Face Portrait | (240, 0) | 48x64 | The Portrait Party gag: a portrait that is now, unmistakably, YOU |
| Your-Face Smiling Wider | (288, 0) | 48x64 | Your portrait, smiling more than you are |
| First Guest Portrait | (336, 0) | 48x64 | The 1784 guest, hung among the ancestors |
| Gastfreund 1784 Small | (384, 0) | 48x64 | Hallway copy of the basement original. Identical to the host |
| Empty Frame Dusty | (432, 0) | 48x64 | Basement spare frame, size suspiciously player-shaped |

### More Subjects — Eye Tracking (48x64 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Countess Eyes Left | (0, 64) | 48x64 | Countess with opera glasses (pointed at you) |
| Countess Eyes Center | (48, 64) | 48x64 | Eyes center |
| Countess Eyes Right | (96, 64) | 48x64 | Eyes right |
| Countess Eyes Lock | (144, 64) | 48x64 | Direct contact state |
| Child Eyes Left | (192, 64) | 48x64 | Period child with hoop toy. Obviously the creepy one |
| Child Eyes Center | (240, 64) | 48x64 | Eyes center |
| Child Eyes Right | (288, 64) | 48x64 | Eyes right |
| Child Eyes Lock | (336, 64) | 48x64 | Direct contact; hoop now absent |
| General Eyes Left | (384, 64) | 48x64 | Mustached general, medals for "Hospitality" |
| General Eyes Lock | (432, 64) | 48x64 | Direct contact state |

### Grand Portraits (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Grand Ancestor Left | (0, 128) | 64x96 | Foyer-scale ancestor, eyes left |
| Grand Ancestor Center | (64, 128) | 64x96 | Eyes center |
| Grand Ancestor Right | (128, 128) | 64x96 | Eyes right |
| Grand Ancestor Lock | (192, 128) | 64x96 | Direct contact |
| Meeting Pose A | (256, 128) | 64x96 | Subject leaning toward neighboring frame, mid-whisper |
| Meeting Pose B | (320, 128) | 64x96 | Subject leaning the other way, listening |
| Returned Slightly Wrong | (384, 128) | 64x96 | Back to normal but hung 2° crooked. It knows you noticed |
| Grand Frame Only | (448, 128) | 64x96 | Empty gilt frame for layered composition |

### Eye Components & Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Eye Glint Frame 1 | (0, 224) | 16x16 | Mechanical glint — Bradley was right about the components |
| Eye Glint Frame 2 | (16, 224) | 16x16 | Glint traverse |
| Eye Glint Frame 3 | (32, 224) | 16x16 | Glint settle |
| Eyes-Only Overlay Strip | (48, 224) | 96x32 | Detached eye pairs (L/C/R) for compositing onto any portrait |
| "Original Artwork" Plaque | (144, 224) | 48x16 | Brass label per Rule 5 |
| Four-Second Vignette | (192, 224) | 64x64 | Crimson edge cue that builds during sustained portrait eye contact |

### Gallery Composites:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hallway Portrait Row | (0, 288) | 192x96 | Four-frame corridor gallery strip |
| Staircase Portrait Cluster | (192, 288) | 160x96 | Salon-hang cluster for the selfie backdrop |
| Foyer Founder Portrait | (352, 288) | 96x128 | Massive founder portrait above reception. Guess who |

### Reduced-Motion & Colorblind Set:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Portrait Strip | (0, 416) | 192x96 | All subjects, eyes permanently center — motion-sensitivity mode |
| Static Eye Set Center | (192, 416) | 96x64 | Center-only eye overlays for reduced-motion compositing |
| Eye Direction Arrows | (288, 416) | 64x32 | Small arrow glyphs indicating gaze direction without eye movement |

### Technical Notes:
- Eye tracking is a frame SWAP (L/C/R/Lock), never a tween — per profile, subtle horror cues over obvious effects
- Portrait Party (Sheet 5, Portrait Wall Facing Bed) plus Your-Face Portrait combine for the Royal Chamber's major clue beat
- Lock frames must survive downscaling: pupils get a 1px Innocent Cream ring so eye contact reads at game resolution

---

## ✨ Sprite Sheet 7: Effects, Audio Cues & Accessibility Variants
**File:** `gilded_suite_effects.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #FFBF66 (Candlelight Amber), #8B0000 (Watchful Crimson), #D4AF37 (Palatial Gold), #FFFDD0 (Innocent Cream)

### Ambient & Audio-Cue Glyphs:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Soft Chime Glyph 1 | (0, 0) | 24x24 | Bell-shimmer glyph — visual cue for Gastfreund's appearance chime |
| Soft Chime Glyph 2 | (24, 0) | 24x24 | Shimmer expand |
| Soft Chime Glyph 3 | (48, 0) | 24x24 | Shimmer fade |
| Portrait Sting Flash | (72, 0) | 32x32 | Crimson accent burst — visual for the portrait-movement sting |
| Sad Trombone Notes | (104, 0) | 32x24 | Drooping brass notes — visual for the caught-snooping cue |
| Door Creak Arc | (136, 0) | 24x24 | Arc-lines glyph at hinges for every door creak |
| Footsteps-In-Wall 1 | (160, 0) | 32x32 | Bootprint impressions bulging through wallpaper |
| Footsteps-In-Wall 2 | (192, 0) | 32x32 | Alternate step — cadence matches the PLAYER's walk pattern |
| Wrong-Clock Tick Glyph | (224, 0) | 24x24 | Bent tick-marks radiating from clocks (audio: ticking wrong times) |
| Slow Waltz Note 1 | (248, 0) | 16x24 | Eighth note, drooping — the waltz is slightly too slow |
| Slow Waltz Note 2 | (264, 0) | 16x24 | Note sagging further |
| Dust Motes Arranged | (280, 0) | 64x64 | Dust particles hanging in a too-neat grid formation |
| Candle Flicker Sync 1 | (344, 0) | 16x24 | Flame lean left — ALL candles use this frame simultaneously |
| Candle Flicker Sync 2 | (360, 0) | 16x24 | Flame lean right, still unanimous |
| House Settling Whisper | (376, 0) | 48x24 | Dust-script text "…stay…" — Rule 12's visual form |

### Boss & Event Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Time Warp Swirl | (0, 64) | 64x64 | Gold clock-face spiral — One More Night attack |
| Service Shower Sparkle | (64, 64) | 64x64 | Cascading amenities glitter — Five-Star Service attack |
| Guest Book Spirits | (128, 64) | 64x64 | Testimonial wisps with tiny star trails — The Guest Book attack |
| Lock Slam Glyph | (192, 64) | 32x32 | Gold lock icon slamming shut — Checkout Denied attack |
| One-Star Projectile | (224, 64) | 24x24 | Single hollow star — the player's weapon of truth |
| Five-Star Halo | (248, 64) | 48x24 | Row of five filled stars orbiting charmed targets |
| Decision Paralysis Spiral | (296, 64) | 48x48 | Cream spiral over player during overwhelming kindness |
| Existential Question Mark | (344, 64) | 24x32 | Gold "?" — the vacation suggestion hitting home |
| Materialize Shimmer | (368, 64) | 48x64 | Candlelight coalescence for host/porter appearances |
| Eye-Tracking Motion Lines | (416, 64) | 32x24 | Two faint arcs beside portrait eyes on swap frames |

### Environment & UI Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Surveillance Corner Vignette | (0, 128) | 64x64 | Soft crimson iris creeping into one screen corner |
| 3AM Knock Ripple | (64, 128) | 32x32 | Concentric rings on door per knock |
| Basement Reveal Dust | (96, 128) | 48x48 | Dust burst when the fruit painting swings open |
| Engine Steam Puff 1 | (144, 128) | 24x32 | Hospitality Engine exhalation |
| Engine Steam Puff 2 | (168, 128) | 24x32 | Puff dissolve |
| Engine Gauge Glow | (192, 128) | 32x32 | Amber gauge bloom for Active state |
| Checkout Tick FX | (224, 128) | 24x24 | Pulse on the checkout clock as 11 AM nears |
| Eternal Fruit Gleam | (248, 128) | 16x16 | The fruit's highlight. Identical in every frame it appears. Always |
| Watched Border Pulse | (264, 128) | 64x32 | Screen-edge crimson band, static-friendly (opacity step, no motion) |
| Chandelier Sparkle | (328, 128) | 32x32 | Crystal glint for foyer beauty shots |
| Elevator Ding Glyph | (360, 128) | 24x24 | Ding visual — fires before the button is pressed |
| Name-At-Night Text | (384, 128) | 64x24 | Your character's name rendered in settling-dust font (Rule 12) |

### High-Contrast & Static Accessibility Variants:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| HC Gastfreund Outline | (0, 192) | 48x96 | Cream outline silhouette — host visible against any shadow |
| HC Fruit Painting Outline | (48, 192) | 96x112 | High-contrast rim on the basement entrance interactable |
| HC Guest Book Outline | (144, 192) | 48x32 | Reception interactable highlight |
| HC Release Lever Outline | (192, 192) | 32x48 | Emergency exit puzzle piece, enhanced visibility |
| HC Basement Stair Marker | (224, 192) | 48x48 | Discovered-entrance marker |
| Static Sconce Set | (272, 192) | 72x48 | Three sconces at fixed brightness — no dimming behavior |
| Static Carpet Pattern | (344, 192) | 64x64 | One carpet. It never changes. Peace |
| Static Fountain Eyes | (408, 192) | 96x96 | Fountain with eyes locked forward permanently |

### Supplementary Visual Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Knock Visual Burst | (0, 304) | 32x32 | Star-burst at door for each 3AM knock (deaf-accessible knock) |
| Music Box Note | (32, 304) | 16x24 | Undertone melody glyph for basement ambience |
| Static Watched Icon Frame | (48, 304) | 64x32 | Non-pulsing replacement for Watched Border Pulse |

### Technical Notes:
- ALL audio events in this location have a paired glyph on this sheet — the horror must work on mute
- Particle systems are minimal by design (profile: subtle cues over obvious effects): dust grid, engine steam, and service sparkle never run concurrently
- Watched Border Pulse animates by opacity step (3 levels), not translation — vestibular-safe by default

---

## 🗝️ Sprite Sheet 8: UI & Items
**File:** `gilded_suite_ui.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #D4AF37 (Palatial Gold), #FFFDD0 (Innocent Cream), #8B0000 (Watchful Crimson), #2F2F2F (Something Wrong)

### Key Items:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Room Key Standard | (0, 0) | 32x32 | Brass key, tag reads "217" (subject to change) |
| Room Key Deluxe | (32, 0) | 32x32 | Brass key, red tassel |
| Room Key Royal | (64, 0) | 32x32 | Gold key, crest tag, faintly warm |
| Guest Agreement | (96, 0) | 48x64 | 27-clause scroll; fine print spirals inward hypnotically |
| House Rules Document | (144, 0) | 64x96 | Full readable UI art — Rule 6 removed for your comfort, Rule 8 gilded |
| Eternal Guest Card | (208, 0) | 48x32 | Gold card: free stays, no surveillance, rule immunity |
| Honest Review Badge | (256, 0) | 32x32 | One-star medallion worn with pride — fake-review immunity citywide |
| Being Watched Indicator | (288, 0) | 32x32 | Gold-lidded eye debuff icon (-5% stealth) |
| Being Watched Pattern Variant | (320, 0) | 32x32 | Same icon with hatched texture for colorblind mode |
| Checkout Clock UI | (352, 0) | 64x64 | Countdown dial to 11 AM; hand trembles in final hour |
| Basement Clue Icon | (416, 0) | 48x48 | Furniture-arrangement diagram left by The Rearrangement |
| Eternal Fruit Basket Item | (464, 0) | 48x48 | Inventory art. Cannot be eaten. Cannot be discarded. Is |

### Night Event Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Night Event Banner | (0, 96) | 256x64 | "3:00 AM" header panel, crimson on Something Wrong |
| Night Event Choice Card | (256, 96) | 128x48 | Option card: Answer / Ignore / Investigate |
| Night Event Choice Selected | (256, 144) | 128x48 | Gold-rimmed selected state |
| Star Rating Filled | (384, 96) | 96x24 | ★★★★★ display row |
| Star Rating One Star | (384, 120) | 96x24 | ★☆☆☆☆ — the weapon |
| Review Bubble UI | (384, 144) | 96x48 | Review-text frame for guest dialogue |

### Booking & Status:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Room Tier Card Standard | (0, 192) | 96x64 | 150 Sovs — "Basic creepy." 80% HP/SP |
| Room Tier Card Deluxe | (96, 192) | 96x64 | 300 Sovs — "Extra portraits." 100% HP/SP |
| Room Tier Card Royal | (192, 192) | 96x64 | 500 Sovs — "Full experience." 120% + buff |
| Well-Rested Buff Icon | (288, 192) | 32x32 | Crown-and-pillow icon |
| Overstayed Welcome Debuff | (320, 192) | 32x32 | Door-with-no-handle icon — trapped state |
| Surveillance Level Pips | (352, 192) | 64x16 | Camera pips: Medium / High / Maximum |
| House Rule Entry Line | (352, 208) | 160x24 | Rule-log line item for the documentation quest |
| Rule Documented Check | (288, 232) | 24x24 | Gold check with tiny star |

### Quest & Social:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Guest Book UI Page | (0, 256) | 128x96 | Signature page — 240 years of names converging into one hand |
| Achievement Toast | (128, 256) | 160x48 | Banner for Check In / Survived / Night Watch / etc. |
| Eternal Guest Card Glow | (128, 304) | 48x32 | Award-moment variant with gold bloom |
| Refund Notice 500 Sovs | (176, 304) | 64x32 | Confrontation victory payout slip |
| Selfie Frame Palace Life | (288, 256) | 96x96 | Staircase selfie overlay, chandelier visible |
| Selfie Frame The Watched | (384, 256) | 96x96 | Variant: portraits in background, all facing camera |
| Checkout Receipt | (0, 352) | 64x32 | Stamped 10:59 AM. Cutting it close |
| 11AM Warning Banner | (64, 352) | 96x32 | Static "CHECKOUT: 11:00" strip, no flashing |
| Emergency Release Icon | (160, 352) | 32x32 | Early-exit puzzle progress marker |

### Technical Notes:
- All interactive UI elements built to 44px+ effective touch size at runtime scale (cards, choice buttons, tier cards)
- Star ratings pair fill-state with count — never color-only
- House Rules Document must be legible at full-screen zoom; it is the location's single most screenshot-able asset

---

## 🎬 Animation Specifications

### Gastfreund Materialize:
- **Duration:** 0.6 seconds
- **Frames:** 3
- **Pattern:** Frame 1 → 2 → 3, hold; play reversed for departure
- **Trigger:** Host spawn events (check-in, night visit, boss phases, "when needed and when not needed")
- **Purpose:** He doesn't walk in. He is simply there. The signature dread-beat
- **Audio Sync:** Soft chime begins on frame 1, resolves on frame 3 (paired glyph: Soft Chime Glyph 1–3)
- **Mobile Optimization:** 2-frame version (skip frame 2) on low-end devices

### Portrait Eye Tracking:
- **Duration:** 0.2 seconds per gaze step (frame swap, no tween)
- **Frames:** 4 per subject (Left / Center / Right / Lock)
- **Pattern:** Gaze frame matches player's relative position; Lock fires on direct approach
- **Trigger:** Player movement past any portrait
- **Purpose:** The core ambient wrongness — cheap to run, impossible to unsee
- **Audio Sync:** Sting on FIRST Lock per room entry only (paired glyph: Portrait Sting Flash)
- **Mobile Optimization:** Update gaze at 0.4s intervals on low-end; static center frames in reduced-motion mode

### Portrait Party Reveal (Royal Chamber):
- **Duration:** Instant swap (0 seconds — a timed reveal, not an animation)
- **Frames:** 2 states (Portrait Wall Normal → Facing Bed, plus Your-Face Portrait insert)
- **Pattern:** State swap while screen is dark during wake-up transition
- **Trigger:** "The Portrait Party" night event (Very Rare, Royal only)
- **Purpose:** The game's best jump-scare-that-isn't: nothing moves, everything changed
- **Audio Sync:** Sting on reveal; slow waltz resumes 1.5 seconds later, slightly slower than before
- **Mobile Optimization:** None needed — static swap is already the optimized form

### Sconce Dimming:
- **Duration:** 0.8 seconds (lit → dimming → dark)
- **Frames:** 3
- **Pattern:** Advance one frame while player faces sconce; relight instantly off-screen
- **Trigger:** Player look direction
- **Purpose:** The hallway pretends to sleep when watched
- **Audio Sync:** None
- **Mobile Optimization:** Static Sconce Set replaces behavior entirely in reduced-motion / Low LOD

### 3AM Visit Sequence:
- **Duration:** 4.5 seconds (three knocks over 1.5s → 3s waiting hold)
- **Frames:** 2 host frames (Knock, Waiting) + Knock Ripple + Knock Visual Burst
- **Pattern:** Knock ×3 → hold Waiting until player chooses Answer / Ignore / Investigate
- **Trigger:** "The Visit" night event (Common)
- **Purpose:** The tentpole night event — comedy timing lives in the 3-second silence
- **Audio Sync:** Door knock on each ripple; door creak if Answered; muffled "just checking in" during Waiting
- **Mobile Optimization:** None needed

### Footsteps in the Walls:
- **Duration:** Matches player's step cadence exactly (sampled, typically 0.5s alternation)
- **Frames:** 2
- **Pattern:** Frame A ↔ B along wallpaper, mirroring player movement; stops 0.3 seconds AFTER the player stops
- **Trigger:** First night onward, hallways and Standard/Deluxe rooms
- **Purpose:** Bradley's line made visible: "The footsteps match our walking patterns"
- **Audio Sync:** Muffled in-wall footsteps sample-locked to player footfall audio; glyph IS the deaf-accessible cue
- **Mobile Optimization:** Audio-only on Low LOD with subtitle cue "(footsteps, yours, inside the wall)"

### Hospitality Attacks (Boss — one spec each, shared timing):
- **Duration:** 1.0 second per attack cast
- **Frames:** 2 cast frames + 1 effect sprite each (Time Warp Swirl / Service Shower Sparkle / Guest Book Spirits / Lock Slam Glyph)
- **Pattern:** Cast 1 (0.4s) → Cast 2 (0.6s) → effect resolves on UI
- **Trigger:** Herr Gastfreund social-combat rotation: One More Night → Five-Star Service → The Guest Book → Checkout Denied
- **Purpose:** Menace rendered as customer service; each attack is a hotel amenity weaponized
- **Audio Sync:** One More Night: clock ticking wrong, accelerating; Five-Star Service: waltz swells (still too slow); The Guest Book: whispered testimonials; Checkout Denied: every door in the palace locking in sequence, distant to near
- **Mobile Optimization:** Effect sprites render at half opacity without particle trails on Low LOD

### Sad Doorway Wave:
- **Duration:** 2.4 seconds, looping until player leaves the garden
- **Frames:** 3
- **Pattern:** Raise (0.6s) → wave (1.2s) → lower-but-not-quite (0.6s), loop from wave
- **Trigger:** Player checkout / escape — final shot of the location
- **Purpose:** The horror's last word is heartbreak. He'll miss you. He means it. That's the problem
- **Audio Sync:** Slow waltz, solo music-box arrangement, fading with distance
- **Mobile Optimization:** None needed

### First Guest Tearful Checkout:
- **Duration:** 2.0 seconds
- **Frames:** 2 (Tearful Checkout 1 → 2) + Departing Free hold
- **Pattern:** Single play at quest resolution, then Departing Free walk-off
- **Trigger:** "The First Guest" quest completion at the Original Checkout Desk
- **Purpose:** 240 years of confusion resolving into the game's most sincere emotional beat
- **Audio Sync:** Quill scratch, ledger thump, then the FIRST correctly-timed clock chime in the whole building (11:00, and for once it is actually 11:00)
- **Mobile Optimization:** None needed

### Synchronized Guest Turn:
- **Duration:** 0.6 seconds
- **Frames:** 2 (group sprites)
- **Pattern:** Single play when player enters breakfast room; hold on frame 2
- **Trigger:** Breakfast room entry with Other Guests present
- **Purpose:** Three heads, one motion, zero comfort
- **Audio Sync:** Fabric rustle in unison; waltz skips one beat
- **Mobile Optimization:** None needed

### Hospitality Engine Loop:
- **Duration:** 1.2 second cycle
- **Frames:** 2 (Idle ↔ Active gauge glow) + steam puffs (2 frames, 0.6s each)
- **Pattern:** Continuous loop, basement only
- **Trigger:** Basement discovery
- **Purpose:** The truth has a heartbeat, and it's rated five stars
- **Audio Sync:** Deep mechanical heartbeat; music box undertone; steam hiss per puff
- **Mobile Optimization:** Steam disabled on Low LOD; gauge glow becomes static Active frame

### Minibar Restock:
- **Duration:** 0.4 seconds, single play
- **Frames:** 2 (Cabinet → Restocking → Cabinet)
- **Pattern:** Fires only while the player is LOOKING at the minibar
- **Trigger:** Random interval during room occupancy
- **Purpose:** It restocks while you watch. That's the joke. That's the horror
- **Audio Sync:** Single glass clink
- **Mobile Optimization:** None needed

### Eternal Fruit Gleam:
- **Duration:** 0 seconds — one frame, permanent
- **Frames:** 1
- **Pattern:** The gleam never moves, never varies, never dies
- **Trigger:** Constant on every fruit basket in every tier
- **Purpose:** Rule 8: The fruit is complimentary. The fruit is eternal
- **Audio Sync:** None. The fruit is silent
- **Mobile Optimization:** It is already perfect

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| HC Gastfreund Outline | (0, 192) on effects sheet | 48x96 | Cream silhouette rim — host readable against Something Wrong shadows |
| HC Fruit Painting Outline | (48, 192) on effects sheet | 96x112 | Basement entrance interactable, enhanced visibility |
| HC Guest Book Outline | (144, 192) on effects sheet | 48x32 | Reception interaction marker |
| HC Release Lever Outline | (192, 192) on effects sheet | 32x48 | Early-exit puzzle lever highlight |
| HC Basement Stair Marker | (224, 192) on effects sheet | 48x48 | Discovered-passage marker |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Portrait Strip | (0, 416) on portraits sheet | 192x96 | All portrait eyes locked center — no tracking, ever |
| Static Eye Set Center | (192, 416) on portraits sheet | 96x64 | Center-only overlays for composited portraits |
| Eye Direction Arrows | (288, 416) on portraits sheet | 64x32 | Gaze conveyed by small arrows instead of moving eyes |
| Static Sconce Set | (272, 192) on effects sheet | 72x48 | Fixed-brightness sconces, no look-triggered dimming |
| Static Carpet Pattern | (344, 192) on effects sheet | 64x64 | Carpet never shifts between visits |
| Static Fountain Eyes | (408, 192) on effects sheet | 96x96 | Fountain gaze fixed forward |
| Static Watched Icon Frame | (48, 304) on effects sheet | 64x32 | Non-pulsing surveillance indicator |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Soft Chime Glyphs 1–3 | (0–48, 0) on effects sheet | 24x24 ea | Visual for Gastfreund's appearance chime |
| Portrait Sting Flash | (72, 0) on effects sheet | 32x32 | Visual for the portrait-movement sting |
| Sad Trombone Notes | (104, 0) on effects sheet | 32x24 | Visual for the caught-while-snooping cue |
| Door Creak Arc | (136, 0) on effects sheet | 24x24 | Visual for every door creak |
| Footsteps-In-Wall 1–2 | (160–192, 0) on effects sheet | 32x32 ea | Visual for in-wall footsteps matching player cadence |
| Wrong-Clock Tick Glyph | (224, 0) on effects sheet | 24x24 | Visual for clocks ticking wrong times |
| Slow Waltz Notes 1–2 | (248–264, 0) on effects sheet | 16x24 ea | Visual for the too-slow waltz |
| House Settling Whisper | (376, 0) on effects sheet | 48x24 | Visual for name-like settling sounds (Rule 12) |
| Knock Visual Burst | (0, 304) on effects sheet | 32x32 | Visual for 3AM knocks |
| Elevator Ding Glyph | (360, 128) on effects sheet | 24x24 | Visual for the premature elevator ding |

### Colorblind Considerations:
- Being Watched debuff ships a hatched-pattern variant (ui sheet, (320, 0)) — surveillance state never conveyed by crimson tint alone
- Star ratings pair fill-state (solid vs. hollow outlines) with count; the one-star weapon is shape-distinct, not color-distinct
- Portrait gaze direction available as arrow glyphs for players who can't parse pupil contrast
- Room tier cards use distinct crest silhouettes (plain / double / crowned), not only gold-level tinting
- Touch zones minimum 44px for booking cards, night-event choices, guest book, fruit painting, and checkout interactions

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); portraits sheet needs ASTC 4x4 — pupil positions must survive compression or the whole location dies
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for `gilded_suite_portraits.png` and `herr_gastfreund.png` (eye detail is gameplay-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| gilded_suite_environment | exterior, tileset, rooms | 2048x2048 |
| gilded_suite_characters | herr_gastfreund, npcs, portraits | 1024x1024 |
| gilded_suite_effects_ui | effects, ui | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full eye tracking (0.2s), sconce dimming, dust grid, engine steam, all glyph cues, footsteps-in-wall sprites |
| Medium | Eye tracking at 0.4s intervals, no dust motes, engine steam halved, sconce dimming retained |
| Low | Static portrait strip, static sconces, no ambient particles, night events as instant state swaps, footsteps-in-wall audio+subtitle only |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 18 per frame
- **Memory Footprint:** 45 MB maximum
- **Particle Limit:** 12 (dust grid 8 OR engine steam 4 OR service sparkle 12 — never concurrent)

### Performance Notes:
- Rooms load per tier — only the booked tier's sprite set enters memory; Royal's portrait walls are the heaviest single load and never coexist with Standard/Deluxe assets
- Night events are triggered state SWAPS, not animation loops (per profile: static backgrounds, timed reveals) — Portrait Party, Rearrangement, and carpet shifts cost zero runtime animation
- Basement assets (engine, records, First Guest) load on-demand at discovery; pre-discovery players never pay for them
- Hallway "shifting" is implemented as tile re-index on room transition — one TileMap, zero extra draw calls
- Gastfreund is a single AnimatedSprite2D reused across all encounters; his materialize shimmer shares the porter's effect sprite

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- AnimatedSprite2D for Gastfreund, First Guest, porter, and guest states; TileMap for foyer/hallway/basement; static Sprite2D room bases
- CPUParticles2D (not GPU) for dust grid, engine steam, service sparkle — respecting the 12-particle cap
- Portrait gaze driven by a single `PortraitWatcher` script: computes player-relative angle, swaps region_rect among L/C/R/Lock — no per-portrait animation players
- Location state machine: `pre_stay → night_1..n → basement_discovered → boss_available → resolved_(first_guest|honest_review|eternal_guest)` drives sprite set swaps
- Night event scheduler rolls Common/Uncommon/Rare/Very Rare per rest; Portrait Party gated to Royal Chamber flag
- Elevator floor indicator reads the player's booked-tier variable — render only that floor number

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Gastfreund materialize | Soft chime | Begins frame 1, resolves frame 3 |
| Portrait eye Lock (first per room) | Horror-comedy sting | On Lock frame swap |
| Caught snooping (basement/staff door) | Sad trombone | On detection state |
| Any door open/close | Directed creak | On door state swap |
| Footsteps-in-wall sprites | Muffled in-wall footsteps | Sample-locked to player footfall |
| All clock sprites | Ticking at wrong tempos | Continuous, desynced per clock |
| Foyer/breakfast ambience | Waltz slightly too slow | Continuous; skips one beat on synchronized guest turn |
| 3AM Knock Ripple | Triple knock | One knock per ripple |
| Checkout Denied cast 2 | Every door locking, far to near | Over 0.6s cast frame |
| First Guest checkout | First correct 11:00 chime | On ledger signature |
| Sad Doorway Wave | Music-box waltz solo | Loops, fades with player distance |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The First Guest | First Guest full state set, Original Checkout Desk, shifting hallway tiles, riddle UI | Basement discovery → puzzle boss → Tearful Checkout → Eternal Guest Card award |
| House Rules | House Rules Frame, House Rules Document UI, Rule Entry Line, Rule Documented Check | Player logs all 27 rules; Rule 6's absence is itself an entry |
| Honest Review | Gastfreund attack states, One-Star Projectile, all four attack effects, Mildly Distressed set, Refund Notice | Post-basement escape attempt triggers social combat; one-star review is the finisher |
| Eternal Guest | Room tier cards, night event set, Eternal Guest Card + Glow, Gastfreund Eternal Guest Nod | Multi-night stay track unlocking all night events and content |
| Achievements (Check In / Survived / Night Watch / Rule Follower / Basement Tourist / Helped Check Out / Honest Reviewer / Eternal Guest) | Achievement Toast + respective quest sprites | Toast fires on each milestone |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Moderato Pub | Couchsurfing comparison UI (rest-quality cards referenced side by side); no shared world sprites | Standard door transition; comparison dialogue triggers |
| Café Existenz | Rumor dialogue references exterior art ("the palace that traps tourists") | None — reputation travels, sprites don't |
| The Black-Tie Backroom | Lost Items Shelf includes a Black-Tie chip tray — guests who gambled and never came back | None; environmental cross-reference only |
| Citywide Bulletin Boards | Bulletin Ad Poster (688, 320 on exterior sheet) reused on every board | Poster tap → map marker for the Gilded Suite |
| Imperial Square | Shared Imperial District cobblestone/lamppost tiles | Street-level walk-in, exterior night overlay handoff |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Five-star perfection held one degree too long"
- **Color Mood:** Innocent Cream and Palatial Gold doing 90% of the talking; Watchful Crimson only where the building's attention shows; Something Wrong pooling in corners the chandeliers can't reach
- **Lighting:** Warm chandelier glow and candlelight amber throughout — the horror is never dark, it's beautifully lit; spotlit portraits; basement in verdigris half-light
- **Texture:** Polished marble, fresh gilt, pressed linen — zero decay. The wrongness is that nothing is worn, nothing is dusty, nothing has aged since 1784

### Environmental Storytelling:
- Neighboring buildings lean away; the fountain watches; the welcome mat's last letter trails off — the exterior warns you before a single line of dialogue
- Identical handwriting across 240 years of guest book; awards-and-plaques absent entirely (the reviews ARE the awards); one modern suitcase in the basement lost-items pile does more work than any lore dump
- Escalation-by-tier is the satire engine: pay more, get watched more, and the game prices it like an amenity
- Rule 6 is missing from the framed rules. No asset explains why. No asset ever will

### Character Integration Notes:
- Herr Gastfreund renders at full opacity always — no ghost translucency; he is unbearably PRESENT, that's the point
- Other Guests get 10% desaturation and period-mismatched wardrobes; they should read as "happy customers" for a full second before they read as wrong
- The First Guest is the only NPC drawn in unfiltered period color — visually free even before he's actually freed
- The Porter's face is a rendering rule, not a sprite choice: cap shadow in all seven frames, no exceptions

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Portrait Party** — waking to a wall of portraits rotated toward the bed, one of them now wearing your face
2. **The inches-away morning greeting close-up** — "I never left. *smile* More coffee?" filling the whole dialogue box
3. **The House Rules document** — 27 rules of escalating dread, Rule 6 conspicuously removed for your comfort
4. **The Survived selfie** — bags packed, fleeing at 10:59 AM, Herr Gastfreund waving sadly in the doorway

### TikTok Potential:
- "POV: your Airbnb host says he 'never left'"
- "Rating hotel red flags: the bathroom door has no lock, the fruit is eternal, the elevator knows your floor"
- "When the 5-star reviews are all the same sentence" *zoom on three guests chanting in unison*
- "He's not a monster, he just really doesn't want you to check out" *sad doorway wave, music-box waltz*

### Quote Potential:
- "Rest Well. We're Watching."
- "The breakfast buffet is exceptional. Five stars. Never leaving."
- "I never left. *smile* More coffee?"
- "Checkout is at 11 AM. This is non-negotiable."
- "The fruit is complimentary. The fruit is eternal." — House Rule 8
- "A guest who leaves is a failure of hospitality." — Herr Gastfreund

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | gilded_suite_exterior.png | 1024x512 |
| 2 | gilded_suite_tileset.png | 1024x768 |
| 3 | herr_gastfreund.png | 512x512 |
| 4 | gilded_suite_npcs.png | 512x384 |
| 5 | gilded_suite_rooms.png | 1024x768 |
| 6 | gilded_suite_portraits.png | 512x512 |
| 7 | gilded_suite_effects.png | 512x384 |
| 8 | gilded_suite_ui.png | 512x384 |

**Total Estimated Memory:** ~12.3 MB (uncompressed RGBA at ~4 bytes/pixel; well inside the 45 MB location budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `gilded_suite_exterior.png` (1024x512)
- [ ] `gilded_suite_tileset.png` (1024x768)
- [ ] `herr_gastfreund.png` (512x512)
- [ ] `gilded_suite_npcs.png` (512x384)
- [ ] `gilded_suite_rooms.png` (1024x768)
- [ ] `gilded_suite_portraits.png` (512x512)
- [ ] `gilded_suite_effects.png` (512x384)
- [ ] `gilded_suite_ui.png` (512x384)

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
- **Backup:** Master PSD/layered file with organized layer groups (portrait eye layers separated per subject)
- **Documentation:** Animation timing reference sheet + night-event state-swap guide + portrait gaze-angle table

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] Portrait eyes read clearly at game resolution — pupil positions distinguishable across L/C/R/Lock on a 5-inch screen
- [ ] Herr Gastfreund's eyes are open in every single frame, including distress and farewell states
- [ ] Horror stays comedic: no gore, no jump-scare compositions — polite menace and subtle wrongness only
- [ ] The fruit basket is pixel-identical everywhere it appears (Standard, Deluxe, Royal scale variants share one arrangement; the gleam never varies)
- [ ] The three room tiers escalate visibly (portraits 1→2→6, fruit modest→more→mountain, locks none→broken→cameras)
- [ ] Synchronized candle frames are truly synchronized — every flame the same frame
- [ ] Guest book handwriting reads as "suspiciously similar" at zoom
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets — rental-culture jokes visible without dialogue
- [ ] Hidden areas/interactions have discoverable visual cues (fruit painting rim light, basement clue, lever outline)
- [ ] Mobile performance optimized (CPU particles ≤12, atlas limits respected, 60 FPS / 18 draw calls / 45 MB honored)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices (Portrait Party and doorway wave framed for capture)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; Viennese palace-hotel culture evoked, never named |
| Cultural Specificity | ✅ | Habsburg palace tourism, Austrian Gemütlichkeit weaponized, imperial-gold hospitality theater |
| Satirical Targets Appropriate | ✅ | Short-term rental culture, fake reviews, surveillance hosts, agreement-skipping bros — punches up, never at housing-insecure people |
| Seedy Underbelly Present | ✅ | Surveillance-as-service, fabricated reviews, 240 years of guest entrapment, forged "historic" claims |
| Gameplay Value Established | ✅ | Three-tier rest system, night events, optional dungeon, puzzle boss + social-combat boss, two unique reward items |
| Technical Feasibility | ✅ | Eight sheets, atlas plan, LOD tiers, per-tier loading documented |
| Mobile Performance Budget | ✅ | 60 FPS, 18 draw calls, 45 MB, 12 particles (per profile) |
| Accessibility Features | ✅ | Visual glyph for every audio cue; static variants for all motion triggers; colorblind patterns |
| No Crypto Elements | ✅ | None present |
| Social Media Integration | ✅ | Portrait Party, morning close-up, House Rules, and Survived selfie identified |

**The Gilded Suite: where the reviews are five stars, the fruit is eternal, the host never blinks — and once these assets are delivered, every player will learn exactly why checkout at 11 AM is the only rule worth keeping.**
