import time

from lib.stage import GameStage
from typing import List, Tuple
from lib.managers.ghost_manager import GhostGroup
from lib.entity.pacman import Pacman
from lib.entity.object import GameObject
from lib.map.map import GameMap
from lib.enums.game_events import GAME_OVER, NEXT_LEVEL, POINT_EATEN, GHOST_PLAYER_COLLISION
import pygame
import logging

logger = logging.getLogger(__name__)


class GameplayStage(GameStage):
    _map: GameMap = None
    _entities: List[GameObject] = []
    font: pygame.font.Font = None
    _next_state = None
    score: int = 0

    def __init__(self, screen: pygame.surface.Surface, **kwargs):
        self.screen = screen
        self._player = Pacman(**kwargs)
        self.add_entity(self._player)
        self._ghost_group = GhostGroup(self._player, **kwargs)
        self.clock = pygame.time.Clock()
        self._score = 0
        self._lives = 1
        self._fruits = None
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.kwargs = kwargs

    def add_entity(self, *entities: GameObject):
        self._entities.extend([*entities])

    def get_entities(self):
        return self._entities

    @classmethod
    def get_target_fps(cls):
        return 60

    def render(self):
        GameMap().render(self.screen)
        for entity in self._entities:
            entity.render(self.screen)
        self._ghost_group.render(self.screen)
        self.screen.blit(self.font.render(f"Score: {self.score}", True, (0, 0, 0)), (0, 0))
        if self.kwargs.get("verbose", False):
            self.screen.blit(
                self.font.render(f"Ghosts: {self._ghost_group.get_global_ghost_state()}", True, (0, 0, 0)),
                (100, 0))

    def update(self, dt: float):
        for entity in self._entities:
            entity.update(dt)
        self._ghost_group.update(dt)
        self.clock.tick(self.get_target_fps())

    def start(self):
        self._ghost_group.start()

    def reset(self):
        self._ghost_group.freeze()
        self._player.freeze()
        self._lives -= 1
        logger.info(f'Game Over, left lives {self._lives}')
        self._ghost_group.reset()
        self._player.reset()
        GameMap().reset()

    def handle_event(self, event):
        if event.type == GAME_OVER:
            self.reset()
        if event.type == POINT_EATEN:
            self.score += 10
        if event.type == GHOST_PLAYER_COLLISION:
            self.score += 50
        if event.type == NEXT_LEVEL:
            self._ghost_group.next_level()
        self._ghost_group.handle_event(event)
        for entity in self._entities:
            entity.handle_event(event)

    def next(self):
        if self._next_state is not None:
            return self._next_state
        return
