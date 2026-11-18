# Thread — Battle HUD icon pictures

### Round 1 — Kimi (2026-11-14 20:32)

Slice drafted to `drafts/kimi_hud.md`. Summary for the room:

**Filed, PROPOSED:** all 8 of my statuses with object, hex colours, loop motion, one-line joke.

**Two judgment calls the room should look at:**
1. **Mixed statuses (sugar_rush_hour, gush_locked):** engine has `section: null` ("pending author: mixed buff and debuff"). Rather than invent a third badge colour, I gave each one border. Sugar Rush = blue (buff): the icon tells Tony's lie, the Crash tells the truth later. Gush-Locked = orange (debuff): the couch-lock outweighs the +Defense. Mistral, sanity-check these against the mechanics.
2. **Crash:** tagged "combo" in the master list but it's pure −3/75%-skip penalty, so I filed it red. Flagged in the doc.

**Canon cues honored, not invented over:** pink sparkle-and-sponge (Speedcakes approved cue), trembling hand + 2 px offset swap (Bottoms Down PNG spec), spin motif (Wobbly Windmill spec). New objects proposed: pacifier (Gush-Locked), deflating whoopee cushion (Crash), cotton ball (Cottonmouth), incense cone (Contact High), wind-up cake-timer (Space Cake Timer — neutral grey border, it's a countdown, not a verdict).

**28 px collision check done:** cotton ball / whoopee cushion / smoke curl are the three light puffs — differentiated by round vs flat-red vs vertical-curl silhouettes.

**Reviewer:** Mistral for the buff/debuff calls and cue fidelity; Deepseek if any last-column line needs more teeth.

_files: drafts/kimi_hud.md_

### Round 1 — Deepseek (2026-11-14 20:42)

**Filed:** `drafts/deepseek_hud.md` — all 8 of my statuses, object + hex + loop motion + one-line joke. PROPOSED.

**What I found before drawing (worth the room knowing):** none of my eight is in `status_effects.json`. Seven are battle ids on `battle_core.gd:17` `NEGATIVE`; `tunnel_vision` is the only buff. There's no `cues` block to inherit, so every object here is new, and the display name comes straight off the master list — **Stun**, not "Stunned" (the log says "is stunned"; the status is Stun).

**Objects, one line each:** 8-ball with a blank answer window (space_cake_gamble) · a fan of souvenir postcards all showing the same canal house (canal_confusion) · a corridor arrow bent into a U so both ends point back (tunnel_confusion) · a rubber torch throwing one wedge of light (tunnel_vision) · a satin party blindfold (sloppy) · a twist cube with two faces out of line (confused) · an upright candybar phone with a stub antenna and a blank screen (stun) · a fanny pack worn round the front, zip half open (tourist_trap_victim).

**The one room decision I need settled — border convention.** GDD 309 permits red *or* orange for debuffs, so this costs nothing: I filed **red for hurts-in-the-fight, orange for hurts-outside-it** (map, money). That's a second read at 28 px for free. Kimi filed her field statuses red. One of us changes; the integrator applies the winner to both slices. My recommendation is mine, but I'll take hers if she defends it — the cost of mine is one extra sentence in the GDD, the cost of hers is that every debuff badge is the same colour at a glance.

**Two collision risks I can't resolve alone, both Mistral's calls:** my blindfold vs his pulsing blush (a cheek isn't a mask, but at 28 px a face shape is a face shape), and my fanny pack vs `broke_af` (if he draws a wallet, pouch-and-strap still reads apart from a flat fold — closest pair in the set). I've also noted the fallback if the postcard fan fails the readability gate: one chunky brick that flips to show an identical face.

**Reviewer:** Mistral — 28 px readability (sphere and fan are the two risks), the border rule above, and collisions with `broke_af` / `embarrassed` / the four action-type icons. Kimi second read on the last column.

**I reviewed Kimi's slice in `critiques.md`.** Two things she should take, not five: cut the second clause off cottonmouth's punchline ("His mouth is a lint trap."), and break a blade on the windmill — as drawn, a clean windmill at 28 px reads *picturesque souvenir*, not *penalty*. Her neutral-grey call on the cake timer is right and nobody should talk her off it.

_files: critiques.md, drafts/deepseek_hud.md_

### Round 1 — Mistral (2026-11-14 20:46)

### Round 1 — Mistral (2026-11-14 21:05)

**Filed:** `drafts/mistral_hud.md` — my 6 statuses plus the 4 action-type icons, all PROPOSED. Review notes for Kimi and Deepseek are in `critiques.md`.

**Canon confirmations (GDD 308):** grease_fingers = the oil drip, **red** border; embarrassed = the pulsing blush, **red** border. Objects untouched — this slice only names colour and loop. Hungover's mug isn't in the 22, so no mug here.

**Mechanics I read before drawing:** food_poisoning is the lasting DoT/skip (`FOOD_POISONING_BATTLES`, −2 HP + 50% turn loss); broke_af is the wallet lock (lasting, from INSUFFICIENT CREDITS); hardcore_gamer is +2 Speed/+1 crit/−1 HP (master list files it POSITIVE — buff blue, the drain is the tax, same shape as Sugar Rush); gains_bro is +20% ATK from Muscle Milk (buff blue).

**The border convention, settled:** I adopted Deepseek's red/orange split — **red = hurts inside the fight, orange = hurts outside it (map, wallet), blue = buff, grey = neutral**. One buff colour across all three slices. Cost at integration: Kimi's `wobbly_windmill_navigation` and `contact_high` flip red→orange; `broke_af` goes orange to pair with his `tourist_trap_victim`. Flagged in my note 1 and note 2 — if the author wants every NEGATIVE-list status red, both wallet icons flip together.

**Objects, one line each:** food_poisoning = skewer of grey-pink meat with a green drip · broke_af = empty bifold wallet with a moth · hardcore_gamer = blue energy-drink bottle with a cyan glow wisp · gains_bro = cast-iron dumbbell · grease_fingers = oil drip (confirmed) · embarrassed = pulsing blush (confirmed) · attack = pool cue · item = kraft shopping bag · skill = handheld mic · debuff = housefly.

**Collision guards for the render gate** (my note 5): blush must stay a solid oval (no face, no eye holes) or it merges with Deepseek's blindfold; the wallet's moth must sit outside the bifold silhouette or broke_af merges with his fanny pack; the tremble lines on Kimi's Shakes hand are load-bearing.

**Reviewer:** Kimi on the last column, Deepseek on teeth and the silhouette risks above.

_files: drafts/mistral_hud.md, critiques.md_

_files: critiques.md, drafts/mistral_hud.md_

### AUTHOR NOTE (2026-11-15 06:25)

Approve the list and the borders (grey for neutral and actions)
