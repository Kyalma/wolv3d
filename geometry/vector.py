import numpy as np
from typing import Union


class Vector2D:
    # def __init__(self, vx: float = 0, vy: float = 0) -> None:
    #     self._v = np.array((vx, vy))

    def __init__(self, array: np.array) -> None:
        if isinstance(array, (tuple, list)):
            self._v = np.array(array)
        else:
            self._v = array

    @property
    def x(self):
        return self._v[0]

    @property
    def y(self):
        return self._v[1]

    def as_tuple(self):
        return tuple(self._v)

    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, value):
        self._v[index] = value

    def __repr__(self):
        return repr(self._v)

    def __add__(self, other):
        return Vector2D(self._v + other._v)

    def __sub__(self, other):
        return Vector2D(self._v + other._v)

    def __mul__(self, other):
        if isinstance(other, (int, float, np.ndarray)):
            return Vector2D(self._v * other)
        return Vector2D(self._v * other._v)

    __rmul__ = __mul__

    def rotate_90(self):
        self.rotate(90, inplace=True)

    def rotate(self, angle: int, *, inplace: bool = False):
        t = np.radians(angle)
        r = np.array((
            (np.cos(t), -np.sin(t)),
            (np.sin(t), np.cos(t))
        ))
        rotated = r.dot(self._v)
        # print("Rotated vector: {}".format(rotated))
        if inplace:
            self._v = rotated
            return self
        return Vector2D(rotated)

    def delta_dist(self):
        """
        delta_dist_x and delta_dist_y are the distance the ray has to travel to go from 1 x-side to the next x-side, likewise for y.
        those are *ratio* of the current vector
        """
        if self._v[0] == 0 or self._v[1] == 0:
            delta_dist_x = (0 if self._v[1] == 0 else (1 if self._v[0] == 0 else abs(1 / self._v[0])))
            delta_dist_y = (0 if self._v[0] == 0 else (1 if self._v[1] == 0 else abs(1 / self._v[1])))
            # return np.array([delta_dist_x, delta_dist_y])
            return delta_dist_x, delta_dist_y
        # return np.absolute(1 / self._v)
        return tuple(np.absolute(1 / self._v))

    def steps(self):
        step_x = -1 if self._v[0] < 0 else 1
        step_y = -1 if self._v[1] < 0 else 1
        return step_x, step_y

    def side_dist(self, pos, map):
        """
        side_dist_x is the distance from the current position to the next x-side, likewise for y.
        those are *ratio* of the current vector
        """
        step_x, step_y = self.steps()
        delta_dist_x, delta_dist_y = self.delta_dist()
        side_dist_x = (pos.x - map.x) * delta_dist_x if step_x == -1 else (map.x + 1 - pos.x) * delta_dist_x
        side_dist_y = (pos.y - map.y) * delta_dist_y if step_y == -1 else (map.y + 1 - pos.y) * delta_dist_y
        # return np.array([side_dist_x, side_dist_y])
        return side_dist_x, side_dist_y


if __name__ == "__main__":
    v = Vector2D((1, 0))
    r = v.rotate(90)
    print(v + r)
