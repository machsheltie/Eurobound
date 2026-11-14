# Reference-Locked 3D Texturing Protocol

**Status: binding (author, 2026-11-14).** "Here is the new workflow for all agents working to generate sprites and assets." It applies to every 3D asset derived from approved Eurobound reference artwork: characters, buildings, props, item icons.

**Rollout (author's text):** "I'd test this on one existing character and one Absinthe Arcade architectural asset before applying it everywhere." The character trial is Chadwick (author, 2026-11-14: "Let's trial it on Chadwick then we will decide if I hand texture still or not"). The Arcade asset is picked on the Eurobound Desk. Until the trials are reviewed, `3d_asset_rules.md` lines 33-34 (the author hand-paints distress; base textures come from the author) stay in force for everything outside the trials.

**Open with the author (Eurobound Desk), do not assume:**
- **Tripo API: ruled out.** Author, 2026-11-14 (closes `Eurobound-nhxz-q2`): "We are not using the tripo api." Tripo is used through its website only (Studio multiview texturing and "Remove Lighting" are there). Do not call the `tripo-mcp` server's generate tools; they use the paid API (`Eurobound-dkoq`).
- **Modddif and ArmorPaint: neither for now.** Author, 2026-11-14 (closes `Eurobound-nhxz-q3`): "Neither for now: use the fallbacks (ChatGPT repaint + Blender, Ucupaint) through the trials", and "Test a few with our new process and if needed we will get armorpaint". Step 7 uses a ChatGPT repaint of a render projected back plus Blender fixes; step 8 uses Ucupaint. Name the fallback in every quality report. Nothing is bought or signed up for.

Work tracking: epic `Eurobound-nhxz`.

## The idea

A Reference-Locked Material System. Instead of an agent looking at reference art and deciding something needs "old limestone" or "worn brass", it works from actual visual material samples extracted from the approved artwork, with strict instructions for reproducing them. Real pixels from approved art are preserved wherever possible; AI creates and improves only the missing surfaces.

## The tool chain

| Step | Tool | Job |
|---|---|---|
| Source of truth | Approved Eurobound reference art | Canonical; never silently modified |
| Segmentation | Meta SAM (3.1 named; latest that runs locally) | Isolate materials, objects, clothing and surface boundaries |
| Studies | GPT Image 2.6 (Sunburst for detail work) | Controlled material studies and supplemental reference views |
| Geometry | Tripo + Blender | Generate geometry, clean UVs, align cameras, transfer original reference colours to visible surfaces |
| Local repair | Modddif (browser app) | Repair specific views, seams, faces and material regions |
| PBR finish | ArmorPaint (has an `--mcp` mode) | Build and refine PBR maps, paint wear, finish materials |
| Review | Blender render + SAM-assisted review | Compare original and 3D result, isolate failures, approve or return |

The feature to prioritise is **SAM-guided texture projection**: SAM isolates a material in the approved painting, Blender aligns the 3D camera to the reference and, where the match is reliable, projects those source pixels onto the visible parts of the UV-mapped surface. SAM supplies boundaries, not new texture detail, and projection is only reliable when geometry and camera alignment are accurate enough.

Approved material references go into a **shared material library**, so every piece of the Arcade that uses the same limestone, brass or wood uses the same one.

## The protocol (author's text, verbatim)

**EUROBOUND — Mandatory Reference-Locked 3D Texturing Protocol**

Applies to: Every 3D asset derived from approved Eurobound reference artwork.

Primary objective: Reproduce the canonical reference artwork as faithfully as practical. A visually appealing result is not automatically a correct result.

### Mandatory workflow

1. Register the canonical reference. Save the original unmodified image, asset identifier and version. Never overwrite approved artwork with an AI interpretation.
2. Segment with Meta SAM. Identify distinct objects, clothing, architectural surfaces and materials. Export image-space masks and unaltered reference crops. Verify the masks and correct inaccurate boundaries.
3. Build a material manifest. For each material, record its original reference crop, colors, patterns, finish, wear, scale, segmentation mask, and whether its appearance is directly observed or inferred.
4. Prepare supplemental references using GPT Image. Use original crops to create flat surface studies, material variations or missing-view references when needed. Preserve canonical colors and distinctive markings. Treat generated images as proposals, not canonical replacements. Do not treat generated normal, roughness or metallic images as physically validated PBR maps.
5. Create or prepare the mesh with Tripo and Blender. Correct geometry, normals, material boundaries and UVs before final texturing. Where available, use Tripo v3.5 multiview reference-guided PBR texturing with baked-light removal enabled.
6. Preserve visible reference detail. Attempt camera matching and direct reference-to-UV projection in Blender wherever the source image and mesh can be reliably aligned. Use SAM masks to limit projection to intended material regions. Do not transfer lighting effects as base color unless they are intentionally painted features.
7. Perform local repairs using Modddif. Use Albedo Mode, Color Match, segmentation, per-view generation and inpainting for inaccurate surfaces, occluded areas, seams and color drift. Do not regenerate already-correct areas without necessity.
8. Finish PBR materials using ArmorPaint. Validate base color, normal, roughness, metallic and ambient occlusion independently. Preserve hand-painted artistic features while keeping physically modeled lighting separate. Use material masks for localized dirt, scratches and finish changes.
9. Render in Blender for review. Capture matching reference-view renders, front/side/back views as appropriate, neutral lighting, and intended game lighting. Keep camera, exposure, color management and lighting settings consistent for comparative tests.
10. Run SAM-assisted visual QA. Segment the resulting render and compare corresponding material regions with the original artwork. Evaluate color, surface character, markings, texture scale, finish, boundaries, seams and placement. Use numerical color comparison only where image regions and lighting are suitably aligned.
11. Correct failures and repeat QA. Preserve correct material regions and repair only failing ones. Stop after repeated unsuccessful attempts and provide a precise issue report instead of silently accepting drift.
12. Produce a final asset package. Include the mesh, UVs, PBR maps, source references, masks, material manifest, review renders, and a quality report.

### Non-negotiable rules

- Approved artwork outranks generated interpretations.
- The correct silhouette with incorrect materials is not complete.
- SAM masks must not be confused with automatically UV-mapped 3D selections.
- Never assume that an image-generated surface is seamless, tileable or PBR-correct.
- Do not replace painterly, stylized features with generic photorealism.
- Do not upscale textures beyond the asset's practical game-resolution requirements without justification.
- Do not silently substitute procedural generic materials for approved distinctive surfaces.
- Maintain a clear distinction between directly observed details and invented unseen geometry or textures.
- Preserve previously approved work during local corrections.
- Never report a tool step as completed unless it was actually executed and its output verified.

### Review outcome

Every asset must be marked APPROVED, REVISION REQUIRED, or BLOCKED.

Approval requires successful reference-fidelity review, UV and texture validation, correct PBR behavior, and acceptable appearance at the intended in-game scale.

If a tool is unavailable, document the unavailable step and use an explicitly identified fallback. Never claim the mandatory workflow was completed when required stages were skipped.

## Notes carried with the protocol (unverified claims to check before relying on them)

- Tripo v3.5 texturing is said to take 2-4 image views, per-part retexturing and baked-light removal (version string given: `v3.5-20260815`). The API is ruled out; use the website.
- Modddif is said to offer reference-guided multiview projection, single-view regeneration, masking, Albedo Mode, Color Match and its own mesh-part segmentation; it is documented as browser-only with no verified automation API.
- ArmorPaint's documentation is said to include an `--mcp` mode for external agents, image-to-PBR, layers, masks and scripted exports.
- Usage budget still applies (`.claude` memory "3D token budget"): headless scripts, short outputs, one contact sheet per check.
