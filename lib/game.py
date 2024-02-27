from .stage import GameStage
import pygame, os


class Game:
    __state: GameStage = None

    def __init__(self, state: GameStage):
        self.__state: GameStage = state

    def update(self, dt: float):
        self.__state.update(dt)

    def handle_events(self, events):
        try:
            for event in events:
                if event == pygame.QUIT:
                    exit(0)
                self.__state.handle_event(event)
        except Exception as e:
            print(e)
            exit(1)

    def render(self):
        self.__state.render()
