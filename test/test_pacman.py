import pygame
import pytest
from lib.entity.pacman import Pacman


class TestPacman:

    @pytest.mark.parametrize("spawn, direction, target_fps, speed, frames, expected", [
        (pygame.Vector2(1, 1), pygame.Vector2(1, 0), 1, 11, 1, pygame.Vector2(2, 1)),
        (pygame.Vector2(1, 1), pygame.Vector2(1, 0), 1, 11, 1, pygame.Vector2(2, 1))
    ])
    def test_move_pacman(self, spawn, frames, target_fps, direction, expected_position):
        pacman = Pacman(spawn=spawn)
        pacman.set_direction(direction)
        for _ in range(frames):
            pacman.update(1)

        assert pacman.get_position(), expected_position
