# Old NPC conversations and easter eggs: audit

Date: 2026-11-15. Bead: Eurobound-rras. Asked for by the author on the Eurobound Desk (Eurobound-rras-q1): "Have it audited first and show me what is worth keeping".

Nothing was changed. This is a reading of the old text against the current rules. The verdicts are a recommendation; the author decides.

## What was read

- `game/assets/data/npcs/dialogue_trees/debaucheryville_dialogue.json` (dated 2025-09-15): three conversations, plus status lines and world-state lines.
- `game/assets/data/npcs/easter_eggs.json` (dated 2025-09-15): six easter eggs, two "behavioral" eggs, a debug block, an analytics block.
- `game/assets/data/npcs/dialogue_trees/behavioral_triggers.json`: one entry, no text.

The game shows none of it today.

## The short version

- **Keep as is: 1. Keep with a fix: 11. Cut: 8.** Three more blocks are not writing at all (debug, analytics, the triggers file) and are a code matter.
- **Vlad's own lines are the best thing here.** Most match his approved profile word for word.
- **Bobo is good while he is pitching and breaks the rules when he turns sincere.** The second half of his conversation ends on hope, coffee and a group hug.
- **"Dmitri the Exchanger" is not a character.** He has no profile, and his first name is already taken by Dmitri "The Router".
- **The bros' side is the weakest part everywhere.** Their choices are scam-aware ("That's just a sales pitch...", "This seems sketchy...") or kind and wise ("Things will get better."). Both break standing rules.

## Do the three NPCs still exist?

| NPC id in the old data | Who it is now | Status |
|---|---|---|
| `vlad_validator` | Vladimir "Vlad" Kryptovich, `design/worlds/debaucheryville/npcs/Velvet_Curtain_Club/vlad_the_validator.md` | Exists. Approved canon (ledger, 2026-08-03). Not struck. |
| `crypto_clown` | Bobo "The Blockchain" Bitsworth, `design/worlds/debaucheryville/npcs/Cirque_du_Shady/crypto_clown.md` | Exists. Approved canon. Not struck. |
| `shadow_exchange_dealer` | "Dmitri the Exchanger" | **No profile, no catalog row.** The Shadow Exchange is staffed by Mrs. Rata, The Exchange Broker, the Token Goblin, The UV Man and others. The name also collides with Dmitri "The Router" (Cyberspace Kavarna). He appears only in old engine data. |

Two things the old data gets wrong about the two real NPCs:

- **Vlad works the inside door, not the street door.** His profile says the street door is Kamil's. One egg places Vlad at `velvet_curtain_entrance`.
- **The NPC ids do not match.** The profiles use `debaucheryville_npc_vip_backroom_bouncer_01` and `debaucheryville_cirque_crypto_clown_01`.

## Verdict table

### Conversations (debaucheryville_dialogue.json)

| # | Item | Verdict | Why |
|---|---|---|---|
| 1 | Vlad: whole conversation (7 nodes) | KEEP WITH A FIX | Vlad's lines are strong and mostly match his profile. The bros' reactions make them the sane ones; one node bails out; 2 choices lead nowhere. |
| 2 | Bobo: the pitch (greeting, performance, repeat visit) | KEEP WITH A FIX | Funny and in voice. Tip price is in "KC". Two bro choices are scam-aware. 3 choices lead nowhere. |
| 3 | Bobo: MBA confession | KEEP WITH A FIX | "Harvard" was struck by the author on 2026-11-11. Both replies are sincere sympathy and lead nowhere. |
| 4 | Bobo: the tip ("first tip I've gotten all week") | KEEP WITH A FIX | The line is in his approved profile. The price is "KC", the flag is called `bobo_humanized`, and it hands out a 50% shop discount nobody ruled on. |
| 5 | Bobo: "honest moment", coffee, friendship path | CUT | The joke turns into sincerity. Bobo finds hope; the bros nod wisely and offer a group hug. |
| 6 | "Dmitri the Exchanger": whole conversation (2 nodes) | CUT | Not a character. Generic. Bro choices are scared, scam-aware and crime-stopping. 4 of 5 choices lead nowhere. |

### Status lines and world-state lines (same file)

| # | Item | Verdict | Why |
|---|---|---|---|
| 7 | Vlad: 3 status lines | KEEP AS IS | In voice, match his profile. |
| 8 | Bobo: 3 status lines | KEEP WITH A FIX | One good, one fine, one where Bobo drops the delusion and pities himself. They also differ from the three in his profile. |
| 9 | Dmitri: 3 status lines | KEEP WITH A FIX | Two of the best lines in the file, said by a character who does not exist. They need a speaker. |
| 10 | Vlad: 3 world-state lines | KEEP WITH A FIX | Two keepers. The third is flat and leans on a "social media fame" system that does not exist. |
| 11 | Bobo: 2 world-state lines | KEEP WITH A FIX | One keeper. The other fires when the bros "helped other NPCs", which makes them do-gooders. |
| 12 | Dmitri: 2 world-state lines | CUT | Boring and professional. Depends on a police system that does not exist. |

### Easter eggs (easter_eggs.json)

| # | Item | Verdict | Why |
|---|---|---|---|
| 13 | `crypto_portfolio_confession` (Vlad) | KEEP WITH A FIX | Best egg. Price is in dollars and disagrees with the ruling. Reward item does not exist. The closing line goes sincere. |
| 14 | `clown_breakdown` (Bobo) | CUT | Third telling of the same MBA reveal, and the weakest. |
| 15 | `dmitri_police_scare` | CUT | Not a character. Sitcom-generic. Needs a police-siren system. |
| 16 | `meta_commentary_vlad` | CUT | Breaks the fourth wall. The game never winks. |
| 17 | `cross_world_reference` (Vlad) | CUT | Treats the bros as real legends. They are the punchline, never aspirational. |
| 18 | `seasonal_crypto_reference` (Vlad) | KEEP WITH A FIX | The line and the fallback are good. The reply teaches a lesson. It fires on the real-world calendar. |
| 19 | `grease_fingers_magnet` (behavioral) | KEEP WITH A FIX | Only the title name is worth keeping. One shared greeting for every NPC flattens them all. |
| 20 | `crypto_conversion_success` (behavioral) | CUT | Rewards the bros as crypto experts. The one line is generic. |

### Not writing: code concerns

| # | Item | Verdict | Why |
|---|---|---|---|
| 21 | `debug_easter_eggs` (developer mode) | CUT | A debug door, already off in production. The game has its own debug commands. Its one line talks to the player. |
| 22 | `analytics_tracking` | CUT | Four descriptions of statistics. No tracking system exists. |
| 23 | `behavioral_triggers.json` | CUT | One entry, no text. Names NPC groups that do not exist. Disagrees with egg 19 on the number. |

## Lines worth keeping, word for word

### Vlad

From the conversation:

> "Whoa there, tourist. This establishment operates on proof-of-stake entry protocols."

> "Fiat mentality detected. Please update to digital native mindset." (to Lord Pilsner)

> "Respectable follower count, but what's your engagement rate?" (to Chadwick)

> "Bro, you even lift... smart contracts?" (to Bradley)

> "Oh man, you're totally ngmi. Look, imagine if every drink order was verified by a distributed network of—"

> "—every drink order, verified, immutable, forever. Anyway. Point is: you're not on the list. You're barely on the blockchain."

> "Whoa! Actual digital scarcity! Welcome to the future, citizen. VIP section is through here."

> "Nerd? NGU technology is the foundation of Web3 social infrastructure! Do you even understand market cap fundamentals?"

> "Back again? Your wallet address is starting to look familiar..."

> "Still think I'm a nerd? My portfolio says otherwise... well, it used to."

> "VIP access is still active, diamond hands."

Status lines (keep as is):

> "Your cognitive hash rate appears compromised. Try some nootropics."

> "Hygiene protocol violation detected. Please sanitize hands before touching anything."

> "Social credit score dropping in real-time, my dude."

World-state lines:

> "Debaucheryville has better crypto infrastructure than Publandia's outdated banking system."

> "Beer is just proof-of-work for your liver, am I right?"

From the eggs:

> "Look... between you and me... I bought Bitcoin at $68,000. My mom still thinks I'm a financial advisor."

> "Anyway... back to verifying the VIP list..."

> "New year, new portfolio! This time I'm diversifying into... *checks phone* ...oh no, not again..."

> "Diamond hands, right? ...Right?"

### Bobo

> "Step right up! Witness the amazing blockchain balloon animals! Each one represents a unique NFT opportunity!"

> "A distinguished investor! Let me show you my business plan for decentralized entertainment!" (to Lord Pilsner)

> "Social media influencer! We should collaborate! I have so many content ideas!" (to Chadwick)

> "You look strong! Want to invest in my gym-meets-blockchain startup idea?" (to Bradley)

> "Behold! I shall make your fiat currency... DISAPPEAR! And replace it with exciting investment opportunities!"

> "You... you actually gave me money? For my performance? I... thank you. This is the first tip I've gotten all week."

> "Back for another show? This time I've got a new crypto-circus fusion concept to pitch!"

> "You came back! That means my performance was memorable, right? Right?"

> "Hey! My friend is back! Want to hear about my latest business plan? This one's definitely going to work!"

> "You look like you need some hair of the blockchain that bit you!"

> "Welcome to the club! I lost everything on DogeCoin derivatives!"

### Said by "Dmitri", worth keeping if they get a real speaker

> "Embarrassment is just another currency. I can exchange it for regret."

> "I don't touch money that's been... wherever yours has been."

> "Rough night? I have some... recovery supplements. Extra charge."

## Keep with a fix: the rule broken and the kind of fix

No fixed lines are written here. Each entry names the problem and the kind of work it needs.

### 1. Vlad: whole conversation

- **Bros as the sane ones.** The reaction tags have Lord Pilsner on "eye_roll" and Bradley on "facepalm" while Vlad talks. That makes the bros the straight men and Vlad the joke. The rule is the other way round: the bros are the punchline. Fix: the reactions are re-decided under the bros-are-doofuses rule.
- **Bail-out ending.** One node is named "longer explanation" and delivers the opposite:
  > "Market cap fundamentals, tokenomics, the whole... look, just... just stand over there and don't touch anything, okay?"

  His profile's running gag is "Every crypto explanation gets longer and more incomprehensible". This one gives up. Fix: Writers' Room, or cut the node.
- **Greeting disagrees with the profile.** The data says "Whoa there, tourist." The profile's default greeting says "Whoa there, chad." Fix: author picks one.
- **A lost line.** "VIP access is still active, diamond hands." is in the file but can never be read: its entry and the next share the same key, so only the second survives. Code fix.
- **Bribes.** The NFT Screenshot and Electrolyte Pack bribes are in his profile, but neither item has an item file. Fix: item rulings before these choices can work.

### 2. Bobo: the pitch

- **Money.** The tip choice costs `"currency": "KC", "amount": 1`. All money is SOVS. Fix: the unit, and the author confirms the amount.
- **Scam-aware bros.** Two choices have the bros seeing through him:
  > "That's just a sales pitch..."

  > "Are those real coins?" (Lord Pilsner tagged "skeptical", Chadwick tagged "fact_checking")

  The bros are never scam-aware. Fix: these choices are re-decided or dropped.
- **Decent, sensitive bros.** Reaction tags such as "feels_bad", "protective_anger", "secondhand_embarrassment" and "confused_but_supportive" give the bros taste and a conscience. Fix: same as Vlad's.
- **A minigame.** The performance starts `rigged_coin_toss`. The profile mentions a rigged coin toss; nothing is designed or built.

### 3. Bobo: MBA confession

- **Struck by ruling.** The line says "an MBA from Harvard". The ledger, 2026-11-11: "Strike 'Harvard MBA' from Bobo." His profile now says "MBA from a prestigious school". Fix: bring the line in step with the ruling.
- **Sincere bros.** The replies are "That's actually really tragic." (Lord Pilsner tagged "genuine_sympathy") and "So why not get a normal job?" (tagged "practical_question"). One is a redemption beat for the bros and the other is sound advice. Both lead to nodes that were never written. Fix: the replies are re-decided.
- **Told three times.** The same reveal is in this node, in egg 14, and as a hidden trigger in his profile. Fix: author picks one home for it.

### 4. Bobo: the tip

- **Money.** Same "KC" problem as above.
- **Flag names that show the intent.** The node sets `bobo_humanized` and `player_showed_kindness`. They exist to open the path in item 5. Fix: they go if item 5 goes.
- **An unruled number.** `unlocks_shop_discount: 0.5`. A 50% discount is an economy number and needs an author ruling.
- **The follow-up.** The only choice is "Are you okay?", with Chadwick tagged "stopping_recording", which is a growth moment for him. The profile already has an approved answer to that exact question, and it keeps the delusion:
  > "Okay? I'm living the dream! Who needs traditional success when you have... artistic freedom!"

  The old data replaces it with the sincere version in item 5.

### 8. Bobo: status lines

- "Hey, at least you're not performing for pocket change like me!" has Bobo seeing himself clearly. His profile's line for the same status keeps him deluded. Fix: author picks which set of three is canon; the data and the profile disagree on all three.

### 9. Dmitri: status lines

- **No speaker.** The lines are good; the character is not real. Fix: an author ruling on who says them (an existing Shadow Exchange NPC or nobody).

### 10. Vlad: world-state lines

- "Saw your TikTok blow up. That's some serious engagement metrics." is the flattest line Vlad has, and it fires on `gained_social_media_fame`, a system that does not exist. Fix: Writers' Room or cut. The other two lines stand.

### 11. Bobo: world-state lines

- "You're building quite the reputation. Want to invest in my comeback tour?" fires on `helped_other_npcs`. Bros who go around helping people are not these bros. Fix: the trigger is re-decided. The DogeCoin line stands.

### 13. Egg: Vlad's portfolio confession

- **Money, and it disagrees with a ruling.** "$68,000" is in dollars. The ledger, 2026-11-11: "Vlad's '$60,000' becomes 60,000 SOVS", and his profile says he "bought Bitcoin at 60,000 SOVS". Fix: bring the number and unit in step with the ruling.
- **A reward that does not exist.** `Crypto_Sympathy_Card` has no item file. New items need an author ruling.
- **An "experience" reward.** 50 XP for listening. XP is real (`design/mechanics/Progression/xpgain.md`), but no rule gives XP for conversation, and the number is unruled.
- **Sincere close.** After the confession:
  > "Thanks for listening, man. Most people just want to hear about my 'gains'."

  The joke softens into a thank-you. The fallback line already does the job. Fix: cut or Writers' Room.
- **The flag is called `vlad_humanized`.** Same tell as Bobo's.

### 18. Egg: Vlad's new-year portfolio

- **A lesson.** The reply is:
  > "Maybe this year I'll actually research before investing..."

  Vlad learns something. No lessons, at any scale. Fix: cut the reply or Writers' Room.
- **Real-world calendar.** It fires on 1 to 7 January on the player's own computer. The game runs on its own clock. It also checks a player level. Fix: a mechanics ruling on the trigger.
- **Reward item** `New_Year_Resolution_List` does not exist.

### 19. Behavioral egg: grease magnet

- **One line for everybody.** Every NPC in the game opens with:
  > "Ah, our local grease magnet returns!"

  NPCs are never boring and each has a voice. Fix: the shared greeting goes.
- **Worth keeping:** the title "Grease Lightning".
- **Systems that do not exist:** player titles, a "social media trigger", and 200 XP.

## Cut: the worst line in each

### 5. Bobo: "honest moment", coffee, friendship path

> "Okay? I check my old crypto wallets every morning hoping for a miracle. My Harvard classmates cross the street when they see me. But... this interaction? This gives me hope."

The bros' choices after it:

> "Want to grab a coffee and talk?"

> "Things will get better."

That last one is tagged Lord Pilsner "wise_nod", Chadwick "inspired", Bradley "group_hug_offer". The node is also marked `screenshot_moment` with the sharing tag `crypto_clown_humanity_revealed`. The irony resolves into sincerity, the bros come out wise and kind, and nothing undercuts it. It also still says "Harvard". Both choices lead to nodes that were never written.

Worth saving from the wreck: "I check my old crypto wallets every morning hoping for a miracle" is already in his profile as his secret shame, and "My Harvard classmates cross the street when they see me" is a good image apart from the struck word.

### 6. "Dmitri the Exchanger": whole conversation

> "Psst. You look like tourists who need... better exchange rates. I can help."

A stock back-alley money changer with no name joke and no angle. The bros' choices are worse:

> "This seems sketchy..."

> "[Report to authorities]"

> "That's highway robbery!"

The bros are never afraid, never scam-aware and never crime-stoppers. The scene also assumes a second currency to exchange into, when all money is SOVS, and a police contact that does not exist.

### 12. Dmitri: world-state lines

> "Ah, I see you've been successful. Perhaps interested in premium services?"

Polite, professional, about nothing.

### 14. Egg: clown breakdown

> "You know what the worst part is? I actually went to business school. Magna cum laude. Now look at me..."

The same reveal as item 3, ending on a shrug. Its trigger needs a world state (`performance_failed`) and two items that do not exist. Its follow-up, "Maybe I should call my parents... they still think I'm 'following my dreams'.", is the one line with a pulse, and it is the same joke as Vlad's mom.

### 15. Egg: Dmitri's police scare

> "Quick! You didn't see me here! I'm just... selling totally legal... tour guides! Yes, tour guides!"

### 16. Egg: meta commentary Vlad

> "Did you just... screenshot our conversation? Dude, I'm not an NPC in some satirical RPG game!"

Followed by:

> "Wait... are we in a game right now? Is someone controlling you?"

It names the game as a satire to the player's face, with a "record_scratch" sound and a `Meta_Awareness_Token` reward. It also needs the game to detect a screenshot.

### 17. Egg: cross-world reference

> "Wait, you're the legend from Publandia! I saw the footage of your epic pub crawl. That's some serious social proof!"

Followed by "Celebrity status confirmed! Welcome to the elite tier." and a free pass into the VIP Backroom. The bros win, sincerely, with no undercut.

### 20. Behavioral egg: crypto conversion

> "Finally, someone who gets it!"

Ten crypto chats earn the title "Crypto Whisperer", "insider information access" and an `Honorary_Blockchain_Certificate`. It pays the bros for being clever about crypto.

## Structural facts

### The 13 of 23 choices that lead nowhere

Each points at a node that was never written.

Vlad (2):

1. "[Bribe with Electrolyte Pack]" → `vlad_bribe_success`
2. "Finally..." → `conversation_end`

Bobo (7):

3. "Are those real coins?" → `crypto_clown_defensive`
4. "[Walk away]" → `crypto_clown_desperate_follow`
5. "That's just a sales pitch..." → `crypto_clown_exposed_but_persistent`
6. "That's actually really tragic." → `crypto_clown_gratitude_spiral`
7. "So why not get a normal job?" → `crypto_clown_pride_defense`
8. "Want to grab a coffee and talk?" → `crypto_clown_friendship_path`
9. "Things will get better." → `crypto_clown_hope_restored`

Dmitri (4):

10. "This seems sketchy..." → `dmitri_defensive`
11. "[Report to authorities]" → `dmitri_panicked`
12. "That's highway robbery!" → `dmitri_negotiation`
13. "[Make exchange]" → `shop_interface`

Two of these (`conversation_end`, `shop_interface`) read like intended exits, not missing scenes. The other eleven are scenes nobody wrote.

### Other structural problems

- **Two lines are silently lost.** In both "repeat visit" entries (Vlad's and Bobo's) the key `conditions` appears twice. A JSON reader keeps only the second, so Vlad's "diamond hands" line and Bobo's "My friend is back!" line can never be read.
- **Two Vlad nodes simply stop.** `vlad_explanation_continues` and `vlad_longer_explanation` have no choices.
- **The Konami code is incomplete.** The debug egg lists eight directions and no buttons.
- **Two grease counters disagree.** `easter_eggs.json` says 5 or more; `behavioral_triggers.json` says 3 or more.

### Mechanics the lines assume that do not exist

- Player level checks, player titles ("Grease Lightning", "Crypto Whisperer"), and XP handed out for conversations.
- A police system: sirens nearby, "police attention", a police contact flag.
- Screenshot detection, "screenshot moments", social sharing triggers and social media fame.
- A real-world calendar trigger (the game has its own clock, `game/core/game_clock.gd`, so the late-night trigger on egg 13 could work).
- A currency exchange with a commission. All money is SOVS; koruna does not exist.
- The `rigged_coin_toss` minigame, a shop discount, and the `VIP_Backroom` unlock.
- "Bros helped other NPCs" and "cross-world celebrity" world states.
- Eight reward or trigger items with no item file anywhere: `Crypto_Sympathy_Card`, `Business_Degree_Fragment`, `Suspicious_Business_Card`, `Meta_Awareness_Token`, `Guinness_Foam_Mustache`, `New_Year_Resolution_List`, `Honorary_Blockchain_Certificate`, and `Rare_NFT_Screenshot` (named in Vlad's profile only).
- NPC groups `all_bartenders` and `posh_npcs`.

### Blocks that are code concerns, not writing

- `debug_easter_eggs`: a developer-menu door. The game already has `game/core/debug_commands.gd`.
- `analytics_tracking`: four sentences describing statistics. Nothing collects them.
- `behavioral_triggers.json`: no code reads it.
- `easter_eggs.json` as a whole: no game code reads it. Only a validator test (`Tools/tests/test_validate_data.py`) opens it.
- `debaucheryville_dialogue.json` is required by `game/core/data_repo.gd`, `Tools/validate_data.py` and `game/tests/unit/test_data_repo.gd`. Retiring any of it means those three change with it (already recorded on the bead).

## Recommendation

1. Keep Vlad's lines. They are the reason this file is worth anything.
2. Keep Bobo's pitch and tip. Cut everything after the tip.
3. Cut the "Dmitri" conversation and eggs. Rule separately on whether his three status lines go to a real Shadow Exchange NPC.
4. Cut eggs 14, 15, 16, 17 and 20.
5. Send the keep-with-a-fix items to the Writers' Room only for the parts that need writing (the bros' choices and reactions, the two bail-out lines). The rest are unit, number and ruling fixes.
6. Hand the three non-writing blocks to code cleanup.

This is a recommendation. The author decides.
