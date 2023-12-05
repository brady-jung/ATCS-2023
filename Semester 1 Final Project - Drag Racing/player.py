import pygame
import sys
import random


from gauge import Gauge
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 800
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self, color, start_position):
        super().__init__()
        self.image = pygame.Surface((25, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = start_position
        self.speed = 0

    def update(self):
        self.rect.y += self.speed

        # Ensure the player stays within the screen boundaries
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT




