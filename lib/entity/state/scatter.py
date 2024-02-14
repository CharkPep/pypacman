from .state import EntityState
from ...map.map import Map
import time

class ScatterState(EntityState):

    def __init__(self, map: Map):
        self.__map = map
        self.__timeout = time.clock() + 20

    def handle_event(self, event):
        pass

    def next(self):
        # if self.__timeout < time.clock():
        #     return States.CHASE
        return None

