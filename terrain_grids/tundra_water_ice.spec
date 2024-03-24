
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
gfx = "vectron/terrain/borders_v2/tundra_water_ice"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 180
dy = 60
pixel_border = 1
tiles = { "row", "column", "tag"
  0, 0, "t.l0.hex_cell_right_t_t_t"
  0, 1, "t.l0.hex_cell_left_t_t_t"
  0, 2, "t.l0.hex_cell_right_t_t_w"
  0, 3, "t.l0.hex_cell_left_t_t_w"
  0, 4, "t.l0.hex_cell_right_t_t_i"
  0, 5, "t.l0.hex_cell_left_t_t_i"
  1, 0, "t.l0.hex_cell_right_t_w_t"
  1, 1, "t.l0.hex_cell_left_t_w_t"
  1, 2, "t.l0.hex_cell_right_t_w_w"
  1, 3, "t.l0.hex_cell_left_t_w_w"
  1, 4, "t.l0.hex_cell_right_t_w_i"
  1, 5, "t.l0.hex_cell_left_t_w_i"
  2, 0, "t.l0.hex_cell_right_t_i_t"
  2, 1, "t.l0.hex_cell_left_t_i_t"
  2, 2, "t.l0.hex_cell_right_t_i_w"
  2, 3, "t.l0.hex_cell_left_t_i_w"
  2, 4, "t.l0.hex_cell_right_t_i_i"
  2, 5, "t.l0.hex_cell_left_t_i_i"
  3, 0, "t.l0.hex_cell_right_w_t_t"
  3, 1, "t.l0.hex_cell_left_w_t_t"
  3, 2, "t.l0.hex_cell_right_w_t_w"
  3, 3, "t.l0.hex_cell_left_w_t_w"
  3, 4, "t.l0.hex_cell_right_w_t_i"
  3, 5, "t.l0.hex_cell_left_w_t_i"
  4, 0, "t.l0.hex_cell_right_w_w_t"
  4, 1, "t.l0.hex_cell_left_w_w_t"
  4, 2, "t.l0.hex_cell_right_w_w_w"
  4, 3, "t.l0.hex_cell_left_w_w_w"
  4, 4, "t.l0.hex_cell_right_w_w_i"
  4, 5, "t.l0.hex_cell_left_w_w_i"
  5, 0, "t.l0.hex_cell_right_w_i_t"
  5, 1, "t.l0.hex_cell_left_w_i_t"
  5, 2, "t.l0.hex_cell_right_w_i_w"
  5, 3, "t.l0.hex_cell_left_w_i_w"
  5, 4, "t.l0.hex_cell_right_w_i_i"
  5, 5, "t.l0.hex_cell_left_w_i_i"
  6, 0, "t.l0.hex_cell_right_i_t_t"
  6, 1, "t.l0.hex_cell_left_i_t_t"
  6, 2, "t.l0.hex_cell_right_i_t_w"
  6, 3, "t.l0.hex_cell_left_i_t_w"
  6, 4, "t.l0.hex_cell_right_i_t_i"
  6, 5, "t.l0.hex_cell_left_i_t_i"
  7, 0, "t.l0.hex_cell_right_i_w_t"
  7, 1, "t.l0.hex_cell_left_i_w_t"
  7, 2, "t.l0.hex_cell_right_i_w_w"
  7, 3, "t.l0.hex_cell_left_i_w_w"
  7, 4, "t.l0.hex_cell_right_i_w_i"
  7, 5, "t.l0.hex_cell_left_i_w_i"
  8, 0, "t.l0.hex_cell_right_i_i_t"
  8, 1, "t.l0.hex_cell_left_i_i_t"
  8, 2, "t.l0.hex_cell_right_i_i_w"
  8, 3, "t.l0.hex_cell_left_i_i_w"
  8, 4, "t.l0.hex_cell_right_i_i_i"
  8, 5, "t.l0.hex_cell_left_i_i_i"
}