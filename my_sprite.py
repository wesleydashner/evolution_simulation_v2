import pygame
import math


class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        delta_x, delta_y = self.get_deltas(45, 5)
        self.rect.x += delta_x
        self.rect.y += delta_y

    def get_deltas(self, angle, speed):
        radians = angle * math.pi / 180
        return speed * math.cos(radians), speed * math.sin(radians)
