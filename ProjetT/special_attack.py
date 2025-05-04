import pygame
from pygame.locals import *
import math

class Projectile:
    def __init__(self, x, y, dx, dy, power, owner):
        self.x = x
        self.y = y
        self.dx = dx * (power / 25)
        self.dy = dy * (power / 25)
        self.owner = owner
        # At 230 FPS, 1.5 seconds ≈ 345 frames
        self.lifetime = 200
        self.angle = 0
        self.update_angle()

    def update(self, matrice):
        # Move continuously
        self.x += self.dx
        self.y += self.dy

        # Destroy if out of the 600x600 playfield
        if self.x < 0 or self.x > 600 or self.y < 0 or self.y > 600:
            return True

        # Update rotation angle
        self.update_angle()

        # Decrement life; explode when time's up
        self.lifetime -= 1
        return self.lifetime <= 0

    def update_angle(self):
        if self.dx == 0 and self.dy == 0:
            return
        self.angle = math.degrees(math.atan2(-self.dy, self.dx))

class SpecialAttackSystem:
    def __init__(self):
        self.projectiles = []
        self.charging = False
        self.charging_player = 0
        # Direction unit vector for arrow aiming
        self.charge_dx = 1
        self.charge_dy = 0
        self.is_active = False

        # Load images
        arrow = pygame.image.load("arrow.png").convert_alpha()
        self.arrow_img = pygame.transform.scale(arrow, (30, 30))
        bomb = pygame.image.load("specialbomb.png").convert_alpha()
        self.bomb_img = pygame.transform.scale(bomb, (40, 40))

    def handle_event(self, ev, p1_has_special, p2_has_special, p1_x, p1_y, p2_x, p2_y):
        # Start charging for Player 1
        if (ev.type == KEYDOWN and ev.key == K_LSHIFT
                and p1_has_special and not self.charging and not self.is_active):
            self.charging = True
            self.charging_player = 1
            self.charge_dx, self.charge_dy = 1, 0
            return False

        # Start charging for Player 2
        if (ev.type == KEYDOWN and ev.key == K_r
                and p2_has_special and not self.charging and not self.is_active):
            self.charging = True
            self.charging_player = 2
            self.charge_dx, self.charge_dy = 1, 0
            return False

        # Release charge on second key press
        if self.charging and ev.type == KEYDOWN:
            if (self.charging_player == 1 and ev.key == K_LSHIFT) or \
               (self.charging_player == 2 and ev.key == K_r):
                # Determine start position
                sx, sy = (p1_x + 20, p1_y + 20) if self.charging_player == 1 else (p2_x + 20, p2_y + 20)
                # Launch projectile
                self.projectiles.append(
                    Projectile(sx, sy, self.charge_dx, self.charge_dy, power=25, owner=self.charging_player)
                )
                self.charging = False
                return True
        return False

    def update_charging(self, keys):
        if not self.charging:
            return
        dx = dy = 0

        if self.charging_player == 1:
            # Player 1 aims with arrow keys
            if keys[K_UP]:
                dy = -1
            elif keys[K_DOWN]:
                dy = 1
            if keys[K_LEFT]:
                dx = -1
            elif keys[K_RIGHT]:
                dx = 1
        else:
            # Player 2 aims with WASD
            if keys[K_w]:
                dy = -1
            elif keys[K_s]:
                dy = 1
            if keys[K_a]:
                dx = -1
            elif keys[K_d]:
                dx = 1

        # Normalize and store
        if dx != 0 or dy != 0:
            mag = math.hypot(dx, dy)
            self.charge_dx = dx / mag
            self.charge_dy = dy / mag

    def update_projectiles(self, matrice):
        self.is_active = len(self.projectiles) > 0
        for proj in self.projectiles[:]:
            if proj.update(matrice):
                self.projectiles.remove(proj)
                yield (proj.x, proj.y, proj.owner)

    def draw(self, surface, p1_x, p1_y, p2_x, p2_y):
        # Draw active bombs
        for proj in self.projectiles:
            rotated = pygame.transform.rotate(self.bomb_img, proj.angle)
            rect = rotated.get_rect(center=(proj.x, proj.y))
            surface.blit(rotated, rect)

        # Draw aiming arrow
        if self.charging:
            cx, cy = (p1_x + 20, p1_y + 20) if self.charging_player == 1 else (p2_x + 20, p2_y + 20)
            ang = math.degrees(math.atan2(-self.charge_dy, self.charge_dx))
            arrow_rot = pygame.transform.rotate(self.arrow_img, ang)
            arect = arrow_rot.get_rect(center=(cx, cy))
            surface.blit(arrow_rot, arect)
