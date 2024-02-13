from .entity import Entity
from .movement import MovementStrategy
from .state import machine, state
import pygame


class Ghost(Entity):

    def __init__(self,
                 image: pygame.image,
                 rect: pygame.rect.Rect,
                 movement: MovementStrategy,
                 playerMovement: MovementStrategy,
                 state : machine.StateMachine,
                 ):
        """
        :param image: assets
        :param rect: MapObject where player is placed
        """
        self.state = "chase"
        self.playerMovement = playerMovement
        self.state = state
        self.direction = []
        self.movement = movement
        self.next_move = None
        self.__image = image
        self.__rect = rect

    def update(self):
        self.direction = self.aiStrategy.moving_direction(self.movement.get_current_position(), self.playerMovement.get_current_position())
        print(self.direction, self.movement.get_current_position())
        if self.movement.move(self.__rect, -pygame.Vector2(pygame.Vector2(self.movement.get_current_position()[1] - self.direction[0][1], self.movement.get_current_position()[0] - self.direction[0][0]).normalize())):
            self.next_move = None
        else:
            self.next_move = self.direction
        return

    def render(self, surface: pygame.surface.Surface):
        pygame.draw.rect(surface, (0, 0, 0), self.__rect)
        # surface.blit(self.__image, self.__rect)

    def get_rect(self):
        return self.__rect

    def collide(self, other: pygame.rect.Rect):
        return pygame.Rect.colliderect(self.__rect, other)