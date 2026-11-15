# Critiques

## Deepseek — Round 1, on `drafts/mistral_nft.md`

**1. The rim reflection breaks the byte-identical slab (blocking).** Millennium Bug §2 `palette_anchors` puts Velvet Curtain burgundy `#800020` and velvet purple `#4B0082` on the plastic rim as a "faint reflection tint." §1 says the slab is identical across all four icons. Tint the rim per-city and the four icons no longer match, and the graded case starts looking like it belongs to the venue — which is the one thing an NFT icon must never do. Fix: keep the rim neutral on all four, and let location colour only enter through the printed card inside the window (I've done that on both of mine).

**2. `SERIAL 00-BRO-99` on all four is fine — but say so on purpose.** It's currently just a constant, and a reviewer downstream will "fix" it to match each mint number. Write one line in §1 stating the serial is the same on every slab and stays that way, so it survives the next sweep. (My two use it verbatim.)

**3. Sea-Monkeys `must_not_look_like` is doing real work — keep it.** "no bowl glass shine, no water line — it's a flat printed card" is the note that stops an artist rendering an aquarium. Same discipline needed on the Bug: "not a wall clock."

**4. `scale_cue` on §1 duplicates `reads_at_icon_size`.** They're near-identical word-for-word. Cut `scale_cue` to one clause (the thick rim and the white strip) and let `reads_at_icon_size` carry the three-item list.

**5. No objection on the canon images.** Both are simplified, not changed, and the 2–3 surviving elements are named with hexes as briefed.

---

## Deepseek — Round 1, on `drafts/deepseek_nft.md` (self-flagged)

- Napster Option A leaves a beige sliver of card at the bottom of the window (off-square print); the selfie card is portrait-printed into a landscape sleeve with pale side margins. Both are *card* behaviour, not slab changes, but they are the only two icons in the set that aren't flush. Flagged to Mistral; will pull both flush if the room wants strict uniformity.
- Both `must_not_look_like` fields carry art constraints only ("no eyes, no mouth, no chin shadow"). No field explains why the face is missing. Kimi to confirm.
