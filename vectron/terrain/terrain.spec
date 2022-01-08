[spec]

; Client capabilities supported by this file
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]
artists = "
    louis94 (spec files)
    TriClad (visuals)
"

[file]
gfx = "vectron/terrain/terrain"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 360
dy = 180
pixel_border = 1

tiles = { "row", "column","tag"
  ; Grassland
  0,    0,  "t.l0.grassland1"
  0,    0,  "t.l0.grassland2"
  0,    0,  "t.l0.grassland4"
  0,    0,  "t.l0.grassland5"
  0,    0,  "t.l0.grassland7"
  0,    0,  "t.l0.grassland8"
  0,    0,  "t.l0.grassland10"
  0,    0,  "t.l0.grassland11"
  0,    0,  "t.l0.grassland13"
  0,    0,  "t.l0.grassland14"
  0,    0,  "t.l0.grassland16"
  0,    0,  "t.l0.grassland17"
  0,    0,  "t.l0.grassland19"
  0,    0,  "t.l0.grassland20"
  0,    0,  "t.l0.grassland22"
  0,    0,  "t.l0.grassland23"
  0,    0,  "t.l0.grassland25"
  0,    0,  "t.l0.grassland26"

  0,    1,  "t.l0.grassland3"
  0,    2,  "t.l0.grassland6"
  0,    3,  "t.l0.grassland9"
  0,    4,  "t.l0.grassland12"
  0,    5,  "t.l0.grassland15"
  0,    6,  "t.l0.grassland18"
  0,    7,  "t.l0.grassland21"
  0,    8,  "t.l0.grassland24"
  0,    9,  "t.l0.grassland27"

  ; Plains
  1,    0,  "t.l0.plains1"
  1,    1,  "t.l0.plains2"

  ; Swamp
  2,    0,  "t.l0.swamp1"
  2,    1,  "t.l0.swamp2"

  ; Desert
  3,    0,  "t.l0.desert1"

  ; Tundra
  4,    0,  "t.l0.tundra1"

  ; Arctic
  5,    0,  "t.l0.arctic1"

  ; Lake
  6,    0,  "t.l0.lake1"

  ; Coast -- FIXME not needed, uses water.spec
  ;7,    0,  "t.l0.coast1"

  ; Deep ocean
  8,    0,  "t.l0.floor1"

  ; Missing base terrain sprites
  ; Use transparent placeholders
  10,    0,  "t.l0.inaccessible1"

  ; Resources and other extras
  ; Use transparent placeholder
  10,    0,   "base.airstrip"
  10,    0,   "base.airbase"
  10,    0,   "base.buoy"
  10,    0,   "base.fortress"
  10,    0,   "base.outpost"
  10,    0,   "extra.ruins"
  10,    0,   "road.maglev"
  10,    0,   "road.pave"
  10,    0,   "road.rail"
  10,    0,   "road.road"
  10,    0,   "road.river"
}
