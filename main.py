import pygame
from sys import exit

pygame.init()

# Variables
Game_clock = pygame.time.Clock()
FPS = 35
background = 145, 22, 3
screen_width = 1150
screen_height = 750
Barrier_color = (217, 177, 69)
P1_color = (91, 227, 116)
P2_color = (31, 104, 163)

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

# Game Loop
while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(left_wall, (0, 80))
    screen.blit(right_wall, (screen_width - 20, 80))
    screen.blit(upper_wall, (20, 80))
    screen.blit(upper_wall, (20, screen_height - 20))

    screen.blit(score_text1, (300, 14))
    screen.blit(score_text2, (775, 14))

    pygame.display.update()
    Game_clock.tick(FPS)
