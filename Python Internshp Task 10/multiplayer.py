import pygame
import random
import time
from tkinter import messagebox

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class MultiPlayerSnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game - Multiplayer')
        self.clock = pygame.time.Clock()
        self.running = True

        self.snake1 = [(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)]
        self.snake2 = [(3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)]

        self.obstacles = self.generate_obstacles()

        self.direction1 = (1, 0)  
        self.direction2 = (-1, 0)

        self.food1 = self.generate_food()
        self.food2 = self.generate_food()
        self.score1 = 0
        self.score2 = 0

        self.font = pygame.font.Font(None, 36)  

    def generate_food(self):
        while True:
            x = random.randrange(0, SCREEN_WIDTH, CELL_SIZE)
            y = random.randrange(0, SCREEN_HEIGHT, CELL_SIZE)
            if (x, y) not in self.snake1 and (x, y) not in self.snake2 and (x, y) not in self.obstacles:
                return x, y

    def generate_obstacles(self):
        obstacles = []
        for _ in range(10):
            while True:
                x = random.randrange(0, SCREEN_WIDTH, CELL_SIZE)
                y = random.randrange(0, SCREEN_HEIGHT, CELL_SIZE)
                if (x, y) not in self.snake1 and (x, y) not in self.snake2 and (x, y) not in obstacles:
                    obstacles.append((x, y))
                    break
        return obstacles

    def draw_snake(self, snake, color):
        for segment in snake:
            pygame.draw.rect(self.screen, color, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    def draw_food(self, food, color):
        pygame.draw.rect(self.screen, color, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            pygame.draw.rect(self.screen, BLUE, (obstacle[0], obstacle[1], CELL_SIZE, CELL_SIZE))

    def draw_clock(self):
        current_time = time.strftime('%I:%M:%S %p')
        text_surface = self.font.render(current_time, True, WHITE)
        self.screen.blit(text_surface, (10, 10))

    def draw_score(self):
        score1_text = f'Player (Green) Score: {self.score1}'
        score2_text = f'Player (Red) Score: {self.score2}'
        text_surface1 = self.font.render(score1_text, True, WHITE)
        text_surface2 = self.font.render(score2_text, True, WHITE)
        text_rect1 = text_surface1.get_rect()
        text_rect2 = text_surface2.get_rect()
        text_rect1.topright = (SCREEN_WIDTH - 10, 10)
        text_rect2.topright = (SCREEN_WIDTH - 10, 40)
        self.screen.blit(text_surface1, text_rect1)
        self.screen.blit(text_surface2, text_rect2)

    def move_snake(self, snake, direction):
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = ((head_x + dx * CELL_SIZE) % SCREEN_WIDTH, (head_y + dy * CELL_SIZE) % SCREEN_HEIGHT)

        snake.insert(0, new_head)
        
        self.check_collision(self.snake1, self.snake2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.direction1 = (0, -1)
                elif event.key == pygame.K_s:
                    self.direction1 = (0, 1)
                elif event.key == pygame.K_a:
                    self.direction1 = (-1, 0)
                elif event.key == pygame.K_d:
                    self.direction1 = (1, 0)
                elif event.key == pygame.K_UP:
                    self.direction2 = (0, -1)
                elif event.key == pygame.K_DOWN:
                    self.direction2 = (0, 1)
                elif event.key == pygame.K_LEFT:
                    self.direction2 = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.direction2 = (1, 0)

    def check_collision(self, snake1, snake2):
        if snake1[0] in self.obstacles:
            self.game_over("Player (Green) hit an obstacle!")
        
        if snake2[0] in self.obstacles:
            self.game_over("Player (Red) hit an obstacle!")

        if snake1[0] in snake1[1:]:
            self.game_over("Player (Green) hit its own body!")

        if snake2[0] in snake2[1:]:
            self.game_over("Player (Red) hit its own body!")

        if snake1[0] in snake2 or snake2[0] in snake1:
            self.game_over("Snakes collided!")

        return False

    def game_over(self, message):
        messagebox.showinfo("Game Over", message)
        self.running = False

    def run(self):
        while self.running:
            self.handle_events()
            self.move_snake(self.snake1, self.direction1)
            self.move_snake(self.snake2, self.direction2)

            self.screen.fill(BLACK)
            self.draw_obstacles()
            self.draw_snake(self.snake1, GREEN)
            self.draw_snake(self.snake2, RED)
            self.draw_food(self.food1, GREEN)
            self.draw_food(self.food2, RED)
            self.draw_clock()
            self.draw_score()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    game = MultiPlayerSnakeGame()
    game.run()