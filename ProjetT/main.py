from pygame import *
from math import *
from random import *
from pygame import mixer
import pygame
def start_bomberman(surface, show_path, player_alg, en1_alg, en2_alg, en3_alg, tile_size):
    """Starts the Bomberman game."""
    init()
    fenetre = surface  # Use the surface passed from the menu


    fenetre = display.set_mode((600, 600), RESIZABLE)

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 24)
    liste_bombes_p1 = []
    liste_bombes_p2 = []

    # musique

    music_fond = mixer.Sound("Megalovania.mp3")
    music_fond.set_volume(2.0)
    music_fond.play(-1)

    explosion_bombe = mixer.Sound("mixkit-8-bit-bomb-explosion-2811.wav")
    explosion_bombe.set_volume(0.2)

    fond = image.load("bomberman_background.png").convert()
    boots = image.load("boots.png").convert_alpha()  # 5 dans la matrice
    for x in range(boots.get_size()[0]):
        for y in range(boots.get_size()[1]):
            (r, v, b, t) = boots.get_at((x, y))
            if r + b + v > 700:
                boots.set_at((x, y), (r, v, b, 0))
    a1 = image.load("images/a1.png").convert_alpha()  # 5 dans la matrice
    for x in range(a1.get_size()[0]):
        for y in range(a1.get_size()[1]):
            (r, v, b, t) = a1.get_at((x, y))
            if r + b + v > 700:
                a1.set_at((x, y), (r, v, b, 0))
    a2 = image.load("images/a2.png").convert_alpha()  # 5 dans la matrice
    for x in range(a2.get_size()[0]):
        for y in range(a2.get_size()[1]):
            (r, v, b, t) = a2.get_at((x, y))
            if r + b + v > 700:
                a2.set_at((x, y), (r, v, b, 0))
    a3 = image.load("images/a3.png").convert_alpha()  # 5 dans la matrice
    for x in range(a3.get_size()[0]):
        for y in range(a3.get_size()[1]):
            (r, v, b, t) = a3.get_at((x, y))
            if r + b + v > 700:
                a3.set_at((x, y), (r, v, b, 0))
    a4 = image.load("images/a4.png").convert_alpha()  # 5 dans la matrice
    for x in range(a4.get_size()[0]):
        for y in range(a4.get_size()[1]):
            (r, v, b, t) = a4.get_at((x, y))
            if r + b + v > 700:
                a4.set_at((x, y), (r, v, b, 0))
    a5 = image.load("images/a5.png").convert_alpha()  # 5 dans la matrice
    for x in range(a5.get_size()[0]):
        for y in range(a5.get_size()[1]):
            (r, v, b, t) = a5.get_at((x, y))
            if r + b + v > 700:
                a5.set_at((x, y), (r, v, b, 0))
    perso1 = image.load("images/perso1.png").convert_alpha()
    for x in range(perso1.get_size()[0]):
        for y in range(perso1.get_size()[1]):
            (r, v, b, t) = perso1.get_at((x, y))
            if r + b + v > 700:
                perso1.set_at((x, y), (r, v, b, 0))
    perso2 = image.load("images/perso2.png").convert_alpha()
    for x in range(perso2.get_size()[0]):
        for y in range(perso2.get_size()[1]):
            (r, v, b, t) = perso2.get_at((x, y))
            if r + b + v > 700:
                perso2.set_at((x, y), (r, v, b, 0))
    block = image.load("images/block.png").convert()  # 2 dans la matrice
    bombe = image.load("images/bombe.png").convert_alpha()  # 3 dans la matrice
    for x in range(bombe.get_size()[0]):
        for y in range(bombe.get_size()[1]):
            (r, v, b, t) = bombe.get_at((x, y))
            if r + b + v > 700:
                bombe.set_at((x, y), (r, v, b, 0))
    flamme = image.load("images/flame1.png").convert_alpha()
    for x in range(flamme.get_size()[0]):
        for y in range(flamme.get_size()[1]):
            (r, v, b, t) = flamme.get_at((x, y))
            if r + b + v > 760:
                flamme.set_at((x, y), (r, v, b, 0))  # 4 dans la matrice
    liste_im = [block, bombe, flamme, boots]
    fin1 = image.load("images/ecrandefin.png").convert()
    fin2 = image.load("images/ecrandefin1.png").convert()
    lafin = [fin2, fin1]

    # matrice
    matrice = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    # apparition au hasard des blocs:
    for l in range(len(matrice)):
        for c in range(len(matrice[0])):
            if l + c >= 4 and l + c <= 24:
                if matrice[l][c] == 0:
                    if randint(1, 10) >= 6:
                        matrice[l][c] = 2

    xp = 80
    yp = 40
    xp2 = 520
    yp2 = 520
    collision = 1
    continuer = 0
    liste_bombes = []
    liste_f = []
    vie1 = 1
    vie2 = 1
    fin = 1
    anim = [a1, a2, a3, a4, a5]
    chance_b_f = 3
    vitesse1 = 1
    vitesse2 = 1

    from special_attack import SpecialAttackSystem  # if not already imported

    player1_bricks = 0
    player2_bricks = 0
    player1_has_special = False
    player2_has_special = False
    special_attack = SpecialAttackSystem()

    victoires_p1 = 0
    victoires_p2 = 0
    manche_terminee = False

    while True:
        # 1) Cap to 230 FPS
        time.Clock().tick(230)

        # 2) Handle quit & special‐attack key events
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                return  # or quit()

            # feed key‐downs into the SpecialAttackSystem
            special_used = special_attack.handle_event(
                ev,
                player1_has_special, player2_has_special,
                xp, yp, xp2, yp2
            )
            if special_used:
                # consume the special for whomever fired
                if special_attack.charging_player == 1:
                    player1_has_special = False
                else:
                    player2_has_special = False

        # 3) While charging, let the player re‐aim the arrow
        special_attack.update_charging(pygame.key.get_pressed())

        # 4) Draw the world
        fenetre.blit(fond, (0, 0))
        fenetre.blit(perso1, (xp, yp))
        fenetre.blit(perso2, (xp2, yp2))

        for ligne in range(13):
            for col in range(13):
                val = matrice[1 + ligne][1 + col]
                if val >= 2:
                    fenetre.blit(
                        liste_im[int(val) - 2],
                        (col * 40 + 40, ligne * 40 + 40)
                    )


        # 🧠 ADD THESE:
        # Replace your current text rendering code with:
        text1 = font.render(f'Bricks P1: {player1_bricks}/5', True, (255, 255, 255))
        text2 = font.render(f'Bricks P2: {player2_bricks}/5', True, (255, 255, 255))
        text_special1 = font.render('SPECIAL!' if player1_has_special else '', True, (255, 215, 0))
        text_special2 = font.render('SPECIAL!' if player2_has_special else '', True, (255, 215, 0))

        # Show the score
        score_text = font.render(f'Score - P1: {victoires_p1} | P2: {victoires_p2}', True, (255, 255, 255))
        fenetre.blit(score_text, (200, 70))

        # Blit the counters and indicators onto the screen
        fenetre.blit(text1, (20, 10))  # Position for Player 1's brick counter
        fenetre.blit(text_special1, (20, 40))  # Position for Player 1's special attack indicator
        fenetre.blit(text2, (450, 10))  # Position for Player 2's brick counter
        fenetre.blit(text_special2, (450, 40))  # Position for Player 2's special attack indicator


        # Draw special attack visuals
        special_attack.draw(fenetre, xp, yp, xp2, yp2)

        display.flip()


        # attaque:

        keyb = key.get_pressed()
        # Player 2 bomb placement
        if keyb[K_e] and not (special_attack.charging or special_attack.is_active):
            if len(liste_bombes) <= 3:
                matrice[int((yp2 + 20) // 40)][int((xp2 + 20) // 40)] = 3.5
                bomb_position = [int((xp2 + 20) // 40), int((yp2 + 20) // 40), 300]
                liste_bombes.append(bomb_position)
                liste_bombes_p2.append(bomb_position)  # Track ownership

        # Player 1 bomb placement
        if keyb[K_RSHIFT] and not (special_attack.charging or special_attack.is_active):
            if len(liste_bombes) <= 3:
                matrice[int((yp + 20) // 40)][int((xp + 20) // 40)] = 3.5
                bomb_position = [int((xp + 20) // 40), int((yp + 20) // 40), 300]
                liste_bombes.append(bomb_position)
                liste_bombes_p1.append(bomb_position)  # Track ownership


        # gestion des bombes
        # Bomb management
        # Bomb management
        for bombes in liste_bombes:
            bombes[2] -= 1
            if bombes[2] == 150:
                matrice[bombes[1]][bombes[0]] = 3
            if bombes[2] == 0:
                matrice[bombes[1]][bombes[0]] = 0
                liste_bombes.remove(bombes)
                matrice[bombes[1]][bombes[0]] = 4
                feu = [59, (bombes[0], bombes[1], 0)]
                for i in range(1, 3):
                    if matrice[bombes[1] - i][bombes[0]] == 2:
                        matrice[bombes[1] - i][bombes[0]] = 4
                        feu.append((bombes[0], bombes[1] - i, int(randint(1, chance_b_f) == 1)))
                        explosion_bombe.play()
                        # Increment brick counter for the correct player
                        if bombes in liste_bombes_p1:
                            player1_bricks += 1
                        elif bombes in liste_bombes_p2:
                            player2_bricks += 1
                        break
                    elif matrice[bombes[1] - i][bombes[0]] == 0:
                        matrice[bombes[1] - i][bombes[0]] = 4
                        feu.append((bombes[0], bombes[1] - i, 0))
                        explosion_bombe.play()
                    elif matrice[bombes[1] - i][bombes[0]] in [3, 3.5]:
                        for bombe2 in liste_bombes:
                            if bombe2[0] == bombes[0] and bombes[1] - i == bombe2[1]:
                                bombe2[2] = 1
                                explosion_bombe.play()
                                break
                    else:
                        break

                for i in range(1, 3):
                    if matrice[bombes[1] + i][bombes[0]] == 2:
                        matrice[bombes[1] + i][bombes[0]] = 4
                        feu.append((bombes[0], bombes[1] + i, int(randint(1, chance_b_f) == 1)))
                        explosion_bombe.play()
                        if bombes in liste_bombes_p1:
                            player1_bricks += 1
                        elif bombes in liste_bombes_p2:
                            player2_bricks += 1
                        break
                    if matrice[bombes[1] + i][bombes[0]] == 0:
                        matrice[bombes[1] + i][bombes[0]] = 4
                        feu.append((bombes[0], bombes[1] + i, 0))
                        explosion_bombe.play()
                    else:
                        break
                for i in range(1, 3):
                    if matrice[bombes[1]][bombes[0] + i] == 2:
                        matrice[bombes[1]][bombes[0] + i] = 4
                        feu.append((bombes[0] + i, bombes[1], int(randint(1, chance_b_f) == 1)))
                        explosion_bombe.play()
                        if bombes in liste_bombes_p1:
                            player1_bricks += 1
                        elif bombes in liste_bombes_p2:
                            player2_bricks += 1
                        break
                    if matrice[bombes[1]][bombes[0] + i] == 0:
                        matrice[bombes[1]][bombes[0] + i] = 4
                        feu.append((bombes[0] + i, bombes[1], 0))
                        explosion_bombe.play()
                    else:
                        break
                for i in range(1, 3):
                    if matrice[bombes[1]][bombes[0] - i] == 2:
                        matrice[bombes[1]][bombes[0] - i] = 4
                        feu.append((bombes[0] - i, bombes[1], int(randint(1, chance_b_f) == 1)))
                        explosion_bombe.play()
                        if bombes in liste_bombes_p1:
                            player1_bricks += 1
                        elif bombes in liste_bombes_p2:
                            player2_bricks += 1
                        break
                    if matrice[bombes[1]][bombes[0] - i] == 0:
                        matrice[bombes[1]][bombes[0] - i] = 4
                        feu.append((bombes[0] - i, bombes[1], 0))
                        explosion_bombe.play()
                    else:
                        break
                liste_f.append(feu)

        # gestion des bonus
        if matrice[int((yp + 20) // 40)][int((xp + 20) // 40)] == 5:
            vitesse1 *= 1.25
            matrice[int((yp + 20) // 40)][int((xp + 20) // 40)] = 0
        if matrice[int((yp2 + 20) // 40)][int((xp2 + 20) // 40)] == 5:
            vitesse2 *= 1.25
            matrice[int((yp2 + 20) // 40)][int((xp2 + 20) // 40)] = 0
        #

        # gestion des flammes
        for feu in liste_f:
            feu[0] -= 1
            if feu[0] == 0:
                for couple in feu[1:]:
                    matrice[couple[1]][couple[0]] = couple[2] * 5
                liste_f.remove(feu)

        # 💣 Gestion des explosions de projectiles spéciaux
        # In the projectile explosion handling:
        for explosion in special_attack.update_projectiles(matrice):
            ex, ey, owner = explosion
            feu_entry = [59]
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    cx = int((ex + dx * 40) // 40)
                    cy = int((ey + dy * 40) // 40)
                    if 0 <= cx < 15 and 0 <= cy < 15:
                        # Only destroy breakable blocks (2) and empty spaces (0)
                        if matrice[cy][cx] in [0, 2]:
                            matrice[cy][cx] = 4
                            feu_entry.append((cx, cy, int(randint(1, chance_b_f) == 1)))
                            # Count destroyed bricks

            liste_f.append(feu_entry)
            explosion_bombe.play()



        # gestion de la vie:
        if matrice[int((yp + 20) // 40)][int((xp + 20) // 40)] == 4:  # si le feu est touche
            vie1 -= 1
        if matrice[int((yp2 + 20) // 40)][int((xp2 + 20) // 40)] == 4:
            vie2 -= 1

        if vie1 < 1:
            fin = 0  # fin du jeu
        if vie2 < 1:
            fin = -1

        # === Special Attack Unlock ===
        if not player1_has_special and player1_bricks >= 5:
            player1_has_special = True
            player1_bricks = 0  # Reset counter

        if not player2_has_special and player2_bricks >= 5:
            player2_has_special = True
            player2_bricks = 0  # Reset counter



        # deplacement:

        # perso 1 movement - Modified with special attack immobilization
        keyb = key.get_pressed()
        player1_can_move = not (
                    special_attack.charging and special_attack.charging_player == 1) and not special_attack.is_active
        if player1_can_move:
            if keyb[K_UP]:
                if matrice[int((yp + 0) // 40)][int((xp + 20) // 40)] in [0, 3.5, 5]:
                    yp -= vitesse1
                    if xp % 40 <= 20 and xp % 40 != 0: xp -= 1
                    if xp % 40 > 20 and xp % 40 != 0: xp += 1
            if keyb[K_DOWN]:
                if matrice[int((yp + 40) // 40)][int((xp + 20) // 40)] in [0, 3.5, 5]:
                    yp += vitesse1
                    if xp % 40 <= 20 and xp % 40 != 0: xp -= 1
                    if xp % 40 > 20 and xp % 40 != 0: xp += 1
            if keyb[K_LEFT]:
                if matrice[int((yp + 20) // 40)][int((xp + 0) // 40)] in [0, 3.5, 5]:
                    xp -= vitesse1
                    if yp % 40 <= 20 and yp % 40 != 0: yp -= 1
                    if yp % 40 > 20 and yp % 40 != 0: yp += 1
            if keyb[K_RIGHT]:
                if matrice[int((yp + 20) // 40)][int((xp + 40) // 40)] in [0, 3.5, 5]:
                    xp += vitesse1
                    if yp % 40 <= 20 and yp % 40 != 0: yp -= 1
                    if yp % 40 > 20 and yp % 40 != 0: yp += 1

        # perso 2 movement - Modified with special attack immobilization
        player2_can_move = not (
                    special_attack.charging and special_attack.charging_player == 2) and not special_attack.is_active
        if player2_can_move:
            if keyb[K_w]:
                if matrice[int((yp2 + 0) // 40)][int((xp2 + 20) // 40)] in [0, 3.5, 5]:
                    yp2 -= vitesse2
                    if xp2 % 40 <= 20 and xp2 % 40 != 0: xp2 -= 1
                    if xp2 % 40 > 20 and xp2 % 40 != 0: xp2 += 1
            if keyb[K_s]:
                if matrice[int((yp2 + 40) // 40)][int((xp2 + 20) // 40)] in [0, 3.5, 5]:
                    yp2 += vitesse2
                    if xp2 % 40 <= 20 and xp2 % 40 != 0: xp2 -= 1
                    if xp2 % 40 > 20 and xp2 % 40 != 0: xp2 += 1
            if keyb[K_d]:
                if matrice[int((yp2 + 20)) // 40][int((xp2 + 40) // 40)] in [0, 3.5, 5]:
                    xp2 += vitesse2
                    if yp2 % 40 <= 20 and yp2 % 40 != 0: yp2 -= 1
                    if yp2 % 40 > 20 and yp2 % 40 != 0: yp2 += 1
            if keyb[K_a]:
                if matrice[int((yp2 + 20) // 40)][int((xp2 + 0) // 40)] in [0, 3.5, 5]:
                    xp2 -= vitesse2
                    if yp2 % 40 <= 20 and yp2 % 40 != 0: yp2 -= 1
                    if yp2 % 40 > 20 and yp2 % 40 != 0: yp2 += 1

        if vie1 < 1: vie1 -= 1
        if vie2 < 1: vie2 -= 1
        if vie1 <= -30 or vie2 <= -30:
            if vie1 <= 0:
                for i in range(5):
                    fenetre.blit(anim[i], (xp, yp))
                    display.flip()
                    time.wait(100)
            if vie2 <= 0:
                for i in range(5):
                    fenetre.blit(anim[i], (xp2, yp2))
                    display.flip()
                    time.wait(100)

            while True:  # affichage et reinitialisation du jeu

                fenetre.blit(lafin[-fin], (0, 0))
                display.flip()
                for evenements in event.get(): pass
                keyb = key.get_pressed()
                if keyb[K_SPACE]:
                    matrice = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                               [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
                    xp = 80
                    yp = 40
                    xp2 = 520
                    yp2 = 520
                    collision = 1
                    continuer = 0
                    liste_bombes = []
                    liste_f = []
                    vie1 = 1
                    vie2 = 1
                    fin = 1
                    anim = [a1, a2, a3, a4, a5]
                    chance_b_f = 3
                    vitesse1 = 1
                    vitesse2 = 1

                    player1_bricks = 0
                    player2_bricks = 0
                    player1_has_special = False
                    player2_has_special = False
                    special_attack = SpecialAttackSystem()

                    for l in range(len(matrice)):
                        for c in range(len(matrice[0])):
                            if l + c >= 4 and l + c <= 24:
                                if matrice[l][c] == 0:
                                    if randint(1, 10) >= 6:
                                        matrice[l][c] = 2

                    break
        display.flip()

    # Détection de fin de manche
    if vie1 <= 0 and not manche_terminee:
        victoires_p2 += 1
        manche_terminee = True
        pygame.time.wait(2000)
    elif vie2 <= 0 and not manche_terminee:
        victoires_p1 += 1
        manche_terminee = True
        pygame.time.wait(2000)

    # Affichage du score
    score_text = font.render(f"Score - P1: {victoires_p1} | P2: {victoires_p2}", True, (255, 255, 255))
    fenetre.blit(score_text, (200, 70))

    # Vérifie si un joueur a gagné 3 manches
    if victoires_p1 == 3:
        fin_text = font.render("JOUEUR 1 GAGNE LA PARTIE !", True, (0, 255, 0))
        fenetre.blit(fin_text, (120, 300))
        display.flip()
        pygame.time.wait(5000)
        pygame.quit()
        return

    if victoires_p2 == 3:
        fin_text = font.render("JOUEUR 2 GAGNE LA PARTIE !", True, (0, 255, 0))
        fenetre.blit(fin_text, (120, 300))
        display.flip()
        pygame.time.wait(5000)
        pygame.quit()
        return

    # Réinitialisation de la manche
    if manche_terminee:
        start_bomberman(surface, show_path, player_alg, en1_alg, en2_alg, en3_alg, tile_size)
        return

    pygame.quit()

if __name__ == "__main__":
    pass

