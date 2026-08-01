# Euro Ink 4 Less - Complete PNG Asset Requirements

## 📋 Overview
**Location ID:** `debaucheryville_oldtown_euro_ink_4_less_01`  
**Theme:** Budget tattoo parlor where skeletons become ducks through "artistic interpretation"  
**Zone:** Old Town District, Alley off Astronomical Cock-Up Square  
**Hours:** 10:00 - 02:00

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Neon Pink | #FF1493 | Main signage, accent lighting |
| Clinical White | #F5F5F5 | Walls, work surfaces |
| Neon Green | #7FFF00 | Beer sign glow |
| Blood Red | #8B0000 | Accent details, some flash art |
| Dingy Gray | #696969 | Floor, shadows |
| Nicotine Yellow | #F5DEB3 | Ceiling stains, aged elements |
| Fluorescent Blue | #F0F8FF | Harsh overhead light |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/euro_ink_4_less/
├── environment/
│   ├── shop_interior_complete.png
│   ├── exterior_alley.png
│   ├── neon_signage.png
│   ├── flash_art_wall.png
│   └── lighting_overlays.png
├── npcs/
│   ├── jakub_artist.png
│   ├── marta_assistant.png
│   └── lord_pilsner_reactions.png
├── objects/
│   ├── tattoo_station.png
│   ├── reception_counter.png
│   ├── waiting_area.png
│   └── equipment_details.png
├── tattoo_process/
│   ├── sketch_sequence.png
│   ├── tattooing_animation.png
│   ├── reveal_sequence.png
│   └── duck_tattoo_final.png
├── effects/
│   ├── neon_flicker.png
│   ├── fluorescent_flicker.png
│   ├── dust_motes.png
│   └── tattoo_gun_effects.png
└── ui/
    ├── mini_game_ui.png
    ├── shop_menu.png
    └── dialogue_portraits.png
```

---

## 🏪 Sprite Sheet 1: Shop Interior
**File:** `shop_interior_complete.png`  
**Dimensions:** 1024x512 pixels

### Floor & Walls:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Floor Tiles Main | (0, 0) | 256x128 | Cracked linoleum, slightly sticky looking |
| Floor Tiles Worn | (256, 0) | 128x128 | Extra worn section near tattoo chair |
| Wall Base White | (0, 128) | 256x256 | Dingy white walls, nicotine tint at top |
| Wall With Flash Art | (256, 128) | 256x256 | Covered in tattoo flash sheets |
| Ceiling Tiles | (512, 0) | 256x128 | Drop ceiling, one tile missing |
| Beaded Curtain | (384, 0) | 128x256 | Entrance to back room |

### Architectural Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Front Window | (512, 128) | 192x192 | Tinted, stickers visible from inside |
| Entry Door | (704, 128) | 128x192 | Glass door, "PUSH" sign |
| Back Room Glimpse | (512, 320) | 256x128 | Mattress visible through beads |

---

## 🌃 Sprite Sheet 2: Exterior Alley
**File:** `exterior_alley.png`  
**Dimensions:** 512x384 pixels

### Alley Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Alley Floor | (0, 0) | 256x128 | Cracked concrete, puddles |
| Alley Walls | (256, 0) | 256x256 | Brick, graffiti, pipes |
| Shop Entrance | (0, 128) | 192x192 | Door with neon glow spill |
| Kebab Shop (Adjacent) | (192, 128) | 160x192 | Neighboring business, lit sign |
| Currency Exchange (Adjacent) | (352, 128) | 160x192 | Other neighbor, sketchy rates |
| Dumpster | (0, 320) | 96x64 | Near entrance |
| Street Light | (96, 256) | 32x128 | Flickering |

---

## 💡 Sprite Sheet 3: Neon Signage
**File:** `neon_signage.png`  
**Dimensions:** 384x256 pixels

### Sign States:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Full Sign On | (0, 0) | 192x64 | "EURO INK 4 LESS" full glow |
| Sign Flicker 1 | (0, 64) | 192x64 | "4" dimmed |
| Sign Flicker 2 | (0, 128) | 192x64 | "4" off |
| Sign Flicker 3 | (0, 192) | 192x64 | Whole sign dim |
| Walk-Ins Welcome | (192, 0) | 128x32 | Hand-painted secondary sign |
| No Regrets Sign | (192, 32) | 128x48 | With small "Mostly" visible |
| Window Stickers | (192, 80) | 128x64 | "HYGENIC" misspelled, expired license |
| Beer Sign Neon | (192, 144) | 96x64 | Generic beer brand, pink/green |
| Open Sign | (288, 144) | 64x32 | Red neon "OPEN" |

---

## 🎨 Sprite Sheet 4: Flash Art Wall
**File:** `flash_art_wall.png`  
**Dimensions:** 512x512 pixels

### Flash Art Categories:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Skulls Section | (0, 0) | 256x128 | 12 skull designs, varying quality |
| Tribal Section | (256, 0) | 256x128 | Generic tribal patterns |
| Animals Section | (0, 128) | 256x128 | Eagles, wolves, inexplicable ducks |
| Looney Tunes Section | (256, 128) | 256x128 | Bootleg cartoon characters |
| Hearts & Roses | (0, 256) | 128x128 | Classic flash, faded |
| Dragons | (128, 256) | 128x128 | European style (confused) |
| Text Designs | (256, 256) | 128x128 | "MOM", "DEATH", "NO REGRETS" |
| Jakub's Specials | (384, 256) | 128x128 | His "best work" - mostly birds |
| Clock Skeleton | (0, 384) | 96x96 | Reference photo (looks like skeleton) |
| Jakub's Interpretation | (96, 384) | 96x96 | His sketch (clearly a duck) |

---

## 👤 Sprite Sheet 5: Jakub the Artist
**File:** `jakub_artist.png`  
**Dimensions:** 512x384 pixels

### Character Poses:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Idle Standing | (0, 0) | 64x96 | Welcoming pose, arms open |
| Greeting Gesture | (64, 0) | 64x96 | Enthusiastic wave |
| Showing Sketch | (128, 0) | 64x96 | Holding paper proudly |
| Pointing at Flash | (192, 0) | 64x96 | Gesturing to wall |
| Seated Working | (256, 0) | 96x96 | At tattoo station |
| Tattooing Frame 1 | (352, 0) | 96x96 | Gun in hand, focused |
| Tattooing Frame 2 | (448, 0) | 64x96 | Mid-stroke |
| Tattooing Frame 3 | (0, 96) | 64x96 | Wiping |
| Proud Reveal | (64, 96) | 64x96 | Arms wide, presenting work |
| Nodding Agreement | (128, 96) | 64x96 | Validating customer |
| Money Counting | (192, 96) | 64x96 | Satisfied transaction |
| Confused | (256, 96) | 64x96 | "Duck? No, is skeleton." |

### Detail Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Jakub's Arms | (0, 192) | 192x64 | Showing his own tattoo work |
| Leather Vest | (192, 192) | 64x64 | Costume detail |
| Gold Tooth Glint | (256, 192) | 32x32 | Smile detail |
| Reading Glasses | (288, 192) | 32x16 | On forehead, never used |
| Cigarette Behind Ear | (320, 192) | 16x32 | Sometimes lit |
| Tattoo Gun | (336, 192) | 48x32 | Equipment |
| Sketch Pad | (384, 192) | 64x48 | With duck drawing |

---

## 👩 Sprite Sheet 6: Marta (Assistant)
**File:** `marta_assistant.png`  
**Dimensions:** 256x192 pixels

### Character Poses:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Counter Idle | (0, 0) | 64x96 | Behind reception, skeptical |
| Eye Roll | (64, 0) | 64x96 | Reacting to Jakub |
| Shrug | (128, 0) | 64x96 | "He does good work. Usually." |
| Cash Handling | (192, 0) | 64x96 | Taking payment |
| Arms Crossed | (0, 96) | 64x96 | Watching judgment |
| On Phone | (64, 96) | 64x96 | Ignoring everything |

### Detail Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bleached Hair | (128, 96) | 48x32 | Hair detail |
| Excessive Jewelry | (176, 96) | 48x32 | Rings, necklaces |
| Nail Inspection | (128, 128) | 64x32 | Bored pose hands |

---

## 😰 Sprite Sheet 7: Lord Pilsner Reactions
**File:** `lord_pilsner_reactions.png`  
**Dimensions:** 384x256 pixels

### Reaction Sequence:
| Expression | Position | Size | Description |
|------------|----------|------|-------------|
| Excited Entry | (0, 0) | 64x96 | Confident, pointing at back |
| Design Review Happy | (64, 0) | 64x96 | Approving the duck sketch |
| Lying Down | (128, 0) | 96x64 | On tattoo chair, face down |
| Pain Flinch 1 | (0, 96) | 64x64 | Mild discomfort |
| Pain Flinch 2 | (64, 96) | 64x64 | More pain |
| Pain Flinch 3 | (128, 96) | 64x64 | Trying to be brave |
| Mirror Check | (192, 96) | 64x96 | Looking backwards, confused |
| Revelation Joy | (256, 96) | 64x96 | "It's PERFECT" |
| Defensive | (320, 96) | 64x96 | "It's ARTISTIC INTERPRETATION" |
| Satisfied Leaving | (0, 160) | 64x96 | Walking out proud |

### Pain Meter Faces:
| Level | Position | Size | Description |
|-------|----------|------|-------------|
| Level 1 | (192, 0) | 32x32 | Slight grimace |
| Level 2 | (224, 0) | 32x32 | Teeth gritted |
| Level 3 | (256, 0) | 32x32 | Eyes watering |
| Level 4 | (288, 0) | 32x32 | Full flinch |
| Level 5 | (320, 0) | 32x32 | Maximum pain |

---

## 🪑 Sprite Sheet 8: Tattoo Station
**File:** `tattoo_station.png`  
**Dimensions:** 384x256 pixels

### Station Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tattoo Chair Empty | (0, 0) | 128x128 | Adjustable, duct-taped |
| Tattoo Chair Occupied | (128, 0) | 128x128 | With Lord Pilsner |
| Rolling Cart | (256, 0) | 64x96 | Equipment, ink bottles |
| Ink Bottles | (320, 0) | 64x32 | Various colors |
| Adjustable Lamp | (256, 96) | 48x64 | Harsh spotlight |
| Paper Towels | (304, 96) | 32x32 | Bloody ones |
| Autoclave | (336, 96) | 48x64 | Steaming (for show) |
| Mirror Stand | (0, 128) | 64x96 | Awkward angle |
| Hand Mirror | (64, 128) | 32x48 | For reveal |
| Stencil Paper | (96, 128) | 48x32 | With duck design |

### Chair Animation States:
| State | Position | Size | Description |
|-------|----------|------|-------------|
| Reclined Empty | (0, 176) | 128x80 | Ready position |
| Reclined Occupied | (128, 176) | 128x80 | LP face down |
| Mid-Tattoo | (256, 176) | 128x80 | Jakub working |

---

## 🛒 Sprite Sheet 9: Reception Counter
**File:** `reception_counter.png`  
**Dimensions:** 256x192 pixels

### Counter Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Counter Full | (0, 0) | 192x96 | Glass display, register |
| Jewelry Display | (0, 96) | 96x64 | All same cheap pieces |
| Guest Book | (96, 96) | 48x32 | Suspiciously empty |
| Lollipop Jar | (144, 96) | 32x48 | "For brave customers" |
| Cash Register | (176, 96) | 48x48 | Old, manual |
| Business Cards | (192, 0) | 64x32 | "EURO INK 4 LESS - Jakub" |
| Fake License | (192, 32) | 64x48 | Clearly printed at home |

---

## 🛋️ Sprite Sheet 10: Waiting Area
**File:** `waiting_area.png`  
**Dimensions:** 256x192 pixels

### Furniture:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Chair 1 | (0, 0) | 48x64 | Mismatched plastic |
| Chair 2 | (48, 0) | 48x64 | Different mismatched |
| Beanbag | (96, 0) | 64x48 | Stained, deflated |
| Coffee Table | (0, 64) | 96x48 | Magazines from 2017 |
| Magazines | (96, 64) | 48x32 | Outdated, worn |
| Floor Lamp | (144, 0) | 32x96 | Doesn't work |
| Wall Clock | (176, 0) | 32x32 | Stuck at 4:20 |
| "Wall of Fame" | (0, 112) | 192x80 | Customer photos (uncertain faces) |

---

## 🦆 Sprite Sheet 11: Tattoo Process Sequence
**File:** `tattoo_process_sequence.png`  
**Dimensions:** 512x256 pixels

### Sketch Sequence:
| Frame | Position | Size | Description |
|-------|----------|------|-------------|
| Reference Photo | (0, 0) | 64x64 | Actual clock skeleton |
| Jakub Drawing 1 | (64, 0) | 64x64 | Starting sketch |
| Jakub Drawing 2 | (128, 0) | 64x64 | Adding "skull" (beak) |
| Jakub Drawing 3 | (192, 0) | 64x64 | Adding scythe |
| Final Sketch | (256, 0) | 64x64 | Obvious duck |
| Sketch Close-Up | (320, 0) | 96x96 | Detail view of duck |

### Tattooing Animation:
| Frame | Position | Size | Description |
|-------|----------|------|-------------|
| Stencil Apply | (0, 64) | 96x64 | Purple transfer |
| Outline Start | (96, 64) | 96x64 | Gun to skin |
| Outline Progress 1 | (192, 64) | 96x64 | Duck emerging |
| Outline Progress 2 | (288, 64) | 96x64 | More duck |
| Outline Complete | (384, 64) | 96x64 | Full duck outline |
| Shading Start | (0, 128) | 96x64 | Adding depth |
| Shading Progress | (96, 128) | 96x64 | Very duck |
| Final Result | (192, 128) | 96x64 | Complete duck with scythe |
| Bandage Apply | (288, 128) | 96x64 | Covering "masterpiece" |

### The Duck Tattoo:
| View | Position | Size | Description |
|------|----------|------|-------------|
| Fresh (Bandaged) | (384, 128) | 64x64 | Just done |
| Healed | (448, 128) | 64x64 | Final appearance |
| On Lord Pilsner's Back | (0, 192) | 96x96 | In-game sprite placement |
| Close-Up Detail | (96, 192) | 96x96 | For post-credits |
| Mirror View (Backwards) | (192, 192) | 64x64 | What LP sees |

---

## ✨ Sprite Sheet 12: Effects
**File:** `shop_effects.png`  
**Dimensions:** 256x192 pixels

### Lighting Effects:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Neon Glow Pink | (0, 0) | 64x64 | Overlay for pink areas |
| Neon Glow Green | (64, 0) | 64x64 | Overlay for beer sign |
| Fluorescent Flicker 1 | (128, 0) | 64x32 | Full brightness |
| Fluorescent Flicker 2 | (128, 32) | 64x32 | Dimmed |
| Fluorescent Flicker 3 | (192, 0) | 64x32 | Off briefly |
| Work Lamp Spot | (192, 32) | 64x64 | Harsh circle |

### Particles:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Dust Mote 1 | (0, 64) | 16x16 | Floating in light |
| Dust Mote 2 | (16, 64) | 16x16 | Variant |
| Dust Mote 3 | (32, 64) | 16x16 | Variant |
| Cigarette Smoke 1 | (48, 64) | 32x48 | Drifting |
| Cigarette Smoke 2 | (80, 64) | 32x48 | Dissipating |
| Autoclave Steam | (112, 64) | 48x48 | Rising |
| Tattoo Gun Sparks | (0, 112) | 32x32 | Optional effect |
| Blood Drop | (32, 112) | 16x16 | Occasional |

---

## 🎮 Sprite Sheet 13: UI Elements
**File:** `euro_ink_ui.png`  
**Dimensions:** 256x192 pixels

### Mini-Game UI:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hold Still Meter | (0, 0) | 128x32 | Flinch prevention gauge |
| Meter Fill (Good) | (0, 32) | 128x16 | Green progress |
| Meter Fill (Bad) | (0, 48) | 128x16 | Red warning |
| Flinch Warning | (128, 0) | 64x32 | "DON'T MOVE!" |
| Perfect Bonus | (128, 32) | 64x32 | "STEADY!" |

### Shop Menu:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Menu Background | (0, 64) | 192x96 | Price list frame |
| Item Highlight | (0, 160) | 192x32 | Selection bar |
| Price Tag | (192, 64) | 48x24 | "€XX" format |
| Sold Out | (192, 88) | 48x24 | Red stamp |

### Dialogue Portraits:
| Portrait | Position | Size | Description |
|----------|----------|------|-------------|
| Jakub Happy | (0, 160) | 48x48 | Default |
| Jakub Proud | (48, 160) | 48x48 | Showing work |
| Jakub Confused | (96, 160) | 48x48 | "Duck? No..." |
| Marta Skeptical | (144, 160) | 48x48 | Default |
| Marta Shrug | (192, 160) | 48x48 | "Usually." |

---

## 🎬 Animation Specifications

### Neon Sign Flicker:
- **Duration:** 3-5 seconds random interval
- **Pattern:** Full → "4" flicker → Full → Whole dim → Full
- **Audio Sync:** Buzzing intensifies during flicker

### Tattoo Gun Animation:
- **Duration:** 0.5 seconds per cycle
- **Frames:** 4
- **Audio Sync:** Buzzing sound loops

### Jakub's Confident Drawing:
- **Duration:** 8 seconds total
- **Frames:** 12
- **Key Frames:** Reference look → Draw → Proud glance → Continue
- **Audio Sync:** Pencil scratching, humming

### Lord Pilsner Pain Reactions:
- **Trigger:** Player fails to hold still
- **Duration:** 0.3 seconds per flinch
- **Recovery:** 1 second to stabilize

---

## ♿ Accessibility Sprite Requirements
**File:** `euro_ink_accessibility.png` (supplemental sheet — delivered alongside the 13 base files, not counted in their total)
**Dimensions:** 384x256 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Hold Still Meter, Bold | (0, 0) | 128x32 | Thick-bordered flinch gauge with enlarged fill area |
| Flinch Warning, Bold | (128, 0) | 96x48 | Oversized "DON'T MOVE!" with heavy outline |
| Shop Menu Highlight, Bold | (224, 0) | 160x32 | High-contrast selection bar for the price list |
| Jakub Interactive Outline | (0, 48) | 64x96 | White-on-dark outline for Jakub's idle/greeting interaction poses |
| Entry Door Outline | (64, 48) | 64x96 | Outlined glass door with enlarged "PUSH" sign |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Neon Sign, Steady | (128, 48) | 192x64 | "EURO INK 4 LESS" at constant glow — no "4" flicker cycle |
| Fluorescent, Steady | (128, 112) | 64x32 | Constant overhead tube, flicker frames disabled |
| Tattoo Gun, Reduced | (192, 112) | 48x32 | Vibration-free gun sprite; spark particles disabled in this mode |
| Beer Sign, Steady | (240, 112) | 96x64 | Pink/green neon at constant glow |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gun Buzz Lines | (0, 144) | 48x32 | Vibration lines around the gun — intensity steps with the buzz volume during the mini-game |
| Record Scratch Icon | (48, 144) | 48x48 | Scratched-disc burst on the duck reveal (Lord Pilsner's internal record scratch) |
| Sad Trombone Icon | (96, 144) | 48x48 | Drooping note on Chadwick's "Bro, that looks like a duck" |
| Heroic Swell Icon | (144, 144) | 48x48 | Rising-notes burst over Lord Pilsner's denial (his perspective) |
| Ka-Ching Icon | (192, 144) | 48x48 | Coin burst at payment / Jakub's Money Counting pose |
| Radio Note Icon | (240, 144) | 48x48 | Tinny-note wisp from the radio; wobbles when Jakub hums along |
| Pain Hiss Indicator | (288, 144) | 48x48 | Sharp inhale lines matching each flinch's hiss-of-pain audio |

### Colorblind Considerations:
- Hold Still meter fill must not rely on green-vs-red alone: Good fill is solid with a check icon, Bad fill is hatched with a warning icon
- Pain Meter faces (Levels 1–5) already carry expression changes, not color-only states — preserve that
- Price tags and Sold Out stamp use text + shape, never color coding alone
- Mini-game tap zone is full-screen width (well beyond the 44px minimum); shop menu rows and dialogue portraits sized 48px+ for touch

---

## 📱 Mobile Optimization

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| euro_ink_environment | Interior, exterior, signage | 1024x1024 |
| euro_ink_characters | Jakub, Marta, LP reactions | 512x512 |
| euro_ink_process | Tattoo sequence, effects | 512x512 |

### Performance Notes:
- Simple single-room interior
- Focus on character animation quality over environmental complexity
- Mini-game requires responsive 60fps
- Limit particles to dust and occasional smoke

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Single-room scene; AnimatedSprite2D for the tattoo process sequence and Jakub's drawing loop; CPUParticles2D (not GPU) for dust motes, cigarette smoke, autoclave steam
- Neon and fluorescent flicker via simple alpha toggle timers (no shaders); flicker timers disabled when reduced-motion mode is active
- "Hold Still" mini-game: full-screen InputEventScreenTouch tap zone at a locked 60fps; flinch count writes `tattoo_quality` (wobblier duck = funnier, per design)
- The finished duck composites permanently onto Lord Pilsner's base sprite — the tattoo layer must export as a separate alpha-masked overlay for global reuse across the rest of the game
- State tracking per `euro_ink_4_less_state` (tattoo_acquired, tattoo_quality, jakub_friendship, lord_pilsner_special_unlocked, matching_ducks_offered, times_jakub_encountered_in_other_cities)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Tattoo Gun frames (0.5s cycle) | Gun buzzing loop | Buzz starts on Outline Start frame, stops on Bandage Apply |
| Jakub's Confident Drawing (12 frames, 8s) | Pencil scratching + humming | Humming swells on the "proud glance" key frame |
| Duck Reveal / Mirror View | Record scratch (internal), triumphant horn (Jakub's POV) | Both on the hand-mirror raise frame — the collision is the joke |
| "It's a duck" beat | Subtle sad trombone | On Chadwick's dialogue line |
| Lord Pilsner Defensive pose | Heroic music swell | On "It's ARTISTIC INTERPRETATION" |
| Jakub Money Counting | Cash register + satisfied grunt | On pose entry |
| Neon Sign Flicker | Transformer buzz intensifies | During flicker frames only |
| Pain Flinch 1–3 | Hiss of pain | Per flinch, 0.3s |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Tramp Stamp | Full tattoo_process_sequence, lord_pilsner_reactions, jakub_artist, mini_game UI | Entry requires `tattoo_decision_made` from Astronomical Cock-Up Square; barker referral funnels the crying Lord Pilsner here |
| The Lord Pilsner Special (unlock) | Shop menu + price tag sprites, framed duck photo (added to Wall of Fame) | Menu item appears after the bros' visit; referenced in ALL other Euro Ink locations |
| Matching Ducks (return visits) | Jakub Greeting/Proud portraits, flash_art_wall duck designs | Jakub offers matching ducks for Chadwick and Bradley on return |
| Post-Credits Twin Peaks Reveal | Duck Tattoo Close-Up Detail sprite | Final reveal to "Amber"; sprite must hold up at dialogue-scene scale |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Astronomical Cock-Up Square | exterior_alley.png and neon_signage.png must match the square's Euro Ink facade + Neon Sign (Sheet 11 of that spec) | Alley walk from the square, pink glow spill |
| 24-Hour Kebab Shop / Currency Exchange | Adjacent facades in exterior_alley.png | Static neighbors, lit signage |
| Velvet Curtain Club | Duck tattoo overlay visible on LP's sprite during the show-off scene (nobody cares) | Item/cosmetic persistence |
| Hostel | Bandaged → infected tattoo states as running bit dressing | Cosmetic state progression |
| Publandia / Sinfonia / Shamsterdam | Jakub's shop variants (Shamrock Ink, Opera Ink, Euro Ink 4 Less - Shamsterdam) reuse this interior kit with re-skinned signage and flash art | Cross-city asset family |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Confident incorrectness rendered in permanent ink, under fluorescent light"
- **Color Mood:** Neon Pink ambition against Clinical White pretension, undercut by Dingy Gray floors and Nicotine Yellow ceiling stains
- **Lighting:** Harsh flickering fluorescent overhead, pink/green beer-sign accents, one brutal white work-lamp spotlight on the chair
- **Texture:** Sticky-looking cracked linoleum, duct-taped vinyl chair, faded flash sheets, home-printed paper "credentials"

### Environmental Storytelling:
- The credentials wall tells the whole story: "Online Tattoo Academy - 3 Week Course - 2019" certificate, license expired 2019 and clearly home-printed, "HYGENIC" misspelled on the window
- Every flash design has subtle duck qualities — the wall is foreshadowing (dragons that look like geese, a skull with a beak somehow)
- The Wall of Fame's customers all look uncertain; the guestbook is suspiciously empty; the clock is stuck at 4:20 (unintentionally — just broken)
- The reference photo vs. Jakub's Interpretation pair (Sheet 4) is the location's thesis in two 96x96 sprites

### Character Integration Notes:
- Jakub reads as warm and sincere in every pose — he is a true believer, never a villain; his Confused pose ("Duck? No, is skeleton.") is genuine bafflement
- Marta is present ~50% of visits; her sheet is intentionally minimal (skepticism needs few frames)
- Lord Pilsner's reaction sheet carries the scene's emotional arc: excitement → pain → backwards-mirror joy → defensiveness

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Shop Sign** - "EURO INK 4 LESS" with the flickering "4"
2. **The Design "Review"** - Jakub proudly presenting the duck sketch as "skeleton"
3. **The Reveal** - First glimpse of the duck, hand mirror at an awkward angle
4. **Chadwick's Line** - "Bro, that looks like a duck"
5. **The Certificate** - "Online Tattoo Academy - 3 Week Course - 2019"
6. **Flash Art Wall** - Every single design slightly duck-like

### Quote Potential:
- "Is skeleton. Very death. Much bone."
- "In my country, death is sometimes duck. Is metaphor."
- "It's ARTISTIC INTERPRETATION. Europeans do things different."
- "When duck holds scythe, winter comes."
- "No appointment. No regrets. Mostly no regrets."

---

## 📋 Required PNG Files (13 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | shop_interior_complete.png | 1024x512 |
| 2 | exterior_alley.png | 512x384 |
| 3 | neon_signage.png | 384x256 |
| 4 | flash_art_wall.png | 512x512 |
| 5 | jakub_artist.png | 512x384 |
| 6 | marta_assistant.png | 256x192 |
| 7 | lord_pilsner_reactions.png | 384x256 |
| 8 | tattoo_station.png | 384x256 |
| 9 | reception_counter.png | 256x192 |
| 10 | waiting_area.png | 256x192 |
| 11 | tattoo_process_sequence.png | 512x256 |
| 12 | shop_effects.png | 256x192 |
| 13 | euro_ink_ui.png | 256x192 |

**Total Estimated Memory:** ~20MB

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `shop_interior_complete.png` (1024x512)
- [ ] `exterior_alley.png` (512x384)
- [ ] `neon_signage.png` (384x256)
- [ ] `flash_art_wall.png` (512x512)
- [ ] `jakub_artist.png` (512x384)
- [ ] `marta_assistant.png` (256x192)
- [ ] `lord_pilsner_reactions.png` (384x256)
- [ ] `tattoo_station.png` (384x256)
- [ ] `reception_counter.png` (256x192)
- [ ] `waiting_area.png` (256x192)
- [ ] `tattoo_process_sequence.png` (512x256)
- [ ] `shop_effects.png` (256x192)
- [ ] `euro_ink_ui.png` (256x192)
- [ ] `euro_ink_accessibility.png` (384x256, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (duck tattoo overlay on its own alpha-masked layer — it composites onto Lord Pilsner's sprite for the rest of the game)
- **Documentation:** Animation timing reference sheet (tattoo gun cycle, Jakub's 8-second drawing, flinch/recovery windows)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Neon Pink #FF1493, Clinical White #F5F5F5, Neon Green #7FFF00, Nicotine Yellow #F5DEB3)
- [ ] The final tattoo is visually, undeniably a duck — at every zoom level, including the 64x64 healed state
- [ ] Reference photo reads as skeleton; Jakub's sketch reads as duck; the gap between them is the joke
- [ ] Certificate, expired license, and "HYGENIC" sticker text readable on examine
- [ ] Accessibility visual alternatives included for all audio cues (gun buzz, record scratch, trombone, ka-ching)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (mutual confident delusion, not malice) is clear throughout all assets — Jakub must read warm, never sinister
- [ ] Every flash art design carries subtle duck qualities (foreshadowing requirement from design notes)
- [ ] Mobile performance optimized (single room, alpha-toggle flickers, dust/smoke particle caps)
- [ ] Touch zone sizing considered (44px minimum — full-screen mini-game tap zone, 48px menu rows)
- [ ] Colorblind-friendly alternatives available where color codes meaning (hatched/iconed meter fills, never green-vs-red alone)
- [ ] Social media viral potential maximized (reveal composition, certificate close-up framing)

---

## ✅ Validation Status

| Requirement | Status |
|-------------|--------|
| World Consistency | ✅ PASS |
| Cultural Specificity | ✅ PASS |
| Satirical Targets | ✅ PASS |
| Gameplay Value | ✅ PASS |
| No Crypto Elements | ✅ PASS |
| Mobile Optimization | ✅ PASS |
| Seedy Underbelly Present | ✅ PASS (permanent decisions made in emotional states) |
| Technical Feasibility | ✅ PASS (single room, character-animation focus) |
| Mobile Performance Budget | ✅ PASS (60 FPS, 10-15 draw calls, 20MB) |
| Accessibility Features | ✅ PASS (visual buzz/reveal cues, steady-light variants) |
| Social Media Integration | ✅ PASS (viral moments identified) |

---

**Euro Ink 4 Less delivers the visual comedy of watching a duck emerge from confident artistic intention. Jakub's sincere belief in his own skill, combined with Lord Pilsner's desperate need to validate his "authentic European experience," creates a perfect storm of permanent regret rendered in careful pixel art. The duck tattoo becomes a running visual gag visible on Lord Pilsner's sprite throughout the rest of the game, culminating in the post-credits Twin Peaks reveal.**
