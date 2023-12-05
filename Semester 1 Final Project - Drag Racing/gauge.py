import pygame
import sys
import random
import math

pygame.init()
WIDTH, HEIGHT = 600, 800
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Gauge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.radius = 60
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 1000)  # Adjusted position
        self.speed = 0
        self.mark_length = 10
        

    def update(self):
        self.rect.y += self.speed

        # Ensure the gauge stays within the screen boundaries
        if self.rect.top < HEIGHT // 2:
            self.rect.top = HEIGHT // 2
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
    
    def draw_speed_marks(self):
        for speed in range(0, 101, 10):
            angle = math.radians(180 - speed * 1.8)  # Convert speed to angle
            x = int(self.radius * math.cos(angle))
            y = int(self.radius * math.sin(angle))
            pygame.draw.line(self.image, WHITE, (self.radius, self.radius), (self.radius + x, self.radius - y), 2)
            pygame.draw.line(self.image, WHITE, (self.radius, self.radius), (self.radius - x, self.radius - y), 2)