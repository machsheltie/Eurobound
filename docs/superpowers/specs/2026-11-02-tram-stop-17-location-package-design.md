# Tram Stop #17 Location Package Design

## Intent and Identity

Audit Tram Stop #17 as a quiet recurring-NPC landmark between Old Town and the neon entertainment district.

- Location ID: `debaucheryville_transit_tram_stop_17_01`
- Slug: `tram_stop_17`
- NPC folder: `Tram_Stop_17`
- Primary source: `tram_stop_17.md`
- Existing package treatment: retain compatible content and correct only cross-package drift.

## Visual and Spatial Design

The stop begins as an ordinary glass-and-metal European shelter with cracked timetable case, obsolete 1994 schedule, rusted `TRAMVAJ 17` sign, faded map, pigeons, and a weathered bench. Repeated visits transform the bench area into a small Jiří shrine: offerings and candles accumulate, his coat increasingly merges with the slats, and a bronze plaque eventually formalizes the legend.

This is a compact exterior node, not a full transit station. Define street approach, shelter, bench/offerings, timetable, route-map inspection, curb safety boundary, and district exits. Theoretical tram routes must not become working fast travel unless an authoritative system source enables them.

## Gameplay, Quests, and State

The stop is always accessible and has no item or stat gate. Jiří never leaves. The `eternal_commuter` quest owns his dialogue progression and outcomes; the location owns visit-count presentation, interaction staging, ambient commuter loops, offerings, and progressive visual states. Information-point interactions may reference nearby districts without promising functional service.

## Package Directives

Core and nodes must separate physical walking exits from nonfunctional tram-route lore. Environment covers weather exposure, tram pass-bys, pigeons, city ambience, candles, and day/night readability. Items include only local offerings or quest references that the source actually supports. NPC mapping binds Jiří to his existing profile and treats commuters and pigeons as ambient populations. PNG and mapping must provide modular shrine stages rather than four unrelated full-scene paintings.

## Validation

- Jiří's quest dialogue is referenced, not copied.
- Visit progression is deterministic and uses the same thresholds across files.
- No functional transit destination is invented.
- The bench, offerings, plaque, sign, and timetable remain independently mappable assets.
- Existing correct package data remains intact.
