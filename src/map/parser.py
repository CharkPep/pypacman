import os
import object
from pygame import image, sprite, surface
from typing import List, Union
from map import Map
from enum import Enum

class MapObjectEnum(Enum):
    WALL = 0
    VOID = 1
    THIN_WALL = 2


class MapParser:
    def __init__(self,
                mapPath="assets/default.txt",
                wallsPath="assets/wall.png",
                thinWallsPath="assets/thinWall.png",
                voidPath="assets/void.png",
                oneWayPath="assets/oneWay.png",
                cherryPath="assets/cherry.png"
        ):
        if wallsPath is None:
            raise ValueError("wallsPath cannot be None")
        if thinWallsPath is None:
            raise ValueError("thinWallsPath cannot be None")
        if voidPath is None:
            raise ValueError("voidPath cannot be None")
        if oneWayPath is None:
            raise ValueError("oneWayPath cannot be None")
        if cherryPath is None:
            raise ValueError("cherryPath cannot be None")
        self.assetsPath = {
            "wallsPath" : wallsPath,
            "thinWallsPath" : thinWallsPath,
            "voidPath" : voidPath,
            "oneWayPath" : oneWayPath,
            "cherryPath" : cherryPath,
        }

    def parse(self, filepath : str) -> Map:
        """
        :param filepath(str): path to map file.
        :return Map: list of lists of game assets, different parsers can use different assets. 
        """
        file = os.open(filepath, os.O_RDONLY)
        fileContent = os.read(file, os.stat(filepath).st_size)
        os.close(file)
        fileContent = fileContent.decode("utf-8")
        fileContent = fileContent.split("\n")
        map = []
        for line in fileContent:
            for row in line:
                match row:
                    case "0":
                        map.append(MapObjectEnum.WALL)
                    case "1":
                        map.append(object.Wall())
                    case _:
                        raise ValueError("Invalid map file")
    def __loadAssets(self) -> dict[image]:
        self.assets = {
            "walls" : image.load(self.assetsPath["wallsPath"]),
            "thinWalls" : image.load(self.assetsPath["thinWallsPath"]),
            "void" : image.load(self.assetsPath["voidPath"]),
        } 