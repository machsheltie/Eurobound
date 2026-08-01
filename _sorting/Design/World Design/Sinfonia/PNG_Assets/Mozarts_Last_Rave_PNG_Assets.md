# Mozart's Last Rave - Complete PNG Asset Requirements

## 📋 Overview
This document provides exact specifications for all PNG files needed for Mozart's Last Rave — the crypt-club beneath Komponistenfriedhof where the entrance is a fictional composer's grave, the DJs are dead (allegedly), and every fight is fought on the beat. It is a rhythm-combat dungeon with a four-booth mini-boss ring, a three-phase boss who resents Mozart personally, a peaceful resolution that requires finding his lost symphony, and a "secret underground venue" that has a health inspection certificate and 847 online reviews.

**Location ID:** `sinfonia_cemetery_mozarts_last_rave_01`
**Theme:** Classical-music commercialization and death tourism — musical heritage desecrated into a nightclub by people who are, arguably, honoring it better than the opera tourists ever did
**Zone:** Beneath Komponistenfriedhof (Composer's Cemetery)
**Hours:** 11 PM - 5 AM (the dead don't party before midnight)
**Primary Function:** Underground crypt-club / dungeon — rhythm combat, four elemental mini-bosses, three-phase boss with dual resolution, discovery puzzle, couchsurf host, three selfie spots

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Crypt Gray | #808080 | Masonry, catacomb stone, cemetery monuments, fog base |
| Neon Purple | #9400D3 | Club lighting, UV wash, signage, DJ booth glow |
| Bone White | #FFFAF0 | Skeletons, bone décor, glass-floor bones, spectral wisps |
| Death Black | #1A1A1A | Void behind the neon, boss chamber depth, night sky |
| Grave Moss | #4A5A42 | Cemetery surface greens, ivy, weathering (derived surface accent) |
| Dawn Amber | #E8A44C | 5 AM exit light, torch/candle warmth on the surface (derived exit accent) |

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/mozarts_last_rave/
├── environment/
│   ├── mozarts_rave_cemetery.png
│   ├── mozarts_rave_tileset.png
│   └── mozarts_rave_landmarks.png
├── npcs/
│   ├── bassmeister_boss.png
│   ├── mozarts_rave_djs.png
│   └── mozarts_rave_cast.png
├── effects/
│   └── mozarts_rave_effects.png
└── ui/
    └── mozarts_rave_ui.png
```

---

## ⚰️ Sprite Sheet 1: Komponistenfriedhof Surface & Descent
**File:** `mozarts_rave_cemetery.png`
**Dimensions:** 1024x384 pixels
**Color Palette:** #808080 (Crypt Gray), #4A5A42 (Grave Moss), #1A1A1A (Death Black), #E8A44C (Dawn Amber), #9400D3 (Neon bleed on the descent)

### Ground Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cemetery Gravel Path | (0, 0) | 32x32 | Tourist route |
| Grass, Unkempt | (32, 0) | 32x32 | Between plots |
| Grass With Bass Ripple | (64, 0) | 32x32 | Night state — the ground subtly vibrates |
| Cobbled Cemetery Lane | (96, 0) | 32x32 | Main approach |
| Mud Churned By Club Traffic | (128, 0) | 32x32 | Nobody has ever asked about this |
| Flagstone Slab | (160, 0) | 32x32 | Tomb surround |
| Grave Plot Edging | (192, 0) | 32x32 | Border piece |
| Open Grave Mouth | (224, 0) | 32x32 | The entrance, unlidded |

### Walls, Fence & Gates:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Wrought Iron Railing | (0, 32) | 32x64 | Perimeter |
| Cemetery Wall Stone | (32, 32) | 32x64 | Boundary masonry |
| Wall With Ivy | (64, 32) | 32x64 | Weathered variant |
| Gate Pier | (96, 32) | 32x64 | Entry post |
| Cemetery Gate, Closed | (128, 32) | 64x64 | Daytime state |
| Cemetery Gate, Ajar | (192, 32) | 64x64 | Night state, unexplained |

### Signage, Kiosk & The Tourist Trap:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cemetery Signage "Komponistenfriedhof" | (256, 0) | 192x32 | Zone marker |
| Suspicious "Mourner" Queue Decal | (256, 32) | 96x32 | Club wear, 11:40 PM |
| Yelp-Style Review Card, 847 Reviews | (256, 64) | 96x32 | The secret is extremely findable |
| 4.2-Star Plaque, Weathered | (352, 32) | 96x32 | Mounted by the gate, ignored by everyone |
| Ticket Stub | (352, 64) | 48x32 | The €5 pass, retained |
| Cover Charge Sign | (400, 64) | 48x32 | Says "donation" |
| Visitor Pass Kiosk | (448, 0) | 64x96 | Where the "cemetery pass" is sold |
| "Composer's Rest" Pass Board €5 | (512, 0) | 96x32 | Basically club cover |
| Health Inspection Certificate, Framed | (512, 32) | 96x32 | Current, displayed, unread |
| Tax Compliance Notice | (512, 64) | 96x32 | Fifteen years of them |
| Tourist Guide With Umbrella | (608, 0) | 48x96 | Explaining "cultural significance" |

### Monuments, Graves & The Entrance:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Weeping Angel | (0, 96) | 64x128 | Ornate, mossy, unimpressed |
| Ornate Composer Tomb A | (64, 96) | 96x128 | Fictional composer, musical epitaph |
| Ornate Composer Tomb B | (160, 96) | 96x128 | Fictional composer, musical epitaph |
| "Mozart's Grave" (Wrong Grave, Tourist Crowded) | (256, 96) | 96x128 | The decoy; permanently photographed |
| Johann Bassmeister Headstone, 1756–1791 | (352, 96) | 96x128 | Tiny carved speaker icon, easy to miss |
| Bassmeister Headstone, Knocked | (448, 96) | 96x128 | Three knocks in rhythm; sliding open |
| Bassmeister Grave Open, Ladder Down | (544, 96) | 96x128 | The entrance |
| Musical Epitaph Plaque Set | (640, 96) | 96x64 | Reusable inscription variants |
| Tiny Speaker Icon Carving | (640, 160) | 32x32 | The only clue on the surface |
| Wrong-Rhythm Comedy Plaque | (672, 160) | 64x32 | Sad-trombone dialogue trigger |
| Headstone, Generic A | (736, 96) | 48x96 | Filler plot |
| Headstone, Generic B | (784, 96) | 48x96 | Filler plot |
| Broken Column Monument | (832, 96) | 48x128 | Classical grief, mass-produced |
| Mausoleum Door | (880, 96) | 64x128 | Sealed; not the entrance |
| Bench, Mourner's | (944, 96) | 64x48 | Occupied at odd hours |
| Security Guard Post | (944, 144) | 64x80 | Patrols; mysteriously ignores the grave with people climbing into it |
| Wilted Wreath | (640, 192) | 48x32 | Surface dressing |
| Club-Wear "Mourners" Loitering | (688, 192) | 48x96 | Not fooling anyone; not trying to |
| Tourist Cluster, Daytime | (640, 224) | 48x64 | Solemn, photographing the wrong grave |
| Fog At Ground Level, Surface | (736, 192) | 96x48 | Night-only ambient band |
| Ground Vibration Ripple Overlay | (736, 240) | 96x48 | The bass, felt before it is heard |

### The Descent (Transition Zone):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Descent, Stone Upper | (0, 288) | 96x96 | Weathered stone, quiet |
| Descent, Transition Mid | (96, 288) | 96x96 | Stone giving way to neon |
| Descent, Neon Lower | (192, 288) | 96x96 | Fully lit, music loud |
| Spiral Step Tile | (288, 288) | 32x32 | Tileable descent step |
| Dripping Water Detail | (288, 320) | 32x64 | Ambient audio anchor |
| Handrail Section, Bone-Wrapped | (320, 288) | 32x96 | Commitment increases with depth |
| Neon Strip, Purple | (352, 288) | 64x16 | Wall lighting run |
| Bone Decoration, Solemn | (352, 304) | 48x40 | Upper descent |
| Bone Decoration, Party-Themed | (400, 304) | 48x40 | Lower descent; same bones, sunglasses |
| Level Marker "Louder" Sign | (352, 344) | 96x32 | Helpful, honest |
| Cemetery Backdrop, Night | (448, 288) | 288x96 | Parallax layer, 11 PM–4 AM |
| Cemetery Backdrop, Dawn | (736, 288) | 288x96 | Parallax layer, 5 AM exit |

### Surface Set Dressing (upper-right block):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Distant Church Spire Silhouette | (656, 0) | 96x96 | Skyline |
| Chapel Ruin Fragment | (752, 0) | 96x96 | Weathered stone |
| Yew Tree | (848, 0) | 96x96 | Cemetery standard |
| Lamp, Cemetery | (944, 0) | 32x96 | Sparse, sodium-warm |

### Technical Notes:
- **The wrong grave and the right grave must be equally impressive.** The joke fails if Bassmeister's headstone looks special — the only distinguishing mark is a 32x32 speaker icon that is genuinely easy to miss
- The Bassmeister headstone ships in three aligned states (idle / knocked / open); all three share the same base geometry so the slide animation lands
- Ground Vibration Ripple is a night-only additive overlay on the grass and lane tiles, never on the daytime state
- Dawn backdrop is used exactly once per playthrough — the 5 AM exit — and carries the "Back from the Dead" selfie
- Regions x976–1024 (y0–96) and x800–944 (y192–288) are reserved padding

---

## 💀 Sprite Sheet 2: Crypt-Club Interior Tileset
**File:** `mozarts_rave_tileset.png`
**Dimensions:** 1024x512 pixels
**Color Palette:** #808080 (Crypt Gray), #9400D3 (Neon Purple), #FFFAF0 (Bone White), #1A1A1A (Death Black)

### Floor Tiles (32x32 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Crypt Flagstone | (0, 0) | 32x32 | Base catacomb floor |
| Catacomb Bone-Set Floor | (32, 0) | 32x32 | Bones set into mortar |
| Glass Dancefloor Panel, Lit | (64, 0) | 32x32 | Underlit, bones visible |
| Glass Dancefloor Panel, Dark | (96, 0) | 32x32 | Between beats |
| Bones Under Glass Layer | (128, 0) | 32x32 | Sub-layer, obviously fake |
| Bone Bar Alcove Floor | (160, 0) | 32x32 | Entry area |
| Requiem Room Rug | (192, 0) | 32x32 | VIP softness |
| Conductor's Crypt Marble | (224, 0) | 32x32 | Boss arena, ornate |
| Bass Pit Floor, Safe | (256, 0) | 32x32 | Between drops |
| Bass Pit Floor, Charged | (288, 0) | 32x32 | Damage state |
| Bone Pile Floor, Intact | (320, 0) | 32x32 | Steppable on-beat |
| Bone Pile Floor, Collapsed | (352, 0) | 32x32 | Stepped off-beat |

### Wall & Ceiling Tiles:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Crypt Masonry | (0, 32) | 32x64 | Base wall |
| Masonry With Niche Skulls | (32, 32) | 32x64 | Catacomb standard |
| Neon-Lit Surface | (64, 32) | 32x64 | Club conversion |
| UV Underlit Panel | (96, 32) | 32x64 | Dancefloor perimeter |
| Catacomb Arch Segment | (128, 32) | 32x64 | Passage framing |
| Tombstone Speaker Wall | (160, 32) | 32x64 | Speakers shaped as headstones |
| Requiem Velvet Drape Wall | (192, 32) | 32x64 | VIP quiet |
| Boss Chamber Ornate Wall | (224, 32) | 32x64 | Deepest level |
| Vaulted Ceiling Rib | (256, 32) | 64x64 | Overhead structure |
| Ceiling Bone Chandelier Mount | (320, 32) | 32x64 | Fixture anchor |

### The Bone Bar (Entry Area):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bone Bar Counter, Long | (0, 96) | 160x64 | Built into crypt alcoves |
| Bar Alcove Arch | (160, 96) | 64x96 | Original masonry, repurposed |
| Coffin-Lid Seat | (224, 96) | 48x32 | Surprisingly comfortable |
| Femur Bar Stool | (272, 96) | 24x48 | Commits to the bit |
| Rib Cage Coat Rack | (296, 96) | 32x64 | Commits harder |
| Pelvic Bowl For Tips | (328, 96) | 32x24 | "Tips for the dead" go to owners |
| Tombstone Menu Plaque | (360, 96) | 48x64 | Menu carved as epitaphs |
| Skull Glass Shelf | (408, 96) | 64x32 | It's from IKEA |
| Smoking Skeleton Decoration | (472, 96) | 48x80 | Fog-machine powered |
| "RIP Your Sobriety" Neon Sign | (520, 96) | 128x32 | The club's signature |
| Spine Glow-Stick Merch Rack | (648, 96) | 48x64 | Merchandise |
| Fog Machine, Visible | (696, 96) | 32x32 | Not hidden; nobody minds |
| Bar Back Bottle Rack | (728, 96) | 96x64 | Standard stock |
| Skull Tap Handles | (824, 96) | 48x32 | Draught |
| Helga's Station Detail | (872, 96) | 64x64 | The only living employee's post |

### Club Fittings & VIP:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Coffin-Lid Bench Row | (0, 160) | 128x64 | Seating run |
| Bone Pile Décor | (128, 160) | 32x32 | Ambient |
| Skull Sconce | (128, 192) | 32x32 | Wall light |
| Catacomb Niche, Occupied | (224, 160) | 64x64 | Original tenant |
| Catacomb Niche, Party-Dressed | (288, 160) | 64x64 | Same tenant, glow sticks |
| Velvet Rope, VIP | (352, 160) | 48x24 | Requiem Room gate |
| VIP Sign "Requiem Room" | (352, 184) | 48x24 | Post-completion access |
| Classical Cocktail Shelf | (400, 176) | 64x48 | Drinks named after compositions |
| Ghost Appearance Marker | (464, 176) | 56x48 | Occasional ghost NPC spawn point |
| Requiem Coffin-Cushion Seating | (520, 160) | 96x64 | Couchsurf bed; "Restful Death" |
| Bone Throne Dais | (616, 160) | 96x64 | Selfie spot platform |
| Skeletal Chandelier Mount Low | (712, 160) | 48x64 | Fixture anchor |
| Pipe Organ Base Section | (760, 160) | 96x64 | Boss domain footing |
| Boss Chamber Dais | (856, 160) | 96x64 | Raised performance floor |

### Dancefloor Architecture & Hazards:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Descent Arrival Arch | (0, 224) | 96x128 | Where the staircase lets out |
| Dancefloor Perimeter Rail | (96, 224) | 128x32 | Crowd boundary |
| Strobe Rig | (224, 224) | 96x32 | Overhead |
| Laser Emitter | (320, 224) | 48x32 | Fog-diffused |
| Fog Vent Grille | (368, 224) | 48x32 | Floor-level |
| UV Tube Strip | (416, 224) | 96x16 | Perimeter run |
| Neon Purple Strip | (416, 240) | 96x16 | Perimeter run |
| Skull Disco Ball Mount | (512, 224) | 48x32 | Ceiling fixture |
| Tombstone Speaker, Large | (96, 256) | 64x96 | Bass source |
| Tombstone Speaker, Small | (160, 256) | 48x64 | Fill |
| DJ Booth Plinth | (208, 256) | 64x64 | Cardinal-direction base |
| Bone Piles, Stepping Hazard | (272, 256) | 48x64 | Collapse if stepped off-beat |
| Bass Pit, Marked | (320, 256) | 64x64 | Damages on bass drops |
| Fog Bank Volume | (384, 256) | 64x64 | Reduced visibility zone |
| Strobe Zone Volume | (448, 256) | 64x64 | Timing-disruption zone |
| Coffin Alcove Cluster | (512, 256) | 48x64 | Wall recess set |
| Catacomb Passage, Branching | (560, 224) | 128x128 | Navigation between areas |
| Boss Arena Floor Inlay | (688, 224) | 128x128 | Conductor's Crypt, acoustically ornate |
| Organ Pipe Bank | (816, 224) | 96x128 | Boss chamber wall |
| Requiem Room Interior Wall | (912, 224) | 112x128 | VIP enclosure |

### Floor Decals:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Glass Panel Crack Detail | (160, 320) | 48x32 | Wear |
| Bone Under-Glass Detail | (208, 320) | 64x32 | Close-up sub-layer |
| Footprint Glow Decal | (272, 320) | 48x32 | UV-reactive |
| Bass Shockwave Floor Decal | (320, 320) | 64x32 | Drop marker |
| Danger Decal, Bone Pile | (384, 320) | 64x32 | Hazard telegraph |
| Neon Floor Arrow | (448, 320) | 64x32 | Wayfinding |
| Coffin Lid, Open | (512, 320) | 48x32 | Prop state |

### Backdrop / Parallax Layers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Catacomb Backdrop Far | (0, 352) | 384x160 | Slow parallax |
| Dancefloor Crowd Silhouette Layer | (384, 352) | 320x160 | Mid parallax, bass-reactive scale |
| Boss Chamber Backdrop | (704, 352) | 320x160 | Static, no parallax |

### Technical Notes:
- The glass dancefloor is authored as two tiles (lit/dark) plus a shared bone sub-layer; the beat drives which tile is drawn, so the floor pulses without a shader
- Every bone in this location is visibly plastic on close inspection. The skeletal chandelier is "composer remains" and reads as prop-shop at 1x zoom
- Bass Pit and Bone Pile hazard tiles must telegraph their state through *shape* change, not colour alone (charged pit has raised edge geometry; collapsed pile is visibly lower)
- Region x936–1024 (y96–160) is reserved padding

---

## 🎛️ Sprite Sheet 3: Booths, Organ & Bone Landmarks
**File:** `mozarts_rave_landmarks.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #9400D3 (Neon Purple), #FFFAF0 (Bone White), #1A1A1A (Death Black), #808080 (Crypt Gray)

### The Four DJ Booths:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| DJ Booth North (Bass) | (0, 0) | 192x128 | Grave-o's station; subwoofer stack shaped as a sarcophagus |
| DJ Booth East (Treble) | (192, 0) | 192x128 | Soprano Specter's station; horn array |
| DJ Booth South (Rhythm) | (0, 128) | 192x128 | Tempo Mortis's station; clock-face decks |
| DJ Booth West (Melody) | (192, 128) | 192x128 | Harmony Haunt's station; harp-strung console |

### Bone Throne & Overhead:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Skull Disco Ball, Frame A | (384, 0) | 64x64 | Rotation frame A |
| Skull Disco Ball, Frame B | (448, 0) | 64x64 | Rotation frame B |
| Bone Throne, Empty | (384, 64) | 64x96 | "Composer bones," obviously fake |
| Bone Throne, Occupied (Selfie) | (448, 64) | 64x96 | "King/Queen of the Dead" |
| Crown Of Skulls Prop | (384, 160) | 32x32 | Available prop |
| Bone Throne Dais Close | (384, 192) | 32x64 | Base detail |
| Skeletal Chandelier | (416, 160) | 96x96 | Plastic, magnificent |

### The Conductor's Crypt & Bar Heroes:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pipe Organ Synthesizer, Full | (0, 256) | 192x128 | Converted; the boss's domain and his undoing |
| Organ Keyboard Detail | (192, 256) | 96x48 | Playable during Phase 3 wind-up |
| Organ Stops, Relabeled As Faders | (192, 304) | 96x48 | Someone did this with a label maker |
| Organ Bench, Bone | (192, 352) | 96x32 | Seat |
| Bone Bar, Hero Prop | (288, 256) | 128x64 | Wide-shot bar composition |
| Skull Glass Rack | (288, 320) | 64x48 | Vessel storage |
| Coffin-Lid Seat Cluster | (352, 320) | 64x48 | Grouped seating |
| Floor Cable Snake | (288, 368) | 128x16 | Gaffer-taped, unglamorous, real |
| Glass Dancefloor Hero Panel | (416, 256) | 96x64 | Wide-shot floor composition |
| Requiem Room Hero Prop | (416, 320) | 96x64 | VIP wide-shot composition |

### Technical Notes:
- The four booths share one silhouette footprint so the cardinal-direction arena reads as symmetrical; only the instrument metaphor differs
- The pipe organ must read as *converted*, not built: original pipework with modern faders bolted on, and a visible label-maker strip over the stops
- The floor cable snake is the location's honesty gag — the "supernatural" venue is gaffer-taped like every real club

---

## 🎧 Sprite Sheet 4: Johann Bassmeister — The Undead DJ
**File:** `bassmeister_boss.png`
**Dimensions:** 512x768 pixels
**Color Palette:** #FFFAF0 (Bone White), #1A1A1A (18th-century formal wear), #9400D3 (Neon Purple rim light), #808080 (Crypt Gray)

### Introduction & Phase 1 — The Warmup (100–66% HP), 128x192 each:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Boss Intro, Rising From Organ | (0, 0) | 128x192 | "Ah, more TOURISTS!" |
| Phase 1 Idle | (128, 0) | 128x192 | Skeleton in 18th-c formal wear, modern DJ headphones. 120 BPM, steady |
| Phase 1 "Ghostly Groove" | (256, 0) | 128x192 | Party must match rhythm or take damage |
| Phase 1 "Bass from the Grave" | (384, 0) | 128x192 | Ground-pound AOE on bass drops |

### Phase 2 — The Breakdown (66–33% HP), 128x192 each:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Phase 2 Idle | (0, 192) | 128x192 | Tempo fluctuating 80–160 BPM |
| Phase 2 "Tempo Terror" | (128, 192) | 128x192 | Sudden shifts that scramble timing |
| Phase 2 "Skeleton Shuffle" Summon | (256, 192) | 128x192 | Calls dancing skeleton adds |
| Phase 2 "Drop of Death" | (384, 192) | 128x192 | Massive bass drop, delayed damage |

### Phase 3 — The Finale (33–0% HP), 128x192 each:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Phase 3 Idle | (0, 384) | 128x192 | Boss-controlled tempo, reactive |
| Phase 3 "Eternal Encore" | (128, 384) | 128x192 | Loops damage until the cycle is broken |
| Phase 3 "Symphony of Suffering" | (256, 384) | 128x192 | Uses all four elemental DJ attacks |
| Phase 3 "Last Rave" Wind-Up | (384, 384) | 128x192 | Long telegraph; the organ window opens here |

### Resolutions, 128x192 each:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Defeat, Combat Resolution | (0, 576) | 128x192 | "If I can't be REMEMBERED... I'll make sure you NEVER FORGET!" |
| Appeasement, Lost Composition Presented | (128, 576) | 128x192 | The symphony held up; he stops |
| Appeased Idle — Vendor Stance | (256, 576) | 128x192 | Becomes a vendor; "Dance here anytime." |
| Appeased, Offering Spectral Breakfast | (384, 576) | 128x192 | Couchsurf morning; not edible |

### Animation Timing:
- Phase idle loops: 3fps, 4-frame internal sub-cycle authored within each idle cell's alpha layers (head bob + arm), looped continuously
- Attack telegraphs: 4fps, single play, wind-up length scales with phase (Phase 1: 1.0s, Phase 2: 0.7s, Phase 3: 0.5s except "Last Rave" at 3.0s)
- "Last Rave" wind-up: 3.0s hold — the entire mechanic is that this window is long enough to reach the organ
- Phase transitions: 1.2s, single play, tempo audibly resets on the transition frame
- Appeasement sequence: 4.0s, single play, no reversal; the boss music decays into strings

### Character Notes:
- Theatrical, bitter, and genuinely wounded about Mozart. Every hostile frame is a performance; every appeased frame is not
- The 18th-century formal wear must be period-correct enough to read against the modern headphones — the collision is the character
- Whether he is a real ghost, a hallucination, or a very good performer is **deliberately ambiguous and must remain so in the art.** No frame may resolve it: no visible harness, no seam, no wire, and equally no unambiguous supernatural tell
- The appeased sprite is the same skeleton with the tension gone out of the shoulders. Do not soften the design; soften the posture

---

## 🎚️ Sprite Sheet 5: The Four Elemental Undead DJs
**File:** `mozarts_rave_djs.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #9400D3 (Neon Purple), #FFFAF0 (Bone White), #1A1A1A (Death Black), per-element accent rim

### Mini-Bosses (128x192 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| DJ Grave-o (Bass), North | (0, 0) | 128x192 | "Feel it in your BONES... because I don't have any FLESH." |
| DJ Soprano Specter (Treble), East | (128, 0) | 128x192 | "My voice could shatter GLASS. Your skull is... slightly thicker." |
| DJ Tempo Mortis (Rhythm), South | (256, 0) | 128x192 | "Time is RELATIVE. Death is ABSOLUTE." |
| DJ Harmony Haunt (Melody), West | (384, 0) | 128x192 | "Such BEAUTIFUL chaos... let me add some STRUCTURE." |

### Attack Poses & Markers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Grave-o Bass Shockwave Pose | (0, 192) | 64x64 | Floor shockwave cast |
| Soprano Shatter-Note Pose | (64, 192) | 64x64 | Dazed-inflicting high note |
| Tempo Mortis Time-Distort Pose | (128, 192) | 64x64 | Party movement slowed |
| Harmony Haunt Charm Pose | (192, 192) | 64x64 | Targeting confusion |
| Weakness Marker: High-Frequency | (256, 192) | 32x32 | Counters Grave-o |
| Weakness Marker: Bass | (288, 192) | 32x32 | Counters Soprano Specter |
| Weakness Marker: Tempo-Change | (320, 192) | 32x32 | Counters Tempo Mortis |
| Weakness Marker: Dissonance | (352, 192) | 32x32 | Counters Harmony Haunt |
| Booth Nameplate Set | (256, 224) | 128x32 | Four carved plaques |
| Elemental Icon Row | (384, 192) | 128x32 | Bass / Treble / Rhythm / Melody |
| Mini-Boss Defeated Slump Set | (384, 224) | 128x32 | Four collapse poses, small |

### Technical Notes:
- Each DJ needs a distinct silhouette at 128x192: Grave-o is wide and low, Soprano Specter is tall and thin, Tempo Mortis is angular, Harmony Haunt is flowing
- Weakness markers are shape-coded (spike / wave / clock / broken-chord glyph) so the counter system reads without colour
- All four are visibly the same *kind* of thing as Bassmeister — they are "his orchestra" and the family resemblance is the lore

---

## 🦴 Sprite Sheet 6: Enemies, Staff, Ghosts & The Party
**File:** `mozarts_rave_cast.png`
**Dimensions:** 512x384 pixels
**Color Palette:** #FFFAF0 (Bone White), #9400D3 (Neon rim), #808080 (Crypt Gray), living-NPC earth tones

### Standard Enemies (64x96 unless noted):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dancing Skeleton A | (0, 0) | 64x96 | Basic rhythm enemy, attacks on beat |
| Dancing Skeleton B | (64, 0) | 64x96 | Off-phase variant |
| Grave Groover A | (128, 0) | 64x96 | Faster, tighter timing windows |
| Grave Groover B | (192, 0) | 64x96 | Off-phase variant |
| Skeleton Dancer Ambient A | (256, 0) | 64x96 | Background crowd |
| Skeleton Dancer Ambient B | (320, 0) | 64x96 | Background crowd |
| Spectral Heckler | (384, 0) | 64x96 | Appears when rhythm breaks; applies Embarrassed |
| Spectral Heckler, Jeering | (448, 0) | 64x96 | Active mockery frame |

### Blockers & Combat Detail:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tombstone Bouncer, Blocking | (0, 96) | 96x128 | Blocks paths until a rhythm challenge is passed |
| Tombstone Bouncer, Passed | (96, 96) | 96x128 | Steps aside, unimpressed |
| Skeleton, Rhythm Challenge Pose | (192, 96) | 64x96 | Call-and-response stance |
| Skeleton, On-Beat Strike | (256, 96) | 64x96 | Bonus-damage window |
| Skeleton, Off-Beat Stumble | (320, 96) | 64x96 | Off-Key debuff visual |
| Bone Rattle Detail | (384, 96) | 32x32 | Close-up prop |
| Xylophone Hit Glyph | (416, 96) | 32x32 | Hit-confirm prop |
| Skeleton Head, Bobbing A | (448, 96) | 32x32 | Ambient loop frame |
| Skeleton Head, Bobbing B | (480, 96) | 32x32 | Ambient loop frame |
| Skeleton Pile, Reassembling | (384, 128) | 64x64 | Post-defeat recovery |
| Skeleton Limb, Detached | (448, 128) | 64x64 | Comedy debris |

### Living Staff & Ghosts (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Helga The Bartender, Pouring | (0, 192) | 64x96 | Somehow looks MORE alive surrounded by undead |
| Helga, Unflappable | (64, 192) | 64x96 | "It's from IKEA." |
| Helga, Couchsurf Offer | (128, 192) | 64x96 | Twenty years here; the dead don't micromanage |
| The Grave Guide, Too Into The Bit | (192, 192) | 64x96 | Living person in a badly fitting skeleton costume |
| The Grave Guide, Rhythm Tutorial | (256, 192) | 64x96 | "...okay, the rhythm tutorial is this way." |
| Ghost Groupie A | (320, 192) | 64x96 | Translucent, period-inappropriate clothing |
| Ghost Groupie B | (384, 192) | 64x96 | Variant |
| Ghost Groupie C | (448, 192) | 64x96 | Variant |

### The Bros & The Reality (64x96 each):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lord Pilsner, Climbing Into Grave | (0, 288) | 64x96 | "The most metal thing we've ever done." |
| Lord Pilsner, Skull Glass | (64, 288) | 64x96 | "Do you think it's... REAL?" |
| Chadwick, Dancing With Skeleton | (128, 288) | 64x96 | "Coolest or most cursed moment of my life!" |
| Chadwick, Content Warning Pose | (192, 288) | 64x96 | "DEFINITELY against several laws." |
| Bradley, Refusing To Dance | (256, 288) | 64x96 | "I refuse to dance." |
| Bradley, 12% Uncertain | (320, 288) | 64x96 | "There is a 0% probability of actual reanimation." |
| Theatre Student In Costume, Off-Shift | (384, 288) | 64x96 | €15/hour; the morning-after reality |
| Theatre Student, Ill-Fitting Skeleton Suit | (448, 288) | 64x96 | Seam visible only here, never on the floor |

### Character Notes:
- **The theatre-student sprites are the only place the illusion breaks**, and they only appear off the dancefloor. On the floor, nothing resolves the ambiguity
- Ghost Groupies are translucent (60% alpha) with a bone-white rim; their clothing is period-mismatched in a way that reads at 64px
- Helga is drawn at full opacity and warmer saturation than everyone else in the room — she is the anchor
- The Grave Guide's costume must fit badly in a specific, consistent way (shoulder seam, ankle gap) across both frames

---

## 🌫️ Sprite Sheet 7: Fog, Lasers, Bass & Comedy Stings
**File:** `mozarts_rave_effects.png`
**Dimensions:** 512x256 pixels
**Color Palette:** #9400D3 (Neon Purple), #FFFAF0 (Bone White), #808080 (Fog Gray), #E8A44C (Dawn Amber)

### Fog:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fog Bank Frame A | (0, 0) | 128x64 | Heavy roll, frame A |
| Fog Bank Frame B | (128, 0) | 128x64 | Frame B |
| Fog Bank Frame C | (256, 0) | 128x64 | Frame C |
| Fog Roll, Low Density | (384, 0) | 128x64 | Medium/Low LOD substitute |

### Lighting:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Strobe Flash Overlay | (0, 64) | 96x64 | Full-screen white pop |
| Strobe Off Frame | (96, 64) | 96x64 | Motion-safe held state |
| Laser Fan A | (192, 64) | 96x64 | Fog-diffused sweep |
| Laser Fan B | (288, 64) | 96x64 | Second position |
| UV Underglow Wash | (384, 64) | 128x64 | Dancefloor perimeter bloom |

### Bass & Rhythm:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bass Shockwave Ring 1 | (0, 128) | 64x64 | Drop impact, inner |
| Bass Shockwave Ring 2 | (64, 128) | 64x64 | Expanding |
| Bass Shockwave Ring 3 | (128, 128) | 64x64 | Dissipating |
| Bass-Reactive Particle Burst | (192, 128) | 64x64 | Floor-panel pulse |
| Spectral Wisp A | (256, 128) | 32x64 | Ambient ghost trail |
| Spectral Wisp B | (288, 128) | 32x64 | Frame B |
| Bone Dust Puff | (320, 128) | 48x48 | Skeleton hit/collapse |
| Crescendo Aura | (368, 128) | 64x64 | Full Harmony Meter, all attacks critical |
| Harmony Meter Glow | (432, 128) | 80x64 | Combo build feedback |

### Comedy Stings, Cue Glyphs & Motion-Safe Variants:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sad Trombone Glyph | (0, 192) | 48x32 | Wrong-rhythm knock on the headstone |
| Bone Rattle Glyph | (48, 192) | 32x32 | Skeleton movement audio marker |
| Xylophone Sting Glyph | (80, 192) | 32x32 | Skeleton hit audio marker |
| Off-Key Glyph | (112, 192) | 32x32 | Missed-beat debuff marker |
| On-Beat Hit Ring | (144, 192) | 32x32 | Successful timing marker |
| Bass Drop Cue Glyph | (176, 192) | 48x32 | Incoming drop, visual advance warning |
| Tempo Shift Glyph | (224, 192) | 48x32 | Phase 2 tempo change warning |
| Ghost Mockery Glyph | (272, 192) | 32x32 | Spectral Heckler audio marker |
| Screen Shake Marker | (304, 192) | 32x32 | Impact indicator (shake-free alternative) |
| Pipe Organ Blast Glyph | (336, 192) | 48x32 | Phase 3 counter-attack marker |
| Dawn Light Shaft | (384, 192) | 64x64 | 5 AM surface exit |
| Skull Disco Reflection Specks | (448, 192) | 64x64 | Rotating light scatter |
| Static Fog Frame (Motion-Safe) | (0, 224) | 128x32 | No roll |
| Non-Flashing Strobe Substitute | (128, 224) | 128x32 | Steady wash replacing the flash |
| Reduced-Motion Laser Static | (256, 224) | 128x32 | Fixed fan position |

### Technical Notes:
- **The strobe requires a photosensitivity guard.** Default flash rate must not exceed 3Hz, and the Non-Flashing Strobe Substitute must be the *automatic* asset whenever Reduced Motion or Photosensitivity mode is enabled — not an opt-in
- Fog is the heaviest particle load in the location: it is pre-rendered as three looping frames, not simulated
- Bass Shockwave Rings are the only effect permitted to drive screen shake; the Screen Shake Marker glyph substitutes when shake is disabled
- Bass-reactive particles read the same beat clock as the glass floor tiles so the whole room pulses together

---

## 🖥️ Sprite Sheet 8: Rhythm HUD, Boss UI & Items
**File:** `mozarts_rave_ui.png`
**Dimensions:** 256x288 pixels
**Color Palette:** #9400D3 (Neon Purple), #FFFAF0 (Bone White), #1A1A1A (Panel), #E8A44C (Success accent)

### Rhythm Combat Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Rhythm Track Bar | (0, 0) | 256x32 | The beat rail — every fight runs on this |
| Beat Marker | (0, 32) | 24x24 | Approaching beat |
| Hit Window Ring | (24, 32) | 32x32 | Timing window, closes by shape |
| Perfect Hit Burst | (56, 32) | 32x32 | On-beat confirm |
| Miss Marker | (88, 32) | 24x24 | Off-Key trigger |
| Harmony Meter Bar | (112, 32) | 144x32 | Consecutive on-beat actions |
| Crescendo Mode Banner | (0, 64) | 160x32 | Full meter: all attacks critical |
| Tempo Indicator Dial | (160, 64) | 64x64 | Current BPM, boss-controlled in Phase 3 |
| BPM Readout Plate | (0, 96) | 96x24 | Numeric tempo |
| Phase Pip Row | (96, 96) | 64x24 | Boss phase 1/2/3 |

### Statuses & Rewards:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Off-Key Debuff Icon | (0, 128) | 32x32 | Reduced accuracy |
| Dazed Icon | (32, 128) | 32x32 | Soprano Specter's high notes |
| Embarrassed Icon | (64, 128) | 32x32 | Spectral Heckler |
| Exhausted Icon ("Danced to Death") | (96, 128) | 32x32 | Failure state, returns you to the surface |
| Touched By Death Icon | (128, 128) | 32x32 | Couchsurf bonus: +15% rhythm for 3 hours |
| Undead DJ's Blessing Icon | (160, 128) | 32x32 | Permanent +5% on-beat damage |
| Bone Conductor's Gloves | (192, 128) | 32x48 | Boss reward: +10% rhythm timing, +3 Charm |
| Eternal Setlist | (224, 128) | 32x48 | Key item: unlocks Requiem Room VIP |

### Items & Consumables:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cemetery Pass "Composer's Rest" €5 | (0, 176) | 48x32 | Entry item; basically club cover |
| Lost Composition | (48, 176) | 48x64 | Enables the peaceful resolution |
| RIP Your Sobriety | (96, 176) | 32x48 | Powerful but risky drink |
| Skull Glass | (128, 176) | 32x48 | Bar vessel. IKEA |
| Spine Glow-Stick | (160, 176) | 24x48 | Merchandise |
| Rare LP (Vinyl Hunt) | (184, 176) | 40x40 | Hidden in the Requiem Room |
| Tip In Pelvic Bowl Icon | (224, 176) | 32x32 | Tips for the dead |

### Prompts, Bars & Captions:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Knock-Rhythm Prompt Panel | (0, 208) | 96x24 | Three knocks; any rhythm works |
| Boss Health Bar Frame | (96, 208) | 160x24 | Three-phase segmented |
| Selfie Caption "Dance Partners: Deceased" | (0, 232) | 128x24 | Dancefloor spot |
| Selfie Caption "Back from the Dead" | (128, 232) | 128x24 | Grave entrance, 5 AM |
| Selfie Caption "King/Queen of the Dead" | (0, 256) | 128x32 | Bone Throne, VIP |
| Achievement Toast Frame | (128, 256) | 128x32 | "Grave Robber" / "Appeased the Dead" / "Mozart Would Approve" |

### Technical Notes:
- The Hit Window Ring communicates timing by *closing geometry*, not colour shift — it must be readable in monochrome
- Boss Health Bar is segmented at 66% and 33% so phase transitions are legible without reading the pip row
- The Knock-Rhythm Prompt accepts any rhythm; the panel must not imply a "correct" pattern, because getting it wrong is a content branch (sad trombone + comedy dialogue), not a failure

---

## 🎬 Animation Specifications

### The Knock (Grave Entrance):
- **Duration:** 2.0 seconds, single play
- **Frames:** 3 (headstone idle → knocked → open with ladder)
- **Pattern:** Three knocks, then a stone slide; any rhythm succeeds
- **Trigger:** Interacting with the Bassmeister headstone at 11 PM–5 AM with a pass or the secret
- **Purpose:** The satirical puzzle payoff — the entrance is a grave, and the guard is watching, and nothing happens
- **Audio Sync:** Three knock impacts synced to the player's input; stone-grind on the slide. **Wrong rhythm plays a sad trombone before the stone opens anyway**
- **Mobile Optimization:** None needed

### The Descent:
- **Duration:** 4.0 seconds, scripted traversal
- **Frames:** 3 background states (stone upper → transition mid → neon lower) cross-faded
- **Pattern:** Continuous downward scroll with music volume ramping across the three states
- **Trigger:** Entering the grave
- **Purpose:** The bone decorations get progressively more party-themed as you go down
- **Audio Sync:** Club track rises from -30dB to 0dB across the traversal; dripping water fades out at the midpoint
- **Mobile Optimization:** Cross-fade reduced to hard cuts on Low LOD

### Glass Dancefloor Pulse:
- **Duration:** Locked to the current track's beat clock
- **Frames:** 2 (lit panel ↔ dark panel), tile-swapped
- **Pattern:** Panels alternate in a travelling wave from the nearest speaker
- **Trigger:** Constant on the dancefloor
- **Purpose:** The floor is the metronome; players read the beat from the room before the UI
- **Audio Sync:** One swap per beat, locked to the same clock as the Rhythm Track Bar
- **Mobile Optimization:** Wave becomes a whole-floor flash on Medium; static lit floor on Low

### Skeleton Dance Loop:
- **Duration:** 1.0 second cycle at 120 BPM (scales with tempo)
- **Frames:** 2 per skeleton (A ↔ B) plus 2 head-bob frames layered
- **Pattern:** Ambient dancers loop on-beat; enemy skeletons loop on-beat and strike on the downbeat
- **Trigger:** Constant on the dancefloor; combat-gated for enemies
- **Purpose:** Enemy attack timing is telegraphed by the dance itself
- **Audio Sync:** Bone rattle on each loop; xylophone sting on hit
- **Mobile Optimization:** Ambient dancer count 12 → 6 (Medium) → 4 (Low); all share two frames

### Bass Drop:
- **Duration:** 0.8 seconds, single play
- **Frames:** 3 (shockwave ring 1 → 2 → 3) + floor decal + screen shake
- **Pattern:** Ring expands from the active speaker; Bass Pit tiles switch to charged for the duration
- **Trigger:** Track drops; Grave-o's attack; Bassmeister "Bass from the Grave" / "Drop of Death"
- **Purpose:** The location's defining impact — mitigation timing hangs on this
- **Audio Sync:** Sub-bass hit on ring 1; the Bass Drop Cue Glyph appears 0.5s *before* the audio as an advance warning
- **Mobile Optimization:** Two rings on Medium; one ring, no shake, on Low. Screen shake replaced by the Screen Shake Marker whenever shake is disabled

### Strobe:
- **Duration:** Continuous while active
- **Frames:** 2 (flash ↔ off)
- **Pattern:** **Maximum 3Hz.** Never faster, under any tempo
- **Trigger:** Dancefloor and Strobe Zone hazards
- **Purpose:** Timing disruption as an environmental hazard
- **Audio Sync:** None
- **Mobile Optimization:** Automatically replaced by the Non-Flashing Strobe Substitute under Reduced Motion or Photosensitivity settings — not an opt-in

### Fog Roll:
- **Duration:** 3.0 second cycle
- **Frames:** 3 (fog bank A → B → C)
- **Pattern:** Slow horizontal drift, three emitters offset
- **Trigger:** Constant; heavier in Fog Bank hazard volumes
- **Purpose:** Concealment hazard and the venue's entire atmosphere budget
- **Audio Sync:** Fog machine hiss on emitter cycle
- **Mobile Optimization:** Low-density variant on Medium; two static frames cross-faded on Low

### Boss Phase Transition:
- **Duration:** 1.2 seconds, single play
- **Frames:** Idle → transition → new phase idle
- **Pattern:** Tempo audibly resets on the transition frame; health bar segment locks
- **Trigger:** Boss HP crosses 66% and 33%
- **Purpose:** The fight restructures around you twice
- **Audio Sync:** Track breakdown into the new BPM on the transition frame; Bassmeister's phase line begins immediately after
- **Mobile Optimization:** None needed

### "Last Rave" Wind-Up:
- **Duration:** 3.0 seconds, single play, held telegraph
- **Frames:** 1 held wind-up frame with an escalating charge overlay
- **Pattern:** Long, obvious, and exactly long enough to reach the pipe organ
- **Trigger:** Phase 3 desperation attack
- **Purpose:** The counter-play — turn his music against him
- **Audio Sync:** Rising organ drone; the Pipe Organ Blast Glyph appears on the interactable at 0.5s
- **Mobile Optimization:** None needed — this is the mechanic

### The Appeasement:
- **Duration:** 4.0 seconds, single play
- **Frames:** 3 (Lost Composition presented → recognition → appeased idle)
- **Pattern:** No reversal; the boss music decays into unaccompanied strings
- **Trigger:** Present the Lost Composition during Phase 3
- **Purpose:** "You... found it? My symphony? It SURVIVED?"
- **Audio Sync:** EDM layers drop out one at a time across the three frames until only strings remain
- **Mobile Optimization:** None needed

### Skull Disco Ball Rotation:
- **Duration:** 2.0 second cycle
- **Frames:** 2 (A ↔ B) plus a scatter-speck overlay
- **Pattern:** Continuous slow rotation
- **Trigger:** Constant on the dancefloor
- **Purpose:** Texture
- **Audio Sync:** None
- **Mobile Optimization:** Static frame on Low LOD

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bassmeister headstone outline | set at sheet layout | 96x128 | The entrance must be findable at high contrast |
| Bassmeister boss outline | set at sheet layout | 128x192 | Boss silhouette against fog and neon |
| Four DJ outlines | set at sheet layout | 128x192 | One per mini-boss |
| Bone Throne outline | set at sheet layout | 64x96 | Selfie spot marker |
| Helga outline | set at sheet layout | 64x96 | Vendor/couchsurf host |
| Bass Pit hazard outline | set at sheet layout | 64x64 | Hazard visibility in fog |
| Bone Pile hazard outline | set at sheet layout | 48x64 | Hazard visibility in fog |
| Pipe organ interactable outline | set at sheet layout | 192x128 | Phase 3 counter-play target |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Non-flashing strobe substitute | (128, 224) | 128x32 | **Automatic**, not opt-in, under Reduced Motion / Photosensitivity |
| Static fog frame | (0, 224) | 128x32 | No roll |
| Reduced-motion laser static | (256, 224) | 128x32 | Fixed fan position |
| Screen shake marker | (304, 192) | 32x32 | Replaces camera shake entirely |
| Static disco ball frame | set at sheet layout | 64x64 | No rotation |
| Static glass floor (lit) | set at sheet layout | 32x32 | No beat pulse; beat conveyed by the Rhythm Track Bar alone |
| Reduced skeleton dancer set | set at sheet layout | 64x96 | Four static background dancers |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bass drop cue glyph | (176, 192) | 48x32 | Appears 0.5s **before** every bass drop |
| Tempo shift glyph | (224, 192) | 48x32 | Fires on every Phase 2 tempo change |
| On-beat hit ring | (144, 192) | 32x32 | Confirms every successful on-beat action |
| Off-key glyph | (112, 192) | 32x32 | Confirms every missed beat |
| Bone rattle glyph | (48, 192) | 32x32 | Skeleton movement |
| Xylophone sting glyph | (80, 192) | 32x32 | Skeleton hit |
| Ghost mockery glyph | (272, 192) | 32x32 | Spectral Heckler taunt |
| Pipe organ blast glyph | (336, 192) | 48x32 | Phase 3 counter window open |
| Sad trombone glyph | (0, 192) | 48x32 | Wrong-rhythm knock |
| Beat marker (Rhythm Track Bar) | (0, 32) | 24x24 | **Every beat has a visual equivalent — the entire combat system is playable deaf** |

### Colorblind Considerations:
- Hit Window Ring closes by geometry, never by hue shift
- The four elemental weakness markers are shape-coded: spike (high-frequency), wave (bass), clock (tempo-change), broken chord (dissonance)
- Bass Pit charged state raises its edge geometry; Bone Pile collapsed state visibly lowers — hazard states are never colour-only
- Boss health bar is segmented at 66% / 33% with physical notches, plus a phase pip row
- Status icons are shape-first: Off-Key = broken note, Dazed = spiral, Embarrassed = downturned mask, Exhausted = slumped figure, Touched by Death = handprint, Blessing = crowned note
- Touch zones minimum 44px for rhythm inputs, the knock prompt, the organ interactable, and the selfie prompts

---

## 📱 Mobile Optimization

### Texture Compression by Platform:
- **iOS:** ASTC 6x6 for environment and cast; ASTC 4x4 for `mozarts_rave_ui.png` (rhythm timing legibility is non-negotiable) and `bassmeister_boss.png` (the period-costume/headphone collision must survive). PVRTC 4BPP fallback.
- **Android:** ETC2 with alpha across all sheets
- **Fallback:** PNG high quality for `mozarts_rave_effects.png` — fog gradients band badly under aggressive compression, and fog is the venue

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| mozarts_rave_surface | cemetery (surface + descent) | 1024x512 |
| mozarts_rave_interior | crypt tileset, landmarks | 2048x1024 |
| mozarts_rave_characters | Bassmeister, four DJs, cast | 1024x1024 |
| mozarts_rave_fx_ui | effects, UI | 1024x512 |

*(Max atlas size 2048x2048 for mobile GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Three-frame fog on three emitters, laser fans, strobe, UV wash, full glass-floor wave, 12 ambient dancers, bass-reactive particles, spectral wisps, disco ball rotation, three parallax layers |
| Medium | Low-density fog on two emitters, single laser fan, strobe retained at 3Hz, whole-floor flash instead of wave, 6 ambient dancers, halved particles, two parallax layers |
| Low | Two cross-faded static fog frames, no lasers, non-flashing strobe substitute, static lit floor, 4 static dancers, no wisps, static disco ball, no parallax. **Rhythm Track Bar, beat markers, bass drop cue, and all boss telegraphs are retained at every LOD — they are the game** |

### Performance Targets:
- **Target FPS:** 45 (per location profile: "45 FPS target")
- **Max Draw Calls:** 22 per frame (per location profile)
- **Memory Footprint:** 55 MB maximum (per location profile)
- **Particle Limit:** 28 (fog 12, bass-reactive 8, bone dust 4, spectral wisps 4 — boss-phase bursts temporarily suspend ambient wisps and bone dust rather than adding to the count)

### Performance Notes:
- Four sub-areas (Bone Bar, Dancefloor, Requiem Room, Conductor's Crypt) load as separate scene states off one shared interior atlas; the cemetery surface is a separate scene with its own atlas
- The Requiem Room is gated behind first completion and loads on demand
- Ambient skeleton dancers are a `Sprite2D` pool sharing two frames with per-instance phase offsets — never individual `AnimatedSprite2D` nodes
- The boss arena drops all ambient dancers and the disco ball to free draw calls for the three-phase fight
- Audio streaming (not preloaded) for club tracks and the boss theme, per the profile's platform considerations
- Fog is three pre-rendered looping frames, never a simulation

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- `TileMap` for cemetery and crypt floors/walls; `ParallaxBackground` with up to three `ParallaxLayer` nodes (catacomb far, crowd silhouette mid, boss backdrop static)
- `AnimatedSprite2D` for Bassmeister (16 states across three phases + two resolutions), the four elemental DJs, Helga, and the Grave Guide
- `Sprite2D` pool for ambient skeleton dancers (max 12), ghost groupies (max 3), enemy skeletons (max 6)
- `CPUParticles2D` (not GPU) for fog, bone dust, bass-reactive bursts, spectral wisps
- `CanvasLayer` for the Rhythm Track Bar, Harmony Meter, boss health bar, and phase pips
- **Central beat clock** (`AudioStreamPlayer` playback position → `beat_signal`) drives: glass floor tile swaps, skeleton dance loops, enemy strike windows, the Rhythm Track Bar, bass-reactive particles, and the disco ball. Nothing in this location animates on an independent timer during combat
- Discovery puzzle state machine: `rumor_heard → cemetery_entered → wrong_grave_examined → correct_grave_found → knocked → descended`. The wrong-grave branch is content, not a failure
- Boss state machine: `intro → phase_1 → phase_2 → phase_3 → (defeat | appeased)`. Appeasement requires `lost_composition` in inventory and is only presentable during `phase_3`
- Rhythm difficulty is per-zone: Bone Bar (slow tempo, forgiving), Dancefloor (medium), Requiem Room (variable), Conductor's Crypt (boss-controlled, adaptive)
- Couchsurf flow (Helga): three drinks purchased + tip given + no "are the undead real" dialogue selected → Requiem Room rest → full HP/SP, "Touched by Death" +15% rhythm for 3 hours, permanent 10% Bone Bar discount

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Headstone knock frames | Knock impacts, player-driven | Per input |
| Wrong-rhythm knock | Sad trombone | Before the stone opens anyway |
| Descent traversal | Club track ramp -30dB → 0dB | Across 4.0s |
| Glass floor tile swap | Beat | One swap per beat, shared clock |
| Skeleton dance loop | Bone rattle | Per loop |
| Skeleton hit | Xylophone sting | On contact frame |
| Bass drop cue glyph | *(silent)* | 0.5s **before** the sub-bass hit |
| Bass shockwave ring 1 | Sub-bass hit | On ring spawn |
| Strobe flash | *(silent)* | Max 3Hz |
| Boss phase transition frame | Track breakdown into new BPM | On transition frame |
| "Last Rave" wind-up | Rising organ drone | Across 3.0s; organ glyph at 0.5s |
| Appeasement frames 1–3 | EDM layers dropping out to strings | One layer per frame |
| Spectral Heckler appearance | Ghostly jeer | On spawn |
| 5 AM exit | Dawn ambience, distant church bells | On surface transition |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| "Finding Bassmeister's Grave" | Wrong grave (tourist-crowded), Bassmeister headstone, speaker icon carving, knocked/open states, knock-rhythm prompt, sad trombone glyph, security guard post | Discovery quest from Moderato Pub / Café Existenz rumors |
| "The Lost Composition" | Lost Composition item, Appeasement frames, Appeased Idle vendor stance | Hidden in the crypt; enables peaceful boss resolution |
| "Dance Until You Drop" | Dawn backdrop, dawn light shaft, grave-entrance selfie, Exhausted icon | Survive the full night to 5 AM |
| "Vinyl Hunt" | Rare LP sprite, Requiem Room interior | One of Sinfonia's rare LPs hidden in the Requiem Room |
| Boss rewards (either victory) | Bone Conductor's Gloves, Eternal Setlist, RIP Your Sobriety, Undead DJ's Blessing icon | Granted on defeat or appeasement |
| Couchsurf — Helga | Helga couchsurf-offer frame, Requiem coffin-cushion seating, Touched By Death icon, Appeased spectral breakfast frame | Three drinks + tip + don't ask if the undead are real |
| Selfie Spot 1 — The Bone Throne | Bone Throne occupied, crown of skulls prop, caption "King/Queen of the Dead" | VIP area; special variant with Bassmeister's ghost on the appeased route |
| Selfie Spot 2 — The Dancefloor | Skeleton dancers, fog, laser fans, caption "Dance Partners: Deceased" | Special variant during a bass drop (screen shake) |
| Selfie Spot 3 — The Grave Entrance | Bassmeister grave open, dawn backdrop, dawn light shaft, caption "Back from the Dead" | Requires completing the full night to 5 AM |
| Achievements | Achievement toast frame, Crescendo Mode banner, appeased/defeat frames | "Grave Robber," "Dance with Death," "Appeased the Dead," "Slayed the Dead," "Bone Throne Royalty," "Back from the Dead," "Living Legend," "Mozart Would Approve" |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Moderato Pub | Rumors heard here lead to discovery; shared rumor-flag UI | None (quest flag) |
| Café Existenz | Intellectual NPCs debate whether the club "exists" | None (dialogue flag) |
| The Bassline Opera House | Thematic inversion — high vs. underground music culture; rhythm-combat timing systems shared | Shared Rhythm Track Bar and Harmony Meter assets |
| Komponistenfriedhof Cemetery | Surface location; daytime tourist state uses the same cemetery sheet with the night overlays disabled | Day/night state swap on the same scene |
| The Composer's Cart | "Lost Manuscript" stock connects to Bassmeister lore; Tempo Guide and Conductor's Notes buff this location's rhythm combat | None (item carry-over) |
| Grounds For Concern | Speed buff aids rhythm timing; caffeine tremor narrows the hit window | None (status carry-over) |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A catacomb that has been rented out — original masonry, plastic bones, gaffer tape, and a health inspection certificate"
- **Color Mood:** Crypt gray and neon purple over death black, with bone white as the only light that reaches the floor; dawn amber exactly once, at 5 AM
- **Lighting:** UV underlighting from the glass floor upward, neon strips at wall height, fog-diffused lasers, a strobe capped at 3Hz, and one skull disco ball scattering everything
- **Texture:** Damp masonry, plastic bone with visible mold seams, scuffed glass panels, velvet drapes in the VIP, and cable snake taped across the floor

### Environmental Storytelling:
- The bones are plastic and the club is not hiding it — mold seams are visible on the chandelier at 1x zoom
- A framed health inspection certificate and fifteen years of tax notices hang by the kiosk, unread by anyone who calls this place secret
- A weathered 4.2-star plaque is mounted at the cemetery gate
- The wrong grave is permanently crowded with photographing tourists; the right grave has a 32x32 speaker icon
- A security guard post overlooks the entrance and the guard patrols past people climbing into it
- The pipe organ is original pipework with faders bolted on and a label-maker strip across the stops
- Gaffer-taped cable runs cross the dancefloor — the supernatural venue has an electrician
- The Requiem Room's coffin-cushion seating is genuinely comfortable, which nobody expected

### Character Integration Notes:
- **The ambiguity must survive the art.** No frame of any undead performer may resolve whether they are ghosts, hallucinations, or theatre students — except the two off-shift theatre-student sprites, which only appear away from the floor
- Bassmeister's 18th-century formal wear must be period-credible enough that the modern headphones read as collision, not costume
- The four elemental DJs are a family: same construction, four silhouettes, one lore
- Helga is the only fully saturated, fully opaque figure in the club — the human anchor in a room of rim-lit bone
- Ghost Groupies are 60% alpha with bone-white rim lighting and period-mismatched clothing
- The Grave Guide's skeleton costume fits badly in the same specific way in both frames — shoulder seam and ankle gap

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Bone Throne** — crown of skulls, "King/Queen of the Dead," with Bassmeister's ghost standing beside you on the appeased route
2. **The bass drop on the dancefloor** — glass floor lit from below, fog, laser fans, and a skeleton mid-dance beside the player
3. **Climbing into the grave** — a player in club clothes descending into a headstone, with a security guard visible in frame doing nothing
4. **The wrong grave** — a tourist crowd photographing the decoy while the real entrance sits two plots away with a tiny speaker carved into it
5. **The appeasement** — an 18th-century skeleton in DJ headphones holding his own lost symphony
6. **5 AM at the grave entrance** — dawn light, club clothes, "Back from the Dead"
7. **The framed health inspection certificate** in the same crop as a "SECRET UNDERGROUND VENUE" sign

### Quote Potential:
- "Feel the BASS... feel it in your BONES... because I don't have any FLESH." - DJ Grave-o
- "My voice could shatter GLASS. Your skull is... slightly thicker." - DJ Soprano Specter
- "Time is RELATIVE. Death is ABSOLUTE. And my beats are ETERNAL." - DJ Tempo Mortis
- "Mozart got the FAME. I got the BASS." - Johann Bassmeister
- "Mozart WISHED he could drop bass like THIS! History ROBBED me!" - Johann Bassmeister
- "If I can't be REMEMBERED... I'll make sure you NEVER FORGET!" - Johann Bassmeister
- "You... found it? My symphony? It SURVIVED? ...Perhaps death has been too loud." - Johann Bassmeister, appeased
- "The skeletons? Lovely coworkers. Never call in sick. Never eat the garnishes. Never ask for raises because, you know, they're dead." - Helga
- "It's from IKEA." - Helga, on the skull glass
- "I'm TECHNICALLY alive, but I feel the music in my BONES! ...Get it? Because— okay, the rhythm tutorial is this way." - The Grave Guide
- "Your 'sneakers' are FASCINATING! In my day, we danced in COFFINS! ...Wait, that's not right." - Ghost Groupie
- "There is a 0% probability of actual reanimation. I am... 12% uncertain." - Bradley

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | mozarts_rave_cemetery.png | 1024x384 |
| 2 | mozarts_rave_tileset.png | 1024x512 |
| 3 | mozarts_rave_landmarks.png | 512x384 |
| 4 | bassmeister_boss.png | 512x768 |
| 5 | mozarts_rave_djs.png | 512x256 |
| 6 | mozarts_rave_cast.png | 512x384 |
| 7 | mozarts_rave_effects.png | 512x256 |
| 8 | mozarts_rave_ui.png | 256x288 |

**Total Estimated Memory:** ~8 MB (2,039,808 px uncompressed RGBA); ~2.2 MB after ETC2/ASTC compression — comfortably inside the 55 MB profile budget

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `mozarts_rave_cemetery.png` (1024x384)
- [ ] `mozarts_rave_tileset.png` (1024x512)
- [ ] `mozarts_rave_landmarks.png` (512x384)
- [ ] `bassmeister_boss.png` (512x768)
- [ ] `mozarts_rave_djs.png` (512x256)
- [ ] `mozarts_rave_cast.png` (512x384)
- [ ] `mozarts_rave_effects.png` (512x256)
- [ ] `mozarts_rave_ui.png` (256x288)

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
- **Documentation:** Animation timing reference sheet (all timings expressed in seconds AND beats at 120 BPM) + parallax layer guide (three layers) + boss phase-transition flow diagram + **photosensitivity compliance note (strobe ≤ 3Hz, automatic substitution asset)**

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (including the two derived accents, flagged in the palette table)
- [ ] **The wrong grave is as impressive as the right grave** — the only distinguishing mark is the 32x32 speaker carving
- [ ] Bassmeister's three headstone states share identical base geometry
- [ ] Every bone in the location reads as plastic on close inspection; the chandelier has visible mold seams
- [ ] Bassmeister's 18th-century formal wear is period-credible against the modern headphones
- [ ] **No frame resolves the ghost/hallucination/performer ambiguity** except the two off-shift theatre-student sprites
- [ ] The four elemental DJs have four distinct silhouettes at 128x192 but share one construction language
- [ ] Helga is the only fully opaque, fully saturated figure in the club
- [ ] The Grave Guide's costume fits badly in the same specific way in both frames
- [ ] The pipe organ reads as converted, not built (original pipework + bolted faders + label-maker strip)
- [ ] The gaffer-taped cable snake is present and unglamorous
- [ ] **Strobe assets ship at a maximum 3Hz flash rate with an automatic non-flashing substitute**
- [ ] Hazard states (Bass Pit charged, Bone Pile collapsed) differ by geometry, not colour
- [ ] Accessibility visual alternatives included for all audio cues — every beat has a visual equivalent
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (classical commercialization, death tourism, "secret" venue with 847 reviews) is clear throughout
- [ ] The health inspection certificate, tax notices, and 4.2-star plaque are legible in surface crops
- [ ] The security guard is visible in the same frame as people climbing into a grave
- [ ] Hidden areas (Requiem Room, Lost Composition) have discoverable visual cues
- [ ] Mobile performance optimized (CPU particles only, 22-draw-call ceiling, four atlas binds, audio streamed, fog pre-rendered)
- [ ] Touch zone sizing considered (44px minimum for rhythm inputs, knock prompt, organ interactable, selfie prompts)
- [ ] Colorblind-friendly alternatives available where color codes meaning
- [ ] Social media viral potential maximized in composition choices

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia and Komponistenfriedhof only; Bassmeister and all tomb occupants are fictional composers — no real composer grave is depicted or mocked |
| Cultural Specificity | ✅ | Sinfonia's composer-grave tourism, classical-legacy merchandising, and the city's performance culture inverted into an underground venue |
| Satirical Targets Appropriate | ✅ | Death tourism, themed-nightclub absurdity, and bros convinced they found something secret; the venue's staff are working people (Helga, the Grave Guide, €15/hour theatre students) treated with affection |
| Seedy Underbelly Present | ✅ | Profile's explicit section: a €5 "cemetery pass" that is club cover, "tips for the dead" going to the owners, and a fifteen-year-old tourist attraction sold as an underground secret |
| Gameplay Value Established | ✅ | Full rhythm-combat system, four elemental mini-bosses, three-phase boss with dual resolution, four standard enemy types, four environmental hazards, discovery puzzle, couchsurf host, three selfie spots, eight achievements |
| Technical Feasibility | ✅ | Eight sheets, four atlases, three LOD tiers, on-demand VIP loading, central beat clock, pre-rendered fog, streamed audio |
| Mobile Performance Budget | ✅ | 45 FPS / 22 draw calls / 55 MB taken verbatim from the profile's stated budget. Flagged: 45 FPS is below the 60 FPS engine default — confirm deliberate low-end target for a rhythm-critical location, since frame pacing affects timing windows |
| Accessibility Features | ✅ | Every beat has a visual equivalent; bass drops telegraph 0.5s early; strobe capped at 3Hz with **automatic** non-flashing substitution; shape-coded hazards, weaknesses, and statuses; screen-shake replacement glyph |
| No Crypto Elements | ✅ | None present, and the profile explicitly confirms "No crypto elements (Death/music satire only)" |
| Social Media Integration | ✅ | Three documented selfie spots with variants and unlock conditions, seven screenshot moments, twelve quotable lines |

**Mozart's Last Rave: a fifteen-year-old tourist attraction with a health inspection certificate, four dead DJs, and one skeleton who has been waiting two hundred and thirty years for somebody to say his name — where every fight is fought on the beat and the only way to win properly is to tell him his symphony survived.**
