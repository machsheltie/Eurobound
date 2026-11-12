# Euro Ink 4 Less Location Package Design

## Intent and Identity

Complete and reconcile Euro Ink 4 Less as the regrettable tattoo-shop payoff to the Astronomical Cock-Up Square tattoo decision.

- Location ID: `debaucheryville_gilded_square_euro_ink_4_less_01` (renamed from the retired oldtown id by Eurobound-a06/Eurobound-7j0m)
- Slug: `euro_ink_4_less`
- NPC folder: `Euro_Ink_4_Less`
- Primary source: `euro_ink_4_less.md`
- Existing package treatment: audit seven existing outputs and create the missing item catalog.

## Visual and Spatial Design

The exterior is a cracked-concrete alley storefront whose failing pink `EURO INK 4 LESS` neon, desperate walk-in signage, expired credentials, and peeling glass tint are visible from the square. The interior is one cramped room: reception at entry, mismatched waiting furniture, two tattoo stations divided by a sheet, walls buried in cheap flash art, and a beaded-curtain glimpse of the back room. Harsh fluorescent light is contaminated by pink and green beer-sign neon.

Nodes should make the barker-to-door-to-counter-to-chair flow unmistakable. The back room remains set dressing unless the source explicitly assigns an interaction; no unauthored treatment room should be created.

## Gameplay, Quests, and State

The shop operates 10:00-02:00. Entry follows the square's `tattoo_decision_made` state and first contact with the exterior barker. The tattoo sequence is a comedy set-piece with menu selection, payment, seating, result reveal, status or appearance consequences, and follow-up recognition. Viktor owns tattoo delivery; Marta and the barker use their documented schedules and roles.

Current `astronomical_cockup` files own the triggering quest state and dialogue. The location owns the service interaction, resulting local appearance state, shop inventory references, repeat-visit reactions, and return exit.

## Package Directives

Items must distinguish purchasable services, consumed supplies or aftercare, and permanent cosmetic/result flags; a tattoo service must not be modeled as a conventional carried object. Nodes and interactions need explicit chair/camera staging for image generation and cutscene implementation. NPCs reference existing Viktor profile material rather than duplicating biography or dialogue. PNG requirements cover storefront states, signage emissions, cramped room faces, flash sheets, station props, barker and artist sprites, tattoo-result UI, and sanitation-comedy details.

## Validation

- All files use the dedicated Old Town location ID.
- The package contains an authoritative item/service catalog.
- The square owns the tattoo decision; Euro Ink owns execution and consequences.
- Operating hours, barker gate, menu prices, and tattoo outcomes agree across files.
- Flash art and results are mapped without claiming copyrighted character likenesses as deliverable assets.
