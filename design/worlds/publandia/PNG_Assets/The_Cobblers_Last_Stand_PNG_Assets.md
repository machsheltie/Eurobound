# The Cobbler's Last Stand - Complete PNG Asset Requirements

## 📋 Overview
A footwear shop run like a war room — Finbar O'Sullivan outfits tourists for the battle against Dublin's cobblestones with the gravity of a general sending troops to the front. This document specifies every sprite needed to sell the satire: an equipment shop where the RPG "every purchase is life or death" trope is played completely, gloriously straight.

**Location ID:** `publandia_shop_cobblers_last_stand_01`
**Theme:** Overly intense specialty shopkeeper meets Dublin's foot-destroying streets — shoe shopping as tactical briefing
**Zone:** Cobblestone Market Street (appropriately named)
**Hours:** 10:00-21:00 (Finbar needs his rest for tomorrow's battles)
**Primary Function:** Equipment shop / footwear stat gear / Veteran Walker progression / Finbar assessment system

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Leather Brown | #8B4513 | Shoes, apron, wood shelving |
| Heroic Gold | #DAA520 | Signage lettering, display lighting, commendations |
| Cobblestone Gray | #696969 | Street, exterior ground, the enemy itself |
| Drama Red | #8B0000 | Banner accents, "What We Fight Against" case |
| Faded Cream | #F5F5DC | Wall of Honor photos, aran texture |
| Spotlight Amber | #FFBF00 | Heroic display beams, dust motes |

---

## 📁 File Structure
```
assets/sprites/locations/publandia/cobblers_last_stand/
├── environment/
│   ├── exterior_shopfront.png
│   ├── shop_interior.png
│   └── back_room.png
├── npcs/
│   ├── finbar.png
│   └── cobbler_customers.png
├── objects/
│   └── footwear_arsenal.png
├── effects/
│   └── cobblers_effects.png (packed into cobblers_effects_ui.png)
└── ui/
    └── cobblers_effects_ui.png
```

---

## 🏪 Sprite Sheet 1: Exterior Shopfront
**File:** `exterior_shopfront.png`
**Dimensions:** 512x384 pixels

### Building Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shopfront Base | (0, 0) | 256x256 | Small corner shop, battle-worn stone and timber |
| Roofline & Trim | (0, 256) | 256x64 | Weathered slate, heroic gold trim |
| Main Sign | (256, 0) | 192x48 | "THE COBBLER'S LAST STAND" in weathered heroic lettering |
| Subtitle Plaque | (256, 48) | 192x32 | "Est. 1987 — Still Fighting" |
| Banner | (256, 80) | 192x32 | "YOUR FEET DESERVE A CHAMPION" |
| Window Display | (256, 112) | 128x96 | Shoes arranged like troops awaiting deployment |
| Window Sign | (384, 112) | 64x48 | "Pub Crawl Survivors Outfitted Here" |
| Door Sign | (448, 112) | 64x48 | "Enter Blistered, Leave Prepared" |
| Door Open | (256, 208) | 64x96 | Timber door, brass fittings |
| Door Closed | (320, 208) | 64x96 | Same, closed state |
| Lamppost | (448, 160) | 64x128 | Market street iron lamp |

### Street Environment:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cobblestone Tile Clean | (384, 208) | 64x64 | The enemy, at rest |
| Cobblestone Tile Wet | (384, 272) | 64x64 | The enemy, rain-slicked and lethal |
| Cobblestone Tile Cracked | (448, 288) | 64x64 | Battle damage — theirs, not ours |
| Rain Puddle | (256, 304) | 64x32 | Reflective, near door |
| Awning | (0, 320) | 192x64 | Faded canvas, drama red stripe |
| Doormat | (192, 336) | 64x32 | "WIPE YOUR BOOTS, SOLDIER" |

### Technical Notes:
- Window Display troops must read as deliberately arranged rows at map zoom — the "deployment" gag lands from silhouette alone
- Wet cobblestone tile swaps in during rain weather state; shares tiling edges with clean tile

---

## 🏰 Sprite Sheet 2: Shop Interior — The Battlefield
**File:** `shop_interior.png`
**Dimensions:** 512x512 pixels

### Room Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floorboards | (0, 0) | 256x128 | Worn timber, decades of fitting-strip traffic |
| Back Wall | (0, 128) | 256x128 | Leather brown paneling, mounted commendations |
| Counter | (0, 256) | 192x64 | Cobbler's bench counter, tools racked with military precision |
| Fitting Strip | (0, 320) | 256x64 | The Proving Ground — marked walking lane for gait assessment |
| Back Room Door | (192, 256) | 64x96 | "VETERANS ONLY" — velvet rope hook beside it |

### The Assessment Zone:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Leather Chair Left | (256, 0) | 64x64 | Worn consultation chair |
| Leather Chair Right | (320, 0) | 64x64 | Matching, more worn |
| Reveal Mirror | (384, 0) | 64x96 | Angled for dramatic shoe reveals |
| Briefing Rug | (448, 0) | 64x64 | Where the mission briefing feeling begins |

### The Arsenal (Display Walls):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Speed Wall | (256, 96) | 128x96 | "SPEED — Wet Street Navigation" shelf with spotlit shoes |
| Stealth Wall | (384, 96) | 128x96 | "STEALTH — Bouncer Evasion" shelf, dimmer lighting |
| Defense Wall | (256, 192) | 128x96 | "DEFENSE — Foot Protection" shelf, steel glinting |
| Endurance Wall | (384, 192) | 128x96 | "ENDURANCE — Long Night Survival" shelf |
| Tactical Labels Strip | (256, 288) | 256x32 | Dramatic category description cards |

### The Wall of Honor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Honor Wall Base | (256, 320) | 160x128 | Photos of satisfied customers, survivor testimonials |
| Destroyed Shoes Case | (416, 320) | 96x96 | Glass case, ruined flip-flops: "WHAT WE FIGHT AGAINST" |
| Commendation Frames | (0, 384) | 96x64 | Finbar's personal commendations |
| Observation Post | (96, 384) | 96x96 | Finbar's stool, clipboard, intense sightline to fitting strip |
| Spotlight Fixture | (192, 384) | 64x48 | Ceiling spot aimed at displays |
| Testimonial Cards | (192, 432) | 64x48 | "NOT ONE BLISTER" framed quotes |
| Measuring Station | (256, 448) | 128x64 | Brannock device, arch-support charts, war maps of foot anatomy |
| Shoe Box Stack | (384, 448) | 128x64 | Pre-prepared boxes for Regulars |

### Technical Notes:
- Display wall spotlights use additive Spotlight Amber overlay; disabled in Low LOD
- Fitting Strip has subtle painted distance markers — Finbar's gait analysis is visible environmental storytelling

---

## 🚪 Sprite Sheet 3: The Back Room — Veteran's Collection
**File:** `back_room.png`
**Dimensions:** 256x256 pixels

### Premium Area:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Premium Shelf Wall | (0, 0) | 256x128 | Dark wood, museum lighting, where the really good stuff lives |
| Last Stand Boots Display | (0, 128) | 64x64 | Finbar's masterwork on a pedestal |
| Legendary Loafers Display | (64, 128) | 64x64 | Glass dome, "Swift as the Wind" |
| Cobbler's Pride Pedestal | (128, 128) | 64x64 | Custom-made display, spotlit |
| Battle-Worn Veterans Display | (192, 128) | 64x64 | Shoes that have "Seen Things" |
| Velvet Curtain | (0, 192) | 64x64 | Entry drape, earned access only |
| Trust Lamp | (64, 192) | 32x64 | Single warm lamp — intimacy of earned respect |
| Custom Mod Bench | (96, 192) | 96x64 | Where Veteran Walker modifications happen |
| Heirloom Tools | (192, 192) | 64x64 | Three generations of cobbler tools, oldest at center |

### Technical Notes:
- Back room only loads after `veteran_walker` flag (3 purchases); door remains a locked interaction until then
- Heirloom Tools is an examine point unlocking Finbar's family history dialogue

---

## 👞 Sprite Sheet 4: Finbar O'Sullivan
**File:** `finbar.png`
**Dimensions:** 384x384 pixels

### Finbar States (96x128 each):
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Idle | (0, 0) | 96x128 | Behind counter, leather apron, watchful |
| Assessing | (96, 0) | 96x128 | Kneeling, examining customer footwear with visible concern |
| Tactical Briefing | (192, 0) | 96x128 | Pointing at display wall, full war-room mode |
| Presenting Shoe | (288, 0) | 96x128 | Two-handed dramatic reveal, shoe held like a relic |
| Observing | (0, 128) | 96x128 | Arms crossed at Observation Post, watching the fitting strip |
| Concerned | (96, 128) | 96x128 | Deep sigh, Grade D-F footwear detected |
| Approving Nod | (192, 128) | 96x128 | The rare verdict: "Now you're ready." |
| Emotional | (288, 128) | 96x128 | Softened — Mary's-photo-grade restraint for the free-fitting moment |

### Finbar Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Leather Apron | (0, 256) | 64x64 | Tool loops, thirty years of polish stains |
| Cobbler Hands | (64, 256) | 64x32 | Hands that have shaped thousands of shoes |
| Measuring Tape | (128, 256) | 32x32 | Drawn like a weapon |
| Brannock Device | (160, 256) | 32x32 | The instrument of truth |
| Clipboard | (192, 256) | 32x32 | Gait assessment notes |

### Finbar Expressions (48x48 each):
| Expression | Position | Size | Description |
|------------|----------|------|-------------|
| Suspicious Assessment | (0, 288) | 48x48 | Default for casual browsers |
| Thousand-Yard Stare | (48, 288) | 48x48 | "These are what you've been WALKING on?" |
| Medical Emergency | (96, 288) | 48x48 | Visible blisters detected |
| General's Pride | (144, 288) | 48x48 | Premium purchase complete |
| Rare Warmth | (192, 288) | 48x48 | "...this one gets fitted for free." |

### Dialogue Portraits (64x48 each):
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Portrait Default | (0, 336) | 64x48 | Grave intensity |
| Portrait Briefing | (64, 336) | 64x48 | Mid-education |
| Portrait Horror | (128, 336) | 64x48 | Grade F silent horror |
| Portrait Approval | (192, 336) | 64x48 | The verdict softens |

---

## 👥 Sprite Sheet 5: Customer NPCs
**File:** `cobbler_customers.png`
**Dimensions:** 256x192 pixels

### Customers (64x96 each):
| NPC | Position | Size | Description |
|-----|----------|------|-------------|
| The Convert | (0, 0) | 64x96 | Returning believer — "NOT ONE BLISTER. The man's a genius." |
| The Skeptic | (64, 0) | 64x96 | Eye-rolling, reluctant browsing: "It's just SHOES, mate." |
| The Casualty | (128, 0) | 64x96 | Limping in desperately, flip-flop victim |
| The Regular | (192, 0) | 64x96 | Local, points at shoes, nods — 15-second transaction |

### Customer Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ruined Flip-Flops | (0, 96) | 32x32 | The Casualty's crime against feet |
| Pre-Prepared Box | (32, 96) | 32x32 | The Regular's order, always ready |
| Bandaged Feet | (64, 96) | 32x32 | Post-intervention Casualty state |
| Bradley's Arch Supports | (96, 96) | 32x32 | Brought from home — free fitting earned |
| Trainer Pair (Doomed) | (128, 96) | 32x32 | Lord Pilsner's "they're fine" trainers |
| Customer Portraits Strip | (0, 128) | 256x48 | 4 dialogue portraits, 64x48 each |

---

## 🥾 Sprite Sheet 6: The Footwear Arsenal
**File:** `footwear_arsenal.png`
**Dimensions:** 256x256 pixels

### Speed & Stealth Row (32x32 each, y=0):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Comfy Loafers | (0, 0) | 32x32 | Speed basic, 35 Sovs |
| Craic Tax Treads | (32, 0) | 32x32 | Speed mid — "They've seen combat" |
| The Quickstep | (64, 0) | 32x32 | Speed advanced, Light-Footed buff |
| Finbar's Flyers | (96, 0) | 32x32 | Speed premium, winged heel detail |
| Pub Crawl Sneakers | (128, 0) | 32x32 | Stealth basic |
| The Silent Strider | (160, 0) | 32x32 | Stealth mid, soft profile |
| Soft-Sole Specials | (192, 0) | 32x32 | Stealth, "Unnoticed" buff |
| Ghost Walkers | (224, 0) | 32x32 | Stealth premium, bouncer bypass |

### Defense & Endurance Row (32x32 each, y=32):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Steel-Toe Stouts | (0, 32) | 32x32 | Defense basic, steel glint |
| The Fortified Foot | (32, 32) | 32x32 | Defense mid, kick-enabled |
| Cobblestone Crushers | (64, 32) | 32x32 | Terrain immunity |
| Finbar's Fortress | (96, 32) | 32x32 | Defense premium, "Immovable" |
| All-Night Stompers | (128, 32) | 32x32 | Endurance basic, blister immunity |
| The Marathon Walker | (160, 32) | 32x32 | Endurance mid |
| Comfort Crusaders | (192, 32) | 32x32 | Fatigue reduction |
| Finbar's Forever Feet | (224, 32) | 32x32 | Endurance premium, "Inexhaustible" |

### Premium Stock Row (32x32 each, y=64):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| The Last Stand Boots | (0, 64) | 32x32 | Masterwork, all-terrain |
| Legendary Loafers | (32, 64) | 32x32 | "Swift as the Wind" |
| The Cobbler's Pride | (64, 64) | 32x32 | Custom-made, gold stitching |
| Battle-Worn Veterans | (96, 64) | 32x32 | "Seen Things" intimidation |
| Shoe Box Closed | (128, 64) | 32x32 | Standard issue packaging |
| Shoe Box Open | (160, 64) | 32x32 | Tissue paper reveal state |
| Polish Tin | (192, 64) | 32x32 | Counter prop |
| Legendary Ribbon | (224, 64) | 32x32 | Premium tier marker |

### Accessories Row (24x24 each, y=96):
| Item | Position | Size | Description |
|------|----------|------|-------------|
| Lucky Charm Bracelet | (0, 96) | 24x24 | Bravado resistance |
| Rain-Resistant Socks | (24, 96) | 24x24 | "Soggy" immunity |
| Cobblestone Insoles | (48, 96) | 24x24 | Retrofit upgrade |
| Emergency Blister Kit | (72, 96) | 24x24 | Cures "Blistered" once |
| Power Stance Laces | (96, 96) | 24x24 | "Firm Footing" |

### Display Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Heroic Display Glow | (0, 128) | 64x64 | Under-shoe pedestal light |
| Spotlight Cone | (64, 128) | 64x64 | Makes footwear look heroic |
| Price Tag Set | (128, 128) | 64x32 | 35-150 Sovs range tags |
| Category Icons | (128, 160) | 64x32 | Speed/Stealth/Defense/Endurance glyphs (wing, mask, shield, mountain) |
| Tactical Description Cards | (0, 192) | 256x64 | Dramatic per-shoe copy plates, 64x64 each x4 |

### Technical Notes:
- Every shoe sprite needs a mirrored equip variant generated at runtime — no extra art
- Category icons are shape-coded (not color-coded) for colorblind safety

---

## ✨ Sprite Sheet 7: Effects & UI
**File:** `cobblers_effects_ui.png`
**Dimensions:** 512x256 pixels

### Effects:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Dust Motes | (0, 0) | 32x32 | Floating in light beams |
| Polish Shine Frame 1-4 | (32, 0) | 64x16 | Four 16x16 glint frames on leather |
| Spotlight Beam | (96, 0) | 64x96 | Heroic display shaft |
| Dramatic Vignette | (160, 0) | 64x64 | Screen-edge darkening for assessment verdicts |
| Reveal Sparkle | (224, 0) | 32x32 | Shoe presentation flourish |

### Shopping UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Equipment Menu Frame | (0, 96) | 192x128 | Shop interface, war-room map styling |
| Assessment Grades A-F | (192, 96) | 192x48 | Six 32x48 grade cards, gold A to red F |
| Fitting Ceremony Tracker | (192, 144) | 128x48 | Six-step progress: Assess → Consult → Measure → Select → Test → Approve |
| Stat Comparison Panel | (320, 144) | 128x96 | Current vs. new footwear stats |
| Veteran Walker Badge | (256, 0) | 48x48 | Back room access earned |
| Finbar Approval Stamp | (304, 0) | 64x64 | Boot-print seal, rare honor |
| "Well-Shod" Buff Icon | (368, 0) | 32x32 | Terrain resistance active |
| "Finbar Approved" Icon | (400, 0) | 32x32 | Assessment passed |
| Warning Popup | (384, 96) | 128x48 | "GRADE F. IMMEDIATE INTERVENTION." |
| Purchase Confirm | (0, 224) | 96x32 | "EQUIP FOR BATTLE?" |
| Discount Banner | (96, 224) | 96x32 | Veteran 10% / Grade A 5% / rescue markup 10% |
| Rescue Markup Tag | (192, 224) | 64x32 | "He's doing you a favor" |

---

## 🎬 Animation Specifications

### Finbar Assessment:
- **Duration:** 4 seconds
- **Frames:** 5
- **Pattern:** Idle → kneel → examine (hold 2s) → rise → verdict expression
- **Trigger:** Player enters shop or requests assessment
- **Purpose:** The medical-diagnosis gravity that defines the location
- **Audio Sync:** Ominous low tone swells during the examine hold; verdict sting on final frame
- **Mobile Optimization:** None needed

### The Shoe Reveal:
- **Duration:** 2.5 seconds
- **Frames:** 4 + Reveal Sparkle overlay
- **Pattern:** Reach → lift → two-handed presentation (hold) → sparkle
- **Trigger:** Selecting any item in the equipment menu
- **Purpose:** Every shoe is presented like a relic; the satire is the ceremony
- **Audio Sync:** Dramatic reveal sting exactly on the presentation hold frame
- **Mobile Optimization:** Sparkle overlay dropped on Low LOD

### Fitting Strip Walk:
- **Duration:** 6 seconds
- **Frames:** Player walk cycle + Finbar Observing state with 3 clipboard-check frames
- **Pattern:** Walk down strip → turn → walk back; Finbar notes at each marker
- **Trigger:** Fitting Ceremony step 5
- **Purpose:** The Proving Ground moment of truth
- **Audio Sync:** Footsteps on timber; pencil scratch on each clipboard check
- **Mobile Optimization:** Clipboard frames reduced to 1 on Low LOD

### Approval Nod:
- **Duration:** 1.5 seconds
- **Frames:** 3
- **Pattern:** Stillness → single slow nod → hold
- **Trigger:** Ceremony passed / Grade A assessment / Cobbler's Blessing (+20 Bravado)
- **Purpose:** Restraint is the reward — one nod carries thirty years of standards
- **Audio Sync:** Subtly epic music swell resolves on the nod
- **Mobile Optimization:** None needed

### Dust Motes & Spotlight:
- **Duration:** Continuous, 8-second drift loop
- **Frames:** 3 mote positions, alpha-cycled
- **Trigger:** Constant in interior
- **Purpose:** Moody, heroic equipment-montage atmosphere
- **Audio Sync:** None
- **Mobile Optimization:** Motes off on Low LOD, spotlight becomes static overlay

---

## ♿ Accessibility Sprite Requirements
**File:** `cobblers_accessibility.png` (supplemental sheet — delivered alongside the 7 base files, not counted in their total)
**Dimensions:** 256x192 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Equipment Menu, Bold | (0, 0) | 96x64 | Thick-bordered shop frame, enlarged item rows |
| Grade Cards, Bold | (96, 0) | 96x48 | A-F with letter + outline weight, not color alone |
| Finbar Interaction Outline | (192, 0) | 48x64 | White-on-dark counter hotspot outline |
| Destroyed Shoes Case Outline | (0, 64) | 64x64 | Examine hotspot, "WHAT WE FIGHT AGAINST" at readable weight |
| Back Room Door Outline | (64, 64) | 64x64 | Locked/unlocked states clearly differentiated by icon |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Spotlight, Static | (128, 64) | 64x64 | Non-shimmering display beam |
| Reveal, No Sparkle | (192, 64) | 32x32 | Presentation hold without flourish particles |
| Vignette, Off | (224, 64) | 32x32 | Flat verdict frame replacing screen-edge pulse |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Reveal Sting Burst | (0, 128) | 32x32 | Starburst glyph on shoe presentation |
| Ominous Tone Lines | (32, 128) | 32x32 | Low-wave glyph during assessment hold |
| Music Swell Note | (64, 128) | 32x32 | Rising-note glyph on approval nod |
| Leather Creak Icon | (96, 128) | 32x32 | On chair sit / apron gestures |
| Pencil Scratch Icon | (128, 128) | 32x32 | Clipboard checks during fitting walk |
| Footstep Ripple | (160, 128) | 32x32 | Fitting strip walk feedback |

### Colorblind Considerations:
- Grade cards carry letters A-F plus distinct border patterns — never gold/red alone
- Shoe category coding is icon-shaped (wing/mask/shield/mountain), not shelf-color dependent
- All examine hotspots and menu rows meet the 44px minimum touch target

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (grade cards and signage text at ASTC 4x4 for legibility)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for Finbar portraits and signage

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| cobblers_environment | exterior, interior, back_room | 1024x1024 |
| cobblers_characters | finbar, cobbler_customers | 512x512 |
| cobblers_items_ui | footwear_arsenal, effects_ui | 512x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full dust motes, spotlight shimmer, sparkle, all customer NPCs |
| Medium | Static spotlight, motes halved, 2 customer NPCs max |
| Low | No particles, static displays, Finbar + 1 customer only |

### Performance Targets:
- **Target FPS:** 60
- **Max Draw Calls:** 12 per frame
- **Memory Footprint:** 30 MB maximum
- **Particle Limit:** 12 (motes + sparkle combined)

### Performance Notes:
- Back room streams on demand behind the Veteran Walker gate — never resident before unlock
- Display wall spotlights are one shared additive quad, not four fixtures

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- TileMap for cobblestone street tiles (clean/wet/cracked variants swap by weather state); simple fade for interior/exterior transition
- CPUParticles2D (not GPU) for dust motes and reveal sparkle; spotlight shimmer via alpha-modulated overlay, disabled in reduced-motion mode
- Area2D examine points: Destroyed Shoes Case, Wall of Honor, Heirloom Tools, Fitting Strip markers
- Assessment system reads player equipment slot on entry → grade A-F → drives Finbar state, dialogue branch, and discount/markup (`cobblers_state`: grade, purchases_count, veteran_walker, ceremony_completed, blessing_received)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Shoe Reveal (2.5s) | Dramatic reveal sting | On the presentation hold frame |
| Assessment examine hold | Ominous low tone | Swells across the 2s hold, cuts on verdict |
| Approval Nod | Epic music swell resolve | Resolves exactly on the nod |
| Fitting strip clipboard checks | Pencil scratch | Each marker pass |
| Grade F verdict | Silence, then intervention line | 1s dead air before "Sit down." |
| Door open | Shop bell + leather creak | On door-open frame |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Perfect Fit | Fitting Ceremony Tracker, all 6 ceremony beats, Measuring Station | Completing the full ceremony start to Approval Nod |
| Cobblestone Conquest | Well-Shod buff icon, cobblestone tiles | Pub crawl completed without foot damage while wearing Cobbler's gear |
| The Back Room | Veteran Walker Badge, Back Room Door, all 4 premium displays | Unlocks on third purchase; door interaction changes state |
| Finbar's Approval | Rare Warmth expression, Approval Stamp, Portrait Approval | The genuine compliment — +20 Bravado "Cobbler's Blessing" |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Craic Tax | Cobblestone tiles are the shared battlefield; Craic Tax Treads named for it | Standard street transition; Finbar's briefing references it |
| The Bunk & Blunder | The Casualty NPC limps in from there | None — narrative link via dialogue |
| Plot Armor Provisions | Complementary prep shop (food vs. equipment) | Market street adjacency |
| The Quiet Man | Defense shoes carry into fight mechanics | Steel-Toe Stouts / Fortress stat bonuses apply in the Pit |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A war room that happens to sell shoes — heroic lighting on humble leather"
- **Color Mood:** Leather Brown and Cobblestone Gray grounded reality, cut by Heroic Gold and Spotlight Amber wherever Finbar has decided something matters (everything matters)
- **Lighting:** Dramatic display spotlights against moody ambiance; the fitting strip lit like an operating theater
- **Texture:** Worn leather, polished counters, scuffed timber floor from thirty years of proving-ground walks

### Environmental Storytelling:
- The window display's troop formation tells you everything before you enter
- The Destroyed Shoes Case ("WHAT WE FIGHT AGAINST") is the location's thesis in one prop
- Wall of Honor testimonials and the pre-prepared Regular's box show a man who has never once been casual about this
- Category walls escalate from retail shelf to armory the deeper you look

### Character Integration Notes:
- Finbar's eight states must sell total sincerity — the comedy comes from the gravity, never from mugging
- The Approval Nod is a single slow nod; overdoing it breaks the character
- Customer NPCs are the reaction spectrum: Convert, Skeptic, Casualty, Regular map the full arc from doubt to devotion

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Destroyed Shoes Case** - A glass museum case containing ruined flip-flops labeled "WHAT WE FIGHT AGAINST"
2. **The Window Display** - Shoes arranged like troops awaiting deployment, visible from the street
3. **The Grade F Verdict** - Finbar's silent horror expression with the intervention popup
4. **The Shoe Reveal** - A loafer presented with the ceremony of a holy relic
5. **The Wall of Honor** - Framed testimonial: "NOT ONE BLISTER"

### Quote Potential:
- "Sir. Nothing about these is fine. Sit down. We have work to do."
- "You're going on a pub crawl? That's 8-12 kilometers of urban warfare. Are you EQUIPPED for that?"
- "The Romans conquered Europe in sandals, and look what happened to THEM. History teaches us: invest in footwear."
- "My competitors sell shoes. I sell SURVIVAL. The shoes are just the delivery mechanism."
- "...this one gets fitted for free."

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | exterior_shopfront.png | 512x384 |
| 2 | shop_interior.png | 512x512 |
| 3 | back_room.png | 256x256 |
| 4 | finbar.png | 384x384 |
| 5 | cobbler_customers.png | 256x192 |
| 6 | footwear_arsenal.png | 256x256 |
| 7 | cobblers_effects_ui.png | 512x256 |

**Total Estimated Memory:** ~14 MB

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `exterior_shopfront.png` (512x384)
- [ ] `shop_interior.png` (512x512)
- [ ] `back_room.png` (256x256)
- [ ] `finbar.png` (384x384)
- [ ] `cobbler_customers.png` (256x192)
- [ ] `footwear_arsenal.png` (256x256)
- [ ] `cobblers_effects_ui.png` (512x256)
- [ ] `cobblers_accessibility.png` (256x192, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (each display wall and Wall of Honor photo on separate layers — the honor wall is designed to grow)
- **Documentation:** Animation timing reference sheet (assessment 4s, reveal 2.5s, fitting walk 6s, nod 1.5s)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Leather Brown #8B4513, Heroic Gold #DAA520, Cobblestone Gray #696969, Drama Red #8B0000)
- [ ] "WHAT WE FIGHT AGAINST" case label readable on examine
- [ ] Window display troop formation reads from street view
- [ ] Approval Nod restraint preserved — one nod, no flourish
- [ ] Accessibility visual alternatives included for all audio cues (sting, tone, swell, scratch, bell)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (military gravity applied to shoe retail) is clear throughout all assets
- [ ] Easter eggs discoverable: Heirloom Tools, Bradley's arch supports, the doomed trainers, pre-prepared Regular's box
- [ ] Mobile performance optimized (12-particle cap, streamed back room, shared spotlight quad)
- [ ] Touch zone sizing considered (44px minimum — menu rows, grade cards, examine hotspots compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (lettered grades, icon-shaped categories)
- [ ] Social media viral potential maximized (Destroyed Shoes Case framing, reveal ceremony composition)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Publandia, Cobblestone Market Street only |
| Cultural Specificity | ✅ | Dublin cobblestone carnage, passionate Irish craftspeople |
| Satirical Targets Appropriate | ✅ | Intense shopkeepers + tourist footwear hubris — affectionate, punches up |
| Seedy Underbelly Present | ✅ | Cobblestone trauma capitalized on; Grade F "rescue" markup |
| Gameplay Value Established | ✅ | Full equipment shop, stat gear, assessment system, Veteran Walker progression |
| Technical Feasibility | ✅ | 7 sheets, simple transitions, mobile optimization documented |
| Mobile Performance Budget | ✅ | 60 FPS, 12 draw calls, 30MB |
| Accessibility Features | ✅ | Visual cues for every audio beat, static-light variants, lettered grades |
| No Crypto Elements | ✅ | Absent from source and spec |
| Social Media Integration | ✅ | Five viral moments identified, quote bank sourced from profile |

**The Cobbler's Last Stand delivers when the player laughs at Finbar's intensity on entry and silently thanks him twelve pubs later. Every asset — the troop-formation window, the flip-flop reliquary, the single slow nod — insists that shoe shopping matters. Because in Publandia, it does.**

**"Enter Blistered, Leave Prepared."**
