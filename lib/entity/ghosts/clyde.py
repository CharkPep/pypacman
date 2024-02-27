from lib.map.map import GameMap
from lib.entity.ghost import Ghost
from lib.enums.ghost_states import GhostStates
from lib.entity.entity import Entity
from typing_extensions import override
import math, random, pygame


# Yellow
class Clyde(Ghost):
    COLOR = (255, 255, 0)

    def __init__(self, position, player: Entity):
        super().__init__(position, 11, player)
        self._player = player
        self._state = GhostStates.IDLE
        self._target_tile = None
        self.SCATTER_TILE = pygame.Vector2(0, len(GameMap.get_instance().get_map()))

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
        if self._state == GhostStates.CHASE and math.dist(self._player.get_position(), self._position) > 8:
            pygame.draw.circle(surface, self.COLOR,
                               GameMap.get_instance().get_tile(self._position).get_rect().center,
                               8 * GameMap.get_instance().get_tile_size()[0], width=1)

    def _update_direction_SCATTER(self):
        self._target_tile = self.SCATTER_TILE
        self.set_direction(self._select_best_direction())

    @override
    def _update_direction_CHASE(self):
        self._target_tile = self._player.get_position()
        if math.dist(self._player.get_position(), self._position) <= 8:
            self._target_tile = self.SCATTER_TILE
        self.set_direction(self._select_best_direction())
