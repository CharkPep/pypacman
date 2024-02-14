from .entity import Entity
from .state import manager, state as States
from .movement.strategy import MovementStrategy
from .movement.tileMovement import TileBasedMovement
from ..map.map import Map
from typing import Tuple
import pygame


class Ghost(Entity):

    def __init__(self,
                 image: pygame.image,
                 position: Tuple[int, int],
                 map: Map,
                 current_state: States.EntityState,
                 ):
        self.__rect = pygame.rect.Rect(map.get_tile(position[0], position[1]).get_rect().topleft[0], map.get_tile(position[0], position[1]).get_rect().topleft[1], map.get_tile(0,0).get_rect().width, map.get_tile(0,0).get_rect().width)
        self.movement: MovementStrategy = TileBasedMovement(map, self.__rect, position)
        self.state: States.EntityState = current_state

    def handle_event(self, event):
        self.state.handle_event(event)

    def update(self):
        self.state.update(self.movement)
        self.movement.move()

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (0, 0, 0), self.__rect)

    def get_rect(self):
        return self.__rect

    def collide(self, other: pygame.rect.Rect):
        return pygame.Rect.colliderect(self.__rect, other)