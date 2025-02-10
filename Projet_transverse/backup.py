import pygame
from pygame.locals import *
from math import *

pygame.init()  # Initialize Pygame

# Set up the display
fenetre = pygame.display.set_mode((800, 600), RESIZABLE)
fond = pygame.image.load("Bomberman_background.jpeg").convert()
perso = pygame.image.load("").convert_alpha()  # Replace with the correct image file name

# Matrice
matrice = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Time
clock = pygame.time.Clock()

# Movement
x = 0
y = 0
xp = 0
yp = 0

running = True
while running:
    clock.tick(180)  # Control the frame rate

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keyg = pygame.key.get_pressed()  # Get the state of all keyboard buttons

    # Handle movement with WASD
    if keyg[K_w]: yp -= 1
    if keyg[K_s]: yp += 1
    if keyg[K_a]: xp -= 1
    if keyg[K_d]: xp += 1

    # Handle movement with arrow keys
    if keyg[K_UP]: y -= 1
    if keyg[K_DOWN]: y += 1
    if keyg[K_LEFT]: x -= 1
    if keyg[K_RIGHT]: x += 1

    # Update the display
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, (xp, yp))  # Draw the character at the new position
    pygame.display.flip()  # Update the full display Surface to the screen

pygame.quit()  # Quit Pygame