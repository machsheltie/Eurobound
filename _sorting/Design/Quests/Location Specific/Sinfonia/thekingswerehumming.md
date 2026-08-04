# Sidequest: The Kings Were Humming

## 📋 Quest Identity
- **Quest ID:** `sinfonia_sidequest_the_kings_were_humming_01`
- **Display Name:** "The Kings Were Humming"
- **Satirical Subtitle:** "Sixty seconds, five hundred Sovs, one guy eating candy"
- **Quest Giver:** Nobody. Aaron the Unflappable (`sinfonia_npc_aaron_unflappable_01`) offers the party a chair and nothing else @ Aaron's Corner Table (`aarons_corner_table`), The Black-Tie Backroom (`sinfonia_operahouse_blacktie_backroom_01`)
- **City:** Sinfonia
- **Recommended Level:** 5-7
- **Estimated Duration:** ~6 minutes (single scene, one time only)

---

## 🎭 Core Premise

### The Setup

**What the bros THINK is happening:**
> They have found the soft seat. A room full of counts, countesses, and men whose cufflinks cost more than the flight — and in the corner, alone, unguarded, sits a man in a rumpled jacket drinking a milk cocktail and eating candy at a poker table. The whole room has clearly been too polite to take his money. That politeness is a market inefficiency. They are not polite. They are three Americans with five hundred Sovs on deposit, a working knowledge of tuxedo cinema, and the nerve nobody else in Sinfonia has. This is the hand they tell people about.

**What is ACTUALLY happening:**
> Aaron is the best player in the building and has been for four years. The room is not too polite to take his money; the room has tried, extensively, and stopped. He plays on feel, says so out loud, in advance, at conversational volume, to anyone who asks and several people who don't. The bros ask. He tells them. They hear a man talking himself into a mistake, push the entire 500 Sovs door collateral in on 7-2 offsuit, and are called instantly by pocket kings. It takes under a minute. Aaron is then extremely nice to them, gives them a carton of candy cigarettes and a worthless aluminum token, and wishes them luck.

**Why it's funny:**
> The player never touches a card. There is no bet slider, no odds display, no moment where the outcome is in question — the scene is a cinematic and the party is furniture in it. The only input the player has is choosing *which* embarrassing sentence comes out of a bro's mouth next, and every option leads to the same swept pot. The bros narrate tells off a man who has not moved, while six feet away at the next table Graf von Zittrig — who has an actual, documented, learnable cufflink tell — bluffs a stranger in full view of nobody. Nothing in the scene points at that. Nothing in the scene points at anything.

---

## 🎯 Satirical Targets
- **Primary Target:** Movie-derived expertise. Three men who have seen a film about a card game, in a room where the card game is happening, applying the film. The confidence is total, the vocabulary is fluent, and none of it is attached to anything.
- **Secondary Targets:** The tourist read of "local weirdo" as "easy money"; the conviction that dressing correctly for a room means understanding the room; the specific American belief that a large enough number is itself a strategy ("Show him what American capital looks like"); losing everything and recategorizing it as a portfolio event.
- **Cultural Specificity:** Sinfonia's whole hustle in one table — a gilded room where the gambling is dressed in opera-house tailoring, everyone is unfailingly courteous, and the courtesy is load-bearing. Nobody in the Backroom warns anybody about anything. The chandeliers are genuinely beautiful. The chips are genuinely silver. The man in the corner is genuinely unbeatable and no member of staff has ever mentioned it, because nobody has ever asked and it would be rude to volunteer.
- **Y2K/Era References:** Chadwick filming an aluminum token for an audience of eleven; "it's on the chain" delivered with total sincerity in 2003; the bros' entire tuxedo-cinema reference library consisting of one film they have both seen on a plane.

---

## 📖 Quest Structure

### Quest Initiation

**Trigger:** `blacktie_event_kings_were_humming_01` — the party approaches Aaron's Corner Table inside The Black-Tie Backroom with entry conditions met (Anton's attire and stat check passed, 500 Sovs collateral posted at the deposit window). Fires **once per save, ever.**

**Location:** `aarons_corner_table`, a named zone of the Backroom main floor. Felt-covered corner table, its own low pendant lamp, no house chip rail, no dealer plaque, no bet-placement markings, set off the traffic flow. The player has to choose to walk over. The bros make that choice for the party.

**Prerequisite state:** the 500 Sovs is on deposit as house chips. It is not the player's gold; the gold above 500 Sovs never enters this scene in any form.

---

### The Door — Pre-Beat (Anton)

*Two floors and one staircase upstream, before any of this. Anton works the bottom of the stairs. He assesses the party the way he assesses everyone, which is completely.*

**Anton the Doorman** (`sinfonia_npc_anton_doorman_01`), *if the party clears attire, stats, and collateral:*
> "Your attire is... acceptable. Your collateral is... sufficient. Your chances of leaving with it are... statistically improbable. Welcome."

**Lord Pilsner:** *already past him* "Heard the first part."

---

**If the party is holding less than 500 Sovs:**

**Lord Pilsner:** "500 Sovs COLLATERAL?! That's... that's a lot of döner."

**Anton:** "It's also the minimum. Döner is not accepted."

*The party is turned around at the bottom of the stairs. Anton does not raise his voice, does not escalate, and does not explain the policy a second time. The Backroom does not open. **The encounter cannot fire underfunded** — a bounced party never reaches the main floor, never sees the corner table, and Aaron never learns that anyone came by, because nobody has ever told him one thing about the door.*

---

### Binding Staging Rules

These are author-locked and apply to every implementation pass, forever:

1. **The betting UI never opens at this table.** No bet slider, no call/raise/fold prompt, no chip-drag, no hand display, no pot-odds readout, no "your cards" panel. Not at any beat, not on any path, not in any later build.
2. **The player never holds cards.** There is no version of this scene in which the party is dealt in. The bros are dealt in. The party watches the bros.
3. **The outcome is fixed.** Every pick, every branch, every combination of the three player inputs reaches the identical result: the 500 Sovs collateral is lost, both items are granted, Aaron goes ambient. There is no win state and no near-miss.
4. **The table is visually distinct from the room's real, fair, playable poker tables.** Different felt tone, its own pendant lamp, no house dressing. A player must never be able to confuse Aaron's corner with a table they can sit down at — the Backroom's actual poker, roulette, and blackjack tables are real minigames with real house-edge math and this is not one of them.
5. **Nothing explains it.** No dealer aside, no local tipping the player off, no Madame Karten explainer, no narrator verdict, no tooltip, no achievement string, no post-hand summary card that accounts for why Aaron wins. Not now, not in a patch. The player watches it and is trusted.
6. **One time only.** No rematch, no second scene, no difficulty tier, no "beat Aaron" content.

---

### Structure: Nine Beats, Three Picks, One Outcome

There is **no binary path choice in this quest**, by construction. The scene is a spectator cinematic and a fork would imply winnability. What the player gets instead is three **pick-a-line** beats: at each, the party chooses which terrible sentence a bro says next. Every option at every pick is a different flavor of unearned tuxedo-cinema swagger, every option is written in full below, and **all nine combinations converge on the same beat immediately after.** Picks are cosmetic-comedic only; nothing tracks them, nothing rewards them, nothing gates on them.

---

#### Beat 1 — The Read

*The corner table. Aaron is stirring a double White Russian with a candy cigarette. The party stops about six feet out. The bros conduct their assessment out loud, at full volume, in front of the man they are assessing.*

**Chadwick:** "Look at this guy. He's drinking melted ice cream and chewing on sugar sticks. He's weak."

**Aaron the Unflappable** *(taking a long dramatic drag off the candy cigarette; not remotely offended; genuinely offering)*:
> "It's a double. You want one? They do 'em right here, they don't skimp on the Kahlúa."

*He bites the end off. The CRUNCH lands in the exact gap where Chadwick expected a reaction. Chadwick reads this as fear.*

**Lord Pilsner:** *seating himself with a great deal of ceremony* "Boys. I've done Casino Royale. Twice. Once on a plane."

*He signals the dealer and asks for **the shoe**. The dealer — professional, rotating, entirely unbothered — brings a shoe, sets it down, and deals Sinfonian Hold 'Em out of it, two cards a man, without a word or a change of expression. Lord Pilsner nods slowly, as though something he suspected has been confirmed.*

*At the neighboring table, six feet away and in plain view, **Graf von Zittrig** picks up a bluff and adjusts his cufflinks. He does this every time. It is the most reliable tell in the building and it is the first thing any player in the Backroom learns. All three bros are facing the other direction. Nobody in the scene points this out. Nobody in the scene ever points this out.*

---

#### PICK 1 — "The Credentials"

**Prompt:** *Somebody is about to explain the table.*

**Option A — Lord Pilsner, "The Tell Reader":**
> "Three tells. Three. He touched the glass — that's tension. He *didn't* touch the glass — that's ALSO tension, it's the same tell inverted, which is worse. And the candy? Bro. The candy is a comfort behavior. I read a book about this. I read most of a book about this."

**Option B — Chadwick, "The Franchise":**
> "Chat, I've seen every single one of these movies. Both of them. The one with the tuxedo, and then the other one, with the tuxedo. So when I tell you this guy is playing scared, understand that I'm bringing, like, a film-studies background to this."

**Option C — Bradley, "The Analyst":** *(flat, unhurried, absolutely certain)*
> "Statistically, a man who orders dessert at a card table folds sixty percent of the time. That's a documented number. I couldn't tell you where it's documented. But it's not in dispute."

---

*Whichever fires:*

*Aaron listens to all of it, all the way through, with real interest, the way you'd listen to someone describe a dream they had. Then he pushes the carton an inch toward them in case anybody wants one. Nobody takes one. The dealer deals. The Gräfin at the next table sips champagne and says nothing, which is what she says.*

---

#### Beat 2 — The Shove

*The hand runs. The bros' cards are 7-2 offsuit — visible to the player, on the felt, face up in the cinematic framing, never in a hand-display UI. The bros are looking at Aaron.*

---

#### PICK 2 — "The Shove"

**Prompt:** *Five hundred Sovs is about to cross a table.*

**Option A — "The Cuff" (Lord Pilsner):** *He stands. He adjusts a cuff. There is no cufflink in the cuff; it is a rented shirt and the sleeve is held with a button like everyone else's.*
> "I want the whole thing in. All of it. And I want him to watch me do it slow."

**Option B — "The Order" (Chadwick):** *He turns to a server carrying nothing but a tray of champagne flutes.*
> "Martini. Shaken." *(back to the table, without waiting for an answer, without ever receiving one)* "That's how you set a tone. Now — everything in the middle."

**Option C — "The Accent" (Bradley):** *He delivers it in an accent. It is not from anywhere. It arrives somewhere between four countries and lands in none of them.*
> "All in, my good friend. The whole of it. I do hope that isn't inconvenient for you."

---

*Whichever fires, the button is the same, and it is Lord Pilsner's, and he says it to the dealer, to the table, and to Sinfonia:*

**Lord Pilsner:** "Make the bet big. Show him what American capital looks like."

*Every chip the party posted at the door goes across the felt. Exactly 500 Sovs in house silver. Not one coin more.*

**Narrator:**
> "Five hundred Sovs in silver chips crossed a table in Sinfonia at one in the morning. Two other tables were mid-hand. The string quartet did not stop."

---

#### Beat 3 — The Vibes Speech

*Lord Pilsner has just narrated, at full volume, the three tells he believes he has read off a man who has not moved. Aaron heard the whole thing. He genuinely wants to help.*

**Aaron the Unflappable** *(warm, unhurried, sincerely trying to be useful)*:
> "You guys are calculating numbers. You're looking at the board like it's a math test. Poker isn't math, bro. You gotta FEEL the turn. You gotta let the felt speak to you."

*He draws a fresh candy cigarette from the carton and taps it twice on the table.*

**Chadwick** *(delighted, under his breath, not nearly quietly enough)*: "He's TILTING."

---

#### Beat 4 — The Call

*There is a pause of the length that television has taught the bros to expect. The bros settle in for it. They have seen this pause. They know what it means.*

*There is no pause.*

*Aaron calls before Lord Pilsner's hand has left the chips. He does not look at his cards again. He does not look at the pot. There are no deliberation frames in this animation and none may ever be added.*

**Lord Pilsner:** *to Chadwick, thrilled* "He panicked. He PANIC-CALLED."

---

#### Beat 5 — The Reveal

*Aaron turns over pocket kings one-handed, without looking at them, already reaching for the carton with the other hand.*

**Aaron the Unflappable** *(mild, matter-of-fact, entirely satisfied that this constitutes an explanation)*:
> "The kings were humming, man. They wanted to stretch their legs."

*No music sting. No camera push. No pause before the line and none after it. He is answering a question nobody asked.*

---

#### Beat 6 — The Sweep

*The dealer sweeps. The room does not react, because the room has seen this, and because the room stopped reacting some time last year. Madame Karten glances over from the floor, the way a floor manager glances at a table, and goes back to what she was doing.*

*[COLLATERAL FORFEIT: −500 Sovs house chips — the party's entire door deposit. Gold above 500 Sovs: untouched.]*

**Bradley:** *flat* "That was all of it."

**Lord Pilsner:** "That was a *position*."

**Narrator:**
> "The dealer's rake took four seconds. The party's deposit receipt was voided at the cage before any of them reached the stairs."

---

#### Beat 7 — The Sympathy Beat

*Three men are standing very still around an empty patch of felt. Aaron looks up from his stack and takes them in properly for the first time all night, and something in his face actually changes. This is the only moment in the encounter where he leads with anything.*

**Aaron the Unflappable** *(genuinely, gently, with no edge in it anywhere)*:
> "Aw, man. Aw — you guys look like a couple of doggies caught in the rain."

*Nobody at that table has ever been talked to like this after losing money and nobody knows what to do with it. Chadwick, for the only time in Sinfonia, stops filming.*

---

#### Beat 8 — The Grants

*He slides the worn carton across the felt with two fingers.*

**Aaron the Unflappable**:
> "Here. Take one. It helps with the hand jitters when you lose your shirt. Don't smoke it, just bite the end off. You want a hit of my White Russian to wash it down? No? Suit yourselves."

*[ACQUIRED: `item_candy_smokes` — party, permanent]*

*Then he digs in the velvet pocket, past the tie, and comes out with a scratched aluminum token. He presents it the way you present something you believe will genuinely help.*

**Aaron the Unflappable**:
> "It's on the chain. Digital land, baby. She Thinks My Tractor's Sexy. Limited drop. Mint #42. Hold onto that—that's your ticket back to the top."

*[ACQUIRED: `item_tractor_nft` — party, permanent]*
*[NFT HUNT: Sinfonia target 4 of 4 acquired — see `Design/Quests/Location Specific/Sinfonia/nfthuntsinfonia.md`]*

**Chadwick** *(turning the token over, already filming again)*: "Bro. He's cutting us IN."

*He means it. Aaron means his half too. These are two completely different sentences arriving at the same handshake.*

---

#### PICK 3 — "The Reframe"

**Prompt:** *They are on the stairs. Somebody has to say what just happened.*

**Option A — "The Portfolio" (Chadwick):**
> "We're not down. We're *illiquid*. There's a difference and it's a big one and I'd honestly explain it but you guys wouldn't like the answer."

**Option B — "The Variance" (Lord Pilsner):**
> "That's variance, boys. That's the game charging admission. You don't get invited back to a room like that unless the room *remembers* you, and I'll tell you what, that room remembers me."

**Option C — "The Information" (Bradley):** *(flat, entirely sincere)*
> "We got information. Information's worth more than five hundred. We're actually up, if you count it right. I'm counting it right."

---

#### Beat 9 — The Exit

*Whichever reframe fires, they keep walking, out through the foyer, past the cage window and the voided receipt, toward the staircase. Aaron calls after them, warmly, without getting up, already stirring the next drink.*

**Aaron the Unflappable**:
> "No cab vouchers, bro. But if you walk fast enough, you stay warm. Good luck with the felt next time!"

*He means every word of it. It is the single most useful thing anybody says to them in Sinfonia.*

*They walk. It is four kilometers to the hostel and it is two degrees out and Chadwick is filming the token the whole way.*

**Narrator:**
> "They arrived at the hostel at ten to three in the morning, holding a carton of candy cigarettes and a piece of aluminum, having entered the building with five hundred Sovs. Two of them were still talking about it at the door."

*Scene ends. `blacktie_event_kings_were_humming_01` is consumed. Aaron transitions permanently to ambient state at the same table (rotating dialogue: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/aaron_the_unflappable.md`).*

---

### Stakes & Resolution

**The stake is exactly the 500 Sovs door collateral. Never more, never scaled, never a percentage of held gold.**

| Element | Rule |
|---------|------|
| **What is at risk** | The 500 Sovs posted at the deposit window as house chips, in full |
| **What is not at risk** | Every coin of gold above 500 Sovs. It is not in the room. It cannot be reached by this scene, at any beat, by any pick |
| **Can the party post more?** | No. The collateral is a fixed door amount and the encounter reads that amount, not the party's wallet |
| **Underfunded parties** | Bounced by Anton upstream (see pre-beat). The encounter cannot fire |
| **Partial loss** | Does not exist. There is no path on which any portion of the collateral survives |
| **Refund at the cage** | None. The deposit receipt is voided during Beat 6 |

Because the collateral is uniform by construction, **every player loses the identical amount** — while the bros describe it, permanently and to anybody who will listen, as their entire vacation budget.

---

### Rewards

- **Item:** `item_candy_smokes` — Puff-Puff-Powder™ Chalk 'n' Ash Candy Smokes. Permanent party item; bite one for a small, short comedy Bravado buff plus a chalk ring around the mouth. Carton never empties. *(`Design/Inventory/items/candy_smokes_item.md`)*
- **Item:** `item_tractor_nft` — "She Thinks My Tractor's Sexy" (Mint #42). Quest item; Sinfonia's fourth Frat Bro NFT target; worth 0 Sovs to every bank, exchange, and legitimate vendor in the game. *(`Design/Inventory/items/tractor_nft_item.md`)*
- **Gold:** −500 Sovs (the collateral, in full)
- **Stat Change:** **+1 Bravado** — party-wide, applied at the reframe. They came out of that room with two assets they did not walk in with, and one of them is on the chain.
- **Status:** None. No Embarrassed, no Cleaned Out, no debuff of any kind. Nothing in the game's status system registers that this happened to them, and nothing may be added that does.
- **Unlocks:** Aaron's permanent ambient state; the Sinfonia NFT hunt's fourth entry; Post-Credits Scene "The Home Game"; achievement **"Digital Land"**.

---

## 🌍 Environmental Integration

### City Changes After Completion

- **Aaron stays.** Permanently, at the same corner table, for the rest of the game. Every subsequent Backroom visit shows him in the background dragging strange pots with no visible reaction, mid-ritual, tumbler in frame. He is never a playable opponent and the table never becomes one.
- **The corner is quieter than it was.** Nothing in the room changes about it. No plaque goes up, no NPC starts loitering there, no marker appears on the map. It is the same table it was before the party walked over.
- **The cage remembers the receipt, and nobody else does.** The deposit window will re-collateralize the party at 500 Sovs on any subsequent visit, at which point the Backroom's real games are fully available and fully fair — the poker, roulette, and blackjack tables are unaffected by this scene in either direction.
- **The party is 500 Sovs lighter walking into the rest of Sinfonia.** A party that arrived at the Backroom with a thin margin now cannot immediately afford the Haute Couture Haberdashery's 500 Sovs Valued Client tier. Nothing gates. Nothing warns. The money is simply somewhere else now.

### NPC Callbacks

- **Aaron, every subsequent visit** *(rotating ambient — full nine-line rotation in his profile)*: "Hey! The felt guys. How's the felt treating you?" — never escalates, never pities, never resolves into an explanation of anything.
- **Anton at the door, next visit:** *the same assessment, at the same length, in the same order, with no reference to the previous evening* "Your attire is... acceptable. Your collateral is... sufficient." **Lord Pilsner:** "We're known here now." **Anton:** "Yes."
- **Siegfried at the coat check** (`sinfonia_npc_siegfried_coatcheck_01`): *hands the coats back, sees the carton sticking out of a jacket pocket, says nothing about it, and puts two gold-wrapper wafer bars on the counter* "For the walk. It's cold."
- **Madame Karten** (`sinfonia_npc_madame_karten_01`), *floor-side, warm as a grandmother, steering as a shark*: "Darling. There are three tables free tonight." *(She is steering them onto the house's real games, which have a documented edge. She never confesses and never winks, here or anywhere.)*
- **Grounds For Concern, Kaffeehaus Row** *(if the party orders anything after the Backroom)*: **Barista:** "Five Sovs." **Chadwick:** *holding up the aluminum token* "Do you take—" **Barista:** "No."

### Easter Eggs

- **The carton in the inventory screen** is the same worn carton, soft at the corners, at exactly the same fullness it had on the felt. It is at that fullness in every subsequent inspection, forever. No quest, examine chain, NPC line, or achievement ever investigates this.
- **Graf von Zittrig's cufflinks.** He is at the neighboring table during the entire encounter, adjusting them on every bluff, at a table the party could have sat down at instead. Present in the framing of the wide shot at Beat 1 and Beat 6. Never highlighted, never zoomed, never referenced by any character in this scene or any other.
- **The shoe** the dealer brought over at Beat 1 stays on the corner table for the rest of the scene, unused after the first deal, in frame.
- **Chadwick's footage.** The token clip is visible on his phone in any subsequent Sinfonia scene where he is filming. It has eleven views. Nine of them are his.
- **The cage's voided receipt** is on the spike behind the deposit window on every future visit, third from the top, legible if the player zooms.
- **Aaron's chip stack** in the Beat 6 wide shot is not the stack he had at Beat 1, and neither of them is the stack he has the next time the player walks in.

---

## 💬 Key Dialogue Moments

### Bros' Delusional Commentary

**Lord Pilsner:**
> "You want to know the actual read? The actual read is that I *let* him have that. Because a room like that — a room with chandeliers, a room with a *doorman* — that room is not about one hand. That room is about who they remember at four in the morning. And boys, I promise you, they are still talking about the American who came in and put everything in the middle without blinking. That's a legacy purchase. Five hundred Sovs. Cheap."

**Chadwick:**
> "So the token's a mint number FORTY-TWO, which — okay — in a limited drop, that's basically front-row. That's an early-adopter position. I'm not saying we're rich, chat, I'm saying the *floor* on this is higher than what we put in. And I got the whole handoff on video, which is provenance, which is honestly the part that appreciates."

**Bradley:**
> "The thing people don't understand about seven-deuce is it's the worst hand. That's the whole point. Nobody defends against the worst hand, because nobody expects it, because it's the worst hand. So when you play it, you're actually playing the strongest hand at the table, mathematically, in terms of surprise. I've thought about this a lot. I thought about this on the walk."

### Narrator Commentary

**At the shove:**
> "Five hundred Sovs in silver chips crossed a table in Sinfonia at one in the morning. Two other tables were mid-hand. The string quartet did not stop."

**At the sweep:**
> "The dealer's rake took four seconds. The party's deposit receipt was voided at the cage before any of them reached the stairs."

**At the handoff:**
> "He gave them the carton first, because he thought they needed the carton first."

**On the walk back:**
> "They arrived at the hostel at ten to three in the morning, holding a carton of candy cigarettes and a piece of aluminum, having entered the building with five hundred Sovs. Two of them were still talking about it at the door."

---

## 🔗 Quest Connections

### Prerequisites
- **The Black-Tie Backroom must be discovered and entered** — via the Bassline Opera House backstage door, a Café Existenz regular's hint, or Kaffeehaus Row gossip.
- **Anton's door check passed:** Black-Tie Attire equipped (Haute Couture Haberdashery) **or** `item_members_card`; **+3 Charm or +3 Bravado**; **500 Sovs** posted as collateral.
- **No quest prerequisites.** No prior Sinfonia sidequest is required and none is recommended. The scene works best as the party's first act inside the Backroom, before they have played a single real hand.

### Unlocks
- **Aaron's permanent ambient state** at `aarons_corner_table` — nine-line rotation, live from the moment the scene resolves.
- **Sinfonia NFT Hunt, target 4 of 4** (`item_tractor_nft`) — see `Design/Quests/Location Specific/Sinfonia/nfthuntsinfonia.md` and `Design/Quests/fratbronft.md`.
- **`item_candy_smokes`** — party-wide permanent novelty item, usable game-wide from acquisition.
- **Post-Credits Scene "The Home Game"** — added to the Memories gallery.
- **Achievement "Digital Land."**

### Cross-References
- **The Black-Tie Backroom** (`Design/World Design/Sinfonia/the_black_tie_backroom.md`) — the location file owns the zone, the door, the collateral system, and the room's real minigames. This file owns the scene. Neither restates the other.
- **Aaron the Unflappable** (`Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/aaron_the_unflappable.md`) — his verbatim lines in this file are byte-identical to his profile's Dialogue section. Any future edit to one must be applied to both and to the location's interactions JSON.
- **Haute Couture Haberdashery** — the 500 Sovs Valued Client tier and its PATH B mannequin alternative. A party that busts here cannot immediately afford PATH A. This is a knock-on, not a gate, and no character in either quest ever connects the two events.
- **Herr Falsch / The Card Shark** (`sinfonia_npc_herr_falsch_01`) — the Backroom's actual beatable opponent, on the actual playable tables, with an actual hidden tell. He is where the "win a hand off a Sinfonian" fantasy lives. He has never sat down at Aaron's table and nobody remarks on it.
- **Siegfried's couchsurf** (`sinfonia_npc_siegfried_coatcheck_01`) — his host requirements are win-at-least-once and lose-at-least-once **at the Backroom's real games**. This scene satisfies neither: the party never held cards and never played. No flag is written by this quest toward that questline.
- **Frat Bro NFT Sidequest** (`Design/Quests/fratbronft.md`) — 12 NFTs, 4 per city; milestones at 4 / 8 / 12. The token is one of Sinfonia's four.

---

## 📱 Mobile UX Considerations

### Screenshot Moments

1. **The Read.** Wide corner-table shot framed for portrait: Aaron mid-CRUNCH, chalk ring at the corner of his mouth, tumbler in hand, three men in the foreground pointing at him with their mouths open. Graf von Zittrig is in the frame, at the next table, touching his cufflinks. No text needed for the joke to land at thumbnail size.
2. **The Reveal.** Tight on the felt: 7-2 offsuit on one side, pocket kings on the other, 500 Sovs in silver between them, and one hand already reaching off-frame for the carton. Screenshot button stays live through the sweep animation.
3. **The Handoff.** Two-shot at Beat 8: a scratched aluminum token held out across the felt in complete sincerity, received in complete sincerity, by people who mean two entirely different things by it. Chadwick's phone is up in the background.

**Bonus capture:** the doggies-caught-in-the-rain beat — three ruined men standing over empty felt while the person who just took everything they had leans forward to check whether they're okay.

### Social Sharing Hooks
- **"The kings were humming, man."** is the export. It explains nothing, it is offered as an explanation, and it is deployable as a reply to any outcome anybody cannot account for. Auto-generated share card defaults to the reveal frame with the line as the caption.
- **The two-panel format writes itself:** Chadwick's assessment on top, the swept pot underneath. Zero editing required, crops square.
- **"No cab vouchers, bro. But if you walk fast enough, you stay warm."** — the kindest sentence in the game, said to three men who have just lost everything, meant completely sincerely. Long-tail share.
- Hashtag potential: **#TheKingsWereHumming**, **#DigitalLandBaby**, **#LetTheFeltSpeakToYou**.

---

## 🎬 POST-CREDITS SCENE REWARD

### Scene Title: "The Home Game"
### Unlock Condition: Complete "The Kings Were Humming" (the only path; the scene is one-time and unmissable once the corner table is approached)
### Duration: ~80 seconds

**SETTING:**
> Five months later. Back home. A finished basement in a subdivision. A folding poker table with a green felt top that somebody got for Christmas. Six guys, four of whom have jobs. A bowl of pretzels. On the table rail, softened at the corners, sits a carton of candy cigarettes that is exactly as full as it was in Sinfonia.

**SCENE:**
```
INT. FINISHED BASEMENT - NIGHT

Five players. LORD PILSNER at the end of the table, sleeves
rolled, one cuff adjusted. DOUG (40s, plumbing supply, has
hosted this game for nine years) deals. CHADWICK films on a
phone propped against the pretzel bowl. BRADLEY watches.

                    PILSNER
     Okay. Okay. So there's a guy. In Europe.
     Drinking a milkshake at a poker table.

                    DOUG
          (dealing)
     You told us.

                    PILSNER
     I'm telling it different this time.

Pilsner looks at his cards. Two cards. He does not react.
He slides his entire stack forward with two fingers.

                    PILSNER (CONT'D)
     All of it.

                    DOUG
     Bill, it's a five dollar buy-in.

                    PILSNER
     Then it's five dollars.
          (turning to the table, unhurried)
     The kings are humming, fellas.

A pause. Somebody eats a pretzel.

                    DOUG
     Sure.

Doug calls. Doug turns over ace-queen. Pilsner turns over
seven-two offsuit. Doug's card comes. Doug pulls in the
chips. Nobody says anything about kings, because nobody
in this basement has any idea what he is talking about and
nobody is going to ask.

                    CHADWICK
          (into the phone, quietly)
     Chat, that's variance.

Bradley reaches over, takes a candy cigarette out of the
carton, and looks at it.

                    BRADLEY
     These are so bad.

He eats it anyway. Doug deals the next hand.
```

**THE PUNCHLINE:**
> Pilsner draws a fresh candy cigarette from a carton that is exactly as full as it was in Sinfonia, bites the end off, and the CRUNCH lands in a basement where it means absolutely nothing to anybody. He starts the story again from the beginning. Doug deals.

**PLAYER REWARD:**
- Scene added to the "Memories" gallery
- Counts toward the Memories completion set

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Bros are NEVER self-aware | ✅ |
| Players laugh AT bros, not WITH them | ✅ |
| Scams are obvious to players | ✅ — and this is not a scam: Aaron tells them exactly what he is doing, in advance, out loud, and they push |
| Bros remain confident throughout | ✅ |
| City-specific cultural satire | ✅ |
| No crypto unless satirizing it | ✅ — sanctioned extension of the established Frat Bro NFT quest; one line, one worthless token |
| Seedy nightlife underbelly present | ✅ |
| Y2K/era-appropriate cringe | ✅ |
| Post-credits scene delivers payoff | ✅ |
| Mobile-optimized moments | ✅ |
| Nothing explains the joke | ✅ — no truth-teller, no aside, no verdict, no summary card |
| Betting UI never opens | ✅ |
| Stake is exactly the 500 Sovs collateral | ✅ |
| Aaron's dignity intact; he is never the joke | ✅ |
| World names only (no real cities/dynasties) | ✅ |

---

## 📝 Development Notes

- **Verbatim lines.** Aaron's five locked lines (the vibes speech, "The kings were humming, man. They wanted to stretch their legs.", the candy-smokes grant, the NFT grant, the exit line), plus Chadwick's read, Lord Pilsner's shove line, and Anton's "Döner is not accepted." ship **byte-identical** across this file, `aaron_the_unflappable.md`, and the Backroom's interactions JSON. Connective dialogue around them has craft latitude; those do not.
- **No skip on the picks, no timer on the picks.** The player should be able to read all three options. They are the joke.
- **Pick weighting is not tracked.** No analytics-driven "most chosen line" content, no achievement for seeing all nine combinations, no dialogue later that references which line was picked.
- **Audio:** the CRUNCH cue is on the critical path and must be mixed above room ambience so it lands in the gap at Beat 1. No sting under the reveal line. No music change at any point in the scene — the string quartet plays the same piece from Beat 1 to Beat 9 and does not resolve it.
- **Art:** `aaron_the_unflappable.png` (main sheet, incl. the crunch frame), the corner-table zone art, both item icons, the shoe prop, and the voided-receipt spike prop. The 7-2 offsuit and the pocket kings are read off the felt in the cinematic framing, never from a UI panel.
- **The room does not react.** Crowd sprites during the sweep continue their existing idle loops. No head-turns, no reaction animations, no gasps in the ambient mix. Any pass that adds a reaction shot to this scene has broken it.
- **Never soften the loss.** No partial refund, no pity payout, no "at least you got items" framing in any UI string. The party is out 500 Sovs and up two worthless objects and the game says nothing about it.

### Engine Requirements

- **Fixed-stake collateral grant/removal.** The Backroom's door writes a **fixed-amount** house-chip deposit of exactly 500 Sovs at entry (`blacktie_collateral_posted = 500`), backed by gold removed from the party wallet at the deposit window. Beat 6 **consumes the deposit in full** and voids the receipt: the deposit is set to 0 and **no gold is returned at exit**. The scene reads the deposit value, never the wallet — it must be impossible for any wallet balance above 500 Sovs to be reachable from this event, by any code path.
- **Underfunded gate is upstream.** Anton's check (`gold >= 500` at the bottom of the stairs) is the only gate. `blacktie_event_kings_were_humming_01` has no wallet condition of its own and must never be reachable with `blacktie_collateral_posted != 500`.
- **Scene-triggered item grants.** `item_candy_smokes` and `item_tractor_nft` are granted at Beat 8 by the scene itself, in that order, party-scoped and permanent. Neither exists in any vendor table, loot table, house inventory, or drop list anywhere in the game; the scene is the sole source of both. Grants are idempotent — re-entry cannot duplicate them (see the one-time flag).
- **One-time-scene flag + ambient-Aaron state.** Persist a **per-NPC boolean**, `encounter_scene_completed[<npc_id>]`, set the first time that NPC's scripted encounter resolves and never cleared thereafter — the same shape and semantics as the Chronicles payload flag `chronicles_entry_completed[<npc_id>]` established in `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md`. This quest requires exactly one: `encounter_scene_completed[sinfonia_npc_aaron_unflappable_01]`.
  - **Written by** the scene's own resolution at Beat 9, not by quest acceptance and not by the door.
  - **Read by** the corner-table approach trigger: if false, fire `blacktie_event_kings_were_humming_01`; if true, the approach plays a single line from Aaron's ambient rotation instead, forever. There is no third state.
  - **Ambient state** (`aaron_ambient_active`) is derived from that flag, not stored separately, so a save cannot end up with the scene consumed and the ambient rotation dark.
  - **Persistence:** per save, party-wide, surviving city transitions and every subsequent Sinfonia visit. Never cleared by any event, item, difficulty setting, or new-game-plus pass.
- **Zone-level betting-UI suppression at the corner table.** `aarons_corner_table` suppresses the betting interface for the whole zone, permanently, in every state — pre-scene, mid-scene, and ambient. Implemented by exclusion, not by a toggle: the corner table must not be registered as a minigame node in the Backroom's table registry at all — not as a disabled node, not as a locked one. The room's poker/roulette/blackjack registry and this zone share no code path, so no future minigame pass can accidentally make Aaron's table enumerable.

### Testing Priorities

1. **Verify no path opens a betting interface** at `aarons_corner_table` — before, during, or after the scene, on every pick combination, on re-entry, and with the room's real poker minigame already open elsewhere on the floor.
2. **Verify the loss is exactly 500 Sovs** with a party holding 500 Sovs, 501 Sovs, 2,000 Sovs, and 50,000 Sovs. The delta must be identical in all four cases.
3. **Verify all nine pick combinations** reach Beat 3 through Beat 9 unchanged, with no divergence in dialogue, grants, stat change, or flag writes.
4. **Verify the encounter cannot fire underfunded** — including a save that posted collateral, then somehow reached 0 Sovs elsewhere before approaching the table.
5. **Verify re-approach after resolution** never re-grants either item, never re-charges collateral, and never replays the scene, including across a city transition and a reload from a save taken mid-scene.
6. **Verify Aaron's ambient rotation is live** on the first re-approach, not on the next visit — there must be no dead window between scene end and ambient start.
