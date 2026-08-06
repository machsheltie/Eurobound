# Brewery Tour — Publandia (City Instance)

**Authority**: `design/quests/general_quests/brewerytour.md` (master spec) wins every conflict.
Item detail (stamps, openers, signature beers) lives in `design/items/brewery_tour/` — this file
holds Publandia's quest-layer instances only.

---

## The Trigger (this city hosts it)

The Brewery Tour does not exist for the player until the bros **order the special beer at The
Blarney Trap** [source: design/quests/general_quests/brewerytour.md, The Trigger; acquisition
location per design/items/brewery_passport_book_complete.md L11]. That order hands over the
Bottle Opener Keychain (`bottle_opener_keychain`), The Blarney Trap's opener
(`opener_blarney_trap`), and the Brewery Tour Passport Book (`brewery_passport_book`). Before
the trigger, NO brewery anywhere hands over stamps, sells special beers, or gives out openers.

## Brewery Overview

| Brewery | Stamp | Opener | Signature Beer |
|---|---|---|---|
| The Blarney Trap | `design/items/brewery_tour/stamp_blarney_trap_item.md` | `opener_blarney_trap_item.md` | `beer_blarney_trap_item.md` (The Sweet Surrender) |
| The Stoutworks Brewery | `stamp_stoutworks_brewery_item.md` | `opener_stoutworks_brewery_item.md` | `beer_stoutworks_brewery_item.md` (Vat Master's Reserve) |
| Trinity of Pints | `stamp_trinity_of_pints_item.md` | `opener_trinity_of_pints_item.md` | `beer_trinity_of_pints_item.md` (Academic Amber) |
| Shenanigans | `stamp_shenanigans_item.md` | `opener_shenanigans_item.md` | `beer_shenanigans_item.md` (The Fool's Gold) |

## Challenges

### The Blarney Trap
⚠ AUTHOR TO DESIGN — Publandia challenges trend drinking games per the master spec; nothing is designed yet.

### The Stoutworks Brewery
⚠ AUTHOR TO DESIGN — Publandia challenges trend drinking games per the master spec; nothing is designed yet.

### Trinity of Pints — AUTHOR-DICTATED (extraction Rulings, Trinity redesign + addenda 1–6)

Grading is DEAD ("we will no longer be grading"). The course FORMAT stays: four playable
rounds, each opened by chugging a beer — stacking impairment as the difficulty curve.

1. **Pub 115 — Social Drinking Basics**: win a toast-off against an NPC. Faculty: Prof.
   Róisín O'Sullivan (Spirits Dept — intro course teaches toasting as foundational etiquette,
   shot in hand).
2. **Song 220 — Music Studies**: rhythm game, Irish drinking songs. Faculty: Prof. Aisling
   Byrne (bodhrán/rhythm/Irish drinking songs).
3. **Greek 330 — Applied Fraternal Traditions**: hazing gauntlet with real fights at each
   station. Faculty: Prof. Cian MacCarthy (Games & Rec).
4. **Thesis Defense 401**: beer pong tournament against the staff — the thesis survives as a
   name-only joke: you defend your thesis across ten cups; no grading anywhere. Opponent:
   Dean Cathal Murphy.

**The Dean cheats and self-destructs:** he's winning with a magnetized ball + hidden
under-table magnet; overconfident, he winds up a dramatic trick shot, throws too hard, the
magnet yanks the ball down onto the cup rim — loud brittle CRACK — the cheap plastic shell
shatters, a grey lodestone magnet clatters out and zips across the table, locking onto the
Dean's own metal belt buckle/ring.

**The referee-reveal beat (dialogue verbatim, author-dictated):** the win is FORCED on the
bros by panicked tournament officials — the ref blows a whistle, waves a red card, shouts
over the crowd "Dean Cathal is disqualified! By tournament rule 4B, the challengers win by
default!" Pilsner completely ignores the word "disqualified" — in his mind his aura
physically shattered the Dean's ball on impact. Pilsner: "Did you see that?! My defense was
so solid his ball literally exploded! That's a critical block! We broke his ammo!" When the
ref points at the magnets on the table, Pilsner isn't mad — he's inspired: "Wait... you can
put MAGNETS in the ping pong balls?! Dean, you beautiful bastard! Chadwick, write this down!
We're magnetizing our balls next time we play beer pong!" Dean Cathal screams "I WAS
CHEATING, YOU ABSOLUTE MONKEYS! I WAS TRYING TO HUMILIATE YOU!" Pilsner smirks, pats his
shoulder: "Hey, no need to be humble, Dean! Game recognizes game. Now hand over the bottle
opener, or do we have to take our diplomas by force?"

**Boss battle (author addendum: BATTLE IS IN):** the Dean — humiliated and exposed as a
fraud in front of the "students" (patrons) and professors — grows red-faced, RIPS OFF his
tweed jacket, grabs his heavy ceremonial brass gavel, and screams "NOBODY GRADUATES! SECURE
THE QUAD!" → battle vs. the Dean + the three professors (backhanded compliment delivered
post-battle). Author note: lets the bros succeed without being heroes or great at any of it.

**Graduation beat:** bros don graduation robes → podium photo with the Dean and the
(obliviously smiling) Brewmaster, who holds up the bottle opener + Academic Amber; Lord
Pilsner takes a rolled-up "graduation certificate" and gives the Dean rabbit ears; Bradley
bent over vomiting on the Dean's shoes (Dean disgusted); Chadwick mooning the camera under
his robes. The Brewmaster stamps the passport and hands over the items; Dean mumbles about
stupid American tourists.

**Exit beat:** at the door the drunk bros are confronted by SECURITY (not the faculty) — cut
to black, sounds/text imply a lesson being taught during the blackout — they wake Hungover
(pounding headache, nausea) in the alley behind Trinity of Pints.

**Secondary event — the Brenda call (immediately after the alley wake-up; dialogue
verbatim, author-dictated).** Phone canon (transcribed, not extended — the phone/ICQ system
doc is the author's other window's to draw): the bros' cellphones were taken on arrival in
Euromemeia; they share ONE phone — contacts pre-programmed (caller ID shows names), has ICQ
messenger, and it ONLY works on speakerphone; there is no privacy on this phone, ever.
Brenda = Chadwick's wife; she acts as if she doesn't know she's on speaker (SHE KNOWS —
reason lands in story work in the author's other window; do not explain it anywhere).

Scene (bros wake Hungover in the alley, nauseous, dizzy; Bradley + Pilsner groaning on the
curb about their stomachs, sun too bright; phone rings, caller ID: Brenda):
- Chadwick (whispering frantically): "Guys... quiet! It's Brenda!"
- Brenda: "Chadwick? Are you alone? I've been thinking about you all day..."
- Chadwick: "Uh- hi honey! Yes! Total signal isolation over here! Just... standing in a very
  quiet academic square!"
- Brenda: "Good. Because Headmistress Brenda needs to know if her naughty little student has
  been misbehaving in class. Did you get sent to the principal's office?"
- Lord Pilsner: (gagging silently in the background, making a face)
- Brenda: "Tell me what you're wearing right now, Chadwick. Are you touching yourself? Put
  your hand down your pants for Headmistress Brenda right now."
- Chadwick (panicking, eyes darting to Pilsner and Bradley who are shaking with silent
  laughter): "Uhhh-" (making mouth sounds to fake a bad signal) "Honey you're-" (more mouth
  sounds) "breaking up! I'm going into a-" (more distorted mouth sounds) "a tunnel!"
- Brenda: "Don't you dare make static mouth noises at me, Chadwick. I know you're just-"
- Chadwick: (increasingly annoying loud mouth-static sounds) "Losing connection!" (sounds)
  (SLAM — hangs up)

The moment the call ends, the Hungover misery is instantly replaced by Pilsner and Bradley
mercilessly tearing into Chadwick:
- Lord Pilsner: "Headmistress Brenda, Chadwick? Really? Is your hand down your cargo shorts
  right now, 'naughty student'?"
- Bradley: "I'm hungover as hell, but watching you sweat through your polo shirt just cured
  my headache. Call her back! I want to hear about your detention. Does she spank you with a
  ruler?"
- Chadwick (bright red, adjusting his collar): "She was testing the network stability! It
  was a line test!"

**Dev notes (author's stated canon logic — cite, do not soften):** (1) self-centered logic —
Pilsner attributes the win to his own toughness/luck, never procedure; (2) anti-hero satire —
the scam fails because the bros are too self-absorbed to notice being scammed, so the insult
never lands; (3) escalation — the Dean gets ZERO satisfaction from his villainy; being
trolled by oblivious confidence drives the rage that triggers the boss fight.

**Pending NPC drafts (Rulings addendum 5):** the tournament REFEREE (whistle, red card, rule
4B call, reluctantly presents the rigged ball) and the Trinity BREWMASTER (stamps the
passport, obliviously smiling in the graduation selfie holding the opener + Academic Amber)
— Claude drafts both as full NPC-template profiles, ⚠ AUTHOR-REVIEW flagged, for author
approval before they enter canon. Trinity's stamp animation + stamp speech (Gaps #10/#12)
route through the Brewmaster draft.

**Files affected beyond this one:** `design/worlds/publandia/trinity_of_pints.md` (existing
structure largely stands, grading removed — per Rulings addendum 1).

### Shenanigans
⚠ AUTHOR TO DESIGN — Publandia challenges trend drinking games per the master spec; nothing is designed yet.

---

## Legendary Hangover — "The Full Irish Experience"

[source: design/items/brewery_passport_book.md L237-245]
- **Unlock**: All 4 Publandia stamps
- **Effect**: +15 to ALL stats for entire battle
- **Consequence**: "Legendary Hungover" status after battle
- **Legendary Hungover**: -10 all stats for 30 minutes
- **Cure**: Full Irish Breakfast, sleep, or waiting
- **Price**: 50 Sovs (repurchasable from any stamped Publandia location)
- **Flavor**: "Four stamps. Four surrenders. The night of your life has a morning after."

**Strategic use** [source: design/items/brewery_passport_book.md L247-253]:
- Best used for boss fights or difficult encounters
- Plan for the aftermath (have cure ready)
- Multiple Legendary Hangovers can be stacked (not recommended)
- "Legendary Hungover" does not stack (one instance at a time)

---

## Selfie Spots (Brewery Tour)

[source: design/items/brewery_passport_book.md L289-294; rows 3–4 completed per
design/worlds/publandia/brewery_passport_book.md L329-330]

| Location | Selfie Spot | Special Variant |
|---|---|---|
| The Blarney Trap | Fireplace with shamrocks | With Seamus (Regular status) |
| The Stoutworks Brewery | Copper Cathedral | With Vat Master (negotiate route) |
| Trinity of Pints | Graduation podium | In scholar's robes (post-graduation) |
| Shenanigans | Lucky Spin Wheel | "Wise Fool" crown (post-stamp) |

**Selfie mechanics** [source: design/items/brewery_passport_book.md L296-300]: find the
selfie spot (camera icon), interact to take photo, photo added to the passport's selfie
gallery (the bros' scrapbook — Chadwick posts to his feed, #EuroboundMoments, per the master
spec); special variants for completing certain conditions.

**Full selfie collection reward — "Photogenic Drinker"** [source:
design/items/brewery_passport_book.md L303-307]:
- Passive +1 resistance to "Hungover" debuff permanently
- Reduces Hungover duration by 10%
- Stacks with Continental Beer Master for maximum efficiency

---

## Continental Rewards Touchpoint — The Master's Toast

[source: design/items/brewery_passport_book_sinfonia.md L278-282 (deepest source);
design/items/brewery_passport_book.md L275-279]
- Available only to Continental Beer Masters (all 16 stamps)
- Automatically wins any toast speech challenge
- Grants "Legendary Craic" status to entire party (+5 all stats, 10 min)
- Single use per game day (resets at midnight)
