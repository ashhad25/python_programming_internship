import pygame
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class SinglePlayerSnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game - Single Player')
        self.clock = pygame.time.Clock()
        self.running = True

        self.snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]

        self.obstacles = self.generate_obstacles()
        
        self.direction = (0, -1)
        self.food = self.generate_food()
        self.score = 0


        self.font = pygame.font.Font(None, 36) 

    def generate_food(self):
        while True:
            x = random.randrange(0, SCREEN_WIDTH, CELL_SIZE)
            y = random.randrange(0, SCREEN_HEIGHT, CELL_SIZE)
            if (x, y) not in self.snake and (x, y) not in self.obstacles:
                return x, y

    def generate_obstacles(self):
        obstacles = []
        for _ in range(10):
            while True:
                x = random.randrange(0, SCREEN_WIDTH, CELL_SIZE)
                y = random.randrange(0, SCREEN_HEIGHT, CELL_SIZE)
                if (x, y) not in self.snake and (x, y) not in obstacles:
                    obstacles.append((x, y))
                    break
        return obstacles

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    def draw_food(self):
        pygame.draw.rect(self.screen, RED, (self.food[0], self.food[1], CELL_SIZE, CELL_SIZE))

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            pygame.draw.rect(self.screen, BLUE, (obstacle[0], obstacle[1], CELL_SIZE, CELL_SIZE))

    def draw_clock(self):
        current_time = time.strftime('%I:%M:%S %p')
        text_surface = self.font.render(current_time, True, WHITE)
        self.screen.blit(text_surface, (10, 10))

    def draw_score(self):
        score_text = f'Score: {self.score}'
        text_surface = self.font.render(score_text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.topright = (SCREEN_WIDTH - 10, 10)
        self.screen.blit(text_surface, text_rect)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = ((head_x + dx * CELL_SIZE) % SCREEN_WIDTH, (head_y + dy * CELL_SIZE) % SCREEN_HEIGHT)

        if new_head in self.snake or new_head in self.obstacles:
            self.game_over()

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 10 
            self.food = self.generate_food()
        else:
            self.snake.pop()

    def draw_game_over_screen(self):
        darken_rect = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        darken_rect.set_alpha(128)
        darken_rect.fill((0, 0, 0))
        self.screen.blit(darken_rect, (0, 0))

        game_over_text = self.font.render("Game Over", True, WHITE)
        score_text = self.font.render(f"Your Score: {self.score}", True, WHITE)
        self.screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(score_text, ((SCREEN_WIDTH - score_text.get_width()) // 2, SCREEN_HEIGHT // 2 + 40))

        pygame.display.flip()

        pygame.time.wait(1000)

    def game_over(self):
        self.draw_game_over_screen()
        self.running = False


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    self.direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    self.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.direction = (1, 0)

    def run(self):
        while self.running:
            self.handle_events()
            self.move_snake()

            self.screen.fill(BLACK)
            self.draw_obstacles()
            self.draw_snake()
            self.draw_food()
            self.draw_clock()
            self.draw_score() 
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    game = SinglePlayerSnakeGame()
    game.run()