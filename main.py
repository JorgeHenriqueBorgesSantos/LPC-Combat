import pygame
from sys import exit

pygame.init()

# Variables
Game_clock = pygame.time.Clock()
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 10
FPS = 35
background = 145, 22, 3
screen_width = 1150
screen_height = 750
Barrier_color = (217, 177, 69)
P1_color = (91, 227, 116)
P2_color = (31, 104, 163)

# Players Moves
pressed_keys = pygame.key.get_pressed()

keys_P1 = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT
}

keys_P2 = {
    "up": pygame.K_w,
    "down": pygame.K_s,
    "left": pygame.K_a,
    "right": pygame.K_d
}

# Text
score_font = pygame.font.Font('Fonts/PressStart2P.ttf', 60)

score_text1 = score_font.render('0', True, P1_color)
score_text1_rect = score_text1.get_rect()

score_text2 = score_font.render('0', True, P2_color)
score_text2_rect = score_text2.get_rect()

# Display Configuration
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Combat!')
screen.fill(background)

# Walls
left_wall = pygame.Surface((20, screen_height - 80))
left_wall.fill(Barrier_color)

right_wall = pygame.Surface((20, screen_height - 80))
right_wall.fill(Barrier_color)

upper_wall = pygame.Surface((screen_width - 40, 20))
upper_wall.fill(Barrier_color)

lower_wall = pygame.Surface((screen_width - 40, 20))
lower_wall.fill(Barrier_color)

# player 1
player_1 = pygame.image.load("Sprites/tank1.png")
player_1_x = 900
player_1_y = 640

player_1_dx = 4
player_1_dy = 3

# Player 2
player_2 = pygame.image.load("Sprites/tank2.png")

player_2_x = 90
player_2_y = 60

player_2_dx = 4
player_2_dy = 3

pygame.mouse.set_visible(False)


# Game Loop
while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Create Walls
    screen.blit(left_wall, (0, 80))
    screen.blit(right_wall, (screen_width - 20, 80))
    screen.blit(upper_wall, (20, 80))
    screen.blit(upper_wall, (20, screen_height - 20))

    # Spawn Players
    screen.blit(player_1, (120, 350))
    screen.blit(player_2, (120, 120))

    # Player_1 Moves
    if pressed_keys[keys_P1["right"]] or pressed_keys[keys_P1["left"]]:
        if pressed_keys[keys_P1["right"]]:
            player_1_dx = +1
            player_1_x = player_1_x + player_1_dx
        else:
            player_1_dx = -1
            player_1_x = player_1_x + player_1_dx

    if pressed_keys[keys_P1["up"]] or pressed_keys[keys_P1["down"]]:
        if pressed_keys[keys_P1["up"]]:
            player_1_dy = -1
            player_1_y = player_1_y + player_1_dy
        else:
            player_1_dy = +1
            player_1_y = player_1_y + player_1_dy

    # Create Scores
    screen.blit(score_text1, (300, 14))
    screen.blit(score_text2, (775, 14))

    pygame.display.update()
    Game_clock.tick(FPS)
