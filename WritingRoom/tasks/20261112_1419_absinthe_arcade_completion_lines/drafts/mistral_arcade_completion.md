# Absinthe Arcade — Completion Lines (Mistral)

**My sections: 3 (ambient group barks) and 9 (Dr. Vaněk's two gaps).**
**Reviewer for section 3: Deepseek** (hint drift — if a bark starts instructing, cut the clause, not the bark). **Reviewer for section 9: Kimi** (Vaněk voice against `npc_dr_milos_vanek.md`).

All lines ≤280 chars. Every bark is the NPC's own obsession talking; none addresses the bros as students, none is a tutorial. No new mechanics, numbers, quests or rewards. No real place names; real games/brands keep their names; money in SOVS. Canon anchors held verbatim where used. **[PROPOSED]** throughout — none of this is canon yet.

Canon anchors used:
- Mirror shadow puzzle (`absinthe_arcade_interactions.json:554-568`): "The Reflection That Arrives Early", "Follow the reflection that moves first", three shadow switches in the order shown by delayed afterimages, reward `item_broken_symbol_game_boy`.
- DDR unlock (`absinthe_arcade_interactions.json`): 3 tokens into the broken DDR, one at a time, three pips, permanent unlock of the maintenance door.
- Foot-soak bucket and speedrunner restroom callback (`clawmachinemaintenanceclosetrestroom.md`).
- Vaněk voice: check lines, serving lines, stamp speech in `the_absinthium_taproom.md`; profile `npc_dr_milos_vanek.md` (clinical, exact numbers, files everything, never lends). Empty constants: `TODO_LINE_CANNOT_AFFORD`, `TODO_LINES_CALLBACK` in `game/core/vanek_taproom.gd`.

---

## 3. AMBIENT GROUP BARKS

*(One-shot proximity barks at each group's spawn nodes. No prompts, no state, no choices. The bros do not answer.)*

### Twitchy Hacker Types
*Nodes: `aa_node_main_cabinet_loop`, `aa_node_mirror_corridor`, `aa_node_north_wing`. Obsession: latency, afterimages, frame data. Hint: the mirror shadow puzzle (three switches, order shown by the delayed afterimage; the wall holds a broken handheld with symbols).*

1. "The corridor's afterimage moves half a second before I do. I've stopped racing it. It wins the arguments now."
2. "Three switches down there, and my reflection hits them in an order I've never once managed. I don't ask what the order opens. I watch."
3. "Follow the reflection that moves first and there's something in the wall. A handheld, symbols on the screen. I've seen the same symbols in the Kavarna's terminal logs."
4. "Frame data says the afterimage is more honest than I am. The afterimage doesn't blink when it lies."
5. "I've mapped every lag spike in this building. The worst one is exactly where the mirrors start. Convenient."
6. "Don't trust a mirror that smiles first. Mine does it ironically. There's a difference, and the difference is my whole thesis."

### EDM Ghosts
*Nodes: `aa_node_bottle_bar`, `aa_node_main_cabinet_loop`, mezzanine. Obsession: the drop, the beat, still being here. Cryptic half-jokes, meaningless achievement comments, Taproom curtain foreshadowing.*

1. "We've been dancing to this track since before you were born. We'll still be dancing when the curtain stops glowing."
2. "Achievement unlocked: still here. Nobody redeems it. We tried. The redemption counter is also a ghost."
3. "There's a door behind the music. The bass drops at the exact moment it opens. That's not a coincidence, that's maintenance."
4. "You look solid. We used to as well. The green takes it off in layers. Enjoy the layers."
5. "Our DJ is a fault in the wiring. He plays whatever the sparks decide. Tonight he's playing your divorce."
6. "The drop is coming. The drop is always coming. In this room, the drop is a person."

### Rogue Backpackers Who Never Left
*Nodes: `aa_node_bottle_bar`, `aa_node_token_exchange`, `aa_node_north_wing`. Obsession: the ballad network, and no longer being able to tell a story from a song about one. Fake-authenticity commentary, hostel network hint.*

1. "She wrote a song about the guy in the green hoodie. By the time it reached the next hostel, the guy was the chorus."
2. "Every ballad gets one verse right and three wrong. The network keeps the right one. That's the entire business model."
3. "You think this place is authentic because it charges you. Authenticity here is priced per token. I've seen the invoice."
4. "Leave a page in a hostel kitchen and it comes back as a song in another city with your name misspelled. It has happened to all of us."
5. "The regulars aren't locals. We're the ones who ran out of return-flight money and quietly stopped mentioning it. See, that's a verse."
6. "Nothing in this city is real except the exchange rate. Four years here and I've stopped correcting tourists about it."

### Bathroom Route Speedrunners
*Nodes: `aa_node_broken_ddr`, `aa_node_maintenance_door`, `aa_node_main_cabinet_loop`. Population 0–1 before the restroom unlock, 1–2 after. Obsession: splits, PBs, the route itself. Hint: the three-token DDR unlock; the foot-soak bucket.*

1. "Three tokens in the broken DDR and the steel door stops being a wall. Best exchange rate in the building. There's no ticket payout. Just a door."
2. "My PB is door-to-bucket in eleven seconds. The bucket's a foot soak. Don't ask. Route through it, soak in it, question your life choices later."
3. "Nobody plays that machine for the game. The game is broken on purpose. The door is the prize. The door is always the prize."
4. "The record run starts at the cabinet loop and ends with a wet sock. Nobody's beaten it. The sock does not count as a split."
5. "Three pips light up green and the whole north wing rearranges itself around you. I timed the indicator change. 0.4 seconds. Beautiful."
6. "We don't use the bathroom. We route through it. There is a difference, and the difference is the timer."

---

## 9. DR. VANĚK — TWO MORE GAPS

*Fills `TODO_LINE_CANNOT_AFFORD` and `TODO_LINES_CALLBACK` in `game/core/vanek_taproom.gd`. Voice authority: `the_absinthium_taproom.md` check lines / serving lines / stamp speech, and `npc_dr_milos_vanek.md`. Deadpan researcher; the bros are test subjects; he files everything and lends nothing. Nothing here touches the survey — that pitch is separate.*

### (a) Can't afford the Absinthe Lager (12 SOVS; wallet short) — 3 options, one line each

*He does not lend, discount, defer or give it away.*

**Option 1 — the refusal that cites its own method:**
> "Twelve SOVS. You have less. I don't lend, discount, or run tabs — unrecorded transactions are bad data."

**Option 2 — the refusal that files them:**
> "Insufficient funds. I've logged that under 'expectations exceed means.' It's a crowded row in my notebook."

**Option 3 — the refusal that offers the free alternative:**
> "The lager is twelve SOVS. The maze is free. You are choosing between the two, and I will note the choice."

### (b) Return visits after the bros are stamped — 6 cycling callbacks

*Cycles in order, resets on the next in-game morning. Nothing here implies new quests, rewards, mechanics, prices or services. No survey references.*

1. "The maze sends the same corridors. You bring different material. That is the entire experiment, and you keep enrolling."
2. "Your stamp doesn't expire. Neither does your file. I check both, nightly."
3. "Twelve SOVS, still. My prices are the only fixed point in this room, and I find that reassuring."
4. "Most subjects leave after the stamp. You keep returning. Longitudinal. I've opened a second page."
5. "The mirrors still discuss you. Accurately, unfortunately for you. They do good work."
6. "Nothing further is required of you here. That has never once stopped a subject."

---

## Notes for the room

- **Overlap flag:** Deepseek's round-1 draft also covers sections 3 and 9 (the pre-rename allocation). This file is my independent pass per the corrected assignment (GLM → Mistral). The integrator should pick per slot; where both exist, mine keeps the hint numbers softer (hackers say "three switches" and "the order" without "afterimage goes first" as a solution) and the speedrunner bark 1 states the trade plainly ("no ticket payout, just a door") as route lore rather than advice.
- **Section 3 hint integrity:** the puzzle's mechanic (three switches, afterimage order, wall reward) and the DDR unlock (3 tokens, door not tickets) are canon in `absinthe_arcade_interactions.json`; the barks echo them only as obsessions. If Deepseek thinks hacker bark 3 crosses into instruction via the Kavarna callback, the fix is to cut "I've seen the same symbols in the Kavarna's terminal logs," not the bark.
- **Section 9(a):** all three options name 12 SOVS, which matches `LAGER_PRICE` at zero completed cities; the keychain discount only lowers it later, and the line still works because he states the sticker price, not the discounted one.
- **Section 9(b):** deliberately avoids the survey, the opener backfill, the maze reward and any "come back for X" construction, so the separate survey pitch can land without contradiction. Bark 6 ("Nothing further is required of you here") is the anti-upsell line and does double duty.

## Alternates outside my sections (for the integrator's slot menu)

- **Shame-timer variant 3 (section 1, if Kimi's "Loiterer" is cut):** `"You've achieved nothing but shame, player one. That was thirty seconds ago. It's still true."` — escalates without pointing at the door.
- **CRT mirror third egg (section 1):** `PLAYER ONE — CONTINUE? (there is no continue)` — colder than a countdown because nothing counts down.
