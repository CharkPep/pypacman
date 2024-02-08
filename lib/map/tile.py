from typing import List, Union, Tuple
import pygame


class Tile:
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        """
        :param position: Position of rectangle on the screen
        :param size: Size of rectangle
        :param image: Asset to be rendered on the rectangle
        """
        self.__rect = pygame.Rect(position, size)
        self.__image = image

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 255, 255), self.__rect)
        pygame.draw.line(surface, (0,0,0), self.__rect.topleft, self.__rect.topright)
        pygame.draw.line(surface, (0,0,0), self.__rect.topleft, self.__rect.bottomleft)
        pygame.draw.line(surface, (0,0,0), self.__rect.bottomleft, self.__rect.bottomright)
        pygame.draw.line(surface, (0,0,0), self.__rect.bottomright, self.__rect.topright)
        # surface.blit(self.__image, self.__rect)

    def get_rect(self):
        return self.__rect

    def passable(self):
        return False

    def collide(self, other: pygame.Rect):
        return pygame.Rect.colliderect(self.__rect, other)


class PlayerSpawn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)

    def passable(self):
        return True



class Wall(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class ThinWall(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class OneWay(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class Void(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)

    def passable(self):
        return True
