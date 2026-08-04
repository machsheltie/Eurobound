# The Black-Tie Backroom

*Where Sinfonia's elite gamble fortunes while pretending they're just "having a flutter" — high-stakes games hidden behind opera house sophistication*

## Location Identity
- **Location ID**: sinfonia_operahouse_blacktie_backroom_01
- **Display Name**: The Black-Tie Backroom
- **German Alias**: "Der Schwarze Krawatte Hinterzimmer"
- **Satirical Subtitle**: "Where Fortunes Go to Die in Style"
- **World Location**: Sinfonia
- **Area Zone**: Hidden behind The Bassline Opera House
- **Location Type**: Exclusive Underground Lounge / Gambling Den / Mini-Game Hub / Reputation Gate

## Access & Requirements
### Entry Conditions
- **Time Restrictions**: 9 PM - 5 AM (after opera, before breakfast shame)
- **Stat Requirements**: +3 Charm OR +3 Bravado minimum (can't fake belonging here)
- **Item Requirements**: 
  - Black-Tie Attire equipped (available from Haute Couture Haberdashery)
  - OR "Member's Card" (quest reward)
  - OR Invitation from NPC (rare)
- **Previous Location Requirements**: Must discover the entrance via:
  - Backstage labyrinth exit (The Bassline Opera House)
  - OR hint from Café Existenz regulars
  - OR overheard gossip from Kaffeehaus Row
- **Special Conditions**: Gold minimum of €500 to enter (they "hold" it as collateral)

### The Hidden Entrance
The Backroom's entrance is a layered secret:
1. **Opera House Backstage**: A door marked "Private — Staff Only" (not actually staff area)
2. **The Passage**: Narrow corridor behind prop storage, decorated like a closet
3. **The Second Door**: Looks like a broom closet, actually opens to stairs
4. **The Final Check**: Doorman at bottom of stairs verifies attire, stats, and "collateral"

### Exit Conditions
- **Normal Exit**: Back through passage (if you still have dignity)
- **Completion Requirements**: Play at least one game (win or lose)
- **Failure States**: 
  - "Cleaned Out" — lose all gold, ejected with Embarrassed status
  - "Banned" — cheat and get caught, 24-hour lockout
- **Progressive Unlocks**: "High Roller" status after winning €1000+ total (better tables)

## Visual Design
### The Hidden Entrance
- **Opera House Side**: Unremarkable door, easily missed
- **The Passage**: Deliberately shabby, discourages curiosity
- **The Staircase**: Suddenly elegant — marble steps, brass railings, gas lamp style lighting
- **The Transition**: From dusty backstage to gilded luxury in 30 steps

### Interior Layout — The Gilded Cage

**The Foyer (Verification Zone)**
- Small antechamber where doorman assesses worthiness
- Mirror for final attire check (and surveillance)
- "House Rules" posted in elegant calligraphy:
  - "Gentlemen settle debts. Ladies collect them."
  - "The House always wins. The House is very polite about it."
  - "Cheating is punished. Being caught cheating is punished more."
- Gold deposit window (your "collateral")

**The Main Floor (Common Games)**
- Open floor with multiple gaming tables
- Roulette, blackjack, poker — all dressed up as "private club games"
- Bar along one wall (drinks are "complimentary" — built into house edge)
- Crystal chandeliers, velvet everything, gold leaf details
- Where most visitors play (and lose)

**Aaron's Corner Table (Named Main-Floor Zone)**
- Zone ID: `aarons_corner_table` — a felt-covered corner table set apart from the open floor's gaming tables
- **Not a playable table.** Deliberately built to read as its own thing at a glance: different felt tone, its own low pendant lamp instead of the floor's shared table lights, no house chip rail, no dealer plaque, no bet-placement markings. The room's real poker, roulette, and blackjack tables keep the standard house dressing; this one never does. The two must never be confused
- Occupied by Aaron the Unflappable (`sinfonia_npc_aaron_unflappable_01`) — **Full Profile**: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/aaron_the_unflappable.md`
- **Scene trigger**: approaching the table with entry conditions met fires `blacktie_event_kings_were_humming_01`, one time only. The scene is spectator-only; no betting interface opens here, ever. Stake is the door's €500 collateral chips
- **Scene ownership**: the encounter's beats, dialogue, player-choice moments, and item grants live in `Design/Quests/Location Specific/Sinfonia/thekingswerehumming.md` and are not duplicated in this file
- **Post-encounter**: Aaron remains at this table permanently as ambient floor presence. Never a playable opponent, never a mini-game node

**The High Stakes Salon (High Roller Area)**
- Separated by velvet rope (requires High Roller status)
- Tables with higher minimums, bigger payouts
- Personal servers, better odds (still house-favored)
- Where the REAL money moves
- Where Maestro Vice von Strauss sometimes plays

**The Private Boxes (VIP)**
- Individual rooms for discreet games
- Unlocked via special invitation or major wins
- Where the shady deals happen
- Card sharks' natural habitat
- Quest-relevant encounters

**The Vault Antechamber (Post-Boss Access)**
- After defeating Maestro Vice von Strauss
- His keys unlock this area
- Contains Baroness' personal vault
- Late-game gear storage

### The Aesthetic
Every detail screams "legitimate sophistication masking vice":
- Chandeliers that cost more than houses
- Servers in better suits than the guests
- Background music: String quartet playing cards-themed classical
- Chips made of actual silver (house takes them back)
- "No photography" signs (for everyone's protection)

### Technical Specifications
- **Color Palette**: Primary: Velvet Burgundy (#722F37), Accent: Gold Leaf (#FFD700), Background: Midnight Blue (#191970), Vice Black (#0D0D0D)
- **Lighting Setup**: Warm chandelier glow, focused table lights, shadowy edges
- **Particle Systems**: Smoke wisps (cigars), chip shine, card flutter, champagne bubbles
- **Animation Elements**: Card dealing, chip stacking, roulette spin, NPC reactions
- **Performance Optimization**: Pre-rendered roulette, simplified card animations, static crowd

## Satirical Design
### Theme & Vibe
**Core Concept**: The Black-Tie Backroom satirizes the hypocrisy of "respectable" gambling — the way high society pretends card games and roulette are sophisticated pastimes rather than the same vice available in seedier establishments. The only difference is better lighting and more expensive losses.

The deeper joke: Everyone here is either desperately addicted or desperately bored. The "sophistication" is a thin veneer over the same human weakness. The tuxedos don't make the gambling noble — they just make the losses tax-deductible.

### The House Always Wins (Literally)
The Backroom's business model is transparent if you look:
- "Complimentary" drinks encourage continued play
- Chips are silver (feels valuable) but have no value outside
- "Gentleman's games" have hidden house edges
- The helpful servers track your tells for the dealers
- "Luck" at first often turns when you bet bigger

Everyone knows. No one admits it. That's the game within the game.

### Cultural Targets
- **Primary Satirical Focus**: High-society gambling, wealth performance
- **Secondary Targets**: Casino culture, gentlemen's club pretension, addiction dressed in elegance
- **Cultural Specificity**: European private gaming clubs, old-imperial gambling-salon traditions
- **Humor Approach**: The sophistication makes the desperation funnier
- **Sensitivity Considerations**: Satirizes gambling culture, not addiction itself; no romanticization

### Seedy Underbelly Elements
- **Primary Vice**: Gambling (the ENTIRE place is vice)
- **City-Specific Comedy Operations**: Opera money laundering, "donations" that are debts, reputation as currency
- **Buffoon Exploitation**: Bros who think their luck/skill can beat the house (it cannot)
- **Comedy of Errors**: Dramatic losses, accidental wins that encourage bigger losses, tells
- **Consequence System**: Gold loss is REAL; Embarrassed status from public losses; Cleaned Out ejection

### Buffoon Delusion Scenarios

**What bros THINK is happening**: 
"We're in an EXCLUSIVE club! We're basically James Bond! I'm going to WIN BIG!"

**What is ACTUALLY happening**: 
The house is systematically extracting their gold while they feel sophisticated.

**The Entry**:
- **Lord Pilsner**: "Dude, we're IN. We're VIPs. We're HIGH ROLLERS."
- **Reality**: They barely met the minimum requirements and the doorman is placing bets on how fast they'll lose.

**The First Win**:
- **Chadwick**: "I WON! I'm a NATURAL! This is MY GAME!"
- **Reality**: The house lets early wins happen. Encourages bigger bets.

**The Inevitable**:
- **Lord Pilsner**: "Okay, ONE more hand. I can feel the luck turning."
- **Bradley**: "We have forty euro."
- **Lord Pilsner**: "That IS one more hand."

**The Cleanup**:
- **Chadwick**: "How did we... we had €500... where did..."
- **Doorman**: "Thank you for visiting. Please return when you've... recovered."

## Gameplay Mechanics

### The House Edge System

**Gold Economy**:
- Minimum €500 gold to enter (held as collateral)
- All games use house chips (no gold directly)
- Chips convert back to gold at exit (minus "handling fee")
- House edge varies by game and table
- "Complimentary" items deducted from winnings

**The Hidden Math**:
| Game | Displayed Odds | Actual House Edge | High Roller Edge |
|------|----------------|-------------------|------------------|
| Roulette | "Fair" | 5.3% | 2.7% |
| Blackjack | "Standard" | 4.2% | 1.8% |
| Poker (vs House) | "Skill-based" | 8% rake | 4% rake |
| Poker (vs NPCs) | Varies | True skill | True skill |

### Card Games — Poker (Primary Mini-Game)

**Sinfonian Hold 'Em**:
- Texas Hold 'Em with period-appropriate terminology
- Can play vs House Dealer OR vs NPC opponents
- NPCs have tells that can be learned

**NPC Opponents**:

**The Nervous Noble** (Easy)
- **Tell**: Adjusts cufflinks when bluffing
- **Pattern**: Folds to aggression, overplays strong hands
- **Bankroll**: €200 (small wins)

**The Silent Countess** (Medium)
- **Tell**: Sips champagne more frequently when strong
- **Pattern**: Calculated, occasional bluffs, exploits weakness
- **Bankroll**: €500 (moderate wins)

**The Card Shark** (Hard)
- **Name**: Herr Falsch ("Mr. False")
- **Tell**: None apparent (actually has one: breathes slower when bluffing)
- **Pattern**: Adapts to player style, varies play
- **Bankroll**: €1000+ (major wins possible)
- **Special**: Defeating him unlocks "Shark Fin" accessory

**The House Dealer** (Unbeatable Long-Term)
- **Name**: Various — they rotate
- **Tell**: N/A (house always plays optimally)
- **Pattern**: Perfect basic strategy, no emotion
- **Bankroll**: Unlimited (the House)
- **Note**: Can win sessions, can't beat the edge over time

### Roulette (Secondary Mini-Game)

**Sinfonian Wheel**:
- Single-zero European style (better than American)
- Can bet numbers, colors, odd/even
- Special bets: "Composer's Dozen" (Mozart's favorite numbers, fake)

**Betting Options**:
| Bet Type | Payout | Actual Probability |
|----------|--------|-------------------|
| Single Number | 35:1 | 2.7% (1/37) |
| Red/Black | 1:1 | 48.6% |
| Composer's Dozen | 2:1 | 32.4% |
| "Lucky" Number | 35:1 | 2.7% (no luck involved) |

### Blackjack (Tertiary Mini-Game)

**Twenty-One Sinfonian**:
- Standard rules with period terminology
- Dealer stands on 17
- Can double, split, surrender

**House Rules (Disadvantage)**:
- Only one split allowed
- No surrender after dealer checks
- "Tip the dealer" encouraged (reduces winnings)

### Cheating System (High Risk)

**Cheat Options** (require items or skills):
- **Marked Cards**: +15% win rate, caught on nat 1 (5% chance per hand)
- **Sleeve Ace**: Auto-win one hand, caught if used twice in session
- **Chip Palming**: Steal €50/attempt, caught on visible tells
- **Partner Signals**: With party member at same table, share information

**Getting Caught**:
- First Offense: Warning, lose current bet, watched closely
- Second Offense: Banned 24 hours, lose all chips, Embarrassed status
- Third Offense: Permanent ban, bouncer "escort" (combat encounter)

### The Card Shark Boss Fight

**Alternative to Gambling**:
If players lose repeatedly (€1000+ total) OR discover Herr Falsch is cheating, they can challenge him directly.

**Boss Profile — Herr Falsch**:
- **Title**: The House's Secret Weapon
- **Appearance**: Immaculate tuxedo, card-themed accessories, knowing smile
- **Personality**: Enjoys the game more than the winning
- **Secret**: He's been cheating the whole time (sleeve cards, marked deck)

**Boss Fight Mechanics**:
- Hybrid combat: Regular attacks + card-based special moves
- **Attacks**:
  - "Full House": Summons card construct allies
  - "Dead Man's Hand": Targets single character with debuff stack
  - "The River": Changing arena hazard (cards flip tiles)
  - "Ace Up His Sleeve": Interrupt attack when below 25% HP
- **Weakness**: Exposing his cheating during fight reduces his stats
- **Victory**: His entire chip stash (€2000), "Shark Fin" accessory, "Card Counter" achievement

### Couchsurfing Integration
**Host**: "The Reformed Gambler" — Siegfried, runs the coat check

**Meeting Requirements**:
- Win at least once
- Lose at least once (he relates to the struggle)
- Tip him personally (€20)

**Stay Details**:
- Sleep in his tiny apartment above the club
- "Dreams of Fortune" reveal how he lost everything (tragic backstory)
- Wake to him preaching the dangers of gambling (while ironing your tuxedo)

**Morning Scene**:
- He lost €50,000 over 10 years
- Now works coat check to "stay close to what he can't have"
- Offers genuine advice: "The only winning move is not to play. But we both know you'll play anyway."

**Stay Effects**:
- "Gambler's Insight": See one hidden card per game for next session
- -€50 (he "borrowed" it — can't help himself)
- Permanent 5% reduction in house edge (knows their tricks)

### Selfie Spot Integration

**Location**: The High Stakes Salon (requires High Roller status)

**Standard Photo**:
- Posed with chip stack (provided for photo, must return)
- Green felt table, chandelier above
- Caption: "High Roller Status"

**"The Winner"** Variant:
- After significant win (€500+)
- Actual chips visible
- Defeated opponent in background (if applicable)
- Caption: "The House Doesn't ALWAYS Win"

**"The Shark Slayer"** Variant:
- After defeating Herr Falsch
- His marked cards visible on table
- Caption: "Caught the Card Shark"

## NPCs & Characters

### The Doorman — Viktor
- **NPC ID**: `sinfonia_npc_viktor_doorman_01`
- **Full Profile**: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/viktor_the_doorman.md`
- **Role**: Entry verification, stat check, gold collection
- **Appearance**: Built like a bouncer, dressed like a butler
- **Personality**: Politely threatening
- **Function**: Gatekeeper, can be bribed for information
- **Dialogue**: "Your attire is... acceptable. Your collateral is... sufficient. Your chances of leaving with it are... statistically improbable. Welcome."

### The Pit Boss — Madame Karten
- **NPC ID**: `sinfonia_npc_madame_karten_01`
- **Full Profile**: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/madame_karten.md`
- **Role**: Floor manager, game oversight, rule enforcer
- **Appearance**: Elegant older woman, eyes that miss nothing
- **Personality**: Grandmother's warmth with shark's instincts
- **Function**: Runs games, catches cheaters, offers "advice" (encourages betting)
- **Dialogue**: "Darling, you seem TENSE. Another drink? The cards favor the relaxed player. *They don't, but she'll never say that.*"

### Herr Falsch — The Card Shark
- **NPC ID**: `sinfonia_npc_herr_falsch_01`
- **Full Profile**: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/herr_falsch.md`
- **Role**: Hidden boss, poker opponent, cheater-in-chief
- **Appearance**: Too perfect tuxedo, card-themed accessories, smile that knows secrets
- **Personality**: Enjoys the con as much as the win
- **Function**: Hard mode opponent, optional boss fight
- **Dialogue**: "Luck is just skill's more attractive sibling. I have both. *He has neither — just better cheating.*"

### The Nervous Noble — Graf von Zittrig
- **NPC ID**: `sinfonia_npc_graf_von_zittrig_01`
- **Full Profile**: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/graf_von_zittrig.md`
- **Role**: Easy poker opponent, comic relief
- **Appearance**: Sweating through expensive clothes, obvious tell adjustments
- **Personality**: Desperate to look calm, failing visibly
- **Function**: Learning opponent, loses entertainingly
- **Dialogue**: "I'm perfectly calm. *adjusts cufflinks for the 47th time* Completely calm. Your bet? *cufflinks again*"

### The Silent Countess — Gräfin Stille
- **NPC ID**: `sinfonia_npc_grafin_stille_01`
- **Full Profile**: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/grafin_stille.md`
- **Role**: Medium poker opponent, mysterious regular
- **Appearance**: Perfect poker face, speaks only in bets
- **Personality**: Communicates through play, unsettling composure
- **Function**: Skill check opponent, challenging but fair
- **Dialogue**: *Sips champagne. Raises €100. No other communication necessary.*

### The Coat Check — Siegfried
- **NPC ID**: `sinfonia_npc_siegfried_coatcheck_01`
- **Full Profile**: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/siegfried_coat_check.md`
- **Role**: Coat check attendant; couchsurf host (see Couchsurfing Integration, above)
- **Function**: Item storage, tip interaction, couchsurf questline entry

### Aaron the Unflappable
- **NPC ID**: `sinfonia_npc_aaron_unflappable_01`
- **Full Profile**: `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/aaron_the_unflappable.md`
- **Zone**: `aarons_corner_table` (main floor) — resident, all opening hours
- **Function**: Scene trigger for `blacktie_event_kings_were_humming_01`; ambient floor presence thereafter. Never a playable opponent
- **Scene ownership**: `Design/Quests/Location Specific/Sinfonia/thekingswerehumming.md`

### Easter Egg — The Entrance Conversation (author-dictated 2026-08-03)
- **Zone**: just inside the entrance, main floor side
- **What it is**: A purely ambient background scene running while the bros do anything near the entrance: a pretty brunette in a little black dress is being chatted up — hit on, frankly — by the security guards. Both of them. Competing. Entirely off-duty about it.
- **Overheard fragments** (ambient text bubbles; draft lines pending author approval):
  - Guard 1: "There is absolutely no way you're forty-four."
  - Guard 2: "Ignore him. But seriously. No way."
  - She just smiles.
- **Rules**: The bros never notice the scene, never comment, never interact. No quest hook, no examine text, no name, no roster entry, no explanation — ever. The scene simply exists near the door, every visit.

### Bros' Black-Tie Backroom Reactions

**At the Door**:
- **Lord Pilsner**: "€500 COLLATERAL?! That's... that's a lot of döner."
- **Viktor**: "It's also the minimum. Döner is not accepted."
- **Chadwick**: "We're COMMITTED now! This is CONTENT! 'Chadwick Gambles with the ELITE'!"

**First Game**:
- **Lord Pilsner**: "Okay, I KNOW poker. I've seen Casino Royale like THREE TIMES."
- **Chadwick**: "So you're basically Bond."
- **Lord Pilsner**: "Same energy!"
- *It was not the same energy.*

**Winning Early**:
- **Chadwick**: "WE'RE UP! WE'RE ACTUALLY UP!"
- **Madame Karten**: "How wonderful! Perhaps a larger table? The cards seem to favor you tonight..."
- **Bradley**: "Or we could leave."
- **Lord Pilsner**: "And go WHERE, Bradley? We're WINNING."

**Losing Later**:
- **Lord Pilsner**: "I don't understand. I was WINNING."
- **Chadwick**: "My CONTENT... it's becoming a TRAGEDY..."
- **Bradley**: "I'm poor now."

**Discovering Herr Falsch's Cheating**:
- **Chadwick**: "WAIT. He's been CHEATING?! I KNEW something was off!"
- **Lord Pilsner**: "That means... we didn't lose because we're BAD... we lost because he's a CRIMINAL!"
- **Bradley**: "Comforting."
- **Lord Pilsner**: "Let's FIGHT him."

## System Integration

### Quest Integration
- **"The Black-Tie Backroom"**: Discovery quest (from city description)
- **"High Stakes"**: Win €1000+ total for High Roller status
- **"The Card Shark"**: Discover and defeat Herr Falsch
- **"The Reformed Gambler"**: Siegfried's backstory questline
- **"Baroness' Vault"**: Access after defeating Maestro Vice von Strauss (late-game)
- **"The Kings Were Humming"** (`sinfonia_sidequest_the_kings_were_humming_01`): One-time scene at `aarons_corner_table`, triggered by `blacktie_event_kings_were_humming_01` on approach with entry conditions met. Requires the €500 door collateral to be on deposit (under-funded parties never get past Viktor). Quest file: `Design/Quests/Location Specific/Sinfonia/thekingswerehumming.md`

### Item Registrations
**Scene-granted (not vendor stock, not house inventory — obtainable only from `blacktie_event_kings_were_humming_01`)**:
- `item_candy_smokes` — Puff-Puff-Powder™ Chalk 'n' Ash Candy Smokes. Item file: `Design/Inventory/items/candy_smokes_item.md`
- `item_tractor_nft` — "She Thinks My Tractor's Sexy" (Mint #42). Advances the Frat Bro NFT hunt (Sinfonia leg). Item file: `Design/Inventory/items/tractor_nft_item.md`

Both grants are staged in the quest file; neither appears at the bar, the cage, or any table.

**House-sourced (existing location canon, now formalized)**:
- `item_shark_fin` — Shark Fin accessory, awarded for defeating Herr Falsch. Item file: `Design/Inventory/items/shark_fin_item.md`
- `item_members_card` — Member's Card, alternative Backroom access. Item file: `Design/Inventory/items/members_card_item.md`

### Cross-Location Dependencies
- **The Bassline Opera House**: Backstage connects here; Maestro's keys open vault
- **Café Existenz**: Regulars hint at Backroom existence
- **Haute Couture Haberdashery**: Black-Tie Attire sold here
- **Baroness' Ballroom**: Connected via social network; vault keys relevant

### Achievement Track
- **"The Door Opens"**: Enter for the first time
- **"First Blood"**: Win any game
- **"Cleaned Out"**: Lose everything (technically an achievement)
- **"High Roller"**: Achieve High Roller status
- **"The Shark Slayer"**: Defeat Herr Falsch
- **"Reformed Witness"**: Hear Siegfried's full story
- **"Vault Access"**: Open Baroness' personal vault

## Audio Design

### Environmental Audio
- **Ambient**: Chip clicks, card shuffles, murmured conversations, distant string quartet
- **Music**: Elegant classical with subtle tension undertones
- **Interactive**: Roulette ball spin, card deal, chip stacking
- **Comedy**: Sad trombone on losses (internal, not audible in-world)

### Character Audio
- **Viktor**: Deep, measured, vaguely threatening
- **Madame Karten**: Warm grandmother voice with predator edge
- **Herr Falsch**: Smooth, confident, hints of amusement
- **NPCs**: Various relief levels in voice (nervous to composed)

### Win/Loss Stingers
- **Small Win**: Subtle positive chime
- **Big Win**: Triumphant flourish
- **Small Loss**: Quiet deflation
- **Big Loss**: Dramatic orchestral drop
- **Cleaned Out**: Full tragedy score moment

## Implementation Specifications

### Technical Requirements
- **Asset List**:
  - Hidden entrance sequence (3 stages)
  - Main floor with multiple tables
  - Aaron's corner table (non-playable scene zone, distinct dressing from the gaming tables)
  - High Stakes Salon (separate area)
  - Private boxes (VIP rooms)
  - Vault antechamber (post-boss)
  - Gaming table interfaces (poker, roulette, blackjack)
  - 6+ NPC opponents
  - Herr Falsch boss sprite
- **Animation Requirements**:
  - Card dealing sequences
  - Chip movement
  - Roulette spin
  - NPC tells (subtle)
  - Win/loss reactions
- **Performance Budget**: 45 FPS target, max 20 draw calls, 50MB memory
- **Platform Considerations**: Pre-rendered card animations, simplified roulette, streamlined betting input

### Development Timeline
- **Asset Creation**: 12 hours (multiple game interfaces, elegant environment)
- **Implementation Phase**: 18 hours (gambling systems, boss fight, probability math)
- **Testing Requirements**: Game balance, cheat detection, economy impact
- **Polish Phase**: 8 hours (animations, audio sync, NPC tells)

## Quality Assurance Checklist
- [x] **World consistency verified** (Sinfonia specific)
- [x] **Cultural specificity confirmed** (European private gaming clubs)
- [x] **Satirical targets appropriate** (Wealth gambling, not addiction)
- [x] **Gameplay value established** (Multiple mini-games, boss, economy system)
- [x] **Sinfonia requirements met**:
  - [x] High society expectations
  - [x] Formal etiquette (dress codes)
  - [x] Imperial history (old-imperial gambling-salon traditions)
  - [x] Luxury/sophistication
- [x] **No unsanctioned crypto elements** (traditional gambling satire; the single tractor token is the sanctioned Frat Bro NFT hunt item, scene-granted only)
- [x] **Aaron's corner table visually distinct from all playable tables** (no betting UI reachable at that zone)

---

## PNG Asset Requirements Summary

*Full artist specs: `Design/World Design/Sinfonia/PNG_Assets/the_black_tie_backroom_png_assets.md`*

### Environment Art (13 PNGs)
- hidden_entrance.png - 256x384 - Opera backstage door
- staircase_transition.png - 256x512 - Shabby to elegant
- foyer_verification.png - 384x256 - Entry checkpoint
- main_floor.png - 640x512 - Primary gaming area
- high_stakes_salon.png - 512x384 - VIP gaming
- private_box.png - 256x256 - Individual rooms
- vault_antechamber.png - 384x384 - Post-boss area
- poker_table.png - 384x256 - Card game interface
- roulette_table.png - 384x384 - Wheel interface
- blackjack_table.png - 384x256 - 21 interface
- bar_area.png - 256x192 - Complimentary drinks
- chandelier_detail.png - 192x192 - Ambient luxury
- aarons_corner_table.png - 320x256 - Corner table zone (distinct from playable tables)

### Character Sprites (11 PNGs)
- viktor_doorman.png - 96x128 - Entrance guardian
- madame_karten.png - 64x96 - Pit boss
- herr_falsch.png - 128x192 - Card shark boss
- nervous_noble.png - 64x96 - Easy opponent
- silent_countess.png - 64x96 - Medium opponent
- house_dealer.png - 64x96 - Table dealer
- siegfried_coatcheck.png - 64x96 - Couchsurf host
- high_roller_npc.png - 64x96 - Background elite
- server_tray.png - 64x96 - Drink bearer
- bouncer_escort.png - 96x128 - Cheat consequence
- aaron_the_unflappable.png - 96x128 - Corner table resident

### UI/Item Sprites (14 PNGs)
- chip_stack.png - 64x64 - Currency display
- card_deck.png - 48x64 - Dealing animation
- roulette_wheel.png - 192x192 - Spinning interface
- bet_interface.png - 256x128 - Placement UI
- house_edge_meter.png - 128x32 - Hidden math visualization
- high_roller_badge.png - 48x48 - Status indicator
- shark_fin.png - 32x48 - Boss reward accessory
- marked_cards.png - 48x64 - Cheat item
- collateral_receipt.png - 48x32 - €500 deposit
- members_card.png - 48x32 - Access item
- tell_indicator.png - 32x32 - NPC weakness hint
- cleaned_out_stamp.png - 64x64 - Failure badge
- candy_smokes_carton.png - 48x48 - Scene-granted item icon
- tractor_nft_token.png - 32x32 - Scene-granted item icon

---

*The Black-Tie Backroom: Where the elite lose fortunes with dignity, the drinks are "complimentary" (they're not), and the house always wins (unless you literally fight the card shark). Dress code: Black tie. Minimum buy-in: €500. Minimum wisdom required: More than you probably have. The cards are waiting. The odds are not in your favor. Welcome.*
