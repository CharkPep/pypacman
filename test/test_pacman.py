import pygame
import pytest
from lib.entity.ghosts import blinky
from lib.entity.pacman import Pacman
from lib.enums.game_events import POINT_EATEN, PALLET_EATEN


class TestPacman:

    @pytest.mark.parametrize("spawn, direction, ticks, expected_position", [
        (pygame.Vector2(1, 1), pygame.Vector2(1, 0), 60, pygame.Vector2(12, 1)),
        (pygame.Vector2(1, 1), pygame.Vector2(0, 1), 60, pygame.Vector2(1, 8)),
        (pygame.Vector2(21, 26), pygame.Vector2(0, -1), 60, pygame.Vector2(21, 12)),
        (pygame.Vector2(26, 29), pygame.Vector2(-1, 0), 61, pygame.Vector2(14, 29))
    ])
    def test_pacman_should_change_direction(self, spawn, direction, ticks, expected_position):
        pacman = Pacman(spawn)
        pacman.set_direction(direction)
        for _ in range(ticks):
            # tick rate is 60 so 1/60 is one tick aka 1/FPS, pacman moves 11 tiles/sec
            pacman.update(1 / 60)
        print(pacman.get_position(), expected_position)
        assert pacman.get_position() == expected_position

    @pytest.mark.parametrize("spawn, direction, expected", [
        (pygame.Vector2(1, 1), pygame.Vector2(1, 0), pygame.Vector2(2, 1)),
        (pygame.Vector2(1, 1), pygame.Vector2(1, 0), pygame.Vector2(2, 1))
    ])
    def test_move_pacman(self, spawn, direction, expected):
        pacman = Pacman(spawn=spawn)
        pacman.set_direction(direction)
        for _ in range(10):
            pacman.update(1 / 60)

        assert pacman.get_position() == expected

    def test_pacman_move_to_wall(self):
        pacman = Pacman(pygame.Vector2(1, 1))
        pacman.set_direction(pygame.Vector2(0, -1))
        for _ in range(10):
            pacman.update(1)
        assert pacman.get_position() == pygame.Vector2(1, 1)

    def test_pacman_eat_point(self):
        pygame.event.get()
        pacman = Pacman(pygame.Vector2(1, 1))
        pacman.update(1)
        assert pygame.event.Event(POINT_EATEN), pygame.event.poll()

    def test_pacman_eat_power_pallet(self, map):
        pygame.event.get()
        pacman = Pacman(pygame.Vector2(1, 1))
        pacman.set_direction(pygame.Vector2(0, 1))
        for _ in range(60):
            pacman.update(1 / 60)
        event = pygame.event.poll()
        assert pygame.event.Event(PALLET_EATEN), pygame.event.poll()
