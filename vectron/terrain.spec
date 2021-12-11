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
  1,    0,  "t.l0.tundra1"
  1,    1,  "t.l0.arctic1"
  1,    2,  "t.l0.swamp1"
  2,    0,  "t.l0.lake1"
  2,    1,  "t.l0.coast1"
  2,    2,  "t.l0.floor1"

  ; Missing base terrain sprites
  ; Use transparent placeholders
  4,    2,  "t.l0.inaccessible1"

  ; Resources and other extras
  ; Use transparent placeholder
  3,    0,   "base.airstrip"
  3,    0,   "base.airbase"
  3,    0,   "base.buoy"
  3,    0,   "base.fortress"
  3,    0,   "base.outpost"
  3,    0,   "extra.ruins"
  3,    0,   "road.maglev"
  3,    0,   "road.pave"
  3,    0,   "road.rail"
  3,    0,   "road.road"
  3,    0,   "road.river"
  3,    0,   "ts.arctic_ivory"
  3,    0,   "ts.buffalo"
  3,    0,   "ts.coal"
  3,    0,   "ts.fish"
  3,    0,   "ts.fruit"
  3,    0,   "ts.furs"
  3,    0,   "ts.gems"
  3,    0,   "ts.gold"
  3,    0,   "ts.grassland_resources"
  3,    0,   "ts.horses"
  3,    0,   "ts.iron"
  3,    0,   "ts.oasis"
  3,    0,   "ts.oil"
  3,    0,   "ts.peat"
  3,    0,   "ts.pheasant"
  3,    0,   "ts.seals"
  3,    0,   "ts.silk"
  3,    0,   "ts.spice"
  3,    0,   "ts.tundra_game"
  3,    0,   "ts.whales"
  3,    0,   "ts.wheat"
  3,    0,   "ts.wine"
  3,    0,   "tx.irrigation"
  3,    0,   "tx.fallout"
  3,    0,   "tx.farmland"
  3,    0,   "tx.mine"
  3,    0,   "tx.oil_mine"
  3,    0,   "tx.oil_rig"
  3,    0,   "tx.pollution"
  3,    0,   "tx.village"

  ; Goto sprites
  3,    0,   "path.exhausted_mp"
  3,    0,   "path.normal"
  3,    0,   "path.step"
  3,    0,   "path.waypoint"

  ; Other required sprites
  3,    0,   "mask.tile"
  3,    0,   "t.dither_tile"
  3,    0,   "tx.darkness"
  3,    0,   "tx.fog"
  3,    0,   "user.attention"
}
