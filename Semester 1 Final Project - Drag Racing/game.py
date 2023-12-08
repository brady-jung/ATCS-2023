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
BLACK = (0, 0, 0)


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Initialize the game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Drag Racing Game")

        self.speed = 0
        self.clock = pygame.time.Clock()
        # Create sprites
        self.all_sprites = pygame.sprite.Group()
        self.gauge = Gauge()
        self.player1 = Player(RED, (WIDTH // 4, HEIGHT // 1.3), (self.gauge.speed))
        self.player2 = Player(BLUE, (3 * WIDTH // 4, HEIGHT // 1.3), 0)
        self.added_speed = 0
        self.all_sprites.add(self.player1, self.player2, self.gauge)
        self.lose_speed = False
        self.gain_speed = True
        self.dt = 0

    def get_speed(self):
        return self.added_speed


    # Game loop
    def run(self):
        running = True
        while running:
            print(self.gauge.speed)
            self.dt += self.clock.tick(120)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.gain_speed = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.lose_speed = True
            
            if self.dt > 120:
                if self.gain_speed == True:
                    self.gauge.increase_speed()
                    self.gain_speed = False
                elif self.lose_speed == True:
                    self.gauge.decrease_speed()
                    self.lose_speed = False
                else:
                    self.gauge.decrease_speed()
                    self.lose_speed = False

                self.player1.gauge_speed = self.gauge.speed
                self.dt = 0

            if self.player1.gauge_speed > 0:
                self.player1.gauge_speed = self.gauge.speed

            self.player2.gauge_speed = 0
           
            

            # Update
            self.all_sprites.update()

            # Draw
            self.screen.fill((0, 0, 0))

            # Draw a center line
            pygame.draw.line(self.screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT - 150), 5)
            self.all_sprites.draw(self.screen)
            self.gauge.draw_circle()
            self.gauge.draw_gauge()
            pygame.display.flip()
            self.gauge.draw_needle()

            

        # Quit the game
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pm = Game()
    pm.run()