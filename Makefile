# Simple svg-to-png converter
# Released in the public domain

files = vectron/terrain.png

all: ${files}

clean:
	${RM} ${files}

.PHONY: all

%.png: %.svg
	inkscape $< -o $@
