import os.path
from abc import ABC, abstractmethod
from .map import Map
from .object import MapObject
from typing import Tuple
import pygame


class Wall(MapObject):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class ThinWall(MapObject):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class OneWay(MapObject):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)


class Void(MapObject):
    def __init__(self, position: Tuple[int, int], size: Tuple[int, int], image: pygame.image):
        super().__init__(position, size, image)

    def isPassable(self):
        return True


class MapParser(ABC):
    """
    Abstract class for a map parser
    """
    @abstractmethod
    def parse(self, screen: Tuple[int, int]) -> Map:
        pass


codes = {
    "e": None,
    "w": Wall,
    "t": ThinWall,
    "s": None,
    "o": OneWay,
    "v": Void,
}


class DefaultMapParser(MapParser):
    __file = ""

    def __init__(self, file, surface: pygame.surface.Surface, margin=0, padding=0):
        self.margin = margin
        self.padding = padding
        self.__file = os.path.abspath(file)
        self.__surface = surface

    def parse(self, screen_size) -> Map:
        lines = 0
        columns = 0
        game_map = []
        with open(self.__file, "r") as file:
            for line in file:
                lines += 1
                layer = []
                current_column_count = 0
                for tile in line:
                    current_column_count += 1
                    if tile == "\n":
                        break
                    layer.append(codes[tile])
                game_map.append(layer)
                if current_column_count > columns:
                    columns = current_column_count
        columns -= 1
        size = min(screen_size[0] / columns, screen_size[1] / lines)
        if size == 0:
            raise ValueError("The map is too big for the screen")
        first_rectangle_position = (screen_size[0] - columns * size) / 2., (screen_size[1] - lines * size) / 2.
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                if game_map[i][j] is None:
                    continue
                rectangle_image = None
                game_map[i][j] = game_map[i][j]((first_rectangle_position[0] + size * j, first_rectangle_position[1] + size * i), (size, size), rectangle_image)
        return Map(game_map)
