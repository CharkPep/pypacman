import pygame
from .movement import MovementStrategy
from ...map.map import Map
from typing import Tuple
import math
from functools import cache


class PlayerMovement(MovementStrategy):
    _current_tile: Tuple[int, int] = None
    _map: Map = None

    def __init__(self, map: Map, entity: pygame.rect.Rect, current_tile: Tuple[int, int], TARGET_FPS = 60):
        self._map = map
        self._current_tile = current_tile
        self._rect = entity
        # 11 tiles per second
        self._velocity = 11 * self._map.get_tile(0, 0).get_rect().width / 60
        self._TARGET_FPS = TARGET_FPS

        self._direction = pygame.Vector2(0, 0)
        self._change_direction: pygame.Vector2 = self._direction

    def set_direction(self, direction: pygame.Vector2):
        # Can not really change speed if the entity is not in the middle of a tile
        self._change_direction = direction

    def get_direction(self) -> pygame.Vector2:
        # if self._change_direction is None:
        return self._direction
        # return self._change_direction


    @cache
    def _is_passable(self, tile: Tuple[int, int]) -> bool:
        tile = self._map.get_tile(tile[0], tile[1])
        if tile is None:
            return False
        return tile.passable()

    @cache
    def _is_intersection(self, tile: Tuple[int, int]):
        top = self._is_passable((tile[0], tile[1]))
        left = self._is_passable((tile[0], tile[1] - 1))
        right = self._is_passable((tile[0], tile[1] + 1))
        bottom = self._is_passable((tile[0] + 1, tile[1]))
        return top + left + right + bottom >= 2

    def _get_tile(self, tile: Tuple[int, int]):
        return self._map.get_tile(tile[0], tile[1])

    def get_current_position(self):
        return self._current_tile

    def _is_passable_in_direction(self, direction: pygame.Vector2):
        return self._is_passable((int(self._current_tile[0] + direction.y), int(self._current_tile[1] + direction.x)))

    def _check_if_target_reached(self):
        # Move from the current tile to the direction tile
        direction_tile = int(self._current_tile[0] + self._direction.y), int(self._current_tile[1] + self._direction.x)
        if math.dist(self._rect.center,
                     self._get_tile(direction_tile).get_rect().center) <= self._velocity:
            self._current_tile = direction_tile
            self._rect.center = self._get_tile(self._current_tile).get_rect().center
            return True
        return False

    def update(self):
        # Change movement direction
        self._check_if_target_reached()
        if self._is_intersection(self._current_tile) and self._change_direction != self._direction:
            # Check if change direction is possible
            if self._change_direction is not None and self._is_passable_in_direction(self._change_direction):
                self._direction = self._change_direction
                self._rect.center = self._get_tile(self._current_tile).get_rect().center
                self._change_direction = None

    def move(self, dt):
        if self._is_passable_in_direction(self._direction):
            self._rect.move_ip(self._direction * self._velocity)
