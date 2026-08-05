# The Hemp Museum - Complete PNG Asset Requirements

## 📋 Overview
The Hemp Museum charges 10 Sovs for 500 years of genuinely fascinating history that visitors will speed-walk past on their way to look at plants, and then sells them a grinder on the exit. This document specifies every PNG asset for the museum: the canal-house facade attempting scholarly dignity between a peep show and a coffeeshop, four exhibit floors whose visitor dwell times are inversely proportional to their educational value, the growing room with its purple glow and its patient botanist, the gift shop that occupies more floor space than any exhibit, and Lars — who wrote a forty-page thesis on hemp rope's role in Dutch maritime history and has sold zero audio guides today. Its satirical essence in a sentence: everyone in the building knows why you came, and only one of them is upset about it.

**Location ID:** `shamsterdam_roodelicht_hemp_museum_01`
**Theme:** Educational tourism as cultural alibi — the performance of learning, monetised at the exit
**Zone:** Roodelicht Row, attempting respectability, and technically achieving it relative to its neighbours
**Hours:** 10 AM - 10 PM (gift shop closes 9:45, which is most people's main question)
**Primary Function:** Museum / shop hybrid — four-floor navigation with hidden speed-run tracking, "Feel the Hemp!" and "Identify the Terpenes!" interactives, the free-tea funnel, Cultural Alibi flag, and the Gift Shop Bag tourist marker

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Educational Green | #228B22 | Signage, staff clothing, hemp imagery |
| Museum Cream | #F5F5DC | Exhibit panels, gallery walls, placards |
| Historic Brown | #8B4513 | Canal house timber, floorboards, frames |
| Grow Light Purple | #8B008B | Second floor LED wash, the actual attraction |
| Gift Shop Bright | #FFE9A8 | Retail lighting, commercial cheer |
| Dust Gray | #9A9186 | Old building grime, unread panel shadow |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/hemp_museum/
├── environment/
│   ├── hemp_museum_floors_a.png
│   ├── hemp_museum_floors_b.png
│   ├── hemp_museum_floors_c.png
│   └── hemp_museum_exhibits.png
├── objects/
│   └── hemp_museum_objects.png
├── npcs/
│   ├── npc_hemp_museum_staff.png
│   └── npc_hemp_museum_visitors.png
└── fx_ui/
    └── hemp_museum_fx_ui.png
```

---

## 🏛️ Sprite Sheet 1: Floors A — Entry Hall & Industrial Hemp
**File:** `hemp_museum_floors_a.png`
**Dimensions:** 2048x1024 pixels (paired room backgrounds, streamed — only one floor sheet resident at a time)
**Color Palette:** #F5F5DC, #8B4513, #9A9186

### Room Backgrounds:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Entry Hall & Timeline | (0, 0) | 1024x1024 | Narrow canal-house entry: ticket counter left, audio guide rack beside it, welcome panel "HEMP: A History of Humanity's Most Versatile Plant," timeline graphic starting at 10,000 BCE, coat hooks (trust system), donation box (optimistic), stairs up at the rear |
| Industrial Hemp Section (Ground Floor) | (1024, 0) | 1024x1024 | Glass cases of hemp rope, Dutch Golden Age ships panel, industrial plant samples, global cultivation map, recreated sailor's quarters, "Feel the Hemp!" fabric station — extremely detailed signage, extremely unread |

### Technical Notes:
- Anchor points (Entry Hall): ticket counter at (256, 640), audio guide rack at (448, 576), timeline wall at (640, 384), stairs-up at (896, 512), coat hooks at (96, 448)
- Anchor points (Industrial): rope cases at (1216, 576), ships panel at (1472, 448), fabric station at (1728, 640), map at (1920, 448), stairs-up at (1024, 512)
- Both rooms share one 8.39 MB texture and load/unload together as the player moves between the ground-floor pair — this pairing is what keeps a five-room museum inside a 38 MB budget
- Industrial section is deliberately the best-lit and best-signed room in the building; its emptiness must be the composition's subject
- Gallery lighting is baked flat — the spot pools (Sheet 8) provide the "attempted gallery lighting, achieving dim with spots" effect

---

## 🖼️ Sprite Sheet 2: Floors B — Historical Usage & Growing Room
**File:** `hemp_museum_floors_b.png`
**Dimensions:** 2048x1024 pixels (paired room backgrounds, streamed)
**Color Palette:** #F5F5DC, #8B4513, #8B008B

### Room Backgrounds:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Historical Usage Section (First Floor) | (0, 0) | 1024x1024 | Replica ancient pipes, historical paintings, dense medical history panels, the Queen Victoria fact panel, vintage advertisement wall, the Prohibition Timeline — genuinely fascinating material receiving 10% of its deserved attention |
| Growing & Processing Room (Second Floor) | (1024, 0) | 1024x1024 | The observation window dominating the far wall, live plants under LED rigs, purple wash across everything, processing equipment displays, smell jars station with a queue, video loop screen nobody finishes, Sanne's post beside the glass |

### Technical Notes:
- Anchor points (Historical): pipe case at (192, 512), painting cluster at (448, 384), Queen Victoria panel at (640, 448), vintage ad wall at (832, 448), video screen at (384, 704)
- Anchor points (Growing): observation window at (1408, 512), plant display at (1664, 576), smell jars at (1856, 640), Sanne post at (1536, 768), grow rig at (1664, 320)
- The Growing Room is painted one full stop brighter in saturation than every other room; the purple wash overlay (Sheet 8) sits on top of it
- The Queen Victoria panel is painted at 2x internal resolution — it is the single fact every visitor retains and must be readable at gameplay zoom
- The observation window's glass layer is a separate alpha element so the plant sway animation (Sheet 8) renders behind it

---

## 🛍️ Sprite Sheet 3: Floors C — Gift Shop & Hemp Garden Courtyard
**File:** `hemp_museum_floors_c.png`
**Dimensions:** 2048x1024 pixels (paired room backgrounds, streamed)
**Color Palette:** #FFE9A8, #228B22, #8B4513

### Room Backgrounds:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gift Shop Floor (Exit) | (0, 0) | 1024x1024 | Larger than any exhibit floor, impossible to bypass, bright and cheerful: Educational Materials / Hemp Products / Paraphernalia / Souvenir / Seeds / CBD zones, Bob Marley poster, "Hemp Can Save The World" propaganda, register at the exit, hemp tea station funnelling traffic in |
| Hemp Garden Courtyard | (1024, 0) | 1024x1024 | Henrik's domain: industrial hemp beds (very legal, very boring to look at), one bench, one seasonal employee, four summers of accumulated silence |

### Technical Notes:
- Anchor points (Gift Shop): register at (832, 704), paraphernalia zone at (448, 576), seeds cabinet at (640, 512), CBD shelf at (256, 576), tea station at (128, 768), exit door at (960, 832)
- Anchor points (Courtyard): bench at (1408, 704), hemp beds at (1664, 640), doorway back inside at (1152, 512)
- Gift shop floor area must visibly exceed any single exhibit room in the same scene scale — this is the location's central structural joke and cannot be softened for composition
- The hemp tea station sits between the stairs and the shop entrance so the funnel geometry reads without dialogue
- Courtyard is the only naturally-lit room; the daylight wash (Sheet 8) is warm and completely uneventful, matching Henrik's tenure

---

## 🪢 Sprite Sheet 4: Exhibits & Fixtures
**File:** `hemp_museum_exhibits.png`
**Dimensions:** 1024x1024 pixels
**Color Palette:** #F5F5DC, #8B4513, #228B22, #8B008B

### Exterior & Entry:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Museum Exterior (Canal House) | (0, 0) | 384x512 | Green door, brass historical plaque (real), neon OPEN sign (less historical), "EDUCATIONAL EXHIBITS" large / "Gift Shop" small |
| Ticket Counter | (384, 0) | 256x192 | 10 Sovs entry, 3 Sovs audio guide, bored staff, hope |
| Welcome Panel | (640, 0) | 192x128 | "HEMP: A History of Humanity's Most Versatile Plant" |
| Timeline Graphic (10,000 BCE →) | (832, 0) | 192x128 | Establishing ancient legitimacy in one wall |
| Audio Guide Rack | (640, 128) | 96x64 | 3 Sovs extra. Fully stocked. Always fully stocked. |
| Coat Hook Row | (736, 128) | 96x64 | The coat check. It is hooks. It is trust. |
| Donation Box | (832, 128) | 96x64 | Optimistic |
| Ticket Desk Sign | (928, 128) | 96x64 | Prices and hours, laminated |

### Industrial Hemp Exhibits:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Glass Case of Hemp Rope | (384, 192) | 192x192 | Riveting. Genuinely riveting. Nobody stops. |
| Dutch Golden Age Ships Panel | (576, 192) | 192x192 | The rigging needed hemp; the empire needed rigging |
| Hemp Plant Samples (Industrial) | (768, 192) | 128x192 | Disappointingly legal variety |
| Global Cultivation Map | (896, 192) | 128x192 | A lot of pointing at this, very little reading |
| Recreated Sailor's Quarters | (384, 384) | 256x128 | Why is this here. It is here. It is beautifully made. |
| "Feel the Hemp!" Station | (640, 384) | 192x128 | Fabric samples you can touch. Everyone touches. Nobody learns. |
| Replica Ancient Pipes Case | (832, 384) | 192x128 | "Now we're talking" — the first exhibit anyone photographs |

### Historical Usage Exhibits:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Historical Paintings Cluster | (0, 512) | 192x192 | Artistic legitimacy, three frames |
| Medical Marijuana History Panels | (192, 512) | 192x192 | Lengthy, detailed, skimmed |
| "Queen Victoria" Fact Panel | (384, 512) | 192x128 | The one fact everyone remembers, forever |
| Vintage Advertisement Wall | (576, 512) | 192x192 | From when it was legal; always photographed |
| Prohibition Timeline | (768, 512) | 256x192 | When fun ended, by country, in order |
| Video Exhibit Screen | (384, 640) | 192x128 | "The Cultivation Process" — ten minutes, zero completions |
| Bob Marley Poster | (576, 704) | 192x64 | Legally required |
| "Hemp Can Save The World" Propaganda | (768, 704) | 256x64 | Earnest. Entirely earnest. |
| Gift Shop Zone Signage Set | (0, 704) | 192x64 | Six zone headers: Educational / Hemp / Paraphernalia / Souvenir / Seeds / CBD |
| Museum Floor Tile (Tileable) | (192, 704) | 64x64 | Worn canal-house board, seamless all edges |
| Staff Hemp Clothing Rack | (256, 704) | 128x64 | Uniform requirement, commitment to the bit |

### Growing Room:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Observation Window | (0, 768) | 384x256 | The actual attraction; glass layer authored separately |
| Live Cannabis Plants Display | (384, 768) | 256x256 | Stylised, healthy, under-lit in purple |
| Grow Light Rig | (640, 768) | 128x256 | LEDs optimising the spectrum, as Sanne will explain if given the chance |
| Smell Jars Station | (768, 768) | 128x128 | The line forms here |
| "Identify the Terpenes!" Board | (896, 768) | 128x128 | Multiple choice. Impossible. Attempted universally. |
| "No Touching" Sign | (768, 896) | 128x64 | Tested regularly |
| Growing Room Info Panels | (896, 896) | 128x64 | For education! |
| Sanne's Post Marker | (768, 960) | 128x64 | Positioned to intercept close-up photography |
| Grow Room Vent / Fan | (896, 960) | 128x64 | The hum that defines the floor |

### Technical Notes:
- Observation Window ships as frame plus a separately-authored glass alpha layer so plant sway (Sheet 8) renders behind glass with a correct reflection pass
- Museum Floor Tile must seam on all four edges and tolerate 90° rotation; it is the only tiled asset in the location
- Queen Victoria panel, Prohibition Timeline, and all zone signage are baked at 2x internal resolution and flagged for the uncompressed-texture exception list
- Exhibit cases in the Industrial section are drawn with pristine glass and zero fingerprints; the Growing Room glass is covered in them

---

## 🎒 Sprite Sheet 5: Objects & Gift Shop Inventory
**File:** `hemp_museum_objects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #228B22, #FFE9A8, #8B4513, #F5F5DC

### Handheld & Tickets:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Audio Guide Device | (0, 0) | 32x48 | 3 Sovs, genuinely informative, ~5% selection rate |
| Smell Jar (Individual) | (32, 0) | 32x48 | Terpene challenge unit |
| Hemp Tea Cup | (64, 0) | 32x48 | "Complimentary." Earthy. Disappointing. |
| CBD Oil Bottle (Gift Shop) | (96, 0) | 32x48 | 30 Sovs-80, "Wellness product." |
| Museum Ticket (10 Sovs) | (128, 0) | 64x48 | The cultural alibi, purchased |
| Combo Ticket (15 Sovs) | (192, 0) | 64x48 | Neighbouring attraction, separate gift shops |
| Rolling Papers (Branded) | (256, 0) | 64x48 | 5 Sovs, "Museum quality." |
| "Educational" Grinder | (320, 0) | 64x48 | 15 Sovs-45, "For herbs. Any herbs." |
| Hemp Tote Bag (Museum) | (384, 0) | 64x48 | 18 Sovs, cosmetic inventory expansion |
| Gift Shop Bag (Tourist Marker) | (448, 0) | 64x48 | The consequence; budtenders recognise it |

### Interactives & Shop Goods:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fabric Samples ("Feel the Hemp!") | (0, 48) | 128x48 | Four swatches, touch-prompted, instantly forgotten |
| Hemp Tea Station | (128, 48) | 96x48 | Loss leader, positioned for maximum funnel |
| Hemp Soap + Box | (224, 48) | 64x48 | 8 Sovs, exists purely for plausible deniability |
| "I Got High on Knowledge" Shirt | (288, 48) | 64x48 | 28 Sovs, +Embarrassed when worn, "Popular choice." |
| "Hemp History" Book | (352, 48) | 64x48 | 25 Sovs, +Intelligence display, will not be read |
| Seed Packet ("Souvenir only") | (416, 48) | 96x48 | 20 Sovs-50, very important, very fine print |

### Readable Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Vintage Advertisement (Framed) | (0, 96) | 96x64 | Always photographed |
| Queen Victoria Fact Panel (Readable) | (96, 96) | 96x64 | Menstrual cramps. 1890s. Everyone remembers. |
| Terpene Reference Card | (192, 96) | 96x64 | Post-mini-game handout; knowledge degrades within the hour |
| Prohibition Timeline (Readable) | (288, 96) | 96x64 | Country by country, when fun ended |
| Live Plant (Single, Stylised) | (384, 96) | 64x64 | Growing room unit |
| Hemp Plant (Industrial, Stylised) | (448, 96) | 64x64 | Ground floor unit; visually near-identical, legally not |

### Staff Props & Tools:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Grinder (Premium 45 Sovs) | (0, 160) | 64x48 | Marco's best seller |
| Grinder (Basic 15 Sovs) | (64, 160) | 64x48 | Marco's volume seller |
| Growing Guide (NOT Provided) | (128, 160) | 96x48 | Visible on a shelf behind the counter, never sold, never explained |
| Thesis Manuscript (Lars's) | (224, 160) | 96x48 | 40 pages on hemp rope in Dutch maritime history |
| Clipboard (School Group) | (320, 160) | 64x48 | Worksheet, mostly doodles |
| Notebook (Actual Enthusiast) | (384, 160) | 64x48 | Genuine notes; almost mythical |
| Museum Polo + Name Tag | (448, 160) | 64x48 | Henrik's uniform, four summers deep |

### Icons & Materials:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Audio Guide Icon | (0, 208) | 32x32 | Headset silhouette |
| Ticket Icon | (32, 208) | 32x32 | Stub silhouette |
| Grinder Icon | (64, 208) | 32x32 | Toothed-disc silhouette |
| Seeds Icon | (96, 208) | 32x32 | Packet silhouette |
| CBD Oil Icon | (128, 208) | 32x32 | Dropper silhouette |
| Gift Shop Bag Icon | (160, 208) | 32x32 | Handled-bag silhouette (tourist marker) |
| Trivial Knowledge Icon | (192, 208) | 32x32 | Small-book-with-question-mark silhouette |
| Calm Status Icon | (224, 208) | 32x32 | Level-line silhouette |
| Embarrassed Status Icon | (256, 208) | 32x32 | Zigzag silhouette |
| Cultural Alibi Icon | (288, 208) | 32x32 | Column-and-ticket silhouette |
| Hemp Rope (Display Coil) | (320, 208) | 64x48 | The most under-appreciated object in the building |
| Museum Floor Tile (64px) | (384, 208) | 64x48 | Alternate tile crop for prop layering |
| Reserve | (448, 208) | 64x48 | Reserved cell, do not paint |

### Technical Notes:
- Live Plant and Hemp Plant (Industrial) are near-identical by design; the entire ground-floor joke depends on visitors not being able to tell why one floor is boring
- Gift Shop Bag must be recognisable at 32px from across a coffeeshop scene — it is a cross-location social marker
- The Growing Guide prop is visible in the gift shop backdrop but has no interaction; it is environmental storytelling only
- All readable props flagged for the uncompressed-texture exception list

---

## 👔 Sprite Sheet 6: Museum Staff
**File:** `npc_hemp_museum_staff.png`
**Dimensions:** 512x512 pixels
**Sprite Size:** 64x96 per character frame; 128x128 per portrait (Henrik portrait 128x96, cropped)
**Color Palette:** #228B22 staff hemp clothing, #F5F5DC, #8B008B

### Ticket Attendant Lars — The Arc of a Shift:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lars Hopeful | (0, 0) | 64x96 | Start of shift, ponytail, glasses, "I have a history degree" energy |
| Lars Pitching Audio Guide | (64, 0) | 64x96 | "The audio guide is... very good." |
| Lars Resigned | (128, 0) | 64x96 | By lunch |
| Lars Directing Upstairs | (192, 0) | 64x96 | "Past the historical exhibits. The historical exhibits are also interesting." |
| Lars Thesis Mention | (256, 0) | 64x96 | "I wrote my thesis on—" |
| Lars Watching Them Walk Away | (320, 0) | 64x96 | "—oh, you're already walking. Okay." |
| Lars Zero-Sales Slump | (384, 0) | 64x96 | End of shift. Audio guide sales: zero. Again. |
| Lars Audio Guide SOLD (Shock) | (448, 0) | 64x96 | Visible surprise. Rare. Celebrated by staff. |

### Growing Room Attendant Sanne:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sanne Idle (Lab Coat) | (0, 96) | 64x96 | Botany student, lab coat adding legitimacy, hemp accessories underneath |
| Sanne Photography Intercept F1 | (64, 96) | 64x96 | Step forward |
| Sanne Photography Intercept F2 | (128, 96) | 64x96 | Hand raised, patient, non-confrontational |
| Sanne "Please don't tap the glass" | (192, 96) | 64x96 | "The plants don't like it. I don't like it either." |
| Sanne Terpene Correction | (256, 96) | 64x96 | Politely corrects, explains anyway, is forgotten immediately |
| Sanne Licence Explanation | (320, 96) | 64x96 | "Yes, it's legal. We have a licence. Yes, I get that question a lot." |
| Sanne Waiting (Patiently) | (384, 96) | 64x96 | "—okay, you're taking a photo, I'll wait." |
| Sanne Pointing to Smell Jars | (448, 96) | 64x96 | "No, you can't smell the actual plants. No, really." |

### Portraits & Marco/Henrik Base:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lars Portrait (Hopeful) | (0, 192) | 128x128 | Start-of-shift optimism, thesis-shaped |
| Lars Portrait (Resigned) | (128, 192) | 128x128 | Same face. Different eyes. |
| Sanne Portrait | (256, 192) | 128x128 | Knows everything, is asked nothing |
| Marco Idle | (384, 192) | 64x96 | Most enthusiastic staff member; commission may be involved |
| Henrik Bench Idle | (448, 192) | 64x96 | Thousand-yard stare, fourth summer |
| Reserve / Atlas Padding | (384, 288) | 128x32 | Reserved strip, do not paint |

### Gift Shop Attendant Marco:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marco Sales Pitch | (0, 320) | 64x96 | "Looking for anything specific?" |
| Marco Seed Explanation F1 | (64, 320) | 64x96 | "They're legal to buy." |
| Marco Seed Explanation F2 | (128, 320) | 64x96 | "Growing them is... check your local laws." |
| Marco Grinder Upsell | (192, 320) | 64x96 | "Museum quality. Works for any... herbs." |
| Marco Bag Recognition | (256, 320) | 64x96 | "Everyone will know where you've been. That's part of the experience." |
| Marco Portrait | (320, 320) | 128x128 | Helpful in a specifically commercial way |
| Henrik Thousand-Yard Stare | (448, 320) | 64x96 | Contemplating life choices on a bench |

### Henrik & Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Henrik "Fun fact:" | (0, 416) | 64x96 | "Most people stop listening after I say 'fun fact.'" |
| Henrik Gift Shop Hours | (64, 416) | 64x96 | "Most people's main question is 'when does the gift shop close.'" |
| Henrik Portrait (Cropped) | (128, 416) | 128x96 | Cropped-height portrait; renders letterboxed in the dialogue frame by design |
| Lars High-Contrast Silhouette | (256, 416) | 64x96 | Accessibility outline variant |
| Sanne High-Contrast Silhouette | (448, 416) | 64x96 | Accessibility outline variant |
| Accessibility Reserve Block | (320, 448) | 128x64 | Reserved for high-contrast/audio-cue glyph overflow |

### Technical Notes:
- Lars's eight frames form a single shift-arc; the game selects among them by in-game clock, not by dialogue branch — his decline is ambient, not scripted at the player
- Lars Portrait (Hopeful) and (Resigned) must be the same drawing with only the eyes and mouth-corner altered; the joke is that nothing else changed
- Sanne's intercept frames trigger on sustained close-up photography at the observation window, never on the first photo
- Henrik's portrait is deliberately cropped shorter than every other portrait in the game — he does not get a full frame

---

## 👥 Sprite Sheet 7: Visitors
**File:** `npc_hemp_museum_visitors.png`
**Dimensions:** 1024x256 pixels
**Sprite Size:** 64x96 per single NPC frame; 128x128 per portrait
**Color Palette:** Mixed visitor palette, museum-cream ambient grade (purple grade in growing room)

### Visitors:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| School Group | (0, 0) | 256x96 | Fifteen teenagers, permission slips, giggling at everything, learning nothing |
| Exhausted Teacher | (256, 0) | 64x96 | "Please focus on the INDUSTRIAL applications." |
| Couple Pretending They're Not High | (320, 0) | 128x96 | Reading EVERY panel. Very slowly. With real feeling. |
| Embarrassed Parent + Teen | (448, 0) | 128x96 | "This is about HISTORY." Walking faster. |
| Actual Enthusiast | (576, 0) | 64x96 | Notebook, audio guide, being what the museum wanted. Rare spawn. |
| Speed-Walking Tourist F1 | (640, 0) | 64x96 | Ground floor transit pose |
| Speed-Walking Tourist F2 | (704, 0) | 64x96 | Ground floor transit pose, faster |
| Bros Trio | (768, 0) | 192x96 | Lord Pilsner / Chadwick / Bradley, pre-composed |
| Gift Shop Browser | (960, 0) | 64x96 | Twenty minutes and counting |

### Portraits & Group Blocks:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| School Group Giggle Strip | (0, 96) | 192x96 | Three 64x96 frames for randomised giggle bursts |
| Teacher Portrait | (192, 96) | 128x128 | Beyond exhaustion, into something calmer |
| Couple Portrait | (320, 96) | 128x128 | "Babe. Babe. Look at this rope." |
| Enthusiast Portrait | (448, 96) | 128x128 | Genuine, informed, quietly making everyone feel worse |
| Growing Room Crowd Block | (576, 96) | 192x96 | Pre-composed cluster at the observation window |
| Gift Shop Queue Block | (768, 96) | 192x96 | Pre-composed register line |
| Photography Pose Strip | (960, 96) | 64x96 | Two 64x48 frames: phone raised / phone lowered |

### Ambient:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Section-Time Comparison Silhouettes | (0, 192) | 192x64 | Three 64x64 silhouettes for the speed-run tracker UI |
| Observation Window Crowd Silhouette | (576, 192) | 192x64 | Backs of heads at the glass, cheap depth |
| Gift Shop Silhouette Row | (768, 192) | 192x64 | Browsing depth for the retail floor |
| Accessibility Reserve | (960, 192) | 64x64 | Reserved for high-contrast marker |
| Portrait Band Padding | (192, 224) | 384x32 | Reserved padding, do not paint |

### Technical Notes:
- School Group, Growing Room Crowd, Gift Shop Queue, and Bros Trio all ship as pre-composed blocks to protect the 16-draw-call budget
- Growing Room Crowd Block must be authored to accept the purple grade multiply cleanly — no baked warm lighting
- The Actual Enthusiast has a spawn weight of roughly 1-in-8 visits; when present, she must be visible from the Industrial section entrance

---

## ✨🧭 Sprite Sheet 8: Effects & UI
**File:** `hemp_museum_fx_ui.png`
**Dimensions:** 1024x512 pixels (combined FX + UI sheet)
**Color Palette:** #8B008B, #F5F5DC, #228B22, #FFE9A8

### Effects — Light & Air (left half):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Grow Light Shimmer Frame 1 | (0, 0) | 64x64 | LED spectrum ripple |
| Grow Light Shimmer Frame 2 | (64, 0) | 64x64 | Ripple variant |
| Purple Grow Glow Plate | (128, 0) | 128x128 | Additive bloom around the rig |
| Dust Motes (Old Building) F1 | (256, 0) | 64x64 | Historic charm, suspended |
| Dust Motes F2 | (320, 0) | 64x64 | Drift variant |
| Incense Wisp (Gift Shop) | (384, 0) | 64x64 | Faint, commercial, slightly reggae-adjacent |
| Plant Gentle Sway F1 | (448, 0) | 64x64 | Behind glass, subtle |
| Plant Gentle Sway F2 | (0, 64) | 64x64 | Behind glass, subtle variant |
| Video Screen Loop Flicker | (64, 64) | 64x64 | Ten-minute loop, perpetual |
| Gallery Spot Pool | (256, 64) | 64x64 | Attempted gallery lighting, achieved dim-with-spots |
| Gift Shop Bright Wash | (320, 64) | 64x64 | "Please buy things" |
| Smell Jar Aroma Wisp | (384, 64) | 64x64 | One-shot on jar open |
| Camera Flash (Blocked) | (448, 64) | 64x64 | Flash fires, Sanne is already there |

### Visual Audio Cues & Reduced Motion:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Creak Glyph (Old Building) | (0, 128) | 32x32 | Mirrors the ambient building creak |
| Grow Room Hum Glyph | (32, 128) | 32x32 | Mirrors LED and ventilation hum |
| Video Loop Glyph | (64, 128) | 32x32 | Mirrors the persistent exhibit audio |
| Register Beep Glyph | (96, 128) | 32x32 | Mirrors the gift shop register |
| School Giggle Glyph | (128, 128) | 32x32 | Mirrors the random giggle encounter |
| Audio Guide Selected Glyph | (160, 128) | 32x32 | Mirrors the rare-purchase celebration sound |
| Terpene Correct Glyph | (192, 128) | 32x32 | Mirrors the mini-game success chime |
| Terpene Wrong Glyph | (224, 128) | 32x32 | Mirrors the polite-correction sting |
| Tea Pour Glyph | (256, 128) | 32x32 | Mirrors the complimentary tea cue |
| Footstep (Speed-Run) Glyph | (288, 128) | 32x32 | Mirrors accelerating footsteps in the Industrial section |
| Static Grow Light | (320, 128) | 64x64 | Reduced-motion non-shimmering LED plate |
| Static Plants | (384, 128) | 64x64 | Reduced-motion non-swaying plant plate |
| Dust-Free Plate | (448, 128) | 64x64 | Reduced-motion clean-air variant |
| Cultural Alibi Sparkle | (0, 192) | 32x32 | One-shot on flag acquisition |
| Bag Marker Pulse | (32, 192) | 32x32 | Gift shop bag acquired |
| Effects Reserve | (64, 192) | 448x64 | Reserved strip, do not paint |

### Room Grade Plates:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Grow Room Purple Wash (Full) | (0, 256) | 256x256 | Full-room multiply plate, the floor's signature |
| Museum Warm Wash | (256, 256) | 128x128 | Historical section grade |
| Gift Shop Wash | (384, 256) | 128x128 | Bright commercial grade |
| Courtyard Daylight Wash | (256, 384) | 128x128 | The only natural light in the building |
| Entry Hall Wash | (384, 384) | 128x128 | Neutral, slightly dusty |

### UI — Mini-Games & Trackers (right half):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Terpene Game UI | (512, 0) | 256x192 | Smell-and-guess interface, four options, ~10% success rate |
| Section Time Tracker | (768, 0) | 256x64 | Per-section dwell timer, hidden until the exit reveal |
| Speed-Run Comparison Bars | (768, 64) | 256x64 | Your time vs. average visitor time, per section, brutal |
| Cultural Alibi Badge | (768, 128) | 64x64 | "Visited a Museum" — usable in future dialogue |
| Audio Guide Selection Panel | (832, 128) | 192x64 | 3 Sovs prompt with visible staff-reaction slot |
| Hemp vs Marijuana Popup | (512, 192) | 192x128 | Educational correction, triggered by asking "where's the weed?" |

### UI — Status, Shop & Accessibility:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Gift Shop Marking Indicator | (704, 192) | 128x32 | Bag-carrier status, visible to other locations |
| Trivial Knowledge Status Bar | (704, 224) | 128x32 | Terpene win duration; degrades rapidly |
| Calm Status Bar | (704, 256) | 128x32 | Hemp tea / CBD effect |
| Embarrassed Status Bar | (704, 288) | 128x32 | Shirt-worn effect |
| Gift Shop Purchase Panel | (832, 192) | 192x128 | Eight-item list with Marco's one-line comments |
| Exhibit Examine Panel | (512, 320) | 256x96 | Flavour text frame for any examinable display |
| Ticket Purchase Panel | (768, 320) | 128x96 | 10 Sovs + optional 3 Sovs audio guide |
| Combo Ticket Panel | (896, 320) | 128x96 | 15 Sovs, neighbouring attraction, separate gift shops |
| Alibi Track Strip | (512, 416) | 256x64 | Four 64x64 markers: Entered / Endured / Educated / Purchased |
| Status Icon Row | (768, 416) | 128x32 | Four 32x32: Trivial Knowledge / Calm / Embarrassed / Cultural Alibi |
| High-Contrast Exhibit Marker | (896, 416) | 64x32 | Bold outline for examinable displays |
| Terpene Silhouette Set | (960, 416) | 64x32 | Four terpene options as shape-coded glyphs with text |
| Touch-Zone Guide Overlay | (768, 448) | 128x32 | Dev-only 44px minimum overlay, stripped at build |
| UI Reserve | (896, 448) | 128x64 | Reserved strip, do not paint |

### Technical Notes:
- The Section Time Tracker records silently throughout the visit and only surfaces at the gift shop exit; its comedic payload depends entirely on the player not knowing it was running
- Terpene options are shape-coded glyphs with text labels; the mini-game is meant to be nearly impossible, but never impossible for the wrong reason
- Room grade plates are multiply-blend full-screen quads swapped on room transition — one draw call per room, never per-object tinting
- Plant sway renders behind the observation window's glass alpha layer; if the glass is disabled on Low LOD, sway must also be disabled to preserve the compositing order

---

## 🎬 Animation Specifications

### Grow Light Shimmer (Sheet 8):
- **Duration:** 2.4 seconds per cycle
- **Frames:** 2 shimmer frames + continuous purple bloom plate
- **Pattern:** Slow crossfade loop, continuous
- **Trigger:** Constant while the Growing Room is loaded
- **Purpose:** The purple glow is the reason anyone paid 10 Sovs; it must be the most alive thing in the museum
- **Audio Sync:** LED and ventilation hum bed, phase-locked to the shimmer
- **Performance Optimization:** Low LOD uses the Static Grow Light plate with the bloom held at fixed alpha (profile requirement: simplified grow lights)

### Plant Gentle Sway (Sheets 4 & 8):
- **Duration:** 3.6 seconds per cycle
- **Frames:** 2, crossfaded (never popped)
- **Pattern:** Continuous, each plant instance phase-offset by a random 0-3.6s
- **Trigger:** Constant while the Growing Room is loaded
- **Purpose:** Living plants. That is the whole exhibit. They must move.
- **Audio Sync:** None (covered by the room hum)
- **Performance Optimization:** Low LOD uses Static Plants (profile requirement); the glass reflection layer is also disabled to keep compositing correct

### Video Exhibit Loop (Sheets 4 & 8):
- **Duration:** 1.2 seconds per flicker cycle
- **Frames:** 2 screen-flicker plates over a static painted frame
- **Pattern:** Continuous, all day, every day
- **Trigger:** Constant while the Historical section is loaded
- **Purpose:** Ten minutes of content nobody has ever finished, playing forever
- **Audio Sync:** Muffled narration bed, persistent, slightly too quiet to follow
- **Performance Optimization:** Low LOD holds a single static frame; audio bed is retained

### The Lars Shift Arc (Sheet 6):
- **Duration:** Full in-game day, frame selection by clock
- **Frames:** Hopeful (10 AM-12 PM) → Resigned (12-6 PM) → Zero-Sales Slump (6-10 PM), with reaction frames overriding
- **Pattern:** Ambient state, not a played animation
- **Trigger:** In-game clock
- **Purpose:** The museum's emotional throughline, delivered entirely by which sprite is standing at the desk
- **Audio Sync:** None
- **Performance Optimization:** None needed (single-sprite state swap)

### Audio Guide Purchase (Sheets 5, 6, 8):
- **Duration:** 2.0 seconds (0.4s selection, 0.6s Lars shock frame, 1.0s hold)
- **Frames:** Selection panel confirm + Lars Audio Guide SOLD frame + celebration sparkle
- **Pattern:** One-shot, roughly 5% of visits
- **Trigger:** Purchasing the 3 Sovs audio guide
- **Purpose:** The rarest positive event in the building, celebrated disproportionately
- **Audio Sync:** Small triumphant sting at 0.4s — the only unambiguously happy sound in the museum
- **Performance Optimization:** None needed (one-shot)

### "Identify the Terpenes!" Mini-Game (Sheets 4, 6, 8):
- **Duration:** Per attempt: 1.0s jar open, 2.0s selection window, 1.2s result
- **Frames:** Smell jar aroma wisp + Sanne Terpene Correction (on failure) + result glyph
- **Pattern:** Repeatable; ~10% success rate by design
- **Trigger:** Interacting with any smell jar
- **Purpose:** Impossible without actual knowledge; attempted by everyone; forgotten immediately either way
- **Audio Sync:** Jar lid at 0.0s; success chime or polite-correction sting at 3.0s; Sanne's explanation continues past the UI dismissal
- **Performance Optimization:** Aroma wisp reduced to a single frame on Low LOD

### Photography Intercept (Sheets 6, 7, 8):
- **Duration:** 2.2 seconds (0.6s flash, 0.8s Sanne step-in, 0.8s patient hold)
- **Frames:** Camera flash (blocked) + Sanne Intercept F1/F2 + Sanne Waiting
- **Pattern:** One-shot, triggers on the third sustained close-up photo attempt
- **Trigger:** Extended photography at the observation window
- **Purpose:** "—okay, you're taking a photo, I'll wait." She is not stopping you. She is present.
- **Audio Sync:** Shutter at 0.0s; footstep at 0.8s; no dialogue until 2.2s
- **Performance Optimization:** None needed (one-shot)

### The Speed-Run Reveal (Sheets 7 & 8):
- **Duration:** 3.0 seconds (0.6s panel slide, 2.4s bar fill per section, staggered)
- **Frames:** Section Time Tracker + Speed-Run Comparison Bars + section silhouettes
- **Pattern:** One-shot at the gift shop exit
- **Trigger:** Leaving via the gift shop for the first time
- **Purpose:** 45 seconds in Industrial Hemp. 15 minutes in the Growing Room. 20 minutes in the gift shop. The numbers were always being kept.
- **Audio Sync:** Bars fill to a soft tick per section; no music; the silence after the final bar is the punchline
- **Performance Optimization:** Bars snap to final values instead of filling in reduced-motion mode

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| High-Contrast Exhibit Marker | Sheet 8 (896, 416) | 64x32 | Bold outline for every examinable display across all four floors |
| Terpene Silhouette Set | Sheet 8 (960, 416) | 64x32 | Four terpene options as shape-coded glyphs with text labels |
| Lars High-Contrast Silhouette | Sheet 6 (256, 416) | 64x96 | Enhanced-visibility outline of the ticket-desk NPC |
| Sanne High-Contrast Silhouette | Sheet 6 (448, 416) | 64x96 | Enhanced-visibility outline of the growing-room NPC |
| Accessibility Reserve Block | Sheet 6 (320, 448) | 128x64 | Overflow space for additional high-contrast variants |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static Grow Light | Sheet 8 (320, 128) | 64x64 | Non-shimmering LED plate, bloom held at fixed alpha |
| Static Plants | Sheet 8 (384, 128) | 64x64 | Non-swaying plant plate; glass reflection layer also disabled |
| Dust-Free Plate | Sheet 8 (448, 128) | 64x64 | Clean-air variant with no drifting motes |
| Static Video Screen | Sheet 8 (64, 64) frame 1 | 64x64 | Non-flickering exhibit screen; audio bed retained |
| Instant Speed-Run Bars | Sheet 8 (768, 64) | 256x64 | Bars snap to final values instead of animating |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Creak Glyph | Sheet 8 (0, 128) | 32x32 | Mirrors the old-building ambient creak |
| Grow Room Hum Glyph | Sheet 8 (32, 128) | 32x32 | Mirrors LED and ventilation hum |
| Video Loop Glyph | Sheet 8 (64, 128) | 32x32 | Mirrors the persistent exhibit narration |
| Register Beep Glyph | Sheet 8 (96, 128) | 32x32 | Mirrors the gift shop register |
| School Giggle Glyph | Sheet 8 (128, 128) | 32x32 | Mirrors the random giggle encounter |
| Audio Guide Selected Glyph | Sheet 8 (160, 128) | 32x32 | Mirrors the rare-purchase triumph sting |
| Terpene Correct Glyph | Sheet 8 (192, 128) | 32x32 | Mirrors the mini-game success chime |
| Terpene Wrong Glyph | Sheet 8 (224, 128) | 32x32 | Mirrors the polite-correction sting |
| Tea Pour Glyph | Sheet 8 (256, 128) | 32x32 | Mirrors the complimentary tea cue |
| Footstep (Speed-Run) Glyph | Sheet 8 (288, 128) | 32x32 | Mirrors accelerating footsteps through Industrial Hemp |

### Colorblind Considerations:
- Terpene options are shape-coded glyphs with text labels; the mini-game never depends on jar colour
- Section Time Tracker bars use pattern fills (solid / hatched / dotted / crosshatched) plus numeric minute counts, never colour-coded performance
- Legality and status effects use distinct silhouettes: small-book-with-question-mark (Trivial Knowledge), level line (Calm), zigzag (Embarrassed), column-and-ticket (Cultural Alibi)
- The four floors are distinguishable by architecture and fixture silhouette as well as by lighting grade
- Live Plant vs. Industrial Hemp Plant are distinguished by leaf-count and stem thickness, with text placards — never by tint alone
- Touch zones minimum 44px for all exhibit examines, terpene options, ticket options, and gift shop items

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) all exhibit panels, the Queen Victoria panel, the Prohibition Timeline, zone signage, readable props, and all portraits kept uncompressed
- **Fallback:** PNG high quality for all three floor sheets (the purple grow-light gradient and the gallery spot pools band badly under lossy compression)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| hemp_museum_exhibits | hemp_museum_exhibits | 1024x1024 |
| hemp_museum_characters | npc_hemp_museum_staff, npc_hemp_museum_visitors | 1024x1024 |
| hemp_museum_fx_ui | hemp_museum_fx_ui, hemp_museum_objects | 1024x1024 |

*(The three floor sheets load and unload as paired-room units — only one is ever resident. Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Grow light shimmer, plant sway behind glass with reflection, dust motes on all floors, video flicker, incense wisp, full crowd blocks, animated speed-run bars |
| Medium | Shimmer retained, plant sway at half rate, dust motes in Entry and Historical only, video flicker retained, crowd blocks at reduced count |
| Low | Static grow lights (profile requirement), static plants (profile requirement), reduced dust motes (profile requirement), static video screen, reduced NPC count (profile requirement), snapped speed-run bars |

### Performance Targets:
- **Target FPS:** 60 (per location performance budget)
- **Max Draw Calls:** 16 per frame
- **Memory Footprint:** 38 MB maximum
- **Particle Limit:** 16 (dust motes, aroma wisps, incense, grow shimmer motes)

### Performance Notes:
- Paired-room streaming is the core budget strategy: typical resident footprint is ~17.3 MB (one floor sheet + all atlases); the theoretical all-resident worst case is ~33.6 MB, still inside budget
- School Group, Growing Room Crowd, Gift Shop Queue, and Bros Trio all render as pre-composed single blocks
- Room grade plates are single multiply quads swapped on transition, never per-object tinting
- Plant instances share one AnimatedSprite2D texture with per-instance phase offset — one material, N instances
- Section Time Tracker runs as a lightweight timer dictionary with no per-frame cost

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D (floor backgrounds, exhibits, fixtures), AnimatedSprite2D (plants, grow lights, video screen, staff), CPUParticles2D (dust motes, aroma wisps, incense — not GPU), CanvasLayer (terpene game, ticket panel, shop panel, speed-run reveal), Area2D (every examinable exhibit, smell jars, fabric station, tea station, register)
- Special systems: per-section dwell timer dictionary with silent accumulation and exit-time reveal, Lars shift-arc clock state machine, terpene mini-game with weighted ~10% success, Cultural Alibi global flag, Gift Shop Bag cross-location marker with discard option, audio guide purchase flag altering exhibit flavour text depth, photography-attempt counter driving Sanne's intercept

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Grow light shimmer | LED + ventilation hum bed | Continuous, phase-locked |
| Video exhibit flicker | Muffled narration bed | Continuous, deliberately too quiet |
| Smell jar open | Jar lid + aroma cue | 0.0s of terpene attempt |
| Terpene result | Success chime or polite-correction sting | 3.0s of terpene attempt |
| Audio guide purchase | Triumphant sting (the only one in the building) | 0.4s |
| Camera flash at window | Shutter, then a single footstep | 0.0s / 0.8s of intercept |
| Tea station pour | Complimentary tea cue | On tea collection |
| Gift shop register | Register beep | On any purchase |
| Speed-run bar fill | Soft tick per section, then silence | 0.6-3.0s of reveal |
| Entering Industrial section | Player footstep tempo increases automatically | On section entry |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Cultural Alibi System | Cultural Alibi badge, museum ticket, alibi sparkle, Alibi Track Strip | Visiting sets a global flag usable as "We went to a MUSEUM" in future dialogue; Bravado gain if believed, loss if called out |
| Identify the Terpenes! | Smell jars, terpene game UI, Sanne Terpene Correction, Trivial Knowledge status | ~10% success grants one coffeeshop conversation starter that degrades rapidly |
| The Gift Shop Bag Marker | Gift shop bag sprite and icon, bag marker pulse, marking indicator | Any purchase produces the branded bag; budtenders recognise it; discardable at a style cost |
| The Audio Guide (Rare Path) | Audio guide device, Lars SOLD frame, selection panel | Purchasing unlocks the deeper flavour-text tier on every exhibit and permanently changes Lars's greeting |
| The Speed-Run Reveal | Section Time Tracker, comparison bars, section silhouettes | Silently recorded across the whole visit, surfaced once at the gift shop exit |
| Terpene Knowledge Application | Terpene Reference Card, Trivial Knowledge status | Attempt strain identification at coffeeshops; correct = +Bravado, incorrect = staff correction |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| De Groene Gids | Gift Shop Bag sprite persists as a carried prop | Budtenders recognise the bag and may comment on "doing things backwards"; prices may reflect |
| Café de Schaamte | Cultural Alibi badge in dialogue UI | Bros discuss the "cultural experience" over espresso; Havok is unimpressed |
| The Tolerance Hostel | Gift Shop Bag prop visible in dorm and kitchen scenes | Kitchen gossip may include museum "recommendations"; the alibi can be challenged here |
| Schrödinger's Souvenir | Shared CBD/THC infographic visual language; distinguishable shop bags | Educational counterpart; the two bags must be told apart at 32px |
| Coffeeshop Quarter | Terpene Reference Card, Trivial Knowledge status bar | Unlocks strain/terpene dialogue options that are usually wrong |
| Venustempel (Museum Mile) | Cultural Alibi badge, shared museum-ticket UI style | "We've been to TWO museums" — with decreasing conviction. The Venustempel grants the Cultural Alibi flag outright; the Hemp Museum is the second stamp on it. |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A genuinely good museum with a gift shop bolted to its exit, staffed by one person who still cares"
- **Color Mood:** Museum cream and historic brown throughout, interrupted by one floor of grow-light purple and one room of commercial gold — the palette itself shows you where the money and the interest are
- **Lighting:** Attempted gallery spots achieving dim-with-pools on the exhibit floors; full LED purple in the Growing Room; bright cheerful flood in the gift shop; the only natural light is in the courtyard where nobody goes
- **Texture:** Musty canal-house timber, pristine unfingerprinted exhibit glass, thoroughly fingerprinted observation glass, laminated placards, fresh retail vinyl in the shop

### Environmental Storytelling:
- The Industrial Hemp section is the best-lit, best-signed, best-researched room in the building and it is always empty
- The observation window's glass is covered in fingerprints; every other case in the museum is spotless
- The gift shop occupies more floor area than any exhibit floor and the plan makes no attempt to hide it
- The audio guide rack is always full
- The hemp tea station sits exactly between the stairs and the shop entrance, which is not an accident
- Henrik's bench faces the hemp garden, which is industrial hemp, which is very legal and very boring to look at

### Character Integration Notes:
- Lars is the museum's heart and the museum is killing him slowly; his sprite arc runs on the clock, not on the player
- Sanne never blocks, scolds, or escalates — she steps in, waits, and explains to nobody. She knows everything and is asked nothing.
- Marco is the only staff member whose energy rises across the day, because his floor is the one people use
- Henrik gets a shorter portrait than everyone else in the game, and this is deliberate
- The Actual Enthusiast must be composed to make the player feel mildly guilty from across the room

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Speed-Run Reveal** — 45 seconds in Industrial Hemp, 15 minutes in the Growing Room, 20 minutes in the gift shop, all three bars on one screen
2. **Lars Hopeful vs. Lars Resigned** — the same drawing, side by side, four hours apart
3. **The Empty Rope Room** — a beautifully lit, immaculately signed exhibit with nobody in it
4. **The Growing Room Glass** — purple wash, live plants, and a wall of fingerprints
5. **Henrik on the Bench** — museum polo, name tag, hemp garden, fourth summer, no questions

### Quote Potential:
- "They didn't even look at the rope section. The rope section is FASCINATING."
- "I have a 40-page thesis on hemp rope's role in Dutch maritime history. No one cares."
- "Yes, these are real cannabis plants. Yes, it's legal. We have a licence. Yes, I get that question a lot."
- "Please don't tap on the glass. The plants don't like it. I don't like it either."
- "The gift shop? At the end. Yes, you have to go through the museum. That's... how museums work."
- "The gift shop closes at 9:45. Most people's main question is 'when does the gift shop close.'"
- "Fun fact: George Washington grew hemp. Most people stop listening after I say 'fun fact.'"

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | hemp_museum_floors_a.png | 2048x1024 |
| 2 | hemp_museum_floors_b.png | 2048x1024 |
| 3 | hemp_museum_floors_c.png | 2048x1024 |
| 4 | hemp_museum_exhibits.png | 1024x1024 |
| 5 | hemp_museum_objects.png | 512x256 |
| 6 | npc_hemp_museum_staff.png | 512x512 |
| 7 | npc_hemp_museum_visitors.png | 1024x256 |
| 8 | hemp_museum_fx_ui.png | 1024x512 |

**Total Estimated Memory:** ~17.3 MB typical resident (one floor sheet + all atlases); ~33.6 MB theoretical all-resident worst case. Within the 38 MB location budget.

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `hemp_museum_floors_a.png` (2048x1024)
- [ ] `hemp_museum_floors_b.png` (2048x1024)
- [ ] `hemp_museum_floors_c.png` (2048x1024)
- [ ] `hemp_museum_exhibits.png` (1024x1024)
- [ ] `hemp_museum_objects.png` (512x256)
- [ ] `npc_hemp_museum_staff.png` (512x512)
- [ ] `npc_hemp_museum_visitors.png` (1024x256)
- [ ] `hemp_museum_fx_ui.png` (1024x512)

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
- **Documentation:** Animation timing reference sheet + floor-pair streaming diagram + full exhibit panel copy sheet for localisation + Lars shift-arc clock table

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (#228B22, #F5F5DC, #8B4513, #8B008B, #FFE9A8, #9A9186)
- [ ] Key gags read clearly: the gift shop visibly larger than any exhibit floor, the always-full audio guide rack, the fingerprinted observation glass against spotless exhibit cases, the tea station sitting in the funnel, Henrik's cropped portrait
- [ ] Lars Hopeful and Lars Resigned are the same drawing with only eyes and mouth-corner altered
- [ ] All exhibit panel text is legible at gameplay zoom on a 5-inch display
- [ ] Accessibility visual alternatives included for all audio cues (creak, hum, video loop, register, giggle, audio guide, terpene correct/wrong, tea pour, speed-run footsteps)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (the target is educational pretense and gift shop economics — the hemp history itself is presented as genuinely worthwhile)
- [ ] The Industrial Hemp section is convincingly excellent and convincingly empty
- [ ] Hidden areas/interactions have discoverable visual cues (courtyard door, audio guide rack, fabric station, smell jars, the Growing Guide prop behind the counter)
- [ ] Performance optimized (paired-room streaming, CPU particles, atlas limits respected, static grow-light/plant fallbacks, reduced NPC counts)
- [ ] Touch zone sizing considered (44px minimum for exhibit examines, terpene options, and shop items)
- [ ] Colorblind-friendly alternatives available where color codes meaning (shape-coded terpenes, pattern-filled tracker bars, placarded plant types)
- [ ] Social media viral potential maximized in composition choices (speed-run reveal framing, Lars diptych, empty rope room, fingerprinted glass)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam Roodelicht Row; the museum's own historical panels reference "the Dutch Golden Age" and "the port city," never a real modern city |
| Cultural Specificity | ✅ | Amsterdam's unique museum landscape, Dutch maritime hemp history, cannabis tourism, the hemp-vs-marijuana semantic dance |
| Satirical Targets Appropriate | ✅ | Tourist "educational" pretense and museum gift-shop economics — the hemp history and the staff's expertise are treated as genuinely valuable |
| Seedy Underbelly Present | ✅ | Monetising the gap between education and interest; seeds legal to buy and illegal to grow; the free-tea loss leader funnelling into retail |
| Gameplay Value Established | ✅ | Four-floor navigation, two interactives, hidden speed-run tracker, Cultural Alibi flag, cross-location bag marker, 8-item shop economy |
| Technical Feasibility | ✅ | Paired-room streaming, static grow-light/plant fallbacks per profile, reduced NPC counts per profile, pre-composed crowd blocks |
| Performance Budget | ✅ | 60 FPS, 16 draw calls, 38 MB, 16 particles per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all ten audio cues, reduced-motion set, shape-coded terpenes and tracker bars, 44px touch zones |
| No Crypto Elements | ✅ | Pure museum commerce; the only speculative instrument is a 20 Sovs seed packet |
| Social Media Integration | ✅ | 5 screenshot moments + 7 quotable lines identified |

**Once these assets ship, The Hemp Museum becomes the game's most quietly devastating location: a beautiful, empty room about rope; a purple room full of people; a gift shop bigger than both; and one man at the front desk who wrote forty pages about the empty room and will tell you about it if you stop walking.**
