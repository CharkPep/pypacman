from lib.utils.testing_utils import *
from lib.entity.entity import Entity, DEFAULT_VELOCITY


class TestEntity:
    Entity.__abstractmethods__ = set()

    class Dummy(Entity):
        def __int__(self, position, velocity):
            super().__init__(position, velocity)

    def test_entity_crossing_map_edge(self, empty_map):
        assert True

    def test_entity_move_in_direction(self, empty_map):
        assert True

    @pytest.mark.parametrize("spawn,direction,expected", [
        (pygame.Vector2(1, 1), pygame.Vector2(1, 0), pygame.Vector2(2, 1)),
        (pygame.Vector2(1, 1), pygame.Vector2(0, -1), pygame.Vector2(1, 1)),
        (pygame.Vector2(1, 1), pygame.Vector2(0, 1), pygame.Vector2(1, 2)),
        (pygame.Vector2(1, 1), pygame.Vector2(-1, 0), pygame.Vector2(1, 1)),
    ])
    def test_should_update_entity(self, spawn, direction, expected, map_with_walls):
        entity = self.Dummy(spawn)
        entity.set_direction(direction)
        print(GameMap.get_instance().get_tile(spawn + direction))
        for _ in range(int(calculate_updates_to_reach_target(spawn + direction, spawn, entity._velocity)) + 3):
            entity.update(1 / 60)

        assert entity.___position == expected

    @pytest.mark.parametrize("spawn, offset,direction,expected", [
        (pygame.Vector2(1, 1), pygame.Vector2(0, -TILE_SIZE[0] / 2), pygame.Vector2(1, 0),
         False),
        (pygame.Vector2(1, 1), pygame.Vector2(0, -TILE_SIZE[0]), pygame.Vector2(1, 0),
         True),
    ])
    def test_check_if_target_reached(self, spawn, offset, direction, expected):
        entity = self.Dummy(spawn)
        entity.rect.move_ip(offset)
        print(entity.rect.center)
        print(GameMap.get_instance().get_tile(spawn + direction).get_rect().center)
        entity.set_direction(direction)
        assert entity.__move_position_if_target_reached() == expected
