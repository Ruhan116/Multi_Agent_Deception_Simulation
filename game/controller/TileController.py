import pygame

TILE_SIZE = 16
WALL_ID = 3759

class TileController:
    def __init__(self, tilemap):
        self.tilemap = tilemap

    def is_walkable_rect(self, rect: pygame.Rect) -> bool:
        # Get the tile indices overlapped by the player's rectangle
        left = rect.left // TILE_SIZE
        right = rect.right // TILE_SIZE
        top = rect.top // TILE_SIZE
        bottom = rect.bottom // TILE_SIZE

        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                # Bounds check
                if row < 0 or col < 0 or row >= len(self.tilemap.tiles) or col >= len(self.tilemap.tiles[0]):
                    return False  # treat out-of-bounds as solid
                tile = self.tilemap.tiles[row][col]
                if tile.tile_id == WALL_ID:
                    return False
        return True
