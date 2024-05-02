import pygame
import pytest
from lib.entity.ghosts import blinky, inky, pinky, clyde
from lib.enums.ghost_states import GhostStates
from lib.enums.game_events import GHOST_PLAYER_COLLISION, GAME_OVER
from lib.entity.pacman import Pacman


class TestGhost:

    @pytest.mark.parametrize("spawn, pacman_spawn, target", [
        (pygame.Vector2(1, 1), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(20, 1), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(10, 10), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(20, 10), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(10, 30), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
    ])
    def test_blinky_target(self, spawn, pacman_spawn, target):
        pacman = Pacman((1, 29))
        ghost = blinky.Blinky(pygame.Vector2(1, 1), pacman)
        ghost.activate()
        ghost._state = GhostStates.CHASE
        for _ in range(10):
            ghost.update(1 / 60)
        assert ghost._target_tile == pygame.Vector2(1, 29)

    @pytest.mark.parametrize("spawn, pacman_spawn, target", [
        (pygame.Vector2(1, 1), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(20, 1), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(10, 10), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(20, 10), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(10, 30), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
    ])
    def test_inky_target(self, spawn, pacman_spawn, target):
        pacman = Pacman(pacman_spawn)
        independent = blinky.Blinky(pacman_spawn, pacman)
        dependant = inky.Inky(spawn, pacman, independent)
        dependant.activate()
        dependant._state = GhostStates.CHASE
        for _ in range(10):
            dependant.update(1 / 60)
        assert dependant._target_tile == target

    @pytest.mark.parametrize("spawn, pacman_spawn, target", [
        (pygame.Vector2(1, 1), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(20, 1), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(10, 10), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(20, 10), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(10, 30), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
    ])
    def test_inky_target(self, spawn, pacman_spawn, target):
        pacman = Pacman(pacman_spawn)
        ghost = clyde.Clyde(spawn, pacman)
        ghost.activate()
        ghost._state = GhostStates.CHASE
        for _ in range(10):
            ghost.update(1 / 60)
        assert ghost._target_tile == target

    @pytest.mark.parametrize("spawn, pacman_spawn, target", [
        (pygame.Vector2(1, 1), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(20, 1), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(10, 10), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(20, 10), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
        (pygame.Vector2(10, 30), pygame.Vector2(1, 29), pygame.Vector2(1, 29)),
    ])
    def test_pinky_target(self, spawn, pacman_spawn, target):
        pacman = Pacman(pacman_spawn)
        pacman.set_direction(pygame.Vector2(1, 0))
        ghost = pinky.Pinky(spawn, pacman)
        ghost.activate()
        ghost._state = GhostStates.CHASE
        for _ in range(10):
            ghost.update(1 / 60)
        assert ghost._target_tile == target

    def test_ghost_run_from_pacman_direction(self):
        pass

    def test_dead(self):
        pass
