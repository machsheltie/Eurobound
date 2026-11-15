# Thread — Item physical descriptions batch 1 Kokos Loco Bucket

### MODERATOR (2026-11-14 18:26)

**Moderator: assignments.** Mistral, Deepseek and Aion each write one full draft as described in the brief (drafts/<name>_kokos_physical.md). Kimi integrates afterwards. Read only: the brief, design/worlds/debaucheryville/items/bohemian_riviera_items.json (the item_kokos_loco_bucket entry), design/worlds/debaucheryville/bohemian_riviera.md lines 85-95 and 195-205, and dev/asset_team/icon_refs/item_kokos_loco_bucket_prompt.md (the failed round-3 prompt, so you can see what not to repeat). Write your file within your first 4 tool calls. Each writer: solve SCALE differently if you can, so the author gets real options.

### Round 1 — Mistral (2026-11-14 18:28)

Draft is in `drafts/mistral_kokos_physical.md`.

**Mistral:** Physical description written as a line-by-line art brief — caramel tan glossy injection-moulded shell (#C89B6A, mould seam, ejector-pin dots, husk bumps #A87F4F), three misregistered paint blobs (magenta #FF1493, lime #32CD32, orange #FF7F32, chipped at rim), heaped grainy pale-yellow piña colada (#F2E3A0 with fibre flecks, one drip), squised pineapple wedge, three wide straws (red/blue/snapped white), plus reuse wear: peeling white sticker rectangle, coral lipstick smear on the rim, base scratches. My scale solve, deliberately different from the other drafts: no person in frame — scale reads from the mouth-wider-than-tall squat bucket silhouette plus the three mouth-sized straws and the heaped-over-brim fill. Checklist and must-not-miss list built directly from the three QC failures; template section proposed for all later batches (`physical_description` heading with silhouette_and_scale / materials_and_cheap_cues / colours / contents / decoration / condition / garnish_and_addons / reads_at_icon_size / must_not_look_like / lettering fields). Reviewer: Kimi.

_files: drafts/mistral_kokos_physical.md_

### Round 1 — Deepseek (2026-11-14 18:29)

Draft is in `drafts/deepseek_kokos_physical.md`. Reviewer named: **Mistral** (scale-solve collision check); Kimi integrates.

**Deepseek:** My scale solve is the opposite of Mistral's, deliberately: **low fill, not a heap.** The bucket is a squat frustum (mouth 1.6× wider than the body is tall) and the drink sits visibly *below* the rim, leaving a tall band of bare ribbed inner wall over the liquid. A bowl, cup or soft-serve dish physically cannot show that much empty inner wall, so the depth reads even at 64 px. Mistral's heaped-over-brim mound is a direct round-3 hazard: an opaque smooth dome is what got read as soft-serve twice. Root causes split cleanly — scale = proportion + visible depth + **eight straws** (a four-person order, not one tourist's); dubious = ochre-yellow plastic, greasy semi-matte sheen, sand in the foot ring, two lipstick smears in different colours, chip, peeling barcode-white rectangle over a glue shadow.

Kill-cues I invented for my own risks: **four cloudy ice blocks** breaking the surface (kills dessert and ice cream), **hardened dried amber foam ring** (kills "clean appetising cream"), paint misregistered **across the mould seam** so the seam splits the lime frond (kills tidy decals), and a fresh glossy touch-up blob of paint (kills kids' toy).

**On Mistral's draft** — concrete cuts:
1. `#F2E3A0` + smooth heaped mound + "one drip" is the round-1 appetising-cream failure reconstituted. Needs a visible liquid surface broken by something solid, and a low fill.
2. Three straws argues for one drinker, not a bucket. Six to eight.
3. "Filled just over the brim" cannot coexist with "a dried drink ring inside" — pick one; the interior wall is the strongest scale cue on the sheet.
4. Typo: "squised" → "squashed" / "pinched".
5. His smeared-mound tongue reads as soft-serve once rendered as flat 3D vinyl; the grany texture won't survive 64 px. Replace texture-loss with shape-loss.

**Template disagreement:** split his `silhouette_and_scale` into two required fields — `silhouette` (proportions) and `scale_cue` (**one** sentence, the single thing that reads big in an empty frame). All three failed rounds were scale failures and a merged field lets a painter hedge. I also added `palette_anchors`, marking which hexes are inherited from the location palette (`#FF1493` EMTV magenta, `#32CD32` inflatable-palm green, `#FF7F32` space-heater orange are all already in `bohemian_riviera.md`) versus new to the item, so icons and location art don't clash.

Flag for Kimi at integration: Mistral's and my descriptions are **options for the author**, not a composite. Merging them produces the heaped mound on a squat bucket with eight straws and two sticker stories.

_files: drafts/deepseek_kokos_physical.md_

### Round 1 — Aion (2026-11-14 18:36)

Draft is in `drafts/aion_kokos_physical.md`. Reviewer: **Deepseek** (failure-mode collision — you killed Mistral's heaped mound on exactly the grounds I risk, kill mine the same way). Kimi integrates.

**Aion:** My scale solve is a genuine third option, not a remix of the two on the table: **proportion mismatch via a known-size object.** A pineapple wedge hangs off the rim — and the mouth is so wide the wedge reads small. No person in frame, no straw-count argument, no proportion math for the painter to fudge. It pairs with a thick rolled **pail** rim (the round-3 prompt explicitly said "no handles, thick solid rim" and still read as a bowl — the missing piece was the rim being a *pail* rim with bare inner wall above the liquid, not a cup rim). Fill is two-thirds, with a dried amber tide-line over bare inner wall, so depth reads like Deepseek's without converging on his eight straws.

Dubiousness is carried by things a painter can actually render at 64 px, not texture that dies at thumbnail: yellowed packing tape over a crack, a mould seam that splits all three painted shapes, ejector-pin dots, coral lipstick, sand in the foot ring, grey at the drink's edges. Dessert is killed by three cloudy ice cubes breaking the cream surface plus an outside drip — no smooth swirled dome anywhere. I keep one red-striped straw with tooth marks at the tip: reuse evidence and beverage cue, not a scale argument. Deepseek, I've flagged in the file that I'll cut it rather than defend it if you think one straw drags toward single-serve.

**On the other drafts, concrete:**

**Mistral:** the tide-line contradiction Deepseek flagged is real and you should fix it in your file — "filled just over the brim" and "a dried drink ring inside" cannot both render. Also your #F2E3A0 heaped smooth mound is round-1's "clean white cream reads appetising" with a yellow tint; the fibre flecks won't survive 64 px. Take Deepseek's shape-loss advice: break the surface with something solid.

**Deepseek:** your eight straws are doing scale work, but eight readables at 128 px means eight thin lines — I'd bet half render as noise. Consider six, fanned, thick-gauge. Your ochre-yellow shell is the right call against "chocolate/ceramic." I back your `silhouette`/`scale_cue` split and `palette_anchors`, and I've added both to my template section, plus a mandatory `lettering: none` field so no future brief leans on a readable sticker again — that's what round 3's "peeling barcode-white rectangle" habit keeps drifting toward.

**For Kimi at integration:** all three drafts are options for the author, not a composite. The three scale solves are mutually exclusive as *primary* cues (overbrim heap / low fill + eight straws / wedge proportion mismatch) but the cheapness, drink and condition language is converging nicely — that's the layer you can safely merge. Open flag for the author, in my file: if the pineapple wedge dies at 64 px, my option collapses toward Deepseek's and the author should know the wedge is the load-bearing difference.

_files: drafts/aion_kokos_physical.md_

### MODERATOR (2026-11-14 18:37)

**Moderator: integration order for Kimi.** Write final.md as one art brief with ONE shared body and THREE scale options, so the author picks the scale solve on the Desk.
1. **Shared body** (shell, paint, drink colour, condition), merged from all three. Shell: tan-to-amber glossy injection-moulded plastic with a yellow cast, never chocolate, orange or green. Use one hex for the shell and one for the husk bumps; pick between #C09A62 and #B5722F and say which. Paint: the three location palette anchors, verified in bohemian_riviera.md:121-124 (EMTV Magenta #FF1493, Inflatable-Palm Green #32CD32, Space Heater Orange #FF7F32), botched and split by the mould seam. Drink: opaque cream-gold, never white, with cloudy ice cubes breaking the surface and a dried amber foam ring. Condition: peeling white barcode-shaped sticker with no readable text, coral lipstick smear, sand in the foot ring, chipped lip, and Aion's yellowed packing tape over a crack. No handles, ever.
2. **Scale options**, each in 2-3 sentences with its own straw count:
   A (Deepseek): low fill with a tall bare inner wall, plus a fan of eight straws (a four-person order). List all eight colours; the draft only names four.
   B (Aion): a pineapple wedge reading small against a huge rolled pail rim, plus one bent, tooth-marked straw.
   C (Mistral): drink heaped just over the brim, plus three wide straws. State its known risk plainly: the heap is the round-3 soft-serve failure.
3. **Cuts:** 'husk bumps moulded upside down' (unpaintable), 'one hard white highlight' (lighting belongs to the render), and any word a painter can't paint.
4. **Reads at icon size** (3 items) and **Must not look like** (merged, deduped), each written so they hold for all three options.
5. **Template section:** use Aion's 12-field list (silhouette, scale_cue, materials_and_cheap_cues, colours, contents, decoration, condition, garnish_and_addons, palette_anchors, reads_at_icon_size, must_not_look_like, lettering). Heading: '## Physical description (icon art brief)'.
Keep it plain and concrete. No bros, no flavour copy. Don't touch the price, effects or the player_sees/bros_see lines.

### FINAL PASS — Kimi (2026-11-14 18:38)

Integration is done and my vote is recorded.

**Summary of what `final.md` contains:**

1. **Shared body** — silhouette (squat frustum, 1.5–1.6× mouth:height, thick rolled pail rim, no handles ever), shell in amber-tan #B5722F with darker #7A4A21 husk bumps, mould seam, ejector-pin dots, greasy wrong sheen; the three canon palette-anchor paint shapes (#FF1493 / #32CD32 / #FF7F32) botched and split by the seam; opaque cream-gold drink #F2E3A0 with four cloudy ice blocks #D6E7EC, dried amber foam ring #B8912F, greyed edges; full reuse-condition layer (peeling barcode-white sticker over glue shadow, coral lipstick, sand in the foot ring, chipped lip, yellowed packing tape over a crack, dried spill streak).

2. **Three scale options, mutually exclusive, each with its own straw layer** — A (Deepseek: low fill + bare inner wall + eight straws, all eight colours listed), B (Aion: dwarfed pineapple wedge + one bent tooth-marked straw), C (Mistral: heaped fill + three straws, with the round-3 soft-serve risk stated verbatim).

3. **Icon-size checklist and must-not-look-like list** merged, deduped, holding for all three options, seeded from all three QC failures plus each draft's self-identified risks.

4. **The 12-field template** (`## Physical description (icon art brief)`) proposed for batches 2+, with Aion's `lettering: none` field and Deepseek's `silhouette`/`scale_cue` split and `palette_anchors`.

5. **Two outstanding author decisions** documented in-file: the scale pick (room recommends A or B) and template adoption.

_files: final.md_

### AUTHOR NOTE (2026-11-14 19:07)

Desk Eurobound-rpac-q1 (author, 2026-11-14): "Approve with A: low fill + eight straws, and adopt the template". Desk Eurobound-rpac-q2: "A: a short .md per item from its template"
