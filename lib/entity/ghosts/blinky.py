from ..ghost import Ghost
from lib.map.map import GameMap
from ..entity import Entity
import pygame
import math
import random
from typing_extensions import override
from lib.enums.ghost_states import GhostStates


# Red
class Blinky(Ghost):
    COLOR = (255, 0, 0)

    def __init__(self, position, player: Entity):
        super().__init__(position, 11, player)
        self._state = GhostStates.IDLE
        self.SCATTER_TILE = pygame.Vector2(len(GameMap.get_instance().get_map()[0]) - 1, 0)

    def _calculate_distance_to_target_from_direction_vector(self, direction: pygame.Vector2):
        tile = GameMap.get_instance().get_tile(self._position + direction)
        return math.dist(GameMap.get_instance().get_tile(self._target.get_position()).get_rect().center,
                         tile.get_rect().center)

    def handle_event(self, event: pygame.event.Event):
        pass

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, self.COLOR, self.get_rect())
        if self._target_tile is not None:
            pygame.draw.circle(surface, self.COLOR,
                               GameMap.get_instance().get_tile(self._target_tile).get_rect().center, 5)

    def set_state(self, state):
        self._state = state
        self._direction.rotate_ip(180)

    def _update_direction_SCATTER(self):
        self._target_tile = self.SCATTER_TILE
        self._direction = self._select_best_direction()
