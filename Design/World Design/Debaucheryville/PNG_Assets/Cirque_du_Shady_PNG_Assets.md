# The Cirque du Shady - Complete PNG Asset Requirements

## 📋 Overview
**Location ID:** `debaucheryville_circus_cirque_du_shady_01`
**Theme:** A traveling circus that stopped traveling in 1997 — a full-stack carnival grift ecosystem stitched from a rigged game alley, a garbage-prize booth, a food cart, a prophecy tent, a performance circle, and a reality-TV production office running off a folding table and a fax machine
**Zone:** Circus Grounds, edge of Old Town
**Hours:** 14:00–01:00 daily; Beatdown filming days shift traffic toward the riverside gear path (see parent profile's Time-of-Day Variations)

**Scope note:** This document specs only the assets new to this parent-grounds document — the gate, big top exterior, Vance's tent, the Shady Productions office, the knife-throwing act, game alley, and ICQ backroom. The prize booth, mystery meat cart, prophecy tent, and Bobo's performance spot keep their own already-published PNG asset docs (`Mystery_Meat_Cart_Complete_PNG_Asset_Requirements.md` and equivalents); this document does not duplicate or re-spec those files' assets.

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Faded Big-Top Red | #B22222 | Big top canvas panels, main gate arch trim |
| Canvas Cream | #F5F0DC | Tent canvas base tone, folding-table cloth |
| Neon Marquee | #FF6EC7 | Main gate marquee, night signage glow |
| Vape-Cloud Gray | #C0C0C8 | Vance's vape particle effects, ICQ monitor glow |

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
│   └── fax_paper_spit.png
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
| Trampled-Grass-to-Sawdust Transition | (0, 256) | 512x128 | Old Town cobblestone → circus grounds ground tile |

### Technical Notes:
- Marquee glow layer is a separate additive overlay so it can be toggled off for day/night without re-rendering the arch base
- Ground transition tile is designed to tile-repeat along the approach path from Old Town

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
| "€5 / EVERYTHING ELSE EXTRA" Sign | (0, 192) | 192x64 | Main pricing sign, taped bathroom addendum visible on close read |

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
**Files:** `vape_cloud_particles.png`, `marquee_flicker.png`, `fax_paper_spit.png`, `icq_terminal.png`, `knife_dodge_prompt_ui.png`

### File Dimensions:
| File | Dimensions |
|------|------------|
| vape_cloud_particles.png | 128x128 |
| marquee_flicker.png | 256x128 |
| fax_paper_spit.png | 96x96 |
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

## 📱 Mobile Optimization

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| Cirque Grounds Environment Atlas | main_gate_and_marquee, big_top_exterior, vance_tent_exterior, icq_backroom_interior | 2048x2048 |
| Cirque Grounds Object Atlas | ticket_booth, corkboard_flyers, fax_machine_and_flyers, prize_pallet_2003_office, knife_target_board, icq_terminal | 2048x2048 |
| Cirque Grounds Circle Atlas | game_alley_rig, shady_productions_office, performance_circle_ground | 2048x2048 |
| Cirque Grounds NPC Atlas | vance_vallaro, blanka_knife_assistant | 1024x1024 |
| Cirque Grounds Effects/UI Atlas | vape_cloud_particles, marquee_flicker, fax_paper_spit, knife_dodge_prompt_ui | 1024x1024 |

### Performance Notes:
- Vape-cloud particle density is reducible on mobile (ambient drift can drop to 2-frame loop under LOD pressure)
- Grounds crowd (shared with sub-locations' own crowd assets) LOD-steps down aggressively past `game_alley` mid-ground, consistent with the pattern already established in `Bohemian_Riviera_PNG_Assets.md`
- Casting-flyer texture is built once and instanced at both the corkboard and the fax machine, halving that asset's memory footprint
- This document intentionally excludes the prize booth, mystery meat cart, prophecy tent, and Bobo's performance sprites — those remain owned by their own already-published PNG asset docs and must not be re-exported here

---

## 📋 Required PNG Files (19 Total)

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
| 18 | icq_terminal.png | 192x192 |
| 19 | knife_dodge_prompt_ui.png | 256x128 |

**Total Estimated Memory:** ~38MB

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

**The Cirque du Shady's grounds-level art spec covers the gate, the big top's exterior, a Ringmaster who exhales mid-sentence, a fax machine that has printed the same flyer for twenty-two seasons, and a knife act older than most of its audience — while leaving every already-published sub-location's own asset spec exactly where it lives.**
