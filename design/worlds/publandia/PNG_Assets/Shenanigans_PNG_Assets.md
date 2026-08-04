# Shenanigans - Complete PNG Asset Requirements

## 📋 Overview
Shenanigans is the side-alley Publandia pub where every game is rigged, every "winner" is on payroll, and the only honest thing in the building is the beer — this document specifies every PNG needed to render a con so obvious it loops back around to charming. The satirical engine: the marks know, the house knows the marks know, and everyone keeps playing anyway, because hope sells at 5 Sovs a spin.

**Location ID:** `publandia_pub_shenanigans_01`
**Theme:** Tourist gullibility and the psychology of gambling — the scam pub where losing gracefully IS the achievement
**Zone:** The Craic Tax (side street, slightly hidden, tout-guided "accidental" discovery)
**Hours:** 16:00-03:00 (prime scamming hours)
**Primary Function:** Scam mini-game venue / Brewery Tour stamp stop / "Wise Fool" loss-based progression / Shill Offer moral choice

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Faded Green | #6B8E23 | Chipped exterior paint, signage, clover iconography |
| Lucky Gold | #DAA520 | Wheel segments, prize display, stamp ink, Fool's Gold |
| Sketchy Brown | #654321 | Interior wood, bar, back tables, alley shadow |
| Neon Accent | #FF4500 | "EVERYONE Wins!" signage, game spotlights, near-miss flash |
| Guinness Cream | #F5F0E1 | Pint heads, welcome drink, chalkboard lettering |
| Alley Slate | #4A5A6A | Rain-slick cobbles, night alley approach |
| Wilted Sage | #9CAF88 | The one dead clover leaf, faded "luck" everywhere |
| Shill Flush | #E8875A | Celebration bursts, fake-winner warmth |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/shenanigans/
├── environment/
│   ├── shenanigans_exterior.png
│   └── shenanigans_interior.png
├── npcs/
│   ├── mickey_finnegan.png
│   ├── shenanigans_staff.png
│   └── mark_npcs.png
├── objects/
│   ├── rigged_games.png
│   └── brewery_items.png
├── ui/
│   └── shenanigans_ui_fx.png
└── accessibility/
    └── shenanigans_accessibility.png
```

---

## 🏚️ Sprite Sheet 1: Exterior & Alley Approach
**File:** `shenanigans_exterior.png`
**Dimensions:** 512x384 pixels
**Color Palette:** Faded Green #6B8E23 dominant, Alley Slate #4A5A6A cobbles, one warm Lucky Gold window against the gloom

### Facade & Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pub Front Facade | (0, 0) | 256x256 | Cramped pub front, chipped green paint, intentionally easy to miss |
| SHENANIGANS Sign | (256, 0) | 192x64 | Hand-painted letters, slightly crooked — plausible deniability in typography |
| Ancient Guinness Sign | (448, 0) | 64x64 | Decades of rust, still glowing faintly |
| Subtitle Sign | (256, 64) | 192x32 | "Traditional Irish Games & Craic" |
| Working Light On | (448, 64) | 32x32 | The ONE working exterior light |
| Working Light Flicker | (480, 64) | 32x32 | Its occasional struggle frame |
| Window Sign | (256, 96) | 128x64 | "TONIGHT: Lucky Spin Wheel! EVERYONE Wins!" (everyone loses) |
| Chalkboard | (384, 96) | 64x96 | "Happy Hour: 2-for-1 on selected drinks" (selection is nothing) |
| Warning Sign Tiny | (256, 160) | 96x16 | "For entertainment purposes only" — legally load-bearing, deliberately unreadable |
| Dead Lamp | (352, 160) | 32x32 | The non-working light, for contrast |

### Alley & Atmosphere:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rain-Slick Cobble Tile | (448, 96) | 64x64 | Wet Publandia side-street stone, reflective |
| Alley Wall Brick Tile | (448, 160) | 64x64 | Grimy brick, old poster scraps |
| Puddle Reflection Tile | (448, 224) | 64x64 | Neon "EVERYONE Wins!" mirrored in rainwater |
| Alley Approach Segment | (0, 256) | 128x128 | Side-alley entrance view — found by "accident" |
| Doorway Welcome Glow | (128, 256) | 128x64 | Warm light spilling out, suspiciously inviting |
| Sign Bracket & Chains | (128, 320) | 64x64 | Crooked mounting hardware for the crooked sign |
| Rain Gutter Drip | (192, 320) | 64x64 | Dripping downpipe, ambiance loop |
| Cobble Drain Variant | (448, 288) | 64x64 | Alley drain tile, coins glinting just out of reach |

### Doors, Windows & Touts:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Door Closed | (256, 176) | 64x96 | Green door, brass handle worn by ten thousand marks |
| Door Open | (256, 272) | 64x96 | Warmth and trad music pouring out |
| Window Glass Warm | (320, 192) | 64x64 | Too-friendly staff visible through glass |
| Window Glass Night | (384, 192) | 64x64 | Late-hour variant, games corner glowing |
| Tout Guide Idle | (320, 256) | 64x96 | Craic Tax tout who "just happens" to know a place |
| Tout Guide Gesture | (384, 256) | 64x96 | Pointing down the alley — the funnel in action |

### Technical Notes:
- Facade renders on base layer; signage as separate sprites for individual sway/flicker
- Working Light alternates On/Flicker on a 20-40s random timer (alpha toggle, disabled in reduced motion)
- Warning Sign Tiny scales up 4x on examine — the joke requires the zoom
- Puddle reflection uses simple pre-baked sprite, no realtime reflection shader

---

## 🍺 Sprite Sheet 2: Interior — The Con Cathedral
**File:** `shenanigans_interior.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** Sketchy Brown #654321 warmth, Lucky Gold game lighting, dim everywhere except where the drama needs brightness

### The Five Zones:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Entry (Welcome Mat) | (0, 0) | 256x256 | Disarming warmth, host podium, coat hooks |
| The Main Bar (Distraction) | (256, 0) | 384x256 | Comfortable seating, good music, softening zone |
| The Games Corner (Extraction) | (640, 0) | 384x256 | Where the real business happens — bright, staged, hungry |
| The Back Tables (Recovery) | (0, 256) | 256x256 | Comfort food and sympathy — the "one more try" pitch zone |
| The Snug (Long Con) | (256, 256) | 256x256 | Private booth for high-value marks; post-stamp observation deck |

### Zone Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Prize Display Case | (512, 256) | 128x128 | Prominent prizes, faint dust — rarely awarded |
| Lucky Penny Jar | (640, 256) | 64x64 | Rigged, obviously. Pennies glued at the visible layer |
| Welcome Drink Tray | (704, 256) | 64x64 | Complimentary drink (waters down subsequent orders) |
| Bar Back Shelf | (768, 256) | 128x64 | Legitimately good drinks — the trust-builder |
| Trad Session Corner | (896, 256) | 128x128 | Musicians mid-tune, one fiddle visibly a half-step off |
| Comfort Food Plate | (640, 320) | 64x64 | Recovery-zone stew, steam loop |
| Sympathy Pint | (704, 320) | 64x64 | Gráinne's on-the-house consolation |
| Snug Curtain Open | (768, 320) | 64x64 | Velvet, slightly worn |
| Snug Curtain Closed | (832, 320) | 64x64 | A whale is being processed |
| Worn Floor Path | (512, 384) | 128x128 | Floorboards visibly worn in a line from bar to games corner |
| Wall of "Winners" | (640, 384) | 128x64 | Framed photos of past champions — all of them staff |
| Celtic Clover Bunting | (768, 384) | 128x32 | Weaponized clover iconography strung over the games |
| Game Spotlight Cone | (896, 384) | 64x128 | Bright at the games for drama, dim enough elsewhere to hide tricks |
| "EVERYONE Wins!" Poster | (640, 448) | 128x64 | Interior repeat of the lie, bigger font |

### Technical Notes:
- Zones assembled as one TileMap; lighting handled per-zone via CanvasModulate regions (dim bar, bright games)
- Worn Floor Path overlays the base floor — environmental storytelling in one sprite
- Trad Session Corner animates 2 frames only (bow up/down); the off-key note lives in the audio layer
- Snug curtain state driven by `wise_fool_status` (open = observation access earned)

---

## 🎡 Sprite Sheet 3: The Rigged Games (All Seven)
**File:** `rigged_games.png`
**Dimensions:** 512x512 pixels
**Color Palette:** Lucky Gold #DAA520 and Neon Accent #FF4500 carnival brightness over Sketchy Brown apparatus

### The Lucky Spin Wheel:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wheel Base | (0, 0) | 128x128 | Colorful segments: JACKPOT, FREE DRINK, TRY AGAIN (mostly TRY AGAIN) |
| Wheel Frozen: TRY AGAIN | (128, 0) | 128x128 | The default resting state and selfie backdrop — 85% weighted home |
| Wheel: JACKPOT Photo State | (256, 0) | 128x128 | Mickey spins it here for photos only. "Don't tell anyone." |
| Spin Blur Frame 1 | (384, 0) | 64x64 | Motion blur, segments smeared gold |
| Spin Blur Frame 2 | (448, 0) | 64x64 | Faster blur variant |
| Spin Blur Frame 3 | (384, 64) | 64x64 | Deceleration blur |
| Spin Blur Frame 4 | (448, 64) | 64x64 | Final tick-tick-tick crawl |

### Three Card Monty & Darts:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Card Table Setup | (0, 128) | 128x64 | Felt table, "Find the Lady" chalked on the edge |
| Palmed Queen Reveal | (128, 128) | 64x64 | RIGGED DETAIL: the queen in Eamon's palm, visible on Wise Fool replay |
| Three Cards Face Down | (0, 192) | 96x48 | The shuffle state — she's not under any of them |
| Queen of Hearts Face | (96, 192) | 32x48 | The Lady herself, mostly ceremonial |
| Bent Dart Close-Up | (128, 192) | 64x32 | RIGGED DETAIL: your darts, subtly bent 20% off true |
| Straight Dart Comparison | (128, 224) | 64x32 | The staff's darts, insultingly regulation |
| Dart Board Regulation | (416, 128) | 96x96 | Their board is fine. That was never the problem |
| Dart Flight Frames | (416, 224) | 96x32 | 3 frames (32x32) of a dart curving wrong |

### Ring Toss:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ring Toss Booth | (192, 128) | 128x128 | Bottle array, carnival trim, "anyone can win" |
| Too-Small Ring | (320, 128) | 32x32 | RIGGED DETAIL: 0.5cm too small to ever seat clean |
| Oversized Bottle | (320, 160) | 32x64 | RIGGED DETAIL: neck slightly too large — physics-based deception |
| Ring vs Bottle Diagram | (352, 128) | 64x64 | Wise Fool overlay: the mathematical impossibility, annotated |
| Ring Near-Miss Bounce | (320, 224) | 32x32 | The "SO close" rattle-off frame |
| Rigged Reveal Glow | (352, 192) | 64x64 | Shared overlay glow marking any game exposed by Wise Fool sight |

### Cup Shuffle & Lucky Dice:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cup Shuffle Station | (0, 256) | 128x64 | Three cups on worn felt, follow along |
| Palmed Ball Hand Reveal | (128, 256) | 64x64 | RIGGED DETAIL: ball in hand, under no cup, ever |
| Three Cups Row | (0, 320) | 96x48 | Shuffle-ready formation |
| Ball Sprite | (96, 320) | 32x32 | The ball, in its natural habitat (Eamon's palm) |
| Lucky Dice Pair | (192, 256) | 64x64 | Innocent-looking dice, roll doubles for 3x |
| Loaded Dice Cutaway | (256, 256) | 64x64 | RIGGED DETAIL: internal weight visible — doubles hit 8%, not 16.7% |
| Dice Roll Frames | (192, 320) | 128x32 | 4 tumble frames (32x32) |
| Near-Miss Combos | (192, 352) | 128x32 | 5-6 and 4-5 results — programmed to hit often |

### The "Broken" Slot Machine:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Slot Machine Body | (320, 256) | 128x192 | Old machine, "usually broken but try your luck" |
| "Usually Broken" Sign | (448, 256) | 64x32 | Handwritten, hanging by one corner |
| Slot Reels Close-Up | (448, 288) | 64x64 | Reels programmed to pay just enough to keep you pulling |
| Payout Tease Frame | (448, 352) | 64x64 | Two clovers and an almost — psychological exploitation, per pull, 1 Sov |
| Slot Coin Tray | (320, 448) | 128x64 | Empty. Echoing. Occasionally clinks anyway |
| Wheel Pointer & Sticky Peg | (448, 416) | 64x96 | RIGGED DETAIL: the pointer peg that drags every spin home to TRY AGAIN |

### Odds & Bookkeeping:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "Displayed Odds" Placard | (0, 384) | 96x64 | 25% Free Drink, 25% Prize, 50% Try Again — the fiction |
| "Actual Odds" Ledger | (96, 384) | 96x64 | RIGGED DETAIL: 5% / 0% / 95% — Mickey's private arithmetic |
| Loss Tally Chalkboard | (0, 448) | 96x64 | Chalk marks nobody asked to be counted |
| Game Cost Signs | (96, 448) | 96x64 | 5 Sovs, 10 Sovs, "escalating" — the menu of hope |
| Darts Scoreboard | (192, 384) | 128x64 | Staff column permanently ahead |
| "Double or Nothing" Slate | (192, 448) | 128x64 | The escalation invitation, freshly chalked every night |

### Technical Notes:
- Every game has exactly one RIGGED DETAIL sprite — revealed only via "Wise Fool" status (one game per visit)
- Wheel spin composites Base + Blur frames; the deceleration is scripted, never physics (see Animation Specs)
- Slot Machine reels are a 3-frame vertical scroll, not per-symbol simulation — mobile budget respected
- Rigged Reveal Glow is reused across all seven games — one sprite, seven lies

---

## 🎩 Sprite Sheet 4: Mickey "The Mick" Finnegan
**File:** `mickey_finnegan.png`
**Dimensions:** 384x384 pixels
**Color Palette:** Slightly rumpled suit browns, Lucky Gold pocket accents, warmth in every frame — the calculations stay in the eyes

### Mickey States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| The Welcome | (0, 0) | 96x128 | Arms open, warm smile: "You look lucky." |
| During-Scam Encouragement | (96, 0) | 96x128 | Leaning in at the wheel: "Ohhh, SO close! Go again, I feel it." |
| Consoling | (192, 0) | 96x128 | Hand on shoulder, drink extended: "Rough night? Happens to everyone." |
| Wise Fool Toast | (288, 0) | 96x128 | Glass raised, the one genuine frame in the building |
| Stamp Ceremony | (0, 128) | 96x128 | Passport open, stamp descending — "Not for winning. For losing with grace." |
| Selfie Wheel-Rig | (96, 128) | 96x128 | Nudging the wheel to JACKPOT for the photo, finger to lips |
| Warm Laughter | (192, 128) | 96x128 | Head back, delighted — at you, with you, both |
| Shill Offer Lean-In | (288, 128) | 96x128 | Conspiratorial: "50 Sovs per night to play 'winner' for fresh marks." |

### Mickey Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rumpled Suit Texture | (0, 256) | 64x64 | Third-generation entertainment-entrepreneur tailoring |
| Twinkling Eyes Close-Up | (64, 256) | 64x64 | Warmth over calculation, calculation clearly visible |
| Hands with Stamp | (128, 256) | 64x32 | Faded-gold ink pad and stamp, held like a sacrament |
| Raised Glass | (192, 256) | 32x32 | Fool's Gold, for the toast |
| Stamp Slam Frames | (224, 256) | 96x32 | 3 frames (32x32): lift, hover, THUNK |
| Pocket Watch Charm | (320, 256) | 32x32 | Grandfather's, from the O'Connell Street days |

### Mickey Expressions:
| Expression | Position | Size | Description |
|------------|----------|------|-------------|
| Warm Calculation | (0, 288) | 48x48 | Default: reading your wallet through your face |
| Sympathy | (48, 288) | 48x48 | Post-loss consolation, 90% sincere |
| Genuine Respect | (96, 288) | 48x48 | Wise Fool moment — the mask and the face match |
| Delight | (144, 288) | 48x48 | Every fool is a character; you're a good one |
| "Gotcha" Twinkle | (192, 288) | 48x48 | The half-second the con shows through, for players paying attention |

### Dialogue Portraits:
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Portrait Welcome | (0, 336) | 64x48 | For dialogue boxes, standard warmth |
| Portrait Consoling | (64, 336) | 64x48 | Softened, drink-offering |
| Portrait Wise Fool | (128, 336) | 64x48 | Genuine — used only for the stamp conversation |
| Portrait Post-Stamp | (192, 336) | 64x48 | "My favorite fool!" |

### Technical Notes:
- The Wise Fool Toast and Stamp Ceremony frames must read as tonally DIFFERENT — drop the twinkle, keep the warmth
- "Gotcha" Twinkle appears for 0.3s max during scam encouragement — an easter egg, never a tell the game punishes you for missing
- Portrait Wise Fool is gated to the stamp conversation; reuse anywhere else breaks the beat

---

## 👥 Sprite Sheet 5: Staff — The Shill Network
**File:** `shenanigans_staff.png`
**Dimensions:** 512x256 pixels
**Color Palette:** Shill Flush #E8875A celebration warmth; costumes read "customer," body language reads "payroll"

### Staff States (Row 1):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Darren "Winning" Idle | (0, 0) | 96x128 | Lucky charm bracelet, perpetual victor's posture |
| Darren Celebrating | (96, 0) | 96x128 | "YESSSS! Third time tonight! This wheel is HOT!" (staged) |
| Gráinne with Drink Tray | (192, 0) | 96x128 | Sympathy drinks inbound: "Here, have a drink. On me." |
| Gráinne Consoling | (288, 0) | 96x128 | Recovery-zone specialist, keeps marks in the building |
| Eamon Dealing | (384, 0) | 96x128 | Sleepy eyes hiding alertness, cards moving like water |

### Staff States (Row 2) & Details:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Eamon Fast Hands | (0, 128) | 96x128 | Sleight blur — the hands the eye cannot follow |
| Eamon Post-Stamp | (96, 128) | 96x128 | "I could teach you the moves. Not here, though. Mickey'd kill me." |
| Darren Post-Stamp Nod | (192, 128) | 96x128 | Quiet, act dropped: "Fair play. Most people never figure it out." |
| Gráinne Post-Stamp Smile | (288, 128) | 96x128 | "You're one of the good ones. Most blame me somehow." |
| Lucky Charm Bracelet | (480, 0) | 32x32 | Darren's prop — luck as costume |
| Sympathy Pint Detail | (480, 32) | 32x32 | Gráinne's signature delivery |
| Eamon's Cuff Card | (480, 64) | 32x32 | A queen's corner peeking from a sleeve |
| Wink Sparkle | (480, 96) | 32x32 | Shill-to-shill signal glint |

### Staff Portraits & Group Beats:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Portrait Darren | (384, 128) | 64x48 | Enthusiasm, factory-fresh |
| Portrait Gráinne | (448, 128) | 64x48 | Warmth, professionally deployed |
| Portrait Eamon | (384, 176) | 64x48 | Sleepy-eyed, sees everything |
| Shill Sync Frame | (448, 176) | 64x48 | Two shills celebrating in accidental unison — the tell |
| Synchronized Arm-Wave Strip | (384, 224) | 128x32 | 4 frames (32x32) of suspiciously coordinated cheering |

### Technical Notes:
- Shills win publicly, lose privately: Celebration states trigger on OTHER players' near-misses, never their own turns
- Synchronized Arm-Wave plays 0.2s offset per shill normally; in the "tell" moment, offset drops to zero
- Post-stamp states swap in globally once `wise_fool_status = true` — the whole room drops the act for you

---

## 🎭 Sprite Sheet 6: The Marks
**File:** `mark_npcs.png`
**Dimensions:** 512x256 pixels
**Color Palette:** Tourist brights fading toward Sketchy Brown as the losses accumulate

### Mark States (Row 1):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Angry Tourist Ranting | (0, 0) | 96x128 | "This is FRAUD! I want my 100 Sovs back! I'm calling the— who do I even call?!" |
| Angry Tourist Deflated | (96, 0) | 96x128 | Accepting Mickey's consolation drink mid-rant |
| Oblivious Optimist at Wheel | (192, 0) | 96x128 | Deep in losses, spending freely, luck due any spin now |
| Optimist "SPIN AGAIN" | (288, 0) | 96x128 | "It HAS to hit eventually! Statistics! Law of averages!" |
| Repeat Fool Peaceful | (384, 0) | 96x128 | Years of losses, zero regrets: "I know it's rigged. So's life." |

### Mark States (Row 2) & Details:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Fresh Marks Trio | (0, 128) | 192x128 | Tourist group — the bros' mirror: "DUDE this place is AWESOME!" |
| Fresh Mark High-Five | (192, 128) | 96x128 | Pre-loss confidence, painful in hindsight |
| Repeat Fool with Mickey | (288, 128) | 96x128 | Losing peacefully, chatting like old friends |
| Empty Wallet Flutter | (480, 0) | 32x32 | Moths optional but encouraged |
| Spilled Coin Purse | (480, 32) | 32x32 | The 50 Sovs "Deep Mark" moment |
| Flop Sweat Drop | (480, 64) | 32x32 | Stage 4: "I've spent too much to quit now" |
| Hope Sparkle | (480, 96) | 32x32 | Irrational, renewable, monetized |

### Mark Portraits & Despair:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Portrait Angry Tourist | (384, 128) | 64x48 | Realization rage |
| Portrait Optimist | (448, 128) | 64x48 | Sunk-cost serenity |
| Portrait Repeat Fool | (384, 176) | 64x48 | The Wise Fool end state, lived-in |
| Portrait Fresh Mark | (448, 176) | 64x48 | About to learn everything |
| Despair Slump Strip | (384, 224) | 128x32 | 4 frames (32x32): the mark's journey, shoulders only |

### Technical Notes:
- Fresh Marks Trio spawns only when the bros first enter — the mirror lands once, then they rotate out
- Despair Slump Strip is shared by all marks including the player party during loss stingers
- Max 4 mark NPCs on screen (reduced shill/crowd count per performance budget)

---

## 🏅 Sprite Sheet 7: Brewery Tour Items & Selfie Spot
**File:** `brewery_items.png`
**Dimensions:** 256x256 pixels
**Color Palette:** Faded gold stamp ink (#DAA520 desaturated — like your lost money), Wilted Sage #9CAF88 for the dead leaf

### The Stamp & The Beer:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shenanigans Stamp | (0, 0) | 64x64 | Circular, jester cap border, three-leaf clover with one leaf wilted; "Shenanigans" banner arcs the top, and along the bottom rim the words "Wise Fool Since" flow into a four-digit year worked directly into the engraving — the year renders as part of the stamp art, weathered like the rest |
| Stamp Inked on Passport | (64, 0) | 64x64 | Faded-gold impression, slightly smudged — pressed with feeling |
| Fool's Gold Bottle | (128, 0) | 32x64 | Golden Ale, honey glint, bitter-finish label. The only honest thing here |
| Fool's Gold Poured Pint | (160, 0) | 32x64 | Golden, hopeful, bitter finish — just like your evening |
| Fool's Gold Inventory Icon | (192, 0) | 32x32 | +30 HP, +15 SP, "Learned Optimism" chance |
| Bottle Cap Clover | (224, 0) | 32x32 | Three leaves, one wilted — brand consistency in defeat |
| Stamp Ink Pad | (192, 32) | 32x32 | Faded gold, refilled with lost money (spiritually) |
| "House Rules" Coaster | (224, 32) | 32x32 | "First one free. We're not heartless." |

### Badges, Crowns & Prerequisites:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shill Badge | (0, 64) | 32x32 | If you turned — 50 Sovs/night, soul sold separately |
| Moral Fool Badge | (32, 64) | 32x32 | If you didn't — kept your soul, Mickey respects it more |
| Bottle Opener Keychain Icon | (64, 64) | 32x32 | The Blarney Trap prerequisite, shown grayed until owned |
| Lucky Penny | (96, 64) | 32x32 | Pried loose from the rigged jar (achievement flavor) |
| Wise Fool Paper Crown | (128, 64) | 48x48 | Paper crown, earned through stamp — royalty of losing gracefully |
| Jester Cap Prop | (176, 64) | 48x48 | Selfie prop, bells included |
| Mickey's Tips Notebook | (224, 64) | 32x32 | Genuine scam-avoidance tips — post-stamp gift |

### Brewmaster Selfie Spot:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Selfie Backdrop | (0, 96) | 128x96 | In front of the Lucky Spin Wheel frozen on TRY AGAIN, rigged games arrayed behind |
| Sad Empty Wallet Prop | (128, 112) | 48x48 | Joke prop, held aloft with pride |
| Crown Selfie Variant | (176, 112) | 48x48 | Wise Fool crown, worn, slightly crumpled |
| Selfie Flash Overlay | (128, 160) | 64x32 | White burst, one frame |
| Photo Frame Border | (192, 160) | 64x32 | Clover-corner frame for the share card |
| Stamp Ceremony Tableau | (0, 192) | 256x64 | 4 frames (64x64): Mickey's toast → passport open → stamp slam → the handshake |

### Technical Notes:
- The stamp's year is BAKED INTO THE ART as engraved numerals — it is not a dynamic text field and must never render as one
- Selfie Backdrop supports the JACKPOT wheel swap (sheet 3) when Mickey rigs it for the photo — the only time it will ever land there
- Fool's Gold assets are shared with The Blarney Trap post-stamp (see Cross-Location Dependencies)

---

## 🎮 Sprite Sheet 8: UI & Effects
**File:** `shenanigans_ui_fx.png`
**Dimensions:** 512x384 pixels
**Color Palette:** Neon Accent #FF4500 near-miss urgency, Lucky Gold progress, Guinness Cream panel text

### Scam Mini-Game UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mini-Game Interface Frame | (0, 0) | 256x192 | Shared frame for all seven games: cost display, "TAP TO STOP" button, outcome window |
| Near-Miss Indicator | (256, 0) | 128x64 | "So close!" burst — fires on every engineered almost |
| Loss Total Tracker | (256, 64) | 128x32 | Running shame count in Sovs, always visible, always growing |
| Wise Fool Progress | (256, 96) | 128x64 | 3 scam-loss pips + return-visit marker — the path to the stamp |
| Shill Offer Moral Choice | (384, 0) | 128x160 | Accept / Decline / Ask for more — 50 Sovs a night vs. your soul |
| Stamp Ceremony UI | (256, 160) | 192x128 | Mickey's toast panel, passport slot, stamp descent zone |
| Learned Optimism Buff Icon | (448, 160) | 32x32 | +10% scam-detection resistance — the beer working |
| Sentimental Debuff Icon | (448, 192) | 32x32 | 5% risk: donate extra gold to NPCs, weepily |
| Rigged Reveal Eye Icon | (480, 160) | 32x32 | Wise Fool sight — marks ONE game "RIGGED" per visit |
| Odds Toggle Icon | (480, 192) | 32x32 | Displayed odds ⇄ actual odds flip (post-stamp examine) |
| "Double or Nothing?" Warning | (448, 224) | 64x64 | Escalation confirm — the game's one honest hesitation |

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wheel Spin Sparkle Strip | (0, 192) | 128x32 | 4 frames (32x32) of gold glint chasing the rim |
| Dice Tumble Dust | (128, 192) | 64x32 | 2 puff frames |
| Card Shuffle Blur | (192, 192) | 64x32 | Motion smear for Eamon's hands |
| Shill Confetti Burst | (0, 224) | 96x32 | Celebration particles — CPU-budget confetti, 3 frames |
| Sad Trombone Glyphs | (96, 224) | 64x32 | Descending notes, subtle, comically sad |
| "Awww" Crowd Bubble | (160, 224) | 64x32 | Sympathetic crowd exhale, visualized |
| Coin Drain Strip | (0, 256) | 128x32 | 4 frames (32x32): coins migrating from your side of the table |
| Near-Miss Tick Glow | (128, 256) | 64x32 | The wheel peg lighting up one segment short of JACKPOT |
| Spotlight Flicker | (192, 256) | 64x32 | Games-corner drama lighting, 2 frames |
| Loss Stinger Vignette | (0, 288) | 128x96 | Screen-edge darkening for the comically sad loss beat |
| Shill Win Burst | (128, 288) | 128x96 | The rare "win" celebration — shill-only, gloriously overdone |

### Achievement Toasts:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Toast Strip A | (256, 288) | 256x48 | 4 cards (64x48): "Mark" / "Deep Mark" / "Diversified Fool" / "Persistent Fool" |
| Toast Strip B | (256, 336) | 256x48 | 4 cards (64x48): "Graduated" / "Moral Fool" / "Turned" / blank clover-pattern spare |

### Technical Notes:
- Mini-Game Interface tap targets (spin button, cup selects, card selects) all meet 44px minimum
- Input on the "TAP TO STOP" button is cosmetic — outcomes are predetermined at entry (see Technical Integration)
- Loss Total Tracker persists across games in a CanvasLayer; it never resets during a visit, by design

---

## 🎬 Animation Specifications

### Wheel Spin with Rigged Deceleration:
- **Duration:** 4.5 seconds total
- **Frames:** 12 (4 blur frames cycled, then 4-frame deceleration crawl, then hold)
- **Pattern:** Blur 1→2→3→4 loop (2.5s) → decel crawl slowing over 1.5s → dramatic 0.5s near-JACKPOT hesitation → settle on TRY AGAIN
- **Trigger:** Player taps "TAP TO STOP" (input timing has zero effect on outcome)
- **Purpose:** Sell a fair spin that was decided the moment 5 Sovs left the wallet; the final hesitation IS the product
- **Audio Sync:** Wheel whir during blur; tick-tick-tick on decel; the "almost" landing sound on the hesitation; sad trombone on settle
- **Mobile Optimization:** Scripted keyframes, no physics simulation (simplified wheel physics per budget); Low LOD skips blur frames entirely

### Card Shuffle Sleight:
- **Duration:** 3 seconds per round
- **Frames:** 8 shuffle + 1 palm frame
- **Pattern:** Cards cross 1→2→3→...→8 with accelerating swap rhythm; palm frame inserted at frame 5, visible only on Wise Fool replay
- **Trigger:** Three Card Monty round start
- **Purpose:** The queen leaves the table mid-shuffle; the game is over before the choice is offered
- **Audio Sync:** Card shuffle riffle throughout; soft felt-slap per swap
- **Mobile Optimization:** Low LOD drops to 4 shuffle frames; palm frame always retained (it's the joke)

### Cup Shuffle Speed Progression:
- **Duration:** 2.5s (round 1) scaling down to 1.2s (round 4+)
- **Frames:** 6 per shuffle pass
- **Pattern:** Cup swap cycle at 1x speed → 1.4x → 1.8x → 2.2x across consecutive rounds ("it got faster" explains every failure)
- **Trigger:** Cup Shuffle round start; speed tier = consecutive rounds played
- **Purpose:** Escalating speed launders the impossible into the merely difficult
- **Audio Sync:** Cup slide scrapes per swap; "awww" cue on reveal
- **Mobile Optimization:** Speed tiers capped at 1.8x on low-end devices; blur sprite substitutes for high-tier frames

### Dice Roll (Loaded):
- **Duration:** 1.8 seconds
- **Frames:** 4 tumble + 1 settle
- **Pattern:** Tumble 1→2→3→4 (1.2s) → bounce → settle on near-miss combo (5-6 and 4-5 weighted to appear often)
- **Trigger:** Player shake-and-release gesture (feels random, isn't)
- **Purpose:** Doubles at 8% instead of 16.7%; the near-miss combos do the retention work
- **Audio Sync:** Dice rattle during tumble; double-clack on settle
- **Mobile Optimization:** Pre-baked tumble sprite frames, no rigid-body sim

### Shill Celebration:
- **Duration:** 2 seconds
- **Frames:** 6 (arm-wave strip x4 + confetti burst x3 overlapped)
- **Pattern:** Darren leaps → arms up → confetti → hold grin → settle; nearby shills join at 0.2s offsets
- **Trigger:** Any mark's near-miss, or scripted "win" beat every 90-120s
- **Purpose:** Manufactured proof that winning is possible; synchronization glitch (0s offset) is the discoverable tell
- **Audio Sync:** Fake winner celebration whoop; glass clinks; Mickey's warm laughter tail
- **Mobile Optimization:** Confetti capped at 12 particles; Low LOD uses static Shill Win Burst sprite, no particles

### Near-Miss Beat:
- **Duration:** 1.2 seconds
- **Frames:** 3 (tick glow → "So close!" indicator pop → fade)
- **Pattern:** Near-Miss Tick Glow on the losing element → indicator spring-pop (0.3s) → hold (0.6s) → fade
- **Trigger:** Every engineered almost: wheel one segment short, dice at 5-6, ring rattle-off, dart lip-out
- **Purpose:** The core retention loop of the entire location, rendered honest by repetition
- **Audio Sync:** The "almost" landing sound, then sympathetic "awww" from crowd
- **Mobile Optimization:** None needed — three sprites and a tween

### Mickey Idle Cycle:
- **Duration:** 12 seconds loop
- **Frames:** Welcome stance (5s) → survey room (2s) → polish glass (3s) → pocket watch check (1s) → warm chuckle (1s)
- **Pattern:** Sequential with 10% chance to insert "Gotcha" Twinkle expression for 0.3s during survey
- **Trigger:** Constant while Mickey is unengaged
- **Purpose:** The room's warm center of gravity; the twinkle rewards observant players
- **Audio Sync:** Occasional warm laughter on the chuckle beat
- **Mobile Optimization:** Low LOD drops survey and watch-check beats

### Stamp Ceremony:
- **Duration:** 6 seconds
- **Frames:** 4 tableau frames + 3 stamp slam frames
- **Pattern:** Toast raise (2s) → passport open (1s) → stamp lift-hover-THUNK (1.5s) → handshake hold (1.5s)
- **Trigger:** "Wise Fool" conversation completion (3 scams lost + return visit + Bottle Opener Keychain)
- **Purpose:** The one un-rigged moment in the building; play it completely straight
- **Audio Sync:** Mickey's genuine toast on raise; page rustle; deep stamp THUNK; glasses clink on handshake hold
- **Mobile Optimization:** None needed — this moment gets full budget on every device

---

## ♿ Accessibility Sprite Requirements
**File:** `shenanigans_accessibility.png` (supplemental sheet — delivered alongside the 8 base files, not counted in their total)
**Dimensions:** 256x256 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mini-Game Interface, Bold | (0, 0) | 96x64 | Thick-bordered game frame, enlarged cost/outcome text |
| "RIGGED" Reveal Banner | (96, 0) | 96x32 | High-contrast RIGGED banner: bold text + crossed-dice glyph, never color alone |
| Wheel Segments, Patterned | (192, 0) | 64x64 | JACKPOT striped / FREE DRINK dotted / TRY AGAIN solid — outcomes readable without color |
| Game Hotspot Outlines | (96, 32) | 96x32 | White-on-dark outlines for all seven game interaction zones |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wheel, Reduced Spin | (0, 64) | 64x64 | Stepped pointer advance replacing full-spin blur — same rigged outcome, no rotation blur |
| Celebration, Static | (64, 64) | 64x64 | Shill Win Burst as single static frame — confetti particles disabled |
| Cup Shuffle, Step Mode | (128, 64) | 64x64 | Discrete swap positions replacing accelerating slide animation |
| Dice, Static Result | (192, 64) | 64x64 | Settle frame only — tumble sequence skipped |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wheel Spin Whir Icon | (0, 128) | 32x32 | Spiral-lines glyph while the wheel spins |
| Dice Rattle Icon | (32, 128) | 32x32 | Shake-lines dice glyph during tumble |
| Card Shuffle Flutter Icon | (64, 128) | 32x32 | Riffling-cards glyph during Eamon's shuffles |
| Fake Winner Celebration Burst | (96, 128) | 32x32 | Starburst + "WIN?" glyph when shills erupt |
| Sympathetic "Awww" Bubble | (128, 128) | 32x32 | Crowd-sigh speech bubble on every reveal |
| Sad Trombone Glyph | (160, 128) | 32x32 | Descending notes on the loss stinger |
| "Almost" Landing Tick | (192, 128) | 32x32 | Single bright tick mark on the near-miss hesitation |
| Stamp Toast Clink Icon | (224, 128) | 32x32 | Two glasses meeting — Mickey's genuine stamp-ceremony toast, visualized |
| Off-Key Note Wobble | (0, 160) | 32x32 | Wavy note glyph for the slightly-wrong trad music |
| Warm Laughter Ripple | (32, 160) | 32x32 | Soft ripple rings for Mickey's laughter |

### Touch Targets & Reduced-Motion UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Large Spin Button | (64, 160) | 48x48 | 48px tap-to-stop button (exceeds 44px minimum) |
| Cup Select Zones, Large | (112, 160) | 144x48 | Three 48px cup selection targets |
| High-Contrast Loss Tracker | (0, 208) | 112x48 | Bold-bordered loss total, enlarged Sov count |
| Stamp Ceremony, Static | (128, 208) | 128x48 | Single-frame toast tableau for reduced-motion mode |

### Colorblind Considerations:
- Rigged-game reveals NEVER rely on color alone: the "RIGGED" banner pairs bold text with the crossed-dice glyph, and the Rigged Reveal Glow adds a dashed outline pattern
- Wheel outcomes are pattern-coded (striped/dotted/solid) in addition to color; displayed-vs-actual odds use text labels, not red/green
- Shill Badge vs Moral Fool Badge differ in shape (angular vs rounded), not just palette
- All seven mini-game inputs (spin button, card picks, cup picks, ring throw, dart throw, dice shake, slot pull) meet the 44px minimum touch target

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 for environment sheets; ASTC 4x4 for Mickey, the stamp, and all UI text elements (dialogue portraits and stamp engraving need the fidelity)
- **Android:** ETC2 with alpha across all sheets
- **Fallback:** Lossless PNG for `brewery_items.png` (stamp legibility is quest-critical) and `shenanigans_ui_fx.png`

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| shenanigans_environment | exterior, interior | 2048x2048 |
| shenanigans_characters | mickey_finnegan, shenanigans_staff, mark_npcs | 1024x1024 |
| shenanigans_games_items | rigged_games, brewery_items | 1024x1024 |
| shenanigans_ui | shenanigans_ui_fx, shenanigans_accessibility | 1024x1024 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full wheel blur frames, 8-frame card shuffle, confetti particles, 4 mark NPCs, all 3 shills active |
| Medium | Reduced confetti (8 particles), 4-frame shuffle, 3 mark NPCs, 2 shills active |
| Low | Static blur substitutes, step-mode cup shuffle, 2 mark NPCs, 1 shill (reduced shill count), no particles |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 14 per frame (per location performance budget)
- **Memory Footprint:** 35 MB maximum
- **Particle Limit:** 20 (confetti capped at 12 per burst, dice dust 4, sparkle 4)

### Performance Notes:
- Simplified wheel physics: the spin is scripted keyframes, never a physics body — the rig demands determinism anyway
- Reduced shill count on Medium/Low LOD (3 → 2 → 1); shill dialogue reassigns to remaining actors
- Only one mini-game animates at a time; background games hold static frames
- The Snug loads as a sub-scene on demand — whales are processed off the main memory budget
- Trad session, spotlight flicker, and exterior light flicker are alpha toggles, not shaders

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Interior zones as one TileMap with per-zone CanvasModulate lighting; ParallaxBackground for the alley approach
- CPUParticles2D (not GPU) for confetti, dice dust, and rain drip; all particle emitters respect the 20-particle cap and disable in reduced-motion mode
- **Rigged mini-game logic:** ALL seven games resolve their outcome at buy-in, before any player input. The "TAP TO STOP," aim, shake, and throw inputs are cosmetic. Near-miss results are drawn from weighted tables (wheel 95% TRY AGAIN, dice 8% doubles, monty/cups 0% win). "Wise Fool" status flags exactly ONE game per visit as `revealed_rigged`, swapping in its RIGGED DETAIL sprite and the Rigged Reveal Glow before play
- Area2D examine points: lucky penny jar, tiny warning sign (4x zoom), prize display case, wall of "Winners," displayed/actual odds placards (post-stamp toggle), worn floor path
- State tracking per `shenanigans_state` (losses_by_game, total_lost, scams_lost_distinct, returned_after_losses, wise_fool_status, shill_offer_result, stamp_earned, fools_gold_unlocked, frequent_victim)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Wheel Spin (4.5s) | Wheel spinning whir → tick crawl | Whir through blur phase; ticks per decel frame |
| Wheel near-JACKPOT hesitation | The "almost" landing sound | On the 0.5s hesitation, every time |
| Dice Tumble | Dice rolling rattle | Rattle through tumble; double-clack on settle |
| Card Shuffle Sleight | Cards shuffling riffle | Riffle spans all 8 frames; silent on the palm frame (the crime is quiet) |
| Shill Celebration | Fake winner celebrations | Whoop on the leap; Mickey's warm laughter on the tail |
| Any loss reveal | Sympathetic "awww" from crowd | On the reveal frame |
| Loss Stinger Vignette | Sad trombone (subtle) | Descending with the vignette fade-in |
| Stamp Ceremony tableau | The Stamp Sound — Mickey's genuine toast | Toast line on glass raise; deep THUNK on stamp slam; clink on handshake hold |
| Trad Session Corner | Traditional Irish, slightly off-key | Continuous ambient; wrong note every 4th bar |
| Shill Offer Moral Choice open | Music drops to a hush | On panel open — the one quiet decision |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Wise Fool Stamp Path | All seven game apparatuses + RIGGED DETAIL sprites, Wise Fool Progress UI, Mickey Wise Fool Toast + Stamp Ceremony states, Stamp Ceremony UI, Shenanigans Stamp, Stamp Ceremony tableau | Lose at 3 DIFFERENT scams AND return to Shenanigans; requires Bottle Opener Keychain from The Blarney Trap (grayed keychain icon shows the gate); Mickey approaches personally and the ceremony fires |
| The Shill Offer (Moral Choice) | Shill Offer Moral Choice panel, Mickey Shill Offer Lean-In, Shill Badge / Moral Fool Badge, Toast Strip B ("Turned" / "Moral Fool") | Post-stamp trigger; Accept = 50 Sovs/night + Shill Badge, Decline = Moral Fool Badge + deeper respect, Ask for more = Mickey laughs, still respects you |
| Brewmaster Selfie | Selfie Backdrop, Wheel JACKPOT Photo State, Sad Empty Wallet Prop, Jester Cap Prop, Crown Selfie Variant, Selfie Flash Overlay, Photo Frame Border | Selfie spot in front of the wheel; Mickey swaps the wheel to JACKPOT for the photo only — "Don't tell anyone." |
| Fool's Gold Unlock | Fool's Gold Bottle, Poured Pint, Inventory Icon, Learned Optimism Buff Icon, Sentimental Debuff Icon | Unlocks with the stamp; first one free per house rules; the only purchase in the building with honest odds |
| Achievement Track | Toast Strips A & B, Despair Slump Strip, Empty Wallet Flutter | "Mark" → "Deep Mark" → "Diversified Fool" → "Persistent Fool" → "Graduated" → "Moral Fool"/"Turned" |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Blarney Trap | Bottle Opener Keychain icon (stamp prerequisite); Fool's Gold Bottle + icon appear on Blarney Trap shelves post-stamp (Seamus smirks knowingly — he and Mickey are old friends, honest trap and dishonest trap in mutual respect) | Shared item sprites; Seamus dialogue references Mickey by name |
| The Craic Tax | Tout Guide Idle/Gesture sprites — the tout network funnels tourists down the side alley "by accident" | Tout hand-off transition from the Craic Tax street scene into the alley approach |
| The Craic Broker | Warning dialogue references the alley approach and SHENANIGANS sign sprites; respects players who go anyway | Standard street transition; Broker's warning icon appears over the alley entrance if the warning was heard |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A con so warm you tip it on the way out — carnival gold drowning in pub brown"
- **Color Mood:** Lucky Gold and Neon Accent promise everything under game spotlights; Sketchy Brown and Faded Green deliver the truth everywhere else; Wilted Sage keeps one leaf dead in every clover
- **Lighting:** Dim enough to hide tricks, bright at the games for drama — the lighting design IS the scam architecture
- **Texture:** Chipped exterior paint, rain-slick alley cobbles, worn felt on every game table, a floor path polished by ten thousand marks walking bar-to-wheel

### Environmental Storytelling:
- The worn floor path from Main Bar to Games Corner — the house's funnel, written in floorboard wear
- The Wall of "Winners": every framed champion is recognizably a staff member
- Displayed odds placard in cheerful paint; actual odds ledger in Mickey's cramped pencil — the whole satire in two props
- The tiny "For entertainment purposes only" sign doing legal load-bearing work at 16px
- Celtic clover bunting over the games — luck iconography weaponized, one wilted leaf per garland if you look closely

### Character Integration Notes:
- Mickey is warmth first, calculation second — the twinkle never fully leaves except in the Wise Fool Toast and Stamp Ceremony frames, where it must
- Shills read as customers at a glance and as payroll on a second look: too-clean celebration timing, eyes that check Mickey before cheering
- Marks arc visually from tourist-bright to pub-brown as losses stack; the Fresh Marks Trio wears the bros' palette

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Wheel Frozen on TRY AGAIN** - The selfie backdrop that IS the location's thesis statement
2. **The JACKPOT Photo Rig** - Mickey nudging the wheel for your photo, finger to lips — the shareable open secret
3. **The Wall of "Winners"** - Every winner is staff; the internet will notice in seconds
4. **The Wise Fool Stamp Ceremony** - Jester cap border, wilted clover, faded gold — earned by LOSING
5. **The "Actual Odds" Ledger** - 5% / 0% / 95% next to the cheerful displayed odds placard
6. **The Sad Empty Wallet Selfie** - Jester cap on, wallet aloft, wheel on TRY AGAIN behind

### Quote Potential:
- "You've earned the stamp. Not for winning. For understanding what winning actually is."
- "The games are rigged, but the hope is real. You can't bottle hope. But you CAN sell it for 5 Sovs a spin."
- "The beer's real. I'm not a MONSTER. You can't scam someone on the beer. That's sacred."
- "I know it's rigged. So's life. At least here the beer's good and Mickey's honest about it."
- "I'll spin it to 'JACKPOT' for the photo. Only time it'll ever land there. Don't tell anyone."
- "It says you're human. Welcome to the club."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | shenanigans_exterior.png | 512x384 |
| 2 | shenanigans_interior.png | 1024x512 |
| 3 | rigged_games.png | 512x512 |
| 4 | mickey_finnegan.png | 384x384 |
| 5 | shenanigans_staff.png | 512x256 |
| 6 | mark_npcs.png | 512x256 |
| 7 | brewery_items.png | 256x256 |
| 8 | shenanigans_ui_fx.png | 512x384 |

**Total Estimated Memory:** ~22 MB (within the 35 MB location budget, headroom reserved for audio and the Snug sub-scene)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `shenanigans_exterior.png` (512x384)
- [ ] `shenanigans_interior.png` (1024x512)
- [ ] `rigged_games.png` (512x512)
- [ ] `mickey_finnegan.png` (384x384)
- [ ] `shenanigans_staff.png` (512x256)
- [ ] `mark_npcs.png` (512x256)
- [ ] `brewery_items.png` (256x256)
- [ ] `shenanigans_ui_fx.png` (512x384)
- [ ] `shenanigans_accessibility.png` (256x256, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (each game's RIGGED DETAIL sprite on its own layer for the Wise Fool reveal system; stamp engraving layers preserved so the year stays baked into the art)
- **Documentation:** Animation timing reference sheet (4.5s wheel deceleration curve, cup shuffle speed tiers, shill celebration offsets, 6s stamp ceremony)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Faded Green #6B8E23, Lucky Gold #DAA520, Sketchy Brown #654321, Neon Accent #FF4500)
- [ ] The stamp's wilted clover leaf reads clearly at 64x64 AND at inventory scale — the dead leaf is the whole joke
- [ ] The Too-Small Ring visibly cannot fit the Oversized Bottle in the Wise Fool diagram — the impossibility must be legible, not implied
- [ ] Fool's Gold assets read as genuinely appealing — the only honest thing in the building should LOOK like the only honest thing in the building
- [ ] "For entertainment purposes only" is illegible at world scale and crisp at 4x examine zoom
- [ ] Wheel TRY AGAIN frozen state and JACKPOT photo state are pixel-consistent apart from pointer position
- [ ] Accessibility visual alternatives included for all audio cues (wheel whir, dice rattle, shuffle, fake celebrations, "awww," sad trombone, "almost" tick, stamp toast)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (obvious scams that work anyway; respect earned through graceful losing) is clear throughout all assets
- [ ] All seven RIGGED DETAIL sprites discoverable via Wise Fool sight: sticky peg, palmed queen, too-small ring, bent darts, palmed ball, loaded dice cutaway, actual-odds ledger
- [ ] Easter eggs discoverable: Wall of "Winners" all-staff photos, worn floor path, "Gotcha" Twinkle, shill synchronization tell, one wilted leaf in every clover garland
- [ ] Mobile performance optimized (scripted wheel, 20-particle cap, reduced shill count on LOD, one animated game at a time)
- [ ] Touch zone sizing considered (44px minimum — all seven mini-game inputs compliant, 48px large variants on the accessibility sheet)
- [ ] Colorblind-friendly alternatives available where color codes meaning (patterned wheel segments, glyph-paired RIGGED banner, shape-differentiated badges)
- [ ] Social media viral potential maximized (TRY AGAIN selfie framing, JACKPOT photo rig, empty wallet prop composition)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia only; Dublin exists solely as a satirical reference in design docs, never in-game art |
| Cultural Specificity | ✅ | Irish tourist-trap pub economy, carnival game psychology, trad-session-slightly-off-key texture |
| Satirical Targets Appropriate | ✅ | Punches at tourist gullibility, sunk-cost bros, and "I can beat the system" mentality — never at locals (locals don't come here; tourists are brought here) |
| Seedy Underbelly Present | ✅ | Seven rigged games, a 3-5 person shill network, tout funneling, whale processing in the Snug — vice is the load-bearing wall |
| Gameplay Value Established | ✅ | Seven scam mini-games, loss-based stamp progression, Wise Fool reveal mechanic, Shill Offer moral choice, achievement track |
| Technical Feasibility | ✅ | Scripted (non-physics) wheel, alpha-toggle lighting, one-animated-game rule, Snug sub-scene loading all documented |
| Mobile Performance Budget | ✅ | 60 FPS target, 14 draw calls max, 35 MB cap (~22 MB spent), 20-particle limit, LOD-tiered shill count |
| Accessibility Features | ✅ | Full supplemental sheet: 10 visual audio cues, reduced-motion wheel/celebration/shuffle/dice variants, patterned wheel segments, 44px+ inputs |
| No Crypto Elements | ✅ | PASS — the scams here are lovingly analog; not a token in sight |
| Social Media Integration | ✅ | Six screenshot moments identified; selfie spot with props is a designed share loop |

**Shenanigans delivers the rarest thing in Eurobound: a location where losing is the content, the reward, and the punchline. Every asset serves the same beautiful irony — the games are rigged in plain sight, the shills celebrate on cue, the odds are posted in two versions, and the marks keep playing because hope is irrational and Mickey knows it's worth 5 Sovs a spin. When the bros finally walk out with a jester-cap stamp, a paper crown, and the only honest pint in the building, the assets will have told the whole joke without a single line of dialogue: the house always wins, and somehow, so did you.**

**"You've earned the stamp. Not for winning. For understanding what winning actually is."**
