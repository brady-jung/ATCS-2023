import pygame
import sys
import random
import math

pygame.init()
WIDTH, HEIGHT = 600, 800
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)


class Gauge(pygame.sprite.Sprite):
    #initialize gauge, used to show the users speed, ChatGPT assisted
    def __init__(self):
        super().__init__() 
        self.radius = 60
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 1000)  # Adjusted position
        self.speed = 0
        self.mark_length = 10
        self.needle_length = self.radius - 10  # Adjust needle length
        self.needle_color = RED
        self.border_color = WHITE
        self.border_width = 3
        self.green_slice_angle = 70
        self.red_slice_angle = 85
        self.orange_slice_angle = 100
    
    #increases speed    
    def increase_speed(self):
        self.speed += 0.1
    
    #decreases speed
    def decrease_speed(self):
        if self.speed > 0:
            self.speed -= 0.1

    #updates the gauge with the needle at a different position based on speed
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
    
    def draw_needle(self):
        angle = math.radians(180 - self.speed * 25 * 1.8)  # Convert speed to angle
        x = int(self.needle_length * math.cos(angle))
        y = int(self.needle_length * math.sin(angle))
        pygame.draw.line(self.image, self.needle_color, (self.radius, self.radius), (self.radius + x, self.radius - y), 3)

    def draw_border(self):
        pygame.draw.circle(self.image, self.border_color, (self.radius, self.radius), self.radius, self.border_width)
    
    def draw_green_slice(self):
        start_angle = math.radians(180 - self.green_slice_angle * 1.8)
        end_angle = math.radians(180)
        pygame.draw.arc(self.image, GREEN, self.image.get_rect(), start_angle, end_angle, self.border_width)

    def draw_orange_slice(self):
        start_angle = math.radians(180 - self.orange_slice_angle * 1.8)
        end_angle = math.radians(180)
        pygame.draw.arc(self.image, ORANGE, self.image.get_rect(), start_angle, end_angle, self.border_width)

    def draw_red_slice(self):
        start_angle = math.radians(180 - self.red_slice_angle * 1.8)
        end_angle = math.radians(180)
        pygame.draw.arc(self.image, RED, self.image.get_rect(), start_angle, end_angle, self.border_width)

    def draw_circle(self):
        pygame.draw.circle(self.image, BLACK, (self.radius, self.radius), self.radius)

    def draw_gauge(self):
        self.draw_speed_marks()
        self.draw_border()
        self.draw_orange_slice()
        self.draw_red_slice()
        self.draw_green_slice()