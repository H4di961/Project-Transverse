import pygame
from pygame.locals import *
import math

class Projectile:
    def __init__(
        self, x, y, dx, dy, power, owner,
        mass=1.0, lifetime_s=2.0, drag=0.8, speed_mul=8.0
    ):
        # dt tick
        self.dt = 1.0 / 230
        self.mass = mass
        self.drag = drag

        # pos
        self.x, self.y = x, y
        # initial speed
        v0 = (power * speed_mul) / self.mass
        self.vx = dx * v0
        self.vy = dy * v0

        # lifespan in frames
        self.lifetime = int(lifetime_s / self.dt)
        self.owner = owner
        self.angle = 0
        self.update_angle()

    def update(self, matrice):
        # apply drag
        f = max(0.0, 1 - self.drag * self.dt)
        self.vx *= f; self.vy *= f

        # move
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt

        # bounds check
        if not (0 <= self.x <= 600 and 0 <= self.y <= 600):
            return True

        self.update_angle()
        # decay
        self.lifetime -= 1
        return self.lifetime <= 0

    def update_angle(self):
        if not (self.vx or self.vy):
            return
        # orient
        self.angle = math.degrees(math.atan2(-self.vy, self.vx))


class SpecialAttackSystem:
    def __init__(self):
        self.projectiles = []
        self.charging = False
        self.charging_player = 0
        self.charge_dx = 1
        self.charge_dy = 0
        self.is_active = False

        # images
        arrow = pygame.image.load("arrow/arrow.png").convert_alpha()
        self.arrow_img = pygame.transform.scale(arrow, (30, 30))
        bomb = pygame.image.load("bomb/specialbomb.png").convert_alpha()
        self.bomb_img = pygame.transform.scale(bomb, (40, 40))

    def handle_event(
        self, ev,
        p1_has_special, p2_has_special,
        p1_x, p1_y, p2_x, p2_y
    ):
        if ev.type == KEYDOWN:
            if ev.key == K_LSHIFT and p1_has_special:
                if not self.charging:
                    self.charging = True
                    self.charging_player = 1
                    self.charge_dx, self.charge_dy = 1, 0
                    return False
                elif self.charging_player == 1:
                    return self.fire(p1_x, p1_y)

            elif ev.key == K_r and p2_has_special:
                if not self.charging:
                    self.charging = True
                    self.charging_player = 2
                    self.charge_dx, self.charge_dy = 1, 0
                    return False
                elif self.charging_player == 2:
                    return self.fire(p2_x, p2_y)

        return False

    def fire(self, x, y):
        mag = math.hypot(self.charge_dx, self.charge_dy)
        if not mag:
            return False
        dx, dy = self.charge_dx / mag, self.charge_dy / mag
        proj = Projectile(
            x + 20, y + 20,
            dx, dy,
            power=25,
            owner=self.charging_player,
            lifetime_s=2.0,
            drag=0.8,
            speed_mul=8.0
        )
        self.projectiles.append(proj)
        self.charging = False
        return True

    def update_charging(self, keys):
        if not self.charging:
            return

        dx = dy = 0
        if self.charging_player == 1:
            if keys[K_UP]:    dy -= 1
            if keys[K_DOWN]:  dy += 1
            if keys[K_LEFT]:  dx -= 1
            if keys[K_RIGHT]: dx += 1
        else:
            if keys[K_w]:     dy -= 1
            if keys[K_s]:     dy += 1
            if keys[K_a]:     dx -= 1
            if keys[K_d]:     dx += 1

        if dx or dy:
            mag = math.hypot(dx, dy)
            self.charge_dx = dx / mag
            self.charge_dy = dy / mag

    def update_projectiles(self, matrice):
        self.is_active = bool(self.projectiles)
        for proj in self.projectiles[:]:
            if proj.update(matrice):
                self.projectiles.remove(proj)
                yield (proj.x, proj.y, proj.owner)

    def draw(self, surface, p1_x, p1_y, p2_x, p2_y):
        for proj in self.projectiles:
            rot = pygame.transform.rotate(self.bomb_img, proj.angle)
            r = rot.get_rect(center=(proj.x, proj.y))
            surface.blit(rot, r)

        if self.charging:
            cx, cy = (
                (p1_x + 20, p1_y + 20)
                if self.charging_player == 1
                else (p2_x + 20, p2_y + 20)
            )
            ang = math.degrees(math.atan2(-self.charge_dy, self.charge_dx))
            arrow = pygame.transform.rotate(self.arrow_img, ang)
            ar = arrow.get_rect(center=(cx, cy))
            surface.blit(arrow, ar)
