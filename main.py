import pygame
import random
import sys

# Inițializare Pygame
pygame.init()

# Configurări generale
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 10
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Crearea ferestrei jocului
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Font pentru afișarea scorului și mesajelor
FONT = pygame.font.SysFont("arial", 24)
GAME_OVER_FONT = pygame.font.SysFont("arial", 48)


class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Inițial 3 segmente
        self.direction = "RIGHT"
        self.growing = False

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            head_y -= CELL_SIZE
        elif self.direction == "DOWN":
            head_y += CELL_SIZE
        elif self.direction == "LEFT":
            head_x -= CELL_SIZE
        elif self.direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        if not self.growing:
            self.body.pop()  # Elimină ultima poziție a șarpelui dacă nu crește
        else:
            self.growing = False

        self.body.insert(0, new_head)  # Adaugă noua poziție la început

    def grow(self):
        self.growing = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(SCREEN, GREEN, (*segment, CELL_SIZE, CELL_SIZE))


    def check_collision(self):
        # Coliziune cu marginile ecranului
        head_x, head_y = self.body[0]
        if head_x < 0 or head_y < 0 or head_x >= SCREEN_WIDTH or head_y >= SCREEN_HEIGHT:
            return True

        # Coliziune cu propriul corp
        if self.body[0] in self.body[1:]:
            return True

        return False


class Food:
    def __init__(self):
        self.position = (random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

    def draw(self):
        pygame.draw.rect(SCREEN, RED, (*self.position, CELL_SIZE, CELL_SIZE))

    def reset(self):
        self.position = (random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)


def draw_score(score):
    """Funcție pentru afișarea scorului pe ecran."""
    score_text = FONT.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(score_text, (10, 10))


def game_over_screen(score):
    """Funcție pentru afișarea ecranului de Game Over."""
    SCREEN.fill(WHITE)

    # Mesaj de Game Over
    game_over_text = GAME_OVER_FONT.render("Game Over!", True, BLACK)
    SCREEN.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))

    # Afișarea scorului final
    score_text = FONT.render(f"Your Score: {score}", True, BLACK)
    SCREEN.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

    # Instrucțiuni pentru continuare
    restart_text = FONT.render("Press R to Restart or Q to Quit", True, BLACK)
    SCREEN.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    pygame.display.update()

    # Buclă pentru ecranul de Game Over
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Repornire
                    main()
                elif event.key == pygame.K_q:  # Închidere joc
                    pygame.quit()
                    sys.exit()


def difficulty_selection():
    """Funcție pentru selectarea dificultății."""
    SCREEN.fill(WHITE)
    title_text = GAME_OVER_FONT.render("Select Difficulty", True, BLACK)
    SCREEN.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

    easy_text = FONT.render("1. Easy (Slow)", True, GREEN)
    SCREEN.blit(easy_text, (SCREEN_WIDTH // 2 - easy_text.get_width() // 2, SCREEN_HEIGHT // 2 - 30))

    medium_text = FONT.render("2. Medium (Normal)", True, BLACK)
    SCREEN.blit(medium_text, (SCREEN_WIDTH // 2 - medium_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

    hard_text = FONT.render("3. Hard (Fast)", True, RED)
    SCREEN.blit(hard_text, (SCREEN_WIDTH // 2 - hard_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    pygame.display.update()

    # Buclă pentru selectarea dificultății
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 5  # Dificultate ușoară
                elif event.key == pygame.K_2:
                    return 10  # Dificultate medie
                elif event.key == pygame.K_3:
                    return 15  # Dificultate dificilă


# Funcția principală a jocului
def main():
    difficulty = difficulty_selection()  # Selectează dificultatea
    snake = Snake()
    food = Food()
    running = True
    score = 0  # Inițializarea scorului

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"

        # Mișcarea șarpelui
        snake.move()

        # Verificare coliziune cu mâncarea
        if snake.body[0] == food.position:
            snake.grow()
            food.reset()
            score += 10  # Creșterea scorului cu 10 puncte

        # Verificare coliziune cu marginile sau propriul corp
        if snake.check_collision():
            game_over_screen(score)  # Afișare ecran Game Over
            running = False

        # Actualizare ecran
        SCREEN.fill(WHITE)
        snake.draw()
        food.draw()
        draw_score(score)  # Afișarea scorului
        pygame.display.update()
        clock.tick(difficulty)  # Ajustează viteza în funcție de dificultate

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
