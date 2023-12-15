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
    def __init__(self, color, start_position, gauge_speed):
        super().__init__()
        #self.image = pygame.Surface((25, 50))
        self.image = pygame.image.load("purplecar.png")
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.start_position = (self.x, self.y)
        self.rect.center = start_position
        self.gauge_speed = gauge_speed

    def update(self):
        self.rect.y -= self.gauge_speed

        # Ensure the player stays within the screen boundaries
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        




