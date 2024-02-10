import math

from .entity import Entity
from .movement import MovementStrategy
from ..map.map import Map
from typing import  Tuple
import pygame


class Player(Entity):

    def __init__(self, image: pygame.image, rect: pygame.rect.Rect, movement: MovementStrategy):
        """
        :param image: assets
        :param rect: MapObject where player is placed
        """
        self.movement = movement
        self.next_move = None
        self.__image = image
        self.__rect = rect

    def update(self):
        direction = self.handle_input(pygame.key.get_pressed())
        if direction is None:
            if self.next_move is not None:
                direction = self.next_move
        if self.movement.move(self.__rect, direction):
            self.next_move = None
        else:
            self.next_move = direction

    def handle_input(self, key):
        if key[pygame.K_UP]:
            return pygame.Vector2(0, -1)
        elif key[pygame.K_DOWN]:
            return pygame.Vector2(0, 1)
        elif key[pygame.K_LEFT]:
            return pygame.Vector2(-1, 0)
        elif key[pygame.K_RIGHT]:
            return pygame.Vector2(1, 0)
        return None

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 0, 0), self.__rect)

    def get_rect(self):
        return self.__rect

    def collide(self, other: pygame.rect.Rect):
        return pygame.Rect.colliderect(self.__rect, other)


