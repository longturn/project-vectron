
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
gfx = "vectron/terrain/borders_v2/grassland_tundra_mountains"

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
  0, 4, "t.l0.hex_cell_right_g_g_m"
  0, 5, "t.l0.hex_cell_left_g_g_m"
  1, 0, "t.l0.hex_cell_right_g_t_g"
  1, 1, "t.l0.hex_cell_left_g_t_g"
  1, 2, "t.l0.hex_cell_right_g_t_t"
  1, 3, "t.l0.hex_cell_left_g_t_t"
  1, 4, "t.l0.hex_cell_right_g_t_m"
  1, 5, "t.l0.hex_cell_left_g_t_m"
  2, 0, "t.l0.hex_cell_right_g_m_g"
  2, 1, "t.l0.hex_cell_left_g_m_g"
  2, 2, "t.l0.hex_cell_right_g_m_t"
  2, 3, "t.l0.hex_cell_left_g_m_t"
  2, 4, "t.l0.hex_cell_right_g_m_m"
  2, 5, "t.l0.hex_cell_left_g_m_m"
  3, 0, "t.l0.hex_cell_right_t_g_g"
  3, 1, "t.l0.hex_cell_left_t_g_g"
  3, 2, "t.l0.hex_cell_right_t_g_t"
  3, 3, "t.l0.hex_cell_left_t_g_t"
  3, 4, "t.l0.hex_cell_right_t_g_m"
  3, 5, "t.l0.hex_cell_left_t_g_m"
  4, 0, "t.l0.hex_cell_right_t_t_g"
  4, 1, "t.l0.hex_cell_left_t_t_g"
  4, 2, "t.l0.hex_cell_right_t_t_t"
  4, 3, "t.l0.hex_cell_left_t_t_t"
  4, 4, "t.l0.hex_cell_right_t_t_m"
  4, 5, "t.l0.hex_cell_left_t_t_m"
  5, 0, "t.l0.hex_cell_right_t_m_g"
  5, 1, "t.l0.hex_cell_left_t_m_g"
  5, 2, "t.l0.hex_cell_right_t_m_t"
  5, 3, "t.l0.hex_cell_left_t_m_t"
  5, 4, "t.l0.hex_cell_right_t_m_m"
  5, 5, "t.l0.hex_cell_left_t_m_m"
  6, 0, "t.l0.hex_cell_right_m_g_g"
  6, 1, "t.l0.hex_cell_left_m_g_g"
  6, 2, "t.l0.hex_cell_right_m_g_t"
  6, 3, "t.l0.hex_cell_left_m_g_t"
  6, 4, "t.l0.hex_cell_right_m_g_m"
  6, 5, "t.l0.hex_cell_left_m_g_m"
  7, 0, "t.l0.hex_cell_right_m_t_g"
  7, 1, "t.l0.hex_cell_left_m_t_g"
  7, 2, "t.l0.hex_cell_right_m_t_t"
  7, 3, "t.l0.hex_cell_left_m_t_t"
  7, 4, "t.l0.hex_cell_right_m_t_m"
  7, 5, "t.l0.hex_cell_left_m_t_m"
  8, 0, "t.l0.hex_cell_right_m_m_g"
  8, 1, "t.l0.hex_cell_left_m_m_g"
  8, 2, "t.l0.hex_cell_right_m_m_t"
  8, 3, "t.l0.hex_cell_left_m_m_t"
  8, 4, "t.l0.hex_cell_right_m_m_m"
  8, 5, "t.l0.hex_cell_left_m_m_m"
}
