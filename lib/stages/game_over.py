import logging
import pygame
from lib.stage import GameStage
from lib.utils.button import Button
from lib.utils.button_stack import ButtonStack
from lib.enums.game_events import NEXT_STAGE

logger = logging.getLogger(__name__)


class GameOver(GameStage):

    def __init__(self, screen: pygame.surface.Surface):
        font_size = int(0.1 * min(*screen.get_size()))
        mx_text_size = pygame.font.Font(None, font_size).size("Back to the menu")
        center = pygame.rect.Rect(
            (screen.get_rect().centerx - mx_text_size[0] // 2, screen.get_rect().centery - mx_text_size[1]),
            mx_text_size)
        self._buttons = (
            ButtonStack("Restart", center, self.handle_restart, size=font_size, offset=pygame.Vector2(0, 10))
            .add("Back to the menu", self.handle_exit))

    def handle_event(self, event):
        self._buttons.handle_event(event)

    def handle_restart(self, button: Button):
        logger.debug("Restarting the game")
        pygame.event.post(pygame.event.Event(NEXT_STAGE, {"stage": 'GameplayStage'}))

    def handle_exit(self, button: Button):
        logger.debug("Restarting the game")
        pygame.event.post(pygame.event.Event(NEXT_STAGE, {"stage": 'Menu'}))

    def render(self, screen):
        self._buttons.render(screen)

    def update(self, dt: float):
        self._buttons.update()

    def reset(self):
        self._buttons.reset()
