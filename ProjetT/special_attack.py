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
        self.lifetime = 180
        self.angle = 0  # For rotation
        self.update_angle()
        self.is_active = False
        self.delay_counter = 0  # Counter for delayed explosion

    def update(self, matrice):
        self.x += self.dx
        self.y += self.dy

        # Convert position to grid coordinates
        cell_x, cell_y = int(self.x // 40), int(self.y // 40)

        # Check if we're out of bounds
        if cell_x < 0 or cell_x >= 15 or cell_y < 0 or cell_y >= 15:
            self.lifetime = 0  # Destroy projectile
            return True

        # Check collision with walls
        if matrice[cell_y][cell_x] == 1:  # Rock wall
            # Check if this is a border wall
            if cell_y == 0 or cell_y == 14 or cell_x == 0 or cell_x == 14:
                self.lifetime = 0  # Destroy projectile on border walls
                return True
            # For inner rock walls, just slow down and set a delay for explosion
            self.dx *= 0.7
            self.dy *= 0.7
            self.delay_counter = 30  # Set delay for explosion

        elif matrice[cell_y][cell_x] == 2:  # Brick wall
            # Optional: Add brick wall behavior here if needed
            pass

        self.update_angle()
        self.lifetime -= 1

        # Check for delayed explosion
        if self.delay_counter > 0:
            self.delay_counter -= 1
            if self.delay_counter == 0:
                self.lifetime = 0  # Trigger explosion

        return self.lifetime <= 0 or self.x < 0 or self.x > 600 or self.y < 0 or self.y > 600

    def update_angle(self):
        """Calculate rotation angle based on movement direction"""
        if self.dx == 0 and self.dy == 0:
            return
        self.angle = math.degrees(math.atan2(-self.dy, self.dx))

class SpecialAttackSystem:
    def __init__(self):
        self.projectiles = []
        self.charge_power = 0
        self.charging = False
        self.charging_player = 0
        self.charge_dx = 0
        self.charge_dy = 0
        self.is_active = False  # True when projectile is active

        # Load images with error handling
        try:
            self.arrow_img = pygame.transform.scale(
                pygame.image.load("arrow.png").convert_alpha(), (30, 30)
            )
            self.bomb_img = pygame.transform.scale(
                pygame.image.load("specialbomb.jpg").convert_alpha(), (30, 30)
            )
        except pygame.error as e:
            print(f"Error loading images: {e}")
            # Fallback to simple shapes
            self.arrow_img = None
            self.bomb_img = None

    def handle_input(self, keys, player1_has_special, player2_has_special, p1_x, p1_y, p2_x, p2_y):
        # Player 1 special attack (use LEFT SHIFT instead of RIGHT SHIFT to avoid bomb conflict)
        if keys[K_LSHIFT] and player1_has_special and not self.charging and not self.is_active:
            self._handle_charging(keys, 1, K_UP, K_DOWN, K_LEFT, K_RIGHT)
            return False

        # Player 2 special attack (use R instead of e)
        if keys[K_r] and player2_has_special and not self.charging and not self.is_active:
            self._handle_charging(keys, 2, K_w, K_s, K_a, K_d)
            return False

        # Release charged attack
        elif self.charging:
            released = self._release_charge(p1_x, p1_y, p2_x, p2_y)
            if released:
                if self.charging_player == 1:
                    return True  # Signal to consume player 1's special
                else:
                    return True  # Signal to consume player 2's special
        return False

    def _handle_charging(self, keys, player, up_key, down_key, left_key, right_key):
        self.charging = True
        self.charging_player = player
        self.charge_power = min(100, self.charge_power + 2)

        # Get current direction
        self.charge_dx = 0
        self.charge_dy = 0
        if keys[up_key]:
            self.charge_dy = -1
        elif keys[down_key]:
            self.charge_dy = 1
        if keys[left_key]:
            self.charge_dx = -1
        elif keys[right_key]:
            self.charge_dx = 1

        # Normalize direction vector
        magnitude = math.sqrt(self.charge_dx**2 + self.charge_dy**2)
        if magnitude > 0:
            self.charge_dx /= magnitude
            self.charge_dy /= magnitude

    def _release_charge(self, p1_x, p1_y, p2_x, p2_y):
        if self.charge_dx == 0 and self.charge_dy == 0:
            self.charging = False
            return False

        # Create projectile
        if self.charging_player == 1:
            start_x = p1_x + 20
            start_y = p1_y + 20
        else:
            start_x = p2_x + 20
            start_y = p2_y + 20

        self.projectiles.append(Projectile(
            start_x, start_y,
            self.charge_dx, self.charge_dy,
            self.charge_power,
            self.charging_player
        ))

        self.charge_power = 0
        self.charging = False
        return True

    def update_projectiles(self, matrice):
        self.is_active = len(self.projectiles) > 0  # Update active status
        for proj in self.projectiles[:]:
            if proj.update(matrice):
                self.projectiles.remove(proj)
                yield (proj.x, proj.y, proj.owner)

    def draw(self, surface, p1_x, p1_y, p2_x, p2_y):
        # Draw projectiles
        for proj in self.projectiles:
            if self.bomb_img:
                # Rotate and draw bomb image
                rotated_img = pygame.transform.rotate(self.bomb_img, proj.angle)
                img_rect = rotated_img.get_rect(center=(proj.x, proj.y))
                surface.blit(rotated_img, img_rect)
            else:
                # Fallback circle
                pygame.draw.circle(surface, (255, 0, 0), (int(proj.x), int(proj.y)), 5)

        # Draw charging UI
        if self.charging:
            # Get player position
            if self.charging_player == 1:
                x, y = p1_x, p1_y
            else:
                x, y = p2_x, p2_y

            # Draw charge bar
            pygame.draw.rect(surface, (200, 200, 200), (x, y - 30, 40, 5))
            pygame.draw.rect(surface, (0, 255, 0), (x, y - 30, 40 * (self.charge_power / 100), 5))

            # Draw direction arrow
            if self.charge_dx != 0 or self.charge_dy != 0:
                if self.arrow_img:
                    angle = math.degrees(math.atan2(-self.charge_dy, self.charge_dx))
                    rotated_arrow = pygame.transform.rotate(self.arrow_img, angle)
                    arrow_rect = rotated_arrow.get_rect(center=(x + 20, y + 20))
                    surface.blit(rotated_arrow, arrow_rect)
                else:
                    # Fallback arrow
                    end_pos = (x + 20 + self.charge_dx * 30,
                               y + 20 + self.charge_dy * 30)
                    pygame.draw.line(surface, (255, 0, 0),
                                     (x + 20, y + 20), end_pos, 3)
