import pygame


class Troop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.attacking = False

    def to_mouse(self):
        mx, my = pygame.mouse.get_pos()
        self.rect.x = mx
        self.rect.y = my

    def update(self):
        pass


class Blaster(Troop):
    cost = 50

    def __init__(self):
        super().__init__()
        self.damage = 4
        self.sprite = pygame.image.load("images/blastersprite.jpg").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.sprite, [0, 0])
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("sounds/blastersound.wav")

    def attack(self, enemy, enemies_in_range):
        if pygame.time.get_ticks() % 6 == 0:
            effect = self.damage / enemies_in_range
            if effect < 1:
                effect = 1
            enemy.health -= effect
            pygame.mixer.Sound.play(self.sound)


class Rocket(Troop):
    cost = 100

    def __init__(self):
        super().__init__()
        self.damage = 20
        self.sprite = pygame.image.load("images/rocketsprite.jpg").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.sprite, [0, 0])
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("sounds/rocketsound.wav")

    def attack(self, enemy, enemies_in_range):
        if pygame.time.get_ticks() % 60 == 0:
            enemy.health -= self.damage - (0 * enemies_in_range)
            pygame.mixer.Sound.play(self.sound)


class Miner(Troop):
    cost = 150

    def __init__(self):
        super().__init__()
        self.damage = 10
        self.sprite = pygame.image.load("images/minersprite.jpg").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.sprite, [0, 0])
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("sounds/minersound.wav")

    def attack(self, enemy, enemies_in_range):
        if pygame.time.get_ticks() % 20 == 0:
            effect = self.damage / enemies_in_range
            if effect < 2:
                effect = 2
            enemy.health -= effect
            pygame.mixer.Sound.play(self.sound)
