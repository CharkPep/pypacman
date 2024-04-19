from lib.enums.game_events import NEXT_STAGE
import pygame

mouse_click = pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"mouse_pos": (100, 100)}))
assert (pygame.event.poll(), mouse_click)
