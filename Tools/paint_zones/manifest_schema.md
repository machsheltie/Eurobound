# Material manifest (protocol steps 1-3)

Binding workflow: `design/style_guides/reference_locked_texturing_protocol.md`. One manifest per asset: `tools/paint_zones/manifests/<asset_id>.json`. Characters and Arcade assets use the same format.

## File layout

```
tools/paint_zones/
  refs/registry.json                 step 1: canonical refs, sha256, version (never edited images)
  manifests/<asset_id>.json          step 3: this format
  work/<asset_id>/masks/<zone>.png   step 2: SAM masks, image space of the canonical ref (white = in)
  work/<asset_id>/crops/<zone>.png   step 2: unaltered crops of the canonical ref (bbox of the mask, alpha = mask)
  library/<material_id>/             shared materials (see library/README.md)
```

## Manifest JSON

```json
{
  "asset_id": "chadwick",
  "reference": {"path": "...", "sha256": "...", "version": "portrait_v3"},
  "sam": {"model": "sam2.1_hiera_base_plus", "mode": "points|auto", "verified_by": "blind reviewer id or 'pending'"},
  "materials": [
    {
      "zone": "polo",                       // unique per asset; also the mask/crop file name
      "label": "red polo shirt, body and sleeves",
      "library_ref": null,                  // or "<material_id>" when it reuses a library material
      "mask": "work/chadwick/masks/polo.png",
      "crop": "work/chadwick/crops/polo.png",
      "colors": {"median": "#DC5B4F", "shadow": "#9A3A33", "light": "#F08A7A"},   // sampled from the crop, not invented
      "pattern": "none | stripes 2 cm | ...",
      "finish": "matte cotton pique",
      "wear": "none visible | ...",
      "scale_m_per_px": 0.0012,             // from the ref's figure height / height_m
      "markings": [{"text": "...", "where": "..."}],   // exact letters, if any
      "observed": "direct",                 // direct | inferred
      "inferred_from": null,                // when inferred: what it was reasoned from (e.g. "front view only; back assumed same colour")
      "projection": "camera_match | zone_fill | none",   // how step 6 applies it
      "notes": ""
    }
  ],
  "unseen": ["back of polo", "soles"],      // surfaces the reference does not show; textures there are inferred
  "fallbacks": [{"step": 7, "tool": "Modddif", "used": "ChatGPT repaint + Blender texture paint", "why": "nhxz-q3 open"}]
}
```

## Rules

- `colors` come from the crop's own pixels (median plus the 10th and 90th luminance percentiles), never from a name like "brick red".
- `observed: "inferred"` always carries `inferred_from`. The quality report lists every inferred zone.
- A mask is not a UV selection. UV zones come from step 6 (camera-matched projection, clipped by these masks).
- Lighting painted into the reference (cast shadows, rim light) is noted in `notes`; it is not copied as base colour unless the artist painted it as a feature.
