# SPDX-FileCopyrightText: 2021-2022 Louis Moureaux
#
# SPDX-License-Identifier: GPL-3.0-or-later OR CC-BY-SA-4.0

files = $(patsubst %.svg,%.png,$(wildcard vectron/*/*.svg))
files += $(patsubst %.svg,%.png,$(wildcard vectron/*/*/*.svg))

# Inkscape < 1.0 had different options. Auto-detect
inkscape_export_option ?= $(shell (inkscape --help | grep \\--export-filename >/dev/null && echo ' -o') || echo ' -e')

all: _terrain_grids ${files}

clean:
	${RM} ${files}
	${RM} -r ${terrain_grids}

.PHONY: all clean

.PHONY: _terrain_grids
_terrain_grids: terrain_grids/Makefile
terrain_grids/Makefile: generate_terrain.py vectron/terrain/borders/generator.svg
	python3 generate_terrain.py
	${MAKE} -C terrain_grids

%.png: %.svg
	inkscape $< ${inkscape_export_option} $@
