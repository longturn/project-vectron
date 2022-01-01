[spec]

; Client capabilities supported by this file
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]
artists = "
    louis94 (spec files)
    TriClad (visuals)
"

[file]
gfx = "vectron/terrain/hills_mountains"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 360
dy = 180
pixel_border = 1

tiles = { "row", "column","tag"
  ; Hill sprites
  0,    0,  "t.l1.hills1"
  0,    1,  "t.l1.hills2"
  0,    2,  "t.l1.hills3"
  0,    3,  "t.l1.hills4"

  ; Mountain sprites
  1,    0,  "t.l1.mountains1"
  1,    1,  "t.l1.mountains2"
}
