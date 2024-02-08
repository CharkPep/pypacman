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

    def spawn_player(self):
        map = self.map.get_map()
        for line in map:
            for row in line:
                if isinstance(row, tile.PlayerSpawn):
                    self.player = player.Player(None, pygame.rect.Rect(row.get_rect()))