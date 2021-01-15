import logging
import numpy as np

from geometry import Vector2D


class Map:
    def __init__(self, map_path: str):
        """
        Create a game map, with walls and stuff.
        map_path: str ; A filepath to a map_*.txt that contains a 'bitmap' readable by numpy
        """
        self._map = np.loadtxt(map_path)

    def at(self, pos):
        # try:
        #     cell_value = self._map[pos.as_tuple()]
        # except Exception:
        #     logging.exception("Cell value not acessible")
        #     return 0
        # return cell_value
        if isinstance(pos, (tuple, list)):
            return self._map[pos]
        return self._map[pos.as_tuple()]
