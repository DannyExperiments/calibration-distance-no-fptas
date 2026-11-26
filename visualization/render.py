#!/usr/bin/env python3
"""Render the two exact anchor-load examples as rotating three-dimensional stacks."""
from functools import lru_cache
from math import cos, pi, sin
from os import environ
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SIZE = (648, 453)
BG, CARD = "#0b1627", "#13283f"
WHITE, MUTED = "#eff7fc", "#bfd1e1"
GREEN, ORANGE, BLUE, GOLD = "#65e1ba", "#ffad7c", "#88c4ff", "#f9d77b"
PALETTES = (
    ("#22725f", "#164c50", "#3ba68a"),
    ("#327398", "#225376", "#56a0c9"),
)
CASES = (
    ("4, 4, 5, 5, 6, 6", ((4, 5, 6), (4, 5, 6)), "0", "Both loads equal 15."),
    ("4, 4, 4, 6, 6, 6", ((4, 6, 6), (4, 4, 6)), "4800/3607", "Even weights cannot make a load of 15."),
)


@lru_cache
def font(size, bold=False):
    key = "Q460_BOLD_FONT" if bold else "Q460_FONT"
    name = "Arial Bold.ttf" if bold else "Arial.ttf"
    local = Path("/System/Library/Fonts/Supplemental") / name
    return ImageFont.truetype(environ.get(key, str(local)), size)


def text(draw, point, value, size, color=WHITE, bold=False, anchor=None):
    draw.text(point, value, fill=color, font=font(size, bold), anchor=anchor)


def stack(draw, x, angle, weights, j):
    def project(a, b, z):
        across = a*cos(angle)-b*sin(angle)
        depth = a*sin(angle)+b*cos(angle)
        return x+across, 300-8.6*z-0.39*depth

    def prism(lower, higher, color, width=94, depth=57):
        u, v = width/2, depth/2
        for side, fill in zip((
            ((-u,-v,lower),(u,-v,lower),(u,-v,higher),(-u,-v,higher)),
            ((-u,-v,lower),(-u,v,lower),(-u,v,higher),(-u,-v,higher)),
            ((-u,-v,higher),(u,-v,higher),(u,v,higher),(-u,v,higher)),
        ), color):
            vertices = [project(*xyz) for xyz in side]
            draw.polygon(vertices, fill=fill)
            draw.line(vertices + vertices[:1], fill=BG, width=2)

    prism(-2, 0, ("#39485a", "#2b3748", "#526478"), 107, 67)
    load = 0
    for weight in weights:
        prism(load, load+weight, PALETTES[j])
        px, py = project(0, -28.5, load+weight/2)
        text(draw, (px, py), str(weight), 20, WHITE, True, "mm")
        load += weight

    a = project(-79, 0, 15)
    b = project(79, 0, 15)
    for k in range(8):
        t, s = k/8, (k+.43)/8
        draw.line([tuple(l+(r-l)*p for l,r in zip(a,b)) for p in (t,s)], fill=GOLD, width=2)
    text(draw, (b[0]+9, b[1]-10), "15", 17, GOLD, True)


def frame(case, angle):
    weights, splits, excess, note = case
    canvas = Image.new("RGB", SIZE, BG)
    draw = ImageDraw.Draw(canvas)
    text(draw, (20, 13), "Why exact anchor loads matter", 32, bold=True)
    text(draw, (20, 58), f"Ordinary weights: {weights}", 23, MUTED)
    for j, (left, items) in enumerate(zip((14, 329), splits)):
        x = left+151
        draw.rounded_rectangle((left, 97, left+305, 366), 15, fill=CARD)
        text(draw, (x, 112), f"Anchor {j+1} · forecast {('7/24', '1/3')[j]}", 21, bold=True, anchor="mt")
        stack(draw, x, angle, items, j)
        load = sum(items)
        text(draw, (x, 352), f"Ordinary load {load}", 23, GREEN if load==15 else ORANGE,
             True, "mm")
    text(draw, (20, 378), f"Minimum excess loss: {excess}", 24, GOLD, True)
    text(draw, (20, 415), note, 21, MUTED)
    return canvas


if __name__ == "__main__":
    frames = [frame(case, .64+.35*sin(2*pi*i/20)) for case in CASES for i in range(20)]
    samples = Image.new("RGB", (2*SIZE[0], SIZE[1]))
    samples.paste(frames[0], (0,0))
    samples.paste(frames[20], (SIZE[0],0))
    palette = samples.quantize(colors=96)
    frames = [img.quantize(palette=palette, dither=Image.Dither.NONE) for img in frames]
    output = Path(__file__).with_name("anchor-load-gap.gif")
    frames[0].save(output, save_all=True, append_images=frames[1:], duration=140,
                   loop=0, optimize=True)
