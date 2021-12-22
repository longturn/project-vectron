[spec]

; Client capabilities supported by this file
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]
artists = "
    louis94 (spec files)
    TriClad (visuals)
"

[file]
gfx = "vectron/terrain/tile_addons"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 360
dy = 120
pixel_border = 1

tiles = { "row", "column","tag"
  ; Resources and other extras
  0,    0,   "tx.oil_mine"
  0,    1,   "tx.mine"
  0,    2,   "tx.oil_rig"
  1,    0,   "tx.irrigation"
  1,    1,   "tx.farmland"
  1,    2,   "tx.fallout"
  3,    0,   "tx.pollution"
  3,    1,   "tx.village"
}
