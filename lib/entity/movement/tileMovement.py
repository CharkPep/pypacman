import pygame
from .strategy import MovementStrategy
from ...map.map import Map
from typing import Tuple
import math


class TileBasedMovement(MovementStrategy):
    __target_tile: Tuple[int, int] = None
    __current_tile: Tuple[int, int] = None
    __map: Map = None

    def __init__(self, map: Map, entity: pygame.rect.Rect, current_tile: Tuple[int, int]):
        self.__map = map
        self.__current_tile = current_tile
        self.__target_tile = current_tile
        self.__rect = entity
        self.__speed = pygame.Vector2(0, 0)
        self.__direction = self.__speed

    def set_speed(self, speed: pygame.Vector2):
        # Can not really change speed if the entity is not in the middle of a tile
        self.__direction = speed

    def get_speed(self) -> pygame.Vector2:
        return self.__speed

    def get_current_position(self):
        return self.__current_tile

    def move(self):
        # Reverse movement
        if self.__direction * -1 == self.__speed:
            self.__current_tile = self.__target_tile
            self.__speed = self.__direction
            self.__target_tile = int(self.__current_tile[0] + self.__speed.y), int(self.__current_tile[1] + self.__speed.x)

        target_rect = self.__map.get_map()[int(self.__target_tile[0])][int(self.__target_tile[1])].get_rect()
        if math.dist(self.__rect.center, target_rect.center) <= 0.1:
            self.__rect.center = target_rect.center
            self.__current_tile = self.__target_tile
            self.__speed = self.__direction
            next_tile = self.__current_tile[0] + self.__speed.y, self.__current_tile[1] + self.__speed.x
            if next_tile[0] < 0 or next_tile[0] >= len(self.__map.get_map()) or next_tile[1] < 0 or next_tile[1] >= len(
                    self.__map.get_map()[0]):
                self.__speed = pygame.Vector2(0, 0)
                return
            if not self.__map.get_map()[int(next_tile[0])][int(next_tile[1])].passable():
                self.__speed = pygame.Vector2(0, 0)
                return
            self.__target_tile = int(next_tile[0]), int(next_tile[1])
        self.__rect.move_ip(self.__speed)
