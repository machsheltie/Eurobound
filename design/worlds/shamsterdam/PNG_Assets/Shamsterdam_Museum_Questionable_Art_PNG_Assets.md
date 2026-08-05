# Shamsterdam Museum of Questionable Art - Complete PNG Asset Requirements

## 📋 Overview
The Shamsterdam Museum of Questionable Art is a Roodelicht Row "museum" that is 90% gift shop with delusions of cultural relevance — three floors of tourist bait funneling every visitor through the Chocolate Anatomy Emporium and past a 4 Sovs "Fabergé-Style Collector's Egg" that the bros treat as a priceless heist target. This document specifies every PNG asset for the location: the four-floor backdrops, gift shop fixtures, Daan and Dennis NPC sheets, atmospheric visitors, heist/NFT effects, and UI. Its satirical essence in a sentence: a cash register wearing a museum as a costume.

**Location ID:** `shamsterdam_roodelicht_museum_questionable_art_01`
**Theme:** Tourist trap "museums" that exist purely to sell merchandise with educational pretense; bachelor party souvenir culture; NFT art satire
**Zone:** Roodelicht Row, wedged between a coffeeshop and a souvenir emporium
**Hours:** 10 AM - 2 AM ("because culture never sleeps"); night access after 10 PM requires Fabergé quest activation
**Primary Function:** Tourist trap shop / Fabergé Egg Hunt heist location (Quest Stage 3) / NFT Hunt site / Couchsurf trigger ("Dennis's Art Studio") — gift shop economy, heist cutscene sequence, NFT minting terminal

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Tourist Trap Red | #CC3333 | Main signage, banners, carpet accents |
| Gift Shop Gold | #FFD700 | Price tags, "collectible" case trim, Fabergé egg foil |
| Questionable Cream | #F5E6D3 | Walls, background surfaces |
| Chocolate Brown | #5D3A1A | Chocolate Anatomy Emporium stock, shelving |
| Red Bulb Glow | #8B1A1A | Upper-floor "atmosphere" lighting accents |
| Fluorescent Wash | #F8F8E8 | Ground-floor harsh overhead lighting |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/museum_questionable_art/
├── environment/
│   ├── museum_backdrops.png
│   └── museum_fixtures.png
├── npcs/
│   ├── npc_daan_cashier.png
│   ├── npc_dennis_artist.png
│   └── npc_museum_visitors.png
├── effects/
│   └── museum_effects.png
└── ui/
    └── museum_ui.png
```

---

## 🏪 Sprite Sheet 1: Museum Floor Backdrops
**File:** `museum_backdrops.png`
**Dimensions:** 2048x1152 pixels
**Color Palette:** Global palette; fluorescent wash dominant on ground floor, red bulb glow on floors 1-3

### Floor Scenes (single-screen backdrops, 1024x576 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Ground Floor — Gift Shop & Entrance | (0, 0) | 1024x576 | 60% gift shop, 40% "exhibits"; spinning racks, testimonials, "No Photography (except in the gift shop)" signage |
| First Floor — "Erotic Arts Through History" | (1024, 0) | 1024x576 | Peep show devices, "historical" erotica frames (abstracted), window photo-op booth, red bulbs |
| Second Floor — "Contemporary Expressions" | (0, 576) | 1024x576 | Inappropriate tulip canvases, sculpture pedestals (one broken), video installation glow |
| Third Floor — "The Vault" | (1024, 576) | 1024x576 | Storage room with rope barriers, dramatic spot on Fabergé case, motion-sensor light track on ceiling |

### Technical Notes:
- Backdrops are static; all animated elements (racks, lights, screens) are separate sprites layered on top
- Third floor backdrop painted darker so the motion-sensor "laser grid" trigger effect reads clearly
- Creaky wooden stair transitions are baked into each backdrop's edge; no separate stairwell scene needed

---

## 🏛️ Sprite Sheet 2: Fixtures & Exhibit Props
**File:** `museum_fixtures.png`
**Dimensions:** 1024x1152 pixels
**Color Palette:** Chocolate Brown + Gift Shop Gold dominant

### Exterior & Gift Shop Anchors:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Exterior facade | (0, 0) | 384x512 | Canal-side storefront, uncertain "MUSEUM" neon, TripAdvisor 3.2 stickers, rotating banner mount |
| Chocolate Anatomy Emporium display | (384, 0) | 512x384 | Tiered floor display, strategic glisten lighting, 4-language bachelor-party signage |
| Fabergé display case | (384, 384) | 256x256 | Glass case, simple latch, "2 for 6 Sovs" sticker, gold-foil eggs stacked inside |
| Cash register station | (640, 384) | 192x128 | Daan's domain: register, phone glow, coupon graveyard |
| NFT QR terminal | (832, 384) | 96x128 | Dennis's scheme; screen shows "Abstract Expression #69" thumbnail |

### Merchandise & Signage (row y=512):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Merchandise rack (4 rotation frames) | (0, 512) | 512x256 (4x 128x256) | Spinning "I ❤️ SHAMSTERDAM" rack, continuous slow rotation |
| Entrance door | (512, 640) | 128x192 | "WELCOME! PUSH TO ENTER :)" glass door with jingle bell |
| Exit-through-gift-shop sign | (640, 640) | 128x64 | "Thank You For Supporting The Arts" |
| PLEASE TAKE ONE sign | (768, 640) | 64x32 | Completely ignored by bros |
| 4 Sovs price tag | (832, 640) | 32x16 | The "priceless" reveal, must read at gameplay zoom |
| Inventory shrinkage clipboard | (864, 640) | 48x64 | Daan's acknowledgment of theft |

### Upper Floor Exhibits (row y=768):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Victorian peep show device | (0, 768) | 128x192 | Coin-operated, mechanical, still works |
| Toilet seat "Masterpiece" | (128, 768) | 96x128 | Mirror in frame — "you are the art" |
| Motion-sensor light bar | (224, 768) | 512x128 | Third-floor ceiling track, the "laser security system" (off state) |
| Sculpture pedestals (3, one broken) | (736, 768) | 192x128 | Second-floor "sculpture garden" |
| Video installation screen | (0, 960) | 256x128 | "Shamsterdam After Dark" YouTube loop frame |
| Chocolate specimens (white/milk/dark) | (256, 960) | 384x96 (3x 128x96) | Neon-marbled, classic, "sophisticated" tiers (abstracted shapes) |
| Premium chocolate shelf | (640, 960) | 192x96 | Top hats, bow ties, googly eyes editions |
| Abstract Expression #69 display | (832, 960) | 64x64 | The NFT in 8-bit pixel glory |
| PLEASE DO NOT TOUCH sign | (896, 960) | 48x32 | Universally ignored |

### Technical Notes:
- Merchandise rack frames play at 0.5 FPS (slow creaky rotation); pause on low LOD
- Fabergé case has a separate open-latch overlay in Sheet 5 effects for the heist climax
- All chocolate anatomy content abstracted per MA-rating art guidelines — suggestive silhouettes, never explicit detail

---

## 👤 Sprite Sheet 3: Daan the Guard/Cashier
**File:** `npc_daan_cashier.png`
**Dimensions:** 256x288 pixels
**Sprite Size:** 64x96 pixels (4 columns x 3 rows)

### Animation Rows:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Row 0: Phone scroll loop (4 frames) | (0, 0) | 256x96 | TikTok eternal scroll, thumb flick, zero investment |
| Row 1: Sigh (2 frames) | (0, 96) | 128x96 | Periodic disappointment exhale |
| Row 1: Not-looking-up (1 frame) | (128, 96) | 64x96 | Heist "neutralization" state — head never rises |
| Row 1: "Drie vijftig" mumble (1 frame) | (192, 96) | 64x96 | Mouth barely moves; bros interpret as "calling for backup" |
| Row 2: Rare look-up (2 frames) | (0, 192) | 128x96 | "Did you guys pay for those magnets?" |
| Row 2: Shrinkage note (2 frames) | (128, 192) | 128x96 | Marks clipboard, returns to phone |

### Technical Notes:
- Idle loop is Row 0 at 1 FPS; all other rows are dialogue/quest triggered
- Daan NEVER faces the player directly during the heist sequence — the joke depends on it
- Phone screen glow rendered as additive 8x12 sub-sprite region baked into frames

---

## 🎨 Sprite Sheet 4: Dennis (CryptoBroArtCollective)
**File:** `npc_dennis_artist.png`
**Dimensions:** 256x288 pixels
**Sprite Size:** 64x96 pixels (4 columns x 3 rows)

### Animation Rows:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Row 0: Idle baseline (2 frames) | (0, 0) | 128x96 | Misplaced passion at rest, gift shop apron |
| Row 0: Glasses adjust (2 frames) | (128, 0) | 128x96 | Pre-monologue tell |
| Row 1: Explaining art (4 frames) | (0, 96) | 256x96 | Passionate gesture cycle — "the blockchain is forever" |
| Row 2: NFT pitch (3 frames) | (0, 192) | 192x96 | Sales mode activation, points at QR terminal |
| Row 2: Studio invitation (1 frame) | (192, 192) | 64x96 | Couchsurf trigger pose — "It's mostly my apartment." |

### Technical Notes:
- Explaining loop at 2 FPS while his dialogue box is open; idle otherwise
- Studio invitation frame appears only after the player examines the NFT (Couchsurf system hook)

---

## 👥 Sprite Sheet 5: Museum Visitors & Manager
**File:** `npc_museum_visitors.png`
**Dimensions:** 768x288 pixels
**Sprite Size:** 64x96 base; groups use 256x96 / 192x96 / 128x96 blocks

### Row 0 (y=0):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bachelor party group — browsing | (0, 0) | 256x96 | Matching "CHAD'S LAST RIDE" shirts, arms filling with chocolate |
| Bachelor party group — checkout frenzy | (256, 0) | 256x96 | "How much for ALL of them?" pose |
| Instagram influencer (2 frames) | (512, 0) | 128x96 | Ring light up, performing for nobody |
| Museum manager (2 frames) | (640, 0) | 128x96 | Sweater vest, clipboard, counting money, approving nod |

### Row 1 (y=96):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Confused family — retreat (2 frames) | (0, 96) | 384x96 (2x 192x96) | Rapid walk toward gift shop exit, child shielded |
| Couple on a dare (2 frames) | (384, 96) | 256x96 (2x 128x96) | One embarrassed, one delighted, both holding bags |
| Ring light prop (standalone) | (640, 96) | 64x96 | Placed separately when influencer poses |

### Row 2 (y=192):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Generic tourist walk cycle (4 frames) | (0, 192) | 256x96 | Shared crowd rig for all floors |
| Generic tourist gawk (2 frames) | (256, 192) | 128x96 | Staring at exhibits, phone raised |
| Bros heist-crouch silhouettes (3 frames) | (384, 192) | 192x96 | Tactical-entry cutscene shapes (hand signals, somersault prep) |
| Bradley yoga-pose "laser dodge" (2 frames) | (576, 192) | 128x96 | Elaborate unnecessary maneuvers under motion lights |

### Technical Notes:
- Visitor groups spawn max 3 concurrently; reduce to 1 on low-end devices per profile crowd rules
- Heist silhouettes used only in the Stage 3 cutscene layer at 25% opacity over normal sprites

---

## ✨ Sprite Sheet 6: Effects & Particles
**File:** `museum_effects.png`
**Dimensions:** 512x384 pixels

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| NFT minting animation (frames 1-4) | (0, 0) | 512x128 (4x 128x128) | 8-bit image loads line by line on phone screen |
| NFT minting animation (frames 5-6) | (0, 128) | 256x128 (2x 128x128) | Mint chime flash, "#69" stamp |
| Fabergé case latch-open overlay (2 frames) | (256, 128) | 128x128 (2x 64x128) | Heist climax — Bradley "cracks it with his bare hands" |
| Register drawer flash | (384, 128) | 64x64 | Purchase completion ka-ching sparkle |
| Motion light trigger (4 frames) | (0, 256) | 512x64 (4x 128x64) | "LASER GRID" activating tile by tile as player walks |
| Dust motes (3 variants) | (0, 320) | 96x32 (3x 32x32) | Museum authenticity particles |
| Chocolate display shine (4 frames) | (96, 320) | 128x32 (4x 32x32) | Inappropriate glisten sweep |
| Peep show activation whir (2 frames) | (224, 320) | 64x32 (2x 32x32) | Mechanical shutter flutter |
| Spotlight cone (Vault) | (288, 320) | 128x64 | Dramatic spot on the 4 Sovs egg |

### Technical Notes:
- Motion light trigger is player-proximity driven; frames advance with movement, not time
- All particles CPUParticles2D-compatible single quads; particle cap 20

---

## 🖥️ Sprite Sheet 7: UI Elements
**File:** `museum_ui.png`
**Dimensions:** 512x448 pixels

### Interface Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bros' interpretation vs. reality split-screen | (0, 0) | 384x256 | Comedic reveal frame: heist fantasy left, TikTok reality right |
| Entrance fee prompt | (384, 0) | 128x96 | "Suggested donation: 15 Sovs" (mandatory) |
| Heist music indicator | (384, 96) | 64x32 | Player-only dramatic soundtrack icon |
| Achievement toast: "Patron of the Arts" | (384, 128) | 128x48 | First gift shop purchase |
| Gift shop purchase popup | (0, 256) | 192x128 | Item acquisition celebration |
| NFT inventory card | (192, 256) | 128x128 | "Abstract Expression #69 — cannot sell, cannot delete" |
| Quest stage banner (Stage 3: The Heist) | (320, 256) | 192x64 | Fabergé Egg Hunt tracker |
| Dennis artist statement scroll | (320, 320) | 192x128 | Pretentious popup on first NFT viewing |
| Touch highlight ring (44px min) | (0, 384) | 48x48 | Interactive object indicator |

### Technical Notes:
- Split-screen art doubles as a marketing/screenshot asset — compose for 16:9 crop
- NFT card uses deliberately ugly 8-bit styling contrasted with polished UI frame

---

## 🎬 Animation Specifications

### Merchandise Rack Rotation (Sheet 2):
- **Duration:** 8 seconds per full rotation (0.5 FPS, 4 frames)
- **Frames:** 4
- **Pattern:** Frame 1 → 4 → loop, continuous
- **Trigger:** Constant while ground floor loaded
- **Purpose:** Gift-shop ambience; creak is part of the soundscape
- **Audio Sync:** Creak SFX on frames 2 and 4
- **Performance Optimization:** Static frame 1 on low LOD

### Daan Phone Scroll (Sheet 3):
- **Duration:** 4 seconds per loop (1 FPS)
- **Frames:** 4
- **Pattern:** Scroll → scroll → pause → thumb flick → loop
- **Trigger:** Constant idle; interrupted only by dialogue rows
- **Purpose:** The "guard" who genuinely does not care
- **Audio Sync:** Occasional muffled TikTok audio blip on frame 3
- **Performance Optimization:** None needed

### Motion-Sensor "Laser Grid" (Sheets 2 & 6):
- **Duration:** 0.8 seconds per light bank (5 FPS)
- **Frames:** 4
- **Pattern:** Off → warm-up flicker → on, advancing bank-by-bank with player position
- **Trigger:** Player proximity on third floor
- **Purpose:** The gap between automatic lights and "military-grade security"
- **Audio Sync:** Fluorescent hum + dramatic sting (player-only heist audio channel)
- **Performance Optimization:** Skip warm-up flicker frame on low LOD

### NFT Minting (Sheet 6):
- **Duration:** 3 seconds (2 FPS, 6 frames)
- **Frames:** 6
- **Pattern:** QR scan → progressive 8-bit load (4 frames) → mint stamp flash, played once
- **Trigger:** Examine QR terminal, confirm 2 Sovs payment
- **Purpose:** "The blockchain is forever. Like art. Like chocolate. Like regret."
- **Audio Sync:** Mint chime on frame 6
- **Performance Optimization:** None needed

### Fabergé Latch Open (Sheet 6):
- **Duration:** 1 second (2 FPS)
- **Frames:** 2
- **Pattern:** Latch lift → case open, hold
- **Trigger:** Heist climax interaction
- **Purpose:** "Pressure-sensitive vault" that is a simple latch
- **Audio Sync:** Tiny click, then triumphant orchestral hit (player-only)
- **Performance Optimization:** None needed

### Dennis Explaining Art (Sheet 4):
- **Duration:** 2 seconds per cycle (2 FPS)
- **Frames:** 4
- **Pattern:** Gesture up → wide → point at terminal → hands to heart, loop while dialogue open
- **Trigger:** Player prompts his "artistic vision"
- **Purpose:** Misplaced passion characterization
- **Audio Sync:** Dialogue voice bleeps synced to gesture beats
- **Performance Optimization:** None needed

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fabergé case outline variant | (896, 384) in Sheet 2 reserve zone | 128x128 | Bold gold outline so the quest target survives high-contrast mode |
| Register/QR terminal outlines | (896, 512) in Sheet 2 reserve zone | 128x128 | Interactive-vendor outline pair |
| Stair/floor-transition arrows | (896, 704) in Sheet 2 reserve zone | 64x64 | High-contrast navigation markers between floors |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Static merchandise rack | Sheet 2 frame 1, (0, 512) | 128x256 | Reduced-motion mode holds rotation frame 1 |
| Non-flicker light bank | Sheet 6, (384, 256) reserve | 128x64 | Motion lights snap on without warm-up flicker |
| NFT mint (no flash) | Sheet 6 frames 1-5 only | 128x128 | Skip stamp-flash frame for reduced-motion mode |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Register ding icon | (48, 384) in Sheet 7 | 48x48 | Visual mirror of purchase ka-ching |
| Heist soundtrack indicator | (384, 96) in Sheet 7 | 64x32 | Already visual by design — player-only music shown as icon |
| Door jingle burst | (96, 384) in Sheet 7 | 48x48 | Entry chime visualization |
| Peep show click marker | (144, 384) in Sheet 7 | 48x48 | Mechanical clicking visual for first floor |

### Colorblind Considerations:
- Fabergé quest target uses shape (egg silhouette + spotlight cone) and gold outline, never color alone
- Motion-light "grid" reads via brightness and tile pattern, not red/green coding
- Touch zones minimum 44px for register, QR terminal, Fabergé case, and all floor-transition stairs

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import); split-screen UI art and Fabergé case need higher quality (readable text/gag detail)
- **Fallback:** PNG high quality for museum_ui.png (text-heavy)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| museum_environment | museum_backdrops (streamed per floor), museum_fixtures | 2048x2048 |
| museum_characters | Daan, Dennis, visitors | 1024x1024 |
| museum_effects | effects, UI | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full display reflections, rack rotation, all visitor groups, dust particles |
| Medium | Simplified reflections, reduced visitor density, half particle rate |
| Low | Static racks, static lighting, single visitor group, no dust (per profile mobile notes) |

### Performance Targets:
- **Target FPS:** 60 (per location profile budget)
- **Max Draw Calls:** 18 per frame
- **Memory Footprint:** 42 MB maximum
- **Particle Limit:** 20

### Performance Notes:
- Load one floor backdrop at a time; the 2048x1152 sheet streams per-region
- Heist cutscene layers (silhouettes, split-screen) load on demand at quest Stage 3 only
- Simplified display reflections and reduced NPC crowd density on older devices (per profile)

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: Sprite2D backdrops per floor, AnimatedSprite2D (NPCs, rack, effects), CPUParticles2D (dust — not GPU), CanvasLayer (UI/split-screen), Area2D proximity triggers for motion lights
- Special systems: heist cutscene state machine (Entry → Gauntlet → Guard → Laser Grid → Vault → Escape), player-only audio bus for heist music, NFT permanence flag (cannot sell/delete), "gift vs kept" purchase tracker

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Entrance door | Cheerful jingle | On door open (bros hear "perimeter breach") |
| Register drawer flash | Cash register ding + "Patron of the Arts" sting | On purchase completion |
| Motion light frames | Fluorescent hum + dramatic heist sting | Frame 3 of each bank activation |
| NFT mint frame 6 | Mint chime | On stamp flash |
| Fabergé latch frames | Tiny click → orchestral hit | Click frame 1, hit frame 2 |
| Daan sigh row | Periodic sigh | Frame 1 of sigh |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Fabergé Egg Hunt (Stage 3: The Heist) | Third floor backdrop, Fabergé case + latch overlay, motion light bars/trigger, Daan not-looking-up, heist silhouettes, split-screen UI | Full heist sequence; debrief at Café de Schaamte |
| NFT Hunt (Shamsterdam #1 of 3) | QR terminal, NFT minting frames, NFT inventory card, Dennis pitch row | Examine Chocolate Anatomy QR terminal |
| Couchsurf: "Dennis's Art Studio" | Dennis studio-invitation frame | Near QR terminal after examining NFT |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Café de Schaamte | Quest banner UI (briefing/debrief) | Agent Havok sends bros here; standard street transition |
| Roodelicht Row | Exterior facade sprite in street strip | Museum sits in tourist-trap concentration |
| The Tolerance Hostel | NFT card + "heist" dialogue callbacks | Kitchen scene: bros brag, guests unimpressed |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A gift shop cosplaying as a cultural institution"
- **Color Mood:** Tourist Trap Red and Gift Shop Gold shouting over Questionable Cream walls; chocolate brown wherever the real business happens
- **Lighting:** Harsh fluorescents failing to be gallery lighting; red bulbs for "atmosphere" upstairs; one sincere dramatic spotlight — on a 4 Sovs egg
- **Texture:** Laminated, shrink-wrapped, price-stickered; the only patina is on the "historical" exhibits printed last month

### Environmental Storytelling:
- Floor space ratio tells the whole joke: gift shop swallows the ground floor, exhibits shrink as you climb
- "PLEASE TAKE ONE" sign beside the "vault" case collapses the heist fantasy in one prop
- TripAdvisor 3.2 stars and BuzzFeed sticker establish the exact tier of institution
- The QR terminal in a chocolate display is the NFT-era update of the postcard rack

### Character Integration Notes:
- Daan is a fixture at the register; he never patrols — the "guard" label is purely the bros' delusion
- Dennis floats between shelf-stocking idle and terminal-adjacent pitch position
- Visitor groups are ambience: they rotate per visit and never interact with the heist layer
- Heist-fantasy overlays render at reduced opacity so reality stays visible underneath — the comedy is the gap

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **Split-screen heist vs. reality** — Bradley "cracking the vault" beside Daan not looking up; built as a shareable 16:9 frame
2. **The 4 Sovs price tag on the "priceless" Fabergé case** — one image, whole satire
3. **The Chocolate Anatomy Emporium** — tiered, glistening, four-language bachelor signage
4. **The toilet seat "Masterpiece"** — "you are the art" mirror selfie bait
5. **NFT minting screen** — "Abstract Expression #69, edition 1 of 47,000"

### Quote Potential:
- "The blockchain is forever. Like art. Like chocolate. Like regret."
- "Those are 4 Sovs. Or 2 Sovs if you buy a keychain. Whatever."
- "The 'laser grid' upstairs? Those are automatic lights. They turn on when you walk. That's how lights work."
- "My collective? Yeah, it's just me. 'Collective' sounds better on grants."
- "hey did you guys ever pay for those magnets"

---

## 📋 Required PNG Files (7 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | museum_backdrops.png | 2048x1152 |
| 2 | museum_fixtures.png | 1024x1152 |
| 3 | npc_daan_cashier.png | 256x288 |
| 4 | npc_dennis_artist.png | 256x288 |
| 5 | npc_museum_visitors.png | 768x288 |
| 6 | museum_effects.png | 512x384 |
| 7 | museum_ui.png | 512x448 |

**Total Estimated Memory:** ~16 MB uncompressed sprite data; ~42 MB location ceiling per profile budget (includes audio, code, atlases)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `museum_backdrops.png` (2048x1152)
- [ ] `museum_fixtures.png` (1024x1152)
- [ ] `npc_daan_cashier.png` (256x288)
- [ ] `npc_dennis_artist.png` (256x288)
- [ ] `npc_museum_visitors.png` (768x288)
- [ ] `museum_effects.png` (512x384)
- [ ] `museum_ui.png` (512x448)

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
- **Backup:** Master PSD/layered file with organized layer groups (per-floor groups mandatory)
- **Documentation:** Animation timing reference sheet + heist cutscene overlay layering guide

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: 4 Sovs tag on the "vault," PLEASE TAKE ONE sign, Daan's unmoving head during the heist, split-screen reveal
- [ ] Accessibility visual alternatives included for all audio cues (register ding, door jingle, heist music, peep show clicks)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (gift shop capitalism wearing museum drag)
- [ ] Hidden areas/interactions have discoverable visual cues (QR terminal glow, Vault spotlight, night-access door state)
- [ ] Performance optimized (CPU particles, per-floor streaming, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (quest target shape/outline coding)
- [ ] Social media viral potential maximized in composition choices (split-screen built as shareable frame)
- [ ] Adult-adjacent exhibit content abstracted to suggestive-silhouette level per MA-rating art guidelines

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam/Roodelicht Row only; "Est. 1996" is in-world |
| Cultural Specificity | ✅ | Amsterdam-style sex-museum tourism + chocolate novelty gift economy |
| Satirical Targets Appropriate | ✅ | Tourist trap economics, bachelor bros, NFT culture — not legitimate museums or artists |
| Seedy Underbelly Present | ✅ | FOMO pricing, "suggested" mandatory donation, shoplifting-as-heist, gift shop funnel |
| Gameplay Value Established | ✅ | Fabergé heist Stage 3, NFT Hunt #1/3, shop economy, Couchsurf trigger |
| Technical Feasibility | ✅ | Per-floor streaming, CPU particles, on-demand heist layers documented |
| Performance Budget | ✅ | 60 FPS, ≤18 draw calls, ≤42 MB per profile budget |
| Accessibility Features | ✅ | Visual mirrors for all audio cues, reduced-motion variants, 44px touch zones |
| No Crypto Elements | ✅ | NFT terminal IS established source material (Dennis's scheme) — satirical target, no real crypto |
| Social Media Integration | ✅ | 5 screenshot moments + split-screen frame designed for sharing |

**Once these assets are delivered, the Shamsterdam Museum of Questionable Art becomes the world's saddest heist target: a place where the player executes "the greatest heist in European history" over a 4 Sovs chocolate egg while a teenager marks it as shrinkage without looking up.**
