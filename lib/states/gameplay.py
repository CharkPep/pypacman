from ..state import GameState
from typing import List, Tuple
from ..entity.entity import Entity
from ..map.map import Map
from ..entity.player import Player
import pygame


class GameplayState(GameState):
    __map: Map = None
    __entities: List[Entity] = []
    __font: pygame.font.Font = None
    __next_state = None
    score: int = 0

    def __init__(self, map: Map, screen: pygame.surface.Surface):
        self.__map = map
        self.__screen = screen
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def add_entity(self, entity: Entity):
        self.__entities.append(entity)

    def render(self):
        self.__map.render(self.__screen)
        for entity in self.__entities:
            entity.render(self.__screen)
        self.__screen.blit(self.font.render(f"Score: {self.score}", True, (255, 255, 255)), (0, 0))

    def update(self):
        # for player in self.__players:
        #     player.update()
        #     for entity in self.__entities:
        #         if player.collide(entity.get_rect()):
        #             self.score += 1
        #             entity.reset()
        for entity in self.__entities:
            entity.update()

    def handle_event(self, event):
        for entity in self.__entities:
            entity.handle_event(event)

    def next(self):
        if self.__next_state is not None:
            return self.__next_state
        return
