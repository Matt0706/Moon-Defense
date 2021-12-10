import pygame
import MoonDefense
import color
import random


class Enemy(pygame.sprite.Sprite):

    health = 100

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(color.RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-500, -50)
        self.rect.y = random.randint(105, 125)
        self.velx = 0
        self.vely = 0
        self.damage = 1
        self.speed = 2

    # Moves the enemy along the path, needs to be copied for different paths
    def move1(self):
        if self.velx == 0 and self.vely == 0:
            self.velx = self.speed
        if random.randrange(650, 680) <= self.rect.x and 100 \
                <= self.rect.y <= 150:
            self.velx = 0
            self.vely = self.speed
        if 650 <= self.rect.x <= 700 and random.randrange(320, 350) \
                <= self.rect.y <= 370:
            self.velx = -self.speed
            self.vely = 0
        if 210 <= self.rect.x <= random.randrange(210, 240) and 320 \
                <= self.rect.y <= 370:
            self.velx = 0
            self.vely = self.speed
        if 210 <= self.rect.x <= 240 and self.rect.y >= \
                random.randrange(650, 680):
            self.velx = self.speed
            self.vely = 0

    def update(self):
        if MoonDefense.Game.world == 1:
            self.move1()
        self.rect.x += self.velx
        self.rect.y += self.vely


class Alien(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 200
        self.damage = 5
        self.speed = random.randrange(2, 3)
        self.image = pygame.Surface([20, 39])
        self.sprite = pygame.image.load("images/aliensprite.jpg").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.sprite, [0, 0])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-500, -50)
        self.rect.y = random.randint(105, 125)


class Dog(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.damage = 2
        self.speed = 5
        self.speed = random.randrange(3, 5)
        self.image = pygame.Surface([40, 24])
        self.sprite = pygame.image.load("images/dogsprite.jpg").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.sprite, [0, 0])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-500, -50)
        self.rect.y = random.randint(105, 125)


class Ship(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 750
        self.damage = 10
        self.speed = random.randrange(1, 2)
        self.image = pygame.Surface([40, 32])
        self.sprite = pygame.image.load("images/shipsprite.jpg").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.sprite, [0, 0])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-500, -50)
        self.rect.y = random.randint(105, 125)
