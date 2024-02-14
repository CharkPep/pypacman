import math
from .state import EntityState
from ..movement.strategy import MovementStrategy
from ...map.map import Map
import time


class ChaseState(EntityState):

    def __init__(self, map: Map):
        self.__map = map

    def handle_event(self, event):
        pass
        # if event == "PACMAN_BOOSTED":
        #     self.next_state = States.SCATTER

    def next(self):
        pass
        # if self.next_state is not None:
        #     state = self.next_state
        #     self.next_state = None
        #     return state
        # if self.timeout < time.clock():
        #     return States.SCATTER

    def update(self, entity: MovementStrategy):
        pass
        # if len(direction) > 0:
        #     direction = direction[0]
        #     entity.set_speed(pygame.Vector2(direction[1] - entity.get_current_position()[1], direction[0] - entity.get_current_position()[0]))