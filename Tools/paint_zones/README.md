# tools/paint_zones: SAM paint zones and the material manifest

Shared by the Sprite Development Team (characters) and the Asset Development Team (buildings, props, icons). It implements steps 1-3 of the binding `design/style_guides/reference_locked_texturing_protocol.md` and the SAM part of steps 6 and 10. Beads: epic Eurobound-nhxz (nhxz.1 SAM zones, nhxz.6 manifest and library).

**SAM version:** SAM 2.1 `hiera_base_plus` (Apache-2.0), running locally on the RTX 5060 (8 GB) in this folder's venv. SAM 3/3.1 was not used: its download is gated, and the only thing it adds is video tracking (tool check `docs/research/2026-11-14-texturing-protocol-tool-check.md`).

## Setup (once per machine; the venv and weights are gitignored)

```
py -3.12 -m venv tools/paint_zones/.venv
tools/paint_zones/.venv/Scripts/python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128
tools/paint_zones/.venv/Scripts/python -m pip install "git+https://github.com/facebookresearch/sam2.git" opencv-python-headless pillow numpy
curl -L -o tools/paint_zones/checkpoints/sam2.1_hiera_base_plus.pt https://dl.fbaipublicfiles.com/segment_anything_2/092824/sam2.1_hiera_base_plus.pt
```

The RTX 5060 (Blackwell, sm_120) needs the cu128 torch wheels; older CUDA builds will not see the card.

## Files

| File | What it does | Run |
|---|---|---|
| `refs/registry.json` | Step 1: canonical references with sha256, version and role (`canonical` / `derived`). `segment_ref.py` refuses to run if the image's hash no longer matches. | Edit by script; never point it at an AI reinterpretation |
| `segment_ref.py` | Step 2: segments any image (a canonical reference **or a render**, for the step-10 QA) into named zones from point and box prompts. Writes `work/<id>/masks/<zone>.png`, unaltered `crops/<zone>.png` (alpha = mask), and `segment.json` (SAM score, area, bbox, median / shadow / light colour). `--sheet` writes an overlay sheet of at most 1024 px. | `tools/paint_zones/.venv/Scripts/python tools/paint_zones/segment_ref.py tools/paint_zones/zones/<id>_ref.json --sheet` |
| `zones/<id>_ref.json` | The prompts per asset: `pos`/`neg` points, `box` (always give a box; a single point on a small part grabs the whole figure), `minus` (subtract earlier zones), and the strap and chain tools `keep_hsv`, `close_px`, `open_px`, `cut_boxes` (hand correction) and `largest_cc`. See the docstring. | `zones/chadwick_ref.json` is the worked example |
| `manifest_schema.md` | Step 3: the material manifest format, one JSON per asset in `manifests/` | — |
| `library/` | The shared material library; see `library/README.md` | — |

## Lessons (Chadwick, 2026-11-14)

1. Always give a box. Points alone on a goatee, collar or hand returned the whole figure (scores 0.3-0.7); points plus a box returned clean parts (0.81-0.98).
2. A strap loop over clothing: SAM includes what's inside the loop. Use `keep_hsv` on the strap's colour (the navy strap had saturation 0.54 against the denim's 0.10), then `close_px` to fill the prints, `open_px` to cut seams, and `largest_cc`.
3. A mask is image space, not a UV selection (protocol rule). Getting it onto the mesh is a separate step: camera-matched projection (`tools/char3d/project_ref.py`), clipped by the mask.
4. Masks need verifying: a blind reviewer checks the overlay sheet before the manifest is used (protocol step 2).
