from .state import State
from ..player import Player

class StateMachine:

    def __init__(self, state: State):
        self.__state = state

    def next(self, player : Player):
        pass

    def current_state(self):
        return self.__state

    def run(self):
        return self.__state.moving_direction()