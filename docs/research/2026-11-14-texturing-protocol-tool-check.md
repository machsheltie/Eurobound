# Texturing protocol tool check

Date: 2026-11-14. Bead: Eurobound-nhxz.5. Protocol checked: `design/style_guides/reference_locked_texturing_protocol.md`.

**Nothing was installed, bought, signed up for, downloaded or reconfigured.** No Tripo credits were spent. This report says which of the protocol's tools we can really use, what each costs, and what to use instead when one is out of reach.

Machine checked: Windows 11, RTX 5060 Laptop GPU (8 GB video memory, about 1.8 GB already in use by other programs when I looked), Blender 5.2.

## The short version

| Tool | Real? | Can we use it today? | Cost | Fallback |
|---|---|---|---|---|
| Meta SAM | Yes. SAM 3.1 exists. | SAM 2.1: yes after a free download. SAM 3.x: only after you accept Meta's access form. | Free | SAM 2.1 base-plus, then SAM 2.1 small, then hand-drawn masks |
| GPT Image 2.6 (Sunburst) | Yes | Yes, through Firefly's home screen or ChatGPT | Covered by your existing subscriptions | GPT Image 2.5 Sunburst in Firefly |
| Tripo multiview texturing with light removal | Yes | **Yes, on the website.** I saw the controls. | 30 credits per texture at 8K (you have 18,715) | Blender projection from the reference (protocol step 6) |
| Modddif | Yes | Not yet. It needs an account, and **the free plan makes our art public.** | Free, or $30 a month for private work | Tripo's Magic Brush on the website, or Blender texture paint |
| ArmorPaint | Yes, and `--mcp` is real | Not installed | $19 once, or free if built from source | Blender with Ucupaint (already installed) |

**The protocol's claims held up better than expected.** I found no invented tool and no invented version number. The things I could not confirm are listed at the end.

**Three things need your decision** (filed as beads, see the end):
1. Modddif's free plan publishes everything under a Creative Commons licence and may train their AI on it. For unreleased game art that is a real problem.
2. ArmorPaint: pay $19, or install Microsoft's compiler (several GB) to build it for free.
3. The `tripo-mcp` connection on this machine calls the paid Tripo API, which you banned.

---

## 1. Meta SAM (Segment Anything)

**What it is.** A free AI model from Meta that traces the outline of things in a picture. We use it to cut a reference painting into material zones (shirt, hair, brass, limestone).

**Does "SAM 3.1" exist?** Yes. Meta released SAM 3 in November 2025 and SAM 3.1 on 27 March 2026. SAM 3.1's only addition is faster tracking of many objects at once **in video**. For still images it brings nothing over SAM 3. Source: [SAM 3 repository](https://github.com/facebookresearch/sam3), [SAM 3.1 model page](https://huggingface.co/facebook/sam3.1).

**What SAM 3 adds over SAM 2.1.** You can ask for things in words ("the red polo shirt") instead of clicking points on them. That is the one feature that would matter to us.

**What SAM 3.x needs.**
- Python 3.12 or newer, PyTorch 2.7 or newer, an NVIDIA card with CUDA 12.6 or newer. The paint-zones tool's environment already has Python 3.12.10 and PyTorch 2.11 with CUDA 12.8 working on the RTX 5060. I ran that check.
- The model is large: 848 million parameters, against 81 million for SAM 2.1 base-plus. That is about ten times bigger.
- **Meta publishes no video-memory requirement.** Third-party write-ups disagree: some measured 4 to 6 GB for one image, others say 12 GB minimum. On an 8 GB laptop card that is also running Blender, it is a tight fit at best. Unconfirmed.
- **The download is gated.** You must log in to Hugging Face and agree to share your contact details with Meta before the files unlock. That is a sign-up step, so I did not do it.

**SAM 2.1 in 8 GB.** Comfortable. Sizes from Meta's own list: tiny 38.9M, small 46M, base-plus 80.8M, large 224.4M parameters. Base-plus and small will both run with plenty of room. The downloads are direct links with no login. Source: [SAM 2 repository](https://github.com/facebookresearch/sam2).

**Licence for the weights.**
- SAM 2.1: Apache 2.0. Free for commercial use, no strings beyond keeping the notice.
- SAM 3 and 3.1: Meta's own "SAM License" (last updated 19 November 2025). It allows use, copying and changes, royalty-free, and does not forbid commercial use. It bans military, weapons, nuclear and espionage uses, and anyone you pass the model to must get a copy of the licence. Nothing in it restricts what you do with the masks it produces. Source: [SAM License](https://github.com/facebookresearch/sam3/blob/main/LICENSE).

**Is 3.x worth switching to?** **No, not now.** Stay with SAM 2.1 base-plus as the Sprite Development Team planned.
- SAM 3.1 specifically gives us nothing (video only).
- SAM 3's word prompts are attractive, but it is ten times bigger, has no confirmed fit in 8 GB, and needs your Hugging Face sign-off.
- Clicking points works fine for a painted reference where an agent can see the zones.
- Worth a small trial later, once the Chadwick test shows whether point-clicking is the slow part.

**How an agent drives it.** A Python script run from the command line: `tools/paint_zones/segment_ref.py`, already written for SAM 2.1.

**One Windows catch.** Meta's SAM 2 instructions "strongly recommend" running it under WSL (Linux inside Windows). WSL is not installed here. SAM 2 normally installs on plain Windows anyway, with one optional speed-up skipped, which Meta says is safe to ignore. That is read, not tested.

**What I verified myself.** The GPU, Python and PyTorch versions in `tools/paint_zones/.venv`; that the `sam2` package and the model files are **not** on this machine yet. **What I only read.** Everything about SAM 3's needs and both licences.

**Fallback.** SAM 2.1 base-plus, then SAM 2.1 small, then masks drawn by hand as polygons.

---

## 2. GPT Image 2.6, including Sunburst

**What it is.** OpenAI's image generator. "Images 2.6" came out on 4 November 2026. It comes in two flavours: Flare (fast) and Sunburst (higher quality, better at keeping an image consistent across edits). Sources: [OpenAI announcement](https://openai.com/index/introducing-images-2-6/), [runtimewire coverage](https://runtimewire.com/article/openai-chatgpt-images-2-6-gifs-flare-sunburst-api).

**Reachable?** Yes, by both allowed routes.
- **Adobe Firefly.** Our own note (`bd memories firefly`, your observation of 2026-11-12) says GPT Image 2.6 Sunburst is offered when you start from Firefly's **main screen**. The `/generate/image` page only lists up to 2.5 Sunburst. I did not re-open Firefly to check.
- **ChatGPT.** Press reports say Images 2.6 is in ChatGPT for every tier, free included. You have a standing OK for ChatGPT image generation.

**Cost and licence.** No new cost: both routes ride on subscriptions you already have. I did not look up Firefly's credit price per image. No paid API is involved or needed.

**How an agent drives it.** The Chrome browser tools, as we do now for Firefly. One known limit, from the same note: Firefly's "upload a reference image" button cannot be reached by the browser tools. The protocol's step 4 wants original crops fed in as references, so **for reference-guided studies ChatGPT is the working route**, or the crop has to be described in words in Firefly.

**What I verified myself.** That our notes and `Tools/item3d/README.md` agree on the Firefly home-screen route (the README still says 2.5 Sunburst). **What I only read.** The 2.6 release details. I found **no public announcement** that Adobe has added 2.6 to Firefly; the public articles only cover 2.5. Your own sighting is the evidence for 2.6.

**Fallback.** GPT Image 2.5 Sunburst in Firefly, which is the model we already use.

---

## 3. Tripo v3.5 multiview PBR texturing with baked-light removal

**What it is.** Tripo paints a texture onto a 3D model using two to four pictures of it (front, left, right, back), and can strip out the lighting painted into those pictures so the game's own lights work properly.

**Is it on the WEBSITE? Yes.** I opened Tripo Studio in Chrome, in your logged-in session, loaded an existing model into the Texture tool and looked. I did not press Generate. I saw:
- A **multiview input** tab with four slots: Front, Left, Right, Back.
- A **"Remove Lighting"** switch, tagged "New". It is off by default.
- **Texture Resolution**: 2K, 4K, 8K.
- The **Generate Texture** button showing **30 credits** with 8K selected. Your balance read 18,715.

So the protocol's step 5 can be done on the website with no API.

**Does the version number check out?** Yes. Tripo's developer documentation lists texture model `v3.5-20260815` as the newest, says it is the only one that reads the light-removal setting, takes 2 to 4 views with the front required, and can texture named parts only. Source: [Tripo texture documentation](https://developers.tripo3d.com/en/docs/models-texture). The website does not print a version number, so I cannot prove the website uses v3.5. Since light removal only exists in v3.5, it very likely does.

**Cost and licence.** From Tripo's pricing page, read today: Free $0 (200 credits a month, non-commercial, public models); Pro $20 a month (3,000 credits, commercial use, private models); Max $90 a month (25,000 credits, unlimited 8K). Extra credits: $10 per 1,000. Part-based texture editing and the Magic Brush are listed as plan features. Source: [Tripo pricing](https://www.tripo3d.ai/pricing). I did not check which plan you are on. Tripo states that the website and the API are separate products with separate billing.

**How an agent drives it.** Chrome browser tools, clicking through the Studio page. The page text cannot be read by the tools on that site, so the agent works from screenshots. That is slower and costs more usage than a script, which matters for the 3D token budget.

### The `tripo-mcp` connection: it calls the paid API

Plainly: **yes, it does, and it should not be used.**

- It is not in the project's `.mcp.json`. It is set up in your personal Claude settings for this project and starts with `uvx --with "mcp<2" tripo-mcp` (version 0.1.2).
- I read its source code without running it. Two of its tools, `create_3d_model_from_text` and `get_task_status`, send requests to `openapi.tripo3d.ai`, which is the paid Tripo API. They get the API key from the Tripo add-on inside Blender.
- No key is saved in the Blender add-on folder right now, so today those two tools would simply fail. If a key were ever typed into the add-on, they would start spending money.
- Its other tools only talk to Blender on this machine or download free Poly Haven assets. They do not touch the Tripo API.
- **It has no texturing tool at all.** It cannot do the v3.5 texturing even if the API were allowed.

**What I verified myself.** The website controls and the credit price on the button (screenshots); the pricing page; the `tripo-mcp` source. **What I only read.** The developer documentation. **Not checked.** The credit price at 2K and 4K; whether the website has a PBR on/off switch (I did not see one); per-part retexturing on the website (listed on the pricing page, not opened).

**Fallback.** Blender camera-matched projection from the reference (protocol step 6) plus zone fills with `Tools/char3d/recolor_region.py`.

---

## 4. Modddif

**What it is.** A website for AI texturing of 3D models, made by one developer (Guillaume, in Lyon, France). It runs its own AI servers. Source: [Modddif about page](https://docs.modddif.com/about/).

**Do the named features exist?** Yes, all of them. From its documentation:
- **Albedo Mode**: generates images "with fewer shadows, highlights, and reflections".
- **Color match**: makes new texture match the colours already on the model.
- **Multiview generation** from preset camera angles, and **single view generation** from the current camera.
- **Inpainting** of a selected region, with a patch tool.
- **Segmentation** of the 3D model into parts, automatic or painted by hand.
- Reference images, layers, 2K textures (4K on Pro).

Source: [Modddif texture docs](https://docs.modddif.com/project/texture/), [segmentation docs](https://docs.modddif.com/project/segmentation/).

**Cost.** No credits; everything is unlimited. Source: [Modddif pricing](https://modddif.com/pricing/).
- **Free, $0.** 2K textures, 150,000-face limit on imported models.
- **Pro, $30 a month (€25).** 4K textures, 1.5 million faces, private projects, FBX export.

**The catch, and it is a big one.** On the Free plan, in Modddif's own words:
- "All work shared under a Creative Commons license"
- "Projects shared in the Modddif public gallery"
- "Projects may be used to improve Modddif AI models"

Uploading Chadwick or the Arcade on the Free plan would publish unreleased Eurobound art and let others reuse it. Only Pro keeps work private and out of AI training.

**Login.** Required. I opened the app and got a login screen: Google, or email and password. There is no account in this browser. I did not create one.

**API.** None. The docs say "Modddif is a web app only". No command line, no plug-in, no MCP.

**Could the Chrome tools drive it?** Probably, slowly. It is a 3D painting app drawn on a canvas, so the tools would work from screenshots and mouse drags, with keyboard shortcuts (K for the inpaint selection, I for the patch tool). Uploading a model through a file picker may hit the same wall as Firefly's upload button. None of this could be tested without an account.

**What I verified myself.** The login wall (screenshot); the pricing page. **What I only read.** The feature docs. **Not found.** Their terms of service page would not load as text.

**Fallback.** Tripo's Magic Brush and part-based texture edit on the website; or Blender texture paint, with a GPT Image patch projected onto the bad area.

---

## 5. ArmorPaint

**What it is.** A desktop program for painting textures straight onto 3D models, like a small Substance Painter. Version 1.0; the download page shows "Latest Update: November 13, 2026".

**Price.** **$19, one payment**, all updates included, with a "no questions asked refund policy". Source: [ArmorPaint download](https://armorpaint.org/download).

**Building it from source instead.** Allowed and free. The licence is zlib, which permits any use including commercial. The project says: "Distributed binaries are paid to help with the project funding." Source: [licence](https://git.armorpaint.org/blob/license.md), [source repository](https://github.com/armory3d/armortools).
- Building on Windows needs Git and Visual Studio with its clang tools, then four short commands.
- **Git is on this machine. Visual Studio is not** (I looked for it and for its compilers). Installing it is several GB and counts as an install, so it needs your OK.
- Honest comparison: $19 saves an install, a build that may fail, and an agent's time fixing it.

**Windows support.** Yes. Windows, Linux and macOS, portable with no installer. Its built-in AI features recommend 6 GB of video memory; we have 8.

**Does `--mcp` really exist?** **Yes.** The current manual lists it: "`--mcp`: Serve the open instance to agents over the model context protocol (stdio)", with the note "The project needs to be saved first." Source: [ArmorPaint manual](https://armorpaint.org/manual). I did not run it, because ArmorPaint is not installed.

**Scripting and export automation.** Yes, also in the manual:
- `--background` runs it with no window.
- `--export-textures <type> <preset> <path>` exports PNG, JPG or EXR.
- `--export-mesh` and `--export-material`.
- `--script <path>` runs a script on the open project.
- `--api` prints the scripting reference.
- Scripts and plug-ins are written in a small C-like language.
- "To Material" turns a photo into base colour, height, normal, occlusion and roughness maps.

A separate community project, [armorpaint-mcp](https://github.com/baktubak/armorpaint-mcp) (MIT licence), offers 58 agent tools through a plug-in. With the built-in `--mcp` we should not need it.

**How an agent drives it.** Command line for batch exports and scripts; `--mcp` for step-by-step painting.

**What I verified myself.** That ArmorPaint and Visual Studio are not on this machine. **What I only read.** Everything else, from the official manual and download page. The manual is the primary source, but **nobody here has seen `--mcp` work**.

**Fallback.** Blender with **Ucupaint**, a layer-painting add-on that is **already installed** in Blender 5.2 on this machine, plus Blender's own baking.

---

## Claims I could NOT confirm

- **SAM 3 or 3.1 running in 8 GB.** Meta gives no figure. Third-party numbers range from 4 GB to 12 GB.
- **GPT Image 2.6 inside Firefly, from any public source.** Only your own sighting supports it. Public articles cover 2.5 in Firefly.
- **That the Tripo website uses texture model v3.5.** The site shows no version. The "Remove Lighting" switch points to it.
- **A PBR switch on the Tripo website.** Not seen in the Texture panel.
- **That the Chrome tools can operate Modddif.** Untestable without an account.
- **That ArmorPaint's `--mcp` works in practice.** Documented, never run here.
- **Firefly's credit cost per GPT Image 2.6 picture.** Not looked up.

## Claims that were wrong or need a caveat

- **"SAM 3.1" as the segmentation tool.** It exists, but its new part is video tracking. It is the wrong reason to pick it, and it is gated behind a Meta access form.
- **Modddif as a free browser tool.** Free, yes, but free means public, Creative Commons, and usable for their AI training.
- **`tripo-mcp` as a way to reach Tripo.** It reaches the banned paid API and has no texturing tool.
- **Small mismatch on Tripo's own site.** A Tripo guide says the Free plan has 300 credits and Pro costs $19.90; the live pricing page says 200 credits and $20.

## Follow-up beads

- `Eurobound-nhxz.5` stays open and points here.
- `Eurobound-hbqg`: Modddif free plan makes work public; skip it or pay for Pro? (author ruling)
- `Eurobound-kj21`: ArmorPaint: buy for $19, build from source, or use Blender + Ucupaint? (author ruling)
- `Eurobound-dkoq`: remove the `tripo-mcp` connection that can call the banned API? (author ruling)
