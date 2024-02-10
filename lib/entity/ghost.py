from .entity import Entity
from typing import Tuple
from ..map.map import Map
import pygame

class Ghost(Entity):

    def __init__(self, image: pygame.image, position : Tuple[int, int], map: Map):
        """
        :param image: assets
        :param rect: MapObject where player is placed
        """
        self.__image = image
        self.__rect = map.get_map()[position[0]][position[1]].get_rect()
        self.__current_tile : Tuple[int, int] = position
        self.__direction_tile : Tuple[int , int] = position
        self.__speed = pygame.Vector2(0, 0)
        self.__map = map
        self._instance = self

    def update(self):
        return

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 0, 0), self.__rect)
        # surface.blit(self.__image, self.__rect)