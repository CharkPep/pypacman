from .stage import GameStage
from lib.utils.singleton import SingletonMeta
from lib.map.parser import TiledMapParser
from lib.stages.gameplay import GameplayStage
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
        self._screen = pygame.display.set_mode((int(kwargs["width"]), int(kwargs["height"])))
        self.kwargs = kwargs
        if kwargs.get("verbose", False):
            logger.setLevel(logging.DEBUG)
        TiledMapParser(kwargs.get("level", "../levels/original.json"), verbose=kwargs.get("verbose", False)).parse(
            resolution=kwargs["RESOLUTION"])
        self._stage_screen = pygame.Surface(kwargs["RESOLUTION"])
        self._stage = GameplayStage(self._stage_screen, verbose=kwargs.get("verbose", False))

    def start(self):
        self._stage.start()

    def update(self):
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
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def render(self):
        self._screen.fill((0, 0, 0))
        self._stage.render()
        min_side = min(self.kwargs["width"], self.kwargs["height"])
        self._screen.blit(pygame.transform.scale(self._stage_screen, (min_side, min_side)),
                          ((self.kwargs["width"] - min_side) // 2, (self.kwargs["height"] - min_side) // 2))
