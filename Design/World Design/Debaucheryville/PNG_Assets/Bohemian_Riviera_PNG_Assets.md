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
| Lifeguard Tower Base | (256, 256) | 192x256 | Structural tower, spans into Sheet 4 |
| Riverbank Edge | (448, 256) | 320x128 | Sand-to-water transition |
| No Diving Sign Post | (768, 128) | 96x128 | Zip-tied hand-lettered sign |

### Technical Notes:
- Sand tile needs a subtle heat-shimmer overlay hook (see Sprite Sheet 12) at midday
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
| Launch Animation — Splash Impact | (384, 256) | 256x128 | 4 frames, ties to Sprite Sheet 12 |
| Hazard Tape / Off-Season Dressing | (0, 384) | 256x64 | Roped-off state between tapings |
| Prize Pallet (2003, background) | (256, 384) | 192x128 | Half-opened, visible not pointed at |

### Technical Notes:
- **Three independently-triggerable launch units required** — build as separate triggerable animation instances, not a single combined three-unit sequence, so Launch One (Q4 interruption) and Launch Two (Q7 mid-syllable) can fire on independent timers
- Broken center-unit door-swing needs its own idle-open state, reusable outside the launch sequence
- Arc must visibly clear inflatable palms and lifeguard tower before water contact (see Sprite Sheet 1 & 4 for silhouette reference)

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
| Triple-Can Sip | (64, 0) | 192x96 | Rehearsed simultaneous sip, 3 frames |
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
- **Duration:** ~2 seconds
- **Frames:** 3 (rehearsed, visibly practiced motion)
- **Loop:** No, plays as a "beat" filler on correct-answer resolution
- **Timing:** 8fps, simultaneous three-can motion

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

### Performance Notes:
- Vacationer crowd rendered as simplified distance sprites beyond `bar_strip` mid-ground; full detail only on close approach
- Bar TV loop is one shared low-res asset instanced across all three venues, not rendered per-venue
- Catapult launch sequence is pre-rendered per unit rather than computed per-frame, to keep the staggered three-unit trigger cheap
- Night-party string lights use a single ambient glow shader rather than per-bulb sprites

---

## 📋 Required PNG Files (18 Total)

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

**Total Estimated Memory:** ~60MB

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
