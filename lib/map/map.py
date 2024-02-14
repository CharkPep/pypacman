from typing import List, Union, Tuple, Dict

import pygame.surface
from .tile import Tile


class Map:
    __map: List[List[Tile]] = None
    __graph: Dict[Tuple[int, int], List[Tuple[int, int]]] = {}
    __score =[]
    __boosts = []

    def __init__(self, map: List[List[Tile]]):
        self.__map = map

    def render(self, surface : pygame.surface.Surface):
        surface.fill((0, 0, 0))
        for layer in self.__map:
            for tile in layer:
                if tile is not None:
                    tile.render(surface)

    def get_map(self) -> List[List[Tile]]:
        return self.__map

    def get_tile_from_tuple(self, pos: Tuple[int, int]):
        if pos[0] < 0 or pos[0] >= len(self.__map) or pos[1] < 0 or pos[1] >= len(self.__map[0]):
            return None
        return self.__map[pos[0]][pos[1]]

    def get_tile(self, x: int, y: int) -> Union[Tile, None]:
        if x < 0 or x >= len(self.__map) or y < 0 or y >= len(self.__map[0]):
            return None
        return self.__map[x][y]

    def __parse_map(self):
        for i in range(len(self.__map)):
            for j in range(len(self.__map[i])):
                if self.__map[i][j].passable() and (self.__map[i][j].get_rect().centerx, self.__map[i][j].get_rect().centery) not in self.__graph:
                    self.__graph[(i, j)] = []
                    if self.get_tile(i + 1, j) is not None and self.get_tile(i + 1, j).passable():
                        self.__graph[(i, j)].append((i + 1, j))
                    if self.get_tile(i - 1, j) is not None and self.get_tile(i - 1, j).passable():
                        self.__graph[(i, j)].append((i - 1, j))
                    if self.get_tile(i, j + 1) is not None and self.get_tile(i, j + 1).passable():
                        self.__graph[(i, j)].append((i, j + 1))
                    if self.get_tile(i, j - 1) is not None and self.get_tile(i, j - 1).passable():
                        self.__graph[(i, j)].append((i, j - 1))

    def get_graph(self) -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
        if not self.__graph:
            self.__parse_map()
        return self.__graph