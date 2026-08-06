# Brewery Tour — Publandia Instance

**Authority:** `design/quests/general_quests/brewerytour.md` is the master spec and wins every
conflict. This file holds Publandia's four brewery instances, the Trigger sequence, the
Trinity of Pints set-piece (author-dictated redesign, 2026-08-05), and Publandia's
city-completion systems (hangover, selfies, cross-city Master's Toast).

Item-level detail (stamp/opener/beer stat blocks, PNG specs) lives in each collectible's own
file under `design/items/brewery_tour/` — this file does not duplicate it beyond a short
pointer table.

---

## The Trigger — The Blarney Trap

Publandia is where the Brewery Tour begins for the player. At **The Blarney Trap**, the bros
order the special beer for the first time. That single order is the whole ignition system:

- **The Bottle Opener Keychain** (the container item — one per party, forever)
- **The Blarney Trap's opener** (the first of sixteen)
- **The Brewery Passport Book**

...all change hands in the same moment, handed over by Seamus O'Brien. [source:
`design/quests/general_quests/brewerytour.md` "The Trigger"; `design/items/bottle_opener_keychain_item.md`;
`design/items/brewery_passport_book_item.md`]

Before this order fires, no brewery anywhere in the game — Publandia or otherwise — will
stamp a passport, sell a signature beer, or hand over an opener. The tour is invisible until
Publandia opens it.

Seamus's line on handing over the book: *"This book? It's your passport to the real beer
culture of Europe. Every brewery, every pub worth its salt — they'll stamp you. Proves you
were there. REALLY there. Fill a city's page, you earn their Legendary Hangover. Fill the
whole book? Continental Beer Master. That's not just a title. That's a LIFESTYLE."* [source:
`design/items/brewery_passport_book_item.md` L18]

---

## The Blarney Trap

**Stamp / Opener / Beer:** `stamp_blarney_trap`, `opener_blarney_trap`, `beer_blarney_trap`
(full detail in `design/items/brewery_tour/`).

### Challenge

⚠ AUTHOR TO DESIGN — Publandia challenges trend drinking games per the master spec; nothing
is designed yet.

---

## The Stoutworks Brewery

**Stamp / Opener / Beer:** `stamp_stoutworks_brewery`, `opener_stoutworks_brewery`,
`beer_stoutworks_brewery` (full detail in `design/items/brewery_tour/`).

### Challenge

⚠ AUTHOR TO DESIGN — Publandia challenges trend drinking games per the master spec; nothing
is designed yet.

---

## Trinity of Pints

**Stamp / Opener / Beer:** `stamp_trinity_of_pints`, `opener_trinity_of_pints`,
`beer_trinity_of_pints` (full detail in `design/items/brewery_tour/`). Venue reference:
`design/worlds/publandia/trinity_of_pints.md`.

**Status: FULLY DESIGNED — author-dictated redesign, 2026-08-05.** Every legacy grading/GPA/
Dean's-List mechanic tied to Trinity is dead. "We will no longer be grading." The academic
*framing* survives (cover charge as "tuition," courses as "courses," Dean Cathal in full
regalia) — only the pass/fail scoring apparatus is gone. Nothing below is a placeholder.

### Enrollment

Same cover-charge framing as the venue doc: 10 Sovs "tuition" at the Entrance Hall desk buys
a laminated Student ID, a branded pint glass ("textbook"), and access to the evening's
curriculum. Returning graduates pay the 5 Sovs Alumni Rate. This beat is unchanged by the
redesign — it's the front door, not the grading apparatus.

### The Curriculum — Four Courses, Chug to Open

The four "courses" are four playable rounds. **Each round opens with the bros chugging a
beer** before the challenge starts — the chugs stack across the sequence, so the party gets
progressively more impaired as the courses get harder. ⚠ AUTHOR-REVIEW: impairment is modeled
as a stacking accuracy/timing penalty on that round's minigame inputs (the toast-off, the
rhythm game, the hazing gauntlet, and beer pong all get harder to execute cleanly by round
four, purely from the chugging — no separate "drunk" status effect is spent on it). Exact
penalty curve pending author balance pass.

**Course 1 — PUB 115: Social Drinking Basics**
- Format: toast-off against Prof. Róisín O'Sullivan (Spirits Department)
- Opens with a chug. Win condition: out-toast her — crowd approval, not a graded score.
- Faculty note: Róisín teaches toasting as foundational etiquette, shot in hand, per her
  established characterization at Trinity [source: `design/worlds/publandia/trinity_of_pints.md`
  L265-272].

**Course 2 — SONG 220: Music Studies**
- Format: rhythm minigame, Irish drinking songs, hosted by Prof. Aisling Byrne (bodhrán in
  hand)
- Opens with a second chug, on top of Course 1's.
- Faculty note: Aisling runs the rhythm/drinking-song track per her established
  characterization [source: `design/worlds/publandia/trinity_of_pints.md` L283-290].

**Course 3 — GREEK 330: Applied Fraternal Traditions**
- Format: hazing gauntlet — a run of stations, each ending in a real fight (a battle
  encounter, not a puzzle), hosted by Prof. Cian MacCarthy (Games & Recreation)
- Opens with a third chug, on top of Courses 1 and 2.
- ⚠ AUTHOR-REVIEW: station count, enemy roster, and fight difficulty curve are drafted, not
  ruled — three stations is the working assumption (matches the gauntlet's Games & Rec host
  and gives the course parity with the others), each a short mob fight themed as a hazing
  "trial" (paddle race, keg-carry brawl, blindfolded pledge tackle). None of this is
  author-approved yet.
- Faculty note: Cian runs Games & Recreation and will not let anyone forget his '08 darts
  championship [source: `design/worlds/publandia/trinity_of_pints.md` L274-281].

**Course 4 — THESIS DEFENSE 401**
- Format: beer pong tournament against the school's staff, culminating in **Dean Cathal
  Murphy** as the round's opponent. "Thesis" survives as a name-only joke — you defend your
  thesis across ten cups. There is no grading anywhere in the room.
- Opens with a fourth chug, on top of Courses 1 through 3 — the bros are at their most
  impaired for the hardest round.

### The Dean Cheats — Always Sunny Self-Destruct

Dean Cathal is winning Thesis Defense 401 with a magnetized ball and a hidden under-table
magnet. Overconfident, he winds up a dramatic trick shot, throws too hard — the magnet yanks
the ball down onto the cup rim. Loud, brittle **CRACK**. The cheap plastic ball shatters, a
grey lodestone magnet clatters out, skids across the table, and locks onto the Dean's own
metal belt buckle/ring.

The bros read this as part of the technique. They obliviously applaud the "legendary
high-level technique," cheer, slap his back, and demand he teach them how to "shatter the orb"
on command.

### The Referee-Reveal Beat (dialogue verbatim — author-dictated)

Panicked tournament officials force the win on the bros before Dean Cathal can recover:

> **Referee**, blowing a whistle, waving a red card, shouting over the crowd: "Dean Cathal is
> disqualified! By tournament rule 4B, the challengers win by default!"

Pilsner completely ignores the word "disqualified" — in his mind his aura physically shattered
the Dean's ball on impact.

> **Lord Pilsner**: "Did you see that?! My defense was so solid his ball literally exploded!
> That's a critical block! We broke his ammo!"

When the referee points at the magnets on the table, Pilsner isn't mad — he's inspired.

> **Lord Pilsner**: "Wait... you can put MAGNETS in the ping pong balls?! Dean, you beautiful
> bastard! Chadwick, write this down! We're magnetizing our balls next time we play beer
> pong!"

The Dean's brain breaks — stripped of his title for cheating while Pilsner claims a
mind-toughness KO, celebrates the default win, and fanboys his "tactical magnet placement."

> **Dean Cathal**: "I WAS CHEATING, YOU ABSOLUTE MONKEYS! I WAS TRYING TO HUMILIATE YOU!"

Pilsner smirks, pats his shoulder.

> **Lord Pilsner**: "Hey, no need to be humble, Dean! Game recognizes game. Now hand over the
> bottle opener, or do we have to take our diplomas by force?"

Cathal snaps, calls the professors.

**Canon logic (author's stated rationale, for dev reference — never surfaced in-game, no
narrator device exists to say it):** (1) self-centered logic — Pilsner attributes the win to
his own toughness and luck, never to procedure; (2) anti-hero satire — the scam fails because
the bros are too self-absorbed to notice they were nearly scammed, so the insult never lands;
(3) escalation — the Dean gets zero satisfaction from his own villainy, and being trolled by
oblivious confidence is exactly what drives the rage that triggers the boss fight.

### SECURE THE QUAD — Battle Trigger

Dean Cathal, humiliated and exposed as a fraud in front of the "students" and his own
faculty, grows red-faced, rips off his tweed jacket, grabs his heavy ceremonial brass gavel,
and screams:

> **Dean Cathal**: "NOBODY GRADUATES! SECURE THE QUAD!"

Straight into battle: Dean Cathal + the three professors (Róisín O'Sullivan, Cian MacCarthy,
Aisling Byrne) as a 4-enemy encounter. Full combat spec: `design/worlds/publandia/npcs/
Trinity_Of_Pints/villain_secure_the_quad.md`. The bros succeed without being heroes or great
at any of it — this is not a competence fantasy, it's four extremely drunk tourists
stumbling through a bar fight against a man wielding a gavel.

⚠ AUTHOR-REVIEW: the backhanded compliment Dean Cathal delivers once the fight ends (per the
ruling: "compliment delivered after," dripping in sarcasm/disdain) is drafted, not
author-dictated verbatim. Working line: *"Congratulations. You've beaten a man in his fifties
and three adjuncts who haven't slept properly since the Thesis Defense season started. Do
enjoy telling that story."* Placement: immediately post-battle, before the graduation beat
below.

### Graduation Beat (staging verbatim — author-dictated, addendum 1)

The bros don graduation robes. Podium photo in The Quad with the Dean and the — obliviously
smiling — Trinity Brewmaster, who holds up the bottle opener and the location's signature
beer for the camera.

- **Lord Pilsner** takes a rolled-up "graduation certificate" and gives the Dean rabbit ears.
- **Bradley** is bent over vomiting on the Dean's shoes. The Dean is disgusted.
- **Chadwick** moons the camera under his robes.

The Trinity Brewmaster stamps the passport and hands over the items (opener + Academic
Amber). Full brewmaster profile, including his drafted stamp speech, is in
`design/worlds/publandia/npcs/Trinity_Of_Pints/npc_brendan_nolan.md`.

The Dean mumbles about stupid American tourists. ⚠ AUTHOR-REVIEW: the ruling describes this
beat in prose ("Dean mumbles about stupid American tourists") rather than as an exact quote —
the line above is a direct paraphrase of that description, not verbatim dictated dialogue.
Drafted staging only: > **Dean Cathal**, mumbling: "Stupid American tourists."

### Exit Beat — Security, Blackout, Alley

At the door, the drunk bros are confronted by security. **Security knocks them out** — not
the faculty, per the author's revision to the original beat. The lesson-teaching beatdown
happens during the blackout. Cut to black; sound/text implies a lesson being taught. No
detail is shown.

### Wake-Up — Hungover in the Alley

The bros wake **Hungover** in the alley behind Trinity of Pints. Pounding headache, nausea.
Bradley and Pilsner are groaning on the curb about their stomachs; the sun is too bright.

### The Brenda Call (dialogue verbatim — author-dictated, addendum 6)

**Phone canon (partial — being drawn out in a separate work item; transcribed here, not
extended):** the bros' cellphones were confiscated on arrival in Euromemeia; why is a story
beat the author is filling in elsewhere and is NOT explained anywhere in this file. They share
ONE phone: contacts are pre-programmed (caller ID shows names), it has ICQ messenger, and it
**only works on speakerphone** — there is no privacy on this phone, ever. This file only uses
that canon; it does not extend or design the phone/ICQ system, which belongs to a different
work item.

Brenda is Chadwick's wife. She acts as if she doesn't know she's on speaker. She knows — the
reason for that is landing in the author's other story work and is not explained here or
anywhere in-game.

The phone rings. Caller ID: Brenda.

> **Chadwick** (whispering frantically): "Guys... quiet! It's Brenda!"
>
> **Brenda**: "Chadwick? Are you alone? I've been thinking about you all day..."
>
> **Chadwick**: "Uh- hi honey! Yes! Total signal isolation over here! Just... standing in a
> very quiet academic square!"
>
> **Brenda**: "Good. Because Headmistress Brenda needs to know if her naughty little student
> has been misbehaving in class. Did you get sent to the principal's office?"
>
> **Lord Pilsner**: (gagging silently in the background, making a face)
>
> **Brenda**: "Tell me what you're wearing right now, Chadwick. Are you touching yourself? Put
> your hand down your pants for Headmistress Brenda right now."
>
> **Chadwick** (panicking, eyes darting to Pilsner and Bradley who are shaking with silent
> laughter): "Uhhh-" (making mouth sounds to fake a bad signal) "Honey you're-" (more mouth
> sounds) "breaking up! I'm going into a-" (more distorted mouth sounds) "a tunnel!"
>
> **Brenda**: "Don't you dare make static mouth noises at me, Chadwick. I know you're just-"
>
> **Chadwick**: (increasingly annoying loud mouth-static sounds) "Losing connection!" (sounds)
> (SLAM — hangs up)

The moment the call ends, the Hungover misery is instantly replaced by Pilsner and Bradley
mercilessly tearing into Chadwick:

> **Lord Pilsner**: "Headmistress Brenda, Chadwick? Really? Is your hand down your cargo
> shorts right now, 'naughty student'?"
>
> **Bradley**: "I'm hungover as hell, but watching you sweat through your polo shirt just
> cured my headache. Call her back! I want to hear about your detention. Does she spank you
> with a ruler?"
>
> **Chadwick** (bright red, adjusting his collar): "She was testing the network stability! It
> was a line test!"

This is the last beat of the Trinity of Pints sequence.

---

## Shenanigans

**Stamp / Opener / Beer:** `stamp_shenanigans`, `opener_shenanigans`, `beer_shenanigans` (full
detail in `design/items/brewery_tour/`). Unlike the other three Publandia breweries, this
stamp is the tour's one loss-condition unlock — "Lose 3 scams AND return" [source:
`design/quests/general_quests/brewerytour.md` extraction table; `design/items/brewery_tour/
stamp_shenanigans_item.md`].

### Challenge

⚠ AUTHOR TO DESIGN — Publandia challenges trend drinking games per the master spec; nothing
is designed yet.

---

## Publandia Overview Table

| Slot | Location | Stamp | Opener | Signature Beer |
|---|---|---|---|---|
| 1 | The Blarney Trap | Celtic harp, emerald ink | Celtic knot shamrock, "May Your Glass Never Be Empty" | The Sweet Surrender — Irish Stout, 5.2% ABV, 8 Sovs |
| 2 | The Stoutworks Brewery | Copper still, bronze ink | Copper still shape, "Forged in Flavor" | Vat Master's Reserve — Imperial Stout, 9.5% ABV, 12 Sovs |
| 3 | Trinity of Pints | Scholarly cap, navy ink | Graduation cap w/ tassel, "Summa Cum Lager" | Academic Amber — Irish Red Ale, 4.8% ABV, 9 Sovs |
| 4 | Shenanigans | Wilted clover, faded gold ink | Wilted clover, "Lucky Eventually" | The Fool's Gold — Golden Ale w/ honey, 5.0% ABV, 8 Sovs |

Full stat blocks, PNG specs, and Notes (including salvaged ambient dialogue) live in each
item's own file under `design/items/brewery_tour/`.

---

## Publandia Legendary Hangover — "The Full Irish Experience"

**Unlock:** all 4 Publandia stamps collected.

- **Effect:** +15 to ALL stats for the entire battle
- **Consequence:** inflicts **"Legendary Hungover"** status after the battle ends
- **Legendary Hungover:** -10 all stats for 30 minutes
- **Cure:** Full Irish Breakfast, sleep, or waiting it out
- **Price:** 50 Sovs, repurchasable from any stamped Publandia location
- **Flavor text:** *"Four stamps. Four surrenders. The night of your life has a morning
  after."*

[source: `design/items/brewery_passport_book.md` L237-245; `design/worlds/publandia/
brewery_passport_book.md` L114 for the title text]

### No-Stack Rule

"Legendary Hungover" does not stack — only one instance applies at a time. Multiple
Legendary Hangovers (i.e., using Publandia's alongside another city's) can technically be
consumed together, but it is not recommended. [source: `design/items/brewery_passport_book.md`
L247-251]

### Strategic Use

Best used for boss fights or difficult encounters — including SECURE THE QUAD, if the player
is carrying it by then. Plan for the aftermath; have a cure ready before the buff wears off.

---

## Publandia Selfie Spots — "Photogenic Drinker" Ladder

| Location | Selfie Spot | Standard Photo | Special Variant |
|---|---|---|---|
| The Blarney Trap | Fireplace with shamrocks | — | With Seamus (Regular status) |
| The Stoutworks Brewery | Copper Cathedral | — | With Vat Master (negotiate route) |
| Trinity of Pints | Graduation podium | — | In scholar's robes (post-graduation) |
| Shenanigans | Lucky Spin Wheel | — | "Wise Fool" crown (post-stamp) |

[source: `design/worlds/publandia/brewery_passport_book.md` L327-330 — the corrected/filled
version of the base file's table, including the Trinity "(post-graduation)" qualifier and the
Shenanigans row]

**Mechanics:** find the selfie spot (camera icon marker), interact to take the photo, photo is
added to the passport's selfie gallery. Special variants require the listed condition.

**Full Publandia Selfie Collection Reward — "Photogenic Drinker":**
- Permanent +1 resistance to "Hungover" debuff
- Reduces Hungover duration by 10%
- Stacks with Continental Beer Master

[source: `design/items/brewery_passport_book.md` L302-306; `design/quests/general_quests/
brewerytour.md` L74-75]

---

## The Master's Toast (cross-city — Continental Beer Master achievement)

### Continental Beer Master

**Requirements:** collect ALL 16 stamps across all four cities (4 cities × 4 breweries).

**Reward — Permanent +1 to All Alcohol-Based Items:**
- All HP restoration from beer/alcohol items
- All SP restoration from beer/alcohol items
- All buff durations from beer/alcohol items
- All "chance of" effects from beer/alcohol items (improved by 1%)

**Additional rewards:**
- Title: "Continental Beer Master," displayed on character
- NPCs at breweries/pubs recognize the achievement in dialogue
- 10% discount off all alcohol purchases everywhere
- Unlocks **The Master's Toast**

[source: `design/items/brewery_passport_book.md` L255-273]

### The Master's Toast

- Available only to Continental Beer Masters
- Automatically wins any toast speech challenge
- Grants **"Legendary Craic"** status to the entire party — **+5 all stats, 10 minutes**
  (normalized: the Publandia/`complete` sources say "+all stats" with no number, but the
  design spec's deepest-source rule resolves to the Sinfonia passport doc's specific figure —
  "party-wide 'Legendary Craic' +5 all stats 10 min, 1/day reset midnight" — since it is the
  only source with an actual number attached; both city files now carry the same normalized
  value [source: `docs/superpowers/specs/2026-08-05-brewery-tour-decomposition-design.md`
  Appendix A.2])
- Single use per game day (resets at midnight)

[source: `design/items/brewery_passport_book.md` L275-279; `design/worlds/publandia/
brewery_passport_book.md` L311-315; normalized per `design/items/brewery_passport_book_sinfonia.md`
L278-282 and Appendix A.2 above]

---

## Notes

- Trinity of Pints is the only fully-designed Publandia brewery challenge in this file — the
  other three await author design per the master spec's "Publandia trends drinking games"
  guidance.
- Every ⚠ AUTHOR-REVIEW flag above (course-3 gauntlet detail, the post-battle compliment
  line, impairment-stacking mechanic) is a Claude draft standing in until the author reviews
  it — none of it is canon yet.
- The Brenda-call phone/ICQ system is explicitly out of scope here — this file transcribes
  the ruling's canon lines and nothing more. Do not add new phone mechanics to this file.
