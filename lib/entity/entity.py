from abc import ABC, abstractmethod
import pygame
from typing import List

class AiStrategy(ABC):
    @abstractmethod
    def move(self, game):
        pass


class Entity(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def render(self, surface):
        pass

    @abstractmethod
    def collide(self, other: pygame.rect.Rect):
        pass
