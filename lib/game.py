from lib.stage import GameStage
from lib.utils.singleton import SingletonMeta
from lib.stages.menu import Menu
from lib.stages.gameplay import GameplayStage
from lib.stages.game_over import GameOver
from lib.enums.game_events import NEXT_STAGE, FREEZE, UNFREEZE
import pygame
import logging

logger = logging.getLogger(__name__)


class Game(metaclass=SingletonMeta):
    _stage: GameStage = None
    _freeze = None

    def __init__(self, **kwargs):
        pygame.init()
        pygame.display.set_caption("Pacman")
        self._screen = pygame.display.set_mode((kwargs["width"], kwargs["height"]))
        self.clock = pygame.time.Clock()
        self.kwargs = kwargs
        self.states = {
            'Menu': Menu(self._screen),
            'GameplayStage': GameplayStage(**kwargs),
            'GameOver': GameOver(self._screen)
        }

        self._stage = self.states['Menu']
        if kwargs.get("debug", False):
            self._stage = self.states['GameplayStage']

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
        self._stage.update(self.clock.get_time() / 1000)

    def handle_events(self, events):
        """
        Handle events
        :param events: List[pygame.event.Event]
        """

        for event in events:
            self._stage.handle_event(event)
            if event.type == NEXT_STAGE:
                if "stage" in event.__dict__:
                    self._stage = self.states[event.__dict__["stage"]]
                else:
                    self._stage = self.states[self._stage.next()]

                self._stage.start()
            if event.type == FREEZE:
                self._stage.pause()
            if event.type == UNFREEZE:
                self._stage.unpause()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def render(self):
        self._screen.fill((0, 0, 0))
        self._stage.render(self._screen)
