import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_HEIGHT = HEIGHT - 50

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Runner")

# Load Assets
player_img = pygame.image.load("Snapchat-1609693769.jpg")  # Load user image
player_img = pygame.transform.scale(player_img, (40, 40))  # Resize to fit character size

obstacle_img = pygame.Surface((30, 30))
obstacle_img.fill((255, 0, 0))

# Player Properties
player_x = 100
player_y = GROUND_HEIGHT - 40
player_vel_y = 0
gravity = 0.5
jump_power = -10
is_jumping = False

# Obstacles
obstacles = []
obstacle_speed = 5
spawn_timer = 0

# Game Loop
running = True
clock = pygame.time.Clock()
score = 0

while running:
    screen.fill(WHITE)
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not is_jumping:
            player_vel_y = jump_power
            is_jumping = True

    # Player Physics
    player_vel_y += gravity
    player_y += player_vel_y
    if player_y >= GROUND_HEIGHT - 40:
        player_y = GROUND_HEIGHT - 40
        is_jumping = False
    
    # Spawn Obstacles
    spawn_timer += 1
    if spawn_timer > 50:
        obstacles.append([WIDTH, GROUND_HEIGHT - 30])
        spawn_timer = 0
    
    # Move Obstacles
    for obstacle in obstacles:
        obstacle[0] -= obstacle_speed
    
    # Remove Off-Screen Obstacles
    obstacles = [obs for obs in obstacles if obs[0] > -30]
    
    # Collision Detection
    for obstacle in obstacles:
        if player_x < obstacle[0] + 30 and player_x + 40 > obstacle[0] and player_y + 40 > obstacle[1]:
            running = False  # Game Over
    
    # Draw Player
    screen.blit(player_img, (player_x, player_y))
    
    # Draw Obstacles
    for obstacle in obstacles:
        screen.blit(obstacle_img, (obstacle[0], obstacle[1]))
    
    # Update Score
    score += 1
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()
