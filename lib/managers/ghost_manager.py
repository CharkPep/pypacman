import json
import logging
from lib.enums.ghost_states import GhostStates
from lib.entity.ghosts.blinky import Blinky
from lib.entity.ghosts.pinky import Pinky
from lib.entity.ghosts.inky import Inky
from lib.entity.ghosts.clyde import Clyde
from lib.enums.game_events import GHOST_EXITED_HOUSE, PALLET_EATEN, GHOST_PLAYER_COLLISION, GAME_OVER
from itertools import cycle
import threading
import pygame
import logging

logger = logging.getLogger(__name__)


class GhostGroup(pygame.sprite.Group):
    _global_ghost_state = GhostStates.IDLE
    _is_ghost_exited_house = False
    _frightened_state_timer = None
    _activation_timer = None

    def __init__(self, player, ghost_props="./levels/ghosts.json", level=1, **kwargs):
        super().__init__()
        self._level = level
        self._global_ghost_state = GhostStates.IDLE
        self.kwargs = kwargs
        self._player = player
        with open(ghost_props) as file:
            data = json.load(file)
            logger.debug(f"Loaded {ghost_props}")
            self._chase_time = cycle(iter(data["chase_duration"][str(self._level)]))
            self._scatter_time = cycle(iter(data["scatter_duration"][str(self._level)]))
            blinky = Blinky(pygame.Vector2(data["blinky_spawn"]), player)
            pinky = Pinky(pygame.Vector2(data["pinky_spawn"]), player)
            inky = Inky(pygame.Vector2(data["inky_spawn"]), player, blinky)
            clyde = Clyde(pygame.Vector2(data["clyde_spawn"]), player)
            blinky.set_state(GhostStates.IDLE)
            self._activation_time = cycle(iter(data["activation_time"][str(self._level)]))
        # determine the activation order corresponding to the timeouts
        self.add(blinky, pinky, inky, clyde)
        self._is_frozen = False
        # self.add(blinky)

    def start(self):
        self._activation_timer = threading.Timer(next(self._activation_time), self._active_ghosts_with_timeout,
                                                 args=[iter(self.sprites()), self._activation_time])
        logger.debug("Start activation timer.")
        self._activation_timer.start()

    def freeze(self):
        for ghost in self.sprites():
            ghost.freeze()

    def unfreeze(self):
        for ghost in self.sprites():
            ghost.unfreeze()

    def reset(self):
        for sprite in self.sprites():
            sprite.reset()
        self._global_ghost_state = GhostStates.EXITING_HOUSE
        self._is_ghost_exited_house = False
        self._frightened_state_timer.cancel()
        self._activation_timer.cancel()
        self.start()

    def next_level(self):
        self._level += 1

    def update(self, dt):
        for ghost in self.sprites():
            ghost.update(dt)
        for ghost in self.sprites():
            if ghost.get_state() != GhostStates.DEAD and pygame.sprite.collide_rect(self._player, ghost):
                if ghost.get_state() == GhostStates.FRIGHTENED:
                    logger.debug("Player collided with frightened ghost.")
                    ghost.set_state(GhostStates.DEAD)
                    ghost.set_direction(-ghost.get_direction())
                    pygame.event.post(pygame.event.Event(GHOST_PLAYER_COLLISION, message=ghost))
                else:
                    logger.debug("Player collided with ghost.")
                    self._frightened_state_timer.cancel()
                    self._activation_timer.cancel()
                    pygame.event.post(pygame.event.Event(GAME_OVER, message=ghost))

    def render(self, screen):
        for ghost in self.sprites():
            ghost.render(screen)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.QUIT:
            if self._frightened_state_timer is not None:
                self._frightened_state_timer.cancel()
            self._activation_timer.cancel()
        if event.type == GHOST_EXITED_HOUSE:
            if not self._is_ghost_exited_house:
                self._update_scatter()
            self._is_ghost_exited_house = True
        if event.type == PALLET_EATEN and self._is_ghost_exited_house:
            logger.debug("Pallet eaten by player.")
            self._global_ghost_state = GhostStates.FRIGHTENED
            for ghost in self.sprites():
                if ghost.is_active():
                    ghost.set_state(GhostStates.FRIGHTENED)
            self._frightened_state_timer.cancel()
            self._frightened_state_timer = threading.Timer(10, self._update_chase)
            self._frightened_state_timer.start()

    def _active_ghosts_with_timeout(self, ghosts, timeout):
        try:
            ghost = next(ghosts)
            logger.debug(f"Activating ghost {ghost}.")
            ghost.activate()
            timer = next(timeout)
        except StopIteration:
            logger.debug("All ghosts are active.")
            return
        else:
            self._activation_timer = threading.Timer(timer, self._active_ghosts_with_timeout, args=[ghosts, timeout])
            self._activation_timer.start()

    def _update_chase(self):
        logger.debug("Switching to chase mode.")
        self._global_ghost_state = GhostStates.CHASE
        for ghost in self.sprites():
            ghost.set_state(GhostStates.CHASE)
        try:
            timeout = next(self._chase_time)
        except StopIteration:
            logger.debug("All ghosts are active.")
            return
        else:
            if timeout is not None:
                self._frightened_state_timer = threading.Timer(timeout, self._update_scatter)
                self._frightened_state_timer.start()

    def _update_scatter(self):
        logger.debug("Switching to scatter mode.")
        self._global_ghost_state = GhostStates.SCATTER
        for ghost in self.sprites():
            ghost.set_state(GhostStates.SCATTER)
        timeout = next(self._scatter_time)
        if timeout is not None:
            self._frightened_state_timer = threading.Timer(timeout, self._update_chase)
            self._frightened_state_timer.start()

    def get_global_ghost_state(self):
        return self._global_ghost_state
