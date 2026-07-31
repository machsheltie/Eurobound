# Black-Tie Backroom & Aaron the Unflappable Implementation Plan (Agent-Team Edition)

> **For agentic workers:** Executed by an **agent team**: orchestrator (session lead), four implementer lanes with strict file ownership, one canon/tone reviewer. Each implementer receives ONLY its own lane section plus the Global Constraints. Source of truth: `docs/superpowers/specs/2026-07-30-black-tie-backroom-aaron-design.md` (~210 lines — implementers read it in full; its §1 rules override everything).

**Goal:** Complete the Black-Tie Backroom location (data suite + edits), ship Aaron the Unflappable and 8 more full NPC profiles, the scripted "Kings Were Humming" encounter quest, 4 item files, the NFT-quest rescale to 4/8/12 — and eradicate Gregory from all committed content first.

**Architecture:** Lane D (Gregory eradication + engine notes) runs FIRST and commits before any other lane starts. Then Lanes A (location suite) and B (NPC profiles, Aaron first) run parallel; Lane C (encounter/items/NFT) starts once Aaron's profile is committed. Reviewer sweeps the whole batch; one fix wave; re-review; land on main.

**Tech Stack:** Markdown design docs against repo templates; JSON validated with PowerShell `ConvertFrom-Json`.

## Global Constraints

- **Spec §1 rules are supreme (read them verbatim in the spec before writing a word):**
  - **1a Trust the Player:** nothing explains the joke, ever. No truth-tellers, meta-narrators, or fourth-wall devices. Dramatic irony by STAGING, never STATEMENT. Content that explains the joke is a defect.
  - **1b Gregory is dead:** no file may reference Gregory. Any lane touching a file containing him removes him: each Gregory line is CUT or becomes a plain understated Bradley line with the explanatory observation DELETED. Never transfer his truth-telling function anywhere.
  - **1c Full-strength satire:** MA-rated adult comedy; never soften, sanitize, or tame. Only the author's own boundaries apply (no graphic sexual content — implication/cutaway; satire targets bros/tourist psychology, never marginalized groups; women keep dignity).
- **Carried rules:** bros NEVER self-aware, NEVER scam-aware (+ steal corollary: they always believe THEY got one over; the seller always knows exactly what they have); world names only (Sinfonia, never Vienna/Viennese/Habsburg); never "spring break"; Y2K-era cringe; templates are floors not ceilings (NPC=16 H2s, permanent item=12 H2s, sidequest=every section).
- **Aaron privacy (binding):** all content 100% diegetic; nothing in any file may hint at real-world inspiration.
- **Aaron tone (binding):** he is a winner-operator, dignity fully intact, never the joke; his vibes-based play WORKS and is never explained (rule 1a). The joke is the bros misreading him.
- **Canonical IDs (verbatim everywhere):** location `sinfonia_operahouse_blacktie_backroom_01`; quest `sinfonia_sidequest_the_kings_were_humming_01`; encounter event `blacktie_event_kings_were_humming_01`; NPCs `sinfonia_npc_aaron_unflappable_01`, `sinfonia_npc_viktor_doorman_01`, `sinfonia_npc_madame_karten_01`, `sinfonia_npc_herr_falsch_01`, `sinfonia_npc_graf_von_zittrig_01`, `sinfonia_npc_grafin_stille_01`, `sinfonia_npc_siegfried_coatcheck_01`, `sinfonia_npc_monsieur_aiguille_01`, `sinfonia_npc_night_porter_01`; items `item_candy_smokes`, `item_tractor_nft`, `item_shark_fin`, `item_members_card`.
- **Canonical verbatim quotes (copy exactly; connective dialogue around them has craft latitude within the tone rules):**
  - Chadwick: "Look at this guy. He's drinking melted ice cream and chewing on sugar sticks. He's weak."
  - Lord Pilsner: "Make the bet big. Show him what American capital looks like."
  - Aaron (vibes speech): "You guys are calculating numbers. You're looking at the board like it's a math test. Poker isn't math, bro. You gotta FEEL the turn. You gotta let the felt speak to you."
  - Aaron (reveal): **"The kings were humming, man. They wanted to stretch their legs."**
  - Aaron (candy smokes): "Here. Take one. It helps with the hand jitters when you lose your shirt. Don't smoke it, just bite the end off. You want a hit of my White Russian to wash it down? No? Suit yourselves."
  - Aaron (NFT): "It's on the chain. Digital land, baby. She Thinks My Tractor's Sexy. Limited drop. Mint #42. Hold onto that—that's your ticket back to the top."
  - Aaron (exit): **"No cab vouchers, bro. But if you walk fast enough, you stay warm. Good luck with the felt next time!"**
  - Viktor (existing canon, unchanged): "Döner is not accepted."
- **Encounter mechanics (author-locked):** pure spectator cinematic — poker betting UI NEVER opens at Aaron's table; player input limited to 2–3 pick-which-terrible-line beats, all paths identical outcome; stake is exactly the €500 door-collateral chips (gold above €500 untouched; under-€500 parties bounced by Viktor); one-time scene, Aaron ambient at his table forever after, never a playable opponent; scene visually distinct from the room's real playable poker tables.
- **Git discipline:** a concurrent session shares this checkout. Implementers run NO git commands; the orchestrator commits per lane with explicit paths only.
- **Surgical edits on existing files** — never rewrite or reformat untouched sections.

## File Ownership Map

| Lane | Creates | Edits |
|---|---|---|
| D (first) | — | `Design/Quests/Location Specific/Debaucheryville/nothingisgettingthrough.md`, `Design/Inventory/items/gold_circle_coin_item.md`, `Design/Inventory/items/leopard_print_thong_item.md`, `Design/World Design/Sinfonia/haute_couture_haberdashery.md` (de-Gregory ONLY), `Design/World Design/Debaucheryville/the_participation_trophy.md`, `Design/Quests/greatdonerdebate.md` |
| A | `Design/World Design/Sinfonia/PNG_Assets/the_black_tie_backroom_png_assets.md` + 8 JSONs `Design/World Design/Sinfonia/{core,npcs,interactions,environment,items,events,location_nodes,sprite_mapping}/the_black_tie_backroom_*.json` | `Design/World Design/Sinfonia/the_black_tie_backroom.md` |
| B | 9 profiles under `Design/Character Profiles/SinfoniaNPCs/` (paths in Lane B) | `Design/World Design/Sinfonia/haute_couture_haberdashery.md` (ID backfill ONLY, after Lane D's commit) |
| C | `Design/Quests/Location Specific/Sinfonia/thekingswerehumming.md`, `Design/Quests/Location Specific/Sinfonia/nfthuntsinfonia.md`, `Design/Inventory/items/candy_smokes_item.md`, `Design/Inventory/items/tractor_nft_item.md`, `Design/Inventory/items/shark_fin_item.md`, `Design/Inventory/items/members_card_item.md` | `Design/Quests/fratbronft.md` |

Haberdashery file is the ONE shared file: Lane D touches it first (de-Gregory), Lane B touches it last (two ID blocks). No other overlap.

---

### Lane D: Gregory Eradication + Engine Notes (RUNS FIRST)

**Read first:** spec §1a/§1b/§8; the Gregory-line inventory below.

- [ ] **Step 1: De-Gregory the six files.** Find every site with `Select-String -Pattern "Gregory" <file>`. Apply spec §1b: CUT the line, or make it a plain understated Bradley line with the explanatory observation deleted. Specific known sites:
  - `nothingisgettingthrough.md`: Oz song verse 2 (Gregory sings the response "And a plan is what we are!" + Bradley's echo line) → rewrite so BRADLEY sings the response himself (the line "And a plan is what we are!" is absurd sincerity, not explanation — it may stay as Bradley's); the verse 2 intro line about Gregory being "vocally the most committed performer"; the montage line "Gregory's sitting this one out"; post-credits staging if present. Preserve song meter and section order (11/11 H2s).
  - `gold_circle_coin_item.md`: "Gregory has aspired to this his entire life." reaction row and any others → reassign or cut per rule.
  - `leopard_print_thong_item.md`: any Gregory reaction rows → same.
  - `haute_couture_haberdashery.md`: "Bradley: 'Gregory believes the correct term is 'elevated.''" → rewrite as plain Bradley (e.g. a one-word deadpan) with no explanatory function. De-Gregory ONLY — touch nothing else in this file.
  - `the_participation_trophy.md`, `greatdonerdebate.md`: whatever sites grep finds → same rule.
- [ ] **Step 2: Engine Requirements note** in `nothingisgettingthrough.md` Development Notes: formalize the existing flag into a titled "Engine Requirements" block (per-NPC first-completion tracking for the Chronicles payload rule). One block, surgical.
- [ ] **Step 3: Validate.** `Select-String -Pattern "Gregory"` returns ZERO hits across all six files; quest file still 11/11 template H2s; no other content changed.
- [ ] **Step 4: Report DONE** (orchestrator commits; other lanes are then cleared to start).

### Lane A: Black-Tie Backroom Completion

**Read first:** spec §2; `the_black_tie_backroom.md` in full (it is binding canon to complete, not rewrite); one complete sibling suite for schema (`bassline_opera_house` — its 8 JSONs + PNG_Assets doc); `Templates/location_validation_template.md`.

- [ ] **Step 1: Surgical .md edits:**
  - Scrub world-name violations: "Habsburg-era gambling traditions" (~line 122) and QA checklist "Imperial history (Habsburg gambling traditions)" (~line 462) → Sinfonia-world equivalents (e.g. "old-imperial gambling-salon traditions" — no real dynasties/places). Grep the whole file for Vienna/Viennese/Habsburg and scrub all hits (there are several "Viennese Wheel"-style names — rename in-world, e.g. "Sinfonian Wheel").
  - De-Gregory the file's 4 dialogue sites per spec §1b.
  - Add **Aaron's Corner Table** as a named main-floor zone: felt-covered corner table, scene trigger for `blacktie_event_kings_were_humming_01`, explicitly visually distinct from the playable poker tables, Aaron ambient there post-encounter. Pointer to his profile and to `thekingswerehumming.md` — do NOT restate his characterization or the scene beats.
  - Register in the relevant existing sections: the two grantable items (`item_candy_smokes`, `item_tractor_nft` — granted by the encounter, not vendor stock), the quest hook, and NPC-profile pointers for the six promoted NPCs (file paths only).
- [ ] **Step 2: Create `PNG_Assets/the_black_tie_backroom_png_assets.md`** following the sibling PNG doc's format, harvesting the .md's existing "PNG Asset Requirements Summary" (34 PNGs) as the base and adding: Aaron's sprite sheet — canonical filename `aaron_the_unflappable.png` (velvet jacket, tumbler, candy-cigarette ritual frames incl. the crunch; Lane B's profile uses the same filename), his corner-table zone art, and the two item icons. Every referenced PNG must be specced.
- [ ] **Step 3: Create the 8 JSONs** following each sibling file's schema exactly (same top-level keys, entries shaped like neighbors): core (identity/access incl. €500 collateral + entry conditions), npcs (7 registrations: the six promoted + Aaron, presence-only with `full_profile` pointers — no characterization), interactions (the encounter as a staging stub: trigger + phase list carrying ONLY the plan's canonical quotes, pointer to the quest file), environment (atmosphere/particles), items (house items + the two grants marked scene-granted), events (`blacktie_event_kings_were_humming_01` registration), location_nodes, sprite_mapping (incl. Aaron's sheet from Step 2).
- [ ] **Step 4: Validate.** All 8 JSONs parse (`Get-Content <f> -Raw | ConvertFrom-Json`); zero hits for Gregory/Vienna/Viennese/Habsburg in the .md; every sprite named in sprite_mapping exists in the PNG doc.
- [ ] **Step 5: Report DONE.**

### Lane B: Nine NPC Profiles (Aaron FIRST — blocks Lane C)

**Read first:** spec §3, §7; `Templates/NPC_Profile_Template.md`; `the_black_tie_backroom.md` (binding embedded canon for the six promotions); `haute_couture_haberdashery.md` + `nothingisgettingthrough.md` (binding canon for Aiguille and the Night Porter); house style: `Design/Character Profiles/DebaucheryvilleNPCs/Bohemian Riviera/janek_sykora.md`.

- [ ] **Step 1: `SinfoniaNPCs/Black-Tie Backroom/aaron_the_unflappable.md` FIRST** (all 16 sections; report immediately on completion so Lane C can start). Requirements from spec §3: rumpled velvet dinner jacket; double White Russian in crystal tumbler; the candy-cigarette ritual (stir → dramatic drag → loud CRUNCH → fresh one from a worn carton that never empties; recently quit smoking); junk-food connoisseur; squirrely dopamine-chasing vibes player; won big last year on pocket kings; genuine unforced kindness after cleaning someone out; ambient rotating vibes-dialogue for post-encounter (write 6+ rotating lines); sprite sheet table (matching the filenames Lane A specs — coordinate via the canonical name `aaron_the_unflappable.png` main sheet). His verbatim quotes from Global Constraints appear in his Dialogue section. Dignity intact; vibes play works, never explained; 100% diegetic.
- [ ] **Step 2: The six Backroom promotions** (16 sections each) — harvest the location file's embedded characterization as BINDING (Viktor's politely-threatening doorman voice + existing dialogue; Madame Karten's grandmother-warmth/shark-instinct; Herr Falsch's cheat secret, tells, boss mechanics pointer; Graf von Zittrig's cufflink tell; Gräfin Stille's speaks-only-in-bets; Siegfried's €50,000/10-years backstory, couchsurf scene, "The only winning move is not to play. But we both know you'll play anyway."). Files: `viktor_the_doorman.md`, `madame_karten.md`, `herr_falsch.md`, `graf_von_zittrig.md`, `grafin_stille.md`, `siegfried_coat_check.md` in `SinfoniaNPCs/Black-Tie Backroom/`.
- [ ] **Step 3: The two Haberdashery citizens** in `SinfoniaNPCs/Haute Couture Haberdashery/`: `monsieur_aiguille.md` (Assessment Protocol, Aiguille=needle pun, vitrine ceremony, "It is not for sale. It is for aspiration.", the price-reveal beats, PATH A errand role — all binding from the shop file + quest file) and `the_night_porter.md` ("The mannequins are two.", three-years-from-a-pension knee math, walks on, post-quest callback compliment — binding from the quest file; he KNOWS and indulges, which is never stated aloud, per rule 1a).
- [ ] **Step 4: ID backfill edit** in `haute_couture_haberdashery.md` (ONLY after Lane D's commit has landed there — verify the file contains no "Gregory" before editing): add formal NPC ID lines for `sinfonia_npc_monsieur_aiguille_01` and `sinfonia_npc_night_porter_01` at their existing character entries, matching the repo's ID-block format. Nothing else.
- [ ] **Step 5: Validate.** Nine files × 16 H2s matching the template in order; zero Gregory/real-world-place hits; report DONE (with Step 1 reported early).

### Lane C: Encounter Quest + NFT Integration + Four Items (starts after Aaron's profile commits)

**Read first:** spec §4, §5, §6; `Templates/sidequest_template.md` + `Templates/permanent_item_template.md`; `Design/Character Profiles/SinfoniaNPCs/Black-Tie Backroom/aaron_the_unflappable.md` (quote him verbatim); `Design/Quests/Location Specific/Debaucheryville/nfthuntdebaucheryville.md` (pattern for the Sinfonia leg); `Design/Quests/fratbronft.md`; house style: `Design/Quests/Location Specific/Debaucheryville/bacchanusbeachbeatdown.md`.

- [ ] **Step 1: `thekingswerehumming.md`** (new folder `Design/Quests/Location Specific/Sinfonia/`; full sidequest template). The nine beats from spec §4 with the canonical quotes; the 2–3 player pick-a-terrible-line moments (write all options — every option a different flavor of unearned Casino-Royale swagger; identical outcome); the bros' "expertise" showcase (misread tells narrated aloud, Casino Royale cited as credentials — per rule 1b Bradley's baccarat correction is GONE; find another staging for their wrongness that no character explains); Viktor bounce pre-beat; €500 collateral stake mechanics; both item grants with `[ACQUIRED: ...]` lines; asset-rich exit reframe; Engine Requirements block (fixed-stake collateral grant/removal, scene-triggered item grants, one-time-scene flag + ambient-Aaron state). NO betting UI ever; scene visually distinct from playable tables — stated as a binding staging rule.
- [ ] **Step 2: `nfthuntsinfonia.md`** mirroring the Debaucheryville leg's format: Sinfonia's four acquisitions — auction QR catalog, Bassline Opera House backstage terminal, latte-art AR filter, Aaron's tractor token (pointer to the quest file for the acquisition scene; do not restate it).
- [ ] **Step 3: `fratbronft.md` surgical edits:** milestones → 4 (cosmetic badge) / 8 (Wallet of Shame, +1 Charm) / 12 (Crypto Kings press-conference crash); "Meme Lord's First Selfie" formalized as Debaucheryville target #4; Sinfonia section listing its four; Publandia line noting 3 defined + 1 open slot (sanctioned TBD, flagged as future-round).
- [ ] **Step 4: Four item files** (12 template sections each): `candy_smokes_item.md` (`item_candy_smokes`; permanent never-empty carton; bite-one use effect = small short comedy Bravado buff + chalk ring visual; "+4% Perceived Confidence" gag framing; granted at encounter beat 8), `tractor_nft_item.md` (`item_tractor_nft`; the locked description facts from spec §5.2; worth €0 everywhere; advances NFT hunt; Kahlúa + fresh-cut grass), `shark_fin_item.md` (`item_shark_fin`; Herr Falsch victory accessory per location canon), `members_card_item.md` (`item_members_card`; Backroom access alternative per location canon). Gemini drafts are starting points; craft latitude within locked facts.
- [ ] **Step 5: Validate.** Quest file: every sidequest-template H2 in order; four item files 12/12; `fratbronft.md` edits additive/surgical; zero Gregory; all canonical quotes byte-identical to the plan's. Report DONE.

---

## Review & Landing (orchestrator)

- [ ] Commit Lane D first; clear other lanes; commit each on DONE (explicit paths, session trailers).
- [ ] Reviewer over the whole batch: spec §1 rules sweep (nothing explains the joke; Gregory zero hits in committed files; no softening/sanitizing), canon fidelity (verbatim quotes byte-identical across copies), tone (bros never self/scam-aware + steal corollary; Aaron/locals dignity intact; no meta/personal references), world-names scan (Vienna/Viennese/Habsburg/Prague/Dublin = zero), template compliance (16/12/full-sidequest), JSON validity, lane discipline, cross-file consistency (Aaron quotes profile↔quest↔interactions stub; item grants quest↔items JSON↔item files).
- [ ] One fix wave (resume owning implementers), scoped re-review, then land: fetch origin, fast-forward main, push.
