from .entity import Entity
import pygame
from typing import Tuple
from .movement.strategy import MovementStrategy
from .movement.tileMovement import TileBasedMovement
from ..map.map import Map


class Player(Entity):

    def __init__(self, image: pygame.image, position: Tuple[int ,int], map: Map):
        self.__rect = pygame.rect.Rect(position[0], position[1], map.get_tile(0,0).get_rect().width, map.get_tile(0,0).get_rect().width)
        self.movement: MovementStrategy = TileBasedMovement(map, self.__rect, position) 
        self.__image = image

    def get_movement(self):
        return self.movement

    def update(self):
        self.movement.move()

    def handle_event(self, event):
        if event == pygame.K_UP:
            self.movement.set_speed(pygame.Vector2(0, -1))
        elif event == pygame.K_DOWN:
            self.movement.set_speed(pygame.Vector2(0, 1))
        elif event == pygame.K_LEFT:
            self.movement.set_speed(pygame.Vector2(-1, 0))
        elif event == pygame.K_RIGHT:
            self.movement.set_speed(pygame.Vector2(1, 0))
        return None

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 0, 0), self.__rect)

    def get_rect(self):
        return self.__rect

    def collide(self, other: pygame.rect.Rect):
        return pygame.Rect.colliderect(self.__rect, other)


