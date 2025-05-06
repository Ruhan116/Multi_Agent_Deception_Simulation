import csv
from model.Tile import Tile

TILE_SIZE = 16

class TileMap:
    def __init__(self, csv_path, tile_properties=None):
        self.tiles = []  # 2D list of Tile objects
        self.tile_properties = tile_properties or {}

        with open(csv_path) as f:
            reader = csv.reader(f)
            for y, row in enumerate(reader):
                tile_row = []
                for x, val in enumerate(row):
                    tile_id = int(val)
                    props = self.tile_properties.get(tile_id, {})
                    tile = Tile(
                        tile_id,
                        (x * TILE_SIZE, y * TILE_SIZE),
                        is_walkable=props.get("walkable", True),
                        is_task=props.get("task", False)
                    )
                    tile_row.append(tile)
                self.tiles.append(tile_row)
