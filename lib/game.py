from .state import GameState
import pygame


class Game:
    __state: GameState = None

    def __init__(self, state: GameState):
        self.__state: GameState = state

    def update(self, dt: float):
        self.__state.update(dt)

    def handle_events(self, events):
        for event in events:
            self.__state.handle_event(event)

    def render(self):
        self.__state.render()


