import pygame
from lib.entity.entity import Entity


class Pacman(Entity):
    # TODO - Add dynamic spawn position depending on map
    SPAWN_POSITION = (1, 1)

    def __init__(self):
        super().__init__(self.SPAWN_POSITION, 11)

    # def resize_images(self, images: dict, width: int, height: int) -> dict:
    #     resized_images = {}
    #     for key, image in images.items():
    #         resized_image = pygame.transform.scale(image, (width, height))
    #         resized_images[key] = resized_image
    #     return resized_images

    def update(self, dt: float):
        super().update(dt)

    def handle_event(self, event: pygame.event.Event):
        if event.dict.get('key') == pygame.K_UP and event.type == pygame.KEYDOWN:
            self.set_direction(pygame.Vector2(0, -1))
            # self.__image = self.__image_dict['up']
        elif event.dict.get('key') == pygame.K_DOWN and event.type == pygame.KEYDOWN:
            self.set_direction(pygame.Vector2(0, 1))
            # self.__image = self.__image_dict['down']
        elif event.dict.get('key') == pygame.K_LEFT and event.type == pygame.KEYDOWN:
            self.set_direction(pygame.Vector2(-1, 0))
            # self.__image = self.__image_dict['left']
        elif event.dict.get('key') == pygame.K_RIGHT and event.type == pygame.KEYDOWN:
            self.set_direction(pygame.Vector2(1, 0))
            # self.__image = self.__image_dict['right']

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (255, 0, 0), self.get_rect())
        pygame.draw.line(surface, (0, 255, 0), self.get_rect().center,
                         self.get_rect().center + self._direction * 20)
        # surface.blit(self.__image, self.__rect)
