from typing import Tuple
from abc import abstractmethod, ABC
from .entity import Entity
from lib.map.map import GameMap
import pygame


class Ghost(Entity, ABC):

    def __init__(
            self,
            position: Tuple[int, int],
            velocity: int,
    ):
        super().__init__(position, velocity)

    def _get_possible_directions(self, movement_direction: pygame.Vector2):
        left = movement_direction.rotate(90)
        right = movement_direction.rotate(-90)
        straight = movement_direction
        if movement_direction == pygame.Vector2(0, 0):
            left = pygame.Vector2(0, -1).rotate(90)
            right = pygame.Vector2(0, -1).rotate(-90)
            straight = pygame.Vector2(0, -1)
        possible_directions = []
        if GameMap.get_instance().is_passable((int(self._position[0] + straight.y),
                                               int(self._position[1] + straight.x))):
            possible_directions.append(straight)
        if GameMap.get_instance().is_passable((int(self._position[0] + right.y),
                                               int(self._position[1] + right.x))):
            possible_directions.append(right)
        if GameMap.get_instance().is_passable((int(self._position[0] + left.y), int(self._position[1] + left.x))):
            possible_directions.append(left)
        return possible_directions

    def update(self, dt: float):
        self._update_direction()
        super().update(dt)

    def _select_best_direction(self):
        movement_direction = self._direction
        if movement_direction == pygame.Vector2(0, 0):
            movement_direction = pygame.Vector2(0, -1)
        possible_directions = self._get_possible_directions(movement_direction)
        distance_to_target = self._calculate_distance_to_target_from_direction_vector(self._direction)
        new_direction = None
        if new_direction is None and len(possible_directions) > 0:
            new_direction = possible_directions[0]
        if new_direction is None:
            new_direction = -movement_direction
        for direction in possible_directions:
            distance = self._calculate_distance_to_target_from_direction_vector(direction)
            if distance <= distance_to_target:
                new_direction = direction
                distance_to_target = distance
        return new_direction

    @abstractmethod
    def _calculate_distance_to_target_from_direction_vector(self, direction: pygame.Vector2) -> float:
        """
        Calculates the distance to the target from the direction vector, the implementation depends on the ghost, 
        so different ghosts can have different targets
        :returns: float
        """
        pass

    @abstractmethod
    def set_state(self, state):
        """
        Changes the state of the ghost
        """
        pass

    @abstractmethod
    def _update_direction(self):
        """
        Updates the movement direction of a ghost
        """
        pass
