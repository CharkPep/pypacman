from abc import ABC, abstractmethod
import pygame


class MovementStrategy(ABC):
    """
    Abstract class for the movement strategy of an entity
    Responsible for handling the movement pattern of an entity
    """
    @abstractmethod
    def get_current_position(self):
        pass

    @abstractmethod
    def set_speed(self, speed: pygame.Vector2):
        pass

    @abstractmethod
    def get_speed(self) -> pygame.Vector2:
        pass

    @abstractmethod
    def move(self, update: float):
        pass

