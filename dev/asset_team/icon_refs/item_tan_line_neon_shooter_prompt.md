# item_tan_line_neon_shooter (The Tan Line Neon Shooter): scripted Blender lathe (batch 15, round 1)
Method: `Tools/item3d/lathe_item.py plain <out.glb> <liquid_hex>`: same chunky opaque satin shot glass as absinthe_shot, glass alone, liquid colour a parameter.
Canon: `design/worlds/debaucheryville/items/bohemian_riviera_items.json` L125-141 ("A shot glowing the exact color of the tanning-bed neon wallpapered across The Tan Line's walls"); venue `design/worlds/debaucheryville/bohemian_riviera.md` L91 and `PNG_Assets/Bohemian_Riviera_Complete_PNG_Asset_Requirements.md` L102 ("tanning-bed neon trim").
COLOUR (round 1B, coordinator ruling): the docs name no hex for "tanning-bed neon", so the agent's choice stands: electric violet-blue #5B2BFF (the UV tanning-bed glow) for liquid top and body, flat, no emission. The hot-magenta accent (EMTV Magenta #FF1493, bohemian_riviera.md L121) is available but not used on the glass.
No lettering. No venue facade, no props.

## Round 2 (A3 R1 fail)
Re-lathed as a real shot glass: 0.90 tall x 0.6 wide at the rim (1.5:1), heavy 0.30 base, walls flared slightly. Painted flat: violet-blue #5B2BFF liquid, darker sticky residue rings, a drip from the rim, scuffed grey base. Art: `item_tan_line_neon_shooter_paint.png`. Script: `lathe_item.py shot <out.glb> <paint.png>`.
