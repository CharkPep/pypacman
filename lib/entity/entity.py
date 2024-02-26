from abc import ABC, abstractmethod
from .object import GameObject
from lib.map.map import GameMap
from lib.stages.gameplay import GameplayStage
import pygame
from typing import Tuple
import math

SECOND = 60


class Entity(GameObject, ABC):
    _direction = pygame.Vector2(0, 0)
    """
        Entity base abstract class describes the basic movement and properties of an entity
        It exposes methods to move the entity and get its position
    """

    def __init__(self, position, velocity):
        """
        :param position: Tuple[int, int]
        :param velocity: int, speed in tiles per second
        """
        super().__init__()
        self._position = position
        self._velocity = velocity * GameMap.get_instance().get_tile(0,
                                                                    0).get_rect().width / SECOND * GameplayStage.get_target_fps()
        self._change_direction: pygame.Vector2 = self._direction
        self._rect = pygame.rect.Rect(GameMap.get_instance().get_tile_from_tuple(self._position).get_rect())

    def set_direction(self, direction: pygame.Vector2):
        # Can not really change speed if the entity is not in the middle of a tile
        self._change_direction = direction

    def _is_passable_in_direction(self, direction: pygame.Vector2):
        return GameMap.get_instance().is_passable(
            (int(self._position[0] + direction.y), int(self._position[1] + direction.x)))

    def _check_if_target_reached(self):
        # Move from the current tile to the direction tile
        direction_tile = int(self._position[0] + self._direction.y), int(
            self._position[1] + self._direction.x)
        # The speed is measured in tile/sec, but when set to entity is multiplied by the target fps
        if math.dist(self._rect.center,
                     GameMap.get_instance().get_tile_from_tuple(
                         direction_tile).get_rect().center) <= self._velocity / GameplayStage.get_target_fps():
            self._position = direction_tile
            self._rect.center = GameMap.get_instance().get_tile_from_tuple(self._position).get_rect().center
            return True
        return False

    def update(self, dt):
        # Change movement direction
        self._check_if_target_reached()
        if GameMap.get_instance().is_intersection(self._position) and self._change_direction != self._direction:
            # Check if change direction is possible
            if self._change_direction is not None and self._is_passable_in_direction(self._change_direction):
                self._direction = self._change_direction
                self._rect.center = GameMap.get_instance().get_tile_from_tuple(self._position).get_rect().center
                self._change_direction = None

        self.move(dt)

    def get_position(self):
        return self._position

    def move(self, dt):
        if self._is_passable_in_direction(self._direction):
            self._rect.move_ip(self._direction * self._velocity * dt)

    def get_rect(self):
        return self._rect

    def collide(self, other: pygame.rect.Rect):
        return pygame.Rect.colliderect(self._rect, other)
