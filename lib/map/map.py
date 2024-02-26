from typing import List, Union, Tuple, Dict

import pygame.surface
from .tile import Tile


class GameMap:
    _map: List[List[Tile]] = None
    __score = []
    __boosts = []
    _size = None
    _instance = None

    @classmethod
    def get_instance(cls, *args) -> 'GameMap':
        if cls._instance is None:
            cls._instance = cls(*args)
        return cls._instance

    def get_size(self):
        return self._size

    def is_intersection(self, tile: Tuple[int, int]):
        top = self.is_passable((tile[0], tile[1]))
        left = self.is_passable((tile[0], tile[1] - 1))
        right = self.is_passable((tile[0], tile[1] + 1))
        bottom = self.is_passable((tile[0] + 1, tile[1]))
        return top + left + right + bottom >= 2

    def is_passable(self, tile: Tuple[int, int]) -> bool:
        tile = self.get_tile_from_tuple(tile)
        if tile is None:
            return False
        return tile.passable()

    def get_tile_size(self):
        return self._size

    def __init__(self, map: List[List[Tile]]):
        self._map = map
        self._size = (map[0][0].get_rect().width, map[0][0].get_rect().height)

    def render(self, surface: pygame.surface.Surface):
        surface.fill((0, 0, 0))
        for layer in self._map:
            for tile in layer:
                if tile is not None:
                    tile.render(surface)

    def get_map(self) -> List[List[Tile]]:
        return self._map

    def get_tile_from_tuple(self, pos: Tuple[int, int]):
        if pos[0] < 0 or pos[0] >= len(self._map) or pos[1] < 0 or pos[1] >= len(self._map[0]):
            return None
        return self._map[pos[0]][pos[1]]

    def get_tile(self, x: int, y: int) -> Union[Tile, None]:
        if x < 0 or x >= len(self._map) or y < 0 or y >= len(self._map[0]):
            return None
        return self._map[x][y]
