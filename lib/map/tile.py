from typing import Tuple
import pygame


class Tile:
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        """
        :param position: Position of rectangle on the screen
        :param size: Size of rectangle
        :param image: Asset to be rendered on the rectangle
        """
        self._rect = pygame.Rect(position, size)
        self._image = image

    def render(self, surface: pygame.surface.Surface):
        surface.blit(self._image, self._rect)

    def get_rect(self):
        return self._rect

    def passable(self):
        return False

    def collide(self, other: pygame.Rect):
        return pygame.Rect.colliderect(self._rect, other)


class PlayerSpawn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)

    def passable(self):
        return True


class Void(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)

    def passable(self):
        return True


class HorizontalOutsideWall(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class VerticalOutsideWall(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class OutsideAngleTopRight(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class OutsideAngleBottomRight(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class OutsideAngleBottomLeft(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class OutsideAngleTopLeft(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class OutsideAngleTopLeft(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class HorizontalWall(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class VerticalWall(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class TopEnd(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class RightEnd(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class BottomEnd(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class LeftEnd(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class BigTopT(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class BigRightT(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class BigBottomT(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class BigLeftT(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class SmallTopT(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class SmallRightT(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class SmallLeftT(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class LeftTopTurn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class RightTopTurn(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class OneWay(Tile):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)

    def passable(self):
        return False
