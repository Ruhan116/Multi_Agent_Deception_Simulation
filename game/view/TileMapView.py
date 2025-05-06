import pygame

TILE_SIZE = 16

class TileMapView:
    def __init__(self, tilemap):
        self.tilemap = tilemap

    def draw(self, surface):
        for row in self.tilemap.tiles:
            for tile in row:
                x, y = tile.position
                color = self._get_tile_color(tile.tile_id)
                pygame.draw.rect(surface, color, (x, y, TILE_SIZE, TILE_SIZE))

    def _get_tile_color(self, tile_id):
        if tile_id == 3759:
            return "black"
        elif tile_id == 4883:
            return "white"
        else:
            return "blue"
