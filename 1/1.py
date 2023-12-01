import pygame
import sys
import re


with open("input.txt", 'r') as f:
    lines = f.readlines()

def first(lines):
    total_sum = 0
    for line in lines:
        if len(line) == 0:
            continue
        digits = []
        for character in line:
            if character.isnumeric():
                digits.append(int(character))
        number = digits[0] * 10 + digits[-1]
        total_sum += number

    return total_sum

def second(lines):
    total_sum = 0
    possible_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    reverse_digits = [s[::-1] for s in possible_digits]
    pattern = re.compile("|".join(re.escape(digit) for digit in possible_digits))
    reverse_pattern = re.compile("|".join(re.escape(digit) for digit in reverse_digits))
    for line in lines:
        match = pattern.search(line).group()
        reverse_match = reverse_pattern.search(line[::-1]).group()

        print(line, match, reverse_match)

        if match.isnumeric():
            first_digit = int(match)
        else:
            first_digit = int(possible_digits.index(match)) + 1

        if reverse_match.isnumeric():
            second_digit = int(reverse_match)
        else:
            second_digit = int(reverse_digits.index(reverse_match)) + 1

        print(first_digit, second_digit)
        total_sum += first_digit * 10
        total_sum += second_digit


    return total_sum

def second_for_pygame(line):
    possible_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    reverse_digits = [s[::-1] for s in possible_digits]
    pattern = re.compile("|".join(re.escape(digit) for digit in possible_digits))
    reverse_pattern = re.compile("|".join(re.escape(digit) for digit in reverse_digits))
    match = pattern.search(line)
    reverse_match = reverse_pattern.search(line[::-1])

    match_indices = [i for i in range(match.start(), match.end())]
    reverse_match_indices = [i for i in range(len(line) - (reverse_match.end()), len(line) - (reverse_match.start()))]

    return (match_indices, reverse_match_indices)

print(second_for_pygame("boneas9three"))

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AoC Day 1")

# Font settings
font = pygame.font.SysFont("monospace", 36)
text_lines = [line.strip() for line in lines]
for text_line in text_lines:
    if len(text_line) > 30:
        text_lines.remove(text_line)

# Calculate text positions dynamically for centering
text_positions = []
for i, line in enumerate(text_lines):
    rendered_text = font.render(line, True, (0, 0, 0))
    text_x = (WIDTH - rendered_text.get_width()) // 2
    text_y = i * 5*font.get_height() // 2
    text_positions.append((text_x, text_y))

text_indices = [second_for_pygame(text_line) for text_line in text_lines]

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

def render_line(line, position, indices, screen):
    rendered_text = font.render(line, True, (0, 0, 0))
    screen.blit(rendered_text, position)
    ESTIMATED_FONT_WIDTH = 22
    for i,letter in enumerate(line):
        if i in indices[0]:
            x = position[0] + ESTIMATED_FONT_WIDTH*i
            rendered_letter = font.render(letter, True, (0, 255, 0))
            screen.blit(rendered_letter, (x, position[1]))
        elif i in indices[1]:
            x = position[0] + ESTIMATED_FONT_WIDTH * i
            rendered_letter = font.render(letter, True, (255, 0, 0))
            screen.blit(rendered_letter, (x, position[1]))


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update text positions for vertical scrolling effect
    for i in range(len(text_lines)):
        text_positions[i] = (text_positions[i][0], text_positions[i][1] - 4)  # Adjust scrolling speed as needed

    # Draw background
    screen.fill(WHITE)

    # Draw scrolling text lines
    for i, line in enumerate(text_lines):
        render_line(line, text_positions[i], text_indices[i], screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()