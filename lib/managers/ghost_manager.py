from lib.enums.ghost_states import GhostStates

class GhostManager:
    ghosts = []
    state_timeout_pnt = 0
    STATE_TIMEOUT = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
    }

    def __init__(self, game):
        self._game = game
        blinky = Blinky()
        pinky = Pinky()
        inky = Inky()
        clyde = Clyde()
        self._add_ghost(blinky, pinky, inky, clyde)

    def next_level(self, dt):

    def _add_ghost(self, *ghost):
        self.ghosts.append(ghost)
