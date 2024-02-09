from .entity import Entity
import pygame


class Score(Entity):
    def __init__(self, score: int, position: pygame.rect.Rect, img: pygame.image):
        super().__init__()
        self.__score = score
        self.__position = position
        self.__img = img

    def get_rect(self):
        return self.__position

    def update(self):
        pass

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 0, 255), self.__position)
        # surface.blit(self.__img, self.__position)
        pass

    def collide(self, other: pygame.rect.Rect):
        pass

    def get_score(self):
        return self.__score