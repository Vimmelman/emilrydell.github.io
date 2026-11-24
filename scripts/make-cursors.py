"""Generates the pixelated cursors in public/. Run: python3 scripts/make-cursors.py"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "public"
SCALE = 3  # each grid cell becomes a 3x3 block

# Classic arrow, hotspot at the tip (top-left).
arrow = [
    "O............",
    "OO...........",
    "OWO..........",
    "OWWO.........",
    "OWWWO........",
    "OWWWWO.......",
    "OWWWWWO......",
    "OWWWWWWO.....",
    "OWWWWWWWO....",
    "OWWWWWWWWO...",
    "OWWWWWWWWWO..",
    "OWWWWWWWWWWO.",
    "OWWWWWWOOOOOO",
    "OWWWOWWO.....",
    "OWWO.OWWO....",
    "OWO..OWWO....",
    "OO....OWWO...",
    "O.....OWWO...",
    ".......OWWO..",
    ".......OWWO..",
    "........OO...",
]
# Pointing hand for links, hotspot at the fingertip.
hand = [
    ".....OO..........",
    "....OWWO.........",
    "....OWWO.........",
    "....OWWO.........",
    "....OWWO.........",
    "....OWWOOO.......",
    "....OWWOWWOOO....",
    "....OWWOWWOWWOO..",
    ".OO.OWWOWWOWWOWO.",
    "OWWOOWWWWWWWWOWWO",
    "OWWWOWWWWWWWWWWWO",
    ".OWWWWWWWWWWWWWWO",
    "..OWWWWWWWWWWWWWO",
    "..OWWWWWWWWWWWWWO",
    "...OWWWWWWWWWWWO.",
    "...OWWWWWWWWWWWO.",
    "....OWWWWWWWWWO..",
    "....OWWWWWWWWWO..",
    "....OOOOOOOOOOO..",
]
COLORS = {"O": "#000000", "W": "#ffffff"}


def svg(grid):
    w, h = len(grid[0]), len(grid)
    rects = "".join(
        f'<rect x="{x}" y="{y}" width="1" height="1" fill="{COLORS[c]}"/>'
        for y, row in enumerate(grid)
        for x, c in enumerate(row)
        if c in COLORS
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w * SCALE}" height="{h * SCALE}" '
        f'viewBox="0 0 {w} {h}" shape-rendering="crispEdges">{rects}</svg>\n'
    )


for name, grid in {"cursor.svg": arrow, "cursor-pointer.svg": hand}.items():
    assert all(len(r) == len(grid[0]) for r in grid), name
    (OUT / name).write_text(svg(grid))
    print("wrote", name, len(grid[0]) * SCALE, "x", len(grid) * SCALE)
