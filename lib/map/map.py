import pygame.surface
from .tile import Tile
from lib.utils.singleton import SingletonMeta


class GameMap(metaclass=SingletonMeta):
    layers = None

    def __init__(self, **props):
        """
        :param layers: list of layers, layers must be the same size
        :param tile_set: Tileset used to blit tiles on the screen as tile by itself does not contain image
        :param props:  dictionary of properties
        :param width: int, width of the map in tiles
        :param height: int, height of the map in tiles
        """
        self.layers = props["layers"]
        self.background = props["background"]
        self.props = {}
        for prop in props["properties"]:
            self.props[prop["name"]] = prop["value"]
        self.width = props["width"]
        self.height = props["height"]

    def reset(self):
        for tile in self.layers[1]:
            if tile.id != 0:
                tile.kwargs["render"] = True

    def render(self, surface: pygame.surface.Surface):
        if self.background is not None:
            surface.blit(self.background, (0, 0))
        for layer in self.layers:
            for tile in layer:
                tile.render(surface)

    def clamp_position(self, position: pygame.Vector2):
        x = max(0, min(position.x, self.width - 1))
        y = max(0, min(position.y, self.height - 1))
        return pygame.Vector2(x, y)

    def get_tile(self, position: pygame.Vector2, layer=0) -> Tile:
        position = self.clamp_position(position)
        return self.layers[layer][int(position.y * self.width + position.x)]
