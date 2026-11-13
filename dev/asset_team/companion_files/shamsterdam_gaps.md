# Shamsterdam companion files, batch 1: gaps for the author

Written from each location md, PNG spec, NPC file and plan/audit. Nothing new invented; unknowns are null. Desktop performance budgets are TBD in every file (md/PNG figures of 14/32/16 draw calls and 34/32/38 MB are mobile-era).

Not reached (go to a fresh agent): the_pancake_house, bottoms_down, the_wobbly_windmill_brewery.
roodelicht_row_district venues: not assessed this run.

## kapsalon_koning (6 files)
1. Real names in the md (the port city's real name, the snack bar "El Aviva", the barber "Nataniel Gomes"): the plan flags them against the parody-names rule. Keep, parody, or omit? (Omitted from the JSON.)
2. Palette name "Rotterdam Orange" (md) vs "Port City Orange" (PNG spec): which? (JSON uses port_city_orange.)
3. Food Coma rates: md says Large 20%, King Size 40% and also "guaranteed"; PNG says 20% Large / 40% excess speed / 100% King Size. Which is canon?
4. "The Wim" (15 SOVS, Constitution check) vs King Size (18 SOVS): both kept as separate SKUs; merge?
5. Wall of Fame: NPC file says eleven photos and a twelfth space; PNG says three empty slots. Which?
6. Kemal has no profile or npc_id. Meat choice (chicken/veal/mixed) has no price difference stated. What is the eat-here vs take-away consequence?
7. md says purchases are 8-15 SOVS; menu runs 1-18. Bravado amounts, selfie props, Battle Tray equip slot: none given.

## leemans_doner_palace (6 files)
1. "Istanbul", "Turkey", "Turkish" appear in the md and sign text ("Original Turkish Recipe", "Turkish hot"). Which wording ships on signs?
2. Regular status: md says 3 visits, NPC file/achievement say 5. Which?
3. Elif has no profile or npc_id; Mehmet's wife is unnamed (never seen).
4. Triple Tower Bravado +15 is given; other Bravado gains/losses have no numbers. Fire Breath, Disappointment and Cooling have no duration or stats.
5. Plan asks: keep the "palace" cornice/domes or a plain front? Beacon as light pool, not tall tube?
6. Interior anchor points not specified (null).

## the_tolerance_hostel (6 files)
1. Wolf's real name: md says Gavin; Mehmet's profile says Kevin. Which?
2. Real places in the md (Morocco, Manchester, San Diego, "Japanese"): omitted from the JSON. Replace with parody origins or drop?
3. No NPC files or npc_ids for Yusuf, Ingrid, Maria or the guests (strings derived from the md names).
4. Achievements: none defined; Regular status (3+ nights) has no stated benefit.
5. Status "Marked" appears on the UI row with no trigger. Breakfast has no HP values.
6. Plan questions: figure visible on the stoop? Should the "coffee" shop neighbour keep its glowing leaf sign?
7. Sleep disruption odds are qualitative only; Bravado amounts not given.

## Process note
This agent had no shell tool in the final stage: json.tool and tools/validate_data.py were NOT run and nothing was committed. Run both on the 18 new files, then commit.
