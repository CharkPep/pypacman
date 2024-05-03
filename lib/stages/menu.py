import logging
import pygame
from lib.stage import GameStage
from lib.utils.button import Button
from lib.utils.button_stack import ButtonStack
from lib.enums.game_events import NEXT_STAGE

logger = logging.getLogger(__name__)


class Menu(GameStage):

    def __init__(self, screen: pygame.Surface):
        # TODO move to a separate button stack e.g CenteredButtonsStack, LeftButtonsStack
        font_size = int(0.2 * min(*screen.get_size()))
        mx_text_size = pygame.font.Font(None, font_size).size("Quite")
        logo = pygame.image.load("./assets/logo.png")
        logo = pygame.transform.scale_by(logo, mx_text_size[0] / logo.get_width() * 2)
        center = pygame.rect.Rect(
            (screen.get_rect().centerx - mx_text_size[0] // 2, screen.get_rect().centery - mx_text_size[1]),
            mx_text_size)
        # if it works it is good, if not it is very bad
        logo_rect = pygame.rect.Rect(center)
        logo_rect.centery -= mx_text_size[1] * 2
        logo_rect.centerx -= mx_text_size[0] // 2
        self._buttons = (
            ButtonStack("Play", center, self.handle_play, size=font_size, offset=pygame.Vector2(0, 10))
            .add("Quite", self.handle_exit))
        self._buttons.addButton(Button("", logo_rect, self.handle_click, background=logo))
        self._buttons.addButton(Button("version 0.0.1", pygame.rect.Rect(
            (screen.get_rect().bottomright[0] - pygame.font.Font(None, int(0.05 * min(*screen.get_size()))).size(
                "version 0.0.1")[0], screen.get_rect().bottomright[1] - int(0.05 * min(*screen.get_size()))),
            pygame.font.Font(None, int(0.05 * min(*screen.get_size()))).size(
                "version 0.0.1")), self.handle_click, size=int(0.05 * min(*screen.get_size()))))

    def handle_click(self, button: Button):
        logger.info("hello there")
        # TODO: should not call handler several times

    def handle_play(self, button: Button):
        logger.debug(f"Click on the f button with text {button.text}")
        pygame.event.post(pygame.event.Event(NEXT_STAGE))

    def handle_exit(self, button: Button):
        logger.debug("Click exit")
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def handle_event(self, event):
        self._buttons.handle_event(event)

    def render(self, screen):
        screen.fill((0, 0, 0))
        self._buttons.render(screen)

    def update(self, dt: float):
        self._buttons.update()

    def start(self):
        pass

    def reset(self):
        self._buttons.reset()

    def next(self) -> 'GameStage':
        return 'GameplayStage'
