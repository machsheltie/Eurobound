# Neon & Chrome Boutique Location Package Design

## Intent and Identity

Define Neon & Chrome as the premium club-gear showroom and status merchant of the neon quarter.

- Location ID: `debaucheryville_shop_neon_chrome_01`
- Slug: `neon_and_chrome_boutique`
- NPC folder: `Neon_And_Chrome_Boutique`
- Primary source: `neon_and_chrome_boutique.md`

## Visual and Spatial Design

A glass-and-chrome storefront with purple/pink neon and fully styled mannequins opens into an aggressively hosted showroom. Departments for eyewear, footwear, glow gear, access/status accessories, premium stock, fitting area, club-simulation booth, and Katarina's counter form a polished loop. It should feel like a nightclub monetized before opening, while remaining a distinct shop rather than an Arcade interior.

Strobe simulation and mirrored chrome require reduced-flash, reduced-reflection, and high-readability variants.

## Gameplay, Quests, and State

Hours are 16:00-04:00. Standard stock is money-gated. The source's legacy `bouncer defeat` premium unlock is superseded: premium stock unlocks only after stage 7 exports `debaucheryville.velvet_curtain_club.vip_wristband_quest_complete` and `velvet_curtain_club_access_was_always_free`, without assuming combat occurred. The club simulation previews equipment effects; VIP Potential and Bravado interactions affect reactions, not the ownership of the Velvet entry gate.

## Package Directives

Items define standard and premium catalog entries, prices, equipment slots, status effects, and unlock tier. Interactions consume the external Velvet resolution flag, run fitting/simulation previews, and never grant club entry directly. NPCs cover Katarina, staff, and customers. PNG and mapping cover storefront states, showroom modules, mannequins, fitting and simulation states, characters, product icons, equipment overlays, UI, and accessibility alternatives.

## Validation

- Premium stock uses the current Velvet confrontation-resolution state.
- No unsupported bouncer-combat requirement is introduced.
- Boutique equipment can influence club play without bypassing the wristband gate.
- Hours, stock tiers, prices, and effects agree across files.
- Simulation effects respect accessibility settings.
