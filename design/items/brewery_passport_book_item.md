# The Brewery Tour Passport Book

- **Item ID**: `brewery_passport_book`
- **Type**: permanent collectible + dedicated menu interface (the stamp book / scrapbook item)
- **Granted**: with the Bottle Opener Keychain and the first brewery's opener when the bros order the special beer at the first brewery in Publandia — the tour's one-time trigger. NEVER sold. [source: design/quests/general_quests/brewerytour.md, The Trigger]

*Your leather-bound ticket to the Continental Beer Trail — collect stamps, unlock beers, become legend* [source: design/items/brewery_passport_book.md L3]

## Seamus's Introduction

*"This book? It's your passport to the real beer culture of Europe. Every brewery, every pub worth its salt — they'll stamp you. Proves you were there. REALLY there. Fill a city's page, you earn their Legendary Hangover. Fill the whole book? Continental Beer Master. That's not just a title. That's a LIFESTYLE."* [source: design/items/brewery_passport_book_complete.md L17]

## Menu Integration

### Access Location
**Pause Menu → "Brewery Passport" tab** [source: design/items/brewery_passport_book.md L24]
- New tab appears in pause menu once book is acquired [source: design/items/brewery_passport_book.md L25]
- Icon: Leather book with hop leaf bookmark [source: design/items/brewery_passport_book.md L26]
- Notification badge when new stamp is available [source: design/items/brewery_passport_book.md L27]

### Interface Layout

**Main View (Book Closed)** [source: design/items/brewery_passport_book.md L31-44]
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

**Book Open View (City Selection)** [source: design/items/brewery_passport_book.md L46-72]
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

**Stamp Detail View (When Selected)** [source: design/items/brewery_passport_book.md L74-99]
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

## Stamp-Slot Pages

One page per city, four stamp slots per page — 4 cities × 4 breweries, 16 stamps total [source: design/quests/general_quests/brewerytour.md, Overview]. Per-stamp designs, inks, animations, stampers, and speeches live in the per-stamp item files in `design/items/brewery_tour/`.

## Stamp Mechanics

### Challenge Formats
Stamps are earned on challenge completion at each brewery, never on ordering (author ruling 2026-08-04). Challenge unlock conditions come in four archetypes [source: design/items/brewery_passport_book.md L159-162; the source's keychain-possession requirement is DEAD per the author's gating ruling]:

1. **Challenge-Based**: Win a drinking contest, complete a puzzle, pass a test
2. **Completion-Based**: Finish a tour, clear a dungeon, complete a questline
3. **Status-Based**: Reach a certain reputation level with the establishment
4. **Discovery-Based**: Find a hidden location or secret entrance

### Stamp Collection Process [source: design/items/brewery_passport_book.md L164-170]
1. Meet the unlock condition at a brewery/pub
2. NPC offers to stamp your passport
3. **Animation**: Stamp pressed onto page (satisfying sound effect)
4. **Notification**: "STAMP COLLECTED! [Location Name]"
5. **Unlock**: Signature beer now available for purchase
6. **Progress Update**: City completion percentage updates

### Stamp Permanence [source: design/items/brewery_passport_book.md L172-176]
- Stamps are permanent once collected
- Cannot be lost, traded, or removed
- Persist across save files (tied to account, not individual save)
- Stamp date/time recorded for bragging rights

## The Selfie Gallery (the Bros' Scrapbook)

- The passport's selfie gallery is canonically the bros' **scrapbook** [source: design/quests/general_quests/brewerytour.md, Selfie/Scrapbook Layer]
- Each brewery's brewmaster selfie is earned on challenge completion — the honor of a photo WITH the brewmaster [source: design/quests/general_quests/brewerytour.md, The Loop]
- **Chadwick posts each selfie to his feed** as the tour progresses (#EuroboundMoments) [source: design/quests/general_quests/brewerytour.md, Selfie/Scrapbook Layer]
- Album viewable at hostels / Wi-Fi cafés; bartenders react to specific poses when shown the album; Charm dialogue bonuses scale with how obviously staged the photos look [source: design/quests/general_quests/brewerytour.md, Selfie/Scrapbook Layer]

## PNG Assets

### Book Assets (8 PNGs) [source: design/items/brewery_passport_book.md L340-348]
- `passport_book_closed.png` — 128x128 — Cover view
- `passport_book_open.png` — 512x384 — Full spread
- `passport_page_publandia.png` — 256x384 — City page
- `passport_page_debaucheryville.png` — 256x384 — City page
- `passport_page_sinfonia.png` — 256x384 — City page
- `passport_page_shamsterdam.png` — 256x384 — City page
- `passport_spine.png` — 32x384 — Book spine detail
- `bookmark_hop.png` — 32x64 — Hop leaf bookmark

### Shared Stamp-Slot Assets [source: design/items/brewery_passport_book.md L354-356]
- `stamp_slot_empty.png` — 64x64 — Placeholder
- `stamp_slot_locked.png` — 64x64 — Undiscovered
- (Per-brewery stamp, beer, and opener PNGs live in their item files in `design/items/brewery_tour/`)

### Achievement Assets (6 PNGs) [source: design/items/brewery_passport_book.md L368-374]
- `legendary_hangover_publandia.png` — 48x48
- `legendary_hangover_debaucheryville.png` — 48x48
- `legendary_hangover_sinfonia.png` — 48x48
- `legendary_hangover_shamsterdam.png` — 48x48
- `continental_beer_master_badge.png` — 96x96
- `photogenic_drinker_badge.png` — 64x64

### UI Assets (8 PNGs) [source: design/items/brewery_passport_book.md L377-385]
- `passport_tab_icon.png` — 32x32 — Menu icon
- `passport_notification.png` — 24x24 — New stamp available
- `progress_bar_city.png` — 128x16 — City completion
- `progress_bar_continental.png` — 256x16 — Overall progress
- `selfie_spot_marker.png` — 32x32 — In-world indicator
- `selfie_gallery_frame.png` — 192x256 — Photo display
- `stamp_collected_popup.png` — 256x128 — Notification
- `beer_unlocked_popup.png` — 256x128 — Notification

## Signature Beer Unlock Availability

Each stamp unlocks that location's signature beer as a purchasable consumable [source: design/items/brewery_passport_book.md L182-186]:
- Available at the originating location
- Some available at The Blarney Trap (Publandia hub)
- Cross-city availability for completed stamps

Global stat guideline ranges (the 8–15 Sovs price band is a GUIDELINE, not a rule — author ruling, Contradiction 3) [source: design/items/brewery_passport_book.md L188-195]: +25 to +50 HP, +0 to +20 SP, location-specific buff, 5–15% minor debuff risk.

## Implementation Notes [source: design/items/brewery_passport_book.md L364-374 region]

- Menu system integration (new tab); stamp collection tracking (per-location flags); beer unlock system (inventory additions); achievement tracking (city and continental); selfie gallery (image collection)
- Save data: stamps saved to profile (persist across saves); beer unlocks tied to stamps; selfie collection separate tracking; achievement progress persistent
- UI/UX priorities: satisfying stamp animation; clear progress indicators; easy navigation between cities; quick access to unlocked beers; celebratory feedback on completions

## Notes

- The base doc's acquisition (free with a keychain purchase, or a Pint-Off win) is superseded by the master spec's one-time Publandia special-beer-order trigger. City-completion and full-book rewards (Legendary Hangovers, Continental Beer Master, Photogenic Drinker) are quest-layer — see `design/quests/general_quests/brewerytour.md` and the per-city quest files.
- The Stamp Detail View mockup's "Acquired: Won Pint-Off Challenge" line is a UI example copied verbatim from the base doc; actual acquisition text per stamp comes from that brewery's challenge (⚠ AUTHOR TO DESIGN per city quest files).
