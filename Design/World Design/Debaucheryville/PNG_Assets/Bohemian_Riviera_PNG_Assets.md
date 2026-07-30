# The Bohemian Riviera - Complete PNG Asset Requirements

## 📋 Overview
**Location ID:** `debaucheryville_riverfront_bohemian_riviera_01`
**Theme:** A landlocked country's beach resort — trucked-in sand, inflatable palms, and a reality-TV catapult show that has launched two out of three contestants for twenty-two consecutive seasons
**Zone:** The Bacchanus Riverfront
**Hours:** 24/7 (Beatdown filming days on rotating schedule; night-party zone unlocks post-quest-completion)

---

## 🎨 Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Sand | #E8D4A0 | Fauxst Beach ground, loungers |
| The Bacchanus (murk-green) | #5E7350 | River water, splash effects |
| EMTV Magenta | #FF1493 | Production branding, crane, signage, bar-TV glow |
| Catapult Steel | #708090 | Pneumatic arm, port-o-potty frame hardware |
| Inflatable-Palm Green | #32CD32 | Palm trees, tiki decor accents |
| Space Heater Orange | #FF7F32 | Heater glow, golden-hour accent |
| Night String-Light Amber | #FFC966 | Night party zone lighting |

---

## 📁 File Structure
```
assets/sprites/locations/debaucheryville/bohemian_riviera/
├── environment/
│   ├── fauxst_beach_tileset.png
│   ├── bar_strip_facades.png
│   ├── catapult_rig_and_toilets.png
│   ├── prize_podium_and_banner.png
│   ├── signup_table_setup.png
│   ├── night_party_zone_dressing.png
│   └── river_parallax_background.png
├── npcs/
│   ├── jaxson_vane.png
│   ├── janek_sykora.png
│   ├── petra_production_assistant.png
│   ├── hamstradamus_beach_variant.png
│   ├── rosta_retrieval_man.png
│   ├── standa_lifeguard.png
│   ├── zdenka_shower_vendor.png
│   └── vacationer_crowd.png
├── objects/
│   ├── inflatable_palm_trees.png
│   ├── space_heaters.png
│   ├── lifeguard_tower.png
│   ├── no_diving_sign.png
│   ├── release_forms_and_clipboard.png
│   ├── prize_pallet_2003.png
│   └── riverbank_portapotty_monuments.png
├── effects/
│   ├── launch_splash_and_arc.png
│   ├── heat_shimmer.png
│   ├── confetti_and_string_lights.png
│   └── port_o_cologne_flies.png
└── ui/
    ├── strike_counter_and_timer.png
    ├── suspicion_meter_oakleys.png
    └── dialogue_and_prompt_ui.png
```

---

## 🏖️ Sprite Sheet 1: Fauxst Beach Environment
**File:** `fauxst_beach_tileset.png`
**Dimensions:** 1024x512 pixels

### Ground & Set Dressing:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sand Base | (0, 0) | 512x256 | Raked trucked-in sand tile |
| Sand Variant (footprints) | (512, 0) | 256x128 | Worn crowd-traffic patch |
| Delivery Receipt Sign | (768, 0) | 128x64 | "40 TONS — NOT FOR HUMAN CONSUMPTION" |
| Lounger Cluster | (0, 256) | 256x128 | Mismatched beach chairs |
| Lifeguard Tower Base | (256, 256) | 192x256 | Structural tower background placement; full interactive foreground tower with Standa in Sprite Sheet 8 |
| Riverbank Edge | (448, 256) | 320x128 | Sand-to-water transition |
| No Diving Sign Post | (768, 128) | 96x128 | Zip-tied hand-lettered sign |

### Technical Notes:
- Sand tile needs a subtle heat-shimmer overlay hook (see Sprite Sheet 8: Environmental Props & Effects) at midday
- Delivery receipt is a static readable-on-approach detail, not an interactable

---

## 🍹 Sprite Sheet 2: Bar Strip Facades
**File:** `bar_strip_facades.png`
**Dimensions:** 1024x384 pixels

### Venue Frontages:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Žá Žá Beach Klub | (0, 0) | 320x256 | Repainted shipping container, string lights |
| The Tan Line | (320, 0) | 320x256 | Sports-bar shell, tanning-bed neon trim |
| Kokos Loco | (640, 0) | 320x256 | Plastic tiki-hut facade, painted coconuts |
| Shared Bar TV | (960, 0) | 64x64 | Mounted screen, looping episode footage |
| Terrace Seating | (0, 256) | 512x128 | Shared outdoor tables, all three venues |
| Sound System Stack | (512, 256) | 128x128 | Migrates nightly, Eurodance source |

### Technical Notes:
- Bar TV sprite is a single shared asset instanced across all three venue facades, not rendered per-venue (mobile memory optimization)
- Terrace seating tile-repeats to extend the strip without new art

---

## 🚽 Sprite Sheet 3: Catapult Rig & Port-O-Potties
**File:** `catapult_rig_and_toilets.png`
**Dimensions:** 1024x512 pixels

### Rig & Launch Frames:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pneumatic Arm (idle) | (0, 0) | 256x256 | Steel arm, roped off between tapings |
| Port-O-Potty Unit — Left | (256, 0) | 128x192 | Static loaded state |
| Port-O-Potty Unit — Center (broken latch) | (384, 0) | 128x192 | Door ajar variant included |
| Port-O-Potty Unit — Right | (512, 0) | 128x192 | Static loaded state |
| Launch Animation — Wind-Up | (640, 0) | 128x128 | 2 frames |
| Launch Animation — Release | (640, 128) | 384x128 | 6 frames, staggered per unit |
| Launch Animation — Mid-Arc | (0, 256) | 384x128 | 4 frames, arc must clear palms/tower |
| Launch Animation — Splash Impact | (384, 256) | 256x128 | 4 frames; reusable particle overlay mirrored in `launch_splash_and_arc.png` (Required PNG Files #18) |
| Hazard Tape / Off-Season Dressing | (0, 384) | 256x64 | Roped-off state between tapings |
| Prize Pallet (2003, background) | (256, 384) | 192x128 | Half-opened, visible not pointed at |

### Technical Notes:
- **Three independently-triggerable launch units required** — build as separate triggerable animation instances, not a single combined three-unit sequence, so Launch One (Q4 interruption) and Launch Two (Q7 mid-syllable) can fire on independent timers
- Broken center-unit door-swing needs its own idle-open state, reusable outside the launch sequence
- Arc must visibly clear inflatable palms and lifeguard tower before water contact (see Sprite Sheet 1 for the lifeguard tower silhouette and Sprite Sheet 7 for the inflatable palm silhouettes)

---

## 🎙️ Sprite Sheet 4: Sign-Up Table & Prize Podium
**File:** `signup_table_setup.png` / `prize_podium_and_banner.png`
**Dimensions:** 512x384 pixels each

### Sign-Up Table Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Folding Table | (0, 0) | 192x128 | Petra's station |
| Clipboard + Pen (coiled cord) | (192, 0) | 96x96 | Interactable prop |
| Release Forms (fanned) | (288, 0) | 128x96 | 3 forms, Czech-parody text |
| Sign-Up Multilingual Banner | (0, 128) | 384x64 | "SIGN-UP HERE" x6 languages |

### Prize Podium Elements:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Card Table (creased banner) | (0, 0) | 256x192 | Shady Productions logo, folded crease visible |
| Hamstradamus Trapdoor | (256, 0) | 64x64 | Entrance point |
| Confetti Residue (ground) | (0, 192) | 256x64 | Never fully swept |

---

## 👥 Sprite Sheet 5: NPCs — Principal Cast
**File:** `jaxson_vane.png` / `janek_sykora.png` / `petra_production_assistant.png` / `hamstradamus_beach_variant.png`
**Dimensions:** 384x288 pixels each

### Jaxson Vane:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Hosting Idle | (0, 0) | 64x96 | Cue card up, Oakleys on |
| Triple-Can Sip | (64, 0) | 192x96 | Rehearsed triple-can sip, 6 frames at 32x96 each (2 per can) |
| Lever Pull | (256, 0) | 64x96 | "Unfortunately, bro." |
| Oakleys Removal (DQ) | (0, 96) | 64x96 | Disqualification stance |
| Crowd Scan | (64, 96) | 64x96 | Camera-trained sweep |

### Janek Sýkora:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Idle Perfect Posture | (0, 0) | 64x96 | Gym bag at feet |
| Bored Answer | (64, 0) | 64x96 | Quick correct answer |
| Buzzer Wave (1.5s window) | (128, 0) | 192x96 | Sudden Death tell, 4 frames |
| Polite Handshake | (320, 0) | 64x96 | Post-round beat |

### Petra:
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Table Disclosure | (0, 0) | 64x96 | Clipboard, mid-script |
| Form Present | (64, 0) | 64x96 | Fanning out release forms |
| Clipboard Tick | (128, 0) | 64x96 | Precise checkmark |
| Headset Log | (192, 0) | 64x96 | Off-table, coordinating |

### Hamstradamus (Beach Variant):
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Speedo Strut | (0, 0) | 192x96 | Full-table strut, profile, 4 frames |
| Badge Pin | (192, 0) | 96x96 | Crooked badge lands on application |
| Prophecy Trance | (0, 96) | 64x96 | Whiskers still, booming voice |

---

## 🪝 Sprite Sheet 6: Location NPCs
**File:** `rosta_retrieval_man.png` / `standa_lifeguard.png` / `zdenka_shower_vendor.png`
**Dimensions:** 256x192 pixels each

### Rosťa (Boat-Hook Retrieval Man):
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Idle at Station | (0, 0) | 64x96 | Boat hook in hand |
| Retrieval Action | (64, 0) | 64x96 | Hooking a drifting unit |
| Monument Placement | (128, 0) | 64x96 | Standing a unit upright on the bank |

### Standa (Lifeguard):
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Tower Idle (reading) | (0, 0) | 64x96 | Paperback in hand |
| Whistle Blow | (64, 0) | 64x96 | Reacting to a launch |
| Tower Scan | (128, 0) | 64x96 | Half-hearted lifeguard duty |

### Zdenka (Shower Vendor):
| Pose | Position | Size | Description |
|------|----------|------|-------------|
| Cart Idle | (0, 0) | 64x96 | Behind the shower cart |
| Transaction | (64, 0) | 64x96 | Taking coins |
| Hose Deployed | (128, 0) | 64x96 | `port_o_cologne` cure animation |

---

## 🏄 Sprite Sheet 7: Vacationer Crowd & Environmental Objects
**File:** `vacationer_crowd.png` / `inflatable_palm_trees.png` / `riverbank_portapotty_monuments.png`
**Dimensions:** 512x384 pixels / 256x256 pixels / 256x256 pixels

### Vacationer Crowd:
| Sprite Type | Position | Size | Description |
|-------------|----------|------|-------------|
| Flip-Phone Filmer | (0, 0) | 32x48 | Filming the taping |
| Beer-Chant Group | (32, 0) | 96x48 | "pět… pět… pět…" chant cluster |
| Heckler (walk of shame) | (128, 0) | 32x48 | Czech-parody heckle bark |
| Golden-Hour Poser | (160, 0) | 32x48 | Sunset selfie pose |
| Crowd Dense (background) | (0, 48) | 512x64 | Simplified distance sprites |

### Inflatable Palm Trees:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Palm (15° list, variant A) | (0, 0) | 128x128 | Under-inflated |
| Palm (15° list, variant B) | (128, 0) | 128x128 | Under-inflated, mirrored |
| Idle Sway Animation | (0, 128) | 256x128 | 4 frames |

### Riverbank Port-O-Potty Monuments:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Monument, Upright, Clean | (0, 0) | 96x128 | Fresh placement |
| Monument, With Laundry (Day 6+) | (96, 0) | 96x128 | Post-completion easter egg state |
| Monument, Vendor Adjacent | (192, 0) | 128x128 | With small stall set up beside it |

---

## 🏗️ Sprite Sheet 8: Environmental Props & Effects
**Files:** `space_heaters.png`, `lifeguard_tower.png`, `no_diving_sign.png`, `release_forms_and_clipboard.png`, `prize_pallet_2003.png`, `heat_shimmer.png`, `confetti_and_string_lights.png`, `port_o_cologne_flies.png`

### File Dimensions:
| File | Dimensions |
|------|------------|
| space_heaters.png | 128x128 |
| lifeguard_tower.png | 192x320 |
| no_diving_sign.png | 96x128 |
| release_forms_and_clipboard.png | 256x192 |
| prize_pallet_2003.png | 192x128 |
| heat_shimmer.png | 128x128 |
| confetti_and_string_lights.png | 256x128 |
| port_o_cologne_flies.png | 96x96 |

### Space Heaters (`space_heaters.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Heater, Idle | (0, 0) | 64x64 | Off-season standby state |
| Heater, Full Blast (glow) | (64, 0) | 64x64 | Orange-coil July setting, ties to Space Heater Orange #FF7F32 |

### Lifeguard Tower (`lifeguard_tower.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Tower Structure, Interactive Foreground | (0, 0) | 128x256 | Full-detail object, distinct from the background placement baked into Sprite Sheet 1's tileset |
| Standa, Perched (reading) | (128, 0) | 64x64 | Composited at the platform mark |
| Standa, Whistle-Blow Overlay | (128, 64) | 64x64 | Reaction state, plays on any witnessed catapult launch |

### No Diving Sign (`no_diving_sign.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Sign Post + Board | (0, 0) | 64x96 | "NO DIVING (SERIOUSLY, IT'S 40cm)" hand-lettered board |
| Zip-Tie Detail (examine close-up) | (64, 0) | 32x32 | Readable-on-approach detail |

### Release Forms & Clipboard (`release_forms_and_clipboard.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Clipboard, Idle | (0, 0) | 96x96 | Coiled-cord pen attached |
| Release Forms, Fanned (x3) | (96, 0) | 128x96 | Four-page Czech-parody legalese, fanned for sign-up |
| Clipboard Tick, Close-Up | (224, 0) | 32x32 | Precise checkmark detail |

### Prize Pallet 2003 (`prize_pallet_2003.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Pallet, Shrink-Wrapped | (0, 0) | 96x128 | Sealed state, background dressing at `catapult_row` |
| Pallet, Half-Opened | (96, 0) | 96x128 | Badges, steins, Hamagotchis visible in bulk — never pointed at |

### Heat Shimmer (`heat_shimmer.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Shimmer Overlay, 4-Frame Loop | (0, 0) | 128x128 | Midday sand heat distortion, referenced from Sprite Sheet 1 |

### Confetti & String Lights (`confetti_and_string_lights.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Confetti Burst, 4 Frames | (0, 0) | 128x64 | Post-WIN prize podium celebration |
| String Light Strand (day, inactive) | (128, 0) | 64x64 | `night_party_zone` dressing, daytime state |
| String Light Strand (night, amber glow) | (128, 64) | 64x64 | `night_party_zone` dressing, ties to Night String-Light Amber #FFC966 |

### Port-O-Cologne Flies (`port_o_cologne_flies.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Fly Swarm, 4-Frame Ambient Loop | (0, 0) | 64x64 | Trails any party member with `port_o_cologne` active |
| Fly Swarm, Dissipate | (64, 0) | 32x32 | Plays once on cure (Zdenka's riverbank shower) |

### Technical Notes:
- Splash-impact particles remain owned by Sprite Sheet 3 (`catapult_rig_and_toilets.png`) and its `launch_splash_and_arc.png` overlay; this sheet covers ambient and prop-level effects only, not the launch sequence itself
- Lifeguard tower's foreground interactive object is intentionally separate from the background tower tile in Sprite Sheet 1 (parallax layering, not a duplicate asset)

---

## 🎮 Sprite Sheet 9: Quest UI
**Files:** `strike_counter_and_timer.png`, `suspicion_meter_oakleys.png`, `dialogue_and_prompt_ui.png`

### File Dimensions:
| File | Dimensions |
|------|------------|
| strike_counter_and_timer.png | 256x128 |
| suspicion_meter_oakleys.png | 192x64 |
| dialogue_and_prompt_ui.png | 384x256 |

### Strike Counter & Timer (`strike_counter_and_timer.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Strike Icon, Unfilled (x3) | (0, 0) | 32x32 | Selected bro's counter only — non-selected bros have no on-screen strike UI per quest doc |
| Strike Icon, Filled | (32, 0) | 32x32 | Struck state |
| Timer Ring, Full | (64, 0) | 64x64 | 12-second countdown start |
| Timer Ring, Depleting (8 frames) | (128, 0) | 64x64 | Countdown animation |
| Timer Ring, Timeout Flash | (192, 0) | 64x64 | Fires a strike on timeout |

### Suspicion Meter — Oakleys (`suspicion_meter_oakleys.png`) — Path B (Chadwick) only:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Oakleys, Baseline | (0, 0) | 48x32 | No suspicion — worn normally |
| Oakleys, Tick 1 (tilted 1/4 inch) | (48, 0) | 48x32 | First GO LIVE activation |
| Oakleys, Tick 2 (lowered to nose-tip) | (96, 0) | 48x32 | Second GO LIVE activation |
| Oakleys, Tick 3 (removed, set on podium) | (144, 0) | 48x32 | Third activation — fires immediate disqualification |

### Dialogue & Prompt UI (`dialogue_and_prompt_ui.png`):
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Dialogue Box | (0, 0) | 256x96 | Shared speech-bubble frame, all NPCs |
| Answer Option Prompt (x4) | (0, 96) | 256x64 | Trivia gauntlet selectable-answer buttons; the bro's confidently-wrong shout is always one of the four |
| GO LIVE Button (Path B) | (256, 96) | 96x64 | ICQ overlay trigger, Chadwick exclusive, disabled via animated unplug in Phase 2 |
| Czech-Parody Question Box | (0, 160) | 256x64 | Diacritic-safe (ě š č ř ž ý á í é ů), no translation toggle |

### Technical Notes:
- No numeric counter, no bar fill, and no tooltip on the Suspicion Meter — the four Oakleys states are the entire UI, per NPC profile spec
- GO LIVE button needs a disabled/unplugged-cord overlay frame for its Phase 2 lockout, animated rather than grayed out
- Diacritic glyph coverage must be verified in the UI font before content lock — a missing glyph turns the Czech-parody joke into a bug report

---

## 🎬 Animation Specifications

### Catapult Launch Sequence:
- **Duration:** ~3 seconds total (wind-up + release + arc + splash)
- **Frames:** 16 total across sub-phases
- **Loop:** No (one-shot per trigger)
- **Timing:** Wind-up 0.5s → release 0.5s → arc 1.5s → splash impact 0.5s
- **Critical constraint:** three units must be independently triggerable for staggered fire (Launch One ~Q4, Launch Two mid-syllable ~Q7)

### Splash Impact:
- **Duration:** 0.5 seconds
- **Frames:** 4
- **Loop:** No
- **Timing:** Synced to *THUNK-hisssss-splash* audio cue

### Jaxson's Triple-Sip:
- **Duration:** ~2 seconds (6 frames @ 4fps = 1.5s, plus a 0.5s hold on the final frame for the camera-aware finish)
- **Frames:** 6 (2 per can — reach, sip — rehearsed and visibly practiced motion)
- **Loop:** No, plays as a "beat" filler on correct-answer resolution
- **Timing:** 4fps base cadence, simultaneous three-can motion

### Janek's Buzzer-Wave:
- **Duration:** Exactly 1.5 seconds (rig constraint, tied to gameplay win window)
- **Frames:** 4
- **Loop:** No
- **Timing:** Must sync to oar catch-and-release audio cue ramping 2s before the turn

### Hamstradamus Speedo Strut:
- **Duration:** ~2.5 seconds
- **Frames:** 4
- **Loop:** No
- **Timing:** Full-length card-table traverse in profile

---

## 📱 Mobile Optimization

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| Bohemian Riviera Environment Atlas | fauxst_beach_tileset, bar_strip_facades, catapult_rig_and_toilets | 2048x2048 |
| Bohemian Riviera NPC Atlas | jaxson_vane, janek_sykora, petra, hamstradamus_beach_variant, rosta, standa, zdenka | 2048x2048 |
| Bohemian Riviera Effects Atlas | launch_splash_and_arc, heat_shimmer, confetti_and_string_lights, port_o_cologne_flies | 1024x1024 |
| Bohemian Riviera Props Atlas | space_heaters, lifeguard_tower, no_diving_sign, release_forms_and_clipboard, prize_pallet_2003 | 1024x1024 |
| Bohemian Riviera UI Atlas | strike_counter_and_timer, suspicion_meter_oakleys, dialogue_and_prompt_ui | 1024x1024 |

### Performance Notes:
- Vacationer crowd rendered as simplified distance sprites beyond `bar_strip` mid-ground; full detail only on close approach
- Bar TV loop is one shared low-res asset instanced across all three venues, not rendered per-venue
- Catapult launch sequence is pre-rendered per unit rather than computed per-frame, to keep the staggered three-unit trigger cheap
- Night-party string lights use a single ambient glow shader rather than per-bulb sprites

---

## 📋 Required PNG Files (29 Total)

| # | Filename | Dimensions |
|---|----------|------------|
| 1 | fauxst_beach_tileset.png | 1024x512 |
| 2 | bar_strip_facades.png | 1024x384 |
| 3 | catapult_rig_and_toilets.png | 1024x512 |
| 4 | signup_table_setup.png | 512x384 |
| 5 | prize_podium_and_banner.png | 512x384 |
| 6 | night_party_zone_dressing.png | 512x256 |
| 7 | river_parallax_background.png | 1024x512 |
| 8 | jaxson_vane.png | 384x288 |
| 9 | janek_sykora.png | 384x288 |
| 10 | petra_production_assistant.png | 384x288 |
| 11 | hamstradamus_beach_variant.png | 384x288 |
| 12 | rosta_retrieval_man.png | 256x192 |
| 13 | standa_lifeguard.png | 256x192 |
| 14 | zdenka_shower_vendor.png | 256x192 |
| 15 | vacationer_crowd.png | 512x384 |
| 16 | inflatable_palm_trees.png | 256x256 |
| 17 | riverbank_portapotty_monuments.png | 256x256 |
| 18 | launch_splash_and_arc.png | 512x256 |
| 19 | space_heaters.png | 128x128 |
| 20 | lifeguard_tower.png | 192x320 |
| 21 | no_diving_sign.png | 96x128 |
| 22 | release_forms_and_clipboard.png | 256x192 |
| 23 | prize_pallet_2003.png | 192x128 |
| 24 | heat_shimmer.png | 128x128 |
| 25 | confetti_and_string_lights.png | 256x128 |
| 26 | port_o_cologne_flies.png | 96x96 |
| 27 | strike_counter_and_timer.png | 256x128 |
| 28 | suspicion_meter_oakleys.png | 192x64 |
| 29 | dialogue_and_prompt_ui.png | 384x256 |

**Total Estimated Memory:** ~70MB

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

**The Bohemian Riviera delivers a complete landlocked beach-resort art spec — trucked-in sand, three independently-triggerable catapult units, a boat-hook retrieval man with a personal-best chart, and a hamster who has never once been wrong about anything.**
