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

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        SCREEN.fill(WHITE)  # Clear the screen
        pygame.display.update()
        CLOCK.tick(30)  # Set the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()