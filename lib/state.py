from abc import ABC


class GameState(ABC):
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def next(self) -> 'GameState':
        pass
