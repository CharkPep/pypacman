from .entity import Entity
import pygame
from typing import Tuple
from .movement.movement import MovementStrategy
from .movement.basic import BasicMovement
from ..map.map import Map


class Player(Entity, pygame.sprite.Sprite):

    def __init__(self, images: dict, position: Tuple[int, int], map: Map):
        self.__rect = pygame.rect.Rect(map.get_tile(position[0], position[1]).get_rect().topleft[0], map.get_tile(position[0], position[1]).get_rect().topleft[1], map.get_tile(0,0).get_rect().width, map.get_tile(0,0).get_rect().width)
        self.movement: MovementStrategy = BasicMovement(map, self.__rect, position)
        self.__image_dict = self.resize_images(images, map.get_tile(0, 0).get_rect().width,
                                               map.get_tile(0, 0).get_rect().height)
        self.__image = self.__image_dict['right']

    def resize_images(self, images: dict, width: int, height: int) -> dict:
        resized_images = {}
        for key, image in images.items():
            resized_image = pygame.transform.scale(image, (width, height))
            resized_images[key] = resized_image
        return resized_images

    def get_movement(self):
        return self.movement

    def update(self, dt: float):
        self.movement.update()
        self.movement.move(dt)

    def handle_event(self, event: pygame.event.Event):
        if event.dict.get('key') == pygame.K_UP and event.type == pygame.KEYDOWN:
            self.movement.set_direction(pygame.Vector2(0, -1))
            self.__image = self.__image_dict['up']
        elif event.dict.get('key') == pygame.K_DOWN and event.type == pygame.KEYDOWN:
            self.movement.set_direction(pygame.Vector2(0, 1))
            self.__image = self.__image_dict['down']
        elif event.dict.get('key') == pygame.K_LEFT and event.type == pygame.KEYDOWN:
            self.movement.set_direction(pygame.Vector2(-1, 0))
            self.__image = self.__image_dict['left']
        elif event.dict.get('key') == pygame.K_RIGHT and event.type == pygame.KEYDOWN:
            self.movement.set_direction(pygame.Vector2(1, 0))
            self.__image = self.__image_dict['right']
        return None

    def render(self, surface: pygame.surface.Surface):
        surface.blit(self.__image, self.__rect)


    def get_rect(self):
        return self.__rect

    def collide(self, other: pygame.rect.Rect):
        return pygame.Rect.colliderect(self.__rect, other)


