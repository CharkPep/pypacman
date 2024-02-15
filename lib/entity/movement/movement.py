from abc import ABC, abstractmethod
import pygame
from typing import Tuple


class MovementStrategy(ABC):
    """
    Abstract class for the movement strategy of an entity
    Responsible for handling the movement pattern of an entity
    """
    @abstractmethod
    def get_current_position(self) -> Tuple[int, int]:
        pass

    @abstractmethod
    def set_direction(self, direction: pygame.Vector2):
        pass

    @abstractmethod
    def get_direction(self) -> pygame.Vector2:
        pass

    def update(self):
        pass

    @abstractmethod
    def move(self, update: float):
        pass

