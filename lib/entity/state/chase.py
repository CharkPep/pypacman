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

    def update(self, entity: MovementStrategy):
        pass