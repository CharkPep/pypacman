from .entity import Entity
from .state import manager, state as States
from .movement.movement import MovementStrategy
from .movement.frighten import FrightenedMovement
from .movement.ghost import GhostMovement
from ..map.map import Map
from typing import Tuple
import pygame


class Ghost(Entity):

    def __init__(self,
             image: pygame.image,
             position: Tuple[int, int],
             map: Map,
             state_manager: manager.StateManager,
                 ):
        self._image = image
        self._rect = pygame.rect.Rect(map.get_tile(position[0], position[1]).get_rect().topleft[0], map.get_tile(position[0], position[1]).get_rect().topleft[1], map.get_tile(0, 0).get_rect().width, map.get_tile(0, 0).get_rect().width)
        self._state_manager: manager.StateManager = state_manager

    def handle_event(self, event):
        self._state_manager.handle_event(event)

    def update(self, dt):
        self._state_manager.get_movement().update()
        self._state_manager.get_movement().move(dt)

    def render(self, surface: pygame.surface.Surface):
        # surface.blit(self._image, self._rect.topleft)
        pygame.draw.rect(surface, (255, 0, 0), self._rect)
        pygame.draw.line(surface, (0, 255, 0), self._rect.center, self._rect.center + self.movement.get_direction() * 20)

    def get_rect(self):
        return self._rect

    def collide(self, other: pygame.rect.Rect):
        return pygame.Rect.colliderect(self._rect, other)