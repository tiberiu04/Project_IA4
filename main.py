import pygame
import sys

pygame.init()

# Screen settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
CLOCK = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.size = 40
        self.change_x = 0
        self.change_y = 0
        self.body = [[self.x, self.y]]
        self.length = 1

    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        self.body.append([self.x, self.y])
        if len(self.body) > self.length:
            del self.body[0]

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(SCREEN, BLACK, (segment[0], segment[1], self.size, self.size))

def main():
    running = True
    snake = Snake()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_x = -snake.size
                    snake.change_y = 0
                elif event.key == pygame.K_RIGHT:
                    snake.change_x = snake.size
                    snake.change_y = 0
                elif event.key == pygame.K_UP:
                    snake.change_y = -snake.size
                    snake.change_x = 0
                elif event.key == pygame.K_DOWN:
                    snake.change_y = snake.size
                    snake.change_x = 0

        snake.move()
        SCREEN.fill(WHITE)
        snake.draw()
        pygame.display.update()
        CLOCK.tick(10)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()