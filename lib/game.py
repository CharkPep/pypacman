from .map import map as Map, tile
from .entity import entity, player, point
from .entity.movement import TileBasedMovement
from typing import List, Tuple
import pygame


class Game:
    map: Map.Map = None
    entities: List[entity.Entity] = []
    __player = None
    font: pygame.font.Font = None
    score = 0

    def __init__(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def set_map(self, map: Map.Map):
        self.map = map

    def render(self, surface: pygame.surface.Surface):
        surface.fill((0, 0, 0))

        img = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.map.render(surface)
        for entity in self.entities:
            entity.update()
            entity.render(surface)
        self.__player.update()
        self.__check_score()
        self.__player.render(surface)
        surface.blit(img, (10, 10))

    def spawn_score(self, file_path: str, score: int):
        with open(file_path, 'r') as file:
            matrix = [[int(char) for char in line.strip()] for line in file if line.strip()]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    position_on_map = self.map.get_map()[i][j].get_rect()
                    self.entities.append(point.Score(score, position_on_map, self.font))

    def __check_score(self):
        for entity in self.entities:
            if isinstance(entity, point.Score):
                if entity.get_rect().colliderect(self.__player.get_rect()):
                    self.score += entity.get_score()
                    self.entities.remove(entity)

    def spawn_player(self):
        for i in range(len(self.map.map)):
            for j in range(len(self.map.map[i])):
                if isinstance(self.map.map[i][j], tile.PlayerSpawn):
                    self.__player = player.Player(None, pygame.rect.Rect(self.map.map[i][j].get_rect()), 
                                                  TileBasedMovement(self.map, (i, j)))