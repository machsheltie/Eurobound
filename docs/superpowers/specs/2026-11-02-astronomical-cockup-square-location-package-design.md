# Astronomical Cock-Up Square Location Package Design

## Intent and Identity

Reconcile the existing Astronomical Cock-Up Square package as Debaucheryville's open-air Old Town quest hub and tourist-scam landmark.

- Location ID: `debaucheryville_oldtown_astronomical_cockup_square_01`
- Slug: `astronomical_cockup_square`
- NPC folder: `Astronomical_Cockup_Square`
- Primary source: `astronomical_cockup_square.md`
- Existing package treatment: audit and correct; preserve compatible detail.

## Visual and Spatial Design

Narrow cobbled streets should open abruptly into a crowded historic square dominated by a sincere Gothic astronomical clock tower. Gold trim, the dial, masonry, and Old Town façades provide credibility; the scam economy forms a comic vendor ring around it. Essential landmarks are the central viewing crowd, the intentionally bad paid viewing spot behind a pillar, Party Monk blessing rug, Clock Wine cart, merchandise tables, roaming wristband seller territory, and the alley sightline toward Euro Ink 4 Less.

This is an exterior location. Surrounding stalls and thresholds are service footprints, not invented building interiors. Crowd density and phone flashes rise before the hourly clock show. Time states must cover morning setup, peak tourism, evening dispersal, and the more predatory night economy.

## Gameplay, Quests, and State

The square is always accessible and requires no entry item. The clock show triggers on the hour during the day cycle. It hosts scam purchases, economic choices, examinations, the tattoo decision that points to Euro Ink, and the first reliable source for fake Velvet Curtain Club wristbands.

Bind current quest states from `astronomical_cockup`, `vip_wristbands`, `club_flyers`, and `eternal_commuter`; reference `bacchanusbeachbeatdown` only where its current quest text explicitly uses the square. Quest files own dialogue and rewards. The package owns vendor placement, encounter triggers, crowd/show states, and exits.

## Package Directives

Core must distinguish physical exits from quest referrals. Nodes must preserve a legible loop around the clock while keeping the show visible. Interactions must separate each scammer and prevent the roaming wristband seller from becoming a fixed stall. Items must reconcile Clock Wine, temporary tattoo or merchandise purchases, wristbands as quest-owned objects, and non-item scam outcomes. NPC mapping must preserve the existing vendor cast and crowd groups. PNG and mapping files must treat the clock tower and façades as painterly HD-2D hero architecture with modular crowds, carts, signs, show states, and phone-flash overlays.

## Validation

- Existing correct IDs and authored detail survive reconciliation.
- The clock show is day/hour gated, not a continuous animation.
- Euro Ink and Velvet Curtain are outbound/referral destinations, not square interiors.
- VIP wristband dialogue and quest rewards are referenced rather than duplicated.
- All scammer nodes remain readable without blocking primary traversal.
