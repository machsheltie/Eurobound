# Deepseek — Names draft (5 per job, top 3 marked)

Reviewer requested: **Kimi** (voice/register). Secondary: **Aion** (does the joke land for the target audience or is it clever-clever).

---

## Job 1 — quest name (location keeps "Meme Black Market"; quest needs a new one)

Quest shape per brief: restroom graffiti "DO NOT LOOK AT THE BABY" in the Velvet Curtain Club VIP stall → ICQ ping from MemeLord.exe → Internet History Museum in a gutted Blockbuster → GeoCities kiosk at exactly 3:33 AM → password AllYourBase69 at a broken MSN Messenger terminal → VHS shelf slides open onto the den.

**1. Do Not Look at the Baby** ⭐ TOP 3
The graffiti is the quest-log line and the quest-log line is an order the bros cannot follow. No explanation needed, no pun, reads at a glance. A woman who has ever been on a road trip with a man who says "don't" knows this quest ends in a den.
Clash check: found only as graffiti string inside `design/quests/general_quests/memeblackmarket.md`; not in `docs/catalog/quests.md`, not in `locations.md`, `items.md`. Clear.

**2. AllYourBase69** ⭐ TOP 3
The password is the quest name. It is a 2001 meme a 2001 man would pick as a password, with the 69 stapled on, and the quest log shows it before the player has typed it. Nothing to explain.
Clash check: not present anywhere in `docs/catalog/` (quests/items/locations/status/npcs). Only candidate risk is the quest doc body, which is the intended source; no named entity collision. Clear.

**3. Internet History Museum** ⭐ TOP 3
The quest is named after the room the bros are proudest of finding, and the joke is that a gutted Blockbuster is where they feel historically significant. Reads as a real place, which is what makes the quest log sad.
Clash check: appears as a location label inside the same quest doc; NOT in `docs/catalog/locations.md` and not minted as its own location file. **Flag: if the room later mints the museum as a location, this name is taken.** Recommend as quest name only.

**4. 3:33 AM**
The kiosk hour as a quest title. Two-beat, no pun, and it tells the player the quest is about a schedule that no adult should be awake for. Slightly weaker than #1 because nothing in the title is funny on its own — the hour only pays off once you've been to the kiosk.
Clash check: no collision in `docs/catalog/`. Clear.

**5. Somebody Set Us Up the Quest**
Real meme, real name, kept intact, and it's the one line from that meme a bro would actually quote out loud at a bartender. Marked down because it's the room being clever with a meme rather than the bros being caught by one.
Clash check: no collision in `docs/catalog/`. Clear.

**Cut for me:** anything using "Black Market" in the new name. The location keeps that name and a quest called "Black Market ___" re-creates the exact duplicate the author is paying us to fix. Also cut "The VHS Vault" — Tony420's .SWF vault lives in the same quest doc; two vaults is a continuity mess, not a joke.

---

## Job 2 — kapsalon buff name (effect unchanged: +5 Bravado, 1 hour)

Premise per brief: the false courage of a man who just ate a medium tray of fries, döner meat, melted cheese, salad and sauce and now believes he can fight anyone. "Canal Courage" is reserved for Shamsterdam's Legendary Hangover. Effect does not change.

**1. Tray Rage** ⭐ TOP 3
Two words, badge-sized, and it names the object that produced the courage: an aluminum tray. "Rage" is what he calls it; the tray is what it actually is. Lands cold for anyone who has watched a man get brave on a 9 SOVS styrofoam lid.
Clash check: not in `docs/catalog/status_effects_and_abilities.md`, not in `items.md`. Clear.

**2. Cheese Bravado** ⭐ TOP 3
Names the stat and the food in one badge, and the pairing is the whole joke — bravado with a cheese source. No italics, no wink, plays straight in a buff list next to real buffs.
Clash check: no collision in `docs/catalog/status_effects_and_abilities.md`. Clear.

**3. Nine SOVS of Courage** ⭐ TOP 3
The buff is named after what he paid, and the price is the insult. In a status badge it reads as a receipt. Also survives being said out loud by a player, which is the real test for this audience.
Clash check: no collision in `docs/catalog/`. Note: it hard-codes the 9 SOVS price into a name, so if economy review ever re-prices the Inventor's Cut, the name is wrong. **Flag for Mistral.**
 
**4. Kapsalon Courage**
The knockoff of the reserved "Canal Courage" in the same shape Mistral used for "Aluminum Courage" — swap the source, keep the structure, and the reserved name keeps its own lane. Marked down only because it's the fourth "___ Courage" in the file and the joke of the form is thinning.
Clash check: "Canal Courage" is the reserved name (author ruling) and is NOT reused here. Clear.

**5. Gut Full of Brave**
The most accurate one and the least badge-friendly. It's a sentence fragment, not a name, and a status badge that wraps to two lines looks like a bug. Keep it in a line of dialogue somewhere instead.
Clash check: no collision in `docs/catalog/`. Clear.

**Cut for me:** "Grease Lightning" (already disqualified — NPC nickname in `game/assets/data/npcs/easter_eggs.json`), and anything that implies the buff is real courage. The buff must sound like a mistake he made about himself.

---

## My top 3, stated plainly

**Quest:** Do Not Look at the Baby / AllYourBase69 / Internet History Museum
**Buff:** Tray Rage / Cheese Bravado / Nine SOVS of Courage

If Kimi wants one from each list that best survives a quest-log line *and* a status badge with no supporting text: **Do Not Look at the Baby** and **Tray Rage**.
