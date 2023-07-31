import pygame
import random

# Initialize Pygame
pygame.init()

# Constants for the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Invaders"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player constants
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5

# Enemy constants
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_SPEED = 3
ENEMY_COUNT = 10

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# Create the player
player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

# Create the enemies
enemies = []
for i in range(ENEMY_COUNT):
    enemy = pygame.Rect(random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH), random.randint(0, 300), ENEMY_WIDTH, ENEMY_HEIGHT)
    enemies.append(enemy)

# Create the clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
        player.x += PLAYER_SPEED

    # Draw the player
    pygame.draw.rect(screen, WHITE, player)

    # Move and draw enemies
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        pygame.draw.rect(screen, RED, enemy)

    # Check for collision with enemies
    for enemy in enemies:
        if player.colliderect(enemy):
            print("Game Over!")
            running = False

    # Respawn enemies if they go off the screen
    for enemy in enemies:
        if enemy.top > SCREEN_HEIGHT:
            enemy.y = 0
            enemy.x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit the game
pygame.quit()

