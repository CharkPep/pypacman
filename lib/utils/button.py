import pygame
import logging

logger = logging.getLogger(__name__)


class Button:

    def __init__(self, text, rect: pygame.rect.Rect, callback, align="center", background=None, color=(255, 255, 255),
                 font=None,
                 size=None):
        self.clicked = False
        self.text = text
        self._callback = callback
        self.background = background
        logger.debug(f"Button {text} with {rect}")
        self.rect = rect
        self.emitted = False
        self._align = align
        if size is None:
            size = min(rect.size)

        self._rendered_text = pygame.font.Font(font, size).render(text, True, color)

    def render(self, screen: pygame.Surface):
        if self.background is not None:
            screen.blit(self.background, self.rect)

        to_render = self._rendered_text
        if self.rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
            # blur the text
            to_render = pygame.transform.scale_by(pygame.transform.smoothscale_by(self._rendered_text, 10), 0.1)

        if self._align == "center":
            screen.blit(to_render, (
                self.rect.center[0] - self._rendered_text.get_width() // 2,
                self.rect.center[1] - self._rendered_text.get_height() // 2))
        elif self._align == "left":
            screen.blit(to_render, self.rect)
        elif self._align == "right":
            screen.blit(to_render, (
                self.rect.midright[0] - self._rendered_text.get_width(),
                self.rect.midright[1] - self._rendered_text.get_height()))

    def reset(self):
        self.emitted = False
        self.clicked = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.clicked and (
                    self.rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
                self.clicked = True

    def update(self):
        if self.clicked and not self.emitted:
            self.emitted = True
            self._callback(self)
