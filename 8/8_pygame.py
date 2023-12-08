import math

with open("ghost_input.txt", 'r') as f:
    lines = f.readlines()

instructions = list(map(lambda x: 0 if x == 'L' else 1, lines[0].strip()))

steps = {}
for line in lines[2:]:
    parts = list(map(lambda x: x.strip(), line.split('=')))
    left = parts[1][1:4]
    right = parts[1][6:9]
    steps[parts[0]] = (left, right)

def first(instructions, steps):
    counter = 0
    current_index = 0
    current_position = 'AAA'
    while current_position != 'ZZZ':
        choice = steps[current_position]
        direction = instructions[current_index]
        current_position = choice[direction]
        current_index += 1
        current_index = current_index % len(instructions)
        counter += 1

    return counter

def modified_first(instructions, steps, start):
    counter = 0
    current_index = 0
    current_position = start
    while not current_position.endswith('Z'):
        choice = steps[current_position]
        direction = instructions[current_index]
        current_position = choice[direction]
        current_index += 1
        current_index = current_index % len(instructions)
        counter += 1

    return counter

def second(instructions, steps):
    counter = 0
    current_index = 0
    current_positions = list(filter(lambda x: x.endswith('A'), steps.keys()))
    while not all(map(lambda x: x.endswith('Z'), current_positions)):
        print(current_positions)
        direction = instructions[current_index]
        for i in range(len(current_positions)):
            position = current_positions[i]
            choice = steps[position]
            current_positions[i] = choice[direction]
        current_index += 1
        current_index = current_index % len(instructions)
        counter += 1

        if counter % 10000 == 0:
            print(counter)

    return counter

def second_smarter(instructions, steps):
    current_positions = list(filter(lambda x: x.endswith('A'), steps.keys()))
    counters = [0 for _ in range(len(current_positions))]
    for i in range(len(current_positions)):
        counters[i] = modified_first(instructions, steps, current_positions[i])

    return math.lcm(*counters)

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
NODE_RADIUS = 20

# Function to calculate coordinates for ghosts
def calculate_position_node(node, total_nodes):
    radius = min(WIDTH, HEIGHT) // 3  # Adjust the radius as needed
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    # Calculate equally spaced angles for each node
    angle = (2 * math.pi * list(steps.keys()).index(node) / total_nodes) - math.pi / 2

    x = center_x + int(radius * math.cos(angle))
    y = center_y + int(radius * math.sin(angle))
    return x, y

nodes_positions = [calculate_position_node(node, len(steps.keys())) for node in steps.keys()]

# Colors
BACKGROUND_COLOR = (241, 186, 114)
BLACK = (0, 0, 0)

# Load and resize ghost image
original_ghost_image = pygame.image.load('ghost.png')
ghost_size = (NODE_RADIUS * 2 + 5, NODE_RADIUS * 2 + 5)  # Slightly larger than NODE_RADIUS
ghost_image = pygame.transform.scale(original_ghost_image, ghost_size)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AoC Day 3")

nodes_list = list(steps.keys())

# Ghost sprite class
class Ghost(pygame.sprite.Sprite):
    def __init__(self, prefix, loop_offset):
        super().__init__()
        self.nodes = prefix
        self.loop_offset = loop_offset
        self.current_node_index = 0
        self.image = ghost_image
        self.position = nodes_positions[nodes_list.index(self.nodes[self.current_node_index])]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

    def update(self):
        self.position = nodes_positions[nodes_list.index(self.nodes[self.current_node_index])]
        self.rect.topleft = self.position
        self.current_node_index = (self.current_node_index + 1) % len(self.nodes)
        if self.current_node_index == 0:
            self.current_node_index += self.loop_offset

def calculate_position_ghost(ghost):
    return nodes_positions[ghost.current_node_index]

# Create sprite groups
all_sprites = pygame.sprite.Group()
ghosts = pygame.sprite.Group()

# Create ghosts
ghost1 = Ghost(['11A', '11B', '11Z'], 1)
ghost2 = Ghost(['22A', '22B', '22C', '22Z'], 1)

# Add ghosts to sprite groups
all_sprites.add(ghost1, ghost2)
ghosts.add(ghost1, ghost2)


# Function to draw nodes and connections
def draw_nodes_and_ghosts():
    screen.fill(BACKGROUND_COLOR)  # Set background color

    total_nodes = len(steps)

    # Draw connections
    for node, (left_node, right_node) in steps.items():
        x1, y1 = nodes_positions[nodes_list.index(node)]
        x2, y2 = nodes_positions[nodes_list.index(left_node)]
        pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 2)

        x4, y4 = nodes_positions[nodes_list.index(right_node)]
        pygame.draw.line(screen, BLACK, (x1, y1), (x4, y4), 2)

    # Draw nodes and display node names
    for node, _ in steps.items():
        x, y = calculate_position_node(node, total_nodes)
        pygame.draw.circle(screen, BLACK, (x, y), NODE_RADIUS)

        # Display node name in white text
        font = pygame.font.Font(None, 20)
        text = font.render(node, True, (255, 255, 255))
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

    # Draw ghost sprites
    all_sprites.draw(screen)


# Set up the clock to control the frame rate
clock = pygame.time.Clock()

time = 0
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ghost positions
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ghosts.update()

    # Draw nodes, connections, and ghosts
    draw_nodes_and_ghosts()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

