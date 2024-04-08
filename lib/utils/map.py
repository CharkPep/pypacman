from lib.map.map import GameMap
import pygame


def is_walkable(position):
    # print(position, GameMap().get_tile(position).props.get("walkable", False))
    return GameMap().get_tile(position).kwargs.get("walkable", False)


def is_intersection(position):
    return sum([is_walkable(position + direction) for direction in
                [pygame.Vector2(0, 1), pygame.Vector2(0, -1), pygame.Vector2(1, 0), pygame.Vector2(-1, 0)]]) >= 2
