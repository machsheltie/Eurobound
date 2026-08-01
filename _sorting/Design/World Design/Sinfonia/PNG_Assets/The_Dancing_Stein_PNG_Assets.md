# The Dancing Stein - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for The Dancing Stein — a MusikGasse waltz pub where the beer swirls in three-quarter time, the door rotates at waltz tempo, and you cannot get served until you've taken at least three steps in rhythm. It satirizes Vienna's waltz obsession by turning a simple drink order into a mandatory dance performance that nobody — staff included — actually performs well, while everyone agrees to pretend the shuffling is elegant. The location hosts Brewery Tour stamp #4 and the Stein Waltz rhythm challenge: a full circuit of the dance floor carrying a full beer, judged against the acceptable-loss line marked on the stein.

**Location ID:** `sinfonia_musikgasse_dancing_stein_01`
**Theme:** Waltz culture as mandatory tradition — rhythmic gatekeeping, dance snobbery, the "authentic Viennese experience" nobody can actually execute
**Zone:** MusikGasse, Street Performer District
**Hours:** 5 PM – 2 AM (waltz hours)
**Primary Function:** Pub / Brewery Tour stamp location #4 / rhythm QTE challenge venue ("The Stein Waltz") / buff-and-status economy (Graceful, Two Left Feet, Light on Your Feet) / selfie spot

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Ballroom Gold | #DAA520 | Chandeliers, trim, stamp ink, gilded décor, exterior sign |
| Waltz Blue | #4169E1 | Accent details, stamp accents, UI rhythm elements, Frau Schritt's dress |
| Polished Wood | #8B4513 | Dance floor, bar structure, wall paneling, furniture |
| Foam White | #FFFAF0 | Beer foam, shirt fronts, mirror highlights, spill splashes |
| Copper Shine | #B87333 | Bar top, taps, keg fittings (sensible addition — profile calls for a copper bar) |
| Cellar Stone | #6E6658 | Cellar walls, spiral stairs, keg alcove (sensible addition) |
| Sheet Music Cream | #F5EEDC | Wallpaper base, menu cards, passport page (sensible addition) |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/dancing_stein/
├── environment/
│   └── dancing_stein_tileset.png
├── npcs/
│   ├── herr_drehmeister.png
│   └── dancing_stein_npcs.png
├── objects/
│   ├── dancing_stein_landmarks.png
│   └── dancing_stein_challenge_items.png
├── effects/
│   └── dancing_stein_effects.png
└── ui/
    ├── dancing_stein_ui.png
    └── dancing_stein_accessibility.png
```

---

## 🏛️ Sprite Sheet 1: Interior & Exterior Tileset
**File:** `dancing_stein_tileset.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #8B4513 (Polished Wood), #DAA520 (Ballroom Gold), #B87333 (Copper Shine), #6E6658 (Cellar Stone), #F5EEDC (Sheet Music Cream)

### Floor Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Polished Hardwood A | (0, 0) | 32x32 | Dance floor base, high-gloss grain |
| Polished Hardwood B | (32, 0) | 32x32 | Variation tile, breaks repetition |
| Floorboard "1" | (64, 0) | 32x32 | Hardwood with subtle painted "1" |
| Floorboard "2" | (96, 0) | 32x32 | Hardwood with subtle painted "2" |
| Floorboard "3" | (128, 0) | 32x32 | Hardwood with subtle painted "3" — tiles lay in waltz sequence |
| Sticky Practice Floor | (160, 0) | 32x32 | Practice corner — matte, slightly tacky sheen for grip |
| Sticky Floor Scuffed | (192, 0) | 32x32 | Practice corner with beginner scuff marks |
| Cellar Stone Floor | (224, 0) | 32x32 | Below the dance floor, cool grey-brown |
| Perimeter Rest Carpet | (256, 0) | 32x32 | Earned-rest zone under tables, waltz-blue weave |
| Floor Shine Overlay | (288, 0) | 32x32 | Additive gloss tile for chandelier reflections |
| Spilled Beer Decal | (320, 0) | 32x32 | Wet patch left by failed Stein Waltz runs |

### Wall Tiles (32x64 unless noted):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wood Panel Wall | (0, 32) | 32x64 | Dark polished wainscoting |
| Sheet Music Wallpaper A | (32, 32) | 32x64 | Waltz notation pattern on cream |
| Sheet Music Wallpaper B | (64, 32) | 32x64 | Notation variant with handwritten drink-pairing annotations ("Blue Danube — pairs with Weizen") |
| Sheet Music Wallpaper C | (96, 32) | 32x64 | Notation variant, annotation "Allegro — Tango IPA" |
| Mirror Panel | (128, 32) | 32x64 | Wall mirror for checking your form |
| Mirror Panel (Flattering) | (160, 32) | 32x64 | Slightly warped mirror for checking your ego — everyone looks 10% more graceful |
| Window w/ Dancing Silhouettes | (192, 32) | 32x64 | Painted waltzing-couple silhouettes, street-visible |
| Cellar Stone Wall | (224, 32) | 32x64 | Rough stone with keg-ring stains |
| Gilded Chair Rail | (256, 32) | 32x64 | Ballroom gold molding strip |
| "1-2-3" Baseboard Stencil | (288, 32) | 32x32 | Subtle gold stencil where wall meets floor |

### Furniture & Bar Sections:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Perimeter Table | (0, 96) | 32x32 | Small round table — for those who've earned rest |
| Table w/ Metronome | (32, 96) | 32x32 | Perimeter table, metronome set to waltz tempo |
| Bentwood Chair | (64, 96) | 24x32 | Dark wood, technically permitted |
| Chair (Pulled Out) | (88, 96) | 24x32 | Post-dance collapse position |
| Copper Bar Straight | (112, 96) | 64x48 | Long copper bar section, back wall |
| Copper Bar Corner | (176, 96) | 48x48 | Rounded corner — no sharp edges near dancers |
| Tap Array (Dancing Reach) | (224, 96) | 64x48 | Six taps angled outward in an arc so a waltzing bartender can pour mid-turn |
| Back-Bar Stein Shelf | (288, 96) | 64x48 | Glassware racked at sway-safe spacing |
| Practice Corner Barre | (352, 96) | 64x32 | Ballet-style rail, beginner handhold |
| Cellar Keg Rack | (416, 96) | 64x48 | Spinning Brewery kegs, fresh delivery |

### Large Structures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Spiral Stairs (Top Flight) | (0, 144) | 64x80 | Stairs down to cellar — they spiral, naturally |
| Spiral Stairs (Mid Flight) | (64, 144) | 64x80 | Continuation curve, stone and wood |
| Cellar Stamp Alcove | (128, 144) | 96x80 | Arched alcove framing the stamp ceremony spot |
| Rotating Door Housing | (224, 144) | 64x80 | Static door frame/case (animated leaves live on Sheet 4) |
| Practice Corner Assembly | (288, 144) | 96x80 | Full corner: sticky floor, barre, encouragement posters |
| Ballroom Chandelier | (384, 144) | 80x64 | Warm gold crystal, selfie-spot anchor |

### Waltz Décor Gags:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dancing Couple Figurine A | (0, 224) | 16x24 | Porcelain waltzers, mid-turn — on every surface |
| Dancing Couple Figurine B | (16, 224) | 16x24 | Variant pose, dip |
| Dancing Couple Figurine C | (32, 224) | 16x24 | Variant pose, one figurine visibly gluing back on a broken arm |
| Table Metronome (Tick A) | (48, 224) | 16x24 | Pendulum left, set to 3/4 |
| Table Metronome (Tick B) | (64, 224) | 16x24 | Pendulum right — alternates with Tick A |
| "No Sitting Permitted" Sign | (80, 224) | 48x32 | Brass sign; there are actually seats, but the sign stays |
| Dancing Shoes Case A | (128, 224) | 48x64 | Glass display: cracked 1890s ballroom slippers, brass plaque |
| Dancing Shoes Case B | (176, 224) | 48x64 | Glass display: suspiciously modern sneakers labeled "circa 1850" |
| "Est. 1849" Plaque | (224, 224) | 32x16 | Below the main sign motif |
| Wall Sconce | (256, 224) | 16x32 | Warm romantic glow source |
| Drink-Pairing Annotation Detail | (272, 224) | 48x32 | Close-up readable wallpaper note for interaction popup |

### Exterior:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tavern Façade Section | (0, 304) | 128x96 | Traditional Austrian tavern front, silhouette windows |
| Exterior Sign: Stein Mid-Waltz | (128, 304) | 64x64 | Painted beer stein with legs, "The Dancing Stein — Est. 1849" |
| Window Glow (Night) | (192, 304) | 32x64 | Warm interior light with whirling figure shadow |
| MusikGasse Street Lamp | (224, 304) | 24x64 | District-standard lamp, ties into street tileset |

### Technical Notes:
- Floorboard "1-2-3" tiles must lay in strict sequence when tiled — the floor itself teaches the waltz
- Mirror tiles use a screen-blend highlight band; the "flattering" variant subtly stretches reflections vertically
- Sticky practice floor reads matte against the gloss of the main floor — the contrast IS the joke
- Floor Shine Overlay is additive-blended and driven by the chandelier's light position

---

## 🎩 Sprite Sheet 2: Herr Drehmeister (Barkeep)
**File:** `herr_drehmeister.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #8B4513 (Vest), #FFFAF0 (Shirt/Foam), #DAA520 (Bowtie, watch chain), #4169E1 (Pocket square)

### Perpetual Waltz-Sway Idle & Reactions (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sway Frame 1 (ONE) | (0, 0) | 48x96 | Weight left, down-beat emphasis — he never stops moving |
| Sway Frame 2 (two) | (48, 0) | 48x96 | Rise, weight center |
| Sway Frame 3 (three) | (96, 0) | 48x96 | Weight right, heel lift |
| Sway Frame 4 (and) | (144, 0) | 48x96 | Return transition — loops to Frame 1 |
| Greeting Gesture | (192, 0) | 48x96 | Arms wide: "Welcome! One-two-three, one-two-three, what can I get you?" |
| "First You DANCE!" Point | (240, 0) | 48x96 | Finger at dance floor, rules being explained |
| Scandalized ("WALKING?!") | (288, 0) | 48x96 | Hands to face, witnessing a patron walk to the bar |
| "...Close Enough" Shrug | (336, 0) | 48x96 | Accepting a bad shuffle, half-smile |
| Approving Nod | (384, 0) | 48x96 | Beat-synced nod for competent dancers |

### Waltz-Pour Sequence (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pour Frame 1 (Reach) | (0, 96) | 48x96 | Reaching tap mid-sway, stein in hand |
| Pour Frame 2 (Pour Left) | (48, 96) | 48x96 | Pouring while swaying left — not a drop wasted |
| Pour Frame 3 (Pour Right) | (96, 96) | 48x96 | Pouring while swaying right, foam building |
| Pour Frame 4 (Present) | (144, 96) | 48x96 | Stein presented on the beat, foam swirling |
| Pour Flourish (Spin) | (192, 96) | 48x96 | Full-turn pour for the Sinfonian Whirl order |
| Counting Beat ONE | (240, 96) | 48x96 | Arm raised, emphatic down-beat count |
| Counting Beat two | (288, 96) | 48x96 | Arm mid, softer |
| Counting Beat three | (336, 96) | 48x96 | Arm out, completing the bar |

### Rhythm-Stamp Ceremony (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stamp Raise | (0, 192) | 48x96 | Stamp held high, waltz music starting |
| Stamp Beat ONE | (48, 192) | 48x96 | First downward pulse — "ONE-" |
| Stamp Beat two | (96, 192) | 48x96 | Lift and hover — "-two-" |
| Stamp Beat THREE (Impact) | (144, 192) | 48x96 | "-three, STAMPED!" — full-arm landing |
| Triumphant Arms | (192, 192) | 48x96 | "Welcome to the dancers, friend!" |
| Judging Watch | (240, 192) | 48x96 | Arms crossed, swaying, evaluating a Stein Waltz run |
| Applauding | (288, 192) | 48x96 | On-beat clapping for a clean finish |
| Wince at Spill | (336, 192) | 48x96 | Sympathetic flinch — "Acceptable losses! Keep going!" |

### Detail Props (various):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stamp In Hand | (0, 288) | 24x24 | Close-up: stein-with-legs stamp face visible |
| Stamped Passport | (24, 288) | 32x24 | Brewery Tour book open to fresh gold stamp |
| "1-2-3" Speech Glyph | (56, 288) | 32x24 | Floats over his head during counting dialogue |
| Pocket Metronome | (88, 288) | 16x24 | He carries one. Of course he does |

### Technical Notes:
- The sway idle NEVER stops — even the scandalized and stamp frames keep hips offset in waltz posture
- Vest and bowtie must stay crisp in every frame; his body moves, his grooming does not
- Beat ONE frames carry the strongest silhouette change — animation reads at 44px on-screen height

---

## 👥 Sprite Sheet 3: NPCs — Instructor, Regulars, Server, Stumbler
**File:** `dancing_stein_npcs.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #4169E1 (Frau Schritt), #DAA520 (Elegant wear), #8B4513 (Wood tones), #FFFAF0 (Shirts, foam)

### Frau Schritt — Dance Instructor (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Posture Demonstration | (0, 0) | 48x96 | Perfect frame, chin up — former ballroom champion (claims) |
| Teaching Count ONE | (48, 0) | 48x96 | Sharp down-beat gesture |
| Teaching Count two | (96, 0) | 48x96 | "The two is important! Feel the two!" — emphatic mid-gesture |
| Teaching Count three | (144, 0) | 48x96 | Closing sweep of the bar |
| Encouraging Clap | (192, 0) | 48x96 | "You're doing wonderful! The beer thinks so too!" |
| Gentle Correction | (240, 0) | 48x96 | Repositioning a student's arm, infinite patience |
| Emphatic "No, No!" | (288, 0) | 48x96 | Hands up, restarting the count — kindly |
| Proud Smile | (336, 0) | 48x96 | Student completed three steps without casualty |

### Elegant Dancing Regulars (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Elegant Dancer M — Beat 1 | (0, 96) | 48x96 | Genuinely graceful box-step, down-beat |
| Elegant Dancer M — Beat 2 | (48, 96) | 48x96 | Rise phase |
| Elegant Dancer M — Beat 3 | (96, 96) | 48x96 | Turn phase, loops to Beat 1 |
| Elegant Dancer F — Beat 1 | (144, 96) | 48x96 | Mirror pattern, skirt swirl on down-beat |
| Elegant Dancer F — Beat 2 | (192, 96) | 48x96 | Rise phase |
| Elegant Dancer F — Beat 3 | (240, 96) | 48x96 | Turn phase, loops to Beat 1 |

### Enthusiastic Regulars (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Enthusiastic Dancer — Beat 1 | (0, 192) | 48x96 | Maximum effort, minimum technique |
| Enthusiastic Dancer — Beat 2 | (48, 192) | 48x96 | Deliberately lands a hair late on the "two" — the shuffle everyone pretends is a waltz |
| Enthusiastic Dancer — Beat 3 | (96, 192) | 48x96 | Recovers with confidence |
| Fifteen-Year Regular (Twirl) | (144, 192) | 48x96 | "Never sit anymore. Forgot how." — perpetual mid-twirl |
| Regular Giving Advice | (192, 192) | 48x96 | "Don't watch me, feel the music!" gesture |
| Two-Stein Braggart | (240, 192) | 48x96 | Miming the legendary double-stein run ("...Once. Never again.") |

### Waltzing Server (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tray Carry (Sway) | (0, 288) | 48x96 | Tray aloft, hips in 3/4 time |
| Spin Delivery Frame 1 | (48, 288) | 48x96 | Wind-up quarter turn |
| Spin Delivery Frame 2 | (96, 288) | 48x96 | Half turn, tray level — physics-defying |
| Spin Delivery Frame 3 | (144, 288) | 48x96 | Completing rotation |
| Delivery Flourish | (192, 288) | 48x96 | Stein landed on table exactly on beat ONE |
| Full Whirl (Sinfonian Whirl) | (240, 288) | 48x96 | Extended spin pose for the €8 full-spin delivery |

### Stumbling Patron — Comedy Fail (48x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Confident Start | (0, 384) | 48x96 | Stein up, misplaced certainty |
| Wobble | (48, 384) | 48x96 | Beer tilting, eyes widening |
| Flail | (96, 384) | 48x96 | Full pinwheel arms — record scratch fires here |
| Splash-Fall | (144, 384) | 48x96 | Down, beer airborne, dignity gone |
| Sheepish Sit-Up | (192, 384) | 48x96 | Soaked, waving off help |
| Apologetic Selfie Pose | (240, 384) | 48x96 | "It's Harder Than It Looks" — Two Left Feet photo variant |

### Technical Notes:
- All dancer loops are frame-synced to the global 3/4 conductor clock (see Animation Specifications) so the whole floor moves as one
- Elegant and enthusiastic loops share timing but NOT easing — elegant frames flow, enthusiastic frames snap
- Server tray must remain perfectly level through all spin frames; that's the gag

---

## 🚪 Sprite Sheet 4: Landmarks & Set Pieces
**File:** `dancing_stein_landmarks.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #8B4513 (Wood), #B87333 (Copper), #DAA520 (Gold), #FFFAF0 (Foam White highlights)

### The Rotating Waltz-Tempo Door (64x96 each, 8 frames):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Door Rotation Frame 1 | (0, 0) | 64x96 | Leaves at 0° — entry gap open, beat ONE |
| Door Rotation Frame 2 | (64, 0) | 64x96 | 45° — glass catching chandelier light |
| Door Rotation Frame 3 | (128, 0) | 64x96 | 90° — beat two position |
| Door Rotation Frame 4 | (192, 0) | 64x96 | 135° |
| Door Rotation Frame 5 | (256, 0) | 64x96 | 180° — beat three position |
| Door Rotation Frame 6 | (320, 0) | 64x96 | 225° |
| Door Rotation Frame 7 | (384, 0) | 64x96 | 270° — next measure's down-beat |
| Door Rotation Frame 8 | (448, 0) | 64x96 | 315° — loops to Frame 1; it sets the tempo. Seriously |

### Bar & Ballroom Set Pieces:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Copper Bar Assembly | (0, 96) | 160x96 | Full destination bar: arc of taps, brass rail, gleam pass |
| Back-Bar Mirror & Shelf | (160, 96) | 128x96 | Mirrored back wall doubling the dancer chaos |
| Chandelier w/ Spotlight | (288, 96) | 96x96 | Ballroom chandelier with special-dance spotlight cone |
| Selfie Spot Medallion | (384, 96) | 64x64 | Inlaid floor medallion at dance floor center, under chandelier |

### Cellar — Stamp Ceremony:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stamp Ceremony Station | (0, 192) | 96x96 | Candle-lit cellar table, stamp pad, gold ink pot |
| Spinning Brewery Keg Stack | (96, 192) | 64x96 | Partner brewery kegs, spiral logo, "FRESH — DELIVERED DANCING" |
| Stamp Podium | (160, 192) | 48x64 | Where the passport lies for the three-beat landing |
| "Famous Dances" Photo Wall | (208, 192) | 128x96 | Framed regulars mid-waltz; one frame is just a blur with a plaque reading "THE INCIDENT, 1997" |
| Wallpaper Pairing Plaque | (336, 192) | 64x48 | Framed legend explaining the sheet-music drink pairings |

### Mirrors & Practice Corner:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wall Mirror w/ Reflection | (0, 288) | 64x96 | Shows a generic dancer reflection layer slot |
| Flattering Mirror (Ego Check) | (64, 288) | 64x96 | Same slot, reflection rendered 10% more graceful |
| "No Judgment (Much)" Sign | (128, 288) | 48x32 | Practice corner house rules |
| Door Tempo Gear Detail | (176, 288) | 32x32 | Visible clockwork governor keeping the door at 3/4 — interaction close-up |

### Technical Notes:
- Door frames are pre-rotated art (no runtime rotation) so glass highlights stay hand-placed
- Mirror pieces reserve a masked reflection region; game composites live dancer sprites into it at 40% opacity
- Photo wall is screenshot bait — every framed photo must read as an individual joke at 2x zoom

---

## 🍺 Sprite Sheet 5: Stein Waltz Challenge, Beers & Stamp
**File:** `dancing_stein_challenge_items.png`
**Dimensions:** 256x256 pixels
**Color Palette:** #FFFAF0 (Foam), #DAA520 (Beer gold), #4169E1 (Loss line, accents), #B87333 (Stein bands)

### Stein Carry States (held-item overlays):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stein 100% Full | (0, 0) | 24x32 | Master difficulty — foam dome above the rim |
| Stein 75% Full | (24, 0) | 24x32 | Standard difficulty fill |
| Stein 50% Full | (48, 0) | 24x32 | Beginner difficulty fill |
| Stein At Loss Line | (72, 0) | 24x32 | Beer level exactly at the blue acceptable-loss line |
| Stein Below Line (Fail) | (96, 0) | 24x32 | Under the line — run failed (but funny) |
| Stein Empty (Triumphant) | (120, 0) | 24x32 | Post-challenge, drained what remained |
| Loss Line Close-Up | (144, 0) | 32x32 | Readable detail of the etched blue line + "MIN." mark |
| Stein Tilt Left | (176, 0) | 24x32 | Carry-state lean, beer sloshing left |
| Stein Tilt Right | (200, 0) | 24x32 | Carry-state lean, beer sloshing right |

### Spill States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Splash Small | (0, 32) | 16x16 | Minor slosh over the rim |
| Splash Medium | (16, 32) | 24x24 | Major stumble splash |
| Splash Large | (40, 32) | 32x32 | Full crest of lost beer — record-scratch territory |
| Total Spill Puddle | (72, 32) | 48x24 | Floor puddle, failure state |
| Foam Trail | (120, 32) | 32x16 | Drip line tracing a wobbly circuit |

### Beer Lineup (32x64 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Waltz Weizen — Swirl 1 | (0, 64) | 32x64 | Signature: cloudy gold, foam mid-swirl (clockwise, always) |
| Waltz Weizen — Swirl 2 | (32, 64) | 32x64 | Foam rotated 120° clockwise |
| Waltz Weizen — Swirl 3 | (64, 64) | 32x64 | Foam rotated 240° clockwise — loops. We don't know why it does this |
| Two-Step Lager | (96, 64) | 32x64 | €4, basic rhythm, honest glass |
| Foxtrot Ale | (128, 64) | 32x64 | €5, amber, subtly wrong tempo (rebellion) |
| The Wallflower | (160, 64) | 32x64 | €3, plain glass, served with visible shame aura |
| Tango IPA | (192, 64) | 32x64 | €6, dramatic red-tinged, rose garnish |
| Sinfonian Whirl | (224, 64) | 32x64 | €8, tall spiral glass — earns the full spin delivery |

### Bottle Opener & Stamp:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bottle Opener Frame 1 | (0, 128) | 24x48 | Stein silhouette with dancing legs; opener as handle. "One-Two-Three" inscription |
| Bottle Opener Frame 2 | (24, 128) | 24x48 | Mid-spin — weighted to spin when flicked, like a dancer |
| Bottle Opener Frame 3 | (48, 128) | 24x48 | Spin blur frame |
| Stamp Graphic (Face) | (72, 128) | 64x64 | Stein with dancing legs, foam trailing like a skirt |
| Stamp Inked On Page | (136, 128) | 64x64 | Ballroom gold ink, blue accents, "Danced & Drank" |
| Passport Page (Open) | (200, 128) | 48x64 | Brewery Tour page awaiting stamp #4 |

### Stamp Landing Animation (three beats):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stamp Descend (ONE) | (0, 192) | 48x48 | Stamp spinning down toward page |
| Stamp Hover (two) | (48, 192) | 48x48 | Rotation aligning, foam-skirt motif visible |
| Stamp Impact (THREE) | (96, 192) | 48x48 | Landing flourish with gold ink burst |
| Gold Ink Shimmer | (144, 192) | 32x32 | Post-impact glint overlay |
| "Danced & Drank" Ribbon | (176, 192) | 64x24 | Banner unfurl beneath fresh stamp |

### Technical Notes:
- The acceptable-loss line is Waltz Blue against Foam White — the single highest-priority readability element in this location
- Waltz Weizen foam frames must rotate CLOCKWISE only; reversed playback is a validation failure
- Stein carry states composite over any party-member sprite; anchor point bottom-center

---

## ✨ Sprite Sheet 6: Effects & Particles
**File:** `dancing_stein_effects.png`
**Dimensions:** 256x128 pixels
**Color Palette:** #FFFAF0 (Foam/sparkle), #DAA520 (Glints), #4169E1 (Beat pulses)

### Ambience & Light:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floor Shine Sweep 1 | (0, 0) | 32x32 | Gloss band traveling with chandelier light |
| Floor Shine Sweep 2 | (32, 0) | 32x32 | Band advanced |
| Floor Shine Sweep 3 | (64, 0) | 32x32 | Band fading — loops |
| Drink Swirl Particle | (96, 0) | 16x16 | Micro foam curl for served steins |
| Clockwise Swirl Arrow | (112, 0) | 16x16 | Debug/QA overlay confirming swirl direction |
| Mirror Glint | (128, 0) | 16x16 | Passing sparkle on mirror panels |
| Chandelier Sparkle | (144, 0) | 16x16 | Crystal glint, beat-synced |
| Quarter Note Particle | (160, 0) | 16x16 | Drifts from the (unseen) band |
| "1-2-3" Note Trio | (176, 0) | 32x16 | Three linked notes rising over dancers |
| Spotlight Beam | (208, 0) | 32x64 | Special-dance cone from chandelier |

### Event Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Splash Burst | (0, 64) | 32x32 | Beer impact effect, pairs with splash audio |
| Record-Scratch Jag | (32, 64) | 32x32 | Jagged white flash for major stumbles |
| Sad Accordion Wheeze | (64, 64) | 32x32 | Drooping bellows cloud for full failure |
| Success Flourish Starburst | (96, 64) | 48x48 | Gold burst on clean challenge completion |
| Beat Pulse Ring 1 | (144, 64) | 32x32 | Expanding ring on beat ONE (strong) |
| Beat Pulse Ring 2 | (176, 64) | 32x32 | Softer ring, beat two |
| Beat Pulse Ring 3 | (208, 64) | 32x32 | Softer ring, beat three |

### Technical Notes:
- Beat pulse rings originate from the rotating door — the door IS the metronome
- All particles CPUParticles2D; note particles capped at 6 concurrent on High LOD
- Record-scratch and accordion effects are single-play, never looped

---

## 🖥️ Sprite Sheet 7: UI Elements
**File:** `dancing_stein_ui.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #4169E1 (Rhythm UI), #DAA520 (Gold accents), #FFFAF0 (Fill/foam), #8B4513 (Frames)

### Rhythm QTE Indicator:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| QTE Track | (0, 0) | 256x48 | Horizontal timeline, measures ruled in 3/4 |
| Beat Marker ONE | (256, 0) | 32x32 | Large gold marker — down-beat, biggest tap target |
| Beat Marker two | (288, 0) | 32x32 | Medium blue marker |
| Beat Marker three | (320, 0) | 32x32 | Medium blue marker |
| Hit Zone Highlight | (352, 0) | 48x48 | Timing window frame (width scales per difficulty) |
| Perfect Hit Flash | (400, 0) | 48x48 | Gold flash + note burst |
| Miss X | (448, 0) | 32x32 | Slosh-warning miss marker |

### Spill Meter:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Spill Meter Frame | (0, 48) | 192x32 | Stein-shaped horizontal gauge |
| Spill Fill Gradient | (192, 48) | 176x24 | Beer level fill, gold → pale as beer is lost |
| Acceptable-Loss Marker | (368, 48) | 16x32 | Blue line on gauge matching the stein's etched line |

### Difficulty Select:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Difficulty Panel | (0, 80) | 288x96 | Three-column selection card, chalkboard style |
| Beginner Stein (50%) | (288, 80) | 48x64 | Half-full stein icon, generous window note |
| Standard Stein (75%) | (336, 80) | 48x64 | Three-quarter stein icon |
| Master Stein (100%) | (384, 80) | 48x64 | Brimming stein icon, foam dome, tight window |
| Reward Badge 1x | (432, 80) | 32x32 | Beginner multiplier |
| Reward Badge 1.5x | (464, 80) | 32x32 | Standard multiplier |
| Reward Badge 2x | (432, 112) | 32x32 | Master multiplier, gold trim |

### Status, Buffs & Misc:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Graceful Buff Icon | (0, 176) | 32x32 | Dancing figure in gold ring — +10% Dance, 1 hour |
| Two Left Feet Icon | (32, 176) | 32x32 | Two left shoes, blue ring — 50% off next beer, must retry |
| Light on Your Feet Icon | (64, 176) | 32x32 | Winged shoe — Waltz Weizen effect |
| 3/4 Tempo Marker | (96, 176) | 32x32 | Time signature glyph for rhythm HUD |
| Dance Skill Pip | (128, 176) | 24x24 | +1 Dance indicator for service checks |
| Stamp Progress Badge | (152, 176) | 48x32 | "Sinfonia 4/6" Brewery Tour tracker chip |
| Beer Menu Card | (200, 176) | 96x64 | Six-line menu with prices and "Served With" column |
| Achievement Toast Frame | (296, 176) | 160x48 | Banner for First Steps / Not a Drop / Dance Marathon / hidden Two Left Feet |

### Technical Notes:
- All tappable UI elements here render at ≥44px on target devices; beat markers scale up, never down
- QTE track is the deaf-accessible primary rhythm channel — it must be fully playable with audio off (see Accessibility)
- Spill meter and stein overlay always agree; both read from the same `stein_fill` value

---

## ♿ Sprite Sheet 8: Accessibility Alternates
**File:** `dancing_stein_accessibility.png`
**Dimensions:** 256x256 pixels
**Color Palette:** #FFFFFF/#000000 (High contrast pair), #DAA520, #4169E1

*(Coordinate detail for this sheet appears in the Accessibility Sprite Requirements section below — this sheet is the delivery container for all high-contrast, reduced-motion, and visual-audio-cue sprites.)*

### Technical Notes:
- High-contrast outlines are 2px white-on-black double strokes, visible on any background
- Reduced-motion variants are single static frames swapped 1:1 for their animated counterparts
- Beat indicator glyphs are the deaf-play channel for the entire rhythm game — they ship in this sheet so they load even when effects LOD is Low

---

## 🎬 Animation Specifications

**Global conductor clock:** all location animations sync to a shared 3/4 metronome at 60 measures/minute — **one measure = 1.0 second, one beat = 0.333 seconds**. Beat ONE is the down-beat. The rotating door, every dancer, the metronomes, and the QTE track all subscribe to this clock.

### Rotating Waltz-Tempo Door:
- **Duration:** 3.0 seconds per full rotation (one rotation = three measures)
- **Frames:** 8
- **Pattern:** Frame 1 → 8 → loop, 0.375 s per frame
- **Trigger:** Constant while location is loaded
- **Purpose:** The door sets the tempo for the entire pub — players entering are literally metered in
- **Audio Sync:** Soft whoosh lands on beat ONE of each measure; door gap aligns with entry on beat ONE of measure 1
- **Mobile Optimization:** Low LOD holds static open frame (accessibility static variant reused)

### Herr Drehmeister Waltz-Sway Idle:
- **Duration:** 1.0 second loop (one measure)
- **Frames:** 4
- **Pattern:** ONE → two → three → and → loop
- **Trigger:** Constant — he is never still, even mid-dialogue
- **Purpose:** Character thesis: EVERYTHING can be done in waltz tempo
- **Audio Sync:** Frame 1 lands on ambient music down-beat
- **Mobile Optimization:** None needed (single 48x96 sprite)

### Herr Drehmeister Waltz-Pour:
- **Duration:** 2.0 seconds (two measures), single play
- **Frames:** 4 (+1 spin flourish frame for Sinfonian Whirl orders)
- **Pattern:** Reach → pour left → pour right → present; flourish frame inserts before present on Whirl orders
- **Trigger:** Any drink order completed
- **Purpose:** "The beer pours better if you're moving. Scientific fact. Probably."
- **Audio Sync:** Tap hiss starts beat ONE measure 1; stein lands on counter exactly on beat ONE measure 3
- **Mobile Optimization:** None needed

### Rhythm-Stamp Ceremony:
- **Duration:** 3.0 seconds (three measures), single play
- **Frames:** 5 (raise → beat ONE → beat two → beat THREE impact → triumphant)
- **Pattern:** Raise holds measure 1; stamp lands over the three beats of measure 3 — pulse on ONE, hover on two, impact on three
- **Trigger:** Stein Waltz challenge passed, cellar ceremony cutscene
- **Purpose:** "ONE-two-three, ONE-two-three, STAMPED!" — the location's signature payoff
- **Audio Sync:** Waltz music swells through all three measures; stamp impact thuds on beat three of measure 3; ribbon audio flourish immediately after
- **Mobile Optimization:** None needed (cutscene context)

### Frau Schritt Teaching Count:
- **Duration:** 1.0 second loop
- **Frames:** 3 (ONE, two, three)
- **Pattern:** One gesture per beat, extra emphasis frame on "two" ("Feel the two!")
- **Trigger:** Player in practice corner or tutorial active
- **Purpose:** Tutorial telegraphing — her arms ARE the beat chart
- **Audio Sync:** Spoken "one-TWO-three" aligned per beat
- **Mobile Optimization:** None needed

### Dancing Regulars (Elegant + Enthusiastic):
- **Duration:** 1.0 second loop per dancer
- **Frames:** 3 each
- **Pattern:** Beat-per-frame; elegant sets ease smoothly, enthusiastic sets snap and land ~0.04 s late on beat two (intentional comedy desync)
- **Trigger:** Constant while location loaded
- **Purpose:** Living ballroom; the late "two" sells the satire that nobody here is actually good
- **Audio Sync:** Down-beat foot-plant on beat ONE
- **Mobile Optimization:** Low LOD freezes background dancers to static poses; only 4 nearest dancers animate (see Performance Notes)

### Waltzing Server Spin Delivery:
- **Duration:** 1.0 second (one measure), single play
- **Frames:** 4 (wind-up → half turn → complete → flourish)
- **Pattern:** Spin occupies beats ONE-two-three; stein touches table on the next down-beat
- **Trigger:** Waltz Weizen or Sinfonian Whirl delivered to table (Whirl uses extended Full Whirl pose, 2.0 s)
- **Purpose:** Signature-beer showmanship — the small spin from the profile, escalated for the €8 order
- **Audio Sync:** Glass-clink lands on the down-beat following the spin
- **Mobile Optimization:** None needed

### Stumbling Patron Fail:
- **Duration:** 2.0 seconds, single play
- **Frames:** 5 (confident → wobble → flail → splash-fall → sheepish)
- **Pattern:** Confident holds one measure; wobble-to-fall collapses across measure 2
- **Trigger:** Random ambient event (~90 s cooldown); mirrors player failure states
- **Purpose:** Social proof that failing is normal, expected, and hilarious here
- **Audio Sync:** Record scratch fires on flail frame; splash SFX on splash-fall; scattered on-beat applause after sheepish frame
- **Mobile Optimization:** Event disabled on Low LOD

### Waltz Weizen Foam Swirl:
- **Duration:** 3.0 second loop
- **Frames:** 3 (swirl 1 → 2 → 3)
- **Pattern:** Continuous clockwise rotation, 120° per second — NEVER reversed
- **Trigger:** Any visible Waltz Weizen (bar, table, carry state)
- **Purpose:** "The foam always swirls clockwise. We don't know why." — the beer is the mascot
- **Audio Sync:** None (silent, eerie, wonderful)
- **Mobile Optimization:** Low LOD holds swirl frame 1 static

### Spill Splash:
- **Duration:** 0.3 seconds, single play
- **Frames:** 3 (small → medium → large, entered at severity level)
- **Pattern:** Scale-in burst, fades to floor decal on total spill
- **Trigger:** QTE miss during Stein Waltz; stumble events
- **Purpose:** Immediate, legible cost of missing the rhythm
- **Audio Sync:** Splash SFX on frame 1; on total spill, sad accordion begins 0.3 s after
- **Mobile Optimization:** Particle count halved on Medium LOD

### Beat Pulse Rings (UI/Ambient):
- **Duration:** 0.333 seconds per pulse (one per beat)
- **Frames:** 3 ring stages
- **Pattern:** Strong gold ring on ONE, soft blue rings on two and three, emitted from the rotating door
- **Trigger:** Constant; doubles as the QTE metronome during challenges
- **Purpose:** Makes the tempo visible everywhere — critical deaf-accessibility channel
- **Audio Sync:** Ring spawn is frame-locked to each music beat
- **Mobile Optimization:** Never disabled — this is an accessibility-critical animation; Low LOD renders rings without alpha gradient

### Table Metronomes:
- **Duration:** 0.667 second tick cycle (pendulum crosses on alternate beats)
- **Frames:** 2 (Tick A / Tick B)
- **Pattern:** A ↔ B alternation locked to conductor clock
- **Trigger:** Constant on perimeter tables
- **Purpose:** Décor gag that doubles as a peripheral beat reference
- **Audio Sync:** Tick SFX only within 2 tiles of player (audio clutter control)
- **Mobile Optimization:** Static Tick A frame on Low LOD

### Stamp Landing (Passport Page):
- **Duration:** 3.0 seconds
- **Frames:** 3 (+ shimmer + ribbon)
- **Pattern:** Stamp spins onto page across three beats — descend on ONE, hover on two, impact on THREE; shimmer and ribbon follow
- **Trigger:** Stamp ceremony completion
- **Purpose:** Brewery Tour stamp #4 lands like a dance finale
- **Audio Sync:** Waltz music during entire animation; stamp landing over three beats (thud on beat three); success flourish on ribbon unfurl
- **Mobile Optimization:** None needed (cutscene context)

---

## ♿ Accessibility Sprite Requirements

All sprites below ship on **Sheet 8: `dancing_stein_accessibility.png` (256x256)**.

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rotating Door Outline | (0, 0) | 64x96 | White double-stroke frame marking the entry/exit and its swing radius |
| Herr Drehmeister Silhouette | (64, 0) | 48x96 | High-contrast barkeep outline against dark bar backdrop |
| Frau Schritt Silhouette | (112, 0) | 48x96 | Instructor outline for practice corner findability |
| Cellar Stairs Outline | (160, 0) | 64x80 | Marks the spiral descent to the stamp ceremony |
| Bar Edge Contrast Strip | (224, 0) | 32x48 | Tiling high-visibility band along the copper bar's service edge |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Door (Open) | (0, 96) | 64x96 | Replaces the rotating door entirely — reduced-motion mode treats it as a normal doorway |
| Static Dancer Pose A | (64, 96) | 48x96 | Elegant couple frozen mid-frame; swaps for all animated background dancers |
| Static Dancer Pose B | (112, 96) | 48x96 | Enthusiastic variant, frozen |
| Static Foam Stein | (160, 96) | 32x64 | Waltz Weizen with painted (non-rotating) clockwise swirl |
| Static Metronome | (192, 96) | 16x24 | Pendulum at rest |
| Static Chandelier | (208, 96) | 48x48 | No sparkle cycling; constant warm glow |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Beat Indicator ONE | (0, 192) | 32x32 | Large gold flash glyph — fires on every musical down-beat. CRITICAL: with these three glyphs plus the QTE track, the rhythm game is fully playable with zero audio |
| Beat Indicator two | (32, 192) | 32x32 | Blue mid-beat glyph |
| Beat Indicator three | (64, 192) | 32x32 | Blue closing-beat glyph |
| Splash Cue Glyph | (96, 192) | 32x32 | Droplet burst icon fires with every spill sound |
| Success Flourish Glyph | (128, 192) | 32x32 | Gold fanfare icon for the success sting |
| Record-Scratch Glyph | (160, 192) | 32x32 | Jagged needle icon for major-stumble scratch |
| Sad Accordion Glyph | (192, 192) | 32x32 | Drooping bellows icon for the failure wheeze |
| Stamp-Beat Glyph | (224, 192) | 32x32 | Triple-pulse icon mirroring the three-beat stamp landing during the ceremony |

### Colorblind Considerations:
- Beat markers differ by SIZE and SHAPE (large diamond ONE vs. small circles two/three), never by gold/blue alone
- The acceptable-loss line pairs its blue color with a dashed etch pattern and "MIN." text label
- Difficulty steins are distinguished by fill silhouette (half / three-quarter / foam-domed), not tint
- Graceful vs. Two Left Feet status icons use opposite silhouettes (upright dancer vs. crossed shoes), readable in grayscale
- Touch zones minimum 44px for QTE beat markers, difficulty select, door interaction, bar ordering, and stamp podium

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback); challenge/items sheet needs ASTC 4x4 — the acceptable-loss line and foam swirl must stay crisp
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for `dancing_stein_challenge_items.png` and `dancing_stein_ui.png` (rhythm-game readability is gameplay-critical)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| dancing_stein_environment | tileset, landmarks | 2048x1024 |
| dancing_stein_characters | Herr Drehmeister, NPCs sheet | 1024x1024 |
| dancing_stein_effects_ui | challenge items, effects, UI, accessibility | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | 8 animated dancers, rotating door, foam swirls, floor shine, note particles, beat pulse rings with gradients, metronome ticks |
| Medium | 6 animated dancers, door animated, foam swirl on nearest steins only, no note particles, halved splash particles |
| Low | 4 animated dancers max — all others static poses; door holds static open frame; static foam; no ambient particles; beat pulse rings retained (flat alpha) as accessibility-critical |

### Performance Targets:
> **Note:** the source profile (`the_dancing_stein.md`) states no performance budget. The numbers below are proposed defaults against the project-standard 60 FPS mobile target and must be ratified by tech art before production.

- **Target FPS:** 60 (default target — not stated in source profile)
- **Max Draw Calls:** 40 per frame (proposed default)
- **Memory Footprint:** 38 MB maximum (proposed default)
- **Particle Limit:** 25 concurrent (notes 6, splashes 8, shine 4, beat rings 3, sparkles 4)

### Performance Notes:
- **The crowd of constant dancers is the primary performance risk.** Animated dancer count is hard-capped per LOD (8/6/4); all dancers beyond the cap render as static background poses from the accessibility sheet — motion budget goes to the dancers nearest the player
- All dancers share one conductor-clock AnimationPlayer; per-dancer offsets are frame indices, not separate timelines (one animation update, N sprites)
- Rotating door is 8 pre-rendered frames, zero runtime rotation math
- Cellar sprites (stamp station, kegs, stairs interior) load on-demand when the player descends
- Foam swirl updates at 3 FPS effective (frame changes every 1.0 s per 120° step) — cheap despite being ever-present

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- AnimatedSprite2D for NPCs; one shared conductor-clock AnimationPlayer broadcasts beat ticks (signal `beat(n)`) that every dancer, the door, metronomes, and the QTE HUD subscribe to
- CPUParticles2D (not GPU) for splashes, notes, sparkles
- CanvasLayer for QTE track, spill meter, and beat indicator glyphs
- Mirror reflections: masked Sprite2D duplicates at 40% opacity inside mirror regions (no viewport textures on mobile)
- Location state machine: `pre_challenge → challenge_active(difficulty) → passed / failed(two_left_feet) → stamped` drives stein fill value, Drehmeister dialogue set, and cellar access

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Beat pulse rings / beat glyphs | Waltz music down-beat + rhythm cues | Ring/glyph spawn frame-locked to each beat; gold ONE on every down-beat |
| Rotating door | Soft whoosh | Beat ONE of each measure as gap aligns |
| QTE hit/miss markers | Rhythm cue tick / slosh warning | On marker crossing hit zone |
| Spill splash sprites | Splash SFX | Frame 1 of splash animation |
| Success flourish starburst | Success flourish sting | Burst spawn frame on challenge pass |
| Record-scratch jag | Record scratch | Stumbling flail frame / major QTE failure |
| Sad accordion wheeze cloud | Sad accordion sting | 0.3 s after total-spill puddle lands |
| Stamp ceremony frames | Waltz music during stamp; landing thud | Music runs full 3.0 s; stamp lands over three beats, thud on beat three of measure 3 |
| Waltz-pour present frame | Stein-on-copper clink | Beat ONE, measure 3 of pour |
| Table metronomes | Tick SFX (proximity-gated) | Alternate beats, conductor-locked |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Stein Waltz (stamp challenge) | Stein carry/spill states, QTE track, spill meter, difficulty select, stamp ceremony frames, stamp animation | Challenge start at bar; ceremony in cellar on pass; sets Brewery Tour stamp #4 |
| "The Perfect Waltz" | Master stein (100%), tight hit zone, Not a Drop variant of success flourish, selfie medallion | Master difficulty, zero spill — unlocks "Didn't Spill a Drop" selfie |
| "Dance Marathon" | Dance floor circuit markers, dancer sprites, achievement toast frame | Counter increments per completed floor crossing; toast at 10 in one visit |
| "The Wallflower's Redemption" | The Wallflower beer sprite (shame aura), Frau Schritt teaching frames, Graceful buff icon | Order The Wallflower, then complete a clean waltz circuit to clear the shame |
| Achievement track (First Steps / The Stein Waltz / Not a Drop / Dance Marathon / hidden "Two Left Feet") | Achievement toast frame, status icons, apologetic selfie pose | Hidden Two Left Feet fires on spectacular failure + triggers the failure selfie variant |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| MusikGasse (street) | Façade section, exterior sign, street lamp match district tileset; waltz music audible from street | Rotating-door entry — player is metered in on beat ONE |
| The Moderato Pub | 3/4 tempo marker icon shared (tempo-debate overlap — waltz time is controversial there) | Standard door transition; tempo marker flashes during debate dialogue |
| Baroness' Ballroom | Elegant dancer sprites reused as Dance Duelists practicing here first | None (shared character atlas) |
| Brewery Tour (Sinfonia) | Stamp graphic, stamped passport, stamp progress badge "4/6", bottle opener | Passport UI overlay, persistent across all stamp locations |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A ballroom pretending to be a pub pretending to be a ballroom"
- **Color Mood:** Warm ballroom gold over polished wood, cut with waltz blue — romantic, glowing, faintly ridiculous
- **Lighting:** Chandelier warmth as base; spotlight cone for special dances; night windows spill gold onto MusikGasse
- **Texture:** High-gloss floor against matte sticky practice corner; copper gleam; cream sheet-music walls; everything polished by decades of shuffling feet

### Environmental Storytelling:
- The "1-2-3" floorboards teach the waltz before any NPC says a word
- "No Sitting Permitted" sign hanging over visible, occupied seats = the tradition is theater and everyone knows it
- The flattering mirror, the "circa 1850" sneakers, and the blurred "THE INCIDENT, 1997" photo all whisper the deeper joke: nobody here is actually good, and that's fine
- Spilled-beer decals near the bar mark the trail of failed Stein Waltz runs — the floor keeps score

### Character Integration Notes:
- Herr Drehmeister's sway idle never stops — his silhouette must read as "in motion" even in a static screenshot
- Dancer crowd renders behind the player layer with soft shadows; nearest dancers get motion priority (see LOD)
- Frau Schritt is the only figure allowed perfect posture — visual authority for the tutorial
- Stumbling patron shares its fail frames with the player's own failure state — the game never mocks the player harder than it mocks its NPCs

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The rotating waltz-tempo door mid-spin** — a door with a time signature is instantly clippable
2. **Master-difficulty Stein Waltz, foam dome intact** — the "Didn't Spill a Drop" selfie under the chandelier
3. **Total spill fail with sad accordion cloud** — the "It's Harder Than It Looks" apologetic selfie
4. **The stamp landing over three beats** — gold ink, foam-skirt stein, "Danced & Drank"
5. **The "No Sitting Permitted" sign above a row of occupied chairs** — the whole location in one frame

### TikTok Potential:
- "POV: you just want a beer but the door is in 3/4 time"
- "Rating my Stein Waltz attempts until I stop spilling" (spill meter series)
- The enthusiastic dancer who is always slightly late on the two
- Bottle opener spin flicks — "it's weighted like a dancer"

### Quote Potential:
- "ONE-two-three, ONE-two-three, STAMPED! Welcome to the dancers, friend!" — Herr Drehmeister
- "There is no OPTIMAL! There is only the DANCE!" — Herr Drehmeister
- "Then WALTZ for it! This is THE DANCING STEIN! Not 'The Walking Stein!'" — Herr Drehmeister
- "You SURVIVED! That counts!" — Herr Drehmeister
- "No, no! One-TWO-three! The two is important! Feel the two!" — Frau Schritt
- "The Stein Waltz? Easy! I've done it with TWO steins! ...Once. Never again." — a Regular

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | dancing_stein_tileset.png | 1024x512 |
| 2 | herr_drehmeister.png | 512x384 |
| 3 | dancing_stein_npcs.png | 512x512 |
| 4 | dancing_stein_landmarks.png | 512x512 |
| 5 | dancing_stein_challenge_items.png | 256x256 |
| 6 | dancing_stein_effects.png | 256x128 |
| 7 | dancing_stein_ui.png | 512x256 |
| 8 | dancing_stein_accessibility.png | 256x256 |

**Total Estimated Memory:** ~6 MB (uncompressed RGBA at 4 bytes/pixel: 1,540,096 px ≈ 5.9 MB, rounded)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `dancing_stein_tileset.png` (1024x512)
- [ ] `herr_drehmeister.png` (512x384)
- [ ] `dancing_stein_npcs.png` (512x512)
- [ ] `dancing_stein_landmarks.png` (512x512)
- [ ] `dancing_stein_challenge_items.png` (256x256)
- [ ] `dancing_stein_effects.png` (256x128)
- [ ] `dancing_stein_ui.png` (512x256)
- [ ] `dancing_stein_accessibility.png` (256x256)

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
- **Documentation:** Animation timing reference sheet (conductor-clock beat map) + door-rotation frame alignment guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Waltz Weizen foam swirls CLOCKWISE in every frame, on every sheet — no exceptions, no mirrored exports
- [ ] Acceptable-loss line on stein readable at game resolution (and in the 44px carry-state overlay)
- [ ] "1-2-3" floorboards tile in correct sequence with no seam breaks
- [ ] Herr Drehmeister reads as "in motion" in every single frame, including dialogue stills
- [ ] Rotating door frames align — glass highlights continuous across the 8-frame loop
- [ ] Elegant vs. enthusiastic dancers distinguishable at gameplay zoom (ease vs. snap silhouettes)
- [ ] Beat indicator glyphs legible against every interior background (deaf-play channel)
- [ ] "No Sitting Permitted" sign and seated patrons composable in one screenshot
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets — mandatory tradition, mediocre execution, collective denial
- [ ] Hidden areas/interactions have discoverable visual cues (cellar stairs, practice corner, door gear detail)
- [ ] Rhythm game fully playable with audio off (QTE track + beat glyphs verified)
- [ ] Mobile performance optimized (CPU particles, atlas limits respected, dancer caps honored)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (beat shapes, loss-line pattern, status silhouettes)
- [ ] Social media viral potential maximized in composition choices (door, selfie medallion, stamp landing)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia / MusikGasse only; Vienna evoked, never named |
| Cultural Specificity | ✅ | Viennese waltz obsession, ballroom culture, 3/4-time-as-religion |
| Satirical Targets Appropriate | ✅ | Mocks the mandatory-tradition performance and dance gatekeeping, not locals; staff are in on the joke and equally mediocre |
| Seedy Underbelly Present | ❌ | Honest miss: this is a gentle, warm location. The nearest thing to vice is dance snobbery, a shame-priced beer, and a suspiciously fake shoe exhibit — none of it qualifies as a seedy underbelly. Flagged deliberately rather than inventing one; the location's role in the Sinfonia mix is the friendly counterweight |
| Gameplay Value Established | ✅ | Rhythm QTE challenge, Brewery Tour stamp #4, buff/status economy, three quests, five achievements, selfie spot |
| Technical Feasibility | ✅ | Eight sheets, atlas plan, LOD tiers, dancer caps, conductor-clock architecture documented |
| Mobile Performance Budget | ✅ | 60 FPS / 40 draw calls / 38 MB / 25 particles — proposed defaults; source profile stated no budget (flagged in Mobile Optimization) |
| Accessibility Features | ✅ | Visual cues for every audio event; rhythm game deaf-playable; reduced-motion variants for door and dancers; colorblind shape coding |
| No Crypto Elements | ✅ | None present — pure dance satire |
| Social Media Integration | ✅ | Door, spill fails, stamp landing, and sign-vs-seats moments identified |

**The Dancing Stein: where the door counts you in, the floor teaches you the steps, the beer judges your balance, and eight PNG sheets turn "ONE-two-three, ONE-two-three, DRINK!" into a playable waltz nobody performs well and everybody loves.**
