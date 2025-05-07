import pygame
from model.Player import Player
from view.PlayerView import PlayerView
from controller.PlayerController import PlayerController
from model.Tilemap import TileMap
from view.TileMapView import TileMapView
from controller.TileController import TileController
from model.GameState import GameState
from controller.GameStateController import GameStateController

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

game_state = GameStateController()

tilemap = TileMap(r"assets\map\amogus.csv") 
tilemap_view = TileMapView(tilemap)
tilemap_controller = TileController(tilemap)

player = Player("Player1", (100, 100), is_impostor=False)
player_view = PlayerView(player)
player_controller = PlayerController(player, tile_controller=tilemap_controller)

while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_state.is_state(GameState.MENU):  
                    game_state.change_state(GameState.PLAYING)  

    if game_state.is_state(GameState.PLAYING):
        player_controller.handle_input(dt)
    elif game_state.is_state(GameState.MENU):
        pass
    
    screen.fill("black")
    
    if game_state.is_state(GameState.PLAYING):
        tilemap_view.draw(screen)
        player_view.draw(screen)
    elif game_state.is_state(GameState.MENU):
        font = pygame.font.SysFont(None, 72)
        text = font.render("AMONG US CLONE - PRESS ENTER TO PLAY", True, (255, 255, 255))
        screen.blit(text, (screen.get_width()//2 - text.get_width()//2, 
                        screen.get_height()//2 - text.get_height()//2))
    
    pygame.display.flip()  

pygame.quit()