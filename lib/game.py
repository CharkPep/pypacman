from .map import map as Map, tile
from .entity import entity, player
from typing import List
import pygame


class Game:
    map: Map.Map = None
    entities: List[entity.Entity] = []

    def set_map(self, map: Map.Map):
        self.map = map

    def render(self, surface: pygame.surface.Surface):
        self.map.render(surface)
        for entity in self.entities:
            entity.update()
            entity.render(surface)

    def spawn_player(self):
        for i in range(len(self.map.map)):
            for j in range(len(self.map.map[i])):
                if isinstance(self.map.map[i][j], tile.PlayerSpawn):
                    self.entities.append(player.Player(None, (i, j), self.map))