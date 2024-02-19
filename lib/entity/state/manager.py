from ...map.map import Map
from .state import EntityState
from ..movement.movement import MovementStrategy
from .frightened import FrightenedState
from .chase import ChaseState
from ..movement import ghost, frighten

class StateManager:


    def __init__(self, map: Map, player: MovementStrategy, initial_state: EntityState):
        self.__map = map
        self._states = {
            FrightenedState: FrightenedState(self.__map),
            ChaseState: ChaseState(player),
        }
        self._movements = {
            FrightenedState: frighten.FrightenedMovement(),
        }
        self._current_state = initial_state

    def handle_event(self, event):
        self._current_state.handle_event(event)
        new_state = self._current_state.next()
        if new_state is not None:
            self._current_state = self._states[new_state]

    def get_movement(self) -> MovementStrategy:
        pass

    def get_current_state(self) -> EntityState:
        return self._current_state
