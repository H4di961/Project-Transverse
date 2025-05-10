# counter.py
import pygame

class MatchCounter:
    def __init__(self, target=3):
        self.target = target
        self.p1 = 0
        self.p2 = 0

    def reset(self):
        """Reset both players’ match scores to zero."""
        self.p1 = 0
        self.p2 = 0

    def add_point(self, winner):
        """Award one point to player `winner` (1 or 2)."""
        if winner == 1:
            self.p1 += 1
        elif winner == 2:
            self.p2 += 1

    def is_over(self):
        """Returns True once either player reaches `target` points."""
        return self.p1 >= self.target or self.p2 >= self.target

    def get_winner(self):
        """Return 1 or 2 when someone has hit the target, else None."""
        if self.p1 >= self.target:
            return 1
        if self.p2 >= self.target:
            return 2
        return None

    def render(self, font, color=(255,255,255)):
        """Return a pygame.Surface of the current score, e.g. "2 – 1"."""
        text = f"{self.p1}  –  {self.p2}"
        return font.render(text, True, color)
