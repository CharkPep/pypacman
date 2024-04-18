from lib.map.map import GameMap
from lib.entity.ghost import Ghost
from lib.enums.ghost_states import GhostStates
from lib.entity.entity import Entity
from typing_extensions import override
import math, pygame


# Yellow
class Clyde(Ghost):
    COLOR = (255, 255, 0)

    def __init__(self, position, player: Entity):
        super().__init__(position, 11, player)
        self._player = player
        self._target_tile = None
        self.SCATTER_TILE = pygame.Vector2(0, GameMap().height)
        self.__image = pygame.image.load('assets/ghosts/clyde.png')

    def handle_event(self, event: pygame.event.Event):
        pass

    def render(self, surface: pygame.surface.Surface):
        if self._state == GhostStates.DEAD:
            image_rect = self._dead_image.get_rect(topleft=self.rect.topleft)
            surface.blit(self._dead_image, image_rect)
        elif self._state == GhostStates.FRIGHTENED:
            image_rect = self._frightened_image.get_rect(topleft=self.rect.topleft)
            surface.blit(self._frightened_image, image_rect)
        else:
            image_rect = self.__image.get_rect(topleft=self.rect.topleft)
            surface.blit(self.__image, image_rect)

        if self._target_tile is not None:
            pygame.draw.circle(surface, self.COLOR,
                               GameMap().get_tile(self._target_tile).rect.center, 5)
        if self._state == GhostStates.CHASE and math.dist(self._player.get_position(), self._position) > 8:
            pygame.draw.circle(surface, self.COLOR,
                               GameMap().get_tile(self._position).rect.center,
                               self.rect.width * 8, width=5)

    def _update_direction_SCATTER(self):
        self._target_tile = self.SCATTER_TILE
        self.set_direction(self._select_best_direction())

    @override
    def _update_direction_CHASE(self):
        self._target_tile = self._player.get_position()
        if math.dist(self._player.get_position(), self._position) <= 8:
            self._target_tile = self.SCATTER_TILE
        self.set_direction(self._select_best_direction())
