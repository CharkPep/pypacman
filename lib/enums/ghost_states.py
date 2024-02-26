from enum import Enum


class GhostStates(Enum):
    SCATTER = "SCATTER"
    FRIGHTENED = "FRIGHTENED"
    IDLE = "IDLE"
    CHASE = "CHASE"
    EXITING_HOUSE = "EXITING_HOUSE"
    DEAD = "DEAD"
