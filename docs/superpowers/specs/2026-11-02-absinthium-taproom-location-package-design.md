# The Absinthium Taproom Location Package Design

## Intent and Identity

Define the Taproom as Brewery Tour location one and a reality-distorting puzzle dungeon behind Absinthe Arcade.

- Location ID: `debaucheryville_brewery_absinthium_taproom_01`
- Slug: `absinthium_taproom`
- NPC folder: `Absinthium_Taproom`
- Primary source: `the_absinthium_taproom.md`

## Visual and Spatial Design

Absinthe Arcade owns the north-hall green curtain, vapor leak, warning plaque, approach, and discovery interaction. The Taproom begins beyond the veil with a short transition into the Distortion Den: impossible mirror extensions, fractured floor/ceiling reflections, absinthe-green vapor, central service point, navigation maze, mirror portal, Dr. Milos Vanek's position, selfie chalice, and Green Fairy confrontation space.

The spatial graph must describe objective topology separately from deceptive visual presentation. Each mirror route needs a stable node connection even when reflections imply false space. Accessibility states reduce warping, chromatic displacement, and mirror motion while retaining puzzle cues.

## Gameplay, Quests, and State

The location operates 20:00-04:00 and consumes `absinthium_taproom_entrance_discovered` from Absinthe Arcade. The keychain is the externally owned `bottle_opener_keychain` container, not an entry credential. Completing the Mirror Maze/Green Fairy challenge while the tour is active and the keychain is present earns `opener_absinthium_taproom` and `stamp_absinthium_taproom`; the opener is never sold. It also unlocks the 12-Sov `beer_absinthium_taproom` purchase and floating-chalice selfie. A pre-tour completion stores the challenge flag and grants those rewards on the first eligible return interaction without replay. The Taproom also owns Mirror Chad, Dr. Vanek, local statuses, and its return exit.

`brewerytourdebaucheryville.md` owns tour progression and cross-brewery dialogue. Couchsurf integration is bound by state rather than reproduced as local dialogue.

## Package Directives

Core distinguishes entry hours, challenge completion, purchase availability, and boss completion. Nodes contain both real and apparent adjacency. Items reference the externally owned keychain and the authoritative opener, stamp, and beer item files rather than redefining them. Older Blarney-opener checks, the €22 opener purchase, and opener-as-service-gate dialogue are deprecated. PNG and mapping cover interior architecture, mirror variants and masks, portal states, bar props, characters, Wisp effects, selfie landmark, opener/stamp/brew UI, and accessibility replacements.

## Validation

- Arcade and Taproom own opposite sides of one transition.
- Entry does not incorrectly require a Blarney or local opener.
- Challenge completion awards the local opener and stamp together; the beer remains a separate 12-Sov purchase.
- Mirror topology remains solvable with reduced effects.
- No other brewery interior is duplicated.
