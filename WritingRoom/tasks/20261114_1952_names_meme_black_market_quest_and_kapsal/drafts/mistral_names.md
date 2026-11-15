# Mistral — name candidates: Meme Black Market quest rename + kapsalon buff rename

Clash-check method: every candidate grepped against `docs/catalog/` (quests.md, items.md, locations.md, status_effects_and_abilities.md, npcs.md, catalog.json), all of `design/`, and `game/assets/data/`. A clash with any existing quest/item/location/status/NPC/engine name disqualifies. Dialogue text and graffiti text are not names and do not disqualify.

---

## Job 1 — Quest name (replaces "Meme Black Market" on the quest; the location keeps it)

Quest contents: graffiti "DO NOT LOOK AT THE BABY" in the Velvet Curtain VIP stall → ICQ ping from MemeLord.exe ("i got what ur soul needs lol") → Internet History Museum (gutted Blockbuster) → GeoCities kiosk at exactly 3:33 AM → password AllYourBase69 at broken MSN terminal → VHS shelf slides open onto the den.

### Candidates

1. **Don't Look at the Baby** — The graffiti trigger is the entire hook; as a quest log line it reads like a dare the bros absolutely took. Reads at a glance, funny because it's the stupidest possible quest name. Clash check: graffiti string "DO NOT LOOK AT THE BABY" exists in `game/assets/data/world_data/events/publicrestroomgraffiti/graffiti_quest_data.json:73` and design docs, but as graffiti text, not as any named entity. No quest/item/location/status/NPC named this. **CLEAR.**

2. **i got what ur soul needs** — MemeLord.exe's ICQ ping verbatim; a lowercase ICQ handle-speak line in the quest log is instantly funny and marks the quest as the weird internet one. Clash check: string appears only as dialogue in `design/Quests/general_quests/memeblackmarket.md:71` and `design/worlds/debaucheryville/memeblackmarket.md:133`. Not a name anywhere. **CLEAR.**

3. **3:33 AM** — The kiosk hour. Short, ominous, badge-sized; a quest log that just says "3:33 AM" is its own joke. Clash check: no matches in catalog, `design/`, or engine data. **CLEAR.**

4. **All Your Base** — The password, real meme name kept per rules. Clash check: "All Your Base Are Belong to Us" appears as dialogue/graffiti in `design/Quests/debaucheryville/club_flyers.md:238,292`, not as a name. **CLEAR.**

5. **Dial-Up to the Den** — Pun on the dial-up modem shrine and the hidden den; reads at a glance as a quest title. Clash check: no matches for the full phrase anywhere. **CLEAR.**

**Rejected during clash check:** "The VHS Vault" (too generic, and "vault" collides conceptually with Tony420's .SWF vault in the same quest doc — avoided to keep the two distinct).

### Top 3
1. **Don't Look at the Baby**
2. **i got what ur soul needs**
3. **3:33 AM**

---

## Job 2 — Buff name (The Inventor's Cut, 9 SOVS kapsalon; effect unchanged: +5 Bravado, 1 hour)

The false courage of a man who just ate a tray of cheese-fries-meat and thinks he can fight anyone. "Canal Courage" is reserved for Shamsterdam's Legendary Hangover and must not be reused.

### Candidates

1. **Tray Rage** — The anger/courage a man feels holding an aluminum tray of melted everything; short enough for a status badge, reads instantly, implies he thinks he can fight. Clash check: no matches in catalog, `design/`, or engine data. **CLEAR.**

2. **Aluminum Courage** — Direct knockoff of the reserved "Canal Courage," swapping canal for the kapsalon tray; the parody of a hangover buff name on a food buff is the joke. Clash check: "Canal Courage" exists as a status (`status_effects.json`, bead n355) but "Aluminum Courage" has no matches anywhere. **CLEAR.**

3. **Cheese Confidence** — Alliterative, badge-sized; the confidence that comes specifically from melted cheese on fries. Clash check: no matches anywhere. **CLEAR.**

4. **Inventor's High** — Ties to the item name "The Inventor's Cut"; the high you get from eating it as the inventor intended. Clash check: no matches for the phrase in catalog, `design/`, or engine data ("The Inventor's Cut" is the item, distinct). **CLEAR.**

5. **Grease Guts** — The gut that ate the tray and now believes in itself. Clash check: "Gut of Steel" / "Continental Gut of Steel" exist as titles in greatdonerdebate.md, but "Grease Guts" itself has no matches. **CLEAR** (kept distinct from the Gut of Steel titles).

**Rejected during clash check:** "Grease Lightning" — clashes with an NPC nickname/title in `game/assets/data/npcs/easter_eggs.json:160,163`. Disqualified.

### Top 3
1. **Tray Rage**
2. **Aluminum Courage**
3. **Cheese Confidence**
