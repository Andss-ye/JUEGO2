import pygame
from global_Var import *
from bullet import *

class Player(pygame.sprite.Sprite):
    def __init__(self, bullets, enemys, screen):
        super().__init__()
        self.bullets = bullets
        self.enemys = enemys
        self.screen = screen
        original_image = pygame.image.load("img/player.png")
        original_image.set_colorkey(black)
        self.image = pygame.transform.scale(original_image, (70, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height - 10
        self.speed_x = 0
        self.speed_y = 0  # Agregamos velocidad vertical
        self.health = 100
        self.health_color = (0, 255, 0)  
        heart_image = pygame.image.load("img/heart.webp")  
        self.heart_image = pygame.transform.scale(heart_image, (50,50))
        self.heart_rect = self.heart_image.get_rect()
        self.heart_rect.x = 30
        self.heart_rect.y = 10

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y  # Actualizamos la posición vertical

        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

        if self.health <= 50:
            self.health_color = (255, 165, 0)
        if self.health <= 20:
            self.health_color = (255, 0, 0)

    def move_left(self):
        self.speed_x = -7

    def move_right(self):
        self.speed_x = 7

    def move_up(self):
        self.speed_y = -7

    def move_down(self):
        self.speed_y = 7

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0

    def shoot(self):
        speed_y = -10  
        bullet = Bullet(self.rect.centerx, self.rect.top, speed_y)
        self.bullets.add(bullet)


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def draw_health(self):
        pygame.draw.rect(self.screen, self.health_color, (10, 10, self.health, 20))
        self.screen.blit(self.heart_image, (self.heart_rect.x + self.health + 10, self.heart_rect.y))
