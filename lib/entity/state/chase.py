from .state import EntityState
from ..movement.movement import MovementStrategy
from ...map.map import Map
from typing import Tuple


class ChaseState(EntityState):

    def __init__(self, target: MovementStrategy):
        self._target = target

    def get_target(self) -> Tuple[int, int]:
        return self._target.get_current_position()

    def handle_event(self, event):
        pass
        # if event == "PACMAN_BOOSTED":
        #     self.next_state = States.SCATTER

    def next(self):
        pass
