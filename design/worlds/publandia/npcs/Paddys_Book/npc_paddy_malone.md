# NPC Profile: Paddy Malone

*"The house always wins. That's not greed — that's math. I just understand math better than my customers."*

## 📋 NPC Identity
- **NPC ID**: `publandia_npc_paddy_malone_01`
- **Display Name**: Paddy
- **Internal Name**: Paddy Malone — "The Book"
- **Role**: Bookmaker / Loan Shark / Gambling Operator / Quest Giver / Debt Antagonist
- **Associated Quest**: `publandia_sidequest_cleaning_the_debt_01` (primary), with three linked quests — `publandia_sidequest_the_inside_bet_01`, `publandia_sidequest_whale_watching_01`, `publandia_sidequest_the_ringer_revealed_01`
- **Primary Location**: Paddy's Book — "Leabhar Phádraig" — an unmarked door behind a dumpster in a back alley off The Craic Tax, Publandia
- **Secondary Appearances**: Does not leave the den. His associates do — debt collectors appear at The Blarney Trap if the player owes, and his scouts work the Craic Tax nightly feeding him proposition-bet intelligence
- **Family**: His sister Maureen works the Recovery Corner and handles the soft side of collection. His father ran books. His grandfather ran books during the Emergency. "Four generations of the same arithmetic."

---

## 🎭 Core Concept

### What He's Actually Doing

Running an unlicensed book out of a converted cellar, on odds he sets, judging disputes he rules on, over outcomes he has scouts watching. The dice are slightly loaded. The high-low payout is 1.8:1 where fair would be 2:1. The Liar's Dice opponents are professionals who read tourist tells for a living. Roughly 30% of the brawls in the back pit are predetermined, and the "Australian" in the Tourist Battle Royale is a local fighter who has never been further south than Cork.

The gambling is the front. The real business is the Recovery Corner: when a tourist hits zero, Maureen brings a drink, and then Paddy arrives with a loan at 50% interest **per day**, secured against a marker — which is to say, against the mark's ability to walk around Publandia unbothered. Paddy does not consider this predatory. He considers it a service with a price attached, and he will explain the arithmetic to you with real patience while your money is being counted into a box behind him.

### What Bros Believe

That they have found the authentic criminal underbelly of Publandia via a secret password and a green bulb, that Paddy is a grandfatherly old character who has taken a shine to them, that "house rules" is colourful local custom rather than a mechanism for reversing any outcome the house dislikes, and — critically — that they have a system. Lord Pilsner is up 40 Sovs early and has concluded that the dice listen to him. Chadwick is not losing; he is investing in the narrative.

### The Comedy Gap

Every single thing in the room is labelled. There is a sign on the wall reading **"THE HOUSE IS ALWAYS RIGHT."** The odds board has "HOUSE RULES: THE HOUSE IS ALWAYS RIGHT" printed across the bottom in a banner. The proposition bets include *rain before midnight* at 1:3 — in Publandia — which is functionally a fee for the privilege of being condescended to. A man in the corner will tell you, unprompted, not to take the loan, because he has been "working it off" for six months.

The bros read all of this as atmosphere. Then they take the loan.

---

## 👤 Appearance

### Physical Description
| Attribute | Description |
|-----------|-------------|
| Age | Early 60s |
| Build | Neat, small, immaculately still — he is the only person in the den who never fidgets |
| Height | Short, seated most of the night behind the desk, which makes the height irrelevant |
| Energy | Grandfatherly warmth, running continuous arithmetic underneath |

### Clothing
- **Waistcoat, dark brown**: Buttoned. Always. In a smoke-filled cellar in July. It is a uniform and it is worn as one.
- **White shirt, green tie**: The tie is the only colour on him and it is exactly the green of money on the odds board behind his head. This is not an accident; Paddy chose it in 1987 and has bought the same tie eleven times since.
- **The watch**: Expensive, brass and gold, funded entirely by other people's losses. He does not hide it and he does not flaunt it. It is simply always there, on the left wrist, in every frame.
- **Accessories**: A pen for the ledger. Reading glasses, worn only when the numbers get serious — putting them on is a tell the player should learn to fear. A whiskey glass, filled once per night and never twice.
- **Footwear**: Polished, quiet, largely unseen behind the desk.

### Distinguishing Features
- **The eyes**: Sharp and warm at the same time. He is genuinely pleased to see you and he is simultaneously pricing you.
- **The stillness**: In a room of dice throws, shouting, and crowd surge, Paddy does not move. When he *does* move, everyone notices, which is the point of not moving.
- **The ledger stroke**: One elegant pen mark per bet. He never looks at the pen while writing.
- **The wince**: On a rare genuine payout, a flicker of physical pain, professionally suppressed within a quarter-second. It is the only involuntary thing he does.
- **The reading glasses**: When they come on, a player has won too much, and "house rules" is roughly forty seconds away.

### Sprite Notes

Sprite sheet `paddy_malone.png` (512x384) — four rows: warmth and the book, house rules and the loan, the mask slipping, and detail elements. Priorities:

- **The watch must appear in every single body frame** — left wrist, two or three lit pixels. Continuity is the joke. If a frame ships without it, the joke breaks silently.
- **Warmth-to-Calculation Transition** is the most important frame on the sheet. It is the tween between any Warm state and any Business state, and it is where grandda becomes bookmaker. It should be reusable and it should be brief.
- **Paddy Dialogue Bust** must keep the smile ambiguous — readable as kindly OR predatory depending entirely on the text beneath it. Do not resolve it. The same bust carries "welcome, friend" and "the terms are simple."
- **Rare Payout Wince** is a one-frame joke that pays off across an entire playthrough. Give it real physical discomfort.
- Paddy is the still point in a moving room. Every idle should be smaller in amplitude than any other NPC's in the den.

---

## 🧠 Personality

### Archetype

**The Arithmetic Grandfather** — Paddy is warm, welcoming, patient, and completely without malice, and he will take everything you have because the numbers say he should. He does not think of himself as a criminal; he thinks of himself as a mathematician who accepts cash. His affection for his customers is real and does not interfere with the business in any way, because he has never once experienced those two things as being in tension. This is what makes him more dangerous than Mickey Finnegan and less pleasant than he appears: Mickey has a line he won't cross. Paddy has a formula.

### Personality Traits
| Trait | Description |
|-------|-------------|
| Grandfatherly warmth | Genuine, deployed constantly, and entirely compatible with cleaning you out. He is not pretending. |
| Total numeracy | Learned odds before multiplication tables. Calculates a parlay faster than the player can read it. |
| Rule-flexible | Invokes "house rules" the instant the house is exposed, and presents the invention as tradition. |
| Information advantage | Runs scouts across The Craic Tax. Every proposition bet is a bet against a man who already knows. |
| Patient predator | Never rushes the loan. Waits for zero. The pitch only lands at zero and he knows it. |
| Institutionally protected | "The police know me. We have an understanding." Stated plainly, never elaborated. |

### Internal Monologue

> "He's up forty. Good. Let him be up forty — a man who's up forty tells his friends and his friends come with him tomorrow. He'll bet bigger now because the forty doesn't feel like his, and that's the whole of it, that's the entire business in one sentence: money you've won never feels like money you own. He'll be level by eleven, down two hundred by one, and at half two he'll be standing at Maureen's table with an empty wallet and a face like a christening gone wrong. And then I'll sit down beside him and I'll be kind to him, because I will be, because I like him. And he'll sign. They always sign. Fifty per cent a day. It's on the paper. I never once hid it."

### Motivation

Continuity and arithmetic. Paddy is the fourth generation of a family that has taken bets through a civil war, an Emergency, a boom, and a bust, and the ledger has closed in the black every year of it. He is not accumulating toward anything. He has no plan for the money beyond the watch and the whiskey. What he wants is for the book to balance, for the den to keep running, and for the flow of people who believe they are different — smarter, luckier, systematic — to never stop arriving, because he genuinely loves them for believing it. He was cleaned out exactly once, at twelve. He learned. Almost nobody else does, and that is not a tragedy to him. That is a business model.

---

## 💬 Dialogue

### At the Door (via Tiny)

**If the player uses "What odds on rain?" (always works)**:
> *from inside, before the door is fully open* "In Publandia? Evens. Come in out of it."

**If the player uses "The ponies are thirsty" (Monday)**:
> "Monday's word, and it's Monday. Somebody's been paying attention. I like that in a customer. I'll like it less by closing."

**If the player uses "I'm here for the book club" (Tuesday/Thursday)**:
> "We're reading the ledger. It's a tragedy. Everyone dies broke."

**If the player uses "Seamus sent me" (works sometimes — risky)**:
> "Seamus. *pause, weighing it* Seamus O'Brien doesn't send anyone here. Seamus O'Brien pours a lovely pint and tells people to go to bed. But you've the brass shamrock on you, so you've been in his pub, and that means you're not a guard. *nods at Tiny* Let him in. And tell Seamus I said the name still opens doors, which he'll not enjoy hearing."

**If the player uses "Seamus sent me" without the Bottle Opener Keychain**:
> "Everyone says that. *no warmth at all for exactly one second, then it returns* Fifty Sovs. Show me. Then we'll be friends."

---

### The Welcome

> "Welcome, welcome! New faces, new friends, new opportunities. What's your pleasure?"

> "First time? Let me explain how we do things. Simple, fair, exciting. You'll love it."

> "The password worked, did it? Good man. You're among friends now."

**Explaining the board**:
> "Brawls on the top. Dice in the middle. Propositions at the bottom — that's where the fun is, that's where a man can back his own judgement. Rain before midnight, one to three. Hen party gets sick in the Craic Tax, one to two. Tourist orders a 'Publandia Bomb', evens. Police raid tonight, fifty to one. *smiles* Nobody's ever taken the fifty to one. I'd love it if somebody would."

---

### During Gambling

> "Ohhh, close one! The dice are fickle tonight. But I feel your luck changing..."

> "There you go! A winner! See? Everyone wins here. Eventually."

> "Ah, that's a tough break. But you know what they say — unlucky in dice, lucky in love. Or vice versa."

**High-Low, 20 Sovs a round**:
> "Twenty in, call it high or low, pays one point eight. Fingers'll throw for you. He's got the hands for it — that's not a compliment, that's a job description."

**Liar's Dice, 50 Sovs entry**:
> "Fifty to sit down. Winner takes the pot, house takes twenty per cent for the chairs and the atmosphere. Mind the man opposite. He's been reading faces since before you had one."

**Paddy's Special, 100 Sovs minimum**:
> "The Special. Hundred minimum, one roll, your choice of game, up to five-to-one on the long shots. *leans back* Ties go to the house. Disputes go to the house. That's the only unfair thing about it and I've just told you what it is."

**On the propositions, if the player wins one**:
> "You backed rain. In Publandia. And it rained. *counts out the money without hesitation* You've taken three Sovs off me and you've earned every cent of it. Would you like to do something ambitious with it?"

**If the player is on a winning run**:
> "Well well! Someone's got the touch tonight! Enjoy it while it lasts..."

> "You know, we've got higher stakes tables in back. A winner like you..."

> "House rule check... no, you're fine. For now. Keep playing, keep playing."

---

### The House Rules (Invoked When the House Is Losing)

> "Now, we play Publandia rules here. Slight variation on what you might know."

> "That's a disputed roll. House decides in disputes. House says... re-roll. Fair, right?"

> "I'm going to invoke the Malone Clause here. For your protection, really."

**Technical difficulties**:
> "Dice need recalibrating. Take a break, have a drink, it's on me. *the drink is on him because the break is worth more than the drink*"

**The floor**:
> "That roll's invalid. Floor's tilted — has been since the eighties, everyone knows it, we all play around it. You'll get used to it."

**Personal discretion**:
> "I don't like how that landed. Re-roll. *pleasantly* You can argue if you'd like. Tiny settles arguments. He's very good at it and he's never once had to raise his voice."

**If the player accepts a house-rules reversal gracefully**:
> "Good man. That's how it's done. You'll be welcome here a long time."

**If the player argues**:
> "Now, now. *reading glasses come off, folded, set down* You're a guest. Guests don't audit the host."

---

### The Loan Pitch (Triggers at 0 Sovs — "Cleaned Out")

> "I hate to see you walk out with nothing. Tell you what — I can help."

> "A small loan. Just to get you back on your feet. Among friends, what's a little money?"

> "The terms are simple. Pay me back tomorrow, no interest. Day after? Small interest. Week? Well... let's not wait a week."

**If pressed on the actual rate**:
> "Fifty per cent. Per day. *no change in tone whatsoever* It's on the paper. I've never hidden it and I never will. It's a terrible loan. It's also the only one you're being offered at three in the morning by a man who likes you."

**The marker**:
> "No collateral as such. Just your marker. Your word, your name, your ability to walk down the Craic Tax without anyone stopping you for a chat. Small things. You'll never miss them."

**If the loan is refused**:
> "No? *genuinely warm, no edge at all* Then you're a wiser man than most who sit in that chair, and I mean that. Go on. Maureen'll see you to the door. Come back when you've money — you'll always be welcome, and I'd rather have you as a customer than as a debtor. That's true, by the way. It's just not true enough to change the terms."

**If the loan is accepted**:
> "Grand. Sign there, and there. *one elegant pen stroke in the ledger* You're in the book now. That's not a threat. That's just where you are."

**If the debt goes unpaid past one day**:
> "Nothing's changed between us. You owe more, is all. That's not a mood, that's a sum."

---

### On Himself (Philosophy, Extended)

> "My grandfather took bets during the Emergency. War's good for gambling — uncertainty makes people want to control SOMETHING."

> "I'm not a criminal. I'm a mathematician who accepts cash. The police know me. We have an understanding."

> "The tourists think this is exciting and dangerous. It IS exciting. The danger is mostly to their wallets."

> "Every man who walks in thinks he's different. Smarter. Luckier. They're not. But I love them for believing."

> "I've been cleaned out exactly once in my life. I was twelve. I learned. Most people never learn. That's my business model."

**On Mickey Finnegan (if asked)**:
> "Mickey takes fivers off tourists and calls it art. I take everything and call it arithmetic. We're not the same trade. He'd tell you he has standards. He does. That's his limitation, not his virtue."

**On Seamus O'Brien (if asked)**:
> "The best publican in this city and the worst gambler I ever met, which is why he's never once sat at that table. He knows exactly what he is. There's about four of us in Publandia who do."

**On the Debt Ghost in the corner**:
> "Him? He's working it off. He'll tell you not to take the loan and he's right and you should listen to him. *doesn't lower his voice; the Debt Ghost can hear every word* I've never stopped a man from saying it. Why would I? Nobody's ever listened."

---

### Post-Interaction

**"High Roller" status achieved (500 Sovs cumulative bets)**:
> "Five hundred through my book. That's a High Roller, that is. Better whiskey, better seat, and the odds get a small adjustment. *pause* In which direction, I'll let you work out."

**Closing time, if the player is still solvent**:
> "Five in the morning and you've money in your pocket. That's rarer than you'd think. Go home. Don't come back tomorrow. *smiles* You'll come back tomorrow."

**On being asked whether the games are honest**:
> "Honest? The odds are on the board. The rules are on the wall. The wall says the house is always right, and every night the house is always right. Where exactly is the dishonesty? Point at it for me."

---

### Callback Dialogue (Return Visits)

**Second visit**:
> "Back. Of course you're back. Sit down, I've kept the chair."

**After paying off the debt in full**:
> "Paid. In full. *closes the ledger, and for one second the warmth and the arithmetic are the same thing* Very few do that. You'll not be offered another loan — not because I'm punishing you. Because you've proven you'd pay it, and a man who pays is worth more to me at the table than in the book."

**After defaulting and escaping**:
> "You've been away. *doesn't stand* You'll not be playing tonight. You'll not be playing next month either. But you're not barred forever — nothing's forever except the sum, and the sum is still there, and it's still growing. Come back when you'd like to discuss it."

**Late game, if the player exposed the fixed fight**:
> "You cost me eight hundred Sovs and a fighter. *long pause, then the warmth returns, fully* Good bet. Best one made in here all year. Now. What'll you have?"

---

## 📅 Schedule & Location

### Primary Schedule
| Time | Location | Activity |
|------|----------|----------|
| 18:00-20:00 | The Book Station (Paddy's Desk) | Doors open. Setting tonight's odds. Scouts report in from The Craic Tax with proposition intelligence. Quiet trade. |
| 20:00-23:00 | Book Station / The Pit | Odds-calling to the floor. Sports and proposition action. Sizing up every tourist Tiny lets through. |
| 23:00-01:00 | The Brawl Pit | Fight cards. The real money. Odds manipulated live based on betting patterns. Tourist Battle Royale offered to fighting-inclined bros. |
| 01:00-03:00 | Book Station | Peak dice action, Paddy's Special, house rules invoked as required. The reading glasses go on and off. |
| 03:00-05:00 | The Recovery Corner | The loan shift. Maureen softens; Paddy closes. This is the most profitable two hours of the night by a wide margin. |
| 05:00 | Book Station | Closing tally. Ledger shut, cash counted, watch checked, one whiskey. Then he goes wherever he goes. |
| 05:00-18:00 | Not present | The den is a cellar with a locked door. Paddy is elsewhere and it is not the player's business. |

### Positioning Notes
- **Paddy is behind the desk by default and this is structural, not incidental.** The desk is the book; the book is the business. He leaves it for exactly three things: fight cards, the loan pitch, and the closing tally.
- The Odds Board is directly behind and above him, so every conversation with Paddy is framed with "HOUSE RULES: THE HOUSE IS ALWAYS RIGHT" over his shoulder. The framing should be preserved in every camera setup in the location.
- Tiny is at the door and never further than a glance away. Paddy has never had to call him; he looks, and Tiny is already moving.
- Maureen works the Recovery Corner independently and Paddy does not go there until she signals. The handoff between them is wordless and repeats identically every night.
- During the loan pitch Paddy sits *beside* the player rather than across from them — the only time in the game he does this. It should read as kindness and it is a closing technique.

---

## 🎒 Inventory / Services

### The Book — Games & Stakes
| Game/Service | Price | Displayed Odds | Actual Edge | Result |
|--------------|-------|----------------|-------------|--------|
| Dice Fights (High-Low) | 20 Sovs entry per round | Predict higher or lower than the current roll | Die slightly loaded — 55/45 in the house's favour; odds *worsen* as the player wins ("house adjustment") | Payout 1.8:1 where fair would be 2:1 |
| Liar's Dice Tournament | 50 Sovs entry | Bluffing tournament, winner takes the pot | NPC opponents are professionals who read tourist tells perfectly | Winner takes pot, house takes a 20% cut |
| Paddy's Special (ask at desk) | 100 Sovs minimum | Single high-stakes roll, player's choice of game, up to 5:1 on long shots | "Paddy's choice" on all ties and disputes; house rules activate if the player wins too much | The 5:1 long shots do not hit |
| Proposition — Rain before midnight | Stake at player's discretion | 1:3 | It is Publandia. Always bet rain. Everyone knows. That is what makes it 1:3. | Small, reliable house income |
| Proposition — Hen party vomit (Craic Tax) | Stake at player's discretion | 1:2 | Saturday-night special; Paddy's scouts report from the street | Information asymmetry |
| Proposition — Tourist orders "Publandia Bomb" | Stake at player's discretion | 1:1 | Daily occurrence; Paddy scouts the bars and knows the count before he sets the line | Information asymmetry |
| Proposition — Police raid tonight | Stake at player's discretion | 50:1 | "The police know me. We have an understanding." | Has never paid out. Paddy would genuinely enjoy it if it did. |
| Brawl Betting | Stake at player's discretion | Board odds, shifting live | Paddy knows the fighters' conditions; tourists don't. ~30% of high-bet matches are predetermined. | Odds manipulated against the betting pattern |
| Tourist Battle Royale | 30 Sovs to fight, or bet on others | Odds on each participant, constantly shifting | The house favourite is frequently a ringer — a local fighter presenting as a tourist | Winner takes the pot minus a 30% house cut |

### Tonight's Brawl Card (Standing Odds Board)
| Fighter | Odds | Reality |
|---------|------|---------|
| Big Mick vs. Quarry Jimmy | 2:1 / 3:2 | The headline card. Both are known local quantities; the line is honest because it doesn't need to be crooked. |
| The Brewery Gorilla vs. ??? | 5:1 / 1:8 | The 1:8 is the tell. Paddy knows who "???" is. |
| "American Mike" | 3:1 | Actually decent. A genuine tourist. |
| "British Barry" | 5:1 | Overconfident, quick loss. |
| "The Australian" | 2:1 | Ringers are often "Australian." |
| "German Tourist" | 4:1 | Wildcard. Could genuinely surprise. |
| "Mystery Entrant" | 8:1 | Usually the ringer reveal. |

### The Loan Book
| Service | Terms | Collateral | Consequences |
|---------|-------|------------|--------------|
| Paddy's Assistance | 50% interest **per day** | Your marker — reputation, standing, freedom of movement in Publandia | Default: barred from Paddy's Book; associates "remind" you around the city; debt collectors appear at The Blarney Trap; "In Debt to Paddy" status persists until resolved by quest |

### Status Effects Paddy Administers
| Status | Trigger | Effect |
|--------|---------|--------|
| "On a Roll" | Won last 3 bets | +confidence, worse decision-making, bet sizes creep upward |
| "Chasing Losses" | Lost last 3 bets | −judgment, bet amounts increase automatically |
| "Cleaned Out" | Hit 0 Sovs at Paddy's | 1 game-day ban, −20 Bravado (it is public knowledge), loan offer follows you to The Blarney Trap |
| "In Debt to Paddy" | Loan accepted | Interest accrues daily; associates watching; quest chain activates |
| "High Roller" | 500 Sovs cumulative bets | Respect, better service, marginally better odds — still losing long-term |

### Hidden Details / Easter Eggs
- **The House Rules sign** is examinable. It reads, in full: "THE HOUSE IS ALWAYS RIGHT." There is no second clause. There has never been a second clause.
- **The ledger** can be examined when Paddy leaves the desk for the fight card. It is legible. Three columns: names, sums, and a third column of single-word notes on each customer. The player's own name appears after their second visit, with a note. The note is never shown.
- **The whiskey glass**: filled once per night, never twice. Examining it late in the night shows it still nearly full. Paddy on the subject: "A bookmaker who drinks is a customer with extra steps."
- **The 50:1 police raid line**: if the player backs it, Paddy is visibly, genuinely delighted, and takes the bet in front of the whole floor. It has never hit. Whether it can ever hit is left unresolved.
- **Maureen's tray**: the "on the house" drinks in the Recovery Corner are the only free thing in the building, and they are the most expensive thing in the building.

---

## 🔗 Connections

### Professional/Social Network
| NPC | Relationship |
|-----|--------------|
| Maureen (The Consoler) | Paddy's sister. Runs the Recovery Corner and the soft-touch side of collection. Her sympathy for your loss is real; her interest in your solvency is professional. They have worked this handoff for thirty years without discussing it. |
| Tiny (The Bouncer) | Door security, funds check, dispute settlement. 6'8", surprisingly gentle voice, has never had to raise it. Paddy has never once had to call him — he looks, and Tiny moves. |
| Fingers O'Brien (Dice Master) | Former magician, now the hands behind the High-Low pit. Flashy, entertaining, wholly untrustworthy. Paddy keeps him at the dice and away from the book, on the grounds that a man that good with his hands should never be near a ledger. |
| The Local Shark | Professional gambler who genuinely understands the odds, wins 20 Sovs a night, and is tolerated because he brings marks. Paddy's assessment: "He's not beating me. He's on salary and he doesn't know it." |
| The Whale | Rich tourist losing enormous sums cheerfully. Beloved by all staff. Paddy watches him lose with undisguised joy — the "Whale-Watching Delight" sprite frame exists for this and only this. |
| The Debt Ghost | Six months into "working it off." Warns every newcomer not to take the loan, in Paddy's hearing, with Paddy's full permission. |
| The Ringer | Professional fighter presenting as an Australian tourist. Enters the Battle Royale, dominates, winks at Paddy, collects real payment. |
| Seamus O'Brien (The Blarney Trap) | Not a friend; a fixed point. Paddy uses "Seamus sent me" as a password without permission and knows Seamus dislikes it. Paddy's debt collectors are permitted inside The Blarney Trap on the strict condition they never raise their voices — Seamus's rule, and Paddy keeps it. |
| Mickey "The Mick" Finnegan (Shenanigans) | Professional acquaintance. Different scams, same marks, careful mutual distance. Mickey thinks Paddy's loan book is past where the craft should stop. Paddy thinks Mickey's standards are a limitation. Both are correct. |
| The Craic Broker (The Blarney Trap) | Feeds rumours about Paddy's Book to the quest board, which is how most tourists find the alley. Paddy has never met him and pays him nothing. |

### Territory / Social Dynamics
- **Paddy does not enforce anything personally.** Tiny is the enforcement, Maureen is the collection, the associates are the reminder. Paddy is only ever the arithmetic. This separation is deliberate and it is why "the police know me" is a sentence he can say calmly.
- **The den has a strict internal hierarchy and Paddy is at the top of it without appearing to be.** He is seated. Everyone else is standing. There are deliberately very few chairs on the main floor — it keeps people moving and it makes his desk the only place anyone sits down.
- **The scouts are not staff and are not paid a wage.** They are Craic Tax fixtures who get a drink and a small cut for reporting what tourists are doing. This is how every proposition bet is decided before it is offered.
- **Locals gamble small and leave. Tourists gamble large and stay.** Paddy prices accordingly and has never pretended otherwise to anyone who asked.

---

## 🔄 Recurring Appearances

### Within Publandia

Paddy never leaves the den. **His debt does.**

- **The Blarney Trap**: If the player holds an active loan, Paddy's associates appear in the pub. They do not threaten, do not shout, and do not approach the bar. They sit. They are there the next night too. Seamus permits this and dislikes it, and will say so if asked: "Paddy's lads are in the corner. They'll not bother you and they'll not leave. That's the arrangement and I'm not proud of it."
- **The Craic Tax streets**: Scouts feed Paddy proposition intelligence nightly. Players with "In Debt to Paddy" status find that street encounters change — touts back off, and one scout follows at a distance.
- **Shenanigans**: Mentioning Paddy to Mickey Finnegan post-stamp triggers Mickey's only unprompted warning to anyone in the game: "My games take fivers. His take everything you've got and then lend you more. Know the difference before you knock."
- **The Quiet Man**: Fighters cross between the Brawl Pit and The Quiet Man. Cross-betting flows both directions and Paddy sets lines on fights he cannot personally observe — the one place his information advantage is genuinely thin.
- **Paddy's Book itself**: Post-"High Roller", Paddy stands to greet the player, which he does for nobody else on the floor, and which costs him nothing.

### In Other Cities

Paddy Malone does not appear outside Publandia and has no interest in doing so. This is a deliberate character constraint, not an omission: his entire edge is local information — scouts on the Craic Tax, fighters he has watched train, weather he has lived under for sixty-two years. Away from that alley he would be an old man betting blind, and he knows it. If the player asks whether he has ever considered expanding:

> "To where? I'd be a tourist. *pause* And you've seen what happens to tourists."

The debt, however, does travel. "In Debt to Paddy" remains active across all cities and blocks certain services in Debaucheryville and Shamsterdam — vendors who deal in reputation notice the marker. No collectors follow the player abroad. They simply wait, which is worse.

### Evolution Through Game
- **First visit**: Pure hospitality. Paddy is the warmest NPC in the seedy underbelly and it is not an act. Nothing bad happens on night one unless the player insists on it.
- **Second and third visits**: House rules begin appearing, always politely, always in the player's disfavour, always framed as tradition.
- **Post-"Cleaned Out"**: The loan pitch. This is the character's hinge. Everything before it is charming; everything after it is a sum.
- **In debt**: Paddy's dialogue does not become hostile. It becomes *unchanged*, which is the point. The same warmth, the same courtesy, the same interest in the player's night — while the number grows.
- **Debt paid**: Genuine, unguarded respect, once, briefly. Then business as usual.
- **Post-"The Ringer Revealed"**: If the player exposes the fixed-fight system, Paddy loses real money and real face, congratulates them sincerely, and continues to run fixed fights. There is no reform.
- **What never changes**: Paddy is never angry, never threatening, and never lies about the terms. Every single thing he does to the player is disclosed in advance, on a wall, on a board, or in a sentence.

---

## 🎬 Animation States

### Idle Animations
| Animation | Description | Frequency |
|-----------|-------------|-----------|
| idle_warm_folded | Hands folded on the desk, eyes twinkling, doing arithmetic | 35% |
| idle_breathe | Breathing frame; the smile a half-pixel wider | 25% |
| watch_glint | Light catches the watch face, travels the band (2 frames) | 20% |
| ledger_glance | Brief look down at the columns without moving his head | 12% |
| sizing_up_squint | Half-second appraisal of a new tourist crossing the floor | 8% |

### Interaction Animations
| Animation | Trigger |
|-----------|---------|
| welcome_arms_open | Player approaches the desk for the first time that night |
| dealing_3frame | Bet placed: slip taken → ledger entry → cash to box |
| odds_calling_3frame | Calling tonight's action: arm raised → board point → cupped shout |
| house_rules_3frame | House rules invoked: finger raised → hand on heart → apologetic shrug |
| malone_clause | The Malone Clause declaration, "for your protection, really" |
| dispute_decision | "House says... re-roll. Fair, right?" |
| loan_lean_in | Elbows on desk, then hand on shoulder — the pitch, seated beside the player |
| loan_contract_slide | Paper across the desk; 50% per day, among friends |
| winner_congratulation | Applauds a player win while calculating the clawback |
| rare_payout_wince | Genuine physical discomfort, suppressed within a quarter-second |
| whale_delight | Watching The Whale lose happily — pure, uncomplicated joy |
| warmth_to_calculation | Reusable tween between any Warm state and any Business state |
| closing_tally | Ledger closed, watch checked, satisfied |

### Sprite States
| State | When Used |
|-------|-----------|
| paddy_warm | Default. Welcome, board explanation, general floor conversation. |
| paddy_dealing | Any active bet at the Book Station |
| paddy_house_rules | Rule invocation, dispute rulings, the Malone Clause |
| paddy_loan | Recovery Corner pitch — the only state where he is seated beside the player |
| paddy_calculating | Post-"warmth_to_calculation"; used when the reading glasses are on |

---

## 🎯 Quest Integration

### Primary Quest: Cleaning the Debt
- **Quest**: Cleaning the Debt
- **Quest ID**: `publandia_sidequest_cleaning_the_debt_01`
- **Role**: Quest Giver and antagonist-by-arithmetic
- **Trigger**: Accepting Paddy's loan after "Cleaned Out" status
- **Stages**: Loan accepted → interest accrues at 50%/day → associates appear at The Blarney Trap → player either works the debt off through tasks for Paddy, repays in cash, or attempts to escape it
- **Outcome**: "Survivor" achievement on full repayment; "Marked" if the debt persists; permanent reputation consequences either way

### Linked Quests
| Quest | Quest ID | Paddy's Role | Moral Choice |
|-------|----------|--------------|--------------|
| The Inside Bet | `publandia_sidequest_the_inside_bet_01` | Unwitting target — the player learns a fight is fixed | Participate in the fix for profit, or expose it |
| Whale Watching | `publandia_sidequest_whale_watching_01` | Quest Giver — asks the player to help land a big fish | Help Paddy extract from The Whale, or refuse and warn him |
| The Ringer Revealed | `publandia_sidequest_the_ringer_revealed_01` | Target — the player uncovers the ringer system in the Battle Royale | Exploit the knowledge for betting profit, or expose it publicly |

### Quest Gate Function

**Paddy gates the seedy underbelly of Publandia through funds and Bravado, not through story.** Entry requires Bravado 25+ *or* an NPC vouch, plus a minimum 50 Sovs which Tiny physically verifies at the door. Players below either threshold are turned away politely and permanently until they qualify.

Paddy is explicitly **not** a Brewery Passport stamp giver. Paddy's Book is not a Brewery Tour location, has no signature beer, and awards no stamp. This is intentional: the four Publandia stamps live at The Blarney Trap, The Stoutworks Brewery, Trinity of Pints, and a fourth location still to be designated. Paddy sells risk, not craft, and giving him a stamp would confuse the passport's meaning.

The "In Debt to Paddy" status functions as a soft cross-city gate — reputation-sensitive vendors in Debaucheryville and Shamsterdam decline service to marked players until the debt is resolved.

### Items Acquired From This NPC
| Item | Quest Stage | Permanent? | Effect |
|------|-------------|------------|--------|
| Betting Slip | Any bet placed | No | Records a wager; tracks toward "High Roller" (500 Sovs cumulative) |
| Loan Contract | Loan accepted | Yes, until repaid | Sets "In Debt to Paddy"; 50% daily interest; associates activated |
| Marker Chit | Loan accepted | Yes, until repaid | Collateral form — "essentially your reputation" |
| High Roller Badge | 500 Sovs cumulative bets | Yes (status) | Better whiskey, a seat, respect, marginally adjusted odds |
| Battle Royale Pot | Winning the Tourist Battle Royale | No | Pot minus 30% house cut, plus bragging rights |

---

## 📸 Social Media / Viral Potential

### Screenshot Moments
1. The odds board in full, with "HOUSE RULES: THE HOUSE IS ALWAYS RIGHT" across the bottom and Paddy's head directly beneath it.
2. "Police raid tonight — 50:1" and Paddy's delighted face when someone finally backs it.
3. The loan contract sliding across the desk: 50% interest per day, in plain type.
4. The Debt Ghost warning the player while Paddy nods along in the background.
5. The Rare Payout Wince — one frame, screenshot-perfect.
6. "Rain before midnight — 1:3" in a city where it is currently raining.

### Meme Potential
- "The house always wins. That's not greed — that's math."
- "I'm not a criminal. I'm a mathematician who accepts cash."
- "Point at it for me." (in response to any accusation of dishonesty)
- "That's not a threat. That's just where you are."
- "It's a terrible loan. It's also the only one you're being offered at three in the morning by a man who likes you."
- Lord Pilsner: "...Paddy, about that loan you mentioned..." / Paddy: "Of course, friend. We're all friends here."

---

## 🗣️ Voice Direction

### Accent

Dublin, older generation, unhurried. Paddy speaks more slowly than anyone else in the den and never competes with the room's volume — people quieten down to hear him, which is the effect. Warm, grandfatherly, with perfect diction on any sentence containing a number. Not exaggerated, never cartoonish. This is a man who has explained odds to strangers for fifty years and has become extremely good at being understood.

### Tone
- **The Welcome**: Open, delighted, completely genuine. He is glad you came.
- **Explaining the board**: Precise and slightly proud. This is craft and he wants you to appreciate it.
- **House rules**: Apologetic, reasonable, immovable. The apology is sincere. The ruling does not change.
- **The loan pitch**: Kind. Quiet. Seated beside you. The warmest register in the entire performance, deployed at the worst possible moment for the player.
- **Anything involving a number**: Flat and clear. The 50% daily rate should be delivered exactly like the time of day.

### Key Delivery Notes
- **"Fifty per cent. Per day."** — no emphasis, no relish, no apology. It is a fact he is providing because he was asked. If the actor plays it as a threat, the character collapses into a stock villain.
- **"Point at it for me."** — genuine invitation, no sarcasm. He would honestly like to know.
- **"That's not a threat. That's just where you are."** — warm. Almost consoling. This is the most quietly frightening line in Publandia and it must not be played as frightening.
- The Rare Payout Wince should be audible as well as visible — a half-breath, immediately swallowed.
- He never raises his voice in any branch, including the argument branch. His response to being argued with is to speak more quietly, and to fold his reading glasses.
- The one moment of unguarded warmth — "Paid. In full." — should be shorter than the actor wants it to be. Two seconds, then the ledger closes.

---

## ✅ Validation Checklist

| Requirement | Status |
|-------------|--------|
| Full appearance documented | ✅ |
| Personality & motivation clear | ✅ |
| Complete dialogue trees | ✅ (55+ lines across 9 branches) |
| Schedule & location specified | ✅ |
| Connections to other NPCs | ✅ (10 named, all pre-existing) |
| Recurring appearances planned | ✅ (Publandia network + cross-city debt consequences) |
| Animation states defined | ✅ |
| Quest integration documented | ✅ (1 primary + 3 linked) |
| Sprite notes for artists | ✅ (mapped to `paddy_malone.png`) |
| Comedy value preserved | ✅ |
| Bros never achieve self-awareness | ✅ |
| World consistency (city names) | ✅ (Publandia, Debaucheryville, Shamsterdam) |
| Real prices and odds from source file | ✅ (all lifted from `paddys_book.md`) |
| No bracketed placeholders | ✅ |

---

## 📝 Development Notes

- **The "Seamus sent me" password is Paddy's, unauthorised.** Seamus O'Brien has not sanctioned it and dislikes it; Paddy uses it anyway and finds it flattering. The password should work *sometimes* — implement as a Tiny-discretion roll that succeeds automatically if the player holds the Bottle Opener Keychain, and roughly 50/50 otherwise. This is the mechanical expression of the Seamus network reaching a door it was never meant to open.
- **Paddy is not a stamp giver.** Paddy's Book has no Brewery Passport stamp, no signature beer, and no selfie spot. Do not add one during passport implementation; the fourth Publandia stamp location is still TBD in `the_blarney_trap.md` and should not default here.
- All four quest IDs are **newly coined** — the four quests are named in `paddys_book.md` but carried no IDs at time of writing. Reconcile with the Quests directory before they harden.
- The 50% daily interest must be **shown in UI as a number, never as a warning.** No red text, no "are you sure?" modal. The horror is that the game presents it as neutrally as Paddy does.
- The Debt Ghost's warning must be audible in Paddy's presence, with Paddy visibly permitting it. If the warning is staged as a secret, the joke inverts and Paddy becomes a conventional villain.
- The ledger's third column — the one-word note on every customer, including the player — should never be readable. Multiple examine attempts, always obscured, no reveal. It is the single best unresolved detail in the location.
- Balance risk: "On a Roll" and "Chasing Losses" both push bet sizes upward, which means an unlucky player can compound very fast. Cap automatic escalation, or the debt quest triggers before the player has understood the gambling systems at all.
- Consider: an achievement for backing "Police raid tonight" at 50:1. Whether it can ever pay out is a design decision that should be made deliberately and probably answered "no."
- Voice acting priority: **third in Publandia**, after Seamus and Mickey. Paddy has fewer lines but they carry more weight per line; cast for stillness rather than charm.

---

## 🚫 Warnings & Restrictions

### ⚠️ CRYPTO CHECK
- [x] **Crypto content conforms to `design/economy/economy_system.md`** — Paddy has no crypto content. Paddy's Book runs entirely on physical cash Sov: 20 Sovs dice entries, 50 Sovs tournament buy-ins, 100 Sovs Special minimums, 500 Sovs High Roller threshold, and loans in notes. Nothing in the location touches SOVS or the darknet shitcoin pool, and nothing has been added.
- [x] **NO automatic crypto assumptions** — a bookmaker whose entire edge is untraceable cash and deniable records would consider an immutable public ledger professionally insane. The absence is characterisation, not an omission.
- [x] **Coins, kiosks, and certificates come from the master pool** — none invented here; none used here.
- [x] **The bros are never scam-aware** — Lord Pilsner wins early and concludes the dice listen to him, loses late and invokes the law of averages, and is asking about the loan before he ever considers that the game was tilted. Chadwick reframes the debt itself as character development. Neither ever arrives at "we were robbed."
- [x] **Nothing winks** — Paddy's total in-fiction transparency is aimed at other characters. No line, sign, tooltip, or examine text signals to the player that any of this is satire.
- [x] **Focus on city-specific cultural exploitation instead** — Irish bookmaking tradition, proposition-betting culture, the romance tourists attach to "authentic" criminal experiences, and betting on Dublin rain.

### Satirical Target Verification
- [x] Targets tourist/frat bro behavior, NOT local culture or ethnicity — the joke is the tourist certainty of having a system, in a room with a sign reading "THE HOUSE IS ALWAYS RIGHT."
- [x] NPC is savvy entrepreneur, not villain or stereotype — Paddy is courteous, numerate, never violent in person, and discloses every term. He is dangerous because he is honest, not because he is criminal.
- [x] Humor is affectionate mockery, not mean-spirited — gambling addiction is treated as real and the satire targets the industry's arithmetic, never the addicted. The Debt Ghost is written with sympathy and given the most useful line in the building.

---

## 🔧 Development Status

- **Status**: Drafted
- **Profile File Location**: `Design/World Design/Publandia/npcs/Paddys_Book/npc_paddy_malone.md`
- **Registered In**: **No `paddys_book_npcs.json` exists for this location** — the expected roster file `paddys_book_npcs.json` does not exist; NPC not yet registered in a JSON roster. (Only `cloverleaf_npcs.json` and `paddys_premium_motors_npcs.json` exist under Publandia at time of writing.)
- **Sprite Sheet**: `paddy_malone.png` (512x384 — verified against `PNG_Assets/Paddys_Book_PNG_Assets.md`, Sprite Sheet 2)

## 📜 Revision History

| Date | Change | Author |
|------|--------|--------|
| 2026-08-01 | Initial profile | Claude (NPC authoring pass, Publandia Wave 1) |

---

*Template Version 1.1*
