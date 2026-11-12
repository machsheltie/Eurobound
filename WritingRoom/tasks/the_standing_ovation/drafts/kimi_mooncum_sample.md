# Kimi — Tony420's 50-MoonCum free sample

**Scope:** exact replacement text for `final.md` §11, plus the Appendix D3 item 2 replacement and the Appendix C2/C3 state note. Nothing else is revised.
**Authority:** author desk ruling, 2026-11-10 — "Tony420 airdrops exactly 50 MoonCum as a 'free sample' right before pitching the pill". Canon delivery rule: `design/economy/icq_airdrops.md` §1.4.
**Reviewers:** GLM — existing-hook gating, deposit/purchase state and save/load; Aion — Tony420 voice and continuity.

---

## 1. Replacement for `final.md` §11 in full

## 11. Optional Tony420 ICQ window — after TROUSER SNAKE, before D5

*The venue-door FREE Wi-Fi decal is PROPOSED dressing only; the documented Sinfonia hostel-lobby hotspot is the CANON fallback. The evening never advances on a timer while the player is using ICQ. Reachable after ANY D3 outcome — the pill route is not gated on the paid drink branch.*

*The vintage ICQ "Uh-oh!" arrives.*

```
Tony420:
free sample. 50 mooncum. check ur assets
dont spend it all in one place
u can only spend it here
```

*Bagholder Assets receives exactly **50 MoonCum696969 ($MCUM)**. The row renders flat grey with its plain quantity and denomination. No accept prompt, item-get jingle or value commentary.*

**PILSNER:** He fronted us, Chadwick. We're in business.

```
Tony420:
heard u been at the opera. got something 4 the high notes 50 mooncum
xanax flintstones. chewable. grape
u want the purple one trust me
```

**Price: 50 MoonCum696969, crypto only, payable to Tony420 only (CANON author ruling q10: A).** No SOVS alternative. The author-ruled free sample supplies exactly the purchase amount before the pitch. If the player already holds AD-04's 8.4M units, the sample still arrives and is still exactly 50; the purchase deducts 50 and leaves the rest untouched.

- **Decline / close without buying:** `ur loss. theyre shaped like dinosaurs`
- **Purchase complete:** `sent. dont take 2` / `2 is a different product`
- **Sales close:** `pleasure doing business. tell ur friends. especially the one with the camera` / `he looks like he needs vitamins`

*The old `no coin no vitamins. wallet or walk` branch is not used in this window: when the encounter fires, the sample has already supplied the exact price. That line remains available to Tony420's other appearances.*

*Access conditions (DESIGN TARGET, existing hooks only): this is a deterministic, one-shot quest delivery, not an entry in the random AD-01–AD-12 selection. On the first valid §11 connection after TROUSER SNAKE and before D5, it requires the revealed Bagholder Assets tab (`has_inspected_first_crypto_trash`) and reads any existing `tony420_unlocked` contact requirement rather than bypassing it. The quest grants neither the reveal flag nor the contact unlock. If either requirement is absent, this encounter does not fire and no partial deposit occurs; the player can establish access through the existing certificate-inspection and contact routes, then return before D5 without a timer or any other lost content. Once those existing conditions are met, the sample is guaranteed on every save, regardless of D3 branch or later D5 choice.*

*Delivery uses the existing ICQ pop-up, `airdrops_delivered` and `bagholder_assets` hooks. The quest record `standing_ovation_tony420_sample` is appended to `airdrops_delivered` and the +50 deposit commits with it, atomically, before the pitch; it fires at most once per save and is never offered to the random airdrop selector. A save/load after delivery but before purchase preserves both the one-shot record and the deposited 50, so the route cannot be lost or duplicated. Purchase deducts exactly 50 with the item grant. MoonCum remains spendable with Tony420 only, so it cannot have been spent elsewhere first. Declining keeps the coins and every non-pill route.*

**Use — Bradley eats the purple one.** The TROUSER SNAKE banner ends mid-sip. `sinfonia.ovation.flintstone_xanax_active` is set (DESIGN TARGET): recurrence and Bradley's sexual performance are blocked until the next in-game morning, reliably, with no roll, across save/load and scene changes.

**PILSNER:** Vitamins. Good. You're depleted.

**CHADWICK:** Supplement journey.

*Nobody explains why it works. Tony420 does not diagnose anyone. Bradley gives no medical lecture. Flintstone Fentanyl is a separate product with no assigned effect. Item inspection text: **"Grape. Shaped like a dinosaur."** (`flintstone_vitamins`: consumable, `usable: true`, `heal_hp: 0`, `heal_bravado: 0`; consumption IS the trigger. PROPOSED registration, Appendix C.)*

---

## 2. Replacement for Appendix D3 item 2

2. **SETTLED (author, via the desk, 2026-11-10): "Tony420 airdrops exactly 50 MoonCum as a 'free sample' right before pitching the pill."** §11 delivers exactly +50 MoonCum696969 immediately before his existing pitch, once per save, on every path that meets the existing wallet/contact access conditions. The pill route no longer depends on AD-04 or random airdrop luck; an existing AD-04 balance does not change the sample size. The hidden-tab and contact requirements are read, never granted or bypassed. The performer and decline routes remain complete regardless, and the pill is never a progression gate. The matching canon rule is already in `design/economy/icq_airdrops.md` §1.4.

---

## 3. Appendix C2/C3 state note

**No new boolean and no change to the eight-flag count.** Add this bullet immediately after C3's `footage_posted` bullet:

- **Tony420's free sample uses existing economy state only:** `airdrops_delivered` gains the one-shot string `standing_ovation_tony420_sample`; its presence is the duplicate-delivery guard and the only new reader. `bagholder_assets` receives exactly +50 MoonCum696969 in the same committed delivery. `has_inspected_first_crypto_trash` and any applicable `tony420_unlocked` contact are prerequisites read from existing systems, never set by this quest. No C2 item row is needed for the currency deposit; `flintstone_vitamins` is unchanged.

**Splice note for the moderator:** the §11 replacement above removes the `[MOONCUM SOURCE: PENDING AUTHOR]` marker. No marker or replacement is supplied for any other passage.
