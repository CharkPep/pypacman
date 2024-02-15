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
        self.__target_tile = self._current_tile

    def __get_possible_directions(self, movement_direction: pygame.Vector2):
        left = movement_direction.rotate(90)
        right = movement_direction.rotate(-90)
        straight = movement_direction
        if movement_direction == pygame.Vector2(0, 0):
            left = pygame.Vector2(0, -1).rotate(90)
            right = pygame.Vector2(0, -1).rotate(-90)
            straight = pygame.Vector2(0, -1)
        possible_directions = []
        if self._map.get_tile(int(self._current_tile[0] + straight.y), int(self._current_tile[1] + straight.x)).passable():
            possible_directions.append(straight)
        if self._map.get_tile(int(self._current_tile[0] + right.y), int(self._current_tile[1] + right.x)).passable():
            possible_directions.append(right)
        if self._map.get_tile(int(self._current_tile[0] + left.y), int(self._current_tile[1] + left.x)).passable():
            possible_directions.append(left)
        return possible_directions

    def _calculate_distance_to_target_from_direction_vector(self, direction: pygame.Vector2):
        target = self._map.get_tile_from_tuple(self.states.get_current_state().get_target())
        tile = self._map.get_tile_from_tuple((int(self._current_tile[0] + direction[1]), int(self._current_tile[1] + direction[0])))
        return math.dist(target.get_rect().center, tile.get_rect().center)

    def _select_best_direction(self):
        movement_direction = self._direction
        if movement_direction == pygame.Vector2(0, 0):
            movement_direction = pygame.Vector2(0, -1)
        possible_directions = self.__get_possible_directions(movement_direction)
        distance_to_target = self._calculate_distance_to_target_from_direction_vector(self._direction)
        new_direction = None
        if new_direction is None and len(possible_directions) > 0:
            new_direction = possible_directions[0]
        if new_direction is None:
            new_direction = -movement_direction
        for direction in possible_directions:
            distance = self._calculate_distance_to_target_from_direction_vector(direction)
            if distance <= distance_to_target:
                new_direction = direction
                distance_to_target = distance
        return new_direction

    @override
    def update(self):
        if self._check_if_target_reached():
            self._direction = self._select_best_direction()
