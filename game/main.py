import pygame
from model.Player import Player
from view.PlayerView import PlayerView
from controller.PlayerController import PlayerController
from model.Tilemap import TileMap
from view.TileMapView import TileMapView
from controller.TileController import TileController



pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


tilemap = TileMap(r"assets\map\amogus.csv") 
tilemap_view = TileMapView(tilemap)

tilemap = TileMap("assets/map/amogus.csv")
tilemap_controller = TileController(tilemap)

player = Player("Player1", (100, 100), is_impostor=False)
player_view = PlayerView(player)
player_controller = PlayerController(player, tile_controller=tilemap_controller)

while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_controller.handle_input(dt)
    
    screen.fill("black")
    tilemap_view.draw(screen)
    player_view.draw(screen)
    pygame.display.flip()

pygame.quit()