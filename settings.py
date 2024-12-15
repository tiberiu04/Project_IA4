import pygame

class Settings:
    def __init__(self):
        # Screen Settings
        self.screen_width = 800
        self.screen_height = 600
        self.fps = 60

        # Color Palette
        self.background_color = (20, 20, 40)  # Dark blue-black
        self.snake_color = (0, 255, 0)  # Bright green
        self.food_color = (255, 0, 0)  # Bright red
        self.obstacle_color = (100, 100, 100)  # Gray