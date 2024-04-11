import os.path
import xml.etree.ElementTree as ET
import pygame


class TileSet:
    """
    Used to parse and store information and properties of tile from props Path,
    TileSet does not initialize the Tile object, it only stores the information about the tile.
    """

    def __init__(self, props, tile_size, **kwargs):
        """
        :param pros: Path to xml file with tile properties
        :param tile_size: Tuple[int, int]
        """

        self.kwargs = kwargs
        self.resolution = tile_size
        with open(props) as file:
            self.root = ET.parse(file).getroot()

        img = self.root.find("./image").get("source", None)
        if img is None:
            raise ValueError("tilesheet not found")

        self.image = pygame.image.load(os.path.join(os.path.dirname(props), img))
        self.tiles: dict[int, any] = {
            # empty tile, props can be added if id in properties file is set to -1
            0: {
                "img": None,
            }
        }

        self._parse_tiles()
        self._parse_props()

    def _parse_props(self):
        for tile in self.root.findall("./tile"):
            id = int(tile.attrib["id"]) + 1
            for child in tile.findall("./properties/property"):
                if child.attrib["type"] == "bool":
                    self.tiles[id][child.attrib["name"]] = child.attrib["value"] == "true"
                    continue
                if child.attrib["type"] == "int":
                    self.tiles[id][child.attrib["name"]] = int(child.attrib["value"])
                    continue
                self.tiles[id][child.attrib["name"]] = child.attrib["value"]

    def _parse_tiles(self):
        columns = int(self.root.get("columns"))
        tile_px = int(self.root.get("tilewidth")), int(self.root.get("tileheight"))
        for i in range(len(self.root.findall("./tile")) // columns):
            for j in range(columns):
                self.tiles[i * columns + j + 1] = {
                    "img": pygame.transform.scale(self.image.subsurface(
                        (j * tile_px[0], i * tile_px[1], tile_px[0], tile_px[1])), self.resolution)
                }

    def get_tile(self, tile_code):
        """
        Return an object that describes the tile with tile_code.

        :param tile_code: int
        :return: Object[str, Any]
        """
        return self.tiles[tile_code]
