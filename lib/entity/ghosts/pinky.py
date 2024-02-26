from lib.entity.ghost import Ghost
from lib.map.map import GameMap
from lib.enums.ghost_states import GhostStates
from lib.entity.entity import Entity
import math
import pygame
from typing_extensions import override


# Pink
class Pinky(Ghost):
    SCATTER_TILE = (0, 0)
    COLOR = (255, 192, 203)

    def __init__(self, position, player: Entity):
        super().__init__(position, 11, player)
        self._player = player
        self._state = GhostStates.CHASE
        self._target_tile = None
        self.SCATTER_TILE = pygame.Vector2(1, 1)

    def _calculate_distance_to_target_from_direction_vector(self, direction: pygame.Vector2):
        tile = GameMap.get_instance().get_tile(self._position + direction)
        return math.dist(GameMap.get_instance().get_tile(self._target_tile).get_rect().center,
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
        self._target_tile = self._get_tile_in_front_of_player(4)
        if self._player.get_direction() == pygame.Vector2(0, -1):
            self._target_tile = self._get_tile_in_front_and_left_of_player(4)
        self._direction = self._select_best_direction()
