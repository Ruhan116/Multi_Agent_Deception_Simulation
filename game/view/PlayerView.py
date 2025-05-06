import pygame


class PlayerView:
    def __init__(self, player):
        self.player = player

    def draw(self, screen):
        print(f"Drawing player at position: {self.player.position}")
        color = (255, 0, 0) if self.player.is_impostor else (0, 255, 0)
        width, height = self.player.size
        rect = pygame.Rect(self.player.position[0], self.player.position[1], width, height)
        pygame.draw.rect(screen, color, rect)
