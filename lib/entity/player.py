import math

from .entity import Entity
from ..map.map import Map
from typing import  Tuple
import pygame

def distance(point1, point2):
  """Calculates the Euclidean distance between two points represented as tuples.

  Args:
    point1: A tuple representing the coordinates of the first point (x, y).
    point2: A tuple representing the coordinates of the second point (x, y).

  Returns:
    The Euclidean distance between the two points.
  """
  x1, y1 = point1
  x2, y2 = point2
  squared_distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
  return math.sqrt(squared_distance)


class Player(Entity):

    def __init__(self, image: pygame.image, position : Tuple[int, int], map : Map):
        """
        :param image: assets
        :param rect: MapObject where player is placed
        """
        self.next_move = None
        self.__image = image
        self.__rect = map.get_map()[position[0]][position[1]].get_rect()
        self.__current_tile : Tuple[int, int] = position
        self.__direction_tile : Tuple[int , int] = position
        self.__speed = pygame.Vector2(0, 0)
        self.__map = map
        self._instance = self

    def update(self):
        self.handle_input()
        self.handle_coordinates()
        return

    def handle_change_speed(self, key):
        if key[pygame.K_UP]:
            self.__speed = pygame.Vector2(0, -1)
        elif key[pygame.K_DOWN]:
            self.__speed = pygame.Vector2(0, 1)
        elif key[pygame.K_LEFT]:
            self.__speed = pygame.Vector2(-1, 0)
        elif key[pygame.K_RIGHT]:
            self.__speed = pygame.Vector2(1, 0)

    def handle_coordinates(self):
        self.__rect.move_ip(self.__speed*2)

    def handle_input(self):
        current_position = self.__rect.center
        direction_position = self.__map.get_map()[int(self.__direction_tile[0])][int(self.__direction_tile[1])].get_rect().center
        key = pygame.key.get_pressed()
        if distance(current_position, direction_position) <= 5:
            self.__rect.center = direction_position
            self.__current_tile = self.__direction_tile
            if self.next_move is not None:
                self.handle_change_speed(self.next_move)
                self.next_move = None
            next_tile = self.__current_tile[0] + self.__speed.y, self.__current_tile[1] + self.__speed.x
            if next_tile[0] < 0 or next_tile[0] >= len(self.__map.get_map()) or next_tile[1] < 0 or next_tile[1] >= len(self.__map.get_map()[0]):
                self.__speed = pygame.Vector2(0, 0)
                return
            if not self.__map.get_map()[int(next_tile[0])][int(next_tile[1])].passable():
                self.__speed = pygame.Vector2(0, 0)

        if self.__direction_tile == self.__current_tile:
            self.handle_change_speed(key)
            self.__direction_tile = self.__current_tile[0] + self.__speed.y, self.__current_tile[1] + self.__speed.x
            if not self.__map.get_map()[int(self.__direction_tile[0])][int(self.__direction_tile[1])].passable():
                self.__speed = pygame.Vector2(0, 0)
                self.__direction_tile = self.__current_tile
        else:
            if key[pygame.K_UP] or key[pygame.K_DOWN] or key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
                self.next_move = key

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 0, 0), self.__rect)

    def get_rect(self):
        return self.__rect

    def collide(self, other: pygame.rect.Rect):
        return pygame.Rect.colliderect(self.__rect, other)


