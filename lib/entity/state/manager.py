from ...map.map import Map
from .state import EntityState


class StateManager:
    _instance = None

    def __init__(self, map: Map, initial_state: EntityState, states: dict[EntityState, EntityState]):
        self.__map = map
        self._current_state = initial_state

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def handle_event(self, event):
        pass

    def get_current_state(self) -> EntityState:
        return self._current_state
