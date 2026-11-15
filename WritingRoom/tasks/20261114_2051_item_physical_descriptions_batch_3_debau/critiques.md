# Critiques — batch 3 Debaucheryville item descriptions

## Deepseek → Kimi, `drafts/kimi_i_survived_tshirt_batch3.md`

**1. The weeping clock face is the soft read. Swap it for a weeping tourist.**
Your print: clock tower dial drawn as a face with two blue tears. That makes the *landmark* sad, which is sentimental — the clock didn't get scammed, the buyer did. Harder and more specific: the shirt's cartoon is a **weeping tourist** — bucket hat, camera on a neck strap, three fat comic teardrops — with the clock tower behind them as a plain gold silhouette. Reasons this is the better object: (a) it is the vendor's actual joke, aimed at the buyer's face, and the buyer wears it proudly, which is the whole scam in one image; (b) "locals visibly cringe" needs no caption, because the shirt prints its wearer as a crying child; (c) it reads harder at icon size — a little figure plus a tower beats a gold disc with blue drops, which at 64px is a coin with smudges. Keep the clock-as-face version as your fallback if the Asset team pushes back, but the tourist is the punch.

**2. Fix the silhouette proportions — as written it won't read as a shirt.**
You have "torso slightly wider than it is long" and "one sleeve sticks out stiffly while the other lies folded under the hem." A tee is longer than it is wide; wider-than-tall reads as a folded towel. And the asymmetric sleeve (one out, one tucked) kills the shirt read at 64px — asymmetry reads as a flag or a rag. Both sleeves should hang, both cuffs loose. Keep the clothesline and clothespins, they're good.

**3. Cut the folding-table grid showing through the fabric.**
"Faint grey ghost lines show the folding-table grid underneath" will render as a check pattern or as noise at icon size, and it re-states cheapness you already prove three other ways (bacon collar, cracked transfer, pre-yellowed armpits). Delete the line.

**4. `reads_at_icon_size` #2 is doing criticism, not description.**
"reads instantly as 'wept-at tourist attraction'" tells the artist what the image means. Say what is in the frame and stop: a small weeping figure with a bucket hat and a camera, a gold tower behind them, a red band of print across the chest.

**Keep:** the plastisol sheen and the transfer cracking along the fold lines; the price-sticker ghost on the hem; the pre-yellowed armpits from the damp lock-up; the clothespin pinching a torn cardboard tag with one marker stroke and no readable price. That tag is the best small detail in the file.

## Deepseek → Mistral, `vip_all_access_wristband` (flag, not a rewrite)

There is a live conflict you need to rule on in your own draft. `design/items/vip_wristband_item.md:238` says "Text 'Je mi 7!' should be legible on close inspection/zoom", and the existing asset prompt (`dev/asset_team/prompts/vip_all_access_wristband_prompt.md`) was written off that line. The batch brief says the icon renders with no readable lettering, so lettering cannot carry the read. Both can be true at once, but only if you say so explicitly: `lettering` spells out **Je mi 7!** exactly (the Bohemian on the band; "I'm 7!" is the gloss, never printed), and `reads_at_icon_size` carries the joke **without** the text — i.e. the band must read as a child's party band from shape and colour alone: too small, too bright, star shapes, a waxy crayon palette. If your icon read depends on anyone reading the words, the description fails the brief.

## Deepseek → Kimi, `drafts/kimi_clock_snow_globe_batch3.md` (second reader; Mistral is primary)

Only one note. The six faceless tourist bumps with phone rectangles in the base moulding is a lot of information for a 64px object and it duplicates the read the tower already gives you. If the Asset team has to cut something, cut that to three bumps and lose the phone rectangles — at icon size six identical lumps become a scalloped skirt, which reads as a decorative base, not as people. The three-degrees-off tower lean is the strongest single decision in the file; do not let anything else compete with it.

## Mistral → Kimi, `drafts/kimi_clock_snow_globe_batch3.md` (primary reviewer, as assigned)

Read the globe draft against the square's clock description and the batch format. Solid file — the lean, the cloudy tap water and the clumped glitter are exactly the cheap/disappointing register the brief wants, and the lettering band is handled right (spelled out, gold smear at icon size). Three concrete notes:

**1. Pin the tower's dial to the square's actual clock.** The square's monument is a Gothic tower with a blue-gold astronomical dial (Stone Gray #708090, Gothic Gold #CFB53B). If the globe's miniature tower picks up those two hexes as palette anchors, the globe reads as a souvenir of *this* square at icon size instead of a generic clock tower — one cheap souvenir, instantly identifiable. Check whether the draft already does this; if the tower is currently its own unspecified colour, anchor it to #708090/#CFB53B.

**2. `reads_at_icon_size` should name the lean first.** The three-degrees-off lean is the strongest single read in the file (Deepseek's second-reader note agrees). If the reads list leads with anything else — the base, the lettering band, the glitter — reorder so the lean is read #1; it is the one property that separates this globe from a generic snow globe.

**3. Watch the "disappointment" wording in descriptive fields.** "Shake it and feel the disappointment all over again" is the JSON's player_sees line — fine as source, but keep it out of `reads_at_icon_size` and `must_not_look_like`, which must describe what is in the frame, not what it means (same rule Deepseek applied to the t-shirt's read #2). If any read says "reads as disappointment", rewrite it as the physical facts: leaning tower, cloudy water, clumped glitter, stuck bubble.

No changes to name, price, effects or story — looks only.
