import pygame
import random
import time

class MonkeyTypeGame:
    def __init__(self):
        # Constants
        self.WIDTH, self.HEIGHT = 1000, 600
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.FONT_SIZE = 36
        self.FONT = pygame.font.Font(None, self.FONT_SIZE)

        # ... (other constants and variables)

        # Variables
        self.current_phrase = ""
        self.input_text = ""
        self.words_typed = 0
        self.mistakes = 0
        self.level = 1
        self.word_bank = ["apple", "banana", "orange", "grape", "watermelon", "pineapple", "strawberry", "blueberry",
                          "computer", "keyboard", "monitor", "mouse", "laptop", "desktop", "software", "hardware",
                          "python", "programming", "language", "coding", "developer", "variable", "function", "algorithm"]

        self.generate_new_phrase()

        # Timing variables
        self.start_time = time.time()
        self.time_limit = 60  # in seconds
        self.start_game_time = time.time()

        # Pygame setup
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("MonkeyType Game")
        self.clock = pygame.time.Clock()

    def generate_new_phrase(self):
        self.current_phrase = ' '.join(random.sample(self.word_bank, self.level + 4))

    def draw_text(self, text, x, y):
        text_obj = self.FONT.render(text, True, self.BLACK)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        self.window.blit(text_obj, text_rect)

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.handle_return_key()
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode

    def handle_return_key(self):
        if self.input_text == self.current_phrase:
            if time.time() - self.start_time < self.time_limit:
                self.words_typed += len(self.current_phrase.split())
                self.level += 1
                self.generate_new_phrase()
            else:
                self.mistakes += 1
            self.input_text = ""
        else:
            self.mistakes += 1
            self.input_text = ""

    def run(self):
        running = True

        while running:
            self.window.fill(self.WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.handle_input(event)

            self.draw_text("Type the phrase:", 20, 20)
            self.draw_text("Type: " + self.current_phrase, 20, 60)

            self.draw_text("Your typing:", 20, 120)
            input_text_surface = self.FONT.render(self.input_text, True, self.BLACK)
            self.window.blit(input_text_surface, (20, 160))

            time_elapsed = time.time() - self.start_game_time
            time_left = max(self.time_limit - time_elapsed, 0)
            self.draw_text("Time left: {:.2f}".format(time_left), self.WIDTH - 200, self.HEIGHT - 40)

            elapsed_time = time_elapsed
            minutes_passed = max(elapsed_time / 60, 1 / 60)
            words_per_minute = int(self.words_typed / minutes_passed)
            self.draw_text("Words Per Minute: " + str(words_per_minute), self.WIDTH - 300, self.HEIGHT - 80)
            self.draw_text("Level: " + str(self.level), 20, self.HEIGHT - 40)
            self.draw_text("Words Typed: " + str(self.words_typed), 20, self.HEIGHT - 80)
            self.draw_text("Mistakes: " + str(self.mistakes), 20, self.HEIGHT - 120)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

