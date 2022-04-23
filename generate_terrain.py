import xml.etree.ElementTree as ET
import itertools as it
import math
import os

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

folder = os.path.join('vectron', 'terrain', 'borders')
os.makedirs(folder, exist_ok=True)

cells = 2 * len(groups)**2
columns = int(math.floor(math.sqrt(cells))) // 2
rows = int(math.ceil(cells / columns))

debug = False # Set to true to display which sprites are used

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
gfx = "vectron/terrain/borders/corners_{{}}"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = {cell_width}
dy = {cell_height}
pixel_border = 1
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

for g0 in groups:
    # Spec file
    with open(os.path.join(folder, f'corners_{g0}.spec'), 'wt') as f:
        f.write(preamble.format(g0))
        f.write('tiles = { "row", "column", "tag"\n')
        for i, (g1, g2) in enumerate(it.product(groups, groups)):
            # Left hand side (for the tileset, right)
            #  \   2
            # 1 \___
            #   /
            #  /   0
            x, y = xy(2 * i)
            f.write(f'  {y}, {x}, "t.l0.hex_cell_right_{g1[0]}_{g2[0]}_{g0[0]}"\n')

            # Then right hand side (for the tileset, left)
            #  2   /
            # ____/ 1
            #     \
            #  0   \

            x, y = xy(2 * i + 1)
            f.write(f'  {y}, {x}, "t.l0.hex_cell_left_{g1[0]}_{g2[0]}_{g0[0]}"\n')
        f.write('}\n')

    # SVG file
    svg = ET.Element('svg',
                    version='1.1',
                    xmlns='http://www.w3.org/2000/svg',
                    width=px(total_width) + 'mm',
                    height=px(total_height) + 'mm',
                    viewBox=f'0 0 {px_to_mm(total_width)} {px_to_mm(total_height)}',
                    attrib={'xmlns:xlink': 'http://www.w3.org/1999/xlink'})

    # We copy stuff from generator.svg. In principle we could use external
    # references, but my Inkscape doesn't seem to support them.
    generator = ET.parse(os.path.join(folder, 'generator.svg'))

    # Merge any <defs> element into our svg
    ns = {'': 'http://www.w3.org/2000/svg'}
    for defs in generator.findall('defs', ns):
        svg.append(defs)

    # Copy sprites into a hidden layer
    hidden = ET.SubElement(svg, 'g', id='generator', style='display: none')
    sprites = set(groups)
    for g1 in groups:
        sprites.add(f'{g0}_{g1}_left')
        sprites.add(f'{g0}_{g1}_centre')
        sprites.add(f'{g0}_{g1}_right')
    for sprite in sprites:
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

    for i, (g1, g2) in enumerate(it.product(groups, groups)):
        # Left hand side first
        #  \   2
        # 1 \___
        #   /
        #  /   0

        x, y = xy(2 * i)

        # Images
        g = ET.SubElement(svg, 'g', id=f'tile_{x}_{y}', transform=f'translate({cell_x(x)}, {cell_y(y)})', attrib={'clip-path': 'url(#cliprect)'})

        # Terrains (offsetting automatically; the numbers work but are a bit arbitrary)
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate(0, {px(-2.5 * cell_height)})', attrib={'xlink:href': f'#{g2}'})
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate({px(-cell_width)}, {px(-1.5 * cell_height)})', attrib={'xlink:href': f'#{g1}'})
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate(0, {px(-0.5 * cell_height)})', attrib={'xlink:href': f'#{g0}'})

        # Borders (offsetting automatically; the numbers work but are a bit arbitrary)
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate({px(-cell_width)}, {px(-2.5 * cell_height)})', attrib={'xlink:href': f'#{g1}_{g2}_right'})
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate(0, {px(-0.5 * cell_height)})', attrib={'xlink:href': f'#{g0}_{g2}_centre'})
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate(0, {px(-0.5 * cell_height)})', attrib={'xlink:href': f'#{g0}_{g1}_left'})

        # Debugging
        if debug:
            text = ET.SubElement(g, 'text', x='0', y='0',
                                style='fill: #f0f', attrib={'font-size': '2'})
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'left: #{g1}_{g2}_right'
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'centre: #{g0}_{g2}_left'
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'right: #{g0}_{g1}_left'


        # Then right hand side
        #  2   /
        # ____/ 1
        #     \
        #  0   \

        x, y = xy(2 * i + 1)

        # Images
        g = ET.SubElement(svg, 'g', id=f'tile_{x}_{y}', transform=f'translate({cell_x(x)}, {cell_y(y)})', attrib={'clip-path': 'url(#cliprect)'})

        # Terrains (offsetting automatically; the numbers work but are a bit arbitrary)
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate({px(-cell_width)}, {px(-2.5 * cell_height)})', attrib={'xlink:href': f'#{g2}'})
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate(0, {px(-1.5 * cell_height)})', attrib={'xlink:href': f'#{g1}'})
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate({px(-cell_width)}, {px(-0.5 * cell_height)})', attrib={'xlink:href': f'#{g0}'})

        # Borders (offsetting automatically; the numbers work but are a bit arbitrary)
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate(0, {px(-2.5 * cell_height)})', attrib={'xlink:href': f'#{g1}_{g2}_left'})
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate({px(-cell_width)}, {px(-0.5 * cell_height)})', attrib={'xlink:href': f'#{g0}_{g2}_centre'})
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate({px(-cell_width)}, {px(-0.5 * cell_height)})', attrib={'xlink:href': f'#{g0}_{g1}_right'})

        # Debugging
        if debug:
            text = ET.SubElement(g, 'text', x='0', y='0',
                                style='fill: #f0f', attrib={'font-size': '2'})
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'left: #{g1}_{g2}_right'
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'centre: #{g0}_{g2}_left'
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'right: #{g0}_{g1}_left'

    ET.ElementTree(svg).write(os.path.join(folder, f'corners_{g0}.svg'))
