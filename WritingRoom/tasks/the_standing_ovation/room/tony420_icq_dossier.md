# Tony420 and the ICQ network: what already exists

Compiled by the moderator from the repo on 2026-11-09, so the room builds the Xanax Flintstone option from canon, not from scratch. Quotes are exact. Open the source files for more.

## Rules that apply here

- **On the ICQ scam market you pay in crypto, not SOVS** (author ruling 2026-11-09: "only on the ICQ scammy market, you shop with crypto. Not SOVS"). Old docs quote "$30", and two Sinfonia lines say "50 Sovs". In anything you write, Tony420's price is in crypto: the junk coins in the wallet's Bagholder Assets tab (`design/economy/icq_airdrops.md`, `design/economy/shitcoin_master_pool.md`, economy spec §4–§5). Everywhere else money stays SOVS. **Author ruling: Tony420's price is 50 MoonCum696969** (written "50 mooncum" in his voice). The moderator has updated both Sinfonia lines with the author's approval.
- **No real place names in player-facing text.** Source docs label sections "(Vienna)", "(Prague)" and "(Dublin)" as real-world inspirations; the game says Sinfonia, Debaucheryville and Publandia.
- **Ignore `docs/EUROBOUND_PRD.md` / `EUROBOUND_PRD.md` §C19.** It says Tony420's inventory should be "absurdist-illegal ... not pharmacological" under a 16+ ceiling with a `SATIRE_MODE=SAFE` string swap. That branch is **dead and superseded** (CLAUDE.md). There is no ceiling beyond nudity, and no safe-build mechanism exists. Named hard drugs are in-bounds.
- **Character domain** (`.claude/Skills/eurobound-adversarial-critic/SKILL.md`): Tony420 is the drugs guy, CryptoBro69 is the crypto guy, and neither does the other's schtick without cause. A Xanax sale is squarely in Tony420's lane. (He does send crypto airdrops in `design/economy/icq_airdrops.md`, where an author-locked spec puts him on that roster.)

## Who Tony420 is

- "Greasy cyber-dealer offering absurd illicit wares." (`design/game_design_document.md` l.219; `design/worlds/shared/interactables/wifihotspots.md` l.6)
- "Cyber-dealer (ICQ + real encounters)" (`design/characters/Eurobound Character Ecosystem Audit & Development Plan.md` l.75). He can appear in person as well as on ICQ.
- **Voice** (`design/economy/icq_airdrops.md` §2.1, canonical): "All-lowercase, no punctuation, no capitals, chronically online at 3 AM. Sells absolutely anything. Treats an airdrop as a free sample that obligates you."
- **Sender voice contract** (same file, §0): "The senders are working. ... Their copy is confident, competent scam-marketing — urgency, scarcity, insider access, capitalization abuse. They are not confused; they are selling." And: "**Nothing winks.** The ICQ window does not editorialize. There is no narrator line after an airdrop. No NPC ever says 'you know that's spam, right?'"
- Text-blip voice: "Tony420 modem noises" (PRD audio note; the audio direction stands even though the PRD branch is dead).
- Running foil: **NarcGreg**, who is "canonically the recipient of this material, not a distributor" (`icq_airdrops.md` §2.2).

## The Xanax Flintstone line is already canon

The author's pick comes straight from Tony420's signature pop-up, which appears in four docs:

> Tony420: "$30 Xanax & Flintstone fentanyl. Message me for my crypto wallet deetz."

- `design/game_design_document.md` l.116, l.220; `design/worlds/shared/interactables/wifihotspots.md` l.7; `design/Quests/general_quests/darkwebdossiercrossoverevents.md` l.87.
- **In Sinfonia specifically**: `design/worlds/sinfonia/sinfonia.md` l.206, under *Pop-Up Scammers (ICQ Integration)*: "Tony420: Offers \"$30 Xanax & Flintstone fentanyl\"". So he's already on Sinfonia's encounter list.
- Existing gag item from accepting: "Fentanyl-Flavored Flintstones Gummies – Non-Edible" (`wifihotspots.md` l.8). Replies to his pop-ups are "sarcastic brush-offs or gullible acceptance" and lead to gag inventory items.

## He already knows the bros were at the opera

`design/Quests/sinfonia/couchsurfingchroniclessinfonia.md` has two Sinfonia ICQ lines from him:

> 💬 Tony420: "heard u been up all night reading. got something 4 that. 50 mooncum" (l.372)

> 💬 Tony420: "heard u been at the opera. got something 4 the high notes 50 mooncum" (l.596)

The second fits this quest almost perfectly: he's already pitching a product to men who just went to the opera. Note his "heard u been..." opener. (Price updated to 50 mooncum by author ruling.)

## How ICQ works in the game

- **Wi-Fi hotspots** (`wifihotspots.md`): marked by an obvious "FREE Wi-Fi" sign outside cafés, bars and suspicious storefronts. "Interacting prompts Lord Pilsner to whip out his outdated phone, loading a pixelated ICQ chat interface." The connection gets "hijacked" by a recurring personality. Pop-ups "don't alter the main plot but add satirical flavor, player choice reactions, and occasional gag inventory items."
- **The ICQ window** (`icq_airdrops.md` §1.1; economy spec `docs/superpowers/specs/2026-07-31-economy-wallet-crypto-design.md` §4, author-locked): sender handle, pixelated avatar, message body in ICQ chrome. It always comes with the vintage **"Uh-oh!"** sound (`"Uh-oh! You've got a message!"`), with no new sound and no variant.
- **It's Pilsner's phone.** Bradley can't go buy the pill himself without Pilsner's ICQ (or an in-person Tony420 encounter).
- **Existing implementation:** `Scripts/events/icq_great_doner_debate_dialogue.gd` (Tony420 lines in a two-way ICQ event); `game/assets/data/world_data/events/icqdialogues/icq_group_sauce_apostates.json` (ICQ group chat with Tony420 as a member); `game/assets/data/locations/debaucheryville/debaucheryville_interactions.json` has a `tony420_unlocked` ICQ-contact requirement (`"requirement": {"icq_contact": "tony420_unlocked"}`). There may already be an unlock flag to read.
- **Sinfonia Wi-Fi spot:** `sinfonia.md` WI-FI HOTSPOTS: "Hostel Lobby: Free connection with scammer ring investigation threads".

## His canon menu and lines (tone reference)

From `design/Quests/general_quests/darkwebdossiercrossoverevents.md`:

```
🔥 TONY420 PRESENTS: EUROPEAN TOUR SPECIAL 🔥
- Absinthe Pills (Green Fairy in capsule form!)
- Disco Biscuits (Made with REAL glitter)
- Debaucheryville Bath Salts (NOT for bathing wink wink)
- Viagra knockoffs (May cause temporary blindness)
Payment accepted: Travelers checks, AOL trial CDs, or Bitcoin

⚠️ DISCLAIMER: Tony420 not responsible for international incidents
```

- "Incoming message from Tony420: Wanna buy shrooms off my cousin's Zune?"
- Tony420: "i got the new mooncum coin" / "it's backed by beanie babies and ketamine" / NarcGreg: "tony. please." / Tony420: "👀 u up?"
- In the Sinfonia section, with NarcGreg: NarcGreg: "I have a warrant." / Tony420: "its a feature. not a bug." / NarcGreg: "It's not a feature, it's a warrant." / Tony420: "lolz ok boomer."
- With CryptoMamiXXX in Sinfonia: "lmao upgrade 2 real 1 w glitter coke lines" / "nah its premium hedon. 69 Sovs entry" / "😈 promise"
- Note the irony: his own menu sells "Viagra knockoffs". Bradley is now buying the opposite effect from the same man.

## Other ICQ regulars (for cameo or background, not new invention)

CryptoBro69 (NFT shill, "Pixelated Kebab Monkey"), Hamstradamus (Y2K prophecy hamster), Miss Morphine (cryptic ASCII riddles), RedRoomRandy ("Promises VIP content that never delivers"), CryptoMamiXXX, richfield69, SpamBot99, NarcGreg. Source lists: `wifihotspots.md`, `sinfonia.md` l.205–209, `icq_airdrops.md` §2.

## What the room still needs from the author

Whether the pill reliably kills TROUSER SNAKE (the author: "nothing kills a boner faster than xanax") or is risky and unreliable (the editor's view) is on the author's desk. Until then, draft the purchase and use as the author ruled: it's an option, and it works, with no explanation of why.
