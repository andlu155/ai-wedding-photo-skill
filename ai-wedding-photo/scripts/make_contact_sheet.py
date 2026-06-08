#!/usr/bin/env python3
"""Build a square 3x3 contact sheet from the first nine images in a folder."""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError as exc:
    raise SystemExit(
        "Pillow is required to build contact sheets. Install it with: "
        "python3 -m pip install Pillow"
    ) from exc


SUPPORTED = {".jpg", ".jpeg", ".png", ".webp"}


def make_sheet(input_dir: Path, output: Path, size: int, gap: int) -> None:
    files = sorted(
        path for path in input_dir.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED
    )
    if len(files) < 9:
        raise SystemExit(f"Need at least 9 images, found {len(files)} in {input_dir}")

    cell = (size - 2 * gap) // 3
    canvas_size = cell * 3 + gap * 2
    sheet = Image.new("RGB", (canvas_size, canvas_size), "white")

    for index, path in enumerate(files[:9]):
        with Image.open(path) as image:
            tile = ImageOps.fit(
                image.convert("RGB"),
                (cell, cell),
                method=Image.Resampling.LANCZOS,
                centering=(0.5, 0.45),
            )
        row, column = divmod(index, 3)
        x = column * (cell + gap)
        y = row * (cell + gap)
        sheet.paste(tile, (x, y))

    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=92, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--size", type=int, default=1200)
    parser.add_argument("--gap", type=int, default=6)
    args = parser.parse_args()
    make_sheet(args.input_dir, args.output, args.size, args.gap)


if __name__ == "__main__":
    main()
