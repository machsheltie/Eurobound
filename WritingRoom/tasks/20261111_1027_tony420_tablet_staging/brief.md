# Tony420 tablet staging

# Tony420 tablet staging: Döner Debate rewrite, Kavarna options, Brewery Tour popups

The author's rulings on Tony420 (2026-11-11), all binding:
- Tony420 is never seen in person. When he "appears", a goon brings in a tablet. The author, verbatim: "when the goon brings in the tony420 tablet, the screen should at first be blank and then the familiar ICQ 'uh-oh!' plays and the screen lights up to show the blurred/voice changed tony420". The goon is unnamed, big and silent, and holds the tablet at face height like a hostage photo. The Oakleys stay visible through the blur. The voice changer is deep, slowed and pitch-shifted, and his subtitles keep his lowercase ICQ spelling.
- His voice: "tony420 isnt' that eloquent. He writes like a chatspeak using scammer from the late 90's." Lowercase by default; shouted words and full stops are allowed. Real 90s chatspeak: u, ur, 4, 2, lol, brb, k, l8r, sup, etc.
- Crypto only, across every in-game shitcoin (design/economy/shitcoin_master_pool.md). Rug-pulled coins can't be spent. MoonCum696969 spends only with him.
- Deliveries: "All tony delivered things are drop delivered, unless a goon is already in a scene, or it's somewhere sheisty (say he's dealing with another darkweb adjacent character or they're at the kavarna or the shadow exchange)".
- The Kavarna goon is off-limits until after the Shamsterdam Döner Debate, so that the Debate keeps its reveal.
- Read his profile first: design/worlds/debaucheryville/npcs/Cyberspace_Kavarna/npc_tony420.md

## Job 1 (Kimi): rewrite the Great Döner Debate's body lines for the tablet
File: design/quests/general_quests/greatdonerdebate.md (read only; writers never edit canon). The lines that assume a body, around lines 373–400 and 539–541: "The door creaks open slowly. Tony420 himself walks in", "...Tony? You're... real?", "in the flesh lol / mostly flesh", Big Wim's "Who is this child in my establishment?", "Tony420 holds up a phone showing the original ICQ poll", "Slow zoom on Tony420's face (he's still there somehow)", and line ~651 "Tony420 appearing 'in the flesh' should feel like a major reveal". Restage the scene: the goon walks in, the tablet is blank, the ICQ "Uh-oh!" plays, and the screen lights up blurred. Keep it the major reveal it was built to be (it's the first time the bros "meet" him), keep the poll beat working, and keep every non-Tony character's lines unless a line stops making sense. Output exact old → new replacement text in drafts/kimi_doner_debate_tablet.md.

## Job 2 (Kimi): Kavarna staging options for the author
The author: "we need to decide how to handle the Kavarna since we are holding the goon for the doner scene." Canon has Katka (design/worlds/debaucheryville/npcs/Cyberspace_Kavarna/npc_cybergoth_katka.md) staking out the terminal Tony rents at Cyberspace Kavarna in Debaucheryville, and Dmitri the Router (npc_dmitri_the_router.md) renting it to him. That city comes before Shamsterdam. Propose THREE distinct options for what the bros find at his Kavarna terminal before the Döner Debate that don't spend the goon reveal. One or two sentences of staging each, plus one sample line from Katka or Dmitri. Put them in the same file under "Kavarna options".

## Job 3 (Gemini): bring back the Brewery Tour Debaucheryville ICQ popups
The author ruled "bring them back". In 2026-08-05, four ICQ popup blocks (Miss Morphine, Tony420, RedRoomRandy, CryptoBro69) were removed from design/quests/debaucheryville/brewerytourdebaucheryville.md, because "each one sold openers or opener-adjacent packages for Sovs, which is dead per the master spec's earned-not-bought opener model" (see that file's Reconciliation note, around line 356). Read the removal note, then use git history to see what was cut (`git log -p -- design/quests/debaucheryville/brewerytourdebaucheryville.md`, read only). Write four NEW popups, one per sender, that:
- never sell bottle openers or opener-adjacent packages (openers are earned, never bought),
- are tied to the brewery tour,
- keep each sender's established voice (read the Darkweb Dossier, design/quests/general_quests/darkwebdossiercrossoverevents.md, for Miss Morphine, RedRoomRandy and CryptoBro69),
- price Tony420 in a crypto coin, and price CryptoBro69 in crypto. The other two use SOVS, or have no price if their gag doesn't sell anything,
- follow the junk-item rule if any junk item is involved.
Output to drafts/gemini_brewery_popups.md.

House rules apply (bible/00_room_rules.md): full-strength MA satire, no narrator, no explaining the joke, the bros are never afraid, disgusted or self-aware, real brands keep their real names, no real place names. Save early, post a short summary, then vote done.
