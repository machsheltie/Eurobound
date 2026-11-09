# Three-Crown Keg Haus Location Package Design

## Intent and Identity

Define Three-Crown Keg Haus as Brewery Tour location two, a royal-dive-bar stealth dungeon near Shadow Exchange.

- Location ID: `debaucheryville_shadowexchange_threecrownkeghaus_brewery_03`
- Slug: `three_crown_keg_haus`
- NPC folder: `Three_Crown_Keg_Haus`
- Primary source: `three_crown_keghaus.md`

## Visual and Spatial Design

A shadowed alley and rusting three-crown sign lead into a cramped, sticky dive bar lit by beer-foam sconces and an empty-keg chandelier. Moldy patched booths, mismatched furniture, passed-out patrons, creaky floor tiles, service bar, patrol lanes, Keg Sentinel arena, and a velvet keg throne form the playable route.

The graph must encode safe/unsafe floor tiles and patron obstacles independently of their art so the stealth puzzle remains deterministic. Shadow Exchange is a nearby discovery/referral node, not an interior connection.

## Gameplay, Quests, and State

After discovery, the Keg Haus is always accessible but requires +1 Bravado to cross the threshold. No opener gates the door or ordinary service. Completing the stealth/Keg Sentinel challenge while the tour is active and `bottle_opener_keychain` is present earns `opener_three_crown_keg_haus` and `stamp_three_crown_keg_haus`; the opener is never sold. It also unlocks the 10-Sov `beer_three_crown_keg_haus` purchase and Velvet Keg Throne selfie. A pre-tour completion stores the challenge flag and grants those rewards on the first eligible return interaction without replay. The location also owns Slurring Bar Flies, rewards, and return.

## Package Directives

Interactions define Bravado check, floor/patron detection, encounters, service, selfie, and exits. Environment covers haze and low light with high-readability stealth cues. Items reference `bottle_opener_keychain` plus the authoritative opener, stamp, and beer files. Older Blarney checks and the €15 opener purchase are deprecated. NPCs include bartender/service roles, Bar Flies, Sentinel, and patrons. PNG/mapping cover alley/door, room faces, tile states, obstacles, booths, keg chandelier, throne, characters, stealth UI, opener/stamp/brew/selfie UI, and accessibility overlays.

## Validation

- Discovery and Bravado entry remain distinct; no opener check is introduced.
- Safe-tile logic agrees between nodes, interactions, and art mapping.
- Shadow Exchange remains a referral/adjacent location.
- Tour order identifies this as stop two.
- Low-vision mode preserves stealth readability.
