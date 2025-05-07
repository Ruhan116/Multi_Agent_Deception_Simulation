import pygame
from controller.GameStateController import GameStateController

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

game = GameStateController()

while game.running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        game.get_state().handle_event(event)

    game.get_state().update(dt)
    game.get_state().draw(screen)

    pygame.display.flip()

pygame.quit()
