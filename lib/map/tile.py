from typing import Tuple
import pygame


class Tile(pygame.sprite.Sprite):

    def __init__(self, id, position: Tuple[int, int], size: Tuple[int, int], layer, **kwargs):
        super().__init__()
        self.id = id
        self.kwargs = kwargs
        self._layer = layer
        self.rect = pygame.Rect(position, size)

    def render(self, surface: pygame.surface.Surface):
        img = self.kwargs.get("img", None)
        if img is not None and self.kwargs.get("render", False):
            surface.blit(img, self.rect)
        if self.kwargs.get("verbose", False):
            pygame.draw.rect(surface, (255, 0, 0), self.rect, width=1)
