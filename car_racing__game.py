import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load and scale images
road_bg = pygame.image.load("Project/road.png")
road_bg = pygame.transform.scale(road_bg, (width, height))

player_car = pygame.image.load("Project/car.webp")
enemy_car = pygame.image.load("Project/enemyy.png")
player_car = pygame.transform.scale(player_car, (50, 100))
enemy_car = pygame.transform.scale(enemy_car, (50, 100))

# Background scroll variables
bg_y1 = 0
bg_y2 = -height
scroll_speed = 5

# Car positions
player_x = 175
player_y = 500
player_speed = 5

enemy_x = random.randint(0, width - 50)
enemy_y = -100
enemy_speed = 5

score = 0
font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()

def show_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

# Game loop
running = True
while running:
    clock.tick(60)

    # Move background
    bg_y1 += scroll_speed
    bg_y2 += scroll_speed
    if bg_y1 >= height:
        bg_y1 = -height
    if bg_y2 >= height:
        bg_y2 = -height

    # Draw scrolling background
    screen.blit(road_bg, (0, bg_y1))
    screen.blit(road_bg, (0, bg_y2))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - 50:
        player_x += player_speed

    # Move enemy
    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_y = -100
        enemy_x = random.randint(0, width - 50)
        score += 1
        enemy_speed += 0.3

    # Collision detection
    if (player_x < enemy_x + 50 and
        player_x + 50 > enemy_x and
        player_y < enemy_y + 100 and
        player_y + 100 > enemy_y):
        running = False

    # Draw cars and score
    screen.blit(player_car, (player_x, player_y))
    screen.blit(enemy_car, (enemy_x, enemy_y))
    show_score()
    pygame.display.update()

# Game over screen
screen.fill(RED)
text = font.render("Game Over!", True, WHITE)
screen.blit(text, (120, 250))
pygame.display.update()
pygame.time.wait(2000)
pygame.quit()
