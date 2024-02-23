from .stage import GameStage
import pygame


class Game:
    __state: GameStage = None

    def __init__(self, state: GameStage):
        self.__state: GameStage = state

    def update(self, dt: float):
        self.__state.update(dt)

    def handle_events(self, events):
        for event in events:
            if event == pygame.QUIT:
                exit(0)
            self.__state.handle_event(event)

    def render(self):
        self.__state.render()
