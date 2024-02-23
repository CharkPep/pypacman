from enum import Enum
import pygame


class MovementDirections(Enum):
    UP = pygame.Vector2(0, 1)
    DOWN = pygame.Vector2(0, -1)
    LEFT = pygame.Vector2(-1, 0)
    RIGHT = pygame.Vector2(1, 0)
