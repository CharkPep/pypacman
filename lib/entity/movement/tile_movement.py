import pygame
from .strategy import MovementStrategy
from ...map.map import Map
from typing import Tuple
import math


class TileBasedMovement(MovementStrategy):
    __target_tile: Tuple[int, int] = None
    __current_tile: Tuple[int, int] = None
    __map: Map = None

    def __init__(self, map: Map, entity: pygame.rect.Rect, current_tile: Tuple[int, int], TARGET_FPS = 60):
        self.__map = map
        self.__current_tile = current_tile
        # self.__target_tile = current_tile
        self.__rect = entity
        # 11 tiles per second
        self._velocity = 11 * self.__map.get_tile(0, 0).get_rect().width / 60
        self.TARGET_FPS = TARGET_FPS
        self._direction = pygame.Vector2(0, 0)
        self._change_direction_target = self._direction

    def set_speed(self, direction: pygame.Vector2):
        # Can not really change speed if the entity is not in the middle of a tile
        self._change_direction_target = direction

    def get_speed(self) -> pygame.Vector2:
        if self._change_direction_target is None:
            return self._direction
        return self._change_direction_target

    def _is_passable(self, tile: Tuple[int, int]) -> bool:
        tile = self.__map.get_tile(tile[0], tile[1])
        if tile is None:
            return False
        return tile.passable()

    def _is_intersection(self, tile: Tuple[int, int]):
        top = self._is_passable((tile[0], tile[1]))
        left = self._is_passable((tile[0], tile[1] - 1))
        right = self._is_passable((tile[0], tile[1] + 1))
        bottom = self._is_passable((tile[0] + 1, tile[1]))
        return top + left + right + bottom > 2

    def _get_tile(self, tile: Tuple[int, int]):
        return self.__map.get_tile(tile[0], tile[1])

    def get_current_position(self):
        return self.__current_tile

    def move(self, dt):
        direction_tile = int(self.__current_tile[0] + self._direction.y), int(self.__current_tile[1] + self._direction.x)
        change_direction_tile = None

        if self._change_direction_target is not None:
            change_direction_tile = int(self.__current_tile[0] + self._change_direction_target.y), int(self.__current_tile[1] + self._change_direction_target.x)
        if change_direction_tile is not None and change_direction_tile != direction_tile:
            if self._is_passable(change_direction_tile) and self._is_intersection(self.__current_tile):
                direction_tile = change_direction_tile
                self._direction = self._change_direction_target
                self.__rect.center = self._get_tile(self.__current_tile).get_rect().center
            if self._is_passable(change_direction_tile) and self._direction == pygame.Vector2(0, 0):
                self.__rect.center = self._get_tile(self.__current_tile).get_rect().center
                self._direction = self._change_direction_target
        if not self._is_passable(direction_tile):
            self.__rect.center = self._get_tile(self.__current_tile).get_rect().center
            self._direction = pygame.Vector2(0, 0)

        if math.dist(self.__rect.center,
                     self._get_tile(direction_tile).get_rect().center) <= self._velocity:
            self.__current_tile = direction_tile

        self.__rect.move_ip(self._direction * self._velocity * dt * self.TARGET_FPS)
