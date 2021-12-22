# Simple svg-to-png converter
# Released in the public domain

files = $(patsubst %.svg,%.png,$(wildcard vectron/*/*.svg))

# Inkscape < 1.0 had different options. Auto-detect
inkscape_export_option ?= $(shell (inkscape --help | grep \\--export-filename >/dev/null && echo ' -o') || echo ' -e')

all: ${files}

clean:
	${RM} ${files}

.PHONY: all

%.png: %.svg
	inkscape $< ${inkscape_export_option} $@
