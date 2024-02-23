from ..stage import GameStage


class TitleState:

    def __init__(self, screen):
        self.options = ["Start", "Select level", "Quit"];
        self.selected_option = "Start"
        self.selected = 0

    def handle_events(self, events):
        pass

    def render(self):
        pass
