
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
gfx = "vectron/terrain/borders_v2/grassland_swamp_mountains"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 180
dy = 60
pixel_border = 1
tiles = { "row", "column", "tag"
  0, 0, "t.l0.hex_cell_right_g_g_g"
  0, 1, "t.l0.hex_cell_left_g_g_g"
  0, 2, "t.l0.hex_cell_right_g_g_s"
  0, 3, "t.l0.hex_cell_left_g_g_s"
  0, 4, "t.l0.hex_cell_right_g_g_m"
  0, 5, "t.l0.hex_cell_left_g_g_m"
  1, 0, "t.l0.hex_cell_right_g_s_g"
  1, 1, "t.l0.hex_cell_left_g_s_g"
  1, 2, "t.l0.hex_cell_right_g_s_s"
  1, 3, "t.l0.hex_cell_left_g_s_s"
  1, 4, "t.l0.hex_cell_right_g_s_m"
  1, 5, "t.l0.hex_cell_left_g_s_m"
  2, 0, "t.l0.hex_cell_right_g_m_g"
  2, 1, "t.l0.hex_cell_left_g_m_g"
  2, 2, "t.l0.hex_cell_right_g_m_s"
  2, 3, "t.l0.hex_cell_left_g_m_s"
  2, 4, "t.l0.hex_cell_right_g_m_m"
  2, 5, "t.l0.hex_cell_left_g_m_m"
  3, 0, "t.l0.hex_cell_right_s_g_g"
  3, 1, "t.l0.hex_cell_left_s_g_g"
  3, 2, "t.l0.hex_cell_right_s_g_s"
  3, 3, "t.l0.hex_cell_left_s_g_s"
  3, 4, "t.l0.hex_cell_right_s_g_m"
  3, 5, "t.l0.hex_cell_left_s_g_m"
  4, 0, "t.l0.hex_cell_right_s_s_g"
  4, 1, "t.l0.hex_cell_left_s_s_g"
  4, 2, "t.l0.hex_cell_right_s_s_s"
  4, 3, "t.l0.hex_cell_left_s_s_s"
  4, 4, "t.l0.hex_cell_right_s_s_m"
  4, 5, "t.l0.hex_cell_left_s_s_m"
  5, 0, "t.l0.hex_cell_right_s_m_g"
  5, 1, "t.l0.hex_cell_left_s_m_g"
  5, 2, "t.l0.hex_cell_right_s_m_s"
  5, 3, "t.l0.hex_cell_left_s_m_s"
  5, 4, "t.l0.hex_cell_right_s_m_m"
  5, 5, "t.l0.hex_cell_left_s_m_m"
  6, 0, "t.l0.hex_cell_right_m_g_g"
  6, 1, "t.l0.hex_cell_left_m_g_g"
  6, 2, "t.l0.hex_cell_right_m_g_s"
  6, 3, "t.l0.hex_cell_left_m_g_s"
  6, 4, "t.l0.hex_cell_right_m_g_m"
  6, 5, "t.l0.hex_cell_left_m_g_m"
  7, 0, "t.l0.hex_cell_right_m_s_g"
  7, 1, "t.l0.hex_cell_left_m_s_g"
  7, 2, "t.l0.hex_cell_right_m_s_s"
  7, 3, "t.l0.hex_cell_left_m_s_s"
  7, 4, "t.l0.hex_cell_right_m_s_m"
  7, 5, "t.l0.hex_cell_left_m_s_m"
  8, 0, "t.l0.hex_cell_right_m_m_g"
  8, 1, "t.l0.hex_cell_left_m_m_g"
  8, 2, "t.l0.hex_cell_right_m_m_s"
  8, 3, "t.l0.hex_cell_left_m_m_s"
  8, 4, "t.l0.hex_cell_right_m_m_m"
  8, 5, "t.l0.hex_cell_left_m_m_m"
}