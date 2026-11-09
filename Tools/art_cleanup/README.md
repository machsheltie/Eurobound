# art_cleanup

Cleans AI-generated sprites and props (Firefly / GPT image) before they go into Godot.

## Setup (once)

```
python -m venv tools/art_cleanup/.venv
tools/art_cleanup/.venv/Scripts/python -m pip install -r tools/art_cleanup/requirements.txt
```

The first AI cutout downloads a ~180 MB model to `~/.u2net/`.

## Typical use

```
PY=tools/art_cleanup/.venv/Scripts/python
# background off, halo cleaned, trimmed onto a fixed canvas with feet on the bottom edge
$PY tools/art_cleanup/art_cleanup.py pipeline "incoming/*.png" --out cleaned --canvas 512x768
# review on checker / dark / light / magenta before shipping
$PY tools/art_cleanup/art_cleanup.py sheet "cleaned/*.png" --out review/sheet.png
# lock a batch to one palette
$PY tools/art_cleanup/art_cleanup.py palette extract "approved/*.png" --colors 32 --out palettes/bros.png
$PY tools/art_cleanup/art_cleanup.py palette apply "cleaned/*.png" --palette palettes/bros.png --strength 0.6
```

## Choosing a cutout mode

- **AI (default, `isnet-general-use`)**: works on any background. Use `--model isnet-anime` for
  cel-shaded/anime-leaning art and `--matting` for hair and soft edges.
- **Chroma key (`--key`)**: exact and instant, but only when the generation prompt asked for a
  flat **#00FF00 green or #FF00FF magenta** background. On white or light backgrounds it eats
  white details (caps, shoes, eyes). The magenta column of `sheet` exposes this immediately.

Always read the `sheet` output before an asset ships: halos show on the dark column, holes on
the magenta one. Words baked into generated art get a spelling check by eye (GEGRETS -> REGRETS).
