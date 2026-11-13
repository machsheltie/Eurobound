# Audit: Cirque du Shady - Mystery Meat Cart (full 8-file review)

**Files read** (all under `design/worlds/debaucheryville/`):
1. Main md: `mysterymeatcart.md`
2. `core/mystery_meat_cart_core.json`
3. `environment/mystery_meat_cart_environment.json`
4. `interactions/mystery_meat_cart_interactions.json`
5. `items/mystery_meat_cart_items.json`
6. `location_nodes/mystery_meat_cart_location_nodes.json`
7. `npcs/Mystery_Meat_Cart/mystery_meat_cart_npcs.json` (the folder holds only this file; there is no Chef Chuckles md, his look comes from the main md L90, L193, L319-330)
8. `PNG_Assets/Mystery_Meat_Cart_Complete_PNG_Asset_Requirements.md`
9. `sprite_mapping/mystery_meat_cart_sprite_mapping.json`
`events/`: MISSING (no match). Nothing else is missing.
Review image: `dev/asset_team/reviews/mystery_meat_cart_ext_review.jpg` (no interior; sprite_mapping lists it `not_built_yet`; md L49 "Hidden Areas: None").

## Q1, how well does it represent the location? Score 4/5 (unchanged)
Painted and correct: carnival-striped cart, glitching marquee ("Shady Dogs" / "Meat Roulette"), "Free Sample (Not Legally Binding)" placard, cracked clown-mask rack (`mmc_chef` display), neon carousel rotisserie (`mmc_rotisserie`), steam, popcorn, ringmaster tent and ferris wheel behind.
Not yet on the plate (all named nodes or props in the new files): the butterfly-knife flip station and Chef Chuckles himself (`mmc_chef`; sleeveless tuxedo, clown shoes, md L90); closed ingredient containers (`mmc_storage`); a reaction zone with crying-child and distressed-family silhouettes (`mmc_consume`, PNG L276-290); hazard props: electrical sparks, sanitation nightmare, structural concerns, no authority figures (PNG L292-295); food-pun warning signs (md L45).

## Q2, how well does it lean into the design requirements? Score 4/5 (unchanged)
Md/PNG palette #DC143C red, #39FF14 neon, #4B0082 shadow all read in their roles; PNG adds meat browns #8B4513 to #696969 and lime #00FF00 pulse. PNG L519 "carnival grift meets dark web wet market", "no soft light". The plate is a fever dream but a clean, gift-shop one; the wet-market grime and hazard evidence are underplayed.

## Verdict: KEEP (confirmed). The base plate stands. The new files add polish items below, as cutouts and overlays, not a redo. Interior: none.

## Polish plan (not a redo)
- **Hook:** "Carnival grift meets dark web wet market" (PNG L519); "Free Sample, Not Legally Binding" (core.json).
- **Palette:** keep #DC143C, #39FF14, #4B0082; add #8B4513/#696969 meat range, #00FF00 pulse for the Brain Brat secret item.
- **Exterior (by node):** `mmc_cart` as painted; `mmc_menu` sign with base text "SHADE MEAT 4 CLOWN SOULS" (md L8, PNG L305) in its glitch cycle; `mmc_rotisserie` as painted; `mmc_chef` knife station plus mask display; `mmc_storage` sealed containers; `mmc_consume` popcorn, silhouettes of distressed families; hazards (sparks, sanitation) at the cart base; pun signs scattered.
- **Interior:** none.
- **Satire beats:** (1) disclaimer sign; (2) clown masks as stock; (3) crying children as ambience; (4) health-code violations as flavour (PNG L535); (5) carousel of mystery meat.
- **Conflicts, need approval:**
  - Palette words in core/environment.json ("neon yellow", "steam grey", "porcelain white") differ from the hex palette in md/PNG; which governs?
  - Prices: md says SOVS; items.json and interactions.json (`charge_kebab_coins`) say Kebab Coins.
  - Is Chef Chuckles painted into the plate, or sprite only?
