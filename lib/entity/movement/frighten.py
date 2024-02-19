from .basic import BasicMovement
from typing_extensions import override
from .movement import MovementStrategy
from ...map.map import Map
from typing import Tuple
import random
import pygame


class FrightenedMovement(BasicMovement):
    def __init__(self, map: Map, entity: pygame.rect.Rect, current_tile: Tuple[int, int]):
        super().__init__(map, entity, current_tile)

    @override
    def _select_best_direction(self):
        movement_direction = self._direction
        if movement_direction == pygame.Vector2(0, 0):
            movement_direction = pygame.Vector2(0, -1)
        possible_directions = self._get_possible_directions(movement_direction)
        return possible_directions[random.randint(0, len(possible_directions) - 1)]