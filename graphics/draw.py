from .constants import DISPLAY_SIZE
from pygame import Color

LIME = 0x00FF00
DARK_LIME = 0x007F80

RED = 0xFF0000
DARK_RED = 0x8B0000

WALL_COLORS = {
    1: (LIME, DARK_LIME),
    2: (RED, DARK_RED),
}


def to_pixel_repr(raycasting_result: list):
    for x, (side, cell_value, wall_dist) in enumerate(raycasting_result):
        color = WALL_COLORS[cell_value][side]

        wall_height = DISPLAY_SIZE[1] / wall_dist
        draw_start = DISPLAY_SIZE[1] / 2 - wall_height / 2
        draw_end = DISPLAY_SIZE[1] / 2 + wall_height / 2

        start_pos = (x, draw_start if draw_start > 0 else 0)
        end_pod = (x, draw_end if draw_end < DISPLAY_SIZE[1] else DISPLAY_SIZE[1])
        yield (color, start_pos, end_pod)
