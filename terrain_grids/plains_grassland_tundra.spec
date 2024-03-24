
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
gfx = "vectron/terrain/borders_v2/plains_grassland_tundra"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 180
dy = 60
pixel_border = 1
tiles = { "row", "column", "tag"
  0, 0, "t.l0.hex_cell_right_p_p_p"
  0, 1, "t.l0.hex_cell_left_p_p_p"
  0, 2, "t.l0.hex_cell_right_p_p_g"
  0, 3, "t.l0.hex_cell_left_p_p_g"
  0, 4, "t.l0.hex_cell_right_p_p_t"
  0, 5, "t.l0.hex_cell_left_p_p_t"
  1, 0, "t.l0.hex_cell_right_p_g_p"
  1, 1, "t.l0.hex_cell_left_p_g_p"
  1, 2, "t.l0.hex_cell_right_p_g_g"
  1, 3, "t.l0.hex_cell_left_p_g_g"
  1, 4, "t.l0.hex_cell_right_p_g_t"
  1, 5, "t.l0.hex_cell_left_p_g_t"
  2, 0, "t.l0.hex_cell_right_p_t_p"
  2, 1, "t.l0.hex_cell_left_p_t_p"
  2, 2, "t.l0.hex_cell_right_p_t_g"
  2, 3, "t.l0.hex_cell_left_p_t_g"
  2, 4, "t.l0.hex_cell_right_p_t_t"
  2, 5, "t.l0.hex_cell_left_p_t_t"
  3, 0, "t.l0.hex_cell_right_g_p_p"
  3, 1, "t.l0.hex_cell_left_g_p_p"
  3, 2, "t.l0.hex_cell_right_g_p_g"
  3, 3, "t.l0.hex_cell_left_g_p_g"
  3, 4, "t.l0.hex_cell_right_g_p_t"
  3, 5, "t.l0.hex_cell_left_g_p_t"
  4, 0, "t.l0.hex_cell_right_g_g_p"
  4, 1, "t.l0.hex_cell_left_g_g_p"
  4, 2, "t.l0.hex_cell_right_g_g_g"
  4, 3, "t.l0.hex_cell_left_g_g_g"
  4, 4, "t.l0.hex_cell_right_g_g_t"
  4, 5, "t.l0.hex_cell_left_g_g_t"
  5, 0, "t.l0.hex_cell_right_g_t_p"
  5, 1, "t.l0.hex_cell_left_g_t_p"
  5, 2, "t.l0.hex_cell_right_g_t_g"
  5, 3, "t.l0.hex_cell_left_g_t_g"
  5, 4, "t.l0.hex_cell_right_g_t_t"
  5, 5, "t.l0.hex_cell_left_g_t_t"
  6, 0, "t.l0.hex_cell_right_t_p_p"
  6, 1, "t.l0.hex_cell_left_t_p_p"
  6, 2, "t.l0.hex_cell_right_t_p_g"
  6, 3, "t.l0.hex_cell_left_t_p_g"
  6, 4, "t.l0.hex_cell_right_t_p_t"
  6, 5, "t.l0.hex_cell_left_t_p_t"
  7, 0, "t.l0.hex_cell_right_t_g_p"
  7, 1, "t.l0.hex_cell_left_t_g_p"
  7, 2, "t.l0.hex_cell_right_t_g_g"
  7, 3, "t.l0.hex_cell_left_t_g_g"
  7, 4, "t.l0.hex_cell_right_t_g_t"
  7, 5, "t.l0.hex_cell_left_t_g_t"
  8, 0, "t.l0.hex_cell_right_t_t_p"
  8, 1, "t.l0.hex_cell_left_t_t_p"
  8, 2, "t.l0.hex_cell_right_t_t_g"
  8, 3, "t.l0.hex_cell_left_t_t_g"
  8, 4, "t.l0.hex_cell_right_t_t_t"
  8, 5, "t.l0.hex_cell_left_t_t_t"
}
