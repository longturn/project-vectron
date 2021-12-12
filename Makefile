# Simple svg-to-png converter
# Released in the public domain

files = vectron/movement_selection.png \
        vectron/terrain.png            \
        vectron/terrain_blending.png   \
        vectron/tile_addons.png        \
        vectron/tile_specials.png

# Inkscape < 1.0 had different options. Auto-detect
inkscape_export_option ?= $(shell (inkscape --help | grep \\--export-filename >/dev/null && echo ' -o') || echo ' -e')

all: ${files}

clean:
	${RM} ${files}

.PHONY: all

%.png: %.svg
	inkscape $< ${inkscape_export_option} $@
