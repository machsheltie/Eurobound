# Brewery Decomposition — Extraction Table, Gap Manifest, Contradiction List (Phase 1)

**Status:** working artifact for the brewery-tour decomposition round. Authority: master spec
`design/quests/general_quests/brewerytour.md` wins every conflict it speaks to; where silent,
the deepest source wins per Appendix A of
`docs/superpowers/specs/2026-08-05-brewery-tour-decomposition-design.md`. Dead mechanics
(opener vendors/prices, ICQ opener sales, keychain-gates-all, per-city-opener model + barter,
prerequisite chain, Shamsterdam-hangover-as-passive) are excluded from the table. Shamsterdam
content is out of scope except where flagged for the future naming round (see parking lot).

Sources walked (all seven, cited by short name below):
- `base` = `design/items/brewery_passport_book.md`
- `complete` = `design/items/brewery_passport_book_complete.md`
- `deb_passport` = `design/items/brewery_passport_book_debaucheryville.md`
- `sin_passport` = `design/items/brewery_passport_book_sinfonia.md`
- `opener_doc` = `design/items/brewery_tour_bottle_opener_system.md`
- `master` = `design/quests/general_quests/brewerytour.md`
- `deb_quest` = `design/quests/debaucheryville/brewerytourdebaucheryville.md`

Roster cross-check sources: `worlds_copy` = `design/worlds/publandia/brewery_passport_book.md`;
`tracker` = `game/assets/data/saves/brewery_tracker_full.json`; `shenanigans_world` =
`design/worlds/publandia/shenanigans.md`.

---

## Roster

12 breweries confirmed across three cities. Engine tracker keys use bare slugs (no city
prefix, nested under a city object) — recorded next to each slug below.

- **Publandia:** `blarney_trap`, `stoutworks_brewery`, `trinity_of_pints`, `shenanigans`
  — engine keys `publandia.blarney_trap`, `publandia.stoutworks_brewery`,
  `publandia.trinity_of_pints`, `publandia.shenanigans` [source: game/assets/data/saves/brewery_tracker_full.json L9-14]
- **Debaucheryville:** `absinthium_taproom`, `three_crown_keg_haus`, `tap_dat_vault`,
  `ye_olde_brew_lab` — engine keys `debaucheryville.absinthium_taproom`,
  `debaucheryville.three_crown_keg_haus`, `debaucheryville.tap_dat_vault`,
  `debaucheryville.ye_olde_brew_lab` [source: game/assets/data/saves/brewery_tracker_full.json L3-8]
- **Sinfonia:** `standing_ovation`, `crown_and_cask`, `dancing_stein`, `moderato_pub` —
  engine keys `sinfonia.moderato_pub`, `sinfonia.standing_ovation`, `sinfonia.crown_and_cask`,
  `sinfonia.dancing_stein` [source: game/assets/data/saves/brewery_tracker_full.json L15-20]

### Publandia 4th brewery verdict: CONFIRMED — Shenanigans

Four independent sources agree, none contradict:
1. `complete` city-page table names it directly: "Shenanigans | Wilted clover, faded gold ink |
   The Fool's Gold | Lose 3 scams AND return" [source: design/items/brewery_passport_book_complete.md L231]
2. `opener_doc` gives it a full opener writeup ("Shenanigans Bottle Opener") [source: design/items/brewery_tour_bottle_opener_system.md L91-105]
3. `worlds_copy` (the stray Publandia copy) names it in both the city-page table and the
   ASCII "Page Layout (Complete)" mockup [source: design/worlds/publandia/brewery_passport_book.md L111, L136-138]
4. Engine tracker has a `shenanigans` key under `publandia` [source: game/assets/data/saves/brewery_tracker_full.json L13]
5. The world file `design/worlds/publandia/shenanigans.md` exists, has Location Type
   "...Brewery Tour Stop" and Location ID `publandia_pub_shenanigans_01`, and houses NPC
   Mickey Finnegan (`npcs/Shenanigans/npc_mickey_finnegan.md`) — matching `opener_doc`'s
   gatekeeper "Mickey" for this location [source: design/worlds/publandia/shenanigans.md L1-13]

No gap; not seeded to the manifest. `base` alone leaves this slot `[TBD]` — it is the
shallowest source on Publandia's 4th brewery and is superseded by the four sources above.

---

## Deep-diff verdict: stray copy (`design/worlds/publandia/brewery_passport_book.md`) vs base (`design/items/brewery_passport_book.md`)

**Verdict: NOT a strict subset — unique content found, added to the extraction table below.**

The stray copy is byte-for-byte identical to `base` for the large majority of its content
(System Overview, Menu Integration mockups except one, Stamp Mechanics, Signature Beers intro,
Legendary Hangovers, Continental Beer Master, Brewmaster Selfies intro, Implementation Notes,
PNG Asset Requirements). A direct `diff -U0` between the two files shows exactly **four
hunks**, three of which are pure fill-ins of `base`'s placeholder rows and one of which
modifies existing (non-placeholder) text:

1. **Modifies existing table text, not a pure addition** — the Publandia city-page table's row
   3 (Trinity of Pints) unlock condition changes from `base`'s "Complete drinking lecture"
   [source: design/items/brewery_passport_book.md L110] to "Graduate (complete Senior Thesis)"
   [source: design/worlds/publandia/brewery_passport_book.md L110], in the same hunk as row 4
   ([TBD] placeholders → Shenanigans filled in)
   [source: design/worlds/publandia/brewery_passport_book.md L111]. This is the hunk that
   matters for Contradiction List #1 below: the stray copy does NOT corroborate "Complete
   drinking lecture" — it silently rewrites away from it, onto the "Senior Thesis" variant.
2. **Legendary Hangover line modified + new ASCII mockup added** — the Legendary Hangover line
   gains the "The Full Irish Experience" title text (a modification)
   [source: design/worlds/publandia/brewery_passport_book.md L114], and an entirely new
   "Page Layout (Complete)" ASCII mockup is appended showing the finished 4/4 Publandia page
   with all four stamps, including Shenanigans (a pure addition)
   [source: design/worlds/publandia/brewery_passport_book.md L116-143]. `base` only has the 2/4
   in-progress mockup. Cosmetic/UI reference value only — no new game-mechanical fact beyond
   what hunk 1 already established.
3. **A full stat block for The Fool's Gold (fills a placeholder)** — Style, ABV, Stats, Effect,
   Risk, Price, Flavor, and a "Unique Unlock" note
   [source: design/worlds/publandia/brewery_passport_book.md L256-265], replacing `base`'s
   `[Fourth Beer TBD]` placeholder [source: design/items/brewery_passport_book.md L227-228].
   **This directly contradicts the design spec's Gap Manifest seed "The Fool's Gold stat block
   (name exists, no stats anywhere)"** — stats DO exist, in this one file. Flagged in the
   report; the stat block is pulled into the extraction table below under `shenanigans` since
   master is silent and this is the only source with the full block (deepest-source-wins).
4. **Selfie spot table: one modification + one placeholder fill** — row 3 (Trinity of Pints)
   gains the parenthetical "(post-graduation)" on its existing "In scholar's robes" entry (a
   modification) [source: design/worlds/publandia/brewery_passport_book.md L329], and row 4
   fills `base`'s `[TBD]` placeholders with "Shenanigans | Lucky Spin Wheel | 'Wise Fool' crown
   (post-stamp)" [source: design/worlds/publandia/brewery_passport_book.md L330]. `base`'s
   unmodified row 3 reads "In scholar's robes" with no parenthetical
   [source: design/items/brewery_passport_book.md L293], and its row 4 is `[TBD]`
   [source: design/items/brewery_passport_book.md L294]. Selfie content is quest-layer per the
   master spec's separation rule, not an item-doc field — not added to the extraction table,
   noted here for completeness only.

Per the design spec's retirement rule (§ target architecture, retired files): since it is not a
strict subset, its unique content (item #2 above) must get a home before this file retires in
Task 9 — it now has one (the `shenanigans` beer block below).

---

## Extraction Table

Each brewery block lists `stamp:`, `opener:`, `beer:` fields only (selfie/brewmaster-NPC/
challenge fields are quest-layer per the master spec and out of scope for item docs). Empty
fields are listed as **GAP** and numbered into the Gap Manifest below.

### Publandia

#### blarney_trap
**stamp:**
- visual: Celtic harp [source: design/items/brewery_passport_book.md L108; design/items/brewery_passport_book_complete.md L228]
- ink: emerald [source: design/items/brewery_passport_book.md L108]
- animation: **GAP #1**
- stamper NPC: **GAP #2**
- stamp speech: **GAP #3**
- PNG: implied `stamp_blarney_trap.png` — 64x64 [source: design/items/brewery_passport_book.md L347]

**opener:**
- design: Celtic knot shamrock with bottle opener integrated into stem [source: design/items/brewery_tour_bottle_opener_system.md L41]
- inscription: "May Your Glass Never Be Empty" [source: design/items/brewery_tour_bottle_opener_system.md L43]
- material gag: "Authentic" brass (actually spray-painted zinc) [source: design/items/brewery_tour_bottle_opener_system.md L42]
- special feature: shamrock spins freely on the ring [source: design/items/brewery_tour_bottle_opener_system.md L45]
- PNG: `bottle_opener_blarney_trap.png` 48x48; `bottle_opener_blarney_spin.png` 48x48 [source: design/items/brewery_passport_book_complete.md L452-453]

**beer: The Sweet Surrender**
- style: Irish Stout [source: design/items/brewery_passport_book.md L200]
- ABV: 5.2% [source: design/items/brewery_passport_book.md L201]
- HP/SP: +35 HP, +10 SP [source: design/items/brewery_passport_book.md L202]
- effect: "Comfortable Trap" — +10% Bravado retention (1 hour) [source: design/items/brewery_passport_book.md L203]
- risk: 5% "Contentment" (reduced urgency) [source: design/items/brewery_passport_book.md L204]
- price: 8 Sovs [source: design/items/brewery_passport_book.md L205]
- flavor text: "You surrendered to Blarney Trap pricing. It's delicious." [source: design/items/brewery_passport_book.md L206]
- brewed by: **GAP #4**
- special quirk: **GAP #5**
- PNG: `sweet_surrender_bottle.png` 32x64; `sweet_surrender_icon.png` 32x32 [source: design/items/brewery_passport_book.md L357-358]

#### stoutworks_brewery
**stamp:**
- visual: Copper still [source: design/items/brewery_passport_book.md L109]
- ink: bronze [source: design/items/brewery_passport_book.md L109]
- animation: **GAP #6**
- stamper NPC: **GAP #7**
- stamp speech: **GAP #8**
- PNG: implied `stamp_stoutworks.png` — 64x64 [source: design/items/brewery_passport_book.md L348]

**opener:**
- design: Copper still shape with bottle opener as the spout [source: design/items/brewery_tour_bottle_opener_system.md L58]
- inscription: "Forged in Flavor" [source: design/items/brewery_tour_bottle_opener_system.md L60]
- material gag: copper-plated steel with verde patina accents (fake-aged) [source: design/items/brewery_tour_bottle_opener_system.md L59]
- special feature: hollow center creates whistle sound when swung [source: design/items/brewery_tour_bottle_opener_system.md L62]
- PNG: `bottle_opener_stoutworks.png` 48x48; `bottle_opener_stoutworks_whistle.png` 48x48 [source: design/items/brewery_passport_book_complete.md L454-455]

**beer: Vat Master's Reserve**
- style: Imperial Stout (whiskey barrel aged) [source: design/items/brewery_passport_book.md L209]
- ABV: 9.5% [source: design/items/brewery_passport_book.md L210]
- HP/SP: +40 HP, +15 SP [source: design/items/brewery_passport_book.md L211]
- effect: 10% "Fermented Fury" (+15% Attack next battle) [source: design/items/brewery_passport_book.md L212]
- risk: 10% "The Vat's Whisper" (cosmetic yeast thoughts) [source: design/items/brewery_passport_book.md L213]
- price: 12 Sovs [source: design/items/brewery_passport_book.md L214]
- flavor text: "Aged during the incident. Tastes like existential crisis." [source: design/items/brewery_passport_book.md L215]
- brewed by: **GAP #9**
- special quirk: Negotiate Route Bonus — +5% enemy negotiation success [source: design/items/brewery_passport_book.md L216]
- PNG: `vat_masters_reserve_bottle.png` 32x64; `vat_masters_reserve_icon.png` 32x32 [source: design/items/brewery_passport_book.md L359-360]

#### trinity_of_pints
**stamp:**
- visual: Scholarly cap [source: design/items/brewery_passport_book.md L110]
- ink: navy [source: design/items/brewery_passport_book.md L110]
- animation: **GAP #10**
- stamper NPC: **GAP #11**
- stamp speech: **GAP #12**
- PNG: implied `stamp_trinity_pints.png` — 64x64 [source: design/items/brewery_passport_book.md L349]

**opener:**
- design: Scholarly graduation cap with bottle opener as the tassel [source: design/items/brewery_tour_bottle_opener_system.md L75]
- inscription: "Summa Cum Lager" [source: design/items/brewery_tour_bottle_opener_system.md L77]
- material gag: navy enamel over brass with gold trim (mock academic regalia) [source: design/items/brewery_tour_bottle_opener_system.md L76]
- special feature: tassel actually moves/dangles [source: design/items/brewery_tour_bottle_opener_system.md L80]
- PNG: `bottle_opener_trinity.png` 48x48; `bottle_opener_trinity_tassel.png` 24x24 [source: design/items/brewery_passport_book_complete.md L456-457]

**beer: Academic Amber**
- style: Irish Red Ale [source: design/items/brewery_passport_book.md L219]
- ABV: 4.8% [source: design/items/brewery_passport_book.md L220]
- HP/SP: +25 HP, +20 SP [source: design/items/brewery_passport_book.md L221]
- effect: "Scholar's Focus" — temporary INT boost (+3 for 30 min) [source: design/items/brewery_passport_book.md L222]
- risk: 10% "Pretentious" (dialogue options become insufferable) [source: design/items/brewery_passport_book.md L223]
- price: 9 Sovs [source: design/items/brewery_passport_book.md L224]
- flavor text: "Brewed for minds that think they're smarter when drinking. They're not. But it helps." [source: design/items/brewery_passport_book.md L225]
- brewed by: **GAP #13**
- special quirk: **GAP #14**
- PNG: `academic_amber_bottle.png` 32x64; `academic_amber_icon.png` 32x32 [source: design/items/brewery_passport_book.md L361-362]

#### shenanigans
**stamp:**
- visual: Wilted clover (four-leaf, three leaves drooping) [source: design/items/brewery_passport_book_complete.md L231; design/items/brewery_tour_bottle_opener_system.md L92]
- ink: faded gold [source: design/items/brewery_passport_book_complete.md L231]
- animation: **GAP #15**
- stamper NPC: **GAP #16**
- stamp speech: **GAP #17**
- PNG: **GAP #18** — `base` lists only a generic placeholder `stamp_[fourth_publandia].png` [source: design/items/brewery_passport_book.md L350], never resolved to a real filename anywhere in the seven sources.

**opener:**
- design: wilted four-leaf clover (three leaves drooping) with bottle opener as stem [source: design/items/brewery_tour_bottle_opener_system.md L92]
- inscription: "Lucky Eventually" [source: design/items/brewery_tour_bottle_opener_system.md L94]
- material gag: faded gold-tone metal, intentionally tarnished [source: design/items/brewery_tour_bottle_opener_system.md L93]
- special feature: fourth leaf is detachable (falls off occasionally) [source: design/items/brewery_tour_bottle_opener_system.md L97]
- PNG: `bottle_opener_shenanigans.png` 48x48; `bottle_opener_shenanigans_broken.png` 48x48 [source: design/items/brewery_passport_book_complete.md L458-459]

**beer: The Fool's Gold**
- style: Golden Ale with honey [source: design/worlds/publandia/brewery_passport_book.md L257]
- ABV: 5.0% [source: design/worlds/publandia/brewery_passport_book.md L258]
- HP/SP: +30 HP, +15 SP [source: design/worlds/publandia/brewery_passport_book.md L259; corroborated design/items/brewery_tour_bottle_opener_system.md L104]
- effect: "Learned Optimism" — +10% resistance to scam detection failure [source: design/worlds/publandia/brewery_passport_book.md L260-261]
- risk: 5% "Sentimental" (donate extra gold to NPCs) [source: design/worlds/publandia/brewery_passport_book.md L262]
- price: 8 Sovs [source: design/worlds/publandia/brewery_passport_book.md L263]
- flavor text: "The only honest thing in this entire establishment. Golden, hopeful, with a bitter finish — just like your evening." [source: design/worlds/publandia/brewery_passport_book.md L264]
- brewed by: **GAP #19**
- special quirk: "Unique Unlock: Only stamp earned through LOSING, not winning" [source: design/worlds/publandia/brewery_passport_book.md L265]
- PNG: **GAP #20** — no bottle/icon PNG for this beer in any of the seven sources or the stray copy.

---

### Debaucheryville

#### absinthium_taproom
**stamp:**
- visual: green fairy silhouette trapped inside cracked absinthe glass [source: design/items/brewery_passport_book_complete.md L252]
- ink: shifting emerald (appears to move in certain light) [source: design/items/brewery_passport_book_complete.md L253]
- animation: green mist swirls before stamp lands with ethereal chime [source: design/items/brewery_passport_book_complete.md L255]
- stamper NPC: Dr. Vaněk [source: design/items/brewery_passport_book_complete.md L256]
- stamp speech: "Congratulations. You've seen yourself. The stamp is proof. The memory is punishment." [source: design/items/brewery_passport_book_complete.md L256]
- PNG: `stamp_absinthium_taproom.png` 64x64; `stamp_absinthium_animation.png` 64x64x4 [source: design/items/brewery_passport_book_debaucheryville.md L273, L277]

**opener:**
- design: cracked absinthe glass with Green Fairy silhouette emerging, bottle opener as the glass stem [source: design/items/brewery_tour_bottle_opener_system.md L120]
- inscription: "I Saw Myself" [source: design/items/brewery_tour_bottle_opener_system.md L122]
- material gag: emerald-tinted metal with iridescent "oil slick" finish [source: design/items/brewery_tour_bottle_opener_system.md L121]
- special feature: surface appears to shift colors in different lighting (lenticular effect) [source: design/items/brewery_tour_bottle_opener_system.md L125]
- PNG: `bottle_opener_absinthium.png` 48x48; `bottle_opener_absinthium_shift.png` 48x48 [source: design/items/brewery_passport_book_complete.md L462-463]

**beer: Absinthe Lager**
- style: absinthe-infused lager (legally questionable) [source: design/items/brewery_passport_book_debaucheryville.md L114]
- ABV: 8.5% (plus "additives") [source: design/items/brewery_passport_book_debaucheryville.md L115]
- HP/SP: +15 SP restoration [source: design/items/brewery_passport_book_debaucheryville.md L116]
- effect: 30% chance to apply "Green Fairy Confusion" to the USER [source: design/items/brewery_passport_book_debaucheryville.md L117]
- risk: "The confusion is part of the experience" (self-inflicted by design) [source: design/items/brewery_passport_book_debaucheryville.md L118]
- price: 12 Sovs [source: design/items/brewery_passport_book_debaucheryville.md L119]
- flavor text: "It's not a bug, it's a feature. The disorientation means it's working." — Dr. Vaněk [source: design/items/brewery_passport_book_debaucheryville.md L120]
- brewed by: The Absinthium Taproom (in-house) [source: design/items/brewery_passport_book_debaucheryville.md L121]
- special quirk: only beer that debuffs the user by design [source: design/items/brewery_passport_book_debaucheryville.md L122]
- PNG: `absinthe_lager_bottle.png` 32x64; `absinthe_lager_icon.png` 32x32 [source: design/items/brewery_passport_book_debaucheryville.md L283-284]

#### tap_dat_vault
**stamp:**
- visual: soundwave pattern emerging from vault door shape [source: design/items/brewery_passport_book_complete.md L259]
- ink: electric cyan with hot pink accents [source: design/items/brewery_passport_book_complete.md L260]
- animation: bass drop sound effect, stamp pulses with rhythm before landing [source: design/items/brewery_passport_book_complete.md L262]
- stamper NPC: Strobe Brewmistress [source: design/items/brewery_passport_book_complete.md L263]
- stamp speech: "You... kept... the beat... *glitch* ...drink responsibly... *static* ...or don't..." [source: design/items/brewery_passport_book_complete.md L263]
- PNG: `stamp_tap_dat_vault.png` 64x64; `stamp_tapdatvault_animation.png` 64x64x4 [source: design/items/brewery_passport_book_debaucheryville.md L274, L278]

**opener:**
- design: vault door shape with soundwave pattern cutout, bottle opener integrated into the door handle [source: design/items/brewery_tour_bottle_opener_system.md L137]
- inscription: "Inhaled & Survived" [source: design/items/brewery_tour_bottle_opener_system.md L139]
- material gag: brushed chrome with cyan/hot-pink neon accents that actually glow [source: design/items/brewery_tour_bottle_opener_system.md L138]
- special feature: contains tiny LED that pulses in rhythm when squeezed [source: design/items/brewery_tour_bottle_opener_system.md L142]
- PNG: `bottle_opener_tapdatvault.png` 48x48; `bottle_opener_tapdatvault_glow.png` 48x48 [source: design/items/brewery_passport_book_complete.md L464-465]

**beer: Vape Stout**
- style: vapor-infused experimental stout [source: design/items/brewery_passport_book_debaucheryville.md L125]
- ABV: 6.9% [source: design/items/brewery_passport_book_debaucheryville.md L126]
- HP/SP: +20 SP restoration [source: design/items/brewery_passport_book_debaucheryville.md L127]
- effect: "Glow-Up Aura" (+1 Charm, +1 Defense for 30 min) [source: design/items/brewery_passport_book_debaucheryville.md L128]
- risk: applies "Grease Fingers" status (reduced item accuracy) [source: design/items/brewery_passport_book_debaucheryville.md L129]
- price: 14 Sovs [source: design/items/brewery_passport_book_debaucheryville.md L130]
- flavor text: "We don't serve beer — we inhale it. Your lungs are just another glass." [source: design/items/brewery_passport_book_debaucheryville.md L131]
- brewed by: The Tap Dat Vault (vapor-extraction process) [source: design/items/brewery_passport_book_debaucheryville.md L132]
- special quirk: consumed as vapor cloud animation [source: design/items/brewery_passport_book_debaucheryville.md L133]
- PNG: `vape_stout_bottle.png` 32x64; `vape_stout_icon.png` 32x32 [source: design/items/brewery_passport_book_debaucheryville.md L285-286]

#### three_crown_keg_haus
**stamp:**
- visual: three rusting crowns arranged above a foaming stein [source: design/items/brewery_passport_book_complete.md L266]
- ink: rust orange with faded royal purple accents [source: design/items/brewery_passport_book_complete.md L267]
- animation: regal fanfare (off-key), stamp lands with sticky thud [source: design/items/brewery_passport_book_complete.md L269]
- stamper NPC: Bartender (unnamed) [source: design/items/brewery_passport_book_complete.md L270]
- stamp speech: "You've joined the nobility! We invented beer before hygiene — and look at you, still standing! Mostly!" [source: design/items/brewery_passport_book_complete.md L270]
- PNG: `stamp_three_crown_keghaus.png` 64x64; `stamp_keghaus_animation.png` 64x64x4 [source: design/items/brewery_passport_book_debaucheryville.md L275, L279]

**opener:**
- design: three rusted crowns stacked vertically with bottle opener as the base/throne, miniature stein charm dangles from ring [source: design/items/brewery_tour_bottle_opener_system.md L154]
- inscription: "Noble by Liver" [source: design/items/brewery_tour_bottle_opener_system.md L156]
- material gag: intentionally tarnished brass with rust-orange patina [source: design/items/brewery_tour_bottle_opener_system.md L155]
- special feature: stein charm actually holds 1ml of liquid (decorative) [source: design/items/brewery_tour_bottle_opener_system.md L159]
- PNG: `bottle_opener_keghaus.png` 48x48; `bottle_opener_keghaus_charm.png` 24x24 [source: design/items/brewery_passport_book_complete.md L466-467]

**beer: Iron Gut Tripel**
- style: Slavic-style triple-fermented strong ale [source: design/items/brewery_passport_book_debaucheryville.md L136]
- ABV: 11.5% [source: design/items/brewery_passport_book_debaucheryville.md L137]
- HP/SP: +40 HP restoration [source: design/items/brewery_passport_book_debaucheryville.md L138]
- effect: "Inspired" status (+10 Bravado for 30 min) [source: design/items/brewery_passport_book_debaucheryville.md L139]
- risk: -10% Accuracy next turn (the strength hits hard) [source: design/items/brewery_passport_book_debaucheryville.md L140] — **see Contradiction List #2** (unbounded elsewhere)
- price: 10 Sovs [source: design/items/brewery_passport_book_debaucheryville.md L141]
- flavor text: "300 years of brewing tradition. 0 years of health code compliance. Priorities." [source: design/items/brewery_passport_book_debaucheryville.md L142]
- brewed by: Three-Crown Keg Haus (ancient recipe, questionable equipment) [source: design/items/brewery_passport_book_debaucheryville.md L143]
- special quirk: served in antique goblet (return for 2 Sovs deposit) [source: design/items/brewery_passport_book_debaucheryville.md L144]
- PNG: `iron_gut_tripel_goblet.png` 32x64; `iron_gut_tripel_icon.png` 32x32 [source: design/items/brewery_passport_book_debaucheryville.md L287-288]

#### ye_olde_brew_lab
**stamp:**
- visual: pixelated hop cone with scrolling blockchain hash numbers [source: design/items/brewery_passport_book_complete.md L273]
- ink: neon blue with green circuit traces [source: design/items/brewery_passport_book_complete.md L274]
- animation: digital processing sounds, stamp "downloads" onto page [source: design/items/brewery_passport_book_complete.md L276]
- stamper NPC: BrewBot (if defeated) OR Robotic Bartender (if bypassed) [source: design/items/brewery_passport_book_complete.md L277; design/items/brewery_passport_book_debaucheryville.md L107]
- stamp speech: BrewBot — "Achievement... unlocked... brewery tour... OPTIMIZED... *sparking*" [source: design/items/brewery_passport_book_complete.md L277]; Robotic Bartender — "Congratulations! Your taste profile has been... SYNERGIZED! Welcome to the Brewvolution™!" [source: design/items/brewery_passport_book_debaucheryville.md L107] (deb_passport is the deeper/fuller version — `complete`'s copy truncates before "Welcome to the Brewvolution™")
- PNG: `stamp_brew_lab.png` 64x64; `stamp_brewlab_animation.png` 64x64x4 [source: design/items/brewery_passport_book_debaucheryville.md L276, L280]

**opener:**
- design: pixelated hop cone shape with scrolling LED display showing fake "blockchain hash," bottle opener as the stem [source: design/items/brewery_tour_bottle_opener_system.md L171]
- inscription: "Algorithm Verified" [source: design/items/brewery_tour_bottle_opener_system.md L173]
- material gag: matte black plastic with neon blue circuit trace inlays [source: design/items/brewery_tour_bottle_opener_system.md L172]
- special feature: tiny LED screen scrolls random hexadecimal codes [source: design/items/brewery_tour_bottle_opener_system.md L176]
- PNG: `bottle_opener_brewlab.png` 48x48; `bottle_opener_brewlab_scroll.png` 48x48x4 [source: design/items/brewery_passport_book_complete.md L468-469]

**beer: Blockchain Bock**
- style: "AI-optimized" dark bock [source: design/items/brewery_passport_book_debaucheryville.md L147]
- ABV: 7.2% [source: design/items/brewery_passport_book_debaucheryville.md L148]
- HP/SP: +20 HP, +10 Sovs (crypto fluctuation bonus, not SP) [source: design/items/brewery_passport_book_debaucheryville.md L149]
- effect: applies "Tourist Trapped" status (increased vulnerability to scams) [source: design/items/brewery_passport_book_debaucheryville.md L150]
- risk: the Sovs bonus may be negative if "market crashes" [source: design/items/brewery_passport_book_debaucheryville.md L151]
- price: 18 Sovs (fluctuates ±5 Sovs based on fake crypto ticker) [source: design/items/brewery_passport_book_debaucheryville.md L152] — **see Contradiction List #3** (breaks the 8–15 Sov price band)
- flavor text: "Brewed by algorithms. Verified by blockchain. Tasted by... actually, the AI doesn't taste. That's YOUR job." [source: design/items/brewery_passport_book_debaucheryville.md L153]
- brewed by: Ye Olde B.R.E.W. Lab (random number generator) [source: design/items/brewery_passport_book_debaucheryville.md L154]
- special quirk: price literally changes each time you check the menu [source: design/items/brewery_passport_book_debaucheryville.md L155]
- PNG: `blockchain_bock_bottle.png` 32x64; `blockchain_bock_icon.png` 32x32 [source: design/items/brewery_passport_book_debaucheryville.md L289-290]

---

### Sinfonia

#### moderato_pub
**stamp:**
- visual: metronome pendulum frozen mid-swing, beer stein at rest below [source: design/items/brewery_passport_book_sinfonia.md L131]
- ink: warm amber with copper accents [source: design/items/brewery_passport_book_sinfonia.md L132]
- animation: metronome ticks three times, stamp lands on final tick [source: design/items/brewery_passport_book_sinfonia.md L134]
- stamper NPC: Herr Takt [source: design/items/brewery_passport_book_sinfonia.md L135]
- stamp speech: "You argued! You defended! You probably changed no minds! But you PARTICIPATED! That's what matters here. *stamp* Welcome to the debate, forever." [source: design/items/brewery_passport_book_sinfonia.md L135] (fuller than `complete`'s truncated version)
- PNG: `stamp_moderato_pub.png` 64x64; `stamp_moderato_animation.png` 64x64x4 [source: design/items/brewery_passport_book_sinfonia.md L310, L314]

**opener:**
- design: metronome shape with bottle opener as the pendulum arm [source: design/items/brewery_tour_bottle_opener_system.md L199]
- inscription: "Tempo Is Everything" [source: design/items/brewery_tour_bottle_opener_system.md L201]
- material gag: aged bronze with copper accents [source: design/items/brewery_tour_bottle_opener_system.md L200]
- special feature: pendulum actually swings slightly when hanging [source: design/items/brewery_tour_bottle_opener_system.md L204]
- PNG: `bottle_opener_moderato_pub.png` 48x48; `bottle_opener_moderato_swing.png` 48x48 [source: design/items/brewery_passport_book_sinfonia.md L330-331] — **see Contradiction List #5** (`complete` names these `bottle_opener_moderato.png`/`_moderato_swing.png`)

**beer: Tempo Tantrum**
- style: medium-bodied amber ale, perfectly balanced [source: design/items/brewery_passport_book_sinfonia.md L163]
- ABV: 5.5% [source: design/items/brewery_passport_book_sinfonia.md L164]
- HP/SP: +20 HP, +10 SP [source: design/items/brewery_passport_book_sinfonia.md L165]
- effect: "Moderate Mood" — immune to Rushed/Sluggish for 30 min [source: design/items/brewery_passport_book_sinfonia.md L166]
- risk: none [source: design/items/brewery_passport_book_sinfonia.md L167]
- price: 6 Sovs [source: design/items/brewery_passport_book_sinfonia.md L168] — **see Contradiction List #3** (below the 8-Sov price-band floor)
- flavor text: "Not too hoppy, not too malty, not too strong, not too weak... It's perfect." — Herr Takt [source: design/items/brewery_passport_book_sinfonia.md L169]
- brewed by: The Moderato Pub (in-house, recipe unchanged since 1848) [source: design/items/brewery_passport_book_sinfonia.md L170]
- special quirk: the only beer all tempo factions grudgingly accept [source: design/items/brewery_passport_book_sinfonia.md L171]
- PNG: `tempo_tantrum_bottle.png` 32x64; `tempo_tantrum_icon.png` 32x32 [source: design/items/brewery_passport_book_sinfonia.md L320-321]

#### standing_ovation
**stamp:**
- visual: comedy and tragedy theater masks clinking beer steins together [source: design/items/brewery_passport_book_sinfonia.md L138]
- ink: dramatic crimson with gold leaf flecks [source: design/items/brewery_passport_book_sinfonia.md L139]
- animation: curtain rises, spotlight hits page, applause sound effect [source: design/items/brewery_passport_book_sinfonia.md L141]
- stamper NPC: Herr Dramatisch [source: design/items/brewery_passport_book_sinfonia.md L142]
- stamp speech: "You have PERFORMED! You have TOASTED! You have DRUNK! Let the record show: you earned this standing ovation. *stamps with flourish* BRAVO!" [source: design/items/brewery_passport_book_sinfonia.md L142]
- PNG: `stamp_standing_ovation.png` 64x64; `stamp_ovation_animation.png` 64x64x4 [source: design/items/brewery_passport_book_sinfonia.md L311, L315]

**opener:**
- design: comedy/tragedy theater masks with bottle opener integrated into the ribbon connecting them [source: design/items/brewery_tour_bottle_opener_system.md L216]
- inscription: "Bravo!" [source: design/items/brewery_tour_bottle_opener_system.md L218]
- material gag: polished brass with crimson enamel accents [source: design/items/brewery_tour_bottle_opener_system.md L217]
- special feature: makes a tiny "applause" click sound when used [source: design/items/brewery_tour_bottle_opener_system.md L221]
- PNG: `bottle_opener_standing_ovation.png` 48x48; `bottle_opener_standing_applause.png` 48x48 [source: design/items/brewery_passport_book_sinfonia.md L332-333] — **see Contradiction List #5** (`complete` names these `bottle_opener_ovation.png`/`_ovation_applause.png`)

**beer: Curtain Call Copper**
- style: Sinfonian copper lager with dramatic finish [source: design/items/brewery_passport_book_sinfonia.md L174]
- ABV: 5.8% [source: design/items/brewery_passport_book_sinfonia.md L175]
- HP/SP: +25 HP, +10 SP [source: design/items/brewery_passport_book_sinfonia.md L176]
- effect: "Stage Presence" (+3 Charm for 30 min) [source: design/items/brewery_passport_book_sinfonia.md L177]
- risk: none [source: design/items/brewery_passport_book_sinfonia.md L178]
- price: 8 Sovs [source: design/items/brewery_passport_book_sinfonia.md L179]
- flavor text: "Aged in barrels from the old opera house. Some say you can taste the ambition. Others say that's just the hops." [source: design/items/brewery_passport_book_sinfonia.md L180]
- brewed by: The Standing Ovation (on-site, with ceremony) [source: design/items/brewery_passport_book_sinfonia.md L181]
- special quirk: served with a small bow, always [source: design/items/brewery_passport_book_sinfonia.md L182]
- PNG: `curtain_call_copper_bottle.png` 32x64; `curtain_call_copper_icon.png` 32x32 [source: design/items/brewery_passport_book_sinfonia.md L322-323]

#### crown_and_cask
**stamp:**
- visual: ornate Habsburg-style crown resting atop an oak beer barrel [source: design/items/brewery_passport_book_sinfonia.md L145]
- ink: royal purple with gold leaf flecks [source: design/items/brewery_passport_book_sinfonia.md L146]
- animation: trumpet fanfare (tiny), crown descends onto page, wax seal effect [source: design/items/brewery_passport_book_sinfonia.md L148]
- stamper NPC: König Klaus [source: design/items/brewery_passport_book_sinfonia.md L149]
- stamp speech: "By the power vested in me by my grandfather, who vested it in himself, I hereby STAMP thee! Rise, Knight of the Cask! Your liver serves the crown!" [source: design/items/brewery_passport_book_sinfonia.md L149]
- PNG: `stamp_crown_cask.png` 64x64; `stamp_crown_animation.png` 64x64x4 [source: design/items/brewery_passport_book_sinfonia.md L312, L316]

**opener:**
- design: miniature Habsburg-style crown with bottle opener as the base/rim [source: design/items/brewery_tour_bottle_opener_system.md L233]
- inscription: "By Royal Appointment" [source: design/items/brewery_tour_bottle_opener_system.md L235]
- material gag: gold-tone metal with purple velvet pouch [source: design/items/brewery_tour_bottle_opener_system.md L234]
- special feature: comes with "Certificate of Nobility" (tiny scroll) [source: design/items/brewery_tour_bottle_opener_system.md L238]
- PNG: `bottle_opener_crown_cask.png` 48x48; `bottle_opener_crown_certificate.png` 32x32 [source: design/items/brewery_passport_book_sinfonia.md L334-335] — **see Contradiction List #5** (`complete` names the first `bottle_opener_crown.png`)

**beer: Heir Apparent Ale**
- style: Belgian-style golden ale with noble hop character [source: design/items/brewery_passport_book_sinfonia.md L185]
- ABV: 6.5% [source: design/items/brewery_passport_book_sinfonia.md L186]
- HP/SP: +30 HP, +15 SP [source: design/items/brewery_passport_book_sinfonia.md L187]
- effect: "Noble Blood" (+2 Charm, +2 Style for 45 min) [source: design/items/brewery_passport_book_sinfonia.md L188]
- risk: none [source: design/items/brewery_passport_book_sinfonia.md L189]
- price: 10 Sovs [source: design/items/brewery_passport_book_sinfonia.md L190]
- flavor text: "Brewed with hops that can trace their lineage back seven generations. The yeast is merely five generations, but we don't discuss that." [source: design/items/brewery_passport_book_sinfonia.md L191]
- brewed by: Crown & Cask (family recipe, "royal" process) [source: design/items/brewery_passport_book_sinfonia.md L192]
- special quirk: served in crown-shaped glass, which you keep (adds 3 Sovs) [source: design/items/brewery_passport_book_sinfonia.md L193]
- PNG: `heir_apparent_ale_bottle.png` 32x64; `heir_apparent_ale_icon.png` 32x32 [source: design/items/brewery_passport_book_sinfonia.md L324-325]

#### dancing_stein
**stamp:**
- visual: traditional beer stein with cartoon legs mid-waltz, foam trailing like a dress [source: design/items/brewery_passport_book_sinfonia.md L152]
- ink: ballroom gold with blue waltz accents [source: design/items/brewery_passport_book_sinfonia.md L153]
- animation: waltz music plays (3 beats), stamp spins onto page in rhythm [source: design/items/brewery_passport_book_sinfonia.md L155]
- stamper NPC: Herr Drehmeister [source: design/items/brewery_passport_book_sinfonia.md L156]
- stamp speech: "You waltzed! You carried! You barely spilled! *stamp in rhythm* ONE-two-three, ONE-two-three, STAMPED! Welcome to the dancers, friend!" [source: design/items/brewery_passport_book_sinfonia.md L156]
- PNG: `stamp_dancing_stein.png` 64x64; `stamp_dancing_animation.png` 64x64x4 [source: design/items/brewery_passport_book_sinfonia.md L313, L317]

**opener:**
- design: beer stein silhouette with dancing legs, bottle opener as the stein handle [source: design/items/brewery_tour_bottle_opener_system.md L250]
- inscription: "One-Two-Three" [source: design/items/brewery_tour_bottle_opener_system.md L252]
- material gag: brushed silver with ballroom gold accents [source: design/items/brewery_tour_bottle_opener_system.md L251]
- special feature: weighted to spin when flicked (like a dancer) [source: design/items/brewery_tour_bottle_opener_system.md L255]
- PNG: `bottle_opener_dancing_stein.png` 48x48; `bottle_opener_dancing_spin.png` 48x48 [source: design/items/brewery_passport_book_sinfonia.md L336-337] — **see Contradiction List #5** (`complete` names these `bottle_opener_dancing.png`/`_dancing_spin.png`)

**beer: Waltz Weizen**
- style: Bavarian-style wheat beer with swirling head [source: design/items/brewery_passport_book_sinfonia.md L196]
- ABV: 5.2% [source: design/items/brewery_passport_book_sinfonia.md L197]
- HP/SP: +20 HP, +15 SP [source: design/items/brewery_passport_book_sinfonia.md L198]
- effect: "Light on Your Feet" (+3 Speed, +2 Dance for 30 min) [source: design/items/brewery_passport_book_sinfonia.md L199]
- risk: none [source: design/items/brewery_passport_book_sinfonia.md L200]
- price: 7 Sovs [source: design/items/brewery_passport_book_sinfonia.md L201] — **see Contradiction List #3** (below the 8-Sov price-band floor)
- flavor text: "Brewed in three stages, fermented in three tanks, served in three-quarter time. The foam always swirls clockwise. We don't know why." [source: design/items/brewery_passport_book_sinfonia.md L202]
- brewed by: The Spinning Brewery (off-site partner, delivers fresh daily) [source: design/items/brewery_passport_book_sinfonia.md L203]
- special quirk: server does a small spin when delivering [source: design/items/brewery_passport_book_sinfonia.md L204]
- PNG: `waltz_weizen_bottle.png` 32x64; `waltz_weizen_icon.png` 32x32 [source: design/items/brewery_passport_book_sinfonia.md L326-327]

---

## Gap Manifest

Seeded from the design spec §3, plus everything new the walk uncovered.

**Publandia stamp mechanics (all four locations — animation and stamp speech missing
everywhere; design + ink ARE present via the city-page tables, so only these sub-fields gap):**
1. `blarney_trap` stamp animation
2. `blarney_trap` stamper NPC (no source explicitly names who stamps; Seamus is the hub NPC but is never stated to be the stamper)
3. `blarney_trap` stamp speech
4. `blarney_trap` beer "Brewed By" (Sweet Surrender)
5. `blarney_trap` beer special quirk (Sweet Surrender)
6. `stoutworks_brewery` stamp animation
7. `stoutworks_brewery` stamper NPC
8. `stoutworks_brewery` stamp speech
9. `stoutworks_brewery` beer "Brewed By" (Vat Master's Reserve)
10. `trinity_of_pints` stamp animation
11. `trinity_of_pints` stamper NPC
12. `trinity_of_pints` stamp speech
13. `trinity_of_pints` beer "Brewed By" (Academic Amber)
14. `trinity_of_pints` beer special quirk (Academic Amber)
15. `shenanigans` stamp animation
16. `shenanigans` stamper NPC
17. `shenanigans` stamp speech
18. `shenanigans` stamp PNG (only a generic unresolved placeholder `stamp_[fourth_publandia].png` exists anywhere)
19. `shenanigans` beer "Brewed By" (The Fool's Gold)
20. `shenanigans` beer PNG (bottle + icon — no PNG spec exists for The Fool's Gold anywhere, including the stray copy)

**Keychain replacement gags (parody stand-ins for real-world references — belongs to
`bottle_opener_keychain_item.md`, not one of the seven extraction sources; genuinely unresolved):**
21. Cancún
22. Daytona Beach
23. Señor Frog's
24. Munich/Oktoberfest
25. Belgium/Trappist
26. Germany/Czech Republic + Pilsner Urquell

**Salvage pile (dead-mechanic content the author must rule dead or keep as flavor):**
27. The 28 gatekeeper NPC quotes in `opener_doc` (With/Without-opener dialogue for 14 locations — Fiona, Dean Cathal, Mickey, Dr. Vaněk, Glitching Bouncer/Bouncer/Scanner, Herr Takt, Herr Dramatisch, König Klaus, Herr Drehmeister, Hendrik, Kees) — attached to the dead prerequisite-chain mechanic
28. "Key Collector" achievement — absent from the master spec's Rewards Ladder; appears in `deb_passport`'s and `sin_passport`'s Cross-City Mechanics sections as the reward for owning all openers [source: design/items/brewery_passport_book_debaucheryville.md L258; design/items/brewery_passport_book_sinfonia.md L295] (does NOT appear in `complete` — verified absent from that file)

**Not a gap — flagging for the record:** the design spec's own §3 lists "The Fool's Gold stat
block (name exists, no stats anywhere)" as a known gap. This extraction found a full stat block
in the stray copy (`design/worlds/publandia/brewery_passport_book.md` L256-265) — see the
deep-diff verdict above. The design spec's assumption was wrong; this is resolved, not gapped.

---

## Contradiction List

### Live (author decision needed)

1. **Trinity of Pints unlock condition** — three variants across sources:
   - "Complete drinking lecture" [source: design/items/brewery_passport_book.md L110] — `base`
     is the only source with this wording. (Checked directly: the stray Publandia copy does
     NOT repeat this text — it independently rewrites the row to "Graduate (complete Senior
     Thesis)" [source: design/worlds/publandia/brewery_passport_book.md L110], so it
     corroborates the variant below, not this one — see the Deep-diff verdict hunk 1 above.)
   - "Graduate (complete any drinking course)" as the OPENER's own acquisition condition [source: design/items/brewery_tour_bottle_opener_system.md L79]
   - "Complete the 'Senior Thesis' (final exam drinking course)" as the STAMP's unlock condition in the same document [source: design/items/brewery_tour_bottle_opener_system.md L86], matching `complete`'s [source: design/items/brewery_passport_book_complete.md L230], `sin_passport`'s [source: design/items/brewery_passport_book_sinfonia.md L94], and the stray copy's [source: design/worlds/publandia/brewery_passport_book.md L110] city-page tables (all read "Graduate (complete Senior Thesis)")
   Note the opener doc itself is internally split: opener acquisition = "any drinking course," stamp unlock = "Senior Thesis." Not resolved by depth — needs an author ruling on whether these are the same requirement worded loosely or genuinely two different gates.

2. **Iron Gut Tripel debuff duration** —
   - "-10% Accuracy" with no duration given (reads as unbounded) [source: design/items/brewery_passport_book_complete.md L306; design/items/brewery_tour_bottle_opener_system.md L166]
   - "-10% Accuracy next turn" [source: design/items/brewery_passport_book_debaucheryville.md L140]

3. **Beer price band vs actual prices** — template states 8–15 Sovs [source: design/items/brewery_passport_book.md L195]. Violations found:
   - Blockchain Bock: 18 Sovs (±5 fluctuation) — above ceiling [source: design/items/brewery_passport_book_debaucheryville.md L152; design/items/brewery_passport_book_complete.md L315]
   - Tempo Tantrum: 6 Sovs — below floor [source: design/items/brewery_passport_book_sinfonia.md L168] (newly found this pass — not in the design spec's seed)
   - Waltz Weizen: 7 Sovs — below floor [source: design/items/brewery_passport_book_sinfonia.md L201] (newly found this pass)

4. **+5% "Confused" resistance — dual, possibly duplicate, unlock paths** — the identical buff
   is granted by two different completion tracks:
   - Debaucheryville selfie-set completion ("Neon Photogenic" badge) [source: design/items/brewery_passport_book_debaucheryville.md L193]
   - "Debaucheryville Collector" achievement (own all 4 Debaucheryville openers) [source: design/items/brewery_tour_bottle_opener_system.md L190]
   Needs a ruling on whether this is an intentional stack, a duplication error, or two separate systems that happen to share a number.

5. **Sinfonia bottle-opener PNG naming** — `sin_passport` names per-brewery opener PNGs with
   full brewery-name stems (`bottle_opener_moderato_pub.png`, `_standing_ovation.png`,
   `_standing_applause.png`, `_crown_cask.png`, `_dancing_stein.png`)
   [source: design/items/brewery_passport_book_sinfonia.md L330-337], while `complete` uses
   shortened stems (`_moderato.png`, `_ovation.png`, `_ovation_applause.png`, `_crown.png`,
   `_dancing.png`) [source: design/items/brewery_passport_book_complete.md L472-479]. Flagged
   in Appendix A.2 as "a pipeline naming decision for the item files" — needs a ruling before
   the PNG_Assets docs are written in phase 3, since it affects real filenames.

### Void (do not ask)

Per design spec §2, dropped silently — listed here only for coverage-tracking, not for
interview:

- **Shamsterdam 6-stamp model** — `base` shows Shamsterdam with 4+2 bonus = 6 stamp slots
  [source: design/items/brewery_passport_book.md L138-150]; superseded by the 16-brewery
  (4 cities × 4) ruling in the master spec [source: design/quests/general_quests/brewerytour.md L12].
- **Passport slot order** — visit order across all city-page tables; ruled unimportant.
- **All stamp/opener/brewery totals other than 16** — 12 base + 2 expansion = 14
  [source: design/items/brewery_passport_book_complete.md L428-445; design/items/brewery_tour_bottle_opener_system.md L329, L362]; 12 base + 6 expansion = 18
  [source: design/items/brewery_passport_book_sinfonia.md L267-269, L347]; 16 base ruling
  [source: design/quests/general_quests/brewerytour.md L12] wins, all others void.
- **Per-location opener vendors and their Sovs prices** — every opener's "OR purchase for N
  Sovs" clause across `opener_doc`, `complete`, `deb_passport`, `sin_passport` (dead per
  design spec §2, ruled 2026-08-04).
- **ICQ opener sales** — Miss Morphine/Tony420/RedRoomRandy/CryptoBro69 popups selling
  "authentic culture"/openers [source: design/quests/debaucheryville/brewerytourdebaucheryville.md L39-50, L91-98, L141-148, L191-198]; dead with the sales mechanic (ICQ scam-gag reuse is fair game per master spec but is new content, not extraction).
- **One-keychain-gates-all / prerequisite chain ("Golden Rule")** — the entire ASCII
  prerequisite chain and "CRITICAL: this is THE KEY ITEM" framing
  [source: design/items/brewery_tour_bottle_opener_system.md L9-34], plus every gatekeeper's
  With/Without check dialogue gating access on possessing the Blarney Trap opener.
- **Per-city-opener model + cross-city barter** — the single "Debaucheryville Bottle Opener"
  (neon fairy, Shadow Exchange, 20 Sovs or Publandia-stamp-proof barter)
  [source: design/items/brewery_passport_book_debaucheryville.md L31-36] and single "Sinfonia
  Bottle Opener" (eighth note, Standing Ovation, 25 Sovs)
  [source: design/items/brewery_passport_book_sinfonia.md L38-43] — both superseded by the
  ruled hybrid model (one keychain container + per-brewery earned openers).
- **Shamsterdam-hangover-as-passive** — "Canal Courage" as PERMANENT PASSIVE
  [source: design/items/brewery_passport_book_complete.md L212-219]; ruled a CONSUMABLE like
  the other three cities' Legendary Hangovers [source: design/quests/general_quests/brewerytour.md L92-93]. (Shamsterdam is otherwise out of scope this round.)

---

## Shamsterdam parking lot

Out of scope this round; flagged only because these conflicting facts will matter to the future
Shamsterdam naming round.

- **Beer names conflict**: `base` names the two existing Shamsterdam beers "Molen's Midnight"
  and "Liquid Courage" [source: design/items/brewery_passport_book.md L141-142] while `complete`
  names them "Windmill Wit" and "Oude Genever" [source: design/items/brewery_passport_book_complete.md L162-163, L188, L198]. Both establishment names ("Brouwerij de Molen" — a real Dutch
  brewery — and "Proeflokaal 't Kansen") are themselves flagged for author rename in the master
  spec [source: design/quests/general_quests/brewerytour.md L19-22], so both beer names will
  need to be re-minted alongside them regardless of which wins.
- **Stamp ink color conflict**: `base` city-page table gives "orange ink" for Brouwerij de
  Molen's stamp [source: design/items/brewery_passport_book.md L141], while `complete`'s
  detailed stamp entry gives "Grain gold with copper metallic accents"
  [source: design/items/brewery_passport_book_complete.md L173].
- **`dutch_courage_passive.png` naming defect** — per design spec §2, this PNG name
  [source: design/items/brewery_passport_book_complete.md L501] must be corrected to the
  Canal Courage naming when the Shamsterdam round writes its assets.

---

## Rulings (Task 2 gap interview, 2026-08-05 — author)

**Contradiction 1 (Trinity of Pints gate): SUPERSEDED BY REDESIGN (author-dictated).** All
three legacy variants (thesis/course/lecture) are DEAD — "we will no longer be grading."
The course FORMAT stays but the courses become four playable rounds, each opened by
chugging a beer (stacking impairment as difficulty curve):
1. **Pub 115 — Social Drinking Basics**: win a toast-off against an NPC.
2. **Song 220 — Music Studies**: rhythm game, Irish drinking songs.
3. Hazing gauntlet with real fights at each station (course name TBD by author).
4. Beer pong tournament against the staff; **Dean Cathal is the round-4 opponent**.
**The Dean cheats and self-destructs (Always Sunny style):** he's winning with a magnetized
ball + hidden under-table magnet; overconfident, he winds up a dramatic trick shot, throws
too hard, the magnet yanks the ball down onto the cup rim — loud brittle CRACK — the cheap
plastic shell shatters, a grey lodestone magnet clatters out and zips across the table,
locking onto the Dean's own metal belt buckle/ring. The bros obliviously applaud the
"legendary high-level technique," cheer, slap his back, demand he teach them how to
"shatter the orb" on command. Referee reluctantly declares the bros winners and brings up
the rigged ball; Dean is salty throughout. OPEN (author weighing): straight to a backhanded
compliment dripping in sarcasm/disdain, OR a battle vs the Dean + three professors first
(compliment delivered after). **Graduation beat:** bros don graduation robes → podium photo
with the Dean and the (obliviously smiling) brewmaster, who holds up the bottle opener +
location special beer; Lord Pilsner takes a rolled-up "graduation certificate" and gives
the Dean rabbit ears; Bradley bent over vomiting on the Dean's shoes (Dean disgusted);
Chadwick mooning the camera under his robes. Brewmaster stamps the passport and hands over
the items; Dean mumbles about stupid American tourists. **Exit beat:** at the door the
drunk bros are confronted by the Dean and the professors — cut to black, sounds/text imply
a lesson being taught — they wake Hungover (pounding headache, nausea) in the alley behind
Trinity of Pints. A secondary event follows immediately after (author has it, to be
dictated). Files affected beyond the item files: the Publandia city quest file AND
design/worlds/publandia/trinity_of_pints.md (existing structure largely stands, grading
removed). Gap #11 partially resolved: the BREWMASTER is Trinity's stamper.

**Trinity ruling addendum (author): BATTLE IS IN.** After the referee ruling, the Dean —
humiliated and exposed as a fraud in front of the "students" (patrons) and professors —
grows red-faced, RIPS OFF his tweed jacket, grabs his heavy ceremonial brass gavel, and
screams "NOBODY GRADUATES! SECURE THE QUAD!" → straight into battle vs the Dean + three
professors (backhanded compliment delivered post-battle). Author note: lets the bros
succeed without being heroes or great at any of it. CHANGED beat: the post-graduation
knockout at the door is done by SECURITY (not the faculty) — bros are knocked out, the
lesson-teaching beatdown happens during the blackout, then wake Hungover in the alley
behind Trinity of Pints as planned.

**Trinity ruling addendum 2 (author-dictated, dialogue verbatim): the referee-reveal beat.**
Bros read the magnet as part of the technique (option 1), and the win is FORCED on them by
panicked tournament officials: the ref blows a whistle, waves a red card, shouts over the
crowd "Dean Cathal is disqualified! By tournament rule 4B, the challengers win by default!"
Pilsner completely ignores the word "disqualified" — in his mind his aura physically
shattered the Dean's ball on impact. Pilsner: "Did you see that?! My defense was so solid
his ball literally exploded! That's a critical block! We broke his ammo!" When the ref
points at the magnets on the table, Pilsner isn't mad — he's inspired: "Wait... you can put
MAGNETS in the ping pong balls?! Dean, you beautiful bastard! Chadwick, write this down!
We're magnetizing our balls next time we play beer pong!" The Dean's brain breaks — stripped
of his title for cheating while Pilsner claims a mind-toughness KO, celebrates the default
win, and fanboys his "tactical magnet placement." Dean Cathal screams "I WAS CHEATING, YOU
ABSOLUTE MONKEYS! I WAS TRYING TO HUMILIATE YOU!" Pilsner smirks, pats his shoulder: "Hey,
no need to be humble, Dean! Game recognizes game. Now hand over the bottle opener, or do we
have to take our diplomas by force?" → Cathal snaps, calls the professors, battle starts.
Author's stated rationale (canon logic, cite in quest doc dev notes): (1) self-centered
logic — Pilsner attributes the win to his own toughness/luck, never procedure; (2) anti-hero
satire — the scam fails because the bros are too self-absorbed to notice being scammed, so
the insult never lands; (3) escalation — the Dean gets ZERO satisfaction from his villainy;
being trolled by oblivious confidence drives the rage that triggers the boss fight.

**Trinity ruling addendum 3 (author):** Course 3 = "Greek 330 — Applied Fraternal
Traditions" (the hazing gauntlet with real fights per station). Course 4 = "Thesis Defense
401" (the beer pong tournament — the thesis survives as a name-only joke: you defend your
thesis across ten cups; no grading anywhere).

**Trinity ruling addendum 4 (author): faculty casting approved as proposed.** Pub 115
toast-off = Prof. Róisín O'Sullivan (Spirits Dept, bent: intro course teaches toasting as
foundational etiquette, shot in hand). Song 220 = Prof. Aisling Byrne (bodhrán/rhythm/Irish
drinking songs). Greek 330 = Prof. Cian MacCarthy (Games & Rec). Thesis Defense 401 = Dean
Cathal Murphy. The three professors are the Dean's battle allies in SECURE THE QUAD.
TWO NEW NPCs REQUIRED (author-flagged): the tournament REFEREE (whistle, red card, rule 4B
call, reluctantly presents the rigged ball) and the Trinity BREWMASTER (stamps the passport,
obliviously smiling in the graduation selfie holding the opener + special beer). Identity/
names pending next interview answer.

**Trinity ruling addendum 5 (author):** Claude drafts BOTH new NPCs (referee + brewmaster)
as full NPC-template profiles, ⚠ AUTHOR-REVIEW flagged, for author approval before they
enter the files. The brewmaster draft carries Trinity's stamp speech (folds gap #12 into
the review). Gaps #10/#12 (Trinity stamp animation + speech) route through these drafts.

**Trinity ruling addendum 6 (author-dictated): the Brenda call — secondary event
immediately after the alley wake-up.** PHONE CANON (partial, being drawn in another
window — transcribe, do not extend): the bros' cellphones were taken on arrival in
Euromemeia (parody Europe; author to fill in WHY later). They share ONE phone: contacts
pre-programmed (caller ID shows names), has ICQ messenger, and it ONLY works on
speakerphone — there is no privacy on this phone, ever. Brenda = Chadwick's wife; she acts
as if she doesn't know she's on speaker (SHE KNOWS — reason lands in story work in the
author's other window; do not explain it anywhere).

SCENE (dialogue verbatim, placement: bros wake Hungover in the alley, nauseous, dizzy;
Bradley + Pilsner groaning on the curb about their stomachs, sun too bright; phone rings,
caller ID: Brenda):
- Chadwick (whispering frantically): "Guys... quiet! It's Brenda!"
- Brenda: "Chadwick? Are you alone? I've been thinking about you all day..."
- Chadwick: "Uh- hi honey! Yes! Total signal isolation over here! Just... standing in a
  very quiet academic square!"
- Brenda: "Good. Because Headmistress Brenda needs to know if her naughty little student
  has been misbehaving in class. Did you get sent to the principal's office?"
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
  my headache. Call her back! I want to hear about your detention. Does she spank you with
  a ruler?"
- Chadwick (bright red, adjusting his collar): "She was testing the network stability! It
  was a line test!"

Home: Publandia city quest file, Trinity of Pints sequence (post-alley-wake-up scripted
event). Cross-window dependency: the phone/ICQ system doc is the OTHER window's to draw in;
this scene only USES the canon above.

**Contradiction 2 RULED (author): Iron Gut Tripel = "-10% Accuracy next turn" (next turn
only), per the Debaucheryville city file.**
