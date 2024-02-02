from typing import List, Union
from object import MapObject

class Map:
    def __init__(self, map: List[List[MapObject]]):
        self.map = map
        
    def getMap(self) -> List[List[MapObject]]:
        pass
    def render(self, surface):
        pass
