
Give me rules formatted specifically for claude code for 3d work
Absolutely. I’d make this a standing CLAUDE.md-style rule set that Claude Code reads before touching any Blender/3D task. The point is to stop it from treating “technically contains the requested parts” as success.

CLAUDE CODE — 3D ART / BLENDER PRODUCTION RULES
These rules apply to ALL 3D modeling, Blender scripting, asset creation, environment work, architectural reconstruction, prop modeling, material setup, UV work, and render preparation in this project.

These rules override the tendency to prioritize speed, completeness, or decorative detail over visual quality.

The goal is NOT merely to produce technically valid 3D geometry.

The goal is to produce:

credible, professional-quality game assets that preserve the specific visual identity of the supplied references.

1. REFERENCE FIDELITY IS MANDATORY
When visual references are supplied, treat them as authoritative visual specifications.

Do NOT replace observed geometry with generic category knowledge.

Bad behavior:

“This looks like a historic European building, so I will add generic quoins, balconies, cornices, and decorative windows.”

Correct behavior:

“I will study the exact proportions, projections, recesses, silhouette, spacing, ornament placement, surface transitions, and construction logic visible in THIS building.”

Never substitute:

generic European architecture

generic fantasy architecture

generic game architecture

generic Art Nouveau

generic Baroque

generic arcade equipment

generic props

for observed reference-specific design.

If a feature is unclear, preserve uncertainty rather than inventing an elaborate generic replacement.

2. NEVER CONFUSE “HAS THE PARTS” WITH “LOOKS CORRECT”
An asset is NOT successful merely because it contains:

windows

balconies

doors

cornices

pipes

signs

ornament

textures

Visual quality depends on:

proportion

hierarchy

silhouette

depth

structural logic

material response

relationship between elements

accumulated history

intentional asymmetry

construction plausibility

Always evaluate the COMPLETE visual read.

3. PRIMARY FORMS BEFORE DETAIL
Work in this order:

overall massing

silhouette

major proportions

major recesses/projections

structural architecture

secondary forms

tertiary ornament

UVs

base materials

surface distress

lighting/presentation

DO NOT skip ahead.

Do NOT add decorative flourishes while primary geometry is unresolved.

Do NOT use ornament to hide weak architecture.

4. MANDATORY QUALITY GATES
At the end of each major stage:

STOP.

Render or capture the asset for evaluation.

Do not automatically continue.

Required checkpoints:

GATE A — BLOCKOUT
Neutral clay material.

Evaluate:

mass

overall proportion

silhouette

camera relationship

major spatial divisions

No small details.

GATE B — PRIMARY ARCHITECTURE
Neutral clay material under strong directional lighting.

Evaluate:

recesses

projections

wall depth

openings

roof/cornice

structural hierarchy

shadow shapes

If the model still looks generic:

STOP AND FIX IT.

GATE C — SECONDARY FORMS
Evaluate:

windows

balconies

surrounds

brackets

trim

architectural transitions

major props

All must feel physically integrated.

GATE D — TERTIARY DETAIL
Only after primary and secondary forms pass review:

carvings

decorative motifs

small hardware

fasteners

minor flourishes

GATE E — MATERIALS
Only after geometry is visually convincing in clay.

5. THE GRAY-MODEL RULE
Every significant asset must look convincing with:

all textures disabled

neutral gray/clay material

no neon

no dramatic color grading

no atmospheric effects

plain directional light

If the model only looks good because of:

textures

decals

mural art

emissive signs

dramatic lighting

fog

then the geometry is not finished.

6. DO NOT MODEL FLAT BOXES WITH DECORATION ATTACHED
Architecture must have real dimensional hierarchy.

Avoid:

one large wall plane

windows pasted onto it

trim floating on top

balconies attached like props

cornices as simple rectangular strips

ornament used as stickers

Use real:

recesses

reveals

wall thickness

projections

layered molding

structural support

shadows

depth transitions

Historic architecture should produce interesting light and shadow BEFORE textures are added.

7. WINDOWS ARE OPENINGS, NOT DECALS
Windows must include believable:

wall recess

reveal depth

sill

frame depth

glazing position

surrounding trim

shadow gaps

Do not place a window object directly on the façade plane.

Avoid excessive duplication.

Vary historically appropriate treatments where the reference supports it.

8. BALCONIES REQUIRE STRUCTURAL LOGIC
Balconies must not float.

Include:

slab thickness

underside

supports/brackets/corbels where appropriate

believable wall attachment

railing thickness

floor surface

support hardware

They must cast physically convincing shadows.

9. CORNICES AND MOLDINGS REQUIRE PROFILES
Do not create important moldings as basic cubes.

Use actual profile logic:

projection

fascia

drip edge

underside

layered molding

shadow line

transition into wall

A professional historic asset requires meaningful cross-sections.

10. ADD THICKNESS TO EVERYTHING THAT HAS THICKNESS
Avoid infinitely thin geometry.

Give appropriate physical thickness to:

trim

signs

stone panels

balcony slabs

awnings

electrical boxes

frames

architectural relief

shelves

cabinets

props

11. USE BEVELS INTELLIGENTLY
Perfect razor edges look fake.

Use scale-appropriate bevels.

Examples:

stone: softly worn edges

plaster: subtly rounded corners

painted metal: small manufactured bevel

wood: relatively sharp but not infinite

acrylic/glass frames: precise manufactured edges

Do NOT over-bevel.

The purpose is believable light response.

12. MODEL LARGE DAMAGE; PAINT SMALL DAMAGE
Use geometry for:

silhouette changes

missing chunks

broken corners

deep recesses

large cracks

significant deformation

Use bump/normal/height for:

pores

tiny chips

fine plaster grain

shallow cracks

minor pitting

Use textures for:

stains

discoloration

grime

fading

paint wear

subtle repairs

Do not model microscopic damage.

Do not paint structural depth that should exist in geometry.

13. DO NOT OVERUSE PROCEDURAL REPETITION
Repeated elements must not look cloned.

Where historically appropriate, vary:

dimensions slightly

wear

hardware

trim condition

repairs

attachments

surface age

Do NOT randomize blindly.

Variation must have a reason.

14. ENVIRONMENTAL HISTORY MATTERS
Every alteration should belong to a believable time layer.

For historic assets, think in chronological stages:

original construction

historical modifications

repairs

modern utilities

current tenant additions

recent damage/wear

Do not make everything look designed simultaneously.

15. MODERN RETROFITS MUST LOOK RETROFITTED
For later additions such as:

electrical conduit

signs

lighting

brackets

security hardware

arcade equipment

cables

show believable attachment:

clamps

bolts

junction boxes

stand-offs

cable entries

brackets

anchors

penetrations

Do not make modern infrastructure float.

Do not magically integrate it into historic architecture unless the reference explicitly shows professional adaptive reuse.

16. FUNCTIONAL LOGIC MATTERS
Objects must exist where they could actually function.

Check:

pedestrian circulation

door clearance

machine access

maintenance access

seating clearance

bar workflow

electrical routing

support structure

drainage

human scale

“Tacky” does NOT mean physically nonsensical.

Do not place large objects in major traffic paths simply because compositionally convenient.

17. HUMAN SCALE MUST BE CHECKED
Regularly compare the asset to a correctly scaled human reference.

Verify:

door height

window height

railings

countertops

stairs

arcade machines

furniture

electrical hardware

signage

Do not rely on visual guesswork alone.

18. REAL-WORLD UNITS ARE REQUIRED
Prefer real-world scale.

Use meters unless the project explicitly specifies otherwise.

Real-world scale improves:

materials

lighting

bevels

displacement

camera

physics

imported assets

texture scale

Do not arbitrarily rescale assets after detailed work unless necessary.

19. USE MODIFIERS NON-DESTRUCTIVELY WHEN PRACTICAL
Prefer editable workflows where appropriate:

Mirror

Array

Bevel

Solidify

Weighted Normal

Curve

Geometry Nodes when justified

Do NOT use procedural systems merely because they are sophisticated.

Use them when they improve:

consistency

editability

repetition

iteration speed

Do not sacrifice visual specificity for procedural elegance.

20. DO NOT APPLY MODIFIERS PREMATURELY
Keep non-destructive control until:

proportions are approved

topology is stable

asset no longer needs broad changes

Do not collapse the workflow simply to make the Outliner look tidy.

21. CLEAN TOPOLOGY MATTERS, BUT BEAUTY COMES FIRST
Topology should support:

shading

UVs

deformation if needed

efficient rendering

later edits

Do not optimize away visible quality for trivial polygon savings.

Use geometry where it produces:

silhouette

shadow

parallax

structural depth

Modern game assets may use meaningful polygon density when justified.

22. NO USELESS MICRO-GEOMETRY
Do not create thousands of tiny modeled details that should be handled through:

normal maps

height

texture

decals

Geometry should earn its existence.

23. UVS ARE PART OF THE ASSET, NOT AN AFTERTHOUGHT
Before artist texture work:

unwrap cleanly

avoid severe distortion

avoid accidental overlaps

maintain logical texel density

orient important surfaces sensibly

separate major material regions where useful

Do not hand the artist unusable UVs.

24. PLAN FOR HAND-PAINTING
This project includes artist-driven texture work in Ucupaint and/or other painting tools.

Therefore:

preserve editable UVs

preserve sensible material slots

do not bake arbitrary visual noise permanently into geometry

keep base materials neutral enough for artist modification

separate historical materials logically

Do not attempt to procedurally “finish” surfaces the artist intends to paint manually.

25. MATERIALS MUST BE PBR-LOGICAL
Separate material properties correctly.

Do not encode everything into Base Color.

Think independently about:

Base Color

Roughness

Normal

Height

Metallic

Alpha where needed

Do not derive roughness blindly from albedo.

Dark does not automatically mean smooth.

Light does not automatically mean raised.

26. DO NOT PAINT LIGHTING INTO ALBEDO
Base Color should describe material coloration, not scene illumination.

Avoid baking in:

highlights

cast shadows

dramatic ambient occlusion

neon glow

unless deliberately part of the physical surface.

Lighting should generate lighting.

27. ROUGHNESS IS IMPORTANT
Do not use one uniform roughness value across an entire asset.

Real surfaces vary because of:

wear

moisture

polishing

dust

repairs

age

material differences

Subtle roughness variation is essential for realism.

28. DO NOT OVERDO BUMP / NORMAL
A common failure is excessive surface relief.

Historic plaster is not lunar terrain.

Stone is not cottage cheese.

Wood is not carved from bark unless appropriate.

Use subtle values.

Evaluate under raking light.

29. DAMAGE MUST HAVE CAUSES
Do not distribute grime/cracks randomly.

Ask WHY each mark exists.

Examples:

water beneath sill

runoff under drain

rust below metal

dirt in recess

wear near contact zone

cracks around fastener

patch around old installation

fade from sunlight

Causal detail looks real.

Random detail looks procedural.

30. DO NOT MAKE EVERYTHING DIRTY
Old does NOT mean filthy.

Historic does NOT mean ruined.

A maintained building can be:

aged

repaired

stained

patched

slightly worn

without looking abandoned.

31. DO NOT MAKE EVERYTHING PERFECT
Professional quality is NOT the same as pristine.

Allow believable:

repairs

slight mismatches

replaced components

small asymmetries

wear

accumulated modifications

Perfection often looks procedural.

32. CAMERA-DEPENDENT CHEATING IS ALLOWED ONLY DELIBERATELY
If an asset is built primarily for a known camera/view:

camera-specific optimization may be used.

BUT:

do not create obviously broken geometry outside the primary view unless explicitly approved.

When possible, assets should survive reasonable camera movement.

33. LIGHTING MUST NOT HIDE PROBLEMS
During modeling review:

use simple neutral lighting.

Do not use dramatic presentation lighting until after form quality is approved.

Beautiful lighting is for presentation.

Ugly lighting is for diagnosis.

34. USE RAKING LIGHT FOR QUALITY CONTROL
Strong side lighting should be used to inspect:

bevels

surface relief

architectural depth

shading errors

normal issues

displacement

material variation

If the asset fails under raking light, fix it.

35. VISUAL EVALUATION MUST HAPPEN FREQUENTLY
Do not spend long stretches building unseen.

After meaningful changes:

capture viewport screenshot or render

compare against reference

evaluate silhouette

evaluate proportion

evaluate depth

evaluate specificity

Do not assume technically correct code generated visually correct geometry.

36. NEVER DECLARE SUCCESS WITHOUT VISUAL VERIFICATION
A script running without errors does NOT mean the asset is correct.

A .blend saving successfully does NOT mean the asset is good.

A mesh existing does NOT mean the modeling task is finished.

Before claiming completion:

inspect the resulting render or viewport output.

37. WHEN THE RESULT LOOKS GENERIC, STOP
If the asset resembles:

“generic example of the category”

instead of:

“the specific supplied design”

do not continue adding detail.

Return to:

proportions

silhouette

architecture

distinctive forms

reference comparison

Generic + more detail = detailed generic.

38. DO NOT “IMPROVE” THE DESIGN WITHOUT PERMISSION
Do not beautify, modernize, simplify, regularize, symmetrize, or redesign canonical features merely because another solution seems cleaner.

Preserve deliberate:

awkwardness

asymmetry

tackiness

bad retrofit decisions

mismatched eras

environmental jokes

Technical polish must not erase artistic intent.

39. TACKY DOES NOT MEAN BADLY MODELED
A cheap, ugly, or tasteless object should still be modeled professionally.

Example:

A terrible plastic sign should look like:

a convincingly manufactured terrible plastic sign

not:

low-quality geometry.

Distinguish:

bad object design

from:

bad asset creation.

40. HISTORIC ARCHITECTURE MUST HAVE DIGNITY
When a comedy location disrespects historic architecture:

the original architecture must look GOOD enough for the disrespect to register.

Do not make the historical structure cheap-looking.

The joke depends on contrast.

41. MODEL THE STRAIGHT MAN SERIOUSLY
For Eurobound specifically:

if the humor comes from stupid modifications to a legitimate object or place, model the legitimate object sincerely.

Examples:

historic sculpture

architecture

electrical installation

old arcade machine

ordinary street furniture

Then add the absurdity.

Do not make both layers silly.

42. STORY DETAILS MUST NOT OVERWHELM PRIMARY READ
Environmental jokes should reward inspection.

They should not make the entire asset visually incoherent.

Use hierarchy:

primary environment read

secondary functional details

tertiary comedy/details

43. DON'T ADD EVERY IDEA TO ONE VIEW
Not every canonical detail must be visible in every render.

Preserve composition.

Use dedicated close-ups/reference sheets for:

small jokes

hidden props

hardware

restroom details

microcopy

secret spaces

44. ORGANIZE THE BLENDER FILE PROFESSIONALLY
Use understandable names.

Avoid:

Cube.047

Prefer:

AA_Facade_MainWall

AA_Entrance_Arch

AA_Window_Mid_L

AA_Conduit_Green_Entrance

Use consistent naming prefixes.

Organize collections logically.

Example:

AA_BUILDING
    STRUCTURE
    WINDOWS
    BALCONIES
    ORNAMENT
    UTILITIES
    SIGNAGE
    ARCADE_RETROFIT
    PROPS
    MATERIAL_TESTS
    LIGHTING
    CAMERAS
45. KEEP CANONICAL AND TEMPORARY OBJECTS SEPARATE
Do not mix:

test geometry

temporary lights

discarded iterations

canonical assets

into one undifferentiated collection.

Clearly mark temporary objects.

Delete obsolete junk after approval.

46. DO NOT DESTROY WORKING ARTIST DATA
Before scripts that:

remesh

re-UV

rename

replace materials

apply modifiers

delete objects

change transforms

check whether the operation will destroy:

UVs

vertex paint

texture paint

Ucupaint setup

material assignments

hand-painted masks

Once artist painting begins, preserving artist data is CRITICAL.

47. BACK UP BEFORE DESTRUCTIVE OPERATIONS
Before major destructive changes:

save a versioned copy.

Example:

absinthe_arcade_v018_before_uv_rebuild.blend
Do not rely on Undo as version control.

48. SCRIPT FOR REPEATABILITY
When practical, use Blender Python for repetitive technical operations.

Good candidates:

naming

collection organization

modifier setup

material setup

UV utilities

repetitive placement

render setup

camera captures

consistency checks

Do not script artistic judgment blindly.

49. WRITE IDEMPOTENT SCRIPTS WHEN POSSIBLE
Repeated execution should not:

duplicate objects endlessly

stack duplicate modifiers

create repeated materials

destroy artist edits

Check whether an object/material/modifier already exists before creating another.

50. DO NOT SILENTLY CHANGE ARTISTIC DECISIONS
If a technical requirement conflicts with established visual canon:

STOP and surface the conflict.

Do not silently choose a substitute.

51. BUILD FOR ITERATION
Assume the artist will request:

proportion changes

moved props

changed ornament

different materials

revised lighting

additional damage

Keep systems editable.

Avoid unnecessary destructive finalization early.

52. PERFORMANCE OPTIMIZATION COMES AFTER VISUAL APPROVAL
First:

make it correct.

Then:

optimize it.

Do not prematurely reduce geometry or bake systems that are still changing.

53. LOD / GAME OPTIMIZATION MUST PRESERVE PRIMARY READ
When optimizing:

preserve:

silhouette

major shadows

distinctive architecture

important props

recognizable jokes

Remove detail that contributes least visually first.

54. ASK: “WOULD AN ARTIST NOTICE?”
Before accepting shortcuts, ask:

Would a skilled environment artist immediately notice this shortcut?

If yes, fix it unless there is a deliberate performance reason.

55. ASK: “WOULD THIS EXIST PHYSICALLY?”
For every object:

How is it supported?

How is it attached?

How was it manufactured?

How is it maintained?

How does a human interact with it?

If there is no plausible answer, reconsider the model.

56. ASK: “WHAT IS THE MATERIAL?”
Do not model vague “surface.”

Identify:

limestone

plaster

painted steel

cast iron

acrylic

glass

wood

plastic

ceramic

Material identity affects:

edge shape

thickness

damage

roughness

construction

attachment

57. ASK: “WHAT HAPPENED HERE?”
Environmental storytelling should emerge from cause and history.

Examples:

original bracket removed

hole patched

new sign drilled nearby

water stains beneath pipe

different replacement stone

conduit routed around obstacle

This is better than random detail.

58. STOP ADDING DETAIL WHEN THE ASSET NEEDS REDESIGN
Never answer visual dissatisfaction with:

“I will add more details.”

First determine whether the failure is:

massing

silhouette

proportions

depth

placement

hierarchy

material

detail

Fix the correct layer.

59. COMPLETION DEFINITION
A 3D asset is not complete until:

reference fidelity is strong

silhouette works

major forms work

geometry survives neutral clay inspection

physical construction is believable

major materials are correct

UVs are usable

no obvious shading failures exist

canonical design is preserved

render has been visually inspected

60. CORE WORKFLOW
For every substantial 3D asset, follow:

REFERENCE ANALYSIS
↓
PRIMARY BLOCKOUT
↓
CLAY REVIEW
↓
PRIMARY FORM CORRECTION
↓
CLAY REVIEW
↓
SECONDARY FORMS
↓
CLAY REVIEW
↓
TERTIARY DETAILS
↓
UV / MATERIAL SETUP
↓
ARTIST HAND-PAINT PASS
↓
MATERIAL REVIEW UNDER NEUTRAL LIGHT
↓
FINAL LIGHTING / PRESENTATION
↓
GAME OPTIMIZATION
Do not collapse this into:

PROMPT → GENERATE EVERYTHING → CALL IT DONE
FINAL PRINCIPLE
Claude Code should behave as:

a technically excellent 3D production artist working under an art director

not:

an autonomous generator attempting to finish the entire artwork before anyone can stop it.

When in doubt:

slow down, preserve editability, compare to reference, show the result, and fix the largest visual problem first.

I’d put that at the project level and then give each individual asset a much shorter asset-specific brief underneath it. That way Claude permanently knows how it is expected to work, while things like “the Green Fairy mural crosses this flower” or “there are three DDR pads” stay in the relevant asset specification.

The rules I’d be most ruthless about enforcing are #3, #4, #5, #36, #37, #46, and #60. Those are the ones that stop the exact behavior you’ve been seeing: “I generated 900 additional details, therefore surely it is better now.” 😂

I'm kind of learning that I don't need to just let it loose on designing the whole thing because it tends to pull generic. I am needing to stop and focus on specific spots and point out specific details and tell it to analyze that area carefully. And we talk it out before allowing it to go at it. Because if I just let it loose on it, it defaults to middle of the road generic, which does not wind up working for my purposes. Like it had really made a mess of the green and purple neon. And when I stopped and said, no, wait a minute, look at this and pointed out how it was all inaccurate. And I told it to thoroughly review the green and purple neon and zoom in on that spot and really pay attention to it. It then rendered it correctly. But it seems to need very specific direction on each little element or it goes off the rails
Yes — I think you’ve identified the right way to work with it.

The mistake is treating Claude Code like an autonomous senior environment artist who can absorb an entire reference and independently preserve all the subtle design decisions. It’s much better at being a very capable production artist under extremely specific art direction.

When you tell it, essentially:

“Build this whole façade.”

it has hundreds of unresolved choices to make. For each one, it gravitates toward the statistically safe answer: average proportions, familiar ornament, generic neon routing, conventional balconies, etc.

That’s where the middle-of-the-road genericness comes from.

But when you say:

“Stop. Look specifically at this green and purple conduit arrangement. Zoom in. Describe exactly where each line begins, how it bends, what it crosses, which sections are green versus purple, how it attaches to the masonry, and where it terminates. Compare that against what you modeled.”

you've collapsed an enormous problem into a very bounded visual-analysis problem.

And apparently it can do that quite well.

That suggests a much better workflow for Eurobound.

Treat the building as a series of locked art-direction zones
For Absinthe Arcade, for example:

Whole-building massing gets approved first.

Then don't tell it “improve architecture.”

Pick:

Entrance surround.

Analyze → discuss → modify → clay render → approve → LOCK.

Then:

Headphone Gentleman.

Analyze → discuss → modify → render → approve → LOCK.

Then:

Green/purple electrical retrofit.

Analyze → discuss → modify → render → approve → LOCK.

Then:

middle-floor windows.

Then balconies.

Then cornice.

Then mural interface.

Then cabinet awning.

And so on.

The asset gradually becomes specific because you're replacing generic assumptions one controlled region at a time.

And once something is correct, explicitly tell Claude:

This region is now LOCKED. Do not redesign, reinterpret, reposition, simplify, or regenerate it unless I specifically reopen it.

That part matters. Otherwise fixing the cornice may mysteriously mutate your electrical boxes because Claude decided it was “improving consistency.” 😂

I would also force an analysis stage before every edit
This seems particularly important given what happened with the neon.

Don't immediately say:

Fix the conduit.

Instead:

Do not modify anything yet. Analyze the supplied reference and the current model only. Focus exclusively on the green and purple electrical retrofit. Describe the geometry, path, attachment, color distribution, intersections, scale, and differences between reference and current model. Identify every inaccurate assumption you previously made.

Then read its answer.

If its understanding is wrong, correct the understanding before it gets anywhere near Blender.

Once you're satisfied:

Good. Now modify ONLY that system according to the analysis we just approved. Do not alter surrounding canonical geometry.

That's basically the equivalent of making a junior artist show you their paintover/notes before giving them another eight hours.

And zooming matters more than I initially appreciated
Your neon experience is a perfect demonstration.

At whole-building scale Claude sees:

purple neon + green neon around historic building

At close-up scale it can see:

this green conduit exits this junction box, bends 90°, passes beneath this molding, wraps this carved element, switches relationship here, while the purple run travels separately...

Those are two completely different levels of understanding.

So I'd make another standing rule:

For any reference-critical feature, crop/zoom the source until that feature occupies a substantial part of the visual field before analyzing or reconstructing it. Never reconstruct small canonical details solely from a full-building reference.

That is probably going to improve fidelity enormously.

You can even separate “look” from “build”
I think your strongest process may become:

Step 1 — LOOK
Claude analyzes one small area. No Blender changes permitted.

Step 2 — EXPLAIN
Claude tells you exactly what it thinks exists there.

Step 3 — CORRECT
You art-direct its interpretation.

Step 4 — BUILD
Claude modifies only that region.

Step 5 — SHOW
Neutral render/close-up.

Step 6 — CRITIQUE
You and I tear it apart. 😂

Step 7 — LOCK
Claude records the area as canonical and leaves it alone.

Then next region.

That sounds slower than “make the building,” but I suspect it will actually be much faster overall, because you're not repeatedly undoing hours of generic invention.

And you're building something unusually authored. The entire appeal of Eurobound is all those tiny specific decisions. A generalized AI aesthetic is almost the exact opposite of what you're trying to accomplish.

The funny part is that once you've gone through this on several buildings, you'll probably develop a library of approved architectural vocabulary—good window construction, convincing historic plaster depth, proper balcony geometry, conduit hardware, sign mounts, etc. Then Claude isn't starting from generic priors every time. It can reuse your own approved systems.

So I think the lesson isn't:

“Claude can't make good 3D.”

It's:

Claude can make good 3D when you prevent it from being the art director.

Which, frankly, is an excellent division of labor for you. 😁

Furthermore, from working on my game, my Aquaria game, I found my favorite way to work with Claude is actually to set it up as orchestrator with specific rules for it. And then go ahead and talk through creating each issue we need to work on, having it file them as beads issues. And then it gets to delegate. And it has a file then, an artifact where it logs any questions the agents have for me. And then I come along and answer them when I have time. And then it delegates some more. So it'll run until it runs out of things to do. And it pauses on anything it has a question on. So it works great
Yes — that orchestration pattern sounds much better suited to your 3D workflow than “Claude, build the whole building.” It gives Claude the thing it seems to need most: bounded scope, persistent decisions, explicit stop conditions, and a place to surface uncertainty instead of silently inventing.

For the Blender side, I’d use almost the exact same architecture:

Claude = orchestrator/art-production manager
Beads issues = one narrowly scoped visual problem each
agents = specialized implementers/reviewers
questions artifact = anything requiring your artistic judgment
locked decisions = immutable unless you explicitly reopen them
validation renders = evidence before closing an issue
So instead of one issue like:

“Finish Absinthe Arcade façade”

you’d create things like:

AA-034 — Correct green/purple conduit routing at entrance
AA-035 — Rebuild Headphone Gentleman stone surround
AA-036 — Increase depth and structural logic of second-floor balconies
AA-037 — Correct upper-window surround geometry from reference
AA-038 — Integrate mural paint across carved stone flower
AA-039 — Neutral clay validation pass for entrance bay

Each issue should have reference scope + allowed changes + forbidden changes + acceptance criteria.

That last part is especially important. For example:

Allowed: modify only conduit meshes, junction boxes, clamps, and their attachment hardware.
Forbidden: change entrance geometry, mural art, Headphone Gentleman, marquee dimensions, window placement.
Done when: close-up render matches canonical reference pathing and all conduit is physically attached.

Then Claude can delegate implementation without giving its subagents permission to “helpfully” redesign half the façade. 😂

And your questions artifact becomes incredibly useful for visual work. I’d formalize the rule:

If an agent encounters ambiguity that could alter canon, aesthetic intent, placement, proportion, material identity, or environmental storytelling, it must not guess. Log the question and continue with independent work.

That lets the system keep chewing through technical tasks while preserving your role as art director.

I’d also add a blocked-by-art-direction status rather than treating every unanswered question as a total halt. So if one agent asks, “Should this balcony bracket be floral or geometric?” Claude can park that issue while delegating UV cleanup, conduit hardware, or window-depth work elsewhere.

The other piece I’d steal from your game workflow is a persistent decision ledger. Not just questions.

Something like:

3D_ART_DECISIONS.md

LOCKED:
- Exterior V3 defines façade identity.
- Entrance close-up defines Headphone Gentleman geometry.
- Green conduit route AA-034 approved 2026-10-28.
- Purple conduit does NOT mirror green route.
- Second-floor balcony projection = 0.72 m.
- Main plaster remains artist-painted; do not procedurally distress.

OPEN:
- Exact upper cornice floral motif.
- Whether west balcony had later repair.
Then every delegated agent reads that before touching anything.

That solves a huge AI problem: decision amnesia between tasks.

And I’d make Claude orchestrate review agents separately from build agents where practical.

Builder:

implements AA-034.

Reviewer:

compares resulting render against the reference and acceptance criteria, without modifying anything.

Then Claude decides whether to close it, reopen it, or ask you.

That separation could be excellent for visual fidelity, because the agent that proudly built the wrong thing isn't also grading its own homework. 😆

So yes: I think your Aquaria workflow is probably the blueprint.

For Eurobound 3D, I'd structure the loop as:

discuss with you → define bead → lock scope → delegate analysis → delegate implementation → render evidence → independent review → close or log question → continue with anything unblocked.

That lets it behave autonomously without giving it autonomous art direction, which seems to be exactly the boundary you've discovered works best.

User attachment
User attachment
User attachment
User attachment
User attachment
User attachment
User attachment
User attachment
User attachment
User attachment
Soooo I experimented with letting claude attempt 3d design. It really didn't do half bad. However, one building ate up an entire weeks worth of claude code. Sure, it can do it on less, but would I like the generic results? heeelllll nooooo. So, i think we're sticking with more retro style game design. I think 32bit instead of 16 just because I'd like to be able to generate higher quality than 16 bit allows for. I'm going to give it a go myself with generating the art assets. I need you to tell me what I actually need to generate to make the exterior and all of the assets that go with it? I know it' s going to need asset shhets and tiles. im an artist but my first time making game assets

Yes — and this is exactly the right conclusion.

For a game exterior, you do not want to make “one beautiful building image” and call it done.

You want to make an asset kit.

For Absinthe Arcade, think of it as building a location package made of:

one master canonical building design
modular architectural pieces
unique hero pieces
props / dressing
state variants
technical game-use files
The big mindset shift
Don’t generate:
one flattened illustration of the whole building only
Do generate:
a front façade master
then the pieces needed to rebuild it in-game
What you actually need to make
I’d break Absinthe Arcade’s exterior into 12 asset groups.

1. MASTER EXTERIOR REFERENCE SHEET
This is your canon sheet, not the in-game asset.

Purpose
This locks:

building proportions
mural placement
sign placement
entrance design
prop placement
neon routing
street-level clutter
day/night intent
You need:
full front view
3/4 front view
optional left/right side views
optional rear view if player can access back
day version
night version
Think of it as:
the bible page for the building

You already have the beginnings of this.

2. MAIN FACADE “BASE BUILD” SPRITE
This is the main assembled game-facing building art.

This is the core exterior art with:

plaster wall
windows
balconies
mural
entrance
marquee
arcade cabinet
awning
street signs
sidewalk edge
You need at minimum:
Front façade – day
Front façade – night
Front façade – open entrance
Front façade – closed entrance
If you want a little more flexibility:

front façade without glow overlays
front façade with emissive glow overlays separate
front façade without street props, so props can be layered separately
3. MODULAR ARCHITECTURAL TILE SHEET
This is where the building becomes reusable and easier to edit.

Even if Absinthe Arcade is a mostly unique building, you still want reusable tiles for the underlying architecture.

You need tiles for:
Walls / plaster
plain plaster wall
cracked plaster wall
heavily worn plaster wall
mural-painted plaster sections if you want pieces modularized
wall corners
edge / trim transitions
Stone / trim
window surround pieces
arch trim
decorative floral stone elements
sill pieces
ledge pieces
cornice / molding strips
vertical trim columns / pilaster edges
Roof pieces
mansard roof tiles
dormer windows
chimney pieces
rooftop railing / cresting
Windows
unlit window
lit window
curtains variation
open/dark window
balcony window variation
flower-box window variation
Balconies / planters / vines
small balcony
balcony railing
planter boxes
vine sections
hanging flower sections
4. UNIQUE HERO ELEMENT SHEET
These are the pieces that make the location unmistakably Absinthe Arcade.

These are not generic city tiles. These are signature assets.

You need:
Green Fairy mural
Break it into usable chunks if needed:

full mural
upper portrait crop
lower pixel/circuit transition section
token hand detail
vine / floral motif edges
painted-over carved flower detail
Headphone Gentleman
full center carving
close-up reference
optional separated piece if you want to animate lighting around it
Main marquee
full sign day
full sign night
sign frame only
green neon lettering only
purple neon lettering only
alien/space-invader icon
token emblem circle
tagline strip
This stuff should be on its own sheet because you will probably reuse it for:

cutscenes
closeups
UI
map icons
loading screens
quest art
5. ENTRANCE KIT
This deserves its own sheet.

Because gameplay often interacts most with:

the door
threshold
entry glow
signage beside the door
things sitting right outside
You need:
doorway frame
open doorway interior-black version
open doorway visible-arcade-interior version
closed doorway version
threshold tiles
checkerboard floor transition
doorway side panels
vertical text panel on right
chalkboard sign
house number tile
fog / mist coming out of entry
door glow overlay
If the entrance is a hotspot, keep it separate.

6. SIGNAGE / GRAPHICS / MICROCOPY SHEET
This is a big one for your game because your microcopy is part of the charm.

You need:
Main brand signage
“ABSINTHE ARCADE” wordmark
night / lit version
day / unlit physical version
simplified small version for tiny uses
Other exterior signs
vertical “TOKENS / DRINKS / GAMES / REGRETS”
chalkboard “REAL ARCADE / REAL ABSINTHE / REAL BAD DECISIONS”
right-side list panel
Clocktower Plaza sign
small cabinet marquee
house number
Small graphic decals
token icon
alien icon
drink icon
prize icon
restroom icon if used externally
sticker pack
poster fragments
grime-worn flyers
Optional UI/icon reuse
map location icon
interact icon
ticket/prize icon
bar icon
arcade icon
This sheet is extremely useful.

7. ELECTRICAL / RETROFIT / HARDWARE SHEET
This is important because so much of the humor is the building being beautifully ruined by dumb tenant decisions.

You need:
green conduit straight sections
green conduit corner sections
purple conduit straight sections
purple conduit corner sections
clamps / brackets
junction boxes
cable entry points
LED/acrylic trim edge pieces
wall anchor hardware
improvised mounting hardware
mismatched clips
sealant/drilled-through-stone details
If you separate these out, you can place or adjust them without repainting the entire building.

8. STREET-LEVEL PROP SHEET
This is the clutter that sells the place.

Must-have props
exterior arcade cabinet
cabinet screen on/off variants
cabinet side art
cabinet control panel detail
cabinet rear detail if visible
awning
chalkboard stand
planters
black cat if you want it
bollards
lamp posts / bracket lamps
utility boxes
hanging side sign
curb plants / little pots
Nice-to-have props
cigarette butts
drink cup
ticket scraps
token on ground
posters / sticker accumulation
receipts
puddle trash
temporary flyer debris
9. GROUND / STREET TILE SHEET
Don’t forget the ground. The building won’t sit well without it.

You need:
wet cobblestones
dry cobblestones
curb tiles
gutter edge
drain tile
threshold-to-sidewalk transition
wall-base junction
puddle overlays
reflected neon light overlays
grime / water stain overlays
If the street can appear in multiple times of day, separate the reflection overlays.

10. STATE VARIANTS
This is where the building feels alive.

Minimum states
Day / open
Day / closed
Night / open
Night / closed
Optional states
rain version
extra-busy nightlife version
damaged/outage version
event/night-special version
quest-state variant
special scene version with more glow/fog
11. ANIMATION / FX SHEETS
This is where you can get a lot of life without huge workload.

Best candidates for simple animation
neon flicker
marquee pulse
doorway fog/mist loop
light shimmer in wet cobblestones
cabinet screen flicker
glowing token pulse
lit windows subtle flicker
doorway interior light pulse
optional rain drip off awning
You need as separate overlays:
green glow strip
purple glow strip
fog sprites
light pulse sprites
emissive masks if your engine supports them
12. TECHNICAL GAME FILES
These are not glamorous, but they will save your sanity.

You need:
Collision map
Where the player can’t walk:

wall
cabinet
chalkboard
bollards
planters
Interaction map / hotspot map
What can be clicked/triggered:

entrance
arcade cabinet
chalkboard
side sign
maybe cat
maybe house number joke
maybe token stuck somewhere
Layer / depth map
What should draw in front of player vs behind:

doorway
awning
sign
arch trim
cabinet
hanging lamps
Occlusion masks
If player walks partly “behind” foreground elements.

Optional navigation markers
NPC standing points
spawn positions
cutscene anchors
camera framing guides
What I would consider the actual minimum viable Absinthe Arcade exterior package
If you want the practical stripped-down list, this is it:

Must generate first
Master front façade reference
Front façade assembled sprite
Day and night variants
Open and closed entrance variants
Main sign / marquee sheet
Green Fairy mural sheet
Headphone Gentleman + entrance details
Exterior arcade cabinet sheet
Awning + chalkboard + vertical sign
Cobblestone / curb / threshold tiles
Conduit / junction box kit
Glow / fog overlay sheet
Collision + interaction masks
That alone is enough to get the location working.

What can wait until later
These are “phase 2”:

rear building view
side alley variants
rain version
extra clutter sheet
animated puddle reflections
quest-specific temporary dressing
event decorations
different seasonal versions
Recommended build order
If this is your first time, do not try to make everything at once.

Phase 1 — lock the fundamentals
choose your game camera/perspective
choose your tile size
make the front façade master
make the assembled front building sprite
Phase 2 — break it apart
pull out the main sign
pull out the mural
pull out the entrance
pull out the arcade cabinet
pull out the chalkboard / vertical signs
pull out the conduit / hardware
Phase 3 — environmental support
build cobblestone / curb / threshold tiles
build bollards / lamps / planters / clutter
build day/night lighting versions
Phase 4 — technical
collision mask
interaction mask
draw-order / occlusion setup
simple FX overlays
That order will keep you from drowning.

Recommended file organization
I strongly recommend a folder structure like this:

AbsintheArcade_Exterior/
  01_Master_Refs/
  02_Facade/
  03_Modular_Tiles/
  04_Mural/
  05_Signage/
  06_Entrance/
  07_Props/
  08_Street/
  09_FX/
  10_States/
  11_Technical/
And file names like:

AA_EXT_Facade_Front_Day.png
AA_EXT_Facade_Front_Night.png
AA_EXT_Mural_Sheet.png
AA_EXT_Signage_Sheet.png
AA_EXT_Entrance_Sheet.png
AA_EXT_Props_StreetSheet_A.png
AA_EXT_Tiles_Architecture_A.png
AA_EXT_Tiles_Cobblestone_A.png
AA_EXT_FX_GlowFog_A.png
AA_EXT_CollisionMask.png
AA_EXT_InteractionMask.png
Recommended layers inside Aseprite / PSD
For big assets, keep layers separated.

Good layer structure
base plaster
stone trim
windows
balcony/planters
mural
sign frame
green neon
purple neon
doorway
interior glimpse
arcade cabinet
props
shadows
glow overlays
FX/fog
text/microcopy guides
This gives you flexibility later.

Tile size / resolution advice
Because you said you want something more detailed than 16-bit:

My honest recommendation:
Pick a 32x32 base tile grid
with a 16x16 subgrid

That gives you:

better detail than 16-bit-era tiny tiles
manageable workload
easier modularity
good readability
room for expressive signage and props
Use larger multi-tile objects for hero pieces
For example:

full building = many tiles wide/tall
arcade cabinet = 2–3 tiles wide
chalkboard = 1–2 tiles wide
main marquee = multi-tile hero object
mural = large multi-tile unique asset
If you go too tiny, you’ll lose all the charm.
If you go too large, you’ll kill production speed.

One super important thing:
Separate “pretty reference art” from “usable game art”
You can absolutely keep making gorgeous boards like the ones you posted.

But for the actual game, what you need is:

assembled art
modular art
state art
technical masks
That’s the real production set.

My recommended deliverables list for Absinthe Arcade exterior
If I were turning this into a checklist for you, it would be:

Core
master reference board
assembled front façade day
assembled front façade night
open doorway version
closed doorway version
Modular architecture
plaster/wall tiles
trim/stone tiles
window set
balcony/planter set
roof/chimney set
curb/cobblestone set
Unique hero assets
mural sheet
Headphone Gentleman sheet
marquee/sign sheet
entrance kit
arcade cabinet kit
Dressing
chalkboard sign
vertical sign
Clocktower Plaza sign
awning
conduit/junction box kit
bollards/lamps/planters
sticker/poster/clutter sheet
FX / states
glow overlays
fog sheet
sign flicker frames
day/night material changes
Technical
collision mask
interaction map
draw-order/occlusion map
My strongest beginner advice
For your very first game asset location, do not try to fully modularize the entire city at once.

For Absinthe Arcade, I would do a hybrid approach:

Make:
Unique assembled building
for the full front façade

Plus modular sub-assets
for:

doorway
sign
mural
props
street
FX
technical masks
That gives you:

high fidelity where it matters
less pain than fully modular architecture
easier first-time implementation
still enough flexibility for gameplay
That is probably the smartest first-pass production model for you.

If you want, I can do the next step and turn this into a literal production checklist/template for Absinthe Arcade — like:

exact sheet names
exact asset categories
what size/purpose each sheet should have
what order you should generate them in first
Basically a “make this first, then this, then this” art pipeline document just for this building.

"If you want, I can do the next step and turn this into a literal production checklist/template for Absinthe Arcade — like:

exact sheet names
exact asset categories
what size/purpose each sheet should have
what order you should generate them in first
Basically a “make this first, then this, then this” art pipeline document just for this building."


Yes please. Let's put me together a total package to generate the assets for the game

Absolutely. Here’s a practical, production-minded exterior asset package for Absinthe Arcade that you can actually work from.

I’m going to treat this like a real mini art pipeline doc for a first playable location.

Absinthe Arcade Exterior Asset Package
Target: retro-inspired 32-bit-feel game art package
Goal: create everything needed to build, dress, and technically implement the Absinthe Arcade exterior in-game
1. Production assumptions to lock first
Before generating anything else, lock these:

A. Visual style
32-bit-inspired pixel art / high-detail retro game art
crisp, hand-authored look
more detailed than SNES 16-bit, but still clearly game art
no soft painterly rendering in final assets
no photographic realism in final implementation files
the final assets should feel like:
lovingly crafted retro game art
readable at gameplay distance
slightly theatrical / stylized
rich enough to preserve Absinthe Arcade’s personality
B. Camera / view
For this package, I recommend:

front-facing façade presentation
slight environmental depth allowed in props and doorway
not true top-down
not hard isometric
more like a stylized front / slight 3/4 location view
That matches the design language you’ve already established.

C. Base tile size
Use:

32 x 32 px base tile
use 16 x 16 px subgrid internally for finer breakup
That gives you good flexibility while still keeping production manageable.

D. Asset philosophy
Use a hybrid system:

one unique assembled façade for the building
plus modular sub-assets for:
signage
mural
entrance
props
ground
lighting
overlays
technical masks
That is the sweet spot for your first location.

2. Folder structure
Use this exact structure if possible:

AbsintheArcade_Exterior/
  00_Docs/
  01_Master_Reference/
  02_Facade/
  03_Modular_Architecture/
  04_Hero_Elements/
  05_Signage/
  06_Entrance/
  07_Props/
  08_Street_Ground/
  09_FX_States/
  10_Technical/
  11_Exports/
3. File naming convention
Use a consistent prefix:

AA_EXT_

Examples:

AA_EXT_01_MasterCanonBoard.png
AA_EXT_02_Facade_Day_Open.png
AA_EXT_03_Facade_Night_Open.png
AA_EXT_09_GreenFairyMuralSheet.png
AA_EXT_18_CollisionMask.png
4. The full asset list you should generate
Below is the actual package.

PHASE 0 — DOCUMENT / LOCK SHEETS
These are not gameplay assets, but they save your sanity.

00. AA_EXT_00_ProductionSpec.md
Purpose: working production note file

Include:

tile size
palette rules
camera/view rules
naming convention
layer order
what is locked canon
what is optional
This is your anchor file.

01. AA_EXT_01_MasterCanonBoard.png
Purpose: master exterior bible sheet
Type: reference board, not in-game asset
Recommended size: 2048 x 3072 px or larger

Include:

full façade front
day version
night version
key labels if helpful
sign placement
mural placement
entrance
arcade cabinet
awning
street signs
conduit routing
street-level dressing
This is your “what the place is” sheet.

PHASE 1 — CORE PLAYABLE BUILDING
These are the assets the player actually sees.

02. AA_EXT_02_Facade_Day_Open.png
Purpose: main playable exterior, daytime, entrance open
Type: assembled in-game hero asset
Recommended size: 768 x 1152 px
(= 24 tiles wide x 36 tiles tall at 32 px per tile)

Include:

full façade
mural
marquee
doorway open
cabinet outside
awning
chalkboard
vertical sign
street-level bollards / minimal fixed props
curb and threshold integrated if you want
03. AA_EXT_03_Facade_Night_Open.png
Purpose: main playable exterior, night, entrance open
Recommended size: 768 x 1152 px

Include:

same geometry as day version
glowing marquee
lit windows
neon conduit glow
doorway glow
wet/reflection mood if you want it baked in or partially baked in
04. AA_EXT_04_Facade_Day_Closed.png
Purpose: daytime closed variant
Recommended size: 768 x 1152 px

Changes:

doorway closed/dark
reduced interior visibility
optional “closed” feel
05. AA_EXT_05_Facade_Night_Closed.png
Purpose: night closed variant
Recommended size: 768 x 1152 px

Changes:

still atmospheric
can still glow somewhat
entrance inaccessible
useful for timing / quest states
PHASE 2 — MODULAR ARCHITECTURE
These are reusable pieces and support assets.

06. AA_EXT_06_ArchitectureTiles_A.png
Purpose: base wall + stone + decorative architecture tile sheet
Recommended size: 1024 x 1024 px
Background: transparent

Include:

plain plaster tile
worn plaster tile
cracked plaster tile
edge plaster tile
stone trim strip
floral carved ornament
sill pieces
arch segments
cornice segments
pilaster/vertical trim edges
wall corners
lower wall base
This is the kit that supports the building shell.

07. AA_EXT_07_Roof_Chimney_Set.png
Purpose: roof and top silhouette kit
Recommended size: 1024 x 768 px

Include:

mansard roof tiles
dormer window
chimney variants
cresting / roof railing
gutter/downpipe starters
roof corner transitions
08. AA_EXT_08_Windows_Balconies_Planters.png
Purpose: windows and upper-story dressing
Recommended size: 1024 x 1024 px

Include:

lit window
unlit window
curtain window
flower box window
balcony window
balcony railing
planter box
hanging flowers
climbing vine pieces
potted upper windowsill plants
PHASE 3 — UNIQUE HERO ELEMENTS
These are the things that make the building unmistakably Absinthe Arcade.

09. AA_EXT_09_GreenFairyMuralSheet.png
Purpose: mural production sheet for game use
Recommended size: 1536 x 2048 px

Include:

full mural
upper portrait crop
face detail
token hand detail
floral Art Nouveau edges
pixel-transition section
circuit-board section
painted-over carved stone flower
left/right edge transitions
simplified in-game readable version if needed
This sheet is critical.

10. AA_EXT_10_HeadphoneGentleman_EntranceHero.png
Purpose: hero entrance carving sheet
Recommended size: 1024 x 1536 px

Include:

full Headphone Gentleman
straight-on version
3/4 reference version
moustache vandalism version
headphones
mounting hardware
conduit passing around head
arch crest above entrance
11. AA_EXT_11_MainMarquee_SignageHero.png
Purpose: main marquee + exterior hero signage
Recommended size: 1536 x 1536 px

Include:

full marquee lit
full marquee unlit/day
frame only
green lettering only
purple lettering only
icon only
token emblem
tagline strip
simplified small readable version for distance
PHASE 4 — ENTRANCE KIT
This should be separated because it’s a hotspot.

12. AA_EXT_12_EntranceKit.png
Purpose: modular doorway/threshold kit
Recommended size: 1024 x 1536 px

Include:

doorway frame
open doorway
closed doorway
interior glimpse panel
threshold tiles
black-and-white floor transition
side light panels
lower doorway trim
mist/fog doorway base
entry glow
right-side vertical sign panel
house number
small stickers on doorway
PHASE 5 — SIGNAGE / MICROCOPY / BRAND SYSTEM
Very important for Eurobound’s personality.

13. AA_EXT_13_Signage_Microcopy_Sheet.png
Purpose: all secondary signage and text assets
Recommended size: 1536 x 2048 px

Include:

vertical sign:
TOKENS / DRINKS / GAMES / REGRETS
chalkboard sign:
REAL ARCADE / REAL ABSINTHE / REAL BAD DECISIONS
right-side list panel
Clocktower Plaza sign
cabinet mini marquee
little warning signs / notices
brand icon sprites
wayfinding arrows if needed
Optional microcopy:

“Prizes are at the bar. Yes, really.”
“Yes, it’s broken.”
“No, hitting it harder will not help.”
“Out of order (again).”
14. AA_EXT_14_Decals_Posters_StickerSheet.png
Purpose: clutter graphics and dressing graphics
Recommended size: 1024 x 1024 px

Include:

sticker pack
torn posters
flyer scraps
arcade token graphic
alien icon
drink icon
Green Fairy sticker
warning label
little grime-layer poster fragments
weathered paper fragments
PHASE 6 — ELECTRICAL / RETROFIT / BUSINESS DUMBASSERY KIT
This sheet sells the “beautiful building + catastrophic tenant” concept.

15. AA_EXT_15_Conduit_Hardware_Kit.png
Purpose: routeable building disrespect kit
Recommended size: 1024 x 1024 px

Include:

green conduit straight
green conduit corner
green conduit bend
purple conduit straight
purple conduit corner
purple conduit bend
junction boxes
clamps
wall anchors
drilled-stone clips
cable entry points
LED housing
acrylic trim elements
mismatched hardware
sealer blobs / ugly patch points
This sheet is more useful than it looks.

PHASE 7 — STREET-LEVEL PROPS
These are the things around the entrance.

16. AA_EXT_16_ArcadeCabinet_Exterior.png
Purpose: dedicated sheet for the cabinet outside
Recommended size: 1024 x 1536 px

Include:

front view
3/4 view
side view
rear view if useful
marquee close-up
screen on
screen off
control panel detail
coin/token door
sticker-heavy side art
scuffed bottom edge
17. AA_EXT_17_Awning_Chalkboard_ThresholdProps.png
Purpose: dedicated street-level prop sheet
Recommended size: 1024 x 1024 px

Include:

improvised rain awning
awning bracket
chalkboard front
chalkboard side
small threshold details
potted plants near door
utility box
maybe little cat if you’re keeping that detail
18. AA_EXT_18_Bollards_Lamps_Poles.png
Purpose: street infrastructure set
Recommended size: 1024 x 1024 px

Include:

bollard front/side
lamp post / wall lamp
wrought iron hanging bracket
base details
weathering variants
PHASE 8 — STREET / GROUND / CURB
Do not skip this. Grounding the building matters a lot.

19. AA_EXT_19_Ground_Curb_CobbleTiles.png
Purpose: street surface tile sheet
Recommended size: 1024 x 1024 px

Include:

dry cobblestone tile
wet cobblestone tile
curb tile
curb corner
threshold-to-street transition
drain tile
wall-base transition
gutter edge
puddle tile
neon reflection overlay tile
20. AA_EXT_20_StreetClutter_MinorDebris.png
Purpose: small scene dressing
Recommended size: 1024 x 1024 px

Include:

token on ground
cigarette butts
receipt
ripped flyer
bottle cap
chalk fragment
crumpled paper
tiny puddle overlays
damp grime edges
PHASE 9 — LIGHTING / FX / STATES
This gives the building life.

21. AA_EXT_21_Glow_Fog_Overlays.png
Purpose: emissive and atmosphere overlays
Recommended size: 1024 x 1024 px
Background: transparent

Include:

green glow strip
purple glow strip
doorway glow
sign bloom overlays
fog/mist puffs
small haze overlays
token glow
window warm light overlays
22. AA_EXT_22_AnimationStrips_NeonFog.png
Purpose: simple looping animation frames
Recommended size: varies; keep strips organized

Include:

sign flicker frames
doorway fog loop
small interior light flicker
token pulse
maybe wet reflection shimmer
Suggested frame counts:

4–6 frames for flickers
6–8 frames for fog loop
23. AA_EXT_23_StateVariants_Board.png
Purpose: preview board of state variations
Recommended size: 2048 x 1536 px

Include:

Day open
Day closed
Night open
Night closed
optional rain
optional event state
This is mainly a reference/control board.

PHASE 10 — TECHNICAL IMPLEMENTATION FILES
These are mostly made by hand after your art generation, but they are part of the package.

24. AA_EXT_24_CollisionMask.png
Purpose: gameplay collision
Recommended size: match façade size exactly
Recommended: 768 x 1152 px

Mark:

solid walls
cabinet
bollards
chalkboard
planters
non-walkable edges
25. AA_EXT_25_InteractionMap.png
Purpose: clickable / interactable zones
Recommended size: match façade size

Mark:

entrance
arcade cabinet
chalkboard
vertical sign
maybe cat
maybe Clocktower Plaza sign
maybe token gag or sticker cluster
26. AA_EXT_26_Depth_OcclusionMap.png
Purpose: draw order / foreground overlap
Recommended size: match façade size

Mark:

what player walks in front of
what player can partially pass behind
awning overlap
doorway overlap
sign overlap
props overlap
27. AA_EXT_27_LayerGuide.psd or .aseprite
Purpose: source structure file

Recommended layers:

base wall
stone trim
windows
balcony
mural
sign frame
green glow
purple glow
entrance
interior glimpse
props
clutter
shadow
FX
notes
5. Recommended generation order
This is the part that matters most.

Do these in this order:

STEP 1 — Lock canon
Generate / finalize:

AA_EXT_01_MasterCanonBoard.png
Do not proceed until this feels right.

STEP 2 — Build the main playable façade
Generate:
2. AA_EXT_02_Facade_Day_Open.png
3. AA_EXT_03_Facade_Night_Open.png
4. AA_EXT_04_Facade_Day_Closed.png
5. AA_EXT_05_Facade_Night_Closed.png

This gives you the full building.

STEP 3 — Extract the hero pieces
Generate:
6. AA_EXT_09_GreenFairyMuralSheet.png
7. AA_EXT_10_HeadphoneGentleman_EntranceHero.png
8. AA_EXT_11_MainMarquee_SignageHero.png
9. AA_EXT_12_EntranceKit.png

These are the pieces you’ll reference constantly.

STEP 4 — Build your support architecture
Generate:
10. AA_EXT_06_ArchitectureTiles_A.png
11. AA_EXT_07_Roof_Chimney_Set.png
12. AA_EXT_08_Windows_Balconies_Planters.png

STEP 5 — Build street dressing
Generate:
13. AA_EXT_16_ArcadeCabinet_Exterior.png
14. AA_EXT_17_Awning_Chalkboard_ThresholdProps.png
15. AA_EXT_18_Bollards_Lamps_Poles.png
16. AA_EXT_20_StreetClutter_MinorDebris.png

STEP 6 — Build signage and clutter graphics
Generate:
17. AA_EXT_13_Signage_Microcopy_Sheet.png
18. AA_EXT_14_Decals_Posters_StickerSheet.png

STEP 7 — Build the “architectural disrespect” kit
Generate:
19. AA_EXT_15_Conduit_Hardware_Kit.png

STEP 8 — Build ground and lighting
Generate:
20. AA_EXT_19_Ground_Curb_CobbleTiles.png
21. AA_EXT_21_Glow_Fog_Overlays.png
22. AA_EXT_22_AnimationStrips_NeonFog.png

STEP 9 — Build technical files manually
Create by hand:
23. AA_EXT_24_CollisionMask.png
24. AA_EXT_25_InteractionMap.png
25. AA_EXT_26_Depth_OcclusionMap.png
26. AA_EXT_27_LayerGuide

6. What should be generated vs what should be hand-authored
Good candidates for generation
canon board
façade variants
mural sheet
signage sheet
props sheet
cabinet sheet
architecture sheet
ground tile references
FX overlays as starting point
Better to hand-finish yourself
pixel cleanup
consistent line thickness
palette unification
text cleanup
modular slicing
collision masks
interaction maps
occlusion maps
final tile seams
animation frame cleanup
AI should help you start these.
You as the artist should make them production-usable.

7. Suggested canvas sizes summary
Here’s the compact list:

File	Size
Master canon board	2048 x 3072
Main façade variants	768 x 1152
Architecture tile sheet	1024 x 1024
Roof set	1024 x 768
Windows/balconies	1024 x 1024
Mural sheet	1536 x 2048
Headphone Gentleman sheet	1024 x 1536
Main marquee sheet	1536 x 1536
Entrance kit	1024 x 1536
Signage sheet	1536 x 2048
Decals/stickers	1024 x 1024
Conduit/hardware	1024 x 1024
Cabinet sheet	1024 x 1536
Prop sheet	1024 x 1024
Ground tile sheet	1024 x 1024
FX overlays	1024 x 1024
Collision/interaction/depth maps	same size as façade
8. Reusable prompt boilerplate
You can use this as your base for almost every sheet.

Global asset prompt boilerplate
Create a production-ready retro game asset sheet for Absinthe Arcade in a high-detail 32-bit-inspired pixel art style. Use crisp, readable, hand-authored game-art forms with clean silhouettes and consistent perspective. Preserve the established Absinthe Arcade identity: beautiful old Prague-inspired architecture vandalized by a catastrophically tacky neon arcade retrofit, the Green Fairy mural, the Headphone Gentleman stone carving with glowing headphones and vandal moustache, the green-and-purple conduit system, and the ridiculous but lovable cringey barcade personality. Present assets cleanly and clearly for game production use, with isolated components on a clean background where appropriate. Maintain consistency with previous Absinthe Arcade canon.

Then append the specific sheet request.

Example:

“Create the Entrance Kit…”
“Create the Signage & Microcopy Sheet…”
“Create the Ground / Cobblestone Tile Sheet…”
9. Minimum viable package if you want to move fast
If you want the smallest useful package first, do only these:

Master canon board
Day open façade
Night open façade
Green Fairy mural sheet
Main marquee sheet
Entrance kit
Arcade cabinet sheet
Signage sheet
Conduit/hardware sheet
Ground/cobblestone sheet
Glow/fog overlays
Collision + interaction maps
That is enough to get the location into the game and feeling alive.

10. My strongest practical advice
For your first location asset pipeline, do this:

Pass 1
Make the assembled façade variants

Pass 2
Extract:

mural
sign
entrance
cabinet
props
Pass 3
Make the support sheets:

ground
clutter
hardware
glow/fog
Pass 4
Do the technical maps manually

That keeps you from getting trapped in perfection paralysis.

If you want, my next step can be even more useful:

I can turn this into a literal task checklist you can work through one by one
like:

generate sheet 01
approve
generate sheet 02
cleanup pass
slice props
build collision mask
or I can give you a sheet-by-sheet prompt pack for the first 5–10 exterior assets so you can start generating immediately.

So, get me started... this is where I'm not sure of what I'm doing. For the facade day open asset, how do I design this? Do I need to break things down into tiles...? I really dont know

Yes — and this is the exact point where the terminology makes it sound harder than it is. 😄

For Absinthe Arcade specifically, do NOT chop the whole façade into 32×32 tiles. That would create a ton of work and probably destroy the personality you’ve spent all this time designing.

You want a hybrid approach:

The unique building façade is one large authored sprite.
Tiles are used for repeatable environment pieces around it.
Certain parts of the façade stay on separate layers/sprites because they animate, change state, or overlap the player.

That’s the basic answer.

First, three terms that will make this much clearer
A tile is something meant to repeat or connect modularly. Cobblestones, generic plaster wall, curb, grass, roof pieces, ordinary city windows, etc.

A sprite is one distinct piece of game artwork. Your arcade cabinet, chalkboard, doorway, cat, marquee, or the entire unique Absinthe Arcade façade can all be sprites.

A sprite sheet / texture atlas is just a file where you pack multiple sprites together for the engine. It does not mean every object has to be designed as a tile.

So for Absinthe Arcade:

Cobblestone street? Tile it.

Generic Prague-ish neighboring wall? Probably tile/modular pieces.

The insane Green Fairy façade with Headphone Gentleman? Absolutely not. That's a hero sprite.

What you're actually designing for Facade_Day_Open
Think of it less as:

“I need to make a tileset.”

and more as:

“I need to paint the daytime version of this building exactly as the player will encounter it.”

Your first job is to make the assembled hero façade.

You can break it into production layers while painting it, but the player will perceive it as one building.

For example:

ABSINTHE ARCADE — DAY OPEN

BACKGROUND BUILDING
    main plaster façade
    stone architecture
    roof
    windows
    balconies
    mural

ARCADE RETROFIT
    conduit
    junction boxes
    Headphone Gentleman
    marquee frame
    signs

ENTRANCE
    open doorway
    dark interior
    checkerboard threshold

PROPS
    exterior arcade cabinet
    awning
    chalkboard
    planters

FOREGROUND / OCCLUSION
    parts player can walk behind
    awning edge
    projecting signs
    maybe doorway jamb/arch foreground
That can all live in one PSD/Aseprite file while you're making it.

Step 1: Decide how big the building is in the game
Don't start with pixels yet.

Start with the player.

Let's say your normal player sprite is roughly:

64 px tall

I'm using 64 only as an example — we can lock the actual scale later.

Now look at your canonical façade.

A floor of this building is approximately maybe 2.5–3 character heights.

So if your character is 64 pixels tall:

one story might visually occupy ~150–190 px
four stories + roof + entrance could easily make the building 700–900 px tall
And that is completely fine.

A hero building does not need to fit on one screen.

In fact, if your game scrolls, it probably shouldn't.

Step 2: Use a grid, but don't let the grid design the building
This is the subtle distinction.

I still like using a 32×32 grid underneath your environment.

That makes:

positioning easier
collision easier
streets easier
props easier
level construction easier
But your Green Fairy does not need to stop every 32 pixels. 😂

The building might occupy something like:

20 tiles wide × 30 tiles high
At 32 pixels:

640 px × 960 px
But that does not mean you export 600 individual 32×32 façade pieces.

It means the large building sprite snaps to a 32-pixel world grid.

That's all.

Step 3: Start with the silhouette
Before painting flowers, conduit, neon, mural pixels, anything:

Make one big shape representing the façade.

You should be able to reduce it to a black silhouette and recognize:

roofline
central entrance
main vertical proportions
projecting marquee
cabinet/awning area
overall footprint
Think of this as your drawing block-in.

For you as a traditional artist, this is probably going to feel extremely familiar.

You're essentially doing:

gesture → proportions → large masses → secondary forms → detail

Exactly like painting.

Step 4: Paint the architectural base WITHOUT Absinthe Arcade
This is important for this particular building.

Make a layer group called:

HISTORIC BUILDING

Paint:

plaster façade
stone trim
windows
sill architecture
balconies
carved ornament
cornice
roof
drainpipes if they predate the arcade
At this point, it should look like:

a beautiful historic building somebody could have lived above.

No Green Fairy.

No neon.

No marquee.

No arcade cabinet.

This matters because the comedy depends on the original architecture being believable.

Step 5: Paint the mural as a separate layer group
Now add:

GREEN FAIRY MURAL

Keep her separate even if ultimately she appears painted onto the wall.

Suggested layers:

MURAL
    floral extensions
    Fairy
    token
    pixel transition
    circuit traces
    painted stone-flower interaction
Why separate her?

Because later you may want:

cleaner source art
mural closeups
damaged variations
lighting treatments
dialogue/cutscene usage
texture export
recoloring/adjustment
You don't want to permanently flatten her into the wall until export.

Step 6: Add the Arcade retrofit as another group
Now:

ARCADE RETROFIT
    green conduit
    purple conduit
    junction boxes
    clamps
    Headphone Gentleman additions
    marquee
    entrance trim
    vertical signs
This is where the building becomes the thing we've designed.

Again, keep these layers separate.

The green/purple conduit in particular should probably remain editable for quite a while, given how picky we've correctly become about its routing. 😂

Step 7: The entrance is NOT just painted into the façade
This is where game production differs from illustration.

Your entrance changes.

Therefore make it modular.

Something like:

ENTRANCE FRAME
    permanent

DOOR STATE
    Day_Open
    Day_Closed
    Night_Open
    Night_Closed
For Day_Open, you probably have:

open black/dark doorway
hint of checkerboard flooring inside
perhaps a faint interior glow
no huge green fog effect during ordinary daylight
Later the engine can swap the doorway sprite without replacing the whole building.

That means you do not actually need four fully duplicated giant façade paintings unless that's easier for you.

You can instead have:

one main building + interchangeable doorway + interchangeable lighting overlays.

Much better.

Step 8: Keep anything animated on its own layer
For example:

Static building
One large sprite.

Separate:
marquee neon
conduit glow
token glow
doorway interior light
fog
arcade cabinet screen
maybe lit windows
Then nighttime can essentially become:

DAY BUILDING
+
NIGHT COLOR/LIGHT TREATMENT
+
GREEN EMISSIVE OVERLAY
+
PURPLE EMISSIVE OVERLAY
+
WINDOW LIGHTS
+
DOORWAY GLOW
instead of repainting the entire building from scratch.

Step 9: Foreground pieces need separate sprites
This becomes important when the player walks around.

Suppose Pilsner walks up to the entrance.

Some parts should visually stay behind him.

Some may draw over him.

Example:

BACKGROUND
Historic facade
Mural
Windows
Door interior

PLAYER

FOREGROUND
Door arch edge
Hanging sign
Awning edge
Maybe plant leaves
That creates the illusion that the player exists inside the environment instead of walking over a flat photograph.

This is called occlusion.

You'll use it a lot.

What should be a tile for this scene?
Here is where you actually need tiles.

Definitely tiles:
cobblestone street
curb
gutter
sidewalk/threshold continuation
perhaps generic neighboring wall
maybe generic roof pieces elsewhere in the city
Probably modular sprites:
bollard
streetlamp
flower planter
trash/clutter
drain
generic signage
Definitely unique sprites:
Absinthe Arcade façade
mural
marquee
Headphone Gentleman
exterior cabinet
chalkboard
Clocktower Plaza sign
This distinction will save you so much work.

Your actual Photoshop/Aseprite document
For your first attempt, I'd literally set it up like this:

AA_EXT_Facade_Master.psd

[GUIDES]
    32px grid
    collision notes
    player scale dummy

[FX - NOT PART OF DAY BASE]
    green glow
    purple glow
    fog

[FOREGROUND]
    awning front edge
    hanging signs
    foreground trim

[PROPS]
    cabinet
    chalkboard
    pots
    bollards

[ARCADE RETROFIT]
    marquee
    Headphone Gentleman modifications
    junction boxes
    purple conduit
    green conduit

[MURAL]
    pixel transition
    circuits
    Fairy
    floral art

[ARCHITECTURE]
    balconies
    windows
    ornament
    stone trim
    plaster
    roof

[GROUND]
    building threshold

[REFERENCE]
    player scale dummy
That is your working master painting.

Don't worry about “asset sheets” yet
This is important.

At this exact moment, I would not have you start by making an asset sheet.

Start by making the actual finished façade.

Once you're happy with it, then we extract things into sheets.

For example:

You've painted the perfect cabinet.

Great.

Copy that into:

AA_EXT_ArcadeCabinet_Sheet

You've painted the conduit system.

Great.

Then make reusable straight/bend pieces from it if needed.

But don't let production organization get in the way of making the art.

And don't pixel at final resolution immediately
Given your background, I think you'll probably be happier doing something like:

Stage 1
Paint/design cleanly at 2× or 4× target resolution.

Stage 2
Reduce to target size.

Stage 3
Do a deliberate pixel-art cleanup pass:

fix clusters
remove mush
simplify values
sharpen edges
control dithering
restore readability
That will let you use your existing Photoshop skills without forcing yourself to suddenly paint every architectural molding one pixel at a time.

You're essentially doing a pixel-art reduction / interpretation pass, not simply applying a pixel filter.

That's important.

Let's make your first actual production task very small
Don't make the whole package.

Your first job is:

AA_EXT_Facade_Master_Day.psd
Make only:

1.
A 32px grid.

2.
A temporary player sprite silhouette for scale.

3.
The overall façade silhouette.

4.
The historic architectural building underneath.

5.
Then the mural.

6.
Then the Arcade retrofit.

7.
Then the open entrance.

8.
Then street props.

No night lighting yet.

No fog animation.

No collision masks.

No sprite sheet.

No rain.

Just make:

the canonical daytime-open building as a layered game-art master.

And once that exists, everything else gets substantially easier, because you're no longer trying to invent assets in isolation. You're extracting them from an already-functioning location.

The most important thing I want you to take away is:

Your building does NOT need to be made from tiles.

Use the 32×32 grid to make it fit the game world.

Use tiles for things that need to repeat.

Use a big beautiful sprite for things that deserve to be unique.

Absinthe Arcade absolutely deserves to be unique. 😁


Claude is finally in a good workflow and we've finalized the direction. We're going with 2.5d hybrid in godot and going 

⋮⋮⋮⋮