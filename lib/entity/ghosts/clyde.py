from ..ghost import Ghost
from lib.map.map import GameMap
from ..entity import Entity
import pygame
import math
from typing_extensions import override
from lib.enums.ghost_states import GhostStates


class Clyde(Ghost):

    def __init__(self, position, player: Entity):
        super().__init__(position, 11)
        self._player = player
        self._state = GhostStates.IDLE
        self._target_tile = None

    def _calculate_distance_to_target_from_direction_vector(self, direction: pygame.Vector2):
        tile = GameMap.get_instance().get_tile_from_tuple(
            (int(self._position[0] + direction.y), int(self._position[1] + direction.x)))
        return math.dist(self._player.get_rect().center,
                         tile.get_rect().center)

    def handle_event(self, event: pygame.event.Event):
        pass

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 255, 0), self.get_rect())

    def set_state(self, state):
        pass

    @override
    def _update_direction(self):
        if self._state == GhostStates.IDLE:
            self._direction = pygame.Vector2(0, 0)
        if self._check_if_target_reached() and self._state == GhostStates.CHASE:
            self._direction = self._select_best_direction()
