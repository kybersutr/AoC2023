with open('input.txt', 'r') as f:
    content = f.read()

records = list(map(lambda i: (int(i[0]), int(i[1])), zip(*[x.split()[1:] for x in content.split('\n')[0:2]])))
true_record = [int(''.join(y)) for y in [x.split()[1:] for x in content.split('\n')[0:2]]]

def first():
    total = 1
    for record in records:
        time = record[0]
        distance = record[1]

        possibilities = 0
        for push in range(time):
            traveled_distance = (time - push) * push
            if traveled_distance > distance:
                possibilities += 1


        total *= possibilities

    return total

def second():
    time = true_record[0]
    distance = true_record[1]

    possibilities = 0
    for push in range(time):
        traveled_distance = (time - push)*push
        if traveled_distance > distance:
            possibilities += 1

    return possibilities

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)

MILLIMETER = WIDTH / 13
UNIT_DISTANCE = MILLIMETER / 100

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AoC Day 6")

IMG_SIZE = (120, 80)

time = 0
MAX_TIME = 700

background_image = pygame.image.load("background.png")
# Load boat images and resize them
boat_images = [
    pygame.transform.scale(pygame.image.load('boat1.png'), IMG_SIZE),
    pygame.transform.scale(pygame.image.load('boat2.png'), IMG_SIZE),
    pygame.transform.scale(pygame.image.load('boat3.png'), IMG_SIZE),
    pygame.transform.scale(pygame.image.load('boat4.png'), IMG_SIZE),
    pygame.transform.scale(pygame.image.load('boat5.png'), IMG_SIZE),
    pygame.transform.scale(pygame.image.load('boat6.png'), IMG_SIZE),
    pygame.transform.scale(pygame.image.load('boat7.png'), IMG_SIZE),
    pygame.transform.scale(pygame.image.load('boat8.png'), IMG_SIZE)
]

# Boat class
class Boat(pygame.sprite.Sprite):
    def __init__(self, image, speed, scale):
        super().__init__()
        self.image = image
        self.waiting_time = speed * 100
        self.rect = self.image.get_rect()
        self.x = 0
        self.rect.x = 0
        self.index = boat_images.index(image)
        self.rect.y = 5 + self.index * (IMG_SIZE[1])  # Random initial y position
        self.speed = speed
        self.scale = scale
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * scale), int(self.rect.height * scale)))
        self.highlighted = False
        self.offset = 3

    def update(self):
        if time > MAX_TIME:
            return
        if time > self.waiting_time:
            if self.highlighted:
                self.highlighted = False
                self.rect.y -= self.offset
            self.x += self.speed * UNIT_DISTANCE
            self.rect.x = self.x

        elif not self.highlighted and time % 5 == 0:
            self.rect.y += self.offset
            self.highlighted = True

        elif time % 5 == 0:
            self.rect.y -= self.offset
            self.highlighted = False

def draw_vertical_line(x):
    pygame.draw.line(screen, (255, 0, 0), (x, 0), (x, HEIGHT), 2)

def display_timer():
    font = pygame.font.Font(None, 36)
    text = font.render(f'Time: {time / 100}', True, (0, 0, 0))
    screen.blit(text, (WIDTH - 150, 10))

# Create a sprite group for boats
all_sprites = pygame.sprite.Group()

# Create boats with different speeds and images
boats = [Boat(image, speed, 0.5) for image, speed in zip(boat_images, range(0, 8))]

# Add boats to the sprite group
all_sprites.add(boats)

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Draw the background image
    screen.blit(background_image, (0, 0))

    draw_vertical_line(9*MILLIMETER)

    display_timer()

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

    if time <= MAX_TIME:
        time += 1

# Quit Pygame
pygame.quit()
sys.exit()
