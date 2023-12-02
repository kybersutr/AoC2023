with open("input.txt", 'r') as f:
    lines = f.readlines()

games = []
for game in lines:
    data = game.split(':')[1].strip()
    draws = data.split(';')
    game = []
    for draw in draws:
        rgb = [0,0,0]
        colors = [x.strip() for x in draw.split(',')]
        for color in colors:
            num, name = color.split(' ')
            if name == 'red':
                rgb[0] += int(num)
            elif name == 'green':
                rgb[1] += int(num)
            elif name == 'blue':
                rgb[2] += int(num)
            else:
                raise ValueError(f"Invalid color {name}")
        game.append(rgb)
    games.append(game)

def first(games):
    total = 0
    for i, game in enumerate(games):
        game_id = i + 1
        valid = True
        for draw in game:
            print(draw)
            if draw[0] > 12 or draw[1] > 13 or draw[2] > 14:
                valid = False
                break
        if valid:
            total += game_id

    return total

def second(games):
    total = 0
    for game in games:
        power = 0
        max_r = 0
        max_g = 0
        max_b = 0
        for draw in game:
            max_r = max(max_r, draw[0])
            max_g = max(max_g, draw[1])
            max_b = max(max_b, draw[2])

        power = max_r * max_g * max_b
        total += power

    return total

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AoC Day 2")

# Font settings
font = pygame.font.Font(None, 36)

def draw_squares(red_count, green_count, blue_count):
    # Calculate square settings
    square_size = 50
    margin = 10

    # Draw red squares
    for i in range(red_count):
        pygame.draw.rect(screen, RED,
                         (WIDTH // 2 - red_count * (square_size + margin) // 2 + i * (square_size + margin),
                          HEIGHT // 2 - 2 * (square_size + margin), square_size, square_size))

    # Draw green squares
    for i in range(green_count):
        pygame.draw.rect(screen, GREEN,
                         (WIDTH // 2 - green_count * (square_size + margin) // 2 + i * (square_size + margin),
                          HEIGHT // 2 - (square_size + margin), square_size, square_size))

    # Draw blue squares
    for i in range(blue_count):
        pygame.draw.rect(screen, BLUE,
                         (WIDTH // 2 - blue_count * (square_size + margin) // 2 + i * (square_size + margin),
                          HEIGHT // 2, square_size, square_size))


def draw_max_counters(red_count, green_count, blue_count):
    # Display counters for each color
    red_counter_text = font.render(f"Red: {red_count}", True, (0, 0, 0))
    green_counter_text = font.render(f"Green: {green_count}", True, (0, 0, 0))
    blue_counter_text = font.render(f"Blue: {blue_count}", True, (0, 0, 0))

    screen.blit(red_counter_text, (10, 50))
    screen.blit(green_counter_text, (10, 80))
    screen.blit(blue_counter_text, (10, 110))

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

current_game = 0
current_draw = 0

max_r = 0
max_g = 0
max_b = 0
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_id = current_game + 1
    r = games[current_game][current_draw][0]
    g = games[current_game][current_draw][1]
    b = games[current_game][current_draw][2]

    # Draw background
    screen.fill(WHITE)

    # Draw squares with different counts for each color
    draw_squares(red_count=r, green_count=g, blue_count=b)
    draw_max_counters(red_count=max_r, green_count=max_g, blue_count=max_b)

    # Draw text "Game 1" in the top left corner
    game_text = font.render(f"Game {game_id}", True, (0, 0, 0))
    screen.blit(game_text, (10, 10))

    # Update the display
    pygame.display.flip()

    max_r = max(r, max_r)
    max_b = max(b, max_b)
    max_g = max(g, max_g)

    current_draw += 1
    if current_draw >= len(games[current_game]):
        current_game += 1
        current_draw = 0
        max_r = 0
        max_g = 0
        max_b = 0
    if current_game >= len(games):
        break

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

