from ..ghost import Ghost
from lib.map.map import GameMap
from ..entity import Entity
import pygame
import math
from ...enums.ghost_states import GhostStates


# Red
class Blinky(Ghost):
    COLOR = (255, 0, 0)

    def __init__(self, position, player: Entity):
        super().__init__(position, 11, player)
        self.SCATTER_TILE = pygame.Vector2(GameMap().width, 0)
        self.__image = pygame.image.load('assets/ghosts/blinky.png')

    def _calculate_distance_to_target_from_direction_vector(self, direction: pygame.Vector2):
        tile = GameMap().get_tile(self._position + direction)
        return math.dist(GameMap().get_tile(self._target_tile).rect.center,
                         tile.rect.center)

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

        pygame.draw.circle(surface, self.COLOR, GameMap().get_tile(self._position).rect.center, 5)
        if self._target_tile is not None:
            pygame.draw.circle(surface, self.COLOR,
                               GameMap().get_tile(self._target_tile).rect.center, 5)

    def _update_direction_SCATTER(self):
        self._target_tile = self.SCATTER_TILE
        self.set_direction(self._select_best_direction())

    def _update_direction_CHASE(self):
        self._target_tile = self._target.get_position()
        self.set_direction(self._select_best_direction())
