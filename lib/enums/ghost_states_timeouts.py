from abc import ABC, abstractmethod


class GhostsStateTimeOuts(ABC):
    _level = 0

    def set_level(self, level):
        self._level = level

    @abstractmethod
    def get_timeout(self, state):
        pass


class GhostsStateTimeOutsEasy(GhostsStateTimeOuts):

    def __init__(self):
        self._curr_timeout = 0
