[spec]

; Client capabilities supported by this file
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]
artists = "
    louis94 (spec files)
    TriClad (visuals)
"

[file]
gfx = "vectron/units/foot_units"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 360
dy = 180
pixel_border = 1

tiles = { "row", "column","tag"
  ; Units
  0,    0,   "u.settlers_se"
  0,    1,   "u.settlers_s"
  0,    2,   "u.settlers_w"
  0,    3,   "u.settlers_nw"
  0,    4,   "u.settlers_n"
  0,    5,   "u.settlers_e"

  0,    0,   "u.warriors_se"
  0,    1,   "u.warriors_s"
  0,    2,   "u.warriors_w"
  0,    3,   "u.warriors_nw"
  0,    4,   "u.warriors_n"
  0,    5,   "u.warriors_e"

  0,    0,   "u.explorer_se"
  0,    1,   "u.explorer_s"
  0,    2,   "u.explorer_w"
  0,    3,   "u.explorer_nw"
  0,    4,   "u.explorer_n"
  0,    5,   "u.explorer_e"

  0,    0,   "u.worker_se"
  0,    1,   "u.worker_s"
  0,    2,   "u.worker_w"
  0,    3,   "u.worker_nw"
  0,    4,   "u.worker_n"
  0,    5,   "u.worker_e"

  0,    0,   "u.phalanx_se"
  0,    1,   "u.phalanx_s"
  0,    2,   "u.phalanx_w"
  0,    3,   "u.phalanx_nw"
  0,    4,   "u.phalanx_n"
  0,    5,   "u.phalanx_e"

  0,    0,   "u.legion_se"
  0,    1,   "u.legion_s"
  0,    2,   "u.legion_w"
  0,    3,   "u.legion_nw"
  0,    4,   "u.legion_n"
  0,    5,   "u.legion_e"

  0,    0,   "u.diplomat_se"
  0,    1,   "u.diplomat_s"
  0,    2,   "u.diplomat_w"
  0,    3,   "u.diplomat_nw"
  0,    4,   "u.diplomat_n"
  0,    5,   "u.diplomat_e"

  0,    0,   "u.pikemen_se"
  0,    1,   "u.pikemen_s"
  0,    2,   "u.pikemen_w"
  0,    3,   "u.pikemen_nw"
  0,    4,   "u.pikemen_n"
  0,    5,   "u.pikemen_e"

  0,    0,   "u.musketeers_se"
  0,    1,   "u.musketeers_s"
  0,    2,   "u.musketeers_w"
  0,    3,   "u.musketeers_nw"
  0,    4,   "u.musketeers_n"
  0,    5,   "u.musketeers_e"

  0,    0,   "u.engineers_se"
  0,    1,   "u.engineers_s"
  0,    2,   "u.engineers_w"
  0,    3,   "u.engineers_nw"
  0,    4,   "u.engineers_n"
  0,    5,   "u.engineers_e"

  0,    0,   "u.riflemen_se"
  0,    1,   "u.riflemen_s"
  0,    2,   "u.riflemen_w"
  0,    3,   "u.riflemen_nw"
  0,    4,   "u.riflemen_n"
  0,    5,   "u.riflemen_e"

  0,    0,   "u.alpine_troops_s"
  0,    1,   "u.alpine_troops_sw"
  0,    2,   "u.alpine_troops_nw"
  0,    3,   "u.alpine_troops_n"
  0,    4,   "u.alpine_troops_ne"
  0,    5,   "u.alpine_troops_se"

  0,    0,   "u.spy_se"
  0,    1,   "u.spy_s"
  0,    2,   "u.spy_w"
  0,    3,   "u.spy_nw"
  0,    4,   "u.spy_n"
  0,    5,   "u.spy_e"

  0,    0,   "u.marines_se"
  0,    1,   "u.marines_s"
  0,    2,   "u.marines_w"
  0,    3,   "u.marines_nw"
  0,    4,   "u.marines_n"
  0,    5,   "u.marines_e"

  0,    0,   "u.partisan_se"
  0,    1,   "u.partisan_s"
  0,    2,   "u.partisan_w"
  0,    3,   "u.partisan_nw"
  0,    4,   "u.partisan_n"
  0,    5,   "u.partisan_e"

  0,    0,   "u.paratroopers_se"
  0,    1,   "u.paratroopers_s"
  0,    2,   "u.paratroopers_w"
  0,    3,   "u.paratroopers_nw"
  0,    4,   "u.paratroopers_n"
  0,    5,   "u.paratroopers_e"

  0,    0,   "u.leader_se"
  0,    1,   "u.leader_s"
  0,    2,   "u.leader_w"
  0,    3,   "u.leader_nw"
  0,    4,   "u.leader_n"
  0,    5,   "u.leader_e"

  0,    0,   "u.barbarian_leader_s"
  0,    1,   "u.barbarian_leader_sw"
  0,    2,   "u.barbarian_leader_nw"
  0,    3,   "u.barbarian_leader_n"
  0,    4,   "u.barbarian_leader_ne"
  0,    5,   "u.barbarian_leader_se"

  0,    0,   "u.fanatics_se"
  0,    1,   "u.fanatics_s"
  0,    2,   "u.fanatics_w"
  0,    3,   "u.fanatics_nw"
  0,    4,   "u.fanatics_n"
  0,    5,   "u.fanatics_e"

  0,    0,   "u.migrants_se"
  0,    1,   "u.migrants_s"
  0,    2,   "u.migrants_w"
  0,    3,   "u.migrants_nw"
  0,    4,   "u.migrants_n"
  0,    5,   "u.migrants_e"
}
