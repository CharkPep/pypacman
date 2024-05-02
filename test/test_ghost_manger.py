import pygame
import pytest
from lib.entity.pacman import Pacman
from lib.managers.ghost_manager import GhostGroup
from lib.enums.ghost_states import GhostStates
from lib.enums.game_events import GAME_OVER


class TestGhostManger:

    @pytest.mark.parametrize("player_spawn, ticks, activate_idx, level", [
        (pygame.Vector2(1, 1), 60, 0, 1),
        (pygame.Vector2(1, 1), 60, 0, 2),
        (pygame.Vector2(1, 1), 60, 0, 3),
        (pygame.Vector2(1, 1), 60, 0, 4)
    ])
    def test_ghost_manager_handling_player_ghost_collision(self, player_spawn, level, activate_idx, ticks):
        pygame.event.get()
        pacman = Pacman(player_spawn)
        group = GhostGroup(pacman, "./levels/ghosts_test.json", level=level)
        group.sprites()[activate_idx].activate()
        group.sprites()[activate_idx]._state = GhostStates.CHASE
        group.start()
        for _ in range(ticks):
            group.update(1 / 60)
        assert pygame.event.poll().type == GAME_OVER

    @pytest.mark.parametrize("player_spawn", [
        pygame.Vector2(1, 1), pygame.Vector2(1, 2),
        pygame.Vector2(4, 1), pygame.Vector2(1, 2),
        pygame.Vector2(6, 1), pygame.Vector2(1, 2),
    ])
    def test_ghost_manager_handling_player_ghost_collision(self, player_spawn):
        pacman = Pacman(player_spawn)
        pacman.update(1)
        pygame.event.get()
        group = GhostGroup(pacman, "./levels/ghosts.json", level=5)
        group.start()
        group.sprites()[0].activate()
        group.update(1 / 60)
        group.sprites()[0]._position = pygame.Vector2(2, 2)
        group.sprites()[0]._state = GhostStates.CHASE
        for _ in range(120):
            group.update(1 / 60)
        pygame.event.poll()
        assert pygame.event.poll().type == GAME_OVER

    @pytest.mark.parametrize("player_spawn", [
        pygame.Vector2(1, 1),
        pygame.Vector2(1, 2),
        pygame.Vector2(1, 3),
        pygame.Vector2(1, 5)]
                             )
    def test_pacman_kill_ghost(self, player_spawn):
        pacman = Pacman(player_spawn)
        pacman.set_direction(pygame.Vector2(0, 1))
        group = GhostGroup(pacman, "./levels/ghosts.json", level=5)
        group.start()
        group.sprites()[0].activate()
        group.update(1 / 60)
        group.sprites()[0]._position = pygame.Vector2(1, 8)
        group.sprites()[0]._state = GhostStates.FRIGHTENED
        for _ in range(60):
            pacman.update(1 / 60)
            group.update(1 / 60)
            group.sprites()[0]._position = pygame.Vector2(1, 6)
        assert pacman.get_position() == pygame.Vector2(1, 8)
        assert group.sprites()[0]._state, GhostStates.DEAD

    @pytest.mark.parametrize("player_spawn", [
        pygame.Vector2(1, 1), pygame.Vector2(1, 2),
        pygame.Vector2(4, 1), pygame.Vector2(1, 2),
        pygame.Vector2(6, 1), pygame.Vector2(1, 2),
    ])
    def test_ghost_kill_player(self, player_spawn):
        pacman = Pacman(player_spawn)
        pacman.update(1)
        pygame.event.get()
        group = GhostGroup(pacman, "./levels/ghosts.json", level=5)
        group.start()
        group.sprites()[0].activate()
        group.update(1 / 60)
        group.sprites()[0]._position = pygame.Vector2(2, 2)
        group.sprites()[0]._state = GhostStates.CHASE
        for _ in range(120):
            group.update(1 / 60)
        pygame.event.poll()
        assert pygame.event.poll().type == GAME_OVER
