[spec]

; Client capabilities supported by this file
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]
artists = "
    louis94 (spec files)
    TriClad (visuals)
"

[file]
gfx = "vectron/terrain/terrain_blending"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 360
dy = 120
pixel_border = 1

tiles = { "row", "column","tag"
  0,    0,   "t.dither_tile"
  0,    1,   "mask.tile"
  0,    2,   "tx.fog"
  2,    0,   "tx.darkness_n"
  2,    1,   "tx.darkness_e"
  2,    2,   "tx.darkness_se"
  3,    0,   "tx.darkness_s"
  3,    1,   "tx.darkness_w"
  3,    2,   "tx.darkness_nw"
}
