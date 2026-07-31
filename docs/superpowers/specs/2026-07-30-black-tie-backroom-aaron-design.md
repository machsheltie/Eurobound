# Design Spec: The Black-Tie Backroom & Aaron the Unflappable + NFT Quest Integration

**Date:** 2026-07-30
**Status:** Approved by author (interview + section-by-section review)
**Execution:** Agent team — orchestrator (session lead), implementer lanes with strict file ownership, canon/tone reviewer.
**Predecessors:** Bacchanus Beach Beatdown batch; "Nothing Is Getting Through" batch (both on main). This
spec builds on the Round 2 spec's binding rules (never self-aware, never scam-aware + steal corollary,
world names only, template floors) — all of which remain in force.

---

## 1. NEW BINDING RULES (author-locked, game-wide, permanent — precede everything else)

### 1a. Trust the Player
No guardrails around the author's satire, ever. The satire is never broken, softened, lampshaded,
or explained without the author's explicit permission. Forbidden devices: truth-tellers, Greek
choruses, moral compasses, meta-narrators, fourth-wall explainers, or ANY character/mechanism whose
function is to tell the player what they just watched or that the bros are wrong. Dramatic irony is
delivered by STAGING (what the player sees), never by STATEMENT (what a character or narrator
announces). The player is trusted to get the joke. Content that explains the joke is a defect.
(The Narrator voice remains canon where already established — dry stage description, e.g. "Nobody
said it out loud." — but never explains, moralizes, or winks that "this is satire.")

### 1b. Gregory Is Dead (eradication, strip-on-sight)
"Gregory," a hand puppet attributed to Bradley, was invented by earlier AI sessions and is NOT
author canon (he appears in no author-written Bradley material). He is stricken:
- Gregory does not exist. No file may reference him. Any lane touching a file that contains him
  MUST remove him as part of its edit, whatever the lane's primary task.
- Replacement rule: each Gregory line is either (a) CUT entirely, or (b) rewritten as a plain,
  understated Bradley line with the explanatory observation itself DELETED — Bradley may be the
  quiet one; he may never be the explanation. Never transfer Gregory's truth-telling function to
  any other character or device.
- Committed files to purge this round (Lane D): `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md`
  (incl. rewriting the Oz song's verse 2 response line), `Design/Inventory/items/gold_circle_coin_item.md`,
  `Design/Inventory/items/leopard_print_thong_item.md`, `Design/World Design/Sinfonia/haute_couture_haberdashery.md`,
  `Design/World Design/Debaucheryville/the_participation_trophy.md`, `Design/Quests/greatdonerdebate.md`.
- `the_black_tie_backroom.md` is purged by Lane A during its completion pass.
- The ~55 uncommitted draft world files containing Gregory are NOT processed this round; the
  standing rule strips him whenever a future round formally processes those files.

## 2. Location: The Black-Tie Backroom — Keep + Complete

The existing `Design/World Design/Sinfonia/the_black_tie_backroom.md` (513 lines: hidden entrance,
€500 collateral, three mini-games with house-edge math, cheating system, Herr Falsch hidden boss,
Siegfried couchsurf, Baroness vault tie-in) is APPROVED as canon foundation. This round:
1. **Full data suite** matching Sinfonia's four complete locations: `PNG_Assets/the_black_tie_backroom_png_assets.md`
   + 8 JSONs (`core`, `npcs`, `interactions`, `environment`, `items`, `events`, `location_nodes`,
   `sprite_mapping`) in the existing per-type subfolders, following the sibling files' schemas.
2. **Surgical .md edits:** scrub the two "Habsburg" world-name violations (lines ~122, ~462 area —
   replace with Sinfonia-world equivalents, same treatment as the Haberdashery scrub); remove
   Gregory (4 dialogue sites); add **Aaron's felt-covered corner table** as a named zone of the
   main floor (scene trigger, visually distinct from the playable poker tables); register the two
   new items and the encounter in the relevant sections.
3. Location ID stays `sinfonia_operahouse_blacktie_backroom_01`.

## 3. NPC: Aaron the Unflappable (new, full profile)

- **File:** `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/aaron_the_unflappable.md`
  (new folder tree; full `Templates/NPC_Profile_Template.md`, all 16 sections minimum).
- **ID:** `sinfonia_npc_aaron_unflappable_01`. Display name: "Aaron the Unflappable."
- **Who:** the Unbothered Local Legend at the corner table. Slightly rumpled velvet dinner jacket.
  Double White Russian in a crystal tumbler, always. The candy-cigarette ritual: stirs the drink
  with it, takes a dramatic drag, bites the end off with a loud CRUNCH, draws a fresh one from a
  worn carton (he recently quit smoking; the carton never seems to empty). Junk-food connoisseur.
  Squirrely, dopamine-chasing, ADHD energy — plays poker entirely on vibes and gut ("You gotta
  FEEL the turn. You gotta let the felt speak to you."). Won big last year on pocket kings; the
  encounter reenacts it. Genuine, unforced kindness after cleaning someone out.
- **Tone (binding):** he is a winner-operator with dignity fully intact — never the joke. The joke
  is the bros misreading him ("He's drinking melted ice cream and chewing on sugar sticks. He's
  weak."). His vibes-based play WORKS; no one explains why; no one may ever explain why (rule 1a).
- **Post-encounter:** stays at his table permanently as ambient flavor — rotating vibes dialogue,
  visibly winning weird hands in the background. NEVER a playable opponent.
- **Privacy (binding):** all content 100% diegetic. No meta commentary anywhere in any file about
  real-world inspiration. Nothing in the repo may hint the character is a personal Easter egg.

## 4. The Encounter: "The Kings Were Humming" (scripted cinematic)

- **Structure (author-locked, per playtest-hazard review):** pure spectator comedy beat. The poker
  betting UI NEVER opens at Aaron's table. Approaching the corner table (with the entry conditions
  met) triggers the scene. The player never holds cards, never sees a bet slider, never has input
  that implies winnability. Player participation: at 2–3 beats, the player picks WHICH terrible
  line a bro says next — every option is a different flavor of unearned Casino-Royale swagger; all
  paths reach the identical outcome. The scene must be visually distinct from the room's real,
  fair, playable poker tables so the two are never confused.
- **Stakes (author-locked):** the pot is exactly the door's €500 collateral chips. Uniform for
  every player by construction; bros dramatize it as "our entire vacation budget" (never
  scam-aware; the loss becomes high-roller variance in their telling). Gold above €500 untouched.
  Under-€500 parties are bounced by Viktor at the door (existing canon beat: "Döner is not
  accepted") — the encounter cannot fire underfunded. Systemic comedy note: a party that busts
  here can no longer afford the Haberdashery's €500 Valued Client path — organically nudging
  broke players toward PATH B's mannequin heist. No hard gate either direction.
- **Beats:** (1) bros clock the milk drink and candy cigarettes as weakness, showcase their
  "expertise" hard — misread tells narrated aloud at full volume, Casino Royale cited as poker
  credentials; (2) the 7-2 offsuit all-in ("Show him what American capital looks like"); (3) the
  vibes speech ("You guys are calculating numbers... Poker isn't math, bro."); (4) instant call,
  zero hesitation; (5) POCKET KINGS — "The kings were humming, man. They wanted to stretch their
  legs."; (6) bust-out, dealer sweeps; (7) the sympathy beat — Aaron's genuine "aw, you look like
  a couple of doggies caught in the rain" moment; (8) both item grants (§5); (9) exit — bros
  reframe as asset-rich; Aaron: "No cab vouchers, bro. But if you walk fast enough, you stay
  warm." One-time scene; Aaron ambient thereafter (§3).
- **Quest wrapper:** the encounter is registered as a sidequest file
  `Design/Quests/Location Specific/Sinfonia/thekingswerehumming.md` (full
  `Templates/sidequest_template.md` compliance), which also carries the staging of the item
  grants and the NFT-hunt hook. (Sinfonia folder under Location Specific is new — create it.)

## 5. The Two New Items (full `Templates/permanent_item_template.md`, 12 sections each)

1. **Puff-Puff-Powder™ Chalk 'n' Ash Candy Smokes** — `Design/Inventory/items/candy_smokes_item.md`,
   id `item_candy_smokes`. Permanent novelty item (author-locked: NOT a consumable — a worn carton
   that never runs out, mirroring Aaron's). Use effect: bite one — small, short comedy
   confidence/Bravado buff; chalky white ring around the mouth (visual); the "+4% Perceived
   Confidence" gag stat framing is canon-approved flavor. Granted by Aaron at encounter beat 8
   with his line ("Don't smoke it, just bite the end off.").
2. **"She Thinks My Tractor's Sexy" (Mint #42)** — `Design/Inventory/items/tractor_nft_item.md`,
   id `item_tractor_nft`. Quest item / digital junk: a low-res animated GIF of a zero-turn mower
   doing a donut on a manicured lawn, tiny pixelated cowboy hat bouncing on the seat, stamped on
   a scratched aluminum token that smells faintly of Kahlúa and fresh-cut grass. QR links to an
   expired Geocities page. Worth €0 at any bank, exchange, or legitimate vendor. Advances the
   Frat Bro NFT quest (one of Sinfonia's four, §6). Granted at encounter beat 8 ("It's on the
   chain. Digital land, baby. ... that's your ticket back to the top.").
- Gemini's stat/flavor drafts are starting points; lanes have craft latitude within the locked
  facts above. Crypto note: the NFT quest is established canon — this extends it at the author's
  direction; the no-NEW-crypto rule refers to unsanctioned additions, not this.

## 6. Frat Bro NFT Quest Integration

- **Rescale (author-locked):** collection becomes **12 NFTs, 4 per city**; milestones move to
  **4 (cosmetic badge) / 8 (Wallet of Shame, +1 Charm) / 12 (Crypto Kings press-conference crash
  epilogue)**. Edit `Design/Quests/fratbronft.md` accordingly (surgical).
- **Debaucheryville's 4th:** "Meme Lord's First Selfie" (already listed ambiguously in the file)
  is formalized as Debaucheryville target #4. No new invention needed.
- **Sinfonia's four:** auction QR catalog, Bassline Opera House backstage terminal, latte-art AR
  filter, **Aaron's tractor token** (the §4 encounter). New file
  `Design/Quests/Location Specific/Sinfonia/nfthuntsinfonia.md` mirroring the Debaucheryville
  leg's pattern (`nfthuntdebaucheryville.md`), detailing all four acquisitions.
- **Publandia's 4th:** open slot, explicitly flagged as TBD-future-round in `fratbronft.md`
  (one line; this is a sanctioned open slot, not a placeholder defect).

## 7. NPC & Item Promotion Batch (template floors for everyone in the area)

Full 16-section profiles (new files, `Design/Character Profiles/SinfoniaNPCs/...`):
- **Black-Tie Backroom/**: `viktor_the_doorman.md` (`sinfonia_npc_viktor_doorman_01`),
  `madame_karten.md` (`sinfonia_npc_madame_karten_01`), `herr_falsch.md`
  (`sinfonia_npc_herr_falsch_01`), `graf_von_zittrig.md` (`sinfonia_npc_graf_von_zittrig_01`),
  `grafin_stille.md` (`sinfonia_npc_grafin_stille_01`), `siegfried_coat_check.md`
  (`sinfonia_npc_siegfried_coatcheck_01`). Existing embedded characterization in the location file
  is BINDING canon to harvest, not reinvent.
- **Haute Couture Haberdashery/** (carry-forwards promoted to full citizens):
  `monsieur_aiguille.md` (`sinfonia_npc_monsieur_aiguille_01`) and `the_night_porter.md`
  (`sinfonia_npc_night_porter_01`). Their established beats (Assessment Protocol, vitrine ceremony,
  "The mannequins are two.", pension math, post-quest callback) are binding canon. ID blocks also
  backfilled into `haute_couture_haberdashery.md`.
Item files (full permanent-item template): `Design/Inventory/items/shark_fin_item.md`
(`item_shark_fin` — Herr Falsch victory accessory) and `Design/Inventory/items/members_card_item.md`
(`item_members_card` — Backroom access). Existing mentions in the location file are binding.

## 8. Cleanup Lane

1. **Gregory eradication** across the six committed files (§1b list) — the round's first commit,
   so every other lane works from a Gregory-free base.
2. **Engine Requirements note:** add an explicit engine-requirements block (per-NPC first-completion
   tracking for the Chronicles payload rule; fixed-stake €500 collateral grant/removal for the
   Aaron encounter; scene-triggered item grants) to the quest files that need them
   (`nothingisgettingthrough.md` dev notes already flag the first — formalize; the new
   `thekingswerehumming.md` carries the second and third natively).
3. Backroom QA checklist "Habsburg" line corrected as part of Lane A's scrub.

## 9. Agent-Team Structure

- **Lane D — Gregory eradication + engine notes (§8)**: runs FIRST (fast, mechanical); commits
  before other lanes touch overlapping files. Owns the six §1b files for this purpose only.
  (`nothingisgettingthrough.md` engine-note edit rides in this lane to avoid double ownership.)
- **Lane A — Location completion (§2)**: the Backroom .md edits (scrub, de-Gregory, Aaron table,
  registrations) + PNG_Assets doc + 8 JSONs.
- **Lane B — NPC profiles (§3, §7)**: Aaron FIRST (Lane C quotes him), then the six Backroom
  promotions, then Aiguille + Night Porter (+ ID backfill edit in the Haberdashery file, AFTER
  Lane D's de-Gregory commit lands there).
- **Lane C — Encounter + items + NFT quest (§4, §5, §6)**: `thekingswerehumming.md`,
  `nfthuntsinfonia.md`, `fratbronft.md` edits, both new item files. Starts after Aaron's profile
  (quotes his dialogue verbatim from it).
- **Reviewer:** canon fidelity, tone (bros never self/scam-aware and believe they got the steal;
  Aaron/locals dignity intact), template compliance, **rule 1a sweep (nothing explains the joke)**,
  **Gregory = zero hits repo-wide in committed files**, world-names scan, no meta/personal
  references, lane discipline.
- Orchestrator commits per lane with explicit paths (concurrent-session checkout unchanged rules).

## 10. Deliverable Checklist

1. Lane D: 6 committed files de-Gregory'd + engine notes (§8)
2. `the_black_tie_backroom.md` completed pass (scrub, de-Gregory, Aaron table, registrations)
3. `PNG_Assets/the_black_tie_backroom_png_assets.md` + 8 Backroom JSONs (all parse)
4. `aaron_the_unflappable.md` (16 sections)
5–10. Six Backroom NPC promotions (16 sections each)
11–12. `monsieur_aiguille.md`, `the_night_porter.md` (+ ID backfill in Haberdashery file)
13. `thekingswerehumming.md` (full sidequest template)
14. `nfthuntsinfonia.md` + `fratbronft.md` rescale edits
15–18. Four item files: `candy_smokes_item.md`, `tractor_nft_item.md`, `shark_fin_item.md`,
   `members_card_item.md` (12 sections each)
