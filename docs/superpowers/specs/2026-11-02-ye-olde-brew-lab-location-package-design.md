# Ye Olde B.R.E.W. Lab Location Package Design

## Intent and Identity

Define Ye Olde B.R.E.W. Lab as Brewery Tour location four and the technology-satire finale beneath Velvet Curtain Club.

- Location ID: `debaucheryville_velvetcurtain_brew_lab_01`
- Slug: `ye_olde_brew_lab`
- NPC folder: `Ye_Olde_BREW_Lab`
- Primary source: `ye_olde_brew_lab.md`

## Visual and Spatial Design

Velvet Curtain Club owns the dance-floor approach, Staff Only rope, QR pad exterior, and service-door transition. This package begins below in an L-shaped blue-lit lab: brewing vats and bioluminescent liquid on one leg, AI consoles and NFT flavor screens on the other, with LED floor paths, wired fermentation tanks, robotic bartender rails, taste-logic station, BrewBot arena, Algorithm Archive selfie terminal, tour counter, and return stair.

The graph must keep puzzle stations and boss lanes readable beneath screen and liquid effects. Reduced-flash, reduced-scroll, and high-contrast floor-path variants are required.

## Gameplay, Quests, and State

Hours are 22:00-04:00. Entry follows `brew_lab_entrance_discovered` and either the documented Bravado-2 bypass or bouncer-charm route, which sets `brew_lab_access_unlocked`. No opener gates entry or ordinary service. Completing the taste-profile/BrewBot challenge while the tour is active and `bottle_opener_keychain` is present earns `opener_ye_olde_brew_lab` and `stamp_ye_olde_brew_lab`; the opener is never sold. It also unlocks `beer_ye_olde_brew_lab` at 18 Sovs with a live plus/minus-5 volatility roll, the Algorithm Archive selfie, and the brewery-tour completion check. A pre-tour completion stores the challenge flag and grants those rewards on the first eligible return interaction without replay.

## Package Directives

Core separates club access, Lab threshold gate, challenge progression, purchase availability, and tour completion. Interactions bind current brewery, NFT, and couchsurf quest states without copying dialogue. Items reference `bottle_opener_keychain` plus the authoritative opener, stamp, and beer files; older Blarney checks and the €25 opener purchase are deprecated. NPCs include the bartender, algorithm entities, BrewBot, and documented service characters. PNG/mapping cover lab faces, vats, consoles, tanks, rail bartender, QR/door interior, minigame UI, enemies, boss, selfie/opener/stamp/brew UI, LED paths, and safe variants.

## Validation

- Velvet Curtain owns the approach; the Lab owns only the destination interior.
- Bravado/charm controls the transition; no opener check is introduced.
- Challenge completion awards the local opener and stamp together; Blockchain Bock uses the documented volatile price.
- Tour completion triggers only after the documented fourth stamp/outcome.
- NFT and couchsurf rewards remain quest-owned references.
- Brewery order identifies this as stop four.
