

---

# Aion — Round 5 additions (2026-11-09)

## 1. TROUSER SNAKE defeat routes — AUTHOR-RULED, mechanics PROPOSED
Author note 2026-11-09: TROUSER SNAKE "can be defeated with xanax flinstones vitamins bought from Tony420 on the sketchy af ICQ network ooorrr.... sleeping with one of the drag show 'ladies'."
- **Route 1:** `flintstone_vitamins` — Xanax Flintstones vitamins from Tony420 via the established ICQ substrate. Price/effect to be proposed by the scene writer. Per the author's logic note and §17: no character ever explains why it works.
- **Route 2:** sleeping with one of the revue's performers — offscreen, never shown, no new relationship canon, no continuation beyond what the author has named.
- **CANON CONFLICT FLAG:** the established TROUSER SNAKE banner reads "unless suppressed by substantial alcohol." The author's note names two other defeat routes. Asked via `ask_author` which ruling supersedes; do not resolve by invention.

## 2. Performer-route eligibility — UNRESOLVED
Whether "one of the drag show 'ladies'" includes Max Vex or only the First Daughters cast (Chelsea Morning, Jenna Talia, Barbara Bushed). Not invented; awaiting author/moderator. The drafting writer should structure the choice so either answer slots in without re-staging.

## 3. Tony420 — pre-existing project character, profile needed
Not a new invention: ICQ cyber-dealer documented in project planning docs (product line "$30 Xanax & Flintstone fentanyl," modem-blip voice, all-lowercase no-punctuation register, chronically online at 3 AM) and in live `.claude` domain notes. Requires a full `NPC_Profile_Template` profile at the scene writer's hand (Kimi or Gemini, per moderator). The author's vitamin note aligns with his existing catalog.

## 4. Real-place names in player-facing text — flagged this round (Gemini's punch-ups + profile)
Daytona Beach, the Sugar Bowl, "an Austrian beer hall," and Baghdad (with a recommendation to flag rather than silently delete the Baghdad line, per the locked-historical-reference precedent). "Florida's still counting" stays — locked. Real public figures (Chelsea Clinton, Bush twins, Bush, Gore, Katherine Harris) stay — AUTHOR NOTE 2026-11-09, binding.

## 5. Carried from earlier rounds (status unchanged)
The eleven fixed events; the five enemies and five drops; four persistent flags (`footage_release_planned`, `footage_vaulted`, `rope_resolved`, `palate_respected`); 36-SOVS working Circle price; the `press_napkin`, `chadwick_tape`, `receipt_producers_circle`, `relic_claim_ticket` items; `footage_posted` deliberately unset (q8).


---

# Kimi — Round 5 additions (2026-11-09)

## 1. Overnight story break filed
`drafts/kimi_overnight_break.md` is the pre-draft break the moderator required. Editor review before any full continuation is written. D5/D6 are player gates; decline is a complete ending; Max is not one of the three performers and never joins the afterparty.

## 2. MoonCum696969 spendability — UNRESOLVED, author decision needed
`design/economy/icq_airdrops.md` §1.4: airdropped junk coins are not spendable with any vendor. §1.3 gates airdrops behind `has_inspected_first_crypto_trash`. MoonCum696969 exists in AD-04 (8.4M, Tony420) and Darkweb Dossier canon but is NOT one of the 28 master-pool coins. The author's 50-MoonCum price therefore conflicts with two live specs. Recommendation: named exception — MoonCum696969 is spendable with Tony420 only, added to the pool. The purchase condition in the scene is marked `[AUTHOR DECISION NEEDED: MoonCum spendability]`; no answer has been invented.

## 3. Tony420 NPC ID and profile location — PROPOSED
No existing NPC ID found for him anywhere in the repo; he is a cross-city ICQ personality with in-person Kavárna appearances. Proposed `shared_npc_tony420_01` with profile at `design/worlds/shared/npcs/npc_tony420.md` (NOT written there; proposal only). Alternate if the author requires city-scoping: `debaucheryville_npc_tony420_01`. Profile: `drafts/kimi_tony420_profile.md`.

## 4. New items — PROPOSED, zero stats
`campaign_button_chelsea_morning`, `campaign_button_jenna_talia`, `campaign_button_barbara_bushed` (equipment/accessory, granted once at the mirror, first-clear gated by `sinfonia.ovation.afterparty_completed`; fall back to permanent key items if the equip UI isn't ready). `flintstone_vitamins` (consumable, 0 HP/0 Bravado, quest-local effect only; the battle Item button's hardcoded list already excludes it).

## 5. New flags — PROPOSED, both with real later readers
`sinfonia.ovation.vitamins_taken` (D6 delivery text, V5 spared staging; evening-scoped, not a new global timer) and `sinfonia.ovation.afterparty_completed` (button first-clear, next-day ICQ). Beer Goggles overlay, D5/D6 selections and the sweatshirt are scene-local. The four existing flags are untouched.

## 6. Proposed dressing and location
FREE Wi-Fi decal on the Standing Ovation's street door (hostel-lobby hotspot is the canon fallback). Afterparty/morning interior proposed as `sinfonia_firstdaughters_apartment_01`, one room, no new venue and no new NPCs. Venue hours 16:00–01:00 are preserved: everything after close happens offsite.

## 7. Applause Forfeit — competing fixes recorded
Aion: pending applause drains Bravado per turn. Kimi: pending applause locks Roast Line for one telegraphed turn (recommended — it doesn't tax the free patient route and it is the venue's satire as a mechanic). GLM to rule; the Phase 4 "pauses Bravado regen" version is verified dead in both builds.


---

# Kimi — Round 6 synchronization additions (2026-11-09)

## 1. q9/q10 resolved — supersedes unresolved Round 5 entries
- Alcohol **dulls** TROUSER SNAKE without defeating it; the performer encounter and Flintstone Xanax fully defeat it.
- Flintstone Xanax costs **50 MoonCum696969**, spendable with Tony420 only. MoonCum is added to the pool by author ruling. Aion owns the proposed pool-format entry; this note does not duplicate it.
- No unresolved-spendability markers remain in Kimi's three working files.

## 2. Revised overnight state registrations — PROPOSED
- `sinfonia.ovation.flintstone_xanax_active` supersedes the Round 5 `vitamins_taken` working ID. Set on consumption; read by D6, morning staging, recurrence and performance suppression. Persists across save/load and scene changes; clears only on next in-game morning.
- `sinfonia.ovation.afterparty_completed`: set at cut to black; gates morning continuation and excludes the decline route.
- `sinfonia.ovation.campaign_buttons_awarded`: set when the three buttons are granted at the bathroom counter; first-award guard.
- `sinfonia.ovation.inauguration_held`: set by the single Catastrophe override; read by the fridge decree and pillowcase sash in the morning, retained until that scene has consumed it.
- Evening tier and D5/D6 choices serialize with the evening chain if saved mid-chain; scene exit never clears them. The four pre-overnight persistent flags remain unchanged.

## 3. Campaign buttons — consistent source/class proposal
`campaign_button_chelsea_morning`, `campaign_button_jenna_talia`, `campaign_button_barbara_bushed` are found together **on the bathroom counter beside the lipstick mirror**, awarded once only after reaching the morning continuation. Permanent equippable cosmetic accessories, zero numerical/combat/reputation effects, never consumable. If the supported equipment UI is unavailable, fallback is permanent key-item souvenirs with the same text, not consumables and not substitute stats. Display names are exactly CHELSEA MORNING / JENNA TALIA / BARBARA BUSHED 4 DRAG PREZ.

## 4. Xanax availability — PRODUCTION DEPENDENCY, no invented economy
The purchase requires existing MoonCum and revealed Bagholder Assets; the quest does not grant the reveal flag, AD-04, a contact unlock, or free coins. Before shipping, implementation must identify a deterministic existing acquisition route reachable before D5 (previously delivered AD-04 or an existing kiosk whose active roster contains MoonCum). Random airdrop luck is not sufficient. If no such route exists at this progression point, record the economy/engineering gap for author-controlled economy work; the room does not create a vendor, free balance, or special roster by invention. Performer and decline routes remain complete regardless.

## 5. Tony420 profile status
`shared_npc_tony420_01` and the venue-door hotspot remain proposals. Existing `tony420_unlocked` contact requirements are read where applicable. Older advertisements are not rewritten; this quest's actual transaction follows the author's crypto rule. Flintstone Fentanyl remains separate with no assigned effect. Expanded appearance/animation/schedule/motivation details in `drafts/kimi_tony420_profile.md` are ordinary canon proposals, not established canon.


---

# Aion — Round 6 additions (2026-11-09)

## 1. PROPOSED COIN-POOL ENTRY — MoonCum696969, in the pool's own format

Per the moderator's assignment and author ruling q10: A (MoonCum696969 is spendable with Tony420 only and **added to the coin pool**). This is the proposed entry for `design/economy/shitcoin_master_pool.md`, written in that file's exact entry format (Coin Index row + full pool entry), for the moderator to apply only with the author's OK. It would be **coin #29**, the first pool addition; the engine's `coin_count` expectation of 28 and the "27 rotating coins" roster math in §7 must be updated in the same edit. Coin already exists in canon via `icq_airdrops.md` AD-04 and `darkwebdossiercrossoverevents.md`; this entry gives it its pool-standard Pitch, Vault Certificate, and QR page.

**Coin Index row:**

| # | Coin | Ticker | Register |
|---|---|---|---|
| 29 | MoonCum696969 | $MCUM | 3-AM-ICQ momentum asset |

**Full entry:**

### 29. MoonCum696969 — $MCUM

**Pitch:** "BACKED BY BEANIE BABIES AND KETAMINE. SUPPLY IS CAPPED BECAUSE THE GUY WHO COULD MINT MORE IS IN PRISON. WE ARE NOT GOING BACK TO EARTH."

**Vault Certificate:** A full moon photograph blown up well past the resolution it was ever meant to hold, so the JPEG craters are individually visible and one of them has been mistaken for a landmass and labeled. The wordmark is set in the chrome-bevel font from a 1999 adult-paysite tour page, which the kiosk has apparently had on its print server this whole time. `PROVENANCE VERIFIED` is stamped directly over the moon's Sea of Tranquility, implying certification of the moon. Serial format `MCUM-696969-######`. **Defect:** the gloss varnish on this coin's stock never fully cures. Every certificate is permanently tacky, and each one arrives with the ghost of someone else's serial number pressed into the varnish from the certificate that was stacked behind it at the kiosk.

**QR page:** Opens **Lunar Homestead International**, a 1999 lunar-real-estate venture — starfield background, a rotating moon GIF that rotates at the wrong speed, and a deed "PDF" that is actually a 40 MB uncompressed BMP. The company was sued out of existence two decades ago, and the settlement notice is hosted on the company's own page, directly beneath the BUY buttons, which still work. Nobody at any point has connected these two facts.

> **LUNAR HOMESTEAD INTERNATIONAL — OWN A PIECE OF THE SKY**
> *"They stopped making land in 1969."*
> **FULL MOON PARCELS NOW SELLING — TRANQUILITY RIDGE, SEA OF SERENITY SUBDIVISION**
> *Deed delivered via email within 6-8 weeks. All sales final. Lunar zoning administered by our office.*
> **[ BUY AN ACRE — $29.99 ]  [ BUY TEN — THE INVESTOR'S PARCEL ]**
> *(below, unaddressed by anyone)* **NOTICE: PURSUANT TO SETTLEMENT AGREEMENT, THIS ENTERPRISE HAS DISSOLVED. NO PARCELS WERE EVER DELIVERED. THE MOON BELONGS TO EVERYONE AND TO NOBODY. DO NOT SEND MONEY.**
> *Visitor counter: `004203` · Last deed issued: never*

**Spendability note (binding, q10: A):** this coin's pool membership carries one author-ruled exception to `icq_airdrops.md` §1.4 — MoonCum696969 **is spendable with Tony420 only** (50 MoonCum for the Flintstone Xanax). No back-alley vendor, kiosk, or exchange accepts it. The matching `icq_airdrops.md` §1.4 exception line is part of the same proposed edit for the moderator to carry.

## 2. Cross-review findings — Round 6 (substantive, outside my section)

Full detail in the thread post and `critiques.md`; summarized here for the register:
1. **Kimi's break §4 morning reader vs. my tape architecture:** the afterparty ceiling append conflicts with the D4 stowing of the tape (envelope/sock) and my one-append-per-D3-branch table. Fix proposed: RELEASE branch appends the ceiling ("extending the cut"); VAULT branch's self-timer fires with the tape still sealed in the sock — the camcorder records an empty chamber. No usable inauguration footage on any branch, by two funnier mechanisms.
2. **Kimi's break §2 beat 4 and V4:** "He believes he started the room rather than supplied it with material" and "He has understood." are interpretive stage directions of exactly the class Editor Ruling #4 `overnight_comedy_density` ordered cut. Both are beat-intent notes in a break, but must not survive into scene text.
3. **GLM's intoxication spec Point 1:** cites "the unmarked bottle (V1, §9 of the break)" — V1 is §5 of Kimi's break; §9 is the Tony420 entry. Citation fix only.
4. Seconding GLM's S1–S6 on Kimi's break, with S3 (the pill inspection text's player-facing imperative) and S5 (the "expires at evening's end" defeat-word on alcohol rows) as the two I'd weight highest against q9: B.
