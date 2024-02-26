from enum import Enum


# Used to determine background music and game events
class GameStates(Enum):
    START_GAME = "START_GAME"
    PAUSE_GAME = "PAUSE_GAME"
    RESUME_GAME = "RESUME_GAME"
    PACMAN_DEATH = "PACMAN_DEATH"
    GHOST_DEATH = "GHOST_DEATH"
    NEXT_LEVEL = "NEXT_LEVEL"
    GAME_OVER = "GAME_OVER"
