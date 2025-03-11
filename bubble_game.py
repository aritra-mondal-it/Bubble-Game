import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Pop!")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Bubble properties
bubble_radius = 30
bubbles = []  # List to store bubble positions and speeds

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

def create_bubble():
    x = random.randint(bubble_radius, WIDTH - bubble_radius)
    y = HEIGHT + bubble_radius  # Start below the screen
    speed_y = random.uniform(-5, -2)  # Move upwards
    bubbles.append([x, y, speed_y])

def draw_bubbles():
    for bubble in bubbles:
        pygame.draw.circle(screen, BLUE, (int(bubble[0]), int(bubble[1])), bubble_radius)

def move_bubbles():
    for bubble in bubbles:
        bubble[1] += bubble[2]

def check_collisions(mouse_x, mouse_y):
    global score
    popped_bubbles = []
    for i, bubble in enumerate(bubbles):
        distance = ((mouse_x - bubble[0]) ** 2 + (mouse_y - bubble[1]) ** 2) ** 0.5
        if distance < bubble_radius:
            popped_bubbles.append(i)
            score += 1

    # Remove popped bubbles
    popped_bubbles.sort(reverse=True) #remove highest index first
    for index in popped_bubbles:
        del bubbles[index]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_collisions(mouse_x, mouse_y)

    # Create new bubbles
    if random.random() < 0.02:  # Adjust frequency as needed
        create_bubble()

    # Move and draw bubbles
    move_bubbles()

    # Clear screen
    screen.fill(WHITE)

    # Draw bubbles
    draw_bubbles()

    # Remove off-screen bubbles
    bubbles = [bubble for bubble in bubbles if bubble[1] > -bubble_radius]

    # Draw score
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()