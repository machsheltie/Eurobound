# Design Spec: Nothing Is Getting Through (The Herp / Gold Circle Coin Questline) + Deferral Batch

**Date:** 2026-07-30
**Status:** Approved by author (interview + section-by-section review)
**Execution:** Agent team (agent-teams plugin) — 1 lead, 4 implementer lanes with file ownership, 1 canon/tone reviewer.
**Predecessor:** Bacchanus Beach Beatdown batch (merged to main at cbe3d7d). This spec builds on its
locations (Bohemian Riviera / Fauxst Beach night_party_zone seed), its status-effect conventions
(Port-O-Cologne), and its permanent-item template.

---

## 1. Premise

The morning after an all-night Fauxst Beach party, all three bros wake up itching. They diagnose
poison ivy. It is not poison ivy. It is **The Herp** — permanent, incurable, and suppressible only
by the legendary **Gold Circle Coin** (Pretty Woman's "condom of champions — nothin' is gettin'
through this sucker"), which sits in a velvet vitrine in Sinfonia's **Haute Couture Haberdashery**.
The bros must limp across Europe with burning crotches, get humiliatingly rejected by every woman
they approach, and either buy their way into Monsieur Aiguille's respect or steal the Coin in
formal wear. The Herp is never cured — only suppressed while the Coin is equipped.

- **Quest ID:** `debaucheryville_sidequest_nothing_is_getting_through_01`
- **Display Name:** "Nothing Is Getting Through"
- **Satirical Subtitle:** "A love story between three men and one legendary prophylactic"
- **File:** `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md`
  (originates in Debaucheryville; spans to Sinfonia; full `Templates/sidequest_template.md` compliance)

## 2. Patient Zero: QUEEN Riviéra Renata (new NPC, full profile)

- **Who:** A Bohemian Riviera institution. ~15 years OLDER than the bros (mid-50s). Decades of
  devoted sun worship. Ridiculously high libido, loves a good party, "spreads the love amongst
  all beachgoers equally — it's only fair." Local legend spoken of with genuine respect and mild awe.
- **Tone rule (binding):** SHE IS NOT THE JOKE. She gets the Janek treatment — confident,
  self-possessed, zero shame, gets exactly what she came for, has the sense to redress. The comedy
  lands 100% on the bros' beer goggles and morning horror. Never body-mock her; the bros' delusion
  is the target.
- **Appearance rule (author revision, binding):** Renata is genuinely HOT at 55 and stunningly,
  impeccably dressed the morning after. Sun worship reads as decades-deep bronze and total ease —
  texture, never decay. The beer goggles' lie was her AGE (she rendered as 22), NOT her looks;
  she was never a downgrade. She is never written or rendered as withered, gross, or a cautionary
  tale — she's the confident older woman doing exactly what celebrated men do, collecting younger
  men without shame. The bros' morning horror is the age-and-legend reveal plus The Herp — never
  her appearance. The satire target here is the double standard itself: she visibly IS a queen,
  they visibly were the haul.
- **Name mechanics:** Locals mention "Riviéra Renata" in passing during the party-night scene
  ("Renata's here somewhere tonight—") — the bros never connect it. During her morning exit, it
  dawns on them: "Wait— *you're* Riviéra Renata?" She answers with a wink, pride in her voice, and
  serious swagger: **"That's QUEEN Riviéra Renata to you!"**
- Her Chronicles entry is scripted/mandatory (see §4).
- **File:** `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/queen_riviera_renata.md`
  (full `Templates/NPC_Profile_Template.md`).

## 3. The Outbreak Scene (scripted trio event, night_party_zone)

1. **Party montage:** strobes; beer goggles rendered LITERALLY — through-the-goggles her sprite is
   a 22-year-old knockout, shown three separate times to three oblivious bros (each unaware of the
   others). Locals' background dialogue drops her name. (Beer goggles + possibly substances; keep
   it goggles-forward.)
2. **Morning:** seagulls, regret. Two bros discover the third **cocooned in a sleeping bag wearing
   only a leopard-print male thong that is not his** ("Bro. Whose is this." / "...Mine now?").
   **Thong-bro is LORD PILSNER (author-locked).** Chadwick and Bradley are the standing bros;
   Bradley keeps the CRABS line AND the "DEFINITELY foliage" line; "...Mine now?" is Pilsner's;
   Pilsner delivers the verdict "POISON IVY. Thank God. Boys, that's poison ivy." from inside
   the sleeping bag. Renata's neck-hug + kiss goes to Pilsner.
   **Thong item (author-locked):** the leopard-print thong is a PERMANENT, EQUIPPABLE item —
   `item_leopard_print_thong`, full `Templates/permanent_item_template.md` file at
   `Design/Inventory/items/leopard_print_thong_item.md`. Granted automatically to Lord Pilsner
   during the outbreak morning ("...Mine now?" IS the acquisition line). Cannot be sold, dropped,
   or traded. Its original owner is NEVER established — not Renata's, not anyone's; the mystery
   is permanent canon. This supersedes the earlier "props-only / no item ID" working rule; the
   quest file's and Renata profile's binding notes update accordingly.
3. **The exit (the reveal):** Renata rises from the other side of the sleeping bag, **stunningly
   dressed** — put-together, striking, morning-light glamorous while the bros are crusty wreckage —
   sunglasses on. She **pats each standing bro on the cheek exactly the way
   their mothers would**, throws her arms around thong-bro's neck, plants a big kiss on his mouth,
   and jogs off down the beach calling **"You're such nice boys!"** Mid-exit: the "QUEEN Riviéra
   Renata to you!" beat (§2). The identical maternal affection to all three IS the reveal — no
   cross-referencing dialogue. Narrator: "Nobody said it out loud."
4. All three bros itching in unison by scene's end. All three infected — guaranteed, scripted.
5. Bros' diagnosis: poison ivy ("there was DEFINITELY foliage at that beach party"). Bradley
   delivers: **"Bro it itches so bad it looks like we got CRABS."** They remain serenely confident.

## 4. Quest Flow

1. **Outbreak** (§3) — doubles as a canonical Couchsurfing Chronicles entry. Because it is
   scripted for all players, full Chronicles completion REQUIRES catching The Herp; the
   "Slept Around, Found Out" title becomes literal and load-bearing.
2. **Diagnosis refusal — Věra @ Midnight Munchies General Store** (its file already lists "status
   effect management"). Věra, judgment-free, glances once: it is not poison ivy; there was no
   poison ivy; that beach has no plants — it doesn't even have real sand. She refuses standard
   cures: **"European strains require cinematic-grade containment."** The Herp locks in.
3. **Prophecy pointer — Hamstradamus's tent:** "ONLY THE GOLD CIRCLE SHALL STAY THE BURNING.
   SEEK THE HOUSE OF NEEDLES. REPENT." (House of Needles = the Haberdashery; **Aiguille = French
   for "needle"** — the pun is canon now.)
4. **The Departure — Oz parody (author-locked):** the moment the bros commit to seeking the Gold
   Circle Coin in Sinfonia, they LINK ARMS AND SKIP toward the airport singing an original parody
   of "We're Off to See the Wizard" — destination the House of Needles / the Haberdashery /
   Monsieur Aiguille (reference only what they canonically know at that story beat). ORIGINAL
   lyrics only — scans to the Oz tune and mirrors its call-and-response structure, but reproduces
   none of the 1939 lyrics. Fully sincere, zero self-awareness; the skip visibly fights the Herp's
   Agonizing Friction (wince-skip-wince); locals watch. This is a staged musical scene in the
   quest file.
5. **The Limp to Sinfonia:** The Herp active throughout. NO temporary suppressant exists anywhere
   (author decision: delayed gratification; the Coin must feel Excalibur-tier). Couchsurf attempts
   while infected trigger per-NPC characterized rejection scenes (§6). Missed opportunities are
   the point.
6. **Haute Couture Haberdashery (EXISTING location — surgical edit, not a rewrite):**
   The Gold Circle Coin sits in a locked vitrine in the Accessories Alcove, filed under
   *Objets d'Héritage*: "Molded 1990. A piece of cinema history. **It is not for sale. It is for
   aspiration.**" The bros' canonical first-visit snubbing (the shop's existing Assessment
   Protocol) is the Pretty Woman snub; the return is the "Big mistake. Huge." arc.
   - **PATH A — "Become Someone Who Belongs Here" (trade):** reach Valued Client status (€500
     spent via the shop's EXISTING tier system) + an absurd errand for Monsieur Aiguille; he then
     opens the vitrine with genuine ceremony — he respects the Coin more than they do.
   - **PATH B — "Big. Huge. Mistake." (heist):** after-hours infiltration requiring formal wear
     purchased from the same shop; the bros hold mannequin poses in opera capes while the night
     porter passes (the quest's marquee screenshot moment).
7. **The Prize:** the Gold Circle Coin (§7). Party-wide suppression while equipped by ANY bro.
8. **The Return:** cities are revisitable. Every NPC who rejected a herp'd bro can be re-attempted
   post-Coin; each has a rejection-callback line. Chronicles completion stays fully achievable.
9. **Post-credits scene:** months later, back home — the Coin framed on a wall like a championship
   belt; one bro still absentmindedly scratching.

## 5. The Herp (status effect, id `the_herp`)

- Permanent. Never cured; suppressed only while the Coin is equipped (any bro → whole party).
- Effects while active: −2 Charm (all NPCs); romance/couchsurf attempts auto-trigger rejection
  scenes; **Groin Blurts** — rare involuntary dialogue interruptions ("DOES ANYONE HAVE A BAG OF
  FROZEN PEAS?!", "IT'S JUST A RASH, I SWEAR!"); subtle waist-level heat-shimmer particle (REUSES
  the Riviera PNG doc's existing heat_shimmer asset); NPCs visibly step back.
- Entry added to `Design/Mechanics/Battle/status_effects.md` beside Port-O-Cologne, matching house
  style. All three bros carry it simultaneously.

## 6. The Rejection System & The Six Ladies

Harvest the five Debaucheryville couchsurf NPCs from `couchsurfingchroniclesdebaucheryville.md`
into official full NPC profiles (same treatment as the Beatdown NPCs), PLUS Renata (§2). Each
profile includes a **characterized Herp-rejection scene** (matching her established personality;
humiliating for the bros; never nice) and a **post-cure callback line** for the re-attempt:

| NPC | File (in `Design/Character Profiles/DebaucheryvilleNPCs/`) | Rejection flavor (starting point) |
|---|---|---|
| Queen Riviéra Renata | `Bohemian Riviera/queen_riviera_renata.md` | (She's the source; her "rejection" is cheerful unavailability — she's already moved on to the next party) |
| Vape Witch Vanessa | `DebaucheryvilleNPCs/.../vape_witch_vanessa.md` | Consults her crystals, recoils: "your aura is... contagious" |
| Backpack Girl Who Never Left | `.../backpack_girl_who_never_left.md` | Writes a ballad about it on the spot, performs it at the hostel |
| CryptoBro69's "Ex" | `.../cryptobro69s_ex.md` | Laughs, screenshots, sends to CryptoBro69; his ICQ gloating follows |
| Suspicious Twins (Polina & Paulina) | `.../suspicious_twins_polina_paulina.md` | Update the American Tourist Bingo card ("herpes" was already a square) |
| Miss Morphine | `.../miss_morphine.md` | Rejection is just an ICQ auto-reply (preserves her is-she-real ambiguity — NEVER resolve it) |

Existing canon files updated (not rewritten): `Design/Quests/couchsurfingchronicles.md` and
`.../Location Specific/Debaucheryville/couchsurfingchroniclesdebaucheryville.md` gain the Renata
entry, the rejection-hook note, and the completion-requires-Herp note. Twins stay at the Cirque;
Ex stays at the Shadow Exchange; nobody relocates.

## 7. Gold Circle Coin (item, `item_gold_circle_coin`)

- Full permanent-item file using `Templates/permanent_item_template.md`:
  `Design/Inventory/items/gold_circle_coin_item.md`.
- Key item / equippable accessory. **The Deception inverted:** for once the item actually IS what
  the legend claims — the one item in the game that fully delivers. Party-wide Herp suppression
  ("aura of champions") while equipped by any bro; unequip → the shimmer returns.
- One and only. Cannot be sold, dropped, or traded ("It is not for sale. It is for aspiration." —
  the bros finally agree with Aiguille on something).
- Pretty Woman quote canon: "the condom of champions, the one and only… nothin' is gettin'
  through this sucker."

## 8. Aaron / "She Thinks My Tractor's Sexy" NFT — PARKED

Author is developing this separately for the Black-Tie Backroom (Sinfonia). NOT in this batch.
Do not reference it anywhere.

## 9. Deferral Cleanup Batch (Lane D — from the Beatdown round's ledger triage)

1. **NPC ID backfill:** add formal NPC ID blocks to `the_participation_trophy.md` (Yolanda →
   `debaucheryville_npc_yolanda_kovarik_01`) and `mysterymeatcart.md` (Chef Chuckles →
   `debaucheryville_npc_chef_chuckles_01`), matching the provisional IDs minted in the Cirque
   NPCs JSON so they become canonical.
2. **Item-icon sprite fixes:** the 5 icon refs in `items/bohemian_riviera_items.json` that point
   at unspecced PNGs → convert to existing-sheet pointer style (the pattern
   `cirque_du_shady_items.json` uses); unify the currency field wording.
3. **Small polish:** stein rarity-line rewording (dedupe vs badge); improve the flat "random
   tourist kid" NPC reaction row in `trivia_champ_badge_item.md`; add one line to the Beatdown
   minigame turn-structure row stating launched bros leave the round-robin; add a one-line spec
   note in the stein file acknowledging Glitter Gullet as a deliberate deviation from the spec's
   "brief Nausea."
4. **Optional (do last, only if capacity):** compact standalone profiles for Rosťa, Standa, Zdenka.

## 10. Agent-Team Structure

1 team-lead + 4 implementers (strict file ownership) + 1 canon/tone reviewer.

- **Lane A — Quest & Scenes:** the sidequest file (full template: outbreak scene per §3, Věra
  refusal, prophecy, limp, both Haberdashery paths, post-credits) + the two Chronicles file updates.
- **Lane B — The Six Ladies:** six NPC profiles per §6 (full template each). Renata FIRST —
  Lane A quotes her dialogue.
- **Lane C — Items & Systems:** Gold Circle Coin item file; `the_herp` status entry; Haberdashery
  vitrine + quest-dialogue edit (surgical — do not rewrite the shop file); Bohemian Riviera
  night_party_zone outbreak wiring (location file + relevant JSONs in the existing suite).
- **Lane D — Deferral batch** (§9).
- **Reviewer dimension:** canon fidelity (verbatim quotes: Renata's lines, Věra's line, prophecy,
  Pretty Woman quote), tone (satire targets the bros; Renata and the ladies keep their dignity as
  established), template compliance, no lane-crossing edits.
- Sequencing: Lane B delivers Renata before Lane A finalizes the outbreak scene. Lanes C and D
  fully parallel.

## 11. Binding Tone & World Rules (carried from the Beatdown spec)

- Bros NEVER self-aware; players laugh AT them; the bros are delusional pushing-40 dad-bods, not
  studs — every "conquest" is a misread.
- **Bros NEVER scam-aware (author-locked, applies to all three, game-wide):** they never suspect,
  question, or even momentarily entertain that they are being scammed, overcharged, or
  manipulated. They believe they are special, always. Canonical example: the VIP "bracelets" —
  kids' 8th-birthday-party bracelets they proudly believe are genuine VIP. Any line where a bro
  wonders whether he is being played (e.g. "Did we just get manipulated into spending €800?") is
  a defect and must be rewritten as sincere delusion.
  **Corollary (author-locked):** whenever money changes hands, the bros believe THEY are the ones
  getting one over on the seller — the price is a STEAL, the find is underpriced, the seller
  "doesn't know what he has." Inverse Legally Blonde: they are the mark who is certain they're
  the shark. The seller always knows exactly what they have.
- Satire targets frat-bro/tourist psychology, reality-TV, and luxury-retail gatekeeping — never
  Czech/Austrian people, never women's bodies. Renata, Věra, Aiguille, and all six ladies keep
  their dignity; they are winners, operators, or unbothered.
- No crypto beyond established canon (CryptoBro69's existing gags are fine; add nothing new).
- Never "spring break." World names only (Debaucheryville, Sinfonia, The Bacchanus — never
  Prague/Vienna/Vltava). Y2K-era cringe (ICQ, 1990 latex, VHS).
- No graphic sexual content — everything by implication, cutaway, and morning-after wreckage
  (consistent with the Chronicles' existing "no graphic content" rule).

## 12. Deliverable Checklist

1. `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md` (new, full template)
2. `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/queen_riviera_renata.md` (new)
3–7. Five harvested-lady profiles (new; §6 table paths)
8. `Design/Inventory/items/gold_circle_coin_item.md` (new, permanent-item template)
9. Edit `Design/Mechanics/Battle/status_effects.md` (+`the_herp`)
10. Edit `Design/World Design/Sinfonia/haute_couture_haberdashery.md` (vitrine, quest dialogue, quest integration)
11. Edit `Design/World Design/Debaucheryville/bohemian_riviera.md` + relevant Riviera JSONs (outbreak event wiring)
12. Edit `Design/Quests/couchsurfingchronicles.md` + `couchsurfingchroniclesdebaucheryville.md`
13. Deferral batch edits (§9: 2 NPC files, 1 items JSON, 3 polish edits; optional 3 compact profiles)
