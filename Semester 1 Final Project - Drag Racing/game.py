import pygame
import sys
import random


from gauge import Gauge
from player import Player
# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 600, 800
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 0)


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Initialize the game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Drag Racing Game")

        self.image = pygame.Surface((25, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 4, HEIGHT // 2)
        self.speed = 0
        self.clock = pygame.time.Clock()
        # Create sprites
        self.all_sprites = pygame.sprite.Group()
        self.player1 = Player(RED, (WIDTH // 4, HEIGHT // 1.3))
        self.player2 = Player(BLUE, (3 * WIDTH // 4, HEIGHT // 1.3))
        self.gauge = Gauge()
        self.all_sprites.add(self.player1, self.player2, self.gauge)

    # Game loop
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            # Update
            self.all_sprites.update()

            # Check for collision between player and gauge
            if pygame.sprite.collide_rect(self.player1, self.gauge):
                self.player1.speed = self.gauge.speed
            else:
                self.player1.speed = self.gauge.speed

            if pygame.sprite.collide_rect(self.player2, self.gauge):
                self.player2.speed = self.gauge.speed
            else:
                self.player2.speed = self.gauge.speed

            # Draw
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)
            self.gauge.draw_speed_marks()

            # Draw a center line
            pygame.draw.line(self.screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT - 150), 5)

            pygame.display.flip()
            

        # Quit the game
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pm = Game()
    pm.run()