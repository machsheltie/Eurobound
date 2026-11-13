# Eurobound asset team: brief

You are one art agent on a team of up to six. The orchestrator (the main session, `eurobound-c8`) gives you **one asset**. You make it, save it, commit it in your own git worktree, clean up, and report back. Then you end. A fresh agent takes the next asset. Read this whole file before you start.

## 1. Read first (required, in this order)

1. `README.md` (repo root).
2. `CLAUDE.md` (repo root) and `.claude/CLAUDE.md`. The content rules there are binding: an MA satire, parody place names only, real brand names keep their real names, money is SOVS, no mascots, no nudity, no people painted into rooms.
3. This brief, then the style guide for your asset kind (section 4).
4. Your asset's description, at the doc and line the orchestrator gave you. The description is canon. Draw what it says. For a location, the line is only where to start: read the building's whole file (section 2, "Every building is a parody").

`PRODUCT.md`, `DESIGN.md` and an `EquoriaBible/` folder do not exist in this repo, so skip them. If you ever meet an `EquoriaBible` folder, read it if useful but **never change anything inside it**.

## 2. The look

Eurobound is a **2.5D HD-2D hybrid**: pixel-art characters standing in painterly 3D dioramas, like *Star Ocean: The Second Story R* and *Bravely Default 1 and 2*. Look at the style references in `dev/asset_team/style_refs/` before you generate anything:

- `_contact.jpg`: the whole look on one sheet.
- `exterior_front_day.jpg` / `exterior_front_night.jpg`: a finished building face (Absinthe Arcade). It is a straight-on **orthographic** painted elevation, rich and painterly, with Art Nouveau and Bohemian details, neon added later and visibly fastened on.
- `interior_hall_*.jpg`, `interior_taproom_night.jpg`, `interior_restroom_day.jpg`: finished interiors. They use a **high three-quarter camera looking down about 30 to 40 degrees**, Bravely Default style, painterly HD, warm practical light plus neon accents, real open floor, and **no people**.
- `sprite_*.png`: finished 128x128 character sprites (the bros, and Cara, an NPC). Semi-realistic proportions (4 to 5 heads), crisp dark outline, flat cel shading, readable faces. FFX-2 Remastered detail bar. Not chibi.

Match these. Painterly HD for places, crisp pixel art for characters and item icons. Never photoreal, never flat vector, never anime chibi.

### Every building is a parody, built from its own file (author, 2026-11-12, binding)

The author: "We should be following the guide within each buildings files which tell you what the interior and exterior should look like complete with color schemes. And our buildings shouldn't look like proper respectable businesses and buildings. They should be a bit over the top. Play into parody and satire on the area. Lay into the theme for each location. Don't just go 'well, this is fake Prague. Let's Prague it up.' It's a video game. Not a historical depiction."

So, for every location plate:
1. **Read the building's whole file, not one paragraph.** That means everything under `## Visual Design` (exterior, interior and every named sub-area), **`### Technical Specifications` → `Color Palette`**, and everything under `## Satirical Design` (Theme & Vibe, Cultural Targets, Seedy Underbelly). Also read its PNG asset spec if one exists: `design/worlds/<city>/PNG_Assets/<Name>_PNG_Assets.md`, or the venue doc's own PNG section.
2. **The palette is binding.** Build the image from the doc's hex colours: the Primary colour dominates, the Accent colour draws the eye, and the Background colour sets the ground. Put the hex values in your prompt by name, and check the result against them. If the plate's main colours aren't the palette's, it fails review.
3. **Over the top, never respectable.** The building itself tells the joke. Exaggerate its theme in the architecture: its shape, scale, signage, props and decay. A döner shop looks like a temple to meat; a hostel looks held together by passive-aggressive notes. Take the satire section's targets and make them visible. Video-game readable and a little absurd, like a JRPG town, not a tidy historical streetscape. The city's style (Bohemian, Dutch canal house) is seasoning, not the point: don't just "Prague it up" or "Amsterdam it up".
4. Neighbouring placeholder buildings stay plain and unnamed, so the hero building pops.
5. In your report, list the palette hex values and where each one appears, and name the two or three satire beats you made visible.

### Plan first, then paint (author, 2026-11-12, binding)

The author: "From now on agents are supposed to tell me their plan for each building based on its files before proceeding to make it as I don't want respectable Prague. I want Debaucheryville. Land of scandalous activities. Debauchery. Seediness. Over the top design that smacks of what each location is. I want cleverness and satire and parody." Also: "most of the buildings so far are boring af", and "every new building should be relying on its design files to lean into what they're to be and look like. It shouldn't just be generic design. If you need guidance, ask".

Every location goes in two separate agent jobs:
1. **Plan job (no image generation).**
   - **Read all nine files for the location** (author, 2026-11-12: "Each location has an original md then they have 8 files in the sub folders within their cities folder. All should be reviewed by the agent working on each building."):
     - the main `design/worlds/<city>/<stem>.md`;
     - its files in `core/`, `environment/`, `interactions/`, `items/`, `location_nodes/`, `npcs/<Location>/` (every file in that folder), `PNG_Assets/` and `sprite_mapping/`, plus any match in `events/`.
   - Find them by globbing the city folder for the file stem AND for the `location_id`.
   - In the plan, list every file read and mark any that don't exist as MISSING.
   - Read the building's whole file and its PNG asset spec. Load the `eurobound-satire-voice` skill for tone.
   - Write `dev/asset_team/plans/<id>_plan.md` (at most 300 words) with these sections:
     - **Hook**: the file's own parody hook, in one line.
     - **Palette**: hex values and where each one goes.
     - **Exterior**: shape, storeys, roofline, signs (doc text only), props, staging, and how it differs from `existing_exteriors_contact.jpg`.
     - **Interior**: every named sub-area, floor, light.
     - **Satire beats made visible**: 3 to 5, each citing a doc line.
     - **Not in the file, needs approval**: as questions.
   - Commit only the plan. The orchestrator posts it to the Eurobound Desk.
2. **Paint job**, only after the author approves the plan. Paint exactly the approved plan, with the author's notes applied.

Over the top means the building itself is the joke: scandalous, seedy, debauched, clever, never a tidy historical street.

## 3. Tools

Priority order for image generation:

1. **Adobe Firefly** (browser; the author's account has unlimited generations). Use the model **GPT Image 2.5 Sunburst** with **Quality: High** (the author called it "GPT Image 2.6 Sunburst"; 2.5 Sunburst is the newest Sunburst Firefly lists). **Start from the Firefly HOME screen, https://firefly.adobe.com/** (2026-11-12: the /generate/images page now lists only Firefly Image 3 and 2; the home screen's prompt box still offers Partner models with Quality High, 16:9 and 2K). The home prompt box can show other agents' reference attachments (shared account state): remove every reference that isn't yours before each Generate. Older route, if the home screen ever fails: on https://firefly.adobe.com/generate/image **wait until the page has fully loaded and the Model field shows a model name** (if you open the dropdown too early it lists only the Adobe models and no Partner models, which looks like a lost plan but is not: reload, wait ~5 s, try again; never report a paywall until you have done this twice), then open the **Model** dropdown under General settings. The list opens on the Adobe models (Firefly Image 5, 4 Ultra, 4, 3), and the mouse wheel does NOT scroll it. **Drag the list's own scrollbar down** past "Custom models" to **"Partner models"**: Gemini 3.1 (Nano Banana 2), GPT Image 2.5 Flare, **GPT Image 2.5 Sunburst**, GPT Image 2, GPT Image 1.5, Gemini Nano Banana 2.1 and others. Click GPT Image 2.5 Sunburst, then set **Quality** (the dropdown under Aspect ratio) to **High**. "Reference images (0/6)" below takes up to 6 reference uploads. Firefly Image 3/4/5 are NOT the house model: they come out photoreal. Don't settle for them. For relights and local edits of an image you already like (for example a night version of a day plate), use **Gemini 3.1 (Nano Banana 2)** (Nano Banana Pro family): it holds the image, while GPT Image redraws everything. **Never draw the asset yourself in code (Pillow) instead of generating it.** Code is for cleanup only: downsampling, palette, cutout, splices. If generation fails three times, stop and report.
2. **ChatGPT**: allowed again (author, 2026-11-13 evening, via the Absinthe Orchestrator: "You can use ChatGPT. Just x off the pay thing."). Use it for edits Firefly fails at. If a payment or upgrade dialog appears, close it with its X. Never enter payment details and never subscribe.
3. **PixelLab** (MCP server `pixellab`, or `Tools/sprite_pipeline/pixellab_client.py`): pixel-art conversion, character rotation and animation. It has 8 job slots shared by the whole team, so run at most 2 jobs at a time.
4. **scenario.com** and **ludo.ai** are open in the author's browser. Use them only if the three above can't do the job.

Local tools: Aseprite (`C:/Program Files/Aseprite/Aseprite.exe`, CLI `-b`), Python with Pillow, `Tools/art_cleanup/` (cutout, palette, review sheets; see its README), `Tools/sprite_pipeline/` (see `design/style_guides/character_sprite_pipeline.md`).

### Driving the browser (Firefly, ChatGPT)

- Load the Chrome tools with ToolSearch in **one** call: `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__find,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__tabs_close_mcp`.
- Call `tabs_context_mcp` with `createIfEmpty: true`, then **open your own new tab** (`tabs_create_mcp`) and go to https://firefly.adobe.com/generate/images. Other agents use the same Chrome. Never touch tabs you didn't open. Close your tabs when you finish.
- Read pages as text (`find`, `read_page`) and screenshot only to confirm a result. Use `scale: 0.5` screenshots.
- **0x0 viewport or screenshots timing out?** Run `[window.innerWidth, window.innerHeight, window.screenX]` in your tab. If screenX is about -32000 or -21333, the agents' Chrome window is minimized. Don't drive the page blind: send `main` "CHROME MINIMIZED" and wait; the orchestrator restores it. A background tab reporting 0x0 while screenX is normal is fine; bring your own tab to the front.
- Never trigger alerts or dialogs. Never accept new terms, never buy anything, never enter credentials. If Firefly asks you to sign in or shows a paywall, stop and report it.
- **Getting files in and out of Firefly.** Firefly's file input sits in a shadow DOM and it blocks anchor downloads. Use the local CORS server:
  `python dev/asset_team/cors_server.py <serve_dir> <inbox_dir> <port>` (run it in the background; use the port the orchestrator gave you, so agents don't collide). Inject a reference image by fetching `http://127.0.0.1:<port>/<file>` in the page and setting it on the file input with a `DataTransfer`. Save a result by fetching the generated image's blob in the page and `POST`ing it to `http://127.0.0.1:<port>/<name>.png`; it lands in `<inbox_dir>`. If Chrome asks to allow local network access, that's a human-only prompt: report it and stop.
- **Saving home-screen Firefly results (2026-11-12):** the result image sits on a signed Adobe CDN URL (in-page fetch is CORS-blocked, canvas export is tainted), so the CORS POST fails. Use Firefly's own **Download** button (plain image; stop if it asks to accept terms, sign in or upgrade). The file lands in `C:\Users\heirr\Downloads`: take the newest, Read it to confirm it's yours, then **move** it into your worktree. Don't put id tags in prompts (one got painted into an image); take your result from your own tab's result panel right after it renders, not from the shared history. For the night relight, open your day result in Firefly and use its edit / use-as-reference action with Gemini 3.1 instead of uploading.
- **Aspect ratio must match the input** when you edit an image, or the model squeezes it. GPT Image 2.5 Sunburst only offers 3:2 and 1:1: generate 3:2 and crop or extend to 16:9, never squeeze.
- **Shared Firefly state:** other agents use the same Firefly account in other tabs, and Firefly can carry prompt and reference state between tabs. Before every Generate, check that the model, prompt and reference images in your tab are yours.
- **Painterly, not photographic.** Prompts that just describe a room come back photoreal. Always upload one or two `style_refs/` plates as Firefly reference images, and say so in words: "hand-painted digital matte painting, HD-2D JRPG background in the style of Octopath Traveler and Bravely Default, visible painterly brushwork, stylized; NOT a photograph, NOT photorealistic, NOT a 3D render". Interiors use a high three-quarter camera looking down about 35 degrees, with the whole floor visible.

### No look-alikes (author, 2026-11-12)

The author: "be sure we aren't making the tiered floor identical or near identical from building to building". Before you prompt, open `dev/asset_team/style_refs/existing_exteriors_contact.jpg` and `existing_interiors_contact.jpg` (every finished plate), and make yours clearly different from all of them, not only from its neighbours:
- **Exteriors:** vary the storey count and storey heights, window rhythm and shape, ground-floor shopfront, and roofline. Shamsterdam already has five stepped gables, so use the other canal-house types too: bell, neck, spout, plain cornice, or a flat-fronted modern infill. Debaucheryville already has four near-identical three-storey cream stucco blocks, so vary the material, colour, height and ornament. Don't default to the same staging (canal railing in front, tree on the right, lamp post on the left). Change the street furniture and the angle of the street.
- **Interiors:** vary the floor. About six rooms already have a glossy checkerboard floor, so use a different material and pattern (planks, herringbone, terrazzo, tiles of another shape, sawdust, carpet, concrete) unless the doc names checkerboard. Also vary the floor plan (levels, stairs, mezzanines), ceiling and light colour.
- In your report, name the closest existing plate and say how yours differs.

## 4. What "done" means for each asset kind

Put files under the paths below (create folders as needed; snake_case, no spaces). `<city>` is `debaucheryville`, `publandia`, `shamsterdam`, `sinfonia` or `shared`. `<id>` is the asset id the orchestrator gave you.

### A. Character sprite (NPC, villain, enemy)
Follow `design/style_guides/character_sprite_pipeline.md` (binding). Deliver:
1. A Firefly **model sheet** (front, side, back, full body, neutral pose, flat background) at `Assets/Graphics/sprites/characters/npcs/<city>/<id>/<id>_model_sheet.png`.
2. The PixelLab **128x128** sprite, reinterpret mode, face pass (3 seeds, pick the best), rotated to **8 directions**, baked shadow removed, palette locked. Hand-place any lettering. Packed with `pack_aseprite.lua` into `game/assets/characters/npcs/<city>/<id>.aseprite` (stills, tags `idle_<dir>`; animations are a later stage unless the orchestrator asks).
3. A **review sheet** (`art_cleanup.py sheet`: checker, dark, light, magenta) at `dev/asset_team/reviews/<id>_review.png`, plus `dev/asset_team/reviews/<id>_compare.png`: the model sheet front view beside the south sprite at 4x nearest.
4. Add the character's description file to `Tools/sprite_pipeline/characters/<id>.txt`.
Enemies with a battle sprite follow the existing `game/assets/characters/enemies/<city>/<id>_battle_w.png` pattern (west-facing battle pose) if the orchestrator says "battle sprite".

### B. Location exterior
Deliver painterly HD-2D plates in the Arcade's style:
1. **Hero view, day**: the building (or the outdoor place) from the game's fixed tilt camera, about 30 to 40 degrees down, narrow field of view, building centred and complete, **no people, no vehicles in motion, no readable text except text the description gives**. 16:9, at least 2048 px wide. `game/assets/worlds/<city>/<id>/exterior/<id>_ext_day.png`
2. **Hero view, night**: a Nano Banana Pro relight of the day plate (same framing, pixel-registered as closely as you can; register with `Tools/content_generation/absinthe_arcade/hd2d/register_to.py` if they drift). Neon, windows and lanterns lit. `.../<id>_ext_night.png`
3. **Front elevation, day**: a straight-on orthographic painting of the main facade (no perspective), for the painted-box diorama. `.../<id>_ext_front_elevation_day.png`
4. A review sheet: the three plates side by side, at most 1600 px wide, at `dev/asset_team/reviews/<id>_ext_review.jpg`.
Neighbouring buildings are placeholders: plain, anonymous facades (shutters, doors, windows) that fit the street, with no names or signage. ("Scaffolding" in older notes meant placeholder; never paint literal construction scaffolding or tarps unless the description asks for it.)

### C. Location interior
1. **Interior plate, day** (or the venue's real hours if it only opens at night): same camera as the Arcade interiors, high three-quarter view, 16:9, at least 2048 px wide, straight rows and real open floor, **no people painted in** (patrons become NPCs later). `game/assets/worlds/<city>/<id>/interior/<id>_int_day.png`
2. **Interior plate, night**: Nano Banana Pro relight, **resized to exactly the day plate's pixel size** (Gemini returns 2752x1536; Sunburst 2560x1440). `.../<id>_int_night.png`
3. Review sheet at `dev/asset_team/reviews/<id>_int_review.jpg`.

### D. Item icon
**Superseded for new icons (author, 2026-11-12): "use tripo/blender from here on out and stop pixel art".** New icons are Tripo models rendered in Blender in the author's final look B ("cleaner, higher-res 3D renders (no pixelation)", Desk 2026-11-12), with the Sprite team's look (`tools/char3d/look.py`), under `tools/char3d/README.md` "Keep usage low". **Approved look (author, 2026-11-13, on the Crown & Cask trial): "Yes, this is the look: make all icons this way".** Recipe: `Tools/item3d/README.md`. Firefly reference, then Tripo image-to-3D (55 credits), then Retopo to 20k triangles (35), then GLB, then headless Blender `Tools/item3d/render_item.py` with `look.py`, fixed ortho scale 0.95, giving `game/assets/items/icons/3d/<id>_512.png` + `_128.png`. Match your Tripo task by its thumbnail or prompt, never "the newest". **Tripo website only. The Tripo API and every pay-per-use API are forbidden (author, 2026-11-13: "We may not use the Tripo API... I do not like paying API costs").** Log credits per icon in your report. The pixel rules below are kept only for maintaining approved icons.
Follow `Assets/Graphics/items/_EUROBOUND-ITEM-ART-STYLE-GUIDE.md` (binding: EarthBound-flavoured SNES item sprite, clay-model forms, 16 colours, plum-brown outline, magenta key, illegible lettering). Its per-item spec, if one exists, is `Assets/Graphics/items/<slug>.md`. Deliver `game/assets/items/icons/<id>_128.png` (master) and `<id>_64.png` (nearest-neighbour), both with alpha, 16 colours or fewer, plus `dev/asset_team/reviews/<id>_review.png` (both sizes at 4x on checker and dark backgrounds, and at 32 px to prove the silhouette reads).

## 5. Quality gates (check these yourself before you report)

- Item icons: keep a margin. No object pixel within 3 px of the frame edge, and the drop shadow must be clearly visible. Keep your raw generation until the orchestrator approves (a send-back may need it).
- Item icons: the silhouette-edge check counts **8-neighbour** contact (diagonals too). Every opaque pixel touching transparency in any of the 8 directions must be the outline colour `#2B1A2E` (the shadow is exempt), and the outline is 1 px thicker underneath.

- Zoom in on every word on every image. AI text is unreliable: fix misspellings by splicing a corrected local edit. Remove any text the description doesn't give. Unapproved invented signage, names or logos go.
- No real city or place names anywhere in the art. Real brands keep their real names.
- No nudity. No people painted into places.
- Does it match the description, line by line? Count things: windows, signs, props, colours the doc names.
- Does it look like it belongs next to `_contact.jpg`?
- At most **3 generation rounds** per deliverable. If round 3 still misses, stop and report the best attempts and what's wrong.

## 6. Questions: hold, never guess

If the description is missing, unclear or self-contradictory, or the art would need you to invent content (names, signage text, story), **don't invent it**. Send `SendMessage` to `main`:
`QUESTION from <your asset id>: <one sentence>` / `CONTEXT: <doc:line, what conflicts>` / `OPTIONS: A) ... B) ...`
Then stop and end with a final message starting `HOLDING:`. The orchestrator posts it to the author's Eurobound Desk (one desk for every author question, Tools/beads_board/README.md) and a new agent resumes with the answer.

## 7. Finish

1. **Commit** in your worktree branch only the files you made for this asset (no `git add -A`; never commit the main repo's unrelated changes). Message: `art(<city>): <asset name> <kind> (asset team)`, ending with the attribution lines the orchestrator gave you.
2. **Clean up**: delete your temp files and scratch images, **only inside your own named scratch subfolder** (never `rm` loose files or globs at the scratchpad root: other agents and the orchestrator keep files there) (keep only the deliverables and the review sheets), stop your CORS server and any python, node, Aseprite or Blender process you started (`tasklist` to check), and close your browser tabs. Don't kill processes you didn't start. **Stop your CORS server by its PID or by its port** (`Get-NetTCPConnection -LocalPort <your port>`), never by matching `cors_server` in command lines: other agents run the same script on other ports. Then **verify**: `netstat -ano | findstr :<your port>` must show no `LISTENING` line (TIME_WAIT lines are fine). **Write deliverables only inside your own worktree**, never into the main checkout (read refs from main, write to your worktree): a stray copy in main blocks the orchestrator's merge. Two agents reported "stopped" while their server was still listening; the orchestrator checks this.
3. **Report**, under 200 words: the commit hash and branch, the deliverable paths, the review sheet path, the description lines you followed, anything you couldn't match, and confirmation that cleanup is done.
