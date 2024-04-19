from lib.map.parser import TiledMapParser
from lib.stage import GameStage
from typing import List, Tuple
from lib.managers.ghost_manager import GhostGroup
from lib.entity.pacman import Pacman
from lib.entity.object import GameObject
from lib.map.map import GameMap
from lib.enums.game_events import GAME_OVER, NEXT_LEVEL, POINT_EATEN, GHOST_PLAYER_COLLISION, PALLET_EATEN
from lib.utils.sound_manager import SoundManager
from lib.utils.singleton import SingletonMeta
import pygame
import logging

logger = logging.getLogger(__name__)


class GameplayStage(GameStage):
    _map: GameMap = None
    _entities: List[GameObject] = []
    font: pygame.font.Font = None
    _next_state = None
    score: int = 0

    def __init__(self, **kwargs):
        TiledMapParser(layers=kwargs.get("map", "./levels/original.json")).parse(kwargs.get("RESOLUTION"))
        self._player = Pacman(**kwargs)
        self.add_entity(self._player)
        self._ghost_group = GhostGroup(self._player, levels=1, **kwargs)
        self.clock = pygame.time.Clock()
        self._score = 0
        self._lives = 3
        self._fruits = None
        self._left_points = GameMap().points
        self.sound_manager = SoundManager()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.kwargs = kwargs

    def add_entity(self, *entities: GameObject):
        self._entities.extend([*entities])

    def get_entities(self):
        return self._entities

    @classmethod
    def get_target_fps(cls):
        return 60

    def render(self, screen):
        min_side = min(self.kwargs["width"], self.kwargs["height"])
        downscaled = pygame.Surface(self.kwargs["RESOLUTION"])
        GameMap().render(downscaled)
        for entity in self._entities:
            entity.render(downscaled)
        self._ghost_group.render(downscaled)
        downscaled.blit(self.font.render(f"Score: {self.score}", True, (0, 0, 0)), (0, 0))
        if self.kwargs.get("verbose", False):
            downscaled.blit(
                self.font.render(f"Ghosts: {self._ghost_group.get_global_ghost_state()}", True, (0, 0, 0)),
                (100, 0))
        screen.blit(pygame.transform.scale(downscaled, (min_side, min_side)),
                    ((self.kwargs["width"] - min_side) // 2, (self.kwargs["height"] - min_side) // 2))

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

    def handle_event(self, event):
        if event.type == GAME_OVER:
            if self._lives <= 0:
                # DRAW GAME OVER
                self._lives = 3
                self.sound_manager.play_sound_sync('death')
                # -> TO MAIN MENU
            self.sound_manager.play_sound_sync('death')
            self.reset()
        if event.type == POINT_EATEN:
            self.sound_manager.play_sound('chomp')
            self.score += 10
            self._left_points -= 1
        if event.type == PALLET_EATEN:
            self.sound_manager.play_sound('chomp')
            self.score += 50
        if event.type == GHOST_PLAYER_COLLISION:
            self.sound_manager.stop_sound()
            self.sound_manager.play_sound('eat_ghost')
            self.score += 200
        if self._left_points == 0:
            self.reset()
        if event.type == NEXT_LEVEL:
            self._ghost_group.next_level()
            self.reset()
        self._ghost_group.handle_event(event)
        for entity in self._entities:
            entity.handle_event(event)

    def next(self):
        if self._next_state is not None:
            return self._next_state
        return
