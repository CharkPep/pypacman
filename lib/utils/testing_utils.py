from lib.map.map import GameMap
from lib.map.tile import *
import pytest
import math

# Pixel size of a tile
TILE_SIZE = (16, 16)


# 16x16 empty map
@pytest.fixture(scope="function")
def empty_map():
    map = [Void((j * TILE_SIZE[0], i * TILE_SIZE[1]), TILE_SIZE, None) for i in range(16) for j in range(16)]
    map = GameMap([map[i:i + 16] for i in range(0, len(map), 16)])
    GameMap.set_instance(map)


# 16x16 map with walls on the edges
@pytest.fixture(scope="function")
def map_with_walls():
    map = [Void((j * TILE_SIZE[0], i * TILE_SIZE[1]), TILE_SIZE, None) for i in range(16) for j in range(16)]
    map = [map[i:i + 16] for i in range(0, len(map), 16)]
    for i in range(16):
        map[i][0] = VerticalWall((i, 0), TILE_SIZE, None)
        map[i][15] = VerticalWall((i, 9), TILE_SIZE, None)

    for i in range(16):
        map[0][i] = HorizontalWall((0, i), TILE_SIZE, None)
        map[15][i] = HorizontalWall((9, i), TILE_SIZE, None)

    map = GameMap(map)
    GameMap.set_instance(map)


# Map with a horizontal passage in the middle
@pytest.fixture(scope="function")
def map_with_passages():
    map = [Void((j * TILE_SIZE[0], i * TILE_SIZE[1]), TILE_SIZE, None) for i in range(16) for j in range(16)]
    for i in range(1, 15):
        map[7][i] = HorizontalWall((7, i), TILE_SIZE, None)
        map[9][i] = HorizontalWall((7, i), TILE_SIZE, None)
    map = GameMap(map)
    GameMap.set_instance(map)


def calculate_updates_to_reach_target(target: pygame.Vector2, start: pygame.Vector2, velocity: int):
    return math.dist(GameMap.get_instance().get_tile(target).get_rect().center,
                     GameMap.get_instance().get_tile(start).get_rect().center) / velocity * 60
