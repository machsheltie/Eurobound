# The Strobe Survival Kit Location Package Design

## Intent and Identity

Define The Strobe Survival Kit as the neon quarter's night vendor for club protection, sensory mitigation, and rave supplies.

- Location ID: `debaucheryville_vendor_strobe_survival_01`
- Slug: `strobe_survival_kit`
- NPC folder: `Strobe_Survival_Kit`
- Primary source: `the_strobe_survival_kit.md`

## Visual and Spatial Design

A fold-out stall combines military-surplus organization with rave clutter: stencil signs, pegboard stock, earplug dispensers, glow-stick bins, LED accessories, chemical-support shelf, tactical pouches, and a decibel warning display. The footprint is approach, audio-defense section, visual section, support section, operator counter, warning display, briefing point, and street exit.

The nearby clubs may color the backdrop, but the stall is not inside Absinthe Arcade or Velvet Curtain Club. Strobe-heavy merchandise is represented with controlled emission and preview windows, never an unavoidable full-screen flash.

## Gameplay, Quests, and State

Hours are 20:00-05:00, with a documented post-midnight price increase. Equipment modifies club hazards and statuses; tactical briefing previews those effects. Purchases need explicit duration, stack, and compatibility rules so protection is consistent across downstream locations.

## Package Directives

Items are the authoritative equipment inventory and consumables. Interactions own browse, compare, purchase, equip, briefing, decibel-display, and closed-state denial. NPCs define Miroslav and ambient clubgoers. Environment supplies club bleed, street ambience, emission states, and reduced-flash modes. PNG and mapping cover stall deployment, pegboards, stock variants, warning display, operator, customers, icons, equipment overlays, shop UI, and closed/folded state.

## Validation

- Hours and midnight markup agree across files.
- Protective effects reference the exact hazard IDs used by clubs and breweries.
- Flash previews obey reduced-flash settings.
- Stock remains legible without relying on emission alone.
- No club interior content enters the stall package.
