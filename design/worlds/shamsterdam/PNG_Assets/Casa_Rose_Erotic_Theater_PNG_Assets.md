# Casa Rosé Erotic Theatre - Complete PNG Asset Requirements

## 📋 Overview
Casa Rosé Erotic Theatre is the pink-neon tourist-trap live show venue on Roodelicht Row where bachelor parties pay 65 Sovs to see something they'll describe incorrectly for decades — a regret factory built on FOMO, drink minimums, and a photogenic pink elephant statue. This document specifies every PNG asset for the venue: the neon exterior with the elephant photo-op landmark, the lobby/bar extraction zone, the theatre space (show content abstracted per profile — the assets cover atmosphere and reactions, never acts), staff NPCs Bogdan/Katya/André/Amber, customer archetypes, drinks and trophy objects, effects, and UI. Its satirical essence in a sentence: everyone came because they felt obligated, everyone will lie about it afterward.

**Location ID:** `shamsterdam_roodelicht_casa_rose_01`
**Theme:** Bachelor party ritual tourism — paying for "experiences" you'll lie about; red light district commodification; mandatory group activities
**Zone:** Roodelicht Row, prime tourist corridor location
**Hours:** 8 PM - 3 AM (shows run hourly on the hour; "special late show" at 1 AM is the same show)
**Primary Function:** Live entertainment venue / bachelor party ritual site — entry/seating/drink-minimum systems, abstracted show reaction mini-game, "Witnessed Something" status, Pink Elephant photo op, story retelling system

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Casa Pink | #FF69B4 | Neon, elephant, wash lighting |
| Neon Hot Pink | #FF1493 | Marquee, spotlights, accents |
| Velvet Purple | #800080 | Walls, rope, upholstery |
| Dim Black | #1A1A1A | House darkness, carpet-age concealment |
| Champagne Gold | #D4AF37 | "Premium" trim, bucket, door handles |
| Fog Grey | #C8C0C8 | Fog machine haze (covers many sins) |

---

## 📁 File Structure
```
assets/sprites/locations/shamsterdam/casa_rose_erotic_theatre/
├── environment/
│   ├── casa_rose_exterior.png
│   ├── casa_rose_lobby_bar.png
│   └── casa_rose_theatre.png
├── npcs/
│   ├── npc_casa_staff.png
│   └── npc_casa_customers.png
├── effects/
│   └── casa_effects.png
├── objects/
│   └── casa_objects.png
└── ui/
    └── casa_ui.png
```

---

## 🌃 Sprite Sheet 1: Exterior & Roodelicht Street
**File:** `casa_rose_exterior.png`
**Dimensions:** 1024x768 pixels

### Facade:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Facade Base | (0, 0) | 512x384 | Pink neon facade in a sea of red; black door, pink trim |
| Neon Marquee Flicker 1-3 | (512, 0) / (768, 0) / (512, 128) | 256x128 each | "CASA ROSÉ — LIVE SHOWS NIGHTLY" flicker states |
| "WORLD FAMOUS BANANA SHOW" Sign | (768, 128) | 192x64 | Featured act sub-sign |
| "PRIVATE SHOWS AVAILABLE" Sign | (768, 192) | 192x32 | Secondary sub-sign |
| "18+ ONLY — NO CAMERAS" Door Sign | (768, 224) | 96x32 | No exceptions (selectively enforced) |
| Pricing Board (Obscured) | (512, 256) | 128x192 | Intentionally hard to read behind promoter |
| Velvet Rope | (640, 256) | 64x192 | Always open, rope remains for "atmosphere" |
| Golden Door Handles | (704, 256) | 32x64 | Shaped like... anatomy (silhouette-suggestive only) |
| Pink Light Spill | (736, 256) | 128x64 | Neon glow pooling on pavement |
| Promoter Engagement Zone Marker | (736, 320) | 128x64 | Bogdan's 20-foot domain decal |

### The Pink Elephant:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pink Elephant Statue | (0, 384) | 256x384 | Life-sized photo ritual site, trunk posed for "hilarious" group shots |
| Graffiti Overlay Clean/Tagged | (256, 384) / (384, 384) | 128x128 each | Tags cleaned daily, reappear nightly; tagged variant carries quest-callback scrawls |

### Street:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Roodelicht Row Background | (256, 512) | 768x256 | Red-lit street context strip, bass-thump district |

### Technical Notes:
- Marquee flicker frames swap randomly; steady frame 1 in reduced-motion mode
- Elephant graffiti overlay swaps nightly (game-day counter); some tags are callbacks to completed quests
- Bass thump from inside pulses pink light spill scale ±5%

---

## 🍸 Sprite Sheet 2: Lobby / Bar Interior
**File:** `casa_rose_lobby_bar.png`
**Dimensions:** 1024x512 pixels

### Fixtures:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Circular Bar | (0, 0) | 384x256 | Compressed entry forces immediate bar interaction |
| Uncomfortable Stools 1-2 | (384, 0) / (416, 0) | 32x64 each | Encourage standing, drinking faster |
| Drink Menu Board | (448, 0) | 192x256 | Names you won't say out loud |
| Velvet Wall Tile | (640, 0) | 256x256 | Tileable; hides questionable stains |
| Mirror Panel Tile | (896, 0) | 128x256 | Mirrors everywhere — disorientation by design |

### Décor:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Vintage Performer Posters 1-3 | (0, 256) / (96, 256) / (192, 256) | 96x128 each | All performers left for "opportunities" |
| Merch Display Case | (288, 256) | 128x128 | Merchandise nobody buys |
| Coin-Op Vintage Machine | (416, 256) | 64x128 | Dubious purpose |
| "CELEBRITY VISITORS" Wall | (480, 256) | 128x128 | Empty frames; photos are "in storage" (lawyers) |
| Pink Champagne Bucket (Décor) | (608, 256) | 64x96 | Never contains champagne, always contains regret |
| Fake Flowers Vase | (672, 256) | 32x64 | Maintenance level: zero |
| Ticket Booth | (704, 256) | 128x192 | 65 Sovs entry, 85 Sovs "premium," group "discounts" |
| Stairway to Theatre | (832, 256) | 192x192 | Pink-lit ascent |
| Aged Carpet Tiles 1-2 | (0, 384) / (32, 384) | 32x32 each | Deliberately dim-lit for a reason |
| Pink Wash Light Cone | (64, 384) | 96x128 | Spot on drink specials |

### Technical Notes:
- Mirror tiles use screen-space reflection fake (flipped sprite at 20% alpha) — no shader cost
- Ticket booth and bar are the two mandatory interaction hotspots (44px+)

---

## 🎭 Sprite Sheet 3: Theatre Space
**File:** `casa_rose_theatre.png`
**Dimensions:** 1024x768 pixels

### Stage (Abstracted — atmosphere only, never acts):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stage with Pole & Chair | (0, 0) | 512x384 | Industrial pole (inspected annually, allegedly), the chair that has seen things; empty-stage dressing only |
| Suspicious Props Basket | (512, 0) | 96x96 | Various props for various acts, closed lid |
| Pre-EU Lighting Rig | (608, 0) | 256x96 | Predates safety standards |
| Emergency Exit Sign Glow 1-2 | (864, 0) / (928, 0) | 64x32 each | Hopefully visible |

### Seating:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Premium Front Row Section | (512, 96) | 384x192 | 85 Sovs total — closest to what you don't want to be close to |
| Seating Occupied Overlay | (512, 288) | 256x96 | Silhouette crowd fill layer |
| Standard Middle Rows | (0, 384) | 512x256 | Bachelor party territory, matching shirts visible |
| Back Standing Room | (512, 384) | 384x192 | 55 Sovs "budget," escape route access |
| House Light Dim Tile | (896, 96) | 128x128 | Ambient darkness tile |

### Atmosphere:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Stage Curtain | (0, 640) | 512x128 | Pink velvet, opens on the hour |
| Low Fog Bank | (512, 640) | 512x128 | Floor-level fog machine output |

### Technical Notes:
- Show sequences render as lighting/fog/crowd-reaction only; camera favors the AUDIENCE (profile: focus on reactions, never acts)
- Premium row has % audience-participation risk — groom-selection spotlight uses Pink Spotlight Beam (Sheet 6)

---

## 👔 Sprite Sheet 4: Staff NPCs
**File:** `npc_casa_staff.png`
**Dimensions:** 512x384 pixels
**Sprite Size:** 64x96 pixels

### Promoter Bogdan:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bogdan Idle 1-2 | (0, 0) / (64, 0) | 64x96 each | Cheap black suit, pink pocket square, rejection-tested smile |
| Bogdan Pitch 1-4 | (128, 0) / (192, 0) / (256, 0) / (320, 0) | 64x96 each | "Special deal, my friend" gesture cycle |
| Bogdan Rejected | (384, 0) | 64x96 | "Okay, okay. You come back later. I am here. Always here." |

### Bartender Katya:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Katya Idle 1-2 | (0, 96) / (64, 96) | 64x96 each | "I've calculated your net worth" expression |
| Katya Upsell 1-3 | (128, 96) / (192, 96) / (256, 96) | 64x96 each | Champagne suggestion choreography |
| Katya Calculating Stare | (320, 96) | 64x96 | Tab-memory activation |

### Door Host André & Server Amber:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| André Idle 1-2 | (0, 192) / (64, 192) | 64x96 each | Large, earpiece for show not function |
| André Pointing Inside | (128, 192) | 64x96 | "Ticket. ID. Inside. Bar is mandatory stop." |
| Amber Walk-in-Dark 1-3 | (192, 192) / (256, 192) / (320, 192) | 64x96 each | Navigates blackness with drink tray |
| André Confiscation Reach | (0, 288) | 64x96 | Ring light enforcement moment |
| Amber Whisper-Offer | (64, 288) | 64x96 | "Another round? Special price during show." |

### Technical Notes:
- Bogdan operates only in the exterior engagement zone; despawns inside
- Amber renders at 60% brightness during shows — visible mostly by tray glint

---

## 🎉 Sprite Sheet 5: Customer NPCs
**File:** `npc_casa_customers.png`
**Dimensions:** 512x384 pixels
**Sprite Size:** 64x96 pixels (groups noted)

### Customers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bachelor Party "DAVE'S LAST RIDE" 1-2 | (0, 0) / (256, 0) | 256x96 each | Eight guys, matching shirts, one sober photographer |
| Confused Couple 1-2 | (0, 96) / (128, 96) | 128x96 each | "You said it was a 'cabaret.'" She's giving him a look |
| Regular (Solo, Since the '80s) 1-2 | (256, 96) / (320, 96) | 64x96 each | Has "his seat"; normal Tuesday energy |
| Influencer Filming / Caught / Escorted | (0, 192) / (64, 192) / (128, 192) | 64x96 each | Ring light despite rules; consequence arc |
| Groom "Selected" Panic 1-2 | (192, 192) / (256, 192) | 64x96 each | Audience participation freeze |
| Crowd Silhouette Strip | (0, 288) | 512x96 | Back-row darkness fill, reaction-wave source |

### Technical Notes:
- Crowd silhouette strip animates via UV offset for reaction waves — one draw call
- Influencer arc mirrors Chadwick's ring light consequence; frames trigger sequentially on detection

---

## ✨ Sprite Sheet 6: Effects & Lighting
**File:** `casa_effects.png`
**Dimensions:** 512x256 pixels

### Effects:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fog Haze Tile | (0, 0) | 256x256 | Tileable fog machine output (covers many sins) |
| Pink Spotlight Beam | (256, 0) | 128x256 | Stage spot / groom-selection beam |
| Glitter Particles 1-4 | (384, 0) to (480, 0), 32px steps | 32x32 each | Persistent glitter — it never fully leaves |
| Neon Glow Halo | (384, 32) | 64x64 | Sign and trim bloom |
| Bass Vibration Lines 1-2 | (448, 32) / (480, 32) | 32x32 each | Seat-felt thump indicator |
| UV Accent Strip | (384, 96) | 128x32 | Blacklight edge glow |
| Illegal Camera Flash | (384, 128) | 64x64 | Someone's always taking photos |
| Discomfort Record-Scratch Lines | (448, 128) | 64x64 | Reaction mini-game fail burst |
| Stage Light Rotation 1-2 | (384, 192) / (448, 192) | 64x64 each | Rotating rig heads |

### Technical Notes:
- Fog via two scrolling tile layers at different speeds; density per LOD (profile: simplified fog on older devices)
- Glitter uses CPUParticles2D, max 15 concurrent
- All strobe-adjacent effects (flash, rotation) have reduced-motion statics — no flashing above 3 Hz anywhere

---

## 🥂 Sprite Sheet 7: Objects & Consumables
**File:** `casa_objects.png`
**Dimensions:** 256x256 pixels

### Drinks (menu table coverage):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "Pink Lady" House Special | (0, 0) | 32x32 | 15 Sovs — exactly as pink as the décor |
| "The Bachelor" | (32, 0) | 32x32 | 18 Sovs — watered down, +Bravado (temporarily) |
| "Champagne" Bottle (Not Actually) | (64, 0) | 32x48 | 95 Sovs — very romantic, very premium |
| "The Forget-Me-Not" | (96, 0) | 32x32 | 20 Sovs — memory becomes vague |
| Heineken | (128, 0) | 24x48 | 12 Sovs — everyone knows you're stalling |
| Water Glass | (152, 0) | 24x32 | 8 Sovs — no effects, but costs 8 Sovs |
| "I Survived Casa Rosé" Shot Glass | (176, 0) | 32x32 | 25 Sovs merch trophy |
| Drink Tray | (208, 0) | 48x32 | Amber's offerings |

### Props & Trophies:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Empty Champagne Bucket (Trophy) | (0, 48) | 64x96 | Party trophy item post-purchase |
| Pink Cash Register | (64, 48) | 96x64 | Transaction completion emphasis |
| No Camera Sign | (160, 48) | 64x32 | Selectively enforced |
| Ticket Stub | (160, 80) | 32x32 | 65 Sovs non-refundable |
| Confiscated Phone Bin | (192, 80) | 64x48 | Ring light graveyard |
| Handheld Drink Menu | (0, 144) | 48x96 | Names you won't say out loud |
| Entry Wristband/Stamp | (48, 144) | 32x32 | Re-entry mark |

### Technical Notes:
- Drink sprites double as bar-order UI icons at native size
- Champagne bucket trophy persists in party inventory as a "we did this" object

---

## 📸 Sprite Sheet 8: UI Elements
**File:** `casa_ui.png`
**Dimensions:** 512x512 pixels

### Interface Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pink Elephant Photo Frame UI | (0, 0) | 384x256 | Group photo composition overlay — everyone's profile picture for one evening |
| Show Schedule Board | (384, 0) | 128x192 | Hourly on the hour; 1 AM "special" (same show) |
| Seating Selection UI | (0, 256) | 256x128 | Front (85 Sovs) / Middle (65 Sovs) / Back (55 Sovs) with mechanics notes |
| Drink Minimum Tracker | (256, 256) | 96x32 | 15 Sovs requirement progress |
| "Witnessed Something" Status Icon | (352, 256) | 64x64 | Applied post-show, lasts until next city |
| Premium Upsell Popup | (256, 320) | 128x64 | "Worth it? That's for you to decide." |
| Audio-Cue Icons 1-3 | (416, 256) to (480, 256), 32px steps | 32x32 each | Bass-thump / announcement / register visual mirrors |
| Story Retelling Variant Cards | (0, 384) | 192x96 | Three contradicting versions (Pilsner/Chadwick/Bradley) |
| Photo Added Notification | (192, 384) | 128x64 | Album update toast |
| Participation Bravado Prompt | (320, 384) | 128x64 | Refuse (lose Bravado) / Participate (lose dignity) |

### Technical Notes:
- Elephant photo frame composites current party sprites + statue + graffiti state
- Retelling cards resurface randomly in later cities via the story system

---

## 🎬 Animation Specifications

### Neon Marquee Flicker (Sheet 1):
- **Duration:** Random 4-8 second steady periods, 0.6-second flicker bursts (3 frames at 5 FPS)
- **Frames:** 3
- **Pattern:** Steady → flicker burst → steady (never faster than 3 Hz)
- **Trigger:** Constant exterior ambient
- **Purpose:** Aging glamour; the district's visual language
- **Audio Sync:** Neon buzz dips during flicker
- **Mobile Optimization:** Steady frame only on Low LOD and reduced-motion

### Fog Drift (Sheets 3, 6):
- **Duration:** Continuous; two layers scrolling at 12s and 20s per screen-width
- **Frames:** 1 tile, dual-layer offset
- **Pattern:** Slow cross-drift, density rises during shows
- **Trigger:** Show start (fog machine activates as lights dim)
- **Purpose:** Covers many sins; abstracts the stage
- **Audio Sync:** Fog machine hiss on density increase
- **Mobile Optimization:** Single layer, 50% density on older devices (profile-mandated)

### Crowd Reaction Wave (Sheets 3, 5):
- **Duration:** 1.5-second wave across silhouette strip (UV offset)
- **Frames:** Strip + occupied overlay
- **Pattern:** Wave ripples back-to-front on show beats
- **Trigger:** Show event scripts; bachelor party whooping
- **Purpose:** The show is told entirely through the audience
- **Audio Sync:** Whoop/gasp samples locked to wave start
- **Mobile Optimization:** Static crowd on older devices (profile-mandated)

### Bogdan Approach Pattern (Sheet 4):
- **Duration:** Pitch cycle 2 seconds (4 frames at 2 FPS), loops while player in engagement zone
- **Frames:** 4 + rejected hold
- **Pattern:** Idle → intercept vector → pitch loop → rejected (holds 2s) → reset
- **Trigger:** Player enters 20-foot sidewalk zone
- **Purpose:** Commission-based persistence as NPC AI
- **Audio Sync:** "My friend!" bark on pitch frame 1
- **Mobile Optimization:** None needed

### Katya Drink Preparation (Sheet 4):
- **Duration:** 1.5-second upsell rhythm (3 frames at 2 FPS)
- **Frames:** 3
- **Pattern:** Pour → present → suggest champagne, single play per order
- **Trigger:** Drink purchase flow
- **Purpose:** Upselling without appearing to
- **Audio Sync:** Cocktail shake + glass clink on frames 1-2; register ka-ching on completion
- **Mobile Optimization:** None needed

### Groom Selection Spotlight (Sheets 3, 6):
- **Duration:** 3-second sweep, then 2-second lock (beam sprite rotation)
- **Frames:** Beam + 2 panic frames
- **Pattern:** Sweep audience → lock on groom-flagged party member → panic frames → choice prompt
- **Trigger:** Front-row seating + bachelor party flag, % chance per show
- **Purpose:** The participation-risk mechanic made visible
- **Audio Sync:** Drumroll during sweep, spotlight clunk on lock
- **Mobile Optimization:** Reduced sweep (fade-in lock only) on Low LOD

### Bass Thump (Sheets 1, 6):
- **Duration:** 0.5-second pulse at 120 BPM ambient
- **Frames:** 2 vibration-line frames + light spill scale
- **Pattern:** Continuous with music bed
- **Trigger:** Constant inside; audible/visible from street
- **Purpose:** You hear Casa Rosé before you see it
- **Audio Sync:** Locked to Euro-dance bass track
- **Mobile Optimization:** Visual pulse only every 4th beat on Low LOD

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Exit route outlines | Sheet 8, (416, 288) | 64x64 | Bold-outline emergency exit and back-row escape path markers |
| Seating section borders | Sheet 8, (480, 288) | 32x64 | High-contrast section dividers for the dim theatre |
| Staff interaction highlight | Sheet 8, (416, 352) | 64x96 | Outline variant marking ticket booth, bar, and Amber as interactive |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Steady marquee | Sheet 1 (Marquee frame 1) | 256x128 | No flicker variant |
| Static fog | Sheet 6 (Fog tile at fixed alpha) | 256x256 | Non-drifting haze |
| Lock-only spotlight | Sheet 6 (Beam static) | 128x256 | No sweep; fade-in only |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bass-thump icon | Sheet 8, (416, 256) | 32x32 | Pulse chip mirroring music bed |
| Announcement icon | Sheet 8, (448, 256) | 32x32 | PA chip for show/lights-dim calls |
| Register ka-ching chip | Sheet 8, (480, 256) | 32x32 | Purchase-emphasis mirror |
| Camera-shutter mirror | Sheet 6, (384, 128) | 64x64 | Elephant photo "click" visual (there's no real camera) |

### Colorblind Considerations:
- Seating tiers labeled with text + price, never pink-shade coding alone
- Drink minimum tracker uses fill + numeric `N SOVS` readout (word lettered, no currency mark)
- Participation prompt options icon-coded (mask/run), not color-coded
- Touch zones minimum 44px for ticket booth, bar, seating select, and photo op

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC (fallback PVRTC 4BPP); marquee and menu board need higher quality (readable neon text)
- **Android:** ETC2 with alpha
- **Fallback:** PNG high quality for Pink Elephant statue (photo-op hero asset)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| casa_environment | exterior, lobby, theatre | 2048x2048 |
| casa_characters | staff, customers | 1024x512 |
| casa_fx_ui | effects, objects, UI | 1024x1024 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Dual-layer fog, glitter particles, crowd waves, full flicker, mirror fakes |
| Medium | Single fog layer, half glitter, wave every other beat |
| Low | Static fog and crowd, no glitter, steady neon (profile-mandated reductions) |

### Performance Targets:
- **Target FPS:** 60 (per location profile performance budget)
- **Max Draw Calls:** 18 per frame
- **Memory Footprint:** 42 MB maximum
- **Particle Limit:** 20 (fog wisps, glitter)

### Performance Notes:
- Three scenes (exterior/lobby/theatre) load independently; theatre only during show hours
- Show sequences are lighting + audio + crowd — no additional performer sprite budget by design
- Mirror reflections are flipped-sprite fakes, zero shader cost

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Node types: TileMap (velvet/carpet/mirror tiles), AnimatedSprite2D (NPCs, marquee, beams), CPUParticles2D (fog wisps, glitter — not GPU), CanvasModulate (house darkness), AudioStreamSync for bass-locked pulses
- Special systems: hourly show scheduler, drink-minimum tracker, seating-section modifiers (participation risk %), reaction composure mini-game with Bravado checks, "no camera" detection (Chadwick ring light = immediate enforcement), story retelling variant generator, pink elephant photo compositor with nightly graffiti state

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Bass vibration lines / light spill | Euro-dance bass bed | Locked 120 BPM |
| Marquee flicker | Neon buzz dip | On flicker burst |
| Bogdan pitch frame 1 | "My friend!" bark | On loop start |
| Katya prep frames | Shake + clink + ka-ching | Frames 1-2, completion |
| Lights-dim + fog | Announcement PA + fog hiss | Show start on the hour |
| Groom spotlight | Drumroll → clunk | Sweep → lock |
| Elephant photo | Shutter click (no camera exists) | On photo confirm |
| Post-show clear | Staff efficiency bustle | Scene transition |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| "Witnessed Something" Status | Status icon, retelling cards | Applied post-show; dialogue references until next city |
| Pink Elephant Photo Ritual | Photo frame UI, statue, graffiti overlays | Auto-album add; ±Bravado by share context |
| Groom Selection | Spotlight beam, panic frames, participation prompt | Front-row bachelor party % event |
| "Veteran" Status | Staff recognition dialogue flags | 2+ visits (unclear if this is good) |
| Drink Minimum | Tracker UI, drink sprites | Required status to remain in venue |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Café de Schaamte | Retelling cards resurface | Next-morning espresso processing scene |
| The Tolerance Hostel | "Did you go to Casa Rosé?" dialogue flags | Guest opinion exchanges |
| De Groene Gids | Impairment level modifier | Pre-visit state affects show experience |
| Roodelicht Row (street) | Background strip, light spill | Seamless corridor walk; elephant visible in other tourists' photos |
| Condomerie Het Gulden Vlies | Shared district palette | "Different end of spectrum" RLD network |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Maximum pink, minimum dignity — a regret factory with a velvet rope nobody closes"
- **Color Mood:** Casa pink and hot neon against dim black; the dark hides the carpet, the pink hides nothing
- **Lighting:** Pink wash everywhere, deliberately dim house, one honest green exit sign; fog diffuses all of it
- **Texture:** Worn velvet, smudged mirrors, industrial pole gleam — glamour at 30 years and 30,000 bachelor parties

### Environmental Storytelling:
- The velvet rope that's always open but never removed is the business model in one prop
- Empty "CELEBRITY VISITORS" frames tell a legal story without a word
- 8 Sovs water on the menu board does more satire than any dialogue
- The pink elephant's nightly graffiti cycle makes the street itself a repeat character

### Character Integration Notes:
- Staff are bored professionals — every animation reads efficiency, never sleaze
- Show content never renders: reactions, lighting, and fog carry the entire sequence (profile mandate)
- The bros' discomfort is the camera's subject; frame audience faces, not the stage

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Pink Elephant Photo** - The bachelor party ritual everyone has and everyone regrets
2. **8 Sovs Water** - Menu board close-up; the purest tourist-trap artifact
3. **The Groom Spotlight** - Panic frames under the pink beam
4. **Three Retellings** - Side-by-side contradiction cards
5. **Influencer Escorted Out** - Ring light consequence arc, Chadwick's mirror

### Quote Potential:
- "You Can't Unsee What You Came To See"
- "World famous banana show. You hear about this? Tonight, special price."
- "Water is... eight Sovs. This is normal."
- "That was... that was definitely... something."
- "You want story to tell? This is story. Trust me. Your grandchildren will... actually, don't tell grandchildren."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | casa_rose_exterior.png | 1024x768 |
| 2 | casa_rose_lobby_bar.png | 1024x512 |
| 3 | casa_rose_theatre.png | 1024x768 |
| 4 | npc_casa_staff.png | 512x384 |
| 5 | npc_casa_customers.png | 512x384 |
| 6 | casa_effects.png | 512x256 |
| 7 | casa_objects.png | 256x256 |
| 8 | casa_ui.png | 512x512 |

**Total Estimated Memory:** ~12 MB raw RGBA texture data; ~42 MB maximum total footprint (location performance budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `casa_rose_exterior.png` (1024x768)
- [ ] `casa_rose_lobby_bar.png` (1024x512)
- [ ] `casa_rose_theatre.png` (1024x768)
- [ ] `npc_casa_staff.png` (512x384)
- [ ] `npc_casa_customers.png` (512x384)
- [ ] `casa_effects.png` (512x256)
- [ ] `casa_objects.png` (256x256)
- [ ] `casa_ui.png` (512x512)

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
- **Documentation:** Animation timing reference sheet + show-sequence lighting script + graffiti rotation table

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly
- [ ] Key gags read clearly: always-open velvet rope, 8 Sovs water, empty celebrity frames, elephant ritual, contradicting retellings
- [ ] Accessibility visual alternatives included for all audio cues (bass, PA, register, shutter)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits
- [ ] Show content fully abstracted — audience reactions and atmosphere only, zero explicit imagery (profile mandate)

### Quality Checkpoints:
- [ ] Satirical theme is clear throughout all assets (obligation tourism, extraction economics)
- [ ] Hidden areas/interactions have discoverable visual cues (graffiti callbacks, back-row escape, veteran recognition)
- [ ] Mobile performance optimized (CPU particles, atlas limits, per-scene loading)
- [ ] Touch zone sizing considered (44px minimum for interactive elements)
- [ ] Colorblind-friendly alternatives available where color codes meaning (tier labels, tracker numerals)
- [ ] Social media viral potential maximized in composition choices (elephant photo framing)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Shamsterdam / Roodelicht Row in-world; profile's "Amsterdam" lines are meta commentary only |
| Cultural Specificity | ✅ | Red-light live show tourism, bachelor party ritual culture |
| Satirical Targets Appropriate | ✅ | Tourist obligation and commercial exploitation; performers and sex workers explicitly not targets — show is abstracted, staff are competent professionals |
| Seedy Underbelly Present | ✅ | Drink minimums, fake champagne, selective camera enforcement, 100 Sovs+ extraction per head |
| Gameplay Value Established | ✅ | Seating/drink systems, reaction mini-game, status effects, photo op, retelling system |
| Technical Feasibility | ✅ | Three-scene loading, fake mirrors, lighting-only show sequences documented |
| Mobile Performance Budget | ✅ | 60 FPS, 18 draw calls, 42 MB per profile budget |
| Accessibility Features | ✅ | Visual audio mirrors, no >3 Hz flashing, reduced-motion variants, 44px zones |
| No Crypto Elements | ✅ | Pure tourist trap commerce |
| Social Media Integration | ✅ | 5 screenshot moments + quote bank identified |

**Once these assets are delivered, Casa Rosé becomes the pinkest monument to peer pressure in Eurobound: the venue every bachelor party enters loudly, exits quietly, and describes three different ways forever — with the elephant photo as the only reliable witness.**
