# Tony420 canon audit: The Standing Ovation (final.md)

Read-only audit, 2026-11-11. Target: `WritingRoom/tasks/the_standing_ovation/final.md` (2,123 lines).
Paths are relative to the repo root. "DWD" = `design/Quests/general_quests/darkwebdossiercrossoverevents.md`, the canonical copy. The root-level `design/Quests/darkwebdossiercrossoverevents.md` still contains merge-conflict markers and real place names, so it is not canon (see §4). "GDD-Q" = `design/Quests/general_quests/greatdonerdebate.md`.

---

## 1. Canon dossier

### Identity, handle, IDs
- Handle is always spelled `Tony420`, written as one token everywhere. In ads it also appears lowercased as `icq tony420` (DWD:308, 376, 396, 473) and in caps as `TONY420 PRESENTS` (DWD:102). In-voice nickname: "tony" (DWD:18, 94, 240). Item name derived from him: "Tony's Deepfried Memes Collection" (`memeblackmarket.md:76`).
- No NPC profile and no NPC ID exist for him anywhere in canon. The only matches for `shared_npc_tony420_01` are in WritingRoom files. **No duplicate exists.**
- NPC ID convention is `[city]_npc_[name]_01` (`design/templates/NPC_Profile_Template.md:6`). No `shared_npc_` prefix exists anywhere in the repo, and `design/worlds/shared/` contains only `interactables/`.
- Precedent for a cross-city ICQ personality: Miss Morphine is `debaucheryville_npc_miss_morphine_01` (`design/worlds/debaucheryville/npcs/_unassigned/miss_morphine.md:6`).
- An existing sprite slot for him: **"Tony420 Fake Crypto" (48, 192, 48x64), crypto scammer with obvious fake wallet** (`design/worlds/debaucheryville/PNG_Assets/Cyberspace_Kavarna_Complete_PNG_Asset_Requirements.md:168`).
- Flags and IDs that exist:
  - `tony420_unlocked`, used as an `icq_contact` requirement on the Meme Black Market trade (`game/assets/data/locations/debaucheryville/debaucheryville_interactions.json:2807-2811`). **Nothing in canon ever sets it.**
  - The condition string `tony420_contact_unlocked_and_rare_memes_acquired` (same file, :2999).
  - Trigger `tony420_meme_trading` (:2807).
  - `swf_vault_via_tony420_trading` and `tony420_icq_network_swf_vault` (`debaucheryville_locations.json:2927, 2937`).
  - The Mystery Meat lore hook "unlocks_unique_lore_when_consumed_during_tony420_interaction" (`debaucheryville_locations.json:667`, `debaucheryville_interactions.json:268`).
  - Quest item "The Tony420 File" (`npc_cybergoth_katka.md:187, 301`).
- Katka's intel: "Same wallet, three years, **four handles**. He changes the handle and keeps the wallet" (`npc_cybergoth_katka.md:112`). The File "identifies the reused wallet across four handles" (:301).

### Voice
- Rule as written: "All-lowercase, no punctuation, no capitals, chronically online at 3 AM. Sells absolutely anything. Treats an airdrop as a free sample that obligates you." (`design/economy/icq_airdrops.md:80`)
- He is competent, not confused: "Tony420 and company know exactly what a $SPANK token is worth… They are not confused; they are selling." (`icq_airdrops.md:15`)
- DWD profile:
  - "Speaks in early 2000s internet slang mixed with fake business terminology"
  - "Never admits fault, always spins disasters as 'features'"
  - "Always online at suspicious hours (3AM - 6AM)"
  - Source: DWD:603-608.
- Real usage:
  - It is mostly lowercase, uses **full stops freely**, and drops apostrophes.
  - "dont sell it. dont even look at it. just hold / u kno what u got" (`icq_airdrops.md:112-115`)
  - "its a feature. not a bug." (DWD:218)
  - "lolz ok boomer." (DWD:222)
  - "lmao feature not a bug. 69 Sovs refund?" (DWD:315)
  - "lol clown just rage quit / anyway ur kebab karma just got spicier" (`Scripts/systems/icq_events/icq_great_doner_debate_dialogue.gd:12`)
  - "reminder: box meat is legal tender in some backchannels" (`game/assets/data/world_data/events/icqdialogues/icq_group_sauce_apostates.json:9`)
- Recurring pitch template, Couchsurfing Chronicles: "heard u been [X]. got something 4 [X]. 50 [currency]". It appears in:
  - `couchsurfingchroniclessinfonia.md:372, 596`
  - `couchsurfingchroniclespublandia.md:304, 665`
  - `couchsurfingchroniclesdebaucheryville.md:551`
  - `couchsurfingchroniclesshamsterdam.md:721`
- Catchphrases:
  - "u up?" (DWD:84)
  - "message me for my crypto wallet deetz" (DWD:87; GDD:116)
  - "feature not a bug" (DWD:218, 315)
  - "no cap" (DWD:16)
  - "ez" (DWD:385, 407)
  - "4 / 2 / u / ur / da / dat / w/" substitutions throughout DWD 240-455
- Capitals do occur in canon, which conflicts with the rule (see §4-B):
  - "BANANA" (`bacchanusbeachbeatdown.md:193`)
  - "HODL!!!1" (`icq_airdrops.md:159`)
  - "Yeh, also includes PDF…" (DWD:76)
  - "wassup bros! …" (`club_flyers.md:365`)

### What he sells, prices, currencies
- Author-established product names: **Flintstone Xanax** and **Flintstone Fentanyl**. Fentanyl must not get the Xanax effect (`design/mechanics/intoxication_law.md:61-82`). "His existing canonical characterization, inventory, and crypto payment mechanics must be respected" (:63).
- Flintstone Xanax price: **50 MoonCum696969, MoonCum spendable with Tony420 only** (`icq_airdrops.md:51`; `shitcoin_master_pool.md:855`).
- Free sample: exactly 50 MoonCum airdropped "right before pitching the pill" in *The Standing Ovation* (`icq_airdrops.md:52`).
- Legacy pitch: "$30 Xanax & Flintstone fentanyl. message me for my crypto wallet deetz." It appears in:
  - `design/game_design_document.md:116, 220`
  - `design/worlds/shared/interactables/wifihotspots.md:7`
  - `design/worlds/sinfonia/sinfonia.md:206`
  - DWD:57 ("$30 Xanax"), DWD:87
- Gag item from accepting that pitch: "Fentanyl-Flavored Flintstones Gummies – Non-Edible" (`wifihotspots.md:8`).
- "Flintstones" wording elsewhere:
  - "yo u want the good Flintstones sh*t? / dino-shaped. no cap." (DWD:15-16)
  - **"bundle w my fentanyl vitamins?"** (DWD:280). He already uses "vitamins" for a *fentanyl* product.
- Tony quotes SOVS in many places:
  - 50 Sovs: Guinness suppositories (DWD:122)
  - 69 Sovs (DWD:246, 315, 331)
  - 20 Sovs (DWD:296)
  - 40 Sovs: off-brand viagra, "opera-ready wood" (DWD:349-351)
  - 200 Sovs: opera glasses (DWD:496)
  - 50 Sovs in Couchsurfing for Debaucheryville, Publandia and Shamsterdam (lines above)
  - Sinfonia Couchsurfing quotes **50 mooncum** (`couchsurfingchroniclessinfonia.md:372, 596`)
- Other payment jokes:
  - "Doge, expired Olive Garden gift cards, or cursed Pokémon cards" (DWD:68)
  - "Travelers checks, AOL trial CDs, or Bitcoin" (DWD:107)
- Airdrops he sends: AD-01 100k $SPANK, AD-04 8.4M MoonCum696969, AD-07 66,600 TractorCoin, AD-11 2M SafeMoon-X (`icq_airdrops.md:109-262`).
- His MoonCum pitch: "backed by beanie babies and ketamine" (DWD:80-81; `icq_airdrops.md:157`).

### Contact channel and gating
- He reaches the party by ICQ pop-up at signed "FREE Wi-Fi" hotspots "outside cafés, bars, and random suspicious storefronts". Lord Pilsner opens the phone and the connection is "hijacked" (`wifihotspots.md:1-6`; DWD:1-4).
- The sound is "Uh-oh! You've got a message!" (DWD:4; `icq_airdrops.md:26`).
- Hotspots "double as save points" (`icq_airdrops.md:32`).
- Airdrops are hard-gated on `has_inspected_first_crypto_trash`, recorded in `airdrops_delivered`, and paid into `bagholder_assets` (`icq_airdrops.md:38, 307-311`).
- **Documented Sinfonia hotspots:**
  - Opera Lobby, University Café, Museum Foyer (`sinfonia.md:159-163`)
  - Café Existenz (`sinfonia.md:55`; `cafe_existenz.md:225`)
  - Bassline Opera House Grand Lobby, "Opera House Public Wi-Fi" (`bassline_opera_house.md:24, 136`; `interactions/bassline_opera_house_interactions.json:96-104`)
  - The Standing Ovation venue is the "Converted opera house annex near The Bassline Opera House" (`sinfonia.md:80-82`).
- The "Hostel Lobby" hotspot at `sinfonia.md:212` sits inside a **Debaucheryville block pasted into sinfonia.md** (lines ~170-220 cover the Velvet Curtain Club, the Absinthe Cathedral and "Debaucheryville-Specific Systems" at :218). **Sinfonia has no documented hostel hotspot.**

### Schedule
- "online at 3:07 AM" (DWD:55); "3AM - 6AM" (DWD:604); "chronically online at 3 AM" (`icq_airdrops.md:80`); "it's 3am on a tuesday" (DWD:588).
- No formal schedule exists. His Kavarna terminal sits next to Katka's, and she is there 14:00-00:00 (`npc_cybergoth_katka.md:170-176`).

### Locations and in-person status
- **In person, Debaucheryville, Cyberspace Kavarna:**
  - He rents terminals from Dmitri and "Runs a fake crypto wallet scheme out of a machine Dmitri rents him at full price" (`npc_dmitri_the_router.md:214`).
  - Katka sits "immediately to [his] right" on a three-year stakeout (`npc_cybergoth_katka.md:176, 210`).
  - Screenshot moment: "Katka and Tony420 at adjacent terminals, him oblivious" (:313).
  - "Cyber-dealer (ICQ + real encounters)" (`Eurobound Character Ecosystem Audit & Development Plan.md:75`).
- **In person, Shamsterdam expansion (Döner Debate):** "Tony420 himself walks in — a pale, hoodie-clad figure who has clearly never seen sunlight." Pilsner: "...Tony? You're... real?" Tony: "in the flesh lol" (GDD-Q:373-380). "should feel like a major reveal" (GDD-Q:651).
- Claims to have been in the Sinfonia opera: "snuck into VIP box at the opera / told them i was a 'cultural influencer'" (DWD:513-515).
- ICQ presence in each city:
  - Debaucheryville: `debaucheryville.md:175`; Cirque du Shady backroom hotspot (`cirque_du_shady.md:198`; `GDD:110-116`); Bohemian Riviera livestream chat (`bohemian_riviera_interactions.json:701-705`)
  - Shamsterdam: "Returns with Amsterdam-specific 'offerings'" (`shamsterdam.md:423`)
  - Sinfonia: DWD:202-528
  - Publandia: DWD:114-125

### Visual
- ICQ avatar: "Pixelated avi wearing **Oakleys indoors**" (DWD:59). "Blurry photo of someone in Oakleys, could be anyone" (DWD:607).
- In person: "pale, hoodie-clad figure who has clearly never seen sunlight" (GDD-Q:373-374). Sprite slot "Crypto scammer with obvious fake wallet" (PNG reqs :168).

### Relationships
- **NarcGreg**: target of his pitches and holds a warrant against him (DWD:17-18, 82-83, 214-222, 293-298).
- **CryptoMamiXXX**: DWD:239-250, 313-317, 348-353, 450-455.
- **Hamstradamus**: DWD:275-284, 327-333, 597; `club_flyers.md:373`.
- **richfield69**: DWD:380-435, 585-590.
- **Dmitri**: rents him terminals (`npc_dmitri_the_router.md:214`).
- **Katka**: watches him; he has no idea (`npc_cybergoth_katka.md:210`).
- **Miss Morphine**: "Same client, adjacent hours" (`miss_morphine.md:191`).
- **ICQ groups**: member of Sauce Apostates 2.0 (`icq_group_sauce_apostates.json:4`); admin of the Döner Council (GDD-Q:588).
- **MemeLord.exe**: through the SWF-vault trade (`debaucheryville_interactions.json:2814`).
- "Tony420's dentist" (DWD:46).

### Events he appears in
- The Great Döner Debate verdict poll and outcomes (GDD-Q:103-170, 460-545; `icq_great_doner_debate_dialogue.gd`).
- Operation Script Kiddie, where his wallet scheme gets exposed (`cyberspacekavarna.md:97`; `npc_cybergoth_katka.md:279-282`).
- ICQ Scammer Sting (`icqscammersting.md:13`).
- Meme Black Market SWF vault (`memeblackmarket.md:76, 81`; `design/worlds/debaucheryville/memeblackmarket.md:51, 135`).
- Club Flyers hooks (`club_flyers.md:355-373`).
- Chadwick's GO LIVE chat (`bacchanusbeachbeatdown.md:189-193, 641`).
- Mystery Meat lore (`mysterymeatcart.md:106, 141`).
- Couchsurfing harassment in all four cities.
- The brewery-tour Tony popups were deliberately removed (`brewerytourdebaucheryville.md:356-363`).

---

## 2. Comparison table (final.md vs canon)

| # | final.md | Verdict | Notes / sources |
|---|---|---|---|
| 1 | Handle `Tony420`, ICQ pop-up, vintage "Uh-oh!" (974) | CONSISTENT | `icq_airdrops.md:26`; DWD:4 |
| 2 | Free sample of exactly 50 MoonCum just before the pitch, no prompt, flat-grey row (977-983, 1004) | CONSISTENT | `icq_airdrops.md:52, 4.4` (silent deposit, no jingle) |
| 3 | Price 50 MoonCum696969, Tony-only, no SOVS (994) | CONSISTENT | `icq_airdrops.md:51`; `shitcoin_master_pool.md:855` |
| 4 | Gated on `has_inspected_first_crypto_trash`; uses `airdrops_delivered` and `bagholder_assets` (1002-1004, 1935) | CONSISTENT | `icq_airdrops.md:38, 307-311`. The pill route needs prior rug-pull + certificate + Inspect (`economy_system.md:269`); that is correct but worth stating. |
| 5 | "reads any existing `tony420_unlocked` contact requirement… the player can establish access through the existing… contact routes" (1002; also 1935) | **CONTRADICTS / broken reference** | **No canon source sets `tony420_unlocked`.** It is only read, by the Meme Black Market trade (`debaucheryville_interactions.json:2811`). Canon's ICQ model is that Tony **hijacks any FREE Wi-Fi connection unprompted** (`wifihotspots.md:3-6`). If an implementer gates §11 on this flag, the pill route can never be reached. |
| 6 | "the documented Sinfonia hostel-lobby hotspot is the CANON fallback" (972); "Orchestra Pit / foyer or hostel hotspot" (2008); profile, same claim | **CONTRADICTS** | `sinfonia.md:212` "Hostel Lobby" belongs to the Debaucheryville block (sinfonia.md ~170-220). Sinfonia's real hotspots are the Opera Lobby / Bassline Opera House Grand Lobby, University Café, Museum Foyer and Café Existenz (`sinfonia.md:55, 159-163`; `bassline_opera_house.md:24, 136`). final.md:1016 also says the bros "have not departed for the hostel" during the window. |
| 7 | Venue-door FREE Wi-Fi decal, PROPOSED (972) | CONSISTENT in kind | Canon places hotspots at "cafés, bars, and random suspicious storefronts" (`wifihotspots.md:2`), and a brewery is a bar. Note that hotspots double as **save points** (`icq_airdrops.md:32`), so the decal adds a save point at the venue. |
| 8 | Pitch "heard u been at the opera. got something 4 the high notes 50 mooncum" (989) | CONSISTENT voice; **duplicate line** | Verbatim from `couchsurfingchroniclessinfonia.md:596` (Digital Footprint Disaster harassment set). Players who trigger both see the identical line twice. Also, :372 already has a separate "50 mooncum" pitch for something else. |
| 9 | "xanax flintstones. chewable. grape" (990) | Minor drift | The author's product name is "Flintstone Xanax" (`intoxication_law.md:67`; `icq_airdrops.md:51`). "chewable / grape / purple" fits canon "dino-shaped" (DWD:16). |
| 10 | Lowercase, no apostrophes, full stops ("free sample. 50 mooncum. check ur assets", "sent. dont take 2") (978-998) | CONSISTENT with practice | Matches AD-01 and DWD usage. The full stops technically break the "no punctuation" rule at `icq_airdrops.md:80` (see §4-B). final.md:1966 repeats "no punctuation", which its own lines contradict. |
| 11 | "u can only spend it here" (980) | Minor voice risk | Tony states the spend restriction outright. The room's own voice direction says he "never explains… a mechanic", and `icq_airdrops.md:21` says the ICQ window "does not editorialize". Arguably in-character as sales copy. Author's call. |
| 12 | "dont spend it all in one place" / "trust me" / decline / close lines (979, 991, 996-998) | CONSISTENT | Confident and competent sales register (`icq_airdrops.md:15`). The "free sample that obligates" trait (:80) is honoured. |
| 13 | Item ID `flintstone_vitamins` (1012, 1908, 1935); Pilsner "Vitamins." (1008) | **Name-collision risk** | Canon Tony already uses "**fentanyl vitamins**" (DWD:280). final.md itself insists Fentanyl stays separate, "do not merge" (1908). An ID reading "vitamins" invites conflation. The in-dialogue joke ("Vitamins.") is fine. |
| 14 | "Flintstone Fentanyl is a separate product with no assigned effect" (1012, 1908) | CONSISTENT | `intoxication_law.md:82` |
| 15 | Pill effect: ends TROUSER SNAKE; recurrence and performance blocked to next morning, no roll (1006, 1927) | CONSISTENT | `intoxication_law.md:70-74` |
| 16 | Not met in person; ICQ only; "No physical Sinfonia sprite" (profile) | CONSISTENT | No in-person staging in §11. This does not collide with the Döner Debate "major reveal" (GDD-Q:651). |
| 17 | Time 00:05-00:25 (2008) | CONSISTENT (soft) | Canon puts him "always online", with emphasis on 3-6 AM (DWD:604). Midnight is fine. "3 AM" isn't used as a hook. |
| 18 | Appendix C: "crypto-only for actual ICQ purchases"; "Older dollar/SOVS-facing ads are historical pitch copy" (1966) | **CONTRADICTS (overreach)** | Canon has him quoting SOVS prices for live pitches in four Couchsurfing quests and across DWD. "Takes cryptocurrency payments" (`intoxication_law.md:61`) does not mean crypto-*only*. Only *this* transaction is crypto-only by ruling (q10). Calling the other pitches "historical" is an invented reclassification. |
| 19 | `shared_npc_tony420_01`, profile at `design/worlds/shared/npcs/npc_tony420.md` (1966, 2025) | Not a duplicate; **convention conflict** | No existing ID or profile, so nothing is duplicated. But the template requires `[city]_npc_…` (`NPC_Profile_Template.md:6`), the `shared/npcs/` folder doesn't exist, and the closest precedent (Miss Morphine) uses `debaucheryville_npc_…`. His physical home is Cyberspace Kavarna, and a sprite slot already exists there (PNG reqs :168). |
| 20 | Visual expansion: hoodie, fingerless gloves, USB lanyard, "2003 webcam" avatar (draft profile, cited by 1966/2025) | **MISSING / partial conflict** | Omits the canon **Oakleys-indoors** avatar (DWD:59, 607). The hoodie matches Döner Debate (GDD-Q:373) but isn't cited. The existing "Tony420 Fake Crypto" sprite (PNG reqs :168) isn't referenced. |
| 21 | Relationships (profile): NarcGreg, CryptoMamiXXX, CryptoBro69, Dmitri, Katka, Miss Morphine | MISSING | Omits Hamstradamus, richfield69, ChefChuckles / Sauce Apostates / Döner Council (admin), MemeLord.exe / SWF vault, Chadwick's livestream chat, and the Döner Debate in-person reveal (all §1). |
| 22 | Operation Script Kiddie state | MISSING | If the player exposed his wallet scheme in Debaucheryville (`npc_cybergoth_katka.md:282`), §11 still fires. That is canon-compatible, since Katka says he keeps working (:112), but final.md never says so. |
| 23 | Appendix C 1890 "canon edits to `design/economy/` pending the author's OK"; checklist 2097 "pool entry proposed, not applied" | **CONTRADICTS (stale)** | The pool entry and the Tony-only exception are already applied (`shitcoin_master_pool.md:855-857`, "Added 2026-11-10 by author approval"; `icq_airdrops.md:51-52`). final.md:2026 itself says DONE. |
| 24 | Name uniqueness | CONSISTENT | `Tony420` is unique. The only bare "Tony" uses are nicknames for him. "Flintstone Xanax" is distinct from the "Fentanyl-Flavored Flintstones Gummies" gag item. |

---

## 3. Recommended exact fixes to final.md

All of these are text-accuracy fixes. Items marked (AUTHOR) need a ruling before they are applied.

1. **Line 972**:
   - old: `the documented Sinfonia hostel-lobby hotspot is the CANON fallback.`
   - new: `the documented Bassline Opera House Grand Lobby hotspot ("Opera House Public Wi-Fi", next door to the venue annex) is the CANON fallback.`
2. **Line 2008**:
   - old: `Orchestra Pit / foyer or hostel hotspot`
   - new: `Orchestra Pit / foyer or Opera House Grand Lobby hotspot`
3. **Line 1966**: in the same sentence, change `the hostel-lobby hotspot is the documented fallback` to `the Bassline Opera House Grand Lobby hotspot is the documented fallback`. The same fix is needed in `drafts/kimi_tony420_profile.md` "Primary Location" and "Recurring Appearances".
4. **Line 1002** (AUTHOR):
   - old: `and reads any existing \`tony420_unlocked\` contact requirement rather than bypassing it. The quest grants neither the reveal flag nor the contact unlock. If either requirement is absent`
   - new: `It does not read \`tony420_unlocked\` (that flag gates only the Meme Black Market SWF trade and no canon source sets it; Tony420 hijacks any FREE Wi-Fi connection unprompted per \`wifihotspots.md\`). The quest does not grant the reveal flag. If the reveal flag is absent`
   - Apply the matching edit at **1935**: delete `and any applicable \`tony420_unlocked\` contact`.
5. **Lines 1012, 1908, 1935** (AUTHOR / engine): rename the ID `flintstone_vitamins` → `flintstone_xanax`. Reason: canon Tony already sells "fentanyl vitamins" (DWD:280), so the current ID points the wrong way. Pilsner's "Vitamins." line stays.
6. **Line 990** (AUTHOR, optional):
   - old: `xanax flintstones. chewable. grape`
   - new: `flintstone xanax. chewable. grape`
   - This uses the author's product name.
7. **Line 989**: add a note under the block:
   - `*Opener shared verbatim with Couchsurfing Chronicles Sinfonia's Digital Footprint harassment (\`couchsurfingchroniclessinfonia.md:596\`); author to rule whether the reuse stands or that set suppresses it once §11 has fired.*`
8. **Line 980** (AUTHOR, optional): cut `u can only spend it here`. Tony then no longer states the mechanic, and line 979 still carries the joke.
9. **Line 1890**:
   - old: `added to the coin pool (canon edits to \`design/economy/\` pending the author's OK — the room's pool-format entry is in \`canon_proposals.md\`, coin #29, $MCUM)`
   - new: `added to the coin pool (applied 2026-11-10: \`shitcoin_master_pool.md\` #29, $MCUM; exception in \`icq_airdrops.md\` §1.4)`
10. **Line 2097**:
    - old: `pool entry proposed, not applied;`
    - new: `pool entry applied (#29, $MCUM, 2026-11-10);`
11. **Line 1966**:
    - old: `All-lowercase, no punctuation, chronically online, competent scammer, crypto-only for actual ICQ purchases, vintage "Uh-oh!". Older dollar/SOVS-facing ads are historical pitch copy; this quest's transaction follows the author's crypto rule.`
    - new: `All-lowercase, no apostrophes, clipped full stops (as AD-01), chronically online (3-6 AM), competent scammer; ICQ avatar is a pixelated avi in Oakleys indoors (DWD:59, 607). This quest's purchase is crypto-only by ruling (q10: A); canon elsewhere also prices him in SOVS and dollars, which this quest neither reuses nor reclassifies. Physically rents a Cyberspace Kavarna terminal (Dmitri, Katka); existing sprite slot "Tony420 Fake Crypto" (Cyberspace Kavarna PNG reqs).`
12. **Lines 1966 and 2025** (AUTHOR): present the alternate ID `debaucheryville_npc_tony420_01`, with the profile at `design/worlds/debaucheryville/npcs/Cyberspace_Kavarna/npc_tony420.md`. That follows the template `[city]_npc_` and the Miss Morphine precedent. Present it beside `shared_npc_tony420_01`, and say that `design/worlds/shared/npcs/` does not exist.
13. **Line 2025, item 6**: append `Profile must also carry the canon relationships omitted from the draft (Hamstradamus, richfield69, Sauce Apostates/Döner Council admin, MemeLord.exe SWF trade, Chadwick's GO LIVE chat) and the Döner Debate in-person appearance (GDD-Q:373-380).`
14. **After line 1004**: add `*§11 fires regardless of Operation Script Kiddie state; per Katka, exposure never stops him (\`npc_cybergoth_katka.md:112\`).*` (AUTHOR to confirm.)

---

## 4. Conflicts inside canon for the author to rule on

- **A. Has the party met him in person?** Base-game Debaucheryville has him physically seated at a Kavarna terminal for three years (`npc_dmitri_the_router.md:214`; `npc_cybergoth_katka.md:176, 210, 313`; Ecosystem Audit :75). The Shamsterdam Döner Debate treats seeing him as a "major reveal": "...Tony? You're... real?" (GDD-Q:378, 651). Both cannot hold unless the Kavarna Tony is never identified to the bros.
- **B. Voice rule vs practice.** `icq_airdrops.md:80` says "no punctuation, no capitals". The same file's AD-01 uses full stops (:113-114) and AD-04 has "HODL!!!1" (:159). "BANANA" (`bacchanusbeachbeatdown.md:193`), "Yeh, also includes PDF…" (DWD:76), "Wanna buy shrooms off my cousin's Zune?" (DWD:22) and "wassup bros! …" (`club_flyers.md:365`) all break it too. Rule on whether shouted tokens and full stops are allowed.
- **C. Currency.** CLAUDE.md says "All money is SOVS… never dollars", yet several live documents still read "$30 Xanax":
  - `game_design_document.md:116, 220`
  - `wifihotspots.md:7`
  - `sinfonia.md:206`
  - DWD:57, 87
  
  Tony prices in SOVS throughout Couchsurfing (Debaucheryville, Publandia, Shamsterdam) and DWD, but in MoonCum in Sinfonia Couchsurfing (:372, 596). `intoxication_law.md:61-63` calls his crypto payment mechanics canon. Rule on whether Tony is crypto-only, mixed, or per-city.
- **D. Misfiled block in sinfonia.md.** Lines ~170-220 are Debaucheryville content: the Velvet Curtain Club, the Absinthe Cathedral, the Hostel Lobby hotspot and the Tony "$30" line. This is what created final.md's false "Sinfonia hostel-lobby hotspot".
- **E. `tony420_unlocked`** is required by the Meme Black Market trade but set nowhere. A second, differently named condition also exists: `tony420_contact_unlocked_and_rare_memes_acquired` (`debaucheryville_interactions.json:2811` vs :2999). That leaves no defined way to unlock his contact.
- **F. Duplicate quest files.**
  - `design/Quests/darkwebdossiercrossoverevents.md` has `<<<<<<< HEAD` / `=======` markers (lines 2-4), real place names ("Temple Bar", "Czech Republic Bath Salts") and "SOVS" casing. The `general_quests/` copy is the clean one.
  - `design/Quests/greatdonerdebate.md` differs from `general_quests/greatdonerdebate.md` on every line, probably line endings only.
  - Legacy `design/World Design/**` duplicates mirror the same Tony lines.
- **G. Handle identity.** Katka says Tony runs "four handles" on one wallet (`npc_cybergoth_katka.md:112, 301`). It is unruled whether "Tony420" is the person or one mask.
- **H. Real person.** DWD:69 "Plot twist- Tony420 gets busted as being a ketamin fueled Elon Musk" is an unrealized note that ties him to a real person. It is never staged anywhere. Rule whether it's live canon.
- **I. Mystery Meat hook.** "Unlocks unique lore when consumed during Tony420 interaction" (`mysterymeatcart.md:106, 141`) is never defined anywhere.
- **J. Product split.** "Flintstone fentanyl" (canon pitch), "fentanyl vitamins" (DWD:280), "FLINTSTONES FENTANYL VAPES… 25 Sovs" (DWD:398, sender unattributed) and "Fentanyl-Flavored Flintstones Gummies – Non-Edible" (`wifihotspots.md:8`) may be one product or several. `intoxication_law.md:82` leaves Flintstone Fentanyl undesigned.
