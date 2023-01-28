# SPDX-FileCopyrightText: 2021-2022 Louis Moureaux
#
# SPDX-License-Identifier: GPL-3.0-or-later OR CC-BY-SA-4.0

files = $(patsubst %.svg,%.png,$(wildcard vectron/*/*.svg))
files += $(patsubst %.svg,%.png,$(wildcard vectron/*/*/*.svg))

all: _borders ${files}

clean:
	$(RM) ${files}
	$(RM) -r tmp
	$(RM) -r vectron/terrain/borders

.PHONY: all clean

.PHONY: _borders
_borders: tmp/borders/Makefile
	@$(MAKE) -C tmp/borders
	@echo "-- Copying..."
	@mkdir -p vectron/terrain/borders
	@cp tmp/borders/*.png tmp/borders/borders.spec vectron/terrain/borders

tmp/borders/Makefile: generate_terrain.py vectron/terrain/border_generator.svg
	python3 generate_terrain.py

%.png: %.svg
	@echo "-- Rendering $@..."
	@rsvg-convert $< -o $@
