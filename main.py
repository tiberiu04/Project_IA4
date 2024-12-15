import pygame
import random
import sys
from enum import Enum, auto

class GameState(Enum):
    MAIN_MENU = auto()
    DIFFICULTY_SELECT = auto()
    PLAYING = auto()
    GAME_OVER = auto()
    SETTINGS = auto()

class SnakeGame:
    def __init__(self):
        pygame.init()
    def _quit_game(self):
        pygame.quit()

def main():
    game = SnakeGame()
    game._quit_game()

if __name__ == '__main__':
    main()