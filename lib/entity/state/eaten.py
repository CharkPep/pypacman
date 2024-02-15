from .state import EntityState
import pygame
from ...map.map import Map
from ...map.tile import OneWay


class EatenState(EntityState):

    def __init__(self, entity_image: pygame.image, map: Map):
        self._entity_image = entity_image
        for i in range(len(map.get_map())):
            for j in range(len(map.get_map()[i])):
                if isinstance(map.get_map()[i][j], OneWay):
                    self._target = (i, j)

    def handle_event(self, event):
        pass 

    def next(self):
        pass

    def get_target(self):
        return self._target




