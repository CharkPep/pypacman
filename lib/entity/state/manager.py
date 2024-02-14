from ...map.map import Map
from .state import EntityState
from .chase import ChaseState
from .frightened import FrightenedState
from .eaten import EatenState
from .scatter import ScatterState
from enum import Enum


class States(Enum):
    CHASE = ChaseState
    SCATTER = ScatterState
    FRIGHTENED = FrightenedState
    EATEN = EatenState


class StateManager:
    _instance = None

    def __init__(self, map: Map):
        self.__map = map
        self.__states = {
            # ChaseState: ChaseState(map),
            # ScatterState: ScatterState(map)
            # EatenState: EatenState(map),
            # FrightenedState: FrightenedState(map)
        }

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_state(self, state: States):
        return self.__states[state.value]
