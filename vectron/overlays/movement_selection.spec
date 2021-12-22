[spec]

; Client capabilities supported by this file
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]
artists = "
    louis94 (spec files)
    TriClad (visuals)
"

[file]
gfx = "vectron/overlays/movement_selection"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 360
dy = 120
pixel_border = 1

tiles = { "row", "column","tag"
  ; Goto sprites
  0,    0,   "path.exhausted_mp"
  0,    1,   "path.normal"
  0,    2,   "path.step"
  0,    3,   "path.waypoint"

  ; Other required sprites
  0,    4,   "user.attention"

  ; Selected unit
  1,     0,  "unit.select0"
  1,     1,  "unit.select1"
  1,     2,  "unit.select2"
  1,     3,  "unit.select3"
  1,     4,  "unit.select4"
  2,     0,  "unit.select5"
  2,     1,  "unit.select6"
  2,     2,  "unit.select7"
}
