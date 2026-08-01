# Venustempel - Complete PNG Asset Requirements

## 📋 Overview
Venustempel is the world's first sex museum, groundbreaking in 1985 and dated since roughly 1986, where €5 buys you a Victorian mannequin that lifts its skirts on a motion sensor, a coin-operated flip-card machine that was scandalous in 1890, and the genuine surprise that John Lennon drew erotic sketches. This document specifies every PNG asset for the museum: the art-deco storefront with its permanently half-flickering neon Venus, three cramped canal-house floors of mechanical curiosity, the Giggling Figure and its pneumatic inevitability, the photo-op stations nobody will post, Anke's fifteen years of total immunity, and the gift shop you have to walk through. Its satirical essence in a sentence: tourists arrive expecting titillation, receive Victorian machinery, and leave with photographs they will keep forever and show to no one.

**Location ID:** `shamsterdam_roodelicht_venustempel_01`
**Theme:** The gap between "edgy Amsterdam museum" expectations and "mechanical mannequin in a cramped canal house" reality — group awkwardness as the actual exhibit
**Zone:** Roodelicht Row, directly on the main tourist corridor, between a waffle shop and a souvenir store
**Hours:** 10 AM - 11 PM (school groups 10 AM-2 PM, bachelor parties 4-8 PM, quiet couples 8-11 PM)
**Primary Function:** Museum / photo-consequence system — the Giggling Figure encounter, coin-operated peep show devices, five photo-op stations with postability ratings, the Venus Temple Collection privacy-flagged album, and the John Lennon knowledge unlock

**Content Handling Note:** Every asset in this specification depicts machinery, mannequins, framed historical artefacts, signage, and visitor reactions. No sprite in this document depicts explicit content. The comedy is entirely mechanical, architectural, and social — the museum's own presentation and the group dynamics around it.

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Venus Red | #DC143C | Door, ground floor wash, signage, velvet |
| Velvet Purple | #800080 | Curtains, upholstery, upper floor accents |
| Vintage Cream | #FFF8DC | Placards, Victorian paper, mannequin fabric |
| Neon Pink | #FF69B4 | Exterior Venus outline, UV accents, gift shop |
| Brass Mechanism | #B08D57 | Mutoscope bodies, coin slots, pneumatic fittings |
| Canal House Dark | #241A22 | Low ceilings, stair shadow, deliberate dim corners |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/venustempel/
├── environment/
│   ├── venustempel_floors_a.png
│   ├── venustempel_floors_b.png
│   └── venustempel_exhibits.png
├── objects/
│   └── venustempel_animated_objects.png
├── npcs/
│   ├── npc_venustempel_staff.png
│   └── npc_venustempel_visitors.png
├── effects/
│   └── venustempel_effects.png
└── ui/
    └── venustempel_ui.png
```

---

## 🕰️ Sprite Sheet 1: Floors A — Ground Floor (Victorian) & First Floor (20th Century)
**File:** `venustempel_floors_a.png`
**Dimensions:** 2048x1024 pixels (paired room backgrounds, streamed — only one floor sheet resident at a time)
**Color Palette:** #DC143C, #FFF8DC, #B08D57, #241A22

### Room Backgrounds:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ground Floor — Victorian Era | (0, 0) | 1024x1024 | Cramped canal-house entry under red and pink wash: the Giggling Figure positioned immediately inside where it cannot be avoided, a row of coin-operated mutoscopes along the left wall, framed historical prints, 1800s medical diagrams that are more alarming than anything else in the building, the chastity belt case, low ceilings, creaky stairs rear-right, and a bench |
| First Floor — 20th Century | (1024, 0) | 1024x1024 | Slightly brighter: the Marilyn Monroe statue over its subway grate, the John Lennon sketch display (easy to miss, genuinely the most interesting thing here), vintage pin-up collection, early film room with a looping screen, the 1970s section, and "modern art" sculptures that make everyone tilt their head |

### Technical Notes:
- Anchor points (Ground): Giggling Figure at (288, 640), mutoscope row at (128, 576) / (128, 768), chastity case at (576, 512), print wall at (768, 448), medical diagrams at (832, 640), bench at (640, 832), stairs at (896, 576)
- Anchor points (First): Marilyn at (1280, 576), Lennon display at (1600, 512), pin-up wall at (1856, 480), film room screen at (1408, 768), 1970s wall at (1728, 768), sculptures at (1920, 704)
- Both floors share one 8.39 MB texture and stream together as the lower pair
- The Giggling Figure's position must make it unavoidable from the door in any camera framing — the layout is the joke and the layout is load-bearing
- The John Lennon display is deliberately under-lit and positioned off the main sightline; discovering it should feel like the player found something
- Ceilings are painted low enough that any 96px character sprite reads as slightly cramped on both floors

---

## 📸 Sprite Sheet 2: Floors B — Second Floor (Photo Ops) & Gift Shop / Mirror Maze
**File:** `venustempel_floors_b.png`
**Dimensions:** 2048x1024 pixels (paired room backgrounds, streamed)
**Color Palette:** #800080, #FF69B4, #FFF8DC, #241A22

### Room Backgrounds:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Second Floor — Photo Ops | (0, 0) | 1024x1024 | "Experience The Temple": The Throne centred as the mandatory group photo spot, costume corner rack (€5), the swing with its small "for display only" sign, wax figures in legally-distinct poses, green screen station (€10), constant flash photography, gift shop visible ahead and pulling you forward |
| Gift Shop & Mirror Maze | (1024, 0) | 1024x1024 | Cramped retail wedged into the exit path, shelving to the ceiling, postcards, discreet packaging behind the counter, gift wrapping station — with the short, disorienting mirror maze passage feeding into it from the left, reflecting things you would rather not see reflected |

### Technical Notes:
- Anchor points (Second Floor): Throne at (512, 640), costume rack at (192, 576), swing at (768, 512), green screen at (896, 704), wax figures at (320, 512), exit toward shop at (960, 896)
- Anchor points (Gift Shop): counter at (1728, 768), shelving runs at (1280, 576) / (1600, 512), maze entrance at (1088, 640), maze exit at (1408, 832), postcard spinner at (1536, 704)
- The mirror maze occupies the left third of the gift shop room rather than a separate scene; its reflective panels are authored as a tileable element (Sheet 3) so the passage can be assembled at any length
- The gift shop must visibly obstruct the exit — there is no bypass route in the layout and there must be no bypass route in the art
- Second floor is the brightest room in the building because it is where the cameras are

---

## 🎭 Sprite Sheet 3: Exhibits & Fixtures
**File:** `venustempel_exhibits.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #DC143C, #800080, #B08D57, #FFF8DC

### Exterior & Ground Floor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Venustempel Exterior | (0, 0) | 384x512 | Narrow storefront, red door with golden Venus symbol, velvet curtain in the window, tourists photographing the sign |
| Giggling Figure (Static / Rest) | (384, 0) | 256x384 | Life-sized Victorian mannequin in its resting state, skirts down, mechanism dormant, entirely innocent-looking |
| Peep Show Device (Mutoscope) | (640, 0) | 192x256 | Coin-operated Victorian flip-card viewer, brass body, original |
| Marilyn Monroe Statue (Rest) | (832, 0) | 192x384 | Standing over the subway grate, dress down, waiting for the timer |
| Coin Slot Detail | (640, 256) | 96x128 | €0.50 per viewing, brass, worn smooth |
| Coin Collection Tray | (736, 256) | 96x128 | Change from the ticket desk lives here |
| Chastity Belt Display | (384, 384) | 256x128 | Real artefacts, questionable provenance, universally photographed |
| Historical "Art" Frames | (640, 384) | 192x128 | Framed prints that would have been contraband 150 years ago |
| Medical Diagrams (1800s) | (832, 384) | 192x128 | "Educational" anatomy charts, more terrifying than titillating |

### First & Second Floor Exhibits:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| John Lennon Sketch Display | (0, 512) | 192x256 | Yes, really. He drew these. The most genuinely interesting exhibit in the building. |
| Vintage Pin-Up Collection | (192, 512) | 192x256 | From tasteful to "what decade was this acceptable" |
| Early Film Room Screen | (384, 512) | 192x128 | Looping clips from the earliest adult cinema. Surprisingly boring. |
| 1970s Section Wall | (576, 512) | 192x128 | An aesthetic that has not aged well, and is fascinating for exactly that reason |
| "Modern Art" Sculptures | (768, 512) | 128x256 | Head-tilt inducing. "Huh." |
| Wax Figures (Legally Distinct) | (896, 512) | 128x256 | Celebrities. Allegedly. Legally distinct. Allegedly. |
| The Throne | (384, 640) | 256x128 | Oversized chair. Mandatory group photo spot. Bradley will not be sitting on that. |
| Red Velvet Curtain (Tileable) | (640, 640) | 128x128 | Seamless vertical drape run, all floors |

### Mirror Maze, Gift Shop & Signage:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mirror Maze Panel (Tileable) | (0, 768) | 128x128 | Reflective panel, seamless, assembles into any passage length |
| Mirror Maze Corner Piece | (128, 768) | 128x128 | 90° junction with double reflection |
| Costume Corner Rack | (256, 768) | 192x128 | €5 rental accessories for "artistic" photos |
| Green Screen Station | (448, 768) | 192x192 | €10 printed composite into "classic" scenes |
| The Swing ("For Display Only") | (640, 768) | 128x192 | The sign is small. It is still for display only. |
| Gift Shop Shelving (Cramped) | (768, 768) | 256x192 | Floor to ceiling, aggressively stocked, judgement-free |
| Bench | (0, 896) | 128x128 | "If you need to sit down after the Giggling Figure, there's a bench." |
| Ticket Desk + Cross-Stitch | (128, 896) | 128x128 | €5, cash or card, coins for the machines, Anke's project |
| Neon Venus Outline | (256, 896) | 96x128 | Pink, always on, always flickering slightly |
| "ADULTS ONLY" Sign | (352, 896) | 96x64 | Font suggests this was added later |
| "Educational Exhibits" Plaque | (352, 960) | 96x64 | Sure |
| Art Deco "VENUSTEMPEL" Sign | (448, 960) | 192x64 | Attempting class, achieving it, mostly |
| Creaky Wooden Stairs | (640, 960) | 128x64 | The building is old and says so constantly |
| Victorian Music Box | (768, 960) | 128x64 | Ground floor ambient source, period appropriate |
| Museum Floor Tile (Tileable) | (896, 960) | 128x64 | Worn canal-house board, seamless all edges |

### Technical Notes:
- The Giggling Figure at rest must look completely harmless; nothing in the static sprite may telegraph the mechanism. First-encounter comedy depends entirely on this.
- Mirror Maze Panel and Corner Piece must tile without visible seams in the reflection, and the reflection content is a separately-authored low-detail ghost layer (Sheet 7) rather than a real render
- Red Velvet Curtain, Mirror Maze Panel, and Museum Floor Tile are the location's three tiled assets
- All signage and placards are baked at 2x internal resolution and flagged for the ASTC 4x4 exception list
- The John Lennon display frame is authored with a subtle extra highlight so a player who slows down finds it — a discoverability affordance, not a UI marker

---

## ⚙️ Sprite Sheet 4: Animated Mechanisms
**File:** `venustempel_animated_objects.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #FFF8DC, #B08D57, #DC143C, #800080

### The Giggling Figure Cycle:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Giggling Figure Frame 1 | (0, 0) | 256x384 | Mechanism engages, skirts begin to lift, the clicking has already started |
| Giggling Figure Frame 2 | (256, 0) | 256x384 | Mid-lift, pneumatic, unstoppable |
| Giggling Figure Frame 3 | (512, 0) | 256x384 | Full extent, recorded giggle plays, everyone jumps |
| Giggling Figure Frame 4 | (768, 0) | 256x384 | Descent, mechanism resets, thirty seconds until the next one |

### The Marilyn Cycle & Mechanism Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marilyn Dress Billow Frame 1 | (0, 384) | 192x384 | Grate activates |
| Marilyn Dress Billow Frame 2 | (192, 384) | 192x384 | Rising |
| Marilyn Dress Billow Frame 3 | (384, 384) | 192x384 | Full billow, the photograph everyone takes |
| Marilyn Dress Billow Frame 4 | (576, 384) | 192x384 | Settling, thirty-second reset |
| Motion Sensor Trigger Zone | (768, 384) | 96x96 | Dev/accessibility visualisation of the Giggling Figure's detection radius |
| Mechanical Clicking Indicator | (864, 384) | 96x96 | The pre-activation tell; learn to anticipate |
| Pneumatic Hiss Plate | (960, 384) | 64x96 | Air release visualisation |

### Peep Show Flip Cards (Tasteful Victorian Silhouettes):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Flip Card Frame 1 | (768, 480) | 128x64 | Victorian silhouette animation, frame 1 |
| Flip Card Frame 2 | (896, 480) | 128x64 | Frame 2 |
| Flip Card Frame 3 | (768, 544) | 128x64 | Frame 3 |
| Flip Card Frame 4 | (896, 544) | 128x64 | Frame 4 |
| Flip Card Frame 5 | (768, 608) | 128x64 | Frame 5 |
| Flip Card Frame 6 | (896, 608) | 128x64 | Frame 6 |
| Flip Card Frame 7 | (768, 672) | 128x64 | Frame 7 |
| Flip Card Frame 8 | (896, 672) | 128x64 | Frame 8 — thirty seconds total, then it stops, and you consider another coin |

### Accessibility & Reduced Motion Variants:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Giggling Figure High-Contrast Silhouette | (0, 768) | 256x256 | Bold outline variant of the location's key interactive |
| Marilyn High-Contrast Silhouette | (256, 768) | 192x256 | Bold outline variant of the second photo station |
| Static Giggling Figure (Reduced Motion) | (448, 768) | 256x256 | Locked to frame 1; no lift, no jump-scare, the giggle audio and glyph still play |
| Static Marilyn (Reduced Motion) | (704, 768) | 192x256 | Locked to rest; the photo station still functions |
| Peep Show Static Card | (896, 768) | 128x64 | Single-frame substitute for the flip animation |
| Camera Flash Effect | (896, 832) | 128x128 | Tourist flash simulation, additive |
| Reserve | (896, 960) | 128x64 | Reserved cell, do not paint |

### Technical Notes:
- The Giggling Figure's four frames must be readable as *mechanical* rather than lifelike — visible pneumatic strut, slight jerkiness, and 1985 build quality. The joke is that it is a machine, not a person.
- Flip cards depict Victorian-era silhouettes only, in the style of period mutoscope reels; they are tame by any modern standard and that is the punchline the game explicitly makes
- Motion Sensor Trigger Zone ships as a real asset because it is used both by the accessibility "show interaction zones" option and by the anticipation tell after the first encounter
- Both mechanisms reset on a hard 30-second timer with no randomisation — predictability is required for the "learn to anticipate" gag to land

---

## 🧵 Sprite Sheet 5: Museum Staff
**File:** `npc_venustempel_staff.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 per character frame; 128x128 per portrait
**Color Palette:** #DC143C, #FF69B4, #FFF8DC

### Ticket Seller Anke — Fifteen Years of Immunity:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Anke Ticket Seller Idle | (0, 0) | 64x96 | Middle-aged Dutch, reading glasses, entirely unfazed |
| Anke Cross-Stitch | (64, 0) | 64x96 | Between customers. Always between customers. |
| Anke Coin Exchange | (128, 0) | 64x96 | "Coins for the machines are there." |
| Anke Deadpan Frame 1 | (192, 0) | 64x96 | Has heard every possible reaction |
| Anke Deadpan Frame 2 | (256, 0) | 64x96 | Is immune to all of them |
| Anke "You will also jump." | (320, 0) | 64x96 | Not a warning. A prediction. Accurate. |
| Anke Lennon FAQ | (384, 0) | 64x96 | "Yes, the John Lennon. Yes, really. I get that question a lot." |
| Anke "I know what we sell." | (448, 0) | 64x96 | Regarding the gift shop. Total equanimity. |

### Floor Attendant Willem:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Willem Floor Attendant Idle | (0, 96) | 64x96 | Young Dutch, museum polo, "this is my summer job" |
| Willem Intervention Frame 1 | (64, 96) | 64x96 | Approaching |
| Willem Intervention Frame 2 | (128, 96) | 64x96 | "Please don't touch the exhibits." |
| Willem "Display only." | (192, 96) | 64x96 | "I know the sign is small. It's still for display only." |
| Willem Suppressed Smile | (256, 96) | 64x96 | Professional neutrality, briefly failing |
| Willem Bench Suggestion | (320, 96) | 64x96 | "Many people use the bench." |
| Willem Mirror Maze Reassurance | (384, 96) | 64x96 | "You will find your way out. Eventually." |
| Willem at Lennon Display | (448, 96) | 64x96 | "Yes, really. I don't know why either. But yes." |

### Portraits & Petra:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Anke Portrait (Dialogue) | (0, 192) | 128x128 | Fifteen years. Cross-stitch. Nothing left to surprise her. |
| Willem Portrait (Dialogue) | (128, 192) | 128x128 | Professionally neutral, occasionally human |
| Petra Portrait (Dialogue) | (256, 192) | 128x128 | Cheerful, pink apron, gift-wrapping ribbon in her hair |
| Petra Gift Shop Idle | (384, 192) | 64x96 | Aggressively helpful |
| Petra Gift Wrapping | (448, 192) | 64x96 | "No judgment. Very discreet packaging available." |
| Reserve / Atlas Padding | (384, 288) | 128x32 | Reserved strip, do not paint |

### Petra & Staff Extras:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Petra Best Seller Pitch | (0, 320) | 64x96 | "People say 'ironic gifts' but they buy two so..." |
| Petra Discreet Packaging | (64, 320) | 64x96 | Plain paper, no branding, entirely routine |
| Petra Postcard Recommendation | (128, 320) | 64x96 | "Yes, you can mail them. Yes, people do mail them." |
| Petra "We'll be here when you're ready." | (192, 320) | 64x96 | Since 1985. Delivered warmly. |
| Willem Casual Eye (Solo Traveler) | (256, 320) | 64x96 | Everything's probably fine |
| Willem Crowd Management | (320, 320) | 64x96 | Bachelor party containment posture |
| Anke Coin Count | (384, 320) | 64x96 | "Three euros? That's six viewings. You're sure?" |
| Anke First-Timer Warning | (448, 320) | 64x96 | "The figure is right there. No, you can't avoid it. Good luck." |

### Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Anke High-Contrast Silhouette | (0, 416) | 64x96 | Accessibility outline variant |
| Willem High-Contrast Silhouette | (64, 416) | 64x96 | Accessibility outline variant |
| Petra High-Contrast Silhouette | (128, 416) | 64x96 | Accessibility outline variant |
| Ticket Desk Pose (Anke) | (192, 416) | 64x96 | Behind-counter anchor pose |
| Accessibility Reserve Block | (256, 416) | 256x96 | Reserved for high-contrast/audio-cue glyph overflow |

### Technical Notes:
- Anke's two Deadpan frames must be functionally identical; the immunity is the characterisation and it must be visually total
- Willem's Suppressed Smile is the only frame in the staff set with any visible reaction, and it fires rarely — reserve it for the best tourist moments
- Petra treats every transaction as completely normal in every frame; no knowing looks, no winks. Her cheerfulness is sincere and that is what makes the gift shop funny.

---

## 👥 Sprite Sheet 6: Visitors
**File:** `npc_venustempel_visitors.png`
**Dimensions:** 1024x256 pixels
**Sprite Size:** 64x96 per single NPC frame; 128x128 per portrait
**Color Palette:** Mixed tourist palette, red-wash and purple ambient grades

### Visitors:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bachelor Party (British) | (0, 0) | 256x96 | Six lads, matching "GARY'S LAST STAND" shirts, one recording everything |
| Gary (Reluctant) | (256, 0) | 64x96 | "GARY. GARY. Sit on the throne. For the LADS. GARY." |
| Couple on Holiday | (320, 0) | 128x96 | Guidebook visible, treating it academically, one of them actually reading |
| Solo Traveler (Suspicious) | (448, 0) | 64x96 | No camera. Just looking. Doesn't laugh at anything. Probably fine. |
| Teenager Who Got In | (512, 0) | 64x96 | Definitely not 18, alternating between shock and performed boredom |
| School Group (Art History) | (576, 0) | 192x96 | Clipboards, notes, professor-managed nervous giggling |
| Professor with Clipboard | (768, 0) | 64x96 | "Note the mechanical innovation required for this period. Stay focused." |
| Bros Trio | (832, 0) | 192x96 | Lord Pilsner / Chadwick / Bradley, pre-composed |

### Portraits & Reaction Strips:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Jump-Scare Reaction Strip | (0, 96) | 256x96 | Four 64x96 stages: unaware / click heard / full jump / recovery |
| Bachelor Party Portrait | (256, 96) | 128x128 | Competitive edginess, visibly effortful |
| Couple Portrait | (384, 96) | 128x128 | "It says this is from 1847. That's actually fascinating when you think about—" |
| Teenager Portrait | (512, 96) | 128x128 | "This is... this is whatever. I've seen... whatever." (Has not seen.) |
| Photo Op Pose Strip | (640, 96) | 256x96 | Four 64x96 poses: throne / Marilyn recreation / costume / green screen |
| Composure-Maintenance Strip | (896, 96) | 128x96 | Two 64x96 frames: holding it together / not holding it together |

### Ambient:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gift Shop Crowd Silhouette | (0, 192) | 256x64 | Cramped retail depth |
| Floor Crowd Silhouette | (640, 192) | 256x64 | Exhibit floor depth, low ceiling clearance |
| Accessibility Reserve | (896, 192) | 64x64 | Reserved for high-contrast marker |
| Bench Occupant (Recovering) | (960, 192) | 64x64 | Many people use the bench |
| Portrait Band Padding | (256, 224) | 384x32 | Reserved padding, do not paint |

### Technical Notes:
- Bachelor Party, School Group, and Bros Trio all ship as pre-composed blocks to protect the 16-draw-call budget
- Jump-Scare Reaction Strip is palette-modulated onto any visitor and fires for every NPC in the Giggling Figure's radius simultaneously — the collective jump is funnier than any individual one
- Photo Op Pose Strip is reused across all five stations; the station art supplies the context, the pose supplies the awkwardness
- The Solo Traveler must be composed as genuinely ambiguous — not sinister, not obviously academic. The discomfort is the group's projection.

---

## ✨ Sprite Sheet 7: Effects — Flash, Red Light & Mechanism
**File:** `venustempel_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #DC143C, #FF69B4, #800080, #B08D57

### Light & Photography:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Camera Flash Burst Frame 1 | (0, 0) | 64x64 | Tourist flash, constant on the second floor |
| Camera Flash Burst Frame 2 | (64, 0) | 64x64 | Falloff |
| Red Light Wash Plate | (128, 0) | 64x64 | Ground floor signature grade |
| Pink Neon Flicker Frame 1 | (192, 0) | 64x64 | Exterior Venus outline |
| Pink Neon Flicker Frame 2 | (256, 0) | 64x64 | The slight, permanent, never-fixed flicker |
| Spot Lighting Pool | (320, 0) | 64x64 | Per-exhibit display spot |
| UV Accent Glow | (384, 0) | 64x64 | Second floor and mirror maze accent |
| Dust Motes (Old Building) | (448, 0) | 64x64 | Authenticity, suspended |

### Mechanism & Reaction:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mirror Maze Fog | (0, 64) | 64x64 | Subtle, disorienting, short-lived |
| Mirror Reflection Ghost | (64, 64) | 64x64 | Low-detail reflected silhouette layer for maze panels |
| Pneumatic Hiss Puff | (128, 64) | 64x64 | The Giggling Figure's mechanism venting |
| Mechanical Click Spark | (192, 64) | 64x64 | The pre-activation tell, visible as well as audible |
| Coin Drop Glint | (256, 64) | 64x64 | €0.50 entering a mutoscope |
| Jump-Scare Vignette | (320, 64) | 64x64 | Brief edge darkening on first Giggling Figure encounter only |
| Embarrassment Flush Overlay | (384, 64) | 64x64 | Character-parented, for the -Composure state |
| Composure Meter Wobble | (448, 64) | 64x64 | UI-adjacent wobble plate |

### Grades & Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ground Floor Victorian Wash | (0, 128) | 128x128 | Full-scene red multiply plate |
| First Floor Modern Wash | (128, 128) | 64x64 | Slightly brighter, screens glowing |
| Second Floor Photo Op Wash | (192, 128) | 64x64 | Brightest floor, flash-friendly |
| Gift Shop Wash | (256, 128) | 64x64 | Pink, cheerful, commercial |
| Mirror Maze Wash | (320, 128) | 64x64 | UV-tinted, reflective, brief |
| Giggle Glyph | (384, 128) | 32x32 | Mirrors the signature recorded giggle |
| Pneumatic Hiss Glyph | (416, 128) | 32x32 | Mirrors the mechanism venting |
| Mechanical Click Glyph | (448, 128) | 32x32 | Mirrors the pre-activation clicking — the anticipation cue |
| Camera Shutter Glyph | (480, 128) | 32x32 | Mirrors constant tourist photography |
| Coin Clunk Glyph | (128, 192) | 32x32 | Mirrors coin insertion |
| Flip Card Glyph | (160, 192) | 32x32 | Mirrors the mutoscope card flipping |
| Marilyn Whoosh Glyph | (192, 192) | 32x32 | Mirrors the dress mechanism |
| Music Box Glyph | (224, 192) | 32x32 | Mirrors the ground floor Victorian music box |
| Stair Creak Glyph | (256, 192) | 32x32 | Mirrors the old wooden stairs |
| Static Neon (Reduced Motion) | (288, 192) | 64x64 | Steady exterior Venus outline |
| No-Flash Plate (Reduced Motion) | (352, 192) | 64x64 | Photography without the burst |
| Static Fog (Reduced Motion) | (416, 192) | 64x64 | Motionless mirror maze atmosphere |
| Reserve | (480, 192) | 32x64 | Reserved cell, do not paint |

### Technical Notes:
- The Mechanical Click Spark and its glyph are the anticipation system: after the first encounter, both fire ~1.2 seconds before the Giggling Figure activates, converting the jump scare into a comedy of dread
- Jump-Scare Vignette fires exactly once per save file, on the first encounter only
- Mirror Reflection Ghost is a low-detail silhouette layer, not a real-time reflection; it renders at 40% alpha behind each maze panel
- Camera Flash bursts fire from ambient NPCs on a randomised 4-9 second interval on the second floor; they are capped at three simultaneous instances

---

## 🧭 Sprite Sheet 8: UI Elements
**File:** `venustempel_ui.png`
**Dimensions:** 512x512 pixels
**Color Palette:** #DC143C UI chrome, #800080 panel fill, #FF69B4 highlights

### Photography System:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Photo Station Popup | (0, 0) | 192x128 | "Take Photo?" interface with station name and cost |
| Photo Op Station Table | (192, 0) | 192x128 | Five stations with their honest postability ratings (0% / 15% / 5% / 0% / never) |
| Coin Insertion Prompt | (384, 0) | 128x64 | €0.50 per mutoscope viewing |
| Peep Show Coin UI | (384, 64) | 128x64 | Remaining coins and viewings, thirty seconds each |
| Photo Album (Venus Temple Collection) | (0, 128) | 256x128 | Privacy-flagged sub-album, separate from the main photo album |
| Privacy Warning Panel | (256, 128) | 128x96 | "Cannot show to certain NPCs" with the named exclusion list |
| Sensitive Content Flag | (384, 128) | 128x32 | Per-photo marker |
| Unexplainable Photo Item Card | (384, 160) | 128x64 | Key item, cannot be discarded, sourced from The Throne |

### Stations & Composure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Costume Rental Panel | (256, 224) | 128x96 | €5, accessorised portraits, +Regret |
| Green Screen Panel | (384, 224) | 128x96 | €10 printed composite, +Artifact, never shown to anyone |
| Composure Meter | (0, 256) | 128x64 | Temporary state after the Giggling Figure; recovers on the bench |
| Jump-Scare Result Panel | (128, 256) | 128x64 | First encounter outcome with the -Composure application |

### Knowledge & Achievements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Knowledge Unlock: Lennon | (0, 320) | 256x64 | "Did you know John Lennon drew erotic sketches?" dialogue option added |
| Lennon Dialogue Reaction Split | (256, 320) | 256x64 | 70% disbelief / 20% "I knew that" / 10% extremely interested, shown as a stacked bar with labels |
| Temple Tourist Achievement Strip | (0, 384) | 320x64 | Five 64x64 badges: Entered / Jumped / Photographed / Lennon / Temple Tourist |
| Museum Ticket UI (€5) | (320, 384) | 96x64 | Suspiciously cheap, explained by what is inside |
| Coin Purse | (416, 384) | 96x64 | €0.50 units for the machines |

### Status & Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Status Icon Row | (0, 448) | 128x32 | Four 32x32: Embarrassed / Vintage Knowledge / Trivial Knowledge / Composure |
| Post-to-Social Panel | (128, 448) | 192x64 | Optional posting with the -Bravado comment consequence |
| High-Contrast Exhibit Marker | (320, 448) | 64x32 | Bold outline for examinable exhibits and photo stations |
| Exhibit Silhouette Set | (384, 448) | 128x32 | Giggling Figure / Marilyn / Throne / mutoscope as labelled stepped silhouettes |
| Touch-Zone Guide Overlay | (320, 480) | 192x32 | Dev-only 44px minimum overlay, stripped at build |
| Reserve | (0, 480) | 128x32 | Reserved strip, do not paint |

### Technical Notes:
- The Photo Op Station Table displays honest postability percentages as part of the UI copy; the game tells you nobody will post these before you take them, and you take them anyway
- The Privacy Warning Panel names its exclusions explicitly (Mom via ICQ, Ingrid at the hostel, Agent Havok) rather than showing a generic lock icon
- Composure is a temporary state with a visible recovery path (the bench), not a punishment — the meter must read as gentle
- Every photo station prompt, coin option, and caption choice renders at 44px+ touch height

---

## 🎬 Animation Specifications

### The Giggling Figure (Sheets 4 & 7):
- **Duration:** 3.2 seconds (1.2s pre-activation click, 0.4s lift, 0.8s hold at full extent with giggle, 0.8s descent)
- **Frames:** 4 + mechanical click spark + pneumatic hiss puff
- **Pattern:** Every 30 seconds exactly, whenever anyone is within the sensor radius. No randomisation.
- **Trigger:** Motion sensor; unavoidable on entry
- **Purpose:** 100% jump-scare rate on first encounter, 80% photography rate on second. Sets the tone for the entire museum: mechanical, dated, trying too hard.
- **Audio Sync:** Mechanical clicking begins at 0.0s (the tell); pneumatic hiss at 1.2s; recorded giggle at 1.6s; mechanism reset thunk at 3.2s
- **Mobile Optimization:** Never reduced. In reduced-motion mode the figure holds at frame 1, the giggle audio and glyph still fire, and the jump-scare vignette is suppressed.

### Marilyn Dress Timer (Sheets 4 & 7):
- **Duration:** 2.4 seconds (0.4s grate activation, 0.6s rise, 0.8s full billow, 0.6s settle)
- **Frames:** 4
- **Pattern:** Every 30 seconds on a timer, independent of player presence
- **Trigger:** Timer only — no sensor
- **Purpose:** Everyone takes the same photograph. Everyone. Every time.
- **Audio Sync:** Grate whoosh at 0.4s
- **Mobile Optimization:** Low LOD reduces to 2 frames (rest and full billow); reduced-motion mode holds at rest with the photo station still functional

### Peep Show Flip Cards (Sheets 4, 7, 8):
- **Duration:** 30 seconds per €0.50 viewing; the 8-frame loop cycles at 0.4s per frame
- **Frames:** 8
- **Pattern:** Loops for the paid duration, then stops mid-cycle
- **Trigger:** Coin insertion
- **Purpose:** "People paid money for THIS? ...Put in another coin."
- **Audio Sync:** Coin clunk at 0.0s; mechanical flip per frame; the machine winding down at 30s
- **Mobile Optimization:** Low LOD reduces to 4 frames at 0.8s; reduced-motion uses the static card with the audio retained

### The Jump-Scare Encounter (Sheets 4, 6, 7, 8):
- **Duration:** 4.4 seconds (3.2s figure cycle + 1.2s reaction hold)
- **Frames:** Figure cycle + Jump-Scare Reaction Strip on every NPC in radius + vignette (first time only)
- **Pattern:** One-shot vignette on first encounter; the mechanism itself continues forever
- **Trigger:** First entry, unavoidable
- **Purpose:** The collective jump — every NPC in frame reacting simultaneously is funnier than the player's own reaction
- **Audio Sync:** Musical jump-scare hit at 1.6s, synchronised to the giggle; total silence 2.4-3.2s while everyone recovers
- **Mobile Optimization:** Reaction strip caps at four simultaneous NPCs on Low LOD

### Photo Op Capture (Sheets 6, 7, 8):
- **Duration:** 2.0 seconds (0.8s pose, 0.4s flash, 0.8s result card)
- **Frames:** Photo Op Pose Strip frame + camera flash burst + album entry
- **Pattern:** One-shot per station
- **Trigger:** Interacting with any of the five photo stations
- **Purpose:** The photo is added to a privacy-flagged album with an honest postability rating attached
- **Audio Sync:** Shutter at 0.8s; a small resigned tone at 2.0s
- **Mobile Optimization:** Flash replaced by the no-flash plate in reduced-motion mode

### Neon Venus Flicker (Sheets 3 & 7):
- **Duration:** 0.2-second dip roughly every 6 seconds
- **Frames:** 2
- **Pattern:** Continuous, exterior only, has been like this since 1985
- **Trigger:** Constant
- **Purpose:** Always on, always flickering slightly, never repaired
- **Audio Sync:** Faint neon buzz
- **Mobile Optimization:** Static neon plate on Low LOD; disabled in reduced-motion mode

### The John Lennon Discovery (Sheets 3, 5, 8):
- **Duration:** 2.8 seconds (0.6s examine, 0.6s pause, 1.6s knowledge unlock panel)
- **Frames:** Lennon display examine + Willem's "Yes, really." frame + unlock panel
- **Pattern:** One-shot per save file
- **Trigger:** Examining the John Lennon sketch display
- **Purpose:** The one genuinely surprising fact in the building, and the game is not lying about it
- **Audio Sync:** A single clean chime at 1.2s — distinct from every other sound in the museum
- **Mobile Optimization:** None needed (one-shot)

### Mirror Maze Traversal (Sheets 3 & 7):
- **Duration:** ~12 seconds of traversal with continuous reflection ghosting
- **Frames:** Reflection ghost layer + maze fog + UV wash
- **Pattern:** Continuous while inside the maze passage
- **Trigger:** Entering the maze
- **Purpose:** Short. Disorienting. You will find your way out. Eventually.
- **Audio Sync:** Footsteps gain a slight reverb tail inside the passage
- **Mobile Optimization:** Reflection ghosts cap at two instances on Low LOD; static fog in reduced-motion mode

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Giggling Figure High-Contrast Silhouette | Sheet 4 (0, 768) | 256x256 | Bold outline of the location's defining interactive |
| Marilyn High-Contrast Silhouette | Sheet 4 (256, 768) | 192x256 | Bold outline of the second photo station |
| High-Contrast Exhibit Marker | Sheet 8 (320, 448) | 64x32 | Bold outline for all examinable exhibits and photo stations |
| Exhibit Silhouette Set | Sheet 8 (384, 448) | 128x32 | Four key exhibits as labelled stepped silhouettes |
| Anke / Willem / Petra High-Contrast Silhouettes | Sheet 5 (0/64/128, 416) | 64x96 each | Enhanced-visibility outlines of all three staff NPCs |
| Motion Sensor Trigger Zone | Sheet 4 (768, 384) | 96x96 | Visualises the Giggling Figure's detection radius when interaction zones are enabled |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Giggling Figure | Sheet 4 (448, 768) | 256x256 | Holds at frame 1; no lift, no jump-scare vignette; giggle audio and glyph retained so the beat still lands |
| Static Marilyn | Sheet 4 (704, 768) | 192x256 | Holds at rest; the photo station remains fully functional |
| Peep Show Static Card | Sheet 4 (896, 768) | 128x64 | Single-frame substitute with audio retained |
| Static Neon | Sheet 7 (288, 192) | 64x64 | Steady exterior Venus outline |
| No-Flash Plate | Sheet 7 (352, 192) | 64x64 | Photography without the burst; ambient NPC flashes also suppressed |
| Static Fog | Sheet 7 (416, 192) | 64x64 | Motionless mirror maze atmosphere; reflection ghosts held still |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mechanical Click Glyph | Sheet 7 (448, 128) | 32x32 | Mirrors the pre-activation clicking — the anticipation cue, and the single most important glyph in the location |
| Giggle Glyph | Sheet 7 (384, 128) | 32x32 | Mirrors the signature recorded giggle |
| Pneumatic Hiss Glyph | Sheet 7 (416, 128) | 32x32 | Mirrors the mechanism venting |
| Camera Shutter Glyph | Sheet 7 (480, 128) | 32x32 | Mirrors constant tourist photography |
| Coin Clunk Glyph | Sheet 7 (128, 192) | 32x32 | Mirrors coin insertion |
| Flip Card Glyph | Sheet 7 (160, 192) | 32x32 | Mirrors the mutoscope card flipping |
| Marilyn Whoosh Glyph | Sheet 7 (192, 192) | 32x32 | Mirrors the dress mechanism |
| Music Box Glyph | Sheet 7 (224, 192) | 32x32 | Mirrors the ground floor Victorian music box |
| Stair Creak Glyph | Sheet 7 (256, 192) | 32x32 | Mirrors the old wooden stairs |
| Lennon Chime Glyph | Sheet 8 (0, 320) | 256x64 | The knowledge unlock panel doubles as the visual mirror for its distinct chime |

### Colorblind Considerations:
- Photo station postability is shown as explicit percentage text, never as a colour-coded rating
- The Composure meter uses segment count and a text state label, never a red-to-green gradient
- The Lennon dialogue reaction split is a stacked bar with pattern fills and written percentages
- Exhibits are identified by silhouette and placard text; the three floors are distinguishable by architecture and fixture layout as well as by lighting grade
- Status effects use distinct silhouettes: zigzag (Embarrassed), small-frame (Vintage Knowledge), book-with-question-mark (Trivial Knowledge), steady-line (Composure)
- Privacy-flagged photos carry a shape-coded corner marker in the album, not a colour tint
- Touch zones minimum 44px for all photo stations, coin insertions, exhibit examines, and caption choices

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 (fallback PVRTC 4BPP); all exhibit placards, the art deco sign, the "ADULTS ONLY" and "Educational Exhibits" signage, the Lennon display label, and all portraits at ASTC 4x4
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for both floor sheets (the red wash and the mirror maze UV both band under lossy compression)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| venustempel_exhibits | venustempel_exhibits | 1024x1024 |
| venustempel_mechanisms | venustempel_animated_objects | 1024x1024 |
| venustempel_characters | npc_venustempel_staff, npc_venustempel_visitors | 1024x1024 |
| venustempel_fx_ui | venustempel_effects, venustempel_ui | 1024x512 |

*(The two floor sheets load and unload as paired-room units — only one is resident in normal play. Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full 4-frame Giggling Figure and Marilyn cycles, 8-frame flip cards, ambient NPC flash bursts, neon flicker, mirror reflection ghosts, dust motes, collective jump-scare reactions |
| Medium | Marilyn at 2 frames, flip cards at 4 frames, flash bursts capped at two, reflection ghosts capped at two |
| Low | Simplified mechanism animations (profile requirement) — Giggling Figure retains all 4 frames as the location's core beat, Marilyn holds 2, flip cards hold 1; reduced flash effects (profile requirement); static mannequins elsewhere (profile requirement); no dust motes |

### Performance Targets:
- **Target FPS:** 45 (per location performance budget)
- **Max Draw Calls:** 16 per frame
- **Memory Footprint:** 38 MB maximum
- **Particle Limit:** 14 (dust motes, mirror fog, pneumatic puff, flash motes)

### Performance Notes:
- Paired-floor streaming keeps typical resident footprint at ~20.4 MB (one floor sheet + all atlases); theoretical all-resident worst case is ~28.8 MB, inside budget
- The Giggling Figure is the one animation that is never degraded below four frames on any LOD — it is the location's entire identity
- Bachelor Party, School Group, and Bros Trio all render as pre-composed single blocks
- Mirror reflection ghosts are static silhouette sprites at 40% alpha, never real-time renders
- Ambient camera flashes are hard-capped at three simultaneous instances and pooled

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (floor backgrounds, exhibits, fixtures), AnimatedSprite2D (Giggling Figure, Marilyn, flip cards, neon, staff), CPUParticles2D (dust motes, mirror fog, pneumatic puff — not GPU), CanvasLayer (photo UI, album, coin prompts, knowledge unlock), Area2D (Giggling Figure sensor radius, each mutoscope, all five photo stations, Lennon display, maze entrance, gift shop counter)
- Special systems: 30-second hard-timer mechanism scheduler shared by the Giggling Figure and Marilyn, first-encounter jump-scare flag with vignette suppression afterwards, anticipation-tell activation after first encounter, coin economy with per-viewing 30-second timers, five-station photo system writing to a privacy-flagged sub-album, Unexplainable Photo key-item grant from The Throne, NPC-exclusion list enforcement on album viewing, John Lennon knowledge flag with a 70/20/10 weighted NPC reaction table, Composure temporary state with bench recovery, time-of-day clientele mix selector

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Mechanical click spark | Pre-activation clicking (the tell) | 0.0s of Giggling Figure cycle |
| Pneumatic hiss puff | Air release | 1.2s |
| Giggling Figure frame 3 | Recorded giggle + musical jump-scare hit | 1.6s |
| Post-jump recovery | Total silence | 2.4-3.2s |
| Mechanism reset | Reset thunk | 3.2s |
| Marilyn grate activation | Dress whoosh | 0.4s of Marilyn cycle |
| Coin insertion | Coin clunk | 0.0s of peep show viewing |
| Flip card frames | Mechanical flip, per frame | Every 0.4s for 30s |
| Photo station capture | Shutter, then a small resigned tone | 0.8s / 2.0s |
| Lennon display examine | A single clean chime, unique in the building | 1.2s of discovery |
| Ground floor ambience | Victorian music box loop | Continuous |
| Stairs | Wooden creak | Per step |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Giggling Figure Encounter | Figure cycle, jump-scare vignette, reaction strip, Composure meter, bench | Unavoidable on entry; first encounter costs Composure, second becomes a photo opportunity |
| Photo Consequences System | Five station panels, photo album, privacy warning, sensitive content flags | All photos route to the Venus Temple Collection sub-album with honest postability ratings |
| The "Unexplainable Photo" | The Throne, photo station popup, item card | Key item, cannot be discarded, occasionally recognised by random NPCs |
| John Lennon Knowledge Unlock | Lennon display, Willem's "Yes, really." frame, unlock panel, reaction split bar | Adds a permanent dialogue option with a 70% disbelief / 20% "I knew that" / 10% very interested split |
| Peep Show Devices | Mutoscopes, coin UI, 8-frame flip cards | €0.50 per 30-second viewing; grants Vintage Knowledge and mild confusion about past generations |
| Temple Tourist Achievement | Achievement strip, all five photo stations | Photographing every station; five badges |
| Composure Management | Composure meter, bench, Willem Bench Suggestion | Maintaining composure at the Giggling Figure grants Bravado; the bench is the recovery path |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Tolerance Hostel | Venus Temple Collection album privacy flag; Ingrid on the exclusion list | Kitchen conversation may reference the museum; the photos cannot be shown to Ingrid |
| Café de Schaamte | Album entries, Composure status | Bros attempt to describe the experience, fail, give up; Havok remains unimpressed |
| Casa Rosé | Shared Roodelicht Row corridor; staff dialogue hook | "Ah, the Temple. That's the... gentle introduction." |
| The Hemp Museum | Shared museum-ticket UI style, Cultural Alibi badge | "We've been to TWO museums" — with decreasing conviction |
| ICQ / Mom (system) | Privacy warning panel exclusion list | Mom is a hard exclusion; the panel names her explicitly |
| Agent Havok (character system) | Privacy warning panel exclusion list | Professional relationship; also a hard exclusion |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A haunted house about Victorian machinery, designed in 1985 by somebody's uncomfortable uncle, and genuinely historic"
- **Color Mood:** Venus red and velvet purple under pink neon, warming to vintage cream on the exhibit placards — kitsch, cramped, and unexpectedly earnest
- **Lighting:** Red and pink wash throughout the ground floor, spot pools on individual displays, UV accents upstairs and in the maze, deliberately dim corners everywhere, and constant tourist flash on the second floor
- **Texture:** Brass mutoscope bodies worn smooth, red velvet, Victorian paper, 1985 moulded plastic, creaky varnished floorboards, mirror panels with fingerprint haze

### Environmental Storytelling:
- The Giggling Figure is positioned where nobody can avoid it, which was a decision somebody made on purpose in 1985
- The most interesting exhibit in the building — the John Lennon sketches — is under-lit and off the main sightline
- The 1800s medical diagrams are genuinely more alarming than anything else in the museum
- There is a bench on the ground floor, positioned in direct sight of the Giggling Figure, and it is well-worn
- The "for display only" sign on the swing is small and has clearly been replaced several times
- The neon Venus has flickered since 1985 and nobody has fixed it, because fixing it would change the building

### Character Integration Notes:
- Anke's total immunity is the location's anchor; she has heard every reaction and her expression range is the narrowest in the museum
- Willem's professional neutrality is the second anchor, but he gets one Suppressed Smile frame — deploy it rarely
- Petra's cheerfulness is completely sincere; she is not in on a joke, which is what makes the gift shop land
- Visitor reactions are the real exhibit; the Jump-Scare Reaction Strip fires on everyone in radius simultaneously, and the collective jump is the shot
- Bradley will not be sitting on The Throne. He has standards. His refusal frame comes from the Composure-Maintenance Strip.

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Collective Jump** — the Giggling Figure at full extent with six NPCs reacting simultaneously
2. **The Mechanical Click Tell** — the anticipation frame, after you have learned what comes next
3. **The John Lennon Discovery** — the display, the label, and Willem saying "Yes, really. I don't know why either."
4. **The Photo Op Station Table** — five stations with their honest postability ratings printed next to them
5. **The Bench** — worn, well-used, in direct sight of the Giggling Figure, with someone recovering on it

### Quote Potential:
- "The giggling figure is on your right. Yes, it moves. Everyone jumps. You will also jump."
- "John Lennon sketches are upstairs. Yes, the John Lennon. Yes, really. I get that question a lot."
- "Photos are allowed. What you do with them is your business."
- "Gift shop is at the exit. Yes, you have to walk through it. Yes, I know what we sell."
- "The swing is for display only. I know the sign is small. It's still for display only."
- "If you need to sit down after the Giggling Figure, there's a bench. Many people use the bench."
- "The mirror maze is short. You will find your way out. Eventually."
- "Come back anytime. We're here since 1985. We'll be here when you're ready."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | venustempel_floors_a.png | 2048x1024 |
| 2 | venustempel_floors_b.png | 2048x1024 |
| 3 | venustempel_exhibits.png | 1024x1024 |
| 4 | venustempel_animated_objects.png | 1024x1024 |
| 5 | npc_venustempel_staff.png | 512x512 |
| 6 | npc_venustempel_visitors.png | 1024x256 |
| 7 | venustempel_effects.png | 512x256 |
| 8 | venustempel_ui.png | 512x512 |

**Total Estimated Memory:** ~20.4 MB typical resident (one floor sheet + all atlases); ~28.8 MB theoretical all-resident worst case. Within the 38 MB location budget.

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `venustempel_floors_a.png` (2048x1024)
- [ ] `venustempel_floors_b.png` (2048x1024)
- [ ] `venustempel_exhibits.png` (1024x1024)
- [ ] `venustempel_animated_objects.png` (1024x1024)
- [ ] `npc_venustempel_staff.png` (512x512)
- [ ] `npc_venustempel_visitors.png` (1024x256)
- [ ] `venustempel_effects.png` (512x256)
- [ ] `venustempel_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + 30-second mechanism scheduler diagram + photo station postability table + content-handling sign-off confirming no explicit depiction in any delivered asset

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (#DC143C, #800080, #FFF8DC, #FF69B4, #B08D57, #241A22)
- [ ] Key gags read clearly: the Giggling Figure at rest looks completely harmless, the mechanism reads as 1985 machinery rather than lifelike, the bench is visibly well-used and in sight of the figure, the John Lennon display is discoverable but under-lit, the gift shop has no bypass route
- [ ] Content handling verified: no delivered asset depicts explicit content; all exhibits are machinery, mannequins, framed historical artefacts, signage, or visitor reactions
- [ ] Peep show flip cards are period-accurate Victorian silhouettes and tame by any modern standard
- [ ] All signage and placard text is legible at gameplay zoom on a 5-inch display
- [ ] Accessibility visual alternatives included for all audio cues (click, giggle, hiss, shutter, coin, flip, whoosh, music box, stair creak, Lennon chime)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (targets are tourist photo culture, museum kitsch, and group awkwardness — not human sexuality or legitimate sex education)
- [ ] Staff read as completely unfazed professionals doing an ordinary job
- [ ] Hidden areas/interactions have discoverable visual cues (Lennon display highlight, the bench, the anticipation tell, the maze entrance)
- [ ] Mobile performance optimized (paired-floor streaming, CPU particles, atlas limits respected, simplified mechanism and reduced flash fallbacks per profile)
- [ ] Touch zone sizing considered (44px minimum for photo stations, coin slots, and exhibit examines)
- [ ] Colorblind-friendly alternatives available where color codes meaning (percentage text on postability, segmented Composure meter, pattern-filled reaction split, shape-coded album privacy markers)
- [ ] Social media viral potential maximized in composition choices (collective jump framing, anticipation tell, Lennon discovery staging, the bench)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam Roodelicht Row; the museum's own signage claims "World's First Since 1985" without naming a real city |
| Cultural Specificity | ✅ | Shamsterdam's unique position as a city where this museum could exist, Dutch directness about sexuality, Victorian mutoscope history, canal-house architecture |
| Satirical Targets Appropriate | ✅ | Tourist photo-op culture, museum kitsch, and group dynamics around awkward content — never human sexuality or sex education |
| Seedy Underbelly Present | ✅ | €5 for an experience nobody can adequately describe afterwards; exploiting the city's reputation to sell Victorian machinery; photos priced at €5 and €10 that will never be shown to anyone |
| Gameplay Value Established | ✅ | Giggling Figure encounter with a Composure state, coin-operated peep shows, five photo stations with consequence tracking, privacy-flagged album, Lennon knowledge unlock, 5-badge achievement |
| Technical Feasibility | ✅ | Paired-floor streaming, simplified mechanism and reduced flash fallbacks per profile, static mannequins on older devices per profile, pooled flash instances |
| Mobile Performance Budget | ✅ | 45 FPS, 16 draw calls, 38 MB, 14 particles per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all ten audio cues including the critical anticipation click, reduced-motion set that preserves the comedy beat without the jump-scare, 44px touch zones |
| No Crypto Elements | ✅ | Pure mechanical curiosity; the only currency is €0.50 coins for machines built in the 1890s |
| Content Handled Appropriately | ✅ | No asset in this specification depicts explicit content; every exhibit is machinery, a mannequin, a framed artefact, signage, or a visitor reaction |
| Social Media Integration | ✅ | 5 screenshot moments + 8 quotable lines identified |

**Once these assets ship, Venustempel becomes the game's most honest tourist trap: five euros, three cramped floors, one pneumatic mannequin on a thirty-second timer, a genuinely surprising John Lennon, a gift shop you cannot walk around, and a photograph you will keep forever and show to absolutely no one.**
