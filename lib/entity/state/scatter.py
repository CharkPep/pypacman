from .state import EntityState
from ...map.map import Map
from typing import Tuple
import time


class ScatterState(EntityState):

    def __init__(self, corner: Tuple[int, int]):
        self._target = corner

    def handle_event(self, event):
        pass

    def next(self):
        return None

    def update(self, target):
        pass

    def get_target(self):
        return self._target


