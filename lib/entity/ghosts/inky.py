from ..ghost import Ghost
from lib.map.map import GameMap
from ..entity import Entity
import pygame
import math
from typing_extensions import override
from typing import Union
from lib.enums.ghost_states import GhostStates


# Blue
class Inky(Ghost):
    COLOR = (0, 0, 255)
    _vector_to_blinky = None

    def __init__(self, position, player: Entity, blinky: Entity):
        super().__init__(position, 11, player)
        self._player = player
        self._state = GhostStates.CHASE
        self._target_tile: Union[pygame.Vector2, None] = None
        self._blinky = blinky
        self.SCATTER_TILE = pygame.Vector2(len(GameMap.get_instance().get_map()) - 1,
                                           len(GameMap.get_instance().get_map()[0]) - 1)

    def _calculate_distance_to_target_from_direction_vector(self, direction: pygame.Vector2):
        self._vector_to_blinky = [self._target_tile, self._blinky.get_position()]
        self._real_vector_to_blinky = self._vector_to_blinky[1] - self._vector_to_blinky[0]
        self._real_vector_to_blinky.rotate_ip(180)
        self._real_target = self._target_tile + self._real_vector_to_blinky
        return math.dist(GameMap.get_instance().get_tile(self._real_target).get_rect().center,
                         GameMap.get_instance().get_tile(self._position + direction).get_rect().center)

    def handle_event(self, event: pygame.event.Event):
        pass

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, self.COLOR, self.get_rect())
        if self._target_tile is not None:
            pygame.draw.circle(surface, self.COLOR,
                               GameMap.get_instance().get_tile(self._real_target).get_rect().center, 5)
        if self._vector_to_blinky is not None and self._state == GhostStates.CHASE:
            pygame.draw.line(surface, self.COLOR,
                             GameMap.get_instance().get_tile(self._vector_to_blinky[0]).get_rect().center,
                             GameMap.get_instance().get_tile(self._vector_to_blinky[1]).get_rect().center, 1)

    def set_state(self, state):
        self._state = state
        self._direction.rotate_ip(180)

    def _get_tile_in_front_of_player(self, tiles: int) -> pygame.Vector2:
        return self._player.get_position() + self._player.get_direction() * tiles

    def _get_tile_in_front_and_left_of_player(self, tiles: int):
        tile_in_front = self._get_tile_in_front_of_player(tiles)
        tile_in_front += self._player.get_direction().rotate(-90) * tiles
        return tile_in_front

    def _update_direction_SCATTER(self):
        self._target_tile = self.SCATTER_TILE
        self._direction = self._select_best_direction()

    @override
    def _update_direction_CHASE(self):
        self._target_tile = self._get_tile_in_front_of_player(2)
        if self._player.get_direction() == pygame.Vector2(0, -1):
            self._target_tile = self._get_tile_in_front_and_left_of_player(2)
        self._direction = self._select_best_direction()
