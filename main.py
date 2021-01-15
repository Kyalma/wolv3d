import argparse
import pygame
import logging
from pygame.locals import *
import time
import sys

from scene.map import Map
from entities import Player
from graphics import to_pixel_repr
from graphics import DISPLAY_SIZE


def main(args):
    pygame.init()
    pygame.font.init()

    pygame.display.init()
    display = pygame.display.set_mode(size=DISPLAY_SIZE, flags=pygame.DOUBLEBUF)
    pygame.display.set_caption("Wolv3D")

    surface = pygame.display.get_surface()

    gmap = Map("maps/map_1.txt")
    player = Player((2.2, 1.4))

    running = 1 if not args.stop_after else args.stop_after
    while running > 0:
        try:
            frame_start = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.dir.rotate(-10, inplace=True)
                    elif event.key == pygame.K_RIGHT:
                        player.dir.rotate(10, inplace=True)
                    elif event.key == pygame.K_UP:
                        player.pos += player.dir
                else:
                    logging.debug("Got event: %s", event)
            time.sleep(.1)
            raycasting = player.see(gmap)
            surface.fill((0, 0, 0))
            for line in to_pixel_repr(raycasting):
                pygame.draw.line(surface, *line, width=1)
            pygame.display.flip()

            frame_end = time.time()
            logging.debug("Frame took %fs", frame_end - frame_start)
            if args.stop_after:
                running -= 1

        except KeyboardInterrupt:
            logging.debug("Interrupted by user")
            running = 0

    pygame.display.quit()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    # parser.add_argument('--perf', action='store_true', help='enable vmprof profiling')
    parser.add_argument('--stop-after',
                        type=int, metavar='N',
                        help='stop the execution after N generated frames, useful for profiling a fix set of frames'
    )
    args = parser.parse_args()
    main(args)
    sys.exit(0)
