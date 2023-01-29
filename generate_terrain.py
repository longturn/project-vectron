import xml.etree.ElementTree as ET
import filecmp
import itertools as it
import multiprocessing as mp
import os
import shutil
import tempfile


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

generator_file = os.path.join('vectron', 'terrain', 'border_generator.svg')
folder = os.path.join('tmp', 'borders')

width = 180
height = 60

px_to_mm = 0.26458335

def px(x):
    return px_to_mm * x


def translate(tr_x, tr_y):
    # Strange offset in the generator svg
    dx, dy = (-9.3245926e-06, -0.08928591)
    return f'translate({px(tr_x) - dx}, {px(tr_y) - dy})'


transforms = {
    'left':  (translate(-width, -2.5 * height),
              translate(0, -1.5 * height),
              translate(-width, -0.5 * height),
              translate(0, -1.5 * height),
              translate(-width, -0.5 * height),
              translate(-width, -0.5 * height)),
    'right': (translate(0, -2.5 * height),
              translate(-width, -1.5 * height),
              translate(0, -0.5 * height),
              translate(-width, -1.5 * height),
              translate(0, -0.5 * height),
              translate(0, -0.5 * height)),
}


# We copy stuff from generator.svg. In principle we could use external
# references, but my Inkscape doesn't seem to support them.
generator = ET.parse(generator_file)

gen_sprites = set(groups)
for g0, g1 in it.permutations(groups, 2):
    gen_sprites.add(f'{g0}_{g1}_left')
    gen_sprites.add(f'{g0}_{g1}_centre')
    gen_sprites.add(f'{g0}_{g1}_right')
gen_sprites = sorted(gen_sprites)

svg_ns = {'': 'http://www.w3.org/2000/svg'}

cache = dict()
for sprite in gen_sprites:
    node = generator.find(f'.//g[@id="{sprite}"]', svg_ns)  # They need to be groups
    if node is not None:
        cache[sprite] = node


def make_svg(side, file_groups):
    viewbox = f'0 0 {px(width)} {px(height)}'
    svg = ET.Element('svg',
                     version='1.1',
                     xmlns='http://www.w3.org/2000/svg',
                     width=f'{px(width)}mm',
                     height=f'{px(height)}mm',
                     viewBox=viewbox,
                     attrib={'xmlns:xlink': 'http://www.w3.org/1999/xlink'})

    # Merge any <defs> element into our svg
    for defs in generator.findall('defs', svg_ns):
        svg.append(defs)

    # Copy sprites into a hidden layer
    hidden = ET.SubElement(svg, 'g', id='generator', style='display: none')
    hidden_sprites = set(file_groups)
    for g0, g1 in it.permutations(file_groups, 2):
        hidden_sprites.add(f'{g0}_{g1}_left')
        hidden_sprites.add(f'{g0}_{g1}_centre')
        hidden_sprites.add(f'{g0}_{g1}_right')
    for sprite in sorted(hidden_sprites):
        if sprite in cache:
            hidden.append(cache[sprite])

    tr = transforms[side]
    g0, g1, g2 = file_groups

    # Terrains
    ET.SubElement(svg, 'use', x='0', y='0', transform=tr[0], attrib={'xlink:href': f'#{g1}'})
    ET.SubElement(svg, 'use', x='0', y='0', transform=tr[1], attrib={'xlink:href': f'#{g0}'})
    ET.SubElement(svg, 'use', x='0', y='0', transform=tr[2], attrib={'xlink:href': f'#{g2}'})

    # Borders
    up = f'#{g0}_{g1}_right' if side == 'right' else f'#{g0}_{g1}_left'
    down = f'#{g2}_{g0}_right' if side == 'left' else f'#{g2}_{g0}_left'
    ET.SubElement(svg, 'use', x='0', y='0', transform=tr[3], attrib={'xlink:href': up})
    ET.SubElement(svg, 'use', x='0', y='0', transform=tr[4], attrib={'xlink:href': f'#{g2}_{g1}_centre'})
    ET.SubElement(svg, 'use', x='0', y='0', transform=tr[5], attrib={'xlink:href': down})

    # Save
    name = side + '_' + '_'.join(file_groups) + '.svg'
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = os.path.join(tmp, name)
        with open(tmp_path, mode='wb') as out:
            ET.ElementTree(svg).write(out)

        # Only modify if it changed (speed up incremental builds)
        path = os.path.join(folder, name)
        if os.path.isfile(path) and filecmp.cmp(path, tmp_path):
            print(f'-- Skipped {path}')
        else:
            print(f'-- Generated {path}')
            shutil.move(tmp_path, path)


def make_spec(all_sprites):
    preamble = '''\
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

[extra]
sprites = {
  "tag", "file"
'''
    footer = '}\n'

    with open(os.path.join(folder, f'borders.spec'), 'wt') as f:
        f.write(preamble)
        for side, file_groups in all_sprites:
            name = side + '_' + '_'.join(file_groups)
            s = "_".join(g[0] for g in file_groups)
            f.write(f'  "t.l0.hex_cell_{side}_{s}", "vectron/terrain/borders/{name}"\n')

        f.write(footer)


def make_makefile(all_sprites):
    preamble = '''\
# ***** THIS FILE WAS GENERATED *****
# Script: generate_terrain.py
# Changes will be overwritten!
# ***********************************

%.png: %.svg
	@echo "-- Rendering $@"
	@rsvg-convert $< -o $@

'''

    with open(os.path.join(folder, 'Makefile'), 'wt') as f:
        f.write(preamble)
        f.write('.PHONY: all\n')
        f.write('all: \\\n')

        all_pngs = []
        for side, file_groups in all_sprites:
            name = side + '_' + '_'.join(file_groups)
            f.write(f'  {name}.png \\\n')

        f.write('\n')


if __name__ == '__main__':
    os.makedirs(folder, exist_ok=True)

    all_sprites = list(it.product(transforms.keys(), it.product(groups, repeat=3)))
    print(f'-- Will generate {len(all_sprites)} sprites')

    with mp.Pool() as pool:
        pool.starmap(make_svg, all_sprites)

    print(f'Making spec file...')
    make_spec(all_sprites)

    print(f'Making Makefile...')
    make_makefile(all_sprites)
