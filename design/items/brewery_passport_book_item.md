# The Brewery Passport Book

*Your leather-bound ticket to the Continental Beer Trail — collect stamps, unlock beers, become legend* [source: design/items/brewery_passport_book.md L3]

## System Overview

### What Is It?
The Brewery Passport Book is a collectible menu item that tracks the player's progress through the Brewery Tour sidequest. It functions as both a physical in-game item and a dedicated menu interface, displaying stamps collected from breweries and pubs across all cities in the game. [source: design/items/brewery_passport_book.md L8]

### Acquisition
- **Item ID**: `brewery_passport_book`
- **Location**: The Blarney Trap, Publandia
- **Method**: GRANTED — handed over together with the Bottle Opener Keychain and The Blarney Trap's opener, all in the same moment, the instant the bros order the special beer for the first time. Never purchased, never a Pint-Off reward. [source: design/quests/general_quests/brewerytour.md L27-34] (Supersedes both legacy sources' "given free with a keychain purchase, or as a challenge reward" framing — that purchase/reward language is dead per the Publandia special-beer-order trigger ruling, 2026-08-04 [source: design/items/brewery_passport_book.md L12; design/items/brewery_passport_book_complete.md L12].)
- **Requirement**: Cannot participate in the Brewery Tour without both the keychain and the book in inventory [source: design/items/brewery_passport_book.md L13]
- **Timing**: The moment the trigger fires — the first special-beer order at The Blarney Trap [source: design/quests/general_quests/brewerytour.md L27-31]

### Seamus's Introduction
*"This book? It's your passport to the real beer culture of Europe. Every brewery, every pub worth its salt — they'll stamp you. Proves you were there. REALLY there. Fill a city's page, you earn their Legendary Hangover. Fill the whole book? Continental Beer Master. That's not just a title. That's a LIFESTYLE."* [source: design/items/brewery_passport_book_complete.md L17]

---

## Menu Integration

*Copied verbatim from `design/items/brewery_passport_book.md` L21-99. The "2/16" progress figure below was already correct in the source (16 total breweries) and required no change; no other totals appear in this section.*

### Access Location
**Pause Menu → "Brewery Passport" tab**
- New tab appears in pause menu once book is acquired
- Icon: Leather book with hop leaf bookmark
- Notification badge when new stamp is available

### Interface Layout

**Main View (Book Closed)**
```
╔══════════════════════════════════════════════╗
║     THE CONTINENTAL BEER TRAIL               ║
║     ══════════════════════════               ║
║                                              ║
║          [BOOK COVER IMAGE]                  ║
║                                              ║
║     Progress: 2/16 Stamps Collected          ║
║     ▓▓░░░░░░░░░░░░░░ 12.5%                  ║
║                                              ║
║     [OPEN BOOK]                              ║
╚══════════════════════════════════════════════╝
```

**Book Open View (City Selection)**
```
╔══════════════════════════════════════════════╗
║  ◄ PUBLANDIA    DEBAUCHERYVILLE ►            ║
║    (2/4)           (0/4)                     ║
╠══════════════════════════════════════════════╣
║                                              ║
║              PUBLANDIA                       ║
║        "The Emerald Isle's Finest"           ║
║                                              ║
║    ┌─────────┐        ┌─────────┐           ║
║    │ ☘ STAMP │        │ 🏭 STAMP│           ║
║    │ Blarney │        │Stoutworks│           ║
║    │  Trap   │        │ Brewery │           ║
║    └─────────┘        └─────────┘           ║
║                                              ║
║    ┌─────────┐        ┌─────────┐           ║
║    │░░░░░░░░░│        │░░░░░░░░░│           ║
║    │ Trinity │        │ [LOCKED]│           ║
║    │of Pints │        │         │           ║
║    └─────────┘        └─────────┘           ║
║                                              ║
╠══════════════════════════════════════════════╣
║  LEGENDARY HANGOVER: 🔒 LOCKED (2/4)         ║
║  Collect all Publandia stamps to unlock      ║
╚══════════════════════════════════════════════╝
```

**Stamp Detail View (When Selected)**
```
╔══════════════════════════════════════════════╗
║           THE BLARNEY TRAP                   ║
║           ═══════════════                    ║
║                                              ║
║         [LARGE STAMP IMAGE]                  ║
║          Celtic Harp Design                  ║
║          Est. 1847 — Publandia               ║
║                                              ║
║  ─────────────────────────────────────────   ║
║  SIGNATURE BEER UNLOCKED:                    ║
║                                              ║
║  🍺 The Sweet Surrender                      ║
║     Irish Stout • 5.2% ABV                   ║
║     +35 HP, +10 SP                           ║
║     "Comfortable Trap" buff                  ║
║                                              ║
║  Acquired: Won Pint-Off Challenge            ║
║  Date: Day 3, 9:47 PM                        ║
║                                              ║
║  📸 SELFIE: [View] [Not Yet Collected]       ║
║                                              ║
║            [CLOSE]                           ║
╚══════════════════════════════════════════════╝
```

---

## Stamp Mechanics

### How Stamps Are Earned
Each brewery/pub has a specific unlock condition that must be met WHILE possessing the Bottle Opener Keychain: [source: design/items/brewery_passport_book.md L157]

1. **Challenge-Based**: Win a drinking contest, complete a puzzle, pass a test
2. **Completion-Based**: Finish a tour, clear a dungeon, complete a questline
3. **Status-Based**: Reach a certain reputation level with the establishment
4. **Discovery-Based**: Find a hidden location or secret entrance

[source: design/items/brewery_passport_book.md L159-162]

### Stamp Collection Process
1. Meet the unlock condition at a brewery/pub
2. NPC offers to stamp your passport
3. **Animation**: Stamp pressed onto page (satisfying sound effect)
4. **Notification**: "STAMP COLLECTED! [Location Name]"
5. **Unlock**: Signature beer now available for purchase
6. **Progress Update**: City completion percentage updates

[source: design/items/brewery_passport_book.md L164-170] (Author ruling: the stamp is earned by challenge completion, not by ordering [source: design/quests/general_quests/brewerytour.md L52].)

### Stamp Permanence
- Stamps are permanent once collected
- Cannot be lost, traded, or removed
- Persist across save files (tied to account, not individual save)
- Stamp date/time recorded for bragging rights

[source: design/items/brewery_passport_book.md L172-176]

---

## Brewmaster Selfies — The Scrapbook

The passport's selfie gallery is canonically the bros' scrapbook. [source: design/quests/general_quests/brewerytour.md L66]

- **Chadwick posts each selfie to his feed** as the tour progresses — ties into the existing in-fiction feed content, **#EuroboundMoments**. [source: design/quests/general_quests/brewerytour.md L67-68]
- Album viewable at hostels / Wi-Fi cafés. Bartenders react to specific poses when shown the album. Charm dialogue bonuses scale with how obviously staged the photos look. [source: design/quests/general_quests/brewerytour.md L69-70]
- Per-city payoff: completing a city's 4 selfies feeds the **"Brewery Bro Safari"** auto-generated 15-second compilation (Y2K VHS filter, MIDI Hamster Dance audio, grid finale: "European Beer Experts 🍺"). [source: design/quests/general_quests/brewerytour.md L71-73]
- Full-collection reward: **"Photogenic Drinker"** — permanent +1 Hungover resistance, −10% Hungover duration, stacks with Continental Beer Master. [source: design/quests/general_quests/brewerytour.md L74-75]

Each brewery's specific selfie spot, pose, and NPC variant lives in that brewery's own item docs (`design/items/brewery_tour/`) — this book only tracks whether a given selfie has been collected.

---

## City Pages (Stamp-Slot Pages)

### Publandia (4 slots)
| Slot | Location | Stamp Design | Signature Beer |
|---|---|---|---|
| 1 | The Blarney Trap | Celtic harp, emerald ink | The Sweet Surrender |
| 2 | The Stoutworks Brewery | Copper still, bronze ink | Vat Master's Reserve |
| 3 | Trinity of Pints | Scholarly cap, navy ink | Academic Amber |
| 4 | Shenanigans | Wilted clover, faded gold ink | The Fool's Gold |

**Page Theme**: Emerald green background, Celtic knot borders [source: design/items/brewery_passport_book.md L113]
**Legendary Hangover**: "The Full Irish Experience" [source: design/quests/general_quests/brewerytour.md L89]
**Item docs**: `stamp_blarney_trap`, `stamp_stoutworks_brewery`, `stamp_trinity_of_pints`, `stamp_shenanigans` (full detail in `design/items/brewery_tour/`)

### Debaucheryville (4 slots)
| Slot | Location | Stamp Design | Signature Beer |
|---|---|---|---|
| 1 | The Absinthium Taproom | Green fairy in cracked glass, shifting emerald ink | Absinthe Lager |
| 2 | The Tap Dat Vault | Soundwave in vault door, electric cyan/hot pink ink | Vape Stout |
| 3 | Three-Crown Keg Haus | Three rusted crowns over stein, rust-orange ink | Iron Gut Tripel |
| 4 | Ye Olde B.R.E.W. Lab | Pixelated hop cone with blockchain hash, neon blue ink | Blockchain Bock |

**Page Theme**: Neon purple background, absinthe bottle borders with circuitry accents [source: design/items/brewery_passport_book_complete.md L246]
**Legendary Hangover**: "The Neon Nightmare" [source: design/quests/general_quests/brewerytour.md L90]
**Item docs**: `stamp_absinthium_taproom`, `stamp_tap_dat_vault`, `stamp_three_crown_keg_haus`, `stamp_ye_olde_brew_lab`

### Sinfonia (4 slots)
| Slot | Location | Stamp Design | Signature Beer |
|---|---|---|---|
| 1 | The Moderato Pub | Metronome over stein, warm amber ink | Tempo Tantrum |
| 2 | The Standing Ovation | Theater masks clinking steins, crimson/gold ink | Curtain Call Copper |
| 3 | Crown & Cask | Habsburg crown over barrel, royal purple ink | Heir Apparent Ale |
| 4 | The Dancing Stein | Stein with dancing legs, ballroom gold ink | Waltz Weizen |

**Page Theme**: Golden background, musical note and crown borders with baroque flourishes [source: design/items/brewery_passport_book_complete.md L328]
**Legendary Hangover**: "Imperial Concerto" (inflicts "Imperial Hangover") [source: design/quests/general_quests/brewerytour.md L91]
**Item docs**: `stamp_moderato_pub`, `stamp_standing_ovation`, `stamp_crown_and_cask`, `stamp_dancing_stein`

### Shamsterdam (4 slots — reserved)
| Slot | Location | Stamp Design | Signature Beer |
|---|---|---|---|
| 1 | slots reserved — names pending author minting | — | — |
| 2 | slots reserved — names pending author minting | — | — |
| 3 | slots reserved — names pending author minting | — | — |
| 4 | slots reserved — names pending author minting | — | — |

**Page Theme**: pending author minting — Shamsterdam is out of scope for this decomposition round [source: docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md, Shamsterdam parking lot]
**Legendary Hangover**: "Canal Courage" (name retained; a CONSUMABLE like the other three cities' hangovers, not a permanent passive — author ruling) [source: design/quests/general_quests/brewerytour.md L92-93]

The two existing Shamsterdam establishment names in the legacy docs ("Brouwerij de Molen" — a real Dutch brewery — and "Proeflokaal 't Kansen") fail the satire bar and are queued for author rename, alongside two entirely new establishments; none of the four Shamsterdam brewery names are canon yet. [source: design/quests/general_quests/brewerytour.md L19-23]

---

## Progression & Rewards

| Milestone | Reward |
|---|---|
| Each brewery | Stamp + brewmaster selfie + opener + signature beer unlocked |
| City complete (4/4) | That city's Legendary Hangover — a named consumable |
| All 16 breweries | **Continental Beer Master** — permanent +1 to all alcohol-based item effects |
| All selfies | **Photogenic Drinker** — permanent +1 Hungover resistance, −10% Hungover duration |

[source: design/quests/general_quests/brewerytour.md L79-93] — 16 breweries total (4 cities × 4), per the master spec's authoritative ruling. The legacy base/complete files' conflicting fourteen-stamp and eighteen-stamp totals (tied to the dead bottle-opener-vendor and Shamsterdam-6-stamp models) are superseded and not carried forward.

---

## Implementation Notes

### Technical Requirements
- Menu system integration (new tab)
- Stamp collection tracking (per-location flags)
- Beer unlock system (inventory additions)
- Achievement tracking (city and continental)
- Selfie gallery (image collection)

### Save Data
- Stamps saved to profile (persist across saves)
- Beer unlocks tied to stamps
- Selfie collection separate tracking
- Achievement progress persistent

### UI/UX Priorities
1. Satisfying stamp animation
2. Clear progress indicators
3. Easy navigation between cities
4. Quick access to unlocked beers
5. Celebratory feedback on completions

[source: design/items/brewery_passport_book.md L310-330]

---

## PNG Asset Requirements

### Book Assets
- `passport_book_closed.png` — 128x128 — Cover view
- `passport_book_open.png` — 512x384 — Full spread
- `passport_page_publandia.png` — 256x384 — City page
- `passport_page_debaucheryville.png` — 256x384 — City page
- `passport_page_sinfonia.png` — 256x384 — City page
- `passport_spine.png` — 32x384 — Book spine detail
- `bookmark_hop.png` — 32x64 — Hop leaf bookmark

[source: design/items/brewery_passport_book.md L336-344 — `passport_page_shamsterdam.png` omitted here; Shamsterdam page art is pending author minting and out of scope this round]

### Stamp Assets (Generic)
- `stamp_slot_empty.png` — 64x64 — Placeholder (unearned slot)
- `stamp_slot_locked.png` — 64x64 — Undiscovered (matches the "[LOCKED]" state in the Book Open View mockup above)

[source: design/items/brewery_passport_book.md L351-352 — per-brewery stamp faces and their animation sheets are specified in each collectible's own item doc under `design/items/brewery_tour/`, not duplicated here; this generic pair is the only Stamp Assets content that belongs at the container level]

### Achievement Assets
- `legendary_hangover_publandia.png` — 48x48
- `legendary_hangover_debaucheryville.png` — 48x48
- `legendary_hangover_sinfonia.png` — 48x48
- `continental_beer_master_badge.png` — 96x96
- `photogenic_drinker_badge.png` — 64x64

[source: design/items/brewery_passport_book.md L365-371 — `legendary_hangover_shamsterdam.png` (48x48) omitted here; Shamsterdam's hangover icon is pending author minting and out of scope this round, per the same reservation as the Book Assets section above]

### UI Assets
- `passport_tab_icon.png` — 32x32 — Menu icon
- `passport_notification.png` — 24x24 — New stamp available
- `progress_bar_city.png` — 128x16 — City completion
- `progress_bar_continental.png` — 256x16 — Overall progress
- `selfie_spot_marker.png` — 32x32 — In-world indicator
- `selfie_gallery_frame.png` — 192x256 — Photo display
- `stamp_collected_popup.png` — 256x128 — Notification
- `beer_unlocked_popup.png` — 256x128 — Notification

[source: design/items/brewery_passport_book.md L373-381]

Per-brewery stamp, opener, and signature-beer PNG assets are specified in each collectible's own item doc under `design/items/brewery_tour/`, not duplicated here.

---

## Notes
- Menu Integration section above (Access Location + all three Interface Layout ASCII mockups) is copied verbatim from `design/items/brewery_passport_book.md` L21-99, per the Task 7 brief.
- Achievement/Legendary-Hangover full stat blocks are out of scope for this file — they belong to the per-city quest files (not yet written) referenced by the master spec.
- The stray copy `design/worlds/publandia/brewery_passport_book.md` supplied the "Graduate (Senior Thesis)" Trinity of Pints variant, since superseded entirely by the Trinity redesign (author ruling; see `design/items/brewery_tour/stamp_trinity_of_pints_item.md`); nothing from the stray copy needed re-pulling here.

---

*The Brewery Passport Book: proof that you didn't just visit Europe — you DRANK it. One stamp at a time. One hangover at a time. Continental Beer Master isn't a title. It's a lifestyle choice.* [source: design/items/brewery_passport_book.md L385, adapted]
