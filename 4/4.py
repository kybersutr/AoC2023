with open('input.txt', 'r') as f:
    input_lines = f.readlines()

def get_winning_amount(num):
    if num == 0:
        return 0

    amount = 1
    for i in range(num-1):
        amount = 2*amount
    return amount

def first(lines):
    total = 0
    for line in lines:
        numbers = line.split(':')[1]
        numbers_parsed = list(map(lambda x: x.split(), numbers.split('|')))
        winning_numbers = set(numbers_parsed[0])
        scratched_numbers = set(numbers_parsed[1])
        winning = winning_numbers.intersection(scratched_numbers)
        total += get_winning_amount(len(winning))
    return total

def second(lines):
    card_numbers = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        numbers = line.split(':')[1]
        numbers_parsed = list(map(lambda x: x.split(), numbers.split('|')))
        winning_numbers = set(numbers_parsed[0])
        scratched_numbers = set(numbers_parsed[1])
        winning = winning_numbers.intersection(scratched_numbers)
        winning_count = len(winning)
        for j in range(winning_count):
            try:
                card_numbers[i + j + 1] += card_numbers[i]
            except IndexError:
                break
        print(card_numbers)

    return sum(card_numbers)

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RECTANGLE_COLOR = (0, 0, 255)
TEXT_COLOR = (255, 255, 255)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Rectangles Animation")

# Font settings
font = pygame.font.Font(None, 20)

# Rectangle settings
rectangle_width = 50
rectangle_height = 30
margin = 20

# Animation settings
animation_duration = 60  # Number of frames for the animation
animation_frames = 0

# Left rectangle initial position and size
left_rect_initial = (-rectangle_width - margin, HEIGHT // 2 - rectangle_height // 2, rectangle_width, rectangle_height)
left_rect_animation = list(left_rect_initial)

# Right rectangle initial position and size
right_rect_initial = (WIDTH + margin, HEIGHT // 2 - rectangle_height // 2, rectangle_width, rectangle_height)
right_rect_animation = list(right_rect_initial)

# Flag to determine when to start the animation for the right rectangle
start_right_animation = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.fill(WHITE)

    # Update left rectangle animation
    if not start_right_animation and animation_frames < animation_duration:
        # Calculate animation progress
        progress = animation_frames / animation_duration

        # Calculate new position based on animation progress
        left_rect_animation[0] = (WIDTH // 2 - rectangle_width // 2 + (left_rect_initial[0] + rectangle_width + margin) * progress)

        # Calculate new size based on animation progress
        left_rect_animation[2] = rectangle_width + rectangle_width * progress

        # Draw left rectangle
        pygame.draw.rect(screen, RECTANGLE_COLOR, left_rect_animation)

        # Draw changing text inside the left rectangle
        text = font.render("abc", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(left_rect_animation[0] + left_rect_animation[2] // 2, left_rect_animation[1] + left_rect_animation[3] // 2))
        screen.blit(text, text_rect)

        # Update animation frame
        animation_frames += 1
    else:
        # Reset animation frames and flag
        animation_frames = 0
        start_right_animation = True

        # Draw left rectangle in its initial position
        pygame.draw.rect(screen, RECTANGLE_COLOR, left_rect_initial)

        # Draw initial text inside the left rectangle
        text = font.render("abc", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(left_rect_initial[0] + left_rect_initial[2] // 2, left_rect_initial[1] + left_rect_initial[3] // 2))
        screen.blit(text, text_rect)

    # Update right rectangle animation
    if start_right_animation and animation_frames < animation_duration:
        # Calculate animation progress
        progress = animation_frames / animation_duration

        # Calculate new position based on animation progress
        right_rect_animation[0] = (WIDTH // 2 - rectangle_width // 2 - (right_rect_initial[0] + rectangle_width + margin) * progress)

        # Calculate new size based on animation progress
        right_rect_animation[2] = rectangle_width + rectangle_width * progress

        # Draw right rectangle
        pygame.draw.rect(screen, RECTANGLE_COLOR, right_rect_animation)

        # Draw changing text inside the right rectangle
        text = font.render("xyz", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(right_rect_animation[0] + right_rect_animation[2] // 2, right_rect_animation[1] + right_rect_animation[3] // 2))
        screen.blit(text, text_rect)

        # Update animation frame
        animation_frames += 1
    else:
        # Reset animation frames
        animation_frames = 0

        # Draw right rectangle in its initial position
        pygame.draw.rect(screen, RECTANGLE_COLOR, right_rect_initial)

        # Draw initial text inside the right rectangle
        text = font.render("xyz", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(right_rect_initial[0] + right_rect_initial[2] // 2, right_rect_initial[1] + right_rect_initial[3] // 2))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()



