import pygame
from lib.map.map import GameMap
from lib.enums.game_events import POINT_EATEN, PALLET_EATEN
from lib.entity.entity import Entity


class Pacman(Entity):

    def __init__(self, spawn=(1, 1), velocity=11, **kwargs):
        super().__init__(pygame.Vector2(spawn), VELOCITY=velocity, **kwargs)
        # self.sprite = tileset

    def update(self, dt: float):
        on_tile = GameMap().get_tile(self._position, layer=1)
        if on_tile.id != 0 and on_tile.kwargs.get("render", False):
            if on_tile.id == GameMap().props["pallet"]:
                pygame.event.post(pygame.event.Event(PALLET_EATEN, {"tile": on_tile}))
                on_tile.kwargs["render"] = False
                return
            pygame.event.post(pygame.event.Event(POINT_EATEN, {"tile": on_tile}))
            on_tile.kwargs["render"] = False
        super().update(dt)

    def handle_event(self, event: pygame.event.Event):
        if event.dict.get('key') == pygame.K_UP and event.type == pygame.KEYDOWN:
            self.set_direction(pygame.Vector2(0, -1))
        elif event.dict.get('key') == pygame.K_DOWN and event.type == pygame.KEYDOWN:
            self.set_direction(pygame.Vector2(0, 1))
        elif event.dict.get('key') == pygame.K_LEFT and event.type == pygame.KEYDOWN:
            self.set_direction(pygame.Vector2(-1, 0))
        elif event.dict.get('key') == pygame.K_RIGHT and event.type == pygame.KEYDOWN:
            self.set_direction(pygame.Vector2(1, 0))

    def render(self, surface: pygame.surface.Surface):
        # surface.blit(next(iter(self.sprite)), self.rect)
        if self.kwargs.get("verbose", False):
            pygame.draw.circle(surface, (255, 255, 0), self.rect.center, self.rect.width // 2)
            pygame.draw.rect(surface, (255, 0, 0), self.rect, width=1)
