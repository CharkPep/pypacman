from typing import List, Union, Tuple
import pygame

class MapObject:
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        self.__rect = pygame.Rect(position, size)
        self.__image = image

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 255, 255), self.__rect)
        pygame.draw.line(surface, (0,0,0), self.__rect.topleft, self.__rect.topright)
        pygame.draw.line(surface, (0,0,0), self.__rect.topleft, self.__rect.bottomleft)
        pygame.draw.line(surface, (0,0,0), self.__rect.bottomleft, self.__rect.bottomright)
        pygame.draw.line(surface, (0,0,0), self.__rect.bottomright, self.__rect.topright)

    def isPassable(self):
        return False

    def collide(self, other: pygame.Rect):
        return pygame.Rect.colliderect(self.__rect, other)