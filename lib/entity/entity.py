from abc import ABC
from .object import GameObject
import logging
from lib.utils.map import GameMap, is_walkable, is_intersection
import pygame
import math

SECOND = 60
logger = logging.getLogger(__name__)


class Entity(GameObject, ABC):
    _direction = pygame.Vector2(0, 0)

    """
        Entity base abstract class describes the basic movement and properties of an entity
        It exposes methods to move the entity and get its position
    """

    def __init__(self, position: pygame.Vector2, VELOCITY=11, TARGET_FPS=60, **kwargs):
        """
        :param position: Tuple[int, int]
        :param VELOCITY: int, speed in tiles per second
        """

        super().__init__()
        self._is_frozen = False
        self.kwargs = kwargs
        self._spawn_position = position
        self._position = position
        self.TARGET_FPS = TARGET_FPS
        self._velocity = (VELOCITY * GameMap().get_tile(
            pygame.Vector2(0, 0)).rect.width / SECOND * TARGET_FPS)
        self._change_direction: pygame.Vector2 = self._direction
        self.rect = pygame.rect.Rect(GameMap().get_tile(self._position).rect)

    def get_spawn_position(self):
        return self._spawn_position

    def reset(self):
        self._position = self._spawn_position
        self.rect.center = GameMap().get_tile(self._position).rect.center
        self._direction = pygame.Vector2(0, 0)
        self._change_direction = self._direction
        self._is_frozen = False

    def freeze(self):
        self._is_frozen = True

    def unfreeze(self):
        self._is_frozen = False

    def set_direction(self, direction: pygame.Vector2):
        # Can not really change direction if the entity is not in the middle (close to) of a tile
        if direction != self._direction and direction != self._change_direction:
            self._change_direction = direction

    def get_direction(self):
        return self._direction

    def peek_in_direction(self, direction: pygame.Vector2) -> bool:
        return is_walkable(self._position + direction)

    def _move_position_if_target_reached(self) -> bool:
        direction_position = self._position + self._direction
        direction_tile = GameMap().get_tile(direction_position)
        if not is_walkable(direction_position):
            return True

        if math.dist(self.rect.center, direction_tile.rect.center) <= self._velocity / self.TARGET_FPS:
            # entities can wrap around the map, so we add the width and height of the map to the position
            # and then take the modulo of the width and height to get the new position, this garanties that
            # the entity will be in the map
            # For example map width = 10, height = 10, position = (10, 10), direction = (1, 1)
            # new_position = (10, 10) + (1, 1) = (11, 11)
            # new_position = (11, 11) % (10, 10) = (1, 1)

            direction_position += pygame.Vector2(GameMap().width, GameMap().height)
            direction_position = pygame.Vector2(direction_position.x % GameMap().width,
                                                direction_position.y % GameMap().height)
            direction_tile = GameMap().get_tile(direction_position)
            self._position = direction_position
            self.rect.center = direction_tile.rect.center
            return True
        return False

    def update(self, dt):
        self._move_position_if_target_reached()

        # as is_intersection returns if there is 2 walkable tiles around the entity
        # we can reverse movement without any additional checks
        if is_intersection(self._position) and self._change_direction is not None and self.peek_in_direction(
                self._change_direction):
            self._direction = self._change_direction
            self.rect.center = GameMap().get_tile(self._position).rect.center
            self._change_direction = None

        self._move(dt)

    def get_position(self) -> pygame.Vector2:
        return self._position

    def _move(self, dt):
        if self.peek_in_direction(self._direction):
            self.rect.move_ip(self._direction * self._velocity * dt)
