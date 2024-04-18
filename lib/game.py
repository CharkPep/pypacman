from lib.stage import GameStage
from lib.utils.singleton import SingletonMeta
from lib.stages.menu import Menu
from lib.stages.gameplay import GameplayStage
from lib.enums.game_events import NEXT_STAGE
import time
import pygame
import logging

logger = logging.getLogger(__name__)


class Game(metaclass=SingletonMeta):
    _stage: GameStage = None
    __current_time = time.time()
    __prev_time = __current_time

    def __init__(self, **kwargs):
        pygame.init()
        pygame.display.set_caption("Pacman")
        self._screen = pygame.display.set_mode((kwargs["width"], kwargs["height"]))
        self.clock = pygame.time.Clock()
        self.kwargs = kwargs
        self.states = {
            Menu: Menu(self._screen),
            GameplayStage: GameplayStage(**kwargs)
        }

        self._stage = self.states[Menu]
        if kwargs.get("debug", False):
            self._stage = self.states[GameplayStage]

    def start(self):
        self._stage.start()
        while True:
            try:
                self.handle_events(pygame.event.get())
                self.update()
                self.render()
                pygame.display.flip()
                self.clock.tick(60)
            except KeyboardInterrupt:
                self.handle_events([pygame.event.Event(pygame.QUIT)])
                break
            except Exception as e:
                print("Error: ", e)
                break

    def update(self):
        """
        Handles update with delta time accounted
        """
        self.__current_time = time.time()
        dt = self.__current_time - self.__prev_time
        self._stage.update(dt)
        self.__prev_time = self.__current_time

    def handle_events(self, events):
        """
        Handle events
        :param events: List[pygame.event.Event]
        """

        for event in events:
            self._stage.handle_event(event)
            if event.type == NEXT_STAGE:
                self._stage = self.states[self._stage.next()]
                self._stage.start()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def render(self):
        self._stage.render(self._screen)
