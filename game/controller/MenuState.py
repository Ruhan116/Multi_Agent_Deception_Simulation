import pygame
from model.GameState import GameState

class MenuState:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont(None, 72)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.game.change_state(GameState.PLAYING)

    def update(self, dt):
        pass  

    def draw(self, screen):
        screen.fill("black")
        text = self.font.render("AMONG US CLONE - PRESS ENTER TO PLAY", True, (255, 255, 255))
        screen.blit(
            text,
            (screen.get_width() // 2 - text.get_width() // 2,
             screen.get_height() // 2 - text.get_height() // 2)
        )
