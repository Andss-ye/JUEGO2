import pygame
import math
from global_Var import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_x = 0
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.bottom < 0 or self.rect.top > height or self.rect.left < 0 or self.rect.right > width:
            self.kill()
