from .state import GameState
import pygame


class Game:
    __state: GameState = None

    def __init__(self, state: GameState):
        self.clock = pygame.time.Clock()
        self.__state: GameState = state

    def update(self):
        self.__state.update()
        self.clock.tick(60)

    def handle_events(self, events):
        for event in events:
            self.__state.handle_event(event)

    def render(self):
        pygame.display.flip()
        self.__state.render()


