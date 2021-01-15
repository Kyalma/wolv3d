from typing import Iterable
import logging

from geometry import Vector2D
from scene import Camera


class Player(Camera):
    # A player is basically a camera with legs
    # Now I cannot sleep

    def __init__(self, pos) -> None:
        Camera.__init__(self, pos)

    # def set_position(self, new_pos) -> None:
    #     self.pos = Vector2D(new_pos)

    def see(self, map):
        """
        Return a flat list of distance to the closest wall for each pixel in
        the x axis of the display surface.
        The player does not know what to see, so it needs to be given a map.
        """
        # logging.debug("straight ahead, I see %s", self.pos + self.dir)
        raycasting_results = []
        for ray_vector in self.raycasting_vectors():
            res = self.calculate_vector_wall_hit(ray_vector, map)
            raycasting_results.append(res)
        return raycasting_results
