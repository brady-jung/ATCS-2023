import pygame
import sys
import math

# Constants
WIDTH, HEIGHT = 600, 800
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
accelerating = 0
decelerating = 1

pygame.init()

class CPU(pygame.sprite.Sprite):
    def __init__(self, color, start_position):
            super().__init__()
            self.image = pygame.Surface((25, 50))
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.x = 0
            self.y = 0
            self.start_position = (self.x, self.y)
            self.rect.center = start_position
            self.speed = 1  # Initial speed for the opponent
            self.state = accelerating  # Initial state

    def update(self):
        if self.state == accelerating:
            self.speed += 0.1
            if self.speed >= 2:  # Maximum speed
                self.speed = 2
                self.state = decelerating
        elif self.state == decelerating:
            self.speed -= 0.1
            if self.speed <= 0:  # Minimum speed
                self.speed = 0
                self.state = accelerating

        self.rect.y -= self.speed

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT