import pygame
import sys
import random
import os
<<<<<<< HEAD
import math

# Pygame initialization 
=======

>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
pygame.init()
pygame.mixer.init()

<<<<<<< HEAD
# Screen settings
=======
pygame.mixer.init()

>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Modern Snake Game')

<<<<<<< HEAD
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock
CLOCK = pygame.time.Clock()
BLOCK_SIZE = 40

# Fonts
FONT_SCORE = pygame.font.SysFont("bahnschrift", 35)
FONT_MESSAGE = pygame.font.SysFont("comicsansms", 50, bold=True)
FONT_MENU = pygame.font.SysFont("comicsansms", 60, bold=True)
FONT_SUBMENU = pygame.font.SysFont("bahnschrift", 40)
FONT_LARGE = pygame.font.SysFont(None, 74)
FONT_MEDIUM = pygame.font.SysFont(None, 48)
FONT_SMALL = pygame.font.SysFont(None, 36)

# Files
HIGH_SCORE_FILE = "highscore.txt"

# Load images and sounds
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
    sad_face_width = 200
    sad_face_height = 200
    SAD_FACE_IMAGE = pygame.transform.scale(SAD_FACE_IMAGE, (sad_face_width, sad_face_height))

    # Load power-up images
    POWERUP_SPEED_IMAGE = pygame.image.load('images/powerup_speed.png').convert_alpha()
    POWERUP_SPEED_IMAGE = pygame.transform.scale(POWERUP_SPEED_IMAGE, (BLOCK_SIZE, BLOCK_SIZE))
    POWERUP_SPEED_IMAGE.set_alpha(200)  # Set transparency for Power-Up Speed

    POWERUP_DOUBLE_IMAGE = pygame.image.load('images/powerup_double.png').convert_alpha()
    POWERUP_DOUBLE_IMAGE = pygame.transform.scale(POWERUP_DOUBLE_IMAGE, (BLOCK_SIZE, BLOCK_SIZE))
    POWERUP_DOUBLE_IMAGE.set_alpha(200)  # Set transparency for Power-Up Double Points

    POWERUP_SHIELD_IMAGE = pygame.image.load('images/powerup_shield.png').convert_alpha()
    POWERUP_SHIELD_IMAGE = pygame.transform.scale(POWERUP_SHIELD_IMAGE, (BLOCK_SIZE, BLOCK_SIZE))
    POWERUP_SHIELD_IMAGE.set_alpha(200)  # Set transparency for Power-Up Shield

    # Loading sounds
    SLURP_SOUND = pygame.mixer.Sound('sounds/slurp.wav')
    GAMEOVER_SOUND = pygame.mixer.Sound('sounds/au.wav')
    POWERUP_SOUND = pygame.mixer.Sound('sounds/powerup.wav')
=======
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
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3

except pygame.error as e:
    print(f"Error loading images or sounds: {e}")
    print("Ensure that the images are in the 'images/' directory and sounds in 'sounds/' directory.")
    pygame.quit()
    sys.exit()

<<<<<<< HEAD
# Global variables
snake = None
food = None
enemies = []
obstacles = []

# Displaying the sad face
SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
SCREEN.blit(SAD_FACE_IMAGE, ((SCREEN_WIDTH - sad_face_width)//2, (SCREEN_HEIGHT - sad_face_height)//2))
pygame.display.update()

# Score functions
def read_high_scores():
    if not os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, 'w') as f:
            f.write("0\n0\n0\n0\n0")  # Top 5 scores are initialized with 0
    with open(HIGH_SCORE_FILE, 'r') as f:
        try:
            scores = f.read().splitlines()
            scores = [int(score) for score in scores]
            scores += [0] * (5 - len(scores))  # Ensuring there are 5 scores
            return scores[:5]
        except:
            return [0, 0, 0, 0, 0]

def save_high_scores(score):
    high_scores = read_high_scores()
    high_scores.append(score)
    high_scores = sorted(high_scores, reverse=True)[:5]
    with open(HIGH_SCORE_FILE, 'w') as f:
        for hs in high_scores:
            f.write(f"{hs}\n")

# Snakes class
class Snake:
    def __init__(self):
        global snake
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.change_x = 0
        self.change_y = 0
        self.body = [[self.x, self.y]]
        self.length = 1

    # Moving the snake
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
        head = [self.x, self.y]
        self.body.append(head)
        if len(self.body) > self.length:
            del self.body[0]
    
    # Drawing the snake on the screen
    def draw(self, screen):
        if len(self.body) > 0:
            screen.blit(SNAKE_HEAD_IMAGE, (self.body[-1][0], self.body[-1][1]))
            for segment in self.body[:-1]:
                screen.blit(SNAKE_BODY_IMAGE, (segment[0], segment[1]))

    def get_head_rect(self):
        return pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def reset_position(self):
        # Resetting the snake to the center of the screen
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.change_x = 0
        self.change_y = 0
        self.body = [[self.x, self.y]]
        self.length = 1

class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.reset()

    def reset(self):
        while True:
            self.x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            self.y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            # Ensuring the food does not overlap with the snake, enemies, or obstacles
            if ([self.x, self.y] not in snake.body and 
                not any([self.x, self.y] == [enemy.x, enemy.y] for enemy in enemies) and 
                not any([self.x, self.y] == [obstacle.x, obstacle.y] for obstacle in obstacles)):
                break

    def draw(self, screen):
        screen.blit(FOOD_IMAGE, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

class Enemy:
    def __init__(self):
        global enemies
        self.x = 0
        self.y = 0
        self.reset()
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.move_counter = 0
        self.move_delay = 30  # The initial speed of the snake

    def set_move_delay(self, snake_speed):
        # Adjusting move_delay depending on the snake's speed
        self.move_delay = max(1, 30 - int(snake_speed))

    def reset(self):
        while True:
            self.x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            self.y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            # The enemy should not overlap with the snake, food, or other enemies
            if ([self.x, self.y] not in snake.body and 
                [self.x, self.y] != [food.x, food.y] and 
                not any([self.x, self.y] == [enemy.x, enemy.y] for enemy in enemies)):
                break
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.move_counter = 0

    def move(self, snake_speed):
        self.move_counter += 1
        self.set_move_delay(snake_speed)
        if self.move_counter > self.move_delay:
            self.move_counter = 0
            # Changing direction randomly
            if random.random() < 0.3:
                self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

            # The movement of the enemy
            if self.direction == "UP" and self.y - BLOCK_SIZE >= 0:
                self.y -= BLOCK_SIZE
            elif self.direction == "DOWN" and self.y + BLOCK_SIZE < SCREEN_HEIGHT:
                self.y += BLOCK_SIZE
            elif self.direction == "LEFT" and self.x - BLOCK_SIZE >= 0:
                self.x -= BLOCK_SIZE
            elif self.direction == "RIGHT" and self.x + BLOCK_SIZE < SCREEN_WIDTH:
                self.x += BLOCK_SIZE

    def draw(self, screen):
        screen.blit(ENEMY_IMAGE, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

class PowerUp:
    def __init__(self):
        self.size = BLOCK_SIZE
        self.type = random.choice(["SPEED", "DOUBLE_POINTS", "SHIELD"])  # Types of powerups
        self.x, self.y = self.generate_position()
        self.active = False

    def generate_position(self):
        min_distance = BLOCK_SIZE * 3  # A minimum distance from the snake
        while True:
            x = random.randrange(0, SCREEN_WIDTH - self.size, self.size)
            y = random.randrange(0, SCREEN_HEIGHT - self.size, self.size)
            # Checking if the position is valid
            if ([x, y] not in snake.body and 
                not any([x, y] == [enemy.x, enemy.y] for enemy in enemies) and 
                not any([x, y] == [obstacle.x, obstacle.y] for obstacle in obstacles)):
                
                # Computing the distance to the head of the snake
                distance = math.hypot(snake.x - x, snake.y - y)
                if distance >= min_distance:
                    return x, y

    def draw(self, screen):
        if self.type == "SPEED":
            image = POWERUP_SPEED_IMAGE
        elif self.type == "DOUBLE_POINTS":
            image = POWERUP_DOUBLE_IMAGE
        elif self.type == "SHIELD":
            image = POWERUP_SHIELD_IMAGE
        screen.blit(image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

class Obstacle:
    def __init__(self):
        self.size = BLOCK_SIZE
        self.x = random.randrange(0, SCREEN_WIDTH - self.size, self.size)
        self.y = random.randrange(0, SCREEN_HEIGHT - self.size, self.size)
        self.direction_x = random.choice([-1, 1])  
        self.direction_y = random.choice([-1, 1])  
        self.speed = 2  # The speed of the obstacle
        self.move_counter = 0
        self.move_delay = 30

        # Ensuring the obstacle does not overlap with the snake, food, or enemies
        while ([self.x, self.y] in snake.body or 
               [self.x, self.y] == [food.x, food.y] or 
               any([self.x, self.y] == [enemy.x, enemy.y] for enemy in enemies)):
            self.x = random.randrange(0, SCREEN_WIDTH - self.size, self.size)
            self.y = random.randrange(0, SCREEN_HEIGHT - self.size, self.size)

    def set_move_delay(self, snake_speed):
        # Adjusting move_delay depending on the snake's speed
        self.move_delay = max(1, 30 - int(snake_speed))

    def move(self, snake_speed):
        self.move_counter += 1
        self.set_move_delay(snake_speed)
        if self.move_counter > self.move_delay:
            self.move_counter = 0
            # The movement continues
            self.x += self.direction_x * self.speed
            self.y += self.direction_y * self.speed

            # Checking if the obstacle hits the wall
            if self.x <= 0 or self.x >= SCREEN_WIDTH - self.size:
                self.direction_x *= -1
            if self.y <= 0 or self.y >= SCREEN_HEIGHT - self.size:
                self.direction_y *= -1

    def draw(self, screen):
        screen.blit(ENEMY_IMAGE, (self.x, self.y))  # Displaying the obstacle with the associated image

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

# Displaying the highscore
def display_score(score):
    text = FONT_SCORE.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(text, [10, 10])

def display_high_scores(high_scores):
    spacing = 150  # The spacing between the high scores
    start_x = 50  # The starting position
    y = 10  # The vertical position

    for i, hs in enumerate(high_scores):
        text = FONT_SCORE.render(f"{i+1}. {hs}", True, BLACK)
        SCREEN.blit(text, [start_x + i * spacing, y])

def display_lives(lives):
    text = FONT_SCORE.render(f"Lives: {lives}", True, BLACK)
    SCREEN.blit(text, [10, 50])

def display_message(msg, color):
    text = FONT_MESSAGE.render(msg, True, color)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    SCREEN.blit(text, text_rect)

# The game logic is located here
def game_snake(SNAKE_SPEED):
    global snake, food, enemies, obstacles
    game_over = False
    closed_game = False

    snake = Snake()
    food = Food()
    enemies = []

    # The creation of the initial enemies
    for _ in range(3):
        enemy = Enemy()
        while [enemy.x, enemy.y] in snake.body or [enemy.x, enemy.y] == [food.x, food.y]:
            enemy.reset()
        enemies.append(enemy)

    # Creating the obstacles
    obstacles = []
    for _ in range(4):
        obstacle = Obstacle()
        # Ensuring the obstacles do not overlap with the snake, food, or enemies
        while ([obstacle.x, obstacle.y] in snake.body or 
               [obstacle.x, obstacle.y] == [food.x, food.y] or 
               any([obstacle.x, obstacle.y] == [enemy.x, enemy.y] for enemy in enemies)):
            obstacle = Obstacle()
        obstacles.append(obstacle)

    # Game variables
    level = 1
    points_per_level = 3
    current_score = 0
    high_scores = read_high_scores()
    lives = 3
    shield_active = False

    # Power-ups
    powerup = None
    powerup_timer = random.randint(3000, 6000)  # 3-6 seconds interval for testing
    last_powerup_time = pygame.time.get_ticks()
    POWERUP_DURATION = 5000  # ms
    powerup_active = False
    powerup_start_time = None
    active_powerup_type = None  # New variable to store the type of the active power-up
    original_speed = SNAKE_SPEED # Store the original speed
    original_points_per_level = points_per_level

    while not game_over:
        while closed_game:
            save_high_scores(current_score)
            GAMEOVER_SOUND.play()
            return "game_over"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_high_scores(current_score)
                pygame.quit()
                sys.exit()
            # The movement of the snake
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

        # Colision with the walls, snake loses a life
        if snake.x >= SCREEN_WIDTH or snake.x < 0 or snake.y >= SCREEN_HEIGHT or snake.y < 0:
            if not shield_active:
                lives -= 1
                if lives <= 0:
                    closed_game = True
                else:
                    snake.reset_position()  # Resetting the snake to the center
            else:
                # If the shield is active, the snake does not lose a life
                pass

        snake.move()

        SCREEN.blit(BACKGROUND_IMAGE, (0, 0)) 

        # Drawing the food
        food.draw(SCREEN)

        # drawing and moving the enemies
        for enemy in enemies:
            enemy.move(SNAKE_SPEED)
            enemy.draw(SCREEN)

        # Drawing the obstacles
        for obstacle in obstacles:
            obstacle.move(SNAKE_SPEED)
            obstacle.draw(SCREEN)

        # Generating the power-up
        current_time = pygame.time.get_ticks()
        if powerup is None and current_time - last_powerup_time > powerup_timer:
            powerup = PowerUp()
            last_powerup_time = current_time
            # Setting a new random timer for the next power-up
            powerup_timer = random.randint(3000, 6000)  # 3-6 seconds

        # Drawing the power-up if it exists
        if powerup is not None:
            powerup.draw(SCREEN)

        # Drawing the snake
        snake.draw(SCREEN)

        # Displaying the score, high scores, and lives
        display_score(current_score)
        display_high_scores(high_scores)
        display_lives(lives)

        # Displaying updates
        pygame.display.update()

        snake_head_rect = snake.get_head_rect()
        food_rect = food.get_rect()

        # Colision with food
        if snake_head_rect.colliderect(food_rect):
            SLURP_SOUND.play()
            snake.length += 1
            current_score += 1
            food.reset()

            # Generating a new enemy/level
            if current_score % points_per_level == 0:
                level += 1
                SNAKE_SPEED += 2
                enemy = Enemy()
                while [enemy.x, enemy.y] in snake.body or [enemy.x, enemy.y] == [food.x, food.y]:
                    enemy.reset()
                enemies.append(enemy)

        # Colision with the snake's body
        for segment in snake.body[:-1]:
            if segment == [snake.x, snake.y]:
                if not shield_active:
                    lives -= 1 # The snake loses a life
                    if lives <= 0:
                        closed_game = True
                    else:
                        snake.reset_position()  # Resetting the snake to the center
                else:
                    # If the shield is active, the snake does not lose a life
                    pass

        # Colision with the enemies
        for enemy in enemies:
            enemy_rect = enemy.get_rect()
            if snake_head_rect.colliderect(enemy_rect):
                # If the shield is not active, the snake loses a life
                if not shield_active: 
                    lives -= 1
                    if lives <= 0:
                        closed_game = True
                    else:
                        snake.reset_position()  # Resetting the snake to the center
                else:
                    # If the shield is active, the snake does not lose a life
                    pass

        # Colision with the obstacles
        for obstacle in obstacles:
            obstacle_rect = obstacle.get_rect()
            if snake_head_rect.colliderect(obstacle_rect):
                if not shield_active:
                    lives -= 1
                    if lives <= 0:
                        closed_game = True
                    else:
                        snake.reset_position()  # Resetting the snake to the center
                else:
                    # If the shield is active, the snake does not lose a life
                    pass

        # Colision with the power-up
        if powerup is not None and snake_head_rect.colliderect(powerup.get_rect()):
            POWERUP_SOUND.play()  # Playing the sound
            powerup_active = True
            powerup_start_time = pygame.time.get_ticks()
            active_powerup_type = powerup.type  # Storing the type of the active power-up
            if powerup.type == "SPEED":
                SNAKE_SPEED += 3  # The speed boosts
            elif powerup.type == "DOUBLE_POINTS":
                points_per_level = 1  # The points per level double
            elif powerup.type == "SHIELD":
                shield_active = True
            # Powerup does not exist anymore
            powerup = None

        # Checking if the power-up is still active
        if powerup_active and current_time - powerup_start_time > POWERUP_DURATION:
            powerup_active = False
            if active_powerup_type == "SPEED":
                SNAKE_SPEED -= 3  # Resetting the speed
            elif active_powerup_type == "DOUBLE_POINTS":
                points_per_level = original_points_per_level
            elif active_powerup_type == "SHIELD":
                shield_active = False
            active_powerup_type = None  # Resetting the active power-up type

        CLOCK.tick(SNAKE_SPEED)

    # Exiting the game
    pygame.quit()
    sys.exit()

# Menu functions
def main_menu():
    menu_active = True
    font_title = pygame.font.SysFont("comicsansms", 80, bold=True)
    font_options = pygame.font.SysFont("bahnschrift", 40)

    title_color = (255, 215, 0)  # Gold
    options_color = (255, 255, 255)  # White
=======
def main_menu():
    menu_active = True
    # Încarci un font personalizat sau folosești alt font integrat
    font_title = pygame.font.SysFont("comicsansms", 80, bold=True)
    font_options = pygame.font.SysFont("bahnschrift", 40)

    title_color = (255, 215, 0)  # auriu
    options_color = (255, 255, 255)
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3

    while menu_active:
        SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

<<<<<<< HEAD
        # Overlay for the menu
=======
        # Semi-transparent overlay pentru a face textul mai vizibil
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(100)
        overlay.fill((0,0,0))
        SCREEN.blit(overlay, (0,0))

<<<<<<< HEAD
        # Text for the menu
=======
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        title_text = font_title.render("ADVANCED SNAKE GAME", True, title_color)
        start_text = font_options.render("Press ENTER to Start", True, options_color)
        quit_text = font_options.render("Press Q to Quit", True, options_color)

<<<<<<< HEAD
        # Displaying the title with a shadow
=======
        # Efect de umbră pentru titlu
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        SCREEN.blit(font_title.render("ADVANCED SNAKE GAME", True, (0,0,0)), 
                    (SCREEN_WIDTH//2 - title_text.get_width()//2 + 2, SCREEN_HEIGHT//2 - 100 + 2))
        SCREEN.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, SCREEN_HEIGHT//2 - 100))
        
<<<<<<< HEAD
        # Displaying the options with a shadow
        SCREEN.blit(font_options.render("Press ENTER to Start", True, (0,0,0)), 
                    (SCREEN_WIDTH//2 - start_text.get_width()//2 + 2, SCREEN_HEIGHT//2 + 2))
        SCREEN.blit(font_options.render("Press Q to Quit", True, (0,0,0)), 
                    (SCREEN_WIDTH//2 - quit_text.get_width()//2 + 2, SCREEN_HEIGHT//2 + 52))
        
        # Listing the options
=======
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        SCREEN.blit(start_text, (SCREEN_WIDTH//2 - start_text.get_width()//2, SCREEN_HEIGHT//2))
        SCREEN.blit(quit_text, (SCREEN_WIDTH//2 - quit_text.get_width()//2, SCREEN_HEIGHT//2 + 50))

        pygame.display.update()

<<<<<<< HEAD
        # Event handling
        for event in pygame.event.get():
            # Exiting the game
=======
        for event in pygame.event.get():
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
            if event.type == pygame.QUIT:
                menu_active = False
                pygame.quit()
                sys.exit()
<<<<<<< HEAD
            # Starting the game
            if event.type == pygame.KEYDOWN:
                # If enter is pressed, the game starts
                if event.key == pygame.K_RETURN:
                    return
                # If Q is pressed, the game quits    
=======
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def difficulty_menu():
    difficulties = ["EASY", "MEDIUM", "HARD"]
    selected_index = 1
    
<<<<<<< HEAD
=======
    # Folosim SysFont cu caractere bold
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
    font_title = pygame.font.SysFont("comicsansms", 80, bold=True)
    font_options = pygame.font.SysFont("bahnschrift", 60, bold=True)
    font_instructions = pygame.font.SysFont("bahnschrift", 30)

<<<<<<< HEAD
    title_color = (255, 165, 0)  
    selected_color = (255, 255, 255)
    unselected_color = (180, 180, 180)
    instructions_color = (220, 220, 220)
    
    # Background image
=======
    # Culoarea titlului și a textului
    title_color = (255, 165, 0)  # portocaliu
    selected_color = (255, 255, 255)  # alb pentru selectat
    unselected_color = (180, 180, 180) # gri deschis pentru neselectat
    instructions_color = (220, 220, 220)

    # Încarcă imaginea de fundal dacă ai una potrivită
    # Dacă nu, poți folosi doar un gradient ca înainte
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
    try:
        fancy_bg = pygame.image.load('images/fancy_bg.jpg').convert()
        fancy_bg = pygame.transform.scale(fancy_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except:
<<<<<<< HEAD
        # If the image is not found, a gradient background is created
=======
        # Dacă nu există imagine, folosim un gradient simplu
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        fancy_bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        top_color = (0, 50, 0)
        bottom_color = (0, 120, 0)
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            r = int(top_color[0]*(1-ratio) + bottom_color[0]*ratio)
            g = int(top_color[1]*(1-ratio) + bottom_color[1]*ratio)
            b = int(top_color[2]*(1-ratio) + bottom_color[2]*ratio)
            pygame.draw.line(fancy_bg, (r,g,b), (0, y), (SCREEN_WIDTH, y))

<<<<<<< HEAD
    # Overlay for the menu
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0,0,0,100))

    # Displaying the menu
=======
    # Overlay semi-transparent negru
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0,0,0,100)) # Negru cu opacitate 100/255

>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
    while True:
        SCREEN.blit(fancy_bg, (0, 0))
        SCREEN.blit(overlay, (0,0))

<<<<<<< HEAD
        # The title of the menu
        title_surface = font_title.render("SELECT DIFFICULTY", True, title_color)
        title_x = SCREEN_WIDTH//2 - title_surface.get_width()//2
        title_y = 100

        # The shadow of the title
=======
        # Titlu cu umbră
        title_surface = font_title.render("SELECT DIFFICULTY", True, title_color)
        title_x = SCREEN_WIDTH//2 - title_surface.get_width()//2
        title_y = 100
        # Umbra titlului (negru, ușor offset)
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        SCREEN.blit(font_title.render("SELECT DIFFICULTY", True, (0,0,0)),
                    (title_x+3, title_y+3))
        SCREEN.blit(title_surface, (title_x, title_y))
        
<<<<<<< HEAD
        # The options for the difficulty and the spacing and placement
=======
        # Poziționarea opțiunilor
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        num_options = len(difficulties)
        spacing = 70
        total_height = (num_options-1)*spacing + font_options.get_height()
        options_start_y = (SCREEN_HEIGHT // 2) - (total_height // 2) + 50

        for i, diff in enumerate(difficulties):
<<<<<<< HEAD
            # The color of the selected difficulty
=======
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
            is_selected = (i == selected_index)
            color = selected_color if is_selected else unselected_color
            diff_surface = font_options.render(diff, True, color)
            diff_x = SCREEN_WIDTH//2 - diff_surface.get_width()//2
            diff_y = options_start_y + i * spacing

<<<<<<< HEAD
            SCREEN.blit(font_options.render(diff, True, (0,0,0)), (diff_x+2, diff_y+2))

            # Highlighting the selected difficulty
=======
            # Umbra text opțiuni
            SCREEN.blit(font_options.render(diff, True, (0,0,0)), (diff_x+2, diff_y+2))

            # Highlight simplu pentru opțiunea selectată
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
            if is_selected:
                highlight = pygame.Surface((diff_surface.get_width()+20, diff_surface.get_height()+20), pygame.SRCALPHA)
                highlight.fill((255, 255, 255, 50))
                SCREEN.blit(highlight, (diff_x-10, diff_y-10))

            SCREEN.blit(diff_surface, (diff_x, diff_y))

<<<<<<< HEAD
        # The instructions for the menu
=======
        # Instrucțiuni jos
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        instructions = [
            "Use UP/DOWN to select",
            "Press ENTER to start",
            "Press ESC to go back"
        ]
        
<<<<<<< HEAD
        # The placement and spacing of the instructions
        line_height = 35
        instructions_start_y = SCREEN_HEIGHT - (len(instructions)*line_height) - 40
        
        # Displaying the instructions
=======
        line_height = 35
        instructions_start_y = SCREEN_HEIGHT - (len(instructions)*line_height) - 40
        
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        for i, text_line in enumerate(instructions):
            instr_surf = font_instructions.render(text_line, True, instructions_color)
            instr_x = SCREEN_WIDTH//2 - instr_surf.get_width()//2
            instr_y = instructions_start_y + i * line_height
<<<<<<< HEAD

            SCREEN.blit(font_instructions.render(text_line, True, (0,0,0)), (instr_x+2, instr_y+2))
            SCREEN.blit(instr_surf, (instr_x, instr_y))
        
        # Updating the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            # Exiting the game
=======
            # Umbra instrucțiunilor
            SCREEN.blit(font_instructions.render(text_line, True, (0,0,0)), (instr_x+2, instr_y+2))
            SCREEN.blit(instr_surf, (instr_x, instr_y))
        
        pygame.display.flip()

        for event in pygame.event.get():
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
<<<<<<< HEAD
                # Changing the selected difficulty and checking which key was pressed in the menu
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(difficulties)
                # The down key was pressed    
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(difficulties)
                # The enter key was pressed
                elif event.key == pygame.K_RETURN:
                    return difficulties[selected_index]
                # The escape key was pressed and no difficulty was selected    
=======
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(difficulties)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(difficulties)
                elif event.key == pygame.K_RETURN:
                    return difficulties[selected_index]
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
                elif event.key == pygame.K_ESCAPE:
                    return None

def game_over_menu():
<<<<<<< HEAD
    # Background image
=======
    # Încearcă să încarci o imagine de fundal "images/fancy_bg.jpg"
    # Dacă nu există, folosește un gradient
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
    try:
        fancy_bg = pygame.image.load('images/fancy_bg.jpg').convert()
        fancy_bg = pygame.transform.scale(fancy_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except:
        fancy_bg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        top_color = (50, 0, 0)
        bottom_color = (120, 0, 0)
<<<<<<< HEAD
        # Creating a gradient background
=======
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            r = int(top_color[0]*(1-ratio) + bottom_color[0]*ratio)
            g = int(top_color[1]*(1-ratio) + bottom_color[1]*ratio)
            b = int(top_color[2]*(1-ratio) + bottom_color[2]*ratio)
            pygame.draw.line(fancy_bg, (r,g,b), (0, y), (SCREEN_WIDTH, y))

<<<<<<< HEAD
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0,0,0,100))

    font_title = pygame.font.SysFont("comicsansms", 100, bold=True)
=======
    # Overlay semi-transparent
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0,0,0,100))

    # Fonturi
    font_title = pygame.font.SysFont("comicsansms", 100, bold=True)
    # font_options fără bold
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
    font_options = pygame.font.SysFont("bahnschrift", 40) 
    font_small = pygame.font.SysFont("bahnschrift", 30)

    game_over_active = True

<<<<<<< HEAD
    title_color = (255, 0, 0)
    instructions_color = (255, 255, 0) 

    # Scaling the sad face image
=======
    # Poziționare text
    title_color = (255, 0, 0) # roșu pentru GAME OVER
    instructions_color = (255, 255, 0) # galben pentru instrucțiuni

    # Redimensionează emoticonul să fie mai mare
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
    sad_face_w = SAD_FACE_IMAGE.get_width()
    sad_face_h = SAD_FACE_IMAGE.get_height()
    scale_factor = 1.5
    SAD_FACE_SCALED = pygame.transform.scale(SAD_FACE_IMAGE, 
                                             (int(sad_face_w*scale_factor), int(sad_face_h*scale_factor)))

<<<<<<< HEAD
    # Displaying the game over menu
=======
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
    while game_over_active:
        SCREEN.blit(fancy_bg, (0,0))
        SCREEN.blit(overlay, (0,0))

<<<<<<< HEAD
        # Game over title with a shadow
        title_surface = font_title.render("GAME OVER", True, title_color)
        title_x = SCREEN_WIDTH//2 - title_surface.get_width()//2
        title_y = 100

        # Displaying the title with a shadow
        SCREEN.blit(font_title.render("GAME OVER", True, (0,0,0)), (title_x+3, title_y+3))
        SCREEN.blit(title_surface, (title_x, title_y))

        # Displaying the sad face
=======
        # Text "GAME OVER" cu umbră
        title_surface = font_title.render("GAME OVER", True, title_color)
        title_x = SCREEN_WIDTH//2 - title_surface.get_width()//2
        title_y = 100
        # Umbra titlului
        SCREEN.blit(font_title.render("GAME OVER", True, (0,0,0)), (title_x+3, title_y+3))
        SCREEN.blit(title_surface, (title_x, title_y))

        # Afișează emoticonul sub titlu
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        face_x = SCREEN_WIDTH//2 - SAD_FACE_SCALED.get_width()//2
        face_y = title_y + title_surface.get_height() + 50
        SCREEN.blit(SAD_FACE_SCALED, (face_x, face_y))

<<<<<<< HEAD
        # Displaying the options after losing the game
        r_text = font_options.render("Press R to Select Difficulty", True, instructions_color)
        r_x = SCREEN_WIDTH//2 - r_text.get_width()//2
        r_y = face_y + SAD_FACE_SCALED.get_height() + 50

        SCREEN.blit(font_options.render("Press R to Select Difficulty", True, (0,0,0)), (r_x+2, r_y+2))
        SCREEN.blit(r_text, (r_x, r_y))

        # Setting the design for the instructions, specificallly the escape key
=======
        # Text "Press R to Select Difficulty" fără bold
        r_text = font_options.render("Press R to Select Difficulty", True, instructions_color)
        r_x = SCREEN_WIDTH//2 - r_text.get_width()//2
        r_y = face_y + SAD_FACE_SCALED.get_height() + 50
        # Umbră pentru text
        SCREEN.blit(font_options.render("Press R to Select Difficulty", True, (0,0,0)), (r_x+2, r_y+2))
        SCREEN.blit(r_text, (r_x, r_y))

        # Text "Press ESC for Menu" fără bold (folosește același font_options)
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        esc_text = font_options.render("Press ESC for Menu", True, instructions_color)
        esc_x = SCREEN_WIDTH//2 - esc_text.get_width()//2
        esc_y = r_y + r_text.get_height() + 10
        SCREEN.blit(font_options.render("Press ESC for Menu", True, (0,0,0)), (esc_x+2, esc_y+2))
        SCREEN.blit(esc_text, (esc_x, esc_y))
        
        pygame.display.flip()

<<<<<<< HEAD
        # Event handling
        for event in pygame.event.get():
            # Exiting the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Selecting the option
            if event.type == pygame.KEYDOWN:
                # The R key was pressed
                if event.key == pygame.K_r:
                    # Returning to the main menu
                    return "again" 
                elif event.key == pygame.K_ESCAPE:
                    # Returning to the main menu
                    return "menu"

def main():
    while True:
        main_menu()
        
        # The difficulty selection
        chosen_difficulty = difficulty_menu()
        if chosen_difficulty is None:
            continue
        
        # Setting the initial speed based on the chosen difficulty
=======
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
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
        if chosen_difficulty == "EASY":
            initial_speed = 5
        elif chosen_difficulty == "MEDIUM":
            initial_speed = 7.5
        else:
            initial_speed = 10

<<<<<<< HEAD
        # Starting the game
        result = game_snake(initial_speed)
        # If the game is over, the game over menu is displayed
        if result == "game_over":
            action = game_over_menu()
            # If the player wants to play again, the game starts again
            if action == "again":
                continue
            # If the player wants to go to the main menu, the game goes back to the main menu
            elif action == "menu":
=======
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
>>>>>>> bd82d67929bb8a6c7274293d39cde6ef50cb25b3
                continue

if __name__ == "__main__":
    main()