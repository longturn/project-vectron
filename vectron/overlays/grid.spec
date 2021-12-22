[spec]

; Client capabilities supported by this file
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]
artists = "
    louis94 (spec files)
    TriClad (visuals)
"

[file]
gfx = "vectron/overlays/grid"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 360
dy = 120
pixel_border = 1

tiles = { "row", "column","tag"
  ; Grid sprites
  0, 0, "grid.main.we"
  0, 1, "grid.main.ud"
  0, 2, "grid.main.ns"

  1, 0, "grid.city.we"
  1, 1, "grid.city.ud"
  1, 2, "grid.city.ns"

  2, 0, "grid.worked.we"
  2, 1, "grid.worked.ud"
  2, 2, "grid.worked.ns"

  3, 0, "grid.selected.we"
  3, 1, "grid.selected.ud"
  3, 2, "grid.selected.ns"

  4, 0, "grid.coastline.we"
  4, 1, "grid.coastline.ud"
  4, 2, "grid.coastline.ns"

  5, 3, "grid.borders.w"
  5, 0, "grid.borders.e"
  5, 5, "grid.borders.n"
  5, 2, "grid.borders.s"
  5, 4, "grid.borders.u"
  5, 1, "grid.borders.d"

  6, 0, "grid.unavailable"
  6, 1, "grid.nonnative"
}
