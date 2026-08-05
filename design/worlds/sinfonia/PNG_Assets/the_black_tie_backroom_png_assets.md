# The Black-Tie Backroom - Complete PNG Asset Requirements

*Artist Reference Document for Sinfonia's Hidden Gambling Den*

## 📋 Overview
The Black-Tie Backroom (Der Schwarze Krawatte Hinterzimmer) is where Sinfonia's fortunes go to die in style — an exclusive underground gambling den hidden thirty steps behind the Bassline Opera House's prop corridor, where the chips are actual silver, the servers dress better than the guests, and the house always wins and is very polite about it. This document specifies all 38 PNGs for the location's environment, characters, and UI/items.

**Location ID:** `sinfonia_operahouse_blacktie_backroom_01`
**Theme:** Respectable gambling hypocrisy — addiction dressed in elegance, satirizing European private gaming clubs and old imperial gambling-salon traditions
**Zone:** Hidden behind the Bassline Opera House (Imperial Square District underside)
**Hours:** 21:00–05:00 (entry gated by attire, stats, and 500 Sovs collateral)
**Primary Function:** Mini-game hub (poker, roulette, blackjack) / hidden boss arena (Herr Falsch) / reputation gate (High Roller salon) / scripted encounter (`blacktie_event_kings_were_humming_01` at Aaron's corner table)

**Priority**: HIGH (Mini-Game Hub, Hidden Boss Arena, Reputation Gate, Scripted Encounter)
**Total PNGs Required**: 38 (13 environment, 11 character, 14 UI/item)
**Performance**: Target 60 FPS on min-spec hardware, max 20 draw calls, 50MB memory

**Source of truth**: `Design/World Design/Sinfonia/the_black_tie_backroom.md` (PNG Asset Requirements Summary). Every filename below appears in that summary; every filename referenced by `sprite_mapping/the_black_tie_backroom_sprite_mapping.json` appears below.

---

## 🎨 Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Velvet Burgundy | #722F37 | Drapery, seating, wall panels |
| Gold Leaf | #FFD700 | Trim, chandeliers, frames, chip accents |
| Midnight Blue | #191970 | Background depth, shadowed edges |
| Vice Black | #0D0D0D | Corners, the staircase's upper dark, vignetting |
| Table Green | #0B3D2E | Standard house felt (playable tables ONLY) |
| Corner Oxblood | #4A1F24 | Aaron's corner table felt (never used on playable tables) |

### Two-Felt Rule (BINDING)
Every playable gaming surface — poker, roulette, blackjack, high-stakes salon, private boxes — uses **Table Green (#0B3D2E)** with the full house dressing: brass chip rail, dealer plaque, printed bet-placement markings, shared overhead table light.

**Aaron's corner table uses Corner Oxblood (#4A1F24) and carries none of that dressing.** No rail, no plaque, no markings, its own low pendant lamp. A player must be able to tell the two apart in a single glance, at thumbnail size. This is a hard requirement, not a style preference.

---

## 📁 File Structure
```
assets/sprites/locations/sinfonia/the_black_tie_backroom/
├── environment/
│   ├── hidden_entrance.png
│   ├── staircase_transition.png
│   ├── foyer_verification.png
│   ├── main_floor.png
│   ├── aarons_corner_table.png
│   ├── high_stakes_salon.png
│   ├── private_box.png
│   ├── vault_antechamber.png
│   ├── poker_table.png
│   ├── roulette_table.png
│   ├── blackjack_table.png
│   ├── bar_area.png
│   └── chandelier_detail.png
├── npcs/
│   ├── anton_doorman.png
│   ├── madame_karten.png
│   ├── herr_falsch.png
│   ├── nervous_noble.png
│   ├── silent_countess.png
│   ├── house_dealer.png
│   ├── siegfried_coatcheck.png
│   ├── high_roller_npc.png
│   ├── server_tray.png
│   ├── bouncer_escort.png
│   └── aaron_the_unflappable.png
└── ui/
    ├── chip_stack.png
    ├── card_deck.png
    ├── roulette_wheel.png
    ├── bet_interface.png
    ├── house_edge_meter.png
    ├── high_roller_badge.png
    ├── shark_fin.png
    ├── marked_cards.png
    ├── collateral_receipt.png
    ├── members_card.png
    ├── tell_indicator.png
    ├── cleaned_out_stamp.png
    ├── candy_smokes_carton.png
    └── tractor_nft_token.png
```

---

# PART 1 — ENVIRONMENT ART (13 PNGs)

## 🚪 Sprite Sheet 1: Hidden Entrance
**Filename**: `hidden_entrance.png`
**Dimensions**: 256 × 384

Three horizontal states across the sheet:
1. **Closed**: Unremarkable door in the opera house backstage, "Private — Staff Only" plate, scuffed paint, easily missed
2. **Ajar**: Warm sliver of light at the seam, hinting at somewhere that does not belong behind a prop corridor
3. **Open**: Full reveal of the passage mouth beyond

*Art Note*: The door must look boring. Its only tell is that it is slightly too clean around the handle.

---

## 🪜 Sprite Sheet 2: Staircase Transition
**Filename**: `staircase_transition.png`
**Dimensions**: 256 × 512

A single vertical piece reading top-to-bottom as a class transition in thirty steps: dusty boards and bare bulb at the top, marble treads mid-way, brass railings and gas-lamp-style sconces at the bottom. Carpet appears one third of the way down and thickens.

*Art Note*: Light temperature shifts with the material — cold and grey at the top, gold and heavy at the bottom.

---

## 🪞 Sprite Sheet 3: Foyer / Verification Zone
**Filename**: `foyer_verification.png`
**Dimensions**: 384 × 256

Small antechamber. Full-length mirror (attire check and surveillance both), brass gold-deposit window with a small scale and receipt spike, and the House Rules posted in elegant calligraphy on a stand. Doorman's position marked at frame left.

*Art Note*: The calligraphy must be legible at 2× zoom — the three House Rules are readable content in-world.

---

## 🎰 Sprite Sheet 4: Main Floor
**Filename**: `main_floor.png`
**Dimensions**: 640 × 512

The primary gaming room. Open floor with the standard house tables (poker, roulette, blackjack) in Table Green with full dressing, bar running along one wall, crystal chandeliers, velvet everything, gold leaf details. Corner recess at frame right reserved for the corner-table zone (see next sheet) — the base plate leaves that recess empty so the zone can be composited over it.

*Art Note*: Sightlines matter. The corner recess must be visible from the room's entry point without the player having to hunt for it.

---

## 🕯️ Sprite Sheet 5: Aaron's Corner Table
**Filename**: `aarons_corner_table.png`
**Dimensions**: 320 × 256

The named main-floor zone `aarons_corner_table`, composited into the main floor's corner recess.

**Three states across the sheet:**
1. **Ambient (pre-scene)**: Corner Oxblood felt, low pendant lamp with a warm tight pool of light, one crystal tumbler with a pale drink, a worn candy-cigarette carton at the table edge, a small ring of chalky white dust on the felt. Two spare chairs. No chip rail, no dealer plaque, no bet markings
2. **Scene-lit (during `blacktie_event_kings_were_humming_01`)**: Pendant lamp intensity up, room behind the table falls a stop darker, three additional chairs occupied, chips pushed to centre
3. **Ambient (post-scene)**: As state 1, with a taller chip stack and the chalk ring larger

*Art Note (BINDING)*: This table must never be mistakable for a playable table. Different felt, different lamp, no house furniture. If an artist's pass makes it look like the room's other tables, the pass is wrong.

---

## 🥂 Sprite Sheet 6: High Stakes Salon
**Filename**: `high_stakes_salon.png`
**Dimensions**: 512 × 384

Separated from the main floor by a velvet rope on brass stanchions. Fewer tables, larger spacing, personal servers stationed at the walls, better upholstery. Table Green with full dressing throughout. Selfie-spot framing marked at the centre table (chip stack + chandelier above).

---

## 🔒 Sprite Sheet 7: Private Box
**Filename**: `private_box.png`
**Dimensions**: 256 × 256

A single discreet room: one table, four chairs, heavy door, no windows, one lamp. Deliberately under-decorated compared to the floor — this room is for business.

---

## 🗝️ Sprite Sheet 8: Vault Antechamber
**Filename**: `vault_antechamber.png`
**Dimensions**: 384 × 384

Post-boss area behind a keyed door. Cold stone under gold trim, storage racks, and the Baroness' personal vault door dominating the far wall. Two states: **locked** (keyhole plate dark) and **unlocked** (plate lit, door ajar).

---

## 🃏 Sprite Sheet 9: Poker Table
**Filename**: `poker_table.png`
**Dimensions**: 384 × 256

Playable poker interface plate. Table Green felt, brass chip rail, dealer plaque, printed betting positions for up to six seats, card landing zones marked.

---

## 🎡 Sprite Sheet 10: Roulette Table
**Filename**: `roulette_table.png`
**Dimensions**: 384 × 384

Playable roulette layout for the **Sinfonian Wheel** — single-zero European style. Numbered grid, outside bets, and the marked "Composer's Dozen" special-bet block. Wheel well at the head of the table (wheel itself is a separate UI sheet).

---

## ♠️ Sprite Sheet 11: Blackjack Table
**Filename**: `blackjack_table.png`
**Dimensions**: 384 × 256

Playable **Twenty-One Sinfonian** layout. Seven seat positions, insurance line, "Dealer stands on 17" printed in period lettering along the arc.

---

## 🍾 Sprite Sheet 12: Bar Area
**Filename**: `bar_area.png`
**Dimensions**: 256 × 192

Long bar along the main floor wall. Backlit bottle shelving, crystal glassware, a discreet tally book at the server's end. Small "complimentary" card in a brass stand.

---

## 💎 Sprite Sheet 13: Chandelier Detail
**Filename**: `chandelier_detail.png`
**Dimensions**: 192 × 192

Hero decorative element, reused across zones at varying scales. Crystal drops, gold armature, subtle glint frames for the sparkle particle effect.

---

# PART 2 — CHARACTER SPRITES (11 PNGs)

*Cell sizes below are as registered in the location file's asset summary. Sheet dimensions are the full multi-row sheets.*

## 🧤 Sprite Sheet 14: Anton the Doorman
**Filename**: `anton_doorman.png`
**Cell Size**: 96 × 128 | **Sheet**: 384 × 512 (4 columns × 4 rows)
**NPC ID**: `sinfonia_npc_anton_doorman_01`

- **Look**: Built like a bouncer, dressed like a butler. Tailcoat cut a size too small across the shoulders on purpose. White gloves. Immaculate.
- **Animations**: Row 0 `idle_stance` (2f, 1 fps) · Row 1 `assess_attire` (4f, 3 fps — head-to-toe look, unhurried) · Row 2 `accept_collateral` (3f, 3 fps — gloved hand extended, receipt returned) · Row 3 `refuse_entry` (3f, 3 fps — half-step sideways, arm across the doorway)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/anton_the_doorman.md`

---

## 👁️ Sprite Sheet 15: Madame Karten
**Filename**: `madame_karten.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 384 (4 columns × 4 rows)
**NPC ID**: `sinfonia_npc_madame_karten_01`

- **Look**: Elegant older woman, floor-length dark gown, pearls, hair up. Eyes that track the room, not the player.
- **Animations**: Row 0 `idle_survey` (4f, 2 fps — slow scan of the floor) · Row 1 `approach_warm` (4f, 4 fps) · Row 2 `offer_drink` (3f, 3 fps) · Row 3 `catch_cheater` (4f, 4 fps — the scan stops, no other movement)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/madame_karten.md`

---

## 🦈 Sprite Sheet 16: Herr Falsch
**Filename**: `herr_falsch.png`
**Cell Size**: 128 × 192 (boss scale) | **Sheet**: 512 × 960 (4 columns × 5 rows)
**NPC ID**: `sinfonia_npc_herr_falsch_01`

- **Look**: Tuxedo too perfect to be comfortable. Card-motif studs and cufflinks. A smile held slightly too long.
- **Animations**: Row 0 `idle_dealing` (4f, 3 fps) · Row 1 `full_house_summon` (6f, 5 fps — card constructs rise from the felt) · Row 2 `dead_mans_hand` (4f, 5 fps — targeted flick) · Row 3 `the_river` (4f, 4 fps — arena tiles flip) · Row 4 `sleeve_ace_interrupt` (4f, 6 fps) + `exposed` variant frames (cheating revealed: sleeve cards visible, posture drops)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/herr_falsch.md`

---

## 😰 Sprite Sheet 17: Graf von Zittrig (The Nervous Noble)
**Filename**: `nervous_noble.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 288 (4 columns × 3 rows)
**NPC ID**: `sinfonia_npc_graf_von_zittrig_01`

- **Look**: Expensive clothes visibly damp at the collar. Handkerchief. Cufflinks that catch the light.
- **Animations**: Row 0 `idle_composed` (2f, 1 fps — trying) · Row 1 `cufflink_adjust` (3f, 4 fps — **the tell**, must be readable at a glance) · Row 2 `fold_relief` (3f, 3 fps)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/graf_von_zittrig.md`

---

## 🤫 Sprite Sheet 18: Gräfin Stille (The Silent Countess)
**Filename**: `silent_countess.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 288 (4 columns × 3 rows)
**NPC ID**: `sinfonia_npc_grafin_stille_01`

- **Look**: Immaculate, still, champagne flute always within reach. Expression never changes across any frame in the sheet.
- **Animations**: Row 0 `idle_motionless` (2f, 1 fps — blink only) · Row 1 `champagne_sip` (3f, 2 fps — **the tell**) · Row 2 `push_chips` (3f, 3 fps — the only way she speaks)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/grafin_stille.md`

---

## 🎴 Sprite Sheet 19: House Dealer
**Filename**: `house_dealer.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 384 (4 columns × 4 rows)

Rotating generic house dealer — **three palette variants** on the same skeleton (waistcoat colour + hair) so the roster can rotate without new sheets.

- **Animations**: Row 0 `idle` (2f, 1 fps) · Row 1 `deal_cards` (4f, 6 fps) · Row 2 `spin_wheel` (4f, 6 fps) · Row 3 `sweep_pot` (4f, 5 fps)

---

## 🧥 Sprite Sheet 20: Siegfried (Coat Check)
**Filename**: `siegfried_coatcheck.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 384 (4 columns × 4 rows)
**NPC ID**: `sinfonia_npc_siegfried_coatcheck_01`

- **Look**: Club waistcoat, sleeves rolled, coat-check counter. A second, plainer variant row for his apartment above the club (no waistcoat, iron in hand).
- **Animations**: Row 0 `idle_counter` (2f, 1 fps) · Row 1 `take_coat` (3f, 3 fps) · Row 2 `accept_tip` (3f, 3 fps) · Row 3 `apartment_ironing` (4f, 2 fps)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/siegfried_coat_check.md`

---

## 💰 Sprite Sheet 21: High Roller (Background Elite)
**Filename**: `high_roller_npc.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 384 (4 columns × 4 rows)

Ambient crowd filler for the salon and floor. **Four palette/silhouette variants** (two gowns, two dinner suits) so a crowd can be built from one sheet.

- **Animations**: Row 0 `idle_standing` (2f, 1 fps) · Row 1 `idle_seated` (2f, 1 fps) · Row 2 `celebrate_small` (3f, 3 fps) · Row 3 `deflate` (3f, 2 fps)

---

## 🍷 Sprite Sheet 22: Server with Tray
**Filename**: `server_tray.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 288 (4 columns × 3 rows)

- **Look**: Better suit than most of the guests. Tray of "complimentary" drinks never empty.
- **Animations**: Row 0 `walk_tray` (4f, 4 fps) · Row 1 `offer_drink` (3f, 3 fps) · Row 2 `observe` (2f, 1 fps — pause at the table's shoulder)

---

## 💪 Sprite Sheet 23: Bouncer Escort
**Filename**: `bouncer_escort.png`
**Cell Size**: 96 × 128 | **Sheet**: 384 × 384 (4 columns × 3 rows)

Cheat-consequence encounter sprite. Same tailoring language as Anton, none of the polish.

- **Animations**: Row 0 `idle_menace` (2f, 1 fps) · Row 1 `grab` (4f, 6 fps) · Row 2 `eject` (4f, 5 fps — toward the stairs, off-frame)

---

## 🍸 Sprite Sheet 24: Aaron the Unflappable
**Filename**: `aaron_the_unflappable.png`
**Cell Size**: 96 × 128 | **Sheet**: 384 × 1024 (4 columns × 8 rows)
**NPC ID**: `sinfonia_npc_aaron_unflappable_01`
**Zone**: `aarons_corner_table` (resident, all hours)

### Visual Design
- **Jacket**: Velvet dinner jacket, slightly rumpled — the rumple is deliberate and consistent across every frame, never "fixed" in any pose
- **Drink**: Double White Russian in a crystal tumbler — pale, layered, condensation on the glass. The tumbler is present in every row; it is never absent from the sheet
- **Candy cigarette**: A chalk-white candy stick. **Required prop states**: full length, half length (post-crunch), and a worn carton on the table with a soft-creased lid
- **Chalk residue**: A faint white dust ring on the oxblood felt beside the tumbler, and a faint white trace at the fingertips. Present from the first frame

### Animations (8 rows)
| Row | Name | Frames | FPS | Loop | Contents |
|-----|------|--------|-----|------|----------|
| 0 | `idle_seated` | 4 | 2 | yes | Seated, tumbler in hand, candy stick resting between the fingers of the other hand |
| 1 | `stir_drink` | 4 | 3 | no | Candy stick lowered into the tumbler, two slow turns, lifted out wet at the tip |
| 2 | `dramatic_drag` | 3 | 2 | no | Candy stick to the lips, held, lowered; head tilts back a few degrees on the hold |
| 3 | `crunch` | 3 | 4 | no | Bite. Frame 1 contact, frame 2 the break (small chalk-dust puff, two crumbs falling), frame 3 the shortened stick lowered. **The signature frame of the sheet — the break must read clearly at 1× scale** |
| 4 | `fresh_from_carton` | 4 | 3 | no | Reaches to the worn carton, draws a fresh full-length stick, sets the carton back without looking at it |
| 5 | `lay_cards_down` | 4 | 3 | no | Two cards turned face-up onto the oxblood felt, hand withdrawn |
| 6 | `offer_carton` | 3 | 3 | no | Carton extended toward frame left, open end forward |
| 7 | `rake_chips` | 4 | 3 | yes | Both forearms sweep the pot in; used as background ambient after the scene |

### Technical Notes
- Rows 1–4 are the ritual cycle and are sequenced as one ambient chain (`stir_drink` → `dramatic_drag` → `crunch` → `fresh_from_carton`) on a long random interval when idle
- Row 3's chalk-dust puff uses the shared `chalk_puff` particle from the UI/item chalk assets — do not bake particles into the sprite
- Sheet is referenced by `sprite_mapping/the_black_tie_backroom_sprite_mapping.json` under `npc_aaron_unflappable`, and by his profile at `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/aaron_the_unflappable.md`. **Filename is canonical — both documents use `aaron_the_unflappable.png` exactly**
- Everything beyond appearance and frame content — voice, manner, dialogue, ambient lines — is owned by the profile file and is not restated here

---

# PART 3 — UI / ITEM SPRITES (14 PNGs)

## 🪙 Sprite Sheet 25: Chip Stack
**Filename**: `chip_stack.png` · **Dimensions**: 64 × 64
Silver house chips in stacked heights (1, 5, 10, 20+). Actual silver sheen, milled edges, house crest struck on the face. Four height variants across the sheet for the currency display.

## 🃏 Sprite Sheet 26: Card Deck
**Filename**: `card_deck.png` · **Dimensions**: 48 × 64
Deck back (house crest), deck side profile, and a 3-frame deal animation strip (top card lifting, in flight, landed).

## 🎯 Sprite Sheet 27: Roulette Wheel
**Filename**: `roulette_wheel.png` · **Dimensions**: 192 × 192
Single-zero Sinfonian Wheel head. 8-frame spin cycle (blur-tiered: crisp → light blur → heavy blur → light blur), plus a settled state with the ball in a pocket.

## 🖥️ Sprite Sheet 28: Bet Interface
**Filename**: `bet_interface.png` · **Dimensions**: 256 × 128
Placement UI frame in burgundy and gold: chip-denomination selector, confirm/clear, and the bet-total readout plate.
*Binding note*: This asset is used **only** at the room's playable tables. It has no state, variant, or anchor at `aarons_corner_table`.

## 📊 Sprite Sheet 29: House Edge Meter
**Filename**: `house_edge_meter.png` · **Dimensions**: 128 × 32
Thin horizontal bar with a gold fill and a small engraved plate. Debug/informational visualization of the hidden math; shown only where design calls for it.

## 🎖️ Sprite Sheet 30: High Roller Badge
**Filename**: `high_roller_badge.png` · **Dimensions**: 48 × 48
Status indicator. Gold-rimmed enamel disc, velvet-rope motif. Locked (grey) and earned (gold) states.

## 🦈 Sprite Sheet 31: Shark Fin
**Filename**: `shark_fin.png` · **Dimensions**: 32 × 48
`item_shark_fin` — Herr Falsch victory accessory. Lapel-pin scale, brushed silver dorsal fin on a card-suit backing plate. Inventory icon plus equipped overlay.
*Item file*: `Design/Inventory/items/shark_fin_item.md`

## 🔍 Sprite Sheet 32: Marked Cards
**Filename**: `marked_cards.png` · **Dimensions**: 48 × 64
Cheat item. Two states: **normal view** (identical to a standard deck back) and **marked view** (faint scratch pattern in the corner ornament, visible only in the cheat overlay).

## 🧾 Sprite Sheet 33: Collateral Receipt
**Filename**: `collateral_receipt.png` · **Dimensions**: 48 × 32
The 500 Sovs door deposit slip. Thin card stock, house crest, hand-inked amount, spike hole at the top edge. States: **issued**, **redeemed**, **forfeit** (stamped through).

## 🖤 Sprite Sheet 34: Member's Card
**Filename**: `members_card.png` · **Dimensions**: 48 × 32
`item_members_card` — Backroom access alternative. Black card, gold engraving, no name printed on it.
*Item file*: `Design/Inventory/items/members_card_item.md`

## ❗ Sprite Sheet 35: Tell Indicator
**Filename**: `tell_indicator.png` · **Dimensions**: 32 × 32
Small diegetic-adjacent flourish shown above an NPC when a learned tell fires. Three intensity variants. Never appears at `aarons_corner_table`.

## 🛑 Sprite Sheet 36: Cleaned Out Stamp
**Filename**: `cleaned_out_stamp.png` · **Dimensions**: 64 × 64
Failure badge. Ink-stamp lettering across a receipt corner, slightly off-register.

## 🚬 Sprite Sheet 37: Candy Smokes Carton
**Filename**: `candy_smokes_carton.png` · **Dimensions**: 48 × 48
`item_candy_smokes` — Puff-Puff-Powder™ Chalk 'n' Ash Candy Smokes. Worn carton, soft-creased lid, faded period-cartoon branding, corners furred from handling. **States**: closed carton (inventory icon), open carton with sticks visible, single stick full length, single stick post-bite.
Includes the shared **`chalk_puff`** particle strip (4 frames, 8 fps) and the **chalk ring** mouth overlay (2 variants) used by the item's use-effect.
*Item file*: `Design/Inventory/items/candy_smokes_item.md` · Scene-granted only, at `blacktie_event_kings_were_humming_01`

## 🚜 Sprite Sheet 38: Tractor NFT Token
**Filename**: `tractor_nft_token.png` · **Dimensions**: 32 × 32
`item_tractor_nft` — "She Thinks My Tractor's Sexy" (Mint #42). Scratched aluminium token, struck edge, "#42" stamped small. Face carries the low-res animated GIF loop: a zero-turn mower doing a donut on a manicured lawn, a tiny pixelated cowboy hat bouncing on the seat. **6-frame loop at 4 fps, deliberately low-fidelity** — the animation must look worse than the rest of the game's art, on purpose. Reverse face: a QR block.
*Item file*: `Design/Inventory/items/tractor_nft_item.md` · Scene-granted only, at `blacktie_event_kings_were_humming_01`

---

## 🎬 Animation Specifications

### General Animation Guidelines (all sheets)
- **Idle Loops**: 2–4 frames, 1–2 FPS
- **Tells**: 3 frames, 2–4 FPS — must read at a glance without a UI prompt
- **Action Animations**: 3–6 frames, 3–6 FPS
- **Boss Attacks**: 4–6 frames, 4–6 FPS

### Aaron's Ritual Chain (`stir_drink` → `dramatic_drag` → `crunch` → `fresh_from_carton`):
- **Duration:** ~1.3s + 1.5s + 0.75s + 1.3s ≈ 4.9 seconds per full chain
- **Frames:** 4 / 3 / 3 / 4
- **Pattern:** Sequenced as one ambient chain on a long random interval when idle; returns to `idle_seated`
- **Trigger:** Timer while resident at the corner table (all hours)
- **Purpose:** Character-defining ritual — the calmest man in the building, running his own economy of chalk and cream
- **Audio Sync:** Glass clink on stir turn 2; dry crunch exactly on the row-3 break frame
- **Performance Optimization:** None needed (single resident NPC); chalk_puff particle capped at 1 instance

### Herr Falsch Boss Set (Full House / Dead Man's Hand / The River / Sleeve Ace):
- **Duration:** 1.2s / 0.8s / 1.0s / 0.67s respectively
- **Frames:** 6 / 4 / 4 / 4 (+ exposed variant frames)
- **Pattern:** Boss AI state machine; `sleeve_ace_interrupt` fires below 25% HP; exposed variant replaces idle once cheating is revealed
- **Trigger:** Hidden boss fight, private boxes
- **Purpose:** Card-shark menace with a tell of his own — the too-long smile drops when exposed
- **Audio Sync:** Card-snap on each attack's release frame; arena tile flips on The River carry a shuffled-deck riffle
- **Performance Optimization:** Card-construct summons capped at 3 concurrent on low-end

### NPC Tells (Cufflink Adjust / Champagne Sip):
- **Duration:** 0.75s / 1.5s
- **Frames:** 3 each
- **Pattern:** Single play at decision moments during poker hands
- **Trigger:** NPC hand-strength logic
- **Purpose:** Learnable, diegetic poker reads — the entire skill layer of poker_vs_npc
- **Audio Sync:** None (silence is the point); tell_indicator overlay fires only after the tell is learned
- **Performance Optimization:** None needed — tells must never be simplified away

### Roulette Wheel Spin:
- **Duration:** ~2 second spin (8 frames, blur-tiered), then settled state
- **Frames:** 8 + settled
- **Pattern:** Crisp → light blur → heavy blur → light blur → settle; pre-rendered cycle
- **Trigger:** Bet confirmation at the roulette table
- **Purpose:** The house's favorite theater — fair-looking, 5.3% edge
- **Audio Sync:** Ball rattle decelerating; final click on the settled frame
- **Performance Optimization:** Pre-rendered (per mobile targets); reduced to 4-frame spin on low-end

### House Dealer Loop (Deal / Spin / Sweep):
- **Duration:** 0.67s / 0.67s / 0.8s
- **Frames:** 4 / 4 / 4
- **Pattern:** Game-state driven, returns to idle
- **Trigger:** Minigame flow at playable tables
- **Purpose:** Frictionless, interchangeable house machinery (three palette variants, one skeleton)
- **Audio Sync:** Card slide per deal frame; chip cascade on sweep_pot
- **Performance Optimization:** Card deal animations pre-rendered per mobile targets

### Tractor NFT Token Loop:
- **Duration:** 1.5 second loop
- **Frames:** 6 at 4 fps
- **Pattern:** Continuous loop on the token face — deliberately low-fidelity; must look worse than the rest of the game's art, on purpose
- **Trigger:** Constant while inspected in inventory
- **Purpose:** The punchline is the production value
- **Audio Sync:** None
- **Performance Optimization:** None needed (it is already the optimization)

---

## ✨ Particle & Effect Requirements

| Effect | Source | Notes |
|--------|--------|-------|
| Cigar smoke wisps | Main floor, salon | Slow drift, low opacity, never obscures a table |
| Chip shine | `chip_stack.png` | Glint on stack changes |
| Card flutter | `card_deck.png` | Deal and sweep |
| Champagne bubbles | Bar, salon | Tied to `server_tray.png` and Gräfin Stille's tell |
| Chandelier sparkle | `chandelier_detail.png` | Rare, subtle |
| `chalk_puff` | Aaron row 3, candy-smokes use effect | **Shared** — one particle asset, two consumers |

---

## ♿ Accessibility Sprite Requirements

### High Contrast Alternatives:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Playable-table outline set | set at sheet layout | per table | High-contrast dressing (rail + plaque emphasized) reinforcing the Two-Felt Rule beyond hue |
| Aaron's corner table outline | set at sheet layout | 320×256 | Distinct dashed-pool outline — reads as "not a game" even in high-contrast mode |
| Hidden entrance discoverability variant | set at sheet layout | 256×384 | Boosted handle-clean tell for the too-easily-missed door |
| Velvet rope / salon gate marker | set at sheet layout | 64×96 | Enhanced-visibility gate for the High Roller threshold |

### Motion Sensitivity Options:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Roulette reduced spin | set at sheet layout | 192×192 | 4-frame low-blur spin + settled state, no heavy blur tier |
| Static chandelier | set at sheet layout | 192×192 | No sparkle glint frames |
| Smoke-free floor overlay | set at sheet layout | full room | Disables cigar-smoke drift |
| Tell indicator steady variant | set at sheet layout | 32×32 | Non-pulsing single-intensity version |

### Visual Audio Cues:
| Element | Position | Size | Description |
|---------|----------|------|-------------|
| Card-snap flash | set at sheet layout | 24×24 | Glyph on Herr Falsch attack release frames |
| Chip cascade marks | set at sheet layout | 32×16 | Falling-chip glyphs when the pot sweeps (win/loss audio) |
| Wheel-click marker | set at sheet layout | 16×16 | Tick glyph on the roulette settle click |
| Crunch burst | set at sheet layout | 16×16 | The chalk_puff itself doubles as the visual for Aaron's crunch audio |

### Colorblind Considerations:
- The Two-Felt Rule is not carried by hue alone: playable tables have rail/plaque/markings, Aaron's table has none — furniture is the redundant channel
- Tell indicator intensities differ by shape (one/two/three flourish marks), not color
- Collateral receipt states (issued/redeemed/forfeit) are stamp-based, readable in greyscale
- Touch zones minimum 44px for bet interface controls, table seats, and door interactions

---

## 🖥️ Performance & Assets

### Texture Compression:
- **Desktop:** S3TC/BPTC VRAM compression (Godot 4.4 import) main floor plate and Aaron's sheet need uncompressed — felt color fidelity is a binding requirement
- **Fallback:** PNG high quality for `aarons_corner_table.png` (the oxblood/green distinction must survive compression)

### Texture Atlases:
| Atlas | Contents | Max Size |
|-------|----------|----------|
| backroom_environment | entrance, staircase, foyer, floor plates, tables, bar, chandelier | 1024x1024 |
| backroom_characters_a | Anton, Madame Karten, dealers, Siegfried, high rollers, server, bouncer | 1024x1024 |
| backroom_characters_b | Herr Falsch (boss scale), Aaron the Unflappable | 1024x1024 |
| backroom_ui_items | all 14 UI/item sprites | 512x512 |

*(Maximum 4 atlases at 1024px per original spec; max atlas size 2048x2048 for broad GPU compatibility.)*

### LOD Levels:
| Level | Description |
|-------|-------------|
| High | Full smoke drift, chandelier sparkle, champagne bubbles, 8-frame wheel spin, full crowd variants |
| Medium | Reduced smoke, no sparkle, 4 crowd fillers, 8-frame wheel kept |
| Low | No ambient particles, static crowd fills (pre-rendered), 4-frame wheel spin |

### Performance Targets:
- **Target FPS:** 60 on min-spec hardware
- **Max Draw Calls:** Under 20 for the full location
- **Memory Footprint:** Under 50 MB with all zones loaded
- **Particle Limit:** 60 simultaneous
- **Pre-rendered:** Roulette spin cycle, card deal animations, static crowd fills

### Performance Notes:
- Zone loading enabled (foyer, main floor, salon, boxes, vault load independently)
- Aaron's corner table is a composite overlay on the main floor plate — one extra draw call, budgeted
- Scene-lit corner state is a lighting preset swap, not a second floor plate

---

## 🔧 Technical Integration Notes

### Godot Engine Integration:
- All sprites designed for Godot 4.x compatibility, top-left origin (0,0)
- AnimatedSprite2D for all NPC/boss states; CPUParticles2D (not GPU) for smoke, bubbles, chalk_puff
- Minigame tables run as scene sub-controllers; `bet_interface.png` instantiates only at playable tables (zone flag `betting_ui_enabled: false` at `aarons_corner_table` is authoritative)
- Location state machine: normal / high_roller / banned / cleaned_out / post_kings_were_humming / post_card_shark / vault_unlocked drives zone access and sprite state swaps
- Aaron's ritual chain runs on a long-interval random timer, sequenced rows 1→2→3→4

### Audio Sync Points:
| Visual Element | Audio Cue | Timing |
|----------------|-----------|--------|
| Aaron `crunch` row 3 | Dry candy-stick crunch | Exactly on frame 2 (the break) |
| Roulette wheel settle | Ball rattle → final click | Click on settled frame |
| Card deal strip | Card slide | Per deal frame |
| Pot sweep | Chip cascade | On sweep_pot frames 2–4 |
| Herr Falsch attacks | Card snap | On each release frame |
| Collateral deposit | Scale clink + receipt spike | On Anton `accept_collateral` frame 3 |

### Quest Integration:
| Quest | Sprite Elements Used | Integration Point |
|-------|---------------------|-------------------|
| The Kings Were Humming (`blacktie_event_kings_were_humming_01`) | `aarons_corner_table.png` scene-lit state, Aaron rows 0–7, `candy_smokes_carton.png`, `tractor_nft_token.png` | One-time scripted spectator encounter on approach; grants candy smokes + tractor NFT |
| High Stakes | Playable table plates, chip stack, high roller badge | Win 1,000 Sovs total → salon rope opens |
| The Card Shark | Herr Falsch full sheet, marked cards, shark fin | Hidden boss discovered in private boxes; exposed-cheating weakness |
| The Reformed Gambler | Siegfried both variant rows | Foyer coat-check backstory questline; couchsurf grants permanent −5% house edge |
| Baroness Vault | Vault antechamber locked/unlocked states | Post-main-boss access via Baroness' vault keys |
| NFT Hunt (Sinfonia leg) | `tractor_nft_token.png` | `Design/Quests/fratbronft.md`, acquired via the Kings Were Humming scene |

### Cross-Location Dependencies:
| Connected Location | Sprite Connection | Transition Effect |
|--------------------|-------------------|-------------------|
| The Bassline Opera House | Backstage prop-corridor tiles (the hidden entrance is dressed to match them); Baroness' vault keys icon (drops from the Maestro; opens the vault antechamber) | Hidden-door + staircase descent |
| Haute Couture Haberdashery | Black-Tie Attire equipped-state overlays (the Backroom's dress-code check reads them) | None (item-state read); systemic note: a party busted here can no longer afford the Haberdashery's 500 Sovs Valued Client path |
| Café Existenz / Kaffeehaus Row | Discovery hints only (regulars' gossip) | No sprite transition |
| The Kings Were Humming (quest) | `aaron_the_unflappable.png`, `aarons_corner_table.png`, `candy_smokes_carton.png`, `tractor_nft_token.png` are all consumed by `Design/Quests/Location Specific/Sinfonia/thekingswerehumming.md`. No additional PNGs are required by that quest | In-location scene |

---

## 🎨 Art Direction Summary

### Visual Aesthetic:
- **Primary Theme:** "Legitimate sophistication worn as a mask over vice." Thirty steps take the player from a dusty prop corridor to gilded luxury. Everything is expensive; nothing is warm. Chandeliers that cost more than houses, servers dressed better than guests, chips of actual silver that mean nothing outside these walls. The elegance should never read as cosy — it reads as *engineered*.
- **Color Mood:** Burgundy and gold over midnight blue and vice black; two felts, two moral registers (green for the house's games, oxblood for the one table that isn't playing)
- **Lighting:** Warm chandelier glow with shadowed Vice Black edges — the room's perimeter is always darker than its tables (see Lighting Requirements below)
- **Texture:** Deep velvet, milled silver, gold leaf, cold stone under the vault's trim — luxury with the temperature of a ledger

### Environmental Storytelling:
- The staircase is the thesis: class transition in thirty steps, cold grey to heavy gold
- The foyer mirror is both attire check and surveillance; the House Rules in calligraphy are legible, binding, and unhelpful
- The tally book at the bar's end and the "complimentary" card in brass: nothing here is free, everything is itemized
- Aaron's undressed oxblood table is the only honest furniture in the building
## Technical Specifications

### File Format Requirements
- **Format**: PNG-24 with alpha transparency
- **Color Space**: sRGB
- **Resolution**: 72 DPI (screen optimized)
- **Compression**: Lossless
- **Naming Convention**: `snake_case_descriptive.png`

### Performance Optimization Targets
- **Texture Atlases**: Maximum 4 at 1024px
- **Draw Calls**: Under 20 for the full location
- **Memory**: Under 50MB with all zones loaded
- **Particles**: Maximum 60 simultaneous
- **Target FPS**: 60 on min-spec hardware
- **Pre-rendered**: Roulette spin cycle, card deal animations, static crowd fills

### Character Integration Notes:
- Anton and the bouncer share tailoring language; only the polish differs
- The tells (cufflink adjust, champagne sip) are gameplay-critical animation — readable at a glance, never prompted
- Aaron's rumple, tumbler, and chalk residue are consistency requirements across every frame, not decoration
- Gräfin Stille's expression never changes across any frame in her sheet; stillness is the characterization

---

## 💡 Lighting Requirements

### Main Floor
- **Ambient**: Warm chandelier glow (#FFD700), 70% intensity
- **Table lights**: Focused pools over each playable table, tight falloff, shared warm tone
- **Edges**: Shadowed to Vice Black (#0D0D0D) — the room's perimeter is always darker than its tables

### Aaron's Corner Table
- **Pendant lamp**: Single low point light, warmer and dimmer than the floor's table lights, radius deliberately smaller so the table sits in its own pool
- **Scene state**: Pendant intensity up one step, room ambient down one step. No other lighting change

### Foyer & Staircase
- **Staircase**: Vertical gradient, cold grey (#F0F0F0, 40%) at the top to gas-lamp gold (#FFD700, 80%) at the bottom
- **Foyer**: Even, unflattering, mirror-bounced — this is a room designed for being looked at in

### Vault Antechamber
- **Locked**: Cold blue key light (#191970), 30%
- **Unlocked**: Gold spill from the open door, 70%

---

## 🎯 Social Media Viral Potential

### Screenshot-Worthy Moments:
1. **The Staircase Descent** - Thirty steps from broom closet to chandelier; the class-transition shot composes itself
2. **Aaron's Crunch** - A man in a rumpled velvet jacket biting a candy cigarette over a 500 Sovs-minimum room, unbothered
3. **The Salon Selfie Spot** - Chip stack + chandelier framing marked into the level design on purpose
4. **The Tractor NFT Reveal** - Mint #42's deliberately terrible mower-donut GIF, worse than everything around it
5. **Cleaned Out** - The off-register CLEANED OUT stamp across a forfeit receipt

### Quote Potential:
- "The house always wins, and is very polite about it."
- "The chips are actual silver. They are worth nothing outside this door."
- "Private — Staff Only." (It is not a staff area.)

---

## 📋 Required PNG Files (38 Total)

| # | Filename | Dimensions | Category |
|---|----------|------------|----------|
| 1 | hidden_entrance.png | 256x384 | Environment |
| 2 | staircase_transition.png | 256x512 | Environment |
| 3 | foyer_verification.png | 384x256 | Environment |
| 4 | main_floor.png | 640x512 | Environment |
| 5 | aarons_corner_table.png | 320x256 | Environment |
| 6 | high_stakes_salon.png | 512x384 | Environment |
| 7 | private_box.png | 256x256 | Environment |
| 8 | vault_antechamber.png | 384x384 | Environment |
| 9 | poker_table.png | 384x256 | Environment |
| 10 | roulette_table.png | 384x384 | Environment |
| 11 | blackjack_table.png | 384x256 | Environment |
| 12 | bar_area.png | 256x192 | Environment |
| 13 | chandelier_detail.png | 192x192 | Environment |
| 14 | anton_doorman.png | 384x512 | Character |
| 15 | madame_karten.png | 256x384 | Character |
| 16 | herr_falsch.png | 512x960 | Character |
| 17 | nervous_noble.png | 256x288 | Character |
| 18 | silent_countess.png | 256x288 | Character |
| 19 | house_dealer.png | 256x384 | Character |
| 20 | siegfried_coatcheck.png | 256x384 | Character |
| 21 | high_roller_npc.png | 256x384 | Character |
| 22 | server_tray.png | 256x288 | Character |
| 23 | bouncer_escort.png | 384x384 | Character |
| 24 | aaron_the_unflappable.png | 384x1024 | Character |
| 25 | chip_stack.png | 64x64 | UI/Item |
| 26 | card_deck.png | 48x64 | UI/Item |
| 27 | roulette_wheel.png | 192x192 | UI/Item |
| 28 | bet_interface.png | 256x128 | UI/Item |
| 29 | house_edge_meter.png | 128x32 | UI/Item |
| 30 | high_roller_badge.png | 48x48 | UI/Item |
| 31 | shark_fin.png | 32x48 | UI/Item |
| 32 | marked_cards.png | 48x64 | UI/Item |
| 33 | collateral_receipt.png | 48x32 | UI/Item |
| 34 | members_card.png | 48x32 | UI/Item |
| 35 | tell_indicator.png | 32x32 | UI/Item |
| 36 | cleaned_out_stamp.png | 64x64 | UI/Item |
| 37 | candy_smokes_carton.png | 48x48 | UI/Item |
| 38 | tractor_nft_token.png | 32x32 | UI/Item |

**Manifest split:** Environment 13 · Character 11 · UI/Item 14 = 38.

**Total Estimated Memory:** ~13.5 MB (uncompressed RGBA)

---

## 📦 File Delivery Checklist

### Required PNG Files — Environment (13):
- [ ] `hidden_entrance.png` (256x384)
- [ ] `staircase_transition.png` (256x512)
- [ ] `foyer_verification.png` (384x256)
- [ ] `main_floor.png` (640x512)
- [ ] `aarons_corner_table.png` (320x256)
- [ ] `high_stakes_salon.png` (512x384)
- [ ] `private_box.png` (256x256)
- [ ] `vault_antechamber.png` (384x384)
- [ ] `poker_table.png` (384x256)
- [ ] `roulette_table.png` (384x384)
- [ ] `blackjack_table.png` (384x256)
- [ ] `bar_area.png` (256x192)
- [ ] `chandelier_detail.png` (192x192)

### Required PNG Files — Character (11):
- [ ] `anton_doorman.png` (384x512)
- [ ] `madame_karten.png` (256x384)
- [ ] `herr_falsch.png` (512x960)
- [ ] `nervous_noble.png` (256x288)
- [ ] `silent_countess.png` (256x288)
- [ ] `house_dealer.png` (256x384)
- [ ] `siegfried_coatcheck.png` (256x384)
- [ ] `high_roller_npc.png` (256x384)
- [ ] `server_tray.png` (256x288)
- [ ] `bouncer_escort.png` (384x384)
- [ ] `aaron_the_unflappable.png` (384x1024)

### Required PNG Files — UI/Item (14):
- [ ] `chip_stack.png` (64x64)
- [ ] `card_deck.png` (48x64)
- [ ] `roulette_wheel.png` (192x192)
- [ ] `bet_interface.png` (256x128)
- [ ] `house_edge_meter.png` (128x32)
- [ ] `high_roller_badge.png` (48x48)
- [ ] `shark_fin.png` (32x48)
- [ ] `marked_cards.png` (48x64)
- [ ] `collateral_receipt.png` (48x32)
- [ ] `members_card.png` (48x32)
- [ ] `tell_indicator.png` (32x32)
- [ ] `cleaned_out_stamp.png` (64x64)
- [ ] `candy_smokes_carton.png` (48x48)
- [ ] `tractor_nft_token.png` (32x32)

### Quality Requirements:
| Requirement | Specification |
|-------------|---------------|
| Format | PNG-24 with alpha channel |
| Color Space | sRGB |
| DPI | 72 (screen resolution) |
| Compression | Lossless PNG |
| Naming Convention | snake_case, all lowercase (`snake_case_descriptive.png`) |
| Layer Organization | Preserve layers in master file |

### Delivery Format:
- **Primary:** Individual PNG files per specifications above
- **Backup:** Master PSD/layered file with organized layer groups
- **Documentation:** Animation timing reference sheet + Two-Felt Rule compliance sheet (side-by-side thumbnail proof)

---

## ✅ Final Delivery Validation

### Before Submitting Assets:
- [ ] All PNG files match exact dimensions specified
- [ ] Color palette matches hex codes exactly — felt hexes (#0B3D2E / #4A1F24) bit-exact
- [ ] Two-Felt Rule verified at thumbnail size on a phone screen (BINDING)
- [ ] Aaron's tumbler, rumple, and chalk residue present in every frame of his sheet
- [ ] The crunch break (Aaron row 3, frame 2) reads clearly at 1× scale
- [ ] Tells (cufflink adjust, champagne sip) readable at a glance without UI prompt
- [ ] Tractor NFT loop is convincingly worse than everything around it
- [ ] Accessibility visual alternatives included for all audio cues
- [ ] File naming follows snake_case convention (aaron_the_unflappable.png exact)
- [ ] Master files preserve layer structure for future edits

### Quality Checkpoints:
- [ ] Satirical theme (elegance as anesthetic for the house edge) clear throughout
- [ ] Hidden entrance discoverable but genuinely boring at first glance
- [ ] Performance optimized (pre-rendered spins/deals, ≤20 draw calls, atlas limits respected)
- [ ] Touch zone sizing considered (44px minimum for bet interface and interactive elements)
- [ ] Colorblind-friendly redundancy for the Two-Felt Rule (furniture, not just hue)
- [ ] Social media viral potential maximized in composition choices (staircase, selfie spot, crunch)

---

## 🏆 Location Validation Status

| Requirement | Status | Notes |
|-------------|--------|-------|
| World Consistency (no real city names) | ✅ | Sinfonia only; imperial gambling salons evoked, never named |
| Cultural Specificity | ✅ | European private gaming clubs, old imperial salon traditions |
| Satirical Targets Appropriate | ✅ | High-society wealth performance and the polite house edge — punches up |
| Seedy Underbelly Present | ✅ | This IS the underbelly: hidden den, collateral window, rigged odds, marked cards |
| Gameplay Value Established | ✅ | Three minigames, hidden boss, reputation gate, scripted encounter, vault |
| Technical Feasibility | ✅ | 38 PNGs, 4-atlas plan, pre-rendered heavy animations, zone loading |
| Performance Budget | ✅ | 60 FPS, ≤20 draw calls, ≤50 MB, 60 particles |
| Accessibility Features | ✅ | Visual audio cues, reduced-motion wheel, shape-redundant Two-Felt Rule |
| No Crypto Elements | ✅ | Tractor NFT is established source material (fratbronft.md NFT Hunt) and is satirized as worthless by design |
| Social Media Integration | ✅ | Staircase, crunch, selfie spot, and NFT-reveal moments identified |

**The Black-Tie Backroom: thirty steps from a prop corridor to a chandelier, silver chips that mean nothing outside the door, and one corner table that is not for sale.**
