from abc import ABC, abstractmethod
from typing import Union
from ..movement.strategy import MovementStrategy

class EntityState(ABC):
    """
    Abstract class for the state of an entity
    Responsible for handling events, movement behavior, sprite and state transitions
    """
    @abstractmethod
    def handle_event(self, event):
        pass

    @abstractmethod
    def update(self, entity: MovementStrategy):
        pass

    @abstractmethod
    def next(self) -> Union['EntityState', None]:
        pass
