from .ghost import GhostMovement



class FrightenedMovement(GhostMovement):
    def __init__(self, current_state: StateManager, map: Map, entity: pygame.rect.Rect, current_tile: Tuple[int, int]):
        super().__init__(map, entity, current_tile, current_state)
