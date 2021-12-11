# Simple svg-to-png converter
# Released in the public domain

files = vectron/movement_selection.png \
        vectron/terrain.png            \
        vectron/terrain_blending.png   \
        vectron/tile_addons.png        \
        vectron/tile_specials.png

all: ${files}

clean:
	${RM} ${files}

.PHONY: all

%.png: %.svg
	inkscape $< -o $@
