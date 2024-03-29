from lib.stage import GameStage
from typing import List, Tuple
from lib.managers.ghost_manager import GhostManager
from lib.entity.players.pacman import Pacman
from lib.entity.object import GameObject
from lib.map.map import GameMap
from lib.enums.game_events import STATE_HANDLER_NOT_IMPLEMENTED, GAME_OVER, NEXT_LEVEL
import pygame


class GameplayStage(GameStage):
    _map: GameMap = None
    _entities: List[GameObject] = []
    _font: pygame.font.Font = None
    _next_state = None
    score: int = 0

    def __init__(self, screen: pygame.surface.Surface):
        self._map = GameMap.get_instance()
        self.__screen = screen
        player = Pacman()
        self.add_entity(player)
        self._ghost_manager = GhostManager(self)
        self._clock = pygame.time.Clock()
        self._font = pygame.font.SysFont('Comic Sans MS', 30)

    def add_entity(self, *entities: GameObject):
        self._entities.extend([*entities])

    def get_entities(self):
        return self._entities

    @classmethod
    def get_target_fps(cls):
        return 60

    def render(self):
        self._map.render(self.__screen)
        for entity in self._entities:
            entity.render(self.__screen)
        self.__screen.blit(self._font.render(f"Score: {self.score}", True, (255, 255, 255)), (0, 0))

    def update(self, dt: float):
        for entity in self._entities:
            entity.update(dt)
        self._clock.tick(self.get_target_fps())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == STATE_HANDLER_NOT_IMPLEMENTED:
            print("State Handler not implemented", event.message)
        if event.type == NEXT_LEVEL:
            self._ghost_manager.next_level()

        for entity in self._entities:
            entity.handle_event(event)

    def next(self):
        if self._next_state is not None:
            return self._next_state
        return
