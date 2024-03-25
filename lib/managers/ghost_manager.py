from lib.enums.ghost_states import GhostStates
from lib.entity.ghosts.blinky import Blinky
from lib.entity.ghosts.pinky import Pinky
from lib.entity.ghosts.inky import Inky
from lib.entity.ghosts.clyde import Clyde
from lib.entity.players.pacman import Pacman
from lib.enums.game_events import GHOST_EXIT_HOUSE, PALLET_EATEN
from lib.map.map import GameMap
from itertools import cycle
import threading
import pygame


class GhostManager:
    ghosts = []
    _global_ghost_state = GhostStates.IDLE
    _is_ghost_exited_house = False

    def __init__(self, game):
        self._game = game
        ghost_house = cycle(GameMap.get_instance().get_metadate()["ghost_house"]["tiles"])
        player = next(filter(lambda x: isinstance(x, Pacman), game.get_entities()))
        blinky = Blinky(pygame.Vector2(next(ghost_house)), player)
        pinky = Pinky(pygame.Vector2(next(ghost_house)), player)
        inky = Inky(pygame.Vector2(next(ghost_house)), player, blinky)
        clyde = Clyde(pygame.Vector2(next(ghost_house)), player)
        blinky.set_state(GhostStates.EXITING_HOUSE)
        pinky.set_state(GhostStates.EXITING_HOUSE)
        inky.set_state(GhostStates.EXITING_HOUSE)
        clyde.set_state(GhostStates.EXITING_HOUSE)
        blinky.activate()
        pinky.activate()
        inky.activate()
        clyde.activate()
        self._add_ghost(blinky, pinky, inky, clyde)
        game.add_entity(blinky, pinky, inky, clyde)
        self._level = 1
        self._chase_time = iter(GameMap.get_instance().get_metadate()["chase_duration"][str(self._level)])
        self._scatter_time = iter(GameMap.get_instance().get_metadate()["scatter_duration"][str(self._level)])

    def next_level(self):
        pass

    def handle_event(self, event: pygame.event.Event):
        if event.type == GHOST_EXIT_HOUSE and not self._is_ghost_exited_house:
            self._is_ghost_exited_house = True
            self.update_scatter()
        if event.type == PALLET_EATEN and self._is_ghost_exited_house:
            for ghost in self.ghosts:
                ghost.set_state(GhostStates.FRIGHTENED)

    def update_chase(self):
        self._global_ghost_state = GhostStates.CHASE
        for ghost in self.ghosts:
            ghost.set_state(GhostStates.CHASE)
        timeout = next(self._chase_time)
        print(timeout)
        if timeout is not None:
            threading.Timer(timeout / 1000, self.update_scatter).start()

    def update_scatter(self):
        self._global_ghost_state = GhostStates.SCATTER
        for ghost in self.ghosts:
            ghost.set_state(GhostStates.SCATTER)
        timeout = next(self._scatter_time)
        print(timeout)
        if timeout is not None:
            threading.Timer(timeout / 1000, self.update_chase).start()

    def get_global_ghost_state(self):
        return self._global_ghost_state

    def _add_ghost(self, *ghost):
        self.ghosts.extend(ghost)
