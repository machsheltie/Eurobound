# aa_prize_two_grand_tie_dye_tee: prompt review and ref 3 (redo)

Author note (Desk): "Ask an agent to review how it is prompting it. It should look like a folded tie dyed T-shirt. Then you can have an agent add the writing post process in adobe photoshop on my desktop".

## What was wrong with the old prompts

- Ref 1 (build 1): asked for a "chunky, thick, neatly folded stack, a fat solid rectangular slab". The model read "stack" and "slab" as a lump; the stubby sleeves slumped. Lettering was in the prompt, so Tripo baked the print into the fold and garbled it.
- Ref 2 (build 2): the prompt demanded "one perfectly flat, rigid, boxy rectangular slab ... no sleeves ... no collar ... no creases". That is the opposite of a shirt. The image was a card, not a folded tee, so the build was a boxy slab. The fix for ref 1 overcorrected.
- Both: lettering was drawn by the image model and Tripo then baked it into the texture, so it smudged on folds. Both asked for a photoreal fabric, which Tripo cannot hold at fold scale. Colours were given as three bands only.
- Root cause: the prompts described the shape in geometry words (slab, stack) and never named the recognisable parts of a folded shirt (collar, folded-in sleeves, fold creases).

## New prompt (ref 3)

Lettering is removed from the reference and the model. It is added afterwards as a Photoshop text layer.

Target: a neatly retail-folded tie-dye T-shirt, front panel facing the viewer, round collar opening visible at the top, both short sleeves folded in to the back so only their folded edges show at the sides, a soft horizontal fold across the lower third, soft rounded fabric folds, chunky and simple. Spiral tie-dye in hot pink, electric blue and acid yellow-green. Front print area left as plain tie-dye.

Prompt: see `aa_prize_two_grand_tie_dye_tee_prompt.md` (updated to ref 3).

Checks for A3: recognisably a shirt; collar and sleeves visible; no text anywhere; square 1:1; flat light grey background; margin at least 10 percent on every side (Pillow).
