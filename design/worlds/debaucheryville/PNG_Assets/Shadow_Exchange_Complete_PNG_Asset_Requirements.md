# Shadow Exchange - Complete PNG Asset Requirements

## Canonical Identity

- **Location ID:** `debaucheryville_gilded_square_shadow_exchange_01`
- **Engine:** Godot 4.7
- **Pipeline:** Painterly HD-2D painted faces, depth cards, cutout props, emission masks and state overlays
- **Visual target:** A damp wine cellar converted into a counterfeit Bloomberg terminal and barter bazaar.

## Resolution and Frame Layout

Every required PNG uses one of these production classes; do not infer canvas size from the visible subject:

| Asset role | Resolution class | Frame layout |
|---|---:|---|
| Exterior, threshold or full interior scene plate | 2048x1152 px | Single 16:9 frame; provide clean plate and separate depth cards |
| Node or landmark cutout | 1024x1024 px | Single transparent frame with 8 px safe padding |
| NPC or creature animation | 2048x512 px | Four 512x512 cells in one row: idle, talk, react, service/combat; 8 fps unless mapping overrides |
| Item, reward or inventory icon | 256x256 px | Single transparent frame with 16 px safe area |
| UI atlas | 2048x1024 px | Power-of-two atlas; label frame rectangles in delivery manifest |
| FX atlas | 2048x2048 px | 8x8 grid of 256x256 cells; unused cells transparent |
| Emission/occlusion mask | Match its source asset exactly | One grayscale mask per source frame; preserve frame order |

## Composition

1. **Candle-Marked Alley** — Damp Gilded Square alley with crooked sign, cash-only candle marker and hinged cobblestone.
2. **Hidden Stair** — Cold stairwell revealed by the moving cobblestone, lit by cigarette-burned tealights.
3. **Exchange Counter** — Scratched glass currency counter beneath the clacking split-flap rate board.
4. **Barter Window** — Iron-lattice stall trading goods, favors and questionable documents.
5. **Contract Desk** — Single lamp illuminates the duct-taped Shadow Ledger and contract forms.
6. **Premium Stock Cage** — Locked market cage opened by the documented post-boss state.
7. **Cellar Exit** — Return stair to the Gilded Square and referral route toward Three-Crown Keg Haus.

## Required PNG Assets

| Asset ID | Filename | Role | Node |
|---|---|---|---|
| `shadow_exchange_ext_alley` | `shadow_exchange_exterior_alley.png` | exterior hero layer | `se_alley_marker` |
| `shadow_exchange_int_cellar` | `shadow_exchange_interior_cellar.png` | interior painted faces | `se_exchange_counter` |
| `shadow_exchange_node_se_hidden_stair` | `shadow_exchange_se_hidden_stair.png` | transition landmark | `se_hidden_stair` |
| `shadow_exchange_node_se_exchange_counter` | `shadow_exchange_se_exchange_counter.png` | service landmark | `se_exchange_counter` |
| `shadow_exchange_node_se_barter_window` | `shadow_exchange_se_barter_window.png` | service landmark | `se_barter_window` |
| `shadow_exchange_node_se_contract_desk` | `shadow_exchange_se_contract_desk.png` | quest landmark | `se_contract_desk` |
| `shadow_exchange_node_se_premium_cage` | `shadow_exchange_se_premium_cage.png` | shop landmark | `se_premium_cage` |
| `shadow_exchange_node_se_cellar_exit` | `shadow_exchange_se_cellar_exit.png` | exit landmark | `se_cellar_exit` |
| `shadow_exchange_npc_se_npc_exchange_broker` | `shadow_exchange_se_npc_exchange_broker.png` | character sprite | `se_exchange_counter` |
| `shadow_exchange_npc_se_npc_barter_clerk` | `shadow_exchange_se_npc_barter_clerk.png` | character sprite | `se_barter_window` |
| `shadow_exchange_npc_se_npc_contract_fixer` | `shadow_exchange_se_npc_contract_fixer.png` | character sprite | `se_contract_desk` |
| `shadow_exchange_npc_se_npc_cryptobro_ex` | `shadow_exchange_se_npc_cryptobro_ex.png` | character sprite | `se_premium_cage` |
| `shadow_exchange_item_item_nft_napster` | `shadow_exchange_item_nft_napster_icon.png` | item/UI icon | global |
| `shadow_exchange_item_se_currency_bundle` | `shadow_exchange_se_currency_bundle_icon.png` | item/UI icon | global |
| `shadow_exchange_item_se_shadow_contract` | `shadow_exchange_se_shadow_contract_icon.png` | item/UI icon | global |
| `shadow_exchange_item_se_counterfeit_charm` | `shadow_exchange_se_counterfeit_charm_icon.png` | item/UI icon | global |
| `shadow_exchange_ui_service` | `shadow_exchange_service_ui.png` | exchange/barter UI | global |
| `shadow_exchange_fx_atmosphere` | `shadow_exchange_atmosphere_fx.png` | smoke, UV and CRT overlays | global |
| `shadow_exchange_mask_emission` | `shadow_exchange_emission_masks.png` | lighting masks | global |

## Character, Item, and State Coverage

- **The Exchange Broker:** idle, talk, react and service frames; Severe coat, UV loupe, fingerless accounting gloves.
- **Barter Clerk:** idle, talk, react and service frames; Layered scarves, ledger pencil, key ring.
- **Contract Fixer:** idle, talk, react and service frames; Blue-grey suit lit by a single amber lamp.
- **CryptoBro69's Ex:** idle, talk, react and service frames; Chrome coat, exhausted glamour, cracked phone.
- **Napster (Mint #01):** inventory/service icon and acquired/disabled state.
- **Mixed Currency Bundle:** inventory/service icon and acquired/disabled state.
- **Shadow Contract:** inventory/service icon and acquired/disabled state.
- **Counterfeit Lucky Charm:** inventory/service icon and acquired/disabled state.
- Hidden, hinted, discovered and permanently known alley/stair states.
- Base, active and completed states for conversion, barter, contracts, ledger NFT and premium stock.

## Accessibility Assets

- Reduced smoke.
- Static rate-board alternative.
- High-contrast currency confirmation.
- Subtitled ticker audio.
- Text/icon equivalents for audio and color-only cues.
- Clean plates beneath smoke, dust, screen glow and rate-board motion.

## Delivery Checklist

- [ ] Every asset ID appears in `sprite_mapping/shadow_exchange_sprite_mapping.json`.
- [ ] Interactive states match `interactions/shadow_exchange_interactions.json`.
- [ ] Transparent assets have clean alpha and 8 px atlas padding.
- [ ] Color, normal and emission-ready variants are supplied for painted faces.

