import pygame
import sys
import random
import time

from gauge import Gauge
from player import Player
from cpu import CPU
# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 600, 800
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
BLACK = (0, 0, 0)
GREEN = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Initialize the game window
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
        pygame.display.set_caption("Drag Racing Game")
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text1 = self.font.render('Player 1 Wins!', True, RED, BLACK)
        self.text2 = self.font.render('Player 2 Wins!', True, GREEN, BLACK)
        self.start3 = self.font.render('3', True, BLACK, RED)
        self.start2 = self.font.render('2', True, BLACK, ORANGE)
        self.start1 = self.font.render('1', True, BLACK, YELLOW)
        self.startgo = self.font.render('GO!', True, BLUE, GREEN)
        self.sextRect = self.text1.get_rect()
        self.textRect = (WIDTH // 2 - 100, HEIGHT // 2)
        self.textRect2 = (WIDTH // 2, HEIGHT // 2)
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.speed = 0
        self.clock = pygame.time.Clock()
        # Create sprites
        self.all_sprites = pygame.sprite.Group() 
        self.gauge = Gauge()
        self.player1 = Player(RED, (WIDTH // 4, HEIGHT // 1.3), (self.gauge.speed))
        self.player2 = CPU(BLUE, (3 * WIDTH // 4, HEIGHT // 1.3))
        self.added_speed = 0
        self.all_sprites.add(self.player1, self.player2, self.gauge)
        self.lose_speed = False
        self.gain_speed = True
        self.dt = 0

    def get_speed(self):
        return self.added_speed
    
    def check_win(self, player):
        if player.rect.top == 0:
            return True
        
    def start_game(self):
        self.display_surface.blit(self.start3, self.textRect2)
        pygame.display.update()
        time.sleep(1)
        self.display_surface.blit(self.start2, self.textRect2)
        pygame.display.update()
        time.sleep(1)
        self.display_surface.blit(self.start1, self.textRect2)  
        pygame.display.update()
        time.sleep(1)
        self.display_surface.blit(self.startgo, self.textRect2)
        pygame.display.update()
        

    # Game loop
    def run(self):
        running = True
        self.start_game()
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

            self.player2.gauge_speed = 1
           
            

            # Update
            self.all_sprites.update()

            if self.check_win(self.player1) == True:
                print("Player 1 Wins!")
                self.display_surface.blit(self.text1, self.textRect)
                pygame.display.update()
                time.sleep(3)
                return
            if self.check_win(self.player2) == True:
                print("Player 2 Wins!")
                self.display_surface.blit(self.text2, self.textRect)
                pygame.display.update()
                time.sleep(3)
                return
            

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