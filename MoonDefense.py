"""
Matthew Medina
Moon Defense Game
Beta Version

Known bugs:

Needed to be added:


Slow Grind by Ron Gelinas Chillout Lounge |
https://soundcloud.com/atmospheric-music-portal
Creative Commons Attribution 3.0 Unported License
https://creativecommons.org/licenses/by/3.0/deed.en_US
Music promoted by https://www.chosic.com/free-music/all/
"""

import Enemy
import Icon
import Troop
from menu import *

# Set the screen width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


# Set some sounds


# The object for the base
class Base(pygame.sprite.Sprite):
    # The object for the base which enemies will travel to
    health = 100

    def __init__(self):
        super().__init__()
        self.x = 500
        self.y = 500

        self.image = pygame.Surface([118, 168])
        self.sprite = pygame.image.load("images/dish.jpg").convert()
        self.image.set_colorkey(WHITE)
        self.image.blit(self.sprite, [0, 0])
        self.rect = self.image.get_rect()
        self.rect.x = 866
        self.rect.y = 591


class Path(pygame.sprite.Sprite):
    # The object for one piece of the path
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill((200, 125, 125))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100


# Displays health on the top of the screen
def display_health(screen):
    pygame.draw.rect(screen, GREEN, [380, 20, 150, 50])
    health_str = "Health: " + str(Base.health)
    font = pygame.font.SysFont("serif", 25)
    text = font.render(health_str, True, BLACK)
    screen.blit(text, [385, 25])


class Game:
    all_sprites_list = None

    game_over = False
    gold = 200
    base = None
    wave = 0
    world = 1

    def __init__(self):
        self.alien = Enemy.Alien()
        self.enemies = pygame.sprite.Group()
        self.enemy = Enemy.Enemy()
        self.game_over = False
        self.all_sprites_list = pygame.sprite.Group()
        self.base = Base()
        self.purchasing = False
        self.troops_list = pygame.sprite.Group()
        self.wave_button = pygame.Rect(600, 20, 150, 50)
        self.shop = pygame.Rect([900, 20, 200, 400])
        self.blaster_button = pygame.Rect([925, 45, 150, 100])
        self.rocket_button = pygame.Rect([925, 170, 150, 100])
        self.miner_button = pygame.Rect([925, 295, 150, 100])
        self.blasterIcon = Icon.BlasterIcon()
        self.rocketIcon = Icon.RocketIcon()
        self.minerIcon = Icon.MinerIcon()
        self.holdingBlaster = False
        self.holdingRocket = False
        self.holdingMiner = False

    # Creates the world by placing the path
    # Can be expanded by checking the world parameter of the Game class
    def draw_path(self):
        step = 55
        for i in range(3):
            path = Path()
            path.rect.x -= i * step
            self.all_sprites_list.add(path)
        for i in range(11):
            path = Path()
            path.rect.x += i * step
            self.all_sprites_list.add(path)
        for i in range(4):
            path = Path()
            path.rect.x += 10 * step
            path.rect.y += step
            path.rect.y += i * step
            self.all_sprites_list.add(path)
        for i in range(8):
            path = Path()
            path.rect.x = 45 + 10 * step
            path.rect.x -= i * step
            path.rect.y = 320
            self.all_sprites_list.add(path)
        for i in range(6):
            path = Path()
            path.rect.x += 2 * step
            path.rect.y = 375
            path.rect.y += i * step
            self.all_sprites_list.add(path)
        for i in range(11):
            path = Path()
            path.rect.x += 3 * step
            path.rect.x += i * step
            path.rect.y = 320 + (6 * step)
            self.all_sprites_list.add(path)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
                self.click(pygame.mouse.get_pos()[0],
                           pygame.mouse.get_pos()[1])
        return False

    def click(self, x, y):
        if self.holdingBlaster:
            if not self.shop.collidepoint(x, y):
                self.buy_blaster()
            self.all_sprites_list.remove(self.blasterIcon)
            self.holdingBlaster = False
        if self.holdingRocket:
            if not self.shop.collidepoint(x, y):
                self.buy_rocket()
            self.all_sprites_list.remove(self.rocketIcon)
            self.holdingRocket = False
        if self.holdingMiner:
            if not self.shop.collidepoint(x, y):
                self.buy_miner()
            self.all_sprites_list.remove(self.minerIcon)
            self.holdingMiner = False
        if self.wave_button.collidepoint(x, y):
            self.new_wave()
        elif self.blaster_button.collidepoint(x, y):
            if self.gold >= Troop.Blaster.cost:
                if not self.holdingBlaster or self.holdingRocket or \
                        self.holdingMiner:
                    self.all_sprites_list.add(self.blasterIcon)
                    self.holdingBlaster = True
        if self.rocket_button.collidepoint(x, y):
            if self.gold >= Troop.Rocket.cost:
                if not self.holdingBlaster or self.holdingRocket or \
                        self.holdingMiner:
                    self.all_sprites_list.add(self.rocketIcon)
                    self.holdingRocket = True
        if self.miner_button.collidepoint(x, y):
            if self.gold >= Troop.Miner.cost:
                if not self.holdingBlaster or self.holdingRocket or \
                        self.holdingMiner:
                    self.all_sprites_list.add(self.minerIcon)
                    self.holdingMiner = True

    # Draws and updates sprites
    def draw_sprites(self):
        self.draw_path()
        self.all_sprites_list.add(self.base)
        self.all_sprites_list.update()

    # Checks if troops need to attack, if enemies died or made it to the end
    def run_logic(self):
        if not self.game_over:
            self.all_sprites_list.update()
        if Base.health <= 0:
            self.game_over = True
        enemies_at_base = pygame.sprite.spritecollide(Base(),
                                                      self.enemies, True)
        for enemy in enemies_at_base:
            Base.health -= enemy.damage
        for troop in self.troops_list:
            enemiesInRange = 0
            for enemy in self.enemies:
                if (enemy.rect.x + 200 >= troop.rect.x >=
                    enemy.rect.x - 200) and (enemy.rect.y + 200 >=
                                             troop.rect.y >=
                                             enemy.rect.y - 200):
                    enemiesInRange += 1
            for enemy in self.enemies:
                if (enemy.rect.x + 200 >= troop.rect.x >=
                    enemy.rect.x - 200) and (enemy.rect.y + 200 >=
                                             troop.rect.y >=
                                             enemy.rect.y - 200):
                    troop.attack(enemy, enemiesInRange)
                    if type(troop) == Troop.Miner:
                        if enemy.health < 1:
                            self.gold += 5
        for enemy in self.enemies:
            if enemy.health < 1:
                self.enemies.remove(enemy)
                self.all_sprites_list.remove(enemy)
                self.gold += 10

    # Handles drawing to the screen and flipping the front and back buffers
    def display_frame(self, screen):
        background = pygame.image.load("images/moonsurface.jpg").convert()
        screen.fill(WHITE)
        screen.blit(background, [0, 0])
        if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            if self.wave == 1:
                text = font.render("Game Over, you survived " +
                                   str(self.wave) +
                                   " wave! Click to Restart.", True, BLACK)
            else:
                text = font.render("Game Over, you survived " +
                                   str(self.wave) +
                                   " waves! Click to Restart.", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
        if not self.game_over:
            self.all_sprites_list.draw(screen)
            self.display_feedback(screen)
        pygame.display.flip()

    # Displays all other stats and buttons to the screen
    def display_feedback(self, screen):
        self.display_gold(screen)
        self.display_wave(screen)
        display_health(screen)
        self.display_next_wave(screen)
        self.display_shop(screen)

    def display_gold(self, screen):
        pygame.draw.rect(screen, YELLOW, [20, 20, 150, 50])
        gold_str = "Gold: " + str(self.gold)
        font = pygame.font.SysFont("serif", 25)
        text = font.render(gold_str, True, BLACK)
        screen.blit(text, [25, 25])

    def display_wave(self, screen):
        pygame.draw.rect(screen, GREY, [200, 20, 110, 50])
        wave_str = "Wave: " + str(self.wave)
        font = pygame.font.SysFont("serif", 25)
        text = font.render(wave_str, True, BLACK)
        screen.blit(text, [205, 25])

    def display_next_wave(self, screen):
        shade = GREY
        if not self.enemies:
            shade = RED
        font = pygame.font.SysFont("Serif", 25)
        txt = font.render("Next Wave", True, BLACK)
        pygame.draw.rect(screen, shade, self.wave_button)
        screen.blit(txt, [605, 25])

    def buy_blaster(self):
        buy_sound = pygame.mixer.Sound("sounds/purchase.wav")
        pygame.mixer.Sound.play(buy_sound)
        mx, my = pygame.mouse.get_pos()
        blaster = Troop.Blaster()
        blaster.rect.x = mx
        blaster.rect.y = my
        self.all_sprites_list.add(blaster)
        self.gold -= blaster.cost
        self.purchasing = False
        self.troops_list.add(blaster)

    def buy_rocket(self):
        buy_sound = pygame.mixer.Sound("sounds/purchase.wav")
        pygame.mixer.Sound.play(buy_sound)
        mx, my = pygame.mouse.get_pos()
        rocket = Troop.Rocket()
        rocket.rect.x = mx
        rocket.rect.y = my
        self.all_sprites_list.add(rocket)
        self.gold -= rocket.cost
        self.purchasing = False
        self.troops_list.add(rocket)

    def buy_miner(self):
        buy_sound = pygame.mixer.Sound("sounds/purchase.wav")
        pygame.mixer.Sound.play(buy_sound)
        mx, my = pygame.mouse.get_pos()
        miner = Troop.Miner()
        miner.rect.x = mx
        miner.rect.y = my
        self.all_sprites_list.add(miner)
        self.gold -= miner.cost
        self.purchasing = False
        self.troops_list.add(miner)

    # Creates new enemies based on the wave number
    def new_wave(self):
        if not self.enemies:
            self.wave += 1
            for i in range(self.wave):
                newAlien = Enemy.Alien()
                self.enemies.add(newAlien)
                self.all_sprites_list.add(newAlien)
            for i in range(self.wave):
                if i > 2:
                    newDog = Enemy.Dog()
                    self.enemies.add(newDog)
                    self.all_sprites_list.add(newDog)
            newShip = Enemy.Ship()
            if self.wave > 10:
                shipAmount = self.wave - 5 // 5
                for _ in range(shipAmount):
                    self.enemies.add(newShip)
                    self.all_sprites_list.add(newShip)

    # Displays the shop and handles mouse clicks on the buttons
    def display_shop(self, screen):
        font = pygame.font.SysFont("Serif", 25)
        pygame.draw.rect(screen, GREY, [900, 20, 200, 400])
        pygame.draw.rect(screen, LIGHTGREY, self.blaster_button)
        pygame.draw.rect(screen, LIGHTGREY, self.rocket_button)
        pygame.draw.rect(screen, LIGHTGREY, self.miner_button)
        blasterTxt = font.render("Blaster: " + str(Troop.Blaster.cost),
                                 True, BLACK)
        rocketTxt = font.render("Rocket: " + str(Troop.Rocket.cost),
                                True, BLACK)
        minerTxt = font.render("Miner: " + str(Troop.Miner.cost),
                               True, BLACK)
        screen.blit(blasterTxt, [930, 60])
        screen.blit(rocketTxt, [930, 180])
        screen.blit(minerTxt, [930, 300])


def main():
    menu()
    pygame.init()
    pygame.mixer.init(44100, 16, 2, 4096)
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Moon Defense")
    pygame.mouse.set_visible(True)

    done = False
    clock = pygame.time.Clock()

    game = Game()

    # Spawn in path and enemies
    game.draw_sprites()

    while not done:
        # process events
        done = game.process_events()
        # update objects
        game.run_logic()
        # draw the frame
        game.display_frame(screen)

        # wait for next frame
        clock.tick(60)

    # Quit when done
    pygame.quit()


# Call the main function
if __name__ == "__main__":
    main()
