from .entity import Entity
import pygame
from typing import Tuple
from .movement.strategy import MovementStrategy
from .movement.tileMovement import TileBasedMovement
from ..map.map import Map


class Player(Entity):

    def __init__(self, image: pygame.image, position: Tuple[int ,int], map: Map):
        self.__rect = pygame.rect.Rect(map.get_tile(position[0], position[1]).get_rect().topleft[0], map.get_tile(position[0], position[1]).get_rect().topleft[1], map.get_tile(0,0).get_rect().width, map.get_tile(0,0).get_rect().width)
        self.movement: MovementStrategy = TileBasedMovement(map, self.__rect, position) 
        self.__image = image

    def get_movement(self):
        return self.movement

    def update(self):
        self.movement.move()

    def handle_event(self, event: pygame.event.Event):
        if event.dict.get('key') == pygame.K_UP and event.type == pygame.KEYDOWN:
            self.movement.set_speed(pygame.Vector2(0, -1))
        elif event.dict.get('key') == pygame.K_DOWN and event.type == pygame.KEYDOWN:
            self.movement.set_speed(pygame.Vector2(0, 1))
        elif event.dict.get('key') == pygame.K_LEFT and event.type == pygame.KEYDOWN:
            self.movement.set_speed(pygame.Vector2(-1, 0))
        elif event.dict.get('key') == pygame.K_RIGHT and event.type == pygame.KEYDOWN:
            self.movement.set_speed(pygame.Vector2(1, 0))
        return None

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 0, 0), self.__rect)

    def get_rect(self):
        return self.__rect

    def collide(self, other: pygame.rect.Rect):
        return pygame.Rect.colliderect(self.__rect, other)


