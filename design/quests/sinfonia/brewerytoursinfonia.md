# Brewery Tour — Sinfonia Instance

**Authority:** `design/quests/general_quests/brewerytour.md` is the master spec and wins every
conflict. This file holds Sinfonia's four brewery instances and Sinfonia's city-completion
systems (hangover, selfies, cross-city Master's Toast), built from EXISTING content only —
no new mechanics are introduced in this pass.

Item-level detail (stamp/opener/beer stat blocks, PNG specs) lives in each collectible's own
file under `design/items/brewery_tour/` — this file does not duplicate it beyond a short
pointer table.

**Dead mechanics excluded from this file:** per-location opener vendors and their Sovs
prices ("OR purchase for N Sovs" on every opener), the per-city single-opener model, and the
"Sinfonia Sommelier" achievement tied to buying openers — all superseded by the master
spec's earned-per-brewery opener model. Openers are earned through each brewery's challenge,
never bought.

---

## Sinfonia Overview Table

| Slot | Location | Stamp | Opener | Signature Beer |
|---|---|---|---|---|
| 1 | The Moderato Pub | Metronome over stein, warm amber ink | Metronome shape, "Tempo Is Everything" | Tempo Tantrum — amber ale, 5.5% ABV, 6 Sovs |
| 2 | The Standing Ovation | Comedy/tragedy masks, crimson/gold ink | Theater masks, "Bravo!" | Curtain Call Copper — Sinfonian copper lager, 5.8% ABV, 8 Sovs |
| 3 | Crown & Cask | Habsburg crown on barrel, royal purple ink | Miniature crown, "By Royal Appointment" | Heir Apparent Ale — Belgian-style golden ale, 6.5% ABV, 10 Sovs |
| 4 | The Dancing Stein | Stein with dancing legs, ballroom gold ink | Stein silhouette, "One-Two-Three" | Waltz Weizen — Bavarian wheat beer, 5.2% ABV, 7 Sovs |

Full stat blocks, PNG specs, and Notes live in each item's own file under
`design/items/brewery_tour/`. Prices below the old 8–15 Sovs guideline band (Tempo Tantrum 6,
Waltz Weizen 7) are RULED — the band demotes to a soft guideline, no renumbering [source:
extraction Rulings, Contradiction 3].

### Brewery Tour Difficulty Progression (cross-city)

| City | Challenge Type | Complexity | Failure Consequence |
|------|---------------|------------|---------------------|
| Publandia | Social/Physical | Easy-Medium | Retry available, mild penalties |
| Debaucheryville | Puzzle/Combat | Medium-Hard | Boss fights required |
| Sinfonia | Performance/Social | Medium | Retry with purchase, social penalties |
| Shamsterdam | TBD | TBD | TBD |

[source: design/items/brewery_passport_book_sinfonia.md L369-374 — this is a cross-city
summary table, homed here because the Sinfonia passport doc is its deepest/only source
(Appendix A.2); transcribed verbatim, all four rows. ⚠ AUTHOR-REVIEW: "Retry with purchase"
(Sinfonia row) and "Retry available" (Publandia row) predate the earned-not-bought opener
ruling and were never reconciled against it — this table describes retrying a *challenge*,
not buying an opener or stamp, so it is transcribed as-is rather than assumed dead; flagging
for author confirmation that challenge-retry-for-Sovs is still live alongside the
earned-opener model. Shamsterdam row retained as TBD per its own out-of-scope status this
round.]

---

## The Moderato Pub

**Stamp / Opener / Beer:** `stamp_moderato_pub`, `opener_moderato_pub`, `beer_moderato_pub`.

**Stamper NPC:** Herr Takt. Stamp speech: *"You argued! You defended! You probably changed
no minds! But you PARTICIPATED! That's what matters here. *stamp* Welcome to the debate,
forever."* [source: `design/items/brewery_passport_book_sinfonia.md` L135]

### Challenge — "Win a Tempo Debate"

⚠ AUTHOR TO DESIGN — Sinfonia challenges trend performance/social per the master spec;
nothing is designed yet. Existing one-liner: win a Tempo Debate [source:
`design/items/brewery_passport_book_sinfonia.md` L118].

---

## The Standing Ovation

**Stamp / Opener / Beer:** `stamp_standing_ovation`, `opener_standing_ovation`,
`beer_standing_ovation`.

**Stamper NPC:** Herr Dramatisch. Stamp speech: *"You have PERFORMED! You have TOASTED! You
have DRUNK! Let the record show: you earned this standing ovation. *stamps with flourish*
BRAVO!"* [source: `design/items/brewery_passport_book_sinfonia.md` L142]

### Challenge — "Complete the Bravo Challenge (toast performance)"

⚠ AUTHOR TO DESIGN — Sinfonia challenges trend performance/social per the master spec;
nothing is designed yet. Existing one-liner: complete the Bravo Challenge, a toast
performance [source: `design/items/brewery_passport_book_sinfonia.md` L119].

---

## Crown & Cask

**Stamp / Opener / Beer:** `stamp_crown_and_cask`, `opener_crown_and_cask`,
`beer_crown_and_cask`.

**Stamper NPC:** König Klaus. Stamp speech: *"By the power vested in me by my grandfather,
who vested it in himself, I hereby STAMP thee! Rise, Knight of the Cask! Your liver serves
the crown!"* [source: `design/items/brewery_passport_book_sinfonia.md` L149]

### Challenge — "Complete the Coronation Ceremony (knighting ritual)"

⚠ AUTHOR TO DESIGN — Sinfonia challenges trend performance/social per the master spec;
nothing is designed yet. Existing one-liner: complete the Coronation Ceremony, a knighting
ritual [source: `design/items/brewery_passport_book_sinfonia.md` L120].

---

## The Dancing Stein

**Stamp / Opener / Beer:** `stamp_dancing_stein`, `opener_dancing_stein`,
`beer_dancing_stein`.

**Stamper NPC:** Herr Drehmeister. Stamp speech: *"You waltzed! You carried! You barely
spilled! *stamp in rhythm* ONE-two-three, ONE-two-three, STAMPED! Welcome to the dancers,
friend!"* [source: `design/items/brewery_passport_book_sinfonia.md` L156]

### Challenge — "Complete the Stein Waltz (dance without spilling)"

⚠ AUTHOR TO DESIGN — Sinfonia challenges trend performance/social per the master spec;
nothing is designed yet. Existing one-liner: complete the Stein Waltz, dancing without
spilling [source: `design/items/brewery_passport_book_sinfonia.md` L121].

---

## Sinfonia Legendary Hangover — "The Imperial Concerto"

**Unlock:** all 4 Sinfonia stamps collected.

- **Effect:** +18 to ALL stats for the entire battle, plus Embarrassment immunity during the
  battle
- **Consequence:** inflicts **"Imperial Hangover"** status after the battle ends
- **Imperial Hangover effects:**
  1. -12 all stats for 40 minutes
  2. All dialogue options become "overly formal" (comedic)
  3. Character randomly bows to NPCs
  4. Classical music plays faintly (only the afflicted character can hear it)
- **Cure:** strong coffee (Grounds For Concern), sleep, or a 40-minute wait
- **Price:** 60 Sovs, repurchasable from any stamped Sinfonia location
- **Flavor text:** *"Four stamps. Four performances. Four ceremonies. You drank like royalty.
  Now you suffer like royalty. With dignity. And regret."*

[source: `design/items/brewery_passport_book_sinfonia.md` L208-221]

### Strategic Use

- Balanced between Publandia's +15 and Debaucheryville's +20
- The Embarrassment immunity is useful specifically for social-combat bosses
- Shorter recovery than Debaucheryville's Neon Nightmare (40 min vs 45 min)
- Post-battle effects are comedic but manageable — best saved for a major Sinfonia
  set-piece fight

[source: `design/items/brewery_passport_book_sinfonia.md` L223-228]

---

## Sinfonia Selfie Spots — "Culturally Distinguished" Badge

| Location | Selfie Spot | Standard Photo | Special Variant |
|---|---|---|---|
| The Moderato Pub | Main bar with metronome collection | With tempo chalkboard | With Herr Takt (after winning debate) |
| The Standing Ovation | On stage with spotlight | Mid-toast pose | With confetti falling (perfect performance) |
| Crown & Cask | The Throne | With crown visible | Mid-coronation (ceremony completion) |
| The Dancing Stein | Center dance floor | Mid-waltz with beer | Perfect Stein Waltz (not a drop spilled) |

[source: `design/items/brewery_passport_book_sinfonia.md` L232-239]

**Full Sinfonia Selfie Collection Reward — "Culturally Distinguished":**
- Badge: "Culturally Distinguished"
- +5% resistance to "Embarrassed" status, permanently
- NPCs in Sinfonia occasionally recognize the player with respectful nods

[source: `design/items/brewery_passport_book_sinfonia.md` L241-244] — this is a separate,
Sinfonia-specific reward from the game-wide "Photogenic Drinker" (Publandia's selfie reward);
the two do not overlap or stack against each other.

---

## The Master's Toast (cross-city — Continental Beer Master achievement)

### Continental Beer Master

**Requirements:** collect ALL stamps from ALL cities (16 base game, 4 cities × 4 breweries).

**Rewards:**
- Title: "Continental Beer Master," displayed on character
- Permanent buff: +1 to all alcohol-based item effects
- 10% discount off all alcohol purchases everywhere
- Unlocks **The Master's Toast**
- NPCs at all breweries/pubs recognize the achievement with special dialogue

[source: `design/items/brewery_passport_book_sinfonia.md` L264-276]

### The Master's Toast

- Available only to Continental Beer Masters
- Automatically wins any toast speech challenge
- Grants **"Legendary Craic"** status to the entire party — **+5 all stats, 10 minutes**
  (this is the deepest-sourced figure repo-wide — the Sinfonia passport doc is the only
  source with a specific number attached, per the design spec's deepest-source rule; the
  Publandia city file's Master's Toast entry is normalized to match this same value)
- Single use per game day (resets at midnight)

[source: `design/items/brewery_passport_book_sinfonia.md` L278-282; confirmed as the
authoritative figure by `docs/superpowers/specs/2026-08-05-brewery-tour-decomposition-design.md`
Appendix A.2 ("The Master's Toast full detail (auto-wins toasts, party-wide 'Legendary
Craic' +5 all stats 10 min, 1/day reset midnight)")]

---

## Notes

- All four Sinfonia challenges are unbuilt beyond their one-liner triggers — every Challenge
  section above is flagged `⚠ AUTHOR TO DESIGN` per the brief, and none should be treated as
  ready for implementation.
- The "Key Collector" / "Sinfonia Sommelier" opener-collecting achievements from the legacy
  Sinfonia passport doc are DEAD — redundant under the earned-opener model and ruled dead
  game-wide [source: extraction Rulings, Salvage 28].
- The +5% "Embarrassed" resistance in this file belongs solely to the "Culturally
  Distinguished" selfie badge — there is no duplicate achievement-based grant of it anywhere
  in Sinfonia (parallel to the Debaucheryville ruling on the +5% Confused resistance,
  Contradiction 4).
