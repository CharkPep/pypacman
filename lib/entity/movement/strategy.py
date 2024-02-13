from abc import ABC, abstractmethod
import pygame


class MovementStrategy(ABC):

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
    def move(self):
        pass

