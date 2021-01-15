from scene import Camera
from geometry import Vector2D
from scene import Map


def test_camera():
    c = Camera((2, 2))
    # c.fov()


def test_side_dist():
    map_ = Vector2D([2, 1])
    pos = Vector2D([2.38, 1.7])
    v_dir = Vector2D([1.1, 1.68])
    d_dist = v_dir.delta_dist()
    print(f"delta dist: {d_dist}")
    s_dist = v_dir.side_dist(pos, map_)
    print(f"side dist: {s_dist}")
    print(v_dir * s_dist)
    steps = v_dir.steps()
    print(pos + (v_dir * s_dist))


def test_wall_hit():
    map_ = {(3, 3): 1}

    map_pos = Vector2D([2, 1])
    pos = Vector2D([2.38, 1.7])

    v_dir = Vector2D([1.1, 1.68])
    d_dist_x, d_dist_y = v_dir.delta_dist()
    s_dist_x, s_dist_y = v_dir.side_dist(pos, map_pos)
    steps = v_dir.steps()

    path = []

    for i in range(4):
        if s_dist_x < s_dist_y:
            s_dist_x += d_dist_x
            map_pos[0] += steps[0]
            # side = 0
        else:
            s_dist_y += d_dist_y
            map_pos[1] += steps[1]
            # side = 1
        path.append([map_pos.x, map_pos.y])
        if map_.get(map_pos.as_tuple()) == 1:
            break

    assert path == [
        [2, 2], [3, 2], [3, 3]
    ], path
    print("Path found correctly")


def test_map():
    m = Map("maps/map_1.txt")
    assert m.at((0, 0)) == 1
    assert m.at((1, 1)) == 0


def unittests():
    test_camera()
    test_map()
    test_side_dist()
    test_wall_hit()


if __name__ == "__main__":
    unittests()
