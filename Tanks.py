import pygame
import math as m

pygame.init()

# Variables
Game_clock = pygame.time.Clock()
PLAYER_WIDTH = 41
PLAYER_HEIGHT = 63
FPS = 35
background = 145, 22, 3
screen_width = 1000
screen_height = 750
speed = 10

# Display Configuration
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Combat!')
screen.fill(background)

# player 1
p1_spin = 0.00
player_1_image = pygame.image.load("Sprites/tank1.png")
player_1 = pygame.Rect(500, 500, PLAYER_WIDTH, PLAYER_HEIGHT)


# Player 2
player_2_image = pygame.image.load("Sprites/tank2.png")
player_2 = pygame.Rect(240, 350, PLAYER_WIDTH, PLAYER_HEIGHT)
p2_spin = 0

pygame.mouse.set_visible(False)

# Game Loop
while True:
    Game_clock.tick(FPS)
    screen.fill(background)
    key_pressed_is = pygame.key.get_pressed()
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Player One Actions
    if key_pressed_is[pygame.K_d]:
        p1_spin -= 1
        pygame.transform.rotate(player_1_image, p1_spin)
    if key_pressed_is[pygame.K_a]:
        p1_spin += 1

    if key_pressed_is[pygame.K_w]:
        player_1.x += m.cos(p1_spin) * speed
        player_1.y += m.sin(p1_spin) * speed


    # Player Two Actions
    if key_pressed_is[pygame.K_UP]:
        player_2.x += m.cos(p2_spin) * speed
        player_2.y += m.sin(p2_spin) * speed

    # Spawn Players
    screen.blit(player_1_image, (player_1.x, player_1.y))
    screen.blit(player_2_image, (player_2.x, player_2.y))

    pygame.display.update()
