from abc import ABC


class GameStage(ABC):
    def handle_event(self, event):
        pass

    def update(self, dt: float):
        pass

    def render(self):
        pass

    def next(self) -> 'GameStage':
        pass
