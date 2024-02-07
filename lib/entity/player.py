from .entity import Entity, AiStrategy
import pygame
class Player(Entity):
    _instance = None

    def __init__(self, image: pygame.image, rect : pygame.Rect, strategy: AiStrategy):
        if self._instance is not None:
            raise ValueError("An instance already exists")
        self.__strategy = strategy
        self._instance = self
        self.__image = image
        self.__rect = rect
        self.__speed = pygame.Vector2(0,0)

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 255, 255), self.__rect)
        # surface.blit(self.__image, self.__rect)

    def move(self):
        self.__strategy.move()


class PlayerStrategy(AiStrategy):

    def __init__(self):
        pass

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print("UP")
        if keys[pygame.K_DOWN]:
            print("DOWN")
        if keys[pygame.K_LEFT]:
            print("LEFT")
        if keys[pygame.K_RIGHT]:
            print("RIGHT")
