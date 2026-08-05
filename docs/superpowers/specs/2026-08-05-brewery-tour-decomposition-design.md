# Brewery Tour Decomposition — Design Spec (2026-08-05)

**Status:** author-approved design (brainstorm round 2026-08-05). Canonical system authority
remains `design/quests/general_quests/brewerytour.md` (master spec, author-ruled 2026-08-04);
this document specifies how its decomposition round executes. Where this spec and the master
spec disagree, the master spec wins.

**Scope:** the three named cities only (Publandia, Debaucheryville, Sinfonia — 12 breweries).
The Shamsterdam quarter is **skipped entirely by author ruling** until its 4 brewery names
are minted; its 12 item files are a fast follow-on mini-round using the same templates. No
placeholder stubs.

**No `game/` changes this round** — design-tree work only, so no boot/GUT gate. The engine
brewery tracker (`brewery_tracker_full.json`, rebuilt from author canon) is the roster
cross-check, not a modification target.

---

## 1. Target architecture

### New files

| Path | Content |
|---|---|
| `design/items/brewery_tour/stamp_<brewery>_item.md` ×12 | Stamp: visual design, ink color, animation, stamp speech, unlock (= challenge completion), PNG spec |
| `design/items/brewery_tour/opener_<brewery>_item.md` ×12 | Opener: design, inscription, material gag, earned-on-completion rule, PNG spec |
| `design/items/brewery_tour/beer_<brewery>_item.md` ×12 | Signature beer: style, ABV, HP/SP effects, buff/debuff risk, price in Sovs, flavor text, "Brewed By", special quirk, PNG spec |
| `design/items/brewery_passport_book_item.md` | The book as an item: acquisition (trigger grant), menu-tab UI + the base file's ASCII mockups, stamp-slot pages, selfie gallery/scrapbook framing, account-level persistence rule, book/UI PNG specs |
| `design/templates/stamp_item_template.md` | Compact skeleton (author-approved before any stamp file is written) |
| `design/templates/opener_item_template.md` | Compact skeleton (same gate) |
| `design/templates/signature_beer_item_template.md` | Compact skeleton (same gate) |
| `design/quests/publandia/brewerytourpublandia.md` | City instance: existing Publandia content only (hangover block, selfie spots, city mechanics); challenges marked AUTHOR TO DESIGN |
| `design/quests/sinfonia/brewerytoursinfonia.md` | Same for Sinfonia |

### Modified files

| Path | Change |
|---|---|
| `design/items/bottle_opener_keychain_item.md` | Geography rewrite: 12→16 count; purchase→trigger grant (handed over with the Publandia special-beer order); real-world references (Cancún, Daytona, Munich, Belgium, Germany/Czech Republic, Señor Frog's, Pilsner Urquell, Oktoberfest) replaced with parody equivalents **minted by the author in the gap interview** |
| `design/quests/debaucheryville/brewerytourdebaucheryville.md` | Aligned to master spec (dead mechanics out, surviving quest-layer content kept/restored) |
| `design/quests/general_quests/brewerytour.md` | Gains pointers to the item files + city files; stays the system authority |
| `docs/superpowers/NEXT_WORK.md` | Rulings + completion recorded as they land |

### Retired files (phase 5 only, after the coverage matrix passes)

The six legacy docs + the stray copy move (never rm) to `design/legacy/` with a SUPERSEDED
banner naming their successors: `brewery_passport_book.md`, `brewery_passport_book_complete.md`,
`brewery_passport_book_debaucheryville.md`, `brewery_passport_book_sinfonia.md`,
`brewery_tour_bottle_opener_system.md` (all in `design/items/`), and
`design/worlds/publandia/brewery_passport_book.md` (deep-diff against the base file first —
if it is a strict subset it retires with the rest; any unique content gets a home first).

### Brewery roster (12, cross-checked against the engine tracker)

- **Publandia:** The Blarney Trap, The Stoutworks Brewery, Trinity of Pints, + the 4th named
  in the city file (extraction confirms; the opener doc's gatekeeper roster suggests
  Shenanigans — verify, don't assume).
- **Debaucheryville:** The Absinthium Taproom, Three-Crown Keg Haus, The Tap Dat Vault,
  Ye Olde B.R.E.W. Lab.
- **Sinfonia:** The Standing Ovation, Crown & Cask, The Dancing Stein, The Moderato Pub.

Item-file slugs use the brewery's snake_case short name (e.g. `stamp_tap_dat_vault_item.md`);
engine IDs (e.g. `debaucheryville_clocktower_tapdatvault_brewery_02`) are recorded inside
each file, not in the filename.

---

## 2. Extraction rules (phase 1)

One pass over all seven sources builds a per-brewery × per-field extraction table committed
as a working artifact (scratch location fine; the FINDINGS — gap manifest + contradiction
list — go in the plan execution notes and the ledger).

- **Master spec wins** every conflict it speaks to.
- Where the master spec is silent, the **deepest source version wins**. The analyst reports
  (Appendix A) already establish who is deepest per layer: base file for system/UI/stamp
  mechanics; city passport files for hangover blocks, selfie spots, beer Risk/Flavor/Special
  fields and city PNG specs; opener-system doc for opener fields and the only Publandia beer
  stats; `complete` for stamp speeches/ink/animations (Deb/Sin) and detailed beer tables.
- **Dead mechanics are excluded at extraction** (ruled 2026-08-04; do not relitigate):
  per-location opener vendors and their prices, ICQ opener sales, the one-keychain-gates-all
  model, the per-city-opener model + cross-city barter, the prerequisite/gating chain
  ("Golden Rule"), Shamsterdam-hangover-as-passive.
- **Void contradictions dropped silently:** Shamsterdam 6-stamp model (16-brewery ruling),
  passport slot order (visit order ruled unimportant), all totals other than 16.
- **Live contradictions go to the author, never resolved by invention.** Known members:
  Trinity of Pints unlock ("any drinking course" vs "Senior Thesis"); Iron Gut Tripel debuff
  duration (unbounded vs next-turn); beer price band (15-Sov cap vs 18-Sov Blockchain Bock).
  Extraction may add members.
- **Naming fix applied on sight:** `dutch_courage_passive.png` → Canal Courage naming (and
  Canal Courage is a CONSUMABLE, per ruling).

## 3. Gap interview (phase 2 — author, one item at a time)

Extraction produces the definitive gap manifest. Known members going in:

- All four Publandia stamp designs (ink, speech, animation — missing from every source).
- The Fool's Gold stat block (name exists, no stats anywhere).
- Keychain replacement gags (the parody stand-ins for the real-world references).
- **Salvage pile:** the 28 gatekeeper NPC quotes (attached to the dead gating mechanic —
  salvage as ambient flavor or let die?); the "Key Collector" achievement (absent from the
  master spec's rewards ladder — revive or dead?).
- The live contradictions from phase 1.

Interview format: one question per message, options presented where they exist, every ruling
recorded in the ledger immediately. **No file writing happens until the interview is done.**

## 4. Writing (phase 3) and quest-doc reconciliation (phase 4)

- The three skeletons are presented for author approval FIRST; on approval they are committed
  to `design/templates/` and all 38 files (36 collectibles + keychain rewrite + passport
  book) are written from the extraction table + interview answers. Fields the interview left
  unresolved (if any) carry an explicit ⚠ AUTHOR TO WRITE marker — never silent invention.
- Quest-layer content that survived the rulings is placed per the master spec's separation
  ("quest mechanics live HERE and in the per-city quest files — not in item docs"):
  the selfie system (Debaucheryville props, Brewery Bro Safari, Photogenic Drinker),
  Y2K Brewery Bingo + Y2K Archaeologist, Peak Y2K Tourist (opener upgrade: MIDI Hamster
  Dance), Bravado/midnight/time-gated access rules, The Master's Toast (full mechanics from
  the city files, not `complete`'s bare bullet), Legendary Hangover full blocks (effects,
  consequences, cures, repurchase source — consumable model).
- An ICQ **fake-opener scam gag** is fair game per the master spec, but writing one is new
  content → only if the author asks for it in the interview.

## 5. Verification & retirement (phase 5)

- **Coverage matrix:** every unique fact itemized in Appendix A is ticked against its new
  home (file + section) or an explicit author kill. No unticked rows → retirement proceeds.
- **Sweeps that can actually fail:** greps over the new files for real-place names
  (Cancún|Daytona|Munich|Belgium|Germany|Czech|Oktoberfest|Señor Frog|Pilsner Urquell|
  Amsterdam etc.), dead-mechanic vocabulary (opener vendor, ICQ opener sale, prerequisite
  chain), stale counts (\b12 breweries|14 stamps|18 stamps), and euro/koruna glyphs.
  Each grep is verified against a planted positive before trusting its silence.
- Legacy docs move to `design/legacy/` with SUPERSEDED banners (git mv, never rm — Windows
  case-ambiguity rule). Ledger updated; master spec's "Source Reconciliation" section flipped
  from "deferred" to "done" with the retirement date.

---

## Appendix A — Recovered merge map (the five analyst reports, 2026-08-04)

Recovered verbatim-in-substance from the 2026-08-04 session archive (they were never
committed; this appendix is now the durable copy). File paths predate nothing — all seven
sources still exist at the paths in §1.

### A.1 Opener-system doc vs `complete`

Only in the opener doc: the gating layer ("Golden Rule", ASCII prerequisite chain, per-opener
Prerequisite fields, City Prerequisite notes) — DEAD by ruling but listed for coverage; 28
NPC gatekeeper quotes (With/Without opener) for 14 locations — Fiona, Dean Cathal, Mickey,
Dr. Vaněk, Glitching Bouncer, Scanner, Herr Takt/Dramatisch/Drehmeister, König Klaus,
Hendrik, Kees — plus "Seamus's Pitch" (salvage-pile decision); per-opener Stamp Unlock +
Signature Beer stat lines — the ONLY place Publandia beer stats exist (The Sweet Surrender
+35 HP/+10% Bravado retention; Vat Master's Reserve; Academic Amber; The Fool's Gold);
"COMPLETE OPENER REFERENCE" — the only 14-row master table (design/inscription/price/earn
method — prices dead, designs live). Only in `complete`: the passport item itself
(acquisition, Seamus's intro monologue, menu-interface framing); City Pages (stamp slot
tables, ink colors, page themes, stamp animations, NPC stamp speeches — Deb/Sin/Sham only,
Publandia missing); detailed beers (style, ABV, Sovs, flavor, "Brewed By" — Publandia
omitted); Shamsterdam selfie spots + "Spinning & Bowing" badge; Legendary Hangover
Comparison (adds Duration); 38 PNG assets with dimensions. Depth: opener doc wins on
openers (e.g. Ye Olde B.R.E.W. Lab: adds vendor, Scanner's two-state dialogue, stamp
condition "+ defeat BrewBot (or bypass)", beer stats); `complete` wins on beers/stamps.
Contradictions: Trinity of Pints "any drinking course" vs "Senior Thesis"; keychain
15-Sov + book-required vs no keychain at all; Publandia "3 more openers" vs "(4 Total)";
Iron Gut Tripel "-10% Accuracy" unbounded vs "next turn"; Shenanigans/Keg Haus/Dancing
Stein condition qualifiers ("awarded by Mickey", "without waking patrons", "any
difficulty") present in opener doc, absent in `complete`; `dutch_courage_passive.png` vs
"Canal Courage".

### A.2 Sinfonia passport vs `complete`

A-only: city-level openers incl. designs/inscriptions (Publandia shamrock; Debaucheryville
UV-reactive "Reality Is Optional After Dark"; Sinfonia eighth-note-with-crown "Drink in
Three-Quarter Time", chime/tiny-bell) — model dead, design gags salvageable; Cross-City
Mechanics section incl. **"Key Collector" achievement**; Full Brewery Tour Summary incl. the
Difficulty Progression table (Sinfonia = Performance/Social, Medium, "Retry with purchase,
social penalties"); Sinfonia Selfie Spots (4-row table, "Culturally Distinguished" badge,
+5% Embarrassed resistance, NPC nods); The Master's Toast full detail (auto-wins toasts,
party-wide "Legendary Craic" +5 all stats 10 min, 1/day reset midnight); all Sinfonia stamp/
beer/page PNG specs (four 64x64x4 animation sheets; `passport_page_sinfonia.png` 256x384;
`legendary_hangover_sinfonia.png`); Publandia penalty status name "Legendary Hungover".
Shallower in `complete`: Imperial Concerto (A: unlock, "Imperial Hangover" status, 4 comedic
effects — formal dialogue, random bowing, inaudible classical music — cure at Grounds For
Concern/sleep/40 min, 60 Sovs repurchase, strategy vs Maestro Vice von Strauss/Baroness;
B: one table line); Sinfonia beer Special fields (crown glass you keep +3 Sovs; foam swirls
clockwise; served with a bow; recipe unchanged since 1848); stamp speeches ("Welcome to the
debate, forever", "*stamps with flourish*", "Rise, Knight of the Cask! Your liver serves
the crown!", "Welcome to the dancers, friend!"); Sommelier's "openers combine into
decorative keychain display". Contradictions: totals 18 vs 14 (void — 16 ruled); opener
model (dead); asset renames `bottle_opener_moderato_pub/standing_ovation/crown_cask/
dancing_stein.png` → `_moderato/_ovation/_crown/_dancing.png` (+`_standing_applause` →
`_ovation_applause`) — pipeline naming decision for the item files.

### A.3 Debaucheryville passport vs `complete`

A-only: the city-opener entry (Shadow Exchange vendor, 20 Sovs OR trade Publandia stamp
proof — the only cross-city barter rule; model dead, gag salvageable); Cross-City Mechanics
+ Key Collector; Debaucheryville Selfie Spots (4 spots, standard + special variants, "Neon
Photogenic" badge); Neon Nightmare full detail (10% input-control reversal, glitch screen
flicker, NPC comments, cure meal/sleep/45 min, 75-Sov repurchase from any stamped location,
Strategic Use block); Master's Toast mechanics; ALL Debaucheryville stamp/beer/page PNG
specs (8 stamp incl. four 64x64x4 animation sequences, 8 beer 32x64+32x32,
`passport_page_debaucheryville.png` 256x384, `legendary_hangover_debaucheryville.png`
48x48). Shallower in B: beers 9 fields vs 6 — B strips Risk, Flavor Text, Special from all
four; lost MECHANICS: Iron Gut Tripel 2-Sov goblet deposit; Blockchain Bock live menu-price
re-roll + negative-Sovs crash risk; Absinthe Lager "only beer that debuffs the user by
design"; Vape Stout vapor-cloud consumption animation; Robotic Bartender's "Welcome to the
Brewvolution™" truncated. Contradictions: Shamsterdam 6 vs 2 stamps (void); totals (void);
+5% Confused resistance sourced from selfie set vs opener Collector achievement (interview);
"Legendary Hungover" status name dropped in B.

### A.4 Base passport vs `complete`

A-only: entire Menu Integration section (pause-menu tab spec, hop-leaf bookmark icon,
notification badge, all three ASCII mockups — Book Closed w/ progress bar, City Selection
spread, Stamp Detail View incl. "Acquired: Won Pint-Off / Day 3, 9:47 PM" + selfie row);
entire Stamp Mechanics section (four unlock archetypes Challenge/Completion/Status/
Discovery, 6-step collection process, Stamp Permanence: non-tradeable, **persist across
save files, tied to account not save**, timestamp); Publandia signature beer stat blocks
(Sweet Surrender 5.2%, +35HP/+10SP, "Comfortable Trap" +10% Bravado retention 1 hr, 5%
Contentment, 8 Sovs; Vat Master's Reserve 9.5%, +40/+15, 10% "Fermented Fury" +15% Atk,
+5% negotiate-route bonus, 12 Sovs; Academic Amber 4.8%, +25/+20, +3 INT 30 min, 10%
"Pretentious", 9 Sovs; The Fool's Gold — no stat block); Beer Stats Template + Unlock
System (global ranges +25–50 HP, +0–20 SP, 5–15% debuff risk, 8–15 Sovs; cross-city/hub
availability); "Using Legendary Hangovers Strategically" (no-stack rule, cure list);
Publandia Brewmaster Selfies (4 spots/variants — Fireplace w/ Seamus, Copper Cathedral w/
Vat Master, graduation podium — 4-step selfie mechanic, "Photogenic Drinker" reward);
Implementation Notes (technical requirements, save-data model, UI/UX priorities); ~40 PNG
specs (Book Assets: closed 128x128, open 512x384, spine 32x384, bookmark 32x64, city pages;
generic Stamp Assets: empty/locked slots, stamp_animation 64x64x4, Publandia stamps;
Publandia beer bottles/icons; Achievement Assets: 4 hangover icons,
continental_beer_master_badge 96x96, photogenic_drinker_badge; all 8 UI Assets).
Shallower in B: Legendary Hangovers one row each (no cures/repurchase/flavor); Master's
Toast bare bullet; Continental Beer Master compressed. Contradictions: totals (void);
Shamsterdam beers *Molen's Midnight/Liquid Courage* vs *Windmill Wit/Oude Genever* + orange
vs gold ink (MOOT until Shamsterdam round; record for the naming interview); reward type
consumable vs passive (ruled: consumable); opener model (ruled); Beer Master requirement
all-stamps vs stamps+openers (spec: all 16 breweries — earning is unified, moot); Trinity
of Pints "Complete drinking lecture" vs "Senior Thesis" (interview); price band 15 cap vs
Blockchain Bock 18 (interview).

### A.5 Quest docs vs item docs

Quest-docs-only systems (all KEEP per master spec, placed in phase 4): Brewmaster Selfie
system (Debaucheryville props "Mystical Absinthe"/"Authentic Dive Bar"/"Tech Bro"/
"Investor"; album at hostel/Wi-Fi café; NPC reactions; Charm bonuses scaled to staging;
"Brewery Bro Safari" compilation; collect-all +1 Hungover resistance); Y2K Brewery Bingo
(8-item card → "Y2K Archaeologist" → +1 Nostalgia Resistance); "Peak Y2K Tourist"
mega-achievement (opener upgrade: MIDI Hamster Dance on use + "Nostalgically Self-Aware"
+2 Charm); access rules (Three-Crown +1 Bravado; Tap Dat Vault midnight-only; failed
first-entry Bravado check locks 1 in-game hour; 6-8 PM/midnight/3 AM states); ICQ vendor
prices 40/30/100/500/420/69 Sovs (DEAD with the sales mechanic; fake-opener scam gag may
reuse the joke shape if author wants); micro-dungeon framing (yeast monsters, tour guides);
"add beer to permanent item pool on first completion". Contradictions vs item docs: counts
(void); unlock rule (ruled: hybrid — one keychain container + per-brewery earned openers);
Legendary Hangover versions (ruled: named consumables, city-file depth wins); slot order
(void); opener sellers ICQ vs NPCs (both dead — earned only).

---

## Appendix B — Execution guardrails (project hard rules restated for this round)

Ambiguity escalates to the author, never invention; satire ships at full strength — no
sanitizing while transcribing; SOVS only; deep-diff before ANY legacy file moves; never rm
case-ambiguous paths; verify sweeps with greps that can fail (planted-positive check);
commit early and often (per-phase commits minimum); ledger updated at every ruling.
