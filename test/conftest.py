import os

import pygame
from lib.map.parser import TiledMapParser
from lib.map.map import GameMap
import pytest


@pytest.fixture(autouse=True)
def initialize_pygame():
    pygame.init()
    yield
    pygame.quit()


@pytest.fixture(autouse=True)
def map():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(os.path.join(current_dir, ".."))
    TiledMapParser(layers="./levels/original.json").parse((800, 800))
    return GameMap()
