from abc import ABC, abstractmethod
from typing import Union
from ..movement.movement import MovementStrategy
from typing import Tuple

class EntityState(ABC):
    """
    Abstract class for the state of an entity
    Responsible for handling events, movement behavior, sprite and state transitions
    """
    @abstractmethod
    def handle_event(self, event):
        pass

    @abstractmethod
    def get_target(self) -> Tuple[int, int]:
        pass

    @abstractmethod
    def next(self) -> Union['EntityState', None]:
        pass
