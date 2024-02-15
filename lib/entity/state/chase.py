from .state import EntityState
from ..movement.movement import MovementStrategy
from ...map.map import Map
from typing import Tuple


class ChaseState(EntityState):

    def __init__(self, target: MovementStrategy):
        self._target = target

    def get_target(self) -> MovementStrategy:
        return self._target

    def update(self, target: MovementStrategy):
        pass

    def handle_event(self, event):
        pass
        # if event == "PACMAN_BOOSTED":
        #     self.next_state = States.SCATTER

    def next(self):
        pass
