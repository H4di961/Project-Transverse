from pygame import*
from math import*
init() # initialise différentes choses de pygame

fenetre = display.set_mode((#, #), RESIZABLE)
fond = image.load("Bomberman_background.jpeg").convert()
perso = image.load("").convert_alpha()

#matrice
matrice = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0]]
    
#temps
clock = pygame.time.Clock()

#mvt

x = 0
y = 0
xp = 0
yp = 0

while True :
    clock.tick(180)
    if clock.tick == 0: quit()
    keyg=key.get_pressed() # prend la cartographie du clavier, la variable contient
    # gestion du clavier
    
    if keyg[K_w]:yp=yp-1 # gestion des déplacements de mon personnage avec wasd.
    if keyg[K_s]:yp=yp+1
    if keyg[K_a]:xp=xp-1
    if keyg[K_d]:xp=xp+1
    
    if keyg[K_UP]:y=y-1 # gestion des déplacements de mon personnage à l'aide des flèches.
    if keyg[K_DOWN]:y=y+1
    if keyg[K_LEFT]:x=x-1
    if keyg[K_RIGHT]:x=x+1
    
fenetre.blit(fond, (0,0))
