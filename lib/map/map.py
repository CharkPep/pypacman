from typing import List, Union, Tuple, Dict
from lib.map.tile import OneWay
import pygame.surface
from .tile import Tile


class GameMap:
    _map: List[List[Tile]] = None
    _instance = None

    @classmethod
    def get_instance(cls, *args, **kwargs) -> 'GameMap':
        if cls._instance is None:
            cls._instance = cls(*args, **kwargs)
        return cls._instance

    def is_intersection(self, tile: pygame.Vector2):
        top = self.is_passable(tile)
        left = self.is_passable(pygame.Vector2(tile[0] - 1, tile[1]))
        right = self.is_passable(pygame.Vector2(tile[0] + 1, tile[1]))
        bottom = self.is_passable(pygame.Vector2(tile[0], tile[1] + 1))
        return top + left + right + bottom >= 2

    def is_passable(self, tile: pygame.Vector2) -> bool:
        tile = self.get_tile(tile)
        if tile is None:
            return False
        return tile.passable()

    def get_tile_size(self):
        return self._map[0][0].get_rect().width, self._map[0][0].get_rect().height

    def __init__(self, tiles: List[List[Tile]],
                 background: pygame.image = None, **metadate):
        self._map = tiles
        self._background = background
        self._metadate = metadate

    def get_metadate(self):
        return self._metadate

    def render(self, surface: pygame.surface.Surface):
        if self._background is not None:
            surface.blit(self._background, (0, 0))
        else:
            surface.fill((0, 0, 0))
        for layer in self._map:
            for tile in layer:
                tile.render(surface)

    def get_map(self) -> List[List[Tile]]:
        return self._map

    def clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))

    def clamp_position(self, position: pygame.Vector2):
        return pygame.Vector2(self.clamp(position.x, 0, len(self._map[0]) - 1),
                              self.clamp(position.y, 0, len(self._map) - 1))

    def get_tile(self, position: pygame.Vector2) -> Tile:
        if position.y < 0 or position.y >= len(self._map) or position.x < 0 or position.x >= len(self._map[0]):
            position = self.clamp_position(position)
            return self._map[int(position.y)][int(position.x)]
        return self._map[int(position.y)][int(position.x)]
