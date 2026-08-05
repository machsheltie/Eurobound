# Threads & Treads - Complete PNG Asset Requirements

## 📋 Overview
Threads & Treads is the 24-hour equipment emporium where people buy a new identity at 2 AM: leather as armor, combat boots as commitment, a chain wallet as both pickpocket defense and a statement. This document specifies every PNG for Zdeněk's dark chrome shop — the jacket gauntlet, the flatteringly lit mirror wall, the secret soft section — plus the full equipment catalog that feeds the Cool Factor economy. Zdeněk has dressed 10,000 transformations; these sprites dress the 10,001st.

**Location ID:** `debaucheryville_shop_threads_treads_01`
**Theme:** Retail-assisted identity performance — "Leather, Chains, and the Illusion of Danger."
**Zone:** Absinthe Arcade, Neon Entertainment Quarter
**Hours:** 24 hours (coolness never sleeps; 2 AM - 5 AM brings the honest clientele and a 10% transformation discount)
**Primary Function:** Primary equipment vendor for Debaucheryville — Defense gear, Cool Factor stat economy, Mirror Assessment system, 2 AM transformation mechanics, Bravado interactions

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Leather Black | #1A1A1A | Walls, jackets, facade |
| Chrome Silver | #C0C0C0 | Fixtures, signage lettering, studs |
| Dark Red | #8B0000 | Background accents, fitting room curtain |
| Industrial Gray | #4A4A4A | Floor, racks, shadow midtones |
| Mirror Warm | #E8C87A | Flattering mirror lighting (because commerce) |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/threads_and_treads/
├── environment/
│   ├── threads_exterior.png
│   ├── threads_interior.png
│   └── mirror_transformation.png
├── objects/
│   └── threads_equipment.png
├── npcs/
│   ├── threads_staff.png
│   └── threads_customers.png
├── effects/
│   └── threads_effects.png
└── ui/
    └── threads_ui.png
```

---

## 🏪 Sprite Sheet 1: Exterior
**File:** `threads_exterior.png`
**Dimensions:** 512x384 pixels

### Storefront Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Facade Full | (0, 0) | 320x320 | Narrow storefront, black walls, chrome accents, aggressive aesthetic |
| Window Mannequin Display | (320, 0) | 128x256 | Full leather regalia, combat boots, chains |
| Chrome Main Sign | (448, 0) | 128x48 | "THREADS & TREADS" in chrome lettering |
| Hours Sign | (448, 48) | 64x32 | "24/7 — Because Reinvention Doesn't Sleep" |
| Window Category Strip | (448, 80) | 64x32 | "LEATHER • CHAINS • BOOTS • ATTITUDE" |
| Honest Addition Sign | (448, 112) | 64x32 | "Looking Dangerous Sold Separately (It's Inside You)" |
| Door With Bell | (448, 144) | 64x128 | Heavy door, entry bell above |
| Neon Edge Trim | (448, 272) | 64x32 | Subtle red edge lighting |
| 2 AM Window Glow Overlay | (320, 256) | 128x64 | Late-hours warm interior light spill |
| Street Strip | (0, 320) | 512x64 | Between-clubs-and-hostels sidewalk context |

### Technical Notes:
- Shop never closes: no shuttered state exists, only day facade vs. the 2 AM glow overlay
- Honest Addition Sign is examine-zoomable — the parenthetical is the punchline
- Bell sprite tilts 15° via tween on entry; no extra frames needed

---

## 🧥 Sprite Sheet 2: The Transformation Station
**File:** `threads_interior.png`
**Dimensions:** 1024x512 pixels

### Interior Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Interior Base | (0, 0) | 512x384 | Dark wood, chrome fixtures, industrial spot lighting |
| Leather Jacket Wall | (512, 0) | 384x256 | Jackets lining the wall — the "protagonist" section |
| Boot Display | (896, 0) | 128x256 | "Your feet are your foundation" tiered rack |
| Accessories Rack | (512, 256) | 256x128 | Chains, studs, cuffs, chokers — identity by the piece |
| Soft Section | (768, 256) | 256x128 | Band tees and comfortable alternatives, discreetly placed |
| Patch Display Board | (896, 256) | 128x128 | Band patches pinned in rows — declare your allegiances |

### Fixtures & Zones:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mirror Wall | (0, 384) | 256x128 | Full-length mirrors, strategic flattering light |
| Fitting Room | (256, 384) | 192x128 | Dark red curtain, private transformation chamber |
| Mannequin Trio | (448, 384) | 192x128 | Three full-outfit examples, aspirational |
| Entry Gauntlet | (640, 384) | 192x128 | Jacket corridor — immediate impact on entry |
| Checkout Counter | (832, 384) | 128x128 | Zdeněk's register, no-refunds sign spot |
| Rock Poster Wall | (960, 384) | 64x128 | Faded gig posters, '98 onward |

### Technical Notes:
- Interior lighting shifts warmer and dimmer between 2 AM - 5 AM (CanvasModulate lerp, no extra sprites)
- Mirror Wall pairs with Sheet 6 overlays for the assessment moment
- Leather Jacket Wall is the entry framing shot — composition must hit the moment the door opens

---

## 🛠️ Sprite Sheet 3: Equipment Catalog
**File:** `threads_equipment.png`
**Dimensions:** 256x256 pixels

### Leather & Jackets:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Faux Leather Jacket | (0, 0) | 48x48 | 40 Sovs budget transformation |
| Genuine Leather Jacket | (48, 0) | 48x48 | 120 Sovs — the real deal |
| Studded Leather Jacket | (96, 0) | 48x48 | 150 Sovs maximum statement |
| Vintage Biker Jacket | (144, 0) | 48x48 | Has history (or looks like it) |
| Soft Leather Jacket | (192, 0) | 48x48 | Best of both worlds — the soft section's crown |

### Vests, Tees & Jeans:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Denim Vest (Patchless) | (0, 48) | 48x48 | Canvas for your identity |
| Band T-Shirt (Classic) | (48, 48) | 48x48 | Conversation starter |
| Band T-Shirt (Obscure) | (96, 48) | 48x48 | Test who's real — gatekeepers exist |
| Comfortable Black Jeans | (144, 48) | 48x48 | Looking cool without suffering |
| Band Patch Set | (192, 48) | 64x32 | Allegiance collection, 5 Sovs-15 each |

### Footwear:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Combat Boots (Standard) | (0, 96) | 32x32 | Practical and aggressive |
| Combat Boots (Steel-Toe) | (32, 96) | 32x32 | For serious situations |
| Platform Boots | (64, 96) | 32x32 | Presence amplifier |
| Vintage Army Boots | (96, 96) | 32x32 | Someone else's story |
| Creepers | (128, 96) | 32x32 | Subculture signifier |
| Chain Wallet | (160, 96) | 32x24 | Practical AND aesthetic |
| Studded Belt (Worn) | (192, 96) | 48x16 | Holds up pants, holds up in fights |
| Studded Belt (Coiled) | (192, 112) | 48x16 | Shelf display state |

### Accessories:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fingerless Gloves | (0, 128) | 32x24 | For things that require grip |
| Spiked Bracelet | (32, 128) | 32x24 | Handshake deterrent |
| Leather Cuff | (64, 128) | 24x24 | Subtle statement |
| Choker | (96, 128) | 32x16 | Neck declaration |
| Bandana | (128, 128) | 32x24 | Multiple functions |
| Aviator Sunglasses | (160, 128) | 32x24 | Classic for a reason |
| Patch Singles Strip | (192, 128) | 64x16 | Individual patches for the vest slots |

### Retail Props:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shopping Bag | (0, 160) | 32x32 | Black bag, chrome logo |
| Empty Hanger | (32, 160) | 16x32 | Rack dressing |
| Jacket On Hanger | (48, 160) | 48x64 | Wall display unit |
| Boxed Boots | (96, 160) | 48x32 | Stacked stock |
| Price Tag | (144, 160) | 32x16 | Standard chrome-edge tag |
| 2 AM Discount Tag | (144, 176) | 32x16 | Transformation-hours 10% marker |
| Full Outfit Bundle Icon | (176, 160) | 48x48 | Three-piece commitment purchase |

---

## 🧔 Sprite Sheet 4: Zdeněk & Eva
**File:** `threads_staff.png`
**Dimensions:** 512x256 pixels

### Zdeněk "Z" Holub:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Zdeněk Idle | (0, 0) | 64x96 | Leather vest, grey hair pulled back, visible tattoos, calm presence |
| Zdeněk Assessing F1 | (64, 0) | 64x96 | Honest evaluation, arms crossed |
| Zdeněk Assessing F2 | (128, 0) | 64x96 | Slow nod — "The leather? It fits you. Do you fit IT?" |
| Zdeněk Philosophical | (192, 0) | 64x96 | Deep thought mode, hand on chin |
| Zdeněk Practical Point | (256, 0) | 64x96 | "Genuine leather here, faux there." |
| Zdeněk Calm Lean | (320, 0) | 64x96 | Counter lean, seen everything |
| Portrait: Zdeněk | (384, 0) | 64x96 | Dialogue box default |
| Portrait: Philosophical | (448, 0) | 64x96 | For the 2 AM wisdom lines |

### Night Shift Eva:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Eva Idle | (0, 96) | 64x96 | Fully committed to the aesthetic, former scene kid |
| Eva Encouraging | (64, 96) | 64x96 | "I've been where you are. The jacket helps." |
| Eva Restocking | (128, 96) | 64x96 | Rack work between customers |
| Portrait: Eva | (192, 96) | 64x96 | Dialogue box |
| Zdeněk Jacket Handoff | (256, 96) | 64x96 | Presenting the chosen piece with ceremony |
| Zdeněk No-Judgment Shrug | (320, 96) | 64x96 | "No refunds after wearing. But no judgment either." |
| Eva Discount Gesture | (384, 96) | 64x96 | "Three pieces, 10% off." |
| Zdeněk Walk | (448, 96) | 64x96 | Floor movement frame |

### Expressions & Details:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Zdeněk Knowing | (0, 192) | 48x48 | The look that says he's seen 10,000 of you |
| Zdeněk Approving | (48, 192) | 48x48 | "You're committing. I respect commitment." |
| Eva Grin | (96, 192) | 48x48 | Scene enabler energy |
| Eva Gatekeeper Warning | (144, 192) | 48x48 | Deadpan — "Be ready to discuss them." |
| Zdeněk Remembering '98 | (192, 192) | 48x48 | "The country is finding itself." |
| Tattoo Detail | (240, 192) | 48x48 | Forearm close-up, roadie history in ink |
| Jacket Handoff Hands | (288, 192) | 64x48 | Counter close-up insert |

---

## 🧑‍🤝‍🧑 Sprite Sheet 5: Customers & Bros
**File:** `threads_customers.png`
**Dimensions:** 512x192 pixels

### Atmospheric Customers:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Post-Breakup Purchaser | (0, 0) | 64x96 | Intense focus, significant cart, no eye contact |
| Scene Regular | (64, 0) | 64x96 | "Z, you get those patches in? The Bathory ones?" |
| Curious Tourist | (128, 0) | 64x96 | Touching leather tentatively, imagining |
| Group Purchase Squad | (192, 0) | 192x96 | "We ALL get the jackets. This is SQUAD." |
| Morning-After Return | (384, 0) | 64x96 | Sheepish, sober, reconsidering (after 9 AM only) |
| Generic Browser | (448, 0) | 64x96 | Ambient rack shuffler |

### The Bros:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Lord Pilsner (Jacket Moment) | (0, 96) | 64x96 | "I look like someone who DOES things." |
| Chadwick (Camera Check) | (64, 96) | 64x96 | "Does this translate?" — phone raised at mirror |
| Bradley (Pleather) | (128, 96) | 64x96 | "The statement is what matters, not the cow." |
| Bros Transformed Trio | (192, 96) | 192x96 | Full new looks, walking out together |
| Morning-After (9 AM Light) | (384, 96) | 64x96 | Same NPC, unkind daylight variant |
| Fitting Room Feet Gag | (448, 96) | 64x32 | Boots visible under the curtain, mid-struggle |
| Try-On Silhouette | (448, 128) | 64x64 | Curtain shadow shape for fitting animation |

---

## 🪞 Sprite Sheet 6: The Mirror Wall
**File:** `mirror_transformation.png`
**Dimensions:** 256x256 pixels

### Mirror Assembly:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mirror Frame (Full-Length) | (0, 0) | 96x224 | Chrome-edged, floor to eye-line |
| Flattering Light Overlay | (96, 0) | 96x224 | Warm rim glow — the lighting is kind, the mirror doesn't lie |
| Before Silhouette | (192, 0) | 64x96 | Pre-transformation player shape, slouched |
| After Silhouette | (192, 96) | 64x96 | Post-transformation shape — standing differently |
| Transformation Flash F1 | (192, 192) | 64x32 | White sweep across the glass |
| Transformation Flash F2 | (192, 224) | 64x32 | Sweep exit |
| "Who Do You Want To Be Tonight?" Decal | (0, 224) | 96x32 | Etched above the mirror |
| Mirror Glare Sweep | (96, 224) | 96x32 | Idle glass highlight strip |

### Technical Notes:
- Before/After silhouettes are compositing masks — actual player sprite renders into them via viewport
- The "standing differently" pose difference IS Katarina-grade satire done in posture: shoulders back, chin up, nothing else changes
- Flash frames play only on outfit-complete moments, not every try-on

---

## ✨ Sprite Sheet 7: Effects
**File:** `threads_effects.png`
**Dimensions:** 128x128 pixels

### Atmosphere:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Dust Motes In Beam | (0, 0) | 32x64 | Industrial spotlight column |
| Leather Sheen Sweep | (32, 0) | 64x32 | Traveling highlight on the jacket wall |
| Chain Glint F1 | (96, 0) | 16x16 | Accessory sparkle |
| Chain Glint F2 | (112, 0) | 16x16 | Glint fade |
| Zip Motion Lines | (96, 16) | 32x32 | Jacket zip-up flourish |

### Interaction Feedback:
| Effect | Position | Size | Description |
|--------|----------|------|-------------|
| Boot Stomp Impact | (32, 32) | 32x32 | Try-on floor thud ring |
| Bell Chime Ring | (64, 32) | 32x32 | Entry bell visual ping |
| Spotlight Cone | (0, 64) | 64x64 | Mirror-moment dramatic light |
| Transformation Aura | (64, 64) | 64x64 | Brief confidence glow on outfit completion |

---

## 🎮 Sprite Sheet 8: UI Elements
**File:** `threads_ui.png`
**Dimensions:** 256x256 pixels

### Shop Interface:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Equipment Browser Frame | (0, 0) | 160x96 | Chrome-on-black section navigation |
| Cool Factor Meter | (160, 0) | 96x32 | Style stat display |
| Cool Threshold Pips | (160, 32) | 96x32 | 0-10 / 11-25 / 26-50 / 51+ scene-status markers |
| Stat Comparison Panel | (160, 64) | 96x96 | Before/after equipment stats |

### Mirror & Transformation:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mirror Assessment Frame | (0, 96) | 128x128 | Full character view UI with stat readout |
| 2 AM Discount Banner | (160, 160) | 96x48 | "Transformation hours — 3+ pieces, 10% off" |
| Edgelord Discount Badge | (160, 208) | 48x48 | "Regular" status after 3 purchases |

### Prompts & Feedback:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| "Who Do You Want To Be?" Prompt | (0, 224) | 128x32 | Three-option choice bar (tougher / fit in / just change) |
| No Refunds Sign | (128, 224) | 64x32 | "No refunds after wearing. No judgment either." |
| Bravado Up | (192, 224) | 32x32 | Full-commitment feedback |
| Bravado Down | (224, 224) | 32x32 | "Does this look stupid?" feedback |

---

## 🎬 Animation Specifications

### Entry Bell & Assessment:
- **Duration:** 3 seconds
- **Frames:** Bell tilt tween + Bell Chime Ring (0.5s) → Zdeněk Idle → Assessing F1 (1.5s) → back to Idle (1s)
- **Pattern:** One-shot per entry
- **Trigger:** Player crosses the door
- **Purpose:** Zdeněk clocks you the moment you enter — the shop knows why you're here before you do
- **Audio Sync:** Bell chime at 0.0s over the rock music bed
- **Performance Optimization:** None needed

### Jacket Try-On:
- **Duration:** 3.5 seconds
- **Frames:** Try-On Silhouette behind curtain (1.5s) → curtain open → player in jacket + Zip Motion Lines (1s) → Boot Stomp Impact if boots equipped (0.5s) → hold (0.5s)
- **Pattern:** One-shot per try-on
- **Trigger:** Player equips an item from the browser
- **Purpose:** The transformation fantasy, embodied — each layer lands with physical feedback
- **Audio Sync:** Curtain slide, jacket zip on the motion lines, boot thud on the impact ring
- **Performance Optimization:** Silhouette phase skipped on Low LOD (instant swap)

### The Mirror Moment:
- **Duration:** 4 seconds
- **Frames:** Spotlight Cone fade-in (1s) → Before Silhouette cross-fades to After (1.5s) → Transformation Flash F1-F2 (0.5s) → Assessment UI slides in (1s)
- **Pattern:** One-shot when approaching the mirror with 3+ new pieces
- **Trigger:** Player at Mirror Wall with a qualifying outfit
- **Purpose:** The before/after IS the product — "standing differently" rendered literally
- **Audio Sync:** Satirical transformation sting (per profile) peaking on the flash
- **Performance Optimization:** Cross-fade shortens to 0.75s; flash retained (it is the payoff)

### Leather Sheen Sweep:
- **Duration:** 8 seconds loop
- **Frames:** 1 sprite tweened across the jacket wall
- **Pattern:** Slow left-to-right travel, pause, repeat
- **Trigger:** Constant ambient
- **Purpose:** The wall of jackets breathes; the merchandise looks alive and expensive
- **Audio Sync:** None
- **Performance Optimization:** Off on Low LOD

### 2 AM Lighting Shift:
- **Duration:** 60 seconds transition at 02:00, state holds until 05:00
- **Frames:** CanvasModulate lerp toward warmer/dimmer + 2 AM Window Glow Overlay on exterior
- **Pattern:** Nightly one-shot in, one-shot out
- **Trigger:** In-game clock
- **Purpose:** "2 AM purchases are the most honest" — the room gets intimate when the honest crowd arrives
- **Audio Sync:** Music bed swaps to quieter classic rock; volume -4dB
- **Performance Optimization:** Stepped shift (3 keyframes) instead of continuous lerp

### Dust In The Beam:
- **Duration:** 5 seconds loop
- **Frames:** Dust Note column drift, randomized offsets
- **Pattern:** Constant in spotlight zones
- **Trigger:** Constant ambient
- **Purpose:** Moody industrial texture — the shop's stillness against the Arcade's chaos
- **Audio Sync:** None
- **Performance Optimization:** Static decal on Low

### Morning-After Return (Event):
- **Duration:** 6 seconds scene beat
- **Frames:** Morning-After NPC enters in 9 AM light variant → No-Judgment Shrug from Zdeněk → NPC exits
- **Pattern:** Rare event, after 9 AM only
- **Trigger:** Random morning event roll when player present
- **Purpose:** The consequences NPC — "it made sense at 2 AM" walking past the player as a warning
- **Audio Sync:** Quiet comedic sting on the shrug
- **Performance Optimization:** Event disabled on Low LOD

---

## ♿ Accessibility Sprite Requirements
**File:** `threads_accessibility.png` (supplemental sheet — delivered alongside the 8 base files, not counted in their total)
**Dimensions:** 256x256 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Zdeněk Interactive Outline | (0, 0) | 64x96 | White-on-dark hotspot — critical in a deliberately dark shop |
| Eva Interactive Outline | (64, 0) | 64x96 | Matching night-shift hotspot |
| Browser Frame, Bold | (128, 0) | 96x64 | High-contrast navigation border |
| Honest Sign, Large-Print | (128, 64) | 128x48 | "Looking Dangerous Sold Separately (It's Inside You)" readable without zoom |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Mirror Flash, Removed | (0, 96) | 64x32 | Cross-fade-only transformation (flash frames skipped) |
| Sheen Sweep, Off | (64, 96) | 64x32 | Static highlight decal on the jacket wall |
| Dust, Static | (128, 112) | 32x32 | Fixed Note decal |
| Lighting Shift, Stepped | (160, 112) | 64x32 | Three discrete 2 AM lighting states instead of a continuous lerp |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Bell Chime Icon | (0, 160) | 32x32 | Ring glyph on entry |
| Zip Icon | (32, 160) | 32x32 | Zipper-line glyph on jacket equip |
| Boot Thud Icon | (64, 160) | 32x32 | Impact glyph on boot equip |
| Transformation Sting Icon | (96, 160) | 48x32 | Rising-notes glyph on the mirror moment |
| Music Shift Icon | (144, 160) | 32x32 | Note-dimming glyph at the 2 AM audio swap |
| Chain Rattle Icon | (176, 160) | 32x32 | Link glyph on accessory equip |

### Colorblind Considerations:
- Cool Factor thresholds are pip-count coded (1-4 pips), never color-gradient alone
- Genuine vs. faux leather distinguished by tag text and price, exactly as Zdeněk intends — no color-reliant material coding
- Defense vs. Cool Factor stat deltas use distinct glyphs (shield vs. star) in the comparison panel
- Staff hotspots, browser rows, and the mirror trigger zone all exceed the 44px minimum touch target

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) — threads_equipment.png kept uncompressed (dark-on-dark icons need edge fidelity)
- **Fallback:** PNG high quality for threads_ui.png and signage text

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| threads_environment | exterior, interior, mirror | 2048x1024 |
| threads_characters | staff, customers | 1024x512 |
| threads_items_ui | equipment, effects, ui, accessibility | 512x512 |

*(Max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Sheen sweep, dust columns, full try-on sequence, morning-after event, 4 customer NPCs |
| Medium | Static sheen, 1 dust column, shortened try-on, 3 customers |
| Low | Static lighting per profile, static mannequins, instant equip swaps, 2 customers, no morning event |

### Performance Targets:
- **Target FPS:** 60 (per location profile performance budget)
- **Max Draw Calls:** 14 per frame
- **Memory Footprint:** 34 MB maximum
- **Particle Limit:** 12 (dust + glints combined)

### Performance Notes:
- Simplified lighting and static mannequins per profile platform considerations
- Mirror viewport renders only while the player stands in the mirror zone
- Equipment browser batched from one sheet — single draw call
- 2 AM state is a modulate value, not an asset swap

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- Interior scene with CanvasModulate day/2 AM states driven by the in-game clock; exterior glow overlay toggles in sync
- Equipment system: catalog resource maps sprite regions → Defense / Cool Factor / special effects; equipping writes to shared `player_equipment` consumed city-wide
- Cool Factor thresholds (0-10 / 11-25 / 26-50 / 51+) evaluated per NPC context — club contexts weight it fully, daytime contexts at half
- Mirror Assessment: SubViewport composite of the player sprite into the mirror frame; Before/After masks from Sheet 6
- CPUParticles2D (not GPU) for dust and glints
- State tracking: `threads_treads_state` (purchases, regular_status, two_am_purchases, who_choice, full_outfit_owned, morning_survived)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Entry bell tilt | Bell chime over rock bed | 0.0s on entry |
| Jacket equip | Jacket zip | On Zip Motion Lines |
| Boot equip | Boot stomp | On impact ring |
| Accessory equip | Chain rattle | On equip confirm |
| Mirror Moment flash | Transformation sting | Peak on flash F1 |
| 2 AM shift | Music bed swap, -4dB, quieter classic rock | Over the 60s transition |
| Fitting room | Curtain slide | On curtain open/close |
| Morning-After shrug | Quiet comedic sting | On No-Judgment Shrug |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Transformation Achievement Track | Outfit bundle icon, mirror flash, discount badge, 2 AM banner | "Shopping" → "No Regrets" toasts on first purchase, full outfit, genuine leather, 2 AM buy, confident wear, morning survival |
| "Who Do You Want To Be?" | Choice prompt UI, Zdeněk Assessing poses | First significant purchase; shapes recommendations and dialogue |
| Edgelord Discount | Discount badge, Regular-status dialogue | Unlocks after 3 purchases |
| Cool Factor economy | Cool meter, threshold pips, equipment sprites | Scene NPC reactions city-wide; wearing the shirt isn't enough — scene knowledge checks pair with it |
| 2 AM Transformation Discount | Discount banner, 2 AM lighting states | 3+ appearance-changing items between 02:00-05:00 = 10% off |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Velvet Curtain Club | Outfit affects bouncer interactions and NPC treatment | Equipment flags carry through entry |
| The Bohemian Trap | Certain looks change Emil's pitch | Dialogue branch on Cool Factor / leather equipped |
| Hostel Midnight Checkout | Other travelers react to the transformation | Reaction barks keyed to outfit-changed flag |
| Shadow Exchange | Style-based negotiation bonuses | Cool Factor read in negotiation UI |
| Neon & Chrome Boutique | Complementary vendor (fashion identity vs. club-specific gear); shared platform-boot market | Referenced in dialogue |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "An armory for identities — dark, moody, and surprisingly welcoming"
- **Color Mood:** Leather Black and Industrial Gray depth, Chrome Silver punctuation, Dark Red intimacy; Mirror Warm exists only where commerce needs kindness
- **Lighting:** Moody spots and dramatic shadows; the mirror wall is the one flattering zone in the shop, by strategy
- **Texture:** Real leather grain next to honest pleather sheen (priced accordingly), brushed chrome, worn floorboards from 10,000 transformations

### Environmental Storytelling:
- The honest sign: "Looking Dangerous Sold Separately (It's Inside You)" — the shop's whole philosophy in window vinyl
- The Soft Section is tucked at the back like contraband comfort — wanting the aesthetic without suffering is accommodated, discreetly
- Rock posters date from '98 forward: the shop's history is on the wall behind the register
- The fitting room feet gag under the curtain — transformation is a struggle, physically

### Character Integration Notes:
- Zdeněk never oversells: his poses are still, his assessments land because he isn't performing
- Eva is the aesthetic worn genuinely — her sprite IS the proof of concept the customers are buying toward
- Before/After mirror silhouettes differ in posture only; the satire is that the jacket changes nothing except how you stand, which changes everything

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Mirror Moment** - Before/after silhouettes, flash, and the stat panel — transformation as a game mechanic
2. **The Honest Window Sign** - "Looking Dangerous Sold Separately (It's Inside You)"
3. **The Bros Transformed Trio** - Three new identities walking out at 2:47 AM
4. **The Fitting Room Feet** - Boots wrestling under a curtain
5. **The Morning-After Return** - Same jacket, 9 AM light, different person

### Quote Potential:
- "People come here at 2 AM because something happened... I sell them leather. What they actually buy is permission."
- "You're buying an outfit or an identity? Different prices, same fitting room."
- "The sun will rise. You'll still be wearing this. Make sure you mean it."
- "I've dressed 10,000 transformations. Some stuck. Some didn't. The difference is never the jacket."
- "Pleather is a valid choice. The statement is what matters, not the cow."

---

## 📋 Required PNG Files (8 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | threads_exterior.png | 512x384 |
| 2 | threads_interior.png | 1024x512 |
| 3 | threads_equipment.png | 256x256 |
| 4 | threads_staff.png | 512x256 |
| 5 | threads_customers.png | 512x192 |
| 6 | mirror_transformation.png | 256x256 |
| 7 | threads_effects.png | 128x128 |
| 8 | threads_ui.png | 256x256 |

**Total Estimated Memory:** ~17 MB (well inside the 34 MB location budget)

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `threads_exterior.png` (512x384)
- [ ] `threads_interior.png` (1024x512)
- [ ] `threads_equipment.png` (256x256)
- [ ] `threads_staff.png` (512x256)
- [ ] `threads_customers.png` (512x192)
- [ ] `mirror_transformation.png` (256x256)
- [ ] `threads_effects.png` (128x128)
- [ ] `threads_ui.png` (256x256)
- [ ] `threads_accessibility.png` (256x256, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (day/2 AM lighting states separated; mirror compositing masks in their own group)
- **Documentation:** Animation timing reference sheet (mirror moment, try-on, 2 AM shift) + equipment catalog data map (sprite region → Defense/Cool Factor/effects)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Leather Black #1A1A1A, Chrome Silver #C0C0C0, Dark Red #8B0000, Industrial Gray #4A4A4A)
- [ ] Honest window sign readable on examine (the parenthetical carries the location)
- [ ] Before/After mirror silhouettes differ in posture only — same body, different standing
- [ ] Genuine and faux jacket sprites distinguishable by texture detail, honestly, per Zdeněk's materials policy
- [ ] Accessibility visual alternatives included for all audio cues (bell, zip, thud, sting, rattle, music shift)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (identity performance, affectionately understood) is clear throughout all assets
- [ ] Hidden details discoverable: tucked-away soft section, '98 poster timeline, fitting room feet, morning-after event
- [ ] Performance optimized (modulate-based 2 AM state, zone-gated mirror viewport, batched browser)
- [ ] Touch zone sizing considered (44px minimum — staff, browser, and mirror zones compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (pip thresholds, glyph-coded stats)
- [ ] Social media viral potential maximized (mirror moment, transformed trio, morning-after compositions)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Debaucheryville / Absinthe Arcade only |
| Cultural Specificity | ✅ | Eastern European leather culture and the rock/goth/alternative scene |
| Satirical Targets Appropriate | ✅ | The performance of edginess and 2 AM identity purchases — validated lovingly, never mocking subcultures themselves |
| Seedy Underbelly Present | ✅ | Selling "the them they want to be" at markup, 24 hours a day, to the freshly heartbroken |
| Gameplay Value Established | ✅ | Primary equipment vendor: Defense stats, Cool Factor economy, mirror system, transformation mechanics, Bravado hooks |
| Technical Feasibility | ✅ | 8 sheets, viewport mirror, modulate lighting, flag-based equipment — standard Godot 4.x |
| Performance Budget | ✅ | 60 FPS / 14 draw calls / 34 MB per profile; estimate ~17 MB |
| Accessibility Features | ✅ | Dark-shop hotspot outlines, flash-free mirror path, glyphs for every audio beat |
| No Crypto Elements | ✅ | Pure leather and chain commerce (profile-confirmed) |
| Social Media Integration | ✅ | Five viral moments identified, quotes sourced from profile dialogue |

**With these assets on the racks, Threads & Treads becomes the game's 24-hour confession booth with a register: players walk in as one person, wrestle with a curtain, stand differently in a flatteringly lit mirror, and walk out into the 2 AM Arcade wearing a decision. Zdeněk rings it up either way — the jacket was never the variable.**
