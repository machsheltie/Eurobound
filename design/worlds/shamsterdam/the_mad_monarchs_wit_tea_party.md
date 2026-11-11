# The Mad Monarch's Wit-tea Party

*Happy birthday. Still.*

> **Doc status (2026-11-10).** Built from `design/templates/location_validation_template.md`.
> **APPROVED (author, Round v23, `docs/superpowers/NEXT_WORK.md`):** the name (author-minted) and the
> concept in "Approved Concept" below, including the witbier specialty. **APPROVED (author, Round
> v24, 2026-11-10):** everything else in this doc as written: the location ID, the tour challenge,
> the beer, the opener, the stamp, the selfie, the brewmaster, every price and every line of
> dialogue. The Mad Monarch owns wheat beer in Shamsterdam (the Wobbly Windmill's beer is an amber
> ale, Windmill Grist). The "Author Rulings — Approved" table at the bottom is the record.

## Approved Concept (author canon — do not alter)

A brewery that has thrown the Monarch's Birthday party every day since 1998, because the owner
woke up on the morning after and decided the morning after was for cowards. Everything is orange:
the beer, the walls, the urinal cakes, and anyone who arrives in another colour, because the
bouncer has a paint sprayer. The bros get sprayed at the door and say thank you. Lord Pilsner
thinks the cardboard crown means he has been knighted.

**Author addition:** it specialises in brewing, serving and selling wheat beer (witbier). The name is
a witbier + Mad Hatter tea-party pun: witbier is served in teacups.

**Constraints:** no named real royal; the holiday stays generic ("the Monarch's Birthday"); never
"Oranje" in a name.

---

## Location Identity
- **Location ID**: `shamsterdam_cheeseclog_mad_monarchs_wit_tea_party_01`
- **Display Name**: The Mad Monarch's Wit-tea Party
- **Satirical Subtitle**: "Happy Birthday. Still."
- **World Location**: Shamsterdam
- **Area Zone**: Cheese & Clog Corner (the national-stereotype district; orange is the house
  colour of the stereotype)
- **Location Type**: Brewery Tour Location #4 / Witbier Brewpub / Party That Will Not End

---

## Access & Requirements

### Entry Conditions
- **Time Restrictions**: None. It has not closed since 1998. Every clock in the building is stopped
  at six o'clock.
- **Stat Requirements**: Orange. The bouncer handles it.
- **Item Requirements**: The Blarney Trap Bottle Opener (Publandia) — required for ANY brewery tour
  location (standing tour rule, `design/quests/general_quests/brewerytour.md`)
- **Previous Location Requirements**: None
- **Special Conditions**: Every non-orange guest is sprayed at the door (approved). Applies the
  cosmetic overlay "Freshly Painted" (persists until the next sleep, like Bottoms Down's
  sawdust overlay; NPCs across Shamsterdam treat the bros as party guests while it lasts).

### Exit Conditions
- **Normal Exit**: Out the front, still orange
- **Completion Requirements**: Complete "Clean Cup, Move Down" (below)
- **Failure States**: Party wipe = the bros wake up at the far end of the tea table with fresh
  crowns, re-sprayed. 30-minute lockout ("you missed the toast").
- **Progressive Unlocks**: Seat at the head of the table, the knighting selfie, the opener, Six
  O'Clock Wit on the menu

---

## Visual Design

### Exterior Description
- **Approach**: A side street off Cheese & Clog Corner that has been orange for 28 years. The
  cobbles are orange to the kerb. So is a parked bicycle that has not moved since 2001.
- **Entrance**: Double doors under an orange awning. The bouncer stands beside them with a paint
  sprayer on a backpack tank.
- **Signage**:
  - Banner over the door: "HAPPY BIRTHDAY YOUR MAJESTY" — faded, re-hung every morning
  - Board by the door: "WITBIER — BREWED HERE — SERVED IN CUPS — SOLD BY THE POT"
  - Small plaque: "TODAY IS THE MONARCH'S BIRTHDAY. TOMORROW IS CANCELLED."
- **Atmosphere**: A brass band playing the same birthday song since 1998, bunting, paint mist
- **Environmental Context**: Clog and cheese shops on both sides, all of their awnings orange from
  overspray. None of them asked.

### Interior Visuals
- **Layout**: A long hall with one tea table forty metres long running from the door to the back
  wall, a raised head-of-table dais under the banner, the brewhouse visible behind glass
- **Lighting**: Orange bulbs, orange lampshades, orange light. Daylight through orange-painted windows.
- **Furniture & Props**:
  - Forty metres of mismatched chairs, every one painted orange, some over people's coats
  - Bone-china teacups and teapots by the hundred, all orange
  - The brewhouse: a row of copper tea urns that are the fermenters. There is no tea in the
    building. Ordering tea gets witbier.
  - The cake: the original 1998 birthday cake, re-iced in orange every morning. It is now mostly
    icing and partly geology. Slices are served daily. Bradley has three. They are 28 years old
    and he says they're fine, and they are, until about the second pot.
  - The gents: orange urinals, orange urinal cakes. After the third pot of witbier, everything in
    them is orange too. Chadwick films it for the colour grading.
  - A wall calendar on the 1998 page; staff tear the day off each morning and pin it back
  - Every clock stopped at six
  - A box of cardboard crowns by the door, handed to every guest
- **Decorative Elements**: Twenty-eight years of bunting layered like tree rings; framed photos of
  every year's party, all identical
- **Atmospheric Effects**: Paint mist drifting in from the door, streamer confetti, steam off the urns
- **Hidden Areas**: The cellar door, marked "DO NOT OPEN UNTIL TOMORROW"

### Technical Specifications
- **Color Palette**: Primary: Party Orange (#FF7A00), Accent: Crown Gold (#E8B830), Background:
  Witbier Haze (#F6D7A7), Bone China (#FFF8F0)
- **Lighting Setup**: Saturated warm orange key, low-contrast fill; the cellar the only cool light
- **Particle Systems**: Paint mist, confetti, urn steam, cake crumbs
- **Animation Elements**: The bouncer's spray loop, the table-wide seat shift, stopped clocks
  ticking in place, the brass band
- **Performance Optimization**: Table chairs instanced; confetti pooled

---

## Satirical Design

### Theme & Vibe
**Core Concept**: The national monarch's-birthday street party, turned into a business that never
lets it end. One day a year of orange and beer is a holiday. Every day since 1998 is a lifestyle,
a brand and a debt the owner keeps postponing. The paint sprayer makes fun mandatory. The witbier
in teacups makes it look civilised. The cake makes it look like history.

**The Irony**: A party built entirely so nobody has to face the morning after, attended by three
men whose whole European tour exists for the same reason. They feel completely at home.

### Cultural Targets
- **Primary Satirical Focus**: The perpetual party; the national holiday as an all-year tourist product
- **Secondary Targets**: Mandatory fun; dressing a beer hall up as a tea party; refusing to ever have
  the hangover
- **Cultural Specificity**: The orange-out street party of the Monarch's Birthday, witbier, Shamsterdam
  canal-side brewing
- **Humor Approach**: Nobody in the building knows it's not the first day. Delivered completely straight.
- **Sensitivity Considerations**: No real royal is named or shown; the Monarch is never on screen.
  The target is the never-ending party and the orange-out product, not a monarchy or a people.

### Seedy Underbelly Elements
- **Primary Vice**: Twenty-eight years of daily drinking sold as one long birthday
- **City-Specific Comedy Operations**: Guests are sprayed orange so they can't leave unnoticed; the
  whole district is orange from overspray
- **Buffoon Exploitation**: The bros pay for a party they are also the decorations of
- **Comedy of Errors**: Musical chairs at a forty-metre table, with a full teacup at every seat
- **Consequence System**: Six O'Clock Wit postpones the hangover. It does not cancel it.

### Buffoon Delusion Scenarios
**What bros THINK is happening**: A royal party. An exclusive invitation. Lord Pilsner thinks the
cardboard crown means he has been knighted.

**What is ACTUALLY happening**: The bros have been spray-painted, crowned with cardboard and seated at
a table with men who arrived for one afternoon in 2003.

**How impaired are they**: Steadily. Teacups are small. There are a great many of them.

**Obvious signs they ignore**:
- The calendar is on 1998
- The clocks all say six
- The cake is older than some of the staff
- The 2003 stag party at the table is still in its matching shirts, 23 years older
- The bouncer sprays the bros a second time on the way out to the toilet

**How locals play along**: Everyone wishes everyone a happy birthday, constantly, sincerely.

### Social Media Potential
- **Screenshot Opportunities**: The bros mid-spray, saying thank you; the forty-metre table; Lord
  Pilsner's knighting
- **Quotable Moments**: "The morning after is for cowards." / "Clean cup! Move down!"
- **Easter Eggs**: Clocks stopped at six; the Hatter-style top hat; the cake
- **Viral Content Hooks**: Chadwick's "no filter needed" orange footage

---

## Gameplay Mechanics

### Brewery Tour Flow
1. **Get sprayed at the door** (approved beat). The bros say thank you.
2. **Take a cardboard crown.** Lord Pilsner is now, in his own mind, a knight.
3. **Order the special beer** (Six O'Clock Wit). The brewmaster rings a bell and every guest stands
   up. This triggers the challenge.
4. **Clean Cup, Move Down** (challenge, below)
5. **Head of the table**: stamp, knighting selfie, opener, beer unlocked

### Tour Challenge: "Clean Cup, Move Down"
Micro-dungeon in the standard shape (obstacle → mini-mob → boss), run along the tea table.

**1. Obstacle — Move Down (the table).** Rhythm minigame. Every eight beats the brewmaster shouts
"Clean cup! Move down!" and everyone shifts one seat toward the head of the table. Every seat has a
full teacup of witbier that must be finished before the shift, pinkie raised for a Bravado bonus.
Miss a cup and the bro behind you gets it as well. Reach the head of the table to clear the stage.

**2. Mini-mob — The Lifers (the far end).** Guests who came for one afternoon and stayed. A 2003 stag
party still in its matching shirts; a backpacker who arrived in 2009 and whose visa has expired
four times; a woman who came to collect her husband in 2011 and now runs the bunting. They fight
for their seats.
- **Attacks**: "Toast!" (forces a teacup on the target: +HP, +1 alcohol tier), "Sing-Along" (Confused),
  "Who Are You Again?" (Bravado drain)
- **Gimmick**: Every "Move down!" shuffles the enemy line one seat; the party has to fight the
  Lifer who is now in front of them

**3. Boss — The Hangover of '98 (the cellar).** When the bros take the head seats, Bradley asks
what's on tomorrow. The cellar door marked "DO NOT OPEN UNTIL TOMORROW" opens on its own. Out of it
crawls the hangover from the morning after the 1998 party, postponed for 28 years and grown with
interest: a grey, sweating mass in a deflated party hat and the original cardboard crown.
- **Boss ID**: `shamsterdam_boss_hangover_of_98`
- **Attacks**:
  - "Headache With Interest" — damage increases every turn the fight lasts
  - "Daylight" — opens the blinds; Bleary on the whole party
  - "Remember Last Night?" — Embarrassed; shows a photo from 1998 that contains Chadwick, somehow
  - "Hair of the Dog Bite" — Hungover on one bro
- **Weakness**: Witbier. A teacup drunk mid-battle heals the drinker and damages the boss. The party
  can only win by drinking more.
- **Defeat**: The brewmaster pours a full pot over it. It shrinks back into the cellar to wait for a
  tomorrow that isn't coming. The door is re-labelled.
- **Bros' combat lines**:
  - **Lord Pilsner**: "Stand aside, peasant. I've been knighted."
  - **Chadwick**: "Orange filter, no filter needed. This is the best-lit fight of my life."
  - **Bradley**: "I've woken up next to worse." *(drinks a teacup, pinkie up)*

### Consumable: Six O'Clock Wit
**Type**: Alcoholic Beverage / Brewery Tour Signature Beer
- **Style**: Witbier, 5.5% ABV, orange peel and coriander, cloudy orange, served in a teacup
- **Price**: 6 SOVS per cup; 30 SOVS per pot of six
- **Brewed By**: The Mad Monarch's Wit-tea Party

| Effect | Value |
|--------|-------|
| HP Restore | +30 |
| Bravado Restore | +15 |
| Buff | "Party's Still On" — cannot become Hungover while active |
| Drawback | "Postponed Hangover" — every Hungover the buff blocked lands at once when it ends, doubled |
| Special | Must be drunk with the pinkie raised. The animation does this automatically. |

**Flavor Text**: "It's always six o'clock. It's always the birthday. The bill comes tomorrow, and tomorrow is cancelled."

**"Party's Still On" / "Postponed Hangover" (intoxication law 10-point review)**
1. **Source**: Six O'Clock Wit
2. **Immediate effect**: Blocks Hungover for 5 turns (battle) or until the next location change (overworld)
3. **Escalation**: Each extra cup extends the block by 2 turns and adds 1 to the Postponed count
4. **Player-facing cues**: A tiny stopped clock over the bro's head; the Postponed count on it
5. **Player control**: None during the buff. On expiry, the bro is Hungover and loses his next turn
   per Postponed count, capped at 2 turns
6. **Duration/recovery**: Postponed Hungover follows normal Hungover recovery (rest, food, cure items)
7. **Comedic consequence**: The bros feel invincible for one fight and pay for it in the next
8. **Status interactions**: Counts toward the alcohol tiers; does not stack with "Canal Courage"
   Bravado protection; Bottoms Down's The Shakes still applies
9. **Technical dependencies**: Status that suppresses another status and banks a counter; expiry hook
10. **Further author approval**: Approved as written (2026-11-10, round v24)

### Bottle Opener: The Mad Monarch's Wit-tea Party Bottle Opener
- **Design**: An orange-enamelled brass teacup. The handle is the opener. A cardboard crown, folded
  tiny and lacquered, glued to the rim.
- **Inscription**: "The Morning After Is For Cowards."
- **Acquired**: Completing "Clean Cup, Move Down" only. Per the master spec, openers are earned, not
  bought, so it has no price.
- **Special Feature**: It comes pre-sprayed. Every bottle it opens shows an orange thumbprint.

### Passport Stamp
- **Design**: A teacup wearing a crown
- **Ink**: Party Orange, and it never dries. It prints a mirror-image smudge on the facing page,
  and every later passport page carries a faint orange thumbprint.
- **Animation**: The brewmaster stamps it with a teaspoon handle for a mallet
- **Stamp speech** (the brewmaster): "HAPPY BIRTHDAY!" Every time, including this time.

### Selfie Spot: The Birthday Portrait
- **Staging**: The head of the table under the banner. Lord Pilsner sits in the host's chair in his
  cardboard crown, teacup raised, pinkie out, holding still like an oil painting. The brewmaster
  stands behind him pouring from a pot held high. Chadwick and Bradley flank him in orange. The
  brass band is in frame. The 1998 cake is on the table. Nobody knights anybody: Lord Pilsner
  reached that conclusion from the crown alone (approved concept).
- **NPC reactions when shown the album**: Bartenders elsewhere wish the bros a happy birthday.
  Lord Pilsner captions it "Official portrait. Knighthood pending paperwork."
- **Overlap note**: Crown & Cask (Sinfonia) already holds a real in-world knighting ritual with
  "Sir Pilsner" as its payoff. This selfie deliberately avoids a second knighting ceremony.

### Price List
| Item | Price |
|------|-------|
| Entry (includes crown and spray) | Free |
| Six O'Clock Wit (cup) | 6 SOVS |
| Six O'Clock Wit (pot of six) | 30 SOVS |
| A slice of the 1998 cake | 4 SOVS |
| Re-spray (for the bros who ask) | 2 SOVS |

### Bravado Interactions
- **Gain**: Saying thank you to the bouncer; pinkie-up cups in the minigame; finishing the pot
- **Lose**: Asking what year it is; asking for tea; trying to leave before the toast

### Economic & Quest Integration
- **Shop Functionality**: Witbier by cup and pot, take-home bottles post-completion
- **Currency Accepted**: SOVS
- **Quest Hub Role**: Brewery Tour Location #4 of 4 for Shamsterdam; feeds "Canal Courage"
- **Objective Location**: Shamsterdam brewery tour (city quest file not yet written)

---

## NPCs (sketches only; no profile files yet)

### Brewmaster Sjors Hoedemaker
- **Role**: Owner, brewmaster, host of the party since 1998
- **Appearance**: Sixties, an enormous orange top hat with a paper tag reading "1998" tucked in the
  band, an orange tailcoat over an orange football shirt, orange hands
- **Background**: Threw the Monarch's Birthday party in 1998. Woke up the next morning, decided the
  morning after was for cowards, and put the party back on. He has done it every day since. He has
  not had a hangover in 28 years. He keeps it in the cellar.
- **Personality**: Delighted, hospitable, unstoppable. Treats every guest as if they've just arrived
  for the first birthday ever, including the ones who've been here since 2003.
- **Key Dialogue**:
  - "Happy birthday! Clean cup? Clean cup!"
  - "Tea? This IS tea. It's wheat tea. Drink it."
  - "The morning after is for cowards. We don't do mornings. We do six o'clock."
  - *to Lord Pilsner, about the crown*: "Suits you. Everybody gets one. Happy birthday."
- **Selfie role**: Pouring from on high behind Lord Pilsner's portrait

### The Bouncer (unnamed)
- **Role**: Door, paint sprayer, orange enforcement
- **Key Dialogue**: "Not orange." *(sprays)* "Orange. Happy birthday."

### Atmospheric NPCs
- **The Lifers**: the 2003 stag party, the 2009 backpacker, the 2011 bunting woman (mini-mob, above)
- **The Brass Band**: one birthday song, 28 years, no breaks

---

## Audio Design
- **Ambient Soundscape**: Brass band, teacups on saucers, paint-sprayer hiss at the door, forty metres
  of chairs scraping on "Move down!"
- **Music Style**: Oompah birthday march that loops seamlessly and has never stopped
- **Interactive Audio**: Sprayer hiss, the bell, the teaspoon on the stamp
- **Satirical Stingers**: Party horn on every seat shift; a single tired kazoo when the cellar opens
- **Character Voice Direction**: Hoedemaker booms; the bouncer speaks in single words

---

## Connected Locations
- **Directly Adjacent**: Cheese & Clog Corner
- **Quest-Connected**: The Wobbly Windmill Brewery, Bottoms Down, The Hoisted Pint (Shamsterdam brewery
  tour); The Blarney Trap (Publandia, tour access opener)

---

## Implementation Specifications

### Technical Requirements
- **Asset List**: Orange street exterior; long hall with the forty-metre table; head-table dais;
  cellar; Hoedemaker; the bouncer; the Lifers; the Hangover of '98; teacup, teapot, cake, crowns;
  stamp, opener and beer icons. PNG asset doc to follow
  (`PNG_Assets/the_mad_monarchs_wit_tea_party_png_assets.md`).
- **Animation Requirements**: Spray loop and per-character orange tint; table-wide seat shift;
  stopped clocks; boss growth over turns
- **Performance Budget**: 60 FPS, max 18 draw calls
- **Platform Considerations**: Desktop; orange tint uses a palette swap, not a full-screen filter

### State Tracking
```
mad_monarchs_state:
  - sprayed: bool
  - crown_taken: bool
  - challenge_completed: bool
  - seats_advanced: int
  - hangover_of_98_defeated: bool
  - opener_acquired: bool
  - stamp_acquired: bool
  - selfie_taken: bool
```

---

## Quality Assurance Checklist
- [x] No real city names in player-facing text; no real royal named; no "Oranje" in any name
- [x] Prices in whole SOVS
- [x] Bros never afraid, disgusted, self-aware or scam-aware
- [x] No mascots
- [x] Names grepped for uniqueness on 2026-11-10: Six O'Clock Wit, Clean Cup Move Down, The Lifers,
      The Hangover of '98, Sjors Hoedemaker, Party's Still On, Postponed Hangover, Freshly Painted
- [x] No crypto elements
- [x] Author rulings on every item: approved as written, 2026-11-10, round v24 (table below)

## Author Rulings — Approved

The author approved every proposal below as written (2026-11-10, round v24,
`docs/superpowers/NEXT_WORK.md`). This table is the approved record.

| # | Item | Approved as written | Status |
|---|------|---------------------|--------|
| 1 | Location ID / zone | `shamsterdam_cheeseclog_mad_monarchs_wit_tea_party_01`, Cheese & Clog Corner | Approved 2026-11-10, round v24 |
| 2 | Tour challenge | "Clean Cup, Move Down": teacup musical-chairs rhythm table → The Lifers → boss The Hangover of '98 from the cellar | Approved 2026-11-10, round v24 |
| 3 | Signature beer | Six O'Clock Wit, 5.5% witbier in a teacup, 6 SOVS cup / 30 SOVS pot; blocks Hungover, then it all lands at once doubled | Approved 2026-11-10, round v24 |
| 4 | Opener | Orange teacup, handle is the opener, tiny crown; inscription "The Morning After Is For Cowards.", earned only | Approved 2026-11-10, round v24 |
| 5 | Stamp | Crowned teacup in orange ink that never dries and smudges every later page | Approved 2026-11-10, round v24 |
| 6 | Selfie | "The Birthday Portrait": Pilsner enthroned in his cardboard crown, Hoedemaker pouring from on high; no actual knighting (Crown & Cask owns that) | Approved 2026-11-10, round v24 |
| 7 | Brewmaster | Sjors Hoedemaker, orange top hat tagged "1998", host since the morning after | Approved 2026-11-10, round v24 |
| 8 | Prices | Entry free, cup 6, pot 30, cake slice 4, re-spray 2 (SOVS) | Approved 2026-11-10, round v24 |
| 9 | Door overlay | "Freshly Painted" cosmetic overlay until next sleep | Approved 2026-11-10, round v24 |
