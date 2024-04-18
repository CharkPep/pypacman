import pygame
from typing_extensions import override

from lib.map.map import GameMap
from lib.enums.game_events import POINT_EATEN, PALLET_EATEN
from lib.entity.entity import Entity


def resize_images(images: dict, width: int, height: int) -> dict:
    resized_images = {}
    for key, image in images.items():
        resized_image = pygame.transform.scale(image, (width, height))
        resized_images[key] = resized_image
    return resized_images


class Pacman(Entity):

    def __init__(self, spawn=(1, 1), velocity=11, **kwargs):
        super().__init__(pygame.Vector2(spawn), VELOCITY=velocity, **kwargs)
        images = {
            'up': pygame.image.load('assets/pacman/pacman0.png'),
            'down': pygame.image.load('./assets/pacman/pacman1.png'),
            'left': pygame.image.load('./assets/pacman/pacman2.png'),
            'right': pygame.image.load('assets/pacman/pacman3.png')
        }
        self.__image_dict = images
        self.__image = self.__image_dict['right']

    @override
    def reset(self):
        super().reset()
        self.__image = self.__image_dict['right']

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
            self.__image = self.__image_dict['up']
        elif event.dict.get('key') == pygame.K_DOWN and event.type == pygame.KEYDOWN:
            self.set_direction(pygame.Vector2(0, 1))
            self.__image = self.__image_dict['down']
        elif event.dict.get('key') == pygame.K_LEFT and event.type == pygame.KEYDOWN:
            self.set_direction(pygame.Vector2(-1, 0))
            self.__image = self.__image_dict['left']
        elif event.dict.get('key') == pygame.K_RIGHT and event.type == pygame.KEYDOWN:
            self.set_direction(pygame.Vector2(1, 0))
            self.__image = self.__image_dict['right']

    def render(self, surface: pygame.surface.Surface):
        surface.blit(self.__image, self.rect.topleft)
