class Tile:
    def __init__(self, tile_id, position, is_walkable=True, is_task=False):
        self.tile_id = tile_id
        self.position = position  # (x, y) in pixels
        self.is_walkable = is_walkable
        self.is_task = is_task
