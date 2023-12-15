import pygame
import sys
import time
from gauge import Gauge
from player import Player
from cpu import CPU
from fsm import FSM

# Constants
WIDTH, HEIGHT = 600, 800
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
ACCELERATING = 0
DECELERATING = 1

class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Initialize the game window, ChatGPT assisted
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
        pygame.display.set_caption("Drag Racing Game")
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text1 = self.font.render('Player 1 Wins!', True, BLUE, BLACK)
        self.text2 = self.font.render('Player 2 Wins!', True, RED, BLACK)
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
        
        # Create sprites, ChatGPT assisted
        self.all_sprites = pygame.sprite.Group() 
        self.gauge = Gauge()
        self.player1 = Player(RED, (WIDTH // 4, HEIGHT // 1.3), (self.gauge.speed))
        self.player2 = CPU(BLUE, (3 * WIDTH // 4, HEIGHT // 1.3))
        self.added_speed = 0
        self.all_sprites.add(self.player1, self.player2, self.gauge)
        self.lose_speed = False
        self.gain_speed = True
        self.dt = 0
        self.fsm = FSM(ACCELERATING)
        self.test = "test"
        self.test1 = "test1"
        self.init_fsm()
        self.state = ACCELERATING
        self.accelerate()
        self.bg = pygame.image.load("dragracingbackground.png")
        pygame.display.flip()



    #initialize FSM
    def init_fsm(self):
        self.fsm.add_transition("test", ACCELERATING, self.decelerate, DECELERATING)
        self.fsm.add_transition("test3", ACCELERATING, self.accelerate, ACCELERATING)
        self.fsm.add_transition("test3", DECELERATING, self.decelerate, DECELERATING)
        self.fsm.add_transition("test1", DECELERATING, self.accelerate, ACCELERATING)

    #method for increase CPU speed
    def accelerate(self):
        self.speed += 0.5

    #method for decrease CPU speed
    def decelerate(self):
        self.speed -= 0.25


    #starts a countdown for the game to start
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

    #checks if the game has been won by either player or the CPU
    def check_win(self, player):
        return player.rect.top == 0

    #main run function, ChatGPT assisted
    def run(self):
        running = True
        self.start_game()

        while running:
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
                if self.gain_speed:
                    self.gauge.increase_speed()
                    self.gain_speed = False
                elif self.lose_speed:
                    self.gauge.decrease_speed()
                    self.lose_speed = False
                else:
                    self.gauge.decrease_speed()

                self.player1.gauge_speed = self.gauge.speed
                self.dt = 0

            if self.player1.gauge_speed > 0:
                self.player1.gauge_speed = self.gauge.speed

            self.player2.gauge_speed = 1

            if self.speed >= 2:
                print("1", self.speed)
                self.fsm.process(self.test)
                # pygame.display.flip()
            elif self.speed <= 0:
                print("2", self.speed)
                self.fsm.process(self.test1)
                # pygame.display.flip()
            else:
                self.fsm.process("test3")
            self.player2.rect.y -= self.speed
            # print(self.speed)

            self.player2.rect.y -= self.speed

            if self.player1.rect.top < 0:
                self.player1.rect.top = 0
            elif self.player1.rect.bottom > HEIGHT:
                self.player1.rect.bottom = HEIGHT
            if self.player2.rect.top < 0:
                self.player2.rect.top = 0
            elif self.player2.rect.bottom > HEIGHT:
                self.player2.rect.bottom = HEIGHT

            self.all_sprites.update()

            if self.check_win(self.player1):
                print("Player 1 Wins!")
                self.display_surface.blit(self.text1, self.textRect)
                pygame.display.update()
                time.sleep(3)
                return
            if self.check_win(self.player2):
                print("Player 2 Wins!")
                self.display_surface.blit(self.text2, self.textRect)
                pygame.display.update()
                time.sleep(3)
                return

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.bg, (0, 0))
            self.all_sprites.draw(self.screen)
            self.gauge.draw_circle()
            self.gauge.draw_gauge()
            pygame.display.flip()
            self.gauge.draw_needle()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
