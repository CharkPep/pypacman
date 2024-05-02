import logging
import threading
import time

from lib.enums.game_events import FREEZE, UNFREEZE
import pygame
from lib.utils.singleton import SingletonMeta

logger = logging.getLogger(__name__)


class SoundManager(metaclass=SingletonMeta):
    def __init__(self):
        pygame.mixer.init()
        self.sound_effects = {
            'beginning': pygame.mixer.Sound('assets/sounds/pacman_beginning.wav'),
            'chomp': pygame.mixer.Sound('assets/sounds/pacman_chomp.wav'),
            'death': pygame.mixer.Sound('assets/sounds/pacman_death.wav'),
            'eat_ghost': pygame.mixer.Sound('assets/sounds/pacman_eat_ghost.wav'),
        }
        self.sound_playing = False
        self.current_sound_thread = None
        self.freeze_timer = None

    def play_sound(self, sound_name, finalizer=None):
        if sound_name in self.sound_effects:
            if not self.sound_playing:
                self.sound_playing = True
                self.current_sound_thread = threading.Thread(target=self._play_sound_async,
                                                             args=(sound_name, finalizer))
                self.current_sound_thread.start()
        else:
            logger.debug("Error: Sound not found.")

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            if self.current_sound_thread is not None:
                self.current_sound_thread.join()
            if self.wait_thread is not None:
                self.wait_thread.join()
            if self.freeze_timer is not None:
                self.freeze_timer.cancel()

    def stop_sound(self):
        pygame.mixer.stop()
        self.sound_playing = False

    def _play_sound_async(self, sound_name, finalizer=None):
        self.current_sound_name = sound_name
        self.sound_effects[sound_name].play()
        logger.debug(f"Play sound {sound_name} for {self.sound_effects[sound_name].get_length()}")
        self.wait_thread = threading.Thread(target=self._wait_till_end,
                                            args=[self.sound_effects[sound_name].get_length(), finalizer])
        self.wait_thread.start()

    def _wait_till_end(self, wait, finalizer=None):
        time.sleep(wait)
        if finalizer is not None:
            finalizer()
        self.sound_playing = False
