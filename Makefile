# SPDX-FileCopyrightText: 2021-2022 Louis Moureaux
#
# SPDX-License-Identifier: GPL-3.0-or-later OR CC-BY-SA-4.0

files = $(patsubst %.svg,%.png,$(wildcard vectron/*/*.svg))
files += $(patsubst %.svg,%.png,$(wildcard vectron/*/*/*.svg))

# Inkscape < 1.0 had different options. Auto-detect
inkscape_export_option ?= $(shell (inkscape --help | grep \\--export-filename >/dev/null && echo ' -o') || echo ' -e')

# Generate a list of border files
borders = plains forest swamp water grassland mountains ice desert
borders := $(addprefix vectron/terrain/borders/,$(borders))
borders_spec = $(addsuffix .spec,$(borders))
borders_svg = $(addsuffix .svg,$(borders))
files += $(borders_spec) $(addsuffix .png,$(borders))

all: ${files}

clean:
	${RM} ${files}

.PHONY: all clean

_borders: generate_terrain.py vectron/terrain/borders/generator.svg
	python3 generate_terrain.py
.PHONY: _borders

$(borders_svg): _borders
$(borders_spec): _borders

%.png: %.svg
	inkscape $< ${inkscape_export_option} $@
