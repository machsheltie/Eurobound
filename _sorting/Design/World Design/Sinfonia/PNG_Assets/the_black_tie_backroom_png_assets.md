# The Black-Tie Backroom - Complete PNG Asset Requirements

*Artist Reference Document for Sinfonia's Hidden Gambling Den*

**Location ID**: `sinfonia_operahouse_blacktie_backroom_01`
**Priority**: HIGH (Mini-Game Hub, Hidden Boss Arena, Reputation Gate, Scripted Encounter)
**Total PNGs Required**: 38 (13 environment, 11 character, 14 UI/item)
**Mobile Optimization**: Target 45 FPS on iPhone 8+, max 20 draw calls, 50MB memory

**Source of truth**: `Design/World Design/Sinfonia/the_black_tie_backroom.md` (PNG Asset Requirements Summary). Every filename below appears in that summary; every filename referenced by `sprite_mapping/the_black_tie_backroom_sprite_mapping.json` appears below.

---

## Art Direction Summary

### Visual Identity
The Backroom is **legitimate sophistication worn as a mask over vice**. Thirty steps take the player from a dusty prop corridor to gilded luxury. Everything is expensive; nothing is warm. Chandeliers that cost more than houses, servers dressed better than guests, chips of actual silver that mean nothing outside these walls. The elegance should never read as cosy — it reads as *engineered*.

### Color Palette

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

**Aaron's corner table uses Corner Oxblood (#4A1F24) and carries none of that dressing.** No rail, no plaque, no markings, its own low pendant lamp. A player must be able to tell the two apart in a single glance, at thumbnail size, on a phone. This is a hard requirement, not a style preference.

---

# PART 1 — ENVIRONMENT ART (13 PNGs)

## 1. Hidden Entrance
**Filename**: `hidden_entrance.png`
**Dimensions**: 256 × 384

Three horizontal states across the sheet:
1. **Closed**: Unremarkable door in the opera house backstage, "Private — Staff Only" plate, scuffed paint, easily missed
2. **Ajar**: Warm sliver of light at the seam, hinting at somewhere that does not belong behind a prop corridor
3. **Open**: Full reveal of the passage mouth beyond

*Art Note*: The door must look boring. Its only tell is that it is slightly too clean around the handle.

---

## 2. Staircase Transition
**Filename**: `staircase_transition.png`
**Dimensions**: 256 × 512

A single vertical piece reading top-to-bottom as a class transition in thirty steps: dusty boards and bare bulb at the top, marble treads mid-way, brass railings and gas-lamp-style sconces at the bottom. Carpet appears one third of the way down and thickens.

*Art Note*: Light temperature shifts with the material — cold and grey at the top, gold and heavy at the bottom.

---

## 3. Foyer / Verification Zone
**Filename**: `foyer_verification.png`
**Dimensions**: 384 × 256

Small antechamber. Full-length mirror (attire check and surveillance both), brass gold-deposit window with a small scale and receipt spike, and the House Rules posted in elegant calligraphy on a stand. Doorman's position marked at frame left.

*Art Note*: The calligraphy must be legible at 2× zoom — the three House Rules are readable content in-world.

---

## 4. Main Floor
**Filename**: `main_floor.png`
**Dimensions**: 640 × 512

The primary gaming room. Open floor with the standard house tables (poker, roulette, blackjack) in Table Green with full dressing, bar running along one wall, crystal chandeliers, velvet everything, gold leaf details. Corner recess at frame right reserved for the corner-table zone (see next sheet) — the base plate leaves that recess empty so the zone can be composited over it.

*Art Note*: Sightlines matter. The corner recess must be visible from the room's entry point without the player having to hunt for it.

---

## 5. Aaron's Corner Table
**Filename**: `aarons_corner_table.png`
**Dimensions**: 320 × 256

The named main-floor zone `aarons_corner_table`, composited into the main floor's corner recess.

**Three states across the sheet:**
1. **Ambient (pre-scene)**: Corner Oxblood felt, low pendant lamp with a warm tight pool of light, one crystal tumbler with a pale drink, a worn candy-cigarette carton at the table edge, a small ring of chalky white dust on the felt. Two spare chairs. No chip rail, no dealer plaque, no bet markings
2. **Scene-lit (during `blacktie_event_kings_were_humming_01`)**: Pendant lamp intensity up, room behind the table falls a stop darker, three additional chairs occupied, chips pushed to centre
3. **Ambient (post-scene)**: As state 1, with a taller chip stack and the chalk ring larger

*Art Note (BINDING)*: This table must never be mistakable for a playable table. Different felt, different lamp, no house furniture. If an artist's pass makes it look like the room's other tables, the pass is wrong.

---

## 6. High Stakes Salon
**Filename**: `high_stakes_salon.png`
**Dimensions**: 512 × 384

Separated from the main floor by a velvet rope on brass stanchions. Fewer tables, larger spacing, personal servers stationed at the walls, better upholstery. Table Green with full dressing throughout. Selfie-spot framing marked at the centre table (chip stack + chandelier above).

---

## 7. Private Box
**Filename**: `private_box.png`
**Dimensions**: 256 × 256

A single discreet room: one table, four chairs, heavy door, no windows, one lamp. Deliberately under-decorated compared to the floor — this room is for business.

---

## 8. Vault Antechamber
**Filename**: `vault_antechamber.png`
**Dimensions**: 384 × 384

Post-boss area behind a keyed door. Cold stone under gold trim, storage racks, and the Baroness' personal vault door dominating the far wall. Two states: **locked** (keyhole plate dark) and **unlocked** (plate lit, door ajar).

---

## 9. Poker Table
**Filename**: `poker_table.png`
**Dimensions**: 384 × 256

Playable poker interface plate. Table Green felt, brass chip rail, dealer plaque, printed betting positions for up to six seats, card landing zones marked.

---

## 10. Roulette Table
**Filename**: `roulette_table.png`
**Dimensions**: 384 × 384

Playable roulette layout for the **Sinfonian Wheel** — single-zero European style. Numbered grid, outside bets, and the marked "Composer's Dozen" special-bet block. Wheel well at the head of the table (wheel itself is a separate UI sheet).

---

## 11. Blackjack Table
**Filename**: `blackjack_table.png`
**Dimensions**: 384 × 256

Playable **Twenty-One Sinfonian** layout. Seven seat positions, insurance line, "Dealer stands on 17" printed in period lettering along the arc.

---

## 12. Bar Area
**Filename**: `bar_area.png`
**Dimensions**: 256 × 192

Long bar along the main floor wall. Backlit bottle shelving, crystal glassware, a discreet tally book at the server's end. Small "complimentary" card in a brass stand.

---

## 13. Chandelier Detail
**Filename**: `chandelier_detail.png`
**Dimensions**: 192 × 192

Hero decorative element, reused across zones at varying scales. Crystal drops, gold armature, subtle glint frames for the sparkle particle effect.

---

# PART 2 — CHARACTER SPRITES (11 PNGs)

*Cell sizes below are as registered in the location file's asset summary. Sheet dimensions are the full multi-row sheets.*

## 14. Viktor the Doorman
**Filename**: `viktor_doorman.png`
**Cell Size**: 96 × 128 | **Sheet**: 384 × 512 (4 columns × 4 rows)
**NPC ID**: `sinfonia_npc_viktor_doorman_01`

- **Look**: Built like a bouncer, dressed like a butler. Tailcoat cut a size too small across the shoulders on purpose. White gloves. Immaculate.
- **Animations**: Row 0 `idle_stance` (2f, 1 fps) · Row 1 `assess_attire` (4f, 3 fps — head-to-toe look, unhurried) · Row 2 `accept_collateral` (3f, 3 fps — gloved hand extended, receipt returned) · Row 3 `refuse_entry` (3f, 3 fps — half-step sideways, arm across the doorway)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/viktor_the_doorman.md`

---

## 15. Madame Karten
**Filename**: `madame_karten.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 384 (4 columns × 4 rows)
**NPC ID**: `sinfonia_npc_madame_karten_01`

- **Look**: Elegant older woman, floor-length dark gown, pearls, hair up. Eyes that track the room, not the player.
- **Animations**: Row 0 `idle_survey` (4f, 2 fps — slow scan of the floor) · Row 1 `approach_warm` (4f, 4 fps) · Row 2 `offer_drink` (3f, 3 fps) · Row 3 `catch_cheater` (4f, 4 fps — the scan stops, no other movement)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/madame_karten.md`

---

## 16. Herr Falsch
**Filename**: `herr_falsch.png`
**Cell Size**: 128 × 192 (boss scale) | **Sheet**: 512 × 960 (4 columns × 5 rows)
**NPC ID**: `sinfonia_npc_herr_falsch_01`

- **Look**: Tuxedo too perfect to be comfortable. Card-motif studs and cufflinks. A smile held slightly too long.
- **Animations**: Row 0 `idle_dealing` (4f, 3 fps) · Row 1 `full_house_summon` (6f, 5 fps — card constructs rise from the felt) · Row 2 `dead_mans_hand` (4f, 5 fps — targeted flick) · Row 3 `the_river` (4f, 4 fps — arena tiles flip) · Row 4 `sleeve_ace_interrupt` (4f, 6 fps) + `exposed` variant frames (cheating revealed: sleeve cards visible, posture drops)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/herr_falsch.md`

---

## 17. Graf von Zittrig (The Nervous Noble)
**Filename**: `nervous_noble.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 288 (4 columns × 3 rows)
**NPC ID**: `sinfonia_npc_graf_von_zittrig_01`

- **Look**: Expensive clothes visibly damp at the collar. Handkerchief. Cufflinks that catch the light.
- **Animations**: Row 0 `idle_composed` (2f, 1 fps — trying) · Row 1 `cufflink_adjust` (3f, 4 fps — **the tell**, must be readable at a glance) · Row 2 `fold_relief` (3f, 3 fps)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/graf_von_zittrig.md`

---

## 18. Gräfin Stille (The Silent Countess)
**Filename**: `silent_countess.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 288 (4 columns × 3 rows)
**NPC ID**: `sinfonia_npc_grafin_stille_01`

- **Look**: Immaculate, still, champagne flute always within reach. Expression never changes across any frame in the sheet.
- **Animations**: Row 0 `idle_motionless` (2f, 1 fps — blink only) · Row 1 `champagne_sip` (3f, 2 fps — **the tell**) · Row 2 `push_chips` (3f, 3 fps — the only way she speaks)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/grafin_stille.md`

---

## 19. House Dealer
**Filename**: `house_dealer.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 384 (4 columns × 4 rows)

Rotating generic house dealer — **three palette variants** on the same skeleton (waistcoat colour + hair) so the roster can rotate without new sheets.

- **Animations**: Row 0 `idle` (2f, 1 fps) · Row 1 `deal_cards` (4f, 6 fps) · Row 2 `spin_wheel` (4f, 6 fps) · Row 3 `sweep_pot` (4f, 5 fps)

---

## 20. Siegfried (Coat Check)
**Filename**: `siegfried_coatcheck.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 384 (4 columns × 4 rows)
**NPC ID**: `sinfonia_npc_siegfried_coatcheck_01`

- **Look**: Club waistcoat, sleeves rolled, coat-check counter. A second, plainer variant row for his apartment above the club (no waistcoat, iron in hand).
- **Animations**: Row 0 `idle_counter` (2f, 1 fps) · Row 1 `take_coat` (3f, 3 fps) · Row 2 `accept_tip` (3f, 3 fps) · Row 3 `apartment_ironing` (4f, 2 fps)

*Full characterization*: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/siegfried_coat_check.md`

---

## 21. High Roller (Background Elite)
**Filename**: `high_roller_npc.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 384 (4 columns × 4 rows)

Ambient crowd filler for the salon and floor. **Four palette/silhouette variants** (two gowns, two dinner suits) so a crowd can be built from one sheet.

- **Animations**: Row 0 `idle_standing` (2f, 1 fps) · Row 1 `idle_seated` (2f, 1 fps) · Row 2 `celebrate_small` (3f, 3 fps) · Row 3 `deflate` (3f, 2 fps)

---

## 22. Server with Tray
**Filename**: `server_tray.png`
**Cell Size**: 64 × 96 | **Sheet**: 256 × 288 (4 columns × 3 rows)

- **Look**: Better suit than most of the guests. Tray of "complimentary" drinks never empty.
- **Animations**: Row 0 `walk_tray` (4f, 4 fps) · Row 1 `offer_drink` (3f, 3 fps) · Row 2 `observe` (2f, 1 fps — pause at the table's shoulder)

---

## 23. Bouncer Escort
**Filename**: `bouncer_escort.png`
**Cell Size**: 96 × 128 | **Sheet**: 384 × 384 (4 columns × 3 rows)

Cheat-consequence encounter sprite. Same tailoring language as Viktor, none of the polish.

- **Animations**: Row 0 `idle_menace` (2f, 1 fps) · Row 1 `grab` (4f, 6 fps) · Row 2 `eject` (4f, 5 fps — toward the stairs, off-frame)

---

## 24. Aaron the Unflappable
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

## 25. Chip Stack
**Filename**: `chip_stack.png` · **Dimensions**: 64 × 64
Silver house chips in stacked heights (1, 5, 10, 20+). Actual silver sheen, milled edges, house crest struck on the face. Four height variants across the sheet for the currency display.

## 26. Card Deck
**Filename**: `card_deck.png` · **Dimensions**: 48 × 64
Deck back (house crest), deck side profile, and a 3-frame deal animation strip (top card lifting, in flight, landed).

## 27. Roulette Wheel
**Filename**: `roulette_wheel.png` · **Dimensions**: 192 × 192
Single-zero Sinfonian Wheel head. 8-frame spin cycle (blur-tiered: crisp → light blur → heavy blur → light blur), plus a settled state with the ball in a pocket.

## 28. Bet Interface
**Filename**: `bet_interface.png` · **Dimensions**: 256 × 128
Placement UI frame in burgundy and gold: chip-denomination selector, confirm/clear, and the bet-total readout plate.
*Binding note*: This asset is used **only** at the room's playable tables. It has no state, variant, or anchor at `aarons_corner_table`.

## 29. House Edge Meter
**Filename**: `house_edge_meter.png` · **Dimensions**: 128 × 32
Thin horizontal bar with a gold fill and a small engraved plate. Debug/informational visualization of the hidden math; shown only where design calls for it.

## 30. High Roller Badge
**Filename**: `high_roller_badge.png` · **Dimensions**: 48 × 48
Status indicator. Gold-rimmed enamel disc, velvet-rope motif. Locked (grey) and earned (gold) states.

## 31. Shark Fin
**Filename**: `shark_fin.png` · **Dimensions**: 32 × 48
`item_shark_fin` — Herr Falsch victory accessory. Lapel-pin scale, brushed silver dorsal fin on a card-suit backing plate. Inventory icon plus equipped overlay.
*Item file*: `Design/Inventory/items/shark_fin_item.md`

## 32. Marked Cards
**Filename**: `marked_cards.png` · **Dimensions**: 48 × 64
Cheat item. Two states: **normal view** (identical to a standard deck back) and **marked view** (faint scratch pattern in the corner ornament, visible only in the cheat overlay).

## 33. Collateral Receipt
**Filename**: `collateral_receipt.png` · **Dimensions**: 48 × 32
The €500 door deposit slip. Thin card stock, house crest, hand-inked amount, spike hole at the top edge. States: **issued**, **redeemed**, **forfeit** (stamped through).

## 34. Member's Card
**Filename**: `members_card.png` · **Dimensions**: 48 × 32
`item_members_card` — Backroom access alternative. Black card, gold engraving, no name printed on it.
*Item file*: `Design/Inventory/items/members_card_item.md`

## 35. Tell Indicator
**Filename**: `tell_indicator.png` · **Dimensions**: 32 × 32
Small diegetic-adjacent flourish shown above an NPC when a learned tell fires. Three intensity variants. Never appears at `aarons_corner_table`.

## 36. Cleaned Out Stamp
**Filename**: `cleaned_out_stamp.png` · **Dimensions**: 64 × 64
Failure badge. Ink-stamp lettering across a receipt corner, slightly off-register.

## 37. Candy Smokes Carton
**Filename**: `candy_smokes_carton.png` · **Dimensions**: 48 × 48
`item_candy_smokes` — Puff-Puff-Powder™ Chalk 'n' Ash Candy Smokes. Worn carton, soft-creased lid, faded period-cartoon branding, corners furred from handling. **States**: closed carton (inventory icon), open carton with sticks visible, single stick full length, single stick post-bite.
Includes the shared **`chalk_puff`** particle strip (4 frames, 8 fps) and the **chalk ring** mouth overlay (2 variants) used by the item's use-effect.
*Item file*: `Design/Inventory/items/candy_smokes_item.md` · Scene-granted only, at `blacktie_event_kings_were_humming_01`

## 38. Tractor NFT Token
**Filename**: `tractor_nft_token.png` · **Dimensions**: 32 × 32
`item_tractor_nft` — "She Thinks My Tractor's Sexy" (Mint #42). Scratched aluminium token, struck edge, "#42" stamped small. Face carries the low-res animated GIF loop: a zero-turn mower doing a donut on a manicured lawn, a tiny pixelated cowboy hat bouncing on the seat. **6-frame loop at 4 fps, deliberately low-fidelity** — the animation must look worse than the rest of the game's art, on purpose. Reverse face: a QR block.
*Item file*: `Design/Inventory/items/tractor_nft_item.md` · Scene-granted only, at `blacktie_event_kings_were_humming_01`

---

## Lighting Requirements

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

## Particle & Effect Requirements

| Effect | Source | Notes |
|--------|--------|-------|
| Cigar smoke wisps | Main floor, salon | Slow drift, low opacity, never obscures a table |
| Chip shine | `chip_stack.png` | Glint on stack changes |
| Card flutter | `card_deck.png` | Deal and sweep |
| Champagne bubbles | Bar, salon | Tied to `server_tray.png` and Gräfin Stille's tell |
| Chandelier sparkle | `chandelier_detail.png` | Rare, subtle |
| `chalk_puff` | Aaron row 3, candy-smokes use effect | **Shared** — one particle asset, two consumers |

---

## Technical Specifications

### File Format Requirements
- **Format**: PNG-24 with alpha transparency
- **Color Space**: sRGB
- **Resolution**: 72 DPI (screen optimized)
- **Compression**: Lossless
- **Naming Convention**: `snake_case_descriptive.png`

### Mobile Optimization Targets
- **Texture Atlases**: Maximum 4 at 1024px
- **Draw Calls**: Under 20 for the full location
- **Memory**: Under 50MB with all zones loaded
- **Particles**: Maximum 60 simultaneous
- **Target FPS**: 45 on iPhone 8+
- **Pre-rendered**: Roulette spin cycle, card deal animations, static crowd fills

### Animation Guidelines
- **Idle Loops**: 2–4 frames, 1–2 FPS
- **Tells**: 3 frames, 2–4 FPS — must read at a glance without a UI prompt
- **Action Animations**: 3–6 frames, 3–6 FPS
- **Boss Attacks**: 4–6 frames, 4–6 FPS

---

## Cross-Reference: Related Assets

### From The Bassline Opera House
- Backstage prop-corridor tiles (the hidden entrance is dressed to match them)
- Baroness' vault keys icon (drops from the Maestro; opens the vault antechamber)

### To Haute Couture Haberdashery
- Black-Tie Attire equipped-state overlays (the Backroom's dress-code check reads them)

### To The Kings Were Humming
- `aaron_the_unflappable.png`, `aarons_corner_table.png`, `candy_smokes_carton.png`, `tractor_nft_token.png` are all consumed by `Design/Quests/Location Specific/Sinfonia/thekingswerehumming.md`. No additional PNGs are required by that quest

---

## Asset Manifest (38)

**Environment (13)**: `hidden_entrance.png`, `staircase_transition.png`, `foyer_verification.png`, `main_floor.png`, `aarons_corner_table.png`, `high_stakes_salon.png`, `private_box.png`, `vault_antechamber.png`, `poker_table.png`, `roulette_table.png`, `blackjack_table.png`, `bar_area.png`, `chandelier_detail.png`

**Character (11)**: `viktor_doorman.png`, `madame_karten.png`, `herr_falsch.png`, `nervous_noble.png`, `silent_countess.png`, `house_dealer.png`, `siegfried_coatcheck.png`, `high_roller_npc.png`, `server_tray.png`, `bouncer_escort.png`, `aaron_the_unflappable.png`

**UI/Item (14)**: `chip_stack.png`, `card_deck.png`, `roulette_wheel.png`, `bet_interface.png`, `house_edge_meter.png`, `high_roller_badge.png`, `shark_fin.png`, `marked_cards.png`, `collateral_receipt.png`, `members_card.png`, `tell_indicator.png`, `cleaned_out_stamp.png`, `candy_smokes_carton.png`, `tractor_nft_token.png`

---

**END OF ASSET REQUIREMENTS**

*The Black-Tie Backroom: thirty steps from a prop corridor to a chandelier, silver chips that mean nothing outside the door, and one corner table that is not for sale.*
