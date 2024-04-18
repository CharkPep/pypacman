from lib.utils.button import Button
import pygame
import logging

logger = logging.getLogger(__name__)


class ButtonStack:
    """
        creates a simple list of buttons arranges in a row.
    """

    def __init__(self, text, rect: pygame.rect.Rect, callback, align="center", background=None, color=(255, 255, 255),
                 font=None, size=None, offset=pygame.Vector2(0, 0), verbose=False):
        self._common_rect = rect
        self._verbose = verbose
        self._common_size = size
        self._common_color = color
        self._common_background = background
        self._common_font = font
        self._common_offset = offset
        self._buttons = [
            Button(text, rect, callback, align, background, color, font, size=size)
        ]

    def addButton(self, button: Button):
        self._buttons.append(button)

    def add(self, text, callback, self_offset=pygame.Vector2(0, 0), self_background=None) -> 'ButtonStack':
        bottomLeft = pygame.Vector2(self._common_rect.bottomleft) + self._common_offset + self_offset
        if self_background is None:
            logger.debug(f"Setting background {self_background}")
            self_background = self._common_background
        self._buttons.append(Button(text, pygame.rect.Rect(bottomLeft, self._common_rect.size), callback,
                                    color=self._common_color,
                                    size=self._common_size, background=self_background, font=self._common_font))
        return self

    def render(self, screen):
        for button in self._buttons:
            button.render(screen)

    def update(self):
        for button in self._buttons:
            button.update()

    def reset(self):
        for button in self._buttons:
            button.reset()

    def handle_event(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            logger.debug(f"Click {pygame.mouse.get_pos()}")
        for button in self._buttons:
            button.handle_event(e)
