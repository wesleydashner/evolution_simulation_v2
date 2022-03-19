import pygame
import sys
from my_sprite import MySprite

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

is_running = True

sprites = pygame.sprite.Group()
sprites.add(MySprite(100, 200, (255, 255, 255), 50))

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 0))
    sprites.update()
    for sprite in sprites:
        sprite.rect.clamp_ip(screen.get_rect())
    sprites.draw(screen)
    pygame.display.update()
