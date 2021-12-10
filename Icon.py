import pygame


class Icon(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.rect = self.image.get_rect()
        self.there = True

    def update(self):
        if self.there:
            mx, my = pygame.mouse.get_pos()
            self.rect.x = mx
            self.rect.y = my
        if not self.there:
            self.rect.x = -100
            self.rect.y = -100


class BlasterIcon(Icon):

    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load("images/blastersprite.jpg").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.sprite, [0, 0])


class RocketIcon(Icon):

    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load("images/rocketsprite.jpg").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.sprite, [0, 0])


class MinerIcon(Icon):

    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load("images/minersprite.jpg").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.sprite, [0, 0])
