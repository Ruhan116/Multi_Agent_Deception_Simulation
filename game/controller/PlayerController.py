import pygame
import pygame
from model.Player import Player

class PlayerController:
    def __init__(self, player, tile_controller=None):
        self.player = player
        self.tile_controller = tile_controller

    def handle_input(self, dt):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        speed = self.player.velocity * dt
        if keys[pygame.K_w]:
            dy = -speed
        elif keys[pygame.K_s]:
            dy = speed
        if keys[pygame.K_a]:
            dx = -speed
        elif keys[pygame.K_d]:
            dx = speed

        # Handle horizontal movement
        if dx != 0:
            new_x = self.player.position[0] + dx
            new_rect_x = pygame.Rect(
                new_x,
                self.player.position[1],
                self.player.size[0],
                self.player.size[1]
            )
            if self.tile_controller is None or self.tile_controller.is_walkable_rect(new_rect_x):
                self.player.position[0] = new_x

        # Handle vertical movement
        if dy != 0:
            new_y = self.player.position[1] + dy
            new_rect_y = pygame.Rect(
                self.player.position[0],  # Uses potentially updated x position
                new_y,
                self.player.size[0],
                self.player.size[1]
            )
            if self.tile_controller is None or self.tile_controller.is_walkable_rect(new_rect_y):
                self.player.position[1] = new_y