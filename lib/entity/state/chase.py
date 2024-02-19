from .state import EntityState
from ..movement.movement import MovementStrategy
from .scatter import ScatterState
from .frightened import FrightenedState
from ...map.map import Map
from typing import Tuple


class ChaseState(EntityState):

    def __init__(self, target: MovementStrategy):
        self._target = target

    def get_target(self) -> Tuple[int, int]:
        return self._target.get_current_position()

    def handle_event(self, event):
        if event == "PACMAN_BOOSTED":
            self.next_state = FrightenedState

    def next(self):
        pass
