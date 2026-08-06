> ⚠ SUPERSEDED 2026-08-05 — decomposed into design/items/brewery_tour/, design/items/brewery_passport_book_item.md, bottle_opener_keychain_item.md, and the quests/<city>/brewerytour<city>.md files per docs/superpowers/specs/2026-08-05-brewery-tour-decomposition-design.md. Kept for provenance; do not edit.

# The Brewery Passport Book

*Your leather-bound ticket to the Continental Beer Trail — collect stamps, unlock beers, become legend*

## System Overview

### What Is It?
The Brewery Passport Book is a collectible menu item that tracks the player's progress through the Brewery Tour sidequest. It functions as both a physical in-game item and a dedicated menu interface, displaying stamps collected from breweries and pubs across all cities in the game.

### Acquisition
- **Location**: The Blarney Trap, Publandia
- **Method**: Given FREE with purchase of the Bottle Opener Keychain (15 Sovs) OR as reward for winning a Pint-Off challenge
- **Requirement**: Cannot participate in Brewery Tour without both items
- **Timing**: Available from first visit to The Blarney Trap

### Seamus's Introduction
*"This book? It's your passport to the real beer culture of Europe. Every brewery, every pub worth its salt — they'll stamp you. Proves you were there. REALLY there. Fill a city's page, you earn their Legendary Hangover. Fill the whole book? Continental Beer Master. That's not just a title. That's a LIFESTYLE."*

---

## Menu Integration

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

## City Pages

### Publandia (4 Stamps)
| Slot | Location | Stamp Design | Signature Beer | Unlock Condition |
|------|----------|--------------|----------------|------------------|
| 1 | The Blarney Trap | Celtic harp, emerald ink | The Sweet Surrender | Pint-Off/Toast/Regular status |
| 2 | The Stoutworks Brewery | Copper still, bronze ink | Vat Master's Reserve | Complete tour or dungeon |
| 3 | Trinity of Pints | Scholarly cap, navy ink | Academic Amber | Complete drinking lecture |
| 4 | [TBD] | [TBD] | [TBD] | [TBD] |

**Page Theme**: Emerald green background, Celtic knot borders
**Legendary Hangover**: "Publandia Legendary Hangover" (+15 all stats, inflicts Legendary Hungover post-battle)

### Debaucheryville (4 Stamps)
| Slot | Location | Stamp Design | Signature Beer | Unlock Condition |
|------|----------|--------------|----------------|------------------|
| 1 | [TBD - Main Brewery] | [TBD] | [TBD] | [TBD] |
| 2 | [TBD - Pub/Bar] | [TBD] | [TBD] | [TBD] |
| 3 | [TBD - Pub/Bar] | [TBD] | [TBD] | [TBD] |
| 4 | [TBD - Pub/Bar] | [TBD] | [TBD] | [TBD] |

**Page Theme**: Neon purple background, absinthe bottle borders
**Legendary Hangover**: "Debaucheryville Legendary Hangover" (unique effects TBD)

### Sinfonia (4 Stamps)
| Slot | Location | Stamp Design | Signature Beer | Unlock Condition |
|------|----------|--------------|----------------|------------------|
| 1 | [TBD - Brewery] | [TBD] | [TBD] | [TBD] |
| 2 | [TBD - Wine Bar?] | [TBD] | [TBD] | [TBD] |
| 3 | [TBD] | [TBD] | [TBD] | [TBD] |
| 4 | [TBD] | [TBD] | [TBD] | [TBD] |

**Page Theme**: Golden background, musical note borders
**Legendary Hangover**: "Sinfonia Legendary Hangover" (unique effects TBD)

### Shamsterdam — Expansion (4 + 2 Bonus Stamps)
| Slot | Location | Stamp Design | Signature Beer | Unlock Condition |
|------|----------|--------------|----------------|------------------|
| 1 | Brouwerij de Molen | Windmill, orange ink | Molen's Midnight | Complete brewery challenge |
| 2 | Proeflokaal 't Kansen | Tilted glass, amber ink | Liquid Courage | Drinking game victory |
| 3 | [TBD] | [TBD] | [TBD] | [TBD] |
| 4 | [TBD] | [TBD] | [TBD] | [TBD] |
| 5 (Bonus) | [TBD] | [TBD] | [TBD] | [TBD] |
| 6 (Bonus) | [TBD] | [TBD] | [TBD] | [TBD] |

**Page Theme**: Orange background, tulip/windmill borders
**Legendary Hangover**: "Shamsterdam Legendary Hangover" (unique effects TBD)
**Expansion Bonus**: 2 additional stamps beyond the standard 4

---

## Stamp Mechanics

### How Stamps Are Earned
Each brewery/pub has a specific unlock condition that must be met WHILE possessing the Bottle Opener Keychain:

1. **Challenge-Based**: Win a drinking contest, complete a puzzle, pass a test
2. **Completion-Based**: Finish a tour, clear a dungeon, complete a questline
3. **Status-Based**: Reach a certain reputation level with the establishment
4. **Discovery-Based**: Find a hidden location or secret entrance

### Stamp Collection Process
1. Meet the unlock condition at a brewery/pub
2. NPC offers to stamp your passport
3. **Animation**: Stamp pressed onto page (satisfying sound effect)
4. **Notification**: "STAMP COLLECTED! [Location Name]"
5. **Unlock**: Signature beer now available for purchase
6. **Progress Update**: City completion percentage updates

### Stamp Permanence
- Stamps are permanent once collected
- Cannot be lost, traded, or removed
- Persist across save files (tied to account, not individual save)
- Stamp date/time recorded for bragging rights

---

## Signature Beers

### Unlock System
Each stamp unlocks that location's signature beer as a purchasable consumable:
- Available at the originating location
- Some available at The Blarney Trap (Publandia hub)
- Cross-city availability for completed stamps

### Beer Stats Template
| Attribute | Range |
|-----------|-------|
| HP Restoration | +25 to +50 |
| SP Restoration | +0 to +20 |
| Special Effect | Location-specific buff |
| Status Risk | 5-15% chance of minor debuff |
| Price | 8 Sovs to 15 Sovs |

### Publandia Signature Beers (Detailed)

**The Sweet Surrender (The Blarney Trap)**
- Style: Irish Stout
- ABV: 5.2%
- Stats: +35 HP, +10 SP
- Effect: "Comfortable Trap" — +10% Bravado retention (1 hour)
- Risk: 5% "Contentment" (reduced urgency)
- Price: 8 Sovs
- Flavor: "You surrendered to Blarney Trap pricing. It's delicious."

**Vat Master's Reserve (The Stoutworks Brewery)**
- Style: Imperial Stout (whiskey barrel aged)
- ABV: 9.5%
- Stats: +40 HP, +15 SP
- Effect: 10% "Fermented Fury" (+15% Attack next battle)
- Risk: 10% "The Vat's Whisper" (cosmetic yeast thoughts)
- Price: 12 Sovs
- Flavor: "Aged during the incident. Tastes like existential crisis."
- Negotiate Route Bonus: +5% enemy negotiation success

**Academic Amber (Trinity of Pints)**
- Style: Irish Red Ale
- ABV: 4.8%
- Stats: +25 HP, +20 SP
- Effect: "Scholar's Focus" — temporary INT boost (+3 for 30 min)
- Risk: 10% "Pretentious" (dialogue options become insufferable)
- Price: 9 Sovs
- Flavor: "Brewed for minds that think they're smarter when drinking. They're not. But it helps."

**[Fourth Beer TBD]**
- Details pending fourth Publandia location

---

## Legendary Hangovers

### City Completion Rewards
Collecting all 4 stamps in a city unlocks that city's "Legendary Hangover" — a powerful consumable with significant benefits and consequences.

### Publandia Legendary Hangover
**"The Full Irish Experience"**
- **Unlock**: All 4 Publandia stamps
- **Effect**: +15 to ALL stats for entire battle
- **Consequence**: "Legendary Hungover" status after battle
- **Legendary Hungover**: -10 all stats for 30 minutes
- **Cure**: Full Irish Breakfast, sleep, or waiting
- **Price**: 50 Sovs (repurchasable from any stamped Publandia location)
- **Flavor**: "Four stamps. Four surrenders. The night of your life has a morning after."

### Using Legendary Hangovers Strategically
- Best used for boss fights or difficult encounters
- Plan for the aftermath (have cure ready)
- Multiple Legendary Hangovers can be stacked (not recommended)
- "Legendary Hungover" does not stack (one instance at a time)

---

## Continental Beer Master

### Achievement Requirements
- Collect ALL stamps from ALL cities
- Base game: 16 stamps (4 cities × 4 stamps)
- With expansion: 18 stamps (includes Shamsterdam bonus)

### Reward: Permanent +1 to All Alcohol-Based Items
This affects:
- All HP restoration from beer/alcohol items
- All SP restoration from beer/alcohol items
- All buff durations from beer/alcohol items
- All "chance of" effects from beer/alcohol items (improved by 1%)

### Additional Rewards
- **Title**: "Continental Beer Master" displayed on character
- **Dialogue**: NPCs at breweries/pubs recognize achievement
- **Discount**: 10% off all alcohol purchases everywhere
- **Secret**: Unlocks "The Master's Toast" — ultimate toast speech option

### The Master's Toast
- Available only to Continental Beer Masters
- Automatically wins any toast speech challenge
- Grants "Legendary Craic" status to entire party (+all stats, 10 min)
- Single use per game day (resets at midnight)

---

## Brewmaster Selfies

### Bonus Collectible Layer
Each brewery/pub has a designated "selfie spot" where players can take a commemorative photo.

### Selfie Collection
| City | Location | Selfie Spot | Special Variant |
|------|----------|-------------|-----------------|
| Publandia | The Blarney Trap | Fireplace with shamrocks | With Seamus (Regular status) |
| Publandia | The Stoutworks | Copper Cathedral | With Vat Master (negotiate route) |
| Publandia | Trinity of Pints | Graduation podium | In scholar's robes |
| Publandia | [TBD] | [TBD] | [TBD] |

### Selfie Mechanics
1. Find the selfie spot (marked with camera icon)
2. Interact to take photo
3. Photo added to passport's selfie gallery
4. Optional: Special variants for completing certain conditions

### Full Selfie Collection Reward
**"Photogenic Drinker"**
- Passive +1 resistance to "Hungover" debuff permanently
- Reduces Hungover duration by 10%
- Stack with Continental Beer Master for maximum efficiency

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

---

## PNG Asset Requirements

### Book Assets (8 PNGs)
- passport_book_closed.png - 128x128 - Cover view
- passport_book_open.png - 512x384 - Full spread
- passport_page_publandia.png - 256x384 - City page
- passport_page_debaucheryville.png - 256x384 - City page
- passport_page_sinfonia.png - 256x384 - City page
- passport_page_shamsterdam.png - 256x384 - City page (expansion)
- passport_spine.png - 32x384 - Book spine detail
- bookmark_hop.png - 32x64 - Hop leaf bookmark

### Stamp Assets (20+ PNGs)
- stamp_blarney_trap.png - 64x64
- stamp_stoutworks.png - 64x64
- stamp_trinity_pints.png - 64x64
- stamp_[fourth_publandia].png - 64x64
- stamp_slot_empty.png - 64x64 - Placeholder
- stamp_slot_locked.png - 64x64 - Undiscovered
- stamp_animation.png - 64x64x4 - Stamping sequence
- [Additional stamps for other cities]

### Beer Assets (16+ PNGs)
- sweet_surrender_bottle.png - 32x64
- sweet_surrender_icon.png - 32x32
- vat_masters_reserve_bottle.png - 32x64
- vat_masters_reserve_icon.png - 32x32
- academic_amber_bottle.png - 32x64
- academic_amber_icon.png - 32x32
- [Additional beers for all locations]

### Achievement Assets (6 PNGs)
- legendary_hangover_publandia.png - 48x48
- legendary_hangover_debaucheryville.png - 48x48
- legendary_hangover_sinfonia.png - 48x48
- legendary_hangover_shamsterdam.png - 48x48
- continental_beer_master_badge.png - 96x96
- photogenic_drinker_badge.png - 64x64

### UI Assets (8 PNGs)
- passport_tab_icon.png - 32x32 - Menu icon
- passport_notification.png - 24x24 - New stamp available
- progress_bar_city.png - 128x16 - City completion
- progress_bar_continental.png - 256x16 - Overall progress
- selfie_spot_marker.png - 32x32 - In-world indicator
- selfie_gallery_frame.png - 192x256 - Photo display
- stamp_collected_popup.png - 256x128 - Notification
- beer_unlocked_popup.png - 256x128 - Notification

---

*The Brewery Passport Book: More than a collectible. More than a tracker. It's proof that you didn't just visit Europe — you DRANK it. One stamp at a time. One hangover at a time. Continental Beer Master isn't a title. It's a lifestyle choice.*
