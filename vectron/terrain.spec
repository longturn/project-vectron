[spec]

; Client capabilities supported by this file
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]
artists = "
    louis94 (spec files)
    TriClad (visuals)
"

[file]
gfx = "vectron/terrain"

[grid_main]
x_top_left = 1
y_top_left = 1
dx = 360
dy = 120
pixel_border = 1

tiles = { "row", "column","tag"
  ; Base terrain sprites
  0,    0,  "t.l0.desert1"
  0,    1,  "t.l0.plains1"
  0,    1,  "t.l0.hills1"
  0,    1,  "t.l0.mountains1"
  0,    2,  "t.l0.grassland1"
  0,    2,  "t.l0.jungle1"
  0,    2,  "t.l0.forest1"
  0,    3,  "t.l0.tundra1"
  0,    4,  "t.l0.arctic1"
  0,    5,  "t.l0.swamp1"
  0,    6,  "t.l0.lake1"
  0,    7,  "t.l0.coast1"
  0,    8,  "t.l0.floor1"

  ; Missing base terrain sprites
  ; Use transparent placeholders
  1,    0,  "t.l0.inaccessible1"

  ; Resources and other extras
  ; Use transparent placeholder
  1,    0,   "base.airstrip"
  1,    0,   "base.airbase"
  1,    0,   "base.buoy"
  1,    0,   "base.fortress"
  1,    0,   "base.outpost"
  1,    0,   "extra.ruins"
  1,    0,   "road.maglev"
  1,    0,   "road.pave"
  1,    0,   "road.rail"
  1,    0,   "road.road"
  1,    0,   "road.river"
  1,    0,   "ts.arctic_ivory"
  1,    0,   "ts.buffalo"
  1,    0,   "ts.coal"
  1,    0,   "ts.fish"
  1,    0,   "ts.fruit"
  1,    0,   "ts.furs"
  1,    0,   "ts.gems"
  1,    0,   "ts.gold"
  1,    0,   "ts.grassland_resources"
  1,    0,   "ts.horses"
  1,    0,   "ts.iron"
  1,    0,   "ts.oasis"
  1,    0,   "ts.oil"
  1,    0,   "ts.peat"
  1,    0,   "ts.pheasant"
  1,    0,   "ts.seals"
  1,    0,   "ts.silk"
  1,    0,   "ts.spice"
  1,    0,   "ts.tundra_game"
  1,    0,   "ts.whales"
  1,    0,   "ts.wheat"
  1,    0,   "ts.wine"
  1,    0,   "tx.irrigation"
  1,    0,   "tx.fallout"
  1,    0,   "tx.farmland"
  1,    0,   "tx.mine"
  1,    0,   "tx.oil_mine"
  1,    0,   "tx.oil_rig"
  1,    0,   "tx.pollution"
  1,    0,   "tx.village"

  ; Goto sprites
  1,    0,   "path.exhausted_mp"
  1,    0,   "path.normal"
  1,    0,   "path.step"
  1,    0,   "path.waypoint"

  ; Other required sprites
  1,    0,   "mask.tile"
  1,    0,   "t.dither_tile"
  1,    0,   "tx.darkness"
  1,    0,   "tx.fog"
  1,    0,   "user.attention"
}
