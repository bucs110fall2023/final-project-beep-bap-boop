import pygame
import random
import string
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Create a window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MonkeyType Game")

# Variables
current_phrase = ""
input_text = ""
words_typed = 0
mistakes = 0
level = 1
word_bank = ["apple", "banana", "orange", "grape", "watermelon", "pineapple", "strawberry", "blueberry",
             "computer", "keyboard", "monitor", "mouse", "laptop", "desktop", "software", "hardware",
             "python", "programming", "language", "coding", "developer", "variable", "function", "algorithm"]

def generate_phrase(word_bank, num_words):
    return ' '.join(random.sample(word_bank, num_words))

current_phrase = generate_phrase(word_bank, 5)
start_time = time.time()
time_limit = 60  # in seconds
start_game_time = time.time()

# Function to display text on the screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

running = True
clock = pygame.time.Clock()

while running:
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                if input_text == current_phrase:
                    if time.time() - start_time < time_limit:
                        words_typed += len(current_phrase.split())
                        level += 1
                        current_phrase = generate_phrase(word_bank, level + 4)
                    else:
                        mistakes += 1
                    input_text = ""
                else:
                    mistakes += 1
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    current_phrase_text = FONT.render("Type: " + current_phrase, True, BLACK)
    draw_text("Type the phrase:", FONT, BLACK, window, 20, 20)
    window.blit(current_phrase_text, (20, 60))

    # Display user's input
    input_text_surface = FONT.render(input_text, True, BLACK)
    draw_text("Your typing:", FONT, BLACK, window, 20, 120)
    window.blit(input_text_surface, (20, 160))

    time_elapsed = time.time() - start_game_time
    time_left = max(time_limit - time_elapsed, 0)
    time_text = "Time left: {:.2f}".format(time_left)
    draw_text(time_text, FONT, BLACK, window, WIDTH - 200, HEIGHT - 40)

    elapsed_time = time_elapsed
    minutes_passed = max(elapsed_time / 60, 1 / 60)
    words_per_minute = int(words_typed / minutes_passed)
    draw_text("Words Per Minute: " + str(words_per_minute), FONT, BLACK, window, WIDTH - 300, HEIGHT - 80)
    draw_text("Level: " + str(level), FONT, BLACK, window, 20, HEIGHT - 40)
    draw_text("Words Typed: " + str(words_typed), FONT, BLACK, window, 20, HEIGHT - 80)
    draw_text("Mistakes: " + str(mistakes), FONT, BLACK, window, 20, HEIGHT - 120)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
