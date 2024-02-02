from abc import ABC, abstractmethod
from typing import List, Union
from pygame import image, sprite, surface

# class MapObject(Enum):
#     EMPTY = 0
#     WALL = 1
#     THIN_WALL = 2
#     ONE_WAY = 3
#     CHERRY = 4
#     strawberry = 5
#     orange = 6
#     apple = 7
#     melon = 8
#     galaxian = 9
#     bell = 10
#     key = 11

class MapObject(ABC, sprite.Sprite):
    def __init__(self, object : image, pos: (int, int)):
        ABC.__init__(self)
        sprite.Sprite.__init__(self)
        self.asset = object

    @abstractmethod
    def render(self, surface: surface.Surface) -> Union[image]:
        pass
    @abstractmethod
    def isCollectable(self) -> bool:
        pass
    @abstractmethod
    def isPassable(self) -> bool:
        pass

class Wall(MapObject):
    def __init__(self, object : image,):
        MapObject.__init__(self, object)
        
    def getAsset(self) -> Union[image]:
        return self.asset
    def getCollectionValue(self) -> int:
        return 1

    def isPassable(self) -> bool:
        return False
    
class ThinWall(MapObject):
    def __init__(self, object : image):
        MapObject.__init__(self, object)
        
    def getAsset(self) -> Union[image]:
        return self.asset
    def getCollectionValue(self) -> int:
        return 2

    def isPassable(self) -> bool:
        return False
    
class OneWay(MapObject):
    def __init__(self, object : image):
        MapObject.__init__(self, object)
        
    def getAsset(self) -> Union[image]:
        return self.asset
    def getCollectionValue(self) -> int:
        return 3

    def isPassable(self) -> bool:
        return False
