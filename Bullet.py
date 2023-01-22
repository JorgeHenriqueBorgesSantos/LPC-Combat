import pygame

# Variables
bullet_width = 1
bullet_height = 1
radius = 3
bul_speed = 7

# ball
bullet_sprite = pygame.image.load("Sprites/ball.png")
bullet_hit = 0
bullet = pygame.Rect(0, 0, bullet_width, bullet_height)
bullet_radius = radius
