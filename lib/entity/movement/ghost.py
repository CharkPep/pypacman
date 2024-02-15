import math

from .player import PlayerMovement
from ..state.state import EntityState
from ...map.map import Map
import pygame
from typing import Tuple, Union
from typing_extensions import override
from ..state.manager import StateManager


class GhostMovement(PlayerMovement):

    def __init__(self, current_state: StateManager, map: Map, entity: pygame.rect.Rect, current_tile: Tuple[int, int]):
        super().__init__(map, entity, current_tile)
        self.states = current_state
        self.set_direction(-pygame.Vector2(0, 1))

    def __get_direction(self):
        # 0B1000 - ENTITY IS NOT MOVING
        # 0B0001 - CURRENT DIRECTION
        # 0B0010 - RIGHT OF THE CURRENT DIRECTION
        # 0B0100 - LEFT OF THE CURRENT DIRECTION
        possible_directions = 0b0000
        if self._direction == pygame.Vector2(0, 0):
            return 0b1000
        left = self._direction.rotate(90)
        right = self._direction.rotate(-90)
        straight = self._direction
        if self._map.get_tile(int(self._current_tile[0] + straight.y), int(self._current_tile[1] + straight.x)).passable():
            possible_directions |= 0b001
        if self._map.get_tile(int(self._current_tile[0] + right.y), int(self._current_tile[1] + right.x)).passable():
            possible_directions |= 0b010
        if self._map.get_tile(int(self._current_tile[0] + left.y), int(self._current_tile[1] + left.x)).passable():
            possible_directions |= 0b100
        return possible_directions

    def _calculate_distance_to_target_from_direction_vector(self, direction: pygame.Vector2):
        target = self.states.get_current_state().get_target().get_current_position()
        tile = self.get_current_position() + direction
        return math.dist(target, tile)

    @override
    def move(self, dt: float):
        possible_directions = self.__get_direction()
        print(self._direction)
        print("{0:b}".format(possible_directions))
        if possible_directions == 0b0001:
            super().move(dt)
            return
        super().move(dt)
