import math
import logging
from abc import abstractmethod, ABC
from lib.map.map import GameMap
from lib.enums.game_events import GHOST_EXITED_HOUSE
from lib.entity.entity import Entity
from lib.enums.ghost_states import GhostStates
from typing_extensions import override
import pygame
import random

logger = logging.getLogger(__name__)


class Ghost(Entity, ABC):
    # target_tile can be the player if the ghost is chasing the player, or a scatter tile or any other target
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
        self._is_active = False
        self._next_state = None
        self._frightened_image = pygame.image.load('assets/ghosts/frightened.png')
        self._dead_image = pygame.image.load('assets/ghosts/dead.png')

    def activate(self):
        self._state = GhostStates.EXITING_HOUSE
        self._is_active = True

    @override
    def reset(self):
        super().reset()
        self._state = GhostStates.EXITING_HOUSE
        self._is_active = False
        self._next_state = None
        self._target_tile = None

    def get_state(self):
        return self._state

    def is_active(self):
        return self._is_active

    def set_state(self, state):
        self._next_state = state
        if self._state != state and self._state != GhostStates.DEAD:
            self.set_direction(-self._direction)

    def peek_and_assert_tile(self, tile, direction: pygame.Vector2) -> bool:
        return GameMap().get_tile(self._position + direction).id == tile

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
            if self.peek_in_direction(back) or self._state == GhostStates.EXITING_HOUSE and self.peek_and_assert_tile(
                    GameMap().props["entrance"],
                    back):
                possible_directions.append(back)
        if self.peek_in_direction(left) or (
                self._state == GhostStates.EXITING_HOUSE and self.peek_and_assert_tile(GameMap().props["entrance"],
                                                                                       left)):
            possible_directions.append(left)
        if self.peek_in_direction(right) or (
                self._state == GhostStates.EXITING_HOUSE and self.peek_and_assert_tile(GameMap().props["entrance"],
                                                                                       right)):
            possible_directions.append(right)
        if self.peek_in_direction(straight) or (
                self._state == GhostStates.EXITING_HOUSE and self.peek_and_assert_tile(GameMap().props["entrance"],
                                                                                       straight)):
            possible_directions.append(straight)
        return possible_directions

    def update(self, dt: float):
        if self._is_active and not self._is_frozen:
            self._update_next_state()
            self._update_target_tile()
            super().update(dt)

    # TODO Add No move up tiles
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

    def _calculate_distance_to_target_from_direction_vector(self, direction: pygame.Vector2) -> float:
        tile = GameMap().get_tile(self._position + direction)
        return math.dist(GameMap().get_tile(self._target_tile).rect.center,
                         tile.rect.center)

    def _peek_back(self) -> bool:
        return self.peek_in_direction(-self._direction)

    def _update_next_state(self):
        if self._next_state is not None and (
                self._state != GhostStates.EXITING_HOUSE and self._state != GhostStates.DEAD):
            logger.debug(f"Ghost {self} state set to {self._next_state} from {self._state}")
            self._state = self._next_state
            if self._peek_back():
                self._direction = -self._direction
            self._next_state = None

    # Handles current state target update
    def _update_target_tile(self):
        is_target_reached = self._move_position_if_target_reached()
        handler = None
        try:
            handler = getattr(self, f"_update_direction_{self._state.name}")
        except AttributeError:
            logger.error(f"Ghost {self} has no handler for state {self._state}")
            self._state = GhostStates.IDLE
        if handler is not None and is_target_reached:
            handler()

    def _update_direction_IDLE(self):
        self._direction = pygame.Vector2(0, 0)
        self.rect.center = GameMap().get_tile(self._position).rect.center

    def _update_direction_FRIGHTENED(self):
        direction = random.choice(self._get_possible_directions())
        self.set_direction(direction)

    def _update_direction_DEAD(self):
        self._target_tile = pygame.Vector2(GameMap().props["entrance_target"])
        self.set_direction(self._select_best_direction())
        if self._position == self._target_tile:
            self._state = GhostStates.SCATTER
            # self.set_state(GhostStates.SCATTER)

    def _is_ghost_touch_ghost_house_entrance(self):
        entrance_id = GameMap().props["entrance"]
        for direction in self._get_possible_directions():
            if self.peek_and_assert_tile(entrance_id, direction):
                return True
        return False

    def _update_direction_EXITING_HOUSE(self):
        self._target_tile = pygame.Vector2(GameMap().props["entrance_target"])
        self._direction = self._select_best_direction()
        if self._is_ghost_touch_ghost_house_entrance() and self._position != self._target_tile:
            # move ghost into the gate so that it can move out to the target entrance
            self._position = (self._target_tile + self._position) // 2
            self.rect.center = GameMap().get_tile(self._position).rect.center
        if self._position == self._target_tile:
            logger.debug(f"Ghost {self} exited house.")
            pygame.event.post(pygame.event.Event(GHOST_EXITED_HOUSE, message=self))
            self._state = GhostStates.IDLE
            self._update_next_state()

    def _move(self, dt):
        if self.peek_in_direction(
                self._direction) or self._state == GhostStates.EXITING_HOUSE and self.peek_and_assert_tile(
            GameMap().props["entrance_target"], self._direction):
            self.rect.move_ip(self._direction * self._velocity * dt)
