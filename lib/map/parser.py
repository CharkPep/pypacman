import json
import os.path
from abc import ABC, abstractmethod
from .map import GameMap
from .tile import *
from typing import Tuple
import pygame


class MapParser(ABC):
    """
    Abstract class for a map parser
    """

    @abstractmethod
    def parse(self, screen: Tuple[int, int]) -> GameMap:
        pass


codes = {
    "0": Void,
    "1": HorizontalOutsideWall,
    "2": VerticalOutsideWall,
    "3": OutsideAngleTopRight,
    "4": OutsideAngleBottomRight,
    "5": OutsideAngleBottomLeft,
    "6": OutsideAngleTopLeft,
    "7": TopEnd,
    "8": RightEnd,
    "9": BottomEnd,
    "a": LeftEnd,
    "b": HorizontalWall,
    "c": VerticalWall,
    "d": BigTopT,
    "e": BigRightT,
    "f": BigBottomT,
    "g": BigLeftT,
    "h": OneWay,
    "i": PlayerSpawn,
    "j": SmallTopT,
    "k": SmallRightT,
    "l": SmallLeftT,
    "m": LeftTopTurn,
    "n": RightTopTurn,
}


class DefaultMapParser(MapParser):
    __file = ""

    def __init__(self, file, surface: pygame.surface.Surface, margin=0, padding=0):
        self.margin = margin
        self.padding = padding
        self.__file = os.path.abspath(file)
        self.__surface = surface

    def parse(self, screen_size) -> GameMap:
        lines = 0
        columns = 0
        game_map = []
        data = json.load(open(self.__file, "r"))
        for line in data["map"]:
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
                tile_code = game_map[i][j].__name__
                rectangle_image = pygame.image.load(f"assets/mapTiles/tile{tile_code}.png")
                rectangle_image = pygame.transform.scale(rectangle_image, (int(size), int(size)))
                game_map[i][j] = game_map[i][j](
                    (first_rectangle_position[0] + size * j, first_rectangle_position[1] + size * i), (size, size),
                    rectangle_image)
        return GameMap.get_instance(game_map, ghost_house=data["ghost_house"],
                                    chase_duration=data["chase_duration"], scatter_duration=data["scatter_duration"])
