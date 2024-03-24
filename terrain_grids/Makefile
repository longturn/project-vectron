
# ***** THIS FILE WAS GENERATED *****
# Script: generate_terrain.py
# Changes will be overwritten!
# ***********************************

# Inkscape < 1.0 had different options. Auto-detect
inkscape_export_option ?= $(shell (inkscape --help | grep \\--export-filename >/dev/null && echo ' -o') || echo ' -e')

.PHONY: all
all: plains_grassland_swamp.png plains_grassland_tundra.png plains_grassland_water.png plains_grassland_mountains.png plains_grassland_ice.png plains_grassland_desert.png plains_swamp_tundra.png plains_swamp_water.png plains_swamp_mountains.png plains_swamp_ice.png plains_swamp_desert.png plains_tundra_water.png plains_tundra_mountains.png plains_tundra_ice.png plains_tundra_desert.png plains_water_mountains.png plains_water_ice.png plains_water_desert.png plains_mountains_ice.png plains_mountains_desert.png plains_ice_desert.png grassland_swamp_tundra.png grassland_swamp_water.png grassland_swamp_mountains.png grassland_swamp_ice.png grassland_swamp_desert.png grassland_tundra_water.png grassland_tundra_mountains.png grassland_tundra_ice.png grassland_tundra_desert.png grassland_water_mountains.png grassland_water_ice.png grassland_water_desert.png grassland_mountains_ice.png grassland_mountains_desert.png grassland_ice_desert.png swamp_tundra_water.png swamp_tundra_mountains.png swamp_tundra_ice.png swamp_tundra_desert.png swamp_water_mountains.png swamp_water_ice.png swamp_water_desert.png swamp_mountains_ice.png swamp_mountains_desert.png swamp_ice_desert.png tundra_water_mountains.png tundra_water_ice.png tundra_water_desert.png tundra_mountains_ice.png tundra_mountains_desert.png tundra_ice_desert.png water_mountains_ice.png water_mountains_desert.png water_ice_desert.png mountains_ice_desert.png


%.png: %.svg
	inkscape $< ${inkscape_export_option} $@

