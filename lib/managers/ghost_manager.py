from lib.enums.ghost_states import GhostStates
from lib.entity.ghosts.blinky import Blinky
from lib.entity.ghosts.pinky import Pinky
from lib.entity.ghosts.inky import Inky
from lib.entity.ghosts.clyde import Clyde
from lib.entity.players.pacman import Pacman
from lib.map.map import GameMap
import pygame


class GhostManager:
    ghosts = []

    def __init__(self, game):
        self._game = game
        player = next(filter(lambda x: isinstance(x, Pacman), game.get_entities()))
        blinky = Blinky(GameMap.get_instance().get_next_ghost_house_tile(), player)
        pinky = Pinky(GameMap.get_instance().get_next_ghost_house_tile(), player)
        inky = Inky(GameMap.get_instance().get_next_ghost_house_tile(), player, blinky)
        clyde = Clyde(GameMap.get_instance().get_next_ghost_house_tile(), player)
        blinky.set_state(GhostStates.EXITING_HOUSE)
        pinky.set_state(GhostStates.IDLE)
        inky.set_state(GhostStates.IDLE)
        clyde.set_state(GhostStates.IDLE)
        self._add_ghost(blinky, pinky, inky, clyde)
        game.add_entity(blinky, pinky, inky, clyde)
        self._chase_timeout = GameMap.get_instance().get_metadate()["chase_duration"]
        self._scatter_timeout = GameMap.get_instance().get_metadate()["scatter_duration"]
        self._current_timeout = GhostStates.SCATTER

    def next_level(self):
        pass

    def _add_ghost(self, *ghost):
        self.ghosts.append(ghost)
