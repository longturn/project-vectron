[spec]

; Client capabilities supported by this file
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]
artists = "
    louis94 (spec files)
    TriClad (visuals)
"

[file]
gfx = "vectron/terrain/water"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 180
dy = 60
pixel_border = 1

tiles = { "row", "column","tag"
  ; Beaches
  0,    0,  "t.l0.coast_cell_d111"
  0,    1,  "t.l0.coast_cell_d110"
  0,    2,  "t.l0.coast_cell_d100"
  0,    3,  "t.l0.coast_cell_d000"

  1,    0,  "t.l0.coast_cell_d001"
  1,    1,  "t.l0.coast_cell_d010"
  1,    2,  "t.l0.coast_cell_d011"
  1,    3,  "t.l0.coast_cell_d101"

  0,    4,  "t.l0.coast_cell_l000"
  0,    4,  "t.l0.coast_cell_l010"
  0,    5,  "t.l0.coast_cell_l001"
  0,    5,  "t.l0.coast_cell_l011"

  1,    4,  "t.l0.coast_cell_l100"
  1,    4,  "t.l0.coast_cell_l110"
  1,    5,  "t.l0.coast_cell_l111"
  1,    5,  "t.l0.coast_cell_l101"

  3,    0,  "t.l0.coast_cell_u111"
  3,    1,  "t.l0.coast_cell_u011"
  3,    2,  "t.l0.coast_cell_u001"
  3,    3,  "t.l0.coast_cell_u000"

  2,    0,  "t.l0.coast_cell_u100"
  2,    1,  "t.l0.coast_cell_u010"
  2,    2,  "t.l0.coast_cell_u110"
  2,    3,  "t.l0.coast_cell_u101"

  2,    4,  "t.l0.coast_cell_r000"
  2,    4,  "t.l0.coast_cell_r010"
  2,    5,  "t.l0.coast_cell_r001"
  2,    5,  "t.l0.coast_cell_r011"

  3,    4,  "t.l0.coast_cell_r100"
  3,    4,  "t.l0.coast_cell_r110"
  3,    5,  "t.l0.coast_cell_r101"
  3,    5,  "t.l0.coast_cell_r111"

}
