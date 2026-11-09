# The Tap Dat Vault Location Package Design

## Intent and Identity

Define The Tap Dat Vault as Brewery Tour location three, a midnight-only cyberpunk cellar with rhythm and vapor-pressure challenges.

- Location ID: `debaucheryville_clocktower_tapdatvault_brewery_02`
- Slug: `tap_dat_vault`
- NPC folder: `Tap_Dat_Vault`
- Primary source: `the_tap_dat_vault.md`

## Visual and Spatial Design

Because no separate Clocktower Plaza package exists in this program, Tap Dat Vault owns its plaza-side approach node, concealed switch, countdown glyphs, neon-graffitied vault door, and the interior once activated. The basement uses brewing vats as subwoofers, circuit-filled fermentation chambers, a neon grid, and a DJ/livestream station facing the challenge floor, bar, Brewmistress arena, selfie wall, and return vault.

Nodes must separate the timing of the exterior midnight gate from the internal rhythm puzzle. Bass pulse, strobe, vapor, and neon effects need reduced-flash, reduced-motion, and visual rhythm substitutes.

## Gameplay, Quests, and State

The switch activates at 00:00 and accepts first entry through 00:59; three failed rhythm attempts eject the party until the next midnight window. No opener gates entry or ordinary service. Completing the rhythm/Brewmistress challenge while the tour is active and `bottle_opener_keychain` is present earns `opener_tap_dat_vault` and `stamp_tap_dat_vault`; the opener is never sold. It also unlocks the 14-Sov `beer_tap_dat_vault` purchase and `You Are Brewtiful` selfie wall. A pre-tour completion stores the challenge flag and grants those rewards on the first eligible return interaction without replay. The location also owns the Glitched Brew Ad Bot, local rewards, and return.

`brewerytourdebaucheryville.md` owns sequence progression and cross-brewery dialogue.

## Package Directives

Interactions define the recurring midnight window, switch state, rhythm cues, pressure controls, strike/ejection flow, encounter triggers, service, selfie, and exit. Items reference `bottle_opener_keychain` plus the authoritative opener, stamp, and beer files. Older Blarney checks and the €20 opener purchase are deprecated. NPCs include the Brewmistress and documented bots/patrons. PNG/mapping cover plaza approach, switch/countdown/vault states, cellar faces, vats, chambers, neon grid, DJ station, ad bot, boss, bar, opener/stamp/brew/selfie UI, vapor, and safe cue variants.

## Validation

- The 00:00-00:59 entry window, three-strike ejection, and next-midnight retry agree across files.
- Rhythm play remains solvable without audio or strobe cues.
- Tour stamp, brew, selfie, puzzle, and boss states are distinct.
- The Tap Dat package owns the plaza-side switch because no separate Plaza package exists.
- Brewery order identifies this as stop three.
- Brewery order identifies this as stop two.
