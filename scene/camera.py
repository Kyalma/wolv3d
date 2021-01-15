import numpy as np
from typing import Iterator

from geometry import Vector2D
from graphics import DISPLAY_SIZE


class Camera:
    def __init__(self, pos):
        self.pos = Vector2D(pos)
        self.dir = Vector2D((0.1, 1))
        # self.fov_factor = 1

    def camera_plane(self):
        return self.dir.rotate(90)

    # def fov(self):
    #     plane = self.camera_plane() * self.fov_factor
    #     first = self.pos + self.dir - plane
    #     last = self.pos + self.dir + plane
    #     print("Pos={}, FOV is {} to {}".format(self.pos, first, last))

    def raycasting_vectors(self) -> Iterator[Vector2D]:
        """
        Yield raycasting vectors used to render each pixel column of the display surface.
        This is our window of shape (640, 320)
            640
        *-------------*
        |             |  320
        |             |
        *-------------*
        For each 640 pixel of "width", the function will yield one vector
        The vector is annoted ( ray_dist_x, ray_dist_y )
        and is used for the DDA (or Digital Differential Analysis) algorithm
        """
        plane = self.camera_plane()
        for plane_factor in np.linspace(-1, 1, num=DISPLAY_SIZE[0]):
            yield self.dir + plane * plane_factor

    def calculate_vector_wall_hit(self, ray_vector: Vector2D, map):
        side = 0
        map_pos = Vector2D([int(self.pos.x), int(self.pos.y)])
        delta_dist_x, delta_dist_y = ray_vector.delta_dist()
        side_dist_x, side_dist_y = ray_vector.side_dist(self.pos, map_pos)
        step_x, step_y = ray_vector.steps()

        side = 0
        found = 0
        while found == 0:
            if side_dist_x < side_dist_y:
                side_dist_x += delta_dist_x
                map_pos[0] += step_x
                side = 0
            else:
                side_dist_y += delta_dist_y
                map_pos[1] += step_y
                side = 1
            found = map.at(map_pos)

        perp_wall_dist = (
            (map_pos.x - self.pos.x + (1 - step_x) / 2) / ray_vector.x
            if side == 0 else
            (map_pos.y - self.pos.y + (1 - step_y) / 2) / ray_vector.y
        )
        return side, found, perp_wall_dist


if __name__ == "__main__":
    c = Camera((2, 2))
    # c.fov()
