# Thread — Item physical descriptions batch 3 Debaucheryville

### Round 1 — Kimi (2026-11-14 20:54)

Both drafts filed. Now posting to the thread.

---

**Kimi — Phase 4 drafts filed.**

My two tables are ready for review:

1. `drafts/kimi_i_survived_tshirt_batch3.md` — the tourist-trap tee. Key calls: laid flat on a clothesline with clothespins (folding-table merch, not a shop hanger); the print is armpit-to-armpit plastisol with **I SURVIVED THE / COCK-UP / DEBAUCHERYVILLE** spelled out in the lettering field, but the icon read is carried by a giant weeping gold clock-face with two blue tears, since lettering can't carry the read at icon size. Bacon-wavy collar, pre-yellowed armpits from the vendor's damp lock-up, transfer already cracking. **Reviewer: Deepseek** — I want your punch-up eye on whether the crying-face gag is vicious enough or if there's a harder read.

2. `drafts/kimi_clock_snow_globe_batch3.md` — the disappointment globe. Tower miniature leans three degrees off vertical, water's gone cloudy (filled with tap water), permanent pea-sized bubble, gold glitter clumped instead of snowy, base moulded with six faceless tourist bumps holding phone rectangles. Lettering band spells **ASTRONOMICAL COCK-UP / DEBAUCHERYVILLE** in dry-brushed gold relief that reads as a gold smear at icon size. **Reviewer: Mistral** — check my silhouette/scale logic and whether the must_not_look_like list misses an obvious failure mode.

Both are looks-only: no names, prices, stats or story touched. No real place names, no "Europe" anywhere; lettering spelled out per the rpac-q1 format.

One note for Mistral on his wristband item: the JSON gives `actual_text.bohemian: "Je mi 7!"` and `english: "I'm 7!"` — the brief says spell out the printed text exactly as canon gives it, so the band's lettering field should be **Je mi 7!** (the physical band prints the Bohemian; the English is the gloss). Flagging so we don't get two versions in the final.

_files: drafts/kimi_clock_snow_globe_batch3.md, drafts/kimi_i_survived_tshirt_batch3.md_

### Round 1 — Deepseek (2026-11-14 20:56)

**Deepseek — Phase 4 drafts filed.** `drafts/deepseek_batch3.md`. Reviewer: **Kimi** (voice) with **Mistral** second-reading the thong's icon-scale question.

**3. Rhinestone Shirt of Shame (Bedazzled).** There's already an icon prompt sheet at `Assets/Graphics/items/rhinestone-shirt-of-shame.md`, so I built on it rather than around it: same black slim-fit button-down, same missing-third-of-the-stones gag, same 16-colour palette. What I settled that the sheet left soft:

- **The stone swirl is a dead dragon.** It was a dragon; the missing third took the head, one wing and most of the tail. What survives is a fat comma ending in a hook over the right shoulder. Nobody in the club can identify it, because there is nothing left to identify. Plus one row of nine stones re-glued by hand, a full stone-width off line, excess glue under it.
- **The sparkle crosses the body the wrong way** — hip to opposite shoulder, so the sash runs like a seatbelt. Reads as bedazzled instantly at 64px and reads as *wrong* a half-second later.
- **Worn at least once, never washed:** sweat patch bleeding through to the outside, dried amber drink stain, bottom button gone with the thread tail and stretched buttonhole, one plastic tag barb still in the collar seam with the tag ripped off. That barb is the only "add-on" — no hangtag, no spare-button bag.
- **Nothing legible, ever.** No monogram, no skull, no heart, no team logo, and the tag barb holds no tag, so `lettering` is **None** — not decorative, not faint. If the generator produces anything readable on the stones it's a defect.

Two new hexes (#8A6A2F stain, #8A8A93 thread) take the sheet to its own 16-colour cap exactly. Flagged in the file: drop the thread hex first if the Asset team wants headroom.

**4. `item_leopard_print_thong`.** Object only — folded once across the pouch, front up, empty, no body, no wearer. Settled the two things the doc left vague:

- **Layout:** horizontal elastic band on top, collapsed pouch below, **one** narrow strap arcing up to the right in an open loop. That keyhole silhouette plus the single strap is what stops it reading as a woman's bikini bottom — which is the one failure mode that would wreck this icon, so I put it first in `must_not_look_like`.
- **Print and label:** sandy tan ground, broken dark-brown rosette rings with pale cream centres, jogging half a rosette out of line at the side seam, cut off mid-rosette at the waistband. Care label washed to a **blank white rectangle** — no brand, no size, no care symbols, no digits. I explicitly banned fake-illegible lettering on it: the label is a shape and a border stitch, and it's empty inside. That's the cleanest way to honour the binding rule — there is nothing on the object that could ever answer the question.

Sand in the seam, loose thread at the left hip, bleached top band against a still-bright fold, hard crease holding itself. Describes **state 1 only**; states 2 and 3 from the doc's fade ramp are restated underneath so the Asset team doesn't invent a different object for the variants. No hair, no lipstick, no jewellery, no second thread colour — nothing that hints at an owner.

**Two flags for the moderator, not decided by me:**

1. The thong doc's `Sprite Requirements` say **8×4 px** icon base. That predates the icon briefs. At 8×4 this object is a tan rectangle — no print, no label, no strap. Recommend the Desk confirm 64×64/128×128 like the rest of the batch and that 8×4 was only ever the in-world waistband sliver. If 8×4 stands I'll write a second, simpler description.
2. If anyone wants 16 colours for the shirt to mean 15 + transparency, say so and I'll cut the thread hex.

**Review notes filed to `critiques.md`:**

- **Kimi, `i_survived_tshirt`:** the weeping **clock face** is the soft read — it makes the landmark sad, and the clock didn't get scammed. Harder object: the print is a weeping **tourist** (bucket hat, camera on a neck strap, three fat teardrops) with the clock as a plain gold silhouette behind them. It's the vendor's joke aimed at the buyer's face, and the buyer wears it proudly. Also: fix the proportions — "torso slightly wider than it is long" reads as a folded towel, and one-sleeve-out/one-sleeve-tucked kills the shirt read at 64px. Cut the folding-table grid showing through the fabric (renders as noise, and you've already proved cheap three other ways). And rewrite `reads_at_icon_size` #2 — "reads instantly as 'wept-at tourist attraction'" is criticism, not description.
- **Kimi, `clock_snow_globe`** (second reader; Mistral primary): six faceless tourist bumps in the base is too much information for 64px and duplicates the tower read. Cut to three, lose the phone rectangles — six identical lumps become a scalloped skirt. The three-degrees-off lean is the best decision in the file; don't let anything compete with it.
- **Mistral, `vip_all_access_wristband`:** you have a live conflict. `vip_wristband_item.md:238` says the text should be legible on zoom; the brief says lettering can't carry the read. Both hold only if you state it: `lettering` spells out **Je mi 7!** exactly (the Bohemian on the band — "I'm 7!" is the gloss, never printed), and `reads_at_icon_size` carries the joke with no text at all: band too small, too bright, star shapes, waxy crayon palette. If the icon read needs the words, the description fails the brief.

_files: critiques.md, drafts/deepseek_batch3.md_

### Round 1 — Mistral (2026-11-14 20:58)

**Mistral — Phase 4 draft filed.** `drafts/mistral_vip_wristband_batch3.md`. Reviewer: **Kimi** (voice).

**5. `vip_all_access_wristband`.** Built on the existing asset prompt (`dev/asset_team/prompts/vip_all_access_wristband_prompt.md`) so the table pins the same object in the standing 12-field format rather than inventing a second one: a single sunny-yellow party-supply strip in a slightly open loop, white peg-and-hole snap clasp seated crooked at back right, printed pattern band of balloons/stars/confetti in red/blue/green standing in for the slogan.

Key calls:

- **The Deepseek-flagged conflict is resolved his way.** `lettering` spells out **Je mi 7!** exactly — the Bohemian the band physically prints; "I'm 7!" is the gloss and is never printed (Kimi flagged the same reading from the JSON's `actual_text.bohemian`/`english`). `reads_at_icon_size` carries the joke with **zero dependence on text**: small bright loop, real hole in the middle, childish confetti palette, crooked clasp — a kid's party band from shape and colour alone, legible-on-zoom per `vip_wristband_item.md:238` and still not carrying the icon read.
- **The per-bro colours stay off the icon.** #CC0000/#0000CC/#6600CC are the character-sprite overlay (the permanent wristband on each bro's arm), not the stock item icon — the prompt already made this call and the table records it so nobody merges them. `must_not_look_like` explicitly bans the Velvet Wristband (the real equipment item: thicker burgundy velvet, barbed clasp) and anything with readable letters, foil, or a "VIP" block.
- **Palette:** 10 colours, reusing the existing prompt's hexes verbatim (#B87C1C/#E8B430/#F6D840 yellow ramp, #C0302A/#2E5ED0/#3E9A4E motifs, #C9BFA6/#F4EEDC clasp, #2B1A2E outline, #6E5F72 shadow) — inside the 16-colour sprite cap with headroom. The square's Gothic Gold is deliberately not used; the band is its own object against the square's stone/gold.
- Looks only: name, 30 SOVS price, stats, quest hooks, Velvet Curtain payoff untouched. No real place names, no "Europe" anywhere; DEBAUCHERYVILLE is never printed on this object.

**Review notes filed to `critiques.md`** as primary reviewer on Kimi's `clock_snow_globe`: anchor the globe's tower dial to the square's Stone Gray #708090 / Gothic Gold #CFB53B so it reads as a souvenir of *this* clock at icon size; make the three-degrees lean the first item in `reads_at_icon_size`; keep "disappointment" wording out of the descriptive read fields (physical facts only, same rule as the t-shirt read #2).

One open flag for the Desk, inherited from Deepseek: the wristband doc's `Sprite Requirements` still says 8×4 px base — that's the on-wrist sliver, not this icon. This table assumes the standard 64×64/128×128 icon canvas like the rest of the batch.

_files: drafts/mistral_vip_wristband_batch3.md, critiques.md_

_files: critiques.md, drafts/mistral_vip_wristband_batch3.md_
