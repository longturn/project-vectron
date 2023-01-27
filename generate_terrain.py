import xml.etree.ElementTree as ET
import itertools as it
import math
import os
import shutil

groups = [
    'plains',
    'grassland',
    'swamp',
    'tundra',
    'water',
    'mountains',
    'ice',
    'desert',
]

generator_file = os.path.join('vectron', 'terrain', 'borders', 'generator.svg')
folder = os.path.join('terrain_grids')
shutil.rmtree(folder, ignore_errors=True)
os.makedirs(folder, exist_ok=True)

columns = 6
rows = 9
cells = rows * columns

debug = False  # Set to true to display which sprites are used

cell_width = 180
cell_height = 60

total_width = columns * (cell_width + 1) + 1
total_height = rows * (cell_height + 1) + 1

grid_style = 'fill: #0f0'

preamble = f'''
; ***** THIS FILE WAS GENERATED *****
; Script: generate_terrain.py
; Changes will be overwritten!
; ***********************************

[spec]

; Client capabilities supported by this file
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]
artists = "
    louis94 (spec files)
    TriClad (visuals)
"

[file]
gfx = "vectron/terrain/borders_v2/{{}}"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = {cell_width}
dy = {cell_height}
pixel_border = 1
'''

makefile_preamble = r'''
# ***** THIS FILE WAS GENERATED *****
# Script: generate_terrain.py
# Changes will be overwritten!
# ***********************************

# Inkscape < 1.0 had different options. Auto-detect
inkscape_export_option ?= $(shell (inkscape --help | grep \\--export-filename >/dev/null && echo ' -o') || echo ' -e')

'''
makefile_post = r'''

%.png: %.svg
	inkscape $< ${inkscape_export_option} $@

'''


def px_to_mm(x):
    return x / 3.7795275591

def px(x):
    return str(px_to_mm(x))

def xy(i):
    return i % columns, i // columns

def cell_x(x, dx=1):
    return px(x * (cell_width + 1) + dx)

def cell_y(y, dy=2):
    return px(y * (cell_height + 1) + dy)


transforms = {
    'right': (f'translate({px(-cell_width)}, {px(-2.5 * cell_height)})',
              f'translate(0, {px(-1.5 * cell_height)})',
              f'translate({px(-cell_width)}, {px(-0.5 * cell_height)})',
              f'translate(0, {px(-1.5 * cell_height)})',
              f'translate({px(-cell_width)}, {px(-0.5 * cell_height)})',
              f'translate({px(-cell_width)}, {px(-0.5 * cell_height)})'),
    'left':  (f'translate(0, {px(-2.5 * cell_height)})',
              f'translate({px(-cell_width)}, {px(-1.5 * cell_height)})',
              f'translate(0, {px(-0.5 * cell_height)})',
              f'translate({px(-cell_width)}, {px(-1.5 * cell_height)})',
              f'translate(0, {px(-0.5 * cell_height)})',
              f'translate(0, {px(-0.5 * cell_height)})'),
}


# We copy stuff from generator.svg. In principle we could use external
# references, but my Inkscape doesn't seem to support them.
generator = ET.parse(generator_file)

all_pngs = []
for file_groups in it.combinations(groups, 3):
    # Spec file
    name = '_'.join(file_groups)
    with open(os.path.join(folder, f'{name}.spec'), 'wt') as f:
        f.write(preamble.format(name))
        f.write('tiles = { "row", "column", "tag"\n')
        for i, sprite_groups in enumerate(it.product(file_groups, repeat=3)):
            s = "_".join(g[0] for g in sprite_groups)
            for j, (side, tr) in enumerate(transforms.items()):
                x, y = xy(2 * i + j)
                f.write(f'  {y}, {x}, "t.l0.hex_cell_{side}_{s}"\n')

        f.write('}\n')

    # SVG file
    viewbox = f'0 0 {px_to_mm(total_width)}  {px_to_mm(total_height)}'
    svg = ET.Element('svg',
                     version='1.1',
                     xmlns='http://www.w3.org/2000/svg',
                     width=px(total_width) + 'mm',
                     height=px(total_height) + 'mm',
                     viewBox=viewbox,
                     attrib={'xmlns:xlink': 'http://www.w3.org/1999/xlink'})

    # Merge any <defs> element into our svg
    ns = {'': 'http://www.w3.org/2000/svg'}
    for defs in generator.findall('defs', ns):
        svg.append(defs)

    # Copy sprites into a hidden layer
    hidden = ET.SubElement(svg, 'g', id='generator', style='display: none')
    hidden_sprites = set(groups)
    for g0, g1 in it.permutations(groups, 2):
        hidden_sprites.add(f'{g0}_{g1}_left')
        hidden_sprites.add(f'{g0}_{g1}_centre')
        hidden_sprites.add(f'{g0}_{g1}_right')
    for sprite in hidden_sprites:
        node = generator.find(f'.//g[@id="{sprite}"]', ns)  # They need to be groups
        if node is not None:
            hidden.append(node)

    # Grid (mostly to make it look better)
    grid = ET.SubElement(svg, 'g', id='grid')
    horizontal = ET.SubElement(grid, 'rect', id='hgridrect', width=px(total_width), height=px(1), style='fill: #0f0')
    vertical = ET.SubElement(grid, 'rect', id='vgridrect', width=px(1), height=px(total_height), style='fill: #0f0')

    for x in range(1, columns + 1):
        ET.SubElement(grid, 'use', x=cell_x(x, dx=0), attrib={'xlink:href': '#vgridrect'})
    for y in range(1, rows + 1):
        ET.SubElement(grid, 'use', y=cell_y(y, dy=0), attrib={'xlink:href': '#hgridrect'})

    # Define the clipping rectangle
    # Left
    clip = ET.SubElement(svg, 'clipPath', id='cliprect')
    ET.SubElement(clip, 'rect', x='0', y=px(-1), width=px(cell_width), height=px(cell_height))

    layer = g = ET.SubElement(svg, 'g')

    for i, (g0, g1, g2) in enumerate(it.product(file_groups, repeat=3)):
        for j, (side, tr) in enumerate(transforms.items()):
            x, y = xy(2 * i + j)

            # Images
            g = ET.SubElement(layer, 'g', id=f'tile_{x}_{y}', transform=f'translate({cell_x(x)}, {cell_y(y)})', attrib={'clip-path': 'url(#cliprect)'})

            # Terrains
            ET.SubElement(g, 'use', x='0', y='0', transform=tr[0], attrib={'xlink:href': f'#{g2}'})
            ET.SubElement(g, 'use', x='0', y='0', transform=tr[1], attrib={'xlink:href': f'#{g1}'})
            ET.SubElement(g, 'use', x='0', y='0', transform=tr[2], attrib={'xlink:href': f'#{g0}'})

            # Borders
            up = f'#{g1}_{g2}_right' if side == 'left' else f'#{g1}_{g2}_left'
            down = f'#{g0}_{g1}_left' if side == 'left' else f'#{g0}_{g1}_right'
            ET.SubElement(g, 'use', x='0', y='0', transform=tr[3], attrib={'xlink:href': up})
            ET.SubElement(g, 'use', x='0', y='0', transform=tr[4], attrib={'xlink:href': f'#{g0}_{g2}_centre'})
            ET.SubElement(g, 'use', x='0', y='0', transform=tr[5], attrib={'xlink:href': down})

            # Debugging
            if debug:
                text = ET.SubElement(g, 'text', x='0', y='0',
                                    style='fill: #f0f', attrib={'font-size': '2'})
                ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'[{side}] {g0} {g1} {g2}'


    path = os.path.join(folder, name)
    ET.ElementTree(svg).write(path + '.svg')
    all_pngs.append(name + '.png')


with open(os.path.join(folder, 'Makefile'), 'wt') as f:
    f.write(makefile_preamble)
    f.write('.PHONY: all\n')
    f.write(f'all: {" ".join(all_pngs)}\n')
    f.write(makefile_post)
