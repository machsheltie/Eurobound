# The Blarney Trap - Complete PNG Asset Requirements

## 📋 Overview
The Blarney Trap is Publandia's primary hub — inn, quest central, save point, Bravado testing ground, and origin of the continent-spanning Brewery Tour — a tourist pub so self-aware that the trap is in the name, the "Est. 1847" is technically true (the building, not the pub concept, which is from 2003), and the Guinness is poured with 119.5 seconds of non-negotiable sincerity. This document specifies every PNG asset needed to render manufactured authenticity with professional precision: 847 shamrocks and counting, exactly two actual antiques, and a welcome that is genuine even when it's transactional.

**Location ID:** `publandia_hub_blarney_trap_01`
**Theme:** Manufactured authenticity as a craft — the tourist trap that admits it, satirizing the "Irish Experience" package while still delivering it
**Zone:** The Craic Tax (tourist central), Publandia
**Hours:** 10:30 AM - 2:30 AM (Irish licensing laws, stretched)
**Primary Function:** Primary Hub / Inn / Quest Central / Save-Recovery Point / Bravado Testing Ground (pint-offs, toast challenges) / Brewery Tour Origin

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Pub Green | #228B22 | Facade, signage accents, shamrocks (all 847) |
| Guinness Gold | #FFD700 | Celtic lettering, brass fittings, pint highlights |
| Dark Wood | #3E2723 | Mahogany bar, floors, snug paneling |
| Cream Walls | #FFF8DC | Interior walls, ceiling, foam dome |
| Guinness Black | #1A1110 | The pint itself, night windows |
| Amber Glow | #FFBF00 | Fireplace light, candles, warm window spill |
| Emerald Ink | #046307 | Passport stamp, Celtic knotwork detail |
| Rain Slate | #708090 | Wet cobblestones, rain-on-window streaks |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/the_blarney_trap/
├── environment/
│   ├── blarney_trap_exterior.png
│   ├── main_bar_interior.png
│   ├── snug_backroom_questboard.png
│   └── guest_rooms_suites.png
├── npcs/
│   ├── seamus_and_staff.png
│   └── regulars_and_crowd.png
├── objects/
│   └── consumables_brewery_tour.png
├── ui/
│   └── hub_ui_effects.png
└── accessibility/
    └── blarney_trap_accessibility.png
```

---

## 🏠 Sprite Sheet 1: Exterior & Facade Signage
**File:** `blarney_trap_exterior.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** Pub Green #228B22, Guinness Gold #FFD700, Rain Slate #708090, Amber Glow #FFBF00

### Building & Facade:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Georgian Facade (Day) | (0, 0) | 384x384 | Georgian-era building painted VERY green, window boxes, deliberate weathering |
| Georgian Facade (Night) | (384, 0) | 384x384 | Same facade, warm amber glow from every window, trad music practically visible |
| Slate Roof Cap | (768, 0) | 256x64 | Slate roofline with chimney pots |
| Main Sign "THE BLARNEY TRAP" | (768, 64) | 256x64 | Gold Celtic lettering, knotwork border — the trap, named |
| "Est. 1847" Plaque | (768, 128) | 128x64 | Building from 1847; pub concept from 2003. Both true, one implied |
| "CÉAD MÍLE FÁILTE" Window Decal | (896, 128) | 128x64 | A Hundred Thousand Welcomes, gold on glass |
| "Craic Tax Pricing Applies" Fine Print | (768, 192) | 128x32 | The honest addition, tiny |
| Vintage Guinness Hanging Sign | (896, 192) | 128x96 | Reproduction (a good one), swings on bracket |
| Sidewalk Board | (768, 224) | 96x160 | "Today's Special: The Craic (It's Always The Craic)" |
| Window Box Shamrocks | (864, 288) | 160x96 | Overflowing planter — shamrock count begins before the door |

### Street Level & Entry:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Green Door (Closed) | (0, 384) | 96x128 | Weathered green door, brass fittings |
| Green Door (Open) | (96, 384) | 96x128 | Warmth, noise, and Craic Tax pricing beyond |
| Trap-Spring Welcome Mat | (192, 384) | 96x64 | "FÁILTE" mat — the visual anchor for the trap-spring entry stinger |
| Cobblestone Tile | (192, 448) | 96x64 | Dry cobblestone, tileable |
| Tourist Photographer A | (288, 384) | 96x128 | Phone raised at the facade, mid-photo |
| Tourist Photographer B | (384, 384) | 96x128 | Second angle, selfie variant |
| Rival Pub Facade Slice | (480, 384) | 192x128 | Neighboring identical pub, also claiming authenticity |
| Streetlamp | (672, 384) | 64x128 | Amber lamp, doubles as night light source |
| Rain-Slick Cobblestone Tile | (736, 384) | 96x128 | Wet variant, reflective |
| Exterior Window (Rain-Streaked) | (832, 384) | 96x128 | Frequent-rain state for the facade windows |
| Shamrock Bunting Strip | (928, 384) | 96x128 | Tileable bunting for the eaves |

### Technical Notes:
- Day/night facades swap via crossfade at 18:00 in-game; streetlamp and window glow layers activate with night state
- Trap-Spring Welcome Mat compresses 2px on player entry (syncs with the "trap" spring stinger)
- Rival Pub Facade Slice tiles horizontally to build the rest of The Craic Tax street

---

## 🍺 Sprite Sheet 2: Main Bar Interior
**File:** `main_bar_interior.png`
**Dimensions:** 2048x1024 pixels
**Color Palette:** Dark Wood #3E2723, Guinness Gold #FFD700, Cream Walls #FFF8DC, Amber Glow #FFBF00

### Room Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Main Room Backdrop | (0, 0) | 1024x512 | Full pub interior composite — cream walls, dark wood, amber light |
| Wood Floor Tile | (0, 512) | 256x256 | Worn dark-wood floor, tileable |
| Wall Panel Tile | (256, 512) | 256x256 | Mahogany wainscoting, tileable |
| Interior Window (Rain-Streaked) | (512, 512) | 192x256 | The Craic Tax outside, rain running down the glass |
| Door to The Snug | (704, 512) | 96x256 | Etched glass, "regulars only" energy |
| Door to The Backroom | (800, 512) | 96x256 | Unmarked, locked until proven |
| Staircase Doorway | (896, 512) | 128x256 | To the rooms; "MIND THE CREAK" sign included |

### The Bar (Mahogany & Brass):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mahogany Bar Counter | (1024, 0) | 768x192 | Dark mahogany, brass rail, decades of elbow polish |
| Tap Bank "Pipe Organ" (14 Taps) | (1024, 192) | 448x160 | Fourteen taps arranged like a pipe organ: Smithwick's, Harp, Beamish, Murphy's, craft rotators |
| Guinness Dedicated Tap 1 | (1472, 192) | 64x160 | First of three dedicated Guinness taps, harp badge |
| Guinness Dedicated Tap 2 | (1536, 192) | 64x160 | Second dedicated tap, mid-pour handle state |
| Guinness Dedicated Tap 3 | (1600, 192) | 64x160 | Third dedicated tap — demand justifies all three |
| Vintage Till | (1664, 192) | 128x160 | Ancient register only Seamus understands; POS terminal bolted alongside |
| Whiskey Wall | (1792, 0) | 256x352 | Jameson (multiple expressions), Powers, Redbreast, Midleton, tourist traps on the top shelf |
| Antique Mirror | (1792, 352) | 128x160 | One of exactly two actual antiques in the building |
| Antique Chair | (1920, 352) | 128x160 | The other one |
| Snack & Glassware Shelf | (1024, 352) | 448x160 | Tayto crisps (cheese & onion, obviously), pork scratchings, toastie press, stacked pint glasses |
| Pint Settling Station | (1472, 352) | 192x160 | Behind-bar shelf where Guinness pints wait out their 119.5 seconds |
| Bottle Opener Keychain Display | (1664, 352) | 128x160 | Seamus's collection case — the brass shamrock opener on velvet, quest starter in plain sight |

### The Decor Audit (All 847-Adjacent):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| GAA Jerseys (Framed Pair) | (1024, 512) | 192x128 | County colors, framed with excessive reverence |
| Hurling Sticks x3 (Signed) | (1216, 512) | 192x128 | Signatures questionable, mounting confident |
| "May the Road Rise" Plaques x4 | (1408, 512) | 256x64 | Mass-produced, hung sincerely |
| Irish Blessing Plaque Close-Up | (1408, 576) | 256x64 | Readable version for examine interactions |
| Vintage Guinness Ad Grid (14 Repros) | (1664, 512) | 384x128 | Fourteen reproduction ads in a 7x2 grid — good reproductions |
| Regulars Photo Wall (52 Photos) | (1024, 640) | 512x256 | Actual regulars, all photographed since 2003 |
| Shamrock Decor Cluster A | (1536, 640) | 256x128 | A representative sample of the 847 shamrock items |
| Shamrock Decor Cluster B | (1536, 768) | 256x128 | Counting ongoing |
| "CÉAD MÍLE FÁILTE" Interior Banner | (1792, 640) | 256x64 | Above the bar, gold on green |
| Territorial High Stools x4 | (1792, 704) | 256x128 | Four 64x128 stools, one visibly worn to a specific shape |
| Communal Low Table | (1792, 832) | 256x96 | Low table, ring stains as texture |
| Corner Snug Bench (Main Room View) | (1024, 896) | 256x128 | Coveted corner seating seen from the floor |
| LED Candle (Lit) | (1280, 896) | 64x64 | Looks like fire; is fire-code compliance |
| LED Candle (Off) | (1344, 896) | 64x64 | Daytime state |
| Bar Tip Jar (Empty) | (1408, 896) | 64x64 | Hopeful |
| Bar Tip Jar (Coins) | (1472, 896) | 64x64 | Realistic |
| Bar Tip Jar (Notes) | (1536, 896) | 64x64 | A good trad night happened |
| Chalk Menu Board | (1600, 896) | 192x128 | "THE CRAIC — 8 Sovs" in careful chalk Celtic lettering |
| Bar Mats & Spill Decals | (1792, 928) | 256x96 | Branded mats, honest spills |
| Spilled Pint Puddle Decal | (1280, 960) | 128x64 | Floor hazard, comedy prop |
| Coaster Set | (1408, 960) | 128x64 | Four designs, all shamrocks |

### The Fireplace & Music Corner:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gas Fireplace ("Turf-Burning") | (0, 768) | 256x256 | Gas-powered, engineered to look turf-burning, always flickering |
| Fireplace Mantel (Shamrock Overload) | (256, 768) | 256x256 | Mantel carrying a significant fraction of the 847; designated selfie spot |
| Music Corner Stage | (512, 768) | 320x256 | Small trad stage, well-worn boards, mic that nobody uses |
| Musicians' Tip Jar | (832, 768) | 64x64 | Labeled "MUSICIANS' PENSION FUND" |
| Session Stool (Worn) | (832, 832) | 64x96 | Shaped by decades of reels |
| Bodhrán at Rest | (832, 928) | 64x96 | Leaning on the stage between sessions |
| Fireplace Glow Overlay | (896, 768) | 128x256 | Warm radius overlay, additive blend |

### Technical Notes:
- Backdrop renders as one layer; bar, decor, and fireplace composite over it to keep draw calls inside the hub budget (18 max)
- The three Guinness taps get individual sprites because the pour ritual camera pushes in on them — they must survive scrutiny
- Regulars Photo Wall is one static texture; individual photos are NOT separately animated (52 draw calls would be madness)
- Shamrock clusters tile to imply 847 without rendering 847

---

## 🤫 Sprite Sheet 3: The Snug, Backroom & Quest Board
**File:** `snug_backroom_questboard.png`
**Dimensions:** 1024x1024 pixels

### The Snug (Regulars Only):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Snug Interior | (0, 0) | 512x384 | Traditional enclosed booth seating — where locals actually drink and real information is traded |
| Snug Privacy Partition | (512, 0) | 256x384 | Etched-glass and dark-wood screen between locals and tourists |
| Snug Table with Locals' Pints | (768, 0) | 256x192 | Half-finished pints, no phones in sight |
| "Regulars Only" Brass Plate | (768, 192) | 128x64 | Polished daily; means it |
| Snug Wall Lamp | (896, 192) | 128x64 | Low amber light for quiet dealing |
| Craic Broker's Court Corner | (768, 256) | 256x128 | The Broker's habitual seat — papers, pints, possibilities |

### The Backroom (Unlockable):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Backroom Interior | (0, 384) | 512x384 | Where staff actually relax and unlicensed operations occur |
| Poker Table (Questionable Legitimacy) | (512, 384) | 256x192 | Felt worn, chips uncounted, licensing unexamined |
| Trivia-Fight Setup | (768, 384) | 256x192 | Podium and folding chairs for fights disguised as pub trivia nights |
| Staff Dartboard & Rota | (512, 576) | 128x192 | Shift schedule with darts in it |
| Unlicensed Till #2 | (640, 576) | 128x192 | The register that doesn't officially exist |
| Backroom Door (Inside, Deadbolts) | (768, 576) | 128x192 | Three locks, all decorative except the middle one |
| Staff Couch (Actually Relaxing) | (896, 576) | 128x192 | Sagging, beloved, off-limits to customers forever |

### The Quest Board (Craic Broker's Territory):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rumor Board (Full) | (0, 768) | 384x256 | Corkboard in the main bar — quests, rumors, local knowledge |
| Quest Notice Cards x6 | (384, 768) | 384x128 | Six 128x64 cards: yeast situations, rival trio sightings, work/adventure/trouble |
| Pushpins & String | (384, 896) | 128x64 | Red pins, optional conspiracy string |
| "CRAIC WANTED" Header Banner | (512, 896) | 256x64 | Board title in stencil Celtic |
| Poker Chips & Cards Props | (384, 960) | 192x64 | Backroom scatter props |
| Trivia Night Scoreboard | (576, 960) | 192x64 | Chalk tally: "QUESTIONS: 12 — FIGHTS: 3" |
| Rumor Board (Locked State) | (768, 768) | 256x256 | Pre-Pub-Regular version — half the notices face-down |

### Technical Notes:
- Snug and Backroom are gated scenes: Snug requires "Pub Regular" status or invitation; Backroom requires "Pub Regular" or quest state
- Quest Notice Cards swap texture regions based on active quest flags — board is a live UI surface, not set dressing
- Locked board state renders until `pub_regular == true`, then crossfades to the full board (0.5s)

---

## 🛏️ Sprite Sheet 4: Guest Rooms & Suites
**File:** `guest_rooms_suites.png`
**Dimensions:** 1024x1024 pixels

### Standard Accommodation (First Floor):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shared Dorm | (0, 0) | 384x256 | 35 Sovs, 50% restoration, snoring NPCs included, "Embarrassed" risk visible in bunk spacing |
| Street-Facing Single | (384, 0) | 320x256 | 55 Sovs, 70% restoration — loud but atmospheric, craic audible until 3 AM |
| Courtyard Single | (704, 0) | 320x256 | 70 Sovs, 85% restoration — actually sleepable, less craic |
| Street-Facing Double | (0, 256) | 384x256 | 75 Sovs, bros can share, shamrock density: high |
| Courtyard Double | (384, 256) | 320x256 | 90 Sovs, better value, shamrock density: merciful |
| Shared Bathroom + Queue | (704, 256) | 320x256 | Character building; queue-forming NPC marks on the floor |

### Premium Suites (Second Floor):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| The Yeats Suite | (0, 512) | 512x256 | Quotes stenciled on every surface — walls, mirror, headboard, ceiling ("Tread softly...") |
| The Joyce Suite | (512, 512) | 512x256 | Deliberately confusing layout: door where the wardrobe should be, wardrobe where the bathroom should be |
| The Wilde Suite | (0, 768) | 384x256 | Velvet everything — chaise, curtains, headboard; grants "Wit Sharpened" |
| The Behan Suite | (384, 768) | 320x256 | Minibar pre-stocked and prominently lit, no judgment rendered |

### Circulation:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Creaky Staircase | (704, 768) | 160x256 | Every step announces all movement — security feature or flaw, unresolved |
| Creak-Indicator Floorboards | (864, 768) | 160x128 | Highlighted boards, 3 creak intensities for the ascent animation |
| Room Door + Number Plaques | (864, 896) | 160x128 | Door with swappable number/suite plaques, shamrock-rated |

### Technical Notes:
- Rooms load on demand at check-in; only the booked room texture region streams in
- Restoration tier is data-driven from the room ID — art carries the tier visually (bed quality, shamrock count inversely proportional to price)
- Suite signature gags must read in one screenshot each: quotes, confusion, velvet, minibar
- Creaky staircase pairs each highlighted board with a creak audio event and a visual creak line (see Accessibility)

---

## 👨‍🍳 Sprite Sheet 5: Seamus O'Brien & Staff
**File:** `seamus_and_staff.png`
**Dimensions:** 1024x1024 pixels

### Seamus States (96x128 each):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Welcome (Arms Wide) | (0, 0) | 96x128 | "Céad míle fáilte!" — professional warmth at full beam |
| Pour Stage One | (96, 0) | 96x128 | Glass at 45°, first pull on the dedicated tap |
| The Wait (Surge Watch) | (192, 0) | 96x128 | Arms folded, watching the surge — 119.5 seconds of patience |
| Pour Stage Two | (288, 0) | 96x128 | The top-off, total focus |
| Perfect Dome Presentation | (384, 0) | 96x128 | Pint extended, dome proud: "There she is" |
| Storytelling | (480, 0) | 96x128 | Philosophy mode, towel over shoulder |
| The Wink | (576, 0) | 96x128 | "That's the trap. *winks*" — the marketing frame |
| Till Operation | (672, 0) | 96x128 | The only living master of the vintage register |
| Behind-Bar Idle | (768, 0) | 96x128 | Polishing a glass that is already clean |
| Genuine Mode (After 11 PM) | (864, 0) | 96x128 | Softer posture — the real Publandia hours |
| Opener Pitch | (960, 0) | 64x128 | Holding up the brass shamrock opener: "It's not just for show" |

### Guinness Pour Ritual Frames (64x128 each):
| Frame | Position | Size | Description |
|-------|----------|------|-------------|
| Pour F1 (Glass Tilt) | (0, 128) | 64x128 | 45° angle established |
| Pour F2 (First Pull) | (64, 128) | 64x128 | Tap engaged |
| Pour F3 (Three-Quarter Fill) | (128, 128) | 64x128 | Stop point, non-negotiable |
| Pour F4 (Set to Settle) | (192, 128) | 64x128 | Pint placed on settling station |
| Pour F5 (The Watch) | (256, 128) | 64x128 | Seamus and pint, waiting together |
| Pour F6 (Second Pull) | (320, 128) | 64x128 | The top-off begins |
| Pour F7 (Dome Forming) | (384, 128) | 64x128 | Cream rising just proud of the rim |
| Pour F8 (Presentation) | (448, 128) | 64x128 | Slide to the customer |

### Seamus Dialogue Portraits (96x96 each):
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Portrait Welcome | (512, 128) | 96x96 | Red-faced, permanent welcoming expression |
| Portrait Wink | (608, 128) | 96x96 | Mid-wink, for trap disclosures |
| Portrait Philosophy | (704, 128) | 96x96 | "Manufactured authenticity is still authenticity. Fight me on that." |
| Portrait Genuine | (800, 128) | 96x96 | After-11 sincerity |
| Portrait Pour Focus | (896, 128) | 96x96 | Eyes on the surge, do not speak to him |

### Siobhan & Declan (96x128 states, 96x96 portraits):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Siobhan Idle (Pouring) | (0, 256) | 96x128 | Evening shift, efficient movements, seen everything |
| Siobhan Referee | (96, 256) | 96x128 | Pint-off referee stance, arm raised |
| Siobhan Sarcastic Lean | (192, 256) | 96x128 | "Revolutionary choice. Coming up." |
| Siobhan Genuine Kindness | (288, 256) | 96x128 | Beneath the sarcasm, briefly visible |
| Siobhan Portrait | (384, 256) | 96x96 | Dialogue box version |
| Declan Door Watch | (480, 256) | 96x128 | Night shift, former rugby build, assessing |
| Declan Arms Crossed | (576, 256) | 96x128 | Gatekeeper to real Publandia |
| Declan Closing Point | (672, 256) | 96x128 | "You don't have to go home, but you can't stay here" |
| Declan Backroom Nod | (768, 256) | 96x128 | The almost-imperceptible approval |
| Declan Portrait | (864, 256) | 96x96 | Intimidating but kind |

### Aoife & Detail Sprites:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Aoife Tray Rush | (0, 384) | 96x128 | Perpetually moving, hospitality degree in active use |
| Aoife Key Handoff | (96, 384) | 96x128 | "Your room's ready! Street-facing, so you'll hear the craic until 3 AM. That's a feature." |
| Aoife Weaponized Cheer | (192, 384) | 96x128 | Brightness deployed against hangovers |
| Aoife Full Irish Delivery | (288, 384) | 96x128 | Morning recovery specialist at work |
| Aoife Portrait | (384, 384) | 96x96 | Dialogue box version |
| Seamus Hands on Tap (Detail) | (480, 384) | 128x64 | Close-up for the pour cutaway |
| Perfect Dome Macro | (608, 384) | 96x128 | The pint itself, dome in glory, for the presentation beat |
| Seamus Face Close-Up | (704, 384) | 96x96 | Red face from proximity to business |
| Till Fingers Detail | (800, 384) | 96x64 | The secret handshake with the register |
| Waistcoat Texture Swatch | (896, 384) | 128x64 | Publican's waistcoat weave for zoomed frames |

### Walk Cycles (96x128 per frame):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Seamus Walk F1-F4 | (0, 512) | 384x128 | Four frames at (0,512),(96,512),(192,512),(288,512) — unhurried publican stride |
| Siobhan Walk F1-F2 | (384, 512) | 192x128 | Two frames — efficiency in motion |
| Declan Walk F1-F2 | (576, 512) | 192x128 | Two frames — slow, inevitable |
| Aoife Walk F1-F2 | (768, 512) | 192x128 | Two frames — near-jog service pace |

### Expression Grid (64x64 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Seamus Expressions x5 | (0, 640) | 320x64 | Welcome / Wink / Pride / Philosophy / Genuine |
| Siobhan Expressions x3 | (320, 640) | 192x64 | Deadpan / Amused / Done |
| Declan Expressions x3 | (512, 640) | 192x64 | Assessing / Approving / "No" |
| Aoife Expressions x3 | (704, 640) | 192x64 | Bright / Brighter / Concerned-but-bright |
| Staff Collective Glance | (896, 640) | 128x64 | The shared "tourists" look, wordless |

### Storytelling & Extras:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Storytelling Gesture F1-F4 | (0, 704) | 384x128 | Four 96x128 frames — the philosophy monologue arc |
| "Trust the Process" Pose | (384, 704) | 96x128 | Palm raised at an impatient tourist |
| After-Hours Staff Group | (480, 704) | 288x128 | All four, post-close, actually relaxed |
| Surge-Watch Profile | (768, 704) | 128x128 | Seamus in profile against the settling pint |
| Declan Last Orders | (896, 704) | 96x128 | Bell in hand, argument pre-declined |
| Toast Hands (Raised Pints) | (0, 832) | 128x64 | For toast-challenge cutaways |
| Bar Towel | (128, 832) | 64x64 | Over-shoulder prop |
| Pour Pocket Watch | (192, 832) | 64x64 | Seamus's timer gag — it reads 119.5 |
| Names Notebook | (256, 832) | 64x64 | How everyone becomes a "regular" |
| Free Pint Slide | (320, 832) | 128x64 | "First pint's on me when you earn that stamp" |

### Technical Notes:
- Rows below y=896 are reserved padding for future staff states — do not pack new sheets into this region without updating this spec
- Pour ritual frames F1-F8 are keyframes; the 119.5-second wait holds on F5 with the settle particle overlay (Sheet 8) doing the work
- Portraits export at 2x for dialogue UI crispness on high-DPI phones

---

## 👥 Sprite Sheet 6: Regulars & Crowd
**File:** `regulars_and_crowd.png`
**Dimensions:** 1024x512 pixels

### The Craic Broker & Old Fergal:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Craic Broker Holding Court | (0, 0) | 96x128 | Age unclear, always present, probably lives here |
| Craic Broker Leaning Deal | (96, 0) | 96x128 | "Work? Adventure? Trouble? I've got all three." |
| Craic Broker Quest Handoff | (192, 0) | 96x128 | Paper sliding across the snug table |
| Craic Broker Portrait | (288, 0) | 96x96 | Dialogue box version |
| Old Fergal on His Stool | (384, 0) | 96x128 | Same stool, 40 years, end of the bar, always |
| Old Fergal Storytelling | (480, 0) | 96x128 | Arms wide enough for the exaggeration |
| Old Fergal Pint Request Lean | (576, 0) | 96x128 | "Buy an old man a pint, and I'll tell you about the time I..." |
| Old Fergal Asleep Upright | (672, 0) | 96x128 | A skill, not an accident |
| Old Fergal Portrait | (768, 0) | 96x96 | Unreliable historian face |
| Old Fergal's Stool (Empty) | (864, 0) | 64x128 | Worn precisely to his shape — never sat in by anyone else |
| Real Regular (Post-11 PM) | (928, 0) | 96x128 | Arrives after the tourists sleep; never posts about it online |

### Tourist Crowd Variants:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tourist Crowd Block A | (0, 128) | 256x128 | Four tourists: pointing, photographing, mispronouncing "Sláinte" |
| Tourist Crowd Block B | (256, 128) | 256x128 | Four more: bucket hats, novelty shamrock accessories |
| Crowd Sway Frame A | (512, 128) | 256x128 | Sway-left composite for ambient motion |
| Crowd Sway Frame B | (768, 128) | 256x128 | Sway-right composite — two frames, whole atmosphere |

### Trad Musicians & Ambience:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fiddler | (0, 256) | 96x128 | Session anchor, eyes closed |
| Bodhrán Player | (96, 256) | 96x128 | Keeping time nobody else follows |
| Tin Whistle Player | (192, 256) | 96x128 | Mid-reel |
| Guitarist | (288, 256) | 96x128 | The one tourist-adjacent instrument, tolerated |
| Musicians Playing Frames (Alt Set) | (384, 256) | 384x128 | Second pose per musician (4 at 96x128) for the session loop |
| Between-Tunes Pints | (768, 256) | 128x128 | The sacred pause — instruments down, pints up |
| Hen Party (Distant) | (896, 256) | 128x128 | Silhouettes through the window; shrieks implied |

### Contest & Reaction Sprites:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pint-Off Challenger x2 States | (0, 384) | 192x128 | Confident and mid-defeat (two 96x128 poses) |
| Crowd Cheer Frames x2 | (192, 384) | 256x128 | Pints-up eruption, two frames |
| Crowd Wince | (448, 384) | 128x128 | Collective reaction to a missed beat |
| Photo-Taking Tourist | (576, 384) | 96x128 | Flash raised at the fireplace |
| Scuttered Tourist | (672, 384) | 96x128 | "Absolutely Scuttered" NPC state, gently listing |
| Bathroom Queue Pair | (768, 384) | 128x128 | Two NPCs, character being built |
| Rival Trio Silhouettes | (896, 384) | 128x128 | Cameo sprites for the documentation side quest |

### Technical Notes:
- Crowd renders as composite blocks, never individuals — mobile budget demands the simplified crowd (profile requirement)
- Crowd Sway A/B alternates at 3.2s; Low LOD holds Frame A permanently
- Hen Party stays behind window glass at all times; she is atmosphere, not an encounter

---

## 🎒 Sprite Sheet 7: Consumables & Brewery Tour Items
**File:** `consumables_brewery_tour.png`
**Dimensions:** 1024x512 pixels

### The Brewery Passport (Large Layouts):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Passport Open Spread | (0, 0) | 512x384 | Leather-bound, travel-worn; embossed "The Continental Beer Trail" across the gutter |
| Publandia Stamp Page | (512, 0) | 256x384 | Four stamp slots: The Blarney Trap, The Stoutworks, Trinity of Pints, and a locked fourth slot (faded outline, "Locked"); progress bar "X/4 Publandia — Legendary Hangover" at the base |
| Empty City Page Template | (768, 0) | 256x384 | Reusable page frame with 4 empty slots and banner text area, for every other city |

### Pub Menu & Consumables:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Guinness Settling Stage 1 | (0, 384) | 32x64 | Chaos in the glass — the surge begins |
| Guinness Settling Stage 2 | (32, 384) | 32x64 | Cascade running down the sides |
| Guinness Settling Stage 3 | (64, 384) | 32x64 | Separation — black rising, cream forming |
| Guinness Settling Stage 4 | (96, 384) | 32x64 | Nearly still, dome pending |
| Guinness Perfect Dome | (128, 384) | 32x64 | The finished pint. Worth every one of the 119.5 seconds |
| Smithwick's Pint | (160, 384) | 32x64 | The locals' alternative, Bradley's order |
| Whiskey (Standard) | (192, 384) | 32x48 | Jameson pour, +Bravado temporarily |
| Whiskey (Premium) | (224, 384) | 32x48 | Redbreast-tier, impresses the staff |
| Irish Coffee | (256, 384) | 32x64 | Caffeine and alcohol achieving balance |
| Sweet Surrender (Pint) | (288, 384) | 32x64 | The house stout, poured — chocolate and coffee notes implied in the head |
| Sweet Surrender (Bottle) | (320, 384) | 32x64 | Contract-brewed by Stoutworks, labeled by Seamus's grandfather's recipe |
| Tayto Crisps | (352, 384) | 32x32 | Cheese & Onion or nothing |
| Toastie | (384, 384) | 48x32 | Pub food perfection, absorbs significant alcohol |
| Full Irish | (432, 384) | 64x48 | Cures The Fear. Morning recovery essential |
| Room Key (Basic) | (496, 384) | 32x32 | Standard room, shamrock fob |
| Room Key (Premium) | (528, 384) | 32x32 | Suite access, gold shamrock fob |
| Shamrock Decor Unit | (560, 384) | 32x32 | One of 847. Counting ongoing |
| Bottle Opener Keychain | (592, 384) | 64x64 | Brass opener shaped like a shamrock, "The Blarney Trap" engraved — key to every brewery worth visiting in Europe |
| Passport Book (Closed) | (656, 384) | 64x64 | Inventory/menu icon for the Brewery Passport |
| Blarney Trap Stamp | (720, 384) | 64x64 | Celtic knot circular border, harp silhouette center, "Est. 1847 — Publandia," deep emerald ink |
| Empty Stamp Slot | (784, 384) | 64x64 | Faded outline of a potential stamp |
| Locked Fourth Slot | (848, 384) | 64x64 | Faded outline with small "Locked" banner — the passport page's fourth Publandia slot |
| Pub Regular Badge | (912, 384) | 64x64 | Status achieved: staff remember your name |
| Selfie Spot Indicator | (976, 384) | 48x48 | Camera glyph marking the shamrock-fireplace photo op |

### Rewards & Trackers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Continental Progress Tracker | (0, 448) | 256x64 | "Continental Beer Master" bar — stamps across all cities |
| Legendary Hangover Consumable | (256, 448) | 64x64 | Publandia city-completion ultimate: +15 all stats for one battle, morning consequences included |
| Stamp Ink Press F1-F3 | (320, 448) | 192x64 | Three 64x64 frames: raise → slam → lift, emerald ink fresh |
| Pork Scratchings | (512, 448) | 32x32 | The other snack, unglamorous, effective |
| Free Pint Voucher | (544, 448) | 64x64 | "First pint's on me" — stamp-earned reward token |
| Sweet Surrender Label Detail | (608, 448) | 128x64 | Zoomed label for the unlock reveal |
| Hair of the Dog Tray | (736, 448) | 96x64 | Aoife's combined morning offering |
| Round Tray (Five Pints) | (832, 448) | 96x64 | The round obligation, rendered in glassware |
| Raised Toast Pint Icon | (928, 448) | 96x64 | Toast challenge success flourish |

### Technical Notes:
- Settling stages 1-4 drive the in-glass ritual animation; the Perfect Dome sprite is a separate hold frame, never blended
- Passport pages are UI textures — text regions stay clear of the 16px page margins for localization overflow
- Stamp appears via the Ink Press frames plus one screen-shake tick (2px, skipped in reduced-motion mode)

---

## 🎮 Sprite Sheet 8: Hub UI & Effects
**File:** `hub_ui_effects.png`
**Dimensions:** 1024x1024 pixels

### Room Selection & Rhythm Game:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Room Selection UI | (0, 0) | 384x512 | Nine-row accommodation picker: price, restoration %, noise level, shamrock-density icons per room |
| Pint-Off Rhythm Interface | (384, 0) | 448x192 | Beat track with pint-raise lane, round counter, opponent panel |
| Beat Marker States x3 | (832, 0) | 192x64 | Three 64x64 states: Perfect / Hit / Miss — shape-coded (circle/square/cross), not color-only |
| Pint-Raise Beat Icons x4 | (832, 64) | 192x64 | Four 48x64 frames of the rising pint on the beat lane |
| Combo Counter Frame | (832, 128) | 96x64 | Streak display, Celtic corner flourishes |
| "Lightweight" Debuff Icon | (928, 128) | 48x48 | Missed-beats consequence |
| "Seasoned Drinker" Buff Icon | (976, 128) | 48x48 | Perfect-rhythm reward |
| No-Audio Pulse Bar | (384, 192) | 448x64 | Full-width visual metronome — pint-off playable with sound off |
| Round Timer | (832, 192) | 192x64 | Escalating-difficulty round indicator |

### Toast Builder:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Toast Builder UI | (384, 256) | 384x192 | Speech-construction panel: slot the lines, raise the glass |
| Toast Line Cards x4 | (768, 256) | 256x128 | Four 128x64 cards: Sincere / Funny / Exaggerated / Inappropriate |
| Toast Result Banners x2 | (768, 384) | 256x64 | Two 128x64 banners: "SLÁINTE!" success / polite-wince failure |
| Toast Confirm Button | (384, 448) | 128x64 | Raise-the-glass commit, 44px+ touch target |
| Free Round Banner | (512, 448) | 256x64 | "THE HOUSE APPROVES" possible-free-round payout |
| Applause Meter | (768, 448) | 256x64 | Crowd approval fill bar |

### Hub Status & Menus:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Quest Board UI | (0, 512) | 320x256 | Available missions panel mirroring the physical rumor board |
| Bravado Meter (Pub) | (320, 512) | 192x64 | Local Bravado tracking with pint-glass fill |
| Craic Status | (512, 512) | 128x64 | Current craic level: Mild → Ninety |
| Round Obligation Tracker | (640, 512) | 192x64 | Whose round it is — the trap's true engine |
| Pub Regular Progress | (832, 512) | 192x64 | Toward status: presence, names, rounds |
| The Fear Icon | (320, 576) | 64x64 | Morning consequence, rendered as a small gray sun |
| Scuttered Meter | (384, 576) | 192x64 | Intoxication track: Sober → Absolutely Scuttered |
| "Craic'd Up" Icon | (576, 576) | 48x48 | +Charisma status, patterned badge |
| "Fair Play" Icon | (624, 576) | 48x48 | Earned respect, striped badge |
| "Absolutely Scuttered" Icon | (672, 576) | 48x48 | Spiral badge, self-explanatory |
| "Contentment" Icon | (720, 576) | 48x48 | Sweet Surrender risk state, dotted badge |
| "Comfortable Trap" Icon | (768, 576) | 48x48 | Bravado-retention buff, knot badge |
| Auto-Save Shamrock Spinner | (816, 576) | 64x64 | Check-in save indicator |
| Room Key Confirm Dialog | (880, 576) | 144x64 | Booking confirmation micro-panel |
| Dialogue Box Frame (Celtic Border) | (320, 640) | 448x128 | Knotwork-bordered dialogue frame for all Trap conversations |
| "Brewery Passport" Menu Tab | (768, 640) | 256x64 | Pause-menu tab art, appears once the book is owned |
| POS Terminal Screen | (768, 704) | 256x64 | The till-side terminal — hosts the hidden NFT Hunt acquisition hotspot |

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fireplace Flicker F1-F4 | (0, 768) | 384x128 | Four 96x128 flame frames for the gas-powered turf illusion |
| Pint-Settle Particle F1-F4 | (384, 768) | 192x64 | Four 48x64 cascade-particle frames (crucial, per spec) |
| Surge Cascade Strip | (384, 832) | 192x64 | In-glass nitrogen cascade overlay for the ritual close-up |
| Dust Beam Overlay | (576, 768) | 224x128 | Dust motes in amber window light |
| Rain-on-Window Overlay F1-F2 | (800, 768) | 224x128 | Two 112x128 streak frames, frequent use |
| Candle Flicker F1-F3 | (0, 896) | 144x64 | Three 48x64 LED-candle frames |
| Glass Clink Sparkle | (144, 896) | 64x64 | Toast-impact glint |
| Till Ring Flash | (208, 896) | 64x64 | Register cha-ching burst |
| Laughter Burst Lines | (272, 896) | 96x64 | Eruption lines radiating from crowd blocks |
| Trap-Spring Entry F1-F3 | (368, 896) | 192x64 | Three 64x64 frames: the doormat "snap" flourish on first entry |
| Stamp Slam Effect | (560, 896) | 96x64 | Ink ring + impact star for passport stamping |
| Scuttered Wobble Overlay | (656, 896) | 176x64 | Screen-edge wobble band for Absolutely Scuttered |
| The Fear Desaturation Strip | (832, 896) | 192x64 | Morning-after LUT gradient |
| Shamrock Particles x4 | (0, 960) | 128x32 | Four 32x32 drifting shamrocks (celebration bursts, reduced count on mobile) |
| Foam Bubbles | (128, 960) | 64x32 | Head-of-pint micro detail |
| Chatter Bubbles | (192, 960) | 96x32 | Multilingual murmur glyphs over crowd blocks |
| Hen Party Shriek Lines | (288, 960) | 96x32 | Distant jagged lines at the window |
| Photo Flash Burst | (384, 960) | 64x32 | Tourist camera flash |
| Rain Drip | (448, 960) | 32x32 | Single window-drip particle |

### Technical Notes:
- All particles run on CPUParticles2D — shamrock burst capped at 12 (reduced from 20 per the profile's shamrock-particle budget)
- No-Audio Pulse Bar is mandatory in every pint-off render pass, not an optional accessibility layer — the mini-game must be winnable in silence
- POS Terminal Screen carries a 3-frame idle shimmer; the NFT Hunt hotspot has no unique animation (it is meant to be found, not advertised)

---

## 🎬 Animation Specifications

### The Two-Stage Guinness Pour Ritual:
- **Duration:** 149.5 seconds total — 15s Stage One pour, 119.5s settle (non-negotiable), 10s Stage Two top-off, 5s presentation
- **Frames:** 8 Seamus keyframes (Pour F1-F8) + 4 in-glass settling stages + surge cascade overlay
- **Pattern:** F1 → F2 → F3 → F4 → hold F5 with settling stages 1→2→3→4 cycling under the cascade overlay → F6 → F7 → F8 → Perfect Dome hold
- **Trigger:** Any Guinness order; ritual is skippable via UI after first viewing but the pint arrives no faster (that is the joke and the point)
- **Purpose:** The location's sincerity anchor — everything else is manufactured; this is not
- **Audio Sync:** Two-stage pour/surge sound spans the pull; nitrogen hiss holds through the wait; soft "settle" chime at 119.5s exactly
- **Mobile Optimization:** Low LOD drops the cascade overlay and cycles two settling stages instead of four; timer stays frame-accurate

### Pint-Off Rhythm Beats:
- **Duration:** 30-90 seconds per round, tempo rising 100→140 BPM across rounds
- **Frames:** 4 pint-raise beat icons + 3 beat marker states + 2 crowd cheer frames
- **Pattern:** Beat icons scroll the lane → marker resolves Perfect/Hit/Miss per tap → crowd cheer or wince composite fires on streaks/breaks
- **Trigger:** Player challenges or is challenged by an NPC
- **Purpose:** Bravado testing ground core loop; NPCs remember performance and it feeds Pub Regular progress
- **Audio Sync:** Beats lock to the trad track's downbeat; crowd reaction stingers on streak thresholds
- **Mobile Optimization:** No-Audio Pulse Bar always renders; Low LOD replaces crowd reaction frames with a static cheer banner

### Fireplace Flicker:
- **Duration:** 0.8 seconds loop
- **Frames:** 4
- **Pattern:** F1 → F2 → F3 → F4 → loop, with ±10% random frame-time jitter so the gas fire never looks like a GIF
- **Trigger:** Constant (the fireplace is ALWAYS flickering — profile canon)
- **Purpose:** The warm heart of the manufactured authenticity; selfie spot beacon
- **Audio Sync:** Low gas-flame loop, volume tied to camera distance
- **Mobile Optimization:** Static fireplace option (accessibility sheet frame) replaces the loop entirely on Low LOD and in reduced-motion mode

### Trad Session:
- **Duration:** 2.4 seconds loop per musician, phase-offset per player
- **Frames:** 2 per musician (base + alt set), 8 total
- **Pattern:** Base ↔ alt alternation, each musician offset 0.6s so the session breathes
- **Trigger:** Evenings (live session); afternoons hold the between-tunes pose with recorded trad
- **Purpose:** The music IS live — one of the three true things in the building
- **Audio Sync:** Frame alternation locks to the reel's beat; between-tunes pose syncs to track gaps
- **Mobile Optimization:** Static music session option (profile requirement): all four musicians hold base pose, audio continues

### Crowd Sway:
- **Duration:** 3.2 seconds full cycle
- **Frames:** 2 composite blocks (Sway A / Sway B)
- **Pattern:** A → B → A crossfade, amplitude increasing slightly after 22:00 in-game
- **Trigger:** Constant while crowd blocks are on screen
- **Purpose:** A living pub without per-NPC animation cost
- **Audio Sync:** Sway period loosely matches the session tempo; no hard lock
- **Mobile Optimization:** Simplified crowd (profile requirement): Low LOD holds Frame A; steady-crowd accessibility variant available at all LODs

### Toast Delivery:
- **Duration:** 4 seconds
- **Frames:** Toast hands raise (2) → result banner (1) → applause meter fill (continuous)
- **Pattern:** Line cards lock → hands raise → banner resolves success/fail → meter settles
- **Trigger:** Toast speech challenge commit
- **Purpose:** Words worked (or didn't); either way, everyone still drinks
- **Audio Sync:** Glass clink sparkle on the raise; laughter eruption or polite murmur on the banner
- **Mobile Optimization:** None needed (UI-driven, cheap)

### Rain on Window:
- **Duration:** Continuous, 1.6s streak cycle
- **Frames:** 2 overlay frames + drip particle
- **Pattern:** F1 ↔ F2 alternation with 4-6 drip particles per window
- **Trigger:** Weather state "rain" (frequent — this is Publandia)
- **Purpose:** Cozy-interior contrast; the reason nobody leaves
- **Audio Sync:** Rain-on-glass loop tied to overlay visibility
- **Mobile Optimization:** Static rain texture replaces animated overlay on Low LOD

### Trap-Spring Entry:
- **Duration:** 0.6 seconds, one-shot
- **Frames:** 3
- **Pattern:** Mat compress → snap flourish → settle
- **Trigger:** First entry per session (and first-ever entry for the achievement "Trapped")
- **Purpose:** The name is the disclosure; the spring sound is the punchline
- **Audio Sync:** "Trap" spring stinger exactly on F2
- **Mobile Optimization:** None needed

### Creaky Staircase Ascent:
- **Duration:** Per-step, 0.4s each
- **Frames:** 3 creak-intensity board highlights
- **Pattern:** Board highlights fire under each footstep, intensity randomized between the 3 levels
- **Trigger:** Any character on the staircase
- **Purpose:** Security feature or flaw — every guest movement is broadcast to the whole pub
- **Audio Sync:** Creak sample pitch matches highlight intensity, per step
- **Mobile Optimization:** Highlight-only (no audio-reactive scaling) on Low LOD

### Passport Stamp Slam:
- **Duration:** 1.2 seconds, one-shot
- **Frames:** 3 ink-press frames + stamp slam effect
- **Pattern:** Raise → slam (screen tick, 2px) → lift revealing the Celtic-knot harp stamp in wet emerald ink
- **Trigger:** Stamp acquisition conditions met (Pint-Off win / successful toast / Pub Regular, with Bottle Opener Keychain in inventory)
- **Purpose:** The Brewery Tour's signature feedback — this moment sells the whole continental sidequest
- **Audio Sync:** Thunk on slam; short trad flourish on reveal
- **Mobile Optimization:** Screen tick skipped in reduced-motion mode; frames unchanged

---

## ♿ Accessibility Sprite Requirements
**File:** `blarney_trap_accessibility.png` (supplemental sheet — delivered alongside the 8 base files, not counted in their total)
**Dimensions:** 512x384 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Room Selection, Bold | (0, 0) | 128x96 | Thick-bordered picker with enlarged price/restoration rows |
| Pint-Off Beat Track, High Contrast | (128, 0) | 192x64 | White-on-black lane with shape-coded beats (circle=tap, diamond=hold) — fully playable without audio alongside the No-Audio Pulse Bar |
| Toast Builder, Bold | (320, 0) | 96x96 | Heavy-outline line cards with enlarged text zones |
| Quest Board Hotspot Outline | (416, 0) | 96x96 | White outline + enlarged "CRAIC WANTED" header for the examine hotspot |
| Bar Interaction Hotspots Outline | (128, 64) | 192x64 | Outlined tap bank, opener display, and till/POS hotspots in one strip |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fireplace, Static | (0, 128) | 96x96 | Single warm-glow frame — the always-flickering fire, no longer flickering |
| Crowd, Steady | (96, 128) | 128x96 | Non-swaying crowd composite replacing the A/B cycle |
| Trad Session, Static | (224, 128) | 128x96 | Musicians hold base pose, music unaffected |
| Rain, Static Overlay | (352, 128) | 96x96 | Fixed streak texture replacing animated rain and drips |
| Scuttered, No-Wobble | (448, 128) | 64x96 | Fixed vignette replacing the wobble overlay; status still legible |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Two-Stage Pour Cue | (0, 224) | 64x64 | Progress ring with 119.5s countdown and surge icon — the pour/surge sound made visible, stage transitions marked |
| Trad Music Notes | (64, 224) | 48x48 | Note bubbles pulsing from the music corner while the session plays |
| Glass Clink Spark | (112, 224) | 48x48 | Clink glyph on every toast and pint touch |
| Till Ring "SOVS" Flash | (160, 224) | 48x48 | Till burst on every transaction with the word `SOVS` lettered inside the ring — **the symbol is the word; no currency mark exists.** 48x48 holds four caps at ~10px. (Craic Tax pricing, visualized.) |
| Laughter Eruption Burst | (208, 224) | 48x48 | "HA!" radiating lines when the crowd erupts |
| Rain-on-Window Indicator | (256, 224) | 48x48 | Streak glyph in the window corner while rain audio plays |
| Tourist Photo Flash Frame | (304, 224) | 48x48 | Camera-frame flash replacing the photo shutter sound |
| Trap-Spring "SNAP!" Glyph | (352, 224) | 48x48 | Spring burst on entry — the satirical stinger lands visually |
| Pint-Off Beat Flash | (400, 224) | 48x48 | Screen-edge pulse per beat, paired with the pulse bar for silent play |
| Last Orders Bell Glyph | (448, 224) | 48x48 | Bell burst when Declan calls time |

### Colorblind Considerations:
- Beat markers resolve by shape (circle/square/cross), never by color alone — the pint-off must be judged shape-first
- Status effect badges (Craic'd Up / Fair Play / Scuttered / Contentment / Comfortable Trap) each carry a distinct pattern: solid, striped, spiral, dotted, knotwork
- Room noise levels in the selection UI use icon count (1-3 speaker glyphs), not a red/green scale
- Stamp slots distinguish earned (full-detail ink) / empty (dashed outline) / locked ("Locked" banner) by structure, not hue
- All interactive elements — room rows, toast cards, beat lane, quest notices, opener display, POS terminal — meet the 44px minimum touch target

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (PVRTC 4BPP fallback for legacy devices) — passport pages and dialogue portraits at ASTC 4x4 for text legibility
- **Android:** ETC2 with alpha
- **Fallback:** Lossless PNG for detail-critical assets: passport spread, stamp, main sign lettering, whiskey wall labels

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| blarney_environment | exterior, snug/backroom/questboard, guest rooms | 2048x2048 |
| blarney_bar | main_bar_interior (the hero sheet) | 2048x1024 |
| blarney_characters | seamus_and_staff, regulars_and_crowd | 2048x2048 |
| blarney_items_ui | consumables_brewery_tour, hub_ui_effects, accessibility | 2048x2048 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full pour cascade, animated crowd sway, live trad frames, all particles (dust, shamrocks, rain, foam) |
| Medium | Two-stage settle instead of four, crowd sway at half rate, dust beams static, shamrock burst capped at 8 |
| Low | Static fireplace, static crowd (Frame A), static music session, static rain texture, particles limited to pint-settle only |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 18 per frame (profile performance budget)
- **Memory Footprint:** 40 MB maximum (profile performance budget)
- **Particle Limit:** 20 concurrent — shamrock celebration burst capped at 12, pint-settle 6, dust 8, never all simultaneously

### Performance Notes:
- Simplified crowd is a profile mandate, not a suggestion: crowd is 2 composite blocks + 2 sway frames, full stop
- Static music session option must be selectable independently of LOD (some players just want the musicians still)
- Guest rooms stream on check-in only; the Snug and Backroom load on unlock, never before
- The 119.5-second pour holds ONE keyframe with a particle overlay — it is the cheapest long animation in the game, by design

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- TileMap for floors/walls; ParallaxBackground for The Craic Tax street seen through windows; CPUParticles2D (not GPU) for all particle systems
- Hub systems wired to `blarney_trap_state`: auto-save fires on check-in (Auto-Save Shamrock Spinner, Sheet 8); room restoration tiers (50/70/85/100% + suite buffs) resolve from room ID; pint-off rhythm mini-game reads the beat lane sprites and No-Audio Pulse Bar; toast builder consumes the four line cards; round obligation tracker persists across sessions (the Trap remembers whose round it is)
- "Pub Regular" progression gates content: Snug door (Area2D, locked), Backroom door (locked, quest-overridable), Rumor Board locked/full states, staff dialogue tiers
- Passport is a persistent pause-menu scene once acquired; stamp state, city progress, and Continental tracker read from global save data
- Area2D examine points: Decor Audit items (mirror and chair flagged "actual antique" on examine), regulars photo wall, opener display, "Est. 1847" plaque (triggers the 2003 disclosure), POS terminal (hidden NFT Hunt hotspot)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Pour Ritual F1-F8 + settling stages | Two-stage Guinness pour/surge sound | Pull spans F2-F3; surge holds through the 119.5s settle; chime at completion |
| Trad Session frames | Live/recorded trad music | Frame alternation on the downbeat; between-tunes pose in track gaps |
| Glass Clink Sparkle | Glass clinking | On sparkle frame, every toast |
| Till Ring Flash | Till ringing | On flash frame, every transaction |
| Crowd Cheer frames | Laughter erupting / pint-off crowd reactions | On cheer frame swap |
| Rain-on-Window overlay | Rain on windows | Loop tied to overlay visibility |
| Photo Flash Burst | Tourist photo sound | On burst frame |
| Trap-Spring Entry F2 | "Trap" spring stinger | Exactly on F2, first entry |
| Hen Party Shriek Lines | Distant hen party shrieks | Random 45-90s intervals, evening only |
| Declan Last Orders pose | Last-orders bell | On pose entry, 2:00 AM |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Main Story (Publandia arc) | Seamus states + portraits, dialogue frame, hub backdrop | Main quests progress through key NPC conversations at the Trap; Seamus's Genuine Mode gates late-arc dialogue |
| The Stoutworks Yeast Situation | Craic Broker Quest Handoff, quest notice cards, rumor board | Craic Broker side quest: "Yeast situation. Don't ask questions." Starts at the Snug or board |
| Rival Trio Documentation | Rival Trio Silhouettes, quest notice cards, photo flash burst | Craic Broker side quest: document the rival trio's embarrassment |
| Backroom Operations | Backroom interior, poker table, trivia-fight setup, Declan Backroom Nod | Unlicensed poker and trivia-fights unlock via Pub Regular or quest state |
| Brewery Tour Origin | Bottle Opener Keychain (display + item), Passport (closed/spread/pages), Seamus Opener Pitch | Opener acquired via 15 Sovs purchase, Pint-Off win, or Pub Regular status; Passport Book given FREE with it; the continental sidequest begins here |
| The Blarney Trap Stamp | Stamp sprite, Ink Press frames, Stamp Slam effect, Free Pint Voucher | Stamp requires Pint-Off win OR successful toast OR Pub Regular, with the opener in inventory; unlocks The Sweet Surrender at 8 Sovs |
| Publandia Legendary Hangover | Legendary Hangover consumable, Publandia stamp page, progress bar | All 4 Publandia stamps collected → 50 Sovs ultimate consumable unlocks at any stamped location |
| NFT Hunt (Hidden) | POS Terminal Screen | One hidden acquisition via the Trap's POS terminal — unmarked hotspot, found not advertised |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Craic Tax (streets) | Exterior facade, rival pub slice, cobblestone tiles, street noise through windows | Green door in/out; street ambience crossfade |
| The Stoutworks Brewery | Sweet Surrender bottle/pint/label (contract-brewed by Stoutworks), yeast-situation quest cards | Yeast courier missions depart from the rumor board; Stoutworks stamp shares the passport page |
| Trinity of Pints | Passport page slot, pint-off interface (academic drinking challenges reference Trap rules) | Shared Brewery Tour UI; Trinity stamp on the same page |
| Quay of Last Resort | The Fear icon, desaturation strip, Full Irish sprite | Hungover recovery walks begin from the Trap's door in morning light |
| Shenanigans | Seamus dialogue portraits (Mickey-Seamus friendship references), passport stamp state | Fool's Gold interactions unlock post-stamp; friendship dialogue flags shared |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Every Irish pub cliché executed with professional precision — the trap that tells you it's a trap and traps you anyway"
- **Color Mood:** Pub Green and Guinness Gold selling the brand; Dark Wood and Amber Glow delivering the genuine warmth underneath; Emerald Ink for the moments that turn out to be real
- **Lighting:** Warm amber throughout — fireplace glow, LED candles (fire code), window spill onto wet cobblestones; after-11 lighting drops slightly warmer and dimmer when the real regulars arrive
- **Texture:** Intentional weathering on the facade, elbow-polished mahogany, mass-produced plaques hung with sincere care, exactly two surfaces with genuine age (the mirror, one chair)

### Environmental Storytelling:
- The Decor Audit rendered honestly: 14 reproduction Guinness ads, 4 mass-produced plaques, 3 questionably-signed hurling sticks, 52 real regulars' photos since 2003, 847 shamrocks and counting — and the two actual antiques, unlabeled, for players who look
- "Est. 1847" on the facade vs. the 2003 photo wall: the whole satire in two props
- The gas fireplace that looks turf-burning IS the location: manufactured, warm, and genuinely comforting
- The Snug's etched glass and the unmarked Backroom door promise the real Publandia to anyone who stops being a tourist long enough to earn it

### Character Integration Notes:
- Seamus's welcome must read as both performance AND genuine — the red face, the permanent warmth, the wink; he is never a villain, he is a professional
- The pour ritual frames are the sincerity peak: no comedy in F1-F8, total reverence, the joke is only in how long the bros have to wait
- Old Fergal renders at slightly higher detail than the crowd blocks — he has been on that stool for 40 years and the wear on both should match
- Tourist crowd stays cartoonier than staff and regulars: the satire punches at the visitors, never the hosts

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Perfect Dome Presentation** - Seamus extending the finished Guinness after 119.5 visible seconds of waiting — the whole ritual in one frame
2. **The Trap in the Name** - "THE BLARNEY TRAP — Est. 1847" in gold Celtic lettering with the tiny "Craic Tax Pricing Applies" fine print
3. **The Shamrock Fireplace Selfie Spot** - Designated selfie spot in front of a mantel carrying a meaningful fraction of 847 shamrocks
4. **The Passport Stamp Slam** - Emerald Celtic-knot harp stamp hitting the page, first stamp of the continental tour
5. **The Decor Audit on Examine** - "Actual antiques: 2 (the mirror, one chair)" popping over a wall of manufactured heritage
6. **Old Fergal's Stool** - Empty, worn precisely to one man's shape, 40 years deep
7. **The Joyce Suite** - A hotel room deliberately laid out to be confusing, photographed in bafflement

### Quote Potential:
- "Americans? Brilliant. You'll love it here. Everyone does. That's the trap. *winks*"
- "See that? The surge? That's 119.5 seconds of patience. You can't rush perfection. Or Guinness. Same thing."
- "Every pub in the Craic Tax is a trap. The difference is, I'm honest about it. The trap is in the NAME. That's marketing."
- "The craic is a product. But it's a product I believe in. Manufactured authenticity is still authenticity. Fight me on that."
- "You've been here four hours. That's either commitment or a problem. Could be both."
- "The Snug? That's for regulars. You're not there yet. Maybe soon."
- "You look like you've got The Fear. Don't worry, everyone does. The Full Irish helps. Promise."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | blarney_trap_exterior.png | 1024x512 |
| 2 | main_bar_interior.png | 2048x1024 |
| 3 | snug_backroom_questboard.png | 1024x1024 |
| 4 | guest_rooms_suites.png | 1024x1024 |
| 5 | seamus_and_staff.png | 1024x1024 |
| 6 | regulars_and_crowd.png | 1024x512 |
| 7 | consumables_brewery_tour.png | 1024x512 |
| 8 | hub_ui_effects.png | 1024x1024 |

**Total Estimated Memory:** ~34 MB uncompressed (within the 40 MB hub budget after atlas compression; largest single cost is the 2048x1024 bar interior)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `blarney_trap_exterior.png` (1024x512)
- [ ] `main_bar_interior.png` (2048x1024)
- [ ] `snug_backroom_questboard.png` (1024x1024)
- [ ] `guest_rooms_suites.png` (1024x1024)
- [ ] `seamus_and_staff.png` (1024x1024)
- [ ] `regulars_and_crowd.png` (1024x512)
- [ ] `consumables_brewery_tour.png` (1024x512)
- [ ] `hub_ui_effects.png` (1024x1024)
- [ ] `blarney_trap_accessibility.png` (512x384, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (regulars photo wall, shamrock clusters, and passport page slots on separate layers — the photo wall grows and the passport fills)
- **Documentation:** Animation timing reference sheet (149.5s pour ritual breakdown, pint-off BPM ramp, fireplace jitter, crowd sway period) + day/night facade layer guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Pub Green #228B22, Guinness Gold #FFD700, Dark Wood #3E2723, Emerald Ink #046307)
- [ ] The Perfect Dome reads as genuinely perfect — the one uncompromised craft object in the location
- [ ] "Est. 1847" plaque and 2003 regulars photo wall both legible; the contradiction must be discoverable, not explained
- [ ] "The trap is in the NAME" — main sign, trap-spring mat, and fine print all land in the same establishing screenshot
- [ ] Shamrock clusters convincingly imply 847 without rendering 847; Decor Audit examine data matches the profile counts
- [ ] The two actual antiques (mirror, chair) carry visibly more age than everything around them
- [ ] Accessibility visual alternatives included for all audio cues (pour/surge, trad, clink, till, laughter, rain, photo, trap-spring, bell)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (manufactured authenticity, self-aware tourist trap) is clear throughout all assets
- [ ] Hidden interactions discoverable: antiques on examine, POS terminal hotspot, Snug/Backroom gating cues, locked fourth passport slot
- [ ] Mobile performance optimized (CPU particles, 2048 atlas cap, composite crowd blocks, one-keyframe pour hold)
- [ ] Touch zone sizing considered (44px minimum — room rows, toast cards, beat lane, quest notices, opener display)
- [ ] Colorblind-friendly alternatives available where color codes meaning (shape-coded beats, patterned status badges, icon-count noise levels)
- [ ] Social media viral potential maximized (dome presentation framing, fireplace selfie spot composition, stamp slam moment)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia only; The Craic Tax zone; no real-world city named anywhere in the asset set |
| Cultural Specificity | ✅ | Dublin tourist-district pub economy, Temple Bar pricing satire, Irish pub global brand — rendered in Celtic lettering, knotwork, GAA decor, and the sacred pour |
| Satirical Targets Appropriate | ✅ | Punches at tourist expectations and the "Irish Experience" package, never at Irish hospitality — staff and regulars render with dignity, tourists get the cartoon treatment |
| Seedy Underbelly Present | ✅ | Craic Tax pricing (8 Sovs pints, honest fine print) and the Backroom's unlicensed operations — poker of questionable legitimacy, fights disguised as trivia nights |
| Gameplay Value Established | ✅ | Primary hub: rest/restoration tiers, auto-save, quest board, pint-off rhythm game, toast builder, round obligations, Pub Regular progression, Brewery Tour origin |
| Technical Feasibility | ✅ | 8 sheets, all ≤2048, coordinate-mapped; on-demand room streaming; one-keyframe pour hold; Godot 4.x CPUParticles2D throughout |
| Mobile Performance Budget | ✅ | 60 FPS target, 18 draw calls max, 40 MB memory cap, 20-particle limit with per-system caps documented |
| Accessibility Features | ✅ | Supplemental sheet with visual cues for all critical audio, silent-playable pint-off (pulse bar + shape-coded beats), static fireplace/crowd/session variants, 44px targets |
| No Crypto Elements | ✅ | PASS — the hidden NFT Hunt acquisition at the POS terminal is established in the source material as satire of collectible-mania; it is a diegetic gag, not a monetization system |
| Social Media Integration | ✅ | Seven screenshot moments and profile-sourced quote bank identified; selfie spot indicator is a shipped sprite |

**When these assets are delivered, The Blarney Trap becomes the beating amber heart of Publandia: the inn the bros check into believing they've found a hidden gem, the quest hub that feeds them to the whole city, and the pub honest enough to put the trap in the name, the fine print on the sidewalk, and 119.5 seconds of absolutely genuine craft into every pint they overpay for. Eight hundred forty-seven shamrocks, two real antiques, one perfect dome — and a green door that is always, always open.**

**"You'll love it here. Everyone does. That's the trap."**
