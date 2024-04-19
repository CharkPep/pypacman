import pygame
from lib.map.parser import TiledMapParser
from lib.map.map import GameMap
import pytest


@pytest.fixture(autouse=True)
def map():
    TiledMapParser(layers="./levels/original.json").parse((800, 800))
    return GameMap()
