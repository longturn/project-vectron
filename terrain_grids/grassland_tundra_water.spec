
; ***** THIS FILE WAS GENERATED *****
; Script: generate_terrain.py
; Changes will be overwritten!
; ***********************************

[spec]

; Client capabilities supported by this file
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]
artists = "
    louis94 (spec files)
    TriClad (visuals)
"

[file]
gfx = "vectron/terrain/borders_v2/grassland_tundra_water"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 180
dy = 60
pixel_border = 1
tiles = { "row", "column", "tag"
  0, 0, "t.l0.hex_cell_right_g_g_g"
  0, 1, "t.l0.hex_cell_left_g_g_g"
  0, 2, "t.l0.hex_cell_right_g_g_t"
  0, 3, "t.l0.hex_cell_left_g_g_t"
  0, 4, "t.l0.hex_cell_right_g_g_w"
  0, 5, "t.l0.hex_cell_left_g_g_w"
  1, 0, "t.l0.hex_cell_right_g_t_g"
  1, 1, "t.l0.hex_cell_left_g_t_g"
  1, 2, "t.l0.hex_cell_right_g_t_t"
  1, 3, "t.l0.hex_cell_left_g_t_t"
  1, 4, "t.l0.hex_cell_right_g_t_w"
  1, 5, "t.l0.hex_cell_left_g_t_w"
  2, 0, "t.l0.hex_cell_right_g_w_g"
  2, 1, "t.l0.hex_cell_left_g_w_g"
  2, 2, "t.l0.hex_cell_right_g_w_t"
  2, 3, "t.l0.hex_cell_left_g_w_t"
  2, 4, "t.l0.hex_cell_right_g_w_w"
  2, 5, "t.l0.hex_cell_left_g_w_w"
  3, 0, "t.l0.hex_cell_right_t_g_g"
  3, 1, "t.l0.hex_cell_left_t_g_g"
  3, 2, "t.l0.hex_cell_right_t_g_t"
  3, 3, "t.l0.hex_cell_left_t_g_t"
  3, 4, "t.l0.hex_cell_right_t_g_w"
  3, 5, "t.l0.hex_cell_left_t_g_w"
  4, 0, "t.l0.hex_cell_right_t_t_g"
  4, 1, "t.l0.hex_cell_left_t_t_g"
  4, 2, "t.l0.hex_cell_right_t_t_t"
  4, 3, "t.l0.hex_cell_left_t_t_t"
  4, 4, "t.l0.hex_cell_right_t_t_w"
  4, 5, "t.l0.hex_cell_left_t_t_w"
  5, 0, "t.l0.hex_cell_right_t_w_g"
  5, 1, "t.l0.hex_cell_left_t_w_g"
  5, 2, "t.l0.hex_cell_right_t_w_t"
  5, 3, "t.l0.hex_cell_left_t_w_t"
  5, 4, "t.l0.hex_cell_right_t_w_w"
  5, 5, "t.l0.hex_cell_left_t_w_w"
  6, 0, "t.l0.hex_cell_right_w_g_g"
  6, 1, "t.l0.hex_cell_left_w_g_g"
  6, 2, "t.l0.hex_cell_right_w_g_t"
  6, 3, "t.l0.hex_cell_left_w_g_t"
  6, 4, "t.l0.hex_cell_right_w_g_w"
  6, 5, "t.l0.hex_cell_left_w_g_w"
  7, 0, "t.l0.hex_cell_right_w_t_g"
  7, 1, "t.l0.hex_cell_left_w_t_g"
  7, 2, "t.l0.hex_cell_right_w_t_t"
  7, 3, "t.l0.hex_cell_left_w_t_t"
  7, 4, "t.l0.hex_cell_right_w_t_w"
  7, 5, "t.l0.hex_cell_left_w_t_w"
  8, 0, "t.l0.hex_cell_right_w_w_g"
  8, 1, "t.l0.hex_cell_left_w_w_g"
  8, 2, "t.l0.hex_cell_right_w_w_t"
  8, 3, "t.l0.hex_cell_left_w_w_t"
  8, 4, "t.l0.hex_cell_right_w_w_w"
  8, 5, "t.l0.hex_cell_left_w_w_w"
}
