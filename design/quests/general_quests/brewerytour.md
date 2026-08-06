# Brewery Tour Sidequest — Master Spec

**Status: CANONICAL SYSTEM (author-ruled 2026-08-04).** This file is the authority on how the
brewery tour works. City quest files (`quests/<city>/brewerytour<city>.md`) hold each city's
instances; item files hold the collectibles. Where an older doc contradicts this file, this
file wins.

---

## Overview

- **4 cities × 4 breweries = 16 breweries total** (author ruling)
- Debaucheryville: 4 designed (The Absinthium Taproom, Three-Crown Keg Haus, The Tap Dat
  Vault, Ye Olde B.R.E.W. Lab)
- Publandia: 4 designed (The Blarney Trap, The Stoutworks Brewery, Trinity of Pints, +1 per
  city file)
- Sinfonia: 4 designed (The Standing Ovation, Crown & Cask, The Dancing Stein, The Moderato
  Pub)
- Shamsterdam: **4 required, 0 named.** The two existing establishments carry placeholder
  names that fail the satire bar — one is a real brewery ("Brouwerij de Molen" — real Dutch
  brand, must be renamed) and "Proeflokaal 't Kansen" is generic Dutch with no joke. Both get
  author-minted renames (the jenever-distillery character and Kees stay; only names change),
  plus **2 entirely new establishments to be created**. All 4 names: OPEN AUTHOR DECISION.

---

## The Trigger (once, Publandia)

The quest does not exist for the player until this fires:

1. At the first brewery in Publandia, the bros must **order the special beer**.
2. That order is the triggering event. The establishment hands over:
   - **The Bottle Opener Keychain** (ONE item — the pre-loaded frat-bro keyring; see
     `bottle_opener_keychain` item doc)
   - **That brewery's bottle opener** (the first of 16)
   - **The Brewery Tour Passport Book** (the stamp book / scrapbook item)
3. The first stamp + brewmaster selfie are earned at this location through the standard loop
   below.

**Hard gate:** before the trigger, NO brewery anywhere will hand over stamps, sell special
beers, or give out openers. The tour is invisible until Publandia opens it.

---

## The Loop (every brewery, quest active)

1. **Order the special beer** → this triggers the brewery's **challenge**.
2. **The challenge is a micro-dungeon** (format varies by city — Debaucheryville's four are
   fully designed: themed obstacle/minigame → mini-mob → boss. Sinfonia trends
   performance/social challenges. Publandia trends drinking games. Shamsterdam TBD.)
3. **Completing the challenge earns, all at once:**
   - **The stamp** — applied to the passport (stamps are earned by challenge completion, not
     by ordering; author ruling)
   - **The brewmaster selfie** — the honor of a photo WITH the brewmaster, taken on
     completion. This is the brewery's selfie collectible.
   - **The brewery's bottle opener** — added to the keychain collection
   - **The signature beer unlocked** as a purchasable consumable from then on

**Dead mechanic (do not reintroduce):** ICQ scammers selling bottle openers. Openers are
earned at breweries only. (A scam gag where ICQ contacts sell FAKE openers is fair game.)

---

## The Selfie / Scrapbook Layer (author-confirmed KEEP)

- The passport's selfie gallery is canonically the bros' **scrapbook**.
- **Chadwick posts each selfie to his feed** as the tour progresses (ties into the existing
  in-fiction feed content, #EuroboundMoments).
- Album viewable at hostels / Wi-Fi cafés. Bartenders react to specific poses when shown the
  album. Charm dialogue bonuses scale with how obviously staged the photos look.
- Per-city payoff: completing a city's 4 selfies feeds the **"Brewery Bro Safari"**
  auto-generated 15-second compilation (Y2K VHS filter, MIDI Hamster Dance audio, grid
  finale: "European Beer Experts 🍺").
- Full-collection reward: **"Photogenic Drinker"** — permanent +1 Hungover resistance, −10%
  Hungover duration, stacks with Continental Beer Master.

---

## Rewards Ladder

| Milestone | Reward |
|---|---|
| Each brewery | Stamp + brewmaster selfie + opener + signature beer unlocked |
| City complete (4/4) | That city's **Legendary Hangover** — a named ultimate CONSUMABLE (author ruling: consumable model, with effects, consequences, cures, and repurchase source per city files) |
| All 16 breweries | **"Continental Beer Master"** — permanent +1 to all alcohol-based item effects |
| All selfies | **"Photogenic Drinker"** passive |

**The four Legendary Hangovers:**
- Publandia: **"The Full Irish Experience"**
- Debaucheryville: **"The Neon Nightmare"**
- Sinfonia: **"Imperial Concerto"** (inflicts "Imperial Hangover")
- Shamsterdam: **"Canal Courage"** (minted name retained; it is a CONSUMABLE like the others,
  not a permanent passive — author ruling)

---

## What Every Brewery Needs (flesh-out checklist)

When building or completing a brewery, it is DONE when all of these exist:

- [ ] **Challenge**: micro-dungeon or minigame — intro cutscene text, themed obstacle,
      mini-mob encounter, boss/final encounter
- [ ] **Special beer order beat**: the dialogue/scene where the bros order it (this is the
      challenge trigger)
- [ ] **Brewmaster NPC**: who they are, and the completion selfie staging/variant
- [ ] **Stamp**: visual design, ink color, stamp animation, stamp speech from the stamper
- [ ] **Bottle opener**: design, inscription, material gag
- [ ] **Signature beer**: full stat block (style, ABV, HP/SP effects, buff/debuff risk,
      price in Sovs, flavor text, "Brewed By", special quirk)
- [ ] **Selfie prop/pose**: the themed pose + how NPCs react to it
- [ ] **PNG asset list**: stamp sheet, beer bottle + icon, brewmaster/selfie assets

---

## Item Decomposition (target architecture, author-approved)

- `bottle_opener_keychain` — ONE item file (trigger/container; original doc in
  `design/items/bottle_opener_keychain_item.md` is the seed, pending its geography rewrite)
- One item file per **stamp** (16), per **opener** (16), per **signature beer** (16)
- The **passport book** — one item file: the physical book, menu-tab UI (ASCII mockups in the
  base passport doc), stamp-slot pages, account-level persistence
- Quest mechanics live HERE and in the per-city quest files — not in item docs

## File Map

The 16-brewery decomposition (item files, city quest files, templates) as of the 2026-08-05
quest-doc reconciliation pass.

### Item Files — Publandia (12)
- `design/items/brewery_tour/stamp_blarney_trap_item.md`
- `design/items/brewery_tour/opener_blarney_trap_item.md`
- `design/items/brewery_tour/beer_blarney_trap_item.md`
- `design/items/brewery_tour/stamp_stoutworks_brewery_item.md`
- `design/items/brewery_tour/opener_stoutworks_brewery_item.md`
- `design/items/brewery_tour/beer_stoutworks_brewery_item.md`
- `design/items/brewery_tour/stamp_trinity_of_pints_item.md`
- `design/items/brewery_tour/opener_trinity_of_pints_item.md`
- `design/items/brewery_tour/beer_trinity_of_pints_item.md`
- `design/items/brewery_tour/stamp_shenanigans_item.md`
- `design/items/brewery_tour/opener_shenanigans_item.md`
- `design/items/brewery_tour/beer_shenanigans_item.md`

### Item Files — Debaucheryville (12)
- `design/items/brewery_tour/stamp_absinthium_taproom_item.md`
- `design/items/brewery_tour/opener_absinthium_taproom_item.md`
- `design/items/brewery_tour/beer_absinthium_taproom_item.md`
- `design/items/brewery_tour/stamp_three_crown_keg_haus_item.md`
- `design/items/brewery_tour/opener_three_crown_keg_haus_item.md`
- `design/items/brewery_tour/beer_three_crown_keg_haus_item.md`
- `design/items/brewery_tour/stamp_tap_dat_vault_item.md`
- `design/items/brewery_tour/opener_tap_dat_vault_item.md`
- `design/items/brewery_tour/beer_tap_dat_vault_item.md`
- `design/items/brewery_tour/stamp_ye_olde_brew_lab_item.md`
- `design/items/brewery_tour/opener_ye_olde_brew_lab_item.md`
- `design/items/brewery_tour/beer_ye_olde_brew_lab_item.md`

### Item Files — Sinfonia (12)
- `design/items/brewery_tour/stamp_moderato_pub_item.md`
- `design/items/brewery_tour/opener_moderato_pub_item.md`
- `design/items/brewery_tour/beer_moderato_pub_item.md`
- `design/items/brewery_tour/stamp_standing_ovation_item.md`
- `design/items/brewery_tour/opener_standing_ovation_item.md`
- `design/items/brewery_tour/beer_standing_ovation_item.md`
- `design/items/brewery_tour/stamp_crown_and_cask_item.md`
- `design/items/brewery_tour/opener_crown_and_cask_item.md`
- `design/items/brewery_tour/beer_crown_and_cask_item.md`
- `design/items/brewery_tour/stamp_dancing_stein_item.md`
- `design/items/brewery_tour/opener_dancing_stein_item.md`
- `design/items/brewery_tour/beer_dancing_stein_item.md`

### Container Items (2)
- `design/items/bottle_opener_keychain_item.md`
- `design/items/brewery_passport_book_item.md`

### City Quest Files (3)
- `design/quests/publandia/brewerytourpublandia.md`
- `design/quests/debaucheryville/brewerytourdebaucheryville.md`
- `design/quests/sinfonia/brewerytoursinfonia.md`

### Templates
- `design/templates/stamp_item_template.md`
- `design/templates/opener_item_template.md`
- `design/templates/signature_beer_item_template.md`

Shamsterdam has no item files or city quest file yet — out of scope this round per the
extraction plan's Shamsterdam parking lot.

---

## Source Reconciliation

DONE 2026-08-05 — six legacy docs merged and retired to design/legacy/; coverage matrix in
docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md.

The six legacy docs (`design/legacy/brewery_passport_book.md`,
`brewery_passport_book_complete.md`, `brewery_passport_book_debaucheryville.md`,
`brewery_passport_book_sinfonia.md`, `brewery_tour_bottle_opener_system.md`, and
`brewery_passport_book_worlds_copy_2026-08-05.md`) held unique load-bearing content and
contradictions; every fact was walked against Appendix A of
`docs/superpowers/specs/2026-08-05-brewery-tour-decomposition-design.md` and resolved to a
new home, an author kill ruling, or an explicit Shamsterdam-out-of-scope deferral — the full
row-by-row Coverage Matrix lives in
`docs/superpowers/plans/2026-08-05-brewery-decomposition-extraction.md`. Known casualties
already ruled: per-location opener VENDORS (dead), ICQ opener sales (dead),
Shamsterdam-hangover-as-passive (dead), "one keychain gates everything with no per-brewery
openers" (dead — openers are per-brewery, earned not bought). The six files are kept for
provenance in `design/legacy/` with SUPERSEDED banners; do not edit them further — this spec
and the decomposed item/quest files are the live authority.
