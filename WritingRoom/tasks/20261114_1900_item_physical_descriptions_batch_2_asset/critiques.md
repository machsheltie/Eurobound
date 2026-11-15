# Critiques — batch 2

## Deepseek on Mistral's `drafts/mistral_cirque_du_shady_batch2.md` (teeth pass)

Reviewer note: the format work and the looks are strong and paintable. Four cuts, one repetition, one support.

1. **Voucher, `lettering` — three lines plus a stamp is one line too many for 128 px.** `A BIT OF A GAMBLE, HONESTLY` is nine words of thermal blur; at icon size it renders as a grey smear, so the funniest of the three lines is the one nobody can read. Cut it and keep `SHADY LOOT CRATE` / `VOUCHER — REDEEM AT PRIZE BOOTH` / stamp `NO REFUNDS`; the joke survives in the stamp and the paper, and the block reads as text instead of texture. (Mistral's reason for the line — that it quotes Vance — is a reason it *fits*, not a reason it paints.)

2. **Voucher `decoration` + flyer `condition` — the same coffee ring, twice, in the same tent.** `#8B6F47` appears on both items, described near-identically. Two Shady Productions props then read as the same object photographed twice. Keep it on the flyer (a handout gets set down), delete it from the voucher (`cirque_du_shady_items.json`: pawed, not rested).

3. **Flyer `condition` — six wear marks on one sheet is noise, not detail.** Curled corners, browned edges, middle crease, coffee ring, thumb smudge, double-struck line, bottom tear. Cut the **coffee ring** and the **tear**: both are generic handout wear and neither says "Shady Productions". What is left — fax-browned edges, the crease, the stutter line, the blank two-thirds — is specific, and the text block gets to breathe.

4. **Glitter hat `decoration` and `must_not_look_like` — the branding ban is stated twice.** "No branding of any kind — no logo, no character art" then again "Any branded character merchandise — no logo, no character, no franchise marks of any kind." The second is a restatement of the first. Keep it in `must_not_look_like` (that is where a painter checks) and cut it from `decoration`.

5. **Glitter hat, one thing to add:** the worst stain needs a location. "A dark stain on one streamer" is the object's one grubby punchline and it currently has no place to be. Say *which* streamer and *where* on it.

6. **Support on the voucher sprite question.** The icon must be the paper voucher. Mistral already wrote it that way. An `Art/…vance_vallaro.png` pointer is a sprite-sheet reference, not a look; a "Voucher" slot showing a person's face breaks inventory readability at a glance, and the voucher's own joke is that it is a worthless piece of paper.
