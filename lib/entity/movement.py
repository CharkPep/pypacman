from abc import ABC, abstractmethod
import pygame
from ..map.map import Map
from typing import Tuple
import math


class MovementStrategy(ABC):
    @abstractmethod
    def move(self, entity: pygame.rect, direction: pygame.Vector2) -> bool:
        """

        :param entity: 
        :param direction: 
        :return: Returns True if movement was successful, False otherwise, continues to move
        """
        pass


class TileBasedMovement(MovementStrategy):
    __target_tile: Tuple[int, int] = None
    __current_tile: Tuple[int, int] = None
    __map: Map = None

    def __distance(self, point1: Tuple[int,int], point2 : Tuple[int,int]):
        x1, y1 = point1
        x2, y2 = point2
        squared_distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
        return math.sqrt(squared_distance)

    def __init__(self, map: Map, current_tile: Tuple[int, int]):
        self.__map = map
        self.__current_tile = current_tile
        self.__target_tile = current_tile
        self.__speed = pygame.Vector2(0, 0)

    def set_speed(self, speed: pygame.Vector2):
        self.__speed = speed

    def move(self, rect: pygame.rect.Rect, direction: pygame.Vector2) -> bool:
        target_rect = self.__map.get_map()[int(self.__target_tile[0])][int(self.__target_tile[1])].get_rect()
        changed_direction = False
        if direction is not None and direction * -1 == self.__speed:
            self.__current_tile = self.__target_tile
            self.__speed = direction
            self.__target_tile = self.__current_tile[0] + self.__speed.y, self.__current_tile[1] + self.__speed.x
        if self.__distance(rect.center, target_rect.center) <= 0.1:
            rect.center = target_rect.center
            self.__current_tile = self.__target_tile
            if direction is not None:
                self.__speed = direction
                changed_direction = True
            next_tile = self.__current_tile[0] + self.__speed.y, self.__current_tile[1] + self.__speed.x
            if next_tile[0] < 0 or next_tile[0] >= len(self.__map.get_map()) or next_tile[1] < 0 or next_tile[1] >= len(self.__map.get_map()[0]):
                self.__speed = pygame.Vector2(0, 0)
                return False
            if not self.__map.get_map()[int(next_tile[0])][int(next_tile[1])].passable():
                self.__speed = pygame.Vector2(0, 0)
                return False
            self.__target_tile = int(next_tile[0]), int(next_tile[1])
        rect.move_ip(self.__speed)
        return changed_direction