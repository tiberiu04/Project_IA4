import pygame
import sys
import random
import os

pygame.init()

pygame.mixer.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Modern Snake Game')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

CLOCK = pygame.time.Clock()
BLOCK_SIZE = 40

FONT_SCORE = pygame.font.SysFont("bahnschrift", 35)
FONT_MESSAGE = pygame.font.SysFont("comicsansms", 50, bold=True)
FONT_MENU = pygame.font.SysFont("comicsansms", 60, bold=True)
FONT_SUBMENU = pygame.font.SysFont("bahnschrift", 40)
FONT_LARGE = pygame.font.SysFont(None, 74)
FONT_MEDIUM = pygame.font.SysFont(None, 48)
FONT_SMALL = pygame.font.SysFont(None, 36)

HIGH_SCORE_FILE = "highscore.txt"

try:
    BACKGROUND_IMAGE = pygame.image.load('images/background.jpg')
    BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

    SNAKE_HEAD_IMAGE = pygame.image.load('images/snakehead.png')
    SNAKE_HEAD_IMAGE = pygame.transform.scale(SNAKE_HEAD_IMAGE, (BLOCK_SIZE, BLOCK_SIZE))

    SNAKE_BODY_IMAGE = pygame.image.load('images/snakebody.png')
    SNAKE_BODY_IMAGE = pygame.transform.scale(SNAKE_BODY_IMAGE, (BLOCK_SIZE, BLOCK_SIZE))

    FOOD_IMAGE = pygame.image.load('images/food.png')
    FOOD_IMAGE = pygame.transform.scale(FOOD_IMAGE, (BLOCK_SIZE, BLOCK_SIZE))

    ENEMY_IMAGE = pygame.image.load('images/enemy.png')
    ENEMY_IMAGE = pygame.transform.scale(ENEMY_IMAGE, (BLOCK_SIZE, BLOCK_SIZE))

    SAD_FACE_IMAGE = pygame.image.load('images/sad_face.png').convert_alpha()

    # Opțional redimensionare
    sad_face_width = 200
    sad_face_height = 200
    SAD_FACE_IMAGE = pygame.transform.scale(SAD_FACE_IMAGE, (sad_face_width, sad_face_height))

    SLURP_SOUND = pygame.mixer.Sound('sounds/slurp.wav')
    GAMEOVER_SOUND = pygame.mixer.Sound('sounds/au.wav')
    # În bucla principală de randare
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
    SCREEN.blit(SAD_FACE_IMAGE, ((SCREEN_WIDTH - sad_face_width)//2, (SCREEN_HEIGHT - sad_face_height)//2))
    pygame.display.update()

except pygame.error as e:
    print(f"Error loading images: {e}")
    print("Ensure that the images are in the 'images/' directory.")
    pygame.quit()
    sys.exit()

def read_high_score():
    if not os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, 'w') as f:
            f.write("0")
    with open(HIGH_SCORE_FILE, 'r') as f:
        try:
            return int(f.read())
        except:
            return 0

def save_high_score(score):
    high_score = read_high_score()
    if score > high_score:
        with open(HIGH_SCORE_FILE, 'w') as f:
            f.write(str(score))

class Snake:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.change_x = 0
        self.change_y = 0
        self.body = [[self.x, self.y]]
        self.length = 1

    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        head = [self.x, self.y]
        self.body.append(head)
        if len(self.body) > self.length:
            del self.body[0]

    def draw(self, screen):
        if len(self.body) > 0:
            SCREEN.blit(SNAKE_HEAD_IMAGE, (self.body[-1][0], self.body[-1][1]))
            for segment in self.body[:-1]:
                SCREEN.blit(SNAKE_BODY_IMAGE, (segment[0], segment[1]))

    def get_head_rect(self):
        return pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.reset()

    def reset(self):
        self.x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        self.y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, screen):
        SCREEN.blit(FOOD_IMAGE, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.reset()

    def reset(self):
        self.x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        self.y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, screen):
        SCREEN.blit(ENEMY_IMAGE, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

def display_score(score):
    text = FONT_SCORE.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(text, [10, 10])

def display_high_score(high_score):
    text = FONT_SCORE.render(f"High Score: {high_score}", True, BLACK)
    SCREEN.blit(text, [SCREEN_WIDTH - 250, 10])

def display_message(msg, color):
    text = FONT_MESSAGE.render(msg, True, color)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    SCREEN.blit(text, text_rect)

def game_snake(SNAKE_SPEED):
    game_over = False
    closed_game = False

    snake = Snake()
    food = Food()
    enemies = []

    # Adding initial enemies
    for _ in range(3):
        enemy = Enemy()
        # Ensure not placed over food or snake
        while [enemy.x, enemy.y] in snake.body or [enemy.x, enemy.y] == [food.x, food.y]:
            enemy.reset()
        enemies.append(enemy)

    level = 1
    points_per_level = 3
    current_score = 0
    high_score = read_high_score()

    while not game_over:
        while closed_game:
            # Jocul s-a terminat, salvam scorul
            save_high_score(current_score)
            GAMEOVER_SOUND.play()
            # Returnam "game_over" ca sa stim in main ca jocul s-a incheiat
            return "game_over"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_high_score(current_score)
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.change_x != BLOCK_SIZE:
                    snake.change_x = -BLOCK_SIZE
                    snake.change_y = 0
                elif event.key == pygame.K_RIGHT and snake.change_x != -BLOCK_SIZE:
                    snake.change_x = BLOCK_SIZE
                    snake.change_y = 0
                elif event.key == pygame.K_UP and snake.change_y != BLOCK_SIZE:
                    snake.change_y = -BLOCK_SIZE
                    snake.change_x = 0
                elif event.key == pygame.K_DOWN and snake.change_y != -BLOCK_SIZE:
                    snake.change_y = BLOCK_SIZE
                    snake.change_x = 0

        if snake.x >= SCREEN_WIDTH or snake.x < 0 or snake.y >= SCREEN_HEIGHT or snake.y < 0:
            closed_game = True

        snake.move()

        SCREEN.blit(BACKGROUND_IMAGE, (0, 0)) 

        food.draw(SCREEN)

        for enemy in enemies:
            enemy.draw(SCREEN)

        snake.draw(SCREEN)

        display_score(current_score)
        display_high_score(high_score)

        pygame.display.update()

        # Collision with food
        snake_head_rect = snake.get_head_rect()
        food_rect = food.get_rect()
        if snake_head_rect.colliderect(food_rect):
            SLURP_SOUND.play()
            snake.length += 1
            current_score += 1
            food.reset()

            # Add an enemy each level
            if current_score % points_per_level == 0:
                level += 1
                SNAKE_SPEED += 2
                enemy = Enemy()
                # Ensure not placed over food or snake
                while [enemy.x, enemy.y] in snake.body or [enemy.x, enemy.y] == [food.x, food.y]:
                    enemy.reset()
                enemies.append(enemy)

        # Collision with own body
        for segment in snake.body[:-1]:
            if segment == [snake.x, snake.y]:
                closed_game = True

        # Collision with enemies
        for enemy in enemies:
            enemy_rect = enemy.get_rect()
            if snake_head_rect.colliderect(enemy_rect):
                closed_game = True

        CLOCK.tick(SNAKE_SPEED)

    pygame.quit()
    sys.exit()

def main_menu():
    menu_active = True
    # Încarci un font personalizat sau folosești alt font integrat
    font_title = pygame.font.SysFont("comicsansms", 80, bold=True)
    font_options = pygame.font.SysFont("bahnschrift", 40)

    title_color = (255, 215, 0)  # auriu
    options_color = (255, 255, 255)

    while menu_active:
        SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

        # Semi-transparent overlay pentru a face textul mai vizibil
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(100)
        overlay.fill((0,0,0))
        SCREEN.blit(overlay, (0,0))

        title_text = font_title.render("ADVANCED SNAKE GAME", True, title_color)
        start_text = font_options.render("Press ENTER to Start", True, options_color)
        quit_text = font_options.render("Press Q to Quit", True, options_color)

        # Efect de umbră pentru titlu
        SCREEN.blit(font_title.render("ADVANCED SNAKE GAME", True, (0,0,0)), 
                    (SCREEN_WIDTH//2 - title_text.get_width()//2 + 2, SCREEN_HEIGHT//2 - 100 + 2))
        SCREEN.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, SCREEN_HEIGHT//2 - 100))
        
        SCREEN.blit(start_text, (SCREEN_WIDTH//2 - start_text.get_width()//2, SCREEN_HEIGHT//2))
        SCREEN.blit(quit_text, (SCREEN_WIDTH//2 - quit_text.get_width()//2, SCREEN_HEIGHT//2 + 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_active = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def difficulty_menu():
    difficulties = ["EASY", "MEDIUM", "HARD"]
    selected_index = 1
    
    # Folosim SysFont cu caractere bold
    font_title = pygame.font.SysFont("comicsansms", 80, bold=True)
    font_options = pygame.font.SysFont("bahnschrift", 60, bold=True)
    font_instructions = pygame.font.SysFont("bahnschrift", 30)

    # Culoarea titlului și a textului
    title_color = (255, 165, 0)  # portocaliu
    selected_color = (255, 255, 255)  # alb pentru selectat
    unselected_color = (180, 180, 180) # gri deschis pentru neselectat
    instructions_color = (220, 220, 220)

    # Încarcă imaginea de fundal dacă ai una potrivită
    # Dacă nu, poți folosi doar un gradient ca înainte
    try:
        fancy_bg = pygame.image.load('images/fancy_bg.jpg').convert()
        fancy_bg = pygame.transform.scale(fancy_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except:
        # Dacă nu există imagine, folosim un gradient simplu
        fancy_bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        top_color = (0, 50, 0)
        bottom_color = (0, 120, 0)
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            r = int(top_color[0]*(1-ratio) + bottom_color[0]*ratio)
            g = int(top_color[1]*(1-ratio) + bottom_color[1]*ratio)
            b = int(top_color[2]*(1-ratio) + bottom_color[2]*ratio)
            pygame.draw.line(fancy_bg, (r,g,b), (0, y), (SCREEN_WIDTH, y))

    # Overlay semi-transparent negru
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0,0,0,100)) # Negru cu opacitate 100/255

    while True:
        SCREEN.blit(fancy_bg, (0, 0))
        SCREEN.blit(overlay, (0,0))

        # Titlu cu umbră
        title_surface = font_title.render("SELECT DIFFICULTY", True, title_color)
        title_x = SCREEN_WIDTH//2 - title_surface.get_width()//2
        title_y = 100
        # Umbra titlului (negru, ușor offset)
        SCREEN.blit(font_title.render("SELECT DIFFICULTY", True, (0,0,0)),
                    (title_x+3, title_y+3))
        SCREEN.blit(title_surface, (title_x, title_y))
        
        # Poziționarea opțiunilor
        num_options = len(difficulties)
        spacing = 70
        total_height = (num_options-1)*spacing + font_options.get_height()
        options_start_y = (SCREEN_HEIGHT // 2) - (total_height // 2) + 50

        for i, diff in enumerate(difficulties):
            is_selected = (i == selected_index)
            color = selected_color if is_selected else unselected_color
            diff_surface = font_options.render(diff, True, color)
            diff_x = SCREEN_WIDTH//2 - diff_surface.get_width()//2
            diff_y = options_start_y + i * spacing

            # Umbra text opțiuni
            SCREEN.blit(font_options.render(diff, True, (0,0,0)), (diff_x+2, diff_y+2))

            # Highlight simplu pentru opțiunea selectată
            if is_selected:
                highlight = pygame.Surface((diff_surface.get_width()+20, diff_surface.get_height()+20), pygame.SRCALPHA)
                highlight.fill((255, 255, 255, 50))
                SCREEN.blit(highlight, (diff_x-10, diff_y-10))

            SCREEN.blit(diff_surface, (diff_x, diff_y))

        # Instrucțiuni jos
        instructions = [
            "Use UP/DOWN to select",
            "Press ENTER to start",
            "Press ESC to go back"
        ]
        
        line_height = 35
        instructions_start_y = SCREEN_HEIGHT - (len(instructions)*line_height) - 40
        
        for i, text_line in enumerate(instructions):
            instr_surf = font_instructions.render(text_line, True, instructions_color)
            instr_x = SCREEN_WIDTH//2 - instr_surf.get_width()//2
            instr_y = instructions_start_y + i * line_height
            # Umbra instrucțiunilor
            SCREEN.blit(font_instructions.render(text_line, True, (0,0,0)), (instr_x+2, instr_y+2))
            SCREEN.blit(instr_surf, (instr_x, instr_y))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(difficulties)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(difficulties)
                elif event.key == pygame.K_RETURN:
                    return difficulties[selected_index]
                elif event.key == pygame.K_ESCAPE:
                    return None

def game_over_menu():
    # Încearcă să încarci o imagine de fundal "images/fancy_bg.jpg"
    # Dacă nu există, folosește un gradient
    try:
        fancy_bg = pygame.image.load('images/fancy_bg.jpg').convert()
        fancy_bg = pygame.transform.scale(fancy_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except:
        fancy_bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        top_color = (50, 0, 0)
        bottom_color = (120, 0, 0)
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            r = int(top_color[0]*(1-ratio) + bottom_color[0]*ratio)
            g = int(top_color[1]*(1-ratio) + bottom_color[1]*ratio)
            b = int(top_color[2]*(1-ratio) + bottom_color[2]*ratio)
            pygame.draw.line(fancy_bg, (r,g,b), (0, y), (SCREEN_WIDTH, y))

    # Overlay semi-transparent
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0,0,0,100))

    # Fonturi
    font_title = pygame.font.SysFont("comicsansms", 100, bold=True)
    # font_options fără bold
    font_options = pygame.font.SysFont("bahnschrift", 40) 
    font_small = pygame.font.SysFont("bahnschrift", 30)

    game_over_active = True

    # Poziționare text
    title_color = (255, 0, 0) # roșu pentru GAME OVER
    instructions_color = (255, 255, 0) # galben pentru instrucțiuni

    # Redimensionează emoticonul să fie mai mare
    sad_face_w = SAD_FACE_IMAGE.get_width()
    sad_face_h = SAD_FACE_IMAGE.get_height()
    scale_factor = 1.5
    SAD_FACE_SCALED = pygame.transform.scale(SAD_FACE_IMAGE, 
                                             (int(sad_face_w*scale_factor), int(sad_face_h*scale_factor)))

    while game_over_active:
        SCREEN.blit(fancy_bg, (0,0))
        SCREEN.blit(overlay, (0,0))

        # Text "GAME OVER" cu umbră
        title_surface = font_title.render("GAME OVER", True, title_color)
        title_x = SCREEN_WIDTH//2 - title_surface.get_width()//2
        title_y = 100
        # Umbra titlului
        SCREEN.blit(font_title.render("GAME OVER", True, (0,0,0)), (title_x+3, title_y+3))
        SCREEN.blit(title_surface, (title_x, title_y))

        # Afișează emoticonul sub titlu
        face_x = SCREEN_WIDTH//2 - SAD_FACE_SCALED.get_width()//2
        face_y = title_y + title_surface.get_height() + 50
        SCREEN.blit(SAD_FACE_SCALED, (face_x, face_y))

        # Text "Press R to Select Difficulty" fără bold
        r_text = font_options.render("Press R to Select Difficulty", True, instructions_color)
        r_x = SCREEN_WIDTH//2 - r_text.get_width()//2
        r_y = face_y + SAD_FACE_SCALED.get_height() + 50
        # Umbră pentru text
        SCREEN.blit(font_options.render("Press R to Select Difficulty", True, (0,0,0)), (r_x+2, r_y+2))
        SCREEN.blit(r_text, (r_x, r_y))

        # Text "Press ESC for Menu" fără bold (folosește același font_options)
        esc_text = font_options.render("Press ESC for Menu", True, instructions_color)
        esc_x = SCREEN_WIDTH//2 - esc_text.get_width()//2
        esc_y = r_y + r_text.get_height() + 10
        SCREEN.blit(font_options.render("Press ESC for Menu", True, (0,0,0)), (esc_x+2, esc_y+2))
        SCREEN.blit(esc_text, (esc_x, esc_y))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "again"   # revine la select difficulty
                elif event.key == pygame.K_ESCAPE:
                    return "menu"    # revine la meniul principal
    

def main():
    while True:
        # Meniul principal
        main_menu()
        
        # Dacă ajungem aici înseamnă că s-a apăsat ENTER în meniul principal
        chosen_difficulty = difficulty_menu()
        if chosen_difficulty is None:
            # Dacă s-a apăsat ESC în meniul de dificultate, revenim la meniul principal
            continue

        # Setăm viteza în funcție de dificultate
        if chosen_difficulty == "EASY":
            initial_speed = 5
        elif chosen_difficulty == "MEDIUM":
            initial_speed = 7.5
        else:
            initial_speed = 10

        # Pornim jocul
        result = game_snake(initial_speed)
        # Dacă jocul returnează "game_over", afisăm meniul de game over
        if result == "game_over":
            action = game_over_menu()
            if action == "again":
                # Daca R, reselectam dificultatea
                continue
            elif action == "menu":
                # Daca ESC, mergem la meniul principal
                continue

if __name__ == "__main__":
    main()