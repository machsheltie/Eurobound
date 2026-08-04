# The Cirque du Shady - Complete PNG Asset Requirements

## 📋 Overview
**Location ID:** `debaucheryville_circus_cirque_du_shady_01`
**Theme:** A traveling circus that stopped traveling in 1997 — a full-stack carnival grift ecosystem stitched from a rigged game alley, a garbage-prize booth, a food cart, a prophecy tent, a performance circle, and a reality-TV production office running off a folding table and a fax machine
**Zone:** Circus Grounds, edge of the Gilded Square District
**Hours:** 14:00–01:00 daily; Beatdown filming days shift traffic toward the riverside gear path (see parent profile's Time-of-Day Variations)

**Scope note:** This document specs only the assets new to this parent-grounds document — the gate, big top exterior, Vance's tent, the Shady Productions office, the knife-throwing act, game alley, and ICQ backroom. The prize booth and mystery meat cart keep their own already-published PNG asset docs (`Mystery_Meat_Cart_Complete_PNG_Asset_Requirements.md` and equivalents); this document does not duplicate or re-spec those files' assets. The prophecy tent's own performer — Hamstradamus — is not covered by a separate PNG asset doc; his sprite sheets (`hamstradamus.png`, `hamstradamus_tent_variant.png`, `hamstradamus_beach_variant.png`) are specced in `Design/Character Profiles/DebaucheryvilleNPCs/Cirque Du Shady/hamstradamus.md`, which owns his animation states. Bobo's performance spot sprites remain owned by his own profile's implementation pass, per Sprite Sheet 6's Technical Notes below.

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Faded Big-Top Red | #B22222 | Big top canvas panels, main gate arch trim |
| Canvas Cream | #F5F0DC | Tent canvas base tone, folding-table cloth |
| Neon Marquee | #FF6EC7 | Main gate marquee, night signage glow |
| Vape-Cloud Gray | #C0C0C8 | Vance's vape particle effects, ICQ monitor glow |
| Prophecy Purple | #6A0DAD | Prophecy Tent Glow (base pulse tone) |
| Prophecy Gold | #D4AF37 | Prophecy Tent Glow (crystal-ball highlight, ties to Hamstradamus's turban/crystal-ball dressing per `hamstradamus.md`) |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/cirque_du_shady/
├── environment/
│   ├── main_gate_and_marquee.png
│   ├── big_top_exterior.png
│   ├── vance_tent_exterior.png
│   ├── icq_backroom_interior.png
│   ├── game_alley_rig.png
│   ├── shady_productions_office.png
│   └── performance_circle_ground.png
├── npcs/
│   ├── vance_vallaro.png
│   └── blanka_knife_assistant.png
├── objects/
│   ├── ticket_booth.png
│   ├── corkboard_flyers.png
│   ├── fax_machine_and_flyers.png
│   ├── prize_pallet_2003_office.png
│   ├── knife_target_board.png
│   └── icq_terminal.png
├── effects/
│   ├── vape_cloud_particles.png
│   ├── marquee_flicker.png
│   ├── fax_paper_spit.png
│   └── prophecy_tent_glow.png
└── ui/
    └── knife_dodge_prompt_ui.png
```

---

## 🎪 Sprite Sheet 1: Main Gate & Marquee
**File:** `main_gate_and_marquee.png`
**Dimensions:** 1024x512 pixels

### Gate Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Entrance Arch | (0, 0) | 384x256 | "THE CIRQUE DU SHADY" hand-lettered arch, Faded Big-Top Red trim |
| Neon Marquee Overlay | (384, 0) | 256x128 | Night-only glow layer, Neon Marquee Pink |
| Rope Line + Posts | (640, 0) | 192x64 | Decorative, never actually holds back a crowd |
| Trampled-Grass-to-Sawdust Transition | (0, 256) | 512x128 | Gilded Square cobblestone → circus grounds ground tile |

### Technical Notes:
- Marquee glow layer is a separate additive overlay so it can be toggled off for day/night without re-rendering the arch base
- Ground transition tile is designed to tile-repeat along the approach path from the Gilded Square District

---

## 🎫 Sprite Sheet 2: Ticket Booth & Corkboard
**Files:** `ticket_booth.png`, `corkboard_flyers.png`
**Dimensions:** 256x256 pixels each

### Ticket Booth (`ticket_booth.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Booth Structure | (0, 0) | 192x192 | Warped plywood, barred window |
| Ticket Dispenser (idle) | (192, 0) | 64x64 | Hand-cranked, pre-jam state |
| Ticket Dispenser (jammed) | (192, 64) | 64x64 | Comedic jam frame |
| "5 Sovs / EVERYTHING ELSE EXTRA" Sign | (0, 192) | 192x64 | Main pricing sign, taped bathroom addendum visible on close read |

### Corkboard Flyers (`corkboard_flyers.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Corkboard Base | (0, 0) | 128x128 | Overlapping-flyer backing |
| Prophecy Roulette Hours Flyer | (128, 0) | 64x64 | Cross-references `hamstradamus.md` content, not re-specified here |
| Bubbles Missing-Elephant Poster | (0, 128) | 64x64 | Vanishing Elephant sidequest hook dressing |
| Shady Productions Casting Flyer (curled corner) | (64, 128) | 64x64 | Same flyer art as `fax_machine_and_flyers.png`, reused asset |

### Technical Notes:
- Casting-flyer art on the corkboard reuses the same texture region as the fax machine's printed flyer (see Sprite Sheet 5) — one source asset, two placements, no duplicate art required

---

## 🎪 Sprite Sheet 3: Big Top Exterior
**File:** `big_top_exterior.png`
**Dimensions:** 1024x768 pixels

### Dome & Structure:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Big Top Dome, Base | (0, 0) | 512x384 | Faded red-and-cream canvas, Faded Big-Top Red / Canvas Cream |
| Re-Stitched Canvas Patches (3 variants) | (512, 0) | 192x192 | Overlay decals for visible repair patches |
| Support Pole with Rust Rings | (704, 0) | 128x256 | Historical "used to have wheels" detail |
| Elephant-Adjacent Hay Dressing (interior glimpse) | (0, 384) | 256x128 | Bubbles enclosure ambient dressing, hook-only per parent profile |
| Big Top Entrance Flap | (256, 384) | 192x256 | Main dome entry point |

### Technical Notes:
- Hay dressing sprite is ambient-only; no Bubbles character sprite is speced in this document (Vanishing Elephant quest is a hook, not designed here)
- Canvas patches are randomly composited per-instance to avoid a uniform, obviously-tiled look

---

## ⛺ Sprite Sheet 4: Vance's Tent & ICQ Backroom
**Files:** `vance_tent_exterior.png`, `icq_backroom_interior.png`
**Dimensions:** 512x384 pixels each

### Vance's Tent (`vance_tent_exterior.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tent Structure, Flap Closed | (0, 0) | 192x256 | Abuts big top's side |
| Tent Structure, Flap Fogged (vape haze) | (192, 0) | 192x256 | Default idle-open state |
| "RINGMASTER — BY APPOINTMENT" Sign | (384, 0) | 128x64 | Hand-lettered |

### ICQ Backroom (`icq_backroom_interior.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Unmarked Canvas Flap, Day | (0, 0) | 192x256 | Propped open a crack |
| Unmarked Canvas Flap, Night (CRT glow visible) | (192, 0) | 192x256 | Monitor glow bleeding through the gap |
| Interior Glimpse (partial) | (384, 0) | 128x256 | Terminal silhouette, seen only through the flap gap |

### Technical Notes:
- ICQ backroom's night CRT-glow state is the primary readability cue that the hack-through event is more likely after dark — keep the glow color distinct from Vance's vape-cloud gray so players don't conflate the two flaps

---

## 🎯 Sprite Sheet 5: Shady Productions Office
**File:** `shady_productions_office.png` / `fax_machine_and_flyers.png` / `prize_pallet_2003_office.png`
**Dimensions:** 512x384 pixels / 256x192 pixels / 192x128 pixels

### Office Structure (`shady_productions_office.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Folding Card Table | (0, 0) | 192x128 | Canvas Cream tablecloth |
| Office Chair (wheel missing) | (192, 0) | 96x128 | Tilts visibly on the missing side |
| "SHADY PRODUCTIONS — SEASON 22" Sign | (288, 0) | 160x64 | Taped to fax machine, cross-referenced from `bacchanusbeachbeatdown.md` |
| Behind-Big-Top Canvas Backdrop | (0, 128) | 384x192 | Positions the office as physically behind the dome |

### Fax Machine & Flyers (`fax_machine_and_flyers.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fax Machine, Idle | (0, 0) | 96x96 | Pre-millennium hardware |
| Fax Machine, Paper-Spit (3-frame cycle) | (96, 0) | 96x96 | Casting-flyer print animation |
| Casting-Call Flyer (readable close-up) | (192, 0) | 64x96 | "WANTED: ATHLETIC-INTELLECTUAL HYBRID..." full text |
| Un-Collated Flyer Stack (table dressing) | (0, 96) | 128x64 | Ambient table clutter |

### Prize Pallet, Office Edge (`prize_pallet_2003_office.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pallet, Shrink-Wrapped, Office Variant | (0, 0) | 96x128 | Same asset family as the Bohemian Riviera's 2003 pallet, positioned at the tent-flap edge here |
| Pallet, Partial View (tent-flap occlusion) | (96, 0) | 96x128 | Half-visible-through-flap composite state |

### Technical Notes:
- Casting flyer readable-close-up texture is the same source art referenced by `corkboard_flyers.png` — build once, instance twice
- Prize pallet art should visually match (not duplicate at full resolution) the `prize_pallet_2003.png` asset already speced in `Bohemian_Riviera_PNG_Assets.md`, since both depict the same physical merchandise stock split across two storage locations

---

## 🔪 Sprite Sheet 6: Game Alley & Performance Circle
**File:** `game_alley_rig.png` / `performance_circle_ground.png` / `knife_target_board.png`
**Dimensions:** 1024x384 pixels / 512x256 pixels / 128x256 pixels

### Game Alley Rig (`game_alley_rig.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Milk Bottle Stack (concrete-filled) | (0, 0) | 128x128 | Rigged game 1 |
| Ring Toss Stand | (128, 0) | 128x128 | Oversized rings, undersized necks |
| Coin Pusher (3° tilt) | (256, 0) | 128x128 | Rigged game 3 |
| Barker Podium | (384, 0) | 96x128 | Generic across all three games |
| String Light Border | (0, 128) | 512x64 | Night dressing, tile-repeats the alley length |

### Performance Circle Ground (`performance_circle_ground.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Trampled-Grass Ring Base | (0, 0) | 256x256 | Shared by Bobo's pitch and the knife act |
| Mismatched Folding Chairs (cluster) | (256, 0) | 256x128 | Ambient audience seating |

### Knife Target Board (`knife_target_board.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Target Board, Leaned (idle, off-duty) | (0, 0) | 64x128 | Against support post |
| Target Board, Deployed (in use) | (64, 0) | 64x128 | Upright, scarred surface visible |

### Technical Notes:
- Performance-circle ground tile is intentionally neutral so Bobo's existing sprite sheet (already speced in his own profile's implementation pass) and the new knife-act sprites can share the same floor space without a seam
- Barker podium is a single shared asset across all three `game_alley` games, not rendered per-game, matching the mobile-optimization pattern used elsewhere in this world's location docs

---

## 👤 Sprite Sheet 7: NPCs — Vance & Blanka
**File:** `vance_vallaro.png` / `blanka_knife_assistant.png`
**Dimensions:** 384x288 pixels each

### Ringmaster Vance "Vape" Vallaro:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Idle, Tent Flap | (0, 0) | 64x96 | Default standing pose |
| Vape Exhale (3-frame cycle) | (64, 0) | 192x96 | Cloud puffs mid-sentence |
| Loot-Crate Pitch Gesture | (256, 0) | 64x96 | Presenting a crate |
| Vape-Cloud Speech-FX Overlay | (0, 96) | 128x64 | Composited over dialogue box during his lines |

### Blanka (Knife-Throwing Assistant):
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Idle at Target Board | (0, 0) | 64x96 | Professional stillness |
| Stepping Aside (hand-off to player) | (64, 0) | 64x96 | Coaching gesture |
| Dry Commentary Bark | (128, 0) | 64x96 | Talking pose, no unique mouth-flap needed beyond standard |

### Technical Notes:
- Vance's vape-cloud speech-FX overlay is reused as the same particle family as `vape_cloud_particles.png` (Sprite Sheet 8), just pre-composited into a fixed dialogue-box position for this variant
- No separate sprite sheet is speced for the knife-thrower himself (referenced only in prose in the parent profile) — if a future pass gives him a name and mechanics, he needs his own sheet; out of scope here

---

## ✨ Sprite Sheet 8: Environmental Effects & UI
**Files:** `vape_cloud_particles.png`, `marquee_flicker.png`, `fax_paper_spit.png`, `prophecy_tent_glow.png`, `icq_terminal.png`, `knife_dodge_prompt_ui.png`

### File Dimensions:
| File | Dimensions |
|------|------------|
| vape_cloud_particles.png | 128x128 |
| marquee_flicker.png | 256x128 |
| fax_paper_spit.png | 96x96 |
| prophecy_tent_glow.png | 192x192 |
| icq_terminal.png | 192x192 |
| knife_dodge_prompt_ui.png | 256x128 |

### Vape Cloud Particles (`vape_cloud_particles.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Cloud Puff, 4-Frame Loop | (0, 0) | 128x64 | Ambient drift near Vance's tent |
| Cloud Puff, Dialogue-Triggered (dense) | (0, 64) | 128x64 | Punctuates his mid-sentence exhale |

### Marquee Flicker (`marquee_flicker.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marquee, Full Glow | (0, 0) | 128x64 | Steady night state |
| Marquee, Flicker (4-frame cycle) | (128, 0) | 128x64 | Random-interval flicker, ties to Neon Marquee #FF6EC7 |

### Fax Paper Spit (`fax_paper_spit.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Paper Feed, 3-Frame Cycle | (0, 0) | 96x96 | Synced to the fax-machine chug audio cue |

### Prophecy Tent Glow (`prophecy_tent_glow.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Seam Glow, Idle Pulse (4-frame loop) | (0, 0) | 96x96 | Slow purple-gold pulse bleeding through the `prophecy_tent` canvas seams, Prophecy Purple base with Prophecy Gold highlight |
| Seam Glow, Prophecy-In-Progress (4-frame loop, brighter/faster) | (96, 0) | 96x96 | Intensified variant — triggers on any Prophecy Roulette delivery or in-battle doom prediction, per the `prophecy_trance` cue already defined in `hamstradamus.md` |
| Seam Glow, Overlay Mask | (0, 96) | 96x96 | Alpha mask used to composite the glow through the existing `prophecy_tent` canvas art without a separate tent re-render |

### ICQ Terminal (`icq_terminal.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Terminal, Idle Glow | (0, 0) | 96x96 | CRT green-gray ambient state |
| Terminal, Hack-Through Active | (96, 0) | 96x96 | Darkweb Dossier pop-in visual state |

### Knife Dodge Prompt UI (`knife_dodge_prompt_ui.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dodge Prompt, Left/Right/Center (3 icons) | (0, 0) | 192x64 | Directional dodge cue set |
| Success Flash | (192, 0) | 64x64 | On successful dodge |

### Technical Notes:
- Marquee flicker interval should be random, not metronomic, to avoid reading as a bug rather than a joke
- ICQ terminal's hack-through state is the visual trigger for the ambient Darkweb Dossier pop-in event referenced in the parent profile's Time-of-Day Variations
- Prophecy Tent Glow is a `prophecy_tent` zone-exterior effect only — it dresses the tent from outside the canvas; it does not modify or duplicate any of Hamstradamus's own interior/performer animation states (`prophecy_trance`, `crystal_ball_trip`, etc.), which remain fully owned by `hamstradamus.md`

---

## 🎬 Animation Specifications

### Vape Cloud Exhale:
- **Duration:** ~1.5 seconds
- **Frames:** 4 (ambient) / 4 (dialogue-triggered dense variant)
- **Loop:** Ambient variant loops; dialogue variant is one-shot per line
- **Timing:** 3fps ambient drift, faster 6fps burst on dialogue trigger

### Marquee Flicker:
- **Duration:** Variable, random 0.2–0.6s intervals
- **Frames:** 4
- **Loop:** Yes, night-only
- **Timing:** Randomized, not metronomic

### Prophecy Tent Glow:
- **Duration:** ~4 seconds per pulse cycle (idle state); ~1.5 seconds per pulse cycle (prophecy-in-progress state)
- **Frames:** 4 (idle loop) / 4 (intensified loop)
- **Loop:** Yes, both states loop continuously; state swap is instant, not crossfaded
- **Timing:** Idle — slow purple-gold pulse, 1fps effective cadence, seam-only bleed-through; Prophecy-In-Progress — brighter and roughly 2.5x faster, triggered by the same event window as Hamstradamus's own `prophecy_trance` animation (`hamstradamus.md`) so the tent's exterior glow and his interior performance read as one beat from outside the canvas

### Fax Machine Paper Spit:
- **Duration:** ~1 second
- **Frames:** 3
- **Loop:** No, one-shot per casting-flyer print event
- **Timing:** Synced to the paper-feed chug audio cue

### Ticket Dispenser Jam-and-Release:
- **Duration:** ~2 seconds
- **Frames:** 2 (jam) + 2 (release)
- **Loop:** No, plays once per ticket purchase
- **Timing:** Jam holds ~1.2s before release resolves

### Knife-Throw Dodge Round:
- **Duration:** ~1 second per throw
- **Frames:** 4 (whistle-in, impact/dodge resolution)
- **Loop:** No, per-throw one-shot
- **Timing:** Synced to whistle-and-thunk audio cue

---

## ♿ Accessibility Sprite Requirements
**File:** `cirque_grounds_accessibility.png` (supplemental sheet — delivered alongside the 20 base files, not counted in their total)
**Dimensions:** 384x384 pixels

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dodge Prompt Icons, Bold (x3) | (0, 0) | 192x64 | Thick-outline left/right/center dodge cues for the knife minigame |
| ICQ Terminal Outline | (192, 0) | 96x96 | High-contrast terminal hotspot outline for the backroom flap interaction |
| Ticket Booth Window Outline | (288, 0) | 96x96 | Outlined barred-window interactable at `main_gate` |
| Casting Flyer, Large-Print | (0, 64) | 96x128 | Enlarged readable variant of the "ATHLETIC-INTELLECTUAL HYBRID" flyer close-up |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Marquee, Steady Glow | (96, 64) | 128x64 | Constant night glow replacing the random-interval flicker (the flicker is a joke, but it is still a flicker) |
| Vape Cloud, Static Wisp | (224, 64) | 64x64 | Single non-drifting cloud decal replacing both particle loops near Vance's tent |
| Prophecy Glow, Constant | (96, 128) | 96x96 | Steady mid-brightness seam glow replacing both pulse states — prophecy-in-progress signaled by brightness step, not speed |
| Fax Spit, Single-Frame | (192, 128) | 96x96 | One static paper-out frame replacing the 3-frame cycle |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Knife Whistle-In Arrow | (0, 192) | 64x48 | Directional incoming-throw indicator preceding each knife by the whistle's lead time — required, since the dodge minigame's timing tell is the whistle-and-thunk audio |
| Knife Thunk Burst | (64, 192) | 48x48 | Impact star on the target board at the thunk |
| Calliope Note Icon | (112, 192) | 48x48 | Drifting warped-note icon marking the grounds-wide calliope loop (drops out in the two quiet zones, matching the audio mix) |
| Fax Chug Icon | (160, 192) | 48x48 | Vibration lines on the fax machine during each print event |
| Ticket Jam Clunk Icon | (208, 192) | 48x48 | Jam/clunk indicator over the dispenser during the jam-and-release cycle |
| Hamster Techno Wisp | (256, 192) | 48x48 | Faint note-trail from `prophecy_tent`'s direction when the distant techno is active — cuts off with the food-cart hiss, exactly like the audio |

### Colorblind Considerations:
- Dodge prompts are directional shapes (arrows/center diamond), never color-coded alone
- ICQ CRT green-gray glow and Vance's Vape-Cloud Gray stay visually distinct via shape and placement, not hue alone (per Sprite Sheet 4's technical note)
- Prophecy Purple/Gold pulse carries a seam-pattern change between idle and in-progress states, not just a color shift
- Dodge icons (64px each), ticket booth window, and ICQ terminal hotspot all meet the 44px minimum touch target

---

## 📱 Mobile Optimization

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| Cirque Grounds Environment Atlas | main_gate_and_marquee, big_top_exterior, vance_tent_exterior, icq_backroom_interior | 2048x2048 |
| Cirque Grounds Object Atlas | ticket_booth, corkboard_flyers, fax_machine_and_flyers, prize_pallet_2003_office, knife_target_board, icq_terminal | 2048x2048 |
| Cirque Grounds Circle Atlas | game_alley_rig, shady_productions_office, performance_circle_ground | 2048x2048 |
| Cirque Grounds NPC Atlas | vance_vallaro, blanka_knife_assistant | 1024x1024 |
| Cirque Grounds Effects/UI Atlas | vape_cloud_particles, marquee_flicker, fax_paper_spit, prophecy_tent_glow, knife_dodge_prompt_ui | 1024x1024 |

### Performance Notes:
- Vape-cloud particle density is reducible on mobile (ambient drift can drop to 2-frame loop under LOD pressure)
- Grounds crowd (shared with sub-locations' own crowd assets) LOD-steps down aggressively past `game_alley` mid-ground, consistent with the pattern already established in `Bohemian_Riviera_PNG_Assets.md`
- Casting-flyer texture is built once and instanced at both the corkboard and the fax machine, halving that asset's memory footprint
- This document intentionally excludes the prize booth and mystery meat cart sprites — those remain owned by their own already-published PNG asset docs and must not be re-exported here. It likewise excludes Hamstradamus's prophecy-tent performer sprites (owned by `hamstradamus.md`, not a PNG asset doc) and Bobo's performance sprites (owned by his own profile's implementation pass)

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- TileMap for the trampled-grass-to-sawdust transition and grounds paths; additive-blend overlay layers for the marquee glow and prophecy tent seam glow (glow mask composites through existing tent art, no re-render)
- CPUParticles2D (not GPU) for vape clouds, dust motes, fax paper flutter; marquee flicker on a randomized (non-metronomic) timer script
- Area2D hotspots: `icq_backroom` terminal (random Darkweb Dossier hack-through pop-ins, weighted toward after-dark), Shady Productions table/fax (`beatdown_aware` trigger), Vance's tent flap (`vance_met` trigger)
- Sub-location handoffs: `prophecy_tent`, `prize_booth`, `meat_cart_pitch`, and Bobo's pitch transition to mechanics owned by their own files — this document's assets stop at each zone boundary
- State tracking per `cirque_du_shady_state` (cirque_visited, beatdown_aware, vance_met, filming_day_active, icq_backroom_hackthrough_seen)

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Fax Paper-Spit (3 frames) | Paper-feed chug | Chug per frame; lands on a beat if a bro reads the flyer aloud |
| Ticket Dispenser Jam-and-Release | Jam clunk → dispense clatter | Jam holds ~1.2s before release resolves |
| Knife-Throw Dodge Round | Whistle-in → thunk | Whistle leads each throw; thunk on impact/dodge resolution frame |
| Vape Exhale (dialogue variant) | Audible exhale in Vance's line pacing | Cloud burst on the vape-cloud-shaped pause — built into the voice track, not layered after |
| Marquee Flicker | Neon buzz waver | Buzz dips on off-frames; randomized so it reads as a joke, not a bug |
| Prophecy Glow, In-Progress | Prophecy delivery (per `hamstradamus.md` `prophecy_trance` cue) | Glow state swap is instant on the same event window — tent exterior and interior performance read as one beat |
| Rigged Game Loss | Sad calliope note | On loss resolution at any `game_alley` game |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| Bacchanus Beach Beatdown (`debaucheryville_sidequest_bacchanus_beach_beatdown_01`) | shady_productions_office, fax_machine_and_flyers, corkboard casting flyer, prize_pallet_2003_office | `beatdown_aware` fires on examining the table/fax or hearing Vance mention "the show" — foreshadowing only; sign-up lives at Fauxst Beach |
| The Vanishing Elephant (hook only) | Bubbles missing-elephant poster (corkboard), elephant-adjacent hay dressing (big top) | Ambient dressing per GDD canon; quest not designed in this document |
| ICQ Scammer Sting (cross-referenced) | icq_terminal (idle + hack-through states), icq_backroom_interior night CRT glow | Shares the ICQ substrate and the `Tony420` handle with that questline's cast |
| Prophecy Roulette (owned by `hamstradamus.md`) | prophecy_tent_glow (exterior only) | Glow intensifies on Prophecy Roulette delivery; performer sprites remain owned by his profile |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| Gilded Square Streets | main_gate_and_marquee, trampled-grass-to-sawdust transition tile | Approach smell/sound before the gate is visible; standard street fade |
| The Bohemian Riviera | Riverside gear path from `shady_productions_office`; prize_pallet_2003_office must visually match `prize_pallet_2003.png` in `Bohemian_Riviera_PNG_Assets.md` (same merchandise stock, two storage locations) | Gear-path walk; visible production traffic on filming days |
| Prize Booth (`the_participation_trophy.md`) | Vance's loot-crate voucher pitch hands off to Yolanda's counter | Two-zone transaction: pitch at his tent, fulfillment at `prize_booth` |
| Fauxst Beach (filming days) | Hamstradamus travels the gear path between `prophecy_tent` and `prize_podium` | His tent sits dark/glow-idle while he is absent |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "A traveling circus that stopped traveling in 1997 and never updated a single piece of infrastructure since"
- **Color Mood:** Faded Big-Top Red and Canvas Cream carry the washed-out grandeur; Neon Marquee pink and Prophecy Purple/Gold are the only things on the grounds still trying
- **Lighting:** Afternoon — flat dusty daylight filtered through canvas seams; Night — neon marquee, `game_alley` string bulbs, and whatever spills from tent flaps (Vance's fog, the ICQ CRT glow, the prophecy seam pulse)
- **Texture:** Re-stitched canvas patches (randomly composited per-instance), rust rings where wheels used to be, warped plywood, pre-millennium office hardware

### Environmental Storytelling:
- The support pole's rust rings say "used to have wheels" without a line of dialogue
- The ticket booth sign's taped-on bathroom addendum, the scratched-out EST. date, the 2003 pallet at the office edge — honesty and decay in every prop
- The same casting flyer at two placements (fax + corkboard) — the operation has printed one document for twenty-two seasons
- Bubbles's missing-elephant poster beside faint hay dressing: the elephant is still, technically, on the premises

### Character Integration Notes:
- Vance's vape-cloud speech FX composite over his dialogue box — his pacing is visible, not just audible
- Blanka's professional stillness contrasts the player's dodge prompts; no knife-thrower sprite exists by design (out of scope until he gets a name)
- Sub-location performers (Hamstradamus, Yolanda, Chef Chuckles, Bobo) keep their own files' sprite ownership — grounds art frames them, never redraws them

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The ticket booth sign** - "ADMISSION 5 Sovs. EVERYTHING ELSE EXTRA." with the taped addendum "(THIS INCLUDES THE BATHROOM.)"
2. **Vance mid-exhale pitch** - Ringmaster coat, top hat, vape cloud punctuating a loot-crate sales line
3. **The fax machine at work** - A pre-millennium machine printing the identical casting flyer onto a pile of identical casting flyers
4. **The prophecy tent at night** - Purple-gold seams pulsing while the marquee flickers and the calliope warps
5. **The knife dodge round** - Player in Blanka's spot, incoming-throw arrow, scarred target board

### Quote Potential:
- "Semi-permanent. That's the word. We COULD move. We just — *(exhale)* — haven't needed to."
- "It's — *(exhale)* — it's a bit of a gamble, honestly. Aren't we all?"
- "I flinch never."
- "WANTED: ATHLETIC-INTELLECTUAL HYBRID. CARGO SHORTS PREFERRED. NO EXPERIENCE NECESSARY."

---

## 📋 Required PNG Files (20 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | main_gate_and_marquee.png | 1024x512 |
| 2 | ticket_booth.png | 256x256 |
| 3 | corkboard_flyers.png | 256x256 |
| 4 | big_top_exterior.png | 1024x768 |
| 5 | vance_tent_exterior.png | 512x384 |
| 6 | icq_backroom_interior.png | 512x384 |
| 7 | shady_productions_office.png | 512x384 |
| 8 | fax_machine_and_flyers.png | 256x192 |
| 9 | prize_pallet_2003_office.png | 192x128 |
| 10 | game_alley_rig.png | 1024x384 |
| 11 | performance_circle_ground.png | 512x256 |
| 12 | knife_target_board.png | 128x256 |
| 13 | vance_vallaro.png | 384x288 |
| 14 | blanka_knife_assistant.png | 384x288 |
| 15 | vape_cloud_particles.png | 128x128 |
| 16 | marquee_flicker.png | 256x128 |
| 17 | fax_paper_spit.png | 96x96 |
| 18 | prophecy_tent_glow.png | 192x192 |
| 19 | icq_terminal.png | 192x192 |
| 20 | knife_dodge_prompt_ui.png | 256x128 |

**Total Estimated Memory:** ~39MB

---

## 📦 File Delivery Checklist

### Required PNG Files:
- [ ] `main_gate_and_marquee.png` (1024x512)
- [ ] `ticket_booth.png` (256x256)
- [ ] `corkboard_flyers.png` (256x256)
- [ ] `big_top_exterior.png` (1024x768)
- [ ] `vance_tent_exterior.png` (512x384)
- [ ] `icq_backroom_interior.png` (512x384)
- [ ] `shady_productions_office.png` (512x384)
- [ ] `fax_machine_and_flyers.png` (256x192)
- [ ] `prize_pallet_2003_office.png` (192x128)
- [ ] `game_alley_rig.png` (1024x384)
- [ ] `performance_circle_ground.png` (512x256)
- [ ] `knife_target_board.png` (128x256)
- [ ] `vance_vallaro.png` (384x288)
- [ ] `blanka_knife_assistant.png` (384x288)
- [ ] `vape_cloud_particles.png` (128x128)
- [ ] `marquee_flicker.png` (256x128)
- [ ] `fax_paper_spit.png` (96x96)
- [ ] `prophecy_tent_glow.png` (192x192)
- [ ] `icq_terminal.png` (192x192)
- [ ] `knife_dodge_prompt_ui.png` (256x128)
- [ ] `cirque_grounds_accessibility.png` (384x384, supplemental)

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
- **Backup:** Master PSD/layered file with organized layer groups (marquee glow and prophecy seam glow as separate additive-overlay layers; canvas patch decals in their own group for per-instance compositing)
- **Documentation:** Animation timing reference sheet (marquee random-interval ranges, prophecy glow dual pulse rates, fax/knife/ticket one-shot timings)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly (Faded Big-Top Red #B22222, Canvas Cream #F5F0DC, Neon Marquee #FF6EC7, Vape-Cloud Gray #C0C0C8, Prophecy Purple #6A0DAD, Prophecy Gold #D4AF37)
- [ ] Casting flyer built once and instanced at both corkboard and fax placements — no duplicate art
- [ ] Office prize pallet visually matches (does not duplicate) the Bohemian Riviera's `prize_pallet_2003.png`
- [ ] ICQ CRT glow reads distinct from vape-cloud gray at night
- [ ] Accessibility visual alternatives included for all audio cues — especially the knife whistle-in arrow (the dodge tell is otherwise audio-led)
- [ ] File naming follows snake_case convention
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (a fully honest grift ecosystem that hasn't updated since 1997) is clear throughout all assets
- [ ] Readable details intact: bathroom addendum, scratched-out EST. date, rust rings, 2003 pallet stamp, Bubbles poster
- [ ] No assets re-exported from sub-location PNG docs (prize booth, mystery meat cart) or from `hamstradamus.md` / Bobo's profile
- [ ] Mobile performance optimized (CPU particles, reducible vape density, aggressive crowd LOD past `game_alley`)
- [ ] Touch zone sizing considered (44px minimum — dodge icons, ticket booth, ICQ terminal compliant)
- [ ] Colorblind-friendly alternatives available where color codes meaning (shape-coded dodge prompts, patterned prophecy pulse)
- [ ] Social media viral potential maximized (ticket-booth signage frame, fax-machine composition)

---

## ✅ Validation Status

| Requirement | Status |
|-------------|--------|
| World Consistency | ✅ PASS |
| Cultural Specificity | ✅ PASS |
| Satirical Targets | ✅ PASS |
| Gameplay Value | ✅ PASS |
| No Crypto Elements Beyond Existing Bobo Pointer | ✅ PASS |
| Mobile Optimization | ✅ PASS |
| No Duplicate Assets vs. Sub-Location PNG Docs | ✅ PASS |
| Seedy Underbelly Present | ✅ PASS (grounds-wide grift pipeline, rigged games to TV recruitment) |
| Technical Feasibility | ✅ PASS (stitched-zone approach within budget) |
| Mobile Performance Budget | ✅ PASS (45-60 FPS, 30-45 draw calls, 55-70MB grounds-wide) |
| Accessibility Features | ✅ PASS (visual knife-throw tell, steady-glow variants) |
| Social Media Integration | ✅ PASS (viral moments identified) |

**The Cirque du Shady's grounds-level art spec covers the gate, the big top's exterior, a Ringmaster who exhales mid-sentence, a fax machine that has printed the same flyer for twenty-two seasons, and a knife act older than most of its audience — while leaving every already-published sub-location's own asset spec exactly where it lives.**
