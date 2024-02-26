from abc import abstractmethod, ABC
from lib.map.map import GameMap
from lib.map.tile import OneWay, Tile
from lib.enums.game_events import STATE_HANDLER_NOT_IMPLEMENTED
from lib.entity.entity import Entity
from lib.enums.ghost_states import GhostStates
import pygame
import random


class Ghost(Entity, ABC):
    _target_tile = None

    # TODO Add No move up tiles
    def __init__(
            self,
            position: pygame.Vector2,
            velocity: int,
            target: Entity,
    ):
        super().__init__(position, velocity)
        self._state = GhostStates.IDLE
        self._target = target

    def peek_tile(self, tile: Tile, direction: pygame.Vector2):
        return isinstance(GameMap.get_instance().get_tile(self._position + direction), tile)

    def _get_possible_directions(self):
        left = self._direction.rotate(90)
        right = self._direction.rotate(-90)
        straight = self._direction
        possible_directions = []
        if self._direction == pygame.Vector2(0, 0):
            left = pygame.Vector2(0, -1).rotate(90)
            right = pygame.Vector2(0, -1).rotate(-90)
            straight = pygame.Vector2(0, -1)
            back = pygame.Vector2(0, -1).rotate(180)
            if self._peek_in_direction(back) or self._state == GhostStates.EXITING_HOUSE and self.peek_tile(OneWay,
                                                                                                            back):
                possible_directions.append(back)
        if self._peek_in_direction(left) or self._state == GhostStates.EXITING_HOUSE and self.peek_tile(OneWay, left):
            possible_directions.append(left)
        if self._peek_in_direction(right) or self._state == GhostStates.EXITING_HOUSE and self.peek_tile(OneWay, right):
            possible_directions.append(right)
        if self._peek_in_direction(straight) or self._state == GhostStates.EXITING_HOUSE and self.peek_tile(OneWay,
                                                                                                            straight):
            possible_directions.append(straight)
        return possible_directions

    def update(self, dt: float):
        self._update_direction()
        super().update(dt)

    def _select_best_direction(self):
        possible_directions = self._get_possible_directions()
        distance_to_target = self._calculate_distance_to_target_from_direction_vector(self._direction)
        new_direction = None
        if new_direction is None and len(possible_directions) > 0:
            new_direction = possible_directions[0]
        if new_direction is None:
            new_direction = -self._direction
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

    def _update_direction(self):
        is_target_reached = self._check_if_target_reached()
        handler = None
        try:
            handler = getattr(self, f"_update_direction_{self._state.name}")
        except AttributeError:
            pygame.event.post(pygame.event.Event(STATE_HANDLER_NOT_IMPLEMENTED,
                                                 message=f"State handler for {self._state.name} not implemented"))
        if handler is not None and is_target_reached:
            handler()

    # Basic implementation for GhostStates
    def _update_direction_CHASE(self):
        self._target_tile = self._target.get_position()
        self._direction = self._select_best_direction()

    def _update_direction_IDLE(self):
        self._direction = pygame.Vector2(0, 0)

    def _update_direction_FRIGHTENED(self):
        direction = random.choice(self._get_possible_directions())
        self._direction = direction

    def _update_direction_DEAD(self):
        self._target_tile = GameMap.get_instance().get_ghost_house_exit()
        self._direction = self._select_best_direction()
        if self._position == self._target_tile:
            self.set_state(GhostStates.EXITING_HOUSE)

    def _update_direction_EXITING_HOUSE(self):
        self._target_tile = GameMap.get_instance().get_ghost_house_exit()
        self._direction = self._select_best_direction()
        if self._position == self._target_tile:
            self._state = GhostStates.CHASE

    def move(self, dt):
        if self._peek_in_direction(self._direction) or self._state == GhostStates.EXITING_HOUSE and self.peek_tile(
                OneWay,
                self._direction):
            self._rect.move_ip(self._direction * self._velocity * dt)
