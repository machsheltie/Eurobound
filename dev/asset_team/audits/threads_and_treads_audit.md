# Audit: Threads & Treads

**Files read (8-file set, city debaucheryville, all under design/worlds/debaucheryville/):**
- Main md: threads_and_treads.md (whole)
- core/threads_and_treads_core.json
- environment/threads_and_treads_environment.json
- interactions/threads_and_treads_interactions.json
- items/threads_and_treads_items.json
- location_nodes/threads_and_treads_location_nodes.json
- npcs/Threads_And_Treads/threads_and_treads_npcs.json (only file in folder)
- PNG_Assets/Threads_And_Treads_Complete_PNG_Asset_Requirements.md (HD-2D sheet plus folded-in legacy sheets)
- sprite_mapping/threads_and_treads_sprite_mapping.json
- events/: no folder exists in this city, nothing matches. MISSING files: none.
- Also: dev/asset_team/reviews/threads_and_treads_ext_review.jpg and _int_review.jpg (looked at again).

## Q1, how well does it represent the location? Score 3/5
Doc: "Narrow storefront, dark facade, aggressive aesthetic", "Edgelord Armory", "Illusion of Danger", dark and moody, "surprisingly welcoming". Painted exterior: narrow black front, chrome sign, tagline, window text, honest line, 24/7 plaque, leather mannequins in chains. Text is right. But red/green ivy, skull-and-wings banners and a brass lantern make it a charming heritage shop. Ivy is in no file. The interior (re-viewed) delivers the Entry Gauntlet racks, boot wall, mannequins up top, counter and red curtain, but looks like a cosy Victorian tailor.

## Q2, interior and exterior requirements? Score 3/5 (was 2)
Two palettes disagree. Md/PNG: #1A1A1A, #C0C0C0, #8B0000, #4A4A4A. Core/environment json: black leather, chrome, dark wood, industrial amber. The painted interior (dark wood, amber practicals, red rugs) meets the json palette, not the md one: chrome and gray are thin. Missing from interior: Mirror Wall (json node tt_fitting_mirror), Secret Soft Section, fitting-room curtain gag, dust motes in spot beams, "Neon Edge Trim: subtle red edge lighting" and 2 AM window-glow overlay (PNG sheet 1). Over the top: no.

## Verdict: REDO exterior (strip ivy and heritage charm); REVISE interior

## Redo plan
**Hook:** The all-night store where you buy a new personality at 2 AM: "Leather, Chains, and the Illusion of Danger." (md subtitle)
**Palette:** md/PNG: #1A1A1A, #C0C0C0, #8B0000, #4A4A4A. Pending ruling on conflict 1, keep amber practicals from core json as spot light only.
**Exterior:** Node tt_storefront. Black slab, chrome lettering, chains, studs, red edge trim, window glow, leather mannequins, combat boots, 24/7 sign "Because Reinvention Doesn't Sleep", honest line. No ivy.
**Interior:** Nodes in order: jacket gauntlet (both walls), footwear wall ("Your feet are your foundation" tiered rack), chains and accessories, Mirror Wall with flattering light, Zdeněk Counter, exit. Add the Secret Soft Section of band tees, dark-red fitting curtain with boots visible beneath mid-struggle (PNG "Fitting Room Feet Gag"), dust in spot beams, industrial fixtures. NPC stations: Zdeněk at tt_counter (dark work shirt, tape measure, chrome rings), up to 4 daytime shoppers and 4 2 AM crowd at accessories, mirror, counter.
**Satire beats made visible:** "genuine" vs genuine tags; hidden Soft Section; before/after mirror; 2 AM Discount Tag and banner ("3+ pieces, 10% off"); Post-Breakup Purchaser station.
**Conflicts, approval needed:**
1. Palette: md dark red and industrial gray vs json dark wood and amber.
2. Subtitle: md "Leather, Chains, and the Illusion of Danger." vs core json "Leave Your Old Self at the Door"; sign tagline md "All-Night Equipment Emporium".
3. Night Shift Eva (md, PNG sheet 4) has no entry in npcs json (Zdeněk only).
4. Items: json has 5 (e.g. Genuine-ish Leather Jacket 80, 2 AM Identity Overhaul 150); md has about 30 with other prices.
5. Mirror Wall and Soft Section: md sections, no json node (Soft Section could live in tt_accessories).
**Not in the file, needs approval:** red neon tubes vs red bulbs only; how exaggerated the chain/spike roofline may be.
