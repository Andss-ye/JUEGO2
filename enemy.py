import pygame
import random
import math
from global_Var import *
from bullet import * 
from player import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, bullets, player_rect):
        super().__init__()
        self.bullets = bullets
        self.player_rect = player_rect
        # Genera un número aleatorio entre 1 y 8 para seleccionar una imagen aleatoria
        random_enemy_number = random.randint(1, 8)
        enemy_image_filename = f"img/enemy ({random_enemy_number}).png"
        
        original_image = pygame.image.load(enemy_image_filename)
        original_image.set_colorkey(black)
        self.image = pygame.transform.scale(original_image, (80, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 5)
        self.speed_x = random.randrange(-5, 5)
        self.health = 20
        self.last_shoot = pygame.time.get_ticks()
        self.shoot_delay = 1000
        self.increased_health = False

    def update(self):
        dx = self.player_rect.centerx - self.rect.centerx
        dy = self.player_rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)
        if distance > 0:
            self.speed_x = dx / distance * 5
            self.speed_y = dy / distance * 5

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 25:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 10)

        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            self.last_shoot = now
            self.shoot()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.bottom + 10, self.speed_y)  # No es necesario pasar player_rect
        self.bullets.add(bullet)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()
            
    def reset_health(self):
        self.health = 20
    
    def increase_health(self, amount):
        self.health += amount
