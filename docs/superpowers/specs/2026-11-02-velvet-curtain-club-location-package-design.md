# Velvet Curtain Club Location Package Design

## Intent and Identity

Define Velvet Curtain Club as the gated nightclub, social hub, quest venue, and parent location for the VIP Stall and Ye Olde B.R.E.W. Lab.

- Location ID: `debaucheryville_operaruins_velvetcurtainclub_nightclub_01`
- Slug: `velvet_curtain_club`
- NPC folder: `Velvet_Curtain_Club`
- Primary source: `velvet_curtain_club.md`
- Secondary source: `velvetcurtainclub.md` only for compatible omissions.

## Visual and Spatial Design

A graffiti-lined dead-end lane behind opera ruins ends at a bass-pulsing velvet curtain, rope checkpoint, dumpster mural, glowing bad-taste slogan, and bouncer pair. Inside, deep burgundy fog, crushed-velvet booths, vape-pen chandeliers, gold poles used as coat racks, a broken-throne DJ dais, dance floor, bar/social nodes, and cryptic neon create fraudulent exclusivity.

The club owns visible approaches to two separate destinations: the glitter/lip-gloss trail and `STAFF ONLY` curtain leading to the VIP Stall, and the basement/service approach leading to Ye Olde B.R.E.W. Lab. It owns neither child interior.

## Gameplay, Quests, and State

Full hours are 20:00-04:00. The alley and bouncer conversation are always accessible, while the interior is locked before the quest. `vip_wristbands_all_bros` (stage 3) permits the return approach and starts stages 4-6; it does not itself unlock the interior. Stage 7 completes entry and exports `vip_wristband_quest_complete` plus `velvet_curtain_club_access_was_always_free` for repeat access. Bind current `vip_wristbands`, `club_flyers`, `couchsurfingchroniclesdebaucheryville`, `nothingisgettingthrough`, `brewerytourdebaucheryville`, and relevant beach-beatdown/commuter callbacks without duplicating dialogue.

The club owns social interactions, Vape Witch Vanessa placement, influencer blood ritual event, flyer trigger, bouncer behavior, patrons, and the two child transition exteriors. Discovering the bathroom path sets `velvet_vip_stall_entrance_discovered`; passing its Bravado gate sets `velvet_vip_stall_access_unlocked`. Discovering the Lab service route sets `brew_lab_entrance_discovered`; passing its Bravado/charm gate sets `brew_lab_access_unlocked`.

## Package Directives

Nodes need locked-alley and unlocked-interior graphs plus time-density states. NPCs bind Tomáš, Marek, Vanessa, DJ, attendant references, and patrons. Items distinguish wristbands as quest-owned, club purchases, flyers, and child-location rewards. Environment defines bass, fog, lighting, density, and safe variants. PNG/mapping cover alley, curtain and rope states, club architecture, booths, dais, dance floor, bar, characters, crowd sets, child-entry exteriors, UI, emissions, fog, and reduced-flash layers.

## Validation

- `vip_wristbands_all_bros` starts the return sequence; only stage-7 completion unlocks the interior and repeat access.
- Pre-entry alley content remains available while the interior is locked.
- VIP Stall and B.R.E.W. Lab interiors are excluded.
- Premium-shop and flyer callbacks consume stable exported flags.
- Crowd, fog, and lighting states remain readable in accessibility mode.
