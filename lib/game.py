from .map import map
from .entity import entity
import pygame 
class Game:
    def __init__(self, map: map.Map, entities: entity.Entity, player : entity.Player):
        self.map = map
        self.entities = entities

    def render(self, surface: pygame.surface.Surface):
        self.map.render(surface)
        self.entities.move()


    def spawnPlayer(self):
        pass