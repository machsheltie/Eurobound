# Shared material library

One folder per approved material: `library/<material_id>/`. Every asset that uses the same surface (the Arcade's limestone, the bros' Hornets teal, the cabinet brass) points its manifest's `library_ref` at it and does not derive it again.

## Folder contents

| File | What |
|---|---|
| `material.json` | id, label, colours (median / shadow / light hex), finish, pattern, scale m/px, `observed` (direct / inferred), `source` (the asset id, the reference sha256 and the mask the crop came from), `approved` (who, date, the Desk id or qc_log line) |
| `crop.png` | The unaltered reference crop it was taken from (alpha = mask) |
| `study.png` | Optional flat study (protocol step 4). It is a **proposal**: mark `study_status: proposal` until approved; never canonical |
| `basecolor.png` etc. | Only if made and validated; generated PBR maps are not physically validated (protocol rule) |

## Rules

- A material enters the library only after it passes review (QC gate or a Desk approval). Record the evidence in `approved`.
- Never edit a library material in place once an asset uses it; add `<material_id>_v2` and move assets over deliberately.
- `material_id` is snake_case and names the surface, not the asset: `hornets_teal_mesh_jersey`, not `bradley_shirt`.
