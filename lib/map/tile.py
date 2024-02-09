from typing import Tuple
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
        pygame.draw.line(surface, (0, 0, 0), self.__rect.topleft, self.__rect.topright)
        pygame.draw.line(surface, (0, 0, 0), self.__rect.topleft, self.__rect.bottomleft)
        pygame.draw.line(surface, (0, 0, 0), self.__rect.bottomleft, self.__rect.bottomright)
        pygame.draw.line(surface, (0, 0, 0), self.__rect.bottomright, self.__rect.topright)
        # surface.blit(self.__image, self.__rect)

    def get_rect(self):
        return self.__rect

    def passable(self):
        return False

    def collide(self, other: pygame.Rect):
        return pygame.Rect.colliderect(self.__rect, other)


# tile0.jpg
class PlayerSpawn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)

    def passable(self):
        return True 


# tile0.jpg
class Void(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)

    def passable(self):
        return True


# tile1.jpg
class Dot(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile3.jpg
class BigDot(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile4.jpg
class TopWall(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile5.jpg
class RightWall(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile6.jpg
class BottomWall(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile7.jpg
class LeftWall(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile8.jpg
class LeftTopShortTurn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile9.jpg
class RightTopShortTurn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile10.jpg
class RightBottomShortTurn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile11.jpg
class LeftBottomShortTurn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile12.jpg
class LeftTopLongTurn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile13.jpg
class RightTopLongTurn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile14.jpg
class RightBottomLongTurn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile15.jpg
class LeftBottomLongTurn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


# tile16.jpg
class OneWay(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)

    def passable(self):
        return True
