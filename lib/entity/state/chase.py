import heapq
import math
from .state import EntityState
from typing import Tuple, List
from ...map.map import Map
from ..movement.strategy import MovementStrategy


class EntityChaseState(EntityState):

    def __init__(self, map: Map, player: MovementStrategy, entity: MovementStrategy):
        self.__map = map

    def a_star(self, start, target):
        graph = self.__map.get_graph()
        open_set = []
        heapq.heappush(open_set, (0, start))
        cameFrom = {}
        gScore = {start: 0}
        fScore = {start: math.dist(start, target)}
        while open_set:
            current = heapq.heappop(open_set)[1]
            if current == target:
                path = []
                while current in cameFrom:
                    path.append(current)
                    current = cameFrom[current]
                path.reverse()
                return path
            for neighbor in graph[current]:
                tentative_gScore = gScore[current] + math.dist(current, neighbor)
                if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = tentative_gScore + math.dist(neighbor, target)
                    heapq.heappush(open_set, (fScore[neighbor], neighbor))
        return []

    def update(self):
        pass



    def moving_direction(self, start, target) -> List[Tuple[int, int]]:
        return self.a_star(start, target)
