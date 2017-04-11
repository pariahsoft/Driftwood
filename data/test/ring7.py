def kill_door():
    Driftwood.script.call("libs/stdlib/viewport.py", "end_rumble")
    Driftwood.tick.register(kill_door_callback1, once=True, delay=1.0)
    Driftwood.tick.register(kill_door_callback2, once=True, delay=2.0)
    Driftwood.tick.register(kill_door_callback3, once=True, delay=3.0)


def kill_door_callback1(seconds_past):
    Driftwood.area.tilemap.layers[1].tiles[51].localgid = 18
    Driftwood.area.tilemap.layers[1].tiles[51].gid = 18
    Driftwood.area.tilemap.layers[1].tiles[51].members = [17]
    Driftwood.area.changed = True


def kill_door_callback2(seconds_past):
    Driftwood.area.tilemap.layers[1].tiles[51].localgid = 19
    Driftwood.area.tilemap.layers[1].tiles[51].gid = 19
    Driftwood.area.tilemap.layers[1].tiles[51].members = [18]
    Driftwood.area.changed = True


def kill_door_callback3(seconds_past):
    Driftwood.area.tilemap.layers[1].tiles[51].localgid = 20
    Driftwood.area.tilemap.layers[1].tiles[51].gid = 20
    Driftwood.area.tilemap.layers[1].tiles[51].members = [19]
    Driftwood.area.changed = True

