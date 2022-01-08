import xml.etree.ElementTree as ET
import itertools as it
import os

groups = [
    'plains',
    'forest',
    'swamp',
    'water',
    'grassland',
    'mountains',
    'ice',
    'desert',
]

folder = os.path.join('vectron', 'terrain', 'borders')
os.makedirs(folder, exist_ok=True)

columns = len(groups)
rows = len(groups)**2

debug = False  # Set to true to display which sprites are used

cell_width = 360
cell_height = 120

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
gfx = "vectron/terrain/borders/{{}}"

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
    with open(os.path.join(folder, f'{g0}.spec'), 'wt') as f:
        f.write(preamble.format(g0))
        f.write('tiles = { "row", "column", "tag"\n')
        for i, (g1, g2, g3) in enumerate(it.product(groups, groups, groups)):
            x, y = xy(i)

            #  \   2   /
            # 1 \_____/ 3
            #   /     \
            #  /   0   \
            f.write(f'  {y}, {x}, "t.l1.cellgroup_{g2[0]}_{g3[0]}_{g0[0]}_{g1[0]}"\n')
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

    # Copy needed sprites into a hidden layer
    hidden = ET.SubElement(svg, 'g', id='generator', style='display: none')
    sprites = set()
    for g1, g2, g3 in it.product(groups, groups, groups):
        # Top part
        sprites.add(f'{g2}_{g1}_left')
        sprites.add(f'{g2}_{g3}_right')
        # Bottom part
        sprites.add(f'{g0}_{g1}_left')
        sprites.add(f'{g0}_{g2}_center')
        sprites.add(f'{g0}_{g3}_right')
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
    clip = ET.SubElement(svg, 'clipPath', id='cliprect')
    ET.SubElement(clip, 'rect', x='0', y=px(-1), width=px(cell_width), height=px(cell_height))

    # Images
    for i, (g1, g2, g3) in enumerate(it.product(groups, groups, groups)):
        x, y = xy(i)
        g = ET.SubElement(svg, 'g', id=f'tile_{x}_{y}', transform=f'translate({cell_x(x)}, {cell_y(y)})', attrib={'clip-path': 'url(#cliprect)'})

        # Top part (offsetting automatically; the numbers work but are a bit arbitrary)
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate({px(-cell_width // 2)}, {px(-cell_height // 2)})', attrib={'xlink:href': f'#{g1}_{g2}_right'})
        ET.SubElement(g, 'use', x='0', y='0', transform=f'translate({px(cell_width // 2)}, {px(-cell_height // 2)})', attrib={'xlink:href': f'#{g3}_{g2}_left'})
        # Bottom part
        ET.SubElement(g, 'use', x='0', y='0', attrib={'xlink:href': f'#{g0}_{g1}_left'})
        ET.SubElement(g, 'use', x='0', y='0', attrib={'xlink:href': f'#{g0}_{g2}_center'})
        ET.SubElement(g, 'use', x='0', y='0', attrib={'xlink:href': f'#{g0}_{g3}_right'})

        # Debugging
        if debug:
            text = ET.SubElement(g, 'text', x='0', y='0',
                                style='fill: #f0f', attrib={'font-size': '4'})
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'{g0} {g1} {g2} {g3}'
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'top left: #{g1}_{g2}_right'
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'top right: #{g3}_{g2}_left'
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'bottom left: #{g0}_{g1}_left'
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'bottom center: #{g0}_{g2}_center'
            ET.SubElement(text, 'tspan',  x='0', dy='1.2em').text = f'bottom right: #{g0}_{g3}_right'

    ET.ElementTree(svg).write(os.path.join(folder, f'{g0}.svg'))
