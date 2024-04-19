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

    def play_sound(self, sound_name, freeze=False):
        if sound_name in self.sound_effects:
            if not self.sound_playing:
                self.sound_playing = True
                self.current_sound_thread = threading.Thread(target=self._play_sound_async, args=(sound_name, freeze))
                self.current_sound_thread.start()
        else:
            logger.debug("Error: Sound not found.")

    def play_sound_sync(self, sound_name):
        if sound_name in self.sound_effects:
            sound = self.sound_effects[sound_name]
            length_in_ms = int(sound.get_length() * 1000)
            sound.play()
            pygame.time.wait(length_in_ms)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            if self.current_sound_thread is not None:
                self.current_sound_thread.join()
            if self.freeze_timer is not None:
                self.freeze_timer.cancel()

    def stop_sound(self):
        pygame.mixer.stop()
        self.sound_playing = False

    def _play_sound_async(self, sound_name, freeze=True):
        self.current_sound_name = sound_name
        if freeze:
            logger.debug(f"Playing track {sound_name} for {self.sound_effects[sound_name].get_length()} sec.")
            pygame.event.post(pygame.event.Event(FREEZE))
        self.sound_effects[sound_name].play()
        self.wait_thread = threading.Thread(target=self._wait_till_end,
                                            args=[self.sound_effects[sound_name].get_length(), freeze])
        self.wait_thread.start()

    def _wait_till_end(self, wait, unfreeze=False):
        time.sleep(wait)
        self._finish_playing(unfreeze)

    def _finish_playing(self, unfreeze=False):
        if unfreeze:
            pygame.event.post(pygame.event.Event(UNFREEZE))
        self.sound_playing = False
