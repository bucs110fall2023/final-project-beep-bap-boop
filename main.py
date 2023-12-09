import pygame
from src.monkeytype_game import MonkeyTypeGame

def main():
    # Initialize Pygame
    pygame.init()

    monkeytype_game = MonkeyTypeGame()
    monkeytype_game.run()

main()
