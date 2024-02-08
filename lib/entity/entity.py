from abc import ABC, abstractmethod
import pygame

class Entity(ABC):

    @abstractmethod
    def update(self):
        """
        Updates the entity, being called before rendering
        """
        pass

    @abstractmethod
    def render(self, surface: pygame.surface.Surface):
        """
        Renders the entity on the surface
        :param surface: Surface to render on
        """
        pass

    @abstractmethod
    def collide(self, other: pygame.rect.Rect):
        pass

