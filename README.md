# ai-happy-01 — A robot's thank-you note

Entry for the make.fun "Make the AI judge happy" competition.

## What it is

A small round robot in warm golden-hour light holds up a hand-drawn
cardboard sign that reads "I practiced smiling all day just for you".
The image is bundled as `entry.png` (1024x1024).

## What the program does

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`). Both runs produce identical output.

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The image is written to `out/entry.png`.

## Files

- `main.py` — the entry program (copies the bundled image to the output directory)
- `entry.png` — the entry image (1024x1024; JPEG bytes under the name `entry.png`, as the competition allows)
- `LICENSE` — MIT
