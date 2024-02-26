from abc import ABC, abstractmethod
import pygame


class GameObject(ABC, pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    @abstractmethod
    def update(self, dt: float):
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
    def handle_event(self, event: pygame.event.Event):
        """
        Handles the event
        :param event: Event to handle
        """
        pass

    @abstractmethod
    def collide(self, other: pygame.rect.Rect):
        pass
