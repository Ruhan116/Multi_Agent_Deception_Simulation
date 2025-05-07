from model.Player import Player
from view.PlayerView import PlayerView
from controller.PlayerController import PlayerController
from model.Tilemap import TileMap
from view.TileMapView import TileMapView
from controller.TileController import TileController
import pygame

class PlayingState:
    def __init__(self, game):
        self.game = game

        self.tilemap = TileMap(r"assets/map/amogus.csv")  
        self.tilemap_view = TileMapView(self.tilemap)
        self.tilemap_controller = TileController(self.tilemap)

        self.player = Player("Player1", (100, 100), is_impostor=False)
        self.player_view = PlayerView(self.player)
        self.player_controller = PlayerController(self.player, self.tilemap_controller)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.game.running = False

    def update(self, dt):
        self.player_controller.handle_input(dt)

    def draw(self, screen):
        screen.fill("black")
        self.tilemap_view.draw(screen)
        self.player_view.draw(screen)
