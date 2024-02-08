from typing import List, Union

import pygame.surface

from .tile import Tile


class Map:
    def __init__(self, map: List[List[Tile]]):
        self.map = map

    def render(self, surface : pygame.surface.Surface):
        for layer in self.map:
            for tile in layer:
                if tile is not None:
                    tile.render(surface)

    def get_map(self):
        return self.map
