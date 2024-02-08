from .entity import Entity
from ..map.tile import Tile
import pygame


class Player(Entity):
    _instance = None

    def __init__(self, image: pygame.image, rect: Tile):
        """
        :param image: assets
        :param rect: MapObject where player is placed
        """
        if self._instance is not None:
            return
        self.__image = image
        self.__rect = rect
        self.__speed = pygame.Vector2(0,0)
        self._instance = self

    def update(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 0, 0), self.__rect)
        # surface.blit(self.__image, self.__rect)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.__speed = pygame.Vector2(-1, 0)
        if key[pygame.K_RIGHT]: 
            self.__speed = pygame.Vector2(1, 0)
        if key[pygame.K_UP]:
            self.__speed = pygame.Vector2(0, -1)
        if key[pygame.K_DOWN]:
            self.__speed = pygame.Vector2(0, 1)
        self.__rect.move_ip(self.__speed)
        for line in map.get_map():
            for row in line:
                if row.collide(self.__rect):
                    print("collide")
                    break
    def collide(self, other: pygame.rect.Rect):
        return pygame.Rect.colliderect(self.__rect, other)


