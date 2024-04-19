import threading
import pygame


class SoundManager:
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

    def play_sound(self, sound_name):
        if sound_name in self.sound_effects:
            if not self.sound_playing:
                self.sound_playing = True
                self.current_sound_thread = threading.Thread(target=self._play_sound_thread, args=(sound_name,))
                self.current_sound_thread.start()
        else:
            print("Error: Sound not found.")

    def play_sound_sync(self, sound_name):
        if sound_name in self.sound_effects:
            sound = self.sound_effects[sound_name]
            length_in_ms = int(sound.get_length() * 1000)
            sound.play()
            pygame.time.wait(length_in_ms)

    def stop_sound(self):
        pygame.mixer.stop()
        self.sound_playing = False

    def _play_sound_thread(self, sound_name):
        self.current_sound_name = sound_name
        self.sound_effects[sound_name].play()
        pygame.time.wait(int(self.sound_effects[sound_name].get_length() * 1000))
        self.sound_playing = False
